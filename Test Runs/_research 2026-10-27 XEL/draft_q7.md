
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED (the file closed at Q5). Facts are under AFTER THE STOP.

## Q7: WHAT IS IT WORTH? NOT REACHED as a question. The owner's reporting figures follow, as the brief asks.

### COMPUTATION, NOT A CLEARANCE (the file closed at Q5; nothing here is a verdict or entry language, operator rule 3)
Built by Q7's construction as written (the range convention, the four PG specifics, specifics (a) to (f), the floor tested
first, The regulated utility as amended 2026-10-23, and Part VII's fair price). Arithmetic in
`Test Runs/_research 2026-10-27 XEL/q7_calc.py`, output in `q7_output.txt`. USD millions unless per share.

- **The window and the cash input.** FY2021 to FY2025, from the filed cash-flow statements (`0000072903-26-000009` for
  2023 to 2025; `0000072903-23-000007` for 2021 and 2022). Owner cash after interest and after the company's own tax =
  operating cash flow less stock pay less spending. The maintenance guess is depreciation plus nuclear fuel amortization
  (nuclear fuel is bought inside capital spending). The rows allow depreciation as the guess: it is "not inappropriate in
  most companies to use as a proxy for required capital expenditures" **[M1998-127]**. For a utility it is read as a floor
  **[L2011-019]**. The filing gives no maintenance figure of its own, so specific (e)'s case rests on this guess, said so.

  | FY | OCF | Stock pay | Capex | Maintenance (D&A + NFA) | Owner cash after maintenance | After all spending | Growth spending |
  |---|---|---|---|---|---|---|---|
  | 2021 | 2,189 | 31 | 4,244 | 2,257 | -99 | -2,086 | 1,987 |
  | 2022 | 3,932 | 20 | 4,638 | 2,554 | 1,358 | -726 | 2,084 |
  | 2023 | 5,327 | 25 | 5,854 | 2,567 | 2,735 | -552 | 3,287 |
  | 2024 | 4,641 | 33 | 7,364 | 2,875 | 1,733 | -2,756 | 4,489 |
  | 2025 | 4,083 | 46 | 10,908 | 3,082 | 955 | -6,871 | 7,826 |
  | 5-yr average | | | | | **1,336** | **-2,598** | **3,935** |

- **(a) The cycle base.** The first year is aberrational on the filer's own description: 2021 operating cash fell $659M,
  in the 10-K for FY2021 (`0000072903-22-000010`) "primarily due to the deferral of net natural gas, fuel and purchased
  energy costs related to Winter Storm Uri", and the deferral was recovered in 2022 and 2023 (Colorado: over 24 and 30
  months from January and April 2022). A utility has no business cycle to average over; the deferral and its recovery
  both fall inside the window, so the five-year average already nets the event and is used as the base. CONVENTION of this
  run: where the aberrational year's own reversal lies inside the window, the window average is the cycle base;
  rationale: it is the shortest span that contains the whole event, and the text's "last full cycle" does not exist here.
  Beside it, the 2022-2025 base without 2021: owner cash $1,695M.
- **(b) The growth shown.** The compound rate between the end years is meaningless (2021 is negative), so it is measured
  between the halves: 2021-2022 average $630M to 2024-2025 average $1,344M, 28.8% a year.
- **(f) The cap.** Carried ten years, 28.8% would put owner cash at about $16.7 billion, above the highest share of sales
  the business has earned in the filings read (19.3%, 2023) and above sales themselves; the text cuts any result that
  traces to an absurdity **[M1999-067]**. Cut to the business's own sales growth over the same window: revenue $13,431M
  (2021) to $14,669M (2025), 2.23% a year. Both written down. Beside it, sales growth 2020-2025 (4.94%).
- **(c) Acquisitions:** none in the window. **(d) Working capital:** inside operating cash flow, counted.
- **(e) Growth spending** = capital spending above the maintenance guess: $3,935M in year one, growing at 2.23% to $4,795M
  in year ten, none after. The maintenance guess is charged in every year of every case.
- **The regulated utility.** The deciding part (regulated electric, 88.6% of segment net income) earns a return a regulator
  allows, so the equity-only basis is central **[L2017-012]**, **[M2010-037]**. Utility debt credit: long-term debt
  (long-term, current portion and finance leases) rose from $20,143M at end-2020 to $33,634M at end-2025, $2,698M a year;
  commercial paper and cash left out; no securitization bonds found in the 10-K text read. Credited against the growth
  spending only **[L2000-035]**, capped at the deciding part's allowed debt share. The filings state allowed equity
  ratios for Minnesota electric (52.5%, verbal decision June 2026), North Dakota (52.5%), Wisconsin (52.5%) and Colorado
  electric (54.5%, verbal decision 2026-08-19), which together cover more than half of the electric rate base; weighted
  by rate base (Minnesota electric $14.0B, North Dakota $0.8B, Wisconsin taken at NSP-Wisconsin's $3.5B, Colorado electric
  $13.0B), the allowed debt share is about 46.6%. CONVENTION of this run: the electric rate base by state is not stated as
  one table, so the weights are the rate bases the filings give for each case; rationale: every stated share lies between
  45.5% and 47.5%, so no reasonable weighting moves the cap by more than a point. The cap binds: credit = 46.6% x growth
  spending = $1,834M in year one, growing and stopping with the growth spending (the uncapped $2,698M exceeds it). Beside
  it, the cap at the business's own long-term debt share of long-term capital at 2026-06-30 (61.4%).
- **The two ends, at the 5.31% Treasury rate:**
  - No-growth case (maintenance owner cash $1,336M a year, no growth spending, no credit): $25,160M, **$40.29 a share**.
  - Shown-growth case (2.23%): owner cash after maintenance grows from $1,336M; growth spending and the credit run ten
    years and stop; zero nominal growth after year ten: **$20.13 a share**.
  - The growth bought is worth less than its cost, so the order inverts: the no-growth case is the top of the range and
    the growth case the bottom. The text names this finding, in the row's words "growth can destroy value"
    **[L2000-023]**.
- **VALUE RANGE: $20.13 to $40.29 a share, against $77.86** (2026-10-26, aggregator). Width 2.0 to 1. The literal window
  is the one shown; the 2022-2025 base beside it gives $22.36 to $51.11.
- **The floor, tested first** **[M2003-149]**: at $77.86 the no-growth case yields 2.75% on the price (owner cash
  $1,336M against a market value of $48,634M), and the growth case less; no case in the range earns about ten percent at
  the price, so a Q7 reached would close OUT on the floor whatever the width. A price above the top of the range closes
  OUT by the floor convention as well.
- **FAIR PRICE (Part VII; a reporting figure, never a verdict): $11.91 a share, equity-only, central** (each end valued at
  ten percent: no-growth $21.39, growth $2.42; averaged), after the company's own tax.
  **All-equity, beside: not positive (-$46.26 a share).** Owner cash before interest (interest paid averaged $1,003M,
  added back at 79%): $2,128M; enterprise value no-growth at 5.31% $40,084M against net debt of $38,774M at 2026-06-30
  (long-term $35,948M, current portion $999M, short-term $2,510M, finance leases about $1,327M, less cash $2,010M; operating
  leases left out), $2.10 a share; the all-equity growth case, with all growth spending charged and no credit, -$37.87.
  The utility rule makes the equity-only figure central; the all-equity figure never decides alone.
- **Beside the central figures, for the operator** (none decides): growth at 2020-2025 sales growth (4.94%): range $28.45
  to $40.29, fair $13.23; growth at the low end of the filer's own EPS objective (6%; a seller's figure, see the
  foundations): $32.29 to $40.29, fair $13.84; cap at own long-term debt share (61.4%): $27.90 to $40.29, fair $15.02; the
  2025 finance-lease addition ($1,239M, non-cash) left out of the debt credit: unchanged (the cap binds); the 69.8M forward
  shares and their $5,177M minimum proceeds added: the proceeds per share (about $74) exceed the range, so adding both
  raises value per share slightly and changes no conclusion; the all-spending case (owner cash -$2,598M a year): negative.
- **Whose tax.** The company paid little income tax in the window (income tax benefit of $245M in 2025) because of
  production tax credits, which the filer flows back to customers through rates (10-K Item 7: "PTCs flowed back to
  customers (offset by lower ETR)", $172M in 2025). CONVENTION of this run: owner cash is not recomputed at the statutory
  rate; rationale: the credits are passed through to customers in rates, so their expiry would raise revenue as it raises
  tax, and the text's shelter rule assumes a credit the owner keeps.
- **Q6's buyback line:** no repurchases of common stock (none in the fourth quarter of 2025, 10-K Item 5; none in the
  cash-flow statements of the window), so the buyback test has nothing to read against the bottom of the range.
