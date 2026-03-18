# Task 2 Affected File Map — Canonical Sources and Derived Artifacts

Date: 2026-03-09T00:00:00+00:00
Plan: `plan007`

## Canonical Sources

### Entry guidance and enabled-project structure
- `docs/catherder/project-structure.md`
  - currently defines minimum structure and reading order for enabled projects
  - should own the canonical model for enabled-project entry guidance, document roles, and baseline structure

### Workflow authority and process rules
- `docs/catherder/plans-and-tasks.md`
  - source for plan/task lifecycle and execution contract
- `docs/catherder/planning-vs-execution.md`
  - source for separation of planning and execution
- `docs/catherder/prompt-precedence-and-conflicts.md`
  - source for precedence/conflict rules
- `docs/catherder/persistence-and-validation-norms.md`
  - source for durable-artifact and validation guidance
- `docs/catherder/philosophy.md`
  - source for intent and methodology framing

### Git rules
- `docs/catherder/git-workflow.md`
  - source for optional git module behavior

### Canonical index / derivation map
- `docs/catherder/README.md`
  - should reflect any new or clarified derivations and guidance boundaries

## Derived / Reusable Artifacts

### Instruction templates
- `repo/instructions/README.md`
  - catalog guidance on what enabled projects should copy
- `repo/instructions/catherder.instructions.md`
  - condensed workflow instructions for enabled projects
- `repo/instructions/catherder-git.instructions.md`
  - condensed git module for enabled projects

### Agent definitions / bootstrap guidance
- `repo/agents/README.md`
  - likely place to document expectations for minimal `AGENTS.md` behavior if standardized
- `repo/agents/agent-TEMPLATE.md`
  - candidate location if bootstrap guidance becomes part of agent scaffolding

### Plans/templates impact (possible, lighter)
- `repo/plans/README.md`
  - may need wording updates if instruction-entry guidance is referenced there

## Local Operational Files Used as Proven Reference

These are not canonical upstream targets, but they are the concrete examples that motivated this plan:

- `AGENTS.md`
- `.instructions/project.instructions.md`
- `.instructions/catherder.instructions.md`
- `.instructions/catherder-git.instructions.md`
- `.instructions/SCRATCHPAD.md`

## Likely Change Scope Summary

High-likelihood direct edits:
- `docs/catherder/project-structure.md`
- `docs/catherder/git-workflow.md`
- `docs/catherder/README.md`
- `repo/instructions/README.md`
- `repo/instructions/catherder.instructions.md`
- `repo/instructions/catherder-git.instructions.md`

Possible additional edits depending on chosen upstream model:
- `repo/agents/README.md`
- `repo/agents/agent-TEMPLATE.md`
- `docs/catherder/philosophy.md`
