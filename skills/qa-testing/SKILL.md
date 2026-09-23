---
name: qa-testing
description: Independent automated QA with real executed-test evidence and transient scratch suites when tests are not deliverables.
---

QA is independent from implementation.

Always inspect the implemented behavior before writing tests.

Evidence is mandatory:
- at least one non-empty test artifact;
- a relevant test command exits zero;
- output proves at least one test actually ran.

When `qa_mode=transient`, put QA-only tests only in the assigned `.codex-factory-qa/<job-id>/` directory.
The runtime removes that directory after successful evidence capture.

When `qa_mode=persistent`, create/update the project's real test suite.

Do not rename production directories to make them importable.
For Python targets under paths containing hyphens or otherwise not importable as packages:
- use `importlib.util.spec_from_file_location`, or
- execute the target via subprocess and validate observable behavior.

A test command that reports zero tests is a failure even if its process exit code is zero.
