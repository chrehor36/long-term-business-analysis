# BAM competitor row: peer data from FY2025 10-Ks

DATA ONLY. No verdicts, no conclusions. Gathered 2026-09-13 for the BAM run's Q2 competitor row.

**Method.** Each 10-K primary document fetched from EDGAR (User-Agent per `tools/sources.py` SEC_UA, 0.4s throttle), converted HTML to text with the `totext` helper, saved as `<TICKER>_10K_FY2025.txt` in this folder. Figures transcribed from those text files by keyword search (`kwic.py`); arithmetic in `calc.py` (re-runnable). All nine peers filed a FY2025 10-K (period ending 2025-12-31) in Feb 2026, so no substitute annual report was needed.

**Location convention.** The HTML-to-text conversion does not preserve page numbers reliably, so each figure is located by its Item and its table or caption title as filed. Quotes are verbatim from the text files, including curly apostrophes. Page-break artifacts inside a quote are flagged in square brackets and never smoothed.

**Units.** Each filer's own unit is kept: BX, KKR, ARES, OWL and TPG report in thousands of dollars ($000); APO, CG, BLK and TROW report in millions ($m); AUM tables vary and are labelled per line.

**Computed figures** are marked COMPUTED, with the arithmetic shown.

**Caution on the GAAP fee line.** Firms that consolidate funds or an insurer eliminate some management fees in GAAP. KKR and APO show this most: their GAAP management-fee lines are far below their segment lines, because Global Atlantic and Athene fees and consolidated-fund fees are eliminated. Where the segment line differs from GAAP, both are given, and the fee rate is computed on both.

---

## 1. Blackstone Inc. (BX), CIK 1393818

**1. Filing.** Form 10-K for FY ended 2025-12-31. Accession **0001193125-26-082531**, filed **2026-02-27**, primary document `d48618d10k.htm`.

**2. GAAP management fee line.** "Management and Advisory Fees, Net". Item 8, Consolidated Statements of Operations, and Item 7, Consolidated Results of Operations table ($000):
- FY2025: 8,075,601
- FY2024: 7,188,936
- FY2023: 6,671,260

Segment "Base Management Fees", Total Segments ($000): 7,548,857 (2025), 6,780,882 (2024), 6,465,847 (2023). Segment "Total Management and Advisory Fees, Net": 8,016,049 (2025), 7,133,534 (2024), 6,663,244 (2023).

**3. FEAUM equivalent.** "Fee-Earning Assets Under Management", "Balance, End of Period", Total. Item 7, Fee-Earning Assets Under Management roll-forward tables ($000):
- YE2023: 762,607,902
- YE2024: 830,708,603
- YE2025: 921,674,454

MD&A text: "Fee-Earning Assets Under Management were $921.7 billion at December 31, 2025, an increase of $91.0 billion compared to $830.7 billion at December 31, 2024."

Total Assets Under Management, YE2025: $1,274,931,234 thousand ("Balance, End of Period (e)", Total).

Firm's own fee-rate disclosure: "Annualized Base Management Fee Rate (f)", Total: 0.86% (2025), 0.85% (2024), 0.88% (2023). Footnote (f): "Annualized Base Management Fee Rate represents annualized year to date Base Management Fee divided by the average of the beginning of year and each quarter end’s Fee-Earning Assets Under Management in the reporting period."

**4. Perpetual share.** Item 7, "Perpetual Capital": "Perpetual Capital Total Assets Under Management were $523.6 billion as of December 31, 2025, an increase of $78.8 billion, compared to $444.8 billion as of December 31, 2024."
- No perpetual share of FEAUM or of management fees is stated in the text.
- COMPUTED share of Total AUM: 523.6 / 1,274.931 = **41.1%**.

**5. FRE.** Measure "Fee Related Earnings", Total Segments, Item 7, Segment Analysis ($000):
- FY2025: 5,737,537
- FY2024: 5,282,065

The 10-K does not label a single "fee related revenues" line. The FRE build is:
- 2025: "Total Management and Advisory Fees, Net" 8,016,049 + "Fee Related Performance Revenues" 1,825,428, less Fee Related Compensation (2,690,701) and Other Operating Expenses (1,413,239).
- 2024: 7,133,534 + 2,135,945.

COMPUTED FRE margin:
- FY2025: 5,737,537 / (8,016,049 + 1,825,428 = 9,841,477) = **58.3%**
- FY2024: 5,282,065 / 9,269,479 = 57.0%

**6. GAAP OCF.** "Net Cash Provided by Operating Activities", Item 8, Consolidated Statements of Cash Flows ($000):
- FY2023: 4,056,906
- FY2024: 3,481,662
- FY2025: 4,663,161

Consolidates Blackstone Funds: yes ("consolidated Blackstone Funds"). Operating activities include lines that carry fund-level flows:
- "Investments Purchased": (3,807,149) in 2025
- "Cash Proceeds from Sale of Investments": 6,679,186 in 2025
- "Cash Acquired with Consolidation of Fund Entities"
- "Cash Relinquished with Deconsolidation of Fund Entities": (69,477) in 2025

The statement does not show a separate consolidated-fund subtotal.

**7. Dividends.** "Dividends/Distributions to Stockholders and Unitholders", FY2025: (6,013,385) $000. This line includes distributions to Blackstone Holdings unitholders, not common stockholders alone.

**8. Quotes.**
1. Item 1, Business, "Competition": "In addition, competition for fundraising in the private wealth and insurance channels is also driven by the willingness of certain of our competitors to charge lower fees or pay higher or different types of distributors fees."
2. Item 1A, Risk Factors: "Although we have no obligation to modify any of our fees with respect to our existing funds, we may experience pressure to do so, including in response to regulatory focus by the SEC on the quantum and types of fees and expenses charged by private funds."
3. Item 1A, Risk Factors: "We have confronted and expect to continue to confront requests from a variety of investors and groups representing investors to decrease fees, which could result in a reduction in the fees and Performance Revenues we earn."

---

## 2. KKR & Co. Inc. (KKR), CIK 1404912

**1. Filing.** Accession **0001404912-26-000007**, filed **2026-02-27**, `kkr-20251231.htm`.

**2. GAAP management fee line.** "Management Fees". Item 8, Note 3 "REVENUES – ASSET MANAGEMENT AND STRATEGIC HOLDINGS" ($000):
- FY2025: 2,496,783
- FY2024: 1,994,089
- FY2023: 1,843,144

"Fee Credits" are a separate negative line: (712,433), (696,091), (297,936).

Segment line "Management Fees" (Item 7, Analysis of Asset Management Segment Operating Results, $000):
- FY2025: 4,100,841
- FY2024: 3,461,381
- FY2023: not in a segment table in this filing. The Item 1 business-line five-year tables give "Management Fees ($ in millions)" for 2023 of 1,286 (Private Equity), 826 (Real Assets) and 919 (Credit and Liquid Strategies). COMPUTED sum: 3,031 $m.

**3. FEAUM equivalent.** "Fee Paying Assets Under Management" (FPAUM), Item 7 summary table ($ millions):
- YE2023: not disclosed as a firm total in this filing. COMPUTED from the Item 1 "Select Key Metrics" FPAUM rows, which are rounded $bn: 108 + 112 + 226 = **446 $bn**.
- YE2024: 511,963
- YE2025: 604,144

"Assets Under Management", YE2025: $743,858 million.

**4. Perpetual share.** Item 1, Business: "As of December 31, 2025, approximately 92% of our AUM consists of capital that has a duration of at least eight years at inception or longer, including what we refer to as perpetual capital."
- This 92% is long-duration including perpetual. It is not a perpetual-only share.
- No perpetual-only dollar amount or share is stated in the text.

**5. FRE.** "Fee Related Earnings", asset management segment ($000):
- FY2025: 3,714,313
- FY2024: 3,267,796

The components are "Management Fees", "Transaction and Monitoring Fees, Net" and "Fee Related Performance Revenues", less "Fee Related Compensation" and "Other Operating Expenses". A "fee related revenues" subtotal is not printed.

COMPUTED fee related revenues:
- 2025: 4,100,841 + 1,092,577 + 181,784 = 5,375,202
- 2024: 3,461,381 + 1,165,884 + 137,992 = 4,765,257

COMPUTED FRE margin: **69.1%** (2025) and 68.6% (2024).

**6. GAAP OCF.** "Net Cash Provided (Used) by Operating Activities" ($000):
- FY2023: (1,493,812)
- FY2024: 6,649,878
- FY2025: 477,760

Includes Global Atlantic insurance lines (e.g. "Change in Policy Liabilities and Accruals, Net – Insurance") and consolidated investment funds. MD&A wording: "Because our consolidated investment funds are treated as investment companies for accounting purposes, certain of these cash flow amounts are included in our cash flows from operations." Operating lines include "Investments Purchased – Asset Management and Strategic Holdings" (42,904,105) and "Proceeds from Investments – Asset Management and Strategic Holdings" 33,698,163 in 2025.

**7. Dividends.** "Common Stock Dividends", FY2025: (649,942) $000. Separately, "Series D Mandatory Convertible Preferred Stock Dividends" (118,596).

**8. Quotes (all Item 1A, Risk Factors).**
1. "Such terms may include reduced management fees, fee holidays, increased co-investment rights or other economic or governance concessions, which could materially and adversely affect us in a number of ways, including by reducing the fee revenues we earn."
2. "Competitive pressures and evolving investor expectations may require us to agree to such unfavorable terms in order to attract or retain capital."
3. "Some of our competitors may have agreed to terms on their investment funds or products that are more favorable to investors than our funds or products and therefore we may be forced to match or otherwise revise our terms to be less favorable to us than they have been in the past and, further, some of our competitors may be willing to pay higher placement fees in order to gain distribution of their private wealth products."

---

## 3. Apollo Global Management, Inc. (APO), CIK 1858681

**1. Filing.** Accession **0001858681-26-000013**, filed **2026-02-25**, `apo-20251231.htm`.

**2. GAAP management fee line.** "Management fees" under "Asset Management". Item 8, Consolidated Statements of Operations ($m):
- FY2025: 2,378
- FY2024: 1,899
- FY2023: 1,772

Segment "Management fees" (Item 7, Asset Management segment, Credit + Equity, $m):
- FY2025: 3,391
- FY2024: 2,776
- FY2023: 2,480

Retirement Services also shows "Strategic capital management fees": 131 / 105 / 72.

**3. FEAUM equivalent.** "Fee-Generating AUM", Item 7, "Change in Fee-Generating AUM" table, Total ($ millions):
- YE2023: 492,952 (2024 "Beginning of Period")
- YE2024: 568,666
- YE2025: 709,139

MD&A: "Total Fee-Generating AUM was $709.1 billion at December 31, 2025, an increase of $140.5 billion, or 24.7%, compared to $568.7 billion at December 31, 2024." Also: "Total AUM was $938.4 billion at December 31, 2025."

**4. Perpetual share.**
- Item 1, Business, "Perpetual Capital": "Included within our investing strategies above is $535.6 billion of perpetual capital, out of the $938.4 billion of AUM as of December 31, 2025."
- Item 1, Business: "Perpetual capital vehicles, which represent nearly 60% of total AUM and over 70% of total fee-generating AUM, are highly scalable with the ability to deploy capital on an ongoing basis."
- COMPUTED check: 535.6 / 938.4 = 57.1% of AUM.

**5. FRE.** "Fee Related Earnings (FRE)", Asset Management segment ($m):
- FY2025: 2,528
- FY2024: 2,063
- FY2023: 1,768

A revenue subtotal is not printed. The components are Management fees, "Capital solutions fees and other, net" and "Fee-related performance fees", less "Fee-related compensation" and "Non-compensation expenses".

COMPUTED fee related revenues:
- 2025: 3,391 + 808 + 266 = 4,465
- 2024: 2,776 + 668 + 208 = 3,652

COMPUTED FRE margin: **56.6%** (2025) and 56.5% (2024).

**6. GAAP OCF.** "Net cash provided by operating activities" ($m):
- FY2023: 6,322
- FY2024: 3,253
- FY2025: 7,246

Consolidates Athene (Retirement Services) and consolidated funds/VIEs. The MD&A split table (Item 7, Liquidity):

| Line as filed | 2025 | 2024 | 2023 |
|---|---|---|---|
| "Net cash provided by the Company's operating activities" | 7,263 | 3,781 | 6,519 |
| "Net cash used in the Consolidated Funds and VIEs operating activities" | (17) | (528) | (197) |

MD&A wording: "Because our consolidated funds and VIEs are generally treated as investment companies for accounting purposes, their investing cash flow amounts are included in our cash flows from operating activities."

**7. Dividends.** "Common stock dividends", FY2025: (1,201) $m. Separately, "Preferred stock dividends" (97).

**8. Quotes (all Item 1A, Risk Factors).**
1. "Although we have no obligation to modify any fees or other terms with respect to the funds we manage, we experience pressure to do so."
2. "While we have historically competed primarily on the performance of the funds we manage, and not on the level of our management fees or performance fees relative to those of our competitors, there is a risk that management fees and performance fees in the alternative investment management industry will decline, without regard to the historical performance of a manager."
3. "Management fee or performance fee reductions on existing or future funds, without corresponding decreases in our cost structure even if other revenue streams increase, would adversely affect our revenues and profitability."

---

## 4. The Carlyle Group Inc. (CG), CIK 1527166

**1. Filing.** Accession **0001527166-26-000009**, filed **2026-02-27**, `cg-20251231.htm`.

**2. GAAP management fee line.** "Fund management fees". Item 8, Consolidated Statements of Operations ($m):
- FY2025: 2,396.6
- FY2024: 2,188.1
- FY2023: 2,043.2

Segment "Fund management fees" (Item 7, total segment revenues, $m):
- FY2025: 2,243.1
- FY2024: 2,107.5
- FY2023: not in this filing's segment table

**3. FEAUM equivalent.** "Fee-earning AUM", Item 7, "Fee-earning AUM Rollforward", Consolidated Results ($ millions):
- YE2023: 307,418 (2024 "Balance, Beginning of Period")
- YE2024: 304,358
- YE2025: 336,778

Footnote: "Ending balances as of December 31, 2025 and 2024 exclude $16.8 billion and $22.8 billion, respectively, of pending Fee-earning AUM for which fees have not yet been activated."

Total AUM, YE2025 (Item 1): "we have grown to manage $477 billion in AUM as of December 31, 2025."

Firm's own fee-rate disclosure is by segment only, as "Annualized Management Fee Rate" for 2025 and 2024:
- Global Private Equity: 1.17% and 1.17%
- Global Credit: 0.36% and 0.36%
- Carlyle AlpInvest: 0.68% and 0.66%

No consolidated rate is disclosed.

**4. Perpetual share.** Item 7, Key Financial Measures: "As of December 31, 2025, our total AUM and Fee-earning AUM included $115.4 billion and $110.9 billion, respectively, of Perpetual Capital. Our Perpetual Capital total AUM and Fee-earning AUM, exclusive of assets managed under the strategic advisory services agreement with Fortitude, was $35.0 billion and $30.5 billion, respectively, as of December 31, 2025."
- COMPUTED: 110.9 / 336.778 = 32.9% of FEAUM (9.1% excluding Fortitude, 30.5 / 336.778)
- COMPUTED: 115.4 / 477 = 24.2% of AUM

**5. FRE.** "Fee Related Earnings", total segments ($m):
- FY2025: 1,236.2
- FY2024: 1,104.6

Fee revenues as filed: "Total fund level fee revenues" 2,642.7 (2025) and 2,403.8 (2024), made up of Fund management fees, "Portfolio advisory and transaction fees, net and other", and "Fee related performance revenues".

COMPUTED FRE margin: 1,236.2 / 2,642.7 = **46.8%** (2025) and 1,104.6 / 2,403.8 = 46.0% (2024).

**6. GAAP OCF.** "Net cash provided by (used in) operating activities" ($m):
- FY2023: 204.9
- FY2024: (759.5)
- FY2025: (3,275.5)

Consolidates funds (mainly CLOs). The consolidated-fund flows sit inside operating activities. Item 7, Cash Flows table:

| Line as filed | 2025 | 2024 |
|---|---|---|
| "Net cash provided by the Company’s operating activities" | 1,088.6 | 1,088.9 |
| "Net cash used in the Consolidated Funds’ operating activities, after eliminations" | (4,364.1) | (1,848.4) |

COMPUTED check: 1,088.6 - 4,364.1 = (3,275.5). A notes table of operating-entity cash flows, whose net income column ties to the 2023 consolidating statement, shows "Net cash provided by operating activities" of 1,088.6 / 1,088.9 / 955.7 for 2025 / 2024 / 2023.

**7. Dividends.** "Dividends to common stockholders", FY2025: (505.1) $m.

**8. Quotes (all Item 1A, Risk Factors).**
1. "We have received and expect to continue to confront requests from a variety of investors and groups representing investors to decrease fees and to modify our carried interest and incentive fee structures, which could result in a reduction in or delay in the timing of receipt of the fees and carried interest and incentive fees we earn."
2. "We have historically competed primarily on the performance of our funds, and not on the level of our fees or carried interest relative to those of our competitors. However, there is a risk that fees and carried interest in the investment management industry will decline, without regard to the historical performance of a manager."
3. "While we have no obligation to modify any of our fees with respect to our existing funds, we may experience pressure to do so in our funds, including in response to regulatory focus by the SEC on the quantum and types of fees and expenses charged by private funds."

---

## 5. Ares Management Corporation (ARES), CIK 1176948

**1. Filing.** Accession **0001628280-26-011413**, filed **2026-02-25**, `ares-20251231.htm`.

**2. GAAP management fee line.** "Management fees". Item 8, Consolidated Statements of Operations ($000):
- FY2025: 3,680,467
- FY2024: 2,942,126
- FY2023: 2,551,150

Segment "Management fees", Total incl. OMG (Item 8 segment note, $000):
- FY2025: 3,682,922
- FY2024: 2,957,430
- FY2023: 2,571,513

**3. FEAUM equivalent.** "FPAUM" (fee paying AUM). Item 7, "rollforwards of our total FPAUM by segment", Total ($ millions):
- YE2023: 262,357
- YE2024: 292,553
- YE2025: 384,949

Total AUM, YE2025: 622,505 ($ millions, total AUM roll-forward "Balance at 12/31/2025").

Firm's own fee-rate disclosure: "effective management fee rate", defined as "annualized management fees divided by the average fee paying AUM for the period, excluding the impact of catch-up fees". It is presented by segment in charts, and the rate values are not in the extractable text, so they are not transcribed.

**4. Perpetual share.** Item 7: "For the years ended December 31, 2025 and 2024, 93% and 95%, respectively, of management fees were earned from perpetual capital or long-dated funds."
- This combines perpetual and long-dated; it is not perpetual-only.
- The "Perpetual Capital Assets Under Management" dollar amounts appear only in a chart, not in the text, so they are not disclosed in extractable form.

**5. FRE.** "Fee related earnings", Total column after OMG (Item 8 segment note, $000):
- FY2025: 1,775,300
- FY2024: 1,361,737

"Total Segments" before OMG: 2,583,501 and 1,982,667.

A fee-related-revenue subtotal is not printed. COMPUTED on the Total column:
- 2025: Management fees 3,682,922 + Fee related performance revenues 301,309 + Other fees 272,707 = 4,256,938
- 2024: 2,957,430 + 231,537 + 91,879 = 3,280,846

COMPUTED FRE margin: 1,775,300 / 4,256,938 = **41.7%** (2025) and 41.5% (2024).

**6. GAAP OCF.** "Net cash provided by (used in) operating activities" ($000):
- FY2023: (233,261)
- FY2024: 2,791,154
- FY2025: 3,266,959

Consolidates funds, and the operating section carries "Consolidated Funds:" lines. Item 7 split for 2025 and 2024:
- "Net cash provided by operating activities" (the Company): 2,113,088 and 1,404,724
- "Net cash provided by the Consolidated Funds’ operating activities, net of eliminations": 1,153,871 and 1,386,430

**7. Dividends.** "Dividends and distributions", FY2025: (1,756,688) $000. This single line combines Class A and non-voting common dividends, Series B preferred dividends and AOG unit distributions. A common-only cash line is not shown on the cash-flow statement. Dividends per Class A share declared in 2025: $1.12 per quarter (equity-compensation note).

**8. Quotes (all Item 1A, Risk Factors, under the heading "We may not be able to maintain our current fee structure as a result of industry pressure from fund investors to reduce fees, which could have an adverse effect on our profit margins and results of operations.").**
1. "In recent years, however, there has been a general trend toward lower fees in the investment management industry."
2. "Institutional investors have continued increasing pressure to reduce management and investment fees charged by external managers, whether through direct reductions, deferrals, rebates or other means."
3. "Although our investment management fees vary among and within asset classes, historically we have competed primarily on the basis of our performance and not on the level of our investment management fees relative to those of our competitors."

---

## 6. Blue Owl Capital Inc. (OWL), CIK 1823945

**1. Filing.** Accession **0001823945-26-000009**, filed **2026-02-19**, `owl-20251231.htm`.

**2. GAAP management fee line.** "Management fees, net (includes Part I Fees of $ 567,754 , $ 527,859 and $ 387,346 , respectively)". Item 8, Consolidated Statements of Operations ($000):
- FY2025: 2,521,937
- FY2024: 1,994,064
- FY2023: 1,527,241

**3. FEAUM equivalent.** "Fee-Paying AUM or FPAUM". Item 7, "Changes in FPAUM", Total "Ending Balance" ($ millions):
- YE2023: 102,696 (2024 "Beginning Balance")
- YE2024: 159,794
- YE2025: 187,735

Total AUM, YE2025: 307,432 ($ millions, "Changes in AUM" Ending Balance). Item 7 caption: "Blue Owl AUM: $307.4 billion FPAUM: $187.7 billion".

**4. Permanent share.**
- Item 1, Business: "For the year ended December 31, 2025, approximately 85% of our management fees were earned from Permanent Capital vehicles."
- Item 7: "Over the past year, approximately 84% and 85% of our GAAP and FRE management fees, respectively, were generated by Permanent Capital and the remainder was primarily from long-dated capital, with no meaningful pressure on our asset base from redemptions."

**5. FRE.** "Fee-Related Earnings" ($000):
- FY2025: 1,496,536
- FY2024: 1,253,366

"FRE revenues": 2,654,712 (2025) and 2,170,563 (2024). "Fee-Related Earnings Before Noncontrolling Interests": 1,547,525 and 1,289,438.

Firm-reported "FRE Margin": **58.3%** (2025) and 59.4% (2024). Definition as filed: "FRE Margin is a supplemental non-GAAP measure that equals Fee-Related Earnings before net income allocated to noncontrolling interests, divided by FRE revenues."

COMPUTED on the same basis as the other peers (FRE after NCI / FRE revenues): 1,496,536 / 2,654,712 = 56.4% (2025) and 57.7% (2024).

**6. GAAP OCF.** "Net Cash Provided by Operating Activities" ($000):
- FY2023: 949,145
- FY2024: 999,555
- FY2025: 1,256,032

The statement shows no consolidated-fund line items in operating activities.

**7. Dividends.** "Dividends paid on Class A Shares", FY2025: (546,657) $000. Separately, "Distributions to noncontrolling interests" (928,726).

**8. Quotes (all Item 1A, Risk Factors).**
1. "Additionally, Blue Owl may not be able to maintain its current fee structure as a result of increased transparency required by SEC rules or industry pressure from product investors to reduce fees."
2. "More recently, institutional investors have been increasing pressure to reduce management and incentive fees charged by external managers, whether through direct fee discounts as described in this paragraph, deferrals, [page-break artifact in source text: "27 Table of Contents"] rebates or by other means."
3. "As a result, Blue Owl may need to provide discounts more broadly to investors or reduce fees to meet such industry pressures, which reduction in fees may be further exacerbated by discount expectations of existing investors."

---

## 7. TPG Inc. (TPG), CIK 1880661

**1. Filing.** Accession **0001880661-26-000011**, filed **2026-02-17**, `tpg-20251231.htm`.

**2. GAAP management fee line.** "Management fees". Item 8, Revenues note ($000):
- FY2025: 1,826,411
- FY2024: 1,637,990
- FY2023: 1,187,947

The FY2023 figure predates the Angelo Gordon acquisition (listed in the investing lines as "Acquisition of Angelo Gordon").

Non-GAAP FRE table "Management fees" / "Total Management Fees": 1,800,061 (2025) and 1,625,710 (2024).

**3. FEAUM equivalent.** "Fee-earning AUM (“FAUM”)". Item 7, FAUM roll-forward ($ millions):
- YE2023: 136,794 (2024 "Balance as of Beginning of Period")
- YE2024: 141,286
- YE2025: 170,102

Total AUM, YE2025: 303,029 ($ millions, "AUM as of end of period").

**4. Perpetual share.** Not disclosed. The text refers to "open-ended funds and perpetual capital vehicles" but states no share or amount.

**5. FRE.** "Fee-Related Earnings" ($000):
- FY2025: 952,572
- FY2024: 764,228

"Fee-Related Revenues": 2,109,255 (2025) and 1,831,457 (2024).

COMPUTED FRE margin: 952,572 / 2,109,255 = **45.2%** (2025) and 41.7% (2024). No firm-reported FRE margin was found in the text.

**6. GAAP OCF.** "Net cash provided by operating activities" ($000):
- FY2023: 720,518
- FY2024: 532,146
- FY2025: 1,032,395

Liquidity wording lists "cash generated by our operating activities, such as management fees, monitoring, transaction and other fees, realized capital allocation-based income and investment sales from our consolidated funds". The 2023 operating section includes "Assets and liabilities, net related to consolidated Public SPACs" of 658,952.

**7. Dividends.** "Dividends/Distributions", FY2025: (1,229,045) $000. This line combines Class A dividends and distributions to non-controlling interests. In the equity statement, the 2025 "Dividends/distributions" row shows (289,209) in the TPG Inc. column and (999,053) for non-controlling interests, total (1,288,262). Those are equity-statement amounts, not the cash line.

**8. Quotes (all Item 1A, Risk Factors).**
1. "Investors could also demand lower fees or fee concessions for existing or future funds, which would likewise decrease our revenue."
2. List item, quoted as a fragment of a bulleted sentence: "some of our competitors may have agreed, or may agree, to terms on their funds or products that are more favorable to fund investors than those of our funds or products, such as lower management fees, greater fee sharing or higher hurdles for performance allocations, and we may be unable to match or otherwise revise our terms;"
3. "General market volatility or a reduction in distributions to investors could cause investors to delay making new commitments to funds or negotiate for lower fees, different fee sharing arrangements for transaction or other fees and other concessions."

---

## 8. BlackRock, Inc. (BLK), CIK 2012383

The filer is the new BlackRock, Inc. holding company CIK. This is the only 10-K under that CIK.

**1. Filing.** Accession **0001193125-26-071966**, filed **2026-02-25**, `blk-20251231.htm`.

**2. GAAP fee line.** No "management fee" line. The equivalent lines are "Investment advisory and administration fees" and "Total investment advisory, administration fees and securities lending revenue". Item 8, Consolidated Statements of Income ($m):

| Line as filed | FY2025 | FY2024 | FY2023 |
|---|---|---|---|
| Investment advisory and administration fees | 18,474 | 15,485 | 13,724 |
| Total investment advisory, administration fees and securities lending revenue | 19,179 | 16,100 | 14,399 |
| "Investment advisory performance fees" (separate line) | 1,424 | 1,207 | 554 |
| Total revenue | 24,216 | 20,407 | 17,859 |

**3. FEAUM equivalent.** No firm-wide FEAUM measure; total AUM is used. "Total" AUM, Item 7 component-changes tables ($ millions):
- YE2023: 10,008,995
- YE2024: 11,551,251
- YE2025: 14,041,518

"Full year average AUM": 12,603,633 (2025) and 10,804,007 (2024).

Private-markets fee-paying disclosure is limited to one transaction: "The closing of the HPS Transaction added $165 billion of client AUM and $118 billion of fee-paying AUM in July."

**4. Perpetual share.** Not applicable, and not disclosed.

**5. FRE.** Not applicable. Operating income and margin instead ($m):

| Line as filed | FY2025 | FY2024 | FY2023 |
|---|---|---|---|
| "Operating income" (GAAP) | 7,045 | 7,574 | 6,275 |
| "Operating income, as adjusted" | 9,600 | 8,110 | not in this reconciliation |
| "Operating margin, GAAP basis" | 29.1% | 37.1% | |
| "Operating margin, as adjusted" | **44.1%** | 44.5% | |

The as-adjusted margin is on "Revenue used for operating margin measurement" of 21,756 and 18,236.

Fee-rate disclosure: no basis-point base fee rate is stated. Narrative only: "BlackRock’s effective fee rates fluctuate due to changes in AUM mix." Also: "Clients awarded BlackRock with a record $698 billion of net inflows in 2025, driving 9% organic base fee growth."

COMPUTED fee rate:
- Spec basis: 19,179 / avg(11,551,251, 14,041,518) = 19,179 / 12,796,384.5 = **15.0 bps**
- Advisory and administration fees only: 18,474 / 12,796,384.5 = 14.4 bps
- On the firm's full-year average AUM: 19,179 / 12,603,633 = 15.2 bps

**6. GAAP OCF.** "Net cash provided by/(used in) operating activities" ($m):
- FY2023: 4,165
- FY2024: 4,956
- FY2025: 3,927

Consolidated investment products (CIPs) flow through operating activities. Item 7 supplemental table "Cash Flows Excluding Impact of CIPs":
- "Net cash provided by/(used in) operating activities": 7,463 (2025) and 7,267 (2024)
- "Impact on Cash Flows of CIPs": (3,536) and (2,311)

**7. Dividends.** "Dividends/Subco distributions paid", FY2025: (3,347) $m. Note 23: "During 2025, 2024 and 2023, the Company paid cash dividends of $ 20.84 per share (or $ 3.3 billion )".

**8. Quotes.**
1. Item 1A, Risk Factors: "This evolution, together with the introduction of new technologies, as well as regulatory changes, continues to alter the competitive landscape for investment managers, which may lead to additional fee compression or require BlackRock to invest more to modify or adapt its product offerings to attract and retain customers and remain competitive with the products, services and geographic diversity offered by other financial institutions, technology companies, advisory or asset management firms."
2. Item 1A, Risk Factors: "Increased competition on the basis of any of these factors, including competition leading to fee reductions on existing or new business, may cause the Company’s AUM, revenue and earnings to decline."
3. Item 7, MD&A (the sentence also appears in Item 1A): "As a result, the Company’s average effective fee rate may be lower (or higher) from period to period."

---

## 9. T. Rowe Price Group, Inc. (TROW), CIK 1113169

**1. Filing.** Accession **0001628280-26-008002**, filed **2026-02-13**, `trow-20251231.htm`.

**2. GAAP fee line.** "Investment advisory fees". Item 8, Consolidated Statements of Income ($m):
- FY2025: 6,602.3
- FY2024: 6,399.7
- FY2023: 5,709.5

"Performance-based advisory fees" is a separate line: 37.4 / 59.3 / 38.2. "Net revenues": 7,314.8 / 7,093.6 / 6,460.5.

**3. FEAUM equivalent.** No FEAUM measure; "Ending AUM" is used. Item 7 summary table ($ billions):
- YE2023: 1,444.5
- YE2024: 1,606.6
- YE2025: 1,775.6

"Average AUM": 1,677.3 (2025), 1,561.9 (2024), 1,362.3 (2023).

**4. Perpetual share.** Not applicable, and not disclosed.

**5. FRE.** Not applicable. "Net operating income" (GAAP) is used instead ($m):
- FY2025: 2,188.8
- FY2024: 2,333.3
- FY2023: 1,986.2

The non-GAAP adjusted "Net operating income" is 2,720.8 / 2,685.9 / 2,263.2.

COMPUTED GAAP operating margin: 2,188.8 / 7,314.8 = **29.9%** (2025) and 2,333.3 / 7,093.6 = 32.9% (2024).

Firm's own fee-rate disclosure, "Investment advisory annualized effective fee rate (EFR) (in bps)":

| Measure as filed | 2025 | 2024 | 2023 |
|---|---|---|---|
| "EFR without performance-based fees" | 39.4 | 41.0 | 41.9 |
| "EFR with performance-based fees" | 39.6 | 41.4 | 42.2 |

COMPUTED spec-basis rate: 6,602.3 / avg(1,606.6, 1,775.6) = 6,602.3 / 1,691.1 $bn = **39.0 bps**.

**6. GAAP OCF.** "Net cash provided by operating activities" ($m):
- FY2023: 1,219.1
- FY2024: 1,685.6
- FY2025: 1,753.4

Consolidated investment products sit inside operating activities. Item 7 split, "Cash flow attributable to T. Rowe Price Group" and "Cash flow attributable to consolidated investment products":

| | 2025 | 2024 | 2023 |
|---|---|---|---|
| T. Rowe Price Group | 2,489.5 | 2,313.9 | 2,058.6 |
| Consolidated investment products | (797.3) | (633.8) | (888.9) |
| Eliminations | 61.2 | 5.5 | 49.4 |

**7. Dividends.** "Dividends paid to common stockholders and equity-unit holders", FY2025: (1,143.0) $m.

**8. Quotes.**
1. Item 1, Business (repeated in Item 7): "The investment management industry continues to evolve and face challenging trends, including the shift in market share from traditional active strategies to passive products, persistent downward fee pressure, demand for lower cost investment vehicles, and an ever-changing regulatory landscape."
2. Item 1A, Risk Factors: "In the event that we decide to reduce the fees we charge for investment advisory services in response to competitive pressures, which we have done selectively in the past, revenues and operating margins could be adversely impacted."
3. Item 7, MD&A: "The average annualized effective fee rate earned for 2025 declined from 2024 primarily due to client flows and transfers shifting assets under management toward lower-fee strategies and products, partially offset by market appreciation."

---

## SUMMARY TABLE

All rates, CAGRs, shares and margins are COMPUTED unless marked "as filed". Arithmetic is in the notes below and in `calc.py`.

| ticker | 10-K accession | mgmt fee revenue FY2025 (label) | FEAUM-equiv YE2023 / YE2024 / YE2025 (label) | mgmt-fee rate, bps: FY25 fees / avg(YE24, YE25) | FEAUM CAGR 2023-25 | perpetual / permanent share (as stated) | FRE margin FY2025 (measure) | GAAP OCF FY2023 / FY2024 / FY2025 |
|---|---|---|---|---|---|---|---|---|
| BX | 0001193125-26-082531 | $8,075.6m "Management and Advisory Fees, Net" (segment Base Mgmt Fees $7,548.9m) | $762.6bn / $830.7bn / $921.7bn "Fee-Earning Assets Under Management" | **92.2** GAAP line; 86.2 on base fees; firm's own "Annualized Base Management Fee Rate" 0.86% | 9.9% | Perpetual Capital Total AUM $523.6bn (41.1% of Total AUM, computed); FEAUM share not disclosed | **58.3%** "Fee Related Earnings" / (Mgmt & Advisory Fees, Net + Fee Related Performance Revenues) | $4,056.9m / $3,481.7m / $4,663.2m |
| KKR | 0001404912-26-000007 | $2,496.8m GAAP "Management Fees" (segment "Management Fees" $4,100.8m) | ~$446bn (computed from rounded line items) / $512.0bn / $604.1bn "Fee Paying Assets Under Management" | **44.7** GAAP line; **73.5** on segment | 16.4% (on computed 2023) | "approximately 92% of our AUM" has a duration of at least eight years at inception or longer, including perpetual capital; perpetual-only share not disclosed | **69.1%** "Fee Related Earnings" / (Mgmt Fees + Transaction & Monitoring Fees, Net + FRPR) | $(1,493.8)m / $6,649.9m / $477.8m (incl. Global Atlantic and consolidated funds) |
| APO | 0001858681-26-000013 | $2,378m GAAP "Management fees" (segment $3,391m) | $493.0bn / $568.7bn / $709.1bn "Fee-Generating AUM" | **37.2** GAAP line; **53.1** on segment | 19.9% | "nearly 60% of total AUM and over 70% of total fee-generating AUM" (perpetual capital vehicles); $535.6bn of $938.4bn AUM | **56.6%** "Fee Related Earnings (FRE)" / (Mgmt fees + Capital solutions fees + Fee-related performance fees) | $6,322m / $3,253m / $7,246m (incl. Athene; funds/VIEs $(197) / $(528) / $(17)m) |
| CG | 0001527166-26-000009 | $2,396.6m "Fund management fees" (segment $2,243.1m) | $307.4bn / $304.4bn / $336.8bn "Fee-earning AUM" | **74.8** GAAP line; 70.0 on segment; firm rates by segment only | 4.7% | Perpetual Capital $110.9bn of Fee-earning AUM (32.9%, computed); $30.5bn ex-Fortitude (9.1%, computed) | **46.8%** "Fee Related Earnings" / "Total fund level fee revenues" | $204.9m / $(759.5)m / $(3,275.5)m (Company-only 2024 $1,088.9m, 2025 $1,088.6m) |
| ARES | 0001628280-26-011413 | $3,680.5m "Management fees" (segment $3,682.9m) | $262.4bn / $292.6bn / $384.9bn "FPAUM" | **108.6** GAAP line; 108.7 on segment | 21.1% | "93%" of 2025 management fees from "perpetual capital or long-dated funds" (95% in 2024); perpetual-only share not in text | **41.7%** "Fee related earnings" (after OMG) / (Mgmt fees + FRPR + Other fees) | $(233.3)m / $2,791.2m / $3,267.0m (Company-only 2024 $1,404.7m, 2025 $2,113.1m) |
| OWL | 0001823945-26-000009 | $2,521.9m "Management fees, net" | $102.7bn / $159.8bn / $187.7bn "Fee-Paying AUM or FPAUM" | **145.1** | 35.2% | "approximately 85% of our management fees were earned from Permanent Capital vehicles" (84% GAAP / 85% FRE management fees) | **56.4%** FRE after NCI / "FRE revenues"; firm-reported "FRE Margin" 58.3% (before NCI, as filed) | $949.1m / $999.6m / $1,256.0m (no consolidated-fund lines shown) |
| TPG | 0001880661-26-000011 | $1,826.4m "Management fees" (FRE table $1,800.1m) | $136.8bn / $141.3bn / $170.1bn "Fee-earning AUM (FAUM)" | **117.3** GAAP line; 115.6 on FRE-table fees | 11.5% | not disclosed | **45.2%** "Fee-Related Earnings" / "Fee-Related Revenues" | $720.5m / $532.1m / $1,032.4m |
| BLK | 0001193125-26-071966 | $19,179m "Total investment advisory, administration fees and securities lending revenue" ($18,474m advisory & admin fees) | $10,009.0bn / $11,551.3bn / $14,041.5bn total AUM (no FEAUM measure) | **15.0** (14.4 on advisory & admin fees only); no firm bps disclosure | 18.4% (AUM) | not applicable / not disclosed | n/a (no FRE). "Operating margin, as adjusted" 44.1% (as filed); GAAP operating margin 29.1% (as filed) | $4,165m / $4,956m / $3,927m (ex-CIPs 2024 $7,267m, 2025 $7,463m) |
| TROW | 0001628280-26-008002 | $6,602.3m "Investment advisory fees" | $1,444.5bn / $1,606.6bn / $1,775.6bn "Ending AUM" (no FEAUM measure) | **39.0**; firm's own "EFR without performance-based fees" 39.4 (2025), 41.0 (2024), 41.9 (2023) | 10.9% (AUM) | not applicable / not disclosed | n/a (no FRE). GAAP operating margin 29.9% (net operating income / net revenues) | $1,219.1m / $1,685.6m / $1,753.4m (T. Rowe-only 2023 $2,058.6m, 2024 $2,313.9m, 2025 $2,489.5m) |

### Arithmetic for the summary table

**Fee rate in bps = FY2025 fees / ((YE2024 + YE2025) / 2) x 10,000**, with units matched:

| ticker | fees | average FEAUM-equivalent | bps |
|---|---|---|---|
| BX | 8,075,601 | (830,708,603 + 921,674,454) / 2 = 876,191,528.5 ($000) | 92.2 |
| BX, base fees | 7,548,857 | 876,191,528.5 | 86.2 |
| KKR | 2,496,783 ($000) | (511,963 + 604,144) / 2 = 558,053.5 $m = 558,053,500 ($000) | 44.7 |
| KKR, segment | 4,100,841 | 558,053,500 | 73.5 |
| APO | 2,378 ($m) | (568,666 + 709,139) / 2 = 638,902.5 ($m) | 37.2 |
| APO, segment | 3,391 | 638,902.5 | 53.1 |
| CG | 2,396.6 ($m) | (304,358 + 336,778) / 2 = 320,568 ($m) | 74.8 |
| CG, segment | 2,243.1 | 320,568 | 70.0 |
| ARES | 3,680,467 ($000) | (292,553 + 384,949) / 2 = 338,751 $m = 338,751,000 ($000) | 108.6 |
| ARES, segment | 3,682,922 | 338,751,000 | 108.7 |
| OWL | 2,521,937 ($000) | (159,794 + 187,735) / 2 = 173,764.5 $m = 173,764,500 ($000) | 145.1 |
| TPG | 1,826,411 ($000) | (141,286 + 170,102) / 2 = 155,694 $m = 155,694,000 ($000) | 117.3 |
| TPG, FRE table | 1,800,061 | 155,694,000 | 115.6 |
| BLK | 19,179 ($m) | (11,551,251 + 14,041,518) / 2 = 12,796,384.5 ($m) | 15.0 |
| BLK, advisory & admin | 18,474 | 12,796,384.5 | 14.4 |
| TROW | 6,602.3 ($m) | (1,606.6 + 1,775.6) / 2 = 1,691.1 $bn = 1,691,100 ($m) | 39.0 |

**CAGR 2023-2025 = (YE2025 / YE2023)^(1/2) - 1:**

| ticker | arithmetic | CAGR |
|---|---|---|
| BX | 921,674,454 / 762,607,902 | 9.9% |
| KKR | 604.144 / 446 (2023 computed from rounded business-line $bn) | 16.4% |
| APO | 709,139 / 492,952 | 19.9% |
| CG | 336,778 / 307,418 | 4.7% |
| ARES | 384,949 / 262,357 | 21.1% |
| OWL | 187,735 / 102,696 | 35.2% |
| TPG | 170,102 / 136,794 | 11.5% |
| BLK | 14,041,518 / 10,008,995 | 18.4% |
| TROW | 1,775.6 / 1,444.5 | 10.9% |

Growth for KKR (Global Atlantic, HealthCare Royalty), OWL (IPI, Prima, Kuvare, Atalaya), ARES (GCP), TPG (Peppertree), APO (Bridge) and BLK (GIP, HPS, ElmTree) includes acquisitions, per each filing's roll-forward "Acquisitions" rows.

**FRE margin, FY2025:**

| ticker | FRE / fee related revenues | margin |
|---|---|---|
| BX | 5,737,537 / (8,016,049 + 1,825,428) | 58.3% |
| KKR | 3,714,313 / (4,100,841 + 1,092,577 + 181,784) | 69.1% |
| APO | 2,528 / (3,391 + 808 + 266) | 56.6% |
| CG | 1,236.2 / 2,642.7 | 46.8% |
| ARES | 1,775,300 / (3,682,922 + 301,309 + 272,707) | 41.7% |
| OWL | 1,496,536 / 2,654,712 (firm-reported, before NCI: 1,547,525 / 2,654,712 = 58.3%) | 56.4% |
| TPG | 952,572 / 2,109,255 | 45.2% |

**Perpetual shares:**

| ticker | arithmetic | share |
|---|---|---|
| BX | 523.6 / 1,274.931 | 41.1% of Total AUM |
| APO | 535.6 / 938.4 | 57.1% of AUM (firm states "nearly 60%") |
| CG | 110.9 / 336.778 | 32.9% of FEAUM |
| CG | 30.5 / 336.778 | 9.1% of FEAUM ex-Fortitude |
| CG | 115.4 / 477 | 24.2% of AUM |

**Comparability flags (data, not verdicts).**
- The FRE definitions differ by firm:
  - BX and KKR include fee-related performance revenues and transaction fees.
  - ARES's Total FRE is after "OMG" (Operations Management Group) costs.
  - OWL's own margin uses FRE before NCI.
- FEAUM definitions differ: some include performance-only capital (BX), exclude pending fee-earning commitments (CG), or use gross assets for BDCs (OWL).
- GAAP fee lines are net of consolidation eliminations, most materially at KKR and APO.
