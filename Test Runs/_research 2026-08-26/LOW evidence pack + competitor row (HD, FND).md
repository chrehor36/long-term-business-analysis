# LOW — evidence pack and competitor row
**Built 2026-08-31 for `Test Runs/2026-08-31 Run - LOW (Lowes) v4.1.md`.**
Every figure below is from a filed document. Live quotes are flagged as such.

---
## 1. DOCUMENTS PULLED (accessions recorded)

| Document | Period | Filed | Accession | Primary doc |
|---|---|---|---|---|
| **Lowe's 10-K FY2025** | 52 wks ended **2026-01-30** | 2026-03-23 | **0000060667-26-000029** | low-20260130.htm |
| Lowe's 10-Q Q2 FY2026 | 13/26 wks ended 2026-07-31 | 2026-08-27 | **0000060667-26-000117** | low-20260731.htm |
| Lowe's DEF 14A 2026 | mtg 2026-05-29 | 2026-04-16 | **0000060667-26-000056** | low-20260415.htm |
| Lowe's 10-K FY2023 | 52 wks ended 2024-02-02 | 2024-03-25 | 0000060667-24-000033 | low-20240202.htm |
| Lowe's 10-K FY2021 | 52 wks ended 2022-01-28 | 2022-03-21 | 0000060667-22-000038 | low-20220128.htm |
| Lowe's 10-K FY2010 | 52 wks ended 2011-01-28 | 2011-03-29 | 0000060667-11-000061 | (crash-era balance sheet) |
| Lowe's 8-K earnings + outlook | FY2021/22/23/24/25 Q4, Q2 FY2026 | various | 0000060667-22-000017, -23-000016, -24-000012, -25-000018, -26-000020, -26-000113 | exhibit 99.1 |
| **Home Depot 10-K FY2025** | 52 wks ended **2026-02-01** | 2026-03-18 | **0001628280-26-019436** | hd-20260201.htm |
| Floor & Decor 10-K FY2025 | ended 2025-12-25 | 2026-02-19 | 0001628280-26-009770 | fnd-20251225.htm |

**Cross-check performed [E3-27, protocol 4]:** FY2025 **operating cash flow $9,864M** appears
identically in (a) the filed Consolidated Statements of Cash Flows, (b) the MD&A Executive
Overview table, (c) the MD&A liquidity text ("cash flows from operating activities were
$9.9 billion"), and (d) the XBRL tag. Second check: **net sales $86,286M** identical in the
income statement, the Executive Overview and Note 3 (Revenue).

**53-week flag:** Lowe's fiscal year ends the Friday nearest 31 January. **FY2022 (ended
2023-02-03) was a 53-week year** — the company quantified the extra week at "approximately
$1.4 billion" of sales (FY2023 10-K MD&A). All other years in the window are 52 weeks.
**Home Depot's 53-week year was FY2024** (ended 2025-02-02), quantified at ~$2.5bn of sales
and ~$0.30 of EPS. The two duopolists' extra weeks fall in *different* years — noted so the
competitor row is not read across them naively.

**Sovereign:** FRED `fredgraph.csv?id=DGS30`, retrieved 2026-08-31. Last observation
**5.19% on 2026-08-27** (5.18% 08-26, 5.17% 08-25, 5.23% 08-24). USD; Lowe's earns
essentially all revenue in USD (US stores only since the Canadian retail sale; FBM has some
Canadian branches — FX is not quantified as material in the filing).

**Price:** $205.76, 2026-08-31, aggregator (Yahoo chart endpoint) — **live quote only,
flagged**. Prior closes $208.05 (08-28), $206.74 (08-27).

**Share count:** 10-Q cover, **561,054,019 shares outstanding at 2026-08-25**; 10-K cover
560,063,429 at 2026-03-19. **Single class** — "Common Stock, $0.50 par value" is the only
class registered under 12(b); "Securities registered pursuant to section 12(g): None";
preferred stock 5.0 million shares authorised, **"none of which have been issued"**
(Note 10). Market cap = 561.054M × $205.76 = **$115,442M**.

---
## 2. THE COMPETITOR ROW [E3-28] — same metric, same window, filing-sourced

**Peer count: 1 of the 1 national big-box home-improvement competitor**, plus one specialist
attacker for context. The issuers themselves define the structure: Lowe's calls itself
"the world's second largest home improvement retailer"; Home Depot calls itself "the world's
largest home improvement retailer based on net sales." Lowe's Item 1 "Our Competition"
describes the wider field as "highly fragmented" — hardware stores, lumber yards, paint
stores, garden centres, warehouse clubs, online retailers, wholesalers — none of which is a
national two-format peer. No peer filing was unavailable, so the moat class is **not
provisional**.

### 2a. The honest series — units, not dollars [E4-55]

| Metric, fiscal 2025 | **Lowe's** (FYE 2026-01-30) | **Home Depot** (FYE 2026-02-01) |
|---|---|---|
| Comparable sales | **+0.2%** | **+0.3%** |
| — comparable **customer transactions** | **−2.8%** | **−1.0%** |
| — comparable average ticket | **+3.0%** | **+1.4%** |
| Customer transactions (millions) | **780** | **1,601.5** |
| Average ticket | **$106.13** | **$90.56** |

Both metrics are retail-only on both sides: Lowe's footnotes transactions/ticket as
"metrics used by management to evaluate performance of our **retail locations**"; HD
footnotes that they "do not include results from HD Supply or SRS (including GMS)."

**The multi-year physical series** (transactions, millions; Lowe's restated FY2023/24 in the
FY2025 10-K to exclude certain order modifications, so the three figures below are on one
definition):

| | FY2023 | FY2024 | FY2025 | FY2026 H1 |
|---|---|---|---|---|
| **Lowe's transactions** | 827 | 801 | **780** | 416 (vs 424 PY, **−1.9%**) |
| Lowe's comp transactions % | −4.6% | n/d | **−2.8%** | Q2 **−2.1%** |
| **HD comp transactions %** | −2.9% | −1.0% | **−1.0%** | — |

Longer reach, from the earlier 10-Ks (transactions derived as net sales ÷ average ticket,
both filed): FY2019 921M → **FY2020 1,046M (boom peak)** → FY2021 1,002M → FY2022 936M
(incl. Canada) → FY2023 827M → FY2024 801M → **FY2025 780M**. Comparable-transaction
declines are filed for FY2021 (−4.2%), FY2023 (−4.6%) and FY2025 (−2.8%).

### 2b. Economics, same window

| Metric, fiscal 2025 | **Lowe's** | **Home Depot** |
|---|---|---|
| Net sales | $86,286M | $164,683M |
| — of which non-retail Pro distribution | FBM+ADG, **~$2.3bn stub** (FBM alone = 1.5% of consolidated sales) | "Other" (SRS/GMS) **$12,717M** |
| Gross margin | 33.48% | 33.3% |
| SG&A % of sales | 19.46% | 18.6% |
| **Operating margin, consolidated** | **11.77%** | **12.7%** |
| **Operating margin, retail segment** | not segmented | **13.5%** (Primary segment) |
| Net margin | 7.71% | 8.6% |
| **ROIC (each company's own definition)** | **26.1%** | **25.7%** |
| Stores | 1,759 | 2,359 |
| Pro-distribution branches | "over 540" | "over 1,250" |
| **Retail sales per store** | **~$47.7M** (ex-acquisitions) | **$64.4M** (Primary ÷ stores) |
| Operating cash flow | $9,864M | $16,325M |
| Capital expenditure | $2,213M | $3,679M |
| OCF less capex | $7,651M | $12,646M |
| Total debt (incl. current + ST) | **$39,921M** | $55,772M |
| **Total shareholders' equity** | **−$9,917M** | **+$12,813M** |
| Operating lease liabilities | $4,756M | $9,578M |
| Dividends paid | $2,636M ($4.70/sh) | $9,152M ($9.20/sh) |
| **Share repurchases (cash)** | **$211M** | **$0** |
| Debt / EBITDA | 3.23x (net 3.12x) | 2.24x |

**Both companies stopped buying their own stock in fiscal 2025 and bought a Pro building-
products distributor with debt instead** — HD acquired SRS (June 2024) then GMS via SRS
(Sept 2025); Lowe's acquired ADG (June 2025, $1.3bn) then FBM (Oct 2025, $8.8bn). This is
recorded at Q3 against [E2-30] behaviour (4), peer imitation.

### 2c. Context peer — Floor & Decor (FND 10-K FY2025)
Comparable store sales **−1.8%** (FY2025) after **−7.1%** (FY2024); 270 warehouse stores
(from 251). The specialist growth attacker is *also* negative on comps. The filing's own
diagnosis: "mortgage interest rates remain high and existing home sales remain low, which
together have reduced home remodeling activity … We have seen pressure on customer traffic
and average ticket sizes." Included only to establish that the demand slack is
**category-wide**, not a Lowe's execution failure — which is the honest reading and it cuts
*against* the bear case on Q2.

### 2d. The row's limit [E3-61]
The row shows relative position. It cannot show conduct. HD and LOW have run structurally
identical formats for forty years and produced persistently different unit economics; the
corpus's own answer is that "you'd have to know the people involved," and it declines to
model that.

---
## 3. NEITHER COMPANY QUANTIFIES PRO MIX IN ITS 10-K — an UNRESEARCHED metric, named

The structural argument for the duopoly's asymmetry is HD's higher Pro penetration.
**Neither 10-K states Pro as a percentage of sales.** Lowe's Item 1 describes its Pro focus
as "primarily the small to medium sized Pro"; HD describes "two primary customer groups —
consumers (including both DIY and DIFM customers) and Pros" with no split. Lowe's proxy
discloses that "Pro Sales Growth" is a 10%-weighted bonus metric with a fiscal-2025 growth
target of **1.5%**, but not the base.

**Work order:** the Pro-share percentage lives in (i) each company's investor-day deck and
(ii) the Q4 earnings-call transcripts furnished under Item 7.01 — company IR sites, evidence
ladder rung 3. It was **not** pulled for this run, and **no Pro-share number is used
anywhere in the run's verdicts.** The filing-sourced proxies used instead are: retail sales
per store ($64.4M HD vs ~$47.7M LOW), dedicated Pro-distribution branch counts (1,250+ vs
540+), Pro-distribution revenue ($12,717M vs ~$2.3bn stub), and average ticket ($90.56 vs
$106.13, i.e. Lowe's higher ticket on far fewer transactions).

---
## 4. GUIDANCE VERSUS OUTTURN [E3-48] — Lowe's own record

Initial full-year outlook, taken from each February 8-K exhibit 99.1, against the filed
outturn:

| Year | Guided (initial) | Outturn | Read |
|---|---|---|---|
| **FY2022** | sales $97–99bn; comps −1% to +1%; **op margin 12.8–13.0%**; EPS $13.10–13.60; **ROIC "over 36%"**; buyback ~$12bn | sales $97,059M (**bottom**); comps **−0.9%** (bottom); op margin 10.46% GAAP, ~12.7% ex-Canada charges (**below**); EPS $10.17 GAAP / $13.81 adj (**above, adjusted**); **ROIC 30.4% (missed by ~6 points)**; buyback $14.1bn (above) | mixed; ROIC badly missed |
| **FY2023** | sales ~$88–90bn; comps flat to −2%; **op margin 13.6–13.8%**; EPS $13.60–14.00 | sales $86,377M (**below**); comps **−4.7%** (**far below**); op margin 13.38% (**below**); EPS $13.20 / $13.09 adj (**below**) | **missed every line** |
| **FY2024** | sales $84–85bn; comps −2% to −3%; **op margin 12.6–12.7%** | sales $83,674M (**below**); comps −2.7% (within); op margin 12.51% (**below**); EPS $12.23 / $11.99 adj | missed sales and margin |
| **FY2025** | sales $83.5–84.5bn; comps flat to +1%; **op margin 12.3–12.4%**; net interest ~$1.3bn; D&A ~$1.8bn; EPS $12.15–12.40; capex ~$2.5bn | sales $86,286M (above — but only via $10.1bn of acquisitions announced *after* the guide); comps +0.2% (**low end**); op margin **11.77%**, ~12.1% adj (**below**); net interest $1,406M (**above**); D&A $2,194M (**above**); EPS **$11.85 (below)** / $12.28 adj (within); capex $2,213M (under) | **fourth consecutive operating-margin miss** |
| **FY2026** | Feb 2026: sales $92–94bn; comps flat to +2%; op margin 11.2–11.4% (adj 11.6–11.8%); EPS $11.75–12.25 (adj $12.25–12.75) | **Aug 19 2026: cut to the bottom of every range** — sales $92.0bn; comps flat; op margin 11.2%; EPS ~$11.75 | live; already reduced |

**The guided operating-margin path itself:** 13.0% (FY2022) → 13.7% (FY2023) → 12.65%
(FY2024) → 12.35% (FY2025) → **11.3% (FY2026)**. Guided down every year since FY2023, and
missed to the low side in each of the last four completed years.

**[E2-49] metric-switching check:** ROIC appeared as a *guided* line once (FY2022, "over
36%"), was missed by six points, and has not been guided since. It is still **disclosed**
every year in the 10-K, and the disclosed series falls — 35.3% (FY2021), 30.4%, 36.4%,
32.0%, **26.1%** (FY2025). The yardstick was dropped from the forward-looking statement but
not from the report. Recorded as a **partial** fire: the guidance line was disposed of after
deterioration; the reported number was not.

---
## 5. DIVIDEND INTEGRITY — the Stage 0(b) leg, from the filings

Cash dividends **declared** per share, from the Consolidated Statements of Shareholders'
Deficit and the XBRL 10-K series (`CommonStockDividendsPerShareDeclared`):

| FY | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DPS declared | 1.07 | 1.33 | 1.58 | 1.85 | 2.13 | 2.30 | **3.00** | **3.95** | 4.35 | 4.55 | **4.75** |
| y/y | | +24% | +19% | +17% | +15% | **+8%** | **+30%** | **+32%** | **+10%** | **+4.6%** | **+4.4%** |

Total dividends paid (`PaymentsOfDividendsCommonStock`, 10-K): $1,704M (FY2020) → $1,984M →
$2,370M → $2,531M → $2,566M → **$2,636M** (FY2025). **No year down. No quarter skipped
anywhere in the eleven-year filed series. No special dividend at any point** — every
distribution in the record is the regular quarterly. The FY2025 10-K states the most recent
raise plainly: "In the third quarter of fiscal 2025, we increased our quarterly dividend
payment by **4%** to $1.20 per share."

**Computed CAGRs (mine, from the filings):**
- 5-year on declared DPS, FY2020 → FY2025: 2.30 → 4.75 = **+15.6%/yr**
- from a pre-2020 base, FY2019 → FY2025 (6 yrs): 2.13 → 4.75 = **+14.3%/yr**
- 10-year, FY2015 → FY2025: 1.07 → 4.75 = **+16.1%/yr**
- **last three raises: +10.1%, +4.6%, +4.4%**

**I could not reproduce the screening pass's "+13.3% raw 5y CAGR / +13.0% from a pre-2020
base" on any window I tried** (declared DPS, paid DPS, calendar-year rates, or total
dollars). My figures are *higher* on the long windows. The screen's qualitative finding —
clean, regular-only, no cuts, no skipped quarters — **is confirmed**; its rate is not
reproduced and mine is reported instead. The discrepancy does not matter, because the
finding that does matter runs the other way and is set out at Stage 0(c) below.

---
## 6. THE CAPITAL STRUCTURE — the facts the negative-equity judgment rests on

**Balance-sheet history, filed** (`StockholdersEquity`,
`LongTermDebtAndCapitalLeaseObligations`, plus current maturities and short-term borrowings):

| At | Shareholders' equity | Total debt |
|---|---|---|
| 2009-01-30 (through the housing collapse) | **+$18,055M** | **$5,039M** |
| 2013-02-01 | +$13,857M | $9,030M |
| 2016-01-29 | +$7,654M | $11,545M |
| 2021-01-29 | +$1,437M | $21,780M |
| 2022-01-28 | −$4,816M | $24,727M |
| 2024-02-02 | −$15,050M | $35,921M |
| **2026-01-30** | **−$9,917M** | **$39,921M** |
| 2026-07-31 (Q2 FY2026) | −$7,437M | (LT ex-current $35,204M) |

**Debt terms (Note 8), read [E3-52]:** total long-term debt $39,921M, of which finance
leases $391M and current maturities $2,431M. Weighted-average coupons by tranche: 3.29%
(due through FY2030, $12,638M), 4.26% (FY2031-35, $9,140M), 5.74% (FY2036-40), 3.88%
(FY2041-45), 3.78% (FY2046-50), 4.86% (FY2051-55), 5.19% (FY2061-65), plus a $1,999M term
loan at 4.88% maturing Oct 2028. Principal maturities: FY2026 $2,350M · FY2027 $3,018M ·
FY2028 $5,005M · FY2029 $1,811M · FY2030 $2,500M · **thereafter $25,135M**. Nearly all
fixed-rate; "Fluctuations in interest rates do not have a material impact … nearly all of
our long-term debt is carried at amortized cost and consists primarily of fixed-rate
instruments" (Item 7A).

**Covenants:** "The notes contain certain restrictive covenants, none of which are expected
to impact the Company's capital resources or liquidity. The Company was in compliance with
all financial covenants." The September 2025 indenture "**does not require the Company to
maintain specified financial ratios or levels of net worth or liquidity**." And: "There are
no provisions in any agreements that would require early cash settlement of existing debt or
leases as a result of a downgrade in our debt rating or a decrease in our stock price."
**The negative book equity trips nothing.**

**Liquidity:** cash $982M + short-term investments $370M; **$5.0bn undrawn** under three
revolving facilities (2025 Credit Agreement $2.0bn to Sept 2030; 2023 Credit Agreement
$2.0bn to Sept 2028; $1.0bn 364-day to Sept 2026); **no commercial paper outstanding** at
either year-end (max outstanding at any point in FY2025: $500M). Ratings **BBB+ / Baa1,
outlook stable** at 2026-03-23.

**Asset backing:** "approximately **89% [of retail stores] are owned**, which includes
stores on leased land" (Item 2). Property, net $18,362M carrying 196 million square feet of
selling space at historical cost.

**[E2-54] coverage, computed:** cash interest paid $1,489M; all interest payable and accrued
= $1,471M expense (net of capitalised) + $25M OID/loan-cost amortisation + $3M on tax
uncertainties + $20M finance-lease interest = **$1,519M**. Cash flow available =
OCF $9,864M + cash interest $1,489M − ample capex $2,500M (FY2026 guided) = $8,853M.
**Coverage 5.83x.** Stress: OCF −11% (the peak-to-trough OCF decline actually recorded
through FY2007–FY2010) → 5.11x; −25% → 4.20x; −35% → 3.56x; **−59% → 2.00x**.

**Distributions vs owner earnings, FY2021–FY2025:** owner earnings $35,414M; dividends
$12,087M; buybacks $37,443M; **total returned $49,530M**, a **$14,116M excess** over owner
earnings — and $24,204M once the $10,088M of FY2025 acquisitions is added. Funded by debt:
**+$18,141M** over the same five years.

**Buyback prices paid (10-K "Share Repurchases" tables, settlement basis):**

| FY | amount | shares | avg price |
|---|---|---|---|
| FY2020 | $4,971M | 34.5M | $144.08 |
| FY2021 | $13,012M | 62.8M | $207.32 |
| FY2022 | $14,124M | 71.2M | $198.39 |
| FY2023 | $6,138M | 29.2M | $210.07 |
| FY2024 | $4,053M | 16.6M | $244.63 |
| FY2025 | $116M | 0.5M | $243.48 |
| **FY2021–25 total** | **$37,443M** | **180.3M** | **$207.67** |

$10.8bn remains authorised; "In fiscal 2025, the Company paused its share repurchase
program."

---
## 7. THE FY2025 ACQUISITIONS — Note 2, in full

| | ADG (2025-06-02) | FBM (2025-10-09) |
|---|---|---|
| Cash price | $1,300M | $8,778M |
| Goodwill | $366M | $3,254M |
| Intangibles | $714M | $5,041M |
| **Goodwill + intangibles as % of price** | **83%** | **94%** |
| Net tangible assets acquired | ~$220M | ~$483M |
| Customer-relationship life | 20 yrs | 20 yrs |

Combined $10,078M of purchase price against ~$0.7bn of net tangible assets; $3,620M goodwill
and $5,755M intangibles now sit on the balance sheet where $588M sat a year earlier. Purchase
price allocations are **preliminary**. "Pro forma revenue and earnings since the acquisitions
have not been provided as the acquisitions were not material to the consolidated financial
statements." FBM's aggregate assets ex-goodwill/intangibles were 4.5% of consolidated
assets, and its net sales **1.5% of consolidated net sales** (Item 9A scope exclusion).
Deloitte flagged the FBM customer-relationship valuation as a **critical audit matter**.

**First-year return, from management's own FY2026 guidance:** FY2026 sales $92.0bn (+$5.7bn,
essentially the annualisation of FBM/ADG) at a guided operating margin of **11.2%** =
$10,304M of operating income, against FY2025's $10,153M; net interest guided up to ~$1.6bn
from $1,406M. Guided pre-tax = $8,704M vs FY2025's $8,747M — **flat to slightly down after
deploying $10.1bn**. On the adjusted guide (11.6% margin) pre-tax is $9,072M, +$325M, a
**~3.2% first-year pre-tax return** on the price paid, against a 4.88% term loan.

---
## 8. LEGAL / CONDUCT SWEEP (Item 3, FY2025 10-K, read in full)

One matter is disclosed. The U.S. Attorney (C.D. Cal.) and EPA Region 9 investigated whether
Lowe's and its third-party installers complied with lead-safe recordkeeping and practices
under TSCA / the RRP Rules **and with a 2014 EPA civil consent decree**. In Q3 FY2023 the
EPA and DOJ "informed the Company that they have identified possible deviations from the
consent decree." On **2025-11-25** Lowe's, without admitting liability, agreed to a
**$12.5 million civil penalty** and a second consent decree replacing the 2014 one, lodged
and subject to public comment and court approval. Nothing else is disclosed; the general
paragraph states no proceeding is expected to be material.

Per the worked **TJX 2022** precedent this is an environmental/product-safety matter, not
financial dishonesty toward owners, and it is **not** the [E5-16] binary. It *is* a
[E5-22] latency item — a second consent decree because the first was not fully honoured —
and is carried as a Q6 watch item, where the test is whether they act on what they learn,
not the size of the fine.

---
## 9. PROXY — the compensation metrics [E4-29 check]

**Annual incentive, fiscal 2025 (DEF 14A 2026):** Sales **40%** · Operating Income **40%** ·
Inventory Turnover **10%** · Pro Sales Growth **10%**. Not an adjusted-EPS plan.
Long-term incentive: PSUs on **three-year average ROIC** with a relative-TSR modifier, plus
time-vested RSAs. Threshold payout raised from 25% to 50% for fiscal 2025; a "below target"
tier pays 85%.

Goals were set "consistent with guidance provided to the market on February 26, 2025."
Fiscal 2025 results were above target on all four metrics **after** the Committee, under
pre-published adjustment guidelines, **excluded the impacts of the ADG and FBM acquisitions**
and adjusted for $105M of unbudgeted acquisition costs — "This adjustment had the overall
effect of modestly increasing the achievement result for operating income performance."
Payout: **104.67% of target**, in a year when net earnings fell 4.4%, diluted EPS fell 3.1%,
ROIC fell 590bp and customer transactions fell 2.8%.

Hedging and pledging of company stock are prohibited. Director and executive stock-ownership
guidelines are in force.

**Total shareholder return, FY2020→FY2025 (10-K Item 5 table, $100 invested 2021-01-29):**
Lowe's **$175.63** · S&P 500 **$200.84** · S&P Retail Index **$164.12**. Beat retail;
**trailed the index** across the five years in which $37.4bn of stock was retired.

---
## 10. THE CRASH-ERA CALIBRATION [E4-40] — exposure, not experience

Filed revenue and operating cash flow through the last housing collapse (XBRL, 10-K):

| FY ended | 2008-02-01 | 2009-01-30 | 2010-01-29 | 2011-01-28 | 2012-02-03 |
|---|---|---|---|---|---|
| Net sales | $48,283M | $48,230M | $47,220M | $48,815M | $50,208M |
| Operating cash flow | $4,347M | $4,122M | $4,054M | $3,852M | $4,349M |

Peak-to-trough: **sales −2.2%, operating cash flow −11.4%.** The business never came close
to a cash-flow crisis. **But it carried $5.0bn of debt and $18.1bn of equity through it.**
It enters the current freeze with $39.9bn of debt and −$9.9bn of equity. The benign history
is exactly the kind [E4-40] calls "not only useless, but actually dangerous" as a guide,
because the balance sheet that absorbed it no longer exists — which is why the death section
in the run models the exposure arithmetically instead.
