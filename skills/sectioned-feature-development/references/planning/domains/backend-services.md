# Backend services / APIs

Axis: `domain`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

The task changes a service handler, business operation, job consumer or exposed API.

Do not select merely because the project is full-stack but only a UI style changes.

## Decisions before sectioning

- Trace ingress/identity→validation→canonical operation→commit/external effect→response/consumer.
- Freeze error/status, absent values, ordering/pagination and idempotency only to existing obligations.
- For multi-service work identify actual partial failure/timeout/retry boundaries; do not automatically create distributed transactions.

## Handoff and smallest useful evidence

Use the real handler/serialization and representative request/error fixture; inspect transaction/queue integrations only where changed. Hand client workers the same successful and rejected result contract.

## Scope boundary

No microservice split, universal retry/caching/auth framework or generated API suite without authority. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Pact consumer guidance](https://docs.pact.io/consumer); [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
