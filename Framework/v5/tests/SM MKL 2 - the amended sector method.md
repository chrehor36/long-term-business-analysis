# Company Run: Markel Group Inc. (NYSE: MKL), 2026-10-05: the AMENDED v5 sector method, repeat test
**Framework v5** (`Framework/THE FRAMEWORK v5.md`), with the insurer method of
`Framework/v5/CASE 2026-10-05 - a v5 sector method for insurers and float companies, for the operator's approval.md` applied
as AMENDED (A1 to A5 supersede the steps and conventions they name). Test design:
`Framework/v5/TEST - the v5 sector method on MKL, PREREGISTRATION.md`, pass rules P1 to P4, plus P6 from the amendment.
Governing rules: `Framework/OPERATOR-PROTOCOL.md`. **This is a test run. It is not a run of record and binds nothing.**
Working folder (filings as text, the arithmetic script and its output): `Framework/v5/tests/_work_SM_MKL_2/`
(`compute.py`, `compute_output.txt`, `results.json`).

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is barred by this test's blind rule; the run
binds nothing either way.

**BLIND RULE AND CONTAMINATION, declared.** Not opened: the first test run and its working folder, the test's RESULTS file,
the 2026-09-02 MKL run and its research folder, any other insurer run, the register, the reading list, the v4 sector method,
`PORTFOLIO.md`. Read, because the method requires it: the amendment, which states findings of the first test (that
undeducted float was $3.1B to $3.9B too high, that two readings of the underwriting were $55M and $292M a year apart, that
two tax bases were $96 to $177 a share apart, that a decade average passed a float whose first half cost more than the long
rate, and that the gross figure doubled the value). None of those figures is an input here; every figure below is computed
from MKL's filings. But I knew the direction of those findings before computing, which is an incentive to confirm them
**[M1997-127]**; where my figures agree with the amendment's description, the agreement is not independent evidence.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $1,737.18, close 2026-10-02 (`python tools/run.py MKL --shares 12.389958`; aggregator quote, flagged per
  operator rule 5).
- **Shares:** 12,389,958 common, no par, one class (`python Screens/cover_shares.py MKL`: 10-Q filed 2026-07-29, period
  2026-06-30, accession `0001096343-26-000064`). The preferred stock was redeemed in 2025 (10-K FY2025 balance sheet:
  preferred nil at 2025-12-31 against $591.9M at 2024-12-31).
- **Market cap:** $21,523.6M (labelled arithmetic: 1,737.18 x 12.389958).
- **Sovereign, USD (the earnings and reporting currency; C11 disclosure below):** 5.63%, US Treasury daily par yield curve,
  30-year, 10/02/2026 (`tools/run.py`, issuing authority). Annual means of the same series for 2016 to 2025, for the cost of
  float, were computed from the Treasury's own yearly CSV files (`_work_SM_MKL_2/treasury_<year>.csv`,
  `treasury_30y_annual.json`): 2016 2.594, 2017 2.894, 2018 3.112, 2019 2.580, 2020 1.556, 2021 2.056, 2022 3.113,
  2023 4.095, 2024 4.407, 2025 4.777 (percent).
- **`tools/run.py`:** it refuses an insurer ("Operating cash flow contains float growth ... The yield would be overstated").
  Run with `--shares`, its owner-earnings lines (OCF less capex) are **not used**: they are the cash figure the method
  forbids (Q4 step 1). Its arithmetic lines used here: price, shares, sovereign, and the ten-year balance-sheet table (Q4).
- **Filings read** (operator rule 4), all from EDGAR, CIK 0001096343:

| document | filed | accession | read for |
|---|---|---|---|
| 10-K FY2025 | 2026-02-26 | 0001096343-26-000020 | business, segments, MD&A, balance sheet, income statement, note 2 (segments), note 11 (reserves, rollforward, both loss-development triangles), note 12 (reinsurance), note 15 (taxes), repurchases, float definition and figures |
| 10-Q Q2 2026 | 2026-07-29 | 0001096343-26-000064 | balance sheet at 2026-06-30, Markel Insurance results H1 2026, Global Reinsurance run-off, Hagerty transition, the $205.3M credit loss, repurchases |
| 10-K FY2022 | 2023-02-17 | 0001096343-23-000033 | segment underwriting 2020 to 2022, income statement 2020 to 2022 |
| 10-K FY2020 | 2021-02-19 | 0001096343-21-000032 | segment underwriting 2018 to 2020, selected data 2016 to 2020 |
| 10-K FY2017 | 2018-02-23 | 0001096343-18-000042 | segment underwriting 2015 to 2017 |
| 10-K FY2023 | 2024-02-23 | 0001096343-24-000025 | life and annuity, receivables (spot checks) |
| DEF 14A 2026 | 2026-04-02 | 0001096343-26-000033 | pay design, ownership |
| 8-K | 2026-09-08 | 0001096343-26-000074 | chairman retires; CEO becomes chairman; co-presidents |
| 8-Ks | 2026-02-04, 02-26, 05-20 (two) | 0001096343-26-000008, -000021, -000046, -000050 | results release, letter posted, meeting presentation, articles amendment |

  Year-end balance-sheet items for 2015 to 2023 were screened from XBRL company facts (first-filed vintage,
  `_work_SM_MKL_2/xbrl_bs.json`) and checked against filed statements where read.
- **One figure cross-checked against the filed statement:** net reserves for losses and LAE at 2025-12-31, XBRL
  `LiabilityForUnpaidClaimsAndClaimsAdjustmentExpenseNet` $16,707.0M, equals the filed rollforward in note 11 of the 10-K
  FY2025, "Net reserves for losses and loss adjustment expenses, end of year 16,706,969" (thousands). Second check:
  `tools/run.py` shareholders' equity 2025 $18,598M equals the filed balance sheet, $18,597,756 thousand.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what the insurance operation, the portfolio and some sixty-odd operating businesses
will produce, not the quotation **[M1997-109]**, **[M2006-077]**. Who is paid to tell you: the filer publishes its own
"intrinsic value per share" (an earnings multiple of 8x to 16x plus a balance-sheet figure) and its own "insurance float";
both are read as the filer's account of itself, not as inputs **[M2020-037]**. The margin of safety is an attitude here and
arithmetic only at Q7 **[M1996-084]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) the calendar record
the filer advertises ("the eighteenth year in the last 20 years that we earned an underwriting profit", 10-K FY2025) does not
survive restatement by accident year: every accident year from 2016 to 2020 is an underwriting loss on today's developed
figures (computation block below); (2) the castle the filer describes ("Competition in the specialty insurance market tends to
focus less on price") is contradicted by its own retreat: the Global Reinsurance division sold and placed in run-off in
August 2025, the risk-managed D&O lines exited in late 2024 and early 2025, the IP collateral protection line discontinued,
and Hagerty moved to fronting on 2026-01-01; (3) a $205.3M credit loss in Q2 2026 on a fronting capacity provider in
bankruptcy (10-Q Q2 2026) shows that the $8.8B of fronting recoverables carry real counterparty risk. Written down, as the
rule asks, against the attractive look of the long calendar record.

## THE STANDING RULE
The buyer's conduct: a purchase for cash, unlevered and sized so that no outcome at MKL can force a sale, satisfies the
rule **[M2012-081]**, **[L2023-005]**; borrowed money to buy it would not **[L2014-005]**. Nothing in this test proposes a
purchase.

---
## STAGE ZERO (the method): is it an insurer, a holding company that owns one, or neither?
1. **Split.** Four reported segments with their own capital (10-K FY2025, note 2): Markel Insurance (operating revenues
   $9,353M, adjusted operating income $1,379M, total equity $12,923M in 2025), Industrial ($3,928M; $343M), Financial
   ($737M; $327M: State National fronting and its collateral-protection underwriting, Nephila and other insurance-linked
   fund managers paid in fees), Consumer and Other ($1,383M; $175M) **[L2008-005]**, **[L1998-002]**. The insurance part runs
   this method; the others run the ordinary questions as parts of a holding company (CONVENTION of Q1, M2023-031 OPEN)
   **[M2023-031]**. The Financial segment's fee businesses are outside the method (C10) and enter component 2 as ordinary
   operating earnings. No unit is read as borrowing on the parent's credit beyond the senior notes, whose interest is charged
   in component 2 **[L2010-010]**.
2. **Float (A2), constructed and reconciled**: computation block below. A2 float at 2026-06-30: **$20,859.6M**.
3. **The two ratios (C2, no threshold)** at 2026-06-30: float to invested assets 0.555; invested assets to shareholders'
   equity 1.977 (float to equity 1.098) **[L1995-015]**, **[M1995-035]**, **[M2001-053]**. Read: a little over half the
   portfolio is funded by money that is not the owners'; with about $1.10 of float per $1 of equity, the company is not in
   the position the rows describe where float is "just about as useful to us as equity money" **[M1995-035]**.
4. **Scope (C10):** a run-off life and annuity reinsurance book ($581.6M of benefits at 2025-12-31, payout annuities and
   traditional life, 10-K FY2025 note 1(q)) is outside the method; it is small against the whole and is carried in the
   filer's float figure but not in the A2 float. No cash-out features are reported **[L2013-003]**, **[L2014-024]**.

---
## COMPUTATION — NOT A CLEARANCE: float, the developed underwriting and the cost of float (measured here because Q2 reads it)
*Arithmetic only. It is placed before Q1 to Q4 close because the method makes the cost of float Q2's main exhibit; it carries
no entry language (operator rule 3).*

### F1. Float, A2 read literally, and its reconciliation to the filer's own figure
A2: float = loss and LAE reserves net of reinsurance recoverables on unpaid losses (the filer reports reserves gross) +
unearned premiums less prepaid reinsurance premiums **[L1993-009]**, **[L1996-008]** (CONVENTION A2, the two deductions).

| year-end ($M) | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026-06-30 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A2 float | 10,079 | 10,073 | 11,174 | 11,494 | 12,117 | 13,467 | 14,888 | 17,108 | 18,940 | 19,630 | 20,886 | 20,860 |
| filer's "insurance float" | | | | | | | 13,543 | 14,947 | 16,733 | 17,519 | 18,827 | |

Sources: reserves, recoverables on unpaid losses, unearned premiums and prepaid reinsurance premiums from the balance sheets
and note 11 rollforwards (2024 to 2026 read in the filed statements; 2015 to 2023 XBRL first-filed vintage); the filer's float
from the key-metrics table of the 10-K FY2025.

**Reconciliation to the filer** (A2 requires it). The filer defines float as "unpaid losses and loss adjustment expenses,
unearned premiums, payables to insurance and reinsurance companies, and life and annuity benefits, net of premium receivables,
reinsurance recoverables, prepaid reinsurance premiums, and deferred policy acquisition costs" (10-K FY2025, key metrics,
note 3). Line by line, 2025 ($M): A2 20,886.1; less premiums receivable 2,967.6; less DAC 909.5; plus payables to insurance
and reinsurance companies 1,667.9; plus life and annuity benefits 581.6; less reinsurance recoverables on paid losses 465.8
(total recoverables 14,616.3 less 14,150.5 on unpaid); rebuilt 18,792.7 against the filer's 18,827; residual 34.3 (0.2%),
unexplained by the filed lines read. 2024: rebuilt 17,488.1 against 17,519 (residual 30.9). 2022: 14,982.7 against 14,947
(residual -35.7). 2021: 13,483.2 against 13,543 (residual 59.8). So the A2 figure exceeds the filer's by about $2.0B; the
difference is the filer's deduction of receivables, DAC and paid recoverables, net of its addition of reinsurer payables and
the life book. **The A2-plus-C1 reading** (A2 with C1's deductions of premiums receivable and DAC kept) gives $17,009M at
2025-12-31, $3,877M below A2 literal. Which of these A2 means is not settled by its text: see "What in the method was wrong
or unclear", item 1.

### F2. Underwriting by accident year (A3), from the filer's loss-development tables
Calendar underwriting by year, as filed: 2016 and 2017 the U.S. Insurance, International Insurance and Reinsurance segments
(10-K FY2017, note 2); 2018 to 2020 Insurance and Reinsurance (10-K FY2020, note 2); 2021 and 2022 Insurance and Reinsurance
(10-K FY2022, note 2); 2023 to 2025 the Markel Insurance segment (10-K FY2025, note 2 and MD&A). Each year's earned premiums,
current-accident-year losses and LAE, prior-year development and underwriting expenses were taken from those tables, and the
script checks that they add to the filed underwriting profit (they do, to within $0.6M).

Development of each accident year's reserves: the two triangles of the 10-K FY2025, note 11(d) ("Markel Insurance Segment
excluding Global Reinsurance Division" and "Global Reinsurance Division"), cumulative incurred losses and ALAE net of
reinsurance, accident years 2016 to 2025. For accident year Y: development = (value at 2025-12-31) less (value at the end of
year Y), both triangles summed; the developed accident-year result = earned premiums less current-year losses booked less
expenses of year Y, less that development. CONVENTION A3 (the accident-year basis); **CONVENTION (ours, this run): an accident
year is IMMATURE while less than half of its current ultimate has been paid** (paid and ultimate from the same triangles),
because until then the figure is more reserve than payment **[L2001-021]**, **[L1997-012]**; A3 requires the flag and names
no cut-off.

| AY | earned prem. | calendar UW (filed) | prior-yr dev. in that calendar year (+ favourable) | AY result as booked | later development of this AY (+ adverse) | **AY result, developed** | AY combined, developed | paid / ultimate | flag |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 3,865.1 | 306.8 | 495.1 | -188.3 | -131.0 | **-57.3** | 101.5% | 91% | |
| 2017 | 4,248.1 | -212.9 | 492.8 | -705.7 | -96.7 | **-609.0** | 114.3% | 89% | |
| 2018 | 4,712.5 | 110.5 | 545.2 | -434.8 | +75.2 | **-510.0** | 110.8% | 86% | |
| 2019 | 5,047.7 | 269.8 | 526.9 | -257.1 | +62.9 | **-320.0** | 106.3% | 85% | |
| 2020 | 5,617.8 | 135.0 | 606.3 | -471.3 | -229.2 | **-242.1** | 104.3% | 78% | |
| 2021 | 6,507.3 | 641.2 | 486.4 | 154.8 | -252.2 | **+407.0** | 93.7% | 69% | |
| 2022 | 7,591.6 | 633.7 | 169.0 | 464.8 | -278.2 | **+743.0** | 90.2% | 51% | |
| 2023 | 8,011.5 | 92.8 | 36.7 | 56.1 | -516.6 | +572.7 | 92.9% | 46% | IMMATURE |
| 2024 | 8,130.7 | 367.0 | 454.9 | -88.0 | -590.2 | +502.2 | 93.8% | 30% | IMMATURE |
| 2025 | 8,401.3 | 455.7 | 484.0 | -28.3 | 0.0 | -28.3 | 100.3% | 11% | IMMATURE |

($M; labelled arithmetic in `compute.py`.) **Cross-check:** the triangles imply calendar-2025 development on accident years
2016 to 2024 of $515.9M favourable; the filer reports $484.0M favourable for the segment in 2025. The filer attributes the
difference to accident years before 2016 and to amounts outside the tables (note 11(d)); it is $31.9M.

**What the table shows.** Calendar underwriting 2016 to 2025 sums to $2,799.5M of profit; the same years by accident year,
developed, sum to $458.2M (all years) or a loss of $588.5M (mature years 2016 to 2022 only). The calendar profits of
2016 to 2020 came from releasing reserves set before the window, while the business written in those years lost money every
year. That is the A3 point, and in this filer it is large.

**Data caveats, confessed.** (a) In 2025 the filer recast the accident-year allocation in its international operations and
restated the history columns (note 11(d)); total ultimates were unchanged, so per-year development carries reallocation that
sums to about zero across years. (b) The 2016 to 2022 calendar figures are the old segments, which from 2018 include State
National's collateral-protection underwriting (restated Markel Insurance underwriting profit in the 10-K FY2025 is $614.3M
for 2021 and $594.3M for 2022, against $641.2M and $633.7M in the old segments); the triangles exclude it. (c) The triangles
translate at 2025 exchange rates. (d) Current-year losses booked include ULAE; the triangles carry ALAE only, so ULAE is
taken as booked.

### F3. The cost of float, by half of the window (A1 test 1)
Cost = minus the developed underwriting result divided by the average float of the same years (CONVENTION C3, the ratio),
set beside the mean 30-year Treasury yield of the same years **[L1993-009]**, **[L1993-010]**, **[L1997-011]**. The window is the
longest the filer publishes by accident year, 2016 to 2025 (C3); halves 2016 to 2020 and 2021 to 2025 (CONVENTION A1).

| span | underwriting used ($M) | sum of average float ($M-years) | **cost of float** | long Treasury, mean |
|---|---|---|---|---|
| **H1, 2016-2020, developed** | -1,738.4 | 56,631 | **+3.07%** | 2.55% |
| H2, 2021-2022 (mature years only), developed | +1,150.0 | 30,175 | -3.81% | 2.59% |
| H2, 2021-2025 with immature years as now booked | +2,196.6 | 87,741 | -2.50% | 3.69% |
| window, mature years 2016-2022, developed | -588.5 | 86,806 | +0.68% | 2.56% |
| H1, calendar (A3 not applied, shown only) | +609.2 | 56,631 | -1.08% | 2.55% |
| H2, calendar (shown only) | +2,190.3 | 87,741 | -2.50% | 3.69% |

A negative cost is a profit. **The first half's float cost more than the long government rate on developed figures; the
calendar figures, which A3 forbids, show it as profitable.** The second half shows float that paid MKL to hold it, but three of
its five years are immature, and the two most recent mature cohorts are written in the hard market of 2021 and 2022.

---
## Q1: CAN I UNDERSTAND IT? STOP.
- **Liability side (C8).** The reserve history is published (ten accident years, two triangles, paid and incurred, IBNR, claim
  counts, payout pattern; the recast disclosed) and has been read above **[M2005-067]**, **[M2008-033]**. The long-tail lines
  (general liability, professional liability including D&O, workers' compensation, run-off reinsurance) are where claims "pop
  up 10 or 20 or 30 years later" **[M1999-098]**, **[M2005-069]**, and where "almost any earnings" can be reported
  **[L2003-015]**. The history does not settle adequacy for the youngest years (flagged immature), but it does show what the
  reserving has done: initial picks set high and released on most years, with re-strengthening on 2018 and 2019 and on
  every Global Reinsurance year 2016 to 2021. That is readable. Not TOO HARD (WORK): the work is done. Not TOO HARD (NATURE):
  the deciding question (below, Q2) does not turn on the unknowable tail.
- **Asset side.** $37.6B of invested assets at 2026-06-30: $17.7B of available-for-sale fixed maturities, $13.5B of equities,
  $2.3B short-term, $4.1B cash and restricted cash (10-Q Q2 2026). Readable.
- **The other parts.** Industrial and Consumer and Other are many small manufacturing, distribution, construction and
  consumer businesses; their key variables (volume, price, capital per unit) are ordinary. Under the holding-company
  CONVENTION they are read at segment level; doubt about any one would not keep the whole out, since none matters alone
  **[M2002-092]**; **[M2023-031]** stays OPEN against the by-parts reading.
- **VERDICT: IN** **[M1995-051]**, **[M2012-065]**.

## Q2: WHY IS THE CASTLE STILL STANDING? STOP.
The insurance part is the part that matters: it holds the float and $12.9B of the $18.6B of equity, and earned $1,379M of
the $2,304M of 2025 adjusted operating income (10-K FY2025). Its castle is tested first.
- **The product.** A promise on paper that anyone can copy **[L2003-014]**; "most insureds don't care from whom they buy"
  **[L2004-003]**; average is "terrible in insurance over time" **[M2000-072]**; "a producer of mediocre results, even when very
  well managed" **[L2014-043]**; one must be "in the top 10 percent" **[M2012-059]**. MKL's specialty and E&S niche (fifth
  largest U.S. E&S writer, Lloyd's syndicate, over 100 products, 10-K FY2025) is the kind of franchise the rows allow,
  specialised talents and distribution **[M1999-112]**; whether it holds is what the evidence below must show.
- **The main exhibit, the cost of float kept low over years** **[L2001-006]**, **[L1997-011]**, **[L1998-015]**: on developed
  accident-year figures, every accident year 2016 to 2020 lost money (combined ratios 101.5% to 114.3%), and the half's float
  cost 3.07% against a long Treasury of 2.55% (F3). A single good stretch is not relied on **[L1993-011]**, **[L1997-012]**,
  **[M1996-022]**; 2021 and 2022, the two mature profitable years, were the hard market.
- **The competitor row, same metric, competitors' own filings** (GAAP combined ratio; expense ratio in brackets):

| year | MKL (underwriting segments) | W. R. Berkley, total | RLI | Kinsale |
|---|---|---|---|---|
| 2021 | 90.1% | | 86.8% (40.3) | |
| 2022 | 91.7% | | 84.4% (39.5) | |
| 2023 | 98.8% (34.4) | 89.7% (28.4) | 86.6% (39.9) | |
| 2024 | 95.5% (35.5) | 90.3% (28.5) | 86.2% (37.8) | 76.4% (20.6) |
| 2025 | 94.6% (36.1) | 90.7% (28.3) | 83.6% (38.6) | 75.9% (20.8) |

  Sources: MKL as in F2 (2021 and 2022 computed from the old segments' filed lines); W. R. Berkley 10-K FY2025, accession
  0000011544-26-000005; RLI 10-K FY2025, accession 0001104659-26-018013; Kinsale 10-K FY2025, accession 0001669162-26-000015.
  MKL's combined ratio is the worst of the four in every year shown, on calendar figures that flatter it. Its expense ratio
  is about eight points above Berkley's and fifteen above Kinsale's.
- **The low-cost test.** In a commodity-like field the way through is to be the low-cost operator **[L2004-007]**,
  **[L2000-017]**; the high-cost producer is the one the rows rule out **[M1997-010]**, **[L1994-035]**, **[M2001-013]**. On this
  row MKL is not the low-cost operator, and the rivals with lower costs also earn more on the same kind of paper.
- **Widening or narrowing** **[L2005-010]**, **[M1999-108]**: narrowing on the filings. Exits and run-offs in two years (Global
  Reinsurance sold and in run-off from August 2025, $1.0B of 2025 premium; risk-managed D&O exited after $176.9M (2024) and
  $128.8M (2025) of adverse development; IP collateral protection discontinued after $97.6M, $168.5M and $64.3M of losses in
  2023 to 2025; Hagerty moved to fronting on 2026-01-01); $326.8M of adverse development on U.S. general and professional
  liability in 2023; rates "relatively flat" in H1 2026 with decreases in U.S. property and international lines (10-K FY2025,
  10-Q Q2 2026). Against it: 2024, 2025 and H1 2026 combined ratios improved (92.8% in H1 2026), and the filer says the
  exits were underwriting discipline. Written down both ways **[M1997-127]**.
- **Would an attacker with money take it?** The rows' test **[M2011-015]**: on this row the attackers are already inside and
  earning more; the filer's own description is of competition with "large, global specialty insurance carriers".
- **The other parts.** The ventures' castles were not judged business by business; they do not rescue a failed insurance
  castle, because the insurance part is the part that matters (Q1's by-parts reading) **[M2002-092]**.
- **VERDICT: OUT.** On the evidence the castle is not keeping attackers out: over a full decade of accident years the float
  was not low-cost in the first half, the competitor row shows rivals with lower costs and better results on the same paper,
  and the business has been retreating from lines rather than widening the moat **[L2001-006]**, **[L2004-007]**,
  **[M1997-010]**, **[M2011-015]**. A castle shown open closes OUT, not TOO HARD **[M2006-013]**. *(A reader who weighs the
  2021 to 2025 improvement more heavily would say the future cannot be judged and close TOO HARD (NATURE) **[M2000-019]**; it
  is still a STOP, and the box is still not IN.)*

**The file is closed at Q2.** Everything below is the method carried to its end for the test, under COMPUTATION — NOT A
CLEARANCE, with no entry language; the verdict lines are recorded as the method would read them and are not clearances.

---
## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING. *(NOT REACHED; recorded for the test)*
- The capital behind the promises **[M2025-049]**, **[M2020-041]**: Markel Insurance total equity $12,923M against net written
  premiums $8,399.7M in 2025, 1.54 to 1 (C2, no threshold; nearest row **[M2023-013]**).
- The three items **[L1995-015]**: the assets earned net investment income of $871.5M in 2025 in the segment (plus equity
  gains, which the filer's segment ROE counts); the float cost 3.07% in H1 and was profitable in the hard-market years (F3);
  the senior debt costs about 4.8% (interest $205.9M on $4,304M, labelled arithmetic); leverage 1.98 of assets to equity.
  The filer's five-year average Markel Insurance return on equity is 13%, at a notional 22% tax and including investment gains
  (10-K FY2025); a return on equity raised by leverage is read as such **[M2001-054]**, **[M1994-019]**.
- Capital against use **[M1995-069]**: shareholders' equity grew from $8,461M (2016) to $18,598M (2025) while earned premiums
  grew from $3,865M to $8,401M; capital kept roughly in step.
- Non-insurance parts: adjusted operating income on total capital including purchased goodwill, 2025: Industrial 12.4%,
  Financial 16.3%, Consumer and Other 12.3%; on tangible capital 23.3%, 29.2%, 26.6% (10-K FY2025 key data; labelled
  arithmetic). Goodwill is forgotten for the business and counted for the allocation **[M2011-060]**, **[M2010-090]**.
- **UNDECIDED:** decent returns on tangible capital in the ventures, ordinary returns on what was paid for them, and an
  insurance return that leans on leverage and on equity-market gains **[L2009-012]**, **[M1998-081]**.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion; otherwise WEIGHING. *(NOT REACHED; recorded for the test)*
- **Balance sheets first, ten years** **[M2025-032]** (`tools/run.py` table, XBRL first-filed vintage, read against the filed
  statements for 2016, 2020, 2022, 2025): total assets $25,875M (2016) to $68,905M (2025), most of the rise from fronting
  gross-up (reinsurance recoverables $14,616M in 2025, of which $8.8B fronting) and float growth; shareholders' equity $8,461M
  to $18,598M; goodwill and intangibles $1,865M to $4,365M (acquisitions: State National, Nephila, the ventures); senior and
  other debt $2,575M (2016, 10-K FY2020 selected data) to $4,304M; retained earnings $3,526M to $15,035M; equity securities
  $13.0B against cost of $4.1B at 2025-12-31. What the figures cannot say: the adequacy of $16.7B of net reserves in long-tail
  lines **[M2005-067]**.
- **Step 1, the cash figure.** Operating cash flow ($2,761M in 2025) contains float growth and investment income; it is not
  the figure **[L1996-008]**, **[M2023-004]**, **[M2001-030]** (M2016-058 OPEN) **[M2016-058]**.
- **Step 2 and A5, investment income out, calendar underwriting out, line by line**: see component 2 under Q7. Net income
  swung by securities gains is ignored **[L2010-017]**, **[M2023-001]**, **[M2014-002]**.
- **Step 3, A3:** done in F2. **Step 4:** catastrophe losses stay in (they are in the booked current-year losses)
  **[L2002-002]**, **[M2018-024]**. **Step 5:** F3, reported as a judgment, never added to value **[L1993-009]**.
- **Step 6, the candor reading.** Direction across the window: favourable on most accident years and in total (development
  on 2016 to 2024 of $1,956.0M favourable, labelled arithmetic from F2), but adverse on 2018 and 2019 and on every Global
  Reinsurance year 2016 to 2021, with Markel Insurance accident years 2018 and 2019 first released (2,407.9 to 2,125.5 and
  2,608.5 to 2,356.5 by 2021) and then strengthened again, 2018 above its first estimate (2,427.2) and 2019 most of the way back (2,551.9). The filer names its errors as
  "adverse development" and gives causes (social inflation, severity), which is better than silence, but the rows call it what
  it is, "an error in the earnings previously reported" **[L2001-021]**; the natural bias runs to under-reserving
  **[L2002-006]**. Tells looked for: reserves moving around a sale or purchase of stock **[M2013-085]** (MKL buys in stock;
  the rows' tell is building reserves while buying, and the opposite is seen: large releases on accident years 2023 and 2024,
  $516.6M and $590.2M within one or two years, while buying; recorded, not counted as the tell); reserves reset at an
  acquisition **[L1998-034]** (none found in the years read); discounting **[M2003-103]**, **[L2001-024]** (the filer states it
  does not discount P&C reserves); published targets **[M2005-036]** (none found); smoothing **[R1996-015]**,
  **[L1994-027]** (the stated policy of reserves "more likely redundant than deficient" with steady releases is a form of
  smoothing, recorded); a struggling insurer **[L2001-022]** (not the case). Under Q4's two-tell CONVENTION, adverse
  development alone is a weighing **[M1995-063]**, **[M2003-029]**; no second tell is established.
- **Real costs.** Amortization of acquired intangibles $185.0M in 2025; the filer's "adjusted operating income" excludes it.
  Shown both ways in component 2 **[L2021-003]**, **[L2012-003]**; featuring an adjusted figure is read as a mild weight
  against, not a tell **[L2016-006]**.
- **Liquidity (step 7):** no cash-out features; liquid assets far above the payment pattern (payout 16% of incurred in year
  one, 20% in year two, from the triangles) **[M2002-073]**, **[L2013-003]**.
- **VERDICT on confusion: IN** (the filings are clear and full); **WEIGHS AGAINST** on what the calendar numbers show: they
  overstate what the business written in the window earned **[L2001-021]**, **[M1994-079]**.

## Q5: WHO RUNS IT? STOP on integrity. *(NOT REACHED; recorded for the test)*
- Integrity: no tell found in the documents read. The 10-K names its mistakes and exits plainly; the recast is disclosed
  **[M1994-008]**, **[L2024-003]**, **[M2010-081]**. **IN on integrity** (doubt alone would close it **[M2015-047]**; none found).
- Ability, read against the hand dealt **[M1994-008]**: accident-year losses 2016 to 2020, then strong 2021 to 2022 results in
  a hard market, then exits of lines that lost money. The insurer's disciplines: walking away when the premium is
  inadequate **[L2010-008]** is what the D&O and reinsurance exits claim to be; it came after the losses.
- Pay **[M1994-009]**: the 2026 proxy ties the cash award and the performance equity equally to five-year average GAAP
  operating income (which includes net investment gains; $2,596.9M for 2021 to 2025, paid at 140% of target) and five-year
  stock-price CAGR (16%, paid at 200%). Half the formula is the stock price, which the managers do not control, and the other
  half includes market gains on the equity portfolio; the rows want pay tied to what the person controls **[M2003-019]**,
  **[L1996-018]**, and an insurer's pay not tied to overall results that mix underwriting and investing **[L1996-020]**,
  **[L1999-004]**. Long holding periods (five years after vesting) and ownership guidelines are on the other side.
- Board: from 2026-09-08 the CEO is also chairman (8-K, accession 0001096343-26-000074) **[L2014-026]**.
- **Ability WEIGHS AGAINST** (narrowly), integrity IN.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING. *(NOT REACHED; recorded for the test)*
- **Part A, retention** **[R1995-009]**, **[R2009-002]**, **[M2011-072]**: diluted earnings per share kept 2021 to 2025 total
  $668.46 (176.51, -23.57, 146.98, 199.32, 169.22; no common dividend); book value per share rose from $885.72 (2020) to
  $1,477.18 (2025-12-31, 18,597.8 / 12.590 thousand shares), +$591.46; the price rose from $1,033.30 (2020 close) to $1,737.18
  (2026-10-02), +$703.88. Market leg passes, book leg does not; UNDECIDED.
- **Buybacks**: a $2B programme with no stated price (10-K FY2025; 10-Q) **[L2016-002]**; paid $2,003.05 a share on average in
  Q4 2025 and $1,857.72 in Q2 2026. Against the bottom of the Q7 range below ($1,389 on the method's construction), the prices
  paid are above it, so under Q6's CONVENTION the programme **weighs against** **[L1999-023]**, **[L2013-012]**,
  **[L2011-003]**. A buyback raises float per share **[L2021-008]**, which is worth something only for float "of the right
  sort"; H1's cost says this float has not shown that it is.
- **Part B**: as Q5, pay weighs against **[M2003-019]**, **[M2000-062]**.

## Q7: WHAT IS IT WORTH? STOP. *(NOT REACHED; COMPUTATION — NOT A CLEARANCE, carried to the end for the test)*
The value is two components and a stated judgment **[M1997-141]**, **[L1998-002]**, **[L2006-002]**, **[L2010-002]**.

### Component 1: the investments, and A1 (gross or net)
| $M | 2025-12-31 (10-K FY2025) | 2026-06-30 (10-Q Q2 2026) |
|---|---|---|
| total investments + cash + restricted cash | 37,439.3 | 37,572.6 |
| less deferred tax on investments | 1,953.9 (filed, note 15) | 1,985.6 (filed figure rolled at 21% on the $151.4M rise in net unrealized gains; labelled arithmetic) |
| **component 1, gross** | **35,485.4** | **35,587.0** |
| less A2 float | 20,886.1 | 20,859.6 |
| **component 1, net (A1 default)** | **14,599.3** | **14,727.4** |

Deferred tax deducted **[M2016-058]**, **[M2017-077]**; the deferral itself is a liability without due dates, not hidden equity
**[R1996-010]**, **[M2015-030]**. No finance operation offsets investments with its own borrowings (C4). No investment belongs
to minority holders. Cash inside the insurers is noted as "slightly less valuable" than at the parent **[L2016-009]**: the
holding company held $4.0B of the $37.6B at 2026-06-30 (10-Q), so most of component 1 sits inside regulated insurers;
stated, not priced.

**A1, the three tests, each answered from the filing.** Net is the default; gross only if all three hold **[L2011-005]**.
1. *Costless in each half* **[L1994-025]**, **[L1993-010]**, **[L1997-012]**: **fails.** H1 2016-2020 developed cost 3.07% against
   a long Treasury of 2.55% (F3). H2 passes on either reading (-3.81% mature years only; -2.50% with immature years as booked),
   but the test asks each half.
2. *Long-enduring* **[M2002-006]**, **[L2013-003]**: **fails.** A float-producing book was sold and placed in run-off in August
   2025 (Global Reinsurance; $3,564.3M of net reserves at 2025-12-31 that will run off "several additional years", 10-K FY2025
   note 11(d) and Item 1); its on-risk international marine and energy business was reinsured away on 2026-01-01 (10-Q); the
   Hagerty book moved to fronting on 2026-01-01; the D&O and IP collateral protection lines are in run-off. No sudden-demand
   features are reported, but run-off is named in terms.
3. *Equity enough behind it* **[M2001-053]**, **[M1995-035]**, **[M2023-012]**: **fails.** Float is 1.10 times equity and invested
   assets 1.98 times; the filing gives no reason why MKL is the exception the rows say no other insurer is. The filer itself
   separates "policyholder capital, or float" from "shareholder capital", which "is used to support the regulatory capital
   requirements" (10-K FY2025, Item 1, Investments).

**Component 1 is counted NET: $14,727.4M at 2026-06-30.** Gross is shown, $35,587.0M; the gap, $20,859.6M, is $1,683.6 a share.

### Component 2: operating earnings, A5 shown line by line, A3 underwriting put in once
Pre-tax, $M (10-K FY2025: adjusted operating income from the intrinsic-value table and note 2; net investment income and
interest from the income statements; Markel Insurance calendar underwriting from the segment ROE table; NCI from the income
statements; 2021 and 2022 interest and NCI from the 10-K FY2022):

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| consolidated adjusted operating income | 1,423.5 | 1,761.2 | 1,585.4 | 2,086.8 | 2,303.8 |
| less all net investment income (to component 1) | -367.4 | -446.8 | -734.5 | -920.5 | -970.4 |
| **A5: less Markel Insurance calendar underwriting** | -614.3 | -594.3 | -92.8 | -367.0 | -455.7 |
| less Velocity one-time income (an investee's sale of its operations; investment in kind) | | | | | -41.4 |
| operating earnings excluding insurance underwriting and investment income | 441.8 | 720.1 | 758.1 | 799.3 | 836.3 |
| less interest expense | -183.6 | -196.1 | -185.1 | -204.3 | -205.9 |
| less net income to noncontrolling interests | -22.7 | -112.9 | -105.0 | -100.4 | -45.4 |
| less amortization of acquired intangibles | -160.5 | -178.8 | -180.6 | -181.5 | -185.0 |
| **operating earnings for component 2, before underwriting** | **74.9** | **232.4** | **287.3** | **313.2** | **400.0** |

Five-year average: **$261.6M** (after amortization, **[L2021-003]**); **$438.8M** with amortization added back (shown as a
sensitivity; whether these intangibles deplete is not shown by the filing **[L2012-003]**). State National's
collateral-protection underwriting ($47.0M in 2025) stays inside the Financial segment's earnings: it is in no triangle, so it
is counted once, on the calendar basis (stated in the gaps below).

**The underwriting, entered once, here** **[L2015-002]**, **[M2011-051]**: developed accident-year average over the mature
years 2016 to 2022, **-$84.1M a year** (F2). C6: the low end takes the lesser of zero and that average, the high end the
average; both are -$84.1M, because the average is a loss **[M2007-001]**. (With the immature years as now booked the average
is +$45.8M; on calendar figures, which A3 replaces, +$280.0M.)

**Component 2 pre-tax: $261.6M - $84.1M = $177.5M.** **After tax (A4)** at the filer's effective rate over 2021 to 2025,
21.32% (sum of tax $2,560.0M over sum of pre-tax income $12,007.5M, labelled arithmetic): **$139.6M.**

**Growth.** Growth shown on the aggregate, 2021 to 2025, is 52.0% a year: an artefact of a 2021 base year depressed by low
operating earnings, the case the rows warn of **[L2005-003]**; it runs past the discount rate and is capped by Q3 at just under
it, 5.62% **[M1997-095]**, **[M1999-067]**, **[M2003-120]**. The underwriting is carried flat at both ends.

### The range (Q7 CONVENTION: ten years at the growth, then zero nominal growth, at 5.63%)
| | low end (no growth; UW -84.1) | high end (growth 5.62% capped; UW -84.1) |
|---|---|---|
| present value of operating earnings after tax | 3,655.3 | 5,708.7 |
| present value of underwriting after tax | -1,174.8 | -1,174.8 |
| component 2 value | 2,480.4 | 4,533.8 |
| **+ component 1 net** | 14,727.4 | 14,727.4 |
| **value, $M** | **17,207.8** | **19,261.2** |
| **per share** | **$1,388.85** | **$1,554.58** |
| shown only: + component 1 gross instead | $3,072.44 | $3,238.17 |

**Value range: $1,389 to $1,555 a share against a price of $1,737.18.** Width 1.12 to 1.

**The floor (pre-tax, A4 keeps the pre-tax figure for it).** The price less component 1 net is $6,796.2M paid for component 2;
its pre-tax earnings of $177.5M are a 2.61% yield (5.22% with amortization added back), far under about ten percent
**[M2003-149]**, **[L2002-020]**, **[M1994-004]**.

**The bracket check (C7), insurance part** **[M2012-033]**, **[L2011-005]**, **[L2011-006]**, **[L1994-025]**: Markel Insurance
net worth $12,923M (2025-12-31); net worth plus A2 float $33,809M. The components' value of the insurance part, with its
invested assets taken as total invested assets less the holding company's $4.4B (10-K FY2025 MD&A, rounded; labelled
approximation): net $9,024M, gross $29,911M. The net value sits below net worth while H1's cost of float exceeded the long
rate, which is what L1994-025 and L2011-006 lead one to expect; no contradiction to resolve. Neither figure exceeds net worth
plus float, so M2012-033's two reasons are not needed.

**The third element** **[L2010-002]**: down, stated. The retained money's recent use (buybacks above the range, acquisitions of
businesses earning about 12% on what was paid) does not argue for a premium; the insurance capital sits behind a float whose
cost has not been shown to stay below the long rate. No number is attached.

**Sensitivities (shown, not used for the close), per share:**

| case | low | high |
|---|---|---|
| the method's figure (net A2, after amortization, UW -84.1) | 1,389 | 1,555 |
| amortization added back | 1,589 | 1,867 |
| float A2 plus C1's deductions (receivables, DAC) | 1,702 | 1,868 |
| float on the filer's construction | 1,555 | 1,721 |
| float A2 plus C1 and amortization added back | 1,902 | 2,180 |
| UW high end with immature years as booked (+45.8) | 1,389 | 1,701 |
| calendar UW (A3 not applied), 0 / +280.0 | 1,484 | 1,965 |
| debt principal deducted in component 1, interest added back to component 2 | 1,256 | 1,546 |
| component 1 gross (A1 not applied) | 3,072 | 3,238 |
| gross, calendar UW, amortization added back (the uncorrected method) | 3,367 | 3,961 |

- **Close as the method reads it: OUT.** The price sits above the top of the range, so the expected return at the price is
  below the floor **[M2003-149]**, **[M2009-005]**; the range is narrow, so not TOO HARD **[L2000-025]**. On every net
  sensitivity the price is inside the range or at most 9% below its bottom: never a screamer **[M1996-084]**, **[M1995-115]**.
  Only the gross construction, which A1 refuses, puts the price far below value. The A1 fork is therefore the whole of the
  difference between OUT and a screamer, and A1 decides it.

## Q8: BETTER THAN THE ALTERNATIVES? STOP. *(NOT REACHED)*
The 30-year Treasury yields 5.63%; the price buys component 2 at a 2.6% pre-tax yield on the method's figures. It would lose
to the bond **[M1997-089]**, **[M2007-095]**.

## Q9: COULD IT RUIN US? WEIGHING. *(NOT REACHED; the method's readings recorded)*
1. *One event* **[M2024-021]**, **[L2001-008]**, **[M2003-034]**: Middle East conflict losses $76.0M in H1 2026 across terrorism,
   energy and marine war (10-Q); catastrophe property and Nephila-fronted property-catastrophe programmes.
2. *Worst case against capital* **[L1994-028]**, **[M2019-025]**: equity $19.0B against net reserves $16.8B; the licence to
   concentrate does not transfer **[M2023-012]**.
3. *Whose promise* **[L2002-007]**, **[L2001-018]**, **[L2008-009]**, **[M2003-084]**: reinsurance recoverables $15.8B at
   2026-06-30; fronting recoverables $8.8B at 2025-12-31, the largest single reinsurer Longtail Re at 26% of them, much of the
   rest unconsolidated Nephila-managed entities, related parties (10-K FY2025 note 12). A capacity provider is in bankruptcy and
   produced a $205.3M credit loss in Q2 2026 (10-Q note 7). The worst-case warning is no longer hypothetical here.
4. *Sudden demands* **[L2014-024]**: none reported; the life and annuity run-off carries longevity risk on $581.6M.
5. *Uncapped and stretched liabilities* **[L2000-005]**, **[M2007-072]**, **[M2021-036]**: long-tail GL, PL and D&O; social inflation
   named by the filer.
6. *The portfolio* **[L2019-002]**: $13.5B of equities on $19.0B of equity; high-grade fixed maturities.
7. *Currency* **[M2003-087]**: the filer states its foreign-currency reserves (mainly EUR and GBP) are matched by securities in
   the same currencies (10-K FY2025 MD&A). C11: run at the USD sovereign, disclosed.
8. Debt **[M1995-104]**, **[L2014-023]**: $4.4B of senior and other debt, 19% of capital; interest covered many times by
   operating earnings. **WEIGHS AGAINST** on item 3.

## Q10: THE FAT PITCH? WEIGHING. *(NOT REACHED)*
Inaction **[M1996-006]**, **[M2003-070]**.

## Q12 (optional): not asked.

---
## THE BOX
**OUT, decided at Q2** (the castle question): the float cost more than the long government rate across the first half of a
decade of developed accident years, the competitor row shows MKL with the highest costs and the weakest results of four
specialty writers, and the filings show retreat from lines rather than a widening moat. Carried to the end for the test, Q7
would also close OUT: **$1,389 to $1,555 a share against $1,737.18.**

## SELF-AUDIT
- [x] Written to the test's named file; not committed (the task forbids commits). Write-early not applied: single session.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by script after writing; no v4 id; every filing fact carries its
      document and accession.
- [x] The order kept; the first STOP (Q2, OUT) closed the file; everything after it is under COMPUTATION — NOT A CLEARANCE.
- [x] No net-income proxy; operating cash flow refused as the insurer's cash figure; the sovereign from the Treasury; the price
      flagged as an aggregator quote.
- [x] Contrary evidence written down as found **[M1997-127]** (Foundations, Q2).
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` used.
- [x] `python tools/check_framework.py` run after writing (PASS; see the reply).

---
# THE TEST, SCORED

**P1, executability: PASS.** Every step of section 3 as amended gave its figure from MKL's own filings: float (A2, $20,859.6M at
2026-06-30, reconciled to the filer's own $18,827M at 2025-12-31 with a residual of 0.2%); the developed underwriting by
accident year (A3, ten years, from both triangles); the cost of float in each half (3.07% against 2.55%; -3.81% or -2.50%
against 2.59% or 3.69%); component 1 gross and net ($35,587.0M; $14,727.4M); component 2 pre-tax and after tax ($177.5M;
$139.6M); a value range ($1,389 to $1,555). No step lacked an input document. Three steps needed a choice the method does not
make, each made by a stated convention of this run: the immaturity cut-off (A3 names none), the insurance part's invested
assets for the bracket check (no filed segment figure; total less the holding company's $4.4B), and the scope of the old
segments before 2023 (they include State National's underwriting, which the triangles exclude). None is a missing input.

**P2, no double count: PASS.** All net investment income ($970.4M in 2025, consolidated) is removed from component 2, and the
one-time investee gain ($41.4M) with it; the Markel Insurance calendar underwriting is removed line by line before the
developed accident-year result is put in (A5); the underwriting enters the value once, in component 2, as the C6 ends
(-$84.1M a year). The cost of float is reported at Q2 and A1 and never added. Investments are counted net, so float earnings
are not added beside them. One adjacent issue is not a double count but is unclear (item 4 below): the float is deducted at
face in component 1 while the debt is carried only through its interest in component 2.

**P3, one answer for component 1: PASS.** A1 decides the fork it was written for. All three tests fail on the filing, so the run
reports one figure, net, $14,727.4M; gross is shown and not used. The gap is large ($1,683.6 a share, the difference between a
range of $1,389 to $1,555 and one of $3,072 to $3,238) and the conventions close it. **A residual fork remains inside "net"**:
A2's text supersedes C1's construction without saying whether C1's deductions of premiums receivable and DAC survive. Read
literally (applied here) float is $20,859.6M; with C1's deductions kept it is about $3.9B lower, which moves component 1 by
about $310 a share. It does not change the box (the range becomes $1,702 to $1,868, price inside it), so it does not make P3 fail
as P3 is worded, but a stricter grader could call it a second construction. Named for amendment (item 1).

**P4, scope: PASS** on this file: every judgment cites a v5 id or names a CONVENTION (the case's C1 to C11 and A1 to A5, Q7's
range and floor conventions, Q4's two-tell line, Q6's buyback reading, the holding-company reading, and this run's immaturity
cut-off); no E-id appears; every M, L and R id resolves in `principle_ledger_v5.csv` (script check after writing); check 7 of
the acceptance test passes.

**P6, component 1 defended on A1: PASS.** Both figures shown (gross $35,587.0M, net $14,727.4M; $3,072 and $1,389 a share at
the low end). Each test answered from the filing: costless in each half, fails on H1 (3.07% against 2.55%, F3); long-enduring,
fails (Global Reinsurance sold and in run-off from August 2025, 10-K FY2025 Item 1 and note 11; Hagerty to fronting and
reinsurance of the on-risk marine and energy book, 10-Q Q2 2026); equity enough behind it, fails (float 1.10 times equity, and
the filing offers no reason MKL is the exception **[M2023-012]**). Any one failure would have decided it.

**Verdict on the rules as pre-registered:** P1, P2, P3 and P4 hold, and P6 holds. The amended method passes on this repeat, with
the defects below recorded before adoption.

# What in the method was wrong or unclear
1. **A2 does not say whether C1's deductions survive.** "Supersedes the construction in CONVENTION C1" can be read as replacing
   C1 (reserves net plus unearned net of prepaid: $20.9B) or adding to it (also less premiums receivable and DAC: about $17.0B).
   L1996-008's "money we hold but don't own" **[L1996-008]** argues for deducting premiums not yet collected and acquisition
   costs already paid; the filer's own figure ($18.8B) sits between. The choice moves component 1 by about $3.9B, $310 a share.
   Amend A2 to state the full list of deductions and additions.
2. **A3 names no cut-off for "immature".** This run used "less than half of current ultimate paid". On it, three of the five
   years of the second half are immature, so "costless in each half" is tested on two years for H2. Amend A3 (or A1) to fix the
   cut-off and to say how a half with immature years is scored.
3. **A3 does not say how to restate when the triangles do not match the calendar segments.** MKL re-segmented in 2025, recast
   its accident-year allocation in 2025, and its triangles exclude State National while the old segments include it. The method
   should say which earned premiums and expenses pair with which triangle, and that a recast is disclosed and carried as
   reallocation.
4. **Debt and float are treated inconsistently under "net".** A1 deducts float at face, "as book value treats it", but component
   1 does not deduct the senior debt, whose interest is charged in component 2 (L2021-003's "after interest"). Deducting the debt
   too and adding the interest back moves the range to $1,256 to $1,546. Neither is a double count; the method should pick one
   treatment for every interest-bearing or float liability.
5. **Q7's growth convention breaks on a depressed base year.** Growth shown was 52% a year because 2021 operating earnings were
   low; the cap (just under the discount rate) then sets the high end, which is the cap, not anything shown **[L2005-003]**. The
   convention needs a base-year test, or growth measured on a trend rather than the end years.
6. **Amortization of acquired intangibles is left to choice.** L2021-003 counts it; Q4 allows adding back what does not deplete
   **[L2012-003]**; the filer gives no basis to tell which. It moves the range by $200 to $300 a share. The method should set a
   default.
7. **The floor is not defined for a two-component value.** The run read it as component 2's pre-tax yield on the price less net
   component 1; a reader could instead set total expected return against the whole price. The method should say which.
8. **State National's underwriting** (in the Financial segment, outside the triangles) is counted on the calendar basis because
   no developed figure exists. A5 covers only underwriting for which a triangle exists; it should say so.
9. **The bracket check (C7) needs the insurance part's invested assets**, which the filer does not report by segment; the run
   approximated. Say what to do when they are not filed.
10. **The Q2 exhibit precedes Q4.** The method makes Q4's cost of float Q2's main exhibit, so a run must compute before Q1 to Q4
    close; this run headed it COMPUTATION — NOT A CLEARANCE. The method should say that this is the expected order.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
The template's position note asks the run to check `PORTFOLIO.md`, which this test's blind rule forbids; it was declared as not
checked. Q2 gives no rule for a holding company whose principal part fails while its other parts were not judged; the run
closed on the part that matters, by the by-parts reading of Q1, which is a CONVENTION and not a row.
