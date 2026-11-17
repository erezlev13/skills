# Simplify Code for Claude Code

Run `/daily-useful:simplify-code` on a diff, file, or folder, for example: “Simplify the invite e2e support code.”

Claude looks for cuts (files merged, fallbacks dropped, parameters removed, redundant cleanup deleted) while keeping behavior, validation, and your conventions intact. It proposes a short plan with a before/after file tree and line counts, waits for your approval, applies it in one pass, then proves it by running the real flow, not just lint and types. While writing new code it applies the same questions without a separate cleanup pass.

Install the Daily Useful Claude plugin using the repository's Claude Code guide. For a standalone skill, copy this complete folder into `~/.claude/skills/simplify-code/` and invoke `/simplify-code`.

This provider is authored in `providers/claude-code/simplify-code/`; the package copy is generated. It needs no helper scripts, hooks, MCP server, credentials, or background process.
