---
name: simplify-code
description: Simplify code so it is robust, readable and well structured without changing what it does — merge files, cut moving parts, shrink the surface. Use when the user asks to simplify, clean up or stop "adding and adding" code, when reviewing a diff or file for what to cut, and as a mindset while writing new code. Not an automatic pass after every change.
---

# Simplify code

Simpler code has less to read, less to keep in sync and fewer places to break. Prefer removing and merging over adding. Part of the `simplify` family; this skill covers code, including tests.

## When

- **On request** ("simplify", "clean this up", "too much code"): run the full workflow below.
- **On review** of a diff or file: same workflow, scoped to what was asked.
- **While writing**: before adding anything, ask the questions under "While writing". Do not run a separate cleanup pass unless asked.

## What simpler means

- **Fewer files.** Code that only one feature uses and that always changes together lives in one module.
- **Fewer moving parts.** One reliable path, not a chain of just-in-case strategies. No step the system already does for you.
- **Smaller surface.** Fewer exports, params, options, defaults and types. Callers pass only what varies; fixed values become constants inside the module.
- **Readable over clever.** Plain names and straight-line flow. A helper only when it removes real repetition or a cast. No type assertions or tricks to save lines.

## Red flags

| Flag | Example | Usual fix |
| --- | --- | --- |
| File per concept | `acceptInviteToken.ts`, `mailSlurpCommands.ts` used by one spec | Merge into the module that uses them |
| Fallback chain | find link → decode payload → follow redirect | Keep the paths that actually happen; drop speculative ones |
| Unused flexibility | `inviteViewer({ fullName, email, phone })` where only `email` varies; exported param types for one caller | Take only what varies; inline the rest as constants |
| Redundant cleanup | deleting inboxes that expire after an hour; re-validating validated input | Delete the step; say why in one line if it is not obvious |

## Hard limits

- **Behavior stays the same.** A bug found while simplifying is a separate, named fix in the plan and report, never hidden inside a cleanup.
- **Robustness stays.** Keep validation at boundaries, clear error messages and real cleanup. Do not drop a guard to save lines.
- **Conventions still apply.** Repo and personal rules (file-size limits, no `any`, naming, comment policy, import order) win over brevity.
- **Tests follow the same rules** and must still prove the same behavior.

## Workflow

1. **Read** the code in scope, its callers and the governing conventions (CLAUDE.md / AGENTS.md). Note what each file, export and step is for.
2. **Find cuts** using the red flags. For each, check every caller (grep) so a merge or removal breaks nothing.
3. **Propose a short plan and wait for approval.** A few bullets of direction, then a before/after tree with the line delta. Mark merges, deletions and kept files:

   ```
   Before (405 lines, 5 files)            After (~257 lines, 3 files)
   support/                               support/
     tasks.ts             137               tasks.ts             ~121  ← + token lookup
     acceptInviteToken.ts  63  ✂ merged
     inviteCommands.ts     84               inviteCommands.ts     ~79  ← + MailSlurp commands
     mailSlurpCommands.ts  34  ✂ merged
   e2e/invitee/spec.cy.ts  87               e2e/invitee/spec.cy.ts ~57  (no inbox teardown)
   ```

   List any behavior fix separately. Apply only what the user approves.
4. **Apply in one pass**, then update docs that describe the changed files (READMEs, AGENTS.md, PR body).
5. **Prove it by running the real flow** — the spec, the endpoint, the app — not just lint and types (run those too). If the real flow cannot run as-is (it hits production or a paid vendor), build a local harness: boot the stack locally and stub only the external boundary, keeping everything else real. Keep the harness out of the commit unless asked. Exercise the changed functions directly (e.g. mocked `fetch`) for paths the harness cannot reach.
6. **Report** what was merged, removed and kept, the before/after numbers, how it was proven, and what was not covered.

## While writing

Before adding, ask:

- New file? Can the module that uses it hold it?
- New param, option or export? Does any caller pass a different value today?
- Fallback path? Has the primary path actually failed this way?
- Cleanup or re-check step? Does the system already handle it?

If the answer points to "not needed", don't add it.
