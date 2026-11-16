---
name: step-by-step
description: Provide one-step-at-a-time guidance for setup, troubleshooting, and hands-on procedures, with Next, Back, Done, and contextual help buttons. Use for walkthroughs and follow-along guidance, not requests to execute a task or list every instruction at once.
---

# Step by step

Present a survey-like guide: one actionable step and one primary button. Explicit requests call for working controls when the host supports them, even for short procedures.

## Prepare

Establish the goal, environment, and starting point. Verify changing product labels or prerequisites with sources. Ask only for information that changes the next action. Use choices for known paths; resolve unknown paths in chat rather than inventing instructions.

Give steps stable IDs, concise instructions, and an observable expected result. Keep necessary caveats and source links beside the action. Next confirms the current step; Back revisits; Done confirms the final step. These buttons record self-reported progress, never perform or independently verify external actions. Changing an earlier choice invalidates dependent confirmations and answers.

## Render

Read the active host's `visualize` contract once when needed; reuse it while current. Follow its output location, styling, delivery marker, and supported APIs. Do not assume `/workspace` exists. A skill cannot add an unavailable rendering surface.

Read [references/guide-format.md](references/guide-format.md) only when preparing unfamiliar guide data. Generate through the bundled builder; do not routinely load its template/runtime into model context:

```sh
python3 <skill-dir>/scripts/build_guide.py <guide.json> <authorized-output>/guide.html
```

Reuse known schema and assets for later guides. The builder provides conditional steps, accessible choice buttons, progress, navigation, and contextual help. Honor explicit requests for instructional content when generic visualization guidance would otherwise omit it.

Offer Ask a question, Something is missing, and My screen is different at every step. Show the outgoing message with the current action and compact resume context. When documented and available, call `window.openai.sendFollowUpMessage({prompt,title})` directly from the submit click, before awaiting anything. Promise resolution does not prove delivery; retain Copy question/manual selection and tell the user to paste into chat if needed. Never simulate replies or call models from the fragment. Next, Back, choices, and Done remain local and start no chat turn.

Use optional documented host state only for bounded non-sensitive progress. Persistence is best effort; do not store help drafts or secrets. Local edits take precedence over delayed host snapshots. Pass `--no-host-bridge` when those APIs are not documented for the active host.

If inline rendering is unavailable or its supported output cannot be written, explain that briefly. Continue with one step in chat and Next/Back/question replies, using native buttons only if supported. Do not silently dump a full list or fake buttons.

## Continue and check

Answer follow-up questions first, repair affected instructions, and resume at the unresolved step. Use explicit resume context, not assumed state delivery. Preserve only still-valid confirmations; change the guide revision and supply valid `resume` data after corrections.

Check generated output and exercise navigation, changed choices, and help in an available preview when practical. Keep required information visible and the guide usable on narrow screens. State testing limits honestly. Do not read back full generated HTML for routine validation; use the bundled tests and targeted diagnostics.
