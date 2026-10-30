# Company Run - The Clorox Company (CLX) - 2026-09-25
**CIK 0000021076. NYSE. Fiscal year ends 30 June. WAVE 7, name 30 of 218 by the order file
(`Screens/_daily/_wave7_order.txt` line 30; `_wave7_done.txt` held 29 lines, the last EXP, when this run
started; both counted by this run, not carried from the brief). Name claimed at dispatch (commit `063170b`,
02:48 local; no `*Run - CLX *.md` existed in `Test Runs/`). Run unattended overnight, 2026-09-25.
Research folder: `Test Runs/_research 2026-09-25 CLX/`. Clorox was one of ten competitor-row peers in the
CL run of 2026-09-13; that run's research folder held the Clorox 10-Ks for FY2021-FY2026 with their Exhibit
99.1 (MD&A and financial statements). Those files were copied into this run's folder and reused; each
accession below was re-checked against a fresh EDGAR submissions pull made by this run. Nothing else of the
CL run's was relied on without re-reading the filing.**

**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

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
- rate **5.47** % · date **09/24/2026** (the newest row the curve carried at 02:49 local on 2026-09-25) ·
  source (issuing authority) **US Treasury daily par yield curve, 30 Yr, `home.treasury.gov`
  daily-treasury-rates.csv for 2026**, struck fresh by this run and saved raw as
  `Test Runs/_research 2026-09-25 CLX/treasury_2026.csv`. Neighbouring rows 5.40 (09/23), 5.29 (09/22).
  **FRED DGS30 was not used.** `tools/run.py CLX` read the same 5.47% on the same date.
- FX if the quote and the earnings differ in currency: **not required for the sovereign.** Note 22 (FY2026
  10-K): net sales **$5,629M United States and $1,091M foreign** of $6,720M (84% domestic); the International
  segment (17% of sales) is a translation exposure, not a reason to change the currency. USD sovereign.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K for the fiscal year ended 2026-06-30 (FY2026), filed 2026-08-07, accession
    `0000021076-26-000034`.** Clorox files its MD&A and financial statements as **Exhibit 99.1 to the 10-K**
    (primary document `clx-20260630.htm`, the exhibit `clx-20260630_d2.htm`); both read: Item 1 whole, Item
    1A, Item 1C, the cover; Exhibit 99.1's MD&A (segment results, liquidity, material cash requirements,
    critical estimates including the Venture Agreement terminal obligation), the four statements, and Notes 1,
    2 (GOJO), 3 (divestitures), 8 (intangibles), 9 (accrued liabilities and the Venture Agreement), 10
    (supply-chain finance), 11 (debt), 22 (segments).
  - **10-Ks FY2025 `0000021076-25-000039`, FY2024 `0000021076-24-000030`, FY2023 `0000021076-23-000037`,
    FY2022 `0000021076-22-000026`, FY2021 `0000021076-21-000016`** (reused from the CL run's folder, each with
    its Exhibit 99.1), and **FY2019 `0000021076-19-000012`, FY2016 `0001206774-16-006893`, FY2013
    `0001206774-13-003034`, FY2010 `0001206774-10-001891`** fetched by this run for the long series (each
    carries three years of cash flow, so FY2008-FY2026 is covered without a gap).
  - **10-Qs for 2025-12-31 (`0000021076-26-000010`) and 2026-03-31 (`0000021076-26-000019`)**, cover and
    balance sheet, for the float-date share count below.
  - **8-Ks read (the perimeter), every one filed since the FY2025 10-K except the earnings releases, which are
    read at Q3:** 2025-10-30 (`0001206774-25-000735`, Item 5.02: the chief operating and strategy officer
    resigns); **2026-01-22 (`0001206774-26-000048`, Items 7.01/8.01: agreement to buy GOJO Industries, maker
    of Purell, for $2.25bn in cash)**; **2026-03-10 (`0001206774-26-000133`, Items 1.01/2.03: a $1.0bn 364-day
    revolver and a $1.25bn delayed-draw term loan for the purchase)**; **2026-04-01 (`0001206774-26-000173`,
    Items 7.01/8.01: GOJO closed)**; **2026-05-11 (`0001193125-26-216807`, Item 8.01: $1.5bn of senior notes,
    4.700% 2031, 4.950% 2033, 5.250% 2036)**; **2026-05-28 (`0001206774-26-000296`, Item 5.02: the chair and
    CEO asks the board to begin a CEO search, stepping down "for health reasons")**; 2026-06-17
    (`0001206774-26-000333`, Item 5.02: a new chief operating officer). **No 8-K and no 10-Q has been filed
    since the FY2026 10-K** (fresh submissions pull, 2026-09-25); the Q1 FY2027 10-Q (quarter ending
    2026-09-30) is not yet due.
- figure cross-checked against the filed statement (say which): **FY2026 net cash provided by operations,
  $612M** (Consolidated Statements of Cash Flows, Exhibit 99.1 p. 31), rebuilt from its own lines: net
  earnings 601 + D&A 247 + stock-based compensation 48 + deferred income taxes 81 - **Venture agreement payment
  476** - other 7 + receivables 151 - inventories 71 + prepaid 2 + accounts payable and accrued 38 - lease
  ROU net 4 + income taxes 2 = **612. Ties.** Net earnings 601 ties to the equity statement (587 to Clorox
  plus 14 to noncontrolling interests).
- *If the filing could not be obtained → **UNRESEARCHED**.* **Not invoked; every rung used was SEC EDGAR
  primary documents.**

**A SOURCE FINDING, recorded because it moves every tool-built number on this name: SEC companyfacts has not
ingested the FY2026 10-K seven weeks after it was filed.** A live pull of
`data.sec.gov/api/xbrl/companyfacts/CIK0000021076.json` made by this run (saved as `companyfacts_live.json`)
carries facts from filings up to the 424B2 of 2026-05-08 and **nothing from accession
`0000021076-26-000034`**. That is why the screen row's `newest_filing` reads 2025-06-30, and why `tools/run.py
CLX`, run today with a fresh cache, still builds its windows from FY2023-FY2025 (`runpy_out.txt`). **The brief's
prior that "the screen's windows are a year stale" is right; the cause is the tagged-data source, not the date
the screen was built.** Every owner-earnings figure in this file is built by hand from the filed cash-flow
statements. REPORTED, NOT PATCHED (see the self-audit).

**THE PERIMETER, checked before anything else. Three events move the windows, and one of them is inside the
newest year.**
1. **GOJO Industries (Purell) was bought on 2026-04-01 for cash consideration of about $2,147M** (Note 2;
   *"Business acquired, net of cash acquired | ( 2,104 )"* in investing cash flow), funded by commercial paper
   and $1.5bn of notes. FY2026 carries one quarter of it: *"the Company recognized $ 211 of Net sales and $ 6 of
   Net earnings attributable to Clorox from GOJO from the acquisition date through June 30, 2026."* The
   unaudited pro forma gives net sales of **$7,331M (FY2026) and $7,882M (FY2025)** against reported $6,720M
   and $7,104M, so GOJO is roughly an $0.8bn-a-year business, about 11% of the enlarged company.
2. **Two disposals: Argentina (March 2024, FY2024, loss on divestiture $240M) and the Better Health VMS
   business (Natural Vitality, NeoCell, Rainbow Light, RenewLife; 2024-09-10, FY2025, loss $118M).** Both
   confirmed from the FY2024 and FY2025 10-Ks; **the brief's general-knowledge belief is verified, not
   dropped.** Both leave the history, so the older windows carry businesses no longer owned (the VMS business
   carried goodwill and trademark impairments of $329M in FY2021 and $445M in FY2023 before it went).
3. **P&G's 20% interest in Glad was bought out on 2026-03-02 for $476M, and the payment runs through
   OPERATING cash flow** (Note 9: *"paid in cash for $ 476 on March 2, 2026 and is reflected in Operating
   activities within the consolidated statement of cash flows"*). Until then *"The Company paid a royalty to
   P&G for its interest in the profits, losses and cash flows, as contractually defined, of the Glad business,
   which is included in Cost of products sold."* So every year up to FY2026 carried a charge that has now
   ended, and FY2026 carries a one-time $476M purchase of it inside operating cash. Both matter at Q4.
4. **The brief's other belief, the cyberattack and the ERP transition, is also verified from the filings**:
   the August 2023 cyberattack cut FY2024 (*"lower shipments resulting from the impacts of the cyberattack"*,
   FY2024 MD&A), and the U.S. ERP cut-over pulled sales from FY2026 into FY2025 (*"certain retailers placed
   orders in advance of the ERP system transition in the U.S. ... the offsetting impacts were reflected in
   fiscal year 2026 net sales as retailers drew down this inventory"*, FY2026 Item 1). **Three of the last
   three fiscal years are distorted by an event, in both directions.**

**THE PRICE AND THE CAP** *(struck by this run; the screen's cap was flagged, and the flag is resolved below)*
- **Share count, quoted from the cover of the FY2026 10-K, accession `0000021076-26-000034`:** *"As of July 22,
  2026, there were 120,931,005 shares of the registrant’s common stock outstanding."* No periodic report has
  been filed since. One equity class: the balance sheet reads *"Preferred stock: $ 1.00 par value; 5,000,000
  shares authorized; none issued or outstanding"* and *"120,926,454 and 122,694,263 shares outstanding as of
  June 30, 2026 and 2025"*; the cover registers one class, *"Common Stock - $1.00 par value"*, NYSE. No classes
  were summed.
- **Price $81.80** (close 2026-09-24, **aggregator quote, flagged**: Yahoo Finance chart endpoint,
  `regularMarketTime` 2026-09-24 20:00 UTC; raw responses saved as `price_raw.json` and
  `price_hist_raw.json`). **$81.80 is the lowest close in the two-year series pulled**, which runs from $169.74
  down; the price has fallen every week since 2026-08-28 ($102.53). No split in the window.
- **cap = close x shares**, split-invariant, `close` never `adjclose`: $81.80 x 120,931,005 = **$9,892 million.**
- **The screen flag, resolved: neither number is wrong; they are a year apart and the price fell 37% in
  between.** The row read *"cap $12,426M against a filed float of $19,900M (1.60x) as of 2024-12-31."* The
  float is the FY2025 10-K's: *"The aggregate market value of the registrant’s common stock held by
  non-affiliates as of December 31, 2024 [...] was approximately $ 19.9 billion."* The close that day was
  **$162.41**. The cap came from the operator's source list (`Screens/2026-08-31 PREPPED LIST.csv`, cap_m
  12426), an implied price of about $101.6 on the FY2025 cover count, a level CLX traded at in December 2025
  and April 2026. **The guard in `Screens/regen_queue.py` compares a cap at one date with a float at another**,
  and for a stock that has fallen by more than a third between the two dates it fires on correct inputs. The
  newer float confirms both: the FY2026 cover gives *"approximately $ 12.2 billion"* at 2025-12-31, and
  120,890,241 shares (10-Q balance sheet, `0000021076-26-000010`) x $100.83 (close that day) = **$12,189M**,
  i.e. the float is essentially the whole company and ties. REPORTED, NOT PATCHED (see the self-audit).

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words, no management language:** Clorox makes cheap, frequently repurchased
  household goods (bleach and disinfecting wipes, trash bags, cat litter, charcoal, salad dressing, water
  filters, lip balm, and since April 2026 hand sanitizer and its wall dispensers), mostly in its own plants, and
  sells them to retailers, who resell them to households. **Walmart alone took 26% of FY2026 net sales and the
  five largest customers about half** (Item 1). Revenue is units shipped times the net price after trade
  promotion; cost is resin, chemicals, corrugate, soybean oil and freight on the way in, then about 11% of
  sales in advertising to keep the consumer asking for the brand by name (*"Advertising costs | 749 | 770"*, 11.1%
  and 10.8% of sales). FY2026, filed segment tables (Exhibit 99.1 of `0000021076-26-000034`): **Health and
  Wellness** $2,697M of net sales, segment adjusted EBIT $678M (25%); **Household** (Glad, Fresh Step and Scoop
  Away, Kingsford) $1,787M, $192M (11%); **Lifestyle** (Hidden Valley, Brita, Burt's Bees) $1,123M, $208M
  (19%); **International** $1,113M, $113M (10%); corporate costs $(161)M. Consolidated net sales $6,720M, gross
  margin 42.3%, earnings before income taxes $791M, net earnings attributable to Clorox $587M. **By product
  line, cleaning is 44% of sales, bags and wraps 15%, food 11%, cat litter 10%** (Note 22).
- **The scarce input this business controls:** **the consumer's habit of buying a named brand at a price
  above the store's own label, and the shelf space that habit earns from the retailer.** Item 1: *"Over 80% of
  the Company’s sales are generated from brands that hold the No. 1 or No. 2 market share positions in their
  categories"*, and *"The Company’s products compete with other nationally advertised brands and with “private
  label” brands within each category."* Every input to the physical product (bleach, resin film, clay litter,
  charcoal) is available to anyone, and the 10-K says so of its own raw materials (*"numerous unaffiliated U.S.
  and international suppliers"*). Whether the habit is strong enough to be a franchise is Q2's question, not
  this one's.
- **Will the fundamentals look broadly the same in ten years?** **Yes.** The FY2010 10-K
  (`0001206774-10-001891`) describes the same brands sold through the same channels (Clorox, Pine-Sol, Glad,
  Kingsford, Fresh Step, Hidden Valley, Brita, Burt's Bees), the same Walmart concentration (*"Net sales to the
  Company’s largest customer, Wal-Mart Stores, Inc. and its affiliates, were 27% for fiscal years 2010 and
  2009"*), and the same *"“private label”"* competition. What has changed is the perimeter at the edges (the
  Armor All and STP auto-care brands, still in the FY2010 10-K, since gone; the Nutranext supplements business
  bought on April 2, 2018 and sold as Better Health VMS in 2024; Argentina sold 2024; GOJO bought 2026), not the
  kind of business. The moving parts the filing names (retailer
  power, private label, commodity and freight costs, tariffs, the ERP system) are understandable; they are Q2
  and Q4 questions.
- **VERDICT: [x] IN**
  *A maker of branded household consumables sold through a few large retailers. Every figure above is off the
  filed FY2026 statements, Item 1 and the FY2010 10-K; nothing rests on "unverified", "general knowledge" or
  "provisional". The business can be stated in five sentences, and the two general-knowledge priors the brief
  carried (the disposals, the cyberattack and ERP disruption) were checked against the filings before being
  used.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**
- Needed or desired **[x]** · no close substitute **[ ] NOT SHOWN for the company; argued below segment by segment** ·
  not price-regulated **[x]** (household consumables are not price-regulated; EPA registration of disinfectant claims
  governs entry to a label claim, not the price)

**The test the corpus attaches to the three conditions, and the two tests that sharpen it.** [E3-03]: *"The existence of
all three conditions will be demonstrated by a company's ability to regularly price its product or service aggressively
and thereby to earn high rates of return on capital."* [E2-44] states the pricing half as a test that can be failed:
*"(1) an ability to increase prices rather easily (even when product demand is flat and capacity is not fully utilized)
without fear of significant loss of either market share or unit volume, and (2) an ability to accommodate large dollar
volume increases in business (often produced more by inflation than by real growth) with only minor additional investment
of capital."* [E4-47] states the inflation half: *"The best business to have during inflation is one that retains its
earning power in real dollars without commensurate investment."* And [E4-55] says which series to trust when the two
disagree: *"This decline in physical volume is a serious reverse, not likely to disappear in some "bounce back" effect."*
All four are run below on Clorox's own filed figures, sixteen fiscal years, before the competitor row is read.

- **Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04]** No. Bleach, trash bags,
  charcoal, cat litter and salad dressing are not in the rapid-change class, and a brand is defended by advertising, not
  replaced (the scope paragraph's Coca-Cola case). [E4-04]'s perimeter close (UNKNOWABLE) is **refused in writing**: the
  filings answer the franchise question. Nothing in the record makes the business depend on one manager [E4-23]; the CEO's
  announced departure for health reasons (8-K 2026-05-28) is a Q3 and Q6 matter.

### THE SUBJECT'S OWN RECORD, FY2011-FY2026 (working files `ntoa.py` / `ntoa_out.md`, `oe.py`, the 10-K MD&As)
EBIT = earnings (continuing) before income taxes plus interest expense, from the filed income statements (10-Ks FY2013
`0001206774-13-003034`, FY2016 `0001206774-16-006893`, FY2019 `0000021076-19-000012`, FY2022 `0000021076-22-000026`, FY2025
`0000021076-25-000039`, FY2026 `0000021076-26-000034`). "Charges" are the filed impairment, divestiture-loss and pension
settlement lines (FY2011 Burt's Bees goodwill $258M; FY2021 VMS $329M; FY2023 VMS $445M; FY2024 Argentina loss $240M and
pension $171M; FY2025 VMS loss $118M). NTOA is the CL run's definition (total assets less cash, goodwill, intangibles and
operating ROU assets, less current liabilities net of short-term debt and current lease liabilities); balance-sheet inputs
FY2010-FY2025 from companyfacts, **FY2026 typed from the filed balance sheet, and FY2025 recomputed from the filed balance sheet
as the cross-check: 1,438 both ways.** Volume is the MD&A's total-company figure: *reported* volume FY2011-FY2019 (includes the
RenewLife and Nutranext supplement acquisitions, since sold), *organic* volume FY2020-FY2026 from the filed bridge tables.

| FY | net sales $M | gross margin | EBIT $M (GAAP) | EBIT margin, ex-charges | pre-tax return on avg NTOA, GAAP / ex-charges | volume | price/mix |
|---|---|---|---|---|---|---|---|
| 2011 | 5,231 | 43.5% | 686 | 18.0% | 34.9% / 48.0% | 0 | n/t |
| 2012 | 5,468 | 42.1% | 916 | 16.8% | 47.9% | +2 | n/t |
| 2013 | 5,623 | 42.9% | 975 | 17.3% | 50.4% | 0 | +2.7 (filed "approximately 270 basis points") |
| 2014 | 5,514 | 42.7% | 987 | 17.9% | 62.0% | 0 | n/t |
| 2015 | 5,655 | 43.6% | 1,021 | 18.1% | 85.1% | +2 | n/t |
| 2016 | 5,761 | 45.1% | 1,071 | 18.6% | 95.1% | +4 | n/t |
| 2017 | 5,973 | 44.7% | 1,121 | 18.8% | 94.4% | +6 | n/t |
| 2018 | 6,124 | 43.7% | 1,139 | 18.6% | 86.6% | +3 | n/t |
| 2019 | 6,214 | 43.9% | 1,121 | 18.0% | 78.5% | +2 | n/t |
| 2020 | 6,721 | 45.6% | 1,284 | 19.1% | 95.7% | **+10** | 0 |
| 2021 | 7,341 | 43.6% | 999 | 18.1% | 72.9% / 96.9% | **+6** | +3 |
| 2022 | 7,107 | 35.8% | 713 | 10.0% | 44.1% | **-5** | +3 |
| 2023 | 7,389 | 39.4% | 328 | 10.5% | 20.4% / 48.2% | **-10** | **+16** |
| 2024 | 7,093 | 43.0% | 488 | 12.7% | 29.7% / 54.8% | **-5** | +5 |
| 2025 | 7,104 | 45.2% | 1,166 | 18.1% | 72.2% / 79.5% | **+7** | -1 |
| 2026 | 6,720 | 42.3% | 921 | 13.7% | 51.9% | **-7** | 0 |

*(n/t: not tabulated in that year's filing in this form; the sentences give reported volume only. FY2025 carries about 3.5
points of ERP pull-forward and a $70M cyberattack insurance recovery; FY2026 carries the reversal of the pull-forward, about
7.5 points, and one quarter of GOJO.)*

**What the record shows, in four readings.**

1. **High returns on tangible capital, every year: the half of [E3-03]'s demonstration that is met.** Pre-tax return on
   average net tangible operating assets was never below 44% in any year once the filed charges are set aside, and ran
   78-96% for FY2015-FY2021. Through a cyberattack (August 2023), an ERP cut-over, a pandemic surge and its reversal, and
   three write-downs, the business kept earning more than a third of its tangible capital every year. That is [E3-43]'s
   *"franchises can tolerate mis-management"* in the form a filing can show it, and it is the strongest evidence against
   the verdict below. **It is also what every branded staple in the competitor row earns** (see the row: KMB 24-37%, CHD
   59-116%, CL 61-101%, PG 78-92%, and the two names this project has already closed OUT at Q2 on the business, General Mills
   and J.M. Smucker, 25.8-396.6% (flagged there as distorted by a small denominator) and -21.2% to 61.0% on the same construction in the CL run's row). Asset-light, negative-working-capital
   distribution of branded goods earns high returns on tangible capital as a class. [E3-46]'s *"has it earned high returns on
   capital?"* is answered yes; it does not separate Clorox from the businesses that failed this gate.

2. **The pricing half: [E2-44]'s first characteristic fails on the registrant's own words, repeatedly, in the flagship
   categories.** The test is to raise price *"without fear of significant loss of either market share or unit volume"*. The
   MD&As, verbatim:
   - FY2014 (10-K `0001206774-14-002682`): *"lower shipments due to heightened competitive activity in the disinfecting
     wipes category, including the distribution loss of Clorox ® disinfecting wipes at a major club customer; lower shipments
     of Glad ® trash bags, primarily due to a price increase in the second half of fiscal year 2014"*.
   - FY2015 (10-K `0001206774-16-006893`): *"lower shipments of Clorox ® liquid bleach due to the February 2015 price
     increase, category softness and increased competition; and lower shipments of Brita ® water-filtration products,
     primarily due to continuing category softness and increased competition."*
   - FY2019 (10-K `0000021076-19-000012`, Household): *"Volume decreased, primarily driven by lower shipments of Glad ® bags
     and wraps, mainly due to wider price gaps compared to a year ago and distribution losses, and lower shipments in
     Charcoal, mainly due to distribution losses and lower merchandising activity."*
   - FY2023 (10-K `0000021076-23-000037`): *"Volume decreased by 10% versus the prior year primarily due to pricing
     actions."* Price/mix was +16 points; by segment, Household +13 price and -7 volume, Lifestyle +11 and -4, International
     +16 and -5, Health and Wellness +20 and -16 (the last carrying the unwinding of pandemic disinfecting demand).
   - FY2026 (10-K `0000021076-26-000034`, Lifestyle): *"The volume decrease was primarily due to lower shipments in the
     current period following the incremental shipments related to the ERP transition in the fourth quarter of fiscal year
     2025 and lower consumption. The variance between volume and net sales was mainly due to higher trade promotion
     spending."* Lifestyle volume -12 against about 7.5 points of ERP reversal company-wide, price/mix -2.
   **Bleach, wipes, trash bags, charcoal and water filters, each named by the company as losing units to its own price or to
   competition.** The price did stick after FY2023 (price/mix -1 in FY2025, 0 in FY2026, gross margin back to 45.2% in
   FY2025), so this is not General Mills' pattern of price handed back. It is the other failure [E2-44] names: the price
   held and the units went.

3. **The physical series [E4-55]: units have not come back.** Chaining the filed organic volume, FY2019 = 100: FY2020 110,
   FY2021 117, FY2022 111, FY2023 100, FY2024 95, FY2025 101, **FY2026 94**; the two-year mean of FY2025-26, which nets the
   ERP pull-forward against its reversal, is **about 98**. Seven years after FY2019, with price/mix up about 28% (FY2021-26
   chained: +3, +3, +16, +5, -1, 0), Clorox ships slightly fewer units than it did before the pandemic. This is not Precision
   Steel's one-third fall, and three of the seven years carry a named disruption. It is also not the record of a product
   *"thought by its customers to have no close substitute"*: the units lost to the FY2023 price did not return when the
   cyberattack and ERP effects were lapped.

4. **The inflation test [E4-47]: nominal earning power is below FY2019.** GAAP EBIT $1,121M in FY2019 and **$921M in
   FY2026**; the company's own adjusted EBIT (*"Total | $ | 1,030"*, segment adjusted EBIT less corporate, FY2026 MD&A) is
   also below FY2019's GAAP figure, which carried no adjustment. The best year since, FY2025's $1,284M ex-charges, carried
   the ERP pull-forward and a $70M insurance recovery. Across seven years of general inflation the business raised price
   about 28% and did not raise its operating profit in nominal dollars; in real dollars it fell. **And the company's own
   forward statement says the pricing that would restore it is not available now** (8-K `0000021076-26-000028`, EX-99.1,
   2026-08-03, FY2027 outlook): *"Gross margin is expected to be about 42%, reflecting higher-than-normal inflationary
   headwinds and negative mix more than offsetting the benefits from cost savings."* That is [E4-37]'s *"agony they go
   through in determining whether a price increase can be sustained"*, stated by management as a plan.

**By segment, because the whole company is not one business (filed segment tables, FY2020 10-K `0000021076-20-000016` for
FY2018-19 on the current segment basis, FY2026 10-K for FY2024-26).** Segment earnings before income taxes FY2018 / FY2019
against segment adjusted EBIT FY2024 / FY2025 / FY2026, $M: **Health and Wellness 550 / 570 against 719 / 840 / 678**
(margin 23.5% in FY2019, 28.9% / 31.1% / 25.1%; FY2019 included the supplement business since moved out, and FY2026 includes
one quarter of Purell); **Household 384 / 337 against 260 / 325 / 192**; **Lifestyle 253 / 264 against 253 / 290 / 208**;
**International 84 / 96 against 122 / 110 / 113.** *(The two measures differ in name; the FY2019-basis figure is the
segment's "Earnings before income taxes" and the recent one "Segment adjusted EBIT"; both exclude interest and the
corporate charges, and they are shown side by side, not ranked.)* **The cleaning and disinfecting business (Clorox,
Pine-Sol, Liquid-Plumr, CloroxPro, now Purell) is the one leg that raised its nominal earnings and its margin across the
period, and it is where a franchise case would have to rest**; its units, chained the same way, are about 8% below FY2019
(FY2020 +15, FY2021 +7, FY2022 -9, FY2023 -16, FY2024 -4, FY2025 +11, FY2026 -8), and its flagship liquid bleach lost units
to its own price in FY2015 as quoted above. **Household (Glad, Fresh Step, Kingsford; 26% of FY2026 sales) earned less in
FY2026 than in FY2018 in nominal dollars on a larger sales base, and Lifestyle (Hidden Valley, Brita, Burt's Bees; 17%)
earned less than in FY2019.** Together with International (17%, flat earnings for seven years) that is 60% of sales whose
earnings did not keep pace with inflation.

**THE COMPETITOR ROW — required [E3-28].** A moat is a claim about *relative* position.

*Row 1, company level, same construction.* The CL run of 2026-09-13 built this row from each filer's own statements with the
NTOA definition used above (`_research 2026-09-13 CL/peers/peer_metrics.py`; accessions in that run's Q2). **Reused, with
the Clorox cells re-derived by this run**: organic volume and price/mix re-read from the Clorox bridge tables (identical);
the NTOA return re-computed here on EBIT (pre-tax plus interest) rather than the CL run's operating profit, which is why the
Clorox figures differ by a few points from the CL run's 67.6 / 46.3 / 25.4 / 31.2 / 66.8. The peers' cells are the CL run's
and were not re-derived; they are the CL run's evidence, cited, not this run's.

| company (fiscal years) | operating margin | pre-tax return on avg NTOA | organic volume | price (or price/mix) | source |
|---|---|---|---|---|---|
| **Clorox (FY21-26, Jun)** | **13.6 / 10.0 / 4.4 / 6.9 / 16.4 / 13.7** (EBIT, GAAP) | **72.9 / 44.1 / 20.4 / 29.7 / 72.2 / 51.9** | **+6 / -5 / -10 / -5 / +7 / -7** | **+3 / +3 / +16 / +5 / -1 / 0** | this run, 10-Ks above |
| Procter & Gamble (FY21-26, Jun) | 23.6 / 22.2 / 22.1 / 22.1 / 24.3 / 22.7 | 91.7 / 85.2 / 83.0 / 81.5 / 84.6 / 77.8 | +3 / +2 / -3 / 0 / +1 / 0 | +1 / +4 / +9 / +4 / +1 / +1 | CL run row |
| Colgate-Palmolive (FY21-25, Dec) | 19.1 / 16.1 / 20.5 / 21.2 / 16.2 | 84.7 / 61.5 / 76.0 / 91.0 / 79.0 | +1.0 / -2.0 / -0.5 / +3.1 / -0.4 | +3.5 / +9.5 / +10.0 / +4.4 / +2.1 | CL run |
| Church & Dwight (FY21-25, Dec) | 20.8 / 11.1 / 18.0 / 13.2 / 17.4 | 106.5 / 59.3 / 98.4 / 72.0 / 116.1 | +1.0 / -5.1 / +0.9 / +3.3 / +0.8 | +3.3 / +6.5 / +4.4 / +1.3 / -0.1 | CL run row |
| Kimberly-Clark (FY21-25, Dec) | 13.2 / 13.3 / 11.2 / 16.1 / 14.3 | 30.9 / 31.8 / 24.5 / 37.4 / 31.8 | -4 / -3 / -2 / +0.8 / +2.5 | +2 / +9 / +6 / +1.9 / -0.9 | CL run row |
| Kenvue (FY23-25, Dec) | 16.3 / 11.9 / 16.0 | 89.3 / 63.9 / 78.3 | -2.7 / -1.2 / -2.3 | +7.7 / +2.7 / +0.1 | CL run row |

**In the price-taking year the row separates, and Clorox is at the bottom of it.** Every filer took price in 2022-2023;
Clorox took the most (+16) and lost the most units (-10); Procter & Gamble took +9 and lost 3, Colgate +10 and lost half a
point, Church & Dwight +4.4 and gained 0.9. Over the five comparable years Clorox's operating margin is the lowest in the row
in three of them (FY2022-FY2024), and its return on tangible capital, while high, sits below Procter & Gamble, Colgate and Church & Dwight in
every year.

*Row 2, the trash-bag leg, same product, different measure.* Reynolds Consumer Products (Hefty), transcribed from REYN's
filed 10-Ks by a sub-agent of this run (`peers_reyn/REYN_ROW.md`, every cell with its accession; FY2025 10-K
`0001628280-26-005284`). REYN files only segment adjusted EBITDA, so Clorox's Household segment is put on the same basis by
adding its filed segment D&A to its segment adjusted EBIT (Note 22; arithmetic only). **The scopes differ**: REYN's Hefty
Waste & Storage is trash and food bags, some store-brand; Clorox Household is Glad plus cat litter plus charcoal, and until
January 2026 carried the P&G royalty on Glad in its cost of products sold.

| | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| Clorox Household, (segment adj. EBIT + segment D&A) / sales | (234+67)/1,984 = 15.2% | (308+78)/2,098 = 18.4% | (260+77)/1,950 = 17.3% | (325+81)/2,001 = 20.3% | (192+85)/1,787 = 15.5% |
| REYN Hefty Waste & Storage, segment adj. EBITDA / revenues (CY) | 21.9% | 27.6% (recast) | 28.2% (recast) | 27.6% | H1: 28.7% (new segment) |
| REYN HWS price / volume-mix | +10 / -3 | +2 / -2 | +1 / +1 (retail) | -1 / +4 (retail) | H1: -1 / nil |

REYN's FY2025 10-K on position: *"We have the #1 branded market share in the U.S. large black trash bag segment, and the #2
branded market share in the food storage bag and tall kitchen trash bag segments."* It names *"The Clorox Company"* first
among its competitors, and it makes store-brand bags itself: *"we produce both branded and store brand trash and food
storage bags"*. **Glad's closest branded rival earns a higher margin on its bags than Clorox earns on the segment that holds
Glad, and sells private label against it from the same plants.** No filed figure shows Glad with a position its competitor
lacks.

*Row 3, the disinfecting leg: Reckitt (Lysol).* Reckitt Benckiser Group plc is not an SEC registrant; the rung is the
company's own English IR site (evidence ladder, rung 3). Transcribed by a second sub-agent of this run from Reckitt's Annual
Reports 2021-2025 and its H1 2026 results announcement of 29 July 2026 (`peers_reckitt/RECKITT_ROW.md`, every cell with its
document, page and URL; PDFs saved raw). GBP; like-for-like; **the scope changes**: 2021-2024 is the "Hygiene" segment
(Lysol with Finish, Vanish, Air Wick, Harpic and others), 2025 onward the "Germ Protection" category (Lysol, Dettol, Harpic),
which carries no profit line. Clorox's Health and Wellness segment is set beside it (fiscal years to June; segment adjusted
EBIT; organic volume and price/mix from the bridge tables).

| | 2021 | 2022 | 2023 | 2024 | 2025 | H1 2026 |
|---|---|---|---|---|---|---|
| Reckitt Hygiene / Germ Protection: volume / price-mix | +5.1 / +2.4 | -12.6 / +9.5 | -6.0 / +11.1 | +1.8 / +2.4 | +6.1 / +2.3 (Germ Protection) | +8.2 / +2.3 |
| Reckitt Hygiene adjusted operating margin | 23.7% | 20.4% | 20.1% | 22.4% | not reported | not reported |
| Clorox Health and Wellness (FY): organic volume / price-mix | +7 / +1 | -9 / -1 | -16 / +20 | -4 / +2 | +11 / -2 | FY2026: -8 / +1 |
| Clorox Health and Wellness segment adjusted EBIT margin | 27.8% | 15.7% | 23.5% | 28.9% | 31.1% | FY2026: 25.1% |

**The disinfecting leg is where the franchise case is strongest, and the row cuts both ways there.** On margin, Clorox's
cleaning segment out-earns Reckitt's broader Hygiene segment in three of the four comparable years. **On the relative claim,
the direct competitor says it has taken share from 2019 on and is still taking it**: Reckitt's Annual Report 2021, *"Lysol has
gained more than 700bps of market share in the US since 2019, driven primarily by growth in the core business: wipes and
disinfectant spray."*; Annual Report 2022, *"Lysol continues to outperform the market and has gained +300bps global market
share since 2019."*; the H1 2026 announcement, *"Lysol grew LFL net revenue high-single-digit in H1 with continued market share
momentum."* Reckitt's volumes turned positive in 2024 and have grown since (+1.8, +6.1, +8.2); Clorox's cleaning units are
about 8% below FY2019. **These are a competitor's own claims about share and are recorded as such, not as a measurement of
Clorox's share, which Clorox does not file.** They agree in direction with every filed Clorox series above. Both companies lost
volume on price in 2022-2023, so part of Clorox's FY2023 unit fall is the category normalising after the pandemic, as the
brief's prior allowed; what the category does not explain is that Lysol's units came back and Clorox's did not.

- Peers named: **company level 5** (P&G, Colgate, Church & Dwight, Kimberly-Clark, Kenvue, each from the CL run's row) plus
  **category level 2** (Reynolds for bags; Reckitt for disinfectants) of the real competitors. **Not measurable from any
  filing, and not filled from memory**: S.C. Johnson (private; Glade, Ziploc, Windex), Nestlé Purina (Tidy Cats; Nestlé is
  not an SEC registrant and does not segment litter), Royal Oak and the private charcoal makers, the private-label
  manufacturers behind the store brands the 10-K names in every category, and Kraft Heinz's dressings (a filer, but not
  segmented at that level). **Not UNRESEARCHED**: no document exists to fetch for a private company, and the verdict does not
  rest on a missing peer; it rests on Clorox's own sixteen-year record and its own sentences, with the row confirming the
  direction.
- **Untapped pricing power [E3-33]? No.** [E5-28] scopes the class to *"a monopoly or a near monopoly"*; the company's own
  claim is *"Over 80% of the Company’s sales are generated from brands that hold the No. 1 or No. 2 market share positions in
  their categories"* (it read *"Nearly 80%"* in the FY2019 10-K), which is category leadership against a named rival and
  private label, not near-monopoly. The FY2027 margin guidance above is the opposite of untapped pricing power.
- **[E2-45], the attacker's test.** A rival does not need to build a brand to take Clorox's units; the retailer that takes
  26% of its sales sells its own label beside it, and in bags the branded rival, Reynolds, makes store brands too. Item 1A says it: *"retailers,
  including club stores, grocery stores, drugstores, dollar stores, mass merchandisers, e-commerce retailers and subscription
  services, which are increasingly offering “private label” brands that are typically sold at lower prices and compete with
  the Company’s products in certain categories."*
- **[E2-53], the dominance class? Not claimed.** No filed share figure puts any Clorox brand in the position of a dominant
  newspaper; the filings say No. 1 or No. 2.
- Class: [ ] WIDE [ ] NARROW **[x] NONE, for the company** [ ] PROVISIONAL · Direction: **down** (units below FY2019,
  nominal EBIT below FY2019, FY2027 gross margin guided below FY2024 and FY2025). The cleaning and disinfecting leg is
  recorded as the one part that shows franchise economics; it is 40% of sales and is not what a buyer of CLX buys alone.
- **VERDICT: [ ] IN  [x] OUT (on the business)  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**
  *Clorox sells branded household staples at a premium to the store's own label, and earns a high return on the little
  tangible capital that takes; every branded staple in the row does the same. The corpus's sharper tests separate the
  businesses the row cannot: [E2-44]'s price rise *"without fear of significant loss of either market share or unit
  volume"* is failed in the registrant's own words for bleach (FY2015), trash bags (FY2014, FY2019) and the company as a
  whole (FY2023, *"primarily due to pricing actions"*); [E4-55]'s physical series stands below FY2019 seven years and about
  28 points of price later; [E4-47]'s real earning power was not kept, EBIT being lower in nominal dollars than in FY2019;
  and the FY2027 outlook says inflation will not be priced through. In the row, Clorox took the most price and lost the most
  units in the price-taking year, and the one leg with franchise margins faces a direct competitor reporting share gains
  since 2019. [E3-03] criterion (2) is not shown for the company. **Not UNKNOWABLE**: the filings answer the question.
  **[E3-47] was weighed before writing this**, because this is a business inside the circle and the closed file is the costly
  error: the cleaning segment's margins and the sixteen-year return on tangible capital are what would make the close an
  error of omission, and they are recorded above as the strongest evidence against it. They do not reach IN because the
  return on tangible capital does not separate this name from General Mills and J.M. Smucker, which this project closed at Q2
  on the pricing test, while the unit, pricing and inflation tests do separate it from Colgate, which it did not. **The contrast
  with the CL run is stated so that the difference is visible rather than implied**: Colgate held 39-45% of the world's
  toothpaste dollars for twelve filed years, its units grew over the decade, and its 2022 and 2023 price increases (+9.5,
  +10.0) came with volume of -2.0 and -0.5; Clorox files no share, its units are below FY2019, and its FY2023 price increase cost it ten points. The file closes
  here, on the business.*

---
⛔ **THE FILE CLOSED AT Q2, OUT ON THE BUSINESS.** What follows is material gathered beneath the close, recorded so the
next reader does not have to fetch it again, and because the brief asked for priors to be tested (the long-window
owner-earnings rebuild [E4-25], the perimeter, the earnings-release read). **None of it carries a verdict. Q5 does not open;
its block is replaced by COMPUTATION - NOT A CLEARANCE, with no box, no ranking and no entry language (operator rules 2 and
3).**

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? MATERIAL ONLY, NO VERDICT
- **Weight case, as it would be declared:** control not ticked (listed shares); leverage not ticked in [E3-29]'s sense (not
  a 20:1 balance sheet; the debt is taken at Q4 below); daily execution ticked in part, because Q2 found the company is
  nearer [E3-43]'s *"a business"* than its *"franchise"* outside the cleaning leg, and trade terms are renegotiated
  continuously with a retailer holding 26% of sales. Not scored further, because Q3 is not reached.
- **Honesty, dated to when each matter became public [E5-16].** The FY2026 10-K's Item 3 describes *"routine litigation
  incidental to its business"*, and Note 14 records environmental remediation liabilities of $28M (Alameda County,
  California, $12M; Dickinson County, Michigan, $10M). No conduct matter, restatement, regulator's finding or fine was found
  in the FY2026 10-K or the 8-Ks since the FY2025 10-K. **No disqualifier found on the filed record read; this is not a
  finding that anyone is honest [E5-17].** The earlier 10-Ks were read for the operating series, not swept for conduct
  matters; a Q3 that opened would sweep them.
- **The earnings release, read before scoring the flags (the CGNX companion rule).** The FY2026 release (8-K
  `0000021076-26-000028`, EX-99.1, 2026-08-03) leads with GAAP net sales, gross margin and diluted EPS, then *"Adjusted EPS 1
  decreased 42% to $1.66"* for the quarter, and gives an FY2027 outlook in both forms (*"Diluted EPS is expected to be between
  $5.41 and $5.71"*; *"Adjusted EPS is expected to be between $5.70 and $6.00"*). **The word EBITDA appears in neither the
  release nor the 10-K's Exhibit 99.1 except inside the revolver's interest-coverage covenant** (*"Consolidated EBITDA"*), so
  **[E4-29] does not fire.** What the company promotes instead:
  - **Adjusted free cash flow that adds back a real cash cost** (MD&A): *"Net cash provided by operations | $ | 612"*, less
    capital expenditures, *"Add: Venture agreement termination payment | 476"*, *"Adjusted free cash flow | $ | 881"*. The
    $476M bought P&G's 20% of Glad; it is capital spent, and a figure that adds it back reports more free cash than
    operations produced. The adjustment is shown line by line, which is [E2-26]'s passing form; the headline figure is the
    one that excludes it.
  - **The same exclusion five years running [E2-57], [E5-33]:** *"Digital capabilities and productivity enhancements
    investment"* is excluded from adjusted earnings in every year FY2022-FY2026, $61M, $100M, $108M, $111M and $59M, $439M
    in all (the filed reconciliations in each 10-K's MD&A). Disclosed at every line, so not concealed; but a cost incurred
    every year for five years is a cost of the business, and *"to tell owners year after year, 'Don't count this'"* is the
    practice [E5-33] names.
  - **Long-term targets against outturn [E4-22] third flag, [E3-48].** The FY2026 MD&A: *"The Company’s long-term financial
    goals reflected in IGNITE include annual net sales growth of 3% to 5% — increased from 2% to 4% in 2021 — annual
    adjusted EBIT margin expansion of 25 to 50 basis points and annual adjusted free cash flow as a percentage of net sales of
    11% to 13%."* Outturn since the 2021 increase: net sales $7,341M (FY2021) to $6,720M (FY2026), a decline, and GAAP EBIT
    margin 13.6% to 13.7% with the ex-charges margin down from 18.1% to 13.7%. **The targets were raised in 2021 and have not
    been met in any cumulative sense since.** A prompt to read, not a verdict.
- **Incentives first [E4-27].** DEF 14A filed 2025-10-07 (`0001552781-25-000311`): the long-term plan pays on economic profit
  (*"Economic profit"* for the PSUs), and *"Performance share units completing their performance period at the end of fiscal
  year 2025 paid out at 133%"*, while the short-term multiplier was 80%, with *"Results exclude the impact of ERP
  transition-related shipments."* Economic profit, as the 10-K defines it, excludes *"asset impairments"*, *"significant
  losses related to divestitures"* and the digital investment. **So the three-year PSU cycle FY2023-FY2025, in which the
  company recorded the $445M VMS impairment, the $240M Argentina loss and the $118M VMS loss, paid 133% of target on a
  measure that excludes all three.** [E2-49]'s yardstick point in its incentive form; prompt only.
- **Capital allocation, the record in the filings [E2-56], [E3-40].** Burt's Bees, *"acquired on November 30, 2007"* (FY2010 10-K; the FY2008 line *"Businesses
  acquired, net of cash acquired"* is $913M), goodwill impaired $258M in FY2011, and its trademark still flagged in FY2026 (*"had 20% or
  less excess fair value over its carrying value"*, carrying value $322M). RenewLife ($290M, FY2016) and Nutranext ($681M,
  April 2018) became the VMS business: impairments $329M (FY2021) and $445M (FY2023), then sold in September 2024 at a
  $118M loss for proceeds of $128M. Argentina sold FY2024 at a $240M loss. GOJO bought April 2026 for $2,147M, debt-funded,
  followed by an S&P downgrade (*"Standard and Poor’s | A-2 | BBB | A-2 | BBB+"*, 2026 against 2025). **The base business
  earned 44-97% pre-tax on tangible capital while roughly $1.9bn went into three supplement and personal-care acquisitions
  against which about $1.15bn was written down or lost on sale ($258M + $329M + $445M + $118M)** (arithmetic
  from the filed lines above; Burt's Bees is still carried). [E3-40]: *"gets sidetracked and neglects its wonderful base business while purchasing other businesses that are
  so-so or worse"* is the prompt; the corpus puts it at Q6 as an exit trigger, not an engagement plan [E4-24].
- **Buybacks [E5-08].** FY2025: 2,260 thousand shares for $332M (about $147 a share); FY2026: 2,157 thousand for $254M (about
  $118). Measured against this run's own computation below (value roughly $6-8bn at the ~10% floor with no growth, $11-14bn
  at the bond rate, or about $51-64 and $94-116 a share), the FY2025 purchases were made above even the bond-rate figure, so
  the second condition, a *"material discount to the company's intrinsic business value, conservatively calculated"*, would
  not be shown met. Stated with [E4-13]: *"They also know a whole lot more about them than I do."* Not scored.
- **Filed-figure tells [E4-30].** Cash taxes paid over pre-tax income: FY2024 87% (347/398, a pre-tax figure cut by
  non-deductible losses), FY2025 24% (264/1,078), **FY2026 13% (104/791)**, which the MD&A explains: *"The lower tax payments
  were a result of the enactment of The One Big Beautiful Bill Act (OBBBA)."* Explained in the filing; prompt only.
  **Serial issuance [E5-15]: no**; shares outstanding fell from 122,694,263 to 120,926,454 in FY2026.
- **Leadership.** The chair and CEO asked the board on 2026-05-26 to begin a search, stepping down *"for health reasons"*
  (8-K `0001206774-26-000296`); no successor had been filed by 2026-09-25. The chief operating and strategy officer resigned
  in October 2025, a new chief operating officer was appointed in June 2026. Recorded for Q6, not scored.

## Q4 — WILL IT SURVIVE? MATERIAL ONLY, NO VERDICT

### Owner earnings **[E2-23]**, rebuilt year by year from the filed cash-flow statements; no net-income proxy
Construction (the framework's CONVENTION): operating cash flow (continuing operations where the filing separates it), less
stock-based compensation from the cash-flow line, less (c). The working-capital increment is inside operating cash flow.
Script `oe.py`, output `oe_out.md`; $M. Sixteen years, because the screen's `da_note` asked for the rebuild across a longer
window than five [E4-25].

| FY | OCF | SBC | D&A | capex | OE, (c) = D&A | OE, (c) = capex | acquisitions |
|---|---|---|---|---|---|---|---|
| 2011 | 690 | 32 | 173 | 228 | 485 | 430 | 0 (auto-care sale +747) |
| 2012 | 620 | 27 | 178 | 192 | 415 | 401 | 93 |
| 2013 | 777 | 35 | 182 | 194 | 560 | 548 | 0 |
| 2014 | 786 | 36 | 177 | 137 | 573 | 613 | 0 |
| 2015 | 858 | 32 | 169 | 125 | 657 | 701 | 0 |
| 2016 | 768 | 45 | 165 | 172 | 558 | 551 | 290 |
| 2017 | 868 | 51 | 163 | 231 | 654 | 586 | 0 |
| 2018 | 976 | 53 | 166 | 194 | 757 | 729 | 681 |
| 2019 | 992 | 43 | 180 | 206 | 769 | 743 | 0 |
| 2020 | 1,546 | 50 | 180 | 254 | 1,316 | 1,242 | 0 |
| 2021 | 1,276 | 50 | 211 | 331 | 1,015 | 895 | 85 |
| 2022 | 786 | 52 | 224 | 251 | 510 | 483 | 0 |
| 2023 | 1,158 | 73 | 236 | 228 | 849 | 857 | 0 |
| 2024 | 695 | 74 | 235 | 212 | 386 | 409 | 0 (sale +17) |
| 2025 | 981 | 81 | 219 | 220 | 681 | 680 | 0 (sale +128) |
| 2026 | 612 | 48 | 247 | 207 | 317 (793 before the Glad buyout) | 357 (833) | 2,104 (GOJO) |

- **Every window, both (c) ends, and the Glad buyout both ways** ($M): 3y FY2024-26 **461-482** (620-641 with the $476M
  added back); 5y FY2022-26 **549-557** (644-652); 10y FY2017-26 **698-725** (746-773); 16y FY2011-26 **639-656** (669-686);
  the five pre-pandemic years FY2015-19 **662-679**. **Combined range, the buyout treated as the purchase of a stream rather
  than a running cost: about $620M to $770M; with it counted as a cost of FY2026, from $460M.** The spread is wide for a
  staple (about 25% top to bottom before the buyout question) and every one of the last seven years carries a named event:
  the pandemic surge (FY2020-21, OCF $1,546M and $1,276M), the cost spike (FY2022), the cyberattack (FY2024), the ERP
  pull-forward and its reversal (FY2025-26), the buyout (FY2026) [E5-11].
- **(c) as a disclosed guess [E2-09, E3-44, E2-41].** Not the capital-intensive exception class [E5-20]: capex ran 2.2-4.5%
  of sales and near D&A across sixteen years (sum FY2011-26 capex $3,382M against D&A $3,105M), the filing gives no sign that
  depreciation understates renewal, and FY2021's $331M included pandemic capacity. **Judged (c): about D&A**, the capex end
  shown beside it; [E4-47]'s caution noted, since the plants are old.
- **Stock compensation [E5-06]: resolves and is complete.** the line appears on every cash-flow statement FY2011-FY2026 (*"Share-based
  compensation"* in the FY2013 10-K, *"Stock-based compensation"* from the FY2016 10-K on; $27-81M, 3-11% of operating cash) and was subtracted in full; [E3-70]'s market-value measure was not rebuilt, so the reported charge is the floor of the subtraction, as that row says it is.
- **The perimeter in the windows.** Every window before FY2025 carries the VMS business (sold September 2024) and every one
  before FY2024 Argentina; none carries GOJO except one quarter of FY2026. GOJO's filed pro forma adds net sales of $611M to FY2026 (beyond
  the quarter already included) and $778M to FY2025 and, after the acquisition interest the pro forma charges (*"Added interest expense of $ 81 and $ 113"*), moves net
  earnings attributable to Clorox by **+$38M in FY2026 and -$95M in FY2025** (625 against 587; 715 against 810). **So on the
  filed pro forma GOJO roughly pays its own financing and adds little to owner earnings on the equity**; the historical
  windows are not understated by leaving it out. **The P&G royalty on Glad ends from February 2026**, which lifts future
  owner earnings by 20% of Glad's contractually defined profit; the amount is not given in the filing read and is not
  estimated here.
- **Do owner earnings bear the acquisitions?** Net acquisition spending averaged **$148M a year FY2011-26** and **$272M a year
  FY2017-26** (GOJO included); without GOJO, $17M and $69M. The supplement acquisitions were bought and sold inside the
  window at a loss.

### Great, good, or gruesome? **[E4-20]**: stated, unticked
Nearer good than great on the filed record: a very high return on the tangible capital the base business needs (44-97%
pre-tax), earned on units that have not grown in seven years, with the growth that was bought (supplements, now Purell)
earning far less on what was paid.

### Staying power, all three scored **[E5-11]**: findings, not a verdict
(1) **Earnings stream:** large and continuous (owner earnings positive in all sixteen years), not reliable in level (the
seven-year spread above). (2) **Liquid assets:** cash $143M at 2026-06-30 against *"current liabilities exceeded current
assets by $949, primarily due to credit obligations maturing within a year"*; undrawn revolvers $1,964M ($764M of it a
364-day facility maturing 2027-03-05, $1,200M to March 2030). (3) **Near-term cash requirements:** notes and loans payable
(commercial paper) $1,086M, the MD&A's material cash requirements $1,551M in FY2027 and $1,324M in FY2028 (debt maturities
with interest $167M and $1,060M), **dividends $602M a year** plus $16M to noncontrolling interests. Long-term debt $3,982M
after $1.5bn of May 2026 notes; net debt about $4.9bn (1,086 + 1 + 3,981 - 143). Interest paid $122M in FY2026, with the
pro forma's full-year acquisition interest of about $81M more to come. **[E2-54]'s coverage test:** operating cash before
the one-time buyout less capex, $1,088M - $207M = $881M, against interest of about $200M on a full year of the new debt:
about four times, met. **[E2-60]'s third dimension:** the dividend ($618M including noncontrolling interests) is about 100% of
owner earnings on the recent windows ($620-650M before the buyout) and more than the three-year figure with it; the debt rose
to buy GOJO and the Glad interest, not to pay the dividend, but the payout leaves nothing retained to repay it.

### The way it dies, named from exposure **[E2-27, E3-24, E4-40]**: named, not scored
Not insolvency: the coverage is four times and the covenant is interest cover of 4.0 on "Consolidated EBITDA". **The
exposure is slow**: the value-seeking consumer and the retailer's own label take units whenever Clorox prices for cost
(FY2014, FY2015, FY2019, FY2023, all in the filings), while the dividend absorbs all of owner earnings and the Purell debt
must be refinanced (the $1,060M of FY2028 maturities with interest). Arithmetic from filed figures: at the FY2022-FY2024
ex-charges EBIT margin of 10-13% on roughly $7.4bn of sales with GOJO, EBIT of about $740-960M, less about $210M of interest,
taxed at 24%, leaves about $400-570M of net earnings against a $618M dividend. **A real possibility**, and it is the
FY2022-24 record repeated, not a new event. A shape from `Screens/SURVIVAL SHAPES - index.md` is not claimed, because Q4 did
not open.

## COMPUTATION - NOT A CLEARANCE
*Arithmetic only. Q5 did not open. No box, no ranking, no entry language.*
- Owner earnings about **$620M to $770M** (the Glad buyout treated as a purchase; **$460M** at the bottom if it is counted as
  a cost of FY2026) against the cap of **$9,892M** ($81.80 x 120,931,005): a yield of **6.3% to 7.8%** (4.7% at the lowest
  construction), against the 5.47% sovereign (09/24/2026), **0.8 to 2.3 points over the bond**.
- Against the ~10% floor [E4-28] the yield falls short by **2.2 to 3.7 points** before any growth is counted. The growth that
  would have to close it, for decades, is set against the record: the owner-earnings mean of FY2011-15 was $538M (D&A end) and
  of FY2022-26 $644M before the buyout, **about 1.6% a year nominal across the eleven years between the two midpoints**, and GAAP EBIT fell between
  FY2019 and FY2026. [E4-35]'s base rate is the burden.
- Capitalised with no growth, the range is roughly **$6bn to $8bn at 10%** and **$11bn to $14bn at the bond rate**, against
  **$9.9bn** now. Round numbers [E4-01]; the ceiling [E2-63] is the unit series, which has not grown in seven years. Windage
  count ONE (the capex end shown beside the judged (c)); the buyout shown both ways is a perimeter question, not windage.
- `tools/run.py CLX` printed 6.45%-6.56% on FY2023-FY2025 (`runpy_out.txt`); it cannot see FY2026 (the companyfacts gap at
  Step 0) and its three-year window contains FY2023's $1,158M of operating cash. It is recorded, not used.

## Q6 — WHAT WOULD PROVE ME WRONG? REVERSAL CONDITIONS, NO POSITION
No alert is armed and no PORTFOLIO.md row is written: the name failed on the business (the QLYS ruling).
**What would reverse the Q2 verdict, in words:**
1. **Units back above the pre-pandemic level while price holds**: the chained organic volume index (FY2019 = 100, about 94
   in FY2026) above 100 on a two-year mean, with price/mix not negative, in the filed bridge tables. That is [E2-44]'s price
   *"without fear of significant loss of either market share or unit volume"* and [E4-55]'s physical series, both passing.
2. **Real earning power restored**: EBIT ex-filed-charges above FY2019's $1,121M by more than the inflation since, for two
   consecutive years that carry no pull-forward or insurance recovery, on the enlarged perimeter with GOJO's contribution
   shown [E4-47].
3. **A filed share figure** (Clorox's own, or a competitor's) showing Clorox holding or gaining share in disinfecting against
   Lysol, which Reckitt's filings currently say is gaining.
4. The next filed tests: the Q1 FY2027 10-Q (quarter to 2026-09-30, due about early November 2026), the FY2027 10-K (about
   August 2027) against the guided *"Gross margin is expected to be about 42%"* and organic growth of 3.5-4.5% with more than
   3.5 points from lapping the ERP drawdown, and the CEO appointment. [E3-30]'s question, cycle or permanent slip, is the one
   to put to the unit series then.

---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN, Q2 OUT. Q3, Q4 and Q6 carry material only; Q5's block is
  replaced by COMPUTATION - NOT A CLEARANCE with no box and no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 rests on the filed FY2026 statements,
  Item 1 and the FY2010 10-K; the brief's two general-knowledge beliefs were verified against the filings before use.
- [x] Every UNRESEARCHED verdict names the artifact: **none issued.** The unmeasured competitors are private or
  non-segmented, named at Q2; no document exists to fetch for them.
- [x] Every UNKNOWABLE verdict states what cannot be known: **none issued.** [E4-04]'s perimeter close was considered and
  refused in writing at Q2.
- [x] **Step 0: the filing was read, accession numbers recorded; FY2026 net cash provided by operations of $612M rebuilt
  from its own lines.** A second cross-check: FY2025 net tangible operating assets recomputed from the filed balance sheet
  ties to the companyfacts figure (1,438 both ways).
- [x] **Owner earnings on multi-year means, five windows up to sixteen years, both (c) ends, the judged end disclosed, the
  Glad buyout shown both ways; SBC from the cash-flow line in every year; no net-income proxy.**
- [x] **Competitor row filled**: five company-level peers reused from the CL run's row (cited as that run's evidence, the
  Clorox cells re-derived here), plus Reynolds (Hefty) from its 10-Ks and Reckitt (Lysol) from its annual reports and H1
  2026 announcement, both transcribed by sub-agents of this run with every cell sourced; figures read against the sub-agents'
  files, and two quotes (Reckitt's 700bps and H1 2026 share sentences) spot-checked in the extracted text before use.
- [x] **Sovereign for the earnings currency (USD), from the issuing authority, dated**: 5.47%, US Treasury daily par yield
  curve, 30 Yr, 09/24/2026, raw file saved; FRED not used.
- [x] Value stated as a round-number range, inside the COMPUTATION only.
- [x] One bar: none chosen, because Q5 did not open; windage count stated (ONE).
- [x] **Prices dated; aggregator used for the live quote only and flagged** ($81.80, close 2026-09-24, Yahoo chart endpoint,
  raw responses saved).
- [x] Every ledger id cited checked against `principle_ledger.csv` (all present; the quotations used were read against
  the rows); `tools/check_framework.py` run before the fold commit.
- [x] Run committed to git with pathspecs: `063170b` (claim), `d8f8489` (Step 0, Q1), `ad3e896` (Q2), `7dbba04`
  (beneath the close), then the fold commit (the queue file staged from the HEAD blob plus the register entry only).

**ERRORS, ARTIFACTS AND REPORTED-NOT-PATCHED, recorded rather than smoothed.**
1. **The brief's error.** The brief said the screen's `newest_filing` of 2025-06-30 meant the screen was built before the
   FY2026 10-K. The 10-K was filed 2026-08-07, before the screen's date; the cause is that **SEC companyfacts had still not
   ingested the FY2026 10-K on 2026-09-25**, seven weeks after filing (Step 0). The brief also said the CL run recorded Clorox's
   volume as *"-10 then -7"*; those are FY2023 and FY2026, not consecutive years, with -5 and +7 between them (the CL run's own
   row reads +6 / -5 / -10 / -5 / +7 / -7, which this run re-read from the bridge tables and confirms). And the brief's
   perimeter prior named only disposals; **the largest perimeter event is an acquisition, GOJO ($2,147M, April 2026), plus a
   $476M buyout run through operating cash**, neither of which the brief mentioned. The brief's other priors (the disposals,
   the cyberattack, the ERP disruption, the stale cap) were each right on the filings.
2. **REPORTED, NOT PATCHED: `tools/run.py` cannot see a 10-K that companyfacts has not ingested, and does not say so.** On
   CLX it priced FY2023-FY2025 as "the mean of 3 years" with no warning that a newer 10-K sat in EDGAR submissions. A check
   that compares the newest 10-K in `submissions` with the newest 10-K accession in companyfacts would name the gap. Not
   patched by this run, as the brief instructed for the sibling run.py defect of the same night.
3. **REPORTED, NOT PATCHED: the cap guard in `Screens/regen_queue.py` compares a cap and a float struck at different dates.**
   *"A cap cannot be smaller than a subset of itself"* is true only on one date; for a stock that fell 37% between the float
   date (2024-12-31, $162.41) and the cap's price, it fires on two correct numbers. Dating both, or restating the float at the
   cap's price date, would separate a stale input from a wrong one.
4. **My own error, caught before the Q2 commit:** the first Step 0 draft said the two disposed businesses were *"loss-making
   or low-margin"*; no filed figure read supported that for Argentina. Replaced by the filed VMS impairments. A second, in the
   Q2 draft: the row sentence said Clorox's operating margin was lowest in the row in four of five years; it is three
   (FY2022-FY2024). And the Q4 draft's capex and D&A sums and the FY2011-15 owner-earnings mean were first typed from memory of
   the table and were wrong ($3,362M, $3,205M, $522M); recomputed as $3,382M, $3,105M, $538M before commit.
5. **Text artifacts.** The stripped text of the FY2014-FY2016 10-K exhibits renders the registered-trademark sign as the
   replacement character (U+FFFD); the quotations restore the filed *"®"*, which is the filing's character and this run's
   extraction artifact. The Reckitt sub-agent flagged out-of-column numbers in two annual-report summary boxes and re-extracted
   the H1 2026 tables with a second library; see `peers_reckitt/RECKITT_ROW.md`. The REYN sub-agent flagged a garbled dash
   (nil) in three 10-Ks and a $4M unreconciled capex gap in FY2019.
6. **Repository weight, disclosed:** the Reckitt annual reports' extracted text (about 13 MB of `.txt`) was committed with the
   Q2 commit, because the verbatim Reckitt quotes rest on it; the PDFs themselves are ignored by `.gitignore`. Recorded, not
   rebased.
7. **The price is the lowest close in the two-year series** and has fallen every week since 2026-08-28 with no 8-K filed;
   nothing in this file depends on the reason, and none is offered.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- **One line: Q1 IN / Q2 OUT, on the business.** A maker of branded household staples that earns a high return on its small
  tangible capital, as every branded staple does, but whose price rises cost it units in its own words (bleach FY2015, Glad
  FY2014 and FY2019, the company FY2023 *"primarily due to pricing actions"*), whose units are below FY2019 after about 28
  points of price, whose EBIT is lower in nominal dollars than in FY2019, and whose direct disinfecting competitor reports
  share gains since 2019. At $81.80 (cap $9,892M) against a 5.47% sovereign the owner-earnings yield is about 6.3% to 7.8%,
  recorded as arithmetic only.
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.
