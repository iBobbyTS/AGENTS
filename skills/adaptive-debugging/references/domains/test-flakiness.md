# Test Flakiness Debugging

Load this playbook when a test alternates pass/fail, fails only in a suite, parallel run, CI, retry, specific order, or under timing/load variation.

A retry that passes is evidence of nondeterminism; it is not a fix.

## Preserve the failing identity

Capture:

- commit/build and exact test binary/config;
- test name, project/browser/device, worker count;
- seed, shard, order and preceding tests;
- environment, clock/timezone/locale;
- retries and which attempt failed;
- trace, screenshots/video, logs, requests, DB state, crash dump;
- duration/resource pressure and external dependency state.

Do not rerun until transient artifacts from the first failure are preserved.

## Classify the dependency

Test controlled variations to classify:

- **timing:** condition becomes true eventually but test observes too early;
- **order/shared state:** another test or prior run changes global/persistent state;
- **parallelism/concurrency:** workers compete for identifiers, ports, files, rows, accounts, or locks;
- **random data/seed:** generated input exposes an edge case;
- **environment:** CI runner, architecture, browser, locale, timezone, permissions, filesystem;
- **external service/network:** availability, latency, rate limit, eventual consistency;
- **clock:** expiration, date boundary, timers, daylight saving;
- **resource pressure:** CPU, memory, descriptors, database pool, queue depth;
- **test defect:** unstable locator/assertion or implementation-detail expectation;
- **product defect:** real race/state bug exposed by the test.

## Experiment matrix

Run the smallest useful comparisons:

```text
same seed/order repeatedly
isolated test versus full suite
one worker versus original parallelism
fresh state versus reused state
local versus CI-like container/runner
fixed virtual clock versus wall clock
real dependency versus deterministic fake
```

State what each comparison predicts. Do not run many random repetitions without recording seed/order and environment.

## Isolation audit

Check ownership and cleanup of:

- user/account/database rows;
- files/directories/download names;
- ports/processes/server instances;
- browser contexts, cookies, storage, service workers;
- environment variables and module/global state;
- fake timers and clock changes;
- mocks/spies/stubs and dependency injection;
- queues/jobs/messages;
- transactions and connection pools.

Each test should create unique state or reset it through a reliable contract. Cleanup must run on failure/cancellation and must not delete another worker’s state.

## Waiting and synchronization

Replace fixed sleeps with a condition tied to the product contract:

- visible/accessible UI state;
- response/event completion;
- database/queue state with bounded polling;
- task/future completion;
- virtual clock advancement;
- explicit barrier in a test-only dependency.

A longer timeout may reduce frequency while preserving the race. Measure the actual readiness signal.

## Playwright-specific checks

Load [browser-frontend.md](browser-frontend.md). Use trace viewer to inspect action snapshots, locator resolution, network, console and timing. Prefer accessible locators and web-first assertions. Keep each test in an isolated browser context and use unique server-side data.

Do not accept:

- `waitForTimeout` as synchronization;
- high retry count as resolution;
- broad force-click that bypasses actionability without explaining the UI state;
- screenshot-only diagnosis;
- serializing the whole suite unless shared-state semantics require it and are documented.

## Test-order pollution

When isolated test passes but suite fails:

1. Preserve the failing order.
2. Bisect preceding tests or use order randomization with recorded seed.
3. Compare global/process/database/browser state before and after the polluting test.
4. Identify the resource that crosses the intended isolation boundary.
5. Add a regression that runs polluter then victim when practical.

## Product race versus test race

A test can be correct while exposing a product timing defect. Determine whether a real user can reach the same state transition. If yes, repair the product and retain the test. If no, repair the test contract without weakening valid user-visible assertions.

## Acceptance evidence

- deterministic reproduction or a preserved statistical trigger;
- classified dependency and first shared/timing boundary;
- regression test that fails under the old behavior;
- repeated execution under the original parallelism/order/environment;
- retries returned to normal policy and quarantine removed or explicitly documented;
- residual failure-rate uncertainty disclosed when the trigger cannot be made fully deterministic.
