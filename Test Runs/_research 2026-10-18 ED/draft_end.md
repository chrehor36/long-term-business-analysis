
## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed OUT). Facts under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7**: the equity-only value range (central, the regulated utility) is $14.35 to $61.04 a share against $112.26, the
best case returns 2.95 percent at the price, and no case earns the floor (fair price $20.24 equity-only central, -$57.52
all-equity beside). Q1 IN, Q2 IN, Q3 UNDECIDED, Q4 WEIGHS AGAINST, Q5 integrity IN and ability WEIGHS FOR narrowly, Q6 Part A
and Part B WEIGH AGAINST. Not a TOO HARD; no research pass. *Re-look condition (the operator's alert, not a rule): the fair
price; and a fresh Q7 when the income-tax audit or the weld investigation is decided, or a new rate plan changes the allowed
return.*

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.
- **Q8 (the bond).** The 30-year Treasury yields 5.43 percent (Step 0); the top case of the range returns 2.95 percent at the
  price and the strongest contrary test 7.87 percent (Q7).
- **Q9 (debt and exposures).** Pre-tax income plus interest over interest (consolidated, 10-K income statements via the XBRL
  facts, the 2023 pre-tax gain of $865M removed): 2.2 times in 2020, 2.5 in 2021, 3.5 in 2022, 3.1 in 2023, 2.8 in 2024, 3.1 in
  2025. Borrowings at 2026-06-30: long-term debt $26,843M, current portion $250M, notes payable (commercial paper) $721M; cash
  $1,470M (10-Q `0001047862-26-000142`). The company plans long-term debt of "up to $3,200 million" in 2026 and "up to $3,000
  million" in 2027, "including for maturing securities", and about $9,900M in 2028-2030 (10-K Item 1): the maturities are
  refinanced, not paid. The parent's dividends and interest depend on dividends from the Utilities, which the NYSPSC limits to
  "not more than 100 percent of their respective income available for dividends calculated on a two-year rolling average
  basis" (Item 1A). One dense territory: the 2014 East Harlem explosion (eight dead), the open weld investigation, and the
  10-K's risk that "A failure of, or damage to, these facilities [...] could result in bodily injury or death" (Item 1A); the
  tariff limits liability for service interruptions to gross negligence or willful misconduct (Item 1).
- **Q10.** Nothing recorded.
- **Q12.** Delivery of electricity, gas and steam in New York City; no business named in Q12's list. Nothing recorded.
- **Integrity facts** were judged at Q5, which was reached; no flag is owed.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). Step 0 to
      the lines of evidence were committed before the session limit (6d8106c7); Q1 to Q7 were written and committed one by one
      on resume.
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's; the fold is the
      dispatching session's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Contamination declared at the top;
      added on resume: the opening commit list of this session showed the subject "Overnight log: ED skipped, run file fresh"
      (a scheduling note, no result) and subjects of an ELPC run (another company); not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (`check_ids.py`
      in the research folder, 0 problems); no E-id; every filing fact has its accession.
- [x] The order was kept; Q7, the first STOP that failed, closed the run; nothing after it is a clearance. The Q7 arithmetic was
      computed before the session limit (`q7.py`) and was not read into Q1 to Q6 as a clearance; Q6's buyback line was written
      back with Q7, as the template asks.
- [x] Owner cash after every real cost, never a net-income proxy: built by hand from the filed cash-flow statements; GAAP net
      income appears only as a labelled test of the close, forbidden as an input and not used in the range. The sovereign from
      the Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found: the foundations' earnings-yield-plus-growth case, the receivables, the tax
      asset, the welds, the regulator, each where found.
- [x] No row dated after the anchor (a live run; not point-in-time).
- [x] Only the arithmetic lines of `tools/run.py` were used; its capital spending stops at 2022 and omits cost of removal, so
      the series was built from the filed statements.
- [x] `python tools/check_framework.py` PASS before the final commit.
- Confessed weak points: (1) the O&R share of the debt credit is its gross issuance as the 10-Ks state it, its retirements not
  separated (an upper bound, at most about $120M a year); (2) the Clean Energy Businesses' operating cash for 2021 and 2022
  ($175M, $506M) was re-read on resume in the segment liquidity table of the 10-K FY2022 (`0001047862-23-000038`) and agrees;
  their depreciation ($231M, $178M), removed from the maintenance guess, was written into `q7.py` before the session limit
  and not re-read; (3) depreciation as the maintenance need is a stated guess the filing does not confirm; (4) the
  all-equity figure taxes interest at 25 percent, a round figure near the combined federal and state rate, not a filed rate;
  it decides nothing.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **"The long-term debt raised over the window"** (Q7, The regulated utility) does not say gross issuance or issuance less
retirements, nor whether a holding company's parent debt counts. Refinancing raises debt without funding any asset, so this
run credited the Utilities' issuance less retirements (central, $8,185M) and showed gross issuance beside ($9,300M); the
parent's debt was left out because the parent retired debt with the sale proceeds of a business removed from the series. The
two readings move the bottom case from $14.35 to $31.50 a share and decide nothing here, but on a closer price they would.
(2) **Whether the debt credit applies to the maintenance-only case.** Specific (e) makes the maintenance-only no-growth case
the top; the utility paragraph credits debt "against the capital spending it funded". At no growth the rate base and its debt
stay flat, so no new debt is raised and none was credited to the top case; the text does not say so. (3) **The cap's two
sentences in (f)**: "inside the ten years the shown rate is the cap" and, for an absurd rate, "the business's own sales growth
[...] never above the discount rate". Here the cut rate (7.53 percent) exceeds the sovereign, and the run carried 5.43 percent
on the second sentence. (4) **Q2 test 9 for a monopoly**: the test presumes rivals; the brief's departure supplied the
convention (the same regulator's other franchises), but the framework itself has no rule for a business whose filing names
no competitor. (5) **Q2's regulator exception** sends ordinary regulated returns "to Q3 as a second best", and Q3 has no
paragraph that receives them; Q3's test 4 covered it in substance.
