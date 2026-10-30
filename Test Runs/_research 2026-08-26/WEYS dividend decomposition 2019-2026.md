# WEYS - Dividend decomposition, regular vs special, 2019-2026
**2026-08-30.** Evidence file for `Test Runs/2026-08-30 Run - WEYS (Weyco) v4.1.md`.
All figures from filed statements (equity statements of the 10-Ks, 10-Q equity statements,
dividend 8-Ks). This is the tasked FIRST question of the run, answered before any gate.

## The answer in one line
**The ~6.8% trailing yield is roughly two-thirds SPECIAL dividend. The regular dividend
yields ~2.4% at $45.39 and has grown ~2.2%/yr over five years, not 26%.** The screen's
"~26% 5y dividend CAGR" is an artifact of two $2.00 special dividends (Q4 2024, Q4 2025)
stacked on a ~$1.00 regular; the company's own press release calls the special a
"return of capital ... cash in excess of what we need to fund operations and capital
expenditures" (8-K 2025-11-04, acc. 0001104659-25-106262).

## Declared per share by calendar year (10-K consolidated statements of equity)
| Year | Total declared | Regular | Special | Source |
|---|---|---|---|---|
| 2019 | $0.95 | $0.95 | - | FY2020 10-K equity stmt (acc. 0001104659-21-035462) |
| 2020 | $0.96 | $0.96 | - | same |
| 2021 | $0.96 | $0.96 | - | FY2022 10-K equity stmt (acc. 0001410578-23-000248) |
| 2022 | $0.96 | $0.96 | - | same |
| 2023 | $0.99 | $0.99 | - | XBRL companyfacts, FY2023 10-K |
| 2024 | **$3.03** ($29.101M) | $1.03 | **$2.00** (declared Q4 2024; prefunded Dec 2024; paid Jan 2025) | FY2025 10-K equity stmt (acc. 0001104659-26-027690) |
| 2025 | **$3.07** ($29.321M) | $1.07 (0.26/0.27/0.27/0.27) | **$2.00** (declared 2025-11-04; ~$19M; paid 2026-01-09) | FY2025 10-K; 8-K acc. 0001104659-25-106262 |
| 2026 YTD | $0.83 + Q4 TBD | Q1 $0.27 · Q2 $0.28 · Q3 $0.28 (declared 2026-08-04) | none declared as of 2026-08-30 | Q2 2026 10-Q (acc. 0001104659-26-092615); 8-K 2026-08-04 |

## The screen metrics, decomposed
- **"26% 5y dividend CAGR"** = ($3.07 / $0.96)^(1/5) − 1 = 26.2%. Take out the special:
  ($1.07 / $0.96)^(1/5) − 1 = **2.2%/yr**. The 26% is entirely the special.
- **"~6.8% trailing yield"** at $45.39 (Nasdaq close 2026-08-28): trailing-12-month
  declarations = $0.27 (Q4'25 reg) + $2.00 (special) + $0.27 + $0.28 + $0.28 = $3.10 →
  6.8%. Decomposed: **regular ~2.4% + special ~4.4%.**
- **"No cuts"**: true of the regular (no reduction found in the series read, 2019-2026;
  raises of $0.01/qtr roughly annually). The special has existed for exactly two years.

## Cash mechanics (why "dividends paid" looks small in 2025)
- 2024 Q4 regular + special ($21.579M) prefunded into a separate account in Dec 2024,
  paid to holders Jan 2025; shown as "Prefunded dividend" asset at YE2024 and settled
  non-cash in 2025. FY2025 cash dividends paid line: only $7.732M (three regular payments).
- 2025 Q4 regular + special ($21.385M) sat as "Dividend payable" at YE2025, paid
  2026-01-09. H1 2026 cash dividends paid: $26.6M.

## Coverage (against owner earnings, from the run file's Q4 table)
- Regular run-rate: $0.28 × 4 = $1.12/sh ≈ **$10.7M/yr** vs multi-year OE ~$24-27M →
  **~2.3-2.5x covered.** The regular is durable at current earnings.
- Regular + special: ~$29.7M/yr vs OE ~$24-27M → **~110-120% of OE.** The special is not
  covered by earnings; it is a drawdown of the $98-115M cash pile, exactly as management
  describes it. Whether it recurs is a yearly board decision (declared each November,
  two years running), not a policy.

## Consequence for the operator's thesis
The "dividend payer that also compounds" case rests on the REGULAR dividend: 2.4% yield
growing ~2%/yr in a business whose revenue fell 9% nominal over six years. The 6.8%
headline requires the November special to repeat indefinitely, which management has
explicitly framed as excess-capital return, and which stops being possible-without-
drawdown at ~$24-27M OE against ~$29.7M of total distributions.
