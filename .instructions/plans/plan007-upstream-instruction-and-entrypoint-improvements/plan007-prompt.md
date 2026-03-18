We have improved `.instructions/` and `AGENTS.md` in this repository while operating it.

This repository is also the canonical source for CatHerder-enabled project scaffolding and conventions.
We should upstream the improvements that are generalizable so downstream projects get the better defaults.

Create a plan to review what changed in this repository-level operational instructions, decide what belongs in canonical CatHerder artifacts, and update the source-of-truth materials accordingly.

Important considerations:
- Keep one authoritative source per instruction topic.
- Optimize instructions for agents: low ambiguity, low context overhead, actionable read conditions.
- Prefer markdown links over bare filenames.
- Distinguish between required, operational, and conditional reading.
- `project-status-roadmap.md` should not always be mandatory.
- `SCRATCHPAD.md` should be read when resuming/continuing repository work and updated at session end, not necessarily read for every chat.
- Add ignore-by-default guidance for searches/scans (`.git/`, `.venv/`, generated/cache directories).
- Clarify the relationship between `AGENTS.md`, `project.instructions.md`, `catherder.instructions.md`, and `catherder-git.instructions.md`.
- Update repository structure guidance so examples/descriptions match actual intended CatHerder repository structure and clearly distinguish operational files, canonical publishable artifacts, and legacy/reference material.

The result should improve catherder-instructions-repo itself as the source of truth, and identify which files under `docs/catherder/`, `repo/instructions/`, `repo/agents/`, and related templates need changes.



-----

Notes from qewn3-coder

