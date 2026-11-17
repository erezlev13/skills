# Simplify

Version **1.0.0** · One plugin containing **Guiding Questions** and **Simplify Code**.

The installer may display the plugin as `simplify`.

## Install in ChatGPT Work

1. Download `simplify-plugin.zip` from this repository's `downloads/` folder.
2. If your interface offers **Plugins → Add → Upload plugin archive**, select this ZIP.
3. Review the plugin, complete installation, and start a new conversation to try it.

Installation controls can differ by account. This is a plugin archive, not a single-skill archive. A repository update does not automatically update a previously uploaded plugin; use the update or replacement flow in your interface and verify the version.

## Try each skill

- **Guiding Questions:** “Ask me what I actually want before you design this skill.”
- **Simplify Code:** “Simplify the invite e2e support folder without changing behavior.”

See the bundled guides for details: [Guiding Questions](skills/guiding-questions/README.md) and [Simplify Code](skills/simplify-code/README.md).

## What the host provides

Guiding Questions uses the host's multiple-choice question tool when it has one; otherwise it asks in chat. Simplify Code needs access to the code it simplifies and a way to run its real flow for proof. Both are plain instructions: no scripts, credentials, or additional service.

## Codex

Copy a complete skill folder from the repository's `providers/codex/` into `~/.codex/skills/`. Start a new conversation if discovery needs refreshing. A local Codex installation does not install a Work plugin.

## Claude Code

Use the separate [Claude Code package](../simplify-claude/README.md), installed from this repository as a marketplace. The Work archive is not the Claude package.

## Source and feedback

The repository is [erezlev13/skills](https://github.com/erezlev13/skills). Report the prompt, what happened, and what you expected in a [GitHub issue](https://github.com/erezlev13/skills/issues). MIT licensed.
