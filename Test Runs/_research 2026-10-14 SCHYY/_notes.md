# SCHYY research notes (2026-10-14)
Working notes for the run file `Test Runs/2026-10-14 Run - SCHYY Sands China.md`. Large downloads go to `cache/` (gitignored).

- 2026-10-14: template copied before any fetch; folder opened.
- Tools refused (non-SEC filer). Primary documents: HKEXnews ARs 2016, 2020, 2022, 2024, 2025; interim 2026; SCL 20-F XBRL (CIK 1755281). PDFs and text in cache/ (ignored).
- ADR ratio 1:10 from three F-6 filings (CIK 1491703).
- compute.py holds every hand-typed input with its source; run with `python -I compute.py`.
- Q1 closed TOO HARD (NATURE): concession to 2032-12-31, gaming assets revert without compensation; renewal terms unknowable.
- 2026-10-15 (resume, killed session of 2026-10-14): balance-sheet n/r cells filled (borrowings 2015, 2016, 2023). Rivals' FY2022 filings and the SCL FY2018 20-F fetched by `fetch_rivals22.py` into cache/ (Wynn 0001174922-23-000048, MGM 0000789570-23-000008, Melco 0001193125-23-086859, SCL 0001755281-19-000042).
- compute.py: net debt changed to face borrowings excluding lease liabilities (6,306) less cash 851 plus the interim dividend US$516M = 5,971 (lease principal already inside owner cash). Central growth = Q7 (b) halves of the cycle window (-10.64%); the phase comparison (-3.24%) beside.
- Rival Macao segment table (2017-2025) in compute.py, with accessions.
- 2026-10-15: THE BOX, AFTER THE STOP, COMPUTATION, SELF-AUDIT, framework gaps written. check_cites.py: no E-ids, all 30 distinct ids in the v5 ledger, every adjacent quote in its row (two heuristic artefacts verified by hand); one defect found and fixed (M1997-109 quote, dated note). check_framework PASS.
