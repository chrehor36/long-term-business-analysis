# 03 - Competitor row, attacker metric
# DICK'S SPORTING GOODS (DKS) - research file, 2026-09-02

**This file fetches and computes. It concludes nothing.** No moat claim, no verdict.

## THE METRIC

    Return on unleveraged net tangible operating assets
      = OperatingIncomeLoss (FY)
      / ( PropertyPlantAndEquipmentNet
        + InventoryNet
        + AccountsReceivableNetCurrent
        - AccountsPayableCurrent )                        [all at fiscal-year END]

Operating-lease right-of-use assets are **excluded from the denominator for every company,
consistently**. This flatters lease-heavy retailers in absolute terms; it is applied
identically across the row, so the ranking is comparable even though the level is not a
return on total capital.

**Source.** `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`, form 10-K facts
only, deduplicated by period end taking the latest accession. User-Agent
`Chris Hrehor chrehor36@gmail.com`. Pulled 2026-09-02.

**Tag fallbacks used**, per company and per year, in this priority order:
- PP&E: `PropertyPlantAndEquipmentNet` → `PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization`
- Inventory: `InventoryNet` → `RetailRelatedInventory`
- Receivables: `AccountsReceivableNetCurrent` → `ReceivablesNetCurrent` → `AccountsNotesAndLoansReceivableNetCurrent`
- Payables: `AccountsPayableCurrent` (no company in the row required a fallback)

The tag actually used is stated under each table. Where a tag does not exist for a company
or a year, the cell reads **tag absent**. Nothing is estimated.

---

# PART 1 - COMPANY BY COMPANY

## DKS - DICK'S Sporting Goods, Inc.

CIK 0001089063 · entity name on file: DICK'S Sporting Goods, Inc.

Uses `us-gaap:AccountsNotesAndLoansReceivableNetCurrent` for receivables in FY2020 onward; `AccountsReceivableNetCurrent` is tag absent. FYE 2026-01-31 is the first year consolidating Foot Locker (acquired 2025-09-08).

| FYE | OI | PP&E net | Inventory | Receivables | Accounts payable | Denominator | Return | 10-K accession | filed |
|---|---|---|---|---|---|---|---|---|---|
| 2026-01-31 | 1,095.9 | 3,512.8 | 4,907.8 | 475.9 | 1,987.0 | 6,909.5 | **15.9%** | 0001089063-26-000007 | 2026-03-27 |
| 2025-02-01 | 1,473.9 | 2,069.9 | 3,349.8 | 214.2 | 1,497.7 | 4,136.3 | **35.6%** | 0001089063-26-000007 | 2026-03-27 |
| 2024-02-03 | 1,282.4 | 1,638.2 | 2,848.8 | 114.9 | 1,288.7 | 3,313.1 | **38.7%** | 0001089063-26-000007 | 2026-03-27 |
| 2023-01-28 | 1,463.0 | 1,313.0 | 2,830.9 | 71.3 | 1,206.1 | 3,009.1 | **48.6%** | 0001089063-25-000012 | 2025-03-27 |
| 2022-01-29 | 2,034.5 | 1,319.7 | 2,297.6 | 68.3 | 1,281.3 | 2,404.2 | **84.6%** | 0001089063-24-000037 | 2024-03-28 |
| 2021-01-30 | 741.5 | 1,300.3 | 1,953.6 | 53.1 | 1,258.1 | 2,048.9 | **36.2%** | 0001089063-23-000023 | 2023-03-23 |

Tags: PP&E `PropertyPlantAndEquipmentNet` · inventory `InventoryNet` · receivables `AccountsNotesAndLoansReceivableNetCurrent` · payables `AccountsPayableCurrent`. All $M, USD.

## ASO - Academy Sports and Outdoors, Inc.

CIK 0001817358 · entity name on file: Academy Sports and Outdoors, Inc.

Fiscal year ends the Saturday nearest 31 January. Latest 10-K: FY2025, ended 2026-01-31.

| FYE | OI | PP&E net | Inventory | Receivables | Accounts payable | Denominator | Return | 10-K accession | filed |
|---|---|---|---|---|---|---|---|---|---|
| 2026-01-31 | 512.2 | 584.1 | 1,503.8 | 34.8 | 637.9 | 1,484.8 | **34.5%** | 0001817358-26-000031 | 2026-03-17 |
| 2025-02-01 | 538.6 | 525.1 | 1,308.8 | 16.8 | 612.4 | 1,238.3 | **43.5%** | 0001817358-26-000031 | 2026-03-17 |
| 2024-02-03 | 677.9 | 445.2 | 1,194.2 | 19.4 | 541.1 | 1,117.7 | **60.6%** | 0001817358-26-000031 | 2026-03-17 |
| 2023-01-28 | 846.5 | 351.4 | 1,283.5 | 16.5 | 686.5 | 965.0 | **87.7%** | 0001817358-25-000027 | 2025-03-20 |
| 2022-01-29 | 907.9 | 345.8 | 1,171.8 | 19.7 | 737.8 | 799.5 | **113.6%** | 0001817358-24-000042 | 2024-03-21 |
| 2021-01-30 | 420.4 | 378.3 | 990.0 | 17.3 | 791.4 | 594.2 | **70.8%** | 0001817358-23-000062 | 2023-03-16 |

Tags: PP&E `PropertyPlantAndEquipmentNet` · inventory `InventoryNet` · receivables `AccountsReceivableNetCurrent` · payables `AccountsPayableCurrent`. All $M, USD.

## BOOT - Boot Barn Holdings, Inc.

CIK 0001610250 · entity name on file: Boot Barn Holdings, Inc.

Fiscal year ends the last Saturday in March, so the periods do not line up with the January retailers.

| FYE | OI | PP&E net | Inventory | Receivables | Accounts payable | Denominator | Return | 10-K accession | filed |
|---|---|---|---|---|---|---|---|---|---|
| 2026-03-28 | 299.1 | 514.1 | 844.6 | 15.3 | 142.1 | 1,231.9 | **24.3%** | 0001104659-26-061346 | 2026-05-14 |
| 2025-03-29 | 239.4 | 422.1 | 747.2 | 10.3 | 134.4 | 1,045.1 | **22.9%** | 0001558370-25-007889 | 2025-05-15 |
| 2024-03-30 | 198.2 | 323.7 | 599.1 | 10.0 | 132.9 | 799.9 | **24.8%** | 0001558370-25-007889 | 2025-05-15 |
| 2023-04-01 | 231.8 | 257.1 | 589.5 | 13.1 | 134.2 | 725.5 | **31.9%** | 0001558370-25-007889 | 2025-05-15 |
| 2022-03-26 | 258.3 | 155.2 | 474.3 | 9.7 | 131.4 | 507.8 | **50.9%** | 0001558370-24-008176 | 2024-05-15 |
| 2021-03-27 | 86.3 | 110.4 | 275.8 | 12.8 | 104.6 | 294.3 | **29.3%** | 0001558370-23-010209 | 2023-05-18 |

Tags: PP&E `PropertyPlantAndEquipmentNet` · inventory `InventoryNet` · receivables `AccountsReceivableNetCurrent` · payables `AccountsPayableCurrent`. All $M, USD.

## HIBB - Hibbett Inc.

CIK 0001017480 · entity name on file: HIBBETT INC

Acquired by JD Sports July 2024. Last 10-K is FY2023, ended 2024-02-03, filed 2024-03-25. No filings after that.

| FYE | OI | PP&E net | Inventory | Receivables | Accounts payable | Denominator | Return | 10-K accession | filed |
|---|---|---|---|---|---|---|---|---|---|
| 2024-02-03 | 137.0 | 183.9 | 344.3 | 16.7 | 96.4 | 448.6 | **30.5%** | 0001017480-24-000043 | 2024-03-25 |
| 2023-01-28 | 168.4 | 169.5 | 420.8 | 12.8 | 190.6 | 412.5 | **40.8%** | 0001017480-24-000043 | 2024-03-25 |
| 2022-01-29 | 228.2 | 146.0 | 221.2 | 13.6 | 85.6 | 295.1 | **77.3%** | 0001017480-24-000043 | 2024-03-25 |
| 2021-01-30 | 98.4 | 107.2 | 202.0 | 11.9 | 107.2 | 213.9 | **46.0%** | 0001017480-23-000026 | 2023-03-24 |
| 2020-02-01 | 36.1 | 101.0 | 288.0 | 8.5 | 131.7 | 265.8 | **13.6%** | 0001017480-22-000023 | 2022-03-25 |
| 2019-02-02 | 37.5 | 115.4 | 280.3 | 9.5 | 107.3 | 297.8 | **12.6%** | 0001017480-21-000077 | 2021-04-07 |

Tags: PP&E `PropertyPlantAndEquipmentNet` · inventory `InventoryNet` · receivables `ReceivablesNetCurrent` · payables `AccountsPayableCurrent`. All $M, USD.

## SCVL - Shoe Carnival, Inc. (renamed Shoe Station Group Inc., ticker SHOE)

CIK 0000895447 · entity name on file: Shoe Carnival, Inc.

No store-count or square-footage tags in XBRL at all.

| FYE | OI | PP&E net | Inventory | Receivables | Accounts payable | Denominator | Return | 10-K accession | filed |
|---|---|---|---|---|---|---|---|---|---|
| 2026-01-31 | 66.8 | 185.6 | 439.6 | 6.4 | 79.2 | 552.4 | **12.1%** | 0001193125-26-126279 | 2026-03-26 |
| 2025-02-01 | 91.2 | 172.8 | 385.6 | 9.0 | 52.0 | 515.4 | **17.7%** | 0001193125-26-126279 | 2026-03-26 |
| 2024-02-03 | 93.5 | 168.6 | 346.4 | 2.6 | 58.3 | 459.4 | **20.4%** | 0001193125-26-126279 | 2026-03-26 |
| 2023-01-28 | 146.4 | 141.4 | 390.4 | 3.1 | 78.8 | 456.0 | **32.1%** | 0000950170-25-043195 | 2025-03-21 |
| 2022-01-29 | 207.7 | 88.5 | 285.2 | 14.2 | 69.1 | 318.8 | **65.1%** | 0000950170-24-035337 | 2024-03-22 |
| 2021-01-30 | 21.9 | 62.3 | 233.3 | 7.1 | 57.7 | 245.0 | **8.9%** | 0001564590-21-015810 | 2021-03-26 |

Tags: PP&E `PropertyPlantAndEquipmentNet` · inventory `InventoryNet` · receivables `AccountsReceivableNetCurrent` · payables `AccountsPayableCurrent`. All $M, USD.

## FL - Foot Locker, Inc.

CIK 0000850209 · entity name on file: Foot Locker, Inc.

Acquired by DICK'S 2025-09-08. Last 10-K is FY2024, ended 2025-02-01, filed 2025-03-27.

| FYE | OI | PP&E net | Inventory | Receivables | Accounts payable | Denominator | Return | 10-K accession | filed |
|---|---|---|---|---|---|---|---|---|---|
| 2025-02-01 | 103.0 | 910.0 | 1,525.0 | 156.0 | 378.0 | 2,213.0 | **4.7%** | 0001437749-25-009620 | 2025-03-27 |
| 2024-02-03 | 142.0 | 930.0 | 1,509.0 | 160.0 | 366.0 | 2,233.0 | **6.4%** | 0001437749-25-009620 | 2025-03-27 |
| 2023-01-28 | 581.0 | 920.0 | 1,643.0 | 160.0 | 492.0 | 2,231.0 | **26.0%** | 0001437749-25-009620 | 2025-03-27 |
| 2022-01-29 | 870.0 | 917.0 | 1,266.0 | 134.0 | 596.0 | 1,721.0 | **50.6%** | 0001437749-24-009866 | 2024-03-28 |
| 2021-01-30 | 309.0 | 788.0 | 923.0 | 124.0 | 402.0 | 1,433.0 | **21.6%** | 0000850209-23-000006 | 2023-03-27 |
| 2020-02-01 | 649.0 | 824.0 | 1,208.0 | 100.0 | 333.0 | 1,799.0 | **36.1%** | 0000850209-22-000003 | 2022-03-24 |

Tags: PP&E `PropertyPlantAndEquipmentNet` · inventory `InventoryNet` · receivables `ReceivablesNetCurrent` · payables `AccountsPayableCurrent`. All $M, USD.

## BGFV - Big 5 Sporting Goods Corporation

CIK 0001156388 · entity name on file: BIG 5 SPORTING GOODS CORPORATION

Calendar-ish fiscal year (Sunday nearest 31 December). Taken private in 2025; the FY2024 10-K (ended 2024-12-29, filed 2025-02-26) is the last one filed.

| FYE | OI | PP&E net | Inventory | Receivables | Accounts payable | Denominator | Return | 10-K accession | filed |
|---|---|---|---|---|---|---|---|---|---|
| 2024-12-29 | -55.6 | 51.8 | 260.3 | 10.3 | 69.7 | 252.6 | **-22.0%** | 0000950170-25-027520 | 2025-02-26 |
| 2023-12-31 | -10.7 | 58.6 | 275.8 | 9.2 | 55.2 | 288.3 | **-3.7%** | 0000950170-25-027520 | 2025-02-26 |
| 2023-01-01 | 33.5 | 58.3 | 303.5 | 12.3 | 67.4 | 306.7 | **10.9%** | 0000950170-24-021829 | 2024-02-28 |
| 2022-01-02 | 136.0 | 60.4 | 280.0 | 13.7 | 104.4 | 249.7 | **54.5%** | 0000950170-23-005451 | 2023-03-01 |
| 2021-01-03 | 76.3 | 57.2 | 251.2 | 19.9 | 80.9 | 247.4 | **30.8%** | 0001564590-21-010511 | 2021-03-03 |
| 2019-12-29 | 14.8 | 68.4 | 309.3 | 13.6 | 83.7 | 307.7 | **4.8%** | 0001564590-21-010511 | 2021-03-03 |

Tags: PP&E `PropertyPlantAndEquipmentNet` · inventory `InventoryNet` · receivables `ReceivablesNetCurrent` · payables `AccountsPayableCurrent`. All $M, USD.

## DBI - Designer Brands Inc.

CIK 0001319947 · entity name on file: DESIGNER BRANDS INC.

**Tag change, FY2025 (ended 2026-01-31).** `PropertyPlantAndEquipmentNet` is **tag absent**
at 2026-01-31. The FY2025 10-K re-tagged the line as
`PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization`
= 213.3, of which `FinanceLeaseRightOfUseAsset` = 29.5 (that same tag reads 0.0 at
2025-02-01, and the combined tag reads 208.2 at 2025-02-01, identical to
`PropertyPlantAndEquipmentNet` for that date - so the two tags are interchangeable until
finance leases appear). Property **excluding** the finance-lease ROU asset is therefore
213.3 − 29.5 = 183.8, which gives a denominator of 570.5 and a return of **8.4%**. The
table below uses the as-tagged 213.3 / 8.0%. Finance-lease ROU assets are not
operating-lease ROU assets, so neither figure violates the stated exclusion; the 0.4pp
difference is immaterial to the ranking. Flagged, not smoothed.

| FYE | OI | PP&E net | Inventory | Receivables | Accounts payable | Denominator | Return | 10-K accession | filed |
|---|---|---|---|---|---|---|---|---|---|
| 2026-01-31 | 47.8 | 213.3 | 563.5 | 59.4 | 236.2 | 600.1 | **8.0%** | 0001319947-26-000022 | 2026-03-30 |
| 2025-02-01 | 34.9 | 208.2 | 599.8 | 50.4 | 271.5 | 586.8 | **6.0%** | 0001319947-26-000022 | 2026-03-30 |
| 2024-02-03 | 72.4 | 219.9 | 571.3 | 83.6 | 289.4 | 585.5 | **12.4%** | 0001319947-26-000022 | 2026-03-30 |
| 2023-01-28 | 187.4 | 235.4 | 605.7 | 77.8 | 255.4 | 663.5 | **28.2%** | 0001319947-25-000012 | 2025-03-24 |
| 2022-01-29 | 205.2 | 256.8 | 586.4 | 199.8 | 340.9 | 702.2 | **29.2%** | 0001319947-24-000011 | 2024-03-25 |
| 2021-01-30 | -586.3 | 296.5 | 473.2 | 196.0 | 245.1 | 720.6 | **-81.4%** | 0001319947-23-000014 | 2023-03-16 |

Tags: PP&E `PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization` · inventory `InventoryNet` · receivables `AccountsReceivableNetCurrent` · payables `AccountsPayableCurrent`. All $M, USD.

## GCO - Genesco Inc.

CIK 0000018498 · entity name on file: Genesco Inc.

| FYE | OI | PP&E net | Inventory | Receivables | Accounts payable | Denominator | Return | 10-K accession | filed |
|---|---|---|---|---|---|---|---|---|---|
| 2026-01-31 | 17.3 | 237.7 | 433.9 | 39.8 | 156.7 | 554.6 | **3.1%** | 0001193125-26-123492 | 2026-03-25 |
| 2025-02-01 | 13.9 | 228.0 | 425.2 | 48.9 | 168.1 | 534.0 | **2.6%** | 0001193125-26-123492 | 2026-03-25 |
| 2024-02-03 | -13.5 | 240.3 | 379.0 | 53.6 | 114.6 | 558.2 | **-2.4%** | 0001193125-26-123492 | 2026-03-25 |
| 2023-01-28 | 93.2 | 233.7 | 458.0 | 40.8 | 145.0 | 587.6 | **15.9%** | 0000950170-25-044864 | 2025-03-26 |
| 2022-01-29 | 155.6 | 216.3 | 278.2 | 39.5 | 152.5 | 381.5 | **40.8%** | 0000950170-24-036902 | 2024-03-27 |
| 2021-01-30 | -107.2 | 207.8 | 291.0 | 31.4 | 150.4 | 379.8 | **-28.2%** | 0001564590-21-016951 | 2021-03-31 |

Tags: PP&E `PropertyPlantAndEquipmentNet` · inventory `InventoryNet` · receivables `AccountsReceivableNetCurrent` · payables `AccountsPayableCurrent`. All $M, USD.

## SPWH - Sportsman's Warehouse Holdings, Inc.

CIK 0001132105 · entity name on file: SPORTSMAN’S WAREHOUSE HOLDINGS, INC.

Uses `us-gaap:RetailRelatedInventory`, not `InventoryNet`. `InventoryNet` is tag absent for every year.

| FYE | OI | PP&E net | Inventory | Receivables | Accounts payable | Denominator | Return | 10-K accession | filed |
|---|---|---|---|---|---|---|---|---|---|
| 2026-01-31 | -37.4 | 133.3 | 312.9 | 4.4 | 44.9 | 405.6 | **-9.2%** | 0001193125-26-134702 | 2026-03-31 |
| 2025-02-01 | -18.2 | 167.8 | 342.0 | 2.4 | 64.0 | 448.2 | **-4.1%** | 0001193125-26-134702 | 2026-03-31 |
| 2024-02-03 | -25.3 | 194.5 | 354.7 | 2.1 | 56.1 | 495.2 | **-5.1%** | 0001193125-26-134702 | 2026-03-31 |
| 2023-01-28 | 58.1 | 162.6 | 399.1 | 2.1 | 61.9 | 501.8 | **11.6%** | 0000950170-25-048890 | 2025-04-02 |
| 2022-01-29 | 90.6 | 128.3 | 386.6 | 1.9 | 58.9 | 457.9 | **19.8%** | 0001558370-22-004698 | 2022-03-30 |
| 2021-01-30 | 122.7 | 99.1 | 243.4 | 0.6 | 77.4 | 265.7 | **46.2%** | 0001558370-22-004698 | 2022-03-30 |

Tags: PP&E `PropertyPlantAndEquipmentNet` · inventory `RetailRelatedInventory` · receivables `AccountsReceivableNetCurrent` · payables `AccountsPayableCurrent`. All $M, USD.

---

# PART 2 - THE TWO DICK'S YEARS, SIDE BY SIDE

The Foot Locker acquisition closed **2025-09-08**, inside fiscal 2025. FY2025 therefore
carries roughly five months of Foot Locker on the income statement and a **full** Foot
Locker balance sheet at 2026-01-31. The denominator is fully consolidated; the numerator is
not. Reading the two years as a like-for-like decline is a category error, and reading
FY2025 as the run-rate of the merged company is a different one.

| | FY2024 - standalone DICK'S | FY2025 - DICK'S + Foot Locker |
|---|---|---|
| Fiscal year end | 2025-02-01 | 2026-01-31 |
| Operating income | 1,473.9 | 1,095.9 |
| PP&E net | 2,069.9 | 3,512.8 |
| Inventories, net | 3,349.8 | 4,907.8 |
| Accounts receivable, net | 214.2 | 475.9 |
| Accounts payable | 1,497.7 | 1,987.0 |
| **Denominator** | **4,136.3** | **6,909.5** |
| **Return** | **35.6%** | **15.9%** |
| Net sales | 13,442.8 | 17,215.1 |
| Operating margin (as filed, % of net sales) | 10.96% | 6.37% |

Both years are taken from the same accession, `0001089063-26-000007` (10-K for FY2025,
filed 2026-03-27), so the FY2024 column is the comparative as most recently filed.

**What moved the denominator.** Net tangible operating assets rose 2,773.2 (+67.0%) while
operating income fell 378.0. Of that increase, the acquired Foot Locker balance sheet is
the dominant term: PP&E +1,442.9 and inventories +1,558.0. Operating lease assets, which
this metric excludes throughout, rose from 2,367.3 to 4,594.7 over the same period; they
are excluded for DICK'S exactly as they are excluded for every other company in the row.

**What moved the numerator.** As disclosed in the FY2025 10-K MD&A: the Foot Locker
Business produced a $60.0 million net loss for the stub period, and the year carries
$307.3 million after tax of acquisition-related costs (inventory assortment actions, merger
and integration costs, bridge financing fees), of which merger and integration costs of
$164.2 million sit inside operating income as a separate line (0.95% of net sales). These
figures are stated here as disclosed, not adjusted. **No normalised or pro-forma figure is
computed in this file.** If the parent run wants a clean-year number it must build it and
label it.

---

# PART 3 - STORE COUNT AND GROSS SQUARE FOOTAGE

**XBRL is not the source here.** `us-gaap:NumberOfStores` exists for most of these
companies but is inconsistently scoped (Foot Locker's tag reads 7 and 13, which is a
segment or banner count, not the store base). Square footage is **essentially absent from
XBRL for every company in the row**; the only hits are per-store averages carried as
dimensioned facts. Everything below is read from the 10-K text (Item 1 Business, Item 2
Properties, or the MD&A store-activity table) and the location is named. Where a total is
not disclosed, the cell says so. **Nothing here is derived by multiplying an average store
size by a store count.**

### DKS, DICK'S Sporting Goods, FY2025 (ended 2026-01-31)
From the store-activity table in Item 7, 10-K accession 0001089063-26-000007:

| Segment | Ending stores | Ending gross sq ft (millions) |
|---|---|---|
| DICK'S (banner) | 644 | 34.4 |
| DICK'S Field House | 42 | 2.4 |
| DICK'S House of Sport | 35 | 3.8 |
| *Total DICK'S* | *721* | *40.6* |
| Golf Galaxy | 113 | 2.5 |
| Going Going Gone! | 51 | 2.3 |
| Public Lands | 3 | 0.1 |
| *Total Other Specialty Concepts* | *167* | *4.9* |
| **Total DICK'S Business** | **888** | **45.5** |
| Foot Locker North America (FL, Champs, Kids FL, WSS) | 1,610 | 9.7 |
| Foot Locker International (Europe, Asia Pacific, atmos) | 697 | 2.8 |
| *Total owned Foot Locker stores* | *2,307* | *12.4* |
| Licensed stores (Middle East, Asia, Europe) | 254 | 1.1 |
| **Total Foot Locker Business** | **2,561** | **13.5** |
| **Combined, owned stores only** | **3,195** | **57.9** |
| **Combined, including licensed** | **3,449** | **59.0** |

Licensed stores are not company-operated and their sales are not consolidated, so the
**owned-store line (3,195 stores, 57.9 million gross sq ft) is the one that pairs with
consolidated net sales**. Columns may not recalculate due to rounding; the filing says so
itself, footnote 11.

### DKS, DICK'S Sporting Goods, FY2024 standalone (ended 2025-02-01)
From the store-activity table in the FY2024 10-K, accession 0001089063-25-000012:

| | Ending stores | Ending sq ft (millions) |
|---|---|---|
| Total DICK'S Sporting Goods | 723 | 40.1 |
| Total Other Specialty Concepts | 133 | 3.5 |
| **Total** | **856** | **43.6** |

That total **excludes** 29 Warehouse Sale locations, which the FY2024 filing calls
temporary in nature (footnote 3). The FY2025 10-K restates the same opening position to
**885 stores and 44.8 million sq ft** by folding those 29 locations and 1.3 million sq ft
back in (footnote 3 of the FY2025 table). Both figures are as filed; the difference is a
presentation change, not an estimate.

### Every other company, most recent fiscal year

| Company | FYE | Stores | Gross square footage | Where it comes from |
|---|---|---|---|---|
| **ASO** Academy | 2026-01-31 | **322** (321 leased, 1 owned) | **21.9 million** combined leased and owned store sq ft | Item 1 and Item 2. Stores range 40,000 to 130,000 gross sq ft, average approx. 70,000 |
| **FL** Foot Locker (last 10-K) | 2025-02-01 | **2,410** in 26 countries | **12.75 million gross**; 7.89 million selling | Selected operating data table, MD&A |
| **BOOT** Boot Barn | 2026-03-28 | **539** in 49 states | **6.147 million SELLING sq ft**; gross **not disclosed** | MD&A operating-metrics table. Average 11,404 selling sq ft per store |
| **SPWH** Sportsman's Warehouse | 2026-01-31 | **147** in 32 states | **approx. 5.5 million gross** | Item 2 Properties. Stores 7,500 to 75,000 gross sq ft, average approx. 37,000 |
| **HIBB** Hibbett (last 10-K) | 2024-02-03 | **1,169** in 36 states (960 Hibbett, 193 City Gear, 16 Sports Additions) | **not disclosed as a total** | Item 1. Brand averages only: Hibbett 5,800, City Gear 5,200, Sports Additions 2,900. MD&A gives only a 3.4% year-over-year change in total square footage |
| **SCVL** Shoe Carnival | 2026-01-31 | **426** in 35 states and Puerto Rico (282 Shoe Carnival, 144 Shoe Station), all leased | **not disclosed as a total** | Item 2 Properties. Stores use 8,000 to 20,000 sq ft, average approx. 11,600; selling area is greater than 80% of gross |
| **BGFV** Big 5 (last 10-K) | 2024-12-29 | **422** (414 by end of February 2025 after eight closures) | **not disclosed as a total** | Item 1. Average approx. 12,000 sq ft, range 8,000 to 15,000. The filing does disclose **same-store sales per square foot of approximately $162 for fiscal 2024** |
| **GCO** Genesco | 2026-01-31 | **1,236** (Journeys Group 965, Schuh 118, Johnston & Murphy 153) | **not disclosed as a total** | Item 1. Segment averages only: Journeys approx. 2,100, Schuh approx. 4,950, Johnston & Murphy approx. 1,950 |
| **DBI** Designer Brands | 2026-01-31 | **665** in the Retail segment (DSW 519, The Shoe Co. 118, Rubino 28) | **not disclosed** anywhere in the 10-K; Item 2 gives corporate and distribution-centre square footage only | MD&A "Number of Stores" table |

### Sales per square foot, where both halves are disclosed

Net sales are `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax` (or `Revenues`
where that tag is absent), same 10-K accessions as Part 1. Square footage is the **ending**
figure, not a monthly average, so these are not the companies' own reported productivity
metrics and will differ from them.

| Company | FYE | Net sales $M | Sq ft (M) | Sales per sq ft |
|---|---|---|---|---|
| FL Foot Locker | 2025-02-01 | 7,988.0 | 12.75 gross | **$627** gross / $1,012 selling |
| BOOT Boot Barn | 2026-03-28 | 2,253.9 | 6.147 selling | **$367** selling; no gross figure exists |
| DKS DICK'S, FY2024 standalone | 2025-02-01 | 13,442.8 | 43.6 gross | **$308** |
| ASO Academy | 2026-01-31 | 6,053.4 | 21.9 gross | **$276** |
| SPWH Sportsman's Warehouse | 2026-01-31 | 1,209.2 | 5.5 gross | **$220** |
| DKS DICK'S, FY2025 consolidated | 2026-01-31 | 17,215.1 | 57.9 gross (owned) | **$297, do not use** |

**The last row is not a real number.** Foot Locker's 12.4 million sq ft sat on the balance
sheet at year end but contributed only about five months of sales, disclosed as $3.1
billion. The DICK'S Business alone, on the same basis, is 17,215.1 minus 3,100 = 14,115.1
over 45.5 million sq ft = **$310 per gross sq ft**, and that subtraction uses the "$3.1
billion" figure as rounded in the MD&A, so it is good to roughly the nearest ten dollars.
Flagged, not smoothed.

HIBB, SCVL, BGFV, GCO and DBI cannot be given a sales-per-square-foot figure from their
filings, because no total square footage is disclosed. **Not estimated.**

---

# PART 4 - REFERENCE BLOCK: THE BRANDS

Carried from prior runs. These are **not** sporting-goods retailers; they are the vendors
and the vertically integrated brands, and they are here only to show what the metric looks
like when the asset base is a brand rather than a box. Three of the four are recomputed
here from XBRL on the identical recipe and reproduce exactly.

| Company | CIK | FYE | OI | PP&E | Inventory | Receivables | Payables | Denominator | Return | Carried figure |
|---|---|---|---|---|---|---|---|---|---|---|
| Deckers Outdoor (DECK) | 0000910521 | 2026-03-31 | 1,262.9 | 337.8 | 487.0 | 319.0 | 384.5 | 759.2 | **166.3%** | 166.3%, matches |
| lululemon (LULU) | 0001397187 | 2026-02-01 | 2,210.6 | 2,033.7 | 1,700.8 | 190.7 | 331.4 | 3,593.7 | **61.5%** | 61.5%, matches |
| On Holding (ONON) | 0001858985 | n/a | see note | n/a | n/a | n/a | n/a | n/a | n/a | **52.4%** carried |
| NIKE (NKE) | 0000320187 | 2026-05-31 | see note | 4,796.0 | 7,501.0 | 5,931.0 | 3,600.0 | 14,628.0 | **26.0%** | 26.0%, matches |

Deckers uses `AccountsPayableTradeCurrent`; lululemon uses `ReceivablesNetCurrent`. Both
are within the stated fallback order. Deckers and lululemon accessions:
`0001628280-26-037664` (filed 2026-05-22) and `0001397187-26-000020` (filed 2026-03-17).

**On Holding note.** CIK 0001858985 returns **zero `us-gaap` tags** from the companyfacts
API. On Holding is a foreign private issuer filing a 20-F under IFRS, so there are no 10-K
facts and no us-gaap taxonomy to pull. The 52.4% is carried from the prior run and **cannot
be reproduced under this recipe**. Treat it as a different measurement until someone
rebuilds it from the IFRS statements.

**NIKE note.** `us-gaap:OperatingIncomeLoss` is **tag absent for every year**. NIKE's
income statement presents no operating-income subtotal; it runs gross profit, demand
creation expense, operating overhead expense, then straight to income before income taxes.
`InventoryNet` is likewise absent after fiscal 2011; the live tag is
`InventoryFinishedGoodsNetOfReserves`. Substituting `GrossProfit` minus
`SellingGeneralAndAdministrativeExpense` = 19,911.0 minus 16,114.0 = **3,797.0** as the
numerator reproduces the carried 26.0% exactly on a denominator of 14,628.0. That is a
**derived numerator, not the specified tag**, and it is labelled as such. On the same
derivation the prior two years read 27.3% (FY2025) and 44.8% (FY2024). Accession
`0000320187-26-000088`.

---

# PART 5 - THE RANKED ROW

Most recent fiscal year filed, high to low. **Direct sporting-goods and athletic-footwear
retailers only.** DICK'S appears twice, because which DICK'S you are ranking is the whole
point.

| # | Company | Ticker | FYE | Return | Note |
|---|---|---|---|---|---|
| 1 | **DICK'S Sporting Goods, standalone** | DKS | 2025-02-01 | **35.6%** | last pre-acquisition year |
| 2 | Academy Sports and Outdoors | ASO | 2026-01-31 | **34.5%** | |
| 3 | Hibbett | HIBB | 2024-02-03 | **30.5%** | last 10-K ever filed; two years stale |
| 4 | Boot Barn Holdings | BOOT | 2026-03-28 | **24.3%** | March fiscal year |
| 5 | **DICK'S Sporting Goods, with Foot Locker** | DKS | 2026-01-31 | **15.9%** | full FL balance sheet, approx. five months of FL income |
| 6 | Shoe Carnival | SCVL | 2026-01-31 | **12.1%** | now Shoe Station Group, ticker SHOE |
| 7 | Designer Brands | DBI | 2026-01-31 | **8.0%** | 8.4% excluding the finance-lease ROU asset |
| 8 | Foot Locker | FL | 2025-02-01 | **4.7%** | last 10-K; acquired by DKS 2025-09-08 |
| 9 | Genesco | GCO | 2026-01-31 | **3.1%** | |
| 10 | Sportsman's Warehouse | SPWH | 2026-01-31 | **-9.2%** | third consecutive operating loss |
| 11 | Big 5 Sporting Goods | BGFV | 2024-12-29 | **-22.0%** | last 10-K; taken private 2025 |

With the reference brands folded in, on the same recipe:

| # | Company | FYE | Return | Kind |
|---|---|---|---|---|
| 1 | Deckers Outdoor | 2026-03-31 | 166.3% | brand |
| 2 | lululemon athletica | 2026-02-01 | 61.5% | brand, vertically integrated |
| 3 | On Holding | n/a | 52.4% | brand; carried, IFRS, not reproduced |
| 4 | DICK'S, standalone | 2025-02-01 | 35.6% | retailer |
| 5 | Academy Sports and Outdoors | 2026-01-31 | 34.5% | retailer |
| 6 | Hibbett | 2024-02-03 | 30.5% | retailer, stale |
| 7 | NIKE | 2026-05-31 | 26.0% | brand; derived numerator |
| 8 | Boot Barn | 2026-03-28 | 24.3% | retailer |
| 9 | DICK'S, with Foot Locker | 2026-01-31 | 15.9% | retailer |
| 10 | Shoe Carnival | 2026-01-31 | 12.1% | retailer |
| 11 | Designer Brands | 2026-01-31 | 8.0% | retailer |
| 12 | Foot Locker | 2025-02-01 | 4.7% | retailer |
| 13 | Genesco | 2026-01-31 | 3.1% | retailer |
| 14 | Sportsman's Warehouse | 2026-01-31 | -9.2% | retailer |
| 15 | Big 5 | 2024-12-29 | -22.0% | retailer |

**Fiscal years are not aligned.** Boot Barn's year ends in March and NIKE's in May; Big 5's
in December; Hibbett's and Foot Locker's most recent numbers are two years and one year
stale respectively, because both were acquired. Rows are as filed, not calendarised.

---

# PART 6 - VERIFICATION, AND WHAT COULD NOT BE DONE

**Cross-check against the filed statement** (operator rule 4). The DICK'S FY2025 10-K,
accession 0001089063-26-000007, Consolidated Balance Sheets as filed, in thousands:
Accounts receivable, net **475,852**; Inventories, net **4,907,823**; Property and
equipment, net **3,512,776**; Accounts payable **1,986,990**; and, excluded by the metric,
Operating lease assets **4,594,670**. Every one matches the XBRL figure used in Part 1.
Operating income is confirmed against the MD&A percentage table: 6.37% of net sales of
17,215.1 = 1,096.6 against the tagged 1,095.9, a rounding difference of the disclosed
percentage. Prior year: 10.96% of 13,442.8 = 1,473.3 against the tagged 1,473.9.

**Every company in the assigned row was computed.** Four required a documented tag
substitution, all inside the stated fallback order:

| Company | Substitution | Effect |
|---|---|---|
| SPWH | `InventoryNet` absent for all years; used `RetailRelatedInventory` | none, it is the same balance-sheet line |
| DKS | `AccountsReceivableNetCurrent` absent for all years; used `AccountsNotesAndLoansReceivableNetCurrent` | none, verified against the filed balance sheet above |
| HIBB | `AccountsReceivableNetCurrent` absent FY2021 to FY2023; used `ReceivablesNetCurrent` | none |
| DBI | `PropertyPlantAndEquipmentNet` absent at 2026-01-31 only; used the combined finance-lease tag | +0.4pp, both figures shown |

**What could not be produced, and why:**

1. **Total gross square footage for HIBB, SCVL, BGFV, GCO and DBI.** Not disclosed as a
   total in any of those 10-Ks, and absent from XBRL. Per-store and per-brand averages are
   disclosed and are quoted in Part 3, but multiplying an average by a store count is an
   estimate, and this file does not estimate.
2. **Sales per square foot for those same five companies.** Follows from (1).
3. **On Holding on this recipe.** No us-gaap facts exist; it is a 20-F / IFRS filer.
4. **NIKE on this recipe.** `OperatingIncomeLoss` is tag absent; the reproduced 26.0% uses
   a derived numerator, labelled in Part 4.
5. **A normalised DICK'S FY2025.** Deliberately not attempted. The acquisition-cost and
   stub-period figures are quoted as disclosed in Part 2 so the parent run can build one
   and own it.

**This file concludes nothing.** No moat claim, no franchise judgment, no verdict. Q2 is
the parent run's to answer.
