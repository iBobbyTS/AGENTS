# Node.js

Axis: `adapter/runtime`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Node runtime-specific stream, process, file, worker or module behavior.

Do not select merely because JavaScript/TypeScript runs in a browser or another host.

## Decisions before sectioning

- Inspect active Node version, ESM/CommonJS boundary and actual installed entry.
- For streams define backpressure, error, EOF, close and completion ownership.
- For children/workers define stop/reap and lost response behavior; event-loop responsiveness differs from mere Promise use.

## Handoff and smallest useful evidence

Use actual stream/process interfaces with bounded data and relevant close/error cases; avoid test-only fake protocol clients.

## Scope boundary

No runtime migration, global worker pool or logging of arbitrary raw subprocess output. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Node streams](https://nodejs.org/api/stream.html); [MDN promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
