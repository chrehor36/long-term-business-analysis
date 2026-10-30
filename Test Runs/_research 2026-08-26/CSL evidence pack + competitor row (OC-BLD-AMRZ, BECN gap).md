# CSL — EVIDENCE PACK AND COMPETITOR ROW
**Carlisle Companies Incorporated (NYSE: CSL) · assembled 2026-08-31 · Framework v4.1**

Every figure below is from an SEC primary filing unless flagged. Aggregator use is flagged in
place and is confined to live and historical quotes. This file is the working paper for
`Test Runs/2026-08-31 Run - CSL (Carlisle Companies) v4.1.md`.

---
## 1. DOCUMENTS READ

| document | period | filed | accession | primary doc |
|---|---|---|---|---|
| **Form 10-K FY2025** | year to 2025-12-31 | 2026-02-13 | **0000790051-26-000012** | csl-20251231.htm |
| **Form 10-Q Q2 2026** | quarter to 2026-06-30 | 2026-07-30 | **0000790051-26-000037** | csl-20260630.htm |
| **DEF 14A 2026** | meeting 2026-04-29 | 2026-03-17 | **0001193125-26-109193** | d932758ddef14a.htm |
| Form 10-K FY2024 | 2024-12-31 | 2025-02-14 | 0000790051-25-000077 | csl-20241231.htm |
| Form 10-K FY2023 | 2023-12-31 | 2024-02-16 | 0000790051-24-000058 | csl-20231231.htm |
| Form 10-K FY2022 | 2022-12-31 | 2023-02-16 | 0000790051-23-000044 | csl-20221231.htm |
| Form 10-K FY2020 | 2020-12-31 | 2021-02-11 | 0000790051-21-000080 | csl-20201231.htm |
| 8-K ex-99.1 Q2 2026 release | 2026-07-29 | 2026-07-29 | 0000790051-26-000033 | q22026-ex991xearningsrelea.htm |
| 8-K ex-99.1 Q4 2025 release | 2026-02-03 | 2026-02-03 | 0000790051-26-000009 | q42025-ex991xearningsrelea.htm |
| 8-K ex-99.1 Q4 2024 release | 2025-02-04 | 2025-02-04 | 0000790051-25-000034 | q42024-ex991xearningsrelea.htm |
| 8-K notes offering | 2025-08-20 | 2025-08-20 | 0001193125-25-184090 | d17228d8k.htm |

**Competitor filings:** Owens Corning 10-K FY2025 **0001370946-26-000067**; Amrize Ltd 10-K FY2025
**0002035989-26-000017**; TopBuild Corp 10-K FY2025 **0001104659-26-020481**.

**Sovereign:** FRED `fredgraph.csv?id=DGS30` (Federal Reserve Bank of St. Louis, 30-Year Treasury
Constant Maturity), retrieved 2026-08-31. Last observation **5.22% at 2026-08-28**; prior 5.19%
(08-27), 5.18% (08-26), 5.17% (08-25), 5.23% (08-24).

**Quote (aggregator, flagged):** CSL **$346.58 at 2026-08-31**. Prior closes $356.53 (08-28),
$360.74 (08-27), $365.72 (08-26), $363.27 (08-25).

**Cross-checks performed against the filed statements:**
- **Operating cash flow $1,101.8 million (2025)** appears identically in (a) the Consolidated
  Statement of Cash Flows, (b) the MD&A liquidity table, (c) the 8-K ex-99.1 of 2026-02-03
  ("Generated $1.1 billion in operating cash flow in 2025"), and (d) the XBRL tag.
- **Revenues $5,019.9 million (2025)** identical in the income statement, the MD&A revenue bridge,
  the Note 2 segment table, the Note 6 end-market table and the Note 6 geographic table.

---
## 2. SHARE COUNT — TOTAL ECONOMIC SHARES

| source | date | shares |
|---|---|---|
| **10-Q Q2 2026 cover (used)** | **2026-07-23** | **39,714,133** |
| 10-K FY2025 cover | 2026-02-06 | 40,883,868 |
| Balance sheet, 2026-06-30 | | 39.8 million outstanding; treasury 38.8 million |
| Balance sheet, 2025-12-31 | | 41.0 million outstanding; treasury 37.6 million |

- **Preferred stock: $1 par, 5.0 million shares authorised; "no shares were issued or outstanding
  during any period presented."** Nil.
- One class of common only. Securities registered under 12(b): "Common stock, $1 par value | CSL |
  New York Stock Exchange" — one line.
- Two-class method used for EPS because restricted stock awards carry non-forfeitable dividends;
  those shares are already inside the outstanding count. Income allocated to participating
  securities was $1.5 million of $742.5 million in 2025 (~0.2%).
- **Market cap = 39,714,133 × $346.58 = $13,764.1 million.** Using the staler 10-K cover count the
  cap would be $14,169.5 million; the newer count is used, which raises the owner-earnings yield.
  The company repurchased shares continuously through August 2026, so the true count today is
  probably marginally lower still and the cap marginally overstated — the error runs conservative.

---
## 3. THE DIVESTITURE TREATMENT — WHAT CONTINUING OPERATIONS ACTUALLY EARN

Carlisle sold three of its four former segments:

| business | sold | proceeds |
|---|---|---|
| Carlisle Brake & Friction (CBF) | 2021-08-02 | $250M at close + $125M earnout received 2022-02-23 |
| Carlisle Fluid Technologies (CFT) | 2023-10-02 | $520M |
| Carlisle Interconnect Technologies (CIT) | 2024-05-21 | **$2,025M** |

**Where the money and the earnings sit in the filings:**
- **Proceeds are in INVESTING activities, never in operating cash flow.** Cash-flow line "Proceeds
  from sale of discontinued operations, net of cash disposed": $247.7M (2021), $132.0M (2022),
  $510.6M (2023), $1,998.0M (2024), nil (2025). **Total $2,888.3M.**
- **Gains are reversed out of operating cash flow.** The reconciliation line "(Gain) loss on sale
  of discontinued operations" removes −$454.4M (2024) and adds back $82.5M (2023) and $8.0M (2021).
  **Operating cash flow is therefore clean of the gains.**
- **Reported net income and reported EPS are NOT clean.** 2024 net income $1,311.8M included
  $446.7M from discontinued operations, of which $454.4M was the CIT gain. Diluted EPS 2024 was
  **$27.82 total against $18.34 from continuing operations** — a 52% difference. Any screen using
  GAAP EPS for 2024 is reading a gain on sale as earnings.
- **Operating cash flow still contains the divested businesses' cash flow in the earlier years,
  and Note 4 splits it:** discontinued-operations operating cash flow was **+$89.6M (2021),
  +$60.5M (2022), +$164.1M (2023), −$8.9M (2024), −$1.8M (2025)**.

**Continuing-operations operating cash flow, therefore ($M):**

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Consolidated OCF, as filed | 421.7 | 1,000.9 | 1,201.3 | 1,030.3 | 1,101.8 |
| less discontinued OCF | 89.6 | 60.5 | 164.1 | (8.9) | (1.8) |
| **Continuing OCF (used)** | **332.1** | **940.4** | **1,037.2** | **1,039.2** | **1,103.6** |

**Continuing-operations revenue and operating income (CCM + CWT + corporate), from each year's
segment note ($M):**

| | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| Revenue | — | — | — | 3,836.7 | 5,449.4 | 4,586.9 | 5,003.6 | 5,019.9 |
| Operating income | — | — | — | 573.4 | 1,204.8 | 982.8 | 1,143.1 | 1,002.5 |
| Operating margin | — | — | — | 14.9% | 22.1% | 21.4% | 22.8% | 20.0% |
| **CCM revenue** | 2,880.3 | 3,233.3 | 2,995.6 | 2,846.2 | 3,885.2 | 3,253.4 | 3,704.3 | 3,721.7 |
| **CCM operating income** | 435.4 | 576.0 | 581.6 | 619.9 | 1,175.0 | 913.9 | 1,084.3 | 997.2 |
| **CCM operating margin** | **15.1%** | **17.8%** | **19.4%** | **21.8%** | **30.2%** | **28.1%** | **29.3%** | **26.8%** |

*(2018–2020 CCM figures are from the FY2020 10-K segment table, where CCM was one of four segments
and CWT did not yet exist — Henry was acquired 2021-09. Consolidated 2018–2020 figures are not
comparable and are deliberately left blank.)*

**Continuing capex and D&A, from the segment tables ($M):**

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Capex, continuing | 105.5 | 158.8 | 110.8 | 100.9 | 131.2 |
| D&A, continuing | 119.7 | 158.6 | 151.1 | 172.6 | 196.5 |
| — of which depreciation (2023–25) | | | 84.3 | 70.2 | 74.6 |
| — of which amortisation (2023–25) | | | 120.4 | 102.4 | 121.9 |
| SBC (consolidated, as filed) | 19.4 | 31.2 | 41.5 | 30.1 | 34.8 |

*(Cash-flow-statement capex, which includes the divested units, was $134.8M, $183.5M, $142.2M,
$113.3M and $131.2M. The segment figures are used because they match the continuing perimeter.)*

---
## 4. THE FIVE-YEAR CASH BRIDGE — WHAT PAID FOR THE BUYBACK

Cumulative 2021–2025, from the Consolidated Statements of Cash Flows ($M):

| | |
|---|---|
| Operating cash flow (consolidated, as filed) | **4,756.0** |
| Capital expenditures | (705.0) |
| Acquisitions, net of cash acquired | (2,418.6) |
| **Proceeds from sale of discontinued operations** | **+2,888.3** |
| Repurchases of common stock | **(4,501.5)** |
| Dividends paid | (760.7) |
| Notes issued ($842.6M 2021 + $987.8M 2025) less repaid ($1,050.0M) | +780.4 |
| Option exercises less withholding | +189.2 |
| Cash, 2020-12-31 → 2025-12-31 | 850.9 → 1,112.1 |

- **Divestiture proceeds equal 64.2% of the five-year buyback.**
- Free cash flow after capex was $4,051.0M; buybacks plus dividends were $5,262.2M. **The
  $1,211.2M gap was funded by selling businesses and by issuing notes.**
- Diluted share count fell **53.2M (2021) → 43.2M (2025), −18.8%**, and to **39.7M** by
  2026-07-23, a further −8.1%.
- **There is nothing left to sell.** Carlisle is now two segments, both building envelope.

**Buyback prices paid** (cash repurchases ÷ shares retired per the Statements of Stockholders'
Equity; 2026 from the Q2 10-Q):

| year | cash | shares | **average price** | vs $346.58 today |
|---|---|---|---|---|
| 2021 | $315.6M | 1.9M | **$166** | +109% |
| 2022 | $400.0M | 1.6M | **$250** | +39% |
| 2023 | $900.0M | 3.5M | **$257** | +35% |
| 2024 | **$1,585.9M** | 3.9M | **$407** | **−14.8%** |
| 2025 | **$1,300.0M** | 3.7M | **$351** | −1.4% |
| H1 2026 | $500.0M | **1.4M** | **$357** | −3.0% |

*(Share counts are the gross "Repurchases of common stock" line of each Statement of Stockholders'
Equity, not the net change in shares outstanding, which is reduced by stock-compensation issuance.
H1 2026: 1.4 million shares at a treasury cost of $504.1M including excise tax, $500.0M in cash.
Carlisle's monthly closes over H1 2026 ran $340.89, $394.77, $333.62, $355.26, $344.81 and $362.75,
which brackets the $357 average — aggregator quotes, flagged.)*

Q4 2025 monthly detail from Item 5: October 0.3M at **$330.11**, November 0.3M at **$311.67**,
December 0.3M at **$327.07**. Authorisation: 7.5 million additional shares approved 2025-09-03;
7.3 million remaining at 2025-12-31. **2026 target raised from $1.0bn (February) to $1.2bn (July).**

---
## 5. THE DIVIDEND — FILED RECORD AND DECOMPOSITION

**Dividends declared per share**, from each year's Consolidated Statement of Stockholders' Equity:

| 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| $1.54 | $1.80 | $2.05 | $2.13 | $2.58 | $3.20 | $3.70 | **$4.20** |

- **No special dividend anywhere in the filed record. No cut, no flat year, no skipped quarter.**
  Cash dividends paid rose every year: $112.5M (2021) → **$181.1M (2025)**.
- **FY2025 10-K Item 5, verbatim:** *"We intend to pay dividends to our stockholders and have
  **increased our dividend rate annually for the past 49 years**. On January 28, 2026, the Board
  declared a regular quarterly dividend of $1.10 per share."* **The streak is 49 years, not 48.**
- Current quarterly rate **$1.10** (Q1 and Q2 2026, per the 10-Q equity statement); annualised
  **$4.40**, a **1.27% yield at $346.58**.
- **The 50th consecutive increase is not in the filed record as at 2026-08-31.** Carlisle has
  raised with the August board meeting (2025: $1.00 → $1.10, effective with the Q3 payment). No
  8-K or 10-Q discloses a 2026 raise as of the run date.

### Growth rate — reproduction of the screen's +14.2%

| construction | rate |
|---|---|
| DPS 2018 → 2025 (7y) | **+15.41%/yr** |
| **DPS 2019 → 2025 (6y) — the pre-2020 base** | **+15.17%/yr** |
| DPS 2020 → 2025 (5y) | +15.42%/yr |
| DPS 2021 → 2025 (4y) | +18.50%/yr |
| 2019 declared $1.80 → current annualised rate $4.40 (7y) | +13.62%/yr |
| 2019 declared $1.80 → current annualised rate $4.40 (6.5y) | +14.74%/yr |

**The screen's +14.2% sits inside the band of defensible constructions (13.6% to 15.4%) and is
if anything conservative.** No verdict turns on which is used.

### THE DECOMPOSITION — reconciles exactly on every window

Using reported total figures (net income, diluted share count, declared DPS), so that the
divestitures show up where they actually acted:

| window | **dividend growth** | **from earnings** | **from share retirement** | **from payout** |
|---|---|---|---|---|
| **2019 → 2025 (6y)** | **+15.17%/yr** | +7.77%/yr (**53%**) | **+4.88%/yr (34%)** | +1.85%/yr (13%) |
| 2020 → 2025 (5y) | +15.42%/yr | +13.14%/yr | +4.95%/yr | **−2.71%/yr** |
| 2021 → 2025 (4y) | +18.50%/yr | +13.03%/yr | +5.34%/yr | −0.60%/yr |

Each row reconciles: (1+earnings) × (1+retirement) × (1+payout) − 1 = dividend growth.
Attribution shares are log-additive. Net income $472.8M (2019) → $740.7M (2025); diluted shares
57.5M → 43.2M; payout of diluted EPS 22.0% → 24.5%.

**Answer to the operator's question: about one-third of Carlisle's dividend growth from a
pre-2020 base is share retirement — and about two-thirds of the share retirement was paid for by
selling three business segments.** Compare RPM (3–11% of dividend growth from retirement) and
ITW (26%).

### Cash dividends as a share of owner earnings, then versus now

Owner earnings = continuing OCF − SBC − (c), with (c) at the D&A default [E3-44] ($M):

| year | owner earnings (c=D&A) | owner earnings (c=capex) | dividends | payout on D&A end |
|---|---|---|---|---|
| 2021 | 193.0 | 207.2 | 112.5 | 58.3% |
| 2022 | 750.6 | 750.4 | 134.4 | 17.9% |
| 2023 | 844.6 | 884.9 | 160.3 | 19.0% |
| 2024 | 836.5 | 908.2 | 172.4 | 20.6% |
| 2025 | 872.3 | 937.6 | 181.1 | 20.8% |

- **Five-year mean 2021–25: owner earnings $699.4M, dividends $152.1M → payout 21.8%.**
- **Three-year mean 2023–25: owner earnings $851.1M, dividends $171.3M → payout 20.1%.**
- On the **current annualised rate** of $4.40 × 39.714M = **$174.7M**: covered **4.00x** by
  bottom-boundary owner earnings, **5.21x** at the top of the range. Payout 19–25%.
- **The payout has not been expanded to manufacture the growth. It has been roughly flat at
  one-fifth of owner earnings for four years.** That is a genuine finding in Carlisle's favour and
  it is recorded before anything that cuts the other way.
- **The screen's "payout 0.43x worst-five-year EPS" does not reproduce on any construction built
  from the filings.** Tried: $4.20 ÷ worst total diluted EPS 2021–25 ($7.91) = **0.53x**; ÷ worst
  continuing diluted EPS ($7.23) = **0.58x**; ÷ five-year mean total EPS ($17.12) = 0.25x; ÷ 2025
  EPS = 0.24x. The coverage conclusion is unaffected on every one of them.

---
## 6. THE BOOM WINDOW [E4-41] — QUANTIFIED

**The single most important table in this pack.** CCM operating margin, filed, by year:

| 2018 | 2019 | 2020 | 2021 | **2022** | 2023 | 2024 | **2025** |
|---|---|---|---|---|---|---|---|
| 15.1% | 17.8% | 19.4% | 21.8% | **30.2%** | 28.1% | 29.3% | **26.8%** |

**The organic revenue record, from each year's MD&A bridge:**

| year | consolidated organic | CCM organic | acquisitions | note |
|---|---|---|---|---|
| **2022** | **+31.2%** | **+37.3%** | +11.6% (Henry) | the price shock |
| **2023** | **−15.8%** | **−16.3%** | — | destocking and rate shock |
| 2024 | +6.8% | n/d | +2.3% | restock |
| **2025** | **−2.9%** | **−0.7%** | **+3.2%** | acquisitions held revenue flat |
| H1 2026 | +2.3% | n/d | +0.3% | Q2 alone +7.9%, incl. pre-buy |

**Verbatim, FY2023 10-K MD&A:** 2022 CCM revenue *"$3,885.2 … $2,846.2 … 36.5% … Organic 37.3%"*
with operating margin *"30.2% … 21.8%"*. 2023: *"CCM's revenue decreased in 2023 primarily
reflecting lower sales in non-residential end market of $597.8 million from project delays and
uncertainty caused by higher interest rates, and **prolonged distributor destocking** during the
first part of the year."*

**Findings:**
1. **The 2022 organic increase of +37.3% at CCM was overwhelmingly price.** Carlisle does not
   publish the split (§8 below), but volume cannot plausibly have risen 37% in a year in which US
   commercial roofing units did not.
2. **The price was very largely KEPT.** CCM's margin rose 8.4 points in 2022 and has given back
   3.4 of them by 2025. **It stands 5.0 points above 2021 and 9.4 points above the 2018–20 mean
   of 17.4%.** This is stronger evidence of pricing power than the RPM file found, and it is
   recorded as such.
3. **But the level therefore rests on years the filings show are not repeatable.** Each point of
   CCM operating margin is **$37.2M** of pre-tax income on 2025 revenue — 3.7% of consolidated
   operating income per point.

| CCM margin scenario | pre-tax hit | after-tax (21.7%) | bottom-boundary OE | yield at $13,764.1M |
|---|---|---|---|---|
| 26.8% (2025 actual) | — | — | **$699.4M** | **5.08%** |
| 24.0% (half the give-back) | $104.2M | $81.6M | **$617.8M** | **4.49%** |
| 21.8% (2021, itself elevated) | $186.1M | $145.7M | **$553.7M** | **4.02%** |
| 17.4% (2018–20 mean) | $349.8M | $273.9M | $425.5M | 3.09% |

4. **Second boom artifact: the destocking release.** 2023 operating cash flow of $1,201.3M was
   helped by a **$158.0M inventory release**; 2024 rebuilt $103.7M of it. The three-year window
   (2023–25) carries the release; the five-year window carries the 2021–22 build
   (−$136.8M and −$165.2M inventory, −$206.9M and −$25.9M receivables). **This is why the two
   windows differ by 30%.**
5. **Third: the CIT proceeds earned interest inside the window.** Interest income was $60.3M in
   2024 against $25.9M in 2025 and $20.1M in 2023 — roughly $35M of 2024 pre-tax income was the
   divestiture cash sitting in the bank. Small, named, not adjusted out.
6. **The counter-case, stated fairly [E4-51].** Not all of the margin gain is price. Carlisle
   divested three lower-margin segments (the 2018–20 consolidated margins are not the right
   comparison); MTL added architectural metals at CCM margins; the Carlisle Operating System and
   automation capex are real; capex ran at 1.76x depreciation in 2025 with revenue flat, which is
   investment, not harvest. **A full reversion to 17.4% is not the base case. But the burden of
   proof sits on the elevated level, not on the reversion, and this run places the bottom boundary
   at the un-normalised $699.4M while displaying the normalised figures beside it.**

---
## 7. OWNER EARNINGS — BOTH WINDOWS, THE CAPEX BAND, THE BOTTOM BOUNDARY

Convention: **owner earnings = continuing operating cash flow − stock-based compensation − (c)**.

| ($M) | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Continuing OCF | 332.1 | 940.4 | 1,037.2 | 1,039.2 | 1,103.6 |
| less SBC | 19.4 | 31.2 | 41.5 | 30.1 | 34.8 |
| **less (c) = capex** | 105.5 | 158.8 | 110.8 | 100.9 | 131.2 |
| **= OE (capex end)** | **207.2** | **750.4** | **884.9** | **908.2** | **937.6** |
| **less (c) = D&A** | 119.7 | 158.6 | 151.1 | 172.6 | 196.5 |
| **= OE (D&A end)** | **193.0** | **750.6** | **844.6** | **836.5** | **872.3** |

| window | mean OCF | mean SBC | mean capex | mean D&A | **OE, capex end** | **OE, D&A end** |
|---|---|---|---|---|---|---|
| **5-year 2021–25** (corpus default [E2-42]) | 890.5 | 31.4 | 121.4 | 159.7 | **737.7** | **699.4** |
| **3-year 2023–25** | 1,060.0 | 35.5 | 114.3 | 173.4 | **910.2** | **851.1** |

- **Combined range: $699.4M to $910.2M — 30.1% wide.**
- **Bottom boundary [E5-34] = $699.4M** (five-year window, D&A end of the capex band).
- **Which capex case is this?** Carlisle is **not** in the [E5-20] capital-intensive exception
  class: net PP&E is $807.1M on $5,019.9M of revenue, capex is 2.6% of sales, and **capex already
  exceeds depreciation by 76%** ($131.2M vs $74.6M). Depreciation alone would be too low a (c).
  Total D&A is used as the conservative end because **62% of it is amortisation of acquired
  intangibles**, and Carlisle's own 2025 bridge shows acquisitions (+3.2%) exactly offsetting
  organic decline (−2.9%) — i.e. the acquisition spend is, at least in part, what "maintains unit
  volume" under [E2-23]. **(c) is a disclosed judgment and this is the disclosure.**
- **The harsher (c) case, stated but not adopted:** if the whole acquisition programme were
  treated as maintenance of unit volume, (c) would be $121.4M + $483.7M = $605.1M and five-year
  owner earnings would be **$254.0M**, a 1.85% yield. That is too harsh — Henry (2021, $1,571.3M)
  was an expansion into a new segment, not maintenance. **But the 2025 bridge means the question
  is live, and the honest reading is that (c) is nearer the D&A end than the capex end.**
- Stock compensation subtracted in full [E5-06]. Carlisle grants options, restricted stock and
  performance shares; the [E3-70] market-value measure would raise the subtraction, and the
  reported charge ($34.8M, 0.7% of revenue) is the floor. **It cannot move a verdict at this size.**

---
## 8. PRICE VERSUS VOLUME [E4-55] — CARLISLE DOES NOT DISCLOSE IT; TWO OF THREE PEERS DO

**Carlisle, FY2025 10-K, every reference to volume in the document:**
- *"Gross margin decreased in 2025, primarily due to increased unit costs resulting from **higher
  absorption of fixed costs on lower volumes**."*
- *"CWT's revenue decrease in 2025 was primarily the result of **lower sales volumes** due to
  continued softness in new construction activity."*
- *"CWT's operating margin and adjusted EBITDA margin decrease in 2025 primarily reflected
  increased unit costs resulting from **higher absorption of fixed costs on lower volumes**."*

**There is no quantified price-versus-volume split anywhere in the 10-K, the 10-Q or the earnings
releases — not consolidated, not by segment.** The revenue bridge splits organic / acquisition /
FX only. Organic is a single number containing both.

**Owens Corning, FY2025 10-K, MD&A, verbatim:**
- Roofing: *"net sales decreased $193 million … **Lower volumes of approximately 7%** were
  partially offset by **higher selling prices of $129 million**."*
- Insulation: *"lower sales volumes of approximately 5% … partially offset by **favorable selling
  prices of $27 million**."*
- Doors: *"**lower volumes of approximately 8%** and **lower selling prices of $3 million**."*

**TopBuild, FY2025 10-K, MD&A, verbatim:**
- *"Net sales for 2025 increased 1.5 percent … driven by an **8.8 percent increase in sales from
  acquisitions**, and a **0.8 percent impact from higher selling prices**, partially offset by an
  **8.1 percent decline in volume**."*
- Installation Services: *"Sales decreased **11.2 percent from lower sales volume**, partially
  offset by an increase of 7.6 percent from our acquisitions and **0.2 percent from higher selling
  prices**."*

**Amrize, FY2025 10-K,** publishes tons sold and price per ton for cement and aggregates
(Building Materials) but **not** for Building Envelope.

**Conclusion: Carlisle's non-disclosure is a choice, not an industry norm.** The two US peers whose
products compete most directly for the same roof both publish the split in the same document.

---
## 9. THE COMPETITOR ROW — required [E3-28]

All four issuers have a **31 December 2025 fiscal year end**. No offset adjustment is needed —
unlike the RPM row. Every figure is from the issuer's own 10-K, computed by the same formula on
both sides, with operating income taken **after amortisation of acquired intangibles** in every
column.

| Metric, FY2025 | **CSL** | **OC** | **OC ex-impairment** | **BLD** | **AMRZ** |
|---|---|---|---|---|---|
| Fiscal year end | Dec-2025 | Dec-2025 | Dec-2025 | Dec-2025 | Dec-2025 |
| Revenue ($M) | **5,019.9** | 10,103 | 10,103 | 5,409.1 | 11,815 |
| Operating income ($M) | 1,002.5 | 360 | 1,534 | 791.9 | 1,906 |
| **Operating margin** | **19.97%** | 3.56% | 15.18% | 14.64% | 16.13% |
| **Return on unleveraged net tangible operating assets [E2-43]** | **62.1%** | 6.8% | 28.8% | **64.2%** | 21.0% |
| **Same, INCLUDING goodwill and intangibles — pre-tax** | **21.89%** | 3.78% | 16.09% | 14.06% | 9.62% |
| **Same, after tax — the ITW test** | **17.13%** | n/m | 12.40% | 10.43% | **7.54%** |
| Goodwill + intangibles ($M) | 2,964.4 | 4,214 | 4,214 | 4,396.8 | 10,748 |
| **…as % of total assets** | **47.3%** | 32.5% | 32.5% | **66.6%** | 44.3% |
| Total debt / EBITDA | **2.41x** | 4.86x | 2.30x | 2.96x | 1.87x |
| Net debt / EBITDA | **1.48x** | 4.53x | 2.14x | 2.77x | 1.11x |
| Organic / volume growth 2025 | organic **−2.9%** | Roofing vol **−7%** | | volume **−8.1%** | Bldg Env **−2.2%** |
| **Price vs volume split disclosed?** | **NO** | **YES, in full** | | **YES, in full** | partial (BM only) |
| Dividend record | **49 consecutive raises** | paid; no streak claim | | none | first year public |
| 2025 impairment | none | **$1,135M goodwill + $39M intangible (Doors/Masonite)** | | none | none |

**Denominators:** net tangible operating assets = net PP&E + inventories + trade receivables −
trade payables. CSL: 807.1 + 447.3 + 593.8 − 233.0 = $1,615.2M. OC: 4,170 + 1,472 + 937 − 1,257 =
$5,322M. BLD: 274.2 + 505.2 + 894.4 − 440.2 = $1,233.6M. AMRZ: 7,935 + 1,551 + 1,120 − 1,538 =
$9,068M. After-tax rates: CSL 21.7%, OC(adj) 22.9%, BLD 25.9%, AMRZ 21.6%.

### Segment-level, the closest like-for-like comparison available

| | revenue | adj. EBITDA / segment EBITDA | margin |
|---|---|---|---|
| **CSL — Carlisle Construction Materials** | $3,721.7M | $1,087.0M | **29.2%** |
| **OC — Roofing** | $4,437M | $1,411M | **31.8%** |
| **AMRZ — Building Envelope** (Elevate, Malarkey, Duro-Last) | $3,301M | $732M | **22.2%** |
| OC — Insulation | $3,700M | $848M | 22.9% |
| **CSL — Carlisle Weatherproofing Technologies** | $1,298.2M | $224.8M | **17.3%** |

### Peers named: 3 of the 4 major single-ply manufacturers, plus the installer

- **CSL's own Item 1, verbatim:** *"**As one of four major manufacturers in the single-ply
  industry**, CCM competes through innovative products, long-term warranties and customer service."*
- **Taken:** Owens Corning (roofing and insulation, direct); Amrize Ltd (the Holcim North American
  spin-off that owns **Elevate**, formerly Firestone Building Products, plus Malarkey and
  Duro-Last — **the operator's named gap is CLOSED**, because Amrize files a US Form 10-K); TopBuild
  (installation and specialty distribution).
- **NAMED GAPS, and why:**
  - **Beacon Roofing Supply (BECN) no longer files.** QXO, Inc. acquired Beacon in **April 2025**;
    Form 15-12G filed 2025-05-09 (CIK 1124941, now "QXO Building Products, Inc."). Last 10-K was
    FY2024, filed 2025-02-27. It is a **distributor**, i.e. Carlisle's largest customer, not a
    competitor, and is treated as such at Q2.
  - **TopBuild also no longer files.** QXO acquired it in 2026; **Form 15-12G filed 2026-07-13**
    (CIK 1633931, now "QXO Insulation, LLC"). Its FY2025 10-K, filed 2026-02-26, is its last and is
    used here on the same window.
  - **Johns Manville** is a wholly owned Berkshire Hathaway subsidiary and publishes no separable
    financials. **GAF / Standard Industries** is private. **Sika AG** files no Form 10-K.
    **Three of the industry's real competitors are therefore unavailable at any rung of the
    evidence ladder** — but two of the four named single-ply manufacturers (CSL itself and
    Amrize/Elevate) are covered, so **the moat class is not held provisional**.
- **The row's limit [E3-61].** It shows position, not conduct. Owens Corning's 2025 numbers are
  wrecked by a $1,174M impairment on an acquisition it made 19 months earlier; Amrize's first
  full year as a separate registrant carries a $7.5bn related-party recapitalisation; TopBuild was
  taken over mid-2026. **None of that is visible in the ratios and none of it could have been
  predicted from them.**

---
## 10. Q3 EVIDENCE — GUIDANCE VERSUS OUTTURN, INCENTIVES, FLAGS

### Guidance record [E3-48]

| guided | when | for | outturn |
|---|---|---|---|
| *"mid-single-digit revenue growth, along with approximately 50 basis points of adj. EBITDA margin expansion"*; *"another record year"* | 8-K 2025-02-04 | FY2025 | **revenue +0.3%; adj. EBITDA margin −220bp (26.6% → 24.4%); adj. EPS $19.40 vs $20.20, −4%.** Not a record year. |
| *"LSD revenue growth and ~50 bps of adj. EBITDA margin expansion"*; *"repurchase up to $1 billion of shares in 2026"* | 8-K 2026-02-03 | FY2026 | walked back within six months |
| *"raising our full-year 2026 revenue outlook to mid-single-digit growth with operating and adjusted EBITDA margins **approximately flat**"*; buyback target raised to **$1.2 billion** | 8-K 2026-07-29 | FY2026 | open |

**Vision 2030, the long-run target, verbatim:** *"we remain very confident in our key long-term
financial objective of delivering **$40 of adjusted EPS**"* (2026-02-03) and *"we remain confident
in our path to **$40 of adjusted EPS and 25%-plus ROIC** under Vision 2030"* (2026-07-29).
From 2025 adjusted EPS of $19.40 that is **+15.6% a year for five years** — the [E4-35] class.

**The arithmetic of the $40 target, which the run performs because nobody else does:** 2025
adjusted EPS $19.40 × 43.2M diluted = **$838M of adjusted earnings**. At $1.2bn of repurchases a
year at $346.58, the count falls to **~22.4M shares by 2030** (−12.1%/yr). $40 × 22.4M =
**$896M** — a **1.4% a year** increase in total adjusted earnings. **The headline target is a
buyback plan, not an earnings plan.** And $6.0bn of repurchases over five years against roughly
$500–700M a year of free cash after dividends means **$2.5–3.5bn would have to be borrowed**,
with nothing left to divest.

### Incentive design and outcome [E2-49]

2025 annual-incentive measures and results (DEF 14A, pages 23 and 28):

| measure | weight | threshold | target | maximum | **2025 actual** |
|---|---|---|---|---|---|
| Sales | 25% | $5.139bn | $5.293bn | $5.499bn | **$4.991bn — below threshold** |
| Operating income margin | 20% | 22.0% | 22.5% | 23.0% | **20.5% — below threshold** |
| Average working capital % of sales | 15% | 17.7% | 17.2% | 16.7% | **18.6% — below threshold** |
| Earnings | 40% | | | | **$759M vs $868M in 2024, −12.6%** |

**Result, verbatim:** *"**None of the Company's other named executive officers were paid any 2025
annual incentive awards** as the performance measures on which their respective 2025 annual
incentive awards were based were not met."* Only Mr Ready received 19.2% of target, on CWT
business-unit performance. **The bullseyes were pre-set, they were missed, and the bonus was
zero.** That is the [E2-49] standard met.

**Against it:** long-term incentives are **performance shares earned on relative total shareholder
return versus the S&P MidCap 400** plus stock options — i.e. **100% market-price-based**. The
2023–25 award paid at **153.95% of target** on a 42.59% TSR against the index's 35.94%.

**Say-on-pay:** approximately **77%** support in 2025, against *"an average of over 90% during the
five years prior"*, following a **$6.2 million one-time success payment to Mr John Berlin,
President of CIT, conditioned on the sale of CIT** (Letter Agreement, 8-K 2024-01-30). The company
then engaged holders of ~60% of the shares; ~18% accepted.

### The flags, run [E4-22, E5-15, E4-29, E4-30, E3-53, E2-52, E2-57, E3-50]

| flag | fires? | what the filing says |
|---|---|---|
| Weak accounting | **no** | SBC expensed; US pension largely settled ($21.1M settlement 2024, $3.0M 2025); Deloitte since 2017, unqualified opinion; one critical audit matter (Henry indefinite-lived trade name, $219.0M) |
| Unintelligible footnotes | **no** | 15 notes, plain language, short document |
| **Trumpeted projections / growth targets** | **YES** | Vision 2030 "$40 of adjusted EPS and 25%-plus ROIC"; annual February guidance; 2025 guidance missed on every limb |
| Serial share issuance [E5-15] | **no — the opposite** | 64.7M shares (2014) → 39.7M (2026); option exercises $23.5M in 2025 against $1,300.0M of repurchases |
| **EBITDA / adjusted-metric promotion [E4-29]** | **YES** | adjusted EBIT, adjusted EBITDA, adjusted EBITDA margin and adjusted EPS in every release and in the MD&A; the long-run corporate objective is stated **in an adjusted metric** |
| Cash tax % of pretax falling [E4-30] | **no** | 27.1% (2021), 26.3% (2022), 26.6% (2023), 29.2% (2024), 21.7% (2025) — no drift; 2025 equals the book rate |
| Unnaturally smooth growth [E4-30] | **no — the opposite** | operating income 573 → 1,205 → 983 → 1,143 → 1,003 |
| Restructuring [E3-53] | **no** | $9.8M (2025), $2.9M (2024), $6.3M (2022) — trivial against $1.0bn of operating income |
| Dividends funded by issuance [E2-52] | **no** | net repurchaser every year |
| **"Except for" [E2-57]** | **partial** | adjusted EPS $19.40 vs GAAP $17.16 (+13%) is driven mainly by adding back amortisation of acquired intangibles **while running a continuous acquisition programme**. The non-comparable items themselves are small: $27.5M on $1,001.4M of EBIT (2.7%) |
| Stock-price targeting [E3-50] | **mild** | *"Carlisle is committed to generating superior stockholder returns"*; LTI 100% market-based |
| Integrity matters | **none found** | Item 3: *"The Company is a party to certain lawsuits in the ordinary course of business."* Note 15: asbestos claims with insurance receivable; accrual *"not material"*. No regulatory or accounting action in the filed record. |

### Management, from the 10-K Item 10 and the proxy

- **D. Christian Koch, 61.** *"Chair of the Board of Directors since May 2020, Director, President
  and Chief Executive Officer since January 2016."* With Carlisle since February 2008. **~10.7
  years as CEO; combined Chair and CEO.**
- Beneficial ownership 306,253 shares — **~$106M at $346.58**, real skin.
- **No named successor.** The Corporate Governance and Nominating Committee *"discusses succession
  planning and recommends a new Chief Executive Officer as appropriate"*; Willis Towers Watson
  presented on *"leadership succession planning"* in September 2025. There is a Lead Independent
  Director.
- **CCM leadership changed in November 2025:** Stephen F. Schwar (41 years at Carlisle) moved to
  Vice Chair, CCM; **Jason L. Taylor** became President, CCM, having been *"President, West
  Division, Beacon Building Products from October 2020 to April 2025"* — **hired out of the
  largest customer.** CFO Kevin P. Zdimal since February 2022 (30 years at Carlisle). General
  Counsel replaced May 2025 (from Summit Materials).

### The [E3-54] retention read

- **Net retention over 2021–25 was NEGATIVE.** Net income $4,165.6M less dividends $760.7M less
  buybacks $4,501.5M = **−$1,096.6M**. Carlisle distributed more than it earned, funded by
  $2,888.3M of divestiture proceeds and $780.4M of net new debt. **The literal $1-for-$1 test does
  not bite because nothing was retained on a net basis.**
- The corpus's restated form (market value against the index) is published in the filing itself.
  Item 5 performance graph, $100 invested 2020-12-31: **CSL $216.26 · S&P 500 $196.16 · S&P MidCap
  400 $154.68.** Carlisle beat both over five years.
- **But 2025 alone: CSL 246.48 → 216.26 (−12.3%) while the S&P 500 rose 166.40 → 196.16 (+17.9%)
  — a 30-point underperformance in the most recent year.**

---
## 11. Q4 EVIDENCE — BALANCE SHEET, TERMS, COVERAGE

**Long-term debt, Note 13 (all fixed-rate unsecured senior notes):**

| instrument | principal | issued | matures |
|---|---|---|---|
| 3.75% Notes | $600.0M | 2017-11-16 | **2027-12-01** |
| 2.75% Notes | $750.0M | 2020-02-28 | 2030-03-01 |
| 2.20% Notes | $550.0M | 2021-09-28 | 2032-03-01 |
| 5.25% Notes | $500.0M | 2025-08-20 | 2035-09-15 |
| 5.55% Notes | $500.0M | 2025-08-20 | 2040-09-15 |
| discount, issuance costs, other | (13.6) | | |
| **Total debt** | **$2,886.4M** | | |

- **Revolver:** $1.0bn unsecured, undrawn, maturing **2029-04-03**, $500M accordion, $50M LC
  sublimit. No borrowings in 2025. *"The Company was in compliance with all covenants and
  limitations as of December 31, 2025, and 2024."* **The covenant levels are not disclosed** —
  the 10-K says only *"certain leverage and interest coverage ratios."*
- Cash **$1,112.1M** (2025-12-31), **$665.3M** (2026-06-30). Net debt $1,774.3M → **1.48x EBITDA**.
- Letters of credit and bank guarantees outstanding $48.8M.
- **[E2-54] coverage: (OCF − capex) ÷ interest expense = (1,101.8 − 131.2) ÷ 78.5 = 12.4x.**
  Cash interest paid $56.2M (2025), $70.2M (2024), $71.9M (2023).
- **[E3-52] terms:** all senior unsecured, fixed-coupon, make-whole redeemable, no maintenance
  covenant on the notes, laddered 2027/2030/2032/2035/2040. **Plus $372.3M of contract liabilities
  — customer-prepaid extended-warranty money with no covenant and no due date**, recognised over
  five to forty years ($29.8M in 2026, $231.3M "thereafter").
- Total equity $1,795.4M, depressed by $6,149.3M of treasury stock; **book equity is not a usable
  denominator for [E2-01]** and the [E2-43] tangible construction is used instead.

**Raw materials, verbatim risk factor:** *"The Company utilizes petroleum-based products,
chemicals, resins and other commodities in its manufacturing processes. **Raw materials, including
inbound freight, accounted for approximately 66% of the Company's cost of goods sold in 2025.**"*
→ $3,227.3M × 66% = **$2,130M of oil-linked input cost. A 10% unrecovered spike is $213M pre-tax,
21% of 2025 operating income.**

**Cyclicality, verbatim risk factor:** *"the CCM and CWT segments are susceptible to downturns in
the commercial construction industry, **particularly in the construction repair and replacement
sectors**, and the CWT segment is susceptible to downturns in the residential construction
industry."*

**Customer concentration, verbatim:**
- Item 1: *"in 2025 CCM's two largest customers represented **33% of the Company's consolidated
  revenues**. The loss of either of these customers could have a material adverse effect."*
- Note 6: *"QXO Inc. acquired Beacon Roofing Supply Inc. in April 2025. Revenues from QXO, Inc. and
  Beacon Roofing Supply, Inc. accounted for approximately **16.7%, 17.8% and 16.4%** … ABC Supply
  Co. accounted for approximately **16.3%, 15.9% and 15.3%**"* for 2025, 2024 and 2023.
- Risk factor: *"These markets have experienced **recent consolidation among distributors of
  roofing materials and complementary building products**."*

**End markets, Note 6 (2025):** non-residential construction **$4,028.7M (80.3%)**; residential
$863.1M (17.2%); other $128.1M (2.6%). **Geography: United States $4,500.3M = 89.6%** of revenue.

**Scale:** approximately **5,900 employees** at 2025-12-31 (4,800 in the US), ~500 unionised.
Revenue per employee **$851,000**.

---
## 12. THE Q5 ARITHMETIC

Market cap **$13,764.1M**. Sovereign **5.22%** (DGS30, 2026-08-28).

| owner-earnings case | $M | yield | pts vs sovereign | multiple | growth needed for the 10% floor |
|---|---|---|---|---|---|
| normalised bottom (CCM margin 24.0%) | 617.8 | **4.49%** | **−0.73** | 22.3x | 5.51% |
| **bottom boundary — 5y, (c)=D&A** | **699.4** | **5.08%** | **−0.14** | **19.7x** | **4.92%** |
| 5y, (c)=capex | 737.7 | 5.36% | +0.14 | 18.7x | 4.64% |
| 3y, (c)=D&A | 851.1 | 6.18% | +0.96 | 16.2x | 3.82% |
| **top — 3y, (c)=capex** | **910.2** | **6.61%** | **+1.39** | **15.1x** | **3.39%** |

Per share (39.714M): bottom **$17.61**, normalised bottom $15.56, top **$22.92**.
Value capitalised at the bare sovereign with zero growth: **$298 / $337 / $439**.
Value at the 10% floor with zero growth: **$156 / $176 / $229**.

**Incremental return on capital deployed 2021 → 2025:** acquisitions $2,418.6M + capex $705.0M =
**$3,123.6M invested**; operating income $573.4M → $1,002.5M = **+$429.1M**; **13.7% pre-tax,
10.7% after tax.** *If CCM's margin reverted to its 2021 level of 21.8%, 2025 operating income
would be $816.6M and the incremental return would be **7.8% pre-tax, 6.1% after tax — below the
sovereign.*** Both figures are reported.

---
## 13. WHAT COULD NOT BE OBTAINED

1. **The price-versus-volume split.** Carlisle publishes none. Route: **none exists in the filed
   record.** Proxies used: the organic-growth series, CCM's margin path, and the peer disclosures
   from Owens Corning and TopBuild. **No verdict rests on the missing figure**; it is recorded as
   an [E4-55] disclosure defect.
2. **Segment assets and segment ROIC.** Note 2, verbatim: *"The Company does not report total
   assets by segment as this is not a metric used by the CODM."* Route: none in the filings.
   Segment capex and D&A **are** given and are used.
3. **The revolver's covenant levels** (leverage and interest-coverage ratios). Route: the Fifth
   Amended and Restated Credit Agreement, filed as an exhibit to the 8-K of 2024-04 — not pulled,
   because the facility is undrawn and net leverage is 1.48x, so no verdict depends on it.
4. **Johns Manville, GAF/Standard Industries and Sika segment economics.** Route: none —
   wholly-owned subsidiary, private, and non-10-K filer respectively.
5. **The 50th consecutive dividend increase.** Not in the filed record at 2026-08-31. Route: the
   Carlisle dividend declaration press release and Q3 2026 10-Q, expected August–October 2026.
