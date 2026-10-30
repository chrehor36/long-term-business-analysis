# AHCO owner cash, recast from the filed cash-flow statements (USD millions)
Sources: 10-K FY2025 `0001628280-26-011213` (FY2023-25), 10-K FY2023 `0001628280-24-007254` (FY2021-23),
10-K FY2022 `0001628280-23-005590` (FY2020-22, unpaid equipment 2020, finance-lease equipment 2021-22),
10-Q Q2 2026 `0001628280-26-052646` (H1 2026). Script: `owner_cash.py`; output below.

Owner cash = OCF - stock pay - cash capex - increase in unpaid equipment at year end - equipment taken on finance
leases - distributions to the noncontrolling interest. Depreciation basis = OCF - stock pay - (D&A less intangible
amortization plus finance-lease right-of-use amortization) - NCI distributions. OCF is after cash interest and cash tax.
| FY | OCF | SBC | cash capex | change in unpaid equipment | finance-lease equipment | NCI distributions | OWNER CASH (capex basis) | depreciation basis | working-capital change inside OCF | cash acquisitions |
|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | 275.7 | 25.3 | 203.3 | 6.1 | 23.0 | 1.1 | **17.0** | 37.7 | -125.3 | 1620.3 |
| 2022 | 373.9 | 22.4 | 391.4 | 10.3 | 1.3 | 2.0 | **-53.6** | 38.3 | -76.8 | 19.0 |
| 2023 | 480.7 | 22.5 | 337.5 | 11.6 | 32.1 | 2.5 | **74.5** | 99.6 | +7.3 | 19.7 |
| 2024 | 541.8 | 14.9 | 306.1 | 20.3 | 17.9 | 5.6 | **177.2** | 167.2 | +6.9 | 9.5 |
| 2025 | 601.8 | 21.9 | 382.4 | 9.8 | 31.4 | 7.0 | **149.4** | 196.0 | +97.7 | 42.4 |

five-year mean, capex basis 72.9; depreciation basis 107.8; three-year (2023-25) capex basis 133.7; depreciation basis 154.3
capital put in 2021-25 (capex+unpaid change+finance-lease equipment) 1784.3; depreciation ex-amortization incl. finance-lease ROU 1610.0; cash acquisitions 1710.9; owner cash sum 364.4
H1 2026 owner cash, capex basis: -81.9; cash acquisitions H1 2026 127.4

shares, common plus preferred as converted 148.75
5yr capex  g=0.000  PV  1294.6  equity  1290.7  per share   8.68
5yr capex  g=0.017  PV  1481.2  equity  1477.4  per share   9.93
5yr dep    g=0.000  PV  1914.0  equity  1910.1  per share  12.84
5yr dep    g=0.017  PV  2190.0  equity  2186.1  per share  14.70
3yr capex  g=0.000  PV  2374.4  equity  2370.6  per share  15.94
3yr capex  g=0.017  PV  2716.8  equity  2713.0  per share  18.24
3yr dep    g=0.000  PV  2739.9  equity  2736.0  per share  18.39
3yr dep    g=0.017  PV  3134.9  equity  3131.0  per share  21.05
