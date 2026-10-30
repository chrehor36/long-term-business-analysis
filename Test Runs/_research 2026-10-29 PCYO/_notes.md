# PCYO run 2026-10-29: working notes (research folder)

## Framework notes (read THE FRAMEWORK v5.md top to bottom in slices, 2026-10-29)
- Boxes: IN / OUT / TOO HARD (WORK or NATURE). TOO HARD (WORK) opens a research pass (steps 1-2 written, not run, per brief).
- Foundations: not a gate. Contrary evidence written down as found [M1997-127].
- Standing rule: buyer's conduct, not the target's.
- Q1 STOP: ten-year economics foreseeable; start-ups OUT [L2007-015], [M2008-088]; fast change TOO HARD; holding co / segments read by parts (part decides >50% of 5y op profit, else largest).
- Q2 STOP: castle tests 1-11; competitor row from filings; parts table; field returns over full cycle judged in words; durable castle with ordinary returns = OUT; regulated return exception carried to Q3 [M2009-104],[L2009-012]; change for better credited only on a full cycle (else TOO HARD NATURE with re-look condition); commodity business: low-cost producer test.
- Q3 WEIGHING: return on tangible capital needed; maintenance vs growth spend; growth arithmetic; capital-heavy as second best.
- Q4 STOP on confusion/suspicion: balance sheets 8-10 years first [M2025-032]; real costs; tells; suspicion -> OUT; confusion -> TOO HARD WORK/NATURE; make-the-numbers habit weighed, carried to Q5. Construction in progress named as prone to games [M2013-086].
- Q5 STOP on integrity (doubt closes [M2013-088]); ability weighing.
- Q6 WEIGHING: retention test, buybacks vs bottom of Q7 range, issuance; all-stock deal in undervalued stock = STOP. Part B pay, board.
- Q7 STOP: 5y avg owner cash after every real cost; growth shown on aggregate owner cash, capped; 10y then zero nominal growth; at long govt rate; ends no-growth and shown-growth; specifics (a)-(f); floor tested first (no case earns ~10% at price -> OUT); then >3:1 width -> TOO HARD; price inside or just below narrow range -> OUT; IN only if screamer. All-equity basis central (owner cash before interest vs EV), equity-only beside. Utility exception: equity-only central with LT-debt credit vs growth spending, capped at allowed debt share.
- Fair price: each end valued at 10%, averaged, per share, all-equity less net debt; equity-only beside.
- Q8 STOP bond/alternatives; Q9 weighing (little or no debt is the whole-business STOP); Q10 weighing; Q12 optional.
- Part VII: tools/run.py arithmetic lines only; AFTER THE STOP facts section; research pass only where some case earns floor at price.

## Blind-rule / contamination log
- The gitStatus snapshot at session start listed recent commit subjects about another company (CDZI) and an untracked file in another company's research folder (ARCB). Nothing about PCYO. Not used.
- MEMORY.md index in the session context mentions queue state and holdings counts in general terms; no line names PCYO. Not used.

## Run decisions (2026-10-29)
- FY2026 10-K not on EDGAR (latest filing a Form 4 of 2026-09-23). Latest period: 10-Q to 2026-05-31.
- Not a regulated utility for Q7: no allowed return; contractual cap (average of three neighbours) set by a district the company's officers direct.
- Parts: land 62% of FY2021-25 segment profit -> decides. Water read too: ~8% pre-G&A on segment assets.
- Competitors: 10-K names Aurora (municipal, no SEC filing) and unnamed developers -> CONVENTION set FOR, FPH, JOE (rivals.py).
- Q1 IN; Q2 OUT (ordinary field returns; finite parcel). COMPUTATION in q7_compute.py / q7_output.txt.
- tools/run.py capex line incomplete (one tag of four investing lines).
- Write-early breach: Step 0 to Q2 written in one pass after the research; declared in the self-audit.
