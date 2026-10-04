# Company Run — PHOTRONICS, INC. (PLAB) — 2026-09-01
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**RESULT IN ONE LINE: the file closes at Q2. Photronics is not a franchise, and its own
10-K is the document that says so.** The price is reported below under operator rule 3 as
**COMPUTATION — NOT A CLEARANCE**.

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- **rate 5.27%** · **date 2026-09-01** · source: **U.S. Department of the Treasury, Daily
  Treasury Par Yield Curve Rates, 30-year, published by the issuing authority at
  `home.treasury.gov`**.
- **DEVIATION DECLARED.** `CLAUDE.md` names FRED DGS30 as the USD source. FRED refused
  connection on five attempts across this session (`Remote end closed connection`). The
  Treasury's own daily par-yield file was used instead. Operator rule 5 requires the
  sovereign *"from the issuing authority"*; the U.S. Treasury **is** the issuing authority
  and FRED is a Federal Reserve redistribution of it, so this substitution moves **up** the
  evidence ladder, not down. Treasury 30-year: 5.27% (2026-09-01), 5.25% (2026-08-31),
  5.18% (2026-08-26 — the rate the screen used).
- Earnings currency: the reporting currency is USD, but **82% of FY2025 revenue was earned
  outside the United States** (10-K Item 1, *"Revenues from our non-U.S. operations were
  approximately 82%, 83% and 86% of our total revenues in 2025, 2024 and 2023"*). The USD
  sovereign is retained because the filer reports and the shareholder is paid in USD; the
  FX exposure is recorded at Q4 rather than by switching the yardstick.
- FX / ADR ratio: **not applicable** — PLAB is a domestic filer with ordinary shares on
  Nasdaq.

**The filing was read** — not tagged data **[E3-27]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines and the supplemental non-cash block
  [x] footnotes (Notes 1, 5, 6, 8, 10, 19, and the related-party note)
- **document · date · accession no.: Form 10-K for the fiscal year ended 2025-10-31 ·
  filed 2025-12-11 (EDGAR index date 2025-12-17) · accession
  0001140361-25-045801 · primary document `ef20057458_10k.htm`.**
- Also read: **Form 10-Q for the quarter ended 2026-05-03, filed 2026-06-11, accession
  0001140361-26-024915** — the most recent periodic filing in existence. No Q3 FY2026 10-Q
  had been filed as of this run.
- **Figure cross-checked against the filed statement:** *Purchases of property, plant and
  equipment* in the Consolidated Statements of Cash Flows reads **$(188,137) thousand** for
  FY2025, **$(130,942)** FY2024, **$(131,295)** FY2023. SEC companyfacts
  `PaymentsToAcquirePropertyPlantAndEquipment` returns 188.1 / 130.9 / 131.3 ($M). **They
  agree.** Second cross-check: filed *Net cash provided by operating activities* **$247,798
  thousand** FY2025 against companyfacts 247.8. Agree.

---
# STAGE 0 — ARTIFACT CHECK, AND WHAT THE SCREEN GOT WRONG

**The screen's nine-year owner-earnings series was recomputed line by line against the
filed cash-flow statements of the FY2017–FY2025 10-Ks.** Construction: operating cash flow,
less share-based compensation, less purchases of property, plant and equipment.

| FY | OCF | SBC | capex paid | **filed OE** | **screen** |
|---|---|---|---|---|---|
| 2017 | 96.8 | 3.6 | 92.0 | **1.2** | 1 |
| 2018 | 130.6 | 3.2 | 92.6 | **34.8** | 35 |
| 2019 | 68.4 | 3.7 | 178.4 | **−113.7** | −114 |
| 2020 | 143.0 | 4.9 | 70.8 | **67.3** | 67 |
| 2021 | 150.8 | 5.3 | 109.1 | **+36.4** | **−6 ← does not reconcile** |
| 2022 | 275.2 | 6.3 | 112.3 | **156.6** | 157 |
| 2023 | 302.2 | 8.0 | 131.3 | **162.9** | 163 |
| 2024 | 261.4 | 13.9 | 130.9 | **116.6** | 117 |
| 2025 | 247.8 | 13.4 | 188.1 | **46.3** | 46 |

**Eight of the nine years reconcile to the dollar. FY2021 does not.** The FY2021 10-K
(accession 0001140361-21-042251) reports capital expenditure of **$109.1M**, not the
~$151M the screen's "capital acquired" measure implies. The supplemental non-cash line
*Accruals for property, plant and equipment not yet paid* was **$7.8M at FY2021 against
$13.1M at FY2020** — a *decrease* of $5.3M, which moves the figure the wrong way for the
screen. **The filed FY2021 figure is +$36.4M and it is used here.**

**Consequence for the boom test, and it does not rescue the name:**
- earlier-six mean (FY2017–22): screen 23 → **filed 30.4**
- recent-three mean (FY2023–25): screen 109 → **filed 108.6**
- **The [E4-41] BOOM signature survives the correction: 108.6 against 30.4, a 3.6x step.**
  *"normalize the mean DOWN for luck"* **[E4-41]** — favourable exogenous breaks in the
  window are named and removed before the mean is trusted. The break is named at Q2: the
  2021–23 semiconductor shortage.

**The screen's $95M bottom boundary is reproduced and corrected.** It is the five-year mean
(FY2021–25) of the screen's own series, which carried the erroneous −6. **On filed figures
the same five-year construction is $103.8M — and it is still gross of the noncontrolling
interest, which is the correction that decides this file.**

**capex/D&A, filing-sourced:** 1.50x (nine-year), 1.64x (five-year), **1.87x (three-year)**,
**2.42x (FY2025 alone)**, and **4.25x on the company's own FY2026 guidance**. The operator's
1.56x is in the right region and the direction is confirmed: **capex is the conservative end
and D&A is the generous end**, which is the reverse of the [E3-44] default's usual
comfort. This is adjudicated at Q4, not assumed.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, without management's language.**

Photronics runs eleven job shops that make one thing: a flat quartz plate with an opaque
chrome pattern on it. A chip designer finishes a circuit layout; that layout has to be
turned into physical stencils before any wafer can be exposed. Photronics takes the design
file, writes the pattern onto the plate with an electron-beam or laser writer, inspects it,
repairs the defects, and ships it — often inside twenty-four hours. It charges per plate.
A modern chip needs a *set* of these, one per layer, and the set has to be remade whenever
the design changes.

**The revenue driver is design releases, not wafer volume.** This is the single most
important thing to understand about the business and the filing says it outright: *"The
size of the photomask market is driven by the number of designs released to support IC and
FPD product introductions and manufacturing expansions."* A customer that runs a billion
wafers off one mask set buys one mask set. Photronics is therefore levered to **design
activity**, which is the most volatile part of the semiconductor cycle, not to chip
consumption, which is the most stable part.

**The cost structure is depreciation and clean rooms, and it is fixed.** Gross property,
plant and equipment is **$2,489.3M**, of which **$2,109.5M — 84.7% — is machinery and
equipment** (Note 5). Against $849.3M of revenue, this is a business with roughly three
dollars of gross plant per dollar of annual sales. The filing states the consequence:
*"Our employees and our integrated global manufacturing network represent a significant
portion of our fixed operating cost base. Should our revenue decrease as a result of a
decrease in design releases from our customers, we may have excess or underutilized
production capacity, which could significantly impact our operating margins, or result in
write-offs from asset impairments."* Volume falls, margin collapses. That is a job shop.

**The scarce input the business controls.** I looked for one and I do not find a durable
one. The candidates, tested:
- *The writing tools.* Not controlled — they are **bought** from a handful of vendors
  (principally a Japanese e-beam supplier and laser-writer makers) who sell the same tools
  to every competitor. The filing: *"We rely on a limited number of equipment suppliers to
  develop and provide the equipment used in the photomask manufacturing process."*
- *The blanks.* Not controlled, and this is pointed: the quartz substrates are *"primarily
  obtained from Japanese and South Korean suppliers"* — **Hoya, named in the same 10-K as a
  competitor, is one of the principal makers of photomask blanks.** Photronics buys its raw
  material from a company it competes with.
- *Proximity and turnaround.* This is the real one, and it is **local, not global**:
  *"geographic proximity to customers is an important factor in certain markets where cycle
  time from order to delivery is critical."* It is a genuine advantage and it is why
  Photronics has plants in Taiwan, Korea and China. It is also **replicable by anyone
  willing to build a plant next door**, which is exactly what has happened in China.
- *Process know-how.* Real, but the filing itself disclaims that it is differentiating —
  see Q2.

**R&D is 1.9% of revenue** ($15.8M on $849.3M, FY2025). For a business that says it must
*"continually anticipate, respond to, and utilize changing technologies"*, that is a very
small number, and it is the tell that explains everything at Q2: **Photronics does not
develop the technology, it buys it.** The technical progress is embodied in purchased
capital equipment, and the purchase order is open to every competitor.

**Will the fundamentals look broadly the same in ten years?** The *mechanism* — yes.
Optical lithography has required physical masks for fifty years, and the filing's own
enumerated threats (chip-stacking methodologies, programmable devices displacing ASICs,
*"alternative methods of transferring circuit designs onto semiconductor wafers"*) are
carried with the statement that *"there is no indication today that such diminishing of
long range photomask demand is occurring or will occur."* Masks will be needed. **What I
cannot be certain of is Photronics' share and Photronics' price** — and under **[E3-42]**
that is not a Q1 matter. Certainty is handled at the understanding gate and again in the
end discount; the understanding gate asks whether I understand the money-making, and I do.
Share and price are adjudicated at Q2, which is where this file ends.

- **VERDICT: [x] IN**

*Recorded against myself under [E4-26] and operator rule 9: I found this business easy to
understand and that is not a compliment to it. A job shop is easy to understand precisely
because there is not much to it.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The three criteria, taken one at a time.**

> a franchise is a product or service that "(1) is needed or desired; (2) is thought by its
> customers to have **no close substitute** and; (3) is not subject to price regulation."
> — **[E3-03]**

- **(1) Needed or desired — YES.** No wafer is patterned without a mask. This criterion
  passes and it is the only one that does.
- **(2) No close substitute — FAILS, and the subject's own 10-K is the evidence.** Three
  separate filed statements, each fatal on its own:
  - *"The photomask industry is highly competitive, and **most of our customers utilize
    multiple photomask suppliers.**"*
  - *"At these geometries and various high-end nodes, we can produce full lines of
    photomasks, and **there is no significant technology employed by our competitors that
    is not available to us.**"* Photronics writes this as reassurance that it is not
    behind. Read as a franchise test it is an admission: **the technology is symmetric.**
    Nothing is available to Photronics that is not available to the others either, because
    all of them buy the same tools from the same vendors.
  - *"We also compete with semiconductor and FPD manufacturers' **captive photomask
    manufacturing operations**."* **This is the structural point the operator asked to have
    established precisely, and it is the whole of Q2.** Photronics' customers are the
    people who can make the product themselves. A merchant supplier whose buyers own
    working substitutes for its factory has no pricing power that those buyers do not
    choose to grant it.
- **(3) Not subject to price regulation — passes, and it is worth nothing here.**
  **[E2-59]** is exact on why: administered pricing *floors* a commodity business's profits
  and *caps* a franchise's, and *"neither creates the class."* Photronics is unregulated and
  unprotected, which is the worse half of that trade.

**Must the moat be continuously rebuilt? [E4-04]**

**Yes, and this is the excluded class, not the defended one.** The framework's own test:
*"does a lapse in spending destroy the structure, or merely narrow it — and does the
spending defend the same advantage, or buy its replacement?"* Photronics' spending **buys
the replacement**. The company says so: FY2026 capital expenditure of approximately **$330
million** including *"investments to **replace end-of-life mask-making equipment** with
higher-performing systems."* The advantage does not live in an asset that persists; it
lives in a tool fleet that obsoletes and must be re-bought at rising prices. That is
Munger's **competitive destruction**, and what Photronics has had instead of a moat is a
**surfing run [E3-51]** — *"the advantage lives in the wave, not the surfer."*

**Which of the four causes of extreme success is the recent record? [E4-36]** The
2021–2023 result — operating income from $94.6M (FY2021) to $253.1M (FY2023) — is
**wave-riding.** It is the semiconductor shortage. The evidence that it was the wave and
not the surfer is that **the wave receded and the numbers went with it**: operating income
$253.1M → $221.5M → $208.2M, revenue $892.1M → $866.9M → $849.3M.

### The commodity doctrine — [E2-58], and the filing states it in Photronics' own words

> "persistent over-capacity without administered prices (or costs) equals poor
> profitability" … long-term profitability set by "the ratio of supply-tight to
> supply-ample years" … the one exception is "a cost advantage that is both **wide and
> sustainable** … By definition such exceptions are few." — **[E2-58]**

The 10-K, verbatim:

> "**We expect to face continued competition which, in the past, has led to pressure to
> reduce prices. We believe the pressure to reduce prices, together with the significant
> investment required in capital equipment to manufacture high-end photomasks will continue
> in the future.**"

That is a filed, forward-looking statement by management that **prices will keep falling
and capital requirements will keep rising.** Under **[E4-37]**'s inverse metric — *"you can
almost measure the strength of a business over time by the agony they go through in
determining whether a price increase can be sustained"* — Photronics is not merely in the
agony case. It has skipped the prayer session and published the surrender.

**And [E3-62]'s second step is the mechanism.** The corpus's question about capital spending
in a commodity business is *"how much is going to stay home and how much is just going to
flow through to the customer."* Photronics buys a multi-beam e-beam writer; so does
Tekscend; so does the captive shop at a large foundry; so does a Shenzhen entrant. The
tool's productivity gain becomes the industry's cost curve, and the industry's cost curve
becomes the customer's price. The textile-loom lesson applies without modification:
***"Nothing was going to stick to our ribs as owners."*** The $330M is not buying a moat.
It is buying the right to stay in the game at next year's prices.

**Is there a wide and sustainable cost advantage — [E2-58]'s one exception?** No. The
company disclaims technological differentiation in its own filing, and it is not the scale
leader: revenue of $849.3M sits below the photomask revenue of the captive operations of
its largest customers and is not demonstrably above its nearest merchant rivals. **The
exception does not apply.**

### The primary moat metric, filing-sourced, and its trend

**[E3-46]: *"the best businesses, by definition, are going to be businesses that earn very
high returns on capital employed over time"* — asked about the business, before the
manager.** Return on equity attributable to Photronics shareholders, computed from the
filed balance sheets and income statements (net income attributable to Photronics ÷
Photronics shareholders' equity, noncontrolling interests excluded from both):

| FY | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| **ROE** | 6.5% | 1.8% | 5.5% | 3.9% | 4.2% | 6.7% | 14.3% | 12.9% | 11.7% | 11.6% |

- **ten-year mean 7.9%** · **five-year mean 11.4%** · **the peak of the best cycle in the
  company's history was 14.3%**
- **Basis, stated so it is reproducible in under two minutes:** numerator is
  `NetIncomeLoss` (net income attributable to Photronics, after the noncontrolling
  interest); denominator is `StockholdersEquity` (Photronics shareholders' equity, excluding
  the noncontrolling interest), taken at **fiscal year end**. On **average** equity instead,
  the ten-year mean is **8.2%** and the five-year mean **11.9%** — the choice moves the
  figure by three-tenths of a point and moves no verdict. Both are stated rather than the
  more favourable one being selected **[E4-38]**.
- **[E2-42]:** *"Red lights should start flashing if the five-year average annual gain falls
  much below the return on equity earned over the period by American industry in
  aggregate."* 7.9% over ten years is not a high return on capital employed. It is a
  below-average one, earned across a full cycle, with no leverage flattering it (the company
  is debt-free).

**[E4-55] — where units exist, monitor units.** Photronics does not publish mask counts, but
it publishes the next best physical series, revenue disaggregated by product type (Note 10),
and it is the most damaging table in the filing:

| $000 | FY2023 | FY2024 | FY2025 | change |
|---|---|---|---|---|
| IC high-end | 194,939 | 228,469 | **238,865** | **+22.5%** |
| **IC mainstream** | **456,340** | **409,682** | **376,239** | **−17.6%** |
| Total IC | 651,279 | 638,151 | 615,104 | −5.6% |
| FPD high-end | 200,842 | 195,365 | 195,520 | −2.7% |
| FPD mainstream | 39,955 | 33,430 | 38,670 | −3.2% |
| Total FPD | 240,797 | 228,795 | 234,190 | −2.7% |
| **Total revenue** | **892,076** | **866,946** | **849,294** | **−4.8%** |

**IC mainstream is 44.3% of FY2025 revenue and it has fallen 17.6% in two years.** That is
the segment where the product is most nearly identical between suppliers and where the two
Chinese competitors Photronics itself names — **Shenzhen Newway Photomask Making Co., Ltd.**
and **Shenzhen Qingyi Photomask, Ltd.** — are building. High-end grew and did not grow
enough to hold the total.

**[E4-32] — direction outranks existence.** *"the moat widened every year"* is *"the primary
criterion of a great business."* Photronics' direction is **narrowing**: total revenue down
4.8% in two years, the largest segment down 17.6%, gross margin down from 37.7% to 35.3%,
operating margin down from 28.4% to 24.5%, and the capital required to hold position rising
from $131M to a guided $330M. **Every vector points the same way.**

**[E2-44] — the two-characteristic test.** Can it raise prices *"even when product demand is
flat and capacity is not fully utilized"*? The filing answers no, twice: the price-pressure
sentence above, and the underutilisation warning. Can it grow dollar volume *"with only
minor additional investment of capital"*? No — dollar volume **shrank** while capital
investment rose 43% in one year. **Both halves fail.**

**[E2-45] — the attacker's test.** *"how I would like, assuming I had ample capital and
skilled personnel, to compete with it."* I would like it very much, and the filing tells me
how: buy the same tools from the same vendors, build next to a cluster of customers, and
undercut on mainstream nodes where the plates are interchangeable and the buyers already
multi-source. There is no trademark to overcome, no switching cost that survives a
qualification cycle, no scale I cannot buy, and no patent estate the filing claims as a
barrier. **A well-capitalised entrant with a Shenzhen address is doing precisely this now.**

**[E3-33] / [E5-28] — untapped pricing power?** **No, and claiming it here would be
claiming near-monopoly** — *"If you name some business that has incredible pricing power,
you're talking about a business that's a monopoly or a near monopoly"* **[E5-28]**.
Photronics is one of roughly nine named merchant suppliers competing against its own
customers' in-house shops. There is no unexercised price increase sitting on the table; the
filing forecasts the opposite direction.

**[E2-53] — the dominance class.** *"Once dominant, the newspaper itself, not the
marketplace, determines just how good or how bad the paper will be. Good or bad, it will
prosper."* Photronics is not in this class and does not claim to be. The marketplace, not
Photronics, determines how good Photronics will be.

### The merchant-versus-captive structure — established precisely, as instructed

This is the operator's central question and the filing answers it fully. **Photronics' own
account of the market's history is an account of a share that oscillates, driven entirely by
its customers' capital-budget decisions rather than by anything Photronics does:**

> "The production value of photomasks produced by merchant suppliers has transitioned from a
> period when there was a trend toward the divestiture or closing of captive photomask
> operations by semiconductor manufacturers, and to an increase in the share of the market
> served by independent merchant manufacturers … **That period was followed by a period
> during which, in order to reach certain roadmap milestones, some captive mask facilities
> invested at faster rates than independent manufacturers, and the revenue share of market
> transitioned back to photomasks being majority captive-supplied.** More recently, there has
> been a tendency of more production being directed to the independent merchant
> manufacturers, with market share moving toward the independents."

**Read that as a moat test.** The merchant share went up, then down, then up — and in every
case the *cause* named is what the **captives** chose to invest. Photronics is the residual.
When Intel, Samsung and a large foundry decide to spend on their own mask shops to hit a
roadmap milestone, the merchant share falls and Photronics' addressable market shrinks
without any competitive event occurring at Photronics at all. **A business whose market size
is set by the capital-allocation decisions of its own customers does not have a moat; it has
a position in someone else's supply chain.** That is [E3-51]'s wave, stated by the company.

**And the customers are concentrated enough to act on it.** Note 19 and Item 1:

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Customer A | 14% | 15% | **16%** |
| Customer B | 10% | 12% | **13%** |
| Customer C | 13% | 9% | **8%** |
| **Two largest, aggregate** | **27%** | **27%** | **29%** |
| **Five largest, aggregate** | **51%** | **50%** | **50%** |

- **Customer A is also 19.6% of net accounts receivable at FY2025.**
- Photronics sold to *"approximately 636 customers"* in FY2025, and **half its revenue came
  from five of them.** Concentration is rising at the top, not falling: the two largest went
  27% → 27% → 29%.
- **These are the same firms that own captive mask shops.** The concentration and the
  captive threat are not two risks; they are one risk, because the counterparty holding
  half the revenue is the counterparty holding the substitute.

### THE COMPETITOR ROW — required **[E3-28]**

**Photronics' own named competitor list, from Item 1 of the FY2025 10-K, verbatim:**
*"Compugraphics International, Ltd., Dai Nippon Printing Co., Ltd (outside of Taiwan and
China), Hoya Corporation, LG Innotek Co., Ltd., Shenzhen Newway Photomask Making Co., Ltd.,
Shenzhen Qingyi Photomask, Ltd., SK-Electronics Co., Ltd., Taiwan Mask Corporation, and
Tekscend Photomask."* **Nine named merchant competitors, plus the captive operations.**

**Two structural facts in that list that change the reading:**
1. **"Tekscend Photomask" is the former Toppan Photomask** — carved out of Toppan on
   2022-04-01, renamed 2024-11-01, and **listed on the Tokyo Stock Exchange Prime Market on
   2025-10-16 at ¥3,000 a share, ticker 429A**, with TOPPAN Holdings retained at 46.55% and
   no longer the parent. **It is a fully reporting, single-segment, pure-play photomask
   company, and it is the cleanest comparator this industry offers.**
2. **"Dai Nippon Printing Co., Ltd (outside of Taiwan and China)"** — the parenthesis is the
   most revealing five words in the filing. **DNP is Photronics' competitor everywhere
   except Taiwan and China, because in China DNP owns 49.99% of Photronics' Xiamen
   business.** Note 6: *"DNP obtained a 49.99% interest in the Company's IC business in
   Xiamen, China."* Photronics' partner in its largest growth investment is its global
   rival, and that rival holds a put option over the stake (quantified at Q4).

> ### ⚠ CORRECTION, STATED LOUDLY — this run's first draft was WRONG about Tekscend
>
> **The first draft of this row recorded Tekscend Photomask as *"NOT OBTAINABLE — privately
> held … no public segment reporting."* That was false.** Tekscend **listed on the Tokyo
> Stock Exchange Prime Market on 2025-10-16** and files full IFRS accounts. It is the
> **world's largest merchant semiconductor photomask maker** and a **pure play**. The single
> best comparator in the industry was called unobtainable because I did not look hard
> enough, and the row is now filled from its tanshin and its EDINET prospectus.
> **[E4-26] requires the disconfirming search be run hardest against one's own hypothesis;
> here it was run too weakly, and the correction is recorded rather than quietly absorbed.**
> **The verdict does not move, and §"What the completed row does to Q2" below sets out why
> in terms that can be attacked.**

**THE ROW, same metric (operating margin), most recent full fiscal year, all primary-sourced.
Full working, with URLs and the Japanese-language sources, is at
`Test Runs/_research 2026-09-01 PLAB/COMPETITOR ROW - photomask merchants and captives.md`.**

| Company | operating margin | revenue, same period | purity | period | source |
|---|---|---|---|---|---|
| **PHOTRONICS (PLAB)** | **24.5%** *(28.4% FY23 → 25.6% FY24 → 24.5% FY25)* · ROE 11.6%, **10-yr mean 7.9%** | **$849.3M, −4.8% over 2 yrs** | **PURE PLAY** (72% IC / 28% FPD) | FY2025, to 2025-10-31 | 10-K acc. 0001140361-25-045801 |
| **Tekscend Photomask (ex-Toppan)** — **world #1 merchant, 37.8% share** | **21.2%** *(23.9% prior yr; current yr carries one-off IPO costs)* · **ROE 17.2%** (7.8% prior yr) | **¥129,576m ≈ $858M, +9.8%** | **PURE PLAY, single reportable segment** | FY to 2026-03-31 | 決算短信 IFRS, 2026-05-13 |
| **DNP — Electronics segment** | **20.1%** *(24.7% → 23.2% → 20.1%)* · semiconductor business **ROE ~10%** | ¥251,804m segment | **MIXED** — semiconductor photomask is ~27% of the segment; also OLED metal masks, lead frames, HDD suspensions | FY to 2026-03-31 | Consolidated FS Note 23 |
| **Hoya — Information Technology segment** | **51.0–55.1%** *(quarterly; full-year segment OP not disclosed)* | ¥354,751m external | **MIXED** — mask **blanks** (incl. EUV), FPD masks, HDD glass, optics | FY to 2026-03-31 | AR Note 5 + quarterly decks |
| **Intel** | **NO PHOTOMASK DISCLOSURE** — the words *photomask*, *mask shop* and *reticle* appear **zero times** in the FY2025 10-K | — | CAPTIVE | FY to 2025-12-27 | 10-K, filed 2026-01-23 |
| **TSMC** | **NO PHOTOMASK DISCLOSURE** — *photomask* and *reticle* appear **zero times** in the FY2025 20-F; Note 38: *"the Company has only one operating segment, the foundry segment"* | — | CAPTIVE | FY to 2025-12-31 | 20-F, filed 2026-04-16 |
| **Samsung Electronics** | **NOT COMPLETED** in the research pass | — | CAPTIVE | — | — |
| Compugraphics, LG Innotek, Shenzhen Newway, Shenzhen Qingyi, SK-Electronics, Taiwan Mask Corp | not pulled | — | — | — | — |

**THE NUMBER THE OPERATOR ASKED FOR, AND IT IS NOW SOURCED.** The captive-versus-merchant
split was the whole Q2 question and the first draft could not source it. It is:

| | share | year | source |
|---|---|---|---|
| **CAPTIVE share of the photomask market** | **63%** | 2024 | **SEMI *2024 Photomask Characterization Study***, quoted verbatim in Tekscend's EDINET prospectus (S100WN47, 2025-09-04, p.36) |
| **MERCHANT share** | **~37%** | 2024 | same |
| **Tekscend's share of the merchant semiconductor mask market** | **37.8%, world #1** | 2024 | same study, same filing, p.24 |
| Merchant semiconductor photomask market size | **$2,100M** (2024); $2,660M forecast 2028 | 2024 | DNP IR-Day 2025, slide 53, *"DNP estimates based on SEMI data"* |

**Photronics does not disclose its own market share in either the FY2025 or FY2024 10-K —
and it deleted the market-size disclosure it used to give.** The FY2024 10-K carried a
TechInsights estimate of the total IC photomask market (~$7.8bn for 2023) and a Photronics
estimate for FPD (~$930M). **Both were removed from the FY2025 10-K.** A disclosure that
disappears is a **[E2-26]** half-owner-test item: it is information a shareholder would want
to know, and it was there last year.

- **Peers: 9 merchant competitors named by the subject, plus the captive class. Same-metric
  filing-sourced figures now obtained for 4 of them — and for the two largest captives the
  answer is a definitive, verified NIL DISCLOSURE.**
- **The captive half of the industry is a structural UNKNOWABLE, not an UNRESEARCHED gap.**
  Intel and TSMC were full-text searched and the words are simply not in the documents. **No
  document exists that would resolve it**, because the captives do not measure photomasks as
  a segment for external reporting. That is the four-verdict test applied correctly: I asked
  *"can I name the document that would resolve this?"* and the answer is no.

### What the completed row does to Q2 — including the two facts that cut the other way

**THE VERDICT DOES NOT MOVE. It gets narrower and better evidenced.** The row is treated as
completing the record, not as capable of reopening a question the subject's own admissions
already closed. But two findings in it genuinely favour Photronics and both are stated
first, because **[E4-51]** requires the case against my position be put better than its
holders would put it.

**CUTS FOR PHOTRONICS — 1: on operating margin, Photronics is the best of the comparable
pure and near-pure players.** 24.5% against Tekscend's 21.2% and DNP Electronics' 20.1%. I
expected the reverse and did not find it. Two honest qualifiers, neither of which erases the
lead: Tekscend's year carries **one-off IPO costs** and its prior year was **23.9%**, and
the fiscal years are offset by five months.

**CUTS FOR PHOTRONICS — 2: the captives are outsourcing more, and this is a real tailwind.**
Tekscend's FY2026/3 MD&A reports outsourcing demand rising *"among semiconductor makers that
DO produce photomasks in-house, against a background of internal resource shortage"*, and
expects self-supplying memory makers to outsource as they concentrate internal resources on
leading-edge AI memory. DNP plans to *"expand our business into cutting-edge areas currently
dominated by in-house photomasks."* **The 63/37 split is moving toward the merchants.**

**AND HERE IS WHY NEITHER REOPENS Q2.**

1. **The tailwind is the wave, not the moat — [E3-51], and this is the same finding the
   first draft made from Photronics' own oscillation narrative, now confirmed from three
   independent competitor sources.** The merchant share is rising **because the captives are
   choosing to outsource**, for reasons internal to *them* (resource shortage, High-NA EUV
   prioritisation). Nothing Photronics did caused it and nothing Photronics can do will hold
   it: the same passage says in-house shops will *"concentrate capital and personnel on
   High-NA EUV and use merchant supply for existing nodes"* — that is, the captives keep the
   advanced work and outsource the **mainstream**, which is precisely the segment where
   Photronics' revenue is **falling 17.6% in two years** and where the Shenzhen entrants are
   building. **The wave is real and it is breaking on a beach Photronics is losing.**
2. **The tailwind is accruing to a rival, not to Photronics.** Tekscend grew revenue
   **+9.8%** in its most recent year and holds **37.8% of the merchant market as world #1**.
   Photronics' revenue **fell 2.0%** in FY2025 and **4.8% over two years**, and it discloses
   no share at all. **Photronics is losing ground inside a growing merchant market.** A
   margin lead earned while ceding volume is [E4-55]'s warning exactly: *"Dollar revenue
   flattered by pricing is how a shrinking franchise hides; the physical series is the honest
   one."*
3. **Nobody in merchant photomasks earns a franchise return, and that is [E2-58]'s signature
   confirmed across the industry rather than inferred from one filer.** The whole merchant
   layer clusters at **20–25% operating margins** and **single-digit-to-mid-teens ROE**:
   DNP's own semiconductor business at **~10% ROE** by its own IR-Day disclosure, Tekscend at
   **7.8% then 17.2%**, Photronics at a **7.9% ten-year mean**. *"Persistent over-capacity
   without administered prices equals poor profitability."* Photronics being the best of a
   poor class does not make it a franchise; it makes it the best-run job shop in a job-shop
   industry, which is **[E2-37]**'s remarkable-textile-company exactly.
4. **The value chain's economics sit UPSTREAM, and this is the most important single fact the
   row produced.** Hoya's Information Technology segment runs at **51–55% operating margin**
   while Photronics runs at 24.5% — and **Hoya is one layer above Photronics on the blanks it
   buys.** Hoya states it is *"the only manufacturer that has rolled out both EUV and optical
   mask blanks"* and holds *"an exceptionally high market share."* **Photronics' input cost
   is partly set by a near-monopolist earning double its margin, and Photronics' 10-K
   confirms its own exposure: *"There are a limited number of suppliers of these raw
   materials, and we do not have long-term contracts with these suppliers."*** The franchise
   in this chain exists; it belongs to the blank maker, not the mask writer. *(Recorded
   honestly: Hoya's segment is **MIXED** — it carries HDD glass and optics as well as blanks —
   and Photronics never names Hoya as a supplier, so the vertical link is an industry-
   structure inference, not a sourced contract. The margin gap is large enough that the
   direction survives the imprecision.)*
5. **A well-capitalised competitor is investing into Photronics' segment while Photronics'
   sales fall.** DNP plans photomask sales growth of **11.6% CAGR FY2024–28** against a
   market at 8.13%, on a **¥30bn** FY2026–28 capital plan, with EUV masks *"expected to be
   10% of overall sales"* and shipments starting to Rapidus. **[E2-27]**'s mechanism, in a
   competitor's own words: everyone puts more money in the game and returns stay anemic.
6. **And the original grounds are untouched.** Photronics still (a) tells its owners prices
   will keep falling, (b) says no competitor technology is unavailable to it — which by
   symmetry means none of its own is unavailable to them, (c) sells to customers who
   multi-source and who **make 63% of the world's photomasks themselves**, and (d) has earned
   **7.9%** on equity over ten years. **The completed row confirms every one of these from
   outside the subject's own filing.**

**The row's limit, stated [E3-61]:** *"In some businesses, the participants behave like a
demented Kellogg. In other businesses, they don't … I think you'd have to know the people
involved."* The row would show position; it could not show conduct. And on conduct the
filed evidence is already in: the industry's conduct is **published price reduction**.

- Class: [ ] WIDE  [ ] NARROW  **[x] NONE**  [ ] PROVISIONAL · **Direction: NARROWING**
- **VERDICT: [x] OUT**

> **Q2 closes the file. Under the hard sequence (operator rule 2), no verdict below this
> point is reached, and no Q5 clearance exists.** Everything that follows was performed
> because the operator asked for it specifically, and is recorded as **NOT REACHED —
> COMPUTATION, NOT A CLEARANCE** (operator rule 3). None of it carries entry language and
> none of it can reopen Q2.

---
# BELOW THE CLOSING GATE — RECORDED, NOT REACHED
### **COMPUTATION — NOT A CLEARANCE** (operator rule 3)

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — **NOT REACHED**

**STEP 1 — THE WEIGHT CASE, declared even though the gate is not reached.**
- [x] **Daily execution [E3-38]** — **TICKED.** The product is undifferentiated by the
  company's own statement, customers multi-source, and delivery runs from twenty-four hours
  to a two-to-three week backlog. This is a have-to-be-smart-every-day business; there is no
  franchise to coast on.
- [ ] Control [E1-16] — not ticked; minority public stake.
- [ ] Leverage [E3-29] — not ticked. **Photronics is effectively debt-free.** Long-term debt
  ran off to nil by FY2023 (the PDMCX facility liens *"were paid off during fiscal year 2023
  and there was no remaining debt at October 31, 2023"*).
- **One ticked → had the gate been reached, Q3 would be a BINARY GATE and no price would
  compensate.**

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30].** *Each is a prompt to read, never a
verdict [E5-36].*
- [ ] weak accounting — **not fired.** Share-based compensation is expensed ($13.4M FY2025)
  and is in the cash-flow reconciliation.
- [ ] unintelligible footnotes — **not fired.** Note 6 on PDMCX explains the VIE
  consolidation, the 50.01% variable interest, and the put/call mechanics in plain terms.
- [ ] trumpeted projections — **not fired.** The only forward number is a capital-expenditure
  estimate ($330M for FY2026), which is a spending plan, not an earnings promise.
- [x] **serial share issuance [E5-15] — DOES NOT FIRE, and fires in reverse.** Diluted shares
  went 62.0M → 61.2M → 61.8M → 62.4M → **59.9M**. The company **retired** 5.0M shares in
  FY2025.
- [ ] EBITDA promotion [E4-29] — **not fired** in the 10-K.
- [x] **filed-figure tells [E4-30] — CHECKED AND CLEAN, and this cuts in the company's
  favour, which is why it is stated [E4-26].** Cash taxes paid as a share of reported pretax
  income: **37.3% (2020), 22.3% (2021), 15.8% (2022), 26.1% (2023), 25.3% (2024), 27.2%
  (2025).** The tell is cash taxes *falling* as a share of pretax income. They are **rising**.
  In FY2025 the book tax charge was $31.6M (14.2%, after a valuation-allowance release) while
  **cash taxes paid were $60.4M — nearly double the book charge.** A company managing
  appearances does not pay cash tax at twice its reported rate.
- **Unnaturally smooth growth [E4-30]?** The opposite. Owner earnings run −$113.7M to
  +$162.9M inside nine years. Nobody is smoothing this.

**STEP 3 — THE PRIMARY TEST [E2-01].** The ROE series is at Q2 above: **ten-year mean 7.9%,
five-year mean 11.4%, cycle peak 14.3%.** Denominator note per **[E2-43]**: there is **no
goodwill on the balance sheet**, so book equity is already net tangible and no goodwill
wedge needs separating. The series is unleveraged — there is no debt to strip. **This is a
clean read and it is a mediocre number, and [E2-73] is the reason it belongs to the business
and not to the managers: *"what we pay for a business does not affect the amount of capital
its manager has to work with."*** The hand dealt was a commodity job shop.

**The half-owner test [E2-26].** **Passes, and better than most.** Note 10 disaggregates
revenue by product type *and* by geographic origin *and* by timing of recognition. Note 19
gives customer concentration in both revenue and receivables. Note 6 quantifies PDMCX's net
income separately ($19.5M / $20.1M / $25.1M) and discloses the put. The FY2026 capital
plan, the outstanding commitments ($126.4M) and the accrued equipment liabilities ($13.0M)
are all given. **And the related-party disclosure is made without being forced to:**

> "One of our executive officers is related to an individual in a position of authority at
> one of the Company's largest customers. The Company recorded revenue from this customer of
> $137.3 million, $127.0 million, and $126.5 million, in 2025, 2024, and 2023, respectively."

**$137.3M is 16.2% of FY2025 revenue — that is Customer A.** The company's largest customer
relationship runs through a family connection to an executive officer. **This is disclosed
plainly, with the number, in the filing.** Under **[E2-68]** — conduct where the company
holds the information advantage — putting a negative face-up on the table is the *clean*
case, not the flag. It remains a genuine standing exposure and would be a Q6 monitoring
item, but it is a candor credit, not a candor debit.

**The institutional imperative — score all four [E2-30]:**
- [ ] resists change in current direction — no finding.
- [x] **projects/acquisitions materialise to soak up available funds — LIVE.** The company
  holds $588.2M of cash and short-term investments and has announced a **$330M** capital
  programme into a business whose revenue fell 4.8% over two years, while stating it *"stand[s]
  ready to invest in mergers, acquisitions, or strategic partnerships."*
- [ ] staff studies to justify a craving — not observable from filings.
- [x] **peer behaviour mindlessly imitated — this is [E2-27]'s mechanism and it is the
  named death.** See Q4.

**Capital allocation — the two buyback conditions [E5-08], plus the third [E4-31]:**
- **(1) ample funds for operations and liquidity?** **Contested, and this is the sharpest
  Q3 finding.** Cash and equivalents were $492.3M at FY2025. But the MD&A discloses that
  **$446.1M was held by foreign subsidiaries, "including an aggregate of $353.8 million held
  by our joint ventures in Taiwan and China."** So **cash outside the joint ventures is
  $492.3M − $353.8M = $138.5M**, against a **$330M** FY2026 capital programme and **$126.4M**
  of outstanding capital commitments. The company repurchased **$97.4M** of stock in FY2025
  in that position.
- **(2) repurchases at a material discount to conservatively calculated IV?** The FY2025
  buyback retired **5.0M shares for $97,422 thousand — an average of $19.48 per share** —
  against today's $27.33. **On execution timing this is a genuine success and it is stated
  as one.** On our own numbers, however, even $19.48 was not a material discount: at that
  price the capitalisation was roughly $1,208M against five-year owner earnings net of the
  noncontrolling interest of $50.8M — a 4.2% yield, still under the sovereign. **The
  humility clause [E4-13] is attached and it is not a formality here: management bought at
  $19.48 and the stock is $27.33. They were right and our range was not.**
- **(3) [E4-31] — was the register supplied all the information needed to estimate value?**
  **This is the one that fails, and it fails on the same fact that decides Q4.** The
  ownership percentage of the **Taiwan** joint ventures — which generate the majority of the
  $53.8M of noncontrolling-interest earnings — **is not disclosed anywhere in the 10-K.**
  There is no Exhibit 21 list of subsidiaries in the filing. A shareholder cannot compute
  what share of the consolidated cash flow belongs to him without it.
- **→ CAPITAL ALLOCATION FLAG raised on (1) and (3). It binds position size, never the
  discount rate.**

**THE GUARDRAIL [E2-37, E2-38, E3-39].** *"a textile company that allocates capital
brilliantly within its industry is a remarkable textile company — but not a remarkable
business."* **Nothing in this Q3 is used to promote the name, and the well-timed buyback in
particular is not.** Q2 closed the file and a strong Q3 cannot repair Q2.

- **VERDICT: NOT REACHED.** *Had it been reached, the honest entry would be: no integrity
  disqualifier found — which under **[E5-17]** is the absence of found disqualifiers and not
  a finding that the managers are honest — with a live capital-allocation flag on the
  liquidity condition and the undisclosed Taiwan ownership.*

## Q4 — WILL IT SURVIVE? — **NOT REACHED. COMPUTATION — NOT A CLEARANCE.**

### The noncontrolling interest — the correction the operator asked for, and it is larger than at Otis

**The operator's premise needs one correction, and it makes the problem worse rather than
better.** The instruction named "China joint ventures (Xiamen and Hefei)". The filing says
otherwise. **NO INSTANCE FOUND of a minority interest in Hefei**, and the sweep is named:
the 10-K carries exactly one joint-venture note (Note 6, *"PDMCX JOINT VENTURE"*, Xiamen
only); the Hefei plant is listed as *"Owned"* in the Item 2 property table; and the Hefei
site was established under an *"Investment Cooperation Agreement between Hefei State
Hi-tech Industry Development Zone and **Photronics UK, Ltd.**"* Every mention of Hefei in
the document was read. **This is an absence, stated as an absence rather than as a fact** —
the filing nowhere affirms that Hefei is wholly owned, and no Exhibit 21 exists to confirm
it. The disclosed joint venture is **Xiamen (PDMCX, DNP 49.99%)**, and the larger minority
sits in **unnamed Taiwan entities**. The MD&A: net income attributable to
noncontrolling interests rose *"as a result of increased net income at both our
**Taiwan-based** and China-based joint venture IC facilities."* And Note 6 quantifies
Xiamen alone: **PDMCX net income $19.5M (FY2025)** against **total noncontrolling-interest
earnings of $53.8M**.

**The Xiamen minority cannot account for most of the leakage, on either reading of that
line.** The 10-K says *"net income the Company recorded from the operations of PDMCX"* =
$19,462 thousand, which is ambiguous between PDMCX's whole result and Photronics' 50.01%
share. Both readings are carried rather than resolved by preference:
- if $19.5M is **PDMCX's total**, DNP's 49.99% share is **$9.7M — 18% of the $53.8M leakage**
- if $19.5M is **Photronics' share**, DNP's share is **$19.5M — 36% of the leakage**

**Either way the majority of the minority earnings — between 64% and 82% — arises outside
Xiamen, in the Taiwan entities, whose ownership percentage is disclosed nowhere in the
10-K.** The single largest deduction in this file therefore attaches to entities the filing
does not size. That is a disclosure finding under **[E4-31]**, and it is why the deduction
is taken at the reported consolidated noncontrolling-interest earnings rather than built up
from ownership percentages: the percentages are not available to build from.

**The leakage, from the filed statements ($M):**

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | 5-yr mean |
|---|---|---|---|---|---|---|
| Net income, total (consolidated) | 78.8 | 179.2 | 199.6 | 183.8 | 190.2 | 166.3 |
| **less: attributable to noncontrolling interests** | **23.4** | **60.5** | **74.1** | **53.2** | **53.8** | **53.0** |
| Net income attributable to Photronics | 55.4 | 118.8 | 125.5 | 130.7 | 136.4 | 113.4 |
| **NCI as % of total** | 29.7% | 33.8% | **37.1%** | 28.9% | 28.3% | **31.9%** |
| Dividends paid to noncontrolling interests | 9.6 | 0.0 | **0.0** | **0.0** | **0.0** | 1.9 |
| Noncontrolling interest, balance sheet | 176.9 | 230.6 | 300.6 | 359.9 | **423.7** | — |

**Three findings, and the second is the one that matters most:**

1. **Consolidated operating cash flow contains, on a five-year mean, $53.0M a year that
   belongs to other people.** That is **31.9% of consolidated net income** — three times the
   proportion the Otis run found, and Otis's ~$104M/yr changed that answer. Every
   owner-earnings figure the screen computed is gross of this.
2. **Unlike Otis, the minorities take nothing out in cash — and that is worse, not better.**
   Dividends to noncontrolling interests have been **zero for four consecutive years**. The
   money is not leaking out; **it is being retained inside the joint ventures**, where the
   noncontrolling balance has compounded from $176.9M to **$423.7M**, now **26.5% of total
   equity**. At Otis the cash left and could be counted at the door. Here it never leaves,
   so a cash-based measure cannot see it at all — **and neither can a Photronics shareholder
   reach it.** The MD&A confirms the trap: of $492.3M of cash, **$353.8M sits inside the
   Taiwan and China joint ventures**, and repatriation *"could be subject to foreign
   withholding taxes"* and *"in certain jurisdictions … U.S. state income taxes and/or local
   country withholding taxes."*
3. **The deduction used is $53.0M (five-year mean noncontrolling-interest earnings), and the
   judgment is disclosed.** Its direction of bias is stated honestly: because the joint
   ventures are capital-hungry, the minorities' claim on *owner earnings* is arguably a
   little smaller than their claim on *net income*, so this deduction is mildly conservative.
   The offsetting consideration is that the retained noncontrolling capital is being
   reinvested at the joint ventures' returns and a Photronics shareholder will never see it.
   **The exact split is not computable because the Taiwan ownership percentage is not
   disclosed. That is recorded as a work order, not filled with an assumption.**

### Owner earnings — the one number **[E2-23]**, with (c) as a DISCLOSED JUDGMENT

**THE (c) JUDGMENT — and [E5-20] decides it against the D&A end.**

The corpus default is D&A **[E3-44, E2-41]**. The exception is *"anything whose own filing
says depreciation understates renewal"* **[E5-20]**, and for that class **the D&A end is
INVALID, not merely optimistic.** Photronics is in the exception class, on five filed
grounds:

1. **The filing says it, in terms:** *"**The manufacture of photomasks … has been, and
   continues to be, capital intensive.**"*
2. **The company states the spend's purpose is replacement:** *"investments to **replace
   end-of-life mask-making equipment** with higher-performing systems that better serve our
   customers."* Replacing end-of-life equipment is precisely [E2-23]'s (c) — what the
   business *"requires to fully maintain its long-term competitive position and its unit
   volume."*
3. **The arithmetic of the fleet.** Gross PP&E $2,489.3M, accumulated depreciation
   $1,634.9M — **the asset base is 65.7% depreciated**. Machinery and equipment alone is
   $2,109.5M gross. Annual D&A is **$77.6M**. That implies an average life across the gross
   base of **32 years**. Electron-beam mask writers do not last 32 years; the number is
   large because a great deal of the fleet is **already fully depreciated and still running**.
   Depreciation is being charged on tools bought in old dollars while replacements are
   bought at today's prices — which is **[E4-47]** exactly: *"inflation destroys value, but
   it destroys it very unequally"*, and the D&A default weakens for asset-heavy filers.
4. **Capex has exceeded D&A in every window**: 1.50x (9-yr), 1.64x (5-yr), 1.87x (3-yr),
   2.42x (FY2025), **4.25x on FY2026 guidance of $330M**.
5. **The decisive point, and it is the strongest argument that this capex IS maintenance:
   revenue is FALLING while capex rises.** Revenue $892.1M → $866.9M → $849.3M while capex
   $131.3M → $130.9M → $188.1M → guided $330M. **Capital going in without unit volume coming
   out is, by [E2-23]'s own definition, maintenance** — spending required to *maintain* the
   position, not to grow it. A growth-capex reading requires believing that $330M is buying
   expansion in a business whose sales shrank.

**Ruling: the D&A end of the band is INVALID under [E5-20] and is struck. (c) is judged
upward from D&A toward total capex, and total capex is used as the judged figure.** The D&A
construction is displayed below only as a display of the guess **[E4-25]**, never as an
equally legitimate answer.

**THE WINDOWS AND THE BAND — the spread is part of the range [E4-25], and every window is
published [E4-38]:**

| window | (c) | mean(OCF−SBC) | **gross OE** | **less NCI** | **yield on $1,611.5M cap** | vs sovereign 5.27% | **g needed for the [E4-28] 10% floor** |
|---|---|---|---|---|---|---|---|
| 3-yr (FY23–25) | *D&A — INVALID* | 258.7 | *178.3* | *117.9* | *7.32%* | *+2.05* | *2.68%* |
| 5-yr (FY21–25) | *D&A — INVALID* | 238.1 | *156.4* | *103.4* | *6.42%* | *+1.15* | *3.58%* |
| 9-yr (FY17–25) | *D&A — INVALID* | 179.3 | *97.3* | *62.9* | *3.90%* | *−1.37* | *6.10%* |
| **3-yr (FY23–25)** | **capex** | 258.7 | **108.6** | **48.2** | **2.99%** | **−2.28** | **7.01%** |
| **5-yr (FY21–25) — JUDGED [E2-42] default window** | **capex** | 238.1 | **103.8** | **50.8** | **3.15%** | **−2.12** | **6.85%** |
| **9-yr (FY17–25) — full cycle** | **capex** | 179.3 | **56.5** | **22.1** | **1.37%** | **−3.90** | **8.63%** |

- **Short-window mean** (3 yr, judged (c)): **$48.2M** · **Long-window mean** (9 yr):
  **$22.1M** · **five-year default [E2-42]: $50.8M**
- **Stock compensation subtracted in full [E5-06]:** yes, at the reported charge ($13.4M
  FY2025, five-year mean $9.4M). **[E3-70] notes the reported charge is the floor of the
  correct subtraction, not the measure**; at PLAB's scale (1.6% of revenue) the difference
  is not decisive and no further windage is spent on it.
- **Combined range, valid constructions only: $22.1M to $50.8M. Including the struck D&A
  end for display: $22.1M to $117.9M — the top is 5.3x the bottom.**

**IS THE RANGE TOO WIDE TO REACH A CONCLUSION [E4-25]? No — and the reason is the useful
part.** *"If the combined range is too wide to reach a conclusion, that IS the
conclusion."* Here the width is enormous but **the verdict does not move anywhere inside
it.** Two arithmetic facts settle it:

- **The (c) that would make five-year owner earnings merely MATCH the 5.27% sovereign is
  $100.2M.** That is 23% above mean D&A, 25% *below* mean actual capex, and **70% below the
  company's own FY2026 capital guidance.**
- **The (c) that would reach the [E4-28] 10% floor on zero growth is $23.9M** — under a
  third of the depreciation charge and under a fifth of mean capex. **There is no
  construction of maintenance capital expenditure, honest or dishonest, that gets Photronics
  to the floor without growth.**

**Which distorted year sits in the window [E5-11]?** Two, in opposite directions: **FY2019**
(capex $178.4M against $68.4M of operating cash flow — the Xiamen and Hefei build-out, owner
earnings −$113.7M) and **FY2022–23** (the semiconductor shortage peak). **[E3-55] is
consulted and does not rescue the width:** volatility is not a defect *"If we have a business
about which we're extremely confident as to the business result."* Photronics' bounce is not
See's losing money eight months a year around a certain annual total. The *level* is what is
uncertain, and that is exactly the width [E4-25] says to carry.

**The current run rate, from the most recent filing, and it is the sharpest number in the
file.** Six months to 2026-05-03 (10-Q, accession 0001140361-26-024915): operating cash flow
$144.3M, share-based compensation $6.6M, capital expenditure $93.4M → **owner earnings
$44.3M**, less noncontrolling-interest earnings of **$29.1M** → **$15.2M attributable to
Photronics shareholders in six months**, against a $1,611.5M market capitalisation. And the
company guides capital expenditure to roughly double in the second half to hit $330M.

### Great, good, or gruesome? **[E4-20]** — and I am not going to overstate this

- [ ] great  · **[x] good** · [ ] gruesome
- **The honest answer is GOOD, not gruesome, and saying so cuts against the conclusion of
  this file, which is why it is said [E4-26].** **[E4-43]** scopes the test: the *good* class
  **passes** — *"nothing shabby about earning $82 million pre-tax on $400 million of net
  tangible assets"*, which is 20.5%. Photronics FY2025: operating income **$208.2M** against
  net assets of $1,597.3M **less** $588.2M of cash and short-term investments =
  **$1,009.1M of operating net tangible assets → 20.6% pre-tax.** That lands **on**
  [E4-43]'s benchmark. There is no goodwill to strip.
- **The qualification, and it is large.** That 20.6% is computed on a depreciation charge
  [E5-20] says is too low. Substituting the observed five-year replacement rate ($134.3M for
  $77.6M) takes operating income to $151.5M and the return to **15.0%** — still "good", not
  gruesome. And roughly **32% of it belongs to the noncontrolling holders.**
- **So Q4 would not have failed on the great/good/gruesome test.** The business earns an
  acceptable return on the assets it operates. **What it does not do is convert that return
  into cash a Photronics shareholder can have**, because (c) consumes it and the minorities
  take a third of what is left. That is a Q5 problem and a Q2 problem, not a survival
  problem.

### Staying power — score all three **[E5-11]** — *"acceptable long-term results under extraordinarily adverse conditions"* **[E2-55]**

- **(1) Large and reliable stream of earnings — LARGE, NOT RELIABLE.** Operating income has
  run $94.6M → $211.9M → $253.1M → $221.5M → $208.2M in five years, and owner earnings
  −$113.7M to +$162.9M in nine. Under **[E5-29]** volatility is not risk — but the swing here
  is in the *level*, not around a known one.
- **(2) Massive liquid assets — YES, WITH A LOCATION PROBLEM.** $492.3M cash plus $95.9M
  short-term investments = **$588.2M**, against **essentially no debt**, and working capital
  of $890.1M against $165.9M of current liabilities. On the face of it this is a fortress.
  **But $353.8M of it is inside the joint ventures**, roughly half of that belongs to the
  minorities, and moving it home triggers withholding tax. **Cash genuinely at the parent's
  free disposal is on the order of $138.5M.**
- **(3) No significant near-term cash requirements — THIS ONE FAILS, and it fails on a
  quantified, filed obligation.** *"Ignoring that last necessity is what usually leads
  companies to experience unexpected problems"* **[E5-11]**. Three claims land in the same
  place:
  - **$330M of FY2026 capital expenditure**, of which **$126.4M is already committed** and
    **$120.0M is expected to be funded within twelve months.**
  - **The DNP put.** Note 6 and the MD&A: DNP *"has, under certain circumstances, the right
    to put its interest in the joint venture to Photronics"* at net book value, closing
    *"within three business days of obtaining required approvals."* **"Photronics and DNP
    each had net investments in this joint venture of approximately $160.4 million."**
    **The put is $160.4M against $138.5M of cash held outside the joint ventures.**
    **It exceeds the parent's free cash, and it is exercisable in three business days.**
  - **And the correlation is the danger, not the amount [E4-40] — model exposure, not
    experience.** DNP would rationally put its Xiamen stake **precisely when the China
    business deteriorates** — an export-control action, a demand collapse, a subsidised
    price war. The $160.4M call arrives in the state of the world where Photronics can least
    afford it, and where the $353.8M of joint-venture cash is hardest to move. A benign
    history here is *"not only useless, but actually dangerous"* as a guide.
- **Leverage, named and quantified [E4-16, E3-29]:** **there is effectively none.** No
  long-term debt since FY2023; a CNY 200M ($25M) undrawn revolver at PDMCX, extended to
  2026-07-31. **[E2-54]**'s coverage test passes trivially because there is no interest to
  cover. **This is Photronics' single best defensive fact and it is stated plainly.**
- **[E3-66] jurisdiction:** Photronics is a US registrant, so the US shareholder-priority
  point runs in its favour at the top. **But 68.3% of net assets sit in Taiwan ($663.6M) and
  China ($427.6M)**, where that protection does not reach.

### Name the specific way THIS business dies **[E2-27, E3-24]**

**[E4-51]: I am obliged to state the case against my position better than its holders
would.** Three mechanisms, quantified from filed figures, with likelihoods in the corpus's
vocabulary.

**DEATH 1 — Mainstream commoditisation by subsidised domestic Chinese capacity. LIKELY, and
it is already in the filed numbers.**
- The mechanism is **[E2-27]** exactly: *"Viewed individually, each company's capital
  investment decision appeared cost-effective and rational; viewed collectively, the
  decisions neutralized each other and were irrational … After each round of investment, all
  the players had more money in the game and returns remained anemic."*
- **Quantified:** IC mainstream is **$376.2M, 44.3% of FY2025 revenue**, and has fallen
  **17.6% in two years** (456.3 → 409.7 → 376.2), a −9.2% compound rate. Photronics' own
  10-K names two Chinese entrants — **Shenzhen Newway** and **Shenzhen Qingyi** — as
  competitors. Revenue earned in China fell $245.4M → $232.9M → **$221.0M**.
- **The outcome, computed:** continue the mainstream decline at −9.2%/yr for five years and
  IC mainstream reaches **$232.4M, a loss of $143.8M of revenue.** Because the cost base is
  the fixed one the filing describes, the incremental margin is high. At the FY2025 gross
  margin of 35.3% (a deliberately *low* estimate for incremental volume) the loss is
  **$50.8M of gross profit, taking operating income from $208.2M to $157.4M, −24%.** At a
  70% incremental margin — more realistic for a clean-room job shop losing volume against
  fixed depreciation — the loss is **$100.7M, operating income $107.5M, −48%.** Then the
  noncontrolling holders take roughly a third of what remains.
- **Add the asset leg the filing itself names:** underutilisation *"could … result in
  write-offs from asset impairments"* against **$854.4M of net PP&E**, of which **$264.0M is
  in China**.
- **Likelihood: [x] likely.** Not a forecast — a continuation. It has happened for two
  consecutive filed years.

**DEATH 2 — The DNP put lands in the middle of a China shock. A REAL POSSIBILITY.**
- **$160.4M**, exercisable at net book value on three business days' notice, against
  **$138.5M** of cash outside the joint ventures, correlated by construction with the state
  of the world in which Photronics is least able to pay. Photronics would not be insolvent —
  it could sell short-term investments, draw new debt against an unlevered balance sheet, or
  repatriate at a tax cost — but it would be doing so at the worst moment, and it would end
  up owning **100% of a Chinese mask business at exactly the point that business became
  worth less.**
- **Likelihood: [x] a real possibility.** The filing states *"As of the date of issuance of
  this report, DNP had not indicated its intention to exercise this right."*

**DEATH 3 — Export control or a Taiwan Strait event. A LOW-LEVEL POSSIBILITY, and
catastrophic.**
- The exposure, from Note 19: **Taiwan net assets $663.6M and China net assets $427.6M —
  $1,091.3M, or 68.3% of the $1,597.3M total.** Long-lived assets: Taiwan $240.5M + China
  $264.0M = **$504.5M of $854.4M, 59.0%.** Revenue by origin: Taiwan $283.8M + China
  $221.0M = **59.4%**.
- The export-control mechanism is stated by the company: *"The EAR could prohibit the export
  of certain products out of the US or **could prohibit our foreign sites from manufacturing
  or delivering photomasks to certain restricted entities**."* Photronics' Xiamen plant
  exists to serve Chinese customers; a restricted-entity designation among them removes the
  revenue while leaving the plant.
- **Quantified:** a total loss of the China position writes off **$427.6M of net assets —
  26.8% of book equity, of which roughly half is the minorities' — and removes $221.0M of
  revenue.** A Taiwan event reaches $663.6M more. **Photronics survives the China leg on its
  debt-free balance sheet; it does not survive the Taiwan leg as the same company.**
- **Likelihood: [x] a low-level possibility** for the Taiwan leg; the export-control leg is
  nearer **a real possibility**, and the U.S. Commerce Section 232 semiconductor
  investigation the filing names is live.

- **VERDICT: NOT REACHED** (Q2 closed the file).

---
## Q5 — **NOT REACHED. COMPUTATION — NOT A CLEARANCE.**
### *(operator rule 3: this carries no entry language and is not a clearance)*

**Price and capitalisation.** Close **$27.33** on **2026-09-01** *(aggregator quote, flagged
per operator rule 5 — aggregators for live quotes only)*. Shares outstanding **58,963,698**
as of 2026-06-04 (10-Q cover, dei, accession 0001140361-26-024915). **No stock split at any
date after the measurement date**, so the split-invariant formula reduces to price × shares:
**market capitalisation $1,611.5M.** *(The screen's $1,635M used a slightly earlier share
count; the difference is immaterial and the smaller, current figure is used, which is the
less favourable choice for the conclusion below — it raises the yield.)*

**1. THE YIELD**
- **judged: owner earnings $50.8M ÷ $1,611.5M = 3.15%** · sovereign **5.27%**
- band across valid constructions: **1.37% to 3.15%** · struck D&A display: up to 7.32%

**2. WHAT THE PRICE ALREADY ASSUMES**
- **perpetual growth needed to reach the [E4-28] 10% floor: 6.85%** (judged construction);
  7.01% on the three-year window; **8.63%** on the full nine-year cycle.
- **what the business has actually done:** revenue CAGR **+6.4%/yr** FY2021→FY2025 (a window
  that begins at the cycle trough and ends after the boom); **−2.4%/yr** FY2023→FY2025;
  **+8.2%/yr** FY2017→FY2025. Owner earnings, judged construction, on the nine-year mean:
  **$22.1M**, less than half the five-year figure.
- **[E4-35] is the standing objection to the growth case:** *"fewer than 10 of the 200 most
  profitable companies in 2000 will attain 15% annual growth in earnings-per-share over the
  next 20 years."* 6.85% is not 15% — but it must be **perpetual**, in a business whose
  filing forecasts continued price reduction and whose largest segment is shrinking.
  **[E4-44]** bounds it further: *"the value of an asset … cannot over the long term grow
  faster than its earnings do."*

**3. WHAT YOU ARE PAID**
- **−2.12 points against the sovereign** at the judged construction; **−3.90 points** on the
  full-cycle window. Even the struck D&A end on the five-year window pays **+1.15 points**,
  which is still far below the floor.

**THE STRONGEST DISCONFIRMING CASE, STATED PROPERLY [E4-26, E4-51].** The best argument for
Photronics is that the market capitalisation is heavily backed by financial assets, and it
deserves to be run:
- Cash $492.3M + short-term investments $95.9M = **$588.2M**, against **no debt**.
- Deduct the minorities' claim on the $353.8M held inside the joint ventures at roughly 50%
  (**$176.9M**): **PLAB-attributable financial assets ≈ $411.3M.**
- **Enterprise value attributable to Photronics ≈ $1,611.5M − $411.3M = $1,200.2M.**
- **On EV, the yields are: 4.02% (3-yr, capex), 4.23% (5-yr, capex), 1.84% (9-yr, capex) —
  and on the struck D&A end, 8.62% (5-yr) and 9.82% (3-yr).**
- **The result is the honest one and it survives every favourable choice.** Stack **three**
  concessions at once — take the boom window, use the D&A end that **[E5-20]** rules
  **INVALID**, and price off enterprise value net of attributable cash — and Photronics
  reaches **9.82%**. **It still does not clear the [E4-28] 10% floor.** That is the finding:
  the case for this name requires stacking three favourable choices and still comes up short.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — capitalising the judged owner earnings at
the 5.27% sovereign, and adding back the attributable financial assets:
- **conservative ≈ $14 per share** *(9-yr window, (c) = capex: $22.1M ÷ 5.27% = $419M, plus
  $411M attributable cash = $831M ÷ 59.0M shares = $14.09)*
  **[CORRECTED IN-RUN, 2026-09-02: this line first read "≈ $9", which dropped the cash
  add-back at the rounding step. The corrected figure is $14. Recorded rather than silently
  amended, per operator rule 6's principle. Note the direction: the correction RAISES the
  conservative end and therefore cuts AGAINST this file's conclusion [E4-26].]**
- **central ≈ $23 per share** *(5-yr judged: $50.8M ÷ 5.27% = $964M + $411M = $1,375M)*
- **optimistic ≈ $40 per share** *(the struck D&A end, 5-yr: $103.4M ÷ 5.27% = $1,962M +
  $411M = $2,373M — shown only because [E4-25] says to display the guess; it rests on a
  construction [E5-20] calls invalid)*
- **current price $27.33** *(2026-09-01)*

> **⛔ There is no Q5 verdict, no ranking position, and no bar applied. Q2 returned OUT and
> the hard sequence forbids a Q5 clearance. The band above is arithmetic recorded for the
> next reader, and under the [E4-28] floor it would in any case be quit on rather than
> ranked. Windage count: conservatism applied ONCE — at the (c) judgment, where [E5-20]
> struck the D&A end. No second margin is taken, and none is needed.**

---
## Q6 — **NOT REACHED.**

Recorded for the register, since a closed file still earns a re-open condition:
- **What would reverse Q2:** evidence that mainstream IC photomask pricing has stopped
  falling — specifically, a filed statement replacing *"the pressure to reduce prices … will
  continue in the future"* — together with two consecutive years of rising IC mainstream
  revenue.
- **Next catalyst:** Q3 FY2026 10-Q (quarter ended ~2026-08-02), due within weeks of this
  run, which will show whether capital expenditure is genuinely tracking to $330M and
  whether IC mainstream has stabilised.
- **Position: NIL.** The file is closed at Q2.

---
## SELF-AUDIT
- [x] Questions answered in order; **stopped at the first non-IN verdict (Q2 OUT)**; no
      verdict skipped, and everything below is explicitly marked NOT REACHED
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the
      only IN and it rests on the filing.
- [x] No UNRESEARCHED verdict issued. **One work order is nonetheless recorded** (below),
      because the competitor row is incomplete and saying so is required even where it does
      not change the verdict
- [x] No UNKNOWABLE verdict issued
- [x] Step 0: the filing was read, with accession number; **two figures cross-checked**
      against the filed statements
- [x] Owner earnings on a multi-year mean; **three windows published [E4-38]**; capex band
      disclosed as a judgment and the D&A end **struck as INVALID [E5-20]** with the filing
      quoted for it; **net of noncontrolling interests**
- [x] **Competitor row COMPLETED** *(filled 2026-09-02, after the first draft)*: 9
      competitors named from the subject's own filing; **same-metric operating margins
      obtained for Photronics, Tekscend, DNP and Hoya from primary company documents**; the
      two largest captives full-text searched with a **verified nil disclosure**; and the
      **captive/merchant split sourced at 63/37 (SEMI 2024)**. **One error corrected and
      recorded loudly in the row itself**: the first draft called Tekscend privately held and
      unobtainable; it listed on the TSE Prime Market on 2025-10-16 and reports in full.
      Moat class re-tested against the completed row and **unchanged at NONE**.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated; **the
      deviation from FRED to the U.S. Treasury is declared with its reason**
- [x] Value stated as a round-number range, not a point estimate
- [x] **No bar applied** — Q5 was not reached; windage count stated (one)
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] Every judgment carries a ledger id (operator rule 8); all cited ids verified present in
      `principle_ledger.csv` (261 rows)
- [x] Run committed to git

## REGISTER
- Verdict: **[x] OUT (about the business)**
- **One line: Photronics is a merchant job shop selling an undifferentiated product to
  concentrated customers who own the substitute, its own 10-K forecasts continued price
  reduction and rising capital requirements, and a third of the cash flow the screen
  measured belongs to minority partners it does not name.**
- **THE WORK ORDER — CLOSED 2026-09-02, except where structurally impossible:**
  - **CLOSED. DNP and Hoya segment disclosures** — obtained from DNP's Consolidated
    Financial Statements Note 23 and Hoya's Annual Report Note 5 plus its quarterly decks.
    **DNP Electronics 20.1%, Hoya IT 51–55%**, both flagged **MIXED SEGMENT** as anticipated.
  - **CLOSED, AND THE FIRST DRAFT WAS WRONG. Tekscend Photomask (ex-Toppan)** — **not
    private**: TSE Prime listing 2025-10-16, ticker 429A. **21.2% operating margin, pure
    play, world #1 merchant at 37.8% share.** Correction recorded in the row itself.
  - **CLOSED AS UNKNOWABLE, NOT UNRESEARCHED. The captive mask economics of Intel, TSMC and
    Samsung** — Intel's FY2025 10-K and TSMC's FY2025 20-F were full-text searched and the
    words *photomask* and *reticle* appear **zero times** in each; TSMC reports **one
    operating segment**. **No document exists that would resolve this**, so the separating
    test returns UNKNOWABLE and the file does not carry it as an outstanding task.
  - **STILL OPEN — artifact: the Taiwan joint-venture ownership percentage** · where it
    lives: **an Exhibit 21 list of subsidiaries** · ladder rung: **SEC EDGAR primary
    documents** · **blocked by: no Exhibit 21 is filed with the FY2025 10-K.** Recorded as a
    Q3 disclosure finding under **[E4-31]**, not merely a research gap. **This is the one
    material gap left in the file, and it sits under the largest deduction in it.**
  - **STILL OPEN, IMMATERIAL — Samsung's captive disclosure and an independent read on
    mainstream mask pricing**: both were left as placeholders by the research pass. Neither
    can move Q2, which is already OUT.

---

# THE OUTPUT CONTRACT — THE PRICE, AND THE PASS/FAIL LINE

## (a) THE PRICE — **COMPUTATION — NOT A CLEARANCE** *(operator rule 3)*

**Q1–Q4 did not all return IN. Q2 returned OUT. Therefore this is not a Q5 band, it carries
no entry language, and it is not a clearance. It is arithmetic, reported because the
operator gets a number either way.**

| | |
|---|---|
| **Current price** | **$27.33** (2026-09-01, aggregator quote, flagged) |
| **Shares outstanding** | 58,963,698 (10-Q cover, 2026-06-04, acc. 0001140361-26-024915) |
| **Market capitalisation** | **$1,611.5M** |
| **Sovereign** | **5.27%** — US Treasury 30-year par yield, 2026-09-01, issuing authority |
| **Owner earnings, JUDGED** *(5-yr mean, (c) = total capex, **net of noncontrolling interests**)* | **$50.8M** |
| **Yield on that** | **3.15% — 2.12 points BELOW the sovereign** |
| **Perpetual growth needed for the [E4-28] 10% floor** | **6.85%** |

**THE COMPUTED RANGE, in round numbers [E4-01]:**

| | per share | construction |
|---|---|---|
| **conservative** | **≈ $14** | 9-yr full-cycle window, (c) = capex, net of NCI |
| **central** | **≈ $23** | 5-yr default window [E2-42], (c) = capex, net of NCI |
| *optimistic* | *≈ $40* | *the D&A end — **struck as INVALID under [E5-20]**, shown only to display the guess [E4-25]* |
| **current price** | **$27.33** | |

**The valid range is $14 to $23. The price is $27.33. It sits ABOVE the whole valid range,
and inside the band only if the D&A construction [E5-20] rules invalid is readmitted.**
Under the screamer test's three outcomes **[E4-01]** that is the third one — *"price above
the whole range → no"* — not even the middle *"no useful conclusion"* case. **This is
recorded as arithmetic, not as a recommendation: the gates never opened, and a Q5 result
cannot be reported for a file that closed at Q2.**

## (b) THE PASS/FAIL LINE

> # **FAIL — the file closed at Q2.**
>
> **Photronics is not a franchise.** Its own FY2025 10-K states that *"most of our customers
> utilize multiple photomask suppliers"*, that *"there is no significant technology employed
> by our competitors that is not available to us"*, and that *"the pressure to reduce prices
> … will continue in the future"* — while it competes against the **captive mask operations
> of the same concentrated customers who supply half its revenue.** [E3-03] criterion (2)
> fails on the subject's own admissions, and a ten-year mean return on equity of **7.9%**
> is the number that confirms it [E3-46].
>
> **The completed competitor row confirms it from outside the subject's filing.** The
> captives make **63%** of the world's photomasks in-house (SEMI 2024, via Tekscend's
> prospectus); Photronics fights for the 37% remainder and is **not the leader** — Tekscend
> is, at **37.8%** of the merchant market, growing **+9.8%** while Photronics **fell 4.8%
> over two years**. The whole merchant layer clusters at **20–25% operating margins and
> single-digit-to-mid-teens ROE**, which is [E2-58]'s commodity signature measured across an
> industry rather than inferred from one filer. **The franchise in this value chain belongs
> to Hoya, one layer upstream at 51–55% margins on the blanks Photronics must buy.**

**The six questions:**

| | question | verdict |
|---|---|---|
| **Q1** | Can I understand how this makes money? | **IN** |
| **Q2** | Is it a franchise? | **OUT ← the file closes here** |
| **Q3** | Are they honest, and are they rational? | **NOT REACHED** |
| **Q4** | Will it survive? | **NOT REACHED** |
| **Q5** | What is it worth against a government bond? | **NOT REACHED** — computation only |
| **Q6** | What would prove me wrong, and when do I sell? | **NOT REACHED** |

**Not one of Q3–Q6 is a pass, a fail, or a near miss. Under the hard sequence they were not
asked**, and the material recorded under them above is computation preserved for the next
reader, not a verdict.

---

## THE THREE THINGS A READER SHOULD TAKE FROM THIS FILE

**1. The noncontrolling interest is the largest single correction, and it is bigger here
than at Otis.** Consolidated operating cash flow contains **$53.0M a year on a five-year
mean — 31.9% of consolidated net income — that belongs to minority partners.** Otis's
leakage was ~$104M on a business eight times the size; proportionally Photronics' is roughly
**three times as severe.** And it behaves worse: Otis's minorities took their cash out as
dividends, where it could be counted at the door. **Photronics' minorities have taken
nothing in cash for four consecutive years** — the money compounds inside the joint
ventures, where the noncontrolling balance has grown from $176.9M to **$423.7M (26.5% of
total equity)**, and where **$353.8M of the company's $492.3M of cash is trapped**. A
cash-based screen cannot see this deduction at all, and a Photronics shareholder cannot
reach the money.

**2. The D&A end of the owner-earnings band is INVALID, not merely optimistic — and the
filing is what decides it.** Photronics says *"The manufacture of photomasks … has been, and
continues to be, **capital intensive**"* and describes its spending as *"investments to
**replace end-of-life mask-making equipment**"*. The fleet is **65.7% depreciated**; annual
D&A of $77.6M against $2,489.3M of gross plant implies a 32-year life on electron-beam
writers. Capex has run **1.5x to 2.4x D&A** and is guided at **$330M for FY2026 — 4.25x the
depreciation charge — while revenue FELL 4.8% over two years.** Capital going in without
volume coming out is maintenance by [E2-23]'s own definition. **[E5-20] applies and the
generous construction is struck.**

**3. The range is enormous and the verdict does not move anywhere inside it.** From $22.1M
(nine-year, capex) to $117.9M (three-year, struck D&A end) is a **5.3x spread** — far wider
than the screen's 88%, and under **[E4-25]** the width is itself the finding: a distorted
year sits in every window (FY2019's −$113.7M build-out; FY2022–23's shortage peak). **But
the width does not need resolving, because two numbers close it:** the maintenance capital
figure that would make Photronics merely *match* the government bond is **$100.2M** — 25%
below its own mean capex and 70% below its own FY2026 guidance — and the figure that would
reach the **[E4-28]** 10% floor on zero growth is **$23.9M**, under a third of the
depreciation charge. **No honest construction of (c) reaches the floor.**

---

## THE STRONGEST DISCONFIRMING FACT — stated because [E4-26] and [E4-51] require it

**Photronics is debt-free and roughly a quarter of its market capitalisation is net
financial assets.** Cash of $492.3M plus short-term investments of $95.9M is **$588.2M
against no long-term debt**, with working capital of $890.1M against $165.9M of current
liabilities. Strip the minorities' ~$176.9M claim on the joint-venture cash and
**$411.3M is attributable to Photronics shareholders, giving an enterprise value of about
$1,200M.** On operating net tangible assets the business earns **20.6% pre-tax**, which
lands exactly on **[E4-43]**'s *"nothing shabby"* benchmark — this is the **good** class,
**not the gruesome one**, and Q4 would not have failed on that test. High-end IC revenue
grew **22.5%** over two years. Management retired 5.0M shares at an average **$19.48**
against today's $27.33 and were plainly right to. Cash taxes are **rising** as a share of
pretax income (15.8% → 27.2%), so the **[E4-30]** fraud tell does not fire; in FY2025 the
company paid **$60.4M of cash tax against a $31.6M book charge.**

**And here is the test I set for that case, which is the honest way to end the file.** Stack
**three** favourable choices at once — take the boom window (FY2023–25), use the D&A end that
**[E5-20]** rules **invalid**, and price off enterprise value net of attributable cash — and
Photronics returns **9.82%**.

**It still does not clear the 10% floor [E4-28].** The bull case has to win three arguments
in a row and it comes up short on all three at once. **That is why Q2's verdict is not a
close call, and why no price at Q5 could have rescued it.**
