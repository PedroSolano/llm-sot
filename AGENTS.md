# Managed Codex Software Factory v10.1.0

These instructions originate from the central Git registry and are applied automatically.

## Automatic bootstrap
Normal operation requires no manual bootstrap. Git failure must not block work; use the last valid local registry cache.

## Control Plane route authority
For every substantive request, consult `codex-route` unless the user explicitly opts out. The FINAL route is authoritative.

### Route semantics
- `CODEX`: high-value reasoning/judgment is the primary work and no substantial worker execution is required.
- `WORKER`: bounded mechanical/repetitive/execution-heavy work. Codex may perform lightweight verification, but must not own substantial framing before the worker and substantial review/repair after it.
- `HYBRID`: Codex owns architecture/contracts/acceptance criteria or other material framing, the worker executes a bounded heavy phase, and Codex performs material validation/review/integration afterward.

If Codex must define a contract/criteria before delegation and test/review the worker result afterward, the route is HYBRID even if Qwen performs most edits. Skills/agents never override the route.

## Selective Software Factory
Use only relevant disciplines. For code-changing work, QA evidence and code review are normal gates. Add security/release/SRE when relevant.

Use Control Plane fields: `recommended_factory_roles`, `recommended_agents`, `recommended_skills`, `quality_gates`, `worker_plan`, and `worker_execution`.

## HYBRID / worker decomposition
Do not send one oversized worker job when `worker_plan` contains multiple phases. For each phase:
1. Codex states bounded scope, contracts, non-goals and measurable gate.
2. Delegate that phase with `remote-code-worker`.
3. Run the gate.
4. If it passes, continue.
5. If it fails, allow exactly one Qwen repair: `remote-code-worker --repair-of <JOB_ID> --feedback "<objective failures>"`.
6. Rerun the gate.
7. If repair still fails, stop worker retries and Codex takes over.

Never create an unbounded worker retry loop.

## Worker repair budget
The client enforces one repair attempt per root worker job. Repair feedback must be objective: failing tests, exit code, compiler/linter errors, violated contract items, concise file/line findings. Do not broaden scope during repair.

## Factory telemetry
After the final gate for a delegated unit, emit one prompt-free metadata event:

```bash
codex-factory-event --outcome accepted_first_pass --worker-job JOB_ID --role backend --skill backend-engineering --gate qa --gate code-review
```

```bash
codex-factory-event --outcome accepted_after_repair --worker-job JOB_ID --repair-job REPAIR_JOB_ID --role backend --gate qa
```

```bash
codex-factory-event --outcome codex_takeover --worker-job JOB_ID --role backend --gate qa
```

Include `--route-job` when available and roles/skills actually executed by Codex.

## Hard failover
- Control Plane unavailable: Codex performs the request; do not call Qwen behind the router.
- Worker unavailable/technical failure: Codex takes over.
- Quality gate failure: one repair attempt, then Codex takeover.

## Research
Codex performs current/web retrieval and source validation. Qwen may synthesize bounded supplied/local material under the selected route.

## Final integration
Report final route, actual delegation(s), repair attempt if any, takeover if any, gates/evidence, and residual unverified areas.
