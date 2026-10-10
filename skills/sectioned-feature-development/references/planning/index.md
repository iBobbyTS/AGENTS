# Planning knowledge index

One lookup index for the four routing axes. Consult a section only when a dimension's mapping is uncertain or materially changed; select from actual **changed** paths, read the matched specialized guides, and use [universal](universal.md) only for a named uncovered part. This index is not a product checklist or requirement source.

## Domain — what engineering outcome is this change delivering?

These are engineering domains, not invented industry/regulatory requirements. Domain does not select language/framework.

| Route | Select from evidence | Guide |
|---|---|---|
| AI / ML / model-enabled features | The product change concerns training/evaluation/inference, retrieval, model outputs or agent/tool behavior. | [ai-ml.md](domains/ai-ml.md) |
| Backend services / APIs | The task changes a service handler, business operation, job consumer or exposed API. | [backend-services.md](domains/backend-services.md) |
| CLI / automation / developer tooling | A requested outcome is a command, build/developer utility, batch script or terminal automation. | [cli-automation.md](domains/cli-automation.md) |
| Cloud / platform / DevOps | Deployment/configuration/IaC/CI/service-operability behavior is the requested change. | [cloud-platform-devops.md](domains/cloud-platform-devops.md) |
| Data engineering / pipelines / analytics delivery | The change ingests/transforms/materializes datasets or alters delivery to analytical/operational consumers. | [data-engineering.md](domains/data-engineering.md) |
| Desktop applications | A requested feature changes window/document/editor/device/helper workflows in a desktop application. | [desktop-apps.md](domains/desktop-apps.md) |
| Embedded / IoT / device control | The feature changes firmware, hardware interaction, sensor/control pipeline or constrained-device state. | [embedded-iot.md](domains/embedded-iot.md) |
| Full-stack application delivery | One requested outcome crosses UI/client, service/data and direct readers. | [full-stack.md](domains/full-stack.md) |
| Games / real-time interactive media | The feature changes gameplay, simulation/render timing, entity lifecycle or interactive media behavior. | [games-realtime.md](domains/games-realtime.md) |
| Libraries / SDKs / reusable packages | A public reusable library/API/package is the deliverable or changes observably. | [libraries-sdks.md](domains/libraries-sdks.md) |
| Mobile applications | The change targets a mobile user workflow or its platform lifecycle/data behavior. | [mobile-apps.md](domains/mobile-apps.md) |
| Scientific / numerical / simulation software | The change computes a scientific/numerical result or modifies a simulation/analysis contract. | [scientific-computing.md](domains/scientific-computing.md) |
| Systems software / daemons / local IPC | The feature changes a long-lived service, IPC/protocol handler, process lifecycle or resource owner. | [systems-daemons.md](domains/systems-daemons.md) |
| Web frontend / interaction | A requested change concerns browser-visible interaction, navigation, rendering or client state. | [web-frontend.md](domains/web-frontend.md) |

## Language — which source/query/script/markup semantics actually change?

Language does not imply domain, framework, OS or runtime.

| Route | Select from evidence | Guide |
|---|---|---|
| Bash / POSIX shell | Changed shell scripts or shell command composition. | [bash-posix-shell.md](languages/bash-posix-shell.md) |
| C | Changed C translation units, headers or a C ABI boundary. | [c.md](languages/c.md) |
| C++ | Changed C++ objects/templates, ownership, concurrency or binary interface. | [cpp.md](languages/cpp.md) |
| C# | Changed C# logic or .NET-facing public types. | [csharp.md](languages/csharp.md) |
| Dart | Changed Dart library, async stream/future or isolate boundary. | [dart.md](languages/dart.md) |
| Go | Changed Go package, executable or concurrency contract. | [go.md](languages/go.md) |
| HTML / CSS (markup and style languages) | Changed HTML semantics, form controls, styles or layout selectors. | [html-css.md](languages/html-css.md) |
| Java | Actual Java source, class/module API or Java runtime behavior is changed. | [java.md](languages/java.md) |
| JavaScript | Changed JavaScript logic, Promise/callback composition or module boundary. | [javascript.md](languages/javascript.md) |
| Kotlin | Changed Kotlin source, coroutine/Flow contract or Java interop. | [kotlin.md](languages/kotlin.md) |
| Lua | Changed Lua code or a Lua embedding boundary. | [lua.md](languages/lua.md) |
| PHP | Changed PHP request, command, package or long-lived worker source. | [php.md](languages/php.md) |
| PowerShell | Changed .ps1/.psm1 or PowerShell command/parameter logic. | [powershell.md](languages/powershell.md) |
| Python | Changed Python application, library, CLI or job source. | [python.md](languages/python.md) |
| R | Changed R analysis/package/statistical transformation. | [r.md](languages/r.md) |
| Ruby | Changed Ruby method/module, IO, extension boundary or package. | [ruby.md](languages/ruby.md) |
| Rust | Changed Rust crate, binary, trait/serde contract or FFI owner. | [rust.md](languages/rust.md) |
| SQL | SQL queries, schema/constraint expressions or database-visible semantics are changed. | [sql.md](languages/sql.md) |
| Swift | Changed Swift source, actor/task, value/reference or public module boundary. | [swift.md](languages/swift.md) |
| TypeScript | Changed .ts/.tsx source or a public declaration/generic contract. | [typescript.md](languages/typescript.md) |

## Adapter — which actual framework/runtime/platform changes the contract?

Host-installed tools are not automatically dependencies of the changed path.

| Route | Select from evidence | Guide |
|---|---|---|
| Angular | Changed Angular component, service, router or dependency lifetime. | [frameworks/angular.md](adapters/frameworks/angular.md) |
| ASP.NET Core | Changed ASP.NET Core endpoint, middleware, DI service or background lifecycle. | [frameworks/aspnet-core.md](adapters/frameworks/aspnet-core.md) |
| Django | Changed Django view/model/ORM/transaction/migration code. | [frameworks/django.md](adapters/frameworks/django.md) |
| FastAPI | Changed FastAPI route/dependency/serialization or lifespan behavior. | [frameworks/fastapi.md](adapters/frameworks/fastapi.md) |
| Flutter | Changed Flutter widgets, navigation, model binding or plugin boundary. | [frameworks/flutter.md](adapters/frameworks/flutter.md) |
| Laravel | Changed Laravel controller/Eloquent/job/lifecycle code. | [frameworks/laravel.md](adapters/frameworks/laravel.md) |
| Next.js | Changed Next.js routing, Server/Client Components, mutation or caching path. | [frameworks/nextjs.md](adapters/frameworks/nextjs.md) |
| Ruby on Rails | Changed Rails route/model/callback/transaction or job path. | [frameworks/rails.md](adapters/frameworks/rails.md) |
| React | Changed React components/hooks or React-owned state. | [frameworks/react.md](adapters/frameworks/react.md) |
| Spring | Changed Spring-managed controller/service/transaction/lifecycle path. | [frameworks/spring.md](adapters/frameworks/spring.md) |
| Svelte / SvelteKit | Changed Svelte components or SvelteKit action/load/endpoint/consumer code. | [frameworks/svelte-sveltekit.md](adapters/frameworks/svelte-sveltekit.md) |
| SwiftUI / AppKit | Changed SwiftUI views/model binding or AppKit delegate/bridge behavior. | [frameworks/swiftui-appkit.md](adapters/frameworks/swiftui-appkit.md) |
| Vue / Nuxt | Changed Vue components/reactivity or a confirmed Nuxt server/render path. | [frameworks/vue-nuxt.md](adapters/frameworks/vue-nuxt.md) |
| Android | Changed Android lifecycle/component, permission, data or packaged behavior. | [platforms/android.md](adapters/platforms/android.md) |
| iOS / iPadOS | Changed Apple mobile scenes, app lifecycle, permission, storage or delivery path. | [platforms/apple-mobile.md](adapters/platforms/apple-mobile.md) |
| Browser web platform | Changed browser DOM/events/fetch/history/storage/worker semantics. | [platforms/browser.md](adapters/platforms/browser.md) |
| macOS | Changed macOS app/window/helper/XPC/device or packaged launch behavior. | [platforms/macos.md](adapters/platforms/macos.md) |
| Node.js | Changed Node runtime-specific stream, process, file, worker or module behavior. | [runtimes/nodejs.md](adapters/runtimes/nodejs.md) |
| Tokio | Changed Tokio select/task/channel/process path in real Rust source. | [runtimes/tokio.md](adapters/runtimes/tokio.md) |

## Concern — which cross-cutting semantics actually change?

Do not add reviews, model tiers or performance infrastructure because a guide was listed. `NOT_APPLICABLE` is not a coverage gap.

| Route | Select from evidence | Guide | Do not select merely because |
|---|---|---|---|
| Data evolution | The change affects persisted representation, migration, import/backfill, conversion, atomicity or compatibility of existing data. | [data-evolution.md](concerns/data-evolution.md) | Code reads a database without changing those semantics. |
| Async lifecycle | The change affects async ownership, pending/late results, cancellation, retries, cleanup or process lifetime. | [async-lifecycle.md](concerns/async-lifecycle.md) | An `async` keyword exists in untouched code. |
| External integration | The change crosses an actual service/SDK/device/agent/IPC contract, capability, auth or error boundary. | [external-integration.md](concerns/external-integration.md) | Development uses an AI assistant or a dependency is merely installed. |
| Performance and cardinality | The acceptance path has a concrete input-size, latency, memory, complexity or cost constraint. | [performance.md](concerns/performance.md) | Future growth can be imagined without a current workload or obligation. |

Retain independent matches; a non-applicable dimension does not need fallback. A guide selects questions, not architecture, model tier, section count or extra tests.
