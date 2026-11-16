# Guide data and rendering

Supply UTF-8 JSON with plain text (not HTML or Markdown). The generator escapes embedded data and inserts user text with `textContent`. Links accept only absolute HTTP(S) URLs. Keep instructions concise enough for one screen; use `detail` for optional explanation. See [the branch-protection example](../assets/branch-protection.json) for a complete sample.

```json
{
  "id": "sample-guide", "revision": "1", "title": "Choose your setup",
  "steps": [
    {"id": "platform", "title": "Choose your platform", "instruction": "Which platform are you using?", "choices": [{"value": "mac", "label": "macOS"}, {"value": "windows", "label": "Windows"}]},
    {"id": "mac-step", "title": "Open System Settings", "instruction": "Open the Apple menu, then System Settings.", "showIf": {"step": "platform", "equals": "mac"}},
    {"id": "windows-step", "title": "Open Settings", "instruction": "Open Start, then Settings.", "showIf": {"step": "platform", "equals": "windows"}},
    {"id": "verify", "title": "Check the window", "instruction": "Confirm that the settings window is visible.", "expected": "Settings are open."}
  ]
}
```

- `id`: stable flow ID; `revision`: change when the instructions or branching change. Both use 1–64 lowercase letters, digits, or hyphens.
- `steps`: 1–30 steps with unique IDs; all have `title` and `instruction`. Optional `expected`, `detail`, and `links` appear within their step. Links are `{label,url}` objects.
- `choices`: 2–8 `{value,label}` entries; selection is required before Next. Values use the same identifier format. Do not request secrets or sensitive disclosures.
- `showIf`: optional condition on a preceding choice step. That step must be visible and have the matching answer. Conditions may not point forward or create cycles.
- `resume`: optional `{current, completed, answers}` supplied by the assistant after a chat correction. Include only explicitly known valid confirmations and choices. The renderer drops confirmations beyond the first unfinished visible step. Merely visiting a step never confirms it.

Each changed choice clears answers and confirmations for that step and all later steps; users reconfirm the revised path. Done confirms the final step locally and opens a completion summary; Review steps reopens the first step without losing confirmations.

## Host adaptation

The fragment uses documented visualize utilities (`btn`, `btn-primary`, `form-control`, `progress`, `viz-row`). It includes no external scripts, network requests, icons, or framework dependencies. The output is an HTML fragment, not a standalone website.

Supported visualize APIs, only when present in the active host documentation:

```js
await window.openai.sendFollowUpMessage({prompt, title});
window.openai.widgetState;
await window.openai.setWidgetState({modelContent, privateContent});
// Host update: event.detail.globals.widgetState on openai:set_globals
```

The template namespaces state with a hash of guide data, restores only matching snapshots, stores no free-text help, and bounds snapshots below 16 KiB. Updates replace the whole snapshot. Sequence numbers reject stale snapshots; once the user interacts locally, host events cannot overwrite that view. Reopening the view can restore a saved snapshot. This is not cross-tab synchronization. Saving does not start a chat turn; model delivery is best effort. Explicit help submissions include context regardless of state support.

Use `--no-host-bridge` if the active host does not document these APIs. This also disables host state. A disabled bridge still exposes Copy question and a selectable prompt. In unsupported hosts, follow the SKILL.md fallback instead of claiming the HTML will render. The bridge may resolve even when no message is dispatched; keep copy/manual fallback visible after all attempts.
