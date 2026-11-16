# Routing smoke check — 2026-11-16

A fresh isolated agent received only the skill discovery metadata and shuffled request/environment pairs. It did not receive the skill body, expected routes, assertions, or implementation discussion. It classified whether to select the skill; it did not execute the requests.

- Expected triggers selected: 10/10.
- Expected non-triggers rejected: 10/10.
- The short five-step list and four-date list remained text.
- Interactive two-path and index-write explanations selected the skill without reaching count thresholds.
- Plain-text/table requests, coding changes, status, and implicit terminal-only comparisons stayed text.

This is a batch selection smoke test. It does not establish automatic invocation by an installed host, cross-host rendering, accessibility behavior, or preservation of an actual converted answer. The fresh-session end-to-end protocol in README.md remains to be run in each supported host. No Claude or Canvas runtime was exercised.
