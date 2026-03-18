---
type: reference
description: "Plan and task lifecycle rules: folder structure, required sections, execution contract, and validation constraints"
---
# Plans and Tasks Workflow

This document defines the CatHerder plan/task model and the rules that downstream
artifacts (templates, validator, and skills) must implement.

## Plan Folder Structure

```
.instructions/plans/
  planNNN-short-description/
    planNNN-prompt.md
    planNNN-draft.md
    planNNN.md
    data/
    tasks/
```

Rules:

- Folder name format: `planNNN-short-description`.
- `NNN` is zero-padded three digits and monotonically increasing (project-scoped).
- File names use matching `planNNN` prefix.

## Lifecycle Stages

- Prompt (`planNNN-prompt.md`): free-form input; frontmatter optional.
- Draft (`planNNN-draft.md`): structured intent; not executable.
- Active (`planNNN.md`): canonical executable plan.

Simple plans may skip the prompt stage.

## Draft Plan Requirements

Frontmatter (required):
- `type: plan`
- `description: "Plan NNN — …"`

Status must be: `draft`

Required sections:
- `## Goal`
- `## Context / Why`
- `## What We Want To Achieve (Outcomes)`
- `## Summary Of Work Needed`
- `## Key Principles / Constraints`
- `## Open Questions`

Constraint:
- Draft plans must not contain an executable `## Tasks` checklist with `- [ ]` / `- [x]`.

## Active Plan Requirements

Frontmatter (required):
- `type: plan`
- `description: "Plan NNN — …"`

Status must be one of: `active`, `completed`, `abandoned`

Required sections:
- `## Goal`
- `## Context / Why`
- `## Tasks`
- `## Acceptance Criteria`
- `## Notes`

Rules:
- Tasks are checkboxes (`- [ ]` / `- [x]`).
- Completed plans: every task and acceptance-criteria checkbox must be checked.
- Abandoned plans: Notes must include a rationale.

## Task Execution Contract

Execution rules:

1. Execute exactly one task at a time.
2. Do not change the plan while executing a task.
3. When a task finishes, immediately:
   - Check its checkbox in the plan.
   - Update the plan `**Updated:**` timestamp.
4. Verify the result (tests or explicit reasoning).

## Separate Task Files

Use separate task files when an inline task is too large/complex.

### Naming

Task files are named:

- `taskNNN-NN-short-name.md`

Where:
- `NNN` matches the parent plan number
- `NN` is a zero-padded two-digit task number (01, 02, …)

Example: `task004-01-rewrite-process-doc.md`

Rationale:
- Letters are reserved for **plan variants** (e.g. `plan004b` as an alternative
  version of `plan004`).

### Frontmatter (required)

- `type: task`
- `description: "Task NNN-NN — …"`

### Required sections

Objective, Scope, Steps, Verification, Notes.

### Referencing from the plan

Active plans must reference the task file from the checklist item.

## Plan Data Folder

`data/` holds supporting material (research notes, source summaries, snapshots).
No strict format is required.
