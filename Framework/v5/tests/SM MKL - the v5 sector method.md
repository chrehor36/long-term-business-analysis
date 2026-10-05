# Company Run: Markel Group Inc. (NYSE: MKL), 2026-10-05, under the v5 sector method (TEST)
**Framework v5** (`Framework/THE FRAMEWORK v5.md`), with the method of section 3 of
`Framework/v5/CASE 2026-10-05 - a v5 sector method for insurers and float companies, for the operator's approval.md` applied
where the case says it applies. Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run under
`Framework/v5/TEST - the v5 sector method on MKL, PREREGISTRATION.md`. **This is a test of the method. It is not a run of
record and binds nothing.** Working files and the text relied on: `Framework/v5/tests/_work_SM_MKL/` (the arithmetic is
`compute.py`, its output `compute_out.txt`).

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is barred to this session by the blind rule.

**CONTAMINATION, declared.** (1) The case file says the 2026-09-02 MKL run found a double count and two answers for
component 1; known, and the point of the test. (2) `CLAUDE.md` names the barred MKL run file and research folder by path; not
opened. (3) `python tools/run.py MKL` refused the name as an insurer and printed one sentence describing the old sector
method ("values two components separately") and its path; the file was not opened, and `--shares` was passed to get the
arithmetic lines only. (4) Markel's own 10-K prints its own intrinsic-value method (a 12x multiple of three-year "adjusted
earnings" plus cash, short-term investments and equities, less debt, preferred and minorities; FY2025 10-K, "Intrinsic
Value Per Share Growth"). It is a filer's figure, read as data; nothing of it is used. (5) The session's memory index
mentions the project's queue state, with no MKL figures. Nothing else noticed.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $1,737.18 (close 2026-10-02; `tools/run.py`; aggregator, live quote only, flagged per operator rule 5).
- **Shares by class:** 12,389,958 common, no par, one class (10-Q for the period ended 2026-06-30, filed 2026-07-29,
  accession `0001096343-26-000064`; `python Screens/cover_shares.py MKL`).
- **Market cap:** $21,523.6M (arithmetic: 12.389958M x $1,737.18).
- **Sovereign for the earnings currency (USD):** 5.63%, US Treasury daily par yield curve, 30-year, 10/02/2026 (`tools/run.py`
  via `tools/sources.py`). Reporting currency USD; 73% of 2025 underwriting gross premium is on U.S. risks (10-K FY2025, note
  2(d)); the rest is chiefly euro and sterling, hedged by currency-matched bonds (10-K FY2025, "Net Foreign Exchange Gains and
  Losses"). CONVENTION C11 applied: run at the USD sovereign, exposure stated, the choice disclosed as unresolved.
- **Long rate over the method's window** (for C3 and C5): mean of the daily 30-year par yield by year, US Treasury, fetched
  2026-10-05 (`_work_SM_MKL/treasury30_annual.csv`): 2016 2.59%, 2017 2.89%, 2018 3.11%, 2019 2.58%, 2020 1.56%,
  2021 2.06%, 2022 3.11%, 2023 4.10%, 2024 4.41%, 2025 4.78%; ten-year mean 3.12%.
- **Filings read** (operator rule 4), all from SEC EDGAR, CIK 0001096343:
  - 10-K FY2025, filed 2026-02-26, `0001096343-26-000020`: Item 1; Item 7 (Capital Performance, Markel Insurance results and
    balance sheet, segment results, Consolidated Investment Results, Consolidated Underwriting Reconciliation, Liquidity, Cash
    Obligations, Critical Accounting Estimates); Item 7A (credit risk, fronting); Item 8 balance sheet, income statement,
    statement of equity, cash flows; notes 2, 6, 7, 10, 11 (reserve roll-forward, prior-year development by line, the
    ten-year claims-development tables), 15.
  - 10-Q Q2 2026, filed 2026-07-29, `0001096343-26-000064`: cover, balance sheet, Markel Insurance results.
  - 10-K FY2022 `0001096343-23-000033` (income statement 2020 to 2022, reserve roll-forward, D&A, minorities, equity-method
    note); 10-K FY2019 `0001096343-20-000039` (income statement 2017 to 2019, roll-forward, reserving policy, Markel CATCo
    review); 10-K FY2016 `0001096343-17-000046` (balance sheets 2015 and 2016, income statement 2016, roll-forward,
    reserving policy); 10-K FY2018 `0001096343-19-000074` and FY2021 `0001096343-22-000039` (Markel CATCo inquiries and
    their close; 2020 receivables); 10-K FY2024 `0001096343-25-000027` (2023 premiums receivable). 10-K FY2017, FY2020 and
    FY2023 and the 2026 proxy (`0001096343-26-000033`) were fetched; the proxy was not read, Q5 and Q6 not being reached.
  - XBRL company facts (transcription only) for the balance-sheet series behind float, each year checked against the filed
    statement where the run read one.
- **One figure cross-checked against the filed statement:** unpaid losses and LAE at 2025-12-31, XBRL $30,857.5M against the
  filed balance sheet $30,857,453K (10-K FY2025, `0001096343-26-000020`): agree. Also total assets $68,905M (`tools/run.py`)
  against $68,905,050K filed: agree.
- `tools/run.py` arithmetic lines used: price, sovereign, market cap, the ten-year balance-sheet table. **Not used:** its
  owner-earnings lines, which start from operating cash flow; Q4 step 1 of the method forbids that figure for an insurer.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what Markel's businesses and portfolio will yield, not where the quote goes
**[M1997-109]**. The market serves: the price is read against value and nothing else **[M2006-077]**. Margin of safety is the
attitude that matters most here, because the value of an insurer can swing on one convention (see Q7 below), and "if you
have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**. Who is paid to tell you:
the filer's own "intrinsic value" CAGR (15% over five years) is management's figure about management's record **[M2020-037]**.
**Contrary evidence, written down as found** **[M1997-127]**: (a) 21 consecutive years of favourable reserve development and
an underwriting profit in 18 of the last 20 years (10-K FY2025, Item 1 and Critical Accounting Estimates); (b) equity
portfolio returns of 13.5% a year over ten years and 11.0% over twenty (10-K FY2025, Consolidated Investment Results);
(c) the method's ten-year developed cost of float comes out slightly below zero (Q2 exhibit below); (d) H1 2026 Markel
Insurance combined ratio 92.8% with $273.5M favourable development (10-Q Q2 2026). Each is weighed where it bears.

## THE STANDING RULE
Nothing in a purchase of MKL shares for cash, unlevered, puts the buyer at risk of ruin; the rule binds the buyer's
financing and sizing, which this test does not set **[M2012-081]**, **[L2023-005]**, **[M2004-065]**.

---
## STAGE ZERO OF THE METHOD: is it an insurer, a holding company that owns one, or neither?
1. **Split** (CONVENTION C9, **[L2008-005]**, **[L1998-002]**). Four segments, each with its own capital (10-K FY2025, Capital
   Reconciliation, 2025-12-31): Markel Insurance, total equity $12,923M; Industrial $2,078M; Financial (State National
   fronting, Nephila insurance-linked-securities management) $2,009M; Consumer and Other $1,037M; corporate $549M. Markel
   Insurance carries float funding its investments: the method applies to it. Industrial and Consumer and Other run the
   ordinary questions. Financial is a fronting operation (State National: $3.9B of fronting premium in 2025, almost all
   ceded) and a fee-paid investment manager (Nephila): the fee business is outside the method (CONVENTION C10); State
   National's small retained underwriting ($47.0M profit in 2025) is carried with the underwriting line. A unit on the
   parent's credit is read as standing alone **[L2010-010]**: the insurance segment holds $728M of loans to a group company
   that funded non-insurance acquisitions (10-K FY2025, Markel Insurance balance sheet).
2. **Float, CONVENTION C1** (loss and LAE reserves plus unearned premiums, less reinsurance recoverables, premiums
   receivable and deferred acquisition costs) **[L1993-009]**, **[L1996-008]**. Consolidated, arithmetic from the filed
   balance sheets:

   | year-end | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
   |---|---|---|---|---|---|---|---|---|---|---|---|
   | C1 float, $M | 8,989 | 8,854 | 10,401 | 10,864 | 11,363 | 12,512 | 13,762 | 15,620 | 17,273 | 18,417 | 19,617 |
   | C1 less prepaid reinsurance premiums | 8,667 | 8,554 | 9,301 | 9,533 | 9,947 | 11,060 | 11,964 | 13,554 | 14,908 | 15,470 | 16,543 |

   At 2026-06-30 (10-Q): C1 float $20,372.6M; premiums receivable is not split out in the part of the 10-Q read and is
   estimated at the YE2025 share of receivables ($3,089.5M, arithmetic, labelled). Inputs: 2015 and 2016 recoverables from
   the FY2016 balance sheet (paid plus unpaid); 2020 premiums receivable estimated as receivables $1,930.2M less receivables
   from contracts with customers $406.4M (FY2021 10-K); 2023 premiums receivable $2,686.2M (FY2024 10-K, note 7); other
   years XBRL, first-filed. **Cross-check against the filer's own figure:** Markel reports "insurance float" of $18,827M at
   YE2025 on a definition that adds payables to reinsurers and life and annuity benefits and deducts prepaid reinsurance
   premiums (10-K FY2025, Key Financial Metrics, footnote 3); C1 adjusted the same way gives $18,793M. C1 as written is
   $790M higher than the filer's figure, almost all of it prepaid reinsurance premiums ($3,074M) not deducted: on a fronting
   book the unearned premium is matched by a prepaid reinsurance asset and is not money held. Recorded for section "What in
   the method was wrong".
3. **The two ratios, CONVENTION C2** **[L1995-015]**, **[M1995-035]**, **[M2001-053]**. At 2026-06-30: invested assets
   (investments $33,504.6M plus cash $3,423.2M plus restricted cash $644.8M) $37,572.6M; shareholders' equity $19,005.5M.
   Float to investments 0.54; investments to equity 1.98; float to equity 1.07. About half the portfolio is funded by money
   that is not the owners'. The equity behind the float is about equal to the float. Berkshire's licence was "we have so
   much net worth that, in effect, that float is just about as useful to us as equity money" **[M1995-035]**, and "no other
   insurance company could do it" **[M2023-012]**. No threshold is applied (C2), but the ratio is the fact the Q7 choice turns on.
4. **Scope, CONVENTION C10.** The life and annuity reinsurance run-off ($581.6M of benefits, Markel Insurance balance sheet)
   is a small book with no cash-out feature disclosed; it stays inside the consolidated float as filed and is not valued
   separately. Nephila's fee business is outside the method.

---
## Q1: CAN I UNDERSTAND IT? STOP.
- **The insurer's door (CONVENTION C8)**: both sides of the balance sheet readable. *Asset side:* fixed maturities $17.7B,
  96% rated AA or better; equities $13.5B, listed; short-term and cash $6.4B (10-Q; 10-K FY2025 Item 7A). Readable.
  *Liability side:* the filer publishes ten accident years (2016 to 2025) of net incurred and paid development for the
  insurance segment, with the Global Reinsurance division (in run-off since August 2025) shown separately (10-K FY2025,
  note 11(d)). Read in full. Reserves before 2016 are small ($444.4M plus $295.7M of $16.2B net). Average reserve duration
  4.1 years; 90% of a year's incurred is paid by year nine (payout table). The reserve "is the biggest single element that
  is very difficult to evaluate, even if you own the company" **[M2005-067]**, and the history shows why. AY2016 to AY2019
  (excluding Global Reinsurance) developed favourably for three or four years and then turned adverse: AY2018 went from
  $2,407.9M to $2,125.5M (2021) and back to $2,427.2M (2025), now above its first estimate. Every Global Reinsurance year
  2016 to 2021 developed adversely (+$419M in total). The surprises "can come big and they can come late" **[M1999-098]**.
  But the history is published and long enough to read the pattern. The adequacy question is open on the recent years and
  answerable on the older ones. The book is judgeable from the filer's own history, so C8 does not close the file.
- **The holding company by its parts** (the Q1 CONVENTION, **[M2023-031]** OPEN against it): Industrial (precast concrete,
  bakery equipment, car haulers, building-products distribution, fire protection, equipment rental), Consumer and Other
  (ornamental plants, homebuilding, handbags, manufactured housing, teacher sponsorship), Financial (fronting fees, an ILS
  manager's fees). Each part's ten-year economics can be pictured roughly; none turns on fast-moving technology
  **[M1998-008]**. The key variables are underwriting discipline and reserve adequacy in long-tail U.S. casualty,
  investment results, and the operating businesses' margins **[M1998-044]**.
- **VERDICT: IN.** The economics can be foreseen in outline, and the reserves can be read from the filer's own development
  history **[M2012-065]**, **[M2008-033]**. The doubt is about how good the castle is, which is Q2's question.

## Q2: WHY IS THE CASTLE STILL STANDING? STOP.
**The main exhibit, as the method directs: the cost of float** (method Q2 and Q4 step 5; CONVENTION C3; **[L1993-009]**,
**[L1993-010]**, **[L1997-011]**). Window: the ten accident years the filer publishes developed, 2016 to 2025 (C3). Each year's
result is restated by the later development of that year's reserves **[L2001-021]**. Developed accident-year result =
earned premiums less current-accident-year incurred (consolidated reserve roll-forward) less underwriting expenses, plus the
change in that accident year's ultimate from its first to its latest estimate in the note 11(d) tables (insurance segment
plus Global Reinsurance; the tables exclude unallocated LAE, are restated at 12/31/2025 exchange rates, and were recast in
2025 for a new accident-year allocation; all three limits are disclosed by the filer). Calendar results: earned premiums less
losses and LAE less underwriting expenses, consolidated, as first filed.

| $M | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | sum |
|---|---|---|---|---|---|---|---|---|---|---|---|
| calendar underwriting result | 316.6 | -207.3 | 113.9 | 280.5 | 127.6 | 628.1 | 626.6 | 132.8 | 402.3 | 502.7 | 2,923.8 |
| accident year as first reported | -188.6 | -708.7 | -437.1 | -254.7 | -478.7 | 148.3 | 459.2 | 94.2 | -53.1 | 14.3 | -1,404.9 |
| later development (+ favourable) | 131.0 | 96.7 | -75.2 | -62.9 | 229.2 | 252.2 | 278.2 | 516.6 | 590.2 | 0.0 | 1,956.0 |
| **developed accident-year result** | -57.6 | -612.0 | -512.3 | -317.6 | -249.5 | 400.5 | 737.4 | 610.8 | 537.1 | 14.3 | **551.1** |
| average C1 float | 8,922 | 9,627 | 10,632 | 11,113 | 11,937 | 13,137 | 14,691 | 16,446 | 17,845 | 19,017 | |
| developed cost of float | 0.65% | 6.36% | 4.82% | 2.86% | 2.09% | -3.05% | -5.02% | -3.71% | -3.01% | -0.08% | |
| 30-year Treasury, mean | 2.59% | 2.89% | 3.11% | 2.58% | 1.56% | 2.06% | 3.11% | 4.10% | 4.41% | 4.78% | |

Inputs: earned premiums, losses and expenses from the income statements (FY2016, FY2019, FY2022, FY2025 10-Ks); current-
and prior-accident-year incurred from the roll-forwards in the same filings; development from note 11(d) of FY2025.

- **Window average (C3):** developed underwriting +$55.1M a year on average float $13,336.8M: **developed cost of float
  -0.41%** (a small profit), against a mean long rate of 3.12%. The calendar figures give +$292.4M a year, a cost of -2.19%.
- **The halves:** 2016 to 2020, developed average -$349.8M, cost +3.35% against a rate of 2.55%. On L1997-011's test that
  half is "a lemon" **[L1997-011]**. 2021 to 2025, +$460.0M, cost -2.83%. The whole decade's developed profit rests on
  accident years 2021 to 2024, which are the least developed. At this filer they are reserved above the actuarial point
  estimate by policy: "management's philosophy is to establish loss reserves that are more likely to be redundant rather
  than deficient", releasing only "until those trends are observed over additional periods" (10-K FY2025, Critical
  Accounting Estimates; note 11(c)). AY2016 to AY2019 show what such early releases can become.
- **Where the calendar profit came from:** calendar prior-year development 2016 to 2025 totals $4,312.3M favourable
  (roll-forwards), larger than the whole ten-year calendar underwriting profit of $2,923.8M; accident years as first
  reported summed to -$1,404.9M. Of the calendar releases, about $2,357M concern accident years before 2016 (or ULAE and
  exchange effects outside the tables).

**The castle tests, with their facts.**
- *The product.* "Insurers sell a non-proprietary piece of paper containing a non-proprietary promise" **[L2003-014]**; "most
  insureds don't care from whom they buy" **[L2004-003]**. Markel says its specialty market "tends to focus less on price and
  more on other value-based considerations" and that "expertise is our principal means of competing" (10-K FY2025, Competition).
  That is the franchise of "specialized talents" **[M1999-112]**. But 71% of U.S. Wholesale and Specialty premium is placed
  by wholesale brokers and the top five brokers place 37% of underwriting premium. The customer's agent chooses the carrier.
- *The low-cost position, and the competitor row* (same metric, each company's own filed 10-K for 2025, GAAP combined ratio):

  | company | 2025 | 2024 | 2023 | 2022 | 2021 | expense ratio 2025 | accession |
  |---|---|---|---|---|---|---|---|
  | Markel Insurance segment | 94.6% | 95.5% | 98.8% | 92% | 90% | 36.1% | 0001096343-26-000020 |
  | Kinsale Capital (E&S) | 75.9% | 76.4% | | | | 20.8% | 0001669162-26-000015 |
  | RLI Corp. (specialty) | 83.6% | 86.2% | 86.6% | 84.4% | 86.8% | 38.6% | 0001104659-26-018013 |
  | W. R. Berkley (specialty) | 90.7% | 90.3% | 89.7% | | | 28.3% | 0000011544-26-000005 |

  Markel has the highest combined ratio of the four in every year shown. On the ten-year developed basis its accident
  years average about 99%. Kinsale is the low-cost operator in the same excess-and-surplus market, at an expense ratio 15
  points below Markel's. "commodity businesses have risk unless you’re the low-cost producer, because the low-cost producer
  can put you out of business" **[M1997-010]**; "a tough market helps the low-cost operator" **[L1997-021]**. Markel is not
  that operator **[L2004-007]**. (These are calendar-year ratios with their own reserve releases, and mixes differ. The row is
  read as direction, not as a precise cost gap.)
- *Widening or narrowing* **[L2005-010]**: in 2024 and 2025 Markel exited risk-managed D&O in the U.S. and Europe because "the
  rates on the business ... were inadequate"; it discontinued intellectual-property collateral insurance after $330.4M of
  losses over 2023 to 2025; and it sold the renewal rights of its reinsurance division, whose every accident year 2016 to 2021
  developed adversely (10-K FY2025). Discipline is shown in the exits. That a division and two lines had to be exited is
  evidence of where the castle was not.
- *Without the lord* **[M1995-038]**, **[L2007-006]**: the critical variables in insurance are "managerial brains, discipline
  and integrity" **[L2003-014]**. The second franchise the rows allow, "the ability to use the float effectively"
  **[M1999-112]**, is at Markel an equity portfolio led personally by the chief executive (10-K FY2025, Item 1). Its record
  (contrary evidence (b)) is a record of the person, and "if a business requires a superstar to produce great results, the
  business itself cannot be deemed great" **[L2007-006]**.
- *Contrary evidence weighed:* (a) the calendar profit record is real but, as the table shows, was paid for out of reserve
  releases; (c) a ten-year developed cost of float just below zero is the one exhibit that, alone, says the business "has
  value" **[L1997-011]**. It rests on the four least-developed years.

**VERDICT: OUT.** For an insurer, the castle the rows accept is a cost of float kept low over years **[L2001-006]** or prices
below competitors' with an underwriting profit **[M2013-006]**. Neither is shown. The developed underwriting of the insurance
part averaged about break-even over the ten years the filer publishes, with five straight developed-loss years. The
competitor row shows Markel as the highest-cost of four specialty writers in a commodity-like product. That is the high-cost
producer in a commodity field **[L1994-035]**, **[M1997-010]**, and the "mediocre results" the rows expect of an ordinary
casualty insurer **[L2014-043]**: "if you are average, you’re going to have a very poor business" **[M2000-072]**; "You have to
be in the top 10 percent" **[M2012-059]**. A lower price does not reopen it **[M2000-019]**, **[M2011-015]**. The insurance part
holds about 70% of the group's shareholders' equity ($12,923M of $18,596M at YE2025) and the float that funds about half
its investments, so its verdict closes the holding company. *(Alternative reading, recorded:* the tenuous-moat route **[M2000-019]** to TOO HARD (NATURE), if the
competitor row is discounted for mix. The run takes OUT because the cost-of-float exhibit and the competitor row point the
same way.)

**Q3 to Q10: NOT REACHED as clearances.** Under the preregistration the method's arithmetic is carried to its end below.

---
## COMPUTATION — NOT A CLEARANCE
*Everything below comes after the Q2 close. It carries no entry language. It is here because the test is of the method:
float, cost of float, component 1, component 2 and the value range, step by step as section 3 of the case gives them.*

### Q3 for an insurer (method Q3)
1. Capital behind the promises **[M2025-049]**, **[M2020-041]**: Markel Insurance equity $12,923.6M at YE2025 against 2025 net
   written premiums $8,399.7M, a ratio of 1.54 (no threshold, C2; nearest row **[M2023-013]**).
2. The three items **[L1995-015]**. *Assets:* Markel Insurance total investment return 8%, -4%, 9%, 10%, 7% for 2021 to 2025
   (filer's figure). *Liabilities:* float at a developed cost of about -0.4% over ten years; senior debt $4,303.8M at YE2025,
   interest $205.9M in 2025. *Leverage:* insurance-segment invested assets $31,328.4M on its equity of $12,923.6M, 2.4 times.
   The filer's five-year average segment ROE of 13% includes equity gains; it is read as leverage on a portfolio, not as
   underwriting return **[M2001-054]**, **[M1994-019]**.
3. Capital growth against business growth **[M1995-069]**: segment equity $8,872M (2021) to $12,923M (2025), +46%; segment
   operating revenues $6,736M to $9,353M, +39% (10-K FY2025, five-year segment table). Capital is growing faster than the
   business.
4. Non-insurance parts: capex $206.9M against depreciation $162.9M in 2025 (cash flow statement, D&A less acquired-intangible
   amortization). Growth came largely by acquisition (Valor 2024, EPI 2025; acquisitions $207.8M and $106.2M).

### Q4 for an insurer (method Q4)
1. **Operating cash flow is not the cash figure** **[L1996-008]**, **[M2023-004]**, **[M2001-030]**. In 2025 OCF of $2,761.3M
   includes an increase of $3,973.8M in unpaid losses against $2,929.2M in recoverables (cash flow statement). It is
   float growth, not earnings. **[M2016-058]** stays OPEN.
2. **Investment income out** **[L1998-002]**, **[M1997-141]**: consolidated net investment income ($367.4M, $446.8M, $734.5M,
   $920.5M, $970.4M for 2021 to 2025) and equity-method and other investment income ($15.0M, -$22.9M, -$13.6M, $58.8M,
   $112.9M) come out; gains never enter (the filer's adjusted operating income already excludes them) **[L2010-017]**.
3. **Underwriting over years, developed**: the Q2 table. Single years are not used **[M2005-067]**, **[L1993-011]**,
   **[M1997-018]**.
4. **Catastrophes stay in** **[L2002-002]**: the developed figures include them ($61.9M in 2025, $70.6M in 2024).
5. **The cost of float**: -0.41% developed, -2.19% calendar, against 3.12%. A judgment of the business, never a value term (2.7).
6. **The candor reading of the reserves.** *Direction:* calendar-year favourable in every year of the window ($4,312.3M);
   accident-year favourable in total ($1,956.0M) but adverse late on AY2016 to AY2019 (insurance segment) and on every Global
   Reinsurance year 2016 to 2021. *Size against the underwriting result:* the releases exceed the whole calendar underwriting
   profit. *Named as error?* The filer calls adverse movements "adverse loss development trends" and "social inflation"; the
   rows call development "an error in the earnings previously reported" **[L2001-021]**. *The tells:* (i) **reserves reset at
   acquisition**, stated as policy: "As part of the Company's acquisition of insurance operations, to the extent the reserving
   philosophy of the acquired business differs from the Company's reserving philosophy, the post-acquisition loss reserves
   will be strengthened until total loss reserves are consistent with the Company's target level of confidence" (10-K FY2016
   and FY2019, note on unpaid losses). This is the pattern **[L1998-034]** names. (ii) **smoothing**, contested: a stated
   policy of reserving above the actuarial point estimate and releasing slowly turns accident-year losses into calendar
   profits in 18 of 20 years; **[R1996-015]** forbids "smoothing" and in the same row asks for reserves "both consistent and
   conservative", so the row can be read either way. (iii) **The Markel CATCo reserve inquiries:** DOJ, SEC and the Bermuda
   Monetary Authority inquired into reserves at Markel CATCo Re in late 2017 and early 2018; two executives left after an
   internal review found "violations of Markel policies"; the review found no bad faith; SEC and DOJ closed without action in
   September 2021 (10-K FY2018, Item 1A and the notes; FY2019; FY2021). Recorded, not counted as a tell, since the authorities closed it.
   No discounting of reserves (10-K FY2025 note 11(b)); no earnings guidance found in the parts read. *Under Q4's two-tell
   CONVENTION:* one clear tell plus one contested tell. The reading is a weight against, short of the suspicion that makes the
   STOP **[M1995-063]**, **[M2003-029]**.
7. **Liquidity** **[L2013-003]**, **[L2014-024]**, **[M2002-073]**: estimated reserve payments within one year $6,759.1M (10-K
   FY2025, Cash Obligations) against cash, restricted cash and short-term investments of $6,401.4M at 2026-06-30, with $17.7B
   of AA-or-better bonds behind them. No cash-out features in the P&C book.

### Q7 for an insurer (method Q7)
**Component 1, the investments (CONVENTION C4)** **[L2006-002]**, **[M2016-058]**, **[M2017-077]**:

| item, 2026-06-30 unless stated | $M |
|---|---|
| fixed maturities 17,708.6 + equities 13,462.6 + short-term 2,333.4 + cash 3,423.2 + restricted cash 644.8 | 37,572.6 |
| equity-method investments at carrying value (YE2025, 10-K note 6; Hagerty's disclosed market value is $1.0B against $276.9M carried) | 737.6 |
| less deferred tax on unrealized gains: net unrealized 8,963.0 (equities 9,299.0, bonds -336.0) x 22.17%, the ratio of the filed YE2025 deferred tax liability on investments ($1,953.9M) to YE2025 net unrealized gains | -1,987.4 |
| finance operation offset by its own borrowings | none found |
| minority share | none in the investments (insurance subsidiaries wholly owned; Markel CATCo Re redeemed) |
| **Component 1, counted gross** | **36,322.8** ($2,932 a share) |
| *for comparison: counted net of C1 float ($20,372.6M)* | *15,950.2* ($1,287 a share) |

Check on the filed year-end: gross $36,223.0M at YE2025 with the filed deferred tax. The two dates differ by 0.3%. Cash held
inside the insurer is "slightly less valuable" than at the parent **[L2016-009]**: a stated judgment, no number. Of the
$37.6B, $5.4B is held in trust or on deposit for policyholders (10-K FY2025, Restricted Assets).

**Gross or net (CONVENTION C5)** **[L2011-005]**, **[L1994-025]**, **[L1993-010]**, **[M2002-006]**, **[L2013-003]**:
- *Costless:* developed cost of float over the window -0.41% against a long rate of 3.12%. **Passes.**
- *Long-enduring:* C1 float $8,854M (2016) to $19,617M (2025); it has not shrunk across the window. No sudden demands in the
  P&C book. **Passes.**
- **C5 decides: gross. Component 1 = $36,322.8M.** Recorded beside it, because the test is of the convention: the costless
  test fails on 2016 to 2020 (3.35% against 2.55%) and passes on the decade only through accident years 2021 to 2024.
  "Long-enduring" is read backwards only. The Global Reinsurance division went into run-off in August 2025 with $3,564M of
  net reserves (18% of C1 float), and C5's form cannot see a run-off already announced **[M2002-006]**. And the float is
  backed by equity of about the same size (float to equity 1.07). That is the condition under which the rows say float
  cannot be treated as equity **[M1995-035]**, **[M2023-012]**.

**Component 2, the operating earnings** **[L2006-002]**, **[M1997-141]**, **[L1998-002]**, **[L2021-003]**. The filer's
consolidated adjusted operating income (before net investment gains and acquired-intangible amortization; 10-K FY2025
five-year table) is stripped back to the non-investment, non-underwriting earnings. Then interest, minorities and the full
capital spending are charged. The underwriting line is then added once, at C6's ends.

| $M | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| adjusted operating income | 1,423.5 | 1,761.2 | 1,585.4 | 2,086.8 | 2,303.8 |
| less net investment income | 367.4 | 446.8 | 734.5 | 920.5 | 970.4 |
| less calendar underwriting result (re-entered once, below) | 628.1 | 626.6 | 132.8 | 402.3 | 502.7 |
| less equity-method and other investment income, and 2023 disposition gain | 15.0 | -22.9 | 3.3 | 58.8 | 112.9 |
| less net income to noncontrolling interests (attribution, labelled approximation) | 22.7 | 112.9 | 105.0 | 100.4 | 45.4 |
| less interest expense | 183.6 | 196.1 | 185.1 | 204.3 | 205.9 |
| = after interest, depreciation basis | 206.7 | 401.7 | 424.7 | 400.5 | 466.5 |
| less capital spending above depreciation (capex 145.2, 254.7, 258.6, 255.0, 206.9; depreciation = D&A less amortization) | -30.7 | 66.5 | 119.5 | 94.1 | 44.0 |
| **= owner cash from the operating parts, pre-tax** | **237.4** | **335.2** | **305.2** | **306.4** | **422.5** |

- Five-year average $321.3M (depreciation variant $380.0M). Shown growth on the aggregate, 2021 to 2025: 15.5% a year,
  largely bought (Valor, EPI) and swollen by Markel CATCo Re minorities' results in 2022 to 2024; capped at the discount
  rate by Q3's arithmetic (Q7 CONVENTION), 5.63%.
- Acquired-intangible amortization ($185.0M in 2025) is not charged. It is mostly customer relationships and trade names of
  operating businesses (Q4, **[L2012-003]**, **[M1997-015]**). A stated judgment, and generous.
- **Underwriting at the two ends (CONVENTION C6):** low end the lesser of zero and the developed average, $0; high end the
  developed average, +$55.1M **[L2015-002]**, **[M2011-051]**, **[M2007-001]**.
- **Component 2:** pre-tax $321.3M (low) to $376.5M (high). After tax at 21% (the filer's 2025 effective rate 21.2%):
  $253.9M to $297.4M.
- **Pre-tax or after tax?** The method's step 3 says "Pre-tax earnings" **[L2006-002]**. Q7's definition is the cash that
  can be taken out **[R1996-018]**, and L2021-003's earnings are after taxes **[L2021-003]**. The run values the after-tax
  figure and shows the pre-tax variant beside it.

**The double counts the rows forbid (method Q7 step 5), checked:** investment income is not in component 2 while the
investments are in component 1 (removed: $970.4M of net investment income and $112.9M of other investment income in 2025).
No cost-of-float charge sits beside the underwriting line (the cost of float is reported only as the Q2 exhibit). Float
earnings at the long rate are not added. The float is not added to net worth (component 1 is investments, not equity plus
float). Operating cash flow is not used. **The underwriting result enters once, in component 2, as the C6 line ($0 or
+$55.1M)**, after the calendar underwriting inside the filer's adjusted operating income has been taken out.

**The range** (Q7 CONVENTION: five-year average, growth shown and capped, ten years then no growth, discount at 5.63%)
**[L2000-024]**, **[L1993-010]**: present value of component 2 after tax, $4,509.0M (low: no growth, underwriting $0) to
$8,256.3M (high: growth 5.63%, underwriting +$55.1M).

| | value, $M | a share | price | price / bottom | top / bottom |
|---|---|---|---|---|---|
| **as the method decides (C5 gross)** | **40,832 to 44,579** | **$3,296 to $3,598** | $1,737.18 | 0.53 | 1.09 |
| pre-tax component 2 variant | | $3,392 to $3,775 | | | |
| *comparison only: component 1 net of float* | *20,459 to 24,206* | *$1,651 to $1,954* | | *1.05* | *1.18* |
| *net, pre-tax variant* | | *$1,748 to $2,131* | | | |

**The third element** **[L2010-002]**: management keeps the earnings, buys back stock with no stated price ($429.5M in 2025,
$370.7M in H1 2026; 10-K and 10-Q) and buys businesses. Recorded as a judgment, not a number. Q6 is not reached.

**The bracket check (CONVENTION C7)** **[M2012-033]**, **[L2011-005]**, **[L2011-006]**, **[L1994-025]**, on the insurance part at
YE2025. Insurance-segment invested assets $31,328.4M plus loans to group $728.0M, less a pro-rata deferred tax share of
$1,631.6M (arithmetic: the YE2025 filed DTL times the segment's share of equities, an approximation): $30,424.8M. Plus the
present value of the developed underwriting, $0 to $773.3M, and of segment services income, $219.2M: **$30,425M to $31,417M.**
Net worth $12,923.6M; net worth plus C1 float $32,147.2M; net worth plus float with prepaid reinsurance deducted, $30,730.4M.
Against C1 as written the value sits below net worth plus float, and the check passes. Against the filer-consistent float the
high end exceeds net worth plus float, and M2012-033's two reasons would be needed: "a significant underwriting profit"
(not shown: +$55.1M a year on $8.4B of premium) and "significant growth". **The check's answer depends on C1's definition.**
The value sits above net worth while the cost of float is below the long rate, so there is no contradiction with L1994-025.

**Floor and boxes** (Q7 CONVENTIONS, **[M2003-149]**, **[L2000-025]**, **[M2009-005]**): as the method decides, the range is
narrow (1.09 to 1) and the price is 53% of its bottom. On paper that is the case that "needs no pencil". Under the net
construction the price sits inside the range and the case would close OUT. **The whole of that difference is C5.** Q2 has
already closed the file, so neither reading is a clearance.

### Q9 for an insurer (method Q9), facts only
1. *One event:* property catastrophe is mostly fronted (Nephila) or reinsured. The long-tail casualty book (general and
   professional liability, 53% of 2025 earned premium) is where linked claims and court readings bite **[M2024-021]**,
   **[M2007-072]**, **[M2021-036]**.
2. *Whose promise:* underwriting recoverables $5.8B, collateral $1.5B. Fronting recoverables $8.8B, collateral $5.2B; the
   largest fronting reinsurer (Longtail Re) is unrated but over-collateralized; a related party (Hagerty Re) is unrated
   (10-K FY2025, Item 7A). In the worst case "that reinsurance probably — could likely be — not good at all" **[M2019-025]**;
   **[L2002-007]**, **[L2001-018]**.
3. *Sudden demands:* none of the cash-out kind. Redeemable noncontrolling interests of $506.1M are puttable, $122.1M in 2026.
   Debt maturities are not short (10-K FY2025, Cash Obligations) **[L2014-024]**.
4. *The portfolio against the equity behind it:* equities $13.5B against shareholders' equity $19.0B **[M1995-035]**.
5. *Currency:* euro and sterling reserves matched by same-currency bonds, the rest hedged with forwards (10-K FY2025)
   **[M2003-087]**.

---
## THE BOX
**OUT, at Q2.** The insurance part shows no castle. Its developed underwriting averaged about break-even over the ten
accident years the filer publishes (developed cost of float -0.41% against a 3.12% long rate, with five developed-loss years
first), and it has the highest combined ratio of four named specialty writers. Q7 was not reached as a clearance. For the
record, the method's arithmetic gives a value of $3,296 to $3,598 a share as C5 decides (component 1 gross), and $1,651 to
$1,954 counted net of float, against $1,737.18.

## SELF-AUDIT
- [ ] Copied to the dated file before any fetch, committed after each question: **not done.** This test writes one output
      file at a fixed path and the instruction was not to commit. Recorded as a departure from the template.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every filing fact carries its accession;
      every number is from a filing, from `tools/run.py`, or labelled arithmetic with inputs in `_work_SM_MKL/compute.py`.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; the arithmetic after it is headed
      COMPUTATION — NOT A CLEARANCE and carries no entry language.
- [x] No net-income proxy and no operating-cash-flow figure for the insurer's earnings (operator rule 5; method Q4 step 1).
      Sovereign from the Treasury. Aggregator price flagged. One estimate inside an attribution line (minorities' share, by
      net income to noncontrolling interests) is labelled.
- [x] Contrary evidence written down as found **[M1997-127]** (foundations, items (a) to (d); weighed at Q2).
- [x] No row dated after the anchor: the anchor is today; no point-in-time rule applies.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py`: PASS after writing (2026-10-05), V5 SCOPE check 0 outside citations; a script
      found no E-id in this file and all 92 M, L and R ids cited present in `principle_ledger_v5.csv`.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Q2 has no by-parts rule for a holding company. Q1 has one, a CONVENTION. The run let the insurance part's verdict close the
whole because it holds about 70% of the shareholders' equity and generates the float, and it says so. The tenuous-moat row
**[M2000-019]** and the high-cost-producer rows send a weak insurer's castle to different boxes (TOO HARD against OUT). The run
chose OUT on two concordant exhibits; another analyst could choose TOO HARD.

---
## THE TEST, SCORED
**P1, executability: PASS.** Every step of section 3 was carried out from MKL's own filings and gave its figure.
- Float (C1): $19,617.2M at YE2025, $20,372.6M at 2026-06-30.
- Cost of float (C3): -0.41% developed, against 3.12%.
- Component 1 (C4, C5): $36,322.8M.
- Component 2 (step 3, C6): $321.3M to $376.5M pre-tax, $253.9M to $297.4M after tax.
- Value range: $3,296 to $3,598 a share.

No step failed for a missing input. Four inputs were estimated and labelled, none deciding a figure by more than about 1%:
premiums receivable at 2020 year-end and at 2026-06-30; the deferred tax on unrealized gains at a quarter-end, since the filed
figure exists only at fiscal year-end; and the minorities' share. The development restatement was possible only because the
filer publishes ten accident years of claims-development tables. Those tables exclude ULAE, are restated at current exchange
rates, and were recast in 2025, and the run states all three.

**P2, no double count: PASS.** Investment income is outside component 2: 2025 net investment income of $970.4M and
equity-method and other investment income of $112.9M were removed, and gains never entered. The underwriting result enters
once, in component 2, as the C6 line ($0 at the low end, +$55.1M at the high end). The calendar underwriting inside the filer's
adjusted operating income ($502.7M in 2025) was taken out first. The cost of float is reported only as the Q2 exhibit, never
added.

**P3, one answer for component 1: PASS, in form.** C5's two tests decide the construction: costless (-0.41% against
3.12%) and long-enduring (float more than doubled; no sudden demands). The run reports one figure, $36,322.8M. The remaining
construction choices move it by less than 1% ($36,223.0M on the filed year-end deferred tax). The net figure, $15,950.2M, is
shown as a comparison and is not a second answer. **But the decided answer is fragile, and it is the answer the case itself
warns against.** It passes C5 only on the decade average. On 2016 to 2020 the costless test fails (3.35% against 2.55%), and
component 1 would fall by $20.4B (56%). The value would fall from $3,296 to $3,598 a share to $1,651 to $1,954, which turns a
price at 53% of the bottom of the range into a price inside it. Counting a float backed by about equal equity (float to
equity 1.07) as costless equity is what section 5 of the case calls "smuggled the conclusion in", and what **[M2023-012]**
says no other insurer can do. P3's rule is met, but the convention that meets it is the one that most needs amending (below).

**P4, scope: PASS.** Every judgment cites a v5 id or a CONVENTION of the case (C1 to C11) or of the framework. No v4 id
appears, and all 92 M, L and R ids resolve (checked by script). `python tools/check_framework.py` PASSES, including the
V5 SCOPE check.

**Amendments the run would ask for, though no P-rule failed:**
- **C5** should add the condition the rows themselves attach to treating float as equity: the equity behind it, the C2
  ratios read as a judgment, **[M1995-035]**, **[M2001-053]**, **[M2023-012]**. It should also require costless on fully
  developed years, or in each half of the window, not on a decade average that leans on immature years. It should read
  "long-enduring" forward as well as back, so that an announced run-off counts. Failing those, the default should be net.
- **C1** should deduct prepaid reinsurance premiums, and should state whether payables to reinsurers count. On a fronting
  book C1 overstates float by $3.1B to $3.9B, and C7's answer flips on it.

## WHAT IN THE METHOD WAS WRONG OR UNCLEAR
1. **C5 is the whole valuation.** For a filer whose float equals its equity, the gross/net switch moves value by about $1,650
   a share against a $1,737 price, and C5 throws it on two mechanical tests that ignore the equity behind the float. The case's
   own section 5 warning is not operationalized anywhere in section 3 or 4.
2. **C3 "restated by later development" has two readings.** On an accident-year basis (the claims-development tables, used
   here) the ten-year average is +$55.1M. On a calendar basis it is +$292.4M. The calendar figure carries $2.4B of releases
   on reserves set before the window. The method should name the accident-year reading, say how to treat the immature
   recent years, and say what to do when the tables exclude ULAE or have been recast.
3. **C1 omits prepaid reinsurance premiums.** See P3.
4. **Pre-tax or after tax.** Step 3 says pre-tax (from **[L2006-002]**); Q7's definition and **[L2021-003]** are after taxes.
   The two differ by $96 to $177 a share here.
5. **Step 3 does not say how to strip a filer's segment earnings.** Markel's adjusted operating income contains the calendar
   underwriting, all investment income, equity-method income and minorities' results. Unless the calendar underwriting is
   removed before the C6 line is added, underwriting is counted twice. Step 5 should list this case.
6. **C4** speaks of "the filed deferred tax", which exists only at fiscal year-end. It does not place equity-method
   investments (here $737.6M carried, Hagerty worth $1.0B at market) or say whether their income leaves component 2.
7. **C6 and the Q7 growth input.** Shown growth of 15.5% was mostly bought. The method gives no rule for acquisition-driven
   growth in the operating parts, and the cap at the discount rate is the only brake.
8. **C7 checks only the insurance part and passes anything up to net worth plus float without reasons.** It did not catch the
   dependence of the gross result on C5, and its own answer depends on C1.
9. **Q2 comes before the components, as the method says, but the cost of float is its main exhibit.** The run therefore had
   to compute C3 and the developed table before Q2 closed. That is allowed (the cost of float is not a component), but it
   should be said.
