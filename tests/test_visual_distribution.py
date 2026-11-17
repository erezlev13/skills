"""Catch hand-edited generated copies or a stale committed archive."""
import importlib.util
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_packages", ROOT / "scripts/build_packages.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class VisualDistributionTests(unittest.TestCase):
    def test_generated_visual_sources_match_canonical(self):
        canonical = MODULE.source_files(ROOT / "sources/visual-response")
        for relative in ("providers/chatgpt-work/visual-response",
                         "providers/codex/visual-response",
                         "providers/claude-code/visual-response",
                         "packages/daily-useful-claude/skills/visual-response",
                         "packages/daily-useful-plugin/skills/visual-response"):
            with self.subTest(path=relative):
                self.assertEqual(canonical, MODULE.source_files(ROOT / relative),
                                 "Edit sources/visual-response and rebuild")

    def test_committed_zips_match_complete_packages(self):
        for plugin, skills in MODULE.PLUGINS.items():
            package = ROOT / "packages" / f"{plugin}-plugin"
            expected = {name: (package / name).read_bytes() for name in ("plugin.json", "README.md")}
            for skill in skills:
                expected.update({f"skills/{skill}/{name}": data
                                 for name, data in MODULE.source_files(package / "skills" / skill)})
            with self.subTest(plugin=plugin), zipfile.ZipFile(ROOT / "downloads" / f"{plugin}-plugin.zip") as archive:
                self.assertEqual(len(archive.namelist()), len(set(archive.namelist())))
                self.assertEqual(expected, {name: archive.read(name) for name in archive.namelist()})


if __name__ == "__main__":
    unittest.main()
