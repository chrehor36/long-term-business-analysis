# MTDR COMPETITOR ROW — Permian Resources (PR) · Devon Energy (DVN) · Diamondback (FANG)
### FY2025 (calendar year ended 2025-12-31), filing-sourced

Built for Q2 of the framework ("Is it a franchise? — *requires the competitor row, a moat is a
relative claim*"). This file is **evidence only**. It carries no verdict and no entry language.

**COMPUTATION — NOT A CLEARANCE.**

---

## 0. DOCUMENTS READ

Every number below traces to one of these six primary documents, fetched from SEC EDGAR
(`https://www.sec.gov/Archives/edgar/data/…`, `User-Agent: Chris Hrehor chrehor36@gmail.com`).
Converted to text and saved alongside this file.

| Filer | CIK | Form | Period | Filed | Accession no. | Primary document | Local text |
|---|---|---|---|---|---|---|---|
| Permian Resources Corp | 0001658566 | 10-K | 2025-12-31 | 2026-02-26 | **0001658566-26-000035** | `pr-20251231.htm` | `PR_10K_FY2025.txt` |
| Permian Resources Corp | 0001658566 | 10-Q | 2026-06-30 | 2026-08-06 | **0001658566-26-000101** | `pr-20260630.htm` | `PR_10Q_Q2_2026.txt` |
| Devon Energy Corp | 0001090012 | 10-K | 2025-12-31 | 2026-02-18 | **0001193125-26-056485** | `dvn-20251231.htm` | `DVN_10K_FY2025.txt` |
| Devon Energy Corp | 0001090012 | 10-Q | 2026-06-30 | 2026-08-05 | **0001193125-26-334340** | `dvn-20260630.htm` | `DVN_10Q_Q2_2026.txt` |
| Diamondback Energy, Inc. | 0001539838 | 10-K | 2025-12-31 | 2026-02-25 | **0001539838-26-000010** | `fang-20251231.htm` | `FANG_10K_FY2025.txt` |
| Diamondback Energy, Inc. | 0001539838 | 10-Q | 2026-06-30 | 2026-08-05 | **0001539838-26-000142** | `fang-20260630.htm` | `FANG_10Q_Q2_2026.txt` |

Accession numbers were taken from `https://data.sec.gov/submissions/CIK##########.json` for
each CIK. No aggregator was used for any figure in this file.

**Gas-to-oil conversion.** All three filers convert **6 Mcf of natural gas = 1 Boe**, stated
verbatim in each filing:
- PR 10-K, Item 1, footnote (1) to the proved-reserve table: *"Calculated by converting natural
  gas to oil equivalent barrels at a ratio of six Mcf of natural gas to one Boe."*
- DVN 10-K, Note 22 supplemental, footnote (1) to the proved-reserve table: *"Gas reserves are
  converted to Boe at the rate of six Mcf per Bbl of oil… NGL reserves are converted to Boe on a
  one-to-one basis with oil."*
- FANG uses MBOE throughout with the same 6:1 basis implied by its reserve table columns
  (Oil MBbls / Natural Gas MMcf / NGL MBbls / Total MBOE); the arithmetic of every row in that
  table reconciles at 6:1 (checked below).

---

## 1. PROVED RESERVES AT 2025-12-31, PRODUCTION, AND RESERVE LIFE

| | **PR** | **DVN** | **FANG** |
|---|---|---|---|
| Total proved (MMBoe) | **1,116.3** | **2,428** | **3,617.9** |
| Proved developed (MMBoe) | 794.1 | 1,844 | 2,521.0 |
| Proved undeveloped (MMBoe) | 322.2 | 584 | 1,096.8 |
| PD as % of total | 71% (as disclosed) | 75.9% (computed) | 69.7% (computed) |
| FY2025 production (MMBoe) | **143.311** | **307** | **336.178** |
| Oil as % of production | 46.3% (computed) | 46.3% (computed) | 54.0% (computed) |
| **R/P, total proved (yrs)** | **7.79** | **7.91** | **10.76** |
| **R/P, proved developed (yrs)** | **5.54** | **6.01** | **7.50** |

**Source of each figure.**

- **PR** — 10-K Item 1 & 2, "Proved Oil and Gas Reserves" table: Total proved 1,116,298 MBoe;
  proved developed 794,095 MBoe; proved undeveloped 322,203 MBoe; PD 71% / PUD 29% stated on the
  face of the table. Production from Item 1 & 2 "Production" table: 143,311 MBoe (oil 66,364
  MBbls, NGL 35,773 MBbls, gas 247,045 MMcf). Both tables repeated in Item 8, Supplemental
  Information About Oil & Natural Gas Producing Activities.
- **DVN** — 10-K Note 22, "Supplemental Information on Oil and Gas Operations (Unaudited)",
  "Proved Reserves" table: Dec 31 2025 — oil 961 MMBbls, gas 4,482 Bcf, NGL 720 MMBbls, combined
  **2,428 MMBoe**; proved developed 1,844 MMBoe; proved undeveloped 584 MMBoe. Production of
  **307 MMBoe** is the production line of that same rollforward. Cross-check against MD&A Item 7
  production table: total **840 MBoe/d** × 365 = 306.6 MMBoe. Consistent.
- **FANG** — 10-K Note 18 "Supplemental Information on Oil and Natural Gas Operations
  (Unaudited)", proved-reserve rollforward: as of Dec 31 2025 — oil 1,774,420 MBbls, gas
  5,273,821 MMcf, NGL 964,466 MBbls, **total 3,617,856 MBOE**; proved developed 2,521,028 MBOE;
  proved undeveloped 1,096,828 MBOE. Production of **336,178 MBOE** from the same rollforward and
  from Item 1 & 2 "Oil and Natural Gas Production and Price History" (Midland 309,335 + Delaware
  25,692 + Other 1,151).

**Arithmetic.**

```
PR    R/P      = 1,116.298 / 143.311 = 7.789 yrs      PD R/P = 794.095 / 143.311 = 5.541 yrs
DVN   R/P      = 2,428     / 307     = 7.909 yrs      PD R/P = 1,844   / 307     = 6.007 yrs
FANG  R/P      = 3,617.856 / 336.178 = 10.762 yrs     PD R/P = 2,521.028 / 336.178 = 7.499 yrs
```

**6:1 conversion check (FANG total proved, to prove the 6 Mcf = 1 Boe basis):**
```
1,774,420 + 964,466 + (5,273,821 / 6) = 1,774,420 + 964,466 + 878,970 = 3,617,856 MBOE  ✓
```

---

## 2. COSTS INCURRED FOR OIL AND GAS PRODUCING ACTIVITIES, FY2025

From the Supplemental Oil and Gas Disclosures of each 10-K.

| ($ millions) | **PR** | **DVN** | **FANG** |
|---|---|---|---|
| Property acquisition — proved | 567.9 | 138 | 4,608 |
| Property acquisition — unproved | 513.3 | 224 | 5,226 |
| Exploration | 18.6 | 581 | 212 |
| Development | 1,811.6 | 3,057 | 3,613 |
| **Total costs incurred** | **2,911.4** | **4,000** | **13,659** |

- **PR** — Item 8, Supplemental Information About Oil & Natural Gas Producing Activities, "Costs
  Incurred for Oil and Natural Gas Producing Activities" ($ thousands: 567,919 / 513,268 / 18,648
  / 1,811,551 / total 2,911,386). Footnote (2): development costs exclude wells in progress at
  year-end, which were **$542.2 million** at 2025-12-31. Footnote (3): exploration "includes all
  exploratory expenses, including dry hole costs."
- **DVN** — Note 22, "Costs Incurred" table ($ millions, as printed). Devon's note states
  *"Development costs in the table above includes additions and revisions to Devon's asset
  retirement obligations."*
- **FANG** — Note 18, "Costs Incurred in Oil and Natural Gas Activities" ($ millions, as printed).
  FANG uses the **full cost method**, so its "exploration costs" are capitalised, not expensed;
  PR uses **successful efforts** and DVN uses **successful efforts**. This is a real
  non-comparability in the exploration line.

---

## 3. RESERVE ROLLFORWARD, FY2025

| (MMBoe) | **PR** | **DVN** | **FANG** |
|---|---|---|---|
| Opening balance 2024-12-31 | 1,026.957 | 2,155 | 3,557.416 |
| Revisions to previous estimates | **(36.889)** | **+134** (see split) | **(304.085)** |
|  — of which price revisions | (26.3) stated in narrative | (16) | (130.101) stated in narrative |
|  — of which other than price | see narrative | +150 | see narrative |
| Purchases / acquisitions of minerals in place | **+40.915** | **+43** | **+188.609** |
| Extensions and discoveries | **+228.626** | **+443** | **+578.919** |
| Divestitures / sale of reserves | — (none in 2025) | (40) | (66.825) |
| Production | **(143.311)** | **(307)** | **(336.178)** |
| **Closing balance 2025-12-31** | **1,116.298** | **2,428** | **3,617.856** |

**Rollforward reconciliation (each computed and checked against the filed closing balance):**
```
PR    1,026.957 + 228.626 - 36.889 + 40.915 - 143.311                 = 1,116.298  ✓
DVN   2,155     - 16 + 150 + 443 + 43 - 307 - 40                      = 2,428      ✓
FANG  3,557.416 + 578.919 - 304.085 + 188.609 - 66.825 - 336.178      = 3,617.856  ✓
```

**Narrative detail carried in the filings.**

- **PR** (10-K, Item 8 supplemental, "Notable changes in proved reserves for the year ended
  December 31, 2025"): E&D of 228.6 MMBoe comprised 142.7 MMBoe of new PUD reserves and 85.9
  MMBoe of unproved locations converted to new PDP wells. Revisions of (36.9) MMBoe = (36.0)
  PUD reclassified/removed on development-plan change, (26.3) from lower average commodity
  prices, offset by +25.4 timing and performance. PUD-to-PD conversion rate **30%**; PR spent
  **$772.5 million** converting 84.3 MMBoe of PUD to PD.
- **DVN** (Note 22): of the 443 MMBoe of E&D, **278 MMBoe were in the Delaware Basin**, 81 in the
  Rockies, 51 in Eagle Ford, 33 in the Anadarko Basin. PUD conversions of 175 MMBoe cost
  approximately **$1.1 billion**. Price revisions of (16) MMBoe.
- **FANG** (Note 18): E&D of 578,919 MBOE came from **1,571 new wells, of which 1,311 are wells
  in which the Company owns only a mineral interest through Viper**, plus 582 new PUD locations.
  *"Viper royalty interests accounted for 11% of the extension volumes."* Revisions of (304,085)
  MBOE = (130,101) lower commodity prices, (128,883) development-plan downgrades, (45,101)
  performance. Purchases of 188,609 MBOE = 90,340 from the Double Eagle Acquisition and 98,269
  of Viper royalty purchases (largely Viper's Sitio Acquisition). PUD transfers to developed of
  360,141 MBOE, on approximately **$3.6 billion** of 2025 capital.

---

## 4. RESERVE REPLACEMENT AND FINDING COSTS — COMPUTED

Three ratios, each computed from the numbers in sections 2 and 3 above. Formulas are the ones
specified in the work order.

### 4a. Organic reserve replacement % = extensions & discoveries ÷ production

```
PR    228.626 / 143.311 = 1.5953  →  159.5%
DVN   443     / 307     = 1.4430  →  144.3%
FANG  578.919 / 336.178 = 1.7220  →  172.2%
```

### 4b. Drill-bit F&D cost per Boe = (exploration + development costs) ÷ extensions & discoveries

```
PR    (18.648 + 1,811.551) / 228.626  = 1,830.199 / 228.626 =  $8.01 /Boe
DVN   (581    + 3,057)     / 443      = 3,638     / 443     =  $8.21 /Boe
FANG  (212    + 3,613)     / 578.919  = 3,825     / 578.919 =  $6.61 /Boe
```

### 4c. All-in F&D&A per Boe = total costs incurred ÷ (E&D + acquisitions + revisions)

Revisions enter with their sign. All three were negative in 2025, so all three denominators are
reduced.

```
PR    denominator = 228.626 + 40.915 + (-36.889)  =  232.652 MMBoe
      2,911.386 / 232.652   =  $12.51 /Boe

DVN   denominator = 443 + 43 + (+134)             =  620 MMBoe
      [DVN revisions = -16 price +150 other than price = +134, the only 2025 revisions positive
       in the set]
      4,000 / 620           =   $6.45 /Boe

FANG  denominator = 578.919 + 188.609 + (-304.085) = 463.443 MMBoe
      13,659 / 463.443      =  $29.47 /Boe
```

**Read these three numbers with the caveats in section 12, not on their own.** In particular:
FANG's $29.47 all-in is dominated by $9,834M of 2025 acquisition spend (Double Eagle + Viper's
Sitio) against a denominator cut by a 304 MMBoe downward revision; and FANG's $6.61 drill-bit
number is flattered because 1,311 of the 1,571 wells behind its extensions are royalty-only
wells drilled at somebody else's cost. DVN's $6.45 all-in is flattered in the opposite direction
by a rare **positive** revision year (+134 MMBoe) against near-zero acquisition spend.

---

## 5. PV-10 AND STANDARDIZED MEASURE AT 2025-12-31, AND THE SEC PRICE DECK

| ($ millions) | **PR** | **DVN** | **FANG** |
|---|---|---|---|
| Future cash inflows | 38,611.5 | 81,155 | 140,499 |
| Future development costs | (4,253.8) | (6,035) | (9,425) |
| Future production costs | (18,026.3) | (38,022) | (40,789) + (9,870) prod. taxes |
| Future income tax expenses | (1,787.5) | (5,653) | (12,129) |
| Future net cash flows | 14,543.9 | 31,445 | 68,286 |
| 10% discount | (6,178.4) | (12,680) | (31,376) |
| **Standardized measure** | **8,365.5** | **18,765** | **36,910** |
| **PV-10 (pre-tax)** | **9,439.3 — DISCLOSED** | **not disclosed** | **not disclosed** |

- **PR** discloses PV-10 on the face of the Item 1 & 2 reserve table as *"Total proved pre-tax
  PV 10%"* = **$9,439.3 million**, with the reconciliation printed directly above it
  (standardized measure $8,365.5M + discounted future income tax expense $1,073.8M). Footnote (2)
  labels Pre-tax PV 10% *"a supplemental non-GAAP financial measure as defined by the U.S.
  Securities and Exchange Commission."*
- **DVN** — **PV-10 is not disclosed.** Searched: Item 1 & 2 (Properties / Proved Reserves), Item
  7 MD&A, Note 22 Supplemental Information. The string "PV-10", "PV 10" and "pre-tax present
  value" do not appear anywhere in the 10-K. Devon discloses only the standardized measure of
  **$18,765 million**. It cannot be backed into from the filing, because only the *undiscounted*
  future income tax expense ($5,653M) is given, not its discounted amount.
- **FANG** — **PV-10 is not disclosed.** Same search across Item 1 & 2, Item 7 and Note 18;
  "PV-10" / "PV 10" / "pre-tax present value" do not appear in the 10-K. Standardized measure of
  **$36,910 million** only, and again the future income tax expense ($12,129M) is undiscounted.

### SEC price deck

| | **PR** | **DVN** | **FANG** |
|---|---|---|---|
| Benchmark oil ($/Bbl) | **$66.01** (WTI Posted) | **not disclosed** | **not disclosed** (see note) |
| Benchmark gas ($/MMBtu) | **$3.39** (Henry Hub spot) | **not disclosed** | **not disclosed** (see note) |
| Realized/differential-adjusted oil ($/Bbl) | 64.69 | 62.67 | 64.99 |
| Realized/differential-adjusted gas ($/Mcf) | 0.75 | 1.32 | 1.32 |
| Realized/differential-adjusted NGL ($/Bbl) | 20.58 | 20.85 | 18.87 |

- **PR** states the benchmark deck verbatim in Item 1A Risk Factors: *"Our estimated proved
  reserves as of December 31, 2025, and related standardized measure were calculated under rules
  of the SEC using twelve-month trailing average benchmark prices of $66.01 per barrel of oil
  (WTI Posted) and $3.39 per MMBtu (Henry Hub spot)."* The differential-adjusted prices
  ($64.69 / $20.58 / $0.75) are the weighted-average sales prices in the Item 8 supplemental
  disclosure.
- **DVN** gives only the assumed realized prices, in Note 22: *"For 2025 estimates, Devon's future
  realized prices were assumed to be $62.67 per Bbl of oil, $1.32 per Mcf of gas and $20.85 per
  Bbl of NGLs."* No benchmark WTI or Henry Hub deck is stated anywhere in the 10-K.
- **FANG** defines *"SEC Prices"* in its glossary as the *"Unweighted arithmetic average of the
  first-day-of-the-month price for each month during the 12-month period"* and then gives, in
  Note 18, only *"the SEC Prices **as adjusted for differentials and contractual arrangements**"*
  — oil $64.99/Bbl, gas $1.32/Mcf, NGL $18.87/Bbl. Separately, in Item 7A, FANG states *"During
  2025, 2024 and 2023, WTI prices averaged $64.73, $75.76 and $77.60 per Bbl, respectively, and
  Henry Hub prices averaged $3.62, $2.41 and $2.66 per MMBtu, respectively."* **That sentence is
  a market-conditions statement and is not labelled as the SEC deck** — it is a calendar-year
  average, not stated to be the first-day-of-the-month 12-month average. It is recorded here
  because the work order asked for the deck, but it must not be treated as FANG's SEC deck.

**Note on FANG's 2025 impairment, which the price deck drives.** FANG recorded a **$3,652 million
non-cash ceiling-test impairment** in FY2025, and says in Item 7: *"Given the overall decline in
SEC Prices from the first quarter of 2025 through the first two months of 2026, we believe an
additional material non-cash impairment of our assets is reasonably likely to occur in the first
quarter of 2026."* PR (successful efforts) recorded no impairment: *"The impairment test performed
by the Company indicated that no impairment occurred during the years ended December 31, 2025,
2024 and 2023."* DVN recorded $254M of asset impairments in FY2025.

---

## 6. PER-UNIT OPERATING COSTS, FY2025

| ($/Boe) | **PR** | **DVN** | **FANG** |
|---|---|---|---|
| **Lease operating expense** | **5.26** (disclosed) | **6.27** (disclosed) | **5.55** (disclosed) |
| Severance / production & ad valorem taxes | 2.72 (disclosed) | 6.7% of sales (disclosed as %) | 2.53 (computed) |
| Gathering, processing & transportation | 1.40 (disclosed) | 2.71 (disclosed) | 1.53 (computed) |
| **DD&A** | **14.18** (disclosed) | **11.35** (disclosed, O&G only) / 11.71 (computed, consolidated) | **14.99** (disclosed, incl. accretion) / 14.60 (disclosed, depletion only) |

- **PR** — Item 1 & 2 "Production" table, "Operating costs per Boe": LOE $5.26, severance and ad
  valorem $2.72, GP&T $1.40. DD&A per Boe $14.18 from the Item 7 MD&A DD&A table
  (*"DD&A per Boe was $14.18 for the year ended December 31, 2025 compared to $14.13 for the
  same period in 2024"*). Cross-check: $753,119k LOE ÷ 143,311 MBoe = $5.255 ✓ ;
  $2,032,507k DD&A ÷ 143,311 MBoe = $14.18 ✓
- **DVN** — Item 7 MD&A, "Production Expenses" table, "Per Boe": LOE **$6.27**, GP&T **$2.71**,
  production taxes given only as **6.7% of oil, gas and NGL sales** (not as a $/Boe). DD&A per
  Boe of **$11.35** is from the Note 22 "Results of Operations" schedule and is the *oil-and-gas
  producing-activities* DD&A ($3,479M) only. Consolidated DD&A of $3,595M ÷ 307 MMBoe =
  **$11.71/Boe** — computed here, and stated as computed.
- **FANG** — Item 7 MD&A: LOE $1,865M / **$5.55 per BOE**; *"Oil and natural gas properties
  depletion rate per BOE $14.60"* and *"Depreciation, depletion, amortization and accretion per
  BOE $14.99"*. FANG also summarises: *"Our cash operating costs were $10.23 per BOE, including
  lease operating expenses of $5.55 per BOE, cash general and administrative expenses of $0.62
  per BOE and production and ad valorem taxes and gathering, processing and transportation
  expenses of $4.06 per BOE."* The $2.53 and $1.53 rows above are **computed** by me from the
  income statement ($851M taxes and $515M GP&T ÷ 336.178 MMBoe) because FANG discloses those two
  only combined at $4.06/BOE.

---

## 7. OPERATING MARGIN, FY2025

| ($ millions) | **PR** | **DVN** | **FANG** |
|---|---|---|---|
| Total revenues (line used) | 5,065.2 *(Oil and gas sales)* | 17,188 *(Total revenues)* | 15,026 *(Total revenues)* |
| Operating income (line used) | 1,462.7 *(Income from operations)* | 3,921 *(derived — see below)* | 1,266 *(Income (loss) from operations)* |
| **Operating margin** | **28.88%** | **22.81%** | **8.43%** |

**Exact line items and arithmetic.**

- **PR** — Consolidated Statements of Operations. PR's revenue block contains a single line,
  "Oil and gas sales" $5,065,211k; there is no total-revenues subtotal because there is only one
  line. "Income from operations" of $1,462,729k is printed on the face of the statement.
  ```
  1,462,729 / 5,065,211 = 0.2888  →  28.88%
  ```
- **DVN** — Consolidated Statements of Comprehensive Earnings. **Devon does not print an operating
  income subtotal.** Its "Total expenses" of $13,722M *includes* "Financing costs, net" of $455M.
  I therefore derive operating income by adding financing costs back:
  ```
  Operating income = Total revenues 17,188 - (Total expenses 13,722 - Financing costs, net 455)
                   = 17,188 - 13,267 = 3,921
  3,921 / 17,188 = 0.2281  →  22.81%
  ```
  This is a **derived** figure and is labelled as such. Devon's revenue line includes $5,563M of
  "Marketing and midstream revenues" carried against $5,635M of "Marketing and midstream
  expenses" — a **loss-making pass-through** that inflates the denominator. Computed
  supplementary view, excluding marketing entirely:
  ```
  (3,921 + 72) / (17,188 - 5,563) = 3,993 / 11,625 = 0.3435  →  34.35%  [COMPUTED, not disclosed]
  ```
- **FANG** — Consolidated Statements of Operations. "Total revenues" $15,026M; "Income (loss) from
  operations" $1,266M printed on the face.
  ```
  1,266 / 15,026 = 0.0843  →  8.43%
  ```
  This margin is depressed by the **$3,652M ceiling-test impairment** inside "Total costs and
  expenses". Computed supplementary view, adding the impairment back:
  ```
  (1,266 + 3,652) / 15,026 = 4,918 / 15,026 = 0.3273  →  32.73%  [COMPUTED, not disclosed]
  ```
  FANG's denominator also contains $1,476M of "Sales of purchased oil" carried against $1,474M of
  "Purchased oil expense" — another near-zero-margin pass-through.

**The three headline margins are not comparable as printed.** PR's denominator is pure wellhead
sales; DVN's carries $5.6bn of marketing throughput; FANG's numerator carries a $3.7bn impairment
and its denominator $1.5bn of purchased-oil resale. This is exactly the kind of line that must not
be read across without the adjustment shown.

---

## 8. DEBT, CASH, NET DEBT AND LEVERAGE

### At 2025-12-31

| ($ millions) | **PR** | **DVN** | **FANG** |
|---|---|---|---|
| Total debt | **3,545.6** | **8,389** | **14,489** |
|  — of which current | none | 998 | 763 |
|  — of which long-term | 3,545.6 | 7,391 | 13,726 |
| Cash | **153.7** | **1,384** (+50 restricted = 1,434) | **104** |
| **Net debt** | **3,391.9** | **6,955** | **14,385** |
| FY2025 operating cash flow (filed line) | **3,607.5** | **6,711** | **8,758** |
| **Net debt ÷ FY2025 OCF** | **0.94×** | **1.04×** | **1.64×** |
| Company-reported Adjusted EBITDA | **none in the 10-K** | **EBITDAX $7,413** (company non-GAAP) | **none in the 10-K** |
| Net debt ÷ company non-GAAP | n/a | **0.94×** | n/a |

**Arithmetic.**
```
PR    net debt = 3,545,598 - 153,690 = 3,391,908 ($000)
      3,391,908 / 3,607,541 = 0.940×
DVN   net debt = 8,389 - 1,434 (cash + restricted cash, the balance-sheet caption) = 6,955
      6,955 / 6,711  = 1.036×      6,955 / 7,413 (EBITDAX) = 0.938×
      [using cash and equivalents alone, 8,389 - 1,384 = 7,005, giving 1.044×]
FANG  net debt = 14,489 - 104 = 14,385
      14,385 / 8,758 = 1.642×
```

**Line items used.**
- **PR** — Balance sheet: "Cash and cash equivalents" $153,690k; "Long-term debt, net" $3,545,598k.
  There is **no current portion of long-term debt** on PR's balance sheet. Note 7 shows Senior
  Notes, net of $3,545,598k (face $3,575,000k across the 8.00% 2027, 5.875% 2029, 9.875% 2031,
  7.00% 2032 and 6.25% 2033 notes, less $24,405k issuance costs and $4,997k discount). The
  revolving Credit Agreement had a $4.0bn borrowing base, $2.5bn elected commitments and **no
  borrowings outstanding** at 2025-12-31. Cash flow statement: "Net cash provided by operating
  activities" $3,607,541k. **PR does not present an Adjusted EBITDA or EBITDAX in the 10-K** —
  "EBITDAX" appears only as a defined term in the Credit Agreement leverage covenant (total
  funded debt to consolidated EBITDAX, not greater than 3.5 to 1.0).
- **DVN** — Note 15 Debt: "Total debt $8,389", "Less amount classified as short-term debt 998",
  "Total long-term debt $7,391". Balance sheet caption is "Cash, cash equivalents and restricted
  cash" $1,434M, reconciled in the cash-flow statement to cash and equivalents $1,384M plus
  restricted cash $50M. Cash flow statement: "Net cash from operating activities" $6,711M. Item 7
  MD&A: *"At December 31, 2025, we had total debt of $8.4 billion. $7.4 billion of this debt was
  comprised of debentures and notes that have fixed interest rates which average 5.7%."* Devon's
  own non-GAAP: **EBITDAX (Non-GAAP) $7,413M** for FY2025, defined in Item 7 as *"net earnings
  before income tax expense; financing costs, net; exploration expenses; DD&A; asset impairments;
  asset disposition gains and losses; non-cash share-based compensation; non-cash valuation
  changes for derivatives and financial instruments; accretion on discounted liabilities; and
  other items not related to our normal operations."*
- **FANG** — Note 8 Debt: "Total debt, net $14,489", "Less: current maturities of debt 763",
  "Total long-term debt $13,726". Balance sheet: "Cash and cash equivalents ($13 million related
  to Viper) $104". Cash flow statement: "Net cash provided by (used in) operating activities"
  $8,758M. **FANG presents no Adjusted EBITDA or EBITDAX anywhere in the 10-K** (the strings do
  not appear).

### At 2026-06-30 (most recent 10-Q)

| ($ millions) | **PR** | **DVN** | **FANG** |
|---|---|---|---|
| Total debt | **2,993.1** | **11,388** | **12,614** |
| Cash | **131.7** | **1,009** (incl. restricted) | **462** |
| **Net debt** | **2,861.3** | **10,379** | **12,152** |
| Change in net debt vs 2025-12-31 | **−530.6** | **+3,424** | **−2,233** |

- **PR** 10-Q Note: "Senior Notes, net 2,993,050 / Total long-term debt, net $2,993,050"; balance
  sheet cash $131,722k. No current maturities.
- **DVN** 10-Q Note: "Total debt $11,388 / Less amount classified as short-term debt 1,497 /
  Total long-term debt $9,891"; balance sheet "Cash, cash equivalents and restricted cash $1,009".
  Item 7: *"At June 30, 2026, we had total debt of $11.4 billion."* **The increase is the Coterra
  merger**, which closed May 2026: the 10-Q debt note footnote reads *"These instruments were
  assumed by Devon in May 2026 in conjunction with the Merger. Approximately $277 million and $27
  million of these instruments remain the unsecured and unsubordinated obligations of Coterra and
  Coterra Energy Operating Co., respectively, each of which is a subsidiary of Devon."*
- **FANG** 10-Q Note: "Total debt, net 12,614 / Less: current maturities of debt 1,548 / Total
  long-term debt $11,066"; balance sheet "Cash and cash equivalents ($77 million related to Viper)
  $462". Item 7: *"At June 30, 2026, we had approximately $3.4 billion of liquidity consisting of
  $385 million in standalone cash and cash equivalents and $3.0 billion available under our credit
  facility. At June 30, 2026, we had approximately $1.5 billion of senior notes maturing in the
  next 12 months."*

---

## 9. NET INCOME — PARENT VS NON-CONTROLLING INTERESTS

| ($ millions, FY2025) | **PR** | **DVN** | **FANG** |
|---|---|---|---|
| Net income (consolidated) | 1,098.9 | 2,681 | 1,547 |
| **Less: attributable to NCI** | **(163.8)** | **(39)** | **+117** *(NCI booked a loss)* |
| **Attributable to the parent** | **935.2** | **2,642** | **1,664** |
| NCI equity on the balance sheet | 1,255.6 | not separately captioned in the extract read | 5,995 |
| NCI structure | 10% of OpCo | small midstream/other NCI | **Viper Energy — 57% NCI** |

- **PR** — "Less: Net income attributable to noncontrolling interest (163,762)"; "Net income
  attributable to Class A Common Stock $935,174". Note 10: *"As of December 31, 2025, the
  noncontrolling interest ownership of OpCo had decreased to 10% from 12% as of December 31, 2024
  and 30% as of December 31, 2023."* The reserve footnote: *"Includes total proved reserves of
  112,652 MBoe … attributable to a consolidated subsidiary in which there was a 10% …
  noncontrolling interest"* — i.e. **10.1% of PR's 1,116.3 MMBoe headline is not PR's**.
  Standardized-measure footnote: $844.2M of the $8,365.5M is attributable to that NCI.
- **DVN** — "Net earnings attributable to noncontrolling interests 39"; "Net earnings attributable
  to Devon $2,642". Devon's NCI is immaterial at 1.5% of net earnings.
- **FANG** — "Net income (loss) attributable to non-controlling interest (117)"; "Net income (loss)
  attributable to Diamondback Energy, Inc. $1,664" — the NCI absorbed a loss in 2025, so the
  parent's number is *larger* than consolidated net income. Note 18 footnote: *"Includes total
  proved reserves of 231,440 MBOE … as of December 31, 2025 … attributable to the non-controlling
  interest in Viper"* — **6.4% of FANG's 3,617.9 MMBoe headline is not FANG's**. Standardized
  measure footnote: *"Includes $6.6 billion … attributable to the Company's consolidated
  subsidiary, Viper, in which there is a 57% … non-controlling interest at December 31, 2025"* —
  i.e. **17.9% of FANG's $36,910M standardized measure sits behind a 57% minority**. Balance-sheet
  NCI equity of $5,995M is 14.0% of FANG's $42,967M total equity.

---

## 10. CORPORATE BASE DECLINE RATE

**No instance found in the documents read.**

None of the three filers discloses a corporate or base annual decline rate percentage. Searched:
all six documents in section 0, for every sentence containing "declin*" together with a numeric
percentage, plus targeted searches for "base decline", "corporate decline", "decline rate" and
"annual decline". What exists is qualitative only:

- **PR** — 10-K critical accounting estimates: *"…include estimates of: (i) oil and gas reserves;
  (ii) future production decline rates; (iii) future operating and development costs…"* — an input
  named, no rate given. The only percentage-bearing "decline" sentence in PR's 10-K is a
  change-of-control **ratings** decline covenant, not a production decline.
- **DVN** — 10-K Item 1A: *"The production rates from oil and gas properties generally decline as
  reserves are depleted… our current development activity is focused on unconventional oil and gas
  assets, which generally have significantly higher decline rates as compared to conventional
  assets."* No figure. The only percentage-bearing "decline" sentence in DVN's 10-K is a **price**
  decline ("an approximately 14% decline" in an oil price comparison).
- **FANG** — 10-K critical audit matter: *"…forecasting the timing and volumetric amounts of
  production and corresponding decline rate of producing properties associated with the Company's
  development plan."* No figure. **Zero** percentage-bearing "decline" sentences in FANG's 10-K.

The document that would resolve this is a company investor presentation or an analyst-day deck —
**not a filed document**, and therefore outside the citation shelf for this row. Under the
framework's own test — *"Can I name the document that would resolve this?"* — the honest answer
for a **filing-sourced** row is no. **UNKNOWABLE from the filings.**

---

## 11. THE ROW — SUMMARY

| Metric | **PR** | **DVN** | **FANG** | Source class |
|---|---|---|---|---|
| Total proved (MMBoe) | 1,116.3 | 2,428 | 3,617.9 | disclosed |
| Proved developed (MMBoe) | 794.1 | 1,844 | 2,521.0 | disclosed |
| FY2025 production (MMBoe) | 143.3 | 307 | 336.2 | disclosed |
| R/P (yrs) | 7.79 | 7.91 | 10.76 | computed |
| PD R/P (yrs) | 5.54 | 6.01 | 7.50 | computed |
| Organic reserve replacement % | 159.5% | 144.3% | 172.2% | computed |
| Drill-bit F&D ($/Boe) | 8.01 | 8.21 | 6.61 | computed |
| All-in F&D&A ($/Boe) | 12.51 | 6.45 | 29.47 | computed |
| LOE ($/Boe) | 5.26 | 6.27 | 5.55 | disclosed |
| DD&A ($/Boe) | 14.18 | 11.35 | 14.99 | disclosed |
| Operating margin (as printed) | 28.9% | 22.8% (derived) | 8.4% | see §7 |
| Operating margin (adjusted, computed) | 28.9% | 34.4% ex-marketing | 32.7% ex-impairment | computed |
| Total costs incurred ($M) | 2,911 | 4,000 | 13,659 | disclosed |
| PV-10 ($M) | 9,439 | not disclosed | not disclosed | — |
| Standardized measure ($M) | 8,366 | 18,765 | 36,910 | disclosed |
| Total debt 2025-12-31 ($M) | 3,546 | 8,389 | 14,489 | disclosed |
| Cash 2025-12-31 ($M) | 154 | 1,434 | 104 | disclosed |
| Net debt ($M) | 3,392 | 6,955 | 14,385 | computed |
| FY2025 OCF ($M) | 3,608 | 6,711 | 8,758 | disclosed |
| Net debt / OCF | 0.94× | 1.04× | 1.64× | computed |
| Net debt / co. non-GAAP EBITDA(X) | n/a | 0.94× | n/a | computed off co. figure |
| Net debt 2026-06-30 ($M) | 2,861 | 10,379 | 12,152 | computed |
| Net income to parent ($M) | 935 | 2,642 | 1,664 | disclosed |
| Net income to NCI ($M) | 164 | 39 | (117) | disclosed |
| Base decline rate | not disclosed | not disclosed | not disclosed | — |

---

## 12. COMPARABILITY — REQUIRED CAVEATS

**These three are not the same business, and the row must not be read as if they were.**

1. **Permian Resources is the closest Delaware Basin comparable.** PR's acreage is 481,752 net
   acres in the Permian Basin, and its 2025 extensions came *"primarily in the various Bone Spring
   and Wolfcamp formations on the Company's acreage in the Permian Basin"* — its 2023 language
   named the Delaware Basin specifically. PR is a single-basin, working-interest operator with no
   marketing throughput and no royalty vehicle. Its printed numbers are the ones that read across
   to a Delaware pure play with least adjustment.

2. **Devon is multi-basin, NOT a Delaware pure play.** From the Item 7 production table:
   Delaware Basin 493 MBoe/d of 840 MBoe/d total = **58.7%**; Rockies 195 (23%), Anadarko 83
   (10%), Eagle Ford 65 (8%), Other 4. Roughly two-fifths of Devon is outside the Delaware. Devon
   also **does not disclose proved reserves by basin** in the 10-K (only production and extensions
   by basin), so the Delaware share of its 2,428 MMBoe cannot be isolated from the filing. Devon
   further carries $5,563M of marketing and midstream revenue against $5,635M of marketing and
   midstream expense — a loss-making pass-through with no analogue at PR. **And Devon closed its
   merger with Coterra in May 2026**, so the FY2025 entity in this row no longer exists in the
   same form; the Q2 2026 debt figure ($11,388M vs $8,389M) already reflects the assumed Coterra
   instruments.

3. **Diamondback is Midland-weighted, and consolidates a royalty company.** From Item 1 & 2:
   Midland Basin 309,335 MBOE of 336,178 MBOE = **92.0%** of FY2025 production; Delaware Basin
   25,692 MBOE = **7.6%**. FANG is not a Delaware comparable at all. Two further structural
   differences:
   - **Viper.** FANG consolidates Viper Energy, a minerals and royalty company in which there is a
     **57% non-controlling interest**. 231,440 MBOE of FANG's proved reserves and $6.6bn of its
     standardized measure belong to that minority. Critically for the F&D lines: of the 1,571
     wells behind FANG's 578,919 MBOE of 2025 extensions, **1,311 are wells in which FANG owns
     only a mineral interest through Viper**, and Viper royalty interests are *"11% of the
     extension volumes."* Royalty barrels arrive with **no drilling capital attached**, which
     mechanically depresses FANG's drill-bit F&D relative to a pure working-interest operator.
     PR's 10% OpCo NCI is a different animal — it is a share of the same operated assets, not a
     different business.
   - **Full cost vs successful efforts.** FANG uses the **full cost method**; PR and DVN use
     **successful efforts**. That drives the $3,652M ceiling-test impairment in FANG's FY2025
     operating income (PR took none, DVN took $254M), changes what "exploration costs" means in
     the costs-incurred table, and makes the DD&A rates only loosely comparable.

4. **The F&D ratios are the most fragile numbers in this row.** All three formulas are one-year
   ratios of a lumpy numerator over a lumpy denominator. FANG's all-in $29.47 is driven by $9,834M
   of 2025 M&A (Double Eagle + Viper's Sitio) landing on a denominator cut by a 304 MMBoe negative
   revision; DVN's $6.45 is driven by a near-zero acquisition year colliding with a rare positive
   revision (+134 MMBoe). Neither is a run-rate. A multi-year mean would be the honest form, and
   this file does not compute one.

5. **Reserve-report authorship differs — three different levels of independence behind the single
   biggest number in each column.**
   - **PR**: *"Our proved reserves are estimated by an independent engineering firm, Netherland,
     Sewell & Associates, Inc."* — **prepared** externally, 100%.
   - **DVN**: *"Our engineers prepare our reserve estimates. We then subject certain of our reserve
     estimates to audits performed by a third-party petroleum consulting firm. In 2025, **91% of
     our proved reserves** were subjected to such an audit."* Devon names the firm: *"During 2025,
     we engaged **DeGolyer and MacNaughton** to audit 91% of our proved reserves."* — prepared
     internally, audited externally, **9% unaudited**.
   - **FANG**: *"reserve estimates prepared by our internal reservoir engineers and audited by
     Ryder Scott"*, covering *"100% of our total proved reserves"*, to a stated *"audit tolerance
     guidelines of ten percent"* — prepared internally, audited externally at 100% but to a 10%
     tolerance.

6. **The price decks are not identical.** PR discloses $66.01/Bbl (WTI Posted) and $3.39/MMBtu
   (Henry Hub spot). DVN and FANG disclose no benchmark deck at all — only differential-adjusted
   realizations. Since the SEC deck is a mechanical trailing-12-month average, the three should be
   close on the same commodity, but **that is an inference, not a disclosure**, and the row does
   not claim it.

---

## 13. WHAT THE ROW SHOWS / WHAT THE ROW CANNOT SHOW

### What it shows

- **Reserve life is not where these three separate.** PR 7.79 years and DVN 7.91 years are
  effectively the same; FANG's 10.76 is the outlier, and roughly a third of that gap is the
  Viper royalty book, which has a long tail and no drilling obligation.
- **Every one of the three replaced production organically in 2025** — 144% to 172% — but **all
  three took negative revisions**, and two of the three took large ones. FANG wrote down 304
  MMBoe (of which 128,883 MBOE was *"downgrades related to changes in the corporate development
  plan"*, i.e. a management decision, not geology) and PR wrote down 36.9 MMBoe (36.0 of it the
  same category). The organic-replacement number alone hides that.
- **Drill-bit F&D clusters tightly at $6.61–$8.21/Boe** across three operators with very different
  acreage. That is the closest thing in this row to a statement about the basin rather than the
  company: unconventional Permian development cost per barrel added is roughly the same for
  everyone, which is what one would expect where the input is a purchasable service (rigs, crews,
  sand) and the rock is broadly known.
- **Balance-sheet leverage is low across the set** at 0.94×–1.64× net debt to operating cash flow.
  PR is the least levered on the filed cash-flow line.
- **PR runs the cleanest income statement of the three** — a single revenue line, no pass-through
  throughput, no impairment, and the highest as-printed operating margin at 28.9%.

### What it cannot show

- **Base decline.** Not disclosed by any of the three. Without it, none of the reserve-life or
  replacement numbers can be converted into a statement about what maintenance capital actually
  is. This is the single largest hole in the row, and it is the number that would matter most for
  Q4 (owner earnings — maintenance capex, not total capex). See §10.
- **Maintenance capex, therefore owner earnings.** The costs-incurred table splits acquisition /
  exploration / development, but **nothing in any of these filings splits development capital into
  maintenance and growth**. Any owner-earnings figure built off this row would be spending
  conservatism on a guess.
- **Inventory depth on comparable terms.** Only FANG gives a location count (8,854 gross / 6,541
  net at *"an assumed price of approximately $50.00 per Bbl WTI"*). PR and DVN give none in these
  filings. Location counts are in any case management estimates against an assumed price, not
  reserves.
- **Devon's Delaware Basin reserves.** Not disclosed by basin. The 58.7% production share is the
  best available proxy and it is a proxy, not the figure.
- **PV-10 for DVN and FANG.** Not disclosed, and **not derivable** from the filings, because both
  give future income tax expense only on an undiscounted basis. PR's $9,439M is therefore the
  only pre-tax present value in this row, and it cannot be set against a peer.
- **Whether any of this is a moat.** Reserve life, replacement rate and F&D cost are operating
  statistics, not competitive advantage. Three operators clustering within $1.60/Boe of each other
  on drill-bit F&D is evidence *against* differentiation in the drilling function, not for it. The
  competitor row's job here is to make that visible; it is not evidence of a franchise at any of
  the three, and it is not offered as such.
- **Anything about MTDR.** This file contains no Matador figure. It is the peer column only.

---

*Prepared 2026-08-31. Every figure above traces to one of the six accession numbers in §0.
Nothing is estimated, and nothing is filled from memory or general knowledge. Where a figure is
not in the filings it is written "not disclosed" with the sections searched.*
