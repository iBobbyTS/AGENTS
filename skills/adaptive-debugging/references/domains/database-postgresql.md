# Database and PostgreSQL Debugging

Load this playbook for wrong data, failed SQL, connection/pool issues, migrations, transaction anomalies, locks/deadlocks, query latency, or persistent state inconsistent with application behavior. The conceptual workflow applies to other relational databases; commands here are PostgreSQL-specific.

## Classify before querying

Choose one or more:

- connection, authentication, TLS, DNS, or pool exhaustion;
- syntax/type/schema/search-path mismatch;
- wrong result or data invariant violation;
- transaction isolation, retry, or partial-commit behavior;
- blocking, lock ordering, or deadlock;
- query plan/cardinality/statistics/index performance;
- migration or environment schema drift;
- session state, timezone, locale, role, or row-level security;
- replication/read-after-write/staleness.

Capture database version, server/cluster, database, role, application name, schema/search path, transaction state, isolation level, and exact parameterized SQL shape. Do not paste secrets or full personal records.

## Safe inspection first

Prefer read-only catalog/statistics queries on the correct server. Confirm environment before any statement.

### Activity and waits

A targeted view of active work:

```sql
SELECT
  pid,
  usename,
  application_name,
  client_addr,
  state,
  wait_event_type,
  wait_event,
  xact_start,
  query_start,
  LEFT(query, 500) AS query
FROM pg_stat_activity
WHERE datname = current_database()
ORDER BY query_start NULLS LAST;
```

Interpret `state` together with wait events and transaction age. “Idle in transaction” is materially different from idle.

### Blocking chain

```sql
SELECT
  a.pid AS blocked_pid,
  pg_blocking_pids(a.pid) AS blocking_pids,
  a.wait_event_type,
  a.wait_event,
  a.xact_start,
  LEFT(a.query, 500) AS blocked_query
FROM pg_stat_activity AS a
WHERE cardinality(pg_blocking_pids(a.pid)) > 0;
```

Join blocker PIDs back to `pg_stat_activity`; capture both blocked and blocking transaction/query start times. Do not terminate sessions without authorization and impact analysis.

### Schema and environment drift

Compare actual rather than assumed state:

- table/column types, defaults, nullability, constraints, indexes;
- extension and collation versions;
- migration table and applied order;
- role grants, row-level security policies, search path;
- generated columns/triggers/functions;
- server timezone and client/session settings.

A fresh migration passing does not prove an upgraded production schema follows the same path.

## Query correctness

Use the exact bound values or a privacy-safe minimal reproduction. Check:

- implicit casts and parameter types;
- `NULL` semantics and three-valued logic;
- timezone conversions and date boundaries;
- collation/case behavior;
- join multiplicity and missing predicates;
- pagination order stability;
- transaction snapshot and read source;
- row-level security and role differences;
- stale prepared statements or schema-qualified names.

Build a tiny controlled dataset that includes the failing edge case and a passing neighbor. Avoid testing against a large mutable production dataset when a copied subset suffices.

## Transactions, isolation, and retries

Map the complete logical transaction:

```text
begin/read state → validate → write(s) → external side effect → commit/rollback → retry boundary
```

- Identify the actual isolation level and whether a pool/session overrides it.
- On serialization failures or deadlocks, retry the **whole logical transaction** from a clean state when the product contract allows it.
- Verify idempotency for external side effects and client retries.
- Check whether error handling leaves a transaction open or returns a pooled connection in an aborted state.
- Compare lock acquisition order across competing code paths.
- Do not “fix” a deadlock only by raising timeout or retry count; identify conflicting order/state.

## Query plans and performance

Start with plain `EXPLAIN` when execution is unsafe. For safe read-only or controlled staging queries, consider:

```sql
EXPLAIN (ANALYZE, BUFFERS, VERBOSE, SETTINGS)
SELECT ...;
```

**`EXPLAIN ANALYZE` executes the statement.** Do not run it casually on production writes, expensive queries, or statements with side effects. A surrounding rollback may not undo every external effect or sequence change and can still acquire disruptive locks.

When analyzing a plan:

- compare estimated vs actual rows at the first large divergence;
- inspect loops, filter removal, join strategy, sort/hash spills, buffer reads/hits, and execution time;
- confirm statistics freshness and distribution/skew;
- verify whether parameter-sensitive/custom-vs-generic plans matter;
- use `pg_stat_statements` to find aggregate frequency/latency impact;
- use `auto_explain` only with deliberate thresholds, sampling, privacy, and overhead controls.

Do not add an index solely because a scan appears in one plan. Demonstrate workload benefit and write/storage cost.

## Pools and connections

- Compare application pool metrics with server `max_connections` and active/idle sessions.
- Trace checkout duration, hold duration, transaction duration, and leak paths.
- Check health checks and migrations that bypass the normal pool.
- Confirm connection-string target, DNS, TLS mode, role, application name, and failover behavior.
- Detect session-local settings that survive pool reuse: search path, role, timezone, isolation, temporary tables, prepared state.

## Replication and stale reads

When read-after-write fails:

- identify which node served each read/write;
- correlate transaction commit time and replica replay position/lag;
- check routing, cache, transaction snapshot, and client retry before declaring replication lag;
- define whether the product requires strong read-after-write consistency and at what boundary.

## Common causal chains

```text
open transaction after handled error → connection returned to pool → later request sees aborted transaction
inconsistent lock order → concurrent paths deadlock → retry hides frequency but contention remains
wrong parameter type → implicit cast prevents intended index use → environment-scale-only latency
schema drift → app expects new constraint/default → upgraded database behaves differently from fresh test DB
read routed to replica → immediate post-write fetch is stale → UI appears to lose update
unstable pagination order → concurrent insert shifts page → duplicates/missing rows
```

## Completion evidence

- exact database/server/role and query or transaction contract;
- first incorrect persistent-state or lock boundary;
- safe failing/passing dataset or transaction interleaving;
- before/after plan or lock evidence when relevant;
- migration/rollback and concurrency verification where relevant;
- no production mutations or session termination performed without approval.
