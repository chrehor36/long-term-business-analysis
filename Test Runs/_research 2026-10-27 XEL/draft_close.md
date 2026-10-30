
## Q8: IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9: COULD IT RUIN US? NOT REACHED. Facts are under AFTER THE STOP.
## Q10: IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## THE BOX
**OUT at Q5 (integrity, on doubt), integrity facts recorded, judged at Q5.** Q1 IN, Q2 IN, Q3 weighs against, Q4 IN on
the accounts and weighs against. The COMPUTATION beneath the stop: equity-only value range $20.13 to $40.29 a share
against $77.86 (2026-10-26); fair price $11.91 equity-only, all-equity not positive; no case of the range earns the floor
at the price, so Q7 would also have closed OUT. Q11 belongs to a holding review.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.
- **Q6, Part A (the money).** Common stock issued: proceeds $3,349M in 2025, $1,117M in 2024, $270M in 2023 (filed cash
  flows, `0000072903-26-000009`); shares outstanding 507.2M (2016) to 623.6M (end-2025), 49.2M in 2025; ATM programs of
  $4.0B (August 2025) and $4.3B (May 2026); forward sale agreements for 69.8M more shares outstanding at 2026-06-30
  (minimum proceeds $5,177M); the 2026-2030 plan calls for $7.0B of equity (10-K Item 7; 10-Q `0000072903-26-000154`). The
  serial-issuance row stands in the text as a candidate second STOP, unresolved **[L2014-015]**; the issue prices (about
  $74 a share on the forwards) sit above the computed range. Dividends: $1,282M paid in 2025; target payout 45% to 55%;
  annual increases of 4% to 6% are an objective (10-K Item 7). No repurchases of common stock. Deals: none. The parent
  bought $953M face of its own subsidiary's bonds for $712M in 2024 and 2025 (10-K note 5).
- **Q6, Part B (pay, board, owners).** CEO total compensation 2025 $15,998,859; CEO pay ratio 108 to 1; annual incentive
  2025 paid at 143.76% of target, funded only if ongoing EPS reaches guidance; long-term units 70% performance (ongoing EPS
  growth 30%, emissions 30%, nuclear ratings and wildfire mitigation 20% each, a relative TSR modifier of up to 30%) and
  30% time-based; combined chairman and CEO with a lead independent director; directors' holdings are mostly granted
  stock-equivalent units, with bought shares from none to 14,481 each (proxy, `0000072903-26-000063`).
- **Q8 (the bond).** The 30-year Treasury yields 5.31%; the no-growth case yields 2.75% on the price.
- **Q9 (the target's debt and exposures).** Debt $40.8B at 2026-06-30, 1.70 times equity; interest coverage by pre-tax
  earnings over interest charges **[L2012-002]** fell from about 3.6x (2016) to 2.75x (2020) and 2.2x (2025; about 2.1x
  without AFUDC-equity and the bond-repurchase gain and with the Marshall charge added back); short-term debt $2.51B plus a
  364-day term loan of $1.5B (drawn $750M) maturing January 2027; utilities may have to post collateral if rated below
  investment grade (10-K Item 1A); Xcel Energy Inc. depends on its subsidiaries' dividends, which commissions can limit;
  wildfire exposure in Colorado and Texas with excess liability cover of $450M and the Smokehouse Creek policy period
  nearly spent; the Texas Attorney General's suit over Smokehouse Creek seeks damages and civil penalties (10-K note 12).
  One utility's catastrophe is the rows' named case **[L2005-019]**; here there are four utilities in eight states.
- **Q12.** No business of the named kinds.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `f20df1e1`, before the first EDGAR call); written question by
      question; committed after each (Q1 `7a099560`, Q2 `1c677643`, Q3 `6ccc5fa7`, Q4 `93f1cc8f`, Q5 `ed35b4e0`, Q7
      computation `9bed0171`). **Declared:** the Q7 arithmetic script was written and run during the research, before Q2
      to Q5 were written (it was committed with Q1); its output file is headed COMPUTATION, NOT A CLEARANCE. I saw its
      result (the price far above every case) before judging Q5. The Q5 verdict rests on the integrity facts listed there
      and not on the price; the reader should know the order all the same.
- [x] Dispatched: the brief allowed per-question pathspec commits of my two paths; the lock and the fold are the
      dispatcher's (operator rule 10). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under contamination at the top and not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `Test Runs/_research 2026-10-27 XEL/check_ids.py`; every
      filing fact carries its accession; numbers without a row or a filing are labelled CONVENTION.
- [x] The order was kept; Q5 closed the file; nothing after it is a clearance, and the Q7 figures are headed so.
- [x] Owner cash after every real cost (stock pay, depreciation and nuclear fuel, wildfire payments inside operating cash),
      never a net-income proxy; the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (the foundations, Q2's narrowing, Q5's facts for the other side); facts for
      the later questions under AFTER THE STOP.
- [x] Not a point-in-time run; no row dated after an anchor is at issue.
- [x] Only the arithmetic lines of `tools/run.py` were used; a defect in its debt-table sum is recorded at Step 0.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the final commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The utility debt credit counts finance leases but not the leased asset.** The 2026-10-23 text puts finance leases
in the long-term debt whose increase is credited, but a finance lease added without cash ($1,239M in 2025 here) buys a
plant that never passes through capital spending, so the credit can offset spending the lease did not fund; it did not
matter here only because the cap bound. (2) **The cap's weighting needs a rate base the filings do not tabulate.**
Allowed equity ratios are stated case by case, and electric rate base by state is not one table; I weighted by the rate
bases each case states, and the text does not say whether a verbal decision or a pending settlement counts as "stated".
The cap also takes the operating companies' allowed share while the holding company borrows on top of it (here about two
points of ROE), which the text does not address. (3) **Specific (a) has no reading for a non-cyclical business with an
aberrational year whose reversal sits inside the window** (Winter Storm Uri's deferral in 2021, recovered 2022-2023); I
used the window average and confessed it. (4) **Specific (f)'s fallback to sales growth is a poor measure for a utility,**
whose revenue is dominated by fuel costs passed through at cost (revenue fell from 2022 to 2025 while rate base grew);
kWh sales or rate base growth would measure the business, but the text names sales. (5) **Whose tax** assumes a credit the
owner keeps; production tax credits that a regulator passes to customers through rates need their own sentence. (6)
**Forward equity sales** (69.8M committed, unissued shares here) are not addressed by the share-count instructions. (7)
**The make-the-numbers rows speak of costs waved away and targets reached; the text has no sentence on a non-operating
gain kept inside the featured figure.** I judged it under the rows on hitting the number **[L2002-041]**, **[M2010-001]**,
and the operator may want the line drawn in the text, since it decided this file. (8) **The template's Q7 heading** asks
for growth spending "in year one" and "in year ten"; with the utility credit capped, the credit's year-one and year-ten
figures are as needed and the template has no line for them.
