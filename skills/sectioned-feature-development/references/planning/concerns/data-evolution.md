# Persisted data / migration / transaction planning

Select when representation, backfill, transaction or query semantics actually change. Combine with the actual stack; simply reading an unchanged DB field is not enough.

## Freeze the needed contract

Identify the database/version, canonical writer, current stored examples and directly affected readers. Separate missing/null/zero/default, allowed domain, unit/precision and displayed projection where the change depends on them.

For a migration/import, state initial supported states, transformation, completion/failure states, partial-commit behavior and what retry means. Identify the real database's DDL/transaction restrictions and framework migration state. Keep rollback/backup/old-client compatibility limited to the approved operating model; not every local script needs mixed-version infrastructure.

For an existing transactional write, name the atomic unit and stale-input rule. “Inside a transaction” alone does not prove concurrent read-modify-write behavior. PostgreSQL Read Committed uses per-statement snapshots; other databases/settings differ. Pick evidence for the actual invariant, not a universal lock strategy.

## Slice and verify

Keep data, validation, encoder and required readers under one coherent business boundary. Add temporary coexistence only when deployment requires it. A later cleanup belongs to the responsible behavior, not a proof-only section.

Use representative stored data and the smallest failure/conflict example at the actual owner. Declare fresh-schema versus existing-data evidence and mock limitations. If concurrency is required, distinguish a stale-baseline unit test from genuinely concurrent transaction execution. Do not erase that distinction in readiness.

## Avoid

No automatic outbox, journal, schema marker, shadow table, repository-wide migration, new compatibility tier or zero-data-loss claim. Repository/user safety constraints still apply; diagnostics must not mutate the real user database without authority.

## Sources

[PostgreSQL isolation](https://www.postgresql.org/docs/current/transaction-iso.html); [Django migration state](https://docs.djangoproject.com/en/5.2/topics/migrations/). Version-dependent behavior must be checked in the project's actual database/framework.
