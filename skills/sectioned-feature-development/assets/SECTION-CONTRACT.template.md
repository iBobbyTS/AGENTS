# `<ID>` Section Contract

- Feature ID:
- Title:
- Section base:
- Plan source:
- Primary owner:
- Original section lineage:

## Outcome and changed contract

- Exact observable behavior this section adds or changes.

## Authority and necessity

- External authority anchor: user decision, repository/current-production obligation, or unavoidable correctness dependency.
- Why this section is required for the minimum end-to-end feature outcome:
- Why an existing owner/path or smaller local change cannot satisfy it:
- A plan, another section, or reviewer suggestion alone is not an authority anchor.
- Local-patch versus shared-foundational-owner decision: `not-applicable | local patch authorized | shared owner authorized | owner decision required`
- Decision authority / why sibling callers remain correct:

## Direct impact cone

### Allowed-to-edit manifest

- Owners/files/symbols/routes/workflows the implementer or repair agent may change:

### Inspect-only dependency paths

- Direct callers/callees/serializers/contracts/tests that may be inspected to prove causality:
- An unlisted dependency may be inspected only with an exact data/control/serialization/contract chain from a changed symbol. Inspection does not authorize editing it.

### Explicit exclusions

- Owners/mechanisms that may not be added or changed without a main-agent scope decision:

## Existing invariants

- Invariants and repository rules this section must preserve.

## Allowed structural changes

- `none`, or explicit requirement-anchored mechanisms.

## Non-goals and deferred owner

- Unsupported behavior/environments/actors:
- Named later section/owner:

## Review intensity

- `MECHANICAL | BOUNDED | HIGH_RISK`

## Acceptance criteria

- `AC-<ID>` — Falsifiable behavior, edge, and error outcome.

## Validation tiers

- Targeted:
- Section/package:
- Integration checkpoint, if triggered:

## Review boundary

Blocking findings must be `DIFF_CAUSED`, tightly proven `MERGE_BLOCKING_DEPENDENCY`, or an `EVIDENCE_GAP` citing an exact acceptance criterion/repository gate. Review may not add a new product guarantee, threat model, durability/compatibility promise, generalized framework, global analyzer, or CI policy.

A real blocker requiring a new owner returns to the main agent for one explicit causal scope amendment or owner rebound. The reviewer or repair agent may not expand this manifest.

## Reset triggers

- Material changes to API/schema/trust/persistence/state ownership/concurrency/deployment/section goal.
