- **CLX (The Clorox Company), 2026-09-25 - FAIL at Q2 (OUT, ON THE BUSINESS).**
  Q1 IN. `Test Runs/2026-09-25 Run - CLX Clorox.md`. **WAVE 7, name 30 of 218. Register entry 162**
  (re-derived by line index inside the slice from the line-exact `## COMPLETED FROM THE QUEUE` heading at
  index 501 to `## THE WRITE-EARLY PROTOCOL` at 13218 in the HEAD blob: **161 before, 162 after, CLX first, no
  duplicate**; not inherited). Price **$81.80** (close 2026-09-24, aggregator, flagged; Yahoo chart endpoint,
  raw response in the research folder; the lowest close in the two-year series) x **120,931,005 shares**, **one
  class** ($1.00 par; preferred authorized, none issued), quoted from the **10-K cover for FY2026, filed
  2026-08-07, accession `0000021076-26-000034`** (*"As of July 22, 2026, there were 120,931,005 shares of the
  registrant’s common stock outstanding."*; no periodic report filed since) = cap **$9,892M**. **THE CAP FLAG:
  neither figure was wrong; they were struck a year apart.** The screen set its $12,426M cap (about $101.6 a
  share on the FY2025 cover count) against the FY2025 10-K's *"approximately $ 19.9 billion"* float at
  2024-12-31, when the close was $162.41; the FY2026 cover's *"approximately $ 12.2 billion"* at 2025-12-31 ties to
  120,890,241 shares x $100.83 = $12,189M. REPORTED, NOT PATCHED: the guard in `Screens/regen_queue.py` compares a
  cap and a float of different dates. Sovereign **5.47% USD** (US Treasury daily par yield curve, 30 Yr,
  **09/24/2026**, issuing authority, struck fresh, raw CSV saved; **FRED not used**). Filings read: **10-K FY2026
  `0000021076-26-000034`** (Clorox files MD&A and statements as the 10-K's Exhibit 99.1), 10-Ks FY2025 / 2024 /
  2023 / 2022 / 2021 (reused from the CL run's folder, accessions re-checked) and FY2020 / 2019 / 2017 / 2016 /
  2014 / 2013 / 2011 / 2010 fetched for the sixteen-year series, the 10-Qs for December 2025 and March 2026, every
  8-K since the FY2025 10-K including the FY2026 earnings release (`0000021076-26-000028`), and the DEF 14A of
  2025-10-07 (`0001552781-25-000311`). FY2026 operating cash **$612M** rebuilt from its own lines. **THE
  PERIMETER MOVED THREE WAYS**: GOJO (Purell) bought 2026-04-01 for **$2,147M**, debt-funded ($1.5bn of May 2026
  notes; S&P to BBB); VMS (2024-09-10) and Argentina (March 2024) sold; P&G's 20% of Glad bought for **$476M
  through operating cash**. **SOURCE FINDING, REPORTED NOT PATCHED: SEC companyfacts had not ingested the FY2026
  10-K on 2026-09-25, seven weeks after filing**, which is why the screen's `newest_filing` reads 2025-06-30 and
  why `tools/run.py CLX` still prices FY2023-25 without a warning. Competitor rows: five company-level peers
  reused from the CL run's row (PG, CL, CHD, KMB, KVUE; Clorox cells re-derived), plus **Reynolds (Hefty)** from
  its 10-Ks and **Reckitt (Lysol)** from its annual reports and H1 2026 RNS, transcribed by two sub-agents
  (`peers_reyn/REYN_ROW.md`, `peers_reckitt/RECKITT_ROW.md`).

  **Q2 OUT. [E3-03] criterion (2) is not shown for the company.** Pre-tax return on average net tangible
  operating assets was 44-97% ex-charges in every year FY2011-FY2026, **recorded as the strongest evidence
  against the verdict, but every branded staple in the row earns the same, including General Mills and J.M.
  Smucker, closed OUT at Q2**. The separating tests fail on the registrant's own words: **[E2-44]** (price
  *"without fear of significant loss of either market share or unit volume"*): *"lower shipments of Clorox ®
  liquid bleach due to the February 2015 price increase"*, Glad *"primarily due to a price increase"* (FY2014)
  and *"wider price gaps"* (FY2019), and FY2023 *"Volume decreased by 10% versus the prior year primarily due to
  pricing actions"* on +16 points of price, the most price and the most lost units in the row that year (PG +9 /
  -3, CL +10 / -0.5). **[E4-55]**: organic units about 94 in FY2026 on FY2019 = 100 (about 98 on the FY2025-26
  mean) after about 28 points of price. **[E4-47]**: EBIT $921M in FY2026 against $1,121M in FY2019 in nominal
  dollars, and the FY2027 outlook: *"Gross margin is expected to be about 42%, reflecting higher-than-normal
  inflationary headwinds and negative mix more than offsetting the benefits from cost savings."* The cleaning
  segment is the one leg with rising earnings (segment EBIT 570 in FY2019, 719 / 840 / 678 FY2024-26), and
  Reckitt says of its direct rival: *"Lysol has gained more than 700bps of market share in the US since 2019"*
  (AR 2021), *"continued market share momentum"* (H1 2026). Glad's branded rival earns more on its bags (REYN
  Hefty Waste & Storage adjusted EBITDA 27.6-28.4% against Clorox Household's EBITDA-equivalent 15-20%) and makes
  store brands too. [E4-04]'s perimeter close refused in writing; [E3-47] weighed in writing against the
  cleaning segment and the sixteen-year return record; the contrast with the CL run (IN, narrow) stated.

  **Recorded beneath the close, without verdicts.** **Q3**: no conduct matter found in the filings read ([E5-17]
  cap); [E4-29] does not fire (no EBITDA outside the covenant); **adjusted free cash flow of $881M adds back the
  $476M Glad buyout** against $612M of operating cash; the *"Digital capabilities and productivity enhancements
  investment"* excluded from adjusted earnings five years running ($439M, [E2-57], [E5-33]); IGNITE targets raised
  in 2021 to 3-5% sales growth with net sales down since; PSUs paid 133% for FY2023-25 on economic profit, which
  excludes that cycle's $803M of impairment and divestiture losses; about $1.9bn put into Burt's Bees, RenewLife
  and Nutranext against about $1.15bn written down or lost on sale; FY2025 buybacks at about $147 a share; CEO
  stepping down for health reasons, successor not yet filed. **Q4**: owner earnings, no net-income proxy, sixteen
  years both (c) ends: 3y **$461-482M** ($620-641M with the buyout added back), 5y **$549-557M** ($644-652M), 10y
  **$698-725M** ($746-773M), 16y **$639-656M**; SBC resolves every year; judged (c) about D&A. GOJO roughly pays its
  own financing on the filed pro forma. Net debt about $4.9bn, interest cover about four times, dividend about 100%
  of recent owner earnings. **COMPUTATION - NOT A CLEARANCE**, no box: yield about 6.3% to 7.8% (4.7% counting the
  buyout as a cost) against 5.47%; value roughly $6-8bn at the ~10% floor with no growth against $9.9bn; windage
  ONE. No survival shape claimed; no index row added.
  **`python tools/check_framework.py` PASS, zero phantoms (60 distinct ledger ids in the run file, every one
  resolved against `principle_ledger.csv`).** **No alert armed and no PORTFOLIO.md row** (failed on the business,
  the QLYS ruling); reversal conditions in words at Q6, headed by **organic units back above FY2019 on a two-year
  mean with price/mix not negative**. **The brief's error**: it read the stale `newest_filing` as a screen built
  before the FY2026 10-K (the 10-K predates the screen; companyfacts is the cause), compressed the CL row's volume
  to "-10 then -7" (FY2023 and FY2026, not consecutive), and its perimeter prior named disposals but not GOJO or
  the $476M buyout. My own errors, caught before commit: an unsupported "loss-making or low-margin" for the
  disposals, "four of five" for three of five, and three sums first typed from memory. Commits `063170b` (claim),
  `d8f8489` (Step 0, Q1), `ad3e896` (Q2), `7dbba04` (beneath the close), and the fold commit, all with pathspecs
  except the fold's queue file, staged from the HEAD blob plus this entry only; the CRM re-look's uncommitted hunks
  in this file and `tools/alerts.json` were left in the working tree, not staged. **WAVE 7 IS 30 OF 218. 188 NAMES
  REMAIN. Next in the order file: CVS.**
