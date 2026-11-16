# Visual Response

Turns an answer into something you can explore: an interactive mechanism, a comparison on shared criteria, or a timeline with inspectable events. Simple questions still get simple answers.

## Try it

- “Use Visual Response to explain why indexes make database writes more expensive.”
- “Compare three ways to launch my product, including cost assumptions and milestones.”
- “Show how changing the team size changes this project plan.”

For guided tasks with Next, Back, Done, and contextual questions, use the companion **Step-by-step** skill in Daily Useful.

## What to expect

The first view should be useful immediately; controls should change relevant content or state. Sources, assumptions, and important limitations remain accessible. Explicit visual requests should not quietly turn into Markdown lists.

This skill uses the documented renderer actually supplied by the current host. It does not add UI capabilities, perform the actions shown in a diagram, or guarantee persistence or a chat bridge on every client. If rendering fails, it should explain the limitation and label the text alternative.

## Efficiency and contents

The entrypoint is compact; pattern guidance loads only when needed. Validation runs through a small Python helper, with concise output instead of routinely reading entire generated files. Visual generation and follow-up questions still consume tokens; there is no zero-cost guarantee.

- `SKILL.md`: selection, rendering, verification, and delivery instructions.
- `references/patterns.md`: optional composition examples.
- `references/content-fidelity.md`: required checks when converting an existing answer.
- `references/chatgpt.md`, `claude.md`, `codex.md`: load only the matching host adapter.
- `scripts/check_fragment.py`: basic fragment checks, not browser or UI verification.
- `agents/openai.yaml`: display metadata.

Install through the matching Daily Useful plugin package. For Claude Code, use the marketplace instructions in `packages/daily-useful-claude/README.md` and invoke `/daily-useful:visual-response`. Updating repository files alone does not update an already installed plugin.

## Content preservation

Converting an existing answer preserves its important facts, costs, caveats, examples, success criteria, and next decisions. Ask for “the full answer first, then the interactive guide” to receive both in that order.

## Selection and host support

Candidate signals are three options across three criteria, five steps, four dated events, numeric trends, and mechanisms. These are not quotas: a fixed comparison can remain a Markdown table. Plain-text requests, routine code changes, status updates, and implicit use without a renderer stay in text. Explicit requests may justify smaller visuals.

Only the matching capability adapter loads: ChatGPT/Work, Claude, or Codex. Tool availability—not the product name—determines what can render. Shareable or retained deliverables follow the host's artifact/document workflow; inline content carries no persistence promise.

## Development and evaluation

Edit `sources/visual-response/`; the build generates Work, Codex, and Claude Code provider folders and both plugin copies. Run `python3 scripts/build_packages.py` and `python3 -m unittest discover -s tests` from the repository root. See `evals/visual-response/README.md` for isolated trigger and behavior evaluations. Static tests do not prove automatic host invocation or visual quality.
