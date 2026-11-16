"""Guard prompt size without pretending bytes equal billed model tokens."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SkillBudgetTests(unittest.TestCase):
    def test_discovery_and_instruction_budgets(self):
        for provider in ("chatgpt-work", "codex", "claude-code"):
            for skill in ("visual-response", "step-by-step"):
                path = ROOT / "providers" / provider / skill / "SKILL.md"
                with self.subTest(provider=provider, skill=skill):
                    text = path.read_text(encoding="utf-8")
                    parts = text.split("---", 2)
                    self.assertEqual(parts[0], "")
                    self.assertLessEqual(len(parts[1].encode("utf-8")), 350,
                                         "Keep discovery metadata short")
                    self.assertLessEqual(len(text.encode("utf-8")), 4500,
                                         "Move optional detail into lazy references")
                    self.assertTrue((path.parent / "README.md").is_file(),
                                    "Each skill needs its own user-facing README")


if __name__ == "__main__":
    unittest.main()
