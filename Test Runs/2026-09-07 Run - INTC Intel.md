# Company Run — INTEL CORPORATION (INTC) — 2026-09-07
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
- rate **5.24%** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-year,
  from the issuing authority** (`home.treasury.gov`, `daily_treasury_yield_curve`, fetched
  fresh 2026-09-07; 09/04/2026 is the last published date — 09/07/2026 is Labor Day).
  FRED DGS30 not used; it is the fallback, not the source.
- FX: **none required.** Intel reports in USD and files in USD. The 10-K states the
  functional currency is the US dollar for substantially all operations.

**THE FILING WAS READ** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary: FY2025 Form 10-K, FYE 2025-12-27, filed 2026-01-23, accession
  `0000050863-26-000011`** (`intc-20251227.htm`).
- **Stub, and it matters more here than at any name in this queue: Q2 2026 Form 10-Q,
  period 2026-06-27, filed 2026-07-24, accession `0000050863-26-000157`**
  (`intc-20260627.htm`). **Two quarters of 2026 exist and they change the picture in both
  directions.** The AVGO defect (a stub ignored) does not repeat.
- Also read: **FY2024 10-K**, accession `0000050863-25-000009` (for the dividend-suspension
  language, which the FY2025 10-K does not repeat); **DEF 14A filed 2026-03-23**, accession
  `0000050863-26-000061` (pay v. performance, Item 402(v)).
- **Figure cross-checked against the filed statement:** XBRL `GrossProfit` FY2025 =
  **$18,375M**; the filed Consolidated Statements of Operations shows net revenue **$52,853**
  less cost of sales **$34,478** = **$18,375**. Matches to the dollar. Operating loss
  **$(2,214)M** likewise ties.

### STAGE 0 BY HAND — THE COVER COUNT, AND THE ECONOMIC COUNT IS NOT THE COVER COUNT

The brief requires the government stake and any warrants/convertibles in the economic count
(the FLNC Up-C lesson, the LEVI/PINS dimension lesson). Intel is **single-class** — no A/B
problem — but it has **three** claim layers above the cover number, all created in the last
thirteen months:

| layer | shares (M) | filed source |
|---|---|---|
| common issued and outstanding, **Jun 27 2026 balance sheet** | **5,043** | Q2 2026 10-Q, Consolidated Condensed Balance Sheets |
| common outstanding, **10-Q cover, Jul 17 2026** | **5,044** | *"As of July 17, 2026, the registrant had outstanding 5,044 million shares of common stock."* |
| **Escrowed Shares not yet released** (contingently issuable to the US government at $20.00/sh against $3.2bn of Secure Enclave disbursements) | **+71** | Q2 2026 10-Q Note 4 |
| **= ECONOMIC COUNT USED** | **5,115** | |
| DOC **Warrants**, 241M at $20.00, exercisable **only if Intel ceases to own ≥51% of Intel Foundry** — *"neither currently nor expected to become exercisable"* | (+241 memo) | Q2 2026 10-Q Note 4 |

- **Market cap used: 5,115M × $95.80 = $490,017M.** On the bare cover count it is
  $483,215M; on the fully-loaded count including the warrants (5,356M, net of $4,820M of
  exercise cash) it is **$508,890M less $4,820M = $504,070M** of claim. **The run uses
  $490,017M and states the other two.** The choice moves the yield by ~1.4% relative,
  which is immaterial to every verdict below.
- **Price $95.80, 2026-09-04 close, Yahoo Finance — AGGREGATOR, FLAGGED**, live quote only,
  per operator rule 5. **52-week range $24.05 - $142.35.** The 10-K cover's own
  non-affiliate market value was **$99.3 billion as of June 27, 2025**; the same equity is
  now marked near **$490 billion. That is a ~4x re-rating in fourteen months and it is the
  single most important number in this file.**
- **Split check: none.** The share progression 4,137 (2022) → 4,228 (2023) → 4,330 (2024)
  → 4,994 (2025) → 5,043 (Q2 2026) is fully explained by issuance, not by a split.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### The brief's question: product company, foundry, or both? **The filing answers it, and the answer is "one of each, and they sit on opposite sides of the ledger."**

**Unit economics in my own words, no management language.** Intel does two entirely
different things and reports them separately. **The first is a catalogue business and it
works.** Intel designs x86 processors — the general-purpose engine inside almost every
Windows PC and a large minority of the world's servers — and sells them to a few dozen PC
makers and a handful of cloud operators. In 2025 that business took in **$49,147M and kept
$12,739M of operating income, a 26% margin**, and it has kept between 23% and 26% for three
straight years. **The second is a factory business and it is a furnace.** Intel owns and
runs the fabs that build those processors, and in 2025 that operation booked **$17,826M of
revenue and lost $10,318M** — a **negative 58% operating margin**. Almost all of its revenue
is Intel paying itself: **external foundry revenue was $307M in 2025 and $159M in 2024**,
which is **1.7% of the foundry segment and 0.58% of the company**. Put the two together and
the intersegment revenue cancels: Intel took in **$52,853M and lost $2,214M at the operating
line.** So: the money is made selling chips and it is entirely consumed making them. The
whole investment question is whether the furnace ever pays for itself, and Intel's own filed
answer is that it has not yet started to.

**The scarce input this business controls, and it is real.** Leading-edge logic
manufacturing physically located in the United States. Intel's own words, FY2025 10-K:
*"We continue to innovate and advance leading-edge semiconductor process technology and
manufacturing in the U.S., where we are **the only company conducting both leading-edge
logic R&D and high-volume manufacturing**."* That scarcity is not a marketing claim — it is
why the US Department of Commerce took equity in August 2025 rather than merely writing a
grant. Second scarce input, and it is the older one: **the x86 instruction set and the
thirty-five years of compiled software that assumes it.** Intel does not own x86 alone (AMD
cross-licenses it), but the pair of them own it against everyone else.

### THE HHH TEST — RUN EXPLICITLY, BECAUSE THE BRIEF PUTS IT LIVE

HHH closed at **Q1 UNKNOWABLE** because a declared transformation made the forward entity
unanalyzable: it bolted a specialty insurer with **26 days of filed history** onto a
real-estate developer, and the filed past described a different company from the one the cap
was pricing. **Intel is superficially the same shape and structurally the opposite, and here
is the difference stated so it can be checked:**

| | HHH (closed Q1 UNKNOWABLE) | INTC |
|---|---|---|
| the transforming asset | **acquired**, 2026-06-04 | **already owned**, for forty years |
| filed history of that asset under the registrant | **26 days** | **decades**, and three years retrospectively restated onto today's segments |
| what the forward entity is made of | assets the registrant had never operated | **the same fabs, the same x86 catalogue, the same customers** |
| can the two halves be measured separately today? | no | **yes — Note 3 does it, in dollars, for 2023 / 2024 / 2025** |

**Intel's "transformation" is a re-labelling of manufacturing it already owns, not the
purchase of a business it has never run.** The declared intent — *"transitioning our
semiconductor manufacturing business from one that has historically been designed to serve
our internal product groups into a customer-centric foundry business"* — changes **who the
fab invoices**, not what the fab is. And the failure of that intent so far is itself a filed
number: **$307M**, against which Intel's own 10-K says *"**While we have few external
customers to date**, developing an external foundry business is a key long-term strategy."*
I do not need to forecast the foundry to read this file; I need to read what the foundry has
cost, which is disclosed to the dollar.

**The three complications, named rather than waved at, because each one was a candidate for
closing this gate:**

1. **The US government equity.** 275M shares issued outright, 159M more into escrow at
   $20.00/share against $3.2bn of Secure Enclave disbursements, and warrants over 241M
   shares struck at $20.00 that spring **only if Intel ceases to own at least 51% of Intel
   Foundry**. Unusual — but fully disclosed, dated and quantified. It is a **Stage 0
   share-count problem and a Q3 capital-allocation fact, not an understanding problem.**
2. **The escrowed-share mark-to-market, and it is the strangest single number in this
   queue.** The Escrowed Shares are carried as a **liability marked to market**, so Intel
   books a **loss when its own stock rises.** H1 2026, verbatim from the cash-flow
   statement: *"Mark-to-market (gains) losses on Escrowed Shares **13,619**"* — a **$13.6bn
   non-cash charge** that turned an underlying six-month loss of roughly $1.5bn into a
   reported **$15,129M** loss. **This makes reported net income unusable for 2026, and it is
   precisely why operator rule 5 forbids an owner-earnings net-income proxy.** It obscures
   one line; the cash-flow statement adds it straight back.
3. **The disposals.** Altera 51% sold 2025-09-12 for $4.3bn net consideration, producing a
   **$5.6bn pre-tax gain** parked in *interest and other, net* — of which **$2.1bn is pure
   remeasurement of the retained 49%**, not cash. Mobileye still consolidated. SCIP partner
   structures pushing non-controlling interests to **$15,601M**. These make the *income
   statement* messy. They do not make the *segments* messy, and the segments are where the
   business is.

**Will the fundamentals look broadly the same in ten years?** **Partly, and I will say which
part.** The demand side is stable in a way the corpus would recognise: the world will still
run general-purpose CPUs in datacentres and laptops in 2036, and it will still be a
duopoly-plus-Arm rather than a fragmented market. **What is not stable is Intel's share of
it and the margin it earns** — and that instability is measurable, not mysterious: gross
margin **65.3% (2010) → 55.4% (2021) → 32.7% (2024) → 34.8% (2025)**. **That is a Q2
question about the franchise and a Q4 question about survival, and both are answered below
from filed series. It is not an understanding failure, and pushing it up to Q1 would be
using UNKNOWABLE to avoid arithmetic I am able to do.**

**[E4-46] checked** — *"if we can't make a decision in five minutes, we can't make it in
five months."* This did not take months. The segment note does the hard part: it splits a
profitable design company from a loss-making factory, and it does it for three years.

**[E3-47] checked, and it is the reason the verdict is IN rather than UNKNOWABLE:**
*"our most egregious mistakes fall in the omission, rather than the commission, category…
their invisibility does not reduce their cost."* Closing a file at Q1 on a company whose two
halves are separately filed and separately measured would be dignifying difficulty as
judgment. **Asked aloud: can I name the document that would resolve this?** I did not need
to — the document is Note 3, and it is in hand.

- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

*Two businesses, so [E3-03] is applied twice **[E5-37]** — *"different numbers are of
different importance … depending on the kind of business."* The x86 product franchise is the
claim the brief names; the foundry is the claim management makes.*

### [E3-03] APPLIED TO INTEL FOUNDRY — IT FAILS ON ONE FILED SENTENCE

> "**We have been unsuccessful to date in securing any significant external foundry
> customers for any of our nodes** and our prospects for securing a significant external
> foundry customer for Intel 14A are **uncertain**." — FY2025 10-K, Risk Factors, p.39

**External foundry revenue: $547M (2023) → $159M (2024) → $307M (2025).** Down 44% over
three years, on **$112,121M of capital expenditure over FY2021-25.**

**AND THE 2026 "GROWTH" IS NOT THIRD-PARTY DEMAND.** H1 2026 external foundry revenue rose to
$467M from $53M — and the 10-Q says why: *"primarily due to **Altera's transition to an
external customer following the deconsolidation of Altera in Q3 2025**."* **The foundry's
largest new external customer is Intel's own former subsidiary, reclassified.** Criterion (1) —
*needed or desired* — is not met by anybody who has signed. **This half of the company is
not a franchise; it is a hypothesis, and its own filing rates the hypothesis "uncertain."**

**The filed consequence is the sharpest sentence in the document:**

> "**If we are unable to secure a significant external customer for our Intel 14A node, we
> may pause or discontinue development of Intel 14A and subsequent next generation
> leading-edge nodes.**" — same page

**A business whose own 10-K contemplates abandoning the technology that is its entire
strategic premise has not established a moat around it.**

### [E3-03] APPLIED TO THE x86 PRODUCT FRANCHISE — AND THIS IS THE REAL QUESTION

| criterion | verdict | filed evidence |
|---|---|---|
| **(1) needed or desired** | **YES, emphatically** | $49,147M of revenue; three customers = 43% of net revenue; *"Market demand exceeded our available product supply"* in **both** segments in Q2 2026 |
| **(2) no close substitute** | **NO — and Intel says so** | see below |
| **(3) not price-regulated** | **YES** | no price regulation; the constraint is a CHIPS-agreement dividend prohibition, which is not price regulation |

**Criterion (2), in the registrant's own risk factors, is a list of substitutes and a
confession of share loss:**

> "**we have lost market share in recent years, including in both client and data center
> markets, in the market for x86-based semiconductor products**, and more generally in the
> markets for semiconductor compute products, as competitors have introduced highly
> competitive data center and client platform products. Our data center business has been
> further negatively impacted … by the significant shift of customer spend toward GPUs
> optimized for AI workloads, a rapidly developing and very significant compute market where
> **we have been unsuccessful to date in becoming a meaningful participant**."

Intel names the substitute classes itself: **AMD** (*"which like us designs processors based
on the x86 architecture"* — a literal drop-in), **Arm** (*"Apple with its M series products,
Qualcomm with its Snapdragon products and MediaTek with its Kompanio products"*),
**hyperscaler in-house silicon** (*"many hyperscalers such as Amazon, Google, Meta and
Microsoft"*), **Nvidia**, **Broadcom** in custom ASICs, and **RISC-V**. This is the QCOM
shape — the closest substitutes are built by the largest customers — at ten times the
revenue.

### THE ACLS TEST, WHICH THE BRIEF NAMES: **DID PRICE AND MARGIN HOLD THROUGH THE VOLUME LOSS?**

**PRICE: mostly yes, and in 2026 spectacularly so. MARGIN: no, and the gap between those two
answers is the whole file.**

**The physical series [E4-55] — Intel publishes volume and ASP as percentage changes in
every MD&A vintage. Recorded sweep FY2021–Q2 2026, no absolute unit count is published in
any vintage; the percentage series is the honest physical record and it is used here.**

| year | client/notebook volume | client ASP | server volume | server ASP | filed reason for the ASP move |
|---|---|---|---|---|---|
| 2021 | notebook **+8%**, desktop +8% | notebook **−6%**, desktop +3% | DCG revenue −1% | **lower** | *"product mix and a competitive environment"* |
| 2022 | notebook **−36%**, desktop −19% | notebook **+15%**, desktop +5% | decreased | **decreased** | *"customer and product mix"* |
| 2023 | notebook −5%, desktop −9% | notebook −5%, desktop +5% | decreased (DCAI −20%) | **higher** | *"lower mix of hyperscale … higher mix of high core count"* |
| 2024 | client **+7%** | **flat** | **−8%** | **+11%** | *"lower demand **in a competitive environment**"* |
| 2025 | client **down** | **flat** | **+9%** | **−4%** | *"**pricing actions** taken … driven by **a competitive environment**"* |
| **H1 2026** | client **−10%** | **+22%** | **+2%** | **+38%** | *"**primarily … a higher mix of premium products**, with demand-based pricing actions contributing **to a lesser extent**, in part to offset **higher input costs**"* |

**The answer to the brief's question, stated plainly:**
1. **In 2024 Intel raised server prices 11% while server volume fell 8%.** That is price
   holding through a volume loss — the ACLS pass shape.
2. **In 2025 Intel gave it straight back**: server ASP **−4%**, volume **+9%**, and the
   filed reason is *"pricing actions … driven by a competitive environment."* **Intel bought
   the volume back with price, and said so.** That is **[E4-37]'s agony end** —
   *"it's not a great business when you have to have a prayer session before you raise your
   prices a penny"* — recorded in the filing rather than inferred.
3. **In H1 2026 the ASPs explode (+38% server, +22% client) while volumes fall** — and the
   filing attributes it *primarily to mix*, with real pricing *"to a lesser extent"* and
   *"in part to offset higher input costs."* **A price rise that offsets an input-cost rise
   is not pricing power; it is pass-through.**

**MARGIN — AND THIS IS WHERE THE ANSWER IS UNAMBIGUOUS. The margin did not hold.**

| | 2010 | 2016 | 2019 | **2021** | 2022 | 2023 | **2024** | **2025** | Q2 2026 |
|---|---|---|---|---|---|---|---|---|---|
| **gross margin** | **65.3%** | 61.0% | 58.6% | **55.4%** | 42.6% | 40.0% | **32.7%** | **34.8%** | **40.4%** |
| operating margin | 35.7% | 22.1% | 30.6% | 24.6% | 3.7% | 0.2% | **−22.0%** | −4.2% | +11.1% |
| R&D % of revenue | 15.1% | 21.4% | 18.6% | 19.2% | 27.8% | 29.6% | **31.2%** | 26.1% | 20.9% |
| **revenue $M** | 43,623 | 59,387 | 71,965 | **79,024** | 63,054 | 54,228 | 53,101 | **52,853** | 16,128 |

**Gross margin fell 20.6 points from 2021 to 2025 while revenue fell 33.1%. That is the
[E2-58] commodity equation running in the open** — *"persistent over-capacity without
administered prices (or costs) equals poor profitability"* — except the over-capacity is
Intel's own.

### WHERE THE MARGIN WENT, AND IT IS NOT WHERE A LAZY READ WOULD PUT IT

**The x86 product margin held. The manufacturing margin did not exist.** Filed segment
operating margin:

| | 2023 | 2024 | 2025 | H1 2026 |
|---|---|---|---|---|
| **Intel Products** (CCG/CCPG + DCAI) | **23%** | **26%** | **26%** | **32%** |
| **Intel Foundry** | **−38%** | **−77%** | **−58%** | **−40%** |

**And the transfer price is not the trick.** FY2025 10-K, Note 3, verbatim: *"**Intersegment
sales are recorded at prices that are intended to approximate market pricing.**"* The
Products segments are *"meant to reflect separate fabless semiconductor and foundry
companies."*

**Therefore the single most important derived number in this file: Intel Foundry spent
$28,144M of cost of sales and operating expenses in 2025 to produce $17,826M of output
valued at market. It costs Intel roughly $1.58 to make $1.00 of wafer that anyone can buy
from TSMC for $1.00.** The scarce input Q1 identified — leading-edge logic manufacturing in
the United States — **is one Intel cannot make at a competitive cost, on its own filed
numbers, at market prices it set itself.**

### [E4-04] — THE MOAT THAT MUST BE CONTINUOUSLY REBUILT. **THIS IS THE FINDING.**

> "A moat that must be **continuously rebuilt** will eventually be no moat at all."

The framework's own scoping test: *"does a lapse in spending destroy the structure, or
merely narrow it — and does the spending defend the same advantage, or buy its
replacement?"* Coca-Cola's advertising defends the **same** trademark; Mitsui's Rhodes Ridge
buys a **replacement** deposit.

**Intel's $20-25bn a year buys a replacement, and Intel's own 10-K says a lapse destroys the
structure rather than narrowing it:** *"we may **pause or discontinue** development of Intel
14A and subsequent next generation leading-edge nodes."* A process node has a useful
competitive life of roughly two years and must then be wholly replaced at a cost larger than
the last one. **This is the excluded class by the framework's own definition, and Intel is
the cleanest example of it the queue has produced.**

**[E3-51] — AND THE 2026 RECOVERY IS A SURFING RUN, WHICH IS THE HONEST READ OF THE BEST
NEWS IN THE FILE.** *"when a surfer gets up and catches the wave … he can go a long, long
time. But if he gets off the wave, he becomes mired in shallows … the advantage lives in
the wave, not the surfer."* The H1 2026 ASP explosion happens in a period Intel describes
as one where *"**Market demand exceeded our available product supply**"* and *"we expect
**industry-wide supply constraints** to persist into next year."* **An industry-wide capacity
shortage lifts every supplier's price. It is [E4-36]'s fourth cause of extreme success —
wave-riding — and it is the one cause that is not ownable.**

### [E4-32] DIRECTION OUTRANKS EXISTENCE — EVERY FILED DIRECTIONAL METRIC POINTS ONE WAY

| metric | direction over the filed window |
|---|---|
| x86 share, client and data centre | **DOWN** — *"we have lost market share in recent years"*, Intel's words |
| gross margin | **DOWN** 65.3% → 34.8% (2010→2025) |
| revenue | **DOWN** $79,024M → $52,853M (2021→2025) |
| external foundry revenue | **DOWN** $547M → $307M (2023→2025) |
| return on unleveraged net tangible operating assets **[E2-43]** | **DOWN** 29.2% (2019) → 24.2% (2021) → **−1.9%** (2025) |
| AI accelerators | *"**unsuccessful to date in becoming a meaningful participant**"* |
| dividend | **suspended**, Q4 2024, and contractually prohibited for two more years |

**The one metric pointing up is 2026 pricing, and the filing attributes it primarily to mix
and to an industry-wide supply shortage.**

### [E3-33] UNTAPPED PRICING POWER — THE INVERSE FIRES INSTEAD

Could a manager raise the return simply by raising prices, and has not? **No** — and the
test's own scope forbids claiming it here: *"If you name some business that has incredible
pricing power, you're talking about a business that's **a monopoly or a near monopoly**"*
**[E5-28]**. Intel's own filing says it lost share to a direct architectural clone. **The
inverse metric [E4-37] is what actually fires: 2025's "pricing actions … driven by a
competitive environment" is the prayer-session end of the scale, recorded by the company.**

### THE COMPETITOR ROW — REQUIRED **[E3-28]**. Same metric, same window, filing-sourced.

*A moat is a claim about relative position and cannot be evidenced from one company's
numbers. **Seven peers taken**, in two groups, because Intel competes in two industries.*

**GROUP 1 — THE x86 / COMPUTE PRODUCT ROW. GROSS MARGIN, THE METRIC THE BRIEF NAMES.**

| gross margin % | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | source |
|---|---|---|---|---|---|---|---|---|
| **INTC** | **58.6** | 56.0 | **55.4** | 42.6 | 40.0 | **32.7** | **34.8** | 10-K, `GrossProfit`/`Revenue` |
| **AMD** — the [E2-45] attacker of record | **42.6** | 44.5 | 48.2 | 44.9 | 46.1 | 49.4 | **49.5** | 10-K, CIK 0000002488 |
| **TXN** — IDM comparator | 63.7 | 64.1 | 67.5 | 68.8 | 62.9 | 58.1 | 57.0 | 10-K |
| **MU** — US IDM comparator | 45.7 | 30.6 | 37.6 | 45.2 | −9.1 | 22.4 | 39.8 | 10-K |
| **NVDA** | 62.0 | 62.3 | 64.9 | — | — | — | — | 10-K *(annual-duration facts tagged only through FY2021 in XBRL; not pursued further — Nvidia is a comparator for AI accelerators, not for x86, and Intel's own filing concedes that market outright)* |

| revenue $M | 2019 | 2025 | change |
|---|---|---|---|
| **INTC** | **71,965** | **52,853** | **−26.6%** |
| **AMD** | 6,731 | **34,639** | **+414.6%** |

**THE TWO NUMBERS THAT DECIDE Q2:**
1. **In 2019 Intel's gross margin was 16.0 points ABOVE AMD's. In 2025 it is 14.7 points
   BELOW it. A 30.7-point relative swing in six years, on the same metric, same window,
   both filing-sourced.**
2. **In 2019 Intel's revenue was 10.7x AMD's. In 2025 it is 1.53x.** AMD earned that on
   **$974M of 2025 capital expenditure against Intel's $17,672M — 5.5% of it.**

**THE TEN-YEAR VIEW IS WORSE THAN THE SIX-YEAR VIEW, and it is the honest window
[E4-38] — publish every window, do not select one:**

| gross margin % | **2016** | 2025 | swing |
|---|---|---|---|
| **INTC** | **61.0** | **34.8** | **−26.2 points** |
| **AMD** | **23.1** | **49.5** | **+26.4 points** |
| **TSMC** | 50.1 | **59.9** | **+9.8 points** |
| **relative INTC vs AMD** | **INTC +37.9 ahead** | **INTC 14.7 behind** | **a 52.6-POINT REVERSAL** |

**AND THE SEGMENT TABLES NOW CROSS. FY2025, both filed:**

| | Intel **DCAI** | AMD **Data Center** |
|---|---|---|
| revenue | **$16,919M** | **$16,635M** |
| operating income | **$3,422M** | **$3,603M** |

**AMD's data-centre segment did not exist as a reportable segment in FY2019. In FY2025 it
earns MORE operating income than Intel's does, on 98.3% of the revenue — and it does it
with no fabs.** *(AMD Data Center revenue $1,685M (FY2020) → $16,635M (FY2025); operating
income $198M → $3,603M. Accessions 0000002488-23-000047, -25-000012, -26-000018.)*

### **THE ATTACKER STOPPED CALLING INTEL THE LEADER — AND THE DATE IS RECORDED**

**A recorded sweep of all seven AMD 10-Ks, FY2019 through FY2025, found this sequence in
AMD's own competition risk factor:**

| AMD 10-K vintage | how AMD describes Intel |
|---|---|
| **FY2019 – FY2022** | *"Intel Corporation has been **the market share leader for microprocessors** for many years"* |
| **FY2023 – FY2024** | *"Intel's microprocessor market share **position**"* — the leadership claim deleted, never restored |
| **FY2025** | **"share" dropped for Intel entirely** (*"market **position**"*), and a **dedicated Nvidia share risk factor** appears |

**The competitor's own filed language is a dated, adversarial, self-interested record — and
it stopped conceding leadership in the FY2023 vintage. An attacker has every incentive to
describe the incumbent as dominant (it is a risk factor). AMD stopped.**

**[E4-55] AND THE ABSENCE IS ITSELF THE FINDING, worded per the absence-claim rule.**
Recorded sweep of all seven AMD 10-Ks for "share gains", "gained share", "unit share",
"revenue share", "leadership share", "share growth": **no instance found in which AMD states
a share percentage for its own server, client or x86 processors.** The only share leadership
AMD claims for itself in any year is **game consoles**. **So the x86 share percentage is
UNKNOWABLE from the shelf this project uses — no filing states it.** The finding above rests
instead on two things that ARE filed: **Intel's own admission that it "lost market share …
in both client and data center markets", and the two segment tables, which have crossed.**

**[E2-45], the attacker's test — *"how I would like, assuming I had ample capital and skilled
personnel, to compete with it."* The corpus's one forward-looking moat test does not need to
be imagined here: the attack has already been run, it is filed, and it worked.** AMD is not
a hypothetical; it is a company with the identical instruction set, a higher gross margin, a
fifth of Intel's revenue growing five-fold, and no fabs.

**GROUP 2 — THE FOUNDRY ROW. This is the business management says Intel is becoming.**

| | gross margin % 2024 | gross margin % 2025 | operating margin % 2024 | operating margin % 2025 | revenue $M, latest |
|---|---|---|---|---|---|
| **TSMC** (20-F, CIK 0001046179, IFRS) | **56.1** | n/a¹ | **45.7** | n/a¹ | 88,268 (2024) |
| **UMC** (20-F, trailing-edge) | 32.6 | n/a¹ | 22.2 | n/a¹ | 7,085 (2024) |
| **GlobalFoundries** (20-F) | 24.5 | 24.9 | −3.2 | 11.7 | 6,791 (2025) |
| **INTEL FOUNDRY** (10-K segment, Note 3) | — | — | **−76.8**² | **−57.9**² | **17,826 (2025)** |

¹ *TSMC's and UMC's FY2025 20-F annual facts were not present in the SEC XBRL frames at
run time; the 2024 column is the latest filed and it is sufficient — the gap between +45.7%
and −57.9% is not a rounding question.*
² *Intel does not publish a foundry gross margin. Operating margin computed from the filed
segment table: 2025 (10,318)/17,826; 2024 (13,291)/17,317.*

**EVERY FOUNDRY IN THE ROW EARNS A POSITIVE GROSS MARGIN, INCLUDING THE WEAKEST —
GlobalFoundries, a trailing-edge specialist that abandoned leading-edge development in 2018,
earns 24.9%. Intel Foundry earns MINUS 57.9%, on revenue Intel itself prices at market.**

**Peers taken: 7 of the industry's real competitors** (AMD, TSMC, UMC, GlobalFoundries, TXN,
Micron, Nvidia-partial). *Buffett says eight.*

**PEERS UNAVAILABLE, named with the obstacle [E3-28]:** **Samsung Electronics** — CIK
0000879316 exists but holds only paper SUPPL/ARS filings and 13D/G, **nothing since 2015, no
10-K or 20-F ever, companyfacts 404**; it reports under the **Rule 12g3-2(b) exemption**.
**SK hynix** — CIK 0002120882 is real but the company **only listed in July 2026 via F-1 and
its first 20-F is not yet due**; companyfacts holds five fee-table facts and zero financials.
**SMIC** — not an SEC registrant. **No SEC filing exists to pull for any of the three.** Under the four-verdict test that is **UNKNOWABLE, not
UNRESEARCHED** (the queue's standing treatment for non-registrants). **This does NOT make
the moat class PROVISIONAL in the direction that matters:** the two missing names are
**additional competitors**, and adding a competitor cannot widen a moat. The row is
sufficient to refuse an IN; it would not be sufficient to grant one.

**[E3-61] — THE ROW'S LIMIT, STATED.** *"In some businesses, the participants behave like a
demented Kellogg… I think you'd have to know the people involved."* The row shows position,
not conduct. What it cannot tell me is whether TSMC will price rationally if Intel exits
leading-edge. **That limit does not rescue Intel: the row's finding is about Intel's own
cost, not about others' conduct.**

### CLASS AND DIRECTION

- Class: [ ] WIDE  [ ] NARROW  [x] **NONE, at the company level** · Direction: **NARROWING on
  every filed metric except 2026 pricing, which the filing attributes primarily to mix and
  to an industry-wide supply shortage.**
- **The residual is real and is recorded rather than denied:** the x86 *ecosystem* still has
  switching friction — demand exceeded supply in both segments in H1 2026, and nobody walked
  to AMD. **But an advantage that shows up only when the whole industry is short of capacity
  is [E3-51]'s wave, not [E4-32]'s moat.**

### **VERDICT: [x] OUT**

**THE REASONING, STATED SO IT CAN BE CHECKED RATHER THAN TRUSTED. Four independent grounds,
any one of which would close Q2, and none of which requires a forecast:**

1. **[E3-03] criterion (2) fails on the registrant's own words.** *"we have lost market share
   in recent years, including in both client and data center markets"*; *"unsuccessful to
   date in becoming a meaningful participant"* in AI accelerators. Intel names AMD, Arm,
   Apple, Qualcomm, MediaTek, Nvidia, Broadcom, RISC-V and its own hyperscaler customers as
   the substitutes. **A franchise is a product *"thought by its customers to have no close
   substitute."* Intel's customers build the substitute.**
2. **[E4-04], and this is the sharpest ground.** The moat is process leadership; process
   leadership must be **wholly replaced every node at rising cost**; Intel lost it; and
   Intel's own 10-K contemplates *"pause or discontinue development of Intel 14A and
   subsequent next generation leading-edge nodes."* **A lapse in spending here destroys the
   structure rather than narrowing it — the framework's own test for the excluded class.**
3. **The competitor row inverts.** A **52.6-point** relative gross-margin reversal against the
   attacker over the filed ten-year window (INTC 37.9 points ahead in 2016, 14.7 behind in
   2025), and AMD's data-centre segment now out-earns Intel's, and revenue multiple 10.7x → 1.53x. **This is not a moat that narrowed; it is
   one that changed sides.**
4. **The foundry claim has no customers.** *"We have been unsuccessful to date in securing
   any significant external foundry customers for any of our nodes."* External revenue
   $547M → $307M over three years, against $112,121M of capital expenditure.

**WHY OUT AND NOT "NARROW, CONTINUE TO Q4", WHICH IS WHAT ORCL GOT.** Oracle's Q2 was IN
(NARROW, narrowing) because its database annuity is a **defended** moat — $19.8bn of support
revenue that does not need rebuilding, only maintaining. **Intel's advantage is the
[E4-04]-excluded kind: its basis must be periodically replaced, and the replacement has
already failed twice** (10nm, 7nm) **at a cost the filing puts at $112bn.** The distinction
is not degree; it is class.

**[E4-18] CHECKED: this verdict did not require fighting for it.** It holds on the
company's own risk factors alone, before any peer number is pulled; the row confirms it
rather than producing it. **[E4-26] CHECKED — the disconfirming case was hunted hardest and
is stated in full at the end of this file, not buried: H1 2026 server ASPs +38%, Intel
Products operating margin 32%, demand exceeding supply, Q2 2026 consolidated operating
income +$1,796M. I have weighed it and it does not change the class — it changes the
cycle.**

---
⛔ **THE HARD SEQUENCE. Q2 RETURNED OUT. THE FILE IS CLOSED, PERMANENTLY, ON THE BUSINESS.**
Operator rule 2: *"No Q5 output may be reported unless Q1-Q4 each show IN."* Everything below
is **recorded evidence and arithmetic. None of it is a verdict and none of it confers any
clearance.**

---

## Q3 — NOT REACHED. Q2 closed the file.

**Evidence gathered before the close is recorded rather than discarded, because the brief
earned these tests and because an addendum is the only honest place to correct a run
(operator rule 6). NO Q3 VERDICT IS WRITTEN AND NONE SHOULD BE INFERRED.**
Full working file: `Test Runs/_research 2026-09-07 INTC/q3_evidence.md`.

**Weight case, had it been reached:** **BINARY GATE** — *daily execution* **[E3-38]** ticked
(a company that must hit a two-year node cadence is have-to-be-smart-every-day) and
*leverage* **[E3-29]** ticked ($50,537M of debt, tangible equity thin once $23.9bn of
goodwill is removed).

**WHAT WOULD HAVE COUNTED AGAINST — all filed:**
- **[E4-52] THE RESTRUCTURING STREAK, and it is a lollapalooza of one behaviour repeated.**
  **Three plans in four years**: 2022 Restructuring Program (~$1.3bn, complete Q1 2024),
  **2024 Restructuring Plan**, **2025 Restructuring Plan**. **Severance alone: $1,038M
  (2022), $222M (2023), $2,481M (2024), $1,790M (2025), $235M (H1 2026) — ~$5.8bn in four
  and a half years.** **[E3-53]** is directly on point: *"a large chunk of costs that should
  properly be attributed to a number of years is dumped into a single quarter."*
- **The 2024 plan's own cost estimate rose in every successive filing: $3.0bn (FY2024 10-K)
  → $3.1bn (FY2025 10-K) → $3.2bn (Q2 2026 10-Q)**, and a plan announced Q3 2024 as
  *"substantially complete by the fourth quarter of 2025"* is now *"expected to be completed
  in 2026"* — with two further plans layered on top of it.
- **[E2-49] METRIC-SWITCHING, four times in three years.** Segment structure changed in
  **FY2024** (internal foundry model; Altera out of DCAI), **FY2025** (NEX dissolved into
  CCG and DCAI, **$2.78bn of goodwill reallocated**), **FY2026** (CCG → **CCPG**, "Physical
  AI" added to the PC segment's name) — each with prior periods *"retrospectively
  adjusted."* **And the segment MEASURE changed too: FY2024 disclosed segment GROSS MARGIN;
  FY2025 does not**, and *"Prior to the second quarter of 2025, our CODM regularly reviewed
  cost of sales and operating expenses, on a discrete basis, attributable to each segment.
  We have recast prior period segment operating results."* **No reported segment series
  survives two years on a consistent basis.**
- **THE APOLLO ROUND TRIP — the single sharpest capital-allocation fact in the file
  [E2-29, E2-30].** Q2 2024: sold 49% of Ireland SCIP (Fab 34) to Apollo for **$11.0bn net
  proceeds**, credited to capital in excess of par. **8 April 2026: bought the identical 49%
  back for $14.2bn cash**, $13.5bn of it debited to capital in excess of par. **A $3.2bn
  gross cash cost in 23 months, plus a $755M liquidated-damages derivative loss and $365M of
  distributions paid to Apollo along the way — and NOT ONE DOLLAR OF IT TOUCHED THE INCOME
  STATEMENT.** Both legs are financing cash flows and equity entries.
- **THE ASYMMETRY IS THE TELL [E2-26].** The **$5.6bn GAIN** on the Altera disposal ran
  **through earnings** (in *interest and other, net*). The **$3.2bn COST** of the Apollo
  round trip ran **through equity**. Favourable non-operating item in the income statement;
  unfavourable one in capital in excess of par.
- **THE NON-GAAP MEASURE, and this is where it bites.** *"Adjusted Free Cash Flow …
  calculated using cash flow from operations and adjusted for … additions to property,
  plant and equipment, **net of proceeds from capital-related government incentives and net
  SCIP partner contributions**."* **Intel's headline cash measure subtracts SCIP partner
  money from capex — and Ireland SCIP has now proved that partner money is borrowed, at a
  $3.2bn premium.** In FY2024 the definition also added back *"proceeds from the McAfee
  equity sale in 2022"* ($4,561M) inside a measure named *free cash flow*; that clause and
  the 2022 column were both removed in FY2025. **[E4-38]:** the FY2024 10-K showed **five
  years** of the measure; FY2025 shows **three** — dropping the only two positive years
  (2020: +$21,778M; 2021: +$10,889M).
- **[E5-15] SERIAL SHARE ISSUANCE.** 4,137M shares (Dec 2022) → **5,043M (Jun 2026)**,
  **+21.9%**, including 275M to the DOC, 159M into escrow, 87M to SoftBank at $23.00 and
  215M to Nvidia at $23.28. **All of it sold at $20-23 into a stock now quoted at $95.80.**
- **PAY VERSUS PERFORMANCE (DEF 14A, filed 2026-03-23).** **Three PEOs in one year.** CEO
  Lip-Bu Tan: **Summary Compensation Table total $92,990,900; Compensation Actually Paid
  $161,645,068** — in a fiscal year with a **$(2,214)M operating loss** and **$(267)M of net
  loss attributable to Intel**. Michelle Johnston Holthaus $33.1M SCT / $55.9M CAP; David
  Zinsner $18.2M SCT / $31.3M CAP. **The Company-Selected Measure is "Revenue (Non-GAAP)"**,
  and the three most important measures are **Revenue, Gross Margin Percentage and Relative
  TSR** — *revenue sits above every cost this company has failed to control*, which is the
  TXN finding repeated at forty times the scale. *(The CAP figure is an honest
  mark-to-market of a 2025 mega-grant as the stock rose; recorded as structure, not as a
  fraud claim [E5-38].)*
- **[E2-60] RESTRICTED EARNINGS — and this one resolves in management's favour, so it is
  recorded as such.** *"a company that consistently distributes restricted earnings is
  destined for oblivion."* **Intel stopped.** Dividend $1.46/sh (2022) → $0.74 (2023) →
  $0.38 (2024) → **$0.00 (2025)**; buybacks ceased after Q1 2021. **The distribution was cut
  before the balance sheet was destroyed, which is the correct direction.**

**WHAT WOULD HAVE COUNTED IN MANAGEMENT'S FAVOUR — and it is not trivial [E4-26]:**
- **[E4-29] DOES NOT FIRE. Recorded sweep: "EBITDA" returns ZERO hits in the FY2025 10-K,
  the FY2024 10-K, the Q2 2026 10-Q and the 2026 proxy.** Intel does not promote EBITDA
  anywhere. On the corpus's most-repeated disclosure tell, the filings are clean.
- **[E4-22]'s PROJECTIONS FLAG DOES NOT FIRE, and this is remarkable.** Recorded sweep:
  **no revenue, gross-margin, operating-margin, EPS or free-cash-flow target appears
  anywhere in the FY2025 10-K.** *"Five nodes in four years"* — **zero hits in all four
  documents.** *"On track"* appears only inside the forward-looking-statements boilerplate
  word list. **[E5-30]'s ratchet is not running here.** The forward statements that do exist
  are hedged and directional.
- **The Tower failure is described candidly** — *"our inability to timely obtain required
  regulatory approvals"*, $353M break fee, blame taken rather than deflected. This is the
  opposite of the **[E2-57]** except-for flag.
- **The liquidity language is honest about its own dependence** and, unlike Oracle's, keeps
  the supplements outside the primary claim: *"Our primary sources of liquidity are cash
  generated by operations and our total cash and short-term investments, **supplemented by**
  undrawn committed credit facilities …"*
- **THE ABSOLUTE-SIZE ACQUISITION GATE: PASSES CLEANLY.** Acquisitions net of cash acquired
  **$681M (2022), $13M (2023), $82M (2024), nil (2025), $596M (H1 2026)** — **~$1.37bn in
  four and a half years against $211bn of assets.** The $596M is **Mobileye's** purchase of
  Mentee Robotics, not Intel's. **[E2-30](2) — projects materialising to soak up available
  funds — does not fire through M&A.** Intel's capital went into fabs, not empire-building.
  *(One open item: the FY2025 10-K announced Mentee at ~$900M; the Q2 2026 10-Q records the
  closed price at $637M. A 29% gap with no reconciliation. **UNRESEARCHED**, resolvable from
  Mobileye's own filing or the transaction 8-K.)*
- **ASC 842: IMMATERIAL, CONFIRMED.** Operating leased assets **$421M**, total operating
  lease liabilities **$391M** — **0.19% of $211.4bn of assets**. Finance leased assets
  $453M; undiscounted finance lease payments $133M total. **No hidden off-balance-sheet
  lease obligation of any size.** *(One anomaly recorded: **$832M of finance-lease payments
  in H1 2026 against a disclosed total remaining obligation of $133M** — 6.3x. The 10-Q's
  entire explanation is *"higher payments on finance leases."* **UNRESEARCHED**; the FY2026
  10-K lease note or the Q3 2026 10-Q resolves it.)*
- **ONE FURTHER OPEN ITEM, NAMED: Pat Gelsinger's December 2024 separation terms are NOT
  in the 2026 proxy** (all ten `Gelsinger` hits in it are Pay-versus-Performance data).
  **UNRESEARCHED** — the 2025 DEF 14A (accession `0000050863-25-000054`) or the departure
  8-K resolves it. It does not bear on the Q2 verdict.
- **SOFTWARE CAPEX: IMMATERIAL.** Recorded sweep: `350-40`, `985-20` and "capitalized
  software" return **zero hits**. The maximum ever disclosed is **$128M gross** of
  internal-use software (FY2024, since folded into "Licensed technology, patents and
  other") — **0.06% of assets.** No earnings flattery here.
- **CONTINGENT-LIABILITY PERSISTENCE: PRESENT BUT SMALL.** EC fine $401M accrued 2023,
  reduced $163M in 2025, unpaid on appeal, third-party guaranteed with $340M deposited in
  restricted accounts; VLSI and R2 Semiconductor patent litigation (R2 obtained a German
  injunction in Feb 2024); MCP claiming $66M-$398M; a securities class action over the
  **foundry segment reporting itself** — and a federal court **twice found that plaintiffs
  failed to plead any false or misleading statement**, which is a point in management's
  favour and is recorded as one; it is on appeal. **Nothing here is material against a
  $490bn quote.**
- **[E4-30] CASH-TAX TELL: RUNS THE OPPOSITE WAY, AND IT IS DISCLOSED.** Cash income tax
  paid **$4,282M / $2,621M / $2,202M / $2,299M (2022-25) plus $904M in H1 2026 = $12,308M of
  cash tax against $(15,888)M of cumulative pre-tax loss.** Intel pays cash tax abroad while
  losing money in the US, and a full **domestic valuation allowance** ($9.9bn charged in
  2024; $16.4bn cumulative) blocks any benefit. **This is not soft earnings; it is a US business losing money at
  a scale that has already written off its own deferred tax assets.**

## Q4 — NOT REACHED. Q2 closed the file.

**The brief specifically requested the ORCL measurement. It is run and reported here as
arithmetic only. IT IS NOT A VERDICT.**

### THE ORCL MEASUREMENT, RUN ON INTEL

**1. [E2-56] INCREMENTAL PRE-TAX RETURN ON CAPITAL DEPLOYED OVER FIVE YEARS — the read the
corpus requires, never the blended one.**

| | ORCL (2026-09-06) | **INTC** |
|---|---|---|
| capital deployed, 5 years | $160,283M | **$112,121M of capex FY2021-25, plus $14,200M paid to Apollo = $126,321M** |
| change in operating income | **+$5,393M** | **−$21,670M** (FY2021 $19,456M → FY2025 $(2,214)M) |
| **incremental pre-tax return** | **3.4%** | **NEGATIVE. There is no rate.** |

Measured from the FY2020 peak it is worse: operating income **$23,678M → $(2,214)M**, a
**$25,892M decline**. Measured to the **TTM**, operating income is **$(77)M** — still
negative. **Gross profit $43,612M (2020) → $22,017M (TTM): down $21,595M on $112bn of
capital.** **Against [E5-40]'s ~12% "quite satisfactory" and [E4-43]'s 20.5% *good*-class
illustration, Intel's incremental return does not reach zero.** [E4-20]'s escape clause —
*"unless the cash they consume gets to earn a reasonable return"* — is not available.
**Return on unleveraged net tangible operating assets [E2-43]: 29.2% (2019) → 27.3% (2020)
→ 24.2% (2021) → 2.6% → 0.1% → −10.2% (2024) → −1.9% (2025).**

**2. [E2-54] COVERAGE NET OF CAPEX — *"all interest, both payable and accrued … comfortably
met out of current cash flow net of ample capital expenditures."***

| FY | OCF | total capex | OCF − capex | interest **incurred** (net-of-capitalised + capitalised) | coverage |
|---|---|---|---|---|---|
| 2021 | 29,456 | 18,733 | **+10,723** | 545 (cash) | 19.7x |
| 2022 | 15,433 | 24,844 | **−9,411** | — | **NEGATIVE** |
| 2023 | 11,471 | 25,750 | **−14,279** | 878 + 1,500 = **2,378** | **NEGATIVE** |
| 2024 | 8,288 | 25,122 | **−16,834** | 1,034 + 1,500 = **2,534** | **NEGATIVE** |
| 2025 | 9,697 | 17,672 | **−7,975** | 1,091 + 1,200 = **2,291** | **NEGATIVE** |
| **TTM** | **14,936** | **14,592** | **+344** | ~2,300 | **0.15x** |

**Four consecutive negative years, and the TTM recovery reaches 0.15x on interest actually
incurred. "Comfortably met" it is not.** *(Capitalised interest is included because [E2-54]
says "both payable and accrued"; Intel capitalised **$1.2bn in 2025 and $1.5bn in each of
2024 and 2023**. Total capex includes the PP&E additions Intel reports in **financing**
activities — $1,178M in 2024, $3,026M in 2025, $1,423M in H1 2026 — which the screen's
`PaymentsToAcquirePropertyPlantAndEquipment` tag misses entirely.)*

**3. [E5-11] THE THREE STRENGTHS, AND THE ANSWER IS NOT ORACLE'S.**

- **(1) A large and reliable stream of earnings — LARGE YES, RELIABLE NO.** Operating income
  $19,456M → $2,334M → $93M → $(11,678)M → $(2,214)M → TTM $(77)M. Net income
  attributable to Intel was **$(18,756)M in 2024** and **$(14,761)M in H1 2026**.
- **(2) Massive liquid assets — REAL, AND LARGELY RAISED.** Cash + short-term investments
  **$37,416M** (Dec 2025) → **$29,727M** (Jun 2026), against **$50,537M** of debt. Plus
  **$8.8bn of AMIC tax receivables**. **But $11,835M of it was equity issued in 2025 and
  $13,000M was term debt issued in H1 2026** — the Oracle pattern.
- **(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — AND HERE INTEL IS **BETTER** THAN
  ORACLE, WHICH IS THE HONEST FINDING AND IS RECORDED AS SUCH.** Twelve-month claims from
  the Jun-27-2026 balance sheet: short-term debt $1,988M + interest ~$2,300M + capex $14,592M
  (TTM; the FY2026 commitment was $9,100M) + other purchase obligations $2,200M + Mentee
  $900M = **~$21,980M**, against cash+STI $29,727M plus TTM OCF $14,936M = **$44,663M —
  covered 2.03x**. **Even assuming Arizona SCIP is bought back on the Ireland precedent
  (~$14bn against a $13,428M carrying value), it is covered 1.24x.**
  **Oracle failed this test with an ~$80.7bn requirement against $63.9bn. Intel passes it.
  The difference must be stated, not glossed: Intel can stop building; Oracle had contracted
  not to.** *(Remaining unfunded Arizona SCIP contribution: **$5.2bn**. Arizona carries
  minimum-production covenants with volume-related damages.)*
- **[E5-39] — the kindness of strangers, and Intel is only half-guilty.** The primary
  sufficiency claim rests on operations and cash; credit facilities, future issuances, asset
  monetisation and *"contributions from our Arizona SCIP partner"* are listed as
  **supplements**. Oracle put *"available financing arrangements"* inside the primary claim.
  **Intel's revolver is undrawn ($7.0bn to Feb 2029) and commercial paper is zero.**

**4. GREAT, GOOD OR GRUESOME [E4-20] — GRUESOME, and worse than the category describes.**
*"The worst sort of business is one that grows rapidly, requires significant capital to
engender the growth, and then earns little or no money."* **Intel did not grow. Revenue fell
from $79,024M (2021) to $52,853M (2025) while it consumed $112bn.** The gruesome account
*"both pays an inadequate interest rate and requires you to keep adding money at those
disappointing returns"* — Intel's rate on the added money is below zero.

**5. THE NAMED WAY THIS BUSINESS DIES [E2-27, E3-24, E4-40] — and Intel names it itself.**
**[E4-40] governs the method: model exposure, not experience.**

> "**If we are unable to secure a significant external customer for our Intel 14A node, we
> may pause or discontinue development of Intel 14A and subsequent next generation
> leading-edge nodes.** … In such event, we would expect, over time, to shift manufacturing
> to third-party foundries, **particularly TSMC**." — FY2025 10-K

**Quantified from filed figures.** If Intel becomes a fabless x86 designer buying wafers from
TSMC, the surviving business is Intel Products: **$8,875M of H1 2026 segment operating
income, ~$17,750M annualised, less ~$4,512M of corporate unallocated ex-restructuring =
~$13,238M pre-tax, ~$10,458M after 21% tax.** Against that it must write down some part of
**$105,741M of net property, plant and equipment**, service **$50,537M of debt**, and honour
**$5.2bn of unfunded Arizona SCIP contributions** plus minimum-production covenants on
factories it would no longer need. **Likelihood: a real possibility — Intel elevated it to
the first page of its own risk list.** *(In Q2 2026 Intel "committed to completing
development of Intel 14A" — note the sequence: the commitment was made while customers were
still only *"potential"* and *"evaluat[ing]"*, i.e. before the stated precondition for it was
met.)*

**Second mechanism [E2-27] — collective irrationality, and it is already realised.** TSMC,
Samsung, Intel, Rapidus and SMIC are all adding leading-edge capacity with state money.
*"Viewed individually, each company's capital investment decision appeared cost-effective and
rational; viewed collectively, the decisions neutralized each other."* **Intel's filed share
of the outcome: $112bn deployed, gross margin down 20.6 points, external foundry revenue
$547M → $307M.**

## Q5 — NOT REACHED. Q6 — NOT REACHED.

⛔ **Q5 does not open unless Q1-Q4 each show IN. Q2 is OUT.** The arithmetic below is
published because the queue's output contract requires a price from every run, and it carries
the heading operator rule 3 requires.

---

# COMPUTATION — NOT A CLEARANCE

**This section contains no entry language and confers no clearance. It is arithmetic.**

**Market cap $490,017M** = 5,115M economic shares × **$95.80** (2026-09-04, Yahoo aggregator,
flagged). **Sovereign 5.24%** (US Treasury 30-yr par yield, 2026-09-04, issuing authority).

### EVERY CONSTRUCTION, EVERY WINDOW, BOTH ENDS OF THE BAND

*(OE = operating cash flow − SBC − (c), by hand from the filed cash-flow statements. Capex
end = investing **plus** financing PP&E additions. D&A end = the `Depreciation` line.)*

| FY | OCF | SBC | total capex | depr | **OE, capex end** | **OE, D&A end** | capex/depr |
|---|---|---|---|---|---|---|---|
| 2016 | 21,808 | 1,444 | 9,625 | 6,266 | 10,739 | 14,098 | 1.54 |
| 2017 | 22,110 | 1,358 | 11,778 | 6,752 | 8,974 | 14,000 | 1.74 |
| 2018 | 29,432 | 1,546 | 15,181 | 7,520 | 12,705 | 20,366 | 2.02 |
| 2019 | 33,145 | 1,705 | 16,213 | 9,204 | 15,227 | 22,236 | 1.76 |
| 2020 | 35,864 | 1,854 | 14,259 | 10,482 | **19,751** | **23,528** | 1.36 |
| 2021 | 29,456 | 2,036 | 18,733 | 9,953 | 8,687 | 17,467 | 1.88 |
| 2022 | 15,433 | 3,128 | 24,844 | 11,128 | **−12,539** | 1,177 | 2.23 |
| 2023 | 11,471 | 3,229 | 25,750 | 7,847 | **−17,508** | 395 | 3.28 |
| 2024 | 8,288 | 3,410 | 25,122 | 9,951 | **−20,244** | **−5,073** | 2.52 |
| 2025 | 9,697 | 2,434 | 17,672 | 10,757 | **−10,409** | **−3,494** | 1.64 |
| **TTM** | **14,936** | **2,393** | **14,592** | **11,435** | **−2,049** | **+1,108** | **1.28** |

| window | OE capex end | yield | OE D&A end | yield | value @5.24% | value @10% floor |
|---|---|---|---|---|---|---|
| 3-yr FY2023-25 | −16,054 | −3.28% | −2,724 | −0.56% | — | — |
| **5-yr FY2021-25 (corpus default [E2-42])** | **−10,403** | **−2.12%** | **+2,094** | **+0.43%** | **$7.81/sh** | **$4.09/sh** |
| 7-yr FY2019-25 | −2,434 | −0.50% | 8,034 | 1.64% | $29.97/sh | $15.71/sh |
| 10-yr FY2016-25 | +1,538 | +0.31% | 10,470 | 2.14% | $39.06/sh | $20.47/sh |
| TTM | −2,049 | −0.42% | +1,108 | +0.23% | $4.13/sh | $2.17/sh |
| pre-collapse FY2016-20 (**a different company**) | 13,479 | 2.75% | 18,846 | 3.85% | $70.31/sh | $36.84/sh |
| **FY2020 ALONE at the D&A end — the single most generous number constructible** | — | — | **23,528** | **4.80%** | **$87.78/sh** | **$46.00/sh** |

### **THE ONE SENTENCE THAT PRICES THIS COMPANY**

**The most generous construction obtainable — Intel's best year in history (FY2020), at the
depreciation-only end, which the framework calls INVALID for a capital-intensive filer
[E5-20] — yields 4.80% against a 5.24% sovereign and values the stock at $87.78 against a
$95.80 quote. There is no construction, on any window, at either end of the capex band, that
reaches the government bond.**

### THE BULL CASE, PRICED RATHER THAN DISMISSED [E4-51]

**Value Intel as a fabless x86 designer, giving the entire foundry away for nothing:**
Intel Products H1 2026 operating income $8,875M annualised = $17,750M; less corporate
unallocated **ex-restructuring** $4,512M = **$13,238M pre-tax**; at 21% tax = **$10,458M**.

- **Yield at the quote: 2.13%.**
- **Value at the bare sovereign: $39.02/share. At the [E4-28] floor: $20.45/share.**
- **What this construction gives away free:** the entire Intel Foundry loss (FY2025
  $(10,318)M; H1 2026 $(4,526)M), **$105,741M of net PP&E**, $50,537M of debt and ~$2,300M/yr
  of interest incurred, the $3.9bn H1 2026 goodwill impairment, and it annualises **the best
  half-year Intel Products has ever had.** **It still gives $39.02 against $95.80.**

### WHAT THE PRICE ALREADY ASSUMES

| construction | perpetual growth needed at the **sovereign** | at the **[E4-28] 10% floor** |
|---|---|---|
| 10-yr D&A end ($10,470M) | **3.10%** | **7.86%** |
| fabless bull case ($10,458M) | **3.11%** | **7.87%** |
| TTM D&A end ($1,108M) | **5.01%** | **9.77%** |
| FY2020 best-ever ($23,528M) | 0.44% | 5.20% |

**What the business has actually done, filed:** revenue **−9.6%/yr** over four years
(2021→2025) and **−1.3%/yr** over nine (2016→2025); gross profit **−19.5%/yr**
(2021→2025); operating income negative, so no rate is defined. **[E4-35]'s base rate —
*"fewer than 10 of the 200 most profitable companies"* will compound at 15% for twenty years
— is the standing burden on any growth case, and this one starts from a negative rate.**

### **THE PRICE**

**$95.80** (2026-09-04). **Zero-growth value, judged: roughly $20 to $40 a share at the
[E4-28] floor and the bare sovereign respectively, on the fabless-bull and 10-year
constructions — the two most generous honest reads. The FY2020-alone construction reaches
$88 and it values a company that no longer exists.**

---

## THE SCREEN ROW — REPRODUCED, THEN REBUILT. **BOTH ENDS TIE TO THE DOLLAR, AND BOTH ARE WRONG.**

The tail triage places INTC in **STEP DOWN**, band **−$14,652M to +$2,201M**, with the note
*"the series changed level downward; a tight spread here is not safety."* **Reproduced:**

- **`oe_bottom = −$14,652M` is my 3-year FY2023-25 mean at the INVESTING-CAPEX-ONLY end
  (−14,652.3). Exact to the dollar.**
- **`oe_top = +$2,201M` is my 5-year FY2021-25 mean at the DEPRECIATION end — but only if
  the FY2021 operating cash flow used is the ORIGINALLY FILED $29,991M rather than the
  $29,456M Intel restated it to in the FY2022 10-K. On the restated figure it is +$2,094M.
  The screen is running on a superseded input (2,201.4 vs 2,094.4).**

**SO THE FIFTH SPREAD DEFECT AT A FIFTH NAME IN FIVE DAYS, AND IT HAS A NEW FAILURE MODE ON
TOP OF THE OLD ONE.** The old defect repeats: **the two ends are DIFFERENT WINDOWS** (3-year
against 5-year), so the published "band" is not a band — it is two unrelated statistics.
**The new one: the top end uses a figure the registrant withdrew.**

**Two further screen errors found:**
1. **The capex tag misses a third of the capex.** `PaymentsToAcquirePropertyPlantAndEquipment`
   captures only the **investing** line. Intel also reports PP&E additions in **financing**:
   **$1,178M (2024), $3,026M (2025), $1,423M (H1 2026)**. FY2025 capex is **$17,672M**, not
   $14,646M — the screen understates it by **20.7%**.
2. **The cap is $453,077M against a filed-and-priced $490,017M** — an 8.2% understatement
   from a stale count (4,995M, missing 49M issued since and 71M escrowed) at a stale price.

**AND THE TAIL TRIAGE'S OWN WARNING IS VINDICATED, WITH A CORRECTION.** *"The series changed
level downward; a tight spread here is not safety."* Correct in substance — but the spread
is **not** tight: rebuilt over my own windows the real range runs from **−$16,054M to
+$23,528M, a $39.6bn width.** **And per the ORCL adjudication, width closes a file only when
it straddles the decision. This one straddles nothing: every construction is below the
sovereign.** The width is decision-irrelevant; the verdict rests on Q2, which is a
single-valued reading of the registrant's own risk factors.

---

## **[E4-51] THE STRONGEST FACTS AGAINST THIS CONCLUSION** — *"I'm not entitled to have an opinion unless I can state the arguments against my position better than the people who are in opposition."*

**These are real, they are filed, and I do not think they are answered by anything above.**

1. **THE BUSINESS IS INFLECTING HARD RIGHT NOW, AND THE MOST RECENT FILED QUARTER IS THE BEST
   IN YEARS.** Q2 2026: revenue **$16,128M, +25.4%** year on year; gross margin **40.4%**
   against 27.5%; **operating income +$1,796M** against $(3,176)M. Intel Products operating
   margin **32%**; **DCAI operating margin 40%** against 16%.
2. **PRICING IS THE OPPOSITE OF WHAT A COLLAPSING FRANCHISE LOOKS LIKE.** H1 2026 **server
   ASPs +38%, client ASPs +22%**, and *"Market demand exceeded our available product supply"*
   in **both** segments. **Nobody walked to AMD when Intel could not supply them.** That is
   real switching friction and I have called it a wave; **it may be a moat and I may be
   wrong about which.**
3. **THE CASH TURN IS REAL.** TTM OCF less capex is **+$344M**, the first positive reading
   since 2021; capex has fallen **$25,122M → $17,672M → ~$14,592M TTM**; the balance sheet
   took in **$11,835M of equity** and holds **$8.8bn of AMIC tax receivables** on a credit
   rate just raised from 25% to 35%.
4. **THE US GOVERNMENT IS A ~10% SHAREHOLDER AND HAS REMOVED THE CHIPS MILESTONES.** The
   August 2025 agreement stripped *"substantially all other requirements"* from the CHIPS
   award and accelerated **$5.7bn**. A sovereign with a strategic need for domestic
   leading-edge capacity is a different kind of backstop from a normal investor.
5. **THE COMPETITOR ROW HAS A HOLE THAT CUTS MY WAY AND I MUST SAY SO:** Samsung and SMIC do
   not file with the SEC, so the foundry row rests on TSMC, UMC and GlobalFoundries. And
   **[E2-59]** is live in a way I have not priced: if Washington administers this market —
   tariffs, procurement mandates, an equity holder who is also the customer — *"administered
   pricing can floor a commodity business's profits."* **That would not create a franchise
   (the moat would belong to the regime), but it could make the arithmetic above wrong.**
6. **[E3-47] IS THE COST OF THIS VERDICT.** *"Our most egregious mistakes fall in the
   omission, rather than the commission, category … their invisibility does not reduce their
   cost."* If 18A ramps, 14A lands a customer, and the fabs fill, the incremental return on
   $112bn inverts from negative to something large, and this file will have said no at the
   bottom.

**WHY THE VERDICT STANDS ANYWAY.** Every one of the six is a statement about **the cycle or
the sponsor**, not about the **class of advantage**. [E4-04] asks whether the moat's basis
must be periodically replaced; at Intel it must, at $20-25bn a year, and the replacement has
already failed twice. [E3-03](2) asks whether customers see a close substitute; Intel's own
risk factors say they do and that they have moved. **A better cycle does not convert a
rebuilt moat into a defended one. And [E5-35] governs the price question underneath:
*"You can turn any investment into a bad deal by paying too much. What you can't do is turn
any investment into a good deal by paying little"* — here we are asked to do both at once,
at 4x the price of fourteen months ago.**

---
## SELF-AUDIT
- [x] Questions answered in order; **stopped at Q2, the first verdict that is not IN**
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is IN on
      Note 3 and the segment tables, in hand.
- [x] Every UNRESEARCHED item names the artifact and where it lives: **(a)** the $832M H1
      2026 finance-lease payment against a $133M disclosed obligation → FY2026 10-K lease
      note or Q3 2026 10-Q; **(b)** the Mentee Robotics $900M-vs-$637M price gap → Mobileye's
      own filing or the transaction 8-K; **(c)** Intel's pre-2022 restructuring history →
      FY2016-FY2021 10-Ks. **None of the three bears on the Q2 verdict.**
- [x] Every UNKNOWABLE states what cannot be known: **Samsung Electronics and SMIC are not
      SEC registrants**, so no filing exists to pull; they are additional competitors and
      cannot widen Intel's moat.
- [x] Step 0: the filing was read, with accession numbers; **gross profit $18,375M
      cross-checked to the filed Consolidated Statements of Operations** ($52,853 − $34,478)
- [x] Owner earnings on a multi-year mean; **six windows stated**; the capex band disclosed
      as a judgment and **both ends published**
- [x] **Competitor row filled — 7 peers, two groups**; the two non-filers named with the
      obstacle
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury),
      dated 2026-09-04
- [x] Value stated as a round-number range, not a point estimate
- [x] One bar chosen: **neither** — the file closed at Q2 and no margin was applied to any
      number. **Windage count: ZERO.** No conservatism was spent, because none was needed:
      the most generous construction fails.
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] Run committed to git after every question
- [x] **[E4-18] checked**: the verdict did not require narrowing an assumption, choosing a
      window, or choosing an end of the band. **It holds at every window and at both ends.**
- [x] **[E4-26] checked**: the disconfirming case is stated in full above, at length, and was
      hunted before the verdict was written, not after.

## REGISTER
- Verdict: [ ] IN  [x] **OUT (about the business)**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
- **One line: INTC — FAIL at Q2 (OUT). The x86 moat is the [E4-04]-excluded kind — its basis
  must be wholly replaced every node at $20-25bn a year, Intel lost it twice, and its own
  10-K contemplates abandoning leading-edge development; the competitor row inverted 52.6
  gross-margin points against AMD over ten years and AMD's data-centre segment now out-earns
  Intel's; and the foundry the strategy rests on has,
  in the registrant's own words, "been unsuccessful to date in securing any significant
  external foundry customers for any of our nodes."**
- **Price $95.80. Every owner-earnings construction, on every window, at either end of the
  capex band — including Intel's best year in history at the invalid depreciation-only end —
  yields less than the 5.24% government bond.**
