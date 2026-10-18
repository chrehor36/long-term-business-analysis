
## Q7: WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is the
risk-free interest rate" **[L2000-021]**, held as a range **[L2000-024]**, at the long government rate, 5.43% (Step 0).

**Owner cash, from the filed cash-flow statements** ($ millions; script `Test Runs/_research 2026-10-18 NJR/scripts/q7.py`,
output `q7_output.txt` and `q7b_output.txt`). All spending = utility plant + solar equipment + storage and transportation and
other + cost of removal, with equity-investee flows and business sales netted (specific (c): the FY2025 $137.2M proceeds from
the residential solar sale netted against spending; no business bought inside the window; the FY2020 Leaf River and Adelphia
purchase, $523.6M in cash, lies before it and its earnings are inside the window's statements). Maintenance = depreciation and
amortization + cost of removal (the depreciation proxy **[M1998-127]**; the filing does not split NJNG's spending into
maintenance and growth in a form I could read, so the guess **[M2000-144]** is the depreciation charge plus the removal cost NJR
pays in cash beside it). Stock pay deducted. All-equity basis adds back interest paid at (1 - 25%) (CONVENTION of this run: the
federal 21% plus the filer's "State income taxes, net of federal benefit" line, about four points a year over the window).

| FY | Operating cash | Stock pay | All spending (net) | Owner cash, all spending, after interest | same, all-equity | Owner cash, maintenance only, after interest | same, all-equity |
|---|---|---|---|---|---|---|---|
| 2021 | 391.0 | 7.1 | 622.1 | -238.3 | -179.3 | 222.1 | 281.1 |
| 2022 | 323.5 | 14.8 | 590.6 | -282.0 | -218.7 | 140.1 | 203.4 |
| 2023 | 479.0 | 14.7 | 538.6 | -74.3 | 6.8 | 270.8 | 351.9 |
| 2024 | 427.4 | 16.0 | 569.1 | -157.7 | -67.5 | 196.4 | 286.6 |
| 2025 | 466.3 | 17.8 | 568.3 | -119.7 | -22.0 | 213.8 | 311.5 |
| **Five-year average** | | | | **-174.4** | **-96.1** | **208.6** | **286.9** |
| Literal ten-year window FY2016-25, beside | | | | -217.2 | -160.2 | 157.5 | 214.4 |

**Whose tax.** Operating cash carries the cash taxes actually paid, which were small ($9.9M in FY2025 against a $97.0M provision;
FY2021 to FY2025 the provision exceeded cash paid by $58.9M a year on average), sheltered by deferred taxes on utility plant and
by solar credits that the OBBBA is ending for new projects (10-Q). The framework asks owner cash at the statutory rate with the
shelter's present value added back where credits run out inside ten years. I did not build that schedule; the direction is
known: at the book tax provision the maintenance-case owner cash falls from $286.9M to $228.0M and the top of the range from
$15.91 to $5.22 a share. Every figure below uses the cash-tax figure, the more generous one, and the box does not change on the
stricter one.

**The specifics, in order.** (a) *Cycles.* No end year of the window is a cyclical peak or trough on the filer's own
description. Two things flatter the window and are recorded, not removed: the AMA prepayments ("approximately $260M in cash
from fiscal 2022 through fiscal 2024", ahead of the revenue), and the FY2025 sale proceeds netted under (c). Removing either
would lower every case. (b) *Decline.* The all-spending series is negative in every year of the window, so its growth rate is
meaningless; the maintenance series is positive and grew 2.60% a year end to end (all-equity, FY2021 $281.1M to FY2025
$311.5M), 7.28% between the halves of the window (shown beside). (c) *Acquisitions:* above; not a serial acquirer. (d) *Working
capital* is inside operating cash and counted. (e) *Growth spending.* The filing allows the maintenance guess, so the central
case is owner cash after maintenance only, and the growth spending ($383.0M a year on the five-year average, the difference
between the two series) is charged against the growth it buys in the growth case, for ten years, stopping when growth stops.
(f) *The cap.* The shown 2.60%, carried ten years, would take maintenance owner cash to $371.0M, 18.2% of FY2025 revenue and 21.0%
of revenue carried at the company's own sales growth, above the highest share earned in the window (17.9%, FY2023). So the growth
carried is the business's own sales growth FY2021 to FY2025, **-1.42% a year** ($2,156.6M to $2,036.4M); the shown 2.60% and the
cut are both written down, and the uncapped case is shown beside. (Revenue here includes gas costs passed through to customers,
so it moves with the gas price; I record the oddity in the framework section and apply the text as written.)

**The range, all-equity basis (central)**, enterprise value less net debt of $3,669.0M, per share on 101.468M shares:

| Case | Per share, at 5.43% | Expected return at $52.19 |
|---|---|---|
| Top: maintenance only, no growth (central, (e)) | **$15.91** | 3.20% |
| Bottom: growth case, growth capped at sales growth (-1.42%), growth spending charged ten years | **-$18.22** | 2.03% |
| Beside: growth case at the shown 2.60%, uncapped | -$0.61 | 2.94% |
| Beside: growth case at the halves rate 7.28% | $28.38 | 4.36% |
| Beside: literal ten-year window, maintenance, no growth | $2.76 | |
| Beside: all spending, no growth, forever | -$53.61 | negative |

The inversion (growth case below the no-growth case) is the finding the framework names: "growth can destroy value if it requires
cash inputs in the early years of a project or enterprise that exceed the discounted value of the cash that those assets will
generate in later years" **[L2000-023]**. Here it means that at a 5.43% rate the regulated return of about 7% after tax barely pays
for the money it takes, and at the 10% floor it does not.

Equity-only basis (beside, never decides alone): top $37.87, bottom $5.26 (capped), expected return at the price 3.94% and
2.10%. The equity-only figures are higher because NJR's after-tax interest ($97.7M on $3,669M of net debt, about 2.7%) costs less
than the 5.43% discount rate; the lenders are taking a smaller return than the long bond, which flatters the per-share figure in
exactly the way **[L2017-004]** warns of.

**The floor first** *(the framework's order since 2026-10-10)*. "we don’t want to buy equities where our real expectancy is below
10 percent" **[M2003-149]**. At $52.19 no case of the range earns it: the best case I can defend, the maintenance case with no
growth, yields 3.20% on the enterprise value; even the halves-rate growth case, which I do not hold as central, returns 4.36%; and
a ceiling that is not a case at all (maintenance owner cash grown 7.28% for ten years with no growth spending charged, the double
count the framework forbids) returns 5.69% (q7_output.txt). Every one of them is below the floor, and every one is below the long
bond itself. The price is also above the top of the range, which closes OUT by the same floor. **"Well, if government bond rates
were 2 percent, we’re not going to buy a business to earn 3 or 3 1/2 percent expectancy over the years."** **[M2007-095]**: here
the bond pays 5.43% and the business offers about 3%.

**Value range: -$18.22 to $15.91 a share (all-equity, central) against $52.19.** Width not tested: the floor closes the file first.

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued with its own cash at 10% and the two
averaged, after the company's own (cash) tax: **all-equity -$20.77 a share, not positive** (top at 10%: -$7.88; growth case at
10%: -$33.66); **equity-only $8.03 beside it** (top $20.56; growth case -$4.51). At 10% even the maintenance case's whole
enterprise value ($2,869M) is below the net debt ($3,669M). No cheap price is reported.

**VERDICT: OUT** at Q7, on the floor: no case in the range earns about ten percent at the price, and the price sits above the top
of the range **[M2003-149]**, **[L2000-023]**, **[M2007-095]**.
