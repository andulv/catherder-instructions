---
type: reference
description: "Git workflow for CatHerder execution: branch-per-plan, one-commit-per-task, review and merge constraints"
---
# Git Workflow (Optional Module)

Some CatHerder-enabled projects use the plan/task methodology without git. This document defines the git workflow when git is used.

## Core Rules

- If a repository includes `catherder-git.instructions.md`, its rules are mandatory for work involving repository changes or git operations.
- Plan execution happens on a dedicated branch.
- Each completed task is normally one commit.
- Merges to `main` require explicit supervisor approval.

## Branching

- Create a branch when starting execution of a plan, not during drafting.
- Create the branch from `main` unless explicitly directed otherwise.
- Before branching, verify that the source branch is clean. If it is not, stop and ask the user to clean it first.
- Branch name should reflect the plan (for example: `plan/004-catherder-process-instructions`).

## Direct Changes Outside Plans

- Small direct changes on `main` may be acceptable only when the user explicitly requests them.
- Resist larger direct-on-`main` changes that span multiple files.
- For larger changes, ask the user to create a plan and execute the work on a dedicated branch.

## Commits

- One commit per completed task.
- Commit message starts with the task identifier when available (for example `task004-01: ...`).

## Review / Merge

- Use PR review when available.
- Agents must not merge to `main` without explicit supervisor approval.

## Gitless Mode

If a project does not use git:

- The plan/task lifecycle rules still apply.
- The execution contract still applies (one task at a time, immediate marking, verification).
- Branch and commit constraints are simply not applicable.
