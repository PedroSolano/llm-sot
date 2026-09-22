---
name: orchestration
description: Route every task through the central Control Plane and execute the selected Codex/Worker/Hybrid path.
---

The FINAL Control Plane route is authoritative.

Before substantial execution, obtain the route. Use `recommended_factory_roles`, `recommended_agents`, `recommended_skills` and `quality_gates` as execution context.

When delegating to Qwen, pass the relevant context:

```text
remote-code-worker --agent <agent> --skill <skill> ...
```

If omitted, the worker auto-selects a shared factory profile from the current Git registry.

- `worker`: delegate bounded execution-heavy work, then Codex reviews.
- `hybrid`: Codex owns reasoning/contracts/acceptance criteria; worker executes the bounded heavy phase; Codex integrates and reviews.
- `codex`: Codex performs the task directly.

Skills/agents never override the route. If the worker actually fails, Codex takes over the remaining work.
