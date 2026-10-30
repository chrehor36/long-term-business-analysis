## Q7 — WHAT IS IT WORTH? STOP.
*Arithmetic in `Test Runs/_research 2026-10-23 EVRG/q7_calc.py`, output in `q7_out.txt` beside it. Inputs: the 10-K cash-flow
statements for 2021 to 2025 (XBRL as cross-checked in Step 0), the regulatory-asset tables of the 10-Ks for 2021, 2022, 2024
and 2025, and the 10-Q balance sheet of 2026-06-30. USD millions unless a figure is per share.*

- **Basis: the regulated utility.** The deciding part is the regulated utility (Q2: one segment, all of it rate-regulated), so
  the central figure is on the equity-only basis, owner cash after interest and after the company's tax against the market
  value of the shares, $19,586.7M **[L2017-012]**, **[M2010-037]** (Q7, The regulated utility). The long-term debt raised over the
  window is credited against the capital spending it funded, up to a debt share. **The debt share:** the filing states no
  allowed capital structure from an order (the KCC's orders carry no explicit return, Item 1; the 52% equity in the Kansas
  Central and Metro applications is a request; the stipulations set minimum equity of 35% to 40%, a floor, not an allowance), so
  the rule's fallback applies, the business's own debt share at the latest filed date: long-term debt including current
  maturities over that debt plus equity at June 30, 2026, $13,811.0M against $10,223.0M, 57.5% (the 10-K's own table shows
  57% on the same definition at the end of 2025). The cap does not bind: net long-term debt raised (proceeds less repayments)
  was $3,701.0M over 2022 to 2025 against a cap of 57.5% of $9,681.9M of spending, $5,563.6M. Net, not gross, because the
  gross proceeds include refinancing of maturities, which funded no new plant. Short-term debt also rose over the window and
  is not credited (the rule names long-term debt).
- **Owner cash after every real cost** (Q4's recast): operating cash flow, less stock pay, less capital spending (net of the
  2025 nonrefundable contributions in aid of construction, $170.0M, an investing inflow, and with the 2023
  "Acquisition of Persimmon Creek, net of cash acquired", $217.9M, a wind farm bought for cash, added by specific (c)). **Maintenance**, where the filing
  allows the guess (specific (e)): depreciation and amortization from the cash-flow statement plus the yearly increase in the
  PISA "Depreciation" regulatory asset (the depreciation and carrying cost kept out of expense, Q4), on the proxy row
  **[M1998-127]**; this is likely low for a business that spent 1.4 times depreciation in 2019, before the growth plan
  **[L2023-009]**, so the maintenance-only case flatters.

  | Year | OCF | Stock pay | Capital spending | Maintenance (D&A + PISA increase) | Owner cash after maintenance | After all spending | Net long-term debt raised |
  |---|---|---|---|---|---|---|---|
  | 2021 | 1,351.7 | 15.6 | 1,972.5 | 924.9 | 411.2 | -636.4 | 65.3 |
  | 2022 | 1,801.9 | 18.8 | 2,166.5 | 990.0 | 793.1 | -383.4 | 156.8 |
  | 2023 | 1,980.2 | 17.7 | 2,551.9 | 1,086.1 | 876.4 | -589.4 | 2,005.3 |
  | 2024 | 1,983.7 | 15.2 | 2,336.6 | 1,183.6 | 784.9 | -368.1 | 602.5 |
  | 2025 | 2,045.2 | 20.7 | 2,626.9 | 1,291.7 | 732.8 | -602.4 | 936.4 |

- **Specific (a), the aberrational year.** 2021 is aberrational on the filer's own description: "a significant winter weather
  event" in which Evergy incurred $365.5M of net fuel and purchased-power costs and deferred "substantially all" of them to
  regulatory assets, and booked $94.5M of non-regulated marketing margin (FY2021 10-K `0001711269-22-000008`). A regulated
  utility has no business cycle to average over, so the rule's "average over the last full cycle" has nothing to take.
  *CONVENTION of this run (rationale: the rule names the cause, an aberrational end year, but gives no base for a business
  without a cycle; dropping the year is the least invented repair): the base is the average of the four years 2022 to 2025;
  the literal five-year window is shown beside.* The Kansas share of the Uri costs was recovered in rates inside 2022 to 2025
  OCF, which flatters the central base slightly.
- **Tax.** The company's own tax is the cash it pays, $6.1M in 2025 (effective rate 3.3%, Q4). *CONVENTION of this run
  (rationale: Q7's Whose-tax convention prices a shelter that is "real cash for its life and not after", and here the credits
  and the excess deferred taxes are passed to customers by the rate orders, the nuclear credits "expected to be refunded to
  customers in future rates" and a "net regulatory liability for future refunds" for taxes over-collected (10-K tax and
  regulatory notes), so when they end the revenue requirement rises with the tax; the row on a utility's deferred taxes says
  the same, "that helps our customer and it doesn’t help us, basically" **[M2015-030]**): owner cash is taken at the cash tax
  actually paid, and the statutory-rate restatement is shown beside.* At the filer's "approximately 22%" on 2025 pre-tax
  income of about $897.6M, the extra tax would be $191.4M a year, and the top case would fall from $65.33 to $49.64.
- **The four PG specifics and the six more, as applied.** Growth on aggregate owner cash, not per share. All spending deducted
  in the all-spending case, maintenance only in the central case (e), never both with the growth capped. After year ten, zero
  nominal growth, and the growth spending stops with the growth. (b) The shown growth of owner cash after maintenance over the
  central years is negative, 793.1 to 732.8, -2.6% a year, and is carried as negative. (c) One acquisition in the window, Persimmon
  Creek in 2023 for $217.9M cash, deducted as capital spending with the total growth credited (the default pair; the filer
  reports no organic growth to show beside); purchases are far below half of owner cash, so not a serial acquirer; the
  Sunflower Sky and Foxtrot solar assets bought from developers in 2025 are inside capital spending; the 2018 merger is before
  the window. (d) Working capital is inside operating cash flow. (e) The growth spending, $1,282.6M a year over the
  central years, of which $357.4M is equity after the debt credit, bought owner cash that fell: the growth is worth less than
  its cost, so the inversion applies, "growth can destroy value" **[L2000-023]**: the maintenance-only no-growth case is the
  top and the growth case the bottom. (f) No cap binds in the central case (negative growth); in the literal window the shown
  15.5% (off the Uri base) would carry owner cash above any share of sales the business has earned (the highest was 15.9%,
  2023), so it is cut to the business's own sales growth over the same window, 1.6%.
- **The range, central, equity-only basis, at the 5.29% sovereign** (per share on 230.567M shares):

  | Case | Owner cash a year | Value | Per share |
  |---|---|---|---|
  | Top: maintenance only, no growth | 796.8 | 15,062 | $65.33 |
  | Bottom: growth case, -2.6% for ten years, $357.4M a year of equity growth spending, then flat | 796.8 falling | 9,512 | $41.25 |
  | Beside: all spending with the debt credit, no growth (sign changes, so no growth is measurable) | 439.4 | 8,307 | $36.03 |
  | Beside, literal window 2021-2025: top / bottom (growth cut to 1.6%) | 719.7 | 13,605 / 11,841 | $59.00 / $51.36 |
  | Beside, statutory tax, top | 605.4 | 11,445 | $49.64 |
  | Beside, top with the net cash of the corporate-owned life insurance added (proceeds less premiums plus policy borrowings less repayments, 2023-2025 average $57.0M; a legacy Kansas Central programme in investing and financing) | 853.8 | 16,140 | $70.00 |
  | Beside, all-equity basis (owner cash before interest after tax at 22%, less net debt $16,476.2M): top / bottom | 1,190.7 | | $26.16 / -$34.52 |

  Net debt at June 30, 2026: current maturities $1,495.3M, notes payable and commercial paper $2,331.0M, the receivable-secured
  note $356.0M, long-term debt $12,315.7M, less cash $21.8M (10-Q); finance leases are inside the debt lines as filed;
  operating leases left out. The 10-Q states no subsequent event; the 8-Ks after it (the $600M junior subordinated notes that
  replaced a $500M term loan, the $350M Kansas Central bonds) are not added, by the rule, and would raise net debt by about
  $100M plus whatever of the $350M was not used to repay short-term debt. The convertible notes dilute nothing at any price below
  about $61.80, which covers every figure in this table but the top case.
- **The floor, tested first** (2026-10-10). At $84.95 the top case returns 796.8 / 19,586.7 = 4.07% a year with no growth, and
  every other case less (the all-spending case 2.24%, the literal top 3.67%). No case earns about ten percent: "there’s just a point at which we drop out of the game" **[M2003-149]**. The price also sits above the top of
  the range ($84.95 against $65.33), which closes OUT by the same convention however the width reads. The width (1.6 to 1) is
  narrow and is not reached.
- **Value range:** $41.25 to $65.33 a share (equity-only, the utility's central basis) against $84.95. **Closes: OUT**, no case
  earns the floor at the price.
- **Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent instead of the sovereign,
  the two averaged: top $34.56, bottom $19.51, **fair price $27.04 a share on the equity-only basis (central for a regulated
  utility)**; the all-equity figure beside it is **-$41.03** (top -$19.82, bottom -$62.25: at ten percent the unlevered owner
  cash does not cover the net debt). Both after the company's own (cash) tax; on the statutory-tax restatement the equity-only
  top at ten percent would be $26.26. No cheap price is reported.
- **VERDICT: OUT.** Valued, and the price does not clear the floor on any case **[M2003-149]**; it is not near the bottom of a
  range but a third above its top, so the screamer question **[M2009-005]** does not arise. The rows foresaw the shape: "no way
  we get rich on our utility investments" **[M2009-104]**, and of utilities that "have sold at extraordinary prices", "we can’t pay them and have it make sense" **[M2017-095]**.

