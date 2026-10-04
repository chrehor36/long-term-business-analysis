# Company Run — Colgate-Palmolive Company (CL) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*WAVE 5 of the watchlist queue, row "capex unresolved [E5-20]: build (c) by hand from the filing". Colgate had no row in the master queue or the triage CSV; it was never priced by the screen. Read as UNLABELLED. Research, scripts and extracted filing text: `Test Runs/_research 2026-09-13 CL/`. Run unattended under the write-early protocol; each section is appended as it closes.*

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

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

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Where the money is, 2025 (10-K FY2025 Note 14) and the trailing twelve months to 2026-06-30** (TTM = FY2025 − H1 2025 + H1 2026, from the
10-K and the Q2 2026 10-Q; $M). The 2025 segment table is the pre-recast five-region form; the 10-Q is the recast four-region form, so
the TTM is shown only at the two product segments.

| 2025 | net sales | segment operating profit | margin | share of segment profit | capex | D&A |
|---|---|---|---|---|---|---|
| North America | 4,045 | 784 | 19.4% | 15.6% | 65 | 123 |
| Latin America | 4,776 | 1,411 | 29.6% | 28.1% | 141 | 106 |
| Europe | 2,962 | 748 | 25.3% | 14.9% | 63 | 66 |
| Asia Pacific | 2,814 | 760 | 27.0% | 15.1% | 80 | 80 |
| Africa/Eurasia | 1,172 | 255 | 21.8% | 5.1% | 12 | 10 |
| **Oral, Personal and Home Care** | **15,769** | **3,958** | **25.1%** | **78.8%** | **361** | **385** |
| **Hill's Pet Nutrition** | **4,613** | **1,064** | **23.1%** | **21.2%** | **88** | **144** |
| Corporate (incl. $919 impairment, $99 ERISA, $13 restructuring, $9 acquisition costs; overhead $677) | | (1,717) | | | 115 | 101 |
| **Total** | **20,382** | **3,306** | **16.2%** | | **564** | **630** |

| TTM to 2026-06-30 | net sales | operating profit |
|---|---|---|
| Oral, Personal and Home Care | 15,769 − 7,746 + 8,297 = **16,320** | recast basis only in the 10-Q (H1 2026 $2,112M vs H1 2025 $1,968M) |
| Hill's Pet Nutrition | 4,613 − 2,275 + 2,389 = **4,727** | H1 2026 $549M vs H1 2025 $523M |
| Total | **21,047** | 3,306 − 2,156 + 1,980 = **3,130** (incl. H1 2026 restructuring charges of $305M pre-tax) |

**The cost structure, from the filed statements (10-Ks FY2017-FY2025, Note 17 and the MD&A):**

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| net sales $M | 15,195 | 15,454 | 15,544 | 15,693 | 16,471 | 17,421 | 17,967 | 19,457 | 20,101 | 20,382 |
| gross margin (logistics in SG&A) | 60.0% | 60.0% | 59.4% | 59.4% | 60.8% | 59.6% | 57.0% | 58.2% | 60.5% | 60.1% |
| advertising % of sales | 9.4% | 10.2% | 10.2% | 10.8% | 11.8% | 11.6% | 11.1% | 12.2% | 13.5% | 13.3% |
| GAAP operating margin | 26.0% | 24.0% | 23.8% | 22.6% | 23.6% | 19.1% | 16.1% | 20.5% | 21.2% | 16.2% |
| return on avg. net tangible operating assets, GAAP op. profit **[E2-43]** | 96.9% | 89.8% | 91.2% | 88.6% | 98.5% | 84.7% | 61.5% | 76.0% | 91.0% | 79.0% |
| same, goodwill/intangible impairments added back | | | | | | 99.2% | 76.8% | | | 101.0% |

*Gross profit, operating profit, advertising and assets from companyfacts, newest vintage, checked for 2025 and 2024 against the filed
income statement and Note 17 (advertising $2,703M and $2,720M). Net tangible operating assets = total assets − cash − current marketable
securities − goodwill − other intangibles − operating right-of-use assets − (current liabilities − debt due within one year − current
lease liabilities); 2025 $4,128M. Script `ntoa.py`, output `ntoa_out.md`. Shipping and handling is in SG&A: *"If such costs had been
included as a component of Cost of sales, the Company's Gross profit margin would have been lower by 880 bps in 2025 and 2024"* (10-K
FY2025). Impairments: $571M (2021) and $721M (2022) per the FY2023 10-K cash-flow reconciliation; $919M (2025).*

- **Unit economics in my own words, no management language:**
  1. **Oral, Personal and Home Care.** Colgate makes low-priced goods that are used up and bought again every few weeks (toothpaste,
     toothbrushes, bar and liquid soap, deodorant, dish liquid, surface cleaner, fabric softener) in its own plants in dozens of countries,
     and sells them to retailers, wholesalers and distributors, which pay within about two months (*"typically less than 60 days"*). After
     the cost of the goods it keeps about 60 cents of each sales dollar; it then spends about 9 cents moving the goods to customers, about
     13 cents on advertising, and more on trade promotions that are deducted from sales before they are reported. Around a quarter of each
     sales dollar is left as regional operating profit, before a corporate layer of overhead, research and restructuring.
  2. **Hill's Pet Nutrition.** The same shape in dog and cat food, sold through pet specialty retailers, veterinarians and online, with a
     therapeutic line (Prescription Diet) alongside everyday food (Science Diet) and, since 2025, Australian fresh food (Prime100). It
     earned 23.1% of sales in 2025 and uses more plant per dollar of sales: segment capex of $301M in 2023 against $101M of depreciation,
     plus three US dry pet food plants bought from Red Collar for $719M in 2022.
  3. **The capital under it is small and it recycles fast.** Net tangible operating assets were about $4.1bn against $20.4bn of sales in
     2025; working capital is negative (*"(7.0)% in 2025"* of net sales, 10-K liquidity); capex has run near 3% of sales with the stated
     plan for 2026 *"approximately 3.0% of Net sales"*. On that base the pre-tax GAAP operating return on average net tangible operating assets
     has been 76.0%-98.5% in every year of the decade except 2022 (61.5%), which is why a company with near-zero book equity ($54M at 2025) still pays $1.8bn of dividends a
     year: the equity was bought back, not lost.
  4. **Where the profit comes from, by place:** two-thirds of sales and 73-80% of pre-tax income (2023-2024) come from outside the United
     States. Latin America is the largest profit region (28.1% of segment profit at a 29.6% margin), and it is also where sales are most
     exposed to devaluation (Step 0; carried to Q2 and Q4).
- **The scarce input this business controls:** *(a)* the trademarks themselves (*"We consider trademarks to be material to our business
  ... Our rights in these trademarks endure for as long as they are used and/or registered"*, 10-K Item 1) and the consumer habit attached
  to them; the company reports its own share of the global toothpaste market at **41.3%** and of manual toothbrushes at **32.4%** for 2025
  (Nielsen-based, with its stated limits: *"market share data is currently not generally available for certain retail channels, such as
  eCommerce or certain discounters"*); *(b)* distribution and manufacturing already in place in more than 200 countries and territories,
  with plants in over 80; *(c)* for Hill's, a therapeutic pet food range sold through veterinarians. **Whether any of these has no close
  substitute in the customer's mind is the Q2 question, not assumed here.** The filing itself names the counter-forces: *"vigorous
  competition worldwide, including from strong local competitors (including private label competition)"*, and key retailers *"some of
  which exercise greater bargaining strength than we do"*; Walmart is *"approximately 11%"* of net sales.
- **Will the fundamentals look broadly the same in ten years?** **Yes, for the products:** people will brush their teeth, wash, clean
  and feed pets with goods of this kind, and nothing in the filings describes a technology replacing them. The 10-K of FY2017 describes
  the same two segments, the same categories and the same channels as the 10-K of FY2025. **What is changing is the route to the
  shopper** (*"consumers continue to shop online and increasingly through social commerce and with the assistance of AI"*, retailers'
  *"exclusive access to valuable first-party consumer data"*, *"AI-aided category pricing pressures and algorithms"*) and the currency
  map. Those bear on relative position and on pricing, which is Q2, and are carried there rather than used to fail or excuse Q1.
- **Outside the two segments:** the skin-health acquisitions (EltaMD and PCA SKIN 2018, Filorga 2019, and their successors) are a small
  part of sales and have been written down by $2,211M in three charges (2021, 2022, 2025); Venezuela has been outside the statements
  since 2015. Both are understood as what they are and carried to Q3 (capital allocation) and Q4 (perimeter), not to Q1.

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  The business is legible from the filings without management's words, is *"relatively simple and stable in character"* **[E3-31]**,
  and the scarce inputs can be named. No "unverified" or "provisional" caveat attaches: every figure above is from a named 10-K or 10-Q.
  The market-share figures are the company's own Nielsen-based estimates with stated limits; they describe position, and Q1 does not rest
  on them.

---
## RESUME NOTE — 2026-09-18

*The session that opened this file was killed by a session limit at 17:09 on 2026-09-13, with **Step 0 (`d4398ab`) and Q1
(`0c3de6e`) committed** and nothing written below the Q1 verdict. The scheduler then stopped: `_scheduler_trace.log` shows every
hourly cycle from 2026-09-14 13:35 through 2026-09-15 09:35 ending `RATE LIMITED (exit 1)`, and no cycle at all until
2026-09-18 08:10. **Nothing touched this file or its research folder in those five days.** This session resumed on 2026-09-18
and wrote Q2 onward. Step 0 and Q1 above are history and are not edited (operator rule 6); anything they need is corrected in
the addendum at the foot of this file. **The price and the sovereign in Step 0 were struck on 2026-09-13 and are five days
stale; [E4-15] asks for the currently observed rate, so both are struck again at Q5 and both pairs are recorded there. Every
computed figure at Q5 uses the fresh pair.***

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

- **Needed or desired [x]** · **no close substitute [x] for Oral Care and Pet Nutrition (67% of 2025 sales), [ ] not shown for
  Personal Care and Home Care (33%)** · **not price-regulated [x]**
- **Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04]** **No, on both.** The basis of the
  advantage is a set of trademarks and a consumer habit that the 10-K says *"endure for as long as they are used and/or
  registered"*, plus plants and distribution in place in over 80 and over 200 countries. The FY2017 10-K describes the same two
  segments, the same categories and the same channels as the FY2025 10-K. The spending defends **the same** trademarks; it does
  not buy their replacement, which is the distinction the framework draws between Coca-Cola's advertising and Mitsui's Rhodes
  Ridge, and which **[E5-23]** (*"certainly should be working at improving your own moat and defending your own moat all of the
  time"*) and **[E3-49]** (*"a permanent obsession"*) prescribe for **every** moat. No **[E3-51]** wave is under this: toothpaste
  is not a technology whose generation turns over. Manager-dependence is answered at the bottom of this section, not assumed.
- **Primary moat metric, filing-sourced, and its trend.** Colgate reports one, every year, in the same sentence of the MD&A:
  **its share of the global toothpaste market.** Read across twelve 10-Ks, each figure from the year's own filing:

| full year | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | YTD Q2-2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| global toothpaste share | 44.4% | **44.7%** | 44.0% | 43.3% | 42.0% | 41.1% | 39.8% | **39.4%** | 39.8% | 41.1% | 41.4% | 41.3% | 41.3% |
| global manual toothbrush share | 33.4% | **34.7%** | 33.1% | 32.6% | 32.3% | 31.6% | 31.1% | **30.9%** | 31.7% | 31.5% | 32.2% | 32.4% | 32.7% |

  *Each cell is the number in that fiscal year's own 10-K MD&A (FY2014 "was 44.4% for full year 2014" through FY2025
  "was 41.3% for the full year 2025, down 0.4 share points from full year 2024"); the last column is the 10-Q for the quarter
  ended 2026-06-30, `0000021665-26-000042`, "41.3% on a year-to-date basis, up 0.2 share points" and "32.7% ... up 0.6 share
  points". **The limit is the company's own:** "All market share references represent the percentage of the dollar value of
  sales of our products, relative to all product sales in the category in the countries in which the Company competes and
  purchases data (excluding Venezuela from all periods) ... market share data is currently not generally available for certain
  retail channels, such as eCommerce or certain discounters ... we have not verified the accuracy or completeness of the data"
  (10-K FY2025, "Market Share Information"). **It is a DOLLAR share, not a unit share**, so it is flattered by the same price
  increases measured below.*

  **Trend, stated without decoration: the moat narrowed for six years and has re-widened for four, and it is still 3.4 points
  below its 2015 level in toothpaste and 2.3 below it in toothbrushes.** Over the same span advertising rose from **9.4% of
  sales (2016) to 13.3% (2025)**, which is 3.9 points more of every sales dollar spent to hold a smaller share. **[E4-32]** asks
  for the moat *"widened every year"* as *"the primary criterion of a great business"*; on the company's own primary metric that
  is **not satisfied** across the decade, and it is satisfied across 2022-2025 only.

### THE PHYSICAL SERIES — [E4-55], because dollar revenue flattered by pricing is how a shrinking franchise hides
Colgate files volume, net selling price and foreign exchange as separate components of net sales growth every year. Cumulative
sums of the **filed** components, 2016-2025, each cell transcribed from that year's own 10-K MD&A sentence
(`_research 2026-09-13 CL/resume/q2_org_out.md` carries the source sentence beside every cell; arithmetic in `resume/q2_sums.py`):

| scope | sum volume 2016-2025 | sum net selling price | sum FX | price + FX | sum volume 2021-2025 | sum price 2021-2025 |
|---|---|---|---|---|---|---|
| **Worldwide** | **+7.7** | **+38.0** | **-20.4** | **+17.6** | +1.2 | +29.5 |
| Oral, Personal and Home Care | **+2.9** | +35.7 | -24.7 | +11.0 | -1.6 | +27.2 |
| Hill's Pet Nutrition | **+31.7** | +49.1 | **-3.4** | **+45.7** | +17.2 | +35.1 |
| North America | +9.7 | +12.9 | -0.2 | +12.7 | **-9.3** | +12.9 |
| Latin America | -7.2 | **+76.8** | **-56.2** | +20.6 | +3.3 | +51.3 |
| Europe | +18.2 | +11.0 | -0.5 | +10.5 | -3.8 | +17.5 |
| Asia Pacific | -4.6 | +17.2 | -16.8 | **+0.4** | -0.6 | +14.2 |
| Africa/Eurasia | +3.1 | **+76.2** | **-62.6** | +13.6 | +4.1 | +52.2 |

*Six cells were spot-checked back to the filed sentence and all six matched (FY2016 Latin America, FY2019 Hill's, FY2020 Europe,
FY2022 Africa/Eurasia, FY2023 Africa/Eurasia, FY2025 North America). **Two cells the draft left blank are filled here from the
filing, and the draft is corrected on the record:** Latin America 2018, which the extractor missed because the FY2018 10-K splits
the sentence in two, "Net sales in Latin America decreased 7.5% in 2018 to $3,605 . Volume declines of 2.5% and negative foreign
exchange of 6.5% were partially offset by net selling price increases of 1.5% ."; and Africa/Eurasia 2023, which the FY2023
10-K writes as "Net sales in Africa/Eurasia were flat in 2023, as volume growth of 4.5% and net selling price increases of 13.0%
were offset by negative foreign exchange of 17.5%." Asia Pacific 2017 and 2018 price are 0.0 because both sentences say net
selling prices "were flat"; they are not missing cells and no `?` has been treated as a zero.*

**What the physical series says.** Dollar sales rose 34% over the decade, from $15,195M to $20,382M. **Units, as the company
counts them, rose about 7.7 points in ten years, and in the Oral, Personal and Home Care segment, which is 77% of sales, about
2.9 points in ten years.** That is Precision Steel's shape in miniature **[E4-55]**: *"This decline in physical volume is a
serious reverse ... Nor do we expect another sharp rise in prices ... holding dollar volume roughly level despite a precipitous
drop in physical volume."* Colgate's units did not drop precipitously; they did not grow either. The growth in the decade was
price.

**And the price was largely devaluation recovery, not [E2-44] pricing power.** Split the price by currency regime:
- **Soft-currency regions.** Latin America priced **+76.8** points against foreign exchange of **-56.2**; Africa/Eurasia
  **+76.2** against **-62.6**. In both, price recovered roughly 80-85% of the currency loss and no more. The 10-K names the
  mechanism: *"This is particularly acute in hyper-inflationary economies, including Argentina, Nigeria and Türkiye."*
- **Hard-currency regions.** North America **+12.9** points of price in ten years (about 1.2% a year), Europe **+11.0** (about
  1.0% a year), Asia Pacific **+17.2** against FX of -16.8, so **price plus FX in dollars of +0.4 points across ten years**.
- **And in the home market the last two years are price GIVEN BACK:** North America net selling price **-1.9% in 2024** and
  **-0.2% in 2025**, with volume -1.4% in 2025 and the segment's cumulative volume **-9.3 points over 2021-2025**, while
  advertising ran at 13.5% and 13.3% of sales. **[E4-37]** is the metric for this: *"you can almost measure the strength of a
  business over time by the agony they go through in determining whether a price increase can be sustained ... it's not a great
  business when you have to have a prayer session before you raise your prices a penny."* Two consecutive years of negative net
  selling price in the largest developed market, on the filed record, is the agony reading. **It is a downgrade signal on that
  segment, and it is carried to Q6 as the monitoring metric the framework says it is.**

**The counter-evidence, given its full weight.** In 2022 and 2023 Colgate put through **+9.5%** and **+10.0%** of worldwide net
selling price, and its global toothpaste share went **39.4% (2021) to 39.8% (2022) to 41.1% (2023)**, with worldwide volume
-2.0% then -0.5%. That is **[E2-44]** criterion (1) passing at the global level and in the hardest test the decade offered:
prices raised sharply *"without fear of significant loss of either market share or unit volume"*. The North American reading and
the worldwide reading of the same years point opposite ways, and both are in this file.

### THE SECOND QUESTION ABOUT THE BUSINESS IS A NUMBER — [E3-46], [E2-43]
Pre-tax GAAP operating return on average net tangible operating assets (definition and script in Q1; `ntoa.py`, `ntoa_out.md`):
**96.9% (2016), 89.8, 91.2, 88.6, 98.5, 84.7, 61.5, 76.0, 91.0, 79.0% (2025)**, and 99.2%, 76.8% and 101.0% in 2021, 2022 and
2025 with only the goodwill and intangible **impairments** added back (assets the measure already excludes). *"the best
businesses, by definition, are going to be businesses that earn very high returns on capital employed over time"* **[E3-46]**.
**[E2-44]** criterion (2), *"an ability to accommodate large dollar volume increases in business ... with only minor additional
investment of capital"*, is met without argument: $20,382M of sales stand on $4,128M of net tangible operating assets, working
capital is negative (*"(7.0)% in 2025"* of net sales), and capex has run near 3% of sales with FY2026 planned at
*"approximately 3.0% of Net sales"*.

**THE COMPETITOR ROW — required [E3-28].** *"I can't be an intelligent owner of a business unless I know what all the other
businesses in that industry are doing."* Same metrics, same construction, each company's own five most recent fiscal years,
every figure from a filing on disk in `_research 2026-09-13 CL/peers/`.

| company | fiscal years | operating margin, by year | return on avg. net tangible operating assets | organic volume, by year | price (or price/mix), by year | advertising % of sales | gross margin |
|---|---|---|---|---|---|---|---|
| **Colgate-Palmolive** | FY21-25 (Dec) | **19.1 / 16.1 / 20.5 / 21.2 / 16.2** (ex-impairment 22.4 / 20.1 / 20.5 / 21.2 / 20.7) | **84.7 / 61.5 / 76.0 / 91.0 / 79.0** (ex-impairment 99.2 / 76.8 / - / - / 101.0) | **+1.0 / -2.0 / -0.5 / +3.1 / -0.4** | **+3.5 / +9.5 / +10.0 / +4.4 / +2.1** | **11.6 / 11.1 / 12.2 / 13.5 / 13.3** | 59.6 / 57.0 / 58.2 / 60.5 / 60.1 *(shipping in SG&A)* |
| Procter & Gamble | FY21-26 (Jun) | 23.6 / 22.2 / 22.1 / 22.1 / 24.3 / 22.7 | **91.7 / 85.2 / 83.0 / 81.5 / 84.6 / 77.8** | +3 / +2 / -3 / 0 / +1 / 0 | +1 / +4 / +9 / +4 / +1 / +1 | 10.8 / 9.9 / 9.8 / 11.4 / 10.9 / 11.7 | 51.2 / 47.4 / 47.9 / 51.4 / 51.2 / 50.2 |
| Unilever (20-F, IFRS, EUR) | 2023-25 | 17.4 / 16.8 / 17.9 | not computed (IFRS balance sheet, different tag set) | +1.1 / +3.1 / +1.5 (underlying volume growth) | +6.5 / +1.2 / +2.0 (underlying price growth) | not disclosed as a line | not on the same basis |
| Haleon (20-F, IFRS, GBP) | 2023-25 | 1,996 / 2,206 / **2,412** GBPm; **21.9% in 2025** | not computed (IFRS) | +0.7 in 2025 (volume/mix) | +2.3 in 2025 | not disclosed as a line | not on the same basis |
| Kenvue | FY23-25 (Dec) | 16.3 / 11.9 / 16.0 | 89.3 / 63.9 / 78.3 | **-2.7 / -1.2 / -2.3** | +7.7 / +2.7 / +0.1 | not disclosed as a line | 56.0 / 58.0 / 58.1 |
| Church & Dwight | FY21-25 (Dec) | 20.8 / 11.1 / 18.0 / 13.2 / 17.4 | **106.5 / 59.3 / 98.4 / 72.0 / 116.1** | +1.0 / -5.1 / +0.9 / +3.3 / +0.8 | +3.3 / +6.5 / +4.4 / +1.3 / -0.1 | 11.1 / 10.0 / 10.9 / 11.4 / 11.4 *(marketing, includes advertising)* | 43.6 / 41.9 / 44.1 / 45.7 / 44.7 |
| Kimberly-Clark | FY21-25 (Dec) | 13.2 / 13.3 / 11.2 / 16.1 / 14.3 | 30.9 / 31.8 / 24.5 / 37.4 / 31.8 | -4 / -3 / -2 / +0.8 / +2.5 | +2 / +9 / +6 / +1.9 / -0.9 | 4.6 / 4.5 / 5.3 / 5.9 / 6.2 | 30.8 / 30.8 / 34.4 / 35.8 / 36.0 |
| Clorox | FY21-26 (Jun) | 12.6 / 10.6 / 5.5 / 7.2 / 15.2 / 13.6 | 67.6 / 46.3 / 25.4 / 31.2 / 66.8 | **+6 / -5 / -10 / -5 / +7 / -7** | +3 / +3 / **+16** / +5 / -1 / 0 | 10.8 (FY25) / 11.1 (FY26) | 43.6 / 35.8 / 39.4 / 43.0 / 45.2 / 42.3 |
| General Mills *(pet: Blue Buffalo)* | FY21-26 (May) | 17.3 / 18.3 / 17.1 / 17.3 / 17.0 / **4.8** | 396.6 / 261.8 / 205.1 / 186.4 / 108.3 / 25.8 *(distorted; see note)* | +2 / -1 / -4 / -3 / flat / -1 (tons) | +2 / +7 / +14 / +2 / -1 / -1 | 4.1 / 3.6 / 4.0 / 4.2 / 4.3 / 4.7 | 35.6 / 33.7 / 32.6 / 34.9 / 34.6 / 33.6 |
| J.M. Smucker *(pet)* | FY21-26 (Apr) | 17.3 / 12.8 / 1.8 / 16.0 / **-7.7** / 4.0 | 61.0 / 45.2 / 6.3 / 46.4 / -21.2 / 11.0 | not extracted | not extracted | not extracted | 39.2 / 33.8 / 32.8 / 38.1 / 38.8 / 33.5 |
| Freshpet *(pet, the attacker)* | FY21-25 (Dec) | -5.8 / -8.7 / -4.0 / +3.9 / **+6.9** | -5.1 / -6.8 / -3.1 / +3.3 / +5.9 | net sales **$425M to $1,102M** over the five years, +159%; decomposition not filed in the form used above | - | not disclosed as a line | 38.1 / 31.2 / 32.7 / 40.6 / 40.8 |

*Construction, so another reader can reproduce it: operating margin and return on net tangible operating assets are computed
from each filer's own companyfacts by `peers/peer_metrics.py`, using **the identical NTOA definition applied to Colgate in Q1**
(total assets less cash, current marketable securities, goodwill, other intangibles and operating right-of-use assets, less
current liabilities net of debt due within one year and current lease liabilities; operating profit is GAAP; the average of the
year's and prior year's NTOA is the denominator). **Where the tag was missing the filed statement was read instead:** PG does
not tag `GrossProfit`, so PG gross margin is (net sales less cost of products sold); Clorox does not tag `OperatingIncomeLoss`,
so Clorox operating profit is read off the filed income statement as gross profit less selling and administrative expenses,
advertising costs, research and development costs, loss on divestiture, pension settlement charge and goodwill, trademark and
other asset impairments (FY2021 3,199-1,004-790-149-329 = 927; FY2026 2,844-1,066-749-116 = 913). Unilever and Haleon are 20-F
filers on IFRS with no companyfacts on disk and no comparable tag set, so their operating margins are taken from the filed
statements and no NTOA is computed for them rather than a number being manufactured. **Protocol 4 cross-check on the peer side:**
PG's FY2026 filed income statement reads "NET SALES | $ | 87,032" and "OPERATING INCOME | 19,748", which is 22.7% and matches the
computed cell to the decimal. **The General Mills return column is flagged as distorted and carries no weight:** GIS's balance
sheet is so goodwill-heavy that the residual tangible denominator is small and unstable, which is a property of the definition,
not a finding about GIS. Volume, price, advertising and gross-margin cells for PG, GIS, CHD and KMB come from the transcription
sections `peers/SECTION_PG.md`, `SECTION_GIS.md`, `SECTION_CHD.md` and `SECTION_KMB.md`, each of which carries the filed sentence
and line number; the CLX, KVUE, UL and HLN cells were read from their filings in this session. **Gross margins are not on one
basis and are not compared:** Colgate reports shipping and handling in SG&A and says so, "If such costs had been included as a
component of Cost of sales, the Company's Gross profit margin would have been lower by 880 bps in 2025 and 2024", so Colgate's
60.1% is about 51.3% on the basis PG, CLX, CHD, KMB and GIS use.*

- **Peers named: ten, of roughly a dozen real competitors**, covering every category Colgate sells in: Oral Care (PG, Unilever,
  Haleon), Personal Care (PG, Unilever, Kenvue, CHD, KMB), Home Care (PG, Clorox, CHD, Unilever), Pet Nutrition (GIS/Blue
  Buffalo, Smucker, Freshpet).
- **Not rowed, and named as such, with what cannot be measured.** **Nestlé (Purina PetCare) and Mars (Royal Canin, Pedigree,
  Iams) are the two largest pet-food businesses in the world and neither is an SEC registrant**; no filing on disk gives either
  a revenue, a margin or a volume. The General Mills sweep across six 10-Ks returns **zero** hits for "Purina", zero for "Mars"
  as a whole word and zero for "Hill's", and every "Nestl" hit concerns the cereal joint venture. Also not rowed and not filled
  from memory: **Reckitt, Henkel, Beiersdorf, Lion, Dabur, Patanjali**, and the private-label manufacturers behind *"strong
  local competitors (including private label competition)"*. **Consequence, stated as the framework requires: the moat class for
  PET NUTRITION (23% of 2025 sales, 21.2% of reportable-segment operating profit) is PROVISIONAL**, because its two largest
  competitors cannot be measured from any primary filing. **The Oral Care row is not provisional**: the three multinational
  competitors in toothpaste (PG, Unilever, Haleon) are all here with filed figures, and the verdict rests there.
- **What the row shows.** On the corpus's own demonstration of a franchise, *"the ability to regularly price its product or
  service aggressively and thereby to earn high rates of return on capital"* **[E3-03]**, **Colgate and Procter & Gamble sit at
  the top of the row on returns on capital and nobody else is close on a comparable basis** (CL 61.5-91.0%, PG 77.8-91.7%, KMB
  24.5-37.4%, CLX 25.4-67.6%; CHD's 59-116% is real but on a much smaller and more acquisition-shaped base). On the **physical**
  series the row is uniformly poor and Colgate is at the better end of it: Kenvue's volume is negative in all three filed years,
  Clorox's is -10 in one year and -7 in the latest, Kimberly-Clark's was negative for three straight years, General Mills'
  tonnage is negative in four of six. **Every branded staple in this row grew dollars on price between 2021 and 2024 and gave
  some of it back in 2025.** Unilever is the one peer with positive volume in each of its three filed years, +1.1, +3.1, +1.5.
- **The row's limit [E3-61], stated:** *"In some businesses, the participants behave like a demented Kellogg. In other
  businesses, they don't ... I think you'd have to know the people involved."* The row places Colgate; it cannot say whether the
  three multinationals in toothpaste will keep pricing rationally or whether one of them will buy share. Munger says he has no
  model for it, and neither does this file.
- **Untapped pricing power [E3-33]: NOT CLAIMABLE, and the claim is refused.** **[E5-28]** scopes the class: *"If you name some
  business that has incredible pricing power, you're talking about a business that's a monopoly or a near monopoly."* A 41.3%
  **dollar** share of a category is not a near monopoly, and the direct filed evidence runs the other way: North American net
  selling price was **negative in 2024 and 2025**. A manager could not raise the return here simply by raising prices; the
  manager in the largest developed market has been cutting them.
- **[E2-53] the dominance class, which is where Colgate does qualify, and it is the strongest part of the case.** *"Once
  dominant, the newspaper itself, not the marketplace, determines just how good or how bad the paper will be. Good or bad, it
  will prosper."* Over the decade Colgate lost 3.4 points of toothpaste share, gave up ten points of GAAP operating margin, wrote
  off $2,211M of acquisitions and needed 3.9 more points of sales in advertising, **and still earned 79.0% pre-tax on average
  net tangible operating assets in 2025, and 101.0% before the impairment, the highest in this row bar one.** That is precisely
  **[E3-43]**: *"franchises can tolerate mis-management. Inept managers may diminish a franchise's profitability, but they cannot
  inflict mortal damage."* The mismanagement-tolerance test **[E5-18]** is not hypothetical for Colgate; the decade ran it.
- **[E2-45] the attacker's test, run segment by segment, because it answers differently in each.**
  - **Oral Care (44% of sales).** *"how I would like, assuming I had ample capital and skilled personnel, to compete with it"*:
    badly. Three multinationals with ample capital and skilled personnel (PG, Unilever, Haleon) have competed with it for
    decades and none has taken the position. Colgate's share is still 41.3% of the world's toothpaste dollars, in a category it
    sells in over 200 countries and territories with plants in over 80. The share it lost went diffusely to local brands and
    private label, not to a crosser. **The moat here is narrowed, not crossed.**
  - **Pet Nutrition (23% of sales).** **The attacker's test is being run, and it is being passed by the attacker.** Freshpet took
    net sales from **$130M in 2016 to $1,102M in 2025**, 8.5x in nine years, on a different physical form of the product, and
    crossed into operating profit in 2024 (+3.9%) and 2025 (+6.9%). Hill's held its own over the same span (volume **+31.7**
    points and price **+49.1** with FX of only -3.4, the best two-sided record of any scope in this file), and its therapeutic
    range sold *"principally through authorized pet supply retailers, veterinarians and eCommerce retailers"* is a real barrier.
    **But the class is PROVISIONAL because Purina and Mars cannot be measured**, and a category with a filed 8.5x attacker in it
    is not one where criterion (2) can be asserted.
  - **Personal Care and Home Care (33% of sales).** **Criterion (2) is not shown, and the filing is the reason.** Colgate claims
    *"global leadership in liquid hand soap"* and no other share number for these categories; the products are bar soap, shower
    gel, deodorant, dish liquid, household cleaner and fabric conditioner; and the 10-K's own words are that *"'private label'
    products sold by our retail customers, which are typically sold at lower prices than branded products, are a source of
    competition for certain of our products"*. **No filed metric in this file establishes "no close substitute" for a Palmolive
    dish liquid or an Irish Spring bar soap, and none is invented.**
- **Colgate ran the attacker's test on itself and lost.** The skin-health acquisitions (EltaMD and PCA SKIN 2018, Filorga 2019)
  were the company entering an adjacent premium category with ample capital, and they have been written down **$2,211M in three
  charges: $571M in 2021, $721M in 2022, $919M in 2025.** That is evidence about the boundary of the franchise: it did not
  travel.
- **Class: [ ] WIDE [x] NARROW [ ] NONE [x] PROVISIONAL for Pet Nutrition only** · **Direction [E4-32]: narrowed 2015-2021,
  re-widened 2022-2025, still below its 2015 width, and the re-widening was bought with 3.9 more points of sales in advertising.
  Not a moat widening every year.**

### THE FRANCHISE CASE AND THE CASE AGAINST, BOTH AT FULL STRENGTH [E4-26]
*Hunt disconfirming evidence hardest for the hypothesis you like: **[E4-26]**. Both were built before the verdict was written.*

**The case against, stated at full strength:** *"This is a business whose units have not grown for a decade. Company volume is
+7.7 points in ten years and the Oral, Personal and Home Care segment is +2.9; all the dollar growth was price, and most of that
price was recovering devaluation in Latin America and Africa/Eurasia, where +77 points of price bought back -56 and -63 points of
currency. In the three hard-currency regions real pricing has been about 1% a year, and in the home market it has been NEGATIVE
for two straight years while volume fell 9.3 points over five. The primary share metric is 3.4 points below its 2015 level and
it now takes 3.9 more points of sales in advertising to hold what is left. GAAP operating margin went from 26.0% to 16.2%. The
filing names private label, retailers with 'greater bargaining strength than we do', Walmart at 11% of sales and 'AI-aided
category pricing pressures and algorithms'. The one attempt to buy an adjacent franchise cost $2,211M in write-offs. A third of
sales is in categories where the company claims no share leadership at all."*

**The answer, on the filed record, clause by clause.** (1) Every fact in it is granted; each one is in the tables above, taken
from the filing. (2) **But none of them is a failure of [E3-03].** The corpus's test of the three conditions is *"the ability to
regularly price its product or service aggressively and thereby to earn high rates of return on capital"*, and at the **end** of
that decade of narrowing, after the share loss, after the margin loss, after the write-offs, Colgate earned **79.0% pre-tax on
average net tangible operating assets, and 101.0% before the impairment**, at the top of a ten-company row of its own industry.
A business that can absorb all of the above and still earn that is the business [E3-43] describes, not a counter-example to it.
(3) The 2022-2023 test, **+9.5% and +10.0% of worldwide price with global toothpaste share rising from 39.4% to 41.1%**, is
[E2-44] criterion (1) passing in the hardest conditions the decade offered. (4) [E4-04] is not engaged: the spending defends the
same trademarks, not their replacement, and [E5-23] prescribes that defence for every moat. (5) The narrowing is real and it is
the reason the class is **NARROW and not WIDE**, and the reason [E4-32]'s direction test is recorded as **failed across the
decade**; it is not a reason to call the moat absent. **A narrowing moat is still a moat; the framework's own word for the other
thing is "crossed", and nothing in eleven years of filings shows a crosser.**

**And the manager-dependence half of [E4-04], answered rather than assumed.** [E3-03] says a franchise *"can tolerate
mis-management"*, and [E5-18] puts it as *"if it won't stand a little mismanagement it's not much of a business"*. Colgate's
decade is the test and it stood it. **[E4-33]'s knight, the manager who widens the moat, is a question about DIRECTION, and it
is asked at Q3, after the castle, not here.**

- **Can I name the document that would resolve what is left open?** For Oral Care, Personal Care and Home Care: **no document is
  missing.** The twelve 10-Ks, the 10-Qs and the ten peers' filings are read and they answer the question. For Pet Nutrition,
  **yes, and it cannot be got from a primary filing**: Purina sits inside Nestlé's consolidated accounts and Mars is private, so
  no SEC filing will ever produce the row. That is why the Pet class is held **PROVISIONAL** rather than marked UNRESEARCHED for
  a document that does not exist; and Pet Nutrition is 23% of sales, so it does not carry the verdict.
- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *IN, and narrowly. All three **[E3-03]** conditions hold for Oral Care (44% of 2025 sales, the category in which the company
  has held 39-45% of the world's toothpaste dollars for twelve filed years), and the demonstration the 1991 letter attaches to
  them, aggressive pricing plus high returns on capital, is satisfied by the 2022-2023 pricing record and by returns of
  61.5-101.0% pre-tax on net tangible operating assets across a decade, at the top of a ten-company competitor row. **[E4-04] is
  not engaged**: the moat is defended, not rebuilt, and the decade proved it tolerates mismanagement **[E3-43], [E5-18]**.
  **Class NARROW, not WIDE, and the three findings that keep it out of the WIDE class are recorded and carried, not waived:**
  (a) **[E4-32] direction fails across the decade**, the primary share metric being 3.4 points below its 2015 level with the
  re-widening since 2021 bought by 3.9 more points of sales in advertising; (b) **[E4-37]'s inverse metric is firing in North
  America**, net selling price negative in 2024 and 2025 with volume -9.3 points over five years; (c) **criterion (2) is NOT
  shown for Personal Care and Home Care (33% of sales)**, and **Pet Nutrition (23%) is PROVISIONAL** because Purina and Mars
  cannot be measured from any filing. **[E3-33] untapped pricing power is refused outright.** The file continues to Q3.*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**Q2 returned IN, so this gate is live and governing.** *Provenance note, because it matters to how this section is read: a
draft of this question (`_research 2026-09-13 CL/sec_q3_draft.md`) was written by the killed session **before Q2 closed**, and
carried two lines that presupposed later gates. Both were found and both are corrected here, on the record: (a) the leverage
row asserted "a franchise's earning power" as a premise, which was a Q2 conclusion written into Q3 before Q2 existed, and is
now stated as a finding **of** Q2 with its class; (b) the capital-allocation row imported a value range from an unrun Q5
("the Q5 computation below puts value at the ~10% floor near $50-75 a share"), which is a hard-sequence violation and **is
deleted** — the buyback test's second condition is left OPEN here and closed at Q5. Every quote in the draft was re-read
against the filing before it entered this file.*

### STEP 1 — DECLARE THE WEIGHT CASE. The business sets it.
- **Control [E1-16]: no.** The purchase in question is listed shares; nothing is controlled and the position can be exited.
- **Leverage [E3-29]: no, in the sense the row means.** Read off the face of the 2026-06-30 balance sheet (10-Q
  `0000021665-26-000042`): debt payable within one year **$34M** plus long-term debt **$7,823M** is **$7,857M** of total debt
  against cash of **$1,370M**, so **net debt about $6,487M**. *(Current marketable securities are not a separate line at
  2026-06-30; they sit inside "Other current assets" and are not disclosed, so cash alone is used, which is the conservative
  read. At 2025-12-31 the same arithmetic is $1,117M + $6,871M less $1,288M of cash and $107M of current marketable securities,
  or $6,593M.)* **Interest paid was $270M in 2025** against
  net cash provided by operations less capital expenditures of $3,634M, **13.5x covered** (10-K FY2025 supplemental cash-flow
  line, *"Interest paid | $ | 270 | $ | 302 | $ | 280"*). Book equity is **$54M at 2025-12-31 and $236M at 2026-06-30** — the
  residue of **$28,931M of treasury stock** bought back, not of assets lost. **Not the [E3-29] case:** the 1990 quote is about
  *"leverage of 20:1"* at a bank, where a small error in the assets destroys the equity. Colgate's cushion is the cash flow, and
  the reason the cushion holds is the finding **Q2 returned above** — a NARROW franchise earning 61.5%-101.0% pre-tax on net
  tangible operating assets — not an assumption made here.
- **Daily execution [E3-38, E2-70, E3-43]: MIXED, and the mix is the answer.** [E2-70]'s magnifier is *"no important advantages
  from trademarks, patents, location, corporate longevity"*; Colgate's advantage **is** trademarks, and the 10-K says they
  *"endure for as long as they are used and/or registered"*. This is nearer [E3-38]'s *"have-to-be-smart-once"* pole than to
  the retailer for whom *"hiring that nephew would be an express ticket to bankruptcy"*. **But it is not at that pole.** Trade
  terms are renegotiated continuously with retailers the filing says *"exercise greater bargaining strength than we do"*;
  Walmart is 11% of net sales; pricing has to be reset every few months in Argentina, Türkiye and Nigeria; and 33% of sales sits
  in Personal and Home Care, where **Q2 found criterion (2) not shown** and which is therefore nearer [E3-43]'s *"a business"*
  than its *"franchise"*.
- **WEIGHT CASE, declared: Q3 is a QUALITATIVE OVERLAY, not a binary gate** — on [E3-43]'s own rule, *"franchises can tolerate
  mis-management ... a business, unlike a franchise, can be killed by poor management"*, and Q2 returned a franchise for 67% of
  sales. **But it is scored harder than it would be for a WIDE franchise**, because Q2's class is NARROW, a third of sales did
  not clear criterion (2), and the [E4-37] agony signal is already firing in North America. **No price compensates is NOT
  invoked here**; a poor manager at Colgate would narrow the moat, not kill the company.

### HONESTY — binary, permanent, filings-based [E5-16]. Every matter found in the 10-Ks FY2014-FY2025 and the 2026 10-Qs, dated to when it became public.
- **December 2014:** *"the French competition law authority found that 13 consumer goods companies, including the Company's
  French subsidiary, exchanged competitively sensitive information related to the French home care and personal care sectors,
  for which the Company's French subsidiary was fined $57 million."*
- **July 2017:** the Greek competition authority fined the Greek subsidiary $11M for *"a restriction of parallel imports into
  Greece"*; in April 2019 the Greek courts *"affirmed the judgment against the Company's Greek subsidiary, but reduced the fine
  to $10.5 and dismissed the case against Colgate-Palmolive Company"* (10-K FY2021). The matter does not appear in the FY2024
  10-K.
- **2013-2015:** *"Charges for European competition law matters"* of $23M (2013) and $41M (2014), excluded from the non-GAAP
  figures of those years.
- **June 2016 onward, the ERISA matter:** a suit that residual annuity payments under a 2005 plan amendment *"were improperly
  calculated"*; the company lost in the District Court and the Second Circuit, took charges of $267M (Q1 2023) and $65M (Q1
  2025), and settled for $332M in Q3 2025, final approval January 2026, with $99M of plaintiffs' fees paid by the company and
  the rest funded by the plan.
- **Talc:** 525 individual cases pending at 2026-06-30 (453 at 2025-12-31, 308 at 2024-12-31, 193 at 2017-12-31); settlements
  *"not material"*; aggregate reasonably possible losses in excess of accruals across all disclosed matters *"$ 0 to
  approximately $ 225"*.
- **Tax:** Brazilian Kolynos assessments of about $105M, disputed since 2001, and an IRS imputed-income matter of about $168M,
  not reserved; both argued as more likely than not to be won.
- **Searched and not found:** any SEC enforcement action, restatement, FCPA matter (the phrase appears only in risk-factor and
  regulation descriptions), auditor change, or qualified opinion. PwC is unqualified on the statements and on internal control
  for FY2025.
- **Finding:** two competition-law fines against subsidiaries in shared-industry matters, one reduced on appeal with the parent
  dismissed, and a lost pension-calculation suit. **None names an officer or director, and none is personal misconduct as
  [E5-16] uses the words** (*"our tolerance for personal misconduct is zero"*). **[E2-31]'s veto is not triggered.** The queue's
  open operator question about corporate records with no individual accountability (UMC, 2026-09-13) applies to the French fine
  and is carried there, not decided here.

### STEP 2 — THE FLAGS [E4-22, E4-29]. *Prompts to read; each read below, not scored.*
- [ ] **Weak accounting: no cockroach found.** Stock compensation is expensed in full and the cash-flow add-back equals the
  equity-statement line in every year 2015-2025. **Pension assumption, read:** the US expected long-term return is 6.50%
  against the filing's own record, *"Average annual rates of return for the U.S. plans for the most recent 1-year, 5-year,
  10-year, 15-year and 25-year periods were 10%, 1%, 5%, 6% and 5%, respectively"* (10-K FY2025). **The assumption sits above
  the realised 5-, 10- and 25-year figures.** The filing's own sensitivity is *"approximately $12"* of net income per point.
  A prompt read, found real and found small; not a disqualifier, and recorded rather than waived.
- [ ] **Unintelligible footnotes: no.** The restructuring, impairment, ERISA and hyperinflation notes are specific and
  quantified.
- [x] **Trumpeted earnings projections and growth targets: FIRES.** Guidance is issued every January for net sales, organic
  sales, gross margin, advertising and earnings per share on both bases, against a *"long-term targeted range of 3% to 5%"* for
  organic growth, beneath a standing objective of *"delivering consistent, compounded earnings per share growth"*. **[E3-48]'s
  remedy is to score the forecaster's record against outturn**, so it is scored (guidance from each January release; outturn
  from the next January's release; every cell re-read from the release on disk):

  | year | organic sales guided | outturn | Base Business EPS guided | outturn |
  |---|---|---|---|---|
  | 2021 | *"up within its long-term targeted range of 3% to 5%"* | **+4.5%** | *"mid to high-single-digit"* growth | $3.21, **+5%** |
  | 2022 | *"within its long-term targeted range of 3% to 5%"* | **+7.0%** | *"low to mid-single-digit"*, with *"gross margin expansion"* | **$2.97, -7%**; gross margin 59.6% to 57.0% |
  | 2023 | *"towards the high end"* of 3% to 5% | **+8.5%** | *"low to mid-single-digit"* | $3.23, **+9%** |
  | 2024 | *"within its long-term targeted range of 3% to 5%"* | **+7.4%** | *"mid to high-single-digit"* | $3.60, **+11%** |
  | 2025 | *"within its long-term targeted range of 3% to 5%"* | **+1.4%** | mid-single-digit, with gross margin expansion | $3.69, **+3%**; gross margin 60.5% to 60.1% |
  | 2026 | *"1% to 4%"* | H1 +2.6% | *"mid-single-digit"* (raised in July from low to mid) | open |

  **Met or beaten on organic growth in four of five closed years; missed 2025's badly (+1.4% against 3-5%).** On EPS, met in
  four of five and missed 2022 by a wide margin, along with that year's gross-margin guidance. **One candor point, recorded
  exactly because it cuts both ways:** the January 2023 release describes the 2022 outturn as *"EPS* declined 7% to $2.97, in
  line with the Company's full year guidance"* — which is true of guidance **as revised during 2022** and not of the January
  2022 guidance quoted above. The revision is disclosed; the January-to-January comparison is what [E3-48] asks for and it is
  the one tabulated. **The corpus's objection is not the hit rate:** *"once you start it, it's all over. You can't quit ...
  forecasting earnings, I can't imagine anything more destructive"* **[E5-30]**. This company has run the ratchet for years and
  shows no sign of stopping. **Carried as a standing flag, not as a disqualifier.**
- [ ] **Serial share issuance: no.** Diluted weighted average shares went 898.4M (2016) to 811.1M (2025), **-9.7%**; no dividend
  is funded by issuance.
- [ ] **EBITDA promotion [E4-29]: NO INSTANCE, and the sweep is stated so it can be repeated.** A case-insensitive search for
  "EBITDA" across **every Colgate file on disk** — twelve 10-Ks, the 10-K/A, five 10-Qs, three DEF 14As, every 8-K since 2021
  and every EX-99 earnings release — returns **zero files**. The headline adjusted measure is **Base Business EPS**, which sits
  below every cost line including depreciation and amortisation. *This is the CGNX companion rule applied: the earnings releases
  were read, not just the annual report, and they are clean on this flag.*
- [ ] **Filed-figure tells [E4-30]: no smoothing.** Base Business EPS grew +5%, -7%, +9%, +11%, +3% across 2021-2025: not a
  smooth series. Cash taxes paid as a share of pre-tax income: 24.9% (2016), 29.7% (2017, US tax reform), 24.5%, 24.3%, 23.2%,
  then 24.3%, 28.0% and 23.0% in the impairment years 2021, 2022 and 2025 with the impairments added back, 27.6% (2023), 23.6%
  (2024). **No falling trend**, which is the tell this test looks for.
- **Metric-switching [E2-49]: not fired.** The release headline set is the same in January 2021 and January 2026 (net sales,
  organic sales, GAAP EPS, Base Business EPS, gross margin, operating cash, the two shareholder-return figures). Two committee
  adjustments in the 2026 proxy run in **opposite** directions: the 2025 bonus EPS was raised by $0.06 for tariffs, a right
  *"specifically reserved"* when targets were set in March 2025 (announced ahead, with reasons — the candor form); and
  three-year free-cash-flow productivity was **cut** from 133.6% to 115.7% because impairment and ERISA charges had lowered the
  denominator. **A committee that adjusts a pay metric down is evidence, and it is recorded as such.**
- **The restructuring charge [E5-33]: FIRES, at modest size.** Program items have been excluded from the headline measure in
  **thirteen of the fourteen years 2012-2025**, every year but 2021: the Global Growth and Efficiency Program (Q4 2012 to 2019,
  *"total pretax charges were $ 1,854"*), the 2022 Global Productivity Initiative (*"total pretax charges of $ 228"*), and the
  Strategic Growth and Productivity Program (2025-2028, its estimate raised on 2026-04-30 from *"$200 million to $300 million"*
  to *"between $350 million and $550 million"*). Charges by year 2016-2025: 228, 333, 152, 125, (16), 0, 95, 27, 85, 13; H1 2026
  $305M. That is roughly **$104M a year pre-tax across the decade, about 2.5% of base operating profit.** **Base Business EPS is
  40% of the annual bonus** (2026 proxy), so classifying a cost into a program moves pay. *"to tell owners year after year,
  'Don't count this,' when management is simply making business adjustments that are necessary, is misleading"* **[E5-33]**.
  **Consequence for Q4, recorded here and binding there: owner earnings will include the cash these programs spend, because
  operating cash flow does, and no restructuring line will be added back.**
- **The except-for flag [E2-57]: FIRES on the skin-health purchases.** Three impairments of the same 2018-2019 purchases,
  **$571M (2021), $721M (2022) and $919M (2025), $2,211M in total**, each excluded from Base Business results, each followed by
  a statement of continued belief: *"The Company continues to believe in the strength of the Filorga brand and is confident
  about its long-term growth opportunities"* (Q4 2022 release, 2023-01-27) and *"The Company is taking the appropriate actions
  to improve performance and continues to believe in the growth prospects of the business"* (10-K FY2025 and the Q4 2025
  release). *"Any manager who consistently says 'except for' and then reports on the lessons he has learned from his mistakes
  may be missing the only important lesson — namely, that the real mistake is not the act, but the actor"* **[E2-57]**.
  **No post-mortem of the purchases against their announcement case was found in any 10-K or proxy on disk.**
- **Do the flags converge?** Read as one system: an objective of *"consistent, compounded earnings per share growth"*; annual
  EPS guidance; a bonus 40% on Base Business EPS, which excludes restructuring and impairments; and repurchases budgeted into
  the EPS target. **They point the same way, toward a delivered per-share number.** Against that, the same proxy states the link
  in plain words — *"We take into account the budget for our share repurchase program when setting our earnings per share
  targets, and no decisions about share repurchase plans are tied to an attempt to influence compensation results"* — and cut a
  pay metric that would have flattered management. **Recorded as a converging prompt with its candor case beside it, not as a
  venality finding.** [E2-30]'s own caution applies: *"Institutional dynamics, not venality or stupidity, set businesses on
  these courses"*; and [E5-38] is the reminder that the two are separable — people who *"would return"* your wallet *"would
  play games with any number that came to them."*

### STEP 3 — THE PRIMARY TEST [E2-01], on the denominator the corpus prescribes for this case [E2-43]
*"The primary test of managerial economic performance is the achievement of a high earnings rate on equity capital employed
(without undue leverage, accounting gimmickry, etc.) and not the achievement of consistent gains in earnings per share"*
**[E2-01]**. **Book equity is $54M (2025) after buybacks, so a return on it is not a number** — which is exactly the case
[E2-43] anticipates, and the denominator becomes unleveraged net tangible operating assets. Pre-tax GAAP operating return, from
the Q1 table (`ntoa.py`, `ntoa_out.md`): **96.9%, 89.8%, 91.2%, 88.6%, 98.5%, 84.7%, 61.5%, 76.0%, 91.0%, 79.0% (2016-2025)**;
with the goodwill and intangible impairments added back, 99.2% (2021), 76.8% (2022) and 101.0% (2025). **High and unlevered at
the operating level throughout; the 2022 trough is the input-cost year.** Against the competitor row built at Q2, only Procter &
Gamble is in the same band. **[E2-01]'s warning half is the one that fires: the company's own stated objective and its bonus
plan are built on "consistent gains in earnings per share", which is the metric [E2-01] defines the primary test in opposition
to.** Both halves are recorded.

**The two yardsticks [E3-59].** *"One is how well they run the business"*, judged against *"the hand they were dealt"* and read
against competitors' reports: on the returns figure they are at the top of the row; on the **physical** series they are at the
better end of a poor row (Q2); on the **share** series they lost 5.3 points of global toothpaste share between 2015 and 2021 and
have regained 1.9 since. *"And then the second thing ... is how well that they treat their owners"*: dividends have been paid
and raised, the share count is down 9.7%, every non-GAAP adjustment is quantified at every line, and the segment recasts were
published with restated history (8-Ks 2024-10-25 and 2026-03-17).

**The half-owner test [E2-26]** — *"tell you the business facts that we would want to know if our positions were reversed"* —
**mostly passes.** Every non-GAAP adjustment is quantified at every line of the MD&A and the releases; the market-share figures
carry their own limits; the proxy discloses an adjustment that **reduced** a pay metric. **What an owner in the reverse position
would also want and does not get:** a single plain statement that restructuring has been continuous since 2012, and a reckoning
of the skin-health purchases against what was paid for them.

### THE INSTITUTIONAL IMPERATIVE — all four scored [E2-30]
- [ ] **(1) resists change:** no evidence. Segments were reorganised twice in two years and two productivity programs launched.
- [x] **(2) projects or acquisitions materialise to soak up available funds: FIRES, and this is the sharpest finding in Q3.**
  PCA SKIN and EltaMD (*"professional skin care businesses, for aggregate cash consideration of approximately $730"*, 2018) and
  Filorga (September 2019; $1,711M of 2019 acquisition cash) put about **$2.4bn into a skin-health adjacency in two years**,
  while the core's own primary metric was falling (global toothpaste share 44.0% in 2016 to 41.1% in 2019 to 39.4% in 2021, Q2).
  **$2,211M of it has been written off.** (hello, $351M in 2020, is an oral care business and is not counted here.) **The Pro-Am
  camouflage [E2-56] is exact:** *"Their marvelous core businesses, however, whose earnings grow year after year, camouflage
  repeated failures in capital allocation elsewhere (usually involving high-priced acquisitions of businesses that have
  inherently mediocre economics)."* A consolidated 79%-101% return on net tangible operating assets hides a 90%+ loss on $2.4bn,
  and the framework's guardrail passage names this vector as one of the two that actually damage a great company.
- [ ] **(3) staff studies for the leader's craving:** not observable from filings; no claim made.
- [ ] **(4) peer behaviour mindlessly imitated:** not evidenced from the filings read; no claim made. *(Noted without being
  scored: every peer in the Q2 row ran the same 2021-2023 price push and the same 2025 give-back, which is what a common input
  shock looks like as much as what imitation looks like, and the filings cannot separate them.)*

### CAPITAL ALLOCATION — the buyback conditions [E5-08, E4-31]
- **(1) ample funds beyond the near-term needs of the business: essentially yes, and the earlier draft overstated the gap.**
  **Filed figures only; no owner-earnings number is imported from the unrun Q4.** Over 2016-2025, net cash provided by
  operations was **$34,034M** and capital expenditures were **$5,419M** (593, 553, 436, 335, 409, 567, 696, 705, 561, 564),
  leaving **$28,615M**. The four uses were dividends **$16,627M**, repurchases **$13,355M** less option proceeds **$4,555M**,
  and acquisitions **$3,899M**, totalling **$29,326M**. **The shortfall across the decade is about $711M, roughly 2% of the
  cash generated**, which is why long-term debt is close to where it started ($6,520M at 2016, $6,871M at 2025, $7,823M at
  2026-06-30 after the Prime100 purchase) and cash is close to where it started ($1,315M, $1,288M, $1,370M). *Correction on the
  record: the killed session's draft put the uses at $29,266M against "$27,376M of capex-end owner earnings" and concluded the
  difference "came from debt ... and working capital". The uses figure is $29,326M on the filed cash-flow lines (its option
  proceeds of $4,615M do not reconcile to the filed sum of $4,555M), the comparison it drew was against a Q4 output that did not
  yet exist, and against the filed sources the gap is about a fiftieth of the cash, not a structural reliance on borrowing.*
- **(2) stock selling at a material discount to intrinsic value, conservatively calculated: OPEN, and it is closed at Q5, not
  here.** What is filed: repurchases ran at an average of **$78.54 a share in Q4 2025** (10-K Item 5), **$90.28 in Q1 2026**
  with February at **$95.90**, and **$87.40 in Q2 2026** (10-Q Part II). **No value range is imported into this section**; the
  hard sequence puts the value computation at Q5 and the earlier draft's forward reference to it has been deleted. **Marked
  OPEN, and revisited at Q5 with the fresh price and sovereign.**
- **(3) the disclosure caveat [E4-31]** — *"Shareholders should have been supplied all the information they need for estimating
  that value"* — **yes, largely**, subject to the two half-owner gaps above.
- **Incentives [E4-27], because the corpus says never think about anything else when you should be thinking about them.** Annual
  bonus: **40% Base Business EPS, 40% Organic Sales Growth, 20% Strategic Initiatives**, with a floor (*"If Base Business
  Earnings Per Share was less than $3.38 or organic sales growth was less than 1.0%, no annual bonus would be paid"*). Long-term
  awards: 50% performance-based restricted stock units on relative organic growth, relative Base Business net income growth and
  free-cash-flow productivity, with a plus-or-minus 25% relative total-shareholder-return modifier; 30% options; 20% restricted
  stock units (2026 proxy). CEO total 2025 compensation **$16,478,196** against a median employee's **$59,655**, a ratio of
  **276 times**, as filed. **What the pay plan vests on: adjusted per-share figures and growth rates — and not on returns on
  capital, which is the number [E2-01] and [E3-46] say is the test.** The pay plan and the framework are measuring different
  things, and the filing is candid about which it uses.

### THE GUARDRAIL — checked before the verdict. Q3 can stop a run; it can never start one.
- [x] Nothing in this Q3 is used to promote the name **[E2-37, E2-38, E3-39]**. *"betting on the quality of a business is
  better than betting on the quality of management"* — the Q2 verdict, not this section, is what carries Colgate forward.
- [x] No key-person dependence is claimed. Q2 found the moat is not manager-dependent, and [E5-18] is the standard applied.
- [x] No excisable-cancer case is argued **[E2-35, E2-36]**; no manager is the plan. The skin-health write-offs are a cost
  already taken and are counted in all nine innings **[E2-57]**.
- [x] **The humility clause [E5-17] is applied, and this verdict is written in its form:** *"People are not that easy to read.
  Sincerity and empathy can easily be faked."* **What follows is the absence of found disqualifiers, not a finding that these
  managers are honest.** [E5-32] caps it further: the audited statement is not bedrock, which is why the cash-tax and
  share-count cross-checks above were run rather than assumed.

- **VERDICT: [x] IN**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *IN as an overlay, in the guardrail's own terms: **no integrity disqualifier was found** in twelve years of 10-Ks, five 10-Qs,
  three proxies and every earnings release on disk — no SEC action, no restatement, no auditor change, no qualified opinion, no
  matter naming an officer or director, and **zero instances of EBITDA promotion [E4-29]** across every file. Two subsidiary
  competition-law fines and a lost pension-calculation suit are recorded and are not personal misconduct as **[E5-16]** uses the
  words, so **[E2-31]**'s veto is not triggered. **On [E2-01]'s primary test the record is strong** — 61.5%-101.0% pre-tax on
  average net tangible operating assets over a decade, matched in the Q2 row only by Procter & Gamble. **Four findings are
  carried forward rather than waived, and three of them bind later sections:** (a) **[E2-30](2) with [E2-56]** — about $2.4bn
  put into a skin-health adjacency while the core's share was falling, $2,211M of it written off, with no post-mortem filed;
  (b) **[E5-33]** — program charges excluded from the headline measure in thirteen of fourteen years, which **binds Q4: no
  restructuring is added back to owner earnings**; (c) **[E5-30] and [E3-48]** — annual EPS guidance under a stated objective of
  *"consistent, compounded earnings per share growth"*, scored against outturn above, with 2025's organic guidance missed at
  +1.4% against 3-5%; (d) **[E5-08](2) left OPEN** — repurchases at $78.54 to $95.90 a share whose discount to value cannot be
  judged before Q5, where it is closed. **This IN promotes nothing** (**[E2-37, E2-38, E3-39]**) and it is the absence of found
  disqualifiers, not a certificate (**[E5-17]**). The file continues to Q4.*

## Q4 — WILL IT SURVIVE?

### THE PERIMETER, settled first, because it decides where the window can start
- **Venezuela.** The FY2016 10-K's own organic definition excludes *"the deconsolidation of the Company's Venezuelan
  operations"*, alongside foreign exchange, acquisitions and divestments. **No window in this section starts before 2016**, and
  the eleven-year 2015-2025 window is displayed but not used, and labelled as crossing the perimeter change.
- **Acquisitions inside the window, from the 10-Ks** (each a change of perimeter, none restated backwards): EltaMD and PCA
  SKIN 2018, *"aggregate cash consideration of approximately $730"*; Filorga September 2019, $1,711M of acquisition cash; hello
  2020, $351M; **three United States dry pet food plants from Red Collar Pet Foods in 2022, *"a purchase price, as adjusted, of
  $719"***; Prime100 (Care TopCo, Australia) 2025, $301M. Total acquisition cash 2016-2025: **$3,899M**. They are shown beside
  owner earnings and are **not** subtracted from it; they are capital allocation and were scored at Q3.
- **Equity-method stakes [E3-04]: immaterial and no look-through adjustment is made.** *"equity method investments included in
  Other assets in the Consolidated Balance Sheets were $ 82 and $ 81"* (2025, 2024), against $16,330M of assets.
- **The ESOP open item, closed on the filing.** Step 0 left it open because no share-based-compensation list reads the ESOP
  tags. The note answers it outright: ***"Annual expense related to the ESOP was $ 0 in 2025, 2024 and 2023."*** The 6,646,688
  ESOP shares are common shares already inside the share count and *"have all been released and allocated to participant
  accounts"*; the ESOP *"had no outstanding borrowings from the Company"*. **So nothing is missing from the compensation
  charge, and the draft's deduction of ESOP dividends ($15M in 2025) from owner earnings is over-conservative** — those
  dividends are paid on shares already counted. It is kept in the table as a display and is **not** used in the range.
- **Hyperinflationary remeasurement: inside net income and NOT separately quantified, and that is stated rather than
  estimated.** *"Remeasurement adjustments for these operations are included in Net income attributable to Colgate-Palmolive
  Company"* (Note 2). No amount is disclosed in any 10-K on disk. The exposure can only be bounded by region: Latin America and
  Africa/Eurasia are 29.2% of 2025 net sales, and the 10-K names *"Argentina, Nigeria and Türkiye"*. **An UNRESEARCHED tag is
  not warranted, because no document exists that gives the figure; it is recorded as a disclosure gap.**

### OWNER EARNINGS — THE ONE NUMBER [E2-23]
**Built by hand from the filed cash-flow statements, not from a net-income proxy and not from tagged data** (script `oe.py`,
output `oe_out.md`; sources 10-K FY2017 for 2015-2017, FY2020 for 2018-2020, FY2023 for 2021-2023, FY2025 for 2023-2025, and
the 10-Q for the quarter ended 2026-06-30 for the interim). **Verified in this session against the filings:** FY2025
depreciation and amortization $630M, stock-based compensation $155M, capital expenditures $564M; H1 2026 net cash provided by
operations $1,742M, D&A $311M, SBC $78M, capex $266M; H1 2025 $1,484M / $299M / $55M / $232M and the $293M Prime100 payment.
All match the script's inputs.

**(c), the disclosed judgment. It "must be a guess."**
- **[E5-20] asked on the filing, and answered: Colgate is NOT in the exception class.** The exception is the business *"whose
  own filing says depreciation understates renewal"* — railroads, airlines, utilities. Colgate's filing says the opposite
  shape: net property, plant and equipment is **$4,660M against $20,382M of sales**, capital expenditures have run **2.1% to
  3.9% of sales** across the decade, and the FY2025 10-K plans FY2026 at *"approximately 3.0% of Net sales"*. Over 2016-2025
  **capex was $5,420M against depreciation of $4,719M (1.15x) and D&A of $5,390M (1.01x)** — the [E2-41] and [E3-44] default
  case, *"capital expenditures that over time roughly approximate depreciation"*. **So the D&A end is VALID here, not invalid.**
- **And (c) is still set at TOTAL capital expenditures, not at depreciation, for two reasons from the filing.** (i) **[E4-47],
  the inflation condition:** 29.2% of sales sit in Latin America and Africa/Eurasia, where depreciation is charged in old
  dollars and replacement is bought in new ones — and the segment notes show it: **Latin America's own capex/D&A is 1.35x over
  2016-2025 ($1,198M against $890M)**. (ii) No split of maintenance from growth is filed, and the credit for treating Hill's
  plant building as growth (segment capex of $888M against D&A of $360M across 2021-2024) is **declined** rather than taken.
  **The band is narrow anyway**: the capex end and the D&A end differ by about 1% over ten years.
- **The working-capital increment [E2-23] constraint 3: NONE is required, and the carve-out is why.** Colgate's working capital
  is negative — *"(7.0)% in 2025"* of net sales — so growth **releases** cash rather than absorbing it. That is the benign
  case. **But a release is not a repeatable earning**, so every window below is also shown with the filed working-capital lines
  (receivables, inventories, accounts payable and other working capital) stripped out.
- **No restructuring is added back.** Q3's **[E5-33]** finding binds here: program charges have been excluded from the
  headline measure in thirteen of fourteen years, so their cash stays in owner earnings because operating cash flow carries it.

| year | OCF | SBC | D&A | depreciation | capex | OE (c)=capex | OE (c)=depreciation | OE (c)=D&A | capex/depr. | acquisitions |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 3,141 | 123 | 443 | 410 | 593 | **2,425** | 2,608 | 2,575 | 1.45 | 5 |
| 2017 | 3,054 | 127 | 475 | 440 | 553 | **2,374** | 2,487 | 2,452 | 1.26 | 0 |
| 2018 | 3,056 | 109 | 511 | 452 | 436 | **2,511** | 2,495 | 2,436 | 0.96 | 728 |
| 2019 | 3,133 | 100 | 519 | 457 | 335 | **2,698** | 2,576 | 2,514 | 0.73 | 1,711 |
| 2020 | 3,719 | 107 | 539 | 451 | 410 | **3,202** | 3,161 | 3,073 | 0.91 | 353 |
| 2021 | 3,325 | 135 | 556 | 467 | 567 | **2,623** | 2,723 | 2,634 | 1.21 | 0 |
| 2022 | 2,556 | 125 | 545 | 465 | 696 | **1,735** | 1,966 | 1,886 | 1.50 | 809 |
| 2023 | 3,745 | 122 | 567 | 495 | 705 | **2,918** | 3,128 | 3,056 | 1.42 | 0 |
| 2024 | 4,107 | 135 | 605 | 530 | 561 | **3,411** | 3,442 | 3,367 | 1.06 | 0 |
| 2025 | 4,198 | 155 | 630 | 552 | 564 | **3,479** | 3,491 | 3,413 | 1.02 | 293 |
| TTM to 2026-06-30 | 4,456 | 178 | 642 | n/a | 598 | **3,680** | | 3,636 | | 0 |

**Owner earnings is positive in every year of the window, and its worst year — 2022, the input-cost year — was still
$1,735M.** Share-based compensation has never exceeded 4.9% of operating cash flow and averages 3.6% across the decade, so
shape #2 in the survival-shapes index does not apply.

**THE WINDOWS, AND THE SPREAD IS PART OF THE RANGE [E2-42, E4-25].** The corpus's default is five years; more than one window
is run and the spread carried.

| window | OE (c)=capex | OE (c)=D&A | **less the working-capital release (the conservative read)** |
|---|---|---|---|
| **5-yr 2021-25 — the [E2-42] default** | **2,833** | 2,871 | **2,763** |
| 10-yr 2016-25 — the post-Venezuela perimeter | **2,738** | 2,741 | **2,680** |
| 5-yr 2020-24 | 2,778 | 2,803 | 2,695 |
| 5-yr 2021-25 excluding 2022 | 3,108 | 3,118 | 2,851 |
| 3-yr 2023-25 | 3,269 | 3,279 | **2,879** |
| TTM to 2026-06-30 *(one twelve months, not a mean)* | 3,680 | 3,636 | not computed |
| 11-yr 2015-25 *(crosses the Venezuela perimeter: shown, not used)* | 2,683 | 2,707 | — |

**THE RANGE CARRIED TO Q5: owner earnings of about $2.7bn to $3.3bn a year, centred on the five-year default of $2,833M,
with $3,680M as the trailing-twelve-months reading and $2,680M as the most conservative.** *"working with a range of
possibilities is the better approach"* **[E4-25]**. **The three-year and TTM readings are the ones to distrust, not the
ten-year one**: the three-year window carries a mean working-capital release of **+$390M a year** against **+$58M** across
the decade, which is most of the difference between $3,269M and $2,738M.

**THE WINDAGE COUNT, because conservatism is spent once.** It has been spent **twice** and both are named: (1) (c) is set at
total capital expenditures rather than at the depreciation the corpus's own default prescribes, on the [E4-47] argument above;
(2) the working-capital release is stripped in the conservative column. The ESOP-dividend deduction the draft carried would
have been a **third** and it has been removed as unjustified. **Unwinding both would put the five-year figure at $2,871M rather
than $2,763M — a 4% band.** The count is stated so Q5 cannot spend it again.

### GREAT, GOOD OR GRUESOME — [E4-20]
**GREAT, and the arithmetic says so rather than the adjective.** *"The great one pays an extraordinarily high interest rate
that will rise as the years pass."* Owner earnings per diluted share ran **$2.70 (2016) to $4.29 (2025)**, about **+5.3% a
year**, on net tangible operating assets that **fell** from $4,083M to $4,128M in nominal terms while sales rose 34%. Capital
expenditure has never exceeded 3.9% of sales. This is the opposite of *"the worst sort of business ... grows rapidly, requires
significant capital to engender the growth, and then earns little or no money."* **The qualification, recorded:** the rise in
the rate came from price and from the share count, not from units (Q2: worldwide volume +7.7 points in ten years), so the
"rise as the years pass" clause depends on pricing continuing to outrun costs. **[E4-43]'s caution is noted and not needed
here** — nothing in the record puts Colgate in the *good* class, let alone the gruesome one.

### STAYING POWER — all three scored [E5-11], including the third
1. **A large and reliable stream of earnings: YES.** Net cash provided by operations in every year 2016-2025: 3,141, 3,054,
   3,056, 3,133, 3,719, 3,325, **2,556**, 3,745, 4,107, 4,198. **Never negative, never below $2.5bn, and the trough year was
   the worst raw-material year of the decade.** Two thirds of sales are outside the United States and 45% in emerging markets,
   which is diversification of demand as well as exposure to currency.
2. **Massive liquid assets: NO, and this is scored honestly as a fail rather than argued around.** Cash was **$1,370M at
   2026-06-30** on $16,790M of assets, with current marketable securities not even a separate balance-sheet line. Colgate does
   not carry a fortress balance sheet; it carries a fortress cash flow. **[E2-61]'s sector scope does not rescue it** — that
   carve-out is for insurers and float businesses, and Colgate is neither. **[E5-39] is the standard that is not met:** the
   10-K describes an *"undrawn revolving credit facility supporting our commercial paper programs"*, which is exactly the
   *"kindness of strangers"* the corpus refuses to depend on. **Recorded as the single weakest item in Q4.**
3. **No significant near-term cash requirements: YES, and this is the one most often skipped.** The filed maturity schedule,
   excluding commercial paper: *"2026 | $ | 1,115 | 2027 | 523 | 2028 | 615 | 2029 | 591 | 2030 | 500 | Thereafter | 4,495 |
   Total | $ | 7,839"*. **The largest single year is $1,115M against $4,198M of operating cash flow**, and by 2026-06-30 debt
   payable within one year had already fallen to **$34M** from $1,117M. **Supplier finance is not a hidden maturity:** the
   obligations *"are included in Accounts Payable"* and *"were not material"*. **Pensions are not one either:** United States
   plans are underfunded $441M, international $179M, other retiree benefits $663M — about $1,283M in total, against $4.2bn of
   annual operating cash flow.
- **The coverage test [E2-54]** — *"all interest, both payable and accrued, to be comfortably met out of current cash flow net
  of ample capital expenditures"*: **interest paid $270M in 2025 against $4,198M less $564M of capex, or $3,634M — 13.5x.**
  **Comfortably met**, on the corpus's own construction with capex taken out first.
- **Read the terms, not just the quantity [E3-52].** Colgate's liabilities are the opposite of float: $7,839M of dated,
  covenanted debt, most of it *"Thereafter"*. But its **working capital is negative**, so its suppliers and its customers
  together fund a part of the business without covenants or due dates of the kind that force a sale. The negative working
  capital is a genuine, if small, float-like benefit, and it is named rather than counted twice.
- **Jurisdiction [E3-66].** The registrant is a Delaware corporation on the NYSE, so United States shareholders stand where the
  corpus says they stand best. **But the earning assets do not:** plants in over 80 countries, operations in over 200, with the
  10-K naming *"challenges to our ability to repatriate cash from Russia"* and $1,234M of the $1,288M of 2025 year-end cash
  sitting in foreign subsidiaries. **Where the cash is earned is not where the shareholder stands**, and that gap is recorded.
- **[E2-55] and [E5-29]:** scored on the worst case rather than the expected one, the 2022 trough is the test and it passed
  ($1,735M of owner earnings, 13x interest cover, no covenant event). Volatility in the earnings stream is not risk here;
  impairment of the earning power is, and that is the next section.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES — [E2-27, E3-24, E4-40, E4-51]
**It does not die of its balance sheet. It dies of who owns the shelf.** Stated in the form **[E4-51]** demands, as a bear case
its holders would accept as fairly put, and modelled on **exposure, not experience [E4-40]**.

**The mechanism, from the filing's own words.** Colgate owns the trademark and rents the route to the buyer. The counterparty
that owns that route *"exercise[s] greater bargaining strength than we do, including the exclusive access to valuable
first-party consumer data and analytics"*; it *"ha[s] demanded and may continue to demand higher trade discounts, allowances,
slotting fees, significant investment (including through display media, paid search and co-op programs) or changes to product
assortments, which have led to and could continue to lead to reduced sales or profitability in certain markets"*; it applies
*"AI-aided category pricing pressures and algorithms"*; and it stocks its own *"'private label' products ... which are
typically sold at lower prices than branded products"* on the same shelf. **Walmart alone is *"approximately 11%"* of net
sales**, and the same 11% is filed for 2025, 2024 and 2023. **Trade promotion is deducted from net sales before they are
reported**, so the transfer to the retailer never appears as a line an owner can watch.

**Quantified from filed figures, in the [E3-24] form.** North America is the case where the mechanism has already run, and it
is the only region where retail is concentrated:
- Net selling price: **-1.9% (2024), -0.2% (2025)** — two consecutive years of price given back.
- Volume: **-9.3 points cumulative over 2021-2025.**
- Segment operating margin: **32.4% in 2016** (before skin health was placed in the segment) against **21.5% in 2025** on the
  8-K recast basis that takes skin health back out (net sales $3,679M, operating profit $790M). **About eleven points of margin
  in nine years, or roughly one point a year, like for like.**
- **The model:** if that North American path ran across the whole company for a decade, the 2025 operating margin of **20.7%
  ex-impairment** would fall toward **10-11%**, and owner earnings would roughly **halve, from about $2,833M to about
  $1,450M** — a business still comfortably solvent, still covering its interest 6-7x, and worth less than half of what Q5 is
  about to compute.
- **The likelihood, in the corpus's vocabulary: a REAL POSSIBILITY for the developed-market third, a LOW-LEVEL POSSIBILITY for
  the whole company.** The reason is in the same filings: retail is concentrated in North America and parts of Europe and not
  elsewhere, and the regions where it is not concentrated did not lose margin over the decade — **Latin America 31.0% to
  29.6%, Europe 24.7% to 25.3%, Africa/Eurasia 19.4% to 21.8%, Asia Pacific 31.7% to 27.0%**, against North America's 32.4% to
  21.5%. **Two thirds of the profit sits where no single customer has 11% of anything.** That is what keeps this a
  low-level possibility for the company and a real one for a third of it.
- **[E2-27]'s collective-irrationality mechanism is the aggravator and is named:** every branded staple in the Q2 row raised
  price 2021-2023 and gave some back in 2025, and each one's advertising rose as a share of sales. *"Viewed individually, each
  company's capital investment decision appeared cost-effective and rational; viewed collectively, the decisions neutralized
  each other."* Advertising at 13.3% of sales that holds a share still 3.4 points below 2015's is that pattern in miniature.
- **Exposure, not experience [E4-40].** The benign reading — that Colgate has held 39-45% of global toothpaste for twelve years
  and earns 79-101% pre-tax on tangible operating capital — is the *experience*. The *exposure* is one customer at 11%,
  retailer consolidation the 10-K says *"may further increase our concentration risk"*, a private-label substitute on the same
  shelf, and algorithmic category pricing the filing names by name.

**SURVIVAL SHAPE.** Against `Screens/SURVIVAL SHAPES - index.md`: this is close to **#11 THE PASS-THROUGH** but is not it — the
gains are not competed away by rivals or absorbed by suppliers, they are **taken by one concentrated counterparty at the point
of sale**. It is the inverse of **#13 THE TENANT**: there, the product is rented and the rent is reset; here the **product is
owned outright and the distribution is rented**. **A new shape is therefore proposed, pending the operator, in the form the
other six proposals used: #19 THE SHELF — the brand is owned, but the route to the buyer is rented from a counterparty who
stocks a cheaper copy beside it, holds the buyer's data, and reprices the terms every year.**

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *IN on survival, without strain. **Owner earnings exist, are built by hand from the filed cash-flow statements, and are
  positive in every year of the perimeter window**, with a worst year of $1,735M in 2022 and a range carried to Q5 of about
  **$2.7bn to $3.3bn**, centred on the five-year default of **$2,833M**, with the windage spent twice and counted. **[E5-20] was
  asked on the filing and answered: Colgate is not in the exception class**, capex being 1.15x depreciation and 1.01x D&A over
  the decade; (c) is nevertheless set at total capex on **[E4-47]**'s inflation condition, evidenced by Latin America's own
  1.35x. **[E4-20]: GREAT** — owner earnings per share compounded 5.3% a year on tangible operating capital that did not grow.
  **Staying power scores 2 of 3 [E5-11]:** the earnings stream and the maturity profile pass comfortably (interest covered
  **13.5x** after capex, largest maturity year $1,115M against $4,198M of operating cash), and **strength 2 fails — $1,370M of
  cash is not "massive liquid assets", and the filing points at an undrawn revolver behind its commercial paper, which is
  [E5-39]'s kindness of strangers.** That is recorded as a real weakness and it is not what kills this business. **The named
  death is not insolvency but the slow transfer of the franchise's rent to the owner of the shelf**, modelled above at roughly
  a halving of owner earnings over a decade, **a real possibility for the developed-market third and a low-level possibility
  for the whole**, because two thirds of the profit is earned where no customer has 11% of anything. The file continues to Q5.*

## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**Q1, Q2, Q3 and Q4 all returned IN, so this output is reportable under operator protocol 2.** It is not headed
"COMPUTATION — NOT A CLEARANCE", because the hard sequence was satisfied before it was run.

### THE PAIR IS STRUCK FRESH, AND BOTH PAIRS ARE RECORDED
**[E4-15]** asks for *"the currently observed rate"*, and Step 0's pair is five days old, so both were struck again.
- **Struck at Step 0 on 2026-09-13, left as filed and NOT used below:** USD 30-year **5.35%** (09/11/2026); price
  **US$86.80** (close of 2026-09-11); cap **US$69,194.6M**.
- **STRUCK FRESH THIS SESSION, 2026-09-18, and used for every figure below:**
  - **Sovereign: USD 30-year 5.29%, dated 09/17/2026, US Treasury daily par yield curve** — the issuing authority, through
    `tools/sources.py sovereign("USD")`. **Not FRED**, which is the fallback only. 09/17 is the latest business day the
    curve carries on 2026-09-18.
  - **Price: US$87.73, close of 2026-09-17**, through `tools/sources.py price()`. **Aggregator, flagged: live quote only.**
    *Cross-checked against a primary filing, which is a stronger check than usual: the eight Forms 4 filed 2026-09-15 report
    RSU-vesting tax withholding at* **$86.80** *on 2026-09-11 — the identical figure the same aggregator gave Step 0 for that
    date.*
  - **Share count re-confirmed, not inherited:** **797,172,829**, from the cover of the 10-Q for the quarter ended
    2026-06-30, accession **`0000021665-26-000042`**. **EDGAR was re-queried on 2026-09-18** (CIK 0000021665): the only
    filings since 2026-09-13 are **eight Forms 4 dated 2026-09-15**, all transaction code **F**, *"Withholding of shares for
    payment of tax liability incident to the vesting of restricted stock units"* — no open-market sale, and **no new 10-Q,
    10-K or 8-K**. The cover count therefore stands and the split factor after the measurement date is **1.0**.
  - **MARKET CAP, recomputed on the fresh close: 87.73 × 797,172,829 × 1.0 = US$69,936.0M.**
- **FX:** none. The quote is in USD on the NYSE and the statements are in USD. The currency argument for using the USD
  sovereign against a two-thirds-international earnings stream was made at Step 0 and is not re-opened.

### 1. THE YIELD — owner earnings over market cap, beside the sovereign
*(Arithmetic in `resume/q5.py`. Owner-earnings windows are Q4's, unchanged.)*

| window | owner earnings $M | yield on $69,936M | multiple | points vs the 5.29% sovereign | expectancy = yield + realised growth (5.3%) | vs the ~10% floor |
|---|---|---|---|---|---|---|
| most conservative (10-yr, working-capital release stripped) | 2,680 | 3.83% | 26.1x | **-1.46** | 9.13% | **-0.87** |
| 10-yr 2016-25 | 2,738 | 3.92% | 25.5x | **-1.37** | 9.22% | **-0.78** |
| **5-yr 2021-25 — the [E2-42] DEFAULT** | **2,833** | **4.05%** | **24.7x** | **-1.24** | **9.35%** | **-0.65** |
| 3-yr 2023-25 | 3,269 | 4.67% | 21.4x | **-0.62** | 9.97% | -0.03 |
| TTM to 2026-06-30 *(one year, not a mean)* | 3,680 | 5.26% | 19.0x | **-0.03** | 10.56% | +0.56 |

**On every window, including the trailing twelve months, the owner-earnings yield is BELOW the thirty-year Treasury.**
The growth term is the only thing that lifts the expectancy above the bond, and it is the realised 2016-2025 compound rate of
owner earnings per diluted share (**$2.70 to $4.29, +5.3% a year**) taken at face value — which is generous, because Q2 showed
that growth was price and that most of the price was devaluation recovery.

### 2. WHAT THE PRICE ALREADY ASSUMES
| window | perpetual growth in owner earnings per share needed to reach the ~10% floor | needed merely to match the 5.29% bond |
|---|---|---|
| most conservative | **6.17%/yr** | 1.46%/yr |
| 10-yr | **6.08%/yr** | 1.37%/yr |
| **5-yr default** | **5.95%/yr** | **1.24%/yr** |
| 3-yr | 5.33%/yr | 0.62%/yr |
| TTM | 4.74%/yr | 0.03%/yr |

**Against what the business has actually done:** +5.3% a year in owner earnings per share over 2016-2025, of which about
**1.1 points a year came from the share count alone** (898.4M diluted to 811.1M) and the rest from price, with **worldwide
unit volume up 7.7 points in ten years and the Oral, Personal and Home Care segment up 2.9**. **So $87.73 requires the best
decade the filings show, repeated in perpetuity, and slightly bettered.**
- **[E4-35] is NOT the binding constraint here and is not misapplied:** 5.95% is not a claim of *"15% annual growth in
  earnings-per-share"*, so the fewer-than-10-of-200 base rate does not fire. **What fires instead is [E4-44]'s second bound** —
  *"the value of an asset, whatever its character, cannot over the long term grow faster than its earnings do"* — and the
  earnings growth on offer is the pricing Q2 measured.
- **State the ceiling too [E2-63].** The upside is bounded, and the bound is nameable: return on average net tangible
  operating assets is already **79%-101% pre-tax** and cannot usefully rise, so growth must come from units, price or the
  share count. Units have been flat for a decade; hard-currency pricing has run at about 1% a year; the buyback adds about 1.1
  points a year and is itself being done at $78.54-$95.90 a share. **There is no source of a step change in the filings.**

### 3. WHAT YOU ARE PAID — and the value range, in round numbers [E4-01]
**Value per share at the [E4-28] floor, at three growth assumptions, value = owner earnings / (10% − g):**

| window | g = 5.3% *(the full realised decade rate, granted)* | g = 3.0% *(hard-currency pricing ~1% + buyback ~1.1% + a point)* | g = 0% *(static)* |
|---|---|---|---|
| most conservative | $71.53 | $48.03 | $33.62 |
| 10-yr | $73.08 | $49.07 | $34.35 |
| **5-yr default** | **$75.61** | **$50.77** | $35.54 |
| 3-yr | $87.25 | $58.58 | $41.01 |
| TTM | $98.22 | $65.95 | $46.16 |

**THE RANGE, in round numbers as [E4-01] requires: roughly $50 to $75 a share on the corpus's default five-year window,
widening to roughly $50 to $90 only if the three-year window and the full decade growth rate are both granted at once.**
The quote is **$87.73**.

**No end margin is subtracted on top, and the reason is stated.** *"you don't try and put too much windage in at every level
... And then when you get all through, you apply the margin of safety"* **[E4-11]**. **Q4 already spent conservatism twice and
counted it** (c) set at total capex rather than the depreciation default, and the working-capital release stripped. Applying a
third discount here would be exactly the stacking the framework forbids. **The range above is therefore the honest value, not a
value net of margin; the margin is what the gap between it and the price would have to be, and there is no gap.**

**Bar 2, the screamer test [E4-01, E3-25]:** the conservative end of the range is about **$48-$51**. The price is **$87.73**.
It does not *"scream"*; it sits **above the whole default-window range** and only inside the widest range if two optimistic
choices are made together. **Bar 2's answer for this cell of the table is "no".**

- **THE FLOOR COMES FIRST, AND IT IS NOT CLEARED.** *"that's the figure we quit on ... we don't want to buy equities where our
  real expectancy is below 10 percent. Now, that's true whether short rates are 6 percent or whether short rates are 1
  percent"* **[E4-28]**. On the corpus's own default five-year window the honest pre-tax expectancy at $87.73 is **9.35%**,
  **0.65 points below the floor** — and that figure already grants the full realised decade growth rate. On the ten-year window
  it is 9.22%. Only the trailing-twelve-months reading, a single year rather than a mean, clears it, at 10.56%.
- **RANKING POSITION: NOT RANKED.** A candidate below the floor *"is not ranked — it is quit on, however it compares with the
  bond of the day."* It is not placed in `PORTFOLIO.md`'s ranked opportunity set as an actionable line.
- **VERDICT: the business is IN and the price is not.** **[ ] IN at this price**  [ ] UNRESEARCHED  [ ] UNKNOWABLE →
  **the four business gates are IN; Q5 returns BELOW THE [E4-28] FLOOR at $87.73, NOT RANKED, WATCH-LIST ONLY.**
  *This is the ASML shape of 2026-08-28 and the PNR shape of 2026-09-01, not a finding against the business. **[E5-42]** is the
  reason the two are reported separately: business quality is *"the capital actually needed in the business"*, and *"whether
  it's a good investment for us depends on how much we pay for that in the end."* Colgate needs very little capital and costs
  24.7 times a conservative year's owner earnings.*

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**No position is held** (CL has no row in `PORTFOLIO.md`), so this section sets the yardsticks **prior to the act**
**[E1-02]** — the entry conditions, and the conditions under which the four IN verdicts above should be re-read as wrong.

### A. THE PRICE LINES, pre-committed, and armed because the business cleared all four gates (the QLYS ruling)
- **$75.61 — the five-year floor value with the full 5.3% decade growth rate granted.** At or below this, the ~10% floor is met
  **on the most generous growth assumption the record supports**. **Action: a full v4.1 re-run, not a purchase** — the growth
  assumption must be re-tested against the then-current share and volume series before it is spent.
- **$50.77 — the five-year floor value on g = 3.0%**, the growth the hard-currency pricing record and the buyback actually
  support. At or below this the floor is met **without granting the devaluation-recovery pricing**. **Action: a full v4.1
  re-run, and this is the price at which the name would be expected to rank.**
- Both are armed in `tools/alerts.json` as **prompts to read, never verdicts**, in the PNR two-band form.
- **These lines expire at the next 10-K.** The bands are derived from owner earnings and must be re-derived when the FY2026
  10-K lands (expected February 2027), per the alerts file's own standing note.

### B. WHAT WOULD PROVE Q2 WRONG — the moat downgrade, and [E4-17] says it arrives slowly
*"we sell — really when we ... reevaluat[e] the economic characteristics of the business ... And those beliefs change quite
gradually."* **[E4-17]**. Each of these is an annual read off the 10-K, not a quote to watch:
1. **Global toothpaste share falls below 39.4%** (the 2021 trough) in any full year. The class NARROW would be re-read as
   NONE, because the 2022-2025 re-widening would have failed.
2. **North American net selling price is negative for a third and a fourth consecutive year.** Two years is the [E4-37] agony
   signal already recorded; four would make it the state of the business rather than a cycle.
3. **Advertising passes 14.0% of net sales while global toothpaste share is still below 41.3%.** That is the cost of holding
   position rising again with nothing bought.
4. **Worldwide volume is negative in two consecutive full years.** [E4-55]'s physical series is the honest one, and two
   negative years would end the "franchise, narrowed" reading.
5. **The Personal and Home Care third loses segment margin while Latin America, Asia Pacific and Africa/Eurasia begin to
   follow North America's path.** That is Q4's named death — **#19 THE SHELF** — spreading beyond the concentrated-retail
   third, and it would move the likelihood from *low-level possibility* to *real possibility* for the whole company.

### C. WHAT WOULD PROVE Q3 WRONG
6. **A fourth impairment of an acquired brand**, or any new adjacency purchase above $1bn while the core's share is falling.
   That is **[E3-40]**'s loss of focus and **[E2-56]**'s camouflage confirmed rather than flagged, and **[E4-24]** is the
   corpus's answer to it: *"you'll probably do better to get out"*, not to engage.
7. **An EBITDA or adjusted-EBITDA measure appearing in any release or filing [E4-29]**, where today the sweep returns zero
   files.
8. **Restructuring charges rising above about 5% of base operating profit**, roughly double the decade's 2.5%, without a
   filed statement of what is being rebased and for how long **[E5-33]**.

### D. WHAT WOULD PROVE Q4 WRONG
9. **Interest cover after capital expenditure falls below 8x** (it is 13.5x), or **operating cash flow falls below $3.0bn in a
   year the filings do not attribute to a raw-material shock**.
10. **Cash and the revolver arrangement change** such that commercial paper is not fully backstopped — strength 2 of
    **[E5-11]** already fails, and this is the line at which that failure would start to matter.

### E. THE STANDING NOTE
**No band, and no entry, repairs a gate.** If any condition in B fires, the price lines in A are void until a fresh run is
done, because a moat downgrade changes the owner-earnings growth term the lines are built on. **And the reverse: a fall to
$50.77 on a business that has failed B is not an opportunity, it is a re-rating.** *"what is smart at one price is dumb at
another"* **[E5-08]**.

## SELF-AUDIT
*Operator rule 6: a run is incomplete until its self-audit is checked. Each line is answered, not ticked.*

- [x] **Questions answered in order; no verdict skipped.** Step 0 and Q1 on 2026-09-13; Q2, Q3, Q4, Q5, Q6 on 2026-09-18,
  each written and committed as it closed (`ea8e241`, `a0f392b`, `32f5edb`, `cf49823`). **Q5 was written only after Q1-Q4 all
  showed IN**, so it carries no "COMPUTATION — NOT A CLEARANCE" heading and is not required to.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat — with one qualification that is stated rather
  than hidden.** Q2 is IN and holds the moat class **PROVISIONAL for Pet Nutrition only (23% of 2025 sales)**, because Nestlé
  Purina and Mars are not SEC registrants. **This is not the protocol violation the rule targets**, because the framework's own
  Q2 text prescribes PROVISIONAL for exactly this case, the provisional part is quantified and does not carry the verdict (the
  verdict rests on Oral Care at 44% of sales, where the row is complete with PG, Unilever and Haleon), and no document exists
  that would resolve it — so it is not UNRESEARCHED either. **Recorded here so an auditor sees it without having to find it.**
- [x] **Every UNRESEARCHED verdict names the artifact and where it lives.** No verdict in this run is UNRESEARCHED.
- [x] **Every UNKNOWABLE verdict states what cannot be known.** No verdict in this run is UNKNOWABLE. **Two disclosure gaps are
  recorded inside IN verdicts** and neither is a document that exists: hyperinflationary remeasurement is inside net income and
  is not separately quantified in any Colgate filing (Q4); and Purina's and Mars's figures are in no SEC filing (Q2).
- [x] **Step 0: the filing was read, with accession number; a figure was cross-checked.** Twelve 10-Ks, the FY2017 10-K/A, five
  10-Qs, three DEF 14As, every 8-K since 2021 with its EX-99. FY2025 net cash provided by operations $4,198M matched between
  companyfacts, `tools/run.py` and the filed statement. **A second, independent cross-check was added this session on the peer
  side** (operator protocol 4 applied to the competitor row, which it does not strictly require): PG's FY2026 filed income
  statement reads `"NET SALES | $ | 87,032"` and `"OPERATING INCOME | 19,748"`, matching the computed 22.7% cell exactly.
- [x] **Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.** Six windows run; the
  **five-year 2021-25 default [E2-42]** is named as the governing one and the spread is carried as part of the range [E4-25].
  **(c) is a disclosed judgment**: total capital expenditures rather than the D&A default, on [E4-47]'s inflation condition,
  with [E5-20] asked on the filing and answered **not** in the exception class. Built by hand from the filed cash-flow
  statements; **no net-income proxy anywhere**.
- [x] **Competitor row filled, or the moat marked PROVISIONAL and UNRESEARCHED.** Ten peers with the same metrics on the same
  construction; the two unmeasurable competitors named with what cannot be measured, and the affected segment marked
  PROVISIONAL as the framework requires.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.** USD 30-year **5.29%, 09/17/2026, US
  Treasury daily par yield curve** — the issuing authority, not the FRED redistribution. The currency choice (USD against a
  two-thirds-international earnings stream) was argued from the documents at Step 0 with its limit stated, and not re-opened.
- [x] **Value stated as a round-number range, not a point estimate.** *"roughly $50 to $75 a share"* on the default window,
  *"roughly $50 to $90"* if two optimistic choices are made together. The cell-by-cell table is shown as the working behind
  the range, never as the answer.
- [x] **One bar chosen, not both; windage count stated.** **Bar 2, the screamer test**, is the bar reported at Q5 and its
  answer is "no". **Bar 1's end margin is deliberately NOT applied on top**, and the reason is written into Q5: **windage was
  spent twice at Q4** — (c) at total capex rather than depreciation, and the working-capital release stripped — and a third
  application would be the stacking [E4-11] forbids. **The count is two, both named, and no third was taken.**
- [x] **Prices dated; aggregator used for live quotes only and flagged.** **$87.73, close of 2026-09-17**, aggregator, flagged.
  Step 0's **$86.80 of 2026-09-11** is recorded beside it as struck-and-superseded, and is independently confirmed by a primary
  filing (the Forms 4 of 2026-09-15 report the same $86.80 for 2026-09-11).
- [x] **Run committed to git.** Six commits, each with a fresh message file and an explicit pathspec; no bare `git commit` and
  no `git add -A` at any point, because the index is shared with a live session working on NCLTY.

### VIOLATIONS AND CORRECTIONS FOUND IN THIS RUN, recorded rather than repaired silently
1. **Two hard-sequence defects in the killed session's `sec_q3_draft.md`, both corrected on the record at Q3:** a leverage line
   asserting *"a franchise's earning power"* before Q2 existed, and a capital-allocation line importing a value range from an
   unrun Q5. The Q5 reference is deleted and the [E5-08](2) test was left OPEN at Q3 and closed at Q5.
2. **An arithmetic error in the same draft, corrected at Q3 with the filed lines:** it put 2016-2025 cash uses at $29,266M
   against "$27,376M of capex-end owner earnings" and concluded a structural reliance on debt. On the filed cash-flow lines the
   uses are $29,326M (its option proceeds of $4,615M do not reconcile to the filed $4,555M) against $28,615M of operating cash
   less capex — a gap of about $711M, roughly a fiftieth of the cash generated.
3. **An over-conservatism in the owner-earnings draft, removed at Q4:** it deducted ESOP dividends from owner earnings as an
   "upper bound". The ESOP note says *"Annual expense related to the ESOP was $ 0 in 2025, 2024 and 2023"* and the shares are
   already inside the count, so the deduction was unjustified and would have been a third spend of conservatism.
4. **Two blank cells in the volume/price extraction, filled from the filings at Q2 and flagged:** Latin America 2018 and
   Africa/Eurasia 2023, both missed by the extractor's sentence pattern, not by the filing.
5. **An error in the resume brief itself, corrected here as the instruction requires.** `_brief_resume_2035.md` section 0 says
   *"Only `SECTION_PG.md` and `SECTION_GIS.md` were finished"* and lists CHD and KMB among those with *"scratch scripts but no
   section"*. **`SECTION_CHD.md` and `SECTION_KMB.md` both exist on disk, complete, written 2026-09-13 20:41**, three minutes
   before the brief's own companion file. Four peer sections were finished, not two.
6. **A tooling defect, and its cause named:** `_research 2026-09-13 CL/ledger.py` crashes with `UnicodeEncodeError` on rows
   containing characters outside cp1252 (it hits [E4-55] and [E2-58]) whenever stdout is the Windows console codepage. It is
   not a data defect and the workaround is `PYTHONIOENCODING=utf-8`. Reported, not patched, because the file belongs to this
   run's scratch folder and the same pattern may exist in other runs' copies.
7. **The WAVE 5 "capex unresolved [E5-20]" label is confirmed a tooling artefact, and the mechanism is now named exactly.**
   The capex fact did not disappear and the line never left the face of the statement: **the XBRL tag changed from
   `PaymentsToAcquirePropertyPlantAndEquipment` (10-K years 2011-2022) to `PaymentsToAcquireProductiveAssets` (2020-2025)**.
   Any reader following only the first tag sees capex stop after FY2022. The filed line reads *"Capital expenditures in the year
   ended December 31, 2025 were $564, an increase from $561 in 2024"*.
8. **A stale line in `PORTFOLIO.md`, reported and NOT edited.** Its header still reads *"Q5 sets no hurdle — it RANKS
   [E4-21]"*, which is the pre-Test-D wording the framework rewrote on 2026-08-28 and which `CLAUDE.md` corrected on
   2026-09-02. The ranked rows beneath it already apply the floor correctly (the ASML row says *"below the [E4-28] floor"*).
   **Left for the operator**: changing a governing header is not this run's to make.

## REGISTER
- **Verdict: [x] IN (about the business) — with the price failing at Q5.**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
- **One line:** *Colgate is a franchise, narrowly — 41.3% of the world's toothpaste dollars, 61.5%-101.0% pre-tax on net
  tangible operating assets across a decade, top of a ten-company competitor row — whose moat has not widened since 2015, whose
  units have grown 7.7 points in ten years while price grew 38 and most of that price recovered devaluation; all four business
  gates are IN, and at **$87.73** the honest pre-tax expectancy on the corpus's default five-year window is **9.35%**, **0.65
  points below the ~10% floor [E4-28]**, so it is **NOT RANKED** and goes to the watch list at **$75.61** and **$50.77**.*
- **If UNRESEARCHED — THE WORK ORDER:** not applicable; no verdict is UNRESEARCHED.
- **If UNKNOWABLE:** not applicable; no verdict is UNKNOWABLE.
- **Named death (Q4):** not insolvency but the transfer of the franchise's rent to the owner of the shelf. **Survival shape #19
  THE SHELF, PROPOSED, pending the operator.**
- **Commits:** Step 0 `d4398ab` · Q1 `0c3de6e` · Q2 `ea8e241` · Q3 `a0f392b` · Q4 `32f5edb` · Q5 and Q6 `cf49823` · this
  audit and the fold, below.
