# Rewrites, migrations and repeated repairs

**Trigger:** replaced runtime, moved state owner, schema/protocol evolution, compatibility code or the same symptom fixed repeatedly.

**Hypothesis:** old and new paths disagree about accepted behavior, both can write, or neither owns a failure transition. A repair addresses the visible exception while leaving the upstream acceptance or downstream continuation contract broken.

**Investigate:** locate accepted migration scope and the currently active owner for each consequential path. Trace startup, real entry points, data migration, resume and rollback/refusal behavior. Review a bounded history of related fixes, their tests and the next observed failure. Ask what common invariant explains the sequence without presuming all patches were wrong.

**Distinguish:** drive supported behavior through the actual replacement path and independent expected outcomes. Use the old implementation as a differential signal, not automatically the specification. Include the failed transition and a later restart/consumer action. For adaptive jobs, check whether a short-run fix persists a pathological configuration into the next process. Verify sibling fixes that rely on the same assumption.

**Counterevidence:** explicitly unfinished work is not a regression in a completed feature; dual ownership can be a controlled transition with enforced boundaries. An intentional behavior change need not match the predecessor. Do not recreate an entire language/framework's capabilities when only business-reachable or explicitly bounded behavior is required.

**Expansion/closure:** distinguish separate causes from recurring manifestations of one cause. Close only when the original invariant and affected continuation/consumers are addressed. Prefer a local contract/owner correction over another compatibility layer or wholesale rewrite. Record unresolved ownership as a decision/gap when authority is ambiguous.
