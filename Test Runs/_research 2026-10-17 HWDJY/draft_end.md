
## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7** (the floor): no case of the value range earns about ten percent at 788p. Range 780p to 1,044p a share
(US$41.35 to US$55.33 an ADS) against 788p (US$40.02 an ADS); fair price 499p (US$26.43 an ADS), equity-only 503p
(US$26.66). Q1 IN, Q2 IN, Q3 UNDECIDED, Q4 WEIGHS FOR, Q5 integrity IN and ability FOR, Q6 Parts A and B WEIGH AGAINST.
Re-look is a price question, not a business one: the top of the range valued at ten percent is 567p.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down **[M1997-127]**, not weighed; the box is unchanged (operator rule 2).
- **Q8.** UK 20-year gilt 5.7225% (Bank of England, 14 Oct 2026); the fair price at ten percent is 499p.
- **Q9.** First borrowing in the eleven years read: a £240m term loan drawn 23 June 2026, maturing 31 August 2029,
  "restricted in use for the acquisition", covenants "in line with those within the RCF" (H1 2026); the RCF of £150m,
  undrawn, expiring September 2029, with covenants of net debt to EBITDA below 3:1 and EBITDA to net finance charges above
  4:1 (AR2025 note 19). The company "expects to remain in a net cash position" and states cash "greater than the amount of
  the loan" after the deal (H1 2026 going concern). Lease liabilities £712.9m at 13 June 2026, mostly depot leases. Pension
  deficit £16.9m, triennial valuation as at 31 March 2026 under way, funding arrangement to 31 May 2027. The company's own
  stress case is "the worst 12-month year-on-year fall that the Group has ever experienced". About £40m of cost headwinds
  in H2 2026 from "ongoing disruption in the Middle East" (H1 2026 technical guidance); supply from "+300 global suppliers".
- **Q10, Q12.** None found that bears; no named business of Q12's list.
- **No integrity facts are carried** (Q5 was answered IN).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 4353c815); written question by question; committed after each
      (Step 0 5f761db6; Q1 7eeb002b; Q2 0c8ab89c; Q3 225f8477; Q4 4ed1abc4; Q5 4426eae6; Q6 2f921e14; Q7 c1072a2e).
      The first Write of Step 0 replaced the template's later headings in the file; each section was then rewritten in the
      template's order and wording as it closed.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's (not checked by
      me); folding is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. One filtered listing of
      `Test Runs/` for "HWDJY" and "howden" returned nothing (declared at the top); the git log and memory lines seen are
      declared under contamination and were not used.
- [x] Every v5 id resolves (checked by `scripts/check_cites.py`); every filing fact names its document and date (no SEC
      accession exists; the ADS F-6EF accession is the brief's); every number has a filing or a CONVENTION.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy, for Howdens. **Exception, disclosed:** DIY Kitchens has
      no filed cash figure; its owner cash is a disclosed guess from its filed EBIT (Q7(c)), and the box does not turn on it
      (without DIY growth the top at ten percent is lower still). The sovereign is from the issuing authority (Bank of
      England), its series a CONVENTION of this run; aggregator quotes (price, ADS, the 2020 year-end close) are flagged.
- [x] Contrary evidence written down as found (foundations list; Q2 narrowing; Q3 increment; Q6 pay).
- [x] Not a point-in-time run; no anchor bar applies.
- [x] `tools/run.py` and `cover_shares.py` returned nothing for this name; no v4 material was used.
- [ ] `python tools/check_framework.py` PASS before the commit: see the result recorded at the foot of this file.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Sterling has no sovereign series in the protocol's table**, and the issuing authority's daily par yields stop at 20
years; I used the 20-year and called it a CONVENTION. A 30-year from the Bank's spot-curve archive would be a few basis
points different; the box does not turn on it. (2) **Q7(a) assumes two full cycles are visible.** With eleven years of
reports and an aberrational first window year, only one trough-to-trough cycle (FY2018 to FY2024) can be closed; the text
says growth is "measured between the averages of successive cycles" and gives no fallback when the earlier cycle is
incomplete. I borrowed (b)'s halves method and said so. A cycle-to-partial-cycle rate (FY2015 to FY2017 against FY2018 to
FY2022) would have given about 8.5% a year and a top case at ten percent of 734p, still below 788p, so the choice is
material to how the range is built though not to the box here. (3) **Cash tax
distorted by prior-year credits.** The template asks for owner cash "after the company's own tax" and does not say whether
cash tax or the charge governs when the filer says cash tax carries refunds of earlier years; I used the year's own charge
and showed the cash basis beside. (4) **A deal closed after the window "valued on its own filed record"** does not say what
to do when the record is a press-release EBIT with no cash flow; the protocol forbids a net-income proxy, so I labelled the
EBIT-after-tax figure a disclosed guess. A rule is needed. (5) **The maintenance case (e) can invert the range so that the
bottom rises** (here from 640p to 780p), which narrows the range and moves Q6's buyback test against fewer purchases; the
text treats the inversion as the finding, but the buyback test then reads against a higher bottom than the all-spending
pair would give. Both are shown. (6) **Pension deficit repair** is neither listed as a real cost nor as debt in Q7's net
debt definition; I treated it as debt-like and added the cash back, a CONVENTION of this run. (7) The template's v5 header
still points to `Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`, a test-record file; I did not open it.
