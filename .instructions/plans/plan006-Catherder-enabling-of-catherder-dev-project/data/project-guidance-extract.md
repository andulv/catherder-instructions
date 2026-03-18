# Task 2 Output — Project Guidance Extract for `project.instructions.md`

Source files reviewed:
- legacy `project.INSTRUCTIONS.md`
- legacy `team.md`
- legacy `project-status-roadmap.md`

## Project-specific guidance to carry forward

- Project identity:
  - `catherder` is a custom AI agent orchestrating work across multiple LLM vendors.
  - Purpose: model routing by task complexity and structured workflow execution.
- Architecture direction:
  - .NET (net10/C#) + Generic Host + hosted service.
  - MAF-based orchestration and tool-calling integration.
  - OpenAI-compatible providers plus extensibility to other vendors.
- Development approach:
  - Plans define intent; tasks execute intent.
  - Prefer understanding/research before implementation.
- Testing strategy:
  - Offline unit/smoke tests by default.
  - Optional gated integration tests for live provider calls.
- Domain concept worth retaining:
  - Heavy/Mid/Light model tier framing as a practical execution heuristic.

## Guidance to avoid or reframe

- Avoid legacy cross-repo hard links to old `roles/skills/workflow` paths.
- Avoid carrying over old team schema details as mandatory process.
- Reframe old "Refinement" status to the decided current phase: **Prototype**.

## Proposed placement

- New `.instructions/project.instructions.md`:
  - identity, architecture snapshot, testing strategy, project layout, project-specific conventions.
- New `.instructions/project-status-roadmap.md`:
  - set current phase to **Prototype**, include focus + open questions.
- New `.instructions/SCRATCHPAD.md`:
  - short current context and immediate pending items only.
