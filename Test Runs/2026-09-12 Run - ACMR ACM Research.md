# Company Run — ACM Research, Inc. (ACMR) — 2026-09-12
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

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
- rate **5.35 %** · date **2026-09-11** · source **US Treasury daily par yield curve, 30-year
  constant maturity, issuing authority** (`home.treasury.gov` daily_treasury_yield_curve CSV,
  2026 file; struck by this run, not inherited — the 2026-09-12 print was not yet published at
  the time of the strike, so 09-11 is the currently observed rate. 09-10 was 5.37%, 09-09 5.28%.)
- **Earnings currency is NOT the reporting currency.** ACM Research reports in USD, but
  **99.63% of FY2025 revenue was earned in mainland China** ($897,978k of $901,309k, 10-K
  Item 7 geographic table) and substantially all costs are RMB. The USD sovereign is used
  because the security, the quote and the financial statements are USD and the group's
  intra-group settlements run through USD — **stated as a limitation, not resolved**: an RMB
  sovereign would be the truer discount reference for the operating cash flows, and the
  CGB 30-year is not on this project's three-sovereign list. This does not move the verdict
  (see Q4: owner earnings are negative in every construction, so no rate saves it).
- FX if the quote and the earnings differ in currency: **RMB/USD translation is inside the
  filed statements**; no ADR ratio — ACMR is a Delaware registrant on Nasdaq, not an ADR.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K FY2025**, period 2025-12-31, filed **2026-03-02**, accession **0001628280-26-013231**
    (primary doc `acmr-20251231.htm`) — read: Item 1 Business, Item 1A Risk Factors (regulatory
    and international), Item 7 MD&A in full including the non-GAAP section, the consolidated
    statements, and notes 1, 2, 3, 8, 10, 13, 14, 15, 16, **20 (parent-company-only)** and 21.
  - **10-Q Q2 2026**, period 2026-06-30, filed **2026-08-07**, accession **0001628280-26-054832**
    — cover share counts, cash-by-jurisdiction table, condensed cash-flow statement, ownership.
  - **10-Q Q1 2026** acc. **0001628280-26-032842** · **10-Q Q3 2025** acc. **0001628280-25-050152**.
  - **10-K FY2024** acc. **0001680062-25-000003** · **FY2023** acc. **0001680062-24-000008** ·
    **FY2022** acc. **0001140361-23-009508** · **FY2021** acc. **0001140361-22-007348** ·
    **FY2020** acc. **0001140361-21-006683** · **FY2019** acc. **0001140361-20-006743** ·
    **FY2018** acc. **0001654954-19-002737** · **FY2017** acc. **0001654954-18-002950**.
  - **DEF 14A 2026**, filed **2026-04-27**, accession **0001628280-26-027358**.
  - **8-K 2026-05-12**, accession **0001140361-26-020717** — Item 1.01, with EX-10.1 and EX-5.1.
  - **8-K EX-99.1 earnings releases** (the standing Q3 requirement, set by the CGNX run):
    Q2-2026 acc. **0001628280-26-054581** · Q1-2026 acc. **0001628280-26-031688** ·
    Q4-2025 acc. **0001628280-26-011998**.
  - **8-K 2026-02-06**, accession **0001680062-26-000020** — ACM Shanghai share-transfer results.
- figures cross-checked against the filed statement (three, all exact):
  1. **Gross profit.** Revenue $901,309k − cost of revenue $501,242k = **$400,067k**, equal to
     the filed "Gross profit" line to the dollar.
  2. **The non-controlling-interest split.** Consolidated net income $121,893k − NCI $27,815k =
     **$94,078k**, equal to the filed "Net income attributable to ACM Research, Inc." to the
     dollar; and $94,078k ÷ 64,184,776 weighted basic shares = **$1.4657**, matching the filed
     basic EPS of **$1.47**.
  3. **The operating-income identity used by the cohort competitor row.** Revenue − cost of
     revenue − R&D − S&M − G&A = **$109,429k**, equal to the filed "Income from operations"
     to the dollar — so the row formula is not an approximation for this filer.

**THE PRICE, RE-STRUCK, AND THE SHARE-CLASS JUDGMENT.**
- **Price $72.00**, close **2026-09-11** (Nasdaq via aggregator quote — *aggregator used for
  the live quote only, and flagged*, operator rule 5). 09-10 $72.39, 09-09 $73.83.
- **Share count off the cover of the latest periodic filing**, per the Stage-0 rule
  (`python Screens/cover_shares.py ACMR`): 10-Q filed **2026-08-07**, accession
  **0001628280-26-054832** — **Class A 64,657,388** and **Class B 4,991,808**.
- **`cover_shares.py` refused to sum them, correctly, because the question is a charter
  judgment. The charter answers it, and the answer is SUM THEM.** 10-K FY2025 note 14,
  verbatim: *"Each share of Class A common stock is entitled to one vote, and each share of
  Class B common stock is entitled to twenty votes and is **convertible at any time into one
  share of Class A common stock**. Shares of Class A common stock and Class B common stock are
  treated **equally, identically and ratably** with respect to any dividends declared."*
  **Class B is economically identical to Class A, 1-for-1 convertible, and differs only in
  votes (20:1).** The economic count is therefore **69,649,196**.
- **MARKET CAP = 69,649,196 × $72.00 = $5,014.7M.** The queue row carried **$2,979M**. **The
  queue cap was too small by 40.6% — the real cap is 1.68x it** — the ninth of ten checks and
  the ninth miss. The cause is **not** a share-class artifact this time: the count is roughly
  right and **the price has re-rated** (the May 2026 registered direct offering priced at
  $52.00; the quote is $72.00).
- Class B is **7.2% of the economic capital and 60.7% of the votes** (4,991,808 × 20 =
  99,836,160 votes against 64,657,388 Class A votes). Recorded here; read at Q3.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.**
ACM Research builds machines that wash silicon wafers, and a widening set of machines that do
other single-wafer chemical and thermal steps. A fab buys a tool for **$0.5M to more than $5M**
(10-K Item 1, filed range), qualifies it against a named process step, and then buys more of the
same tool as it adds capacity. The company is paid per box. **It delivered >315 tools in FY2025
and booked $901.3M**, so the average delivered tool carried about **$2.9M** of revenue. Gross
margin has sat in a **44.2%–50.1% band for ten filed years** and was **44.4% in FY2025**. Below
that line the money goes out again: **R&D 16.1% of revenue** and **SG&A 16.2%**, leaving a
**12.1% operating margin**. Everything above is the consolidated group.

**The part that is not ordinary, and it is the whole file.** ACM Research, a Delaware company in
Fremont, California, is a **holding company whose operations are a separately listed Chinese
subsidiary**. ACM Research (Shanghai), Inc. trades on the Shanghai STAR Market as **688082.SS**.
The 10-K states the perimeter in its own words: *"ACM Research has a direct ownership interest in
ACM Shanghai as the result of its holding **74.6%** of the outstanding shares of ACM Shanghai.
**Stockholders of ACM Research may never directly own equity interests in ACM Shanghai.**"*
(10-K FY2025, page 3.) At **2026-06-30 the holding is 73.2%** (10-Q Q2-2026). It is **not** a
VIE — the 10-K says so expressly, and that is a real distinction from the China-ADR class — but
the economic consequence is the same arithmetic: **a dollar of operating cash earned in Shanghai
is not a dollar of owner earnings for an ACMR holder.**

**How much of it belongs to ACM Research shareholders — the filed answer, not an estimate.**

| year | consolidated net income | NCI | **attributable to ACM Research** | **ACMR share** |
|---|---|---|---|---|
| 2019 | $19,458k | $564k | $18,894k | 97.1% |
| 2020 | $21,677k | $2,897k | $18,780k | 86.6% |
| 2021 | $42,921k | $5,164k | $37,757k | 88.0% |
| 2022 | $50,564k | $11,301k | $39,263k | 77.7% |
| 2023 | $96,852k | $19,503k | $77,349k | 79.9% |
| 2024 | $131,269k | $27,642k | $103,627k | 78.9% |
| **2025** | **$121,893k** | **$27,815k** | **$94,078k** | **77.2%** |

Balance sheet, same date: **NCI $466,146k of $1,930,509k total equity (24.1%)**; ACM Research
own stockholders equity **$1,464,363k (75.9%)**. **So roughly 77–78 cents of every dollar of
consolidated economics is ACMR's, and that fraction has fallen in six of the last seven years.**
This is the GHC problem named in the brief, and it is resolved here rather than missed: the
distortion is **not** a mandatorily redeemable instrument, it is **ordinary minority interest in
a listed subsidiary that keeps issuing its own shares** — which is why it appears as a *falling
percentage* rather than as a liability. The dilution mechanism is read at Q3; the arithmetic is
applied to owner earnings at Q4.

**The scarce input this business controls.** Filed, and it is narrow: **594 issued patents**
across six jurisdictions, of which **82 are US**, with 66 international grants on SAPS, 13 PCT
applications on TEBO and 8 on Tahoe; and the **qualified position inside a named process step at
a named fab**, which the 10-K describes as sticky in its own words — *"Once a semiconductor
manufacturer has selected a particular supplier's equipment and qualified it for production, the
manufacturer generally maintains that selection for that specific production application and
technology node."* **The scarce input is the qualification slot, not the technology**, and the
10-K says in the next breath that the same mechanism works against ACM: *"we may experience
difficulty in selling to a given manufacturer if that manufacturer has qualified a competitor's
equipment."* A two-way switching cost is a weaker asset than a one-way one. Note also where the
intellectual property sits: *"The significant majority of our intellectual property has been
developed in mainland China and is **owned by ACM Shanghai**"* — the scarce input is an asset of
the subsidiary, not of the registrant.

**A physical series exists, and this is worth recording because the cohort had none [E4-55].**
The runs on KLAC, AMAT and LRCX found no unit series; ACLS filed a cumulative ~3,400 tools. **ACM
Research files a cumulative tool count in Item 1 of every 10-K**, so a delta series is available:

| filing | cumulative tools delivered since 2009 | revenue-generating | **annual delta** |
|---|---|---|---|
| FY2019 | >80 *(single-wafer wet cleaning only)* | >65 | — |
| FY2020 | >135 *(scope widened: "wet cleaning and other front-end")* | >120 | **+55** |
| FY2021 | >225 | >185 | **+90** |
| FY2022 | >380 | >290 | **+155** |
| FY2023 | >765 *(scope widened again: "tools")* | >650 | **+385** |
| FY2024 | >1,120 | >920 | **+355** |
| FY2025 | >1,435 | >1,255 | **+315** |
| Q2-2026 | >1,590 | >1,430 | **+155 in six months (~310 annualised)** |

**Limit stated before the reading:** the counts are "more than" figures, rounded, and the
definition widened twice (FY2020 and FY2023), so FY2019–FY2022 are not strictly comparable with
what follows. **FY2023 onward is one stable definition, and on it the physical series peaked in
FY2023 and has fallen every year since: 385 → 355 → 315 → ~310.** Over the same stretch dollar
revenue rose from $557.7M to $901.3M and is guided to $1.125–1.175bn. **Revenue per delivered
tool: $1.449M (2023) → $2.203M (2024) → $2.861M (2025) → ~$3.7M implied at the 2026 guide.**
That is either a genuine climb into more expensive platforms — ECP/furnace/PECVD/Track list above
a cleaner, and the ECP-and-other line did grow 32.1% in 2025 — or it is **[E4-55]**'s Precision
Steel pattern, *"a serious reverse, not likely to disappear in some 'bounce back' effect,"* with
dollar revenue flattered while the physical count goes the other way. **Both readings are live;
the series is carried to Q2 as the direction test [E4-32] and to Q6 as the monitoring metric**,
rather than resolved here, because Q1 asks whether I understand the machine, and I do.

**Will the fundamentals look broadly the same in ten years?**
Partly, and the honest answer separates two things. **Wafers will still need washing, and single
wafer wet cleaning will still be bought per box** — the process step is as durable as any in the
industry and the 10-K addressable-market frame ($7.3bn cleaning inside a $21bn served WFE pool)
is credible on its face. **What will not look the same is this company's perimeter.** Four filed
facts say so: the listed subsidiary's share count changes on the Shanghai exchange's timetable,
not ACMR's (81.5% → 74.6% → 73.2% in nineteen months); **99.63% of revenue is earned in one
country whose WFE spend Gartner puts at −1.7% in 2025 and −9.9% forecast for 2026** while the
world grows 11.8%; both principal operating subsidiaries have been on the **BIS Entity List since
2024-12-02**; and the auditor is a mainland China firm, which puts an HFCAA delisting path on the
page. **None of that makes the business unintelligible** — every one of those facts is a filed
fact with a date — and [E4-46] is the right test: this is *"a named filing inside an understood
business,"* not a business that would take months of study. The machine is simple. The claim on
it is complicated, and the complication is **measured**, not guessed.

**VERDICT: [x] IN** — the unit economics are legible per box, the scarce input is named, the
attribution to ACMR's own owners is a filed number rather than an estimate, and a physical unit
series exists. The perimeter is complex but it is **disclosed and quantified**, which is the
distinction [E3-31] draws between a business that is *complex* and one that is *unknowable*.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**Pre-registered before the row was computed** (operator rule 9): my prior is **OUT**, and the
reason I expected is **the customer list, not the technology**. Framed to be refuted **[E4-26]**,
that prior fails if (a) the returns on capital employed sit inside the cohort rather than below
it, (b) gross margin held through the 2024-12-02 Entity List designation, or (c) customer
concentration and the one-country exposure are falling. **All three test results arrived:
(a) and (b) went with the prior, and (c) went partly against it** — see the concentration table.

### THE BULL CASE, BUILT FIRST AND AS STRONGLY AS THE FILINGS ALLOW

1. **Real, patented, differentiated process technology.** 594 issued patents, 82 in the US,
   66 international grants on SAPS alone. TEBO is filed as demonstrated damage-free on 1xnm
   patterned wafers and on 3D structures at 60:1 aspect ratio. Tahoe is filed as using
   *"significantly less sulfuric acid and hydrogen peroxide."* This is not a me-too box.
2. **The demo-to-sales engine works, on the filed count.** Of >1,435 tools delivered, >1,255
   are repeat orders or accepted first tools; at Q2-2026, >1,430 of >1,590. A first tool that
   is evaluated for up to 24 months and then reordered is the qualification lock-in the 10-K
   describes.
3. **Growth that no cohort peer matched.** Revenue **$74.6M (2018) → $901.3M (2025)**, a
   **43% compound rate for seven years**, and H1-2026 revenue **$524.2M, +35.2%** on H1-2025,
   with FY2026 guided to **$1.125–1.175bn**.
4. **A decade of gross margin inside the incumbents' band.** ACMR **44.2%–50.1%** (2016–2025)
   against AMAT **41.7%–48.7%** and LRCX **44.5%–50.5%** over the same years (cohort table
   below). On the gross line alone, ACM prices like Applied and Lam, and **above** Axcelis
   (37.3%–44.9%) in every year.
5. **Export controls protect the home market.** The Western incumbents need licences,
   *"reviewed under a presumption of denial"* (10-K Item 1A), for the advanced end of the
   Chinese market. A domestic supplier inside that wall is shielded from the competitors that
   matter most.
6. **Customer concentration has broadened — this is the disconfirming datum for my prior.**

| period | concentration, filed | source |
|---|---|---|
| 2018 | three customers **87.6%** | 10-K FY2020 Item 1A |
| 2019 | three customers **73.8%** | 10-K FY2020 Item 1A |
| 2020 | three customers **75.8%** | 10-K FY2020 Item 1A |
| 2021 | two customers **48.9%** | 10-K FY2022 note 2 |
| 2022 | three customers **43.8%** | 10-K FY2022 note 2 |
| 2023 | three customers **45.5%** (17% · 15% · 13%) | 10-K FY2025 note 2 |
| 2024 | four customers **52.2%** (15% · 14% · 12% · 12%) | 10-K FY2025 note 2 |
| 2025 | four customers **52.2%** (17% · 14% · 12% · 10%) | 10-K FY2025 note 2 |
| Q2-2025 (three months) | four customers **66.5%** | 10-Q Q2-2026 note 2 |
| **H1-2026** | **one customer 12.7%** — no other above 10% | 10-Q Q2-2026 note 2 |
| accounts receivable | four customers **62.2%** (2025-12-31) → **52.4%** (2026-06-30) | 10-Q Q2-2026 |

**Read honestly: concentration fell by half from 2018 to 2022, rose back to 52% in 2024–25,
and in H1-2026 broadened to a single 10%-plus customer.** That is a genuine improvement in the
most recent period and it is recorded against my prior. **What it does not change** is that
every one of those customers is in one country — the next test.

### NOW THE ATTACK

**[E3-03] criterion (2) — "thought by its customers to have no close substitute." FAILS, on
the filing's own words.** The 10-K names the substitutes: *"We consider our principal
competitors to be those companies that provide wafer cleaning, electrical plating and furnace
products to the global market, including **Lam Research Corporation, NAURA Technology Group
Co., Ltd., SCREEN Holdings Co., Ltd., SEMES Co. Ltd., Tokyo Electron Ltd. and Kokusai
Semiconductor Equipment Corporation.** Principal competitors for our PECVD and Track products
also include Lam Research Corporation, **Applied Materials, Inc., and Suzhou Jingtuo
Semiconductor Technology Co., Ltd.** We also face **additional competitors based in mainland
China across multiple product lines due in part to the recent entrants of local equipment
suppliers**."* And it concedes the terms of the contest: those competitors *"may have …
**multiple product offerings, which may enable them to offer bundled discounts for customers
purchasing multiple products or other incentives that we cannot match or offer**."* **Eight
named substitutes plus unnamed new domestic entrants, and a filed admission of being out-bundled,
is the opposite of no close substitute.** The qualification slot is sticky, but the 10-K's own
sentence makes it a two-way door (Q1).

**[E3-46] — the second question about the business is a number, and on the cohort's own
formula ACMR is last.** Row built by the KLAC run of 2026-09-07 and carried by AMAT and LRCX:
**OP = revenue − cost of revenue − R&D − SG&A**; **ROUNTOA = OP ÷ (assets − goodwill −
intangibles − non-interest-bearing current liabilities)**, year-end — *a CONVENTION of the row,
[E2-43] in the closest computable form*. **ACMR's cells were computed in this run from the
FY2025 10-K (acc. 0001628280-26-013231) and the OP identity matches the filed "Income from
operations" of $109,429k to the dollar.** All other cells are **reused, not rebuilt**, from the
named precedent runs, per the brief.

### THE COMPETITOR ROW — required [E3-28]

| latest FY | **ACMR** | KLAC | LRCX | AMAT | ASML | ONTO | ACLS | VECO |
|---|---|---|---|---|---|---|---|---|
| period end | **12/31/25** | 6/30/26 | 6/28/26 | 10/26/25 | 12/31/25 | 1/3/26 | 12/31/25 | 12/31/25 |
| form · accession | **10-K `0001628280-26-013231`** | 10-K `0000319201-26-000027` | 10-K `0000707549-26-000037` | 10-K `0001628280-25-056742` | 20-F `0001628280-26-011378` | 10-K `0001193125-26-066937` | 10-K `0001104659-26-020461` | 10-K (per ACLS run) |
| revenue | **$901.3M** | $13,579.5M | $23,232.7M | $28,368.0M | €32,667.3M | $1,005.3M | $839.0M | $664M |
| gross margin | **44.4%** | 61.3% | 50.5% | 48.7% | 52.8% | 49.7% | 44.9% | n/c |
| R&D % revenue | **16.1%** | 11.3% | 10.2% | 12.6% | 14.4% | 13.1% | 13.0% | n/c |
| SG&A % revenue | **16.2%** | 8.3% | 4.9% | 6.2% | 3.9% | 17.6% | 17.7% | n/c |
| **operating margin** | **12.1%** | 41.7% | 35.3% | 29.9% | 34.6% | 19.0% | 14.2% | 5.4% |
| **ROUNTOA** (cash in denominator) | **4.9% ← last** | 48.5% | 52.0% | 34.5% | 49.4% | 15.7% | 10.2% | n/c |
| ex-cash return on NTOA | **10.3%** | 56.9% | 81.1% | 73.9% | n/c | n/c | n/c | n/c |
| service/spares % revenue | **≤8.4% ← last** *(blended with adv. packaging tools; no service line filed)* | 23.0% | 35.9% | 22.5% | 25.1% | 15.7% | 31.9% | n/c |
| China % revenue | **99.6% ← highest by 3x** | 29.8% | 33.8% | 30.1% | 29.1% | 7% | n/d | n/c |

*n/c = not computed in any precedent run; n/d = not disclosed. ASML is left in EUR as the
precedent rows left it — margins and ratios comparable, levels not. ACMR's ROUNTOA denominator
is $2,232,749k (assets $2,872,185k − intangibles $2,847k − non-interest-bearing current
liabilities $636,589k); the ex-cash denominator further removes cash $757,373k, restricted cash
$8,589k, short-term time deposits $366,591k and short-term investments $35,524k = $1,064,672k.
The cash-in figure is depressed by the $623.0M ACM Shanghai raised in September 2025, which is
why both are shown; **on either denominator ACMR is last among the filers computed.***

**Gross margin through the downturns and the Entity List — the [E2-44] test, ten filed years, same
formula** (ACMR computed here from each 10-K's filed gross profit and revenue, newest vintage;
the other columns carried from the LRCX run's table):

| FY | **ACMR** | KLAC | LRCX | AMAT | ASML | ONTO | ACLS |
|---|---|---|---|---|---|---|---|
| 2016 | **48.7** | 61.0 | 44.5 | 41.7 | 45.7 | 51.6 | 37.3 |
| 2018 | **46.2** | 64.2 | 46.6 | 45.0 | 46.0 | 54.2 | 40.6 |
| 2019 ↓ | **47.1** | 59.1 | 45.1 | 43.7 | 44.7 | 44.1 | 42.0 |
| 2020 | **44.4** | — | — | — | — | — | — |
| 2021 | **44.2** | 59.9 | 46.5 | 47.3 | 52.7 | 54.4 | 43.2 |
| 2022 | **47.2** | 61.0 | 45.7 | 46.5 | 50.5 | 53.6 | 43.7 |
| 2023 ↓ | **49.5** | 59.8 | 44.6 | 46.7 | 51.3 | 51.5 | 43.5 |
| 2024 ↓ | **50.1** | 60.0 | 47.3 | 47.5 | 51.3 | 52.2 | 44.7 |
| **2025 — first full year on the Entity List** | **44.4 (−5.7)** | 60.9 | 48.7 | 48.7 | 52.8 | 49.7 | 44.9 |
| H1-2026 | **46.1** | 61.3 | 50.5 | — | — | — | — |

- Peers named: **8 SEC filers in the row** (KLAC, LRCX, AMAT, ASML, ONTO, ACLS, VECO, plus
  ACMR) against **the nine competitors ACM names itself** (Lam, NAURA, SCREEN, SEMES, TEL,
  Kokusai, Applied, Suzhou Jingtuo, and "additional competitors based in mainland China").
  **Of ACM's nine named competitors, only Lam and Applied are SEC registrants** — two of nine.
- Any peer unavailable? **Yes, seven of nine, and the limit is stated rather than papered.**
  **SCREEN Holdings and Tokyo Electron** (Japan): no SEC periodic reports; SCREEN appears only as
  an unsponsored ADR (recorded by the LRCX run), and the EDINET rung is blocked by a paid key —
  the framework's own ladder names that obstacle. **SEMES** is a Samsung subsidiary with no
  separate filing. **Kokusai** is TSE-listed with no SEC filing. **NAURA** (SZSE 002371) and
  **Suzhou Jingtuo** file only on Chinese exchanges, in Chinese. **Adjudication, under the rule
  set by the ACLS run and carried by KLAC, AMAT and LRCX: an additional competitor can only
  narrow a moat, never widen one.** The subject is already last in the computed row on returns
  and on service mix, so no unpriced peer can lift it to IN — a stronger SCREEN or NAURA only
  widens the gap. **The gap is recorded as a row limit, not as PROVISIONAL**, because no outcome
  of the fetch moves the verdict (the PLAB rule).
- **[E3-61] limit:** the row shows position, not conduct. On conduct, ACM's filed statement is
  that it competes by *"providing custom-made, differentiated equipment that incorporates
  customer-requested features at a **competitive price**"* — a price-taker's sentence.

**[E2-44] — both halves, and both fail.**
- **Half one: raise prices "even when product demand is flat and capacity is not fully
  utilized."** Demand was **not** flat in FY2025 — revenue rose **15.2%** — and gross margin
  still fell **570 basis points, 50.1% → 44.4%**, in the first full year after ACM Shanghai
  and ACM Korea were named to the BIS Entity List (effective **2024-12-02**). The 10-K attributes
  it to *"revenue mix between product categories, and a higher provision for inventory."* The
  inventory provision rose from $2,796k to $15,485k, **1.4 points of revenue**, so **about 4.3
  points of the decline survive removing it entirely**. **A business that cannot hold margin
  while its revenue is growing has no pricing power to test in a flat year.** Against the cohort
  the direction is the tell: **in FY2025 KLAC, LRCX, AMAT, ASML and ACLS all held or raised
  gross margin; only two filers in the row fell — ONTO by 2.5 points and ACMR by 5.7, more than
  twice as far.**
  And the company's own yardstick concedes the ceiling: the releases state *"ACM's long-term
  business model target range of 42% to 48%"* — **a filed target whose top sits two points below
  what the business actually earned in FY2024.**
- **Half two: grow dollar volume "with only minor additional investment of capital."** From
  FY2018 to FY2025 revenue rose **$826.7M**. Over the same years the business consumed:
  **$318.9M of capex and intangibles**, inventories that now stand at **$702.6M** and receivables
  at **$504.3M**, and **cumulative operating cash of −$32.7M** — eight years of operations that,
  before a dollar of capex, **took in less cash than they paid out**. The balance sheet was
  refilled from outside: **$623.0M raised by ACM Shanghai in September 2025** and **$148.4M net
  raised by ACM Research in May 2026**. That is the opposite of minor additional investment.

**[E2-59] — the moat belongs to the regime, and the filing says so without saying so.**
- **99.63% of FY2025 revenue from mainland China** ($897,978k of $901,309k), and **"Other
  Regions" revenue is falling, not rising: $16,754k (2023) → $6,366k (2024) → $3,331k (2025)**
  — the globalization story told in the releases runs the other way in the filed table.
- The 10-K's own attribution of FY2025 growth: *"a longer-term commitment by our mainland
  China-based customers to increase production capacity **to achieve a greater share of the
  global semiconductor market**"* — the customers' capex is a stated national-share objective,
  which is a policy variable by definition.
- The same 10-K cites Gartner that **China WFE fell 1.7% in 2025 and is forecast to fall 9.9%
  in 2026**, against global WFE +11.8%. The regime that floored the demand is contracting its
  own spend while ACM guides +25–30%.
- **Government grants credited to R&D: $8.0M (2025), $0.5M (2024), $1.7M (2023)**, plus
  **$1.4M / $2.0M / $0.4M** credited to other income; ACM Lingang received **$10.3M in cash
  grants in 2025**. A 5% holder of the US parent is **Shanghai Pudong Innotek Capital Co., Ltd.**
  (3,358,728 Class A, 13D/A of 2024-10-29), a Pudong New Area investment vehicle.
- **The export wall that protects ACM from Lam and Applied at the advanced end is the same wall
  that put ACM Shanghai on the Entity List.** *"These new restrictions have impacted the
  procurement by ACM Shanghai and ACM Korea of items, technology and software from the United
  States … **we believe these regulations may directly impact ACM Shanghai's ability to meet its
  future production plans**."* The regime gives the market and the regime takes the supply
  chain. [E2-59]'s own ending — *"That day is gone"* — is on a timetable set in Washington,
  Tokyo, The Hague and Beijing, none of which is ACM's.

**Export-control exposure, with dates, and what it is NOT.** October 2022: BIS rules expanding
SME controls to China. 2023-05-23: Japan ordinance, effective 2023-07-23. 2023-09-01: the
Netherlands regulation in force. **2024-12-02: ACM Shanghai and ACM Korea added to the BIS Entity
List** — *"prohibit any party worldwide from furnishing hardware, software, or technologies that
are subject to U.S. export controls jurisdiction directly or indirectly to ACM Shanghai or ACM
Korea without obtaining authorization."* December 2025: Dutch supplemental controls. April 2025:
US tariffs on China at 145%. **What happened when the rule changed: revenue grew 15.2% and gross
margin fell 5.7 points in the first full year.** *Per the brief, AMAT's run found a $253M BIS
settlement with a suspended denial order; **ACMR's position does not resemble it and is in one
respect worse**: AMAT was an exporter facing enforcement for shipments it made; ACM Shanghai is a
**designated party** that the rest of the world may not supply. No penalty, settlement or denial
order against ACMR was found in any document read.*

**The service annuity — AMAT's finding applied BY ANALOGY, and labelled as one.** ACMR files no
service line. The smallest filed bucket, *"Advanced packaging (excluding ECP), services &
spares,"* is **$75.8M, 8.4% of FY2025 revenue** — and it includes advanced-packaging tools, so
services and spares are **at most** 8.4%. The cohort: LRCX 35.9%, ACLS 31.9%, ASML 25.1%, KLAC
23.0%, AMAT 22.5%, ONTO 15.7%. **The installed-base annuity that carries the incumbents through
a downturn is essentially absent here.** *By analogy only:* AMAT's run killed the annuity claim
for the cohort by finding service gross margin of 33.4% against 54.2% for systems — i.e. even
where the annuity exists it is not the high-margin leg. **ACMR is not evidence against or for
that finding; it simply does not have the leg the finding was about.** A 1,435-tool installed
base is small beside the incumbents' and young, so the spares tail has not yet had time to form.
That last clause is the honest bull reading of the gap, and it is a forecast, not a fact.

**[E4-04] — must the moat be continuously rebuilt, and is the spending defending the same
advantage or buying its replacement?** R&D is **16.1% of revenue, the highest in this row**
(only Nova, at 16.3% in the precedent KLAC/LRCX rows, is higher), and the filed use of it is **four new product categories** —
furnace, PECVD, Track, panel-level plating — whose *"platforms are at earlier stages of customer
evaluation and adoption."* **That is the replacement test failing:** the spend is buying new
franchises to be, not deepening the cleaning slot. **Direction [E4-32]:** units down three
straight years (385 → 355 → 315 → ~310 annualised), gross margin down 5.7 points, Other Regions
revenue down 80% in two years; concentration broadening in H1-2026 is the one favourable datum.
**Net: NARROWING on the filed numbers.**

**[E4-23] — key-person dependence, recorded here as a moat defect, not at Q3 as a strength.** The
10-K: *"We are **highly dependent on our Chief Executive Officer and President** … Dr. David H.
Wang"*, with *"no employment or retention agreements with, or maintain key person life insurance
policies on, any of our employees."* And the same risk factor names the perimeter's second
dependency: *"ACM Shanghai is now managed by a group of officers separate from those of ACM
Research and **those officers owe fiduciary duties to the various stakeholders of ACM
Shanghai**."* The people running the business an ACMR holder pays for owe their duties to a
different register.

**Untapped pricing power [E3-33, E5-28]?** **Not claimed.** Claiming it would claim near-monopoly;
nine named competitors, a filed bundled-discount concession and a margin that fell while revenue
grew refute the class. **[E2-53] dominance? No.** **[E4-36] — which cause of success does the
record come from?** **Wave-riding [E3-51]**: the 43% revenue compound rate is China's domestic
fab build-out behind an export wall, and the filed attribution is the customers' national-share
objective. *"The advantage lives in the wave, not the surfer."*

**The attacker's test [E2-45]** — how would I compete with it, with ample capital and skilled
people? **The answer is already filed: NAURA and Suzhou Jingtuo are doing it**, inside the same
wall, with the same policy tailwind, and the 10-K calls them *"recent entrants of local equipment
suppliers."* A Western incumbent cannot attack ACM in China; a Chinese one can, and is.

- Needed or desired **[x]** · no close substitute **[ ] — fails, nine named substitutes** · not
  price-regulated **[x] — but demand is policy-set [E2-59]**
- Must the moat be continuously rebuilt? **Yes — R&D buys replacement categories, not defence
  of the cleaning slot [E4-04].** Depends on a great manager? **Filed as yes [E4-23].**
- Primary moat metric and trend: **ROUNTOA 4.9% (10.3% ex-cash), last in the row; gross margin
  −5.7 points in FY2025 against a cohort that held; units falling three years.**
- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: NARROWING**

**Why NONE and not NARROW — the difference from ACLS, which cleared Q2 as NARROW, stated so it
can be attacked.** ACLS was the cohort's lowest-return filer and still cleared, because (i) its
customers cannot make an implanter and there was no captive threat, (ii) its filed price range
rose through the bust, (iii) 31.9% of revenue was an installed-base aftermarket, and (iv) its
China exposure sat inside a diversified customer list. **ACMR fails every one of those four
distinctions**: domestic competitors are named in its own 10-K; its gross margin fell while
revenue grew; its service leg is at most 8.4%; and 99.6% of its revenue is one policy regime.
**And it earns half of ACLS's return on the row's own formula** (4.9% against 10.2%).

**VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**OUT, on the business.** The evidence is here and the business fails the franchise test on four
independent grounds, each from a filed document: criterion (2) fails on ACM's own list of nine
substitutes and its bundled-discount concession **[E3-03]**; the return on capital employed is
last in the cohort **[E3-46]**; both halves of the two-characteristic test fail — margin fell
while demand grew, and growth consumed more capital than eight years of operations produced
**[E2-44]**; and the demand is a policy variable of a single regime that is simultaneously the
subject's customer base, subsidy source and — through the counter-regime — its supply-chain
constraint **[E2-59]**. **The file closes here.** *(Asked aloud: can I name a document that would
move this? The SCREEN, TEL and NAURA filings would only narrow a moat already rated NONE. No.)*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

⚠️ **RECORDED, NOT GOVERNING. Q2 returned OUT and the file closed there.** This section is built
because the brief asked for it — and specifically for the related-party read on the Shanghai
subsidiary — and because a Q2 OUT written without reading the manager record would be an
opinion. **Nothing here promotes anything; per the guardrail a strong Q3 cannot repair Q2
[E2-37, E2-38, E3-39].** The brief's warning is taken literally: no gate was assumed short, and
Q3 turned out to carry the file's most structural finding.

**STEP 1 — DECLARE THE WEIGHT CASE.** *How much damage can this manager do before I can react?*
- [x] **Daily execution — ticked, and the reason is [E3-43], not [E3-38].** This is not a
      promises business. But Q2 found **no franchise**, and the 1991 original is exact:
      *"franchises can tolerate mis-management … **a business, unlike a franchise, can be killed
      by poor management**."* A business that must win a qualification slot tool by tool, ramp
      four new product categories at once, re-source a supply chain around an Entity List
      designation, and run two share registers on two exchanges is a have-to-be-smart-every-day
      business.
- [ ] **Control [E1-16]** — not ticked; a marketable Class A share, exitable. *Recorded the
      other way round because it matters:* the outside holder has **no** control — Dr. David H.
      Wang holds **57.2% of total voting power** on 14.4% of the Class A as converted, and
      officers and directors as a group hold **64.5%** (DEF 14A 2026, beneficial-ownership table).
- [ ] **Leverage [E3-29]** — not ticked. Assets $2,872,185k on total equity $1,930,509k, **1.49
      to 1**; bank borrowings $288,053k against $1,132,553k of cash and deposits.

**One ticked → Q3 is a BINARY GATE and no price compensates [E1-16, E3-29, E5-35].**

### HONESTY — binary, filings-based, each matter dated to when it became PUBLIC [E5-16]

| date public | matter | what the filing says | disqualifier? |
|---|---|---|---|
| **2020-12-21** | *Kain v. ACM Research, Inc., et al.*, N.D. Cal. No. 3:20-cv-09241, Exchange Act §10(b)/20(a) against the company and three executive officers | dismissed with leave to amend **2021-09-09** and again **2021-12-20**; lead plaintiff filed a **stipulation of voluntary dismissal 2022-01-10**, *"the court granted the stipulation and dismissed the case with prejudice"* (10-K FY2021) | **No.** Twice dismissed on the pleadings, then withdrawn with prejudice. No finding. |
| **2023-03-02** (FY2022 10-K) | **Adverse opinion on internal control over financial reporting** from Armanino LLP; two material weaknesses — risk assessment and monitoring, and IT general controls *"across substantially all financial statement areas"* | the financial-statement opinion was clean; **no restatement found in any vintage read**; *"the material weaknesses have been remediated as of December 31, 2023"* (10-K FY2023); FY2025 ICFR opinion from E&Y Hua Ming is unqualified | **No — a weak-accounting PROMPT [E4-22], read and closed.** A control failure, remediated within a year, with no restated number. |
| **2023-07-27** (8-K) | **Armanino resigned**, effective 2023-09-20 | *"due to Armanino's decision to exit from the practice of providing financial statement audit services to all public companies"*; *"there were no (a) disagreements with Armanino on any matter of accounting principles"*; Exhibit 16 letters filed 2023-07-27 and 2023-09-26 | **No.** Exit from the practice, no disagreement, letters on file. |
| **2024-12-02** | ACM Shanghai and ACM Korea added to the **BIS Entity List** | a national-security designation of the subsidiary, not an enforcement finding against the registrant; **no penalty, settlement or denial order found** in any document read | **No integrity finding** — a business and perimeter fact, carried at Q2 and Q4. |

**The auditor path, recorded because it is the perimeter question in its accounting form.** BDO
China Shu Lun Pan audited ACMR through FY2021 and **could not be inspected by the PCAOB**; the
company moved to **Armanino (US)** for FY2022; Armanino left the public-company practice in 2023;
the company then engaged **Ernst & Young Hua Ming LLP, Shanghai**, a mainland China firm, from
FY2023. And **BDO China Shu Lun Pan still signs ACM Shanghai's statutory audit** — the FY2025
profit-distribution announcement cites *"Audit Report (Xin Kuai Shi Bao Zi [2026] No. ZI10018)
issued by BDO China Shu Lun Pan."* **The operating subsidiary and the US registrant are audited
by different firms under different GAAPs.** That is not a flag; it is where the next read would
start if one fired, and [E5-32] is why it is written down.

### THE FLAGS [E4-22, E5-15, E4-29] — prompts to read, and I read them

- [x] **weak accounting** — the FY2022 adverse ICFR opinion, above. **Read and closed**: remediated
  2023-12-31, no restatement. *One cockroach, and the kitchen was inspected twice since.*
- [ ] **unintelligible footnotes** — **not ticked, and the opposite holds.** Note 2's cash-by-
  jurisdiction table, the restricted-net-assets figure, the parent-only statements (note 20),
  the transfer-pricing payments by year and the dividends from ACM Shanghai to ACM Research by
  year are all filed, in plain tables. The perimeter is complicated; the disclosure of it is not.
- [x] **trumpeted earnings projections / growth targets — FIRES.** Every release carries annual
  revenue guidance, raised or maintained each quarter (**$1.08–1.175bn** in the Q4-2025 and Q1-2026
  releases, **raised to $1.125–1.175bn** in Q2-2026), and **a long-term revenue target of $4
  billion** — *"we remain committed to our long-term target of $4 billion in revenue"* (Q4-2025
  release, acc. 0001628280-26-011998); *"as we execute toward our long-term revenue target of $4
  billion"* (Q2-2026 release, acc. 0001628280-26-054581). **$4bn is 4.4 times FY2025 revenue and
  3.4 times the top of the 2026 guide.** [E5-30]: *"once you start it, it's all over. You can't
  quit."* **[E3-48]'s action, taken:** the record of the people who made the projections, on the
  documents I hold — FY2026 guidance was issued at $1,080–1,175M, held through Q1, and raised at
  the bottom end in Q2 while H1 revenue ran +35.2%. **On that short record the guide has been
  met, not missed** — recorded in management's favour. The earlier guidance record was not
  pulled, and it would not move the Q2 verdict.
- [x] **serial share issuance [E5-15] — FIRES, and at TWO registers, which is the finding.**

  **At the registrant.** Weighted basic shares, split-adjusted (three-for-one, effected March 2022 as a stock dividend): **47.4M (2018) →
  64.2M (2025) → 69.6M economic count on the 2026-08-07 cover** — **+47% in about eight
  years**, about 5% a year, from option exercises (2,651,132 / 1,902,713 / 1,380,886 Class A in
  2025/2024/2023) and a **registered direct offering of 2,884,615 Class A at $52.00 on
  2026-05-12** (8-K acc. 0001140361-26-020717, net ~$149.8M) — *seven weeks after a quarter-end at
  which the company held $872,269k of cash and cash equivalents* (10-Q Q1-2026, 2026-03-31).

  **At the subsidiary, invisible in ACMR's own share count.** ACM Research's holding of ACM
  Shanghai: **82.5% (FY2022) → 82.1% (FY2023) → 81.5% (FY2024) → 74.6% (FY2025) → 73.2%
  (2026-06-30).** The mechanisms, each filed: the **STAR IPO (2021)**; the **September 2025
  private offering of 38,601,326 ACM Shanghai shares at RMB 116.11, net $623.0M**; **ACM
  Research's own sale of 4,801,648 ACM Shanghai shares at RMB 160.00 on 2026-02-06, gross
  $110,243k**; and **2,431,900 ACM Shanghai options exercised by ACM Shanghai employees on
  2026-05-12** — the same day the registrant signed its own offering.

  **Combined, on the two filed ratios: a holder of one ACMR share at 2024-12-31 owned a claim on
  the Shanghai operating business that is 81.3% as large today** — (62,960,696 ÷ 69,649,196) ×
  (73.2% ÷ 81.5%) = 0.9040 × 0.8982 = **0.812**. **An 18.8% dilution of the look-through claim in
  nineteen months**, of which only half is visible in the number most screens read. The
  subsidiary issuance was at a premium to book, so ACM Research's equity *rose* — APIC went from
  $677,476k to $1,115,504k — which is why the dilution does not look like dilution in the
  consolidated balance sheet.

  **Candor note, in management's favour [E2-26]:** the FY2020 10-K told holders this in advance —
  *"If the STAR Listing and the STAR IPO are completed, ACM Shanghai will have broad discretion in
  the use of the proceeds … and **it may not spend or invest those proceeds in a manner that
  results in our operating success or with which ACM Research stockholders agree**,"* and *"ACM
  Research stockholders were not entitled to purchase ACM Shanghai shares in the pre-STAR Listing
  placement."* **The risk was disclosed before it was taken.** That is a real candor pass. It is
  not a rationality pass.
- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRES IN THE 10-K, and the corpus's named
  mechanism is written into a loan covenant.** Every 10-K from FY2017 to FY2025 presents
  *"adjusted EBITDA"* as a key measure — **24 occurrences in the FY2025 10-K**. FY2025: **adjusted
  EBITDA $159,958k** in a year when operating cash was **−$10,325k**. The corpus: EBITDA is
  promoted *"in the interests of Wall Street, enormously … **higher borrowing power**, higher
  valuations"* **[E5-41]** — and the FY2025 10-K, note 8: *"short-term borrowings of $14,239 from
  Bank of China have certain covenants which require **ACM Shanghai's year-end outstanding
  interest-bearing debt not to exceed five times of its annual EBITDA**."* **Borrowing power
  measured on the number that deletes depreciation, verbatim.**
  *Three things read in management's favour, and they are recorded, not buried:* (i) **the word
  EBITDA appears zero times in the three 2025–26 earnings releases** — the inverse of the CGNX
  pattern, where the 10-K was clean and the release was not; (ii) the 10-K's EBITDA caveats are
  unusually complete, including *"the assets being depreciated and amortized will often have to be
  replaced in the future"* and that it *"includes expense reductions and non-operating other income
  attributable to mainland China governmental grants"*; (iii) **the same section publishes the
  company's own free cash flow — −$67,092k (2025), +$43,723k (2024), −$163,063k (2023)** — a
  negative number printed beside the flattering one.
  *And one against:* the releases' headline non-GAAP measures **exclude stock-based compensation**
  — [E5-06], *"to say 'stock-based compensation' is not an expense is even more cavalier."* In
  Q2-2026 the same non-GAAP measure also **removed a $69.6M unrealized gain**, cutting non-GAAP net
  income to $44.5M against GAAP $89.0M — a deviation **toward** candor **[E2-69]** on that line.
- [ ] **filed-figure tells [E4-30]** — **not ticked.** Revenue growth is lumpy (+40.2%, +15.2%),
  not smooth. **Cash taxes as a share of pretax income: 6.1% (2019), 25.8% (2020), 2.6% (2021),
  5.3% (2022), 22.5% (2023), 6.7% (2024), 23.9% (2025)** — erratic, with no falling trend.
- [x] **dividends funded by issuance [E2-52] — FIRES at the subsidiary, with a jurisdiction
  qualifier.** ACM Shanghai paid **RMB 288.3M** of FY2024 dividends (ACM Research received
  **$29,238k** after withholding in 2025; the minority **$7,578k**) in the same year it raised
  **$623.0M** from a private offering, and repurchased **RMB 50.0M** of its own shares that year;
  it has proposed **RMB 299.0M** for FY2025 (8-K 2026-03-24) while consolidated operating cash was
  **−$10.3M (2025)** and **−$35.9M (H1-2026)** and the registrant raised $148.4M. **Qualifier, from
  the same announcement:** the payout is tied to *"Article 12.9.1, Paragraph 1, Item (8) of the
  … STAR Market Listing Rules"* — the listing venue's risk-warning rule for insufficient cash
  dividends. **The venue compels the payout; the owner's queue position [E3-66] is set in
  Shanghai.**
- [ ] **metric-switching [E2-49]** — **not ticked.** Shipments, adjusted EBITDA, free cash flow and
  adjusted operating income have been the 10-K's key measures in every vintage FY2017–FY2025,
  unchanged, including through FY2025's margin decline. *(My [E2-49] prior now stands at seven
  fires and six failures — ROKU fired, ACMR did not.)*
- [x] **stock-price targeting [E3-50] — FIRES, and the metric is market capitalisation, which
  issuance moves.** The CEO's March 2020 option vests in three tranches of 545,397 / 545,397 /
  545,400 Class A *"on the first trading day as of which our **market capitalization** equaled or
  exceeded"* **$1,553,383,586** (vested 2020-08-05), **$2,553,383,586** (vested **2025-10-27**) and
  **$3,553,383,586** (unvested at the proxy date, 2026-04-27) (DEF 14A 2026, outstanding-awards
  footnote 4). **A market-cap trigger is satisfied by issuing shares as well as by raising
  per-share value.** At $72.00 on 69,649,196 shares the cap is **$5,014.7M, above the third
  trigger.** *What I cannot establish from these documents, and do not claim:* whether the third
  trigger was crossed by price or with help from the May 2026 issuance — that needs the daily
  share count, and **a fired flag is not a venality finding [E5-38]**. The charter carries the
  same device in a second place: *"Because of the market capitalization achieved by Class A common
  stock during October 2020, **the trigger included in our charter pursuant to which all of the
  shares of Class B common stock must convert into Class A common stock no longer applies**"*
  (10-K FY2025) — the dual-class sunset was switched off by a market-cap level.

**[E4-52] — the flags converge, and they converge on one outcome: a larger quoted market value.**
A $4bn revenue target; adjusted EBITDA as a 10-K key measure and a loan covenant; SBC excluded from
every release headline; a CEO option that vests on market capitalisation; a dual-class sunset
defeated by market capitalisation; and serial issuance at two registers, which raises market
capitalisation mechanically. **Read as one system, not six prompts.** The corpus's own reading of
this confluence is at [E3-50]: the premise *"that their job at all times is to encourage the
highest stock price possible (a premise with which we adamantly disagree)"* — and the next step it
names is *"unadmirable accounting stratagems,"* **which I did not find.** The accounting read
clean after 2023; the disclosure is unusually full. **The convergence is in the incentives and the
capital structure, not in the numbers.**

### RELATED PARTIES — the brief's specific instruction, read closely

- **Item 404:** *"Since January 1, 2025, we have not been a party to any transactions in which the
  amount involved exceeded or will exceed $120,000 and in which any of our directors, executive
  officers or beneficial owners of more than 5% … had or will have a direct or indirect material
  interest, **other than compensation**"* (DEF 14A 2026). Clean on its face.
- **The conflict sits inside the carve-out.** *"We grant our NEOs stock options covering shares of
  **ACM Research and ACM Shanghai** to incentivize value creation across our entire operations"*
  (DEF 14A 2026, CD&A). **Dr. Wang holds 1,250,000 options on ACM Shanghai common stock** (625,000
  exercisable, 625,000 unexercisable, strike 7.06, expiring 2028-08-02); **Jian Wang 930,000; Fuping
  Chen 720,000; Lisa Feng 310,000** — all *"Option covers common stock of ACM Shanghai."* **The
  executives hold directly the equity that ACMR's own shareholders "may never directly own."**
  When the subsidiary issues shares at a price attractive to its own register, the executives are
  on both sides of the dilution and ACMR's holders are on one. The corpus is exact about where to
  look first: *"Never, ever, think about something else when you should be thinking about the power
  of incentives"* **[E4-27]**.
- **The conflict-of-interest policy routes a CEO matter to the CFO** — *"or to the Chief Financial
  Officer if such transaction involves the Chief Executive Officer"* — a reporting line that runs
  upward to the person it reviews.
- **Operating related parties** (note 13): purchases from equity investees **Ninebell $64,919k** and
  **Shengyi $15,173k** in 2025, **$80,092k together, 16.0% of cost of revenue**; payables to them
  **$32,060k**. Ninebell is the principal supplier of robotic subassemblies. **The FY2025 related-
  party payables increase of $15,927k is part of the working-capital support to operating cash
  examined at Q4.** Arm's-length terms are asserted, not evidenced; no mispricing was found.
- **A 5% holder of the US parent is Shanghai Pudong Innotek Capital Co., Ltd.** (3,358,728 Class A,
  Schedule 13D/A of 2024-10-29), a Pudong New Area investment vehicle — recorded for [E3-66].
- **The fiduciary line, filed as a risk factor:** *"ACM Shanghai is now managed by a group of
  officers separate from those of ACM Research and **those officers owe fiduciary duties to the
  various stakeholders of ACM Shanghai**."*

### STEP 3 — THE PRIMARY TEST [E2-01]

Net income attributable to ACM Research ÷ average ACM Research stockholders' equity, filed:

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| NI attributable | $18,894k | $18,780k | $37,757k | $39,263k | $77,349k | $103,627k | $94,078k |
| avg equity | $74,823k | $119,236k | $408,677k | $675,530k | $721,123k | $836,008k | $1,184,494k |
| **ROE** | **25.3%** | **15.8%** | **9.2%** | **5.8%** | **10.7%** | **12.4%** | **7.9%** |

**Five-year mean 2021–2025: 9.2%, without leverage** (1.49:1). On the unleveraged net-tangible-
asset denominator [E2-43] the FY2025 figure is the Q2 row's **4.9%**. And both are *accounting*
returns: FY2025 net income includes a **$17,455k unrealized gain** on STAR-listed stakes and
**$10,290k** of equity-method income, and H1-2026 net income of $148,485k includes **$68,186k**
unrealized and **$22,846k** equity-method. **On owner earnings (Q4) the return on equity is
negative in every window.** [E2-42]'s red light — *"falls much below the return on equity earned
over the period by American industry in aggregate"* — **is on.**

**The half-owner test [E2-26].** *Mostly passes, and this is the strongest thing in the file for
management.* The parent-only statements, the jurisdiction table, the restricted-net-assets figure,
the dividends up the chain, the STAR-IPO warning in advance, the negative free-cash-flow table, the
EBITDA caveats, the unrealized gain stripped out of non-GAAP. **Where it fails**: the SBC exclusion
in every release headline, and a $4bn target with no path in dollars of cash.

**The institutional imperative — all four [E2-30]:**
- [ ] resists change — **no**; the company changed auditor twice and structure once.
- [x] **projects soak up available funds — yes.** $623.0M raised in September 2025 is *"intended to be
  used by ACM Shanghai for research and development, capital expenditures and working capital"*;
  capex ran **$87,311k in H1-2026 against $31,458k in H1-2025** (+178%), and the Oregon facility is
  in build. The spend followed the cash, not the owner earnings.
- [ ] staff studies — not observable from filings.
- [x] **peer behaviour imitated — yes, filed.** Four new platforms (furnace, PECVD, Track, panel-level)
  are the incumbents' categories, entered one by one.

**Capital allocation — the buyback conditions [E5-08], run in reverse because the company issues.**
- (1) ample funds? **Yes on the balance sheet** ($1,132.6M cash and deposits at 2025-12-31) — **and
  no at the registrant**, where the parent-only statements show **$96,184k**.
- (2) **[E5-44] for issuance:** *"The intrinsic value of the shares you give … must not be greater
  than the intrinsic value of the business you receive."* **On owner earnings the business has no
  positive value to set against the $52.00 at which ACMR sold 2,884,615 shares**, so selling paper
  at that price is, arithmetically, not a transfer away from existing holders — **stated honestly,
  that is the one allocation in the file that may have been good for them.** The subsidiary private
  offering at RMB 116.11, five months before ACM Research itself sold ACM Shanghai shares at RMB
  160.00, is the other side: **the registrant's own later sale priced the subsidiary 37.8% above
  the price at which the subsidiary had issued to outsiders.** Whether RMB 116.11 was a fair price
  on the day is UNRESEARCHED (the STAR quote at pricing was not pulled) and does not move Q2.
- **CAPITAL ALLOCATION FLAG, stated with the humility clause [E4-13]:** *"it is natural for CEOs to be
  optimistic about their own businesses. They also know a whole lot more about them than I do."*
  The flag is the two-register dilution. It binds position size, never the discount rate — and
  there is no position.

**THE GUARDRAIL — checked before the verdict.**
- [x] Confirmed: nothing in this Q3 is used to promote the name **[E2-37, E2-38, E3-39]**.
- [x] Key-person dependence recorded **at Q2 as a moat defect [E4-23]**, not here as a strength.
- [x] Is a great manager the reason to act? **No.** The founder built a 43%-a-year revenue compounder,
      and that is a real achievement; but the franchise is not intact (Q2 NONE) and the damage is not
      local, so [E2-35, E2-36]'s excisable-cancer exception has nothing to apply to.

**VERDICT (recorded, not governing): [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [x] NOT REACHED — closed at Q2.**
*Had Q2 been IN, this would read **IN on honesty** — no disqualifier found in a dismissed class
action, a remediated control weakness or an auditor exit; **a Q3 pass is the absence of found
disqualifiers, not a finding that the managers are honest [E5-17]** — with **a CAPITAL ALLOCATION FLAG
and an [E4-52] convergence on market-value incentives**, which under a binary-gate weight case would
have required the gate to be argued, not assumed.*

## Q4 — WILL IT SURVIVE?

⚠️ **RECORDED, NOT GOVERNING. Q2 returned OUT.** Built in full because the brief asked for the
rebuilt range in dollars, the share of owner earnings that belongs to ACMR's own holders, where the
cash sits, the payables flag reconciled to the dollar, and the [E5-11] comparison against four named
survival shapes — and because the screen's two ends had to be rebuilt before anything could be said
about them.

### THE DEFECT IN THE QUEUE'S NUMBER, FOUND BEFORE ANYTHING ELSE

The row reads **`oe_bottom_m -92 | oe_top_m -26`**. **Both ends reproduce, and they come from two
different windows.** `oe_bottom` is the **5-year FY2021–25 mean at the capex end** computed without
intangibles: (−54,363 − 161,018 − 164,537 + 20,411 − 100,185) ÷ 5 = **−$91,938k**. `oe_top` is the
**3-year FY2023–25 mean at the D&A end**: (−110,753 + 92,907 − 60,230) ÷ 3 = **−$26,025k**. **The
advertised $66M spread is a window difference stacked on a capex-band difference** — the same defect
class the BA and INTC runs found in the STEP DOWN sub-class, now found in SIGN CHANGE.

**And the sub-class label is wrong about the direction, not just the width.** SIGN CHANGE was
described as *"early years loss-making, recent years positive."* **ACMR's rebuilt series is the
reverse**: FY2018 and FY2019 are the positive years (+$3.1M and +$5.0M at the D&A end), FY2020–2023
are negative, FY2024 is the single positive recent year, and FY2025 and the trailing twelve months
are negative again. **There is no inflection to date, because there was no recovery** — the brief's
instruction to *"date the inflection and refuse the blended mean"* is answered by the arithmetic
itself: the blended mean is refused because **every window is negative**, not because two businesses
are being averaged.

### Owner earnings — the one number **[E2-23]**

**Construction** *(CONVENTION, per the framework)*: operating cash flow (which nets working capital
from one audited line) **less stock-based compensation in full [E5-06]**, **less (c)**. Every input
is taken from **the filed cash-flow statement of the newest 10-K carrying that year** — **not** from
tagged D&A, which under-reads this filer ($14,405k tagged against $16,328k filed for FY2025; $6,573k
against $9,967k for FY2024).

**SBC resolves for every year, and it is COMPLETE on the charge measure.** The FY2025 10-K note 15
total of **$33,577k** equals the cash-flow add-back to the dollar and sums the by-function table
($1,343k + $6,629k + $8,783k + $16,822k); it includes **both** the registrant's 2016 Omnibus plan and
ACM Shanghai's 2019 and 2023 subsidiary option plans. **No stock-settled retirement contribution
exists** (29 US employees, no 401(k) share match found) — the BA defect class does not apply. **The
limit that does apply is [E3-70]:** the charge is the floor of the subtraction, not the measure, and
ACM Shanghai options with a strike of 7.06 on a share that transferred at RMB 160.00 are the case
where grant-date charge and value transferred diverge widely. **No grant-date total resolves
undimensioned** (the resume-state limit, re-confirmed here), and because owner earnings are already
negative on the charge measure, **a larger subtraction cannot change the sign** — so it is recorded,
not computed.

| FY | revenue | **OCF** | SBC | D&A (filed) | capex + intangibles | **OE, D&A end** | **OE, capex end** | ACMR share of NI | **ACMR-attributable, D&A end** | **ACMR-attributable, capex end** |
|---|---|---|---|---|---|---|---|---|---|---|
| 2018 | $74,643k | +6,909 | 3,363 | 417 | 2,071 | **+3,129** | **+1,475** | 100.0% | +3,129 | +1,475 |
| 2019 | $107,524k | +9,403 | 3,572 | 788 | 1,125 | **+5,043** | **+4,706** | 97.1% | +4,897 | +4,570 |
| 2020 | $156,624k | −13,547 | 5,628 | 1,502 | 5,535 | **−20,677** | **−24,710** | 86.6% | −17,914 | −21,408 |
| 2021 | $259,751k | −40,093 | 5,117 | 2,353 | 9,712 | **−47,563** | **−54,922** | 88.0% | −41,841 | −48,314 |
| 2022 | $388,832k | −62,194 | 7,730 | 5,366 | 92,520 | **−75,290** | **−162,444** | 77.7% | −58,463 | −126,138 |
| 2023 | $557,723k | −75,323 | 27,338 | 8,092 | 64,338 | **−110,753** | **−166,999** | 79.9% | −88,451 | −133,371 |
| 2024 | $782,118k | **+152,450** | 49,576 | 9,967 | 85,948 | **+92,907** | **+16,926** | 78.9% | +73,343 | +13,362 |
| 2025 | $901,309k | −10,325 | 33,577 | 16,328 | 57,655 | **−60,230** | **−101,557** | 77.2% | −46,486 | −78,383 |
| **TTM to 2026-06-30** | — | **−6,602** | 26,194 | 21,738 | 113,200 | **−54,534** | **−145,996** | *77.2% (FY2025 ratio)* | **−42,100** | **−112,709** |

*All in $ thousands. FY2020 D&A of $1,502k is the FY2020 10-K's filed figure; FY2018–19 from the
FY2019 10-K. TTM = FY2025 less H1-2025 (10-Q Q2-2026 comparatives) plus H1-2026 (10-Q Q2-2026,
acc. 0001628280-26-054832). Script: `Test Runs/_research 2026-09-12 ACMR/build_oe.py`.*

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25, E4-38].** Every window published,
none chosen:

| window | consolidated, D&A end | consolidated, capex end | **ACMR-attributable, D&A end** | **ACMR-attributable, capex end** |
|---|---|---|---|---|
| **5y FY2021–25 (the default [E2-42])** | −$40,186k | −$93,799k | **−$32,379k** | **−$74,569k** |
| 5y FY2020–24 | −$32,275k | −$78,430k | −$26,665k | −$63,174k |
| 3y FY2023–25 | −$26,025k | −$83,877k | −$20,531k | −$66,130k |
| 3y FY2022–24 | −$31,045k | −$104,172k | −$24,523k | −$82,049k |
| 4y FY2022–25 | −$38,342k | −$103,518k | −$30,014k | −$81,132k |
| 6y FY2020–25 | −$36,934k | −$82,284k | −$29,968k | −$65,708k |
| 7y FY2019–25 | −$30,938k | −$69,857k | −$24,988k | −$55,669k |
| 8y FY2018–25 (all filed OCF years) | −$26,679k | −$60,941k | −$21,473k | −$48,526k |
| TTM | −$54,534k | −$145,996k | −$42,100k | −$112,709k |

- **Short-window mean** (3y FY2023–25): −$26.0M to −$83.9M consolidated
- **Long-window mean** (8y FY2018–25): −$26.7M to −$60.9M consolidated
- **Combined range, nine annual windows × both (c) ends: −$104.2M to −$26.0M consolidated; −$82.0M to
  −$20.5M attributable to ACM Research.** Including the trailing twelve months: **−$146.0M to −$26.0M
  consolidated; −$112.7M to −$20.5M attributable.**
- *Is the range too wide to reach a conclusion?* **No — and that is the unusual thing about it.** It is
  $78M wide, but **it does not span zero on any window, at either end, or on the trailing twelve
  months.** [E4-25]'s *"no useful conclusion"* is the verdict when a range straddles the answer; this
  one sits entirely on one side of it. **The conclusion is that no construction produces owner
  earnings.**
- *A distorted year in the window [E5-11]:* **FY2024 is the one, and it is distorted favourably.** OCF
  of +$152.5M rode a **+$67.1M increase in customer advances** that **reversed by −$60.8M in FY2025**
  and a further −$25.9M in H1-2026. **[E4-41]'s instruction — normalize the mean DOWN for luck — applies:
  the only positive recent year was partly a customer prepayment that has since been handed back.**

**What share of owner earnings belongs to ACMR's own shareholders?** On the filed net-income
attribution, **77.2% for FY2025** (and 77.7–79.9% across FY2022–24). **That is 77.2% of a negative
number.** The attributable range is the table's right-hand columns. Two further facts bound it from
below:
1. **The ownership percentage is lower than the income ratio** — **73.2% at 2026-06-30** — because the
   FY2025 income ratio carries ownership of 81.5% for the eight and a half months before the
   September 2025 private offering took it to 74.6% (the registrant's own loss-making operations pull
   the ratio the other way, which is why it lands at 77.2% rather than nearer 80%). On a forward basis
   the ACMR share of the Shanghai cash generation is **73.2%, not 77.2%**, and falling (Q3).
2. **The registrant's own cash is a different and much smaller animal.** The parent-only statements
   (10-K note 20) show **parent operating cash of +$7,555k (2025), +$15,285k (2024), +$1,489k (2023)**,
   and **90.5% of the parent's FY2025 net income ($85,129k of $94,078k) is an equity-method pick-up of
   subsidiary earnings that is not cash.** The only cash the Shanghai business sends up the chain is
   **dividends — $29,238k (2025), $28,480k (2024), $19,200k (2023), after withholding** — and
   transfer-pricing payments. **On a strict "cash an ACMR owner can reach" basis, the owner earnings of
   the registrant are roughly the dividend it receives less its own operating loss and SBC — a number
   near zero, positive only by the width of the STAR Market dividend rule.**

**The 657% payables flag, reconciled to the dollar.** `wc_note` says accounts payable moved by 657% of
a year's operating cash. **Confirmed: FY2025 "Accounts payable" +$67,854k ÷ |OCF −$10,325k| = 657.2%.**
The arithmetic is right and the reading needs one correction: **the ratio is large because the
denominator is near zero, not because payables moved unusually** — but that is exactly the finding,
because **without the payables build FY2025 operating cash was −$78,179k, and without the related-party
payables build as well (+$15,927k, to Ninebell and Shengyi) it was −$94,106k.** **The 10-Qs locate
it, which the annual flag cannot:** year-to-date accounts payable +$7,743k (H1-2025) → +$37,354k (9M)
→ +$67,854k (FY); year-to-date OCF −$39,619k → −$44,244k → −$10,325k. **Q4-2025 alone: OCF +$33.9M
on an accounts-payable build of +$30.5M and a related-party build of +$8.7M — the quarter's positive
operating cash was supplier credit.** **It began unwinding in the next quarter:** accounts payable
**−$14,250k in Q1-2026** and **−$10,730k for H1-2026**, with OCF **−$29,538k** and **−$35,896k**.

**Working capital is the business model's cost, and it has been rising for seven years:**

| FY | receivables | DSO | inventories | inventory in months of COGS | (AR + inventory) ÷ revenue |
|---|---|---|---|---|---|
| 2018 | $24,608k | 120 days | $38,764k | 11.6 | 85% |
| 2020 | $56,441k | 132 | $88,639k | 12.2 | 93% |
| 2022 | $182,936k | 172 | $393,172k | 23.0 | 148% |
| 2023 | $283,186k | 185 | $545,395k | 23.2 | 149% |
| 2024 | $387,045k | 181 | $597,984k | 18.4 | 126% |
| **2025** | **$504,250k** | **204** | **$702,631k** | **16.8** | **134%** |

**Receivables and inventory together are $1,206.9M against $901.3M of revenue.** Receivable days rose
from 120 to 204. Part of this is structural and filed — first tools sit at customers for up to 24
months before acceptance, and the auditor's critical audit matter is the identification of repeat
shipments — but **a business that must carry 16.8 months of its cost of goods and 204 days of its
sales to grow is a business whose growth is paid for in cash before it is earned.** The credit-loss
provision went **$2,741k (2023) → $13,517k (2024) → $14,498k (2025)**.

**Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT [E3-44, E2-41].** **Which case: the
D&A default is not invalid here, but it is optimistic, and the band is displayed rather than
resolved.** ACMR is not the railroad class [E5-20] — its 10-K does not say depreciation understates
renewal, and much of the FY2022–25 capex ($296.5M) is the **greenfield Lingang production centre**,
which is growth, not maintenance. **But** the plant is new, so current D&A ($16.3M, rising to $21.7M
TTM) reflects a partial year of depreciation on a $314.8M net PP&E base, and **H1-2026 capex of $87.3M
is building a second site in Oregon.** My judgment: **true maintenance (c) sits above D&A and well below
total capex — and it does not matter, because owner earnings are negative at the D&A end in every
window.** **The capex band does not change the verdict**, so the [E4-25] rule — *"if the capex band
changes the verdict → UNKNOWABLE"* — does not bite.

**[E3-04] look-through.** Equity-method income was **$10,290k (2025)** and **$22,846k (H1-2026)**;
dividends received from those investees were $2,100k and $2,821k. The undistributed share is excluded
by the OCF construction. **Adding back the undistributed $8,190k moves the FY2025 D&A-end figure from −$60.2M to
−$52.0M** — still negative; recorded, not applied.

### Great, good, or gruesome? **[E4-20]**
- [ ] great · [ ] good · **[x] gruesome**
- *"grows rapidly, requires significant capital to engender the growth, and then earns little or no
  money."* **Revenue compounded 43% a year for seven years; cumulative operating cash FY2018–25 is
  −$32.7M; cumulative owner earnings are −$213.4M at the D&A end and −$487.5M at the capex end;
  the balance sheet was refilled with $623.0M of subsidiary equity and $148.4M of registrant equity.**
  *"Investors have poured money into a bottomless pit, attracted by growth when they should have been
  repelled by it."* **[E4-43]'s protection for the good class does not apply:** the good class earns
  *"an attractive rate of interest … also on deposits that are added"*; here the rate on the added
  deposits is negative in cash.

### Staying power — score all three **[E5-11]**
- **(1) a large and reliable stream of earnings — NO.** Operating cash negative in **five of eight**
  filed years and in the trailing twelve months; the one strong year was a customer prepayment.
- **(2) massive liquid assets — YES in the consolidated statement, and this is where the perimeter
  decides how much of it is the owner's.** **Where the cash is, 2025-12-31** (10-K note 2):

| jurisdiction | cash & equivalents | plus time deposits | total | share | transfer restriction, as filed |
|---|---|---|---|---|---|
| **Mainland China** | $228,777k | **$366,591k** (all at mainland banks, *"cannot be withdrawn before maturity"*) | **$595,368k** | **52.6%** | *"required to obtain approval from the State Administration of Foreign Exchange ("SAFE") to transfer funds into or out of mainland China"* |
| **Hong Kong** (CleanChip) | $421,104k | — | $421,104k | 37.2% | *"no additional restrictions for the transfer of cash"* — **but CleanChip was sold by ACM Research to ACM Shanghai in December 2019 for $3,500k and is inside the Shanghai perimeter** |
| **United States** | $107,184k | — | $107,184k | 9.5% | none — **of which the registrant itself holds $96,184k** (note 20); the rest is ACM California, also inside the Shanghai perimeter |
| South Korea · Singapore | $241k · $67k | — | $308k | 0.0% | none |
| restricted cash | $8,589k | | $8,589k | 0.8% | restricted |
| **total** | **$757,373k** | **$366,591k** | **$1,132,553k** | | |

  **So 8.5% of the group's cash sat at the registrant.** **91.5% sat inside ACM Shanghai's perimeter,
  of which ACMR's economic share is 74.6% (73.2% today), and more than half is inside mainland China
  behind SAFE approval and fixed deposit terms.** On top of the location, the **restricted net assets —
  *"paid-in capital, additional paid-in capital, and statutory surplus reserve of the Company's mainland
  China subsidiaries totaling $1,675,187"* thousand — exceed ACM Research's entire stockholders' equity
  of $1,464,363k**, which is why Rule 4-08(e)(3) parent-only statements are required at all. And the
  $623.0M private-offering proceeds are use-restricted: *"The use of proceeds raised by Private Offering
  and the STAR Market IPO … without further approvals, are limited to specific usage."* **At
  2026-06-30** US cash rose to **$314,256k** (the $148.4M registrant offering and the $110.2M ACM
  Shanghai share sale landed there), mainland China $223,718k plus deposits $365,055k, Hong Kong
  $427,310k — **the registrant's reachable cash tripled, and it did so by selling equity at two
  registers, not by earning it.**
- **(3) no significant near-term cash requirements — PARTIAL FAIL.** Current liabilities **$745,712k**,
  including short-term borrowings $74,041k, current long-term debt $35,082k and **customer advances of
  $187,809k that must be discharged by delivering tools**. **A dated state covenant:** the Lingang land
  grant requires that **by 2027-07-09** ACM Lingang *"generate a minimum specified amount of annual sales
  of products manufactured on the granted land or … pay at least RMB 157.6 million ($22.2 million) in
  annual total taxes"*; below 80% of the standard, *"the Grantor is entitled to terminate the Grant
  Agreement, take back the Land Use Right"* and *"take back the buildings, fixtures and auxiliary
  facilities"* at residual value. **The production centre where "substantially all of our tools are
  built" is held on a tax-production covenant with a date ten months out.** Oregon capex is in progress.
  **Covenant EBITDA test** at Bank of China: debt ≤ 5x EBITDA.
- **Leverage, named and quantified [E4-16, E3-29]:** bank borrowings **$288,053k** against cash and
  deposits of $1,132,553k — **net cash of $844.5M consolidated; the registrant's own borrowings $28,460k
  against $96,184k.** **The [E2-54] coverage test fails in form and passes in substance:** FY2025
  interest of $6,955k was **not** *"comfortably met out of current cash flow net of ample capital
  expenditures"* — the company's own filed free cash flow was **−$67,092k** — but the cash to pay it is on hand.
  **The corpus test is cash flow, not cash, and on cash flow it fails.**

### Name the specific way THIS business dies **[E2-27, E3-24]**

**The mechanism: a Chinese capex pause caught on a balance sheet built for growth, with the refill
valve on a foreign exchange.** ACM does not die of debt; it has net cash. It dies — or more exactly its
**US holders'** claim dies by attrition — in three filed steps:

1. **The regime turns.** The 10-K's own Gartner citation: **China WFE −1.7% (2025), −9.9% forecast
   (2026).** [E2-58]: *"nothing fails like success"* — China's mature-node capacity build is the
   capacity glut of the late 2020s, and ACM's customers are the builders. A further US, Dutch or
   Japanese control on the parts ACM Shanghai imports (already *"may directly impact ACM Shanghai's
   ability to meet its future production plans"*) turns the same way from the supply side.
2. **The working capital built on the way up has to be collected and sold on the way down.**
   Quantified from the filed balance sheet: **receivables $504.3M (204 days) and inventory $702.6M (16.8
   months of COGS).** **Scenario, not forecast:** revenue falls 30% (ACLS's filed peak-to-trough was
   −25.8%; China WFE forecast −9.9% is a third of that). If inventory of the size carried has to be
   written down by 15% — FY2025's provision was already $15.5M, 2.2% of the balance, in a *growth*
   year — that is **−$105M** of pretax loss; a further 5% of receivables uncollectable is **−$25M**;
   and on FY2025's cost structure (opex $290.6M, 32% of revenue, mostly R&D the 10-K says *"will
   increase in absolute dollars"*), **a 30% revenue decline at 44% gross margin turns $109M of
   operating income into a loss of roughly −$10M before the write-downs, and about −$140M after
   them.** The cash, though, is there: **$1.13bn covers that for years.**
3. **So the death is not insolvency; it is dilution at a register the holder cannot vote in.** The
   subsidiary refills itself on the STAR Market — it did in 2021 and in 2025 — and every refill lowers
   the 73.2%. **If ACM Shanghai raises another RMB 4.4bn at a depressed price in a downturn, the ACMR
   look-through share falls by the same arithmetic as 2025 (81.5% → 74.6%, a 6.9-point loss) or worse**;
   the registrant meanwhile can only reach Shanghai cash by selling Shanghai shares, which lowers the
   percentage again. **Holder attrition compounds: a share of a share of a business that earns no owner
   earnings.** And **the HFCAA path** sits behind all three — *"if ACM Research were to be included on the
   Conclusive List for two consecutive years … the SEC would prohibit trading in our securities"* —
   with a mainland-China auditor on the file since FY2023.

**Likelihood:** [ ] likely **[x] a real possibility** [ ] a low-level possibility — for step 3, the
dilutive refill in a downturn, because it has already happened twice in a growth phase; *a
low-level possibility* for the HFCAA delisting, because the PCAOB's 2021 determination was vacated
on 2022-12-15 and has not been re-imposed.

**[E4-51] — the bear case stated so its holders would accept it:** *ACM is a real engineering company
that has taken share in the world's largest equipment market behind a wall that keeps its best
competitors out, and its cash burn is the cost of building two factories and a first-tool evaluation
pipeline across four new product lines; the dilution was issued at premiums to book, so it created
book value for ACMR holders; and the listed stake alone, at the filed February 2026 transfer price,
is worth more than ACMR's entire market cap.* **Stated fairly, that case is about price and growth.
It does not contain an owner-earnings number, and the framework's Q4 is about owner earnings.**

### THE [E5-11] SHAPE, AGAINST THE FOUR NAMED ONES

| run | shape | ACMR? |
|---|---|---|
| **ORCL** | contracted not to stop — committed obligations run ahead of cash | **No.** No material purchase commitments filed; customers give *"non-binding one- to two-year forecasts."* The one contracted item is the Lingang tax covenant — small, but dated. |
| **ARM** | earning nothing after paying its people — SBC ≈ all of operating cash | **Partly, and worse.** ARM earned OCF and SBC consumed 96.6% of it; **ACMR's cumulative SBC FY2018–25 is $135.9M against cumulative OCF of −$32.7M** — the SBC is paid out of *financing*, not operations. |
| **BE** | too little filed history to judge | **No.** Ten annual reports, eight OCF years, a unit series — the history is ample and it is consistent. |
| **BA** | spending cash undoing past work | **No.** No reach-forward losses, no remediation programme; the cash goes forward, into inventory, receivables and plants. |
| **ACMR — a fifth shape** | **growth refilled by selling the subsidiary** — negative owner earnings on every window, net cash on the balance sheet, and the refill valve is **equity issued at a register the US holder cannot own or vote in** | **the gruesome account [E4-20], with the deposits added by strangers [E5-39] and the interest credited in Shanghai.** |

**VERDICT (recorded, not governing): [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** — had Q2
been IN, Q4 would close OUT: owner earnings are negative on every window, both (c) ends and the trailing
twelve months **[E2-23, E4-25]**; the business is gruesome **[E4-20]**; strength (1) fails **[E5-11]**;
the [E2-54] coverage test fails on cash flow. **The file's governing verdict remains Q2 OUT.**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass. **Q2 returned OUT. Q5 is NOT opened.** What follows is the queue's
required price, **headed as operator rule 3 requires and carrying no entry language.**

---
# COMPUTATION — NOT A CLEARANCE

*Required by the queue's output contract of 2026-09-01: every run ends with a price. This is
arithmetic on a closed file. It ranks nothing and recommends nothing.*

**Inputs, dated.** Price **$72.00** (close 2026-09-11, aggregator quote, flagged) · economic share
count **69,649,196** (Class A 64,657,388 + Class B 4,991,808, cover of 10-Q acc.
0001628280-26-054832, summed on the note 14 charter reading) · **market cap $5,014.7M** · sovereign
**5.35%** (US Treasury 30-year par yield, 2026-09-11).

**The numerator is ACM Research's attributable owner earnings, not the consolidated figure**, because
the market cap prices ACMR's equity only and ~23–27% of the consolidated economics belongs to ACM
Shanghai's minority (Q1, Q4).

**1. THE YIELD**

| construction (ACMR-attributable) | owner earnings | ÷ $5,014.7M | vs 5.35% |
|---|---|---|---|
| 5y FY2021–25, D&A end *(the corpus default window [E2-42] and default (c) [E3-44])* | **−$32.4M** | **−0.65%** | **−6.00 pts** |
| 5y FY2021–25, capex end | −$74.6M | −1.49% | −6.84 pts |
| **TTM to 2026-06-30, D&A end** | **−$42.1M** | **−0.84%** | **−6.19 pts** |
| TTM, capex end | −$112.7M | −2.25% | −7.60 pts |
| best of all nine annual windows (3y FY2023–25, D&A end) | −$20.5M | −0.41% | −5.76 pts |
| worst of all nine annual windows (3y FY2022–24, capex end) | −$82.0M | −1.64% | −6.99 pts |
| *for reference only:* **the best single year in eight filed OCF years** (FY2024, D&A end) | **+$73.3M** | **+1.46%** | **−3.89 pts** |

**Every multi-year construction is negative. The yield is negative on both (c) ends, on every window,
and on the trailing twelve months.**

**2. WHAT THE PRICE ALREADY ASSUMES — in dollars, because a negative base has no growth rate.**
- to yield the **5.35% sovereign** at $72.00, ACM Research must earn **$268.3M** of attributable owner
  earnings a year — at today's 73.2% holding, **$366.5M consolidated**.
- to clear the **~10% floor [E4-28]**, it must earn **$501.5M attributable — $685.1M consolidated**.
- **the most it has ever earned is +$92.9M consolidated (FY2024, D&A end), and that year leaned on a
  customer prepayment it has since returned.** Repeat the best year exactly and the buyer receives
  **1.46%, below the sovereign, and one-seventh of the floor.**
- **$685.1M of consolidated owner earnings is 76% of FY2025 revenue.** At the **$4bn long-term revenue
  target**, it is a **17.1% owner-earnings margin** — above the **12.1% operating margin** the business
  earned in FY2025, and after SBC and (c), which the operating margin is not. **So the price assumes
  that the $4bn target is reached, that working capital stops consuming the growth, that capex falls to
  maintenance, and that the ACMR share of the result stops falling — all four.** [E4-35]'s base rate
  applies to the first alone: *"fewer than 10 of the 200 most profitable companies … will attain 15%
  annual growth in earnings-per-share over the next 20 years."* From $901M to $4bn is a 4.4x; at 15% a
  year it takes 10.7 years, from a base of **negative** owner earnings.

**3. WHAT YOU ARE PAID.** **−5.76 to −7.60 points under the sovereign**, depending on construction;
**−6.19 points** on the trailing twelve months at the default (c) end. **A buyer at $72.00 is paid
nothing and funds the shortfall — twice: once in the business's cash consumption, and once in the
subsidiary issuance that refills it.**

**IN WORDS, WHAT THE BUYER AT TODAY'S PRICE IS PAYING FOR.** $5.01bn buys: **73.2% — and falling — of
a Shanghai STAR-listed equipment maker** that the buyer may never own directly; **99.6% of its revenue
from one country whose equipment spend the company's own cited forecaster puts at −9.9% for 2026**;
both principal operating subsidiaries on the **BIS Entity List**; eight years of operations that
produced **−$32.7M** of cumulative operating cash; **$1.2bn of receivables and inventory** carried
against $901M of revenue; **$1.13bn of cash of which 8.5% sat at the registrant** and more than half
inside mainland China behind SAFE approval; a production centre held on a **state tax-production
covenant dated 2027-07-09**; a **$4bn revenue target** and an **adjusted EBITDA** key measure; a CEO with
**57.2% of the votes** and **1,250,000 options on the subsidiary**; and a share of the operating
business that fell **18.8% in nineteen months** without the ACMR share count showing half of it.
**The buyer is not paying for owner earnings — there are none. The buyer is paying for the proposition
that the listed Shanghai stake is worth more than ACMR's quote** (at the filed February 2026 transfer
price of RMB 160.00 ≈ $23.05, ACMR's ~353M ACM Shanghai shares carry a quoted value of roughly
**$8.1bn**, against ACMR's **$5.0bn**), **and that the discount will close.** That proposition may come
true. **It is a spread between two quotes, not a yield, and a spread between two quotes is what
[E2-28] tells an owner to sell into, not to buy.** It also cannot be distributed: *"Stockholders of ACM
Research may never directly own equity interests in ACM Shanghai"*, and the only way the registrant
has realised it is by selling Shanghai shares, which lowers the 73.2%.

**THE FLOOR, FIRST [E4-28].** Honest pre-tax expectancy at this price: **negative on every construction;
1.46% even on a repeat of the best year in eight.** **Below roughly 10% the name is not ranked — it is
quit on, whatever the sovereign is.** ACMR is quit on twice over: once at Q2 on the business, and once
here on the arithmetic. **The ranking lines are not filled in [E4-21, E3-45].**

**Value as a round-number range [E4-01].** *"Using precise numbers is, in fact, foolish."* **On every
cash construction owner earnings are negative, and the owner-earnings value of the equity is not a
positive number. A round-number range is refused rather than invented.** What can honestly be said: at
the sovereign rate, a business repeating its best-ever attributable year would be worth roughly
**$1.4bn**; one earning its five-year mean, **nothing**; and the quote is **$5.0bn**. **Current price
$72.00.**

**WHICH BAR? NEITHER, and that is the finding.** The normal method [E4-11] needs a value to apply a
margin to; the screamer test [E4-01] needs a conservative case for the price to clear. **The conservative
case is −$112.7M and the optimistic case is −$20.5M. The price is above the whole range** — [E4-01]'s
third outcome, *"no."* **Windage count: one** — the (c) judgment at Q4, displayed as a band and never
resolved to a point. No second conservatism was applied and none was needed: the D&A end, the lenient
one, is already negative.

**PRICE AND PASS/FAIL, PLAINLY:** **$72.00 · market cap $5,014.7M · FAIL at Q2 (OUT, on the business).**

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Not opened as a hold/sell question — there is no position and none is contemplated.** Recorded as the
**refutation conditions** the framework requires of any closed file, pre-committed in writing per
**[E1-02]** — *"I believe in establishing yardsticks prior to the act"* — so that a future re-opening
is triggered by filed evidence and not by a price move.

**THESIS-BREAKING METRICS, each read off a 10-K or 10-Q, each with a threshold.** The file re-opens at
Q2 if **three or more** turn, and is re-read if any single one does:

1. **Positive owner earnings at the D&A end, OCF − SBC − D&A, for two consecutive fiscal years** — with
   customer advances not rising in either year, so the [E4-41] prepayment distortion is excluded.
2. **ACM Research's holding of ACM Shanghai stops falling** for three consecutive annual reports
   (threshold: ≥ 73.2%, the 2026-06-30 figure), with no registrant sale of Shanghai shares.
3. **"Other Regions" revenue above 10% of the total** in an annual report (it was 0.37% in FY2025 and
   falling from 3.0% in FY2023) — the only filed test of whether the moat exists outside the wall.
4. **Gross margin at or above 48% for a full fiscal year while ACM Shanghai remains on the Entity List**
   — the [E2-44] first half, passed.
5. **The annual tool delta, on the FY2023+ definition, exceeds the FY2023 peak of +385** — [E4-55]
   passing on units rather than dollars.
6. **Receivable days below 150 and inventory below 12 months of cost of revenue** in the same year —
   growth that stops pre-paying itself.
7. **Services and spares disclosed as a separate line**, and above 15% of revenue — the installed-base
   annuity forming.
8. **ACM Shanghai and ACM Korea removed from the BIS Entity List**, dated in a filing.

**THE DIRECTION OF THE MOAT, the monitoring question [E4-17, E3-30]:** is the FY2025 margin fall and the
three-year unit decline *"an aberrational cycle"* or has the business *"slipped in a way that
permanently reduces intrinsic business values"*? **Beliefs change gradually [E4-17]; the unit series
and the Other-Regions line are the two slow instruments to watch.**

**Catalyst dates, all filed:** FY2026 10-K (~March 2027) · **2027-07-09, the Lingang land-grant tax
standard** · ACM Shanghai's FY2025 dividend AGM and any further STAR offering or registrant share
transfer (8-K EX-99.1) · COINS Act implementing regulations, due by March 2027 · the third
market-capitalisation tranche of the CEO's March 2020 option (DEF 14A 2027).

**Position size:** none. **Reversal condition in words, not a price alert** (the QLYS ruling of
2026-09-07: a price alert on a name that failed on the business is a category error).

**VERDICT: NOT REACHED — the file closed at Q2.**

---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN → Q2 OUT → file closed. Q3 and Q4 built
      and headed *"RECORDED, NOT GOVERNING"*; Q5 replaced by `COMPUTATION — NOT A CLEARANCE`; Q6 as
      refutation conditions only.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on filed
      documents throughout; the one PROVISIONAL-class matter (seven of nine named competitors unpriced)
      is at Q2, adjudicated by the narrow-only rule, and Q2 is OUT, not IN.
- [x] **Every UNRESEARCHED item names the artifact and where it lives.** Two, neither verdict-moving:
      the STAR quote for ACM Shanghai on the September 2025 private-offering pricing date (SSE / ACM
      Shanghai announcement, Chinese-language, not pulled); the grant-date SBC value of ACM Shanghai
      options (no undimensioned tag; would need note 15's option tables by hand).
- [x] **Every UNKNOWABLE verdict states what cannot be known** — none used.
- [x] **Step 0: the filing was read, with accession numbers; three figures cross-checked** (gross profit,
      the NCI split and EPS, the operating-income identity), all exact.
- [x] **Owner earnings on a multi-year mean; nine windows plus TTM published; capex band disclosed as a
      judgment; attributable figures shown beside consolidated.**
- [x] **Competitor row filled** on the cohort formula; ACMR cells computed here; seven of nine named
      competitors unpriceable and the limit stated.
- [x] **Sovereign for the earnings currency — with a stated limitation.** USD 30-year from the Treasury,
      dated 2026-09-11. **The operating earnings are RMB**; the RMB sovereign is not on the project's
      list, and no rate changes a negative numerator. Recorded, not hidden.
- [x] **Value stated as a range — refused as a range, with the reason**, because every construction is
      negative; the rounded reference figures are labelled as such.
- [x] **One bar chosen — neither applies**, stated; windage count one.
- [x] **Prices dated; aggregator used for live quotes only and flagged.** The ACM Shanghai figure uses
      the **filed** February 2026 transfer price, not a quote.
- [x] **SBC resolves for every year and is complete on the charge measure** (brief requirement): $33,577k
      ties note 15, the function table and the cash-flow add-back; both registrant and subsidiary plans
      included; no stock-settled 401(k). [E3-70] market-value limit recorded.
- [x] **The payables flag cross-checked to the dollar** (657.2%) and **located in the 10-Qs**.
- [x] **The Class A/B judgment made from the charter** (note 14), not from arithmetic.
- [x] **The deal_note opened**: the 2026-05-12 Item 1.01 is a registered direct equity offering — neither
      a credit agreement nor a merger.
- [x] **Corrections recorded here rather than by editing history (operator rule 6):**
  1. **Commit `ed3efc7`'s title says ACMR's was "the only margin that fell while revenue grew."** ONTO's
     FY2025 gross margin also fell (−2.5 points), and ONTO's revenue direction was not checked. The run
     file's text was corrected before commit to *"only two filers in the row fell — ONTO by 2.5 points
     and ACMR by 5.7"*; the commit title stands as written and is wrong by one filer.
  2. **An attribution sentence at Q4 was wrong on first write** — it said the 77.2% income ratio exceeded
     the 73.2% ownership because of the registrant's loss-making operations; the registrant's losses pull
     the other way. Corrected in the working file before the fold: the ratio carries 81.5% ownership for
     most of FY2025.
- [x] **Run committed to git** — after Step 0/Q1, Q2, Q3 and Q4, by file name.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** **ACMR FAILS at Q2 — OUT on the business.** A real single-wafer cleaning technology
  inside China's export wall, but the 10-K names nine substitutes and concedes being out-bundled
  **[E3-03]**, it earns the lowest return on capital in the cohort (ROUNTOA 4.9%) **[E3-46]**, its gross
  margin fell 5.7 points while revenue grew 15.2% in the first full year on the BIS Entity List and eight
  years of growth produced −$32.7M of operating cash **[E2-44]**, and 99.6% of revenue is one policy
  regime **[E2-59]**. Recorded beneath the verdict: owner earnings are negative on every window, both (c)
  ends and the trailing twelve months; ACMR's holders own 73.2% of the operating business and falling;
  8.5% of the group's cash sat at the registrant. **Price $72.00 · cap $5,014.7M · COMPUTATION — NOT A
  CLEARANCE: yield −0.65% to −2.25%, −5.8 to −7.6 points under the 5.35% sovereign.**
