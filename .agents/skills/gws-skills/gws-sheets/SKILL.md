---
name: gws-sheets
version: 1.0.0
description: "Google Sheets: Read and write spreadsheets."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws sheets --help"
---

# sheets (v4)

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

```bash
gws sheets <resource> <method> [flags]
```

## Quick Commands

### `+read` Read Values

```bash
gws sheets +read --spreadsheet <ID> --range <RANGE>
```

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--spreadsheet` | Yes | - | Spreadsheet ID |
| `--range` | Yes | - | Range like `Sheet1!A1:D10` |

Examples:

```bash
gws sheets +read --spreadsheet ID --range 'Sheet1!A1:D10'
gws sheets +read --spreadsheet ID --range Sheet1
```

### `+append` Append Rows

```bash
gws sheets +append --spreadsheet <ID> [--values <CSV>] [--json-values <JSON_ROWS>]
```

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--spreadsheet` | Yes | - | Spreadsheet ID |
| `--values` | No | - | Comma-separated values for one row |
| `--json-values` | No | - | JSON rows, e.g. `[["a","b"],["c","d"]]` |

Examples:

```bash
gws sheets +append --spreadsheet ID --values 'Alice,100,true'
gws sheets +append --spreadsheet ID --json-values '[["a","b"],["c","d"]]'
```

Tips:

- Use `+read` for read-only access.
- `+append` is a write command, confirm with the user before executing.

## API Resources

### spreadsheets

  - `batchUpdate` — Applies one or more updates to the spreadsheet. Each request is validated before being applied. If any request is not valid then the entire request will fail and nothing will be applied. Some requests have replies to give you some information about how they are applied. The replies will mirror the requests. For example, if you applied 4 updates and the 3rd one had a reply, then the response will have 2 empty replies, the actual reply, and another empty reply, in that order.
  - `create` — Creates a spreadsheet, returning the newly created spreadsheet.
  - `get` — Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. By default, data within grids is not returned. You can include grid data in one of 2 ways: * Specify a [field mask](https://developers.google.com/workspace/sheets/api/guides/field-masks) listing your desired fields using the `fields` URL parameter in HTTP * Set the includeGridData URL parameter to true.
  - `getByDataFilter` — Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. For more information, see [Read, write, and search metadata](https://developers.google.com/workspace/sheets/api/guides/metadata). This method differs from GetSpreadsheet in that it allows selecting which subsets of spreadsheet data to return by specifying a dataFilters parameter. Multiple DataFilters can be specified.
  - `developerMetadata` — Operations on the 'developerMetadata' resource
  - `sheets` — Operations on the 'sheets' resource
  - `values` — Operations on the 'values' resource

## Discovering Commands

Before calling any API method, inspect it:

```bash
# Browse resources and methods
gws sheets --help

# Inspect a method's required params, types, and defaults
gws schema sheets.<resource>.<method>
```

Use `gws schema` output to build your `--params` and `--json` flags.

