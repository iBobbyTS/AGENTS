# SQL/ORM semantics that cross a business boundary

**Select only:** an actual database/ORM behavior determines a hypothesis. Identify engine, version, driver, isolation, deployment limits and relevant constraints. Do not infer all of these from SQL syntax.

PostgreSQL documents that an UPDATE count of zero is not an error. Therefore a transaction can commit while an application-level prerequisite was not met. Inspect the whole invariant: conditional no-op may be intended, but when another write depends on success, check the real effect count or a stronger database guarantee. Reproduce on the actual engine when isolation/interleaving semantics are decisive. ([PostgreSQL UPDATE](https://www.postgresql.org/docs/current/sql-update.html), [isolation](https://www.postgresql.org/docs/current/transaction-iso.html))

A query's bind count is not necessarily its number of accepted objects. Derive fixed parameters plus per-object parameters for every generated statement; inspect deployed and runtime limits. SQLite's documented limits vary with version/build and can be lowered at runtime. Do not universally assume 999 or inherit a hosted engine's separate bound. Test both passing and failing neighbors of the actual limit. ([SQLite limits](https://www.sqlite.org/limits.html))

For Django, inspect transaction boundaries and how exceptions are handled; database rollback does not automatically restore in-memory model fields or caches. A cache or external callback can disagree with the final durable state. Check the installed version and the real consumer before prescribing a callback or rollback change. ([Django transactions](https://docs.djangoproject.com/en/stable/topics/db/transactions/))

**Counterevidence:** one authoritative statement/constraint can already protect the invariant; repeated application guards may be redundant. Zero-effect idempotence is not a bug. Do not introduce locks, serializable isolation, an ORM replacement or distributed transactions without a concrete violated guarantee and cost analysis.

**Evidence limit:** an SQLite toy model can illustrate semantic atomicity; it does not reproduce PostgreSQL, D1 or another engine's concurrency guarantee. Keep that distinction in the report.
