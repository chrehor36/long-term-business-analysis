"""Writes THE BOX, AFTER THE STOP, the SELF-AUDIT and the framework notes into the run file."""
p = "Test Runs/2026-10-11 Run - UNP Union Pacific.md"
s = open(p, encoding="utf-8").read()

rep = {}
rep["""## THE BOX
*(not yet written)*"""] = """## THE BOX
**OUT at Q7, on the floor.** Value range $120.64 to $162.31 a share on the all-equity basis ($133.15 to $180.33
equity-only), literal window FY2021 to FY2025, against $278.34 (close 2026-10-09, aggregator); expected return at the
price 2.6% to 4.5% on every case, below the ten percent floor and below the 5.60% long Treasury. Q1 IN, Q2 IN, Q3 weighs
against, Q4 weighs against (no STOP), Q5 integrity IN and ability weighs for, Q6 weighs against (no STOP). Reporting
figures: fair price $59.30 (all-equity, central), $88.94 (equity-only). The pending Norfolk Southern merger, valued
beside as if closed with no synergy, $80.81 to $115.58 a share. No integrity facts adverse to the people were found."""

rep["""## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(not yet written)*"""] = """## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on the questions the STOP left unasked, each with its source **[M1997-127]**; written
down, not weighed; the box unchanged (operator rule 2).

**Q8 (the alternatives).** The long Treasury yields 5.60% (Step 0); every case of Q7's range earns 2.6% to 4.5% at the
price. The company's own alternative, its stock below value, is not open at this price (Q6: buybacks are paused for the
merger in any case, 10-Q Note 16).

**Q9 (the target's debt and exposures).**
- Debt $30,327M at 2026-06-30, all fixed-rate (10-K Item 7: "we did not have variable-rate debt"); contractual debt
  payments including interest $2,724M in 2026, $2,455M in 2027, $2,402M in 2028, $47,667M after 2030 (10-K, contractual
  obligations table). Fair value $24.7B against $30.3B carried (10-Q).
- Coverage on the speakers' measure, pre-tax earnings over interest **[L2012-002]**: FY2025 ($9,166M + $1,309M) /
  $1,309M = 8.0 times.
- Liquidity at 2026-06-30: $1.6B cash, $0.5B short-term investments, a $2.0B undrawn revolver, $600M undrawn on the
  receivables facility; access to that facility "may be reduced or restricted if our bond ratings fall to certain levels
  below investment grade" (10-K MD&A; 10-Q MD&A).
- The merger would add about $20B of new borrowing and NSC's $15.5B of net debt (combined net debt about $63.8B as if
  closed, Q7); the 10-K's risk factors say "the combined company will likely be required to comply with a leverage
  covenant" and that rating agencies "may take negative actions"; a $2.5B termination fee runs each way.
- Exposures: common-carrier obligation to carry hazardous materials, including toxic-inhalation-hazard chlorine,
  "regardless of risk or potential exposure to loss" (10-K Item 1A); NSC's own record carries the East Palestine
  derailment litigation of 2023 (NSC 10-Q, legal actions note). Personal-injury liability $413M accrued with a
  reasonably possible range to $530M; environmental $259M across 343 sites, 17 on the Superfund list; a putative class
  action under the Illinois Biometric Information Privacy Act, no estimate (10-K Note 17). The fuel-surcharge antitrust
  cases, summary judgment for the railroads 2025-06-24, on appeal (10-K Item 3).
- Pension and retiree plans funded at 2025-12-31 (10-K MD&A).

**Q10, Q12.** Nothing recorded.

**Integrity (Q5) facts.** None adverse found; nothing to flag in the box line."""

rep["""## SELF-AUDIT
*(not yet written)*"""] = """## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit eff748e8, before the first EDGAR request); written question by
      question; committed after each question with a pathspec of the run file and the research folder only.
- [x] Dispatched run: the brief allowed per-question commits; the lock is the dispatching session's (not touched here);
      the fold is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One listing of `Test Runs/` (by name
      pattern for today's date, to check this file's name) showed four other runs' file names; declared under
      contamination, not opened, not used. The session context showed the TXN fold's commit subject; declared, not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check
      script `_research 2026-10-11 UNP/scripts/check_run.py`, output `check_run_output.txt`); every filing fact carries
      its accession or names its filing; no E-ids.
- [x] The order was kept: Q1 to Q6 answered (no STOP closed among them), Q7 closed OUT, Q8 to Q12 NOT REACHED; nothing
      after Q7 is a clearance.
- [x] Owner cash after every real cost (all capital spending, stock pay, finance-lease principal), never a net-income
      proxy; the sovereign from the US Treasury par curve (issuing authority); the price is an aggregator quote and is
      flagged.
- [x] Contrary evidence written down as found (foundations paragraph, Q2's volume and coal lines, Q3, Q4); facts for
      later questions under AFTER THE STOP.
- [x] Not a point-in-time run; no anchor-date issue.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 material was ignored.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the research folder,
      `check_framework_output.txt`).

**Honest notes on the work.** (1) The prices paid for buybacks are compared with today's range, not with a range built
at each purchase date; stated in Q6. (2) The maintenance split uses the filer's "capacity and commercial facilities"
line as all of the growth spending and treats locomotives, freight cars and technology as maintenance, which lowers the
top of the range; a different split could raise it, but no split brings the expected return near the floor. (3) BNSF's
operating ratio carries Berkshire's purchase accounting; the comparison flatters UNP by an unstated amount. (4) NSC's
growth-spending split was not read, so the as-if-closed figure uses all-spending cases only. (5) The 2016-2020 to
2021-2025 sensitivity leaves finance-lease principal out of both windows because it is not tagged before 2019.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR"""

rep["""## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
*(not yet written)*"""] = """(1) **Q2's "ordinary returns" against replacement cost.** The convention judges the field's returns "from the filer's
and the rivals' own filings" in words, and the castle rows define the return on "the capital actually needed in the
business" **[M2010-090]**; but for a railroad the rows themselves say the return on replacement value is "a pittance"
**[M2024-058]** while the return on historical cost is well above ordinary (UNP 14% to 17% before tax on net property).
The framework does not say which base the "ordinary returns" test reads, and the two bases give opposite answers for
every railroad. This run read the castle test on historical cost and carried replacement cost to Q3 and Q4; a reader who
chose replacement cost would close Q2 OUT. A sentence naming the base is needed. (2) **Specific (e) and negative growth.**
The inversion rule ("the maintenance-only no-growth case is the top of the range and the growth case the bottom") is
written for growth spending that buys too little growth; when owner-cash growth is negative on every series, the rule
still applies, but the text does not say whether the "growth case" at the bottom is the all-spending series at its own
(negative) rate or the maintenance-only series at its rate; this run used the all-spending series, the more conservative,
and says so. (3) **Specific (a), what makes an end year "aberrational on the filer's own description".** FY2021's low
capital plan was described by the filer as a plan made possible by freed capacity, not as an unusual year; the rule
gives no test for a filer's neutral description of an unusual number, and an analyst could have read FY2021 either way.
The box did not turn on it here (the cycle sensitivity is shown beside). (4) **The brief's instruction on competitors**
("the rivals the 10-K itself names, up to three that file with the SEC") gave one railroad, BNSF; the 10-K names trucks,
barges, ships and pipelines only as classes. A one-rival comparison was the honest result; the framework's Q2 asks for
"the competitors" in the plural and does not say what to do when the filer names one."""

for a, b in rep.items():
    assert a in s, a[:50]
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
print("ok")
