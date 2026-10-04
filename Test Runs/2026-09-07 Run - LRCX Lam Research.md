# Company Run — LAM RESEARCH CORPORATION (LRCX) — 2026-09-07
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**THE THIRD LEG OF THE EQUIPMENT COHORT.** Direct precedents, read in full before any
data was fetched: `Test Runs/2026-09-07 Run - KLAC KLA.md` (IN NARROW, the strongest Q2
evidence in queue history) and `Test Runs/2026-09-07 Run - AMAT Applied Materials.md`
(IN NARROW, "narrower than KLAC's"). This file interrogates the cohort row those two
built; it does not rebuild it.

**HEADLINE — written LAST, after the gates closed, and placed first for the reader.
See `## THE HEADLINE, FILLED IN` at the foot of this file.**

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

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- rate **5.24%** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-year
  — the issuing authority**, struck fresh through `tools/sources.py` (FRED is the fallback,
  not the source; corrected 2026-09-02).
- FX: **none required.** Lam is a Delaware corporation, files in USD, prices and invoices in
  USD. 93.4% of FY2026 revenue is shipped to customers outside the United States
  ($21,703.8M of $23,232.7M), but the tools are sold and the receivables carried in dollars.
  That is a **geographic exposure question read at Q2 and Q4, not an FX repricing question**
  — the same ruling the AMAT run made. No ADR ratio.

**PRICE AND SHARE COUNT — RE-STRUCK BY HAND. Three runs have been bitten here (CRWD 4x on a
split, QLYS 3.1% stale, PINS 3.9% on a frozen quote).**
- **Price $307.65**, the close of **2026-09-04** (Friday; 2026-09-07 is the Labor Day
  holiday and there is no later close). Source: Yahoo chart endpoint via
  `tools/sources.py`'s host list — **an aggregator, used for the live quote only, and
  flagged** per operator rule 5. Prior four closes recorded so a frozen quote would show:
  301.49 · 290.20 · 288.32 · 292.66 · **307.65**. Not frozen.
- **Shares 1,251,321,000.** Read off the **cover of the FY2026 10-K**: *"As of August 4,
  2026, the Registrant had **1,251,321 thousand** outstanding shares of Common Stock."*
- **Cross-check, second independent count in the same document:** the balance sheet reads
  *"issued and outstanding **1,251,278 thousand** shares as of June 28, 2026."* The two
  agree to **43 thousand shares (0.003%)**, the difference being five weeks of ESPP
  issuance and repurchase. **Single class of common stock.**
- **SPLIT GUARD.** `StockholdersEquityNoteStockSplitConversionRatio1 = 10` at **2024-10-02**
  — Lam did a **10-for-1 split** inside the owner-earnings window. Every pre-FY2025 share
  count and per-share price in this file is stated **post-split** and says so. The cover
  count is post-split and needs no adjustment.
- **MARKET CAP = 1,251,321,000 × $307.65 = $384,969M.**
- *Difference from the brief's screen row: the row carried `cap_m 383129`, which implies a
  price of **$306.18**. Same construction, an earlier quote. Immaterial (0.48%) and
  recorded rather than absorbed.*

**THE FILING WAS READ — not tagged data [E3-27, E4-14]:**
- [x] MD&A  [x] cash-flow statement including its detail lines  [x] footnotes
- **Anchor document: Form 10-K for the fiscal year ended 2026-06-28, filed 2026-08-07,
  accession `0000707549-26-000037`.** (SIC 3559; CIK 0000707549.)
- **Vintages read for the multi-year series, each by its own accession** (so no restated
  figure is silently substituted for the one originally filed — the INTC defect of
  2026-09-07): FY2025 `0000707549-25-000075` · FY2024 `0000707549-24-000106` · FY2023
  `0000707549-23-000102` · FY2022 `0000707549-22-000107` · FY2021 `0000707549-21-000136` ·
  FY2020 `0000707549-20-000138` · FY2019 `0000707549-19-000124` · FY2018
  `0000707549-18-000115` · FY2016 `0000707549-16-000050`.
- **Figures cross-checked against the filed statement (four, not one):**
  1. **Share count** — cover 1,251,321k vs balance sheet 1,251,278k (above).
  2. **Operating income** — the XBRL tag reads $8,199,795k; the filed Consolidated
     Statements of Operations read `Gross margin 11,725,308 − R&D 2,375,873 − SG&A
     1,149,640 = Operating income 8,199,795`. Reproduces to the dollar.
  3. **Capital expenditure** — the cash-flow line is *"Capital expenditures **and intangible
     assets** (966,405)"*. The tag `PaymentsToAcquireProductiveAssets` = 966,405. Same
     number; the **caption includes intangibles**, which is recorded because it makes the
     capex end of (c) marginally conservative, not marginally generous.
  4. **Segment gross margin** — Note 19 reconciles $12,120,049k of segment gross margin to
     $11,725,308k of consolidated gross margin through $394,741k of "All other COGS".
     Reproduces.
- **Detail lines that matter and are recorded here because they are read at Q4:**
  non-cash *"Transfers of finished goods inventory to property and equipment $125,691"*
  (FY2026) — inventory becoming PP&E, i.e. capex that never crosses the investing line;
  *"Accrued payables for capital expenditures $119,605"*; cash interest paid $150,101.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics, in my own words, without management's language.**

Lam sells four kinds of machine that a chip factory cannot do without, and then sells the
parts and labour that keep them running. A wafer goes through a few hundred steps; Lam owns
three of the recurring ones — **putting material on (deposition), taking material off
(etch), and washing what is left (clean)** — plus a fourth line, **Reliant**, that sells
older-generation versions of the same machines to factories building non-leading-edge chips.

The money arrives in two streams and Lam files both:

| FY2026 | $M | share |
|---|---|---|
| **Systems** — new leading-edge deposition, etch, clean tools | **14,885.5** | 64.1% |
| **Customer support-related revenue and other** — service, spares, upgrades, and Reliant | **8,347.2** | 35.9% |
| total | 23,232.7 | |

A tool sells for millions of dollars, is bolted into a fab, and then **cannot be swapped**
without re-proving the entire process. Lam says so in its own filing: *"once a semiconductor
manufacturer has selected a particular supplier's equipment and qualified it for production,
the manufacturer generally maintains that selection for that specific production application
and technology node as long as the supplier's products demonstrate performance to
specification in the installed base."* So the first sale buys an annuity, and the annuity is
**a third of the revenue and rising through downturns** (33.2% FY2019 → 40.1% FY2024).

The cost side is a machine shop plus a very large laboratory. Gross margin **50.5%**;
R&D **$2,375.9M, 10.2% of revenue**; SG&A 4.9%. Operating margin **35.3%**. The whole thing
turns on about **$10.1bn of operating capital** once cash and goodwill are stripped out, and
throws off **$8.2bn of pre-tax operating profit** on it. That ratio — **81.0%** — is the
number this run is really about, and it is the highest in the cohort.

**The scarce input the business controls.** Not capital, and not manufacturing: it is the
**qualified process of record** — the specific recipe, on the specific chamber, that a
customer's yield engineers have signed off for a specific device at a specific node. That
asset is created jointly with the customer, sits inside the customer's fab, and is expensive
for the customer to abandon. Lam's second scarce input is **atomic-scale materials
know-how** — the accumulated knowledge of how to remove one layer without touching the one
underneath at dimensions where "one layer" is a few atoms. Neither is a patent portfolio,
and Lam does not claim it is: it counts no patents in Item 1.

**Will the fundamentals look broadly the same in ten years?** **Broadly yes, with one
honest qualification carried into Q2.** Chips will still need material added, removed and
cleaned; there is no route around those three steps that does not still require a machine to
do them. The industry has consolidated to a handful of suppliers and shows no sign of
fragmenting. What will *not* look the same is the *level*: the filing itself opens Note 1
with *"The semiconductor industry is cyclical in nature and has historically experienced
periodic downturns and upturns. Today's leading indicators of changes in customer investment
patterns … may not be any more reliable than in prior years."* Lam's revenue fell **12.9%
in FY2019** and **14.5% in FY2024**; its owner earnings in FY2020 were **$1,734M** against
FY2026's **$4,505M**. **The mechanism is stable and the level is not**, and [E5-29] governs:
*"Volatility is far from synonymous with risk."*

**[E4-46] check — is this a five-minute business or a five-month one?** Five minutes. Four
product lines, one segment, two revenue captions, seven geographies, ten customers that
matter. The accounting is plain and the cash-flow statement has nothing exotic in it. The
hard questions in this file are all at Q2 and Q5, which is where they belong.

- **VERDICT: [x] IN**

*Recorded per [E5-13]: most names should end at Q1 and this one does not. That is not a
compliment to Lam; it is a statement that a machine-tool business with two revenue lines is
inside anybody's circle.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**VERDICT STATED IN ADVANCE, so the evidence can be read against it [E4-26]: IN — NARROW.
Between KLA's narrow and AMAT's, and CLOSER TO AMAT'S. Lam has the best economics in the
cohort and the weakest filed pricing evidence in it. Both are true and this section is
mostly about why they do not cancel.**

### The three criteria [E3-03]

**(1) Needed or desired — YES.** Deposition, etch and clean are three of the few hundred
steps every wafer goes through, and no fab skips them. Not contested.

**(2) No close substitute — THE COMPANY'S OWN FILING NAMES SEVEN, AND THEN SAYS WHY THEY
CANNOT BE SWAPPED IN. Both halves are quoted because both are load-bearing.**

The substitutes, in Lam's own words, Item 1 "Competition", FY2026 10-K, accession
`0000707549-26-000037`:

> "We face significant competition with all of our products and services. **Our primary
> competitor in the dielectric and metals deposition market is Applied Materials, Inc.**
> For ALD and PECVD, we also compete against **ASM International** and **Wonik IPS**. **In
> the etch market, our primary competitors are Applied Materials, Inc.; Hitachi, Ltd.; and
> Tokyo Electron, Ltd.**, and our primary competitors in the wet clean market are **Screen
> Holding Co., Ltd.; Semes Co., Ltd.; and Tokyo Electron, Ltd.**"

**Seven named companies across all four of Lam's product markets, with a named primary
competitor in every one of them.** That is more named substitutes than any other filing in
this cohort — AMAT names none, KLA names five, and neither of them names Lam (recorded
sweep below). It is two fewer than the eight Pinterest named in its own competition
paragraph, and Pinterest was closed OUT at Q2 on exactly this criterion on 2026-09-07.

**Lam is not Pinterest, and the reason is the second half of the same paragraph:**

> "semiconductor manufacturers must make **a substantial investment to qualify and integrate
> new capital equipment into semiconductor production lines**. As a result, **once a
> semiconductor manufacturer has selected a particular supplier's equipment and qualified it
> for production, the manufacturer generally maintains that selection for that specific
> production application and technology node** as long as the supplier's products demonstrate
> performance to specification in the installed base. Accordingly, **we may experience
> difficulty in selling to a given customer if that customer has qualified a competitor's
> equipment.**"

Pinterest's eight substitutes are one tap away and cost the user nothing. Lam's seven
require a fab to re-qualify a process on a running production line. **The same mechanism is
filed independently by Nova Ltd (20-F FY2025, `0001178913-26-000504`)** and was relied on by
both cohort runs, so it is not one registrant's self-description.

**So criterion (2) passes per socket and per node, and fails per contest — the identical
finding the AMAT run reached, reached here from the filing that generated it.** The last
sentence is the sharp one and it is symmetric: **the lock that protects Lam's installed base
is the same lock that keeps Lam out of AMAT's.** A moat that only holds what you already
have is a moat around a fixed area. [E4-32]'s *"widened every year"* is not what this
mechanism does; it is what it prevents.

**(3) Not price-regulated — passes on price; the [E2-59] inversion applies.** Nobody caps
Lam's prices. What is regulated is **who it may sell to**, and Item 1A states the
consequence in the form that matters here:

> "restricting access to our technology (such as recent controls limiting exports to China)
> may cause customers with international operations to reconsider their use of and reliance
> on our products, which could adversely impact our future revenue and profits and
> **strengthen competitors who are not subject to such restrictions.**"

> foreign governments may "**provide special incentives to government-backed local customers
> to buy from local competitors, even if their products are inferior to ours.**"

Unlike AMAT, **Lam carries no enforcement outcome**: Note 17's Legal Proceedings paragraph
reads *"the Company is not currently a party to any legal proceedings that it believes
material"* and no accrual is recorded. AMAT paid **$253M to BIS in Q2 FY2026 and operates
under a suspended denial order.** That is a real point in Lam's favour and it is recorded
here rather than at Q3, because it is a difference in the *business's* regulatory position.

### [E4-04] — MUST THE MOAT BE CONTINUOUSLY REBUILT? THIS IS THE CLOSEST CALL IN THE FILE.

The opening sentence of Lam's own Competition section is the framework's excluded-class
language almost verbatim:

> "**The semiconductor capital equipment industry is characterized by rapid change** and is
> highly competitive throughout the world. **To compete effectively, we invest significant
> financial resources** targeted to strengthen and enhance our product and services portfolio"

[E4-04] excludes *"the moat whose basis must be periodically replaced — rapid-change
industries."* Lam's filing uses the phrase. Against that, the framework's own test: **does a
lapse in spending destroy the structure, or merely narrow it — and does the spending defend
the same advantage, or buy its replacement?**

- **The spending is $2,375.9M of R&D, 10.2% of revenue** — the *lowest* R&D intensity in
  the eight-company row (AMAT 12.6%, KLA 11.3%, ASML 14.4%, NVMI 16.3%). Lam defends more
  franchise per R&D dollar than anyone in the set.
- **What it defends persists across nodes.** Atomic-scale removal and deposition chemistry
  is not thrown away at each node; the Kiyo, Flex, ALTUS, VECTOR and SABRE families in the
  FY2026 product table are the same families that were there in FY2016.
- **A lapse narrows the lead at the next node; it does not vaporise the installed base**,
  because the qualification lock cuts in Lam's favour on everything already installed —
  and the installed base is **35.9% of revenue** and rose in share through both downturns.

**So: DEFENCE, not replacement — the same ruling the AMAT run made, made here with a
narrower margin, because Lam is the registrant that puts "rapid change" in the first line
of its own Competition section and AMAT does not.** Recorded as the closest call in Q2.
**No key-person dependence [E4-23]** — the moat is in the installed base and the recipes,
not in Timothy Archer.

### [E2-44](1) — THE ONE TEST A NO-MOAT SUPPLIER CANNOT PASS. **VERDICT: INCONCLUSIVE, AND THAT IS WORSE THAN IT SOUNDS.**

**First, the instrument. Recorded sweep of the FY2026, FY2025, FY2024, FY2023, FY2020,
FY2019 and FY2016 10-Ks: NO INSTANCE FOUND of an average selling price, a price list, a
price range, or a unit price.** The only price language in the FY2026 document is a
risk-factor variability list (*"changes in average selling prices, customer mix, and
product mix"*) and — pointing the wrong way — two statements of **buyer** power:

> "large customers may be able to negotiate requirements that result in **decreased pricing**,
> increased costs, and/or lower margins for us"

> customer consolidation may result in customers "**gaining additional influence over the
> pricing of products**"

**That is [E4-37]'s inverse metric read off the filing itself.** *"you can almost measure
the strength of a business over time by the agony they go through in determining whether a
price increase can be sustained."* Lam does not describe agony; it describes the customer
setting the price. **The ACLS instrument — a filed system price range that rose through a
26% revenue collapse — does not exist here.** So the test must run on gross margin, and
gross margin is mix-confounded.

**Second, gross margin through every revenue decline in the filed record, same-vintage:**

| downturn | revenue | change | gross margin, prior → year | move | the filer's own explanation |
|---|---|---|---|---|---|
| **FY2009** | $1,115.9M | **−54.9%** | ~46% → **34.8%** | **−11 pts**, plus an **operating loss of $281.2M** | — |
| **FY2012** | $2,665.2M | **−17.7%** | 46.2% → **40.7%** | **−5.5 pts** | — |
| **FY2019** | $9,653.6M | **−12.9%** | 46.6% → **45.1%** | **−1.5 pts** | *"primarily due to **lower factory utilization**"* |
| **FY2024** | $14,905.4M | **−14.5%** | 44.6% → **47.3%** | **+2.7 pts** ✓ | *"largely due to **a more favorable customer mix**, lower spending on material costs, and higher field resource utilization"* |

**Three of four fail. The one that passes is disqualified by the registrant's own
attribution and by the size of the mix shift underneath it.**

- Management attributes the FY2024 rise to **mix and cost, not price.** A margin that rises
  on *"a more favorable customer mix"* is evidence of mix, not of pricing power.
- **The mix shift in FY2024 was the largest in Lam's filed history. Ex-China revenue fell
  33.6% ($12,965.8M → $8,611.4M) while China revenue rose 41.0% ($4,462.7M → $6,294.0M) to
  42.2% of the company.** CSBG rose to 40.1% of revenue, its record. The FY2024 MD&A names
  both drivers: *"increased revenue generation from our **China regional customers**"* and
  CSBG *"strength in **mature node** equipment."*
- **Lam files no margin by geography and no margin by revenue caption** (recorded sweep,
  seven vintages: no instance found), so **the decomposition cannot be completed from the
  primary source.**
- **FY2019 is the clean observation and it is negative**: *"lower factory utilization"* is
  the price-taker-with-operating-leverage signature, word for word the finding the AMAT run
  made on AMAT's own FY2019.

**Under [E4-18] — "a conclusion that required fighting for it is worth less, not more" —
the FY2024 pass is not claimed.** The honest reading: **Lam has no filed evidence of pricing
power through a downturn, and one contaminated observation that points the right way.**

### THE TWO COHORT TESTS THE BRIEF ASKED FOR — BOTH ARE UNRUNNABLE ON LAM, AND THE ABSENCES ARE THE FINDING [E4-25]

**TEST 1 — THE SEGMENT GROSS-MARGIN TEST [E2-44]/THE ACLS INSTRUMENT. NOT RUNNABLE, AND
LAM IS WORSE PLACED THAN AMAT, NOT MERELY EQUAL.**

> "**The Company operates in one reportable business segment**: manufacturing and servicing
> of wafer processing semiconductor manufacturing equipment. The Company's material
> operating segments qualify for aggregation … **The Company's CODM utilizes segment gross
> margin as the measure of profit or loss** to evaluate operating segment profitability"
> — Note 19, FY2026 10-K

So the answer to the brief's question *"does Lam file segment gross profit at all?"* is:
**yes, and it is useless, because there is one segment.** It is filed for **three years
only** (FY2024–26, on ASU 2023-07 adoption):

| Note 19 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Revenue | $14,905.4M | $18,435.6M | $23,232.7M |
| Segment COGS | 7,423.4 | 9,219.5 | 11,112.6 |
| **Segment gross margin** | **$7,482.0M = 50.20%** | **$9,216.1M = 49.99%** | **$12,120.0M = 52.17%** |
| consolidated gross margin | 47.32% | 48.71% | 50.47% |

**Two independent reasons this cannot serve as KLA's instrument.** (i) One segment means
**no mix is controlled** — the entire point of running the test at segment level is to hold
mix fixed, and there is nothing to hold fixed. (ii) **Revenue rises in all three filed
years** ($14,905 → $18,436 → $23,233), so there is **no revenue decline anywhere inside the
disclosure window** — the identical structural defect that made the test unrunnable on
AMAT. And Lam is worse placed: AMAT has three reportable segments with separately filed
cost of products sold; Lam has one. Note 19 also states that *"depreciation and
amortization and equity-based compensation expense are not independently identifiable
components within the segment's results"* and that *"the Company does not identify assets
by operating segment"* — so no segment capital measure exists either.

**KLA passed this test mix-free** (Semiconductor Process Control revenue −6.3% in FY2024,
segment gross margin **+0.57 points**, 63.89% → 64.46%). **Lam cannot take it.** Recorded
per [E4-25] and per the absence-claim rule: the resolving document would be a segment note
disaggregating cost of goods sold by product line, and **no instance of one was found in any
of the seven Lam vintages read.**

**TEST 2 — THE SERVICE/ANNUITY PROFIT-MIX TEST. NOT RUNNABLE. THE AMAT FINDING IS APPLIED
BY ANALOGY AND LABELLED AS SUCH.**

Lam files the revenue split and nothing else:

| FY | Systems $M | CSBG $M | **CSBG % of revenue** |
|---|---|---|---|
| 2019 | 6,451.1 | 3,202.5 | 33.2% |
| 2020 | 6,625.1 | 3,419.6 | 34.0% |
| 2021 | 9,764.8 | 4,861.3 | 33.2% |
| 2022 | 11,322.3 | 5,904.8 | 34.3% |
| 2023 | 10,695.9 | 6,732.6 | 38.6% |
| **2024 (trough)** | 8,921.6 | 5,983.7 | **40.1%** |
| 2025 | 11,491.3 | 6,944.3 | 37.7% |
| 2026 | 14,885.5 | 8,347.2 | 35.9% |

**No gross profit, no cost of revenue and no margin is filed for either caption in any
vintage** — recorded sweep, seven 10-Ks, no instance found. **And the CSBG caption is not
even a pure annuity:** the filing's own definition is *"customer services, spares,
upgrades, **and new and refurbished non-leading edge products in our deposition, etch and
clean markets**"* — the Reliant equipment line sits inside it, unsized. **So Lam's annuity
claim is LESS checkable than AMAT's, whose AGS is at least a reportable segment with a
filed gross margin.**

**The AMAT finding, applied by analogy and labelled as an analogy, not as a Lam fact:**
AMAT files **AGS gross margin 33.4% against Semiconductor Systems' 54.2%** (FY2025 Note 15,
`0001628280-25-056742`). **In this cohort the annuity is the LOW-margin half**, earning
roughly three-fifths of the equipment margin, because it is a distribution-and-labour
business carrying almost no R&D. **Lam's CSBG is the same shape and larger (35.9% vs
22.5%), so if the analogy holds, Lam's revenue mix is MORE weighted to the low-margin half
than AMAT's.** That is the received story about equipment companies inverted, and the
inversion was established on filed numbers by the AMAT run, not asserted here.

**The weak directional evidence from Lam's own numbers points the same way and is stated at
its true strength, which is low:** consolidated gross margin **47.3% → 48.7% → 50.5%** while
CSBG share fell **40.1% → 37.7% → 35.9%**. More CSBG, lower margin; less CSBG, higher
margin. Directionally consistent with the AMAT finding — and confounded by revenue rising
55.9% over the same two years, so no weight is placed on it.

**What the annuity does pass, cleanly, on revenue:** in FY2024 systems revenue fell **16.6%**
while CSBG fell only **11.1%**, and CSBG's share of revenue has risen in every downturn on
record. That is a real durability property. It is a property of the *revenue*, and this run
does not know what it is worth in *profit*.

### [E2-44](2) — DOLLAR VOLUME GROWTH ON MINOR ADDITIONAL CAPITAL. **PASSES DECISIVELY, AND IT IS THE STRONGEST FACT IN THIS FILE.**

On the [E2-43] denominator, ex-cash — the corrected cohort convention published by the AMAT
run, which found the original row contaminated by cash inside the NTOA denominator, and
which this run **reproduced independently from Lam's filed balance sheet**:

- **Operating profit ÷ ex-cash net tangible operating assets, FY2026: $8,199.8M ÷
  $10,121.5M = 81.0%** *(assets 23,529.7 − goodwill and intangibles 1,895.9 −
  non-interest-bearing current liabilities 5,933.2 − cash 5,579.2)*. The row's 81.1% is
  reproduced to a rounding difference.
- **The series: FY2021 70.9% · FY2022 71.8% · FY2023 69.0% · FY2024 58.5% · FY2025 80.5% ·
  FY2026 81.0%.** Never below 58.5% in six years.
- **[E2-56] incremental: FY2022 → FY2026, operating income +$2,818.0M on ex-cash operating
  capital +$2,629.6M = 107.2%**, against **[E5-40]**'s *"quite satisfactory"* ~12%.
- **The eight-year version: FY2019 → FY2026, operating income +$5,735.1M on +$5,189.3M of
  ex-cash operating capital = 110.5%.**

**[E3-46] — "the second question about the business is a number", asked before the manager:
81.0%, the highest in the eight-company cohort row.** AMAT 73.9% (FY2025), KLA 56.9%
(FY2026). On the incremental measure Lam is first again: **107.2% against AMAT's 95.3% and
KLA's 37.7%.**

**The honest qualification, stated because it decides the file: a very large part of that
incremental return is the AI capex wave arriving, not capital being deployed cleverly.**
Operating income rose $2,818M in four years on a revenue rise of $6,005.7M — operating
leverage on a wave. It is carried into Q4's [E4-41] normalization and into Q5, where the
file actually fails.

### [E2-53] — THE DOMINANCE CLASS. **REFUSED.**

*"Once dominant, the newspaper itself, not the marketplace, determines just how good or how
bad the paper will be. Good or bad, it will prosper."* Lam does not meet that. **In FY2009
it posted an operating loss of $281.2M on a 34.8% gross margin; in FY2013 its operating
margin was 3.3% and net income $113.9M on $3,598.9M of revenue.** The marketplace, not the
position, set the level in both. **Position does not set Lam's economics.**

### [E3-33]/[E5-28] — UNTAPPED PRICING POWER. **NOT CLAIMED.**

*"If you name some business that has incredible pricing power, you're talking about a
business that's a monopoly or a near monopoly"* **[E5-28]**. Lam names a primary competitor
in every one of its four markets, which is the opposite of the claim. **And there is no
market-share figure to support it: recorded sweep of seven Lam 10-K vintages — no instance
found of a market-share figure.** All eight occurrences of "market share" in the FY2026
document are risk-factor boilerplate, and one of them concedes the point: markets *"in which
we either do not compete or **have relatively low market share.**"*

### [E4-55] — WHERE UNITS EXIST, MONITOR UNITS. **NO UNIT SERIES EXISTS. THE SECOND CAP ON THE CLASS.**

**Recorded sweep of the FY2026, FY2025, FY2024, FY2023, FY2020, FY2019 and FY2016 10-Ks:
no instance found of systems shipped, tools shipped, chambers installed, or an installed
base expressed as a count.** "Installed base" appears six times in the FY2026 document and
is never sized — *"our broad installed base"*, *"growth of our installed base"*. The only
counts Lam publishes are **patents and headcount (~23,300 regular full-time employees as of
2026-08-04)**. **Lam can be read in dollars only** — the identical finding both cohort runs
made about AMAT and KLA. With no unit series and no ASP series, **the growth of the last
four years cannot be decomposed into price and volume from the primary source at all.**

### [E2-45] — THE ATTACKER'S TEST, AND THE NAMING ASYMMETRY

Run as a recorded sweep of every SEC-registrant peer's latest annual filing for the string
"Lam":

| registrant | latest annual filing | names Lam? |
|---|---|---|
| **KLA Corp** | 10-K FY2026, `0000319201-26-000027` | **no — zero occurrences** |
| **Applied Materials** | 10-K FY2025, `0001628280-25-056742` | **no — zero occurrences** (AMAT names no competitor at all) |
| ASML | 20-F FY2025, `0001628280-26-011378` | **once, and not as a competitor** — the Board remuneration reference group, *"Semiconductor equipment: Applied Materials \| KLA Corporation \| Lam Research"* |
| Nova Ltd | 20-F FY2025, `0001178913-26-000504` | no |
| Onto Innovation | 10-K FY2025, `0001193125-26-066937` | no |
| Camtek | 20-F FY2025, `0001178913-26-001561` | no |
| Axcelis | 10-K FY2025, `0001104659-26-020461` | no |
| **ACM Research** | 10-K FY2025, `0001628280-26-013231` | **YES, twice, as a principal competitor** |

**ACM Research is the only SEC registrant that names Lam as a competitor**, and what it says
is worth the whole sweep:

> "We consider our principal competitors to be those companies that provide wafer cleaning,
> electrical plating and furnace products to the global market, including **Lam Research
> Corporation, NAURA Technology Group Co., Ltd., SCREEN Holdings Co., Ltd., SEMES Co. Ltd.,
> Tokyo Electron Ltd. and Kokusai Semiconductor Equipment Corporation.** Principal
> competitors for our PECVD and Track products also include **Lam Research Corporation**,
> Applied Materials, Inc., and Suzhou Jingtuo Semiconductor Technology Co., Ltd. **We also
> face additional competitors based in mainland China across multiple product lines due in
> part to the recent entrants of local equipment suppliers.**"

**Lam is named alongside NAURA and a Suzhou company by a filer that says Chinese local
entrants are multiplying — in wet clean and PECVD, two of Lam's four markets, and in the
country that is 33.8% of Lam's revenue.** No filing in the set concedes anything to Lam the
way Onto conceded price to KLA (*"selectively reduced prices on our systems in order to
protect our market share"*). **The attacker's test returns nothing in Lam's favour.**

**The asymmetry, stated fairly in both directions.** Lam names seven competitors; AMAT and
KLA name Lam zero times. Read at Q3 under [E2-26] that is **candor in Lam's favour** — it
tells you what you would want to know if the positions were reversed, and AMAT's silence was
scored against AMAT for exactly that reason. Read here at Q2 it is **evidence against Lam's
own moat**, because the substance disclosed is the existence of close substitutes in every
market Lam serves. **Both readings are correct at their own gate; neither cancels the other.**

### CUSTOMER POWER — THE THIRD CAP, AND IT IS FILED EVERY YEAR

| FY | customers ≥10% of revenue | combined |
|---|---|---|
| 2018 | 25%, 14%, 14%, 13%, 12% | **78%** |
| 2019 | 15%, 14%, 14%, 14% | 57% |
| 2021 | 25%, 12%, 10% | 47% |
| 2023 | 22%, 16% | 38% |
| 2024 | 17% | 17% |
| 2025 | 17%, 15% | 32% |
| **2026** | **16%, 15%, 12%, 12%** | **55%** |

Four customers are **55% of FY2026 revenue.** Set beside the filed statement that *"large
customers may be able to negotiate requirements that result in decreased pricing"*, this is
the [E3-03](2) problem from the demand side: **the buyer is concentrated, sophisticated, and
by Lam's own account holds pricing influence.** A Q2 finding about the business, not a Q3
finding about the managers.

### THE COMPETITOR ROW — INTERROGATED, NOT REBUILT [E3-28]

The row was built by the KLAC run of 2026-09-07 and corrected by the AMAT run of the same
date. **Lam's own cells were recomputed independently from the FY2026 filed statements and
they agree** (operating margin 35.3%, gross margin 50.5%, R&D 10.2%, cash-inclusive ROUNTOA
52.2% against the row's 52.0%, ex-cash 81.0% against the row's 81.1%). Same formula for
every filer: **OP = revenue − cost of revenue − R&D − SG&A**; **ROUNTOA = OP ÷ (assets −
goodwill − intangibles − non-interest-bearing current liabilities)**, year-end — a
CONVENTION of the row, [E2-43] in the closest computable form.

| latest FY | **LRCX** | KLAC | AMAT | ASML | ONTO | CAMT | NVMI | ACLS |
|---|---|---|---|---|---|---|---|---|
| period end | **6/28/26** | 6/30/26 | 10/26/25 | 12/31/25 | 1/3/26 | 12/31/25 | 12/31/25 | 12/31/25 |
| revenue | **$23,232.7M** | $13,579.5M | $28,368.0M | €32,667.3M | $1,005.3M | $496.1M | $880.6M | $839.0M |
| gross margin | **50.5%** | **61.3%** | 48.7% | 52.8% | 49.7% | 50.5% | 57.4% | 44.9% |
| R&D % revenue | **10.2%** ← lowest | 11.3% | 12.6% | 14.4% | 13.1% | 9.7% | 16.3% | 13.0% |
| SG&A % revenue | **4.9%** | 8.3% | 6.2% | 3.9% | 17.6% | 14.9% | 12.3% | 17.7% |
| **operating margin** | **35.3%** | **41.7%** | 29.9% | 34.6% | 19.0% | 25.8% | 28.8% | 14.2% |
| ROUNTOA (cash in denominator) | **52.0%** ← 1st | 48.5% | 34.5% | 49.4% | 15.7% | 12.0% | 12.6% | 10.2% |
| **ex-cash return on NTOA** | **81.1% ← 1st** | **56.9%** | **73.9%** | *(not recomputed)* | | | | |
| **incremental, FY2022→latest** | **107.5% ← 1st** | 37.7% | 95.3% | | | | | |
| service/support % of revenue | **35.9% ← 1st** | 23.0% | 22.5% | 25.1% | 15.7% | 5.6% | 19.9% | 31.9% |
| China % of revenue | **33.8% ← highest of the three** | 29.8% | 30.1% | 29.1% | 7% | 49.2% | 33% | n/d |

**Gross margin through both recent downturns, eleven years, same formula** (the [E2-44]
cohort table, LRCX row in bold):

| FY | **LRCX** | KLAC | AMAT | ASML | ONTO | CAMT | NVMI | ACLS |
|---|---|---|---|---|---|---|---|---|
| 2016 | **44.5** | 61.0 | 41.7 | 45.7 | 51.6 | 41.0 | 45.9 | 37.3 |
| 2018 | **46.6** | 64.2 | 45.0 | 46.0 | 54.2 | 49.4 | 57.8 | 40.6 |
| **2019 ↓** | **45.1 (−1.5)** | 59.1 (−5.1) | 43.7 (−1.3) | 44.7 | 44.1 | 48.3 | 54.2 | 42.0 |
| 2022 | **45.7** | 61.0 | 46.5 | 50.5 | 53.6 | 49.8 | 55.5 | 43.7 |
| **2023 ↓** | **44.6 (−1.1)** | 59.8 | 46.7 | 51.3 | 51.5 | 46.8 | 56.6 | 43.5 |
| **2024 ↓** | **47.3 (+2.7)** | 60.0 | 47.5 | 51.3 | 52.2 | 48.9 | 57.6 | 44.7 |
| 2025 | **48.7** | 60.9 | 48.7 | 52.8 | 49.7 | 50.5 | 57.4 | 44.9 |
| 2026 | **50.5** | 61.3 | — | — | — | — | — | — |

**Peers taken: 8 SEC registrants** against **the seven competitors Lam names itself**, of
which **five cannot be priced from any SEC filing**: Tokyo Electron, ASM International,
SEMES and Wonik IPS have no SEC ticker line; SCREEN Holdings appears only as an unsponsored
ADR with no periodic report; Hitachi, Ltd. deregistered on 2012-04-27 by Form 15F-12B.
**Only AMAT of Lam's seven is priceable.** Adjudicated under the rule the ACLS run set and
both cohort runs carried: **an additional competitor can only narrow a moat, never widen
one** — so the gap **caps the class at NARROW** rather than suspending it as PROVISIONAL,
and becomes a Q6 work order.

**Cohort comparison — five unpriceable head-on competitors sits between KLA's two (at the
edges of its franchise) and AMAT's six (at the centre of its two biggest markets), and
Lam's five are at the centre.**

**What the row says about Lam, in three lines:**
1. **Lam earns the highest return on operating capital in the cohort (81.1%) and the second
   highest operating margin (35.3%), on the lowest R&D intensity (10.2%) and the lowest
   SG&A intensity in the equipment set (4.9%).** On [E3-46]'s number it is first.
2. **It does not earn the highest gross margin — KLA does, by 10.8 points** — and gross
   margin is the pricing measure, which is the measure Lam loses on.
3. **[E3-61]'s limit applies:** the row shows position; it cannot show conduct.

### CHINA AT Q2 — THE MOAT BOUNDARY. **LAM MATCHES NEITHER COHORT PATTERN AND IS THE MOST EXPOSED OF THE THREE.**

Filed geographic revenue, every vintage FY2014–FY2026, **no restatement found across
vintages** (each 10-K restates the trailing two years and every overlap reconciles):

| FY | **China $M** | **China %** | ex-China $M | China YoY | ex-China YoY |
|---|---|---|---|---|---|
| 2014 | 623.4 | 13.5% | 3,983.9 | — | — |
| 2016 | 1,040.0 | 17.7% | 4,845.9 | +57.3% | +5.4% |
| 2018 | 1,784.4 | 16.1% | 9,292.6 | +74.4% | +32.9% |
| 2019 | 2,161.4 | 22.4% | 7,492.2 | +21.1% | −19.4% |
| 2020 | 3,083.9 | 30.7% | 6,960.8 | +42.7% | −7.1% |
| 2021 | 5,137.9 | 35.1% | 9,488.2 | +66.6% | +36.3% |
| 2022 | 5,411.5 | 31.4% | 11,815.5 | +5.3% | +24.5% |
| 2023 | 4,462.7 | 25.6% | 12,965.8 | −17.5% | +9.7% |
| **2024** | **6,294.0** | **42.2%** | **8,611.4** | **+41.0%** | **−33.6%** |
| 2025 | 6,205.1 | 33.7% | 12,230.5 | −1.4% | +42.0% |
| **2026** | **7,859.8** | **33.8%** | **15,372.9** | **+26.7%** | **+25.7%** |

**The answer to the brief's question: NEITHER PATTERN. Lam is a third case.**
- **KLA's pattern was flat dollars while total revenue grew 38%** — China ~$4.05bn for
  three straight years. Its run's finding: **not de-risking.**
- **AMAT's pattern was a real fall — China dollars −$1,588M while ex-China grew $2,780M.**
  Genuine de-risking, the strongest structural fact in AMAT's file.
- **Lam's China dollars are at an ALL-TIME HIGH and rising: $6,294.0M → $6,205.1M →
  $7,859.8M, +26.7% in the latest year.** The share fell from 42.2% to 33.8% only because
  ex-China grew faster. **In dollars Lam is $7.86bn exposed against AMAT's $8.53bn on a
  company 18% larger, and KLA's $4.05bn on a company 42% smaller. As a share of revenue Lam
  is the highest of the three at 33.8%.** The brief's prior — "Lam's China share has run
  higher than either" — is **confirmed on the filed series**, and understated: it is higher
  now, it peaked higher (42.2% against AMAT's 37.2%), and it is the only one of the three
  still growing in dollars.
- **And Lam's FY2024 observation is contaminated harder than either peer's**: ex-China
  revenue fell **33.6%** that year — against AMAT's 11.5% — while China rose 41.0%. **Lam
  had a bigger real customer-side downturn in FY2024 than either peer, entirely concealed by
  China.** That is why the one favourable [E2-44](1) observation above cannot be relied on.

**The moat reading:** a third of the franchise sits in a market where Lam's own filing says
governments *"provide special incentives to government-backed local customers to buy from
local competitors, even if their products are inferior to ours"*, and where a fellow
registrant names NAURA and a Suzhou company as competitors in two of Lam's four markets.
**That is a moat boundary being actively rebuilt against, by a state, with money.**

### [E4-32] — DIRECTION

| widening | narrowing |
|---|---|
| gross margin **44.6% → 50.5%** in three years, +5.9 points; operating margin 29.7% → 35.3% | **the [E2-44](1) pricing test still has no clean pass in eighteen filed years** |
| ex-cash return on operating capital **69.0% → 81.0%**; incremental 107.2% | **China at an all-time-high dollar exposure against a state-funded substitute programme** |
| CSBG revenue **$6,732.6M → $8,347.2M**, counter-cyclical on revenue | **five of seven named competitors unpriceable; customer concentration back to 55%** |
| R&D intensity falling **12.8% → 10.2%** while margin rises — operating leverage on the moat | *or* falling R&D intensity is **under-investment**; the filing does not say which. A Q6 monitoring item, and the same ambiguity the KLA run recorded on itself |

**Direction: MIXED.** Widening on every capital and margin measure; narrowing at the China
edge and unproven on price.

### CLASS AND VERDICT

- Needed or desired **[x]** · no close substitute **[~] per socket, NOT per contest** ·
  not price-regulated **[x]**
- **Class: [ ] WIDE  [x] NARROW  [ ] NONE  [ ] PROVISIONAL · Direction: MIXED**
- **[E4-36] — which of the four causes of extreme success?** *A nonlinear combination —
  atomic-scale process know-how, plus socket-level qualification lock, plus an unusually
  large installed base — **riding a very large wave**.* The wave is not ownable and it is
  priced at Q5.

**WHERE LAM LANDS AGAINST KLAC AND AMAT — what this leg of the cohort was run to determine:**

| | KLAC | **LRCX** | AMAT |
|---|---|---|---|
| [E2-44](1) pricing test | **PASSED mix-free at segment level** (+0.57 pts on −6.3% revenue) | **INCONCLUSIVE** — fails 3 of 4 downturns; the one pass is attributed by the filer to mix, in the year ex-China revenue fell 33.6% | **FAILED** 3 of 4 downturns; segment version unrunnable |
| segment gross-margin instrument | **exists and works** — 90%-of-revenue franchise segment, five years | **does not exist** — one reportable segment, three years, all rising revenue | exists, three years, all rising revenue → unrunnable |
| service profit-mix instrument | does not exist | **does not exist** | **exists — and it killed the claim** (AGS 33.4% vs SSG 54.2%) |
| unpriceable head-on competitors | 2, at the edges | **5, at the centre** | 6, at the centre |
| ex-cash return on operating capital | 56.9% | **81.1% — 1st** | 73.9% |
| incremental return FY2022→ | 37.7% | **107.5% — 1st** | 95.3% |
| gross margin (the pricing measure) | **61.3% — 1st** | 50.5% | 48.7% |
| China dollars | flat ~$4.05bn — not de-risking | **all-time high $7.86bn, +26.7%** | **falling −$1,588M — real de-risking** |
| enforcement action | none | **none** | **$253M BIS settlement + suspended denial order** |

**LAM LANDS BETWEEN THEM AND CLOSER TO AMAT — where the brief's prior put it, but for a
different reason than the brief expected.** The prior was: *better economics than AMAT,
weaker evidence than KLA, and the deciding question is whether Lam can show pricing power
the way KLA did.*
- **The economics half is CONFIRMED and by a wider margin than the prior expected** — Lam
  is first in the cohort on both capital measures, not merely ahead of AMAT.
- **The pricing half is REFUTED in its framing.** The question was not whether Lam *can*
  show pricing power the way KLA did. **It cannot be asked at all**, because Lam files no
  instrument that could answer it: one segment, no ASP, no units, no market share, no
  product-line margin. **KLA has an instrument and Lam has none — that is a difference in
  kind, not in degree**, and it is why Lam sits below KLA rather than beside it.

**THE STRONGEST SINGLE FACT AGAINST THIS VERDICT, stated per [E4-51] so a bear would accept
it as fairly put:** *Lam's own Competition section names a primary competitor in every one
of its four markets and its risk factors concede that the customer sets the price; it files
no price series, no unit series, no market-share figure and no product-line margin with
which to test any pricing claim; its single favourable downturn observation occurred in the
year its non-China revenue fell by a third; five of the seven companies it names cannot be
examined at all; four customers are 55% of revenue and the filing concedes they hold pricing
influence; and a third of the business sits in a country running a state-funded programme to
replace it, where a fellow registrant already names two domestic substitutes in two of Lam's
four markets.* **On that evidence a reasonable analyst could write NONE here — the same
sentence the AMAT run wrote about AMAT.**

**Held IN, NARROW on four filed facts:** (i) a socket-level qualification lock filed by two
independent registrants, consistent with a **35.9% installed-base revenue share that rises
in every downturn**; (ii) **the highest return on ex-cash operating capital in the cohort,
81.0%, never below 58.5% in six years**, with a 107.2% incremental return; (iii) gross
margin up **5.9 points in three years** to an all-time high; (iv) **owner earnings positive
in every one of the eighteen years read, including FY2009's operating loss.**

**Capped at NARROW by five absences and one exposure:** no price instrument, no unit series,
no market-share figure, no segment cost split, no product-line margin — and five of seven
named competitors unpriceable, at the centre of the business.

- **VERDICT: [x] IN — NARROW**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — THE WEIGHT CASE. NONE TICKED → Q3 IS A QUALITATIVE OVERLAY.**
*How much damage can this manager do before I can react?*

- [ ] **Daily execution [E3-38, E3-43, E2-70]** — **not ticked.** Lam's product is a
  differentiated capital good protected by a qualification lock, not *"promises"*. A bad
  quarter is visible in a filed revenue line within ninety days. This is the closest of the
  three calls, because a missed node qualification is a slow, invisible error — but that is
  a Q2 moat question, not a manager-magnification question.
- [ ] **Control [E1-16]** — not ticked. Marketable security, exitable.
- [ ] **Leverage [E3-29]** — **not ticked, emphatically.** $3,750.0M of senior unsecured
  notes at par, **100% fixed rate**, against **$5,579.2M of cash** — **net cash
  $1,829.2M** — and **zero principal due in FY2027 or FY2028.**

**Case declared: OVERLAY.** Findings are recorded; manager quality alone does not stop this
run, and — per the guardrail — cannot start one either.

### HONESTY — binary, permanent, filings-based [E5-16]

**No disqualifier found.** Note 17: *"the Company is **not currently a party to any legal
proceedings that it believes material**"*, with no accrual recorded for litigation or
contingencies. Recorded sweep of the FY2026 10-K for `subpoena`, `Bureau of Industry`,
`Department of Justice`, `investigation`: **no instance found of any enforcement matter,
subpoena, settlement, restatement, or officer departure.** Auditor **KPMG LLP**, ratified
**99.35%** at the 2025 annual meeting.

**This is the cleanest conduct record of the three equipment names.** AMAT paid **$253
million to BIS in Q2 FY2026** and operates under a **suspended denial order**; KLA carries a
2006 options-backdating restatement of **$348M pre-tax across FY1995–2005** with a
terminated CEO. **Lam carries neither.** *Stated as [E5-17] requires: this is the absence of
found disqualifiers, not a finding that the managers are honest. "Sincerity and empathy can
easily be faked."*

### STEP 2 — THE FLAGS. **TWO FIRE, ONE OF THEM HARD; SIX DO NOT.**

**[x] 1. TRUMPETED EARNINGS PROJECTIONS — FIRES, AND IT IS THE REAL ONE.** Lam issues
formal quarterly guidance on **revenue, GAAP and non-GAAP gross margin, GAAP and non-GAAP
operating margin, GAAP and non-GAAP diluted EPS, and diluted share count.** Per **[E3-48]**
— *"pull the company's own past guidance and set it against outturn"* — nine consecutive
quarters, from the 8-K exhibit 99.1 that issued the guidance to the one that reported the
result:

| quarter guided | rev guide (mid) | actual | Δ | non-GAAP EPS guide (mid) | actual | Δ |
|---|---|---|---|---|---|---|
| ended 2024-06-30 | $3.80bn | $3,871.5M | **+1.88%** | $7.50 | $8.14 | **+8.53%** |
| ended 2024-09-29 | $4.05bn | $4,168.0M | **+2.91%** | $8.00 (=$0.80 post-split) | $0.86 | **+7.50%** |
| ended 2024-12-29 | $4.30bn | $4,376.0M | **+1.77%** | $0.87 | $0.91 | **+4.60%** |
| ended 2025-03-30 | $4.65bn | $4,720.2M | **+1.51%** | $1.00 | $1.04 | **+4.00%** |
| ended 2025-06-29 | $5.00bn | $5,171.4M | **+3.43%** | $1.20 | $1.33 | **+10.83%** |
| ended 2025-09-28 | $5.20bn | $5,324.2M | **+2.39%** | $1.20 | $1.26 | **+5.00%** |
| ended 2025-12-28 | $5.20bn | $5,344.8M | **+2.78%** | $1.15 | $1.27 | **+10.43%** |
| ended 2026-03-29 | $5.70bn | $5,841.5M | **+2.48%** | $1.35 | $1.47 | **+8.89%** |
| ended 2026-06-28 | $6.60bn | $6,722.2M | **+1.85%** | $1.65 | $1.82 | **+10.30%** |
| **mean** | | | **+2.33%** | | | **+7.79%** |

**Nine for nine at or above the midpoint on both lines. Never below, on either, in nine
quarters.** That is the identical signature the KLAC run found at sixteen-for-sixteen and
the AMAT run at seven-for-seven — **a midpoint set to be beaten.** Cohort position: Lam's
revenue beat (+2.33%) sits between AMAT's +1.54% and KLA's +2.68%; **its EPS beat (+7.79%)
is the largest of the three.**

**[E5-30] governs the seriousness:** *"once you start it, it's all over. You can't quit …
And forecasting earnings, I can't imagine anything more destructive."* **A guidance culture
is not this year's fact; it is a ratchet.** Lam has been guiding for the whole record read.

**[x] 2. METRIC-SWITCHING [E2-49] — FIRES SOFTLY, ON A SPECIFIC AND DATABLE INSTANCE, WITH
A REAL MITIGATION.** For the **2025/2027 long-term incentive program** the committee changed
how relative TSR is measured — from the Company's TSR against the **performance of the
PHLX Semiconductor Index** to a **percentile rank** among the index's constituents. The
stated reason, in the proxy's own words:

> the prior design "resulted in **oversensitivity to the performance of a small number of
> heavily weighted components of the index** … **as in the recent exceptional stock price
> performance of a small number of companies related to artificial intelligence.**"

**A yardstick was changed because a small number of AI names had made it hard to beat.**
That is [E2-49]'s shape — *"Yardsticks seldom are discarded while yielding favorable
readings."* **Three mitigations, and they are substantial:** the change was **announced
ahead, in writing, with the reason stated** — which is [E2-49]'s own candor case; the
**index itself was not changed**; and the same committee simultaneously imposed a
**cap of 100% of target if absolute TSR is negative**, which is a change *against*
management. **Recorded as a soft fire, not a cockroach.**

**[x] 3. Peer behaviour mindlessly imitated [E2-30](4) — FIRES SOFTLY.** Quarterly non-GAAP
EPS guidance is the sector norm; the **ten-for-one stock split** announced 2024-05-21 and
effective 2024-10-02 followed the same year's splits at NVDA, AVGO and (later) KLA. Neither
touches owner earnings.

**FLAGS THAT DO NOT FIRE, each checked against the filing:**

- **[ ] EBITDA / adjusted-earnings promotion [E4-29] — DOES NOT FIRE, AND THE MARGIN IS THE
  WIDEST IN THIS COHORT.** Recorded sweep: **zero occurrences of "EBITDA" and zero
  occurrences of "non-GAAP" in the FY2026, FY2025, FY2024, FY2023, FY2020 and FY2019 10-Ks**
  (two occurrences of "EBITDA" in the FY2016 vintage, none since). Lam does publish non-GAAP
  figures in its press releases — **and the reconciling items are trivially small.** In the
  June 2026 quarter: GAAP diluted EPS **$1.81** against non-GAAP **$1.82**; GAAP gross margin
  51.7% against non-GAAP 52.0%. **The guidance tables reconcile GAAP to non-GAAP with $2.7M
  to $3.4M of items on $5–8bn of quarterly revenue — five hundredths of one per cent.**
  A company whose non-GAAP is indistinguishable from its GAAP is not running the [E4-29]
  practice, whatever the label on the table.
- **[ ] Serial share issuance [E5-15] — THE REVERSE, EMPHATICALLY.** Shares outstanding
  **1,332,966k (FY2023) → 1,303,769k → 1,268,740k → 1,251,278k (FY2026)**, −6.1% in three
  years; **−22% over ten years on a split-adjusted basis.**
- **[ ] Filed-figure tells [E4-30] — RUN THE OTHER WAY.** *"cash taxes falling as a share of
  reported pretax income"* is the tell. Lam's:

| FY | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| cash tax ÷ pretax | 12.3% | 8.7% | 11.9% | 15.6% | 15.8% | **22.7%** | 16.3% | 16.1% |
| book tax rate | 10.4% | 12.6% | 10.6% | 11.3% | 11.7% | 12.2% | 10.1% | 12.1% |

  **The cash rate rose from 12.3% to 16.1% and exceeds the book rate in seven of eight
  years. Over FY2019–26 Lam paid $5,957.5M of cash tax against $4,286.5M of booked expense —
  $1,671.0M more cash tax than it charged to earnings.** The tell does not fire; it fires in
  reverse, which is the candor direction.
- **[ ] Weak accounting.** SBC expensed in full ($386.4M FY2026). No goodwill impairment in
  any year read. The only restructuring in the record is FY2024's **$61.6M** ($43.4M in COGS
  + $18.2M in operating expenses), **quantified on the face of the income statement** rather
  than buried — and, per **[E5-33]**, it is left inside the owner-earnings series, not added
  back.
- **[ ] Unintelligible footnotes.** Note 19 reconciles segment gross margin to consolidated
  gross margin line by line; Note 18 publishes **quarterly repurchase counts, dollars and
  average price paid per share**; Note 14 publishes the full maturity ladder. Reproduced to
  the dollar at Step 0.
- **[ ] Projects/acquisitions materialising to soak up available funds [E2-30](2) — DOES NOT
  FIRE, AND THIS IS THE STRONGEST SINGLE Q3 FACT.** Acquisitions, filed cash-flow line,
  FY2019–FY2026: **$0 · $0 · $0 · $0 · $120.0M · $0 · $0 · $0. One hundred and twenty
  million dollars of acquisitions in eight years, against $27.7bn of owner earnings.**
  **[E3-40]'s loss-of-focus vector — "neglects its wonderful base business while purchasing
  other businesses that are so-so or worse" — has no instance to point at.** There is nothing
  to run [E4-39]'s acquisition post-mortem *on*, which is the happiest possible reason for
  that test to be unrunnable.
- **[ ] Staff studies to justify the leader's craving; [ ] resists any change in direction.**
  No instance found.

**[E4-52] — DO THE FLAGS CONVERGE INTO A LOLLAPALOOZA? NO.** The guidance ratchet and the
LTIP measurement change both point at *managing the reported outcome*, and the buyback
finding below points the other way. Against them: zero EBITDA, a non-GAAP gap of one cent,
cash taxes above book for eight years, a share count down 22%, $120M of acquisitions in
eight years, and a filing that names its own competitors when its two largest peers do not.
**Two prompts, not a system.**

### STEP 3 — THE PRIMARY TEST [E2-01]

*"a high earnings rate on equity capital employed (**without undue leverage, accounting
gimmickry, etc.**)."* **Reported ROE is unusable here and the reason is [E2-47]'s own
carve-out**: $31.6bn of treasury stock has shrunk book equity to $12.5bn on $23.5bn of
assets, so ROE reads **65.1%** and measures the buyback, not the business. Per **[E2-43]**
the denominator is **unleveraged net tangible operating assets**, and per the AMAT
correction it is shown **both** with and without cash, because the cash-inclusive version
flatters companies that hold little cash:

| FY | operating profit $M | ROUNTOA (cash in denominator) | **ex-cash return** |
|---|---|---|---|
| 2013 | 118.1 | 3.1% | 8.7% |
| 2015 | 788.0 | 13.2% | 41.3% |
| 2017 | 1,902.1 | 23.0% | 32.2% |
| 2019 | 2,464.7 | 28.7% | 50.0% |
| 2021 | 4,482.0 | 41.7% | 70.9% |
| 2022 | 5,381.8 | 48.9% | 71.8% |
| 2023 | 5,174.9 | 40.3% | 69.0% |
| **2024 (trough)** | 4,263.9 | 32.4% | **58.5%** |
| 2025 | 5,901.0 | 43.0% | 80.5% |
| **2026** | **8,199.8** | **52.2%** | **81.0%** |

**A rising series that never went below 58.5% ex-cash in the last six years, and 3.1% in
FY2013.** The 2013 figure is the honest reminder that this is a cyclical business and the
manager did not make either number. **[E2-73] applies:** these are returns on the *underlying
assets*, which is the right denominator for judging the operators — and **[E3-59]**'s
*"the hand they were dealt"* adjustment says most of the improvement from FY2019 is the
industry, not the management.

**The half-owner test [E2-26] — does this reporting tell me what I would want to know if the
positions were reversed? MOSTLY YES, and by a wider margin than either peer on three
specific counts:**
1. **Lam names its competitors, by name, market by market. AMAT names none. KLA's filing
   does not contain the string "Lam".** Under [E2-26] that is candor and it is Lam's.
2. **Lam files China revenue in dollars in Note 19 of every vintage back to FY2014** — not
   merely as a percentage. *(The KLAC run's `competitor-row.md` §5 records LRCX's China
   revenue as "not stated in $". That is a defect in the precedent and is corrected here:
   Note 19 states it in thousands in every year.)*
3. **Lam publishes quarterly repurchase share counts, dollars AND average price paid per
   share**, which is what makes the [E5-08] test below runnable at quarterly resolution.

**Against those, three [E2-26] misses:**
1. **No segment cost split, no product-line margin, no geographic margin** — so the two
   tests at Q2 could not be run at all.
2. **No unit or installed-base series [E4-55]** — a company whose entire thesis is the
   installed base publishes no count of it.
3. **The CSBG caption mixes an annuity with new Reliant equipment sales and does not size
   the split.**

### THE INSTITUTIONAL IMPERATIVE — SCORE ALL FOUR [E2-30]

- [ ] resists any change in current direction — no instance found
- [ ] **projects/acquisitions materialise to soak up available funds — NO. $120M in eight
  years.**
- [ ] staff studies produced to justify the leader's craving — no instance found
- [x] **peer behaviour mindlessly imitated — soft fire** (quarterly guidance; the split)

### CAPITAL ALLOCATION — THE TWO BUYBACK CONDITIONS [E5-08]. **THIS IS WHERE MY PRIOR WAS REFUTED.**

**(1) Ample funds for operations and liquidity? YES.** $5,579.2M of cash against $3,750.0M
of fixed-rate notes with nothing due for two and a half years; $5,857.7M of operating cash
flow in FY2026.

**(2) Repurchases at a MATERIAL DISCOUNT to conservatively calculated intrinsic value?**
**The answer depends on which resolution you read it at, and BOTH readings are reported.**

**THE ANNUAL VIEW — ten years, split-adjusted to post-split shares and prices:**

| FY | shares repurchased (post-split, 000) | cash $M | **avg price paid, post-split** |
|---|---|---|---|
| 2017 | 53,220 | 811.7 | **$15.25** |
| 2018 | 147,860 | 2,653.4 | **$17.94** |
| 2019 | 210,590 | 3,780.5 | **$17.95** |
| 2020 | 53,710 | 1,369.7 | **$25.50** |
| 2021 | 58,190 | 2,717.6 | **$46.70** |
| 2022 | 65,740 | 3,845.7 | **$58.50** |
| 2023 | 46,090 | 2,062.5 | **$44.75** |
| 2024 | 37,241 | 2,848.8 | **$76.49** |
| 2025 | 41,812 | 3,409.4 | **$81.54** |
| **2026** | **25,034** | **3,847.2** | **$153.68** |
| **total** | **739,487** | **$27,346.5M** | **$36.98 weighted average** |

On the annual series the pattern reads like KLA's: **the largest outlay in the record,
$3,847.2M, was made in the year of the highest average price, $153.68.** Dollars spent rose
4.7x while the price rose 10.1x.

**THE QUARTERLY VIEW — and Lam files it, which KLA's annual table does not resolve. THIS IS
THE REFUTATION.** Note 18 and Item 5 publish shares, dollars and **average price paid per
share every quarter**:

| quarter | shares (000) | cash $M | **avg price paid** |
|---|---|---|---|
| **FY2025 Q1** (Sep 2024) | 11,952 | 1,003.7 | $83.97 |
| FY2025 Q2 (Dec 2024) | 8,336 | 650.4 | $78.03 |
| FY2025 Q3 (Mar 2025) | 4,448 | 346.5 | $77.91 |
| **FY2025 Q4 (Jun 2025)** | **15,763 ← the largest quarterly count in the record** | **1,306.8** | **$76.18 ← the lowest price of the year** |
| FY2026 Q1 (Sep 2025) | 9,686 | 990.0 | $105.67 |
| FY2026 Q2 (Dec 2025) | 9,387 | 1,442.1 | $153.62 |
| FY2026 Q3 (Mar 2026) | 3,516 | 796.4 | $210.57 |
| **FY2026 Q4 (Jun 2026)** | **811 ← the smallest quarterly count in the record** | **245.9** | **$325.14 ← the highest price in the record** |

> **Across eight consecutive filed quarters the price rose from $76.18 to $325.14 — 4.3x —
> and the quarterly repurchase fell from 15,763 thousand shares to 811 thousand, a 95%
> reduction, with the dollars cut from $1,306.8M to $245.9M. Lam bought the most when it was
> cheapest and the least when it was dearest.**

**That is [E5-24]'s first law — *"what is smart at one price is dumb at another"* — run
FORWARD, and it is the first time in this queue that a large repurchaser has done so.** The
KLAC run found the law *"being run in reverse"*; the AMAT run found the same. **Lam is the
counter-example, and the brief's prior that Lam would replicate KLA's failure is REFUTED on
the filed quarterly series.**

**What condition (2) still fails on, stated honestly.** The test is a **material discount
to conservatively calculated intrinsic value**, not merely a correct direction. Against this
run's zero-growth value band at the sovereign (Q5 below: **~$50 to ~$75 per share**), **every
quarter in the table above was executed above the top of the band** — the cheapest, $76.18,
by about 2%; the dearest, $325.14, by 4.3x. **So condition (2) fails on the level and passes
on the direction.**

- **→ CAPITAL ALLOCATION FLAG, RAISED — but at the lowest severity of the three equipment
  names.** Stated with the humility clause **[E4-13]**: *"it is natural for CEOs to be
  optimistic about their own businesses. They also know a whole lot more about them than I
  do"*, and **[E5-08]**'s *"infractions, even serious ones, are innocent; many CEOs never
  stop believing their stock is cheap."* **The flag binds POSITION SIZE, never the discount
  rate** — and since Q5 fails on price, no position exists for it to bind.
- **[E4-31]'s third condition — was the register adequately informed?** Partly. Lam publishes
  its own repurchase prices, its geographic revenue in dollars, its competitor names and its
  segment reconciliation. It does **not** publish the unit series, market share, or
  product-line margin a shareholder would need to estimate value independently.
- **[E2-51]'s refusal tell does not apply**: Lam buys, aggressively, and has retired
  roughly a fifth of the company.

### [E2-52]/[E2-60] — ARE THE DISTRIBUTIONS FUNDED BY REPLACING THE CAPITAL?

| FY2019–FY2026, $M | |
|---|---|
| owner earnings (capex end, eight years) | **27,661.7** |
| buybacks | 23,847.0 |
| dividends | 7,224.3 |
| **total returned** | **31,071.3 = 112.3% of owner earnings** |
| senior notes issued March 2019 + May 2020 | **4,500.0** |
| notes repaid since | (750.0) |
| **net cash position today** | **+$1,829.2M** |

**Stated plainly and not smoothed: Lam returned more than it earned over eight years, and it
issued $4.5bn of notes inside that window.** [E2-60]'s third dimension of maintenance —
*"its financial strength"* — was **spent**, from zero debt to $4.5bn. **The limb still
holds**, because the balance sheet remains in net cash and nothing is due for two and a half
years, but **it holds with less room than it had in 2018, and that is a fact about the
capital allocation, not about the operations.** Dividends have risen every year since
initiation in April 2014; the FY2026 declared rate is **$1.04 per share, $1,304.1M**, a
**22.3% payout of owner earnings** at the capex end.

### PAY, OWNERSHIP AND THE VOTE [E3-59]

- **Company-selected pay measure: "Non-GAAP operating income as a percentage of revenue."**
  Plus relative TSR and non-GAAP gross margin. **Not EBITDA, not adjusted EPS** — and since
  Lam's non-GAAP is within one cent of its GAAP, the measure is close to an honest operating
  margin. **A better-chosen metric than any in this cohort.**
- **Pay versus performance, PEO Timothy Archer:** SCT $15.5M (FY2021) · $16.9M · $18.3M ·
  $30.1M · **$28.3M (FY2025)**; compensation actually paid $56.9M · $10.3M · $35.5M ·
  **$71.7M** · $14.7M. TSR on an initial $100: 211 · 152 · 209 · 368 · **340**; peer group
  171 · 145 · 190 · 300 · **307**. **CAP fell 79.5% in FY2025 as TSR fell — the plan bites in
  both directions, which is the test [E2-49] actually asks.**
- **Ownership [E2-48]:** all **17 directors and executive officers hold 3,971,889 shares of
  1,261,032,300 = 0.315%**; **CEO Archer holds 1,481,175 shares = 0.117%**, worth ~$456M at
  the run price. **Better than KLA's sixteen insiders at 0.0915% and its CEO at 0.026%, and
  roughly level with AMAT's 0.303% / 0.176%.** These are highly paid employees with a real
  stake, which is more than the KLA run could say.
- **The vote, 2025 annual meeting (8-K `0000707549-25-000094`, Item 5.07), and it is the
  weakest of the three:** **Say-on-Pay 90.83% for** (KLA 92.39%, AMAT 91%); **director
  Michael R. Cannon drew 19.2% against** and Abhijit Talwalkar 10.1%; and a stockholder
  proposal titled *"Realistic Shareholder Ability to Call for a Special Shareholder
  Meeting"* took **41.36% of votes cast.** A 41% shareholder proposal is a real signal about
  governance and is recorded; it is not a conduct finding.

### THE GUARDRAIL — checked before writing the verdict

- [x] **Confirmed: nothing in this Q3 is being used to promote the name.** The $120M-in-eight-
  years acquisition record and the forward-running buyback are the two best facts in this
  file about the *managers*, and **[E2-37]/[E3-39] say a good jockey does not upgrade the
  horse.** Q2 stands at NARROW regardless.
- [x] **This business does not require a great manager**, so [E4-23] records nothing at Q2.
- [x] **No great manager is the reason to act**, so [E2-35]/[E2-36]'s excisable-cancer
  branch does not open.

- **VERDICT: [x] IN — as a QUALITATIVE OVERLAY, with two flags live (guidance culture; one
  LTIP metric change) and one capital-allocation flag raised on the LEVEL of the buyback
  price while its DIRECTION passes.**
  *IN = no disqualifier found. NOT a finding that the managers are honest **[E5-17]**.
  IN never promotes.*

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**

**Construction (the framework's CONVENTION):** owner earnings = **operating cash flow −
stock-based compensation − (c)**, with (c) shown at both ends of the band: **total capital
expenditure** (the conservative end) and **depreciation and amortization** (the [E3-44]
default). Every figure is taken at its **originally filed** value from the vintage that first
reported it, so no restated input sits silently inside a window — the INTC defect of
2026-09-07. **Recorded restatement check across nine vintages: no instance found of a
restated OCF, SBC, D&A or capex figure for Lam.** The working-capital increment is inside
OCF by construction, satisfying [E2-23] constraint 3, and it **bites hard** here (below).

**THE SPREAD CAVEAT IS LIVE AND THE PUBLISHED 20.9% IS WRONG. Rebuilt over THIRTEEN windows
and BOTH (c) ends [E4-25, E4-38]:**

| window | **capex end $M** | yield | **D&A end $M** | yield | growth needed to clear the 10% floor |
|---|---|---|---|---|---|
| 3-yr FY2024–26 | 4,512.7 | 1.172% | **4,824.3** | **1.253%** | 8.83% |
| 4-yr FY2023–26 | 4,482.2 | 1.164% | 4,755.7 | 1.235% | 8.84% |
| **5-yr FY2022–26 (the corpus default [E2-42])** | **4,044.7** | **1.051%** | 4,305.9 | 1.119% | 8.95% |
| 6-yr FY2021–26 | 3,873.7 | 1.006% | 4,098.4 | 1.065% | 8.99% |
| 7-yr FY2020–26 | 3,568.1 | 0.927% | 3,751.3 | 0.974% | 9.07% |
| **8-yr FY2019–26 — THE JUDGED WINDOW** | **3,457.7** | **0.898%** | 3,617.3 | 0.940% | **9.10%** |
| 9-yr FY2018–26 | 3,319.1 | 0.862% | 3,455.1 | 0.897% | 9.14% |
| 10-yr FY2017–26 | 3,159.4 | 0.821% | 3,266.8 | 0.849% | 9.18% |
| 11-yr FY2016–26 | 2,966.0 | 0.770% | 3,053.2 | 0.793% | 9.23% |
| 12-yr FY2015–26 | 2,756.5 | 0.716% | 2,829.8 | 0.735% | 9.28% |
| **13-yr FY2014–26** | **2,580.5** | **0.670%** | 2,636.8 | 0.685% | **9.33%** |
| *best single year ever filed (FY2025, D&A end)* | | | *5,443.6* | *1.414%* | *8.59%* |
| *worst year in the eight-year window (FY2020, D&A end)* | | | *1,668.7* | | |

- **TRUE WIDTH ACROSS THE WINDOW MEANS: $2,580.5M to $4,824.3M = 1.87x, an 87.0% spread**
  — against the row's **20.9%**. **Eleventh consecutive run to find the published spread
  materially too narrow.**
- Including the best single year ever filed the range is **$2,580.5M to $5,443.6M = 2.11x.**
- **[E4-25]'s "too wide to reach a conclusion" test: it does NOT bite here, and that is the
  point.** Every construction in the table — every window, both (c) ends, and the best year
  Lam has ever filed — yields **under 1.42% against a 5.24% sovereign.** The range is
  enormous and **lies entirely on one side of the answer.**

**Owner earnings by year (capex end · D&A end), $M:**

| FY | OCF − SBC | **(c)=capex** | **(c)=D&A** | capex ÷ D&A |
|---|---|---|---|---|
| 2017 | 1,879.3 | 1,721.9 | 1,572.4 | 0.51 |
| 2018 | 2,483.5 | 2,210.1 | 2,157.1 | 0.84 |
| **2019 ↓rev** | 2,988.8 | **2,685.3** | 2,679.5 | 0.98 |
| 2020 | 1,937.3 | 1,734.0 | 1,668.7 | 0.76 |
| 2021 | 3,368.0 | 3,018.9 | 3,060.8 | 1.14 |
| 2022 | 2,840.6 | 2,294.6 | 2,506.9 | 1.64 |
| 2023 | 4,892.3 | 4,390.8 | 4,549.9 | 1.47 |
| **2024 ↓rev** | 4,359.2 | **3,962.5** | 3,999.5 | 1.10 |
| 2025 | 5,829.9 | 5,070.7 | **5,443.6** | 1.97 |
| **2026** | **5,471.3** | **4,504.9** | **5,029.7** | **2.19** |

**OWNER EARNINGS ARE POSITIVE IN ALL EIGHTEEN YEARS READ, including FY2009 — the year Lam
posted an operating LOSS of $281.2M on revenue down 54.9%.** *Reliable in sign; violently
variable in size — a range of roughly 3.3x inside the eight-year window alone.* **[E5-29]
governs: volatility is not risk.**

**MAINTENANCE CAPEX — A DISCLOSED JUDGMENT [E2-23], WITH THE CORPUS DEFAULT [E3-44] AND ITS
EXCEPTION CLASS [E5-20] BOTH TESTED.**

The [E5-20] exception applies *"where the business is capital-intensive … anything whose own
filing says depreciation understates renewal."* **Lam's filing says the opposite, in terms:**

> "The increase of $214.1 million in net cash used for investing activities during fiscal
> year 2026 compared to fiscal year 2025 was primarily due to **higher capital expenditures
> to support lab investments in the United States and global growth in manufacturing
> facilities.**"

**That is growth capital named as growth capital by the registrant.** Net PP&E ran
$1,071.5M (FY2020) → **$2,956.5M (FY2026), 2.76x**, while depreciation ran 1.93x. Capex is
**4.2% of revenue**; this is **not** the railroad class. **So the [E3-44] default is the
defensible reading and the capex end is the conservative one.**

**(c) IS NEVERTHELESS JUDGED AT TOTAL CAPITAL EXPENDITURE, and the reason is a leak the
cash-flow statement discloses and the investing line does not contain:**

> non-cash: *"**Transfers of finished goods inventory to property and equipment**
> $125,691"* (FY2026; $90,873 FY2025; $71,267 FY2024)

**Lam converts finished tools into its own fixed assets without the cash crossing the
investing line.** True FY2026 capital additions are **$966.4M + $125.7M = $1,092.1M**, 13.0%
above the filed capex line — the same shape as UAL's operating-lease leak and DAL's, found
by their runs. Judging (c) at total capex **absorbs that leak and then some**, and it is
where this run sits.

- **Band used: $2,580.5M (13-yr, capex) to $4,824.3M (3-yr, D&A).**
- **JUDGED OWNER EARNINGS: $3,457.7M — the eight-year FY2019–26 mean at total capex.**
  **The judgment, disclosed as a judgment:** the five-year default window FY2022–26 lies
  **entirely inside the wave**; the 12- and 13-year windows contain a company a fifth of the
  present size; **FY2019–26 is the shortest window that contains an uncontaminated revenue
  decline (FY2019, −12.9%, with no China pre-buy in it) and the pre-wave base (FY2020).**
  **It is the same construction the KLAC and AMAT runs used, for the same reason.** The full
  $2,580.5M–$5,443.6M band is carried, not discarded.
- **The capex band does NOT change the verdict** (0.898% vs 0.940%), so [E2-23]'s
  "if the capex band changes the verdict → UNKNOWABLE" does not trigger.
- **Stock compensation subtracted in full [E5-06]: $386.4M in FY2026, and in every one of
  the eighteen years.** Per **[E3-70]** the reported charge is the **floor** of the correct
  subtraction, not the measure; no market-value adjustment is attempted, and any
  understatement makes owner earnings **lower**, not higher.
- **R&D is above the OCF line and therefore already deducted** — $2,375.9M, 10.2% of
  revenue. The QCOM ruling applies in Lam's favour: owner earnings are conservative on this
  axis. **But the direction is a Q6 item: R&D fell from 12.8% of revenue (FY2024) to 10.2%
  (FY2026) — operating leverage, or under-investment, and the filing does not say which.**
- **ASC 842:** operating-lease ROU assets are inside OCF; **no finance-lease ROU asset is
  tagged in any year** ($147 thousand of "other financing arrangements" on the balance
  sheet). The COST/HD finance-lease addendum does not bite. **No capitalized-software
  caption exists** — the HAS defect does not bite.

### [E4-41] — NORMALIZE THE MEAN DOWN FOR LUCK. **THE SCREEN'S STEP IS TOO SMALL, AND THE TOOL'S OWN REFUSAL BRANCH SAYS SO.**

*"Favourable exogenous breaks in the window are named and removed before the mean is
trusted"* **[E4-41]**.

**The break, named: the AI wafer-fab-equipment wave, FY2021–FY2026.** The registrant's own
Item 1A names the three ways it ends:

> "changes in actual or anticipated AI-driven demand for AI-related infrastructure or
> compute power … including due to **slower-than-anticipated adoption of AI technologies,
> increases in compute efficiency, or oversupply of AI-related infrastructure compute
> power**"

*(KLA's Item 1A puts it more bluntly — *"the sustainability of such elevated investments
cannot be assured"* — and that sentence describes Lam's customers as much as KLA's, because
they are the same twenty customers.)*

**The step, computed by hand on owner earnings at the capex end:**

| | |
|---|---|
| pre-wave five-year mean, **FY2015–19** | **$1,620.3M** |
| wave five-year mean, **FY2022–26** | **$4,044.7M** |
| **STEP** | **2.50x** |
| *alternative pre-wave base FY2014–18* | *$1,176.9M → **3.44x*** |

**The screen row read `level_shift 1.68 STEP UP · level_shift_oe 1.64 STEP UP`, and the
brief noted "the two AGREE here". They agree because they are computed on the same
contaminated window.** Reproduced exactly: `Screens/floor_screen.py:level_shift(vals,
tail=3)` on a **nine-year** series returns **1.683** on operating cash flow and **1.658** on
owner earnings — the row's figures to three digits. **A nine-year series means the "earlier"
half is FY2018–FY2023, which already contains three years of the wave.** The base is
contaminated by the step it is measuring, and **agreement between two measures computed on
the same contaminated base is not corroboration.**

**And the same function, given Lam's FULL eighteen-year filed series, REFUSES the ratio:**

> "**EARLY HALF STRADDLES ZERO** … a ratio against it is undefined in substance even where
> it computes (**it gives 3.08x**). **The level HAS changed and the multi-year mean is
> averaging TWO DIFFERENT BUSINESSES. READ THE FILING [E4-25].**"

**The refusal is more informative than the number, and the refusal is what a reader of the
row never sees.** That is the defect class the queue's own FOLD note names — *a diagnostic
that exists but never reaches the reader* — and it is recorded as a tooling finding.
**Cohort tally: KLAC 1.73 reported vs 3.86 hand-computed; AMAT 2.0 vs 2.74; LRCX 1.68 vs
2.50. Third consecutive firing, always in the same direction.**

**Distorted years named in BOTH directions [E5-11, E4-41]:**
- **UP — FY2021–26, the wave.** Step 2.50x. Removed by judging the eight-year window rather
  than the five.
- **UP — FY2024, China.** China was 42.2% of revenue on legacy-node pre-buying while
  **ex-China revenue fell 33.6%.** The one apparently-resilient year in the window is not
  clean, and Q2's [E2-44](1) reading was withdrawn on exactly this ground.
- **DOWN and KEPT IN per [E5-33]:** FY2024's **$61.6M restructuring charge** ($43.4M in COGS
  + $18.2M in operating expenses) is a real cost borne by shareholders and is **not added
  back anywhere in this file.**
- **[E3-55] scope check — distortion, not See's-in-August noise.** See's loses money eight
  months a year around a level that is known. Lam's **level** moved 2.50x, and the filing
  names three mechanisms by which the new level reverses.

### Great, good, or gruesome? **[E4-20]**

- [x] **GREAT — on the [E3-46] number, and it is the best in the cohort.**
- [ ] good  [ ] gruesome

**Evidence.** *"The great one pays an extraordinarily high interest rate that will rise as
the years pass."* **81.0% pre-tax return on ex-cash net tangible operating assets (FY2026),
a series that has not been below 58.5% in six years, and the highest of the three equipment
names — against AMAT's 73.9% and KLA's 56.9%.** Incremental return on operating capital
FY2022→FY2026: **107.2%**, first in the cohort. Over **FY2019–26 Lam earned $27,661.7M of
owner earnings and returned $31,071.3M of it — 112.3% — while operating income went
$2,464.7M → $8,199.8M, 3.3x.** *A business that more than triples its operating profit while
distributing more than it earns is [E4-20]'s great account, and it is the same shape the
AMAT and KLAC runs found in their own names.*

**The qualification, and it is required.** [E4-20]'s *"rise as the years pass"* limb belongs
to the cycle, not to the position: the rate fell in **FY2009, FY2012, FY2013, FY2019 and
FY2024**, and was **3.1%** on the same measure in FY2013. **[E2-53]'s dominance class was
refused at Q2 for exactly this reason.** Lam is a great business inside an industry that
takes the rate away from it every few years.

### Staying power — score all three **[E5-11]**

**(1) A LARGE AND RELIABLE STREAM OF EARNINGS — YES, with the caveat stated.** Owner
earnings positive in **all eighteen years read**, including the year of an operating loss.
Reliable in sign; a 3.3x range inside the judged window. **[E5-29]: volatility is not risk.**

**(2) MASSIVE LIQUID ASSETS — YES, and it is the plainest balance sheet of the three.**
Cash and equivalents **$5,579.2M** (plus $18.8M restricted) against **$3,750.0M** of senior
notes at par — **net cash $1,829.2M**, covered **1.9x by a single year's judged owner
earnings.** No marketable-securities book, no unnamed equity position (the AMAT flag has no
Lam analogue), no held-to-maturity portfolio: it is cash.

**(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — PASSES, AND MORE CLEANLY THAN EITHER
PEER. ← the one that usually kills.** Note 14's ladder:

| fiscal year | principal due | interest |
|---|---|---|
| **2027** | **$0** | $128.0M |
| **2028** | **$0** | $128.0M |
| 2029 | $1,000.0M | $116.3M |
| 2030 | $750.0M | $87.4M |
| 2031 | $0 | $73.8M |
| thereafter (2049/2050/2060) | $2,000.0M | $1,508.7M |
| **total** | **$3,750.0M** | $2,042.2M |

**Zero principal due for two and a half years**, 100% fixed-rate senior unsecured, no
financial-maintenance covenants disclosed, and the only trigger is a **change-of-control
repurchase at 101%**. Against it: **$5,579.2M of cash** and **$2,279.2M of deferred profit**
— customer money already received, which is **[E3-52]**'s *"benefit of debt … with none of
its drawbacks."* *(AMAT's earliest maturity is $1,200M about 13 months out; KLA's is $800M
in March 2029.)* Purchase obligations of **$1,056.9M due in FY2027** are the only other
near-term call and are covered five times by cash alone.

**[E2-54] coverage — "all interest, both payable and accrued, comfortably met out of current
cash flow net of ample capital expenditures":** interest $128.0M against judged owner
earnings of $3,457.7M — which is already **after** full capital expenditure — is **27.0x**;
on the worst year in the eight-year window (FY2020, $1,734.0M) it is **13.5x**; on FY2009's
$67M-equivalent trough it would still be covered. **Certain, not merely likely [E2-55].**

**[E5-39] — "never dependent on the kindness of strangers." MET ON SUBSTANCE, WITH A LITERAL
FAILURE AND A LIVE DIRECTION TO RECORD.** Lam maintains a **$2.00bn commercial paper
program** and a **$2.00bn revolving credit facility** (expandable to $2.75bn, maturing
2030-01-25) that exists as the CP backstop. **Nothing is drawn on either at 2026-06-28.**
Read literally Lam would fail [E5-39] as AMAT does. **Two things make it worth recording
rather than waving through:**
1. **In March 2026 the CP program was increased from $1.50bn to $2.00bn**, and the filing
   states the proceeds *"may be used for general corporate purposes, **including repurchases
   of our Common Stock**."*
2. **That increase was made in the fiscal quarter in which the average repurchase price hit
   $210.57, on the way to $325.14.** Nothing was drawn — but **the capacity to fund buybacks
   with short-term paper was enlarged by a third at the top of the price record.** It is the
   one place in this file where the KLA failure pattern has infrastructure built for it, and
   it is a **Q6 tripwire**, not a present fact.

**Leverage, named and quantified [E4-16, E3-29]** — *there is no ratio ceiling in this
framework and the corpus supplies none:* **$3,750.0M gross, negative $1,829.2M net.** Debt
rose from **zero before March 2019** to $4,500M and has since been reduced by $750M; that
rise funded the distribution programme and is recorded at Q3 under [E2-60].

**[E2-23] constraint 3 — the working-capital increment, INCLUDED BY CONSTRUCTION, AND IT
BITES HARDER THAN IN EITHER PEER.** In FY2026 alone the cash-flow statement shows
**accounts receivable −$1,962.1M** (against −$858.7M the prior year) as receivables ran
$3,378.1M → **$5,339.7M, +58.1% on revenue +26.0%**, and **deferred profit −$286.4M** after
a +$1,147.8M inflow the year before. **Reported net income rose 35.6% and operating cash
flow FELL 5.1%.** Inventory has run $1,540.1M (FY2019) → **$4,276.1M**, a $2,736.0M build,
every dollar of it a use of cash inside owner earnings. **This is the single most important
mechanical fact in Q4: FY2026's record profit did not convert to record cash, and the owner
earnings series is the one that shows it.**

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40]**

*Modelled on **exposure, not experience** [E4-40] — a benign loss history late in a good
cycle is "not only useless, but actually dangerous."* **Three mechanisms. None of them kills
the business; all three impair the level, which is a Q5 fact.**

**1. THE CAPACITY GLUT — the [E2-27] mechanism proper, and the likeliest.** *"viewed
collectively, the decisions neutralized each other and were irrational."* Twenty customers
are building fabs at once on one demand thesis; Lam's own Note 1 opens by saying leading
indicators *"may not be any more reliable than in prior years."*
**Quantified from filed figures.** The filed FY2009 precedent is **revenue −54.9%, gross
margin 34.8%, an operating loss of $281.2M — and owner earnings still positive.** Applied to
today: a **40% revenue decline** takes revenue to **$13,940M**. At the FY2024 trough gross
margin of 47.3% that is **$6,594M of gross profit** against a fixed R&D + SG&A base of
**$3,525.5M** → **operating income ≈ $3,068M.** At the FY2009 crisis margin of 34.8% it is
**$4,851M of gross profit → operating income ≈ $1,326M**, still positive.
**It takes roughly a 55% revenue decline at a 40% gross margin (revenue ~$10.5bn, gross
profit ~$4.2bn) to bring the operating line near $700M**, and a working-capital unwind of
the $4.3bn inventory and $5.3bn receivable books would *release* cash in that year, as it
did in FY2024 (+$528.7M of inventory, +$303.4M of receivables). **Owner earnings in a −40%
year land near $1.7bn–$2.5bn — inside the 12- and 13-year window means already published
above.**
**Likelihood: [x] a real possibility on a five-to-ten-year view. Fatal: no.**

**2. CHINA — the [E4-40] exposure question, and Lam is the most exposed of the three.**
China is **$7,859.8M, 33.8% of revenue, an all-time high in dollars and still growing
26.7%.** Lam's own filing says foreign governments *"provide special incentives to
government-backed local customers to buy from local competitors, even if their products are
inferior to ours"*, and a fellow registrant (ACM Research) already names **NAURA** and a
Suzhou company as competitors in two of Lam's four markets.
**Quantified.** Total loss removes **~$3,969M of gross profit** at the consolidated 50.5%
margin against FY2026 operating income of $8,199.8M — **a 48% cut, taking operating margin
from 35.3% to roughly 18%** and judged owner earnings to roughly **$1.6bn–$1.9bn.**
**And the second-order effect is the one that matters:** the fixed R&D and SG&A base of
$3,525.5M does not shrink, so a third of the revenue leaving takes more than a third of the
profit.
**Likelihood of total loss: a low-level possibility. Likelihood of material erosion at
legacy nodes: [x] a real possibility** — the FY2024 pre-buy already happened and the FY2026
dollars are a record, which means the exposure is larger now than when either peer measured
theirs.
**THE COUNTER-EXPOSURE, and it is Lam's alone in this cohort:** *"**China is the primary
source of supply of certain rare earth elements critical to the manufacture of certain of
our products.** The Chinese government has imposed export controls and license requirements
on certain rare earth elements … (which have been **suspended in part until November 2026**
(unless extended))."* **Lam is exposed to China as a third of its demand AND as a chokepoint
in its supply, with a filed expiry date thirteen weeks after this run.** Not quantifiable
from the filing; recorded as a named exposure with a date.

**3. COMPETITIVE DISPLACEMENT AT THE NODE — the mechanism Q2 could not price.** Lam names a
primary competitor in every one of its four markets and **five of the seven cannot be
examined from any SEC filing.** Displacement happens at the qualification cycle, which turns
over every two to three years. Four customers are **55% of revenue**; losing one process step
at one node at one of them is worth several hundred million dollars of gross profit a year,
compounding as the node scales.
**Quantified at the margin:** Lam's largest customer is 16% of revenue = **$3,717M**; a
single-step loss of a quarter of that customer's Lam spend is **~$930M of revenue, ~$470M of
gross profit, ~5.7% of operating income** — and it would not be visible in the filing until
it had already happened, because **there is no unit series, no ASP series and no market-share
figure [E4-55]**.
**Likelihood at the margin: [x] a real possibility. Wholesale displacement: a low-level
possibility**, because the qualification lock cuts both ways.

**THE BEAR CASE AS ITS HOLDERS WOULD STATE IT [E4-51]:** *Lam is a supplier whose owner
earnings stepped up 2.5x because twenty customers decided at the same time to spend more
than they ever have, on a wave the company's own risk factors say can end three different
ways; it publishes no unit series with which to show any of that growth was volume rather
than price or spending; it has never once, in eighteen filed years, held its gross margin
through a revenue decline except in the single year its non-China revenue collapsed by a
third; a third of the business is in a country running a state-funded programme to replace
it, which is simultaneously a chokepoint in its own supply chain; four customers are 55% of
revenue and the filing concedes they hold pricing influence; its record profit year
converted to LESS operating cash than the year before; and it enlarged a commercial-paper
programme earmarked for buybacks in the quarter its stock hit an all-time high.* **Every
clause of that is filed, and I accept it as fairly put.**

- **VERDICT: [x] IN — GREAT on the [E3-46] number and first in its cohort on it; the range
  is wide, one-sided, and survivable.**

---
✅ **Q1 IN · Q2 IN · Q3 IN · Q4 IN — the hard sequence is satisfied and Q5 opens.**
Fifth name in this queue to reach Q5 on all four business gates, and the third of the
three equipment names.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, BEFORE THE RANKING [E4-28, E3-13].** *"that's the figure we quit on … that's
true whether short rates are 6 percent or whether short rates are 1 percent."*

**1. THE YIELD**

| construction | owner earnings $M | **yield** | points vs 5.24% |
|---|---|---|---|
| *best single year ever filed (FY2025, D&A end)* | 5,443.6 | **1.414%** | −3.83 |
| 3-yr FY2024–26, D&A end | 4,824.3 | 1.253% | −3.99 |
| 5-yr FY2022–26 (corpus default), capex end | 4,044.7 | 1.051% | −4.19 |
| **JUDGED — 8-yr FY2019–26, capex end** | **3,457.7** | **0.898%** | **−4.34** |
| 10-yr FY2017–26, capex end | 3,159.4 | 0.821% | −4.42 |
| 13-yr FY2014–26, capex end | 2,580.5 | **0.670%** | −4.57 |

- **owner earnings $3,457.7M ÷ market cap $384,969M = 0.898%** · **sovereign 5.24%**
- **Band: 0.670% to 1.414%, and 1.414% is the best single year Lam has ever filed.**
- Net cash of $1,829.2M ($1.46/share) lifts the judged yield to **0.902%.** Immaterial.
- **Every lengthening of the window lowers the yield, without a single exception.** That is
  the same result the KLAC and AMAT runs reported, and it is what a wave looks like from
  inside.

**2. WHAT THE PRICE ALREADY ASSUMES**

- **To match the bare sovereign: +4.34% a year, in perpetuity** (3.99% at the 3-year window;
  4.57% at the 13-year; 3.83% granting the best year Lam has ever filed).
- **To clear the [E4-28] 10% floor: +9.10% a year, IN PERPETUITY** — band **8.59%** (best
  year ever) to **9.33%** (13-year window). *The screen row's 8.96% sits inside that band and
  reproduces the arithmetic; its input, not its method, is what this run rebuilt.*
- *Engine only, casting no vote [E3-34]:* `tools/run.py`'s staged DCF returns a **year-1
  growth of 21.5%** at a 5.24% discount rate with a 2.5% terminal rate. Recorded because the
  template asks for it; **it is an engine output and it is not the reported artifact.**
- **What the business has actually done, every window published [E4-38]:** owner earnings
  (capex end) CAGR **+7.67% over 7 years (FY2019→26)** · **+11.28% over 9 years (FY2017→26)**
  · **+20.77% over 12 years (FY2014→26, from a trough)**. Revenue CAGR **+14.72% over 10
  years.**

**THE LOUDEST FACT AGAINST THE CONCLUSION, STATED FIRST [E4-51]: Lam's own filed
owner-earnings growth over nine and twelve years EXCEEDS the 9.10% the floor requires.** It
is the third name in this queue with that shape (CTAS, KLAC, and now Lam). **It fails
anyway, on four independent bounds:**

1. **[E4-38] — terminal-date selection.** *"growth-rate presentations can be significantly
   distorted by a calculated selection of either initial or terminal dates."* **Every one of
   those windows ends at the top of the largest capital-spending wave the industry has ever
   had, and the FY2014 start is a cyclical trough.** The 2.50x step measured at Q4 is the
   size of the terminal-date effect. The seven-year figure — **+7.67%** — is the one that
   starts *after* the FY2019 downturn and it is already **below** the 9.10% required.
2. **[E4-44]/[E2-63] — the lever is nearly spent, and the ceiling can be named.** *"the value
   of an asset … cannot over the long term grow faster than its earnings do."* Lam's
   operating margin is **35.3%**, second in the eight-company row; gross margin **50.5%**, an
   all-time high; SG&A already the lowest in the equipment set at **4.9%**; R&D already the
   lowest at **10.2%**. **Even reaching a 45% operating margin adds about 27% in total and
   then contributes zero, forever.** After that the growth must be all volume.
3. **The scale bound, computed from filings only.** **9.10% in perpetuity doubles the
   business every 7.95 years: $23.2bn of revenue today → ~$46bn by 2034 → ~$93bn by 2042 →
   ~$186bn by 2050.** For scale from filed figures alone, the four largest equipment makers'
   latest-year revenues — AMAT $28.4bn, LRCX $23.2bn, ASML €32.7bn, KLA $13.6bn — total
   roughly **$100bn**. **The price requires Lam alone, forever, to reach almost twice what
   the four of them together sell today.**
4. **[E4-35] — the base rate.** *"fewer than 10 of the 200 most profitable companies in 2000
   will attain 15% annual growth in earnings-per-share over the next 20 years."* The floor
   here needs 9.10% **with no end date**, from a company whose product is bought in violent
   cycles by twenty customers.

**Plus [E4-55]: with no unit series and no price series filed, none of the historical growth
can be decomposed into price and volume from the primary source.** The single most important
input to a growth judgment is unavailable, and that is a fact about the filing, not about
the analyst.

**3. WHAT YOU ARE PAID**

- **−4.34 points over the sovereign** at the judged level; **−4.57 to −3.83 across the whole
  band.** **There is no construction in this file — no window, neither (c) end, not the best
  year Lam has ever filed — in which Lam pays as much as a 30-year Treasury.**
- *Cohort: KLA pays −4.17, AMAT −3.99, Lam **−4.34**. **Lam is the dearest of the three.***

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].**
- **Sovereign used: 5.24% — the bare rate, no per-name premium added.** *"It may look
  mathematical. But it's mathematical gibberish in my view."*
- Certainty is handled **twice, and neither place is the rate**: at the understanding gate
  (Q1, which Lam passes) and in the discount to value demanded at the end. It is priced
  **once** and may not be stacked **[E4-11, E4-48]**.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — zero growth, at the sovereign, net cash
credited, on 1,251,321,000 shares:

| | zero growth at 5.24% | at the **[E4-28] 10% floor** |
|---|---|---|
| **conservative** (13-yr window, capex end) | **~$43/share** | **~$23/share** |
| **judged** (8-yr window, capex end) | **~$54/share** | **~$29/share** |
| **optimistic** (3-yr window, D&A end) | **~$75/share** | **~$40/share** |
| *most generous construction available (best year ever filed)* | *~$84/share* | *~$45/share* |
| **CURRENT PRICE** | **$307.65** | **$307.65** |

- **The price is 4.1x the TOP of the entire zero-growth band and 7.1x its bottom; 7.7x the
  top of the floor band and 13.4x its bottom; and 3.7x the single most generous construction
  this file can build.**

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].** Honest pre-tax expectancy = yield +
sustainable growth. **A generous 6.5% perpetual-equivalent growth judgment is used** — above
the seven-year realised rate of 7.67% only in the sense that 7.67% is itself a wave-top
figure, and well above the ~3% long-run rate an industry can sustain against nominal GDP:

| construction | yield | + growth | **honest expectancy** |
|---|---|---|---|
| 13-yr window | 0.670% | 6.5% | **7.17%** |
| **judged 8-yr window** | **0.898%** | **6.5%** | **7.40%** |
| 3-yr window, D&A end | 1.253% | 6.5% | **7.75%** |
| best year ever filed, most generous construction | 1.414% | 6.5% | **7.91%** |
| *best year ever + a generous 8.0% growth* | *1.414%* | *8.0%* | ***9.41%*** |

> **Every construction, including two built to flatter, sits BELOW the ~10% floor. Even
> granting the best single year Lam has ever filed AND 8% perpetual growth, the expectancy
> does not reach it.**
> **→ THE NAME IS NOT RANKED. IT IS QUIT ON [E4-28].**

- **floor verdict: honest pre-tax expectancy 7.40% (band 7.17%–7.91%) against ~10% — BELOW,
  so the ranking lines below are recorded for the register only and carry no entry language.**
- points over sovereign, this name: **−4.34** (band −4.57 to −3.83)
- against the rest of the opportunity set: **it does not enter it.** *Take the best available,
  or nothing* — and **[E2-74]**'s parking place is where the money stays.

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [ ] Normal method [E4-11]
- [x] **SCREAMER TEST [E4-01, E4-25] (Bar 2).** Take the conservative end of the range and
  ask whether the price already clears it. **No margin is added on top — "startlingly low" is
  what you observe, not what you subtract.** Conservative case **~$43/share**; price
  **$307.65**. **OUTCOME THREE: the price is above the whole range. NO.**
  *Bar 1 is not used and no end margin is applied; using both on the same number is
  forbidden.*
- **WINDAGE COUNT: ONE.** Conservatism is spent once, at the **[E4-41] normalization** of the
  level from the five-year default window to the eight-year window. Realistic inputs
  everywhere else; **no risk premium in the rate [E3-42]; no end margin [E4-48].** *And the
  windage does no work: the verdict is identical at every point in an 87%-wide band,
  including at the most generous construction available.*

- **VERDICT: [ ] IN  [ ] UNRESEARCHED  [ ] UNKNOWABLE — the name FAILS at Q5, ON PRICE, at
  the [E4-28] floor. Ranking position: NONE — quit on, not ranked.**

*Not UNRESEARCHED: no named document would change it. Not UNKNOWABLE: the evidence is in and
the answer is determinate. **This is a finding about the price, not about the business.***

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Q6 IS NOT OPENED.** Q5 failed, no position exists, and **[E1-02]** requires yardsticks to
be established *prior to the act* — there is no act. **Position size: ZERO.** No alert band
is armed and no `PORTFOLIO.md` row is added, per the QLYS ruling of 2026-09-07: a name that
fails on price is not a business failure, but neither is it a holding.

**What is recorded instead, so a future re-look does not start from nothing:**

**The price at which the file re-opens.** The [E4-28] floor clears near **~$29/share** on the
judged construction, **~$40** on the most generous — **a 87–91% decline from $307.65.**
**The file is far likelier to re-open on earnings than on price:** at $307.65 the floor
requires **$38.5bn of owner earnings** against $3.46bn judged, an **11.1x** gap.

**The observation that would most change this file** — the thesis-confirming metric Q2 could
not run: **a filed instrument that decomposes Lam's revenue into price and volume, or a
segment cost-of-goods-sold split by product line.** Either would make the [E2-44](1) test
runnable for the first time in eighteen years. Neither exists today; both are within the
registrant's power to publish.

**Bull-breakers, pre-registered:**
- **gross margin falling in a year in which revenue falls** — i.e. the FY2019 result
  repeating rather than the FY2024 one
- **China revenue in dollars falling while ex-China fails to grow faster** — the exposure
  crystallising rather than diluting
- **any drawing on the $2.00bn commercial paper programme to fund repurchases.** The capacity
  was enlarged by a third in March 2026 at the top of the price record; **using it would
  convert Lam's forward-running buyback into KLA's reverse-running one in a single quarter**
- **R&D below 10.0% of revenue** — the under-investment reading of the falling intensity
- **an acquisition above ~$1bn**, which would break the cleanest [E2-30](2)/[E3-40] record in
  this cohort ($120M in eight years)
- **the CSBG caption falling in share while gross margin also falls** — which would say the
  annuity is not the counter-cyclical asset the revenue series suggests

**Bear-breakers, pre-registered:**
- **gross margin held or raised in a year of falling revenue with China's share NOT rising**
  — the [E2-44](1) test passed clean, which has never happened in the filed record
- **a filed unit or installed-base series**, which would let [E4-55] be run at all
- **China's share of revenue falling below 25% with China dollars falling** and ex-China
  growing — AMAT's de-risking pattern arriving at Lam

- **VERDICT: [ ] IN [ ] OUT [ ] UNRESEARCHED [ ] UNKNOWABLE — NOT OPENED. Q5 closed the
  file.**

---
## SELF-AUDIT

- [x] Questions answered in order; no verdict skipped; Q5 opened only after Q1–Q4 each
      returned IN
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q2's NARROW
      rests on filed facts; its five named absences are recorded as absences, not as
      provisional evidence, and each was established by a **recorded sweep** naming the
      vintages searched
- [x] No UNRESEARCHED verdict was returned, so no work order is owed
- [x] No UNKNOWABLE verdict was returned
- [x] Step 0: the filing was read (MD&A, cash-flow statement including its detail lines,
      footnotes), accession `0000707549-26-000037`, and **four** figures were cross-checked
      against the filed statement
- [x] Owner earnings on a multi-year mean; **thirteen** windows stated; the capex band
      disclosed as a judgment with the filing quoted on both sides of it
- [x] Competitor row filled — 8 SEC registrants; five of Lam's seven named competitors are
      non-registrants, which **caps the class at NARROW** under the ACLS rule and becomes a
      Q6 work order rather than a PROVISIONAL suspension
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury),
      dated 2026-09-04
- [x] Value stated as a round-number range, not a point estimate
- [x] One bar chosen (Bar 2, the screamer test); **windage count: ONE**
- [x] Prices dated; the aggregator used for the live quote only and flagged; the share count
      hand-read off the cover and cross-checked against the balance sheet; the 10-for-1 split
      of 2024-10-02 guarded and every per-share figure stated post-split
- [x] **Absence-claim rule observed:** every "no instance found" names the vintages swept —
      ASP/price series, unit and installed-base series, market-share figure, segment cost
      split, product-line margin, geographic margin (**FY2026, FY2025, FY2024, FY2023,
      FY2020, FY2019 and FY2016 10-Ks**); who-names-Lam (**eight peer registrants' latest
      annual filings**); enforcement matters (**FY2026 10-K**); restatements (**nine
      vintages**)
- [x] Run committed to git after each gate closed, by file name

## REGISTER

- **Verdict: [x] OUT ON PRICE at Q5** — about the price, not the business. Not UNRESEARCHED
  (no named document would change it) and not UNKNOWABLE (the evidence is in).
- **One line:** *The best economics in the equipment cohort — 81% on operating capital, first
  of the three — with the weakest filed pricing evidence in it, at a price that pays a sixth
  of what a Treasury bond pays.*
- **PASS/FAIL, plainly: FAIL. Q5 closed the file, on price.** Q1, Q2, Q3 and Q4 each returned
  IN. Q6 was not opened.

---
## DEFECTS FOUND — IN THE TOOLING, IN THE BRIEF, AND IN THE PRECEDENT

*Recorded per operator rule 6: violations and errors are corrected in an addendum, never by
editing history.*

### TOOLING

**1. THE `level_shift` DEFECT — NEW, AND IT IS THE MOST INTERESTING ONE IN THIS FILE.**
The brief's row read `level_shift 1.68 STEP UP [E4-41] · level_shift_oe 1.64 STEP UP
<-- the two AGREE here`. **Both reproduce exactly**: `Screens/floor_screen.py:level_shift`
on a **nine-year** series returns **1.683** on operating cash flow and **1.658** on owner
earnings. **A nine-year series makes the "earlier" half FY2018–FY2023, which already
contains three years of the wave being measured.** The two measures agree because they are
computed on the same contaminated base; **agreement between two contaminated measures is not
corroboration**, and the brief read it as reassurance.
**And the same function, given the FULL eighteen-year filed series, REFUSES the ratio:**
*"EARLY HALF STRADDLES ZERO … a ratio against it is undefined in substance even where it
computes (**it gives 3.08x**). **The level HAS changed and the multi-year mean is averaging
TWO DIFFERENT BUSINESSES. READ THE FILING [E4-25].**"*
**The refusal branch is right, it is more informative than the number, and a reader of the
row never sees it** — the defect class the queue's FOLD note names as *"a diagnostic that
exists but never reaches the reader."* Hand-computed step on owner earnings: **2.50x**
(3.44x on the alternative pre-wave base). **Cohort tally, all in the same direction: KLAC
1.73 reported vs 3.86; AMAT 2.0 vs 2.74; LRCX 1.68 vs 2.50. Third consecutive firing.**

**2. THE SPREAD DEFECT — ELEVENTH CONSECUTIVE RUN, AND THIS TIME THE BOTTOM END COULD NOT BE
REPRODUCED AT ALL.** The row read `oe_bottom_m 3991 | oe_top_m 4824 | spread 0.209`.
- **`oe_top` 4,824 reproduces to the dollar** as the **3-year FY2024–26 mean at the D&A end**
  ($4,824.3M).
- **`oe_bottom` 3,991 reproduces on NO window at either capex end.** The thirteen windows
  rebuilt in Q4 run 2,580.5 → 4,512.7 at the capex end and 2,636.8 → 4,824.3 at the D&A end;
  the nearest constructions are the **5-year FY2021–25 mean at the D&A end ($3,912.1M, 2.0%
  away)** and **FY2024 as a single year at the D&A end ($3,999.5M, 0.2% away)** — *neither of
  which is a bottom end and one of which is not a mean at all.*
- `tools/screen.py` run live on 2026-09-07 returns **1.16..1.24%**, i.e. the 3-year window at
  both ends, which is a third construction again and does not match the row's 1.04% either.
- **Previous runs found "two different windows, two different capex ends, one number called a
  spread." This run finds worse: one end identified, one end unidentifiable, and a live tool
  that agrees with neither.** True width **87.0%** against the row's 20.9%.

**3. `run.py`'s D&A end and the finished-goods transfer.** Neither `run.py` nor `screen.py`
sees the **$125,691 thousand of finished-goods inventory transferred to property and
equipment** disclosed as a non-cash item in Lam's FY2026 cash-flow statement (also $90,873
FY2025, $71,267 FY2024). **It is real capital spending that never crosses the investing
line**, and it makes the filed capex figure 13.0% too low as a measure of capital additions.
The same shape as UAL's operating-lease leak. Immaterial to the verdict here; it would not be
immaterial on a thinner name.

**4. The four flags the brief said were quiet were quiet, and that was correct.** The D&A
series is clean (no discontinuity); `acq_note` is right — **$120.0M of acquisitions in eight
years**; and the two flags computed on owner earnings do agree with the OCF versions. **The
agreement is real. What it is evidence of is narrower than it looks:** both owner-earnings
flags are computed from the same OCF series with the same nine-year window, so they can only
disagree where the (c) subtraction changes the shape, not the level. **Mildly reassuring
about the data, and — as the brief said — silent about the business.**

### THE BRIEF

- **The screen cap `383129` implies a $306.18 price**; the 2026-09-04 close is **$307.65**.
  Immaterial (0.48%), recorded rather than absorbed.
- **The brief's framing of the Q2 question was refuted, not merely answered.** It asked
  *"whether Lam can show pricing power the way KLA did."* **The question cannot be asked:**
  Lam files one reportable segment, no ASP, no units, no market share and no product-line
  margin, so the instrument that decided KLA's Q2 does not exist. That is a difference in
  kind from AMAT's position (three segments, three years of segment gross margin), not a
  difference in degree.
- **The brief's prior on China was right and understated it.** *"Lam's China share has run
  higher than either."* It is higher **now** (33.8% against AMAT's 30.1% and KLA's 29.8%), it
  **peaked** higher (42.2% in FY2024), it is the **largest in dollars relative to company
  size**, and it is **the only one of the three still growing** (+26.7%).
- **The brief's prior on the buyback was REFUTED.** See below.

### THE PRECEDENT — TWO DEFECTS IN THE KLAC RUN'S RESEARCH FILE

*Both in `Test Runs/_research 2026-09-07 KLAC/competitor-row.md`. Neither affects that run's
verdict; both would mislead a future reader, and per operator rule 6 they are recorded here
rather than edited there.*

1. **§4.5 and §4.6 say of Lam's Item 1 "Competition": *"Likewise generic"* and *"Applied and
   Lam name nobody at all, which is uninformative in either direction."* **That is false.**
   Lam's Competition section names **seven companies** — Applied Materials (twice), ASM
   International, Wonik IPS, Hitachi, Tokyo Electron (twice), Screen Holdings and Semes —
   in the sentences immediately adjacent to the passage that file quotes. The **true** narrow
   claim, which that file also makes and which is correct, is that *"the string 'KLA' does
   not appear anywhere in the filing"* — a different statement. **The AMAT run got this right
   and quoted the naming passage in full; the KLAC research file did not.**
2. **§5 records LRCX's China revenue as *"not stated in $"*.** **Lam states it in thousands
   in Note 19 of every vintage back to FY2014** ($7,859,811 in FY2026). Only the MD&A summary
   table is in percentages. The full dollar series is reproduced in this file's Q2.

---
## THE HEADLINE, FILLED IN

```
Q1 IN · Q2 IN (NARROW) · Q3 IN (overlay) · Q4 IN (GREAT) · Q5 FAIL ON PRICE · Q6 not opened.

PASS/FAIL:  FAIL.  Q5 closed the file, on price, at the [E4-28] floor.

PRICE     $307.65   close of 2026-09-04, aggregator, flagged, four prior closes recorded
SHARES    1,251,321,000   FY2026 10-K cover, as of 2026-08-04, acc 0000707549-26-000037,
                          cross-checked against the balance sheet count 1,251,278,000
MARKET CAP  $384,969M     SOVEREIGN 5.24% USD, US Treasury 30-yr, 2026-09-04

OWNER EARNINGS, 13 windows x both (c) ends:  $2,580.5M .. $4,824.3M  (87.0% wide, not 20.9%)
JUDGED   $3,457.7M   8-yr FY2019-26 at total capex   YIELD 0.898%   -4.34 pts vs the bond
VALUE, zero growth at the sovereign:  ~$43 / ~$54 / ~$75 per share
VALUE, at the [E4-28] 10% floor:       ~$23 / ~$29 / ~$40 per share
PRICE IS 4.1x THE TOP OF THE ZERO-GROWTH BAND and 3.7x the most generous construction here.
TO CLEAR THE FLOOR THE PRICE NEEDS 9.10% PERPETUAL GROWTH.
HONEST PRE-TAX EXPECTANCY 7.40% (band 7.17-7.91%) vs ~10%.  QUIT ON, NOT RANKED.
```

## WHERE LAM LANDS IN THE COHORT — THE THREE-NAME SUMMARY

| | **KLAC** | **LRCX** | **AMAT** |
|---|---|---|---|
| verdict | FAIL at Q5 on price | **FAIL at Q5 on price** | FAIL at Q5 on price |
| Q2 class | IN NARROW — *the strongest narrow this queue has recorded* | **IN NARROW — between the two, and closer to AMAT** | IN NARROW — *narrower than KLAC's* |
| [E2-44](1) pricing test | **PASSED mix-free at segment level** | **INCONCLUSIVE — 3 of 4 downturns fail; the one pass is filer-attributed to mix** | **FAILED** 3 of 4 |
| the instrument | exists | **does not exist — one reportable segment** | exists but unusable (3 rising years) |
| service profit-mix test | not runnable | **not runnable — no CSBG margin filed** | **runnable, and it killed the claim** |
| ex-cash return on operating capital | 56.9% | **81.1% — 1st** | 73.9% |
| incremental return FY2022→ | 37.7% | **107.5% — 1st** | 95.3% |
| gross margin (the pricing measure) | **61.3% — 1st** | 50.5% | 48.7% |
| service/support % of revenue | 23.0% | **35.9% — 1st** | 22.5% |
| China, in dollars | flat ~$4.05bn — **not** de-risking | **all-time high $7.86bn, +26.7% — neither pattern** | **falling −$1,588M — real de-risking** |
| enforcement action | 2006 backdating, all actors gone | **none** | **$253M BIS + suspended denial order** |
| [E5-08] condition (2) | **fails hard** — smallest buyback at the lowest price, largest at the top on fresh debt | **fails on the LEVEL, PASSES on the DIRECTION** — 95% cut in quarterly buying as the price rose 4.3x | fails, *"by a fifth"* |
| guidance record [E3-48] | 16 of 16 above the midpoint | **9 of 9**, +2.33% rev / **+7.79% EPS (largest of the three)** | 7 of 7 |
| [E4-41] step, reported vs hand-built | 1.73 → **3.86x** | 1.68 → **2.50x** | 2.0 → **2.74x** |
| judged yield | 1.07% | **0.898%** | 1.254% |
| **points over the sovereign** | −4.17 | **−4.34 (the dearest)** | −3.99 |
| growth needed for the floor | 8.93% | **9.10%** | 8.75% |

**The cohort's one shared finding, and it is worth more than any of the individual verdicts:**
**all three names cleared all four business gates and all three failed on price, by between
3.99 and 4.34 points, at the top of the same wave.** The three files disagree about almost
everything else — which has the best economics (Lam), which has the best evidence (KLA),
which has genuinely de-risked China (AMAT) — and **on price they are the same file three
times.**

## PRIORS — WHICH WERE CONFIRMED AND WHICH WERE REFUTED

| the brief's prior | outcome |
|---|---|
| *"Lam lands between them — better economics than AMAT, weaker evidence than KLA"* | **CONFIRMED, and both halves by wider margins than expected.** Lam is FIRST in the cohort on both capital measures, not merely ahead of AMAT; and its pricing evidence is not weaker than KLA's, it is **absent**. |
| *"the deciding question is whether Lam can show pricing power the way KLA did"* | **REFUTED IN ITS FRAMING.** The question cannot be asked from Lam's filings. One reportable segment, no ASP, no units, no market share, no product-line margin. |
| *"does Lam file segment gross profit at all?"* | **YES — and it is useless.** One reportable segment, three years, all with rising revenue. Both structural defects that made the test unrunnable on AMAT, at once. |
| *"Lam's Customer Support Business Group is the same claim [as AGS]"* | **CONFIRMED AND WORSE.** No margin filed at all, and the caption **mixes the annuity with new Reliant equipment sales** without sizing the split. The AMAT finding (33.4% vs 54.2%) is the best available evidence and is applied by analogy, labelled. |
| *"Lam's China share has run higher than either"* | **CONFIRMED AND UNDERSTATED.** Higher now (33.8%), higher at peak (42.2%), largest in dollars relative to size, and the only one still growing. **Matches neither cohort pattern.** |
| *"[E4-41] is live and the row says so twice … both series read STEP UP"* | **CONFIRMED ON SUBSTANCE, REFUTED ON MAGNITUDE.** The step is 2.50x, not 1.68x, and the two series "agree" only because they share a contaminated nine-year base. |
| *"Lam buys back aggressively. Run the same test and compare directly to KLA's record."* | **REFUTED — the sharpest refutation in this file.** On the **quarterly** series Lam filed, the price rose from **$76.18 to $325.14 (4.3x)** across eight quarters while the quarterly repurchase fell from **15,763k shares to 811k (−95%)** and the dollars from $1,306.8M to $245.9M. **[E5-24]'s first law run FORWARD — the first time in this queue.** Condition (2) still fails, but on the **level** (every quarter was above the top of the value band), not on the **direction**. |
| *"Q5 will fail on price — 8.96% perpetual growth against [E4-35]'s base rate"* | **CONFIRMED, and by more than the row said.** The judged construction needs **9.10%**, and Lam is the **dearest of the three** at −4.34 points. |

## THE STRONGEST SINGLE FACT AGAINST THIS RUN'S CONCLUSION

**Lam's own filed owner-earnings CAGR over nine years is 11.28% and over twelve is 20.77% —
both above the 9.10% perpetual growth the [E4-28] floor requires at this price.** A reader
who believes those windows are representative should conclude that the price clears the
floor, and this run says it does not. **The four reasons are stated at Q5 and the honest
weight of them is this:** the seven-year figure that begins *after* the last downturn is
**7.67%**, already below the requirement; every window that beats the requirement ends at the
top of a wave the registrant's own risk factors say can end three separate ways; and **with
no unit or price series filed [E4-55], nobody — including management — can decompose that
growth into volume and price from the primary source.** *A conclusion that required fighting
for it is worth less, not more* **[E4-18]** — and that cuts against the growth case here, not
against the refusal.
