# Competitor figures from SEC EDGAR: NRG Energy peer set

Compiled 2026-10-26. The only sources are SEC EDGAR (data.sec.gov XBRL company-facts and submissions APIs, plus primary documents under sec.gov/Archives). This file states facts only and gives no assessments.

## Method and definitions

- **Source per cell.** Each annual cell comes from the 10-K for that fiscal year: the XBRL fact carrying that 10-K's accession number. When that 10-K lacks the fact, the earliest later 10-K that contains it is used. The figures are therefore **as originally filed** and are not recast for later restatements. Notes below each table list the cells that were transcribed from filing text.
- **Revenue** is total operating revenues (us-gaap `Revenues`, or the equivalent revenue tag). **Operating income** is `OperatingIncomeLoss` as filed.
- **D&A** is the depreciation and amortization line on the income statement. For CEG and TLN this line excludes nuclear-fuel amortization, which those companies record in fuel cost. The cash-flow D&A add-back is larger, because it also includes nuclear fuel, contract amortization and accretion.
- **Capex** is the cash-flow-statement capital-expenditure line as filed:
  - Vistra: "Capital expenditures, including nuclear fuel purchases and LTSA prepayments". This line includes growth/development spend from FY2019 on. FY2017 and FY2018 were rebuilt from the separate lines shown in the FY2019 10-K.
  - CEG: "Capital expenditures". It includes nuclear fuel, and no separate line exists.
  - TLN: "Nuclear fuel expenditures" is a separate CF line, shown as the extra row and **added to capex** in the FCF ratio.
- **Debt** is long-term debt including current maturities. It excludes short-term borrowings and commercial paper, which are listed in the notes where material.
- **Intangibles** are intangible assets net, excluding goodwill.
- **Equity** is total equity including noncontrolling interests. Via's Series A preferred is in mezzanine and is excluded.
- **Ratio 1** = operating income / (total assets - goodwill - intangibles), using year-end balances.
- **Ratio 2** = (cash from operations - share-based compensation - capex) / revenue. Capex includes nuclear fuel for all companies.
- **Averages** are simple means of the yearly ratios over the years available: FY2021-25 for the five-year figure, FY2016-25 for the whole span (CEG: FY2021-25).
- **FY2026 YTD** columns use 10-Q XBRL: six months to 30 Jun 2026 (Via: three months to 31 Mar 2026). YTD Ratio 1 is not annualised.

## Ratio summary

| Company | Ratio | FY16 | FY17 | FY18 | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | Avg FY21-25 | Avg span | 2026 YTD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VST | OI/(TA-GW-Int) | n/a | 1.9% | 2.3% | 9.4% | 7.5% | -6.1% | -4.2% | 9.3% | 12.5% | 5.2% | 3.4% | 4.2% (9 yrs) | 5.5% (H1) |
| VST | (OCF-SBC-capex)/Rev | n/a | 18.4% | 9.5% | 16.7% | 17.6% | -10.6% | -6.4% | 25.0% | 13.8% | 6.8% | 5.7% | 10.1% (9 yrs) | 6.0% (H1) |
| CEG | OI/(TA-GW-Int) | - | - | - | - | (0.5%)* | -0.7% | 1.1% | 3.2% | 8.3% | 5.4% | 3.5% | 3.5% (5 yrs) | 3.4% (H1) |
| CEG | (OCF-SBC-capex)/Rev | - | - | - | - | (-6.8%)* | -13.8% | -17.0% | -31.7% | -22.7% | 3.5% | -16.3% | -16.3% (5 yrs) | -5.2% (H1) |
| TLN | OI/(TA-GW-Int) | - | - | - | - | - | - | n/a | 1.2%** | 3.7% | -0.8% | 1.4% (3 yrs) | 1.4% | 0.9% (H1) |
| TLN | (OCF-SBC-capex-nuc fuel)/Rev | - | - | - | - | - | - | -4.0% | 19.5%** | 1.6% | -1.1% | 4.0% (4 yrs) | 4.0% | -15.4% (H1) |
| GNE | OI/(TA-GW-Int) | -28.0% | -5.9% | 9.3% | 7.1% | 12.9% | 15.5% | 29.4% | 3.1% | 3.2% | 7.4% | 11.7% | 5.4% (10 yrs) | 2.4% (H1) |
| GNE | (OCF-SBC-capex)/Rev | 4.8% | 0.3% | 5.1% | 4.5% | 5.7% | 17.6% | 24.3% | 13.6% | 14.5% | 7.1% | 15.4% | 9.8% (10 yrs) | n/a |
| VIA | OI/(TA-GW-Int) | 31.9% | 31.6% | -1.2% | 9.0% | 39.6% | 2.0% | 12.1% | 25.7% | 39.9% | 26.5% | 21.2% | 21.7% (10 yrs) | 2.4% (Q1) |
| VIA | (OCF-SBC-capex)/Rev | 11.0% | 7.2% | 5.2% | 10.5% | 15.7% | 1.7% | 2.3% | 10.5% | 11.7% | 8.4% | 6.9% | 8.4% (10 yrs) | 5.8% (Q1) |

\* CEG FY2020 is the Exelon Generation predecessor comparative period shown in CEG's first 10-K. It is excluded from the averages.
\*\* TLN FY2023 adds the Predecessor (1 Jan-17 May 2023) and Successor (18 May-31 Dec 2023) periods. Fresh-start accounting makes the two periods non-comparable, so the sum is arithmetic only.

**CEG memo.** Exelon Generation/CEG sold receivables under a facility whose "Collection of DPP" (deferred purchase price) proceeds are classified in **investing**, not operating, cash flow:

| | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| Collection of DPP, $m | 3,771 | 3,902 | 4,964 | 7,340 | 10,217 | none |

Sources: CEG FY2022 10-K CF (0001868275-23-000014) and FY2025 10-K CF (0001868275-26-000032). If these collections are added back to OCF, (OCF + DPP - SBC - capex) / revenue is:

| FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Mean |
|---|---|---|---|---|---|
| 6.0% | 3.3% | -2.3% | 20.6% | 3.5% | 6.2% |

This is arithmetic on filed figures and is not a company-reported measure.

## Annual tables

### Vistra Corp (VST, CIK 1692819) -- annual data (USD millions)

| Item | FY2016 | FY2017 | FY2018 | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | YTD to 2026-06-30 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | n/a | 5,430 | 9,144 | 11,809 | 11,443 | 12,077 | 13,728 | 14,779 | 17,224 | 17,738 | 9,657 |
| Operating income | n/a | 198 | 491 | 1,993 | 1,519 | -1,515 | -1,177 | 2,661 | 4,081 | 1,906 | 2,052 |
| D&A (income stmt) | n/a | 699 | 1,394 | 1,640 | 1,737 | 1,753 | 1,596 | 1,502 | 1,843 | 1,986 | 929 |
| Cash from operations | n/a | 1,386 | 1,471 | 2,736 | 3,337 | -206 | 485 | 5,453 | 4,563 | 4,070 | 2,222 |
| Capex (CF line, as filed) | n/a | 366 | 530 | 713 | 1,259 | 1,033 | 1,301 | 1,676 | 2,078 | 2,752 | 1,572 |
|   of which / plus nuclear fuel | n/a | 62.0 | 118 | 89.0 | 88.0 | 44.0 | 198 | 214 | 477 | n/a | n/a |
| Acquisitions, net of cash | n/a | 355 | 0.0 | 880 | 0.0 | 0.0 | 0.0 | 0.0 | 3,065 | 1,140 | -6.0 |
| Share-based comp | n/a | 19.0 | 73.0 | 47.0 | 65.0 | 47.0 | 63.0 | 77.0 | 100 | 113 | 67.0 |
| Total assets | 15,167 | 14,600 | 26,024 | 26,616 | 25,208 | 29,683 | 32,787 | 32,966 | 37,770 | 41,550 | 42,603 |
| Goodwill | 1,907 | 1,907 | 2,068 | 2,553 | 2,583 | 2,583 | 2,583 | 2,583 | 2,807 | 2,810 | 2,810 |
| Intangible assets | 3,205 | 2,530 | 2,493 | 2,748 | 2,446 | 2,146 | 1,958 | 1,864 | 2,213 | 2,435 | 2,286 |
| LT debt incl. current | 4,623 | 4,423 | 11,065 | 10,379 | 9,330 | 10,731 | 11,971 | 14,402 | 16,298 | 17,043 | 19,595 |
| Cash & equivalents | 843 | 1,487 | 636 | 300 | 406 | 1,325 | 455 | 3,485 | 1,188 | 785 | 435 |
| Total equity | 6,597 | 6,342 | 7,867 | 7,960 | 8,361 | 8,292 | 4,918 | 5,322 | 5,583 | 5,110 | 5,494 |
| Share repurchases | n/a | 0.0 | 763 | 656 | 0.0 | 471 | 1,949 | 1,245 | 1,266 | 1,028 | 709 |
| **OI / (TA - GW - intangibles)** | n/a | 1.9% | 2.3% | 9.4% | 7.5% | -6.1% | -4.2% | 9.3% | 12.5% | 5.2% | 5.5% (not annualised) |
| **(OCF - SBC - capex) / revenue** | n/a | 18.4% | 9.5% | 16.7% | 17.6% | -10.6% | -6.4% | 25.0% | 13.8% | 6.8% | 6.0% |

Averages (simple mean of yearly ratios). OI/(TA-GW-intang): FY2021-25 = 3.4% (n=5); whole span = 4.2% (n=9). (OCF-SBC-capex)/revenue: FY2021-25 = 5.7% (n=5); whole span = 10.1% (n=9).

XBRL company-facts values in this table come from these 10-K accessions: 0001692819-18-000018, 0001692819-19-000005, 0001692819-20-000005, 0001692819-21-000004, 0001692819-22-000005, 0001692819-23-000005, 0001692819-24-000012, 0001692819-25-000013, 0001692819-26-000006. Cells marked in the notes below were transcribed from filing text instead.


### Constellation Energy (CEG, CIK 1868275) -- annual data (USD millions)

| Item | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | YTD to 2026-06-30 |
|---|---|---|---|---|---|---|---|
| Revenue | 17,603 | 19,649 | 24,440 | 24,918 | 23,568 | 25,533 | 18,626 |
| Operating income | 256 | -346 | 495 | 1,610 | 4,352 | 3,086 | 2,912 |
| D&A (income stmt) | 2,123 | 3,003 | 1,091 | 1,096 | 1,123 | 985 | 886 |
| Cash from operations | 584 | -1,338 | -2,353 | -5,301 | -2,464 | 4,237 | 1,553 |
| Capex (CF line, as filed) | 1,747 | 1,329 | 1,689 | 2,422 | 2,565 | 2,949 | 2,521 |
| Acquisitions, net of cash | n/a | 30.0 | 29.0 | 1,690 | 32.0 | 14.0 | 2,537 |
| Share-based comp | 27.0 | 47.0 | 116 | 178 | 332 | 385 | n/a |
| Total assets | 48,094 | 48,086 | 46,909 | 50,758 | 52,926 | 57,249 | 98,253 |
| Goodwill | n/a | 47.0 | 47.0 | 425 | 420 | 420 | 11,527 |
| Intangible assets | n/a | 381 | 343 | 336 | 236 | 201 | n/a |
| LT debt incl. current | 5,763 | 6,114 | 4,609 | 7,617 | 8,412 | 7,342 | 19,111 |
| Cash & equivalents | 226 | 504 | 422 | 368 | 3,022 | 3,641 | 697 |
| Total equity | 14,676 | 11,614 | 11,372 | 11,286 | 13,539 | 14,853 | 32,322 |
| Share repurchases | n/a | 0.0 | 0.0 | 992 | 999 | 400 | 1,971 |
| **OI / (TA - GW - intangibles)** | 0.5% | -0.7% | 1.1% | 3.2% | 8.3% | 5.4% | 3.4% (not annualised) |
| **(OCF - SBC - capex) / revenue** | -6.8% | -13.8% | -17.0% | -31.7% | -22.7% | 3.5% | -5.2% |

Averages (simple mean of yearly ratios). OI/(TA-GW-intang): FY2021-25 = 3.5% (n=5); whole span = 3.5% (n=5). (OCF-SBC-capex)/revenue: FY2021-25 = -16.3% (n=5); whole span = -16.3% (n=5).

XBRL company-facts values in this table come from these 10-K accessions: 0001868275-23-000014, 0001868275-24-000014, 0001868275-25-000023, 0001868275-26-000032. Cells marked in the notes below were transcribed from filing text instead.


### Talen Energy (TLN, CIK 1622536) -- annual data (USD millions)

| Item | FY2022 | FY2023 | FY2024 | FY2025 | YTD to 2026-06-30 |
|---|---|---|---|---|---|
| Revenue | 3,089 | 2,554 | 2,115 | 2,581 | 1,876 |
| Operating income | 241 | 84.0 | 226 | -90.0 | 138 |
| D&A (income stmt) | 520 | 365 | 298 | 279 | 195 |
| Cash from operations | 187 | 864 | 256 | 704 | 27.0 |
| Capex (CF line, as filed) | 232 | 254 | 85.0 | 98.0 | 181 |
|   of which / plus nuclear fuel | 80.0 | 94.0 | 104 | 108 | 66.0 |
| Acquisitions, net of cash | 0.0 | 0.0 | 0.0 | 3,793 | 2,568 |
| Share-based comp | 0.0 | 19.0 | 33.0 | 526 | 69.0 |
| Total assets | n/a | 7,121 | 6,106 | 10,905 | 15,068 |
| Goodwill | n/a | 0.0 | 0.0 | 0.0 | n/a |
| Intangible assets | n/a | 0.0 | 0.0 | 0.0 | n/a |
| LT debt incl. current | n/a | 2,820 | 3,004 | 6,811 | n/a |
| Cash & equivalents | n/a | 400 | 328 | 689 | 231 |
| Total equity | -482 | 2,534 | 1,387 | 1,093 | 1,639 |
| Share repurchases | 0.0 | 0.0 | 1,958 | 103 | 298 |
| **OI / (TA - GW - intangibles)** | n/a | 1.2% | 3.7% | -0.8% | 0.9% (not annualised) |
| **(OCF - SBC - capex) / revenue** | -4.0% | 19.5% | 1.6% | -1.1% | -15.4% |

Averages (simple mean of yearly ratios). OI/(TA-GW-intang): FY2021-25 = 1.4% (n=3); whole span = 1.4% (n=3). (OCF-SBC-capex)/revenue: FY2021-25 = 4.0% (n=4); whole span = 4.0% (n=4).

XBRL company-facts values in this table come from these 10-K accessions: 0001622536-26-000017, 0001628280-25-008786. Cells marked in the notes below were transcribed from filing text instead.


### Genie Energy (GNE, CIK 1528356) -- annual data (USD millions)

| Item | FY2016 | FY2017 | FY2018 | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | YTD to 2026-06-30 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 212 | 264 | 280 | 315 | 379 | 364 | 316 | 429 | 425 | 502 | 243 |
| Operating income | -30.5 | -6.5 | 12.0 | 9.8 | 19.3 | 33.1 | 77.8 | 10.0 | 11.3 | 27.7 | 8.4 |
| D&A (income stmt) | 0.6 | 2.1 | 2.1 | 3.6 | 3.5 | 1.3 | 0.4 | 0.5 | 0.9 | 1.0 | 0.7 |
| Cash from operations | 15.6 | 9.3 | 19.4 | 15.8 | 23.1 | 67.0 | 80.7 | 62.5 | 70.7 | 46.3 | -9.9 |
| Capex (CF line, as filed) | 0.6 | 3.3 | 0.6 | 0.4 | 0.2 | 0.1 | 1.0 | 1.4 | 6.7 | 8.2 | n/a |
| Acquisitions, net of cash | 8.7 | 4.2 | 0.2 | 2.0 | 0.0 | 0.0 | 0.0 | 7.7 | 1.3 | 0.0 | n/a |
| Share-based comp | 4.8 | 5.2 | 4.5 | 1.1 | 1.1 | 2.9 | 3.0 | 2.8 | 2.3 | 2.5 | 1.4 |
| Total assets | 122 | 126 | 147 | 156 | 187 | 230 | 278 | 331 | 371 | 389 | 370 |
| Goodwill | 8.7 | 10.0 | 11.1 | 12.1 | 25.9 | 11.8 | 10.0 | 10.0 | 12.7 | 13.0 | 13.9 |
| Intangible assets | 4.3 | 4.9 | 6.3 | 6.8 | 11.6 | 3.6 | 3.1 | 2.7 | 2.4 | 1.8 | 1.7 |
| LT debt incl. current | 0.0 | 2.5 | 2.5 | 0.9 | 2.3 | 0.0 | 0.0 | 0.0 | 9.1 | 8.6 | n/a |
| Cash & equivalents | 35.2 | 29.9 | 41.6 | 31.2 | 36.9 | 95.5 | 98.6 | 108 | 104 | 204 | 185 |
| Total equity | 79.9 | 67.1 | 92.7 | 80.9 | 86.1 | 111 | 174 | 184 | 180 | 244 | 255 |
| Share repurchases | 0.0 | 0.8 | 0.9 | 5.6 | 1.7 | 3.8 | 4.4 | 0.0 | 10.4 | 8.7 | n/a |
| **OI / (TA - GW - intangibles)** | -28.0% | -5.9% | 9.3% | 7.1% | 12.9% | 15.5% | 29.4% | 3.1% | 3.2% | 7.4% | 2.4% (not annualised) |
| **(OCF - SBC - capex) / revenue** | 4.8% | 0.3% | 5.1% | 4.5% | 5.7% | 17.6% | 24.3% | 13.6% | 14.5% | 7.1% | n/a |

Averages (simple mean of yearly ratios). OI/(TA-GW-intang): FY2021-25 = 11.7% (n=5); whole span = 5.4% (n=10). (OCF-SBC-capex)/revenue: FY2021-25 = 15.4% (n=5); whole span = 9.8% (n=10).

XBRL company-facts values in this table come from these 10-K accessions: 0001213900-17-002459, 0001213900-18-003067, 0001213900-19-004396, 0001213900-20-006416, 0001213900-21-015538, 0001213900-22-012716, 0001213900-23-020226, 0001213900-24-022573, 0001213900-25-024009, 0001437749-26-014294. Cells marked in the notes below were transcribed from filing text instead.


### Via Renewables, formerly Spark Energy (VIA, CIK 1606268) -- annual data (USD millions)

| Item | FY2016 | FY2017 | FY2018 | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | YTD to 2026-03-31 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 547 | 798 | 1,006 | 814 | 555 | 394 | 460 | 435 | 399 | 464 | 159 |
| Operating income | 84.0 | 102 | -3.7 | 24.0 | 88.8 | 4.4 | 24.8 | 46.5 | 84.2 | 53.5 | 4.8 |
| D&A (income stmt) | 32.8 | 42.3 | 52.7 | 41.0 | 30.8 | 21.6 | 16.7 | 9.1 | 9.4 | 21.8 | 5.9 |
| Cash from operations | 67.8 | 63.9 | 59.8 | 91.7 | 91.8 | 12.7 | 16.2 | 49.3 | 50.5 | 42.1 | 9.4 |
| Capex (CF line, as filed) | 2.3 | 1.7 | 1.4 | 1.1 | 2.2 | 2.7 | 2.2 | 1.4 | 1.6 | 3.0 | 0.2 |
| Acquisitions, net of cash | 30.1 | 75.9 | 17.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | n/a |
| Share-based comp | 5.2 | 5.1 | 5.9 | 5.5 | 2.5 | 3.4 | 3.3 | 2.3 | 2.4 | 0.0 | n/a |
| Total assets | 376 | 506 | 489 | 423 | 367 | 355 | 331 | 304 | 345 | 331 | 323 |
| Goodwill | 79.1 | 120 | 120 | 120 | 120 | 120 | 120 | 120 | 120 | 120 | 120 |
| Intangible assets | 33.5 | 62.0 | 50.3 | 37.1 | 22.4 | 17.7 | 5.8 | 2.9 | 13.5 | 8.8 | 5.8 |
| LT debt incl. current | 71.8 | 159 | 146 | 123 | 100 | 135 | 120 | 97.0 | 106 | 120 | 130 |
| Cash & equivalents | 19.0 | 29.4 | 41.0 | 56.7 | 71.7 | 68.9 | 33.7 | 42.6 | 53.1 | 41.8 | 50.6 |
| Total equity | 124 | 161 | 90.3 | 67.3 | 88.5 | 50.4 | 28.3 | 38.7 | 81.0 | 77.4 | 73.4 |
| Share repurchases | 0.0 | 2.0 | 0.0 | 0.0 | 0.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | n/a |
| **OI / (TA - GW - intangibles)** | 31.9% | 31.6% | -1.2% | 9.0% | 39.6% | 2.0% | 12.1% | 25.7% | 39.9% | 26.5% | 2.4% (not annualised) |
| **(OCF - SBC - capex) / revenue** | 11.0% | 7.2% | 5.2% | 10.5% | 15.7% | 1.7% | 2.3% | 10.5% | 11.7% | 8.4% | 5.8% |

Averages (simple mean of yearly ratios). OI/(TA-GW-intang): FY2021-25 = 21.2% (n=5); whole span = 21.7% (n=10). (OCF-SBC-capex)/revenue: FY2021-25 = 6.9% (n=5); whole span = 8.4% (n=10).

XBRL company-facts values in this table come from these 10-K accessions: 0001606268-17-000012, 0001606268-18-000017, 0001606268-19-000008, 0001606268-20-000008, 0001606268-21-000015, 0001606268-22-000008, 0001606268-23-000009, 0001606268-24-000008, 0001606268-25-000006, 0001606268-26-000013. Cells marked in the notes below were transcribed from filing text instead.

## Notes on the tables: cells from filing text, and comparability

### Vistra (VST)
- **FY2016 is not tabulated as a year.** Vistra emerged from the TCEH bankruptcy on 3 Oct 2016. FY2016 income and cash flows are split between the Predecessor period (1 Jan-2 Oct 2016) and the Successor period (3 Oct-31 Dec 2016), so no 12-month figures exist. Only the 31 Dec 2016 balance sheet is shown, taken from the FY2017 10-K.
  - FY2016 equity is 6,597. A later 10-K tags this value with a negative sign in the equity statement; the FY2017 10-K value was used.
  - Predecessor capex for 1 Jan-2 Oct 2016 was $263m, including $33m of nuclear fuel. Successor capex for 3 Oct-31 Dec 2016 was $89m, including $41m of nuclear fuel (FY2017 10-K MD&A).
  - Lamar/Forney CCGT acquisition, Apr 2016: $1.313bn aggregate price; $1.343bn cash paid net of cash acquired (Predecessor period).
- **Capex, FY2017-FY2019** (text overrides, built from the separate CF lines in the FY2019 10-K, 0001692819-20-000005):

  | Year | Capex incl. LTSA | Nuclear fuel | Development/growth | Total used |
  |---|---|---|---|---|
  | FY2017 | 114 | 62 | 190 | 366 |
  | FY2018 | 378 | 118 | 34 | 530 |
  | FY2019 | 520 | 89 | 104 | 713 |

  From FY2020 on, the single CF line already includes all three components.
- **Nuclear fuel purchases** (memo; already inside capex):
  - FY2020 88 and FY2021 44 (FY2021 10-K MD&A).
  - FY2022 198, FY2023 214 and FY2024 477 (FY2024 10-K MD&A).
  - FY2025: not separately disclosed in the FY2025 10-K. The 2026 plan is $475m.
- **Acquisitions** (text, CF lines):
  - FY2017: Odessa CCGT, $355m.
  - FY2018: Dynegy, all-stock, with $445m of cash acquired (an inflow).
  - FY2019: Crius $374m plus Ambit $506m.
  - FY2024: Energy Harbor, $3,065m.
  - FY2025: Lotus, $1,140m.
- **SBC FY2017** is 19 (note-disclosed expense). The FY2017 CF statement shows no separate line.
- **2026 YTD:** H1 capex was 1,572. LT debt incl. current was 19,595 at 30 Jun 2026.

### Constellation (CEG)
- The FY2021 10-K (0001868275-22-000020) presents the statements of **Constellation Energy Generation, LLC** (formerly Exelon Generation), because the separation from Exelon took effect 1 Feb 2022. FY2021 equity is therefore member's equity including NCI (11,614).
- **FY2020 comparatives** (Exelon Generation) come from the same filing. Their balance-sheet values (total assets 48,094; cash 226; LTD 5,566 + current 197) were transcribed from the FY2021 10-K balance sheet. FY2020 equity of 14,676 is from XBRL.
- **Debt** is LT debt plus LT debt due within one year:
  - FY2021 also includes $319m of LT debt to affiliates.
  - Short-term borrowings, not included: FY2021 2,082; FY2022 1,159; FY2023 1,644; FY2024 0; FY2025 1,650.
- **Goodwill FY2021** is shown as 47. It is not presented separately on the FY2021 balance sheet; 47 is the 31 Dec 2022 figure in the FY2023 10-K, and no 2022 goodwill addition was found. Treat this cell as an approximation.
- **Intangibles** are finite-lived intangible assets from the notes (XBRL). "Unamortized energy contract assets" are not included.
- **Nuclear fuel** has no separate CF line; it is included in "Capital expenditures". The FY2025 10-K says about 29% of projected 2026/27 capex is nuclear fuel.
- **FY2023 acquisitions of 1,690** are mainly the 44% interest in the South Texas Project, bought from NRG (NRG South Texas LP) on 1 Nov 2023. Net cash paid was $1.65bn (FY2023 10-K).
- **SBC** is the note-disclosed stock-based compensation expense (FY2025: 385).
- **2026 YTD** includes Calpine, from the acquisition date of 7 Jan 2026. YTD goodwill is 11,527; equity is 32,322; LT debt is 19,111 (noncurrent only).

### Talen (TLN)
- **Bankruptcy and deregistration history.**
  - Talen Energy Corp (CIK 1622536) and Talen Energy Supply (CIK 1161976, formerly PPL Energy Supply) filed 10-Ks through FY2015.
  - The Riverstone take-private closed in Dec 2016. Form 15-12B was filed 20 Dec 2016 (Talen Energy Corp) and 16 Dec 2016 (TES).
  - **No Talen 10-K exists for FY2016-FY2023.**
  - TES and 71 subsidiaries filed Chapter 11 on 9 May 2022 (S.D. Tex.), and TEC joined in Dec 2022. The plan was confirmed in Dec 2022, and the companies emerged on **17 May 2023** with fresh-start accounting.
  - Talen re-registered via a Form S-1 (June 2024). Its first 10-K after re-registration is FY2024 (0001628280-25-008786).
- **Comparability.**
  - FY2022 is Predecessor.
  - FY2023 is Predecessor (1 Jan-17 May) plus Successor (18 May-31 Dec), as below. The filing states that Successor periods "are not comparable" with Predecessor periods.
  - FY2024-25 are Successor.
- **FY2023 sums** (FY2024 10-K):

  | Item | Predecessor (1 Jan-17 May) | Successor (18 May-31 Dec) | FY2023 sum |
  |---|---|---|---|
  | Revenue | 1,210 | 1,344 | 2,554 |
  | Operating income | -76 | 160 | 84 |
  | D&A | 200 | 165 | 365 |
  | OCF | 462 | 402 | 864 |
  | Capex | 138 | 116 | 254 |
  | Nuclear fuel | 49 | 45 | 94 |
  | SBC | 0 | 19 | 19 |

  The fresh-start balance sheet at 17 May 2023 (Successor) showed total assets 7,059, cash 169, LTD 2,840 + 5 current, and equity 2,431.
- **FY2022 balance sheet** is not in any filing reviewed except the equity statement, which shows Predecessor total equity of -482 at 31 Dec 2022. The S-1 was not parsed (see Gaps).
- **Goodwill and intangibles:** no goodwill or separately presented intangible line appears on the FY2024 or FY2025 balance sheets. They are shown as 0.
- **FY2025 SBC of 526** includes **501 of liability-classified awards** remeasured at fair value; equity-classified awards were 25 (FY2025 10-K, Note 13).
- **FY2025 acquisitions of 3,793** are the Freedom and Guernsey CCGTs, net of cash acquired.
- **2026 YTD** acquisitions were 2,568.

### Genie (GNE)
- Figures are as filed in each year's 10-K. Genie later recast prior years for discontinued operations. Examples:
  - The FY2025 10-K shows FY2023 operating income of 55.1 and FY2024 of 44.9. As originally filed they were 10.0 and 11.3.
  - FY2020 revenue was 379 as filed and 357 as recast.
- **Debt:**
  - FY2017-20: small revolving lines only (2.5, 2.5, 1.8 plus 0.9 loan, 2.3).
  - FY2016 and FY2021-23: none.
  - FY2024-25: 9.1 and 8.6.
- **FY2025 cells from the 10-K text** (0001437749-26-014294): capex 8.2 and buybacks 8.7 (Class B repurchase program). In addition, employee-related share withholdings were 2.1.
- **Cross-check:** FY2025 OCF of 46,335 thousand on the CF statement, page F-11, equals the XBRL value of 46.3.

### Via Renewables (VIA)
- Figures are as filed. Later 10-Ks recast FY2016-17 for common-control acquisitions; for example, FY2016 total assets were 376 as filed and 368 as recast.
- **Debt** is the Senior Credit Facility (current and long-term) plus subordinated debt from an affiliate plus notes payable:

  | Year | Senior Credit Facility | Subordinated affiliate debt | Note payable | Total |
  |---|---|---|---|---|
  | FY2016 | 51.3 | 5.0 | 15.5 | 71.8 |
  | FY2017 | 125.3 | | 20.5 | 159.2 (incl. note payable) |
  | FY2018 | 129.5 | 10.0 | 6.9 | 146.4 |
  | FY2022 | 100 | 20 | | 120 |

- **Equity** is total equity from each year's balance sheet, excluding the mezzanine Series A preferred.
- **FY2016 intangibles** are customer relationships only (12.1 current + 21.4 noncurrent). Trademarks were not presented separately.
- **D&A** is the income-statement line. The CF add-back also includes customer-acquisition-cost amortization.
- **FY2025 SBC** has no XBRL value (tagged 0); the common stock was taken private in 2024.

## Winter Storm Uri (February 2021)
- **Vistra:**
  - "In February 2021, Winter Storm Uri resulted in a **$2.2 billion negative impact** on the Company's pre-tax earnings in the year ended December 31, 2021, after taking into account approximately **$544 million in securitization proceeds** Vistra expects to receive from ERCOT." (FY2021 10-K, 0001692819-22-000005, MD&A overview.)
  - Adjusted EBITDA excludes $698m of "Winter Storm Uri impacts": default uplift, Koch earn-out accrual, bill credits and legal costs.
  - FY2021 OCF was -$206m, versus +$3,337m in 2020.
- **Just Energy:** the loss led it to seek CCAA/Chapter 15 protection on 9 Mar 2021. It received $147.5m of HB 4492 securitization proceeds in June 2022 (10-K for FY ended 31 Mar 2022, 0001558370-22-012462). The FY ended 31 Mar 2021 operating loss was **-$1,719.7m** (XBRL, same filing).
- **Via:** Q1 2026 Adjusted EBITDA adds back $2.7m for a "non-recurring winter storm loss". This is a 2026 event, not Uri.
- **CEG:** no Uri dollar amount was located in the FY2021 10-K text searched.

## Vistra retail customers (as stated in Item 1 of each 10-K, approximate)

| 10-K for | Total retail customers | ERCOT/Texas | Outside ERCOT |
|---|---|---|---|
| FY2017 | ~1.7m (TXU Energy) | ~1.7m | n/a |
| FY2018 | ~2.8m | ~1.7m | ~1.1m (IL, MA, OH, PA; Dynegy retail) |
| FY2019 | ~4.6m | ~2.3m | ~2.3m (18 states + DC; Crius and Ambit added) |
| FY2020 | ~4.5m | ~2.4m | ~2.1m |
| FY2021 | ~4.3m | ~2.4m | ~1.9m |
| FY2022 | ~3.5m | ~2.4m | ~1.1m |
| FY2023 | ~4m | ~2.5m | n/d |
| FY2024 | ~5m (incl. Energy Harbor) | ~2.6m | n/d |
| FY2025 | ~5m | ~2.6m | n/d |

**Vistra churn statements** ("Competitive retail activity in ERCOT has resulted in retail customer churn..."). Vistra gives net meter-count changes, not an attrition rate:

| 10-K | Statement | Revenue sensitivity |
|---|---|---|
| FY2017 | Customer counts increased slightly in 2017; declined ~1% in 2016 and <1% in 2015 | 1% decline in retail customers = ~$40m annual revenue |
| FY2018 | +2% in 2018 | ~$55m |
| FY2019 | ~+2% in 2019, excluding Ambit and Crius | n/a |
| FY2020 | ~+1% in 2020 | 1% decline in ERCOT customers = ~$57m |
| FY2021 | ~+3% in 2021 | ~$56m |
| FY2022 | ~+3% in 2022 | ~$68m |

The paragraph was not located in the FY2023-FY2025 10-Ks.

## Deals

| Acquirer / target | Date | Consideration | Shares issued | Status | Source |
|---|---|---|---|---|---|
| Vistra / **Dynegy** | Closed 9 Apr 2018 | All-stock merger; exchange ratio 0.652 VST share per Dynegy share; preliminary purchase price ~**$2.3bn** at the Merger Date opening price | **94,409,573** VST shares, plus conversion of options, equity awards, TEUs and warrants | Closed | FY2018 10-K, 0001692819-19-000005 |
| Vistra / **Energy Harbor** | Closed 1 Mar 2024 | Cash **$3.1bn** (CF: $3,065m net of cash acquired) plus a 15% interest in Vistra Vision (FV $1,496m) = total purchase price **$4,596m**; plus FV of NCI in Energy Harbor $811m = acquisition-date FV of **$5,407m** | **None.** Nuveen and Avenue received 15% of the Vistra Vision subsidiary; Vistra later paid $1.748bn (2024) and installments (2025-26) to buy it back | Closed | FY2024 10-K, 0001692819-25-000013, Note 2 |
| Vistra / Cogentrix (5,500 MW gas) | Agreed 31 Dec 2025 | ~$2.3bn cash, net of ~$1.5bn of assumed debt | 5,000,000 VST shares at an agreed $185 | Pending at the H1 2026 10-Q; FERC approved Aug 2026; close expected late 2026 | 0001692819-26-000019 |
| CEG / **Calpine** | Closed 7 Jan 2026 | Purchase price ~**$21.8bn** (total merger consideration $21,835m): ~50 million CEG shares (FV $17,603m at $354.58) plus cash of $4,342m (base $4.5bn less adjustments); $2,290m of Calpine notes exchanged for CEG notes; cash outflow net of cash acquired $2,537m in H1 2026 | ~**50 million** | Closed. Six generating assets held for sale for regulatory divestiture | CEG Q2 2026 10-Q, 0001868275-26-000104, Note 2 |
| CEG / NRG's 44% of STP | Closed 1 Nov 2023 | Net cash $1.65bn | None | Closed | FY2023 10-K, 0001868275-24-000014 |
| Retailco (K. Maxwell) / Via Class A common | Closed 13 Jun 2024 | $11.00 per Class A share | n/a | Common delisted from NASDAQ. Series A preferred stayed listed until Form 25 / Form 15 on 1 Jul 2026 | VIA FY2024 10-K; Form 15, 0001606268-26-000040 |

## Listed retail-energy companies: customer KPIs

**Genie Energy (GRE segment), year-end**

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Meters (k) | 412 | 412 | 315 | 370 | 370 | 285 | 275 | 361 | 423 | 346 |
| of which electric (k) | 296 | 307 | 245 | 297 | 305 | 210 | 196 | 279 | 333 | 258 |
| RCEs (k) | 283 | 301 | 253 | 309 | 337 | 260 | 262 | 350 | 399 | 329 |
| Average monthly churn | 6.0% | 6.6% | 6.5% | 5.3% | 4.4% | 5.7% | 4.8% | 4.9% | 5.4% | 6.0% |

Genie's 10-Ks state that GRE's REPs' "monthly churn rates average between four and seven percent per month" (FY2016-18: "four and eight"). Its stated churn drivers include commodity prices, weather-driven consumption and expiry of municipal aggregation contracts. The FY2016 10-K gives 6.3% for 2015, while the FY2017 10-K gives 5.4% for 2015 and 6.0% for 2016; both are as filed. Genie does not disclose gross margin per unit; it discloses a gross-margin percentage.

**Via Renewables / Spark Energy, year-end**

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| RCEs total (k) | 774 | 1,042 | 908 | 672 | 400 | 408 | 331 | 335 | 388 | 421 |
| of which electricity (k) | 571 | 868 | 754 | 533 | 303 | 298 | 201 | 217 | 232 | 225 |
| RCE attrition, average monthly | 4.3% | 4.3% | 4.7% | 5.0% | 5.0% | 3.3% | 3.8% | 3.4% | 3.9% | 4.2% |
| Retail gross margin, $m | 182.4 | 224.5 | 185.1 | 220.7 | 196.5 | 132.5 | 114.8 | 136.7 | 142.0 | 149.8 |
| Electricity margin, $/MWh | 28.33 | 23.46 | 14.44 | 25.02 | 35.37 | 35.86 | 34.00 | 43.59 | 46.02 | 42.40 |
| Gas margin, $/MMBtu | 3.82 | 3.63 | 3.60 | 4.14 | 4.80 | 4.24 | 2.77 | 4.22 | 4.12 | 3.30 |

In Q1 2026, electricity margin was $13.89/MWh versus $38.40 in Q1 2025, and average monthly customer attrition was 4.5%. Retail gross margin is a non-GAAP measure.

**Just Energy:** at 31 Mar 2022 it had ~2,755,000 RCEs (44% mass market). The mass-market attrition rate for the trailing 12 months was **18%**, up three percentage points; quarterly mass-market attrition was 4% and commercial 2%.

## Other SEC-filing retail electricity providers active 2016-2025 (EDGAR company search)

| Company | CIK | Filing record | Notes |
|---|---|---|---|
| Summer Energy Holdings (Houston, TX REP) | 1396633 | 10-Ks through FY2019 (0001445866-20-000261); Form 15-12B on 5 Feb 2021 | FY2016-19 revenue $90.2m / 117.7 / 151.9 / 166.3m; operating income 0.0 / 2.6 / -6.3 / -8.8; OCF -0.9 / -1.8 / -10.4 / -9.8 (XBRL) |
| Just Energy Group (Canada/US) | 1538789 | 40-F (IFRS, CAD) through FY Mar-2021; one 10-K for FY ended 31 Mar 2022 (0001558370-22-012462) and two 10-Qs; Form 15-12G on 19 Dec 2022 | US GAAP revenue $2,371.7m / 2,074.8 / 2,154.6m (FY Mar-2020/21/22); operating income 84.9 / -1,719.7 / 39.3; OCF 24.8 / 12.4 / -35.1 |
| Calpine Corp (owner of Calpine Energy Solutions retail) | 916457 | 10-Ks through FY2019 (0000916457-20-000007); 15-12B Jan 2019; last 10-Q Aug 2020 | Taken private 2018; acquired by CEG Jan 2026 |
| FirstEnergy Solutions Corp (later Energy Harbor) | 1407703 | 10-Ks through FY2017; Form 15-12G Apr 2018 | Energy Harbor itself was **not an SEC filer**; acquired by Vistra 2024 |
| Crius Energy Trust | n/a | **Not an SEC filer** (Canadian TSX-listed trust; no EDGAR company found) | Acquired by Vistra Jul 2019 for $400m |
| Ambit Energy | n/a | **Not an SEC filer** (only match was an unrelated biotech) | Acquired by Vistra 2019 |
| Direct Energy (Centrica subsidiary) | n/a | **Not an SEC filer** (no EDGAR registrant found) | Named as a competitor in Via 10-Ks. Its acquisition by NRG is not described in the filings read here. |

## Large private Texas / retail electricity providers named in the filings read

- **Not SEC filers:**
  - Direct Energy, Inc. Via's 10-Ks for FY2016-19 name it among "larger, well-capitalized energy retailers".
  - Calpine Energy Solutions, LLC. Named in Via's 10-Ks from FY2018/FY2019 through FY2025; private since 2018 and now owned by CEG.
  - Energy Harbor and Ambit (pre-acquisition).
- **SEC filers named as competitors** in Via 10-Ks: FirstEnergy Solutions (FY2016 list) and Just Energy Group (FY2016-17). Both deregistered later (see above).
- Vistra's 10-Ks do not name competing REPs. Its own Texas brands (TXU Energy, 4Change Energy, Express Energy, Veteran Energy, Ambit Texas, TriEagle) are subsidiaries.
- Searches of the downloaded 10-Ks for Gexa, Green Mountain, Champion Energy, Octopus, Rhythm, Chariot, Tara, Pulse Power, Frontier Utilities, Cirro, Griddy, Shell Energy, Payless Power, Discount Power, Infinite Energy and APG&E found **no mentions**. No further private Texas REPs can be listed from these filings.

## Cross-check: one filed statement figure per company (XBRL value = statement text)

| Company | Figure | XBRL value | Statement text | Location in filing |
|---|---|---|---|---|
| VST | FY2025 cash from operations | 4,070 | "Cash provided by operating activities \| 4,070 \| 4,563 \| 5,453" | FY2025 10-K (0001692819-26-000006, vistra-20251231.htm), Consolidated Statements of Cash Flows, p. 82 |
| CEG | FY2025 OCF | 4,237 | "Net cash flows provided by (used in) operating activities \| 4,237 \| (2,464) \| (5,301)" | FY2025 10-K (0001868275-26-000032, ceg-20251231.htm), Consolidated Statements of Cash Flows, p. 88 |
| TLN | FY2025 OCF | 704 | "Net cash provided by (used in) operating activities \| 704 \| 256 \| 402 \| 462" | FY2025 10-K (0001622536-26-000017, tln-20251231.htm), Consolidated Statements of Cash Flows, p. 54 |
| GNE | FY2025 OCF | 46.3 | "Net cash provided by operating activities \| 46,335 \| 70,742 \| 62,478" (thousands) | FY2025 10-K (0001437749-26-014294), Consolidated Statements of Cash Flows, p. F-11 |
| VIA | FY2025 revenue | 463.5 | "Total revenues \| 463,451 \| 398,868 \| 435,192" (thousands) | FY2025 10-K (0001606268-26-000013, spke-20251231.htm), Consolidated Statements of Operations, p. 72 |

All five matched exactly.

## Accession numbers used (primary documents downloaded and read)

- **VST 10-K:**
  - FY2017 0001692819-18-000018
  - FY2018 0001692819-19-000005
  - FY2019 0001692819-20-000005
  - FY2020 0001692819-21-000004
  - FY2021 0001692819-22-000005
  - FY2022 0001692819-23-000005
  - FY2023 0001692819-24-000012
  - FY2024 0001692819-25-000013
  - FY2025 0001692819-26-000006
- **VST 10-Q:** Q2 2026 0001692819-26-000019
- **CEG 10-K:**
  - FY2021 0001868275-22-000020
  - FY2022 0001868275-23-000014
  - FY2023 0001868275-24-000014
  - FY2024 0001868275-25-000023
  - FY2025 0001868275-26-000032
- **CEG 10-Q:** Q2 2026 0001868275-26-000104
- **TLN 10-K:**
  - FY2015 0001622536-16-000111 (XBRL only)
  - FY2024 0001628280-25-008786
  - FY2025 0001622536-26-000017
- **TLN 10-Q:** Q2 2026 0001622536-26-000066
- **TLN Form 15-12B:** 0001193125-16-798892
- **TES Form 15-12B:** 0001193125-16-795928
- **TLN S-1 filings:** 0001628280-24-029107 and 0001628280-24-031004 (listed only; not parsed)
- **GNE 10-K:**
  - FY2016 0001213900-17-002459
  - FY2017 0001213900-18-003067
  - FY2018 0001213900-19-004396
  - FY2019 0001213900-20-006416
  - FY2020 0001213900-21-015538
  - FY2021 0001213900-22-012716
  - FY2022 0001213900-23-020226
  - FY2023 0001213900-24-022573
  - FY2024 0001213900-25-024009
  - FY2025 0001437749-26-014294
- **GNE 10-Q:** Q2 2026 0001437749-26-026209
- **VIA 10-K:**
  - FY2016 0001606268-17-000012
  - FY2017 0001606268-18-000017
  - FY2018 0001606268-19-000008
  - FY2019 0001606268-20-000008
  - FY2020 0001606268-21-000015
  - FY2021 0001606268-22-000008
  - FY2022 0001606268-23-000009
  - FY2023 0001606268-24-000008
  - FY2024 0001606268-25-000006
  - FY2025 0001606268-26-000013
- **VIA 10-K/A** (Part III only; not used for figures):
  - FY2023 0001606268-24-000011
  - FY2024 0001606268-25-000011
  - FY2025 0001606268-26-000020
- **VIA last periodic report:** Q1 2026 10-Q 0001606268-26-000024
- **VIA Form 15:** 0001606268-26-000040 (1 Jul 2026)
- **Just Energy 10-K:** 0001558370-22-012462
- **Summer Energy 10-K FY2019:** 0001445866-20-000261 (XBRL)
- **Calpine 10-K FY2019:** 0000916457-20-000007 (listing only)
- **FirstEnergy Solutions 10-K FY2017:** 0001031296-18-000015 (listing only)
- **XBRL company-facts API:** CIK0001692819, CIK0001868275, CIK0001622536, CIK0001528356, CIK0001606268, CIK0001396633, CIK0001538789

Raw files are in `cache/comp/` (JSON, HTML and text). The scripts are in `comp_scripts/` (`extract.py`, `build.py`, `tables.py`).

## Gaps (what could not be obtained, and why)

1. **Vistra FY2016:** no 12-month income or cash-flow figures exist, because of the 3 Oct 2016 emergence and the Predecessor/Successor split. FY2016 ratios are n/a.
2. **Vistra FY2025 nuclear fuel purchases:** not separately disclosed in the FY2025 10-K. From FY2023 on, the 10-Ks give only an approximate total retail customer count (rounded to millions), with no non-Texas split.
3. **Vistra churn:**
   - The 10-Ks do not give a retail attrition rate as a percentage. They give only net meter-count changes (FY2017-FY2022 10-Ks).
   - No such statement was located in the FY2023-25 10-Ks.
4. **CEG:**
   - No Form 10-K exists for FY2016-2020 under CIK 1868275. Exelon Generation's own earlier 10-Ks (combined Exelon filings) were not used, since the scope was CEG's own 10-Ks.
   - FY2021 goodwill is approximated at 47.
   - No separate nuclear-fuel capex figure is given on the CF statement.
   - OCF in FY2021-24 is depressed by the classification of receivable (DPP) collections in investing; see the memo above.
5. **Talen:**
   - No SEC periodic reports exist for FY2016-FY2021 (private after Dec 2016). FY2022 figures come only as Predecessor comparatives in the FY2024 10-K.
   - The FY2022 balance sheet was not available in the filings parsed. It is likely in the 2024 S-1, which was not parsed.
   - FY2023 is a non-comparable sum of the Predecessor and Successor periods.
   - Talen disclosed no retail customer metrics.
6. **Genie:**
   - Figures are as filed; later 10-Ks recast them (discontinued operations), which materially changes FY2023-24 operating income in the FY2025 10-K.
   - The H1 2026 YTD capex was not in XBRL, so the YTD Ratio 2 is n/a.
   - No gross margin per unit is disclosed.
7. **Via:**
   - The common stock was taken private in June 2024. Reporting continued for the preferred stock until the Form 15 of 1 Jul 2026, so the last periodic report is the Q1 2026 10-Q.
   - FY2025 and Q1 2026 SBC is not reported in XBRL.
8. **Just Energy:**
   - Its filings before FY Mar-2022 are IFRS/CAD 40-Fs, and no US GAAP annual series exists before then.
   - Its Uri loss is not given as a single dollar figure in the 10-K text searched.
9. **Private Texas REPs:** the 10-Ks reviewed name few competitors. A broader list (for example from NRG's own 10-K risk factors) was outside the files allowed.
10. **Comparability caveats:**
    - D&A definitions differ: CEG and TLN exclude nuclear-fuel amortization from income-statement D&A.
    - Intangibles: CEG uses finite-lived intangibles only, and TLN shows none.
    - Equity: Vistra's equity includes preferred stock classified in equity.
