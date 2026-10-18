# NCTKF (Nabtesco, TSE 6268) research notes, 2026-10-16
- Run file copied from template before any fetch.
- Raw downloads go to cache/ (untrusted data); scripts in scripts/.

## Sources (all downloaded to cache/, gitignored; re-fetchable from nabtesco.com/en/about/ir/library/settlement/<year>/)
- Amended ASR FY2025, FY2024, FY2023 (filed 2026-09-30); original ASR FY2025 (2026-03-25); amended Semiannual FY2026.
- Tanshin FY2016-FY2025; corrections of FY2025 tanshin and FY2026 Q2 tanshin (2026-08-14, 2026-09-30).
- Notices 2026-09-30 (restatement; material weakness), 2026-10-01 (buyback status), 2026-10-14 (Q3 date moved).
- Briefings FY2025 (2026-02-18), FY2026 Q2 script and Q&A, referential data 2026-02-12.
- Harmonic Drive Systems: chart data on hds.co.jp IR highlights (xj-storage feed), FY3/2023-FY3/2026.
- Price: Yahoo Finance chart API 6268.T (aggregator). JGB 30y: MOF jgbcme.csv via tools/sources.py.

## Scripts
- scripts/arith.py -> arith_output.txt (owner cash, range, fair price). scripts/check_ids.py (citation check).
- scripts/rows.py, dumpall.py, pages.py, links.py, hds_parse.py, row.py: extraction helpers.

## Result
- Q1 IN; Q2 OUT (deciding part Component Solutions; ordinary and narrowing returns over the cycle).
- COMPUTATION: range JPY 1,204-2,991 (all-equity), fair 1,084 (equity-only 661) vs price 4,488.
