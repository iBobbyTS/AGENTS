# Browser web platform

Axis: `adapter/platform`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed browser DOM/events/fetch/history/storage/worker semantics.

Do not select merely because a web-related repository exists but the touched path is server-only.

## Decisions before sectioning

- Identify actual form/navigation/request mechanism and browser security boundaries without changing them by default.
- Distinguish cancellation request, network completion, decoded result and UI settlement.
- Name DOM/focus/history/storage lifetime and only the relevant supported browser assumptions.

## Handoff and smallest useful evidence

Use the actual browser/consumer code for a changed gesture or navigation case; isolated rendering does not prove authenticated server wiring.

## Scope boundary

No blanket CORS changes, auth bypass, new automation harness or every-browser gate. No route creates a product requirement, extra review or new test framework.

## Sources and status

[HTML forms specification](https://html.spec.whatwg.org/multipage/forms.html); [MDN promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
