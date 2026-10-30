
## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED as a judgment; the facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (not asked by the operator for this run; no named business of Q12's list is involved).

---
## THE BOX
**OUT at Q7**: no case of the range earns the floor of about ten percent at the price; equity-only range (the regulated
utility's basis) **$45.62 to $82.70 a share against $92.69** (2026-10-26, aggregator close). Q1 IN, Q2 IN, Q3 UNDECIDED,
Q4 WEIGHS AGAINST, Q5 integrity IN with ability WEIGHS AGAINST, Q6 WEIGHS AGAINST. Reporting figures (not verdicts): fair
price **$26.47** equity-only (central); all-equity **-$22.61**, not positive. Not a TOO HARD, so no research pass.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; the box is unchanged; operator rule 2.)* **[M1997-127]**
- **Q8, the bond:** the 30-year Treasury yields 5.33% (2026-10-23); the stock's no-growth owner-cash yield at the price is
  2.62% and the growth case's implied return about 4.94% (Q7), both below the bond.
- **Q9, the debt and its cover:** long-term debt (with current maturities and finance leases) $71,869M at 2025-12-31; net
  debt $72,598M at 2026-06-30 (10-Q), with commercial paper and other notes payable of $2,132M and $4,694M of securities due
  within one year. Pre-tax income plus interest expense over interest expense: (4,999 + 3,238) / 3,238 = 2.5 times in 2025;
  (2,576 + 1,837) / 1,837 = 2.4 times in 2021 (Note 16, XBRL). The parent ("All Other") carried $1,416M of interest expense in
  2025 against no regulated asset of its own (Note 16). The test the rows give for a utility's debt is cover "even under very
  adverse business conditions" **[L2010-012]**; not judged here.
- **Q9, sudden demands for cash:** maximum potential collateral under contracts with credit-rating triggers, at 2025-12-31:
  $32M at BBB/Baa2, $445M at BBB-/Baa3, **$3,774M at BB+/Ba1 or below** (of which Georgia Power $2,503M, Southern Power
  $1,347M) (FY2025 10-K, MD&A, Financial Condition). Unused committed bank credit $8,909M across the system. New convertible
  notes of $833.75M due December 2027 and $1,897.5M due September 2029 (8-K `0000092122-26-000063`); equity units outstanding.
  Forward share sales settleable to June 2028.
- **Q9, one event:** three states and a gas business; hurricane exposure on the Gulf coast (storm damage recovery at Georgia
  Power, Note 2); nuclear plants (Farley, Hatch, Vogtle) and the risk factor that "Damages, decommissioning, or other costs
  could exceed the amount of decommissioning trusts or insurance coverage" (Item 1A); the regulatory climate (base rates in
  Georgia frozen through 2028 except storm costs; Nicor Gas disallowances), the speakers' own utility error **[L2023-011]**.
- **Q9, Southern Power:** 97% of its investment under contract through 2030 and 89% through 2035, average remaining contract
  about 12 years; 63% of contracted MW with AAA to A- counterparties (Item 1).
- **Q10:** nothing beyond the box.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (by the first session, 11:31); written question by question. **Departure:** the
      resumed session's first commit carried Step 0 through Q2 together, and Q3 with Q4 and Q5 with Q6 were committed in pairs;
      Q7 (with the Q6 line written back) and the close were committed on their own. Five commits in all, each with a pathspec of
      the two paths only.
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's (operator rule ten). The
      run binds nothing until folded into the register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under contamination at the top and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (the check
      script `Test Runs/_research 2026-10-26 SO/check.py`: 0 problems); no E-ids; every filing fact carries its document and
      accession (the competitors' figures carry theirs; aggregator prices flagged).
- [x] The order was kept; Q7 closed the file; nothing after it is a clearance. The figures after the stop are facts only.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; stock pay from the
      filed statement (the tool's tag understated it); the sovereign from the US Treasury; the price flagged as an aggregator
      quote.
- [x] Contrary evidence written down as found (THE FOUNDATIONS, and at Q5 the reading against my own integrity verdict);
      AFTER THE STOP filled. Integrity was judged at Q5 (IN), so the box carries no "integrity facts recorded, not judged" flag.
- [x] No point-in-time anchor: today's run; no row dated after an anchor arises.
- [x] Only the arithmetic lines of `tools/run.py` were used; its stock-pay column was replaced by the filed figure.
- [x] `python tools/check_framework.py` PASS before each commit.
- Honest limits: rate base is not stated by company, so net plant weighted the debt-credit cap (CONVENTION of this run);
  the rivals' 2025 returns (and Dominion's 2021 and 2022) are not framed in their XBRL facts and are shown NA rather than
  computed by hand; the proxy was read by search for pay, guidance and governance, not page by page; Southern Power was not
  valued separately (CONVENTION of this run, Q7).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The debt-credit cap for a deciding part of several regulated companies when only one states an allowed equity ratio.**
The text weights the allowed share "by rate base where that part is several regulated companies" and falls back to the
business's own share where an allowed share is stated "for less than half of the deciding part's rate base". Here the filing
states one allowed share (Georgia Power, 56% equity), covers more than half of the part, and states no rate base by company;
the text does not say whether the stated share is applied to the whole part or weighted with nothing for the rest. I applied
44% to the whole part, weighted by net plant as a confessed stand-in for rate base, and showed the own-share case beside
(top $96.44 instead of $82.70; the box does not change). (2) **A consolidated utility holding company with a merchant part.**
The regulated-utility paragraph puts merchant generation on the all-equity basis, but the filer reports operating cash and
capital spending only consolidated; the text does not say whether to split them by segment shares. I valued the whole on the
equity-only basis and confessed it. (3) **The maintenance guess for a utility.** The rows say depreciation can understate a
utility's real need ("your depreciation charges are inadequate" **[M2015-049]**) and Q7 asks for the filing's best guess; the
filing's own capital programme categories gave a cross-check ($5.7B of maintaining categories against $6.0B of D&A), but the
text does not say which categories count as maintaining. (4) **Q2's regulated-return exception** carries the field's ordinary
returns to Q3 "as a second best", while the template's Q2 line says "a durable castle that protects only ordinary returns closes
OUT"; the template omits the exception, and a reader of the template alone would close a utility at Q2. I followed the framework
text. (5) `Screens/cover_shares.py` labels the subsidiary registrants' common shares with the names of debt series from the cover
page; read from the cover itself they are the subsidiaries' shares. (6) `tools/run.py`'s stock-pay column used an APIC tag that
gave about half the filed expense.
