# TRV competitor row, 2026-09-19 — extended from the MKL row via the CB run, not rebuilt

**BASIS: current-accident-year combined ratio = reported combined ratio with prior-year reserve
development removed.** Window 2021-2025. Every cell read from the filer's own Form 10-K.

Eight rows (KNSL, ACGL, CB, WRB, RLI, AXS, MKL, FFH) are **carried unchanged** from
`Test Runs/_research 2026-09-19 CB/peers/row_out.txt`, which put the MKL run's seven-peer row on
this basis and added CB. Five rows are **new in this run**: TRV itself plus the standard-lines
peers the MKL/CB row does not contain — PGR, ALL, CINF (personal automobile and homeowners) and
HIG, CNA (standard commercial).

| company | basis | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean | provenance |
|---|---|---|---|---|---|---|---|---|
| KNSL | consolidated | 82.6 | 82.9 | 78.6 | 79.1 | 79.8 | 80.60 | carried |
| ACGL | consolidated | 89.6 | 89.5 | 83.6 | 85.9 | 86.3 | 86.99 | carried |
| CB | consolidated | 91.9 | 90.4 | 88.4 | 88.6 | 88.2 | 89.50 | carried |
| WRB | consolidated | 89.7 | 88.9 | 89.5 | 90.3 | 90.7 | 89.84 | carried |
| HIG | Business Insurance segment | 94.3 | 92.4 | 91.5 | 91.7 | 91.5 | 92.28 | NEW |
| PGR | total underwriting operations | 95.3 | 96.0 | 93.0 | 89.4 | 89.1 | 92.57 | NEW |
| RLI | consolidated | n/a | 95.1 | 95.0 | 92.4 | 89.7 | 93.08 (4) | carried |
| AXS | consolidated | 98.2 | 96.3 | 91.8 | 92.8 | 91.4 | 94.10 | carried |
| CNA | P&C Operations, NEP-weighted | 96.8 | 94.4 | 93.8 | 95.3 | 94.2 | 94.89 | NEW |
| **TRV** | **consolidated** | **96.3** | **97.5** | **97.4** | **94.2** | **92.3** | **95.54** | **THIS RUN** |
| ALL | Property-Liability | 95.6 | 102.7 | 103.3 | 94.8 | 88.3 | 96.94 | NEW |
| CINF | consolidated P&C | 95.3 | 100.4 | 97.7 | 96.1 | 96.9 | 97.28 | NEW |
| MKL | consolidated | n/a | n/a | 99.3 | 101.1 | 100.4 | 100.27 (3) | carried |
| FFH | — | n/a | n/a | n/a | n/a | n/a | NOT COMPARABLE | carried |

**TRV ranks 10th of the 13 with data; 4th of the 6 standard-lines peers.**

## The new rows, cell by cell, with the arithmetic shown

### TRV — FY2016, FY2018, FY2019, FY2021, FY2023 and FY2025 10-Ks
reported CR, catastrophe points, prior-year development points (favourable positive):
2016 92.0/3.6/+3.2 · 2017 97.9/7.6/+2.3 · 2018 96.9/6.3/+1.9 · 2019 96.5/3.1/−0.2 ADVERSE ·
2020 95.0/5.5/+1.2 · 2021 94.5/6.0/+1.8 · 2022 95.6/5.5/+1.9 · 2023 97.0/7.9/+0.4 ·
2024 92.5/8.0/+1.7 · 2025 89.9/8.4/+2.4.
Current-accident-year CR = reported + favourable development. Checked against the filer's own
stated year-over-year change in the underlying combined ratio at all nine year-pairs, no residual.

### PGR — FY2025 10-K 0000080661-26-000086 (Annual Report exhibit pgr-20251231_d2.htm); FY2023 10-K 0000080661-24-000007
Total underwriting operations combined ratio: 2021 95.3, 2022 95.8, 2023 94.9, 2024 88.8, 2025 87.4.
Prior-year development $m (favourable positive): 2021 +4.7, 2022 +86.3, 2023 −1,094.0 ADVERSE,
2024 +416, 2025 +1,394 — all four figures quoted in the reserves note as "Incurred related to
prior years".
Net premiums earned $m: 44,369 / 49,241 / 58,665 / 70,799 / 81,661 (consolidated income statement).
Points: +0.01 / +0.18 / −1.86 / +0.59 / +1.71. Current-AY: 95.31 / 95.98 / 93.04 / 89.39 / 89.11.
Underwriting expense ratio 2025 **21.5%** (2024 19.7, 2023 17.3).

### ALL — FY2025 10-K 0000899051-26-000031; FY2023 10-K 0000899051-24-000013
Property-Liability combined ratio: 2021 95.9, 2022 106.6, 2023 104.5, 2024 94.3, 2025 85.2.
"Effect of prior year reserve reestimates on combined ratio" (as printed; parentheses = release):
2021 +0.3, 2022 +3.9, 2023 +1.2, 2024 (0.5), 2025 (3.1).
Current-AY = CR less that effect: 95.6 / 102.7 / 103.3 / 94.8 / 88.3.
Catastrophe effect on CR: 8.3 / 7.1 / 11.6 / 9.2 / 8.6. Expense ratio 2025 **21.4%**.

### CINF — FY2025 10-K 0000020286-26-000008; FY2023 10-K 0000020286-24-000014
Consolidated property casualty combined ratio: 2021 88.3, 2022 98.1, 2023 94.9, 2024 93.4, 2025 94.9.
Prior accident years = "before catastrophe losses" plus "catastrophe losses" rows:
2021 (5.9)+(1.1) = −7.0 · 2022 (1.3)+(1.0) = −2.3 · 2023 (2.2)+(0.6) = −2.8 ·
2024 (1.6)+(1.1) = −2.7 · 2025 (1.3)+(0.7) = −2.0, all favourable.
Current-AY: 95.3 / 100.4 / 97.7 / 96.1 / 96.9. Expense ratio 2025 **29.3%**.

### HIG — FY2025 10-K 0000874766-26-000012; FY2023 10-K 0000874766-24-000016
**Business Insurance segment only: HIG publishes no consolidated property-casualty combined
ratio, and that limit is disclosed rather than papered over.**
Combined ratio: 2021 95.8, 2022 90.2, 2023 89.6, 2024 89.9, 2025 88.3.
"Prior accident year development" in the loss-ratio build (negative = favourable):
2021 +1.5 ADVERSE, 2022 (2.2), 2023 (1.9), 2024 (1.8), 2025 (3.2).
Current-AY: 94.3 / 92.4 / 91.5 / 91.7 / 91.5. Expense ratio 2025 **31.2% plus 0.3 dividend ratio**.
HIG personal lines for reference: automobile CR 112.8 (2023) / 103.3 (2024) / 93.2 (2025) with
prior-year releases of (1.1) / 2.8 / 4.8 points; homeowners 96.4 / 90.1 / 89.2.

### CNA — each year's own 10-K; FY2025 0000021175-26-000011
Carried from `peers/data_CNA.json`, extracted earlier the same day in this folder. P&C Operations
(Specialty + Commercial + International), NEP-weighted; CNA prints no P&C Operations combined
ratio, so every cell is computed and the recipe is in that file.
CR: 96.19 / 93.18 / 93.51 / 94.94 / 94.73. Prior-year development points: −0.64 / −1.17 / −0.25 /
−0.32 / +0.49 (negative = favourable). Current-AY: 96.83 / 94.35 / 93.76 / 95.26 / 94.24.
Expense ratio 2025 **29.77%**, excluding the 0.2-0.4 point dividend ratio.
**COMPARABILITY LIMIT, disclosed:** excludes Corporate & Other, where CNA's asbestos,
environmental and legacy mass-tort development ran +$50M to +$134M ADVERSE a year 2020-2025.
**TRV's consolidated figure includes its asbestos charges in full.** So CNA's cell is flattered
relative to TRV's, and correcting it would move TRV up one place.

## Limits of this row, stated

1. **FFH is not comparable** and is left blank, carried from the MKL/CB row.
2. **Two cells are segment-level, not consolidated** (HIG) or computed from segments (CNA),
   because those filers publish nothing else. Both are labelled in the table.
3. **[E3-61]:** the row shows position, never conduct.
4. **Cost of float was NOT computed for the peers.** The row is on the current-accident-year
   combined ratio, which is the numerator of the cost-of-float ratio, so a better ratio on a
   comparable float ratio implies a better cost of float — but that is an inference, and
   CONVENTION 4 would have to be run on each peer's balance sheet to make it a measurement.
