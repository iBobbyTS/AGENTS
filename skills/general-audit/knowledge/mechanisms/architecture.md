# Architecture, coherence and unnecessary complexity

**Trigger:** duplicated rules, shifting ownership, accumulating compatibility layers, repeated cross-module fixes, unsupported flexibility or expensive change paths.

**Hypothesis:** locally reasonable abstractions distribute one invariant among conflicting owners; new features copied a workaround instead of resolving its cause; a compatibility layer now serves no supported consumer but obscures the active path.

**Distinguish:** select a real recent or upcoming change scenario and trace which owners must change together. Find actual call sites, runtime loading, exported APIs, supported configurations and historical decisions. Demonstrate a duplicated decision, conflicting result, repeated repair cost, blocked evolution or unused mechanism under the supported scope. For “can delete,” test counterexamples such as plugins, reflection, generated registration, deployment variants and recovery paths before declaring no consumer.

**Counterevidence:** one implementation, an extra file or a wrapper is not automatically bloat. A boundary can enforce security, ownership, testing isolation or a real future commitment. Repetition may preserve independent domain meaning better than a shared abstraction. Less code is not necessarily fewer states or safer change.

**Expansion:** follow common decision ownership, not aesthetic inconsistency. Compare a small consolidation/removal with the existing design's tradeoffs. Preserve supported behavior, safety guards and deliberate local constraints. Avoid a repository-wide rewrite to cure one painful seam.

**Closure:** a finding can be grounded in demonstrated maintenance cost without a crash, but must explain the consequence and a smaller corrective direction. Generic naming/style preferences belong to existing linters or optional suggestions, not the defect count.

Do not import another organization's layer model or cleanup preferences as product authority.
