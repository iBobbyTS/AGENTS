# Django

Axis: `adapter/framework`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Django view/model/ORM/transaction/migration code.

Do not select merely because Python code or a database exists; framework activation needs imports/settings and the changed owner.

## Decisions before sectioning

- Inspect actual atomic/ATOMIC_REQUESTS settings, caught database exceptions and where transaction entry/exit occurs.
- Distinguish database rollback, Python in-memory state and on_commit/external effects.
- Migration code uses the framework's historical model state; keep new schema and old reader compatibility only when required.

## Handoff and smallest useful evidence

Reuse actual view/service/DB fixtures; transaction-sensitive cases cannot be proved solely by a mocked repository. Include installed migration runner when representation changes.

## Scope boundary

No universal transaction rewrite, outbox, new ORM or migration of unrelated tables. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Django 5.2 transactions](https://docs.djangoproject.com/en/5.2/topics/db/transactions/); [Django 5.2 migrations](https://docs.djangoproject.com/en/5.2/topics/migrations/). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
