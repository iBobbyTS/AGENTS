# Performance and input-cardinality planning

Select for a requested performance/resource outcome or concrete source evidence of an input-growth hazard. “Could be faster” alone does not justify this route.

## Define the measurable question

Name the actual workload, input sizes, environment and user-visible metric: latency, throughput, memory, disk, startup, UI responsiveness or queue growth. Separate a measured baseline from an estimate. Where no SLO is authorized, use a before/after hypothesis without inventing a threshold.

Identify growth factors, not just line count: product of alternatives, repeated scans, N+1 queries, unbounded queues/retention and large materializations. A combinatorial generator needs a representative worst-case input before its implementation is split among workers. Choose the authoritative algorithm/query/queue owner.

## Decompose and verify

Keep semantic equivalence with the optimization. Define correctness examples plus a smallest reproducible workload, bound environment noise, and state what observation would falsify the proposed improvement. Do not benchmark every unrelated module.

A diagnostic/measurement step is not automatically a product section. Internal algorithm or storage increments can be subsections if they preserve one parent invariant and use the same comparison fixture. Reuse known successful functional evidence where unchanged; measure again only when the relevant code/environment changes.

## Avoid

No benchmark platform, cache, index fleet, actor framework, parallel rewrite, new SLO or generalized monitoring absent authority. A faster isolated helper does not prove faster end-to-end behavior. Do not trade away correctness to satisfy a self-imposed cost target.

## Basis

This lens synthesizes the existing Skill's cardinality/oracle rule, the supplied adaptive-debugging performance playbook's discriminating-evidence approach, and outcome-oriented planning. It is a heuristic, not a measured speedup claim. Basis: local source — the supplied adaptive-debugging performance playbook.
