# SD COMPETITOR ROW: Mach (MNR) · Gulfport (GPOR) · Comstock (CRK) · CNX
### Filing-sourced. Same metric, same window (FY2021 to FY2025 calendar years). Built 2026-08-31.

**Subject:** SandRidge Energy, Inc. (NYSE: SD), CIK 0001349436, Mid-Continent (Anadarko Basin /
Cherokee play, OK-KS-TX), gas-and-NGL-weighted E&P, full-cost method, no debt.

**Sources.** All figures below are from SEC EDGAR: the XBRL company-facts API
(`https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`, filtered to `form == "10-K"`)
for financial-statement items, and the 10-K primary documents for reserves, PV-10 and
production, which are not carried as undimensioned XBRL facts for most of these filers.
Accession numbers are recorded under each table. No aggregator was used. No number below is
estimated except where the row says so in words.

**Peer set built (4 of 4 priority peers obtained in full, plus one optional):** MNR, GPOR, CRK
and CNX obtained in full; AMPY obtained but disqualified as a comparable (see §5). PHX Minerals
could not be obtained (see §5).

---

## 1. RETURN ON EQUITY: NetIncomeLoss ÷ average StockholdersEquity

**Metric definition, applied identically to every row:**
numerator `us-gaap:NetIncomeLoss` (net income attributable to the parent) for the fiscal year;
denominator is the simple average of `us-gaap:StockholdersEquity` at the prior and current
fiscal year end (`us-gaap:PartnersCapital` / `us-gaap:MembersEquity` for the LP). Parent-only in
both numerator and denominator, so the noncontrolling interests at CRK and CNX do not distort
the ratio.

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | 5-yr simple avg |
|---|---:|---:|---:|---:|---:|---:|
| **SD** (SandRidge) | **62.5%** | **66.1%** | **12.7%** | **13.6%** | **14.5%** | **33.9%** |
| MNR (Mach), *see caveat A* | 66.2% | 118.6% | 7.7% | 15.5% | 9.0% | 43.4% *(not comparable)* |
| GPOR (Gulfport), *see caveat B* | n/c | 71.8% | 98.4% | (13.5%) | 24.1% | 45.2% *(4 yrs only)* |
| CRK (Comstock) | (22.7%) | 68.4% | 9.1% | (10.0%) | 16.2% | 12.2% |
| CNX (CNX Resources), *see caveat C* | (12.3%) | (4.3%) | 47.1% | (2.1%) | 15.0% | 8.7% |
| AMPY (Amplify), *see caveat D* | NM | NM | 203.2% | 3.2% | 10.1% | NM |

### Average equity used (US$ thousands), for audit

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|
| SD | 186,694 | 366,622 | 478,016 | 464,321 | 485,701 |
| MNR | 209,130 | 435,964 | 892,477 | 1,195,385 | 1,594,218 |
| GPOR | n/c | 689,156 | 1,495,258 | 1,936,536 | 1,773,056 |
| CRK | 1,139,776 | 1,645,546 | 2,318,364 | 2,299,718 | 2,443,916 |
| CNX | 4,061,355 | 3,325,367 | 3,655,739 | 4,229,524 | 4,217,523 |
| AMPY | (49,289) | (34,703) | 193,236 | 399,974 | 433,818 |

### Caveats: read these before using any number above

**A. MNR is a limited partnership and its ROE is NOT comparable to a C-corp's.** Three separate
defects, all disclosed in the filings:

1. **No entity-level income tax.** Mach's only income tax is the Texas franchise tax
   (`srt:FutureNetCashFlowsRelatingToProvedOilAndGasReservesIncomeTaxExpense` = $17.8M on
   $6.1bn of future net cash flows, and the 10-K states "No provision is included for federal
   income taxes since our future net cash flows are not subject to taxation"). Mach's net
   income is therefore a **pre-tax** number sitting on top of a **post-tax** denominator
   convention. SD's is after tax.
2. **The denominator is deliberately starved.** Mach runs a variable-distribution model and
   pays out essentially all distributable cash flow, so partners' capital is held down by
   distributions rather than compounded. That mechanically raises the ratio.
3. **FY2021 and FY2022 are predecessor amounts** of Mach Natural Resources LLC, a private
   entity, presented as members' equity; Mach Natural Resources LP IPO'd in October 2023 and
   the FY2023 denominator therefore straddles a recapitalisation.

   **Verdict: report as return on average partners'/members' capital, flagged. Do not rank MNR
   against SD on this line.**

**B. GPOR FY2021 is not computable** and is marked `n/c`. Gulfport emerged from Chapter 11 on
17 May 2021 and adopted fresh-start reporting, so FY2021 exists only as two stub periods:
Predecessor 1 Jan to 17 May 2021 (net income **+$250,994K**) and Successor 18 May to 31 Dec 2021
(net loss **($112,829K)**). Equity was **negative $300,500K** at 12/31/2020 and was reset to
**$639,667K** at 18 May 2021. A single-year ROE across that reset would be arithmetic nonsense.
For reference only, the 7.5-month successor stub returns **(19.0%)** on average successor
equity, a stub figure, not annualised, not to be ranked.

**C. CNX's GAAP net income is dominated by unrealised mark-to-market on a very large hedge
book, not by operations.** The FY2025 10-K attributes the year-over-year swing to "a $721
million net change in commodity derivative instruments." The FY2023 +47.1% and the FY2021,
FY2022 and FY2024 losses are largely hedge accounting reversing on itself. CNX's ROE line
measures its derivative position, not its wells.

**D. AMPY FY2021 and FY2022 ROE is Not Meaningful because average equity was negative**
(($49,289K) and ($34,703K)). Dividing a loss by a negative number produces a *positive* 65.1%
for FY2021, and dividing a profit by a negative number produces a *negative* 166.8% for FY2022.
Both are artifacts. They are suppressed rather than printed. FY2023's 203.2% is 63% attributable
to a **$248,979K deferred-tax valuation-allowance release** (`us-gaap:IncomeTaxExpenseBenefit`
= (248,979)), not to operations.

**E. Non-operating tax benefits inflate three of the high years, on the same tag
`us-gaap:IncomeTaxExpenseBenefit` (negative = benefit):**

| | year | net income | tax benefit in it | share |
|---|---|---:|---:|---:|
| SD | FY2022 | 242,168 | (64,529) | 27% |
| GPOR | FY2023 | 1,470,916 | (525,156) | 36% |
| AMPY | FY2023 | 392,750 | (248,979) | 63% |
| CRK | FY2024 | (229,651) | (149,075) | *benefit reduced the loss* |

SD's FY2021 116,738 carries **zero** income tax expense or benefit and is a clean operating
number driven by the 2021 gas price recovery.

### Sources, Table 1

| Filer | CIK | Tags | FY2025 10-K accession | Earlier-year accessions used for comparatives |
|---|---|---|---|---|
| SD | 0001349436 | `us-gaap:NetIncomeLoss`, `us-gaap:StockholdersEquity` | **0001628280-26-015318** (`sd-20251231.htm`, filed 2026-03-05) | 0001628280-21-003933 (FY20 eq), 0001628280-22-005741 (FY21 eq), 0001628280-23-008082 (FY22 eq), 0001628280-24-009706 (FY21 NI, FY23 eq), 0001628280-25-012086 (FY22 NI, FY24 eq) |
| MNR | 0001980088 | `us-gaap:NetIncomeLoss`, `us-gaap:PartnersCapital`, `us-gaap:MembersEquity` | **0001628280-26-017249** (`mnr-20251231.htm`, filed 2026-03-12) | 0001628280-24-014131 (FY21/FY22 predecessor NI and members' equity), 0001628280-25-012591 (FY22 NI, FY24 capital) |
| GPOR | 0000874499 | `us-gaap:NetIncomeLoss`, `us-gaap:StockholdersEquity` | **0001628280-26-011487** (`gpor-20251231.htm`, filed 2026-02-25) | 0001628280-21-004026 (FY20 eq), 0001628280-22-004445 (FY21 stub NI and eq), 0001628280-23-005790, 0001628280-24-007527, 0001628280-25-008043 |
| CRK | 0000023194 | `us-gaap:NetIncomeLoss`, `us-gaap:StockholdersEquity` | **0001193125-26-059001** (`crk-20251231.htm`, filed 2026-02-19) | 0000023194-21-000015, 0000023194-22-000011, 0000023194-23-000009, 0000950170-24-016532, 0000950170-25-024783 |
| CNX | 0001070412 | `us-gaap:NetIncomeLoss`, `us-gaap:StockholdersEquity` | **0001070412-26-000038** (`cnx-20251231.htm`, filed 2026-02-10) | 0001070412-21-000016, 0001070412-22-000011, 0001070412-23-000015, 0001070412-24-000015, 0001070412-25-000049 |
| AMPY | 0001533924 | `us-gaap:NetIncomeLoss`, `us-gaap:StockholdersEquity` | **0001104659-26-025299** (`ampy-20251231x10k.htm`, filed 2026-03-09) | 0001564590-21-012491, 0001558370-22-003152, 0001558370-23-003321, 0001558370-24-002637, 0001558370-25-002273 |

---

## 2. RESERVES, PV-10, PRODUCTION, RESERVE LIFE, ORGANIC REPLACEMENT

**Units.** The filers report in three different units. Every row below is shown **both** in
MMBoe and Bcfe at the standard 6 Mcf : 1 Boe conversion, so the row is same-metric. The
"as filed" column names the filer's own unit and figure so the conversion can be checked.

| | Total proved FY2025 | FY2025 as filed | Total proved FY2024 | FY2025 production | Reserve life (R/P, yrs) | E&D FY2025 | Organic replacement (E&D ÷ production) |
|---|---:|---|---:|---:|---:|---:|---:|
| **SD** | **69.1 MMBoe** / 414.9 Bcfe | 69,148 MBoe | **63.1 MMBoe** / 378.5 Bcfe | 6.77 MMBoe / 40.6 Bcfe | **10.2** | 7,298 MBoe | **108%** |
| MNR | 704.7 MMBoe / 4,228.4 Bcfe | 704,732 MBoe | 337.3 MMBoe / 2,023.5 Bcfe | 37.73 MMBoe / 226.4 Bcfe | **18.7** | **zero** | **0%** |
| GPOR | 708.8 MMBoe / 4,253.0 Bcfe | 4,253 Bcfe | 661.5 MMBoe / 3,969 Bcfe | 63.17 MMBoe / 379 Bcfe | **11.2** | 701 Bcfe | **185%** |
| CRK | 1,167.6 MMBoe / 7,005.3 Bcfe | 7,004,121 MMcf + 198 MBbl | 627.3 MMBoe / 3,764.1 Bcfe | 75.07 MMBoe / 450.4 Bcfe | **15.6** | 3,737.8 Bcf | **830%** |
| CNX | 1,610.4 MMBoe / 9,662.1 Bcfe | 9,662,144 MMcfe | 1,423.0 MMBoe / 8,537.9 Bcfe | 104.83 MMBoe / 629.0 Bcfe | **15.4** | 866.9 Bcfe | **138%** |
| AMPY *(not comparable)* | 38.1 MMBoe / 228.6 Bcfe | 38,096 MBoe | 93.0 MMBoe / 557.8 Bcfe | 6.73 MMBoe / 40.4 Bcfe | 5.7 | zero | 0% |

### Value of the reserve base at 12/31/2025

| | PV-10 (pre-tax) | Standardized measure (after-tax) | PV-10 per Boe | PV-10 per Mcfe | Note |
|---|---:|---:|---:|---:|---|
| **SD** | **$439.6M** | $439.6M | **$6.36** | **$1.059** | identical because SD's future income tax expense is **$0**; NOLs shelter the whole stream (10-K line: "Future income tax expenses" reported as nil) |
| MNR | $3,088M | $3,080M | $4.38 | $0.730 | near-identical because an LP pays no federal income tax; the $8M gap is Texas franchise tax |
| GPOR | $3,622M | $3,403M | $5.11 | $0.852 | 10-K states "4.3 Tcfe of proved reserves with a Standardized Measure of $3.4 billion and a PV-10 of $3.6 billion"; future income tax effect $219M |
| CRK | **not disclosed** | $3,867M | n/d | n/d ($0.552 after-tax) | **CRK does not publish PV-10 anywhere in the FY2025 10-K.** The pre-tax 10% discount factor is not disclosed separately, so PV-10 cannot be derived from the filed table. Recorded as a gap, not estimated. |
| CNX | $6,830M | $5,066M | $4.24 | $0.707 | disclosed directly: "Total PV-10 Non-GAAP Measure of Pre-Tax Discounted Future Net Cash Flows $6,830" |
| AMPY | $376.4M | $335.1M | $9.88 | $1.647 | oil-weighted (93% oil), so per-Boe value is not comparable to gas peers |

### What the reserve additions actually were, FY2025 (the important line)

The organic-replacement column above is only half the story. The full roll-forward shows how
each peer got its reserves.

- **SD** (accn 0001628280-26-015318): revisions +3,852 MBoe, acquisitions +1,677, **extensions
  and discoveries +7,298**, production (6,768); reserves 63,090 to 69,148 MBoe. Genuine
  drill-bit growth: 108% organic replacement plus positive price revisions. SD's proved
  undeveloped reserves went 0 (FY2022, FY2023) to 6,120 (FY2024) to 8,831 MBoe (FY2025), the
  first PUD book SD has carried in years, meaning it has only just re-acquired a development
  inventory.
- **MNR** (accn 0001628280-26-017249): revisions +32,234 MBoe, **purchases in place +372,979**,
  **extensions and discoveries nil**, production (37,730); 337,250 to 704,732 MBoe. The 10-K
  states in terms: *"The Company had no extensions or discoveries in 2025."* Mach classifies its
  own drilling as *revisions*, explaining that it drills "in mature basins with well-established
  production histories and clearly defined development patterns." **Mach's reserve growth in
  2025 was 92% bought, not drilled.**
- **GPOR** (accn 0001628280-26-011487): extensions +701 Bcfe, revisions (38), production (379);
  3,969 to 4,253 Bcfe. Purchases and sales of minerals in place were both **zero** in 2022,
  2023, 2024 and 2025. Gulfport grew entirely by the drill bit across four years.
- **CRK** (accn 0001193125-26-059001): extensions +3,737,848 MMcf, revisions (29,753), sales
  (15,870), production (450,202); 3,762,098 to 7,004,121 MMcf. The 830% is real but it is
  **re-booking**, not discovery: the 10-K says 2025 extensions "include proved undeveloped
  reserves that were excluded in 2024 and 2023 due to low natural gas" prices. CRK's PUD book
  went 2,206,051 to 1,030,286 to 4,163,483 MMcf across three years on price alone.
- **CNX** (accn 0001070412-26-000038): extensions +866,936 MMcfe, purchases +667,993, revisions
  +69,057, price changes +170,747, production (628,960), sales (21,572); 8,537,943 to
  9,662,144 MMcfe. 138% organic plus the Apex Energy acquisition.
- **AMPY** (accn 0001104659-26-025299): divestitures (53,213 MBoe), revisions +5,079,
  production (6,733); 92,963 to 38,096 MBoe. Amplify **sold its entire gas book** in 2025.
  Natural gas reserves are literally zero at 12/31/2025. It is now an oil company.

### Sources, Table 2

All reserve, PV-10 and production figures were read from the FY2025 10-K primary documents, not
from XBRL, except where the XBRL `srt:` reserve tags corroborate (they do, for SD, GPOR and CNX):

| Filer | Document | Accession | Where in the document |
|---|---|---|---|
| SD | `sd-20251231.htm` | 0001628280-26-015318 | reserve roll-forward and standardized-measure tables, Notes to Consolidated Financial Statements (Supplemental Oil and Gas Disclosures) |
| MNR | `mnr-20251231.htm` | 0001628280-26-017249 | Item 1 "Reserve Data based on SEC Pricing" table (PV-10 and standardized measure); Notes, reserve quantity roll-forward and standardized measure; Item 1 "Production and Price History" |
| GPOR | `gpor-20251231.htm` | 0001628280-26-011487 | Item 1 Business (PV-10 headline); Item 1/2 "changes in our estimated proved reserves during 2025 (in Bcfe)" |
| CRK | `crk-20251231.htm` | 0001193125-26-059001 | Note 13 "Natural Gas and Oil Reserves Information (Unaudited)" |
| CNX | `cnx-20251231.htm` | 0001070412-26-000038 | Item 1/2 "Net Reserves (Millions of Cubic Feet Equivalent)" and "Discounted Future Net Cash Flows"; Note 22 Supplemental Gas Data |
| AMPY | `ampy-20251231x10k.htm` | 0001104659-26-025299 | Item 1/2 reserve summary with PV-10; Notes, "estimates of the net reserves for the periods indicated" |

XBRL corroboration used: `srt:ProvedDevelopedAndUndevelopedReserveNetEnergy`,
`srt:ProvedDevelopedAndUndevelopedReserveProductionEnergy`,
`srt:ProvedDevelopedAndUndevelopedReserveExtensionAndDiscoveryEnergy`,
`srt:StandardizedMeasureOfDiscountedFutureNetCashFlowsRelatingToProvedOilAndGasReserves`.
CRK and MNR do **not** carry reserve *quantities* as undimensioned XBRL facts; those came from
the document only.

---

## 3. OPERATING CASH FLOW, CAPEX, NET DEBT

### (b) Net cash provided by operating activities, tag `us-gaap:NetCashProvidedByUsedInOperatingActivities` (US$ thousands)

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|
| **SD** | 110,260 | 164,696 | 115,578 | 73,933 | **100,140** |
| MNR *(FY21 to FY22 predecessor)* | 198,462 | 553,542 | 491,742 | 505,292 | 506,956 |
| GPOR *(FY21 split, see note)* | 465,140 † | 739,077 | 723,181 | 650,033 | 803,193 |
| CRK | 860,940 | 1,698,388 | 1,016,846 | 620,337 | 899,607 |
| CNX | 926,357 | 1,235,014 | 814,588 | 815,779 | 1,028,957 |
| AMPY | 62,969 | 64,485 | 141,590 | 51,293 | 49,200 |

† GPOR FY2021 is Predecessor 1 Jan to 17 May 2021 ($172,155K) **plus** Successor 18 May to
31 Dec 2021 ($292,985K). This is an arithmetic sum of two stub periods, not a GAAP full-year
figure, and is marked as such.

### (c) Development capital expenditures (US$ thousands), acquisitions excluded

| | tag / filed line | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---:|---:|---:|---:|---:|
| **SD** | `PaymentsToAcquirePropertyPlantAndEquipment` = "Capital expenditures for property, plant and equipment", plus "Purchase of other property and equipment" | 11,583 | 44,085 | 26,375 | 26,404 | **59,173** |
| MNR | `PaymentsToAcquireOilAndGasPropertyAndEquipment` plus `PaymentsToAcquireOtherPropertyPlantAndEquipment` | 41,008 | 243,025 | 314,804 | 220,316 | 270,546 |
| GPOR | `PaymentsToAcquireOilAndGasProperty` = "Additions to oil and natural gas properties" | 309,443 † | 460,780 | 537,360 | 454,098 | 527,569 |
| CRK | `PaymentsToAcquirePropertyPlantAndEquipment` = "Capital expenditures" | 691,005 | 1,067,800 | 1,425,086 | 1,097,478 | 1,349,280 |
| CNX | `PaymentsToAcquirePropertyPlantAndEquipment` = "Capital expenditures" | 465,861 | 565,754 | 679,404 | 540,332 | 494,988 |
| AMPY | `PaymentsToExploreAndDevelopOilAndGasProperties` plus other PP&E | 29,294 | 34,814 | 31,378 | 73,344 | 85,310 |

† GPOR FY2021 is $102,330K predecessor plus $207,113K successor, summed. Same caveat as above.

**Acquisition spend is deliberately excluded** from this row and disclosed separately, because
it is the line that separates the drillers from the buyers. FY2025 acquisitions: SD $8,514K;
MNR reports in MD&A that cash used in acquisitions rose $507.3M year over year; CNX
`PaymentsToAcquireBusinessesNetOfCashAcquired` $517,599K (Apex Energy); GPOR $0; CRK $0, with
$428,868K of *proceeds* from asset sales.

### FY2025 free cash flow before acquisitions (OCF minus development capex), US$ thousands

| SD | MNR | GPOR | CRK | CNX | AMPY |
|---:|---:|---:|---:|---:|---:|
| **+40,967** | +236,410 | +275,624 | **(449,673)** | +533,969 | (36,110) |

### Development capex per Boe produced, FY2025: the cost line

| | $/Boe | $/Mcfe |
|---|---:|---:|
| CNX | **4.72** | 0.787 |
| MNR | 7.17 | 1.195 |
| GPOR | 8.35 | 1.392 |
| **SD** | **8.74** | **1.457** |
| AMPY | 12.67 | 2.112 |
| CRK | **17.97** | 2.995 |

*This is a single-year development-cost-per-unit-produced ratio, not a three-year F&D cost. It
is a screen, not a conclusion. SD's 2025 figure is elevated by its first real development
program in years, and CRK's by Western Haynesville appraisal drilling.*

### (g) Net debt at the most recent balance sheet date, 30 June 2026 (Q2 FY2026 10-Q)

| | Total debt | Cash & equivalents | **Net debt** | Accession (10-Q, period 2026-06-30) |
|---|---:|---:|---:|---|
| **SD** | **$0** | $113,345K | **($113,345K), net cash** | 0001628280-26-054413, filed 2026-08-06 |
| MNR | $1,169,989K | $41,187K | $1,128,802K | 0001628280-26-054263, filed 2026-08-06 |
| GPOR | $922,257K | $1,054K | $921,203K | 0001628280-26-052313, filed 2026-08-04 |
| CRK | $3,098,770K | $45,008K | $3,053,762K | 0001193125-26-326260, filed 2026-07-30 |
| CNX | $2,223,745K | $6,162K | $2,217,583K | 0001070412-26-000058, filed 2026-07-30 |
| AMPY | $0 | $21,212K | ($21,212K), net cash | 0001104659-26-093408, filed 2026-08-10 |

Tags: `us-gaap:LongTermDebt` / `LongTermDebtNoncurrent` plus `LongTermDebtCurrent`, and
`us-gaap:CashAndCashEquivalentsAtCarryingValue`. No current portion of long-term debt was
tagged for CRK or MNR at 6/30/2026, so total debt equals the noncurrent balance.

**Cross-checked against the filed statement, per operator protocol rule 4.** SD's 30 June 2026
condensed consolidated balance sheet (`sd-20260630.htm`) shows Total liabilities of $125,403K
consisting of accounts payable and accrued expenses $49,030K, current ARO $8,044K, other current
$750K, derivative contracts $31K, non-current ARO $66,855K and other long-term obligations
$693K, with **no borrowings of any kind**. Total stockholders' equity $542,681K on total assets
of $668,084K. Amplify's Note 8 states "the Company had no debt outstanding at June 30, 2026 and
December 31, 2025."

**Net-debt-to-FY2025-OCF (leverage screen):** SD **(1.1x), net cash** · GPOR 1.15x · CNX 2.16x ·
MNR 2.23x · CRK **3.39x** · AMPY (0.43x), net cash.

---

## 4. THE SAME-METRIC SUMMARY ROW

| | SD | MNR | GPOR | CRK | CNX |
|---|---:|---:|---:|---:|---:|
| 5-yr avg ROE | 33.9% | *n/comp* | 45.2% (4y) | 12.2% | 8.7% |
| FY2025 ROE | 14.5% | *n/comp* | 24.1% | 16.2% | 15.0% |
| Worst ROE year in window | 12.7% | n/a | (13.5%) | (22.7%) | (12.3%) |
| Loss years in window | **0 of 5** | 0 of 5 | 1 of 4 | 2 of 5 | 3 of 5 |
| Proved reserves, Bcfe | 415 | 4,228 | 4,253 | 7,005 | 9,662 |
| Reserve life, yrs | 10.2 | 18.7 | 11.2 | 15.6 | 15.4 |
| PV-10 per Mcfe | **$1.06** | $0.73 | $0.85 | n/d | $0.71 |
| Organic replacement FY2025 | 108% | **0%** | 185% | 830%\* | 138% |
| Dev capex per Boe FY2025 | $8.74 | $7.17 | $8.35 | $17.97 | **$4.72** |
| FY2025 FCF before acq., $M | +41 | +236 | +276 | **(450)** | +534 |
| Net debt / FY2025 OCF | **(1.1x)** | 2.23x | 1.15x | **3.39x** | 2.16x |

\* re-booking of previously price-excluded PUDs, not discovery.

---

## 5. PEERS NOT OBTAINED, AND WHY: UNRESEARCHED WORK ORDERS

**1. PHX Minerals: NOT OBTAINED. Verdict: no usable US filing in the window.**
PHX does not appear in `https://www.sec.gov/files/company_tickers.json` as of 2026-08-31, which
lists only currently registered exchange-listed tickers. That is consistent with PHX having
ceased to be a public reporting company. **Work order:** if a PHX row is wanted, search EDGAR
full-text by company name ("PHX Minerals", formerly Panhandle Oil & Gas) rather than by ticker,
take its last filed 10-K, and record explicitly that the comparison window ends at that 10-K
rather than at FY2025. Do not carry PHX forward as if it were a live comparable. Note also that
a mineral and royalty company has no lease operating expense and no development capex, so its
ROE and capex-per-Boe are structurally different from SD's anyway; the ranking value is low.

**2. Amplify Energy (AMPY): OBTAINED but DISQUALIFIED as a comparable.**
The data is in the tables above for completeness, but AMPY is not a Mid-Continent gas peer and
should not be ranked against SD:

- It sold its entire natural gas reserve base during 2025 (53,213 MBoe divested). Natural gas
  reserves at 12/31/2025 are **zero**; the book is 93% oil and 7% NGL.
- Its remaining assets are the Beta field offshore California and the Bairoil CO2 flood in
  Wyoming: a different geology, a different cost structure and a different regulatory regime.
- Its FY2021 and FY2022 equity was negative, so two of five ROE years are Not Meaningful.
- Reserve life 5.7 years, the shortest in the set, on a shrinking asset.

**3. Gaps inside the peers that WERE obtained:**

| Gap | Peer | Why | Work order |
|---|---|---|---|
| PV-10 at FY2025 | CRK | Comstock discloses standardized measure only; the phrase "PV-10" does not appear in the FY2025 10-K. The pre-tax 10% discount is not separately disclosed, so PV-10 is not derivable from filed data. | Either accept the after-tax standardized measure ($3,867M) as the comparison basis for CRK and re-run every other peer on the after-tax basis too, or obtain CRK's reserve report exhibit. Do **not** estimate CRK's PV-10 by grossing up. |
| FY2021 ROE | GPOR | Fresh-start reporting at 17 May 2021 splits the year. | Nothing to research; this is an accounting discontinuity, not missing data. Report as `n/c` permanently. |
| FY2021, FY2022 ROE | MNR | Predecessor private-LLC members' equity. | Nothing further to obtain from EDGAR; MNR's first 10-K is for FY2023. |
| Three-year F&D cost | all | This row uses one-year development capex per unit produced, which is noisy. | If the ranking turns on cost, compute a three-year average F&D from the `Costs Incurred` tables in each peer's ASC 932 disclosures; all six filers publish one. Named document, so UNRESEARCHED, not UNKNOWABLE. |
| Lease operating expense per Boe | all | Not pulled in this pass. | Available in every Item 7 operating-data table. UNRESEARCHED. |

---

## 6. WHAT THE ROW SHOWS

SandRidge does **not** have a cost advantage, and its return advantage is one of balance-sheet
construction rather than of rock. On the operating cost line SD is mid-pack and slightly worse
than the closest comparables: FY2025 development capex of $8.74 per Boe produced against $8.35
at Gulfport, $7.17 at Mach and $4.72 at CNX, with only Comstock's $17.97 clearly worse, and
Comstock's is worse because it is appraising a new play, which is a choice rather than an
inefficiency. SD's reserve life of 10.2 years is the shortest of the four real comparables
(MNR 18.7, CRK 15.6, CNX 15.4, GPOR 11.2), and its 415 Bcfe reserve base is roughly one tenth
of Gulfport's and one twenty-third of CNX's, so there is no scale advantage and no duration
advantage. What SD does have is a genuinely different capital structure and a genuinely
different reserve quality per unit: it is the only peer with **zero debt and $113M of net cash**
at 30 June 2026, against $0.9bn to $3.1bn of net debt at the four comparables, and it carries
the **highest PV-10 per Mcfe in the set at $1.06** against $0.85 at Gulfport, $0.73 at Mach and
$0.71 at CNX, which is a function of its NGL and oil cut (16% oil, 35% NGL by volume) rather
than of operating skill. That combination is why SD posted a profit in all five years while CNX
lost money in three of five and Comstock in two of five, and why SD's 33.9% five-year average
ROE sits above Comstock's 12.2% and CNX's 8.7%: SD earns a modest 12.7% to 14.5% on equity in
normal years with no interest expense, while the levered peers swing between large gains and
large losses. Read carefully, the row says SD is the *least fragile* member of the set and the
*least advantaged*. Its FY2021 and FY2022 returns of 62.5% and 66.1% were a gas-price event plus
a $64.5M deferred-tax release, not a repeatable franchise, and the FY2023 to FY2025 run of
12.7%, 13.6% and 14.5% on an unlevered balance sheet is the honest steady-state number. The one
structural point worth carrying into Q2 is that **SD's 108% organic reserve replacement in
FY2025 was drilled, not bought**, which is more than can be said for Mach, the nearest
structural comparable, whose own 10-K states it had *no extensions or discoveries in 2025* and
which grew reserves 109% in one year almost entirely by purchase in place while adding $1.1bn of
net debt to do it.
