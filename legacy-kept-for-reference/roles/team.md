---
type: meta
description: "Team/member model schema and initial team definition for catherder"
---
# Team Definition — catherder

## Schema

Each team member is defined by the fields below. This schema applies to
both human and AI team members.

### Required fields

| Field    | Type                   | Description                                    |
|----------|------------------------|------------------------------------------------|
| `id`     | string                 | Unique short identifier (slug, no spaces)      |
| `name`   | string                 | Display name                                   |
| `type`   | `human` \| `ai-agent`  | Whether this is a human or AI member            |
| `roles`  | string[]               | References to `../catherder-instructions-repo/roles/*.md` (filename stems) |

### Optional fields

| Field         | Type     | Default | Description                                  |
|---------------|----------|---------|----------------------------------------------|
| `skills`      | string[] | `[]`    | References to `../catherder-instructions-repo/skills/*.md` (filename stems) |
| `model`       | string   | —       | Preferred model (AI agents only)             |
| `model_tier`  | string   | —       | `heavy` \| `mid` \| `light` (AI agents only)|
| `personality` | string   | —       | Overrides or extends the role's personality  |
| `notes`       | string   | —       | Free-form context                            |

### Design notes

- **Roles reference `../catherder-instructions-repo/roles/`.** A member may hold multiple roles
  (e.g. a human who is both architect and product-owner, or an AI agent
  assigned senior-researcher + fact-checker).
- **Skills reference `../catherder-instructions-repo/skills/`.** Skills are additive — they specify
  what the member is competent in, beyond what the role already implies.
- **Model and model_tier are AI-only.** They guide which vendor model to
  use when assigning work to this member. The tier classification matches
  `.instructions/project.INSTRUCTIONS.md` §4 (heavy / mid / light).
- **Personality is an override.** Roles already define a baseline
  personality. This field is for member-specific adjustments (e.g. "more
  cautious than the role baseline" or "prefers terse output").

### Extensibility (future)

These fields are not used today but may be added later:

- `availability` — scheduling constraints for humans, rate limits for AI.
- `cost_budget` — per-task or per-session cost cap for AI members.
- `preferred_tools` — IDE, terminal, or MCP tools this member should use.
- `context_window` — max tokens for AI members (model-dependent).

---

## Current Team

### Human Members

#### anders

| Field    | Value                                      |
|----------|--------------------------------------------|
| `id`     | `anders`                                   |
| `name`   | Anders                                     |
| `type`   | `human`                                    |
| `roles`  | `product-owner`, `architect`, `lead-dev`   |
| `notes`  | Supervisor. All merges to main require his approval. |

### AI Agent Members

AI agents are assigned per-task, not permanently. The members below
represent recurring assignment patterns.

#### agent-heavy

| Field        | Value                                               |
|--------------|-----------------------------------------------------|
| `id`         | `agent-heavy`                                       |
| `name`       | Heavy Agent                                         |
| `type`       | `ai-agent`                                          |
| `roles`      | `senior-researcher`, `instructions-architect`, `architect`, `senior-dev` |
| `model`      | Claude Opus 4.5 / 4.6 (or equivalent)               |
| `model_tier` | `heavy`                                             |
| `notes`      | Used for quality-critical tasks: architecture, deep analysis, design decisions, complex code. |

#### agent-mid

| Field        | Value                                               |
|--------------|-----------------------------------------------------|
| `id`         | `agent-mid`                                         |
| `name`       | Mid Agent                                           |
| `type`       | `ai-agent`                                          |
| `roles`      | `senior-dev`, `code-reviewer`, `fact-checker`       |
| `model`      | Claude Sonnet 4.5 / GPT-5.1 (or equivalent)         |
| `model_tier` | `mid`                                               |
| `notes`      | Used for planning, orchestration, code generation, structured writing. |

#### agent-light

| Field        | Value                                               |
|--------------|-----------------------------------------------------|
| `id`         | `agent-light`                                       |
| `name`       | Light Agent                                         |
| `type`       | `ai-agent`                                          |
| `roles`      | `junior-dev`, `junior-researcher`                   |
| `model`      | GPT-5 mini / Gemini 3 Flash (or equivalent)          |
| `model_tier` | `light`                                             |
| `notes`      | Used for breadth-first research, mechanical edits, simple classification. Low cost. |

---

## Assignment Convention

When a plan or task specifies a role and model tier, match it to a team
member:

- **Role:** determines which `../catherder-instructions-repo/roles/*.md` personality and constraints
  to apply.
- **Model tier / model:** determines which AI model to invoke.
- **Skills:** determine which `../catherder-instructions-repo/skills/*.md` files to include in
  context.

Example from Plan 004:
> **004c** — Role: Senior Researcher, Model: Claude Opus 4.5
> → Assign to `agent-heavy` with the `senior-researcher` role active.
