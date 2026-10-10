# Small decisive probes, not ritual test volume

**Trigger:** ambiguous runtime semantics, a stateful/cross-boundary claim, or a strong conclusion resting on a weak mock. Source proof may already suffice; do not execute merely to check a box.

**Design:** specify competing explanations and the single observation that separates them. Preserve the relevant real expression, ownership, serialization, isolation or scheduling semantics. Use actual producers/consumers where feasible; otherwise label the extraction/model and omitted assumptions. Include a legitimate control case so the probe does not simply reject all behavior.

For a long scenario, target the failure transition and continuation rather than repeating a full endurance run by habit. For concurrency, a controlled barrier/scheduler can expose a specific interleaving more reliably than random sleeps. A small model illustrates a mechanism; only an actual target run establishes that target's observation. Do not generalize finite stress tests to all schedules or workloads.

**Safety:** examine the invoked code and its environment, use disposable state, bound resources/time/effects, and avoid production credentials and external data transfer. Permission to read is not permission for load tests or destructive fault injection. Lack of a safe runtime is a reason to narrow evidence, not to secretly cross a boundary.

**Interpretation:** retain command, relevant version/configuration, result and material limitation. An environment failure is not a product finding. A failing oracle/fixture must be corrected before drawing a product conclusion; preserve its earlier result as superseded, not secretly rerun to select only success.

**Stop/pivot:** if repeated probes cannot distinguish the explanations, state the missing observable or access and continue other priorities. A new testing platform, simulation framework or extra reviewer needs its own cost/benefit justification.

This card motivates targeted evidence, not a universal testing pyramid for every audit.
