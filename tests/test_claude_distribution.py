"""Check Claude package completeness, names, version, and portable paths."""
import importlib.util
import json
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_packages", ROOT / "scripts/build_packages.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ClaudeDistributionTests(unittest.TestCase):
    def test_marketplace_resolves_complete_plugins(self):
        marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
        self.assertEqual(marketplace['name'], 'erezlev-skills')
        self.assertTrue(marketplace['owner']['name'])
        self.assertEqual([entry['name'] for entry in marketplace['plugins']], list(MODULE.PLUGINS))
        for entry in marketplace['plugins']:
            with self.subTest(plugin=entry['name']):
                self.assertTrue(entry['source'].startswith('./'))
                package = (ROOT / entry['source']).resolve()
                self.assertTrue(package.is_relative_to(ROOT))
                manifest = json.loads((package / '.claude-plugin/plugin.json').read_text())
                self.assertEqual(manifest['name'], entry['name'])
                work = json.loads((ROOT / 'packages' / f"{entry['name']}-plugin" / 'plugin.json').read_text())
                self.assertEqual(manifest['version'], work['version'])
                self.assertNotIn('$schema', manifest)
                for name in MODULE.PLUGINS[entry['name']]:
                    self.assertTrue((package / 'skills' / name / 'SKILL.md').is_file())
                    self.assertTrue((package / 'skills' / name / 'README.md').is_file())
                    if name != 'visual-response':
                        self.assertEqual((ROOT / 'providers/claude-code' / name / 'SKILL.md').read_bytes(),
                                         (package / 'skills' / name / 'SKILL.md').read_bytes())

    def test_claude_zips_contain_exact_packages(self):
        for plugin in MODULE.PLUGINS:
            package = ROOT / 'packages' / f'{plugin}-claude'
            expected = {p.relative_to(package).as_posix(): p.read_bytes()
                        for p in package.rglob('*') if p.is_file()
                        and '__pycache__' not in p.parts and p.suffix != '.pyc'}
            with self.subTest(plugin=plugin), zipfile.ZipFile(ROOT / 'downloads' / f'{plugin}-claude.zip') as archive:
                self.assertEqual(len(archive.namelist()), len(set(archive.namelist())))
                self.assertEqual(expected, {name: archive.read(name) for name in archive.namelist()})
                self.assertIn('.claude-plugin/plugin.json', archive.namelist())
                self.assertNotIn('plugin.json', archive.namelist())


if __name__ == '__main__':
    unittest.main()
