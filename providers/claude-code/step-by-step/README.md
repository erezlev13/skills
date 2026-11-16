# Step by Step for Claude Code

Run `/daily-useful:step-by-step` with your goal, for example: “Help me configure branch protection, one step at a time.”

In terminal sessions, you receive one action and its expected result. Reply `next`, `back`, or ask about the current step. Progress is self-reported within the conversation. A renderer is optional; installing this skill does not add buttons to the terminal.

Install the Daily Useful Claude plugin using the repository's Claude Code guide. For a standalone skill, copy this complete folder into `~/.claude/skills/step-by-step/` and invoke `/step-by-step`.

This provider is authored in `providers/claude-code/step-by-step/`; the package copy is generated. It needs no helper scripts, hooks, MCP server, credentials, or background process.
