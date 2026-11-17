# Simplify Code

Simplifies code so it is robust, readable, and well structured without changing what it does: fewer files, fewer moving parts, a smaller surface.

## Try it

“Use simplify-code on the invite e2e support folder.”

The assistant reads the code, its callers, and the repository's conventions, then proposes a short plan with a before/after file tree and line counts. Nothing changes until you approve. It applies the approved cuts in one pass, updates docs that describe the changed files, and proves the result by running the real flow, not just lint and types. A bug found along the way is reported as a separate fix, never hidden in the cleanup.

## Install and compatibility

Use the **Daily Useful** plugin package; see its included README for installation. For Codex, copy this complete skill folder to your configured skills directory. Updating repository files alone does not update an installed plugin.

The skill is plain instructions: no scripts, credentials, or additional service are required. It reads `AGENTS.md` or `CLAUDE.md` when present.
