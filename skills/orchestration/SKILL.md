---
name: orchestration
description: Route through the Control Plane and execute CODEX/WORKER/HYBRID with specialist jobs, evidence gates, one gate-directed repair, and failover.
---

The FINAL route is authoritative.

For HYBRID, follow `worker_plan` sequentially. Each plan item is a separate specialist job unless Codex has objective evidence that two listed units are inseparable.

Pass the plan item's `profile`, `agent` and `skills` to `remote-code-worker`. Do not silently merge QA or documentation back into an implementation job.

After every worker job, inspect its returned evidence and run `gate_after`.

On first gate failure, use exactly one repair:
`remote-code-worker --repair-of JOB_ID --repair-gate GATE --feedback "<objective failures>"`

If the Control Plane provided `repair_profile`, pass it as `--repair-profile`. The client also infers common specialists from gate/feedback as a fallback.

Second failure for the same root job means Codex takeover. Never create an unbounded retry loop.

Emit `codex-factory-event` with the final worker outcome.
