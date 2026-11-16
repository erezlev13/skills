# Claude capability adapter

Inspect the session's exposed tools; this file does not guarantee any Claude interface or tool exists.

- If a visualization tool exposes `read_me`, read its live contract before authoring. Use `show_widget` only if actually exposed and documented by that contract; otherwise use the available documented renderer.
- If an Artifact capability is exposed and the user wants reusable or shareable output, follow its artifact workflow and return the supported artifact reference. Verify the actual sharing/export behavior before claiming it.
- With no supported visual capability, use Markdown and disclose the limitation for explicit interactive requests.

Let the live tool contract govern colors, layout, scripting, allowed content, and validation. Keep the conclusion/next action in adjacent text when useful without repeating the whole visual. Preserve required explanations and evidence adjacent when the widget forbids narrative. Never assume a widget is permanent, ephemeral, shared, or saved.
