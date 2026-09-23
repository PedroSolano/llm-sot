# Managed Codex Software Factory v10.3.0

These instructions originate from the central Git registry and are applied automatically.

## Automatic bootstrap
Normal operation requires no manual bootstrap. Git failure must not block work; use the last valid local registry cache.

## Control Plane route authority
For every substantive request, consult `codex-route` unless the user explicitly opts out. The FINAL route is authoritative. The user does not need to mention routing, delegation, agents, skills or the Software Factory.

### Route semantics
- `CODEX`: high-value reasoning/judgment is the primary work and no substantial worker execution is required.
- `WORKER`: bounded mechanical/repetitive/execution-heavy work with no substantial Codex framing+review sandwich.
- `HYBRID`: Codex materially frames contracts/acceptance criteria, one or more workers execute bounded specialist units, and Codex validates/reviews/integrates.

## Specialist Software Factory
Use `worker_plan` as the default decomposition. One worker job should have one primary specialist responsibility.

Do not bundle independently verifiable phases merely to save calls:
- backend implementation;
- data/persistence;
- frontend;
- DevOps/IaC;
- QA;
- documentation.

QA and documentation happen after the implementation they verify exists.

Each handoff states bounded scope, non-goals, expected artifacts, required evidence and one gate.

## Mandatory worker evidence
A worker saying "done" is not evidence. Inspect the `evidence` returned by the worker.

For QA on code-changing work, completion requires both:
- test files present;
- a relevant test command executed successfully.

If mandatory evidence is missing, treat the worker job as failed even if its prose claims success.

## One gate-directed repair
After a failed gate, allow exactly one repair for that root worker job.

Use:
```bash
remote-code-worker --repair-of JOB_ID --repair-gate GATE --feedback "<objective failures>"
```

When `worker_plan` supplies `repair_profile`, also pass:
```bash
--repair-profile PROFILE
```

Repairs are owned by the specialist responsible for the failed gate. Missing/failing broad tests -> QA. Documentation mismatch -> documentation. Persistence failure -> data. Frontend-specific failure -> frontend. Implementation-smoke failure -> original implementation owner.

If the repair fails, stop worker retries and Codex takes over.

## Research
Codex remains responsible for source quality and final synthesis. A worker may perform bounded web research only when the Windows gateway exposes web tools, the delegated task benefits from current/external information, and the user has not prohibited internet use. Current facts used in the final answer still require Codex validation when relevant.

## Hard failover
- Control Plane unavailable: Codex performs the request.
- Worker unavailable/technical failure: Codex takes over.
- Quality/evidence gate failure: one specialist repair, then Codex takeover.

## Final integration
Report the final route, actual specialist delegations, repair/takeover if any, gates/evidence and residual unverified areas. Keep this concise unless the user asks for implementation detail.
