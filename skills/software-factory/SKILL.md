---
name: software-factory
description: Coordinate selective software disciplines using small specialist jobs, measurable gates, one worker repair attempt, and Codex integration.
---

Use only relevant disciplines. Prefer separate worker jobs for backend+tightly-coupled data, frontend, QA, documentation, and DevOps/IaC when independently testable.

Each handoff must contain bounded scope, inputs/contracts, explicit non-goals, expected output/files, and one measurable gate.

Codex runs every gate. A failed worker delivery gets one repair attempt using objective feedback; if repair fails, Codex takes over.

WORKER is reserved for bounded mechanical/execution-only work. Material Codex framing before worker execution plus material Codex validation/review afterward is HYBRID.
