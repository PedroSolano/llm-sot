---
name: software-factory
description: Coordinate multi-discipline software delivery with explicit handoffs and quality gates.
---
The Control Plane route is authoritative.

Operate as a selective software factory, not a ritual checklist. Identify the change type, then select only relevant roles from `factory/roles.json`.

For code-changing work, normally require:
1. clear acceptance criteria;
2. implementation owner(s);
3. QA/regression evidence;
4. code review;
5. security/release/observability gates when the change touches those risks.

For HYBRID, Codex owns decomposition, decisions, cross-role contracts and final integration review. Delegate bounded execution-heavy phases to the worker using the relevant shared agent/skills. Every handoff must state inputs, constraints, expected output and verification.
