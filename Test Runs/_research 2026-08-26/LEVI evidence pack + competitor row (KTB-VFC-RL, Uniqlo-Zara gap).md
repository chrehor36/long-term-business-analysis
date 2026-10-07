# LEVI — evidence pack and competitor row
**Built 2026-08-31 for `Test Runs/2026-08-31 Run - LEVI (Levi Strauss) v4.1.md`.**
Everything here is filing-sourced with accession numbers. Where a number is a judgment or a
solved-for quantity it is labelled.

---
## 1. THE STAGE 0 ARTIFACT — how a $8.2bn company priced at $801M

**The screen's share count was the 2018 10-K cover count: 37,602,843.**
XBRL `dei:EntityCommonStockSharesOutstanding` for CIK 0000094845 has **30 rows and the last
one is dated 2019-01-30** (2018 10-K, acc. 0000094845-19-000006). There is **no post-IPO row**,
because after March 2019 the tag is dimensioned by `us-gaap:CommonClassAMember` /
`CommonClassBMember` and the `companyfacts` API drops dimensioned facts. Any screen reading
that tag inherits a January 2019 number.

That number is **pre-split and pre-IPO**:
> "the completion of the **ten-for-one stock split** of our common stock that became effective
> on **March 4, 2019**" — Form 424B4 filed 2019-03-21, acc. 0001193125-19-082264

followed by reclassification of all outstanding common into Class B, then the IPO
(9,460,557 primary shares sold by the company; 27,206,110 secondary by selling holders).

| | shares | source |
|---|---|---|
| screen's count | 37,602,843 | 2018 10-K cover, dated 2019-01-30 |
| Class A, 2026-07-01 | 100,456,337 | Q2 FY2026 10-Q cover, acc. 0000094845-26-000037 |
| Class B, 2026-07-01 | 284,394,225 | same cover |
| **total economic shares** | **384,850,562** | |
| ratio | **10.2346x** | |

Balance-sheet cross-check at 2026-05-31: Class A 99,130,650 + Class B 285,717,276 =
384,847,926. FY2025 year-end (2025-11-30): Class A 103,620,225 + Class B 286,756,831 =
390,377,056.

**Class B carries ten votes and converts 1-for-1 into Class A.** Economics are identical
across the classes; only votes differ. So the cap must be computed on the total.

- corrected cap at $21.29 (NYSE close 2026-08-28): **$8,193.5M**
- screen's cap: **~$801M** (37,602,843 × ~$21.30 = $800.9M — an exact reconciliation)
- **understated by 10.23x; the screen captured 9.8% of the company.**
- the screen's 26.3% statute yield ÷ 10.2346 = **2.57%** — below the 5.19% sovereign.

This is the exact failure mode `CLAUDE.md` names: *"cap = close(anchor) × shares(measurement)
× splits AFTER measurement."* The ten-for-one split occurred after the measurement date and
was not applied.

**Third occurrence in this project** (RMR: priced a class with no economic interest; CHWY:
Class A alone understated the cap 43%). LEVI is the worst of the three, and it is a
different mechanism — not a missing class but a **stale, pre-split cover tag that XBRL
stopped updating at the IPO**. Any dual-class filer whose cover tag went dimensional at IPO
carries the same trap.

---
## 2. THE DIVIDEND RECORD — every declaration, from the filed series

Source: XBRL `us-gaap:CommonStockDividendsPerShareDeclared` and
`CommonStockDividendsPerShareCashPaid`, CIK 0000094845, cross-read against the equity
statements in the FY2021/FY2023/FY2025 10-Ks and the Q2 FY2026 earnings release
(acc. 0000094845-26-000038).

| FY | Q1 | Q2 | Q3 | Q4 | year | paid ($M) | note |
|---|---|---|---|---|---|---|---|
| 2018 | 0.24 | 0 | 0 | 0 | 0.24 | 90.0 | pre-IPO, one annual declaration (split-adjusted) |
| 2019 | 0.29 | 0 | 0 | 0.01 | 0.30 | 113.9 | IPO year, still annual-style |
| 2020 | 0.08 | 0.08 | **0** | **0** | **0.16** | 63.6 | **two quarters skipped** |
| 2021 | 0.04 | 0.06 | 0.08 | 0.08 | 0.26 | 104.4 | **resumed at half the pre-suspension rate** |
| 2022 | 0.10 | 0.10 | 0.12 | 0.12 | 0.44 | 174.3 | |
| 2023 | 0.12 | 0.12 | 0.12 | 0.12 | 0.48 | 190.5 | |
| 2024 | 0.12 | 0.12 | 0.13 | 0.13 | 0.50 | 198.5 | |
| 2025 | 0.13 | 0.13 | 0.14 | 0.14 | 0.54 | 212.9 | |
| 2026 | 0.14 | 0.14 | **0.16** | 0.16e | 0.60e | ~246e | raised 14% July 2026, ~$62M/qtr |

**What the record can support:** a payment history of seven years as a public company, one
of which (2020) had half its quarters skipped and the following year restarted at $0.04
against a pre-COVID $0.08.

**What it cannot support:** any claim of a dividend *policy* with a record. The 10-K says
so in its own words: *"In the absence of a dividend policy, we will continue to evaluate and
consider declaration of dividends on a quarterly basis and the expectation is that they will
grow in line with net income"* (FY2025 10-K). There is no aristocrat-class record here and
there is a live precedent of skipping two quarters outright.

### Growth rates — every window published [E4-38]

| window | from | to | years | CAGR |
|---|---|---|---|---|
| FY2020 → FY2025 | 0.16 | 0.54 | 5 | **27.5%** ← the headline |
| FY2021 → FY2026e | 0.26 | 0.60 | 5 | 18.2% |
| pre-COVID run-rate → FY2026e | 0.32 (0.08×4) | 0.60 | 6 | **11.0%** |
| FY2019 → FY2026e | 0.30 | 0.60 | 7 | 10.4% |
| FY2022 → FY2026e | 0.44 | 0.60 | 4 | 8.1% |
| FY2023 → FY2026e | 0.48 | 0.60 | 3 | **7.7%** ← the recent rate |

The prior pass's +26.4% raw and +21.3% pre-2020-base figures reproduce to within rounding
against the FY2020 and FY2021 bases. **Both are artifacts of a base year in which two
quarterly dividends were not paid.** The honest recent rate is 7-8%.

### Decomposition — earnings vs share retirement vs payout expansion

Identity: DPS = payout ratio × EPS; EPS = earnings ÷ shares. Log-contributions.

| window | ΔDPS | earnings | share retirement | payout expansion |
|---|---|---|---|---|
| FY2021 → FY2025 | ×2.077 | ×1.044 (**5.9%**) | ×1.025 (**3.4%**) | ×1.940 (**90.7%**) |
| FY2022 → FY2025 | ×1.227 | ×1.016 (7.7%) | ×1.010 (5.0%) | ×1.196 (**87.4%**) |
| FY2019 → FY2025 | ×1.800 | ×1.465 (65.0%) | ×1.022 (3.6%) | ×1.203 (31.4%) |

Inputs: net income FY2019 $394.6M, FY2021 $553.5M, FY2022 $569.1M, FY2025 $578.1M; diluted
shares 408.4M / 409.8M / 403.8M / 399.7M; payout ratio (DPS ÷ diluted EPS) 31.3% / 19.3% /
31.2% / 37.2%.

**Read:** off the two post-COVID bases, ~90% of dividend-per-share growth is the payout
ratio rising, ~6% is earnings and ~4% is share retirement. Off the FY2019 base earnings do
more work (65%) because FY2021's payout was artificially low mid-restoration. Share
retirement contributes almost nothing in any window — diluted shares are **higher** than
they were at the IPO (388.6M in FY2018 vs 399.7M in FY2025), because stock compensation has
roughly offset buybacks; only in the last two years has the count genuinely fallen
(390.4M at FY2025 year-end → 384.9M at 2026-07-01, the $120M and $200M ASRs).

### Cash dividends as a share of owner earnings — then vs now

| | dividends | OE (c = D&A) | OE (c = total capex) | payout of OE |
|---|---|---|---|---|
| FY2019 | $113.9M paid | $233.1M | $181.6M | **48.9% – 62.7%** |
| FY2025 | $212.9M declared | $241.7M | $226.6M | **88.1% – 94.0%** |
| forward run-rate | ~$246M | $241.7M | $226.6M | **102% – 109%** |

Owner earnings per the framework convention (OCF − SBC − (c)). FY2019: OCF $412.2M, SBC
$55.2M, D&A $123.9M, capex $175.4M.

**The dividend has gone from roughly half of owner earnings to all of it.** Against the
5-year owner-earnings mean the coverage is better (0.98x–1.27x) and against the FY2026
guide-implied accrual view it is comfortable (2.1x) — the gap between those readings is the
central unresolved fact of the whole run.

**But the [E2-52]/[E2-60] flags do NOT fire.** FY2025 distributions ($212.9M dividends +
$150.5M repurchases = $363.4M) exceeded adjusted free cash flow ($529.6M − $221.4M =
$308.2M), and the 10-K discloses that the ASR upfront was funded "from the net proceeds of
the sale of Dockers." Yet **net debt fell** $309.5M → $190.4M, no shares were issued, and
cash rose. Financial strength improved while paying out. The honest observation is narrower
than a flag: **the incremental FY2025 payout came from selling a business.**

---
## 3. THE BOOM-WINDOW QUESTION [E4-41]

The 2021-22 apparel boom sits squarely in every trailing window.

| FY | ROE (NI ÷ avg equity) | gross margin | DTC % of revenue | OCF |
|---|---|---|---|---|
| 2020 | −8.9% | 52.8% | 39% | $469.6M |
| **2021** | **37.3%** | **58.1%** | **36%** | **$737.3M** |
| **2022** | **31.9%** | 57.5% | 38% | $228.1M |
| 2023 | 12.6% | 56.9% | 43% | $435.5M |
| 2024 | 10.5% | 60.0% | 46% | $898.4M |
| 2025 | 27.2% (23.6% ex-Dockers gain) | 61.7% | 49% | $529.6M |

Equity: $1,299.5M / $1,665.7M / $1,903.7M / $2,046.4M / $1,970.5M / $2,278.6M.
Note **FY2021's gross margin rose 530bp while the DTC mix FELL three points** — that is the
boom, undisguised: full-price selling with no promotional cadence. And FY2022's OCF
collapse is the hangover: inventory $898.0M → $1,416.8M in one year.

Two named one-offs stripped before the owner-earnings mean is trusted:
- **FY2024 OCF includes ~$87.1M** of upfront payments from the third-party logistics provider
  for use of the company's warehouse equipment (FY2025 10-K lease note) — a financing-like
  receipt recorded in operating cash flow. Stripped.
- **FY2024 was a 53-week year**, benefiting net revenues by **~$78M, or 1.3%** (FY2025 10-K).
  Flagged, not separately stripped from cash flow.

**Conclusion on Stage 0 (c):** the screen's 26.3% statute yield was the corrupted cap first
(10.2x) and the boom second. Corrected for the cap alone it becomes 2.57%. This run's own
independent owner-earnings computation lands at 2.9%–4.0%, confirming the correction.

---
## 4. THE Q2 CRUX — separating DTC channel mix from pricing power

**LEVI never quantifies the mix component of gross margin in any filing read.** It names the
drivers and quantifies only currency. So the separation has to be solved from the filed
series. All numbers below are as reported in each year's own 10-K.

| FY | DTC % of net revenues | gross margin | the 10-K's own attribution |
|---|---|---|---|
| 2020 | 39% | 52.8% | COVID |
| 2021 | 36% | 58.1% | (mix fell, margin rose 530bp — the boom) |
| 2022 | 38% | 57.5% | |
| 2023 | 43% | **56.9%** | "**increased product costs and lower full priced sales**, partially offset by favorable channel mix"; FX +20bp |
| 2024 | 46% (47% ex-Dockers) | 60.0% (60.6% ex-Dockers) | "**lower product costs and favorable channel and brand mix**"; FX −50bp |
| 2025 | 49% | 61.7% | "**favorable channel mix, price increases, and lower product costs**, partially offset by the impact of tariffs"; FX +40bp |
| H1 2026 | 52% | **62.3%, flat YoY** | "**pricing actions and lower product costs** and the **unfavorable impact of tariffs**"; FX +10bp |

### The solve

**Window A, FY2021 → FY2024 (both as reported, both including Dockers):**
DTC 36% → 46% = **+10 points**. Gross margin 58.1% → 60.0% = **+190bp**.
The DTC-minus-wholesale gross-margin spread that would make channel mix explain **100%** of
the move is 190 ÷ 10 = **19.0 points** — an entirely ordinary apparel channel spread.
**On this window, nothing beyond channel mix is needed to explain the entire gross-margin
gain.** *(Judgment, disclosed: 19.0 points is solved for, not assumed. Sensitivity — at a
15-point spread mix explains 150 of the 190bp; at 25 points it over-explains.)*

**Window B, FY2024 → FY2025 (both ex-Dockers):**
DTC +2 points → mix at 19pts ≈ **+38bp**. Currency, disclosed by the company: **+40bp**.
Actual: **+110bp**. Residual for price + lower product cost − tariffs: **≈ +32bp.**

**Window C, H1 FY2026:**
DTC +1 point → mix ≈ **+19bp**. Currency, disclosed: **+10bp**. Actual: **0bp.**
Residual for price + cost − tariffs: **≈ −29bp.**

**Finding: the consolidated gross-margin expansion is overwhelmingly channel mix, and the
expansion stops when the mix contribution shrinks.** DTC is already 52%. Each further point
buys roughly 19bp. Management guides FY2026 gross margin to **+10 basis points**.

### The disconfirming evidence, hunted [E4-26]

Three filed facts cut the other way and must be carried:
1. **Price and volume rose together** in H1 FY2026 in both channels: *"Wholesale revenues
   increased primarily due to an increase in volumes... DTC and wholesale revenues also
   benefited from price increases"* (Americas); *"The increase in wholesale revenues was
   primarily due to an increase in units sold"* (Asia); DTC comparable sales +7% (Q1) and
   +6% (Q2). Raising price while units grow is stronger evidence than [E2-44] asks for.
2. **The tariff pass-through succeeded.** ~$80M of IEEPA tariffs paid through Q1 FY2026, and
   gross margin still rose 110bp in FY2025 and held flat in H1 FY2026. Compare FY2023, when
   cost inflation was *not* passed through ("lower full priced sales"). The [E4-37] agony
   read is: **agony in FY2023, no agony in FY2025-26.**
3. **"Lower product costs" appears in FY2024, FY2025 and H1 FY2026** — an exogenous input
   tailwind (cotton and freight), not pricing power. [E4-41] instructs that this be named
   and not credited to the moat.

### Units vs dollars [E4-55] — the gap, named

**LEVI files no total unit-volume series anywhere in the filings read.** It files unit *mix*
(pants 67%/66%/67% of total units sold FY2025/24/23; tops 29%/28%/27%; footwear <1%/2%/2%)
and qualitative volume language. The closest thing to a physical series is DTC comparable
sales (+7%, +6% in FY2026 Q1/Q2) and the store count (1,231 company-operated stores at
FY2025 year-end; 110 opened and 70 closed in FY2025).

The one Precision-Steel-pattern instance in the filed record: **FY2025 Asia wholesale — "a
decrease in units sold offset by an increase in average revenues per unit."** It reverses in
H1 FY2026 ("an increase in units sold"). No document in the filed record resolves total
units; this is a disclosure gap, not an unperformed retrieval.

---
## 5. THE COMPETITOR ROW [E3-28]

Latest full fiscal year for each, filing-sourced. Gross margin computed as
(revenue − cost of goods and services sold) ÷ revenue from XBRL `companyfacts`; operating
margin from the filed `OperatingIncomeLoss`.

| Company | fiscal year end | net revenue | gross margin | operating margin | DTC % of revenue | revenue trend |
|---|---|---|---|---|---|---|
| **Levi Strauss (LEVI)** | 2025-11-30 | **$6,282.0M** | **61.7%** | **10.8%** (adj EBIT 11.4%) | **49%** | +4.1% reported, **+7.2% organic**; second consecutive up year |
| **Kontoor Brands (KTB)** | 2026-01-03 (53wk) | $3,152.5M | 45.2% | 10.7% | 15.2% | +20.9% reported — **acquisition-driven**: Wrangler +6.0% (incl. ~2pt 53rd week), **Lee −5.1%**, Helly Hansen $459.7M new |
| **VF Corp (VFC)** | 2026-03-28 | $9,605.2M | 54.8% | 6.0% | n/d | +1.1%; **−18.9% below its FY2022 peak** ($11,841.8M) |
| **Ralph Lauren (RL)** | 2026-03-28 | $8,114.5M | **69.9%** | **14.5%** | n/d | **+14.6%, record** |

Accessions: LEVI 0000094845-26-000008 · KTB 0001760965-26-000014 · VFC 0000103379-26-000030 ·
RL 0001628280-26-037074.

### Kontoor's brand detail — the direct denim comparison

From KTB's FY2025 10-K segment tables (in thousands):

| brand | FY2023 | FY2024 | FY2025 | FY2025 segment profit | segment op margin |
|---|---|---|---|---|---|
| Wrangler | $1,754,130 | $1,805,989 | $1,914,622 | $440.0M | **23.0%** |
| Lee | $842,520 | $790,625 | $750,368 | $68.9M | 9.2% |
| Helly Hansen | — | — | $459,716 | $31.8M | 6.9% |

**The row's single most important fact, and it cuts against the franchise claim:**
LEVI's 61.7% gross margin next to Kontoor's 45.2% looks like brand power and is mostly
**channel structure** — LEVI is 49% DTC, Kontoor 15.2%. At the segment operating line,
before corporate expense, **Wrangler runs 23.0% and Levi's Brands runs 20.2%** (Americas
21.9%, Europe 21.6%, Asia 13.1%). The direct denim comparator's flagship brand is *more*
profitable per revenue dollar than Levi's is.

**And the fact that cuts for it:** Levi's grew **+7.2% organic** in FY2025 while Wrangler
grew ~4% organic (6.0% less the ~2-point 53rd week) and **Lee shrank for the third straight
year**, and while VF Corp sits 19% below its FY2022 peak. Levi's is taking share from the
direct comps. Ralph Lauren, the successful-brand-transition comp, is still ahead on both
margins and growth — LEVI has not caught it.

Corporate expense loads, for fairness: LEVI $520.0M = 8.3% of revenue; Kontoor's segment
profit $508.9M vs operating income $336.8M implies ~$172.1M = 5.5%.

### Peers taken, and the gap named honestly

**3 of roughly 6-8 real public comparators pulled.**

**Named gaps, with routes (UNRESEARCHED work orders, not load-bearing):**
- **Fast Retailing (Uniqlo)** — foreign private issuer, no EDGAR filings. Route: Tokyo Stock
  Exchange / TDnet annual securities report and the English IR site (evidence-ladder rung 4).
- **Inditex (Zara)** — foreign private issuer. Route: CNMV / Bolsas y Mercados Españoles
  annual report, English version on the IR site (rung 4).
- **Shein** — private; no route.
- **Abercrombie & Fitch, American Eagle, Gap** — US filers, EDGAR, ordinary retrieval; not
  pulled. These are channel comps, not brand comps.

**Effect on the class:** the missing rows are the reason the moat class is held at **NARROW
rather than WIDE**. They could show whether Levi's is losing global category share to
fast-fashion; they cannot overturn LEVI's own realized units-and-price record, which is the
deciding evidence. The class is therefore not marked PROVISIONAL.

**Row limit stated [E3-61]:** the row shows position, not conduct. Kontoor's Wrangler margin
advantage says nothing about how either management will behave next year.

---
## 6. THE GUIDANCE RECORD [E3-48] — pulled and scored

Initial full-year guidance is given in the January Q4 earnings release each year.

| FY | initial guide | outturn | score |
|---|---|---|---|
| **2024** (acc. 0000094845-24-000011, 2024-01-25) | reported net revenue growth **1% to 3%**; adjusted diluted EPS **$1.15–$1.25** | +3%; adjusted diluted EPS **$1.25** | **met, at the top of the range** |
| **2025** (acc. 0000094845-25-000006, 2025-01-29) | reported **(1)% to (2)%**; organic **+3.5% to +4.5%**; adj EBIT margin **10.9%–11.1%**; adj diluted EPS **$1.20–$1.25** | organic **+7.2%**; adj EBIT margin **11.4%**; adj diluted EPS **$1.34** | **beat all three** |
| **2026** (acc. 0000094845-26-000009, 2026-01-28) | reported **+5% to +6%**; organic **+4% to +5%**; gross margin **flat**; adj EBIT margin **11.8%–12.0%**; adj diluted EPS **$1.40–$1.46** | raised at Q1 (acc. 0000094845-26-000021) and again at Q2 (acc. 0000094845-26-000038) to reported **+7.0%–7.5%**, organic **+5.5%–6.0%**, gross margin **+10bp**, adj EBIT **12.0%**, adj EPS **$1.46–$1.52** | in progress; **raised twice** |

FY2026 guidance carries a stated assumption: *"Guidance assumes U.S. tariffs on imports from
China remain at 30% and Rest-of-World at 20%."*

**This is the inverse of the OXM record** (three consecutive initial guides missed on every
metric). The [E4-22] projections flag still fires on the *practice* — quarterly guidance is
standing, and Item 1 of the 10-K carries a long-term target of *"approximately $9 billion to
$10 billion in total company net revenue"* and *"Adjusted EBIT margins to approximately 15%
over the long term"*, which is the [E4-35]/[E5-30] class exactly. But the [E3-48] remedy is
to demand the record of the people making the projections, and that record is good.

---
## 7. CAPITAL ALLOCATION — the filed record

### Buybacks [E5-08, E2-51, E5-24, E4-13]

Average price paid per share, each from the filing that reports it:

| FY | amount | shares | average price |
|---|---|---|---|
| 2020 | $56.2M | 3.0M | $18.73 |
| 2021 | $88.4M | 3.4M | **$25.78** ← the boom top |
| 2022 | $172.9M | 8.7M | $19.89 |
| **2023** | **$8.1M** | 0.5M | **$17.97** ← the cheapest year, and they stopped |
| 2024 | $90.0M | 4.8M | $18.75 |
| 2025 | $150.5M ($30.0M open market + $120.0M ASR) | 1.6M + 5.59M | **$20.80** (ASR itself $21.48) |
| 2026 | $200M ASR launched Q1, settling Q3 | — | — |

Authorization remaining: **$440.4M as of 2026-01-23**. Program authorized $750M, 2022-05-31.

**Condition (1), ample funds: PASS** — $848.8M cash and short-term investments at FY2025
year-end, $1.0bn revolver undrawn, no debt maturity before 2030.
**Condition (2), material discount to conservatively-calculated IV: FAILS on this run's
numbers** — the largest purchases were made at the highest prices, and the current $200M ASR
runs at ~$21-22 against an owner-earnings-based value band of roughly $6-17. The FY2023
near-refusal at $17.97 is the [E2-51] tell, though FY2023 was also the year of weakest OCF
and highest inventory, which is a defensible condition-(1) reason.
**[E4-13] humility clause, in full:** this rests on this run's own IV range; management knows
the business better than I do; and the flag binds position size only.

### The acquisition [E2-30(2), E5-24, E4-39]

**Beyond Yoga, Q4 FY2021, $390.9M cash** ("Payments for business acquisition" $390,915k,
FY2021 10-K, acc. 0000094845-22-000010) — the boom top. Trademark valued at $216.0M on a
relief-from-royalty method (a PwC critical audit matter in FY2021 and again in FY2025).

| | impairment | composition |
|---|---|---|
| FY2023 | $90.2M | $75.4M goodwill + $14.8M trademark |
| FY2024 | $111.4M | $36.3M goodwill + $66.0M trademark + $9.1M customer relationships |
| **cumulative** | **$201.6M — 52% of the price** | |

FY2025: revenue $151.3M (+15.4%), **operating loss $(13.6)M** — still loss-making in year
four. The FY2025 annual test disclosed that fair value exceeded carrying value by **less than
10%**, an explicit near-miss disclosure most filers omit (a candor positive [E2-26]).

**No candid acquisition post-mortem [E4-39] found in any filing read.** Each impairment is
attributed to "the macroeconomic environment," "an increase in discount rates," or
"incremental investments in the brand and team" — never to the price paid [E5-24].

### Stated policy vs practice

FY2025 10-K liquidity outlook: capex **3.5-4% of revenue**; *"a dividend payout ratio target
of **25-35% of net income**"*; *"return **55-65% of Adjusted free cash flow** to stockholders."*

| | actual FY2025 |
|---|---|
| capex ÷ revenue | $221.4M ÷ $6,282.0M = **3.5%** — inside policy |
| dividends ÷ continuing-ops net income | $212.9M ÷ $502.0M = **42.4%** — above the 25-35% band |
| dividends ÷ adjusted net income | $212.9M ÷ $537.1M = 39.6% — above the band |
| (dividends + buybacks) ÷ adjusted FCF | $363.4M ÷ $308.2M = **118%** — above the 55-65% band |

The July 2026 raise to $0.16 (~$62M/quarter, ~$246M/year) puts the forward payout at ~43% of
guided FY2026 adjusted net income. A live policy-versus-practice gap; not a flag, because
net debt fell and no shares were issued.

---
## 8. THE FLAGS — what fired and what did not

| flag | verdict | evidence |
|---|---|---|
| Weak accounting [E4-22] | **not fired** | SBC expensed $81.6M; impairments taken at the annual test, not deferred; the "less than 10% headroom" disclosure volunteered |
| Unintelligible footnotes [E4-22] | **not fired** | notes legible; segment, channel, brand, geography, lease and debt detail all readable |
| Trumpeted projections [E4-22] | **FIRED** | standing quarterly guidance + "$9-10 billion" and "approximately 15%" long-term targets in Item 1 [E4-35, E5-30] |
| Serial share issuance [E5-15] | **not fired** | diluted shares 409.8M (FY2021) → 399.7M (FY2025); outstanding 384.85M at 2026-07-01 |
| EBITDA / adjusted promotion [E4-29] | **FIRED** | **Adjusted EBITDA** added to the non-GAAP suite in the FY2025 10-K ("Adjusted EBIT excluding depreciation and amortization"); guidance is given on Adjusted EBIT margin, not GAAP; three headline income figures coexist (GAAP total $578.1M, GAAP continuing $502.0M, adjusted $537.1M) |
| Filed-figure tells [E4-30] | **not fired** | cash taxes ÷ pretax income: 18.9% (FY2021), 19.9%, 33.5%, 47.0%, **25.2%** (FY2025) — not falling; reported growth visibly lumpy, not smoothed |
| Metric-switching [E2-49] | **FIRED, mildly** | organic net revenue guidance *introduced* in January 2025, the year reported revenue was guided to −1% to −2%. Defensible (real divestitures, the 53rd week, full reconciliation published) but the timing is the pattern |
| Dividends funded by issuance [E2-52] | **not fired** | no issuance; net debt fell $309.5M → $190.4M in FY2025 |
| Restricted earnings [E2-60] | **not fired** | financial strength improved while paying out |
| Except-for [E2-57] | **not fired** | GAAP reported alongside adjusted at every line with full reconciliation; no miss framed away |
| Restructuring charge [E3-53] | **FIRED** | FY2014 $128.4M · FY2015 $14.1M · FY2020 $86.8M · FY2021 $5.7M · FY2023 $20.3M · **FY2024 $185.6M** (+$54.3M "restructuring related" inside SG&A) · FY2025 $24.5M (+$12.1M). Three large rebasings in twelve years, and the 10-K warns of more. Counted in the owner-earnings mean [E5-33] — they run through OCF |
| Institutional imperative (2) [E2-30] | **FIRED** | Beyond Yoga, §7 above |
| Institutional imperative (1),(3),(4) | **not fired** | Dockers divested, Denizen killed, footwear exited, distribution outsourced, 10-15% of the corporate workforce cut — real change, not resistance |

---
## 9. CONTROL, RELATED PARTIES, MANAGEMENT

**Control.** Class B = 286,756,831 shares at FY2025 year-end × 10 votes = **96.5% of total
voting power**; Class A holders (the public) hold ~3.5%. Every >5% beneficial owner in the
DEF 14A (acc. 0001308179-26-000050, filed 2026-03-11) is a Haas family member or family fund:
Margaret E. Haas 14.3% of total voting power, Mimi L. Haas 13.9%, Robert D. Haas 12.3%,
Peter E. Haas Jr. Family Fund 8.0%, Daniel S. Haas 8.0%, Jennifer C. Haas 7.1%,
Bradley J. Haas 6.8%. *(Trust co-trusteeships mean these entries may overlap; the structural
96.5% figure is the safe one.)*

Class B converts 1-for-1 into Class A, so **economics are identical across classes.** Class B
is not listed and not publicly traded (81 holders of record of Class A; 240 of Class B).
Family members have organized a **family council** which "engages with us on topics of mutual
interest" (10-K Item 1). **No controlled-company NYSE exemption claim was found in the
documents read** *(absence-claim wording: no instance found, not "none exists").*

The 10-K states the consequence in its own words: *"these stockholders could cause our company
to take actions that are at odds with the investment goals or interests of institutional,
short-term or other non-controlling investors"* and *"we might be a less attractive takeover
target."*

**Related-party transactions, FY2025 (DEF 14A):** the 2019 registration rights agreement with
Class B holders; indemnification agreements with directors and officers; and a **$5.7M
donation to the Levi Strauss Foundation**, on whose board the CEO, the General Counsel and
director Daniel Geballe sit. The proxy states there were no other transactions above the
$120,000 threshold. Nothing extractive found.

**Management.** Michelle Gass joined as President in January 2023 and became CEO in January
2024, succeeding Chip Bergh (12 years). **Harmit Singh, CFO since 2013, announced his
retirement in the Q1 FY2026 release (2026-04-07) after a planned transition** — a second
senior change inside the window. Compensation (Summary Compensation Table, FY2025):
Gass total **$16.15M** (salary $1.475M, stock $8.13M, options $3.14M, non-equity incentive
$3.03M, other $0.36M); FY2023 was **$36.43M** including an $8.1M signing bonus and $14.29M of
make-whole equity. Singh FY2025 total $6.05M. Not low; the incentive component does move with
performance; no extraction pattern found.

**Auditor:** PricewaterhouseCoopers LLP. Unqualified opinion including internal control over
financial reporting. One critical audit matter: the annual Beyond Yoga trademark impairment
assessment. Item 3 Legal Proceedings discloses ordinary-course claims only, none believed
material. No restatement found in the filings read.

---
## 10. BALANCE SHEET AND STAYING POWER — the filed facts

| | FY2025 (2025-11-30) | Q2 FY2026 (2026-05-31) |
|---|---|---|
| cash and equivalents | $757.9M ($591.9M held by foreign subs) | $849.3M ($717.1M foreign) |
| short-term investments | $90.9M | $128.5M |
| total debt | $1,039.2M, **100% fixed rate**, unsecured | same structure |
| net debt | **~$190M** | ~$62M |
| revolver | $1.0bn, **undrawn**, $875.4M unused availability, matures **2029-11-08** | undrawn, $820.9M unused |
| total liquidity | ~$1.7bn | ~$1.8bn |
| debt maturities | 4.000% €475M notes due **August 2030**; 3.50% notes due **2031** | same |
| operating leases | PV $1,266.3M; undiscounted **$1,449.6M**; FY2026 due $304.8M; WA term **6.7 yrs** at 4.34% | — |
| finance leases | $95.8M undiscounted at 7.87% | — |
| operating lease cost incl. variable and short-term | **$411.7M** (6.6% of revenue) | — |
| other commitments | Levi's Stadium naming rights **~$280M through 2043** | — |
| equity | $2,278.6M (goodwill $280.6M + intangibles $194.4M; deferred tax assets $830.1M) | — |

Covenants: the notes are unsecured with customary covenants; the revolver has a **springing**
1.0x fixed-charge coverage ratio that arises only if availability falls below a specified
threshold — nowhere near. Cross-default threshold $50.0M.

Coverage test [E2-54], capex charged first: (OCF $529.6M + interest $48.6M) − maintenance
capex $206.3M = $371.9M against $48.6M of interest = **7.7x**; on the five-year mean OCF it is
~8.4x.

Supplier finance program: confirmed obligations outstanding $136.5M at FY2025 year-end,
$145.1M at 2026-05-31, inside accounts payable; typical supplier terms 90 days.

---
## 11. SOURCES

- **LEVI FY2025 Form 10-K**, year ended 2025-11-30, filed 2026-01-28, **acc. 0000094845-26-000008**
- **LEVI Q2 FY2026 Form 10-Q**, quarter ended 2026-05-31, filed 2026-07-08, **acc. 0000094845-26-000037**
- **LEVI DEF 14A**, filed 2026-03-11, **acc. 0001308179-26-000050**
- LEVI FY2024 10-K acc. 0000094845-25-000005 · FY2023 10-K acc. 0000094845-24-000010 ·
  FY2021 10-K acc. 0000094845-22-000010 · 2018 10-K acc. 0000094845-19-000006
- LEVI Form 424B4 (IPO prospectus) filed 2019-03-21, **acc. 0001193125-19-082264** — the
  ten-for-one split
- Earnings 8-K Ex-99.1: 2024-01-25 acc. 0000094845-24-000011 · 2025-01-29 acc. 0000094845-25-000006 ·
  2026-01-28 acc. 0000094845-26-000009 · 2026-04-07 acc. 0000094845-26-000021 ·
  2026-07-08 acc. 0000094845-26-000038
- Kontoor Brands FY2025 10-K acc. 0001760965-26-000014 · VF Corp FY2026 10-K acc. 0000103379-26-000030 ·
  Ralph Lauren FY2026 10-K acc. 0001628280-26-037074
- SEC XBRL `companyfacts`, CIK 0000094845 (and 0001760965, 0000103379, 0001037038)
- **FRED `DGS30`** (`fredgraph.csv`), USD 30-year Treasury constant maturity: **5.19%, 2026-08-27**
- Live quote: Yahoo Finance, **aggregator, live quote only, flagged** — $21.29 NYSE close
  2026-08-28; $20.86 intraday 2026-08-31; 52-week range $17.72–$25.70
