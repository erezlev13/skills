# Daily Useful

Version **1.0.1** · One plugin containing **Visual Response** and **Step by Step**.

The installer may display the plugin as `daily-useful`.

## Install in ChatGPT Work

1. Download `daily-useful-plugin.zip` from this repository's `downloads/` folder.
2. If your interface offers **Plugins → Add → Upload plugin archive**, select this ZIP.
3. Review the plugin, complete installation, and start a new conversation to try it.

Installation controls can differ by account. This is a plugin archive, not a single-skill archive. A repository update does not automatically update a previously uploaded plugin; use the update or replacement flow in your interface and verify the version.

## Try each skill

- **Visual Response:** “Compare these three approaches visually so I can explore the tradeoffs.”
- **Step by Step:** “Walk me through protecting my GitHub main branch, one step at a time.”

See the bundled [Visual Response guide](skills/visual-response/README.md) and [Step by Step guide](skills/step-by-step/README.md) for details.

## What the host provides

Interactive output needs the host's visualization renderer. A skill cannot unlock unavailable host features. Step by Step uses the supported conversation bridge for contextual questions; otherwise it offers a message to copy into chat. **Done** records guide progress, not independent verification of changes in another app. Resume support depends on the host.

Skill entrypoints stay compact and load supporting guidance only when needed. README files are user documentation, not required routine runtime context. Actual token usage depends on the host and task; this is not a billing guarantee.

## Codex

Copy a complete skill folder from the repository's `providers/codex/` into `~/.codex/skills/`, preserving its resources. Start a new conversation if discovery needs refreshing. A local Codex installation does not install a Work plugin.

## Source and feedback

The repository is [erezlev13/skills](https://github.com/erezlev13/skills). Report the prompt, what happened, and what you expected in a [GitHub issue](https://github.com/erezlev13/skills/issues). MIT licensed.
