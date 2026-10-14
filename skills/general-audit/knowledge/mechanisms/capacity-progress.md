# Capacity, cost and long-run progress

**Trigger:** accepted batch limits, fan-out, buffered results, retries, adaptive chunking, growing state, continuation or sustained load.

**Hypothesis:** a public limit counts objects while the downstream limit counts parameters/bytes; local retry success hides multiplied work; adaptation only shrinks across restarts; a job stays busy without moving the business cursor.

**Distinguish:** trace the accepted bound to actual downstream cardinality, fixed overhead and concurrent multiplication. Check just below/at/above the real boundary in an isolated bounded test. For long-running work, observe progress across interruption and a **new process**, including persisted batch size, remaining work, retry budget and termination reason. Separate temporary deferral from permanent starvation.

**Counterevidence:** supported workloads may be bounded, a small batch may be an intentional safety policy, and resource ceilings may be deployment-dependent. Do not infer a performance defect from asymptotic notation alone. Establish a real throughput/cost/latency constraint or clearly label an unmeasured risk.

**Expansion:** a shared limit helper or persisted adaptation policy warrants sibling inspection. Derive actual configured/compiled limits rather than importing constants from another database or version. Do not force a 192-hour experiment when a decisive transition probe answers the question; also do not label a transition model as a passed endurance run.

**Closure:** the accepting boundary and actual consumer agree, and supported work continues to make progress under the activated scenario. Proposals should preserve safety bounds while addressing the observed bottleneck, not introduce a generic autoscaling platform.
