# Company Run — The Procter & Gamble Company (PG) — 2026-09-25
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

**Registrant, by CIK first.** SEC `submissions` for **CIK 0000080424**: PROCTER & GAMBLE Co, Ohio, fiscal year to **June 30**,
no former names, large accelerated filer (`_research 2026-09-25 PG/submissions.json`, fetched 2026-09-25).

**Sovereign, for the currency the business EARNS in**: the currently observed rate, never a forecast **[E4-15, E3-32]**:
- rate **5.47%** · date **09/24/2026** · source (issuing authority) **US Treasury daily par yield curve, 30 Yr**, struck fresh
  today; raw CSV saved as `_research 2026-09-25 PG/treasury_2026.csv` (row `09/24/2026 ... 5.53,5.47`, 20 Yr then 30 Yr).
  `python tools/sources.py` agrees (USD 5.47%, 09/24/2026). **FRED not used.** No rate inherited from any earlier run.
- **Why USD.** P&G reports in US dollars, is quoted in US dollars, and pays its dividend in US dollars. The 10-K says *"our
  operations outside the U.S. generate more than 50% of our annual net sales"*, so the earnings are multi-currency at the
  source; they reach the owner translated into the reporting currency, and the currency translation risk is carried at Q4
  (Argentina, Russia, the FX lines in the sales bridge), not by switching the yardstick. The same basis the CL run used.
- FX if the quote and the earnings differ in currency: not applicable (USD quote, USD reporting). ADR ratio: none.

**The price, re-struck (aggregator, live quote only, flagged).** **$145.68, NYSE close 2026-09-24**, Yahoo Finance chart
endpoint (`price_raw.json`, fetched 2026-09-25 16:49 UTC; the 09-25 intraday print was $145.78, and `tools/run.py`
priced $145.87 intraday a few minutes later). The screen row's cap of $333,440M is stale and is not used.

**The share count, from the cover of the LATEST periodic filing, and the charter read before anything is summed.**
- The latest periodic filing is the **10-K for the year ended 2026-06-30, filed 2026-08-04, accession
  `0000080424-26-000103`** (no 10-Q has been filed since; the September-quarter 10-Q is due in October). Cover, verbatim:
  *"There were 2,324,433,060 shares of Common Stock outstanding as of July 31, 2026."* `python Screens/cover_shares.py PG`
  returns the same 2,324,433,060, single class, from the same accession.
- **The preferred, read in the charter lines and Note 8, not assumed.** The balance sheet carries *"Convertible Class A
  preferred stock, stated value $1 per share (600 shares authorized)"* at $756M and *"Non-Voting Class B preferred stock"* at
  nil. The Class A preferred is held by the ESOP in two series. Note 8: Series A, *"Each share is convertible at the option of
  the holder into one share of the Company's common stock. The dividend for the current year was equal to the common stock
  dividend of $4.26 per share"*; *"The number of Series A preferred shares outstanding of 18 million"*; Series B, the same
  one-for-one conversion and the same dividend, **48,642 thousand** shares (36,365 allocated, 12,277 unallocated); and
  *"For purposes of calculating diluted net earnings per common share, the preferred shares held by the ESOP are considered
  converted from inception."* Note 6 adds **68.3M** convertible preferred shares to the FY2026 diluted weighted average.
- **So the preferred is common in all but name**: it converts one-for-one, it draws the common dividend ($292M in FY2026),
  and it is a claim on the same owner earnings. **It is counted.** Economic share count = 2,324.43M common + 18M Series A +
  48.64M Series B = **about 2,391.1M**. (The Series A figure is filed rounded to the million; the rounding is at most 0.5M
  shares, about $0.07bn, and is disclosed rather than refined.)

**Market cap.** Common only: 2,324,433,060 × $145.68 = **$338.6bn**. **As-converted, the basis used from here on:**
2,391.1M × $145.68 = **$348.3bn**. *(The ESOP's unallocated Series B shares fund retiree health care; counting every
preferred share outstanding on the capitalization side is also what keeps that stock-settled benefit funding from being
missed at Q4, see the SBC paragraph there.)*

**The deal forms, read before pricing.** The screen's `deal_note` is empty. Every P&G filing since 2006 was listed from the
three submissions files and scanned for Items 1.01, 2.01, 1.02, 2.05, 2.06, 4.02 and 3.01 and for forms S-4, 425 and
SC TO-I. **Found:** the 2008 Folgers split-off (SC TO-I, 425s), the 2011 Pringles 425s, the 2015 Galleria/Coty Item 1.01,
the 2016 Coty beauty split-off exchange offer (SC TO-I 2016-09-01 and 425s), and the 2023-12-05 Item 2.06 (the
Argentina/Nigeria restructuring impairment). **All are closed.** **Not in any 8-K item, found only by reading the 10-K:**
*"On August 4, 2026, the Company entered into an agreement to acquire Thorne, a premium wellness and supplement brand in the
vitamins, minerals and supplements category for $3.8 billion. We anticipate the transaction to close in the second quarter
of fiscal year 2027"* (MD&A, Recent Developments). **P&G is the buyer, so the quote is not a spread**; $3.8bn is about 1.1%
of the as-converted cap. The empty `deal_note` is therefore **half right**: no live deal makes the quote a spread, and a live
$3.8bn acquisition exists that no 8-K item carries (below the significance test, so Item 2.01 will not be required at close;
the same limit the 2026-09-12 resume state recorded for SWK). Also read: the Glad joint venture with Clorox expired in
January 2026, *"Clorox purchased the Company's minority interest in the venture at fair market value for $476 million"*,
after-tax gain $261M, excluded from Core EPS.

**The filing was read**: not tagged data **[E3-27]**:
- [x] MD&A (whole: overview, segment table and share statements, recent developments, results, all five segments, Corporate,
  restructuring, cash flow, liquidity, contractual commitments, critical estimates including the Gillette sensitivity, and
  the non-GAAP reconciliations) [x] cash-flow statement incl. detail lines [x] footnotes (Notes 1-8, 10, 13, 14 read; 9, 11, 12
  scanned) · also Items 1, 1A (whole), 1C, 2, 3, 5, and the executive-officer list.
- document · date · accession no.: **Form 10-K for the fiscal year ended June 30, 2026, filed 2026-08-04,
  `0000080424-26-000103`** (`_research 2026-09-25 PG/tenk_FY2026.txt`, fetched fresh from EDGAR, not the CL run's copy).
  Earlier statements read for the long window: 10-K FY2023 `0000080424-23-000073`, FY2020 `0000080424-20-000053`, FY2017
  `0000080424-17-000047`, FY2014 `0000080424-14-000057`, and the FY2011 10-K `0000080424-11-000014` with its Exhibit 13
  (the statements were incorporated by reference that year, so the exhibit was fetched); FY2019 `0000080424-19-000050` for
  the sales bridge.
- figure cross-checked against the filed statement: **FY2026 net cash from operating activities $19,556M** in the filed
  statement (*"TOTAL OPERATING ACTIVITIES | 19,556 | 17,817 | 19,846"*) = companyfacts
  `NetCashProvidedByUsedInOperatingActivities` 19,556,000,000 under the same accession = MD&A cash-flow table. Also SBC
  $524M, capex $4,409M and D&A $3,160M tie between the statement and the tag.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words, no management language.** P&G makes things people use up every day and buy again within
  weeks: laundry detergent, dish soap, disposable nappies, toilet paper and kitchen towels, razor blades, toothpaste,
  shampoo, deodorant, cold remedies. It buys commodity inputs (pulp, resins, surfactants), runs 96 plants (24 in the US, 72 in
  31 other countries, Item 2), and sells to retailers who resell to households; Walmart is about 16% of sales and the top ten
  customers about 43%. Of each FY2026 sales dollar, about 50 cents goes on making the product (cost of products sold $43.4bn
  on $87.0bn, gross margin 50.2%), about 27.5 cents on selling, advertising and overhead, and about 22.7 cents is operating
  profit ($19.7bn). The business needs little capital for its size: capex ran $4.4bn (5.1% of sales), and it runs on
  suppliers' money, **current liabilities exceeding current assets by $12.5bn**, with payables of $16.3bn on supplier terms
  of 60 to 180 days under a supply-chain-finance programme (Note 14). The money is made because a household that uses Tide,
  Pampers or Gillette tends to buy the same one again, and a retailer has to stock the brands its shoppers ask for, so P&G can
  charge more than its cost plus a normal return on the plants.
- **The scarce input this business controls.** The repeat purchase habit attached to a small set of trademarks in categories
  where the product's performance is noticed by the user (the 10-K's own framing is *"daily-use products where performance
  drives brand choice"*), plus the position that habit buys on retail shelves. The filing's stated positions: *"more than 50%
  share"* of grooming and *"more than 60%"* of blades and razors; *"over 35% market share"* in fabric care in its markets;
  *"more than 30%"* of baby care; *"nearly 30%"* of feminine care and of oral care; *"about 20%"* of hair care; Bounty *"nearly
  40%"* of North America paper towels. **Not scarce**: the plants, the chemistry of most categories, and the retail shelf
  itself, which the retailer owns and rents to private label too (Item 1: *"we compete against other branded products as well
  as retailers' private-label brands"*).
- **Will the fundamentals look broadly the same in ten years?** The FY2017 10-K describes *"ten product categories ...
  aggregated into five reportable segments: Beauty; Grooming; Health Care; Fabric & Home Care; and Baby, Feminine & Family
  Care"*, the same five segments the FY2026 10-K reports, with the same brands leading them. Detergent, nappies, razors and
  toothpaste have no technology generation that turns over; the risks the filing names (channel shift to online and hard
  discounters, retailer media platforms, *"AI based search"*, private label, currency) change how the products are sold and
  at what margin, not what they are or why they are bought. **I expect the fundamentals to look broadly the same.** What is
  genuinely uncertain is margin and share, which are Q2 questions, not comprehension ones.
- **[E4-46] test: could a decision on the business model be made in five minutes?** Yes. Nothing here needs months of study;
  the complexity is size (five segments, about 180 countries), not mechanism. The Thorne acquisition ($3.8bn, supplements)
  adds a category but not a kind of business.
- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *IN: a relatively simple and stable business in the sense of [E3-31], read from the FY2026 10-K and checked against FY2017.
  Understanding how it makes money says nothing yet about whether it is a franchise; that is Q2.*
## Q2 — IS IT A FRANCHISE? **[E3-03]**

- **Needed or desired [x]** · **no close substitute [x] in Grooming, Fabric & Home Care, Baby and Feminine Care, Oral Care and
  Personal Health Care (by the pricing record below); [ ] not shown for Family Care (paper towels, toilet paper, tissues, 8% of
  FY2026 sales)** · **not price-regulated [x]** (no category the 10-K describes is price-regulated in the US; the price
  controls named in Item 1A are foreign exchange and import controls in specific countries, a Q4 risk).
- **Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04]** **Defended, not rebuilt.** The
  spending is advertising ($10.2bn in FY2026, $9.2bn FY2025, $9.6bn FY2024, Note 1; about 11-12% of sales) and research and
  development ($2.1bn), and it defends the same trademarks the FY2017 10-K listed (Tide, Ariel, Downy, Pampers, Always, Gillette,
  Crest, Oral-B, Head & Shoulders, Pantene, Olay, Bounty, Charmin). A lapse in advertising would narrow the position; it would not
  have to be bought again from zero. That is the distinction the framework's scope paragraph draws, and **[E5-23]** prescribes the
  defence for every moat. No **[E3-51]** wave is under it: nappies and detergent have no technology generation. Manager
  dependence is tested below against the 2013-2018 record, not assumed.

### THE PRIMARY MOAT METRICS, filing-sourced, and their trend

**(a) Share, as the company itself reports it every year.** Each 10-K MD&A states, for each segment, *"Global market share of
the ... segment increased/decreased X points"* (dollar share, constant currency, per the 10-K's definition: *"All market share
references represent the percentage of sales of our products in dollar terms on a constant currency basis relative to all product
sales in the category"*). Each cell below is from that fiscal year's own 10-K (the FY2013 and FY2015 cells from the prior-year
columns of the FY2014 and FY2016 10-Ks); extraction in `_research 2026-09-25 PG/shares2.py`, output `shares_out.txt`.

| FY | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | sum 13-18 | sum 19-24 | sum 25-26 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Beauty (19% of sales) | -0.5 | -0.4 | -0.6 | -1.0 | -0.6 | -0.2 | -0.1 | +0.2 | -0.4 | +0.1 | +0.3 | +0.1 | -0.3 | -0.3 | **-3.3** | +0.2 | -0.6 |
| Grooming (8%) | +0.4 | +0.2 | -0.1 | -1.1 | -0.7 | -0.8 | -0.9 | -0.2 | -0.6 | +1.2 | +1.0 | +0.5 | -0.1 | -0.4 | **-2.1** | +1.0 | -0.5 |
| Health Care (14%) | -0.2 | +0.2 | -0.3 | -0.7 | -0.2 | -0.1 | +0.5 | +0.4 | +1.8 | -0.2 | -0.2 | +0.6 | +0.2 | +0.4 | -1.3 | **+2.9** | +0.6 |
| Fabric & Home Care (35%) | -0.3 | +0.2 | -0.1 | -0.2 | -0.1 | +0.1 | +0.5 | +0.7 | +1.0 | +1.5 | 0 | 0 | +0.1 | 0 | -0.4 | **+3.7** | +0.1 |
| Baby, Fem & Family (24%) | -0.2 | -0.3 | -0.6 | -1.1 | -0.1 | -0.7 | +0.1 | -0.3 | -0.2 | +0.8 | 0 | -0.2 | -0.2 | -0.2 | **-3.0** | +0.2 | -0.4 |

*Limits, stated: a segment's "global share" is a sales-weighted blend of category shares the company does not publish; the
company says the data exclude channels it cannot buy data for; and the level statements in Item 1 changed basis between filings
(FY2017: fabric care *"over 25% global market share"*; FY2026: *"over 35% market share in the markets in which we compete"*), so
**levels are not compared across years, only the filed year-on-year changes.***

**Trend, without decoration.** **Six years of share loss in every segment (FY2013-2018), six years of recovery (FY2019-2024),
and two years of renewed slippage in three of five segments (FY2025-2026).** Across the full fourteen years the sums are Beauty
-3.7, Grooming -1.6, Health Care +2.2, Fabric & Home Care +3.4, Baby/Feminine/Family -3.2; weighted by FY2026 sales about -0.1
point in aggregate. **[E4-32]**'s *"widened every year"* is **not met** across the span: it is met in FY2019-2024 only.

**(b) The physical series [E4-55]**, *"Volume Excluding Acquisitions & Divestitures"*, TOTAL COMPANY row of each year's
*"Net Sales Change Drivers"* table (10-Ks FY2014, FY2016, FY2017, FY2018, FY2019, FY2020 fetched for this run; FY2021-FY2025 read
from the primary-document copies the CL run saved, accessions in its `peers/SECTION_PG.md` and re-read line by line here;
FY2026 from `0000080424-26-000103`; extraction `drivers.py`):

| FY | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| organic volume % | +2 | +3 | -1 | -1 | +2 | +2 | +2 | +4 | +3 | +2 | **-3** | 0 | +1 | 0 |
| price % | +1 | +1 | +2 | +1 | 0 | -1 | +2 | +1 | +1 | +4 | **+9** | +4 | +1 | +1 |
| foreign exchange % | -2 | -2 | -6 | -6 | -2 | +2 | -4 | -2 | +1 | -2 | -5 | -2 | -1 | +2 |

**Ten years FY2017-2026: volume +13 points, price +22, mix +7 (filed mix column), FX -13.** **Last five years FY2022-2026:
volume 0, price +19.** So over the decade units did grow, about 1.3% a year, and far more than Colgate's +7.7 in the CL run's
table; but **for the last five years every dollar of organic growth was price, and FY2026 units were flat with volume declines in
North America attributed to *"competitive activity"* in hair care, oral care, home care, baby care and family care.** The phrase
*"competitive activity"* appears **9 times** in the FY2026 10-K against 3, 4, 0, 2 and 3 in FY2021-FY2025 (counted, same method).

**(c) The pricing test, [E2-44] criterion (1) and [E4-37].** The hardest test the period offered: FY2022-FY2024, **+4, +9 and +4
points of price, seventeen in three years**, with volume +2, -3, 0. Over the same three years the filed segment shares were
Beauty +0.5, Grooming **+2.7**, Health Care +0.2, Fabric & Home Care **+1.5**, Baby/Feminine/Family +0.6. **Net share rose in every
segment across the three years (not in every year) while price rose seventeen points.** That is *"the ability to regularly price its product or service aggressively"*
passing in the conditions most likely to break it. The inverse metric **[E4-37]** is firing in one place, and it is named:
*"Net sales in Family Care ... decreased low single digits driven by lower pricing (due to merchandising investments) and a unit
volume decrease (due to competitive activity)"*, North America family care share -0.7 (FY2026 10-K). **The attacker's test
[E2-45] was actually run, on Grooming, and the filing records it:** share fell -1.1, -0.7, -0.8, -0.9 in FY2016-2019; FY2018:
*"Price reductions in Shave Care reduced net sales by 3%"*; FY2019: the $8.3bn Shave Care impairment, *"Given recent reductions in
cash flows caused by currency devaluations, changing consumer grooming habits affecting demand and an increase in the competitive
market environment"*. Then Grooming share came back +1.2, +1.0, +0.5 (FY2022-24), and the FY2026 10-K states *"more than 60%"*
of blades and razors. **The attack narrowed the moat and cost the price premium some points; it did not cross it.** (The
filings do not name the attackers, and this file does not supply names from memory.)

### THE SECOND QUESTION ABOUT THE BUSINESS IS A NUMBER: [E3-46], [E2-43]
Pre-tax GAAP operating return on average net tangible operating assets (NTOA), the **identical definition** the CL run applied
(its `peers/peer_metrics.py`, copied unchanged into `_research 2026-09-25 PG/peers/` and re-run on companyfacts fetched
2026-09-25; output `peers/row_out.txt`): **FY2016 40.5%, 45.6, 46.0, 20.0 (50.4 before the $8,345M Shave Care impairment), 69.7,
91.7, 85.2, 83.0, 81.5 (87.4 before the $1,341M Gillette impairment), 84.6, 77.8% (FY2026)**. Operating margin over the same
years 20.6% to 22.7%, 24.3% the high (FY2025). **A caution the file owes the reader about the rise from ~45% to ~85%**: part of
it is the denominator. Accounts payable went from **$9,325M (FY2016) to $16,306M (FY2026)**, 14.3% to 18.7% of sales, on payment
terms of *"60 to 180 days"* with $6.2bn confirmed under the supply-chain-finance programme (Note 14). Supplier credit is a real
and legitimate funding source, and it is also a source that can be stretched only once. The ~45% of FY2016-2018, before the stretch,
is the cleaner read of the business's own economics, and it is still very high. **[E2-44] criterion (2)** (*"with only minor
additional investment of capital"*) is met: $87.0bn of sales on about $25.9bn of NTOA, capex about 5% of sales.

### THE COMPETITOR ROW: required [E3-28]
*"I can't be an intelligent owner of a business unless I know what all the other businesses in that industry are doing."* Same
metric, same construction, each company's own fiscal years; means are simple means of the annual figures.

| company | where it meets PG | GAAP operating margin, 5 most recent FYs (mean) | long window mean (years) | pre-tax return on avg NTOA, 5y mean | long window mean | source |
|---|---|---|---|---|---|---|
| **Procter & Gamble** | all | FY22-26: 22.2 / 22.1 / 22.1 / 24.3 / 22.7 (**22.7**) | **20.8** (FY17-26; 22.2 ex-impairments) | **82.4** (83.6 ex-imp.) | **68.5** (FY17-26; 72.1 ex-imp.) | companyfacts; FY2026 op income 19,748 and sales 87,032 tie to the filed statement |
| Colgate-Palmolive | oral, personal, home | 2021-25: 19.1 / 16.1 / 20.5 / 21.2 / 16.2 (**18.6**) | 21.3 (2016-25) | 80.3 | **87.4** | companyfacts; 2025 op profit $3,306M ties to CL 10-K FY2025 (*"Operating profit, GAAP \| $ \| 3,306"*) |
| Kimberly-Clark | baby, adult, family care | 2021-25: 13.2 / 13.3 / 11.2 / 16.1 / 14.3 (**13.6**) | 15.0 (2016-25) | 31.3 | 35.4 | companyfacts; 2025 *"Operating Profit \| 2,351"* ties to KMB 10-K FY2025 |
| Church & Dwight | laundry, oral, personal | 2021-25: 20.8 / 11.1 / 18.0 / 13.2 / 17.4 (**16.1**) | 18.0 (2016-25) | **90.5** | **87.3** | companyfacts |
| Kenvue | personal health, skin | 2023-25: 16.3 / 11.9 / 16.0 (**14.7**, 3 yrs) | same | 77.2 | same | companyfacts |
| Edgewell | razors (Schick), fem care, sun | FY21-25: 11.5 / 8.4 / 10.1 / 8.8 / 4.3 (**8.6**) | 9.1 (FY19-25) | 31.6 | 33.4 | companyfacts (op income untagged before FY2019) |
| Estée Lauder | skin care | FY22-26: 17.9 / 9.5 / 6.2 / -5.5 / 5.2 (**6.7**) | 9.9 (FY17-26) | 29.7 | 48.0 | companyfacts |
| Coty | beauty (P&G's former brands) | FY22-26: 4.5 / 9.8 / 8.9 / 4.1 / -1.4 (**5.2**) | -6.8 (FY17-26) | 18.5 | -7.4 | companyfacts |
| Clorox | home care (Glad JV partner) | FY21-26 EBIT: 13.6 / 10.0 / 4.4 / 6.9 / 16.4 / 13.7 | n/a | 72.9 / 44.1 / 20.4 / 29.7 / 72.2 / 51.9 | n/a | **carried from the CLX run's `ntoa.py` (EBIT = pretax + interest, a different numerator), not re-derived; noted as not the same metric** |
| Unilever (20-F, IFRS, EUR) | laundry, hair, personal, skin | 2025: operating profit *"€9.0 billion"* on turnover *"€50.5 billion"* = **17.8%** | not computed | not computed (IFRS) | n/a | re-read from the 20-F FY2025 on disk in the CL run's folder |
| Haleon (20-F, IFRS, GBP) | oral care, OTC | 2025: *"Operating profit 2,412"* on *"Revenue 11,030"* = **21.9%** | not computed | not computed | n/a | re-read from the 20-F FY2025 on disk |
| **Henkel Consumer Brands** (not SEC; IR site, rung 3) | laundry (Persil, all), hair | 2021-25 reported EBIT margin: 874/10,283 = 8.5, 4.2, 7.1, 12.2, 13.6 (**9.1**) | 2019-25: 9.7 | not computed | Henkel's own ROCE 11.7% (2025), not the same metric | Henkel Annual Report 2025, multi-year summary p.481 and segment table (`peers/henkel_AR2025.pdf`, fetched 2026-09-25) |
| **Essity** (not SEC; IR site) | baby, fem, incontinence, tissue | 2021-25 reported operating margin: 10.8 / 6.5 / 10.3 / 12.6 / 13.4 (**10.7**) | 10.8 (2016-25) | not computed | n/a | Essity Annual Report 2025, ten-year summary (`peers/essity_AR2025.pdf`) *"Operating margin, %3) 13.4 12.6 10.3 6.5 10.8 13.8 11.1 9.1 10.9 8.9"* |
| **L'Oréal** (not SEC) | hair, skin | 2025: *"operating profit"* 20.2% of sales, **L'Oréal's own measure, before other income and expenses** | n/a | n/a | n/a | L'Oréal 2025 annual results release (`peers/loreal_2025_results.html`) |

- **Peers named: fourteen, of roughly eighteen real competitors.** Every one of PG's five segments has at least two rowed rivals:
  Fabric & Home Care (Unilever, Henkel, Church & Dwight, Clorox, Colgate); Baby, Feminine & Family (Kimberly-Clark, Essity,
  Edgewell); Grooming (Edgewell); Health Care (Colgate, Haleon, Kenvue); Beauty (Unilever, L'Oréal, Estée Lauder, Coty, Colgate).
  **Not rowed, and named:** Reckitt (air care, dish, OTC; the CLX run holds its annual reports, but its segment line is adjusted
  operating profit only, so no same-metric figure exists), Unicharm and Kao (Asian baby and feminine care), Beiersdorf, and the
  private-label manufacturers behind the 10-K's *"retailers' private-label brands"*. **Grooming has only one rowed rival**, because
  the razor attackers of 2012-2019 are private.
- **What the row shows.** On GAAP operating margin **PG is the highest in the row over the five most recent years (22.7% mean)**,
  above Haleon (21.9% in 2025), L'Oréal's own 20.2%, Colgate 18.6%, Unilever 17.8%, Church & Dwight 16.1%, Kenvue 14.7%,
  Kimberly-Clark 13.6%, Essity 10.7% and Henkel Consumer 9.1%, and far above the beauty specialists that bought or compete with
  its former brands (Coty 5.2%, Estée Lauder 6.7%). **In the same diaper and tissue categories PG earns about 2.5 times
  Kimberly-Clark's return on the same tangible-asset definition (82% against 31%)** and about twice Essity's margin. **On the long
  window PG is NOT top on return on capital**: FY2017-2026, 68.5% against Colgate 87.4% and Church & Dwight 87.3%; the gap is the
  FY2016-2019 years (40-50%), before the payables stretch and while share was falling. **The row places PG at or near the top of
  its industry on margin and return, not alone at it.**
- **The row's limit [E3-61]**, stated: *"In some businesses, the participants behave like a demented Kellogg. In other businesses,
  they don't ... I think you'd have to know the people involved."* The row shows position; it cannot show whether a rival (or a
  retailer's private label) will buy share with price, which is exactly what the FY2026 "competitive activity" sentences may be
  recording.
- **Untapped pricing power [E3-33]: NOT CLAIMED.** **[E5-28]** scopes the class to *"a monopoly or a near monopoly"*. Grooming's
  *"more than 60%"* of blades and razors comes nearest, and the filed record there runs the other way: price was **cut** in FY2018
  under attack. No category shows a price the manager has declined to take.
- **The dominance class [E2-53] and mismanagement tolerance [E5-18], tested on the record rather than asserted.** FY2013-2018 is
  the test the decade ran: share lost in every segment for six years, a razor price war, and a later $8.3bn write-down, and
  **through it the business still earned 40-50% pre-tax on net tangible operating assets and about 20% operating margins**. *"If
  it won't stand a little mismanagement it's not much of a business"* **[E5-18]**; this one stood six poor years. Whether FY2025-26
  is the start of a second such period is a Q6 monitoring question, not a Q2 finding.
- **Class: [ ] WIDE [x] NARROW [ ] NONE [ ] PROVISIONAL** · **Direction [E4-32]: narrowed FY2013-2018, widened FY2019-2024,
  narrowing again FY2025-2026; over fourteen years roughly level.**

### THE FRANCHISE CASE AND THE CASE AGAINST, BOTH AT FULL STRENGTH [E4-26, E4-51]
*Operator rule 9: a famous, high-quality name is where the incentive to clear runs strongest, so the case against was written
first.*

**The case against:** *"P&G's units have not grown in five years; all of the growth since FY2021 was price. For six years to FY2018
it lost share in every segment, lost a price war in its most profitable category and wrote off $8.3bn of Gillette, and it is losing
share again now in Beauty, Grooming and Baby/Feminine/Family, with 'competitive activity' named nine times in its latest 10-K and
family care prices cut. Its celebrated returns on capital doubled mainly because it stretched its suppliers to 60-180 days and
$6.2bn of supply-chain finance. Walmart is 16% of sales and the top ten customers 43%, retailers own the shelf and sell private label
beside every P&G brand, and in a decade of long-window returns Colgate and Church & Dwight beat it."*

**The answer, clause by clause, on the filed record.** (1) The facts are granted; each is in the tables above. (2) None is a failure
of [E3-03]'s demonstration, *"the ability to regularly price its product or service aggressively and thereby to earn high rates of
return on capital"*: in FY2022-2024 P&G took seventeen points of price and **made net share gains in all five segments over the three years**, which is the test
passing at its hardest. (3) The return on capital was very high **before** the payables stretch (40-50% pre-tax on NTOA in FY2016-18,
through the worst share years), so the stretch flatters the level; it does not create it. (4) The 2013-2018 share loss and the razor
attack are the [E2-45] test run for real, and the moat narrowed and held; the corpus's word for the failure case is *crossed*, and
fourteen years of filings show no crosser. (5) Against its own industry on the same metric P&G has the highest margin in a fourteen-
company row and 2.5 times Kimberly-Clark's return in the categories they share. (6) What the case against does establish is recorded
and carried: the class is **NARROW, not WIDE**; **[E4-32]'s direction test fails across the span**; **[E3-33] is refused**; Family
Care's criterion (2) is not shown; and FY2025-2026 is a live downgrade signal for Q6.

- **Can I name the document that would resolve what is left open?** For the verdict, no document is missing: fourteen years of 10-Ks,
  and fourteen peers, ten from primary SEC filings and three from their own annual reports. Unicharm, Kao and Beiersdorf could be read
  from their annual reports; they would add rows in Asian baby care and in skin care, not change P&G's place above the rowed set.
- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *IN, NARROW. All three [E3-03] conditions hold for the business as a whole and for every segment but Family Care (8% of sales); the
  demonstration is met by the FY2022-24 pricing record with net share gains in all five segments, and by pre-tax returns on net tangible
  operating assets of 40-92% across ten years, the highest GAAP operating margin in a fourteen-company competitor row. [E4-04] is not
  engaged: the moat is defended, and the FY2013-2018 record shows it tolerating a poor period [E5-18]. NARROW, because [E4-32]'s
  direction fails over the span, share is slipping again in three segments, the physical series is flat for five years [E4-55], the
  long-window return trails Colgate and Church & Dwight, and [E3-33] is refused. The file continues to Q3.*
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1: DECLARE THE WEIGHT CASE.**
- [ ] **Daily execution**: not ticked. Q2 found a franchise (NARROW), and the 1991 original reads *"franchises can tolerate
  mis-management ... a business, unlike a franchise, can be killed by poor management"* **[E3-43]**; the FY2013-2018 record is the
  tolerance demonstrated (six years of share loss, returns still 40-50% pre-tax on NTOA). It is not a have-to-be-smart-every-day
  business in the [E3-38] sense, though the FY2026 "competitive activity" sentences are the reason this is a judgment and not a
  formality.
- [ ] **Control**: not ticked: a minority purchase of a listed share, exit available daily **[E1-16]**.
- [ ] **Leverage**: not ticked: total debt $34.1bn against FY2026 operating income of $19.7bn and interest expense of $877M
  (about 22 times covered); AA-/Aa3 (MD&A). Small asset errors do not destroy the equity **[E3-29]**.
**Case declared: all three low, so Q3 is a qualitative OVERLAY.** Findings are recorded; a mediocre manager alone would not stop the
run, and nothing here is used to promote it.

**Honesty: binary, permanent, filings-based [E5-16].** Each matter dated to when it became public.
- **2010-2011, European competition-law violations.** The FY2011 10-K, Item 3: *"The Company identified violations in certain
  European countries and appropriate actions were taken"*, after *"In response to the actions of the European Commission and
  national authorities, the Company launched its own internal investigations"*; final decisions that year from *"the Czech Republic,
  the European Commission, Italy, Spain and Switzerland"*; charges *"for competition law fines"* of **$283 million (FY2010) and $303
  million (FY2011)** (FY2011 Exhibit 13). **This is corporate price-fixing, and it is recorded, not waived.** It is fifteen years
  old, it was found and acted on by the company's own investigation (the conduct **[E5-22]** says is the test: the failure that
  counts is *"they didn't act when they learned"*), no officer named in the FY2026 10-K is identified with it in any document read,
  and no later 10-K (FY2014, FY2016, FY2017, FY2020, FY2026 read) reports a recurrence. Whether a corporate plea without named
  individuals meets the honesty test was the question the UMC run put to the operator; this file applies the same reading the runs
  have used since, **it does not disqualify today's management**, and says so rather than hiding the matter.
- **Current**: FY2026 Item 3 lists one matter, a UK Environment Agency penalty *"of less than $2 million"* for a permit P&G UK
  *"proactively notified"*. Note 13: no litigation expected to be material. Proxy: related-person transaction policy; hedging and
  pledging of company stock prohibited for NEOs.
- **No integrity disqualifier found in the documents read.** No enforcement-database sweep was run beyond the filings.

**STEP 2: THE FLAGS [E4-22, E5-15, E4-29, E4-30].** *Each a prompt to read, never a verdict.*
- [ ] **weak accounting**: not found. Stock options expensed ($264M) with the lattice inputs disclosed; pension return assumption
  6.0% with a stated sensitivity; the Gillette intangible's headroom and a sensitivity table published every year and impaired twice
  (FY2019 $8.3bn with goodwill, FY2024 $1.3bn) rather than carried at a stale value.
- [ ] **unintelligible footnotes**: not found; Notes 1-8, 10, 13, 14 read without difficulty; the ESOP note is old-fashioned but
  complete (share counts, conversion, dividend, liquidation value).
- [x] **trumpeted earnings projections / growth targets**: **fires.** Every 10-K since at least FY2022 states a *"long-term growth
  algorithm"* of *"Core EPS growth of mid-to-high single digits"*, and every July release gives a full-year range for sales, organic
  sales, GAAP EPS, core EPS, cash productivity and buybacks, re-affirmed each quarter. **The record of the people who made them
  [E3-48]:** FY2026 guided organic sales *"flat to up four percent"*, outturn **+1%**; core EPS *"flat to up four percent"*, outturn
  **+1%**; GAAP EPS first *"3% to 9%"*, lowered in January to *"one percent to six percent ... reflecting higher non-core
  restructuring charges"*, outturn **+2%**; the April release warned *"toward the lower-end of the guidance range"*. **Inside every
  range, at the bottom, with the one revision announced and explained.** Against the algorithm, core EPS grew 3%, 2%, 12%, 4%, 1%
  in FY2022-2026, about **4.0% a year compounded ($5.66 to $6.89)**, **below the "mid-to-high single digits" the company keeps
  printing.** [E4-35]'s base rate says the target was always unlikely; [E5-30] says a guidance culture is a ratchet. No evidence was
  found that numbers were made up to meet it (cash taxes and the Core reconciliation below point the other way), and the FY2027
  guide (core EPS *"in-line to three percent"*) was set **below** the algorithm, which is the candid direction.
- [ ] **serial share issuance**: no: common shares outstanding fell from 2,357,051K (June 2024) to 2,323,859K (June 2026) and
  equity plans are settled from treasury (Note 7).
- [ ] **EBITDA / adjusted-earnings promotion [E4-29]**: **EBITDA: zero occurrences** in the five releases read (FY25 Q4 through
  FY26 Q4) and in the 10-K. **Core EPS is the headline** of every release, beside GAAP EPS in the same line (*"Diluted EPS +2%; Core
  EPS +1%"*). Read under [E2-57] and [E3-53] below; not scored as the EBITDA flag.
- [ ] **filed-figure tells [E4-30]**: cash taxes paid **$4,678M, $4,554M, $4,363M** against book tax of $4,233M, $4,102M, $3,787M
  (FY2026-2024, Note 5): cash taxes run **above** book, the opposite of the tell. Reported growth is not unnaturally smooth (core EPS
  +12% then +1% within three years).
- **The except-for flag [E2-57] and the restructuring charge [E3-53], read on the Core reconciliation.** Core EPS against diluted
  EPS (10-K statements and reconciliations): FY2016 $3.67/$3.69, FY2017 $3.92/$5.59, FY2018 $4.22/$3.67, FY2019 $4.52/$1.43, FY2020
  $5.12/$4.96, FY2021 $5.66/$5.50, **FY2022 $5.81/$5.81 and FY2023 $5.90/$5.90 (no adjustment at all)**, FY2024 $6.59/$6.02, FY2025
  $6.83/$6.51, FY2026 $6.89/$6.62. **Gains are excluded as well as charges** (the FY2017 Beauty divestiture gain, the FY2026 Glad
  gain), an *"ongoing"* restructuring level of $250-500M a year stays **inside** Core, and every excluded item is quantified line by
  line (the FY2026 reconciliation: cost of products sold, SG&A, other non-operating, taxes). That passes the half-owner test's own
  example: *"a one-time item quantified separately at every line passes"* **[E2-26]**. **What fires is recurrence:** non-core
  restructuring in FY2024, FY2025, FY2026 and guided again for FY2027 ($0.13-0.17 a share), and a $1.2bn Argentina/Nigeria
  programme plus a $1.5-2.0bn two-year plan. **[E5-33]: these are real costs, and owner earnings at Q4 are built from cash flow,
  so they are counted there whatever Core says.**

**STEP 3: THE PRIMARY TEST [E2-01]**, balance sheet first. Return on average total equity (net earnings attributable to P&G over
the average of opening and closing equity including non-controlling interest, companyfacts, tied to the FY2026 statements
$16,046M and $54,311M/$52,284M): **FY2008-2016 16-20% (10.6% in FY2015), FY2017 26.9% (divestiture gain), FY2019 7.8%
(impairment), FY2020-2026 27.6, 30.6, 31.5, 31.2, 30.5, 31.1, 30.1%**, without undue leverage (debt $34.1bn against equity $54.3bn).
The equity denominator carries **$41.3bn of goodwill and $21.4bn of intangibles**, mostly the 2005 Gillette purchase, so the
**[E2-43]** denominator, net tangible operating assets, is the better guide and is in Q2 (40-50% FY2016-18, 78-92% FY2021-26). **[E2-73]**
the operators are judged on the assets they work with: on that measure the business has been run very well since FY2019.

**The half-owner test [E2-26].** Passes on three counts read in the filing: the segment share changes are published every year
**including the declines** (the table in Q2 has 41 negative cells, all in the company's own words); the Gillette intangible's
sensitivity and headroom are published even in years with no charge; the Core reconciliation excludes gains as well as charges.
**Against it:** the long-term algorithm keeps being printed after five years of missing it, and the headline of every release is
Core, not GAAP.

**Pay, and what it vests on [E4-27]** (DEF 14A filed 2026-08-28, `0001193125-26-372211`). STAR bonus: a Business Unit Factor (70%
weight) scored on *"Organic Sales Growth ... Operating Profit Growth ... Adjusted Free Cash Flow Productivity ... Value Share ...
Operating TSR ... Internal Controls"*, and a Total Company Factor, *"Organic Sales Growth and Core EPS Growth"*, 50% each, whose
targets *"are typically linked to the external financial guidance provided at the beginning of the fiscal year, and the Core EPS
target specifically includes the expected impact of our share repurchase program"*. PSP (three years): *"Relative Organic Sales
Growth ... Core EPS Growth ... Constant Currency Core Before-Tax Operating Profit Growth ... Adjusted Free Cash Flow
Productivity"*, times a Relative TSR Multiplier (75%-125%). **Two readings.** For: **value share is a paid metric**, so the moat
metric of Q2 is in the bonus; cash conversion is paid; and the yardstick held when it read badly, *"His STAR payout was $1,634,720,
which is approximately 60% of target"*, *"PSP paid out at 69% of target, based on delivering results below the target"*. Against:
**pay is set against the company's own guidance and on Core EPS, which excludes the recurring restructuring**, and **the Core EPS
target has the planned buyback built in**, so the plan pays for executing a fixed dollar repurchase, not for its price. That is the
incentive the next paragraph reads.

**The institutional imperative: all four scored [E2-30].**
- [ ] resists change in current direction: not found: Batteries (FY2016) and the Beauty brands to Coty (FY2017) divested, both visible in the cash-flow statements, the 2019 re-organisation into
  Sector Business Units, the Argentina and Nigeria exits, 7,000 overhead roles being cut.
- [ ] projects/acquisitions soak up funds: not found on the record: acquisitions, net, $11-$3,945M a year across FY2018-2026
  against adjusted free cash flow of $14-16bn; **Thorne ($3.8bn) is the second-largest in the window and is watched, not scored.**
- [ ] staff studies for the leader's craving: cannot be observed from filings; not scored.
- [x] peers mindlessly imitated: **prompt, weakly**: a fixed annual dollar buyback announced with the guidance is the industry's
  norm, and P&G's is set that way (*"at a value of approximately $5 billion in fiscal year 2026"*, Item 5).

**Capital allocation: the buyback conditions [E5-08, E4-31].**
- (1) **Ample funds: yes.** Operating cash $19.6bn, capex $4.4bn, dividends $10.2bn, buybacks $5.0bn, debt roughly level; current
  liabilities exceed current assets by $12.5bn by design (supplier terms), with an undrawn $8.0bn facility.
- (2) **A material discount to intrinsic value, conservatively calculated: NOT DEMONSTRATED.** Average prices paid, from the equity
  statements: **FY2024 $157.3 (5,014/31.877M), FY2025 $169.0 (6,517/38.552M), FY2026 $150.4 (5,029/33.437M)**; May-June 2026 $147.46
  (Item 5). The owner-earnings yield at those prices is set out in Q4 (arithmetic, not a clearance). Repurchases are a **fixed annual dollar amount set with the guidance** and financed
  *"through a combination of operating cash flows and issuance of debt"* (Item 5), with no stated reference to value. **(3)**
  [E4-31] the information to estimate value is supplied (the filing is full). **CAPITAL ALLOCATION FLAG on condition (2)**, stated
  with the humility clause: *"it is natural for CEOs to be optimistic about their own businesses. They also know a whole lot more
  about them than I do"* **[E4-13]**, and *"many CEOs never stop believing their stock is cheap"* **[E5-08]**. **It binds position
  size, never the discount rate** (CONVENTION, labelled in the framework).
- **Retention [E3-54]** is weakly informative here: dividends plus buybacks ($15.2bn) took essentially all of FY2026's adjusted free
  cash flow ($15.8bn), so very little is retained to test.

**THE GUARDRAIL: checked before the verdict.**
- [x] Confirmed: nothing here is used to promote the name. A good record since FY2019 cannot repair Q2's NARROW class or substitute
  for Q4 **[E2-37, E2-38, E3-39]**.
- [x] "Requires a great manager": not found. The FY2013-2018 record (poor years, franchise intact) is the evidence, recorded at Q2
  **[E4-23]**.
- [x] Great manager as the reason to act: not the case here **[E2-35, E2-36]**; no turnaround thesis is needed or offered.
- **Management change, recorded:** Jon Moeller, CEO from 2021, became Executive Chairman and retired from the board on 2026-07-31
  (8-K 2026-07-29, `0000080424-26-000094`); Shailesh Jejurikar, with P&G since 1989 and COO 2021-2025, is CEO and, from 2026-08-01,
  Chairman. Four of the five sector CEOs are new since 2025 (FY2026 10-K executive-officer list). A develop-from-within succession,
  and a new team that has not yet been judged on its own record.

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *IN as the absence of found disqualifiers, not a finding that the managers are honest **[E5-17]**. The 2010-2011 European cartel
  fines are recorded against the company, dated, and self-investigated. Two prompts are live and carried to Q6 and to sizing: the
  growth-target flag (an algorithm missed for five years and still printed, with pay set against guidance), and a capital-allocation
  flag on buyback condition (2) (a fixed dollar repurchase at prices where no conservative value shows a material discount). IN never
  promotes.*
## Q4 — WILL IT SURVIVE?

### Owner earnings: the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its long-term competitive position and
> its unit volume. (… the working capital **increment also should be included in (c)**.)" … "**(c) must be a guess**."

**Built from the filed cash-flow statements, never from net income.** Each year is taken from the first 10-K that reports it
(FY2011 Exhibit 13 for FY2009-11, FY2014 10-K for FY2012-14, FY2017 for FY2015-17, FY2020 for FY2018-20, FY2023 for FY2021-23,
FY2026 for FY2024-26; the compacted statements are in `_research 2026-09-25 PG/cfs_out.txt`, arithmetic in `oe.py`, output
`oe_out.md`). OE = operating cash flow − share-based compensation − (c), with (c) shown at both ends: D&A (the corpus default
**[E3-44, E2-41]**) and total capex. Operating cash flow nets the working-capital change from one audited line (the CONVENTION in
the framework's section VI).

| FY | OCF | SBC | D&A | capex | capex/D&A | OE, (c)=D&A | OE, (c)=capex | company's one-off tax in OCF |
|---|---|---|---|---|---|---|---|---|
| 2009 | 14,919 | 516 | 3,082 | 3,238 | 1.05 | 11,321 | 11,165 | 0 |
| 2010 | 16,072 | 453 | 3,108 | 3,067 | 0.99 | 12,511 | 12,552 | 0 |
| 2011 | 13,231 | 414 | 2,838 | 3,306 | 1.16 | 9,979 | 9,511 | 0 |
| 2012 | 13,284 | 377 | 3,204 | 3,964 | 1.24 | 9,703 | 8,943 | 0 |
| 2013 | 14,873 | 346 | 2,982 | 4,008 | 1.34 | 11,545 | 10,519 | 0 |
| 2014 | 13,958 | 360 | 3,141 | 3,848 | 1.23 | 10,457 | 9,750 | 0 |
| 2015 | 14,608 | 337 | 3,134 | 3,736 | 1.19 | 11,137 | 10,535 | 729 |
| 2016 | 15,435 | 335 | 3,078 | 3,314 | 1.08 | 12,022 | 11,786 | 0 |
| 2017 | 12,753 | 351 | 2,820 | 3,384 | 1.20 | 9,582 | 9,018 | 418 |
| 2018 | 14,867 | 395 | 2,834 | 3,717 | 1.31 | 11,638 | 10,755 | 0 |
| 2019 | 15,242 | 515 | 2,824 | 3,347 | 1.19 | 11,903 | 11,380 | 235 |
| 2020 | 17,403 | 558 | 3,013 | 3,073 | 1.02 | 13,832 | 13,772 | 543 |
| 2021 | 18,371 | 540 | 2,735 | 2,787 | 1.02 | 15,096 | 15,044 | 225 |
| 2022 | 16,723 | 528 | 2,807 | 3,156 | 1.12 | 13,388 | 13,039 | 225 |
| 2023 | 16,848 | 545 | 2,714 | 3,062 | 1.13 | 13,589 | 13,241 | 225 |
| 2024 | 19,846 | 562 | 2,896 | 3,322 | 1.15 | 16,388 | 15,962 | 422 |
| 2025 | 17,817 | 476 | 2,847 | 3,773 | 1.33 | 14,494 | 13,568 | 562 |
| 2026 | 19,556 | 524 | 3,160 | 4,409 | 1.40 | 15,872 | 14,623 | 688 |

*($ millions. "One-off tax" is the company's own exclusion in its adjusted free cash flow reconciliations: divestiture taxes in
FY2015 and FY2017, the 2017 Tax Act transition tax FY2019-2026, the last of it paid in FY2026. Shown, not added back.)*

**MORE THAN ONE WINDOW: THE SPREAD IS PART OF THE RANGE [E4-25].** Every window the filings allow, at both (c) ends:

| window | OE, (c) = capex | OE, (c) = D&A | yield on the $348.3bn as-converted cap | one-off taxes added back (sensitivity only) |
|---|---|---|---|---|
| 3y FY2024-26 | **$14.7bn** | **$15.6bn** | 4.23% / 4.47% | $15.3bn / $16.1bn |
| **5y FY2022-26 (the default window [E2-42])** | **$14.1bn** | **$14.7bn** | **4.04% / 4.23%** | $14.5bn / $15.2bn |
| 10y FY2017-26 | $13.0bn | $13.6bn | 3.74% / 3.90% | $13.4bn / $13.9bn |
| 18y FY2009-26 | $12.0bn | $12.5bn | 3.43% / 3.58% | $12.2bn / $12.7bn |
| prior 5y FY2017-21 | $12.0bn | $12.4bn | 3.44% / 3.56% | $12.3bn / $12.7bn |

- **Short-window mean** (3y): $14.7-15.6bn · **default** (5y): $14.1-14.7bn · **long-window mean** (18y): $12.0-12.5bn.
- **Spread, conservative end:** 18y against 3y is **-19%**; 5y against 3y **-4.3%** (`run.py` printed the same -4.3%).
- **Combined range (window × capex band): $12.0bn to $15.6bn, yields 3.4% to 4.5%.** Wide in dollars; **not too wide to reach a
  conclusion**, because every point in it sits far below the ~10% floor Q5 will apply first, so no verdict turns on where in the
  band the truth lies. That is recorded here as a fact about the range, not as a Q5 answer.
- **What the spread is.** Mostly growth, not distortion: the long window reaches back to a larger but slower perimeter (the FY2009-
  2016 statements include Pringles until FY2012, Pet Care until FY2015, Batteries until FY2016 and the Beauty brands until FY2017, as
  discontinued or continuing operations, within one OCF line), and owner earnings rose from about $12bn (prior five years) to about
  $14-15bn (latest five), roughly 3-4% a year. **The distorted years are named [E5-11]:** FY2017 (OCF $12.8bn, with $418M of
  divestiture tax), FY2011-12 (OCF $13.2-13.3bn), FY2024 (the $1.2bn Argentina/Nigeria programme was mostly non-cash).
- **Normalising for luck [E4-41], both directions named and quantified, neither substituted.** Favourable: the supplier-terms stretch.
  Payables were **18.0%** of sales at the start of the default window (June 2021: $13,720M on FY2021 sales of $76,118M) and **18.7%** at
  its end (June 2026: $16,306M on $87,032M); the ratio's rise alone is worth about **$0.6bn over five years, about $0.12bn a year** of the
  5-year mean (the larger stretch, 14.3% to 18.0% of sales, happened FY2016-2021 and sits in the 10-year window). Unfavourable: the
  transition tax, **about $0.42bn a year** of the same window, now finished. **Net, the default window's cash is understated by about
  $0.3bn a year rather than flattered; the unadjusted band is carried, which errs by that much on the conservative side** and is counted
  as a windage at Q5.
- **Maintenance capex: a DISCLOSED JUDGMENT with a corpus DEFAULT.** P&G is not in the named exception class (railroads, airlines,
  utilities), and its filing does not say depreciation understates renewal. **But capex exceeded D&A in 17 of 18 filed years**, mean
  1.17 times over eighteen years and **1.40 times in FY2026**, while organic volume grew about 1.3% a year over ten years and **not
  at all over the last five**; D&A includes $308M of acquired-intangible amortization (Note 4) that renews nothing; the segment note
  shows Baby, Feminine & Family Care capex of $1,520M against D&A of $835M in FY2026; and **the FY2027 guidance is *"Capital spending
  is estimated to be in the range of four and a half to five and a half percent of fiscal 2027 net sales"***, i.e. about $4.0-4.9bn,
  above D&A again. Under [E4-47], replacement in today's dollars outruns depreciation charged in older ones, and the last five years
  are the inflation years. **The guess: (c) sits near the TOTAL-CAPEX end, and the capex end is the one carried as the conservative
  figure; the D&A end is displayed as the optimistic bound, not as an equally good answer.** No volume was bought with the recent
  capex that the filings show, which is why it is not treated as growth spending.
- **Stock compensation subtracted in full [E5-06]: SBC RESOLVES in all 18 years** (a filed cash-flow line every year, $335-562M) **and
  is complete** on the evidence read: (i) equity awards are settled from treasury (Note 7), so there is no second stock-settled plan
  outside the SBC line except (ii) the **ESOP**, whose Series B preferred funds retiree health care; those shares are **outstanding
  and counted in the as-converted cap** (Step 0), which is where that stock-settled benefit cost is carried; it is not subtracted a
  second time. **[E3-70] market-value measure**: FY2026 grants at grant-date fair value, options 8,769K × $33.17 = $291M, RSUs 1,704K ×
  $152.91 = $261M, PSUs 585K × $161.53 = $94M, **about $646M against the $524M charge**; SBC is 2.7-3.0% of operating cash, not
  material in [E3-70]'s sense; the difference (about $0.12bn) is inside the band's width and is stated rather than added.
- *If the capex band changes the verdict → UNKNOWABLE.* It does not: both ends carry the same Q4 verdict and the same Q5 floor answer.

### Great, good, or gruesome? **[E4-20]**
- [ ] great  [x] **good**  [ ] gruesome
- **Evidence.** Pre-tax returns of 78-92% on net tangible operating assets FY2021-26 (40-50% before the payables stretch), capex about
  5% of sales, working capital negative: very little capital is added to earn the return, which is the *great* account's shape. **But
  the rate is not rising**, operating margin has sat at 22-24% since FY2021 and owner earnings grow about 3-4% a year, mostly on price;
  the *great* account *"pays an extraordinarily high interest rate that will rise as the years pass"*, and the filing shows the high rate
  without the rise. **Good, at the high end of good.** Not gruesome on any measure.

### Staying power: score all three **[E5-11]**
- **(1) A large and reliable stream of earnings: YES.** Owner earnings positive at both (c) ends in all 18 filed years, $8.9-16.4bn;
  the worst year (FY2012 capex end, $8.9bn) was 63% of the latest five-year mean at the same end.
- **(2) Massive liquid assets: NO, BY DESIGN.** Cash $9.9bn against debt due within one year of $11.3bn (commercial paper $4.8bn,
  current long-term debt $6.5bn), current liabilities exceeding current assets by $12.5bn, and an **$8.0bn** bank facility, of which
  **$4.8bn is 364-day and expires October 2026** (MD&A, Liquidity). The company says it will *"support our short-term liquidity and
  operating needs largely through cash generated from operations"* and refinance maturities *"in commercial paper and bond markets"*.
  **That is reliance on the kindness of strangers [E5-39]**, mitigated by AA-/Aa3 ratings and facilities with no rating triggers or
  material adverse change clauses.
- **(3) No significant near-term cash requirements: REQUIREMENTS EXIST, AND ARE COVERED BY ONE YEAR OF EARNINGS.** Contractual
  payments due within a year **$13.8bn** (debt $11.4bn, interest $0.9bn, pensions $0.2bn, purchase obligations $1.2bn); Thorne
  **$3.8bn** at closing in fiscal Q2 2027; dividends **$10.2bn** a year, discretionary in law and a 70-year record in practice. Against
  that: one year's owner earnings of $14-16bn and $9.9bn of cash. **The debt is rolled, not repaid, and that is the one place the
  structure depends on markets.** Also a supplier-side dependence: **$6.2bn of payables sits in supply-chain finance** with third-party
  banks (Note 14); if those banks withdrew, suppliers could press for shorter terms, a one-time working-capital outflow of up to that
  order, which is inside one year's owner earnings.
- **Leverage, named and quantified [E4-16, E3-29].** Total debt $34.1bn; interest expense $877M against operating income $19.7bn,
  **about 22 times**; **[E2-54]**'s coverage test, *"all interest, both payable and accrued, to be comfortably met out of current cash
  flow net of ample capital expenditures"*: interest of $0.9bn against owner earnings after full capex of $14.1-14.7bn, met about
  sixteen times over. **[E3-52]** read the terms: the debt is market debt with maturities, not float; the ladder is published and
  spread to 2045 (cover-page notes).
- **Jurisdiction [E3-66]:** Ohio registrant, US law; operations in about 65 countries, more than half of sales outside the US, with
  Argentina liquidated (FY2025), Pakistan liquidated (FY2026) and Russia at 1% of sales. The owner stands where US shareholders stand.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40, E4-51]**
- **The mechanism: SHAPE #19, THE SHELF, with #11 THE PASS-THROUGH as a feature** (`Screens/SURVIVAL SHAPES - index.md`; #19 was
  named on the CL run and fits here without modification). The brands are owned; the route to the buyer is rented from retailers who
  are concentrated (**Walmart about 16% of sales, the top ten about 43%**, Item 1), stock their own private label beside every P&G
  brand (*"we compete against other branded products as well as retailers' private-label brands"*), own the shopper data and the
  retail-media platforms the 10-K now names (*"retailers are selling across multiple platforms (digital and physical outlets) and
  building their own media platforms"*), and reset trade terms every year (Item 1A: *"If we cannot reach agreement with a key
  customer on trade terms and principles, our business performance could suffer"*). The pass-through feature: productivity is the
  stated engine (*"Our business model relies on continued productivity improvements to fuel investments"*), and FY2026 shows where
  the savings went, **180bp of manufacturing productivity in gross margin, against 70bp of product and packaging investment, 120bp of
  unfavourable mix, and an 80bp rise in marketing as a share of sales, with gross margin down 100bp and operating margin down 160bp.**
- **Quantified from filed figures.** Each point of FY2026 operating margin is **$0.87bn** pre-tax, about **$0.69bn** after the 20.8%
  effective rate. **Scenario: operating margin returns from 22.7% to the FY2016-2018 level, about 20.6% (the years of share loss).**
  That is **2.1 points, about $1.8bn pre-tax, $1.45bn after tax**, taking the five-year owner-earnings band from $14.1-14.7bn to about
  **$12.6-13.3bn**, a fall of about 10%. **The company lives comfortably** (interest still covered about fourteen times at the capex
  end); **the owner's return compresses.** A harsher case, family-care-style price giveback spreading (FY2026: *"lower pricing (due to
  merchandising investments)"*) to a full reversal of the FY2023 +9 points of price with no cost relief, is not modelled as a
  likelihood: nothing in the filings shows it beginning outside Family Care.
- **Likelihood: [ ] likely [x] a real possibility [ ] a low-level possibility.** FY2026 already shows the first half of the mechanism:
  gross margin -100bp, operating margin -160bp, share down in three of five segments, *"competitive activity"* cited nine times, and
  the FY2027 guide carrying *"a headwind of approximately $1 billion after-tax driven by higher raw materials, energy and transportation
  costs"*. **[E4-40] exposure, not experience:** the benign FY2019-2024 share record is exactly the experience the corpus warns against
  reading as protection; the exposure is the 43% top-ten concentration and the private label on every shelf.
- **The argument against my own position, stated as its holders would [E4-51]:** the retailer has needed P&G's brands for decades,
  the FY2013-2018 period was this mechanism at work and the business came out of it with higher margins, and the FY2022-24 pricing
  record shows the shelf did not stop P&G passing on seventeen points of cost. Granted; that is why the likelihood is *a real
  possibility* and not *likely*, and why the named death is compression, not failure.
- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *IN. Owner earnings are real, positive in all 18 filed years, built from the filed cash-flow statements with SBC resolved and
  complete, and carried as a range of $12.0-15.6bn (five-year default $14.1-14.7bn, capex end the conservative figure). Good, not
  great. Staying power holds on (1) and (3), with (2) weak by design and the debt rolled rather than repaid. The named death is #19 the
  shelf with #11 as a feature, a real possibility that compresses the owner's return by about a tenth in the modelled case and does
  not threaten the company.*
---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q1 IN, Q2 IN (NARROW), Q3 IN (overlay), Q4 IN. **Q5 opens.**

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on ... we don't want to buy equities where our real
expectancy is below 10 percent."* Arithmetic in `_research 2026-09-25 PG/q5.py`, output `q5_out.txt`. Inputs: five-year default
owner earnings **$14,087-14,746M** (capex end / D&A end, Q4), as-converted shares **2,391.1M**, price **$145.68** (close 2026-09-24,
aggregator, flagged), cap **$348.3bn**, sovereign **5.47%** (US Treasury, 30 Yr, 09/24/2026).

**The growth the record supports, stated before it is spent.** Owner earnings (capex end) grew from a five-year mean of $10.3bn
(FY2012-16) to $14.1bn (FY2022-26), **3.2% a year**, and from $12.0bn (FY2017-21) to $14.1bn, **3.3% a year**; the diluted share count
fell about **1.0% a year** (2,471.9M FY2024 to 2,422.5M FY2026, Note 6). **So about 3% a year in total and about 4.25% a year per share
is what the filed record has actually delivered.** The FY2012-16 base includes businesses since sold, so the ten-year rate mixes
perimeters; the five-year rate does not, and they agree. Core EPS grew 4.0% a year FY2021-26 on the company's own measure. **[E4-35]**
is the check on anything higher: sustained double-digit growth is a fewer-than-one-in-twenty event among the most profitable
companies, and nothing here asks for it.

**Honest pre-tax expectancy at $145.68** (yield plus growth; the yield is after corporate tax, so this errs low, and the floor is
judged on it as the corpus's own examples are):
- at **g = 0**: **4.0-4.2%**
- at **g = 3.0%** (total owner-earnings growth, both windows): **7.0-7.2%**
- at **g = 4.25%** (the full per-share rate, buybacks included): **8.3-8.5%**
- **Growth needed to reach the floor: 5.8-6.0% a year in perpetuity**, against a filed record of 3-4.25%. The screen row's
  `growth_required` 0.0578 is reproduced (5.77% at the D&A end).
**Below roughly 10% on every construction, by 1.5 to 3.0 points. QUIT ON; the name is not ranked.** No risk premium is in any rate
**[E3-42]**.

**One book. Owner earnings against the bond.** A DCF may run as an engine; it casts no vote **[E3-34]**.

**1. THE YIELD**
- owner earnings **$14.1-14.7bn** ÷ market cap **$348.3bn** = **4.04-4.23%** · sovereign **5.47%**. On the common-only cap
  ($338.6bn) the yield is 4.16-4.35%; the screen's 4.22% bottom is reproduced within rounding at its stale cap.
- Every window: 3y 4.23-4.47%, 10y 3.74-3.90%, 18y 3.43-3.58%. **No window and no (c) end yields as much as the bond.**

**2. WHAT THE PRICE ALREADY ASSUMES**
- at the bare bond rate, perpetual growth of **1.2-1.4% a year** (5.47% less the yield); at the ~10% floor, **5.8-6.0% a year**.
  (`tools/run.py`'s engine, a ten-year fade to a 2.5% terminal rate at 5.47%, prints year-1 growth of -6.2% and +1.58 to +1.84 points
  over the sovereign; it is an engine with a built-in 2.5% perpetual growth rate and casts no vote.)
- what the business has actually done: **3.2-3.3% a year** in owner earnings, about 4.25% per share.

**3. WHAT YOU ARE PAID**
- the yield alone is **1.2-1.4 points BELOW the sovereign**; with the filed growth the expectancy is **1.6-3.0 points over the
  sovereign and 1.5-3.0 points under the floor.**

**WHERE CERTAINTY IS PRICED: AND IT IS NOT IN THE RATE [E3-42].**
- sovereign used **5.47%**, the bare rate, no per-name premium.
- Certainty is handled at Q1 (passed) and in the end margin, once **[E4-11, E4-48]**; no margin is needed here, because the price is
  above the value before any margin is applied.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]**: the price at which the ~10% floor is met:
- **conservative about $85** (g = 3.0%, capex end) · **optimistic about $110** (g = 4.25%, D&A end with the one-off taxes added back)
  · **current price $145.68**. At zero growth the floor value is about $60.
- **The ceiling [E2-63]:** the upside is bounded by owner-earnings growth, and [E4-44] says the value cannot outgrow the earnings;
  nothing in the filings points to growth above the 3-4% record, and FY2027 is guided at core EPS *"in-line to three percent"*.

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- floor verdict first: honest pre-tax expectancy **7.0-8.5%** (4.0-4.2% at no growth) vs ~10% **[E4-28]**: **below, so quit on,
  and the ranking lines are not filled in.**

**WHICH BAR ARE YOU USING?**
- [ ] Normal method [E4-11]: not reached: the price is above the value before a margin.
- [x] **Screamer test [E4-01]**: the conservative case is about $85 and the most generous about $110; **the price of $145.68 is above
  the whole range. Outcome: no.**
- **Windage count: TWO**, both small and both justified: (i) the capex end of (c) carried as the conservative figure (disclosed at
  Q4 as the judged position, not a stacked discount); (ii) the default window left unadjusted where the two named normalisations net
  to about +$0.3bn a year in the company's favour. **Removing both** (D&A end, one-off taxes added back, full per-share growth) gives
  about $110, still **25% below the price**; the verdict does not depend on either.

- **VERDICT:** [ ] IN — RANKED  **[x] NOT IN — QUIT ON, below the ~10% floor [E4-28]**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *A price answer, not a verdict about the business: Q1-Q4 are all IN. At $145.68 the owner-earnings yield is 4.0-4.2%, below the
  5.47% bond, and the expectancy with the filed growth is 7.0-8.5% against the ~10% floor.*

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Pre-committed before entry [E1-02]**: for a name not bought, these are the conditions under which the file is re-opened, and the
falsifiers that close it at Q2 if they fire first:
- **Thesis-confirming metric:** filed segment share changes net positive across the five segments in a fiscal year, with organic
  volume positive, while price is also positive (the FY2022-24 pattern) **[E2-44, E4-55]**.
- **Thesis-breaking metrics (each a Q2 falsifier; any one fired VOIDS the price bands below until a full re-run):**
  1. **Share declines in three or more of the five segments for a THIRD consecutive fiscal year** (FY2025 and FY2026 already show
     three; the FY2027 10-K, due about August 2027, is the test) **[E4-32, E4-17]**.
  2. **Organic volume negative for two consecutive fiscal years** at the total-company line **[E4-55]**.
  3. **Net price negative at the total-company line in any fiscal year**, or Family Care's *"lower pricing"* spreading to a second
     segment **[E4-37]**.
  4. **GAAP operating margin below 20.6%** (the FY2016-2018 level) for two consecutive fiscal years, which is the named-death scenario
     at Q4 arriving **[E3-30]**.
  5. **A goodwill or Gillette impairment beyond the FY2024 carrying value**, or Walmart's share of sales rising above 20% **[E4-40]**.
- **Next catalyst date:** the Q1 FY2027 release and 10-Q (late October 2026); Thorne closing (fiscal Q2 2027); the FY2027 10-K
  (early August 2027); the re-strike of these bands on that 10-K.

**Price bands (the QLYS ruling: a gate-clearer failed on price carries bands; each a prompt for a FULL v4.1 re-run, never a
purchase):**
- **$84.16**: the ~10% floor met at g = 3.0% on the five-year capex-end owner earnings ($14,087M / 0.07 / 2,391.1M): the growth the
  filed record supports.
- **$107.25**: the floor met only if the full 4.25% per-share rate is granted in perpetuity at the D&A end ($14,746M / 0.0575 /
  2,391.1M); re-test that rate against the then-current share and volume series before spending it.

**The sell rule [E2-28]**: not engaged; no position is held or proposed.
- *Price appreciation and holding period are explicitly rejected as reasons to sell.*

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring question for this name is exactly FY2025-26:
is the renewed share slippage and the nine-fold "competitive activity" an aberrational cycle, like FY2013-2018 from which the business
came back stronger, or has the shelf **[#19]** moved against it in a way that permanently reduces value? The falsifiers above are set so
that the FY2027 10-K answers it.

**Do not trim winners [E5-14].** **Position size:** none; the name is not ranked. If a band fires and a re-run clears, the two live Q3
prompts (the growth-target flag and the capital-allocation flag on buyback condition (2)) size any position DOWN (CONVENTION, labelled
in the framework).

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *The exit and re-entry conditions are pre-committed and dated; the name is watch-listed, not held.*

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1-Q4 IN; Q5 opened only after all four were IN; Q5 QUIT ON.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q2's competitor row carries three non-SEC peers from
  their own annual reports (rung 3 of the ladder) and Clorox carried from the CLX run with its different numerator labelled; the class
  is NARROW, not PROVISIONAL, and the verdict rests on the company's own fourteen-year share series and the ten SEC-filed peers.
- [x] Every UNRESEARCHED verdict names the artifact: none used.
- [x] Every UNKNOWABLE verdict states what cannot be known: none used.
- [x] Step 0: the filing was read, accession `0000080424-26-000103`; OCF $19,556M cross-checked filed statement = tag = MD&A.
- [x] Owner earnings on multi-year means, every window shown (3y, 5y, 10y, 18y and the prior 5y) at both (c) ends; (c) disclosed as a
  judgment near total capex; SBC resolves 18/18 and is complete; no net-income proxy anywhere.
- [x] Competitor row filled: fourteen peers named, four non-SEC not rowed and named.
- [x] Sovereign for the earnings currency (USD), from the issuing authority (US Treasury), dated 09/24/2026, raw file saved; FRED not
  used.
- [x] Value as a round-number range (about $85 to $110; $60 at zero growth).
- [x] One bar chosen (screamer), windage count TWO, stated and justified.
- [x] Prices dated; the aggregator (Yahoo chart endpoint) used for the live quote only, flagged; raw response saved.
- [x] Run committed to git after every gate (commits listed in the register entry).

**The brief's priors, each tested:**
- `cap_m` 333,440: **stale, re-struck**: $348.3bn as-converted, $338.6bn common only at $145.68.
- `oe_bottom_m` 14,087 / `oe_top_m` 15,585: **confirmed to the dollar**: 5y capex end and 3y D&A end of the table at Q4.
- `spread` 0.106 and `spread_caveat` (*"CANNOT see variation older than the 5-year window; rebuild it [E4-25]"*): **acted on**:
  rebuilt to 18 filed years from six 10-Ks and one Exhibit 13; the older windows are LOWER (18y $12.0-12.5bn), so the caveat was
  right that the screen's width understated the range, in the direction that makes the name dearer.
- `cap_flag` empty: **confirmed empty in effect**; no share-class or float inconsistency, but the cover count omits 66.6M one-for-one
  convertible preferred (2.9% of the economic count), which the cap here includes.
- `deal_note` empty: **half right**: no live deal makes the quote a spread, and a live **$3.8bn acquisition (Thorne, agreed
  2026-08-04)** exists that no 8-K item carries; found only in the 10-K MD&A and Note 15. **The fourth `deal_filings()` blind spot in
  a week** (after WS, DMC, TTSH), this time on the buy side.
- `name_change_note`, `wc_note`, `acq_note`, `da_note` empty: confirmed: no name change; no working-capital line of the cash-flow statement moved
  more than 30% of a year's OCF in the five-year window (the largest, "Other" -$1,653M in FY2025, is 9.3%); acquisitions
  small except FY2019 ($3,945M) inside the ten-year window; D&A tag resolves every year.
- `yield_bottom` 0.0422 / `vs_sovereign` -0.0113: **refuted in level, confirmed in sign**: 4.04% on the as-converted cap against a
  sovereign re-struck at 5.47%, -1.43 points.
- `growth_required` 0.0578: **confirmed** (5.77-5.96%).
- `level_shift` 1.15 "no step" / `level_shift_oe` 1.14: confirmed in effect: the recent five years are about 17% above the prior
  five, a steady rise, not a step.
- `best_year_dep` 0.018 / 0.023, *"no single-year dependence"*: confirmed: dropping FY2024, the best year, moves the 5-year capex-end
  mean by 3.3%.
- `flags_disagree` empty, `window_disagree` empty: consistent with the above.
- `years_filed` 19: the run used 18 (FY2009-2026); FY2008 was not needed for any window and was not read.
- `newest_filing` / `newest_periodic` 2026-06-30: **confirmed**: no 10-Q since the 10-K.

**Tooling defects found (none patched):**
1. `deal_note()` blind to an agreed acquisition disclosed only in a 10-K (no 8-K item because it is below the significance test); the
   fourth deal blind spot this week, the first on the buy side.
2. `cover_shares.py` reports the common only and cannot see one-for-one convertible preferred that draws the common dividend; the
   screen's cap is 2.9% low for PG on that ground (the resume state recorded the same class of limit at MRVL).
3. `peer_metrics.py`'s sales tag picks `Revenues`, which for PG FY2012-2014 carries a non-total figure (28,400, 29,200, 29,400); the
   run substituted `SalesRevenueNet` for PG and says so; any other run reading PG's early years through the same function inherits it.
4. `run.py` prices the intraday quote while the sovereign is the prior day's close; immaterial here ($145.87 vs $145.68).

**My own errors, recorded:**
1. `put_section.py` replaced the template's `---` separator above the Q5 stop-sign when Q4 was inserted (commit `cc490f5`); restored in
   this section.
2. The first Q3 draft stated a buyback-era long-bond range and an owner-earnings yield range before either had been computed, and
   *"about 100 brands divested"* from memory; all three were removed before commit `6135b79` (the committed text carries only filed
   facts).
3. The first Q4 draft measured the payables stretch against the wrong year's sales (17.1% instead of 18.0%), which overstated it
   2.3-fold and produced a false "roughly cancel"; corrected before commit `cc490f5`.
4. An early `grep -o` over whole 10-Ks timed out and was abandoned for a Python extraction; no data came from it.
5. The Reckitt re-read failed (the exact quoted sentence did not match the CLX run's PDF text layer), so Reckitt is named and not
   rowed rather than carried unverified.

## REGISTER
- Verdict: Q1 IN · Q2 IN (NARROW) · Q3 IN (overlay) · Q4 IN · **Q5 NOT IN: QUIT ON, below the ~10% floor [E4-28]** · Q6 IN
- One line: **P&G clears all four business gates, a NARROW franchise with the highest operating margin in a fourteen-company row and a
  shelf-shaped named death; at $145.68 the owner-earnings yield is 4.0-4.2% against a 5.47% bond and the expectancy with the filed
  3-4.25% growth is 7.0-8.5%, so it is quit on at the floor. Value at the floor about $85-110.**
- **If UNRESEARCHED: THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.
