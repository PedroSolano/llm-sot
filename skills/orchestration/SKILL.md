---
name: orchestration
description: Route every Codex task through the central control-plane policy and follow codex/worker/hybrid decisions with safe fallbacks.
---

Use `codex-route` before substantive work unless the user explicitly requests
that orchestration itself not be used.

The FINAL route returned by the Control Plane is authoritative:

- `worker`: delegate the bounded token-heavy work with `remote-code-worker`,
  then review.
- `hybrid`: Codex performs reasoning/retrieval/outline/acceptance criteria;
  delegate the token-heavy bounded portion; Codex reviews/finalizes.
- `codex`: Codex performs the task directly.

A skill, custom agent, or Codex capability must never be used to override a
`worker` or `hybrid` route. Skills determine execution method inside the route,
not route selection.

If the worker actually fails, continue in Codex. If the Control Plane is
unavailable, use the Codex failover returned by `codex-route`.
