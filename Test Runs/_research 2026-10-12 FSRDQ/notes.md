# FSRDQ research notes (2026-10-12)
- template copied to run file before any fetch.
- tools: run.py and cover_shares.py refuse FSRDQ (not in SEC ticker list); run.py driven by CIK through run_by_cik.py (output runpy_out.txt).
- filings fetched to cache/ (gitignored) by fetch.py; accessions listed in the run file, Step 0.
- price: no aggregator quote for FSRDQ, FSRNQ, FSRN, FSR (Yahoo, 2026-10-12). FINRA UPC #75-24 (2024-10-18): plan effective 2024-10-17, all equity interests cancelled, no distribution; ticker FSRNQ.
- Tesla competitor row from XBRL companyfacts (cache/peers/TSLA_facts.json).
- q7_computation.py / q7_out.txt: COMPUTATION, NOT A CLEARANCE figures.
- check_citations.py / check_citations_out.txt: 22 ids, 15 fragments, 0 problems. tools/check_framework.py PASS.
- Box: OUT at Q1 (start-up by its own 10-K; equity cancelled under the plan). Integrity facts recorded, not judged.
