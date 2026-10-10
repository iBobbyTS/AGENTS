# Safe transition and version coexistence

**Trigger:** upgrades, staged component changes, package/API/file-format evolution, cache compatibility, rolling restarts or irreversible transformations.

**Hypothesis:** old and new components work separately but not in a combination the actual delivery sequence creates; an upgrade changes interpretation before consumers are ready; “rollback” restores code but not compatible state or already-distributed clients.

**Distinguish:** map the real before/during/after states and allowed ordering. Enumerate only reachable mixed versions and supported upgrade origins. Verify required consumer behavior across those boundaries, including representative persisted/user state where present. Separate preparation, activation and retirement. Identify the actual point where old code/consumers cannot safely return and which containment or forward repair is viable.

**Counterevidence:** an offline all-at-once local upgrade may not need rolling-version compatibility. A first release has no prior installed cohort if that is established. Not every schema or file-format change needs a reverse transformation; preserving a supported recovery path may mean forward repair, restore or withdrawal.

**Expansion:** load the canonical [durable state](../mechanisms/durable-state.md), [SQL](../technology/sql.md), [async ownership](../mechanisms/async-ownership.md) or [recovery](../mechanisms/recovery.md) only for mechanisms actually used. A static site can instead need cached-assets/URL continuity. Don't force a database-centered review.

**Closure:** the proposed manual sequence has evidence for necessary pre-switch assertions, explicit stop conditions, recovery limits and pending post-activation observations. A prerequisite safety fact cannot be deferred until after the irreversible step merely to obtain READY.
