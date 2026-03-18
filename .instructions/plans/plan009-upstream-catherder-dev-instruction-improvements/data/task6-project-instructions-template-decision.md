---
type: reference
description: "Plan 009 Task 6 decision on whether repo/instructions should publish a reusable project.instructions.md template/example"
---
# Plan 009 Task 6 — `project.instructions.md` Template Decision

## Decision

Do **not** add a published `repo/instructions/project.instructions.md` template/example at this time.

Keep `project.instructions.md` as a **documented pattern** defined in canonical docs rather than as a copy-ready shared artifact.

## Rationale

### 1. `project.instructions.md` is intentionally repository-specific
Unlike `catherder.instructions.md` and `catherder-git.instructions.md`, `project.instructions.md` is expected to encode repository-local structure, document map choices, and important local distinctions. That makes it less suitable as a copy-ready artifact.

### 2. A generic template risks cargo-cult copying
A published file in `repo/instructions/` is likely to be copied with minimal thought. For `project.instructions.md`, that would increase the risk of:
- stale or incorrect repository-structure sections
- duplicated or irrelevant document-map entries
- unnecessary prompt bloat from boilerplate not tailored to the target repo

### 3. The pattern is already strong enough in canonical docs
`docs/catherder/project-structure.md` now documents:
- the role of `project.instructions.md`
- that it owns entry/navigation guidance
- that it should use a document map and conditional reading
- that `catherder.instructions.md` should stay process-only

`repo/instructions/README.md` also explains that enabled projects should create `project.instructions.md` locally and what it should contain.

### 4. Concision is better served by local authoring
The current improvement goal is to minimize context use and duplication. Forcing a reusable template too early would likely produce over-generalized boilerplate rather than concise repository-specific guidance.

## Implementation Consequence

- `repo/instructions/` remains limited to reusable shared instruction artifacts:
  - `catherder.instructions.md`
  - `catherder-git.instructions.md`
  - `README.md`
- Canonical docs remain the source for the recommended `project.instructions.md` pattern.
- Downstream repositories should author `project.instructions.md` locally, guided by `docs/catherder/project-structure.md` and `repo/instructions/README.md`.

## Revisit Trigger

Revisit this decision later only if one of these conditions becomes true:
- repeated onboarding failures show that teams need a starter example
- multiple repositories converge on a stable, low-bloat shared shape
- we decide to publish an explicitly labeled example rather than a copy-ready template

## Status

Decision recorded and implemented by retaining documentation-only guidance.
