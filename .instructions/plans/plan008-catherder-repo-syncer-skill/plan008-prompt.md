Create a new reusable skill named `catherder-repo-syncer`.

Purpose of the skill:
- Compare and optionally help sync CatHerder instruction assets between repositories.
- Supported comparison modes:
  1. `catherder-instructions-repo` ↔ one CatHerder-enabled project
  2. one CatHerder-enabled project ↔ another CatHerder-enabled project

Instruction assets in scope:
- `AGENTS.md` in repository root
- everything under `.instructions/`
- everything under `.agents/`

The skill should help with:
- comparing differences and making clear diff lists
- evaluating which side appears newer / stronger / more canonical
- suggesting what should sync from one repo to the other and what should sync in the reverse direction

Background / reason:
- When working in a CatHerder-enabled project we sometimes create or improve skills, agents, or instructions locally and want to sync improvements back to the central `catherder-instructions-repo`.
- The central `catherder-instructions-repo` is also updated over time, and we want to sync improvements out to CatHerder-enabled projects.

Create the skill in standards-compliant form under `repo/skills/` with concise runtime guidance, any needed self-contained references, and validation support. The skill should be practical for agents: clear scope boundaries, comparison procedure, evaluation criteria, output format, and safety rules for optional syncing recommendations.
