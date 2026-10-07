# BRIEF - AEHR (Aehr Test Systems), wave 5, overnight cycle 2026-09-18 ~20:45 EDT

You are running ONE company through the framework, from scratch, unattended. The operator is asleep and nobody will
answer a question. Repository: `C:\Users\chreh\OneDrive\Documents\BRK`. Work in it directly.

## 0. READ FIRST (in this order)
1. `CLAUDE.md` (operator protocol, prime rules, tools).
2. `Framework/THE FRAMEWORK v4.md` - the governing document. If a rule is not in it, it is not in force.
3. `Test Runs/_TEMPLATE - Company Run.md` - the run surface.
4. For what a finished run looks like: `Test Runs/2026-09-18 Run - BX Blackstone.md` (the previous name in this same wave 5
   row, finished about fifteen minutes before this brief) and `Test Runs/2026-09-18 Run - SMCI Super Micro Computer.md`
   (a semiconductor-hardware name from the same row). Read their structure, self-audit, brief-defects section and
   REGISTER block. Their findings belong to their companies; nothing in them is evidence about AEHR. Earlier runs of
   semiconductor test and equipment names (search `Test Runs/` for AMAT, KLAC, TER, ACMR, ACLS, COHU, FORM) may show where
   to look for a competitor row; every figure you use must be re-read on the filer's own filing and cited by accession.
5. `Screens/WATCHLIST RUN QUEUE.md`: the sections `THE WRITE-EARLY PROTOCOL`, `THE FOLD`, `WRITING A BRIEF`, the
   `#### WAVE 5` table and ALL its dated notes (the SMCI, SNOW, TSLA, RIVN, DJT and BX notes are the ones for your row),
   and the top two entries of `## COMPLETED FROM THE QUEUE` (the format).
6. `Screens/SURVIVAL SHAPES - index.md` - name survival shapes by their number; add a new one there only when folding.
7. `Screens/RESUME STATE 2026-09-12 - Opus session, note for Fable.md` sections 3-5: tooling changes, errors not to
   repeat, and the source limits already tested (do not re-attempt them).

## 1. THE NAME, AND WHY IT IS HERE
- Ticker AEHR, Aehr Test Systems, **CIK 0001040470** (companyfacts at that CIK returns entityName "AEHR TEST SYSTEMS";
  confirm against the SEC `company_tickers.json`). **Fiscal year ends on the last Friday of May** (FY2026 ended
  2026-05-29, FY2025 2025-05-30). 10-K/10-Q filer; dei shows a 10-K filed 2026-07-27. Confirm the latest periodic filing
  (a Q1 FY2027 10-Q would not be due until about October) from `submissions.json`.
- **A screen row exists, but not in the corrected master queue**: `Screens/2026-09-01 NEW CANDIDATES batch2.csv` line 33:
  `AEHR,AEHR TEST SYSTEMS,2520,-10,-0.0041,-0.0559,0.1041,` under header
  `ticker,name,cap_m,oe_bottom_m,yield_bottom,vs_sovereign,growth_required,spread` (cap $2,520M, owner-earnings bottom
  -$10M, yield -0.41%). Transcription only; its cap is from 2026-09-01 and is not your price.
- **Skip reason from the wave 5 table, a prompt to read and never a verdict:** *"perimeter or restatement above
  threshold: read the filing first"* (the skipped-reason list adds: *"revenue step or cross-accession restatement above
  threshold"*). **Find out on the filings what the flag was reacting to and say so.** Carry the row's lessons: the TSLA
  note (check a `scale_shift` above 2.0 for non-consecutive years), the SNOW note (`restatement_shift` is not called by
  the triage pipeline), the RIVN note (a `share_count_shift` of None is a missing element), the DJT note (assign each
  tagged year to the right reporting entity), the BX note (read the revenue lines before treating a step as a step).
  **AEHR is the last name in this row; the fold's dated note should close the row's tally.**

## 2. WHAT THE SCREEN RETURNS (tagged data, transcription only; operator rule 4)
This cycle pulled companyfacts fresh at ~20:40 EDT 2026-09-18. Scripts `_probe_screen.py` and `triage_repro.py`, outputs
`_probe_screen_output.txt` and `triage_repro_out.txt`, raw pull `companyfacts.json`, and the triage code copy
`floor_screen_a8bc84f.py`, all in `Test Runs/_research 2026-09-18 AEHR/` (do not refetch companyfacts unless you need a
newer vintage). **Every figure is a prompt to read the filed statement, not a finding:**
- **a8bc84f guard order on facts filed by 2026-09-01:** `share_count_shift` **1.098** (passes); `scale_shift` **3.062**
  (FIRES), on FY2021 $16.6M to FY2022 $50.8M under the revenue elements; the later steps are 1.278, 1.019, 0.891, 0.848
  (FY2023 $65.0M, FY2024 $66.2M, FY2025 $59.0M, FY2026 $50.0M). **Check the years are consecutive and the element is the
  same on both sides (the TSLA check) before reading it as a step.** `filed_years` 17; `restatement_shift` (1.0, FY2018),
  a null.
- `owner_earnings` (screen, current and a8bc84f agree): 5y D&A end -$4.84M, 5y capex end -$5.44M; 3y -$9.74M / -$10.40M.
- Tagged operating cash ($M): FY2017 -4.50, FY2018 -1.35, FY2019 -5.64, FY2020 -2.02, FY2021 -2.70, FY2022 +1.51,
  FY2023 +10.01, FY2024 +1.76, FY2025 -7.40, FY2026 -3.31. Positive in three of the last ten years.
- `working_capital_flag` FIRES: FY2024, `IncreaseDecreaseInAccountsPayable` moved 222% of that year's OCF. Tagged
  inventory increase FY2023 $9.5M, FY2024 $13.7M, FY2025 $2.4M; inventory $15.1M (FY2022) to $41.4M (FY2026).
- Tagged SBC ($M): ~$0.9-1.1M a year to FY2021, then 3.0, 2.7, 2.5, 5.2, 6.8 (FY2022-26). Check the face resolves and is
  complete every year you use.
- Tagged D&A ($M): 0.31 (FY2022) to 2.80 (FY2026). Tagged capex ($M): 0.42, 1.36, 0.75, 4.99, 2.07 (FY2022-26).
- `acquisition_flag` $12.9M: `PaymentsToAcquireBusinessesNetOfCashAcquired` $11.1M FY2025 and $1.8M FY2026; goodwill
  $10.7M from FY2025. **This is an acquisition inside the owner-earnings window; find it, its price, and what it added to
  revenue and D&A.**
- Tagged net income: FY2023 $14.6M, FY2024 $33.2M, FY2025 -$3.9M, FY2026 -$7.1M. A profit that operating cash does not
  follow is a prompt to read the tax note and the cash-flow statement.
- Cash $116.4M at FY2026 end against $24.5M a year earlier; `ProceedsFromIssuanceOfCommonStock` tags of $10.0M, $10.5M,
  $19.5M and $60.0M across FY2026 periods. **Find how many shares were sold, how, and at what prices.**
- dei `EntityCommonStockSharesOutstanding`: 29,915,061 (2025-07-15) ... **32,620,450 (2026-07-20, FY2026 10-K filed
  2026-07-27)**. `EntityPublicFloat` $671.4M (2025-11-28).
The questions these raise are yours to answer: what made the FY2022 step and whether it is a perimeter; who the
customers are and how concentrated; what the business earns in cash over the whole cycle and whether any window exists
in which owner earnings are positive; what the inventory and payables movements are made of; and what the count is.

## 3. THINGS I BELIEVE FROM MEMORY - UNVERIFIED. Verify each on a filing or discard it; never carry one forward
My knowledge has a cutoff that predates the newest filings, and a past brief of mine quoted a price increase that
appeared in no filing (ELF). Each is a hypothesis with the document that would settle it:
- Aehr sells wafer-level and package-level burn-in and test systems (FOX-P family) and consumables (WaferPaks,
  DiePaks); the FY2022-24 rise came from silicon carbide power devices for electric vehicles, with one customer
  (onsemi, I believe) a very large share of revenue, and the decline since from the EV/SiC slowdown (settle on the 10-K
  customer-concentration note and MD&A for each year).
- Aehr bought Incal Technology (package-level burn-in, I believe) in FY2025 (settle on the 8-K and the business
  combination note: price, consideration, revenue added). This is the `acquisition_flag`.
- FY2024 net income included a large release of the deferred-tax valuation allowance (settle on the FY2024 income-tax
  note); if so, FY2024 earnings overstate the business.
- Management has pointed to AI processors, hard-disk drives, gallium nitride and silicon photonics as new markets
  (settle on the 10-K business section and the earnings releases; anything the filings do not show as revenue is outside
  the circle, [E3-31] and [E4-46], as the RIVN and TSLA runs used them).
- Gayn Erickson is CEO (settle on the DEF 14A). Aehr ran an at-the-market offering programme (settle on the S-3,
  prospectus supplements and the 10-K equity note).
- Competitors in burn-in/test include Advantest, Teradyne, FormFactor, Cohu and others (settle on the 10-K competition
  section, which names them; build the row from their own filings).

## 4. REQUIRED HANDLING (the project's standing rules; none of them is a hint about a verdict)
- **Write-early.** Copy the template to `Test Runs/2026-09-18 Run - AEHR Aehr Test Systems.md` BEFORE fetching anything,
  commit it, then write each section as it closes and commit after every gate. Research files go in
  `Test Runs/_research 2026-09-18 AEHR/`. **COMMIT WITH A PATHSPEC ONLY: write the message to a file and use
  `git commit -F <msgfile> -- <path> <path>`.** Never `git add X && git commit` (it commits the whole shared index and has
  swept other sessions' files into wrong commits six times). `git add` a NEW file before the pathspec commit so it is
  tracked, then commit with the pathspec. **Check that each edit succeeded before committing** (the BX run committed after
  a failed edit assertion). Bash heredocs containing apostrophes fail in this environment: write scripts to the research
  folder. Commit trailer: `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. Also commit this brief, the two probe
  scripts, their outputs and the a8bc84f copy into the research folder with your first commit (companyfacts.json left
  untracked, as RIVN, DJT and BX did: re-fetchable, large). `.gitignore` covers .htm/.html/.pdf/.xlsx under research
  folders but NOT images: **do not commit image files.**
- **Sovereign**: strike it yourself from the US Treasury daily par yield curve, 30-year, dated
  (`python tools/sources.py` or the Treasury site; FRED DGS30 only as fallback). `tools/sources.sovereign()` has served a
  stale cached row five times; confirm the date on the row you use against the Treasury itself. Do not inherit the BX
  run's figure.
- **Price**: re-strike it yourself; aggregators are allowed for live quotes only and are flagged.
  `tools/sources.price()` returns an intraday price stamped with today's date although its docstring says "latest close";
  use a dated close and say which. Cross-check against a Form 4 price if one is recent.
- **Share count**: from the cover of the LATEST periodic filing (`python Screens/cover_shares.py AEHR`, and read the cover
  itself), with the accession. Add anything sold after the cover date (ATM or offering 8-Ks, prospectus supplements).
- **SBC**: verify it RESOLVES and is COMPLETE on the face of the cash-flow statement for every year you use. Where SBC/OCF
  is high, [E3-70] asks what the options could have been sold for; the grant table is read by hand (source limit).
- **Deal check**: query EDGAR yourself for any live merger, tender or going-private (8-K Items 1.01/2.01, SC TO, S-4,
  DEFM14A, SC 13D). A live deal makes the quote a spread or changes which company the price buys (ROKU, HHH, DJT).
- **Owner earnings**: rebuild the width over every window the filed statements support, and both (c) ends, from the filed
  statements, never a net-income proxy. Say what the working-capital increment is made of in each year (inventory build,
  customer deposits, payables) and whether it reverses. Say which windows do not exist and why. Report dollars, and a
  word, wherever the bottom sits near or below zero. The acquisition sits inside the window: say how (c) treats it.
- **Hard sequence Q1 to Q5. STOP at the first question that is not IN.** UNRESEARCHED and UNKNOWABLE both close the file.
  Recent runs recorded later questions beneath a close under an explicit "RECORDED, NOT GOVERNING" banner; that is
  allowed, but no such section may carry entry language, and any valuation before Q1-Q4 all close IN is headed exactly
  `COMPUTATION — NOT A CLEARANCE`.
- **Q3**: pull the latest 8-K EX-99.1 earnings releases before scoring [E4-29] and [E4-22]'s flags (the CGNX companion
  rule). The honesty binary is [E5-16]; the incentive read is [E4-27] (NOT [E4-52], which is the lollapalooza row);
  [E5-22] is penalty size is not seriousness; [E4-34] is the four auditor questions; [E2-26] is candor. Read the proxy for
  what pay vests on, and compare what management said about customers and markets in past releases with what later
  filings reported.
- **Q2**: a moat is a relative claim. The same-metric competitor row is a CONVENTION the framework keeps (the corpus's
  own test is pricing conduct plus returns on capital [E3-43]; [E3-28] is the monitoring quote, not the row's authority).
  Build it from competitors' own filings (foreign filers on their 20-F/annual report). Full-text search via
  `tools/sources.py fts_count()` needs the bare zero-padded 10-digit CIK or it silently returns zero. [E3-03] is the
  franchise definition; [E2-44] the pricing-power and low-capital pair; [E4-04] the rapid-change exclusion; [E3-46]
  return on capital; [E2-45] the grizzlies question; [E2-58] the cost-advantage exception; [E2-59] commodity product
  plus over-capacity; [E3-62] who keeps the gains; [E4-37] the price-rise test; [E4-23] key-person dependence. Customer
  concentration bears on who holds the bargaining power; read it from the filing.
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
   the BX entry: price, share count and cover accession, cap, sovereign, and the PASS/FAIL line naming the question
   that closed the file. **Count the register from its heading line to `## THE WRITE-EARLY PROTOCOL`** (entries
   beginning `- **TICKER (`; the ten backfill entries under the `### REGISTER BACKFILL` heading count; BX's fold said
   107 on this rule) and state the new total. Check for a duplicate ticker while counting.
2. Strike AEHR in the wave 5 table (`~~AEHR~~`), and add a short dated note beside the table on what the "perimeter or
   restatement" label turned out to be for AEHR (the BX note is the model; do not edit history). It is the last name in
   the row: close the row's tally in that note.
3. Narrative fold into `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`.
4. `tools/alerts.json` bands and a `PORTFOLIO.md` row ONLY if all four business gates clear. If the file closes at Q1-Q4,
   record the reversal condition in words instead.
5. `python tools/check_framework.py` must PASS before the fold commit.
6. Pathspec commit.
Also add a new survival shape to `Screens/SURVIVAL SHAPES - index.md` only if you name one.

## 6. WHAT TO RETURN TO ME
A short report: the verdict line (which question closed the file and on which ledger ids); price with date and source;
share count with accession; cap; sovereign with date; the owner-earnings range; what the skip reason turned out to be;
the register count after your entry; check_framework result; the commit hashes; and every defect you found in this
brief. If you hit a usage or rate limit, commit whatever is on disk with a pathspec commit and say exactly where you
stopped.
