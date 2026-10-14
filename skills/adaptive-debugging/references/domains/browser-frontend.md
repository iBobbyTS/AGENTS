# Browser and Frontend Debugging

Load this playbook for DOM/rendering defects, stale UI state, hydration mismatches, browser storage/cache problems, service workers, Svelte/SvelteKit behavior, or Playwright browser-test failures.

## Establish the browser failure contract

Capture:

- exact URL, route parameters, navigation sequence, and whether failure follows a reload, client navigation, back/forward navigation, or a fresh session;
- browser/version, viewport/device emulation, extensions, locale/timezone, authentication state, and feature flags;
- whether the page is SSR, prerendered, CSR, or transitions between server and client execution;
- expected DOM/state and observed DOM/state;
- the request/response or event that should cause the UI change;
- cache, storage, cookie, service-worker, and offline state;
- a screenshot or trace only when it preserves evidence not represented by text.

Compare a failing browser context with a clean incognito/new profile control before deleting user state.

## Localize in this order

### 1. Console and source mapping

- Preserve the first exception, rejection, warning, and stack trace; downstream errors may be secondary.
- Verify that source maps point to the exact deployed build. A line in stale source is not reliable evidence.
- Enable pause on uncaught exceptions; include caught exceptions when an error appears swallowed.
- Check browser and server consoles separately in SSR applications.

### 2. Network boundary

Use the Network panel with Preserve log when navigation matters. For the relevant request inspect:

- method, URL, query, request body, cookies/auth, initiator, redirects;
- status, response headers, response body, timing, cache/service-worker source;
- preflight request and CORS headers when the browser blocks access;
- whether the request was sent at all and whether it was aborted or superseded.

Compare three states:

```text
server response → client data object/store → rendered DOM
```

The first divergence determines whether to load backend/network playbooks.

Disabling the browser cache is a diagnostic control, not a repair. If it changes behavior, identify the actual HTTP, framework, application, or service-worker cache contract.

### 3. Runtime breakpoints

Prefer a breakpoint that stops at the transition where state diverges:

- event-listener breakpoint for an input/click/submit path;
- XHR/fetch breakpoint for a request trigger;
- DOM mutation breakpoint for unexpected node changes;
- source breakpoint or conditional breakpoint around the state update;
- exception breakpoint for thrown/rejected failures;
- watch expression for the smallest causal state.

Step through one event path. Avoid broad logging that creates timing changes or obscures event order.

### 4. Application storage and service workers

Inspect, do not immediately clear:

- cookies and SameSite/Secure/domain/path attributes;
- localStorage/sessionStorage/IndexedDB values and schema/version;
- Cache Storage entries and cache keys;
- active/waiting service worker, scope, update lifecycle, fetch interception, and offline fallback;
- whether a stale service worker serves an old HTML/JS pair that cannot hydrate together.

Use a clean profile and “bypass service worker” as controls. If these controls pass, fix lifecycle/version/cache invalidation rather than teaching users to clear storage.

### 5. Performance and memory

When the symptom is jank, long task, layout shift, or memory growth:

- capture a Performance recording around the smallest reproduction;
- inspect main-thread long tasks, scripting, style/layout, paint, network, and event timing;
- use allocation sampling/heap snapshots to compare retained objects before and after the lifecycle;
- identify a retaining path before removing listeners or changing state ownership;
- load [performance.md](performance.md) for measurement discipline.

## Svelte and SvelteKit checks

### Server/client state boundary

- Do not store request-specific or user-specific mutable state in a module-level server variable or shared server store.
- Determine where each `load`, action, hook, and component executes. Log server and browser events with distinct labels and a request/navigation ID.
- Check whether data is serialized from server `load` and then reused during hydration.
- Confirm that browser-only APIs are not read during SSR in a way that changes initial markup.

### Hydration mismatch

Compare:

1. server-rendered HTML;
2. client inputs available at hydration;
3. first client render.

Look for time/randomness, locale/timezone, browser-only conditions, non-deterministic iteration, stale asset versions, and state mutated between SSR and hydration. Fix parity at the source; suppressing the warning is not a repair.

### `load` dependencies and invalidation

- Identify every URL/resource or custom dependency the `load` function consumes.
- Verify whether client navigation is expected to rerun it.
- Check `depends`, `invalidate`, `invalidateAll`, parent data, route params, search params, and fetch dependencies.
- Distinguish “load did not rerun” from “load reran but a downstream store/component retained stale state.”
- Avoid side effects in `load`; repeated execution and navigation invalidation make side-effect timing unreliable.

### Preserved component/page state

On navigation between routes that reuse a component:

- inspect component identity and whether the instance is preserved;
- determine whether local state should reset or follow route data;
- compare reactive dependencies with the state actually read;
- verify cleanup of subscriptions, timers, observers, and event listeners.

### Form actions and errors

Trace the exact sequence:

```text
submit event → request payload → action validation/auth → action result/redirect/error → form enhancement/update
```

Confirm status codes and structured validation errors. Distinguish expected failures returned to the form from unexpected exceptions. Do not turn every exception into a success-shaped payload.

## Playwright workflow

### Preserve the failing execution

Run the smallest failing test with the same project, browser, environment, worker count, and seed/order as the failure. Useful controls include:

```bash
npx playwright test path/to/test.spec.ts --project=<project> --trace on
npx playwright test path/to/test.spec.ts --project=<project> --debug
npx playwright show-trace path/to/trace.zip
```

Inspect trace snapshots, actions, locators, console, requests, responses, and timing. A screenshot alone often misses the causal event.

### Test or product defect?

Compare the trace with the product contract:

- Did the locator target the intended accessible element?
- Was the element actionable, or did an overlay/animation/navigation replace it?
- Did the action trigger the expected request/state transition?
- Is the assertion observing stable user-visible state rather than an implementation detail?
- Is each test isolated with its own context, account/data, clock, and cleanup?

Do not fix flakiness with `waitForTimeout`, excessive retries, or brittle CSS/XPath selectors. Use condition-based locators/assertions and repair the product or isolation source.

## Common causal chains

```text
stale service worker → old JS + new HTML → hydration mismatch
shared server module state → user A data visible in user B request → stale/wrong UI
missing load dependency → client navigation does not invalidate data → old DOM
request aborted during navigation → state update never commits → spinner persists
listener not cleaned up → duplicate handlers → duplicate API mutations
passing retry → timing window remains → test marked green but product race persists
```

## Completion evidence

- reproduce with the original browser/session/navigation conditions;
- show where response/state/DOM first diverged;
- retain a Playwright regression test when the user-visible behavior is automatable;
- verify both fresh load and client navigation when SSR/hydration is involved;
- verify service-worker upgrade paths when caching caused the defect.
