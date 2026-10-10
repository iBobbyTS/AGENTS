# Server/client state and actual reconciliation

**Select only:** server/client ownership, framework lifecycle or response reconciliation changes the answer. Determine the actual framework/version, server rendering, navigation and hydration path; browser/client-only assumptions may not apply.

SvelteKit documents both the risks of shared server state and preservation of component/page state. Inspect whether mutable state is request/user-scoped and whether a component's local values are actually derived or reconciled when new authoritative data arrives. Do not assume remount on every navigation. ([SvelteKit state management](https://svelte.dev/docs/kit/state-management))

**Distinguish:** execute a source-grounded sequence such as initial server `[]` → local saved `[B]` → authoritative deletion → fresh server `[]`. A guard comparing only new server values to the old server snapshot can skip a necessary local update. This is an illustrative example, not a universal framework bug. Exercise the actual synchronization effect and action/load sequence before claiming application proof.

For shared server variables, inspect lifetime and actual per-request identity; use separate synthetic users in an authorized local test to observe any leakage. For reordering, choose a real slow/fast response sequence with version/request ownership, rather than imagining impossible event order.

**Counterevidence:** a preserved draft or optimistic state may intentionally outlive a reload. Resetting every local value can destroy user edits. Distinguish saved authoritative state, ephemeral UI state and unsaved input, then apply the actual product policy. Absence of a global store is not a defect.

**Expansion:** follow the same lifecycle/guard mechanism in credible siblings only. DOM snapshots can support a rendering claim, but do not alone establish persistence, authorization or successful completion of the user journey.
