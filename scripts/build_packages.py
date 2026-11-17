#!/usr/bin/env python3
"""Build the reproducible plugins from canonical Visual Response and per-provider skill sources."""

import argparse
import json
import shutil
import zipfile
from pathlib import Path

PLUGINS = {"daily-useful": ("visual-response", "step-by-step"),
           "simplify": ("guiding-questions", "simplify-code")}
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


def read_plugin(root, name, skills, visual):
    package = root / "packages" / f"{name}-plugin"
    metadata = json.loads((package / "plugin.json").read_text())
    if metadata.get("name") != name:
        raise ValueError(f"Expected {name} plugin identity")
    work_sources, claude_sources = {}, {}
    for skill in skills:
        if skill == "visual-response":
            work_sources[skill] = claude_sources[skill] = visual
            continue
        work_sources[skill] = source_files(root / "providers/chatgpt-work" / skill)
        source_files(root / "providers/codex" / skill)
        claude_sources[skill] = source_files(root / "providers/claude-code" / skill)
    return {"name": name, "metadata": metadata, "work_sources": work_sources, "claude_sources": claude_sources,
            "work_readme": (package / "README.md").read_bytes(),
            "claude_readme": (root / "packages" / f"{name}-claude" / "README.md").read_bytes()}


def mirror_skills(destination, sources):
    if destination.exists():
        shutil.rmtree(destination)
    entries = []
    for name, files in sources.items():
        for relative, data in files:
            target = destination / name / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            entries.append((f"skills/{name}/{relative}", data))
    for name, files in sources.items():
        if source_files(destination / name) != files:
            raise ValueError(f"Generated plugin mirror differs: {destination / name}")
    return entries


def build_plugin(root, plugin):
    name, metadata = plugin["name"], plugin["metadata"]
    package = root / "packages" / f"{name}-plugin"
    work_entries = [("plugin.json", (package / "plugin.json").read_bytes()), ("README.md", plugin["work_readme"])]
    work_entries += mirror_skills(package / "skills", plugin["work_sources"])
    work_zip = root / "downloads" / f"{name}-plugin.zip"
    write_zip(work_zip, work_entries)
    claude_manifest = {key: metadata[key] for key in ("name", "version", "description")}
    claude_manifest.update({key: metadata[key] for key in ("repository", "license") if key in metadata})
    claude_manifest["author"] = {"name": "Erez Lev"}
    claude_package = root / "packages" / f"{name}-claude"
    manifest_path = claude_package / ".claude-plugin/plugin.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_bytes = (json.dumps(claude_manifest, indent=2) + "\n").encode()
    manifest_path.write_bytes(manifest_bytes)
    claude_entries = [(".claude-plugin/plugin.json", manifest_bytes), ("README.md", plugin["claude_readme"])]
    claude_entries += mirror_skills(claude_package / "skills", plugin["claude_sources"])
    claude_zip = root / "downloads" / f"{name}-claude.zip"
    write_zip(claude_zip, claude_entries)
    return [work_zip, claude_zip]


def build(root):
    root = Path(root)
    # Read all sources first; an incomplete provider cannot delete the existing package.
    visual = source_files(root / "sources/visual-response")
    plugins = [read_plugin(root, name, skills, visual) for name, skills in PLUGINS.items()]
    for provider in ("chatgpt-work", "codex", "claude-code"):
        destination = root / "providers" / provider / "visual-response"
        if destination.exists():
            shutil.rmtree(destination)
        for relative, data in visual:
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    return [artifact for plugin in plugins for artifact in build_plugin(root, plugin)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    for artifact in build(args.root):
        print(artifact)
