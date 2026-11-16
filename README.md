# Daily Useful

Two practical skills in one plugin: answers you can explore, and guidance you can follow.

| Skill | Purpose | Guide |
| --- | --- | --- |
| **Visual Response** | Interactive explanations, comparisons, and timelines | [Work](providers/chatgpt-work/visual-response/README.md) · [Codex](providers/codex/visual-response/README.md) |
| **Step by Step** | One step at a time, with Back, Next, Done, and contextual questions | [Work](providers/chatgpt-work/step-by-step/README.md) · [Codex](providers/codex/step-by-step/README.md) |

**[Download Daily Useful](downloads/daily-useful-plugin.zip)** · [Installation and usage](packages/daily-useful-plugin/README.md) · [Interactive catalog](https://erezlev13.github.io/skills/)

## Development

Edit `sources/visual-response/` for Visual Response; the build generates both provider copies and the plugin copy. For Step by Step, edit the provider folders. The build verifies complete plugin copies and creates a deterministic ZIP.

```sh
python3 scripts/build_packages.py
python3 -m unittest discover -s tests
```

[Feedback](https://github.com/erezlev13/skills/issues) · MIT licensed
