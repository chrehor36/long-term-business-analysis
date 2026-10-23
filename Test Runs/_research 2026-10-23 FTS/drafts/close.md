## Q8: IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
Not answered: the file closed OUT at Q7 (operator rule 2). Facts found are under AFTER THE STOP.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
Not answered: the file closed OUT at Q7. Facts found are under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
Not answered: the file closed OUT at Q7.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
Not asked: the file closed at Q7, and the operator has not chosen it for this run.

---
## THE BOX
**OUT at Q7**: no case earns the floor of about ten percent at C$80.99. Value range C$72.41 to C$97.93 a share
(equity-only, central, at the 4.19% Government of Canada long rate) against C$80.99; fair price C$28.96 (equity-only,
central), all-equity beside C$-27.12. Q1 IN, Q2 IN, Q3 weighs undecided, Q4 weighs against lightly, Q5 integrity IN and
ability weighs for lightly, Q6 weighs against lightly.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down under the question each bears on, each with its source **[M1997-127]**; no verdict; the box unchanged.

**Q8, the alternatives.**
- The maintenance-case owner cash yields 3.75% at the price, below the 4.19% Government of Canada long benchmark bond
  (Bank of Canada, 2026-10-21); the all-spending owner cash after the debt credit yields 1.50% (Q7).

**Q9, the target's debt and exposures.**
- Total debt C$34.6B at 2025-12-31 (C$22.2B in 2016); consolidated capital structure 57.0% debt, 2.7% preference shares,
  40.3% common equity and minority interests (MD&A 2025 p.17). Net debt C$35,610M pro forma 2026-06-30 (prospectus
  supplement `0001104659-26-106675`).
- Earnings before interest and tax covered interest and preference dividend requirements 1.89 times (twelve months to
  2025-12-31) and 1.97 times (twelve months to 2026-06-30) (the same supplement, Earnings Coverage Ratios).
- Holding-company debt (Corporate and Other, Note 14 of the 2025 statements): U.S. senior notes C$2,073M, debentures C$200M,
  senior notes C$2,600M, subordinated notes C$750M (2055); then US$1.0B of junior subordinated notes due 2057 issued in
  September 2026 (supplement). The holding company has no revenue of its own; its debt is served from subsidiary dividends.
- Long-term debt principal due: C$3,146M (2026), C$2,389M, C$1,880M, C$943M, C$1,714M (2030), C$23,985M thereafter
  (MD&A 2025, Contractual Obligations). Credit facilities C$5,773M, C$3,741M unused at 2025-12-31, C$5.4B committed with
  maturities 2027 to 2030 (MD&A 2025).
- Ratings at 2025-12-31: S&P A- issuer, BBB+ unsecured, outlook moved from negative to stable in November 2025; Fitch
  BBB+ (first assigned May 2025); Morningstar DBRS A (low). "In January 2026, Moody’s Investor Services, Inc. withdrew its
  ratings for Fortis at the Corporation's request" (MD&A 2025, Capital Structure and Credit Ratings). The PSUs can be
  cancelled if the S&P rating is below BBB (circular).
- Physical risk: the MD&A names wildfire among "its most significant climate hazards"; S&P's outlook change cited
  "developments at the subsidiaries to mitigate physical risks, namely wildfires" (MD&A 2025).
- Central Hudson explosion (November 2023): civil actions pending; contingent liability US$105M at 2026-06-30 with an equal
  insurance receivable (Q2 2026 statements, `0001666175-26-000031`).
- Unrecorded purchase commitments C$13,287M, of which gas and fuel C$6,592M and the Waneta Expansion capacity agreement
  C$2,307M (2025 statements, Commitments and Contingencies).
- Diversity of the earning sources: ten utilities in five provinces, ten states and Grand Cayman, the largest (ITC) about
  30% of five-year segment earnings (Q2).

**Q10, the pitch.** Nothing beyond Q7: the price is about 2.8 times the fair price.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 06504e86); written question by question; committed after each
      (Step 0 to Q1 42aa5212, Q2 674b7cc0, Q3 86ef8b7a, Q4 107617f9 and 49175fd9, then on resume Q5 c807b43b, Q6 064e6624,
      Q7 with the Q6 write-backs 0be83d5c, the close in the last commit). One slip: the Q6 commit 064e6624 went in before
      five corrections to it had been applied (my fix script stopped on an assertion and the commit command ran after it);
      it carried the words "hell-bent on issuing shares" beside **[L2009-019]** instead of their own row, three page
      references I could not confirm and a director-holdings range that was wrong at its low end. All five were corrected in
      0be83d5c; the citation check would have failed on the first.
- [ ] If dispatched: the brief allowed the per-question commits; the lock and the fold are the dispatching session's and
      were not checked by me. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. The contamination declared at the
      head of the file stands; the resumed session saw the same session context (the memory index, a git status naming
      the ARCB and AYI research folders) and nothing about Fortis; not used.
- [x] Every v5 id resolves (`Test Runs/_research 2026-10-23 FTS/scripts/check_ids.py`: no E-ids, every M/L/R id in the
      CSV, every quoted fragment standing before an id found in that row); every filing fact has its accession or names its
      document; numbers without a filing are labelled CONVENTION.
- [x] The order was kept; Q7 closed the run; nothing after it is a clearance; Q8 to Q10 not answered.
- [x] Owner cash from operating cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from
      the issuing authority (Bank of Canada, a CAD series the protocol's table does not list, named and dated); the
      aggregator prices flagged (Yahoo through `tools/sources.py`: the price of 2026-10-22 and the 2020 and 2025 year-end
      closes used in Q6's retention test).
- [x] Contrary evidence written down as found **[M1997-127]** (Step 0 list; Q5 and Q6 facts against); facts for later
      questions under AFTER THE STOP. No integrity facts are open, since Q5 was answered (IN).
- [x] No point-in-time anchor; not applicable.
- [x] Only the arithmetic lines of `tools/run.py` were used; it printed UNRESEARCHED and no figure of it was used.
- [x] `python tools/check_framework.py` PASS before each commit of this session.
- Honest limits: the maintenance figure is a guess at depreciation; the result does not turn on it (the bound with no
  spending at all is still below the price). The allowed debt share for Other Electric is a CONVENTION. The minority's
  claim on ITC is charged by its dividends, not its share of ITC's cash. Segment earnings for Q2 come from the MD&As, not
  the audited segment note. The DRIP issue prices are averages (amount over shares), not per-issue prices.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **The regulated utility's debt credit against the maintenance case.** The paragraph credits "the long-term debt raised
   over the window" against "the capital spending it funded", and specific (e) puts the maintenance case central. Neither
   says how the two meet: whether the credit is set against all spending (then the all-spending case) or only against the
   growth spending (spending above maintenance) that the central case charges. I credited it against growth spending
   only, capped at the allowed share of that, on the reading that depreciation is recovered in rates and the debt funds the
   additions to rate base; the literal all-spending case is beside. The paragraph should say which.
2. **"Long-term debt raised".** Not defined: whether committed credit-facility borrowings that the filer classes as
   long-term count, and whether the short borrowings do. I counted the first and not the second; the difference here was
   C$328M and moved nothing.
3. **The allowed debt share of a holding company of many utilities.** "the debt share of the capital structure the
   regulator allows as the filing states it" assumes one regulator. Fortis has eleven allowed equity ratios; I weighted
   them by midyear rate base and confessed a figure for the segment the filer reports as one. The text should name the
   weighting.
4. **The sovereign for a Canadian-dollar business.** The protocol's table lists USD, JPY and EUR only; the rows name "long-term
   U.S. bonds". I used the Bank of Canada's long benchmark under operator rule 5's earnings-currency clause. A CAD row
   (series `BD.CDN.LONG.DQ.YLD`) would settle it.
5. **A consolidated subsidiary with a minority.** Owner cash from consolidated operating cash includes all of ITC's cash;
   the framework does not say whether to deduct the minority's dividends or its share of earnings. I deducted dividends,
   which overstates owner cash by the minority's retained share (C$61M a year on average, earnings over dividends); the
   verdict does not turn on it.
6. **Specific (c) for a seller.** Netting "businesses sold" against spending raises owner cash in the window while the sold
   businesses' cash leaves the future; for a business that sells and does not buy, the text gives no correction. I netted
   as written and showed the figure without netting beside.
7. **The retention test's intrinsic leg has no rate.** Q6 asks whether retention added intrinsic value, and the answer here
   is yes at the government rate and no at the ten percent floor; the text does not say which governs. I wrote both.
8. **Serial issuance through a dividend reinvestment plan.** The candidate second STOP **[L2014-015]** is unresolved in
   section VI, and the text does not separate shares sold by the company from dividends reinvested at the holders'
   election. I weighed it and said why.
9. **The template's Q5 heading** reads "able, honest, in love with the business, the same after being paid", while the
   framework's Q5 test of the after-the-sale question applies to whole businesses only; for a part-interest the heading
   asks a question the section says is not asked. Kept as the template has it.
