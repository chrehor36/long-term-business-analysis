# BRIEF - META (Meta Platforms), wave 5, overnight cycle 2026-09-18 ~22:00 EDT

You are running ONE company through the framework, from scratch, unattended. The operator is asleep and nobody will
answer a question. Repository: `C:\Users\chreh\OneDrive\Documents\BRK`. Work in it directly.

## 0. READ FIRST (in this order)
1. `CLAUDE.md` (operator protocol, prime rules, tools).
2. `Framework/THE FRAMEWORK v4.md` - the governing document. If a rule is not in it, it is not in force.
3. `Test Runs/_TEMPLATE - Company Run.md` - the run surface.
4. For what a finished run looks like: `Test Runs/2026-09-18 Run - AEHR Aehr Test Systems.md` (the previous name in
   wave 5, finished about an hour before this brief) and `Test Runs/2026-09-18 Run - BX Blackstone.md`. Read their
   structure, self-audit, brief-defects section and REGISTER block. Their findings belong to their companies.
   **Prior runs that put META in a competitor row:** `Test Runs/2026-09-06 Run - GOOGL Alphabet.md`,
   `Test Runs/2026-09-06 Run - MSFT Microsoft.md`, `Test Runs/2026-09-13 Run - AMZN Amazon.md`,
   `Test Runs/2026-09-07 Run - PINS Pinterest.md`, and the 2026-07-15 5-pack. They show where to look for a row. Nothing
   in them is evidence about META until you re-read it on META's own filing and cite the accession; a figure a run of
   another company computed for META is transcription, not a finding.
5. `Screens/WATCHLIST RUN QUEUE.md`: the sections `THE WRITE-EARLY PROTOCOL`, `THE FOLD`, `WRITING A BRIEF`, the
   `#### WAVE 5` table and its dated notes, and the top two entries of `## COMPLETED FROM THE QUEUE` (the format).
6. `Screens/SURVIVAL SHAPES - index.md` - name survival shapes by their number; add a new one there only when folding.
7. `Screens/RESUME STATE 2026-09-12 - Opus session, note for Fable.md` sections 3-5: tooling changes, errors not to
   repeat, and the source limits already tested (do not re-attempt them).

## 1. THE NAME, AND WHY IT IS HERE
- Ticker META, Meta Platforms, Inc., **CIK 0001326801** (companyfacts entityName "Meta Platforms, Inc."; confirm against
  the SEC `company_tickers.json`). Calendar fiscal year. 10-K/10-Q filer. Latest 10-K: FY2025, filed 2026-01-29 (per
  the dei public-float fact). Latest periodic: 10-Q for the period ended 2026-06-30, filed 2026-07-30, accession
  0001628280-26-050705. Confirm both from `submissions.json`.
- **No screen row in `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`.** The only screen rows on disk are in the
  2026-07-15 S&P 500 mechanical screen (`Screens/2026-07-15 SP500 Mechanical Screen - full results.csv`):
  `META,...,MktCap_M 1672140.00,NI_latest_M 60458.00,NI_lowest5yr_M 23200.00,YieldOnLowest 1.39%` - a net-income screen
  from a withdrawn generation (operator rule 5 forbids a net-income proxy for owner earnings). Transcription only.
- **Skip reason from the wave 5 table, a prompt to read and never a verdict:** *"no share count from dei: read the
  cover"*. Probe result: META's companyfacts carries **only `EntityPublicFloat`** under dei, no
  `EntityCommonStockSharesOutstanding` at all, so `share_count_shift` returns None and the screen could not price it.
  **Find out on the filings why (two share classes on the cover is the obvious hypothesis; check it) and say so.**
  META is the **first** name in its wave 5 row (META, DASH, PATH, PUBM, BZFD); the fold's dated note should open the
  row's tally.

## 2. WHAT THE SCREEN RETURNS (tagged data, transcription only; operator rule 4)
This cycle pulled companyfacts fresh at ~22:05 EDT 2026-09-18. Script `_probe_screen.py`, output
`_probe_screen_output.txt`, raw pull `companyfacts.json` and the triage code copy `floor_screen_a8bc84f.py` are in
`Test Runs/_research 2026-09-18 META/` (do not refetch companyfacts unless you need a newer vintage). **Every figure is a
prompt to read the filed statement, not a finding:**
- **Cover (`python Screens/cover_shares.py META`)**: 10-Q filed 2026-07-30, accession 0001628280-26-050705: Class A
  2,205,128,509; Class B 342,377,716. The tool prints the sum 2,547,506,225 and labels it **"arithmetic sum, NOT a share
  count"**. Whether A and B are economically equivalent is a judgment from the charter; read it (conversion, dividend and
  liquidation rights, votes) before you add them. Diluted weighted shares tagged 2,564-2,565M in 2026.
- a8bc84f guards on facts filed by 2026-09-01: `share_count_shift` None (missing element, per the RIVN note, not a
  pass), `scale_shift` 1.372, `restatement_shift` (1.0, FY2017), a null. No acquisition, working-capital, D&A, capex-
  funding or lease-capex flag fired.
- `owner_earnings` (screen): 5y D&A end $50.4bn, 5y capex end $25.6bn; 3y $60.6bn / $30.5bn. **The two ends differ by
  roughly 2x, and the gap is the whole question [E5-20] asks.**
- Tagged ($bn), FY2019-25: OCF 36.3, 38.7, 57.7, 50.5, 71.1, 91.3, 115.8. Capex 15.1, 15.1, 18.6, 31.4, 27.3, 37.3, 69.7.
  D&A 5.7, 6.9, 8.0, 8.7, 11.2, 15.5, 18.6. SBC 4.8, 6.5, 9.2, 12.0, 14.0, 16.7, 20.4. Revenue 70.7, 86.0, 117.9, 116.6,
  134.9, 164.5, 201.0. Net income 18.5, 29.1, 39.4, 23.2, 39.1, 62.4, 60.5.
- Tagged `FinanceLeasePrincipalPayments` $2.5bn FY2025, $1.8bn H1 2026: finance-lease capex is capex the capex tag does
  not see. Check it.
- Tagged `LongTermDebt` $18.4bn (FY2023) to $28.8bn (FY2024) to $58.7bn (FY2025) to $83.7bn (2026-06-30).
  `PaymentsForRepurchaseOfCommonStock` $26.3bn FY2025, **$0.0 in both 2026 quarters tagged**. Dividends $5.3bn FY2025.
- Check the SBC face resolves and is complete every year you use; SBC/OCF is in the high teens, so [E3-70] applies.
The questions these raise are yours to answer: what the share count is; how much of the capex is maintenance and how
much is a build whose return is not yet filed; what the finance leases and any off-balance-sheet data-centre
arrangements add; what the segments earn; and what the business earns for owners after paying its people in stock.

## 3. THINGS I BELIEVE FROM MEMORY - UNVERIFIED. Verify each on a filing or discard it; never carry one forward
My knowledge has a cutoff that predates the newest filings. Each is a hypothesis with the document that would settle it:
- Class B carries ten votes per share, converts to Class A one-for-one, and gives Mark Zuckerberg voting control
  (settle on the charter exhibit, the 10-K risk factors and the DEF 14A beneficial-ownership table).
- Two segments: Family of Apps (advertising on Facebook, Instagram, Messenger, WhatsApp) and Reality Labs, with Reality
  Labs losing on the order of $15-20bn a year for several years (settle on the segment note, every year you use).
- FY2025 net income included a large one-time non-cash tax charge tied to 2025 US tax legislation, in the third quarter
  (settle on the income-tax note and the Q3 2025 release). If so, FY2025 net income understates the year.
- Meta took a large minority stake in Scale AI in 2025, and entered a joint venture or financing arrangement with an
  outside investor for a large Louisiana data centre (Hyperion) that may sit off its balance sheet (settle on the 10-K/
  10-Q notes on equity investments, variable interest entities, leases and commitments, and any 8-K). If real, say how
  (c) and the perimeter treat each.
- Capex guidance for 2026 is far above 2025 (settle on the latest EX-99.1 releases).
- The FTC's monopolisation case over Instagram and WhatsApp was decided at trial; EU Digital Markets Act decisions and
  fines exist (settle on the legal-proceedings note of the latest 10-Q).
- Competitors for advertising: Alphabet, Amazon, TikTok/ByteDance, Snap, Pinterest, Microsoft and others (settle on the
  10-K competition section, which may or may not name them; the AEHR run found its 10-K named nobody).

## 4. REQUIRED HANDLING (the project's standing rules; none of them is a hint about a verdict)
- **Write-early.** Copy the template to `Test Runs/2026-09-18 Run - META Meta Platforms.md` BEFORE fetching anything,
  commit it, then write each section as it closes and commit after every gate. Research files go in
  `Test Runs/_research 2026-09-18 META/`. **COMMIT WITH A PATHSPEC ONLY: write the message to a file and use
  `git commit -F <msgfile> -- <path> <path>`.** Never `git add X && git commit`. `git add` a NEW file before the
  pathspec commit so it is tracked. **Check that each edit succeeded before committing.** Bash heredocs containing
  apostrophes fail in this environment: write scripts to the research folder. Commit trailer:
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. Commit this brief, the probe script, its output and the
  a8bc84f copy with your first commit (companyfacts.json left untracked). **Do not commit image files.**
- **Sovereign**: strike it yourself from the US Treasury daily par yield curve, 30-year, dated. `tools/sources.
  sovereign()` has served a stale cached row six times; confirm the date against the Treasury itself. Do not inherit
  the AEHR run's figure.
- **Price**: re-strike it yourself; aggregators for live quotes only, flagged. `tools/sources.price()` returns an
  intraday price stamped with today's date; use a dated close and say which. Cross-check against a recent Form 4.
- **Share count**: from the cover of the LATEST periodic filing, read on the cover itself, with the accession. Decide
  the A/B treatment from the charter and say why.
- **SBC**: verify it RESOLVES and is COMPLETE on the face of the cash-flow statement for every year you use. [E3-70]:
  the grant table is read by hand (source limit).
- **Deal check**: query EDGAR yourself for any live merger, tender or going-private (8-K Items 1.01/2.01, SC TO, S-4,
  DEFM14A, SC 13D).
- **Owner earnings**: rebuild the width over every window the filed statements support, and both (c) ends, from the
  filed statements, never a net-income proxy. Finance-lease principal and any off-balance-sheet build are part of what
  (c) must see. Say what the working-capital increment is made of. Report dollars and a word wherever the bottom sits
  near or below zero. (c) is a disclosed judgment [E5-20].
- **Hard sequence Q1 to Q5. STOP at the first question that is not IN.** UNRESEARCHED and UNKNOWABLE both close the
  file. Later questions may be recorded beneath a close under an explicit "RECORDED, NOT GOVERNING" banner, with no
  entry language, and any valuation before Q1-Q4 all close IN is headed exactly `COMPUTATION — NOT A CLEARANCE`.
- **Q3**: pull the latest 8-K EX-99.1 earnings releases before scoring [E4-29] and [E4-22]'s flags. The honesty binary
  is [E5-16]; the incentive read is [E4-27] (NOT [E4-52], which is the lollapalooza row); [E5-22] is penalty size is not
  seriousness; [E4-34] is the four auditor questions; [E2-26] is candor. Read the proxy for what pay vests on, and
  compare what management said about spending and new products in past releases with what later filings reported.
- **Q2**: a moat is a relative claim. The same-metric competitor row is a CONVENTION the framework keeps (the corpus's
  own test is pricing conduct plus returns on capital [E3-43]; [E3-28] is the monitoring quote, not the row's
  authority). Build it from competitors' own filings (foreign filers on their 20-F/annual report). Full-text search via
  `tools/sources.py fts_count()` needs the bare zero-padded 10-digit CIK or it silently returns zero. [E3-03] is the
  franchise definition; [E2-44] the pricing-power and low-capital pair; [E4-04] the rapid-change exclusion; [E3-46]
  return on capital; [E2-45] the grizzlies question; [E2-58] the cost-advantage exception; [E2-59] commodity product
  plus over-capacity; [E3-62] who keeps the gains; [E4-37] the price-rise test; [E4-23] key-person dependence. Physical
  series the company files (users, ad impressions, average price per ad) bear on pricing conduct; read them, as the
  GOOGL run read paid clicks and cost-per-click under [E4-55].
- Q1 asks whether you can understand how THIS business makes money on its filings; if the price is paying for something
  the filings do not show as a business, say what the filings show and what they do not, with [E3-31] and [E4-46] as the
  RIVN, TSLA and DJT runs used them, checked against the ledger.
- The TSMC corpus tension against [E4-04] (the 2023 meeting) is an OPEN operator question; if [E4-04] matters here,
  apply v4 as written and note the tension, do not resolve it.
- Every ledger id you cite must exist in `principle_ledger.csv` and say what you cite it for.
- No em dashes in your own prose (verbatim quotes and the required `COMPUTATION — NOT A CLEARANCE` heading excepted).
- Nothing about the framework changes: no ledger rows, no edits under `Framework/`. Corrections go in dated notes.
- Never present the framework as proven to beat the market (operator rule 7).

## 5. THE FOLD - do all six steps yourself (queue file, `## THE FOLD`)
1. Register entry at the TOP of `## COMPLETED FROM THE QUEUE` in `Screens/WATCHLIST RUN QUEUE.md`, in the same form as
   the AEHR entry: price, share count and cover accession, cap, sovereign, and the PASS/FAIL line naming the question
   that closed the file. **Count the register from its heading line to `## THE WRITE-EARLY PROTOCOL`** (entries
   beginning `- **TICKER (`; the backfill entries count; AEHR's fold said 108 on this rule) and state the new total.
   Check for a duplicate ticker while counting.
2. Strike META in the wave 5 table (`~~META~~`), and add a short dated note beside the table on what the "no share
   count from dei" label turned out to be for META (the AEHR/BX notes are the model; do not edit history).
3. Narrative fold into `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`.
4. `tools/alerts.json` bands and a `PORTFOLIO.md` row ONLY if all four business gates clear. If the file closes at
   Q1-Q4, record the reversal condition in words instead.
5. `python tools/check_framework.py` must PASS before the fold commit.
6. Pathspec commit.
Also add a new survival shape to `Screens/SURVIVAL SHAPES - index.md` only if you name one.

## 6. WHAT TO RETURN TO ME
A short report: the verdict line (which question closed the file and on which ledger ids); price with date and source;
share count with accession and the A/B treatment; cap; sovereign with date; the owner-earnings range; what the skip
reason turned out to be; the register count after your entry; check_framework result; the commit hashes; and every
defect you found in this brief. If you hit a usage or rate limit, commit whatever is on disk with a pathspec commit and
say exactly where you stopped.
