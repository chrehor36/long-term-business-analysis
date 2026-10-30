# CDTG run notes (2026-10-29)

## Framework v5 read (lines 1-1916, in slices; Q11 body and closing note skimmed only, not needed for a purchase run)
- Boxes: IN / OUT / TOO HARD (WORK or NATURE). Q4 suspicion -> OUT; confusion -> TOO HARD (WORK if knowable from a filing not read, NATURE if not).
- Q1 STOP: ten-year economics foreseeable; abroad: governance and tax nuances understood [M2000-141]; China paid more for [M2006-021]. Doubt = outside [M2002-092].
- Q2 STOP: castle tests 1-11; commodity + low-cost exception; ordinary-returns castle OUT (no figure); parts rule (>50% of 5y op profit decides).
- Q3 WEIGHING; Q4 STOP on confusion/suspicion, else weighing; balance sheets 8-10 years first [M2025-032]; tells [M1995-064] (receivables vs sales etc).
- Q5 STOP on integrity (doubt closes [M2013-088]); serial issuance [L2014-015] a tell (Q6 candidate second STOP).
- Q6 WEIGHING; all-stock deal in undervalued stock STOP [L2009-019].
- Q7 STOP: 5y avg owner cash after every real cost; aggregate growth; ten years then zero nominal; at sovereign; ends = no-growth and shown-growth; floor tested first (~10% on company after-tax owner cash); width >3:1 TOO HARD; inside or just below range OUT; specifics (a)-(f); all-equity basis central; fair price = average of the two end cases valued at 10%, per share, less net debt.
- Q8 STOP; Q9 WEIGHING; Q10 WEIGHING; Q12 optional.
- Research pass (TOO HARD WORK) only where some case of the range earns the floor at the price; otherwise written and closed unrun (Part VII, 2026-10-12). Brief says: if TOO HARD (WORK), write steps 1 and 2, do not run them.
- tools/run.py: arithmetic lines only.

## Contamination log
- `git log --oneline -3` at start showed CWST commit subjects (another company, run under v5, OUT at Q2). Not used.
- `ls "Test Runs" | grep -i cdt` returned nothing (no other CDTG run file listed). Only the filtered result was seen.
- Memory index line (session context): mentions wave 7 queue state, gate-clearers count; nothing on CDTG. Not used.

## Close
- Box: OUT at Q2. check_framework PASS; check_ids 0 problems.
