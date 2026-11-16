# Visual Response evaluations

`cases.json` contains 10 expected triggers and 10 expected non-triggers. Counts are candidate signals; benefit, intent, and actual renderer availability decide the expected route.

## Automatic selection

Use a fresh session per case with normal skill discovery metadata available. Provide only `prompt` and `environment`, without naming the skill, loading its body, or exposing `expected_use` and `checks`. Record whether the host invokes Visual Response, the chosen output, and the delivered response. Score false positives and false negatives separately; target 10/10 in each group. A batch routing exercise is a smoke test, not proof of automatic invocation in real hosts.

## Behavior after selection

After a positive case selects the skill, allow the matching host guide and current native renderer contract to load. Check the case's assertions and the core checklist: content completeness, first-view usefulness, working keyboard control and state, theme and narrow layout, source preservation, and actual delivery. Exercise unsupported-host fallback and literal-HTML failures separately. Record static checks and real browser checks separately; do not mark unexercised UI behavior as passed.

For conversion regression, provide a baseline answer with cost ranges, units, rationale, milestones, examples, uncertainty, sources, and stop/continue criteria. Compare every material fact to the output. Keep required dimensions visible; allow labeled accessible disclosure for supplementary detail.

Do not put eval cases in the runtime skill package. Packaging/unit tests validate distribution, not model behavior. Store dated model/host/run evidence when available, and do not infer that Claude or Canvas works from Work-only tests.
