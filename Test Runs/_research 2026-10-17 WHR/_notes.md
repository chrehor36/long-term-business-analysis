# WHR run notes 2026-10-17
Working notes for the WHR v5 purchase run. Started before any fetch.

## Sources fetched (raw files in cache/, ignored)
- WHR 10-K FY2025 0000106640-26-000009; 10-Q Q2 2026 0000106640-26-000061; 10-Q Q1 2026 0000106640-26-000036
- DEF 14A 2026 0001193125-26-100387; 8-Ks listed in the run file; 424B5s 0001193125-26-076958 / -076926
- 10-K FY2022 0000106640-23-000015, FY2019 0000106640-20-000017, FY2016 0000106640-17-000013 (segment notes)
- 13D 2026-03-03 0001493152-26-008749, filed by Appaloosa LP (index page only)
- Electrolux: financial data spreadsheet of the Q4 2025 interim report,
  https://www.electroluxgroup.com/wp-content/uploads/sites/2/2020/01/electrolux1_finstat-2512AC-Final-1.xls
  (quarterly 2017-2025); summed to years by scripts/elux_annual.py -> electrolux_annual_from_finstat.txt.
  Cross-check: 2025 net sales 131,282 and OI excl NRI 3,657; 2024 136,150 and 1,666 match the year-end report page
  https://www.electroluxgroup.com/en/electrolux-group-year-end-report-q4-2025-45752/
- The full Electrolux Annual Report 2025 PDF (>10MB) could not be downloaded (curl hung; fetch size limit).
