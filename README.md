# Daily Useful

Two practical skills in one plugin: answers you can explore, and guidance you can follow.

| Skill | Purpose | Guide |
| --- | --- | --- |
| **Visual Response** | Interactive explanations, comparisons, and timelines | [Work](providers/chatgpt-work/visual-response/README.md) · [Codex](providers/codex/visual-response/README.md) |
| **Step by Step** | One step at a time, with Back, Next, Done, and contextual questions | [Work](providers/chatgpt-work/step-by-step/README.md) · [Codex](providers/codex/step-by-step/README.md) |

**[Download Daily Useful](downloads/daily-useful-plugin.zip)** · [Installation and usage](packages/daily-useful-plugin/README.md) · [Interactive catalog](https://erezlev13.github.io/skills/)

## Claude Code

```sh
claude plugin marketplace add erezlev13/skills
claude plugin install daily-useful@erezlev-skills
```

Use `/daily-useful:visual-response` or `/daily-useful:step-by-step`. [Claude Code guide](packages/daily-useful-claude/README.md).

## Simplify

A second plugin for building with less: **Guiding Questions** pins down open-ended requests with short multiple-choice rounds before building, and **Simplify Code** cuts files, moving parts, and surface without changing behavior.

| Skill | Purpose | Guide |
| --- | --- | --- |
| **Guiding Questions** | Short multiple-choice rounds before building anything open-ended | [Work](providers/chatgpt-work/guiding-questions/README.md) · [Codex](providers/codex/guiding-questions/README.md) |
| **Simplify Code** | Fewer files, moving parts, and surface, without changing behavior | [Work](providers/chatgpt-work/simplify-code/README.md) · [Codex](providers/codex/simplify-code/README.md) |

**[Download Simplify](downloads/simplify-plugin.zip)** · [Installation and usage](packages/simplify-plugin/README.md)

```sh
claude plugin install simplify@erezlev-skills
```

Use `/simplify:guiding-questions` or `/simplify:simplify-code`. [Claude Code guide](packages/simplify-claude/README.md).

## Development

Edit `sources/visual-response/` for Visual Response; the build generates all three provider copies and both plugin copies. For every other skill, edit the provider folders. The build verifies complete plugin copies and creates deterministic ZIPs for each plugin.

```sh
python3 scripts/build_packages.py
python3 -m unittest discover -s tests
```

[Feedback](https://github.com/erezlev13/skills/issues) · MIT licensed
