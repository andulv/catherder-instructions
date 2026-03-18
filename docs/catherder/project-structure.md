---
type: reference
description: "CatHerder-enabled project structure, file placement, and scope boundaries"
---
# Project Structure and File Placement

## CatHerder-Enabled Project

A project is CatHerder-enabled when it contains a `.instructions/` directory at its root.

### Minimum structure

```
.instructions/
  project.instructions.md
  SCRATCHPAD.md
  catherder.instructions.md
  project-status-roadmap.md
  plans/
.agents/
AGENTS.md
```

`catherder-git.instructions.md` is optional. Include it only when the project uses git and wants CatHerder git workflow rules.

### Purpose of key locations

- `AGENTS.md`
  - Minimal bootstrap entry point for agents
  - Points to the repository-specific entry guidance
  - May remind agents to update `SCRATCHPAD.md` at session end
  - Should not duplicate repository workflow rules
- `.instructions/`
  - Operational contract for how work is planned and executed
  - Contains repository-specific entry guidance, plans, and project-level instruction files
- `.agents/`
  - Location for local agent definitions and/or skills
  - Keep agent runtime assets out of `.instructions/`

## Repository Entry Guidance (Enabled Projects)

Use a document map, not a blanket "read everything" startup list.

Recommended model:

- `project.instructions.md`
  - Repository-specific entry and navigation guidance
  - Read first for repository work
  - Owns the document map and conditional-reading guidance
- `catherder.instructions.md`
  - Authoritative CatHerder workflow procedure inside the repository
  - Read when doing repository work
  - Should stay focused on process rules, not repository navigation
- `catherder-git.instructions.md`
  - Optional git module
  - Read when present and work involves repository changes or git operations
- `SCRATCHPAD.md`
  - Current working memory / handoff note
  - Read when resuming or continuing repository work
  - Update at session end
- `project-status-roadmap.md`
  - Strategic status and phase context
  - Read when planning, prioritizing, or evaluating project direction

Use markdown links for referenced instruction files where practical.

## Bootstrap Guidance for `AGENTS.md`

Prefer a minimal bootstrap model:

- state that project instructions live under `.instructions/`
- point to `project.instructions.md` as the startup file
- keep the file short and high-signal

Do not turn `AGENTS.md` into a second workflow document.

## Ignore by Default

When searching, scanning, or broadly reviewing a repository, ignore noise-heavy and tool-managed paths unless the task explicitly requires them.

Baseline examples:

- `.git/`
- `.venv/`
- generated/cache/tool-managed directories

## Scope Boundary

Work is scoped to the active project root:

- Treat files outside the project root as read-only unless explicitly requested.
- If multiple projects are open, confirm the active project root first.

## Project Phases

Projects operate in a phase. The phase controls the expected rigour and compatibility constraints.

| Phase | Mindset | Key rules |
|---|---|---|
| Research | Experimental | Speed of learning over durability; DB drop/recreate OK; no migrations required. |
| Prototype | Build-first | Breaking changes OK; tests/compilation not required for every change. |
| Beta | Careful | Run tests; backward compatibility matters; quality gates apply. |
| Production | Stable | Full rigour; migrations required; all quality gates enforced. |

## `project-status-roadmap.md`

Each enabled project maintains:

```
.instructions/project-status-roadmap.md
```

This file is deliberately flexible (one-off scripts vs multi-year programs differ wildly). Typical contents include:

- Component/area → phase table
- Current focus and blockers
- Open questions affecting scope/architecture
- A "needs work" backlog of areas requiring attention
