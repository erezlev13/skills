# Visual Response

Turns an answer into something you can explore: an interactive mechanism, a comparison on shared criteria, or a timeline with inspectable events. Simple questions still get simple answers.

## Try it

- “Use Visual Response to explain why indexes make database writes more expensive.”
- “Compare three ways to launch my product, including cost assumptions and milestones.”
- “Show how changing the team size changes this project plan.”

For guided tasks with Next, Back, Done, and contextual questions, use the companion **Step-by-step** skill in Daily Useful.

## What to expect

The first view should be useful immediately; controls should change relevant content or state. Sources, assumptions, and important limitations remain accessible. Explicit visual requests should not quietly turn into Markdown lists.

This skill uses a renderer supplied by the Codex host. Terminal-only Codex has no inline renderer; a browser-openable HTML alternative may be appropriate. Installing this skill does not add UI capabilities, perform actions shown in a diagram, or guarantee persistence or a chat bridge. If rendering fails, it should explain the limitation and label the alternative.

## Efficiency and contents

The entrypoint is compact; pattern guidance loads only when needed. Validation runs through a small Python helper, with concise output instead of routinely reading entire generated files. Visual generation and follow-up questions still consume tokens; there is no zero-cost guarantee.

- `SKILL.md`: selection, rendering, verification, and delivery instructions.
- `references/patterns.md`: optional composition examples.
- `scripts/check_fragment.py`: basic fragment checks, not browser or UI verification.
- `agents/openai.yaml`: display metadata.

Copy this complete directory to your Codex skills location. The Daily Useful plugin archive packages the ChatGPT Work variant. Updating repository files alone does not update an installed copy.

## Content preservation

Converting an existing answer preserves its important facts, costs, caveats, examples, success criteria, and next decisions. Ask for “the full answer first, then the interactive guide” to receive both in that order.
