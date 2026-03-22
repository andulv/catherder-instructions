# Plan 010 Prompt

CatHerder-enable `tmp-blazor-markdowneditorssample` as a software project using the current CatHerder standards from `catherder-instructions`, while selectively reusing safe project-specific patterns from `tmp-catherder-dev` where the stack and workflow are similar.

Scope:
- target project: `/workspace/tmp-blazor-markdowneditorssample`
- source-of-truth repo: `/workspace/catherder-instructions`
- reference CatHerder-enabled project: `/workspace/tmp-catherder-dev`

Goals:
- add the standard CatHerder bootstrap and instruction structure to the target project
- keep canonical process files aligned with `catherder-instructions`
- adapt project-specific instructions to the Blazor markdown editor sample accurately
- reuse only the `tmp-catherder-dev` guidance that generalizes well to a .NET / Blazor software project
- avoid copying domain-specific agent-orchestration content into the sample project

Expected end state:
- `AGENTS.md`
- `.instructions/project.instructions.md`
- `.instructions/catherder.instructions.md`
- `.instructions/catherder-git.instructions.md`
- `.instructions/project-status-roadmap.md`
- `.instructions/SCRATCHPAD.md`
- `.instructions/plans/`
- `.agents/`

This session is planning only. Do not edit the target project yet.
