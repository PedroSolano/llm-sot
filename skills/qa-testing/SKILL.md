---
name: qa-testing
description: Build automated risk-based coverage and return concrete execution evidence.
---

Derive tests from acceptance criteria and risk. Cover positive, negative, boundary and regression cases.

For delegated code QA:
- inspect the existing implementation first;
- create or update actual test files;
- do not use external network unless the test contract explicitly requires an integration test;
- execute the relevant test command;
- do not mark completion if no test artifact exists;
- do not mark completion if the test command did not run successfully;
- report command, result, test count when available, failures and remaining unverified areas.

When a gate fails, repair feedback must be objective: failing test names, exit code, expected vs actual behavior, missing test artifacts, or violated acceptance criteria. Do not broaden scope.
