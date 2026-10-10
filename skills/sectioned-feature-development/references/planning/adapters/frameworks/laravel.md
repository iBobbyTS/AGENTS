# Laravel

Axis: `adapter/framework`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Laravel controller/Eloquent/job/lifecycle code.

Do not select merely because PHP source exists without Laravel owners.

## Decisions before sectioning

- Inspect input validation, policy/auth, canonical service and serialized resource response.
- For jobs identify transaction/dispatch ordering, retry behavior and exact side effects.
- Treat request-local state and long-lived queue-worker state separately.

## Handoff and smallest useful evidence

Use actual route/job fixtures and one rollback/retry example only if affected; observe external-effect limits explicitly.

## Scope boundary

No queue/ORM replacement, broad retry policy or workflow engine. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Laravel 12 queues](https://laravel.com/framework/docs/12.x/queues); [PHP type juggling](https://www.php.net/manual/en/language.types.type-juggling.php). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
