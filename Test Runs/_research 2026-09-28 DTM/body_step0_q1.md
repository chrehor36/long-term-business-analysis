## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**. DTM bills US customers in dollars under US contracts and FERC tariffs, borrows in
dollars and pays dollar dividends. Its equity-method pipelines NEXUS and Vector reach Ontario; the 10-K's
comprehensive-income line for foreign currency translation is $1M (2025) and $2M (2023), immaterial. Earnings
currency **USD**; no FX step.
- rate **5.49%** · date **09/25/2026** (the last posted business day; 09/26 and 09/27 are a weekend) · source
  **US Treasury daily par yield curve, 30-year, from the issuing authority**. `tools/_cache/sov_USD_treasury.csv`
  was deleted before `python tools/sources.py` ran, so the rate was fetched, not served from cache. FRED was not
  used. Struck fresh; not inherited from the brief or from the TCMD run.
- FX / ADR: not applicable.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes  [x] Item 1  [x] Item 1A
- **Annual report: Form 10-K for the year ended 2025-12-31, filed 2026-02-19, accession 0001842022-26-000003**
  (`dtm-20251231.htm`). Also read for the series and the carve-out: the 10-Ks for FY2021 (0001842022-22-000006),
  FY2022 (0001842022-23-000006), FY2023 (0001842022-24-000003) and FY2024 (0001842022-25-000003).
- **Newest periodic: Form 10-Q for the quarter to 2026-06-30, filed 2026-07-30, accession 0001842022-26-000009**
  (`dtm-20260630.htm`); and the 10-Q to 2026-03-31 (0001842022-26-000006).
- **Furnished releases, for [E4-29]**: 8-K filed 2026-07-30, accession 0001140361-26-030142, EX-99.1 and EX-99.2
  (Q2 2026 results); 8-K filed 2026-02-19, accession 0001140361-26-006115, EX-99.1 and EX-99.2 (FY2025 results).
- **Proxy: DEF 14A filed 2026-03-26, accession 0001140361-26-011280.**
- **Deal-shaped filings read**: 8-K filed 2024-11-19 (0001140361-24-047312, EX-99.1, the $1.2B Midwest pipeline
  purchase from ONEOK), 8-K filed 2024-12-31 (0000947871-24-001058, Item 2.01, the closing), 8-K filed 2021-07-01
  (0001193125-21-205933, the separation from DTE Energy).
- **Figures cross-checked against the filed statement.** The tagged `NetCashProvidedByUsedInOperatingActivities`
  for FY2025 is 867,000,000; the 10-K's Consolidated Statements of Cash Flows print *"Net cash and cash equivalents
  from operating activities | 867 | 763 | 798"* for 2025, 2024, 2023. Also checked line by line: depreciation and
  amortization 258 / 209 / 182, stock-based compensation 26 / 23 / 20, plant and equipment expenditures (426) /
  (350) / (772), and *"Acquisition accounted for as a business combination (and purchase price adjustment) | 10 |
  (1,198) | —"*. Every tag equals the printed figure.

**Price and shares.**
- Price **$122.28**, NYSE close **2026-09-25** (Friday), Yahoo chart endpoint via `tools/sources._chart`,
  `regularMarketTime` 2026-09-25 20:00 UTC checked. **Aggregator, used for the live quote only, flagged.**
- Shares **102,015,296**: the cover of the **10-Q for the quarter to 2026-06-30, filed 2026-07-30, accession
  0001842022-26-000009**, reads *"Number of shares of common stock outstanding as of June 30, 2026: [...] Common
  stock, par value $0.01 | 102,015,296"*; the balance sheet of the same filing reads *"102,015,296 and 101,673,925
  shares issued and outstanding as of June 30, 2026 and December 31, 2025"*. `python Screens/cover_shares.py DTM`
  returned the same count from the same accession. **One class**: 550,000,000 common authorised; preferred
  *"50,000,000 shares authorized, and no shares issued or outstanding"*. Nothing summed.
- **Market cap: $122.28 x 102,015,296 = $12,474.4M.**

**Deal check.** The filer list from 2021 to 2026-09-28 carries no S-4, DEFM14A, SC TO-T or 425. The deal-shaped
filings are DTM buying: the Millennium 26.25% interest from National Grid ($552M, closed 2022-10-07), the Clean
Fuels gathering asset ($12M, 2024-07-01) and the Midwest Pipeline Acquisition from ONEOK ($1.2B, closed
2024-12-31). **The quote is an owner-earnings price, not a spread.**

**Separation and perimeter, established before any window is used.** The FY2021 10-K, Note 1: *"For the periods
prior to the Separation, the Consolidated Financial Statements and Notes to Consolidated Financial Statements were
prepared on a carve-out basis using the consolidated financial statements and accounting records of DTE Energy."*
DTE distributed 96,732,466 DTM shares on 2021-07-01. So **2019, 2020 and the first half of 2021 are carve-out;
2022-2025 are the only four full standalone years.** Two perimeter changes sit inside the series: the Haynesville
gathering business (Blue Union and LEAP, bought 2019-12-04 from Momentum Midstream and Indigo Natural Resources
for a fair value of *"$ 2.74 billion"*, *"$ 2.36 billion paid in cash and an estimated $ 380 million of contingent
consideration"*, $2,296M on the tagged 2019 acquisition line; FY2021 10-K Note 4: *"The acquisition was financed
by DTE Energy."*), and the three ONEOK pipelines, whose cash flows begin
on 2025-01-01. **No cash-flow year before 2025 carries the current perimeter**, and 2019 carries almost none of
the Haynesville business.

---
## THE SCREEN ROW — carried UNLABELLED, a set of claims and not a finding

From `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`: `cap_m 13214 · oe_bottom_m 270 · oe_top_m 570 ·
spread 1.109 · yield_bottom 0.0205 · vs_sovereign -0.033 · growth_required 0.0795 · level_shift 1.42 "no step" ·
best_year_dep 0.048 · level_shift_oe 1.04 · best_year_dep_oe 0.099 · years_filed 7 · acq_note "NET CASH INFLOW on
the acquisition line ($1,208M, 9% of cap) - cash acquired exceeded cash paid, so the CONSID[...]" · spread_caveat
"4-construction width only [...] rebuild it [E4-25]" · newest_periodic 2026-06-30`. Each field used is reproduced
or refuted below; the list of screen errors is gathered at the end of the file.

**The acquisition note is refuted at Step 0, from the filed statement.** The tagged
`PaymentsToAcquireBusinessesNetOfCashAcquired` is **+1,198 for 2024 and −10 for 2025**; the 10-K prints the same
line as *"(1,198)"* in 2024 and *"10"* in 2025. A positive value of a PAYMENTS tag is an outflow. **2024 was a
$1,198M cash payment** (the ONEOK pipelines, financed, in the FY2024 10-K's words, by *"4,168,750 common shares
[...] net proceeds of approximately $406 million"*, *"5.800% senior secured notes due 2034 in aggregate principal
amount of $650 million"* and the revolver), and **2025 was a $10M purchase-price adjustment received**. $1,208M is
the difference of the two tagged values (1,198 − (−10)), which is no quantity at all. There was no net cash inflow,
and no cash acquired exceeding cash paid. **Screen error.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics, in my own words.** DTM owns steel pipe, compressors and one storage field, and rents capacity in
them. It never owns the gas: it is paid to move or hold somebody else's molecule. Two kinds of rent.
- **Pipeline segment (55% of 2025 consolidated revenue; $370M of the $441M 2025 net income attributable to DTM,
  84%).** Long-haul interstate pipe (Guardian, Midwestern, Viking, Birdsboro wholly owned; Millennium 52.5%,
  NEXUS 50%, Vector 40% as equity-method joint ventures), the Washington 10 storage complex in Michigan, an
  intrastate Michigan system, and three "gathering lateral" pipes that carry gas from a producing basin to a
  big pipe (LEAP and Stonewall and Bluestone). Customers reserve capacity for years and pay a fixed monthly
  demand charge whether or not gas flows: *"approximately 92% of our Pipeline revenue was generated under firm
  service revenue contracts and approximately 99% of the revenue of our unconsolidated joint ventures was
  generated under firm service revenue contracts."* The joint ventures' profit reaches DTM as
  *"Earnings from equity method investees"*, $138M in 2025.
- **Gathering segment (45% of revenue; $71M of net income, 16%).** Small-diameter pipe laid into producers'
  acreage in the Haynesville (Blue Union) and the Marcellus/Utica (Susquehanna, Appalachia, Ohio Utica, Tioga)
  that collects gas at the wellhead. *"approximately 57% and 36% of our Gathering segment revenue was generated
  under firm revenue contracts and flowing gas, respectively"* — the flowing-gas part is paid by the unit and
  rises and falls with the producer's volume.
- Revenue = (reserved capacity x a demand charge) + (flowing volume x a fee). Cost = operating the pipe, property
  tax, interest on the debt that built it, and the capital that keeps it running. The commodity price passes
  through except for fuel retained in kind.

**The scarce input this business controls.** Rights of way and FERC certificates for pipe already in the ground
between specific supply basins and specific markets (Chicago, Wisconsin and Minnesota utilities, Michigan and
Ontario, Gulf Coast LNG), plus contractual acreage dedications in the gathering systems. A rival must obtain its
own certificate and right of way to compete for the same path, and the filer says the Northeast approval process
*"has become increasingly challenging"*.

**Will the fundamentals look broadly the same in ten years?** The mechanism will: pipe, reservation charge,
volume fee. The customers who fill the gathering systems drill wells that decline (the filer's own risk factor:
*"If new supplies of natural gas are not obtained to replace the natural decline in volumes from existing supply
basins in our areas of operation [...] the overall volume of natural gas gathered, transported and stored on our
systems would decline"*), and that is a Q2 and Q4 question, as it was for HESM. The business is *"relatively
simple and stable in character"* **[E3-31]** on its mechanism; the magnitudes are not settled here.

**The perimeter is part of understanding it.** The company that trades today has existed as a standalone
registrant since 2021-07-01; its present pipeline perimeter since 2025-01-01. Q1 is answered on the mechanism,
which is the same across both changes; the windows that span them are handled at Q4.

**VERDICT: [x] IN**

---
