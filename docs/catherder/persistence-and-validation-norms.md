---
type: reference
description: "Persistence and validation norms for CatHerder artifacts and generated work"
---
# Persistence and Validation Norms

CatHerder is optimized for durable collaboration. Prefer producing artifacts
that can be audited later.

## Persistence norms

Prefer:

- Writing decisions into the plan `Notes` section (or an ADR if the project uses ADRs)
- Storing supporting material under `.instructions/plans/planNNN*/data/`
- Using separate task files when a task is too large for a single checkbox
- Updating timestamps when an artifact changes

Avoid:

- Keeping important decisions only in chat
- Making changes without leaving a trace in the plan/task artifacts

## Validation norms

When completing a task:

- Verify using the most appropriate method:
  - Run tests/build where applicable, or
  - Provide explicit reasoning when execution is not possible

If the project has validators (format checkers, linters, task/plan validators),
run them as part of verification when feasible.

## Minimum artifact quality

- Artifacts should be clear, concise, and written for downstream readers.
- Use stable filenames and avoid unnecessary churn.

## Stop rule

Stop and ask if:

- You cannot verify work safely.
- Required inputs are missing.
- The plan/task spec conflicts with repository rules.