---
name: long-document
description: Draft long technical documents efficiently by separating structure/fact decisions from high-volume prose generation.
---

The Control Plane route is authoritative. This skill never overrides it.

For a long, detailed, or well-structured technical guide/manual/document,
`hybrid` is the normal execution pattern when the worker is available:

1. Codex defines audience, outline, factual constraints, evidence requirements,
   terminology, and acceptance criteria.
2. The remote worker drafts the high-volume prose or bounded sections.
3. Codex reviews the complete result for accuracy, coherence, omissions, and
   adherence to the requested format.

For `worker`, delegate the bounded drafting/transformation and review it.

For `codex`, perform the task locally only because the Control Plane explicitly
returned `codex` or failover rules require it. Never claim that this skill makes
Codex "the better option" and use that as a reason to ignore a `worker` or
`hybrid` route.
