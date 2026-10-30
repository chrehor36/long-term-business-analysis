# EAT OWNER-EARNINGS SERIES — hand-built 2026-09-05
Source: SEC XBRL companyfacts CIK 0000703351 (as-filed original vintages), cross-checked
against the FY2026 10-K consolidated statement of cash flows (accession 0000703351-26-000029,
filed 2026-08-19, period 2026-06-24). Brinker files in $ millions. Fiscal years end last
Wednesday of June; FY2021 had 53 weeks.

## Construction: OCF − SBC − capex (the CONVENTION in v4.1; one capex line filed —
## "Payments for property and equipment"; NO separate software line, the HAS defect does not bite)

| FY | OCF | SBC | Capex | OE (capex end) | D&A | OE (D&A end) |
|---|---|---|---|---|---|---|
| 2016 | 394.7 | 15.2 | 112.8 | 266.7 | 154.8 | 224.7 |
| 2017 | 312.9 | 14.6 | 102.6 | 195.7 | 155.0 | 143.3 |
| 2018 | 284.5 | 14.2 | 101.3 | 169.0 | 150.1 | 120.2 |
| 2019 | 212.7 | 16.4 | 167.6 | 28.7 | 146.5 | 49.8 |
| 2020 | 245.0 | 14.8 | 104.5 | 125.7 | 160.4 | 69.8 |
| 2021 (53wk) | 369.7 | 16.4 | 94.0 | 259.3 | 148.2 | 205.1 |
| 2022 | 252.2 | 18.6 | 150.3 | 83.3 | 161.3 | 72.3 |
| 2023 | 256.3 | 14.4 | 184.9 | 57.0 | 165.3 | 76.6 |
| 2024 | 421.9 | 25.9 | 198.9 | 197.1 | 170.8 | 225.2 |
| 2025 | 679.0 | 31.4 | 265.3 | 382.3 | 206.6 | 441.0 |
| 2026 | 789.4 | 32.2 | 231.9 | 525.3 | 218.7 | 538.5 |

D&A FY2024-26 from the filed cash-flow line (218.7/206.6/170.8); FY2016-23 from the XBRL
"Depreciation" tag (the cash-flow caption is "Depreciation and amortization"; small gap
possible in older years, direction unknown — noted, immaterial to any verdict).
FY2017 OCF: original vintage 312.9; later vintages restate to 315.1 (+2.2). Original used.

## Windows (capex end / D&A end, $M)
- 3-yr FY2024-26: **368.2 / 401.6**
- 5-yr FY2022-26: **249.0 / 270.7**
- 10-yr FY2017-26: **202.3** (capex end)
- Leave-two-out on 7-yr FY2020-26 (drop FY2025+FY2026, the ANF fix): **144.5**
- Pre-boom 7-yr FY2016-22: **161.2** — the operator's asked-for base
- Best single year ever (FY2026): **525.3**

## The boom signature [E4-41]
Pre-boom 5-yr mean (FY2018-22) = 133.2. Boom 3-yr mean (FY2024-26) = 368.2. A 2.8x step.
Named: the FY2025-26 Chili's traffic surge (Triple Dipper/TikTok virality + "3 for Me"
value platform + staffing/simplification execution under Hochman, CEO since June 2022).
The FY2019 collapse to 28.7 is its own event: $455.7M sale-leaseback year + remodel
program + revenue decline; and FY2016-18 OE (195.7-266.7) sits on an OWNED-real-estate
cost structure that no longer exists (141 restaurants sold-leaseback FY2019) — the
pre-2019 and post-2019 series are two different lease structures [E4-25 caveat].

## Cap, price, yields (cover count 41,765,010 × $230.22 = $9,615M)
| Construction | OE $M | Yield |
|---|---|---|
| Leave-two-out | 144.5 | 1.50% |
| Pre-boom 7-yr | 161.2 | 1.68% |
| 10-yr | 202.3 | 2.10% |
| 5-yr capex end | 249.0 | 2.59% |
| 5-yr D&A end | 270.7 | 2.82% |
| 3-yr capex end | 368.2 | 3.83% |
| 3-yr D&A end | 401.6 | 4.18% |
| FY2026 alone (best ever) | 525.3 | 5.46% |
Sovereign 5.24% (US Treasury 30-yr, 2026-09-04). Every multi-year construction is BELOW
the bond; the single best year in company history clears it by 0.22 points.

## Screen-row reproduction
run.py (2026-09-05): 3-yr window OE 368-404 → yield 3.57-3.92% on its 44.8M
weighted-average share basis (the known tool defect; cover count is 41.77M, cap 9,615 not
10,310). By hand at the cover cap: 3-yr 3.83-4.18%, 5-yr 2.59-2.82%. The brief's
3.2%/6.8% row sits between my 3-yr and 5-yr windows at a slightly larger cap —
reproduced in shape, not to the million; the spread (3-yr vs 5-yr conservative ends:
1 − 249.0/368.2 = 32.4%) is the row's real content and it survives.

## FY2026 quarterly traffic path (Chili's, filed 10-Qs) — the normalization series
Q1 +13.1% (price +4.0) · Q2 +2.7% (price +4.4) · Q3 −1.2% (price +4.6) ·
Q4 implied ≈ +1.2% (arithmetic mine: 4×3.6 − 3×4.4). The wave is lapped; the LEVEL held.
