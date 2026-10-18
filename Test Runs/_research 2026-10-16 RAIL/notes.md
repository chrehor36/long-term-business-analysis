# RAIL run notes, 2026-10-16
- Template copied to the dated run file before any fetch.
- Filings fetched into cache/ (gitignored): RAIL 10-K FY2021-FY2025, 10-Q 2026-06-30, DEF 14A 2026, 8-Ks 2026-07-02,
  2026-08-05, 2026-10-15; Trinity 10-K FY2017, FY2019, FY2021, FY2023, FY2025; Greenbrier 10-K FY2018, FY2020, FY2022,
  FY2023, FY2025; XBRL company facts for all three.
- Scripts: fetch.py, fetch2.py (EDGAR fetch and text), xbrl.py, inst.py (XBRL annual and instant values),
  field.py (field returns table, output field_out.txt), q.py (ledger quote lookup).
- Price 5.92 (Yahoo, 2026-10-16 close, aggregator). Shares 32,791,280 (10-Q cover 2026-07-31). Sovereign 5.43%.
- Q1 closed IN.
- Q2 closed OUT: field ordinary returns; no low-cost position vs Greenbrier; money test fails; 2026 margin fall.
- Close: COMPUTATION (valuation.py, valuation_out.txt), after-the-stop facts, box, self-audit, framework notes. check_ids PASS; check_framework PASS.
