import importlib.util
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("build_packages", Path(__file__).resolve().parents[1] / "scripts/build_packages.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        manifest = self.root / "packages/daily-useful-plugin/plugin.json"
        manifest.parent.mkdir(parents=True)
        manifest.write_text(json.dumps({"name": "daily-useful", "version": "1.0.0"}))
        (manifest.parent / "README.md").write_text("# Daily Useful\nInstallation and usage")
        for provider in ("codex", "chatgpt-work"):
            for skill in MODULE.SKILLS:
                folder = self.root / "providers" / provider / skill
                (folder / "assets").mkdir(parents=True)
                (folder / "SKILL.md").write_text(f"---\nname: {skill}\ndescription: Example\n---\n")
                (folder / "README.md").write_text(f"# {skill}\nUser guide")
                (folder / "assets/template.html").write_text("<div>Complete resource</div>")

    def tearDown(self):
        self.temp.cleanup()

    def test_complete_deterministic_archives_and_mirror(self):
        paths = MODULE.build(self.root)
        before = [path.read_bytes() for path in paths]
        MODULE.build(self.root)
        self.assertEqual(before, [path.read_bytes() for path in paths])
        with zipfile.ZipFile(paths[0]) as archive:
            self.assertEqual(archive.read("skills/step-by-step/assets/template.html"), b"<div>Complete resource</div>")
            self.assertIn("plugin.json", archive.namelist())
            self.assertIn("README.md", archive.namelist())
            self.assertIn("skills/step-by-step/README.md", archive.namelist())
        for skill in MODULE.SKILLS:
            self.assertEqual(MODULE.source_files(self.root / "providers/chatgpt-work" / skill),
                             MODULE.source_files(self.root / "packages/daily-useful-plugin/skills" / skill))

    def test_incomplete_source_preserves_existing_package(self):
        MODULE.build(self.root)
        existing = self.root / "packages/daily-useful-plugin/skills/step-by-step/SKILL.md"
        before = existing.read_bytes()
        (self.root / "providers/chatgpt-work/step-by-step/SKILL.md").unlink()
        with self.assertRaises(ValueError):
            MODULE.build(self.root)
        self.assertEqual(before, existing.read_bytes())

    def test_stale_generated_files_removed(self):
        MODULE.build(self.root)
        stale = self.root / "packages/daily-useful-plugin/skills/old.txt"
        stale.write_text("stale")
        MODULE.build(self.root)
        self.assertFalse(stale.exists())


if __name__ == "__main__":
    unittest.main()
