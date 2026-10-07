# BRIEF - SMCI (Super Micro Computer, Inc.), wave 5, overnight cycle 2026-09-18 ~14:40 EDT

You are running ONE company through the framework, from scratch, unattended. The operator is asleep and nobody will
answer a question. Repository: `C:\Users\chreh\OneDrive\Documents\BRK`. Work in it directly.

## 0. READ FIRST (in this order)
1. `CLAUDE.md` (operator protocol, prime rules, tools).
2. `Framework/THE FRAMEWORK v4.md` - the governing document. If a rule is not in it, it is not in force.
3. `Test Runs/_TEMPLATE - Company Run.md` - the run surface.
4. For what a finished run looks like: `Test Runs/2026-09-18 Run - DLR Digital Realty.md` and
   `Test Runs/2026-09-12 Run - BA Boeing.md`. Read their structure, self-audit and REGISTER block.
5. `Screens/WATCHLIST RUN QUEUE.md`: the sections `THE WRITE-EARLY PROTOCOL`, `THE FOLD`, `WRITING A BRIEF`, the
   `#### WAVE 5` table and its dated notes, and the top two entries of `## COMPLETED FROM THE QUEUE` (the format).
6. `Screens/SURVIVAL SHAPES - index.md` - name survival shapes by their number; add a new one there only when folding.
7. `Screens/RESUME STATE 2026-09-12 - Opus session, note for Fable.md` sections 3-5: tooling changes, errors not to
   repeat, and nine source limits already tested (do not re-attempt them).

## 1. THE NAME, AND WHY IT IS HERE
- Ticker SMCI, Super Micro Computer, Inc., CIK 0001375365, Delaware, fiscal year ends June 30. 10-K/10-Q filer.
- **No screen row exists** in `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv` (checked by this cycle).
- **Skip reason from the wave 5 table, a prompt to read and never a verdict:** *"perimeter or restatement above
  threshold: read the filing first"* (the skipped-reason list adds: *"revenue step or cross-accession restatement
  above threshold"*). Your job at Step 0 is to find out WHAT that flag was reacting to, on the filings, and say so.

## 2. WHAT THE CURRENT SCREEN RETURNS (tagged data, transcription only; operator rule 4)
This cycle pulled companyfacts fresh at ~14:45 EDT 2026-09-18 and ran the current `Screens/floor_screen.py`
functions over it. Script: `Test Runs/_research 2026-09-18 SMCI/_probe_screen.py`; output:
`_probe_screen_output.txt` in the same folder; the raw pull is `companyfacts.json` there (do not refetch it unless
you need a newer vintage). **Every figure below is a prompt to read the filed statement, not a finding:**
- `restatement_shift` -> `(1.0, 2018-06-30)`; `scale_shift` -> 2.10; `share_count_shift` -> 11.2.
- `owner_earnings()` -> 5y D&A end -$1,730M, 5y capex end -$1,794M, 3y D&A end -$2,906M, 3y capex end -$3,003M.
- Tagged operating cash (`ocf_continuing`), by fiscal year: FY2022 -$440.8M, FY2023 +$663.6M, FY2024 -$2,486.0M,
  FY2025 +$1,659.5M, **FY2026 -$6,809.9M**. The screen's `working_capital_flag` returned None on this series. Read
  the FY2026 10-K cash-flow statement and working-capital lines before believing or using any of these.
- Tagged capex: FY2024 $124.3M, FY2025 $127.2M, FY2026 $162.0M. Tagged SBC: FY2023 $54.4M, FY2024 $231.5M, FY2025
  $314.5M, FY2026 $412.1M. Tagged D&A FY2026 $53.0M. `stale_filer` says the newest annual period is 2026-06-30.
- `shares_outstanding()` -> 656,965,384 dated 2026-07-31 (a dei cover fact). Confirm on the cover yourself.
- `acquisition_flag` -> $2.5M, nothing material.
The questions these raise are yours to answer: which fiscal years were restated and why; whether the 11.2x share
shift is a split (and, if so, that every per-share and share figure is on one basis); what the FY2026 operating-cash
figure is made of; whether SBC resolves AND is complete (see section 4).

## 3. THINGS I BELIEVE FROM MEMORY - UNVERIFIED. Verify each on a filing or discard it; never carry one forward
My knowledge cutoff predates the newest filings, and a prior brief of mine was caught quoting a price increase that
appeared in no filing (ELF). Treat each of these as a hypothesis to test, with the document that would settle it:
- A restatement of roughly FY2015-FY2017 results, with delayed 10-Ks around 2017-2019 and a Nasdaq delisting episode
  (settle on the restated 10-K for FY2017/FY2019 and the related 8-Ks).
- An SEC settled order around August 2020 on revenue recognition and related matters, naming the company and a
  former CFO; a clawback from the CEO (settle on the SEC order itself, via EDGAR or sec.gov litigation releases).
- In 2024: a short-seller report, a delayed FY2024 10-K, the resignation of the auditor (Ernst & Young) in late 2024
  with a letter stating concerns, a special committee of the board, and a new auditor (BDO); a DOJ and/or SEC
  inquiry. (Settle on the 8-K Item 4.01 and its Exhibit 16 letter, the special committee 8-K, the FY2024 10-K's
  risk factors and legal proceedings, and the latest 10-K/10-Q legal note for what is still open.)
- A 10-for-1 forward split in 2024 (settle on the 8-K and the equity note).
- Related-party purchases from entities connected to the founder's family (Ablecom, Compuware) (settle on the 10-K
  related-party note and the proxy).
- A 2026 indictment or export-control matter involving individuals connected to the company. I am genuinely unsure
  of this one; check the 8-Ks and legal proceedings for 2025-2026 and record what the filings say, or that they say
  nothing.
Date each matter to when it became PUBLIC, as the DLR run did.

## 4. REQUIRED HANDLING (the project's standing rules; none of them is a hint about a verdict)
- **Write-early.** Copy the template to `Test Runs/2026-09-18 Run - SMCI Super Micro Computer.md` BEFORE fetching
  anything, commit it, then write each section as it closes and commit after every gate. Research files go in
  `Test Runs/_research 2026-09-18 SMCI/`. **COMMIT WITH A PATHSPEC ONLY: write the message to a file and use
  `git commit -F <msgfile> -- <path> <path>`.** Never `git add X && git commit` (it commits the whole shared index and
  has swept other sessions' files into wrong commits six times). `git add` a NEW file before the pathspec commit so it
  is tracked, then commit with the pathspec. Bash heredocs containing apostrophes fail in this environment: write
  scripts to the research folder. Commit trailer: `Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>`.
- **Sovereign**: strike it yourself from the US Treasury daily par yield curve, 30-year, dated
  (`python tools/sources.py` or the Treasury site; FRED DGS30 only as fallback). The last run used 5.29% (09/17/2026);
  do not inherit it.
- **Price**: re-strike it yourself; aggregators are allowed for live quotes only and are flagged. Note from recent runs:
  `tools/sources.price()` returns an intraday price stamped with today's date although its docstring says "latest
  close"; use a dated close and say which. Cross-check against a Form 4 price if one is recent.
- **Share count**: from the cover of the LATEST periodic filing (`python Screens/cover_shares.py SMCI`), with the
  accession. Never sum share classes without reading the charter.
- **SBC**: verify it RESOLVES and is COMPLETE on the face of the cash-flow statement for every year you use (BE's did
  not resolve and the screen subtracted zero; Boeing's resolved under a tag no SBC element contains). Where SBC/OCF
  is high, [E3-70] asks what the options could have been sold for; the grant table is read by hand (source limit).
- **Deal check**: query EDGAR yourself for any live merger, tender or going-private (8-K Items 1.01/2.01, SC TO, S-4,
  DEFM14A). A live deal makes the quote a spread, not an owner-earnings price (ROKU).
- **Owner earnings**: rebuild the width over every window (3y, 5y, 10y, and TTM if you use it) and both (c) ends,
  from the filed statements, never a net-income proxy. Report dollars, and a word, wherever the bottom sits near or
  below zero. Ask what the D&A is made of before assuming the (c) band is about plant, and ask [E5-20] on the filing.
- **Hard sequence Q1 to Q5. STOP at the first question that is not IN.** UNRESEARCHED and UNKNOWABLE both close the
  file. The recent runs have recorded the later questions beneath a close under an explicit "RECORDED, NOT GOVERNING"
  banner; that is allowed, but no such section may carry entry language, and any valuation before Q1-Q4 all close IN
  is headed exactly `COMPUTATION — NOT A CLEARANCE`.
- **Q3**: pull the latest 8-K EX-99.1 earnings releases before scoring [E4-29] and [E4-22]'s flags (the CGNX
  companion rule). The honesty binary is [E5-16]; the incentive read is [E4-27] (NOT [E4-52], which is the
  lollapalooza row, the converging-flags reading); [E5-22] is penalty size is not seriousness; [E4-34] is the four
  auditor questions; [E2-26] is candor.
- **Q2**: a moat is a relative claim; the competitor row [E3-28] is required, from competitors' own filings (full-text
  search via `tools/sources.py fts_count()` needs the bare zero-padded 10-digit CIK or it silently returns zero).
  [E3-03] is the franchise definition; [E2-44] the pricing-power and low-capital pair; [E4-04] the rapid-change
  exclusion; [E3-46] return on capital as the second question about the business; [E2-45] the grizzlies question;
  [E2-58] the cost-advantage exception; [E2-59] commodity product plus over-capacity; [E3-62] who keeps the gains.
- The TSMC corpus tension against [E4-04] (the 2023 meeting) is an OPEN operator question; if [E4-04] matters here,
  apply v4 as written and note the tension, do not resolve it.
- **Prior material on disk about this company, read as UNLABELLED evidence, not as a conclusion**: the DELL run
  (see `Screens/2026-08-31 PREPPED READING LIST (operator lists).md` around line 5100, and the DELL register entry in
  `Screens/WATCHLIST RUN QUEUE.md` around line 3590) used Super Micro's filings as a competitor row. Its figures were
  computed for Dell's question; recompute anything you use from SMCI's own filings.
- Every ledger id you cite must exist in `principle_ledger.csv` and say what you cite it for (check it; the acceptance
  test cannot catch a real id cited for the wrong thing).
- No em dashes in your own prose (verbatim quotes and the required `COMPUTATION — NOT A CLEARANCE` heading excepted).
- Nothing about the framework changes: no ledger rows, no edits under `Framework/`. Corrections go in dated notes.
- Never present the framework as proven to beat the market (operator rule 7).

## 5. THE FOLD - do all six steps yourself (queue file, `## THE FOLD`)
1. Register entry at the TOP of `## COMPLETED FROM THE QUEUE` in `Screens/WATCHLIST RUN QUEUE.md`, in the same form as
   the DLR entry: price, share count and cover accession, cap, sovereign, and the PASS/FAIL line naming the question
   that closed the file. Count the register from its heading line (not the first occurrence of the phrase) and state
   the new total.
2. Strike SMCI in the wave 5 table (`~~SMCI~~`), and add a short dated note beside the table on what the "perimeter or
   restatement" label turned out to be for SMCI (the capex row's notes are the model; do not edit history).
3. Narrative fold into `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`.
4. `tools/alerts.json` bands and a `PORTFOLIO.md` row ONLY if all four business gates clear. If the file closes at
   Q1-Q4, record the reversal condition in words instead.
5. `python tools/check_framework.py` must PASS before the fold commit.
6. Pathspec commit.
Also add a new survival shape to `Screens/SURVIVAL SHAPES - index.md` only if you name one.

## 6. WHAT TO RETURN TO ME
A short report: the verdict line (which question closed the file and on which ledger ids); price with date and source;
share count with accession; cap; sovereign with date; the owner-earnings range; what the skip reason turned out to be;
the register count after your entry; check_framework result; the commit hashes; and every defect you found in this
brief. If you hit a usage or rate limit, commit whatever is on disk with a pathspec commit and say exactly where you
stopped.
