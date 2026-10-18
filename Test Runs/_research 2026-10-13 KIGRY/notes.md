# KIGRY research notes (2026-10-13)

Run file copied from template before any fetch.

## Sources fetched (kept in cache/, gitignored)
- AR 2025 (reports.kiongroup.com/2025/ar/_assets/downloads/2025-Q4_Annual-Report_KION_Group.pdf), AR 2024, AR 2023, AR 2022,
  AR 2021, AR 2019, AR 2018, AR 2017 ("entire" PDFs); Q2 2026 interim report (kiongroup.com). AR 2020 English not found.
- Price: Yahoo chart API KGX.DE (XETRA) close 2026-10-12 EUR 33.85; KIGRY USD 9.35; EURUSD 1.1177 (aggregator).
- ADR ratio: Deutsche Bank Trust Company Americas F-6 POS, 2017-09-18, acc. 0001193805-17-002687: one ADS = one-fourth share.
- Sovereign: tools/sources.py, ECB SR_30Y 3.78% dated 2026-10-09.

## Calculations
- calc/owner_cash.py -> calc/owner_cash_output.txt (owner cash 2018-25 from filed cash flow statements)
- calc/q7.py -> calc/q7_output.txt (COMPUTATION, NOT A CLEARANCE; range and fair price)
- calc/check_ids.py (no E-ids; every M/L/R id in the v5 ledger; quoted fragments in their rows)

## Result
OUT at Q2 (ordinary returns over 2017-25 on the filer's own figures; no rival named in any report).
