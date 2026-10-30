
## Q7: WHAT IS IT WORTH? STOP.
The three questions, "How certain are you that there are indeed birds in the bush? When will they emerge and how many
will there be? What is the risk-free interest rate (which we consider to be the yield on long-term U.S. bonds)?"
**[L2000-021]**, answered as a range: "working with a range of possibilities is the better approach" **[L2000-024]**.
Arithmetic in `q7_calc.py`, output in `q7_calc_output.txt`.

- **The cash input** (the framework's CONVENTION: five-year average of owner cash after every real cost). Because the
  capital structure changed after the window (net debt from about $0.9B at 2026-03-31 to about $2.1B in July 2026), each
  year's owner cash is put on an all-equity basis by adding back interest paid after tax at 25%, and the net debt is
  subtracted at the end. **CONVENTION of this run**, rationale: the five-year average of after-interest owner cash would
  carry the old, smaller interest bill against the new, larger debt; the rows value a purchase "on an all-equity basis"
  **[L2017-004]**. Unlevered after-tax owner cash: FY2022 287.2, FY2023 250.2, FY2024 272.8, FY2025 267.9, FY2026 268.4;
  **average $269.3M**. Pre-tax (owner cash + interest paid + income taxes paid): 349.2, 304.4, 348.2, 332.0, 325.3;
  average $331.8M.
- **The purchases after the window.** Added at the stated EBITDA less tax at 25% and no capital spending: Breathe Right
  $95M (the seller's twelve months to December 2025, from the deal presentation, not an audited figure) and LaCorium
  $12M ("including the benefits from anticipated synergies"), together $80.3M after tax, $107.0M pre-tax. **CONVENTION of
  this run**, rationale: the businesses are owned and their debt is counted, so leaving them out would value the debt
  and not the asset; their figures are the seller's and management's, so two stress variants are shown below. No capital
  spending is assumed because the acquired brands come with contract-manufacturing agreements and no plants (10-Q Note 2).
  **Pro forma base: $349.6M after tax, $438.8M pre-tax, unlevered.**
- **Net debt:** face debt $2,045.0M at 2026-06-30 plus $95.0M borrowed 2026-07-01 = $2,140.0M; cash $89.1M less about
  $55.0M paid for LaCorium from cash = $34.1M; finance-lease liabilities $20.6M (2026-03-31); **net $2,126.5M** (10-Q
  `0001295947-26-000042`; the July note exchange of $400M for $400M is neutral). Shares 47,374,522.
- **The growth input.** Shown on aggregate unlevered owner cash, FY2022 to FY2026: **-1.68% a year**. The window begins on
  a year the filer calls a recovery from COVID-depressed categories (organic +10.1%, FY2022) and ends on a year cut by
  the Clear Eyes shortage (organic -4.5%, FY2026), so a **whole-cycle variant** is shown with the top end at the filer's
  own organic revenue growth over FY2016 to FY2026, **+1.30% a year** (geometric mean of the eleven figures at Q2; a
  CONVENTION of this run, rationale: both ends of the five-year window are abnormal years named as such by the filer, and
  organic revenue is the longest record of the brands' own growth). No case is carried above the growth shown in the
  record, and none past the discount rate **[M1997-095]**.
- **The range at the long government rate, 5.66%** (ten years at the growth input, then zero nominal growth, discounted
  throughout; equity = value less net debt; per share):

| case | growth | enterprise value | equity | per share |
|---|---|---|---|---|
| shown decline (bottom) | -1.68% | $5,410M | $3,284M | **$69.32** |
| no growth (top of the five-year range) | 0.00% | $6,176M | $4,050M | **$85.48** |
| whole-cycle variant (top) | +1.30% | $6,848M | $4,721M | **$99.65** |
| stress: purchased brands worth nothing, their debt counted | -1.68% to +1.30% | | | $43.10 to $66.47 |
| stress: purchased brands worth exactly what was paid | -1.68% to +1.30% | | | $68.32 to $91.70 |

  Width: top over bottom 1.23 (five-year) and 1.44 (whole-cycle), far inside the framework's three-to-one line, so the
  range is narrow enough to decide on, not TOO HARD.
- **The floor** (the framework's CONVENTION: about ten percent pre-tax on the price paid, as the speakers stated and
  qualified it: "we don’t want to buy equities where our real expectancy is below 10 percent" and "And it’s arbitrary."
  **[M2003-149]**; "at least 10% pre-tax returns" **[L2002-020]**; a figure "we are guessing at our future opportunity cost"
  **[M2003-151]** and that cheap money moves "a little" **[M2016-078]**). Applied on the all-equity basis, the price paid
  being the market value plus the net debt the buyer of the whole would assume ($2,160.8M + $2,126.5M = **$4,287.3M**):

| case | expected pre-tax return at $45.61, all-equity basis |
|---|---|
| shown decline | **9.11%** |
| no growth | **10.24%** |
| whole-cycle variant | **11.15%** |

- **Reading the two together.** The price, $45.61, is 34% below the bottom of the per-share range, but the per-share
  discount is magnified by $2.1B of debt standing ahead of the equity; on the whole business the price is 21% below the
  bottom of the range and 31% below its no-growth value. The rows ask for "a big discount from that present value
  calculated using the risk-free interest rate" **[M1997-126]**, and a larger one as the business is less certain: "the
  more volatile the business is [...] the larger the margin of safety" **[M1997-080]**. Here the moat is narrow and partly
  eroding (Q2), the purchases have earned about 8% (Q3), and supply and retailer concentration are live (contrary
  evidence 1 to 3). The floor states the same thing in one number: at this price the business is expected to earn about
  10% pre-tax in the central case, 9% if the five-year decline continues, 11% if the long organic record resumes. That is
  a calculation to tenths of a percent, the case the rows tell us to leave: "forget about the whole exercise"
  **[M2009-005]**; "it’s too close to think about" **[M1996-084]**. On the levered basis the equity's expected return is higher, but only because the lenders stand
  first; the rows evaluate "on an all-equity basis" **[L2017-004]**.
- **VERDICT: OUT.** Valued, narrow range, price well below the range at the long rate, but the expected return on the
  whole business at the price sits on the ten-percent floor in the central case and below it in the shown-decline case:
  not a screamer, a pencil case, quit on under the framework's floor **[M2003-149]**, **[M2009-005]**.

**Reporting at the owner's request (not a rule change). COMPUTATION, NOT A CLEARANCE** (the file closed OUT at Q7):
- **(a) VALUE RANGE:** **$69.32 to $85.48 a share** (five-year convention, shown decline to no growth, at 5.66%);
  **whole-cycle variant $69.32 to $99.65** (top end at the FY2016 to FY2026 organic rate, because both ends of the
  five-year window are abnormal years). Against the price of $45.61.
- **(b) FAIR PRICE: $47.74 a share.** The price at or below which the central case (no growth, pro forma pre-tax
  unlevered owner cash of $438.8M) earns 10% pre-tax on the whole business (enterprise value $4,388M less net debt
  $2,126.5M). Tax treatment: "pre-tax" means before income tax and before interest (owner cash plus interest paid plus
  income taxes paid, as in the five-year table), measured on market value plus net debt; at a 25% tax rate the
  after-tax equivalent is about 7.5%. The same test in the shown-decline case gives $37.87; in the whole-cycle case $56.32.
  The price is about 4% below the central fair price.
- **(c) CHEAP PRICE: $16.86 a share.** Rule (CONVENTION of this run): the price at which the central case earns 15% pre-tax
  on the whole business, one and a half times the floor, so that owner cash could fall by a third and the purchase would
  still clear the floor; that is the margin at which no pencil is needed. In the shown-decline case the same rule gives
  $11.21. The cheap price is so far below the fair price because $2.1B of debt takes the first $2.1B of any value: a
  margin of a third on the business is a margin of about two thirds on this equity.

## Q8: IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (closed OUT at Q7).

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED as a question (closed OUT at Q7). The debt facts are recorded because the balance-sheet reading needs them.
**COMPUTATION, NOT A CLEARANCE.** After the June and July 2026 borrowings: $600M 3.750% notes due April 2031; a $1,140M
term loan at Term SOFR plus 2.00% due June 2033, floating, secured by "substantially all" of the borrower's and guarantors'
assets, amortizing 0.25% a quarter, with an excess-cash-flow sweep from FY2028 if first-lien net leverage exceeds 2.75
times; $400M 6.250% notes due July 2034 (replacing the 5.125% notes due January 2028); a $225M asset-based revolver to
June 2031, undrawn, $193.5M available at June 30 (8-Ks `0001104659-26-074259`, `0001295947-26-000029`,
`0001104659-26-083872`; 10-Q Note 8). Net debt $2,126.5M is 4.8 times the pro forma pre-tax unlevered owner cash of
$438.8M; the company's own figure is "~4" times bank-defined EBITDA. No maturity of size before 2031, so "no significant
near-term cash requirements" **[L2014-023]** is met for five years; the 2031 to 2034 maturities assume refinancing, and
"maturities must actually be met by payment" **[L2010-020]** in a bad market. As a whole business offered for purchase it
would fail the "little or no debt" criterion **[R1997-001]**; that STOP is stated for whole businesses and is not applied
to a market purchase here. The debt is what turns a narrow-moat business into a thin equity: risk "from the capital
structure when somebody sticks a ton of debt into some business" **[M1997-009]**.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED (closed OUT at Q7).

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (closed OUT at Q7). For the record only: remedies for minor ailments sold under their own names; none of the
named businesses of Q12.

---
## THE BOX
**OUT, at Q7.** The castle stands, narrowly (Q2 IN), the accounts are plain (Q4 IN) and no integrity tell was found (Q5
IN); the capital record, the pay design and the uses of cash all weigh against (Q3, Q6). Valued on an all-equity basis
the business is expected to earn about 10% pre-tax at the price in the central case and 9% if its five-year decline
continues: a pencil case on the floor, not a screamer. **Value range $69.32 to $85.48 a share (whole-cycle variant to
$99.65), fair price $47.74, cheap price $16.86, against a price of $45.61.** Not TOO HARD: no research pass is opened.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the copy and the research folder were made before `tools/run.py` ran).
      **Not met in full:** the file was written in three stages (Step 0 to Q2, Q3 to Q6, Q7 to the end) rather than
      question by question, and nothing was committed, because this session's instruction forbids commits.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, below); every filing fact carries its
      accession or names the filing; numbers not from a row or a filing are labelled CONVENTION (the framework's or this
      run's) or flagged as aggregator data (the price, the March closes used in the retention test).
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; Q8, Q10 and Q12 are NOT REACHED and the
      Q9 facts are headed as computation; the fair and cheap prices are headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (OCF less stock pay less capital spending, as filed), never a net-income proxy
      (operator rule 5); the sovereign from the US Treasury; aggregator quotes flagged. Net income is used once, as the
      measure of earnings retained in the retention test, which is what that test retains.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (the nine items under the foundations).
- [x] No row dated after the anchor is cited in a point-in-time run: not a point-in-time run (today's run).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its owner-earnings mean (3-year) was not used; the
      five-year table here is recomputed from the filed figures.
- [x] `python tools/check_framework.py` PASS before finishing (result recorded in the reply; no commit made).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q4 and EBITDA talk.** Q4's "What it rules OUT" lists "EBITDA as earnings and managements that talk it" and the text
under "Why confusion is a STOP" says "On EBITDA talk the stop is stated as a count" (**[M2002-026]**), yet Q4's heading
confines the STOP to confusion or suspicion and the two-tell convention makes suspicion need two tells. PBH talks EBITDA
when it buys, borrows and pays itself, but its accounts are not confusing; I treated the EBITDA talk as a heavy weighing,
not a STOP. Had it been read as a STOP the file would have closed OUT at Q4 instead of Q7. (2) **Q7 and a capital
structure that changed after the window.** The range convention averages five years of owner cash, which is after
interest; PBH doubled its debt for a $1,045M purchase ten weeks after the window closed. The convention says nothing on
this; I put every year on an all-equity basis, added the purchased businesses at their stated EBITDA and subtracted the
net debt, and showed two stress variants. Two analysts could easily do it differently. (3) **The floor's basis.** The
floor is "about ten percent pre-tax on the price paid", but the framework does not say whether the price paid is the
equity's or the enterprise's. On the equity at $45.61 the expected return is well above 10% because of the leverage; on
the enterprise it is about 10%. I used the enterprise, following **[L2017-004]** and Q9's test 2, and the verdict depends
on that choice. (4) **The range and the floor can disagree.** The template says Q7 closes IN "only if the price is so far
below [the range] that no pencil is needed", and a price 34% below the bottom of a range discounted at 5.66% sounds like
that; yet the same price meets the 10% pre-tax floor only to a tenth of a point. The range at the long rate and the floor
are two different hurdles; the framework should say which governs when they conflict (here I let the floor govern,
because the framework's own convention says a candidate at or below the floor is quit on). The same conflict reaches Q6:
the buyback convention reads repurchases against the bottom of the Q7 range, which here sits above the floor's fair
price, so PBH's FY2026 buybacks pass one test and fail the other. (5) **Q2's brand tests with no data.** Share against
the store brand and price against volume are the deciding brand tests, and the filer stopped disclosing shares after
FY2016 and never splits price from volume. The framework sends an unknowable castle to TOO HARD and an unresearched one
to the research pass, but gives no rule for a castle answered only indirectly (here, by fifteen years of gross margins
against the store-brand maker's). I closed Q2 IN on the indirect evidence and said so; another analyst could reasonably
have closed it TOO HARD (WORK). (6) **The roll-up.** Q1's "understood by its parts" is written for holding companies; a
brand roll-up's future depends on purchases not yet made, which no question owns except Q6's weighing. The framework
could say whether expected future deals are part of what must be understood at Q1. (7) The contamination note: the
blind list does not cover commit subjects of other companies' runs visible in the session context, one of which concerned
a branded-consumer name closed at Q2 on retailer power, the very test this run turned on.
