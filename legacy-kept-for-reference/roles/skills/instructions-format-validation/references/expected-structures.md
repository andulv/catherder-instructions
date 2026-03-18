# Expected Structures by File Type

**Last Updated:** 2026-03-04T01:50:00+01:00
**Authoritative Source:** `.instructions/plans/TEMPLATE.md` and `.instructions/plans/tasks/TEMPLATE.md`

Per-type reference for `instructions-format-validation`.
Derived from conventions, templates, and observed patterns.

> Authoritative source: `.instructions/plans/TEMPLATE.md` and `.instructions/plans/tasks/TEMPLATE.md`  
> If this file conflicts with that source, defer to the source.


## Plan  (`type: plan`)

```
type: plan
description: "..."
# Plan NNN — Title

**Status:** draft | in-progress | completed | abandoned
**Branch:** feature/NNN-slug
**Created:** YYYY-MM-DDTHH:MM:SS+HH:MM
**Updated:** YYYY-MM-DDTHH:MM:SS+HH:MM

## Goal
## Context / Why
## Tasks
## Acceptance Criteria
## Role Assumptions   (optional)
```

**Required sections:** Goal, Tasks, Acceptance Criteria
**Required metadata:** Status, Created, Updated
**Optional sections:** Context / Why, Role Assumptions, Risks, Scope, External Resources


## Task  (`type: task`)

```
type: task
description: "..."
# Task NNNx — Title

**Status:** not-started | in-progress | completed | blocked
**Created:** YYYY-MM-DDTHH:MM:SS+HH:MM
**Updated:** YYYY-MM-DDTHH:MM:SS+HH:MM

## Task ID
## Objective
## Scope
## Steps
## Verification
## Notes            (optional)
## Changelog        (optional)
```

**Required sections:** Scope, Steps, Verification
**Required metadata:** Status, Created, Updated
**Optional sections:** Notes, Changelog


## Role  (`type: role`)

```
type: role
description: "..."
# Role: Name

## Summary
## Background / CV
## Personality
## Primary Goals
## Responsibilities
```

**Required sections:** Summary, Primary Goals, Responsibilities
**Optional sections:** Background / CV, Personality


## Skill  (`type: skill`)

```
type: skill
description: "..."
alwaysApply: false    (optional)
# Skill: Name

## topic heading(s)
## Sources           (optional)
```

**Required:** At least one substantive section beyond H1
**Notes:** `description` should include trigger phrases (what + when) to help
the agent decide activation. Only `name` and `description` are required
front-matter fields; other fields depend on the tool reading the skill.


## Workflow  (`type: workflow`)

```
type: workflow
description: "..."
alwaysApply: true     (optional)
# Workflow Title

## section heading(s)
```

**Required:** At least one substantive section
**Notes:** Workflows with `alwaysApply: true` are loaded into every agent context.


## Research  (`type: research`)

```
type: research
description: "..."
# Research: Topic

## Summary
## Findings
## Sources
```

**Required sections:** Summary, Findings, Sources


## Meta  (`type: meta`)

```
type: meta
description: "..."
# Title
```

**Required:** None beyond front-matter + H1
**Notes:** Used for README.md, SCRATCHPAD.md, and other structural files.


## SCRATCHPAD.md (special case)

No front-matter required. Expected structure:

```
# Scratchpad

## Last Updated: YYYY-MM-DDTHH:MM:SS+HH:MM

## Current Context
## Session Notes
```
