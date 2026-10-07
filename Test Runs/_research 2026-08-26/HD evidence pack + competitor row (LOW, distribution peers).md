# HD — evidence pack and competitor row
**Built 2026-08-31 for `Test Runs/2026-08-31 Run - HD (Home Depot) v4.1.md`.**
Every figure below is from a filed document. Live quotes are flagged as such.
Companion file: `LOW evidence pack + competitor row (HD, FND).md` (2026-08-31), whose
HD-side figures are re-checked here against Home Depot's own filings.

---
## 1. DOCUMENTS PULLED (accessions recorded)

| Document | Period | Filed | Accession | Primary doc |
|---|---|---|---|---|
| **Home Depot 10-K FY2025** | 52 wks ended **2026-02-01** | 2026-03-18 | **0001628280-26-019436** | hd-20260201.htm |
| **Home Depot 10-Q Q2 FY2026** | 13/26 wks ended **2026-08-02** | 2026-08-25 | **0001628280-26-058715** | hd-20260802.htm |
| **Home Depot DEF 14A 2026** | mtg 2026-05-21 | 2026-04-07 | **0000354950-26-000090** | hd-20260406.htm |
| Home Depot 10-K FY2024 (53 wks) | ended 2025-02-02 | 2025-03-21 | 0000354950-25-000085 | hd-20250202.htm |
| Home Depot 10-K FY2023 | ended 2024-01-28 | 2024-03-13 | 0000354950-24-000062 | hd-20240128.htm |
| Home Depot 10-K FY2021 | ended 2022-01-30 | 2022-03-23 | 0000354950-22-000070 | hd-20220130.htm |
| Home Depot 10-K FY2019 | ended 2020-02-02 | 2020-03-25 | 0000354950-20-000015 | hd10k02022020.htm |
| HD 8-K earnings + outlook | FY2021–FY2025 Q4; Q2 FY2026 | various | 0000354950-22-000025 · -23-000025 · -24-000031 · -25-000030 · -26-000026 · -26-000145 | exhibit 99.1 |
| HD 8-K — **CEO medical leave** | event 2026-08-12 | 2026-08-12 | **0000354950-26-000141** | hd-20260811.htm |
| HD 8-K — EVP portfolio expansions | event 2026-08-20 | 2026-08-21 | 0000354950-26-000148 | hd-20260820.htm |
| **Lowe's 10-K FY2025** | 52 wks ended 2026-01-30 | 2026-03-23 | **0000060667-26-000029** | low-20260130.htm — the competitor row |
| Lowe's 10-Q Q2 FY2026 | ended 2026-07-31 | 2026-08-27 | 0000060667-26-000117 | low-20260731.htm |

**Cross-check performed [E3-27, protocol 4]:** FY2025 **operating cash flow $16,325M** appears
identically in (a) the filed Consolidated Statements of Cash Flows, (b) the XBRL tag
`NetCashProvidedByUsedInOperatingActivities`, and (c) is the basis of the MD&A statement
"Net cash provided by operating activities decreased by $3.5 billion in fiscal 2025"
($19,810M − $16,325M = $3,485M). Second check: **net sales $164,683M** identical in the
income statement, the Results of Operations table, Note 2 (Segment Reporting and Net Sales,
in four separate presentations) and the Feb 2026 earnings release.

**53-week flag:** HD's fiscal year ends the Sunday nearest 31 January. **FY2024 (ended
2025-02-02) was a 53-week year** — the company quantifies the extra week at "approximately
$2.5 billion" of net sales and "approximately $0.30" of diluted EPS, and excludes the 53rd
week from every comparable metric. FY2023 and FY2025 were 52 weeks. **Lowe's 53-week year
was FY2022 (ended 2023-02-03), a different year** — noted so the row is not read across
naively.

**Sovereign:** FRED `fredgraph.csv?id=DGS30` (Federal Reserve Bank of St. Louis, 30-Year
Treasury Constant Maturity), retrieved **2026-08-31**. Last observation **5.19% on
2026-08-27** (5.18% 08-26, 5.17% 08-25, 5.23% 08-24, 5.27% 08-21). USD; HD earns 92.4% of
sales in the U.S. ($152,170M of $164,683M) with the rest in Canada and Mexico, and the
FY2025 FX effect on sales was −$307M (0.2%). **Retrieval note, stated for honesty:** three
direct fetch attempts to fred.stlouisfed.org from this session timed out; the file used is
the same-day (2026-08-31) download of the identical FRED series made for the Lowe's run and
committed as `LOW_DGS30_2026-08-31.csv`, copied here as `HD_DGS30_2026-08-31.csv`. Same
issuing authority, same series, same retrieval date. Entered as the **currently observed
rate, never a forecast** [E3-32].

**Price:** **$327.83, 2026-08-31**, aggregator (Yahoo chart endpoint) — **live quote only,
flagged**.

**Share count:** 10-Q cover, **997,689,626 shares outstanding at 2026-08-18**; 10-K cover
996,011,466 at 2026-03-04 (**0.17% stale**, not materially so). **Single class** — "Common
Stock, $0.05 Par Value Per Share" is the only class registered under 12(b); "Securities
registered pursuant to section 12(g) of the Act: None." The balance sheet shows one equity
class ("Common stock, par value $0.05; authorized: 10,000 shares; issued: 1,802 shares;
outstanding: 996 shares") and **no preferred stock line appears anywhere in the FY2025 10-K
— balance sheet, notes, or cover** (absence-claim rule: no instance found in a full-text
sweep of the filing; the Restated Charter is Exhibit 3.1 to the 8-K of 2026-05-26 if
authorisation ever needed confirming — no verdict here rests on it). Options outstanding:
2,156 thousand at a $249.25 weighted-average exercise price, 0.2% of shares.
**Market cap = 997,689,626 × $327.83 = $327,073M.**

---
## 2. THE COMPETITOR ROW [E3-28] — same metric, same window, filing-sourced

**Peer count: 1 of the 1 national big-box home-improvement competitor**, plus the named
specialty-distribution competitor set for the SRS/GMS half. Both issuers define the
structure themselves: Home Depot calls itself "the world's largest home improvement
retailer based on net sales"; Lowe's calls itself "the world's second largest." HD's Item 1
describes the field as "highly competitive, highly fragmented, and evolving." No peer
filing was unavailable, so the moat class is **not provisional**.

### 2a. The honest series — units, not dollars [E4-55]

| Metric, fiscal 2025 | **Home Depot** (FYE 2026-02-01) | **Lowe's** (FYE 2026-01-30) |
|---|---|---|
| Comparable sales | **+0.3%** | **+0.2%** |
| — comparable **customer transactions** | **−1.0%** | **−2.8%** |
| — comparable average ticket | **+1.4%** | **+3.0%** |
| Customer transactions (millions) | **1,601.5** | **780** |
| Average ticket | **$90.56** | **$106.13** |
| Q2 FY2026 comparable sales | **+1.7%** | **+0.4%** (H1) |
| Q2 FY2026 comparable transactions | **−1.0%** | **−2.1%** |

Both metrics are retail-only on both sides: HD footnotes that transactions and ticket "do
not include results from HD Supply or SRS (including GMS)"; Lowe's footnotes its as
"metrics used by management to evaluate performance of our **retail locations**."

**HD's multi-year physical series, filed:**

| | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024* | FY2025 | FY2026 H1 |
|---|---|---|---|---|---|---|---|---|
| **Customer transactions (M)** | 1,616.0 | 1,756.3 | **1,759.7** | 1,666.4 | 1,621.8 | 1,637.2 | **1,601.5** | 834.3 (vs 841.6) |
| comparable transactions % | +1.1% | +8.6% | −0.1% | **−5.4%** | **−2.9%** | **−1.0%** | **−1.0%** | **−1.2%** |
| comparable average ticket % | +2.5% | +10.5% | +11.7% | +8.8% | −0.3% | −0.9% | **+1.4%** | **+2.5%** |
| average ticket $ | 67.30 | 74.32 | 83.04 | 90.36 | 90.07 | 89.31 | **90.56** | 92.62 |
| comparable sales % | +3.5% | +19.7% | +11.4% | +3.1% | **−3.2%** | **−1.8%** | **+0.3%** | **+1.2%** |
| **sales per retail sq ft** | — | — | $604.74 | $627.17 | $604.55 | $599.92 | **NOT DISCLOSED** | — |

*FY2024 was 53 weeks; comparable metrics exclude the 53rd week. Sources: FY2025 10-K
Results of Operations table; FY2024 10-K (accession 0000354950-25-000085); FY2023 10-K;
FY2021 10-K; FY2019 10-K; Q2 FY2026 10-Q.

**Two readings, both filed, and they point in opposite directions.**
1. HD's transaction count peaked at 1,759.7M in FY2021 and has fallen four consecutive
   years to 1,601.5M (−9.0%), and is falling again in fiscal 2026.
2. **Against the pre-boom FY2019 base of 1,616.0M, HD's transaction count is essentially
   flat (−0.9% over six years). Lowe's, on the same test, is down 15.3% (921M → 780M).**
   Home Depot kept the customers the pandemic brought it. Lowe's did not.

**And one metric was withdrawn.** "Sales per retail square foot" appeared in HD's selected
financial and sales data table in the fiscal 2024 10-K ($599.92 / $604.55 / $627.17 — down
three years running) and **is absent from the fiscal 2025 10-K**. A full-text sweep of the
FY2025 10-K for "square foot"/"square feet" returns only the Item 1 store-size sentence and
the Item 2 owned-versus-leased table. No reason for the removal is given. Scored at Q3
under [E2-49].

### 2b. Economics, same window

| Metric, fiscal 2025 | **Home Depot** | **Lowe's** |
|---|---|---|
| Net sales | **$164,683M** | $86,286M |
| — retail / Primary segment | **$151,966M** | $86,286M less ~$2.3bn acquired |
| — non-retail Pro distribution | **$12,717M** (SRS incl. GMS) | ~$2.3bn stub (FBM+ADG) |
| Gross margin | 33.3% | 33.5% |
| SG&A % of sales | **18.6%** | 19.5% |
| **Operating margin, consolidated** | **12.68%** | **11.77%** |
| **Operating margin, retail segment** | **13.54%** (Primary) | not segmented |
| **Operating margin, distribution segment** | **2.49%** (Other) | not segmented |
| Net margin | 8.60% | 7.71% |
| ROIC (each company's own definition) | **25.7%** (36.7% two years ago) | 26.1% |
| Stores | **2,359** | 1,759 |
| Store square footage | **244.7M** (90% owned) | 196M selling (89% owned) |
| **Retail sales per store** | **$64.4M** | ~$47.7M |
| Pro-distribution branches | **"over 1,250"** (1,340+ at Q2 FY2026) | "over 540" |
| Operating cash flow | $16,325M | $9,864M |
| Capital expenditure | $3,679M | $2,213M |
| OCF less capex | $12,646M | $7,651M |
| Total debt (incl. ST/CP) | **$55,772M** | $39,921M |
| — of which **commercial paper** | **$4,464M** | **$0** |
| Operating lease liabilities | $9,578M | $4,756M |
| Cash and short-term investments | **$1,389M** | $1,352M |
| **Total shareholders' equity** | **+$12,813M** | **−$9,917M** |
| **Goodwill + intangibles** | **$32,673M (31.1% of assets)** | $9,853M (18.2% of assets) |
| **Return on unleveraged net tangible operating assets [E2-43]** | **36.6%** | **32.4%** |
| **— including the goodwill wedge** | **23.3%** | **24.7%** |
| Net debt / EBITDA | **2.18x** | 3.12x |
| Lease-adjusted debt / EBITDAR | **2.44x** | 3.41x |
| Dividends paid | **$9,152M ($9.20/sh)** | $2,636M ($4.70/sh) |
| Share repurchases, cash | **$0** | $211M |
| Latest dividend raise | **+1.3%** (Feb 2026) | +4.0% (Q3 FY2025) |
| **Item 5 TSR, $100 at 2021-01-29 → 2026-01-30** | **$156.25** | **$175.63** |
| — S&P 500 / S&P 500 Retail Index | $200.82 / $164.12 | $200.84 / $164.12 |

[E2-43] denominator = property, plant and equipment net + operating-lease right-of-use
assets + inventory + receivables − accounts payable. HD FY2025: 28,021 + 9,204 + 25,817 +
5,597 − 11,491 = **$57,148M**; operating income $20,890M → **36.6%**. Including goodwill and
intangibles of $32,673M: $89,821M → **23.3%**. Lowe's on the identical construction: 32.4%
and 24.7%.

**HD's [E2-43] series: FY2020 47.3% · FY2021 53.3% · FY2022 48.7% · FY2023 44.9% ·
FY2024 41.6% · FY2025 36.6%.** Lowe's: 34.1% · 41.1% · 34.9% · 39.1% · 35.4% · 32.4%.

### 2c. The distribution peer set — where SRS/GMS actually competes
HD's "Other" segment (SRS incl. GMS, plus Mingledorff's from May 2026) competes in
specialty trade distribution, not big-box retail. Named competitors in that market are
**ABC Supply** (private — no SEC filings, so no same-metric row is possible), **Beacon
Roofing Supply** (acquired by QXO in 2025 — no standalone current filing), **Builders
FirstSource**, **SiteOne Landscape Supply**, **Watsco** and **Ferguson**. Lowe's entered the
same market twelve months later with ADG and FBM.
**Metric-level UNRESEARCHED, named:** a same-window operating-margin row for ABC Supply and
QXO/Beacon was not built. Route: QXO's 10-K (EDGAR, rung 2) for Beacon; ABC Supply is
private with no filings (rung 6 unavailable). **No verdict in this run rests on that row** —
the finding used instead is HD's own filed segment margin (2.49%) against its own Primary
segment (13.54%), which is sourced from HD and needs no peer.

### 2d. The row's limit [E3-61]
The row shows relative position. It cannot show conduct. HD and LOW have run structurally
identical formats for forty years and produced persistently different unit economics; the
corpus's own answer is that "you'd have to know the people involved," and it declines to
model that.

---
## 3. NEITHER COMPANY QUANTIFIES PRO MIX — an UNRESEARCHED metric, named (unchanged from the LOW pack)

**Neither 10-K states Pro as a percentage of sales.** HD describes "two primary customer
groups — consumers (including both DIY and DIFM customers) and Pros" with no split. HD's
proxy discloses a "Pro strategic goal" measuring "the year-over-year increase in total
comparable sales in the U.S. to Pros in the Home Depot Pro Managed account portfolio" and
states explicitly that "the amount of managed account sales is competitively sensitive
information that we do not publicly disclose."

**Work order:** the Pro-share percentage lives in each company's investor-day deck and the
Q4 earnings-call transcripts furnished under Item 7.01 — company IR sites, evidence ladder
rung 3. Not pulled. **No Pro-share number is used anywhere in this run's verdicts.**
Filing-sourced proxies used instead: retail sales per store ($64.4M vs ~$47.7M), dedicated
Pro-distribution revenue ($12,717M vs ~$2.3bn), branch counts (1,250+ vs 540+), and average
ticket ($90.56 vs $106.13).

---
## 4. GUIDANCE VERSUS OUTTURN [E3-48] — HD's own record, from each February 8-K exhibit 99.1

| Year | Guided (initial, February) | Outturn (filed) | Read |
|---|---|---|---|
| **FY2022** (guided 2022-02-22) | sales and comps "slightly positive"; **operating margin approximately flat with fiscal 2021** (15.24%); net interest ~$1.5bn; tax 24.6%; EPS growth "low single digits" | sales $157,403M **+4.1%**; comps **+3.1%**; op margin **15.27%** (flat — **met**); EPS $16.69, **+7.5%** (**above**) | **MET / BEAT** |
| **FY2023** (guided 2023-02-21) | sales and comps "approximately flat"; **op margin ~14.5%**; tax 24.5%; EPS decline "mid-single digits" | sales $152,669M **−3.0% (below)**; comps **−3.2% (far below flat)**; op margin **14.21% (below)**; EPS $15.11, **−9.5% (worse than guided)** | **MISSED every line** |
| **FY2024** (guided 2024-02-20) | total sales +~1.0% incl. 53rd wk; **comps −1.0%**; ~12 new stores; gross margin ~33.9%; **op margin ~14.1%**; net interest ~$1.8bn; 53-wk EPS growth ~+1.0% | sales $159,514M **+4.5%** (above — but only via SRS, agreed 2024-03-27, *after* the guide, +$6.4bn); comps **−1.8% (below)**; gross margin **33.4% (below)**; op margin **13.49% (below)**; net interest **$2,120M (above)**; EPS **$14.91, −1.3% (below)** | **MISSED comps, margin, EPS** |
| **FY2025** (guided 2025-02-25) | total sales +~2.8%; **comps +1.0%**; ~13 new stores; gross margin ~33.4%; **op margin ~13.0%** (adj ~13.4%); net interest ~$2.2bn; EPS −3% from $14.91; adj EPS −2% from $15.24 | sales $164,683M **+3.2%** (above); comps **+0.3% (below)**; gross margin **33.3% (below)**; op margin **12.68% (below)**, adj **13.1% (below)**; net interest **$2,288M (above)**; EPS **$14.23, −4.6% (below)**; adj EPS **$14.69, −3.6% (below)** | **MISSED comps, margin, EPS** — and the guide was **cut mid-year** from −2% to ~−5% adjusted EPS (recorded in the 2026 proxy at Item 9's supporting statement) |
| **FY2026** (guided 2026-02-24, **reaffirmed 2026-08-18**) | total sales +2.5–4.5%; comps flat to +2.0%; ~15 new stores; gross margin ~33.1%; **op margin 12.4–12.6%** (adj 12.8–13.0%); tax 24.3%; net interest ~$2.3bn; EPS flat to +4.0%; capex ~2.5% of sales | live; H1 comps +1.2%, transactions −1.2%; **reaffirmed after ~$685M of IEEPA tariff refunds were booked into cost of goods sold** | live |

**The guided operating-margin path itself:** ~15.2% (FY2022, "flat") → 14.5% → 14.1% →
13.0% → **12.4–12.6%**. Guided down every year for four years, and **missed to the low side
in each of the last three completed years**. Actual path: 15.27% → 14.21% → 13.49% →
**12.68%**, a **259bp fall in three years**.

Net interest was guided below outturn in both FY2024 ($1.8bn vs $2,120M) and FY2025
($2.2bn vs $2,288M).

---
## 5. DIVIDEND — the Stage 0(b) leg, from the filings

**Declared quarterly rate, from each February earnings release headline (8-K ex-99.1):**

| Announced | Feb 2019 | Feb 2020 | Feb 2021 | Feb 2022 | Feb 2023 | Feb 2024 | Feb 2025 | **Feb 2026** |
|---|---|---|---|---|---|---|---|---|
| quarterly | $1.36 | $1.50 | $1.65 | $1.90 | $2.09 | $2.25 | $2.30 | **$2.33** |
| annualised | 5.44 | 6.00 | 6.60 | 7.60 | 8.36 | 9.00 | 9.20 | **9.32** |
| raise | +32% | +10.3% | +10.0% | **+15%** | **+10%** | **+7.7%** | **+2.2%** | **+1.3%** |

Raise percentages for FY2021–FY2025 are the company's own headline wording ("Increases
Quarterly Dividend by 15 Percent" / "10 Percent" / "7.7%" / "2.2%" / "1.3%").

**Dividends paid per share** (`CommonStockDividendsPerShareCashPaid`, 10-K):
FY2019 $5.44 · FY2020 $6.00 · FY2021 $6.60 · FY2022 $7.60 · FY2023 $8.36 · FY2024 $9.00 ·
FY2025 **$9.20**.
**Total cash dividends paid:** $5,958M (FY2019) → $6,451M → $6,985M → $7,789M → $8,383M →
$8,929M → **$9,152M** (FY2025).

**No special dividend anywhere in the filed record. No cut. No skipped quarter. No year
down.** Item 5: "We paid our first cash dividend on June 22, 1987 and have paid a cash
dividend during each subsequent quarter" — **156 consecutive quarters** as of the Feb 2026
declaration.

**Computed CAGRs (mine, from the filings):**
- 5-year on the declared annual rate, 2021 $6.60 → 2026 $9.32: **+7.15%/yr**
- **from a pre-2020 base**, 2020 rate $6.00 → 2026 $9.32 (6 yrs): **+7.62%/yr**
- from the 2019 rate $5.44 → 2026 $9.32 (7 yrs): **+7.99%/yr** ← this reproduces the
  screening pass's "+7.9% from a pre-2020 base"
- on dividends *paid* per share, FY2020 $6.00 → FY2025 $9.20: **+8.92%/yr**
- **last three raises: +7.7%, +2.2%, +1.3%**

**Payout, the screen's "0.65x worst-five-year EPS" leg — confirmed and then superseded.**
Worst diluted EPS in the last five fiscal years is FY2025's **$14.23**; the declared annual
rate is $9.32; **9.32 ÷ 14.23 = 0.655**. The screen's figure reproduces exactly. **But the
framework's denominator is owner earnings, not EPS**, and on that denominator the payout is
**71.4%** of judged owner earnings and **77.5%** of the bottom boundary (§7 below).

### The decomposition, as instructed: earnings / share retirement / payout expansion
FY2020 (ended 2021-01-31) → FY2025 (ended 2026-02-01), five years, filed figures:

| | FY2020 | FY2025 | CAGR |
|---|---|---|---|
| Net earnings | $12,866M | $14,156M | **+1.93%/yr** |
| Diluted weighted-average shares | 1,078M | 995M | −1.59%/yr → **+1.61%/yr to EPS** |
| Diluted EPS | $11.94 | $14.23 | **+3.58%/yr** |
| Dividends paid per share | $6.00 | $9.20 | **+8.92%/yr** |
| Payout ratio on EPS | **50.3%** | **64.7%** | **+5.15%/yr** |

Check: 1.0358 × 1.0515 = 1.0891 ≈ the 8.92% DPS growth. **Of the ~8.9 points of annual
dividend growth, 1.9 came from earnings, 1.6 from share retirement, and 5.2 — nearly
three-fifths — from taking the payout ratio from 50% to 65%.**

**Cash dividends as a share of owner earnings, then versus now** (owner earnings per §7):
- FY2016–FY2020 mean: dividends $4,946M ÷ owner earnings $11,004M = **45.0%**
- FY2020 alone: $6,451M ÷ $16,066M = **40.2%**
- FY2021–FY2025 mean: $8,248M ÷ $14,062M = **58.7%**
- FY2025 alone: $9,152M ÷ $12,124M = **75.5%**
- Forward run-rate: $9,298M ÷ judged $13,027M = **71.4%**

### The buyback pause and what it does to the per-share engine
- **"In March 2024, we paused share repurchases in connection with the SRS acquisition and
  do not have plans to resume share repurchases in fiscal 2026 as we seek to reduce our
  outstanding debt."** (FY2025 10-K, Liquidity and Capital Resources.)
- **$11.7 billion** of the August 2023 $15.0bn authorisation remains unused at 2026-02-01.
- Repurchases, cash-flow-statement basis: FY2021 $14,809M · FY2022 $6,696M · FY2023 $7,951M
  · FY2024 **$649M** · FY2025 **$0**.
- **Prices paid**, from the treasury-stock rollforward (cost basis) and the treasury share
  counts on the balance sheets (712M → 757M → 778M → 804M → 806M shares):

  | FY | equity-statement cost | shares retired | avg price |
  |---|---|---|---|
  | FY2021 | $15,001M | 45M | **$333.36** |
  | FY2022 | $6,504M | 21M | **$309.71** |
  | FY2023 | $8,074M | 26M | **$310.54** |
  | FY2024 | $599M | 2M | ~$300 |
  | **FY2021–24 total** | **$30,178M** | **94M** | **$321.04** |

- Diluted share count: 1,234M (FY2016) → 1,002M (FY2023) = **−18.8% in seven years**, worth
  roughly 2.9 points a year of EPS growth. Since the pause: 1,002M → 993M → **995M**, and
  **996M** in Q2 FY2026 — **the count has stopped falling and has begun to rise**, because
  employee-plan settlement now exceeds the deemed repurchases.
- **Consequence, stated plainly: two of the three engines that produced 7.6–8.9% dividend
  growth are switched off by stated policy (share retirement) or exhausted (payout
  expansion at 71% of owner earnings), and the third (earnings) is running backwards. The
  Feb 2025 and Feb 2026 raises of +2.2% and +1.3% are what the dividend looks like once the
  levers stop.**

---
## 6. THE BOOM-WINDOW TEST [E4-41] — Stage 0(c)

The five-year window is FY2021–FY2025 (years ended Jan 2022 through Feb 2026). It contains:
- **the two peak-margin years of the pandemic home-improvement boom** — FY2021 operating
  margin **15.24%** and FY2022 **15.27%**, against a pre-boom FY2019 of 14.37%;
- the **all-time peak transaction count** (FY2021, 1,759.7M);
- a **53-week year** (FY2024, ~$2.5bn of sales, ~$0.30 of EPS);
- **$24.2bn of acquisitions** adding $6.4bn (FY2024) and $12.7bn (FY2025) of low-margin
  distribution revenue.

**Part 1 — the owner-earnings LEVEL is not a boom artifact, and the filings show why.**
The peak *cash* year was FY2020 (OCF $18,839M) and it sits **outside** the window. Inside
the window the boom's reported profits were absorbed into working capital — inventory built
from $16,627M (FY2020) to $22,068M (FY2021) to $24,886M (FY2022) — and FY2023 released
$4,137M of it. FY2021+FY2022 combined OCF was **$31,186M against $47,079M of operating
income**; FY2023+FY2024 combined OCF was **$40,982M against $43,215M**. The later, lower-
margin years produced *more* cash. The operating-cash-flow convention nets both from one
audited line. Result:

| window | owner earnings (c = capex) | (c = D&A ex-intangibles) |
|---|---|---|
| **5-yr FY2021–25 (corpus default [E2-42])** | **$14,062M** | $14,163M |
| 3-yr FY2023–25 | $15,191M | $15,351M |
| 2-yr FY2024–25 | $14,004M | $14,160M |
| FY2025 alone | $12,124M | $12,289M |
| prior 5-yr FY2016–20 | $11,004M | $11,024M |

Management's own FY2026 guidance corroborates the five-year mean: sales +2.5–4.5% on
$164,683M (mid $170.4bn) at a 12.5% operating margin = ~$21.3bn of operating income, less
~$2.3bn of net interest, taxed at 24.3% = ~$14.4bn of net earnings; add ~$4.4bn of D&A and
~$0.55bn of SBC, subtract capex at 2.5% of sales (~$4.26bn) and SBC → **~$14.7bn of owner
earnings, or ~$14.2bn once the after-tax value of the one-off IEEPA tariff refund (~$518M)
is stripped [E4-41]**. That is the same place as the five-year mean. **There is no boom to
strip out of the level.**

**Part 2 — every GROWTH rate measured across the window IS a boom artifact, and is refused.**
- Revenue FY2019 $110,225M → FY2025 $164,683M reads **+6.9%/yr** and is meaningless: it
  contains the boom, a 53rd week in the base, and $12.7bn of acquired distribution revenue.
- Measured post-boom: total revenue FY2022 $157,403M → FY2025 $164,683M = +1.5%/yr, **all
  of it acquired**; the retail engine went FY2022 $157,403M → FY2025 Primary **$151,966M =
  −1.2%/yr**.
- **Operating income FY2022 $24,039M → FY2025 $20,890M = −4.6%/yr.**
- **Primary-segment operating income FY2023 $21,689M → FY2025 $20,574M = −2.6%/yr.**
- **Owner earnings FY2021 $13,606M → FY2025 $12,124M = −2.8%/yr.**
- **Diluted EPS FY2022 $16.69 → FY2025 $14.23 = −5.1%/yr.**
- Transactions FY2021 1,759.7M → FY2025 1,601.5M = −2.3%/yr; **against the pre-boom FY2019
  base, −0.15%/yr, essentially flat.**
**No growth assumption in this run's Q5 is measured from a pre-2022 base.** The same rule
kills the headline dividend CAGR at §5: the +7.6–8.9% figures average two boom-funded
raises (+15%, +10%) with the ordinary ones, and the ordinary ones are +7.7%, +2.2%, +1.3%.

---
## 7. OWNER EARNINGS — the table [E2-23]

Convention: multi-year mean of (operating cash flow − stock-based compensation) − (c).
All inputs from the filed cash-flow statements (10-K FY2025 and prior 10-Ks / XBRL).
"D&A" below is the cash-flow line **"Depreciation and amortization, excluding amortization
of intangible assets"** — acquisition intangible amortization is shown separately because
it renews nothing.

| FY | end | wks | OCF | SBC | D&A ex-intang | intang amort | capex | net earnings | **OE (c=capex)** | **OE (c=D&A)** |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 2017-01-29 | 52 | 9,783 | 267 | 1,973 | — | 1,621 | 7,957 | 7,895 | 7,543 |
| 2017 | 2018-01-28 | 52 | 12,031 | 273 | 2,062 | — | 1,897 | 8,630 | 9,861 | 9,696 |
| 2018 | 2019-02-03 | **53** | 13,165 | 282 | 2,152 | — | 2,442 | 11,121 | 10,441 | 10,731 |
| 2019 | 2020-02-02 | 52 | 13,687 | 251 | 2,296 | — | 2,678 | 11,242 | 10,758 | 11,140 |
| 2020 | 2021-01-31 | 52 | 18,839 | 310 | 2,519 | — | 2,463 | 12,866 | 16,066 | 16,010 |
| **2021** | 2022-01-30 | 52 | 16,571 | 399 | 2,862 | — | 2,566 | 16,433 | **13,606** | **13,310** |
| **2022** | 2023-01-29 | 52 | 14,615 | 366 | 2,796 | — | 3,119 | 17,105 | **11,130** | **11,453** |
| **2023** | 2024-01-28 | 52 | 21,172 | 380 | 3,061 | 186 | 3,226 | 15,143 | **17,566** | **17,731** |
| **2024** | 2025-02-02 | **53** | 19,810 | 442 | 3,336 | 425 | 3,485 | 14,806 | **15,883** | **16,032** |
| **2025** | 2026-02-01 | 52 | 16,325 | 522 | 3,514 | 607 | 3,679 | 14,156 | **12,124** | **12,289** |

- **5-yr mean (OCF − SBC): $17,277M · 3-yr mean: $18,654M**
- Capex five-year total $16,075M against D&A-ex-intangibles $15,569M — **capex has run
  1.03x depreciation over the window**, and above it in four of five years.
- **Distorted years, named [E5-11]:** FY2024 (53 weeks, ~$2.5bn of sales); FY2022 (working
  capital absorbed $8.3bn of boom inventory over two years, which is why FY2022 is the
  trough at $11,130M); FY2023 (a $4,137M inventory release, which is why it is the peak at
  $17,566M); and **FY2025, whose OCF was reduced by the deferral of the Q4 fiscal-2024
  federal estimated tax payment into fiscal 2025** — cash taxes paid $3,653M (FY2024) versus
  $4,848M (FY2025) on falling pre-tax income, a ~$600M timing shift *out of* FY2025 and
  *into* FY2024. The multi-year mean is what handles this.
- **[E2-23] constraint 3, the working-capital increment:** captured inside the OCF line
  (inventory absorbed $1,498M in FY2025 and $743M in FY2024, released $4,137M in FY2023).
  HD values the majority of inventory under the **retail inventory method** with the
  remainder at moving-average or FIFO cost — **not LIFO**, so [E2-23]'s LIFO carve-out does
  not apply and the increment is included as the source requires.
- **Stock compensation subtracted in full [E5-06]: yes.** Note 9 discloses pre-tax SBC of
  **$524M** (FY2025), $444M, $382M; the cash-flow line is $522M/$442M/$380M. **[E3-70]
  measure question addressed:** HD does grant options (249k granted in FY2025 at a $92.81
  Black-Scholes fair value ≈ $23M; 2,156k outstanding, 0.2% of shares), but they are a small
  minority of a mix that is mostly performance shares, performance-based restricted stock
  and deferred shares. The reported charge is an adequate measure here, not merely its floor.
- **Look-through [E3-04]: not applicable.** No equity-method or unconsolidated minority
  stakes are disclosed.

### The (c) judgment, disclosed [E2-23, E3-44, E2-41, E5-20, E4-47]
HD is a retailer, the [E2-41] 95% class, **not** the [E5-20] capital-intensive exception —
nothing in the filing says depreciation understates renewal. **But the D&A end is not taken
raw, for four filed reasons, and (c) is judged UP:**
1. **Unit growth is de minimis relative to the base.** 2,317 stores (FY2021) → 2,359
   (FY2025) → 2,364 (Q2 FY2026); ~15 new stores guided for FY2026 on a 2,364 base = **0.6%**.
   Almost all of the $3,679M is remodels, supply chain, technology and renewal. (c) ≈ total
   capex, not less.
2. **The D&A line is contaminated by purchase accounting** if taken whole: total cash-flow
   D&A was $4,121M in FY2025, of which **$607M is acquisition intangible amortization**
   ($683M scheduled for FY2026, $9,680M remaining) that buys nothing and renews nothing.
   Only the $3,514M ex-intangibles line is a candidate proxy, and it is used above.
3. **Management is guiding capex UP.** "We plan to invest approximately $4 billion back into
   our business in the form of capital expenditures in fiscal 2026, in line with our
   expectation of approximately **2.5% of projected fiscal 2026 net sales**" — at the guided
   sales midpoint that is **~$4.26bn**, against a five-year actual average of $3,215M.
4. **[E4-47], inflation-conditioning.** 244.7 million square feet built over forty-five
   years and carried at $28,021M net against **$32.9bn of accumulated depreciation** (Q2
   FY2026) — the store base is 54% written down on old-dollar cost. Replacing it at today's
   construction costs would cost a multiple of book. The D&A charge is light in current
   dollars.

**JUDGMENT, DISCLOSED: (c) = $4.25bn**, management's own forward plan.
- **Judged owner earnings: 5-yr $17,277M − $4,250M = $13,027M; 3-yr $18,654M − $4,250M =
  $14,404M.** Range **$13.0bn – $14.4bn** (10.6% wide). Per share: **$13.06 – $14.44**.
- **Bottom boundary [E5-34]: ≈$12.0bn ($12.03/share)** — set below the judged low because
  (i) the trough actually recorded in the window was $11,130M on a smaller asset base and
  FY2025 delivered $12,124M; (ii) the consolidated operating margin has fallen four
  consecutive years and is guided down again, with three consecutive misses of the initial
  guide; (iii) FY2026 contains a ~$730M one-off IEEPA tariff refund [E4-41]; (iv)
  refinancing drag and a $4.5bn commercial-paper roll. **Conservatism spent once here.
  Windage count: one.**

---
## 8. THE CAPITAL STRUCTURE

**Balance-sheet history, filed** (`StockholdersEquity`; debt = short-term/CP + current
installments of long-term debt + long-term debt excluding current installments):

| At | Shareholders' equity | Total debt |
|---|---|---|
| 2008-02-03 (into the housing collapse) | **+$17,714M** | ~$11bn |
| 2018-01-28 | +$1,454M | — |
| 2019-02-03 | **−$1,878M** | — |
| 2020-02-02 | **−$3,116M** | — |
| 2021-01-31 | +$3,299M | **$37,238M** |
| 2022-01-30 | **−$1,696M** | $40,086M |
| 2023-01-29 | +$1,562M | $43,193M |
| 2024-01-28 | +$1,044M | $44,111M |
| 2025-02-02 | +$6,640M | $53,383M |
| **2026-02-01** | **+$12,813M** | **$55,772M** |

**Correction to the run brief, stated first because it matters:** Home Depot does **not**
have negative book equity. It did — three times, most recently at 2022-01-30 (−$1,696M) —
but equity has been rebuilt from −$3,116M (FY2019) to **+$12,813M** (FY2025), because the
buyback stopped in March 2024 and earnings have been retained since. Over FY2021–FY2025
equity rose **$9,514M**. Lowe's, over the identical window, went from +$1,437M to
−$9,917M.

**Debt terms (Note 5), read [E3-52]:**
- Senior notes principal **$48,800M**; finance lease obligations $2,963M; other $597M;
  total long-term debt $51,308M, less current installments $4,967M.
- **Short-term debt $4,464M — all commercial paper**, weighted-average rate 3.7%, against an
  $11.0bn programme supported by $11.0bn of back-up credit facilities. Maximum outstanding
  during fiscal 2025: **$5.8bn**. At 2026-08-02: $4.2bn at 3.8%, maximum $6.2bn in H1.
- **Covenants: "The indentures governing our senior notes do not generally limit our ability
  to incur additional indebtedness or require us to maintain financial ratios or specified
  levels of net worth or liquidity. The indentures governing these notes contain various
  covenants, none of which are expected to impact our liquidity or capital resources."**
  Back-up facilities: "we were in compliance with all of the covenants contained in our
  back-up credit facilities, none of which are expected to impact our liquidity or capital
  resources." **The only holder-triggered term is a change-of-control put at 101%** — not a
  ratings or net-worth trigger.
- **Maturities of long-term debt, excluding finance leases:** FY2026 **$4,684M** · FY2027
  $3,625M · FY2028 $3,115M · FY2029 $3,852M · FY2030 $2,072M · **thereafter $32,049M**
  (65% beyond five years). Total $49,397M.
- **Weighted-average coupon on the notes maturing through FY2030 ($16,800M): 3.43%**
  (FY2026 $4,550M at 3.84%; FY2027 $3,500M at 3.34%; FY2028 $3,000M at 2.58%; FY2029
  $3,750M at 3.94%; FY2030 $2,000M at 3.01%). HD's own September 2025 issuance priced at
  3.75% (2028), 3.95% (2030) and 4.65% (2035).
- Interest-rate swaps: $5.4bn notional, fixed-to-floating; floating-rate principal $5.4bn =
  ~11% of the notes portfolio; a 100bp move costs ~$54M a year.
- Cash paid for interest, net of capitalised: **$2,405M** (FY2025), $2,199M, $1,809M.
  Income-statement interest expense $2,412M / $2,321M / $1,943M.
- Aggregate remaining lease payment obligations **$15.9bn**, $2.2bn within twelve months.
  Operating lease cost $1,846M; finance-lease interest $113M.

**Liquidity:** cash and cash equivalents **$1,389M**, of which **$1.0bn is held by foreign
subsidiaries**. No short-term investments line. **$11.0bn of back-up credit facilities,
undrawn — but supporting $4,464M of commercial paper that is actually outstanding.**
Credit ratings are **not disclosed** in the 10-K (metric-level UNRESEARCHED; route: rating
agency releases / IR — no verdict rests on it).

**Asset backing:** **90% of store square footage is owned** (including stores on ground
leases), 244.7 million square feet, carried within $28,021M of net property and equipment
against $32.9bn of accumulated depreciation. Distribution and fulfilment centres are 97%
leased; SRS's 1,250+ branches are "the majority of which are leased."

**[E2-54] coverage, computed.** All interest, payable and accrued = income-statement
interest expense **$2,412M** (which includes $113M of finance-lease interest). Cash flow
available = OCF $16,325M **plus** the $2,405M of cash interest already deducted within it,
**less** ample capex of $4,300M (management's own forward plan, above the run-rate) =
**$14,430M**. **Coverage 5.98x.**
Stress: OCF **−19.9%** (HD's own peak-to-trough decline through the last housing collapse) →
**4.64x**; −25% → 4.29x; −35% → 3.61x; −50% → 2.60x; **−58.8% → 2.00x**.

**[E2-60], distributions versus owner earnings, FY2021–FY2025:**
owner earnings **$70,309M**; dividends **$41,238M**; buybacks **$30,105M**; **total returned
$71,343M — an excess of only $1,034M**, i.e. HD distributed almost exactly what it earned.
Acquisitions added $24,989M; debt rose $18,534M; **equity rose $9,514M**.
Lowe's, same window: owner earnings $35,414M, returned $49,530M, a **$14,116M excess**,
funded by $18,141M of new debt, with equity falling $11,354M.
**[E2-60] does not fire on Home Depot's distributions. It fired on Lowe's.**

---
## 9. THE ACQUISITIONS — Note 13 (10-K) and Note 10 (10-Q), in full

| | **SRS** (2024-06-18) | **GMS** (2025-09-04) | **Mingledorff's** (2026-05-11) |
|---|---|---|---|
| Consideration | $17,707M cash + $321M stock = **$18,028M** | $4,257M for shares + $824M GMS debt repaid = **$5,081M** | **~$1,100M** cash (preliminary) |
| Goodwill | $11,003M | $2,610M | $412M |
| Intangibles | $5,780M | $1,800M | $410M |
| **Goodwill + intangibles as % of price** | **93.1%** | **86.8%** | **74.7%** |
| Net tangible assets acquired | ~$1,245M | ~$671M | ~$278M |
| Customer-relationship life | 20 yrs ($5,400M) | 19 yrs ($1,540M) | 21 yrs |
| Trade-name life | 5 yrs ($380M) | 7 yrs ($260M) | — |
| Stub-period earnings disclosed | net sales $6.4bn; **"net earnings … were immaterial"** | net sales $2.0bn; **"net earnings … were immaterial"** | **"immaterial"** |
| Pro forma results | **"not presented as the effect of the acquisition was not material"** | same | same |

**Combined SRS + GMS + Mingledorff's: ~$24.2bn of consideration, of which ~$21.6bn (89%)
is goodwill and intangibles.** A further $354M of GMS senior notes was assumed and redeemed.
Goodwill and intangibles on the balance sheet went **$5,860M (7.7% of assets) at FY2023 →
$28,458M at FY2024 → $32,673M (31.1% of assets) at FY2025 → $33,381M at Q2 FY2026.**

**What the acquired business earns — HD's own segment disclosure (Note 2):**

| | FY2024 (SRS, 7.5 months) | FY2025 (SRS full year + GMS 5 months) |
|---|---|---|
| **Other segment net sales** | $6,406M | **$12,717M** |
| **Other segment operating income** | $213M | **$316M** |
| Other segment operating margin | 3.32% | **2.49%** |
| — acquisition intangible amortization inside it | $218M | **$398M** |
| Operating income before that amortization | $431M (6.7%) | **$714M (5.6%)** |
| Primary (retail) segment operating margin, same year | 13.92% | **13.54%** |

**First-full-year pre-tax return on the ~$24.2bn deployed: 1.3% on the GAAP segment line,
3.0% before acquisition intangible amortization** — against incremental interest expense of
**+$469M** (interest expense $1,943M in FY2023 → $2,412M in FY2025) and against retiring
stock at a ~4.3% owner-earnings yield. **On the filed numbers the acquisition programme has
so far subtracted from consolidated pre-tax earnings.**
Roofing and related products fell from **68% to 53%** of Other net sales as GMS's drywall
and ceilings came in; at Q2 FY2026 it is **39%**.
GMS was excluded from management's fiscal 2025 ICFR assessment (≈3% of consolidated assets
ex-goodwill/intangibles, ≈1% of consolidated net sales) — the standard one-year carve-out.
KPMG's **only critical audit matter** is "Sufficiency of audit evidence over certain
merchandise inventories" (retail inventory method, an IT/process matter). **The GMS
customer-relationship valuation was not designated a CAM** (Deloitte designated the
comparable FBM valuation a CAM at Lowe's).

---
## 10. LEGAL / CONDUCT SWEEP (Item 3, FY2025 10-K, read in full; Note 12; 10-Q Note 9)

Item 3 in full: "The Company is party to various legal proceedings arising in the ordinary
course of its business but is not currently a party to any legal proceeding that management
believes will have a material adverse effect…" plus, under the SEC's $1 million
environmental-proceeding threshold, **an update on the April 2021 civil consent decree with
the DOJ, EPA and the states of Utah, Massachusetts and Rhode Island** on lead-safe work
practices in the installation-services business:

> "In the second quarter of fiscal 2025, we made the final payment of stipulated penalties
> owed under the decree, and in the fourth quarter of fiscal 2025 the decree was formally
> terminated. The aggregate amount of stipulated penalties paid to the EPA under the decree
> totaled approximately $1.7 million, and we have collected fines from our third-party
> installers for this amount."

Note 12 adds outstanding letters of credit of $738M and the same ordinary-course language.
Nothing else is disclosed.

Per the worked **TJX 2022** precedent this is an environmental/product-safety matter, not
financial dishonesty toward owners, and it is **not** the [E5-16] binary. **On the [E5-22]
latency test the direction is favourable and is the reverse of Lowe's:** HD's 2021 decree
was **completed and terminated**; Lowe's 2014 decree was **replaced by a second one on
2025-11-25 with a $12.5 million penalty** after the agencies "identified possible deviations
from the consent decree."

---
## 11. PROXY (DEF 14A 2026, accession 0000354950-26-000090) — compensation [E4-29 check]

**Management Incentive Plan, fiscal 2025:** Sales **50%** · Operating Profit **30%** ·
Inventory Turns **10%** · Pro Strategic Goal **10%**. **Not an adjusted-EPS plan.**
Threshold/maximum at 90%/110% of target with 50%/200% payout; the operating-profit threshold
gates any payout at all.

| Measure | Threshold | Target | Maximum | Actual (as adjusted) | Actual (unadjusted) |
|---|---|---|---|---|---|
| Sales ($bn) | 147.56 | **163.95** | 180.35 | **162.81** | 164.68 |
| Operating profit ($bn) | 19.22 | **21.35** | 23.49 | **21.17** | 20.89 |
| Inventory turns | 4.06 | **4.51** | 4.97 | **4.33** | 4.36 |
| Pro strategic goal | n/a | increase in managed-account sales | n/a | **achieved** | — |

**Pre-published adjustments applied:** sales adjusted **UP** $307.5M for FX and **DOWN
$2.18bn for acquisitions**; operating profit adjusted **UP** $44.2M (FX), **UP** $42.4M
(acquisition transaction costs) and **UP** $192.3M ("certain nonrecurring charges and
write-offs" — not further identified); inventory turns adjusted down 0.03 for acquisitions.
**Net effect: the largest single adjustment ($2.18bn off the 50%-weighted sales measure) ran
AGAINST management.**

**Payout: 95% of target** — below target — in a year when operating income fell 3.0% and
diluted EPS fell 4.6%. (Lowe's, on its comparable plan, paid **104.67%** of target.)
**Fiscal 2023–2025 performance shares paid 70.1%** (three-year average ROIC 37.4% and
average operating profit $21.15bn, both between threshold and target).
Long-term incentive mix: 50% performance shares (3-yr average ROIC + 3-yr average operating
profit), 30% performance-based restricted stock (forfeited if FY2025 operating profit was
below 90% of target), 20% stock options (FY2025 grant at $362.13, in the money by $12.46 at
year end). Hedging and pledging prohibited for all associates and directors; robust stock
ownership and retention guidelines; a clawback policy extending beyond the mandate.
**No defined-benefit pension plan exists** (Note 10: defined-contribution Benefit Plans and
Restoration Plans only; contributions $382M in FY2025) — so [E4-22]'s "fanciful pension
assumptions" cannot fire.

**Shareholder proposal 9** (John Chevedden, independent board chair) records in its
supporting statement — the proponent's words, not the company's — that HD "significantly
lowered its fiscal 2025 outlook… now expects adjusted EPS to decline by approximately 5%…
a steeper drop than its previous forecast of a 2% decline" and that Q3 was "the third
consecutive quarter that Home Depot missed its profit expectations." The mid-year guidance
cut is corroborated by the outturn ($14.69 adjusted, −3.6%, against an initial −2% guide).

---
## 12. CEO MEDICAL LEAVE — 8-K filed 2026-08-12, accession 0000354950-26-000141

> "On August 12, 2026, The Home Depot, Inc. announced that **Edward P. Decker, Chair,
> President and Chief Executive Officer, will take a temporary medical leave from his
> role.** … the Board of Directors, in alignment with Mr. Decker's recommendation, has
> chosen two long-time Home Depot executives to oversee the operations of the Office of the
> CEO during the period of his absence: **Ann-Marie Campbell**, Senior Executive Vice
> President, is providing oversight of Home Depot's day-to-day operations; **Richard V.
> McPhail**, Executive Vice President and Chief Financial Officer, is providing oversight of
> the Company's financial management and Pro subsidiaries and **has been designated as
> interim principal executive officer** … **Gregory D. Brenneman**, in his role as
> independent lead director, is chairing the Board during the period of Mr. Decker's
> absence."

"At this time, no changes have been made to Ms. Campbell or Mr. McPhail's compensation."
Campbell (61) joined Home Depot in 1985 as a cashier; McPhail (56) joined in 2005 and has
been CFO since September 2019. The Q2 FY2026 earnings release (2026-08-18) carries quotes
from McPhail and Campbell, not Decker. The Q2 10-Q's forward-looking-statements paragraph
adds a new item: "the timing and expected impact of organizational changes, including within
the Company's senior leadership team."
**Dated to when it became public: 2026-08-12, nineteen days before this run.**

A second 8-K (2026-08-21, accession 0000354950-26-000148) records that on 2026-07-30 HD
expanded the portfolios of Bastek (merchandising + private brands), Broggi (interconnected
retail + loyalty/credit/payments) and McPhail (a new "Office of Pro Acceleration"
coordinating Home Depot Pro, HD Supply, SRS and Construction Resources), with $500,000
restricted-stock grants to each on 2026-08-20.

---
## 13. THE CRASH-ERA CALIBRATION [E4-40] — exposure, not experience

Filed figures through the last housing collapse (XBRL, 10-K):

| FY ended | 2008-02-03 (53 wks) | 2009-02-01 | 2010-01-31 | 2011-01-30 |
|---|---|---|---|---|
| Net sales | $77,349M | $71,288M | **$66,176M** | — |
| Operating income | $7,242M | **$4,359M** | $4,803M | $5,839M |
| Net earnings | $4,395M | **$2,260M** | $2,661M | $3,338M |
| Operating cash flow | $5,727M | $5,528M | $5,125M | **$4,585M** |
| Shareholders' equity | $17,714M | $17,777M | $19,393M | $18,889M |

**Peak-to-trough: sales −14.4%, operating income −39.8%, net earnings −48.6%, operating cash
flow −19.9%.** (The operating-income trough includes store-rationalisation and EXPO-related
charges; per [E5-33] those are real costs and belong in the mean, but the OCF series is the
cleaner cyclical read.)

**Lowe's, same collapse: sales −2.2%, operating cash flow −11.4%.**

**So the demonstrated cyclical amplitude runs the other way from the current competitive
row: Home Depot's business fell roughly twice as far as Lowe's did in 2007–2010.** Home
Depot went through it carrying roughly $11bn of debt and **$17.7bn of positive equity**,
with no commercial-paper dependence of the current scale. It enters this cycle with
**$55.8bn of debt, $12.8bn of equity, $1.4bn of cash and $4.5bn of commercial paper
outstanding**. [E4-40]: the benign recent history is not evidence; the balance sheet that
absorbed the last one no longer exists in the same form.

---
## 14. ARITHMETIC USED IN THE RUN

- Market cap **$327,073M** = 997,689,626 shares (10-Q cover, 2026-08-18) × $327.83
  (aggregator, 2026-08-31, flagged).
- Owner-earnings yields: mechanical 5-yr $14,062M → **4.30%**; judged 5-yr $13,027M →
  **3.98%**; judged 3-yr $14,404M → **4.40%**; bottom boundary $12,000M → **3.67%**;
  FY2025 free cash flow $12,646M → **3.87%**. Sovereign **5.19%**.
- Implied perpetual growth at the bare sovereign (price = OE ÷ (r − g)): on judged $13,027M,
  **+1.21%**; on mechanical $14,062M, **+0.89%**; on the bottom boundary, **+1.52%**.
- Dividend run-rate **$9,298M** ($2.33 × 4 × 997.69M) = **2.84%** yield. Coverage: 1.51x
  (mechanical 5-yr), **1.40x** (judged), **1.29x** (bottom boundary), 1.20x (the FY2022
  trough), 1.36x (FY2025 free cash flow), 1.52x (FY2025 net earnings).
- P/E on FY2025 GAAP EPS $14.23: **23.0x**; on adjusted $14.69: 22.3x. Lowe's: 17.5x.
- Leverage: total debt $55,772M; operating lease liabilities $9,578M; EBITDA $24,949M
  (operating income $20,890M + segment D&A $4,059M); operating lease cost $1,846M.
  **Net debt/EBITDA 2.18x · lease-adjusted debt/EBITDAR 2.44x · debt/judged owner earnings
  4.28x.**
- Entry bands: judged OE $13,027M; at 1.5%/2.5%/3.0% growth the yields required to reach a
  ~10% honest pre-tax expectancy are 8.5%/7.5%/7.0%, giving **$154 / $174 / $187** per share.
  On the bottom boundary $12,000M: **$141 / $160 / $172**.
