# A FRAMEWORK FOR LONG-TERM BUSINESS ANALYSIS
# The map of the project. Every session inherits this file.

A Buffett and Munger citation shelf, an investment framework built only from verbatim quotes in that
shelf, and the record of every business run through it. Two questions govern: **should I buy this?**
(`Framework/THE FRAMEWORK v4.md`) and **should I keep what I own?** (`Framework/THE HOLDINGS FRAMEWORK.md`).
**Ignore `MBA - UNG/`.** It is university coursework that shares this repository. Do not read it, search it,
cite it or edit it during framework work, and leave its uncommitted changes out of every commit. Open it only when the
operator asks about the coursework by name. `Curriculum/` is a class charter and is likewise out of scope;
nothing in the framework depends on either.

@Framework/OPERATOR-PROTOCOL.md

**The file above binds every session.** It carries the operator protocol and the prime rules, lifted
from this file on 2026-09-25 so that they can be audited by the acceptance test. No run starts before
it is read. If the import did not load, open `Framework/OPERATOR-PROTOCOL.md` now.

---
## READ FIRST, IN ORDER

| | File | Why |
|---|---|---|
| ① | `Framework/OPERATOR-PROTOCOL.md` | binding; the rules of work |
| ② | `Framework/THE FRAMEWORK v4.md` | should I buy this? Every purchase and every add, because an add is a purchase |
| ③ | `Framework/THE HOLDINGS FRAMEWORK.md` | should I keep what I own? H1 to H5, four outcomes |
| ④ | `Screens/RESUME STATE 2026-09-12 - Opus session, note for Fable.md` | the session-state file; its last dated section says where everything stood when the previous session closed and what to do next |
| ⑤ | `Screens/WATCHLIST RUN QUEUE.md` | the register of every run under `## COMPLETED FROM THE QUEUE`, the wave lists, the write-early protocol, the claim-at-dispatch rule, the FOLD. Append-only; search by ticker; count the register from the file |

**Status words used below, one meaning each.** GOVERNING = listed in `DOCS` in `tools/check_framework.py`
and nothing else. INCORPORATED BY REFERENCE = cited by a governing document, not in `DOCS`. LIVE = read or
written by the current process. GENERATED = a tool's output. HISTORY = a record kept under operator rule 6,
never edited. ARCHIVE = superseded, kept as the audit trail. DEAD = code with no live input. OFF-SHELF = a
corpus folder PRIME RULE 4 does not admit.

---
## THE MAP

### Framework/
| Path | What it is | Status |
|---|---|---|
| `Framework/OPERATOR-PROTOCOL.md` | operator protocol, prime rules, tools test, sovereign sources, the standard | GOVERNING |
| `Framework/THE FRAMEWORK v4.md` | the purchase framework. Four verdicts: IN · OUT · UNRESEARCHED · UNKNOWABLE. Six questions, stop at the first not IN: Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? · Q2 — IS IT A FRANCHISE? · Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? · Q4 — WILL IT SURVIVE? · Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND? · Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL? | GOVERNING |
| `Framework/THE HOLDINGS FRAMEWORK.md` | the framework for positions already owned; outcomes HOLD, SELL REVIEW, SELL, ADDS BARRED | GOVERNING |
| `Framework/SECTOR METHOD - owner earnings for insurers and float-bearing holding companies.md` | insurers and float companies: two components plus a judgment, never an owner-earnings number | GOVERNING |
| `Framework/v4/THE MANAGER STANDARD - Q3.md` | the Q3 manager rules from a full-shelf read; v4 and the run template cite it, the acceptance test does not read it | INCORPORATED BY REFERENCE |
| `Framework/README.md` | which framework document to use | LIVE |
| `Framework/PLAIN ENGLISH - what this is and how it works.md` | the non-technical front door; the governing document wins where they differ | supporting |
| `Framework/INVENTIONS - deleted and why.md` | the numeric rules v4 deleted and what each deletion cost | supporting |
| `Framework/v4/` | the proofs and tests: `Framework/v4/PROOF - tests A, B and C, and what they found.md`, the TEST D pair (preregistration and findings register, closed at zero), `Framework/v4/TEST E - PREREGISTRATION - the loss leg.md`, `Framework/v4/BT-17 - PREREGISTRATION - SP500 replication and the microcap panel.md`, `Framework/v4/VERIFICATION - the two cases that decide the deletions.md` (Citigroup and Coca-Cola, worked), the REGRESSION and RERUN files on the live names, `Framework/v4/RULING CASE 2026-09-20 - two Q2 readings the corpus decides, for the operator's approval.md` (applied the same day), three TOOL TEST admissions, `Framework/v4/testB/` (the sealed blind cases), `Framework/v4/ledger_v4_additions.py` (spent) | test record |
| `Framework/v5/` | **v5, a candidate built by a blind read of the annual meetings, not in force** (started 2026-10-03 at the operator's instruction; v4.1 governs until a ruling case the operator approves): `Framework/v5/CASE 2026-10-03 - v5 from the meetings, for the operator's approval.md` (the PRIME RULE 5 and PRIME RULE 4 case), `Framework/v5/PREREGISTRATION - v5 blind read and comparison.md` (the design, the blind rule, the pass rules, fixed before any transcript was read), `Framework/v5/READING REGISTER.md` (append-only, one entry per unit), `Framework/v5/notes/` (one note per unit). The drafts, the reconciliation and the ruling case are written here when the read is done | candidate, test record |
| `Framework/ARCHIVE - RULINGS 1-14 (resolved into v4, 2026-08-26).md`, `Framework/ARCHIVE - v3.x (superseded 2026-08-26)/`, `Framework/ARCHIVE - May 2026 (superseded)/`, `Framework/CHANGELOG.md` (frozen at v3.0), `Framework/2026-08-26 AUDIT - What Actually Works, and What To Cut.md`, `Framework/2026-08-26 THE FIVE PASSAGES - Synopsis and Rulings.md` | how v4 was reached. Never applied | ARCHIVE |

### The corpus
| Folder | What it is | Status |
|---|---|---|
| `Shareholder Letters/` | Berkshire letters 1965 to 2025, plus `Shareholder Letters/Corporate Genealogy.txt` | shelf |
| `Partnership Letters/` | Buffett Partnership letters 1957 to 1970 | shelf |
| `Wesco Letters (Munger)/` | Wesco letters 1997 to 2009 | shelf |
| `Annual Meetings/` | meeting transcripts 1994 to 2025 | shelf |
| `Munger Talks (PCA)/` | Poor Charlie's Almanack, the eleven talks 1986 to 2007 with front and end matter | shelf |
| `Owners Manual/` | An Owner's Manual | shelf |
| `Fortune Essays (Buffett)/` | Buffett's Fortune essays 1977, 1999 and 2001 | shelf |
| `Special Letters/` | the 2014 fiftieth-anniversary pair | shelf |
| `Annual Reports/`, `Quarterly Reports/` | Berkshire's own annual reports and 10-Qs. The signed chairman's sections of each annual report (Owner-Related Business Principles, Acquisition Criteria, Intrinsic Value, The Managing of Berkshire; printed FY1995 to FY2017) are on the shelf since 2026-10-04 as PRIME RULE 4's ninth class and are cited by the v5 ledger's R-rows; the letter portion is cited through the letters folder; everything else in these files is context only *(this row said "context only; the letter portion is cited through the letters folder \| OFF-SHELF" until 2026-10-04)* | shelf (signed sections) / OFF-SHELF (the rest) |
| `Buffett Pledge Letters/` | the giving-pledge material, context only | OFF-SHELF |
| `Ben Graham/` | a separate Graham side project with its own board, `Ben Graham/GRAHAM BOARD.md`; Graham is off the shelf by PRIME RULE 4 | OFF-SHELF |

Each shelf folder holds one plain-text file per document; four carry a provenance file named _SOURCES.txt
(`Shareholder Letters/_SOURCES.txt`, `Partnership Letters/_SOURCES.txt`, `Munger Talks (PCA)/_SOURCES.txt`,
`Fortune Essays (Buffett)/_SOURCES.txt`). Quotes are stored as extracted; OCR and transcript artifacts are
flagged, never smoothed (PRIME RULE 1).

### Root evidence and state
| Path | What it is | Status |
|---|---|---|
| `principle_ledger.csv` | the evidence base: one verbatim passage per row with year and source file; every `[Ex-nn]` in a governing document resolves to a row here; check 4 reads every row against its source on every run. Count it from the file, never from a pointer; this map carries no count on purpose | LIVE |
| principle_ledger_v5.csv | the v5 blind-read ledger (2026-10-03): the same first eight columns plus speaker, kind, heading and unit; ids M, L and R by source folder; rows enter only through `tools/v5_ledger.py`, which matches each quote against its source before appending; checks 3 and 4 of the acceptance test read it whenever it exists. Not cited by any governing document | LIVE, candidate evidence |
| PORTFOLIO.md | holdings, standing lines, the ranked opportunity set, reviews owed | LIVE |
| `README.md` | the human front door to the repository | LIVE |
| `Framework/ARCHIVE - May 2026 (superseded)/claims_audit.csv` | the audit of the May 2026 edition's claims (at the root until 2026-09-26; every VERIFIED row re-verified against the shelf that day) | HISTORY |
| `Framework/ARCHIVE - v3.x (superseded 2026-08-26)/corpus_map.md` | file-by-file inventory of the corpus with shelf labels and word counts; its corpus rows still match the disk, its framework section describes v3 (at the root until 2026-09-26) | HISTORY |
| `Framework/ARCHIVE - v3.x (superseded 2026-08-26)/owners_manual_map.md` | the Owner's Manual principles mapped against the v3 gates; its quotes verify against the manual (at the root until 2026-09-26) | HISTORY |
| `Framework/2026-09-26 AUDIT - the seven root files.md` | what the root files said and what the files they describe say, checked one against the other | record |

### Test Runs/
| Path or pattern | What it is | Status |
|---|---|---|
| `Test Runs/_TEMPLATE - Company Run.md` | the run surface for a purchase; its self-audit is the enforcement surface (operator rule 1) | GOVERNING |
| `Test Runs/_TEMPLATE - Holding Review.md` | the review surface for a holding | GOVERNING |
| `<date> Run - <TICKER> <name>.md` | one company run each; a run dated before 2026-08-28 is pre-v4.1 and binds nothing | record |
| `_research <date> <TICKER>/` | the research folder of a run; raw filings are gitignored | record |
| `ADDENDUM <date> - <title>.md` | a correction filed after the fact, the operator-rule-6 mechanism; a run file is never edited | record |
| `Test Runs/2026-09-21 RE-LOOK - CRM Salesforce at the first level.md`, `Test Runs/2026-09-18 Q2 FRANCHISE TEST - NCLTY Nitori.md` | the pre-committed re-look at a first level, and a single-question test | record |
| `Test Runs/README - which run files are in force.md` | the rule: a run binds if dated 2026-08-28 or later AND named in the register. Its lists stop at 2026-09-20; where it and the register disagree, the register wins | supporting |
| `Test Runs/_ARCHIVE - Company Run TEMPLATE v3.0 (superseded 2026-08-26).md`, `Test Runs/_ARCHIVE - Company Run TEMPLATE v3.1 (superseded 2026-08-26).md` | the v3 templates | ARCHIVE |

### Screens/
| Path | What it is | Status |
|---|---|---|
| `Screens/WATCHLIST RUN QUEUE.md` | the register and the working rules (see READ FIRST) | LIVE |
| `Screens/SURVIVAL SHAPES - index.md` | the named ways a business dies, each line citing its ledger rows; every run names a shape and new shapes are added at fold | LIVE |
| `Screens/RESUME STATE 2026-09-12 - Opus session, note for Fable.md` | the session-state file (see READ FIRST); `Screens/RESUME STATE 2026-09-02 - four runs killed at the session limit.md` is its predecessor | LIVE / HISTORY |
| `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv` | the screen row every brief carries: owner earnings, deal note, SBC, level shifts | LIVE |
| `Screens/2026-08-31 PREPPED READING LIST (operator lists).md` | the narrative fold of every run; append-only, search by ticker | LIVE |
| `Screens/_input/` | the operator's three lists (`Screens/_input/list_largecap.csv`, `Screens/_input/list_midcap.csv`, `Screens/_input/list_smallcap.csv`), the source of wave 7 | LIVE |
| `Screens/cover_shares.py` | share count by class from the filed cover page; required by every run | LIVE |
| `Screens/floor_screen.py` | owner earnings and the floor arithmetic, used as a library by `tools/run.py` | LIVE |
| `Screens/queue.py`, `Screens/regen_queue.py` | the old queue manager and its regenerator; their state file no longer exists | DEAD |
| `Screens/sourcing_sweep.py`, `Screens/dividend_lens.py`, `Screens/prep_lists.py`, `Screens/new_candidates.py`, `Screens/cover_audit.py`, `Screens/shares_staleness.py`, `Screens/dividend_integrity.py` | one-shot generators; their dated CSVs and reading lists sit beside them | GENERATED |
| the 2026-07-15, 2026-07-16 and 2026-07-17 mechanical screens and source lists, `Screens/GLOBAL QUALITY WATCHLIST v0.1.md`, `Screens/SURVIVORS - Non-Bank Candidates Awaiting Full Gate Run.md`, `Screens/_mq.txt` | the v3-era screens | HISTORY |

### tools/
| Path | What it is | Status |
|---|---|---|
| `tools/check_framework.py` | the acceptance test, six checks: phantom ids, unlabelled numbers, ledger integrity, ledger verbatim, phantom ids across every run file, every path in a pointer file exists. Must PASS before any commit touching a governing document, the ledger, a run file or this map | LIVE |
| `tools/ledger_verbatim.py`, `tools/shelf_damage.csv` | the verbatim check and its exception register (live even when empty) | LIVE |
| `tools/sources.py` | fetch and arithmetic: sovereigns from the issuing authority, SEC facts, prices, split-invariant market cap; caches to `tools/_cache/` (gitignored) | LIVE |
| `tools/run.py` | pre-fills a run file with the arithmetic; judgment fields left blank | LIVE |
| `tools/daily_fetch.py` | the daily digest: sovereign move, new filings from watched names, drift toward alert bands | LIVE, scheduled |
| `tools/price_alerts.py`, `tools/alerts.json` | price bands from the run files. A first level is the top of the value range and means re-look; a second level is the floor price and means it ranks; neither is a buy | LIVE, scheduled |
| `tools/screen.py`, `tools/pit.py` | the wide screen with its currency and unit guards; the point-in-time guard for backtests | supporting |
| `tools/flags.py`, `tools/corpus_index.py` | Q3 flag prompts; shelf retrieval. PARTIALLY ADMITTED, see the TOOL TEST files in `Framework/v4/` | admitted in part |
| `tools/integrity.py` | NOT ADMITTED; kept for one helper function | rejected |
| `tools/resume_ping.py` | a one-off message box | HISTORY |

The tooling test is in the protocol: a tool may get the same number sooner; it may never add a number.

### Automation
| Path or task | What it is | Status |
|---|---|---|
| Windows tasks `BRK-overnight` (hourly), `BRK daily fetch`, `BRK price alerts`, `BRK resume queue`, `BRK-wake` (disabled) | the scheduled work | LIVE |
| `Screens/_daily/_overnight.ps1`, `Screens/_daily/_overnight_prompt.md` | the hourly headless cycle and its instructions; the prompt is the document that explains how the cycle works | LIVE |
| `Screens/_daily/_wave7_order.txt`, `Screens/_daily/_wave7_done.txt` | the current queue and its done file; a name is done when it is in both the register and the done file | LIVE |
| _overnight.lock in `Screens/_daily/` | the lock, present only while a session holds it: an interactive holder is honoured while fresh under 75 minutes; a headless holder needs a live PID under 180 minutes; a cycle releases only the lock it wrote. An interactive session running a name writes this lock first | LIVE, gitignored |
| `Screens/_daily/OVERNIGHT LOG.md` | one line per name: price, pass or fail, commit | LIVE |
| `Screens/_daily/_overnight_logs/` | one log per cycle | GENERATED, gitignored |
| `Screens/_daily/<date> daily.md` | the daily digest output | GENERATED |
| `Screens/_daily/WATCHLIST COMPLETE.md` | the note written when the watchlist closed, with the overnight audit and its closure block | HISTORY |
| LISTS COMPLETE.md in `Screens/_daily/` | written by the cycle when the order file is exhausted; does not exist until then | not yet |
| Windows task `BRK-v5-read` (hourly) | the v5 blind read of the annual meetings, one meeting session per cycle (2026-10-03). Shares the lock above with `BRK-overnight`, so the two never run together; `BRK-overnight` stays disabled while it reads | LIVE |
| Windows task `BRK-v5-alert` (every 30 minutes), `tools/v5_alert.py` | a message box to the operator when V5 READ COMPLETE.md appears in `Screens/_daily/`; fires once and disables itself (operator instruction 2026-10-03, local only) | LIVE until it fires |
| `Screens/_daily/_v5_read.ps1`, `Screens/_daily/_v5_read_prompt.md` | the v5 cycle and its instructions: the whitelist blind rule, the five kinds of lesson, the row, the write-early order, the close. The prompt is the document that explains how the cycle works; the design it serves is `Framework/v5/PREREGISTRATION - v5 blind read and comparison.md` | LIVE |
| `Screens/_daily/_v5_order.txt`, `Screens/_daily/_v5_done.txt` | the units of the read (`key | transcript | session heading | letter | report`) and the done file; a unit is done when its key is in the done file and the helper's status command shows its rows and note | LIVE |
| V5 READ LOG.md in `Screens/_daily/` | one line per unit: rows by prefix, verifier result, commit; created by the first cycle | LIVE once created |
| _v5_logs/ in `Screens/_daily/` | one log per v5 cycle and its own scheduler trace; created by the first cycle | GENERATED, gitignored |
| V5 READ COMPLETE.md in `Screens/_daily/` | written by the cycle when the order file is exhausted; does not exist until then | not yet |
| `tools/v5_ledger.py` | the only way rows enter the v5 ledger: validate, match the quote against its source with `tools/ledger_verbatim.py`'s matcher, refuse a failing batch, assign the id, append with csv.writer; also `unit`, `status`, `count`, `verify`. Same number sooner, no number added | LIVE |

### Backtests/
No README. Everything is HISTORY except the honest record, which operator rule 7 states: the BT-15, BT-16,
BT-17 and TEST-E outputs, written up in `README.md` (the withdrawn-backtest section) and in
`Framework/v4/PROOF - tests A, B and C, and what they found.md`, the BT-17 preregistration and the TEST E
preregistration. `Backtests/scripts/bt17_microcap.py` is LIVE as a shared library. `Backtests/gate_timelines/`
was never written up. `Backtests/bt17_cache/` is gitignored.

---
## HOW WORK MOVES
- **Run a company**: read the protocol; write the lock; copy the company template to a dated file before any fetch; write each question as it closes; commit after each; then the six-step FOLD in the register file.
- **Review a holding**: copy the holding template; run H1 to H5 under the holdings framework; an add is a purchase and runs v4.
- **Change a rule**: a written case with quotes first (PRIME RULE 5); the ledger row before the rule (PRIME RULE 6); `tools/check_framework.py` PASS before the commit.
- **Resume the queue**: the last section of the session-state file, then the register's WAVE section, then the lock.
- **Close a session**: append a dated section to the session-state file; update the memory files that live outside this tree; commit with a pathspec.

## RULES OF THIS MAP
- **No counts.** A count belongs to the file that has it. This file is read by the acceptance test, so a number in its prose fails the build.
- **Full paths, no ellipsis.** The acceptance test's check 6 opens every path in this file and fails on one that does not exist.
- **A stale pointer is corrected the day it is found**, with a dated note saying what it said before.
- **History is never edited** (operator rule 6). A record is corrected by an addendum.

## FOLDER NOTE
Working folder is /BRK (referred to as /Long-Term Business Analysis in some older run
files and commits from 2026-07-17; the same folder).
