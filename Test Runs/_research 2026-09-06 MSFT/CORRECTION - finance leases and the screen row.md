# CORRECTION, 2026-09-06 — the screen row DOES reproduce. I was wrong.
Filed as a correction, not by editing the earlier file (operator rule 6).

## WHAT I GOT WRONG
`owner_earnings_byhand.md` recorded the `2026-09-04 FLOOR SCREEN` row
(`oe_bottom 40,268 · oe_top 110,344 · spread 1.74`) as **"NOT REPRODUCED … a fourth screen
spread that failed to reproduce."** **That was my error, and the cause was that I had not yet
included finance-lease right-of-use additions in (c).** Both ends reproduce exactly.

## THE ASC 842 CHECK — IT FAILS MATERIALITY BY THE WIDEST MARGIN IN QUEUE HISTORY
Note 13, FY2021–FY2026 10-Ks. $M.
| | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|
| Finance lease liabilities | 12,541 | 14,902 | 17,067 | 27,145 | 46,172 | **66,594** |
| Amortization of finance ROU assets | 921 | 980 | 1,352 | 1,800 | 3,408 | 5,403 |
| Interest on lease liabilities | 386 | 429 | 501 | 734 | 1,417 | 2,547 |
| **Finance-lease ROU assets OBTAINED** | 3,290 | 4,234 | 3,128 | **11,633** | **20,511** | **24,608** |
| Operating-lease ROU assets obtained | 4,380 | 5,268 | 3,514 | 6,703 | 7,826 | 4,555 |
| Finance-lease discount rate | 3.4% | 3.1% | 3.4% | 3.9% | 4.2% | 4.5% |

- **Finance-lease liabilities ($66,594M) now EXCEED the face value of all bonded debt
  ($46,136M).** Microsoft's largest borrowing is not its bonds.
- **Finance-lease ROU additions FY2024-26 total $56,752M of capital spending that never
  appears in the "additions to property and equipment" line.** Cash principal repaid in
  FY2026 was $3,101M — obligations added roughly **8x faster than they are paid down**, and
  the principal repayment sits in **financing**, so operating cash flow never bears it.
- **LEASES SIGNED BUT NOT YET COMMENCED: $12.7bn → $16.0bn → $42.1bn → $117.0bn → $92.7bn →
  $329,114M (FY2026)**, commencing FY2027–FY2033. **That is 99% of FY2026 total revenue, in
  leases that have not started.** Two disclosure regressions: the operating/finance split of
  this figure was **discontinued after FY2024**, and FY2026 added an unquantified hedge,
  *"with some arrangements subject to certain contractual conditions being met."*
- Reconciliation verified in three vintages: MD&A total lease obligation **$443,506M** less
  Note 13 maturity table **$114,392M** = **$329,114M**, exactly the not-yet-commenced figure.
**This is the check MCD, DRI and CTAS all failed to be immaterial on. Microsoft fails it by
two orders of magnitude more than any of them.**

## THE CORRECTED OWNER-EARNINGS SERIES — (c) = capex + finance-lease ROU additions
| FY | OCF | SBC | capex | finance ROU | **(c)** | **owner earnings** |
|---|---|---|---|---|---|---|
| 2021 | 76,740 | 6,118 | 20,622 | 3,290 | 23,912 | **46,710** |
| 2022 | 89,035 | 7,502 | 23,886 | 4,234 | 28,120 | **53,413** |
| 2023 | 87,582 | 9,611 | 28,107 | 3,128 | 31,235 | **46,736** |
| 2024 | 118,548 | 10,734 | 44,477 | 11,633 | 56,110 | **51,704** |
| 2025 | 136,162 | 11,974 | 64,551 | 20,511 | 85,062 | **39,126** |
| 2026 | 182,935 | 12,405 | 115,948 | 24,608 | 140,556 | **29,974** |

**Windows: 3-yr FY2024-26 = 40,268 · 5-yr FY2022-26 = 44,191 · FY2026 alone = 29,974.**

## BOTH SCREEN ROWS NOW REPRODUCE, TO THE DECIMAL
| screen | field | screen value | my hand value | construction |
|---|---|---|---|---|
| 2026-09-01 FLOOR | oe_bottom | 57,013 | **57,013.4** | 5-yr mean, (c) = capex only |
| 2026-09-01 FLOOR | oe_top | 59,185 | **59,185.3** | 3-yr mean, (c) = capex only |
| 2026-09-01 FLOOR | spread | 0.038 | **3.81%** | |
| **2026-09-04 FLOOR / 09-02 MASTER** | **oe_bottom** | **40,268** | **40,268.0** | **3-yr mean, (c) = capex + finance-lease ROU** |
| **2026-09-04 FLOOR / 09-02 MASTER** | **oe_top** | **110,344** | **110,344.0** | **3-yr mean, (c) = DEPRECIATION ONLY ($15.2/$22.0/$34.3bn)** |
| 2026-09-04 FLOOR | spread | 1.74 | **1.7401** | |
| 2026-09-04 FLOOR | yield_bottom | 0.0106 | 40,268/3,811,904 = **0.01056** | on the screen's cap |
| 2026-09-04 FLOOR | yield_top | 0.0289 | 110,344/3,811,904 = **0.02895** | on the screen's cap |

**Verdict on the screen: it is RIGHT, and it is the first row in this queue that both included
finance leases and used the depreciation-only top end. The failure to reproduce was mine.**
The 2026-09-01 row is the incomplete one — both its ends are capex-only, so its 3.8% "spread"
was never the band at all.

## THE BAND, HONESTLY STATED
| construction | owner earnings | yield on hand cap $3,710,545M |
|---|---|---|
| FY2026 alone, (c) = capex + finance leases | **29,974** | **0.81%** |
| 3-yr mean, (c) = capex + finance leases | **40,268** | **1.09%** |
| 5-yr mean, (c) = capex + finance leases | 44,191 | 1.19% |
| 5-yr mean, (c) = capex only | 57,013 | 1.54% |
| 3-yr mean, (c) = depreciation only — **INVALID [E5-20]** | 110,344 | 2.97% |
| FY2026 alone, (c) = depreciation only — the most generous number constructible | **136,230** | **3.67%** |

**A 4.5x band, $30bn to $136bn wide. Every point in it is below the 5.24% sovereign.**

## THE HEADLINE THE CORRECTION PRODUCES
**Owner earnings including the leased fleet have FALLEN 44% in four years — $53,413M (FY2022)
to $29,974M (FY2026) — while revenue rose 67% ($198.3bn to $331.8bn).**
This is the WMT shape at twice the scale and four times the speed. It is also the answer to
the brief's hypothesis (a): the capital is not merely being *added*, it is being added faster
than the cash the business produces is growing.

## TRUE FY2026 CAPITAL FORMATION, AND ONE ITEM I COULD NOT RESOLVE
cash capex $115,948M + finance-lease ROU $24,608M = **$140,556M** — the figure used above.
Adding operating-lease ROU ($4,555M) would double-count (operating lease cost is already in
OCF), so it is **excluded**.
**Unresolved: the accrued-capex question.** Unpaid PP&E in accounts payable rose $6.9bn →
$26.7bn (+$19,800M) while the cash-flow statement's operating "Accounts payable" line shows
only **+$5,268M** against a balance-sheet AP move of **+$14,692M** ($27,724M → $42,416M).
The $9,424M gap means MSFT excludes *some but apparently not all* of the capex-related
payable from the operating line, and **the filing does not permit a clean reconciliation.**
If operating cash flow is inflated by unpaid capex, FY2026 owner earnings are lower still.
**Carried as a disclosed sensitivity, NOT taken into the base number** — the run does not
spend conservatism twice **[E4-11]**.
