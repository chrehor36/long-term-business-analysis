# Company Run — AXCELIS TECHNOLOGIES, INC. (ACLS) — 2026-09-05
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

**RESULT IN ONE LINE: FAIL at Q5, ON PRICE, at the [E4-28] floor — Q1 IN · Q2 IN
(NARROW) · Q3 IN (overlay, with a five-year backlog-overstatement flag read in full) ·
Q4 IN. Owner earnings on every honest construction yield 1.2–3.6% against a 5.24%
sovereign; honest pre-tax expectancy ~4–7%: quit on, not ranked.**
**PRICE: $115.08 (2026-09-04) vs value ~$50 / $60-65 judged / ~$95 per share (zero-growth
at the sovereign, net cash credited) · ~$40 at the floor. PASS/FAIL: FAIL — on price;
all four business gates IN (the eighth name in queue history to clear them, the first
semiconductor).**

**THE PERIMETER EVENT, stated before anything else (the DKS/HHH class):** on 2025-09-30
Axcelis signed an all-stock merger of equals with **Veeco Instruments** (8-K filed
2025-10-01, accession 0001104659-25-095307): each Veeco share converts to **0.3575**
Axcelis shares; post-close Axcelis holders own **~58.4%** fully diluted. Both shareholder
votes passed **2026-02-06**; the ONLY remaining condition is approval by **China's State
Administration for Market Regulation**, expected close **H2 2026** (Q2-2026 10-Q, Note 19).
The filed history this run values is **standalone Axcelis**; the buyer at today's quote is
buying ~58.4% of a combined company whose other 41.6% (Veeco: laser annealing, MBE, wet
processing — a different toolset) has NO filed history under this registrant. The run
prices what the filings support and states the wedge; it does not pro-forma an unclosed
deal. That China — the company's largest end market and its named export-control risk —
holds the last approval over the company's own merger is recorded at Q4 as exposure.

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
- **rate 5.24%** · **date 2026-09-04** · source: **US Treasury daily par yield curve,
  30-year, from the issuing authority** (`tools/sources.py`, per the 2026-09-02 correction).
- Earnings currency: USD. 83.7% of FY2025 revenue was international, but **88.6% of sales
  were denominated in US dollars** (10-K Item 1) and substantially all system sales are
  billed in USD (Item 1A). The USD sovereign is the yardstick; FX exposure (11.4% of
  revenue in local currencies) is noted at Q4, not repriced.
- FX / ADR ratio: not applicable — domestic filer, single class on Nasdaq.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes (Notes 2, 16, 17, 19
  of the 10-K; Notes 1, 16, 19 of the Q2-2026 10-Q)
- documents · dates · accession nos.:
  - **Form 10-K, FY ended 2025-12-31, filed 2026-02-26, accession 0001104659-26-020461**
    (`acls-20251231x10k.htm`)
  - **Form 10-Q, quarter ended 2026-06-30, filed 2026-08-06, accession
    0001104659-26-091999** — the most recent periodic filing in existence at run date
  - Form 8-K of 2025-10-01 (merger agreement), accession 0001104659-25-095307
  - Form 8-K of 2024-11-06 (backlog correction), accession 0001104659-24-114804, with
    Exhibit 99.2 read
  - FY2024 10-K (0001558370-25-001855), FY2023 10-K (0001558370-24-001628), FY2022 10-K
    (0001558370-23-002006) — vintage checks for backlog and China disclosure
  - DEF 14A filed 2026-03-31, accession 0001104659-26-037356
- **Figures cross-checked against the filed statements:** (1) *Net cash provided by
  operating activities*, FY2025 Consolidated Statements of Cash Flows: **$118,305
  thousand** — companyfacts `NetCashProvidedByUsedInOperatingActivities` returns 118.3
  ($M). Agree. (2) *Expenditures for property, plant and equipment and capitalized
  software*: **$(11,295) thousand** FY2025, $(12,181) FY2024, $(20,656) FY2023 —
  companyfacts returns 11.3 / 12.2 / 20.7. Agree. **The filed capex line INCLUDES
  capitalized software in one caption — the HAS/queue-wide software-capex defect does NOT
  bite on this filer** (checked against the filed caption itself).

**Price and shares:**
- price **$115.08**, 2026-09-04 close (aggregator via `tools/run.py` — live quote only,
  flagged per protocol)
- shares **30,881,489**, hand-read off the Q2-2026 10-Q cover: *"As of August 3, 2026,
  there were 30,881,489 shares of the registrant's common stock outstanding"* — single
  class. (run.py's 31.7M weighted-average basis rejected again — the standing tool defect.)
- **market cap $3,553.8M** ≈ **$3,554M**
- 10-K cover cross-check: 30,718,815 shares at 2026-02-23 — consistent with the 10-Q cover
  plus H1 RSU/ESPP issuance (30,717k → 30,881k in the filed equity statement).

---
# STAGE 0 — ARTIFACT CHECK, AND WHAT THE SCREEN GOT RIGHT AND WRONG

**The owner-earnings series was recomputed line by line from companyfacts and cross-checked
against the filed FY2025 cash-flow statement (two lines to the dollar, above).**
Construction: OCF − SBC − (expenditures for PP&E and capitalized software). $M:

| FY | OCF | SBC | capex | **OE (capex end)** |
|---|---|---|---|---|
| 2016 | −8.8 | 5.2 | 2.5 | **−16.5** |
| 2017 | 56.3 | 5.7 | 7.3 | **43.3** |
| 2018 | 47.0 | 7.8 | 4.7 | **34.5** |
| 2019 | −13.6 | 8.2 | 12.0 | **−33.8** |
| 2020 | 69.7 | 10.5 | 7.4 | **51.8** |
| 2021 | 150.2 | 12.1 | 8.7 | **129.4** |
| 2022 | 215.6 | 13.4 | 10.7 | **191.5** |
| 2023 | 156.9 | 18.3 | 20.7 | **117.9** |
| 2024 | 140.8 | 21.0 | 12.2 | **107.6** |
| 2025 | 118.3 | 20.8 | 11.3 | **86.2** |
| H1-2026 | 36.5 | 11.3 | 5.4 | **19.8 (six months)** |

- **The screen row REPRODUCES in shape.** run.py at today's price: 3-yr window OE
  $101–106M (yield 2.76–2.92%), 5-yr $124–128M (3.40–3.51%), divergence **+23.2%** on the
  conservative end — **the brief's "spread 22.7%" is confirmed as the right region, unlike
  TSCO's irreproducible 22.7%.** The brief's yield 3.03%/growth 6.97% row was struck at a
  slightly different price/vintage; the construction is the same.
- **The screen's cap was NOT reproduced as filed:** run.py's $3.64B rides the 31.7M
  weighted-average share basis (standing defect); the cover count gives **$3,554M**.
- **The [E4-41] boom signature is the loudest in the queue to date:** pre-boom five-year
  mean (FY2016–20) **$15.9M**; boom five-year mean (FY2021–25) **$126.5M** — an **8x
  step**. The boom is 2021–2023 bookings converting to 2022–2024 revenue: the
  mature-node/SiC capex wave plus China stockpiling ahead of export controls. Exactly the
  two-to-three-year shape the brief predicted. Leave-two-out (the ANF fix — drop 2022 and
  2021 from the ten-year series): mean **$48.9M**.
- capex ≈ D&A within a few $M every year (this is an assembler, not a fab); the capex band
  is narrow and is NOT where the width lives. The width lives in the window choice — see Q4.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, without management's language.** Axcelis makes one kind
of machine: an ion implanter — a tool the size of a room that fires electrically charged
dopant atoms into silicon or silicon-carbide wafers to set their electrical properties.
A chip fab needs roughly twenty implant steps per process flow, so every fab buys a fleet
of them. A machine sells for **$2.6M to $12.0M** (10-K Item 1A, filed range). Axcelis
assembles them in Beverly, Massachusetts and South Korea from sourced subassemblies —
gross PP&E is only $58M net against $839M of revenue, because the capital-intensive part
of this industry belongs to the customers, not the toolmaker. The real maintenance spend
is the **R&D line: $109.0M in FY2025, 13.0% of revenue, expensed** — the tool must keep
pace with device roadmaps or stops selling (the QCOM/fabless shape the brief predicted:
(c) runs through the income statement already).

Two revenue engines with different drivers, and the filer itself splits them this way
(10-K MD&A): **Systems** ($571M FY2025) — sold on customers' capital-budget decisions,
violently cyclical; and **CS&I/aftermarket** ($268.0M FY2025: spares, upgrades, used
tools, service labor) — driven by installed-base utilization, ~3,400 tools in 27
countries. Aftermarket is the durable part; systems are the cycle.

- **The scarce input the business controls:** beam-line engineering know-how — the physics
  of producing a pure, precisely-shaped ion beam at energies to 8 MeV — embodied in the
  Purion platform and 169 active US patents (+356 foreign). Only one other company in the
  world (Applied Materials) makes the full range of these machines. That is a real and
  rare input, and it is why Q2 gets a serious hearing.
- **Will the fundamentals look broadly the same in ten years?** The mechanism, yes — ion
  implantation has been a required step for five decades and no filed threat displaces it;
  the 10-K's own risk list names competing technologies only generically. The *perimeter*,
  no — the pending Veeco merger will roughly double the company and add toolsets this
  registrant has never operated (stated at the head of this file; handled as exposure, not
  as a Q1 failure — the standalone business is understood).
- The cycle is understood as part of the business, not a surprise: revenue 267 → 443 → 343
  → 475 → 662 → 920 → 1,131 → 1,018 → 839 ($M, FY2016–25). A toolmaker levered to
  mature-node capex decisions of a concentrated customer base.

- **VERDICT: [x] IN**

*Recorded against myself under operator rule 9: the PLAB precedent shows a semis job shop
is easy to understand precisely because there is little to it. The Q1 pass here rests on
the business being simple, not on it being good — the moat question is decided at Q2, on
the row, not on the word "duopoly."*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The brief's claim: a stable duopoly in a niche too small for new entrants, with an
installed-base aftermarket annuity. The brief's own prior [E4-26]: Q2 OUT or
NARROW-at-best. The verdict is NARROW — and the reasoning is set out so it can be
attacked, because this file's Q2 is the closest call since TSCO.**

**First, the duopoly claim CORRECTED from the filing.** The 10-K names SIX implant
competitors, not one: *"we mainly compete against Applied Materials … Axcelis and Applied
Materials are the only ion implant system manufacturers with a full range of implant
products. Other implantation equipment manufacturers we compete with include Sumitomo
Heavy Industries Ion Technology Co. Ltd. and Nissin Ion Equipment Co., Ltd in Japan,
Advanced Ion Beam Technology, Inc. in Taiwan, as well as Kingstone Semiconductor and CETC
Electronics Equipment Group Co., Ltd. in the People's Republic of China."* The duopoly is
real only at the **full-range** level. And the same paragraph carries the most damaging
filed sentence in the document: *"**Non-U.S. suppliers may have an advantage over U.S.
suppliers under recently established U.S. export controls regulation for shipments to
China.**"* The subject's own 10-K states that policy hands its non-US competitors an edge
in its largest end market.

**The three criteria [E3-03]:**
- **(1) Needed or desired — YES.** ~20 implant steps per process flow; no fab runs without
  implanters.
- **(2) No close substitute — PASSES NARROWLY, and this is where ACLS differs from PLAB
  and QCOM.** Unlike PLAB, there is **no captive threat**: chipmakers do not build
  implanters in-house, and no customer owns a working substitute for the factory. Unlike
  QCOM's QCT, the customers are not building the product themselves. The substitute is
  AMAT — one company — and switching an implanter mid-fleet means re-qualifying a process
  of record. For the high-energy niche the 10-K claims a stronger position (*"Axcelis has
  been a market leader in high energy ion implanters for many years"*). At the mature
  high-current end the substitute set is wider (Japanese + Chinese entrants).
- **(3) Not price-regulated — passes**, but worth little on its own ([E2-59], the PLAB
  point). The real regulation runs the other way: **export controls regulate WHO the
  company may sell to**, and the licence sits with the US government, not the company.

**[E4-04] — must the moat be continuously rebuilt?** The test: *does the spending defend
the same advantage, or buy its replacement?* ACLS's moat spend is the **R&D line — $109.0M,
13.0% of revenue (FY2025), risen from 8.6% in 2023** — defending one beam-line platform
(Purion, in production since the early 2010s) against slow-moving mature-node roadmaps.
This is the **defence** case, not PLAB's replacement-fleet case: capex is $11M a year
against D&A of $18M; nothing obsoletes and must be re-bought. Semiconductor equipment as a
class is rapid-change, but ion implant is the slow corner of it — the physics is 50 years
old and 77% of shipped systems revenue goes to mature process nodes (Q2-2026 10-Q). Held:
the moat is defended, not rebuilt. **Success does not depend on a great manager** — no
key-person dependence found [E4-23].

**Which of the four causes was the 2021-23 record? [E4-36] — wave-riding, and the wave is
named.** Revenue tripled 2020→2023 (475 → 1,131) on the mature-node/SiC capex wave and
Chinese stockpiling ahead of export controls, then fell 26% in two years as the wave
receded. The STRUCTURE (two full-range makers, installed-base service) predates the wave;
the boom ECONOMICS were the wave. Both facts are held: the class below is judged on the
structure; the Q4/Q5 arithmetic is normalized off the wave [E4-41].

**[E2-44] — the two-characteristic test, and ACLS PASSES the half PLAB failed:**
1. *Raise prices when demand is flat and capacity underutilized?* The filed instruments
   through the worst downturn in the company's modern history: **the filed system price
   range ROSE and held — "$2.4 million to $10.0 million" (FY2022 10-K) → "$2.6 million to
   $12.0 million" (FY2023, FY2024 AND FY2025 10-Ks)** — and **gross margin ROSE through
   the collapse: 43.7% (2022) → 43.5% (2023) → 44.7% (2024) → 44.9% (2025)** while revenue
   fell 26%. Compare PLAB, which filed a forecast of continued price declines. Confounder
   stated honestly: the GM series is mix-assisted (aftermarket rose from 21.8% to 31.9% of
   revenue), so it is not a pure price read — but a company being forced on price does not
   print its highest GM of the decade in the trough year.
2. *Grow dollar volume with only minor additional capital?* Trivially yes — revenue
   tripled 2016→2023 on ~$11-21M/yr of capex. The capital intensity of this industry
   belongs to its customers. (The PLAB capex-intensity trap does NOT apply here — the
   opposite balance-sheet shape.)

**[E4-55] — where units exist, monitor units.** The filed physical series: **installed
base ~3,100 (FY2022 10-K) → 3,200 → 3,300 → 3,400 (FY2025 10-K)** — growing ~3%/yr
through the bust, and it is the aftermarket's driver. **Systems SHIPPED per year is NOT
filed in any vintage read** — dollar systems revenue only — so ASP-vs-units cannot be
decomposed from filings (the brief's [E4-55] ask dies at the disclosure wall; recorded).
Aftermarket dollar series, filed: **$247.0M (2023) → $235.3M (2024) → $268.0M (2025) →
$155.4M in H1-2026 (+33.7% YoY, now 37.5% of revenue)** — a record year in the systems
trough, which is what an installed-base annuity should do. Its limit is also filed (Item
1A): customers self-service and third-party parts suppliers compete — *"To the extent our
customers purchase parts and services from other vendors or provide their own system
maintenance labor, our revenue and profitability will be reduced."* An annuity with
competitors, not a toll.

**THE COMPETITOR ROW — required [E3-28].** Same metric (operating margin, GAAP, most
recent full fiscal year, filing-sourced), with the [E3-61] limit stated at the end.

| Company | op margin, latest FY | revenue | purity | source |
|---|---|---|---|---|
| **AXCELIS (ACLS)** | **14.2%** FY2025 *(23.5% FY2023 peak · 6-14% pre-boom)* · GM 44.9% | **$839.0M, −25.8% from peak** | **pure-play implant** (98.2% of revenue) | 10-K acc. 0001104659-26-020461 |
| **Applied Materials (AMAT)** | **29.2%** FY to 2025-10-26 | $28.37B | **MIXED — implant is not a reported segment**; no implant-level economics exist in the 10-K (definitive nil disclosure, the PLAB-captive answer) | 10-K XBRL, companyfacts |
| **Lam Research (LRCX)** | **35.3%** FY to 2026-06-28 | $23.23B | adjacent WFE (etch/dep), no implant | 10-K XBRL |
| **KLA (KLAC)** | **41.7%** FY to 2026-06-30 *(computed: rev − COGS − R&D − SG&A; KLAC stopped tagging the OI subtotal)* | $13.58B | adjacent WFE (process control) | 10-K XBRL |
| **Veeco (VECO)** — the merger partner | **5.4%** FY2025 *(9.3% FY2024)* | $664M, −7.4% | specialty equipment (anneal, MBE, wet processing) | 10-K XBRL |
| Sumitomo Heavy Ion Technology · Nissin Ion (Japan) | not separately reported — subsidiaries inside TSE conglomerates (SHI 6302, Nissin Electric 6641); implant is not a disclosed segment of either | — | — | rung 6, blocked: no segment document exists |
| AIBT (Taiwan) · Kingstone (China, inside Wanye Enterprises SSE 600641) · CETC (China, state-owned) | AIBT/CETC: no public filings exist. Kingstone: a Wanye SSE annual report EXISTS and was not pulled (language/platform) — the one open work-order in this row | — | — | stated below |

- **Peers: 6 implant competitors named by the subject, plus 2 adjacent-WFE majors for the
  cohort economics. Filed same-formula figures obtained for 4 filers + the partner.**
- **The row's finding, and it cuts AGAINST the subject:** ACLS earns the **lowest margin
  of the US semiconductor-equipment cohort — half of KLAC's — even at its own cycle peak**
  (23.5% vs 29-42%). The "niche too small for entrants" is also a niche too small for
  leverage: implant is a single-digit share of fab capex, ACLS's customers are the giant
  fabs (top-10 = 55.2% of FY2025 revenue, 68.5% in H1-2026, two customers at 17.8% each),
  and **[E3-03]'s power sits with the customer**, exactly as the brief's prior said. This
  is why NARROW, not WIDE.
- **The Kingstone gap, adjudicated under the four-verdict test:** the attacker series
  (Chinese implant share inside China) has one obtainable document (Wanye's SSE annual
  report) and it was not pulled. Can it flip this verdict? **No** — a surging Kingstone
  confirms the NARROWING direction already recorded and feeds the Q4 named death; a flat
  Kingstone leaves NARROW standing. Since no outcome of the fetch moves the verdict, the
  gap is recorded as a row limit and a **Q6 monitoring work-order**, not an UNRESEARCHED
  close. *(The PLAB rule applied: the verdict does not move anywhere inside the row's
  uncertainty.)*
- **[E3-61] limit:** the row shows position, not conduct. On conduct the filed record is:
  filed price range UP through the bust (above) — the anti-PLAB conduct.
- **Untapped pricing power [E3-33/E5-28]? Not claimed.** Claiming it would claim
  near-monopoly; six named competitors and 55% customer concentration refute the class.
- **[E2-53] dominance? No** — AMAT is 34x the size; the marketplace, not the position,
  sets outcomes in the down years (op margin 23.5% → 14.2%).
- **[E4-32] direction:** NARROWING at the mature-node end — the subject's own filed
  sentence (non-US suppliers advantaged in China), 77% of shipped systems revenue in
  mature process, and the top-of-cycle margin gap vs the cohort — offset by a growing
  installed base, record aftermarket, and a rising filed price range. Direction is
  adverse; existence is not (yet) in question.

**Why NARROW-IN and not OUT — the difference from the three OUT precedents, stated so it
can be attacked:**
- **vs PLAB (Q2 OUT):** no captive threat; customers cannot make the product; the moat
  spend defends one platform rather than re-buying a tool fleet; the filed price range
  rose where PLAB's filing forecast price declines; GM rose through the bust where PLAB's
  fell.
- **vs QCOM (Q2 OUT):** no licence cliff; the customers are not building the substitute;
  the aftermarket is contract-free but installed-base-anchored, and the installed base is
  filed as growing every year.
- **vs TGT/DRI (Q2 OUT on [E3-03](2)):** the physical series that exists (installed base)
  grows; the pricing instrument that exists (filed ASP range, GM) held through the demand
  collapse. [E2-44](1) passes here; it failed there.

- Class: [ ] WIDE  **[x] NARROW**  [ ] NONE  [ ] PROVISIONAL · **Direction: NARROWING at
  the mature-node/China end; defended at the high-energy/power end**
- **VERDICT: [x] IN — NARROW.** *The strongest fact against this verdict: the cohort-low
  margin plus 55-68% customer concentration reads as a supplier tolerated by giants, not a
  franchise over them — [E3-03](3) power inverted, the brief's own case. It is held IN on
  the filed pricing conduct through the worst two years in the filed history, which is the
  one test a no-moat supplier cannot pass.*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — THE WEIGHT CASE, declared.**
- [ ] **Daily execution [E3-38]** — NOT ticked, with the reasoning shown: [E3-38]'s root
  class is the undifferentiated product that magnifies the manager. ACLS's product is
  differentiated (two full-range makers worldwide; filed price range rising), and Q2
  found a NARROW franchise, which by [E3-43] tolerates some mismanagement. The R&D
  execution dependence is real but is the moat-defence spend, priced at Q2.
- [ ] Control [E1-16] — not ticked; liquid public minority stake.
- [ ] Leverage [E3-29] — not ticked. **No debt at all beyond a $41.6M finance lease; net
  cash ~$546M.**
- **None ticked → Q3 is a qualitative OVERLAY.**

**Honesty — binary, permanent, filings-based [E5-16], each matter dated to when it became
public. ONE matter exists and it was read in full: THE BACKLOG MISSTATEMENT.**
- **8-K of 2024-11-06 (accession 0001104659-24-114804):** during Q3-2024 close, *"the
  Company's internal financial team identified an error in the calculation of backlog in
  prior periods, beginning in 2019 through the second quarter of 2024, as reported in
  previously filed Form 10-Ks."* Exhibit 99.2, the filed correction chart:

  | as of | 2019 | 2020 | 2021 | 2022 | 2023 | Q1-2024 | Q2-2024 |
  |---|---|---|---|---|---|---|---|
  | reported | $99M | $116M | $461M | $1,125M | $1,212M | $1,121M | $994M |
  | corrected | $84M | $111M | $415M | $1,020M | $1,061M | $973M | $879M |
  | variance | −$15M | −$5M | −$46M | −$105M | **−$151M** | −$149M | −$115M |

  **Five-plus years of a misreported operating metric, every period overstated, one
  direction only, peaking at −12.5% exactly when the metric was the headline demand
  indicator of the boom.** Adjudication: (a) the error is in a non-GAAP operational
  metric outside the audited statements — no restatement of any financial statement; (b)
  it was **self-identified** (the CFO seat changed in 2024; the new team found it) and
  published with a full by-period chart — the **[E2-69] deviation-toward-candor** shape;
  (c) **[E5-22]**: the failure that counts is *"they didn't act when they learned"* — they
  acted the quarter they learned. **Not an integrity disqualifier. It IS the
  weak-accounting flag, held open below, and it caps how much weight any ACLS operating
  metric carries in this file.**
- No litigation disclosed as material (Item 3 and Note 16(b), FY2025 10-K, verbatim: *"We
  are not presently a party to any litigation that we believe might have a material
  adverse effect"*). No related-party flags found. FY2023 10-K/A (filed 2024-02-28, five
  days after the 10-K) noted; its stated purpose could not be extracted in this session —
  recorded as a loose end, not adjudicated.

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30].** *Each a prompt to read, never a verdict.*
- [x] **weak accounting — FIRES**, on the backlog error above. *"Seldom just one cockroach
  in the kitchen"* is answered by the metric-switching finding below.
- [ ] unintelligible footnotes — not fired; disclosure is above average (backlog AND
  bookings quantified annually; systems/aftermarket split; end-market mix percentages).
- [x] **trumpeted projections — fires at half strength.** A quarterly guidance culture
  exists (Item 1A acknowledges management forecasts). Not chased to the [E3-48]
  guidance-vs-outturn ledger; the cycle makes single-quarter outturns noisy.
- [ ] serial share issuance [E5-15] — **fires in REVERSE**: 32.365M → 30.717M shares in
  FY2025; a net retirer for five consecutive years.
- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRES IN THE PAY PLAN, NOT THE
  FILINGS.** The 10-K and 10-Q carry **zero** occurrences of EBITDA (checked). The 2026
  proxy carries eight: the **2025 annual cash incentive was keyed to a SINGLE metric,
  "Adjusted EBITDA"** — see the metric-switch below.
- [x] **filed-figure tells [E4-30] — one of two fires at prompt strength.** Smoothness:
  acquitted absolutely (OE runs −$34M to +$192M inside seven years; nobody is smoothing
  this). Cash taxes paid as % of reported pretax: 21.3% (2023) → 23.8% (2024) → **11.4%
  (2025)** — a one-year drop coincident with falling profits; consistent with estimated-
  payment timing; noted as a prompt, not chased to a finding.
- [x] **metric-switching [E2-49] — FIRES, dated, and it is the sharpest Q3 finding.** The
  2024 ATI (metrics: revenue, operating profit, gross margin) paid **68.2%**. For 2025 the
  Compensation Committee **discarded all three metrics for a single "Adjusted EBITDA"
  metric** (proxy, filed 2026-03-31: *"as opposed to the metrics of revenue, operating
  profit, and gross margin used in 2024"*), set target at **$197.8M — below 2024's own
  actual** (FY2024 op income $210.8M + D&A $15.8M + SBC $21.0M ≈ $248M before further
  adjustments), and the plan then scored **103.1%** ($199.7M achieved) — **an
  above-target cash payout in a year revenue fell 17.6% and net income fell 40%.**
  *"Yardsticks seldom are discarded while yielding favorable readings"* — this is the
  DG/ULTA target-set-below-prior-actual shape, executed through a yardstick swap.
  Mitigants stated: the swap was announced in advance with a reason (forecast risk), the
  payout is capped at 200% and at 30% of pre-payout profit, no discretionary adjustment
  was made to the score, and NEOs took a two-week unpaid furlough (~4% salary cut) in the
  same year. The flag stands.
- **[E4-52] convergence check:** the backlog overstatement (2019–2024) and the pay-metric
  swap (2025) point the same optimistic direction but are separated in time and authorship
  (the team that found the error is the team that took the furlough). Read as two flags,
  not one lollapalooza.

**STEP 3 — THE PRIMARY TEST [E2-01].** Earnings rate on equity, no leverage, balance sheet
first: equity $1,034.7M (FY2025), of which **net cash is ~$546M — half the book is cash**.
- ROE on year-end equity: 18.3% (2021) · 27.4% (2022) · 28.5% (2023) · 19.8% (2024) ·
  **11.6% (2025)**; pre-boom years ran mid-single digits (FY2016-20 op margins 6-14% on a
  cash-heavy base). **On net tangible OPERATING assets (equity less net cash ≈ $489M),
  FY2025 earns ~25%** — the operating business is genuinely good; the blended return is
  diluted by the cash hoard and the cycle. Boom years [E2-73]-adjusted: the 2021-23 ROEs
  ride the wave, a tailwind not of management's making.

**The half-owner test [E2-26]: PASSES.** Systems/aftermarket split, end-market mix (77%
mature / 22% DRAM / 1% advanced logic), backlog AND bookings numbers annually, customer
concentration, the merger's remaining condition named plainly — and when the backlog error
was found, the company published the full by-period correction rather than a footnote.
Weakest point: no China revenue percentage has ever been filed (checked FY2022-25 10-Ks —
"significant portion" only), for a company whose largest single risk factor is China.

**The institutional imperative [E2-30]:**
- [ ] resists change — no finding.
- [x] **projects/acquisitions materialise — the Veeco merger is a prompt here**, though
  stock-for-stock at a cycle trough is the least imperative-shaped version of it.
- [ ] staff studies — not observable.
- [x] **peer imitation — a prompt:** semiconductor-equipment consolidation is a wave
  (AMAT itself is the product of one); a merger of equals "for scale" is the industry's
  standard move. Not a venality finding [E2-30].

**Capital allocation.**
- **Buybacks [E5-08]:** (1) ample funds — YES, overwhelmingly (net cash $546M, no debt).
  (2) material discount to conservative IV — **FY2025: 1,827k shares at $66.28 average**
  (monthly $46.42-$83.55; zero after November 2025), against this file's judged zero-growth
  value of ~$45-70/share (Q5): **the FY2025 tranche sits inside the band — the first
  roughly-defensible buyback vintage in this file**; the April-2025 tranche (360k at
  $46.42) was bought at the bottom of the band. **FY2021-24 tranches ($50.0M / $57.5M /
  $52.5M / $60.5M) were executed at market prices that ranged far above any owner-earnings
  construction this run can support** (the stock traded $40-200 over the span) →
  **CAPITAL-ALLOCATION FLAG on the boom-era vintages**, humility clause [E4-13] attached:
  management knows the business better than we do, and our band is built on a normalized
  mean they may legitimately dispute. Binds position size, never the rate.
- **The stock deal [E5-44] — measure the paper given at IV, not at quote.** The merger
  issues ~0.3575 new ACLS shares per Veeco share (~41.6% of the combined company) for a
  business whose FILED trailing economics are: revenue $664M (FY2025, −7.4%), operating
  margin **5.4%** (9.3% FY2024), net income **$35M** — against ACLS's $120.2M. **Veeco
  holders receive ~41.6% of the combined equity for contributing ~22% of combined FY2025
  trailing net income.** On trailing filed numbers the deal is dilutive to owner earnings
  per share (~$3.89 standalone → ~$3.02 combined per share, FY2025 basis). If ACLS stock
  is worth its quote or more, the IV given exceeds the IV received on every trailing
  construction. What would justify it — synergies, Veeco's cycle position, product
  breadth — lives in announcements and projections, not in filings this run read, and
  [E3-48]'s base rate for deal projections is nine-in-ten decided-course justification.
  **CAPITAL-ALLOCATION FLAG, the run's largest.** Humility [E4-13]: both boards
  unanimous (one cross-director recused), both shareholder bases approved it 2026-02-06,
  and trailing troughs understate cyclical acquirees.

**THE GUARDRAIL.**
- [x] Nothing here promotes the name; Q3 cannot repair Q2's narrowness or Q4's cycle.
- [x] No great-manager dependence recorded at Q2; the manager is not the plan.

- **VERDICT: [x] IN — as an OVERLAY.** *No integrity disqualifier found — which under
  [E5-17] is the absence of found disqualifiers, not a finding of honesty; this file
  carries a corrected five-year misstatement, a yardstick swap that paid above target in
  a down year, and two capital-allocation flags. All four are recorded and none stops a
  run that price has already decided (see Q5).*

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**, with (c) a DISCLOSED JUDGMENT

**The (c) judgment, and why the capex band is NOT where the width lives.** Capex
(the filed line *"Expenditures for property, plant and equipment and capitalized
software"*) and D&A track each other within a few $M every year ($11.3M vs $17.6M in
FY2025) — this is an assembler whose customers own the industry's capital intensity. The
PLAB [E5-20] exception does NOT apply; [E3-44]'s default holds trivially. **The real (c)
is the R&D line — $109.0M in FY2025, 13.0% of revenue and RISING (8.6% in 2023) — and it
is already expensed through the income statement** (the QCOM/fabless shape the brief
predicted). (c) is judged at the HIGHER of capex/D&A each year; the difference moves no
verdict. Stock compensation subtracted in full at the reported charge **[E5-06]** ($20.8M
FY2025; [E3-70] noted — the reported charge is the floor of the subtraction; at 2.5% of
revenue, not decisive).

**THE WINDOWS — every one published [E4-38]; the spread IS the finding [E4-25].**
Construction: mean(OCF − SBC) − (c). Cap $3,554M. Sovereign 5.24%.

| window | OE ($M) | yield | vs sovereign | g needed for the [E4-28] floor |
|---|---|---|---|---|
| 5-yr FY2021-25 (the [E2-42] default — and it is ALL boom) | **126.5** | 3.56% | −1.68 | 6.4% |
| 3-yr FY2023-25 | **103.9** | 2.92% | −2.32 | 7.1% |
| 10-yr FY2016-25 (two downturns + the whole boom) | **71.2** | 2.00% | −3.24 | 8.0% |
| 10-yr leave-two-out (drop 2022, 2021 — the ANF fix) | **48.9** | 1.38% | −3.86 | 8.6% |
| trailing 12 months (H2-2025 + H1-2026) | **43.7** | 1.23% | −4.01 | 8.8% |
| pre-boom 5-yr FY2016-20 (displayed, NOT judged — the installed base was ~20% smaller) | *15.9* | *0.45%* | — | — |

- **Spread, conservative ends: the 5-yr window is 2.9x the leave-two-out and 2.9x the
  TTM.** The distorted years are NAMED [E4-25/E5-11]: **2021-2023, the mature-node/SiC
  capex wave plus Chinese pull-forward ahead of US export controls — a favourable
  exogenous break, and [E4-41] requires the mean be normalized DOWN for it.** The screen's
  22.7% spread (5-yr vs 3-yr) was the small spread; the honest one is far wider.
- **JUDGED OE: ~$70M** — essentially the ten-year mean, crediting today's larger
  installed base (3,400 tools vs ~2,700; aftermarket $268M vs ~$120M pre-boom) against
  the boom distortion in the same window. Direction of error: if anything HIGH — the TTM
  runs $44M and H1-2026 OE was $19.8M in six months. Honest range carried: **$44-127M**.
- **Is the range too wide to conclude? No — the verdict does not move anywhere inside
  it.** Even the most generous construction (the all-boom 5-yr window, unnormalized,
  which [E4-41] forbids trusting) yields 3.56% against a 5.24% bond. The width changes
  the size of the shortfall, never its sign.

### Great, good, or gruesome? **[E4-20]**
- **Mechanically GREAT-class, cyclically defective:** FY2025 earns ~25% on net tangible
  operating assets (~$489M) with capex ≈ D&A ≈ 1.3% of revenue; growth to 2023's peak
  consumed almost no incremental fixed capital. It is NOT gruesome — growth does not eat
  capital. What keeps it out of the great class is that the return arrives in waves: the
  ten-year owner-earnings series contains two negative years and an 8x boom step, and the
  reinvestment engine is absent (cash piles up — $546M net — because the business cannot
  absorb it). **Class: GOOD**, with [E3-55] scope honestly applied in reverse: this is
  volatility WITHOUT a certain endgame, so the spread is width, not noise.

### Staying power — score all three **[E5-11]**
- **(1) large and reliable stream — FAILS the "reliable" half:** OCF was NEGATIVE in
  FY2016 (−$8.8M) and FY2019 (−$13.6M) inside the filed decade. The aftermarket
  ($268.0M, record in the trough) is the reliable layer; systems are not.
- **(2) massive liquid assets — PASSES emphatically:** $155.0M cash + $247.2M short-term
  + $174.8M long-term investments = **$577M** (plus $10.6M restricted), against **total
  liabilities of $321M**. [E5-39]: no revolver counted, none exists to count.
- **(3) no significant near-term cash requirements — PASSES:** purchase commitments
  $178.0M ($171.0M in 2026) against $577M liquid; **no debt**; the only funded obligation
  is the $41.6M finance-lease on the Beverly HQ (2015 sale-leaseback, runs to 2044).
- **Leverage, named and quantified [E4-16]:** none. Finance lease $41.6M = 3.9% of
  equity. Coverage [E2-54]: interest is ~$3M of lease interest against $100M+ of pre-tax
  income in the TROUGH year — not a constraint in any modeled state.
- **Worst case [E2-55]:** a repeat of FY2019 (OE −$33.8M) burns 6% of the liquid assets
  per year. The balance sheet survives a decade of 2019s. Survival is not the question
  this file turns on.
- **[E2-60] restricted-earnings check: does NOT fire** — FY2021-25 payouts ($342M of
  buybacks, no dividend — verified: none paid in any year of the filed decade) ran
  well inside the same span's OE (~$633M), with zero debt added and equity rising.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40]**
- **Death 1 — the China lever closes (a REAL POSSIBILITY; this is exposure, not
  experience [E4-40], and the exposure is filed).** Three filed jaws of one vise: (a) US
  export controls already license ACLS's shipments to its Chinese customers — *"we
  currently are able to continue to ship to substantially all of our Chinese customers"*
  is a present-tense, revocable state, with SMIC on the Entity List under a licensing
  carve-out; (b) the subject's own filed sentence that **non-US suppliers hold an
  advantage under those controls**, while two Chinese implanter makers (Kingstone, CETC)
  scale behind a domestic-substitution policy; (c) **China's SAMR holds the last approval
  over the company's own merger.** Quantified from filed figures: Asia is 76.0% of system
  shipments; the China slice is NOT filed (stated at Q3); if licence policy or domestic
  substitution removes even half the Asian mature-node systems flow, systems revenue
  (~$571M) loses ~$200M+ and owner earnings revert toward the aftermarket-anchored
  pre-boom level (~$15-50M) — **a valuation death, not a solvency death: the yield at
  today's cap falls toward 1%.**
- **Death 2 — [E2-27]'s capacity treadmill at the mature node (a real possibility,
  slower):** every implant vendor (AMAT, the Japanese, the Chinese entrants) adds
  mature-node capacity into the same customer capex pool; all players put more in, returns
  stay anemic; ACLS's cohort-low operating margin (14.2% vs 29-42%) is the standing
  evidence of who absorbs that outcome first.
- **Death 3 — solvency (a LOW-LEVEL POSSIBILITY):** requires simultaneous multi-year
  negative OCF exceeding anything filed, against $577M liquid and no debt. Not the vector.
- **The merger cuts both ways and is stated, not scored:** if completed, the perimeter
  doubles into weaker-margin toolsets (Veeco op margin 5.4%) and the standalone series
  this file is built on stops describing the company; if blocked by SAMR, the standalone
  case above stands and the $108.7M/$77.5M termination fees do NOT apply to a regulatory
  failure (only to recommendation changes/competing proposals; a $15M expense
  reimbursement covers vote failure). Merger-related G&A is already in the FY2025/H1-2026
  numbers (+$15.5M H1 professional fees, filed).

- **VERDICT: [x] IN.** *Survival is comfortably evidenced; the earnings LEVEL is the
  file's problem and it is priced at Q5. The wide window spread is carried as the Q4
  finding it is: a boom sits in every recent window and the mean is not trusted until
  normalized down [E4-41].*

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28].** Honest pre-tax expectancy at this price:
**~4-7%** (yield 1.2-3.6% judged ~2.0%, plus honest through-cycle growth — installed base
+3%/yr, aftermarket compounding, mature-node unit growth — worth perhaps +3-5%; the
[E4-35] base rate refuses more without written proof). **Below roughly 10% → the name is
QUIT ON, not ranked.** No risk premium in the rate [E3-42]; the bare sovereign is used.

**1. THE YIELD**
- judged owner earnings **$70M** ÷ market cap **$3,554M** = **1.97%** · honest range
  **1.23% (TTM) to 3.56% (all-boom 5-yr)** · sovereign **5.24%**
- **Every construction, including the one [E4-41] forbids trusting, is below the bond.**

**2. WHAT THE PRICE ALREADY ASSUMES**
- perpetual growth needed to match the BARE BOND: **+1.7%** (off the all-boom 5-yr mean)
  to **+4.0%** (off the TTM); **+3.3%** off judged OE — *the strongest thing sayable for
  the price* — and for the ~10% floor: **+6.4% to +8.8% perpetual** (the screen's 6.97%
  reproduced as the boom-window case).
- what the business has actually done: through-cycle OE growth is real but wave-shaped —
  pre-boom 5-yr mean $15.9M → post-boom judged $70M is the installed-base ratchet worth
  roughly +7%/yr ACROSS A DECADE that contained the largest mature-node capex wave in
  history; the TTM ($43.7M) is the going rate without a wave. A floor case here requires
  believing the next wave is both imminent and priced at zero. [E4-44]: value cannot
  outgrow earnings in perpetuity; [E2-63]: the upside is capped by what the niche can
  absorb — the cash pile is the filed proof the business cannot reinvest.

**3. WHAT YOU ARE PAID**
- **−1.7 to −4.0 points against the sovereign** at the current price. You are paid less
  than the bond to hold the cycle, the China lever, and the merger dilution.

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- sovereign used **5.24%** — **the bare rate, no per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01].** Zero-growth capitalization of owner
earnings at the 5.24% sovereign, with the net cash (~$546M ≈ **$17.70/share**) stated as
a separate, additive line — spent once, not blended into the yield:
- earnings stream: leave-two-out $48.9M → ~$30/sh · judged $70M → **~$45/sh** · all-boom
  5-yr $126.5M → ~$78/sh
- **value including net cash: roughly $50 (conservative) · ~$60-65 (judged) · ~$95
  (optimistic, on the construction [E4-41] rejects)**
- at the ~10% floor: roughly **$33-58/share, judged ~$40**
- **current price $115.08 (2026-09-04, aggregator, flagged) — ABOVE THE ENTIRE ZERO-GROWTH
  BAND, including the boom-window optimistic end with the full cash pile credited.**

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- floor verdict: honest pre-tax expectancy **~4-7%** vs ~10% → **QUIT ON. The ranking
  lines are not filled in.**

**WHICH BAR?**
- [x] **Screamer test [E4-01]** — the price does not clear even the optimistic case;
  **outcome three: above the whole range → no.** No margin was added on top of the
  conservative case (none was needed to decide).
- **Windage count: ONE** — the [E4-41] downward normalization of the mean (judged $70M
  vs the boom windows). Everything else ran at realistic inputs: bare sovereign, full
  net-cash credit, reported-charge SBC, capex/D&A higher-of. The generous displays (5-yr
  boom window, full cash credit) run AGAINST the verdict and it survives them.

- **VERDICT: FAIL AT Q5, ON PRICE, AT THE [E4-28] FLOOR — quit on, not ranked.** All four
  business gates are IN; the eighth name in the queue's history to clear them (after ORLY,
  BRK-B, MCD, HAS, COKE, TSCO, SBUX), and the first semiconductor name. The business
  survives; the price already banks the next boom.

## Q6 — NOT OPENED (no entry; no position exists).
**Pre-committed re-look, per queue practice:** ~$60-65/share at a 5.24% sovereign,
recomputed at the rate of the day — **and the whole file re-opens, not re-prices, the day
the Veeco merger closes** (the standalone series stops describing the company; combined
filings required). Thesis-relevant monitors if ever re-run: China licence policy (any
denial to a mature-node customer); Kingstone/CETC implanter revenue (the Wanye SSE annual
report — the row's open work order); aftermarket series vs installed base; backlog
integrity (any second correction is a different event under [E4-52]); SAMR outcome by the
2027-06-30 outside date.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q6 not opened — no entry exists;
  the queue's standing practice for price-fails)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** The one
  candidate — Q2's Kingstone gap — was adjudicated in place: no outcome of the missing
  fetch moves the verdict, so it is a monitoring work-order, not a PROVISIONAL class.
- [x] No UNRESEARCHED verdicts issued; the open work order (Wanye SSE annual report,
  exchange-filings rung, blocked by language/platform) is recorded at Q2 and Q6-note
- [x] No UNKNOWABLE verdicts issued
- [x] Step 0: 10-K and 10-Q read with accession numbers; TWO figures cross-checked to the
  dollar (OCF FY2025 $118,305k; capex line $(11,295)k)
- [x] Owner earnings on multi-year means; SIX windows published; capex band disclosed as
  a judgment (higher-of capex/D&A; R&D-as-real-(c) stated)
- [x] Competitor row filled: 4 filers + merger partner on identical formulas; nil-disclosure
  and rung-blocked peers stated with obstacles named
- [x] Sovereign 5.24%, USD (the earnings currency), US Treasury daily par yield curve
  (issuing authority), dated 2026-09-04
- [x] Value as round-number range ($50 / $60-65 / $95 with cash)
- [x] One bar (screamer, outcome three); windage count ONE, stated
- [x] Price dated 2026-09-04, aggregator, flagged as live-quote-only
- [x] Committed after Q1, Q2, Q3, Q4, and at close

**DEFECTS CONFESSED, this run:**
1. **A broad `git add -A "Test Runs/"` at the Q2 commit swept a parallel BMI run's
   research files into this run's commit** — the SBUX defect repeated despite being
   logged there. Explicit paths used for every commit after.
2. **The FY2023 10-K/A's stated purpose was not extracted** (two fetch attempts; the
   explanatory note did not surface in the text conversion). Recorded as a loose end;
   given its five-day gap after the original and no accompanying restatement, most
   plausibly administrative — NOT adjudicated.
3. **No China revenue percentage exists in any 10-K read (FY2022-25)** — the brief's
   "40-60%+" China share could not be verified from filings; the run substituted the
   filed instruments (Asia 76.0% of system shipments; the export-control risk factors).
   The absence itself is recorded as a candor observation at Q3.
4. **Quarterly bookings/book-to-bill disclosure history in earnings releases was not
   vintage-checked** (annual 10-K backlog+bookings series WAS built and is continuous);
   an [E2-49] check on the ER cadence remains open.
5. **Session kill mid-Q3** — survived with zero question loss under the write-early
   protocol; resumed from the committed file and the coordinator's pointer.
6. run.py share-basis defect (weighted average vs cover count) bit again and was
   corrected by hand — the standing queue-wide tool defect.

## REGISTER
- Verdict: **FAIL at Q5, ON PRICE, at the [E4-28] floor — about the price, not the
  business. Q1 IN · Q2 IN (NARROW) · Q3 IN (overlay) · Q4 IN.**
- One line: **A genuinely narrow franchise (two full-range implant makers, growing
  installed base, prices held through the bust) whose quote already banks the next boom:
  every owner-earnings construction yields 1.2-3.6% against a 5.24% bond, and the pending
  Veeco merger will shortly make the filed history describe a company that no longer
  exists.**
- Open work order (does not gate this verdict): Kingstone implanter series via Wanye
  Enterprises (SSE 600641) annual report · exchange-filings rung · blocked by
  language/platform access this session.
