# Plan 011 Inventory

**Created:** 2026-03-23T00:00:00+00:00
**Updated:** 2026-03-23T00:00:00+00:00

## Confirmed archive structure

Primary source archive is a Maildir-style mailbox under:
- `reference/mailbox-anders-plantedamp/`

Confirmed mail folders observed:
- `Archive`
- `Arkiv`
- `Barcelona-2023`
- `Betalingslev-kuker`
- `Drafts`
- `Inbox`
- `Innsyn-CBD`
- `Reiseregning`
- `Sent`
- `Spam`
- `Trash`

Each mail folder uses standard Maildir subfolders where present:
- `cur/`
- `new/`
- `tmp/`

Also present in folders:
- `.uidvalidity`
- `.mbsyncstate`

## Initial message volume snapshot

File counts from Maildir message directories:

- `Inbox`: `cur=1999`, `new=265`, `tmp=0`
- `Sent`: `cur=1006`, `new=0`, `tmp=0`
- `Trash`: `cur=1551`, `new=35`, `tmp=0`
- `Drafts`: `cur=24`, `new=1`, `tmp=0`
- `Innsyn-CBD`: `cur=26`, `new=3`, `tmp=0`
- `Barcelona-2023`: `cur=6`, `new=0`, `tmp=0`
- `Reiseregning`: `cur=3`, `new=0`, `tmp=0`
- `Betalingslev-kuker`: `cur=1`, `new=0`, `tmp=0`
- `Archive`: `cur=0`, `new=0`, `tmp=0`
- `Arkiv`: `cur=0`, `new=0`, `tmp=0`
- `Spam`: `cur=0`, `new=0`, `tmp=0`

The largest likely-relevant message concentrations are currently `Inbox`, `Sent`, and `Trash`.

## Confirmed direct Svein matches

Quick text probing confirms multiple messages containing direct identity clues:
- `svein@byrknes.no`
- `Svein Skorpen`

Example confirmed direct sender hit:
- Source: `reference/mailbox-anders-plantedamp/Inbox/cur/1774229759.210405_7.tp-anders,U=7:2,S`
- `From:` `Svein Skorpen <svein@byrknes.no>`
- `Date:` `Wed, 28 Sep 2022 04:14:30 +0000`
- `Subject:` `SV: Vaporizere - Produktkategorier, bruksområde, teknologi, brukersegmenter/use-cases`

Probe output also showed many additional files with either the exact email address or exact name present, including files under `Inbox/cur` and `Drafts/cur`, which supports the need for later heuristic filtering rather than simple string matching.

## Available tooling

Confirmed available local tools:
- `python3` — `Python 3.12.3`
- `grep` — `GNU grep 3.11`
- `find` — `GNU findutils 4.9.0`

Confirmed parsing approach:
- Python standard-library email parsing is available and sufficient for first-pass Maildir traversal and MIME parsing.

## Missing or not-yet-confirmed tooling

Not yet confirmed or intentionally deferred unless needed later:
- dedicated HTML-to-text normalization helpers
- document metadata extractors
- PST-specific tooling
- LLM-assisted review tooling

## Notes

- Archive handling can stay local and non-destructive.
- Initial evidence supports using Python standard-library parsing as the default implementation path.
- Direct string-match probing is useful for discovery but is not sufficient for final retained-text filtering because non-Svein messages may quote or mention him.
