---
type: reference
description: "Operational distinction between planning and execution in CatHerder, and how to switch safely"
---
# Planning vs Execution

CatHerder enforces a strict separation:

- **Plans** define intent (what/why).
- **Tasks** execute intent (how).

This separation reduces drift and makes long-running work auditable.

## Planning mode

You are in **planning** when:

- Creating or updating `planNNN-prompt.md`, `planNNN-draft.md`, or `planNNN.md`
- Breaking a large goal into tasks
- Resolving open questions, tradeoffs, or architecture

Rules:

- You may modify plan files.
- You must not start implementation work that belongs in tasks.

## Execution mode

You are in **execution** when:

- The plan status is `active`
- You are executing a specific task checkbox (or a referenced task file)

Rules:

- Execute **exactly one task at a time**.
- **Do not change the plan** while executing a task.
- When the task completes:
  - Check the checkbox in the plan immediately.
  - Update the plan `Updated` timestamp.
  - Verify (tests or explicit reasoning).

## Switching modes safely

If you discover missing requirements during execution:

1. Stop execution.
2. Ask the user whether to return to planning (modify plan) or continue with the
   plan as-is.

Do not "silently" change plan scope during execution.

## Minimal conflict rule

- A plan may add constraints and specifics.
- A plan may not override CatHerder process rules.
- A task may not override its plan.