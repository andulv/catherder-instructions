# Task 6 Verification Note

## Scope checked

- Canonical docs under `docs/catherder/`
- Reusable artifacts under `repo/instructions/` and `repo/agents/`
- Local operational agent files under `.agents/agents/`
- Local agent registry at `.agents/agents/agents.yaml`

## Findings

### 1. `repo/agents/agent-TEMPLATE.md` is outdated

The template does not match the current agent file format used by:

- `repo/agents/catherder-project-controller/agent.md`
- `repo/agents/catherder-dev-assistant/agent.md`
- `.agents/agents/catherder-project-controller/agent.md`
- `.agents/agents/catherder-dev-assistant/agent.md`

Observed drift:

- template uses `role`, but actual files do not
- template does not include `models`
- template does not include `alignments` / personality-style configuration
- template implies a sectioned markdown body structure that is not how current agent definitions are authored
- template does not reflect runtime tokens actually used in current files (`{{agentInstanceName}}`, `{{agentId}}`)

### 2. `repo/agents/README.md` is outdated

The README still describes an older frontmatter model:

- says `role` exists in frontmatter
- says runtime composition may append `AGENTS.md`
- only mentions simple token substitution

This no longer matches actual usage well enough.

### 3. `agents.yaml` exists as a real operational mechanism

`.agents/agents/agents.yaml` is now used to expose configured agent instances.
It maps:

- instance `name`
- canonical `agent`
- selected `model`
- optional `personality`

This mechanism is not documented in canonical docs or reusable artifacts.

### 4. Canonical docs currently miss the registry concept

No canonical docs mention an agent registry/config list such as `agents.yaml`.
If this is intended to be a CatHerder standard, upstream materials should document it.
If it is implementation-specific, it should at least be labeled as such.

## Conclusion

Tasks 4-5 were directionally correct, but verification found one follow-up gap:
agent-definition and agent-registry guidance is not yet fully synchronized.

## Recommended follow-up

- Update `repo/agents/agent-TEMPLATE.md` to match current agent file conventions
- Update `repo/agents/README.md` to describe current frontmatter and runtime expectations
- Decide whether `agents.yaml` is:
  - canonical CatHerder standard
  - optional supported convention
  - local implementation detail
- If canonical or supported, document it in:
  - `docs/catherder/project-structure.md`
  - `docs/catherder/README.md`
  - `repo/agents/README.md`
  - and add an example template under `repo/agents/`
