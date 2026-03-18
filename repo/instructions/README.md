# Instruction Templates (Catalog)

This folder contains copy-ready instruction templates for CatHerder-enabled projects.

Canonical source documentation lives under `docs/catherder/`.

## What to copy into an enabled project

In the target project, copy these into:

```
.instructions/
```

### Always include (core)

- `catherder.instructions.md`
  - Always-follow process rules
  - Git-agnostic (safe for gitless projects)

### Repository-specific entry guidance

- Create `project.instructions.md` in the target project's `.instructions/`
  - This is the repository-specific entry and navigation document
  - It should contain a document map explaining what each local instruction file is and when to read it
  - It should avoid blanket "read everything" startup lists
  - It should own repository navigation, while `catherder.instructions.md` stays focused on process rules

### Include only when the project uses git

- `catherder-git.instructions.md`
  - Mandatory when present and work involves repository changes or git operations
  - Branch-per-plan, source-branch cleanliness, direct-on-main constraints, commit, and merge approval rules

## Related catalog folders

- `repo/agents/` — agent definition file conventions and templates (Markdown + YAML frontmatter)
- `repo/plans/` — plan/task workflow docs and templates
- `repo/skills/` — reusable skill definitions

## Canonical references

- Process docs index: `docs/catherder/README.md`
- Project structure and entry guidance: `docs/catherder/project-structure.md`
- Plans + tasks: `docs/catherder/plans-and-tasks.md`
- Git workflow: `docs/catherder/git-workflow.md`
