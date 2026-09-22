---
name: orchestration
description: Route through the Control Plane and execute CODEX/WORKER/HYBRID with bounded worker jobs, one repair attempt, and failover.
---

The FINAL route is authoritative.

For `CODEX`, execute directly. For `WORKER`, delegate bounded mechanical/execution-heavy work. For `HYBRID`, Codex owns framing/contracts/acceptance criteria and final integration/review; follow `worker_plan` sequentially.

After every worker job run the gate. First gate failure: exactly one `remote-code-worker --repair-of JOB_ID --feedback ...`. Second failure: Codex takeover. Never retry the worker a second time for the same root job.

Emit `codex-factory-event` with the final worker outcome. Skills/agents never change the final route.
