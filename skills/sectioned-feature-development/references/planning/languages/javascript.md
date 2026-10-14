# JavaScript

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed JavaScript logic, Promise/callback composition or module boundary.

Do not select merely because a build tool happens to be written in JavaScript; Node.js/browser/framework behavior is a separate adapter.

## Decisions before sectioning

- Identify actual host (browser, Node, other), module mode and runtime-supported syntax without inferring a domain.
- Name the authoritative parser and representation at JSON/number/date/undefined/null boundaries.
- If promises change, identify who awaits completion and who cancels underlying work; a rejected aggregate does not prove other work stopped.

## Concrete planning example

A plain Node CLI returning a rejected Promise needs a defined exit/error path, not a web full-stack plan.

## Handoff and smallest useful evidence

Exercise the real exported function/client with an error or late-result case only when affected. A transpiled build is not proof of host APIs or callback completion.

## Scope boundary

No framework migration, global Promise wrapper, blanket retry or new validation dependency. No route creates a product requirement, extra review or new test framework.

## Sources and status

[MDN promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
