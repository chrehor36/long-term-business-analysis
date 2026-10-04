# Company Run — SYNOPSYS, INC. (SNPS) — 2026-09-07 (resumed 2026-09-11)
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*Run opened 2026-09-07, killed by the weekly session limit after the research pull, resumed
2026-09-11 with the research intact on disk (`_research 2026-09-07 SNPS/`). The sovereign and
the price were re-struck on resumption; the brief's 5.24% is stale and is not used.*

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- **rate 5.37%** · **date 2026-09-10** · source: **US Treasury daily par yield curve,
  30-year, from the issuing authority** (`tools/sources.py`, struck fresh on resumption per
  operator rule 5; FRED is the fallback, not the source). *The brief carried 5.24% of
  2026-09-04; the rate moved +13bp while the run was down and the fresh figure is used
  everywhere below.*
- Earnings currency **USD**. Synopsys is a Delaware domestic filer reporting in USD; roughly
  half of revenue is billed outside the US (10-K Item 1A: *"We derive roughly half of our
  revenue from sales outside the United States"*), in dollars, with FX forwards on the
  non-functional-currency exposures. That is an exposure question for Q2 and Q4, not a
  repricing question. **Single class**, direct Nasdaq listing. No ADR ratio.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Form 10-K, FY ended 2025-10-31, filed 2025-12-22, accession `0000883241-25-000028`** —
  the anchor annual document. Notes read in full: 2 (policies), 3 (discontinued operations),
  4 (business combinations — Ansys), 5 (revenue, backlog), 6 (goodwill and intangibles), 7
  (balance sheet components), 10 (debt), 19 (segments), 20 (restructuring).
- **Form 10-Q, quarter ended 2026-07-31, filed 2026-08-26, accession `0000883241-26-000025`**
  — **the current perimeter document.** The brief's `newest_filing 2025-10-31` is the 10-K's
  period end; three 10-Qs have been filed since and the Q3 one carries nine months of a
  fully-consolidated Ansys, the term-loan repayment, the NVIDIA placement, the Processor IP
  divestiture and the enlarged restructuring plan. Every level-setting number in this file is
  taken from it.
- **Form 8-K/A, filed 2026-08-26, accession `0001193125-26-368858`** (restructuring plan
  enlarged to $425–500M); **8-K EX-99.1 earnings releases**, eight consecutive, 2024-12-04
  through 2026-08-26 (accessions in the Q3 guidance table); **DEF 14A filed 2026-02-19,
  accession `0000883241-26-000007`**.
- **Figure cross-checked against the filed statement:** *Net cash provided by operating
  activities*, FY2025 Consolidated Statements of Cash Flows, **$1,518,608 thousand** — agrees
  with the tagged series to the dollar; and *Purchases of property and equipment, net*
  **$(169,454)**, *Stock-based compensation* **$893,294**, *Amortization and depreciation*
  **$660,430**, all to the dollar. Segment revenue in Note 19 ($5,302,340 + $1,751,838 =
  $7,054,178) reproduces the income statement total to the dollar.
- *Note on the 8-K/A the brief called "the ANSYS PRO FORMA 8-K/A" (`0001193125-25-207472`,
  filed 2025-09-18): it is NOT a pro forma. It is a one-paragraph amendment adding a
  committee appointment for a new director. The ASC 805 pro forma lives in the 10-K, Note 4
  — and it is filed, which is the AVGO/CRM shortcut. Recorded as a defect in the brief.*

**Price and shares:**
- price **$397.17**, 2026-09-10 close (aggregator via `tools/run.py` — **live quote only,
  flagged** per operator rule 5).
- shares **191,636,646**, hand-read off the **Q3 FY2026 10-Q cover**: *"As of August 24,
  2026, there were 191,636,646 shares of the registrant's common stock outstanding."*
  **Single class.** The balance sheet at 2026-07-31 shows 191,605 thousand outstanding
  (433 thousand in treasury), consistent.
- **market cap $76,112M** (191,636,646 × $397.17). The brief's `cap_m 79495` was struck at a
  higher quote on the same share basis; the construction is the same.
- **THE SHARE-COUNT GUARD, checked by hand because the count moved 24% in a year.** 10-K
  cover counts, fifteen consecutive years: 149.3M (Dec 2010) · 144.2 · 151.2 · 154.3 ·
  153.1 · 151.5 · 150.1 · 148.7 · 149.5 · 150.5 · 153.0 · 153.4 · 152.4 · 152.0 · **154.6M
  (Dec 2024) → 191.3M (Dec 2025) → 191.6M (Aug 2026).** The step is **+30.0M shares issued
  for Ansys** (Note 4: *"30.0 million shares of Synopsys Common Stock issued to settle 88.1
  million outstanding shares of Ansys Common Stock"*) **plus 4.8M sold to NVIDIA** (10-Q:
  *"we sold an aggregate of approximately 4.8 million shares of our common stock in a
  private placement at a price of $414.79 per share for net proceeds of $2.0 billion"*), net
  of ~0.7M repurchased. **No split; the count is used as filed.** *The fifteen flat years
  before the step are themselves a finding, recorded at Q3 under [E5-15]: a decade and a
  half of buybacks retired exactly the stock that compensation issued, and not one share
  more.*

---
# STAGE 0 — THE PERIMETER, BEFORE ANY ARITHMETIC

*Method from the AVGO and CRM runs, which put this section above Q1 for the same reason. The
brief's instruction was: establish what closed, when, for how much, how much was stock,
whether a pro forma was filed, and whether the owner-earnings window mixes two companies.
All five are answered from the filings.*

## What closed, when, for how much, and how much was stock

**Ansys closed 2025-07-17** — Note 4, FY2025 10-K, the allocation table verbatim:

| Aggregate purchase consideration | $ thousands |
|---|---|
| Cash for outstanding Ansys Common Stock (88.1M shares × $199.91) | **17,613,185** |
| Fair value of Synopsys Common Stock issued (30.0M shares × $571.20) | **17,105,538** |
| Fair value of assumed Ansys equity awards, pre-combination | 130,963 |
| Settlement of pre-existing relationships | 8,794 |
| **Total purchase consideration** | **34,858,480** |
| Less: cash acquired | (931,740) |
| **Total, net of cash acquired** | **33,926,740** |
| of which **Goodwill** | **23,442,889** (67% of the price) |
| of which **Intangible assets** | **12,990,000** |

- **$34.9bn paid; $17.6bn cash (50.5%), $17.1bn stock (49.1%).** The stock was issued at
  **$571.20** a share — 44% above the price on the day this file is written.
- **What the acquisition flag saw:** the investing line *"Acquisitions, net of cash
  acquired"* is **$(16,681,257) thousand** in FY2025. **The $17.1bn stock half is invisible
  to `PaymentsToAcquireBusinessesNetOfCashAcquired`** — the CERT/CRM defect, here at a
  seventeen-billion-dollar scale. Any tool that read the investing line saw half the deal.
- **Financed** by $10.0bn of Senior Notes (March 2025; six tranches, 4.55%–5.70%, maturing
  April 2027 to April 2055) plus the full $4.3bn term loan drawn on closing day, plus cash.
  Since closing: **$850M of the term loan repaid 2025-10-17 and the remaining $3.5bn repaid
  in Q1 FY2026** — *"the Term Loans were terminated upon repayment"* — funded by the $2.0bn
  NVIDIA placement, the $443M Processor IP sale and operating cash. **Debt at 2026-07-31:
  Senior Notes $9.9bn outstanding, $1,020M of it current** (the April 2027 tranche).
- **Regulatory divestitures** (a condition of approval): Synopsys's Optical Solutions Group
  and Ansys's PowerArtist RTL to Keysight, **closed 2025-10-17 for $604.0M cash, pre-tax
  gain $548.9M** ($516.3M net of $32.6M costs).

## The other three perimeter events inside the window — the flag saw none of them

1. **Software Integrity Group sold 2024-09-30** to Clearlake/Francisco Partners funds:
   *"we derecognized net assets of $720.5 million … resulting in a pre-tax gain … of $860.5
   million."* Presented as **discontinued operations**, which is why **FY2022 and FY2023
   revenue were RESTATED downward** in later vintages — $5,081.5M → $4,615.7M and $5,842.6M
   → $5,318.0M (companyfacts, original vs latest filing). The eighteen-year series below
   therefore has **two perimeters inside it before Ansys is even counted**: SIG is *inside*
   the originally-filed FY2014–FY2023 income-statement figures and *outside* the restated
   ones. **OCF was never restated** — the cash-flow statement includes discontinued
   operations in every vintage — so the owner-earnings series is on one basis (SIG in through
   FY2024) and the revenue/margin series is on another. Recorded, and handled by using OCF
   as filed and reading the margin series only for direction.
2. **Processor IP business sold 2026-06-01 to GlobalFoundries** for $443.3M, pre-tax gain
   $425.4M, *"as part of our reallocation of resources to the highest growth opportunities
   in our Design IP segment"* — not discontinued operations.
3. **OpenLight** (a 75%-owned photonics venture, $90.0M in FY2022; $53.5M intangible
   impairment FY2024; divested 2024-12-30) — immaterial in dollars, recorded because it is
   the third exit in twenty months.

**Divestiture gains inside reported net income, and why owner earnings is immune:** FY2024
net income $2,235.8M includes the $860.5M SIG gain (via discontinued operations); FY2025
pretax $1,393.1M includes $548.9M of OSG gain and a $51.4M building gain inside *"Other
income (expense), net $924,944"* — **two-thirds of FY2025 pretax income is non-operating.**
9M FY2026 includes the $425.4M Processor IP gain. **Every one of these is backed out of
operating cash flow on the filed reconciliation** (*"Gain on divestitures, net of transaction
costs (508,044)"*; *"(380,527)"*), so the OCF-based construction is clean of them. This is
the reason the framework refuses the net-income proxy (operator rule 5), demonstrated.

## The filed pro forma — the AVGO shortcut, and what it says

Note 4, *"Supplemental Pro Forma Information (Unaudited)"*, verbatim: *"as if Ansys had been
acquired as of the beginning of fiscal year 2024."*

| combined perimeter, $ thousands | FY2025 | FY2024 |
|---|---|---|
| Pro forma total revenue | **8,920,890** | **8,450,296** |
| Pro forma net income | 743,822 | 651,499 |

- **On the combined perimeter, revenue grew 5.57% in FY2025.** The headline was +15%.
  Ansys contributed $756.6M in the 3.5 months it was owned; the MD&A's own decomposition is
  *"weakness in our business in China, which saw revenue decrease 22% compared to fiscal
  2024, excluding Ansys"* and a Design IP segment that fell 8.1%.
- **The pro forma net income is 8.3% of pro forma revenue** — after $1.6bn/yr of Ansys
  intangible amortisation and a full year of interest on $14bn of new debt. That is the
  accounting picture of the combined company, and it is why net income is the wrong
  numerator here and OCF is the right one.
- **The pro forma does NOT do the owner-earnings work for us** the way AVGO's did: it gives
  revenue and net income only — no pro forma OCF, SBC or capex. **The first full-perimeter
  owner-earnings observation is the trailing twelve months to 2026-07-31**, built from the
  10-K and the two 10-Q nine-month statements. It is one year, and [E2-23] requires a
  multi-year mean; how that is handled is the whole of Q4.

## Does the window mix two companies? YES — every historical window does

| period | perimeter | in the numerator (OCF) | in the denominator (cap) |
|---|---|---|---|
| FY2008–FY2023 | Synopsys incl. Software Integrity | yes | **no** (SIG sold) |
| FY2024 | Synopsys, SIG for 11 months, no Ansys | yes | **half** |
| FY2025 | Synopsys + **3.5 months** of Ansys, no SIG | partial | partial |
| **TTM to 2026-07-31** | Synopsys + Ansys, no SIG, no OSG, Processor IP for 7 months | **yes** | **yes** |

**Market cap $76.1bn prices the fourth row.** The screen's `oe_bottom 426 / oe_top 836` are
the first three rows — **a numerator that excludes a $35bn business the denominator
includes.** That is the HON finding in mirror image (HON's mean *included* a segment the
cap *excluded*), and it is the single most important fact about the screen row: **it is not
merely too narrow a spread; it is the wrong company.** The correction is worked at Q4.

---
# STAGE 0 (continued) — THE SCREEN ROW, REBUILT BY HAND

**Construction, as everywhere in this queue:** owner earnings = **OCF − SBC − capex** (one
end) and **OCF − SBC − D&A** (the other), $M, from `companyfacts` taking the originally
filed value at each fiscal-year end and flagging later restatements. OCF for FY2015–16 is
tagged only as `…ContinuingOperations` (identical in value where both exist) and is used.

| FY (Oct) | revenue* | GM%* | op inc* | op m%* | R&D%* | OCF | SBC | D&A | of which **dep'n** | capex | **OE (capex end)** | OE (D&A end) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2008 | 1,337.0 | 80.6 | 219.1 | 16.4 | 29.5 | 331.1 | 65.5 | 97.1 | — | 38.9 | **226.7** | 168.5 |
| 2009 | 1,360.0 | 79.9 | 208.3 | 15.3 | 30.9 | 239.2 | 56.9 | 101.5 | 48.3 | 39.2 | **143.0** | 80.8 |
| 2010 | 1,380.7 | 79.6 | 184.1 | 13.3 | 32.5 | 341.0 | 60.0 | 101.2 | 50.3 | 39.2 | **241.8** | 179.8 |
| 2011 | 1,535.6 | 77.8 | 212.8 | 13.9 | 32.0 | 440.3 | 56.4 | 128.6 | 51.0 | 57.3 | **326.6** | 255.4 |
| 2012 | 1,756.0 | 77.6 | 190.0 | 10.8 | 33.1 | 486.1 | 71.4 | 156.8 | 52.8 | 54.2 | **360.5** | 257.8 |
| 2013 | 1,962.2 | 76.9 | 246.5 | 12.6 | 34.1 | 496.7 | 67.5 | 187.4 | 56.7 | 65.5 | **363.7** | 241.8 |
| 2014 | 2,057.5 | 77.8 | 248.7 | 12.1 | 34.9 | 551.0 | 79.4 | 192.8 | 63.1 | 103.3 | **368.2** | 278.7 |
| 2015 | 2,242.2 | 76.9 | 266.5 | 11.9 | 34.6 | 495.2 | 86.4 | 211.8 | 71.1 | 87.0 | **321.8** | 196.9 |
| 2016 | 2,422.5 | 77.6 | 317.4 | 13.1 | 35.4 | 586.6 | 97.6 | 207.0 | 73.8 | 66.9 | **422.1** | 282.0 |
| 2017 | 2,724.9 | 76.0 | 347.6 | 12.8 | 33.4 | 632.5 | 108.3 | 189.4 | 82.8 | 70.3 | **453.9** | 334.7 |
| 2018 | 3,121.1 | 76.4 | 360.2 | 11.5 | 34.8 | 424.4 | 140.0 | 209.2 | 72.8 | 99.0 | **185.4** | 75.2 |
| 2019 | 3,360.7 | 77.6 | 520.2 | 15.5 | 33.8 | 800.5 | 155.0 | 201.7 | 100.4 | 198.1 | **447.4** | 443.8 |
| 2020 | 3,685.3 | 78.4 | 620.1 | 16.8 | 34.7 | 991.3 | 248.6 | 210.0 | 119.1 | 154.7 | **588.0** | 532.7 |
| 2021 | 4,204.2 | 79.5 | 734.8 | 17.5 | 35.8 | 1,492.6 | 345.3 | 203.7 | 119.1 | 93.8 | **1,053.6** | 943.7 |
| 2022 | 4,615.7 | 80.5 | 1,148.7 | 24.9 | 34.4 | 1,738.9 | 459.0 | 228.4 | 103.9 | 136.6 | **1,143.3** | 1,051.5 |
| 2023 | 5,318.0 | 80.6 | 1,273.2 | 23.9 | 34.8 | 1,703.3 | 563.3 | 247.1 | 141.4 | 189.6 | **950.4** | 892.9 |
| 2024 | 6,127.4 | 79.7 | 1,355.7 | 22.1 | 34.0 | 1,407.0 | 692.3 | 295.1 | 162.9 | 139.5 | **575.2** | 419.6 |
| 2025 | 7,054.2 | 77.0 | 914.9 | 13.0 | 35.1 | 1,518.6 | 893.3 | 660.4 | 171.9 | 169.5 | **455.9** | **−35.1** |
| **TTM to Jul-2026** | **9,416.5** | 72.8 | 802.4 | 8.5 | 30.5 | **2,938.3** | **950.0** | **1,811.1** | **~201** | **190.6** | **1,797.7** | **177.2** |

*\*Revenue, margins and R&D% are the LATEST-vintage (SIG-excluded) figures from FY2022 on and
originally-filed before; see the perimeter note. Depreciation is the filed "Depreciation
expenses were $171.9 million, $162.9 million and $141.4 million" line (Note 2) and its
predecessors; the FY2022–23 values were restated by $3.7M in later vintages and the latest
is shown. FY2024 capex was restated $123.2M → $139.5M in the FY2025 10-K (the SIG
reclassification); the latest is used, and `run.py` used the original — a live-path defect
recorded at the end. TTM = FY2025 + 9M FY2026 − 9M FY2025 from the two 10-Qs; TTM D&A
$1,811.1M of which acquired-intangible amortisation is $504.4 + $1,210.3 − $99.2 =
$1,615.5M, leaving tangible depreciation ~$196–201M.*

## THE SCREEN'S 96.3% SPREAD IS THE FOURTH SPREAD DEFECT AGAIN — and here it is the least of it

`oe_bottom 426` is the **3-year FY2023–25 mean at the D&A end**; `oe_top 836` is the **5-year
FY2021–25 mean at the capex end**. Both reproduce to the dollar (425.8; 835.7). Two windows,
two (c) ends, one number called a spread — the construction that misled on every name since
AAPL. Rebuilt over six windows and both ends, cap $76,112M:

| window | capex end | yield | D&A end | yield |
|---|---|---|---|---|
| 3-yr FY2023–25 | 660.5 | 0.87% | 425.8 | 0.56% |
| 5-yr FY2021–25 *(corpus default [E2-42])* | 835.7 | 1.10% | 654.5 | 0.86% |
| 8-yr FY2018–25 | 674.9 | 0.89% | 540.5 | 0.71% |
| 10-yr FY2016–25 | 627.5 | 0.82% | 494.1 | 0.65% |
| 15-yr FY2011–25 | 534.4 | 0.70% | 411.4 | 0.54% |
| 18-yr FY2008–25 | 479.3 | 0.63% | 366.7 | 0.48% |
| **TTM to 2026-07-31 — the only full-perimeter observation** | **1,797.7** | **2.36%** | 177.2 | 0.23% |

- **Historical width: $366.7M to $835.7M = 2.28x, a 127.9% spread.** The screen said 96.3%.
- **But the honest statement is that all twelve historical cells are the wrong perimeter**,
  and the first right-perimeter cell is **2.2x the top of the screen's band.** The
  screen's owner-earnings yield of 0.54–1.10% is a fact about Synopsys-without-Ansys priced
  as Synopsys-with-Ansys. Reported here as dollars and words, not as a manufactured ratio:
  *the pre-Ansys company earned roughly $0.45–0.85bn a year for its owners; the combined
  company earned $1.8bn in its first twelve months, before the restructuring is finished and
  with the D&A end invalid (Q4).*
- **The D&A end is INVALID for this filer, and the FY2025 row shows why in one cell: −$35M.**
  TTM D&A of $1,811M contains **$1,616M of purchase-accounting amortisation of Ansys and
  earlier intangibles** against **~$200M of depreciation of things that wear out**. Charging
  the amortisation as (c) would say the combined company needs $1.8bn a year of maintenance
  capex to stand still, when it spends $190M and its filed depreciation is $172M. The
  judgment is made at Q4 from the filed split, as the brief required; the arithmetic is
  shown here so the screen's `oe_bottom` is understood for what it is.

## [E4-41] — the level-shift disagreement, adjudicated

The row says the 9-year window finds *"no step"* (1.52 / 1.02) and the full 18-year finds
**2.30 STEP UP**. Both are right about their own windows and neither is describing a wave:
- FY2008–12 five-year mean (capex end) **$259.7M** → FY2014–18 **$350.3M** → FY2021–25
  **$835.7M**. Steps of 1.35x and 2.39x. **Revenue has risen in every one of the eighteen
  years** — through 2009 (+1.7%), 2019 (+7.7%) and 2023 (+15.2%), the three semiconductor
  downturns in the series — and the 10-K says so in its own words: *"We have consistently
  grown our revenue since 2005, despite periods of global economic uncertainty."*
- **This is the LRCX case in structure and its opposite in substance.** The nine-year base
  sits inside a long run, but the run is not a capex wave the customers might stop — it is
  twenty consecutive years of a ratably-recognised subscription growing at 9–10% a year with
  a **backlog of 1.1x revenue** in front of it. [E4-41] asks that *favourable exogenous
  breaks* be named and removed; the break that is exogenous and favourable is the AI-driven
  design-start boom of FY2021–25 (operating margin 17.5% → 24.9% in one year, FY2021→22),
  and it is named at Q4. The step in the *level* is mostly the business, and the
  normalisation at Q4 is made against the margin, not the revenue.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, without management's language.** A chip is described by
its designers as a few million lines of text. Turning that text into the physical arrangement
of several billion transistors that a foundry can actually print — deciding which gate goes
where, routing the wires between them, proving the signals arrive on time, proving the design
does what the text says before $50M of masks are cut — is done by software, and the software
is bought from three vendors. Synopsys is the largest of them. **It sells (1) that software,
on network licences that let a stated number of engineers run it for a stated term, usually
three years, paid ratably; (2) emulation and prototyping hardware** (ZeBu, HAPS) **that lets a
customer run the chip's software on the chip before the chip exists; (3) pre-designed circuit
blocks** (interface IP: PCIe, USB, DDR, Ethernet, and until June 2026 processor cores) **that a
chip designer licences rather than designs, paid up front plus per-unit royalties; and, since
July 2025, (4) Ansys's physics simulation** — structural, fluid, electromagnetic, thermal —
**sold to mechanical and electrical engineers in every industry that builds a physical
product.** The customer's alternative to (1) is not another vendor's tool in isolation; it is
re-qualifying its entire design flow, which every foundry's process design kit was
co-developed against, and re-training the engineers who script it.

Where the revenue comes from and where it goes, FY2025, as filed (Consolidated Statements of
Income; Note 5; Note 19):

| | $M | % |
|---|---|---|
| Time-based products (ratable licences) | 3,489.6 | 49 |
| Upfront products (IP, hardware, Ansys perpetual/lease) | 2,010.6 | 29 |
| Maintenance and service | 1,554.0 | 22 |
| **Total revenue** | **7,054.2** | 100 |
| by product group: **EDA 62.0% · Design IP 24.8% · Ansys 10.7% · Other 2.5%** | | |
| by segment: **Design Automation $5,302.3M (75%) · Design IP $1,751.8M (25%)** | | |
| Cost of revenue excl. amortisation | 1,311.7 | 18.6 |
| Amortisation of acquired intangibles (COGS + opex) | 504.4 | 7.2 |
| **Research and development** | **2,479.3** | **35.1** |
| Sales and marketing | 1,074.2 | 15.2 |
| General and administrative | 769.6 | 10.9 |
| Operating income (GAAP) | 914.9 | 13.0 |
| Segment adjusted operating income (before SBC, amortisation, deal items) | 2,632.9 | 37.3 |

**Two facts in that table govern the file.** First, **R&D is 35% of revenue and has been 29–36%
in every one of eighteen years** — the largest cost in the business is building next year's
tool, and it is expensed above the operating-cash-flow line, which is the (c) question at Q4.
Second, the gap between the segment measure (37.3%) and GAAP (13.0%) is **$893M of stock
compensation, $504M of amortisation and $255M of deal costs** — the segment measure is what
management is paid on (Q3) and it excludes the cost of paying management.

**The scarce input this business controls.** Three things, and they are of different kinds:
1. **Qualification against the foundry.** A new process node (TSMC N2, Samsung SF2, Intel
   18A) ships with a reference design flow the foundry built with Synopsys and Cadence over
   two to three years; the process design kit is certified against specific tool versions. A
   designer who wants to tape out at that node runs a certified flow or accepts the risk of
   silicon that does not work. This is the input a new entrant cannot buy.
2. **The engineers.** *"approximately 28,000 employees … Approximately 75% of our employees
   are engineers, and over half hold Master's or PhD degrees."* The algorithms are decades of
   accumulated heuristics for problems that are formally intractable (placement, routing,
   timing closure are NP-hard); the accumulation is the asset.
3. **The customer's own flow.** Every large customer has years of scripts, methodologies and
   sign-off criteria written against Synopsys's tool interfaces. That artifact is the
   customer's, but it runs only on Synopsys's runtime — the CRM structure.

**Will the fundamentals look broadly the same in ten years?** For the **EDA and IP three
quarters**, yes: as long as chips are designed they must be synthesised, placed, routed,
timed and verified, and the ratable model means *"decreases as well as increases in customer
spending do not immediately affect our revenue in a significant way"* (MD&A). The *level* has
an AI-design-start tailwind in it that is named at Q4. For the **Ansys quarter**, the
mechanism (physics simulation sold to engineers) is fifty years old and durable; **what is
new is Synopsys owning it**, and whether the *"integrated design and simulation tools across
various industries"* rationale in Note 4 is real or is the [E3-40] loss-of-focus case is a
Q3 question, not a Q1 one. The China exposure — 11.5% of FY2025 revenue, down from 16.1%,
with a BIS licence requirement imposed 2025-05-29 and rescinded 2025-07-02 — is a Q2/Q4
question.

**Is the business "relatively simple and stable in character" [E3-31]?** Simple in mechanism,
legible in the filings (two segments with adjusted margins, a product-group split, a
geographic split, a backlog with its twelve-month conversion rate, a filed depreciation-vs-
amortisation split), and stable in the filed record — eighteen years without a revenue
decline. **What is not simple is the perimeter**, and that is handled above rather than left
to contaminate Q4. The Ansys merger makes this two businesses with different customers,
different sales motions and different competitors; both are individually understandable and
both are disclosed. The INTC and QCOM precedents are the warning: a semiconductor name can be
perfectly understandable and still fail Q2 on its own filed product split — and this filer's
product split has a segment whose adjusted operating income fell 43% in FY2025. Q2 is decided
on the row.

- **VERDICT: [x] IN**

*Recorded against myself under operator rule 9: the brief's prior is that this is "possibly
the widest moat in the queue," and the Q1 pass rests on legibility, not on quality. The
facts that most threaten the brief's prior are already visible at Q1 and are carried into
Q2 rather than softened: Design IP's adjusted operating income fell from $730M to $419M in
one year; the 10-K names no competitor at all; China revenue fell 22% ex-Ansys; and the
newly-hired Chief Revenue Officer was, until November 2025, the CEO of Siemens EDA — the
third firm in the "three-firm industry."*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The brief's claim, framed to be refuted [E4-26]: a three-firm industry whose tools are
qualified into process nodes, with switching costs that "look enormous" — "IN, possibly the
widest moat in the queue." The brief's own instruments: gross margin and pricing through any
revenue decline, the filed backlog, any unit/seat/price series, the Cadence row, and the IP
split. All five are run. The verdict is IN, NARROW — and the brief's "widest in the queue"
is refuted on the row, by the subject's own segment note, and by the absence of a unit
series.**

### The three criteria [E3-03], from the subject's own filings

- **(1) Needed or desired — YES.** No chip reaches a foundry without synthesis, place-and-
  route, timing sign-off and verification; the 10-K's own phrase is *"the mission-critical
  EDA solutions that engineers use to design and test integrated circuits."*
- **(2) No close substitute — CANNOT BE EVIDENCED FROM THIS FILER, and that is a finding.**
  *Recorded sweep of the FY2025 10-K and the Q3 FY2026 10-Q: **no instance found** of a
  competitor named by name.* The competition paragraph, verbatim: *"We compete with a
  variety of different EDA vendors, including publicly traded companies offering varying
  ranges of products and services as well as other EDA vendors that offer products focused on
  one or more discrete phases of the IC design process. Additionally, some of our customers
  internally develop design tools and capabilities that compete with our products. For our
  Ansys S&A software solutions, our competitors include publicly traded companies, small,
  geographically-focused firms, startups, and solutions produced in-house by the end users."*
  And for the quarter of the company that is IP: *"In our Design IP segment, we compete
  against silicon IP providers **as well as our customers' internally developed IP.**"* **The
  only competitor Synopsys names in its own filing is the customer.** "Cadence" appears in the
  10-K once — in the new Chief Revenue Officer's biography (*"started his career in sales at
  Cadence Design Systems in 1997"*; *"Chief Executive Officer of Siemens EDA … from June 2024
  to November 2025"*). Criterion (2) is decided on the row.
- **(3) Not price-regulated — passes on price; the KLAC inversion applies on the buyer.**
  Nobody caps Synopsys's prices. What the US government regulates is **who may buy**, and it
  exercised that power inside the window: *"on May 29, 2025, Synopsys received a so-called
  'is-informed' letter from the BIS imposing a license requirement for the export, reexport,
  or in-country transfer of EDA software and technology … when a party to the transaction is
  located in China … The Q3 2025 BIS Restrictions were subsequently rescinded on July 2,
  2025."* Thirty-four days, and China revenue fell *"22% compared to fiscal 2024, excluding
  Ansys."* **[E2-59]: the regime that moves the boundary is not the company's moat, in either
  direction.** The 10-K names the second-order effect too: *"policies regarding technology
  independence may lead to non-U.S. customers favoring their domestic technology solutions."*

### [E2-44], both halves, on the subject's own numbers

**(a) Can it raise prices when demand is flat?** No price series exists (sweep below), so the
instrument is margin through a revenue decline — and **Synopsys has never filed one.**
Eighteen consecutive years of growth; the 10-K's sentence: *"We have consistently grown our
revenue since 2005, despite periods of global economic uncertainty."*

| downturn year | revenue | YoY | gross margin | operating margin | backlog at year-end |
|---|---|---|---|---|---|
| FY2009 | $1,360.0M | **+1.7%** | 79.9% | 15.3% | not filed (pre-ASC 606) |
| FY2019 | $3,360.7M | **+7.7%** | 77.6% | 15.5% | **$4.4bn**, up from $4.0bn |
| FY2023 | $5,318.0M | **+15.2%** | 80.6% | 23.9% | *(FY2023 vintage not pulled)* |

The honest reading is **not** that the company held price through a downturn; it is that a
**three-year ratable licence with a backlog of 1.1–1.4x revenue never shows a downturn in the
revenue line** — the MD&A: *"decreases as well as increases in customer spending do not
immediately affect our revenue in a significant way."* The test therefore moves to the
**segment** level, where a decline did occur:

| Design IP segment (Note 19; 10-Q Note 17) | FY2023 | FY2024 | **FY2025** | 9M FY2025 | **9M FY2026** |
|---|---|---|---|---|---|
| revenue | $1,542.7M | $1,906.3M | **$1,751.8M (−8.1%)** | $1,344.7M | **$1,335.0M (−0.7%)** |
| adjusted operating income | $514.1M | $730.2M | **$419.3M (−42.6%)** | $363.1M | **$302.2M (−16.8%)** |
| **adjusted operating margin** | 33% | 38% | **24%** | 27% | **23%** |

**When Design IP's revenue fell 8%, its operating income fell 43% and its margin fell fourteen
points.** That is the no-moat signature, in a quarter of the pre-Ansys company. The MD&A's
three filed causes: *"China export control restrictions … weaker than expected demand from a
major foundry customer, and certain roadmap and resource decisions that did not yield their
intended results."* The third is not the regime; it is execution. **The AMAT lesson the brief
anticipated is confirmed: the product split kills the claim the consolidated line supported.**
Design Automation, on the same measure, went 37% → 39% → 42% → **45%** (9M FY2026).

**(b) Can it grow dollar volume with only minor additional capital?** Yes: capex **2.4% of
revenue** (FY2025), 2.0% TTM; net PP&E $749.6M against $9.4bn of TTM revenue; $2.7bn of
customer-funded deferred revenue. The capital this business consumes is R&D at 35% of
revenue, expensed — and acquisitions.

### The backlog — the instrument the brief asked for, and what it shows

| as of | backlog | of which FSA | 12-month conversion | backlog ÷ revenue |
|---|---|---|---|---|
| 2018-10-31 | $4.0bn | — | *"three years of committed orders"* | 1.28x |
| 2019-10-31 | $4.4bn | $0.49bn | 56% | 1.31x |
| 2022-10-31 | $7.1bn | $1.1bn | 44% | 1.40x (SIG basis) |
| 2024-10-31 | $8.1bn | $1.2bn | *(not restated in the FY2025 vintage)* | 1.32x |
| 2025-10-31 | **$11.4bn** | $2.0bn | 45% | 1.62x (3.5 months of Ansys) |
| **2026-07-31** | **$10.9bn** | $1.9bn | 49% | **1.16x** (TTM, full Ansys) |

- Real, filed, 2.7x in eight years; it is why no downturn shows in revenue.
- **Two things cut the other way.** **$1.9–2.0bn of it is FSA** — *"non-cancellable Flexible
  Spending Account commitments … where actual product selection and quantities of specific
  products or services are to be determined by customers at a later date"* — a pre-purchased
  budget, not an order for a named tool; the company excludes it from its own conversion
  percentage. And **the backlog FELL $0.5bn in the nine months of FY2026 while $7.16bn of
  revenue was recognised** — bookings of roughly $6.7bn against $7.2bn of revenue in the first
  three quarters of full Ansys ownership. Part is the Processor IP sale; the FY2022 vintage's
  own caveat applies (*"will fluctuate period to period"*). **Carried as a Q6 monitoring
  item, stated now so it cannot be quietly dropped.**
- Management measures itself on it: the 2026 proxy's revenue-growth goal is *"Fiscal 2026
  Revenue Backlog"* ($4.65bn target; 100.5% achieved) — the [E2-49] pre-set-bullseye form.

### [E4-55] — WHERE UNITS EXIST, MONITOR UNITS. HERE THEY DO NOT EXIST.

*Recorded sweep of the FY2025 10-K for: "average selling price", "ASP", "seats", "seat ",
"number of licenses", "number of users", "units shipped", "units sold", "price increase",
"list price", "renewal rate", "attach rate", "number of customers", "installed base", "design
starts" (as a count), "tape-out", "chips shipped".* **No instance found of any unit, seat,
licence-count, price or renewal series.** *"seats"* appears once — as the basis on which the
CODM allocates revenue to geographies (*"the CODM considers where individual 'seats' or
licenses to our products are located"*) — **so the company counts seats internally and files
none of them.** *"design starts"* appears four times, never as a number. The only physical
series in the filing is headcount (~28,000). **Fifth consecutive run in this queue with no
unit series; the absence caps the class at NARROW for the same reason as the other four —
revenue growth cannot be decomposed into price and volume from any filed document.**
*(Cadence's FY2025 10-K, swept on the same patterns by the row: no instance found either. Of
the eight peers priced, only CEVA files a unit series — 2.1 billion devices in 2025.)*

### [E4-04] — must the moat be continuously rebuilt?

R&D at **35% of revenue, $2.48bn, never below 29% in eighteen years** — and Cadence's is
33.4%: a third of revenue is the price of admission to this industry. Defence of the same
advantage, or purchase of its replacement? **Defence, with a filed caveat.** The franchise
defended — the synthesis/place-and-route/verification flow qualified against every foundry's
process design kit, and the customer's scripts written against it — is the same franchise at
2nm as at 28nm; a lapse narrows the lead at the next node without dissolving the installed
flow. That is [E5-23]'s *"defending your own moat all of the time,"* not [E4-04]'s replaced
basis. **The caveat is the registrant's own:** *"The adoption of AI technologies has brought
new demands and also challenges in terms of disruption to both our business models and
existing technology offerings"* (10-Q, Item 1A). A management that files "disruption to our
business models" is describing the replacement case as a possibility; it has not happened on
the record, and it is a Q6 item.

**Key-person dependence [E4-23] — tested, not found.** The founder-CEO of thirty years
stepped down 2024-01-01; revenue grew 15% and 15% in the two years after. The moat did not go
with the surgeon. *(The Design IP miss and the September 2025 guidance cut happened under the
successor; they are Q3 facts.)*

### China and customer concentration — the two edges, quantified

| FY | China revenue | % of revenue | one-customer concentration |
|---|---|---|---|
| 2017 | — | — | **17.9%** |
| 2018 | — | — | 15.4% |
| 2019 | — | — | 12.8% |
| 2020 | $420.8M | 11.4% | 12.4% |
| 2021 | $562.7M | 13.4% | 10.6% |
| 2022 | $795.4M | 15.7% | 11.7% |
| 2023 | $855.0M | 16.1% | 13.5% |
| 2024 | $989.5M | 16.1% | 12.6% |
| **2025** | **$814.3M** | **11.5%** | **below 10%, not disclosed** |
| 9M FY2026 | $707.0M | 9.9% | — |

- China: 16.1% → 11.5% in one year, −17.7% in dollars (−22% ex-Ansys). Cadence's China
  revenue fell 15.7% in FY2024 and recovered 18.7% in FY2025 to its FY2023 level; Synopsys's
  has not recovered. The 9M FY2026 dollar rise is Ansys's China arriving.
- The one-customer concentration has fallen from 17.9% to under 10% — and the FY2025
  *"weaker than expected demand from a major foundry customer"* is that customer falling below
  the disclosure line. A concentration that falls because the customer's demand fell is not
  diversification.

### THE COMPETITOR ROW — required [E3-28]

**Identical formula for every filer: gross margin = (revenue − cost of revenue) ÷ revenue as
filed; operating margin = filed income from operations ÷ revenue; ROUNTOA = operating income
÷ (total assets − goodwill − intangibles − non-interest-bearing current liabilities), year-end
denominators — a CONVENTION of this row, [E2-43] in the closest computable form.** Latest full
fiscal year each; Ansys is its last standalone year. Sources: `_research 2026-09-07
SNPS/ROW_CDNS_ANSS.md` and `ROW_IP_CAE_PEERS.md`, every figure filing-sourced.

| | **SNPS FY2025** | **SNPS pre-Ansys FY2024** | **CDNS FY2025** | **ANSS FY2024** | ARM FY26 (Mar) | RMBS FY25 | CEVA FY25 | KEYS FY25 (Oct) | PTC FY25 (Sep) | ADSK FY26 (Jan) |
|---|---|---|---|---|---|---|---|---|---|---|
| form · accession | 10-K `0000883241-25-000028` | 10-K `0000883241-24-000024` | 10-K `0000813672-26-000016` | 10-K `0001013462-25-000009` | 20-F `0001973239-26-000097` | 10-K `0001193125-26-057101` | 10-K `0001437749-26-006091` | 10-K `0001601046-25-000127` | 10-K `0001193125-25-291326` | 10-K `0000769397-26-000015` |
| revenue $M | 7,054.2 | 6,127.4 | 5,296.8 | 2,544.8 | 4,920 | 707.6 | 109.6 | 5,375 | 2,739.2 | 7,206 |
| **gross margin** | **77.0%** (81.4% ex-amort.) | 79.7% (81.5% ex-amort.) | **86.4%** (87.6% ex-amort.) | **89.0%** | 97.5% | 79.6% | 87.1% | 62.1% | 83.8% | 91.0% |
| R&D % revenue | **35.1%** | 34.0% | 33.4% | 20.7% | 56.4% | 26.5% | 68.3% | 18.7% | 16.7% | 22.8% |
| SBC % revenue | **12.7%** | 11.3% | 8.6% | 10.6% | 21.4% | 7.7% | 18.1% | 3.0% | 7.9% | 10.9% |
| **operating margin (GAAP)** | **13.0%** | 22.1% | **28.2%** (30.6% ex the $128.5M BIS/DOJ loss) | **28.2%** | 18.3% | 36.8% | (10.4%) | 16.3% | 35.9% | 21.9% |
| **ROUNTOA** | 18.5% | 20.0% | **29.5%** (32.1% ex BIS loss) | 27.4% | 11.5% | 23.4% | (3.8%) | 18.5% | 90.4% | 83.2% |
| goodwill + intangibles $M | 39,578.8 | 3,644.0 | 3,467.3 | 4,494.4 | — | — | — | — | — | — |
| backlog / RPO ÷ revenue | 1.62x | 1.32x | **1.47x** | 0.68x | — | — | — | — | ARR $2.48bn | recurring 97% |
| customer >10% | none (was 12.6%) | 12.6% | **none** | none >5% | — | — | — | — | — | — |
| names Synopsys as competitor | — | — | **yes** | no (peer group only) | no | **yes** (Silicon IP) | indirectly | no | no | no |

*SNPS ROUNTOA: FY2025 $914.9M ÷ ($48,224.5M − $26,899.2M − $12,679.6M − $3,700.4M) = 18.5%;
FY2024 $1,355.7M ÷ ($13,073.6M − $3,448.8M − $195.2M − $2,650.1M) = 20.0%; on the TTM
perimeter at 2026-07-31, GAAP operating income $802.4M ÷ $5,483.2M = **14.6%**, and on owner
earnings $1,797.7M ÷ $5,483.2M = 32.8%. Cadence's cash ($3.0bn) sits inside its denominator as
Synopsys's ($3.6bn) does; ex-cash Cadence is 72.8%. ARM, CEVA, Rambus are the IP-segment
comparators; Keysight, PTC and Autodesk the Ansys-segment comparators; KEYS bought Synopsys's
OSG for $581M in October 2025.*

**GROSS AND OPERATING MARGIN, TEN YEARS, THE TWO EDA FILERS — the [E2-44] test run across the
pair:**

| FY | SNPS GM | **CDNS GM** | SNPS op m | **CDNS op m** | SNPS China % | CDNS China % |
|---|---|---|---|---|---|---|
| 2016 | 77.6 | **85.9** | 13.1 | **13.5** | — | — |
| 2017 | 76.0 | **87.8** | 12.8 | **16.7** | — | — |
| 2018 | 76.4 | **87.9** | 11.5 | **18.5** | — | — |
| **2019 ↓** | 77.6 | **88.6** | 15.5 | **21.1** | — | — |
| 2020 | 78.4 | **88.6** | 16.8 | **24.1** | 11.4 | — |
| 2021 | 79.5 | **89.7** | 17.5 | **26.1** | 13.4 | — |
| 2022 | 80.5 | **89.6** | 24.9 | **30.1** | 15.7 | — |
| **2023 ↓** | 80.6 | **89.4** | 23.9 | **30.6** | 16.1 | 17 |
| 2024 | 79.7 | **86.0** | 22.1 | **29.1** | 16.1 | 12 |
| 2025 | 77.0 | **86.4** | 13.0 | **28.2** | 11.5 | 13 |

**The row's finding, and it runs AGAINST the subject exactly as the brief feared:**
1. **Cadence has earned the higher gross margin AND the higher operating margin in every one
   of the ten years, without exception**, by 6–12 points on gross margin and by 3–15 points on
   operating margin. Cadence's revenue also rose in every year of the series. **[E2-58] runs
   against Synopsys in relative terms: on the same business, over a decade, the smaller
   competitor earns more per dollar.** This is the Keyence-against-Cognex structure the brief
   named, with one difference of degree: Cognex's margins were commodity-like in absolute
   terms, and Synopsys's are not — an 80% gross margin and a 45% Design Automation segment
   margin are franchise economics. **Synopsys is the larger, lower-margin member of a
   two-firm-plus-one industry; it is not the dominant-class member.**
2. **Where the gap comes from is filed.** Three things: (a) **stock compensation, 12.7% of
   revenue against Cadence's 8.6%** — Synopsys pays half again as much stock per revenue
   dollar, which is a real economic cost [E5-06] and one that non-GAAP reporting removes
   (Q3); (b) **the IP and hardware mix** — Design IP earns 23–38% against Design Automation's
   45%, and Synopsys carries $600M of low-margin *"professional service and other"* revenue
   against $444.5M of cost of maintenance and service; (c) **acquired-intangible amortisation**,
   $504M in FY2025 against Cadence's $105M. Strip (c) from both and the gross-margin gap is
   still six points. **On the Design Automation segment alone — 45% adjusted — Synopsys
   out-earns Cadence's whole-company adjusted margin (41.7% on the same add-backs).** The
   franchise is in that segment; the rest of the company dilutes it.
3. **[E2-45] — the attacker's test, run by the actual attacker and filed.** Cadence's Item 1,
   verbatim: *"Key competitors include Synopsys, Inc., Ansys, Inc. (acquired by Synopsys),
   Siemens EDA, and a variety of other tool providers … U.S.-based competitors include
   Keysight Technologies, Inc., Schrödinger, Inc., and CEVA, Inc., while international
   competitors include Altium Limited (acquired by Renesas Electronics Corporation) and
   Zuken, Inc. (Japan) and **emerging players in China such as Huada Empyrean, Xpeedic
   Technology, X-EPIC, Primarius Technologies, Univista, and Giga Design Automation.**"* The
   industry structure the brief asserted is confirmed **from the competitor's filing, not the
   subject's**: three full-flow vendors and six named Chinese entrants. And Cadence's risk
   factor names the mechanism: *"Entity List restrictions and other trade restrictions may
   also encourage customers to seek substitute products from our competitors, including a
   growing class of foreign competitors and open source alternatives … China's stated national
   policy to be a global leader in all segments of the semiconductor industry by 2030 has
   resulted in and may continue to cause increased competitive capability in China."*
4. **Ansys's own filing names no competitor and files no product line**: *"it is impracticable
   for us to provide accurate historical or current reporting among our various product
   lines"* (FY2024 10-K, Note 1). Its record is a franchise's — gross margin 85–89% for nine
   years, operating margin 27–38%, ACV +11–13% a year, no customer above 5%, 85% of ACV
   recurring — but **its principal competitors (Siemens Simcenter, Dassault SIMULIA,
   Hexagon/MSC, Altair now inside Siemens) are all non-SEC filers**, and PTC/Autodesk are
   CAD/PLM adjacents, not simulation rivals. **The Ansys quarter's moat cannot be evidenced
   from a same-formula row on this framework's ladder.**
5. **Peers taken: 9, against the industry's real count of roughly a dozen.** Filed
   same-formula figures for **8 registrants** (SNPS, CDNS, ANSS standalone, ARM, RMBS, CEVA,
   KEYS, PTC, ADSK). **The row's limit, stated: Siemens AG deregistered from the SEC on
   2014-05-16 (Form 15F-12B, accession `0001193125-14-202195`; last 20-F 2013-11-27), so
   Siemens EDA — the third full-flow EDA vendor and the owner of Simcenter and Altair — cannot
   be priced on any SEC rung; Dassault Systèmes and Hexagon likewise.** Adjudicated under the
   ACLS/KLAC rule: an additional competitor can only narrow a moat, never widen one; the gap
   caps the class at NARROW rather than suspending it, and becomes a Q6 work-order.
6. **[E3-61] limit:** the row shows position, not conduct. On conduct the filed record is
   Cadence's — a guilty plea to *"one count of conspiracy to commit export controls
   violations"* for 2015–2021 sales to a Chinese customer, $140.6M of penalties, a three-year
   probation — and Synopsys's *"administrative subpoenas from BIS requesting production of
   information and documentation relating to transactions with certain Chinese entities"*,
   disclosed without a finding. Both are read at Q3.

### The claims NOT made, each refused with its reason

- **[E2-53] dominance class — REFUSED.** *"Good or bad, it will prosper"* does not describe a
  company whose IP segment lost 43% of its operating income in a year the industry grew, or
  whose smaller rival has out-earned it for ten years. Position sets the floor here; execution
  sets the level.
- **[E3-33]/[E5-28] untapped pricing power — NOT CLAIMED.** Claiming it claims near-monopoly;
  the industry is a duopoly-plus-one with six named Chinese entrants, and the Design IP
  margin collapse is affirmative evidence against unused pricing power in a quarter of the
  business. The EDA three-quarters may have it; no filed instrument can show it.
- **[E4-36] which of the four causes?** An extreme max on two variables — the foundry-qualified
  flow and the engineers — riding the AI-driven design-start wave (operating margin 17.5% →
  24.9% in FY2021→22). The structure is ownable and predates the wave; the level of FY2022–25
  is partly the wave, and Q4 normalises for it.

- Class: [ ] WIDE  **[x] NARROW**  [ ] NONE  [ ] PROVISIONAL · **Direction: WIDENING in Design
  Automation (segment margin 37% → 45% in three years, backlog 2.7x in eight); NARROWING in
  Design IP (margin 38% → 23%, Processor IP exited, customers building the substitute) and at
  the China edge (16.1% → 11.5% in a year, with six named domestic entrants); UNPROVEN for the
  Ansys quarter on this ladder.**
- **VERDICT: [x] IN — NARROW.** *The strongest fact against this verdict, stated per [E4-51]
  so a bear would accept it as fairly put: **the only competitor with filed numbers has earned
  a higher gross margin and a higher operating margin than Synopsys in every one of the last
  ten years, and a quarter of the pre-Ansys company — Design IP — competes, in the filer's own
  words, against its customers' internally developed IP and lost fourteen points of margin on
  an eight-percent revenue decline.** Held IN on the Design Automation segment: an 80%+ gross
  margin and a 45% segment margin held through eighteen years without a revenue decline, a
  backlog of 1.2–1.6x revenue, the customer's own flow written against the tool, and an
  industry structure confirmed by the attacker's filing as three full-flow vendors. NARROW,
  not WIDE, for three filed reasons: Cadence out-earns it, the IP quarter is not a franchise,
  and there is no unit series with which to test any of it.*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**The brief's instruction — pull the 8-K EX-99.1 before scoring [E4-29] and [E4-22]'s third
flag — was followed for eight consecutive releases (2024-12-04 `0001193125-24-270723` ·
2025-02-26 `-25-036798` · 2025-05-28 `-25-129525` · 2025-09-09 `-25-199178` · 2025-12-10
`-25-314200` · 2026-02-25 `-26-071601` · 2026-05-27 `-26-241911` · 2026-08-26 `-26-368620`),
and the 2026 proxy (`0000883241-26-000007`).**

**STEP 1 — THE WEIGHT CASE, DECLARED.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution [E3-38]** — NOT ticked. [E3-38]'s root class is the undifferentiated
  product whose *"only products are promises"* [E2-70]. An 80% gross margin, a three-year
  ratable licence and a 1.2x backlog are the opposite; Q2 found a franchise in Design
  Automation, and by [E3-43] a franchise tolerates some mis-management. **But the finding is
  narrower than KLA's**: a quarter of the company (Design IP) *was* mis-managed in FY2025 by
  the filer's own admission and lost 43% of its operating income, so the tolerance is real
  and finite, and the Ansys integration is a daily-execution task for the next two years.
- [ ] **Control [E1-16]** — NOT ticked. Liquid public minority stake.
- [ ] **Leverage [E3-29]** — NOT ticked, and the numbers are given so the call can be
  attacked: **$9.9bn of Senior Notes** (fixed 4.55%–5.70%; $1.0bn due April 2027, $1.0bn
  April 2028, $8.0bn 2030–2055) against **$3.6bn of cash** and **$1.8bn of TTM owner
  earnings**: net debt 3.5x owner earnings, gross 5.5x. TTM interest expense **$624.0M**
  ($446.7M + $429.3M − $252.0M) is covered **5.4x** by pre-interest cash flow net of capex
  ([E2-54] form, Q4). Book equity of $31.2bn is $38.3bn of goodwill and intangibles; **tangible
  equity is −$7.1bn**. That is a purchase-accounting fact, not a solvency one — a goodwill
  impairment destroys no cash flow — but it is stated because *"small asset errors destroy
  equity"* is literally true here: a 19% write-down of goodwill would zero the book. Not a
  gate; recorded.

**NONE TICKED → Q3 IS A QUALITATIVE OVERLAY.** Findings are recorded; manager quality alone
does not stop this run and cannot promote it.

**Honesty — binary, permanent, filings-based [E5-16], each matter dated to when it became
PUBLIC.** *"understanding about business mistakes; tolerance for personal misconduct is zero."*
- **THE DESIGN IP SECURITIES LITIGATION — recorded in full, dated, and weighed as what it is:
  an allegation.** Public **2025-10-31** (*Kim v. Synopsys*, N.D. Cal. 25-cv-09410); a second
  class action 2025-11-25 (*New England Teamsters*), adding Securities Act claims *"on behalf
  of stockholders who received our stock in exchange for their shares of common stock of Ansys"*;
  a third 2025-12-30; three derivative suits 2025-12-22, 2026-02-24, 2026-03-05 against
  named directors and officers for *"breach of fiduciary duty … gross mismanagement, waste of
  corporate assets, unjust enrichment."* All allege *"certain material misstatements or
  omissions related to the performance of our Design IP segment."* Consolidated as *In re
  Synopsys, Inc. Securities Litigation*; **consolidated complaint due 2026-09-23, response
  due 2026-11-04.** No accrual; *"We believe these claims are without merit."* **How it is
  weighed:** [E5-16] refuses integrity failures *found*; a securities class action filed
  after a guidance cut is a source to read, not a finding, and the framework says so (*"a
  source to read, not the primary checklist"*). What the filed record shows about the
  underlying conduct is below at the projections flag — and it cuts both ways. **Not carried
  as a disqualifier; carried as the first Q6 date.**
- **BIS administrative subpoenas** — 10-K Item 1A: *"we have received administrative subpoenas
  from BIS requesting production of information and documentation relating to transactions
  with certain Chinese entities."* Disclosed, undated in the filing, no finding, no accrual.
  **Read against the competitor's record:** Cadence pleaded guilty in July 2025 to one count
  of conspiracy to commit export-control violations for 2015–2021 sales to a Chinese customer
  and paid $140.6M. That is the conduct class the regime polices in this industry; Synopsys
  has a subpoena and no charge. Recorded; not a disqualifier; a Q6 watch.
- **No self-dealing found.** No related-party transactions above the disclosure threshold in
  the proxy; hedging and pledging prohibited; say-on-pay **~91%** on the FY2024 program.

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30].** *Each a prompt to READ, never a verdict.
The list is open.*
- [ ] **weak accounting** — not found. SBC expensed; deal costs expensed as incurred
  (*"Transaction costs … $267.1 million … were expensed as incurred"*); no material DB
  pension; contract liabilities on Ansys measured under ASC 606 as if originated, so **no
  deferred-revenue haircut inflates post-close growth**; KPMG's successor audit unqualified.
- [ ] **unintelligible footnotes** — not found; the opposite. Note 4 prints the consideration
  split cash/stock/awards to the thousand, the share count and price used, the intangible
  fair values by class with lives and methods; Note 19 prints the segment reconciliation
  with SBC, amortisation, restructuring and deal items each on its own line; Note 6 prints the
  amortisation schedule five years forward. **This filer's footnotes are among the most
  legible in the queue** — which is exactly why the perimeter could be established at all.
- [x] **TRUMPETED EARNINGS PROJECTIONS — FIRES, AND THE RECORD INCLUDES ONE LARGE MISS.**
  Formal quarterly and annual guidance on revenue, GAAP and non-GAAP expenses, non-GAAP tax
  rate, GAAP and non-GAAP EPS, operating cash flow and free cash flow, every quarter.
  **[E3-48] requires the record be set against outturn, and it was, for eight quarters, from
  the releases themselves:**

  | quarter | guided (prior release) revenue | actual | vs midpoint | guided non-GAAP EPS | actual | vs midpoint |
  |---|---|---|---|---|---|---|
  | Q1 FY25 | $1,435–1,465M | $1,455M | +0.3% | $2.77–2.82 | $3.03 | **+8.4%** |
  | Q2 FY25 | $1,585–1,615M | $1,604M | +0.3% | $3.37–3.42 | $3.67 | **+8.1%** |
  | **Q3 FY25** | **$1,755–1,785M** | **$1,740M** | **−1.7%, below the range** | **$3.82–3.87** | **$3.39** | **−11.8%, below the range** |
  | Q4 FY25 | $2,230–2,260M | $2,255M | +0.4% | $2.76–2.80 | $2.90 | +4.3% |
  | Q1 FY26 | $2,365–2,415M | $2,409M | +0.8% | $3.52–3.58 | $3.77 | +6.2% |
  | Q2 FY26 | $2,225–2,275M | $2,276M | +1.2%, above the range | $3.11–3.17 | $3.35 | +6.7% |
  | Q3 FY26 | $2,410–2,460M | $2,477M | +1.7%, above the range | $3.63–3.69 | $3.91 | +6.8% |
  | Q4 FY26 | $2,530–2,580M | — | | $4.10–4.16 | — | |

  **And the full-year FY2025 record, which is the one that matters:** guided **$6,745–6,805M**
  in December 2024; *"Reaffirming full-year 2025 guidance"* in February; *"reaffirming our
  full-year revenue and operating margin guidance"* on **2025-05-28, one day before the BIS
  letter of 2025-05-29**; non-GAAP EPS guidance *raised* to $15.11–15.19 in May; then on
  **2025-09-09: *"Expecting full-year 2025 revenue between $7.03 and $7.06 billion"* —
  which INCLUDES ~$757M of Ansys, so the organic number was cut to ~$6.27–6.30bn, a $500M
  (7.3%) reduction to a figure reaffirmed fourteen weeks earlier — and non-GAAP EPS cut to
  $12.76–12.80 from $15.11–15.19.** The three causes were named in that release and the 10-K
  (China restrictions; a major foundry customer; *"roadmap and resource decisions that did not
  yield their intended results"*). **Seven of eight quarters beat the midpoint; the eighth
  missed the bottom of the range on both lines, and it was the quarter the annual number was
  cut by half a billion dollars.** [E5-30]'s ratchet is visible in the pattern (the seven
  beats average +6.2% on EPS on a ±1% band, which is a midpoint set to be beaten), and the
  one miss is what the class action is about. **On [E2-26]'s half-owner test the September
  release passes** — it named its own execution failure in plain words rather than
  "except-for"-ing it — and on [E5-30]'s it is the demonstration: a guidance culture that
  raised its EPS target in May and cut it 16% in September.
- [x] **serial share issuance [E5-15] — FIRES, in a form the flag's author would recognise.**
  Shares outstanding **149.3M (Dec 2010) → 154.6M (Dec 2024)**: fifteen years flat, during
  which the company spent **$6.1bn on repurchases** (FY2008–23, at implied prices from $22 to
  $388) and retired **not one net share** — every dollar bought back the stock that
  compensation issued. Then in nine months: **+30.0M shares to Ansys holders at $571.20**,
  **+4.8M to NVIDIA at $414.79**, and **a $250M ASR at $442.69 plus $50M at $394.78** — the
  company **sold stock at $415 in December and bought it at $443 in March**. [E5-24]'s first
  law — *"what is smart at one price is dumb at another"* — applied within one fiscal year
  in the wrong order. **[E5-44] on the Ansys paper, worked:** the 30.0M shares were issued
  at a quote of $571.20 ($17.1bn); at this file's own zero-growth value range (Q5:
  roughly $70–175 a share, judged ~$145), the intrinsic value given was **~$2–5bn, not
  $17bn** — so on the corpus's own measure Synopsys paid Ansys's owners **~$20–23bn of value
  for a business earning $0.75bn of owner cash flow**, not $35bn. A premium paid in
  *overvalued* shares is smaller than it looks; that is the one respect in which the deal's
  structure favoured Synopsys's continuing owners, and it is stated as such.
- [ ] **EBITDA / adjusted-earnings promotion [E4-29]** — **the EBITDA form does NOT fire**:
  *recorded sweep, zero occurrences of "EBITDA" in the FY2025 10-K, the Q3 FY2026 10-Q and
  all eight earnings releases.* **The SBC-exclusion form FIRES at full strength, and the
  brief's warning about the furnished releases was right:** the releases carry non-GAAP
  everywhere (64 mentions in the latest), and the exclusions, in the company's words:
  *"(ii) Stock-based compensation … We exclude stock-based compensation expense from our
  non-GAAP financial measures primarily because it is not an expense that typically requires
  or will require cash settlement by us."* That is [E5-06]'s named error — *"To say
  'stock-based compensation' is not an expense is even more cavalier"* — applied to
  **$893M, 12.7% of revenue, half again Cadence's rate.** The consequence: non-GAAP operating
  margin **37.3%** against GAAP **13.0%** (FY2025); the segment measure the CODM uses is
  the same construction; and **the pay plan is set on it** (below). *(iii) also excludes the
  gains on divestitures, which is correct and is noted in the company's favour.)*
- [ ] **filed-figure tells [E4-30]** — **DOES NOT FIRE; the evidence runs the other way.**
  Cash taxes paid against pretax income, seven years:

  | FY | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|---|---|
  | cash tax % of pretax | 13.9 | 11.1 | 18.6 | 15.2 | 7.5 | **44.9** | **36.8** |
  | book rate % | 2.4 | −4.0 | 6.1 | 12.6 | 6.9 | 6.6 | 4.0 |

  Cash tax has exceeded book tax in every year since FY2019 — $2.6bn paid against $0.4bn
  booked over seven years. [E4-30] hunts the opposite. (The FY2024–25 spike is tax on the
  SIG and OSG divestiture gains, which sit in investing cash flow while the tax sits in
  operating — a downward distortion to OCF in those two years, noted at Q4.) On smoothness:
  eighteen years without a revenue decline is the ratable model, not smoothing — the
  segment note shows the lumps the consolidated line hides.
- [ ] **metric-switching [E2-49]** — not found. The re-segmentation of FY2024 (Semiconductor
  & System Design → Design Automation + Design IP, after SIG's sale) *exposed* the IP
  weakness rather than hiding it; the non-GAAP tax rate moved to a three-year normalised 18%
  in FY2026 with reasons stated in advance. **The pay plan's bullseyes were pre-set and
  long-lived, and they let the executives miss:** the FY2023 PRSUs required a **13.0%**
  FY23–25 revenue CAGR; the Committee *"certified FY23-25 Revenue CAGR of 10.3%, which
  resulted in a FY23-25 Revenue CAGR Multiplier of 0%"* and rTSR at the 38th percentile —
  **a 0% payout.** The FY2025 EIP scored revenue $6.3bn against a $6.8bn target and non-GAAP
  operating margin 36.3% against 40.0% — *"Average Achievement 91.7"*. That is the
  corpus's positive case for [E2-49], and it is recorded as such.
- [x] **the restructuring charge [E3-53] — FIRES, twice in three years, and the second was
  enlarged.** 2023 Plan **$77.0M**; **2026 Plan announced November 2025 at $300–350M, raised
  by the Board on 2026-08-21 to $425–500M** (8-K/A `0001193125-26-368858`), $236.3M charged
  in 9M FY2026, *"anticipated to be completed by the end of fiscal 2027."* Excluded from
  every non-GAAP figure. **Kept in owner earnings per [E5-33]** — it is cash severance and
  site closure, borne by shareholders.
- [ ] **dividends funded by issuance [E2-52]** — no dividend has ever been paid; n/a.
- [ ] **stock-price targeting [E3-50]** — no instance found.
- [x] **"except for" [E2-57]** — fires in the structural form: every quarter's headline number
  excludes amortisation, SBC, restructuring, deal costs and divestiture gains — five "except
  for" lines, on a permanent basis, with the pay plan attached to the excepted figure.

**[E4-52] — do the flags CONVERGE?** **Partly, and it must be said.** Three flags point at
one system: a guidance culture that beats a narrow midpoint seven quarters in eight; a
non-GAAP construction that removes the company's largest discretionary cost (SBC); and a pay
plan whose two 50%-weighted goals are revenue and *that* non-GAAP margin. That is a
reinforcing system for managing the reported quarter, and the September 2025 cut is what it
looks like when it breaks. **Against convergence:** cash tax exceeds book by $2.2bn over seven
years; the pay plan's long-term bullseye paid 0%; the footnotes are legible; the September
release named its own execution failure. **Two prompts and a partial system, not a
lollapalooza.**

**STEP 3 — THE PRIMARY TEST [E2-01], on the right denominator.**

ROE on book equity (net income ÷ average equity): FY2019 14.1% · FY2020 14.8% · FY2021 14.9%
· FY2022 18.2% · FY2023 21.1% · FY2024 29.9% (19.0% ex the SIG gain) · **FY2025 7.1%** — and
from FY2025 the denominator is $28–31bn of which $38–40bn is goodwill and intangibles, so
**ROE is meaningless post-Ansys and is EXCLUDED** under [E2-47]'s carve-out. On [E2-43]'s
**unleveraged net tangible operating assets** (the row's formula): **FY2024 20.0% · FY2025
18.5% · TTM 14.6%** on GAAP operating income (after $1.6bn of amortisation), and **32.8% on
TTM owner earnings.** [E3-46]'s number is answered: a 20% pre-tax GAAP return on tangible
capital in the pre-Ansys company, against Cadence's 29.5% on the same formula. Good; second in
a row of two.

**[E2-73] — judge the managers on the underlying assets, and [E5-24] on the price paid.**
Ansys, as bought: FY2024 revenue $2,544.8M, operating income $717.9M, OCF $795.7M, owner
cash flow (OCF − SBC − capex) **$480.8M**, ACV growth 11–13%/yr, 85% recurring. Price
**$33.9bn net of cash acquired = 47x operating income, 71x owner cash flow, a 1.4% initial
owner yield** against a 30-year Treasury that was above 4.5% on the day. **At the quote, that
is [E5-24]'s "dumb at another" price by a wide margin.** Two things stated on the other side:
half of it was paid in a share priced at $571.20 that this file values at a fraction of that
([E5-44] above), and the combined perimeter's owner earnings in year one ($1.8bn) already
exceed the sum of the parts' FY2024 figures ($575M + $481M = $1,056M) by $740M, before the
$425–500M restructuring is finished — some of which is revenue growth, some working-capital
timing, and some cost synergy. **The corpus's test is not whether it works; it is whether the
price was right. At 47x operating income the burden of proof is on the buyer, and one year
of results does not discharge it.**

**The half-owner test [E2-26].** Passes on three affirmative instances and fails on one:
1. **The Design IP failure was named in plain words** — *"certain roadmap and resource
   decisions that did not yield their intended results"* — in the same release that cut
   guidance, and again in the 10-K and the 10-Q (*"in response to recent market trends and
   the underperformance of our Design IP segment, we are in the process of reallocating
   resources"*). That is the sentence a half-owner wants and rarely gets.
2. **The pay outcome tables print target, actual and payout** — $6.8bn/$6.3bn; 40.0%/36.3%;
   13.0% CAGR/10.3%/**0%**. A management gaming its disclosure does not print a zero.
3. **The perimeter is fully disclosed** — cash/stock split, pro forma, divestiture gains on
   their own reconciliation lines, the restructuring enlargement filed by 8-K/A.
4. **The failure:** the item a half-owner would most want — **what a seat costs and how
   many there are** — is counted internally (the CODM allocates revenue by *"seats"*) and
   filed nowhere. And every headline number is stated before the cost of paying management.

**The institutional imperative — all four scored [E2-30].** *Not a fraud test.*
- [ ] **resists change in current direction** — not found; the opposite. SIG sold, OSG sold,
  Processor IP sold, OpenLight sold, Ansys bought, a 28,000-person company restructured
  twice in three years.
- [x] **projects/acquisitions materialise to soak up available funds — FIRES, at the largest
  scale in the queue.** The **$34.9bn Ansys merger** — the largest transaction in the
  company's history and one of the largest software deals ever — financed with **$14.3bn of
  new debt** and 30.0M shares, then followed by three divestitures and a $425–500M
  restructuring to pay for it. The stated rationale, verbatim: *"to combine Synopsys'
  semiconductor electronic design automation expertise with Ansys' S&A capabilities to
  address the growing demand for integrated design and simulation tools across various
  industries."* **Recorded sweep of the 10-K, the 10-Q and all eight releases for a
  quantified synergy target: no instance found** — the releases say *"accelerating
  synergies"* and the 10-K says goodwill reflects *"anticipated synergies,"* neither with a
  number. **[E4-39]'s post-mortem cannot yet be owed** (one year); it is pre-registered at
  Q6 as the document this file will look for.
- [ ] **staff studies justifying the leader's craving** — no instance found in the filings.
- [x] **peer behaviour mindlessly imitated — FIRES, softly, on two counts.** Cadence bought
  BETA CAE (simulation) in 2024 and agreed to buy Hexagon's design-and-engineering business
  for **€2.70bn** in September 2025 — **both EDA vendors are buying CAE simulation at the
  same time**, the [E2-27] pattern of collectively neutralising investment. And quarterly
  guidance is the sector norm, followed.

**CAPITAL ALLOCATION — THE TWO BUYBACK CONDITIONS [E5-08], AND CONDITION 2 FAILS.**
- **(1) Ample funds for operations and liquidity? YES**, with the caveat of $9.9bn of debt:
  $3.6bn cash, $850M undrawn revolver, $2.8bn of guided FY2026 OCF, nothing due before
  April 2027.
- **(2) Repurchases at a MATERIAL DISCOUNT to conservatively calculated intrinsic value?
  NO.** The record, implied average prices from the filed dollars and share counts:

  | FY | 2010 | 2013 | 2016 | 2019 | 2021 | 2022 | 2023 | 2024–25 | **FY2026 (9M)** |
  |---|---|---|---|---|---|---|---|---|---|
  | buyback $M | 184.7 | 145.0 | 400.0 | 329.2 | 753.1 | 1,100.0 | 1,160.7 | **0** | **300.0** |
  | implied avg price | ~$22 | ~$36 | ~$47 | ~$120 | ~$271 | ~$305 | ~$388 | — | **$443 / $395** |

  **Dollars rose with price in every step of the series** — the KLAC pattern — and in
  FY2026 the company repurchased at $442.69 three months after selling 4.8M shares to NVIDIA
  at $414.79. Against this run's zero-growth range (Q5: roughly $70–175 a share at the
  sovereign), FY2026's repurchases were made at **2.5x–6x** the band. Fifteen years of
  buybacks that retired zero net shares are not a return of capital; they are the cash cost
  of stock compensation, paid in arrears.
- **→ CAPITAL ALLOCATION FLAG, RAISED**, with the humility clause **[E4-13]**: this rests on
  *our* IV range, and *"it is natural for CEOs to be optimistic about their own businesses.
  They also know a whole lot more about them than I do."* [E5-08]: *"many CEOs never stop
  believing their stock is cheap."* **The flag binds POSITION SIZE, never the discount rate.**
- **[E2-60] — is financial strength being distributed?** The suspension of buybacks for
  FY2024–25 *"until we reduce our expected debt levels"* and the $3.5bn term-loan repayment in
  Q1 FY2026 are the disciplined half; the $300M resumed while $9.9bn of notes and a $425–500M
  restructuring were outstanding is the other half. Small in dollars; recorded.

**THE GUARDRAIL — checked before the verdict is written.**
- [x] Confirmed: **nothing in this Q3 is used to promote the name.** The 20% return on tangible
  capital is a fact about the *business*, recorded at Q2's request [E3-46]; *"a good
  managerial record … is far more a function of what business boat you get into"* [E2-37].
- [x] This business does not require a superstar; no key-person dependence at Q2 [E4-23].
- [x] No great manager is the reason to act; no excisable-cancer case is claimed [E2-35,
  E2-36]. *(If one were, it would be Design IP — a localised, named failure inside an intact
  franchise — and the surgeon has already sold the processor line and hired a new head of
  sales. It is not the reason to act, and it is not used.)*
- **[E3-40] loss of focus — THE VECTOR THIS FILE WATCHES, and the evidence is mixed in a way
  that must be stated exactly.** The Ansys deal is the shape [E3-40] describes — *"purchasing
  other businesses"* outside the base while the base needs attention. The base business's
  larger half (Design Automation) was not neglected: segment margin 37% → 45%, revenue +25%.
  The base business's smaller half (Design IP) **was**: the filer's own words are *"roadmap
  and resource decisions that did not yield their intended results,"* in the year management
  was closing a $35bn deal. **Recorded as a live Q6 monitoring item, not a Q3 finding**, with
  [E4-24]'s exit-not-engage rule attached in advance.
- **The ownership fact, recorded plainly.** All fifteen directors and executive officers
  together hold **1,074,598 shares — 0.56% of 191.6M** — including 297,446 options. The CEO's
  FY2025 total compensation was **$19.6M**; the Executive Chair and founder's $16.4M. Vanguard
  7.1%, BlackRock 6.2%. Highly paid employees with a founder still on the board; not owners
  in the [E3-59] sense. Not a disqualifier; it sits beside the capital-allocation flag.

- **VERDICT: [x] IN — as an OVERLAY, with one capital-allocation flag live and three
  disclosure flags recorded.**
  *IN is **the absence of found disqualifiers, not a finding that these managers are honest**
  — [E5-17]: "People are not that easy to read. Sincerity and empathy can easily be faked,"
  and [E5-32]: audited does not mean true. **IN never promotes.***
  **Carried forward: (1) a guidance culture with a seven-of-eight beat record whose one miss
  was a $500M organic cut fourteen weeks after a reaffirmation, now the subject of a
  consolidated securities class action (complaint due 2026-09-23) [E3-48, E5-30]; (2) non-GAAP
  reporting that excludes $893M of stock compensation and a pay plan set on the excluded
  figure [E4-29, E5-06]; (3) a $35bn acquisition at 47x operating income with no quantified
  synergy target filed, and both EDA vendors buying simulation at once [E2-30, E5-24];
  (4) buybacks run backwards on price, which BINDS POSITION SIZE [E5-08, E4-13].** Against
  them: cash tax $2.2bn above book over seven years, a 0% long-term payout printed in the
  proxy, the IP failure named in plain words, and footnotes that let the perimeter be
  established to the dollar.

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**THE FILING CROSS-CHECK, operator rule 4.** FY2025 10-K, Consolidated Statements of Cash
Flows: *Net cash provided by operating activities* **$1,518,608 thousand**; *Stock-based
compensation* **$893,294**; *Purchases of property and equipment, net* **$(169,454)**;
*Amortization and depreciation* **$660,430**. Q3 FY2026 10-Q, nine months: **$2,298,603 ·
$712,631 · $(156,089) · $1,362,021**; nine months FY2025: **$878,870 · $655,909 · $(134,908)
· $211,307**. Note 2's filed depreciation line: *"Depreciation expenses were $171.9 million,
$162.9 million and $141.4 million in fiscal 2025, 2024 and 2023."* All agree with the tagged
series to the dollar; the TTM is built from these six statements and nothing else.

**MAINTENANCE CAPEX — (c) AS A DISCLOSED JUDGMENT, DECIDED FROM THE FILED SPLIT AS THE BRIEF
REQUIRED, NOT DEFAULTED.** The corpus default is D&A [E3-44, E2-41]. The filed split:

| | FY2025 | TTM to 2026-07-31 |
|---|---|---|
| D&A as tagged | 660.4 | 1,811.1 |
| less amortisation of acquired intangibles (Note 6 / 10-Q Note 17) | (504.4) | (1,615.5) |
| **= depreciation of things that wear out** (Note 2: $171.9M filed) | **~156–172** | **~196–201** |
| **capital expenditures** | **169.5** | **190.6** |
| capex ÷ filed depreciation | **0.99x** | **~0.97x** |
| scheduled amortisation FY2026 / FY2027 (Note 6) | 1,613.4 / 1,545.0 | |

**Ruling: the D&A end is INVALID for this filer — the CVX/AVGO purchase-accounting case, and
the brief's expectation that the D&A end might be the conservative end is answered: it is
not conservative, it is meaningless.** Eighty-nine percent of TTM "D&A" is the straight-line
write-off of $13.0bn of Ansys intangibles over 6–23 years — *"core/developed technologies …
customer relationships … contract rights … trademarks"* — a charge that requires no cash to
renew and that the R&D line, expensed above OCF at $2.5bn a year, already renews. Charging it
as (c) would say the combined company must spend $1.8bn a year to stand still, when its
filed depreciation is $172M and its capex $170M. **(c) is judged at total capex, which the
filed split shows is within 3% of tangible depreciation — so there is no band to display:
the two honest ends coincide.** The QCOM ruling applies on top: the true maintenance spend is
**R&D at 35% of revenue, already inside OCF**, so owner earnings as constructed are
conservative on that axis. **ASC 842**: operating-lease ROU $694.6M, liabilities $137.8M +
$666.6M; no finance leases tagged in any year — the COST/HD addendum does not bite.
**Capitalised software**: $2.2M in FY2023, nil since — the HAS defect does not bite. **The
working-capital increment [E2-23] constraint 3 is inside OCF by construction**: accounts
receivable, inventories (hardware, $479.1M and rising), contract assets ($1,222M, up from
$757M) and deferred revenue all flow through the operating section as filed. **Two
distortions in the recent OCF, named, direction stated, not adjusted:** (i) cash taxes on
the SIG and OSG divestiture gains — $680M and $513M paid in FY2024–25 against $98M in
FY2023 — sit in operating cash flow while the gains sit in investing, **depressing** FY2024–25
OCF; (ii) 9M FY2026 carries a $165M receivables release and a $116M deferred-revenue build
that **flatter** the TTM. They pull in opposite directions and neither is quantified by the
filer; both are recorded.

**Stock compensation subtracted in full [E5-06]: $893.3M in FY2025, $950.0M TTM**, and in
every year of the series. **It is the single largest fact in this Q4.** Over ten years
(FY2015→25) revenue rose 3.1x, operating cash flow 3.1x, **stock compensation 10.3x** (26.3%
a year), and owner earnings at the capex end rose **1.4x — 3.5% a year.** SBC as a share of
OCF: 17% (FY2015) → 33% (FY2023) → 49% (FY2024) → **59% (FY2025)** → 32% (TTM). Per
**[E3-70]** the reported charge is the floor of the correct subtraction, not the measure; no
market-value adjustment is attempted, and any understatement makes owner earnings lower.

**THE WINDOW — AND WHY EVERY HISTORICAL WINDOW IS THE WRONG COMPANY [E4-25, E4-38].** The
corpus default is five years [E2-42]. The combined company has **one** full year. The
Stage 0 table gives the twelve SNPS-only cells ($367M–$836M) and they are not repeated;
they price a company that no longer exists. To satisfy [E2-23]'s *"average annual amount"* on
the *right* perimeter, a **pro forma combined history is built from the two filers' own
statements** — Synopsys as filed plus Ansys standalone (10-K accessions `0001013462-25-000009`,
`-24-000007`, `-23-000013`), each OCF − SBC − capex — and the acquisition interest is then
charged, because the combined company carries it and the parts did not:

| construction | $M | yield on $76,112M | growth to reach 5.37% | growth to reach the 10% floor |
|---|---|---|---|---|
| **pro forma combined 5-yr FY2020–24, less acquisition interest after tax** ($1,285 − $512) | **774** | **1.02%** | 4.35% | 8.98% |
| pro forma combined 3-yr FY2022–24, less acquisition interest after tax | 841 | 1.10% | 4.27% | 8.90% |
| pro forma combined 5-yr, pre-interest | 1,285 | 1.69% | 3.68% | 8.31% |
| pro forma combined 3-yr, pre-interest | 1,353 | 1.78% | 3.59% | 8.22% |
| **FY2026 as guided by the company** (OCF ~$2,800M − capex ~$225M − SBC ~$950M) | **1,625** | **2.14%** | 3.23% | 7.86% |
| **TTM to 2026-07-31 — the only filed full-perimeter year** | **1,797.7** | **2.36%** | 3.01% | 7.64% |
| *(for the record) the screen's band, SNPS-only, FY2008–25, both ends* | *367–836* | *0.48–1.10%* | | |

*Ansys standalone OE: FY2020 $366.3M · FY2021 $360.2M · FY2022 $438.5M · FY2023 $469.9M ·
FY2024 $480.8M. Combined pre-interest: $954.3M · $1,413.8M · $1,581.8M · $1,420.3M ·
$1,056.0M. Acquisition interest: TTM interest expense $624.0M, at the company's own 18%
normalised non-GAAP tax rate = $512M after tax — a CONVENTION of this file, stated as such;
the pre-interest rows are shown so the charge can be seen.*

- **Combined range: $774M to $1,798M — 2.3x, a 132% width.** The screen said 96.3%; the
  screen's band did not contain the right company at all.
- **Is that range too wide to reach a conclusion [E4-25]? No — the KLAC case again: it is
  wide and wholly one-sided.** Every construction, including the company's own guidance and
  the best year it has ever filed on any perimeter, yields **under 2.4% against a 5.37%
  sovereign**. The width does no work at Q5 and it says something true at Q4: **the combined
  company's owner earnings in year one are roughly $740M above what the two parts earned in
  FY2024, before the $425–500M restructuring is complete** — some of it revenue (+11% on the
  pro forma base), some cost, some working-capital timing. Which is which cannot be
  decomposed from the filings; the honest level sits between the guided year and the pro
  forma history.
- **The distorted years, named in both directions [E5-11, E4-41]:**
  - **UP — FY2021–25, the AI design-start wave.** Operating margin 17.5% → 24.9% in one year
    (FY2021→22) and Design Automation's segment margin 37% → 45% since. The registrant:
    *"While we have seen continued strength in the artificial intelligence and high-
    performance computing sectors, certain industries such as industrial, automotive and
    consumer electronics have recovered more slowly."* Ansys's end markets are the slow ones.
  - **UP — TTM working capital**: the $165M receivables release and $116M deferred-revenue
    build named above.
  - **DOWN — FY2024–25 divestiture taxes in OCF** ($1.19bn paid in two years against $98M in
    FY2023) and **FY2025's $267M of expensed deal costs**.
  - **DOWN and KEPT IN per [E5-33]:** the $77.0M 2023 restructuring, the $236.3M charged so
    far of the $425–500M 2026 Plan, and the deal costs — real costs borne by shareholders,
    not added back anywhere in this file.
- **[E3-55] scope check.** Distortion, not See's-in-August noise: the level moved because the
  company doubled in size by acquisition, and the year-one level of the combined company is
  one observation.
- **JUDGED OWNER EARNINGS: $1,500M** — below the guided year and the TTM, above the pro forma
  history. **The judgment, disclosed as a judgment:** the TTM is flattered by ~$280M of
  working-capital timing and sits in a wave the registrant names; the pro forma history
  predates cost synergies that are real (the restructuring is cash severance for headcount
  that has left) and carries interest on a term loan that has been repaid; the guided year is
  management's own number in a guidance culture with a seven-of-eight beat record. $1,500M
  is the TTM less the working-capital flattery, and is **2.0% of the market cap**.

### Great, good, or gruesome? **[E4-20]**

- **[x] GOOD** — *"pays an attractive rate of interest that will be earned also on deposits
  that are added"* — with the base business GREAT and the deposit made at a price that makes
  the blend GOOD.
- **The base business is the great account:** capex 2% of revenue; a **20% pre-tax GAAP return
  on unleveraged net tangible operating assets in the pre-Ansys company** (32.8% on TTM owner
  earnings); revenue up eighteen years running with a 1.2x backlog; growth that consumes
  working capital the customer funds. **[E5-40]'s retention test, FY2015→23 (the clean
  pre-deal span):** owner earnings +$629M on cumulative acquisitions of roughly $2.2bn plus
  capex of $1.0bn — a ~20% incremental pre-tax return, above the "quite satisfactory" 12%.
- **The deposit is the good account at best:** $33.9bn added at a 1.4% initial owner yield,
  now earning — on the most generous reading, attributing all of year one's $740M
  improvement to the deal — 2.2% + 2.2% = a single-digit return on the capital added. That
  is not gruesome ([E4-43]: gruesome is *"unless the cash they consume gets to earn a
  reasonable return"* — Ansys earns 28% operating margins and grew ACV 11–13% a year); it is
  the [E5-42] case: *"whether it's a good investment for us depends on how much we pay for
  that in the end."* The business was great; the price paid for the addition makes the
  blended account good.

### Staying power — all three scored **[E5-11]**

- **(1) A large and reliable stream of earnings — YES.** Owner earnings positive in all
  eighteen filed years, the lowest $143M in FY2009; revenue never down; 49% of a $10.9bn
  backlog converts in twelve months. **[E5-29]: volatility is not risk** — the impairment
  question is coverage.
- **(2) Massive liquid assets — YES, net of a large debt.** Cash $3,606M plus $850M undrawn
  revolver against $9.9bn of notes; **net debt $6.3bn = 3.5x TTM owner earnings, 2.1x the
  company's guided FY2026 operating cash flow.**
- **(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — PASSES, with two dates on the calendar
  and one number that must be watched.** Maturities: **$1.0bn April 2027, $1.0bn April 2028,
  nothing else before April 2030**; $8.0bn is 2030–2055 at 4.85–5.70% fixed. The term loan
  — the only instrument with a leverage covenant — **was repaid in full in Q1 FY2026 and
  terminated**; the revolver carries a leverage covenant but is undrawn (*"no outstanding
  balance … as of July 31, 2026"*), and the Senior Notes indenture carries negative
  covenants only. **[E5-39]'s test — nothing depends on the kindness of strangers — is met
  today: no commercial paper, no revolver draw, no ratings trigger disclosed.** The number to
  watch is the $425–500M of restructuring cash through FY2027 plus $2.0bn of replenished
  buyback authorisation — together larger than the April 2027 maturity — set against ~$2.8bn
  of guided OCF.
- **Leverage, named and quantified [E4-16, E3-29]** — *there is no ratio ceiling in this
  framework*: **$9.9bn principal; TTM interest expense $624.0M; [E2-54] coverage — interest,
  paid and accrued, out of current cash flow NET of capex — is 5.4x on the TTM
  ($2,938M + $624M − $191M ÷ $624M), 3.9x on the guided year, and 2.1x on the pro forma
  FY2020–24 combined mean before interest.** [E2-54] says *"comfortably"*; 5.4x is
  comfortable, 2.1x is the figure on which the deal was underwritten and it is not.
  **[E3-52] on the terms:** fixed-rate, long-dated, covenant-light, plus $2.7bn of
  customer-prepaid deferred revenue — the benefit of debt without its drawbacks, on the
  $8bn that is not due this decade.
- **[E2-55] — score the worst case.** A −20% revenue year (there is none in the filed record;
  the worst is +1.7%) at a 45% decremental margin removes ~$850M of operating income; owner
  earnings land near **$950M**, interest cover ~4.0x, and the 2027–28 maturities are covered
  from cash on hand without a dollar of new borrowing. **Certain, not merely likely.**
- **[E3-66] jurisdiction** — Delaware; shareholders first in the queue. Not an issue.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40]**

**Model exposure, not experience [E4-40].** The benign record — eighteen years without a
revenue decline — is *"not only useless, but actually dangerous"* as a guide. Four
mechanisms, quantified where the filings allow, and the honest finding is that **none kills
the company; two impair the level, one impairs the franchise slowly, and one is
unquantifiable and is the real one.**

1. **THE BASE BUSINESS LOSES THE NODE TO CADENCE — the [E3-40] mechanism, and the row says it
   is already half true.** Cadence has out-earned Synopsys for ten years; Synopsys spent
   FY2024–26 on a $35bn integration, a restructuring and three divestitures; Design IP was
   admittedly under-resourced in the middle of it. **Quantified:** Design Automation is
   $7.8bn annualised at 45%; a five-point share shift to Cadence over a decade is ~$400M of
   revenue and ~$180M of segment income a year, compounding. **Likelihood: [x] a real
   possibility.** Fatal: no; a duopoly's second member still earns 80% gross margins. But it
   is the way a NARROW moat becomes NONE, and it is the Q6 metric.
2. **CHINA — the regime mechanism, exposure named by both EDA filers.** *"government or
   customer efforts, attitudes, laws or policies regarding technology independence may lead to
   non-U.S. customers favoring their domestic technology solutions"* (Synopsys); *"emerging
   players in China such as Huada Empyrean, Xpeedic Technology, X-EPIC, Primarius
   Technologies, Univista, and Giga Design Automation"* (Cadence). **Quantified:** China is
   $814M (11.5%), ~$1.08bn on the TTM perimeter with Ansys; a total loss removes ~$490M of
   segment operating income from ~$3.9bn — a 12% cut. **Likelihood of total loss: a low-level
   possibility. Of continued erosion: [x] a real possibility** — it has already fallen 22%
   ex-Ansys in a year in which Cadence's China revenue recovered to its prior level.
3. **THE DEBT.** $9.9bn at fixed rates; interest $624M. In the [E2-55] case above, cover is
   4.0x and the maturities are met from cash. **Likelihood of the debt killing the company: a
   low-level possibility**, and only via a goodwill-impairment-plus-covenant path that no
   longer exists (the covenanted term loan is gone). What the debt does is convert a $34bn
   acquisition into a permanent $0.5bn-a-year after-tax charge on owners — a level effect,
   priced at Q5.
4. **THE BUSINESS-MODEL DISRUPTION THE REGISTRANT ITSELF FILES — and it cannot be
   quantified.** *"The adoption of AI technologies has brought new demands and also
   challenges in terms of disruption to both our business models and existing technology
   offerings."* The mechanism, in the analyst's words: if the design work now done by
   engineers running seat-licensed tools is done instead by models — whether Synopsys's own,
   a customer's, or a hyperscaler's — the seat is the wrong unit to sell, and the company
   files no seat count with which to see it coming. Synopsys is also the company best placed
   to sell the replacement. **Likelihood: UNKNOWABLE in magnitude; [x] a real possibility in
   kind on a ten-year view.** It is recorded as the one mechanism this file cannot model
   from any document, which is the honest answer rather than a reason to close the file.

- **The bear case stated as its holders would state it [E4-51]:** *Synopsys paid $35bn —
  47x operating income — for a simulation business whose principal competitors it cannot
  price on any SEC filing, financed with $14bn of debt and 30 million shares issued at $571
  that trade at $397; in the same year its IP business, a quarter of the company, lost 43% of
  its operating income on "roadmap and resource decisions that did not yield their intended
  results," a securities class action followed, and the CEO of the third EDA firm was hired
  to run sales; it has spent $6bn on its own shares over fifteen years and retired none of
  them because stock compensation, now 10–13% of revenue and excluded from every number
  management is paid on, absorbed every share; it bought stock at $443 three months after
  selling it at $415; its backlog fell in the first three quarters of owning Ansys; and the
  only EDA competitor with filed numbers has earned a higher gross margin and a higher
  operating margin in every one of the last ten years.* **Every clause is filed, and I accept
  it as fairly put.**
- **What it does not establish is a death.** Owner earnings were positive in the worst year
  on record; revenue has never fallen; the covenanted debt is gone; the maturities through
  2028 are covered by cash on hand; and the franchise segment's margin rose eight points
  while all of the above was happening.

- **VERDICT: [x] IN — GOOD, on a great base business and a dearly-bought addition; the range
  is wide, one-sided, and survivable.**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

*Q1 IN · Q2 IN · Q3 IN · Q4 IN. The gate is open and this is a normal Q5 output, not a
computation. **Synopsys is the twenty-fifth name in this queue to clear all four business
gates.***

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."*

**1. THE YIELD**
- **owner earnings $1,500M (judged) ÷ market cap $76,112M = 1.97%** · **sovereign 5.37%**
- band on the combined perimeter: **1.02% (pro forma 5-yr less acquisition interest) to
  2.36% (TTM)**; the company's own guided year, 2.14%.

**2. WHAT THE PRICE ALREADY ASSUMES** *(perpetual-growth form, as everywhere in this queue)*
- **to match the bare sovereign: +3.40%/yr perpetual** at the judged level (3.01% at the
  TTM; 4.35% at the conservative end).
- **to clear the [E4-28] floor: +8.03%/yr PERPETUAL** at the judged level — **7.64% at the
  TTM, 8.98% at the conservative end.** The screen row's 9.46% was computed on the wrong
  perimeter and a stale rate; the right-perimeter figure is a point lower and the
  conclusion is the same in kind.
- **What the business has actually done — and this is the loudest fact against the growth
  case, not for it.** Revenue compounded **12.1% a year for ten years** (10.9% ex-Ansys) and
  the company guides *"double-digit growth in EDA"*; the pro forma combined perimeter grew
  **5.6%** in FY2025 and the FY2026 guide is ~+9–11% like-for-like. **But owner earnings —
  the thing a buyer is paid from — compounded 3.5% a year over the same ten years**
  (FY2015 $322M → FY2025 $456M), and 14.5% to the clean pre-deal year FY2023, **because stock
  compensation compounded at 26.3%** and took the difference. [E2-63] and [E4-44] together:
  the value cannot grow faster than the owner's earnings, and the owner's earnings have
  grown at a third the rate of the revenue line for a decade.
- **Why the floor is not reached, on three bounds:**
  1. **[E5-34] — the corpus's own routine prices the BOTTOM boundary.** *"we will buy the
     stock … if it sells at a reasonable price in relation to the bottom boundary of our
     estimate."* At the bottom of this file's range (1.02%), even 8% perpetual growth
     gives 9.0%. The floor is not reached at the bottom boundary under any growth belief
     short of 9% forever.
  2. **[E4-35] — the base rate.** *"fewer than 10 of the 200 most profitable companies in
     2000 will attain 15% annual growth in earnings-per-share over the next 20 years."* The
     judged case needs 8% perpetual in *owner* earnings from a company whose owner earnings
     did 3.5% over the last decade on its own perimeter. That is a lesser claim than 15%
     for 20 years, but the record it must overcome is the filer's own.
  3. **[E4-38] — terminal-date selection, in the other direction from KLAC.** The TTM is
     year one of a merger, flattered by ~$280M of working-capital timing and taken at the
     top of an AI design-start wave the registrant itself names; the pro forma history is
     depressed by divestiture taxes and a repaid term loan's interest. Every window is
     published; the judged level sits between them, and neither end is a level the buyer
     can rely on.
- **And the measurement I cannot make, recorded [E4-55]:** with no seat, unit or price series
  filed, none of the revenue growth can be decomposed into price and volume, and the one
  mechanism that would end the growth — the business-model disruption the registrant files as
  a risk — would show first in a seat count the company keeps and does not publish.

**3. WHAT YOU ARE PAID**
- **−3.40 points over the sovereign** at the judged level; **−4.35 to −3.01** across the
  band. **There is no construction on the right perimeter, including the company's own
  guidance and the best year ever filed, in which Synopsys pays as much as a 30-year
  Treasury.**

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- **sovereign used 5.37% — the bare rate, no per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (Q1) and in the discount to value demanded at the end. It is priced **once** — the end
  margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]**, on 191,636,646 shares:

| | conservative (PF 5-yr less interest, $774M) | **judged ($1,500M)** | optimistic (TTM, $1,798M) |
|---|---|---|---|
| **zero growth, at the 5.37% sovereign** | **~$75** | **~$145** | **~$175** |
| **at the [E4-28] 10% floor** | ~$40 | **~$80** | ~$95 |

- **conservative ~$75 · judged ~$145 · optimistic ~$175 · CURRENT PRICE $397.17**
- **The price is 2.3x the TOP of the zero-growth band at the sovereign and 5.3x its bottom;
  4.2x the top of the floor band.** (KLAC was 3.9x its top; AMAT 2.8x; CRM 1.1x. This name
  sits nearer the band than the equipment cohort and further than Salesforce.)

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].** *(Corrected 2026-09-03, found by the
HHH run — this block still carried v4.0's "THERE IS NO HURDLE" heading, the SEVENTH
surviving home of the rule the framework rewrote on 2026-08-28. The floor section above at
[E4-28] already governs; this block is the ranking that applies only to what clears it.)*
- **FLOOR VERDICT FIRST. Honest pre-tax expectancy = owner-earnings yield + sustainable
  growth.** The growth judgment, disclosed: **7% perpetual-equivalent** — above the 5.6%
  the combined perimeter grew in FY2025 and the 3.5% owner earnings grew over ten years,
  below the 9–11% guided for FY2026 and the 12% revenue CAGR, on the reasoning that the EDA
  three-quarters can hold high-single-digit growth if SBC stops growing faster than revenue
  (TTM SBC is back to 10.1% of revenue from 12.7%), and the Ansys quarter's 11–13% ACV
  history predates its owner's guidance culture.

  | construction | yield | + growth | **expectancy** |
  |---|---|---|---|
  | conservative (PF 5-yr less interest) | 1.02% | 7.0% | **8.0%** |
  | **judged** | **1.97%** | **7.0%** | **9.0%** |
  | company-guided FY2026 | 2.14% | 7.0% | 9.1% |
  | TTM, best year ever filed on any perimeter | 2.36% | 7.0% | 9.4% |
  | *judged + a generous 8%* | 1.97% | 8.0% | *10.0% — exactly the floor* |
  | *TTM + a generous 8%* | 2.36% | 8.0% | *10.4%* |

  **At the judged level and the honest growth belief, the expectancy is 9.0% — below the
  floor by one point. It reaches the floor only at 8% perpetual growth, which the record
  does not support, and at the conservative end it does not reach the floor at any growth
  belief under 9%.** *"that's the figure we quit on … that's true whether short rates are 6
  percent or whether short rates are 1 percent"* **[E4-28]**.
- **Stated so it cannot be softened later: THIS IS THE NEAREST-TO-THE-FLOOR FAIL AMONG THE
  RECENT GATE-CLEARERS.** KLAC's most generous construction reached 7.9%; AMAT's needed
  8.75% perpetual; here the most generous honest construction reaches 9.4% and a generous
  one clears. [E4-18] governs: *"A conclusion that required fighting for it is worth less,
  not more"* — a case that clears only by choosing the best year and an above-record growth
  rate is not a case; it is the reason the re-look price below is set where it is.
- **→ THE NAME IS NOT RANKED. It is QUIT ON.** Per the template, the ranking lines are not
  filled in: no ranking position, no comparison against the opportunity set.
- points over sovereign, recorded for the register: **−3.40** (band −4.35 to −3.01).

**WHICH BAR** *(one only)*
- [x] **SCREAMER TEST [E4-01, E4-25]** — take the conservative end and ask whether the price
      already clears it. **No margin is added on top.** Conservative case **~$75/share**;
      judged **~$145**; price **$397.17**. **OUTCOME THREE: the price is above the whole
      range. NO.** *(Bar 1 is not used and no end margin is applied.)*
- **WINDAGE COUNT: ONE.** Conservatism is spent once, at the **[E4-41] normalisation** of the
  level from the TTM ($1,798M) to the judged $1,500M. Realistic inputs everywhere else: the
  bare rate [E3-42]; no end margin [E4-48]; the growth judgment set above the record, not
  below it. **And the windage does no work: the verdict is the same at the TTM level.**

- **VERDICT: [ ] IN  [ ] UNRESEARCHED  [ ] UNKNOWABLE — NONE OF THE THREE IS TICKED. The
  name FAILS at Q5, on PRICE, at the [E4-28] floor: the evidence is in, no named document
  would change it, and the range is one-sided. Ranking position: NONE — quit on, not
  ranked.** *(Wording fixed 2026-09-11 before the fold: an earlier form of this line read
  "[x] UNKNOWABLE is NOT used", which a register parser read as a ticked UNKNOWABLE. The
  verdict was and is FAIL on price.)*
  *A verdict about the price on 2026-09-10, not about the business. Q1–Q4 all returned IN;
  Q4 returned GOOD on a GREAT base business.*

## Q6 — NOT OPENED. No entry; no position exists.

Q6 governs a holding. There is none and none is created. What follows is the **pre-committed
re-look, written in advance per [E1-02]** — *"I believe in establishing yardsticks prior to
the act"* — so that a future run cannot rationalise its way back in, and so that the nearest
miss in the queue is re-opened on a number and not on a mood.

**THE PRICE RE-LOOK — two bands, both on the judged $1,500M at the rate of the day.**
- **Re-run band: ~$175/share** — the top of the zero-growth band at the sovereign. Below
  it, every window and both perimeters are re-run.
- **Floor band: ~$145/share** — the judged zero-growth value, where the judged level with
  the 7% growth belief clears 10% (yield 3.0% at a ~$50bn cap → ~$260/share is where the
  floor is met on 7% growth; ~$145 is where the price sits *inside* the value range and the
  screamer test is no longer outcome three). **The $260 figure is recorded and is NOT armed**:
  at $260 the case would clear the floor only on the growth belief, and [E4-18] says that is
  not a case. **The re-look fires at ~$175; the ranking question opens at ~$145.**
- **The file is likelier to re-open on earnings than on price**, and the earnings condition
  is stated as a number: at $397 the floor needs **~$2.3bn of owner earnings with 7% growth
  ($7.6bn at zero growth)** against $1.5bn judged — roughly the guided FY2026 figure plus
  forty percent, which is what two years of 15% owner-earnings growth with SBC held at 10%
  of revenue would produce. **That is the confirming path, and it is not far.**

**THESIS-CONFIRMING METRIC (both halves, two consecutive fiscal years):** **owner earnings
(OCF − SBC − capex) growing at or above 10% a year WHILE stock compensation stays at or below
10% of revenue.** Either alone is gameable — OE can be grown by working capital, SBC ratio by
revenue mix; together they are the one thing the last decade did not do.

**BULL BREAKERS — pre-registered so they cannot be rationalised away later:**
- **Design Automation segment adjusted operating margin below 42%** in any fiscal year (45%
  in 9M FY2026; 37% in FY2023) — the franchise segment giving back its widening.
- **Backlog below $10.0bn at any fiscal year-end**, or the twelve-month conversion share
  falling below 45% — bookings running below revenue for a second year.
- **Design IP segment adjusted margin below 20%**, or segment revenue down in FY2027 — the
  "reallocation" failing.
- **[E2-49] withdrawal of any of three disclosures**: the two-segment adjusted margin table,
  the product-group percentage table, or the China revenue line. Any of the three removes an
  instrument this file was decided on.
- **Any acquisition above ~$2bn before the Ansys post-mortem is filed** [E4-39] — the
  imperative's second behaviour repeating on the first one's unproven return.
- **A second restructuring enlargement**, or a third plan; or **buybacks above $1bn a year at
  prices above the re-run band** while the notes are outstanding.
- **A revolver draw or a commercial-paper programme** — [E5-39] reversing.
- **A finding — not an allegation — in *In re Synopsys, Inc. Securities Litigation*** or from
  the BIS subpoenas. [E5-16] is a binary and this is the one event that would move Q3 from
  overlay to OUT.

**BEAR BREAKERS — the facts that would make me wrong in the other direction:**
- **Synopsys filing a seat, licence or design-start count for the first time**, closing the
  [E4-55] blind spot that caps this file's Q2 at NARROW.
- **A filed Ansys post-mortem against the announcement case with a quantified synergy
  outcome** [E4-39] — the *"almost never witnessed"* document.
- **Siemens, Dassault or Hexagon becoming SEC registrants**, pricing the Ansys quarter's row.
- **Two years of the confirming metric above.**

**THE MONITORING QUESTION [E3-30], stated now so the answer is not invented later:** *is the
Design IP collapse an aberrational cycle — China, one foundry customer, a processor line now
sold — or has a quarter of the business slipped in a way that permanently reduces intrinsic
value?* On the evidence today it reads as the former for two of the three filed causes and the
latter for the third (*"roadmap and resource decisions"*), and the 9M FY2026 recovery to a 27%
quarterly margin is one quarter. [E4-17]: such beliefs *"change quite gradually"*; [E2-40]:
once crystallised, delay is the graver error.

**Catalysts:** **the consolidated securities complaint, due 2026-09-23**, and the response by
2026-11-04; **the September 2026 Investor Day** announced in the Q2 release — the first
occasion for a quantified synergy target and long-term margin frame; **the FY2026 10-K,
December 2026** — the first full fiscal year of the combined perimeter, and the first Note 4
in which the Ansys purchase-price allocation is final rather than preliminary; **the 2027
DEF 14A, February 2027** — the FY2024 PRSU certification (FY24–26 revenue CAGR) and whether
the pay plan's bullseye let the executives miss again.

**Position size: ZERO.** No position is taken. Had one been contemplated it would have been
**sized DOWN** in any case, because the **[E5-08](2) capital-allocation flag is live** and
[E4-13] binds it to position size and to nothing else.

- **VERDICT: NOT OPENED — no holding exists.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN → Q2 IN (NARROW) → Q3 IN
      (overlay) → Q4 IN (GOOD) → Q5 FAIL on price. Q6 not opened because no position exists.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q2's class is
      **NARROW**, not PROVISIONAL: the unpriced competitors (Siemens EDA, Dassault, Hexagon)
      are **non-SEC filers** — Siemens AG's Form 15F-12B of 2014-05-16 is the document — and
      under the ACLS/KLAC adjudication an *additional* competitor can only narrow a moat,
      never widen one, so the gap caps the class rather than suspending it, and is a Q6
      work-order.
- [x] Every UNRESEARCHED item names its artifact, and **none is load-bearing:** the FY2020,
      FY2021 and FY2023 backlog figures (10-K vintages `0000883241-20-000015`,
      `-21-000022`, `-23-000019`, not pulled); the Ansys S-4's announced synergy targets
      (`0001140361-24-013120`, not pulled — no target appears in any later filing, which is
      the finding); the dollar split of the tax paid on the SIG and OSG gains (not disclosed
      by the filer).
- [x] Every absence claim names its sweep, per the **absence-claim rule**, worded "no
      instance found": competitors named in the subject's 10-K/10-Q · seat/unit/ASP/renewal
      series (17 patterns, FY2025 10-K; Cadence swept on the same patterns by the row) ·
      "EBITDA" (10-K, 10-Q, eight releases) · quantified synergy target (10-K, 10-Q, eight
      releases) · staff studies · price targeting.
- [x] Step 0: the filing was read; **accession `0000883241-25-000028`** (10-K) and
      **`0000883241-26-000025`** (10-Q, the current perimeter); five cash-flow lines and the
      segment revenue total cross-checked to the filed statements to the dollar; the
      depreciation-versus-amortisation split taken from the filed Note 2 line and Note 6
      schedule, not from tags.
- [x] Owner earnings on a multi-year mean **on the right perimeter** — a pro forma combined
      five-year and three-year history built from both filers' statements, the company's
      guided year and the TTM, six constructions published [E4-38]; (c) disclosed as a
      judgment, with the **D&A end ruled INVALID** and the reason given in dollars from the
      filed split, and the two honest ends found to coincide.
- [x] Competitor row filled: **9 companies, 8 with filed same-formula figures**, the
      non-registrants recorded with the rung (SEC), the document (15F-12B) and the obstacle.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury
      daily par yield curve), dated 2026-09-10, struck fresh on resumption; the brief's stale
      5.24% is not used anywhere.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen (Bar 2); **windage count ONE**, stated and located.
- [x] Prices dated; the aggregator quote flagged as a live quote only.
- [x] Run committed to git after every gate under the write-early protocol (five commits:
      file creation; Step 0/perimeter/Q1; Q2; Q3; Q4; this one). Two session kills survived
      with zero question loss.
- [x] **Operator rule 9 discharged:** the brief's favourite hypothesis — "possibly the widest
      moat in the queue" — was the one hunted hardest, and it was refuted on three filed
      facts (Cadence's ten-year margin lead, the Design IP collapse, the absence of a seat
      series). The fact that most threatened the *fail* verdict — that a generous construction
      clears the floor — was stated in its strongest form (10.4% at TTM + 8%) and answered on
      [E5-34], [E4-35] and [E4-18] rather than omitted.

## REGISTER
- **Verdict: [x] OUT ON PRICE at Q5** — about the price, not the business. Not UNRESEARCHED
  (no named document would change it) and not UNKNOWABLE (the evidence is in, and the range,
  though 2.3x wide, is wholly one-sided).
- **One line:** *The larger, lower-margin half of a real duopoly, one year into a $35bn
  acquisition bought at 47x operating income, priced to require a rate of owner-earnings
  growth it has not delivered in a decade because its stock compensation took the growth.*
- **If UNRESEARCHED — the work order:** n/a to the verdict; the three non-load-bearing items
  are listed in the self-audit with their accessions.
- **If UNKNOWABLE:** n/a to the verdict. **Two things are genuinely unknowable from the
  filing rung and are recorded as moat defects rather than verdicts:** the **seat count and
  price per seat** (counted by the CODM for geographic allocation, filed nowhere), and **the
  Ansys quarter's competitive position** (its principal competitors are non-SEC filers and
  Ansys itself declared product-line reporting *"impracticable"*).

---
# THE TWO REQUIRED OUTPUTS (queue contract)

## 1. THE PRICE
**Current price $397.17** (2026-09-10 close, aggregator, flagged as a live quote only) on
**191,636,646 shares** hand-read off the Q3 FY2026 10-Q cover (`0000883241-26-000025`) =
**market cap $76,112M**.

**Value, zero growth against the 5.37% US Treasury 30-year, as a round-number range [E4-01]:**

> ### conservative ~$75 · **judged ~$145** · optimistic ~$175 per share
> ### at the [E4-28] 10% floor: ~$40 to ~$95, **judged ~$80**

**The price is 2.3x the top of the zero-growth band and 5.3x its bottom.** Owner-earnings
yield **1.97%** (band 1.02%–2.36%) against a **5.37%** sovereign; **−3.40 points over the
bond**. Growth required to clear the floor: **+8.03%/yr perpetual** at the judged level.

## 2. PASS / FAIL

# ❌ FAIL — at Q5, ON PRICE, at the [E4-28] floor.
### Q1 IN · Q2 IN (NARROW) · Q3 IN (overlay, one capital-allocation flag, three disclosure flags) · Q4 IN (GOOD) · **Q5 FAIL** · Q6 not opened.

**All four business gates returned IN — the twenty-fifth name in this queue to do so.** The
file closes on price: at a judged 1.97% against a 5.37% bond, the expectancy at an honest 7%
growth belief is 9.0%, one point under the floor, and it reaches the floor only at the best
year ever filed plus 8% perpetual growth from a company whose owner earnings compounded 3.5% a
year over the last decade. **The nearest miss among the recent gate-clearers, and quit on
under [E4-28] rather than ranked** — with the re-look armed at ~$175 and the floor band at
~$145, and an earnings path (two years of 10%+ owner-earnings growth with SBC held at 10% of
revenue) that would re-open it without a price move.
