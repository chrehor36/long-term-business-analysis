# DUK run notes, 2026-10-18 (working file of the analyst)
- Run file copied from the template before any fetch.
- tools/_cache/duk_tmp existed at dispatch (timestamped 18:46 today) holding a 10-K htm, sub.json and four 8-K htm; not made by this analyst; filings re-identified by accession before use.
- 2026-10-22 resume: Q2 to Q7 written and committed one by one; no refetch. New scripts: peers2.py (comparators, per-year tag fallback; peers.py's per-company fallback mis-read SO 2025 and the AEP/D capex tags, not used), q7.py (all Q7 cases, the floor test, fair price), check_run.py (no E-ids, ids exist, quoted fragments in rows). Outputs: peers_output.txt, q7_output.txt.
- Box: OUT at Q7. Central equity-only range $71.06 to $109.64 vs $121.47; fair $47.30 equity-only; all-equity -$35.73.
