## Q7 — WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is
the risk-free interest rate" **[L2000-021]**; value is "the discounted value of the cash that can be taken out of a
business during its remaining life" **[R1996-018]**, with the business credited only "for whatever net cash is left
every year" **[M1998-080]**. The rate is the long Treasury, 5.56% **[M1996-025]**. All arithmetic is in
`scripts/calc.py` and `calc_out.txt`.

**The cash (Q4's recast).** Owner cash = operating cash − stock pay − property − capitalised software − finance-lease
principal − acquisitions (USD millions; filed cash-flow statements):

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| owner cash after interest (equity-only) | 983 | 493 | −203 | 1,375 | 1,490 | 1,365 | 1,729 |
| owner cash before interest (all-equity; interest paid × 0.79 added back) | 1,267 | 835 | 81 | 1,678 | 1,879 | 1,809 | 2,241 |
| of which customer advances (deferred revenue + loyalty liability) | 174 | 825 | −233 | 205 | 552 | 572 | 481 |

**CONVENTION of this run (after-tax interest):** interest paid is added back at (1 − 21%), the U.S. federal statutory rate;
rationale: the company's own tax is inside operating cash already, and the all-equity basis needs the interest after the
tax it saved; the filer's effective rate (about 29% in 2025) would add back less and lower every figure.

**The six specifics.**
- **(a) Cycle.** The literal five-year window is 2021 to 2025; its first year is aberrational on the filer's own account
  ("As a result of the COVID-19 pandemic, the operations of certain of our hotels were suspended", FY2022 10-K, Note 17;
  owner cash −$203M) **[L2005-003]**,
  **[L2003-004]**. The base is therefore the last full cycle **[M2011-101]**, **[M2011-102]**: **2019 to 2025**, the
  pre-pandemic peak to the latest year, which is above it. **CONVENTION of this run:** the cycle runs peak to latest year
  because the company in its present form exists only from the 2017 spin-offs, so no earlier trough or second peak of the
  same business is on file; rationale: the 2016 and earlier figures are a hotel owner and timeshare seller, not this
  business. The April 2020 point pre-sale ($1.0B in) and its use by mid-2022 both fall inside the cycle and net out in its
  average. **Base: $1,398M a year all-equity; $1,033M equity-only.** The literal window is shown beside: $1,537M and $1,151M.
- **(b) Growth, and (f) the cap.** The series changes sign (2021), so growth is measured between the halves of the cycle:
  2019 to 2021 averages $728M before interest, 2023 to 2025 average $1,976M, **28.4% a year**. Carried ten years it would
  put owner cash at several times its highest share of sales in the filings read (36.8% of revenue before reimbursements,
  2022), so by (f) it is cut to the business's own sales growth **[M1999-067]**. **CONVENTION of this run (which sales):**
  the top case uses the management and franchise segment's fee revenue, 2019 to 2025, **7.5% a year**, because that part
  decides (Q2) and the consolidated figure is pulled down by leases deliberately exited; the consolidated revenue before
  reimbursements, **4.7% a year**, is shown beside, and so is the consolidated sales growth between the same halves,
  15.9%, which carries the 2020 to 2021 trough. No rate above the discount rate is carried after year ten
  **[M1997-095]**: years eleven on are at zero growth.
- **(c) Acquisitions.** $240M over the cycle (Graduate, NoMad), deducted, total growth credited. Not a serial acquirer
  (purchases are about 3% of owner cash before purchases). No deal signed and unclosed; none closed after the window.
- **(d) Working capital** is counted as filed. The customer advances added $368M a year on average to the base; they
  grow with the system and the co-branded cards and would not grow in a business that has stopped growing. They are left
  in, which flatters the no-growth case; taking them out lowers every figure below.
- **(e) Maintenance.** The filing does not split maintenance from growth spending (Q3). The central case charges all
  spending; beside it, the case that treats every dollar of key money as growth (base $1,540M), an upper bound.
- **Net debt** at the latest filed date (10-Q, June 30, 2026): debt and finance leases at face $13,444M less cash
  $1,009M = **$12,435M**; restricted cash ($55M) and operating leases ($680M non-current liability) left out, said so; no
  subsequent event in the 10-Q changes it. Enterprise value at the price: $74,179M + $12,435M = $86,614M.

**The floor, tested first** **[M2003-149]**, **[M1994-004]**, **[L2002-020]**: the expected return at $329.59 on each case
(the rate at which the case's cash, ten years at its growth then flat, equals the price paid; all-equity against
enterprise value, equity-only against market value):

| case | value per share at 5.56% (all-equity) | expected return at the price (all-equity) | equity-only value / return |
|---|---|---|---|
| no growth | **$56.50** | 1.6% | $82.56 / 1.4% |
| consolidated sales growth, 4.7% | $106.83 | 2.5% | $119.74 / 2.1% |
| **fee growth of the deciding part, 7.5% (top)** | **$147.79** | 3.1% | $150.00 / 2.7% |
| beside: sales growth between halves, 15.9% | $337.91 | 5.7% | $290.46 / 5.0% |
| beside: key money as growth, 7.5% | $168.32 | 3.4% | |
| beside: literal window, 7.5% | $167.95 | 3.4% | |
| beside: 2025 alone (not the convention), 7.5% | | 4.8% | |
| forbidden by (f): the uncut 28.4% halves rate | $947.80 | 11.2% | $741.02 / 10.1% |

**No case the method allows earns the floor of about ten percent at the price.** The best allowed case returns about 5.7%,
the central top 3.1%, the no-growth case 1.6%, against a 5.56% Treasury. Only the 28.4% rate that (f) forbids, a rate
carried ten years from a pandemic trough, clears it. "there’s just a point at which we drop out of the game" **[M2003-149]**.

**Value range:** **$56.50 to $147.79 a share (all-equity, central) against $329.59**; equity-only $82.56 to $150.00;
literal window beside, $67.60 to $167.95. Width 2.6 to 1. The price is more than twice the top of the range; the market
price implies owner cash growing well above the 7.5% the fee base has shown, for ten years, or a rate below the Treasury.
"You can turn any investment into a bad deal by paying too much" **[M2019-015]**.

**Closes: OUT**, by the floor tested first (2026-10-10): no case in the range earns the floor at the price, and the price
sits above the top of the range, which closes OUT however the width reads **[M2003-149]**, **[M2009-005]**.

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent, averaged:
all-equity ends $6.89 (no growth) and $49.08 (7.5%), **fair price $27.98 a share (central, all-equity, after the
company's own tax)**; **equity-only $61.49** ($45.90 and $77.08). Beside them, with key money treated as growth, $36.40
all-equity. The all-equity figure sits below the equity-only one because at ten percent the no-growth business is worth
little more than its $12.4B of net debt. No cheap price is reported.

- **VERDICT: OUT.** Valued, and the price does not clear the floor on any case the method allows **[M2003-149]**; the
  castle is good (Q2) and the price is the problem, "it makes more sense [...] to buy a wonderful business at a fair price,
  than a fair business at a wonderful price" **[M2003-040]**, and this is neither at $329.59.
