# Managed Codex Software Factory

These instructions originate from the central GitHub registry and are applied automatically.

## Automatic Layer 0 bootstrap

No manual bootstrap is required during normal use.

The client background daemon synchronizes the Git registry continuously and applies:
- this AGENTS.md;
- custom agents;
- skills;
- factory role/workflow definitions;
- routing policy.

The installed CLI/VS Code launch hooks also trigger an immediate best-effort `codex-bootstrap` before launching `codex` or `code`. If GitHub is unavailable, use the last valid local cache and continue. Never block work because Git sync failed.

## Control Plane routing

For every substantive request, use `codex-route` unless the user explicitly opts out of orchestration.

The FINAL route is authoritative:
- `codex`: Codex executes.
- `worker`: delegate bounded execution-heavy work with `remote-code-worker`, then review.
- `hybrid`: Codex owns decisions/contracts/acceptance criteria; delegate the heavy bounded phase; Codex integrates/reviews.

Never replace WORKER/HYBRID with CODEX merely because a local skill or agent appears capable.

## Software Factory

Treat software work as a selective software factory. Use the relevant disciplines from `factory/roles.json`; do not invoke every role mechanically.

Typical disciplines include product/requirements, architecture, UX/UI, frontend, backend, data, QA, security, DevOps/platform, SRE/observability, code review, release and documentation.

For code-changing tasks, QA evidence and code review are normally mandatory. Add security, release and observability gates when the risk/change requires them.

Use `software-factory` for multi-discipline work. Each handoff must state:
- input/context;
- constraints/contracts;
- expected output;
- acceptance/verification.

## Shared Codex + Qwen context

The same Git registry is used by Codex and the remote Qwen worker.

When delegating, pass the Control Plane recommendations when practical:

```text
remote-code-worker \
  --agent cp-backend-developer \
  --skill backend-engineering \
  --skill qa-testing \
  "bounded delegated task..."
```

If no profile is passed, the worker automatically infers a factory role from `factory/roles.json`. The worker receives the selected agent/skill contracts in its system context.

## Hard failover

The router and worker are optional optimizations.

If the Control Plane is unavailable, Codex performs the entire request. Do not call Qwen behind the router.

If the Control Plane is available but the worker fails/unavailable, Codex takes over the remaining request without retry loops.

## Research

Codex performs current/web retrieval and source validation. Qwen may synthesize only bounded supplied material under a HYBRID route.

## Final integration

Before delivery, verify relevant acceptance criteria, tests, security findings, operational impact and documentation. Report unverified areas explicitly.
