---
type: plan
description: "Plan 008 — Create the catherder-repo-syncer skill for comparing and recommending sync of CatHerder instruction assets between repositories"
---
# Plan 008: Create catherder-repo-syncer Skill

**Status:** `draft`

**Created:** 2026-03-11T00:00:00+00:00

**Updated:** 2026-03-11T00:20:00+00:00

## Goal

Create a reusable `catherder-repo-syncer` skill that helps agents compare CatHerder instruction assets across repositories, classify differences safely, and recommend intentional sync actions without assuming every difference should be copied.

## Context / Why

CatHerder instruction assets evolve in both directions:

- downstream projects often improve local instructions, skills, or agents that should be considered for upstreaming into `catherder-instructions-repo`
- the central `catherder-instructions-repo` also evolves and those improvements often need to be evaluated for propagation into downstream CatHerder-enabled projects
- some files are canonical defaults, some are expected local adaptations, and some are operational/local-only and should not be blindly synchronized

This comparison work is currently ad hoc. A dedicated skill should make it repeatable, scoped, and agent-safe by defining exactly what files are in scope, how to compare them, how to classify file roles, how to judge canonical vs local improvements, and how to present sync recommendations without making unsafe assumptions.

Plan 007 established useful upstreaming patterns that should shape this work:

- inventory first
- distinguish canonical defaults from optional or repository-local artifacts
- trace source-of-truth versus derived artifacts
- record unresolved policy gaps instead of guessing
- separate comparison/reporting from modification

## What We Want To Achieve (Outcomes)

A standards-compliant skill under `repo/skills/catherder-repo-syncer/` such that:

- the skill clearly states trigger conditions, supported comparison modes, and non-goals
- scope is explicit: root `AGENTS.md`, `.instructions/`, and `.agents/`
- the skill begins with inventory and file-role classification before any sync recommendation
- the skill defines a practical procedure for matching and comparing files between two repositories
- the skill defines evaluation criteria for deciding whether differences are likely canonical improvements, local customizations, bidirectional candidates, or unsafe/ambiguous cases
- the skill defines a recommended output structure for diff lists, directional sync suggestions, and unresolved decision flags
- the skill includes explicit safety guidance that recommendations should precede edits unless the user explicitly requests synchronization
- the skill includes caution guidance for known ambiguous areas identified in Plan 007
- any supporting references remain self-contained within the skill folder
- the skill passes applicable validation

## Summary Of Work Needed

**1. Inspect existing skill patterns and relevant standards**

Review current repository skill conventions and determine the best concise structure for a comparison/sync recommendation skill.

**2. Define sync-surface classification model**

Define how the skill should classify in-scope files and folders, for example:
- canonical/shared defaults
- locally adaptable files
- local-only / operational files
- unresolved / needs-human-decision files

This classification must reflect lessons from Plan 007 and avoid overconfident copying.

**3. Define the skill contract and decision model**

Define:
- triggers and non-triggers
- repository/file scope
- supported comparison scenarios
- comparison workflow
- evaluation heuristics for newer / better / canonical / project-specific
- recommendation categories such as:
  - sync A → B
  - sync B → A
  - merge manually
  - do not sync
  - needs canonical decision
- output format for findings and recommendations
- safety/stop rules for optional syncing

**4. Incorporate known ambiguity handling**

Ensure the skill explicitly handles unresolved or risky cases surfaced by Plan 007, including drifted or not-yet-canonicalized artifacts and undocumented operational mechanisms. The skill should instruct agents to flag these for human review rather than pretending certainty.

**5. Author the skill files**

Create `SKILL.md` and any self-contained references/scripts needed under `repo/skills/catherder-repo-syncer/`.

**6. Validate the skill**

Run skill validation and fix any issues.

**7. Record completion and follow-up notes**

Document what was created, validation results, known limitations, and any future enhancements.

## Key Principles / Constraints

- Keep the skill self-contained; do not rely on runtime access to repo-external methodology docs.
- Optimize for agent execution: low ambiguity, explicit scope, deterministic output format.
- Recommendations must distinguish compare/report mode from actual sync/edit mode.
- Do not treat every file difference as a sync candidate.
- Prefer canonical source-of-truth only when it is actually established.
- Treat project-local customizations carefully; do not assume central repo should always overwrite downstream repos.
- Flag ambiguous ownership or undocumented file roles for human review.
- Prefer recommendations that preserve intent and explain reasoning.

## Known Inputs From Plan 007

The resulting skill should account for the following already-observed realities:

- `AGENTS.md` has a minimal bootstrap role and should not be treated as a duplicate home for all workflow rules.
- `project.instructions.md` is repository-specific entry guidance and may legitimately differ across enabled repos.
- `SCRATCHPAD.md` is operational local memory and should be treated as local/operational rather than canonical shared content.
- `.agents/agents/agents.yaml` exists as an operational agent-registry mechanism, but its canonical sync status is unresolved.
- `repo/agents/agent-TEMPLATE.md` and `repo/agents/README.md` were found drifted in Plan 007 verification, which means the syncer skill must support “needs canonical decision” instead of assuming one side is authoritative.

## Open Questions

- Does the first version need helper scripts, or is a well-structured procedural skill sufficient?
- Should the skill include a standard table format for file-level sync decisions?
- Should the first version compare only at file level, or also suggest section-level/manual merge handling guidance?
- How opinionated should the heuristics be for determining canonical vs local ownership of changes?

## Notes

- Source prompt: `plan008-prompt.md`
- Skill target location: `repo/skills/catherder-repo-syncer/`
- This plan intentionally inherits Plan 007 lessons about source-of-truth mapping, ambiguity handling, and cautious sync classification.