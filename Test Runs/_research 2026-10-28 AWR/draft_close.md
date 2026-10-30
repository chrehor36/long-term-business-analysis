
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
**OUT at Q7**: no case of the range earns the floor at the price; VALUE RANGE $49.86 to $54.71 a share (equity-only,
regulated-utility basis) against $85.48 (close 2026-10-27, aggregator); FAIR PRICE $23.67 (equity-only), $3.52 all-equity
beside. Q1 IN, Q2 IN (return set by a regulator, carried to Q3 as a second best), Q3 weighs for weakly, Q4 IN (weighs slightly
against), Q5 IN, Q6 weighs against mildly. No integrity facts outside Q5's answer.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.
- **Q8 (the bond).** The 30-year Treasury par yield was 5.30% on 2026-10-27 (Treasury); the central maintenance owner cash
  was 3.09% of the market value at $85.48 (Q7). (Source: `tools/sources.py`; Q7 arithmetic.)
- **Q9 (debt and exposures).**
  - Debt at 2026-06-30: long-term debt $717.7M, current maturities $73.2M (including the 5.50% notes of $65M due 2027),
    bank notes $119.0M, cash $21.7M (10-Q 0001628280-26-053401). The revolvers mature in 2029 (AWR, GSWC) and 2028 (BVES);
    the CPUC requires GSWC and BVES to pay their revolvers to zero within each 24-month period (10-K FY2025, Item 7).
  - Cover: pre-tax income plus interest expense over interest expense, 4.0 times in 2024 ($149.4M + $50.4M over $50.4M), 4.9
    in 2023, 4.6 in 2025 (10-K FY2025 income statement). Covenants: GSWC indebtedness to capitalization 0.4352 against a
    limit of 0.6667, indebtedness to EBITDA 3.4 against 8 (10-K FY2025, Note on debt).
  - Strict liability without negligence: "Water utilities may be held strictly liable under inverse condemnation claims for
    fire damage in the event the water system did not operate as designed, including being damaged by the fire itself, even
    if the fire is no fault of the water utility" (10-K FY2025, Item 1A); BVES distributes electricity in a high wildfire
    risk area; wildfire insurance "could become unavailable on reasonable terms or without exclusions for losses due to
    wildfires" (Item 1A). The single-utility concentration the rows warn of, "A catastrophic event can render a single utility
    insolvent" **[L2005-019]**, applies: all regulated operations are in southern California, with earthquake exposure (Item
    1A, natural disasters).
  - The holding company depends on subsidiary dividends; California law limited GSWC's distributable amount to $933.7M and
    BVES's to $117.7M at 2025-12-31 (Item 7). AWR "generally guarantees performance of all of the contracts of ASUS’s
    subsidiaries" (Item 1).
  - ASUS receivables and contract assets due from the U.S. government were about $106M at 2025-12-31 (Q4), exposed to
    appropriations delays and shutdowns (Item 1A).
- **Q10.** Nothing found beyond Q7.
- **Q12.** Nothing found bearing on how the money is made: a regulated water and power distributor and a contractor to the
  U.S. military bases' water systems.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit d67b6f39, before the first EDGAR request); written question by
      question; committed after each (Q1 39c69d6c, Q2-Q3 8783c559, Q4 5d960bee, Q5-Q6 bfa34136, Q7 with the Q6 line 9f483e30).
- [x] Dispatched run: the brief allowed per-question pathspec commits of my two paths; the lock is the dispatching session's
      and I did not touch it. The fold is the dispatching session's (operator rule ten); a run not in the register binds
      nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen by accident and declared at
      the top under contamination, not used: commit subjects of another water utility's run dated today; the memory index.
      My `git log --oneline -1` calls after each commit printed only my own commits.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in that row, by the check
      script `Test Runs/_research 2026-10-28 AWR/check_ids.py` (output beside it); every filing fact has its accession or the
      named 10-K; no number without a filing or a row, the conventions labelled.
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; Q8 to Q12 are NOT REACHED; the facts after the
      stop are not weighed.
- [x] Owner cash after every real cost from the filed cash-flow statements (operating cash less stock pay less capital
      spending, with the maintenance variant), never a net-income proxy (operator rule 5); the sovereign from the US Treasury
      (issuing authority), dated; the price and the 2020 year-end price are aggregator quotes, flagged.
- [x] Contrary evidence written down as found (foundations; Q2; Q3; Q4; after the stop).
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; its debt column d2 (debt plus equity) was found wrong as debt and
      not used.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the final commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Specific (a) does not fit a rate-case cycle.** The swings in a utility's owner cash are regulatory lag (a late decision
builds regulatory assets, surcharges later release them), not a business cycle with peaks and troughs; (a) speaks of
"cyclical peak or trough" and "a year aberrational on the filer's own description", and here the filer describes both the
delay year (2023) and the recovery year (2025) as unusual. I kept the five-year window central because it holds
a whole rate cycle and its first recovery year, and showed the cycle-only, seven-year and normalized bases beside; all close
OUT, so the choice did not decide, but on a closer price it would. A sentence saying that for a regulated utility the cycle is
the rate-case cycle, and whether the regulatory asset and liability line is working capital under (d) or a timing item to be
averaged out, would remove the choice. (2) **The maintenance guess for a utility.** Q7 asks for the maintenance case central
"where the filing allows the guess"; a utility's renewal spending is economically maintenance but earns a return in rate base
like growth spending, and the filing gives no split. Depreciation as the guess (**[M1998-127]**) probably flatters, since
historical-cost depreciation on fifty-year assets understates replacement (**[L2015-004]**). The utility paragraph credits
debt against "growth spending" without saying how renewal spending is classed. (3) **The cap in (f) at the discount rate
makes the growth case nearly equal to the no-growth case** whenever g is cut to the discount rate: with g equal to r the
growth case adds only ten years of net cash. That is arithmetic, not an error, but it means the sales-growth cut, not the
business, sets the top of the range. (4) **"Capped at the allowed debt share"** reads naturally as 43% of the growth spending,
which is how I applied it; the text could say "of the growth spending" to remove the second reading (43% of the debt
increase). (5) The template's fair-price line asks for a figure "on the equity alone and on equity plus net debt where the two
differ"; for a utility the all-equity fair price can be near zero or negative (here $3.52, with the growth case negative at
ten percent), as the 2026-10-18 paragraph notes of earlier runs; the reporting figure on that basis says little.
