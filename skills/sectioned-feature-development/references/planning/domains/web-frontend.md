# Web frontend / interaction

Axis: `domain`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

A requested change concerns browser-visible interaction, navigation, rendering or client state.

Do not select merely because the repository has a frontend that this task does not change.

## Decisions before sectioning

- Trace input/gesture→request/state owner→render and every user-named direct reader.
- Separate persisted state, local draft, derived order, pending/optimistic state and authority to apply late results.
- Name real form/endpoint encoding and consumer decoding; locate the existing allowed component/browser test surface.

## Concrete planning example

For reorder, two distinct items, an end insertion and a failed save must use the actual request/response shape; retain named sibling readers.

## Handoff and smallest useful evidence

Handoff actual producer contract when present. Test the changed interaction with distinguishable data and one affected failure; one-item rendering proves layout, not reorder. Add a framework/browser adapter only for actual implementation semantics.

## Scope boundary

No whole-application UI/accessibility redesign, global store, API replacement, new Storybook or login bypass. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Pact consumer guidance](https://docs.pact.io/consumer); [HTML forms specification](https://html.spec.whatwg.org/multipage/forms.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
