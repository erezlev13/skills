"""Check Claude package completeness, names, version, and portable paths."""
import json
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ClaudeDistributionTests(unittest.TestCase):
    def test_marketplace_resolves_complete_plugin(self):
        marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
        self.assertEqual(marketplace['name'], 'erezlev-skills')
        self.assertTrue(marketplace['owner']['name'])
        self.assertEqual(len(marketplace['plugins']), 1)
        entry = marketplace['plugins'][0]
        self.assertTrue(entry['source'].startswith('./'))
        package = (ROOT / entry['source']).resolve()
        self.assertTrue(package.is_relative_to(ROOT))
        manifest = json.loads((package / '.claude-plugin/plugin.json').read_text())
        self.assertEqual(manifest['name'], entry['name'])
        work = json.loads((ROOT / 'packages/daily-useful-plugin/plugin.json').read_text())
        self.assertEqual(manifest['version'], work['version'])
        self.assertNotIn('$schema', manifest)
        for name in ('visual-response', 'step-by-step'):
            self.assertTrue((package / 'skills' / name / 'SKILL.md').is_file())
            self.assertTrue((package / 'skills' / name / 'README.md').is_file())
        self.assertEqual((ROOT / 'providers/claude-code/step-by-step/SKILL.md').read_bytes(),
                         (package / 'skills/step-by-step/SKILL.md').read_bytes())

    def test_claude_zip_contains_exact_package(self):
        package = ROOT / 'packages/daily-useful-claude'
        expected = {p.relative_to(package).as_posix(): p.read_bytes()
                    for p in package.rglob('*') if p.is_file()
                    and '__pycache__' not in p.parts and p.suffix != '.pyc'}
        with zipfile.ZipFile(ROOT / 'downloads/daily-useful-claude.zip') as archive:
            self.assertEqual(len(archive.namelist()), len(set(archive.namelist())))
            self.assertEqual(expected, {name: archive.read(name) for name in archive.namelist()})
            self.assertIn('.claude-plugin/plugin.json', archive.namelist())
            self.assertNotIn('plugin.json', archive.namelist())


if __name__ == '__main__':
    unittest.main()
