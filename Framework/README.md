# Framework document set — which one to use

**Current edition: v5, adopted 2026-10-05** *(v4.1 governed from 2026-08-28 to 2026-10-05 and is kept in
`ARCHIVE - v4.x (superseded 2026-10-05)/`; the adoption is `v5/RULING CASE 2026-10-05 - adopt v5, for the operator's approval.md`).*
**Until 2026-10-05 this line read "Current edition: v4.1."** *(This file said "v3.0 (July 2026)" until 2026-09-20 and routed readers to
three archived PDFs. The 10:32 overnight audit of 2026-09-20 found it: the same stale-pointer defect
`CLAUDE.md` fixed on itself the day before, applied nowhere else. Rewritten to match the documents
in force; the v3.0 pointers are preserved in the archive section below, not deleted. On 2026-09-25 the
operator protocol moved out of `CLAUDE.md` into `OPERATOR-PROTOCOL.md` in this folder, the ledger count
below was replaced by "count the file", and the Q3 manager standard was added to the table; this file is
now read by check 6 of the acceptance test, which fails on any path here that is not on disk.)*

**The rules of work, binding on every session:** `OPERATOR-PROTOCOL.md` — the nine-rule operator protocol,
the six prime rules, the tooling test, the sovereign sources and the standard. Audited by
`tools/check_framework.py` like the governing documents below.

**Two governing documents, two questions** *(operator instruction, 2026-09-13)*:

| Document | Use it when |
|---|---|
| **`THE FRAMEWORK v5.md`** | **Should I buy this?** Every new purchase, and every add to an existing position, because an add is a purchase. The foundations, the standing rule, Q1 to Q12 in the speakers' order, three boxes, every rule carrying its verbatim quote and its id in `principle_ledger_v5.csv`. If a rule is not in it, it is not in force. |
| **`THE HOLDINGS FRAMEWORK v5.md`** | **Should I keep what I own?** Six hold questions and the review's four words, for a position already held. Review surface: `Test Runs/_TEMPLATE - Holding Review.md`. |
| **`SECTOR METHOD - owner earnings for insurers and float-bearing holding companies.md`** | An insurer or a float-bearing holding company: two measurable components plus a judgment, never an owner-earnings number from operating cash flow. |
| **`v4/THE MANAGER STANDARD - Q3.md`** | The v4.1 manager standard, from a full read of the shelf. Incorporated by reference from the archived `ARCHIVE - v4.x (superseded 2026-10-05)/THE FRAMEWORK v4.md` and the archived v4.1 run template; v5 carries its own manager questions (Q5 and Q6) from the meeting rows and does not cite this file. Kept as the v4 record. |

**Around them:**
- **`PLAIN ENGLISH - what this is and how it works.md`** — the non-technical front door; where it and
  the governing document disagree, the document wins.
- **`INVENTIONS - deleted and why.md`** — the 43 numeric rules v4 deleted because no quote stood behind
  them, and what each deletion cost.
- **`v4/`** — the proofs and tests: Tests A, B, C, D and E, the Citigroup 2007 and Coca-Cola 1988
  verification, the regressions on the live names, the tool admissions, the Q2 ruling case of 2026-09-20.
- **`2026-08-26 AUDIT - What Actually Works, and What To Cut.md`** and
  **`2026-08-26 THE FIVE PASSAGES - Synopsis and Rulings.md`** — the audit that produced v4 and
  the five passages it turned on.
- **`v5/`** — the record of how v5 was built, tested and adopted (2026-10-03 to 2026-10-05): the case, the
  pre-registration, the reading register and notes, the theme maps and section drafts, the reconciliation against
  v4.1 in four parts, the five tests and their runs, the PRIME RULE 5 case on PERMANENT and the retention test, and
  the ruling case the operator approved. The governing documents themselves are the two v5 files in the table above.

**The evidence base, at repository root:** `principle_ledger.csv` *(count the file, never the pointer:
this line said 76 rows, then 267, and both were stale when read)*, each row a verbatim passage with year
and source file, checked by `tools/check_framework.py`. Every `[Ex-xx]` citation in the governing
documents resolves to a row there.

**Running a company:** copy `Test Runs/_TEMPLATE - Company Run.md` to a dated file and fill it top to
bottom. Operator protocol (binding): `OPERATOR-PROTOCOL.md`. Reviewing a holding: the
holding-review template, under the holdings framework. The map of the whole repository is `CLAUDE.md`.

## ARCHIVES — kept as the audit trail, never used for analysis
- **`ARCHIVE - v4.x (superseded 2026-10-05)/`** — `ARCHIVE - v4.x (superseded 2026-10-05)/THE FRAMEWORK v4.md` and
  `ARCHIVE - v4.x (superseded 2026-10-05)/THE HOLDINGS FRAMEWORK.md` as they stood on 2026-10-05, with every correction filed against them up to that day (the three defects of the
  2026-10-04 addendum, the PERMANENT withdrawal and the retention-test correction of 2026-10-05). Every run and review
  dated 2026-08-28 to 2026-10-05 binds under these two files and still cites `principle_ledger.csv`. Their
  templates are `Test Runs/_ARCHIVE - Company Run TEMPLATE v4.1 (superseded 2026-10-05).md` and
  `Test Runs/_ARCHIVE - Holding Review TEMPLATE v4 (superseded 2026-10-05).md`.
- **`ARCHIVE - v3.x (superseded 2026-08-26)/`** — the three v3.0 PDFs this file used to route to
  (*A Framework for Long-Term Business Analysis v3.0*, *The Analysis Workbook v3.0*, *Principles -
  Complete Source Tracing v3.0*), the v3.1 rules block, and
  `ARCHIVE - v3.x (superseded 2026-08-26)/scripts_v3/`, whose generators hardcode
  "v3.0 — July 2026" on every page and must not be re-run.
- **`ARCHIVE - RULINGS 1-14 (resolved into v4, 2026-08-26).md`** — the eighteen rulings that were
  resolved into v4 or deleted. Do not apply them.
- **`ARCHIVE - May 2026 (superseded)/`** — the audited May editions; known defects catalogued in
  `ARCHIVE - May 2026 (superseded)/claims_audit.csv` (at the repository root until 2026-09-26).
  The v3.x archive also holds the two Phase 0 maps of the v3.0 rebuild,
  `ARCHIVE - v3.x (superseded 2026-08-26)/corpus_map.md` and
  `ARCHIVE - v3.x (superseded 2026-08-26)/owners_manual_map.md`, moved from the root the same day.
- **`CHANGELOG.md`** — the v3.0-against-May changelog, frozen at v3.0 (its header says so).
