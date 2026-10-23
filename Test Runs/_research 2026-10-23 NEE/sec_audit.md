## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 7904fae8); written question by question; committed after each
      (Q1 8b9ed537, Q2 1055802a, Q3 c61d4036, Q4 02a0a6ff, Q5 d69c8c28, after the stop a38053ad, then the close).
- [x] Dispatched: the brief allowed per-question pathspec commits of this file and the research folder only; the lock in
      `Screens/_daily/` is the dispatching session's and was not touched. The fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched, except the one filtered
      listing of `Test Runs/` declared at the top (three other companies' file names seen, none opened). Contamination
      declared there.
- [x] Every v5 id resolves and every fragment quoted beside an id is in that row (`check_ids.py` in the research
      folder, output in `check_ids_out.txt`); every filing fact carries its accession or names its filing; no number
      without a filing or a CONVENTION.
- [x] The order was kept; Q5 closed the run; nothing after it is a clearance, and the Q7 figures are headed
      COMPUTATION, NOT A CLEARANCE. **Declared:** the owner-cash arithmetic in `worksheet.py` (needed for Q3 and Q4) was
      run, and its rough Q7 lines were printed, before Q5 was written. When I judged integrity I already knew the price
      stood far above every case I could build. The Q5 verdict rests on the litigation and the filings named there, but
      a reader should know the order in which I saw things: a run that already "knows" the answer is OUT on price has
      an incentive to close early on a softer ground, and the reverse.
- [x] Owner cash after every real cost (stock pay, interest, tax-equity distributions and a maintenance guess
      deducted), never a net-income proxy (operator rule 5); the sovereign from the US Treasury; the price from an
      aggregator, flagged.
- [x] Contrary evidence written down as it was found (foundations); the facts for later questions are under AFTER THE
      STOP. The Q5 facts were judged at Q5, so the box line carries no "recorded, not judged" flag.
- [x] Not a point-in-time run; no row was barred by an anchor.
- [x] `tools/run.py` printed no arithmetic for NEE ("UNRESEARCHED"); nothing of it was used. All sums are in
      `worksheet.py` from the filed statements.
- [x] `python tools/check_framework.py` PASS before the closing commit (see the close).
- Gaps, honestly: the maintenance guess is depreciation-based and may be low for a utility **[M2015-049]**; the "Whose
  tax" convention was not applied (figures high on that point); 2021's distributions to tax-equity partners are not
  stated separately and were taken as nil; Dominion's growth leg was not computed; the comparators' returns are from
  XBRL tags (equity may include preferred) and were not cross-checked against their filed statements except Dominion's
  2025 operating cash; the FEC complaint's outcome, the 11th Circuit's opinion and the content of the media articles were
  not read (they are not SEC filings).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **The regulated-utility paragraph does not say how to read a company of two parts.** It keys the equity-only basis
   on "the deciding part" but then says "Merchant generation and unregulated renewables ... stay on the all-equity
   basis". For NEE (FPL deciding, NEER a large unregulated part) three readings give very different figures: the whole
   company equity-only with the regulator's debt credit for FPL only (central here, fair $11.53), a sum of parts with
   NEER on the all-equity basis (fair −$6.13), and the whole company all-equity (fair −$33.00). I took the literal
   reading as central and showed the others beside; the operator should say which governs.
2. **The debt credit has no rule for the no-growth case.** A utility that only maintains its rate base raises no net
   new debt, so I credited FPL's net long-term debt raised only against growth spending, capped at 40.4% of FPL's
   spending; the paragraph's words could also be read to credit the window's debt in every case.
3. **Tax-equity money is not addressed.** NEER's projects are part-funded by "differential membership" investors who
   take the tax credits; their cash goes in as financing and their returns largely never pass through NEE's operating
   cash. I credited their proceeds against NEER's spending and deducted their distributions (a CONVENTION of this run,
   rationale: charging the whole project cost while its tax credits stay outside owner cash would charge the same asset
   twice). A rule is needed; the effect on this run is large on the all-spending series.
4. **"Whose tax" does not fit a fleet whose credits are renewed by building.** Each project's credits run ten years,
   but the fleet's are renewed until the phase-out; the convention's "run out inside ten years" test cannot be applied
   cleanly. Not applied; the direction of the error is stated.
5. **Q2's business-of-parts threshold says "operating profit".** NEE reports no operating profit by segment, only net
   income attributable (the CODM's measure), which includes the HLBV allocation that is 56% of NEER's five-year figure.
   I used the reported measure; on any measure FPL decides, but a closer case would turn on the choice.
6. **Q5's doubt rule meets unresolved litigation without guidance.** The rows close on doubt, and the framework says how
   habits carried from Q4 are read, but not whether allegations that survive a motion to dismiss and are settled
   without admission, with reforms aimed at the conduct alleged, are doubt. I judged them doubt and said why; another
   analyst could weigh them instead and reach Q7, where the computation closes the file anyway.
7. **Q7 (e) gives no method for "the growth spending charged against the growth it buys".** I held the window's average
   growth spending for the ten years of growth and stopped it at year ten; holding it at the last year's level (about
   double) would lower the growth case further.
8. **The maintenance guess for a utility whose D&A includes a regulatory reserve.** FPL's reported D&A is net of a
   reserve amortization used to hit a target ROE; I added it back. The framework's maintenance guess **[M2000-144]** says
   nothing of regulatory amortizations inside D&A.
