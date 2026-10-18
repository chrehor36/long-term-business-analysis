
## Q7 — WHAT IS IT WORTH? STOP.
*(Arithmetic in `q7.py`, `q7b.py` and their outputs in the research folder. The first pass of `q7.py` was computed in
the research folder before Q3 to Q6 were written into this file; it carried no entry language and is declared under the
self-audit.)*

- **How much cash, how sure, how soon, at the long government rate** **[L2000-021]**, **[M2009-004]**. The cash
  counted is what comes out net of what must go back in **[M1998-080]**, **[M2014-068]**. Owner cash, from Q4's
  recast, never net income:
  - **All-equity basis (central):** operating cash less stock pay less spending, plus interest paid at the filer's
    blended statutory tax of 26% (CONVENTION of this run: the interest add-back uses cash interest paid, net of
    capitalized, from the cash-flow supplement, and the 26% the 10-K states for its cents-per-share bridge; rationale:
    operating cash is struck after cash interest, and the filer's own blended rate is the only rate the filing gives).
  - **The maintenance guess** **[M2000-144]**, **[L1999-024]**: the filing states no maintenance figure; depreciation is
    used, the proxy the rows allow **[M1998-127]**, flagged as generous because for a utility "your depreciation charges
    are inadequate" **[M2015-049]**. Growth spending is capex less depreciation, $2,224.8M a year on the 2021 to 2025
    means ($3,669.8M less $1,445.0M).

  | USD M | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean |
  |---|---|---|---|---|---|---|
  | owner cash after maintenance, all-equity | 735 | 1,153 | 1,510 | 1,663 | 2,272 | **1,467** |
  | owner cash after all spending, all-equity | -1,000 | -760 | -655 | -1,132 | -244 | -758 |
  | owner cash after maintenance, equity-only | 420 | 801 | 1,106 | 1,211 | 1,713 | 1,050 |
  | owner cash after all spending, equity-only | -1,315 | -1,112 | -1,059 | -1,584 | -803 | -1,175 |

- **The specifics applied.** (a) **Cycle base:** the first window year, 2021, is depressed on the filer's own
  description (the ‘extremely cold weather in mid-February 2021’ raised gas costs, deferred and collected over 18 months
  from April 2021, FY2022 10-K, Liquidity, quoted from the filing). Because the collection fell in 2021 and 2022, both
  inside the window, the five-year mean nets it out; only the growth end-points are distorted. The mean is kept as the
  base, and growth is not read from the 2021 end-point (below). (b) **Decline:** none in the maintenance series; the
  all-spending series is negative in every year and is carried beside, not as an end (see (e)). (c) **Acquisitions:**
  none in the window. (d) **Working capital:** inside operating cash, which is used as filed. (e) **Growth spending:**
  the central case is owner cash after maintenance; the growth case charges the growth spending each year for ten years
  and credits the growth it bought, at the incremental return Q3 measured on added debt plus equity, 6.68% (2020 to 2025;
  5.98% over 2016 to 2025 shown beside), so owner cash rises by that return on each year's growth spending; after year
  ten no growth and no growth spending. (f) **The cap:** the literal shown growth of the maintenance series, 32.6% a year
  (2021 to 2025; 27.7% between the window's halves), carried ten years would need owner cash of $24.6 billion against a
  best share of sales of 25.8% (2025): absurd, so the literal rate is not carried. The growth credited in (e) compounds
  to 7.25% a year over the ten years (owner cash $2,953M in year ten), inside the shown rate, and needs about 15% of
  sales at the shown sales growth: no cut is triggered. **The mechanical alternative**, the sales-growth cut of (f)
  (8.31% shown, cut to the 5.43% discount rate) applied while the growth spending is still charged, gives a lower growth
  case ($11.04 a share, all-equity); it is shown beside and not used, because (e) says ‘Never charge all spending and
  also cap the growth that spending bought’ (the framework's own words, Q7, six more specifics; single-quoted as not
  a ledger row). After year ten: zero
  nominal growth.
- **Whose tax** **[M1994-004]**, **[L2002-020]**: owner cash is after the company's own tax as paid, which was about
  nil for the decade (Q4: tax-credit sales and deferred taxes). The framework's statutory-rate convention is written for
  carryforwards or credits that run out inside ten years; part of Ameren's shelter is of that kind (credit carryforwards
  $178M and loss carryforwards $165M at 2025, 10-K Item 7; credit sales $314M in 2025) and part is deferred tax that
  ratemaking returns to customers **[M2015-030]**. Recomputing at the statutory rate would lower every figure below; it
  is not done, because every case already fails the floor (CONVENTION of this run, confessed: the more generous tax
  basis is kept where the stricter one cannot change the box).
- **Net debt** (all-equity basis): at June 30, 2026, current maturities $1,524M plus long-term debt $19,064M plus
  short-term debt $1,220M less cash $12M = **$21,796M** (10-Q balance sheet, `0001002910-26-000023`); operating leases
  left out; no finance-lease line found. The 10-Q's stated subsequent event is the July 2026 forward sale of 1.4M
  shares (not settled, no cash yet). Later debt issues ($400M Ameren Illinois bonds, 8-K of 2026-08-24; $900M junior
  subordinated notes, 8-K of 2026-09-18) are not in a filed balance sheet and are not added. Enterprise value at the
  price: $29,368M plus $21,796M = $51,164M.

- **The range, all-equity, at the long rate 5.43%** (USD M; per share after net debt, 276.843M shares):

  | case | value | per share |
  |---|---|---|
  | no growth, owner cash after maintenance ($1,467M a year) | 27,011 | **$18.84** |
  | growth bought by the growth spending, at 6.68% incremental return | 32,008 | **$36.89** |
  | beside: the same at 5.98% | 29,722 | $28.63 |
  | beside: the mechanical (f)-capped growth case, spending charged | 24,851 | $11.04 |
  | beside: all spending deducted, no growth ($-758M a year) | -13,962 | negative |
  | beside: forward sales settled (17.4M more shares, $1.76B less debt), no-growth and growth cases | | $23.70 to $40.68 |

  **Value range: $18.84 to $36.89 a share (all-equity) against $106.08.** The growth case is the top because the
  growth spending earns 6.68% against a discount rate of 5.43%, so it adds a little value at the long rate. Width 1.96 to
  one. **Equity-only, beside:** no growth $69.86, growth case $87.91 (`q7_output.txt`, `q7b_output.txt`; the equity-only
  growth case charges the full growth spending against owner cash after interest and credits the unlevered incremental
  return, which flatters it).
- **The floor, tested first** (about ten percent pre-tax, after the company's own tax). The return each case earns at
  the price (the rate that equates the case's cash to what is paid): all-equity, no growth **2.87%**, growth case
  **3.93%** (on enterprise value of $51,164M); equity-only, no growth 3.58%, growth case 4.85% (on the market value of
  $29,368M). For the no-growth case to earn ten percent on enterprise value, owner cash before interest would have to be
  $5,116M a year; the five-year mean is $1,467M and the best year $2,272M. **No case earns the floor at the price**; the
  price is above the top of the range on both bases. "there’s just a point at which we drop out of the game" **[M2003-149]**;
  a price above the top closes OUT however wide the range (Q7, the four specifics).
- **Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and the two
  averaged, after the company's own tax. **All-equity (central): no positive fair price**: the no-growth end is worth
  $14,667M and the growth end $11,042M at ten percent, both below net debt of $21,796M (per share $-25.75 and $-38.85,
  average $-32.30). **Equity-only, beside: $31.39** (ends $37.93 and $24.84). The central figure is the all-equity one.
  No cheap price is reported.
- **VERDICT: OUT.** Valued, and the price does not clear the floor on any case **[M2003-149]**: the regulated return on
  added capital, about 6% to 7% unlevered (Q3), cannot carry an enterprise value of about $51 billion to ten percent
  **[L2000-021]**, **[M1996-025]**. The range is narrow (under two to one), so the box is not TOO HARD **[L2000-025]**.
