---
type: reference
description: "CatHerder philosophy, scope, and why the methodology is structured around plans and tasks"
---
# CatHerder Philosophy

## Core Principle

Plans define **intent**. Tasks execute **intent**.

A plan is a stable contract that expresses *what* and *why*.
Tasks are work items that fulfil the plan.

## Why This Separation Exists

CatHerder optimizes for:

- Stable intent with controlled change (plans)
- Small, independently verifiable execution units (tasks)
- Repeatability and auditability (clear artifacts, timestamps, workflow)

This structure reduces “drift-by-chat” and makes it feasible for humans and
LLMs to collaborate on long-running efforts.

## Canonical vs Derived Artifacts

The canonical process is documented in this `docs/catherder/` folder.

Enabled projects do **not** consume these docs directly during day-to-day work.
Instead, they consume derived/condensed artifacts (skills, templates, instruction
files) that are generated from these canonical sources.

## Compatibility and Tooling

CatHerder conventions intentionally align with:

- GitHub Copilot and VS Code instruction file frontmatter conventions for
  `*.instructions.md` files (see [file-formats.md](file-formats.md))
- The plan/task validator rules used by `plan-task-standards`

Where conventions conflict, prefer compatibility with common tooling and keep
CatHerder-specific extensions optional and minimal.
