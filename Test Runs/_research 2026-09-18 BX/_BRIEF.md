# BRIEF - BX (Blackstone Inc.), wave 5, overnight cycle 2026-09-18 ~20:15 EDT

You are running ONE company through the framework, from scratch, unattended. The operator is asleep and nobody will
answer a question. Repository: `C:\Users\chreh\OneDrive\Documents\BRK`. Work in it directly.

## 0. READ FIRST (in this order)
1. `CLAUDE.md` (operator protocol, prime rules, tools).
2. `Framework/THE FRAMEWORK v4.md` - the governing document. If a rule is not in it, it is not in force.
3. `Test Runs/_TEMPLATE - Company Run.md` - the run surface.
4. For what a finished run looks like: `Test Runs/2026-09-18 Run - DJT Trump Media.md` (the previous name in this same
   wave 5 row, finished about twenty minutes before this brief) and `Test Runs/2026-09-13 Run - BAM Brookfield Asset
   Management.md` (an alternative asset manager, closed at Q2 on a nine-peer competitor row that INCLUDES BX figures).
   Read their structure, self-audit, brief-defects section and REGISTER block. Their findings belong to their companies;
   nothing in them is evidence about BX. The BAM row's BX figures are the BAM run's readings of BX's filings: they tell
   you where to look, and every one you use must be re-read on BX's own filing and cited by accession.
5. `Screens/WATCHLIST RUN QUEUE.md`: the sections `THE WRITE-EARLY PROTOCOL`, `THE FOLD`, `WRITING A BRIEF`, the
   `#### WAVE 5` table and ALL its dated notes (the SMCI, SNOW, TSLA, RIVN and DJT notes are the ones for your row), and
   the top two entries of `## COMPLETED FROM THE QUEUE` (the format).
6. `Screens/SURVIVAL SHAPES - index.md` - name survival shapes by their number; add a new one there only when folding.
7. `Screens/RESUME STATE 2026-09-12 - Opus session, note for Fable.md` sections 3-5: tooling changes, errors not to
   repeat, and the source limits already tested (do not re-attempt them).

## 1. THE NAME, AND WHY IT IS HERE
- Ticker BX, Blackstone Inc., **CIK 0001393818** (companyfacts at that CIK returns entityName "Blackstone Inc."; confirm
  against the SEC `company_tickers.json`). Fiscal year = calendar year. 10-K/10-Q filer. dei shows a 10-K filed
  2026-02-27 and 10-Qs filed 2026-05-08 and 2026-08-07. Confirm the latest periodic filing from `submissions.json`.
- **No screen row exists** in `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv` (grepped by this cycle: the only
  "BX" hit is GBX, Greenbrier, which is not this company) or the other Screens CSVs.
- **Skip reason from the wave 5 table, a prompt to read and never a verdict:** *"perimeter or restatement above
  threshold: read the filing first"* (the skipped-reason list adds: *"revenue step or cross-accession restatement above
  threshold"*). **Find out on the filings what the flag was reacting to and say so.** Carry the row's lessons: the TSLA
  note (check a `scale_shift` above 2.0 for non-consecutive years), the SNOW note (`restatement_shift` is not called by
  the triage pipeline), the RIVN note (a `share_count_shift` of None is a missing element), the DJT note (assign each
  tagged year to the right reporting entity from the basis-of-presentation note before using it).

## 2. WHAT THE SCREEN RETURNS (tagged data, transcription only; operator rule 4)
This cycle pulled companyfacts fresh at ~20:10 EDT 2026-09-18. Scripts `_probe_screen.py` and `triage_repro.py`,
outputs `_probe_screen_output.txt` and `triage_repro_out.txt`, raw pull `companyfacts.json`, and the triage code copy
`floor_screen_a8bc84f.py`, all in `Test Runs/_research 2026-09-18 BX/` (do not refetch companyfacts unless you need a
newer vintage). **Every figure is a prompt to read the filed statement, not a finding:**
- **a8bc84f guard order on facts filed by 2026-09-01:** `share_count_shift` **1.040** (passes); `scale_shift` **3.700**
  (FIRES), on FY2020 $6,101.9M to FY2021 $22,577.1M under the `Revenues` element, **consecutive years**, and the next
  step is **0.377** (FY2022 $8,517.7M), then FY2023 $8,022.8M, FY2024 $13,230.0M, FY2025 $14,450.3M. A step that reverses
  the next year is not a perimeter on its face; find what line of the income statement made it. `filed_years` 16;
  `restatement_shift` (1.004, FY2016), a null.
- `owner_earnings` (screen, a8bc84f): 5y D&A end $3,405M, 5y capex end $3,348M; 3y $2,770M / $2,733M. **These are built
  on GAAP operating cash that may include consolidated funds' activity**; the screen cannot tell. Do not use them.
- Tagged operating cash ($M): FY2016 -88.6, FY2017 -1,626.4, FY2018 45.7, FY2019 1,963.1, FY2020 1,935.9, FY2021 3,986.0,
  FY2022 6,336.3, FY2023 4,056.9, FY2024 3,481.7, FY2025 4,663.2 (FY2014-15 absent from the tag series). The swings are a
  prompt to read the cash-flow statement's lines for the consolidated Blackstone Funds.
- Tagged SBC ($M): 2008 3,302.6 ... 2011 1,396.1 ... FY2021 637.4, FY2022 846.3, FY2023 987.5 (later years in the output
  file). Check the face resolves and is complete every year you use.
- Tagged D&A: ~$127-137M FY2021-24. Tagged capex: FY2022 $235.5M, FY2023 $224.2M (later years in the output file).
- `acquisition_flag` $5.4M (immaterial on its face). `working_capital_flag`, `da_discontinuity_flag`,
  `capex_funding_flag`, `lease_capex_flag` all None. `stale_filer` newest annual 2025-12-31.
- dei `EntityCommonStockSharesOutstanding`: 742,180,737 (2026-02-20, 10-K) ... **750,625,114 (2026-07-31, 10-Q filed
  2026-08-07)**. `EntityPublicFloat` $108.9bn (2025-06-30). **The dei count may be one class only**; see section 3.
The questions these raise are yours to answer: what the FY2021 step and FY2022 reversal are made of; what GAAP revenue
contains that is not fee income (performance allocations, unrealized, and principal investment income) and what cash
each part produced; what the consolidated funds put into operating cash; what owner earnings measures for a fee
manager that also carries a balance sheet of GP and co-investments, and on which ledger id; and what the correct share
count is for the price.

## 3. THINGS I BELIEVE FROM MEMORY - UNVERIFIED. Verify each on a filing or discard it; never carry one forward
My knowledge has a cutoff that predates the newest filings, and a past brief of mine quoted a price increase that
appeared in no filing (ELF). Each is a hypothesis with the document that would settle it:
- GAAP revenues include "Performance Allocations" (carried interest, accrued on fund marks, largely unrealized) and
  "Principal Investments" income, so a strong mark year (2021) inflates revenue and a weak one (2022) reverses it
  (settle on the FY2021 and FY2022 10-K income statements and the revenue note).
- Blackstone consolidates certain funds and CLO vehicles ("Consolidated Blackstone Funds"), whose investment activity
  runs through GAAP operating cash (settle on the cash-flow statement and the consolidation / VIE note).
- Blackstone converted from a publicly traded partnership (The Blackstone Group L.P.) to a corporation on 2019-07-01
  and renamed Blackstone Inc. in 2021 (settle on the 8-Ks and the FY2019 10-K); check whether any year you use crosses
  that change in a way that matters (taxes, per-unit figures).
- **The economic share count is larger than the Class A common count**: Blackstone Holdings Partnership Units held by
  senior managing directors are exchangeable one-for-one into common stock, and the Series I / Series II preferred
  stock carries votes, not economics (settle on the 10-Q cover, the equity note and the "Blackstone Holdings" units
  disclosure; the 10-K/10-Q often reports a total including units). Decide which count the cap uses and state why.
- The company reports non-GAAP Fee Related Earnings and Distributable Earnings; neither is owner earnings. The BAM run
  used BX's FRE margin 58.3% and a fee rate of 92.2bp (firm's own 0.86%) (settle on BX's FY2025 10-K / earnings release).
- Stephen Schwarzman is chairman, CEO and co-founder with a large holding; Jon Gray is president and COO and named
  successor (settle on the DEF 14A beneficial ownership table and succession disclosure) [E4-23].
- BREIT, the non-traded REIT, limited redemptions in late 2022 into 2023 (settle on BX's 10-K risk factors / MD&A and
  BREIT's own filings; date it to when it became PUBLIC). Any SEC or other regulatory matter: settle on the legal
  proceedings note and SEC releases; date each to when it became PUBLIC.
- Dividend policy pays out a high share of distributable earnings (settle on the 10-K dividend policy section).

## 4. REQUIRED HANDLING (the project's standing rules; none of them is a hint about a verdict)
- **Write-early.** Copy the template to `Test Runs/2026-09-18 Run - BX Blackstone.md` BEFORE fetching anything, commit
  it, then write each section as it closes and commit after every gate. Research files go in
  `Test Runs/_research 2026-09-18 BX/`. **COMMIT WITH A PATHSPEC ONLY: write the message to a file and use
  `git commit -F <msgfile> -- <path> <path>`.** Never `git add X && git commit` (it commits the whole shared index and has
  swept other sessions' files into wrong commits six times). `git add` a NEW file before the pathspec commit so it is
  tracked, then commit with the pathspec. Bash heredocs containing apostrophes fail in this environment: write scripts to
  the research folder. Commit trailer: `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. Also commit this brief,
  the two probe scripts, their outputs and the a8bc84f copy into the research folder with your first commit
  (companyfacts.json left untracked, as RIVN and DJT did: re-fetchable, large). `.gitignore` covers .htm/.html/.pdf/.xlsx
  under research folders but NOT images: **do not commit image files.**
- **Sovereign**: strike it yourself from the US Treasury daily par yield curve, 30-year, dated
  (`python tools/sources.py` or the Treasury site; FRED DGS30 only as fallback). `tools/sources.sovereign()` has served a
  stale cached row four times; confirm the date on the row you use against the Treasury itself. Do not inherit the DJT
  run's figure.
- **Price**: re-strike it yourself; aggregators are allowed for live quotes only and are flagged.
  `tools/sources.price()` returns an intraday price stamped with today's date although its docstring says "latest close";
  use a dated close and say which. Cross-check against a Form 4 price if one is recent.
- **Share count**: from the cover of the LATEST periodic filing (`python Screens/cover_shares.py BX`, and read the cover
  itself), with the accession. Then the units question in section 3: show the cap on common alone and on common plus
  exchangeable units, and say which one the yield uses and why.
- **SBC**: verify it RESOLVES and is COMPLETE on the face of the cash-flow statement for every year you use. Where SBC/OCF
  is high, [E3-70] asks what the options could have been sold for; the grant table is read by hand (source limit). For a
  firm that pays people partly in carried interest, find where that compensation sits (performance allocations
  compensation) and whether it is cash, and say how owner earnings treats it.
- **Deal check**: query EDGAR yourself for any live merger, tender or going-private (8-K Items 1.01/2.01, SC TO, S-4,
  DEFM14A, SC 13D). A live deal makes the quote a spread or changes which company the price buys (ROKU, HHH, DJT).
- **Owner earnings**: rebuild the width over every window the filed statements support, and both (c) ends, from the filed
  statements, never a net-income proxy. Strip the consolidated funds out of operating cash using the company's own
  disclosure (the consolidating schedules or the "Blackstone Funds" lines), and show the bridge. Separate cash from fees,
  cash from realized performance revenue, and income on the firm's own balance sheet, and say which ones owner earnings
  measures, with the ledger id that governs the choice. Say which windows do not exist and why. Report dollars, and a word,
  wherever the bottom sits near or below zero.
- **Hard sequence Q1 to Q5. STOP at the first question that is not IN.** UNRESEARCHED and UNKNOWABLE both close the file.
  Recent runs recorded later questions beneath a close under an explicit "RECORDED, NOT GOVERNING" banner; that is
  allowed, but no such section may carry entry language, and any valuation before Q1-Q4 all close IN is headed exactly
  `COMPUTATION — NOT A CLEARANCE`.
- **Q3**: pull the latest 8-K EX-99.1 earnings releases before scoring [E4-29] and [E4-22]'s flags (the CGNX companion
  rule). The honesty binary is [E5-16]; the incentive read is [E4-27] (NOT [E4-52], which is the lollapalooza row);
  [E5-22] is penalty size is not seriousness; [E4-34] is the four auditor questions; [E2-26] is candor. Read the proxy for
  what pay vests on, for carried-interest allocation to insiders, and for related-party arrangements.
- **Q2**: a moat is a relative claim. The same-metric competitor row is a CONVENTION the framework keeps (the corpus's
  own test is pricing conduct plus returns on capital [E3-43]; [E3-28] is the monitoring quote, not the row's authority).
  Build it from competitors' own filings; the BAM run's nine-peer row (OWL, TPG, ARES, BAM, CG, KKR, APO, TROW, BLK) is a
  starting map, re-verified on each filer's filing, never copied. Full-text search via `tools/sources.py fts_count()`
  needs the bare zero-padded 10-digit CIK or it silently returns zero. [E3-03] is the franchise definition; [E2-44] the
  pricing-power and low-capital pair; [E4-04] the rapid-change exclusion; [E3-46] return on capital; [E2-45] the
  grizzlies question; [E2-58] the cost-advantage exception; [E2-59] commodity product plus over-capacity; [E3-62] who
  keeps the gains; [E4-37] the price-rise test; [E4-23] key-person dependence.
- Q1 asks whether you can understand how THIS business makes money on its filings; if the price is paying for something
  the filings do not show as a business, say what the filings show and what they do not, with [E3-31] and [E4-46] as the
  RIVN, TSLA and DJT runs used them, checked against the ledger.
- The TSMC corpus tension against [E4-04] (the 2023 meeting) is an OPEN operator question; if [E4-04] matters here, apply
  v4 as written and note the tension, do not resolve it.
- Every ledger id you cite must exist in `principle_ledger.csv` and say what you cite it for (check it; the acceptance
  test cannot catch a real id cited for the wrong thing).
- No em dashes in your own prose (verbatim quotes and the required `COMPUTATION — NOT A CLEARANCE` heading excepted).
- Nothing about the framework changes: no ledger rows, no edits under `Framework/`. Corrections go in dated notes.
- Never present the framework as proven to beat the market (operator rule 7).

## 5. THE FOLD - do all six steps yourself (queue file, `## THE FOLD`)
1. Register entry at the TOP of `## COMPLETED FROM THE QUEUE` in `Screens/WATCHLIST RUN QUEUE.md`, in the same form as
   the DJT entry: price, share count and cover accession, cap, sovereign, and the PASS/FAIL line naming the question
   that closed the file. **Count the register from its heading line to `## THE WRITE-EARLY PROTOCOL`** (entries
   beginning `- **TICKER (`; the ten backfill entries under the `### REGISTER BACKFILL` heading count; DJT's fold said
   106 on this rule) and state the new total. Check for a duplicate ticker while counting.
2. Strike BX in the wave 5 table (`~~BX~~`), and add a short dated note beside the table on what the "perimeter or
   restatement" label turned out to be for BX (the DJT note is the model; do not edit history).
3. Narrative fold into `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`.
4. `tools/alerts.json` bands and a `PORTFOLIO.md` row ONLY if all four business gates clear. If the file closes at Q1-Q4,
   record the reversal condition in words instead.
5. `python tools/check_framework.py` must PASS before the fold commit.
6. Pathspec commit.
Also add a new survival shape to `Screens/SURVIVAL SHAPES - index.md` only if you name one.

## 6. WHAT TO RETURN TO ME
A short report: the verdict line (which question closed the file and on which ledger ids); price with date and source;
share count with accession; cap (both counts); sovereign with date; the owner-earnings range; what the skip reason turned
out to be; the register count after your entry; check_framework result; the commit hashes; and every defect you found in
this brief. If you hit a usage or rate limit, commit whatever is on disk with a pathspec commit and say exactly where you
stopped.
