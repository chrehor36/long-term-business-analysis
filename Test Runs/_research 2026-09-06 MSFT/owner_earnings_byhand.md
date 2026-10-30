# MSFT owner earnings — built by hand from the filed cash-flow statements
Analyst's own arithmetic, 2026-09-06. Nine 10-K vintages read.
Construction (project CONVENTION): **OCF − SBC − (c)**, where (c) is either total capex
("capex end") or D&A ("D&A end"). All figures $M, fiscal years ended June 30.

## SOURCE VINTAGES AND CROSS-CHECKS
| vintage | accession | years it carries |
|---|---|---|
| FY2026 10-K | 0001193125-26-323660 (filed 2026-07-29) | FY2026, 2025, 2024 |
| FY2025 10-K | 0000950170-25-100235 | FY2025, 2024, 2023 |
| FY2024 10-K | 0000950170-24-087843 | FY2024, 2023, 2022 |
| FY2023 10-K | 0000950170-23-035122 | FY2023, 2022, 2021 |
| FY2022 10-K | 0001564590-22-026876 | FY2022, 2021, 2020 |
| FY2021 10-K | 0001564590-21-039151 | FY2021, 2020, 2019 |
| FY2020 10-K | 0001564590-20-034944 | FY2020, 2019, 2018 |
| FY2019 10-K | 0001564590-19-027952 | FY2019, 2018, 2017 |
| FY2017 10-K | 0001564590-17-014900 | FY2017, 2016, 2015 |
| FY2014 10-K | 0001193125-14-289961 | FY2014, 2013, 2012 |

**Cross-vintage checks run and PASSED (identical to the dollar):** FY2017 OCF 39,507
(FY2017 and FY2019 vintages); FY2018 OCF 43,884 and FY2019 OCF 52,185 (FY2019 and FY2020
vintages); FY2024 capex 44,477 (FY2024 and FY2026 vintages).

**FLAG — the FY2026 10-K states a recast:** *"recast of these prior period cash flows
statements to conform to the current period presentation."* The recast did not move any of
the four lines used here (checked FY2024 and FY2025 against the FY2025/FY2024 vintages).

## THE FILED SERIES
| FY | OCF | SBC | capex | D&A ("Depreciation, amortization, and other") | revenue |
|---|---|---|---|---|---|
| 2012 | 31,626 | 2,244 | 2,305 | 2,967 | |
| 2013 | 28,833 | 2,406 | 4,257 | 3,755 | |
| 2014 | 32,231 | 2,446 | 5,485 | 5,212 | |
| 2015 | 29,668 | 2,574 | 5,944 | 5,957 | |
| 2016 | 33,325 | 2,668 | 8,343 | 6,622 | |
| 2017 | 39,507 | 3,266 | 8,129 | 8,778 | |
| 2018 | 43,884 | 3,940 | 11,632 | 10,261 | |
| 2019 | 52,185 | 4,652 | 13,925 | 11,682 | |
| 2020 | 60,675 | 5,289 | 15,441 | 12,796 | |
| 2021 | 76,740 | 6,118 | 20,622 | 11,686 | |
| 2022 | 89,035 | 7,502 | 23,886 | 14,460 | |
| 2023 | 87,582 | 9,611 | 28,107 | 13,861 | |
| 2024 | 118,548 | 10,734 | 44,477 | 20,958 | 245,122 |
| 2025 | 136,162 | 11,974 | 64,551 | 29,433 | 281,724 |
| 2026 | 182,935 | 12,405 | 115,948 | 38,534 | 331,839 |

**READ THE D&A COLUMN.** It FELL in FY2021 (11,686 vs 12,796) while capex rose 34%, and
FELL again in FY2023 (13,861 vs 14,460) while capex rose 18%. Depreciation going DOWN in a
year the fleet grew a third is not an accident of mix. It is the two useful-life extensions.

## OWNER EARNINGS BY YEAR
| FY | capex end (OCF−SBC−capex) | D&A end (OCF−SBC−D&A) | gap |
|---|---|---|---|
| 2012 | 27,077 | 26,415 | 662 |
| 2013 | 22,170 | 22,672 | (502) |
| 2014 | 24,300 | 24,573 | (273) |
| 2015 | 21,150 | 21,137 | 13 |
| 2016 | 22,314 | 24,035 | (1,721) |
| 2017 | 28,112 | 27,463 | 649 |
| 2018 | 28,312 | 29,683 | (1,371) |
| 2019 | 33,608 | 35,851 | (2,243) |
| 2020 | 39,945 | 42,590 | (2,645) |
| 2021 | 50,000 | 58,936 | (8,936) |
| 2022 | 57,647 | 67,073 | (9,426) |
| 2023 | 49,864 | 64,110 | (14,246) |
| 2024 | 63,337 | 86,856 | (23,519) |
| 2025 | 59,637 | 94,755 | (35,118) |
| 2026 | 54,582 | 131,996 | **(77,414)** |

**THE GAP IS THE FILE.** For a decade to FY2020 the two ends of the band agreed to within
~$2.6bn. From FY2021 they diverge, and in FY2026 alone the gap is **$77.4bn** — three times
ORCL's entire ~$25bn band width, which the queue called "the AI-datacentre capex question."

## WINDOWS
| window | capex end | D&A end |
|---|---|---|
| 3-yr FY2024-26 | **59,185** | **104,536** |
| 5-yr FY2022-26 | **57,013** | **88,958** |
| 8-yr FY2019-26 | 51,078 | 78,272 |
| 10-yr FY2017-26 | **46,504** | 63,931 |
| 15-yr FY2012-26 | 38,857 | 51,876 |
| FY2026 alone (best year) | 54,582 | 131,996 |

## SCREEN ROW — REPRODUCTION
`Screens/2026-09-01 FLOOR SCREEN.csv`: `MSFT,3811904,57013,59185,0.038,...`
- oe_bottom **57,013** = my 5-yr FY2022-26 capex end, **57,013.4 — reproduced to the decimal**
- oe_top **59,185** = my 3-yr FY2024-26 capex end, **59,185.3 — reproduced to the decimal**
- spread 0.038 = (59,185−57,013)/57,013 = **3.81% — reproduced**
**The 2026-09-01 screen row reproduces exactly. Both its ends are CAPEX-end figures; it never
displayed a D&A end at all, so its 3.8% "spread" is not the band — it is two capex windows.**

`Screens/2026-09-04 FLOOR SCREEN.csv` and `2026-09-02 MASTER RUN QUEUE (corrected).csv`:
`oe_bottom 40,268 · oe_top 110,344 · spread 1.74`.
**NOT REPRODUCED.** Neither end matches any window at either capex end on my series
(nearest: 40,268 sits between my 13-yr 40,985 and 14-yr 39,641 capex-end means; 110,344
matches no window — my 3-yr D&A end is 104,536 and my 2-yr is 113,376). Recorded as a
**fourth screen spread that failed to reproduce**. My hand series governs.

## THE HEADLINE ARITHMETIC
Cap $3,710,545M (7,425,545,491 shares × $499.70).
| construction | owner earnings | yield | vs sovereign 5.24% |
|---|---|---|---|
| 15-yr capex end | 38,857 | 1.05% | −4.19 |
| 10-yr capex end | 46,504 | 1.25% | −3.99 |
| 5-yr capex end | 57,013 | 1.54% | −3.70 |
| 3-yr capex end | 59,185 | 1.60% | −3.64 |
| 10-yr D&A end | 63,931 | 1.72% | −3.52 |
| 5-yr D&A end | 88,958 | 2.40% | −2.84 |
| 3-yr D&A end | 104,536 | 2.82% | −2.42 |
| **FY2026 alone, D&A end — the single most generous number that exists** | **131,996** | **3.56%** | **−1.68** |

**Every construction, on every window, at both ends of the capex band, is below the
30-year Treasury.** The most generous number constructible — the single best year in company
history valued as though depreciation fully replaces a fleet whose replacement bill is three
times depreciation — still pays 1.68 points LESS than a government bond.
