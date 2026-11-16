---
name: visual-response
description: "Use for explicit visuals or useful exploration: 3+ options on 3+ criteria, 5+ steps, 4+ dated events, numeric trends, or mechanisms. Treat counts as signals. Skip simple facts, plain text/table requests, code edits, status updates, and implicit use without a renderer."
---

# Visual response

The visual is a presentation of the answer, not a substitute. Preserve the answer first.

## Decide and route

1. Establish the goal, facts, assumptions, unknowns, and evidence. In coding sessions, default to text; consider visuals when the user is deciding or learning. Counts in the description are candidate signals, not quotas. Require a concrete benefit from seeing a relationship or changing a relevant input. Prefer a Markdown table for fixed comparisons; never invent controls to justify rendering.
2. Inspect available capabilities and read only the matching host reference below. Follow the current host's documented rendering, content, style, file, and delivery contract. Never infer support from a host name or invent APIs, paths, or tokens.

| Active surface | Read only |
| --- | --- |
| ChatGPT / Work | [chatgpt.md](references/chatgpt.md) |
| Claude | [claude.md](references/claude.md) |
| Codex desktop or CLI | [codex.md](references/codex.md) |
| Unknown or unsupported | Use Markdown; disclose the limit for explicit visual requests. |

3. Choose one dominant view. Read [patterns.md](references/patterns.md) only if needed. For guided procedures, use an available `step-by-step` skill; otherwise follow the host contract. Without a renderer, provide one action at a time in conversation when requested.
4. Use inline output for exploration; use a supported artifact/document workflow for requested reusable or shareable deliverables and verify the final link. Do not claim inline content disappears or persists universally, or that navigation saves progress or performs external actions.

## Preserve and place content

For conversions, read [content-fidelity.md](references/content-fidelity.md). Treat it as the baseline, not a summary request. Preserve its facts, rationale, examples, ranges, assumptions, sources, and next decisions; invent no filler values. Honor a requested full answer before the interactive version.

Put the conclusion and next action in concise adjacent text when useful; put supported details in the visual as real selectable or accessible text. If the host prohibits narrative in visuals, keep that narrative adjacent. Avoid duplicating the full answer unless requested. Show the recommendation, rationale, decisive criteria, and material caveats before clicks. Optional detail may use clearly labeled, keyboard-accessible disclosure; never make hover the only route to a fact or hide a requested comparison dimension in a tab.

Place sources near supported claims in the host's citation format. For code, cite a verified `file:line` or qualified symbol (and revision when relevant); never invent line numbers. Preserve these references during conversion.

## Check and deliver

- Compare the output with the content map, including sources and uncertainty.
- Check the initial state answers the main question; every control must change meaningful content or state.
- Use native keyboard controls, visible focus, labels, and appropriate state: `aria-pressed` for toggles, `aria-selected` for tabs, `aria-expanded` for disclosure. Do not add pressed state to every button.
- Follow host theme tokens and contrast rules; verify light/dark appearance, narrow layout, touch access, and reduced motion when preview exists. Avoid nested scrolling, clipped text, and fixed-height outer frames.
- For HTML fragments only, run `python3 <skill-dir>/scripts/check_fragment.py <absolute-output-path>`. This checks literal structure, not runtime behavior or accessibility.
- When preview is available, exercise the primary control by keyboard and pointer, plus any bridge's unavailable/error path. Otherwise distinguish static checks from unverified rendering. Never claim tests not run.
- Emit the exact supported visual reference or artifact link. After one concrete failure and one supported recovery, disclose the limitation and provide a labeled text alternative.

Keep interaction local; feature-detect documented follow-up APIs. Reuse facts and current instructions unless reload is required. Skip unrelated guides, README, and evals. Match cost to the decision; length alone never justifies a visual.
