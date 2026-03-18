---
type: reference
description: "Plan 009 Task 2 approved upstream guidance model for concise, reliable CatHerder instruction surfaces"
---
# Plan 009 Task 2 — Approved Guidance Model

## Goal

Define the upstream guidance model to use when refining local instructions in this repository and when updating canonical and published CatHerder artifacts.

The model should optimize for:
- concise instruction surfaces
- reliable and constructive agent behavior
- low startup context cost
- minimal duplication between files
- clearer responsibility boundaries between instruction documents

## Approved Model by File Role

### 1. `AGENTS.md` — minimal bootstrap only
**Role:** bootstrap entry point for agents opening the repository

**Should do:**
- state that project instructions live under `.instructions/`
- point to `project.instructions.md` as the startup file
- optionally remind agents to update `SCRATCHPAD.md` at session end

**Should not do:**
- duplicate process rules
- include repository structure walkthroughs
- include planning/execution rules
- become a broad startup checklist

**Preferred style:**
- minimal
- imperative
- one-screen and high-signal

### 2. `README.md` — orientation for humans and agents, not operational policy
**Role:** explain what the repository is, why it exists, rough layout, and where to start

**Should do:**
- explain repository purpose concisely
- identify major areas and their roles
- point contributors/agents to the real instruction entry point

**Should not do:**
- duplicate detailed `.instructions/` process rules
- become the primary day-to-day operating contract
- contain stale/transitional structure notes unless clearly marked

**Preferred style:**
- orienting rather than governing
- concise and front-loaded with the most important distinctions

### 3. `project.instructions.md` — repository-specific entry and navigation authority
**Role:** authoritative repository-specific entry guidance

**Should do:**
- define what to read first and when
- provide document map / required vs conditional reading guidance
- describe repository-specific structure and distinctions
- identify important repository-local cautions and ignore-by-default areas

**Should not do:**
- restate full process rules from `catherder.instructions.md`
- carry generic git policy that belongs in `catherder-git.instructions.md`
- become bloated with methodology explanation that belongs in canonical docs or README

**Preferred style:**
- document-map-first
- explicit about conditional reading
- optimized for low-context startup

### 4. `catherder.instructions.md` — invariant process rules only
**Role:** authoritative process contract inside the repository

**Should do:**
- define planning vs execution rules
- define prompt precedence, stop rules, persistence norms, task discipline, timestamps, and other cross-cutting process behavior
- refer back to `project.instructions.md` for repository-specific entry guidance

**Should not do:**
- duplicate repository reading/navigation maps
- include broad repository-orientation content
- compete with `project.instructions.md` for startup authority

**Preferred style:**
- stable
- reusable across repositories
- process-focused rather than repository-focused

### 5. `catherder-git.instructions.md` — optional git-specific policy module
**Role:** authoritative git workflow rules when present

**Should do:**
- define branch-per-plan, source-branch cleanliness, direct-on-main constraints, task-to-commit expectations, and merge approval rules
- use neutral, precise, testable wording
- clearly distinguish required refusal conditions from softer recommendations

**Should not do:**
- use anthropomorphic, emotional, or personality-dependent language for policy
- duplicate non-git process rules already covered elsewhere
- rely on implied behavior where explicit refusal or escalation is required

**Preferred style:**
- concise
- policy-like
- unambiguous and machine-followable

## Design Principles for Concise, Reliable Instructions

### Single-purpose files
Each instruction file should have a primary job:
- bootstrap
- orientation
- repository entry/navigation
- process
- git policy

If multiple files attempt the same job, agents waste context and compliance becomes less reliable.

### Document maps over blanket startup lists
Prefer `read this first; read these when needed` over `read everything` guidance.
This lowers context cost and reduces instruction conflicts.

### One authority per topic
Use one file as the authority for each topic:
- entry/navigation → `project.instructions.md`
- process → `catherder.instructions.md`
- git policy → `catherder-git.instructions.md`

### Low-duplication startup
Short reminders and links are acceptable; repeated policy text is not.
Duplication should be treated as drift risk.

### Neutral, testable policy language
Prefer wording agents can follow consistently:
- "ask"
- "stop"
- "refuse"
- "read when"
- "do not"

Avoid language like:
- "you don't like"
- "complain"
- "nag"

### Local vs canonical separation
Keep local project specifics local.
Only upstream wording and structure that generalize across CatHerder-enabled repositories.

## Canonical Implications

The approved model implies these canonical changes should be pursued later in execution tasks:
- strengthen canonical guidance for minimal `AGENTS.md` bootstrap role
- explicitly document that `project.instructions.md` owns entry/navigation
- explicitly document that `catherder.instructions.md` should stay process-only
- improve canonical git workflow wording to match the neutral, precise style
- decide whether a reusable `project.instructions.md` example/template should exist in `repo/instructions/`

## Deferred / Open Question

A remaining design decision is whether `project.instructions.md` should exist as a published reusable artifact in `repo/instructions/` or remain a documented pattern described only in canonical docs. That decision belongs to Plan 009 Task 6.
