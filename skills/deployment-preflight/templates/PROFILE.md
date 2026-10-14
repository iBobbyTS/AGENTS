# Release profile — <project>

Profile version / reviewed: <date or revision; provenance below>
Purpose and authoritative usage/scope: <links>
Product / delivery type: <service / static site / desktop / CLI-library / other>

## Supported consumers and environments
<Who actually consumes the artifact; supported OS/runtime/protocol/API/version families; target/channel locators; first install vs upgrade. Unknowns explicit. Do not put current release revision here.>

## Delivery and ownership model
<Build/package source and actual entry/installer/distribution mechanism; components and owners; external dependencies; configuration/secrets interface and permissions. Link existing commands/runbooks; no secret values.>

## State and transition constraints
<State locations/owners, including user files, config, caches with semantic value and database only if present. Real coexistence/order constraints, user-visible compatibility promises and allowed interruption. “Not applicable” needs a factual reason, not an unchecked default.>

## Observation and containment/recovery
<What proves useful operation or successful consumer use; where signals appear; who decides stop/revert/forward-fix; feasible recovery/withdrawal; irreversibility limits. No corporate on-call or multi-region defaults.>

## Evidence sources and conditional checks
| Assertion / when relevant | Evidence source or bounded method | Environment/permission limit |
|---|---|---|
| <actual project assertion> | <existing result/script/record; inspect before running> | <allowed local / requires separate authority> |

## Authority, known gaps and provenance
<What this preflight may read/run/write; production/publish denied unless separately authorized outside this skill. Stable known-risk pointers and revisit condition; observed/user-confirmed/unknown fact provenance. CI availability describes evidence, not a requirement.>
