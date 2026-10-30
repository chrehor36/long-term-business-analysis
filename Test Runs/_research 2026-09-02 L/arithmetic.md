# LOEWS — the arithmetic, built from filed statements
Built 2026-09-02. All figures $ millions unless stated. Sources: L 10-K FY2025
(0000060086-26-000008), L 10-K FY2022 (0000060086-23-000025), CNA 10-K FY2025
(0000021175-26-000011), Boardwalk Pipeline Partners LP 10-Ks FY2016–FY2025.

## 1. THE SCREEN'S NUMBER, REPRODUCED EXACTLY

Screen row (`Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`):
cap_m 22,432 · oe_bottom_m **2,585** · oe_top_m 2,788 · yield_bottom **11.52%** ·
vs_sovereign +6.25 pts · growth_required **−1.52%**.

Consolidated Loews, five-year window FY2021–FY2025, from the filed cash-flow statements:

| $M | 2021 | 2022 | 2023 | 2024 | 2025 | mean |
|---|---|---|---|---|---|---|
| Net cash flow provided by operating activities | 2,623 | 3,314 | 3,907 | 3,025 | 3,279 | **3,229.6** |
| Purchases of property, plant and equipment | 482 | 660 | 686 | 632 | 579 | 607.8 |
| Depreciation and amortization | 503 | 509 | 534 | 580 | 607 | 546.6 |
| **Insurance reserves** (working-capital line, inside OCF) | **2,463** | **1,791** | **1,667** | **2,365** | **1,670** | **1,991.2** |
| Trading securities (working-capital line, inside OCF) | (49) | 159 | 577 | (695) | (413) | (84.2) |
| Net investment income (income statement) | 2,259 | 1,802 | 2,395 | 2,780 | 2,779 | 2,403.0 |
| CNA operating cash flow (CNA's own 10-K) | 1,997 | 2,502 | 2,285 | 2,571 | 2,490 | 2,369.0 |

`mean over y of [OCF(y) − max(D&A(y), capex(y))] − SBC 27` = **2,585.0**

**The screen reproduces to the dollar.** Its construction is sound as arithmetic. The
question is whether the construction applies.

## 2. THE CORRECTION CHAIN, EACH STEP NAMED, ON cap = $22,380M

| step | correction | authority | owner earnings | yield |
|---|---|---|---|---|
| 0 | screen as printed | — | **2,585** | **11.55%** |
| 1 | less 8.2% of CNA's operating cash flow (the minority) | **[E5-46]** | **2,391** | **10.68%** |
| 2 | less the insurance-reserve increase inside OCF (float growth) | **[E2-61]** | **400** | **1.79%** |
| 2b | memo: also removing the trading-portfolio swing | — | 484 | 2.16% |

**Float growth is 77.0% of the screen's owner-earnings figure** (1,991.2 ÷ 2,585.0).
CNA supplies **73.4%** of consolidated operating cash flow (2,369.0 ÷ 3,229.6).

**Step 3 — investment-income double counting [E5-48].** Mean net investment income is
**$2,403M**, and it sits inside operating cash flow. Any construction that takes a yield
on OCF *and* then credits the $55,376M investment portfolio has counted the portfolio
twice. Under the sector method the portfolio is component 1 and the investment income must
come OUT of component 2. Removing it from the (already float-corrected) $400M drives the
non-investment result **negative**, which is the correct signal that the yield
construction has no meaning here, not a separate finding.

**Step 4 — (c) per business [E5-20], and it moves the number the OTHER way.**

| business | 2025 capex | 2025 D&A | (c) judged | basis |
|---|---|---|---|---|
| Boardwalk | 354 | 443 | **194** | **the filer discloses maintenance capital directly** |
| CNA | 86 | 70 | 86 | no plant to maintain; a portfolio does not wear out |
| Loews Hotels | ~139 | 100 | ~139 | renovation cycle is real; [E5-20] judges up from D&A |
| Corporate | ~0 | ~0 | 0 | |
| **total** | **579** | **~613** | **~419** | |

The per-business (c) is **LOWER** than the consolidated D&A the screen used. **Correcting
(c) properly RAISES owner earnings by roughly $190M. (c) is not where the screen goes
wrong; the numerator is.**

## 3. BOARDWALK — [E4-55] PHYSICAL SERIES, CPI-U DEFLATED TO 2025 DOLLARS

Throughput and network from each year's own 10-K, Item 1. Financials from Boardwalk
Pipeline Partners LP standalone XBRL, 10-K only. CPI-U annual averages as used in the DG
and UAL runs (BLS); 2016 = 240.007.

| yr | avg daily throughput (Bcf/d) | miles of gas pipe | working gas storage (Bcf) | real revenue | real rev / Bcf/d | real operating income | real op inc / Bcf/d | return on unleveraged NTOA |
|---|---|---|---|---|---|---|---|---|
| 2016 | 6.3 | 13,930 | 205.0 | 1,753.5 | 278.3 | 639.0 | 101.4 | 5.94% |
| 2017 | 6.4 | 13,880 | 205.0 | 1,737.1 | 271.4 | 609.4 | 95.2 | 5.56% |
| 2018 | 7.3 | 13,805 | — | 1,568.9 | 214.9 | 531.4 | 72.8 | 4.87% |
| 2019 | 8.0 | 13,610 | 205.0 | 1,631.0 | 203.9 | 596.5 | 74.6 | 5.51% |
| 2020 | 8.6 | 13,650 | 213.0 | 1,614.1 | 187.7 | 565.5 | 65.8 | 5.24% |
| 2021 | 9.4 | 13,615 | 213.0 | 1,592.2 | 169.4 | 555.0 | 59.0 | 5.31% |
| 2022 | 9.3 | 13,515 | 213.0 | 1,575.3 | 169.4 | 549.2 | 59.0 | 5.60% |
| 2023 | 10.0 | 13,455 | 199.5 | 1,709.2 | 170.9 | 556.0 | 55.6 | 5.83% |
| 2024 | 10.2 | 13,445 | 191.9 | 2,081.5 | 204.1 | 675.0 | 66.2 | 7.21% |
| 2025 | 10.7 | 13,420 | 199.5 | 2,305.8 | 215.5 | 739.9 | 69.1 | 7.57% |

Nine-year changes: **throughput +69.8%** · miles of pipe **−3.7%** · real revenue **+31.5%**
· real operating income **+15.8%** · real revenue per Bcf/d **−22.6%** · real operating
income per Bcf/d **−31.8%** · real total assets **−9.3%**.

Return on unleveraged net tangible operating assets = operating income ÷ (total assets −
goodwill − intangibles − non-interest-bearing current liabilities). 2025 current
liabilities are adjusted for the $550M of 6.0% notes redeemed 2026-03-01.

**Reading, stated both ways.** The per-unit decline is real but the denominator is
contestable: Boardwalk sells **reserved capacity, not throughput**, so extra gas over the
same reservation is designed to earn little. The honest summary is the return on capital,
and it **rose from 5.94% to 7.57%** — a low-return business improving, not a franchise
eroding. The [E4-55] instrument that fired on DG, Foot Locker and UAL **does not replicate
here** in the sense that matters: real operating income is UP and real capital employed is
DOWN.

## 4. CONTRACT QUALITY AND CUSTOMER CONCENTRATION (Boardwalk, own 10-Ks)

| yr | % of revenue from capacity reservation fees / MVCs | top-ten customer concentration |
|---|---|---|
| 2016 | 81% | 42% of revenues |
| 2017 | 83% | 41% of revenues |
| 2018 | 87% | 40% of revenues |
| 2019 | 87% | 37% of future committed revenues |
| 2020 | 90% | 40% of total projected operating revenues |
| 2021 | 89% | 39% |
| 2022 | 87% | 56% |
| 2023 | 89% | 53% |
| 2024 | 86% | 62% |
| 2025 | 87% | **66%** |

Firm-revenue share is stable and high. **Customer concentration has risen from 37–42% to
66% in six years** — the growth projects are large LNG/power counterparties.
Projected operating revenues under committed firm agreements: **$14,184M (2024) →
$19,556M (2025)**, of which **$9.9bn is contingent on regulatory approvals and permits and
is subject to construction risk** (the filer says so).

## 5. [E2-01] THE PRIMARY TEST — RETURN ON EQUITY, TEN YEARS

Net income attributable to the parent ÷ average shareholders' equity (parent only).

| yr | Loews ROE | CNA ROE |
|---|---|---|
| 2016 | 3.66% | 7.24% |
| 2017 | 6.23% | 7.43% |
| 2018 | 3.37% | 6.93% |
| 2019 | 4.95% | 8.54% |
| 2020 | −5.04% | 5.54% |
| 2021 | 8.75% | 9.94% |
| 2022 | 5.11% | 6.94% |
| 2023 | 9.54% | 13.07% |
| 2024 | 8.63% | 9.40% |
| 2025 | 9.33% | 11.55% |
| **10-yr mean** | **5.45%** | **8.66%** |

**Loews' ten-year mean return on equity is 5.45%** — at the 30-year Treasury, and far below
what [E2-42] calls "the return on equity earned over the period by American industry in
aggregate." CNA's 8.66% is better but its post-2022 figures are flattered by an equity
denominator cut by AOCI (equity fell $11,105M → $8,548M in 2022 on the bond mark, and the
2023–2025 ROEs are computed on that smaller base).

## 6. CNA FLOAT, COMPUTED

Float = claim and claim adjustment expense reserves + unearned premiums − reinsurance
recoverables − premiums receivable − deferred acquisition costs. (P&C float; the $13,448M
long-term-care future policy benefit reserve is a discounted long-duration liability and is
reported separately rather than folded in.)

| yr | claim reserves | unearned prem | reins recov | prem recv | DAC | **float** |
|---|---|---|---|---|---|---|
| 2016 | 22,343 | 3,762 | 4,416 | 2,209 | 600 | **18,880** |
| 2017 | 22,004 | 4,029 | 4,261 | 2,292 | 634 | **18,846** |
| 2018 | 21,984 | 4,183 | 4,426 | 2,323 | 633 | **18,785** |
| 2019 | 21,720 | 4,583 | 4,179 | 2,449 | 662 | **19,013** |
| 2020 | 22,706 | 5,119 | 4,457 | 2,607 | 708 | **20,053** |
| 2021 | 21,268 | 5,761 | 5,463 | 2,945 | 737 | **17,884** |
| 2022 | 22,120 | 6,374 | 5,416 | 3,158 | 806 | **19,114** |
| 2023 | 23,304 | 6,933 | 5,412 | 3,442 | 896 | **20,487** |
| 2024 | 24,976 | 7,346 | 6,051 | 3,671 | 959 | **21,641** |
| 2025 | 26,599 | 7,635 | 6,381 | 3,739 | 986 | **23,128** |

Float grew from $18,880M to $23,128M over nine years, **+22.5%** — real growth of
**−8.7%** after CPI-U. Loews' 92% share of 2025 float ≈ **$21,272M**.

## 7. CNA'S TOTAL NON-INVESTMENT RESULT — the [E3-69] numerator

CNA total revenues less total benefits/losses/expenses (CNA's own 10-K), stripping out net
investment income and investment gains/losses, then adding back CNA corporate interest
(a financing cost, not underwriting) and removing the non-insurance warranty margin:

2025: pre-tax income 1,620 − NII 2,557 + investment losses 81 + interest 135
− warranty margin 51 = **−772**

This is the whole insurance operation including the long-term-care runoff, A&EP and legacy
mass tort. The P&C book alone reports an underwriting **gain** of $551M (2025) and $496M
(2024); the runoff blocks consume that and more.

## 8. THE BUYBACK RECORD, FROM XBRL — 2009 to 2025

| yr | shares issued (M) | parent equity | BVPS | repurchase $M | dividends $M |
|---|---|---|---|---|---|
| 2009 | 425 | 16,899 | 39.76 | 334 | 108 |
| 2010 | 415 | 18,450 | 44.46 | 405 | 105 |
| 2011 | 397 | 18,772 | 47.28 | 732 | 101 |
| 2012 | 392 | 19,459 | 49.64 | 212 | 99 |
| 2013 | 387 | 19,458 | 50.28 | 228 | 97 |
| 2014 | 373 | 19,280 | 51.69 | 622 | 95 |
| 2015 | 340 | 17,561 | 51.65 | 1,265 | 90 |
| 2016 | 337 | 18,163 | 53.90 | 134 | 84 |
| 2017 | 332 | 19,204 | 57.84 | 216 | 84 |
| 2018 | 312 | 18,518 | 59.35 | 1,026 | 80 |
| 2019 | 291 | 19,119 | 65.70 | 1,051 | 76 |
| 2020 | 269 | 17,860 | 66.39 | 923 | 70 |
| 2021 | 248 | 17,846 | 71.96 | 1,136 | 65 |
| 2022 | 236 | 14,349 | 60.80 | 729 | 61 |
| 2023 | 222 | 15,704 | 70.74 | 849 | 57 |
| 2024 | 215 | 17,066 | 79.38 | 608 | 55 |
| 2025 | 206 | 18,686 | 90.71 | 806 | 52 |

**Totals 2009→2025: 219M shares retired (51.5% of the company) for $11,276M cash.
Weighted-average price ≈ $51.49.** Book value per share rose 39.76 → 90.71 (**+128%**)
while total parent equity rose only 16,899 → 18,686 (**+10.6%**). Dividends fell every
single year, 108 → 52.

Cross-check on the one year the filer states directly: 2025, **"we purchased 8.9 million
shares of Loews Corporation common stock"** for **$806M** = **$90.56 per share**, against
year-end book value per share of **$90.71** — **0.998× book.**
