# Task 3 Decision Note — Upstream Guidance Model

Date: 2026-03-09T00:00:00+00:00
Plan: `plan007`

## Approved Upstream Model for Canonical Update

### 1. `AGENTS.md`
- Role: minimal bootstrap file.
- Purpose: point agents to the repository-specific entry document.
- Rule: do not duplicate repository workflow rules or a second authoritative reading-order list.

### 2. `project.instructions.md`
- Role: repository-specific entry guidance.
- Purpose: orient agents to the repository, its document map, structure, and local rules.
- Guidance model: use a concise document map instead of a blanket startup reading-order list.
- Document map should state for each referenced file:
  - what it is
  - when it must be read
- Reading categories should use the pattern:
  - required
  - operational
  - conditional

### 3. `catherder.instructions.md`
- Role: authoritative CatHerder workflow procedure inside an enabled project.
- Rule: do not define a competing repository read-order list.
- Rule: explicitly defer repository-specific entry guidance to `project.instructions.md`.
- Rule: state that these process rules apply to repository work.

### 4. `catherder-git.instructions.md`
- Role: optional git module.
- Rule: if present, it is mandatory for work involving repository changes or git operations.
- Guidance should be phrased as action rules, not as vague inclusion notes.

### 5. `SCRATCHPAD.md`
- Role: current working memory and handoff note.
- Guidance: read when resuming or continuing repository work.
- Guidance: update at session end.
- It should not be described as universally required for every interaction.

### 6. `project-status-roadmap.md`
- Role: strategic status and phase context.
- Guidance: read when planning, prioritizing, or evaluating project direction.
- It should not be described as universally mandatory startup reading.

### 7. Ignore-by-default guidance
- Include baseline guidance in repository entry/structure docs.
- Scope: applies to searching, scanning, and broad review work.
- Default examples:
  - `.git/`
  - `.venv/`
  - generated/cache/tool-managed directories
- Additional examples may be repository-specific.

### 8. Repository structure guidance
- Canonical docs should distinguish:
  - operational repository files
  - reusable/canonical artifacts
  - legacy/reference-only areas
- Enabled-project baseline should stay generic and not embed this repository’s special folders unless documenting CatHerder’s own source repository.

## Implementation Consequences

- Replace rigid reading-order guidance in canonical enabled-project docs with conditional document-map guidance.
- Update reusable instruction templates to align with the same model.
- Add explicit minimal-bootstrap guidance for `AGENTS.md` in the appropriate canonical/reusable location.
- Keep downstream templates concise and optimized for agent execution.
