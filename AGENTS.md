# Managed Codex Software Factory v10.5.0

These instructions come from the central Git Source of Truth.

## Route authority
For every substantive request, consult `codex-route` unless the user explicitly opts out.
The FINAL Control Plane route is authoritative. Users do not need to mention routing or delegation.

## Quality invariant
Reducing orchestration ceremony must never reduce validation rigor.

For every code-changing delivery:
1. implementation output must pass structural integrity checks;
2. every changed implementation artifact must be non-empty;
3. independent QA runs after implementation, even if the user did not request tests;
4. QA must create/find non-empty tests, execute a relevant test command successfully, and prove at least one test ran;
5. a worker statement that something passed is not evidence.

## Micro-task fast path
When `task_shape.micro_task=true`, use exactly the worker plan returned by the Control Plane.

Typical micro code flow:
- one implementation job;
- one independent QA job;
- Codex integration/requested gates.

Do not split tiny README/documentation into a separate writer job.
Do not omit QA.

When tests are not part of the user's requested final artifacts, the QA plan has `qa_mode=transient`.
Pass the plan's worker args to `remote-code-worker`. Transient tests live only under the assigned
`.codex-factory-qa/<job-id>/` directory and are removed automatically after successful evidence capture.

When tests are explicitly requested as deliverables, `qa_mode=persistent`; they remain in the workspace.

The word `test` or `smoke` in a project/folder name is not itself a request for persistent test artifacts.

## Specialist factory
For larger work, decompose independently verifiable implementation responsibilities as appropriate
(backend, data, frontend, DevOps) and run QA after the implementation dependencies complete.

## Evidence
Implementation profiles normally require:
- `workspace_changes`
- `nonempty_workspace_changes`

QA requires:
- `test_files_present`
- `nonempty_test_files`
- `test_command_passed`
- `tests_executed`

## Repair
Each root delegated unit has one repair attempt. Repair owner follows the failed gate.
Second failure means Codex takeover.

## Failover
- Control Plane unavailable -> Codex continues.
- Worker unavailable -> Codex continues.
- Git unavailable -> last valid registry cache continues.
- Worker/evidence failure -> one repair, then Codex takeover.

## Final integration
Keep internal orchestration concise in the user-facing result unless it materially matters.
