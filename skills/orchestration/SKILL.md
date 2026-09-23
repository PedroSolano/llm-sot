---
name: orchestration
description: Execute Control Plane routes with implementation integrity, mandatory independent QA, one specialist repair and failover.
---

The FINAL route is authoritative.

Follow `worker_plan` sequentially. For each job pass its profile, agent and skills to `remote-code-worker`.

If a plan item contains `worker_args`, pass those arguments too. In particular:
- `--qa-mode transient` means QA-only tests are temporary;
- `--qa-mode persistent` means tests are final project artifacts.

Do not invent extra specialist jobs beyond the plan, but never skip the QA job returned for a code change.

After each worker job, inspect objective evidence and run `gate_after`.

On first failure:
`remote-code-worker --repair-of JOB_ID --repair-gate GATE --feedback "<objective failures>"`

Use the plan's repair profile when supplied. Second failure means Codex takeover.

A successful implementation with zero-byte changed files is impossible: the implementation worker must fail evidence first.
QA succeeds only after a real test command passes and at least one test actually executes.
