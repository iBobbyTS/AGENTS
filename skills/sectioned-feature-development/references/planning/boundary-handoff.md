# Boundary contracts and producer–consumer handoff

Use only for a changed interface/state-owner seam or a split between workers that must agree on concrete behavior. Keep ONE compact contract in the existing PLAN/section contract and link it from TASK/HANDOFF. No new contract registry, schema gate or approval artifact.

## Minimum shared contract

Record only applicable items:

| Item | Concrete content |
|---|---|
| Authority and scope | Requirement/example; supported actors; allowed changes and exclusions |
| Production path | Entry → authoritative producer/transaction → serializer/transport → real consumers |
| Input | Exact field names, encoding, types, missing/null/zero meaning, ordering and baseline where used |
| Output | Wire/envelope and decoded payload; success/error categories; visible subset vs full result |
| State | Commit point, rollback/partial effects, late-result/cancel behavior, relevant identity |
| Consumption | UI/read/API consumers that must change or be verified unchanged; who owns each |
| Evidence | One concrete success and the meaningful activated failure; targeted check and remaining integration |

Input/output examples can be redacted source fixtures or proposed examples tied to the approved contract. Label origin (`OBSERVED`, `SOURCE_INSPECTED`, `PLANNED`, `UNKNOWN`). Never claim the new implementation ran before it exists, and never weaken business requirements to copy a broken current fixture.

An assertion about a system this change does not own — a host application, protocol peer, framework or upstream service — is anchored at its consumption site, not only its definition site: cite where that system actually reads, renders, routes or times the asserted value, with the same origin tags. Definition-site citations do not verify external behavior; a contract dense with them but sparse on consumer anchors is unverified exactly where integration risk lives.

## The contract travels across execution

1. PLAN author identifies the shared boundary and concrete examples before splitting producer and consumer work.
2. Producer worker reports the actual input/output encoding, response collection scope, errors, paths/symbols, candidate and relevant fixture/test. If still unimplemented, hand off the planned contract explicitly.
3. Main includes that same contract/fixture in the consumer TASK; a link must name the relevant section/symbol/example, not only the repository root.
4. Consumer worker exercises its real request builder/decoder/state update against that contract. Do not invent a second payload that merely resembles it.
5. If actual behavior differs, classify a bug, approved correction or genuine contract decision before downstream work. Do not silently bless a producer bug by changing the plan.
6. Parent reconciliation checks the joined behavior. Producer tests plus consumer mocks with inconsistent fixtures do not establish agreement.

Existing Handoff and REVIEW files hold this information; store raw output once. Lack of a special heading is not a blocker when the actual contract is present.

## Filters, projections and sibling readers

Write whether each set is global, visible, enabled, paginated, sorted or projected. A response may intentionally contain more entities than the submitted view; successful responses must not be rejected merely because their set is larger. Conversely, validation must not accept incomplete required sets. Determine actual semantics, do not apply either rule universally.

For shared persisted state, enumerate user-named readers and direct production consumers. Mark `VERIFY_UNCHANGED` only when source evidence shows they already satisfy the requirement; otherwise assign an edit to the business parent. Include registration/route reachability, not just private helper existence.

## Failure and verification boundary

Distinguish HTTP/protocol transport success, application result, persistence completion and visible UI state. A successful write followed by an incompatible client decoder can look like a failed write; name the recovery behavior rather than blindly retrying a side effect.

Use existing test facilities to exercise the real consumer code. An isolated UI fixture may prove interaction/layout, not authenticated routing or concurrent database semantics. Do not bypass environment restrictions to close a gap; preserve the gap and existing readiness policy.

## Non-goals

Do not install OpenAPI generation, Pact, a schema registry, strict unknown-field rejection, global locks, automatic retries or compatibility infrastructure merely to document agreement. Reuse such facilities only if already appropriate/authorized. No security actor or fault tolerance promise is introduced by this reference.
