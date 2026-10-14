# Data engineering / pipelines / analytics delivery

Axis: `domain`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

The change ingests/transforms/materializes datasets or alters delivery to analytical/operational consumers.

Do not select merely because Python/SQL exists or a page reads unchanged database fields.

## Decisions before sectioning

- Name schema/units/keys, partition/time semantics, data quality policy and actual downstream reader.
- Define replay/backfill/deduplication and partial-output behavior from the request, not invented exactly-once guarantees.
- Separate transformation correctness from orchestrator retry/scheduling and external-effect atomicity.

## Handoff and smallest useful evidence

Use representative input/output rows including one late/duplicate/malformed case only when relevant; the actual writer and consumer must share the same schema. Scale checks use a concrete bound.

## Scope boundary

No warehouse/lakehouse migration, new scheduler, generalized lineage platform or permanent repair service for a one-off import. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html); [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
