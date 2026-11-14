---
name: visual-response
description: Turn long, structured answers into easy-to-follow interactive visual responses. Use when an answer has multiple sections, steps, comparisons, timelines, or data that readers need to navigate or track. Keep short answers in text.
---

# Visual response

Present substantial answers in the form that makes their content easiest to scan, explore, and act on. Choose the form from the material: a navigable outline for long explanations, a step tracker for procedures, a timeline for dated events, a comparison view for alternatives, or charts and filters for quantitative data. Combine forms only when they help the same reading task.

## Decide and build

1. First establish the complete, accurate answer and its sources. Preserve important qualifications, numbers, and links in the displayed content.
2. Use an interactive visual only when navigation, filtering, expansion, progress tracking, or exploration meaningfully improves a long answer. A short answer, simple table, or static diagram should use the host's normal response format.
3. Use the host's supported in-conversation visualization capability when available. Follow its current rendering instructions. In particular, use the `visualize` skill if available; do not assume that Markdown or a skill file alone can run HTML or JavaScript.
4. Select the smallest useful interaction. Common choices: expandable sections and a contents list; checkable steps with visible progress; sortable or filterable comparisons; a timeline with detail on selection; charts with clear labels and controls. Make the initial view useful without any clicks.
5. Give controls clear names, keyboard access, and readable contrast. Do not hide essential facts behind hover, color alone, or a control that fails to work. Keep the order logical on narrow screens.
6. Add a concise text summary outside the visual when needed. Ensure important content remains available as text or an accessible alternative. If the host cannot render an interactive visual, provide a structured Markdown answer with headings, tables, and checklists instead.
7. Before replying, check that all material from the answer is represented, sources point to their claims, and the primary interaction works. Do not imply progress is saved across sessions unless persistence actually exists.

The visual is a presentation of the answer, not a substitute for doing the underlying task. Respect requests for plain text, a specific file format, or another presentation style.
