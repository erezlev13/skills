# Match the visual to the question

Use this reference to choose a composition. The current host renderer still governs implementation and what content can appear inside its surface.

| User needs to… | Useful view | Meaningful interaction | Avoid |
| --- | --- | --- | --- |
| Understand a mechanism | One labeled diagram or simulation | Advance a stage or change an input; update the mechanism | Prose hidden in unrelated tabs |
| Compare options | Shared criteria and aligned values | Select a criterion or scenario while keeping alternatives comparable | A separate unrelated card per option; invented scores |
| Explore a quantitative trend | Native chart with units and time axis | Inspect points or compare relevant series | Decorative charts without exact values or sources |
| Inspect events | Timeline with verified dates | Select an event to reveal concise evidence | Equal spacing presented as elapsed time |
| Work through a task | One current action with expected result | Next, Back, Done, and contextual questions | A checklist masquerading as a guided flow |
| Navigate a long explanation | Compact overview plus focused detail | Select a meaningful topic; retain orientation | Splitting every paragraph into an accordion |

## Content discipline

Show the takeaway in the initial state without requiring exploration. Keep important limitations accessible; do not hide a disqualifying caveat in an optional tooltip. Make sources available next to the claims they support in the host-supported form. Do not fabricate numbers, timestamps, current UI labels, or user progress to make a visual look complete.

Use concise labels inside visuals and adjacent prose for explanation when required by the host. If there is no meaningful interaction, use a useful static visual or ordinary text unless the user explicitly requested interaction. Make controls respond to a real question, not merely change colors.

## Acceptance examples

- “Explain how indexes slow down writes.” Show a table update and affected indexes, with a control for index count updating the illustrated work. Label it conceptual unless timing measurements exist. Do not invent benchmark latency.
- “Compare three launch approaches with costs and milestones.” Keep the approaches on common criteria, state cost assumptions, and show milestones in an appropriate sequence. Changing an assumption must update all dependent values. Keep the recommendation understandable before interaction.
- “Use Visual Response to show me how to protect this repository.” Provide a guided sequence, ideally through `step-by-step`, with one concrete action and expected result per screen. Navigation only records user progress; it does not change GitHub settings.
- “What is 2 + 2?” Return the answer as text. The implicit skill should not add a chart or a widget.
- “Use Visual Response” after an attempted render failed. Retry using a supported current rendering contract and valid task-owned output location. If that still fails, name the limitation and label the text alternative; do not quietly repeat a Markdown list.

## Completion checks

- Does the initial view communicate the central relationship or decision?
- Does every control change meaningful content, state, or a requested follow-up?
- Are comparison criteria consistent, data correctly scaled, and unknowns visible?
- Can the primary interaction work by keyboard and at a narrow width?
- Does the final response actually include the rendered surface reference?
- Are storage, chat, and completion claims limited to what the host and tests support?
