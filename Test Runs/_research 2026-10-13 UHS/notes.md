# UHS run 2026-10-13, working notes
- 2026-10-13: template copied to the dated run file before any fetch. Research folder created; raw filings go to cache/ (ignored).
- Contamination, declared at start: a directory listing of Test Runs/ filtered for "UHS" showed one filename, "2026-07-15 Run - UHS (Universal Health Services).md" (not opened). The git status/recent commits shown to the session name a THC run (TOO HARD (NATURE) at Q1, with figures in the commit subjects). Neither used.
- Q1 closed TOO HARD (NATURE) and committed. Facts after the stop, COMPUTATION (q7.py), self-audit, unclear section written.
- Scripts: fetch.py (EDGAR), strip.py (htm to text, into cache/), flat.py, facts.py and comp.py (XBRL series and competitor row), q7.py (range and fair price), row.py and check_ids.py (ledger checks). Raw filings and dumps stay in cache/ (ignored).
- check_ids.py: 17 ids, 16 fragments, 0 problems. tools/check_framework.py: PASS.
