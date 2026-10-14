# PHP

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed PHP request, command, package or long-lived worker source.

Do not select merely because the application is a website; PHP does not imply Laravel or WordPress.

## Decisions before sectioning

- Confirm PHP version, Composer/autoload and short-lived request versus long-running worker context.
- Identify coercion/strictness, null/missing/false/zero and numeric-string behavior at the real input boundary.
- Name resource/error behavior and response/session state whose lifetime the task changes.

## Handoff and smallest useful evidence

Use actual handler/CLI/package consumers, one relevant coercion/error example and the existing test runner; use Laravel only when source-proven.

## Scope boundary

No broad strict_types migration, framework adoption, schema generator or global validation framework. No route creates a product requirement, extra review or new test framework.

## Sources and status

[PHP type juggling](https://www.php.net/manual/en/language.types.type-juggling.php). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
