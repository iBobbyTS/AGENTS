# Ruby on Rails

Axis: `adapter/framework`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Rails route/model/callback/transaction or job path.

Do not select merely because Ruby code exists; non-Rails code does not inherit callback conventions.

## Decisions before sectioning

- Trace strong input/identity→service/model→response and all direct readers.
- Place callback and after-commit/external side effects on the actual transaction path.
- Check retries/job delivery and in-memory versus DB changes only when changed.

## Handoff and smallest useful evidence

Use actual request/model callbacks and existing transaction fixtures; a directly invoked helper can miss callback timing.

## Scope boundary

No callback removal campaign, new job framework, event bus or universal outbox. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Rails callbacks](https://guides.rubyonrails.org/active_record_callbacks.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
