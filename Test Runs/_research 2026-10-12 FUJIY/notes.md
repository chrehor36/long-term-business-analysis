# FUJIY research notes (2026-10-12)
- Template copied before any fetch.
- Contamination: a `ls "Test Runs" | grep -i fuji` at the start showed two file names, `2026-07-15 Run - FUJIY (Fujifilm Holdings).md` and `2026-07-15 Run - FJTSY (Fujitsu Ltd).md`. Neither opened. Declared in the run file.
- Sources: all from ir.fujifilm.com (TSE disclosures, English): annual results releases FYE 3/2016 to 3/2026, Q1 FY2026 results, Integrated Reports 2025 and 2021, notices. Raw files in cache/ (gitignored).
- extracts/: cash-flow pages (cf_*.txt), balance-sheet lines (bs_lines.txt), Q7 computation output (q7_output.txt).
- scripts/: rows.py (page rows), find.py (search), row.py (ledger lookup), q7.py (Q7 computation), check_ids.py (id/quote check).
- Competitors: Canon 20-F FY2022 (0001193125-23-084415) and FY2019 (0001193125-20-087524) read for the Imaging unit; Sony, Kodak listed as SEC filers, not used (see run file); Polaroid, Nikon not SEC filers.
