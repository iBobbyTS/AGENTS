# SQL

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

SQL queries, schema/constraint expressions or database-visible semantics are changed.

Do not select merely because a database dependency exists, or an ORM reads unchanged fields.

## Decisions before sectioning

- Identify actual engine/version/dialect, connection settings and migration ownership; SQL does not imply PostgreSQL.
- Specify null/duplicate semantics, deterministic ordering/pagination, constraints and transaction boundaries.
- For changed isolation or locking, state the concrete concurrent scenario and actual engine behavior, not generic atomicity.

## Handoff and smallest useful evidence

Use representative rows and the real engine fixture when dialect/isolation matters. Share schema/query contract with application consumers; explain rollback/forward recovery only to the approved level.

## Scope boundary

No engine switch, global outbox/journal, universal isolation upgrade or optimization absent a concrete workload. No route creates a product requirement, extra review or new test framework.

## Sources and status

[PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
