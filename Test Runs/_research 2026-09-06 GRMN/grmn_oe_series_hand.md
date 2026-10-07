# GRMN owner-earnings inputs, hand-transcribed from filed cash-flow statements
All $000. Construction: OE = OCF − stock compensation − purchases of property and equipment
(capex end); D&A end shown for the band. Working-capital increment inside OCF by
construction (CONVENTION, [E2-23] constraint 3).

## Sources (document · date · accession)
- 10-K FY2025 (FYE 2025-12-27), filed 2026-02-18, acc 0001193125-26-056028 — years FY2025/24/23
- 10-K FY2022 (FYE 2022-12-31, 53 weeks), filed 2023-02-22, acc 0000950170-23-003566 — years FY2022/21/20
- 10-K FY2019 (FYE 2019-12-28), filed 2020-02-19, acc 0001564590-20-005133 — years FY2019/18/17
- 10-K FY2016 (FYE 2016-12-31, 53 weeks), filed 2017-02-22, acc 0001615774-17-000765 — years FY2016/15/14
- 10-Q Q2-2026 (26 weeks ended 2026-06-27), filed 2026-07-29, acc 0001193125-26-322114 — H1-2026/H1-2025

## The series
| FY | OCF | SBC | Capex | Depreciation | Amortization | OE (capex end) | OE (D&A end) |
|---|---|---|---|---|---|---|---|
| 2014 | 522,711 | 24,293 | 73,339 | 48,433 | 28,582 | 425,079 | 421,403 |
| 2015 | 280,467 | 26,290 | 80,592 | 51,311 | 27,049 | 173,585 | 175,817 |
| 2016 | 705,682 | 41,250 | 90,960 | 55,796 | 30,544 | 573,472 | 578,092 |
| 2017 | 660,842 | 44,735 | 139,696 | 59,895 | 26,357 | 476,411 | 529,855 |
| 2018 | 919,520 | 56,391 | 155,755 | 64,798 | 31,396 | 707,374 | 766,935 |
| 2019 | 698,549 | 63,400 | 118,031 | 71,921 | 34,254 | 517,118 | 528,974 |
| 2020 | 1,135,267 | 80,885 | 185,401 | 78,121 | 48,594 | 868,981 | 927,667 |
| 2021 | 1,012,427 | 92,522 | 307,645 | 103,498 | 51,320 | 612,260 | 765,087 |
| 2022 | 788,259 | 76,801 | 244,286 | 118,743 | 45,110 | 467,172 | 547,605 |
| 2023 | 1,376,265 | 101,422 | 193,524 | 132,347 | 45,225 | 1,081,319 | 1,097,271 |
| 2024 | 1,432,471 | 137,162 | 193,571 | 140,494 | 39,241 | 1,101,738 | 1,115,574 |
| 2025 | 1,633,359 | 166,003 | 270,446 | 152,611 | 36,148 | 1,196,910 | 1,278,597 |
| H1-2026 | 939,544 | 88,793 | 194,395 | 81,270 | 16,711 | 656,356 | 741,563 |
| H1-2025 | 593,959 | 82,279 | 85,738 | 75,980 | 17,423 | 425,942 | 418,133 |

## Windows (capex end, $M) — computed by hand
- 3-yr FY2023-25: 1,126.7
- 5-yr FY2021-25: 891.9  ← reproduces the screen's oe_bottom 892
- 10-yr FY2016-25: 760.3
- 12-yr FY2014-25: 683.5
- leave-two-out (10-yr less the two best years 2024, 2025): 663.0
- 3-yr depreciation-only end (OCF−SBC−dep only): FY2023 1,142.5 / FY2024 1,154.8 /
  FY2025 1,314.7 → mean 1,204.0 ← reproduces the screen's oe_top 1,204, which is
  run.py's KNOWN depreciation-only defect (amortization excluded). True 3-yr D&A end: 1,163.8.

## Named distortions in the window [E4-41]
- FY2015 DOWN: $182.8M cash tax paid Q2-2015 for the 2014 inter-company restructuring
  (FY2016 10-K MD&A, verbatim: "The cash tax payments of $78.1 million and $182.8 million
  associated with the restructuring were made in the third quarter of 2014 and the second
  quarter of 2015, respectively."). Also a $121.7M inventory build.
- FY2019 DOWN: working-capital build (OCF $698.5M against net income $952.5M).
- FY2021-22 DOWN: COVID-era inventory builds; FY2021 capex spike $307.6M (facility
  expansion); FY2022 fitness collapse (segment OI $359.2M → $104.7M).
- FY2023-25 UP: the step the screen flags (level_shift 1.7, "STEP UP - normalize down
  [E4-41]") — fitness recovery + record deliveries; inventory drawdown FY2023; FY2025 OCF
  includes favorable timing (to be checked against cash taxes paid).
- FY2025 capex $270.4M vs D&A $188.8M (1.43x): growth component to be judged at (c).
