
## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT**, decided at **Q7** (the floor): the no-growth value is **$26.02 a share** on the central case (all-equity; literal window
beside $17.95 maintenance only, -$5.82 all spending) against a price of **$141.73**; no case earns about ten percent at the price.
Fair price (reporting figure): not positive on the all-equity basis (-$15.65); $37.80 equity-only. Re-look under an alert at the
top of the computed range, like any OUT (Part VII).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.)*
- **Q8, the bond.** The 30-year Treasury at 5.31% (2026-10-26) against an owner cash yield of 2.23% on the central case and 3.59% on
  the best three years (Q7 table).
- **Q9, the debt and the sudden demands.** Total indebtedness about $20.7 billion and about $19.9 billion net of cash at 2025-12-31
  (10-K FY2025, Item 1A); on the face at 2026-06-30, $19,595M of debt plus $300M of receivables financing and $613M of forward
  repurchase obligation, against $435M of cash (10-Q); $1.5 billion of junior subordinated notes added 2026-09-24 (8-K). Collateral:
  margin deposits drained $1,000M (2021) and $1,874M (2022) and returned $1,899M (2023) (cash-flow statements); the 10-K's own words,
  "increased collateral posting requirements" in Uri (10-K FY2023, Item 1A), and a downgrade "could trigger liquidity demands
  pursuant to contractual arrangements" (10-K FY2025, Item 1A). A commodity-linked revolving facility whose borrowing base moves with
  prices ($1.75 billion limit; amended 2026-09-30, 8-K 2026-10-05). Liquidity $6,295M at 2026-06-30 (release). S&P BBB- since
  December 2025. Asset retirement obligations $4.2 billion. Nuclear operations (six units) and their accident risk (Item 1A). The
  "little or no debt" criterion, stated for a whole business, is not met on these facts.
- **Q9, aggregation.** One weather event (Uri) produced the 2021 loss across Texas generation; ERCOT relies on "energy-market price
  signals" without a capacity market (Item 1).
- **Q12.** Coal 20% of capacity, with retirements and gas repowering announced (Item 1); no business named in Q12's list.
- No integrity facts beyond those judged at Q5.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit eda4478c); committed after each question (Q1 9e160df8, Q2 d423c561, Q3
      8cabb8db, Q4 ae17ea71, Q5 39c3a9ff, Q6 and Q7 together f6f0ff37, as the brief asks for Q6's buyback line). **Departure from
      write-early, confessed:** most of the filing research for Q1 to Q7 (cash flows, segments, rivals, proxy) was done before the
      Q1 section was written, and each section was then written and committed in order; the sections were not each written as
      their own research closed. The judgments were made in question order, but the evidence for later questions was in view
      when earlier ones were written.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's. The run binds nothing
      until it is folded into the register (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; the commit subjects seen in the session
      context are declared under Contamination and not used.
- [x] Every v5 id resolves (`Test Runs/_research 2026-10-27 VST/scripts/check_ids.py`: every id in `principle_ledger_v5.csv`,
      every quoted fragment beside an id found in that row, no E-ids); every filing fact carries its document and accession (Step 0
      lists them; the text names the document).
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); sovereign from the Treasury; the price is an
      aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations; Q2's customer counts; Q4's prepaid line); facts for later questions
      under AFTER THE STOP.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; its three-year means were not used and the reason is given in Step 0.
- [x] `python tools/check_framework.py` PASS before the final commit (recorded below).
- Conventions of this run, confessed: the 23% tax (21% federal plus about 2% state) on owner cash; the 21% tax in the field table;
  preferred stock counted with net debt; the cycle base set peak to peak in owner cash, 2019-2023. Figures not obtained: Retail's
  own capital (not reported); retail prices against rivals; the rivals' figures beyond tagged XBRL (not checked line by line); the
  guidance record across years; income taxes paid for 2021 and 2022 (taken as nil; the effect is small against the totals).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The business of parts, applied to a vertically integrated company.** Q2's convention reads reported segments, but here the
Retail segment buys from the generation segments "at market prices" and the two carry opposite hedge marks on the same contracts,
so the split of profit between them is an internal transfer price, and the marks alone moved Retail's five-year share from 52% to
79%. Retail decided on both measures, but the three generation segments together out-earned it on the measure less marks; the text
does not say whether segments that share one fleet and one hedge book should be read as one part. The run applied it as written.
(2) **A range of one case.** Where growth is meaningless the range "is the no-growth case alone", but the fair price is defined as the
average of two end cases; the run valued the one case at ten percent, and reported the template's growth-spending line as $0. (3)
**Preferred stock** is not named in the net-debt definition (borrowings and finance leases); the run counted it with net debt and
confessed the convention. (4) **A credit taken as revenue.** "Whose tax" prices carryforwards and credits "that run out inside ten
years", which reads as income-tax credits; the 45U nuclear PTC is recognized as revenue and runs to 2032; the run took it out of the
base and priced it beside, and the text does not say whether that is required. (5) **A maintenance figure that moves between
filings.** The FY2024 10-K put 2024 growth spending at $800M and the FY2025 10-K implies $351M for the same year; specific (e) does
not say which filing governs; the run used the latest filing where it reaches and the older series before it. (6) **No rivals
named.** The brief asks for the rivals the 10-K names; this 10-K names only categories, so the run chose three and said so.
