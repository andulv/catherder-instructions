---
type: project
description: "Project overview, rules, process and structure for catherder-instructions-repo"
alwaysApply: true
---
# Project Overview

This repository is the source of truth for CatHerder conventions, templates, and reusable guidance.

## Instruction Document Map
Use these documents intentionally. Do not read everything by default.

### Required
1. [`project.instructions.md`](project.instructions.md)
   - Repository-specific overview, structure, and document map.
   - Read first for work in this repository.

### Operational
2. [`catherder.instructions.md`](catherder.instructions.md)
   - Core CatHerder workflow, execution loop, stop rules, and task discipline.
   - Read when doing repository work or when you need process guidance.

3. [`catherder-git.instructions.md`](catherder-git.instructions.md)
   - Git commit, branch, staging, and commit guidance for repository work.
   - Read before making repository changes, executing plans/tasks, or using git.

4. [`SCRATCHPAD.md`](SCRATCHPAD.md)
   - Current working memory, latest session state, and handoff notes.
   - Read when resuming or continuing repository work.
   - Update at the end of each repository work session.

### Conditional
5. [`project-status-roadmap.md`](project-status-roadmap.md)
   - Strategic status, roadmap, and project phase context.
   - Read when planning, prioritizing, or evaluating project direction.

## Repository Role

This repository serves two purposes:

1. **Operate** — Use `.instructions/` for planning and executing work in this repo.
2. **Publish** — Use `repo/` for catalog artifacts consumed by other CatHerder-enabled projects.

## What CatHerder is
CatHerder is a lightweight operating model for human + agent software teams: predictable file layouts, explicit planning/task lifecycle, reusable skills, and workflow standards practical for agentic tooling.

## Repository Structure
```
.instructions/              — operational instructions and working state for this repository
  project.instructions.md   — repository-specific entry instructions
  catherder.instructions.md — CatHerder workflow for repository work
  catherder-git.instructions.md — git workflow rules for this repository
  SCRATCHPAD.md             — current working memory and handoff notes
  plans/                    — local plans for repository work
.agents/                    — local agent runtime assets used by this repository
  agents/                   — local agent definitions
  skills/                   — locally available skills
repo/                       — reusable/published CatHerder artifacts for other projects
  instructions/             — copy-ready instruction templates for enabled projects
  skills/                   — canonical reusable skills
  plans/                    — plan templates and examples
  schemas/                  — shared prompt/data schemas
  agents/                   — reusable agent definitions and templates
  catherder-dev.sln         — solution for repository development assets
docs/                       — longer-form canonical documentation
  catherder/                — CatHerder methodology source docs (authoritative)
legacy-kept-for-reference/  — legacy/reference material; ignore by default unless task-relevant
```

## Important Distinction
- Editing **`repo/`** or **`docs/catherder/`** changes CatHerder standards for all projects.
- Editing **`.instructions/`** affects operation in *this* repository only.

When changing canonical docs in [`docs/catherder/`](../docs/catherder/), check [`docs/catherder/README.md`](../docs/catherder/README.md) for the derivation map. Downstream artifacts under [`repo/instructions/`](../repo/instructions/), [`repo/skills/`](../repo/skills/), and related paths may need updates to stay in sync.

## Ignore by Default
When searching, scanning, or broadly reviewing the repository, ignore these paths unless the task explicitly requires them:

- [`.git/`](../.git/)
- [`.venv/`](../.venv/)
- `node_modules/`
- other generated, cache, or tool-managed directories

This reduces noise and helps avoid accidental edits to generated or non-project working files.
