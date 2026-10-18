# ALFVY research notes 2026-10-17

Template copied before any fetch. Raw downloads are in `cache/` (gitignored); scripts in `scripts/`
(run with `python -I`); `owner_cash_output.txt` is the arithmetic output.

## Documents read (operator rule 4: document and date in place of an accession number)
| key | document | date | source |
|---|---|---|---|
| AR2025 | Alfa Laval Annual & Sustainability Report 2025 (statutory annual report; Management Report, Risk Management, Financial Statements and notes, ten-year overview) | contents determined 2026-03-03, signed Lund 2026-03-23, auditor's report (EY) 2026-03-24 | https://www.alfalaval.com/contentassets/126cf7ff2776412a9a91e39bcffef344/wkr0006.pdf |
| Q2 2026 | Alfa Laval AB (publ) Interim report 1 April - 30 June 2026 (not reviewed by the auditors) | decided 2026-07-20, published 2026-07-21 | https://mb.cision.com/Main/905/4376242/4199107.pdf (Cision release c4376242) |
| AR2024 | Annual & Sustainability Report 2024 | signed Lund 2025-03-28 | https://www.alfalaval.com/contentassets/5f2aa59fae5148ac81b8b2d644b84894/wkr0006.pdf |
| AR2023 | Annual & Sustainability Report 2023 | signed Lund 2024-03-17 | https://mb.cision.com/Main/905/3953677/2701033.pdf |
| AR2022 | Annual & Sustainability Report 2022 | signed Lund 2023-03-27 | https://www.alfalaval.com/globalassets/documents/investors/english/annual-reports/2022/annual-report-2022-april-11.pdf |
| AR2021 | Annual & Sustainability Report 2021 | signed Lund 2022-03-23 | https://www.alfalaval.com/contentassets/ddfe9be2f0d94fe0b13ff222d39501f1/wkr0006.pdf |
| AR2019 | Annual Report 2019 | signed Lund 2020-03-09 | https://www.alfalaval.com/contentassets/f9e134799d024d5eb31b17aa24e1b45f/wkr0006.pdf |
| AR2018 | Annual Report 2018 | signed Lund 2019-03-08 | https://www.alfalaval.com/contentassets/5455dd42a87548698c60230da2737f9e/wkr0006.pdf |
| AR2017 | Annual Report 2017 | signed Lund 2018-02-28 | https://www.alfalaval.com/contentassets/045c1844cf2f4a8d85b180369df71dcd/wkr0006.pdf |
| Q4 releases | "Alfa Laval (publ) Fourth quarter and full year" 2016 to 2025, alfalaval.com investor news pages | 2017-02 to 2026-02-03 | organic sales growth 2024 (6%) and 2025 (8%) footnoted "Organic change" |
| AR2020 | not found at a predictable URL; 2020 figures taken from the ten-year overview and the 2021 report's comparative column | | |

## Rivals' SEC filings
| rival named in AR2021/AR2023 product pages | SEC filer? | document |
|---|---|---|
| SPX FLOW (APV, Seital), US | yes until FY2021 (taken private 2022) | 10-K FY2019 0001641991-20-000004; FY2020 0001641991-21-000016; FY2021 0001641991-22-000015 (XBRL companyfacts, OperatingIncomeLoss and revenue) |
| SWEP (US-listed parent Dover; the report lists "SWEP (US)") | parent Dover files 10-K; SWEP is inside a segment | Dover 10-K FY2019 0000029905-20-000011; FY2022 0000029905-23-000008; FY2023 0000029905-24-000008; FY2025 0000029905-26-000009 (segment earnings tables) |
| GEA, Kelvion, Danfoss, Hisaka, Kangrim, Miura, Osaka, Saacke, Heatmaster, Mitsubishi Kakoki Kaisha, Pieralisi, Flottweg, Guinard/Andritz, Sulzer, Bardiani, Dockweiler, Fristam, Kieselmann, Marflex | no SEC annual report | flagged, not read |

## Market data
- ALFA (Nasdaq Stockholm) close SEK 576.40 on 2026-10-16, Yahoo chart API via `tools/sources.py price('ALFA.ST')`. AGGREGATOR, live quote only.
- Sovereign: Sveriges Riksbank SWEA series SEGVB10YC (Swedish government bond, 10-year), 3.119% on 2026-10-15 (api.riksbank.se/swea/v1/Observations/SEGVB10YC). The Riksbank publishes no longer government series (its list: 2, 5, 7, 10 years).
- Shares: 413,326,315, one class, no treasury shares (AR2025 Management Report, "Share-related information"; Q2 2026 average number of shares 413,326,315).

## Arithmetic notes
- The 2025 report restated the cash flow to a new structure (Note 39): lease principal moved from operating liabilities to financing, interest netted in financing. The ten-year overview carries the restated operating cash flow for every year. Lease principal for 2019-2024 = restated OCF less the OCF as first filed; 2025 is stated (503).
- Owner cash, all-equity basis, leases treated as an operating cost: restated OCF - capex + disposals of fixed assets - lease principal - lease interest. Net debt excludes lease liabilities to match (12,530 at 2026-06-30).
- Maintenance guess: depreciation of owned PPE and intangibles = (EBITDA - EBITA from the ten-year table) - right-of-use depreciation (leasing notes).
