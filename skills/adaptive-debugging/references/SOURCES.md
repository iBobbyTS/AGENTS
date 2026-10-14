# Official Source Catalog

Accessed and synthesized on **2026-08-10**. The playbooks are original paraphrases and operational checklists; they do not reproduce the source documents. Prefer the documentation matching the deployed tool/runtime version when commands or UI differ.

## Skill format and orchestration comparison

- [OpenAI — Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Open Agent Skills specification](https://agentskills.io/)
- [obra/superpowers — systematic-debugging SKILL.md](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md)
- [obra/superpowers — license](https://github.com/obra/superpowers/blob/main/LICENSE)

Used for: progressive disclosure, `SKILL.md`/`references`/`scripts`/`agents/openai.yaml` layout, implicit-invocation description design, local skill paths, disabling an overlapping skill, and comparison with Superpowers’ always-on trigger.

## Browser, frontend, SvelteKit, and Playwright

### Chrome DevTools

- [Debug JavaScript](https://developer.chrome.com/docs/devtools/javascript)
- [Pause code with breakpoints](https://developer.chrome.com/docs/devtools/javascript/breakpoints)
- [Inspect network activity](https://developer.chrome.com/docs/devtools/network)
- [Network panel reference](https://developer.chrome.com/docs/devtools/network/reference)
- [Analyze runtime performance](https://developer.chrome.com/docs/devtools/performance)
- [Memory panel overview](https://developer.chrome.com/docs/devtools/memory)
- [Application panel overview](https://developer.chrome.com/docs/devtools/application)
- [Debug Progressive Web Apps / service workers](https://developer.chrome.com/docs/devtools/progressive-web-apps)
- [JavaScript source maps](https://developer.chrome.com/docs/devtools/javascript/source-maps)

### SvelteKit

- [State management](https://svelte.dev/docs/kit/state-management)
- [Loading data](https://svelte.dev/docs/kit/load)
- [Form actions](https://svelte.dev/docs/kit/form-actions)
- [Errors](https://svelte.dev/docs/kit/errors)
- [Navigation APIs](https://svelte.dev/docs/kit/%24app-navigation)
- [Page options / SSR and CSR](https://svelte.dev/docs/kit/page-options)

### Playwright

- [Trace viewer](https://playwright.dev/docs/trace-viewer)
- [Trace viewer introduction](https://playwright.dev/docs/trace-viewer-intro)
- [Debugging tests](https://playwright.dev/docs/debug)
- [Test isolation / browser contexts](https://playwright.dev/docs/browser-contexts)
- [Best practices](https://playwright.dev/docs/best-practices)
- [Retries](https://playwright.dev/docs/test-retries)
- [Command line](https://playwright.dev/docs/test-cli)

### Browser platform behavior

- [MDN — Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
- [MDN — Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)

Used for: response-versus-render localization, event/XHR/DOM breakpoints, cache and service-worker controls, performance/memory recordings, SvelteKit server state/load invalidation/hydration, Playwright traces and test isolation, and CORS/preflight diagnosis.

## Backend, observability, Node.js, and Python

### OpenTelemetry

- [Traces](https://opentelemetry.io/docs/concepts/signals/traces/)
- [Context propagation](https://opentelemetry.io/docs/concepts/context-propagation/)
- [OpenTelemetry logs specification](https://opentelemetry.io/docs/specs/otel/logs/)
- [Collector troubleshooting](https://opentelemetry.io/docs/collector/troubleshooting/)
- [Collector internal telemetry](https://opentelemetry.io/docs/collector/internal-telemetry/)

### Node.js

- [Inspector API](https://nodejs.org/api/inspector.html)
- [Diagnostic reports](https://nodejs.org/api/report.html)
- [The Node.js event loop](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick)
- [Memory diagnostics](https://nodejs.org/en/learn/diagnostics/memory)
- [Diagnostics Channel API](https://nodejs.org/api/diagnostics_channel.html)
- [Command-line options](https://nodejs.org/api/cli.html)

### Python

- [`pdb` — Python debugger](https://docs.python.org/3/library/pdb.html)
- [`faulthandler`](https://docs.python.org/3/library/faulthandler.html)
- [Developing with `asyncio`](https://docs.python.org/3/library/asyncio-dev.html)
- [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html)
- [Python Development Mode](https://docs.python.org/3/library/devmode.html)

Used for: cross-process correlation, structured log fields, Node inspector/reports/event-loop/memory evidence, Python breakpoints/fault stack capture/async debug/memory tracing, and safe observability boundaries.

## PostgreSQL

- [Cumulative statistics system and `pg_stat_activity`](https://www.postgresql.org/docs/current/monitoring-stats.html)
- [Using `EXPLAIN`](https://www.postgresql.org/docs/current/using-explain.html)
- [Explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html)
- [`pg_locks`](https://www.postgresql.org/docs/current/view-pg-locks.html)
- [Transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
- [`pg_stat_statements`](https://www.postgresql.org/docs/current/pgstatstatements.html)
- [`auto_explain`](https://www.postgresql.org/docs/current/auto-explain.html)
- [Planner statistics](https://www.postgresql.org/docs/current/planner-stats.html)
- [Error reporting and logging](https://www.postgresql.org/docs/current/runtime-config-logging.html)

Used for: activity/wait/blocking evidence, lock and transaction analysis, safe plan inspection, serialization retries, schema/session context, aggregate query statistics, and the warning that `EXPLAIN ANALYZE` executes its statement.

## Docker and containers

- [`docker inspect`](https://docs.docker.com/reference/cli/docker/inspect/)
- [Dockerfile reference, including `HEALTHCHECK`](https://docs.docker.com/reference/dockerfile/)
- [`docker compose up`](https://docs.docker.com/reference/cli/docker/compose/up/)
- [`docker compose logs`](https://docs.docker.com/reference/cli/docker/compose/logs/)
- [Docker Engine daemon troubleshooting](https://docs.docker.com/engine/daemon/troubleshoot/)
- [Container networking](https://docs.docker.com/engine/network/)
- [Runtime resource constraints](https://docs.docker.com/engine/containers/resource_constraints/)

Used for: immutable image/runtime identity, health output, logs, entrypoint/PID 1, mounts, namespaces, Compose configuration, clean-build controls, and resource-limit evidence.

## Build and CI

- [GitHub Actions — Enable debug logging](https://docs.github.com/en/actions/how-tos/monitor-workflows/enable-debug-logging)
- [GitHub Actions — Re-run workflows and jobs](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/re-run-workflows-and-jobs)
- [GitHub Actions — Workflow run logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs)
- [GitHub Actions — Contexts reference](https://docs.github.com/en/actions/reference/contexts-reference)
- [GitHub Actions — Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)

Used for: exact SHA/ref/event identity, runner/step diagnostics, matrix and permissions analysis, cache/artifact evidence, and same-event rerun semantics.

## Concurrency and sanitizers

- [Clang AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html)
- [Clang ThreadSanitizer](https://clang.llvm.org/docs/ThreadSanitizer.html)
- [Clang UndefinedBehaviorSanitizer](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html)
- [Go data race detector](https://go.dev/doc/articles/race_detector)
- [Python asyncio debug mode](https://docs.python.org/3/library/asyncio-dev.html)
- [Swift 6 concurrency migration guide — enabling data-race safety](https://www.swift.org/migration/documentation/swift-6-concurrency-migration-guide/enabledataracesafety/)

Used for: detector scope and overhead, runtime path coverage, controlled scheduling, and distinguishing memory data races from logical ordering failures.

## Network and system runtime

### Network

- [curl command-line manual](https://curl.se/docs/manpage.html)
- [Wireshark User’s Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
- [OpenSSL `s_client`](https://docs.openssl.org/master/man1/openssl-s_client/)
- [MDN CORS guide](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)

### Linux/systemd/kernel

- [`journalctl` manual](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html)
- [`systemctl` manual](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html)
- [Linux kernel cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html)
- [Linux Pressure Stall Information](https://docs.kernel.org/accounting/psi.html)
- [Linux perf tutorial](https://perf.wiki.kernel.org/index.php/Tutorial)

Used for: DNS/TCP/TLS/HTTP boundary ordering, curl trace privacy, packet-filtered capture, service-manager evidence, cgroup limits/OOM, resource pressure, and process/filesystem identity.

## Swift, Xcode, and macOS native applications

### Crashes, symbols, runtime diagnostics

- [Diagnosing issues using crash reports and device logs](https://developer.apple.com/documentation/xcode/diagnosing-issues-using-crash-reports-and-device-logs)
- [Adding identifiable symbol names to a crash report](https://developer.apple.com/documentation/xcode/adding-identifiable-symbol-names-to-a-crash-report)
- [Diagnosing memory, thread, and crash issues early](https://developer.apple.com/documentation/xcode/diagnosing-memory-thread-and-crash-issues-early)
- [Setting breakpoints to pause your running app](https://developer.apple.com/documentation/xcode/setting-breakpoints-to-pause-your-running-app)
- [Understanding the exception types in a crash report](https://developer.apple.com/documentation/xcode/understanding-the-exception-types-in-a-crash-report)
- [Investigating memory access crashes](https://developer.apple.com/documentation/xcode/investigating-memory-access-crashes)

### Hangs, performance, memory, and logging

- [Understanding hangs in your app](https://developer.apple.com/documentation/xcode/understanding-hangs-in-your-app)
- [Improving your app’s performance](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance)
- [Gathering information about memory use](https://developer.apple.com/documentation/xcode/gathering-information-about-memory-use)
- [Apple Logging framework](https://developer.apple.com/documentation/os/logging)
- [`OSSignposter`](https://developer.apple.com/documentation/os/ossignposter)
- [Tracking Memory Usage (archive)](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/FindingPatterns.html)
- [Enabling the Malloc Debugging Features (archive)](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/MallocDebug.html)
- [Viewing Virtual Memory Usage (archive)](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/VMPages.html)

### Swift concurrency

- [Swift 6 migration guide — enabling data-race safety](https://www.swift.org/migration/documentation/swift-6-concurrency-migration-guide/enabledataracesafety/)
- [Swift 6 migration guide — migration strategy](https://www.swift.org/migration/documentation/swift-6-concurrency-migration-guide/migrationstrategy/)
- [SE-0337 — Incremental migration to concurrency checking](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0337-support-incremental-migration-to-concurrency-checking.md)
- [SE-0423 — Dynamic actor isolation enforcement](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0423-dynamic-actor-isolation.md)

Used for: crash-report fields, exact dSYM/UUID symbolication, LLDB and runtime diagnostics, sanitizer/memory graph/Instruments workflows, hang samples, unified logging/signposts, and strict Swift concurrency checking.

## macOS signing, notarization, Gatekeeper, and sandbox

- [Creating distribution-signed code for macOS](https://developer.apple.com/documentation/xcode/creating-distribution-signed-code-for-the-mac)
- [Configuring the hardened runtime](https://developer.apple.com/documentation/xcode/configuring-the-hardened-runtime)
- [Notarizing macOS software before distribution](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution)
- [Resolving common notarization issues](https://developer.apple.com/documentation/security/resolving-common-notarization-issues)
- [Configuring the macOS App Sandbox](https://developer.apple.com/documentation/xcode/configuring-the-macos-app-sandbox)
- [Accessing files from the macOS App Sandbox](https://developer.apple.com/documentation/security/accessing-files-from-the-macos-app-sandbox)
- [TN2206 — macOS Code Signing In Depth](https://developer.apple.com/library/archive/technotes/tn2206/_index.html)
- [Apple Developer Technical Support forum index containing “--deep Considered Harmful” guidance](https://developer.apple.com/forums/topics/code-signing-topic/code-signing-topic-general?page=2&sortBy=oldest)

Used for: inside-out nested signing, sealed resources, hardened runtime, actual signed entitlements, notarization logs and stapling, real quarantined distribution testing, security-scoped file access, and the rule not to use `codesign --deep` as a signing strategy.

## Maintenance rule

When a command, build setting, entitlement, sanitizer availability, Xcode UI, GitHub runner image, Node/Python version, PostgreSQL major version, or Docker behavior is version-sensitive:

1. identify the deployed version;
2. open the matching official documentation;
3. treat this catalog as routing, not a substitute for version-specific verification;
4. update the relevant playbook and the access date if behavior materially changes.
