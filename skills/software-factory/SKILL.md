---
name: software-factory
description: Coordinate implementation and independent QA with mandatory evidence, transient QA when tests are not deliverables, one repair, and Codex integration.
---

Use the Control Plane worker plan exactly.

For every code-changing task, independent QA is mandatory even when the prompt does not ask for tests.

Micro-task fast path means:
- one bounded implementation job;
- one independent QA job;
- Codex integration and any extra checks explicitly requested by the user.

It does NOT mean weaker testing.

Implementation acceptance requires real workspace changes and no zero-byte changed artifacts.

QA acceptance requires:
- non-empty test files;
- a relevant passing test command;
- proof that at least one test executed.

If the plan says `qa_mode=transient`, pass `--qa-mode transient`.
The worker will use `.codex-factory-qa/<job-id>/` and remove that QA-only directory after successful evidence capture.

If the plan says `qa_mode=persistent`, pass `--qa-mode persistent`; project tests are deliverables and remain.

For paths that are not valid Python package names (for example folders containing `-`), QA must not rename production code.
Use importlib file loading or subprocess execution.

One failed delegated unit gets one specialist repair; second failure means Codex takeover.
