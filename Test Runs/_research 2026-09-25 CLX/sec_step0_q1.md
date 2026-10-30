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

