# SHW EVIDENCE PACK — The Sherwin-Williams Company
**Built 2026-08-31 for `Test Runs/2026-08-31 Run - SHW (Sherwin-Williams) v4.1.md`.**
Every figure below is transcribed from a primary SEC filing and the document is named. Nothing
here is from an aggregator except the two lines expressly flagged as live quotes.

---
## 1. THE DOCUMENTS READ

| document | period | filed | accession | primary doc |
|---|---|---|---|---|
| **Form 10-K FY2025** | year to 2025-12-31 | 2026-02-19 | **0000089800-26-000008** | shw-20251231.htm |
| **Form 10-Q Q2 2026** | quarter to 2026-06-30 | 2026-07-28 | **0000089800-26-000049** | shw-20260630.htm |
| **DEF 14A 2026** | 2026 annual meeting | 2026-03-11 | **0000089800-26-000025** | shw-20260310.htm |
| Form 10-K FY2024 | 2024-12-31 | 2025-02-20 | 0000089800-25-000030 | shw-20241231.htm |
| Form 10-K FY2023 | 2023-12-31 | 2024-02-20 | 0000089800-24-000033 | shw-20231231.htm |
| Form 10-K FY2022 | 2022-12-31 | 2023-02-22 | 0000089800-23-000007 | shw-20221231.htm |
| Form 10-K FY2021 | 2021-12-31 | 2022-02-17 | 0000089800-22-000007 | shw-20211231.htm |
| Form 10-K FY2019 | 2019-12-31 | 2020-02-21 | 0000089800-20-000005 | shw-12312019x10k.htm |
| 8-K ex-99.1 FY2025 results + 2026 guidance | — | 2026-01-29 | 0000089800-26-000003 | shw2025yeearningsrelease.htm |
| 8-K ex-99.1 Q2 2026 results + raised guidance | — | 2026-07-28 | 0000089800-26-000046 | shwearningsrelease2q2026.htm |
| 8-K ex-99.1 FY2024 results + 2025 guidance | — | 2025-01-30 | 0000089800-25-000015 | shw2024yeearningsrelease.htm |
| 8-K item 5.02 — CFO transition | — | 2025-11-03 | 0000089800-25-000128 | shw-20251103.htm |
| **PPG Industries 10-K FY2025** | 2025-12-31 | — | (on disk, prior run) | — |
| **Axalta Coating Systems 10-K FY2025** | 2025-12-31 | — | (on disk, prior run) | — |
| **Masco Corporation 10-K FY2025** | 2025-12-31 | 2026-02-10 | **0000062996-26-000005** | mas-20251231.htm |
| RPM International — figures taken from `Test Runs/2026-08-31 Run - RPM (RPM International) v4.1.md` and its evidence pack, as instructed | FY May-2026 | — | — | — |

**Sovereign:** FRED `fredgraph.csv?id=DGS30` retrieved 2026-08-31 → **5.22% at 2026-08-28**
(5.19% 08-27, 5.18% 08-26, 5.17% 08-25, 5.23% 08-24, 5.27% 08-21). Saved as
`FRED_DGS30_2026-08-31.csv`.

**Live quotes, aggregator, FLAGGED (Yahoo chart API, 2026-08-31):** SHW **$338.81**
(344.86 on 08-28, 345.21 on 08-27, 348.66 on 08-26, 350.45 on 08-25, 346.73 on 08-24);
PPG $112.17; MAS $72.16; RPM $104.10; AXTA $36.42.

---
## 2. SHARE COUNT — the artifact check

| source | date | shares |
|---|---|---|
| **10-Q Q2 2026 cover (filed 2026-07-28)** | **2026-06-30** | **242,758,151** ← **USED** |
| 10-K FY2025 cover (filed 2026-02-19) | 2026-01-31 | 247,774,767 — **2.07% stale/high** |
| DEF 14A record date | 2026-02-25 | 247,362,348 |
| Balance sheet, 10-Q | 2026-06-30 | 242.8 million |
| Balance sheet, 10-K | 2025-12-31 | 247.7 million (247,701,463 per Note 12) |

- **One class only.** Securities registered under 12(b): *"Common Stock, par value of $0.33-1/3
  per share | SHW | New York Stock Exchange"* — a single line.
- **Preferred: none outstanding.** *"At December 31, 2025, there were 900,000,000 shares of common
  stock and 30,000,000 shares of serial preferred stock authorized… There we[re] no shares of
  serial preferred stock issued during 2025, 2024 or 2023."*
- **One qualification, found and disclosed:** *"Shares outstanding shown in the following table
  included **1,426,883 shares of common stock held in a revocable trust**"* (a rabbi trust for
  non-qualified benefit plans, consolidated). SHW excludes them from EPS; they are inside the
  cover count. 0.59% of shares. Keeping them in the cap is the conservative treatment.
- **Treasury retirement, not an economic event:** in Q4 2025 SHW retired 29,491,963 treasury
  shares, which moved Retained earnings from $7,246.3M to $1,029.4M and Treasury stock from
  $(6,988.6)M to $(84.3)M. No change in shares outstanding.
- **MARKET CAP = 242,758,151 × $338.81 = $82,248.9M.**

---
## 3. THE FILED SERIES — income statement

| ($M) | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| Net sales | 17,900.8 | 18,361.7 | 19,944.6 | 22,148.9 | 23,051.9 | 23,098.5 | **23,574.3** |
| Gross profit | 8,036.1 | 8,682.6 | 8,542.7 | 9,325.1 | 10,758.1 | 11,195.1 | **11,515.5** |
| **Gross margin** | 44.9% | 47.3% | **42.8%** | **42.1%** | 46.7% | 48.5% | **48.8%** |
| Operating income (constructed) | 2,287.2 | 2,861.3 | 2,558.9 | 3,002.9 | 3,567.7 | 3,811.8 | **3,812.9** |
| **Operating margin** | 12.78% | 15.58% | 12.83% | 13.56% | 15.48% | **16.50%** | **16.17%** |
| Interest expense | 349.3 | 340.4 | 334.7 | 390.8 | 417.5 | 415.7 | **465.0** |
| Income before taxes | 1,981.8 | 2,519.2 | 2,248.6 | 2,573.1 | 3,109.9 | 3,451.8 | **3,338.2** |
| Income taxes | 440.5 | 488.8 | 384.2 | 553.0 | 721.1 | 770.4 | **769.7** |
| **Net income** | 1,541.3 | 2,030.4 | 1,864.4 | 2,020.1 | 2,388.8 | 2,681.4 | **2,568.5** |
| Diluted EPS | 5.50 | 7.36 | 6.98 | 7.72 | 9.25 | **10.55** | 10.26 |
| Diluted shares (M) | 280.3 | 275.8 | 267.1 | 261.8 | 258.3 | 254.1 | **250.4** |
| Effective tax rate | 22.2% | 19.4% | 17.1% | 21.5% | 23.2% | 22.3% | **23.1%** |

**SHW reports no operating-income subtotal.** Operating income is constructed as
gross profit − SG&A − other general (income) expense − impairment, and reconciles exactly to
income before income taxes in every year:
2025: 11,515.5 − 7,695.0 − (−10.2) − 17.8 = **3,812.9**; then −465.0 +11.2 −20.9 = **3,338.2** ✓.
*(The FY2021 10-K presented amortisation as a separate line and SG&A ex-amortisation; the FY2023
10-K restated SG&A to include it. Totals are identical and the series above uses the
amortisation-inclusive form throughout.)*

Earlier years, from the FY2019 10-K: 2017 revenue $14,983.8M, gross margin 44.8%, operating income
$1,693.5M (**11.30%**); 2018 revenue $17,534.5M, gross margin 42.3%, operating income $1,875.6M
(**10.70%**). Both years are distorted by the Valspar acquisition (closed June 2017) and its
integration.

---
## 4. THE FILED SERIES — cash flow

| ($M) | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| **Net operating cash** | 2,321.3 | 3,408.6 | 2,244.6 | **1,919.9** | 3,521.9 | 3,153.2 | **3,451.6** |
| Depreciation | 262.1 | 268.0 | 263.1 | 264.0 | 292.3 | 297.4 | 340.3 |
| Amortisation of intangibles | 312.8 | 313.4 | 309.5 | 317.1 | 330.2 | 326.6 | 336.6 |
| **D&A total** | 574.9 | 581.4 | 572.6 | 581.1 | 622.5 | 624.0 | **676.9** |
| Non-cash lease expense | 370.8 | 381.3 | 400.7 | 416.9 | 452.7 | 460.5 | 508.6 |
| Change in operating lease liabilities | (368.4) | (371.4) | (401.4) | (405.3) | (453.4) | (460.7) | (503.7) |
| Stock-based compensation | 101.7 | 95.9 | 97.7 | 99.7 | 115.9 | 138.1 | **123.5** |
| Deferred income taxes | (131.1) | (145.3) | (80.3) | (144.8) | (88.9) | (74.9) | **+153.2** |
| **Capital expenditures** | 328.9 | 303.8 | 372.0 | 644.5 | 888.4 | **1,070.0** | **797.6** |
| Acquisitions, net of cash | 77.3 | — | 210.9 | 1,003.1 | 264.7 | 78.9 | **1,211.3** |
| Proceeds from divestiture | — | — | 122.5 | — | 103.7 | — | — |
| **Payments of cash dividends** | 420.8 | 488.0 | 587.1 | 618.5 | 623.7 | 723.4 | **789.8** |
| **Treasury stock purchased** | 778.8 | 2,446.3 | **2,752.3** | 883.2 | 1,432.0 | 1,738.8 | **1,656.4** |
| Proceeds from stock options | 154.6 | 182.7 | 192.8 | 67.3 | 111.6 | 242.0 | 140.6 |
| Proceeds from real estate financing | — | — | — | 207.3 | 306.5 | 244.2 | 40.7 |
| Income taxes PAID | — | — | — | — | 816.7 | 779.8 | **592.7** |
| Interest paid | — | — | — | — | 416.5 | 406.9 | **453.0** |
| Cash at year end | 161.8 | 226.6 | 165.7 | 198.8 | 276.8 | 210.4 | **207.2** |

**The lease mechanics:** non-cash lease expense is added back and the change in operating lease
liabilities is subtracted; in 2025 these net to +$4.9M. **Cash rent on ~5,477 leased outlets is
therefore already inside net operating cash** and requires no adjustment.

**H1 2026 (10-Q):** net operating cash **$1,486.6M** (H1 2025 $1,051.5M, +41.4%); capex
**$246.7M** (H1 2025 $370.8M); SBC $57.3M; dividends $394.6M; **treasury stock purchased
$1,837.0M** (H1 2025 $870.2M); net short-term borrowings +$1,054.0M; long-term debt proceeds
$500.0M less repayments $350.0M. Cash at 2026-06-30 **$293.5M**.

---
## 5. THE FILED SERIES — balance sheet

| ($M) | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| Cash | 226.6 | 165.7 | 198.8 | 276.8 | 210.4 | **207.2** |
| Accounts receivable, net | — | 2,352.4 | 2,563.6 | 2,467.9 | 2,388.8 | **2,791.2** |
| Inventories | — | 1,927.2 | 2,626.5 | 2,329.8 | 2,288.1 | **2,318.2** |
| Property, plant and equipment, net | — | 1,867.3 | 2,207.0 | 2,836.8 | 3,533.2 | **4,137.4** |
| Goodwill | — | 7,134.6 | 7,583.2 | 7,626.0 | 7,580.1 | **8,036.6** |
| Intangible assets | — | 4,001.5 | 4,002.0 | 3,880.5 | 3,533.2 | **3,966.1** |
| Operating lease right-of-use assets | — | 1,820.6 | 1,866.8 | 1,887.4 | 1,953.8 | **1,995.2** |
| **Total assets** | 20,401.6 | 20,666.7 | 22,594.0 | 22,954.4 | 23,632.6 | **25,901.7** |
| Accounts payable | 2,117.8 | 2,403.0 | 2,436.5 | 2,315.0 | 2,253.2 | **2,354.2** |
| Short-term borrowings | 0.1 | 763.5 | 978.1 | 374.2 | 662.4 | **1,200.5** |
| Current portion of long-term debt | 25.1 | 260.6 | 0.6 | 1,098.8 | 1,049.2 | **350.1** |
| Long-term debt | 8,266.9 | 8,590.9 | 9,591.0 | 8,377.9 | 8,176.8 | **9,320.7** |
| **Total debt** | **8,292.1** | 9,615.0 | 10,569.7 | 9,850.9 | 9,888.4 | **10,871.3** |
| Operating lease liabilities (ST + LT) | 758.9 | 1,880.4 | 1,938.2 | 1,958.8 | 2,024.9 | **2,071.3** |
| **Total shareholders' equity** | — | 4,437.2 | 3,102.1 | 3,715.8 | 4,051.2 | **4,598.3** |

**Real estate financing liability (the HQ sale-leaseback that does not qualify as a sale):**
total liability **$207.0M (2022) → $515.8M (2023) → $765.6M (2024) → $813.0M (2025)**, split
short-term $51.0M / long-term $762.0M at 2025. *"The Company received the final proceeds for the
new global headquarters in 2025 for a total of $800 million… The initial lease term includes the
construction period and extends for 30 years thereafter… The amount of the lease payments during
the initial 30 year lease term is estimated to be approximately **$1.938 billion**."*

---
## 6. THE HEADQUARTERS/R&D CAPITAL PROGRAMME — segment capex, and the (c) question

**Capital expenditures by segment, from Note 22 of the FY2025 and FY2023 10-Ks:**

| ($M) | PSG | CBG | PCG | **Administrative** | total |
|---|---|---|---|---|---|
| 2021 | 77.6 | 125.5 | 90.8 | **78.1** | 372.0 |
| 2022 | 87.3 | 295.0 | 38.7 | **223.5** | 644.5 |
| 2023 | 111.4 | 309.6 | 32.6 | **434.8** | 888.4 |
| 2024 | 141.3 | 290.3 | 15.2 | **623.2** | 1,070.0 |
| 2025 | 120.2 | 293.1 | 36.2 | **348.1** | 797.6 |
| **operating-segment total** | | | | | **293.9 · 421.0 · 453.6 · 446.8 · 449.5** |

- **The Administrative function IS the new global headquarters and R&D centre.** Note 22: *"The
  Administrative function includes the administrative expenses and assets of the Company's new
  global headquarters and research and development center."* FY2023 MD&A: *"The Administrative
  segment incurred capital expenditures primarily related to construction activities associated
  with the new headquarters and research and development center."*
- **Cumulative Administrative capex 2021–2025 = $1,707.7M**, against **$798.7M** of real-estate
  financing proceeds recognised in FINANCING activities. The capex went out through investing;
  most of the money came back through financing. **Free cash flow computed as OCF − capex is
  therefore understated for 2022–2025 by the gross build.**
- **The programme is finished.** Item 2: *"During 2025, the Company substantially completed the
  construction of its new global headquarters and research and development center."* MD&A:
  *"Buildings within Property, plant and equipment, net increased by $1.491 billion in the twelve
  months since December 31, 2024 primarily due to the new global headquarters and the R&D center
  meeting the criteria to be placed into service during 2025. **An immaterial amount** of capital
  expenditures related to finalizing the construction… will be placed into service during 2026."*
  H1 2026 capex was **$246.7M**, annualising to ~$493M.
- **Management's own maintenance-capex statement, FY2023 10-K MD&A:** *"**Core capital
  expenditures are targeted to be less than 2% of Net sales**… for investments in various
  productivity improvement and maintenance projects at existing manufacturing, distribution and
  research and development facilities and new store openings."* 2% of 2025 net sales is **$471M**;
  the operating-segment run rate is **$421M–$454M**.

**Depreciation by segment 2025:** PSG 90.2, CBG 185.3, PCG 19.0, Administrative 45.8 = 340.3.
**Amortisation 2025:** PSG 5.6, CBG 71.8, **PCG 258.3**, Administrative 0.9 = 336.6. *(The
Valspar intangibles sit almost entirely in Performance Coatings.)*

---
## 7. DIVIDENDS — the filed record

**Declared per share, split-adjusted (three-for-one split effected 2021-03-31; the FY2019 10-K
figures are pre-split and are divided by three):**

| 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | **2026 run-rate** |
|---|---|---|---|---|---|---|---|---|---|
| 1.1333 | 1.1467 | 1.5067 | 1.7867 | 2.20 | 2.40 | 2.42 | 2.86 | **3.16** | **3.20** |

- **The streak and its base year, verbatim (FY2025 10-K):** *"The 2025 annual dividend represented
  the **47th consecutive year** of increased dividend payments."* The FY2021 10-K gives the
  qualifier the later filings drop: *"the 43rd consecutive year of increased dividend payments
  **since the dividend was suspended in 1978**."*
- **The policy is an explicit payout formula, verbatim:** *"The Company's 2025 annual cash dividend
  of $3.16 per share represented **30% of 2024 diluted net income per share**. …On January 26,
  2026, the Board of Directors increased the quarterly cash dividend to **$0.80 per share**. This
  quarterly dividend, if approved in each of the remaining quarters of 2026, would result in an
  annual dividend for 2026 of **$3.20 per share, or a 31% payout of 2025 diluted net income per
  share**."*
- **No special dividend anywhere in the filed record.**
- **The 2026 raise is +1.27%** ($3.16 → $3.20) — mechanically, because 2025 diluted EPS ($10.26)
  fell below 2024's ($10.55) and the payout is anchored at ~30% of the prior year. **The 2023 raise
  was +0.83%** ($2.40 → $2.42) for the same reason.

**Growth constructions, all reproduced from the filings:**

| construction | rate |
|---|---|
| DPS 2018 → 2025 (7y) | +15.58%/yr |
| DPS 2019 → 2025 (6y) | +13.14%/yr |
| **2019 declared $1.5067 → 2026 run-rate $3.20 (7y) — the pre-2020 base** | **+11.36%/yr** ← the brief's +11.3% |
| DPS 2020 → 2025 (5y) | +12.08%/yr |
| 2020 → 2026 run-rate (6y) | +10.20%/yr |
| DPS 2021 → 2025 (4y) | +9.48%/yr |

**THE DECOMPOSITION** (payout ratio measured as actual cash dividends paid ÷ net income; each row
reconciles: (1+earnings)×(1+retirement)×(1+payout) − 1 = DPS growth):

| window | **DPS growth** | **earnings** | **share retirement** | **payout expansion** | payout, then → now |
|---|---|---|---|---|---|
| **2019 → 2025 (6y), the pre-2020 base** | **+13.14%/yr** | **+8.88%/yr — 68%** | **+1.90%/yr — 14%** | **+2.00%/yr — 15%** | 27.3% → 30.7% |
| 2020 → 2025 (5y) | +12.08%/yr | +4.81%/yr — 40% | +1.95%/yr — 16% | **+5.05%/yr — 42%** | 24.0% → 30.7% |
| 2021 → 2025 (4y) | +9.48%/yr | +8.34%/yr — 88% | +1.63%/yr — 17% | −0.59%/yr — −6% | 31.5% → 30.7% |
| 2022 → 2025 (3y) | +9.60%/yr | +8.34%/yr — 87% | +1.50%/yr — 16% | +0.14%/yr — 1% | 30.6% → 30.7% |

**The buyback wedge, stated separately:** diluted EPS grew +10.95%/yr from 2019 to 2025 against
total net income at +8.88%/yr — **a share-retirement contribution of 2.07 points a year.**
2021→2025: +10.11% EPS vs +8.34% net income, **1.77 points**. 2023→2025: +5.32% vs +3.69%,
**1.62 points**.

**Payout against worst-five-year EPS** (the brief's 0.42x):
- $3.16 ÷ worst diluted EPS 2021–25 ($6.98, in 2021) = **0.453x**
- $3.20 run-rate ÷ worst diluted EPS 2022–25 ($7.72, in 2022) = **0.415x**
- $3.16 ÷ $7.72 = 0.409x · $3.20 ÷ $6.98 = 0.458x · $3.16 ÷ five-year mean EPS ($8.95) = 0.353x
**The brief's 0.42x sits inside the band of defensible constructions (0.41x–0.46x). No verdict
turns on which is used.**

---
## 8. BUYBACKS — dollars, shares and prices paid, from Note 12 of each 10-K

| period | $M | shares | **average price** | vs $338.81 today |
|---|---|---|---|---|
| 2021 | 2,752.3 | 10,075,000 | **$273.18** | +24.0% |
| 2022 | 883.2 | 3,350,000 | **$263.64** | +28.5% |
| 2023 | 1,432.0 | 5,600,000 | **$255.72** | +32.5% |
| 2024 | 1,738.8 | 5,200,000 | **$334.38** | +1.3% |
| 2025 | 1,656.4 | 4,800,000 | **$345.09** | **−1.8%** |
| **H1 2026** | **1,837.0** | **5,600,000** | **$328.04** | +3.3% |

- Q4 2025 monthly (Item 5): October nil; **November 350,000 at $337.27**; December nil.
- Authorisation remaining: **29,625,000 shares** at 2025-12-31; **24.0 million** at 2026-06-30.
- **In June 2026 SHW entered an accelerated share repurchase for 2.5 million shares**; the forward
  component settled in July 2026 with a **$34.3 million payment** to Other capital. $58.9M was
  similarly recorded to Other capital in 2025 for ASR settlements.
- **The buyback only partly retires shares.** In 2025 SHW bought 4,800,000 shares but shares
  outstanding fell only 3,589,637 (251,291,100 → 247,701,463), because 1,103,257 option shares
  and 176,018 RSU shares were issued. **Roughly a quarter of the 2025 repurchase offset dilution.**

**CASH BRIDGE 2021–2025, from the filed statements ($M):**

| | |
|---|---|
| Net operating cash | 14,291.2 |
| Capital expenditures | (3,772.5) |
| **Free cash flow after capex** | **10,518.7** |
| Acquisitions, net of cash | (2,768.9) |
| Proceeds from divestitures | +226.2 |
| Proceeds from real estate financing transactions | +798.7 |
| Option exercise and treasury issuance proceeds | +788.0 |
| **Dividends paid** | **(3,342.5)** |
| **Treasury stock purchased** | **(8,462.7)** |
| **Net new debt** (ST +1,200.4; LT issued 4,342.4; LT repaid −2,969.6) | **+2,573.2** |
| Total debt 2020-12-31 → 2025-12-31 | 8,292.1 → **10,871.3** |
| Cash 2020-12-31 → 2025-12-31 | 226.6 → **207.2** |

**Shareholder returns of $11,805.2M against free cash flow after capex of $10,518.7M — 112%.**
The gap plus the $2,768.9M of acquisitions was funded by **$2,573.2M of net new debt** and
**$798.7M of real-estate financing**.

---
## 9. OWNER EARNINGS — three (c) cases

**Convention: owner earnings = net operating cash − stock-based compensation − (c).**

| ($M) | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| Net operating cash | 2,321.3 | 3,408.6 | 2,244.6 | 1,919.9 | 3,521.9 | 3,153.2 | 3,451.6 |
| less SBC | 101.7 | 95.9 | 97.7 | 99.7 | 115.9 | 138.1 | 123.5 |
| **less (c) = TOTAL capex** | 328.9 | 303.8 | 372.0 | 644.5 | 888.4 | 1,070.0 | 797.6 |
| **= OE, total-capex end** | **1,890.7** | **3,008.9** | **1,774.9** | **1,175.7** | **2,517.6** | **1,945.1** | **2,530.5** |
| **less (c) = D&A** | 574.9 | 581.4 | 572.6 | 581.1 | 622.5 | 624.0 | 676.9 |
| **= OE, D&A end** | **1,644.7** | **2,731.3** | **1,574.3** | **1,239.1** | **2,783.5** | **2,391.1** | **2,651.2** |
| **less (c) = operating-segment capex** | n/d | n/d | 293.9 | 421.0 | 453.6 | 446.8 | 449.5 |
| **= OE, operating-capex end** | — | — | **1,853.0** | **1,399.2** | **2,952.4** | **2,568.3** | **2,878.6** |

**Window means:**

| window | OE, total capex | OE, D&A | OE, operating capex |
|---|---|---|---|
| **5-year 2021–25** *(the [E2-42] default)* | **1,988.8** | 2,127.8 | 2,330.3 |
| **3-year 2023–25** | 2,331.1 | 2,608.6 | **2,799.8** |
| 7-year 2019–25 | 2,120.5 | 2,145.0 | — |
| 5-year 2019–23 | 2,073.6 | 1,994.6 | — |

**BOTTOM BOUNDARY [E5-34] = $1,988.8M. TOP OF RANGE = $2,799.8M. Width 40.8%.**

**Growth in TOTAL owner earnings:**

| window | OE (total capex) | OE (D&A) | revenue | operating income |
|---|---|---|---|---|
| 2019 → 2025 (6y) | **+4.98%/yr** | +8.28%/yr | +4.70%/yr | +8.89%/yr |
| 2021 → 2025 (4y) | +9.27%/yr | +13.92%/yr | +4.27%/yr | +10.48%/yr |
| 2022 → 2025 (3y) | +29.11%/yr | +28.86%/yr | +2.10%/yr | +8.29%/yr |
| **2023 → 2025 (2y)** | **+0.26%/yr** | **−2.41%/yr** | +1.13%/yr | +3.38%/yr |

---
## 10. RETURN ON CAPITAL — the ITW/CSL construction

Operating income ÷ (net PP&E + inventories + trade receivables − accounts payable), with the
goodwill-and-intangibles wedge reported separately and never hidden in book equity.

| | 2021 | 2022 | 2023 | 2024 | **2025** |
|---|---|---|---|---|---|
| Operating margin | 12.83% | 13.56% | 15.48% | **16.50%** | 16.17% |
| **Return on unleveraged net tangible operating assets [E2-43]** | **68.3%** | 60.5% | 67.1% | 64.0% | **55.3%** |
| Same, adding operating-lease ROU assets | 46.0% | 44.0% | 49.5% | 48.2% | **42.9%** |
| Same, INCLUDING goodwill and intangibles, pre-tax | 17.20% | 18.15% | 21.20% | **22.33%** | 20.18% |
| **Same, after tax — the ITW test** | 14.26% | 14.25% | 16.29% | **17.35%** | **15.53%** |
| Goodwill + intangibles as % of total assets | 53.9% | 51.3% | 50.1% | 47.0% | **46.3%** |
| Effective tax rate | 17.1% | 21.5% | 23.2% | 22.3% | 23.1% |

**The 2025 fall in the tangible-capital return is substantially the headquarters.** Buildings in
net PP&E rose **$1.491 billion** in 2025 on the HQ and R&D centre being placed in service. Net PP&E
excluding roughly that amount gives net tangible operating assets of about $4,995M and a return of
about **76%** — a rising series, not a falling one. **Both readings are reported; neither is
chosen.**

---
## 11. THE COMPETITOR ROW

Same metric, same construction, each figure from the issuer's own 10-K. Operating income is
**after amortisation of acquired intangibles** in every column.

| Metric, latest fiscal year | **SHW** | **PPG** | **RPM** | **AXTA** | **MAS** |
|---|---|---|---|---|---|
| Fiscal year end | **Dec-2025** | Dec-2025 | **May-2026** | Dec-2025 | Dec-2025 |
| Revenue ($M) | **23,574.3** | 15,875 | 7,863 | 5,117 | 7,562 |
| Operating income ($M) | **3,812.9** | 2,139 | 923.5 | 735 | 1,248 |
| **Operating margin** | **16.17% — 1st** | 13.47% | 11.75% | 14.36% | **16.50%** |
| **Return on unleveraged net tangible operating assets [E2-43]** | **55.3% — 1st** | 32.6% | 26.97% | 27.8% | 50.8% |
| Same, INCLUDING goodwill and intangibles, pre-tax | **20.18% — 2nd** | 14.6% | 15.56% | 13.1% | **37.97%** |
| **Same, after tax — the ITW test** | **15.53% — 2nd** | 11.3% | 11.84% | 9.1% | **28.7%** |
| Goodwill + intangibles ($M) | 12,002.7 | 8,120 | 2,513 | 2,942 | **828** |
| …as % of total assets | **46.3%** | 36.8% | 30.1% | 38.7% | **15.9% (lowest)** |
| Total debt ($M) | **10,871.3** | 7,308 | 2,534 | 3,199 | 2,947 |
| Cash ($M) | **207.2** | **2,163** | 315 | 657 | 647 |
| **Total debt / EBITDA** | **2.42x** | 2.74x | 2.23x | 3.11x | **2.09x** |
| Effective tax rate | 23.1% | 22.4% | 23.9% | 30.6% | 24.4% |
| 2025 organic / core growth | **+2.1% total; PSG same-store +1.7%** | +2% | +2.0% | −3.5% | **−3%** |
| **Price vs volume disclosed?** | **partial — Paint Stores only, in words** | **YES, full bridges** | **NO** | volume yes, price/mix partial | **YES, in words with numbers** |
| Architectural/decorative segment margin | **PSG 22.5%** | GAC not separately margined | Consumer segment | n/a | **Behr/DAP 17.24%** |
| Architectural segment direction 2025 | **sales +3.2%, profit +5.5%** | GAC sales **−2.1%** | Consumer organic negative | n/a | **sales −14%, profit −19%, volume −8%** |
| Dividend | $3.20 run-rate, **47 consecutive raises** | $628M paid | $2.16, **52 consecutive raises** | **none** | paid |

**Peers taken: 4.** SHW's own 10-K names its industry peer group for the performance graph:
*"Akzo Nobel N.V., Axalta Coating Systems Ltd., BASF SE, Genuine Parts Company, H.B. Fuller
Company, The Home Depot, Inc., Lowe's Companies, Inc., Masco Corporation, Newell Brands Inc.,
PPG Industries, Inc., RPM International Inc. and Stanley Black & Decker, Inc."*
- **Taken:** AXTA, MAS, PPG, RPM — the four that are coatings competitors and file a Form 10-K.
- **Not taken, and why:** **Akzo Nobel N.V.** and **BASF SE** are foreign private issuers that file
  no Form 10-K (the SEC rung is blocked; IFRS annual reports would have to be re-based).
  **Benjamin Moore** is a wholly-owned Berkshire Hathaway subsidiary with no separable financials —
  **the SEC rung does not exist**. **Kelly-Moore ceased operations in January 2024.**
  **Home Depot, Lowe's, Genuine Parts, Newell and Stanley Black & Decker** are channels or
  unrelated manufacturers, not coatings competitors.
- **Masco is included precisely because Behr sells through Home Depot** and is the structural
  contrast to SHW's own stores, as the brief directs. **Its figures are not a clean read-across:**
  Masco is a two-segment company of which plumbing is 66% of revenue, and its goodwill is only
  15.9% of assets because it wrote off and divested heavily in prior decades — which is why its
  return-on-total-invested-capital number is the highest in the row and means the least.

**Verbatim, the price-versus-volume disclosures, all from the same fiscal year:**
- **SHW, Paint Stores Group, FY2025:** *"Net sales in the Paint Stores Group increased 3.2%
  primarily due to **selling price increases, which impacted Net sales by a mid-single digit
  percentage, partially offset by a low-single digit decrease in sales volume**."* No split is
  given for Consumer Brands or Performance Coatings; **no gallons are disclosed anywhere** (the
  word "gallon" does not appear in the FY2025 10-K).
- **PPG, Global Architectural Coatings, FY2025:** *"● Divestitures (-3%) ● **Lower sales volumes
  (-2%)** Partially offset by: ● **Higher selling prices (+2%)** ● Favorable foreign currency
  translation (+1%)."*
- **Masco, Decorative Architectural Products, FY2025:** *"Net sales in the Decorative Architectural
  Products segment **decreased 14 percent** in 2025, primarily due to **lower sales volume which
  decreased net sales by eight percent** and the divestiture of Kichler which decreased net sales
  by six percent."*
- **Axalta, FY2025:** *"The decreased net sales were driven by **lower volumes of 4.6%**."*
- **RPM, FY2026:** *"Organic growth (decline) **includes the impact of price and volume**."* No
  split anywhere.

**The SHW paint-store price-versus-volume series, verbatim, by year:**

| year | filed language | same-store |
|---|---|---|
| 2022 *(then "The Americas Group", incl. Latin America)* | *"selling price increases as well as volume growth in all end markets"* | **+11.7%** |
| 2023 | *"**mid-single digit sales volume growth** and selling price increases, which impacted net sales by a low-single digit percentage"* | +6.8% |
| 2024 | *"sales volume growth and selling price increases, **which both impacted Net sales by a low-single digit percentage**"* | +1.7% |
| **2025** | *"selling price increases, which impacted Net sales by a **mid-single digit** percentage, partially offset by a **low-single digit decrease in sales volume**"* | **+1.7%** |
| **H1 2026** | *"selling price increases, which impacted Net sales by a low-single digit percentage, as well as **a low-single digit percentage sales volume growth**"* | **+3.4%** |
| **Q2 2026** | *"selling price increases, which impacted Net sales by a mid-single digit percentage, as well as **low-single digit percentage sales volume growth**"* | **+4.2%** |

**One year of negative volume, 2025, and it reversed in 2026.**

---
## 12. SEGMENTS

| ($M) | 2023 | 2024 | **2025** | **H1 2026** | H1 2025 |
|---|---|---|---|---|---|
| **Paint Stores Group** net sales | 12,839.5 | 13,188.0 | **13,605.9** | 6,939.9 | 6,642.0 |
| PSG segment profit | 2,860.8 | 2,902.6 | **3,061.5** | 1,516.4 | 1,457.7 |
| **PSG margin** | 22.3% | 22.0% | **22.5%** | **21.9%** | 21.9% |
| **Consumer Brands Group** external net sales | 3,365.6 | 3,108.0 | **3,166.4** | 1,891.8 | 1,571.6 |
| CBG segment profit | 309.3 | 589.9 | **509.6** | 410.1 | 296.1 |
| CBG margin on external sales | 9.2% | 19.0% | **16.1%** | 21.7% | 18.8% |
| **Performance Coatings Group** net sales | 6,843.1 | 6,797.3 | **6,795.2** | 3,619.6 | 3,403.1 |
| PCG segment profit | 991.6 | 1,027.9 | **942.7** | 505.7 | 457.8 |
| **PCG margin** | 14.5% | 15.1% | **13.9%** | 14.0% | 13.5% |
| Administrative | (1,051.8) | (1,068.6) | **(1,175.6)** | (639.9) | (572.9) |
| **Consolidated income before taxes** | 3,109.9 | 3,451.8 | **3,338.2** | 1,792.3 | 1,638.7 |

*Effective 2025-01-01 a non-significant high-performance flooring business moved from PCG to PSG;
2024 and 2023 are not recast. Latin America stores moved from the former "Americas Group" to CBG
in the 2024 re-segmentation, so pre-2023 segment figures are not comparable.*

**Outlets:** PSG **4,853** stores (US, Canada, Caribbean) at 2025-12-31, **+80 net** in 2025, +79
in 2024, +70 in 2023; CBG **307** stores in Latin America (net **−27** in 2025); PCG **317**
branches (net **−7** in 2025). Total **5,477**. *"The Paint Stores Group's objective is to grow
sales through the expansion of its store base by an approximate average of **2% each year**."*
2026 plan: *"We plan to expand our footprint by **opening 80 to 100 new stores** in the United
States and Canada in 2026."*
**Approximately 63% of Consumer Brands Group total sales in 2025 were intersegment transfers,
primarily sold through the Paint Stores Group.**
**Employees: 64,249** at 2025-12-31, ~73% in the United States → **$366,900 of revenue per
employee** (against Carlisle's $851,000).

---
## 13. GUIDANCE VERSUS OUTTURN [E3-48]

| fiscal year | guided (January 8-K ex-99.1) | outturn |
|---|---|---|
| **2025** | net sales *"up a low-single digit percentage"*; **adjusted diluted EPS $11.65–$12.05**, *"4.6% growth from 2024 at the mid-point"* | net sales **+2.1% — inside**; **adjusted EPS $11.43, +0.9% — BELOW the bottom of the range** |
| **2026** (initial, 2026-01-29) | net sales *"up by a low to mid-single digit percentage"*; **adjusted diluted EPS $11.50–$11.90**, *"an increase of 2.4% at the midpoint"* | **raised twice** |
| **2026** (raised, 2026-07-28) | net sales *"up a **mid to high-single digit** percentage"*; **adjusted diluted EPS $11.80–$12.20**; GAAP $10.92–$11.32 | open; H1 net sales **+7.2%**, H1 net income **+9.5%** |

Adjusted diluted EPS: **2024 $11.33 · 2025 $11.43 (+0.9%)**. GAAP diluted EPS 2024 $10.55, 2025
$10.26 (−2.7%). **The adjustment is Valspar acquisition-related amortisation of ~$0.80 a share**,
plus restructuring.

**2025 annual cash incentive goals, from the 2026 proxy (Petz, Mistysyn, Garceau):**

| goal | weight | threshold | target | maximum | **result** |
|---|---|---|---|---|---|
| SHW Net Sales | 25% | $21,137M | $23,485M | $23,678M | **$23,410M — below target** |
| SHW Adjusted EPS | 40% | $8.84 | $11.05 | $11.30 | **$10.71 — below target** |
| SHW Adjusted FCF | 35% | $1,198M | $1,498M | $1,538M | **$2,119M — above maximum** |

*(Segment leaders' goals include **Global Architectural RONAE**, target 109.22%, result
**109.15%**, and Global Industrial RONAE, target 51.46%, result 49.93%.)*
*"The Committee chose the **same financial performance metrics as used in 2024**."*
**Say-on-pay 2025: 91.12% of votes cast in favour.**
**Long-term equity: PRSUs vesting on adjusted EPS and adjusted average annual return on net assets
employed (Adjusted RONAE) over a three-year performance period, plus stock options.** Not
total-shareholder-return based.

---
## 14. LEAD PIGMENT AND LEAD-BASED PAINT — the filed record, dated

All from Note 11 of the FY2025 10-K and Note 9 of the Q2 2026 10-Q.

- **The accrual is nil, and SHW says so plainly:** *"We currently have **not accrued any amounts**
  for the pending lead pigment and lead-based paint litigation… because the Company does not
  believe it is probable that a loss will occur, or the Company believes it is not possible to
  estimate the range of potential losses."*
- **The public-nuisance history, verbatim:** proceedings *"brought by various states, cities and
  counties, including by the State of Rhode Island; the City of St. Louis, Missouri; various cities
  and counties in the State of New Jersey; various cities in the State of Ohio and the State of
  Ohio; the City of Chicago, Illinois; the City of Milwaukee, Wisconsin; the County of Santa Clara,
  California and other public entities in the State of California (the California Proceedings); and
  Lehigh and Montgomery Counties in Pennsylvania. **Except for the California Proceedings in which
  the Company reached a court-approved agreement in 2019 after nearly twenty years of litigation,
  all of those legal proceedings have been concluded in favor of the Company** and other
  defendants."*
- **The live matters — Wisconsin, and the date that matters is a trial date:** two federal cases
  (*Ernest Gibson v. American Cyanamid, et al.* and *Deziree and Detareion Valoe v. American
  Cyanamid, et al.*, E.D. Wis.) and one state case (*Arrieona Beal v. Armstrong Containers, Inc.,
  et al.*, Milwaukee County). **Four individual plaintiffs**, invoking *"Wisconsin's **risk
  contribution theory** (which is similar to market share liability, **except that liability can be
  joint and several**)."* **On 2024-05-07 three plaintiffs filed amended complaints adding public
  nuisance claims**; on **2024-11-08** the district court dismissed the general-negligence count
  and the abatement allegations but let the case proceed. **Discovery closes 2026-12-15.** In the
  state case, on **2025-10-06** the court entered an amended scheduling order: **trial to be
  scheduled between 2027-01-15 and 2027-03-31.**
- **Other named matters:** **NJ DEP natural-resource-damages suit filed 2019-12-18** over the
  Gibbsboro, New Jersey former plant — February 2026 trial date adjourned, status conference
  2026-03-02, new trial date to be determined. **Firetex FX9502**: in July 2024 a third-party
  certification provider changed its listing for an intumescent fire-protection coating; SHW *"has
  received claims regarding this matter"* and is investigating *"potential inaccuracies for certain
  other Firetex intumescent products"* and a Design Estimator software issue. **Carboline Global
  filed a Lanham Act false-advertising suit on 2025-09-02** arising from the same listing change.
- **Environmental accrual (a separate matter, and it is accrued):** short-term **$52.7M** and
  long-term **$224.9M** at 2025-12-31, *"the substantial majority"* relating to **Gibbsboro**,
  which is the auditor's **critical audit matter**. Provisions charged: $80.7M (2023), $(1.3)M
  (2024), $15.3M (2025); cash spent $35.3M, $24.1M, $35.1M.

---
## 15. DEBT, LIQUIDITY AND THE COVERAGE TEST

| | |
|---|---|
| Long-term debt (carrying) | **$9,670.8M** gross, of which $350.1M current |
| Short-term borrowings | **$1,200.5M** — domestic commercial paper $281.4M; **USD delayed-draw term loan $625.0M; EUR DDTL $293.6M**; foreign facilities $0.5M |
| **Total debt** | **$10,871.3M** |
| Cash | **$207.2M — 3.2 days of net sales** |
| Operating lease liabilities | $2,071.3M |
| Real-estate financing liability (HQ sale-leaseback) | **$813.0M** |
| **Gross debt / EBITDA** | **2.42x** (EBITDA = operating income $3,812.9M + D&A $676.9M = $4,489.8M) |
| Net debt / EBITDA | 2.38x |
| Lease- and RE-financing-adjusted debt / EBITDAR | **2.75x** |
| **[E2-54] coverage: (OCF − total capex) ÷ interest expense** | **(3,451.6 − 797.6) ÷ 465.0 = 5.71x** |
| Same, on the maintenance-capex figure $449.5M | **6.46x** |
| Same, in the worst year (2022) | (1,919.9 − 644.5) ÷ 390.8 = **3.26x** |
| Interest paid, cash | $453.0M (2025), $406.9M (2024), $416.5M (2023) |

**Maturities:** *"$350.1 million in 2026; $1.5 billion in 2027; $900.0 million in 2028; $800.0
million in 2029 and $1.0 billion in 2030."* The 2026 maturity was **repaid in January 2026 using
commercial paper**. **Unused committed capacity $3.649 billion** at 2025-12-31 (revolver $2.5bn to
2030-08-08, plus $875.0M and $625.0M facilities). Covenants: *"certain covenants relating to liens,
ratings changes, merger and sale of assets, **consolidated leverage** and change of control"* —
**levels not disclosed**; compliance confirmed.
**Interest expense is guided up ~$85 million in 2026** on the refinancing, the Suvinil DDTLs and
*"the incremental interest expense related to the new global headquarters and research and
development center."*

**Pension assumptions, checked for the weak-accounting flag:** domestic expected long-term return
on plan assets **6.0%**, *reduced* from 6.5%; foreign 5.1%; domestic discount rate 5.7%.
**Stock compensation is expensed** ($123.5M in 2025).

**Cash taxes as a share of pre-tax income [E4-30]:** 2023 **26.3%** · 2024 **22.6%** · 2025
**17.8%**, against book effective rates of 23.2%, 22.3%, 23.1%. **The cause is disclosed
legislation, not a tell:** *"On July 4, 2025, U.S. tax reform legislation known as the **One Big
Beautiful Bill Act**… Key provisions… include **immediate expensing of certain domestic capital
expenditures and domestic research and development costs**… The Tax Act did not materially change
the Company's effective tax rate for 2025."* MD&A: deferred income taxes on the balance sheet rose
$157.8M *"primarily due to provisions of the One Big Beautiful Bill Act."* **The 2025 operating
cash flow carries roughly $150–160M of this deferral**, and MD&A names it: *"Net operating cash
increased $298.4 million in 2025… primarily due to **an increase in Deferred income taxes** and
lower cash requirements for working capital, partially offset by lower Net income."*

---
## 16. MANAGEMENT

- **Heidi G. Petz** — Chief Executive Officer since **2024-01-01**, Chair since **2025-01-01**;
  President since 2022. Succeeded **John G. Morikis**, CEO 2016–2023, who remained Executive
  Chairman through 2024. **Two years and eight months as CEO at the run date.**
- **Beneficial ownership (proxy, record date 2026-02-25):** Petz **26,867 shares owned outright**
  plus 74,999 acquirable within 60 days = **101,866 total**, *"less than 1%"*. At $338.81 the
  owned-outright stake is roughly **$9.1M**. All 19 directors and executive officers together own
  **199,598 shares outright** (579,475 including acquirable) out of 247.4 million — **0.08%**.
- **CFO transition:** **Allen J. Mistysyn** notified the company on **2025-11-03** of his
  retirement effective 2025-12-31; **Benjamin E. Meisenzahl, 44**, elected SVP-Finance and CFO
  effective **2026-01-01**, at Sherwin-Williams since January 2004.
- **Auditor:** Ernst & Young LLP, Cleveland, Ohio, report dated **2026-02-19**; unqualified on the
  statements and on internal control; **one critical audit matter — the Gibbsboro
  environmental-related accrual.**
- **Restructuring:** provisions $47.3M (2022), $15.3M (2023), nil (2024), **$111.0M (2025)**; cash
  costs incurred $57.0M (2023), nil (2024), $71.3M (2025). Trademark impairment **$17.8M (2025)**
  in Performance Coatings, *"primarily related to restructuring activities which impacted certain
  trademarks in the Asia, Latin America and Europe regions."*

---
## 17. THE ROW'S LIMITS, STATED

- **Fiscal-year offset:** RPM reports to **May-2026** and therefore contains five months the others
  do not. Its figures are carried from this repository's own RPM run, as instructed, and are not
  re-derived here.
- **Gross margins are not comparable across the row** — SHW's cost of goods sold carries
  depreciation, distribution and research; PPG's caption is expressly *"exclusive of depreciation
  and amortization"*; Masco reports "cost of sales" on a third basis. **Only the operating-margin
  line is like-for-like**, which is why it, and not gross margin, is the row's metric.
- **SHW's tangible-capital lead narrows on a lease-adjusted basis**, because it leases roughly 5,477
  outlets: $1,995.2M of right-of-use assets against PPG's $604M, RPM's $396.9M, AXTA's $112M and
  Masco's $233M. Adding ROU to the tangible denominator: **SHW 42.9%**, PPG 29.8%, AXTA 26.6%,
  RPM 24.2%, Masco 46.3%. SHW's ranking is unchanged; its margin of superiority is not.
- **AXTA is under a signed merger agreement with AkzoNobel**, which bars repurchases, and its 30.6%
  effective rate is a break in series (Bermuda's 15% corporate income tax from 2025). Its FY2025 is
  not a clean comparison year.
- **PPG exited the US and Canada architectural coatings business in 2024**, so its
  Global Architectural Coatings segment is now mostly EMEA and Latin America and is **not** a
  like-for-like read on SHW's Paint Stores Group. *"During 2025, approximately 70% of the Company's
  total net sales were recognized outside of the United States."*
- **[E3-61] governs: the row shows position, not conduct.**

---
## 18. CUSTOMER CONCENTRATION

- **SHW:** *"Export sales and sales to any individual customer were **each less than 10 percent**
  of consolidated sales to unaffiliated customers during all years presented."* Paint Stores Group:
  *"The loss of any single customer would not have a material adverse effect on the business of
  this segment."* **Consumer Brands Group: *"had sales to certain customers that, individually, may
  be a significant portion of the sales and related profitability of the segment"* — not
  quantified.** The big-box percentage is disclosed nowhere in any SEC filing.
- **RPM:** no customer above 10% consolidated; largest customer 20% of the Consumer segment.
- **PPG:** no concentration disclosure exists.
- **AXTA:** largest customer ~5% of sales; top ten 61% of Mobility Coatings.
- **MAS:** *"We do business with home center retailers, wholesalers and a number of other
  customers"* — Behr's dependence on Home Depot is the structural fact of the segment and Masco
  does not quantify it either.
