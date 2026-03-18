---
name: gws-drive
version: 1.3.0
description: "Google Drive: List, search, upload, edit, delete, download files and folders in google drive."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws drive --help"
---

> **Prereq:** `../gws-shared/SKILL.md`. Discover: `gws drive --help` | `gws schema drive.<res>.<meth>`

`gws drive <resource> <method> [flags]`

## Rules & Formatting
- **Efficiency:** ALWAYS constrain `--params '{"fields":"files(id,name,mimeType,size,webViewLink)","pageSize":100}'`. Never loop `get`. Prefer Folder IDs.
- **Quoting:** Outer single quotes, inner double tags: `'{"q":"\"ID\" in parents and trashed=false"}'`. Escape inner quotes for names: `name=\"MyFolder\"`.
- **Output (Humans):** format listings as a Markdown table: `| Icon | Name (as link) | Type | Size |`. NO IDs! Name must be a link (`webViewLink` or `https://drive.google.com/file/d/ID/view`). User-friendly types. Size in KB/MB ("—" for folders and Google Docs/Sheets). Folders first. Then files.
- **Output (Tools/Agents):** Output raw JSON containing IDs. Do NOT use markdown tables or human formatting.
- **Icons:** 📁(folder), 📄(doc/pdf), 📊(sheet), 📘(excel), 📽️(slide), 📋(form), 🖼️(image), 🎬(video), 🎵(audio), 📎(other).

## Recipes
**Upload (Confirm first!):** `gws drive +upload <file> [--parent <ID>] [--name <NAME>]`
**Create Folder:** `gws drive files create --json '{"name":"Q2","mimeType":"application/vnd.google-apps.folder","parents":["ID"]}'`
**Move:** `gws drive files update --params '{"fileId":"ID","addParents":"NEW","removeParents":"OLD"}'`
**List Contents (2 steps if ID unknown):**
1. Get ID: `gws drive files list --params '{"q":"name=\"Name\" and mimeType=\"application/vnd.google-apps.folder\" and trashed=false","fields":"files(id,name)"}'`
2. List: `gws drive files list --params '{"q":"\"ID\" in parents and trashed=false","fields":"files(id,name,mimeType,size,webViewLink)","pageSize":100}'`
