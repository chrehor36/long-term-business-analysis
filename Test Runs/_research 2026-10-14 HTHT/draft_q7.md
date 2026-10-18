## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**, at the
long government rate, here the RMB 30-year at 2.06% (Step 0) **[L2000-021]**, with no risk premium in the rate **[M1996-025]**.
All arithmetic is in `_research 2026-10-14 HTHT/scripts/q7.py`; every input is a filed line (Step 0 table).

- **The window and the cycle, specific (a)** **[L2005-003]**. The literal five-year window is 2021 to 2025. Its first year is
  aberrational on the filer's own description: "Due to the global outbreak of COVID-19, our business was significantly impacted and
  we experienced operating losses in 2021 and 2022" (FY2023 20-F, Item 3.D). So the base is the average over the last full cycle,
  peak to peak, on the owner-cash series: peaks in 2018 (RMB 1,842 million) and 2023 (6,546), trough in 2020 (1,313 negative).
  CONVENTION of this run: the cycle's years are 2019 to 2023, the year after one peak through the next (rationale: one full turn,
  each peak counted once; 2018 to 2023 is shown beside). Cycle average, pre-interest owner cash: **RMB 1,507 million** (equity-only
  1,357; with 2018 included, 1,574). Growth "between the averages of successive cycles" cannot be measured: the filings read
  (2015 to 2025) hold no earlier full cycle, owner cash having risen from 2015 to 2018 with no trough. That is said, and the growth
  case is built as below.
- **Acquisitions, specific (c), and the serial-acquirer rule.** Cash paid for businesses in the cycle window was RMB 6,103 million
  (Deutsche Hospitality 5,060 in 2020; 742 in 2021; 244 in 2019; 57 in 2022) against owner cash before purchases of RMB 7,535
  million over the same years: more than half, so the central figure is the **organic pair** (purchases left out, organic growth
  as the filer reports it), with the default pair beside. The rule is triggered here by one large deal rather than by a habit,
  and is applied as written. The filer reports organic growth only as segment revenue: legacy Huazhu, which in 2019 was the whole
  group, grew revenue from RMB 11,212 million (2019) to RMB 20,535 million (2025), **10.61% a year**; CONVENTION of this run, that
  rate is carried as the organic growth of owner cash (rationale: it is the only organic growth figure the filer reports, and it
  is lower than the rise of owner cash from the cycle average to 2025, so it does not flatter the case). **Cap (f):** at that rate, owner cash in year ten
  is RMB 4,132 million against revenue of RMB 56,301 million at the same rate, 7.3% of revenue, below the 29.9% high (2023): no cut.
  No growth after year ten; zero nominal growth then (the PG specific).
- **Working capital, (d):** inside operating cash flow, counted. **Maintenance, (e):** the filer states a growth-spending figure only
  for 2025 to 2026 (RMB 693 million over one to two years, Item 5.B), not for the cycle years, so the all-spending case is central
  and the maintenance variant is shown with the sensitivity below. **Decline, (b):** not shown on the cycle base. **Whose tax:** owner
  cash is after the company's own tax, PRC withholding on internal dividends included (income taxes paid RMB 1,632 million, 2025).
  Two subsidiaries' 15% high-tech rates (an aggregate tax holiday of RMB 60, 47 and 98 million in 2023 to 2025, Item 5.D) end in
  2026 and 2027 unless renewed; computed at the statutory rate with the shelter's present value added, the base moves by under RMB
  60 million a year and the whole-business value by under 1%: no figure below changes at the precision shown. **Legacy DH** is
  inside the consolidated owner cash and carried at the group's rate; with its five-year adjusted EBITDA below zero, carrying it at
  no growth instead lowers the figures slightly.
- **Net debt, all-equity basis** **[L2017-004]**, at the latest filed balance sheet (2026-06-30, 6-K of 2026-08-17): borrowings RMB
  4,226 million (911 short, 3,315 long) plus finance-lease liabilities 2,993, less cash 14,249, restricted cash 142 and short-term
  investments 1,315: **net cash RMB 8,487 million**; the subsequent event that filing states, the US$275 million dividend declared
  2026-08-17 and paid in September (RMB 1,866 million at the filing's 6.7851), reduces it to **net cash RMB 6,621 million**. The
  CNY 3.35 billion bond of September 2026 adds equal cash and debt, no change. Operating-lease liabilities (RMB 27,015 million at
  2026-06-30) are left out of net debt, said so; their rent is inside owner cash. Long-term investments (RMB 1,352 million, equity
  stakes) are not counted as cash. Market value RMB 93,756 million; **enterprise value RMB 87,135 million**.

- **The floor, tested first** (CONVENTION, about 10% pre-tax as Q7 states it, after the company's own tax, "there’s just a point
  at which we drop out of the game" **[M2003-149]**). Each case valued at 10% against the enterprise value of RMB 87,135 million:

  | Case | Base, RMB m | Growth, years 1-10 | Worth at 10% (RMB m) | Earns the floor at the price? | Return at the price |
  |---|---|---|---|---|---|
  | Central, organic pair, no growth | 1,507 | 0 | 15,070 | no | |
  | Central, organic pair, growth | 1,507 | 10.61% | 31,470 | **no** | 4.2% |
  | Default pair (purchases deducted, base 286; growth not measurable) | 286 | 0 | 2,865 | no | |
  | Literal window 2021-2025, beside (sign change, halves meaningless, so no-growth alone, by (b)) | 3,992 | 0 | 39,919 | no | 4.6% |

  **No case of the range earns the floor at the price: the file closes OUT here, whatever the width.**
- **The value range, central (organic pair, at 2.06%):** whole business RMB 73,158 to 187,670 million; less net debt (net cash
  added), **RMB 25.29 to 61.60 per ordinary share, US$3.759 to 9.153 per ordinary share, US$37.59 to 91.53 per ADS**, against
  US$44.17. Width 2.4 to 1 per share (below three to one). The price sits inside the range: on the width test too this is not a
  screamer, "it’s too close to think about" **[M1996-084]**. Literal window beside: a single no-growth value of US$94.41 per ADS at
  2.06%, which does not earn the floor at the price (4.6%).
- **Sensitivity, COMPUTATION, NOT A CLEARANCE, and not a case of the range** (shown because it is the most generous reading an
  analyst could put forward, and the evidence against the OUT must be written down **[M1997-127]**): on the post-COVID years alone
  (2023 to 2025, pre-interest owner cash 6,591, growth 3.46% a year from 2023 to 2025), the expected return at the price is 9.6%; with
  the filer's growth spending added back (about RMB 347 million a year, half of RMB 693 million), 10.1%. Even the reading that sets
  aside the cycle rule clears the floor by a tenth of a point, which is the case of "the discount rate is 9.6 percent instead of 9.8
  percent — forget about the whole exercise" **[M2009-005]**.
- **Fair price (a reporting figure, never a verdict; Part VII):** each end of the central range valued at 10% and the two averaged,
  after the company's own tax. **All-equity basis (central): US$14.08 per ADS, US$1.408 per ordinary share** (RMB 9.48 per ordinary
  share; whole business RMB 23,270 million plus net cash 6,621). **Equity-only beside: US$9.87 per ADS, US$0.987 per ordinary
  share** (owner cash after interest, base 1,357). The central figure is positive, so the alert can sit on it. No cheap price is
  reported.
- **VERDICT: OUT.** Valued, and no case earns the floor at US$44.17 **[M2003-149]**; the price is inside a range of under three to
  one, not "startlingly low in relation to value" **[L2000-025]**; and the one reading that reaches the floor needs a calculator to
  find it **[M2009-005]**.

