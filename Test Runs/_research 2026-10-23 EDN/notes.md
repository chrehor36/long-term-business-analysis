# EDN research notes 2026-10-23

Working notes for `Test Runs/2026-10-23 Run - EDN Edenor.md`. Raw filings are under `cache/` (gitignored); every figure below
is from a filed statement, accession in the run file.

## Filings fetched (EDGAR, User-Agent Chris Hrehor)
- 20-F FY2025, filed 2026-04-15, 0001292814-26-002270 (ednform20f_2025.htm)
- 20-F FY2024, filed 2025-04-22, 0001292814-25-001581 (restated 2022 and 2023: deferred tax error, material weakness)
- 20-F FY2022, filed 2023-04-19, 0001292814-23-001639
- 20-F FY2020, filed 2021-04-26, 0001292814-21-001740
- 20-F FY2018, filed 2019-04-30, 0001292814-19-001619
- 6-K Q2 2026 interim statements, 2026-08-11, 0001292814-26-004179
- 6-K 2026-08-11 press release (EBITDA headline), 0001292814-26-004183; BYMA results letter 0001292814-26-004180; board minutes 0001292814-26-004184
- 6-K 2026-10-09, call of ordinary meeting for 2026-11-12, 0001292814-26-004882 (agenda not in the 6-K)

## Measuring units (IAS 29)
Each 20-F is in constant pesos of its own year end. Filer's annual inflation (2025 20-F, Note 3): 2021 50.9%, 2022 94.8%,
2023 211.4%, 2024 117.8%, 2025 31.5%. Dec-22 to Dec-25 factor 3.114 x 2.178 x 1.315 = 8.919. Dec-24 to Dec-25 1.315.
Checks: 2024 OCF 245,917 (2024 20-F) x 1.315 = 323,381 vs 323,500 in 2025 20-F; 2020 loss 17,698 (2020 20-F) x 1.509 x 1.948 =
52,023 vs 52,017 in 2022 20-F. Dec-25 to Jun-26: equity at Dec-25 2,222,906 restated in the Q2 interim as 2,597,380, factor 1.1685.

## Owner cash, Dec-2025 pesos, billions (script run in this session)
| year | OCF | capex | lease principal | interest paid | all-equity | equity-only | net new borrowing | credit (cap 38.1% x capex) | equity-only with credit | PP&E depreciation |
|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | 370.9 | 255.8 | 9.1 | 15.5 | 105.9 | 90.4 | 0.0 | 0.0 | 90.4 | 158.1 |
| 2022 | 315.9 | 282.9 | 10.4 | 8.0 | 22.6 | 14.6 | -14.8 | 0.0 | 14.6 | 162.2 |
| 2023 | 204.7 | 343.1 | 18.5 | 5.3 | -156.9 | -162.2 | 47.0 | 47.0 | -115.3 | 237.1 |
| 2024 | 323.5 | 473.5 | 16.0 | 40.4 | -166.0 | -206.4 | 430.0 | 180.4 | -26.0 | 203.3 |
| 2025 | 192.0 | 368.5 | 12.3 | 92.1 | -188.8 | -280.8 | 557.7 | 140.4 | -140.4 | 203.3 |
| avg | 281.4 | 344.8 | 13.3 | 32.3 | -76.6 | -108.9 | | | -35.3 | 192.8 |

Depreciation variant (OCF - PP&E depreciation - lease principal - interest paid): 188.2, 135.3, -56.2, 63.8, -115.7; avg 43.1.

## Operating result / revenue by year (own units)
2016 -23.3% before government "provisional remedies" (-10.8% after); 2017 6.0%; 2018 7.0%; 2019 5.3%; 2020 -21.8% (impairment
17,396 inside; -2.8% without); 2021 -3.9%; 2022 -15.2%; 2023 -17.1%; 2024 2.1%; 2025 4.8%; H1 2026 10.5% (190,654 / 1,822,538).

## Balance sheet ratios (nine year ends; ratios are unit-free)
see run file, Step 0.
