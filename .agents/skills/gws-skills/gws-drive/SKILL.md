---
name: gws-drive
version: 1.3.0
description: "Access files and folders in Google Drive. Use this skill to list, search, upload, edit, delete, download files, documents and folders in Google Drive."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["gws"]
    cliHelp: "gws drive --help"
---
## Help and instructions - discover gws command syntax and subcommands
gws drive --help

--params and --json takes JSON string as arguments. Use \" (backslash, quote) to escape quotes inside JSON values.
To ensure accurate JSON parameter formatting in gws commands, always use double quotes (") for keys and string values, and escape inner quotes with a backslash (\"). 
Example:  --params '{"q":"\"FOLDER_ID\" in parents","pageSize":10}'

## Output Formatting for listing of files and folders
When output is meant to be consumed by humans, format drive/folder listings as Markdown table 
`| Icon | Name (link) | Type | Size |`. 
No IDs. Link via `webViewLink`. Size in KB/MB ("—" for folders/Docs/Sheets). Folders first.
**Icons for human formatting:** 📁 folder · 📄 doc/pdf · 📊 sheet · 📘 excel · 📽️ slide · 📋 form · 🖼️ image · 🎬 video · 🎵 audio · 📎 

When output is meant to be consumed by tools/agents, use `--format json` and include IDs and other metadata.

## Recipes

**Upload:** 
gws drive +upload <file> [--parent <ID>] [--name <NAME>]

**Create Folder:** 
gws drive files create --json '{"name":"FOLDER_NAME_TO_CREATE","mimeType":"application/vnd.google-apps.folder","parents":["PARENT_FOLDER_ID"]}'

**Move:** 
gws drive files update --params '{"fileId":"ID","addParents":"NEW_FOLDER","removeParents":"OLD_FOLDER"}'

**List Contents (2 steps if ID unknown):**
1. Get ID for FOLDER_NAME: gws drive files list --params '{"q":"name=\"FOLDER_NAME\" and mimeType=\"application/vnd.google-apps.folder\" and trashed=false","fields":"files(id,name)"}'
2. List files in FOLDER_ID: gws drive files list --params '{"q":"\"FOLDER_ID\" in parents and trashed=false","fields":"files(id,name,mimeType,size,webViewLink)","pageSize":100}'
