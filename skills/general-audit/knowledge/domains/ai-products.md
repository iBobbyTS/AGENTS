# Products that actually use models or agents

**Use when:** runtime behavior depends on an ML/LLM model, retrieval, probabilistic decisions or tool-using agents. Keep this separate from software merely developed by AI.

**Misleading reassurance:** an evaluator likes the answer or the agent says it succeeded, while the external state is wrong; prompt-level instructions are mistaken for an enforced authorization boundary.

**Investigate:** trace user intent → trusted policy → retrieved/untrusted content → model decision → tool permission/effect → observable outcome. Identify what is enforced outside the model, what data can cross tenants or external providers, and who owns retries, cancellation and cost. Inspect evaluation population and grade the result against a product requirement independent of the generating prompt.

**Distinguish:** use safe synthetic untrusted content and disposable tools to check whether the actual permission boundary prevents the relevant unauthorized effect. Validate structured outputs against the real consumer, not only a schema example. Check final system state, denied actions and representative failure cases. For variable outputs, record actual trials and uncertainty; a single success does not estimate reliability.

**Counterevidence:** a sandbox, capability restriction or human confirmation enforced outside the model may contain the consequence. A deliberately advisory product can tolerate uncertainty that an autonomous writer cannot. Do not claim a filter, prompt or finite adversarial set proves immunity.

**Expand/stop:** investigate the shared permission/retrieval/evaluation owner. Do not add an AI safety platform or demand arbitrary benchmark scores without a product need. Missing access to a hosted model limits runtime evidence, not source inspection of the effect boundary.

Model evaluation and permission checks complement, not replace, ordinary system auditing.
