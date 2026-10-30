# QCOM — Stage 0 research, 2026-09-02
*Written to disk as gathered, per the WRITE-EARLY PROTOCOL.*

## SOVEREIGN — issuing authority

**U.S. Department of the Treasury, Daily Treasury Par Yield Curve Rates**, fetched
2026-09-02 from `home.treasury.gov` (`daily-treasury-rates.csv/2026/all`). Latest published
row is **2026-09-01**.

| date | 30 Yr | 20 Yr | 10 Yr |
|---|---|---|---|
| **2026-09-01** | **5.27** | 5.27 | 4.79 |
| 2026-08-31 | 5.25 | 5.24 | 4.75 |
| 2026-08-28 | 5.22 | 5.21 | 4.73 |
| 2026-08-27 | 5.19 | 5.18 | 4.67 |
| 2026-08-26 | 5.18 | 5.17 | 4.66 |

**Sovereign used: 5.27%, 2026-09-01, U.S. Treasury.** (The screen's 5.18% was the
2026-08-26 print; the run uses the current observation **[E4-15, E3-32]**.)
`tools/sources.py` returned `USD FAILED: The read operation timed out` on the FRED path —
FRED is the fallback and it was down; the issuing authority was used, which is UP the
evidence ladder, exactly as the PLAB run of 2026-09-01 recorded.

## THE FILING

- **Form 10-K, fiscal year ended 2025-09-28, filed 2025-11-05, accession
  `0000804328-25-000085`, primary document `qcom-20250928.htm`.** CIK 0000804328,
  QUALCOMM INC/DE, SIC 3663, FYE 09-27/28.
- Most recent periodic filing in existence at run date: **Form 10-Q for the quarter ended
  2026-06-28, filed 2026-07-29, accession `0000804328-26-000086`** (Q3 FY2026).
- Prior 10-Ks used for the window: FY2024 `0000804328-24-000075`; FY2023
  `0000804328-23-000055`; FY2022 `0000804328-22-000021`; FY2021 `0001728949-21-000076`;
  FY2020 `0001728949-20-000067`; FY2019 `0001728949-19-000072`.

## STAGE 0 — ARTIFACT CHECK: the screen's nine-year series, recomputed

Construction: **operating cash flow − share-based compensation − payments to acquire
productive assets (capex)**, $M, from the filed consolidated statements of cash flows
(SEC XBRL `NetCashProvidedByUsedInOperatingActivities`, `ShareBasedCompensation`,
`PaymentsToAcquireProductiveAssets`, all 10-K/FY-tagged).

| FY (end) | OCF | SBC | capex | **filed OE** | **screen** | D&A |
|---|---|---|---|---|---|---|
| 2017 (09-24) | 4,693 | 914 | 690 | **3,089** | 3,089 | 1,461 |
| 2018 (09-30) | 3,895 | 883 | 784 | **2,228** | 2,228 | 1,561 |
| 2019 (09-29) | 7,286 | 1,037 | 887 | **5,362** | 5,362 | 1,401 |
| 2020 (09-27) | 5,814 | 1,212 | 1,407 | **3,195** | 3,195 | 1,393 |
| 2021 (09-26) | 10,536 | 1,663 | 1,888 | **6,985** | 6,985 | 1,582 |
| 2022 (09-25) | 9,096 | 2,031 | 2,262 | **4,803** | 4,803 | 1,762 |
| 2023 (09-24) | 11,299 | 2,484 | 1,450 | **7,365** | 7,365 | 1,809 |
| 2024 (09-29) | 12,202 | 2,648 | 1,041 | **8,513** | 8,513 | 1,706 |
| 2025 (09-28) | 14,012 | 2,783 | 1,192 | **10,037** | 10,037 | 1,602 |

**All nine years reconcile to the dollar.** *(Note: FY2017 and FY2018 OCF carry two tagged
values each — 4,693/5,001 and 3,895/3,908 — from a later reclassification. The screen used
the earlier-filed figures and so does this run; the alternative moves FY2017 by +308 and
FY2018 by +13 and moves no verdict.)*

**capex/D&A:** nine-year mean capex 1,289.0 ÷ nine-year mean D&A 1,586.3 = **0.813x**.
The operator's 0.81x is confirmed. **capex is BELOW D&A**, so the **D&A end of the band is
the LOW (conservative) end** — the reverse of the PLAB case. Stated rather than assumed.

## THE SCREEN'S BOTTOM BOUNDARY, REPRODUCED EXACTLY

$7,415M = the **five-year (FY2021–25) mean of OCF − SBC − D&A**:
7,291 / 5,303 / 7,006 / 7,848 / 9,627 → 37,075 ÷ 5 = **7,415.0**. ✓
Yield 7,415 ÷ 172,263 = **4.305%** ✓ ("bottom yield 4.30%").
Growth for the [E4-28] 10% floor: 10.00 − 4.30 = **5.70%** ✓.

## OTHER FILED SERIES (10-K/FY XBRL, $M)

| FY | Revenues | Operating income | Pretax (EBT) | Net income | R&D | Buybacks |
|---|---|---|---|---|---|---|
| 2016 | 23,554 | 6,495 | 6,833 | 5,705 | 5,151 | 3,923 |
| 2017 | 22,258 | 2,581 | 2,987 | 2,445 | 5,485 | 1,342 |
| 2018 | 22,611 | 621 | 392 | **−4,964** | 5,625 | **22,580** |
| 2019 | 24,273 | 7,667 | 7,481 | 4,386 | 5,398 | 1,793 |
| 2020 | 23,531 | 6,255 | 5,719 | 5,198 | 5,975 | 2,450 |
| 2021 | 33,566 | 9,789 | 10,274 | 9,043 | 7,176 | 3,366 |
| 2022 | 44,200 | 15,860 | 14,998 | 12,936 | 8,194 | 3,129 |
| 2023 | 35,820 | 7,788 | 7,443 | 7,232 | 8,818 | 2,973 |
| 2024 | 38,962 | 10,071 | 10,336 | 10,142 | 8,893 | 4,121 |
| 2025 | 44,284 | 12,355 | 12,663 | **5,541** | 9,042 | **8,791** |

**FY2025 pretax 12,663 against net income 5,541 — a $7.1bn tax charge.** Flagged for
reading in the filing. **FY2018 net income −4,964 on revenues of 22,611** — the Tax Act
charge, the NXP break fee and the fines year, also flagged.

## SEGMENTS — FY2023–25, from Note 8 of the FY2025 10-K (verbatim table, $M)

| | 2025 | 2024 | 2023 |
|---|---|---|---|
| **QCT revenues** | 38,367 | 33,196 | 30,382 |
| QCT cost of revenues | 19,302 | 16,648 | 15,367 |
| QCT opex (R&D and SG&A) | 7,395 | 7,021 | 7,091 |
| **QCT EBT** | **11,670** | **9,527** | **7,924** |
| **QTL revenues** | 5,582 | 5,572 | 5,306 |
| QTL costs and expenses | 1,539 | 1,545 | 1,678 |
| **QTL EBT** | **4,043** | **4,027** | **3,628** |
| QSI revenues | — | 18 | 28 |
| **QSI EBT** | 180 | 104 | (12) |
| **Reportable segment revenues** | 43,949 | 38,786 | 35,716 |
| **Reportable segment EBT** | **15,893** | **13,658** | **11,540** |
| Consolidated revenues | 44,284 | 38,962 | 35,820 |
| **Consolidated EBT** | **12,663** | **10,336** | **7,443** |

Reconciling items FY2025: nonreportable segments (39); unallocated revenues 143;
unallocated cost of revenues (270); unallocated R&D (2,357); unallocated SG&A (783);
unallocated other expense (39); unallocated interest expense (664); unallocated investment
and other income, net 779.

**FY2025 margins: QCT EBT 30.4% of QCT revenue; QTL EBT 72.4% of QTL revenue.**
**QTL is 12.6% of revenue and 25.4% of reportable-segment EBT.**

Verbatim, Note 8: *"Substantially all of QTL's costs and expenses are comprised of
operating expenses."* And: *"Unallocated revenues in fiscal 2025 were comprised of
licensing revenues resulting from a recent settlement of a licensing dispute."*

## REVENUE BY COUNTRY — Note 8, FY2025 10-K ($M)
*"We report revenues by country based on our customer's/licensee's headquarters."*

| | 2025 | % | 2024 | % | 2023 | % |
|---|---|---|---|---|---|---|
| **China (incl. Hong Kong)** | **20,340** | **46%** | 17,826 | 46% | 13,386 | 37% |
| United States | 10,515 | 24% | 9,686 | 25% | 10,503 | 29% |
| **South Korea** | **9,542** | **21%** | 7,995 | 20% | 8,075 | 23% |
| Other foreign | 3,887 | 9% | 3,455 | 9% | 3,856 | 11% |

## ACQUISITIONS — Note 9, FY2025 10-K
- Pending: **Alphawave IP Group plc, implied enterprise value ~$2.4 billion** announced
  2025-06-09, cash or stock consideration, *"expected to complete during the first quarter
  of calendar 2026"*; **$2.3 billion of cash restricted** on the balance sheet for it.
- Completed FY2025: *"we acquired seven businesses for a total accounting purchase price of
  $668 million"*, $122M intangibles + **$526M goodwill, all allocated to QCT**, *"primarily
  attributable to assembled workforce and certain synergies"*.
