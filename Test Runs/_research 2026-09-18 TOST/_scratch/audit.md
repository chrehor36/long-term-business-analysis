---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN (first session, verified and corrected
  by dated note) → **Q2 OUT, the file closed**; Q3-Q6 recorded beneath explicit RECORDED, NOT
  GOVERNING banners, as at NVDA.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN was
  re-verified line by line. The two UNRESEARCHED cells in Q2 (Clover's numbers; churn, which no
  document publishes) are named and are not what closes the gate.
- [x] No UNRESEARCHED verdict was returned; the Clover cell names its artefact (Fiserv investor
  slides, company IR site rung).
- [x] No UNKNOWABLE verdict was returned.
- [x] Step 0: the filing was read with accession numbers; four figures cross-checked to
  companyfacts at Q4, and the Step 0 claim that they matched is now true rather than asserted.
- [x] Owner earnings on multi-year windows (five-year default, three-year, FY2025, TTM); (c)
  disclosed as a judgment and shown at both ends; capitalised SBC subtracted at the capex end.
- [x] Competitor row filled: nine examined, five numbered; Clover UNRESEARCHED; privates tested
  against a universal-filing route and recorded as not resolving.
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated 09/17/2026,
  re-fetched by this session.
- [x] Value stated as a round-number range under a COMPUTATION - NOT A CLEARANCE heading.
- [x] One bar (the screamer test); windage count one.
- [x] Price dated as a close, aggregator flagged, cross-checked against a Form 4.
- [x] Run committed to git after every question, with a pathspec.
- [x] Every ledger id cited was checked to exist in `principle_ledger.csv` (267 rows).
- [x] No em dashes in anything this session wrote (the template's own headings carry them).

### THINGS THE RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **Q1, the self-description** (first session): two rewrites in six months, not one in eighteen.
2. **Q1, the float** (first session): "cash held on behalf of customers" is payroll float;
   restricted cash is Toast's own collateral; neither is merchant float.
3. **Q1, Toast Capital** (first session): the credit risk is a capped first-loss guarantee, and
   H1 2026 added $46M of loans held on balance sheet.
4. **Q1, interest income** (first session): it is inside operating cash, not outside it. Q4 shows
   owner earnings both ways and Q5 removes it and carries the cash separately.
5. **This session**, before commit: Q3 first said $1.6bn of cash after the H1 2026 buyback; the
   balance sheet says $1,713M. Corrected in the draft.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **The warrant repurchase is dated to the wrong year.** The brief puts *"Warrant repurchase
   ( 61 )"* in **FY2025** financing. The cash-flow columns are 2025, 2024, 2023 and the line reads
   *"— ( 61 ) —"*: it is **FY2024** (the repurchase closed 2024-07-03), as is the $14M
   extinguishment gain.
2. **The quoted capex series mixes two definitions.** *"9, 28, 12, 16, 42, 54, 53"* is
   `annual(f, CAPX_TAGS)`, which returns the **software-excluded** figures for FY2019-22; FY2023-25
   include software. The two tags overlap in FY2021-22 with different values (12/16 against 19/33).
   `owner_earnings()` reads `capital_acquired()` and uses the fuller figures, which is why the
   screen's numbers reproduce while the brief's series does not reconcile for FY2019-22. The brief
   also said `PaymentsToAcquireProductiveAssets` carries FY2023-25; companyfacts carries FY2021-25.
3. **The capitalised-SBC inference was right in direction and wrong in size.** Additions of $54M
   exceed cash capex of $53M by $1M; the filed non-cash SBC in software is **$12M** (cash-flow
   supplemental), because cash capex also contains about $11M of equipment.
4. **The float was misnamed.** The brief called the customer cash merchant float; the notes say it
   is money held to remit customers' payroll taxes, and restricted cash is Toast's own collateral.
   The brief was right that interest may sit inside income; it missed that interest income on
   **all** of Toast's cash sits inside operating cash.
5. **The credit-loss figure was attributed wholly to Toast Capital.** Of the $91M FY2025
   *"Credit loss expense"*, **$62M** is the Toast Capital guarantee (Note 4); **$22M** is the
   receivables allowance (Note 7); the rest is other.
6. **The competitor list omitted the one pure restaurant filer and included a non-filer.** NCR
   Voyix (Aloha) reports a Restaurants segment and names Toast as a key competitor; it was not
   listed. Olo was listed as a filing rival; it filed a Form 15-12G on 2025-09-23 after its merger.
7. **The brief did not know the Toast Capital perimeter moved in 2026** ($46M of loans held for
   investment at 2026-06-30), because it read only the 10-K note.
8. **The brief's prior 2 (credit risk sits with the bank) was wrong, as the brief feared; prior 1
   (the capex label is a tooling artefact and the real (c) question is software) was right; prior
   3 (capitalised SBC) was right in direction.** Prior 4 was honoured: the brief named no gate, and
   the gate that closed (Q2) was not one the brief pointed at.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- `tools/sources.price()` returns an intraday `regularMarketPrice` stamped with today's date while
  its docstring says *"Latest close"* (found by the first session, reproduced by this one at 13:09
  EDT). Every run striking a price during market hours must use the chart's last completed close.
- `floor_screen.annual(f, CAPX_TAGS)` and `capital_acquired()` disagree where two capex tags
  overlap with different scopes (TOST FY2021-22). The priced path is the right one; a brief or run
  that quotes `annual()` gets a mixed-definition series.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**The 8-K Item 7.01 customer letter is the [E4-37] document.** The agony metric had been argued
from pricing language in 10-Ks; here a company filed its own prayer session, with a date, a price
(99 cents) and an apology. For any business that sells to small merchants, search the 8-K
exhibits for letters to customers before scoring [E2-44](1).

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** TOST FAILS AT Q2 (OUT, on [E3-03] criterion 2 as Toast's own filings test it and on
  [E4-04] in its own words; a surfing run, not a franchise). Q1 IN; Q3 IN on the binary (recorded,
  gate case on daily execution, [E4-29] fires in the bonus yardstick); Q4 IN on survival (recorded;
  owner earnings -$76M five-year to +$355M FY2025, SBC 168% of all operating cash ever filed);
  price $30.65 x 578M = $17.7bn, headed COMPUTATION - NOT A CLEARANCE: 1.89% business yield
  against a 5.29% sovereign; Q6 arms nothing.
- Work order: none. UNKNOWABLE: none.
