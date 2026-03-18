# CatHerder Research Findings

## Agent System Prompt Structure

### Agent Definition Files
Located under `repo/agents/`:
- **`catherder-dev-assistant/agent.md`** — Developer agent (.NET focus)
- **`catherder-project-controller/agent.md`** — Project/process manager

Each agent file has YAML frontmatter with:
- `name`: matches folder
- `version`: semver
- `description`: one-line summary
- `models`: list of compatible models
- `personalities`: optional variants (chaotic/lawful)

The Markdown body contains instructions using token substitution: `{{agentInstanceName}}`, `{{agentId}}`.

### Composition Pattern
Per `repo/agents/README.md`:
1. Load agent's `agent.md`
2. Strip frontmatter
3. Optionally append `AGENTS.md` as minimal bootstrap entry point
4. `AGENTS.md` should be short, avoid duplicating shared process rules
5. Prefer referencing skills rather than restating rulebooks

## Skill Loading Mechanism

### Auto-Discovery via FileAgentSkillsProvider
**C# Implementation** (`SystemCatalogService.cs`):
- Scans `.agents/skills/` for `SKILL.md` files recursively
- Returns `SystemSkillInfo` with name and relative path
- `ResolveSkillContextProviders()` matches patterns against known skills
- Patterns support glob-like selectors: `gws/*`, exact names

### Skill Pattern Matching
- Exact name matching: `skill-name`
- Folder-style selectors: `gws/*` matches `gws-docs`, `gws-sheets`, etc.
- Match against folder structure under `.agents/skills/`

### Runtime Assembly
This is NOT automatic injection into prompts. Instead:
- Agents reference skills in their instructions/personality
- Skills are discovered and available via tools/context
- Agent says "check for relevant skill" → skill content becomes available
- Skills may be explicitly loaded via `FileAgentSkillsProvider` when agent needs them

## Skill Structure (All gws skills follow same pattern)

### YAML Frontmatter (required)
```yaml
name: gws-docs (lowercase, matches folder name)
version: 1.0.0
description: "[WHAT] [WHEN] Read and write Google Docs."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws docs --help"
```

### Recommended Content Structure
- Header with PREREQUISITE reference to shared skills
- Progressive disclosure: index → procedures → references
- `references/` + `scripts/` folders (optional)

Examples:
- `gws-docs`: "Read and write Google Docs"
- `gws-sheets`: "Google Sheets: Read and write spreadsheets"
- `gws-slides`: "Google Slides: Read and write presentations"
- `gws-tasks`: "Google Tasks: Manage task lists and tasks"
- `gws-drive`: "Google Drive: Manage files, folders, and shared drives"

All have same pattern: ` > **PREREQUISITE:** Read `../gws-shared/SKILL.md`...`

## API Efficiency & Token Optimization

### From Anthropic Best Practices (in references)
**Concision & Context Economics:**
- Treat context window as shared resource
- Default: model already knows general concepts
- Only include non-obvious or easy-to-miss information
- Remove duplicate information that already exists in broader system context

**Progressive Disclosure:**
- SKILL.md as index/TOC pointing to deeper material
- Keep SKILL.md under ~500 lines (rule of thumb)
- Move long/volatile material into `references/`
- Avoid deep reference chains (prefer one-hop from SKILL.md)
- Long references (>100 lines) should include table of contents

**Minimal Field Principle:**
- Frontmatter `description`: routing metadata only (WHAT + WHEN + keywords, third person)
- No first-person voice in metadata
- Provide defaults + escape hatches, not option menus

### From Project Code
**gws-shared/SKILL.md** includes security rules:
- Never output API keys/tokens directly
- Always confirm before write/delete commands
- Prefer `--dry-run` for destructive operations
- Use `--sanitize` for PII screening

## Validation & Standards

### Skills Validation
1. Upstream: `skills-ref validate path/to/skill`
2. CatHerder references: `bash scripts/validate-references.sh path/to/skill`

### Reference Files Convention (CatHerder)
- MUST start with YAML frontmatter
- Required: `type: reference`, `description`, `snapshot_date`, `sources`
- Enables re-verification against upstream sources

### Script Header Convention (CatHerder)
Every script must start with:
```
# SCRIPT_ID:   <filename>
# PURPOSE:     <one-line description>
# USAGE:       <executable + args>
# ARGS:        <name (required|optional) - description>
# OUTPUT:      <stdout description>
# EXIT:        <code=meaning>
# DEPS:        <dependencies>
```

## Project Instructions Hierarchy

**Prompt Precedence** (per `prompt-precedence-and-conflicts.md`):
1. System instructions
2. Developer instructions (agent identity)
3. User instructions
4. Project process rules (`.instructions/*.instructions.md`)
5. Active plan
6. Task files
7. Repo docs/code comments
8. Host-injected metadata

## Key Files Reference

- **Agent definitions**: `/repo/agents/catherder-dev-assistant/agent.md`, `/repo/agents/catherder-project-controller/agent.md`
- **Agent composition guide**: `/repo/agents/README.md`
- **Process rules**: `/repo/instructions/catherder.instructions.md`, `catherder-git.instructions.md`
- **Skill standards**: `/.agents/skills/catherder-skills/skill-file-standards/SKILL.md`
- **Best practices**: `/.agents/skills/catherder-skills/skill-file-standards/references/anthropic-best-practices-2026-03.md`
- **Skill loading code**: `/src/CatHerder.Core/Services/SystemCatalogService.cs`

