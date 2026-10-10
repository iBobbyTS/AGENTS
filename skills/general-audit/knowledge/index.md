# Knowledge index

28 canonical cards; no complete-world claim and no requirement to read all. Use [router](router.md) by actual question.

## Outcome / domain
| Card | Concrete trigger |
|---|---|
| [Services](domains/services.md) | Business effect across requests/jobs/state/consumers |
| [Clients](domains/clients.md) | Local/server divergence, lifecycle and user interaction |
| [Data/science](domains/data-science.md) | Numerical/population meaning and pipeline completeness |
| [Tools/libraries](domains/tools-libraries.md) | Real import/CLI/package consumer |
| [Systems/devices](domains/systems-devices.md) | Native resources, protocols or physical behavior |
| [AI products](domains/ai-products.md) | Models/agents actually used by the running product |

## Failure mechanism
| Card | Concrete trigger |
|---|---|
| [Authorization](mechanisms/authorization.md) | Trust, privilege, alternate entry or exposure |
| [Durable state](mechanisms/durable-state.md) | Required effects across writes/checkpoints |
| [Async ownership](mechanisms/async-ownership.md) | Retry/cancel/ack/concurrent owners |
| [Recovery](mechanisms/recovery.md) | Detectability, containment, usable restore/startup |
| [Capacity/progress](mechanisms/capacity-progress.md) | Real limits, growing work and continuation |
| [Architecture](mechanisms/architecture.md) | Ownership, repeated cross-boundary cost, parallel mechanisms |
| [Supply chain](mechanisms/supply-chain.md) | Trust in code/dependencies/build privilege/distribution |
| [Verification system](mechanisms/verification-system.md) | Test-suite selection, blind spots, flake and confidence |

## Actual technology semantics
| Card | Concrete trigger |
|---|---|
| [SQL/ORM](technology/sql.md) | Effects/isolation/bind limits/app state |
| [Tasks/processes](technology/task-process.md) | Real runtime and OS lifetime semantics |
| [Web state](technology/web-state.md) | Scope and reconciliation of server/client state |
| [Release/shell](technology/release-shell.md) | Argument/environment/file-selection behavior |

## Evolution
| Card | Concrete trigger |
|---|---|
| [AI-led](evolution/ai-led.md) | Shared generated assumptions/workarounds/evidence claims |
| [Migration/repeated repair](evolution/migration-repairs.md) | Old/new owners, recurring failures and unfinished change |
| [Behavior contract](evolution/behavior-contract.md) | Scope/semantic drift, compatibility vs intended change |
| [Process effectiveness](evolution/process-effectiveness.md) | Actual development workflow cost, failures and missing evidence |

## Evidence
| Card | Concrete trigger |
|---|---|
| [Oracles](evidence/oracles.md) | Independent expected behavior |
| [Population](evidence/population.md) | Actual objects/attempts tested versus summaries |
| [Experiments](evidence/experiments.md) | Safe distinguishing probes and interpretation |

## Release application contexts — shared by all modes
| Card | Concrete trigger |
|---|---|
| [Artifact identity](release/artifact-identity.md) | Source/tested/distributed object or target mismatch |
| [Environment](release/environment.md) | Install/start/consumer runtime, config, permission or dependency drift |
| [Transition](release/transition.md) | Reachable version/coexistence/order and recovery limits |

These are not extra copies of domain, SQL or recovery knowledge. Select those canonical cards as needed. No database is presumed for release work.
