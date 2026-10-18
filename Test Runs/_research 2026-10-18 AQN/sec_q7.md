## Q7 — WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is
the risk-free interest rate" **[L2000-021]**; value is "the discounted value of the cash that can be taken out of a
business during its remaining life" **[R1996-018]**, net of "are you going to have to put more cash into after you buy
it?" **[M2014-068]**. The rate: the long Treasury, 5.43% (Step 0) **[M1996-025]**. The arithmetic is in
`Test Runs/_research 2026-10-18 AQN/q7.py`, its output in `q7_output.txt` beside it; every input is typed there with its
filing.

**The base, and why it is built from the segment notes.** The consolidated cash-flow statements combine the sold
renewables business with the continuing one through FY2024 (FY2025 note 1(c)), so the five-year window FY2021 to FY2025
is built from the continuing parts the segment notes report (Regulated Services, Hydro, Corporate). *CONVENTION of this
run:* (1) the Hydro Group, reported apart only from FY2023, is carried for FY2021 and FY2022 at its FY2023 to FY2025
average ($18.3M of EBIT a year), since it then sat inside the sold group; rationale: it is 4% of the business and has no
other filed figure for those years. (2) Working capital is the consolidated figure (XBRL IncreaseDecreaseInOperatingCapital),
which includes the sold business through FY2024; rationale: no segment figure is filed, and leaving it out would flatter
the base. Each year:

| Year | EBIT (continuing, Atlantica income out, FX loss back) | after the company's 25.9% tax | Depreciation | Sustaining spending | All spending incl. acquisitions | Increase in working capital |
|---|---|---|---|---|---|---|
| 2021 | 403.4 | 298.7 | 288.2 | 406.7 (est.) | 1,013.1 | 522.0 (Storm Uri year) |
| 2022 | 464.7 | 344.2 | 325.0 | 459.2 (est.) | 1,524.6 (incl. $609.3M New York water) | 221.6 |
| 2023 | 388.9 | 288.0 | 354.1 | 500.5 (est.) | 748.7 | (86.3) |
| 2024 | 442.7 | 327.8 | 395.7 | 617.1 | 763.8 | 139.5 |
| 2025 | 497.2 | 368.2 | 400.3 | 505.0 | 608.8 | 45.7 |

Restructuring, the Kentucky termination ($46.5M, 2023) and the disallowed securitization costs ($63.5M, 2023) stay in as
real costs (Q4). The tax is the company's own: the regulated group's FY2025 provision, 25.9% (note 19), no conversion
(Q7, Whose tax); cash taxes were refunds in 2024 and 2025 and are not used as the rate. The tax-equity allocation to
non-controlling interests is left out (Q4).

**The specifics, applied.**
- *(e) Maintenance, central.* The filer's own "Sustaining" spending is filed for 2024 and 2025 only. *CONVENTION of this
  run:* for 2021 to 2023 sustaining is estimated at depreciation times the 2024 to 2025 ratio of sustaining to the
  regulated group's depreciation, 1.426; rationale: the filer's earlier "maintenance" figure was depreciation by
  definition (Q4), which the filer itself replaced with the larger sustaining figure. The depreciation variant and the
  all-spending case are shown beside. The growth spending (all spending less sustaining, $434.1M a year on average) is
  charged against the growth it buys, ten years, stopping with growth.
- *(d) Working capital.* 2021's draw of $522.0M is the year of the February 2021 winter storm, whose "qualified
  extraordinary costs" the filer later securitized (AIF 2.1.2); by (d) it is carried at the other four years' intensity
  ($80.1M) in the central case, the literal window beside.
- *(b) The series changes sign* (central owner cash: 2021 $100.1M, 2022 $(11.7)M, 2023 $227.9M, 2024 $(33.1)M, 2025
  $217.8M), so growth is measured between the halves: $44.2M to $92.4M, 27.8% a year.
- *(f) The cap.* 27.8% carried ten years would need owner cash far above any share of sales the business has earned; cut
  to the business's own sales growth, 4.63% a year (regulated group revenue plus other revenue, FY2021 $1,997.6M to
  FY2025 $2,394.4M, segment notes), below the discount rate **[M1999-067]**, **[M1997-095]**.
- *(c) Acquisitions, and the serial acquirer.* The New York water purchase (2022, $609.3M, MD&A FY2023) is the window's
  one purchase. Net purchases ($609.3M) exceed half of the central owner cash before purchases ($501.0M over five years,
  half $250.5M), so by the serial-acquirer specific the **central figure is the organic pair**: the purchase left out of
  the growth spending (which falls to $312.2M a year) and only organic growth credited. The filer reports no organic
  growth; *CONVENTION of this run:* the total sales growth, 4.63%, is used as its upper bound, which flatters the organic
  case. The default pair (purchase deducted, total growth credited) is shown beside. Q3 has stated what the added
  capital returned, and Q6 weighs the buying.
- *(a) Cycle base.* The window holds the storm year, handled by (d), and the year of the sale (2024), whose consolidated
  working capital is shown as filed.
- *A deal signed but not closed:* the Suralis sale (6-K `0001174169-26-000038`, expected $126.5M) is left out of the
  central figure; valued beside as if closed, it would cut the claims ahead of the common by at most the proceeds and
  Suralis's share of non-controlling interests, about $0.27 a share before taking away Suralis's own cash, and changes
  nothing below.

**The claims ahead of the common** (Q2 2026 balance sheet, 2026-06-30): long-term debt $520.6M current and $6,115.1M
non-current, less cash $55.0M: **net debt $6,580.7M** (operating leases left out; the securitization bonds left in);
preferred shares $184.3M; non-controlling interests $356.3M; **$7,121.3M** in all. Enterprise value at $5.25:
**$11,162.5M**. No later subsequent event in the filings read changes the debt.

**COMPUTATION.** Five-year average owner cash, all-equity basis (before interest, after the company's tax):

| Case | Average owner cash | No-growth value (whole business) | Growth case, net of growth spending | Per share, after claims |
|---|---|---|---|---|
| **Central: organic pair, sustaining maintenance, (d) working capital** | **$100.2M** | $1,845.6M | $310.9M | **$(8.85) to $(6.85)** |
| Default pair beside (purchase deducted, total growth) | $100.2M | $1,845.6M | $(610.7)M | $(10.04) to $(6.85) |
| Sustaining maintenance, literal working capital | $11.8M | $218.1M | (no growth; series changes sign twice) | $(8.97) |
| Depreciation as maintenance, (d) working capital | $245.3M | $4,516.8M | $2,160.0M | $(6.45) to $(3.38) |
| All spending (growth capped at zero, (b)) | $(333.9)M | negative | negative | $(17.24) |

In both pairs the growth case is below the no-growth case: the growth spending is worth less than its cost, so the
no-growth case is the top of the range and the growth case the bottom, as specific (e) records the inversion, "growth
can destroy value" **[L2000-023]**.

**The floor is tested first** (2026-10-10). The most generous case the run can defend, depreciation as the maintenance
charge, growth spending ignored altogether, gives an expected return at $5.25 of **3.28%** a year (the rate at which that
cash stream equals the enterprise value); the central case gives 1.38%. A single-year check beside: FY2025's operating
profit after tax alone, $368.2M, is 3.3% of the enterprise value. No case earns about ten percent at the price
**[M2003-149]**; the width test is not reached.

- **Value range (central, the organic pair): $(8.85) to $(6.85) a share against $5.25.** Default pair beside: $(10.04)
  to $(6.85); literal window beside: $(8.97).
- **Fair price (a reporting figure, never a verdict; Part VII):** each end valued at ten percent and averaged, after the
  company's own tax: **$(8.95) a share on the all-equity basis** (central, the organic pair); **equity-only $(3.70) a
  share** (owner cash after after-tax interest, $(113.5)M a year, with the preferred and the non-controlling interests
  deducted). Default pair beside: $(9.44) all-equity, $(4.18) equity-only. Both are
  below zero: at no positive price does the midpoint of the range earn the floor. No cheap price is reported.
- **Closes: OUT.** No case earns the floor at the price **[M2003-149]**; the price sits above the top of the range, which
  closes OUT however wide the range (Q7, the four specifics). "So, there’s just a point at which we drop out of the
  game." **[M2003-149]**.
- **VERDICT: OUT** **[M2003-149]**, **[M2009-005]**.

