# Stateful clients: web, desktop and mobile

**Use when:** correctness depends on navigation, local edits, identity changes, cache reconciliation, offline work or lifecycle. Select actual framework/platform semantics separately.

**Misleading reassurance:** a fresh response equals the previous server response, so the UI assumes nothing changed; meanwhile local state diverged. A component renders correctly in isolation but becomes stale after a real action/navigation sequence.

**Investigate:** identify authoritative versus optimistic state and the owner of unsaved edits. Trace save → response → reconciliation → another view; consider cancel, deletion, account switch, background/resume and navigation only where supported. Inspect focus/keyboard/accessible error paths when they govern completion of an actual user task, not a visual preference.

**Distinguish:** use the actual action and synchronization code with a sequence that changes local state before a same-valued authoritative reload. Compare visible state, persisted state and what a second view/session reads. For offline features, inspect conflict and replay rules without presuming “server wins.” Test the smallest lifecycle sequence that activates the suspected stale owner.

**Counterevidence:** stable value equality can be correct when no local divergence exists or the contract intentionally preserves a draft. Distinguish a stale saved record from an unsaved draft the product promises to retain. A new response is not universally an instruction to reset all local state.

**Expand/stop:** inspect siblings using the same reconciliation pattern, not every component. A framework-neutral model illustrates the mechanism but does not prove browser/native behavior.
