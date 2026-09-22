---
name: orchestration
description: Route every Codex task through the central control-plane policy and follow codex/worker/hybrid decisions with safe fallbacks.
---

Use `codex-route` before substantive work unless the user explicitly requests
that orchestration itself not be used.

For `worker`, delegate the bounded execution task with `remote-code-worker`.
For `hybrid`, keep architecture/retrieval/decisions in Codex and delegate the
token-heavy execution. For `codex`, perform the task in Codex.

If the worker fails, continue in Codex. If the control plane fails, accept the
local fallback route returned by `codex-route`.
