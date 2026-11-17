# Simplify for Claude Code

Two skills in one Claude Code plugin: **Guiding Questions** and **Simplify Code**.

## Install

Run in your terminal:

```sh
claude plugin marketplace add erezlev13/skills
claude plugin install simplify@erezlev-skills
```

Or use `/plugin marketplace add erezlev13/skills` and `/plugin install simplify@erezlev-skills` in a Claude Code session, then complete the installation panel. Start a new session if commands have not appeared.

## Use

```text
/simplify:guiding-questions Create a skill that keeps my code simple
/simplify:simplify-code Simplify the invite e2e support code
```

Claude may also select a skill from its description. Guiding Questions asks through AskUserQuestion; Simplify Code proposes a plan and waits for your approval before changing code.

See each skill's [Guiding Questions](skills/guiding-questions/README.md) and [Simplify Code](skills/simplify-code/README.md) guide.

## Update and verify

```sh
claude plugin marketplace update erezlev-skills
claude plugin update simplify@erezlev-skills
claude plugin list
```

## Local development

From the repository root, run `python3 scripts/build_packages.py`, then:

```sh
claude plugin validate .
claude plugin validate ./packages/simplify-claude
claude --plugin-dir ./packages/simplify-claude
```

The build generates `.claude-plugin/plugin.json` and both packaged skill folders from `providers/claude-code/<skill>/`. No hooks, MCP servers, or permissions are added. The Work ZIP is a separate package; do not use it as a Claude plugin.
