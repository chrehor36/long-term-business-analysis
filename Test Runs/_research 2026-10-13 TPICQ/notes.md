# TPICQ research notes (2026-10-13)

- Price: aggregator only (digrin.com, $0.01, Oct 2026); Yahoo/Stooq/OTC Markets API returned nothing.
- run.py and cover_shares.py cannot resolve TPICQ; run_wrapper.py patches the CIK lookup (0001455684) and injects the price.
- Raw filings kept in cache/ (gitignored): TPI 10-Ks FY2020, FY2024, FY2025, 10-K/A FY2024, 8-Ks 2026-03-05 and 2026-03-09;
  GE 10-Ks FY2018, FY2021, FY2023; GE Vernova 10-K FY2025.
- check_ids.py: no E-ids, every id in the v5 ledger, every quoted fragment beside an id in its row. Result: 29 ids, 0 problems.
- tools/check_framework.py: PASS (2026-10-13).
- Box: OUT at Q2. COMPUTATION: range -25.07 (all-equity, cycle base) / -38.73 (literal) a share vs $0.01; fair -18.03 / -11.09.
