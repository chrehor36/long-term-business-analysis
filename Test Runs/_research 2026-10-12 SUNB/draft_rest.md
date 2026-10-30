## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED.** The file closed at Q2 (TOO HARD, NATURE). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** The balance sheets were read in Step 0's last subsection, as the template asks when the file closes before Q4; facts on the accounts are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.** Integrity facts found are recorded under AFTER THE STOP, not judged; the box line carries the flag.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** Facts under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED as a question.** The figures below are the operator's two reporting figures (Part VII, The owner's price), computed after the STOP.

### COMPUTATION, NOT A CLEARANCE

Script and output: `q7_computation.py` and `q7_computation_output.txt` in the research folder. All $M unless a per-share figure. Discount rate 5.60% (UST 30-year, 10/09/2026); fair price at 10%.

**The window and its sources.** FY2022 (IFRS, AR2022) to FY2026 (US GAAP, 10-K). FY2022 is bridged to US GAAP by deducting the IFRS 16 lease principal ($107.6M, financing in IFRS) from free cash flow, by taking the lease interest ($80.7M) out of the interest added back, and, for the maintenance series, by deducting the lease interest from IFRS operating profit and the right-of-use depreciation ($154.1M) from IFRS depreciation (AR2022, cash flow statement, Note 6, Note 14).

**Owner cash, all spending deducted (the PG specific), literal window:**

| | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | average |
|---|---|---|---|---|---|---|
| free cash flow as filed (company definition; FY2022 Ashtead's) | 1,125 | 441 | 126 | 1,675 | 2,055 | |
| less lease principal (FY2022), stock pay (cash-flow add-back), finance-lease principal, intangibles and other investing | 970 | 328 | -22 | 1,651 | 1,951 | 976 |
| less acquisitions and contingent consideration, net of disposals | -308 | -755 | -898 | 1,504 | 1,761 | 261 |
| all-equity (plus debt interest paid after the company's tax) | -168 | -572 | -604 | 1,816 | 2,032 | 501 |

The series changes sign, so by specific (b) the growth is measured between the halves of the window, which is also meaningless here (negative first half), and this series gives the no-growth case alone: $501M a year all-equity, worth $8,943M at 5.60%, **$0.17 a share** after net debt. Beside it, before acquisitions (the organic pair; the filer reports no organic growth rate for the whole): $1,215M a year, **$31.31 a share** at no growth.

**The central case, maintenance only (specific e).** The filing allows the maintenance guess two ways: the depreciation charge, which **[M1998-127]** calls "not inappropriate in most companies to use as a proxy for required capital expenditures", and the filer's own statement: "Our current rental fleet has an original equipment cost of c. $19bn with a seven- to eight-year replacement cycle. Thus, on average, we replace $2.4bn per year (using eight years)" (AR2025, climate-related disclosures, printed page 71); less used-equipment proceeds of $0.42B to $0.83B a year (FY2022 to FY2026 cash flows), that is $1.6B to $2.0B of net rental replacement, against a rental depreciation charge of $1,851M in FY2026. I take depreciation as the maintenance proxy and say that it is low: the fleet is depreciated at historical cost while the 10-K names "life cycle inflation", so a shortfall exists that I do not quantify **[L2015-004]**. Maintenance-only owner cash = (operating income + amortization of acquired intangibles) x (1 - the company's own tax rate that year); stock pay and the FY2026 restructuring costs ($134M, which the filer calls non-recurring) stay in as real costs.

| | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | average |
|---|---|---|---|---|---|---|
| maintenance-only owner cash, all-equity (M) | 1,482 | 1,912 | 1,976 | 1,960 | 1,688 | **1,804** |
| growth spending G = net capital spending above depreciation + acquisitions + working-capital increase | 1,877 | 2,662 | 2,688 | 170 | -218 | **1,436** |
| equity-only (M less debt interest after tax) | 1,342 | 1,730 | 1,682 | 1,648 | 1,417 | 1,564 |

Growth shown in M: 3.31% a year, FY2022 to FY2026 end to end (2.43% between the halves); revenue grew 8.79% a year over the same span, most of it bought (G averaged $1,436M a year, $7.2B over five years, against an increase in M of $206M). By specific (e) the growth spending is charged against the growth it buys; the growth bought here is worth less than its cost, so **the no-growth maintenance-only case is the top of the range and the growth case the bottom**, the inversion the convention names: "growth can destroy value" **[L2000-023]**. (f) The cap: 3.31% is below the discount rate and implies no share of sales above anything the filings show; no cut. (a) The cycle base: no end year of the window is called aberrational by the filer; the FY2026 harvest of cash (capital spending cut, fleet age 49 to 53 months) is the countercyclical pattern the filer describes as normal, and it is inside the all-spending series, not the maintenance series; the literal window stands. (c) Deals: the $667M of acquisitions paid in the quarter to 2026-07-31 and the $56M closed after it are in today's net debt and credited at nothing (no filed earnings). The UK part (2% of segment profit) is inside M at no extra growth; separating it moves nothing material.

**Net debt (all-equity basis).** Debt at 2026-07-31 $8,556M (10-Q balance sheet: $550M current plus $8,006M long-term) + finance-lease liabilities $171M (latest stated, 2026-04-30, 10-K XBRL; not restated in the 10-Q) - cash $32M + acquisitions closed after the quarter $56M + the dividend declared 2026-09-09 ($0.30 x 409.76M = $123M) = **$8,874M**. Operating leases ($2,867M at 2026-07-31) are left out, as the convention says, and said so. The $550M notes repaid on 2026-08-12 were refinanced inside the July issues and do not change net debt.

**(a) THE VALUE RANGE (a reporting figure; COMPUTATION):**
- **All-equity, central: $49.42 to $56.94 a share** (whole-business value $29,124M to $32,207M less $8,874M), against **$75.17**. Bottom = the growth case (M grown at 3.31% for ten years with growth spending of $1,436M a year charged, then flat with the spending stopped); top = the maintenance-only no-growth case.
- Equity-only beside: $57.48 to $68.14 a share (owner cash after interest; it is higher because the after-tax cost of the debt, about 4%, is below the 5.60% rate; it does not decide).
- The literal all-spending window beside: $0.17 a share (acquisitions deducted, no-growth alone by specific b); $31.31 (before acquisitions).
- Width: top over bottom 1.15, far inside three to one.

**The floor, tested first:** at $75.17 (whole-business value at the price $39,676M) the expected return is 4.55% on the no-growth case, 4.46% on the growth case, and 5.89% even if the shown growth is credited with no growth spending charged at all. **No case earns about ten percent** **[M2003-149]**; had Q7 been reached it would have closed OUT on price, and the price is above the top of every central range.

**(b) THE FAIR PRICE (a reporting figure, never a verdict; Part VII; COMPUTATION):** each end case valued at ten percent, the two averaged, after the company's own tax:
- **All-equity, central: $15.33 a share** (no-growth end $22.36, growth end $8.30, each after $8,874M of net debt).
- **Equity-only beside: $30.39 a share** (no-growth end $38.16, growth end $22.62).

The tax treatment: the company's own book tax rate each year (25.0% to 26.4%); cash taxes have run lower (FY2026 $332M paid against a $476M provision) because of accelerated tax depreciation on a growing fleet, a deferral that lasts while the fleet grows; no carryforward or credit runs out inside ten years that I found, so no shelter is priced separately.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** (Nothing found in the filings that touches the named businesses.)

---
## THE BOX
**TOO HARD (NATURE), decided at Q2**: General Tool, the deciding part, holds a shared scale position in an undifferentiated, price-led field whose returns were ordinary through the last full construction cycle; the better returns since FY2011 are not credited until a full cycle in which the field's price holds. **Re-look condition:** the first fiscal year in which the business's volume or its field's volume falls, read from the filings (here: the first fiscal year after FY2026 in which Sunbelt's North American equipment-rental revenue at constant currency, or United Rentals' or the industry's North American rental revenue, falls), after which Q2 is put again. **Integrity facts recorded, not judged** (see AFTER THE STOP, Q5 and Q6). For the operator, COMPUTATION, NOT A CLEARANCE: value range $49.42 to $56.94 a share (all-equity; equity-only $57.48 to $68.14) against $75.17; fair price $15.33 (equity-only $30.39); no case earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; the box unchanged (operator rule 2).

**Q3 (capital).**
- Capital spending on the fleet: rental additions $3,624M (FY2024), $1,946M (FY2025), $2,023M (FY2026); total additions $4,311M, $2,402M (AR2025 Table 02; 10-K Item 1). The filer's split (replacement = original cost of equipment sold): FY2022 $829.7M replacement, $935.7M growth (cash); FY2023 $1,380.8M and $1,638.8M; FY2024 $2,121.0M and $1,638.2M; FY2025 $1,323.1M and $622.8M (additions) (AR2022, AR2023, AR2024, AR2025 financial reviews).
- Five years of growth spending ($7.2B by this run's construction, including $3.5B of acquisitions) raised maintenance-only owner cash from $1,482M to $1,688M (q7 computation); revenue +40% over the same four years.
- Free cash flow (company definition) $126M in FY2024 against $2,055M in FY2026: "our cash flows are countercyclical" (10-K Item 7).
- The filer's RoI (pre-tax, goodwill included) 14.5% in FY2025, down from 19.2% in FY2023; segment RoI excluding goodwill FY2025: General Tool 20%, Specialty 30%, UK 7% (AR2025 glossary).

**Q4 (the accounts).**
- The company features "adjusted operating profit" and "adjusted EBITDA" (10-K Item 7, Non-GAAP Financial Measures) and calls EBITDA useful because it helps investors understand "ongoing cash earnings, from which capital investments are made and debt is serviced"; the adjusted figures exclude stock pay and restructuring.
- A material weakness was found after the half-year to 2025-10-31 (the $550M 1.500% notes due August 2026 classified non-current), the Form 10 half-year restated, and the weakness declared remediated at 2026-04-30; the company is not yet required to report on internal control under Section 404 (10-K Item 1A and Item 9A; 8-K of 2026-03-02).
- The stock-pay note corrects a prior figure: the weighted-average fair value of awards outstanding at 2025-04-30 "revised [...] from $44.41 to $60.97" (10-K stock-based compensation note).
- Stock pay swings with the share price because many awards were liability-classified: $92M (FY2024), -$9M (FY2025), $80M (FY2026) in the cash-flow add-back; $61M of awards reclassified from liability to equity in FY2026 (10-K statement of equity).
- Receivables rose 13% in FY2026 ($1,481M to $1,669M) against revenue +3%; the receivable provision charge rose from $28M to $64M (10-K cash flow statement); at 2026-07-31 receivables were $1,929M.
- Deferred tax liabilities $2,001M (FY2023) to $2,394M (FY2026) and $2,463M (2026-07-31); cash taxes paid $332M against a $476M provision in FY2026.
- UK goodwill: the fair value of the UK reporting unit "was not substantially in excess of its carrying value" (10-K Item 7, Critical Accounting Policies).

**Q5 (integrity facts, recorded, not judged).**
- Guidance: the company issues full-year guidance (IR site headline of the Q1 FY2027 release, "raises full-year fiscal 2027 guidance", read only as a headline) and its 10-K lists "our failure to meet our stated guidance" among share-price risks. **[L2019-006]**, **[L2002-041]** bear on this at Q5 if a later run reaches it.
- The adjusted figures featured (Q4 above) **[L2016-006]**.
- At the US listing, outstanding performance share units, including those granted in fiscal 2026, had their performance conditions removed and "deemed to have been met at 85.5% of maximum" (DEF 14A, Compensation Discussion and Analysis), in a year in which net income fell 15%.
- The CEO's total reported pay rose from $12.1M (FY2025) to $14.6M (FY2026), including non-equity incentive pay of $2.2M against $1.4M, while operating income fell 13% (DEF 14A, 2026 Summary Compensation Table).
- The material weakness and the stock-pay correction (Q4 above).
- On the other side: the CEO has been with the business since 1996 and has run it since 2019; other executive officers average about 20 years with the group (10-K Item 1).

**Q6 (the money and the owners).**
- Buybacks: $1,413M in FY2026 (the program launched December 2024, completed in FY2026), an average of roughly $69 a share by the change in shares outstanding (430.7M to 410.3M; an estimate that ignores issuance); $1.5B new program from 2026-03-02, $315M spent by 2026-07-31, at $76.08 (May 2026) and $79.84 (June 2026) a share (10-Q Item 2). No price limit is stated. Against this run's computed range bottom ($49.42, all-equity), every price paid that I found is above it (the Q6 test of Part A, recorded here because Q7 is a computation).
- Dividends: $1.10 a share paid in FY2026; $0.75 declared in the quarter to 2026-07-31 and $0.30 a quarter from September 2026 (10-Q).
- Acquisitions: $1,277M (FY2022), $1,061M, $846M, $134M, $206M, then $667M in the quarter to 2026-07-31 and $56M after it (cash flow statements; 10-Q Note 15); all in cash, none in stock found. The Redomiciliation exchanged shares one for one; no stock-paid deal found.
- Pay: PSUs on relative TSR, compound adjusted EPS growth and adjusted RoI (DEF 14A); see Q5 for the waiver at listing.

**Q9 (debt and exposures).**
- Debt $8,556M at 2026-07-31, 81% fixed at 2026-04-30; senior notes maturing from 2027 to 2036; the ABL ($4,750M committed to November 2029) had $3,302M available at 2026-04-30; the company "was in compliance with all debt covenants that were in effect" (10-K Item 7). Net debt to EBITDA about 1.7x at 2026-04-30 (7,554 / 4,497), near 1.9x after the July acquisitions.
- Operating leases $2,867M (2026-07-31) on top.
- The 10-K's own risk factor: "Our substantial debt could adversely affect our financial health."
- Insurance: significant deductibles and self-insured retentions; no company-wide first-party environmental cover (10-K Item 1A).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). Commits: Step 0 (7ef6ab21), Q1 (9a6d9bfe), Q2 (c63522ec), then the computation and close.
- [x] If dispatched to an analyst: the brief allowed the per-question commits; the lock is the dispatching session's (not checked by me, as the brief does not ask me to); the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. One filtered listing of `Test Runs/` for the company's names was made before any fetch, to confirm the run file name was free; it returned nothing (declared under contamination at the top).
- [x] Every v5 id resolves (`check_cites.py`, run before each commit); every filing fact has its accession or, for the Ashtead annual reports, its document and page; no number without a row or a filing, and the run's own constructions are labelled.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; everything after it is NOT REACHED or headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operating income after depreciation, stock pay and restructuring, after tax; and free cash flow less stock pay, leases and acquisitions); the sovereign from the US Treasury; the price from an aggregator, flagged.
- [x] Contrary evidence was written down as it was found (foundations list, Q2 tests); the facts found for later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used (it printed only that it found no tagged history).
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The re-look condition of Q2's change-for-the-better convention was already met before this run.** The convention credits a change for the better "only on the evidence of a full cycle in which the price behaviour held" and fixes the re-look as "the first fiscal year in which the business's volume or its field's volume falls". For SUNB that year exists in the past: FY2021 (pandemic), US rental revenue -2%, the filer's dollar utilization held (51% to 50%) while United Rentals' fleet productivity fell 6.9%. The text does not say whether a past volume-falling year inside the improved era counts as the full cycle, or whether "full cycle" must be a downturn of the kind that broke the price before (here the construction-led 2009 to 2011). I weighed FY2021 as inconclusive (a one-year shock, the field's evidence mixed) and kept the box at TOO HARD (NATURE); another analyst could read FY2020 to FY2024 as a full peak-to-peak cycle in which the filer's price held, credit the change, and pass Q2, after which the file would close OUT at Q7 on price (no case earns the floor at $75.17). The box differs; the operator's figures do not. A sentence saying whether the re-look event must be a downturn in the field's volume of a stated depth, or simply any fall, would settle it. (2) **"The field's returns" has no measure.** The filer's RoI, United Rentals' and Herc's figures are defined differently; I built one plain measure (operating income on debt plus equity less cash) and labelled it a CONVENTION of this run. (3) **Specific (e)'s maintenance guess** does not say which of two filer-given guesses to use when they differ (depreciation, and "replacement = original cost of equipment sold", which the filer itself uses and which understates replacement when the fleet is aging); I used depreciation, which the row names, and said it is low under inflation. (4) **Specific (b) and (e) together**: the all-spending series changes sign (the investment years FY2023 and FY2024), so (b) reduces it to a no-growth case alone ($0.17 a share), while (e) makes the maintenance case central; the text could say that (b) applies to the beside-figure only when (e) applies. (5) **The template's Q5 wording** asks for integrity applied on doubt alone; a file closed at Q2 records integrity facts without judging them, and the facts here (performance conditions waived at listing, pay up as profit fell, guidance) are of the kind a later run must answer first.
