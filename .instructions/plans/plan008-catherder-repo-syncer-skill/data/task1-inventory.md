# Task 1 Inventory — catherder-repo-syncer Inputs and Reusable Patterns

Date: 2026-03-11T01:00:00+00:00
Plan: `plan008`

## Canonical / Reusable Inputs

### Plan 007 findings worth reusing directly
- `plan007` Task 1 inventory establishes the core distinction between canonical defaults, optional guidance, and repository-local-only material.
- `plan007` Task 2 affected-file map clarifies source-of-truth vs derived artifact thinking.
- `plan007` Task 3 decision note establishes the role model for:
  - minimal root `AGENTS.md`
  - `project.instructions.md` as repository-specific entry guidance
  - `SCRATCHPAD.md` as resume/handoff memory rather than universal startup input
- `plan007` Task 6 verification note surfaces unresolved sync-risk areas:
  - `repo/agents/agent-TEMPLATE.md` drift
  - `repo/agents/README.md` drift
  - `.agents/agents/agents.yaml` as an operational mechanism with unresolved canonical status

### Repository instructions and process rules
- `.instructions/project.instructions.md` defines this repo as source of truth for reusable guidance and distinguishes local operational files from published artifacts.
- `.instructions/catherder.instructions.md` requires task-by-task execution, immediate completion marking, and explicit stop rules.
- `.instructions/catherder-git.instructions.md` requires dedicated branch execution from clean `main` and one commit per completed task when practical.

### Skill authoring patterns to reuse
- `repo/skills/skill-file-standards/` provides the current standard for:
  - self-contained skills
  - frontmatter description wording
  - short `SKILL.md` plus direct references
  - validation helpers and reference-frontmatter convention
- `repo/skills/plan-task-standards/` shows the desired concise skill structure and checklist-driven authoring style.

## Directly Reusable Design Patterns for This Skill

- Inventory first before comparison judgments.
- Classify files by role before suggesting sync direction.
- Treat canonical-vs-local status as a first-class decision, not an afterthought.
- Separate compare/report mode from edit/sync mode.
- Record ambiguity explicitly instead of guessing.
- Keep runtime skill instructions self-contained rather than depending on repository docs.

## Repo-Local Context That Should Not Become Runtime Skill Dependency

These can inform authoring but should not be referenced as required runtime dependencies by the skill:
- this repo’s own `.instructions/` files
- this repo’s plan folder contents
- this repo’s branch naming and session notes
- plan-specific timestamps and execution history

## Notes

- The new skill should ship its own condensed comparison model rather than instructing agents to go read Plan 007.
- The unresolved status of `.agents/agents/agents.yaml` must be carried into the skill as a caution rule.
- The skill should optimize for repeatable analysis and recommendation output, not auto-apply syncs by default.
