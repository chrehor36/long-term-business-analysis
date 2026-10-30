# BRIEF - RIVN (Rivian Automotive, Inc.), wave 5, overnight cycle 2026-09-18 ~19:15 EDT

You are running ONE company through the framework, from scratch, unattended. The operator is asleep and nobody will
answer a question. Repository: `C:\Users\chreh\OneDrive\Documents\BRK`. Work in it directly.

## 0. READ FIRST (in this order)
1. `CLAUDE.md` (operator protocol, prime rules, tools).
2. `Framework/THE FRAMEWORK v4.md` - the governing document. If a rule is not in it, it is not in force.
3. `Test Runs/_TEMPLATE - Company Run.md` - the run surface.
4. For what a finished run looks like: `Test Runs/2026-09-18 Run - TSLA Tesla.md` (the previous name in this same wave 5
   row, finished about an hour ago, and an automaker) and `Test Runs/2026-09-18 Run - SNOW Snowflake.md`. Read their
   structure, self-audit, brief-defects section and REGISTER block. The TSLA run built an automaker competitor row from
   filers' own statements; its figures were computed for Tesla's question, so recompute anything you use from the
   filings themselves and read it as UNLABELLED evidence, not a conclusion.
5. `Screens/WATCHLIST RUN QUEUE.md`: the sections `THE WRITE-EARLY PROTOCOL`, `THE FOLD`, `WRITING A BRIEF`, the
   `#### WAVE 5` table and ALL its dated notes (the SMCI, SNOW and TSLA notes are the ones for your row), and the top two
   entries of `## COMPLETED FROM THE QUEUE` (the format).
6. `Screens/SURVIVAL SHAPES - index.md` - name survival shapes by their number; add a new one there only when folding.
7. `Screens/RESUME STATE 2026-09-12 - Opus session, note for Fable.md` sections 3-5: tooling changes, errors not to
   repeat, and the source limits already tested (do not re-attempt them).

## 1. THE NAME, AND WHY IT IS HERE
- Ticker RIVN, Rivian Automotive, Inc., CIK 0001874178, Delaware, fiscal year = calendar year. 10-K/10-Q filer.
  Newest annual in companyfacts FY2025 (10-K filed 2026-02-12 per the dei public-float fact); the screen's newest share
  fact is dated 2026-06-30, so a Q2 2026 10-Q exists - confirm the latest periodic filing from `submissions.json`.
- **No screen row exists** in `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv` (grepped by this cycle).
- **Skip reason from the wave 5 table, a prompt to read and never a verdict:** *"perimeter or restatement above
  threshold: read the filing first"* (the skipped-reason list adds: *"revenue step or cross-accession restatement
  above threshold"*). The SMCI, SNOW and TSLA notes ask that each remaining name in this row be reproduced against the
  `a8bc84f` guards; this cycle did (section 2). **Find out on the filings what the flag was reacting to and say so**,
  remembering the TSLA note's instruction that a `scale_shift` above 2.0 be checked for non-consecutive years before it
  is read as a step, and the SNOW note's finding that `restatement_shift` is not called by the triage pipeline.

## 2. WHAT THE SCREEN RETURNS (tagged data, transcription only; operator rule 4)
This cycle pulled companyfacts fresh at ~19:12 EDT 2026-09-18. Scripts `_probe_screen.py` and `triage_repro.py` (adapted
from SNOW's), outputs `_probe_screen_output.txt` and `triage_repro_out.txt`, raw pull `companyfacts.json`, and the triage
code copy `floor_screen_a8bc84f.py`, all in `Test Runs/_research 2026-09-18 RIVN/` (do not refetch companyfacts unless
you need a newer vintage). **Every figure is a prompt to read the filed statement, not a finding:**
- **a8bc84f guard order on facts filed by 2026-09-01:** `share_count_shift` returned **None** (passes, but a None means
  it found nothing to compare, not that the count is stable); `scale_shift` **30.15** (FIRES); `filed_years` 7;
  `owner_earnings` 5y D&A end -$4,489M, 5y capex end -$5,195M; `restatement_shift` (1.0, FY2021), a null (not a guard).
- Tagged revenue ($M), all under `RevenueFromContractWithCustomerExcludingAssessedTax` (no other revenue element carries
  annual data): FY2019 0, FY2020 0, FY2021 55, FY2022 1,658, FY2023 4,434, FY2024 4,970, FY2025 5,387. Steps:
  FY2021-22 30.15x, FY2022-23 2.67x, FY2023-24 1.12x, FY2024-25 1.08x.
- **Current screen:** `owner_earnings()` 5y D&A end -$4,489M, 5y capex end -$5,195M, 3y D&A end -$4,122M, 3y capex end
  -$4,527M. `share_count_shift` None with and without ticker. `acquisition_flag` None. `stale_filer` newest annual
  2025-12-31.
- `working_capital_flag` FIRES: *"ONE LINE MADE THE CASH: ContractWithCustomerLiability moved 94% of 2024 OCF"*.
- `da_discontinuity_flag` FIRES: D&A steps 6.8x at FY2021 ($29M to $197M); read the cash-flow statement and Note 1
  before using either end of (c).
- Tagged operating cash ($M): FY2019 -353, FY2020 -848, FY2021 -2,622, FY2022 -5,052, FY2023 -4,866, FY2024 -1,716,
  FY2025 -779.
- Tagged SBC ($M): FY2019 **0**, FY2020 **0**, FY2021 570, FY2022 987, FY2023 821, FY2024 692, FY2025 741 (the zeros may
  be the SBC-of-zero defect the RESUME STATE note describes; check the face).
- Tagged D&A ($M): FY2019 7, FY2020 29, FY2021 197, FY2022 652, FY2023 937, FY2024 1,031, FY2025 784.
- Tagged capex ($M): FY2019 199, FY2020 914, FY2021 1,794, FY2022 1,369, FY2023 1,026, FY2024 1,141, FY2025 1,710.
  `capital_acquired()` adds non-cash additions of $80M (FY2023), $6M (FY2024), $2M (FY2025).
- **companyfacts carries NO dei share-count element** (only `EntityPublicFloat`); the screen's `shares_outstanding()`
  returned 1,362,000,000 dated 2026-06-30 from a non-dei element. Read the cover yourself; there may be more than one
  class (read the charter before summing any classes).
The questions these raise are yours to answer: what the 30x and 2.7x revenue steps are made of (start of production,
perimeter, or both); whether any restatement exists; what the contract-liability line was and whether it is customer
float in the [E3-52] sense; whether SBC resolves AND is complete on the face every year; what the D&A is made of and why it
fell in FY2025; and what the capex buys.

## 3. THINGS I BELIEVE FROM MEMORY - UNVERIFIED. Verify each on a filing or discard it; never carry one forward
My knowledge has a cutoff that predates the newest filings, and a past brief of mine quoted a price increase that
appeared in no filing (ELF). Each is a hypothesis with the document that would settle it:
- IPO November 2021 (settle on the 424B4); pre-IPO years only in the S-1.
- Class A and Class B common stock, Class B with super-voting rights held by the founder (settle on the charter and the
  10-Q cover).
- Amazon is a large shareholder and the launch customer for electric delivery vans, with an exclusivity arrangement that
  later lapsed (settle on the 10-K customer-concentration disclosure, related-party note and 13D/13G filings).
- A joint venture with Volkswagen Group announced June 2024 for electrical architecture and software, with staged
  investments of up to about $5.8bn in equity and loans (settle on the 8-Ks, the JV/equity-method note, and the share
  count effect of any VW convertible note or share purchase).
- A U.S. Department of Energy loan (about $6.6bn conditional, for the Georgia plant) (settle on the 8-K and debt note:
  closed or conditional, drawn or undrawn, and what the current status is).
- Regulatory credit sales are a material part of gross profit; gross profit turned positive around Q4 2024 (settle on
  the revenue disaggregation and MD&A).
- R2, a smaller vehicle, scheduled to start production in 2026 at Normal, Illinois (settle on the 10-Q and releases).
- Securities class actions concerning the IPO disclosures (settle on legal proceedings: filed, settled, open, amounts).
- Founder-CEO R.J. Scaringe; a large CEO performance award (settle on the proxy: what it vests on).
- The company headlines adjusted EBITDA and "gross profit" milestones in its releases (settle on the 8-K EX-99.1
  earnings releases before scoring [E4-29] and [E4-22]).
Date each matter to when it became PUBLIC.

## 4. REQUIRED HANDLING (the project's standing rules; none of them is a hint about a verdict)
- **Write-early.** Copy the template to `Test Runs/2026-09-18 Run - RIVN Rivian.md` BEFORE fetching anything, commit it,
  then write each section as it closes and commit after every gate. Research files go in
  `Test Runs/_research 2026-09-18 RIVN/`. **COMMIT WITH A PATHSPEC ONLY: write the message to a file and use
  `git commit -F <msgfile> -- <path> <path>`.** Never `git add X && git commit` (it commits the whole shared index and has
  swept other sessions' files into wrong commits six times). `git add` a NEW file before the pathspec commit so it is
  tracked, then commit with the pathspec. Bash heredocs containing apostrophes fail in this environment: write scripts to
  the research folder. Commit trailer: `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. Also commit this brief,
  the two probe scripts and their outputs into the research folder with your first commit (the companyfacts.json only if
  the research ignore rules allow it; check `.gitignore`). **Do not commit image files** (the TSLA run committed 33 slide
  JPGs because `.gitignore` does not cover `.jpg`).
- **Sovereign**: strike it yourself from the US Treasury daily par yield curve, 30-year, dated
  (`python tools/sources.py` or the Treasury site; FRED DGS30 only as fallback). The last run recorded 5.34% on
  2026-09-18; do not inherit it.
- **Price**: re-strike it yourself; aggregators are allowed for live quotes only and are flagged.
  `tools/sources.price()` returns an intraday price stamped with today's date although its docstring says "latest close"
  (several runs have recorded this); use a dated close and say which. Cross-check against a Form 4 price if one is recent.
- **Share count**: from the cover of the LATEST periodic filing (`python Screens/cover_shares.py RIVN`, and read the cover
  itself, since companyfacts has no dei count), with the accession. Never sum share classes without reading the charter.
  Consider whether any convertible notes, the VW instruments (if they exist) or unearned award shares belong in the count
  at the price you strike, and state the answer either way.
- **SBC**: verify it RESOLVES and is COMPLETE on the face of the cash-flow statement for every year you use. Where SBC/OCF
  is high, [E3-70] asks what the options could have been sold for; the grant table is read by hand (source limit).
- **Deal check**: query EDGAR yourself for any live merger, tender or going-private (8-K Items 1.01/2.01, SC TO, S-4,
  DEFM14A, SC 13D). A live deal makes the quote a spread, not an owner-earnings price (ROKU).
- **Owner earnings**: rebuild the width over every window (3y, 5y, and TTM if you use it; a 10-year window does not exist
  on filed statements for a 2021 IPO, so say so) and both (c) ends, from the filed statements, never a net-income proxy.
  Report dollars, and a word, wherever the bottom sits near or below zero. Ask what the D&A is made of before assuming the
  (c) band is about plant, and ask [E5-20] on the filing. Show the contract-liability contribution to operating cash
  explicitly, both ways.
- **Hard sequence Q1 to Q5. STOP at the first question that is not IN.** UNRESEARCHED and UNKNOWABLE both close the file.
  Recent runs recorded later questions beneath a close under an explicit "RECORDED, NOT GOVERNING" banner; that is
  allowed, but no such section may carry entry language, and any valuation before Q1-Q4 all close IN is headed exactly
  `COMPUTATION — NOT A CLEARANCE`.
- **Q3**: pull the latest 8-K EX-99.1 earnings releases before scoring [E4-29] and [E4-22]'s flags (the CGNX companion
  rule). The honesty binary is [E5-16]; the incentive read is [E4-27] (NOT [E4-52], which is the lollapalooza row);
  [E5-22] is penalty size is not seriousness; [E4-34] is the four auditor questions; [E2-26] is candor. Read the proxy
  for what pay vests on.
- **Q2**: a moat is a relative claim. The same-metric competitor row is a CONVENTION the framework keeps (the corpus's
  own test is pricing conduct plus returns on capital [E3-43]; [E3-28] is the monitoring quote, not the row's authority).
  Build it from competitors' own filings (full-text search via `tools/sources.py fts_count()` needs the bare zero-padded
  10-digit CIK or it silently returns zero). [E3-03] is the franchise definition; [E2-44] the pricing-power and
  low-capital pair; [E4-04] the rapid-change exclusion; [E3-46] return on capital; [E2-45] the grizzlies question; [E2-58]
  the cost-advantage exception; [E2-59] commodity product plus over-capacity; [E3-62] who keeps the gains; [E4-37] the
  price-rise test; [E4-23] key-person dependence.
- The TSMC corpus tension against [E4-04] (the 2023 meeting) is an OPEN operator question; if [E4-04] matters here,
  apply v4 as written and note the tension, do not resolve it.
- Every ledger id you cite must exist in `principle_ledger.csv` and say what you cite it for (check it; the acceptance
  test cannot catch a real id cited for the wrong thing).
- No em dashes in your own prose (verbatim quotes and the required `COMPUTATION — NOT A CLEARANCE` heading excepted).
- Nothing about the framework changes: no ledger rows, no edits under `Framework/`. Corrections go in dated notes.
- Never present the framework as proven to beat the market (operator rule 7).

## 5. THE FOLD - do all six steps yourself (queue file, `## THE FOLD`)
1. Register entry at the TOP of `## COMPLETED FROM THE QUEUE` in `Screens/WATCHLIST RUN QUEUE.md`, in the same form as
   the TSLA entry: price, share count and cover accession, cap, sovereign, and the PASS/FAIL line naming the question
   that closed the file. Count the register from its heading line (entries beginning `- **TICKER (` under
   `## COMPLETED FROM THE QUEUE`, stopping at the next `##`/`###` heading; TSLA's fold said 104) and state the new total.
2. Strike RIVN in the wave 5 table (`~~RIVN~~`), and add a short dated note beside the table on what the "perimeter or
   restatement" label turned out to be for RIVN (the TSLA note is the model; do not edit history).
3. Narrative fold into `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`.
4. `tools/alerts.json` bands and a `PORTFOLIO.md` row ONLY if all four business gates clear. If the file closes at Q1-Q4,
   record the reversal condition in words instead.
5. `python tools/check_framework.py` must PASS before the fold commit.
6. Pathspec commit.
Also add a new survival shape to `Screens/SURVIVAL SHAPES - index.md` only if you name one.

## 6. WHAT TO RETURN TO ME
A short report: the verdict line (which question closed the file and on which ledger ids); price with date and source;
share count with accession; cap; sovereign with date; the owner-earnings range; what the skip reason turned out to be;
the register count after your entry; check_framework result; the commit hashes; and every defect you found in this brief.
If you hit a usage or rate limit, commit whatever is on disk with a pathspec commit and say exactly where you stopped.
