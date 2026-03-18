# Task 1 Output — Legacy Inventory (Keep / Ignore)

Source folder:
`/home/anders/source/agent/catherder-dev/.instructions-legacy-outdated-but-may-contain-useful-info-instructions-experiments-to-build-on`

## Keep (extract into new `.instructions/`)

- `project.INSTRUCTIONS.md`
  - Keep: project identity, architecture direction (.NET + MAF), testing strategy, model-tier concept.
  - Ignore: references to old external paths/workflow links.
- `project-status-roadmap.md`
  - Keep: high-level phase model and open questions pattern.
  - Override: project phase is now **Prototype** per plan decisions.
- `SCRATCHPAD.md`
  - Keep: recent context only if still valid.
  - Ignore: old task-level execution log details.
- `team.md`
  - Keep: useful team-role ideas as optional reference for project-specific notes.
  - Ignore: hard references to legacy role/skill paths.

## Keep as legacy reference only (do NOT migrate into active `.instructions/`)

- `skills/*` (all experimental instruction-audit/controller skills)
- `agents/*` (legacy controller/planning agent specs)
- `plans/*` and `plans/tasks/*` (old plans/tasks can die per decision)

## Ignore / superseded

- `README.md` in legacy folder (old reading order and layout conventions)
- Legacy plan templates (`plans/TEMPLATE.md`, `plans/tasks/TEMPLATE.md`)

## Decision Summary

- New active setup will be minimal and standards-compliant.
- Legacy folder remains reference/prototype material only.
- No direct migration of legacy skills/agents/plans into active `.instructions/`.
