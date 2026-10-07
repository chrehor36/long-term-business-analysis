# SandRidge Energy (NYSE: SD) — evidence pack
**Assembled 2026-08-31 for `Test Runs/2026-08-30 Run - SD (SandRidge) v4.1.md`.**
Every figure below is transcribed from a filed document named at the head of its section.
Where a number is computed, the arithmetic is shown. Where it is a judgment, it says so.

---

## 0. THE DOCUMENTS

| document | period | filed | accession | primary doc |
|---|---|---|---|---|
| Form 10-K | FY2025 (YE 2025-12-31) | 2026-03-05 | **0001628280-26-015318** | `sd-20251231.htm` |
| Form 10-Q | Q2 2026 (2026-06-30) | 2026-08-06 | **0001628280-26-054413** | `sd-20260630.htm` |
| Form 8-K + Ex-99.1 (Q2 26 results) | 2026-08-04/05 | 2026-08-05 | **0001628280-26-053557** | `sd-20260804.htm`, `sd6302026-ex991earningsrel.htm` |
| DEF 14A | 2026 annual meeting | 2026-04-27 | **0001140361-26-017133** | `ny20066631x1_def14a.htm` |
| Reserve report | YE2025 | filed as Ex-99.1 to the 10-K | Cawley, Gillespie & Associates — 97.9% of proved reserves |

Auditor: not re-verified this session beyond the filed statements themselves.
Local copies: `SD_10K_FY2025.htm/.txt`, `SD_10Q_Q2_2026.htm/.txt`, `SD_8K_2026-08-05_ex991.htm/.txt`,
`SD_DEF14A_2026.htm/.txt`, `SD_companyfacts.json`, `SD_submissions.json`, `DGS30_2026-08-31_SD.csv`.

**Cross-check performed (operator protocol 4).** The filed Consolidated Statements of Cash Flows
in the FY2025 10-K reads, on the line "Net cash provided by operating activities":

> **100,140 · 73,933 · 115,578** (FY2025 · FY2024 · FY2023, $ thousands)

SEC XBRL `companyfacts` carries the identical three values under
`NetCashProvidedByUsedInOperatingActivities`. **Ties. The prior session's figures are re-verified.**
Second cross-check: Q2 2026 net income $26,693K ÷ 36,906K basic weighted shares = $0.723 = the
filed basic EPS of $0.72. Ties.

---

## 1. PRICE AND MARKET CAPITALISATION — verified against filed shares

- **Shares outstanding: 37,075,296**, from the Q2 2026 10-Q cover page: *"The number of shares
  outstanding of the registrant's common stock, par value $0.001 per share, as of the close of
  business on July 30, 2026, was 37,075,296."* Balance-sheet line agrees: 37,075 (thousands)
  issued and outstanding at 2026-06-30.
- **Price $13.96, NYSE close 2026-08-28** (Yahoo chart API — aggregator, live quote only, flagged
  per operator protocol 5). 52-week range $11.10–$18.45; trailing-year daily-close range
  $11.19–$18.08.
- **Market cap = 37,075,296 × $13.96 = $517.6M.** The operator sweep's ~$515M is **verified**
  (the difference is the quote date).
- Cross-reference: the 10-K cover states non-affiliate market value $340.1M at 2025-06-30.
- **Sovereign: USD 30-year Treasury constant maturity 5.19%, observation date 2026-08-27**,
  fetched direct from `fredgraph.csv?id=DGS30` on 2026-08-31 (issuing-authority series via FRED;
  the 1–2 day publication lag is standing and immaterial). Local: `DGS30_2026-08-31_SD.csv`.

---

## 2. THE DIVIDEND, DECOMPOSED — the company's own filed table

**Source: 8-K Ex-99.1, 2026-08-05, section "Dividend Program" ($ thousands).** This is not a
reconstruction; SandRidge publishes the split itself.

| | **Total since 2023** | 2Q26 | 1Q26 | FY2025 | FY2024 | FY2023 |
|---|---|---|---|---|---|---|
| **Special dividends** | **$136,651** | $6,445 | — | **—** | $55,868 | $74,338 |
| **Quarterly dividends** | **$47,786** | $4,190 | $3,868 | $15,862 | $16,426 | $7,440 |
| Total | $184,437 | $10,635 | $3,868 | $15,862 | $72,294 | $81,778 |

Per share, same table:

| | **Total** | 2Q26 | 1Q26 | FY2025 | FY2024 | FY2023 |
|---|---|---|---|---|---|---|
| **Special per share** | **$3.70** | $0.20 | — | — | $1.50 | $2.00 |
| **Quarterly per share** | **$1.35** | $0.13 | $0.12 | $0.46 | $0.44 | $0.20 |
| Total per share | $5.05 | $0.33 | $0.12 | $0.46 | $1.94 | $2.20 |

And the 10-Q MD&A states it in words: *"Since 2023, the Company has paid cash dividends totaling
$184.2 million … which represents **$3.70 per share in special dividends and $1.35 per share in
quarterly dividends** for a total of $5.05 per share."*

**The decomposition, in one line: 74% of every dollar SandRidge has returned as a dividend since
2023 was a special.** $136.7M of $184.4M.

**Where the specials came from.** Cash and equivalents including restricted cash:
2022-12-31 $257.5M → 2023-12-31 $253.9M → **2024-12-31 $99.5M** → 2025-12-31 $112.3M →
2026-06-30 $114.7M. The $2.00 (June 2023) and $1.50 (February 2024) specials were paid out of the
post-2021/22 cash pile, not out of the year's earnings: FY2024 dividends of $72.3M against FY2024
operating cash flow of $73.9M **and** capex of $26.4M **and** acquisitions of $129.7M — the cash
balance fell $154.4M that year. The specials were a **balance-sheet distribution**, and the
balance sheet has since been rebuilt and is about to be spent again (§7).

**The regular leg, at the current quote.** Latest declared regular quarterly dividend **$0.13**
(declared 2026-08-04, payable 2026-08-31, record 2026-08-19; 8-K Ex-99.1). Annualised
$0.52 ÷ $13.96 = **3.7%**. Trend of the regular leg: $0.10 → $0.11 → $0.12 → $0.13 per quarter
(2023 → 2026), i.e. **+$0.01/qtr per year**, a 30% rise in three years off a small base.

A dividend reinvestment plan was adopted 2025-08-05; 92,733 shares were issued in lieu of cash in
2025 and 143,343 in 2Q26. DRIP take-up reduces cash out but **increases the share count** — the
opposite direction to a buyback, and it is why "aggregate cash dividend payments" understates the
declared distribution.

---

## 3. THE RESERVE ARITHMETIC — the [E5-20] exception, worked

### 3.1 Reserves, PV-10 and standardized measure (10-K Items 1 and 8)

| | FY2025 | FY2024 | FY2023 |
|---|---|---|---|
| Total proved (MMBoe) | **69.1** | 63.1 | 55.7 |
| — proved developed | 60.3 | 57.0 | 55.7 |
| — proved undeveloped | 8.8 | 6.1 | 0.0 |
| **PV-10 ($M)** | **439.6** | 362.7 | 296.3 |
| Standardized measure ($M) | **439.6** | 362.7 | 296.3 |
| SEC index oil / gas | $65.34/Bbl · $3.39/MMBtu | $75.48 · $2.13 | — |
| Realised wellhead oil / gas / NGL | $64.15 · $2.07/Mcf · $17.13 | $74.04 · $1.02 · $19.40 | $76.65 · $1.62 · $21.53 |

**PV-10 equals standardized measure exactly, in all three years, because the "Future income tax
expenses" line in the standardized measure is $0.** The 10-K's own footnote says why: future
income taxes are *"computed using statutory tax rates, giving effect to allowable tax deductions
and tax credits under current laws, **including expected tax benefits to be realized from the
utilization of net operating loss carryforwards**."* **The NOL shield is already inside the PV-10.
Adding the NOL to PV-10 as a separate asset double-counts it over the life of the proved book.**

Undiscounted future net cash flows FY2025: inflows $1,542.1M − production costs $592.5M −
development costs $135.3M (*"includes abandonment costs"*) − tax $0 = **$814.3M**, less a 10%
discount of $374.7M = $439.6M.

### 3.2 The ten-year physical series — the [E4-55] units read

Total proved reserves at each year end, MBoe, from the 10-K series in XBRL
(`ProvedDevelopedAndUndevelopedReserveNetEnergy`, all 10-K-sourced):

| 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| 164.0 | **177.6** | 160.2 | 89.9 | 36.9 | 71.3 | 74.3 | 55.7 | 63.1 | **69.1** |

**Down 61% from the 2017 peak.** The series whipsaws on SEC price, which is exactly why the
company's own filing says reserve estimates *"are subject to change"* — but the direction over a
decade is one way. Production over the same decade ran 6–20 MMBoe/yr.

### 3.3 Reserve replacement and finding cost — computed from the filed rollforward

Rollforward (10-K Note 20, MBoe):

| | 2023 | 2024 | 2025 | 3-yr |
|---|---|---|---|---|
| Opening | 74,324 | 55,677 | 63,090 | |
| Revisions of previous estimates | (15,304) | (2,503) | +3,852 | (13,955) |
| Acquisitions (purchases in place) | 1,745 | 15,971 | 1,677 | **19,393** |
| Extensions and discoveries | 1,211 | 1 | 7,298 | **8,510** |
| Sales in place | (147) | — | — | (147) |
| **Production** | **(6,152)** | **(6,056)** | **(6,768)** | **(18,976)** |
| Closing | 55,677 | 63,090 | 69,148 | |

Costs incurred (10-K Note 20, $ thousands):

| | 2023 | 2024 | 2025 | 3-yr |
|---|---|---|---|---|
| Acquisitions — proved | 11,232 | 126,998 | 2,331 | 140,561 |
| Acquisitions — unproved | — | 2,666 | 6,183 | 8,849 |
| Exploration | (46) | 11,246 | 5,016 | 16,216 |
| Development | 22,478 | 15,562 | 63,970 | 101,010 |
| **Total costs incurred** | **33,664** | **156,472** | **77,500** | **267,636** |

**Computed:**

| measure | 3-yr FY2023–25 | arithmetic |
|---|---|---|
| **Organic reserve replacement** (extensions & discoveries ÷ production) | **45%** | 8,510 ÷ 18,976 |
| All-in replacement (extensions + purchases ÷ production) | 147% | 27,903 ÷ 18,976 |
| **Organic F&D cost** | **$13.89/Boe** | ($101.0M dev + $16.2M expl) ÷ 8.510 MMBoe |
| Acquisition cost | $7.70/Boe | $149.4M ÷ 19.393 MMBoe |
| **Blended all-in finding & acquisition cost** | **$9.59/Boe** | $267.6M ÷ 27.903 MMBoe |
| Book depletion rate charged, FY2025 | **$5.38/Boe** | $36.439M oil-and-gas depletion ÷ 6.768 MMBoe |

**The [E5-20] test, stated as arithmetic.** To hold unit volume, SandRidge must replace
6.768 MMBoe a year.

- at the blended $9.59/Boe: **≈ $65M/yr**
- at the organic-only $13.89/Boe: **≈ $94M/yr**
- **against FY2025 total D&A of $42.9M and oil-and-gas depletion of $36.4M.**

**Spending depreciation does not hold unit volume here. It holds roughly half of it.** The
company's own forward number confirms the direction, not the D&A default: the 10-K guides
**"we intend to spend between $76.0 million and $97.0 million in our 2026 capital budget plan"** —
1.8× to 2.3× FY2025 D&A.

Over three years the company spent **$267.6M of costs incurred against $289.7M of cumulative
operating cash flow — 92% of all operating cash back into the ground** — and total proved reserves
went from 74.3 MMBoe (YE2022) to 69.1 MMBoe (YE2025). *(Honest caveat: the YE2022 base was booked
at 2022 SEC gas prices, so part of the fall is price revision, not physical. The revision line
alone is −14.0 MMBoe over the three years.)*

Reserve life at FY2025: total proved 69.1 ÷ 6.768 = **10.2 years**; proved developed 60.3 ÷ 6.768
= **8.9 years**.

---

## 4. THE NOL — valued explicitly, and the double-count identified

**Source: FY2025 10-K Note 12 (Income Taxes) and Risk Factors "Risks Relating to our NOLs".**

Filed facts:
- *"As of December 31, 2025, the Company had approximately **$1.6 billion of federal NOL
  carryforwards**, net of NOLs expected to expire unused due to the 2016 IRC Section 382
  limitation. Of the $1.6 billion, **$0.7 billion expire during the years 2028 through 2037**,
  while $0.9 billion do not have an expiration date."*
- ~$1.0bn of state NOLs ($199.0M from states it does not operate in; $645.0M no expiry;
  $176.0M expiring 2025–2037). Federal tax credits >$33.5M, **beginning to expire in 2029**.
- Deferred tax asset table, $ thousands (FY2025 / FY2024):

| | 2025 | 2024 |
|---|---|---|
| PP&E | 50,421 | 57,061 |
| **NOL carryforwards** | **363,807** | 373,506 |
| Tax credits and other carryforwards | 33,851 | 33,851 |
| Asset retirement obligations | 13,091 | 13,327 |
| Other | 2,033 | 1,551 |
| **Gross deferred tax assets** | **463,203** | 479,296 |
| **Valuation allowance** | **(384,867)** | (406,495) |
| **Net deferred tax asset** | **78,336** | 72,801 |

- Current federal and state income tax: **$0 in each of FY2023, FY2024 and FY2025.**
- A **Tax Benefits Preservation Plan** (a 4.9% NOL poison pill) adopted 2020-07-01, amended
  2021-03-16, 2023-06-20 and **2026-06-15 to extend expiry from 2026-07-01 to 2029-07-01**; the
  board *"plans to request shareholder approval for the third amendment … at the 2027 annual
  meeting."*

**How to value it, honestly, in three steps:**

1. **The headline $1.6bn is not the asset.** The asset is the tax it shields. At the 21% federal
   rate, $1.6bn of federal NOL shields at most **~$336M of cash tax**, undiscounted, over an
   unbounded horizon, and $0.7bn of it dies between 2028 and 2037.
2. **Management's own filed judgment is $78.3M.** The company recognises $78.3M of net deferred
   tax asset and carries a **$384.9M valuation allowance** against the rest — i.e. its own auditors'
   more-likely-than-not test says the remaining shield is **not** expected to be realised. Under
   [E5-32]'s discipline (audited is not bedrock) this is still the best available filed estimate,
   and it cuts against the analyst's wish, not for it.
3. **Most of even that is already inside PV-10.** PV-10 = standardized measure exactly because the
   reserve report already sets future income tax to zero *by reason of the NOLs*. The undiscounted
   future net cash flow of the proved book is $814.3M; the shield consumed against it is the
   reason the $439.6M carries no tax deduction. **The incremental, non-double-counted value of the
   NOL is only the shield on income the proved book does not produce** — from reserves not yet
   booked, from acquisitions, from any future business.

**Range carried into the asset basis: $0 incremental (conservative, no double-count) to $78.3M
(generous, management's entire booked figure treated as incremental).** A number above $78.3M
would be the analyst overriding both management and the auditor in the direction the analyst
wants — precisely the move rule 9 exists to stop.

---

## 5. THE OWNER-EARNINGS TABLE — filed inputs

All from the filed cash-flow statements (FY2025 10-K for 2023–25; XBRL `companyfacts`, 10-K-sourced,
for 2021–22). $ millions.

| FY | OCF | capex (PP&E) | acquisitions | D&A | SBC | net income |
|---|---|---|---|---|---|---|
| 2021 | 110.3 | 11.6 | n/d | 15.4 | 1.4 | 116.7 |
| 2022 | 164.7 | 44.1 | n/d | 17.9 | 1.5 | 242.2 |
| 2023 | 115.6 | 26.4 | 11.2 | 22.2 | 1.9 | 60.9 |
| 2024 | 73.9 | 26.4 | 129.7 | 32.5 | 2.4 | 63.0 |
| 2025 | **100.1** | 58.6 | 8.5 | 42.9 | 2.7 | 70.2 |
| H1 2026 | 62.2 | 40.1 | 5.1 | 23.6 | 1.5 | 45.4 |

Means:

| window | OCF | capex | D&A | SBC | OE (c=capex) | OE (c=D&A) |
|---|---|---|---|---|---|---|
| 5-yr FY2021–25 | 112.9 | 33.4 | 26.2 | 2.0 | **$77.5M** | **$84.8M** |
| 3-yr FY2023–25 | 96.6 | 37.1 | 32.5 | 2.3 | **$57.1M** | **$61.7M** |

Yields on $517.6M: 5-yr 15.0%–16.4%; 3-yr **11.0%–11.9%**.
**The operator sweep's 11.8% "statute yield" is identified: it is the 3-year window at the
c = D&A end (11.9%).** Both ends of both windows are refused below on [E5-20]/[E4-41] grounds.

### The distorted years, named [E5-11] / [E4-41]

- **FY2021–22 is the post-COVID / post-invasion gas spike.** The filing's own volatility
  disclosure: NYMEX Henry Hub spot between **$24.77 and $1.26 per Mcf** over 2021–2025; WTI between
  $123.64 and $47.47. FY2022 net income of $242.2M also contains a **$64.5M income tax benefit**
  (valuation-allowance release), not cash.
- **FY2024 is the reverse distortion** — the company drilled **zero operated wells** that year
  ("During the year ended December 31, 2024, there were no operated wells drilled"), so its $26.4M
  capex is an underspend against maintenance, not a maintenance figure.
- **H1 2026 contains an oil spike.** Realised oil per barrel: **$62.80 (2Q25) → $95.35 (2Q26)**,
  +52%, while realised gas fell $1.82 → $1.36/Mcf. Oil was 18% of 2Q26 volume and **61% of 2Q26
  revenue**. Any annualisation of H1-26 is annualising an oil price, not a business.

### The (c) judgment — disclosed, per [E2-23] constraint 4

D&A is the corpus default for (c) **[E3-44, E2-41]**, but [E5-20] names the exception class and
[E4-04] scopes it: the moat *"whose basis must be periodically replaced … depleting assets."* An
E&P is the purest member of that class — a produced barrel is gone. The filed replacement
arithmetic (§3.3) gives $65M–$94M/yr against $42.9M of D&A, and the company's own 2026 budget of
$76–97M sits inside the replacement range and outside the D&A one. **Therefore the D&A end of the
band is INVALID here, not merely optimistic, and (c) is judged up to $65M–$94M.**

**Normalized owner earnings, the bottom boundary [E5-34]** — FY2023–25 mean OCF $96.6M less SBC
$2.3M = $94.3M available, less (c):

| (c) basis | (c) | OE | yield on $517.6M |
|---|---|---|---|
| D&A (default — **refused**, [E5-20]) | 32.5 | 61.7 | 11.9% |
| capex as spent (contains the zero-rig 2024) | 37.1 | 57.1 | 11.0% |
| **blended replacement cost $9.59/Boe** | **65.0** | **$29.3M** | **5.7%** |
| **organic F&D $13.89/Boe** | **94.0** | **$0.3M** | **0.1%** |
| company's own 2026 budget, midpoint | 86.5 | $7.8M | 1.5% |

**Bottom boundary: ≈ $0M to $29M of owner earnings; ≈ 0% to 5.7% on the current quote.**

---

## 6. THE ASSET BASIS, beside the owner-earnings convention

Balance sheet at **2026-06-30** (10-Q): total assets $668.1M; total liabilities $125.4M
(accounts payable and accrued $49.0M, ARO current $8.0M, ARO non-current $66.9M, other $1.5M);
**stockholders' equity $542.7M**; **no term or revolving debt** (10-Q: *"The Company had no
outstanding term or revolving debt obligations as of June 30, 2026"*). Cash and equivalents
including $1.3M restricted: **$114.7M**.

| component | conservative | generous | source / treatment |
|---|---|---|---|
| PV-10, proved reserves, YE2025 SEC prices | **439.6** | **439.6** | 10-K; net of production, development **and abandonment** costs; tax already zero |
| Cash and equivalents incl. restricted | **114.7** | **114.7** | 10-Q 2026-06-30 |
| Total debt | **0** | **0** | 10-Q |
| Non-cash working capital | **(20.8)** | (12.8) | CA ex-cash $37.0M − CL $57.8M; generous adds back current ARO $8.0M (already inside PV-10 abandonment) |
| Corporate G&A, absent from PV-10 by definition | **(81.1)** | (62.7) | 10-K G&A $13.2M/yr (adjusted, ex-SBC: $10.2M) × 10-yr annuity factor at 10% (6.145) |
| Other PP&E, net | **0** | +72.6 | 10-Q; field infrastructure/disposal/office — conservative case treats it as subsumed in the PV-10's LOE |
| **NOL, incremental to PV-10** | **0** | **+78.3** | §4 — conservative avoids the double-count; generous is management's entire booked net DTA |
| **Asset basis** | **≈ $452M** | **≈ $630M** | |
| **per share (37.075M shares)** | **≈ $12.20** | **≈ $17.00** | |

**Market cap $517.6M / $13.96 sits inside that range, nearer the bottom half.**
Pro-forma for the pending **$65.0M** Cherokee acquisition (§7) the cash leg falls to ~$50M and the
acquired assets replace it — value-neutral by construction until they are booked.

**Sensitivity that matters.** PV-10 is struck at YE2025 SEC prices of $65.34/Bbl oil and
$3.39/MMBtu gas. In 2Q26 SandRidge realised **$95.35/Bbl oil** (far above) and **$1.36/Mcf gas**
(far below). Gas is 50% of volume; oil is 18%. The PV-10 is not a conservative number in one
direction or the other — it is a snapshot of a twelve-month trailing average that has already
moved, and a 10% discount rate is generous for a single-basin depleting asset. This is why the
asset basis is carried as a *range* and not as a floor.

---

## 7. THE PENDING ACQUISITION

10-Q Note (subsequent/commitments) and 8-K Ex-99.1: *"On June 26, 2026, the Company entered into a
purchase and sale agreement for the acquisition of certain producing assets and leasehold interests
in the Cherokee Play of the Mid-Continent region for **$65.0 million**, subject to customary
purchase price adjustments, and **three contingent earn-out payments of $2.0 million each**, based
on exceeding the average daily spot price for West Texas Intermediate crude oil at certain price
thresholds beginning July 1, 2026 and ending December 31, 2027. **The Company expects to fund the
acquisition with cash on hand.** The acquisition is expected to close during the third quarter of
2026 and will be effective May 1, 2026."* Adds ~7,000 net leasehold acres, interests in 21 wells,
eight proven development locations.

**This spends 57% of the cash pile.** It is the third time in four years the balance sheet has been
converted into reserves or specials ($129.7M of acquisitions in 2024; $136.7M of specials
2023–2026; $65M now).

---

## 8. Q3 MATERIAL — the record, from the DEF 14A and the filings

**Ownership (DEF 14A, as of 2026-04-13, on 36,918,259 shares):**
Carl Icahn **13.1%** (4,818,832 shares) · BlackRock 6.6% · all directors and executive officers as
a group **1.6%** (578,701 shares). CEO Pranin personally 173,879 shares (<1%). Vanguard omitted
from the table by reason of its January 2026 internal realignment (footnote 1).

**The board as nominated for the 2026 meeting** — Firestone, B. Icahn, Intrieri, Katz, Pranin,
Dunlap:

| director | since | Icahn connection, as disclosed in the proxy |
|---|---|---|
| Vincent Intrieri (**Chairman**) | Oct 2024 | *"employed by Carl C. Icahn-related entities … from 1998 to 2016"*; Senior MD of Icahn Capital LP 2008–2016 |
| **Brett Icahn** | Aug 2025 | board of Icahn Enterprises L.P.; Portfolio Manager at Icahn Capital LP |
| Nancy Dunlap | Oct 2022 | director of **Icahn Enterprises G.P. Inc.** since April 2021; ex-CVR Refining |
| Jaffrey Firestone | May 2021 | director of **CVR Energy** since 2020; ex-**Voltari** (*"indirectly controlled by Carl C. Icahn"*) |
| Jacob Katz | new nominee | ex-Grant Thornton national managing partner; audit chair; no disclosed Icahn tie |
| Grayson Pranin (CEO) | Jun 2025 | not independent |

**Management, and the churn:**
- **CEO Grayson Pranin** — President and CEO since **2021-07-16**; at SandRidge since Dec 2011;
  joined the board June 2025.
- **CFO Jonathan Frates** — appointed **2024-10-21**. Ex-Managing Director of **Icahn Enterprises
  L.P. (2015–2021)**, and *"previously served as **Chairman of the Board of Directors of the
  Company from June 2018 until September 2024**."* **The board chairman moved into the CFO chair.**
- **Brandon Brown** — CFO **Sept 2023 → Oct 2024** (13 months), then moved to Chief Accounting
  Officer. Three people have held or vacated the CFO seat inside three years.
- **Dean Parrish** — promoted to EVP and COO **2026-03-11**.
- John "Jack" Lipinski left the board on **2025-06-11**.

**Compensation design (DEF 14A).** The 2025 annual incentive runs on **seven metrics** —
health/safety/environmental (10%), total capex (15%), and five others — with payout capped at 150%
of target. The 2025 LTIP PSU metrics are **Adjusted G&A ($10.0–12.0M target; $10.2M actual)**,
**LOE ($42.0–50.0M; $40.4M actual)**, **base oil production (1.00–1.40 MMBbls; 1.21 actual)**, and
**total production AND capex (5.90–7.10 MMBoe and $66.0–85.0M; 6.80 MMBoe and $76.2M actual)**.
**No Adjusted-EBITDA and no TSR metric in the incentive plan.** Capex is a *ceiling* metric, and
production is bounded top and bottom — the design pays for spending discipline, not for growth.

**Non-GAAP promotion [E4-29] — read carefully, because the answer differs by document:**
- **FY2025 10-K: zero occurrences of "Adjusted EBITDA". Zero occurrences of "free cash flow."**
  The only non-GAAP measure in the 10-K is PV-10, and it is labelled as one with the standardized
  measure printed beside it.
- **Q2 2026 10-Q: zero occurrences of "Adjusted EBITDA".**
- **8-K Ex-99.1 earnings release: leads with Adjusted net income, Adjusted operating cash flow,
  Adjusted EBITDA ($34.0M) and Free cash flow ($23.2M)** in the highlights and the first table,
  with GAAP net income and GAAP operating cash flow on the same lines above them, and a
  "Non-GAAP Financial Measures" reconciliation section.

**Buyback record.** $75.0M authorised May 2023 (replacing a $25.0M authorisation from Aug 2021).
Life-to-date: **0.6M shares at an average of $10.75**, $68.3M of the authorisation still open at
2026-06-30. FY2025: 595,635 shares for $6.4M. FY2024: 21,308 shares for $0.2M. 2Q26: none.
**The average price paid is 23% below the current quote** — the opposite shape to the usual
buy-high-abstain-low record.

**Legal (10-K Note 11).** All pre-2016 securities claims were discharged in the Chapter 11 plan
(emerged 2016-10-04). *In re SandRidge Energy Securities Litigation* and *Lanier Trust*: on
**2025-09-11** the Western District of Oklahoma granted summary judgment for the Trust and
dismissed all claims against the Company with prejudice; the appeal right has expired. One live
matter: two settling individual defendants' insurers funded a **$17.0M** settlement and seek
indemnification; the Company refused, litigation continues to the Fifth Circuit; **no liability
established**. Per the TJX calibration this is a legacy-of-the-predecessor dispute, not financial
dishonesty toward today's owners.

---

## 9. THE PRICE-TAKER DISCLOSURE — Q2's evidence, in the filer's own words

- **Item 7A, first line:** *"**Our most significant market risk relates to the prices we receive
  for our oil, natural gas and NGLs.**"*
- **Item 1A:** *"These factors and the volatility of the energy markets, which we expect will
  continue, make it **extremely difficult to predict future oil, natural gas and NGL price
  movements with any certainty**."* The listed factors are worldwide political conditions, global
  inventories, weather, alternative fuels, pipeline capacity, regulation, the dollar — **twenty
  items, none of which SandRidge influences.**
- **Item 1:** *"The price of oil, natural gas and NGLs is not currently regulated and are made at
  market prices."* ([E3-03] criterion 3 passes; criterion 2 fails on the same sentence.)
- **MD&A:** *"Our cash flows from operations are **substantially dependent on current and future
  prices for oil, natural gas and NGL**, which historically have been, and may continue to be,
  volatile."*
- **Competition risk factor:** *"The oil and natural gas industry is intensely competitive, and we
  compete with many companies that have **greater financial and other resources than we do** …
  These companies **may be able to pay more for productive oil and natural gas properties** …"* —
  the scarce input (acreage) is bought at auction against better-capitalised bidders.
- **Full-cost ceiling:** *"Cumulative full cost ceiling impairment from the Emergence Date through
  December 31, 2025 totaled **$947.1 million**."* Note the consequence for the primary test
  [E2-01]: an equity denominator shrunk by $947.1M of write-offs flatters every return ratio
  computed on it — [E2-47]'s mis-stated-asset-values carve-out applies.

---

## 10. THE FIGURES CARRIED TO THE RUN FILE

| | |
|---|---|
| Sovereign USD 30y | **5.19%**, 2026-08-27, FRED DGS30 |
| Price · shares · cap | $13.96 (2026-08-28) · 37,075,296 (10-Q cover, 2026-07-30) · **$517.6M** |
| Regular dividend | $0.13/qtr → $0.52/yr → **3.7%** |
| Special dividends since 2023 | **$3.70/sh, 74% of all dividends paid** |
| OCF FY2025/24/23 | **100.1 / 73.9 / 115.6** — verified against the filed statement |
| 5-yr OE band (refused) | $77.5M–$84.8M → 15.0%–16.4% |
| 3-yr OE band (the sweep's number) | $57.1M–$61.7M → 11.0%–**11.9%** |
| **Bottom-boundary OE** | **$0M–$29M → 0%–5.7%** |
| Replacement cost of one year's production | **$65M–$94M** vs D&A $42.9M |
| 2026 capital budget, company's own | **$76M–$97M** |
| Organic reserve replacement, 3-yr | **45%** |
| PV-10 (YE2025 SEC prices) | **$439.6M** |
| Net cash | **$114.7M, zero debt** (before the $65M acquisition) |
| NOL: headline / booked / incremental to PV-10 | $1.6bn federal / **$78.3M** net DTA / **$0–78.3M** |
| Asset basis | **≈ $452M–$630M ≈ $12.20–$17.00/share** |
| Proved reserves / reserve life | 69.1 MMBoe / **10.2 yrs** (PDP 8.9 yrs) |
