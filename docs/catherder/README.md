---
type: reference
description: "Canonical source documentation for developing and auditing the CatHerder methodology (not for direct use in enabled projects)"
---
# CatHerder Canonical Docs (Source)

This folder is the canonical, maintained source for the CatHerder methodology: process, rules, workflows, and file conventions.

## Intended Use

These documents are written for:

- Humans maintaining CatHerder (project managers, maintainers, auditors)
- Powerful LLMs/agents working on **CatHerder itself** (for example creating or updating `repo/skills/plan-task-standards/`, `repo/skills/skill-file-standards/`, and `repo/plans/` templates and readmes)

These documents are **not** meant to be auto-discovered by agents in CatHerder-enabled projects, and they are **not** the content that should be attached to day-to-day agent prompts in those projects.

Enabled projects should consume **derived, condensed artifacts** (instruction files, skills, templates) generated from these sources.

## Index

- Philosophy and intent: [philosophy.md](philosophy.md)
- Project structure and file placement: [project-structure.md](project-structure.md)
- Plans and tasks workflow: [plans-and-tasks.md](plans-and-tasks.md)
- Git workflow (optional module): [git-workflow.md](git-workflow.md)
- File formats (frontmatter, timestamps): [file-formats.md](file-formats.md)
- Prompt precedence & conflict resolution: [prompt-precedence-and-conflicts.md](prompt-precedence-and-conflicts.md)
- Planning vs execution: [planning-vs-execution.md](planning-vs-execution.md)
- Persistence & validation norms: [persistence-and-validation-norms.md](persistence-and-validation-norms.md)

## Derivation Map (Downstream Artifacts)

These are derived or regenerated from this folder’s content:

- `repo/skills/plan-task-standards/`
  - Primary sources: [plans-and-tasks.md](plans-and-tasks.md), [file-formats.md](file-formats.md)

- `repo/plans/TEMPLATE*.md`
  - Primary sources: [plans-and-tasks.md](plans-and-tasks.md)

- `repo/instructions/catherder.instructions.md`
  - Primary sources: [philosophy.md](philosophy.md), [project-structure.md](project-structure.md), [plans-and-tasks.md](plans-and-tasks.md), [prompt-precedence-and-conflicts.md](prompt-precedence-and-conflicts.md), [planning-vs-execution.md](planning-vs-execution.md), [persistence-and-validation-norms.md](persistence-and-validation-norms.md)
  - Should reflect the canonical model for repository-specific entry guidance, workflow authority, conditional reading, and scratchpad/roadmap usage

- `repo/instructions/catherder-git.instructions.md`
  - Primary sources: [git-workflow.md](git-workflow.md), [plans-and-tasks.md](plans-and-tasks.md)

- `repo/instructions/README.md`
  - Primary sources: [project-structure.md](project-structure.md), [git-workflow.md](git-workflow.md)
  - Should explain the intended role of published instruction artifacts and how enabled projects should create local `project.instructions.md`

- `repo/agents/`
  - Primary sources: [philosophy.md](philosophy.md), [project-structure.md](project-structure.md)
  - Should preserve `AGENTS.md` as a minimal bootstrap pattern rather than a second workflow document

`project.instructions.md` is repository-specific and is not currently a canonical generated artifact. Its recommended structure and role are defined in [project-structure.md](project-structure.md).

When these canonical docs change, update the derived artifacts and check for resulting drift.
