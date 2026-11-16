# ChatGPT / Work capability adapter

Inspect the tools and skill catalog exposed in this session. Do not assume a universal `canvas` API.

- If a native visualization skill or tool is available (for example, Work's `visualize`), read its current instructions in full and then only applicable component guides. Follow its actual fragment/document format, output location, style tokens, content restrictions, and final-reference syntax. Reuse already-read instructions unless a reload is required.
- If only a documented canvas or artifact tool is available, use its supported preview and delivery workflow. Do not emit Work visualization tokens for another surface.
- If neither exists, use Markdown. For an explicit interactive request, explain that inline interaction is unavailable; create a standalone file only when requested or acceptable within the requested deliverable.

In hosts that restrict visuals to labels, values, and accessible alternatives, keep required narrative and caveats in adjacent prose. Do not sacrifice facts to avoid repetition. Respect the host's separate rules for inline response content and saved/exported documents. Verify delivery; writing HTML alone does not render it.
