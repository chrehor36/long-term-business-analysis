# BRIEF - DJT (Trump Media & Technology Group Corp.), wave 5, overnight cycle 2026-09-18 ~19:45 EDT

You are running ONE company through the framework, from scratch, unattended. The operator is asleep and nobody will
answer a question. Repository: `C:\Users\chreh\OneDrive\Documents\BRK`. Work in it directly.

## 0. READ FIRST (in this order)
1. `CLAUDE.md` (operator protocol, prime rules, tools).
2. `Framework/THE FRAMEWORK v4.md` - the governing document. If a rule is not in it, it is not in force.
3. `Test Runs/_TEMPLATE - Company Run.md` - the run surface.
4. For what a finished run looks like: `Test Runs/2026-09-18 Run - RIVN Rivian.md` (the previous name in this same wave 5
   row, finished about twenty minutes before this brief) and `Test Runs/2026-09-13 Run - RGTI Rigetti.md` if it exists
   (a de-SPAC where companyfacts held shell and target years under colliding keys; find it with a glob on `*RGTI*`).
   Read their structure, self-audit, brief-defects section and REGISTER block. Their findings belong to their companies;
   nothing in them is evidence about DJT.
5. `Screens/WATCHLIST RUN QUEUE.md`: the sections `THE WRITE-EARLY PROTOCOL`, `THE FOLD`, `WRITING A BRIEF`, the
   `#### WAVE 5` table and ALL its dated notes (the SMCI, SNOW, TSLA and RIVN notes are the ones for your row), and the
   top two entries of `## COMPLETED FROM THE QUEUE` (the format).
6. `Screens/SURVIVAL SHAPES - index.md` - name survival shapes by their number; add a new one there only when folding.
7. `Screens/RESUME STATE 2026-09-12 - Opus session, note for Fable.md` sections 3-5: tooling changes, errors not to
   repeat, and the source limits already tested (do not re-attempt them).

## 1. THE NAME, AND WHY IT IS HERE
- Ticker DJT, Trump Media & Technology Group Corp., **CIK 0001849635** (confirmed against the SEC `company_tickers.json`
  by this cycle). Fiscal year = calendar year per companyfacts. 10-K/10-Q filer. companyfacts shows a 10-K filed
  2026-02-27, a **10-K/A filed 2026-04-30**, and 10-Qs filed 2026-05-08 and 2026-08-10. Confirm the latest periodic
  filing, and what the 10-K/A amended, from `submissions.json`.
- **No screen row exists** in `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv` or the 2026-09-01 triage/floor
  CSVs (grepped by this cycle).
- **Skip reason from the wave 5 table, a prompt to read and never a verdict:** *"perimeter or restatement above
  threshold: read the filing first"* (the skipped-reason list adds: *"revenue step or cross-accession restatement above
  threshold"*). The earlier notes in this row ask that each remaining name be reproduced against the `a8bc84f` guards;
  this cycle did (section 2). **Find out on the filings what the flag was reacting to and say so.** Remember the TSLA
  note (check a `scale_shift` above 2.0 for non-consecutive years before reading it as a step), the SNOW note
  (`restatement_shift` is not called by the triage pipeline), and the RIVN note (a `share_count_shift` of None is a
  missing element, not a stable count).

## 2. WHAT THE SCREEN RETURNS (tagged data, transcription only; operator rule 4)
This cycle pulled companyfacts fresh at ~19:42 EDT 2026-09-18. Scripts `_probe_screen.py` and `triage_repro.py`
(adapted from RIVN's), outputs `_probe_screen_output.txt` and `triage_repro_out.txt`, raw pull `companyfacts.json`, and
the triage code copy `floor_screen_a8bc84f.py`, all in `Test Runs/_research 2026-09-18 DJT/` (do not refetch
companyfacts unless you need a newer vintage). **Every figure is a prompt to read the filed statement, not a finding:**
- **a8bc84f guard order on facts filed by 2026-09-01:** `share_count_shift` **1.281** (passes, inside 0.75-1.50);
  `scale_shift` **2.809** (FIRES), on FY2022 $1.47M to FY2023 $4.13M, consecutive years; `filed_years` 5;
  `owner_earnings` 3y D&A end -$76.1M, 3y capex end -$74.5M (no 5y window returned); `restatement_shift` (1.0, FY2023),
  a null and not a guard.
- Tagged revenue ($M), `RevenueFromContractWithCustomerExcludingAssessedTax` only: FY2022 1.47, FY2023 4.13, FY2024 3.62,
  FY2025 3.68.
- Tagged operating cash ($M): FY2021 -1.11, FY2022 -1.38, FY2023 -5.14, FY2024 -60.98, FY2025 +14.76.
- Tagged SBC ($M): FY2022 **0**, FY2023 **0**, FY2024 107.4, FY2025 59.2 (the zeros may be the SBC-of-zero defect the
  RESUME STATE note describes; check the face).
- Tagged D&A ($M): FY2022 0.06, FY2023 0.06, FY2024 2.93, FY2025 7.42. Tagged capex ($M): FY2022 0.08, FY2023 0.002,
  FY2024 5.03, FY2025 0.57.
- `working_capital_flag` FIRES: *"ONE LINE MADE THE CASH: AccountsPayableAndAccruedLiabilities moved 182% of 2025 OCF"*.
  The FY2025 positive operating cash is therefore a prompt to read the cash-flow statement, not a turn.
- `stale_filer` newest annual 2025-12-31. `acquisition_flag` None. `da_discontinuity_flag` None.
- dei `EntityCommonStockSharesOutstanding`: 277,067,396 (2025-07-31) ... 276,731,315 (2026-02-25, 10-K) ...
  **277,941,274 (2026-08-07, 10-Q filed 2026-08-10)**. `EntityPublicFloat` $2.49bn (2024-06-28), $2.9bn (2025-06-30).
- **This registrant is a former SPAC** (the CIK dates from 2021; the operating company combined into it). The FY2021-22
  operating-cash figures may be the shell's, while FY2022 revenue may be the operating company's reported through a
  later filing. Establish which entity each tagged year belongs to before any of it is used (the RGTI run found shell and
  target years under colliding keys).
The questions these raise are yours to answer: what the 2.8x revenue step is made of and whether it is a perimeter at
all; what the reporting entity was in each year; what produced FY2024's -$61M and FY2025's +$14.8M of operating cash;
what the balance sheet holds, what it earns, and whether that income is operating earnings of the business; whether SBC
resolves AND is complete on the face every year; and what (c) is for a business with almost no plant.

## 3. THINGS I BELIEVE FROM MEMORY - UNVERIFIED. Verify each on a filing or discard it; never carry one forward
My knowledge has a cutoff that predates the newest filings, and a past brief of mine quoted a price increase that
appeared in no filing (ELF). Each is a hypothesis with the document that would settle it:
- The business combination with Digital World Acquisition Corp. closed in late March 2024; pre-combination history is in
  the S-4/proxy and the 8-K super 8-K (settle on the 8-K Item 2.01 and the FY2024 10-K's basis-of-presentation note:
  which entity is the accounting acquirer).
- The operating products are the Truth Social platform, a streaming service (Truth+), and a financial-services brand
  (Truth.Fi, with ETF/SMA products) (settle on the 10-K business section and the revenue disaggregation).
- In 2025 the company raised roughly $2bn-plus of equity and convertible notes to buy bitcoin as a treasury asset, and
  later took positions in or arrangements around a crypto token (settle on the 8-Ks, the debt note, the digital-assets
  note, and the share count effect of the convertibles and any pre-funded warrants).
- **A merger with TAE Technologies (a private fusion-energy company), announced around December 2025, as an all-stock
  combination.** If it exists and is live, this is a deal check that matters: whether DJT is the acquirer or the
  target, whether the quote is a spread, and what the forward company is against the filed one (the HHH shape) (settle
  on the 8-K Items 1.01/2.01, S-4, DEFM14A and the latest 10-Q subsequent-events note).
- Donald J. Trump holds a large stake, reportedly placed in a revocable trust; there were earnout shares on the
  combination (settle on the proxy's beneficial-ownership table, 13D/Forms 4, and the earnout note).
- SEC and other matters around the SPAC (DWAC settled with the SEC in 2023; related insider-trading cases) (settle on
  the legal-proceedings note and the SEC releases; date each to when it became PUBLIC).
- Revenue is almost entirely advertising, and small relative to the market cap (settle on the revenue note).
Date each matter to when it became PUBLIC.

## 4. REQUIRED HANDLING (the project's standing rules; none of them is a hint about a verdict)
- **Write-early.** Copy the template to `Test Runs/2026-09-18 Run - DJT Trump Media.md` BEFORE fetching anything, commit
  it, then write each section as it closes and commit after every gate. Research files go in
  `Test Runs/_research 2026-09-18 DJT/`. **COMMIT WITH A PATHSPEC ONLY: write the message to a file and use
  `git commit -F <msgfile> -- <path> <path>`.** Never `git add X && git commit` (it commits the whole shared index and has
  swept other sessions' files into wrong commits six times). `git add` a NEW file before the pathspec commit so it is
  tracked, then commit with the pathspec. Bash heredocs containing apostrophes fail in this environment: write scripts to
  the research folder. Commit trailer: `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. Also commit this brief,
  the two probe scripts and their outputs into the research folder with your first commit (companyfacts.json only if
  `.gitignore` allows; check it). **Do not commit image files.**
- **Sovereign**: strike it yourself from the US Treasury daily par yield curve, 30-year, dated
  (`python tools/sources.py` or the Treasury site; FRED DGS30 only as fallback). `tools/sources.sovereign()` has served a
  stale cached row three times; confirm the date on the row you use against the Treasury itself. Do not inherit the
  RIVN run's figure.
- **Price**: re-strike it yourself; aggregators are allowed for live quotes only and are flagged.
  `tools/sources.price()` returns an intraday price stamped with today's date although its docstring says "latest close";
  use a dated close and say which. Cross-check against a Form 4 price if one is recent.
- **Share count**: from the cover of the LATEST periodic filing (`python Screens/cover_shares.py DJT`, and read the cover
  itself), with the accession. Consider whether convertible notes, pre-funded or other warrants, earnout shares and
  unvested awards belong in the count at the price you strike, and state the answer either way.
- **SBC**: verify it RESOLVES and is COMPLETE on the face of the cash-flow statement for every year you use. Where SBC/OCF
  is high, [E3-70] asks what the options could have been sold for; the grant table is read by hand (source limit).
- **Deal check**: query EDGAR yourself for any live merger, tender or going-private (8-K Items 1.01/2.01, SC TO, S-4,
  DEFM14A, SC 13D). A live deal makes the quote a spread or changes which company the price buys (ROKU, HHH).
- **Owner earnings**: rebuild the width over every window the filed statements support, and both (c) ends, from the filed
  statements, never a net-income proxy. Say which windows do not exist and why. Report dollars, and a word, wherever the
  bottom sits near or below zero. Separate the operating business from the income or losses on the treasury assets and
  say which one owner earnings measures, with the ledger id that governs the choice. Show the payables contribution to
  FY2025 operating cash explicitly, both ways.
- **Hard sequence Q1 to Q5. STOP at the first question that is not IN.** UNRESEARCHED and UNKNOWABLE both close the file.
  Recent runs recorded later questions beneath a close under an explicit "RECORDED, NOT GOVERNING" banner; that is
  allowed, but no such section may carry entry language, and any valuation before Q1-Q4 all close IN is headed exactly
  `COMPUTATION — NOT A CLEARANCE`.
- **Q3**: pull the latest 8-K EX-99.1 earnings releases (or whatever the company furnishes instead) before scoring [E4-29]
  and [E4-22]'s flags (the CGNX companion rule). The honesty binary is [E5-16]; the incentive read is [E4-27] (NOT
  [E4-52], which is the lollapalooza row); [E5-22] is penalty size is not seriousness; [E4-34] is the four auditor
  questions; [E2-26] is candor. Read the proxy for what pay vests on and for related-party arrangements.
- **Q2**: a moat is a relative claim. The same-metric competitor row is a CONVENTION the framework keeps (the corpus's
  own test is pricing conduct plus returns on capital [E3-43]; [E3-28] is the monitoring quote, not the row's authority).
  Build it from competitors' own filings (full-text search via `tools/sources.py fts_count()` needs the bare zero-padded
  10-digit CIK or it silently returns zero). [E3-03] is the franchise definition; [E2-44] the pricing-power and
  low-capital pair; [E4-04] the rapid-change exclusion; [E3-46] return on capital; [E2-45] the grizzlies question; [E2-58]
  the cost-advantage exception; [E2-59] commodity product plus over-capacity; [E3-62] who keeps the gains; [E4-37] the
  price-rise test; [E4-23] key-person dependence.
- Q1 asks whether you can understand how THIS business makes money on its filings; if the price is paying for something
  the filings do not show as a business (a treasury asset, a pending combination), say what the filings show and what
  they do not, with [E3-31] and [E4-46] as the RIVN and TSLA runs used them, checked against the ledger.
- The TSMC corpus tension against [E4-04] (the 2023 meeting) is an OPEN operator question; if [E4-04] matters here, apply
  v4 as written and note the tension, do not resolve it.
- Every ledger id you cite must exist in `principle_ledger.csv` and say what you cite it for (check it; the acceptance
  test cannot catch a real id cited for the wrong thing).
- The subject has political prominence. The framework's questions are about the business, its filings and its
  management's conduct as filed; keep the file to that, quote documents, and leave out commentary that no filing supports.
- No em dashes in your own prose (verbatim quotes and the required `COMPUTATION — NOT A CLEARANCE` heading excepted).
- Nothing about the framework changes: no ledger rows, no edits under `Framework/`. Corrections go in dated notes.
- Never present the framework as proven to beat the market (operator rule 7).

## 5. THE FOLD - do all six steps yourself (queue file, `## THE FOLD`)
1. Register entry at the TOP of `## COMPLETED FROM THE QUEUE` in `Screens/WATCHLIST RUN QUEUE.md`, in the same form as
   the RIVN entry: price, share count and cover accession, cap, sovereign, and the PASS/FAIL line naming the question
   that closed the file. **Count the register from its heading line to `## THE WRITE-EARLY PROTOCOL`** (entries
   beginning `- **TICKER (`; the ten backfill entries under the `### REGISTER BACKFILL` heading count; RIVN's fold said
   105 on this rule) and state the new total.
2. Strike DJT in the wave 5 table (`~~DJT~~`), and add a short dated note beside the table on what the "perimeter or
   restatement" label turned out to be for DJT (the RIVN note is the model; do not edit history).
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
