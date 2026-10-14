# Routing and Complexity Gate

Use this document both before implicit invocation and at the start of an explicitly invoked session.

## Bypass the skill only when all conditions hold

A direct first-pass repair is allowed only when:

- this is the first repair attempt for the exact failure contract;
- the failure is deterministic and locally reproducible;
- the error and nearby code/configuration identify one concrete cause rather than merely one symptom;
- the repair is confined to one local expression, declaration, import, path, flag, or setting;
- the change is low risk and does not alter external behavior, persistent data, authorization, concurrency, packaging, or deployment semantics;
- a cheap direct check can re-run the original failure immediately; and
- no hard complexity trigger below applies.

Examples that commonly qualify:

- a syntax error at the reported token;
- a missing import with an existing dependency and unambiguous symbol;
- a misspelled local variable or file path;
- an isolated type mismatch with one intended type already established by surrounding code;
- a missing development-only configuration key whose required value is already documented and available.

Even in bypass mode, verify the original symptom. If the direct repair fails, invoke this skill before another repair.

## Hard triggers — invoke immediately

Any one of these is sufficient:

- A previous proposed or applied fix did not resolve the original failure.
- The problem is intermittent, flaky, timing-sensitive, order-dependent, or cannot be reproduced deterministically.
- There is a crash, hang, deadlock, livelock, data corruption/loss, authorization/security impact, or persistent state inconsistency.
- The symptom crosses process, service, frontend/backend, network, database, container, host, or client/server boundaries.
- The issue appears only in CI, production, release builds, packaged/distributed apps, another machine, or a specific architecture/OS/browser.
- Concurrency, cancellation, duplicate delivery, retries, transactions, locks, caching, or stale state may be involved.
- The task is performance, memory growth/leak, resource exhaustion, or responsiveness diagnosis.
- Reproduction is expensive, destructive, rate-limited, hardware-dependent, or requires scarce user interaction.
- The problem involves macOS signing, hardened runtime, notarization, Gatekeeper, sandbox, entitlements, XPC/helper embedding, or distribution artifacts.
- More than one plausible root cause remains after inspecting the exact error and the nearest relevant code/configuration.
- The user explicitly requests `$adaptive-debugging` or asks for root-cause investigation/evidence.

## Soft complexity indicators

Treat two or more as complex even if no hard trigger is obvious:

- substantial recent refactor or dependency/toolchain change;
- multiple environment dimensions differ;
- state/history affects the outcome;
- error is far from the likely source;
- logs disagree across components;
- a workaround changes frequency but not causality;
- the expected behavior or failure contract is incomplete;
- the relevant component is unfamiliar or weakly covered by tests;
- the repair could change public API, schema, migration, permissions, or user-visible semantics.

## Explicit invocation on a trivial issue

When the user explicitly invokes this skill and the issue meets every bypass condition:

1. State that it qualifies for lightweight mode.
2. Capture the failure contract in one compact block.
3. Confirm the direct causal evidence.
4. Apply one localized repair.
5. Re-run the original failure.
6. Stop; do not load unrelated playbooks or create persistent notes.

Explicit invocation is not a reason to manufacture complexity.

## Domain routing

Choose domains by causal boundaries, not by UI surface or repository folder.

| Signal | Primary domain | Common secondary domains |
|---|---|---|
| Wrong DOM, hydration, stale page state | Browser/frontend | Backend/API, network, test flakiness |
| 4xx/5xx, wrong API payload, timeout | Backend/API | Network, database, concurrency |
| SQL wrong result, lock wait, deadlock | Database/PostgreSQL | Backend/API, concurrency, performance |
| Duplicate work, race, order/cancellation | Async/concurrency | Backend, database, Swift/macOS |
| DNS/TLS/proxy/CORS/connectivity | Network | Browser, backend, Docker, system |
| Process exit/OOM/permissions/filesystem | System/runtime | Docker, performance, Swift/macOS |
| Container starts then exits/unhealthy | Docker | System, network, backend, database |
| Build differs locally vs CI | Build/CI | Docker, system, native app |
| Test only fails sometimes or in suite | Test flakiness | Concurrency, browser, build/CI |
| Slow/high CPU/memory/I/O | Performance | Any domain that owns the hotspot |
| Xcode crash/hang/actor isolation | Swift/macOS native | Performance, concurrency, signing |
| Launch blocked after distribution | macOS signing/sandbox | Build/CI, Swift/macOS runtime |

Load one primary playbook and only the secondary playbooks crossed by evidence.

## Complexity output

At the beginning of the investigation, emit:

```text
Mode: lightweight | systematic
Trigger: <first-pass bypass reason or hard/soft trigger>
Domains: <selected playbooks>
Risk constraints: <production/data/security/distribution constraints>
```
