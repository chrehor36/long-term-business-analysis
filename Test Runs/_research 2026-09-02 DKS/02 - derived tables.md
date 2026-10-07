# DKS — derived tables
Everything here is arithmetic on the figures in `01 - filed figures, transcribed.md`,
`03 - competitor row, attacker metric.md` and `04 - Foot Locker standalone, from its own
10-Ks.md`. No new source data. Reproduce with the formulas stated.

## 1. OWNER EARNINGS — the project's CONVENTION
    OE = operating cash flow − stock-based compensation − (c)
    (c) shown at BOTH ends of the corpus band: D&A [E3-44, E2-41] and total capex.

**Landlord construction allowances are inside operating cash flow and capex is taken gross,
so the pair nets once and correctly. The company's own "net capital expenditures" is NOT
used — it would double-count the allowance.** Allowances: $67.1M (FY2023), $76.3M (FY2024),
$161.7M (FY2025).

### DICK'S standalone, $M
| FY | OCF | SBC | D&A | capex | **OE (D&A end)** | **OE (capex end)** |
|---|---:|---:|---:|---:|---:|---:|
| 2021 | 1,616.9 | 52.8 | 322.6 | 308.3 | 1,241.5 | 1,255.8 |
| 2022 | 921.9 | 50.6 | 365.5 | 364.1 | 505.8 | 507.2 |
| 2023 | 1,527.3 | 57.3 | 393.9 | 587.4 | 1,076.1 | 882.6 |
| 2024 | 1,311.8 | 71.0 | 400.4 | 802.6 | 840.4 | 438.2 |
| 2025 | 1,537.3 | 123.7 | 488.6 | 1,137.2 | 925.0 | 276.4 |

**Screen reproduction check.** 3y capex mean **532.4** (screen 532) · 5y capex **672.0**
(screen 672) · 5y D&A **917.8** (screen 918) · 3y D&A **947.2** (screen 947). **The screen's
arithmetic is confirmed exactly.**

### Foot Locker standalone, $M (its own 10-Ks, CIK 0000850209)
| FL FY | OCF | SBC | D&A | capex | **OE (D&A end)** | **OE (capex end)** |
|---|---:|---:|---:|---:|---:|---:|
| 2020 | 1,062 | 15 | 176 | 159 | 871.0 | 888.0 |
| 2021 | 666 | 29 | 197 | 209 | 440.0 | 428.0 |
| 2022 | 173 | 31 | 208 | 285 | **(66.0)** | **(143.0)** |
| 2023 | 91 | 13 | 199 | 242 | **(121.0)** | **(164.0)** |
| 2024 | 345 | 21 | 202 | 240 | 122.0 | 84.0 |

Four-year mean FY2021–FY2024: **+$93.8M** (D&A end) · **+$51.3M** (capex end).
**Against $2.5bn of consideration that is 3.8% and 2.1% — both below the 5.27% sovereign,
before any of the $500–750M of acquisition charges.**

### PRO FORMA COMBINED, $M — fiscal years align to within days, so the records add
| FY | **OE (D&A end)** | **OE (capex end)** |
|---|---:|---:|
| 2021 | 1,681.5 | 1,683.8 |
| 2022 | 439.8 | 364.2 |
| 2023 | 955.1 | 718.6 |
| 2024 | 962.4 | 522.2 |
| 2025 *(as reported: five months of Foot Locker inside, $390.0M of acquisition charges kept in per [E5-33])* | 925.0 | 276.4 |

| window | D&A end | capex end |
|---|---:|---:|
| five-year FY2021–FY2025 *(corpus default [E2-42])* | **992.6** | **713.0** |
| four-year FY2021–FY2024 *(both filers standalone)* | 1,009.7 | 822.2 |
| three-year FY2023–FY2025 | 947.5 | **505.7** |

**Range $506M–$1,010M.** Conservative-end spread across windows **41%**; full band **100%**.

## 2. THE PRICE ARITHMETIC
Shares **89,502,537** (10-Q cover, 2026-05-29). Price **$136.92** (2026-09-02). Cap
**$12,255M**. Sovereign **5.27%** (US Treasury 30y par, 2026-09-01).

| construction | OE $M | yield | vs bond | growth needed for the [E4-28] 10% floor |
|---|---:|---:|---:|---:|
| 3y capex — **bottom boundary [E5-34]** | 505.7 | **4.13%** | **−1.14 pts** | **5.87%** |
| 5y capex | 713.0 | 5.82% | +0.55 | 4.18% |
| 4y capex | 822.2 | 6.71% | +1.44 | 3.29% |
| 3y D&A | 947.5 | 7.73% | +2.46 | 2.27% |
| 5y D&A | 992.6 | 8.10% | +2.83 | 1.90% |
| 4y D&A | 1,009.7 | 8.24% | +2.97 | 1.76% |

Zero-growth value = OE ÷ rate ÷ 89.502537M shares:
| OE $M | at the 5.27% sovereign | at the 10% floor |
|---:|---:|---:|
| 505.7 | $107/sh | $57/sh |
| 713.0 | $151/sh | $80/sh |
| 822.2 | $174/sh | $92/sh |
| 1,009.7 | $214/sh | $113/sh |

## 3. RETURN ON UNLEVERAGED NET TANGIBLE OPERATING ASSETS — DKS, eight years **[E2-43]**
    = OperatingIncomeLoss ÷ (net PP&E + inventories + receivables − accounts payable)
    operating-lease ROU assets excluded

| FY | OI $M | PP&E | inventory | receivables | payables | denominator | **return** |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2018 | 444.7 | 1,565.3 | 1,824.7 | 38.0 | 889.9 | 2,538.0 | 17.5% |
| 2019 | 375.6 | 1,415.7 | 2,202.3 | 53.2 | 1,001.6 | 2,669.6 | 14.1% |
| 2020 | 741.5 | 1,300.3 | 1,953.6 | 53.1 | 1,258.1 | 2,048.9 | 36.2% |
| 2021 | 2,034.5 | 1,319.7 | 2,297.6 | 68.3 | 1,281.3 | 2,404.2 | **84.6%** |
| 2022 | 1,463.0 | 1,313.0 | 2,830.9 | 71.3 | 1,206.1 | 3,009.1 | 48.6% |
| 2023 | 1,282.4 | 1,638.2 | 2,848.8 | 114.9 | 1,288.7 | 3,313.1 | 38.7% |
| 2024 | 1,473.9 | 2,069.9 | 3,349.8 | 214.3 | 1,497.7 | 4,136.3 | 35.6% |
| **2025** | 1,095.9 | 3,512.8 | 4,907.8 | 475.9 | 1,987.0 | 6,909.5 | **15.9%** |

**Adjusted FY2025**, adding back the $382.1M of Foot Locker acquisition charges that sit
inside operating income (proxy Appendix A): $1,516.2M ÷ $6,909.5M = **21.9%**.

**Peak fiscal 2021, four consecutive declines, then a halving.** Denominator +67.0% in one
year against roughly five months of the acquired business's income.

## 4. FOOT LOCKER, DEFLATED — the DG instrument, replicated
Disclosed "Sales per average gross square foot", Item 6 of FL's own 10-Ks. Deflator BLS
CUUR0000SA0, January of the calendar year each fiscal year ends; base January 2026 = 325.252.

| FL FY | nominal | **real, Jan-2026 $** |
|---|---:|---:|
| 2016 | 515 | **690** |
| 2017 | 495 | 650 |
| 2018 | 504 | 651 |
| 2019 | 510 | 643 |
| 2020 | 417 | 518 |
| 2021 | 540 | 625 |
| 2022 | 548 | 596 |
| 2023 | 510 | 538 |
| 2024 | 507 | **519** |

**Nominal −1.6% over eight years. Real −24.7%.** Comps chained FY2016–FY2024 **+6.9%**
against CPI **+30.8%** = **−18.3% real**. Stores **3,363 → 2,410 (−28.3%)**. Operating income
**$1,000M → $103M (−90%)**.

**Foot Locker does not disclose transactions or sales per transaction in any year**, so the
transactions leg of the brief's test 1 cannot be run on the acquired half. Named as a gap,
not estimated.

## 5. CPI-U DEFLATOR USED (BLS series CUUR0000SA0, January, not seasonally adjusted)
| Jan | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| index | 236.916 | 242.839 | 247.867 | 251.712 | 257.971 | 261.582 | 281.148 | 299.170 | 308.417 | 317.671 | 325.252 |

## 6. GUIDANCE, ISSUED AND REVISED FIVE MONTHS APART **[E3-48]**
| | 10-K, 2026-03-27 | 8-K, 2026-08-25 | change |
|---|---|---|---|
| consolidated net sales | $22.1–22.4bn | $21.9–22.2bn | −$0.2bn |
| **diluted EPS** | **$13.70–14.70** | **$10.94–11.94** | **−$2.76, −19.4% at the midpoint** |
| DICK'S comps | +2% to +4% | +2.5% to +4.0% | held |
| DICK'S segment profit | $1.58–1.66bn | $1.54–1.60bn | −$50M at the midpoint |
| **Foot Locker pro forma comps** | **+1% to +3%** | **−2.0% to 0.0%** | **−3.0 pts** |
| **Foot Locker segment profit** | **+$100M to +$150M** | **−$80M to −$40M** | **−$185M** |
| capex | not given in the 10-K | ~$1.6bn gross / $1.4bn net | vs $488.6M of D&A = **3.3x** |
