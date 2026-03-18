---
type: reference
description: "File format standards for CatHerder artifacts: frontmatter conventions and timestamp requirements"
---
# File Formats

This document defines file-format constraints that support validation, tooling
compatibility, and auditability.

## `.instructions.md` files (Copilot standard)

Files named `*.instructions.md` are treated as instruction files by GitHub
Copilot / VS Code. To maintain compatibility, use the Copilot-standard
frontmatter keys.

Frontmatter keys (all optional):

- `name`: display name in UI (defaults to file name)
- `description`: short description shown on hover
- `applyTo`: glob pattern controlling auto-apply

CatHerder extension (optional):

- `type`: category for internal organization (avoid unless needed)

## `.instructions/` plan/task files (CatHerder + validator)

All `.md` files under `.instructions/` except `SCRATCHPAD.md` must have YAML
frontmatter with:

- `type` (required)
- `description` (required)

For plan draft and active files:
- `type` must be `plan`

For separate task files:
- `type` must be `task`

## Timestamps

Body timestamps must use full ISO 8601 with seconds and explicit timezone
offset:

```
YYYY-MM-DDTHH:MM:SS+HH:MM
```

Invalid by convention: bare dates, `Z` shorthand.

This applies to `Created`, `Updated`, and any other timestamps used in
CatHerder artifacts.
