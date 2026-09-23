---
name: software-factory
description: Coordinate selective software disciplines using specialist jobs, objective evidence, one gate-directed repair attempt, and Codex integration.
---

Use only relevant disciplines. Split independently verifiable responsibilities into separate worker jobs. In particular, do not bundle backend/data/frontend implementation with broad QA or documentation merely to reduce the number of calls.

Each handoff must contain:
- one specialist responsibility;
- bounded scope and explicit non-goals;
- inputs/contracts;
- expected files/artifacts;
- required evidence;
- one measurable gate.

Worker completion is not acceptance. Codex runs the gate.

For QA on code-changing work, required worker evidence is normally:
- test files exist;
- a relevant test command actually ran;
- the command passed;
- the worker reports what ran.

A first gate failure gets exactly one specialist repair. Route the repair to the role responsible for the failed gate rather than automatically reusing the original implementation profile. After a failed repair, Codex takes over.

WORKER remains bounded mechanical/execution work. Material Codex framing plus worker execution plus material Codex validation/review is HYBRID.
