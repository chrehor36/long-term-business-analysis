# ES research notes (2026-10-23)

Working folder for the ES purchase run of 2026-10-23 (blind dispatched run).
- cache/ holds the fetched filings as text (gitignored); fetch.py fetches from EDGAR with the brief's User-Agent.
- run_py.txt, cover_shares.txt: tool outputs (arithmetic only).
- q7.py / q7_out.txt: the Q7 arithmetic (equity-only central, regulated utility).
- comp_roe.txt: the competitor return-on-equity row (ES, UTL, AGR) from XBRL companyfacts, one figure per rival cross-checked to the filed 10-K.
- row.py, rows1.txt, rows2.txt: ledger rows read for citation.
- check_run.py: the run's id and fragment check.
