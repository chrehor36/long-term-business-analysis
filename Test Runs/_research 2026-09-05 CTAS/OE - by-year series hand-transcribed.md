# CTAS owner-earnings inputs, hand-transcribed from filed consolidated statements of cash flows
All $000. Sources: FY2017 10-K (acc 0000723254-17-000020) for FY2015-17; FY2020 10-K
(0000723254-20-000025) for FY2018-20; FY2023 10-K (0000723254-23-000025) for FY2021-23;
FY2025 10-K (0000723254-25-000017) for FY2023-25 cross-check; FY2026 10-K
(0000723254-26-000028) for FY2024-26.

| FY | OCF | SBC | capex | dep | amort (intang + contract costs) |
|---|---|---|---|---|---|
| 2015 | 580,276 | 47,002 | 217,720 | 140,624 | 14,458 |
| 2016 | 465,845 | 79,293 | 275,385 | 149,691 | 15,588 |
| 2017 | 763,887 | 88,868 | 273,317 | 171,565 | 25,030 |
| 2018 | 964,160 | 112,835 | 271,699 | 215,476 | 63,940 |
| 2019 | 1,067,862 | 139,210 | 276,719 | 223,631 | 136,462 |
| 2020 | 1,291,483 | 115,435 | 230,289 | 235,905 | 143,148 |
| 2021 | 1,360,740 | 112,035 | 143,470 | 243,836 | 144,115 |
| 2022 | 1,537,625 | 109,308 | 240,672 | 249,376 | 150,325 |
| 2023 | 1,597,814 | 103,621 | 331,109 | 257,041 | 152,121 |
| 2024 | 2,068,500 | 116,986 | 409,469 | 280,866 | 176,004 |
| 2025 | 2,165,905 | 128,329 | 408,884 | 303,377 | 190,806 |
| 2026 | 2,276,280 | 128,076 | 395,105 | 318,637 | 194,209 |

CROSS-VINTAGE NOTE (found in transcription): FY2023 as filed in the FY2023 10-K shows OCF
1,597,814, depreciation 257,041, prepaid/contract-costs line (132,173), investing Other
(6,640). The FY2025 10-K restates FY2023 as OCF 1,586,228, depreciation 267,223,
prepaid/contract-costs (153,941), investing Other +420. A reclassification of ~$11.6M
(0.7% of OCF) between operating and investing plus ~$10.2M between depreciation captions.
Below threshold; noted, not smoothed. The FY2023-vintage numbers are used for FY2021-23
(as-first-filed), FY2026-vintage for FY2024-26.

## OE by year, capex end = OCF − SBC − total capex ($M)
2015: 315.6 | 2016: 111.2* | 2017: 401.7** | 2018: 579.6 | 2019: 651.9 | 2020: 945.8
2021: 1,105.2*** | 2022: 1,187.6 | 2023: 1,163.1 | 2024: 1,542.0 | 2025: 1,628.7 | 2026: 1,753.1

*FY2016 distorted DOWN: Shred-it partnership sale — $354.1M non-cash gain removed from OCF
but the cash tax on the gain paid inside OCF; also FY2016 revenue base excludes divested
Storage/Shredding.
**FY2017 distorted: G&K Services acquired for $2,102.4M (closed 2017-03-21); transaction
costs $31.4M + short-term financing fees $17.1M added back as non-cash but cash-paid.
***FY2021 flattered: COVID capex cut to $143.5M against $243.8M depreciation — the only
year in the series capex ran materially below depreciation.

## Windows (capex end, $M)
- 3-yr FY2024-26: 1,641.3
- 5-yr FY2022-26: 1,454.9  (run.py's 1,457 reproduced by hand)
- 10-yr FY2017-26: 1,095.9
- leave-two-out (drop FY2026 best + FY2017 worst): 1,100.5
- FY2026 alone (best year ever): 1,753.1

## (c) constructions for a rental model — the brief's [E3-44] direction question, answered
The garment/in-service investment is NOT in capex. It flows through OCF as a working
capital line ("Uniforms and other rental items in service": −137.6M FY2026, −93.6M FY2025,
−22.8M FY2024), amortized 18-30 months (garments) / 8-60 months (other rental items)
per Note 1. So OCF−SBC−capex ALREADY charges the full garment investment INCLUDING the
growth increment — [E2-23] constraint 3 satisfied by construction, conservative direction.
- (c) = total PP&E capex 395.1 (FY2026): includes growth capex (new plants; 484 facilities)
- (c) = depreciation alone 318.6: the [E3-44] default
- run.py's "D&A end" (513) DOUBLE-COUNTS: amortization of capitalized contract costs +
  acquired service contracts is added back in OCF while the current cash spend is already
  inside the working-capital lines (−174.0M FY2026 prepaid/contract-costs). INVALID as (c)
  for this filer — displayed only to show the screen's construction.
