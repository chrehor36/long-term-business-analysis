
## MATERIAL BENEATH THE CLOSE: recorded, not governing

*The file closed at Q2 OUT. What follows was gathered while the business questions were being read, and because the brief asked for the owner-earnings rebuild; it is recorded so the next reader does not have to fetch it again. **None of it is a verdict, none of it can reopen Q2 [E2-37, E3-39], and the valuation arithmetic is headed as the protocol requires.***

### Q3 prompts (no verdict)

**Weight case, as it would be declared:** **daily execution, yes**: a supplier whose price is fixed at the award and whose margin depends on launch execution, scrap and press utilisation (MD&A: *"Performance is also affected by manufacturing efficiencies, including items such as on time delivery, quality, scrap, and productivity"*; new programmes *"are typically extremely complex in nature"*), [E3-38]'s have-to-be-smart-every-day side, and the FY2018-FY2019 losses were execution losses (*"unfavorable product mix and production inefficiencies of 8.1%"*, FY2019). **No leverage** (term loan repaid in H1 2026; cash $12.1M and no borrowings at 2026-06-30, 10-Q) and **no control purchase**. Had Q3 opened it would have been a binary gate on [E3-38] alone. Not declared, because the gate is not opened.

- **[E4-29] FIRES, in the releases and the decks, not in the 10-K.** The Q2 2026 release (8-K `0001026655-26-000049`, EX-99.1) puts *"Adjusted EBITDA 1 of $7.6 million, or 12.2% of net revenues"* among its highlights beside operating income of 3.7%; the investor decks headline *"Adjusted EBITDA 2025 $30.7M"* against 2025 operating income of $14.2M and capital spending of $17.3M, and describe the Volvo roof award as *"Adjusted EBITDA accretive in the first full year"*. The credit amendment of 2026-07-02 adds EBITDA add-backs for the Mexico relocation and the executive retirements. The 10-K reports GAAP operating income and cash flow.
- **[E4-22]'s third flag FIRES: numeric targets and guidance, with an outturn record [E3-48].** Three-to-five-year targets in every deck from August 2025 to June 2026: *"Revenues >$500M"*, *"Operating Income 8%-10%"*, *"Return on Capital Employed 14%-16%"*, against FY2025 revenue of $273.8M and an operating margin of 5.2% (the June 2026 deck drops the earlier qualifier *"Goal timing may be impacted due to return to pre-pandemic demand levels"*). Annual revenue guidance in the 10-K against outturn: for 2023 *"flat to slightly higher than 2022"*, actual −5.2%; for 2024 *"decrease by approximately 10 to 15 percent"*, actual −15.5%; for 2025 *"flat for the full year 2025 as compared to 2024"*, actual −9.5% (with $41.6M of tooling inside it); for 2026 *"increase by approximately 0 to 5 percent"*, with H1 2026 revenue of $121.3M against $140.7M in H1 2025 (10-Q). Three misses, all on the downside, the last two outside the stated range.
- **[E4-27], what pay vests on (DEF 14A of 2026-04-06, `0001026655-26-000019`):** the annual incentive on *"achieving earnings before interest and taxes ("EBIT") and cash flows from operations targets"* (2025 payout *"0% of targeted amounts"*: EBIT *"underachieved ... by $6.8 million or 31%"*; 2024: 61%); half of the long-term restricted stock vests on *"Earnings Before Interest and Tax as a percent of sales and Return on Capital Employed targets"*, ROCE defined as *"EBIT divided by the sum of Total Stockholders' Equity plus total long-term debt"*, the other half on time. **Pay is not on EBITDA, and it charges capital** (the ROCE leg); the new CEO's agreement (8-K 2026-06-05) adds a 20,000-share time-vested initial grant and a long-term incentive target of 200% of salary. The former CEO is paid $50,000 a month as an adviser from 2026-06-01 to 2027-12-31 (8-K 2026-05-19), about $1.0M in all.
- **[E2-26], candor, and five disclosure slips in thirteen months of 8-Ks** (listed at Step 0: the margin range stated two ways in one filing, a wrong issue date for the release, *"$10,00,000"*, a par value of *"$1.00"* against the charter's $0.01, and a retirement announcement dated to the wrong year). None is an accounting matter; together they are a prompt about care in the documents a holder reads. Against that, the 10-K is plain: it states in its own risk factors that OEMs *"demand and receive price reductions"*, that fixed-price contracts may not recover cost increases, and that the Volvo programmes are leaving, and it bridges the gross margin every year in points.
- **Capital allocation, [E5-08], with the humility clause [E4-13].** Condition (1): cash $12.1M, no borrowings, a $50M revolver and a $50M delayed-draw term facility to 2031, against 2026 capital spending of $25-30M. Condition (2), against the computation below ($6-18 a share at the ~10% floor, $11-33 at the sovereign, over every window): the 2024 purchases (172,043 shares at an average *"$ 17.09"*), the 2025 purchases (201,999 at *"$ 15.71"*) and the H1 2026 purchases (24,545 at $18.62) sit inside the sovereign range and at or above the top of the floor range. Management knows the business better than this file does [E4-13]. The 2007 purchase of 3,600,000 shares from Navistar ($26.2M) is recorded, not analysed. No serial issuance [E5-15]: shares outstanding (balance-sheet basis) 8,614,395 at 2024-12-31 and 8,563,299 at 2026-06-30.
- **Honesty.** No Item 4.02 in the 8-K index back to 1996 (Step 0); the one 10-K/A corrected an auditor's consent. Item 3 (FY2025): *"The Company is not aware of any material pending legal proceedings"*. The FY2025 audit of internal control (Crowe LLP) is unqualified; no identified material weakness found by text search of the 10-Ks FY2006-FY2025 (the phrase appears only in generic risk language and audit-scope boilerplate). **No finding of personal misconduct in any document read** [E5-16]; [E5-17]'s cap applies.

### Q4 prompts: owner earnings the corpus's way [E2-23], every window [E4-25]

**Construction.** Operating cash flow as filed, less share-based compensation, less (c). Each year from the latest filed 10-K Consolidated Statement of Cash Flows showing it (FY2008 10-K for 2006, FY2009 for 2007-2008, FY2010 for 2009, FY2011 for 2010, FY2012 for 2011, FY2014 for 2012, then the 10-K two years later for each year to 2023, FY2025 for 2024-2025), parsed by `cfparse.py` and `oe_build.py` (`cf_parsed.json`), assembled by `oe.py` (`oe_out.txt`). **No net-income proxy anywhere** (operator rule 5). **The span is FY2006-FY2025, twenty years**: FY2005 is excluded because stock compensation was not expensed that year (the FY2007 10-K statement shows *"Share-based compensation"* of 268,274, 338,888 and 0 for 2007, 2006 and 2005), so SBC does not resolve before 2006.

- **SBC resolves every year and is complete, as far as the filings show.** *"Share-based compensation"* is a line in every cash-flow statement read, FY2006-FY2025 and the 10-Q; it is 7.4% of operating cash over twenty years, so [E3-70]'s grant-value measure would not move the range materially. The defined-contribution plans are an expense line of $1.7-1.9M a year (FY2023-FY2025, post-retirement note) with no statement in the 10-K that the match is paid in company stock and no plan issuance in the equity statement; the multi-employer plan is paid per hour worked. The former CEO's awards were reclassified to a liability and *"marked to market at each reporting period"* (10-Q), inside the same expense. [E5-06]: subtracted in full.
- **No non-controlling interests and no equity-method investees** (none in the FY2025 balance sheet or income statement). [E3-04] does not arise.
- **(c), both ends, a disclosed judgment [E2-09].** Capital spending was 1.26 times depreciation over the twenty years (2.08 in FY2006-FY2010, 1.75 in FY2011-FY2015, 0.63 in FY2016-FY2020, 1.22 in FY2021-FY2025). Management's own split in the June 2026 deck puts *"Sustaining Capex"* at $6.1M, $9.0M and $10.8M in 2023-2025 against depreciation of $11.2-11.7M, and *"Projected sustaining capital spend in 2026 of $7-10M"*: management says maintenance runs at or below depreciation; that split is the company's, not an audited figure, and is not used as a third end. Nothing in the 10-K says depreciation understates renewal, so this is not [E5-20]'s class on the filings, and D&A is the corpus default [E3-44, E2-41]; both ends are displayed. **The D&A end takes out acquired-intangible amortisation** (Horizon Plastics customer relationships, trademarks and technology: *"$ 951,000 , $ 1,587,000 and $ 1,602,000 of amortization expense"* in 2025-2023, $1.9M a year in 2018-2022, from the tag for earlier years, equal to the filed note where checked); the filed statement carries one *"Depreciation and amortization"* line. **The capex end is total purchases of property, plant and equipment** as filed; acquisitions (CPI Binani $14.5M in 2015, Horizon Plastics $63.0M in 2018, Cincinnati Fiberglass $0.7M in 2005) are not in (c).
- **Working capital.** Inside operating cash, as [E2-23]'s parenthetical requires where the business needs it. The last column strips the five current lines (receivables, inventories, prepaid, payables, accrued) so the swings can be seen: FY2019's $18.3M release as sales fell and FY2018's $13.3M build after Horizon are the large ones.

**By year ($M, `oe_out.txt`):**

| FY | OCF | SBC | D&A as filed | acquired-intangible amortisation | depreciation | capex | five WC lines | OE, D&A end | OE, capex end | OE, capex end, WC stripped |
|---|---|---|---|---|---|---|---|---|---|---|
| 2006 | 16.91 | 0.34 | 2.72 | | 2.72 | 9.23 | +0.77 | 13.85 | 7.34 | 6.57 |
| 2007 | 11.95 | 0.27 | 3.41 | | 3.41 | 2.74 | +2.56 | 8.27 | 8.94 | 6.38 |
| 2008 | 7.16 | 0.29 | 3.54 | | 3.54 | 12.10 | −3.95 | 3.32 | **−5.23** | −1.28 |
| 2009 | 8.23 | 0.33 | 3.86 | | 3.86 | 10.07 | +1.24 | 4.04 | **−2.16** | −3.41 |
| 2010 | 7.37 | 0.35 | 3.95 | | 3.95 | 2.23 | −0.36 | 3.07 | 4.79 | 5.15 |
| 2011 | 11.47 | 0.38 | 3.94 | | 3.94 | 8.81 | −3.92 | 7.15 | 2.29 | 6.21 |
| 2012 | 14.80 | 0.41 | 4.52 | | 4.52 | 8.26 | +3.62 | 9.87 | 6.13 | 2.51 |
| 2013 | 6.92 | 0.41 | 4.88 | | 4.88 | 9.33 | −5.83 | 1.63 | **−2.83** | 3.00 |
| 2014 | 10.83 | 0.74 | 5.02 | | 5.02 | 10.68 | −4.42 | 5.06 | **−0.60** | 3.83 |
| 2015 | 18.61 | 0.79 | 6.04 | 0.04 | 6.00 | 5.68 | −2.59 | 11.83 | 12.15 | 14.74 |
| 2016 | 26.07 | 1.00 | 6.28 | 0.05 | 6.23 | 2.86 | +10.74 | 18.83 | 22.20 | 11.46 |
| 2017 | 6.91 | 1.33 | 6.24 | 0.05 | 6.19 | 4.26 | −5.15 | **−0.61** | 1.32 | 6.47 |
| 2018 | −6.53 | 1.74 | 9.38 | 1.87 | 7.51 | 5.80 | −13.31 | **−15.79** | **−14.07** | −0.76 |
| 2019 | 16.70 | 1.56 | 10.38 | 1.95 | 8.43 | 7.46 | +18.29 | 6.71 | 7.68 | −10.61 |
| 2020 | 28.16 | 1.35 | 11.66 | 1.95 | 9.71 | 3.68 | +5.91 | 17.09 | 23.13 | 17.21 |
| 2021 | 12.55 | 1.89 | 11.62 | 1.95 | 9.67 | 11.57 | −5.46 | 0.99 | **−0.91** | 4.55 |
| 2022 | 18.98 | 2.33 | 11.88 | 1.95 | 9.94 | 16.59 | −4.88 | 6.72 | 0.07 | 4.95 |
| 2023 | 34.84 | 2.92 | 12.91 | 1.60 | 11.31 | 9.10 | −2.83 | 20.61 | 22.82 | 25.65 |
| 2024 | 35.15 | 2.50 | 13.40 | 1.59 | 11.81 | 11.53 | +5.15 | 20.84 | 21.13 | 15.98 |
| 2025 | 19.18 | 1.79 | 12.35 | 0.95 | 11.40 | 17.27 | −4.74 | 6.00 | 0.13 | 4.87 |
| TTM to 2026-06-30 | 16.66 | 1.66 | 12.19 | | | 24.96 | | 2.81 (on D&A as filed) | **−9.96** | |

*(Figures cross-checked: FY2025 OCF 19,185, SBC 1,788, D&A 12,348, capex 17,268 in the filed FY2025 statement; OCF, SBC and capex equal the tags (Step 0); amortisation 951 equals the filed note. **Restated once**: 2010 operating cash $7,366,931 (FY2010 10-K) against $7,368,000 (FY2011 10-K), rounding. TTM is FY2025 plus H1 2026 less H1 2025 from the 10-Q `0001026655-26-000053`; H1 2026 capex was $12.1M, of which *"$9.6 million related to the Company's Mexico expansion project"* (release).)*

**Every window ending FY2025, on the Step 0 cap of $205.4M, against the 5.49% sovereign:**

| window | capex end | D&A end | yield, capex end | yield, D&A end | capex end, WC stripped |
|---|---|---|---|---|---|
| **3y FY2023-25** | **$14.69M** | **$15.82M** | **7.15%** | **7.70%** | $15.50M |
| 4y FY2022-25 | $11.04M | $13.54M | 5.37% | 6.59% | $12.86M |
| **5y FY2021-25 (the corpus's default window [E2-42])** | **$8.65M** | $11.03M | **4.21%** | 5.37% | $11.20M |
| 6y FY2020-25 | $11.06M | $12.04M | 5.38% | 5.86% | $12.20M |
| 7y FY2019-25 | $10.58M | $11.28M | 5.15% | 5.49% | $8.94M |
| 8y FY2018-25 | $7.50M | $7.90M | 3.65% | 3.85% | $7.73M |
| 9y FY2017-25 | $6.81M | $6.95M | 3.32% | 3.38% | $7.59M |
| **10y FY2016-25** | **$8.35M** | $8.14M | **4.06%** | 3.96% | $7.98M |
| 11y FY2015-25 | $8.69M | $8.48M | 4.23% | 4.13% | $8.59M |
| 12y FY2014-25 | $7.92M | $8.19M | 3.86% | 3.99% | $8.20M |
| 13y FY2013-25 | $7.09M | $7.69M | 3.45% | 3.74% | $7.80M |
| 14y FY2012-25 | $7.02M | $7.84M | 3.42% | 3.82% | $7.42M |
| 15y FY2011-25 | $6.71M | $7.80M | 3.27% | 3.80% | $7.34M |
| 16y FY2010-25 | $6.59M | $7.50M | 3.21% | 3.65% | $7.20M |
| 17y FY2009-25 | $6.07M | $7.30M | 2.96% | 3.55% | $6.58M |
| **18y FY2008-25** | **$5.45M** | $7.08M | **2.65%** | 3.45% | $6.14M |
| 19y FY2007-25 | $5.63M | $7.14M | 2.74% | 3.48% | $6.15M |
| **20y FY2006-25 (the longest the filings allow with SBC resolved)** | **$5.72M** | $7.47M | **2.78%** | 3.64% | $6.17M |

**Combined range across every window 3-20 years and both ends: $5.45M to $15.82M (2.65% to 7.70% on the cap).** Above the 5.49% sovereign: the three-year window at both ends, and the four- and six-year windows at the D&A end (the seven-year D&A end equals it). **Every window of eight years or more, and the five-year window at the capex end, sits below the sovereign.** The spread between the three-year top and the eighteen-year bottom is nearly threefold, and **it is two years, not noise [E4-25, E5-11]**: FY2023 and FY2024 ($22.8M and $21.1M on the capex end) are 101.7% of the five-year capex-end total and 38.4% of the twenty-year total; the screen's `best_year_dep_oe` 0.678 saw part of this. **The bottom sits at or below zero in nine of twenty years on the capex end**: below zero in FY2008 (−$5.2M), FY2009 (−$2.2M), FY2013 (−$2.8M), FY2014 (−$0.6M), FY2018 (**−$14.1M**, the screen's figure) and FY2021 (−$0.9M), and within $1.4M of zero in FY2017, FY2022 and FY2025; **the trailing twelve months to 2026-06-30 are −$10.0M** on the capex end, as the Mexico expansion is paid for. Stripping working capital does not rescue the thin years (FY2008, FY2009, FY2018 and FY2019 stay at or below zero): they are years in which the business, not its balance sheet, produced no owner cash. **[E4-41]**: the favourable break in the window is FY2023-FY2024, a truck-cycle peak with the gross-margin repair and a working-capital release; the three-year window rests on it.

**Great, good or gruesome [E4-20], as it would be scored:** closer to the gruesome account than the good one. Sales grew from $162.3M (FY2006) to $273.8M (FY2025) with two acquisitions ($77.5M) and capital spending of $169.2M against depreciation of $134.0M ($148.0M of D&A as filed) over the twenty years, and owner earnings averaged $5.7-7.5M a year across them, on equity that rose from about $30M (FY2009) to $158.2M (FY2025).

**Staying power, as it would be scored [E5-11]:** (1) the stream is neither large nor reliable (nine thin or negative years in twenty); (2) liquid assets $12.1M at 2026-06-30 (from $38.1M at 2025-12-31, after repaying the $19.8M term loan and H1 capex); (3) **near-term cash requirements: 2026 capex of $25-30M against H1 operating cash of $7.1M**, funded, if needed, by the $50M delayed-draw term facility (8-K 2026-07-07). No borrowings at 2026-06-30; the new facility carries a fixed-charge-coverage covenant revised *"by deducting Consolidated Unfunded Capital Expenditures from the numerator thereof"* ([E2-54]'s capex-first coverage test, written by the lender).

**Named death, as a signature only (Q4 was not reached): #11 THE PASS-THROUGH, in its re-tendered-programme form** (GFF's *"a re-tendered Home Depot exclusive"*, on the survival-shapes index): the supplier invests in presses and plants for a programme whose price the OEM fixes and then takes down (*"demand and receive price reductions"*), and at the next award the programme is re-bid or moves (Volvo). The cyclical feature is the fixed-cost cycle at low utilisation: at FY2019's 7.6% gross margin on FY2025 sales, gross margin would be about $20.8M against FY2025 SG&A of $33.4M, an operating loss of about $12.6M (the business lost $11.5M in FY2019 on $284.3M of sales). Not entered in the index's instances column; no new shape.

**COMPUTATION — NOT A CLEARANCE** (no box, no entry language; the file closed at Q2): capitalising the $5.45-15.82M range with no growth gives about $55-158M at the ~10% floor rate [E4-28] and about $99-288M at the 5.49% sovereign; per share on 8,849,034, **about $6-18 at the floor and about $11-33 at the sovereign**, against a price of $23.21. To reach the ~10% floor at today's price, the owner earnings would need about 2.3 to 7.4 points of perpetual growth. Net cash of about $12.1M (no borrowings at 2026-06-30) moves the enterprise figures by about 6% and changes none of this. Windage: ONE (the range itself; no margin, no premium).

### Q6 prompts: what would reverse the Q2 verdict (in words; no alert, no portfolio row)
- The Item 1A sentences withdrawn with evidence: OEMs no longer *"demand and receive price reductions"*, or the company shown to set price at re-award rather than accept it.
- Programmes renewed without re-bid over several cycles, with the renewal price above the prior price, filed in the major-customer or revenue notes.
- An operating margin sustained above the twenty-two-year range (above about 12%) through a truck downturn, with press utilisation below 60%.
- A filed peer (a moulder the registrant names) whose margins show the trade earns franchise returns, which this file could not test.
- Monitoring metric if ever reopened: large-compression-press utilisation and product sales by customer (Item 1 and Note 4), not the adjusted-EBITDA line [E4-55].
