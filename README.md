# Daily Useful

Four practical skills in one plugin: answers you can explore, guidance you can follow, questions that pin down what you mean, and code that stays simple.

| Skill | Purpose | Guide |
| --- | --- | --- |
| **Visual Response** | Interactive explanations, comparisons, and timelines | [Work](providers/chatgpt-work/visual-response/README.md) · [Codex](providers/codex/visual-response/README.md) |
| **Step by Step** | One step at a time, with Back, Next, Done, and contextual questions | [Work](providers/chatgpt-work/step-by-step/README.md) · [Codex](providers/codex/step-by-step/README.md) |
| **Guiding Questions** | Short multiple-choice rounds before building anything open-ended | [Work](providers/chatgpt-work/guiding-questions/README.md) · [Codex](providers/codex/guiding-questions/README.md) |
| **Simplify Code** | Fewer files, moving parts, and surface, without changing behavior | [Work](providers/chatgpt-work/simplify-code/README.md) · [Codex](providers/codex/simplify-code/README.md) |

**[Download Daily Useful](downloads/daily-useful-plugin.zip)** · [Installation and usage](packages/daily-useful-plugin/README.md) · [Interactive catalog](https://erezlev13.github.io/skills/)

## Claude Code

```sh
claude plugin marketplace add erezlev13/skills
claude plugin install daily-useful@erezlev-skills
```

Use `/daily-useful:visual-response`, `/daily-useful:step-by-step`, `/daily-useful:guiding-questions`, or `/daily-useful:simplify-code`. [Claude Code guide](packages/daily-useful-claude/README.md).

## Development

Edit `sources/visual-response/` for Visual Response; the build generates all three provider copies and both plugin copies. For the other skills, edit the provider folders. The build verifies complete plugin copies and creates a deterministic ZIP.

```sh
python3 scripts/build_packages.py
python3 -m unittest discover -s tests
```

[Feedback](https://github.com/erezlev13/skills/issues) · MIT licensed
