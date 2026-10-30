
## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT). Facts found are under AFTER THE STOP.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT**, decided at **Q7** on the floor: value range **-$18.22 to $15.91 a share** (all-equity, central; equity-only $5.26 to
$37.87 beside) against **$52.19**; the best defensible case yields 3.20% on the enterprise value, below the 10% floor and below the
5.43% long bond. Q1 IN, Q2 IN (regulator-set ordinary return carried; political threat recorded; TOO HARD (NATURE) named as the
other reading), Q3 against, Q4 against (not a STOP), Q5 integrity IN and ability for, narrowly, Q6 against in both parts.
Reporting figures (Part VII, not verdicts): fair price **-$20.77 all-equity, not positive**; **$8.03 equity-only**.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.
- **Bears on Q8 (the bond).** The 30-year Treasury yields 5.43% (2026-10-16, US Treasury par yield curve); the business's best case
  at the price yields 3.20% on enterprise value and 3.94% on the equity alone (Q7).
- **Bears on Q9 (debt and exposures).** Debt $3,703.0M at 2026-06-30 (long-term $3,200.1M, current maturities $282.9M,
  short-term $220.0M; 10-Q `0000356309-26-000037`), 58% of debt plus equity; $150M more NJNG notes placed 2026-08-20 to 2026-10-22
  (8-K `0001140361-26-033890`). FY2025 pre-tax earnings before interest against interest, excluding the $58.2M sale gain:
  ($368.3M + $128.6M) / $128.6M = 3.9 times (10-K FY2025). Cash at year end under $5M in eight of the last ten years; the company
  relies on "short-term bank borrowings or commercial paper supported by our revolving credit facilities" ($575M NJR and $250M
  NJNG facilities expiring August 2029, 10-K glossary) and says so in Item 1A. Solar asset financing obligations $471.5M inside
  long-term debt (2025-09-30). Energy Services "could possibly be required to comply with various margin or other credit
  enhancement obligations" on a downgrade (Item 1A). NJNG is one utility in one state; MGP remediation estimated at $144.3M to
  $200.2M, recovered through a BPU rider (Item 3). Operating leases $177.0M outside the debt figure. Debt covenants on
  debt-to-capital ratios (Item 1A).
- **Bears on Q10.** Nothing beyond Q7.
- **Bears on Q12.** No business named in the rows (casinos, tobacco, loading schemes, gambling) is among NJR's; nothing found.
- **Integrity facts:** the make-the-numbers habit (initial NFEPS guidance outperformed five years running, by the company's own
  statement) was reached and judged at Q5, so the box carries no "recorded, not judged" flag.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `1ae70f37`); written question by question; committed after each
      (Q1 `9637fe47`, Q2 `394d403c`, Q3 `dbb96372`, Q4 `072b9caf`, Q5 `ecf8ac1d`, Q6 `0641515e`, Q7 with the Q6 write-back
      `cc4dbc50`, this close in the next commit).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock in `Screens/_daily/` was present at dispatch
      (held by the dispatching session, not touched by me); the fold into the register is the dispatcher's (operator rule ten). A
      run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched, except the one listing of `Test Runs/`
      file names declared under CONTAMINATION at the top, with the commit subjects and memory line seen at dispatch; none used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check script
      `Test Runs/_research 2026-10-18 NJR/scripts/check_run_ids.py`, output `check_run_ids_output.txt`); no E-id; every filing
      fact carries its accession; numbers not from a filing are labelled CONVENTION or are arithmetic on filed figures.
- [x] The order was kept; Q7, the first STOP that failed, closed the run; Q8 to Q12 are NOT REACHED and nothing after Q7 is a
      clearance.
- [x] Owner cash from the filed cash-flow statements after stock pay and all spending, maintenance by the depreciation proxy
      beside, never a net-income proxy (operator rule 5); the sovereign from the US Treasury; aggregator quotes (prices) flagged.
- [x] Contrary evidence written down as found (foundations; Q2's political threat and the closest-call note; Q5's PennEast
      entry); facts for later questions under AFTER THE STOP.
- [x] Not a point-in-time run; no row was rejected for date.
- [x] Only the arithmetic lines of `tools/run.py` were used, and two of those (the owner-earnings window and the "d3" debt
      column) were found wrong for this filer and replaced by the filed statements (Step 0).
- [x] `python tools/check_framework.py` PASS before the closing commit (output in the reply and in
      `Test Runs/_research 2026-10-18 NJR/check_framework_output.txt`).
- Honest gaps: (1) the statutory-tax schedule with the credit shelter's present value was not built (Q7 shows the direction and
  that the box does not move); (2) NJNG's maintenance and growth spending were not split from the filing (the capital table in
  Item 7 is an image), so maintenance is the depreciation proxy; (3) NJNG's own equity is an estimate (54% of net utility plant);
  (4) ONE Gas depreciation was not read; (5) the FY2021 repurchase prices were not read from Item 5 of that year, only bounded by
  the year's closes; (6) the stock-pay add-back could not be seen in the cash-flow statement, so it may be deducted twice
  (at most $17.8M a year); (7) the outcome of New Jersey's proceeding on the future of gas utilities is not in the filings read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Specific (f), the cap, on a pass-through utility.** The cap cuts growth to "the business's own sales growth", but NJR's
revenue is dominated by gas costs passed through without markup, so "sales" fell 1.4% a year over FY2021 to FY2025 because the
gas price fell from its 2022 peak, not because the business shrank (customers and rate base rose). Applied as written, the cap
turns a 2.60% shown growth into -1.42%. The box does not depend on it (every case is below the floor), but for a utility or any
pass-through business the text should say whether "sales" means revenue as filed or a margin the filer reports (here, utility
gross margin), and I applied revenue as filed. (2) **Specific (e) where growth spending is compulsory and regulated.** The
central case values maintenance-only cash at no growth, and the growth case charges the growth spending for ten years; for a
utility whose growth spending earns a regulated return a little above the long bond, the result swings on the discount rate (at
5.43% the halves-rate growth case is above the top; at 10% every growth case is below it), and the text does not say which
growth rate to carry when end-years and halves both are meaningful but differ (2.60% against 7.28%). I took end-years as "the
growth the business has actually shown" and showed halves beside. (3) **Q2's regulated-return exception and a political threat.**
The exception carries a regulator-set ordinary return to Q3, but the text does not say how to judge a castle whose threat is the
regulator's own State (an executive order opening a proceeding on the future of gas utilities). Whether that is "a castle whose
future cannot be judged" (TOO HARD (NATURE)) or a narrowing to be weighed is left to the analyst; I judged IN with the other
reading written down. A sentence on regulatory or legislative threats to a regulated castle would make two analysts agree.
(4) **Q4 and EBITDA.** The STOP paragraph quotes **[M2002-026]** on EBITDA talk ("about zero") inside "Why confusion is a STOP",
while the make-the-numbers paragraph sends an adjusted figure featured to Q5 as a weighing; a segment EBITDA used for 6% of
earnings fell between the two, and I weighed it. (5) **Whose tax, in a deferred-tax utility.** The statutory-rate rule was written
for carryforwards and credits that run out; a regulated utility's deferred taxes on accelerated depreciation do not run out while
it grows, and the text does not say whether they are a shelter to be priced separately or ordinary cash. I used cash taxes and
showed the book-tax direction. (6) **The template's "Shares by class" check against "issued shares less treasury shares"** could
not be done exactly: the balance sheet states outstanding shares directly and the par-value dollar total divided by $2.50 gives a
number (101.2M) below the outstanding count, a presentation I could not reconcile from the face of the statement; the cover count
was checked against the stated outstanding count instead.
