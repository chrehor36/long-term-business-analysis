# EQIX Q2 competitor row: evidence table (peers)

Built 2026-09-18. **Fetch and arithmetic only. No conclusion is drawn here on whether Equinix is a franchise; that is the caller's judgment.** Every figure is transcribed from a filed SEC document named by accession number. Ratios marked *computed* are arithmetic on those figures (script: `peers/compute.py`). Raw downloads are in this folder, stripped to text, with the filer and form in the filename.

## Source register (accession numbers)

| Code | Filer / document | Accession |
|---|---|---|
| EQ25 | Equinix 10-K FY2025 (on disk `../10K_FY2025.txt`) | 0001101239-26-000032 |
| EQ18 | Equinix 10-K FY2018 (on disk `../10K_FY2018.txt`) | 0001628280-19-001771 |
| D25 / D24 / D23 / D22 / D21 | Digital Realty 10-K FY2025 / FY2024 / FY2023 / FY2022 / FY2021 | 0001104659-26-015365 / 0001558370-25-001424 / 0001558370-24-001575 / 0001558370-23-002087 / 0001558370-22-002195 |
| DQ226 | Digital Realty 10-Q Q2 2026 | 0001104659-26-089296 |
| DS25 / DS24 / DS23 / DS22 / DS21 | DLR 8-K Ex-99.1 (earnings release + financial supplement) for Q4 2025 / Q4 2024 / Q4 2023 / Q4 2022 / Q4 2021 | 0001104659-26-010887 / 0001558370-25-000945 / 0001558370-24-001242 / 0001558370-23-001449 / 0001558370-22-001343 |
| DS226 | DLR 8-K Ex-99.1 Q2 2026 | 0001104659-26-086270 |
| A25 / A24 / A23 | American Tower 10-K FY2025 / FY2024 / FY2023 | 0001053507-26-000035 / 0001053507-25-000025 / 0001053507-24-000011 |
| AQ226 | American Tower 10-Q Q2 2026 | 0001053507-26-000133 |
| I25 / I24 / I23 / I22 | Iron Mountain 10-K FY2025 / FY2024 / FY2023 / FY2022 | 0001020569-26-000013 / 0001020569-25-000040 / 0001020569-24-000040 / 0001020569-23-000043 |
| IQ226 | Iron Mountain 10-Q Q2 2026 | 0001020569-26-000071 |
| C22 | Cyxtera 10-K FY2022 (last 10-K) | 0001794905-23-000010 |
| CQ123 | Cyxtera 10-Q Q1 2023 (last 10-Q) | 0001794905-23-000048 |
| C8K | Cyxtera 8-K 2023-06-05, Item 1.03 Bankruptcy (+ Ex-99.1) | 0001193125-23-160378 |
| CONE21 | CyrusOne 10-K FY2021 (last) | 0001553023-22-000009 |
| SW21 | Switch 10-K FY2021 (last) | 0001710583-22-000009 |
| COR20 | CoreSite 10-K FY2020 (last) | 0001558370-21-000757 |
| QTS20 | QTS Realty Trust 10-K FY2020 (last; CIK 1577368) | 0001628280-21-003456 |
| ODIT25 | Blue Owl Digital Infrastructure Trust 10-K FY2025 | 0002069692-26-000016 |
| DB21 / DB25 | DigitalBridge 10-K FY2021 / FY2025 | 0001679688-22-000008 / 0001679688-26-000021 |

**Cross-check against the filed statement (protocol rule 4):** DLR FY2025 total operating revenues $6,112,692K in the D25 Consolidated Income Statement = XBRL `Revenues` 6,112.7M. Equinix FY2025 income from operations read from the EQ25 Consolidated Statement of Operations: **$1,848M** (FY2024 $1,328M, FY2023 $1,443M). The caller's "about $1.85bn" is confirmed.

---

## A. Revenue and annual growth ($M)

| Company | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | H1 2026 vs H1 2025 | Source / definition note |
|---|---|---|---|---|---|---|---|
| **Equinix** (caller) | n/a | n/a | 8,188 | 8,748 (+6.8%) | 9,217 (+5.4%) | n/a | EQ25 |
| **Digital Realty** | 4,427.9 (+13.4%) | 4,691.8 (+6.0%) | 5,477.1 (+16.7%) | 5,555.0 (+1.4%) | 6,112.7 (+10.0%) | 3,559.2 vs 2,900.8 (+22.7%) | D21-D25 income statements; H1 from DQ226. FY2020 base 3,903.6 (XBRL, acc 0001558370-21-002191). H1 2026 includes fee income and other $284.4M vs $56.6M (Q2 2026 alone $249.4M, +596.9%), so the H1 growth is not all rental. |
| **AMT Data Centers segment** | 23.2 (CoreSite closed 28 Dec 2021; not a growth year) | 766.6 | 834.7 (+8.9%) | 924.8 (+10.8%) | 1,053.1 (+13.9%) | 586.0 vs 506.0 (+15.8%) | A23 segment note (2021-2023), A25 segment note (2023-2025), AQ226. US only; 30 facilities, 3.7M NRSF (A25). |
| **IRM Global Data Center segment** | 326.9 | 401.1 (+22.7%) | 495.0 (+23.4%) | 620.0 (+25.3%) | 803.4 (+29.6%) | 517.6 vs 362.6 (+42.7%) | I22, I23, I24, I25 MD&A segment tables; IQ226. FY2021 growth not computed (FY2020 base not fetched). Includes pass-through power. |
| **Cyxtera** | 703.7 (+1.9%) | 746.0 (+6.0%) | Ch. 11 filed 4 Jun 2023 | n/a | n/a | n/a | C22 statement of operations (FY2020 690.5). |
| CyrusOne (STALE) | 1,205.7 (+16.7%) | taken private 2022 | | | | | CONE21 (FY2020 1,033.5) |
| Switch (STALE) | 592.0 (+15.7%, of which $27.4M from Data Foundry acquisition) | taken private Dec 2022 | | | | | SW21 (FY2020 511.5) |
| CoreSite (STALE, FY2020) | FY2020: 606.8 (+6.0% on 572.7) | acquired by AMT Dec 2021 | | | | | COR20 statement of operations |
| QTS (STALE, FY2020) | FY2020: 539.4 (+12.2% on 480.8) | taken private Aug 2021 | | | | | QTS20 |

## B. Interconnection revenue and counts

| Company | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | H1 2026 | Definition note / source |
|---|---|---|---|---|---|---|---|
| **Equinix** (caller) | | | 1,395 (17.0%) | 1,519 (17.4%) | 1,655 (18.0%) | | 500,000+ interconnections at end FY2025 (caller) |
| **Digital Realty** "Interconnection and other" | 360.5 (8.1%) | 379.6 (8.1%) | 419.9 (7.7%) | 442.6 (8.0%) | 478.7 (7.8%) | 254.7 (7.2%) vs 234.9 (8.1%) H1 2025 | DS21-DS25, DS226 supplement income statement. **Not in the 10-K**: the D21-D25 10-Ks do not break interconnection out. Line is "and other", so it overstates pure interconnection. No cross-connect COUNT found in any DLR document fetched. FY2020 327.4. |
| **AMT Data Centers** "Non-lease property revenue" | n/a | n/a | 116.5 (14.0%) | 132.7 (14.3%) | 151.5 (14.4%) | 83.4 (14.2%) vs 72.7 (14.4%) | A25 revenue disaggregation note. A25: "Non-lease property revenue also includes revenue generated from interconnection offerings in the Company's data center facilities." So it is interconnection plus other non-lease items, not interconnection alone. Interconnection **increments** stated in MD&A: +$9.6M (2023, A23), +$11.9M (2024, A24), +$16.2M (2025, A25), +$7.9M (H1 2026, AQ226). No count. |
| **IRM Global Data Center** | not disclosed | | | | | | No interconnection revenue or count in I22-I25. |
| **Cyxtera** | not disclosed as $ | "+$6.3 million" in 2022 | | | | | C22: "Interconnection revenue increased by $6.3 million compared to the prior year, as a result of rate increases in the year." Count: "more than ... 40,000 cross-connects" (C22 Item 1). |
| CoreSite (STALE) | FY2020: 84.1 (13.9%); FY2019: 75.8 (13.2%); +11.0% | | | | | | COR20 MD&A table |
| Switch (STALE) | "Connectivity" 105.8 (17.9%); FY2020 91.9 (18.0%) | | | | | | SW21. Connectivity = "cross-connects, broadband services and external connectivity", broader than interconnection. |
| CyrusOne (STALE) | "$3.6 million increase in interconnection revenue" (2021) | | | | | | CONE21; no $ level found. |
| QTS (STALE) | not disclosed | | | | | | QTS20 |

## C. Renewal pricing and churn

### C1. Digital Realty renewal rent change, full year (LTM at Q4)

GAAP basis per D10-K "Rental Rate Changes" column (which the supplement shows is the GAAP number; D10-K footnote defines the rate as "total cash base rent divided by the total number of years in the contract", i.e. a straight-lined rate). Cash and total from DS supplements.

| Year | 0-1 MW GAAP (10-K) | >1 MW GAAP (10-K) | Other GAAP (10-K) | **Total GAAP** (supp.) | 0-1 MW cash | >1 MW cash | **Total cash** (supp.) | Sources |
|---|---|---|---|---|---|---|---|---|
| 2021 | 1.8% | (6.6)% | 12.3% | (0.4)% | 1.0% | (11.9)% | **(3.1)%** | D21, DS21 |
| 2022 | 3.6% | 0.5% | 19.7% | 3.5% | 3.4% | (3.3)% | **1.8%** | D22, DS22 |
| 2023 | 5.7% | 21.0% | 55.5% | 10.5% | 4.9% | 9.2% | **6.8%** | D23, DS23 |
| 2024 | 5.0% | 27.4% | 47.1% (supp. 47.0%) | 14.3% | 4.2% | 14.4% | **9.0%** | D24, DS24 |
| 2025 | 4.6% | 27.0% | 43.0% | 10.5% | 4.1% | 12.3% | **6.7%** | D25, DS25 |
| H1 2026 (YTD, DLR share, new per-kW layout) | 5.3% | 65.6% | Other 21.9% | Data Center total 19.7% | 4.7% | 48.7% | **Data Center total 15.9%** | DS226 (10-Q DQ226 gives per-kW rates: 0-1 MW $302 to $318; >1 MW $150 to $248) |

### C2. Digital Realty churn (LTM at Q4; "recurring revenue lost during the period due to leases terminated or not renewed, divided by recurring revenue at the beginning of the period")

| Year | 0-1 MW | >1 MW | Other | **Total** | Source |
|---|---|---|---|---|---|
| 2021 | 9.2% | 5.9% | 5.1% | **7.2%** | DS21 |
| 2022 | 7.1% | 6.6% | 2.0% | **6.5%** | DS22 |
| 2023 | 6.3% | 3.2% | 6.7% | **4.8%** | DS23 |
| 2024 | 7.8% | 4.9% | 5.6% | **6.2%** | DS24 |
| 2025 | 8.5% | 3.2% | 3.4% | **5.4%** | DS25 |
| H1 2026 YTD / LTM | 4.4% / 8.3% | 0.9% / 3.3% | 5.6% / 6.3% | Data Center total 2.4% / 5.5% | DS226 |

Churn is **not** in the DLR 10-Ks; it is in the 8-K financial supplements only.

### C3. Others

| Company | Metric | Figures | Source |
|---|---|---|---|
| IRM Global Data Center | churn, stated in segment MD&A | 350 bp (2022), 570 bp (2023), 700 bp (2024); **not stated for 2025 or H1 2026** | I22, I23, I24 |
| AMT Data Centers | no renewal spread or churn number; qualitative only | see quotes | A25, AQ226 |
| Cyxtera | Churn in $ of MRR | $5.9M (2022), $5.4M (2021), $6.9M (2020); MRR $58.7M / $53.5M / $52.9M at year ends. *Computed* churn / beginning MRR: 11.0% (2022), 10.2% (2021) | C22 |
| CyrusOne (STALE) | recurring rent churn | 3.5% (2021), 3.6% (2020) | CONE21 |
| Switch (STALE) | revenue churn | 0.6% (2021), 0.9% (2020) | SW21 |
| CoreSite (STALE) | GAAP rent growth on renewals | 5.5% (2020), 4.2% (2019), 7.5% (2018) | COR20 leasing table |
| QTS (STALE) | renewal rent change (total MRR per sq ft, same-space renewals) | +1.4% FY2020; (1.5)% Q4 2020 | QTS20 |

## D. Return on plant, FY2023-FY2025: (operating income + D&A) / average gross plant (*computed*)

| Company | FY2023 | FY2024 | FY2025 | Inputs and definitional differences |
|---|---|---|---|---|
| **Equinix** | 11.9% | 11.1% | 11.6% | OI 1,443 / 1,328 / 1,848 (EQ25 statement); D&A 1,844 / 2,011 / 2,066 (caller); gross PP&E 25,982 (2022), 29,202 (2023), 30,723 (2024), 36,972 (2025) from on-disk 10-Ks FY2023-FY2025 PP&E note. OI is after impairments of 0 / 233 / 68. |
| **Digital Realty** | 7.0% | 6.9% | 7.4% | OI 524.5 / 471.9 / 658.5; D&A 1,694.9 / 1,771.8 / 1,894.6 (D23-D25 income statements). Gross = investments in operating properties at cost + CIP and space held for development + land held: 31,043.6 (2022), 32,059.8 (2023), 32,762.1 (2024), 36,427.2 (2025) (D23-D25 Note "Investments in Properties"). Excludes $3.4bn investments in unconsolidated JVs (2025) and gains on disposition ($995.6M in 2025, below OI). OI is after impairments of 118.4 / 191.2 / 78.6; adding them back gives 7.4% / 7.5% / 7.6%. |
| **AMT Data Centers** | 3.9% | 4.4% | 5.3% | **Different basis.** Segment operating profit (segment revenue less segment opex and segment SG&A; excludes D&A, so it is already a pre-D&A figure) 414.7 / 455.2 / 562.2 over average segment **total assets** 10,702.8 (2022), 10,482.9 (2023), 10,431.6 (2024), 10,703.9 (2025) (A23, A25 segment note). Total assets include goodwill and intangibles from the CoreSite purchase, so this is a return on acquisition cost, not on plant. Alternative on Schedule III gross real estate for Data Centers (6,309.9 / 6,861.4 / 7,683.4 at 2023 / 2024 / 2025): **6.9% (2024), 7.7% (2025)**. H1 2026 segment operating profit 308.9 on total assets 10,786.5. |
| **IRM Global Data Center** | not computable | | | IRM reports no segment assets or segment gross plant, and segment profit is Adjusted EBITDA (137.3 / 175.6 / 215.9 / 282.5 / 416.3 for 2021-2025; margin 42.0% / 43.8% / 43.6% / 45.6% / 51.8%; H1 2026 270.1, 52.2%). |
| **Cyxtera** | n/a | n/a | FY2022 only: 1.7% | OI (202.1) + D&A 243.0 = 40.9 over average gross PP&E (2,262.6, 2,513.5). OI includes a $153.6M goodwill impairment; adding it back gives 8.1%. Gross PP&E includes $1,130.9M of finance-lease assets (C22). |

## E. Capital expenditure as % of revenue, FY2023-FY2025, and the maintenance split (*computed*)

| Company | FY2023 | FY2024 | FY2025 | Maintenance / recurring split |
|---|---|---|---|---|
| **Equinix** (caller figures) | recurring 219 = 2.7% of rev; 11.9% of D&A | 250 = 2.9%; 12.4% | 284 = 3.1%; 13.7% | caller |
| **Digital Realty** | cash-flow "Improvements to investments in real estate" 3,525.6 = 64.4%; MD&A capex table (ex indirect costs) 3,309.6 = 60.4% | 2,831.7 = 51.0%; 2,601.6 = 46.8% | 3,181.2 = 52.0%; 2,913.4 = 47.7% | MD&A table (D23, D25): development 2,966.9 / 2,260.7 / 2,541.1; enhancement 15.7 / 35.2 / 28.3; **recurring 327.0 / 305.7 / 343.9** = 6.0% / 5.5% / 5.6% of revenue. **Recurring / real-estate D&A** (FFO reconciliation: 1,657.2 / 1,730.1 / 1,855.1) = **19.7% / 17.7% / 18.5%**; recurring / total D&A = 19.3% / 17.3% / 18.2%. Indirect costs capitalized (incl. interest) 267.8 (2025), 230.1 (2024) are outside the table. |
| **AMT Data Centers** | 428.1 = 51.3% | 545.0 = 58.9% | 665.2 = 63.2% | Segment capex from segment note (A25). H1 2026 341.3 = 58.2%. No segment-level maintenance split. A25 says total-company discretionary capex "Includes ... approximately $608.9 million of spend related to data center assets" (2025); the *computed* residual 665.2 - 608.9 = 56.3 (5.3% of revenue) is NOT a filer-labelled maintenance figure. |
| **IRM Global Data Center** | growth 964.2 + recurring 17.2 = 198.3% | 1,422.1 + 19.7 = 232.5% | 1,747.0 + 20.6 = 220.0% | IRM labels "Recurring Capital Expenditures: Data Center: Expenditures related to the replacement of equivalent components and overall maintenance of existing data center assets" (I25). Recurring DC = 3.5% / 3.2% / 2.6% of segment revenue. (2021: 308.7 + 13.3; 2022: 592.9 + 17.0.) No segment D&A, so no recurring / D&A ratio. |
| **Cyxtera** | FY2022: cash purchases of P&E 131.8 = 17.7% | FY2021: 77.5 = 11.0% | FY2020: 83.2 = 12.0% | Plus non-cash P&E purchases 38.5 / 65.7 / 55.3 (C22). No maintenance split. |

## F. Who names whom

| Filer | Names Equinix? | Quote / note | Source |
|---|---|---|---|
| Digital Realty | **Yes**, every year FY2021-FY2025 | "We compete with numerous data center providers globally, many of whom own or operate properties similar to ours in some of the same metropolitan areas where our data centers are located, including Equinix, Inc. and NTT; various private operators in the U.S.; as well as Global Switch Holdings Limited and various regional operators in Europe, Asia, Latin America, Africa and Australia." (FY2021 version also names "Switch, Inc.") | D25, D21 |
| Digital Realty (customer list) | Equinix is DLR's **6th-largest customer** | 20-largest-customers table at 31 Dec 2025: "Equinix", 14 locations, annualized recurring revenue $95,641K, 2.0% of total. Equinix appears in the same table in D21-D24. | D25 |
| Cyxtera | **Yes** | "Certain of our data center competitors include Digital Realty Trust, Inc. and Equinix, Inc. as well as several privately held data center services providers." | C22 |
| CoreSite (STALE) | **Yes** | "...including CyrusOne, Inc., Cyxtera Technologies, Inc., Digital Realty Trust, Inc., Equinix, Inc., Evoque (formerly AT&T, Inc. Data Centers), Flexential, Internap Network Services Corporation, Quality Technology Services, RagingWire Data Centers, a NTT Communications company, SABEY Corporation, Stack Infrastructure, Switch, Inc., and zColo." | COR20 |
| Switch (STALE) | **Yes** | "...including managed services providers and real estate investment trusts (“REITs”) such as CoreSite Realty Corporation, CyrusOne Inc., Digital Realty Trust, Inc., Equinix, Inc. and QTS Realty Trust, Inc., ..." | SW21 |
| American Tower | **No** (as competitor) | FY2025 names tower competitors only; data center competitors unnamed: "Our data center business also competes with a variety of companies offering similar data center solutions and services, including space, power, interconnection and development services." Only Equinix mention in A25 is an officer biography (former Equinix sales role). | A25 |
| Iron Mountain | **No** | Competitors unnamed: "We also compete with numerous data center developers, owners and operators, many of whom own properties comparable to ours in several of the same metropolitan areas where our facilities are located." | I25 |
| CyrusOne, QTS (STALE) | **No** in the documents read | CONE21 and QTS20 competition sections name no competitor. | CONE21, QTS20 |
| **Equinix** | **Names no competitor in FY2025** | FY2025 competitive landscape: "It is estimated that we are one of more than 2,400 companies that provide these offerings around the world." and "While a large number of enterprises and service providers, such as hyperscale cloud service providers, own their own data centers, we believe enterprises are shifting away from single-tenant solutions toward those that enable customers to outsource some or all of their IT infrastructure and interconnection requirements to third-party facilities, such as those operated by Equinix." | EQ25 |
| Equinix, history | Named competitors **through FY2018**, stopped from FY2019 | FY2018: "Providers in addition to Equinix that we believe could be defined as offering carrier-neutral colocation include CoreSite, Digital Realty Trust, Global Switch, Interxion and Telehouse." and "Providers in addition to Equinix that offer colocation both globally and locally include firms such as COLT and NTT." Counts of competitor names in on-disk Equinix 10-Ks: FY2015 8, FY2016 13, FY2017 10, FY2018 10, FY2019-FY2021 1 each (a Digital Realty share purchase agreement in the exhibit list, not a competitor mention), FY2022-FY2025 0. | EQ18; grep of `../10K_FY20*.txt` |

## G. Pricing power, pricing pressure, oversupply (verbatim)

**Rising renewal rates (the peers' own words):**
- DLR, Q4 2021 (DS21): "Rental rates on renewal leases signed during the fourth quarter of 2021 rolled down 3.9% on a cash basis and down 2.6% on a GAAP basis."
- DLR, Q4 2022 (DS22): "Rental rates on renewal leases signed during the fourth quarter of 2022 rolled up 0.8% on a cash basis and up 1.1% on a GAAP basis."
- DLR, Q4 2023 (DS23): "Rental rates on renewal leases signed during the fourth quarter of 2023 increased 8.2% on a cash basis and 10.6% on a GAAP basis."
- DLR, Q4 2024 (DS24): "Rental rates on renewal leases signed during the fourth quarter of 2024 increased 4.7% on a cash basis and 9.1% on a GAAP basis."
- DLR, Q4 2025 (DS25): "Rental rates on renewal leases signed during the fourth quarter of 2025 increased 6.1% on a cash basis and 12.0% on a GAAP basis."
- DLR, Q2 2026 (DS226): "Rental rates on renewal leases signed during the second quarter of 2026 increased 25.4% on a cash basis and 32.0% on a GAAP basis."
- DLR outlook, FY2021 10-K (D21): "...we expect average aggregate rental rates on re-leased or renewed data center leases for 2022 expirations to generally be consistent with the rates currently being paid for the same space on a GAAP basis and on a cash basis." FY2022-FY2025 10-Ks (D22-D25) and DQ226 each: "...we expect average aggregate rental rates on renewed data center leases for [next year] expirations to be positive as compared with the rates currently being paid for the same space on a GAAP basis and on a cash basis."
- DLR 2026 guidance (DS25 slides, Ex-99.2): "Rental Rates on Renewals Leases (Cash) 6.7% 6.0% – 8.0%" (actual 2025, guidance 2026).
- AMT (A25): "Revenue growth from our Data Centers segment in the United States, including rental and power revenue from new lease commencements and expansions, contractual rent and power escalations on existing leases, mark-to-market increases on renewing leases and increased interconnection services and solutions." AQ226: "An increase of $7.9 million in interconnection revenue, primarily due to customer interconnection net additions and pricing increases from existing cross connects".
- IRM (I25): "a 620 basis point increase in Adjusted EBITDA Margin reflecting recent lease commencements, improved pricing and cost containment." IRM (I23, I24): growth from leases "improved pricing and higher pass-through power costs, partially offset by churn of 570 basis points" (2023) / "...churn of 700 basis points" (2024).
- Cyxtera (C22): "Interconnection revenue increased by $6.3 million compared to the prior year, as a result of rate increases in the year."

**Falling renewal rates / pricing pressure:**
- **CyrusOne, FY2021 (CONE21), stale but the only filer stating renewals repriced DOWN:** "Rates contracted with our customers that renewed in 2021 were lower than the rates previously in effect, a trend that we expect to continue and to be driven by increases in data center supply and cloud company offerings. As such, we anticipate decreases in rates as contracts renew which could continue to affect our revenue in future periods. Future economic downturns, regional downturns affecting our markets, or oversupply of or decrease in demand for data center colocation services could impair our ability to attract new customers or renew existing customers’ leases on favorable terms, and this could adversely affect our ability to maintain or increase revenues."
- DLR risk factor (D25): "If the supply of data center space continues to increase as a result of these activities or otherwise, rental rates may be reduced or we may face delays in leasing or be unable to lease our vacant space, including space that we develop."
- AMT (A25): "These advantages could allow our data center competitors to respond more quickly or effectively to strategic opportunities and, as a result, we may lose existing or potential data center customers, incur costs to improve our data centers or be forced to reduce our rental rates. These risks are compounded by the fact that a significant percentage of our data center customer leases expire every year."
- Switch (SW21): "We operate in a competitive market and we face pricing pressure for our services. Prices for our services are affected by a variety of factors, including supply and demand conditions and pricing pressures from our competitors. We may be required to lower our prices to remain competitive, which may decrease our margins and adversely affect our business prospects, financial condition and results of operations."
- CoreSite (COR20): "In addition, our largest customers may choose to develop new data centers or expand existing data centers of their own and may seek to negotiate rent reductions in the future. In the event that any of our key customers were to do so, it could result in a loss of business to us or increase pricing pressure on us."
- Cyxtera (C22): "Our competitors may adopt aggressive pricing policies. As a result, we may suffer from pricing pressure that would adversely affect our ability to generate revenues."
- Equinix itself (EQ25), for symmetry: "Some of our competitors may adopt aggressive pricing policies, especially if they are not highly leveraged or have lower return thresholds than we do. As a result, we may suffer from pricing pressure that would adversely affect our ability to generate revenues."

## Cyxtera: the failed public colocation operator (for "the named way it dies")

| Item | Figure | Source |
|---|---|---|
| Revenue FY2020 / 2021 / 2022 | 690.5 / 703.7 / 746.0 | C22 |
| Income (loss) from operations | 50.4 (2020, incl. $97.7M recovery of affiliate note) / (115.2) / (202.1) | C22 |
| Interest expense, net | (169.4) / (164.9) / (163.3) | C22 |
| Net loss | (122.8) / (257.9) / (355.1) | C22 |
| Owned vs leased | "We own two data center facilities and lease the rest of our data center portfolio." | C22 Item 2 |
| Finance-lease obligations / term-loan debt, 31 Dec 2022 | $1,121.8M / $907.0M | C22 |
| Total undiscounted lease payments, 31 Dec 2022 | $3,671.2M (operating $481.9M, finance $3,189.3M); finance-lease discount rate 10.0% | C22 lease note |
| Filing | Chapter 11, 4 June 2023, District of New Jersey; $200M DIP financing | C8K |

Verbatim on what drove the failure (no single-sentence cause is stated in the 8-K; the drivers are in the 10-K and last 10-Q):
- C22: "We have substantial debt with near term maturities. Specifically, our $120.1 million revolving credit facility would have matured on November 1, 2023 ... and our term loan facilities with $869.0 million of outstanding indebtedness as of December 31, 2022 mature on May 1, 2024".
- C22: "We have never been profitable and do not expect to generate positive net income until at least 2030."
- C22: "Inflation in the United States, Europe and other regions has risen to levels not experienced in recent decades, and it has had a material impact on our business, by, for example, materially increasing our interest rate payments on our outstanding debt and the cost of obtaining new capital. Rising prices for materials related to construction and our data center offerings, energy and gas prices, as well as rising wages and benefits costs negatively impact our business by increasing our operating costs."
- C22: "This increase in cost of revenues was primarily attributable to the cost of power, as utilities expenses increased by $21.7 million during the year ended December 31, 2022 compared to the prior year."
- CQ123: "Since the Company has not successfully further extended its Revolving Facility Amendment and term loan indebtedness, or refinanced or repaid the Revolving Facility Amendment and term loan indebtedness with proceeds from other sources, such as new debt, equity capital, or sales of assets, the Company will not be able to meet its financial obligations due within twelve months from the date of issuance of these March 31, 2023 unaudited condensed consolidated financial statements with its internally generated cash from operations and available cash on hand, which raises substantial doubt about our ability to continue as a going concern."
- CQ123: "In addition, the Company may seek reductions in rental obligations with landlords, seek additional debt or equity capital, reduce or delay the Company's business activities and strategic initiatives, and/or sell assets."
- C8K Ex-99.1: "Cyxtera expects to use the Chapter 11 process to strengthen the Company’s financial position, meaningfully deleverage its balance sheet and facilitate the business’s long-term success."
- Note for the caller: revenue grew in each of the last three years and churn by MRR was $5.4M-$6.9M a year; the filings attribute distress to debt maturities, interest cost, power cost and inflation, not to a revenue collapse.

## What could not be numbered, and why

1. **DLR interconnection revenue in the 10-K**: not broken out; only the 8-K supplement's "Interconnection and other" line exists, which includes "other".
2. **DLR, AMT, IRM interconnection / cross-connect COUNT**: not disclosed in any document fetched.
3. **DLR churn and cash re-leasing spreads**: not in the 10-K; taken from 8-K supplements (furnished, not filed, under Item 2.02/7.01).
4. **IRM return on plant (D)**: IRM reports no segment assets and no segment D&A.
5. **IRM churn 2025 and H1 2026**: not stated in I25 or IQ226 (stated for 2022-2024 only).
6. **AMT maintenance capex for Data Centers**: no segment split; only a computed residual (flagged).
7. **AMT Data Centers FY2021 growth**: segment existed four days in 2021 (CoreSite acquired Dec 2021).
8. **IRM FY2021 growth**: FY2020 base not fetched.
9. **Cyxtera after Q1 2023**: no further 10-K/10-Q; FY2023 onward does not exist in EDGAR.
10. **CyrusOne, QTS, Switch, CoreSite after going private**: no filings with operating metrics; all figures above are STALE (FY2020 or FY2021).
11. **Private operators (Vantage, Stack, Aligned, NTT GDC, Cologix, Flexential, DataBank)**: **not measured by any filing found.** They appear on EDGAR only as ABS-15G due-diligence filers (securitization issuers), in fund NPORT-P holdings of their ABS notes, and in CMBS trust 10-Ks. Two partial exceptions, neither a usable measurement:
    - Blue Owl Digital Infrastructure Trust 10-K FY2025 (ODIT25) owns 11 STACK-operated properties; operations "commenced on December 1, 2025", total revenues $29,499K for one month. Not a measure of STACK.
    - DigitalBridge 10-K FY2021 (DB21) held 20% of DataBank and 13% of Vantage SDC and reported a combined "Digital Operating" segment; both were deconsolidated as discontinued operations at 31 Dec 2023 (DB25). No per-operator pricing or return metric.
12. **Hyperscaler self-build**: no filing measures it. The only statements are qualitative (EQ25 quote in F above; DLR D25: "in areas where high data center construction and operating costs and long time-to-market prohibit many of our customers from building their own data centers, our global footprint and scale allow us to meet our customers’ needs quickly and efficiently.").
13. **NTT Global Data Centers**: FTS finds 4 hits total (GDS 20-F/6-K, a SPAC proxy) and zero 10-Ks.

## EDGAR full-text search log (efts.sec.gov; date range 2021-01-01 to 2026-09-18 unless noted; full results in `FTS_queries.json`, `FTS_queries_naming.json`)

| Query (exact phrase) | Forms | Hits | What the hits are |
|---|---|---|---|
| "Vantage Data Centers" | all | 10,000 (cap) | mostly ABS-15G (Vantage Data Centers Holdings; Retained Vantage Data Centers LP) and fund NPORT-P |
| "Vantage Data Centers" | 10-K | 22 | DigitalBridge (exhibit 21 subsidiary lists), Ares funds, unrelated customers |
| "Stack Infrastructure" | all | 9,986 | NPORT-P, STACK Infrastructure Parent ABS-15G, Blue Owl Digital Infrastructure Trust 10-K |
| "Stack Infrastructure" | 10-K | 21 | Blue Owl Digital Infrastructure Trust (indentures), CoreSite 10-K (competitor list), others |
| "Aligned Data Centers" | all | 10,000 (cap) | NPORT-P, ADC Holdco ABS-15G |
| "Aligned Data Centers" | 10-K | 1,188 | CMBS trust 10-Ks (one hit each) |
| "NTT Global Data Centers" | all | 4 | GDS Holdings 20-F/6-K, SPAC proxy |
| "NTT Global Data Centers" | 10-K | 0 | |
| "Cologix" | all | 6,401 | NPORT-P, Cologix US ABS-15G |
| "Cologix" | 10-K | 11 | credit funds, unrelated |
| "Flexential" | all | 6,956 | Flexential Corp ABS-15G, NPORT-P |
| "Flexential" | 10-K | 1,564 | CMBS trust 10-Ks |
| "DataBank" | all | 10,000 (cap) | DataBank Holdings ABS-15G, DigitalBridge 8-K/10-Q, NPORT-P |
| "DataBank" | 10-K | 110 | DigitalBridge, MSCI and unrelated (word collision) |
| "colocation" | ABS-15G | 33 | Switch Ltd, ADC Holdco, CyrusOne LP, CyrusOne Data Centers Issuer I, Phoenix Data Center Acquisitions |
| "data center" | ABS-EE | 123 | CMBS trusts |
| "cross-connects" | 10-K | 30 | Equinix 6, IBKR 6, DLR 4, Cyxtera 2, Switch 2, WhiteFiber 2 |
| "interconnection revenue" | 10-K | 25 | DLR 7, Equinix 6, AMT 3, Cogent 3, CyrusOne 2, Cyxtera 2 |
| "colocation pricing" | 10-K | 0 | |
| "oversupply" | 10-K | 2,606 | dominated by food, drilling, agriculture filers |
| "Equinix" in each peer's 10-Ks (all years; `sources.fts_count`, bare 10-digit CIK) | 10-K | DLR 26, AMT 10, IRM 0, CYXT 2, CONE 1, SWCH 5, COR 11, QTS 0 | a screen only; the naming test above rests on reading the documents |
| Competitor names in Equinix 10-Ks (all years) | 10-K | "Digital Realty" 17, "CoreSite" 10, "NTT" 19, "Iron Mountain" 0, "American Tower" 0, "hyperscale" 18 | on-disk grep shows the names stop after FY2018 (see F) |

ABS-15G filings are third-party due-diligence reports for securitizations; none of the ones listed was opened, and none is a measured operating metric.
