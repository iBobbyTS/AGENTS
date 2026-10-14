# Systems, native boundaries and devices

**Use when:** the contract crosses processes, memory/resource ownership, native interfaces, device protocols or physical effects. Do not select merely because the language is C++, Rust or Swift.

**Misleading reassurance:** type checking protects one language boundary but not the foreign owner, binary layout, device state or physical effect. A simulated sensor/driver always answers promptly and with ideal values.

**Investigate:** identify who allocates, owns, transfers and releases resources; who can concurrently act; and what happens when either side restarts or disconnects. Inspect actual ABI/serialization, lengths, units, numeric range, timing assumptions and capability negotiation at the relevant seam. Use sanitizers/static tools when available and safe; no manual generic pointer-syntax checklist is required.

**Distinguish:** inspect real generated bindings/protocol fields and a matching consumer fixture. Exercise a bounded timeout/disconnect/partial-transfer sequence on a safe simulator or disposable local process. Verify resulting resource/state ownership, not just the caller's error. For devices, distinguish encoded command correctness from measured physical output.

**Counterevidence:** upstream constraints, hardware interlocks or ownership rules may rule out a suspected sequence, but trace the actual implementation. Tolerated packet loss or a lossy shutdown can be part of the contract. Do not invent hard-real-time requirements or actuate real hardware without permission.

**Expand/stop:** an unknown driver/runtime uses the fallback for that seam; retain applicable mechanisms. A synthetic probe cannot certify device safety. Missing physical evidence should precisely limit claims rather than halt all software inspection.

Controlled simulation is one example, not a requirement to build that infrastructure; other probes are boundary-driven suggestions.
