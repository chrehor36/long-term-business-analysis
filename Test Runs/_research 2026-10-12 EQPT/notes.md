# EQPT research notes (2026-10-12)

Working notes for the run. Raw filings fetched to this folder.

## Files
- scripts/fetch.py, scripts/fetch_any.py, scripts/strip2.py: fetch from EDGAR and strip to text (raw files in cache/, gitignored).
- scripts/owner_cash.py -> owner_cash_output.txt: owner cash by year from the filed cash-flow statements.
- scripts/peers.py: peer XBRL figures (URI, HRI, SUNB) for the Q2 competitor row.
- scripts/q7_computation.py -> q7_computation_output.txt: COMPUTATION, NOT A CLEARANCE (range, fair price).
- scripts/form4.py -> form4_summary.txt: insider Forms 4 since 2026-05-01.
- scripts/check_run.py: citation check of the run file (no E-ids; ids exist; fragments in rows).
- q2_section.md, tail_section.md: drafts of run-file sections, inserted into the run file.
- rf_headings.txt: the 71 risk-factor headings of the 10-K for 2025.
