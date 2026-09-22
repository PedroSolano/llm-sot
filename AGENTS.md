# Managed Codex environment instructions

These instructions originate from the central GitHub Codex Registry.

## Layer 0 — Git registry bootstrap

At the beginning of each NEW Codex conversation/workspace, before substantive
work, run `codex-bootstrap` once.

`codex-bootstrap` asks the out-of-sandbox client daemon to refresh the GitHub
registry and apply the latest AGENTS, custom agents, skills, and routing policy.
If GitHub is unavailable, continue immediately with the last valid cached
revision. Never block the user's work because Git sync failed.

The Git registry is independent from the router and remote LLM. Agents and
skills must remain usable even if all local AI infrastructure is offline.

## Routing

For each user request after bootstrap:

- If the user explicitly says not to use the remote/local LLM or not to
  delegate, primary Codex does the complete task.
- Otherwise call `codex-route` before substantial execution.

Routes:

- `codex`: primary Codex performs everything.
- `worker`: delegate bounded execution-heavy work to `remote-code-worker`, then
  review.
- `hybrid`: Codex does reasoning/retrieval/architecture, Qwen executes the
  bounded high-volume portion, then Codex reviews.


### Route authority

The final route returned by the Control Plane is authoritative for execution.
Do not replace `worker` or `hybrid` with `codex` merely because a Codex skill,
custom agent, or local capability appears suitable. Skills describe HOW to
execute the selected route; they do not choose a different route.

When the final route is `worker` or `hybrid` and `worker_required=true`,
attempt the bounded worker delegation before doing the token-heavy portion in
Codex. Codex may take over only after an actual worker/control-plane failure
covered by the failover rules.

For `hybrid`, Codex must retain the high-value portion (outline, decisions,
facts, retrieval, acceptance criteria, review) and delegate the identified
high-volume portion. Do not interpret `hybrid` as permission for Codex to do
the entire task without attempting delegation.

## Hard failover

The router and Qwen are optional optimizations.

If the Control Plane/router is unavailable, primary Codex performs the entire
request. Do NOT locally reproduce a WORKER/HYBRID route and do NOT call Qwen
behind the router's back.

If the router is available but Qwen is unavailable/fails, primary Codex takes
over the entire remaining request. Do not loop on retries.

## Research

For current/web research, Codex performs retrieval and source validation. Qwen
may synthesize only the bounded material when the router returns `hybrid`.

## Review

Review important reasoning, diffs, tests, facts, citations/source handling, and
security-sensitive changes before final delivery.
