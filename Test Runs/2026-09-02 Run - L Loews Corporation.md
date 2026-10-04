# Company Run — LOEWS CORPORATION (L) — 2026-09-02
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.
**Sector method applies:** `Framework/SECTOR METHOD - owner earnings for insurers and
float-bearing holding companies.md` (written 2026-09-02). Loews is the third name in the
MINI BERK read order (WTM → MKL → **L** → BRK-B) and was chosen because it exercises
**[E5-47]** — earnings from sources other than investments and insurance underwriting —
more directly than any other name in that queue.

Fill top to bottom. **Stop at the first verdict that is not IN.**

**STATUS: IN PROGRESS — written question by question under the WRITE-EARLY PROTOCOL.**

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
- rate **5.27%** · date **2026-09-01** · source **US Treasury daily par yield curve, 30-year
  (issuing authority; `python tools/sources.py`)**. FRED DGS30 is the labelled fallback and
  was not used.
- FX: none. Loews reports in USD and earns in USD (a small International insurance book and
  a UK/Luxembourg/Lloyd's presence are the only non-USD exposure; the 10-K reports the
  effect of FX on International net written premiums as **$9M on $85M of growth**).

**STAGE 0 — SHARE COUNT BY HAND OFF THE COVER** *(the test that has caught four names)*
> "As of July 31, 2026, there were **204,427,720** shares of the registrant's common stock
> outstanding." — L 10-Q, Q2 2026, cover page, verbatim

- **Single class.** "Common stock, par value $0.01 per share | L | New York Stock Exchange"
  is the only line in the Section 12(b) table. There is no A/B structure, no tracking stock
  today. *(There WAS one — the Carolina Group tracking stock, separated in the 2008 Lorillard
  split-off — and it is dealt with in the buyback record at Q3, because a split-off is not a
  repurchase.)*
- Cross-check against the 10-K: **206,003,999 issued, 0 in treasury** at 2025-12-31;
  **206,052,874 outstanding** at 2026-02-06 (MD&A). The count has fallen 1,625,154 in the
  five months to 2026-07-31 — repurchases are ongoing.
- **Price $109.475**, 2026-09-02, **aggregator quote — flagged** (operator rule 5: aggregators
  for live quotes only).
- **Market capitalisation = 204,427,720 × $109.475 = $22,380M.**

**STAGE 0(b) — INSURER, FLOAT-BEARING HOLDING COMPANY, OR NEITHER?**
*(the sector method's own second gate)*
**Loews is a float-bearing holding company, and it is the mixed case the method was written
for.** CNA is **81.2%** of consolidated 2025 revenue (81.5% in 2024, 83.6% in 2023);
Boardwalk **12.6%**; Loews Hotels **5.1%**. The insurer is consolidated at 100% and
**approximately 8% of it belongs to somebody else**. The sector method applies, and
**[E5-46]**'s "net of minority interests" is load-bearing here, not a throwaway clause.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Four primary documents, all read, all FY2025 or later:**

| document | filed | period | accession | primary doc |
|---|---|---|---|---|
| **Loews Corporation 10-K** | 2026-02-10 | 2025-12-31 | 0000060086-26-000008 | l-20251231.htm |
| **Loews Corporation 10-Q** | 2026-08-03 | 2026-06-30 | 0000060086-26-000047 | l-20260630.htm |
| **CNA Financial 10-K** | 2026-02-10 | 2025-12-31 | 0000021175-26-000011 | cna-20251231.htm |
| **Boardwalk Pipeline Partners, LP 10-K** | 2026-02-10 | 2025-12-31 | 0001336047-26-000004 | bwp-20251231.htm |

- **THE STRUCTURAL FIND OF THE RUN, and it was not in the brief.** The brief said Boardwalk
  is wholly owned, which it is — and inferred from that that no standalone statements exist.
  **They do.** *Boardwalk Pipeline Partners, LP* has continued to file its own 10-K and 10-Q
  with the SEC after Loews bought in the public units in 2018, because its senior notes are
  registered. **So BOTH non-Corporate operating columns of Loews have audited standalone
  statements available as primary documents** — CNA because it is 92%-owned and listed,
  Boardwalk because it has public debt. That makes the per-business (c) build required by
  **[E5-20]** a matter of reading, not of estimating. It is the HOG/HDFS and DKS/Foot Locker
  move, available twice over.
- **figure cross-checked against the filed statement:** *Total investments* **$55,376M** at
  2025-12-31, read off the face of the Consolidated Balance Sheet (10-K p. 86), against
  fixed maturities $43,984 + equity securities $1,292 + limited partnerships $2,861 + other
  invested assets $1,195 + short-term investments $6,044 = **$55,376M**. Ties.
- Second cross-check, because the sector method turns on it: **Noncontrolling interests
  $955M** on the balance sheet, and **Amounts attributable to noncontrolling interests
  $(105)M** on the income statement, against CNA's own 10-K.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Loews is a family-controlled
holding company that owns three cash-producing businesses outright or nearly so, holds the
proceeds at the parent, and buys back its own stock with them. It is four different
businesses stapled together, and the only honest way to write the unit economics is one line
each:

1. **CNA (≈92% owned, listed, files its own 10-K) — 81.2% of revenue.** A commercial P&C
   insurer. It takes premiums today, invests them, and pays claims over the following one to
   twenty years. It earns money two ways that must never be added twice: an **underwriting
   margin** (2025 combined ratio **94.7%** on $10,478M of net earned premiums → a **$551M**
   pre-tax underwriting gain) and the **investment return on the money it holds in the
   meantime** ($2,557M of net investment income in 2025). Attached to it is a **runoff
   long-term-care block** which is not an insurer at all any more — it is a closed portfolio
   of promises made in the 1990s and 2000s, with **$13,448M of future policy benefit reserves**
   on the balance sheet and **$26,880M undiscounted** in the contractual-obligations table,
   carried against an investment portfolio. That block lost **$322M of core income in 2025**.
2. **Boardwalk Pipelines (wholly owned, files its own 10-K) — 12.6% of revenue.** 14,275 miles
   of natural-gas and NGL pipe and 199.5 Bcf of working gas storage. It sells **capacity, not
   gas**: 2025 revenue $2,310M, of which the filer states *"approximately 87% of Boardwalk
   Pipelines' revenues were derived from capacity reservation fees under firm contracts or
   from contracts with minimum volume commitments."* It has almost no commodity exposure and
   almost no volume exposure — you pay for the reservation whether you flow gas or not. Its
   rates on the FERC-regulated systems are **cost-of-service capped**.
3. **Loews Hotels (wholly owned) — 5.1% of revenue.** 27 hotels; **11 owned, 15 in joint
   ventures where Loews holds a noncontrolling interest, 1 managed**. In 2025 the JV equity
   income (**$102M**) was *twice* the segment's pre-tax income (**$52M**). Eleven of the
   fifteen JV hotels are at Universal Orlando. This is materially a bet on one theme-park
   operator's attendance.
4. **Corporate — the parent.** $3.9bn of cash and investments net of receivables and payables
   at 2025-12-31, a trading portfolio, $72M of interest expense, and a ~53% **equity-method
   (NOT consolidated)** stake in Altium Packaging that produced a **$28M loss** in each of
   2025 and 2024.

**The scarce input this business controls.** Per business, because there is no single one:
- **Boardwalk: right-of-way and FERC certificates.** 14,275 miles of pipe across thirteen
  states, built on easements, with certificates of public convenience and necessity. This is
  the only genuinely scarce, genuinely non-replicable asset in the group. You cannot buy a
  second Texas Gas.
- **CNA: none that is scarce.** Its inputs are underwriting judgment, capital, and licences.
  The corpus says so directly at **[E2-70]** and Q2 tests it there.
- **Hotels: land at Universal Orlando** — scarce, but it is *Comcast's* scarcity, and Loews
  holds noncontrolling JV interests in it.
- **Parent: permanent capital and family control.** Real, and it is what lets the buyback run
  for twenty years without interruption.

**Will the fundamentals look broadly the same in ten years?** Yes for the pipe (contracts run
to 2030+, and the projected-firm-revenue backlog is **$19,556M** against $2.3bn of annual
revenue). Yes for commercial P&C in the sense that the industry will exist and CNA will still
be a mid-sized writer of it. **The one place where "broadly the same" is genuinely open is
the long-term-care runoff**, and that is not a Q1 objection — it is a Q4 staying-power
question and an **[E2-67]** candor question, taken up there.

**Is this "relatively simple and stable in character" [E3-31]?** It is four businesses and a
consolidation artifact, and I had to read four separate 10-Ks to see it. But the businesses
individually are each simple, the filer segments them cleanly in Note 19, and — decisively —
**two of the three operating subsidiaries publish their own audited statements**, so the
perimeter problem that blocked BAM and BN does not arise. **[E4-46]** is satisfied: this took
reading, not months of study, and no fetch is outstanding.

**VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**Where the money actually is** — the weighting that governs everything below. Net income
attributable to Loews Corporation, FY2025 (10-K MD&A, Consolidated Financial Results):

| segment | net income to Loews | share |
|---|---|---|
| **CNA Financial** | **$1,173M** | **70.4%** |
| **Boardwalk Pipelines** | **$444M** | **26.6%** |
| Loews Hotels & Co | $31M | 1.9% |
| Corporate | $19M | 1.1% |
| **total** | **$1,667M** | |

**A moat claim for Loews must be passed where the earnings are. 70% of them are in a
commercial P&C insurer.**

### [E3-03], the three criteria, applied per business

| | needed or desired | **no close substitute** | not price-regulated |
|---|---|---|---|
| **CNA (70% of earnings)** | yes — insurance is compulsory in most of its lines | **NO** | partly — rates filed and reviewed |
| **Boardwalk (27%)** | yes — the gas has to get to the LNG terminal | **yes** — you cannot build a second Texas Gas | **NO** |
| Loews Hotels (2%) | yes | no | yes |

**Both of the businesses that matter fail a criterion, and they fail different ones.**

**CNA fails criterion 2, and the corpus states the reason in the sector's own terms
[E2-70]:** *"Insurance companies offer standardized policies which can be copied by anyone.
**Their only products are promises.** It is not difficult to be licensed, and rates are an
open book. There are no important advantages from trademarks, patents, location, corporate
longevity, raw material sources, etc."* CNA's own 10-K says the same thing about itself:
*"The property and casualty insurance industry is highly competitive, both as it relates to
rate and service. CNA competes with a large number of stock and mutual insurance companies,
as well as other entities, for both distributors and customers."*

**Boardwalk fails criterion 3, on the filer's own words:** *"The maximum applicable rates
that Boardwalk Pipelines' FERC-regulated subsidiaries may charge for all aspects of the
natural gas transportation services they provide, are established through the FERC's
cost-based rate-making process."* This is the [E2-59] case exactly: administered pricing
**floors** a capital-intensive transport business and **caps** it, but *"the moat belongs to
the regime"*. Regulation caps a franchise ([E3-03] criterion 3) and floors a commodity
business; **neither creates the class.**

### THE COMPETITOR ROW — required [E3-28]. Row 1: CNA vs four P&C peers

**Combined ratio, FY2021–FY2025, every figure from the company's own 10-K.** Full working,
definitions, and per-cell provenance: `_research 2026-09-02 L/competitor_row_CNA.md`.

| Combined ratio (%) | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean | Δ 2021→2025 |
|---|---|---|---|---|---|---|---|
| **CNA** (P&C Ops, computed) | **96.2** | **93.2** | **93.5** | **94.9** | **94.7** | **94.5** | **−1.5** |
| AIG (General Insurance) | 95.8 | 91.9 | 90.6 | 91.8 | 90.1 | 92.0 | −5.7 |
| HIG (BI+PI, computed) | 94.6 | 92.4 | 93.3 | 91.9 | 89.1 | 92.3 | −5.5 |
| TRV (consolidated) | 94.5 | 95.6 | 97.0 | 92.5 | 89.9 | 93.9 | −4.6 |
| WRB (consolidated) | 89.6 | 89.3 | 89.7 | 90.3 | 90.7 | 89.9 | +1.1 |
| **CNA rank (1 = best)** | **5/5** | **4/5** | **4/5** | **5/5** | **5/5** | **5/5** | |

- Peers named: **4 of the 4 the brief specified**; the US commercial P&C industry has more
  than eight scale writers, and four is the row taken. TRV, WRB and AIG read **directly** off
  their own MD&A tables with the 2023 overlap agreeing exactly across two filings each.
  **CNA and HIG do not publish a single consolidated P&C combined ratio** and were computed
  as the earned-premium-weighted average of their disclosed segments; the CNA computation was
  cross-checked a second way as `100 − (P&C underwriting gain ÷ P&C net earned premiums)` and
  the two methods agree to within **0.05 points in every one of the five years**.
- **The row is not merely bad; it is bad and getting worse.** CNA was 0.4 points behind AIG
  in 2021 and is **4.6 points behind in 2025**. Every peer but WRB took 4.6–5.7 points out of
  its combined ratio across the window; CNA took out 1.5, all of it in the single 2021→2022
  step, and has since given 1.5 back.
- **And the comparison flatters CNA.** The CNA figure is Property & Casualty Operations only.
  It **excludes** Life & Group (the long-term-care runoff), and Corporate & Other (A&EP, the
  legacy excess workers' compensation portfolio, legacy mass tort). The entity being ranked
  fifth is **the good half of CNA**.

**The same row on return on equity, which is worse.** *(AIG is excluded from the ranking
sentence because Corebridge consolidation and deconsolidation drive its 2021, 2022 and 2024 —
it is not a like-for-like comparator, and the run says so rather than using it.)*

> **Against the four genuinely comparable P&C writers, CNA is LAST on ROE in every single
> year of the window.** FY2025: **CNA 11.5%** vs HIG 22.0%, TRV 20.7%, WRB 19.7%. The gap to
> the best comparable peer widened from **6.4 points to 10.5 points**.

**And it is losing on price *and* volume.** Net-premium CAGR across the window: **CNA 7.8%**,
against WRB 9.4%, HIG 8.9%, TRV 8.6% — slowest of the comparable four. Meanwhile:

> **CNA's underwriting profit has been flat in dollars — $559M, $585M, $496M, $551M — while
> net earned premium grew 23%. The incremental $1.4bn of earned premium added since 2023
> produced ZERO incremental underwriting profit.**

That is **[E2-44]**'s two-characteristic test failing on its second half: growth in dollar
volume is not being achieved *"with only minor additional investment of capital"* — it is
being achieved at a combined ratio that consumes the entire increment.

### Row 2: Boardwalk vs four midstream peers — **and Boardwalk is LAST**
*(WMB, KMI, OKE, ET — full working in `_research 2026-09-02 L/competitor_row_Boardwalk.md`)*

**The attacker metric — return on unleveraged net tangible operating assets**, FY2021–FY2025,
computed identically for all five as operating income ÷ (total assets − goodwill −
intangibles − non-interest-bearing current liabilities):

| | 5-yr mean | FY2021 | FY2025 |
|---|---|---|---|
| ONEOK | **11.7%** | | |
| Energy Transfer | 8.9% | | |
| Kinder Morgan | 8.8% | | |
| Williams | 7.1% | | |
| **Boardwalk** | **6.3%** | **5.3% (last)** | **7.6% (last)** |

**Boardwalk is last of five on the five-year mean, last in FY2021 and last in FY2025.**
It is **first** of five on operating margin (33.4% mean vs WMB 31.7%, KMI 24.7%, OKE 18.3%,
ET 10.8%) — and those are the same fact stated twice. Boardwalk carries the heaviest asset
base per revenue dollar in the group (asset turnover **0.22×**, about **$4.50 of assets per
dollar of revenue**). **The fat margin is a capital-intensity and regulated-tariff artifact,
not evidence of a moat.** **[E3-46]** asks the second question about the business as a number
— *"the best businesses, by definition, are going to be businesses that earn very high
returns on capital employed over time."* Boardwalk's answer is 6.3%, last in its own row.

*Caveats recorded rather than smoothed: KMI's $20.1bn of goodwill is 27.6% of its assets and
the goodwill deduction lifts its figure from ~6.5% to 9.9%, so the metric rewards whoever
wrote off the most purchase premium; Williams tags no separate intangibles, so its figure may
be understated. Neither moves Boardwalk off last place.*

### [E4-55] — THE PHYSICAL SERIES, CPI-U DEFLATED. **It does not replicate on Boardwalk.**

Ten Boardwalk 10-Ks, FY2016–FY2025, throughput read out of Item 1 of each:

| | 2016 | 2025 | change |
|---|---|---|---|
| average daily throughput (Bcf/d) | 6.3 | **10.7** | **+69.8%** |
| miles of natural-gas pipeline | 13,930 | 13,420 | −3.7% |
| working gas storage (Bcf) | 205.0 | 199.5 | −2.7% |
| real revenue (2025 $) | 1,753.5 | 2,305.8 | +31.5% |
| **real operating income (2025 $)** | **639.0** | **739.9** | **+15.8%** |
| real total assets (2025 $) | — | — | −9.3% |
| real revenue per Bcf/d | 278.3 | 215.5 | −22.6% |
| real operating income per Bcf/d | 101.4 | 69.1 | −31.8% |

**Reported both ways, because the denominator is contestable and the run should say so.**
The per-unit decline looks like the DG/Foot Locker/UAL signature, but **it is not the same
finding**: Boardwalk sells *reserved capacity*, not throughput, so extra gas moved over the
same reservation is designed to earn little. The test that survives the objection is real
operating income against real capital employed — **+15.8% on −9.3%** — and that is a business
whose returns are **improving**. The instrument that fired on DG, Foot Locker and UAL, and
correctly acquitted DICK'S, AEO and ULTA, **acquits Boardwalk.** Firm-contract share has held
at 81–90% for a decade and stands at **87%**; committed firm revenue rose **$14,184M →
$19,556M** in one year.

*Two disclosures against that, from the same filings: **$9.9bn of that $19.6bn backlog is
contingent** on regulatory approvals and permits and carries construction risk — the filer
says so — and **top-ten customer concentration has risen from 37–42% to 66%** in six years.*

### [E4-37] — THE INVERSE METRIC, AND IT FIRES HARD ON CNA

*"you can almost measure the strength of a business over time by the agony they go through in
determining whether a price increase can be sustained."* CNA publishes rate change by segment.
From four CNA 10-Ks (FY2022, FY2023, FY2025):

| rate change | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| **Specialty** (the highest-margin book) | **+11%** | +6% | **0%** | +1% | +3% |
| Commercial | +7% | +5% | +7% | +6% | +5% |
| **International** | **+13%** | +6% | +3% | −1% | **−4%** |

**Specialty went from +11% to zero.** International is now **cutting price 4% a year**. The
10-K names the cause in its own words: Specialty's combined ratio rose 2.7 points in 2025
*"primarily driven by **continued pricing pressure in management liability lines**."* This is
not a franchise with untapped pricing power **[E3-33]**; it is a business that had pricing
power in the 2021 hard market and has been handing it back for four years. **[E5-28]** scopes
the untapped-pricing class as *"a monopoly or a near monopoly"* — the competitor row does not
support that for CNA on any reading.

Retention over the same window is roughly flat (Specialty 86→86→88→89→86; Commercial
82→86→84→84→82), so the rate give-back is **not** being bought back in volume — it is
just price.

### [E4-04] and [E4-23] — rebuild, and the key person

- **[E4-04] rebuild test.** Boardwalk's moat is *defended*, not replaced: $194M a year of
  maintenance capital on assets whose rights-of-way do not expire. That is the Coca-Cola
  case, not the Rhodes Ridge case. **Boardwalk passes [E4-04].** CNA's position must be
  re-underwritten every twelve months against an open rate book; that is closer to the
  excluded class, and **[E2-70]** says the insurance business *"magnifies the effect which
  individual managers have on company performance"* — which is a moat defect under
  **[E4-23]**, not a compliment.
- **[E4-23], recorded here at Q2 as the corpus requires.** *"if a business requires a
  superstar to produce great results, the business itself cannot be deemed great."* Loews is
  a Tisch enterprise in its third generation: **Benjamin J. Tisch, 43, became President and
  CEO in January 2025**; James S. Tisch, 73, is now *"Chairman, Retired President and CEO"*;
  Alexander H. Tisch, 47, runs Loews Hotels. The capital-allocation record at Q3 is
  outstanding **and it is a record of particular people**. That is a moat defect at Q2, and
  it is recorded as one.

### THE STRONGEST CASE FOR A FRANCHISE, STATED BEFORE IT IS REJECTED
*(operator rule 9, and **[E4-51]**: state the argument against your position better than its
holders would)*

1. **Boardwalk's rights-of-way are genuinely irreplaceable.** 14,275 miles of pipe across
   thirteen states on easements and FERC certificates. No one is permitting a second Texas
   Gas. That is as close to a structural, non-rebuildable moat as this project has found.
2. **The contracts are long and the book is growing:** 87% capacity-reservation revenue,
   $19.6bn committed against $2.3bn of annual revenue, and the LNG/data-centre demand is real
   and is showing up in the returns — 5.83% → 7.21% → 7.57% on unleveraged net tangible
   operating assets in three years.
3. **CNA underwrites at a profit.** A combined ratio of 94.7% means the float is *better than
   free* — a real economic advantage the corpus explicitly values at **[E5-46]**.
4. **Loews retired 52.7% of its own shares at 0.81× book over seventeen years.** Per-share
   compounding does not require a moat if the discount is permanent.

**Why it fails anyway.** Points 1 and 2 are true and they describe **26.6% of earnings**, in a
business whose rates are set by *"the FERC's cost-based rate-making process"* and which earns
**7.6%** on its unleveraged tangible capital. Point 3 is true and it describes the **fifth-best
of five** underwriters on the row, losing ground in four of five years. Point 4 is a
capital-allocation finding and belongs at Q3, where **the guardrail forbids it from
promoting the name**: *"a textile company that allocates capital brilliantly within its
industry is a remarkable textile company — but not a remarkable business"* **[E2-37]**.
A superb repurchase record is exactly what [E2-48] says a good allocator does with a
mediocre business; it is not evidence of a moat.

**And [E2-53]'s dominance test is the cleanest refutation:** *"Once dominant, the newspaper
itself, not the marketplace, determines just how good or how bad the paper will be."* CNA's
2025 filing says the opposite about itself — the marketplace determined CNA's Specialty rate
(zero in 2023) and is determining its International rate (−4%). Position is not setting the
economics. The marketplace is.

- **Untapped pricing power [E3-33]?** No — the reverse. The rate series is a record of
  pricing power being surrendered, and **[E4-37]** reads that as a moat downgrade in real time.
- Class: **[ ] WIDE  [ ] NARROW  [x] NONE at the Loews level** *(NARROW at Boardwalk alone,
  which is 26.6% of earnings and is rate-capped)* · Direction: **narrowing at CNA, widening
  at Boardwalk**
- **VERDICT: [x] OUT**

**One line:** 70% of Loews' earnings come from an underwriter that ranks **fifth of five on
combined ratio in three of five years and fifth on the five-year mean**, whose Specialty rate
went **+11% → 0%** and whose International rate is **−4%**; the one business with a real
structural moat is 27% of earnings, earns **7.6%** on unleveraged tangible capital, and has
its rates set by the FERC's cost-of-service process. **[E3-03] criterion 2 fails at CNA and
criterion 3 fails at Boardwalk.**

---
# ⛔ THE FILE CLOSED AT Q2. WHAT FOLLOWS IS RECORDED EVIDENCE, NOT A GATE.

Q2 returned OUT, which is permanent and stops the run. Q3 and Q4 below were worked because
the brief ordered specific tests on them — the [E5-08] buyback record, the long-term-care
block, reserve development as candor, pay versus performance. **None of it can reopen Q2**
(*"a strong Q3 cannot promote a name, repair Q2, or substitute for Q4"* — **[E2-37, E2-38,
E3-39]**), and no verdict below is a gate verdict. It is filed so the next reader of Loews
does not have to redo it.

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? *(recorded, not a gate)*
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — THE WEIGHT CASE.**
- [x] **Daily execution** **[E3-38]**, and the corpus names this exact business as its 1977
      root: **[E2-70]** — *"their only products are promises… there is no question that the
      nature of the insurance business **magnifies the effect which individual managers have
      on company performance**."* 70% of earnings come from that business.
- [x] **Leverage [E3-29]** — Loews carries **$66,707M of liabilities against $18,686M of
      parent equity**. Small errors in a $26,599M claim reserve or a $13,448M long-term-care
      reserve destroy equity. The reserve is an estimate; the equity is the residual.
- [ ] Control — not ticked; L is freely traded and exit is available daily.

**Two of three ticked → Q3 is a BINARY GATE and no price compensates.** Declared before any
finding below was written.

**Honesty — binary, permanent, filings-based [E5-16].** **No disqualifier found.** Written as
the framework requires: this is *the absence of found disqualifiers*, not a finding that the
managers are honest — *"sincerity and empathy can easily be faked"* **[E5-17]**. No
restatement in the window; auditor **Deloitte & Touche LLP**, unchanged, non-audit fees
**2.1%** of $18,240k total; Item 9 reports no disagreements with accountants.

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30, E2-49].** *Each is a prompt to READ, never
a verdict.* **Most of them do not fire, and that is reported as found.**

| flag | fires? | what the filing actually says |
|---|---|---|
| weak accounting | **no** | clean opinions; no restatement in the window |
| unintelligible footnotes | **no** | segment Note 19 is legible and reconciles; the LTC note publishes a sensitivity table (below) |
| trumpeted projections **[E3-48, E5-30]** | **no** | Loews issues **no EPS guidance**. Boardwalk publishes a capex figure and can be tested on it: it guided 2025 firm-fee revenue to ~$1,512.0M and **delivered $1,639.5M** |
| serial share issuance **[E5-15]** | **no — the reverse** | **52.7% of the shares retired in 17 years** |
| **EBITDA promotion [E4-29]** | **YES** | *"Boardwalk Pipelines also utilizes a non-GAAP measure, earnings before interest, income tax expense, depreciation and amortization ('EBITDA')… as a financial measure to assess its operating and financial performance **and return on invested capital**."* Loews reconciles it in the 10-K: **EBITDA $1,174M against net income of $444M.** In a business whose D&A is **$443M**, EBITDA deletes almost the whole expense — precisely **[E5-41]**'s *"reverse float"* |
| CNA "core income" non-GAAP | **partly** | excludes investment gains/losses **and pension settlements**. The 2024 pension settlement charge was **$265M after tax and NCI** and core income excludes it — but Loews **quantifies it separately on the face of the MD&A**, so it passes the [E2-26] half-owner test rather than failing it |
| cash tax falling **[E4-30]** | **no** | cash taxes paid ÷ pre-tax income: **15.2% (2023), 21.5% (2024), 16.7% (2025)** against book tax rates of 22.6 / 20.3 / 22.4%. No downward drift. Only three years are tagged; stated as a limit |
| unnaturally smooth growth **[E4-30]** | **no — the opposite** | net income swings 822 → 1,434 → 1,414 → 1,667, and **2020 was a $931M loss** |
| **metric-switching [E2-49]** | **NO, and this is a clean acquittal** | the instrument that fired on HD, QCOM, ULTA and DKS **does not fire here**. Both the 2025 and 2026 proxies use identically-worded metrics — *"Performance-Based Income"* and *"Performance-Based Income per Share"* — and both state the Committee *"did not make any changes to the … executive compensation program or metrics after they were established in the first quarter."* The target **rose**, $4.15 → $4.55 |
| dividends funded by issuance **[E2-52]** | **no** | no issuance; dividends fell every year, $108M → $52M |

**STEP 3 — THE PRIMARY TEST [E2-01], AND IT IS THE WORST NUMBER IN THE RUN.**
*"The primary test of managerial economic performance is the achievement of a high earnings
rate on equity capital employed."* Net income attributable to the parent ÷ average parent
equity:

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | **10-yr mean** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Loews** | 3.66 | 6.23 | 3.37 | 4.95 | **−5.04** | 8.75 | 5.11 | 9.54 | 8.63 | 9.33 | **5.45%** |
| CNA | 7.24 | 7.43 | 6.93 | 8.54 | 5.54 | 9.94 | 6.94 | 13.07 | 9.40 | 11.55 | 8.66% |

**Loews' ten-year mean return on equity is 5.45% — level with the 30-year Treasury at 5.27%,
and [E2-42]'s red light is flashing:** *"Red lights should start flashing if the five-year
average annual gain falls much below the return on equity earned over the period by American
industry in aggregate."* CNA's 8.66% is better, and is **flattered**: its equity denominator
was cut from $11,105M to $8,548M in 2022 by the AOCI bond mark, so 2023–2025 are computed on
a smaller base.

**The half-owner test [E2-26] — and Loews passes it unusually well.** Two of three operating
subsidiaries file their own audited 10-Ks. The one-time items are quantified separately at
every line (the $265M pension settlement; the $25M hotel impairment; the $36M non-economic
A&EP charge). **[E4-31]'s third buyback condition — that shareholders be supplied the
information needed to estimate value — is satisfied more completely here than at any name in
this queue.**

**The institutional imperative [E2-30] — none of the four fires.**
No acquisitions soaking up funds (the largest 2025 use of cash was **buying its own stock**);
no peer imitation (peers grow, Loews shrinks); direction has been the same for two decades
and that is the *thesis*, not resistance to change; no consultant-led allocation
**[E3-58]** — allocation is done by the CEO and the family, not outsourced.

### CAPITAL ALLOCATION — THE BUYBACK RECORD, WHICH IS THE MAIN EVENT AT LOEWS
*(full table: `_research 2026-09-02 L/buyback_record.md`)*

| | |
|---|---|
| Shares outstanding 2008-12-31 → 2025-12-31 | **435,091,667 → 206,003,999** |
| Net shares retired | **229,087,668 = 52.7% of the company** |
| Total cash paid | **$11,276M** |
| Weighted-average price paid | **$48.09** |
| **Aggregate price ÷ book value per share** | **0.805×** |
| Dividends, same 17 years | $1,379M |
| Buybacks + dividends ÷ net income | **89%** |

**Condition 1 [E5-08] — ample funds: PASSES.** Parent cash and investments net of receivables
and payables **$3.9bn** at 2025-12-31 (up from $3.3bn), against $52M of dividends and no
parent guarantees of subsidiary debt. Loews received **$1.5bn** of subsidiary dividends in
2025 and expects $691M in Q1 2026 alone.

**Condition 2 [E5-08] — below a conservative estimate of intrinsic value: PASSES ON THE
RECORD, on the only seventeen-year yardstick the filings support.** Loews bought **below
year-end book value in every one of seventeen years**, range **0.63× (2020) to 1.00× (2025)**.
Two cautions are recorded *against* Loews rather than for it: year-end book flatters the ratio
in rising-book years because purchases are spread through the year; and the 0.94× of 2022 was
against a book temporarily depressed $3.5bn by the AOCI bond mark.

**And the disconfirming evidence, hunted per [E4-26] and found:** the Q4 2025 monthly
purchases were made at **$99.26, $104.33 and $104.53 against year-end book of $90.71 —
1.09× to 1.15×, the first clear premium to stated book anywhere in the twenty-year file.**
The discount is closing: 0.63×–0.86× through 2023, then 0.99×, then 1.00×, then a premium.
**[E5-24]** governs — *"what is smart at one price is dumb at another"* — and on this record
the buyback is at the point where it stops being obviously smart.

**Condition 3 [E4-31] — PASSES**, see the half-owner test above.

**But the POLICY is an absence, and [E5-25] is the contrast.** *"Intrinsic value" appears
**zero times** in the FY2025 10-K and **zero times** in the 2026 proxy.* So do "undervalued"
and "discount to." The entire stated policy is:

> "Our Board of Directors has authorized our management, as it deems appropriate, to purchase
> our outstanding common stock. Depending on market and other conditions, we may purchase
> shares of our common stock in the open market … in privately negotiated transactions or
> otherwise." — FY2025 10-K, Item 5, verbatim

Columns (c) and (d) of the issuer-purchases table read **"N/A"**: no announced program, no
dollar cap. Berkshire, by contrast, **published both conditions as numbers in advance** — the
110%-of-book limit and the $20bn liquidity floor **[E5-25]**. And the proxy credits the CEO
for buybacks **by volume, never by price**: *"Loews repurchased approximately 8.9 million
shares, or 4.2%, of its common stock in 2025."* Nothing in the compensation language
distinguishes 0.63× from 1.15×. **Seventeen years of disciplined behaviour rests on no stated
policy management could be held to.**

### [E3-54] — THE RETENTION TEST, AND IT FAILS ELEVEN OF TWELVE WINDOWS

*$1 of market value per $1 retained, five-year rolling.* Market value = year-end price ×
year-end shares. Retained = net income attributable to Loews − dividends.

| window | Δ market value $M | MV per $1 retained |
|---|---|---|
| 2009–2014 | +219 | **0.06** |
| 2010–2015 | −3,078 | **−1.19** |
| 2011–2016 | +833 | 0.38 |
| 2012–2017 | +648 | 0.23 |
| 2013–2018 | −4,474 | **−1.56** |
| 2014–2019 | −398 | −0.12 |
| 2015–2020 | −932 | −0.45 |
| 2016–2021 | −1,415 | −0.47 |
| 2017–2022 | −2,839 | −1.06 |
| 2018–2023 | +1,262 | 0.36 |
| 2019–2024 | +2,910 | 0.73 |
| **2020–2025** | **+9,574** | **1.45** ✓ |
| **full 16 years** | **+6,243** | **0.50** |

**Loews earned $13,718M over sixteen years and its total market capitalisation rose $6,243M,
from $15,451M to $21,694M — 40%.** Only the most recent window passes.

**The counter-argument, stated as fairly as its holders would [E4-51].** This test is harsh on
a company that returns capital by *shrinking*. Read a third way — capital **actually left in
the business** = $13,718M − $1,271M dividends − $10,942M buybacks = **$1,505M**, against
$6,243M of market value created = **$4.15 per $1**. And per share the record is good: the
stock went **$36.35 → $105.31, +190% in sixteen years (~6.9%/yr)**, and book value per share
went **$39.76 → $90.71, +128%**, while total equity rose only **10.6%**.

**All three readings are the same fact:** the buyback machine worked at the per-share level
and the consolidated business did not grow. That is exactly **[E2-48]**'s behavioural tell of
the rare good allocator — *"often have found repurchase of their own shares to be the most
sensible employment of corporate capital"* — applied to a 5.45%-ROE business. Which is
**[E2-37]** verbatim: *"a textile company that allocates capital brilliantly within its
industry is a remarkable textile company — **but not a remarkable business**."*

**[E2-60] — distributions vs owner earnings.** Buybacks + dividends were **89% of net income**
over seventeen years, funded by subsidiary dividends, not by borrowing at the parent. Parent
cash **rose** $3.3bn → $3.9bn in 2025. **Does not fire.**

### PAY VERSUS PERFORMANCE, AND SUCCESSION

**Item 402(v) table** (company-selected measure: **"Performance-Based Income (millions)"**):

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| SCT total, PEO | 6,119,523 | 6,439,183 | 6,918,337 | 7,069,657 | **8,753,165** |
| Compensation actually paid, PEO | 6,727,729 | 6,487,578 | 7,276,014 | 7,651,106 | 11,974,575 |
| **Loews TSR** (of $100) | 128.89 | 130.73 | 162.96 | 209.17 | **277.70** |
| **Peer group TSR** | 127.73 | 156.52 | 165.68 | 255.91 | **287.03** |
| Net income $M | 1,562 | 822 | 1,434 | 1,414 | 1,667 |
| Performance-Based Income $M | 1,211 | 1,159 | 1,601 | 1,865 | 1,873 |

**The peer group beat Loews in four of five years and finishes ahead cumulatively**
($287.03 vs $277.70). CEO pay is modest by the standards of a $22bn company: 2025
**$8,753,165** including a one-time SAR grant, **$4,659,665 without it**; pay ratio **93:1**
(~50:1 ex-SAR). The new CEO is paid *less* than his cousin who runs the hotels.

**The pay design's real defect is the target, not the metric.** Payout was **100% of target,
to the dollar, for every named officer in both 2024 and 2025** — because actual
performance-based income per share was **$8.96 against a $4.55 target (197%)** in 2025 and
**$8.46 against $4.15 (204%)** in 2024, and vesting is **capped at 100%**. A bar set at half
the achievable level and capped at target is not an incentive; it is a salary with extra
steps. It is not, however, a **[E2-49]** switch, and this run says so plainly.

*One genuinely well-designed element, recorded because it is rare:* the 2025 special SARs to
the incoming CEO and two others are struck at **$100 / $150 / $200 against an $83.01 stock**,
seven-year cliff, ten-year term. Premium-priced options are the honest form.

### [E4-23] — SUCCESSION, AND THE FINDING IS AN ABSENCE

**Benjamin J. Tisch, 43, became President and CEO in January 2025.** James S. Tisch, 73, is
*"Chairman, Retired President and CEO."* Andrew H. and Jonathan M. Tisch are directors
emeritus. **The third-generation transition has already happened.**

**And the word "succession" appears exactly once in the entire 2026 proxy**, inside a
Compensation Committee charter clause whose three enumerated duties are all about pay:

> "The Compensation Committee assists our Board in discharging its responsibilities relating
> to compensation and succession planning for our executive officers. These responsibilities
> include: ▪ reviewing our general compensation philosophy for executive officers; ▪ overseeing
> the development and implementation of executive compensation programs; and…"

**There is no succession section, no emergency plan, no described process — in the proxy
covering the first full year after a CEO change.** That is the disclosure the brief asked to
be named, and the answer is its absence.

**Control is de facto, not structural — which corrects a common assumption.** Five named
Tisches hold **38,781,506 of 205,767,698 shares = 18.85%**, and are 99.3% of the entire
insider group. **The phrase "controlled company" appears zero times**; there is no dual-class
stock, no voting agreement, no 13D group. 75.5% of the family stake sits in trusts. The
chairman is **not independent**, and the independent majority narrows from 8-of-12 to
**6-of-10** on the slate being voted. One quiet loosening: executive sessions moved from
*"Independent directors meet in executive session"* (2025) to *"Non-management directors,
other than James S. Tisch"* (2026), admitting a director expressly non-independent until 2029.

**Related-party, recorded:** Jonathan M. Tisch was paid **$3,396,154** as Executive Chairman
of Loews Hotels (retired 2025-12-31; consulting at $1,000/hr up to 200 hrs), and *"a member of
the Tisch family began leasing an apartment at the Loews Regency New York Hotel on a
month-to-month basis at an initial rate of $65,000 per month"* — **tenant unnamed, and no
statement that it is at market.** Small in dollars; noted because it is the one place the
filing declines to answer the [E2-26] question.

**THE GUARDRAIL — checked before writing anything.**
- [x] Confirmed: **nothing in this Q3 is used to promote the name.** The buyback record is the
      best capital-allocation record this project has found and **it does not repair Q2**
      **[E2-37, E2-38, E3-39]**.
- [x] Key-person dependence is recorded at **Q2 as a moat defect [E4-23]**, not here as a
      strength.
- [x] Is the franchise intact with excisable damage, or is the manager the plan? **The
      manager is the plan.** Strip out the repurchase and Loews is a 5.45%-ROE holding
      company. That is **[E2-36]**'s *"corporate Pygmalion"* side of the line, not the
      excisable-cancer side.

- **RECORDED (not a gate): IN — no disqualifier found.** Honest, unusually transparent,
  genuinely good at the one thing they do. *IN never promotes, and here it promotes nothing.*

## Q4 — WILL IT SURVIVE? *(recorded, not a gate — the file closed at Q2)*

### THE SECTOR METHOD SAYS: DO NOT COMPUTE AN OWNER-EARNINGS YIELD HERE

*"The corpus does not compute an owner-earnings number for a float-bearing company; it values
two measurable components plus a judgment."* The screen computed one anyway, and the run's
job is to show exactly why the construction fails. **The screen is not wrong by some amount.
It is a category error, and it is the largest one this queue has produced.**

**Reproduction first.** Five-year window FY2021–FY2025, `mean[OCF − max(D&A, capex)] − SBC`:

| $M | 2021 | 2022 | 2023 | 2024 | 2025 | mean |
|---|---|---|---|---|---|---|
| operating cash flow | 2,623 | 3,314 | 3,907 | 3,025 | 3,279 | 3,229.6 |
| capex | 482 | 660 | 686 | 632 | 579 | 607.8 |
| D&A | 503 | 509 | 534 | 580 | 607 | 546.6 |
| **insurance-reserve increase, inside OCF** | **2,463** | **1,791** | **1,667** | **2,365** | **1,670** | **1,991.2** |

**= $2,585.0M. The screen's $2,585M reproduces to the dollar.**

### THE CORRECTION CHAIN, EACH STEP NAMED

| step | correction | authority | owner earnings | yield on $22,380M |
|---|---|---|---|---|
| 0 | screen as printed | — | **2,585** | **11.55%** |
| 1 | less 8.2% of CNA's operating cash flow | **[E5-46]** | 2,391 | 10.68% |
| 2 | less the insurance-reserve increase (float growth) | **[E2-61]** | **400** | **1.79%** |
| 3 | less net investment income, which is component 1 | **[E5-48]** | negative | — |
| 4 | (c) rebuilt per business — **moves it the other way** | **[E5-20]** | +~190 | +0.85 pt |

**Step 1.** CNA supplies **73.4%** of consolidated operating cash flow ($2,369M of $3,229.6M)
and **8.2%** of CNA belongs to someone else — the 2025 income statement books $105M of
$1,278M to noncontrolling interests. **[E5-46]**'s "net of minority interests" costs $194M.

**Step 2, and it is the whole story.** The insurance-reserve line inside operating cash flow
averages **$1,991.2M a year — 77.0% of the screen's entire owner-earnings figure.** That is
premiums collected against losses not yet paid. It is **borrowed money**, and **[E2-61]** is
explicit that its arrival is the symptom of the failing insurer, not evidence of the healthy
one: *"you can be broke but flush… insolvent insurers don't run out of cash until long after
they have run out of net worth. In fact, these 'walking dead' often redouble their efforts to
write business, accepting almost any price or risk, simply to keep the cash flowing in."*
The UNH run of 2026-08-31 stripped exactly this and was vindicated. **Remove it and 11.55%
becomes 1.79%.**

**Step 3.** Mean net investment income is **$2,403M** and it sits inside operating cash flow.
Any construction that takes a yield on OCF **and** credits the $55,376M portfolio has counted
the portfolio twice **[E5-48]**. Removing it drives the non-investment result negative — which
is not a separate finding but the same one: **the yield construction has no referent here.**

**Step 4 — and this is the honest surprise, reported because it cuts against the run's own
direction.** Rebuilding (c) per business **raises** owner earnings:

| business | 2025 capex | 2025 D&A | **(c) judged** | basis |
|---|---|---|---|---|
| **Boardwalk** | 354 | 443 | **194** | **the filer discloses maintenance capital directly** |
| CNA | 86 | 70 | 86 | a securities portfolio does not wear out |
| Loews Hotels | ~139 | 100 | ~139 | renovation cycle is real; judged up from D&A |
| **total** | **579** | **~613** | **~419** | |

**Boardwalk publishes the number [E5-20] asks a run to guess:** *"In 2026, Boardwalk Pipelines
expects to spend approximately $530 million to maintain its pipeline systems… of which
approximately $225 million is expected to be **maintenance capital**. In 2025, Boardwalk
Pipelines spent $516 million on these matters, of which **$194 million was recorded as
maintenance capital**."* Capex is split in the MD&A every year: **2025 $354M = $160M growth +
$194M maintenance; 2024 $392M = $190M + $202M.**

**This overturns the run's prior about [E5-20], and the finding generalises.** The competitor
row establishes that **maintenance capex runs at 0.15×–0.48× of D&A for every midstream filer
that shows its work** (Boardwalk FY2025: **0.44×**). **[E5-20]'s railroad exception — "merely
spending their depreciation expense will not keep them in the same place" — DOES NOT TRANSFER
TO PIPELINES.** For a railroad D&A understates renewal; for these pipelines D&A **overstates**
it by more than two to one. Using D&A as (c) here understates Boardwalk's owner earnings by
about **$249M**, a third of its operating income. *(Also found: **Williams and ONEOK disclose
no maintenance-capex figure at all** — the string does not occur in ONEOK's FY2025 10-K — so
for those two, owner-earnings item (c) cannot be sourced from the 10-K.)*

### COMPONENT 1 — INVESTMENTS AT MARKET, NET OF MINORITY INTERESTS **[E5-46]**

| | $M |
|---|---|
| Total investments, consolidated, at fair value (10-K balance sheet) | **55,376** |
| Cash | 495 |
| less: noncontrolling interests' share | **(955)** |
| **Component 1, net** | **≈ 54,916** |

Composition: fixed maturities $43,984 · equity securities $1,292 · limited partnerships
$2,861 · other invested assets (mostly mortgage loans) $1,195 · short-term $6,044.
**CONVENTION 1 of the sector method applies** — "at market" is taken as the filer's reported
balance-sheet fair value, with **[E5-32]**'s cap: the filed statement is not bedrock.

### COMPONENT 2 — THE COST OF FLOAT **[E3-69]**, MULTI-YEAR, AND IT IS THE RUN'S KEY NUMBER

*"a comparison of underwriting loss to float developed… meaningless over short time periods…
A low cost of funds signifies a good business; a high cost translates into a poor business."*
**CONVENTION 2: the window is the five years FY2021–FY2025, and it is stated.**

Float = claim and claim adjustment expense reserves + unearned premiums − reinsurance
recoverables − premiums receivable − deferred acquisition costs.

| yr | float | **P&C underwriting gain** | **P&C cost of float** | **whole insurance operation** | **total cost of float** |
|---|---|---|---|---|---|
| 2021 | 17,884 | +290 | −1.53% | −767 | +4.04% |
| 2022 | 19,114 | +559 | −3.02% | −752 | +4.07% |
| 2023 | 20,487 | +585 | −2.95% | −646 | +3.26% |
| 2024 | 21,641 | +496 | −2.35% | −1,134 | +5.38% |
| 2025 | 23,128 | +551 | −2.46% | −772 | +3.45% |
| **5-yr** | **mean 20,143** | **+$2,481M** | **−2.46%** | **−$4,071M** | **+4.04%** |

**Read this carefully, because the two lines say opposite things and both are true.**

- **CNA's property & casualty book generates float at −2.46% a year. That is better than
  free, and it is a real economic advantage.**
- **CNA's insurance operation as a whole costs +4.04% a year**, because the long-term-care,
  A&EP, legacy excess-workers'-comp and mass-tort runoff blocks consumed **$4,071M** over the
  same five years — more than the P&C book earned.
- Against a **5.27%** sovereign, 4.04% money is cheaper than the government's, **by 1.23
  points.** It is not free money, and **[E3-69]**'s verdict on "a high cost" is a matter of
  judgment at this level rather than an obvious pass.

Float grew $18,880M → $23,128M over nine years, **+22.5% nominal and −8.7% real** after CPI-U.
**Loews' 91.8% share of 2025 float ≈ $21,232M.**

### COMPONENT 3 — PRE-TAX EARNINGS OF EVERYTHING ELSE, INVESTMENT INCOME REMOVED **[E5-48]**

| $M, FY2025 pre-tax | as filed | investment income removed |
|---|---|---|
| Boardwalk Pipelines | 584 | **570** (less $14M interest income) |
| Loews Hotels & Co | 52 | 52 |
| Corporate (ex investment income) | 27 | **(169)** |
| CNA — non-investment result | — | **(772)** |
| **total** | | **≈ (319)** |

**With investment income properly removed, Loews' second component is NEGATIVE.** Everything
the group earns, it earns on the portfolio. That is the arithmetic statement of what Q2 found
qualitatively.

### GREAT, GOOD, OR GRUESOME? **[E4-20]**
- [ ] great  [x] **good, at Boardwalk only**  [ ] gruesome
- **Boardwalk is the [E4-43] "good" class and it passes on its own**: attractive-ish return
  earned also on added capital. But **[E5-40]** gives the good class a number — ~12% on
  retained utility capital is *"quite satisfactory"* — and Boardwalk earns **7.6%**, last of
  five in its row.
- **CNA is closer to gruesome than to good on the increment.** It grew net earned premium 23%
  since 2023 and its underwriting profit went 585 → 496 → 551. *"attracted by growth when
  they should have been repelled by it."* It is not gruesome outright, because it does earn
  8.66% on equity.
- **At the Loews level the answer is the 5.45% ten-year mean ROE**, and no consolidation of
  the three makes that number better.

### STAYING POWER — SCORED WITH THE THREE MANDATORY SUBSTITUTIONS **[E5-11, E2-61]**

**(1) A large and reliable stream of earnings — PARTIAL.** Large, yes: $1,667M in 2025.
Reliable, no: 822 → 1,434 → 1,414 → 1,667, and **2020 was a $931M loss**. **[E5-29]** scopes
this correctly — volatility is not risk — and **[E3-55]** says a certain endgame with a bouncy
figure is fine. The bounce here is genuine catastrophe and mark-to-market noise, not a
solvency signal.

**(2) SUBSTITUTED, per [E2-61]: reserve adequacy and net worth, NEVER cash on hand.**
*The [E5-11] strength-(2) test returns a FALSE PASS on an insurer if run unchanged — Loews
shows $55.4bn of investments and $3.9bn of parent cash, and none of that is the question.*

- **Reserve development is the honest read, and it is ADVERSE AND ACCELERATING:**

| pretax (favorable)/unfavorable development | 2023 | 2024 | 2025 |
|---|---|---|---|
| Specialty | (14) | (9) | **37** |
| Commercial | (22) | (16) | **39** |
| International | 13 | (6) | (25) |
| **Corporate & Other** (A&EP, EWC, mass tort) | **71** | **79** | **134** |
| **Total** | **48** | **48** | **185** |

  **Three consecutive years of unfavorable development, and 2025 is nearly four times 2024.**
  Both ongoing segments flipped from favorable to unfavorable in 2025.
- **Net worth:** CNA common equity **$11,621M**; Loews parent equity **$18,686M**. CCC's
  maximum 2026 ordinary dividend without regulatory approval is **$1.3bn**, and CCC was in a
  positive earned-surplus position. Ratings: **A.M. Best UPGRADED CNA to A+ in December 2025**;
  Moody's A2 positive; S&P A+; Fitch A+. Loews itself is **A / A3**.
- **Statutory long-term-care margin $1.5bn at 2025-09-30, up from $1.4bn.**

**(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — PASSES, and it passes the [E2-64] way.**
This is the strength that killed UAL, and Loews does the opposite. Short-term debt rose $5M →
$1,052M, and **both maturities were pre-financed before the need**: Boardwalk issued $550M of
5.4% notes in **November 2025** to redeem $550M of 6.0% notes due June 2026, and Loews issued
4.9% notes due 2036 in **February 2026** against its 3.8% notes repaid 2026-03-19. Boardwalk's
**$1.0bn revolver was undrawn** and was extended to November 2030. *"the most attractive
opportunities may present themselves at a time when credit is extremely expensive"*
**[E2-64]** — this is a balance sheet built the way the corpus asks. **No reliance on the
kindness of strangers [E5-39].**

*The real near-term calls, named and quantified:* claim reserves due within one year
**$5,983M**; future policy benefits due within one year **$862M**; Boardwalk's **$3.3bn**
growth programme through 2030 plus **$355M** of binding purchase orders; the **$400M**
Arlington hotel. Against **$3.9bn** of parent liquidity, **$1.5bn** of annual subsidiary
dividends and **$1.0bn** of undrawn revolver.

**Leverage, named and quantified [E4-16, E3-29]:** $8,437M long-term + $1,052M short-term debt
against $18,686M of parent equity. But **[E3-52]** is the governing read: the $47,682M of
insurance reserves are *"liabilities **without covenants or due dates** attached to them"* —
they are not debt, and the **coverage test [E2-54]** passes comfortably ($437M of consolidated
interest against $3,279M of operating cash flow, before any capex).

### THE CANDOR TEST **[E2-67]** — AND CNA PASSES IT

*"judge whether we may have some systemic bias that should make you wary of our current and
future figures."* **CNA publishes the full ten-year loss-development triangle by segment and
by line, and names its own errors specifically** — down to *"an agreement with the Diocese of
Rochester"* and *"higher than expected claim severity and frequency in the Company's
professional errors and omissions (E&O) business."* **The direction of the error is adverse,
it is worsening, and the filer says so in its own words.** That is the positive pole of
[E2-67] — the Berkshire behaviour, done by CNA. It also publishes a **hypothetical-revision
sensitivity table** for the long-term-care assumptions, which is more than the framework asks
for. **Candor: PASS. The reserves: adverse.**

### LONG-TERM CARE — THE BLOCK THE BRIEF EXPECTED TO BE THE KILLER. IT IS NOT.

| | |
|---|---|
| Future policy benefit reserve, discounted | **$13,448M** |
| Undiscounted future benefit payments | **$31,323M** |
| **Reinsurance ceded** | **NIL — the block is entirely unreinsured** |
| Ratio to CNA common equity ($11,621M) | **1.16×** discounted, **2.7×** undiscounted |
| Duration | ~11 years |
| FY2025 core loss | **$(44)M** |
| Earned premium vs interest accretion | $423M vs $742M |
| 2025 annual assumption review | pretax reserve increase of **$7M** (2024: $15M) |
| Statutory margin | **$1.5bn**, up from $1.4bn |
| Auditor treatment | **Critical Audit Matter** |

**The brief asked about "any reinsurance transaction covering it." There is none. Ceded
reserves on the long-term-care block are nil.** *(By contrast the A&EP block **was** ceded to
NICO effective 2010-01-01 — CNA solved that problem with a loss portfolio transfer and has
not done the same for LTC.)*

**The filing's own sensitivity table, which is what [E4-40] asks for — exposure, not
experience:**

| hypothetical revision | estimated reduction to pre-tax income |
|---|---|
| 2.5% increase in morbidity | $300M |
| **5% increase in morbidity** | **$620M** |
| 5% decrease in active life mortality and lapse | $180M |
| **10% decrease in active life mortality and lapse** | **$350M** |
| 50% decrease in anticipated future premium rate increases | $50M |

**Run the worst combination the table offers: $620M + $350M + $50M = $1,020M pre-tax.**
Against a **$1.5bn** statutory margin and **$11,621M** of CNA equity, that is
**8.8% of CNA's equity and about 61% of one year's Loews net income.** Painful. Not fatal.
**The LTC block is unreinsured, larger than CNA's equity, and it is the wrong answer to
"name the way this dies."**

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24]**

**The mechanism is not long-term care. It is a long-tail casualty reserve cycle at the P&C
book, and the filing is already showing its early form.**

CNA carries **$26,599M** of claim and claim adjustment expense reserves. Most of the book is
long-tail by the company's own description — *"it will generally be several years between the
time the business is written and the time when all claims are settled"* — across commercial
auto liability, workers' compensation, general liability, medical professional liability,
professional and management liability. Reserve development has been **unfavorable in each of
2023, 2024 and 2025, and the 2025 figure is 3.9× the 2024 figure.** The named drivers are
**social inflation** and **legacy mass tort abuse claims** — both secular, neither cyclical.

**Quantified from filed figures, in the [E3-24] form:**

| deficiency across the $26,599M net claim reserve | pre-tax | after tax (21%) | vs CNA equity $11,621M | vs Loews net income |
|---|---|---|---|---|
| **5%** | $1,330M | $1,051M | **9.0%** | **0.63 years** |
| **10%** | $2,660M | $2,101M | **18.1%** | **1.26 years** |
| **20%** | $5,320M | $4,203M | **36.2%** | **2.52 years** |

**And the compounding fact that makes this the death and not an inconvenience:** at a
**94.7%** combined ratio, CNA's entire annual underwriting profit is **$551M**. A 5%
deficiency consumes **two years** of it. A 10% deficiency consumes four. CNA has **no
underwriting margin to absorb a reserve cycle with**, because it is fifth of five and the
$1.4bn of premium it added since 2023 produced **zero** incremental underwriting profit. And
**the runoff blocks are already consuming the P&C book's entire float credit** — that is what
the +4.04% total cost of float against the −2.46% P&C cost of float means.

**Model exposure, not experience [E4-40].** The benign figure to resist is the 94.7% combined
ratio in a late hard market. CNA's Specialty rate has gone **+11% → 0% → +1% → +3%** and
International is at **−4%**: the business is being written at prices set in a softening
market, and long-tail losses from a soft market emerge five to ten years later. **[E2-58]**
names the equation — *"persistent over-capacity without administered prices (or costs) equals
poor profitability"* — and the P&C cycle is its canonical case.

- **Likelihood: [ ] likely  [x] a real possibility  [ ] a low-level possibility** — for a
  5% deficiency across a cycle. A 10% deficiency is a low-level possibility. Neither is
  solvency-threatening at Loews, whose parent holds $3.9bn and guarantees nothing; **both
  would eliminate several years of the earnings the current price is paying for.**

- **RECORDED (not a gate): IN on survival, with the reserve cycle named and priced.**
  Loews survives. The question Q2 already answered is whether it compounds.

---
### THE TEMPLATE'S OWNER-EARNINGS FIELDS — WHY THEY ARE NOT FILLED IN

The template's short-window/long-window/capex-band fields assume a single operating business
with a single (c). **Loews has four businesses, one of which is a securities portfolio.**
The sector method's whole point is that *"the corpus does not compute an owner-earnings number
for a float-bearing company."* Every field the template asks for has been answered above in
the form the corpus actually supports:

| template field | where it is answered |
|---|---|
| short/long window means, spread | the correction chain — $2,585M as printed, $400M float-corrected, a **6.5× spread** |
| is the range too wide to conclude? | **Yes, and per [E4-25] that IS the conclusion** — see the component-1 range of $35.39–$273.30/share |
| maintenance capex, D&A default vs [E5-20] | **(c) built per business.** Boardwalk's is **disclosed by the filer** at $194M against $443M of D&A — **0.44×, so [E5-20]'s railroad exception INVERTS for pipelines** |
| stock compensation | $27M/yr, subtracted in full in every construction |
| great/good/gruesome | answered above: good at Boardwalk, marginal at CNA, **5.45% ten-year ROE at Loews** |
| staying power (1)(2)(3) | answered above with the three **[E2-61]** substitutions |
| named way it dies | answered above: a long-tail casualty reserve cycle, quantified at 5/10/20% |

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass. **Q2 returned OUT. Q5 did not open.**

---
# COMPUTATION — NOT A CLEARANCE
**Operator rule 3.** Q2 returned OUT. Q5 did not open and cannot. Everything below is
arithmetic produced to satisfy the queue's output contract (a price, either way) and to
answer the sector-method questions the brief posed. **It carries no entry language and it is
not a valuation verdict.**

## THE SECTOR-METHOD CORRECTIONS APPLIED, AS RULED

**RULING 1 — step 2 is DIAGNOSTIC, not additive.** The cost of float computed at Q4 is a
quality test in the sense of **[E3-69]** — *"A low cost of funds signifies a good business; a
high cost translates into a poor business"* — and **[E3-69] never adds it to anything**.
Under the **[E5-48]** amendment, underwriting income belongs inside component 2, once. The
figures below **do not add the cost of float to the sum**. Restated for the record:
**CNA's P&C float costs −2.46%; the whole insurance operation's float costs +4.04%; the
sovereign is 5.27%. That is a judgment input, and the judgment it supports is "adequate, not
free."**

**RULING 2 — investments ÷ equity is the ratio that governs whether [E5-46] is safe, and
Loews is the worst case this queue has produced.**

| | float ÷ investments | **investments ÷ equity** |
|---|---|---|
| Berkshire (the case [E5-46] was written from) | — | **0.45×** |
| Markel | 50.3% | 2.01× |
| White Mountains | 22% | — |
| **Loews, consolidated** | **41.8%** | **2.96×** |
| **CNA alone** | **45.8%** | **4.34×** |

**The MKL run's argument is correct and Loews is its extreme case.** Berkshire's investments
were *smaller than its own equity*, so counting them gross at market could not double-count.
Loews' investments are **nearly three times** its parent equity, and CNA's are **more than
four times** its own. **Two-thirds of the portfolio is funded by liabilities.** Counting it
gross is not conservative; it is wrong.

**RULING 3 — component 1, gross vs net, and the ambiguity is worth more than the whole
company.** The corpus does not specify. Stated four ways:

| construction | $M | per L share |
|---|---|---|
| gross consolidated investments + cash | 55,871 | **$273.30** |
| less noncontrolling interests at book | 54,916 | $268.63 |
| Loews' 91.8% of CNA's investments, plus non-CNA investments | 51,239 | $250.65 |
| **less ALL insurance reserves ($47,682M)** | **7,234** | **$35.39** |

**The range is $35.39 to $273.30 per share against a $109.475 price — a 7.7× spread produced
entirely by a choice the corpus does not make.** Per **[E4-25]**, *"the range must be so wide
that no useful conclusion can be reached"* — **and that width IS the conclusion for the
component-1 route.** This run therefore **abandons the [E5-46] two-component construction for
Loews** and prices the parts instead. **I adopt the net-of-reserves discipline in spirit:
the portfolio is not an asset of Loews shareholders except to the extent it exceeds the
promises it was collected to pay.** *(**[E3-71]**'s deferred-tax treatment — Munger valuing
the deferred-tax liability as the advantage of an interest-free loan, *"never at face and
never at zero"* — would apply to the $839M deferred income tax liability; at ~$4/share it is
immaterial to the conclusion and is noted rather than modelled.)*

**RULING 4 — [E5-48] destroys a business whose model IS holding investments, and CNA is that
business. Both constructions stated.**

| construction | FY2025 component 2, pre-tax |
|---|---|
| **(a) [E5-48] applied literally** — all dividends and interest stripped | **≈ $(319)M** |
| **(b) investment income retained as operating** — a P&C insurer's return on float is how the business works | **≈ $2,084M** |

**The gap is $2,403M — larger than the sum itself.** Construction (a) is the row as written
and it makes Loews' non-portfolio earnings **negative**; construction (b) double-counts the
portfolio if component 1 is also credited. **Neither is usable alone, and the method decides
neither.** This is the WTM/Kudu wall in its sharpest form: at WTM the two constructions
differed by 27%; **here they differ by 175% of the smaller.** The resolution adopted is the
MKL run's — **abandon the two-component sum and use a look-through sum of the parts**, below.

**RULING 5 — [E5-48] pre-dates ASU 2016-01, and the extension is disclosed, not smuggled.**
The 2015 row says *"dividends and interest."* Since 2018, equity marks run through income.
**At CNA they run through Net investment income itself** — the 10-K states *"Common stock is
owned with the intention of holding the securities primarily for market appreciation and as
such, the changes in the fair value of these securities are recorded through Net investment
income."* So CNA's **$302M** of "Limited partnership and common stock investments" income in
2025 (2024: $320M) is substantially **mark**, not dividends and interest, and Loews' parent
trading portfolio adds more inside the Corporate segment's $196M. **Roughly $400–500M of the
consolidated $2,779M of net investment income — about 15–18% — is unrealized mark that the
[E5-48] row does not name.** *Disclosed judgment: this run strips it with the rest in
construction (a) and retains it in construction (b), and reports both, because the corpus
cannot be made to say more than "dividends and interest."*

**RULING 6 — holding-company debt, stated.** From Note 11, by entity, at 2025-12-31:

| | $M net | % of market cap | recourse to parent? |
|---|---|---|---|
| **Loews Corporation (parent)** | **1,786** | **8.0%** | **yes** |
| CNA Financial | 2,971 | 13.3% | no |
| Boardwalk Pipelines | 3,782 | 16.9% | no |
| Loews Hotels & Co | 1,001 | 4.5% | no (property-secured) |
| **total consolidated** | **9,489** | 42.4% | |

**81.2% of consolidated debt is non-recourse to the parent**, and the 10-K says so verbatim:
*"We are not responsible for the liabilities and obligations of our subsidiaries and **there
are no Parent Company guarantees**."* **Only the $1,786M of parent debt is deducted below.**

**RULING 7 — float ÷ premium, so the cost of float can be read against a peer.**
**CNA float ÷ P&C net earned premium = 2.21×** (2.12× on total premium). This is a long-tail
book, so a given combined ratio produces a *smaller* percentage cost of float than at a
short-tail writer — the −2.46% P&C figure is **not** comparable to a short-tail peer's without
this ratio beside it. And the run's own warning: **CNA's long-tail casualty and its 11-year-
duration LTC block sit at very different durations from each other**, so even the blended
2.21× conceals two businesses.

## THE ACCIDENT-YEAR DECOMPOSITION — THE TEST THAT CLOSED MKL, AND **CNA PASSES IT**

*Run because the WTM finding says the triangle alone can miss where the news is.* Adding back
prior-year development to the reported combined ratio:

| | reported CR | prior-year development $M | points | **current accident year CR** |
|---|---|---|---|---|
| 2023 | 93.5 | (23) favorable | −0.25 | **93.8** |
| 2024 | 94.9 | (31) favorable | −0.32 | **95.2** |
| 2025 | 94.7 | **51 unfavorable** | +0.49 | **94.2** |
| *MKL, for contrast* | | | | *99.3 / 101.1 / 100.3* |

**CNA's underwriting made money on business actually written in all three years, and its 2025
reported ratio is made WORSE by prior-year development, not better.** CNA is not hiding a
deteriorating accident year behind reserve releases — it is absorbing adverse development
into a reported number. **This is a real finding in Loews' favour, produced by an instrument
run to refute it**, and it is reported as prominently as the findings that went the other way.
*It does not change Q2:* 94.2 on the accident year is still fifth of five, and the reserve
cycle named at Q4 is about the **level** of reserves, not about release games.

## THE PRICE — SUM OF THE PARTS, ROUND NUMBERS **[E4-01]**

| | basis | low $M | high $M |
|---|---|---|---|
| **CNA, 91.8%** | **market**: 270,600,928 sh × $48.585 = $13,148M | **12,070** | **12,070** |
| **Boardwalk** | 8×–12× EBITDA $1,174M, less $3,782M debt | 5,610 | 10,306 |
| **Loews Hotels** | $52M pre-tax + $102M JV income; $2,487M assets, $1,001M debt | 1,000 | 1,800 |
| **Parent** | $3,900M cash and investments **less $1,786M parent debt** | 2,114 | 2,114 |
| Altium (~53%, equity method, **loses $28M/yr**) | | 0 | 300 |
| **TOTAL** | | **20,794** | **26,590** |
| **PER SHARE** (204,427,720) | | **$101.72** | **$130.07** |

> ### **PRICE: $109.475** (2026-09-02, aggregator, flagged)
> ### **VALUE, ROUND NUMBERS: ~$100 to ~$130 per share**
> ### Market capitalisation **$22,380M** · book value per share **$90.71** · **1.21× book**

**Bar 2, the screamer test [E4-01]:** the price sits **inside** the range. Three outcomes, and
this is the middle one: **no useful conclusion — move on.** No margin is added on top;
"startlingly low" is what you observe, and it is not observed here.

**THE FLOOR, BEFORE ANY RANKING [E4-28].** Honest pre-tax expectancy at $109.475:

| earnings base | $M | per share | yield |
|---|---|---|---|
| FY2025 net income (best recent year) | 1,667 | $8.15 | **7.45%** |
| five-year mean (2021–25) | 1,380 | $6.75 | **6.17%** |
| ten-year mean (2016–25, incl. the 2020 loss) | 935 | $4.58 | **4.18%** |

**Every construction is below the ~10% figure the corpus quits on.** *"that's the figure we
quit on … that's true whether short rates are 6 percent or whether short rates are 1
percent."* **Loews is not ranked. It is quit on.** Against the **5.27%** sovereign the
five-year mean pays **+0.90 points** and the ten-year mean pays **−1.09 points**.

**Windage count: ONE.** Conservatism is spent once **[E4-11]** — at the low end of the
Boardwalk multiple. Realistic inputs everywhere else: CNA at its own market quote, the parent
at its stated net cash less its own debt, the hotels at roughly book.

**What bounds the upside [E2-63].** Loews' ten-year mean return on equity is **5.45%**, and
*"average ROE barely moves."* The upside is bounded by the repurchase — which requires the
discount to persist, and the discount is closing (0.63× book in 2020, **1.09–1.15× in Q4
2025**). A holding company that compounds by buying itself cheaply stops compounding when it
is no longer cheap.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND? *(DID NOT OPEN — Q2 returned OUT)*

**This gate did not open and no verdict is written in it.** The arithmetic that would have
gone here is in the **COMPUTATION — NOT A CLEARANCE** section above, where it carries no
entry language. For the reader's convenience, the three reportables restated:

**1. THE YIELD.** Not computable in the form the template asks for, and the reason is the
finding: **77.0% of the screen's owner-earnings numerator is float growth [E2-61]**, and the
remaining earnings are the return on a portfolio that component 1 already counts **[E5-48]**.
Trailing earnings yields: **7.45%** on FY2025, **6.17%** on the five-year mean, **4.18%** on
the ten-year mean, against a **5.27%** sovereign.

**2. WHAT THE PRICE ALREADY ASSUMES.** At $109.475 against a $101.72–$130.07 sum of the
parts, the price assumes Boardwalk is worth roughly **10× EBITDA** and that the repurchase
continues to add per-share value. Against what the business has actually done: **ten-year mean
ROE 5.45%**, total market capitalisation **+40% in sixteen years**, and **[E3-54] retention
failing eleven of twelve five-year windows**.

**3. WHAT YOU ARE PAID.** **+0.90 points** over the sovereign on the five-year mean;
**−1.09 points** on the ten-year mean. **Below the [E4-28] floor on every construction —
not ranked, quit on.**

**THE CERTAINTY SPREAD.** None applied. **[E3-42]** forbids a per-name risk premium in the
rate — *"mathematical gibberish"* — and certainty is priced once, at the understanding gate
and in the end discount.

**THE VALUE, ROUND NUMBERS [E4-01]:** conservative **~$100** · optimistic **~$130** ·
**current price $109.475** — *inside the range, which under Bar 2 is the middle outcome and
a finished answer: no useful conclusion.*

**- VERDICT: GATE DID NOT OPEN. No ranking position is assigned.**

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [ ] **Normal method [E4-11]** — realistic inputs, one margin at the end.
      Margin used ____ %, and which corpus illustration it sits nearest:
      bridge ~35% **[E3-25]** · Grand Canyon 60%, the stated ceiling **[E3-26]** ·
      "closer to a dollar on the dollar" for a business you understand **[E4-12]** ·
      "dollar bills for 80 cents" **[E5-09]**
- [ ] **Screamer test [E4-01]** — does the price already clear the **conservative** case?
      No margin is added on top. Three outcomes: below the conservative case → act ·
      **inside the range → no useful conclusion, move on** · above the whole range → no.
- **Windage count: ONE** — the low end of the Boardwalk EBITDA multiple. Every other input is
  realistic **[E4-11]**.

- **VERDICT: GATE DID NOT OPEN. No ranking position.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL? *(DID NOT OPEN)*

Q6 governs a position, and there is none. **What would prove the Q2 OUT wrong is worth
pre-registering anyway, because a permanent OUT deserves a stated refutation [E4-51]:**

- **The Q2 verdict is wrong if CNA's combined ratio closes the gap to AIG/HIG/TRV rather than
  widening it.** Threshold: **CNA's P&C combined ratio at or below 92.0% (the AIG five-year
  mean) for two consecutive years**, with Specialty rate back above +6%.
- **It is wrong if Boardwalk becomes the majority of Loews' earnings at a return that clears
  [E5-40]'s 12%.** Threshold: **Boardwalk's return on unleveraged net tangible operating
  assets above 10%**, with the $3.3bn growth programme actually built and the $9.9bn
  contingent backlog converted.
- **Next catalysts:** Q3 2026 10-Q (early November 2026), which carries the **third-quarter
  annual long-term-care reserve review**; and the FY2026 10-K in February 2027, which carries
  the next reserve-development table.

**The [E4-17] monitoring question, answered for the record:** the erosion at CNA is **not
aberrational cycle**. Rate falling from +11% to 0% in Specialty and to −4% in International,
across four years, while every peer improved its combined ratio by 4.6–5.7 points, is a
relative-position change, not a weather event.

- **VERDICT: DID NOT OPEN.**

---
## SELF-AUDIT
- [x] Questions answered in order; **stopped at the first non-IN verdict.** Q3 and Q4 were
      worked and are explicitly labelled **recorded evidence, not gates**
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is IN on
      four read filings. Q3's and Q4's recorded findings are not gate verdicts
- [x] No UNRESEARCHED verdict was written — nothing needed was unobtainable
- [x] No UNKNOWABLE verdict was written
- [x] Step 0: four filings read with accession numbers; **total investments $55,376M
      cross-checked against the filed balance sheet** and re-derived from its five components
- [x] Owner earnings: **not computed as a single number, per the sector method**, with the
      reason stated and the screen's number reproduced to the dollar and corrected in named
      steps. Window stated (FY2021–FY2025). **(c) built per business**, Boardwalk's read
      directly from the filer
- [x] **Competitor row filled twice** — CNA vs four P&C peers, Boardwalk vs four midstream
      peers. Not PROVISIONAL
- [x] Sovereign **5.27%**, USD, **US Treasury daily par yield curve (issuing authority)**,
      dated **2026-09-01**
- [x] Value stated as a round-number range: **~$100 to ~$130**
- [x] **Bar 2 (screamer) chosen, not both.** Windage count: **one**
- [x] Prices dated 2026-09-02; **aggregator flagged** for both L and CNA quotes
- [x] Run committed to git after every question

### THE PLACES THIS RUN COULD BE WRONG — hunted per [E4-26], listed against my own conclusion
1. **The accident-year decomposition acquits CNA** (93.8 / 95.2 / 94.2). CNA is not gaming
   reserves, and the instrument that closed MKL says so.
2. **The [E4-55] physical series acquits Boardwalk.** Real operating income +15.8% on real
   capital −9.3%; returns rising three years running.
3. **The buyback record is the best this project has found**: 52.7% of the company retired at
   **0.805× book** over seventeen years, below book in **every** year.
4. **[E2-49] metric-switching does not fire**, and the pay metrics are identical across years
   by the filer's own statement.
5. **The peer row I am most confident in is the one I computed myself.** CNA and HIG do not
   publish a consolidated combined ratio; both rows are weighted from segments. The CNA figure
   was cross-checked two independent ways agreeing to 0.05 points; **HIG carries a stated
   ~0.1-point imprecision.** Neither moves a ranking, but the row is not all read-directly.
6. **Boardwalk's peer metric has a known bias:** KMI's $20.1bn of goodwill lifts its figure
   from ~6.5% to 9.9%, so the attacker metric rewards whoever wrote off the most purchase
   premium; Williams tags no intangibles and may be understated.
7. **The strongest single fact against the OUT** is stated in the register below.

## REGISTER

- **Verdict: [x] OUT (about the business).** Not UNRESEARCHED — nothing needed was
  unobtainable. Not UNKNOWABLE — the evidence is in and it decides.

- **One line:** *70% of Loews' earnings come from an underwriter that is fifth of five on
  combined ratio in three of five years, last on the five-year mean, and last on return on
  equity in every year of the window against its comparable peers — whose Specialty rate went
  **+11% → 0%** and whose International rate is now **−4%** — while the one business with a
  genuinely irreplaceable asset is 27% of earnings, earns **7.6%** on unleveraged tangible
  capital (last of five in its own row), and has its rates set by the FERC's cost-of-service
  process.*

- **PRICE: $109.475** (2026-09-02, aggregator, flagged) · market capitalisation **$22,380M**
  on **204,427,720** shares hand-read off the 10-Q cover.
- **VALUE, under `COMPUTATION — NOT A CLEARANCE`: ~$100 to ~$130 per share.** The price sits
  **inside** the range, which under Bar 2 is the middle outcome and a finished answer.
- **Honest pre-tax expectancy 4.18%–7.45%, below the [E4-28] floor on every construction.
  Not ranked — quit on.**

### ⛔ **PASS / FAIL: FAIL. The file closed at Q2 (OUT).**
Q1 IN · **Q2 OUT** · Q3, Q4 recorded as evidence but not as gates · Q5, Q6 did not open.

- **THE STRONGEST SINGLE FACT AGAINST THIS VERDICT**, stated because the run is obliged to
  **[E4-51]**: **Boardwalk's rights-of-way and FERC certificates are the closest thing to a
  structurally unrepeatable asset this project has examined** — 14,275 miles of pipe across
  thirteen states that nobody will permit again — and its economics are **improving on every
  measure at once**: return on unleveraged net tangible operating assets 5.83% → 7.21% →
  7.57%, throughput +69.8% in nine years on a 3.7% smaller network, and committed firm
  revenue up **$14.2bn → $19.6bn in a single year**. If Boardwalk's $3.3bn growth programme
  is built and earns above 10%, and if Loews keeps retiring 4% of its shares a year, the Q2
  OUT will look like a verdict passed on the wrong subsidiary. **The reason it is still OUT
  is arithmetic, not judgment: that business is 26.6% of earnings and 12.6% of revenue, and
  [E3-03] criterion 3 fails on the filer's own description of how its rates are set.**

- **A verdict that required no fighting.** Both closing criteria were found in the subject
  companies' own words, not in a construction of mine: CNA's *"highly competitive, both as it
  relates to rate and service"* and Boardwalk's *"established through the FERC's cost-based
  rate-making process."* **[E4-18]** — no degree-of-difficulty credit was taken and none was
  needed.
