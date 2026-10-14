# Swift and macOS Native Application Debugging

Load this playbook for Swift, SwiftUI, AppKit, mixed Swift/Objective-C, Xcode/LLDB, native crashes, hangs, memory faults/leaks, actor/concurrency issues, lifecycle/state defects, XPC/helper behavior, or release-only native failures.

For code signing, hardened runtime, notarization, Gatekeeper, sandbox, entitlements, or distribution-only launch failures, also load [macos-signing-sandbox.md](macos-signing-sandbox.md).

## Route the native failure

Classify before choosing tools:

- compile, link, module, package, or architecture failure;
- launch/initialization or immediate crash;
- exception, signal, Swift runtime trap, or `EXC_BAD_ACCESS`;
- hang, beachball, watchdog termination, or responsiveness regression;
- memory growth/leak, use-after-free, over-release, retain cycle;
- actor isolation, data race, task ordering, cancellation, continuation misuse;
- SwiftUI/AppKit state, identity, lifecycle, run-loop, notification, or delegate issue;
- XPC service, helper tool, login item, launchd/SMAppService issue;
- debug-versus-release, Intel-versus-Apple-Silicon, local-versus-CI/distributed discrepancy.

Capture exact macOS, Xcode, SDK, Swift language mode, target deployment version, architecture, build configuration, app version/build, commit, and artifact hash.

## Preserve native artifacts

Before rebuilding or cleaning:

- preserve the exact `.app`/binary that failed;
- preserve the matching `.dSYM` and archive;
- preserve crash/hang reports, Console/unified logs, sample/spindump, and user steps;
- record whether the artifact came from Xcode Run, Archive export, CI, App Store/TestFlight, DMG/PKG/ZIP, or direct copy;
- record signing identity/entitlements when distribution may matter;
- preserve input documents and state in a privacy-safe form.

Do not delete DerivedData, app containers, preferences, or user documents before capturing evidence. A clean build can be a later control, not the opening repair.

## Crash reports and symbolication

### Read the report as structured evidence

Capture:

- process/path, app version/build, OS and hardware architecture;
- exception type/codes and termination reason;
- triggered/crashed thread;
- application-specific information and last exception backtrace;
- thread stacks and binary images;
- incident/crash UUID and timestamp.

A termination reason such as watchdog, code signing, namespace, or resource limit can require a different playbook than a normal language exception.

### Require the exact symbols

Symbolication is trustworthy only with the binary and dSYM matching the crash UUID. Compare UUIDs:

```bash
xcrun dwarfdump --uuid "MyApp.app/Contents/MacOS/MyApp"
xcrun dwarfdump --uuid "MyApp.app.dSYM"
```

Use Xcode’s crash organizer/symbolication path where available. If frames remain unsymbolicated, do not guess source lines from addresses against a different build.

Archive dSYMs for every distributed build. Rebuilding the same source is not guaranteed to produce matching symbols.

### Interpret common classes

- **Swift runtime trap:** inspect the top symbolicated application frame and trap message; common sources include failed preconditions, forced unwrap/cast, exclusivity, continuation misuse, or concurrency isolation checks.
- **`EXC_BAD_ACCESS`:** determine invalid address/access and ownership history; use Address Sanitizer, Zombies for Objective-C object lifetime, Guard Malloc/Malloc Scribble, or a watchpoint as appropriate.
- **uncaught `NSException`:** add an Objective-C exception breakpoint and inspect the first throw, not only process termination.
- **abort/fatal signal:** inspect application-specific information, assertion/fatal error, sanitizer output, and preceding logs.
- **watchdog termination:** treat as a hang/responsiveness investigation and inspect the main thread/MainActor path.

## LLDB and Xcode localization

Set breakpoints at causal transitions:

- Swift error/exception path or symbolic function;
- Objective-C exception breakpoint;
- Swift runtime failure symbols when the trap is otherwise downstream;
- state mutation or callback boundary;
- XPC interruption/invalidation;
- allocation/deallocation or write watchpoint for a narrow object/value.

Useful LLDB commands in a controlled session:

```text
bt
thread backtrace all
frame variable
p <expression>
po <object>
thread list
breakpoint set --name <symbol>
watchpoint set variable <name>
```

Inspect all threads during a deadlock or hang. Avoid expression evaluation that mutates state unless deliberately used as a reversible experiment.

## Sanitizers and runtime diagnostics

Enable the relevant diagnostic in a controlled scheme/build, generally one high-overhead tool at a time:

- **Address Sanitizer:** buffer errors, use-after-free and related memory corruption;
- **Thread Sanitizer:** conflicting memory access and some synchronization issues;
- **Undefined Behavior Sanitizer:** applicable undefined operations;
- **Main Thread Checker:** AppKit/UIKit API use from incorrect threads;
- **Zombie Objects:** messages to deallocated Objective-C objects;
- **Guard Malloc / Malloc Scribble / Malloc Stack Logging:** heap lifetime/corruption investigations.

Rules:

- Exercise the exact failing path; a clean sanitizer run on a different path proves little.
- Expect timing and memory-layout perturbation.
- Preserve the first sanitizer report and allocation/access stacks.
- Do not silence findings with unsafe annotations or broad locking before establishing ownership and intended semantics.
- Re-run without diagnostics after repair under the original build/distribution conditions.

## Memory growth and lifetime

### Xcode Memory Graph

At a stable point after the lifecycle should have ended:

1. capture a memory graph;
2. locate unexpectedly retained view models/controllers/documents/tasks;
3. inspect strong reference paths to roots;
4. compare before/after repeating the operation;
5. verify object count returns or reaches a bounded steady state after repair.

Common sources include closure captures, delegates not weak where contract requires, notifications, timers/display links, Combine/async subscriptions, tasks retaining owners, caches, windows/controllers, and XPC connections.

### Instruments and command-line tools

Use:

- Allocations for allocation history/generations;
- Leaks for leaked allocations;
- Time Profiler/System Trace when apparent memory is actually blocked work or paging;
- `vmmap <pid>` for virtual-memory regions;
- `leaks <pid>` for leak analysis;
- `heap <pid>` for heap summaries;
- `malloc_history <pid> <address>` when Malloc Stack Logging captured allocation history.

Treat RSS, Swift object counts, VM regions, caches, mapped files, and child/XPC processes separately. A restart or forced release is not a root-cause repair.

## Hangs and responsiveness

Preserve a sample before force quit when safe:

```bash
sample <pid> 10 -file hang.sample.txt
```

Use Activity Monitor Sample Process, `spindump`, Instruments Time Profiler/Hangs/System Trace, and signposts around the operation. Capture multiple samples if the wait changes over time.

Inspect:

- main thread/MainActor stack;
- synchronous disk/network/database/XPC work on the main path;
- `dispatch_sync`, semaphore, condition, lock and actor waits;
- callback into the queue/thread currently waiting;
- runaway layout/render/update loops;
- task group/continuation that never completes;
- queue saturation or priority inversion;
- modal event loop or AppKit delegate/re-entrancy behavior.

Build a wait-for graph for deadlocks. Increasing a watchdog threshold or moving arbitrary code to a background queue can hide the causal ordering or violate UI ownership.

## Swift concurrency

### Compile-time checking

For modules not already in Swift 6 language mode, use the strictest practical concurrency checking (for example Xcode’s Complete setting) to surface isolation and `Sendable` violations during migration. Treat diagnostics as design evidence about ownership, not warnings to suppress mechanically.

Inspect:

- actor/MainActor isolation of mutable state;
- values crossing actor/task boundaries and `Sendable` conformance;
- escaping closures and callbacks whose executor is not what the caller assumes;
- detached tasks losing actor context, priority, task-local values or cancellation;
- continuation resumed zero or multiple times;
- unstructured tasks outliving the owner;
- cancellation and cleanup in `defer`/`withTaskCancellationHandler`;
- synchronous bridging that blocks an actor or main thread;
- mixed Swift/Objective-C APIs whose concurrency annotations are incomplete.

### Runtime evidence

Combine strict checking with Thread Sanitizer, task/request IDs, monotonic timestamps, actor/queue labels where available, and controlled interleavings. A logical race can exist without a raw memory data race.

Do not use `@unchecked Sendable`, `nonisolated(unsafe)`, detached tasks, or global actors solely to silence diagnostics. Document and prove the ownership invariant first.

## SwiftUI and AppKit state/lifecycle

### SwiftUI

Trace:

```text
source-of-truth mutation → observation dependency → view identity → rendered effect
```

Check:

- intended ownership of `@State`, `@StateObject`, `@ObservedObject`, environment and bindings;
- view/model identity across navigation, lists and conditional branches;
- mutation executor/MainActor;
- tasks tied to view lifecycle and cancellation;
- stale captured values in closures;
- duplicate `.task`, `.onAppear`, notification or subscription work;
- server/document model updates that do not publish on the expected actor.

Use a small state transition log keyed by model/view identity rather than printing entire object graphs.

### AppKit

Inspect delegate/notification ordering, responder chain, window/controller lifetime, run-loop mode, main-thread access, KVO/observation lifetime, and re-entrant callbacks. Mixed Objective-C lifetime issues may require Zombies or exception breakpoints.

## Unified logging and signposts

Use `Logger`/OSLog with stable subsystem and category. Log IDs, state transitions, durations and error classes; use privacy annotations and avoid secrets/user content.

Controlled queries:

```bash
/usr/bin/log stream --level debug --predicate 'subsystem == "com.example.app"'
/usr/bin/log show --last 10m --style compact --predicate 'process == "MyApp"'
```

Use signposts around user operations, import/export, XPC, persistence and expensive work so Instruments can correlate samples with the causal transaction. Remove temporary high-volume logging or make it appropriately gated.

## XPC services, helpers, and login items

Trace both processes with a shared operation ID. Capture:

- connection creation, interruption and invalidation handlers;
- request/reply and timeout/cancellation behavior;
- helper/XPC binary version and actual embedded path;
- process launch/exit and unified logs;
- protocol/schema compatibility;
- signing team/bundle IDs and entitlements;
- sandbox/app-group/file-access boundary;
- whether a stale registered helper differs from the app bundle.

A client timeout does not prove the XPC service never executed. Verify both sides and side effects. Load signing/sandbox playbook for launch or permission failures.

## Release-only and architecture-only failures

Compare one variable at a time:

- Debug versus Release optimization and assertions;
- Xcode Run versus Archive/exported artifact;
- arm64 versus x86_64/Rosetta and dependency slices;
- sandbox/hardened runtime/signature entitlements;
- local machine state versus clean user/clean Mac;
- CI toolchain/SDK/package resolution;
- installed helper/service/version versus bundled version.

Test the exact archived/exported artifact and retain its dSYM. Do not assume a fresh local build represents the distributed binary.

## Common causal chains

```text
synchronous file parsing on MainActor → beachball → watchdog termination
unstructured Task captures view model → view closes but task retains owner → memory grows per open
continuation resumed twice on error+success paths → Swift runtime trap
shared mutable state marked unchecked Sendable → logical race persists despite compiler silence
archive embeds stale helper → XPC protocol skew → works from Xcode but fails after install
release optimization changes timing → latent race appears only in distributed build
```

## Completion evidence

- symbolicated crash or synchronized hang/concurrency timeline;
- matching binary/dSYM/build configuration;
- sanitizer, memory graph, profile, log, or LLDB evidence at the first divergence;
- regression test/reproduction in the original architecture and release mode;
- exact archived/distributed artifact verified when applicable;
- no unsafe concurrency annotation, broad background dispatch, cache deletion, or state reset substituted for causal repair.
