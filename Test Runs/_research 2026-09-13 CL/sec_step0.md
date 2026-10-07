---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.35%** · date **09/11/2026** · source (issuing authority) **US Treasury daily par yield curve, 30-year**, struck fresh by
  `tools/sources.py` `sovereign("USD")` on Sunday 2026-09-13 (09/11 is the latest business day). Not inherited from any run or brief.
  Beside it, for the record only: EUR 3.826% (ECB AAA curve SR_30Y, 2026-09-10) and JPY 3.995% (Japan MOF, 2026-09-10), same call.
- FX: none in the quote (NYSE, USD) or in the reported statements (USD).

**THE CURRENCY CHOICE, argued rather than assumed.** The framework asks for *"the currently observed rate for the currency the
business earns in"*. Colgate earns in many currencies, and the filing says so plainly:
- *"Approximately two-thirds of the Company's Net sales are generated from markets outside the United States, with approximately 45 %
  of the Company's Net sales coming from emerging markets"* (10-K FY2025, Note 14). The segment note gives United States net sales of
  $3,596M (Oral, Personal and Home Care) plus $3,062M (Pet Nutrition) = **$6,658M, 32.7% of $20,382M** in 2025. Latin America is $4,776M
  (23.4%), Europe $2,962M (14.5%), Asia Pacific $2,814M (13.8%), Africa/Eurasia $1,172M (5.8%).
- Pre-tax income by location: United States $1,419M / International $1,640M (2025, after the $919M skin-health impairment); $1,084M /
  $2,872M (2024); $692M / $2,700M (2023). **International is 73-80% of pre-tax income in the two years without the impairment.**
- *"This is particularly acute in hyper-inflationary economies, including Argentina, Nigeria and Türkiye"* (10-K FY2025 and 10-Q Q2
  2026, Outlook). Highly inflationary subsidiaries remeasure non-monetary assets at historical rates, with remeasurement adjustments
  *"included in Net income attributable to Colgate-Palmolive Company"* (Note 2).
- $1,234M of the $1,288M of year-end cash sat in foreign subsidiaries (10-K FY2025, liquidity).

**Choice: USD, for three reasons from the documents, with the limit stated.**
1. **The owner-earnings stream this run measures is a US-dollar stream.** Every figure in Q4 is translated at its own year's rates, so
   every devaluation of the real, the peso, the lira or the naira is already inside it (2024 Latin America: foreign exchange **-13.7%**
   against organic growth +16.8%; Africa/Eurasia -12.1% against +13.3%; 10-K FY2025 organic reconciliation). Setting a USD-translated
   cash stream against a local-currency bond yield would put local inflation into the comparison a second time. The bond must be in the
   unit the owner's cash is counted and paid in: dividends are declared in dollars per share, buybacks are paid in dollars, and the euro
   notes are hedged as net investment hedges and reported in dollars (Note 7, net investment hedges $4,278M notional).
2. **The corpus names this bond:** *"What is the risk-free interest rate (which we consider to be the yield on long-term U.S. bonds)?"*
   **[E4-01]**.
3. **No issuing-authority feed is configured for the currencies that would compete** (BRL, MXN, INR, ARS, TRY, NGN, CNY), and a blended
   "earnings-weighted" sovereign would be a new number, which the tooling rule forbids.
- **The limit, stated:** a local-currency reading would raise the bond bar in Colgate's largest foreign markets, not lower it, and the
  ~10% floor **[E4-28]** does not move with any sovereign. The USD choice therefore cannot flatter the name at Q5. The currency exposure
  itself is a business fact and is carried to Q2 (pricing that only recovers devaluation) and Q4 (translation), not into the rate.
- **Jurisdiction [E3-66]:** the registrant is a Delaware corporation listed on the NYSE; the operating assets sit in over 80 countries,
  including Russia (*"challenges to our ability to repatriate cash from Russia"*) and Venezuela (below). Carried to Q4.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes (restructuring, goodwill and intangibles, debt, fair value and
  hedges, capital stock and stock compensation, ESOP, retirement plans, income taxes, EPS, commitments and contingencies, segments,
  leases, supplier finance, supplemental income statement and balance sheet), Item 1 (distribution, competition, customers), Item 1A,
  Item 2, Item 5 repurchases
- documents · date · accession no. (newest 10-K and 10-Q confirmed from EDGAR `submissions.json`, CIK **0000021665**, not from the brief):
  - **10-Q for the quarter ended 2026-06-30**, filed 2026-07-31, `0000021665-26-000042` (primary: balance sheet, six-month cash flows,
    equity, restructuring, contingencies, segments, MD&A); **10-Q Q1 2026**, filed 2026-05-01, `0000021665-26-000023`; 10-Qs for 2025
    Q1-Q3 `0000021665-25-000020`, `0000021665-25-000041`, `0000021665-25-000053`
  - **10-K FY2025**, filed 2026-02-23, `0000021665-26-000006`; and the 10-Ks FY2024 `0000021665-25-000008`, FY2023 `0000021665-24-000003`,
    FY2022 `0000021665-23-000007`, FY2021 `0000021665-22-000003`, FY2020 `0000021665-21-000007`, FY2019 `0000021665-20-000004`, FY2018
    `0000021665-19-000003`, FY2017 `0000021665-18-000003` (and its 10-K/A `0000021665-18-000006`); every cash-flow statement 2015-2025
    read off these
  - **DEF 14A** 2026 (filed 2026-03-25, `0001308179-26-000136`), 2025 (`0001308179-25-000223`), 2024 (`0001308179-24-000306`)
  - **8-K Exhibit 99 earnings releases** (Colgate numbers its release exhibit 99): Q2 2026, 2026-07-31, `0000021665-26-000041`; Q1 2026,
    2026-05-01, `0000021665-26-000022`; Q4 2025, 2026-01-30, `0000021665-26-000003`; Q3 2025, 2025-10-31, `0000021665-25-000052`; Q2 2025,
    2025-08-01, `0000021665-25-000040`; Q1 2025, 2025-04-25, `0000021665-25-000019`; and every release back to Q4 2020
    (`0001157523-21-000105`), for the guidance record at Q3
  - **Other 8-Ks read:** Item 8.01 segment recasts 2026-03-17 (`0000021665-26-000010`) and 2024-10-25 with its 8-K/A of 2025-01-24
    (`0000021665-24-000042`, `0000021665-25-000002`); Item 8.01 note offerings 2025-11-10, 2025-05-02, 2023-03-01, 2022-08-03 and -09,
    2021-11-05 and -10; Item 8.01 mini-tender response 2021-07-22; Item 7.01 2021-06-10; Items 2.05 (restructuring) 2025-08-01,
    2025-10-31, 2026-05-01; Items 5.02 2025-05-29, 2026-03-12, 2026-04-09
- **figure cross-checked against the filed statement:** FY2025 net cash provided by operations **$4,198M**: companyfacts
  (`NetCashProvidedByUsedInOperatingActivities`) and `tools/run.py` read 4,198; the FY2025 10-K consolidated statement of cash flows
  reads *"Net cash provided by operations | 4,198 | 4,107 | 3,745 |"*. **Match.** Also: capital expenditures *"( 564 ) | ( 561 ) |
  ( 705 )"* and stock-based compensation *"155 | 135 | 122"* match `run.py` to the million; six-month 2026 operations $1,742M read off
  the 10-Q face.
- **Share count:** 10-Q cover, `0000021665-26-000042`: *"Common stock, $1.00 par value | 797,172,829 | June 30, 2026"*. **Cross-checks:**
  Q1 2026 10-Q cover 800,189,310 (March 31, 2026); 10-K cover *"There were 801,548,028 shares of Colgate-Palmolive Company Common Stock
  outstanding as of January 31, 2026"*; Note 8 table 801,239,524 outstanding and 664,466,836 in treasury at 2025-12-31, summing to the
  1,465,706,360 issued that both balance sheets show; Q2 2026 basic weighted average 799.4M. The fall of 4.1M shares in six months sits
  against $590M of treasury stock acquired, less shares issued for options and units (10-Q equity statement). `Screens/cover_shares.py CL`
  printed **797,172,829** from the same accession: **correct for this filer** (the NVDA CIK defect did not recur).
- **Single class, read from the filing:** the only equity line is common stock; *"The Company has the authority to issue 50,262,150
  shares of preference stock"* (Note 8), and neither balance sheet carries a preference line or amount, so none is outstanding. The ESOP's
  *"6,646,688 ... shares of common stock ... outstanding and issued to the Company's ESOP, which have all been released and allocated to
  participant accounts"* (Note 9) are common shares already inside the count, and the ESOP *"had no outstanding borrowings from the
  Company"*.
- **Splits, from the filings:** *"All per share amounts and numbers of shares outstanding were adjusted for the two-for-one stock split of
  the Company's common stock in 2013"* (10-K FY2017). Issued shares are 1,465,706,360 at 2025-12-31 and at 2026-06-30, so no split after
  the measurement date (Yahoo's split history agrees: last event 2:1, May 2013). Split factor after 2026-06-30 = **1.0**.
- **Price:** **US$86.80, close of 2026-09-11** (Yahoo via `tools/sources.py:price()`, and the same close in the daily series;
  **aggregator, flagged: live quote only**).
- **Market cap:** 86.80 × 797,172,829 × 1.0 = **US$69,194.6M** (`run.py` 69.19bn, same inputs).

### THE DEALS, READ BEFORE PRICING
`deal_filings(CIK)` returned **no deal form and no 8-K Item 1.01** since the 10-K of 2026-02-23; `deal_note` returned an empty string.
**Because `deal_filings()` does not read Item 8.01 or 7.01 (the NVDA finding), every 8-K since 2021 was opened by hand:**
- **Nothing makes Colgate a target or party to a live merger.** No DEFM14A, S-4, 425, SC TO or SC 14D9 appears in the submissions index.
  The 8.01 filings are two segment recasts, six note offerings and one response to a 2021 "mini-tender". **The quote is not a spread.**
- **Acquisitions by Colgate (perimeter), from the 10-Ks:** Prime100 (Care TopCo, Australia) closed 2025-04-30 for AU$471M ($301M), *"Pro
  forma results of operations have not been presented as the impact on the Company's Consolidated Financial Statements is not
  material"*; Red Collar Pet Foods (*"three dry pet food manufacturing plants in the United States"*) 2022-09-30, *"a purchase price, as
  adjusted, of $719"*, and Nutriamo (an Italian wet pet food plant, *"additional capacity for the Hill's wet pet nutrition diets"*)
  2022-04-28; Filorga 2019 (payment for acquisitions $1,711M); EltaMD and PCA SKIN 2018 ($728M); hello 2020 ($353M). Disposal: the South
  Pacific laundry detergent business, 2015. **Handled at Q4:** each is small against the cash-flow base, and the two 2022 plant purchases
  are Hill's capacity bought as businesses, which Q4 treats as capital, not as perimeter.
- **Venezuela, verified rather than assumed:** *"Effective December 31, 2015, the Company concluded it no longer met the accounting
  criteria for consolidation of its Venezuelan subsidiary ("CP Venezuela") and began accounting for CP Venezuela using the cost method of
  accounting. As a result, effective December 31, 2015, CP Venezuela's net assets and operating results are no longer included in the
  Company's Consolidated Financial Statements"* (10-K FY2017, Note 2), with a $1,084M *"Charge for Venezuela accounting change"* in 2015's
  cash-flow reconciliation. The FY2025 10-K repeats: *"since December 31, 2015, the local operating results from our Venezuela operations
  have not been included in our Consolidated Financial Statements."* **The perimeter changes at the end of 2015, so no owner-earnings
  window in this run starts before 2016 without saying so.**
- **Officer and board changes:** a Chief Operating Officer, Americas hired from Danone (effective 2025-06-16); the Chief Legal Officer
  retiring with an internal successor (2026-06-01); a director leaving to be CEO of Kraft Heinz (2026-03-12). The Chairman and CEO,
  Noel Wallace, is unchanged.

### THE SKIP REASON, TESTED FIRST: a TOOLING ARTEFACT, the same class as AMZN and NVDA
The wave 5 row says *"capex unresolved [E5-20]: build (c) by hand from the filing"*. Tested in two parts (scripts and output:
`skip_test.py`, `skip_test_out.txt`, `floor_screen_a8bc84f.py` extracted with `git show a8bc84f:Screens/floor_screen.py`).
- **(a) The screen as it stood when the label was written** (`a8bc84f`, 2026-09-01 22:15), run on today's companyfacts, returns
  **`CAPEX_UNRESOLVED`**. Its `CAPX_TAGS` list `PaymentsToAcquirePropertyPlantAndEquipment` first, and its `annual()` stops at the first
  tag with any data. **Colgate used that tag for FY2011-FY2022 only**; FY2023-FY2025 capex sits under `PaymentsToAcquireProductiveAssets`
  (FY2014-FY2025), which the old code never reached. The last five operating-cash years (2021-2025) therefore carried capex for two of
  five years, neither window resolved, and the row went unpriced.
- **(b) The current screen prices it.** `floor_screen.owner_earnings()` today: `{'5y_da': 2,871.2, '5y_capex': 2,833.2, '3y_da': 3,278.7,
  '3y_capex': 3,269.3}` ($M). `python tools/run.py CL` (no `--write`, `runpy_out.txt`): three-year mean **$3,233M-$3,315M**, five-year
  $2,811M-$2,893M; yield 4.67%-4.79% on three years, 4.06%-4.18% on five. The current screen's other flags are quiet
  (`working_capital_flag`, `capex_funding_flag`, `lease_capex_flag` and `da_discontinuity_flag` all None); `acquisition_flag` names
  $1,102M of acquisition cash in its window.
- **Which kind of gap: a tooling artefact, not a presentation gap.** The capex line never left the face of the cash-flow statement:
  *"Capital expenditures"* is its own investing line in every statement 2015-2025 and in the 10-Q. Only the tag changed. **Whether
  depreciation is an adequate measure of what must be spent to stay in place [E5-20] is a separate question, asked at Q4 on the filing.**

**Tooling notes from Step 0 (recorded, no tool edited):**
1. **The two capex tags disagree by $1M for FY2020** (409 under `PaymentsToAcquirePropertyPlantAndEquipment`, 410 under
   `PaymentsToAcquireProductiveAssets`); the FY2020 and FY2021 10-Ks both print **410**. The current screen returns 409 for 2020, so where
   both tags exist the union still prefers the older tag. Immaterial here ($0.2M on a five-year mean); the direction of the preference is
   the note.
2. **`deal_filings()` saw nothing, correctly, but for the NVDA reason could not have seen an 8.01 announcement**; every 8-K was opened.
3. **Exhibit naming:** Colgate's releases from Q2 2024 are filed as `q22026pressreleasetables.htm` and similar, numbered exhibit 99,
   not 99.1; a fetcher matching `ex99` in the file name misses every release after Q1 2024. Found by this run's own first fetch and fixed
   in the research script, not in any tool.
4. **companyfacts carries ESOP tags** (`EmployeeStockOwnershipPlanESOPCompensationExpense`, FY2008-FY2025) that no SBC tag list reads;
   whether they carry an expense outside the SBC line is tested at Q4.
