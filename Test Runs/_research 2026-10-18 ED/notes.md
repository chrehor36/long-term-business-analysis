# ED run notes 2026-10-18

Run started 2026-10-18; template copied before any fetch.

## Working notes
- Filings fetched to cache/filings (ignored): 10-K FY2025/24/23/22/20/19, 10-Q 2026Q2, DEF 14A 2026, 8-Ks, earnings presentation.
- Peers fetched to cache/peers: National Fuel Gas 10-K FY2025, National Grid plc 20-F 2026/2024/2022, Avangrid 10-K FY2023.
- Scripts: fetch.py, html2txt.py, facts.py, row.py (ledger lookup), q7.py (Q7 arithmetic; output q7_output.txt).
- Contamination: none opened; seen git status commit subjects (ELPC, AYI, ARCB) and memory index; framework Q7 utility note.

## Resume 2026-10-18 (after the session limit)
- Verified q7.py inputs against filed cash-flow statements (Con Edison FY2025/FY2023/FY2022; CECONY debt flows; CEB OCF in FY2022 segment liquidity table).
- Wrote Q1 to Q7 one commit each; Q7 OUT; Q6 buyback line written back with Q7; end sections; check_ids.py 0 problems; check_framework PASS.
- Drafts of each section kept here (draft_q2..q7, draft_end).
