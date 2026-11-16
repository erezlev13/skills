# Step by Step

A guided workflow with one action at a time, **Next**, **Back**, **Done**, and help buttons for questions, missing information, or a different screen. Choices can change which steps appear.

## Try it

“Use step-by-step to guide me through protecting my GitHub main branch. I want to follow along.”

Select an answer if needed, perform the action, then click Next. Back preserves your answers; changing an earlier answer clears dependent progress. Done records your confirmation, not an independently verified result.

Ask a question opens a message preview with the current step and progress. Continue in chat requests a follow-up when supported; Copy question provides a fallback. A guide cannot silently inspect or change an external app.

## Install and compatibility

Use the **Daily Useful** plugin package; see its included README for installation. For Codex, copy this complete skill folder to your configured skills directory. The plugin also includes Visual Response. Updating repository files alone does not update an installed plugin.

Interactive controls require a supported inline renderer. In plain CLI/chat environments the skill provides one step per turn. Direct chat and saved progress depend on host capabilities; a copyable question remains available. No credentials or additional service are required.

## Consumption

Next, Back, choices, and Done run locally: **no model request or chat turn**. Asking for help creates a normal chat turn only after you submit it. The skill reuses a bundled builder and assets instead of generating their implementation repeatedly.

The entrypoint stays within the tested 4,500-byte budget. The schema loads only when needed; runtime templates and tests are not routine model context. Host instructions, task data, and tool overhead vary by session.

## Files

`SKILL.md` controls behavior; `references/guide-format.md` defines guide data; `scripts/build_guide.py` builds the fragment; `assets/` holds the reusable UI and example; `scripts/tests/` verifies state transitions and safe generation. Read this README for usage, not on every skill invocation.

## Content preservation

Converting an existing answer preserves its important facts, costs, caveats, examples, success criteria, and next decisions. Ask for “the full answer first, then the interactive guide” to receive both in that order.
