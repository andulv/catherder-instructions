---
type: meta
description: "Project status, roadmap, and current phase for catherder-instructions-repo"
---
# Project Status & Roadmap — catherder-instructions-repo

Last updated: 2026-03-05T12:00:00+01:00

## Phase Overview

| Area | Phase | Notes |
|---|---|---|
| Canonical docs (`docs/catherder/`) | **Beta** | Stable; changes need careful review for downstream drift |
| Instruction templates (`repo/instructions/`) | **Beta** | Stable; consumed by enabled projects |
| Skills (`repo/skills/`, `.agents/skills/`) | **Prototype** | Adding new skills, format still evolving |
| Plan templates (`repo/plans/`) | **Beta** | Templates settled |
| Legacy cleanup | **Prototype** | `legacy-todelete/` pending human review and removal |

## Current Focus

- Stabilize `.instructions/` layout to match canonical standards
- Clean up legacy files (`legacy-todelete/`)
- Develop and validate new skills

## Needs Work

- `repo/agents/` — placeholder, no agent definitions yet
- Legacy files under `legacy-todelete/roles/` — awaiting deletion after human review
- Skill validation tooling — `skills-ref` script coverage

## Open Questions

- Should `repo/agents/` be populated or removed?
- Final cleanup scope for `legacy-todelete/` — which items (if any) to preserve?
