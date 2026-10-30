# Peer utilities: SEC EDGAR XBRL figures, FY2016 to FY2025

Source: data.sec.gov companyfacts API, fetched 2026-10-26. Values in USD millions. Each value is the one reported in the 10-K for that fiscal year (fact fy equals the fiscal year, form 10-K, fp FY, 12-month duration for flows). ROE = net income / average of opening and closing common equity. Script: peers_fetch.py; raw JSON in cache\.

## Pinnacle West Capital (PNW, CIK 764622)

| FY | Net income | Common equity (YE) | ROE | Revenue | OCF | Capex | D&A | LT debt | 10-K accession |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 442 | 4,804 | 9.4% | 3,499 | 1,023 | 1,275 | 565 | 4,147 | 0000764622-17-000010 |
| 2017 | 488 | 5,007 | 10.0% | 3,565 | 1,118 | 1,409 | 611 | 4,872 | 0000764622-18-000018 |
| 2018 | 511 | 5,223 | 10.0% | 3,691 | 1,277 | 1,178 | 651 | 5,138 | 0000764622-19-000019 |
| 2019 | 538 | 5,431 | 10.1% | 3,471 | 957 | 1,191 | 664 | 5,633 | 0000764622-20-000017 |
| 2020 | 551 | 5,634 | 10.0% | 3,587 | 966 | 1,327 | 686 | 6,314 | 0000764622-21-000013 |
| 2021 | 619 | 5,906 | 10.7% | 3,804 | 860 | 1,473 | 719 | 7,064 | 0000764622-22-000014 |
| 2022 | 484 | 6,049 | 8.1% | 4,324 | 1,241 | 1,707 | 818 | 7,792 | 0000764622-23-000023 |
| 2023 | 502 | 6,178 | 8.2% | 4,696 | 1,208 | 1,846 | 854 | 8,416 | 0000764622-24-000016 |
| 2024 | 609 | 6,754 | 9.4% | 5,125 | 1,610 | 2,249 | 956 | 8,859 | 0000764622-25-000023 |
| 2025 | 617 | 7,046 | 8.9% | 5,340 | 1,805 | 2,625 | 970 | 9,806 | 0000764622-26-000011 |

Concepts used:

- Net income: NetIncomeLossAvailableToCommonStockholdersBasic (2016-2025)
- Equity: StockholdersEquity (2016-2025)
- Revenue: SalesRevenueNet (2016-2017); Revenues (2018-2025)
- Capex: PaymentsToAcquireProductiveAssets (2016-2025)
- D&A: DepreciationDepletionAndAmortization (2016-2025)
- LT debt: LongTermDebtNoncurrent + OtherLongTermDebtCurrent (2016-2023); LongTermDebtNoncurrent + LongTermDebtCurrent (2024-2025)

## IDACORP (IDA, CIK 1057877)

| FY | Net income | Common equity (YE) | ROE | Revenue | OCF | Capex | D&A | LT debt | 10-K accession |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 198 | 2,154 | 9.4% | 1,262 | 348 | 297 | 147 | 1,746 | 0001057877-17-000035 |
| 2017 | 212 | 2,251 | 9.6% | 1,349 | 438 | 285 | 166 | 1,746 | 0001057877-18-000027 |
| 2018 | 227 | 2,370 | 9.8% | 1,371 | 492 | 278 | 169 | 1,835 | 0001057877-19-000024 |
| 2019 | 233 | 2,465 | 9.6% | 1,346 | 367 | 279 | 174 | 1,837 | 0001057877-20-000040 |
| 2020 | 237 | 2,560 | 9.5% | 1,351 | 388 | 311 | 176 | 2,000 | 0001057877-21-000036 |
| 2021 | 246 | 2,668 | 9.4% | 1,458 | 363 | 300 | 179 | 2,001 | 0001057877-22-000014 |
| 2022 | 259 | 2,807 | 9.5% | 1,644 | 351 | 433 | 174 | 2,194 | 0001057877-23-000007 |
| 2023 | 261 | 2,908 | 9.1% | 1,766 | 267 | 611 | 200 | 2,776 | 0001057877-24-000005 |
| 2024 | 289 | 3,331 | 9.3% | 1,827 | 594 | 1,009 | 228 | 3,054 | 0001057877-25-000014 |
| 2025 | 323 | 3,572 | 9.4% | 1,813 | 602 | 1,179 | 258 | 3,331 | 0001057877-26-000028 |

Concepts used:

- Net income: NetIncomeLoss (2016-2025)
- Equity: StockholdersEquity (2016-2025)
- Revenue: SalesRevenueNet (2016-2017); RegulatedAndUnregulatedOperatingRevenue (2018-2025)
- Capex: PaymentsToAcquirePropertyPlantAndEquipment (2016-2025)
- D&A: DepreciationDepletionAndAmortization (2016-2025)
- LT debt: LongTermDebt (incl. current) (2016-2025)

## Portland General Electric (POR, CIK 784977)

| FY | Net income | Common equity (YE) | ROE | Revenue | OCF | Capex | D&A | LT debt | 10-K accession |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 193 | 2,344 | 8.4% | 1,923 | 553 | 584 | 321 | 2,361 | 0000784977-17-000006 |
| 2017 | 187 | 2,416 | 7.9% | 2,009 | 597 | 514 | 345 | 2,436 | 0000784977-18-000005 |
| 2018 | 212 | 2,506 | 8.6% | 1,991 | 630 | 595 | 382 | 2,488 | 0000784977-19-000010 |
| 2019 | 214 | 2,591 | 8.4% | 2,123 | 546 | 606 | 409 | 2,608 | 0000784977-20-000005 |
| 2020 | 155 | 2,613 | 6.0% | 2,145 | 567 | 784 | 454 | 3,059 | 0000784977-21-000007 |
| 2021 | 244 | 2,707 | 9.2% | 2,396 | 532 | 636 | 404 | 3,299 | 0000784977-22-000009 |
| 2022 | 233 | 2,779 | 8.5% | 2,647 | 674 | 766 | 417 | 3,659 | 0000784977-23-000005 |
| 2023 | 228 | 3,319 | 7.5% | 2,923 | 420 | 1,358 | 458 | 3,999 | 0000784977-24-000034 |
| 2024 | 313 | 3,794 | 8.8% | 3,440 | 778 | 1,268 | 496 | 4,539 | 0000784977-25-000012 |
| 2025 | 306 | 4,133 | 7.7% | 3,576 | 1,118 | 1,189 | 578 | 4,679 | 0001193125-26-052750 |

Concepts used:

- Net income: NetIncomeLoss (2016); ProfitLoss (2017-2025)
- Equity: StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest (no NCI tagged) (2016-2025)
- Revenue: ElectricUtilityRevenue (2016-2017); Revenues (2018-2025)
- Capex: PaymentsToAcquirePropertyPlantAndEquipment (2016-2025)
- D&A: DepreciationDepletionAndAmortization (2016-2025)
- LT debt: LongTermDebt (incl. current) (2016-2025)

## Xcel Energy (XEL, CIK 72903)

| FY | Net income | Common equity (YE) | ROE | Revenue | OCF | Capex | D&A | LT debt | 10-K accession |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 1,123 | 11,021 | 10.4% | 11,107 | 3,052 | 3,256 | 1,319 | 14,445 | 0000072903-17-000008 |
| 2017 | 1,148 | 11,455 | 10.2% | 11,404 | 3,126 | 3,319 | 1,495 | 14,977 | 0000072903-18-000009 |
| 2018 | 1,261 | 12,222 | 10.7% | 11,537 | 3,122 | 3,957 | 1,659 | 16,209 | 0000072903-19-000010 |
| 2019 | 1,372 | 13,239 | 10.8% | 11,529 | 3,263 | 4,225 | 1,785 | 18,109 | 0000072903-20-000011 |
| 2020 | 1,473 | 14,575 | 10.6% | 11,526 | 2,848 | 5,369 | 1,959 | 20,066 | 0000072903-21-000012 |
| 2021 | 1,597 | 15,612 | 10.6% | 13,431 | 2,189 | 4,244 | 2,143 | 22,380 | 0000072903-22-000010 |
| 2022 | 1,736 | 16,675 | 10.8% | 15,310 | 3,932 | 4,638 | 2,436 | 23,964 | 0000072903-23-000007 |
| 2023 | 1,771 | 17,616 | 10.3% | 14,206 | 5,327 | 5,854 | 2,471 | 25,465 | 0000072903-24-000034 |
| 2024 | 1,936 | 19,522 | 10.4% | 13,441 | 4,641 | 7,364 | 2,769 | 28,419 | 0000072903-25-000029 |
| 2025 | 2,018 | 23,609 | 9.4% | 14,669 | 4,083 | 10,908 | 2,968 | 31,832 | 0000072903-26-000009 |

Concepts used:

- Net income: NetIncomeLoss (2016-2025)
- Equity: StockholdersEquity (2016-2025)
- Revenue: Revenues (2016-2018); RegulatedAndUnregulatedOperatingRevenue (2019-2025)
- Capex: PaymentsToAcquireProductiveAssets (2016-2025)
- D&A: DepreciationAmortizationAndAccretionNet (2016-2025)
- LT debt: LongTermDebtAndCapitalLeaseObligations + LongTermDebtCurrent (2016); LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent (2017-2024); LongTermDebt (incl. current) (2025)

## Tucson Electric Power (TEP, CIK 100122)

| FY | Net income | Common equity (YE) | ROE | Revenue | OCF | Capex | D&A | LT debt | 10-K accession |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 124 | 1,559 | 8.2% | 1,235 | 425 | 250 | 164 | 1,453 | 0000100122-17-000003 |
| 2017 | 177 | 1,664 | 11.0% | 1,341 | 448 | 346 | 178 | 1,354 | 0000100122-18-000005 |
| 2018 | 188 | 1,820 | 10.8% | 1,433 | 457 | 393 | 191 | 1,615 | 0000100122-19-000004 |
| 2019 | 187 | 1,978 | 9.8% | 1,418 | 414 | 608 | 206 | 1,522 | 0000100122-20-000006 |
| 2020 | 191 | 2,341 | 8.9% | 1,425 | 466 | 840 | 234 | 1,814 | 0000100122-21-000005 |
| 2021 | 201 | 2,531 | 8.3% | 1,593 | 428 | 499 | 247 | 2,135 | 0000100122-22-000004 |
| 2022 | 217 | 2,656 | 8.4% | 1,808 | 509 | 458 | 256 | 2,115 | 0000100122-23-000004 |
| 2023 | 259 | 2,849 | 9.4% | 1,875 | 560 | 578 | 244 | 2,397 | 0000100122-24-000002 |
| 2024 | 289 | 3,103 | 9.7% | 1,805 | 663 | 733 | 274 | 2,495 | 0000100122-25-000004 |
| 2025 | 283 | 3,449 | 8.7% | 1,689 | 590 | 828 | 285 | 2,793 | 0000100122-26-000006 |

Concepts used:

- Net income: NetIncomeLossAvailableToCommonStockholdersBasic (2016-2024); NetIncomeLoss (2025)
- Equity: StockholdersEquity (2016-2025)
- Revenue: Revenues (2016-2025)
- Capex: PaymentsToAcquirePropertyPlantAndEquipment (2016-2025)
- D&A: Depreciation + OtherDepreciationAndAmortization (2016-2025)
- LT debt: LongTermDebtNoncurrent (current not tagged) (2016); LongTermDebt (incl. current) (2017-2025)

## Summary, FY2016 to FY2025

| Company | Avg ROE (10 yrs) | Sum OCF minus capex ($m) | Capex / D&A | Revenue CAGR 2016-2025 |
|---|---|---|---|---|
| Pinnacle West Capital (PNW) | 9.5% | -4,216 | 2.17x | 4.8% |
| IDACORP (IDA) | 9.5% | -772 | 2.66x | 4.1% |
| Portland General Electric (POR) | 8.1% | -1,885 | 1.95x | 7.1% |
| Xcel Energy (XEL) | 10.4% | -17,550 | 2.53x | 3.1% |
| Tucson Electric Power (TEP) | 9.3% | -570 | 2.43x | 3.5% |

## Allowed ROE and equity ratio, last state order (from FY2025 10-K text)

| Company (utility) | Allowed ROE | Equity ratio in order | Order | FY2025 10-K accession |
|---|---|---|---|---|
| PNW (APS, ACC) | 9.55% | not stated in 10-K text | ACC approval of 2022 Rate Case ROO, 22 Feb 2024 | 0000764622-26-000011 |
| IDA (Idaho Power, IPUC) | 9.6% | not specified ("filed cost of debt and capital structure") | IPUC approval of 2025 Settlement Stipulation, Dec 2025, rates eff. 1 Jan 2026 | 0001057877-26-000028 |
| POR (PGE, OPUC) | 9.34% | not stated in 10-K text (company target ~50%) | OPUC 2025 GRC order (UE 435), 20 Dec 2024; reaffirmed in Order 25-417, 21 Oct 2025 | 0001193125-26-052750 |
| XEL (NSP-Minnesota, MPUC electric) | 9.25% | 52.5% | MPUC approval, July 2023 (2022-2024 multi-year plan) | 0000072903-26-000009 |
| TEP (ACC) | not stated in 10-K text | not stated in 10-K text | 2023 Rate Order, rates effective 1 Sep 2023 | 0000100122-26-000006 |

Quotes:

- PNW: "On February 22, 2024, the ACC approved the 2022 Rate Case ROO with certain amendments that resulted in, among other things, (i) an approximately $491.7 million increase in the annual base revenue requirement, (ii) a 9.55% return on equity, ..." The 10-K also states APS's actual common equity ratio (ACC definition) was 52% at 31 Dec 2025 and the ACC dividend floor is 40%. The pending 2025 Rate Case requests 10.70% ROE on 52.35% equity.
- IDA: "In December 2025, the IPUC approved a settlement stipulation (2025 Settlement Stipulation) related to the Idaho general rate case that Idaho Power had filed in May 2025, with new rates effective January 1, 2026." Terms: "a 9.6 percent return on equity and a 7.41 percent authorized rate of return based on the filed cost of debt and capital structure, applied to an Idaho-jurisdictional rate base of approximately $4.9 billion".
- POR: "PGE's authorized ROE was 9.34 % for 2025 and 9.5 % for 2024." The 2025 GRC order is referred to as "its Order issued December 20, 2024 related to PGE's 2025 GRC (OPUC Docket UE 435)".
- XEL: "In July 2023, the MPUC approved a three-year rate increase of approximately $332 million for 2022-2024, based on a ROE of 9.25% and an equity ratio of 52.5%." (2024 Minnesota electric case pending: requested 10.3% ROE, 52.5% equity.)
- TEP: the FY2025 10-K says "TEP's last rate case proceeding was finalized in 2023" but gives no ROE or capital structure for the 2023 Rate Order. Pending 2025 Rate Case: "a return on equity of 10.50% ... a capital structure for ratemaking purposes of approximately 55% common equity and 45% long-term debt".

## Tagging notes

- TEP is still an SEC filer: FY2025 10-K filed 12 Feb 2026 (accession 0000100122-26-000006).
- PNW tags net income to common only as NetIncomeLossAvailableToCommonStockholdersBasic (NetIncomeLoss last used FY2010). Revenue is SalesRevenueNet for FY2016-17.
- POR tags ProfitLoss from FY2017 (no noncontrolling interest after 2016) and equity only as StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; with no NCI these equal common figures. POR's FY2025 10-K was filed under a filing agent accession (0001193125-...). It also carries a stray LongTermDebt fact dated 2025-10-27 ($68m), excluded.
- PNW current maturities of LT debt are tagged OtherLongTermDebtCurrent through FY2023, LongTermDebtCurrent from FY2024.
- TEP has no combined D&A tag: D&A = Depreciation + OtherDepreciationAndAmortization (income statement lines). FY2016 TEP LT debt is noncurrent only (current not tagged).
- XEL D&A is DepreciationAmortizationAndAccretionNet (cash flow statement); XEL LT debt for FY2016-24 includes capital/finance lease obligations.
- Revenue concept switches at ASC 606 (FY2018) for most filers; totals used throughout, not RevenueFromContractWithCustomer.
- Figures for parents (PNW, IDA, XEL) are consolidated; companyfacts excludes the subsidiary registrant (APS, Idaho Power, NSP etc.) data in combined filings.
