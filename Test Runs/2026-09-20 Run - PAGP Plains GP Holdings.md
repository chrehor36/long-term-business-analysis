# Company Run — PLAINS GP HOLDINGS, L.P. (PAGP) — 2026-09-20
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

**Wave 7, name 1.** First name in the operator's three CSV lists, opened 2026-09-20. No prior
work in this tree; no register entry; `grep -c PAGP "Screens/WATCHLIST RUN QUEUE.md"` returned 0.

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

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34 %** · date **2026-09-18** (Friday; today 2026-09-20 is a Saturday) · source
  **U.S. Department of the Treasury, Daily Treasury Par Yield Curve Rates, 30-year, 2026
  series CSV, fetched direct from `home.treasury.gov` — the ISSUING AUTHORITY.** FRED DGS30
  was not used and was not needed.
  *(Adjacent tenors on the same strike, recorded so nobody has to refetch: 10-yr 5.01,
  20-yr 5.38, 5-yr 4.86.)*
- FX: none. PAGP reports and is quoted in USD. The Canadian business was sold on 2026-05-12
  (below); the CAD proceeds are a closed item, not an earnings currency.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Documents read, with accession numbers:**

| document | period / event | filed | accession |
|---|---|---|---|
| 10-K FY2025 | 2025-12-31 | 2026-02-27 | **0001581990-26-000012** |
| 10-Q Q2 2026 | 2026-06-30 | 2026-08-10 | **0001581990-26-000025** |
| 8-K + EX-99.1 (pro forma) | 2026-09-09/14 | 2026-09-14 | **0001104659-26-107550** |
| 8-K + EX-99.1 (Q2 earnings release) | 2026-08-07 | 2026-08-07 | **0001581990-26-000023** |
| 8-K + EX-2.2/2.3/2.4 + EX-99.1 (Canadian NGL close) | 2026-05-12 | 2026-05-12 | **0001104659-26-059512** |
| 8-K (credit agreement) | 2026-02-26 | 2026-03-03 | **0001104659-26-022839** |
| 8-K (new credit agreement) | 2026-06-12 | 2026-06-17 | **0001104659-26-075189** |

- **Figure cross-checked against the filed statement:** `tools/run.py` printed FY2025 operating
  cash of **$2,931M**. The filed Consolidated Statements of Cash Flows in the 10-K
  (0001581990-26-000012) reads *"Net cash provided by operating activities | 2,931"*, built
  from *"Cash provided by operating activities - continuing operations | 2,447"* plus
  *"Cash provided by operating activities - discontinued operations | 484"*. **The tag matches
  the filed line — and the filed line is the WRONG NUMERATOR for this registrant**, for the
  reason set out below and worked at Q4. *A match is not a reading (2026-09-20).*

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### The structure comes first, because the screen priced the wrong entity

**PAGP does not own a pipeline.** From the 10-K, Items 1 and 2, verbatim:

> "PAGP does not directly own any operating assets; as of December 31, 2025, its sole source
> of cash flow is derived from an indirect investment in Plains All American Pipeline, L.P.
> ("PAA"), a publicly traded Delaware limited partnership, through its limited partner
> interest in Plains AAP, L.P. ("AAP")." — 10-K FY2025, 0001581990-26-000012

Three tiers, each stated by the filer:

| tier | what it is | what PAGP owns of it |
|---|---|---|
| **PAGP** | the listed security, Class A shares, Nasdaq | **197,904,124 Class A shares** outstanding at 2026-07-31 (10-Q cover, 0001581990-26-000025) |
| **AAP** (Plains AAP, L.P.) | holds PAA units | PAGP holds ~197.9M AAP Class A units = *"an approximate 85% limited partner interest in AAP"* |
| **PAA** | the operating partnership, separately listed (Nasdaq: PAA) | AAP holds *"approximately 233.0 million PAA common units (approximately 31% of PAA's total outstanding common units and Series A preferred units combined)"* |

So the look-through is **0.85 × 31% ≈ 26%** of PAA's common-and-Series-A equity — and the
10-K states the same fact from the other side, in the noncontrolling-interest note:

> "As of December 31, 2025, noncontrolling interests in our subsidiaries consisted of (i)
> limited partner interests in PAA including a **70% interest in PAA's common units and PAA's
> Series A preferred units combined** and 100% of PAA's Series B preferred units, (ii) an
> approximate 15% limited partner interest in AAP, (iii) a 35% interest in the Permian JV,
> (iv) a 30% interest in Cactus II and (v) a 33% interest in Red River."

**Three independent filed measurements of how much of the consolidated group belongs to the
Class A shareholder**, all from 0001581990-26-000012:

| measure | to PAGP Class A | to noncontrolling interests | PAGP's share |
|---|---|---|---|
| **Net income FY2025** | **$260M** | $1,426M | **15.4%** |
| **Partners' capital 2025-12-31** | **$1,345M** | $12,871M | **9.5%** |
| **Cash distributions paid FY2025** | **$301M** | $1,441M | **17.3%** |

**The screen row this run was dispatched on carried `oe_bottom_m 1318 / oe_top_m 1750` and
`cap_m 5535`.** The numerator is the WHOLE consolidated group — PAA's common and preferred
unitholders, the ~15% AAP minority, and the Permian JV / Cactus II / Red River minorities all
included. The denominator is 197.9M Class A shares, which is one class of the top tier only.
**Prior A of the dispatch brief is CONFIRMED, and it cuts against the name: the screen
overstated the numerator by roughly four times.** It is the per-class denominator error the
DASH / META / PATH / PUBM / BZFD covers taught, inverted — here the cover count is right and
the *numerator* is drawn from a wider entity.

**One drafting artifact, flagged and not smoothed (PRIME RULE 1).** The 8-K of 2026-09-14
(0001104659-26-107550) opens: *"Plains All American Pipeline, L.P. ("PAA" or the "Issuer"), a
**wholly owned subsidiary** of Plains GP Holdings, L.P."* — and the 8-K of 2026-05-12
(0001104659-26-059512) repeats it. **This is wrong on the face of the same documents.** PAA's
common units trade on Nasdaq under "PAA" (named as such in the 2026-05-12 EX-99.1), and the
10-K and 10-Q both say AAP holds ~31% of them. The press release attached to the same 8-K
states it correctly: *"PAGP is a publicly traded entity that owns an indirect, non-economic
controlling general partner interest in PAA and an indirect limited partner interest in PAA."*
**Recorded because a reader relying on the 8-K body alone would compute exactly the error the
screen made.**

### The unit economics, in my own words

**PAGP is a taxed wrapper around about 198 million PAA common units.** The filer maintains it
deliberately and names it:

> "We maintain a one-to-one relationship between our Class A shares and the underlying PAA
> common units in which we have an indirect economic interest through our ownership interest
> in AAP (referred to as 'Economic Parity'), such that the number of our outstanding Class A
> shares equals the number of AAP units we own, which in turn equals the number of PAA common
> units held by AAP attributable to our ownership interest in AAP." — 10-K FY2025

So **one Class A share = one PAA common unit of economics**, minus one thing: PAGP *"has
elected to be taxed as a corporation for United States federal income tax purposes"* (10-K,
first line of Items 1 and 2). A PAA unitholder receives the distribution as a partner; a PAGP
shareholder receives it through a taxpaying entity. PAGP's balance sheet carries a **$1,136M
deferred tax asset** (2025-12-31), which is why current tax at the top tier has been small so
far and why it will not stay small forever.

**Underneath, PAA earns money two ways, and the filer separates them:**
1. **Fee assets.** *"we primarily generate revenue through a combination of tariffs, pipeline
   capacity agreements and other transportation fees"*, plus storage, terminalling and
   throughput fees. 20,405 miles of active crude pipeline and gathering systems, 76 million
   barrels of commercial storage, 9,680 thousand barrels a day of 2025 tariff volume, the
   largest presence in the Permian Basin (9,490 system miles, 7,333 kb/d).
2. **Merchant activities.** PAA buys crude at the lease, moves it on its own or third-party
   assets, and sells it — *"PAA's merchant activities provide it with the opportunity to
   realize incremental margins."* This is why **revenue is $44,262M while purchases and
   related costs are $40,433M**: the gross commodity flow runs through the income statement
   and the economics are what is left of it.

**Scale check, FY2025 (10-K):** revenue $44,262M → operating income $1,428M (3.2% of revenue)
→ net income $1,686M → **$260M attributable to PAGP.** A very large physical throughput
operation with a thin margin on an enormous gross, of which the listed security owns a sixth.

### The scarce input the business controls
**Right-of-way, interconnection and acreage dedication in the Permian Basin.** A gathering
network into producing acreage cannot be assembled by writing a cheque; it is easements,
connections and dedications built over decades, and it terminates at Gulf Coast export
outlets the filer names (Corpus Christi). That is a real scarce input — **and it sits one
tier below the security being priced.**

### Will the fundamentals look broadly the same in ten years?
The physical asset will. The 10-K states its thesis as a belief rather than a fact (*"Our
business is based on the fundamental thesis that hydrocarbons are essential to the security
and advancement of human quality of life"*), which is candid drafting. Permian crude will
still need to reach the Gulf in 2036 on any reasonable view. What is *not* stable is the
merchant leg, whose margin the filer itself says *"may vary depending on market conditions
(such as differentials and certain competitive factors)."*

### Is it simple and stable in character **[E3-31]**?
Three tiers, two segments, *"more than 25 joint ventures and/or joint ownership
arrangements"*, eight named unconsolidated equity investees, three consolidated JV
minorities, two classes of PAA preferred, a $40bn merchant book and a derivative programme.
**It is not simple.** But [E3-31]'s test is whether I can *"realistically define what [I]
don't know"*, and the filer states every layer, quantifies every minority and reconciles the
cash path in words. **[E4-46] is the relevant limit** — *"if we can't make a decision in five
minutes, we can't make it in five months"* — and this took reading, not months: the structure
resolved in one page of the 10-K and one note of the 10-Q.

**VERDICT: [x] IN**
*IN on the business model and the cash path, with the structural correction above recorded as
a finding rather than a caveat: the numerator for this registrant is roughly a sixth of the
consolidated statements, and that is now established from the filing rather than assumed.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The unit of the test is the company, not the industry [E4-08].** PAGP's franchise, if it has
one, is PAA's; PAGP itself is a holding wrapper and owns no asset that could carry a moat.
So Q2 is asked of PAA's crude-oil business and answered from PAA's filings.

### The three clauses of [E3-03], each answered from the filing

**(1) Needed or desired — YES.** Permian crude has to reach a refinery or an export dock, and
20,405 miles of active pipeline, 76 million barrels of commercial storage and 9,680 thousand
barrels a day of 2025 tariff volume are how a material share of it does.

**(2) No close substitute — NO. The filer says so, in its own Item 1 and Item 1A, four times.**

> "Although new pipeline projects represent a source of competition for our business,
> **existing third-party owned pipelines with excess capacity in the vicinity of our
> operations also expose us to significant competition** based on the relatively low
> operating cost associated with moving an incremental barrel of crude oil or NGL through
> such unutilized capacity. … **we continue to experience heightened competition for
> uncommitted barrels and contract renewals, which puts downward pressure on tariffs and
> margins.**" — 10-K FY2025, Item 1, "Competition"

> "In addition, **pipelines may also face competition from other forms of transportation,
> such as truck, rail and barge.**" — same section

> "A significant driver of competition in some of the markets where PAA operates (including,
> for example, the Eagle Ford, **Permian Basin**, and Rockies/Bakken areas) stems from the
> rapid development of new midstream energy infrastructure capacity that was driven by the
> combination of (i) significant increases in oil and gas production and development in the
> applicable production areas, both actual and anticipated, (ii) **relatively low barriers to
> entry** and (iii) generally widespread access to relatively low cost capital. … **many of
> the areas where PAA operates have become overbuilt, resulting in an excess of midstream
> energy infrastructure capacity.**" — 10-K FY2025, Item 1A

> "**other competitors with significant excess capacity and high financial leverage may be
> motivated to reduce transportation rates to levels approaching variable operating costs,
> without regard to whether they are generating an acceptable return on their investment.**
> These competitive risks make it more difficult for PAA to attract new customers and expose
> PAA to increased contract renewal and customer retention risk with respect to its existing
> customers and make recontracting at favorable rates and volumes more challenging,
> including, for example, **with respect to certain of PAA's long-haul Permian pipelines.**"
> — 10-K FY2025, Item 1A

**That last passage is [E2-58] written by the subject.** The corpus's commodity equation is
*"persistent over-capacity without administered prices (or costs) equals poor profitability"*,
with long-term profitability set by *"the ratio of supply-tight to supply-ample years"* and
prosperity breeding the next glut (*"nothing fails like success"*). The filer describes the
glut its industry built, names low barriers to entry as a cause, and says rivals will price to
variable cost. **[E2-58]'s one exception is *"a cost advantage that is both wide and
sustainable … By definition such exceptions are few"* — and the competitor row below shows
PAA has the opposite of one.**

**(3) Not subject to price regulation — NO, for the majority of the profits.** The filer
quantifies it itself:

> "**The majority of our pipeline profits in the United States are based on rates that are
> either grandfathered in part or set by agreement with one or more shippers. These rates
> remain regulated by FERC and are subject to challenge or review and modification by FERC
> under the ICA.** Changes in FERC's methodologies for approving rates could adversely affect
> us." — 10-K FY2025, Item 1, "Interstate Liquids Regulation in the United States"

> "Under certain circumstances, **the FERC could limit PAA's ability to set rates based on its
> costs, or could order PAA to reduce its rates and could require the payment of reparations
> to complaining shippers for up to two years prior to the complaint.**" — 10-K FY2025, Item 1A

The mechanism is live, not theoretical: FERC's index rate for July 2021–June 2026 was issued,
**revised down by approximately 1% effective 1 March 2022**, vacated by the D.C. Circuit in
July 2024, re-issued in September 2024, and is still under petitions for review — and the
filer says *"The final resolution of these petitions could have an adverse effect on our cash
flows."* It also says the next five-year index *"is tied in part to an inflation index and is
not based on our specific costs"*, so it *"could hamper our ability to recover cost
increases."*

**This is [E2-59]'s regime, and here it is a CAP and not a floor.** The corpus is explicit on
which way it runs: regulation *caps* a franchise ([E3-03] criterion 3) and *floors* a
commodity business; **neither creates the class**. PAA has the capping half without the
flooring half.

**Prior C of the dispatch brief is answered with proportions, from the filing: the MAJORITY of
US pipeline profit sits on the regulated side, and the merchant leg sits on the unregulated
side of a commodity market the filer calls overbuilt.**

### The competitor row — required **[E3-28]**

A moat is a claim about *relative* position and cannot be evidenced from one company's
numbers. This industry has many SEC registrants filing the same statements on the same
schedule, so "no peer available" would not have been an honest answer here. **Ten peers taken;
Buffett says eight.** The one peer that could not be put on the same line is **Enbridge**, a
40-F filer reporting IFRS in Canadian dollars — named, with the obstacle named, per the
evidence ladder.

**Metric: operating income ÷ (net property, plant and equipment + equity-method investments +
net finite-lived intangibles).** Chosen because [E3-46] makes the second question about a
business *a number* — *"the best businesses, by definition, are going to be businesses that
earn very high returns on capital employed over time"* — and because margin-on-revenue is
meaningless across this set: PAA, ET and OKE run enormous commodity gross flows through
revenue while MPLX, WES and HESM do not. **Window FY2021–FY2025, five years, the corpus
default [E2-42].** All figures from each filer's own 10-K facts (SEC XBRL, newest vintage),
recomputed by `Test Runs/_research 2026-09-20 PAGP/peers.py`.

| Company | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | **5-yr mean** |
|---|---|---|---|---|---|---|
| **PAGP (consolidated = PAA)** | 4.1% | 6.3% | 6.1% | 4.8% | 6.7% | **5.6%** |
| PAA (same statements, one tier down) | 4.1% | 6.3% | 6.1% | 4.8% | 6.7% | **5.6%** |
| Hess Midstream (HESM) | 22.5% | 24.2% | 24.6% | 26.9% | 29.2% | **25.5%** |
| MPLX | 16.1% | 20.8% | 20.7% | 21.8% | 21.3% | **20.1%** |
| Delek Logistics (DKL) | 22.3% | 13.6% | 15.7% | 12.2% | 8.5% | **14.5%** |
| Western Midstream (WES) | 12.8% | 15.6% | 12.3% | 18.1% | 12.7% | **14.3%** |
| Enterprise Products (EPD) | 13.5% | 14.3% | 14.0% | 13.8% | 13.1% | **13.7%** |
| Targa Resources (TRGP) | 6.5% | 10.1% | 14.3% | 13.3% | 14.8% | **11.8%** |
| ONEOK (OKE) | 12.8% | 13.4% | 11.3% | 9.7% | 10.7% | **11.6%** |
| Energy Transfer (ET) | 10.1% | 9.0% | 9.1% | 9.0% | 8.2% | **9.1%** |
| Kinder Morgan (KMI) | 6.5% | 9.0% | 9.0% | 9.2% | 9.7% | **8.7%** |
| Genesis Energy (GEL) | 1.7% | 7.0% | 4.2% | 4.4% | 6.9% | **4.8%** |

- **Peers named: 10**, plus Enbridge named and excluded on currency and accounting basis.
- **PAA is tenth of eleven.** Its five-year mean return on deployed capital is **5.6%** against
  a peer mean of **13.4%** and a peer median of **13.7%**. **Its best year, 6.7%, is below
  every peer's five-year mean except Genesis Energy's.**
- **Limits of the row, stated.** EPD and ET tag no undimensioned `EquityMethodInvestments`, so
  their denominators are understated and their returns are **flattered** — correcting them
  moves EPD to roughly 12.9% and ET to roughly 8.8%, which does not touch the conclusion.
  PAGP's FY2024–25 numerators are continuing operations only (the Canadian NGL Business is in
  discontinued operations from the FY2025 10-K) and its FY2024 denominator falls because those
  assets moved to "assets of discontinued operations"; numerator and denominator move
  together, so the ratio stays comparable. **And the row's own limit [E3-61]:** identical
  structures produce opposite conduct — the row shows position, never behaviour.
- **A tooling defect found while building it, recorded (operator rule 8): PAGP and PAA stopped
  tagging `PropertyPlantAndEquipmentNet` after FY2020** and report under
  `PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization`
  from FY2021. Any screen reading only the first tag returns **nothing** for this filer from
  2021 onward and would silently drop it from a capital-return comparison rather than refuse.

### The other Q2 tests

- **[E2-44], the two-characteristic test.** *Can it raise prices when product demand is flat
  and capacity is not fully utilized?* **No** — and the filing gives the answer as a negative
  variance: FY2025 Crude Oil Segment Adjusted EBITDA rose *"partially offset by … (vi) **the
  impact from certain Permian long-haul contract rates resetting to market in 2025**."* The
  rate reset **downward**, on renewal, in the filer's best basin. *Can it grow dollar volume
  with only minor additional investment of capital?* **No** — FY2025 spent **$2,651M on
  acquisitions plus $643M of capex** while Crude Oil Segment Adjusted EBITDA rose **$68M
  (3%)**. The EPIC / Cactus III purchases closed in October and November 2025, so one year
  understates their contribution; the direction is capital-hungry on any reading.
- **[E3-33] untapped pricing power, and [E4-37]'s inverse metric.** There is none, and the
  inverse fires. The corpus: *"you can almost measure the strength of a business over time by
  the agony they go through in determining whether a price increase can be sustained."* PAA is
  past agony-pricing — its long-haul Permian rates are **set for it, downward, by the market at
  renewal**, and the regulated majority is indexed by FERC to a formula *"not based on our
  specific costs."*
- **[E4-55], where units exist monitor units.** The physical series is the healthy one: total
  tariff volumes **8,934 → 9,680 thousand barrels a day (+8%)**, Permian **6,731 → 7,333
  (+9%)**. Volume up, rate down, return on capital 5.6%. **That is the signature of a
  pass-through, not of a franchise** — the barrels grew and the gain went to the shipper.
  (Precision Steel's lesson [E4-55] read in reverse: there the units fell while price held; here
  the units rise while price falls. Either way the dollar line is the dishonest one.)
- **[E2-53], the dominance class.** Not claimed and not present. The filer describes an
  overbuilt market with low barriers to entry, in which position does not set the economics.
- **[E2-45], the attacker's test.** With ample capital and skilled personnel I would not need
  to attack: the filer states the attack has already happened and is structural — *"relatively
  low barriers to entry"*, *"many of the areas where PAA operates have become overbuilt"*.
- **[E4-04].** Not reached and not needed: the file fails [E3-03] on clauses (2) and (3) before
  durability is in question. Recorded so that no reader infers a perimeter close — **this is
  OUT on the business, not the [E4-04] competence limit ruled on 2026-09-20.**
- **[E4-23], key-person dependence.** None found; the moat defect here is the absence of a
  moat, not a surgeon.

### One price fact, recorded here because it is about the security and not about value

> **COMPUTATION — NOT A CLEARANCE** (operator rule 3)

PAGP closed at **$27.67** and PAA at **$25.37**, both 2026-09-18, both from an aggregator and
flagged as live-quote-only. By the filer's own **Economic Parity** rule one Class A share
carries the economics of one PAA common unit — so **PAGP trades at a 9.1% premium to the
identical claim one tier down**, while being the only one of the two that *"has elected to be
taxed as a corporation for United States federal income tax purposes."* Recorded as a fact
about the two securities. It carries no entry language, and no Q5 output is reported.

### Class and verdict

- Needed or desired [x] · no close substitute [ ] · not price-regulated [ ]
- Class: **[x] NONE** · Direction: **narrowing** — rates resetting to market on renewal in the
  core basin, a FERC index the filer says *"could hamper our ability to recover cost
  increases"*, and a five-year return on capital of 5.6% against a peer median of 13.7%.

**VERDICT: [x] OUT**

**Asked aloud, per [E4-19]: can I name the document that would resolve this?** There is nothing
left to fetch. The 10-K says overbuilt, low barriers to entry, competitors pricing to variable
cost, long-haul rates resetting to market, and *"the majority of our pipeline profits"*
regulated by FERC; eleven filers' own statements say PAA earns 5.6% on deployed capital where
the industry median earns 13.7%. **The evidence is here and the business fails the franchise
test — OUT, permanent. Not UNRESEARCHED, not UNKNOWABLE.**

⛔ **THE FILE CLOSES AT Q2.** Q3, Q4, Q5 and Q6 are **not run** and **no verdict is recorded**
for them. What follows is recorded beneath the close because the dispatch brief put specific
questions to the evidence and the answers are owed to the fold. **None of it is a verdict and
none of it may be read as one.**

---
## RECORDED BENEATH THE CLOSE — the dispatch brief's questions, answered from the documents
**None of the following is a verdict.** Q3, Q4, Q5 and Q6 were not run and are not scored.
These are the answers the fold is owed, each with the filing behind it.

### Prior B — the working-capital flag. **REFUTED as a finding; TRUE as arithmetic.**
The screen's `wc_note` read: *"ONE LINE MADE THE CASH: AccountsPayableAndAccruedLiabilities
moved 99% of 2021 OCF."* **The single line did move 99%. It did not make the cash.** Built
from PAGP's own 10-K cash-flow detail lines (SEC XBRL, newest vintage, cross-checked against
the FY2025 filed statement, where the three lines read 207 / 96 / (337) and net to −34):

| FY | operating cash | receivables | payables & accrued | inventory | **net working-capital cash** | **OCF before working capital** |
|---|---|---|---|---|---|---|
| 2019 | 2,500 | −1,158 | +1,151 | −5 | **−12** | 2,512 |
| 2020 | 1,510 | +1,432 | −1,286 | −304 | **−158** | 1,668 |
| **2021** | **1,991** | **−2,179** | **+1,970** | −18 | **−227** | **2,218** |
| 2022 | 2,404 | +649 | −830 | −10 | **−191** | 2,595 |
| 2023 | 2,722 | +79 | −141 | +102 | **+40** | 2,682 |
| 2024 | 2,484 | +94 | −77 | +120 | **+137** | 2,347 |
| 2025 | 2,931 | +207 | −337 | +96 | **−34** | 2,965 |

**In 2021 payables released $1,970M of cash and receivables absorbed $2,179M of it. Net
working capital was a $227M DRAIN, not a source.** Both lines are the same thing seen twice:
PAA buys and sells roughly $40bn of physical crude a year, so both the payable and the
receivable scale with the crude price, and 2021 is simply the year WTI recovered from the 2020
collapse. **Operating cash before working capital is the stable series — $2.2bn to $3.0bn
across five years with no step.**

**The tooling defect this exposes (operator rule 8).** `working_capital_flag()` measures **one
line in isolation and does not net its matched counter-line.** On any commodity merchant it
will fire in every year the commodity price moved, and it will **name the wrong cause** — here
it named the year the cash was *drained* as the year the cash was *made*. This is the
tail-triage lesson of 2026-09-12 in a new place: the arithmetic was right and the description
of what it meant was wrong. **Proposed fix, not made here: where a filer tags both
`IncreaseDecreaseInAccountsAndOtherReceivables` and
`IncreaseDecreaseInAccountsPayableAndAccruedLiabilities`, the flag should report the NET
working-capital cash effect beside the single line, and refuse the "one line made the cash"
string when the counter-line offsets more than half of it.** The two tags carry **opposite
cash-sign conventions** in the standard taxonomy (an increase in receivables is a use; an
increase in payables is a source), which is the likely reason they were never netted.

### Prior E — the latest 8-K EX-99.1. **CONFIRMED, at full strength.**
Q2 2026 earnings release, 8-K **0001581990-26-000023**, furnished 2026-08-07. **"Adjusted
EBITDA" appears 43 times** in the release and 45 times in the 10-K. The second headline bullet
is *"Delivered strong second-quarter **Adjusted EBITDA attributable to PAA of $738 million**"*;
the non-GAAP table leads with Adjusted EBITDA, Adjusted net income, **"Implied DCF per common
unit"** and **"Adjusted Free Cash Flow"**. Depreciation and amortization was **$953M in FY2025
against $1,428M of operating income** — so the excluded charge is two-thirds the size of the
profit. [E4-29] is not a stray usage here; **the metric is constitutional**:
- the filer's own **targeted credit profile** is written in it — *"a leverage multiple
  averaging between 3.25x to 3.75x, which is calculated as total debt plus 50% of the value of
  preferred units, divided by **Adjusted EBITDA attributable to PAA**"* (10-K FY2025);
- the **bank covenant** is written in it — the Revolving Credit Agreement of 2026-06-12 (8-K
  **0001104659-26-075189**) *"limits Consolidated Funded Indebtedness to adjusted Consolidated
  EBITDA to no greater than 5.00 to 1.00, which increases to 5.50 to 1.00 during an
  Acquisition Period"*;
- and the release headlines *"Adjusted Free Cash Flow"* of **$4,189M for Q2 2026** against
  $348M a year earlier — a figure that is mostly the **$3.9bn of divestiture proceeds**.
**[E2-54] is the corpus's answer to an EBITDA covenant**: *"whenever someone creates a capital
structure that does not allow all interest, both payable and accrued, to be comfortably met out
of current cash flow net of ample capital expenditures — zip up your wallet"* — accrued
interest counts, cash flow is the source, and capex comes out first. Recorded, not scored.

### Prior F — the perimeter. **The screen's `deal_note` was WRONG, and three later events matter.**
`deal_note` read: *"2 8-K Item 1.01 filing(s) since 2026-02-27, none carrying a merger
agreement (EX-2.1) — most likely a credit facility or offering."* Opened, all of them:

| date | accession | what it actually is |
|---|---|---|
| 2026-03-03 | 0001104659-26-022839 | Third Amendments to the revolver and hedged-inventory facilities. Credit facility — the note's guess was right here. |
| **2026-05-12** | **0001104659-26-059512** | **Item 2.01 — COMPLETED SALE of the Canadian NGL business to Keyera for approximately CAD $5.328bn (~USD $3.883bn), ~$3.3bn net. Exhibits EX-2.2, EX-2.3 and EX-2.4 are the three amendments to the Share Purchase Agreement.** |
| 2026-06-17 | 0001104659-26-075189 | New Revolving Credit Agreement; the old revolver and the hedged-inventory facility repaid and terminated. |
| **2026-08-07** | **0001581990-26-000023** | Q2 2026 earnings release (Item 2.01 **and** 7.01 — the release is tagged 2.01). |
| **2026-09-14** | **0001104659-26-107550** | **$700M of 6.750% Series A and $800M of 7.000% Series B Junior Subordinated Notes due 2056, issued five days ago**, plus an Item 8.01 pro forma for the EPIC Crude purchases. |

**The defect in the screen inference, precisely: it searched for `EX-2.1` and this deal's
agreement exhibits are `EX-2.2` through `EX-2.4`, because the original SPA of 2025-06-17 was
filed as EX-2.1 to the Q2 2025 10-Q and only the amendments were attached to the closing 8-K.**
A deal-perimeter test keyed to one exhibit number misses every transaction whose agreement was
filed earlier and amended at closing. **This is the MRVL lesson repeating: `newest_filing
2025-12-31` while a $3.9bn divestiture, a $2.65bn acquisition and $1.5bn of new hybrid debt sat
in later filings.**

**Three perimeter events the FY2025 statements do not carry:**
1. **The Canadian NGL business is gone** (closed 2026-05-12). It is already in discontinued
   operations in the FY2025 10-K, so the continuing-operations series is the right one — but
   the FY2025 *cash-flow statement* still includes *"Cash provided by operating activities -
   discontinued operations | 484"*, i.e. **$484M of the $2,931M operating cash belongs to a
   business that no longer exists.**
2. **EPIC Crude Holdings / Cactus III was bought in two steps** (55% on 2025-10-01, the
   remaining 45% effective 2025-11-01), which is most of the **$2,651M** of FY2025 acquisition
   cash. The company's **own pro forma** (8-K 0001104659-26-107550, Item 8.01), presenting
   FY2025 as if both steps had closed on 1 January 2025, shows net income from continuing
   operations attributable to Class A shareholders falling from **$152M to $135M**, and per
   Class A share from **$0.77 to $0.68** — *the acquisition is dilutive to the Class A
   shareholder on the company's own arithmetic.* Recorded as a fact; **Q3 was not run and no
   capital-allocation verdict is written.**
3. **$1.5bn of junior subordinated notes at 6.750% and 7.000%, due 2056, issued 2026-09-14** —
   six days before this run and after the newest periodic filing. Hybrid debt priced at 6.75–7.00%
   against a 30-year Treasury of 5.34% on 2026-09-18.

### The survival shape the evidence points to — recorded, NOT a Q4 finding
Q4 was not reached, so **no shape is named as this business's death.** What the Q2 evidence
shows is the signature of **#11 THE PASS-THROUGH** (TM, 2026-09-13: the company survives but
the gains go to customers and suppliers): tariff volumes **+8%** (8,934 → 9,680 kb/d) and
Permian **+9%**, while long-haul Permian contract rates **reset to market downward** and the
five-year return on deployed capital sits at **5.6%** against a peer median of **13.7%**. The
barrels grew; the money went to the shipper. **[E3-62]'s second step answers itself here** —
*"how much is going to stay home and how much is just going to flow through to the customer"* —
and the filer's own risk factor names the reason: *"relatively low barriers to entry"* and
competitors who *"may be motivated to reduce transportation rates to levels approaching
variable operating costs."* Shapes **#5 THE SELF-LIQUIDATING DISTRIBUTION**, **#6 THE BORROWED
BALANCE SHEET** and **#28's normalisation instruction** were carried into this run as
candidates and are **untested**, because the file closed two gates before Q4.

### What I could not resolve, and the document that would resolve it
- **PAGP's own entity-level cash tax path.** PAGP carries a **$1,136M deferred tax asset**
  (2025-12-31) and pays corporate tax on income a PAA unitholder receives untaxed at the
  entity. How fast that asset is consumed, and therefore what fraction of the PAA distribution
  actually reaches a Class A shareholder over the next decade, is **not computable from the
  documents read**. *The document that would resolve it: Note 15 (Income Taxes) of the FY2025
  10-K read against the deferred-tax rollforward, plus the Section 754 / basis discussion in
  the Class A share tax summary.* **Not fetched, because the file closed at Q2 and no
  valuation was owed.**
- **The split of PAA's Crude Oil Segment Adjusted EBITDA between fee-based and merchant
  margin.** The 10-K describes both and does not disaggregate them. *The document that would
  resolve it: PAA's own investor-day materials or a supplemental disclosure; it is not in the
  10-K, the 10-Q or any 8-K read here.* Recorded as a real gap; it does not change Q2, because
  both legs fail [E3-03] — the fee leg on clause (3) and the merchant leg on clause (2).

---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN, Q2 OUT, and the run stopped
      there. Q3–Q6 carry no verdict and no checkbox is ticked for them.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests
      on the 10-K and the 10-Q, both read, both cited by accession.
- [x] **Every UNRESEARCHED verdict names the artifact and where it lives.** None was issued.
      The two unresolved items above are recorded *beneath the close*, with their documents
      named, and neither is a gate verdict.
- [x] **Every UNKNOWABLE verdict states what specifically cannot be known.** None was issued.
      Q2 is OUT, not UNKNOWABLE: the resolving documents exist and were read, and they say the
      business fails.
- [x] **Step 0: the filing was read, with accession number; a figure was cross-checked.** Seven
      documents listed with accession numbers. FY2025 operating cash of $2,931M checked against
      the filed Consolidated Statements of Cash Flows, including its two component lines.
- [n/a] **Owner earnings on a multi-year mean; window stated; capex band disclosed.** Q4 was
      not reached. **No owner-earnings figure is reported for this name**, and the screen's
      $1,318–1,750M is refuted at Q1 as the wrong entity's number rather than replaced by
      one of mine.
- [x] **Competitor row filled, or the moat marked PROVISIONAL and UNRESEARCHED.** Filled: ten
      peers, five years, one metric, every figure from the peer's own 10-K facts. Enbridge
      named as the excluded eleventh with its obstacle stated. The moat is **NONE**, not
      PROVISIONAL.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.** USD 5.34%,
      2026-09-18, US Treasury daily par yield curve, struck this session. Nothing inherited.
- [n/a] **Value stated as a round-number range.** No value is stated. Q5 did not open.
- [n/a] **One bar chosen, not both; windage count stated.** No bar was used; no margin of
      safety was applied to anything, because nothing was valued.
- [x] **Prices dated; aggregator used for live quotes only and flagged.** PAGP $27.67 and PAA
      $25.37, both 2026-09-18, both flagged as aggregator quotes, used only for the
      security-premium fact and the cap, never for a verdict.
- [x] **Run committed to git.** Q1+Q2 at `e8a5733`; this tail and the fold in the commit named
      in the register entry.

**Two audit items tested rather than ticked**, per the 2026-09-20 finding that a match is not a
reading:
- **The SBC-of-zero check (RESUME STATE 3F).** `run.py` resolved stock compensation for all
  three years (51 / 52 / 50). Verified against the filed cash-flow statement, which reads
  *"Equity-indexed compensation expense | 50 | 52 | 51"* for 2025 / 2024 / 2023. **No silent
  zero. `ShareBasedCompensation` is not the tag this filer uses**, and the resolution came
  through another element — recorded so the next reader does not re-test it.
- **The ledger-id check.** Every id cited above was read out of `principle_ledger.csv` before
  use. **The file carries 311 data rows and 311 unique ids, not the 267 the dispatch brief and
  `CLAUDE.md` both state** — confirmed by `tools/check_framework.py`, which printed
  *"LEDGER 311 rows, 311 unique ids"* and PASSED on 2026-09-20. **And a trap inside my own
  first count, recorded because it is the kind that looks right:** reading the file with
  `csv.reader(open(path, encoding='utf-8'))` returns **286**, because without `newline=''`
  Python translates the `
` inside quoted multi-line quote fields and the reader splits
  rows that are one row. **`newline=''` is required**, which is exactly what
  `check_framework.load_ledger()` does. A count taken the easy way is 25 rows short and gives
  no error.

---
## REGISTER
- Verdict: **[x] OUT (about the business)**
- One line: **PAGP is a corporate-taxed wrapper on ~198 million PAA common units — about a
  sixth of the consolidated statements the screen priced — and the crude-oil business
  underneath fails [E3-03] on two of three clauses in the filer's own words: an overbuilt
  market with "relatively low barriers to entry" where rivals will "reduce transportation rates
  to levels approaching variable operating costs", and a "majority of our pipeline profits"
  that "remain regulated by FERC". Ten peers on the same metric, same five years, from their own
  filings: PAA earns 5.6% on deployed capital against a peer median of 13.7%, tenth of eleven.**
- Not UNRESEARCHED and not UNKNOWABLE: every document that could resolve the franchise question
  was read, and each of them answers it the same way.
