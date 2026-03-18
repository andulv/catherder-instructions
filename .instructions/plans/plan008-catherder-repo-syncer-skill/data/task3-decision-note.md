# Task 3 Decision Note — Skill Contract and Recommendation Model

Date: 2026-03-11T01:20:00+00:00
Plan: `plan008`

## Supported Scenarios

The skill must support both of these primary comparison modes:

1. `catherder-instructions-repo` ↔ one CatHerder-enabled project
2. one CatHerder-enabled project ↔ another CatHerder-enabled project

The skill should refer to them neutrally as **repo A** and **repo B** and avoid assuming one side always wins.

## Trigger Conditions

Use this skill when the user wants to:
- compare CatHerder instruction assets between repositories
- identify differences in `AGENTS.md`, `.instructions/`, or `.agents/`
- evaluate which side has the newer, cleaner, or more reusable version
- generate directional sync recommendations
- prepare a manual sync plan or proposed patch set

## Non-Trigger / Out-of-Scope Cases

Do not treat this skill as the default for:
- syncing ordinary source code outside the CatHerder instruction surfaces
- merging active work branches generally
- copying operational state without analysis
- broad repository mirroring

## Required Comparison Workflow

1. Confirm repo pair and comparison scope.
2. Inventory in-scope files on both sides.
3. Classify each file/surface before recommending sync.
4. Compare content and role, not just timestamps.
5. Produce recommendation categories with rationale.
6. Do not edit either repo unless the user explicitly asks for sync/apply work.

## Heuristics for Judging Differences

### `newer`
A version may be considered newer if it has:
- a more recent explicit timestamp or commit history
- content reflecting later standards decisions
- references to capabilities or structures known to be introduced later

But newer alone is insufficient for sync direction.

### `better`
A version may be considered better if it is:
- more aligned with current CatHerder standards
- clearer, safer, and less ambiguous for agents
- more reusable across projects
- less contaminated by project-local assumptions
- better structured for its intended file role

### `canonical`
A version is more likely canonical when it:
- comes from a recognized source-of-truth artifact
- reflects established shared conventions rather than local operating state
- generalizes cleanly across enabled projects

### `project-specific`
A version is more likely project-specific when it:
- names local folders, teams, workflows, or runtime details
- encodes active execution state or handoff memory
- depends on local environment assumptions

## Recommendation Categories

Use exactly one primary recommendation per compared item:

- **sync A → B**
- **sync B → A**
- **merge manually**
- **do not sync**
- **needs canonical decision**

## Mandatory Safety Rules

- Default mode is compare/report only.
- Never blindly sync `SCRATCHPAD.md`.
- Never blindly sync active `.instructions/plans/**` contents.
- Treat `.agents/agents/agents.yaml` as unresolved unless the user explicitly wants to compare it and accepts the ambiguity.
- Ask for explicit permission before creating or editing files in either target repository.
- If recommendation confidence is low, prefer `merge manually` or `needs canonical decision`.

## Skill Behavior Style

The skill should bias toward:
- concise inventories
- explicit rationale
- directional recommendations only when justified
- surfacing ambiguity instead of inventing certainty
