# Svelte / SvelteKit planning

Axis: `adapter/framework`. JavaScript/TypeScript are separate language routes; select only languages actually changed.

Select for changed Svelte components, SvelteKit actions/load/endpoints or their real client integration. Inspect installed Svelte/Kit version and whether a path uses runes or legacy reactivity. Do not migrate syntax or choose an experimental data API merely because current docs mention it.

## Identify the real seam

Trace interaction → request builder → exact action/endpoint → application result → decoder/state update → load/read consumers. Distinguish:

- plain JSON endpoint versus form action/ActionResult, including encoding and success/failure/redirect/error handling;
- durable model order versus displayed derived order and stable component identity;
- server request-local state versus shared module state;
- load-provided data versus local drafts/optimistic state that may survive navigation;
- actual global/visible/paginated collections at both request and response.

SvelteKit documents form-action deserialization and `use:enhance` semantics; treating an action response like arbitrary JSON can be incorrect. Inspect the real repository client, not just a route's returned object. Server module globals are not per-user storage. See S01–S03 below.

## Concrete behavior to plan

For changed async UI, choose one real trajectory: act → pending → success/failure → navigate/close/repeat/late response as relevant. Name the owner that prevents an older response or rollback from overwriting a newer successful state. Do not add a generalized state machine.

For drag/reorder, include two distinguishable visible items, the last insertion position, response membership and a failed save. Check the actual renderer's order, not just mutation of `sortOrder`. Preserve expansion/focus/scroll only to the confirmed requirement. Name every other page required to display the same persisted ordering.

## Section/checkpoint design

A service/action checkpoint must hand the UI worker the exact request fields and real response envelope/collection meaning. The UI worker verifies its actual request/decoder with that fixture. Parent reconciliation joins persistence and interaction; an unconnected helper or static screenshot is not end-to-end evidence.

Reuse existing component/browser tests and allowed isolated renderers. Test the affected gesture/state transition, not only that a handle exists. An isolated fixture does not prove authenticated route wiring; preserve that distinction without bypassing auth or building new infrastructure solely to satisfy a review.

## Exclude

No framework upgrade, new global store, parallel API/action implementation, universal invalidation, UI redesign, whole-tree URL grammar, new Storybook/Pact suite or unrequested accessibility rework. Existing product accessibility/permission requirements still apply to the changed interaction.

## Sources

[Form actions](https://svelte.dev/docs/kit/form-actions); [State management](https://svelte.dev/docs/kit/state-management); [Loading data](https://svelte.dev/docs/kit/load). All guidance is conditional on the actual installed version and entry path.
