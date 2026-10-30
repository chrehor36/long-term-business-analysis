# VGNT research notes (2026-10-26)
Working notes for the purchase run. Raw filings in cache/ (gitignored).

## Contamination log
- A directory listing of Test Runs/ (to check that no VGNT file exists before copying the template) showed file names of
  other 2026-10-26 runs (ASML, NRG, OGE, PAM, PCG, PEG, PLTR, PNW, PPL, RWEOY, SNPS, SO, TAC, UTL); no file opened; none
  concerns Versigent or Aptiv. Recent commit subjects (UTL run) seen in the session header; not used.

## Framework notes (read 2026-10-26 in slices: lines 1-1639 and 1798-1916; Part V closing note and Part VI lines 1639-1797 skimmed by heading only)
- Boxes: IN / OUT / TOO HARD (WORK or NATURE). Q1 STOP (fast change -> TOO HARD at Q1). Q2 STOP (open castle OUT; can't judge TOO HARD; field earning ordinary returns over a full cycle OUT; high-cost producer in commodity field OUT; business of parts: part >50% of 5y op profit decides). Change for better credited only on a full cycle -> TOO HARD (NATURE) with re-look.
- Q3 weighing; Q4 STOP on confusion (TOO HARD WORK/NATURE) / suspicion (OUT); balance sheets 8-10 yrs first [M2025-032]; adjusted figures/guidance weigh against, carried to Q5.
- Q5 integrity STOP on doubt [M2013-088]; Q6 weighing (all-stock deal in undervalued stock is a STOP).
- Q7: 5-yr avg owner cash after every real cost; growth shown (aggregate) capped; 10 yrs then zero nominal; long govt rate; ends no-growth and shown growth; floor ~10% after company tax tested first (OUT if no case earns floor at price); TOO HARD if width > ~3:1; OUT if price inside/just below; IN only screamer. Six specifics (a)-(f). All-equity basis central (owner cash before interest, vs mkt cap + net debt; operating leases out), equity-only beside. Fair price = avg of two end cases valued at 10% discount, per share, all-equity less net debt.
- Q8 STOP (bond, more of what owned); Q9 weighing (little or no debt is STOP only for whole business); Q10 weighing; Q12 optional.
- tools/run.py: arithmetic lines only.

## Close (2026-10-26)
- Box: OUT at Q2. COMPUTATION: range $43.43-$92.57 (all-equity, no growth, 3 filed years, FY2023 in/out); fair price $25.23 all-equity, $31.73 equity-only; price $41.40 (2026-10-23).
- check_ids.py: 49 ids, 24 quoted fragments, 0 problems. tools/check_framework.py: PASS.
