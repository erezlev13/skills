---
name: visual-response
description: Create useful interactive explanations, comparisons, and timelines in supported Codex hosts. Use for explicit Visual Response requests or when exploration improves a structured answer. Keep simple facts and requested plain text concise.
---

# Visual response

Make the answer inspectable and useful, with the host's native visual quality. Decorated prose and inert cards do not count as interaction.

Check the active Codex surface. Desktop/Work may supply `visualize`; terminal-only Codex does not gain inline rendering by installing this skill. In a terminal, disclose that limit and offer browser-openable HTML when acceptable to the user; otherwise label the text alternative. Never invent a visualization token or standalone chat bridge. The fragment validator applies to inline output, not standalone documents.

## Choose and render

1. Establish the answer, evidence, unknowns, and user goal. Separate facts, assumptions, and illustrations.
2. Choose one dominant view: a mechanism to inspect, alternatives on shared criteria, changing inputs, or event order. Read [patterns.md](references/patterns.md) only when composition is unclear or examples would help. Keep implicit simple answers in their natural format; honor explicit interaction requests even for short answers.
3. Use the available `step-by-step` skill for guided procedures with Next, Back, Done, and questions. Otherwise implement them through the current host contract; do not substitute a long checklist.
4. Read the available host `visualize` instructions in full, then only applicable component guides. Reuse already-read current instructions within the conversation unless changed or reload is required after compaction. Follow their rendering, content, style, file, and final-reference rules. Prefer native components. This skill cannot install a renderer or enable chat APIs.
5. Resolve a renderer-readable, authorized output location on the actual executor. Do not assume `/workspace`, reuse another executor's paths, or substitute system temp. For an incompatible contract, discover a supported current one or disclose the limitation.

Make the initial view answer the main question. Use mechanisms where useful and expandable explanations where needed; align comparison criteria and quantitative scales. Preserve sources and material caveats in supported visible content or adjacent prose. Keep controls purposeful, selected states clear, and chrome minimal. Support narrow layouts, keyboard, focus, contrast, touch, and reduced motion.

Keep navigation local. Use only documented, feature-detected follow-up APIs for intentional questions. Never claim navigation executed external actions or saved UI state proves task completion.

## Preserve the answer

When converting an existing answer, treat it as the content baseline, not a request to summarize. Map recommendations, reasons, comparisons, costs, milestones, success criteria, examples, caveats, sources, and next decisions to visible content, accessible detail, or adjacent prose. Preserve ranges, units, and assumptions. Check this map before delivery; restore omissions. If the host restricts narrative inside the visual, retain it in adjacent prose. Honor requests for a full answer first and the interactive version afterward.

Keep the recommendation and rationale visible initially. Controls must preserve both ends of ranges, units, qualifiers, and open-ended bounds. Never substitute a lower bound for an estimate or invent milestone durations, evidence, or scores to fill a layout. Label new assumptions separately. Preserve procedural stages and continue/revise/stop criteria. Check every mapped item is reachable and every number retains its meaning; remove unsupported additions. Optimize repeated instructions and code, not useful answer content.

## Verify and deliver efficiently

- Run `python3 <skill-dir>/scripts/check_fragment.py <absolute-output-path>` for readable, literal fragment checks. It does not verify rendering. Execute helpers; inspect concise results instead of loading scripts, templates, or entire generated HTML by default. Read failing regions unless host instructions require more.
- Exercise the primary interaction, narrow layout, and any bridge's unavailable/error path when preview is available. Match validation effort to risk; do not force multiple model passes for simple output. State only what was tested.
- Emit the exact host visualization reference in the final response. Writing a file without delivering its reference is unfinished. Avoid duplicate full prose, code blocks, or download links replacing the visual.
- After one concrete failure and one authorized supported recovery, disclose the rendering limitation and label any text alternative. Never silently downgrade an explicit visual request or bypass permissions.

Reuse verified facts. Keep README and unrelated references out of model context unless needed. Efficiency reduces unnecessary context; it does not eliminate generation or model costs.
