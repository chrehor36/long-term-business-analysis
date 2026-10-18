## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. One fact found is under AFTER THE STOP.

---
## THE BOX
**OUT at Q7** (the floor, tested first): Q1 IN, Q2 IN (management and franchise decides at 97% of five-year segment profit;
a network of owners, members and booking channels tested through a full cycle; operating return on net tangible assets at
the top of its field), Q3 WEIGHS FOR, Q4 no STOP and WEIGHS AGAINST (Adjusted EBITDA featured and guided), Q5 integrity IN
on the record read with the habits weighing against, Q6 Part A WEIGHS AGAINST (buybacks with no stated price at $256 to
$327, above the top of the range, partly borrowed), Part B UNDECIDED. **Value range $56.50 to $147.79 a share (all-equity,
central; equity-only $82.56 to $150.00) against $329.59** at the 5.56% Treasury; no case the method allows earns the floor
at the price (best 5.7%, central top 3.1%). Fair price $27.98 all-equity, $61.49 equity-only (reporting figures, not
verdicts). Integrity facts recorded, not judged: one unverified recollection (Q5), given no weight.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed, each with its source **[M1997-127]**; the box is unchanged (operator rule 2).
- **Q8.** The ten-year comparison is the 5.56% thirty-year Treasury (10/13/2026) against expected returns at the price of
  1.6% to 5.7% on the cases Q7 allows (`calc_out.txt`). "one opportunity cost of buying the stock is to compare it with a
  bond" **[M1997-089]**.
- **Q9.** Debt and finance leases $13,444M at face at June 30, 2026 (10-Q, Note 4), weighted average rate 5.03% (Q2 2026
  release); senior secured term loans $3,119M due 2030; maturities at December 31, 2025: $25M (2026), $619M (2027), $12M
  (2028), $1,360M (2029), $4,124M (2030), $6,319M after (10-K, Note 10), plus $1.0B of 5.500% notes due 2031 issued in May
  2026; the release says "no material indebtedness that matures until April 2029, other than $600 million of outstanding
  Senior Notes due April 2027". Revolver undrawn, $1,894M available, extended to about March 2031 with a first-lien net
  leverage grid (8-K 2026-03-18). Pre-tax earnings over interest **[L2012-002]**: 4.6x (2023), 4.1x (2024), 4.3x (2025).
  Debt guarantees and loan commitments to owners $61M, performance guarantees $22M (Note 19); $77M paid on debt guarantees
  in 2024. Guest loyalty liability $2,913M and deferred revenues $2,506M at December 31, 2025, obligations to reimburse
  hotels for redemptions and to deliver services already paid for. Operating lease liabilities $730M (non-current) and
  minimum operating lease payments of $156M in 2026 (Item 7). Equity is a deficit of $5.4B. The "little or no debt"
  criterion **[R1997-001]** is stated for whole businesses; this name carries net debt of about 5.5 times its 2025 owner cash
  before interest ($12.4B against $2.2B).
- **Q12.** "We also manage hotels with casino gaming operations as part of or adjacent to the hotels" and, where Hilton
  operates the casino, it holds the gaming license (10-K, Item 1, Government Regulation). The rows name casinos among the
  businesses refused to be owned and run **[M2007-018]**. No figure for the size of this activity was found in the filings
  read.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `b05b1215`); written question by question; committed after each
      (Step 0 to Q1 `f48fa9d4`, Q2 `85e0a844`, Q3 `99793c97`, Q4 `9d77fe32`, Q5 `7457a24b`, Q6 `fa2a425b`, Q7 with the Q6
      write-back `049c56d7`, this close in the next commit).
- [x] Dispatched to an analyst: the brief allowed per-question pathspec commits of the run file and research folder only,
      and states that the lock is held by the dispatching session; the fold into the register is the dispatcher's and is
      not done here. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen by accident and declared at
      the top: the subject line of another company's fold commit in the git log shown at session start, which quotes a
      Hilton return figure. Not used; this run's own figure (Q2) was computed from Hilton's filings. The repository's
      `.gitignore` was read for the research-folder rules; it names no company.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check script
      `scripts/check_citations.py`, result in `check_out.txt`); no E-ids; every filing fact has its accession in Step 0 or
      beside it; numbers are filed figures, sums of them, or CONVENTIONs named in the text.
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; nothing after it is a clearance; Q8 to
      Q12 are NOT REACHED and their facts are under AFTER THE STOP.
- [x] Owner cash after every real cost from operating cash, never a net-income proxy (operator rule 5); stock pay, all
      capital spending, finance-lease principal and acquisitions deducted; the sovereign from the Treasury; the price an
      aggregator quote, flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (the foundations' list; Q2 tests 3, 5, 6, 8; Q3's key money;
      Q4's balance sheet).
- [x] No point-in-time anchor applies; the run is dated today and cites rows as the ledger holds them.
- [x] Only the arithmetic lines of `tools/run.py` were used; its owner-earnings windows were not adopted (they leave out
      acquisitions and finance-lease principal and use three or five years where Q7's cycle rule governs).
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in `check_out.txt`).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q4 says two things about EBITDA.** Its "What it rules OUT" list names "EBITDA as earnings and managements that talk it"
**[M2002-026]**, and the row itself says the count of such purchases "is going to be about zero"; the section A convention of
2026-10-06 records a featured adjusted figure at Q4 as a weighing and carries it to Q5. Hilton defines Adjusted EBITDA in
its 10-K, pays its officers on it and guides it quarterly; under the list it could close at Q4, under the convention it
weighs. I followed the convention, which is the later and more specific text, and say so; the list should say whether
"talk it" means using it as the measure or substituting it for earnings. (2) **Cycle rule (a) assumes successive cycles of
the same business.** A company re-formed by a spin-off in 2017 has one peak and one trough on file; the rule says
"peak to peak or trough to trough" and neither exists. I ran peak to latest year and confessed it. (3) **Rule (b) and cap
(f) together leave a choice of sales measure.** Growth between halves through a pandemic trough is 28.4%; (f) cuts it to
"the business's own sales growth over the same window (or between the same cycles)", which here is 4.7% end to end, 15.9%
between the halves (still carrying the trough), or 7.5% on the deciding part's fees. The text does not say consolidated or
deciding part, nor end points or halves. I took 7.5% as the top and showed the others; the box does not depend on the
choice (all fail the floor), but a closer case would. (4) **Customer advances inside operating cash.** Loyalty-program
deferred revenue added $368M a year to the cycle base; specific (d) counts working capital, but says nothing of float-like
advances that grow only while the system grows, and the framework's float treatment lives in the insurer method. The
company's own pay metric strips point pre-sales. I left them in (generous) and said so; a rule is wanted. (5) **The tax
rate on the interest added back for the all-equity basis** is not stated; I used the 21% federal statutory rate as a
CONVENTION of this run. (6) **Integrity on doubt alone, and the analyst's own memory.** Q5 applies "If you’ve got doubts,
forget it" **[M2013-088]** but does not say whether a doubt the analyst carries from outside the filings, unverified, counts;
I recorded it and gave it no weight, which a stricter reader could call the wrong side of the doubt rule. (7) **The template's
Q6 line** asks for the bottom of the Q7 range; here the prices paid were above the top as well, and the convention's words
("at or below the bottom") give no further grade; none was needed.
