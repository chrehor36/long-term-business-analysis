# APEMY research notes (2026-10-13)
- Run file copied from template before any fetch.
- tools/run.py and Screens/cover_shares.py: not an SEC filer (both refused).
- aperam.com served pages and the document list (admin-ajax get_docs, cat 8487) until ~19:35, then refused all connections.
- Annual reports taken as raw byte copies from the Wayback Machine (scripts/wb.sh): AR2025 (snapshot 2026-10-09), AR2024, AR2023, AR2021, AR2019, AR2017. AR2016, AR2018, HYR2026 and the Q2 2026 PDF were not archived.
- Q2 2026 release read via Investegate (EQS dissemination): q2_2026_release.txt.
- Primary statements extracted to stmts_AR*.txt; raw PDFs and full text dumps stay in cache/ (gitignored).
- Q7 arithmetic: scripts/q7_computation.py -> q7_computation_output.txt (COMPUTATION, NOT A CLEARANCE; Q2 closed OUT).
- Citation check: scripts/check_citations.py -> citation_check.txt.
