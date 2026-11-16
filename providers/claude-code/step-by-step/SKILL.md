---
name: step-by-step
description: Provide one-step-at-a-time guidance for setup, troubleshooting, and hands-on procedures. Use for walkthroughs and follow-along help, not requests to execute a task or list every instruction at once.
---

# Step by step

Guide the user through one actionable step per turn. Establish the goal, environment, and current state; ask only what changes the next action. Verify changing labels or prerequisites from available sources. Keep instructions concise and include an observable expected result.

In Claude Code without a documented inline renderer, use normal conversation. End with a short invitation to reply `next`, `back`, or a question. Wait for the user's report before advancing. Never print fake clickable buttons or require an HTML viewer for ordinary guidance. An execution request means do the authorized work, not make the user follow a wizard.

If the user requests a full explanation first, provide it before the guide. When converting prior guidance, preserve all actions, prerequisites, examples needed to act, costs, caveats, sources, and continue/revise/stop criteria across the steps. Keep the rationale and material caveats available; do not reduce the source to an abbreviated checklist.

Answer questions before continuing. Handle a missing item or a different screen by checking the current state and repairing the instructions. Revisit earlier steps on `back`; when an earlier choice changes, invalidate affected later confirmations. A `next` or `done` reply records the user's report, not independent proof of external changes. Do not claim progress persists between sessions; supply concise resume context when useful.

Only use interactive controls if this session exposes a documented renderer, or the user requests a standalone interactive deliverable. Read that renderer's live contract and follow its paths, styles, content restrictions, accessibility, and delivery rules. Use Next, Back, Done, and contextual help when supported. Feature-detect only documented chat/state APIs; never assume `window.openai`, a `visualize` skill, or a Claude artifact API exists. Keep navigation local; show a copyable question when no chat bridge exists.

Before delivery, check content coverage, action prerequisites, expected results, and sources. For actual interactive output, check the primary controls, keyboard access, narrow layout, and help/error fallback when preview is available. State only checks actually performed.
