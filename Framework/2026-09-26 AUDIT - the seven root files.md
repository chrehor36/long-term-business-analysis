# AUDIT 2026-09-26 — the seven root files, checked against the files they describe

*At the operator's instruction "organize and audit all of these", given for the seven files that sat at the
repository root on 2026-09-26: `claims_audit.csv`, `CLAUDE.md`, `corpus_map.md`, `owners_manual_map.md`,
`PORTFOLIO.md`, `principle_ledger.csv`, `README.md`. Every check below was a script that opened the file and the
files it points at and reported what matched; the script concluded nothing. Numbers here are this project's own
record, counted from the files on the day.*

## What was organized
| File | Was | Now | Why |
|---|---|---|---|
| `claims_audit.csv` | root | `Framework/ARCHIVE - May 2026 (superseded)/claims_audit.csv` | it audits the May 2026 edition, which lives in that archive; last changed 2026-07-14 |
| `corpus_map.md` | root | `Framework/ARCHIVE - v3.x (superseded 2026-08-26)/corpus_map.md` | a Phase 0 deliverable of the v3.0 rebuild; its framework rows name files that moved to that archive |
| `owners_manual_map.md` | root | `Framework/ARCHIVE - v3.x (superseded 2026-08-26)/owners_manual_map.md` | maps the manual against the eight gates of v3.0 |
| `CLAUDE.md`, `README.md`, `PORTFOLIO.md`, `principle_ledger.csv` | root | root | the map, the front door, the holdings file and the evidence base belong at the root; `PORTFOLIO.md` joined the acceptance test's pointer check |

Every document that pointed at a moved file was repointed the same day (`CLAUDE.md`, `README.md`,
`Framework/README.md`); history files that name the old paths were left as written (operator rule 6).

## What the audit found, file by file

### 1. `claims_audit.csv` (40 rows: 12 VERIFIED, 10 MISATTRIBUTED, 8 NOT FOUND IN CORPUS, 5 PARTIAL, 5 UNSUPPORTED)
Every quoted fragment of 25 characters or more in the evidence column was searched, normalised, across the eight
shelf folders. **Every VERIFIED row whose evidence carries a quotation is found on the shelf** (C03, C06, C07, C09,
C12, C13, C17, C30, C35, C39, C40; C33 is a taxonomy attribution with no quotation). Fragments not found sit only
in MISATTRIBUTED, PARTIAL and NOT FOUND rows, where the evidence column quotes the disputed claim itself or the
auditor's prose, which is what those verdicts mean. The file is sound as a record and is frozen.

### 2. `corpus_map.md` (317 files listed)
Every corpus path in its table exists on disk, and **no file in any corpus folder is missing from the table**
(0 unlisted across the eight shelf folders and the three context folders). The 14 paths it lists that no longer
exist are all v3.0 framework files (the May PDFs and text extracts, the v3.0 PDFs, `scripts_v3/`), which moved to
the archives on 2026-08-26. Its folder counts and shelf labels still match PRIME RULE 4. So: corpus rows current,
framework rows superseded, as its dated note of 2026-09-25 said.

### 3. `owners_manual_map.md` (33 block quotations)
Each quotation was split at its ellipses and every segment of 20 characters or more was searched in the manual's
text. **33 of 33 verify.** The mapping is against the v3.0 gates and is history.

### 4. `PORTFOLIO.md`
- 72 distinct ledger ids cited, **0 phantom**.
- 53 backticked paths, 1 missing: `Framework/v4/RERUN 3`, a shorthand, written in full the same day. With
  `PORTFOLIO.md` in `POINTER_DOCS`, check 6 now keeps it that way.
- **The opportunity table was reconciled against `tools/alerts.json` and against the register.** Every register
  entry that cleared the four business gates has a row. But **ten tickers with armed alerts had no row and no
  register entry: CSL, HD, ITW, LOPE, LOW, LSTR, OTIS, PNR, RPM, SHW**, all v4.1 runs of 2026-08-31 and 2026-09-01,
  each with Q1 to Q4 IN in its run file and a Q5 that quit on at the floor. Three (CSL, LOPE, OTIS) appear nowhere
  in the queue file. They ran before the FOLD rule of 2026-09-07; the backfill of 2026-09-13 caught the failed runs
  of those days and missed these. **Fixed the same day: ten rows in `PORTFOLIO.md`, a dated backfill section in the
  register, every figure copied from the committed run file.** Consequence: every gate-clearer count stated before
  2026-09-26 (the "34" of the session-state file) is understated by at least ten. Count from the register.
- Nine table rows have no register entry and are not expected to: ASML, COST, HRB, MITSY, NCLTY, NHNKY, TBTC,
  TJX, V are holdings, pre-queue runs or a resolved identity.
- Header wording corrected 2026-09-25 (dated note in the file); cash line still says "needs reconfirmation".

### 5. `principle_ledger.csv` (311 rows)
- Checks 3 and 4 of the acceptance test PASS: 311 unique ids, every source file on disk, 310 verbatim plus the
  one declared NOT A QUOTATION (E5-07).
- The `era` column matches the id prefix on every row.
- 14 rows carry a `year` that is not a year in the source filename; all 14 are E1 partnership rows where the year
  is the partnership year and the letter is dated the following January (the file's convention, stated in the
  cell). No defect.
- Five pairs of rows share the same opening 150 characters; they are the five declared alias pairs (nine rows
  carry ALIAS NOTE, because one passage sits under three ids). No undeclared duplicate.
- Ids **E2-34 and E3-36 do not exist and never did** (no commit ever added them); the sequences skip them. Cosmetic.
- Citation coverage: 248 rows are cited by a governing or live document, 13 more only by run files, and **50 rows
  are cited nowhere**: E1-01, E1-04, E1-05, E1-06, E1-07, E1-09, E1-10, E1-11, E1-12, E1-13, E1-14, E2-02, E2-03,
  E2-05, E2-06, E2-07, E2-11, E2-12, E2-13, E2-15, E2-18, E2-19, E2-20, E2-21, E2-33, E3-05, E3-06, E3-07, E3-09,
  E3-11, E3-12, E3-16, E3-18, E3-19, E3-20, E3-21, E3-22, E3-23, E4-03, E4-05, E4-06, E4-07, E4-09, E4-10, E4-54,
  E5-02, E5-03, E5-04, E5-05, E5-10. They are evidence, not rules; an uncited verbatim row costs nothing and may be
  needed by a later ruling. Left as they are.
- The E5-08 note's coursework path was corrected 2026-09-25 by an appended note; the quote column untouched.

### 6. `CLAUDE.md` (the map, rewritten 2026-09-25)
In `DOCS` and `POINTER_DOCS`: 0 phantom ids, 0 unlabelled numbers, every path on disk. Three rows repointed
today for the moved files; the Owner's Manual row no longer names the moved map. The import of
`Framework/OPERATOR-PROTOCOL.md` was verified in a fresh headless session on 2026-09-25 (nine rules loaded).

### 7. `README.md` (the human front door, rewritten 2026-09-25)
In `POINTER_DOCS`: every path on disk after today's repoint of `claims_audit.csv`. Its honest-record section is the
2026-07-25 text verbatim with a dated addendum; nothing in it contradicts operator rule 7.

## What this audit did not do
It did not re-derive any run, re-price any name, or change any verdict. The ten backfilled entries carry the
prices and sovereigns of their run dates. It did not decide whether uncited ledger rows should be retired; that is
a PRIME RULE 5 question for the operator if it is ever asked.
