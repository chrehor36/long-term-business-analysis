# BOUYF research notes (2026-10-12)

Run file copied from template before any fetch.

## Documents (AMF BDIF, https://bdif.amf-france.org/back/api/v1/documents/<path>)
- FY2025 URD (French), AMF D.26-0111, filed 2026-03-19, ESEF zip path 2026/D.26-0111/3028C813...zip
- FY2024 D.25-0147 (2025-03-26); FY2023 D.24-0153 (2024-03-22); FY2022 D.23-0133 (2023-04-21); FY2021 D.22-0139 (2022-03-24)
- FY2020 D.21-0139; FY2019 D.20-0157; FY2018 D.19-0176; FY2017 D.18-0158; FY2016 D.17-0201; FY2015 D.16-0143; FY2014 D.15-0164
- bouygues.com returns 403 to scripted and WebFetch requests; the English URD not obtained; the French filed text used, translations ours.
- xhtml-to-text: scripts/x2t.py. The FY2025 text loses the "ti" ligature in some sections (e.g. "opéraonnelles").

## Segment current operating profit (ROC / ROCA), EUR m, from note 17 of each URD
| | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 5y 21-25 |
| Colas | 254 | 440 | 468 | 542 | 552 | 586 | 2,588 |
| Bouygues Construction | 171 | 342 | 413 | 281 | 326 | 376 | 1,738 |
| Bouygues Immobilier | 12 | 43 | 37 | 28 | (51) | 20 | 77 |
| Equans | - | - | 130 (Q4 only) | 545 | 680 | 820 | 2,175 |
| Bouygues Telecom | 623 | 572 | 694 | 798 | 795 | 674 | 3,533 |
| TF1 | 190 | 343 | 322 | 287 | 297 | 252 | 1,501 |
| SA & other | (28) | (47) | (46) | (70) | (64) | (73) | (300) |
2021/2020 are ROC (ROCA defined from 2022). Parts total 21-25 = 11,612; BT 30.4% (largest), Colas 22.3%, Equans 18.7%, BC 15.0%, TF1 12.9%.
2022 BC includes Bouygues Energies & Services (moved to Equans in 2023).

## Group cash flow (EUR m)
| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
| CAF after net interest, lease interest, tax paid | 3,332 | 2,709 | 3,165 | 3,324 | 3,855 | 4,307 | 4,180 |
| Change in WC (+ = release) | (223) | 477 | 204 | (606) | 1,148 | 776 | 954 |
| Capex gross | (1,853) | (2,648) | (2,446) | (2,625) | (2,572) | (2,714) | (2,488) |
| Disposals of PP&E | 251 | 428 | 472 | 404 | 455 | 230 | 571 |
| Lease repayments | (351) | (372) | (361) | (441) | (559) | (555) | (455) |
| Acquisitions of consolidated activities | (225) | (930) | (382) | (6,269) | (51) | (1,090) | (165) |
| Disposals of consolidated activities | 1,183 | 646 | 1,046 | 281 | 246 | 25 | 172 |
| Dividends to parent holders | (631) | (646) | (647) | (680) | (671) | (718) | (755) |
Company "cash-flow libre" (CAF - net capex - lease repayments, before WC): 2022 662; 2023 1,179; 2024 1,268; 2025 1,808.

## Close (2026-10-12)
- Box: OUT at Q2 (Bouygues Telecom decides; castle open; field ordinary over the cycle; SFR consolidation not credited). Integrity facts recorded, not judged.
- Price EUR 40.30 (EN.PA close 2026-10-09, Yahoo, aggregator); BOUYF $43.90. Sovereign ECB 30y 3.778% (2026-10-08). Shares 387,402,574.
- COMPUTATION, NOT A CLEARANCE: range EUR 76.73-79.58 all-equity (equity-only 82.75-86.28); fair EUR 17.09 all-equity (equity-only 29.98); no case earns the floor at the price. Output: scripts/q7_computation_output.txt.
- Competitor sources: Orange URD FY2025 (AMF D.26-0217); Iliad URD FY2020 (D.21-0312), FY2012 (D.13-0318), H1 2025 report (copy on fs.siteor.com); Altice France Lux 3 FY2025 MD&A and statements (alticefrance.com).
- Citation check: scripts/check_run.py, 0 problems. check_framework PASS.
