## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts found are under AFTER THE STOP.

---
## THE BOX
**OUT, at Q7** (Q1 IN; Q2 IN narrowly; Q3 against; Q4 against, no STOP; Q5 integrity IN, ability against narrowly; Q6
against on both parts). Value range **$94.23 to $95.63 a share** (all-equity basis, organic pair with the maintenance
inversion, at the 5.56% Treasury) against **$35.18**; no case earns the floor of about ten percent at the price on the
all-equity basis (best 9.12%), because $4.6B of corporate debt sits ahead of an unlevered yield of about 8% to 9%. Fair
price $25.77 all-equity, $60.64 equity-only (reporting figures, not verdicts). Not a TOO HARD, so no research pass.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down **[M1997-127]**, not weighed; the box unchanged (operator rule 2).
- **Q8.** The 30-year Treasury yields 5.56% (2026-10-13). The expected return on the whole business at the price, by the
  Q7 cases, is 8.05% to 9.12%; the equity-only cases 15.0% to 17.9%.
- **Q9.** Corporate debt $4,876M at 2026-06-30 (10-Q), weighted rate 5.691% at 2025-12-31; maturities (Note 15, FY2025
  10-K): term loan A $400M (2028), term loan B $851M (2028; refinanced on 2026-07-17 by a new $850M term loan due
  2033, 8-K `0001140361-26-028827`), notes $850M (2029), revolver $130M drawn (2030; $809M undrawn), term loan B $887M
  (2031), notes $500M (2031), secured notes $900M (2032). Non-recourse debt $2,896M (10-Q): the Timeshare Facility due
  2027 ($615M drawn, $235M undrawn at 2025-12-31) and securitized notes due 2033 to 2044; the securitizations carry
  "portfolio performance requirements related to default, delinquency and recovery rates, which, if not met, would result
  in loss or disruption of cash flow" (Item 1A). Coverage on the speakers' definition, pre-tax earnings over interest
  **[L2012-002]**: ($175M + $311M) / $311M = 1.56 times for 2025; 2.5 times for 2023. Surety commitments $439M; contractual
  obligations $9.4B over 14 years, $1.0B in 2026 (Item 7). For a whole business offered, the "little or no debt"
  criterion **[R1997-001]** would not be met. The loan book defaults at about a tenth a year, and the warehouse must be
  renewed in 2027.
- **Q12.** Facts for the newspaper test **[M2008-011]**: the product is sold on a tour by a commissioned sales force, 67%
  of it financed at a weighted 14.7% under underwriting that does "not include certain traditional ability-to-pay
  factors, such as income verification"; about a tenth of the loan book defaults each year and the defaulting owner's
  interest returns to inventory for resale (Items 1, 1A, 7); exit companies target the acquired Diamond owners (Item 1A).
  None of the businesses Q12 names (casinos, tobacco, distributor-loading schemes, gambling, promotion on a borrowed
  reputation) is this business.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `9a53627a`); written question by question; committed after each
      (Q1 `b96fe649`, Q2 `7b315d7a`, Q3 `2c459b9e`, Q4 `5e831431`, Q5 `65a8418f`, Q6 `bd8cc1e9`, Q7 with the Q6 write-back
      `183f891d`, the close in the final commit).
- [x] Dispatched to an analyst: the brief allowed the per-question pathspec commits; the lock is the dispatching
      session's (a lock file was seen in `Screens/_daily/` and not opened). Folding into the register is the dispatcher's.
- [ ] The blind rule: **one breach, declared at the top**: a listing of `Test Runs/` filtered for the ticker and name,
      run before the first fetch to check the dated path; it returned nothing. Commit subjects of another company's run were
      seen in the session preface and not used. No run file, holding review, `PORTFOLIO.md`, register or reading list was
      opened.
- [x] Every v5 id resolves and every quoted fragment beside an id is in that row (`check.py` in the research folder: no
      E-ids, every M/L/R id in the CSV, every adjacent quotation inside its row); every filing fact carries its accession
      or names its document.
- [x] The order was kept; Q7 was the first STOP that failed; nothing after it is a clearance.
- [x] Owner cash after every real cost (stock pay, all capital spending, the loan losses, the integration costs), never a
      net-income proxy; the sovereign from the Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (the foundations, Q2, Q4); the facts for later questions are under AFTER
      THE STOP; no integrity flag is needed, since Q5 was answered.
- [x] Not a point-in-time run; no row dated after an anchor arises.
- [x] Only the arithmetic lines of `tools/run.py` were used; its owner-earnings and yield lines were set aside.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Receivable-secured non-recourse debt has no rule.** Q7's convention covers inventory-secured trade finance only. For
a seller that lends to its buyers and funds the book with non-recourse securitizations, the choice decides everything: as
the finance arm's working capital (this run's confessed CONVENTION, by extension) the fair price is $25.77; counted in
net debt while the loan growth is also charged in operating cash, it is negative, because that reading charges the
receivables' growth without counting the receivables. The run used the first and showed the second; a ruling is owed.
(2) **EBITDA talk sits in two places.** Q4's "Why confusion is a STOP" still carries the count, "about zero"
**[M2002-026]**, and Q4's rules-OUT list still names "managements that talk it", while the 2026-10-06 convention sends a
featured adjusted figure, guidance and the make-the-numbers habit to Q5 as a weighing. A management that guides and pays
on Adjusted EBITDA falls under both; this run followed the later, more specific convention and judged it at Q5. (3)
**Specific (a) and the serial acquirer.** A full cycle cannot be built across two purchases when the organic pair is
central; the run took the window less its aberrational first year and showed the literal window beside. (4) **"Ordinary
returns" names no capital base.** On tangible capital the field earns well; on what buyers paid, ordinarily or poorly. The
run judged the business on tangible capital (**[M2011-060]**) and sent the purchase prices to Q3 and Q6; another analyst
could close Q2 OUT on the other base. (5) **The parts convention says "operating profit"**; HGV reports only segment
Adjusted EBITDA, which was used for want of anything else. (6) **"Organic growth, as the filer reports it"**: HGV reports
pro forma revenue, not organic owner cash; the run chained the pro forma revenue. (7) **The value range at the government
rate misleads under leverage**: the range ($94 to $96) sits nearly three times the price while no case earns the floor;
for a levered business the floor test and the range point in opposite directions, and the reported range invites a
"cheap" reading that the floor refuses. (8) **The maintenance guess for a developer** rests on the cost of VOI sales under
the relative sales value method, which counts on future recoveries of defaulted inventory, so the guess likely overstates
growth spending and so flatters the maintenance-only case; it did not change the box.
