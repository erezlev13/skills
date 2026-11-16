#!/usr/bin/env python3
"""Build the reproducible Daily Useful plugin from complete provider sources."""

import argparse
import json
import shutil
import zipfile
from pathlib import Path

SKILLS = ("visual-response", "step-by-step")
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
    sources = {name: source_files(root / "providers/chatgpt-work" / name) for name in SKILLS}
    for name in SKILLS:
        source_files(root / "providers/codex" / name)
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
    return [root / "downloads/daily-useful-plugin.zip"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    for artifact in build(args.root):
        print(artifact)
