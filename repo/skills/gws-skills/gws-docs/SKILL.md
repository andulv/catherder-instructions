---
name: gws-docs
version: 1.0.0
description: "Read and write Google Docs."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws docs --help"
---

# docs (v1)

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

```bash
gws docs <resource> <method> [flags]
```

## Quick Commands

### `+write` Append Text

```bash
gws docs +write --document <ID> --text <TEXT>
```

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--document` | Yes | - | Document ID |
| `--text` | Yes | - | Text to append (plain text) |

Examples:

```bash
gws docs +write --document DOC_ID --text 'Hello, world!'
```

Tips:

- Text is inserted at the end of the document body.
- For rich formatting, use `documents.batchUpdate`.
- This is a write command, confirm with the user before executing.

## API Resources

### documents

  - `batchUpdate` — Applies one or more updates to the document. Each request is validated before being applied. If any request is not valid, then the entire request will fail and nothing will be applied. Some requests have replies to give you some information about how they are applied. Other requests do not need to return information; these each return an empty reply. The order of replies matches that of the requests.
  - `create` — Creates a blank document using the title given in the request. Other fields in the request, including any provided content, are ignored. Returns the created document.
  - `get` — Gets the latest version of the specified document.

## Common Recipes

### Create a Doc from a Template

Use this when you need a new doc from a template, then fill and share it.

1. Copy the template: `gws drive files copy --params '{"fileId": "TEMPLATE_DOC_ID"}' --json '{"name": "Project Brief - Q2 Launch"}'`
2. Get the new doc ID from the response.
3. Add content: `gws docs +write --document NEW_DOC_ID --text '## Project: Q2 Launch\n\n### Objective\nLaunch the new feature by end of Q2.'`
4. Share with team: `gws drive permissions create --params '{"fileId": "NEW_DOC_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "team@company.com"}'`

## Discovering Commands

Before calling any API method, inspect it:

```bash
# Browse resources and methods
gws docs --help

# Inspect a method's required params, types, and defaults
gws schema docs.<resource>.<method>
```

Use `gws schema` output to build your `--params` and `--json` flags.

