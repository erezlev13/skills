# Daily Useful for Claude Code

Four skills in one Claude Code plugin: **Visual Response**, **Step by Step**, **Guiding Questions**, and **Simplify Code**.

## Install

Run in your terminal:

```sh
claude plugin marketplace add erezlev13/skills
claude plugin install daily-useful@erezlev-skills
```

Or use `/plugin marketplace add erezlev13/skills` and `/plugin install daily-useful@erezlev-skills` in a Claude Code session, then complete the installation panel. Start a new session if commands have not appeared.

## Use

```text
/daily-useful:visual-response Explain the tradeoffs between these three architectures
/daily-useful:step-by-step Help me configure branch protection one step at a time
/daily-useful:guiding-questions Create a skill that keeps my code simple
/daily-useful:simplify-code Simplify the invite e2e support code
```

Claude may also select a skill from its description. In terminal sessions, Visual Response defaults to Markdown and Step by Step uses one action per turn. Inline interaction requires an actually exposed renderer; this plugin does not install one. Ask explicitly for a browser-openable visual if you want a separate interactive file.

See each skill's guide: [Visual Response](skills/visual-response/README.md), [Step by Step](skills/step-by-step/README.md), [Guiding Questions](skills/guiding-questions/README.md), and [Simplify Code](skills/simplify-code/README.md).

## Update and verify

```sh
claude plugin marketplace update erezlev-skills
claude plugin update daily-useful@erezlev-skills
claude plugin list
```

## Local development

From the repository root, run `python3 scripts/build_packages.py`, then:

```sh
claude plugin validate .
claude plugin validate ./packages/daily-useful-claude
claude --plugin-dir ./packages/daily-useful-claude
```

The build generates `.claude-plugin/plugin.json` and the packaged skill folders. Visual Response comes from `sources/visual-response/`; the other skills come from `providers/claude-code/<skill>/`. No hooks, MCP servers, or permissions are added. The Work ZIP is a separate package; do not use it as a Claude plugin.

Format and command references: [marketplaces](https://code.claude.com/docs/en/plugin-marketplaces), [plugin manifests](https://code.claude.com/docs/en/plugins-reference), [plugin commands](https://code.claude.com/docs/en/plugins/cli-reference).
