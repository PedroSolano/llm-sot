---
name: qa-testing
description: Build risk-based test coverage and verification evidence.
---
Derive tests from acceptance criteria and risk. Cover positive, negative, boundary and regression cases. Prefer automated tests when feasible. Report what actually ran, what passed/failed and what remains unverified.


## Worker gate feedback
When a delegated unit fails, produce concise objective feedback for the single repair attempt: failing test names, exit code, expected vs actual behavior, and minimum violated contract item. Do not broaden scope during repair.
