# HTML / CSS (markup and style languages)

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed HTML semantics, form controls, styles or layout selectors.

Do not select merely because a frontend exists without markup/style changes; this is not a JavaScript framework route.

## Decisions before sectioning

- Identify actual DOM semantics, successful form controls, focus/label relationships and CSS cascade/scoping.
- Define the affected layout/interaction states and only the relevant viewport/content-size boundaries.
- Distinguish visual order from DOM/model order and form serialization from cosmetic presentation.

## Handoff and smallest useful evidence

Use the actual renderer and concrete two-item/overflow/form example when relevant. A screenshot alone does not verify interaction or request wiring.

## Scope boundary

No global redesign, CSS framework replacement, wholesale accessibility audit or unrelated responsive matrix. No route creates a product requirement, extra review or new test framework.

## Sources and status

[HTML forms specification](https://html.spec.whatwg.org/multipage/forms.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
