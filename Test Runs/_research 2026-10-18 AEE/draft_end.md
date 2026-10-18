
## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT). The bond comparison is recorded under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts recorded under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts recorded under AFTER THE STOP.

---
## THE BOX
**OUT at Q7**, the floor: value range **$18.84 to $36.89 a share on the all-equity basis** (equity-only $69.86 to
$87.91) against **$106.08** (close 2026-10-16, aggregator); no case earns about ten percent at the price (2.87% to
3.93% on enterprise value). Q1 IN, Q2 IN (a regulated franchise, its return carried to Q3), Q3 weighs against, Q4 weighs
against, Q5 integrity IN with ability weighing for modestly, Q6 weighs against. Re-look condition: the alert at the top
of the computed range, as for any OUT (Part VII).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.
- **Q8 (the bond).** The 30-year Treasury yields 5.43% (US Treasury, 10/16/2026). The cases in Q7 return 2.87% to 3.93%
  at the price on the all-equity basis and 3.58% to 4.85% on the equity-only basis.
- **Q9 (debt and exposures).** Debt was 60% of debt plus equity at 2025 year-end (52% in 2016); pre-tax interest
  coverage 3.1 times in 2025, down from 3.7 in 2016 (Q4). Total debt $21.8 billion at June 30, 2026, including $1,220M
  of short-term debt; credit agreements of $3.2 billion through December 2030, subject to a 364-day repayment term for
  Ameren Missouri and Ameren Illinois (10-Q, Liquidity). Ameren is a holding company whose dividends and debt service
  depend on distributions from its subsidiaries (10-K Item 1A). After the quarter: $900M of junior subordinated notes due
  2057 (8-K of 2026-09-18) and $400M of Ameren Illinois first mortgage bonds (8-K of 2026-08-24). Planned capital spending
  of $30.5 to $33.1 billion for 2026 to 2030 is to be funded by debt and equity (10-K Item 7; 10-Q Outlook). The
  acquisition criterion "little or no debt" is stated for whole businesses **[R1997-001]**; this business would not meet
  it. Earnings come from two states and three regulators, four segments (Q2's parts table).
- **Q12.** Coal supplied 56.5% of Ameren Missouri's energy in 2025 (10-K Item 1, operating statistics); the Rush Island
  plant was retired early after a federal court found Clean Air Act violations (Q5). None of the businesses Q12 names
  (casinos, tobacco, loading schemes, gambling dressed as investing) is present.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      **Departures, declared:** (1) the first full write replaced the template's body after Q2, and the template's
      later headings were rebuilt in order as each question closed (Q3 onward appended one section at a time, each
      committed); (2) the Q7 arithmetic (`q7.py`) was first computed in the research folder after the Q2 commit and
      before Q3 to Q6 were written; it bore no entry language, but its result leaked into one sentence of Q6 committed
      before Q7 (Part A, the retention test's intrinsic leg: "fails on Q7's arithmetic"), which should have waited for
      the write-back; the sentence is true of the Q7 now committed and is left as written; (3) the Q6 buyback and issuance
      lines were committed as placeholders and written back with Q7, as the brief requires.
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session (not touched here); the run is folded into the register by the dispatcher (operator rule ten). A run not
      in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule); what was seen
      by accident (another utility's commit subjects, the memory index) is declared under contamination and not used.
- [x] Every v5 id resolves (`check_run.py` in the research folder: every M, L and R id found in `principle_ledger_v5.csv`,
      every double-quoted fragment beside an id found in a cited row, no E-ids); every filing fact has its accession.
      Single quotes mark filing text, as stated at the top.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority (US Treasury); the price an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]**: the steady earned return (for the business),
      the serial issuance and the cash shortfall (against), the Rush Island ruling (Q5).
- [x] No row dated after the anchor is cited in a point-in-time run (this is a run of today; not applicable).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its v4 text and verdict-like lines were ignored.
- [x] `python tools/check_framework.py` PASS before the commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Specifics (e) and (f) of Q7 conflict for a business whose growth is bought by heavy spending.** (f) cuts an absurd
shown growth to the business's sales growth, capped at the discount rate; (e) says never charge the spending and also cap
the growth it bought. For a utility both trigger at once: the literal growth (32.6%) is absurd, and the growth spending
is charged. Applied mechanically, the cut and the charge together give $11.04 a share, a case (e) forbids. I credited
the growth case with the growth the spending bought at the incremental return Q3 measured (6.68%), which needs no cut,
and showed the mechanical figure beside. The text should say which specific governs when both apply. (2) **The
maintenance guess for a utility.** The rows allow depreciation as the proxy **[M1998-127]** and say a utility's
depreciation is inadequate **[M2015-049]**; the filing gives no maintenance figure. The framework's (e) asks for the
maintenance case "where the filing allows the guess" and says nothing of what to use when the rows themselves call the
usual guess too low. I used depreciation, flagged as generous; a stricter guess only lowers the range. (3) **Whose tax,
for a regulated company.** The statutory-rate convention is written for carryforwards and credits that run out; a
utility's low cash tax is mostly deferred tax and credit sales that ratemaking passes to customers **[M2015-030]**. The
framework has no rule for that case, and none for the tax rate on the interest add-back of the all-equity basis when
the company pays no cash tax; I used the filer's blended 26% and kept the as-paid tax, both confessed. (4) **The
equity-only growth case** is ill-defined: growth spending in a utility is about 60% debt-funded, so charging all of it
against owner cash after interest, while crediting the unlevered return, mixes bases; the figure is shown beside, as the
text says, and flatters. (5) **Serial issuance** stays a candidate STOP (Q6, Part A); for a utility whose issuance is
its announced funding plan the framework gives no guidance on whether the rows' "hell-bent on issuing shares" reaches it.
(6) **The competitor row** needs a CONVENTION whenever a 10-K names no rival, which is the normal case for a regulated
monopoly; the framework could say that peer utilities in the same wholesale market are the default.
