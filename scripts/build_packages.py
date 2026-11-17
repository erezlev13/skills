#!/usr/bin/env python3
"""Build the reproducible Daily Useful plugin from canonical Visual Response and per-provider sources for the other skills."""

import argparse
import json
import shutil
import zipfile
from pathlib import Path

SKILLS = ("visual-response", "step-by-step", "guiding-questions", "simplify-code")
PROVIDER_SKILLS = SKILLS[1:]
STAMP = (2026, 1, 1, 0, 0, 0)


def source_files(directory):
    files = []
    for path in sorted(directory.rglob("*")):
        relative = path.relative_to(directory)
        if "__pycache__" in relative.parts or path.suffix == ".pyc" or path.name == ".DS_Store":
            continue
        if path.is_symlink():
            raise ValueError(f"Symlinks are not packaged: {path}")
        if path.is_file():
            files.append((relative.as_posix(), path.read_bytes()))
    names = {name for name, _ in files}
    for required in ("SKILL.md", "README.md"):
        if required not in names:
            raise ValueError(f"Missing {required}: {directory}")
    return files


def write_zip(target, entries):
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(entries):
            info = zipfile.ZipInfo(name, STAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    with zipfile.ZipFile(target) as archive:
        if archive.testzip() is not None:
            raise ValueError(f"Corrupt archive: {target}")
        actual = {name: archive.read(name) for name in archive.namelist()}
        if actual != dict(entries):
            raise ValueError(f"Archive contents differ from source: {target}")


def build(root):
    root = Path(root)
    package = root / "packages/daily-useful-plugin"
    manifest = package / "plugin.json"
    metadata = json.loads(manifest.read_text())
    if metadata.get("name") != "daily-useful":
        raise ValueError("Expected daily-useful plugin identity")
    package_readme = (package / "README.md").read_bytes()
    # Read all sources first; an incomplete provider cannot delete the existing package.
    visual = source_files(root / "sources/visual-response")
    sources = {name: (visual if name == "visual-response" else
                     source_files(root / "providers/chatgpt-work" / name)) for name in SKILLS}
    for name in PROVIDER_SKILLS:
        source_files(root / "providers/codex" / name)
    claude_sources = {"visual-response": visual}
    claude_sources.update({name: source_files(root / "providers/claude-code" / name) for name in PROVIDER_SKILLS})
    claude_package = root / "packages/daily-useful-claude"
    claude_readme = (claude_package / "README.md").read_bytes()
    for provider in ("chatgpt-work", "codex", "claude-code"):
        destination = root / "providers" / provider / "visual-response"
        if destination.exists():
            shutil.rmtree(destination)
        for relative, data in visual:
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    generated = package / "skills"
    if generated.exists():
        shutil.rmtree(generated)
    plugin_entries = [("plugin.json", manifest.read_bytes()), ("README.md", package_readme)]
    for name, files in sources.items():
        for relative, data in files:
            target = generated / name / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            plugin_entries.append((f"skills/{name}/{relative}", data))
    write_zip(root / "downloads/daily-useful-plugin.zip", plugin_entries)
    for name, files in sources.items():
        if source_files(generated / name) != files:
            raise ValueError(f"Generated plugin mirror differs: {name}")
    claude_manifest = {key: metadata[key] for key in ("name", "version", "description")}
    claude_manifest.update({key: metadata[key] for key in ("repository", "license") if key in metadata})
    claude_manifest["author"] = {"name": "Erez Lev"}
    manifest_path = claude_package / ".claude-plugin/plugin.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_bytes = (json.dumps(claude_manifest, indent=2) + "\n").encode()
    manifest_path.write_bytes(manifest_bytes)
    generated = claude_package / "skills"
    if generated.exists():
        shutil.rmtree(generated)
    claude_entries = [(".claude-plugin/plugin.json", manifest_bytes), ("README.md", claude_readme)]
    for name, files in claude_sources.items():
        for relative, data in files:
            target = generated / name / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            claude_entries.append((f"skills/{name}/{relative}", data))
        if source_files(generated / name) != files:
            raise ValueError(f"Generated Claude plugin mirror differs: {name}")
    claude_zip = root / "downloads/daily-useful-claude.zip"
    write_zip(claude_zip, claude_entries)
    return [root / "downloads/daily-useful-plugin.zip", claude_zip]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    for artifact in build(args.root):
        print(artifact)
