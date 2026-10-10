# Planning composition examples

These examples are not facts about the user's repositories; always use the actual changed source and requirements. Common entry: router once, the planning index for uncertain dimensions, then necessary source-matched guides. Universal is loaded for a named uncovered part; boundary-handoff is added for a shared changed contract.

| Changed task | Domains | Languages | Adapters | Concerns when activated |
|---|---|---|---|---|
| Svelte TypeScript client + Java Spring controller | full-stack | TypeScript, Java | Svelte/SvelteKit, Spring; browser for browser-specific semantics | external-integration/data-evolution when those semantics change |
| Single-repo SvelteKit TypeScript reorder feature | full-stack | TypeScript | Svelte/SvelteKit | boundary-handoff for the shared contract; async-lifecycle for stale/rollback behavior |
| React/Next server/client feature | full-stack | TypeScript | Next.js; React for a separate state/effect question | actual cache/mutation/async concerns |
| Vue/Nuxt component interaction only | web-frontend | TypeScript | Vue/Nuxt | relevant lifecycle |
| Angular client + C# ASP.NET Core API | full-stack | TypeScript, C# | Angular, ASP.NET Core | actual changed API/data/async boundary |
| Python FastAPI endpoint | backend-services | Python | FastAPI | actual external/data concern |
| Python CLI import | cli-automation | Python; SQL when query semantics change | none by default | data-evolution for changed import atomicity |
| Python Airflow data transformation | data-engineering | Python/SQL actually edited | installed Airflow source for a missing adapter | replay/partition/scale concerns as required |
| Python training/inference change | ai-ml | Python | actual ML framework via source or fallback | performance/data when changed |
| R analysis package | scientific-computing; libraries-sdks if publication changes | R | none by default | numeric tolerance/reproducibility; performance with a bound |
| Swift server route | backend-services | Swift | actual server framework via fallback | — |
| SwiftUI macOS UI controlling Rust helper | desktop-apps; systems-daemons if helper lifetime changes | Swift, Rust | SwiftUI/AppKit, macOS; Tokio when actually used | async-lifecycle; one IPC contract |
| C# desktop editor | desktop-apps | C# | actual Windows UI framework via fallback | — |
| Kotlin Android application | mobile-apps | Kotlin | Android | task/back-stack/process lifecycle when changed |
| Swift iOS/iPadOS scene | mobile-apps | Swift | Apple mobile; SwiftUI/AppKit when that UI family is used | actual scene/task lifecycle |
| Flutter phone/tablet feature | mobile-apps | Dart | Flutter; OS adapter for a native platform seam | async-lifecycle when relevant |
| Go network service | backend-services | Go | actual service runtime via source | cancellation/backpressure where changed |
| Rust synchronous reusable crate | libraries-sdks | Rust | none | — |
| TypeScript command-line tool | cli-automation | TypeScript | Node.js when stream/process behavior matters | — |
| POSIX shell release automation | cli-automation or cloud-platform-devops | Bash/POSIX shell | actual host/toolchain source | error propagation/resource cleanup as required |
| PowerShell deployment command | cloud-platform-devops | PowerShell | actual host/remote API source | — |
| C firmware ISR change | embedded-iot | C | board/RTOS source via fallback | timing/ownership |
| C++ game simulation update | games-realtime | C++ | engine source via fallback | frame/tick timing; performance for concrete requirements |
| Lua host extension | libraries-sdks or actual host domain | Lua | real host binding source | — |
| PHP Laravel background job | backend-services | PHP | Laravel | queue transaction/retry semantics when changed |
| Ruby Rails write + callback | backend-services | Ruby | Rails | transaction/commit/external side-effect boundary |
| HTML/CSS layout/semantic form change | web-frontend | HTML/CSS; JS when changed | browser when layout/event semantics matter | — |
| Elixir/OCaml or another unlisted backend | backend-services | universal fallback for unlisted language | actual framework/version source as needed | independently matched concerns |
| Unknown device/API used by a known language | actual domain if known | actual known language | universal fallback for unknown adapter | external-integration with a bounded probe |

A table row is not a mandatory load set: select the smallest applicable guides for the actual unresolved questions.
