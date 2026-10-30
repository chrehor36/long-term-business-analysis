# A3. ALPHABET INC (GOOGL, CIK 0001652044): PROPERTY, LEASES, DEBT, LIQUIDITY

**Research file. Not a run. No verdict, no valuation. Transcription from primary filings only.**
All figures **$ millions as filed** unless stated.

## DOCUMENT REGISTER (all sentinel-checked: string "Alphabet Inc." present in body)

| FY | Accession | Primary doc | "Alphabet Inc." hits |
|---|---|---|---|
| FY2015 | 0001652044-16-000012 | goog10-k2015.htm | 169 |
| FY2016 | 0001652044-17-000008 | goog10-kq42016.htm | 119 |
| FY2017 | 0001652044-18-000007 | goog10-kq42017.htm | 119 |
| FY2018 | 0001652044-19-000004 | goog10-kq42018.htm | 116 |
| FY2019 | 0001652044-20-000008 | goog10-k2019.htm | 125 |
| FY2020 | 0001652044-21-000010 | goog-20201231.htm | 125 |
| FY2021 | 0001652044-22-000019 | goog-20211231.htm | 124 |
| FY2022 | 0001652044-23-000016 | goog-20221231.htm | 122 |
| FY2023 | 0001652044-24-000022 | goog-20231231.htm | 129 |
| FY2024 | 0001652044-25-000014 | goog-20241231.htm | 133 |
| FY2025 | 0001652044-26-000018 | goog-20251231.htm | 132 |
| 2026Q1 10-Q | 0001652044-26-000048 | goog-20260331.htm | 29 |
| 2026Q2 10-Q | 0001652044-26-000071 | goog-20260630.htm | 35 |

---

# 1. GROSS PP&E BY CATEGORY

## 1a. THE HEADLINE ANSWER TO THE MAINTENANCE-CAPEX QUESTION

**YES. Alphabet DOES split gross book between technical infrastructure and office space, but only from the FY2024 10-K forward.** The taxonomy changed at FY2024. Before that (FY2023 and earlier) the split is by *asset type* (land and buildings / information technology assets / leasehold improvements), not by *function* (data center vs office), and land-and-buildings mixes data centres with offices in a single line that the filing does not decompose.

**And the FY2025 10-K adds the single most useful sentence in the whole document for this purpose**, a footnote that did not exist in FY2024:

> "(1) As of December 31, 2024 and 2025, approximately 60% of technical infrastructure assets were comprised of servers and network equipment. The remaining balance was comprised of data center land and buildings and related assets."
> Source: FY2025 10-K, Note 7, Supplemental Financial Statement Information, Property and Equipment, Net

**The Q2-2026 10-Q repeats it and extends it to the June date** (verified against the raw HTML):
> "(1) As of December 31, 2025 and June 30, 2026, approximately 60% of technical infrastructure assets were comprised of servers and network equipment. The remaining balance was comprised of data center land and buildings and related assets."

That gives the 6-year-life bucket directly, at three dates:

| | 2024 | 2025 | **2026-06-30** |
|---|---:|---:|---:|
| Technical infrastructure, gross (in service) | 141,852 | 203,679 | **247,177** |
| × ~60% = **servers and network equipment (6-yr life)** | **~85,111** | **~122,207** | **~148,306** |
| remaining ~40% = **data center land, buildings and related (7–40 yr)** | ~56,741 | ~81,472 | ~98,871 |

*(The 60% is management's own "approximately"; the dollar split is my arithmetic on their percentage, not a filed figure. Treat these as rounded estimates carrying at least ±$5bn.)*

**Sanity check against reported depreciation.** A naive straight-line build on 2025 in-service gross book at management's own lives gives roughly: servers 122,207 ÷ 6 = 20,368; data centre buildings ~81,472 at say 20 years = 4,074; office space 48,348 at say 20 years = 2,417; corporate and other 14,463 at say 10 years = 1,446. Total ≈ **$28.3bn against reported FY2025 depreciation of $21,136M.** The build runs ~34% hot, and the two obvious reconciling items are (i) **land**, which is inside these buckets and is not depreciated, and (ii) **mid-year additions**, since gross book grew ~33% during 2025 so the average balance was far below the closing balance. Both push the same way. **The gap is expected and does not indicate an error in the filed figures, but it does mean a closing-gross-book build must be run on average balances and must carry a land haircut, or it will overstate depreciation materially.**

## 1b. NEW TAXONOMY: FY2024 and FY2025 10-Ks

**FY2025 10-K, Note 7 (as filed 2026):**

| As of December 31 | 2024 | 2025 |
|---|---:|---:|
| Technical infrastructure(1) | 141,852 | 203,679 |
| Office space | 45,403 | 48,348 |
| Corporate and other assets | 12,574 | 14,463 |
| **Property and equipment, in service** | **199,829** | **266,490** |
| Less: accumulated depreciation | (79,390) | (98,485) |
| Add: assets not yet in service | 50,597 | 78,592 |
| **Property and equipment, net** | **171,036** | **246,597** |

**FY2024 10-K, Note 7 (as filed 2025):**

| As of December 31 | 2023 | 2024 |
|---|---:|---:|
| Technical infrastructure | 112,504 | 139,596 |
| Office space | 40,435 | 43,714 |
| Corporate and other assets | 13,728 | 16,519 |
| **Property and equipment, in service** | **166,667** | **199,829** |
| Less: accumulated depreciation | (67,458) | (79,390) |
| Add: assets not yet in service | 35,136 | 50,597 |
| **Property and equipment, net** | **134,345** | **171,036** |

### FLAG: THE 2024 COLUMN WAS RECAST BETWEEN THE TWO FILINGS

The FY2025 10-K restates the **2024** category split without changing the 2024 total. Compare the two filings' 2024 column:

| 2024 category | FY2024 10-K | FY2025 10-K | Change |
|---|---:|---:|---:|
| Technical infrastructure | 139,596 | 141,852 | **+2,256** |
| Office space | 43,714 | 45,403 | **+1,689** |
| Corporate and other assets | 16,519 | 12,574 | **(3,945)** |
| Property and equipment, in service | 199,829 | 199,829 | 0 |

Net zero, a pure reclassification out of "corporate and other" into technical infrastructure and office space. No filed explanation was located for the reclass. **Use the FY2025 10-K's 141,852 for 2024, not the FY2024 10-K's 139,596**, when building a consistent series.

## 1c. OLD TAXONOMY: FY2023 and FY2021 10-Ks (as requested)

**FY2023 10-K, Note 7:**

| As of December 31 | 2022 | 2023 |
|---|---:|---:|
| Land and buildings | 66,897 | 74,083 |
| Information technology assets | 66,267 | 80,594 |
| Construction in progress | 27,657 | 35,229 |
| Leasehold improvements | 10,575 | 11,425 |
| Furniture and fixtures | 314 | 472 |
| **Property and equipment, gross** | **171,710** | **201,803** |
| Less: accumulated depreciation | (59,042) | (67,458) |
| **Property and equipment, net** | **112,668** | **134,345** |

FY2023 adds a one-line bridge, but no dollar split:
> "Our technical infrastructure is comprised of information technology assets, including servers and networking equipment, and data center land and buildings."

**FY2021 10-K, Note 7:**

| As of December 31 | 2020 | 2021 |
|---|---:|---:|
| Land and buildings | 49,732 | 58,881 |
| Information technology assets | 45,906 | 55,606 |
| Construction in progress | 23,111 | 23,171 |
| Leasehold improvements | 7,516 | 9,146 |
| Furniture and fixtures | 197 | 208 |
| **Property and equipment, gross** | **126,462** | **147,012** |
| Less: accumulated depreciation | (41,713) | (49,414) |
| **Property and equipment, net** | **84,749** | **97,599** |

*(The FY2022 10-K shows 2021 CIP as 23,172 and gross as 147,013, a $1M rounding difference against the FY2021 filing. Immaterial; noted for completeness.)*

## 1d. FULL GROSS PP&E BUILD, FY2014–FY2025 (old taxonomy through 2023, new from 2024)

Each column transcribed from the 10-K in which that year was the current year.

| As of Dec 31 | Land & buildings | IT assets | Constr. in progress | Leasehold impr. | Furn. & fixtures | **Gross** | Accum. depr. | **Net** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2014 | 13,326 | 10,918 | 6,555 | 1,868 | 79 | **32,746** | (8,863) | **23,883** |
| 2015 | 16,518 | 13,645 | 7,324 | 2,576 | 83 | **40,146** | (11,130) | **29,016** |
| 2016 | 19,804 | 16,084 | 8,166 | 3,415 | 58 | **47,527** | (13,293) | **34,234** |
| 2017 | 23,183 | 21,429 | 10,491 | 4,496 | 48 | **59,647** | (17,264) | **42,383** |
| 2018 | 30,179 | 30,119 | 16,838 | 5,310 | 61 | **82,507** | (22,788) | **59,719** |
| 2019 | 39,865 | 36,840 | 21,036 | 6,310 | 156 | **104,207** | (30,561) | **73,646** |
| 2020 | 49,732 | 45,906 | 23,111 | 7,516 | 197 | **126,462** | (41,713) | **84,749** |
| 2021 | 58,881 | 55,606 | 23,171 | 9,146 | 208 | **147,012** | (49,414) | **97,599** |
| 2022 | 66,897 | 66,267 | 27,657 | 10,575 | 314 | **171,710** | (59,042) | **112,668** |
| 2023 | 74,083 | 80,594 | 35,229 | 11,425 | 472 | **201,803** | (67,458) | **134,345** |

| As of Dec 31 | Technical infra. | Office space | Corp. & other | **In service** | Accum. depr. | Not yet in service | **Net** |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2023 (recast) | 112,504 | 40,435 | 13,728 | **166,667** | (67,458) | 35,136 | **134,345** |
| 2024 (as FY2024 10-K) | 139,596 | 43,714 | 16,519 | **199,829** | (79,390) | 50,597 | **171,036** |
| 2024 (as FY2025 10-K) | 141,852 | 45,403 | 12,574 | **199,829** | (79,390) | 50,597 | **171,036** |
| 2025 | 203,679 | 48,348 | 14,463 | **266,490** | (98,485) | 78,592 | **246,597** |

**Bridge check on the taxonomy change at 2023:** old gross 201,803 = new in-service 166,667 + not-yet-in-service 35,136. ✓ Exact. Note the recast moved $93M out of the old "construction in progress" (35,229) into the in-service buckets to produce "assets not yet in service" of 35,136.

**Total gross PP&E including assets not yet in service, 2025 = 266,490 + 78,592 = 345,082.**

## 1d-bis. THE Q2-2026 UPDATE: the table is repeated in the 10-Q

**Q2-2026 10-Q, Note 7:**

| | 2025-12-31 | **2026-06-30** | 6-month change |
|---|---:|---:|---:|
| Technical infrastructure(1) | 203,679 | **247,177** | **+43,498** |
| Office space | 48,348 | 50,635 | +2,287 |
| Corporate and other assets | 14,463 | **6,498** | **(7,965)** |
| **Property and equipment, in service** | **266,490** | **304,310** | +37,820 |
| Less: accumulated depreciation | (98,485) | (105,912) | (7,427) |
| **Add: assets not yet in service** | **78,592** | **122,814** | **+44,222** |
| **Property and equipment, net** | **246,597** | **321,212** | **+74,615** |

**Two things jump out.** (i) Assets not yet in service rose another **$44.2bn in six months to $122.8bn**, which is now **28.8% of total gross PP&E of $427,124M**, far above the 16–20% decade norm. (ii) "Corporate and other assets" fell by $7,965M with no explanation given, which looks like a second reclassification of the same kind seen in the FY2024→FY2025 recast (see the flag above). **Treat the corporate-and-other line as unstable across vintages.**

## 1e. MANAGEMENT'S STATED USEFUL LIVES (for the forward maintenance-capex build)

**FY2024 and FY2025 10-K, Significant Accounting Policies, Property and Equipment** (FY2024 text quoted; FY2025 is materially identical):
> "Property and equipment are stated at cost less accumulated depreciation. Depreciation commences once assets are ready for our intended use and is recorded using the straight-line method over the estimated useful lives of the assets, which we regularly evaluate for factors such as technological obsolescence and our planned use and utilization. We depreciate **data center and office buildings over periods of seven to 40 years**. We depreciate **servers and network equipment generally over a period of six years**. We depreciate **corporate and other assets over periods of two to 25 years**. We depreciate leasehold improvements over the shorter of the remaining lease term or the estimated useful lives of the assets. Land is not depreciated."

**FY2021 10-K, for contrast, the lives were materially shorter and the buildings cap was 25 not 40 years:**
> "We depreciate buildings over periods of **seven to 25 years**. We depreciate information technology assets generally over periods of **four to five years** (generally, four years for servers and five years for network equipment)."

*(The life-extension history is the subject of the companion file A1-useful-lives.md. It is flagged here only because the 6-year server life is an input to the build and it has been extended twice since 2020: 3→4 years effective 2021, 4→6 years effective 2023.)*

**Note the land problem.** Technical infrastructure and office space both *include land*, and land is not depreciated. The filings do not disclose the land component of either bucket. A gross-book × 1/life build will therefore overstate depreciation unless land is stripped, and it cannot be stripped from the filed data. **This is an UNRESEARCHED-not-UNKNOWABLE gap only if a document naming the land carrying value exists; none was located in the 10-K.**

---

# 2. "ASSETS NOT YET IN SERVICE": CAPITAL NOT YET DEPRECIATING

Disclosed as its own caption from FY2024 forward. Before that the comparable caption is "construction in progress."

| As of Dec 31 | Caption | Amount | Total gross PP&E (incl. this line) | **Share of gross** |
|---|---|---:|---:|---:|
| 2014 | Construction in progress | 6,555 | 32,746 | **20.0%** |
| 2015 | Construction in progress | 7,324 | 40,146 | **18.2%** |
| 2016 | Construction in progress | 8,166 | 47,527 | **17.2%** |
| 2017 | Construction in progress | 10,491 | 59,647 | **17.6%** |
| 2018 | Construction in progress | 16,838 | 82,507 | **20.4%** |
| 2019 | Construction in progress | 21,036 | 104,207 | **20.2%** |
| 2020 | Construction in progress | 23,111 | 126,462 | **18.3%** |
| 2021 | Construction in progress | 23,171 | 147,012 | **15.8%** |
| 2022 | Construction in progress | 27,657 | 171,710 | **16.1%** |
| 2023 | Construction in progress | 35,229 | 201,803 | **17.5%** |
| 2023 (recast) | Assets not yet in service | 35,136 | 201,803 | **17.4%** |
| 2024 | Assets not yet in service | 50,597 | 250,426 | **20.2%** |
| 2025 | **Assets not yet in service** | **78,592** | **345,082** | **22.8%** |

**Reading:** the ratio is remarkably stable at 16–20% for a decade and then breaks out to 22.8% in 2025. In dollars it went 35,136 → 50,597 → 78,592 in two years, +$43.5bn, and it is **capital already spent that is producing no depreciation charge yet**. At 2025 year end $78.6bn of gross book sits outside the depreciation base.

**What is in it. FY2025 10-K, Liquidity and Capital Resources, verbatim:**
> "Assets not yet in service are those that are not ready for their intended use, including assets in the process of construction or assembly, and consist primarily of technical infrastructure. The time frame from date of purchase to placement in service of these assets may extend from months to years. For example, our data center construction projects are generally multi-year projects with multiple phases, where we acquire land and buildings, construct buildings, and secure and install servers and network equipment."

**FY2025 10-K, Significant Accounting Policies, verbatim:**
> "Property and equipment is comprised of technical infrastructure, office space, corporate and other assets currently in service, and assets not yet in service. Technical infrastructure includes data center land, buildings and leasehold improvements, and servers and network equipment. Office space includes office land, buildings, and leasehold improvements. Assets not yet in service are those that are not ready for their intended use, including data center buildings and servers in the process of construction or assembly."

**Consequence for the forward build:** the depreciation run-rate implied by 2025 in-service gross book understates the committed run-rate. When the $78.6bn lands in service, "months to years," predominantly technical infrastructure, so call it ~60% servers at 6 years and ~40% buildings at the long life, it adds roughly $78.6bn × (0.60/6 + 0.40/20) ≈ **$9.4bn/yr of incremental depreciation** on capital *already spent*, before any 2026 capex. That is a computation on filed inputs, not a filed figure.

---

# 3. DEPRECIATION AND AMORTIZATION SERIES, FY2015–FY2025 + H1-2026

## 3a. THE CAPTIONS CHANGED TWICE: READ THIS BEFORE USING THE SERIES

The cash-flow statement's D&A captions are **not** consistent across the period:

- **FY2015–FY2022:** two lines, both explicitly including impairment: *"Depreciation and impairment of property and equipment"* and *"Amortization and impairment of intangible assets."*
- **FY2023–FY2025:** one line only, *"Depreciation of property and equipment."* **The intangible-amortization line was DELETED from the cash-flow statement and folded into "Other."** Prior-year depreciation was simultaneously restated downward to strip impairment out.
- There is **no separate intangible-assets note** from FY2023 onward. The note title itself changed, and it changed in the same year the cash-flow line disappeared:

| Filing | Note 9 title |
|---|---|
| FY2022 10-K | **"Goodwill and Other Intangible Assets"** |
| FY2023 10-K | "Goodwill" |
| FY2024 10-K | "Goodwill" |
| FY2025 10-K | "Goodwill" |

  **Intangible amortization for FY2023, FY2024 and FY2025 is NOT SEPARATELY DISCLOSED anywhere in those filings.** Two disclosures were withdrawn simultaneously at FY2023: the cash-flow amortization line and the intangible-assets note. This is a real reduction in disclosure, though of a small number.

## 3b. THE SERIES AS FILED

Each row taken from the 10-K in which that year was the current year.

| FY | Caption used | Depreciation of PP&E | Amortization (+impairment) of intangibles | **TOTAL D&A as filed** |
|---|---|---:|---:|---:|
| 2015 | depr. & impairment / amort. & impairment | 4,132 | 931 | **5,063** |
| 2016 | " | 5,267 | 877 | **6,144** |
| 2017 | " | 6,103 | 812 | **6,915** |
| 2018 | " | 8,164 | 871 | **9,035** |
| 2019 | " | 10,856 | 925 | **11,781** |
| 2020 | " | 12,905 | 792 | **13,697** |
| 2021 | " | 11,555 | 886 | **12,441** |
| 2022 | " | 15,287 | 641 | **15,928** |
| 2023 | depreciation only | 11,946 | NOT DISCLOSED | **11,946 + n/d** |
| 2024 | depreciation only | 15,311 | NOT DISCLOSED | **15,311 + n/d** |
| 2025 | depreciation only | 21,136 | NOT DISCLOSED | **21,136 + n/d** |
| **H1-2026** | depreciation only | **13,586** | NOT DISCLOSED | **13,586 + n/d** |
| *(H1-2025 comparative)* | | *9,485* | | |

**Answer to "I need TOTAL D&A, not just PP&E depreciation":** total D&A is obtainable as a filed figure only through FY2022. From FY2023 the filings disclose PP&E depreciation alone; intangible amortization sits undisclosed inside the cash-flow "Other" line (FY2023 4,330 / FY2024 3,419 / FY2025 2,108, which also contains other items). **The last observed intangible amortization was $641M in FY2022, and it had been declining (925 → 792 → 886 → 641). It is small relative to PP&E depreciation and immaterial to an owner-earnings build, but it is a genuine disclosure gap, and it is UNRESEARCHED, not UNKNOWABLE: a document that would resolve it is the FY2023 10-K XBRL `AmortizationOfIntangibleAssets` tag, if Alphabet still tags it.**

## 3c. THE RESTATEMENT AT FY2023: IMPAIRMENT STRIPPED OUT OF DEPRECIATION

The FY2023 10-K restated the two prior years' depreciation downward when it renamed the caption:

| Year | As filed FY2022 10-K ("depreciation **and impairment**") | As restated FY2023 10-K ("depreciation") | Difference = impairment removed |
|---|---:|---:|---:|
| 2021 | 11,555 | 10,273 | **1,282** |
| 2022 | 15,287 | 13,475 | **1,812** |

The FY2023 10-K explains this only with the boilerplate:
> "Prior Period Reclassifications
> Certain amounts in prior periods have been reclassified to conform with current period presentation."

No line-item reconciliation is given. **Use 10,273 (2021) and 13,475 (2022) for a clean depreciation-only series; use 11,555 and 15,287 if you want depreciation-plus-impairment.** The $1,812M of 2022 impairment is the office-space write-down, see 3d.

## 3d. ACCELERATED DEPRECIATION AND IMPAIRMENT OF ASSETS: EVERY FILED INSTANCE

**There is NO accelerated depreciation or impairment of servers or data-centre assets in any year.** Every accelerated-depreciation and impairment event Alphabet has disclosed relates to **office space**, not technical infrastructure. This is a material negative finding: across an eleven-year run in which server useful lives were extended twice, Alphabet has never taken a writedown on the server fleet.

**FY2023 10-K, MD&A, verbatim:**
> "In January 2023, we announced a reduction of our workforce, and as a result we recorded employee severance and related charges of $2.1 billion for the year ended December 31, 2023. In addition, we are taking actions to optimize our global office space. As a result, exit charges recorded during the year ended December 31, 2023, were $1.8 billion. In addition to these exit charges, for the year ended December 31, 2023, we incurred **$269 million in accelerated rent and accelerated depreciation**."

**FY2024 10-K, MD&A, verbatim:**
> "Employee severance and related charges for the year ended December 31, 2024 were $1.0 billion, a decrease of $1.1 billion as compared to the year ended December 31, 2023. **Office space charges, including accelerated rent and accelerated depreciation, for the year ended December 31, 2024 were $796 million**, a decrease of $1.3 billion as compared to the year ended December 31, 2023. Substantially all of these charges were included in Alphabet-level activities."

**FY2022 10-K, MD&A, verbatim (the charge was flagged forward, and lands as the $1,812M impairment stripped out at FY2023):**
> "In addition, we are taking actions to optimize our global office space. As a result we expect to incur exit costs relating to office space reductions of approximately $0.5 billion in the first quarter of 2023. We may incur additional charges in the future as we further evaluate our real estate needs."

**FY2025 10-K:** no office-space or accelerated-depreciation charge is disclosed. The only FY2025 uses of the phrase "accelerated depreciation" are **tax**, not book. They refer to bonus depreciation on eligible capex under the 2025 US tax legislation, which affects cash taxes (see section 9), not the depreciation expense line:
> "…accelerated depreciation on eligible capital expenditures, the effects of which are included in operating cash flows for the year ended December 31, 2025."

## 3e. THE USEFUL-LIFE CHANGES THAT SUPPRESSED DEPRECIATION (cross-reference)

Two prospective life extensions sit inside this series and both *reduced* reported depreciation. Detail is in the companion file `A1-useful-lives.md`; the load-bearing quotes are repeated here because they distort the D&A trend:

**FY2021 10-K, verbatim** (change effective Q1 2021, servers 3→4 years, certain network equipment →5 years):
> "…resulting in a **reduction in depreciation expense of $2.6 billion** recorded primarily in cost of revenues and R&D."

**FY2022 10-K, verbatim** (change effective FY2023):
> "…useful lives of our servers and network equipment, resulting in a change in the estimated useful life of our servers and certain network equipment **to six years**, which we expect to result in a **reduction of depreciation of approximately $3.4 billion for the full fiscal year 2023 for assets in service as of December 31, 2022**, recorded primarily in cost of revenues and R&D expenses."
and
> "…adjusted the estimated useful life of our **servers from four years to six years** and the estimated useful life of certain **network equipment from five years to six years**."

**Consequence:** the 2021 and 2023 depreciation *declines* (12,905 → 11,555 → and 2023's 11,946 against 2022's 13,475) are accounting-life changes, not asset-base declines. The gross book rose in every one of those years. Do not read the depreciation series as a proxy for economic consumption without adjusting for this.

## 3f. CAPEX ALONGSIDE, FOR THE MAINTENANCE-CAPEX GAP

| Period | Purchases of PP&E (CF investing) | Depreciation of PP&E | **Capex ÷ depreciation** |
|---|---:|---:|---:|
| FY2023 | 32,251 | 11,946 | **2.70×** |
| FY2024 | 52,535 | 15,311 | **3.43×** |
| FY2025 | **91,447** | **21,136** | **4.33×** |
| H1-2025 | 39,643 | 9,485 | 4.18× |
| **H1-2026** | **80,598** | **13,586** | **5.93×** |

Non-cash supplement, FY2025 10-K: *"Purchases of property and equipment included in accrued liabilities and accounts payable"* was **7,435 (2023) / 10,326 (2024) / 15,090 (2025)**, i.e. accrued but unpaid capex rose another $4.8bn in 2025, so cash capex understates capex committed.

**And the Q2-2026 10-Q shows that gap exploding.** The same non-cash line reads *"Property and equipment included in accrued liabilities and accounts payable"*: **$10,635M at 2025-06-30 and $29,113M at 2026-06-30.** Nearly $30bn of capex is incurred but unpaid at the half-year, against $80.6bn of cash capex in the six months. **Cash capex materially understates capex incurred, and the understatement is widening.**

**FY2025 10-K, verbatim, on the forward direction:**
> "During the years ended December 31, 2024 and 2025, we spent $52.5 billion and $91.4 billion on capital expenditures, respectively. **In 2026, we expect to significantly increase, relative to 2025, our investment in our technical infrastructure**, including servers and network equipment, and data centers. Depreciation of our property and equipment commences when such assets are ready for their intended use. For the years ended December 31, 2024 and 2025, our depreciation on property and equipment was $15.3 billion and $21.1 billion, respectively."

**FY2025 10-K, Trends in Our Business, verbatim, management's own warning on the depreciation trajectory:**
> "Increased Investment in Technical Infrastructure: We continue to invest in capital expenditures as we scale our technical infrastructure, in particular for AI, to meet the demand of our users and enterprise customers and to support research internally. We invested heavily in capital expenditures in 2025 and in 2026, we expect to significantly increase, relative to 2025, our investment in our technical infrastructure, including servers and network equipment, and data centers. **The costs associated with operating our technical infrastructure - depreciation, energy, equipment, and network capacity - are expected to significantly increase as developing and serving AI offerings require more compute power than our historical consumer and enterprise offerings.**"

---

# 4. LEASES

## 4a. LEASES SIGNED BUT NOT YET COMMENCED: THE HEADLINE

**This is the fastest-moving number in the filing. It went up roughly 12x in 2025 and another 46% in six months.**

| As of | Short-term | Long-term | **TOTAL not yet commenced** | Commencement window / terms |
|---|---:|---:|---:|---|
| 2021-12-31 | 606 | 5,200 | **~5,806** | not stated |
| 2022-12-31 | 630 | 3,100 | **~3,730** | not stated |
| 2023-12-31 | 657 | 3,300 | **~3,957** | not stated |
| 2024-12-31 | 773 | 6,500 | **~7,273** | not stated |
| **2025-12-31** | **5,800** | **52,700** | **~58,500** | **2026–2031, terms primarily 1–25 yrs** |
| **2026-03-31** | *(not split)* | *(not split)* | **75,600** | not restated in Q |
| **2026-06-30** | *(not split)* | *(not split)* | **85,200** | **2026–2031, terms 1–26 yrs** |

**Against the Microsoft comparable of $329.1bn, Alphabet's figure is $85.2bn at 2026-06-30.** Roughly one quarter the size. But note the two are not perfectly comparable without checking Microsoft's caption; Alphabet's is "leases… that have not yet commenced with future lease payments… that are not yet recorded," undiscounted.

### The verbatim sentences, as requested

**FY2023 10-K, Note 4 Leases:**
> "As of December 31, 2023, we have entered into leases that have not yet commenced with short-term and long-term future lease payments of $657 million and $3.3 billion that are not yet recorded on our Consolidated Balance Sheets."

**FY2024 10-K, Note 4 Leases:**
> "As of December 31, 2024, we have entered into leases that have not yet commenced with short-term and long-term future lease payments of $773 million and $6.5 billion, respectively, that are not yet recorded on our Consolidated Balance Sheets."

**FY2025 10-K, Note 4 Leases:**
> "As of December 31, 2025, we have entered into leases **primarily related to data centers** that have not yet commenced with short-term and long-term future lease payments of **$5.8 billion and $52.7 billion**, respectively, that are not yet recorded. These leases will commence between 2026 and 2031 with non-cancelable lease terms primarily between one and 25 years."

**Q2-2026 10-Q, Note 4 Leases:**
> "As of June 30, 2026, we have entered into leases, **primarily related to data centers**, that have not yet commenced with future lease payments of **$85.2 billion** that are not yet recorded. These leases will commence between 2026 and 2031 with non-cancelable lease terms between one and 26 years."
> "Additionally, in June 2026, we entered into a **short-term lease agreement with a non-cancelable commitment of approximately $5.8 billion**, which will commence in the third quarter of 2026."

*(Q1-2026 10-Q for the trend: "As of March 31, 2026, we have entered into leases primarily related to data centers that have not yet commenced with future lease payments of $75.6 billion that are not yet recorded.")*

**Note the wording shift.** Through FY2024 the sentence says nothing about what the leases are for. From FY2025 it says "primarily related to data centers." The 2021–2024 numbers were office real estate; the 2025–2026 numbers are compute capacity. They are not the same series economically even though the caption is the same.

### Two further off-balance-sheet lease items disclosed only in narrative

**FY2025 10-K, Note 4, verbatim, on a power purchase agreement that will be a lease:**
> "In January 2026, we executed a power purchase agreement which we expect to be accounted for as a lease resulting in future payments depending on certain agreement terms of **$9.9 billion between 2027 and 2047**. If certain contractual conditions for the project are not met, we would instead make a one-time payment of approximately $3.5 billion and assume ownership of the power generating assets."

**Prepayments on leases not yet commenced** (cash already out the door on the not-yet-commenced book):
- FY2025: "The year ended December 31, 2025 includes **$1.1 billion of prepayments for finance leases not yet commenced**."
- Q2-2026: "…during the three and six months ended June 30, 2026, we made **$201 million and $835 million of lease prepayments for leases not yet commenced**, respectively, which are expected to be accounted for as finance leases."

## 4b. BALANCE-SHEET LEASE POSITION

| $M | 2024-12-31 | 2025-12-31 | **2026-06-30** |
|---|---:|---:|---:|
| **Operating leases** | | | |
| Operating lease assets (ROU) | 13,588 | 15,221 | **17,694** |
| Current (in accrued expenses & other liabilities) | 2,887 | 3,209 | **3,446** |
| Noncurrent (operating lease liabilities) | 11,691 | 12,744 | **14,591** |
| **Total operating lease liabilities** | **14,578** | **15,954** | **18,037** |
| **Finance leases** | | | |
| Property and equipment, at cost (finance-lease ROU) | 4,622 | 6,822 | **7,915** |
| Accumulated depreciation | (2,037) | (2,025) | **(2,441)** |
| **Property and equipment, net** | **2,585** | **4,797** | **5,474** |
| Current (in accrued expenses & other liabilities) | 235 | 441 | **449** |
| Noncurrent (other long-term liabilities) | 1,442 | 2,059 | **2,141** |
| **Total finance lease liabilities** | **1,677** | **2,500** | **2,590** |
| **Weighted-average remaining term, operating** | 7.8 yrs | 7.6 yrs | **8.4 yrs** |
| **Weighted-average remaining term, finance** | 10.4 yrs | 8.3 yrs | **8.6 yrs** |
| **Weighted-average discount rate, operating** | 3.4% | 3.6% | **3.8%** |
| **Weighted-average discount rate, finance** | 2.8% | 3.1% | **3.3%** |

**Finance-lease liabilities are tiny, $2.6bn at 2026-06-30, against $85.2bn of signed-but-not-commenced leases.** Essentially the entire data-centre lease programme is still off balance sheet.

## 4c. TOTAL LEASE COST COMPONENTS

| $M | FY2023 | FY2024 | FY2025 | H1-2025 | **H1-2026** |
|---|---:|---:|---:|---:|---:|
| Operating lease cost | 3,362 | 3,304 | 3,345 | 1,608 | **1,834** |
| Finance: amortization of lease assets | 469 | 413 | 553 | 208 | **485** |
| Finance: interest on lease liabilities | 35 | 31 | 65 | 31 | **35** |
| *Finance lease cost (subtotal)* | *504* | *444* | *618* | *239* | ***520*** |
| Variable lease cost | 1,182 | 1,425 | 1,739 | 732 | **863** |
| **Total lease cost** | **5,048** | **5,173** | **5,702** | **2,579** | **3,217** |

Earlier vintages disclosed operating lease cost only (finance leases were immaterial): FY2021 10-K shows operating lease cost 2,267 (2020) / 2,699 (2021) with variable 619 / 726; FY2022 adds 2,900 and 838 for 2022.

## 4d. FINANCE-LEASE ROU ADDITIONS BY YEAR ("assets obtained in exchange for lease liabilities")

| $M | FY2022 | FY2023 | FY2024 | FY2025 | H1-2025 | **H1-2026** |
|---|---:|---:|---:|---:|---:|---:|
| Operating leases | 4,383 | 2,877 | 2,510 | 4,070 | 1,528 | **3,739** |
| **Finance leases** | **577** | **564** | **313** | **1,606** | **606** | **902** |

Finance-lease additions were flat-to-falling through 2024 and then jumped 5x in 2025. Cash on finance leases follows: financing cash flows used for finance leases went 705 (2023) / 405 (2024) / **1,988 (2025)**, and 302 (H1-2025) / **840 (H1-2026)**.

## 4e. MATURITY TABLES

**As of December 31, 2025 (FY2025 10-K):**

| $M | Operating leases | Finance leases |
|---|---:|---:|
| 2026 | 3,275 | 491 |
| 2027 | 3,082 | 345 |
| 2028 | 2,510 | 335 |
| 2029 | 2,061 | 314 |
| 2030 | 1,669 | 241 |
| Thereafter | 5,654 | 1,143 |
| **Total undiscounted lease payments** | **18,251** | **2,869** |
| Less: imputed interest | (2,297) | (369) |
| **Total lease liability balance** | **15,954** | **2,500** |

**As of June 30, 2026 (Q2-2026 10-Q):**

| $M | Operating leases | Finance leases |
|---|---:|---:|
| Remainder of 2026 | 1,836 | 206 |
| 2027 | 3,498 | 387 |
| 2028 | 2,979 | 377 |
| 2029 | 2,576 | 356 |
| 2030 | 2,046 | 285 |
| Thereafter | 8,398 | 1,309 |
| **Total undiscounted lease payments** | **21,333** | **2,920** |
| Less: imputed interest | (3,296) | (330) |
| **Total lease liability balance** | **18,037** | **2,590** |

**Scale check:** recorded undiscounted lease payments at 2026-06-30 total **$24.3bn** across both types. Signed but not yet recorded: **$85.2bn**, plus the $5.8bn short-term lease commencing Q3-2026, plus the $9.9bn PPA. **The unrecorded book is roughly 4x the recorded book.**

## 4f. RELATED: VIE FUNDING COMMITMENTS (found in Note 5, not the lease note)

**Q2-2026 10-Q, Note 5 Variable Interest Entities, verbatim:**
> "The maximum exposure to these VIEs is generally limited to the current carrying value plus future funding commitments. As of December 31, 2025 and June 30, 2026, future funding commitments were **$1.1 billion and $21.9 billion**, respectively. As of June 30, 2026, this amount includes **$20.0 billion of future capital funding commitments with a private company contingent upon the achievement of specified operational and financial milestones through 2030, which is accounted for as an equity derivative.**"

The counterparty is **not named in the filing**. A $20bn commitment appearing between December 2025 and June 2026 and structured as an equity derivative is a material new obligation that does not appear in the lease tables, the debt note, or the purchase-commitment total.

**FY2025 10-K, Note 5, verbatim, on data-centre leasing VIEs:**
> "Leases with data center leasing VIEs are accounted for as finance leases and are included within total lease obligations disclosed in Note 4. The maximum exposure arising from leases with VIEs is limited to the net carrying value of commenced finance lease assets, plus the undiscounted future obligations for leases that have not yet commenced."
> "Credit backstops we have provided to data center VIEs are accounted for as credit derivatives."

---

# 5. DEBT

## 5a. CONFIRMATION OF THE XBRL TRAJECTORY: CONFIRMED FROM THE FILED STATEMENTS

The XBRL series in the task brief is **confirmed against the filed debt notes**:

| Date | Total long-term debt (noncurrent), as filed | Total face value | Source |
|---|---:|---:|---|
| 2024-12-31 | **10,883** | 12,000 | FY2025 10-K Note 6 comparative (FY2024 10-K agrees) |
| 2025-12-31 | **46,547** | 49,085 | FY2025 10-K Note 6 |
| **2026-03-31** | **77,501** | **80,305** | **Q1-2026 10-Q Note 6, transcribed and confirmed** |
| **2026-06-30** | **98,165** | **101,085** | Q2-2026 10-Q Note 6 |

Every date in the XBRL series checks against the filed debt note. **Total FACE value** of long-term debt went 12,000 (2024) to **101,085** (2026-06-30), up **8.4x in eighteen months**.

## 5b. WHAT WAS ISSUED, WHEN, AT WHAT COUPONS, IN WHAT CURRENCIES

**FY2025 10-K, Note 6, verbatim:**
> "During 2025, we issued **$22.5 billion of US dollar-denominated senior unsecured notes and €13.25 billion of euro-denominated senior unsecured notes** for general corporate purposes."
> "In **May 2025**, we issued **$5.0 billion** of US dollar-denominated fixed-rate senior unsecured notes with a weighted-average coupon rate of **4.89%**, and a weighted-average maturity of approximately **24 years**. Additionally, in May 2025, we issued **€6.75 billion** of euro-denominated fixed-rate senior unsecured notes with a weighted-average coupon rate of **3.31%**, and a weighted-average maturity of approximately **14 years**."
> "In **November 2025**, we issued **$500 million** of US dollar-denominated **floating-rate** senior unsecured notes and **$17.0 billion** of US dollar-denominated fixed-rate senior unsecured notes with a weighted-average coupon rate of **4.92%** and a weighted-average maturity of approximately **20 years**. Additionally in November 2025, we issued **€6.5 billion** of euro-denominated fixed-rate senior unsecured notes with a weighted-average coupon rate of **3.44%** and a weighted-average maturity of approximately **16 years**."

**Q2-2026 10-Q, Note 6, verbatim, six currencies in six months:**
> "During 2026, we issued **$20.0 billion of US dollar-denominated fixed-rate senior unsecured notes and $31.8 billion of foreign currency-denominated fixed-rate senior unsecured notes** for general corporate purposes."
> "In the **first quarter of 2026**, we issued fixed-rate senior unsecured notes consisting of: **$20.0 billion US dollar-denominated notes** with a weighted-average coupon rate of **4.80%** and a weighted-average maturity of **15 years**; **£5.5 billion Sterling-denominated notes** with a weighted-average coupon rate of **5.31%** and a weighted-average maturity of **31 years**; and **CHF3.1 billion Swiss Franc-denominated notes** with a weighted-average coupon rate of **1.06%** and a weighted-average maturity of **10 years**."
> "In the **second quarter of 2026**, we issued fixed-rate senior unsecured notes consisting of: **€9.0 billion Euro-denominated notes** with a weighted-average coupon rate of **3.90%** and a weighted-average maturity of **13 years**; **C$8.5 billion Canadian dollar-denominated notes** with a weighted-average coupon rate of **4.35%** and a weighted-average maturity of **15 years**; and **¥576.5 billion Japanese yen-denominated notes** with a weighted-average coupon rate of **2.65%** and a weighted-average maturity of **8 years**."

## 5c. THE DEBT TABLE BY TRANCHE

**Q2-2026 10-Q, Note 6 (supersedes FY2025 for the 2025 column):**

| Debt | Maturity | Coupon rate | Effective rate | 2025-12-31 | **2026-06-30** |
|---|---|---|---|---:|---:|
| 2016 US dollar notes | 2026 | 2.00% | 2.23% | 2,000 | 2,000 |
| 2020 US dollar notes | 2027–2060 | 0.80%–2.25% | 0.93%–2.33% | 9,000 | 9,000 |
| 2025 US dollar notes(1) | 2028–2075 | 3.88%–5.70% | 4.00%–5.79% | 22,500 | 22,500 |
| 2025 Euro notes(2) | 2028–2064 | 2.38%–4.38% | 2.57%–4.51% | 15,585 | 15,074 |
| **2026 US dollar notes** | 2029–2066 | 3.70%–5.75% | 3.93%–5.84% | 0 | **20,000** |
| **2026 Sterling notes(2)** | **2029–2126** | 4.13%–6.13% | 4.23%–6.19% | 0 | **7,263** |
| **2026 Swiss franc notes(2)** | 2029–2051 | 0.43%–1.87% | 0.52%–1.90% | 0 | **3,772** |
| **2026 Euro notes(2)** | 2030–2063 | 3.20%–4.80% | 3.29%–4.88% | 0 | **10,239** |
| **2026 Canadian dollar notes(2)** | 2031–2056 | 3.65%–5.00% | 3.83%–5.10% | 0 | **5,985** |
| **2026 Japanese yen notes(2)** | 2029–2066 | 1.97%–4.60% | 2.04%–4.64% | 0 | **3,566** |
| **Other long-term debt** | | | | 0 | **1,686** |
| **Total face value of long-term debt** | | | | **49,085** | **101,085** |
| Unamortized discount and debt issuance costs(2) | | | | (542) | (921) |
| Less: current portion of long-term notes(3) | | | | (1,996) | (1,999) |
| **Total long-term debt** | | | | **46,547** | **98,165** |

> "(1) Includes $500 million of floating-rate notes due in 2028. Interest is calculated using the compounded Secured Overnight Financing Rate (SOFR) plus 0.52%, reset quarterly.
> (2) Principal, unamortized discount, and debt issuance costs for the foreign currency-denominated notes include the effect of foreign exchange rates.
> (3) Total current portion of long-term debt is included within accrued expenses and other current liabilities."

**Note the 2126 maturity on the Sterling notes, a 100-year bond.** And note "Other long-term debt" of $1,686M appearing for the first time at 2026-06-30 with no tranche detail given.

**Redemption terms, Q2-2026 verbatim:**
> "The notes in the table above are senior unsecured obligations and rank equally with each other. We may redeem the fixed-rate notes, **other than the Japanese yen-denominated notes**, at any time in whole or in part at specified redemption prices. The floating-rate notes and Japanese yen-denominated notes are not redeemable prior to maturity. Interest is payable quarterly for the floating-rate notes, semi-annually for the US dollar, Canadian dollar, and Japanese yen-denominated fixed-rate notes, and annually for the Euro, Sterling, and Swiss franc-denominated fixed-rate notes."

**Fair value:** approximately **$45.6bn** (2025-12-31) and **$94.9bn** (2026-06-30), Level 2. Fair value is *below* face at both dates.

## 5d. MATURITY SCHEDULE

**As of December 31, 2025 (FY2025 10-K), future principal payments:**

| Year | $M |
|---|---:|
| 2026 | 2,000 |
| 2027 | 1,000 |
| 2028 | 2,676 |
| 2029 | 1,764 |
| 2030 | 5,500 |
| Thereafter | **36,145** |
| **Total** | **49,085** |

**74% of the 2025 debt matures after 2030.** The Q2-2026 10-Q does **NOT** repeat the maturity schedule (10-Qs are not required to), so an equivalent table at 2026-06-30 is **NOT DISCLOSED**; the tranche maturity ranges in 5c are the only guide.

## 5e. COMMERCIAL PAPER

**FY2025 10-K, verbatim:**
> "We have a **commercial paper program of up to $25.0 billion**, which is used for general corporate purposes. We had **$2.3 billion of commercial paper outstanding with a weighted-average effective interest rate of 4.4% as of December 31, 2024** and **no commercial paper outstanding as of December 31, 2025**."

**Q2-2026 10-Q, verbatim:**
> "We have a commercial paper program of up to $25.0 billion, which is used for general corporate purposes. We had **no commercial paper outstanding as of December 31, 2025 and June 30, 2026**."

## 5f. CREDIT FACILITY / REVOLVER: AND THE FIRST DRAW

**FY2024 10-K, verbatim:**
> "As of December 31, 2024, we had **$10.0 billion of revolving credit facilities**, of which $4.0 billion expires in April 2025 and $6.0 billion expires in April 2028. The interest rates for all credit facilities are determined based on a formula using certain market rates, **as well as our progress toward the achievement of certain sustainability goals**. **No amounts were outstanding** under the credit facilities as of December 31, 2023 and 2024."

**FY2025 10-K, verbatim** (note the sustainability-linked pricing clause was dropped):
> "As of December 31, 2025, we had **$10.0 billion of revolving credit facilities**, of which $4.0 billion expires in April 2026 and $6.0 billion expires in April 2030. The interest rates for all credit facilities are determined based on a formula using certain market rates. **No amounts were outstanding** under the credit facilities as of December 31, 2024 and 2025."

**Q1-2026 10-Q, verbatim. THE FACILITY IS DRAWN FOR THE FIRST TIME:**
> "As of March 31, 2026, we had **$11.7 billion of credit facilities** expiring at various dates through April 2030, of which **$1.2 billion was outstanding**. The outstanding debt under the credit facilities bears an interest rate of **SOFR plus 1.5% to 2.25%** that is paid quarterly."

**Q2-2026 10-Q, verbatim:**
> "As of June 30, 2026, we had **$11.7 billion of credit facilities**, expiring at various dates through April 2030, of which **$1.3 billion was outstanding**. The outstanding debt under the credit facilities bears an interest rate of **SOFR plus 1.5% to 2.25%** that is paid quarterly."

**Flag:** the caption changed from "revolving credit facilities" to "credit facilities," the size rose from $10.0bn to $11.7bn, and for the first time in the period reviewed an amount is **drawn**. SOFR + 1.5% to 2.25% is a wide spread for a AA-rated issuer and suggests these are not all plain corporate revolvers. No further breakdown is filed.

## 5g. DEBT CASH FLOWS

| $M | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Proceeds from issuance of debt, net of costs | 10,790 | 13,589 | **64,564** |
| Repayments of debt | (11,550) | (12,701) | **(32,427)** |
| *Net* | *(760)* | *888* | ***32,137*** |

Through FY2024 Alphabet's debt cash flows were a wash, i.e. commercial-paper churn. FY2025 is the break: **$64.6bn raised, $32.4bn repaid, $32.1bn net new money.** (The repayments line includes finance-lease principal, which was $1,988M in 2025 per Note 4 footnote 1.)

## 5h. DEBT IS ONLY PART OF IT: THE H1-2026 CAPITAL RAISE, FROM THE Q2-2026 CASH-FLOW STATEMENT

The financing section of the Q2-2026 10-Q shows a capital raise of a kind Alphabet has never previously run, and **two of the three legs are equity, not debt.**

| Financing activities, $M | H1-2025 | **H1-2026** |
|---|---:|---:|
| Net payments related to stock-based award activities | (5,731) | (12,056) |
| **Repurchases of stock** | **(28,306)** | **0** |
| Dividend payments | (4,977) | (5,231) |
| **Proceeds from issuance of common stock, net of costs** | **0** | **30,499** |
| **Proceeds from issuance of mandatory convertible preferred stock, net of costs** | **0** | **19,063** |
| Proceeds from issuance of debt, net of costs | 31,378 | 56,226 |
| Repayments of debt | (18,397) | (5,253) |
| Proceeds from sale of interest in consolidated entities, net | 400 | 3,758 |
| Other financing activities | (400) | (686) |
| **Net cash provided by (used in) financing activities** | **(26,033)** | **86,320** |

**Three things here are without precedent in the eleven years reviewed:**

1. **A $30.5bn common-stock issuance**, of which **$10.0bn was placed privately with Berkshire Hathaway.** Alphabet has been a net repurchaser of its own stock for the entire period reviewed. It issued equity in H1-2026. Q2-2026 10-Q, Note 11 Stockholders' Equity, verbatim:
   > "On **June 4, 2026**, the company completed an underwritten public offering of **29 million Class A shares at a price of $355.1982 per share and 29 million Class C shares at a price of $351.8018 per share**. All shares have a par value of $0.001 per share."
   > "Concurrently with the public offering, on June 4, 2026, the company completed a **private placement of 14 million Class A and 14 million Class C shares to an affiliate of Berkshire Hathaway Inc.** (the 'private placement')."
   > "The net proceeds received by the company were **$20.5 billion from the public offering and $10.0 billion from the private placement**, after deducting underwriting discounts, commissions, and direct offering expenses which were recorded as a reduction to common stock and APIC. **These proceeds will be used for general corporate purposes, including capital expenditures to scale AI infrastructure and global compute.**"

2. **A $19.0bn mandatory convertible preferred stock issuance.** Alphabet had no preferred stock outstanding before 2026. The Q2-2026 income statement now carries a **"Preferred stock dividends"** line ($86M in Q2-2026). Q2-2026 10-Q, Note 11, verbatim:
   > "On **June 5, 2026**, the company issued an aggregate amount of **385 million Series A and Series B depositary shares, representing 19 million shares of 6.25% Mandatory Convertible Preferred Stock**, split evenly into Series A (indexed to Class A stock) and Series B (indexed to Class C stock). Each depositary share represents a 1/20th fractional interest in a share of preferred stock."
   > "The mandatory convertible preferred stock has a par value of $0.001 per share and **liquidation preference of $1,000 per share ($50 per depositary share)**. Aggregate net proceeds were **$19.0 billion** which will be used for general corporate purposes, **including capital expenditures to scale AI infrastructure and global compute**."
   > "**Dividends are cumulative at an annual rate of 6.25%** on the liquidation preference of $1,000 per share… and **may be paid in cash, shares of common stock, or a combination of cash and shares of common stock, at the company's election.** Dividends that are declared will be payable quarterly… commencing on **August 15, 2026** and ending on, and including **May 15, 2029**."
   > "Unless earlier converted, each outstanding share will **automatically convert on the mandatory conversion date, which is on or about May 15, 2029**."

3. **Buybacks stopped dead: $28.3bn in H1-2025, $0 in H1-2026.**

**Note what the filing says the money is for.** Both equity raises carry the same stated use: "general corporate purposes, **including capital expenditures to scale AI infrastructure and global compute**." Alphabet is explicitly funding the property build in sections 1 to 3 with new equity and new debt while suspending buybacks. A 6.25% cumulative preferred is expensive money for an issuer holding $242bn of cash and marketable securities.

**Total H1-2026 external capital raised: $30,499 + $19,063 + $56,226 = $105.8bn, against $86.3bn of net financing inflow.** For a company that generated $84.9bn of operating cash flow in the same six months, this is a decisive change in funding posture and it is the counterpart to the capex and commitment figures in sections 3f and 7.

**The uses, from the same statement (investing activities, H1-2026):** purchases of PP&E $(80,598)M; **acquisitions, net of cash acquired, and purchases of intangible assets $(33,697)M** against $(353)M in H1-2025; purchases of non-marketable securities $(22,051)M against $(2,312)M. Net cash used in investing was **$(145,822)M**, up from $(40,738)M.

*(The $33.7bn acquisition and the preferred/common issuances are capital-structure and M&A matters that belong to the D-series and E-series research files; they are recorded here only because they are the funding counterpart to the property and commitment build, and because a reader of this file would otherwise conclude the capex was debt-funded alone.)*

---

# 6. LIQUIDITY

| As of Dec 31 | Cash & cash equivalents | Marketable securities | **Total cash, equiv. & marketable** | Non-marketable securities |
|---|---:|---:|---:|---:|
| 2020 | 26,465 | 110,229 | **136,694** | 20,703 |
| 2021 | 20,945 | 118,704 | **139,649** | 29,549 |
| 2022 | 21,879 | 91,883 | **113,762** | 30,492 |
| 2023 | 24,048 | 86,868 | **110,916** | 31,008 |
| 2024 | 23,466 | 72,191 | **95,657** | 37,982 |
| 2025 | **30,708** | **96,135** | **126,843** | **68,687** |
| **2026-06-30** | **55,911** | **186,563** | **242,474** | **131,461** |

*(2023 marketable securities of 86,868 is my arithmetic: total 110,916 less cash 24,048. All other cells are as filed. The 2020 non-marketable figure of 20,703 is the 2020 column of the FY2021 10-K balance sheet.)*

**Note the shape of the decade.** Total cash and marketable securities was essentially flat from 2020 to 2024 (136.7 → 95.7, in fact *down*, as buybacks absorbed the cash), then nearly tripled in eighteen months on the back of $87bn of new debt. Non-marketables were flat at $20–38bn for five years and then went to $131.5bn.

**Read the last two rows.** In eighteen months:
- total cash + marketable securities went **95,657 → 242,474**, up **$146.8bn**, while long-term debt went 10,883 → 98,165, up $87.3bn;
- **non-marketable securities went 37,982 → 131,461, up $93.5bn**, a 3.5x rise in private-company holdings. Non-marketables are the account where the H1-2026 gain sits (see the companion C2 file, item 14). The cash-flow statement shows only $5.7bn of *purchases* of non-marketable securities in all of FY2025, so the increase is overwhelmingly **mark-ups, not purchases**.

**FY2025 10-K accounting policy for non-marketables, verbatim. This is why the balance can move without cash moving:**
> "Non-marketable securities primarily consist of equity securities. We account for non-marketable equity securities through which we exercise significant influence but do not have control over the investee under the equity method. Other non-marketable equity securities that we hold are primarily accounted for under the **measurement alternative**. Under the measurement alternative, the carrying value is measured at cost, less any impairment, **plus or minus changes resulting from observable price changes in orderly transactions for identical or similar investments of the same issuer**. Adjustments are determined primarily based on a market approach as of the transaction date and are recorded as a component of OI&E."

**A single observable financing round at a third-party valuation re-prices Alphabet's whole stake and runs the gain through the income statement.** That is the mechanism behind the H1-2026 earnings figure.

---

# 7. PURCHASE COMMITMENTS AND OTHER CONTRACTUAL OBLIGATIONS

## 7a. THE TOTAL, AND ITS TRAJECTORY

| As of | **Total purchase commitments & other contractual obligations** | Of which short-term (≤12 months) | What they relate to |
|---|---:|---:|---|
| 2024-12-31 | **55,400** | 32,500 | "purchase orders for certain technical infrastructure… licenses, including content licenses, inventory, and network capacity" |
| 2025-12-31 | **149,100** | **113,000** | "energy take-or-pay contracts, licenses (including content licenses), and technical infrastructure and inventory orders" |
| **2026-06-30** | **811,000** | **200,700** | "technical infrastructure and inventory through long-term supply agreements and open purchase orders… content licenses and energy take-or-pay contracts" |

**$55.4bn → $149.1bn → $811.0bn in eighteen months. This is the largest single number in the filing and it is disclosed only in narrative. There is no contractual-obligations table.**

## 7b. THE VERBATIM TEXT

**FY2024 10-K, MD&A:**
> "As of December 31, 2024, we had material purchase commitments and other contractual obligations of **$55.4 billion, of which $32.5 billion was short-term**. These amounts primarily consist of purchase orders for certain technical infrastructure as well as the non-cancelable portion or the minimum cancellation fee in certain agreements related to commitments to purchase licenses, including content licenses, inventory, and network capacity."

**FY2025 10-K, MD&A, where take-or-pay now leads the list:**
> "We have material purchase commitments and other contractual obligations primarily related to **energy take-or-pay contracts**, licenses (including content licenses), and technical infrastructure and inventory orders. As of December 31, 2025, the total for these commitments was **$149.1 billion, of which $113.0 billion was short-term**, mostly related to technical infrastructure and inventory orders. These amounts reflect commitments and obligations through open purchase orders as well as the **non-cancelable portion or the minimum cancellation fee** in certain agreements. For those agreements with variable terms, we do not estimate the non-cancelable obligation beyond any minimum quantities and/or pricing as of December 31, 2025. In certain instances, the amount of our contractual obligations may change based on the expected timing of order fulfillment from our suppliers."

**Q2-2026 10-Q, MD&A:**
> "As of June 30, 2026, we had material purchase commitments and other contractual obligations totaling **$811.0 billion, of which $200.7 billion was short-term**. These purchase commitments primarily relate to costs for **technical infrastructure and inventory through long-term supply agreements** and open purchase orders. Additional contractual obligations include commitments for content licenses and energy take-or-pay contracts."

**Q2-2026 10-Q, Note 10 Commitments, on the new long-term supply agreements, verbatim. THIS IS THE KEY DISCLOSURE:**
> "We have contractual obligations from contracts with remaining terms greater than one year primarily consisting of certain **long-term supply agreements to secure future production capacity for technical infrastructure and inventory components**. In addition, we have commitments for certain **energy service agreements to secure energy for data center usage**, and certain content licensing agreements. As of June 30, 2026, expected future fixed or guaranteed commitments under these agreements were **$707.0 billion, the significant majority of which related to long-term supply agreements**."
> "We expect contractual commitments under the long-term supply agreements and content licenses to generally be **fulfilled through 2030**. The energy service agreements include terms **ranging from two to 26 years, with obligations through 2054**, and generally include **take-or-pay provisions for minimum quantities of energy supply and substantive termination fees**."

**Answer to "are they datacenter/take-or-pay": YES, explicitly and on both counts.** The energy service agreements are named as take-or-pay with substantive termination fees and run to 2054. The $707.0bn bulk is long-term supply agreements to secure *production capacity* for technical infrastructure, fulfilled "generally through 2030", i.e. roughly $700bn of chip/server capacity committed over about four years.

## 7c. OTHER COMMITMENTS

**Content licences, FY2025 10-K Note 10, verbatim:**
> "We have certain content licensing agreements with future fixed or minimum guaranteed commitments of **$7.7 billion** as of December 31, 2025, of which the majority is paid quarterly through the first quarter of 2030."

**Financial guarantees / backstops, FY2025 10-K Note 10, verbatim:**
> "We provide financial guarantees to certain counterparties, in the form of **backstop agreements** with varying terms through August 2026. These backstop agreements **support counterparty procurement of long-lead time equipment for our future power purchase agreements**. As of December 31, 2025, our maximum potential amount of future payments under these guarantees was **$5.7 billion**, upon which we may receive certain assets."

**Q2-2026 10-Q, Note 10:** the same backstop programme, terms through September 2026, maximum potential future payments **$7.6 billion**, now covering "future power purchase **and energy agreements**."

**Long-term income taxes payable, Q2-2026 MD&A:**
> "As of June 30, 2026, we had long-term income taxes payable of **$11.3 billion** primarily related to unrecognized tax benefits."

**VIE future funding commitments** (see 4f): $1.1bn at 2025-12-31, **$21.9bn** at 2026-06-30, including the $20.0bn equity-derivative commitment to an unnamed private company through 2030.

## 7d. THE OFF-BALANCE-SHEET TOTAL AT 2026-06-30

Adding the filed narrative disclosures that do not appear on the balance sheet:

| Item | $bn |
|---|---:|
| Purchase commitments and other contractual obligations | **811.0** |
| Leases signed but not yet commenced | **85.2** |
| Short-term lease commencing Q3-2026 | 5.8 |
| PPA expected to be accounted for as a lease (from FY2025 note) | 9.9 |
| Financial guarantees / backstops (maximum potential) | 7.6 |
| VIE future funding commitments | 21.9 |
| **Indicative total** | **~941** |

*This is my addition of separately filed figures, not a filed total, and the items may overlap (e.g. energy take-or-pay may also sit inside the PPA figure). Treat it as an order-of-magnitude marker, not a number to carry into a computation.* Against it: $242.5bn of cash and marketable securities and $164.7bn of FY2025 operating cash flow.

---

# 8. CAPITALIZED SOFTWARE AND R&D

## 8a. IS SOFTWARE CAPEX A SEPARATE LINE? NO.

**Searched the FY2025 10-K for "capitalized software," "internal-use software," and "website development."** The **only** occurrence of "internal-use software" is in the not-yet-adopted accounting-standards paragraph. There is **no capitalized-software line in PP&E, no capitalized-software policy, and no capitalized-software disclosure anywhere in the FY2025 10-K.**

The single hit, verbatim:
> "In September 2025, the FASB issued ASU 2025-06 'Intangibles: Goodwill and Other-Internal-Use Software (Subtopic 350-40): Targeted Improvements to the Accounting for Internal-Use Software' to modernize the accounting for software costs under Subtopic 350-40… Upon adoption, **we will be required to account for internal-use software under the updated capitalization criteria.** The standard is effective for our interim and annual 2028 periods, with early adoption permitted… We are currently assessing adoption timing, the method of adoption, and the effect that the updated standard will have on our consolidated financial statements."

**Consequence:** Alphabet today capitalizes little or no software, and the PP&E categories (technical infrastructure / office space / corporate and other) contain no software bucket. **A future accounting change will force capitalization from 2028 at the latest, which will increase reported operating income and increase capex/amortization.** That is a disclosed, dated, forward change in earnings quality, not a speculation.

## 8b. IS R&D FULLY EXPENSED? YES.

No R&D capitalization policy appears in the FY2025 10-K, no development-cost asset appears in PP&E or on the balance sheet, and there is no separate intangibles note. **R&D is expensed as incurred.** (Note this is the *book* treatment; for *tax*, US R&D has been subject to capitalization and amortization since 2022, which is a driver of the cash-tax series in section 9.)

## 8c. R&D EXPENSE SERIES

| FY | R&D expense | R&D as % of revenue |
|---|---:|---:|
| 2019 | 26,018 |, |
| 2020 | 27,573 |, |
| 2021 | 31,562 |, |
| 2022 | 39,500 |, |
| 2023 | 45,427 |, |
| 2024 | 49,326 | **14%** (as filed) |
| 2025 | **61,087** | **15%** (as filed) |

**FY2025 10-K, MD&A, verbatim. Note what is inside the 2025 increase:**
> "Research and development expenses increased $11.8 billion from 2024 to 2025, primarily driven by increases in employee compensation expenses of $6.9 billion and **depreciation expense of $2.4 billion**. The increase in employee compensation expenses was primarily driven by an increase in SBC expenses of $4.2 billion, which included **an increase in a valuation-based compensation charge related to Waymo**."

Two things worth carrying forward: (i) **$2.4bn of the R&D increase is depreciation, not research**, since the AI capex is landing inside the R&D line; (ii) the **Waymo valuation-based compensation charge** is the only place in the FY2025 10-K where Waymo hits a P&L caption by name (see the companion C2 file).

---

# 9. INCOME TAXES PAID (CASH) VS PRETAX INCOME

| FY | **Cash taxes paid, net of refunds** | **Income before income taxes** | **Cash tax as % of pretax** | Source of cash-tax figure |
|---|---:|---:|---:|---|
| 2018 | 5,671 | 34,913 | **16.2%** | FY2020 10-K, supplemental CF ("cash paid for taxes") |
| 2019 | 8,203 | 39,625 | **20.7%** | FY2020 10-K, supplemental CF |
| 2020 | 4,990 | 48,082 | **10.4%** | FY2020 & FY2022 10-K, supplemental CF |
| 2021 | 13,412 | 90,734 | **14.8%** | FY2022 & FY2023 10-K |
| 2022 | 18,892 | 71,328 | **26.5%** | FY2022 & FY2023 10-K |
| 2023 | 19,164 | 85,717 | **22.4%** | FY2023 10-K & FY2025 tax note |
| 2024 | **27,353** | 119,815 | **22.8%** | FY2025 10-K, Note 14 |
| 2025 | **21,526** | **158,826** | **13.6%** | FY2025 10-K, Note 14 |

**Mean 2018–2025 = 18.4%. The 2025 collapse to 13.6% is the number to interrogate.**

**Caption caveat:** the FY2020 vintage line reads "Cash paid for **taxes**, net of refunds" (all taxes); from FY2022 it reads "Cash paid for **income taxes**, net of refunds." The 2020 figure of 4,990 is identical in both filings, so the captions appear to cover the same thing, but the 2018 and 2019 figures come only from the broader caption.

## 9a. THE 2025 CASH-TAX DROP IS EXPLAINED IN THE FILING: BONUS DEPRECIATION

Cash taxes **fell $5.8bn** in 2025 while pretax income **rose $39.0bn**. The FY2025 10-K attributes this to accelerated tax depreciation on capex:
> "…**accelerated depreciation on eligible capital expenditures**, the effects of which are included in operating cash flows for the year ended December 31, 2025."
> "…accelerated depreciation on eligible capital expenditures, and other tax law changes impacting 2025 with certain changes effective in 2026."

This is corroborated on the cash-flow statement: **deferred income taxes swung from (5,257) in 2024 to +8,348 in 2025**, a $13.6bn swing, i.e. tax deferred rather than eliminated. The $91.4bn of 2025 capex is being expensed for tax far faster than for book. **The cash-tax benefit is a timing difference tied to the capex programme, and it reverses when capex growth stops.** Do not treat the 13.6% rate as a run-rate.

## 9b. THE JURISDICTIONAL SPLIT (FY2025 10-K, Note 14)

| $M | 2023 | 2024 | 2025 |
|---|---:|---:|---:|
| US federal | 13,689 | 19,921 | **13,658** |
| US state and local | 1,224 | 2,697 | 2,919 |
| Foreign: Brazil | 1,264 | 1,101 | 1,368 |
| Foreign: Other | 2,987 | 3,634 | 3,581 |
| *Total foreign* | *4,251* | *4,735* | *4,949* |
| **Total cash paid for income taxes, net of refunds** | **19,164** | **27,353** | **21,526** |

**The entire 2025 decline is US federal** (19,921 → 13,658, down $6.3bn). Foreign cash taxes rose slightly. That is consistent with the bonus-depreciation explanation, since the capex is predominantly US.

## 9c. H1-2026

Q2-2026 10-Q: **income before income taxes of $216,165M for the six months ended June 30, 2026** (H1-2025: $75,722M), against operating income of $80,466M. The gap is the gain on equity securities; it is dissected in the companion file `C2-other-bets.md`, item 14. Note for the tax build: the H1-2026 cash-flow statement shows **deferred income taxes of +$27,538M** (H1-2025: $(1,596)M), which is the deferred tax on that unrealized gain, i.e. **a large book tax charge with no cash behind it**.

---

## OPEN ITEMS / NOT DISCLOSED: the honest register for this file

| Item | Status |
|---|---|
| Land carrying value inside technical infrastructure and office space | **NOT DISCLOSED**; blocks an exact non-depreciable strip-out |
| Intangible amortization FY2023–FY2025 | **NOT DISCLOSED** in the statements; last filed figure $641M (FY2022). UNRESEARCHED via XBRL tag |
| Explanation of the 2024 PP&E category recast ($3,945M out of corporate and other) | **NOT DISCLOSED** |
| Explanation of the FY2023 depreciation restatement (impairment stripped) | boilerplate only |
| Debt maturity schedule at 2026-06-30 | **NOT DISCLOSED** (10-Q not required to repeat it) |
| Tranche detail for "Other long-term debt" $1,686M at 2026-06-30 | **NOT DISCLOSED** |
| Counterparty to the $20.0bn VIE equity-derivative funding commitment | **NOT NAMED** |
| Counterparties / pricing of the $707.0bn long-term supply agreements | **NOT DISCLOSED** |
| Split of the $811.0bn purchase commitments beyond short-term vs total | **NOT DISCLOSED** |
| Short-term / long-term split of not-yet-commenced leases at 2026-06-30 | **NOT DISCLOSED** (given only at year ends) |
