## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
at the long government rate **[L2000-021]**, held as a range **[L2000-024]**. All figures below are from `q7.py` and
`q7_cycle.py` in the research folder, inputs from the filed cash flow statements named there; USD millions unless a per-share
figure. **Price and rate not refreshed:** the price ($90.75, close 2026-10-09) and the sovereign (5.60%, 2026-10-09) of
Step 0 are used unchanged; the result is not near enough to either to need a refresh.

- **The cash input** (Q4's recast): operating cash less stock pay less all capital spending less cash paid for businesses
  plus cash received for businesses sold, specific (c), the default pair: acquisitions deducted, the total growth credited
  (the filer reports no organic owner-cash figure, so the organic pair is not shown). On the all-equity basis **[L2017-004]**
  the after-tax net interest is added back (interest paid less interest income where filed, times one less the year's
  effective rate). Working capital is inside operating cash, specific (d). Unlevered owner cash, FY2016 to FY2025: 3,036;
  2,629; 2,115 (the Nestle prepayment removed, below); 3,858; 181; 5,697; 2,637; 3,821; 3,349; 2,298.
- **Growth spending, specific (e).** The filer gives no maintenance figure (Q3), so the filing does not allow the maintenance
  guess; the central case charges all capital spending, with depreciation in place of capital spending shown beside.
- **The window and the cycle, specific (a).** Both end years of the literal window FY2021 to FY2025 are aberrational on the
  filer's own description: FY2021 carries the recovery from the pandemic and $1,175.0M of cash from the divestiture of the
  South Korea joint venture (10-K FY2022, which describes the conversion of Korea to a fully licensed market); FY2025 is the
  year of the "Back to Starbucks" restructuring, $892.0M of charges and 627 store closures (10-K FY2025). "If either year
  was aberrational, any calculation of growth will be distorted." **[L2005-003]**. **CONVENTION of this run:** the cycles
  are FY2016 to FY2020 and FY2021 to FY2025, each running from a normal year to a year the filer describes as disrupted (the
  pandemic; the restructuring); rationale: the filings name no other cycle and these are the two complete ones in the ten
  years read. **CONVENTION of this run:** the Nestle up-front payment of "approximately $7 billion primarily of prepaid
  royalties" (10-K FY2018) is removed from FY2018 operating cash; rationale: it is decades of royalties received at once, and
  every later year's operating cash already lacks the royalties it prepaid. The variant that keeps it is shown.
- **The base and the growth.** Cycle averages: FY2016 to FY2020, 2,364; FY2021 to FY2025, 3,560 (the same as the literal
  window's average). Growth between the cycle averages: 8.5% a year (7.9% on owner cash after interest). The base is the
  last cycle's average, 3,560.
- **The cap, specific (f).** 3,560 carried ten years at 8.5% is 8,050 in year ten; sales carried at the business's own
  growth between the same cycles (averages 23,690 and 34,129, 7.6% a year) would be about 70,900, so the year-ten owner cash
  is 11.4% of sales, under the highest share earned in a year of the ten read without a business sale (14.6%, FY2019). The
  cap does not cut. Nothing is carried after year ten (zero nominal growth) **[M1997-095]**.
- **The China sale, closed after the window and before the price date, specific (c).** On its own filed record: 60% sold at
  a $4B enterprise value, $3.1B of consideration, $2.5B of net proceeds in the cash flow discussion (10-Q Q3 FY2026). The
  proceeds are inside net debt at 2026-06-28. The five-year base still holds 100% of the China business's cash, which is not
  filed separately. **CONVENTION of this run:** the value given is taken as 60% of the filed enterprise value, $2.4B,
  deducted from the whole-business value; rationale: it is the only filed measure of the part sold; the retained 40% and the
  licence stay in the base. It moves every figure by about $2.1 a share.
- **Net debt** at 2026-06-28 (10-Q Q3 FY2026): borrowings $13,278.6M (current $1,498.4M, long-term $11,780.2M) less cash,
  short-term and long-term investments $3,923.5M = **$9,355.1M**. Operating leases (about $12.4B undiscounted at FY2025) are
  left out, as the convention says, and belong to Q9. Shares 1,140.0M.

**The range (all-equity central, equity-only beside), per share:**

| case | base | growth, years 1 to 10 | all-equity | equity-only |
|---|---|---|---|---|
| **central, cycle (a), Nestle removed: no growth (bottom)** | 3,560 | 0% | **$45.46** | $50.71 |
| **central, cycle (a), Nestle removed: shown growth (top)** | 3,560 | 8.5% (7.9% after interest) | **$99.49** | $94.95 |
| cycle, Nestle prepayment kept as proceeds of a business sold | 3,560 | -1.1% | $40.79 to $45.46 | $42.69 to $50.71 |
| literal window FY2021 to FY2025, decline carried as the bottom (b) | 3,560 | -12.2% (halves) | $11.52 to $45.46 | $17.77 to $50.71 |
| literal window, depreciation in place of capital spending | 4,133 | -5.0% (halves) | $33.37 to $54.42 | $37.98 to $59.67 |
| literal window, in-window divestiture proceeds left out | 3,292 | -7.3% (halves) | $18.71 to $41.25 | $23.88 to $46.50 |

(The literal window's growth is measured between its halves, as `q7.py` does; measured between its end years it would be
-20.3% a year and its bottom lower still. Its end years are what specific (a) replaces.)

- **Value range (central): $45.46 to $99.49 a share** against **$90.75**; width 2.19 to one.
- **The floor first** (Q7, adopted 2026-10-10). At $90.75 the expected return on the central growth case is about 6.0% a
  year and on the no-growth case about 3.1% (the rates that discount each case to the price); the floor is about ten
  percent. On the central base, ten years of growth at 16.8% a year would be needed for the price to earn the floor. No case
  in the table earns it. The most generous reading I could construct (the best five-year average, 3,560, carried at the
  business's own revenue growth of FY2016 to FY2025, 6.4% a year) is worth $82.23 a share at the sovereign and $38.13 at ten
  percent. "there’s just a point at which we drop out of the game" **[M2003-149]**.
- **The price against the range.** The price sits inside the central range, in its upper half; only the shown-growth end
  stands above it, by about 10%. That is the opposite of "It should scream at you." **[M2009-005]**; "if you have to
  actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**.
- **Fair price (a reporting figure, never a verdict; Part VII):** **$33.48 a share** on the all-equity basis (each end of the
  central range valued at ten percent: $20.92 and $45.90 after net debt and the China deduction, averaged), after the
  company's own tax, no conversion; **$38.74** on the equity-only basis beside it. On the literal window the fair price is
  $12.49 (equity-only $20.21). No cheap price is reported.
- **No tax shelter** to price separately: the effective rates of FY2021 to FY2025 run from 21.6% to 25.9% (income tax over
  pre-tax income, 10-Ks), near the statutory rate.
- **VERDICT: OUT.** The business can be valued, and its value does not reach the price at the floor on any case the filings
  support **[M2003-149]**: the price sits inside the range, not below it **[M2009-005]**, and the growth case that lifts the
  top above the price rests on a cycle comparison whose first cycle holds the pandemic year, the kind of base the rows warn
  can "produce a breathtaking, but meaningless, growth rate" **[L2005-003]**. The width (2.19 to one) is under three, so
  the close is OUT and not TOO HARD; under the floor-first order it would be OUT whatever the width.
