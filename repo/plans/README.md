---
type: workflow
description: "Plans — folder structure, lifecycle stages, and authoring guide"
---
# Plans: Structure & Workflow

This document defines how plans are authored, structured, and progressed
through their lifecycle. Plans live under `.instructions/plans/`.

## Core Principle

Plans define **intent**. Tasks execute **intent**. Do not merge these
concerns. A plan is a stable contract; tasks are disposable work items
that fulfil it.

---

## Folder Structure

Each plan lives in its own folder:

```
.instructions/plans/
  planNNN-short-description/
    planNNN-prompt.md        # Stage 1: Prompt / Brainstorm
    planNNN-draft.md         # Stage 2: Draft
    planNNN.md               # Stage 3: Active (the canonical plan)
    data/                    # Supporting research, notes, snapshots
    tasks/                   # Separate task files (when needed)
```

### Naming

- **Folder:** `planNNN-short-description` — zero-padded 3-digit number +
  kebab-case summary (e.g., `plan001-create-skill-for-skill-file-standards`).
- **Files inside** use the same `planNNN` prefix so they sort together and
  are unambiguous when referenced from outside the folder.
- **NNN** is a monotonically increasing sequence scoped to the project.

### `data/`

Holds supporting material created *during* the plan lifecycle:
research notes, source summaries, extracted guidance, brainstorm outputs,
inspiration files, or anything that informs the plan but is not part of
the deliverable.

Files in `data/` are reference material — they do not need front-matter
or strict formatting, but should have a clear title and date when
freshness matters.

### `tasks/`

Holds separate task files when a task outgrows inline definition.
See **Tasks** section below.

---

## Lifecycle Stages

A plan progresses through three stages. Each stage has its own file and
its own purpose. Not every plan needs all three files — a simple plan
may skip the prompt stage or go straight to active — but the stages
define the expected progression.

### Stage 1: Prompt / Brainstorm (`planNNN-prompt.md`)

**Purpose:** Capture raw intent before any structure is applied.

**Content:** Free-form text from human and/or AI. May include:
- The original request or idea
- Links to relevant resources, docs, prior art
- Open-ended questions and options
- Copy-pasted context (chat excerpts, emails, issue descriptions)
- Inspiration or reference material

**Rules:**
- No template required — free text is fine.
- No front-matter required (optional).
- This file is *input* to the drafting process, not a deliverable.
- May be created by a human, an AI, or collaboratively.

**Template:** `TEMPLATE-prompt.md` (minimal, mostly reminders).

### Stage 2: Draft (`planNNN-draft.md`)

**Purpose:** Structure the intent into a plan shape. Focus on *what*
we want to achieve and *higher-level how*, without committing to
concrete tasks.

**Content:**
- Goal (clear, one or two sentences)
- Context / Why (problem statement, motivation)
- What We Want To Achieve (desired outcomes)
- Summary Of Work Needed (narrative, not tasks)
- Key Principles or Constraints
- Open Questions (things to resolve before activating)
- Alternatives or options under consideration

**Rules:**
- Uses YAML front-matter with `type: plan`.
- Status is `draft`.
- Does NOT contain concrete task checklists — those belong in the
  active plan.
- May contain a rough "summary of work needed" section describing
  areas of work without task-level detail.
- Open questions should be called out explicitly — they are the
  checklist for "is this ready to activate?"

**Template:** `TEMPLATE-draft.md`.

### Stage 3: Active (`planNNN.md`)

**Purpose:** The canonical, actionable plan. This is the contract that
tasks execute against.

**Content:**
- Goal (same as draft, possibly refined)
- Context / Why (same as draft, possibly tightened)
- Tasks (concrete, actionable checklist with checkboxes)
- Acceptance Criteria (measurable, checkable)
- Role Assumptions (optional)
- Notes (discoveries, decisions, context learned during execution)

**Rules:**
- Uses YAML front-matter with `type: plan`.
- Status progresses: `active` → `completed` or `abandoned`.
- Tasks are defined as checkboxes (`- [ ]` / `- [x]`).
- Each task should be independently verifiable.
- When a task is completed, mark it immediately and update the
  `**Updated:**` timestamp.
- References to prompt and draft are kept in the Notes section.

**Template:** `TEMPLATE.md`.

---

## Status Values

| Status      | Meaning                                           |
|-------------|---------------------------------------------------|
| `draft`     | Plan is being shaped; not yet actionable           |
| `active`    | Plan is approved and being executed                |
| `completed` | All tasks and acceptance criteria are met          |
| `abandoned` | Plan was dropped (document why in Notes)           |

Draft plans use `planNNN-draft.md`. When a plan is activated, the
active file `planNNN.md` is created with status `active`. The draft
file is kept as history.

---

## Tasks

### Inline tasks (default)

Define tasks directly in the active plan file using checkboxes:

```markdown
## Tasks

- [ ] Task 1: Short description of what to do
- [ ] Task 2: Another concrete action
- [x] Task 3: This one is done
```

### Separate task files (when needed)

Create a file under the plan's `tasks/` folder when a task requires:
- Multi-page step-by-step instructions
- Embedded scripts or code samples
- A detailed changelog tracking multiple attempts
- Complex verification procedures

**Naming:** `taskNNN-NN-short-name.md` where `NNN` matches the plan number
and `NN` is a zero-padded two-digit task number (01, 02, ...).

When a separate task file exists, the plan should reference it:
```markdown
- [ ] Task 1: Short description — see `tasks/taskNNN-NN-short-name.md`
```

### Task file format

Separate task files use front-matter with `type: task` and follow the
task template structure (Objective, Scope, Steps, Verification).

---

## Progression Workflow

```
1. Human or AI captures an idea
   → Create planNNN-prompt.md (or skip if intent is already clear)

2. Structure the idea into a draft
   → Create planNNN-draft.md
   → Resolve open questions (discuss, research, decide)

3. Activate the plan
   → Create planNNN.md with concrete tasks and acceptance criteria
   → Create git branch: plan/NNN-short-description
   → Status: active

4. Execute tasks
   → One task at a time
   → One commit per task
   → Mark completed immediately in planNNN.md

5. Complete or abandon
   → When all acceptance criteria are met: status → completed
   → If plan is dropped: status → abandoned, document why
```

### Who creates what?

- **Prompt:** Usually a human, but can be AI-assisted.
- **Draft:** Human or AI, often collaboratively. AI is good at
  structuring a prompt into draft form.
- **Active plan:** Ideally reviewed by a human before activation,
  especially for plans with architectural impact.
- **Tasks:** Can be created by AI during execution, but the plan
  (which tasks derive from) should be stable.

---

## Relationship to Other Workflow Docs

- `repo/instructions/catherder.instructions.md` — Core plan/task execution contract for agents.
- `repo/instructions/catherder-git.instructions.md` — Optional git add-on (branching/commits).
- `repo/agents/` — Agent definition file conventions and templates.
- `repo/skills/plan-task-standards/` — Reference + validator for plan/task structure.

---

## Templates

| File                  | Purpose                           |
|-----------------------|-----------------------------------|
| `TEMPLATE-prompt.md`  | Stage 1: Prompt / Brainstorm      |
| `TEMPLATE-draft.md`   | Stage 2: Draft                    |
| `TEMPLATE.md`         | Stage 3: Active plan              |

---

## Evolution

This structure is expected to iterate. The stages (prompt → draft →
active) reflect current practice. As we learn more, stages may be
added, merged, or refined. When that happens, update this document
and the templates together.
