# MTSUY (Mitsui & Co., TSE 8031) research notes, 2026-10-12
Working notes for the run file `Test Runs/2026-10-12 Run - MTSUY Mitsui and Co.md`. Raw PDFs go under cache/ (ignored).

## Contamination log
- 2026-10-12, first command of the run: a filtered `ls "Test Runs/" | grep` for the ticker (meant to check the run-file name was free) printed four file names: two runs dated 2026-07-15 (one "MITSY (Mitsui & Co)", one "MTSUY (Mitsubishi Corp)"), a v4.1 run dated 2026-08-28 "MITSY (Mitsui)", and a holding review dated 2026-10-05 "MITSY Mitsui & Co". None opened. Declared, not used.

## Files
- scripts/pagerows.py: page text by rows (the PDFs' text layer is out of order). scripts/owner_cash.py: owner cash
  FY2016-26 with the investing-total check. scripts/valuation.py (literal window) and valuation_cycle.py (cycle base):
  Q7. scripts/check_citations.py: the brief's citation check.
- extracts/: page-row extracts of the statements from the six reports. The parser output statements_10y.csv was removed
  (its generic parser misread several lines); owner_cash.py holds the hand-checked figures and supersedes it.
- drafts/: the sections as written before each was appended to the run file.
