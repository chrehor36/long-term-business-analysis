# BRIEF - SNOW (Snowflake Inc.), wave 5, overnight cycle 2026-09-18 ~15:20 EDT

You are running ONE company through the framework, from scratch, unattended. The operator is asleep and nobody will
answer a question. Repository: `C:\Users\chreh\OneDrive\Documents\BRK`. Work in it directly.

## 0. READ FIRST (in this order)
1. `CLAUDE.md` (operator protocol, prime rules, tools).
2. `Framework/THE FRAMEWORK v4.md` - the governing document. If a rule is not in it, it is not in force.
3. `Test Runs/_TEMPLATE - Company Run.md` - the run surface.
4. For what a finished run looks like: `Test Runs/2026-09-18 Run - SMCI Super Micro Computer.md` (the first name of
   this same wave 5 row, finished an hour ago) and `Test Runs/2026-09-18 Run - TOST Toast.md` (a software name with
   heavy SBC). Read their structure, self-audit, brief-defects section and REGISTER block.
5. `Screens/WATCHLIST RUN QUEUE.md`: the sections `THE WRITE-EARLY PROTOCOL`, `THE FOLD`, `WRITING A BRIEF`, the
   `#### WAVE 5` table and ALL its dated notes (the SMCI note is the one for your row), and the top two entries of
   `## COMPLETED FROM THE QUEUE` (the format).
6. `Screens/SURVIVAL SHAPES - index.md` - name survival shapes by their number; add a new one there only when folding.
7. `Screens/RESUME STATE 2026-09-12 - Opus session, note for Fable.md` sections 3-5: tooling changes, errors not to
   repeat, and the source limits already tested (do not re-attempt them).

## 1. THE NAME, AND WHY IT IS HERE
- Ticker SNOW, Snowflake Inc., CIK 0001640147, Delaware, fiscal year ends January 31 (FY2026 = year ended
  2026-01-31). 10-K/10-Q filer. Latest 10-Q per the dei feed filed 2026-09-04 (quarter ended 2026-07-31).
- **No screen row exists** in `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv` (checked by this cycle).
- **Skip reason from the wave 5 table, a prompt to read and never a verdict:** *"perimeter or restatement above
  threshold: read the filing first"* (the skipped-reason list adds: *"revenue step or cross-accession restatement
  above threshold"*). The SMCI run's dated note asks that each remaining name in this row be reproduced against the
  `a8bc84f` guards to see which one fired. This cycle did a first pass (section 2); **find out on the filings what the
  flag was reacting to and say so, including which guard actually returned the name unpriced and at what threshold**
  (read the guard order and thresholds in `floor_screen_a8bc84f.py`; I did not).

## 2. WHAT THE SCREEN RETURNS (tagged data, transcription only; operator rule 4)
This cycle pulled companyfacts fresh at ~15:15 EDT 2026-09-18. Script: `Test Runs/_research 2026-09-18 SNOW/_probe_screen.py`;
output `_probe_screen_output.txt`; raw pull `companyfacts.json`; the triage code copy `floor_screen_a8bc84f.py`, all in
that folder (do not refetch companyfacts unless you need a newer vintage). The probe passes the ticker to
`share_count_shift` (the SMCI brief's probe did not; defect 1 there). **Every figure is a prompt to read the filed
statement, not a finding:**
- **a8bc84f on facts filed by 2026-09-01:** `share_count_shift` 1.034; `scale_shift` **2.06**; `restatement_shift`
  (1.0, FY2020) - a 1.0 is a null, not a flag (SMCI brief defect 2: the function stops at the first revenue element
  with data); `owner_earnings` 5y D&A end -$527M, 5y capex end -$450M.
- **Current screen:** `owner_earnings()` 5y D&A end -$527M, 5y capex end -$471M, 3y D&A end -$580M, 3y capex end
  -$488M. `scale_shift` 2.06; `share_count_shift` (with ticker) 1.07; `acquisition_flag` $847.5M over five years;
  `stale_filer` newest annual 2026-01-31.
- `working_capital_flag` FIRES: *"ONE LINE MADE THE CASH: ContractWithCustomerLiability moved 478% of 2022 OCF"*.
- Tagged revenue ($M, FY ending Jan): FY2019 96.7, FY2020 264.7, FY2021 592.0, FY2022 1,219.3, FY2023 2,065.7,
  FY2024 2,806.5, FY2025 3,626.4, FY2026 4,683.9.
- Tagged operating cash ($M): FY2019 -144.0, FY2020 -176.6, FY2021 -45.4, FY2022 110.2, FY2023 545.6, FY2024 848.1,
  FY2025 959.8, FY2026 1,221.9.
- Tagged SBC ($M): FY2021 301.4, FY2022 605.1, FY2023 861.5, FY2024 1,168.0, FY2025 1,479.3, FY2026 1,599.5.
- Tagged capex (`annual(CAPX_TAGS)`) FY2026 $101.6M; `capital_acquired()` differs from `annual()` in FY2019-25
  (e.g. FY2025 $75.7M vs $46.3M) - read which lines the face carries (capitalised internal-use software? TOST's
  definition break is the precedent). Tagged D&A FY2026 $220.4M.
- dei cover counts: 345.7M (2026-03-06, 10-K), 346.6M (2026-05-15), **352.8M (2026-08-21, 10-Q filed 2026-09-04)**.
  The dei feed rounds to the hundred-thousand; read the exact count on the cover yourself.
The questions these raise are yours to answer: what the 2.06 revenue step is made of (organic growth or perimeter);
whether any restatement exists on the filings; what the deferred-revenue line did to operating cash and whether any
of it is customer float in the [E3-52] sense or simply prepaid capacity; whether SBC resolves AND is complete; what
the D&A is made of; and what the growing capex line buys.

## 3. THINGS I BELIEVE FROM MEMORY - UNVERIFIED. Verify each on a filing or discard it; never carry one forward
My knowledge has a cutoff that predates the newest filings, and a past brief of mine quoted a price increase that
appeared in no filing (ELF). Each is a hypothesis with the document that would settle it:
- IPO September 2020 (settle on the S-1/424B4). The pre-IPO years are in the S-1 only.
- Revenue is consumption-based: customers buy capacity contracts and are billed for credits consumed; "product
  revenue", net revenue retention and remaining performance obligations are headline disclosures (settle on the
  10-K revenue recognition note and MD&A key metrics).
- The platform runs on AWS, Microsoft Azure and Google Cloud, which are also named competitors (Redshift, Fabric /
  Synapse, BigQuery); Databricks is a private competitor. Snowflake pays the clouds under multi-year purchase
  commitments (settle on the 10-K competition section, the commitments note, and the three clouds' own filings where
  a comparable line exists; a private competitor's absence from EDGAR is a limit to record, not a reason to skip -
  but see whether any filed source counts both, as the SPGI run found Form NRSRO did for its industry).
- CEO change: Frank Slootman to Sridhar Ramaswamy in February 2024 (settle on the 8-K Item 5.02).
- A 2024 incident in which customer accounts were accessed with stolen credentials (settle on the 8-Ks and the 10-K
  risk factors / legal proceedings: what is filed, what is still open, any litigation).
- Convertible senior notes of about $2.3bn issued in 2024 with capped calls, and large share repurchases (settle on
  the debt note, the equity note and the buyback 8-Ks; the capped call and the buyback both bear on the share count).
- Acquisitions paid substantially in stock (Streamlit 2022; others later, possibly including Neeva and Crunchy Data)
  (settle on the business-combinations note; the acquisition flag says $847.5M over five years).
- The company headlines non-GAAP operating margin and adjusted free cash flow in its releases (settle on the 8-K
  EX-99.1 earnings releases before scoring [E4-29] and [E4-22]).
Date each matter to when it became PUBLIC.

## 4. REQUIRED HANDLING (the project's standing rules; none of them is a hint about a verdict)
- **Write-early.** Copy the template to `Test Runs/2026-09-18 Run - SNOW Snowflake.md` BEFORE fetching anything,
  commit it, then write each section as it closes and commit after every gate. Research files go in
  `Test Runs/_research 2026-09-18 SNOW/`. **COMMIT WITH A PATHSPEC ONLY: write the message to a file and use
  `git commit -F <msgfile> -- <path> <path>`.** Never `git add X && git commit` (it commits the whole shared index and
  has swept other sessions' files into wrong commits six times). `git add` a NEW file before the pathspec commit so it
  is tracked, then commit with the pathspec. Bash heredocs containing apostrophes fail in this environment: write
  scripts to the research folder. Commit trailer: `Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>`.
  Also commit this brief, the probe and its output into the research folder with your first commit.
- **Sovereign**: strike it yourself from the US Treasury daily par yield curve, 30-year, dated
  (`python tools/sources.py` or the Treasury site; FRED DGS30 only as fallback). The last run used 5.29% (09/17/2026);
  do not inherit it.
- **Price**: re-strike it yourself; aggregators are allowed for live quotes only and are flagged.
  `tools/sources.price()` returns an intraday price stamped with today's date although its docstring says "latest
  close" (four runs have recorded this); use a dated close and say which. Cross-check against a Form 4 price if one
  is recent.
- **Share count**: from the cover of the LATEST periodic filing (`python Screens/cover_shares.py SNOW`), with the
  accession. Never sum share classes without reading the charter. Consider whether the convertible notes (net of any
  capped call) belong in the count at the price you strike, and state the answer either way.
- **SBC**: verify it RESOLVES and is COMPLETE on the face of the cash-flow statement for every year you use (BE's did
  not resolve and the screen subtracted zero; Boeing's resolved under a tag no SBC element contains; TOST capitalised
  some into software). Where SBC/OCF is high, [E3-70] asks what the options could have been sold for; the grant
  table is read by hand (source limit). Also consider what shares were repurchased for against what was issued.
- **Deal check**: query EDGAR yourself for any live merger, tender or going-private (8-K Items 1.01/2.01, SC TO, S-4,
  DEFM14A, SC 13D). A live deal makes the quote a spread, not an owner-earnings price (ROKU).
- **Owner earnings**: rebuild the width over every window (3y, 5y, and TTM if you use it; a 10-year window may not
  exist on filed statements, and say so if not) and both (c) ends, from the filed statements, never a net-income proxy.
  Report dollars, and a word, wherever the bottom sits near or below zero. Ask what the D&A is made of before
  assuming the (c) band is about plant, and ask [E5-20] on the filing. Show the deferred-revenue contribution to
  operating cash explicitly, both ways, as the TOST run did for its interest income.
- **Hard sequence Q1 to Q5. STOP at the first question that is not IN.** UNRESEARCHED and UNKNOWABLE both close the
  file. Recent runs recorded later questions beneath a close under an explicit "RECORDED, NOT GOVERNING" banner; that
  is allowed, but no such section may carry entry language, and any valuation before Q1-Q4 all close IN is headed
  exactly `COMPUTATION — NOT A CLEARANCE`.
- **Q3**: pull the latest 8-K EX-99.1 earnings releases before scoring [E4-29] and [E4-22]'s flags (the CGNX
  companion rule). The honesty binary is [E5-16]; the incentive read is [E4-27] (NOT [E4-52], which is the
  lollapalooza row, the converging-flags reading); [E5-22] is penalty size is not seriousness; [E4-34] is the four
  auditor questions; [E2-26] is candor. Read the proxy for what pay vests on.
- **Q2**: a moat is a relative claim. The same-metric competitor row is a CONVENTION the framework keeps (v4 line ~1241:
  the corpus's own test is pricing conduct plus returns on capital [E3-43]; [E3-28] "the other eight" is the
  monitoring quote, not the row's authority). Build it from competitors' own filings (full-text search via
  `tools/sources.py fts_count()` needs the bare zero-padded 10-digit CIK or it silently returns zero). [E3-03] is the
  franchise definition; [E2-44] the pricing-power and low-capital pair; [E4-04] the rapid-change exclusion; [E3-46]
  return on capital; [E2-45] the grizzlies question; [E2-58] the cost-advantage exception; [E2-59] commodity product
  plus over-capacity; [E3-62] who keeps the gains; [E4-37] the price-rise test; [E4-23] key-person dependence.
- The TSMC corpus tension against [E4-04] (the 2023 meeting) is an OPEN operator question; if [E4-04] matters here,
  apply v4 as written and note the tension, do not resolve it.
- **Prior material on disk, read as UNLABELLED evidence, not as a conclusion**: the PLTR run
  (`Test Runs/2026-09-11 Run - PLTR Palantir.md`, around lines 279, 352 and 416) used Snowflake as a data-platform
  comparator. Its figures were computed for Palantir's question; recompute anything you use from Snowflake's own
  filings.
- Every ledger id you cite must exist in `principle_ledger.csv` and say what you cite it for (check it; the acceptance
  test cannot catch a real id cited for the wrong thing).
- No em dashes in your own prose (verbatim quotes and the required `COMPUTATION — NOT A CLEARANCE` heading excepted).
- Nothing about the framework changes: no ledger rows, no edits under `Framework/`. Corrections go in dated notes.
- Never present the framework as proven to beat the market (operator rule 7).

## 5. THE FOLD - do all six steps yourself (queue file, `## THE FOLD`)
1. Register entry at the TOP of `## COMPLETED FROM THE QUEUE` in `Screens/WATCHLIST RUN QUEUE.md`, in the same form as
   the SMCI entry: price, share count and cover accession, cap, sovereign, and the PASS/FAIL line naming the question
   that closed the file. Count the register from its heading line (not the first occurrence of the phrase) and state
   the new total (SMCI's fold said 102).
2. Strike SNOW in the wave 5 table (`~~SNOW~~`), and add a short dated note beside the table on what the "perimeter or
   restatement" label turned out to be for SNOW (the SMCI note is the model; do not edit history).
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
