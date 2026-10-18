
---
## COMPUTATION, NOT A CLEARANCE: Q7's range and the fair price, for the owner's two reporting figures
*(The file closed OUT at Q2. Nothing below is a clearance, a verdict or entry language (operator rule 3). Arithmetic in
`valuation.py`, output in `valuation_out.txt`, in the working folder.)*

**The cash input.** Owner cash after every real cost, from the filed cash-flow statements (XBRL first-filed, checked
against the FY2021 to FY2025 10-Ks): operating cash flow, less stock pay, less all capital spending, less finance-lease
principal (FY2022 to FY2025, 0.7, 1.0, 2.1, 1.1), less cash paid for acquisitions (Carly Railcar Components, $6.3M net of
cash, December 2025). This is the equity-only series (after interest). The all-equity series adds back the cash interest
paid (FY2021 to FY2025: 6.5, 8.8, 4.9, 4.6, 13.8) at its cost after the 21% statutory rate. USD millions:

| fiscal year | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| owner cash, equity-only | 38.1 | -37.0 | -25.8 | -69.7 | -60.7 | 0.9 | -10.1 | 34.7 | 20.4 |
| owner cash, all-equity | 38.2 | -36.9 | -25.6 | -69.4 | -55.6 | 7.8 | -6.2 | 38.3 | 31.3 |

**The specifics, in Q7's order.**
- *The window and the cycle, specific (a).* The literal five-year window is FY2021 to FY2025. Its first year is aberrational
  on the filer's own description: the year after "the cyclical industry downturn", with the Shoals plant closed in February
  2021, production moved to Castaños by March 2021, $6.5M of restructuring, and a $24.7M rise in VAT receivable "due to
  production increases and delays in receiving VAT refunds" (FY2021 10-K, `0000950170-22-004254`, Item 7). The base is
  therefore the average over the last full cycle of owner cash, whose peaks are FY2017 (38.1) and FY2024 (34.7): FY2018 to
  FY2024, all-equity **-21.09** a year (equity-only -23.97). FY2017 to FY2023, beside: -21.11. The literal window, beside:
  all-equity **3.12** (equity-only -2.98). A cyclical base is the speakers' own way of reading a lumpy business, "what
  difference does it make to us if the earnings average, say, 300 million a year, if it comes in in a very lumpy fashion?"
  **[M2011-102]**, and the window's ends are the years a growth rate must not be built on **[L2005-003]**.
- *Decline and sign changes, specific (b).* Inside the window the series changes sign (first two years averaging -29.9
  equity-only, last two +27.6); the growth between the halves is meaningless, and between cycles both averages are negative
  (FY2013 to FY2017 -13.7, FY2018 to FY2024 -24.0). **The range is therefore the no-growth case alone, said so**; it has one
  point, not two ends.
- *Acquisitions, specific (c).* The one deal in the window (CRC, $6.3M) is deducted as capital spending; no growth is credited
  in any case, so the organic pair is the same figure. A second aftermarket acquisition closed after 2026-06-30 (earnings
  release of 2026-08-03, exhibit 99.1 to `0001193125-26-330605`); its price was not found in the documents read; credited at
  nothing. Not a serial acquirer (one deal of $6.3M in the window; the half test cannot be read because owner cash before
  purchases is negative over the window, stated).
- *Working capital, specific (d).* Counted, inside operating cash flow. The FY2021 VAT draw is tied by the filer to one event;
  the literal window with it removed is shown beside: all-equity **8.06**.
- *Maintenance, specific (e).* The filing describes the capital spending as "enhancement of machinery and equipment on current
  production lines" (FY2025 10-K, Capital Expenditures) and guides $7.0M to $10.0M for 2026; over the window it ran at 6.2 a year
  against depreciation of 5.0. No growth spending can be separated, so all spending is the maintenance case; the
  depreciation variant (run.py: window mean 0.5 against -0.7 on the capex basis) moves nothing material.
- *The cap, specific (f).* No growth is carried, so no cap applies.
- *Tax* (Q7, Whose tax). The window's owner cash is after the company's own cash tax (mostly Mexican; paid FY2023 to FY2025:
  2.1, 5.9, 7.6). Restated at the 21% statutory rate on each year's pre-tax income before the warrant marks, only FY2024 changes,
  by about $0.3M; the mean moves by less than $0.1M. The shelter (federal loss carryforwards, recorded as a net deferred tax
  asset of $52.1M at 2026-06-30, 10-Q) is valued per case as the present value at 5.43% of 21% of the case's owner cash a year
  until the asset is used: central case nil (no taxable income in it), literal window $11.9M, VAT-adjusted window $25.0M.
- *Net debt* at the latest filed date: debt $100.725M (current 2.875, long-term 97.850) less cash $62.978M = **$37.75M**
  (10-Q 2026-06-30). Operating leases ($44.2M of lease liability, chiefly the Castaños plant) are left out, as Q7 says. No
  floor-plan finance. Shares 32.804M (cover count plus the three penny warrants; the $3.57 warrant left out, about 0.65M shares
  on the treasury method at $5.92, stated). Market value $194.2M; with net debt $231.9M.
- *The floor tested first* (2026-10-10). At the price, all-equity owner cash of about $22M to $23M a year would be needed to
  earn ten percent on the market value plus net debt less the shelter. The central case is -21.1, the literal window 3.1, the
  VAT-adjusted window 8.1. **No case earns the floor at the price** **[M2003-149]** ("there’s just a point at which we drop out
  of the game"), so Q7, had it been reached, would close OUT whatever the width.

**The results** (no-growth case, zero nominal growth for ever, discounted at the 5.43% long Treasury rate; fair price with the
same cash discounted at ten percent; per share):

| case | value a share, all-equity | fair price, all-equity | value a share, equity-only | fair price, equity-only | expected return at $5.92, all-equity |
|---|---|---|---|---|---|
| **CENTRAL: cycle base FY2018 to FY2024** | **-$12.99** | **-$7.58** | -$13.46 | -$7.31 | -9.1% |
| beside: cycle FY2017 to FY2023 | -$13.00 | -$7.59 | -$13.18 | -$7.16 | -9.1% |
| beside: literal window FY2021 to FY2025 | $0.96 | $0.16 | -$1.67 | -$0.91 | 1.4% |
| beside: literal window, FY2021 VAT draw removed | $4.14 | $2.07 | $1.33 | $0.83 | 3.9% |

Two checks that are not cases, flagged as chosen start years ("growth-rate presentations can be significantly distorted by a
calculated selection of either initial or terminal dates" **[L2003-004]**): the years after the move only, FY2022 to FY2025,
all-equity owner cash 17.8 a year, an expected return of 9.1% at the price and a no-growth value of $9.93 a share; the two best
years only, FY2024 and FY2025, 34.8 a year and 18.3%. The second is the whole case for the business: it holds if, and only if,
2024 and 2025 are the normal year of the new business, which the first half of 2026 (operating loss of $4.9M, 10-Q) and the
field's record do not show.

**The two reporting figures** (a reporting convention, not a rule; neither is a verdict):
- **(a) VALUE RANGE:** a single no-growth point, **-$12.99 a share** (all-equity, cycle base FY2018 to FY2024, after the company's
  own tax), against **$5.92**; the literal window beside at $0.96 (equity-only -$1.67). The range has no width because the shown
  growth is meaningless (specific (b)).
- **(b) FAIR PRICE:** **-$7.58 a share** on the all-equity basis (the central figure), **-$7.31** equity-only beside; on the literal
  window, $0.16 all-equity and -$0.91 equity-only. No price earns the floor on the central case.

---
## THE BOX
**OUT at Q2 (Q1 IN): a standing castle that protects only ordinary returns** (Trinity about 5% and Greenbrier about 9% pre-tax on
operating assets over FY2016 to FY2025; this filer a loss on average and at best at cost parity with Greenbrier's manufacturing
margins in its two best years); **integrity facts recorded, not judged**. COMPUTATION, NOT A CLEARANCE: value -$12.99 a share
(no-growth single point, all-equity, cycle base) against $5.92, literal window $0.96 beside; no case earns the floor; fair price
-$7.58 all-equity (-$7.31 equity-only). No research pass (the box is OUT, not TOO HARD).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down as found **[M1997-127]**; no verdict on any of them; the box is unchanged.)*
- **Q3 (capital).** Property, plant and equipment $28.4M at 2026-06-30; the plant is leased (the lease reclassified from finance to
  operating in 2025: right-of-use finance asset $45.1M at the end of 2024, operating $40.3M at the end of 2025; FY2025 10-K).
  Capital spending ran near depreciation over the window; inventory swings with deliveries ($125.0M at the end of 2023, $57.8M at
  2026-06-30); a VAT receivable of $6.7M (10-Q) that drew $24.7M of cash in 2021.
- **Q4 (the accounts).** Warrant fair-value losses of $99.5M (2024) and $32.2M (2025), non-cash and non-operating, from warrants
  issued in financings; FY2025 net income of $38.1M includes a $49.0M tax benefit from the release of a valuation allowance;
  FY2025 other income includes a $3.3M Employee Retention Credit and a $2.1M bargain-purchase gain; FY2023 a $14.9M loss on
  extinguishment of debt. The earnings release of 2026-08-03 features Adjusted EBITDA ($1.2M for the quarter) and gives
  full-year guidance (deliveries 3,500 to 3,900, revenue $410M to $460M, Adjusted EBITDA $36M to $44M), and states "our share of
  industry new-railcar orders reaching approximately 45%" for the quarter. To be weighed at Q4 and carried to Q5 if a later run
  reaches them.
- **Q5 (integrity, recorded and not judged).** (1) Related-party payments: the company paid $24,543,000 in 2025 to the family of
  director Jesús Gil (Fasemex, the plant's lessors, a supplier, a trucker, a warehouse) "related to steel fabrication services,
  rent and security deposit payments for the Manufacturing Facility, material and safety supplies, trucking services, royalty
  payments, and rent of an external warehouse" (proxy, `0001213900-26-031465`, Certain Relationships). (2) On 2026-08-05, after
  the lender's affiliate exercised its warrants, the board adopted a rights agreement; on 2026-10-14 it terminated it under a
  Stockholder Agreement with the OC III holders (about 48.8%), agreeing to adopt no future rights plan with a threshold below 20%,
  with board review of transfers to a would-be holder of more than 20% (8-Ks `0001213900-26-085699`, `0001213900-26-109859`).
  (3) Guidance and a featured Adjusted EBITDA (Q4 above); Adjusted EBITDA also weighs 31.67% of the CEO's and CFO's annual bonus
  (proxy). (4) Corporate professional services expenses rose $5.5M in 2025 (FY2025 10-K MD&A); the cause is not stated in what I
  read. CEO total pay $2.03M (2025) and $2.30M (2024) (proxy, Summary Compensation Table). Any later run that reaches Q5 must
  answer these first (Part VII).
- **Q6 (the money and the owners).** Warrants issued in 2020, 2021 and 2022 to the lender's affiliate for 23%, 5% and 5% of the
  fully diluted common at $0.01, and in 2023 for 1,636,313 shares at $3.57 (10-Q, Warrants); the June 2026 net exercise issued
  13,619,377 shares for no cash, about 41.5% of the shares now outstanding. Series C preferred of $85.4M issued in 2023 in exchange
  for a term loan and redeemed in 2024 from a $115.0M term loan, with $27.9M of dividends paid that year (FY2025 10-K). No dividend
  on the common, no buyback. Q6's buyback test is moot (no buyback).
- **Q9 (debt and exposures).** Term loan $100.7M at 9.7% (2026-06-30), maturing 2028-12-31, with liquidity and quarterly leverage
  covenants; a $35M asset-based revolver with a springing maturity of 2028-10-02 (10-Q); the top five customers about 75% of 2025
  revenue; a sole supplier of roll-formed center sills (66% of new cars in 2025); one plant in Mexico; tariffs named by the filer.
- **Q12.** Nothing found that bears on it.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early): template
      copy `a4c7ee23`; Step 0 to Q1 `c8498e80`; Q2 `57f5f099`; the close in the commit after this one.
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session (the brief says so; I did not touch it); the fold into the register is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule); what was seen by
      accident is declared at the top under Contamination and was not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in its row (`check_ids.py` in the
      working folder, PASS); every filing fact carries its accession; numbers of mine are arithmetic on filed figures, in the
      working scripts.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; everything after it is headed COMPUTATION, NOT A
      CLEARANCE or AFTER THE STOP.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing authority (US
      Treasury par curve); the price an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (the foundations line, and the contrary evidence for the
      business weighed at Q2); facts for later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor is cited in a point-in-time run: not a point-in-time run (anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS before the closing commit.
- One slip to declare: the first write of the run file replaced the template whole with the sections then closed, so the
  template's later headings (Q2 onward, the box, the audit) were re-added by hand as each part closed; nothing in them was
  changed from the template's wording except to fill them.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Section C carries two exits for one fact pattern.** A filer that has improved, on a change not yet tested by a full cycle,
inside a field whose durable players earn ordinary returns, can be sent to TOO HARD (NATURE) by the change-for-the-better
sentence or to OUT by the ordinary-returns item; the text does not say which governs. I read the ordinary-returns item as
deciding where the improvement, credited in full, reaches only parity with the field (the improvement then cannot make a
castle), and said why in Q2; a case may want to write that down. (2) **Specific (a) has no rule for a business that changed its
form inside the cycle.** RAIL's last full cycle of owner cash (FY2018 to FY2024) is mostly the US-plant business it closed in
2020 and 2021; the convention values that business, and the change-for-the-better rule that might speak to it sits at Q2, not Q7.
I kept the convention's base central and showed the post-move years as a flagged check. (3) **The shelter convention says
carryforwards "that run out inside ten years".** Post-2017 federal losses never expire; "run out" can mean expire or be used up.
I valued the shelter by use (until the recorded asset is exhausted), stated. (4) **The all-equity basis names no tax rate for
the interest added back.** I used the 21% statutory rate, stated; a company that pays no US tax because of its losses gains no
cash from the deduction, so the choice slightly flatters the all-equity case. (5) **The brief's rival rule meets a 10-K with no
Item 1A and no named rivals.** A smaller reporting company may omit risk factors; I took the rivals the filer last named (FY2022
10-K) as a CONVENTION of the run before choosing my own, and said so.
