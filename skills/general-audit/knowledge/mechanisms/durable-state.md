# Durable state and semantic atomicity

**Trigger:** more than one business effect, a conditional write, external acknowledgement, replay, migration or checkpoint.

**Hypothesis:** storage commits successfully but the business transition is only partially true. A final statement affecting zero rows is treated like a transaction failure; an acknowledgement/checkpoint is advanced before its promised effects are durable.

**Distinguish:** write the intended before/after invariant. Identify every write and side effect, the actual commit point, and all concurrent writers. In a disposable fixture, activate one reachable state change or interruption between validation, write, effect and acknowledgement. Check the durable invariant and replay result, not only the transaction's success. Use engine-specific semantics when deciding what isolation and constraints actually guarantee.

**Counterevidence:** a conditional no-op can be intentional idempotence, not failure. An invariant may be protected by one statement or a real constraint, so extra locks/transactions would add cost without benefit. Do not delete or roll back pre-existing valid data while compensating for a new failed operation.

**Expansion:** a broken atomicity assumption warrants checking sibling writers and consumers sharing that state. For external side effects, identify existing idempotency/deduplication/reconciliation mechanisms; do not automatically prescribe an outbox or distributed transaction. For a read-only path with no such invariant, this card is unnecessary.

**Closure:** demonstrate the original interleaving or a sound proof that prevents it; cover a legitimate zero-effect/idempotent control. A green happy-path test alone leaves the question open.
