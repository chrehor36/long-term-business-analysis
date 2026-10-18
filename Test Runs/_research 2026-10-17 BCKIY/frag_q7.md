## Q7 — WHAT IS IT WORTH? STOP.
"how much do you get back, how sure are you of getting it, when do you get it?" **[M2009-004]**. Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**, at the long government rate, held as a range. The arithmetic is in `scripts/value.py` and its output in `cache/value_out.txt`. GBP m unless stated.

**The cash input** (Q4's recast, Step 0's definition). Owner cash after every real cost, equity-only: FY22 −205.3, FY23 65.9, FY24 148.0, FY25 139.1, FY26 244.6. On the **all-equity basis** (the central figure), net interest paid is added back after tax at the UK main rate of 25%. **CONVENTION of this run:** one rate is used for all years, although the rate was 19% before April 2023. Rationale: the difference is under £2m a year and the forward rate is 25%.

**The range convention, specific by specific.**
- **(a) Cycle base.** The window's first year, FY22, is aberrational on the filer's own description. Its operating cash flow of £6.8m reflects "the unwind of the past practice of period-end working capital management (principally creditor deferrals and debt factoring)", a £56m VAT deferral unwound, £40m less factoring and an accelerated pension payment (AR2022 pp.30 to 31): "a base year in which earnings were poor can produce a breathtaking, but meaningless, growth rate" **[L2005-003]**. There is no business cycle in the usual sense; the event is the end of a practice. So the base is the average of FY23 to FY26, and the literal five-year window is shown beside it.
- **(b) Decline.** None is shown in the base years. On the literal window the series changes sign, so growth is measured between the halves: FY22 to FY23 average −69.7, FY25 to FY26 average 191.9. That is meaningless, so the literal range is the no-growth case alone, as (b) says.
- **(c) Acquisitions.** Net business purchases over the window were negative (disposals of £405.2m in FY22 and £158.6m in FY23; small items after). Nothing is deducted, disposal proceeds are not counted as owner cash, and growth is measured from FY23, after the disposals. There is no merger, no all-stock deal and no signed unclosed deal in the documents read. The company is not a serial acquirer in the window.
- **(d) Working capital** is inside operating cash flow throughout. FY26 includes a £95.5m contract-liability increase from the Type 31 reversal, which flatters FY26 cash; it is left in, because the base averages four years and the reversal's cash cost falls in later years.
- **(e) The maintenance case is central.** The filing allows the guess (Q3): net capital spending above depreciation, £27.9m a year on average over FY23 to FY26, is growth spending and is added back for the central case. The all-spending case is shown beside it.
- **(f) The cap.** The shown growth of owner cash, FY23 to FY26, is 54.8% a year. Carried ten years, it would need owner cash far above 5.64% of sales, the highest share in the filings read (FY17, itself a dressed year). It is therefore cut to the business's own sales growth over the same years, 4,438.6 to 5,177.7, or **5.27% a year**. That is below the 5.86% discount rate, so no further cap applies. "if you trace out the mathematics of it, you bump into absurdities, then you better change expectations somewhat" **[M1999-067]**. Ten years at 5.27%, then zero nominal growth.
- **The four PG specifics.** Growth is measured on aggregate owner cash. All capital spending is deducted in the side case. Growth after year ten is zero nominal. A price above the top closes OUT.
- **Net debt for the per-share range** (the all-equity basis, **[L2017-004]**): £329.0m at 31 March 2026 (borrowings and leases less cash and the items the filer nets), plus two subsequent events the filing states. These are the remainder of the June 2025 buyback completed in April 2026 (about £47.4m: £200m less the £152.6m cost in FY26) and the FY26 final dividend of 5.0p (about £24.5m, paid September 2026). Total **£400.9m**. Operating leases are inside it, as IFRS 16 puts them. The £250m bond of 2026 does not change net debt. The second £200m buyback is left out because the treasury count shows no purchases by 30 September.

**The range** (per share, all-equity basis less net debt, 490.485m shares, sovereign 5.86%):

| Case | Base (all-equity) | No-growth end | Growth end | Expected return at 961.8p: no growth / growth |
|---|---|---|---|---|
| **Central: FY23–FY26 base, maintenance-only** | 205.0 | **632p** | **998p** | **4.0% / 6.1%** |
| FY23–FY26 base, all spending | 177.1 | 534p | 851p | 3.5% / 5.3% |
| Literal FY22–FY26, maintenance-only (no-growth only, by (b)) | 141.9 | 412p | – | 2.8% |
| Literal FY22–FY26, all spending | 107.4 | 292p | – | 2.1% |
| Side case, generous (**CONVENTION of this run**, below): pension catch-up replaced by £20m a year, the £100m technical-provisions deficit added to net debt | 275.8 | 858p | 1,351p | 5.3% / 7.8% |
| Side case: FY26 alone, maintenance-only | 286.6 | – | – | 5.6% / 8.2% |

The pension side case is a **CONVENTION of this run**. Rationale: the FY23 to FY25 base carries £340m of pension catch-up that the company says has ended ("c.£20 million per annum over the coming years", results statement p.17). Treating the remaining deficit as debt and the catch-up as its repayment is the most generous reading open, and it is shown so that the close does not rest on the pension years.

**The floor is tested first** **[M2003-149]**. At 961.8p, no case in the range, central or side, earns about ten percent: the best is 8.2%, on FY26 alone with 5.27% growth for ten years. For the central growth case to earn ten percent at this price, owner cash before interest would need to be about £356m a year (`value.py`), against £205m on the central base and £287m in the best single year. "there’s just a point at which we drop out of the game" **[M2003-149]**. The width, 998 over 632, is 1.58 to 1. It is not reached as a test. The price sits inside the central range near its top, so it would close OUT by the width rule too, the case being no screamer: "It should scream at you." **[M2009-005]**.

**Value range (central, all-equity): 632p to 998p a share against 961.8p** (ADR USD 13.04, one ADS to one share). Literal window beside it: 412p (no-growth only).

**Fair price (a reporting figure, never a verdict; Part VII):** **427p** a share, central, all-equity basis. Each end of the central range is valued at ten percent instead of 5.86% (no-growth end and growth end, the same cash streams), the two are averaged, and net debt of £400.9m is taken off, after the company's own tax. **The equity-only figure, 440p**, is beside it: owner cash after interest, with the same maintenance add-back, £177.3m, valued the same way, against the market value of the shares alone. The equity-only figure is higher than the all-equity one because the after-tax interest added back on the all-equity basis, about £28m a year, is worth about £0.28bn to £0.36bn at ten percent across the two ends, less than the £400.9m of net debt taken off. No cheap price is reported.

**VERDICT: OUT.** No case earns the floor at the price.

