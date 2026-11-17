# Guiding Questions for Claude Code

Run `/daily-useful:guiding-questions` with what you want built, for example: “Create a skill that keeps my code simple.”

Before building anything open-ended, Claude reads the relevant files, then asks short rounds of up to four multiple-choice questions through AskUserQuestion. Options use your own files and examples, with Claude's pick first and marked “(Recommended)”. After each round you choose another round or build now. Claude then lists the decisions and shows the full draft for you to correct. Specific requests skip the questions.

Install the Daily Useful Claude plugin using the repository's Claude Code guide. For a standalone skill, copy this complete folder into `~/.claude/skills/guiding-questions/` and invoke `/guiding-questions`.

This provider is authored in `providers/claude-code/guiding-questions/`; the package copy is generated. It needs no helper scripts, hooks, MCP server, credentials, or background process.
