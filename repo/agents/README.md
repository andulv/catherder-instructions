# Agents (central catalog)

This folder contains **reusable agent definition files** intended to be consumed by CatHerder-enabled projects.

## Layout

Each agent is a folder containing `agent.md` as the main definition file:

```
repo/agents/
  agent-TEMPLATE.md               # copy to create a new agent folder
  catherder-dev-assistant/
    agent.md                      # agent definition
  catherder-project-controller/
    agent.md                      # agent definition
```

- The **folder name** is the agent identifier (same convention as skills).
- `agent.md` is always the main file (like `SKILL.md` for skills).
- Additional files (references, scripts, context) can be added to the folder as needed in the future.

## Format

Each `agent.md` is Markdown with YAML frontmatter:

```yaml
---
name:        # matches parent folder name
role:        # e.g. dev-assistant | project-controller
version:     # semver
description: # one-line summary
---
```

The Markdown body is the instruction content.

## Composition

At runtime, compose the final instruction text by:

1. Loading the agent's `agent.md`
2. Stripping frontmatter
3. Optionally appending `AGENTS.md` as a minimal bootstrap entry point

`AGENTS.md` should point to the repository-specific entry guidance, stay short and high-signal, and should not duplicate repository workflow rules.

If you need runtime substitution, use a simple token scheme: `{{agentInstanceName}}`, `{{agentId}}`.

## Authoring guidance

- Do not duplicate canonical CatHerder methodology if it already exists in `repo/instructions/` or project `.instructions/` entry points.
- Prefer referencing skills (for example `plan-task-standards`) instead of restating their rulebooks.
- Include shared/base concerns directly in each agent's file; keep it concise.

## Template

Copy `agent-TEMPLATE.md` into a new `<agent-name>/agent.md` to create a new agent.
