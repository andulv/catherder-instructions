# Plan 012 Source Inventory
Primary evidence selection for Tasks 1–3, derived from plan011 outputs.
## Authoritative input files
- Text manifest: `.instructions/plans/plan011-svein-email-and-attachment-extraction/output/manifests/fragments.jsonl`
- Candidate-document manifest: `.instructions/plans/plan011-svein-email-and-attachment-extraction/output/manifests/candidate-documents.jsonl`
- Attachment directory: `.instructions/plans/plan011-svein-email-and-attachment-extraction/output/attachments`

## Text corpus selection
- Total fragment records available: **116**
- Primary text evidence for style extraction: **`direct_primary` fragments** only for first-pass rule extraction. Count: **64**
- Supporting/context-only text sources: `quoted_context` (**47**), `quoted_svein` (**3**), `forwarded_svein` (**2**)
- Rationale: `direct_primary` is the cleanest available style signal for recurring authored language; other fragment types may help confirm phrases or delivery framing but should not dominate rule extraction.
- Mailbox distribution of all fragments: {'Drafts': 1, 'Inbox': 107, 'Sent': 2, 'Trash': 6}
- Confidence distribution of all fragments: {'high': 69, 'medium': 47}

## Spreadsheet corpus selection
- Total candidate-document records available: **66**
- `.xlsx` candidates identified: **5**
- Confidence distribution for `.xlsx` candidates: {'medium': 5}
- Candidate-class distribution for `.xlsx` candidates: {'unknown': 5}
- Primary spreadsheet evidence: `.xlsx` files only, because they can be deterministically inspected locally for workbook structure and formatting traits.
- Non-Excel attachments (`.pdf`, `.doc`, `.docx`, `.zip`) are excluded from primary workbook-style extraction and may be used only as weak contextual evidence if needed later.

## Selected `.xlsx` files for first-pass workbook analysis
- `.instructions/plans/plan011-svein-email-and-attachment-extraction/output/attachments/Inbox/8d63bc4f904e-Salgsrapport pr november 2022.xlsx` — filename: `Salgsrapport pr november 2022.xlsx`; confidence: `medium`; class: `None`; evidence: `FILENAME_MATCH, FROM_EXACT`
- `.instructions/plans/plan011-svein-email-and-attachment-extraction/output/attachments/Inbox/6f31c5146d19-Vedlegg2 180923 Oversikt lisensinntekter til overføring Omnishop AS.xlsx` — filename: `Vedlegg2 180923 Oversikt lisensinntekter til overføring Omnishop AS.xlsx`; confidence: `medium`; class: `None`; evidence: `FILENAME_MATCH, FROM_EXACT, THREAD_CONTEXT_MATCH`
- `.instructions/plans/plan011-svein-email-and-attachment-extraction/output/attachments/Inbox/f8adcf0e7c6d-051225 Nøkkeltall Plantedamp AS regnskap 311025.xlsx` — filename: `051225 Nøkkeltall Plantedamp AS regnskap 311025.xlsx`; confidence: `medium`; class: `None`; evidence: `FILENAME_MATCH, FROM_EXACT`
- `.instructions/plans/plan011-svein-email-and-attachment-extraction/output/attachments/Inbox/9a690aa350a6-090126 Analyse PD AS og GRO PRO AS fra 2022 til 2025 oppdatert.xlsx` — filename: `090126 Analyse PD AS og GRO PRO AS fra 2022 til 2025 oppdatert.xlsx`; confidence: `medium`; class: `None`; evidence: `FILENAME_MATCH, FROM_EXACT, THREAD_CONTEXT_MATCH`
- `.instructions/plans/plan011-svein-email-and-attachment-extraction/output/attachments/Trash/32c3bc0ef77e-060126 Analyse PD AS og GRO PRO AS fra 2022 til 2025.xlsx` — filename: `060126 Analyse PD AS og GRO PRO AS fra 2022 til 2025.xlsx`; confidence: `medium`; class: `None`; evidence: `FILENAME_MATCH, FROM_EXACT`
