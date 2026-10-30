# COMPETITOR ROW: Group 1 Automotive (GPI) against the five other US-listed franchised dealer groups

Built 2026-09-25. Fetch and compute only; no judgment is made in this file.

**Method.** Every figure is read off the filed 10-K primary document (EDGAR Archives, HTML stripped to text by `fetch.py`), not XBRL companyfacts. For each year the figure is taken from the newest 10-K that contains that year: 2023, 2024 and 2025 from the FY2025 10-K; 2021 and 2022 from the FY2023 10-K. USD millions throughout. CIKs were verified against the `name` field of each `data.sec.gov/submissions/CIK##########.json`:

| Ticker | CIK | Name in submissions JSON | FY2025 10-K (accession, filed, primary doc) | FY2023 10-K (accession, filed, primary doc) |
|---|---|---|---|---|
| AN | 350698 | AUTONATION, INC. | 0001628280-26-007800, 2026-02-12, an-20251231.htm | 0000350698-24-000021, 2024-02-16, an-20231231.htm |
| PAG | 1019849 | PENSKE AUTOMOTIVE GROUP, INC. | 0001628280-26-012830, 2026-02-27, pag-20251231.htm | 0001019849-24-000033, 2024-02-16, pag-20231231.htm |
| LAD | 1023128 | LITHIA MOTORS INC | 0001023128-26-000015, 2026-02-25, lad-20251231.htm | 0001023128-24-000032, 2024-02-23, lad-20231231.htm |
| ABG | 1144980 | ASBURY AUTOMOTIVE GROUP INC | 0001144980-26-000051, 2026-02-20, abg-20251231.htm | 0001144980-24-000076, 2024-02-29, abg-20231231.htm |
| SAH | 1043509 | SONIC AUTOMOTIVE INC | 0001628280-26-010570, 2026-02-23, sah-20251231.htm | 0001043509-24-000022, 2024-02-22, sah-20231231.htm |

All five FY2025 10-Ks are filed. Text copies: `AN_tenk_fy2025.txt`, `AN_tenk_fy2023.txt`, and the same pattern for PAG, LAD, ABG, SAH (this folder). Arithmetic: `build_row.py` (inputs transcribed by hand from the text files, then computed); `write_md.py` assembles this file.

**Definitions (CONVENTION, stated so the reader can reproduce them).**
- GM % = total gross profit / total revenues.
- OpM % as filed = operating income (income from operations) as printed / total revenues.
- OpM % ex-impairment = (operating income + impairment lines printed on the face of the income statement) / total revenues. Only face lines are added back, because that is the only like-for-like basis across all five; impairments buried inside other captions are listed in each peer's notes but NOT added back.
- P&S GM % = parts and service gross profit / parts and service revenue. Where the filing gives P&S cost of sales rather than P&S gross profit, gross profit = revenue less cost of sales (computed).
- 5-yr mean = simple arithmetic mean of the five annual percentages (not revenue-weighted).
- Floorplan interest is shown for reference; every peer reports it BELOW operating income, so neither OpM figure is after floorplan interest.

---
## 1. AutoNation (AN), CIK 350698

Source statement: "CONSOLIDATED STATEMENTS OF INCOME", FY2025 10-K (acc. 0001628280-26-007800) for 2023-2025; FY2023 10-K (acc. 0000350698-24-000021) for 2021-2022. P&S revenue, cost and gross profit are all printed on the face of the income statement.

| Year | Source 10-K | Revenue | Cost of sales | Gross profit | GP check (Rev - COS) | GM % | P&S revenue | P&S gross profit | P&S GM % | Operating income (as filed) | Impairment lines on face | OpM % as filed | OpM % ex-impairment | Floorplan interest |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | FY2023 | 25,844.0 | 20,891.4 | 4,952.6 | 4,952.6 OK | 19.16 | 3,706.6 | 1,672.7 | 45.13 | 1,902.8 | 0.0 | 7.36 | 7.36 | 25.7 |
| 2022 | FY2023 | 26,985.0 | 21,719.7 | 5,265.3 | 5,265.3 OK | 19.51 | 4,100.6 | 1,900.3 | 46.34 | 2,024.5 | 0.0 | 7.50 | 7.50 | 41.4 |
| 2023 | FY2025 | 26,948.9 | 21,817.4 | 5,131.5 | 5,131.5 OK | 19.04 | 4,533.7 | 2,139.3 | 47.19 | 1,651.9 | 0.0 | 6.13 | 6.13 | 144.7 |
| 2024 | FY2025 | 26,765.4 | 21,980.0 | 4,785.4 | 4,785.4 OK | 17.88 | 4,614.6 | 2,209.0 | 47.87 | 1,305.5 | 12.5 | 4.88 | 4.92 | 218.9 |
| 2025 | FY2025 | 27,631.4 | 22,682.9 | 4,948.5 | 4,948.5 OK | 17.91 | 4,835.4 | 2,355.1 | 48.71 | 1,239.9 | 159.0 | 4.49 | 5.06 | 188.8 |
| **5-yr mean** | | | | | | **18.70** | | | **47.05** | | | **6.07** | **6.20** | |

Operating income re-add, 2025: 4,948.5 + 9.8 (ANF income) - 3,362.2 - 251.4 - 65.3 - 93.7 + 54.2 (other income, net) = 1,239.9 (filed 1,239.9) OK.

Notes on the operating line:
- Face impairment lines: 2025 "Goodwill impairment" 65.3 and "Franchise rights impairment" 93.7 (sum 159.0); 2024 "Franchise rights impairment" 12.5. None in 2021-2023 on the face.
- Impairments NOT on the face, inside "Other income, net" (operating) and not added back above: cash-flow line "Other impairment charges" 37.9 (2025), 9.3 (2024), 5.2 (2023) (FY2025 10-K cash flow statement); FY2023 10-K Note 19 fair value table shows long-lived asset losses of 2.9 (2023) and 1.6 (2022), plus 2.3 other intangibles (2023). 2021 amount not disclosed in the FY2023 10-K.
- Gains inside operating income ("Other income, net" / "Other (income) expense, net"): cash-flow "Net gain related to business/property dispositions" 18.1 (2021), 16.3 (2022), 9.1 (2023), 55.1 (2024), 8.4 (2025).
- Presentation change: the FY2025 10-K shows "AUTONATION FINANCE INCOME (LOSS)" as a separate operating line (9.8 / (9.3) / (13.9) for 2025/2024/2023). The FY2023 10-K carried AutoNation Finance inside "Other (income) expense, net" (5.9 for 2023 there; FY2025 shows (8.0) other plus (13.9) ANF for the same year; 13.9 - 8.0 = 5.9, operating income unchanged at 1,651.9).

Franchised-dealership segment (company-defined "segment income" = operating income less floorplan interest expense; excludes "Corporate and other", which carries the impairments, unallocated corporate overhead, AutoNation USA used stores, collision, mobile service; AutoNation Finance shown separately). Source: MD&A segment reconciliation, FY2025 10-K (2023-2025) and FY2023 10-K (2021-2022).

| Year | Total Franchised Dealerships revenue | Segment income | Segment income / segment revenue % |
|---|---|---|---|
| 2021 | 24,988.3 | 2,147.9 | 8.60 |
| 2022 | 25,955.9 | 2,268.6 | 8.74 |
| 2023 | 25,720.5 | 1,886.9 | 7.34 |
| 2024 | 25,437.1 | 1,407.2 | 5.53 |
| 2025 | 26,231.3 | 1,497.4 | 5.71 |
| mean | | | 7.18 |

Caution: this segment margin is AFTER floorplan interest but BEFORE all unallocated corporate overhead ("Corporate and other" was (456.1) in 2025, (311.3) in 2024 per the FY2025 10-K), so it is not comparable to the other peers' segment figures, which bear their overhead.

Competition, FY2025 10-K Item 1 (verbatim):
- "Markets and Competition" section: "Our new vehicle store competitors have franchise agreements with the various vehicle manufacturers and, as such, generally have access to new vehicles on the same terms as we have."
- Same section: "In general, the vehicle manufacturers have designated marketing and sales areas within which only one franchised dealer of a given vehicle brand may operate."
- Same section: "However, to the extent that a market has multiple dealers of a particular vehicle brand, as most of our key markets do with respect to most vehicle brands we sell, we face significant intra-brand competition."
- Item 1 franchise agreements paragraph: "The franchise agreements grant the franchised automotive store a non-exclusive right to sell the manufacturer’s or distributor’s brand of vehicles and offer related parts and service within a specified market area."
- No sentence using the words "cost advantage" was found anywhere in the AN FY2025 10-K text (searched).

Structural differences: AutoNation Finance captive auto lender (operating line from FY2025 presentation); AutoNation USA used-vehicle stores, collision centers, parts distribution, mobile service and auctions inside "Corporate and other"; US only. Goodwill impairment 2025 relates to the Mobile Service reporting unit (FY2025 10-K Note 19).

---
## 2. Penske Automotive Group (PAG), CIK 1019849

Source statement: "CONSOLIDATED STATEMENTS OF INCOME", FY2025 10-K (acc. 0001628280-26-012830) for 2023-2025; FY2023 10-K (acc. 0001019849-24-000033) for 2021-2022. P&S is NOT split on the income statement (revenue and cost of sales are split by business line: retail automotive, retail commercial truck, commercial vehicle distribution and other). P&S figures in the table are the RETAIL AUTOMOTIVE service and parts revenue and service and parts gross profit from the MD&A "Retail Automotive Dealership Service and Parts Data" table (FY2025 10-K for 2023-2025; FY2023 10-K for 2021-2022).

| Year | Source 10-K | Revenue | Cost of sales | Gross profit | GP check (Rev - COS) | GM % | P&S revenue | P&S gross profit | P&S GM % | Operating income (as filed) | Impairment lines on face | OpM % as filed | OpM % ex-impairment | Floorplan interest |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | FY2023 | 25,554.7 | 21,113.9 | 4,440.8 | 4,440.8 OK | 17.38 | 2,165.6 | 1,307.3 | 60.37 | 1,356.4 | 0.0 | 5.31 | 5.31 | 26.2 |
| 2022 | FY2023 | 27,814.8 | 22,976.0 | 4,838.8 | 4,838.8 OK | 17.40 | 2,426.7 | 1,439.4 | 59.32 | 1,487.8 | 0.0 | 5.35 | 5.35 | 52.4 |
| 2023 | FY2025 (recast for PMG) | 30,916.5 | 25,769.1 | 5,147.4 | 5,147.4 OK | 16.65 | 2,863.2 | 1,679.3 | 58.65 | 1,409.3 | 40.7 | 4.56 | 4.69 | 135.3 |
| 2024 | FY2025 (recast for PMG) | 31,864.8 | 26,647.7 | 5,217.1 | 5,217.1 OK | 16.37 | 3,182.8 | 1,847.5 | 58.05 | 1,370.1 | 0.0 | 4.30 | 4.30 | 193.1 |
| 2025 | FY2025 | 31,808.5 | 26,591.5 | 5,217.0 | 5,217.0 OK | 16.40 | 3,377.9 | 1,973.8 | 58.43 | 1,280.7 | 0.0 | 4.03 | 4.03 | 170.6 |
| **5-yr mean** | | | | | | **16.84** | | | **58.96** | | | **4.71** | **4.73** | |

Operating income re-add, 2025: 5,217.0 - 3,764.0 - 172.3 = 1,280.7 (filed 1,280.7) OK.

SERIES BREAK (material): On November 19, 2025 PAG acquired Penske Motor Group (PMG) from a commonly controlled affiliate and, per the FY2025 10-K Note 1, "our consolidated financial statements and related notes have been retrospectively recast for all historical comparative periods presented to include the operations of PMG as if the entities had been combined since the beginning of the earliest period presented." So 2023-2025 include PMG; 2021-2022 (from the FY2023 10-K) do not. Effect on 2023: revenue 30,916.5 recast vs 29,527.4 originally; operating income 1,409.3 vs 1,351.5; retail automotive P&S revenue 2,863.2 vs 2,734.3. The FY2025 10-K gives PMG dealership revenue of $1.45bn, $1.41bn, $1.39bn and gross profit $208.7m, $203.6m, $213.5m for 2025, 2024, 2023.

Notes on the operating line:
- Face impairment: 2023 "Goodwill impairment charges" 40.7 (FY2025 10-K; captioned "Impairment charges" in the FY2023 10-K), Used Vehicle Dealerships International reporting unit.
- Gain on sale: 2025 "Gain on sale of dealership" 52.3 is printed BELOW operating income; not in OpM.
- "Equity in earnings of affiliates" (mostly the Penske Transportation Solutions stake: 192.3 / 197.6 / 289.8 for 2025/2024/2023 in the Non-Automotive Investments segment; 490.7 and 366.3 for 2022 and 2021) is BELOW operating income; not in OpM.
- Retail commercial truck P&S (Premier Truck Group), MD&A, not included in the P&S column: revenue 609.0 / 852.2 / 907.3 / 886.3 / 892.4 and gross profit 257.0 / 360.5 / 383.6 / 380.3 / 369.0 for 2021-2025 (margins 42.20 / 42.30 / 42.28 / 42.91 / 41.35 %, mean 42.21 %; computed).

Retail Automotive segment (dealership-only view). Source: segment note, FY2025 10-K (2023-2025; gross profit computed as revenue less cost of sales; SG&A computed as the sum of personnel, advertising, rent and related, and other expenses) and FY2023 10-K (2021-2022; gross profit and SG&A as printed). "Op ex-impairment" = gross profit less SG&A less depreciation (computed; the 2023 goodwill impairment of 40.7 sits in this segment and is excluded).

| Year | RA revenue | RA gross profit | RA GM % | RA SG&A | RA depreciation | RA op ex-impairment | RA OpM % ex-imp | RA floorplan | RA OpM % after floorplan |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | 22,513.3 | 3,870.2 | 17.19 | 2,607.3 | 108.7 | 1,154.2 | 5.13 | 23.9 | 5.02 |
| 2022 | 23,694.7 | 4,126.4 | 17.41 | 2,790.4 | 112.7 | 1,223.3 | 5.16 | 44.5 | 4.97 |
| 2023 | 26,598.2 | 4,389.8 | 16.50 | 3,101.0 | 127.4 | 1,161.4 | 4.37 | 118.2 | 3.92 |
| 2024 | 27,565.8 | 4,454.4 | 16.16 | 3,227.8 | 140.7 | 1,085.9 | 3.94 | 164.2 | 3.34 |
| 2025 | 27,474.6 | 4,482.4 | 16.31 | 3,314.7 | 150.1 | 1,017.6 | 3.70 | 145.9 | 3.17 |
| mean | | | 16.71 | | | | 4.46 | | 4.09 |

Check: 2023 RA segment income as filed 916.1 = 1,161.4 - 40.7 - 118.2 - 90.3 (other interest) + 3.9 (equity earnings) = 916.1. 2025: 1,017.6 - 145.9 - 76.8 + 0.6 + 52.3 (gain on sale) = 847.8 = filed. 2021: the same re-add gives 1,074.7 against a filed 1,046.6; the 28.1 gap is close to the 2021 consolidated "Debt redemption costs" (17.0) plus "Loss on investment" (11.4) = 28.4, which suggests those were charged to the segment; the remaining 0.3 is not explained by the filing.

Competition, FY2025 10-K Item 1 (verbatim):
- "Competition" section: "Our new vehicle dealership competitors have franchise agreements which give them access to new vehicles on the same terms as us."
- Item 1 franchise agreements paragraph: "In exchange for complying with these provisions and standards, we are granted the non-exclusive right to sell the manufacturer's or distributor's brand of vehicles and related parts and warranty services at our dealerships."
- No sentence using the words "cost advantage" was found in the PAG FY2025 10-K text (searched).

Structural differences: heavily international (FY2025 10-K revenue from external customers 2025: U.S. 19,578.8; U.K. 8,334.4; Other International 3,895.3); Premier Truck Group retail commercial truck dealerships (Freightliner, Western Star); Penske Australia commercial vehicle distribution (exclusive importer and distributor of Western Star, MAN, Dennis Eagle), which is a distribution business, not a dealership; equity-method stake in Penske Transportation Solutions below operating income; U.K. dealerships operate "without such local franchise law protection" (Item 1); some U.K. brands on agency models.

---
## 3. Lithia Motors (LAD), CIK 1023128

Source statement: "CONSOLIDATED STATEMENTS OF OPERATIONS", FY2025 10-K (acc. 0001023128-26-000015) for 2023-2025; FY2023 10-K (acc. 0001023128-24-000032) for 2021-2022. P&S revenue and cost of sales are on the face: captioned "Aftersales" in the FY2025 10-K and "Service, body and parts" in the FY2023 10-K; P&S gross profit computed as revenue less cost of sales.

| Year | Source 10-K | Revenue | Cost of sales | Gross profit | GP check (Rev - COS) | GM % | P&S revenue | P&S gross profit | P&S GM % | Operating income (as filed) | Impairment lines on face | OpM % as filed | OpM % ex-impairment | Floorplan interest |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | FY2023 | 22,831.7 | 18,572.7 | 4,259.0 | 4,259.0 OK | 18.65 | 2,110.9 | 1,110.5 | 52.61 | 1,662.5 | 1.9 | 7.28 | 7.29 | 22.3 |
| 2022 | FY2023 | 28,187.8 | 23,035.4 | 5,152.4 | 5,152.4 OK | 18.28 | 2,738.8 | 1,463.0 | 53.42 | 1,941.1 | 0.0 | 6.89 | 6.89 | 38.8 |
| 2023 | FY2025 (reclassified lines) | 31,042.3 | 25,813.4 | 5,228.9 | 5,228.9 OK | 16.84 | 3,206.8 | 1,759.1 | 54.86 | 1,692.4 | 0.0 | 5.45 | 5.45 | 150.9 |
| 2024 | FY2025 | 36,188.2 | 30,627.2 | 5,561.0 | 5,561.0 OK | 15.37 | 3,818.9 | 2,134.1 | 55.88 | 1,568.6 | 0.0 | 4.33 | 4.33 | 278.8 |
| 2025 | FY2025 | 37,634.9 | 31,901.9 | 5,733.0 | 5,733.0 OK | 15.23 | 4,086.8 | 2,357.1 | 57.68 | 1,594.7 | 5.8 | 4.24 | 4.25 | 228.2 |
| **5-yr mean** | | | | | | **16.88** | | | **54.89** | | | **5.64** | **5.64** | |

Operating income re-add, 2025: 5,733.0 + 74.6 (financing ops) - 5.8 - 3,944.7 - 262.4 = 1,594.7 (filed 1,594.7) OK.

Reclassification: the FY2025 10-K states "we combined used wholesale revenue with used retail revenue and now present these revenues collectively as Used vehicle revenue. In addition, we combined fleet revenue with new retail revenue and now present these revenues collectively as New vehicle revenue." The same filing says the reclassifications "had no impact on total revenue, gross profit, operating income, net income, or cash flows for any period presented." The 2023 P&S line nevertheless differs between filings: FY2025 "Aftersales" 3,206.8 revenue / 1,447.7 cost vs FY2023 "Service, body and parts" 3,197.1 / 1,445.7 (54.78% margin on the original basis vs 54.86% recast). The filing does not explain the 9.7 revenue difference; presumably part of the former "Fleet and other" line, but that is not stated.

Notes on the operating line:
- Face impairment: "Asset impairments" 1.9 (2021), 5.8 (2025).
- "Financing operations income (loss)" (Driveway Finance) is INSIDE operating income: 11.0 / (4.0) / (45.9) / 8.4 / 74.6 for 2021-2025.
- Gains inside operating income (in SG&A): "Net gain on disposal of stores" 66.0 (2022), 31.2 (2023), 8.2 (2024), 20.3 (2025); none in 2021 (cash flow statements and non-GAAP reconciliations). Also "Net loss (gain) on disposal of other assets" (2.5) 2021, (0.1) 2022, (3.8) 2023, (8.2) 2024, 9.3 2025 (cash flow; parentheses are gains).

Dealership-only view. LAD's reportable segments are Vehicle Operations and Financing Operations. The company's "Vehicle operations income" (segment note: 1,673.6 / 1,855.5 / 1,595.4 / 1,200.5 / 1,224.1 for 2021-2025) is after floorplan interest, before depreciation, and after internal corporate allocations ("internal rent expense, internal floor plan financing charges"), so it is not a clean comparator. A derived figure instead: operating income + face impairments - financing operations income (computed; includes all corporate overhead and D&A):

| Year | Revenue | Vehicle-ops op income ex-imp (derived) | % of revenue | Less floorplan | % after floorplan |
|---|---|---|---|---|---|
| 2021 | 22,831.7 | 1,653.4 | 7.24 | 22.3 | 7.14 |
| 2022 | 28,187.8 | 1,945.1 | 6.90 | 38.8 | 6.76 |
| 2023 | 31,042.3 | 1,738.3 | 5.60 | 150.9 | 5.11 |
| 2024 | 36,188.2 | 1,560.2 | 4.31 | 278.8 | 3.54 |
| 2025 | 37,634.9 | 1,525.9 | 4.05 | 228.2 | 3.45 |
| mean | | | 5.62 | | 5.20 |

Competition, FY2025 10-K (verbatim):
- Item 1 "Competition": "We do not have any cost advantage in purchasing new vehicles from manufacturers."
- Item 1 "Competition": "Vehicle manufacturers have designated specific marketing and sales areas within which only one dealer of a vehicle brand may operate."
- Item 1A Risk Factors: "Our franchise agreements do not grant us the exclusive right to sell a manufacturer’s product within a given geographic area and many of our competitors sell the same or similar makes of new and used vehicles that we offer in our markets at competitive prices, as well as competitive vehicles we may not sell. We do not have any cost advantage in purchasing new vehicles from manufacturers due to the volume of purchases or otherwise."
- Item 1A Risk Factors: "Our franchise agreements do not give us the exclusive right to a given geographic area."

Structural differences: Driveway Finance captive lender inside operating income; U.K. business (FY2025 10-K revenue from external customers: U.K. 1,904.6 in 2023, 6,788.5 in 2024, 6,914.1 in 2025, the step reflecting the Pendragon acquisition; the filing names the "Pendragon Group Pension Scheme" acquired January 2024); Canada (1,166.4 in 2025); recreational vehicle and motorcycle franchises inside Vehicle Operations; U.K. dealerships lack U.S.-style franchise law protection and several U.K. brands have moved to agency models (Item 1A). Very fast acquisition growth (revenue 22.8bn to 37.6bn over the window) makes the margin series partly a mix effect.

---
## 4. Asbury Automotive Group (ABG), CIK 1144980

Source statement: "CONSOLIDATED STATEMENTS OF INCOME", FY2025 10-K (acc. 0001144980-26-000051) for 2023-2025; FY2023 10-K (acc. 0001144980-24-000076) for 2021-2022. P&S revenue and cost of sales are on the face; P&S gross profit computed.

| Year | Source 10-K | Revenue | Cost of sales | Gross profit | GP check (Rev - COS) | GM % | P&S revenue | P&S gross profit | P&S GM % | Operating income (as filed) | Impairment lines on face | OpM % as filed | OpM % ex-impairment | Floorplan interest |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | FY2023 | 9,837.7 | 7,935.5 | 1,902.2 | 1,902.2 OK | 19.34 | 1,182.9 | 721.9 | 61.03 | 791.8 | 0.0 | 8.05 | 8.05 | 8.2 |
| 2022 | FY2023 | 15,433.8 | 12,333.3 | 3,100.6 | 3,100.5 OK | 20.09 | 2,074.2 | 1,152.6 | 55.57 | 1,272.6 | 0.0 | 8.25 | 8.25 | 8.4 |
| 2023 | FY2025 | 14,802.7 | 12,046.9 | 2,755.8 | 2,755.8 OK | 18.62 | 2,081.5 | 1,150.5 | 55.27 | 953.5 | 117.2 | 6.44 | 7.23 | 9.6 |
| 2024 | FY2025 | 17,188.6 | 14,240.0 | 2,948.6 | 2,948.6 OK | 17.15 | 2,354.7 | 1,351.2 | 57.38 | 835.6 | 149.5 | 4.86 | 5.73 | 89.9 |
| 2025 | FY2025 | 17,999.0 | 14,927.3 | 3,071.7 | 3,071.7 OK | 17.07 | 2,506.8 | 1,472.5 | 58.74 | 860.6 | 141.0 | 4.78 | 5.56 | 91.2 |
| **5-yr mean** | | | | | | **18.45** | | | **57.60** | | | **6.48** | **6.96** | |

Operating income re-add, 2025: 3,071.7 - 1,987.6 - 82.4 - 141.0 = 860.7 (filed 860.6) OK.

Notes on the operating line:
- Face impairment: "Asset impairments" 117.2 (2023), 149.5 (2024), 141.0 (2025). FY2025 10-K MD&A: "As a result, we recognized a $115.0 million pre-tax non-cash impairment charge related to our franchise rights intangible assets during the year ended December 31, 2025." and "We also recorded a franchise rights impairment charge of $26.0 million during the year ended December 31, 2025 related to dealerships that met the assets held for sale criteria during 2025." (115.0 + 26.0 = 141.0, the face line.)
- "Other operating income, net" (5.4) 2021, (4.4) 2022 is inside operating income (a credit).
- "Gain on dealership divestitures, net" 8.0 / 207.1 / 13.5 / 8.6 / 80.2 (2021-2025) is printed BELOW income from operations; not in OpM.
- Floor plan interest was very low in 2021-2023 (8.2 / 8.4 / 9.6) because cash was parked in floor plan offset accounts: FY2023 10-K: "Floor plan interest expense increased by $1.3 million (15%) to $9.6 million during 2023 compared to $8.4 million during 2022 due to less cash held in the floor plan offset account in December 2023 as a result of funding the Koons acquisition." The offset effectively moves the cost of carrying inventory into forgone interest income and other interest, so ABG's floorplan line is not comparable to peers for those years.
- 2021 is not like-for-like: the Larry H. Miller dealerships and TCA were acquired December 17, 2021 (FY2023 10-K), so 2021 revenue (9,837.7) is essentially pre-LHM Asbury.

Dealerships segment. Two reportable segments: Dealerships and TCA (Total Care Auto, the F&I product provider/insurer acquired with LHM). Source: segment note, FY2025 10-K (2023-2025) and FY2023 10-K (2022). Company-defined "Segment operating income" is "derived from GAAP operating income, adjusted to exclude the effects of asset impairments and to include floor plan interest expense." Revenue includes intersegment revenue.

| Year | Dealerships revenue (incl. intersegment) | Dealerships gross profit | GM % | Segment operating income (ex-impairment, after floorplan) | % of revenue |
|---|---|---|---|---|---|
| 2021 | not given (no segment table for 2021 in FY2023 10-K) | | | | |
| 2022 | 15,341.1 | 3,036.0 | 19.79 | 1,173.1 (computed: 3,036.0 - 1,786.3 SG&A - 68.2 D&A - 8.4 floorplan) | 7.65 |
| 2023 | 14,699.0 | 2,671.1 | 18.17 | 955.9 | 6.50 |
| 2024 | 17,107.5 | 2,882.5 (computed) | 16.85 | 816.7 | 4.77 |
| 2025 | 17,944.8 | 3,033.1 (computed) | 16.90 | 858.6 | 4.78 |
| mean (4 yrs) | | | 17.93 | | 5.93 |

Check: 2023 from the FY2023 10-K segment table, 2,671.1 - 1,638.5 - 67.1 - 9.6 = 955.9, equal to the 2023 "Segment operating income" printed in the FY2025 10-K.

Competition, FY2025 10-K (verbatim):
- Item 1 "Competition": "Our new vehicle store competitors also have franchise agreements with the various vehicle manufacturers, and as such, generally obtain new vehicle inventory from vehicle manufacturers on the same terms as us. The franchise agreements grant the franchised dealership a non-exclusive right to sell the manufacturer's (or distributor's) brand of vehicles and offer related parts and service within a specified market area."
- Item 1 "Competition": "State automotive franchise laws restrict competitors from relocating their stores or establishing new stores of a particular vehicle brand within a specified area that is served by our dealership of the same vehicle brand."
- Item 1A Risk Factors: "We do not have any cost advantage over other retailers in purchasing new vehicles from manufacturers. We typically rely on our advertising, merchandising, sales expertise, service reputation, strong local branding and dealership location to sell new vehicles. Because our dealer agreements only grant us a non-exclusive right to sell a manufacturer’s product within a specified market area, our revenues, gross profit and overall profitability may be materially adversely affected if competing dealerships expand their market share."

Structural differences: TCA (vehicle service contract and F&I product provider) captures product profit that other dealers cede to third parties; intersegment F&I and P&S eliminations; step acquisitions (LHM Dec 2021, Koons 2023, Herb Chambers July 2025) make the series partly mix; floor plan offset accounts depress reported floorplan interest (above); U.S. only.

---
## 5. Sonic Automotive (SAH), CIK 1043509

Source statement: "CONSOLIDATED STATEMENTS OF OPERATIONS", FY2025 10-K (acc. 0001628280-26-010570) for 2023-2025; FY2023 10-K (acc. 0001043509-24-000022) for 2021-2022. P&S ("Parts, service and collision repair") revenue and cost of sales are on the face; P&S gross profit computed. The FY2025 statement footnotes: "(1) Cost of sales is exclusive of depreciation and amortization shown separately below."

| Year | Source 10-K | Revenue | Cost of sales | Gross profit | GP check (Rev - COS) | GM % | P&S revenue | P&S gross profit | P&S GM % | Operating income (as filed) | Impairment lines on face | OpM % as filed | OpM % ex-impairment | Floorplan interest |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | FY2023 | 12,396.4 | 10,482.1 | 1,914.3 | 1,914.3 OK | 15.44 | 1,340.4 | 672.9 | 50.20 | 538.4 | 0.1 | 4.34 | 4.34 | 16.7 |
| 2022 | FY2023 | 14,001.1 | 11,684.1 | 2,317.0 | 2,317.0 OK | 16.55 | 1,599.7 | 792.5 | 49.54 | 314.0 | 320.4 | 2.24 | 4.53 | 34.3 |
| 2023 | FY2025 | 14,372.4 | 12,126.7 | 2,245.7 | 2,245.7 OK | 15.63 | 1,759.5 | 874.0 | 49.67 | 423.6 | 79.3 | 2.95 | 3.50 | 67.2 |
| 2024 | FY2025 | 14,224.3 | 12,031.5 | 2,192.8 | 2,192.8 OK | 15.42 | 1,846.5 | 928.9 | 50.31 | 461.5 | 3.9 | 3.24 | 3.27 | 86.9 |
| 2025 | FY2025 | 15,153.6 | 12,770.7 | 2,382.9 | 2,382.9 OK | 15.72 | 2,019.1 | 1,029.1 | 50.97 | 367.5 | 173.8 | 2.43 | 3.57 | 84.7 |
| **5-yr mean** | | | | | | **15.75** | | | **50.14** | | | **3.04** | **3.84** | |

Operating income re-add, 2025: 2,382.9 - 1,678.2 - 173.8 - 163.4 = 367.5 (filed 367.5) OK.

Notes on the operating line:
- Face impairment: "Impairment charges" 0.1 (2021), 320.4 (2022), 79.3 (2023), 3.9 (2024), 173.8 (2025). Segment split (FY2023 10-K): 2022 Franchised Dealerships 115.5 / EchoPark 204.9; 2023 Franchised 1.0 / EchoPark 78.3. FY2025 10-K: 2025 includes approximately 165.9 of franchise asset impairment in the Franchised Dealerships Segment.
- Gains/losses inside operating income (in SG&A): cash-flow "Gain on disposal of dealerships and property and equipment" (3.3) 2021, (10.8) 2022, (18.4) 2023 gains; 0.6 2024, 6.4 2025 losses (parentheses are gains in the cash flow add-back).
- 2021 "Other income (expense), net" (15.5) is below operating income.

Franchised Dealerships segment. Three reportable segments: Franchised Dealerships, EchoPark (used-only stores), Powersports (from 2022). Company "Segment income" is "income (loss) before taxes and impairment charges" (i.e., after floorplan and other interest). Source: segment note, FY2025 10-K (2023-2025) and FY2023 10-K (2021-2022). Derived column adds back the segment's "Interest expense, other, net" (46.3 / 85.0 / 109.7 / 112.7 / 105.9) to give a figure after floorplan interest but before other interest.

| Year | Franchised segment revenue | Segment income (as filed) | + other interest = after-floorplan op (derived) | % of revenue | Segment floorplan | % before floorplan |
|---|---|---|---|---|---|---|
| 2021 | 10,051.1 | 530.3 | 576.6 | 5.74 | 11.8 | 5.85 |
| 2022 | 11,484.6 | 641.6 | 726.6 | 6.33 | 23.6 | 6.53 |
| 2023 | 11,774.8 | 448.0 | 557.7 | 4.74 | 49.2 | 5.15 |
| 2024 | 11,939.2 | 257.6 | 370.3 | 3.10 | 70.6 | 3.69 |
| 2025 | 12,879.1 | 316.1 | 422.0 | 3.28 | 72.0 | 3.84 |
| mean | | | | 4.64 | | 5.01 |

The derived figure still contains the segment's small "Other income (expense), net" (0.2 / (0.5) / 0.1 for 2023-2025); for 2021-2022 the FY2023 10-K does not split that line by segment. 2025 segment income includes "approximately $ 40.0 million of pre-tax benefit from cyber insurance proceeds related to the CDK outage" (FY2025 10-K segment note footnote). Franchised segment gross margin 2023-2025 (segment gross profit 2,033.6 / 1,941.2 / 2,095.2): 17.27 / 16.26 / 16.27 %.

Competition, FY2025 10-K (verbatim). The Item 1 "Competition" section contains no cost-advantage or exclusivity sentence; both appear in Item 1A Risk Factors:
- Item 1A, under "Competition among automotive retailers and the use of the internet in automotive retail may reduce our profit margins on vehicle sales and related businesses.": "We do not have any cost advantage in purchasing new vehicles from manufacturers due to economies of scale or otherwise."
- Item 1A: "Our franchise and dealer agreements do not grant us the exclusive right to sell a manufacturer’s product within a given geographic area. Our revenues or profitability could be materially adversely affected if any of our manufacturers awards franchises to others in the same markets where we operate or if existing franchised dealers increase their market share in our markets."

Structural differences: EchoPark used-vehicle stores carried large losses and impairments (segment income (72.0) 2021, (133.9) 2022, (132.5) 2023, 3.5 2024, 28.1 2025), which depress consolidated OpM; Powersports segment (small); U.S. only; cost of sales stated exclusive of D&A.

---
## SUMMARY (consolidated, as filed; percentages of total revenues; 5-yr simple means)

| Company | GM% 2021 | 2022 | 2023 | 2024 | 2025 | GM mean | OpM% 2021 | 2022 | 2023 | 2024 | 2025 | OpM mean | OpM ex-impairments mean | P&S GM% mean | Accessions |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AN | 19.16 | 19.51 | 19.04 | 17.88 | 17.91 | 18.70 | 7.36 | 7.50 | 6.13 | 4.88 | 4.49 | 6.07 | 6.20 | 47.05 | FY2025 0001628280-26-007800; FY2023 0000350698-24-000021 |
| PAG | 17.38 | 17.40 | 16.65 | 16.37 | 16.40 | 16.84 | 5.31 | 5.35 | 4.56 | 4.30 | 4.03 | 4.71 | 4.73 | 58.96 | FY2025 0001628280-26-012830; FY2023 0001019849-24-000033 |
| LAD | 18.65 | 18.28 | 16.84 | 15.37 | 15.23 | 16.88 | 7.28 | 6.89 | 5.45 | 4.33 | 4.24 | 5.64 | 5.64 | 54.89 | FY2025 0001023128-26-000015; FY2023 0001023128-24-000032 |
| ABG | 19.34 | 20.09 | 18.62 | 17.15 | 17.07 | 18.45 | 8.05 | 8.25 | 6.44 | 4.86 | 4.78 | 6.48 | 6.96 | 57.60 | FY2025 0001144980-26-000051; FY2023 0001144980-24-000076 |
| SAH | 15.44 | 16.55 | 15.63 | 15.42 | 15.72 | 15.75 | 4.34 | 2.24 | 2.95 | 3.24 | 2.43 | 3.04 | 3.84 | 50.14 | FY2025 0001628280-26-010570; FY2023 0001043509-24-000022 |

P&S GM% for PAG is retail automotive only (MD&A); PAG commercial truck P&S mean is 42.21 %. PAG 2021-2022 exclude PMG, 2023-2025 include it.

## SUMMARY (dealership-only views, where the filing allows; definitions differ, read the per-peer notes)

| Company | Dealer view used | Years | Mean margin | What it is after / before |
|---|---|---|---|---|
| AN | Franchised Dealerships segment income / segment revenue | 2021-2025 | 7.18 % | after floorplan; BEFORE unallocated corporate overhead (not comparable) |
| PAG | Retail Automotive: GP - SG&A - depreciation (computed) | 2021-2025 | 4.46 % (4.09 % after RA floorplan) | ex-impairment, before floorplan; 2021-22 not recast for PMG |
| LAD | Operating income + impairments - financing operations income (computed) | 2021-2025 | 5.62 % (5.20 % after floorplan) | includes all corporate overhead |
| ABG | Dealerships segment operating income / segment revenue | 2022-2025 | 5.93 % | ex-impairment, after floorplan (floorplan understated 2022-23 by offset accounts) |
| SAH | Franchised Dealerships segment income + segment other interest (computed) | 2021-2025 | 4.64 % (5.01 % before segment floorplan) | ex-impairment, after floorplan |

## Comparability notes (all peers)

- PAG 2021-2022 exclude PMG; 2023-2025 include it (common-control recast). Series break.
- LAD 2023 P&S line differs slightly between the FY2023 and FY2025 10-Ks (reclassification; 3,197.1 vs 3,206.8 revenue).
- AN moved AutoNation Finance to its own operating line in the FY2025 10-K; operating income totals are unchanged.
- Impairments inside other captions (AN "Other income, net") are NOT added back in "OpM ex-impairment"; AN's are listed in its section (37.9 in 2025, 9.3 in 2024, 5.2 in 2023).
- Gains on dealership sales sit INSIDE operating income for AN (other income), LAD (SG&A) and SAH (SG&A), and BELOW it for PAG and ABG. Not adjusted in any margin above; amounts are listed per peer.
- Captive finance inside operating income: AN (AutoNation Finance) and LAD (Financing operations). ABG's TCA sits inside consolidated gross profit.
- Non-dealer businesses inside consolidated figures: PAG commercial truck dealerships and Australian distribution; SAH EchoPark and Powersports; AN AutoNation USA, collision, mobile service; LAD RV and motorcycle franchises; ABG TCA.
- International: PAG (U.K. 8,334.4 of 31,808.5 revenue in 2025, plus Other International 3,895.3); LAD (U.K. 6,914.1 and Canada 1,166.4 of 37,634.9 in 2025). AN, ABG, SAH are U.S. only.
- Means are simple means of annual ratios; 2021-2022 were the post-pandemic inventory-shortage peak for all five, so any five-year mean ending 2025 carries two peak years.

## Cost-advantage and exclusivity sentences (FY2025 10-Ks), side by side

| Company | Cost-advantage sentence | Exclusive-territory sentence | Where |
|---|---|---|---|
| GPI (reference, supplied in the brief) | "We do not have any cost advantage in purchasing new vehicles from vehicle manufacturers, and our current franchise agreements do not grant us the exclusive right to sell a manufacturer's product within a given geographic area." | (same sentence) | not re-verified here |
| AN | none found; closest: "Our new vehicle store competitors have franchise agreements with the various vehicle manufacturers and, as such, generally have access to new vehicles on the same terms as we have." | "The franchise agreements grant the franchised automotive store a non-exclusive right to sell the manufacturer’s or distributor’s brand of vehicles and offer related parts and service within a specified market area." | Item 1 |
| PAG | none found; closest: "Our new vehicle dealership competitors have franchise agreements which give them access to new vehicles on the same terms as us." | "In exchange for complying with these provisions and standards, we are granted the non-exclusive right to sell the manufacturer's or distributor's brand of vehicles and related parts and warranty services at our dealerships." | Item 1 |
| LAD | "We do not have any cost advantage in purchasing new vehicles from manufacturers." (Item 1); "We do not have any cost advantage in purchasing new vehicles from manufacturers due to the volume of purchases or otherwise." (Item 1A) | "Our franchise agreements do not grant us the exclusive right to sell a manufacturer’s product within a given geographic area ..." (Item 1A); "Our franchise agreements do not give us the exclusive right to a given geographic area." (Item 1A) | Item 1 and 1A |
| ABG | "We do not have any cost advantage over other retailers in purchasing new vehicles from manufacturers." (Item 1A); "...generally obtain new vehicle inventory from vehicle manufacturers on the same terms as us." (Item 1) | "The franchise agreements grant the franchised dealership a non-exclusive right to sell the manufacturer's (or distributor's) brand of vehicles and offer related parts and service within a specified market area." (Item 1) | Item 1 and 1A |
| SAH | "We do not have any cost advantage in purchasing new vehicles from manufacturers due to economies of scale or otherwise." | "Our franchise and dealer agreements do not grant us the exclusive right to sell a manufacturer’s product within a given geographic area." | Item 1A only (Item 1 "Competition" is silent) |

Formatting: the stripped text renders curly apostrophes (’) and straight apostrophes (') exactly as the filers used them; both kinds are preserved above as extracted. No OCR is involved (HTML primary documents). The "..." in the LAD row marks an omission by this file, the full sentence is in section 3.

## What could not be obtained

- AN: the 2021 amount of impairments embedded in "Other (income) expense, net" is not disclosed in the FY2023 10-K (it would be in the FY2021 or FY2022 10-K, not fetched).
- PAG: P&S cost of sales is not printed; only P&S revenue and gross profit (MD&A). 2021-2022 are not available on the PMG-recast basis in any filing fetched (the FY2024 10-K, acc. 0001019849-25-000022, would give 2022 on the pre-PMG basis only, since the recast came in FY2025).
- ABG: no Dealerships segment table for 2021 in the FY2023 10-K.
- SAH: segment split of "Other income (expense), net" for 2021-2022 not given.
- LAD: the filing does not explain the 9.7 difference in 2023 P&S revenue between its two presentations.
