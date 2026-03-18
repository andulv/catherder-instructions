# Task 2 Sync-Surface Classification — `AGENTS.md`, `.instructions/`, `.agents/`

Date: 2026-03-11T01:10:00+00:00
Plan: `plan008`

## Classification Model

Use these classes before making sync recommendations:

- **canonical/shared** — usually good candidates for propagation when their role is clearly standardized
- **locally adaptable** — expected to vary by repository; compare and learn from them, but do not assume one side should overwrite the other
- **local-only / operational** — do not blindly sync; usually stateful, contextual, or repo-runtime-specific
- **unresolved / needs-human-decision** — comparison is allowed, but recommendation must stay cautious until canonical guidance exists

## Surface: root `AGENTS.md`

### Default classification
- **canonical/shared pattern**, but often **locally adaptable content**

### Why
- Plan 007 established that `AGENTS.md` should usually be a minimal bootstrap file pointing to `.instructions/project.instructions.md`.
- The exact wording may vary by repository, but the role pattern is canonical.

### Recommendation rule
- Compare for role conformance first.
- If one version is a cleaner minimal bootstrap and the other duplicates workflow rules, recommend syncing toward the cleaner bootstrap model.
- If both are bootstrap-compliant but include repo-specific references, prefer manual merge or selective adaptation.

## Surface: `.instructions/`

### `.instructions/project.instructions.md`
- **locally adaptable** with some reusable structure patterns
- repository-specific by nature, but compare for improvements to document maps, structure explanation, and reading guidance

### `.instructions/catherder.instructions.md`
- usually **canonical/shared** if copied from central guidance, but may include local drift
- compare for standard process rules and copy-safe improvements

### `.instructions/catherder-git.instructions.md`
- usually **canonical/shared** when present
- compare for process drift and improvements to git execution rules

### `.instructions/SCRATCHPAD.md`
- **local-only / operational**
- never recommend blind syncing
- at most, compare structure conventions or note useful headings/patterns for human adoption

### `.instructions/plans/**`
- usually **local-only / operational** for active plan work
- compare only when the user explicitly wants process comparisons, templates, or examples
- do not treat current project plans as canonical sync targets by default

### Other `.instructions/*.md`
- classify by role:
  - process template / reusable instruction → possibly canonical/shared
  - project strategy, roadmap, working notes, or execution state → locally adaptable or local-only

## Surface: `.agents/`

### `.agents/agents/<agent>/agent.md`
- typically **locally adaptable** with possible reusable improvements
- compare persona/instruction improvements carefully; sync only when changes are not project-specific

### `.agents/skills/<skill>/`
- often **canonical/shared candidate** if the skill is meant to be reusable
- but may also be local-only if tailored to a single project
- evaluate reusability and externalized assumptions before recommending upstream or cross-project sync

### `.agents/agents/agents.yaml`
- **unresolved / needs-human-decision**
- Plan 007 found it is a real operational mechanism but not canonically documented
- compare existence and shape if relevant, but do not recommend blind synchronization

### Other `.agents/` runtime/config files
- default to **local-only / operational** unless clearly documented as reusable templates

## Cross-Cutting Decision Rules

- A file being newer does not mean it should win.
- A file being in the central repo does not automatically make every line canonical.
- A project-local improvement may deserve upstream recommendation if it generalizes cleanly.
- Operational state, working memory, active plans, and runtime registries should never be treated as safe bulk-sync content.
- When classification is uncertain, use `needs canonical decision` instead of guessing.
