
## UPDATE 2026-09-25 - NATH: Q2 OUT. A trademark rent, not a franchise, and the licensee is buying it: the $94.29 quote is a merger spread on Smithfield's $102.00 cash offer.

**Nathan's Famous, Inc. (NATH), wave 7 name 36, register entry 168.** Run file `Test Runs/2026-09-25 Run - NATH
Nathans Famous.md`. Price $94.29 (close 2026-09-24, aggregator, flagged) x 4,097,661 shares (10-Q cover for 2026-06-28,
`0001437749-26-026427`) = cap $386.4M; sovereign 5.47% (US Treasury, 30 Yr, 09/24/2026). **Q1 IN, Q2 OUT on the
business.** This file's older screen note (the payout-coverage exclusion of WGO/NATH/MOV, 2026-08-31) is left as
written; the run answers the business question it did not ask.

### The first thing the run found: a live cash merger the screen could not see
- **Smithfield Foods, Nathan's exclusive retail licensee since March 2014, signed on 2026-01-20 to buy Nathan's for
  $102.00 a share in cash** (8-K `0001104659-26-005233`, EX-2.1; DEFM14A `0001104659-26-110393`). HSR expired
  2026-02-23; **CFIUS cleared 2026-09-17, a fact first made public in the DEFM14A accepted at 16:05 EDT on 2026-09-24,
  after the close the run priced**; special meeting 2026-10-23; about 29.9% under a voting agreement. The offer was cut
  from $103.50 after diligence found *"an approximate $20 million gap"*. **The quote is 92.4% of the consideration: an
  arbitrage [E2-74], not an owner-earnings price.**

### The finding
- **84.4% of segment profit is one royalty**: 10.8% of Smithfield's net sales of Nathan's packaged hot dogs, with
  minimum guaranteed royalties, to March 2032. The foodservice leg (65% of revenue) resells hot dogs at a 6.1-14.2%
  gross margin on prices *"correlated to our cost of beef and beef trimmings"*; the restaurant system is shrinking.
- **[E3-03] criterion (2) fails on the registrant's own words and its own physical series [E4-55].** Every MD&A gives
  retail volume and price separately: FY2017 price -4.0% *"due to competitor pricing pressures"*; FY2023 -4% units on
  +7% price; FY2024 -3% on +3%; **FY2026 -13% on +15%**, *"The price increases year over year led to a reduction in
  promotional activities contributing to the decline in volume."* **FY2022-FY2026: units -10%, price +27%, royalty
  dollars +16%.** The licensee sets price, promotion and shelf and sells Eckrich, Armour and Farmer John beside it.
- **Competitor row**: Smithfield Packaged Meats 12.5-14.0% and Tyson Prepared Foods 8.4-9.0% operating margin, against
  4.1-7.8% for Nathan's own product-selling leg; Oscar Mayer impaired $1.3bn by Kraft Heinz in Q4 2024; no filer
  segments a hot-dog brand.
- **The strongest counter-case, stated and answered**: the 2014 re-licensing tripled the royalty rate (3-5% to 10.8%),
  the licensee is paying $102.00, ten-year units are +34%. One negotiation in twelve years, and a price paid by the one
  buyer that stops paying the royalty, are not pricing power over consumers.

### Priors refuted or confirmed
- **`deal_note` blank: refuted as a description of the security** (a signed cash merger since January).
- **The brief's prior of an SEC settled action around 2019 over undisclosed perquisites: no instance found** in any
  10-K FY2010-FY2026 or in EDGAR full-text search on the CIK for 2017-2026. The one SEC order in the record is
  **director Robert J. Eide's 2018 cease-and-desist as CEO of Aegis Capital** (Section 17(a), Rule 17a-8), disclosed in
  Nathan's proxies. SEC orders never disclosed in EDGAR were not searched.
- **SBC resolves 17 of 17 years and is complete.** **[E4-29] fires in the 10-K itself** (EBITDA and Adjusted EBITDA
  reconciled in the MD&A; Adjusted EBITDA adds back SBC).
- **The screen's width, rebuilt over seventeen years**: 3y $19.2-19.9M, 5y $18.3-18.9M, 10y $14.8-15.4M, 17y
  $11.4-12.1M. **About $4M of the move to the recent level is interest saved** as the recapitalisation notes were
  repaid (the 2015 notes paid the $116.1M special dividend; the 2017 refinancing sat beside a $20.9M one paid mostly
  from cash), not business growth. The (c) band is about $0.6M wide; the
  window choice moves the level by $8M.
- Named death as a signature only: **#19 THE SHELF**, with #6 THE BORROWED BALANCE SHEET as a feature. Not entered in the
  index's instances column (closed at Q2); no new shape.

### Tooling defects (reported, not patched)
- **`tools/sources.py` `deal_filings()` counts deal forms only after the newest 10-K.** A merger announced before the
  annual report (here the 8-K of 2026-01-21 and the PREM14A of 2026-03-06, both before the 10-K of 2026-06-09) is
  invisible until the definitive proxy; the screen of 2026-09-02 showed a blank `deal_note` for a company seven months
  under a signed cash merger. Today the call fires on the DEFM14A. A pending-deal check needs to look back past the
  annual report.
- `run.py`'s "GROWTH THE PRICE ASSUMES" printed -9.1% where the screen's `growth_required` reads +5.46%:
  `implied_growth()` fades to a fixed 2.5% terminal rate, so a price below about 34 times owner earnings at 5.47%
  returns negative "required" growth. Two definitions, opposite signs.
- `annual()` returns Hormel's operating income only through FY2017 (a tag change, not investigated).
