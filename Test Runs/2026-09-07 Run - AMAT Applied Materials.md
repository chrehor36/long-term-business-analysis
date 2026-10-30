# Company Run — APPLIED MATERIALS, INC. (AMAT) — 2026-09-07
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
it is UNKNOWABLE. **[E4-18]**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- **rate 5.24%** · **date 2026-09-04** · source: **US Treasury daily par yield curve,
  30-year, from the issuing authority** (`tools/sources.py`, struck fresh this run per the
  2026-09-02 correction; FRED is the fallback, not the source).
- Earnings currency: **USD**. AMAT is a Delaware domestic filer reporting in USD. 89% of
  FY2025 revenue was to customers outside the United States by shipment destination — an
  exposure question read at Q2 and Q4, not an FX repricing question, because the tools are
  sold and the receivables carried in dollars. No ADR ratio: single class, direct Nasdaq
  listing.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Form 10-K, FY ended 2025-10-26, filed 2025-12-12, accession `0001628280-25-056742`**
  — the anchor document and the most recent annual filing in existence at run date.
- **Form 10-Q, Q3 FY2026, quarter ended 2026-07-26, filed 2026-08-20, accession
  `0001628280-26-058235`** — read in full, and it is load-bearing in this file: it carries
  the BIS export-controls settlement, a second segment recast, and nine months of results
  that post-date the 10-K by three quarters.
- **Form DEF 14A filed 2026-01-28, accession `0001193125-26-027307`** (pay, ownership,
  say-on-pay).
- Vintage 10-Ks read for the through-cycle series: FY2024 (`0000006951-24-000044`), FY2023
  (`0000006951-23-000041`), FY2020 (`0000006951-20-000048`), FY2019
  (`0000006951-19-000046`), FY2013 (`0000006951-13-000044`). Extracts in
  `Test Runs/_research 2026-09-07 AMAT/`.
- **Figures cross-checked against the filed statement (operator rule 4):** FY2025
  Consolidated Statements of Cash Flows — *Cash provided by operating activities* **$7,958M**
  and *Capital expenditures* **$(2,260)M**; both agree with the `companyfacts` series to the
  dollar. Note 15's segment reconciliation sums to the filed $28,368M revenue and $8,289M
  operating income exactly.

**Price and shares:**
- price **$454.71**, 2026-09-04 close (aggregator via `tools/sources.py` — **live quote
  only, flagged** per operator rule 5)
- shares **793,597,443**, hand-read off the **Q3 FY2026 10-Q cover**, *"Number of shares
  outstanding of the issuer's common stock as of July 26, 2026"*. **Single class.** The
  FY2025 10-K cover reads 792,943,366 as of 2025-12-05; the fresher cover is used and both
  are recorded. run.py's weighted-average diluted blend is rejected as everywhere in this
  queue.
- **market cap $360,857M** (793,597,443 × $454.71). The screen's $368,001M was struck at an
  earlier quote; the construction is the same.
- **Split guard: no split.** `split_factor_after('AMAT','2026-07-26') = 1.00`, and the filed
  cover counts run 967M (FY2018) → 916 → 914 → 892 → 844 → 833 → 818 → 793M — a monotone
  buyback decline with no step. Nothing to adjust.

---
# STAGE 0 — THE SCREEN ROW, REBUILT BY HAND. THE TRAP FIRES A SEVENTH TIME.

**Construction, as everywhere in this queue:** owner earnings = **OCF − SBC − capex** (the
conservative end) and **OCF − SBC − D&A** (the other end), $M, from `companyfacts` XBRL
taking the **originally filed** value at each fiscal-year end and flagging any later
restatement (the INTC defect: a superseded input silently inside a window).

| FY (Oct) | revenue | GM% | op inc | op m% | R&D% | OCF | SBC | D&A | of which intang. amort. | tangible D&A | capex | capex ÷ tang. D&A | **OE (capex end)** | OE (D&A end) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2007 | 9,734.9 | 46.1 | 2,371.5 | 24.4 | 11.7 | 2,209.3 | 161.2 | 268.3 | 0.0 | 268.3 | 264.8 | 1.0 | **2,048.1** | 2,048.1 |
| 2008 | 8,129.2 | 42.4 | 1,355.4 | 16.7 | 13.6 | 1,710.5 | 178.9 | 320.1 | 0.0 | 320.1 | 287.9 | 0.9 | **1,531.5** | 1,531.5 |
| **2009 ↓ −38.3%** | **5,013.6** | **28.5** | **−393.6** | **−7.9** | 18.6 | 332.7 | 147.2 | 291.2 | 0.0 | 291.2 | 248.4 | 0.9 | **185.5** | 185.5 |
| 2010 | 9,548.7 | 38.9 | 1,383.7 | 14.5 | 12.0 | 1,722.9 | 126.1 | 304.5 | 0.0 | 304.5 | 169.1 | 0.6 | **1,596.8** | 1,596.8 |
| 2011 | 10,517.0 | 41.5 | 2,398.0 | 22.8 | 10.6 | 2,426.0 | 146.0 | 246.0 | 52.0 | 194.0 | 209.0 | 1.1 | **2,071.0** | 2,280.0 |
| **2012 ↓ −17.1%** | **8,719.0** | **38.0** | 411.0 | 4.7 | 14.2 | 1,851.0 | 182.0 | 422.0 | 224.0 | 198.0 | 162.0 | 0.8 | **1,507.0** | 1,669.0 |
| **2013 ↓ −13.9%** | **7,509.0** | **39.8** | 432.0 | 5.8 | 17.6 | 623.0 | 162.0 | 410.0 | 199.0 | 211.0 | 197.0 | 0.9 | **264.0** | 461.0 |
| 2014 | 9,072.0 | 42.4 | 1,520.0 | 16.8 | 15.7 | 1,800.0 | 177.0 | 375.0 | 184.0 | 191.0 | 241.0 | 1.3 | **1,382.0** | 1,623.0 |
| 2015 | 9,659.0 | 40.9 | 1,693.0 | 17.5 | 15.0 | 1,163.0 | 187.0 | 371.0 | 186.0 | 185.0 | 215.0 | 1.2 | **761.0** | 976.0 |
| 2016 | 10,825.0 | 41.7 | 2,152.0 | 19.9 | 14.2 | 2,466.0 | 201.0 | 389.0 | 189.0 | 200.0 | 253.0 | 1.3 | **2,012.0** | 2,265.0 |
| 2017 | 14,537.0 | 44.9 | 3,868.0 | 26.6 | 12.2 | 3,609.0 | 220.0 | 407.0 | 193.0 | 214.0 | 345.0 | 1.6 | **3,044.0** | 3,389.0 |
| 2018 | 16,705.0 | 46.8 | 4,796.0 | 28.7 | 12.1 | 3,787.0 | 258.0 | 457.0 | 199.0 | 258.0 | 622.0 | 2.4 | **2,907.0** | 3,529.0 |
| **2019 ↓ −12.6%** | **14,608.0** | **43.7** | 3,350.0 | 22.9 | 14.1 | 3,247.0 | 263.0 | 363.0 | 57.0 | 306.0 | 441.0 | 1.4 | **2,543.0** | 2,621.0 |
| 2020 | 17,202.0 | 44.7 | 4,365.0 | 25.4 | 13.0 | 3,804.0 | 307.0 | 376.0 | 56.0 | 320.0 | 422.0 | 1.3 | **3,075.0** | 3,121.0 |
| 2021 | 23,063.0 | 47.3 | 6,889.0 | 29.9 | 10.8 | 5,442.0 | 346.0 | 394.0 | 49.0 | 345.0 | 668.0 | 1.9 | **4,428.0** | 4,702.0 |
| 2022 | 25,785.0 | 46.5 | 7,788.0 | 30.2 | 10.7 | 5,399.0 | 413.0 | 444.0 | 40.0 | 404.0 | 787.0 | 1.9 | **4,199.0** | 4,542.0 |
| 2023 | 26,517.0 | 46.7 | 7,654.0 | 28.9 | 11.7 | 8,700.0 | 490.0 | 515.0 | 44.0 | 471.0 | 1,106.0 | 2.3 | **7,104.0** | 7,695.0 |
| 2024 | 27,176.0 | 47.5 | 7,867.0 | 28.9 | 11.9 | 8,677.0 | 577.0 | 392.0 | 0.0 | 392.0 | 1,190.0 | 3.0 | **6,910.0** | 7,708.0 |
| 2025 | 28,368.0 | 48.7 | 8,289.0 | 29.2 | 12.6 | 7,958.0 | 668.0 | 435.0 | 0.0 | 435.0 | **2,260.0** | **5.2** | **5,030.0** | 7,290.0 |

*(Values are the ORIGINALLY FILED ones. **Restatements found across vintages and recorded,
none of which touches a window boundary or changes a verdict:** OCF FY2016 $2,466M → $2,566M
and FY2017 $3,609M → $3,789M (the ASU 2016-09 excess-tax-benefit reclassification); operating
income FY2017 $3,868M → $3,936M and FY2018 $4,796M → $4,491M; sub-$1M rounding differences in
FY2009–11. **The FY2018 operating-income restatement is DOWNWARD by $305M and is the one
worth naming**, because it sits inside the [E4-41] pre-wave window used below; the
owner-earnings series is unaffected, since it is built from cash flow.)*

## THE SCREEN'S 34.6% SPREAD IS THE FOURTH SPREAD DEFECT AGAIN — SEVENTH CONSECUTIVE RUN

The queue row reads `cap_m 368,001 · oe_bottom_m 5,512 · oe_top_m 7,419 · spread 0.346 ·
growth_required 0.085 · level_shift 2.0`. **Both ends reproduce TO THE DOLLAR, and the width
between them is still not a width:**

- **`oe_top` 7,419 = the 3-year FY2023–25 mean at the D&A end** (my rebuild: 7,419.3).
- **`oe_bottom` 5,512 = the 5-year FY2021–25 mean at the capex end, with ASC 842
  finance-lease additions added to capex** (my rebuild: **5,512.4** — exact once the $109M
  of FY2023 `RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability` is included, which
  is the COST/HD addendum fix working correctly).
- **Two different windows, two different capex ends, one number called a spread.** This is
  the identical construction that misled on AAPL, GOOGL, AVGO, AMD, INTC and KLAC. **Seventh
  consecutive firing.**

**Rebuilt over six windows and both capex ends, per [E4-25]** — *"working with a range of
possibilities is the better approach"* — and per **[E4-38]**'s remedy, **publish every
window**:

| window | capex end | yield | D&A end | yield | growth needed to reach the 10% floor |
|---|---|---|---|---|---|
| 3-yr FY2023–25 | **6,348.0** | 1.759% | 7,419.3 | 2.056% | 8.24% |
| 5-yr FY2021–25 *(the corpus default [E2-42])* | **5,534.2** | 1.534% | 6,300.4 | 1.746% | 8.47% |
| 8-yr FY2018–25 | **4,524.5** | 1.254% | 5,039.5 | 1.397% | 8.75% |
| 10-yr FY2016–25 | **4,125.2** | 1.143% | 4,517.4 | 1.252% | 8.86% |
| 15-yr FY2011–25 | **3,149.1** | 0.873% | 3,357.3 | 0.930% | 9.13% |
| 19-yr FY2007–25 | **2,768.4** | 0.767% | 2,870.4 | 0.795% | 9.23% |
| 5-yr leave-two-out | 4,552.3 | 1.262% | | | 8.74% |
| 10-yr leave-two-out | 3,404.8 | 0.944% | | | 9.06% |
| **best year ever filed (FY2023)** | **7,104.0** | **1.969%** | 7,708.0 (FY2024) | **2.136%** | **7.86%** |

- **TRUE WIDTH: 2,768.4 to 7,708.0 = 2.78x, a 178.4% spread.** The screen said 34.6%. The
  brief's warning was correct and is now confirmed for the seventh consecutive name.
- **The width does not change the verdict, and that is what has to be said plainly.** Every
  construction in the table — including the best single year AMAT has ever filed at the (c)
  = D&A ceiling — yields **under 2.2% against a 5.24% sovereign.**

## [E4-41] — THE STEP TEST IS WRONG TOO, IN THE SAME DIRECTION AS KLAC'S

The row says `level_shift 2.0 · STEP UP — normalize down`. By hand:
- **pre-wave five-year mean, FY2014–18: $2,021.2M**
- **wave five-year mean, FY2021–25: $5,534.2M**
- **step = 2.74x**, not 2.0x. *(On the alternative pre-wave window FY2015–19, $2,253.4M, the
  step is 2.46x. Both are materially above the flag's reading; neither is below it.)*

*"Favourable exogenous breaks in the window are named and removed before the mean is
trusted"* **[E4-41]**. They are named at Q4. Recorded here: the current level is a wave, and
the screen measured the wave at three-quarters of its true height.

## THE OTHER STAGE-0 CHECKS, BY HAND

- **Cover count** — done above; no split, monotone decline, 793,597,443 from the freshest
  filed cover.
- **Dividend + RPM decomposition.** Dividends paid, $M: 306 (FY07) · 325 · 320 · 349 · 397 ·
  434 · 456 · 485 · 487 · 444 · 430 · 605 · 771 · 787 · 838 · 873 · 975 · 1,192 · **1,384
  (FY25)**. Declared per share $0.06 (FY08) → **$1.78 (FY25)**. The dollar total has risen
  every year since FY2017 and the per-share figure every year since FY2014 — **eleven
  consecutive years of per-share increases, +12.7%/yr compounded over eleven, no cut and no
  freeze.** The **RPM decomposition**: FY2025 dividends $1,384M are **17.4% of operating cash
  flow**, and dividends plus buybacks $6,279M are **78.9%** of it. The *rate* per share is
  rising **faster than the dollar total** (+17.1%/yr per share against +12.4%/yr in dollars
  over eight years) — i.e. **roughly a quarter of the per-share dividend growth is the share
  count falling, not the payout rising.** That is real for a holder and is recorded as such,
  not as operating growth. There is **no dividend funded by issuance [E2-52]**: net share
  issuance is negative in every year of the eleven.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, without management's language.** A chip is built by
depositing a film a few atoms thick, cutting a pattern into it, and repeating that several
hundred times. AMAT sells the machines that put the material down and take it away:
deposition (CVD, PVD, epitaxy), etch, ion implantation, chemical-mechanical polishing,
thermal processing, and the packaging tools that stack finished die. It also sells inspection
and metrology, where it is the challenger rather than the incumbent. **AMAT is the widest
catalogue in the industry and is the only company that sells across essentially every
materials step.** A fab picks a tool for a given step at a given node, qualifies it into the
process of record, and then buys that tool for every copy of that fab — so a design win is a
multi-year, multi-fab annuity in units, and the money arrives as a capital order.

Then the second business, and it is where the claim in the brief lives:
- **Applied Global Services (AGS)** sells spares, service contracts, upgrades and factory
  software against the installed base. *"Demand for AGS' service and spares is driven by our
  large and growing installed base of manufacturing systems"* (Item 7). It is the fab's
  **operating** decision rather than its capital decision, which is why it is expected to
  hold up when the capital line does not.

**The filing splits the two, and — this is the finding the brief asked for — it splits them
at the GROSS PROFIT line, which is what makes the profit-mix test possible:**

| FY2025, Note 15 | revenue | costs of products sold | gross profit | **gross margin** | operating income | operating margin |
|---|---|---|---|---|---|---|
| **Semiconductor Systems** | **$20,798M** | 9,530 | **$11,268M** | **54.2%** | **$7,379M** | 35.5% |
| **Applied Global Services** | **$6,385M** | 4,251 | **$2,134M** | **33.4%** | **$1,792M** | 28.1% |
| Corporate and Other | $1,185M | 779 | $406M | 34.3% | $(882)M | — |
| **Total** | **$28,368M** | 14,560 | **$13,808M** | **48.7%** | **$8,289M** | 29.2% |

**The scarce input this business controls.** Three, and they are different in kind:
1. **Materials-process know-how at atomic scale** — recipes, chamber design and the
   metallurgy that makes a film uniform across a 300mm wafer at production throughput.
   Defended with **RD&E of $3,570M, 12.6% of revenue** (FY2025), a line that has fallen in
   only three of nineteen years.
2. **The process of record.** A qualified tool is not swapped mid-node without re-qualifying
   the step, which is expensive and slow. This is what makes the installed base sticky and
   what feeds AGS.
3. **Breadth itself** — the ability to co-optimise adjacent steps that a single-process
   vendor cannot see. **Whether breadth is a moat or merely a catalogue is the whole of Q2
   and it is not conceded here.**

**Will the fundamentals look broadly the same in ten years?** The *mechanism*, yes: chips
will still be built by deposition and removal, and someone will sell the machines. The
*level*, no — and the nineteen-year filed record says so without needing a forecast: revenue
9,735 → 5,014 → 10,517 → 7,509 → 16,705 → 14,608 → 28,368, with an **operating loss of
$393.6M in FY2009** and gross margin at **28.5%** that year against 48.7% now. Owner earnings
have run from **$185.5M to $7,104M** in the same window. The business is legible; its level
is not stable. That is a Q4 and Q5 fact, not a Q1 failure — the ACLS and KLAC precedent.

- **VERDICT: [x] IN**

*Recorded against myself under operator rule 9: this Q1 pass rests on the business being
simple and legible, not on it being good. The INTC precedent is the standing warning that a
semiconductor business can be perfectly understandable and still fail Q2 on its own filed
evidence. Q2 is decided on the row and on the pricing test, not on the description above.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The brief's claim: the broadest equipment franchise — deposition, etch, implant, CMP,
process control — plus a large installed-base annuity in AGS; breadth plus installed base
rather than KLA's single-process dominance. The brief's own stated way of being wrong
[E4-26]: that breadth is not dominance, because AMAT competes head-on with Lam in etch and
with TEL in deposition where KLA competes with nobody at scale. Both were run straight.
The prior was right, and it is right by more than the brief expected.**

**VERDICT IN ADVANCE, so the evidence below can be read against it: IN, NARROW — and
NARROWER THAN KLAC'S NARROW, on filed facts that KLA's file does not contain.**

### The three criteria [E3-03]

- **(1) Needed or desired — YES.** No chip is built without deposition, etch and implant.
  The tool is bought to make the fab exist at all.
- **(2) No close substitute — PASSES ONLY AT THE SOCKET, AND FAILS AT THE PURCHASE DECISION.
  This is the sharpest difference from KLA and it is evidenced from the attacker's filing,
  not from AMAT's.**
  > *"We face significant competition with all of our products and services. **Our primary
  > competitor in the dielectric and metals deposition market is Applied Materials, Inc.**
  > For ALD and PECVD, we also compete against ASM International and Wonik IPS. **In the etch
  > market, our primary competitors are Applied Materials, Inc.; Hitachi, Ltd.; and Tokyo
  > Electron, Ltd.**, and our primary competitors in the wet clean market are Screen Holding
  > Co., Ltd.; Semes Co., Ltd.; and Tokyo Electron, Ltd."*
  > — **Lam Research, Form 10-K FY2026 (ended 2026-06-28), filed 2026-08-07, accession
  > `0000707549-26-000037`, Item 1, "Competition"**

  **Set that beside what KLA's file contained.** Nova's 20-F says of KLA's market: *"the
  market for process control systems used in semiconductor manufacturing **is currently
  concentrated and characterized by relatively few participants**."* **No filing in this
  cohort says anything of the kind about deposition or etch.** Lam names AMAT plus five
  other companies across AMAT's largest markets, and Lam is the etch leader.

  What DOES pass is the socket-level lock, and the same two registrants file the mechanism:
  > *"once a semiconductor manufacturer has selected a particular supplier's equipment and
  > **qualified it for production, the manufacturer generally maintains that selection for
  > that specific production application and technology node**"* — Lam, same filing
  >
  > *"**A substantial investment is required by the customers to evaluate, test, select and
  > integrate capital equipment into a production line.** As a result, once a manufacturer
  > has selected a particular vendor's capital equipment … the manufacturer generally relies
  > upon that equipment for the specific production line application"* — Nova Ltd, 20-F
  > FY2025, acc. `0001178913-26-000504`

  **So criterion (2) passes per socket and per node, and fails per contest.** That is
  exactly what NARROW means and it is why the class cannot be WIDE.
- **(3) Not price-regulated — passes on price; the [E2-59] inversion applies and it has now
  cost real money.** Nobody caps AMAT's prices. What is regulated is *who it may sell to*,
  and in FY2026 that regime produced a **$253 million settlement with the Commerce
  Department's Bureau of Industry and Security** (Q3 FY2026 10-Q, Note 13) — read at Q3. The
  moat belongs to the regime, in either direction, and the regime has moved against AMAT.

### [E4-04] — must the moat be continuously rebuilt?

**This is the DEFENCE case, but by a narrower margin than KLA's, and AMAT's own filing is
the reason to hesitate:**
> *"**The rapid pace of technological change can quickly diminish the value of current
> technologies and products and create opportunities for existing and new competitors.**
> … some applications create the need for **an entirely different technological approach**."*
> — FY2025 10-K, Item 1, "Competition"

That is nearer to [E4-04]'s excluded class than anything in KLA's 10-K. It is held on the
defence side of the line because the *basis* being defended — atomic-scale materials
know-how and the qualified process of record — persists across nodes and is repaired by
**RD&E of $3,570M (12.6% of revenue)**, not replaced wholesale at $20–25bn a year the way
INTC's node is. **A lapse narrows the lead; it does not vaporise the installed base.**
Recorded as the closest call in this section. **No key-person dependence found [E4-23].**

### THE PRICING TEST — [E2-44](1), THE ONE TEST A NO-MOAT SUPPLIER CANNOT PASS

**Stated as a limit before it is used: AMAT files no ASP series, no price list and no price
range.** *Recorded sweep of the FY2025, FY2024, FY2023, FY2020, FY2019 and FY2013 10-Ks: no
instance found of an average selling price figure, a price range, or a unit price.* What it
does file is a **direction**, twice, and both times upward:
> *"Gross margin in fiscal 2023 increased … driven by favorable changes in customer and
> product mix and **an increase in average selling prices**"* — FY2023 10-K
>
> *"Semiconductor Systems' operating margin for fiscal 2025 increased … favorable changes in
> customer and product mix, lower material and manufacturing costs, and **an increase in
> average selling prices**"* — FY2025 10-K

*Recorded sweep: the phrase appears in the FY2023 and FY2025 10-Ks and **no instance is found
in the FY2019, FY2020 or FY2024 10-Ks** — it is filed in up-years and absent in the down-year.
That asymmetry is itself an [E4-37] agony-metric reading.*

**So the [E2-44](1) test must run on gross margin, and it must run SAME-VINTAGE, because AMAT
restated FY2018 cost of sales by roughly $300M and a mixed-vintage comparison overstates the
fall. Every revenue decline in the nineteen-year filed record, on the presentation of the 10-K
that reported it:**

| downturn | revenue | change | gross margin, prior → year | move |
|---|---|---|---|---|
| **FY2009** | $5,013.6M | **−38.3%** | 42.4% → **28.5%** | **−13.9 pts** |
| **FY2012** | $8,719M | **−17.1%** | 41.5% → **38.0%** | **−3.5 pts** |
| **FY2013** | $7,509M | **−13.9%** | 38.0% → **39.8%** | **+1.8 pts** ✓ |
| **FY2019** | $14,608M | **−12.6%** | 45.0% → **43.7%** | **−1.3 pts** |

**AMAT's gross margin fell in three of its four filed revenue declines. Its own FY2019 MD&A
says why, in its own words:** *"Gross margin in fiscal 2019 decreased compared to fiscal 2018,
**primarily due to the decrease in net sales** and unfavorable changes in customer and product
mix."* **A margin that falls "primarily due to the decrease in net sales" is the signature of
a price-taker with operating leverage — the opposite of what [E2-44](1) asks for.**

**And the mix defence runs the WRONG WAY in FY2019, which makes the reading worse, not
better.** The segment that collapsed that year was Display (−28.2%), whose operating margin
(25.0% in FY2018) was **below** Semiconductor Systems' (32.5%). Losing the lower-margin
segment should have *raised* consolidated gross margin by mix. **It fell 1.3 points anyway.**

**Set that beside the two precedents this run is measured against:**
- **ACLS: filed system price range ROSE ($2.4–10.0M → $2.6–12.0M) and gross margin ROSE
  43.7% → 44.9% through a 26% revenue collapse.**
- **KLAC: Semiconductor Process Control segment gross margin ROSE 63.89% → 64.46% while that
  segment's revenue FELL 6.3%, mix-free at the segment level.**
- **AMAT: no filed price instrument at all, and gross margin down 1.3 points on a 12.6%
  decline, down 3.5 on a 17.1% decline, and down 13.9 on a 38.3% decline.**

### THE SEGMENT-LEVEL, MIX-FREE VERSION CANNOT BE RUN, AND THE REASON IS DATED

**AMAT adopted ASU 2023-07 in the fourth quarter of fiscal 2025 and now files segment gross
profit and gross margin — the first name in this equipment cohort to do so.** The disclosure
exists for **FY2023, FY2024 and FY2025 only** (Note 15, prior years recast).

| Note 15 | FY2023 | FY2024 | FY2025 | 9M FY2026 *(second recast)* |
|---|---|---|---|---|
| Semiconductor Systems revenue | $19,698M | $19,911M | $20,798M | $18,146M |
| **Semiconductor Systems gross margin** | **52.0%** | **52.9%** | **54.2%** | **54.8%** |
| AGS revenue | $5,732M | $6,225M | $6,385M | $5,005M |
| **AGS gross margin** | **31.8%** | **34.3%** | **33.4%** | **34.9%** |
| consolidated gross margin | 46.7% | 47.5% | 48.7% | 49.8% |

**Semiconductor Systems revenue ROSE in every one of those years** (19,698 → 19,911 → 20,798;
and $18,146M for nine months of FY2026 against $16,562M recast). There is therefore **no
revenue decline anywhere inside the window for which segment gross margin is filed**, and the
mix-free ACLS/KLAC test is **not runnable on AMAT at all.** That is a finding, not an
omission: the one instrument that cleared both precedents does not exist here, and the
consolidated substitute — the only one available — **fails in three of four downturns**.

*The genuine counterweight, hunted per [E4-26] and stated at its strongest: the Semiconductor
Systems segment's gross margin has risen 52.0% → 54.8% across three years in which AMAT's own
MD&A twice names rising average selling prices as a cause, and consolidated gross margin has
risen 41.7% (FY2016) → 49.8% (9M FY2026), +8.1 points. That is real, filed pricing evidence
and it is why this gate is IN rather than OUT. What it is not is the [E2-44](1) test, which
asks specifically about "**when product demand is flat and capacity is not fully utilized**" —
a condition AMAT has not been in since FY2019, and the FY2019 answer was negative.*

### AGS — THE FRANCHISE-INSIDE-THE-FRANCHISE, AND THE PROFIT-MIX TEST *IS* RUNNABLE

**This is the first equipment name in this queue where the HAS/EFX profit-mix test can be
run, because AMAT files segment cost of products sold and KLA does not. That is itself the
finding the brief asked for. The answer is that the annuity is the LOW-margin half.**

| | share of revenue | **share of gross profit** | share of operating income |
|---|---|---|---|
| AGS, FY2023 | 21.6% | **14.7%** | 20.0% |
| AGS, FY2024 | 22.9% | **16.6%** | 23.0% |
| AGS, FY2025 | 22.5% | **15.5%** | 21.6% |
| **AGS, 9M FY2026 (recast)** | **20.8%** | **14.6%** | **19.7%** |

- **AGS gross margin is 33.4% against Semiconductor Systems' 54.2% — the annuity earns
  roughly three-fifths of the gross margin of the capital-equipment business it hangs off.**
  The received story about equipment companies is that the service annuity is the
  high-quality earnings stream. **On AMAT's own filed numbers it is not.** The dog wags the
  tail: **Semiconductor Systems is 73% of revenue, 82% of gross profit and 80% of
  pre-corporate operating income.**
- *Why AGS's operating margin (28.1%) is nonetheless close to Systems' (35.5%): AGS carries
  almost no RD&E — **$126M against Systems' $3,042M**. It is a distribution-and-labour
  business bolted onto someone else's research. That is a real economic fact and it cuts both
  ways: low reinvestment need, low differentiation, and AMAT's own filing names the
  competition as *"a diverse group of third-party service providers as well as customers that
  choose to perform their own service."***
- **What the annuity DOES pass — the FY2019 downturn test, on revenue, and it passes
  cleanly.** In FY2019 **Semiconductor Systems revenue fell 14.7% ($10,577M → $9,027M) while
  AGS revenue ROSE 2.7% ($3,754M → $3,854M)** and AGS operating income was flat ($1,102M →
  $1,101M) against Systems' −28.4%. That is what an installed-base annuity is supposed to do
  and it did it.
- **And the backlog, which is the strongest single fact FOR the annuity in this file:**

| backlog by segment, $M | FY2018 | FY2019 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| **Semiconductor Systems** | 2,479 | 2,925 | **12,691** | 11,127 | 8,259 | **7,105** |
| **Applied Global Services** | 1,751 | 2,073 | 5,643 | 5,162 | 6,767 | **7,141** |
| Display / Other | 1,862 | 1,475 | 677 | 882 | 847 | 756 |
| **total** | 6,092 | 6,473 | **19,011** | 17,171 | 15,873 | **15,002** |

  **AGS backlog has grown 26.5% in three years while Semiconductor Systems backlog has fallen
  44.0%, and total backlog has fallen 21.1% while revenue rose 10.0%.** The annuity's order
  book is compounding while the capital-equipment order book drains. **Carried with the
  registrant's own caveat** — *"Our backlog on any particular date is not necessarily
  indicative of actual sales for any future periods"* — and with the FY2024 disclosure that
  *"As a result of new export rules and regulations issued in December 2024, backlog as of
  October 27, 2024 is expected to be reduced by approximately $549 million."* It is carried
  to Q6 as the most informative forward series AMAT files.
- **The peer comparison the annuity claim needs, and it does not flatter AMAT.** Lam
  Research's Customer Support Business Group is **$8,347.2M of $23,232.7M = 35.9% of
  revenue** (FY2026 10-K, Note 4) against AGS's 22.5%. **The installed-base annuity is a
  proportionally SMALLER part of AMAT than of its closest competitor** — and Lam, operating
  in **one reportable segment**, files no gross profit for it, so the comparison can be made
  on revenue only.

### [E4-55] — WHERE UNITS EXIST, MONITOR UNITS. HERE THEY DO NOT EXIST.

*Recorded sweep of the FY2025, FY2024, FY2023, FY2020, FY2019 and FY2013 10-Ks for: an
installed-base count, systems shipped, tools shipped, units shipped, chambers installed, or
any absolute count of equipment.* **No instance found.** The FY2025 10-K uses *"our large,
global installed base"* and *"our large and growing installed base of manufacturing systems"*
**four times and never sizes it**. The only counts in the document are **more than 23,500
active patents** and the employee count.

**This is the KLAC outcome, not the ACLS one — worse than ACLS, which filed roughly 3,400
tools rising through its bust.** *(The same absence holds for the closest peer: recorded sweep
of Lam's FY2026 10-K — no installed-base count found there either.)* **AMAT can be read in
dollars only. Revenue growth cannot be decomposed into price and volume from any filing.**
The **segment backlog series above is the nearest available substitute and it is not the same
thing** — it is a forward order book, not a physical count. Carried as a named blind spot and
one of the reasons the class is NARROW.

### THE COMPETITOR ROW — required [E3-28]

**Identical formula for every filer**, carried over from the KLAC run of 2026-09-07 which
built it: **OP = revenue − cost of revenue − R&D − SG&A**; **ROUNTOA = OP ÷ (assets −
goodwill − intangibles − non-interest-bearing current liabilities)**, year-end denominators —
*a CONVENTION of this row, [E2-43] in the closest computable form.* Latest full fiscal year
each. **AMAT's own cells were recomputed independently in this run and agree** (op margin
29.9%; ROUNTOA 34.8% here against the KLAC row's 34.5%, an intangibles-tag rounding
difference that changes nothing).

| | **AMAT** | KLAC | LRCX | ASML | ONTO | CAMT | NVMI | ACLS |
|---|---|---|---|---|---|---|---|---|
| latest FY | **FY2025 10/26/25** | FY2026 6/30/26 | FY2026 6/28/26 | FY2025 cal | FY2025 1/3/26 | FY2025 cal | FY2025 cal | FY2025 cal |
| form · accession | 10-K `0001628280-25-056742` | 10-K `0000319201-26-000027` | 10-K `0000707549-26-000037` | 20-F `0001628280-26-011378` | 10-K `0001193125-26-066937` | 20-F `0001178913-26-001561` | 20-F `0001178913-26-000504` | 10-K `0001104659-26-020461` |
| revenue | **$28,368M** | $13,579.5M | $23,232.7M | €32,667.3M | $1,005.3M | $496.1M | $880.6M | $839.0M |
| gross margin | **48.7%** | **61.3%** | 50.5% | 52.8% | 49.7% | 50.5% | 57.4% | 44.9% |
| R&D % revenue | **12.6%** | 11.3% | 10.2% | 14.4% | 13.1% | 9.7% | 16.3% | 13.0% |
| **operating margin** | **29.9%** | **41.7%** | **35.3%** | 34.6% | 19.0% | 25.8% | 28.8% | 14.2% |
| **ROUNTOA** | **34.8%** | 48.5% | **52.0%** | 49.4% | 15.7% | 12.0% | 12.6% | 10.2% |
| goodwill | $3,707M | $1,788.8M | $1,630.0M | €4,588.6M | $644.0M | $74.3M | $90.8M | none |

*ASML is left in **EUR, not converted** — a stated rung limitation; only its margins and
ratios are comparable, not its levels.*

**GROSS MARGIN THROUGH BOTH RECENT DOWNTURNS, the [E2-44] test across the cohort** (carried
from the KLAC row, same formula, same windows; AMAT's cells are same-vintage as filed):

| FY | **AMAT** | KLAC | LRCX | ASML | ONTO | CAMT | NVMI | ACLS |
|---|---|---|---|---|---|---|---|---|
| 2018 | 45.0 | 64.2 | 46.6 | 46.0 | 54.2 | 49.4 | 57.8 | 40.6 |
| **2019 ↓** | **43.7** | 59.1 | 45.1 | 44.7 | 44.1 | 48.3 | 54.2 | 42.0 |
| 2021 | 47.3 | 59.9 | 46.5 | 52.7 | 54.4 | 50.9 | 56.6 | 43.2 |
| 2022 | 46.5 | 61.0 | 45.7 | 50.5 | 53.6 | 49.8 | 55.5 | 43.7 |
| **2023 ↓** | 46.7 | 59.8 | 44.6 | 51.3 | 51.5 | 46.8 | 56.6 | 43.5 |
| **2024 ↓** | 47.5 | 60.0 | 47.3 | 51.3 | 52.2 | 48.9 | 57.6 | 44.7 |
| 2025 | **48.7** | 60.9 | 48.7 | 52.8 | 49.7 | 50.5 | 57.4 | 44.9 |
| 2026 | *(FY ends 10/2026)* | 61.3 | 50.5 | — | — | — | — | — |

**The row's six findings, and four of them cut against the subject:**
1. **AMAT is the LARGEST company in the cohort by revenue — more than twice KLA — and it
   ranks SIXTH of eight on gross margin and FOURTH of eight on operating margin.** Scale has
   not bought margin. KLA at half AMAT's revenue earns 12.6 more points of gross margin and
   11.8 more points of operating margin.
2. **Its closest head-on competitor beats it on both capital measures.** **Lam Research earns
   a 35.3% operating margin and a 52.0% ROUNTOA against AMAT's 29.9% and 34.8%** — and Lam is
   the company that names AMAT as its primary competitor in the two markets that are the core
   of Semiconductor Systems. **A franchise is a claim about *relative* position [E3-28], and
   on the relative claim the broad incumbent is being out-earned by the focused challenger in
   the incumbent's own biggest markets.** This is the single most damaging cell in the file
   and it is stated where it cannot be missed.
3. **AMAT's return on tangible operating capital is FALLING while the industry booms:**
   50.8% (FY2022) → 39.6% → 34.7% → **34.8% (FY2025)**. The incremental arithmetic, per
   **[E2-56]**'s instruction to judge retention incrementally rather than on the blended
   return:

   | window | Δ operating income | Δ unleveraged NTOA | **incremental pre-tax return** |
   |---|---|---|---|
   | FY2013 → FY2025 | +$7,701M | +$19,164M | **40.2%** |
   | FY2016 → FY2025 | +$6,318M | +$17,102M | **36.9%** |
   | FY2019 → FY2025 | +$5,120M | +$12,745M | **40.2%** |
   | **FY2022 → FY2025** | **+$686M** | **+$9,059M** | **7.6%** |

   **Over a decade the incremental return is a superb ~40%. Over the last three years it is
   7.6% — below [E5-40]'s "quite satisfactory" ~12%.** $9.1bn of additional tangible
   operating capital has bought $686M of additional operating income, in three years of rising
   revenue. *(Named honestly: a large part of the $9.1bn is inventory and receivables built
   for a boom, plus the EPIC R&D centre, and some of it should convert. That is a reason to
   watch it, not to discount it — [E4-40] says model exposure, not experience.)*
4. **[E2-45] — the attacker's test.** Unlike KLA's file, where Onto filed that it *"selectively
   reduced prices on our systems in order to protect our market share"* and still earned
   19.0% against KLA's 41.7%, **no filing in this cohort concedes anything to AMAT.** Lam
   names it as a peer competitor without a single concession on installed base, service
   infrastructure or price conduct. ASML names it as a competitor in patterning applications.
   Nova names it among *"process equipment manufacturers … which develop … in-situ sensors and
   metrology products"* — i.e. as a **challenger** in the market KLA owns. **The only filed
   concession to AMAT anywhere in the set is Axcelis's**, recorded in the ACLS run of
   2026-09-05: of six named ion-implant competitors, **AMAT is the only other full-range
   maker.** Implant is one process step of the several Semiconductor Systems sells.
5. **Peers taken: 8 registrants, plus SIX named competitors that could not be priced.**
   *Recorded sweep of the SEC registrant index (`company_tickers.json`) and, where a ticker
   line exists, of the submissions history:* **Tokyo Electron, ASM International, SEMES and
   Wonik IPS have no SEC ticker line at all; SCREEN Holdings appears only as an unsponsored
   ADR (CIK 0001544379) whose entire filing history is five F-6 / 424B3 documents and no
   periodic report; and Hitachi, Ltd. (CIK 0000047710) DEREGISTERED on 2012-04-27 by Form
   15F-12B, its last 20-F being for FY2011.** **All six are named by Lam as primary
   competitors in AMAT's own core markets.** Adjudicated under the ACLS rule carried by the
   KLAC run: **an additional competitor can only narrow a moat, never widen one** — so the
   gap **caps the class at NARROW** rather than suspending it as PROVISIONAL, and becomes a
   **Q6 monitoring work-order**. *KLA's file had two unpriced competitors at the edges of its
   franchise. AMAT's has six, at the centre of its two largest markets.*
6. **[E3-61] limit:** the row shows position, not conduct. On conduct the filed record is
   AMAT's own twice-stated ASP increase in up-years and its own admission that FY2019 gross
   margin fell "primarily due to the decrease in net sales."

### CHINA — THE KLAC DECOMPOSITION RUN AGAIN, AND IT GIVES THE OPPOSITE ANSWER

AMAT files revenue by customer location in every vintage read (Note 15).

| FY | China $M | % of revenue | ex-China $M | China YoY | **ex-China YoY** |
|---|---|---|---|---|---|
| 2017 | 2,758 | 18.8% | 11,940 | — | — |
| 2018 | 5,047 | 30.2% | 11,658 | +83.0% | −2.4% |
| 2019 | 4,277 | 29.3% | 10,331 | −15.3% | −11.4% |
| 2020 | 5,456 | 31.7% | 11,746 | +27.6% | +13.7% |
| 2021 | 7,535 | 32.7% | 15,528 | +38.1% | +32.2% |
| 2022 | 7,254 | 28.1% | 18,531 | −3.7% | +19.3% |
| 2023 | 7,247 | 27.3% | 19,270 | −0.1% | +4.0% |
| **2024** | **10,117** | **37.2%** | **17,059** | **+39.6%** | **−11.5%** |
| **2025** | **8,529** | **30.1%** | **19,839** | **−15.7%** | **+16.3%** |

**Two findings, and they are not the KLAC findings:**
1. **The fall from 37.2% to 30.1% IS de-risking, unlike KLA's.** The KLAC run found China
   dollars *flat* while total revenue grew — a share fall with no dollar fall. **AMAT's China
   dollars fell $1,588M in absolute terms in FY2025 while ex-China revenue grew $2,780M
   (+16.3%).** That is the real thing, and it is the strongest structural fact in AMAT's
   favour that this run found.
2. **But the same table exposes what the headline conceals: FY2024's +2.7% revenue growth was
   ENTIRELY China. Ex-China revenue FELL 11.5% in FY2024.** AMAT had a real customer-side
   downturn in FY2024 that the consolidated line hides, and the pre-buy that masked it was the
   legacy-node China surge ahead of export controls. **Any reading of the FY2023–25
   segment-margin series must carry that: the "no downturn inside the window" statement above
   is true of the *reported* series and false of the underlying non-China one.**
   *(Whether the China mix is higher or lower margin for AMAT is not determinable from the
   filing — no instance found of a margin-by-geography disclosure in any vintage read — so no
   inference is drawn from it in either direction.)*

### Customer power — the [E3-03](3) inversion, quantified

- **Two customers were 19% and 15% of FY2025 revenue** (Note 15) — **34% between them** —
  against 12% and 11% in FY2024 and 19% and 15% in FY2023. **In the nine months to
  2026-07-26 they are 20% and 14%.** Concentration is high, volatile and not falling.
- 89% of FY2025 revenue was shipped outside the United States; the top four destinations
  (China, Taiwan, Korea, Japan) are 81% of revenue.

### The claims NOT made, each refused with its reason

- **[E2-53] the dominance class — REFUSED.** *"Once dominant … Good or bad, it will prosper."*
  AMAT posted an **operating loss of $393.6M in FY2009** on gross margin of 28.5%, and
  operating margins of **4.7% in FY2012 and 5.8% in FY2013**. The marketplace, not the
  position, sets this company's level. Identical to the ACLS and KLAC findings.
- **[E3-33]/[E5-28] untapped pricing power — NOT CLAIMED.** Claiming it claims near-monopoly.
  *Recorded sweep: no instance found of a market-share figure for AMAT in its own FY2025,
  FY2024, FY2023, FY2020, FY2019 or FY2013 10-K, nor in Lam's FY2026 or FY2024 10-K, nor in
  the seven peer filings read for the KLAC row.* And a company whose primary competitor names
  it publicly as a peer in its two largest markets is not in the near-monopoly class.
- **[E4-36] which of the four causes of extreme success?** Honestly: **a nonlinear
  combination — breadth across process steps plus socket-level qualification lock — riding a
  very large wave.** The structure is ownable and predates the wave. The *current level* is
  the wave. Both are held: the class is judged on the structure, Q4 and Q5 on the normalized
  level.
- **[E4-32] direction.** **NARROWING on three measures and WIDENING on two.** Narrowing:
  ROUNTOA 50.8% → 34.8% and a 7.6% three-year incremental return; Semiconductor Systems
  backlog −44% in three years; six unpriced head-on competitors at the centre of the business.
  Widening: consolidated and segment gross margin up 8.1 and 2.8 points with ASPs filed as
  rising; and genuine China de-risking in dollars.

- Class: [ ] WIDE  **[x] NARROW**  [ ] NONE  [ ] PROVISIONAL · **Direction: MIXED, and on the
  capital measure NARROWING.**
- **VERDICT: [x] IN — NARROW, and narrower than KLAC's narrow.**

  *The strongest fact against this verdict, stated per **[E4-51]** so a bear would accept it
  as fairly put: **AMAT fails the [E2-44](1) pricing test in three of the four revenue
  declines in its filed record; the mix-free segment version of that test cannot be run at all
  because segment gross margin has only ever been filed for three consecutive revenue-growth
  years; its principal competitor names it by name in its two largest markets and out-earns it
  on both operating margin and return on tangible capital; six further named competitors in
  those same markets cannot be priced from any SEC filing; and the last three years of
  retained capital have earned 7.6% pre-tax.*** ***On that evidence a reasonable analyst could
  write NONE here.*** *It is held IN, NARROW on four filed facts: a socket-level qualification
  lock filed by two independent registrants; nineteen consecutive years of positive owner
  earnings including a −38.3% revenue year; a return on unleveraged net tangible operating
  assets that has not been below 14.8% since FY2010 and is 34.8% now **[E3-46]**; and gross
  margin up 8.1 points since FY2016 with the registrant twice naming rising average selling
  prices as a cause. **The class is capped at NARROW by five absences: no unit or
  installed-base series, no ASP series, no market-share figure, no segment gross margin before
  FY2023, and six unpriceable head-on competitors** — one absence more than the four that
  capped KLA, and the sixth of them sits at the centre of the business rather than at its
  edge.*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — THE WEIGHT CASE, DECLARED.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution [E3-38]** — NOT ticked, and it is closer than KLA's. [E3-38]'s root
  class **[E2-70]** is the undifferentiated product whose *"only products are promises"*.
  AMAT's product is a physical machine qualified into a customer's process of record and
  bought again for every copy of that fab; Q2 found a franchise, and by **[E3-43]** a
  franchise tolerates some mis-management. *Recorded against myself: AMAT's gross margin
  ranks sixth of eight in the competitor row, so the differentiation claim is weaker here
  than in the KLA file, and this box was the closest call in Step 1.*
- [ ] **Control [E1-16]** — NOT ticked. Liquid public minority stake; exit is a trade.
- [ ] **Leverage [E3-29]** — NOT ticked, and the numbers are given rather than asserted:
  **$6,500M of senior unsecured notes principal at FY2025 against $12,900M of cash and
  investments** — AMAT is **net cash by ~$6.4bn** — with **zero current maturities** after
  the 3.900% notes were repaid at maturity in FY2025.

**NONE TICKED → Q3 IS A QUALITATIVE OVERLAY.** Findings are recorded; manager quality alone
does not stop this run and cannot promote it.

### Honesty — binary, permanent, filings-based [E5-16], each matter dated to when it became PUBLIC

**THE EXPORT-CONTROLS MATTER IS THE LARGEST CONDUCT ITEM IN THIS FILE AND IT IS RECORDED IN
FULL, WITH ITS DATES, BECAUSE A RUN THAT BURIES IT HAS FAILED THE TEST.**

| date public | what the filing says |
|---|---|
| **FY2023 10-K, filed 2023-12-15** | *"In August 2022, we received a subpoena from the U.S. Attorney's Office for the District of Massachusetts requesting information relating to certain China customer shipments. In November 2023, we received a subpoena from the U.S. Commerce Department's Bureau of Industry and Security requesting the same information."* |
| **FY2024 10-K, filed 2024-12-13** | escalated to three agencies: *"since 2022, we have received **multiple subpoenas** … including from the **U.S. Department of Justice, the U.S. Commerce Department Bureau of Industry and Security, and the U.S. Securities and Exchange Commission**. … **We have continued to receive related subpoenas**"* |
| **FY2025 10-K, filed 2025-12-12** | same, **plus a second and separate matter**: *"We also have received subpoenas from the U.S. Department of Justice requesting information related to **certain federal award applications and information submitted to the federal government**."* And: *"we cannot predict the outcome, **nor reasonably estimate a range of loss or penalties, if any**, relating to these matters."* |
| **2026-02-11 · Q3 FY2026 10-Q, Note 13** | *"we entered into a settlement agreement with the U.S. Commerce Department Bureau of Industry and Security (BIS) to resolve its inquiry relating to certain China customer shipments and export controls compliance and **agreed to pay BIS an amount of $253 million**, which we paid in full during our second quarter of fiscal 2026. The settlement agreement … requires us to conduct **internal audits of our export controls compliance program** … The settlement agreement also includes a **denial order that is suspended and will be waived three years after the date of the order** … provided that we have timely completed the audit requirements."* |

**How it is weighed, stated so it can be attacked:**
- **[E5-16] refuses personal misconduct.** *Recorded sweep of the FY2023, FY2024 and FY2025
  10-Ks and the Q3 FY2026 10-Q: **no instance found** of a named individual charged, of an
  admission of wrongdoing, of a restatement, or of any officer departure connected to the
  matter.* This is a **corporate civil settlement with a regulator over compliance with a
  rule that moved repeatedly during the period in question** — the same regime whose
  boundary-moving Q2 recorded under **[E2-59]**. It is not carried as a personal-misconduct
  disqualifier.
- **[E5-22] governs the sizing, in both directions:** *penalty size is not seriousness* — the
  Wells Fargo error was reading $185M as small. **$253M is 3.2% of a year's operating cash
  flow and would not, by itself, matter. What matters is the suspended denial order**, which
  is the most severe instrument BIS holds: it would bar the company from exporting. It is
  suspended for three years against completed audits. **A company operating under a
  suspended denial order is a company whose licence to trade is conditional on its own
  compliance performance, and that is a real Q4 and Q6 item, not a Q3 footnote.** It is
  carried to both.
- **[E5-22]'s actual test — "the failure that counts is that *they didn't act when they
  learned*" — reads FOR the company on the disclosure record and raises ONE question against
  it on the reserve.** The disclosure escalated in every successive filing rather than being
  held flat, which is the candid direction. **But the FY2025 10-K, filed 2025-12-12, said the
  company could not "reasonably estimate a range of loss or penalties, *if any*" — and
  sixty-one days later it signed a $253 million settlement.** *"If any"* is doing a great
  deal of work two months before a nine-figure agreement. **No reserve appears in the FY2025
  balance sheet for it.** ASC 450 permits that if a loss was not both probable and estimable
  at the balance-sheet date, and I cannot show from the filings that it was. **Recorded as
  the sharpest open candor question in this file, stated as a question and not as a
  finding**, and it is why the flags below were read hard rather than assumed.
- **The DOJ and SEC matters, and the separate federal-award-applications matter, remain OPEN
  as of the Q3 FY2026 10-Q.** Their outcome is **UNRESEARCHED-with-no-document**: no filing
  in existence resolves them, so under the four-verdict test they are **UNKNOWABLE from the
  filing rung today**, carried as a live Q6 monitoring item rather than as a verdict.
- **Say-on-pay 91% for in 2025** (2026 proxy), *"supported by our shareholders each year
  since we began providing this vote in 2011."* No shareholder proposals on the 2026 ballot.

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30].** *Each is a prompt to READ, never a
verdict. The list is open, not closed.*

- [ ] **weak accounting** — not found. SBC is expensed and disclosed ($668M FY2025). KPMG
  audits. No material defined-benefit pension games. Goodwill impairment of **$41M** was
  taken in Q4 FY2025 on the exit of a Corporate-and-Other business, disclosed with the
  reason and the line it was charged to (general and administrative).
- [ ] **unintelligible footnotes** — not found. Note 9 prints every debt tranche with its
  effective rate; Note 15 now prints **segment cost of products sold, gross profit, gross
  margin, RD&E, SG&A, D&A and capital expenditures line by line** — more granular than any
  peer in the row. This is legible reporting and it is the reason several tests in this file
  could be run at all.
- [x] **TRUMPETED EARNINGS PROJECTIONS — FIRES, AND IT IS THE REAL ONE.** AMAT issues formal
  quarterly guidance on **total revenue and non-GAAP diluted EPS** (and, until Q4 FY2025,
  non-GAAP gross margin) in every earnings release. **[E5-30] is the governing reading — the
  behaviour is a ratchet:** *"once you start it, it's all over. You can't quit … And
  forecasting earnings, I can't imagine anything more destructive."* **[E3-48] requires the
  record be pulled and set against outturn, and it was, for seven consecutive quarters** (8-K
  exhibits 99.1, `0000006951-24-000037` through `0001628280-26-056699`):

  | quarter | revenue guide (mid) | revenue actual | Δ | non-GAAP EPS guide (mid) | actual | Δ |
  |---|---|---|---|---|---|---|
  | Q1 FY2025 | $7,150M ±400 | $7,170M | **+0.28%** | $2.29 ±0.18 | $2.38 | **+3.93%** |
  | Q2 FY2025 | $7,100M ±400 | $7,100M | **0.00%** | $2.30 ±0.18 | $2.39 | **+3.91%** |
  | Q3 FY2025 | $7,200M ±500 | $7,300M | **+1.39%** | $2.35 ±0.20 | $2.48 | **+5.53%** |
  | Q4 FY2025 | $6,700M ±500 | $6,800M | **+1.49%** | $2.11 ±0.20 | $2.17 | **+2.84%** |
  | Q1 FY2026 | $6,850M ±500 | $7,010M | **+2.34%** | $2.18 ±0.20 | $2.38 | **+9.17%** |
  | Q2 FY2026 | $7,650M ±500 | $7,910M | **+3.40%** | $2.64 ±0.20 | $2.86 | **+8.33%** |
  | Q3 FY2026 | $8,950M ±500 | $9,120M | **+1.90%** | $3.36 ±0.20 | $3.50 | **+4.17%** |
  | **mean** | | | **+1.54%** | | | **+5.41%** |

  **Seven for seven at or above the midpoint on both lines. Never below, on either, in two
  years.** On a ±$400–500M revenue band and a ±$0.18–0.20 EPS band that is **a midpoint set
  to be beaten** — the same signature the KLAC run found at sixteen-for-sixteen. **Two things
  are fairer to AMAT than to KLA and are stated:** the revenue beat is **+1.54%** against
  KLA's +2.68%, and **one quarter landed exactly on the midpoint** (Q2 FY2025, $7.10bn on a
  $7.10bn guide), which a purely managed number rarely does. The flag fires; the degree is
  milder.
- [ ] **serial share issuance [E5-15]** — **the reverse, and it is emphatic.** Cover-count
  shares outstanding: **1,330.8M (FY2008) → 1,204M (FY2013) → 1,060M (FY2017) → 967M (FY2018)
  → 916 → 914 → 892 → 844 → 833 → 818 → 793M (FY2025)** — **−40.4% over seventeen years and
  down in every year since FY2011.** $35.5bn of buybacks have retired more than a third of
  the company. **The buyback is real retirement, not a dilution offset.** *One qualification,
  recorded: the count has stopped falling. The Q3 FY2026 10-Q cover reads **793,597,443**
  against the FY2025 10-K's 792,943,366 — the count is flat-to-slightly-up over nine months
  despite continued repurchases, i.e. buybacks in FY2026 are running at roughly the rate of
  employee-plan issuance. That is a change of state and it belongs in Q6.*
- [ ] **EBITDA / adjusted-earnings promotion [E4-29]** — **DOES NOT FIRE.** *Recorded sweep of
  the FY2025, FY2023 and FY2019 10-Ks for the string "EBITDA": **zero occurrences in all
  three**.* And the non-GAAP habit has been **withdrawn, not added**: the same sweep counts
  **37 occurrences of "non-GAAP" in the FY2019 10-K, 0 in FY2023 and 4 in FY2025** — AMAT
  stopped printing a non-GAAP adjusted-results table in its annual report. *(It still uses
  non-GAAP in the earnings releases and the proxy, which is where the guidance flag above
  lives.)* **A registrant that removes a non-GAAP presentation from its 10-K is moving in the
  [E2-26] direction, and it is recorded as such.**
- [ ] **filed-figure tells [E4-30]** — **DOES NOT FIRE, AND THE SERIES IS UNUSUALLY NOISY
  RATHER THAN UNUSUALLY SMOOTH.** [E4-30] hunts *reported growth engineered to be unnaturally
  smooth* and *cash taxes falling as a share of reported pretax income*. Cash taxes paid ÷
  pre-tax income, nineteen years:

  | FY | 09 | 12 | 13 | 14 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | **25** |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | cash tax % of pretax | n/m | 76.9 | 56.0 | 13.5 | 7.8 | 5.2 | 6.4 | 16.0 | 13.0 | 12.6 | 24.6 | 13.0 | 11.7 | **16.2** |

  The ratio is **rising, not falling, over the last decade** (5.2% in FY2017 to 16.2% in
  FY2025), which is the opposite of the fraud signature. **And the smoothness test fails in
  the safe direction spectacularly: an operating loss in FY2009, operating margins of 4.7%
  and 5.8% in FY2012–13, and 29.2% in FY2025.** Nothing about this reported series is smooth.
- [x] **METRIC-SWITCHING [E2-49] — FIRES, ON A SPECIFIC AND DATABLE INSTANCE.** *"Yardsticks
  seldom are discarded while yielding favorable readings."* **AMAT has changed its segment
  presentation in three consecutive years, recasting prior periods each time:**
  1. **Q1 FY2024** — share-based compensation began to be included in segment performance
     (Q4 FY2024 release). Neutral; arguably an improvement.
  2. **FY2025** — **Display dropped as a reportable segment** and folded into Corporate and
     Other. *Stated fairly: this one does NOT look like hiding deterioration. Display's
     revenue rose $885M → $1.06bn and its operating income rose $51M → $235M in the year it
     was de-segmented* (Q4 FY2025 release) — a business was hidden while it was improving,
     not while it was failing.
  3. **Q1 FY2026 — the 200mm equipment business was moved OUT of AGS and into Semiconductor
     Systems, and corporate support costs are now fully allocated to the segments.** **This
     one fires.** The FY2025 10-K had said, in the sentence explaining AGS's margin decline:
     *"AGS' operating margin for fiscal 2025 **decreased** … primarily due to **a decrease in
     200mm equipment net revenue**."* **The very next quarter, the line blamed for the
     annuity segment's margin decline was removed from that segment.** AMAT's stated reason —
     *"to increase our operational efficiency and consolidate the reporting of our 200mm
     equipment with the reporting of our other capital equipment"* — is coherent and may well
     be the whole of it. **[E2-49] does not require venality; it requires the reader to notice
     that the yardstick changed right after it gave an unfavourable reading, and to say so.**
     Recorded, with a Q6 bull-breaker attached.
  **The cumulative effect is the real cost: the AGS series cannot be compared on a consistent
  basis for more than two years, and neither can the segment gross-margin series Q2 was
  decided on.**
- [x] **AN UNNAMED $1.3bn PUBLIC EQUITY POSITION — a new flag, recorded because it moves
  reported earnings.** AMAT's *"publicly traded equity securities"* went **cost $543M / fair
  value $723M (FY2024) → cost $1,288M / fair value $2,110M (FY2025) → cost $965M / fair value
  $1,979M (Q3 FY2026)**, carrying an unrealized gain of **$824M and then $1,015M** that runs
  through *interest and other income, net* and therefore through **GAAP net income**. Nine
  months of FY2026 show **+$1,237M** on that line against +$625M a year earlier. *Recorded
  sweep of the FY2025 10-K and the Q3 FY2026 10-Q: **no instance found** of the issuer being
  named, of the size of the stake, or of the strategic rationale.* **A billion dollars of
  reported pre-tax income from an equity position whose identity is not in the filing is an
  [E2-26] miss** — this is exactly a business fact a half-owner would want. *Two mitigations,
  stated: it is disclosed in aggregate with cost and fair value at each date, and **AMAT's own
  non-GAAP EPS EXCLUDES it** — in Q2 FY2026 GAAP EPS was $3.51 against non-GAAP $2.86, i.e.
  the non-GAAP number is the more conservative one, which is the reverse of the usual
  direction and is a candor point. **And it does not touch owner earnings at all**, because
  unrealized gains are reversed out of operating cash flow.*

**[E4-52] — do the flags CONVERGE into a lollapalooza?** *"extreme consequences from
**confluences** of psychological tendencies acting in favor of a particular outcome."*
**Three flags point at one outcome and that is worth stating as a system rather than a list:
the guidance ratchet (a beat every quarter for seven quarters), the segment recast that
followed the unfavourable AGS reading, and the buyback run backwards on price below — all
point at *managing the reported quarter and the share price*.** Against them, and it is
substantial: **zero EBITDA in three vintages, a non-GAAP presentation withdrawn from the
10-K, cash taxes rising as a share of pretax, a share count down 40% in seventeen years, a
company-selected pay metric that is a capital-charge measure and that shows deterioration
(below), and the most granular segment disclosure in the peer row.** **My reading: three
prompts pointing one way, and a stronger set of counter-evidence pointing the other. Not a
lollapalooza. Recorded as a close call rather than a clean pass.**

**STEP 3 — THE PRIMARY TEST [E2-01], on the right denominator.**

AMAT's ROE is not excluded here the way KLA's was — book equity is $20,415M on $37,772M of
assets, an ordinary structure — but the **[E2-43]** denominator is still the comparable one
across the row, so it is what is reported:

| FY | 2013 | 2015 | 2016 | 2017 | 2018 | 2019 | 2021 | 2022 | 2023 | 2024 | **2025** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **op income ÷ unleveraged NTOA** | 14.8% | 18.7% | 29.6% | 33.6% | 42.0% | 28.8% | 45.3% | **50.8%** | 39.6% | 34.7% | **34.8%** |

**[E3-46]'s "second question about the business is a number" is answered well in level and
badly in direction: 34.8% pre-tax on tangible operating capital, never below 14.8% since
FY2010 — and down from 50.8% three years ago while revenue rose 10%.** The incremental
arithmetic is at Q2 and is the same finding: **7.6% on the last three years of retained
tangible capital, against ~40% over a decade.**

**AND AMAT'S OWN COMPANY-SELECTED PAY METRIC SAYS THE SAME THING, WHICH IS THE STRONGEST
CANDOR FINDING IN THIS FILE.** The 2026 proxy's Pay-Versus-Performance table names
**"Non-GAAP Economic Profit"** as the company-selected measure — a capital-charged metric,
not EPS:

| fiscal year | 2021 | 2022 | 2023 | 2024 | **2025** |
|---|---|---|---|---|---|
| GAAP net income ($M) | 5,888 | 6,525 | 6,856 | 7,177 | **6,998** |
| **Non-GAAP Economic Profit ($M)** | 4,249 | **4,866** | 4,277 | 4,263 | **4,243** |
| TSR (initial $100) | 226.06 | 149.67 | 221.11 | 316.48 | **392.09** |
| peer-group TSR | 148.13 | 105.92 | 142.27 | 232.14 | 313.53 |

**AMAT's own economic-profit measure is LOWER in FY2025 than in FY2022 — down 12.8% — while
GAAP net income rose 7.2% and the shares rose 162%.** A management choosing a metric that
prints its own five-year flatline, and printing it in the proxy, is doing the [E2-26] thing.
**It is also independent corroboration, from the company's own capital-charged number, of the
Q2 finding that incremental capital has stopped earning.**

**PAY VERSUS PERFORMANCE, read as [E3-59] asks.** CEO Gary Dickerson: Summary Compensation
Table total **$29.6M** in FY2025 with **compensation actually paid of $86.97M**; the average
non-PEO NEO $7.59M / $16.25M. **The plan does bite in both directions — in FY2022, when TSR
fell from 226.06 to 149.67, compensation actually paid to the PEO was NEGATIVE $(22.1)M.**
That is a real at-risk structure, not a ratchet. **And the ownership limb of [E3-59] reads
much better than KLA's: Dickerson holds 1,398,872 shares — 0.176% of the company, roughly
$636M at the run price — and all 15 directors and executive officers hold 2,405,861 shares,
0.303%.** *(KLA's sixteen insiders held 0.0915% and its CEO 0.026%.)* **This CEO's own
capital is genuinely in the stock.**

**The half-owner test [E2-26].** **Passes, and by the widest margin of any name in this
equipment cohort — which is why the Q2 evidence base was so much richer than KLA's:**
1. **Segment cost of products sold, gross profit and gross margin are filed** (Note 15). KLA
   files none of these. Every mix-free reading in this file exists because AMAT chose to file
   it.
2. **Backlog is filed by segment, every vintage**, including the disclosure that export rules
   would cut it by ~$549M.
3. **Revenue by customer location is filed every vintage**, which is what made the China
   decomposition possible.
4. **The FY2019 gross-margin fall is attributed in plain words to "the decrease in net
   sales"** rather than to an adjusted item. That is a management writing down the fact that
   damages it.
**Against those, three [E2-26] failures, all recorded above:** the unnamed billion-dollar
equity position; the *"if any"* language sixty-one days before a $253M settlement; and
**AMAT names no competitor anywhere in its 10-K** (*recorded sweep of six vintages: the only
occurrences of "KLA" are in executive biographies*) while Lam, Nova, ASML and Axcelis all
name AMAT in theirs.

**The institutional imperative — all four scored [E2-30].** *Not a fraud test.*
- [ ] **resists change in current direction** — not found. Display de-segmented and partly
  exited, 200mm reorganised, corporate costs reallocated, all within three years.
- [ ] **projects/acquisitions to soak up funds — NOT FOUND, and this is a genuine strength.**
  **Cash paid for acquisitions: $25M (FY2023), $0 (FY2024), $29M (FY2025)** — against $35.5bn
  of buybacks and $12.9bn of dividends over the same era. **The absolute-size acquisition
  gate is nowhere near approached; nothing in three years exceeds $29M.** The one large
  capital commitment is internal: the **EPIC Center**, which is the FY2025 capex spike
  ($2,260M, of which $1,696M sits in Corporate and Other) and is the subject of the Q4
  maintenance-capex judgment below.
- [ ] **staff studies justifying the leader's craving** — no instance found.
- [x] **peer behaviour mindlessly imitated — FIRES, softly.** Quarterly non-GAAP EPS guidance
  is the sector norm and AMAT follows it. Not venal; the imperative operating exactly as
  [E2-30] describes.

**[E4-39] — the acquisition post-mortem, the rare positive tell. NOT APPLICABLE and therefore
NOT HELD AGAINST.** *Recorded sweep of six vintages: no acquisition large enough to require a
post-mortem has been made in the period read.* The one candidate is the **abandoned Tokyo
Electron merger (terminated 2015 on DOJ objection)** — which pre-dates every window used here
and, having been abandoned, produced no capital loss to review. **The absence of the
Orbotech-shaped problem is itself a difference from KLA and it is a favourable one.**

**CAPITAL ALLOCATION — THE TWO BUYBACK CONDITIONS [E5-08], AND CONDITION 2 FAILS — BUT BY
LESS THAN KLA'S.**

- **(1) Ample funds for operations and liquidity? YES.** $12,900M of cash and investments at
  FY2025 ($14,501M at Q3 FY2026) against $6,500M of debt; $7,958M of operating cash flow; no
  current maturity.
- **(2) Repurchases at a MATERIAL DISCOUNT to conservatively calculated intrinsic value? NO.**
  The record, buyback dollars against the implied average price paid (repurchase cash ÷ shares
  repurchased, both filed):

  | FY | 2013 | 2015 | 2016 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | **2025** |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | buyback $M | **245** | 1,325 | 1,892 | **5,283** | 2,403 | **649** | 3,750 | **6,103** | 2,189 | 3,823 | **4,895** |
  | implied avg price | **~$13.61** | ~$17.43 | ~$19.71 | ~$51.79 | ~$40.05 | **~$54.08** | ~$133.93 | ~$113.02 | ~$121.61 | **~$191.15** | ~$163.17 |

  **The pattern is the KLAC pattern and it runs the same way round: the smallest repurchases
  in the record came at the lowest prices and the largest at the highest.** $245M at ~$13.61
  and **zero in FY2014**; $649M at ~$54.08 in the year after the COVID trough; then $6,103M at
  ~$113, $3,823M at ~$191 and $4,895M at ~$163. **And the sharpest single instance: in FY2019
  the average price paid fell 23% from FY2018 and the spend fell 55%** — the company bought
  less as the stock got cheaper. **[E5-24]'s first law — *"what is smart at one price is dumb
  at another"* — is being run in reverse.**
  **→ CAPITAL ALLOCATION FLAG, RAISED**, with the humility clause **[E4-13]**: this rests on
  *our* IV range, and *"it is natural for CEOs to be optimistic about their own businesses.
  They also know a whole lot more about them than I do."* **[E5-08]** adds that *"infractions,
  even serious ones, are innocent."* **The flag BINDS POSITION SIZE, never the discount rate.**
- **The degree matters and it is stated, because it is one of the two facts that make AMAT
  different from KLA on price.** Against this run's own Q5 zero-growth band (~$67 to ~$153 per
  share at the sovereign, judged ~$100), **FY2024's ~$191 is about 1.25x the TOP of that band
  and FY2025's ~$163 is about 1.07x it.** **KLA's FY2026 repurchases were at 2.7x to 5.8x the
  top of its band.** Both fail condition 2; AMAT fails it by a fifth, KLA by a multiple.
- **[E2-52]/[E2-60] — are the distributions funded by capital replacement? NO.** Dividends
  plus buybacks were **78.9% of operating cash flow in FY2025** (57.8% FY2024, 36.4% FY2023),
  funded from cash, with **net share issuance negative in every year since FY2011** and **debt
  flat-to-down** ($6.5bn, and the FY2025 maturity was repaid rather than refinanced).
  **[E2-60]'s "financial strength" limb holds: the payout has not been financed by leverage.**
  *(Recorded honestly: in FY2013, FY2015, FY2018 and FY2022 distributions EXCEEDED operating
  cash flow — 112.5%, 155.8%, 155.5% and 129.2% — funded from the cash pile. That is spending
  the balance sheet, not replacing capital, and in each case the balance sheet absorbed it.)*
- **[E2-51] — the refusal tell** does not apply: they buy, aggressively. The demerit is the
  price, not the abstention.

**THE GUARDRAIL — checked before the verdict is written.**
- [x] Confirmed: **nothing in this Q3 is used to promote the name.** The 34.8% return on
  tangible capital is a fact about the *business* recorded at Q2's request [E3-46], not a
  compliment to the manager — *"a good managerial record … is far more a function of what
  business boat you get into than it is of how effectively you row"* **[E2-37]**.
- [x] This business does **not require** a superstar; no key-person dependence recorded at Q2
  **[E4-23]**. *(Noted: Dickerson has been CEO since 2013 and is 68. Succession is a Q6
  watch item, not a moat defect, because the [E4-23] test is whether the moat goes when he
  goes, and Q2 located the moat in qualification lock and materials know-how, not in him.)*
- [x] No great manager is the reason to act. No excisable-cancer case **[E2-35, E2-36]**.
- **[E3-40] loss of focus?** **Not found, and the evidence is unusually clean.** The vector
  [E3-40] warns of — *"neglects its wonderful base business while purchasing other businesses
  that are so-so or worse"* — requires acquisitions, and **AMAT has made $54M of them in three
  years.** RD&E has risen $2,054M (FY2019) → $3,570M (FY2025), +73.8%, and is 12.6% of revenue
  against 10.8% at the FY2021 peak. **The capital has gone into the base business and into
  shareholders' hands, not into empire.** *The one item to watch is the EPIC Center — $1,696M
  of FY2025 capex in Corporate and Other, i.e. unallocated — which is a large internal bet
  whose return is not separately reportable. Recorded as a Q6 item.*

- **VERDICT: [x] IN — as an OVERLAY, with two flags live and one open candor question.**
  *IN is **the absence of found disqualifiers, not a finding that these managers are
  honest** — [E5-17]: "People are not that easy to read. Sincerity and empathy can easily be
  faked," and [E5-32]: audited does not mean true. **IN never promotes**, and nothing here is
  used to repair Q2 or substitute for Q4.*
  **The two live flags, carried forward: (1) a quarterly guidance culture with a
  seven-for-seven record of meeting or beating its own midpoint on both lines [E3-48, E5-30],
  and a segment recast in FY2026 that followed the unfavourable AGS reading it affected
  [E2-49]; (2) a buyback programme run backwards on price [E5-08](2), which BINDS POSITION
  SIZE and nothing else [E4-13].** **The open question, dated and stated as a question: the
  FY2025 10-K's "nor reasonably estimate a range of loss or penalties, if any" on
  2025-12-12, sixty-one days before a $253M BIS settlement on 2026-02-11, with a suspended
  denial order attached.** Against all of that: **no EBITDA in three vintages and a non-GAAP
  table withdrawn from the 10-K; cash taxes rising as a share of pretax; a share count down
  40% in seventeen years; $54M of acquisitions in three years against $8.7bn returned; a
  CEO holding $636M of stock; and a company-selected pay metric that prints its own five-year
  flatline.**

## Q4 — WILL IT SURVIVE?

### ⚠ CORRECTION TO Q2, PUBLISHED HERE RATHER THAN BY EDITING Q2 (operator rule 6, and rule 9)

**Q2 reported that AMAT's incremental pre-tax return on unleveraged net tangible operating
assets was 7.6% over FY2022–25, below [E5-40]'s "quite satisfactory" ~12%, and called it the
franchise deteriorating. That number is arithmetically correct on the row's stated
denominator and it is MISLEADING, and the error was mine.** The row's ROUNTOA convention
(assets − goodwill − intangibles − non-interest-bearing current liabilities) leaves **cash and
investments inside the denominator**, and AMAT's cash-and-investment book grew **$4,561M
(FY2022) → $12,900M (FY2025)**. Almost the whole $9,059M "additional tangible operating
capital" was **money the business did not deploy**. Recomputed on operating capital only:

| ex-cash net tangible operating assets | AMAT | LRCX | KLAC |
|---|---|---|---|
| FY2021 | 85.9% | 70.9% | 70.4% |
| FY2022 | 72.4% | 71.8% | 79.0% |
| FY2023 | 75.2% | 69.8% | 77.0% |
| FY2024 | 75.6% | 58.7% | 53.0% |
| FY2025 | **73.9%** | 80.2% | 65.4% |
| FY2026 | *(FY ends 10/2026)* | **81.1%** | **56.9%** |
| **incremental, FY2022 → latest** | **+$686M on +$720M = 95.3%** | +$2,818M on +$2,622M = **107.5%** | +$2,007M on +$5,326M = **37.7%** |

**Three things change and all three are recorded rather than quietly absorbed:**
1. **The "7.6% incremental return" finding is withdrawn. The correct figure is 95.3%**, and
   AMAT's return on *operating* capital has been flat at 72–86% for five years, not falling.
2. **Q2's "direction NARROWING on the capital measure" is WITHDRAWN.** The capital measure is
   flat. The other two narrowing findings — the −44% Semiconductor Systems backlog and the six
   unpriceable head-on competitors — are unaffected and stand.
3. **The competitor row's most damaging cell softens but does not reverse.** On the row's
   cash-inclusive convention Lam beats AMAT 52.0% to 34.8%. **On operating capital it is 81.1%
   to 73.9% — Lam still ahead, by seven points rather than seventeen.** *And the correction
   cuts AGAINST KLA, which this queue rated the best business it has run: KLA's ex-cash return
   is **56.9%**, the lowest of the three, and its incremental return over the same window is
   **37.7%** against AMAT's 95.3%.* The row was comparing three companies holding very
   different cash piles on a denominator that contains cash.
**The Q2 verdict is UNCHANGED — IN, NARROW.** The correction makes the business look better,
and a correction that improves the subject cannot promote a class that was capped by a failed
pricing test and five named absences. **It is published because operator rule 9 requires the
disconfirming hunt to be run against my own conclusion in both directions, and this one ran
against the bear case I had built.**

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment also
> should be included in (c)**.)" … "**(c) must be a guess**."

**THE FILING CROSS-CHECK, operator rule 4.** FY2025 10-K, Consolidated Statements of Cash
Flows: *Cash provided by operating activities* **$7,958M**; *Capital expenditures* **$(2,260)M**;
*Cash paid for acquisitions, net of cash acquired* **$(29)M**. All agree with the tagged series
to the dollar. Note 15's segment table reconciles to the filed $28,368M / $8,289M exactly.

**MORE THAN ONE WINDOW — THE SPREAD IS THE RANGE [E4-25], EVERY WINDOW PUBLISHED [E4-38].**
The full table is at Stage 0 and is not repeated. In summary, $M, capex end:

| 3-yr | 5-yr | 5-yr LTO | 8-yr | 10-yr | 10-yr LTO | 15-yr | 19-yr |
|---|---|---|---|---|---|---|---|
| 6,348.0 | 5,534.2 | 4,552.3 | 4,524.5 | 4,125.2 | 3,404.8 | 3,149.1 | 2,768.4 |

- **Combined range (window spread × capex band): $2,768.4M to $7,708.0M — a 2.78x width,
  178.4%.** The screen said 34.6%.
- **Is the range too wide to reach a conclusion [E4-25]? NO, and for the same reason as
  KLA's:** the width is enormous and **every point in it lies on the same side of the Q5
  answer.** The most generous construction available — the best year AMAT ever filed, at the
  (c) = D&A ceiling — yields **2.14%** against a 5.24% sovereign. A range that is wide but
  wholly one-sided is a conclusion, not a failure to reach one.
- **The distorted years, named in both directions [E5-11, E4-41]:**
  - **UP — FY2021–26, the AI/leading-edge wave.** The [E4-41] step from the FY2014–18 mean is
    **2.74x** (Stage 0), not the screen's 2.0x. Backlog is the counter-evidence and it points
    *down*: total backlog $19,011M (FY2022) → **$15,002M (FY2025)**, with Semiconductor
    Systems' own book down 44%.
  - **UP — FY2024, China.** China was **37.2% of revenue** that year on legacy-node pre-buying
    ahead of export controls, and **ex-China revenue FELL 11.5%** (Q2). The one apparently
    clean growth year in the segment-margin window is not clean.
  - **DOWN and KEPT IN per [E5-33]:** the **$181M FY2025 restructuring charge** (a Q4 FY2025
    workforce reduction of ~4% of global headcount), the **$41M goodwill impairment**, and the
    **$253M BIS settlement paid in Q2 FY2026** are real costs borne by shareholders and are
    **not added back anywhere in this file.**
- **[E3-55] scope check — is the width distortion, or certain-endgame volatility?** **It is
  distortion.** See's loses money eight months a year around a known level; AMAT's *level*
  moved 2.74x, its owner earnings ran $185.5M to $7,104M inside one filed record, and its
  order book is falling while its revenue rises. The width is uncertainty about the level,
  which is what [E4-25] says belongs in the open.

**MAINTENANCE CAPEX — (c) AS A DISCLOSED JUDGMENT, AND THE D&A END IS INVALID FOR THIS FILER
UNDER [E5-20] — THE SAME RULING AS KLA'S, FOR THE OPPOSITE REASON.**

The corpus default is D&A **[E3-44, E2-41]**. **It does not apply here, and the reason is
arithmetic:**

| | FY2019 | FY2021 | FY2023 | FY2024 | **FY2025** |
|---|---|---|---|---|---|
| tangible D&A $M | 306 | 345 | 471 | 392 | **435** |
| capital expenditures $M | 441 | 668 | 1,106 | 1,190 | **2,260** |
| **capex ÷ tangible D&A** | 1.4x | 1.9x | 2.3x | 3.0x | **5.2x** |
| net PP&E $M | 1,529 | 1,934 | 2,723 | 3,339 | **4,610** |

**Capex has exceeded tangible depreciation in every one of the last twelve fiscal years, by
1.2x to 5.2x, while net PP&E rose from $937M (FY2016) to $4,610M — 4.9x — against a
depreciation charge that rose 2.2x.** [E5-20]'s test is whether *"merely spending their
depreciation expense will not keep them in the same place"*, and on twelve consecutive years
of filed evidence it will not. **So the D&A end of the band is INVALID for this filer and (c)
is judged at total capital expenditure.** The D&A end is displayed, as [E2-23] requires the
guess to be displayed, and is not used.

- **[E3-44] direction question, answered: AMAT is MIDDLEWEIGHT and getting heavier.** Capex is
  **8.0% of revenue** in FY2025 (against 1.5–4.3% for most of the record) and net PP&E is
  16.3% of revenue. It is not the railroad class, but it is no longer KLA's 2.8%-of-revenue
  class either. **The capex band therefore does real work in this file, unlike KLA's, where
  the two ends differed by under 2%:** here they differ by **$2,674M in FY2025 alone**
  ($5,030M vs $7,290M). Judging (c) is a load-bearing choice and it has been made in the
  conservative direction.
- **The one honest argument the other way, stated and then declined.** Note 15 discloses capex
  by segment, and **most of the spike is NOT in the operating segments: FY2025 capex was
  Semiconductor Systems $507M, AGS $57M, Corporate and Other $1,696M** (9M FY2026: $367M /
  $58M / $1,563M). The unallocated portion is the **EPIC Center**, a new collaborative R&D
  facility — *"EPIC Center R&D partnerships expand to 11 engagements"* (Q3 FY2026 release) —
  which is a growth investment, not maintenance of unit volume. On operating-segment capex
  alone, (c) would be ~$564M against $435M of D&A, and owner earnings would be roughly
  **$1.7bn higher in FY2025**. **That construction is REFUSED**, for two reasons: (a) the
  corporate capex is real cash that left the company and the filing does not label any of it
  discretionary; and (b) taking it would be conservatism spent backwards, which is precisely
  the *"narrowing assumptions until the answer appears"* that **[E4-18]** forbids. It is
  recorded so a later reader can see it was considered and priced at zero.
- **[E2-23] constraint 3, the working-capital increment — INCLUDED BY CONSTRUCTION and it
  bites hard, harder than in any equipment name run so far.** Inventory rose **$2,050M
  (FY2016) → $5,915M (FY2025)** and receivables **$2,279M → $5,185M**, every dollar of which
  flows through operating cash flow as a use of cash. **And the current year is the sharpest
  instance in the filed record**: in the nine months to 2026-07-26, **accounts receivable rose
  $2,508M** (against $538M a year earlier), taking the balance to **$7,691M**, and:

  | nine months ended | 2026-07-26 | 2025-07-27 | change |
  |---|---|---|---|
  | revenue | **$24,037M** | $21,568M | **+11.4%** |
  | operating income | **$7,429M** | $6,577M | **+13.0%** |
  | cash provided by operating activities | **$5,568M** | $5,130M | +8.5% |
  | capital expenditures | **$(1,988)M** | $(1,475)M | +34.8% |
  | **operating cash flow less capex** | **$3,580M** | **$3,655M** | **−2.1%** |

  **Reported profit up 13.0%; cash after capital spending down 2.1%.** That is the whole
  reason this framework computes from cash rather than earnings, and it is stated as a filed
  fact for three quarters, not projected forward. *(Fairly noted: Q3 revenue was up 25% year
  on year, so some receivable build is arithmetic rather than deterioration; and AMAT sells
  receivables — **$501M in FY2025, $444M in FY2024** — which is disclosed and roughly
  constant, so it flatters the level but not the trend.)*
- **Stock compensation subtracted in full [E5-06]: $668M in FY2025**, and in every year of the
  nineteen-year series. Noted per **[E3-70]**: the reported charge is the *floor* of the
  correct subtraction, not the measure; no market-value adjustment is attempted, and any
  understatement makes owner earnings **lower**, not higher.
- **ASC 842 — checked, and the answer to the brief's INTC question [E4-52] is YES, AMAT DOES
  report PP&E additions outside the investing capex line, and it is immaterial.**
  `RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability` is tagged at **$109M in FY2023
  and nil in FY2021, FY2022, FY2024 and FY2025** — one year only, 9.9% of that year's capex
  and 0.4% of the five-year owner-earnings mean. **It is included in (c) anyway** (it is the
  difference between my 5-year capex-end mean of $5,534.2M and the screen's $5,512M, which is
  how the screen row reproduced to the dollar). Operating-lease ROU assets are $375M and are
  already inside operating cash flow; they are not double-counted.
- **Software capex — checked.** *Recorded sweep of the FY2025 cash-flow statement: **no
  instance found** of a capitalized-software or software-development caption.* The single line
  is *"Capital expenditures."* **The HAS defect does not bite here.**

### Great, good, or gruesome? **[E4-20]**

- **[x] GREAT on the long record; the last three years read as GOOD, and both are stated.**
- **The great evidence:**
  - **73.9% pre-tax return on ex-cash net tangible operating assets** (FY2025), a series that
    has not been below **53.2%** since FY2015 and that beats KLA's 56.9% and trails Lam's
    81.1%.
  - **Growth has consumed little net capital.** Over **FY2019–25 AMAT earned $33,289M of
    owner earnings and returned $30,632M of it — 92.0%** ($23,812M of buybacks, $6,820M of
    dividends) — while operating income went **$3,350M → $8,470M, 2.5x**. **A business that
    2.5x's its profit while distributing 92% of what it earns is [E4-20]'s great account.**
- **The good-not-great evidence, and it is recent:** owner earnings peaked at **$7,104M in
  FY2023** and have fallen to **$6,910M and then $5,030M**, while capex rose from $1,106M to
  $2,260M and the nine-month FY2026 cash-after-capex figure is *below* the prior year.
  **[E4-43] governs: the good class passes.** *"nothing shabby about earning $82 million
  pre-tax on $400 million of net tangible assets"* — the good class ranks below great at Q5
  and that is all it does. **Either reading clears Q4.**
- *The one qualification, stated as it was for KLA: [E4-20]'s "rise as the years pass" limb
  belongs to the cycle, not to the position. The rate has risen — and it fell in FY2009,
  FY2012, FY2013, FY2015, FY2019, FY2024 and FY2025.*

### Staying power — all three scored **[E5-11]**

- **(1) A large and reliable stream of earnings — YES, with the honest caveat.** **Owner
  earnings have been positive in all nineteen years read, including FY2009 (+$185.5M) when the
  company posted an operating LOSS of $393.6M** and FY2013 (+$264.0M) at a 5.8% operating
  margin. **Reliable in sign; violently variable in size — a 38x range.** **[E5-29] governs:
  volatility is not risk**; the question is coverage, and coverage is not in question.
- **(2) Massive liquid assets — YES, and it is the strongest of the three balance sheets in
  this cohort.** At 2026-07-26: **cash and cash equivalents $7,037M + short-term investments
  $2,196M + long-term investments $5,268M = $14,501M**, against **short-term debt $1,299M and
  long-term debt $5,245M = $6,544M**. **Net cash of roughly $7,957M**, or **$10.03 per share**.
  *(Recorded: $1,979M of that book is publicly traded equity securities carried at fair value
  with a $1,015M unrealized gain — a real asset, but a marked one, and its identity is not in
  the filing. See Q3.)*
- **(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — PASSES, and less cleanly than KLA's.**
  Note 9: **$6,500M of principal at FY2025, 100% fixed-rate senior unsecured notes**, maturity
  ladder **2027 $1,200M · 2029 $700M · 2030 $750M · 2031 $550M · 2035 $500M · 2036 $450M ·
  2041 $600M · 2047 $1,000M · 2050 $750M.** The earliest maturity is **$1,200M in 2027**,
  roughly thirteen months from the run date — **shorter than KLA's two and a half years** —
  and it is covered **11x by cash and investments**. The only redemption trigger is a
  change-of-control-plus-downgrade put at 101%. **[E3-52] applies in AMAT's favour:
  $3,271M of customer contract liabilities** are covenant-free, due-date-free,
  customer-prepaid money — the benefit of debt without its drawbacks.
- **[E5-39] — "never dependent on the kindness of strangers" — MET ON SUBSTANCE, NOT ON THE
  LETTER, and the difference from KLA is recorded.** Unlike KLA, **AMAT does run commercial
  paper** ($399M issued and $400M repaid in the nine months to 2026-07-26 — revolving, small)
  and **maintains $4.1bn of revolving credit facilities**: a $2.0bn five-year agreement
  expiring February 2030, a **$2.0bn 364-day agreement expiring September 2026**, and ~$53M of
  Japanese bank lines. **Nothing was drawn at FY2025.** Against $14,501M of cash and
  investments these instruments are conveniences, not dependencies — but *"no bank lines
  counted, no commercial paper, nothing depended on"* is the corpus's phrasing, and AMAT
  would fail it read literally. **Scored as a pass on substance with the literal failure
  stated.**
- **Leverage, named and quantified [E4-16, E3-29]** — *there is no ratio ceiling in this
  framework*: **$6,544M of principal; interest expense $206M for nine months of FY2026
  (~$275M annualized); [E2-54] coverage — interest, paid and accrued, out of current cash flow
  NET of ample capital expenditure — is 18.3x on the FY2025 figure, 20.1x on the 5-year mean
  and 10.1x on the 19-year mean including FY2009 and FY2013.** It clears on every window,
  which is what [E2-54] asks. **AMAT is net cash; the debt is a financing convenience.**
- **[E2-55] — score the worst case, not the expected one.** At the FY2009 analogue (revenue
  −38.3% to **$17,503M**, gross margin 28.5%), gross profit is ~$4,988M against a fixed RD&E
  plus SG&A base of **$5,338M** → **an operating loss of roughly $350M**, which is exactly what
  FY2009 produced. At a 40% gross margin — the structural level of the last decade rather than
  FY2009's — the same revenue gives **+$1,663M** of operating income. **In either case
  interest of $275M is trivially covered from a $14.5bn liquid book, the only maturity inside
  three years is $1,200M, and FY2009 itself demonstrated that owner earnings stay POSITIVE
  through the loss because working capital unwinds.** **Certain, not merely likely.**
- **[E3-66] jurisdiction** — US filer, Delaware; shareholders stand first in the queue.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40]**

**Model exposure, not experience [E4-40].** The benign recent record is *"not only useless, but
actually dangerous"* as a guide. **Four mechanisms, quantified from filed figures. The honest
finding is that three impair the level — a Q5 fact — and the fourth is the only genuine
extinction mechanism in this file, and it is not a market risk.**

1. **THE CAPACITY GLUT — the [E2-27] mechanism proper, and the likeliest.** Every fab builds
   for AI at once; *"viewed individually, each company's capital investment decision appeared
   cost-effective and rational; viewed collectively, the decisions neutralized each other."*
   **Quantified above:** a FY2009-magnitude −38.3% year takes revenue to $17,503M and produces
   an operating loss at FY2009 margins, +$1.7bn at modern ones; owner earnings land somewhere
   between the FY2013 analogue ($264M) and the FY2019 level ($2,543M) — **inside the 15- and
   19-year window means already published.** **The leading indicator is already filed and
   already negative: Semiconductor Systems backlog −44% in three years.** **Likelihood: [x] a
   real possibility** on a five-to-ten-year view. **Fatal: no.**
2. **THE SUSPENDED DENIAL ORDER — and this is the mechanism KLA's file does not contain.**
   The BIS settlement of 2026-02-11 carries *"a **denial order that is suspended** and will be
   waived three years after the date of the order … **provided that we have timely completed
   the audit requirements**."* **A denial order bars a company from participating in US
   exports.** For a company shipping **89% of its revenue outside the United States**, its
   activation would not impair the level — it would stop the business. **Quantified: $25,305M
   of FY2025 revenue was shipped outside the US.** **Likelihood: [x] a low-level
   possibility** — activation requires AMAT to fail audits that are within its own control and
   that it has every incentive to pass, and the order is suspended rather than imposed. **But
   it is the only mechanism in this file with a filed instrument attached that could end the
   company rather than dent it, and no amount of balance sheet answers it.** It is the reason
   Q6's monitoring set leads with the export-controls file rather than with margin.
3. **CHINA EROSION — the [E4-40] exposure question.** China is **$8,529M, 30.1% of FY2025
   revenue.** A total loss removes ~$4.6bn of gross profit at the Semiconductor Systems 54.2%
   margin against $8,470M of operating income — **a 55% cut**, taking owner earnings to roughly
   **$2.0–2.5bn**. AMAT's own Item 1 names the mechanism: *"We could see increased competition
   from domestic equipment manufacturers in China resulting from local government incentives
   and funding **as well as export controls established by the United States government** …
   Export controls … **may also provide an advantage to our international competitors.**"*
   **Likelihood of total loss: a low-level possibility. Likelihood of continued material
   erosion: [x] a real possibility** — the FY2025 decomposition shows China dollars already
   down 15.7%.
4. **COMPETITIVE DISPLACEMENT IN ETCH AND DEPOSITION.** Lam names AMAT as its primary
   competitor in both, and out-earns it on operating capital (81.1% vs 73.9%) and on operating
   margin (35.3% vs 29.9%). Displacement happens at the node-qualification cycle, which turns
   over every two to three years. **Quantified crudely from what is filed: Semiconductor
   Systems is $20,798M of revenue at a 54.2% gross margin; the loss of one major process step
   at one node is worth several hundred million dollars of gross profit a year, compounding as
   the node scales.** **Likelihood at the margin: [x] a real possibility. Wholesale
   displacement: a low-level possibility**, because the qualification lock cuts both ways.
   *(Customer concentration compounds it: two customers are 20% and 14% of nine-month FY2026
   revenue — 34% between them.)*

- **The bear case stated as its holders would state it [E4-51]:** *AMAT is the largest
  supplier in an industry where it earns the sixth-best gross margin of eight; its principal
  competitor names it by name in its two biggest markets and out-earns it on every measure; six
  more named competitors in those markets cannot be priced from any SEC filing; its gross
  margin has fallen in three of the four revenue declines it has ever reported and its own
  MD&A blames the fall on lower sales; it files no unit count with which to prove any of its
  growth was volume; its Semiconductor Systems order book has fallen 44% in three years while
  revenue rose; a third of its revenue is in a country whose own suppliers its filing says US
  policy is helping; it operates under a suspended export-denial order after paying $253
  million to the agency that could impose it; its nine-month cash-after-capex is lower than
  last year's on revenue 11% higher; and management is buying the stock hardest at the highest
  price it has ever been.* **Every clause of that is filed, and I accept it as fairly put.**
- **What it does not establish is a death.** Owner earnings were positive in the worst year in
  a nineteen-year record that contains a −38% revenue collapse and an operating loss; the
  company is net cash by $8bn; the earliest maturity is $1.2bn against $14.5bn of liquidity;
  and the annuity segment grew revenue and held operating income through the one downturn for
  which segment data exists.

- **VERDICT: [x] IN — GREAT on the long record (GOOD on the last three years), and the range
  is wide, one-sided, and survivable.**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

*Q1 IN · Q2 IN · Q3 IN · Q4 IN. The gate is open and this is a normal Q5 output, not a
computation.*

### THE JUDGED LEVEL — [E4-41] applied, and the brief's Q5 prior tested

The brief's stated way of being wrong at Q5 was: *"AMAT is the cheapest of the three equipment
names on the screen; if the honest normalized level holds up better than KLAC's, the floor is
closer."* **That is what happened, and it is measured rather than asserted. It is still not
close enough.** Every lengthening of the window lowers the yield:

| window | OE $M | yield | yield on cap net of net cash |
|---|---|---|---|
| best year ever filed, D&A end (FY2024) | 7,708.0 | **2.136%** | 2.184% |
| best year ever filed, capex end (FY2023) | 7,104.0 | 1.969% | 2.013% |
| 3-yr FY2023–25 | 6,348.0 | 1.759% | 1.799% |
| 5-yr FY2021–25 *(corpus default [E2-42])* | 5,534.2 | 1.534% | 1.568% |
| 5-yr leave-two-out | 4,552.3 | 1.262% | 1.290% |
| **8-yr FY2018–25 — the shortest window containing a down year** | **4,524.5** | **1.254%** | **1.282%** |
| 10-yr FY2016–25 | 4,125.2 | 1.143% | 1.169% |
| 10-yr leave-two-out | 3,404.8 | 0.944% | 0.965% |
| 15-yr FY2011–25 | 3,149.1 | 0.873% | 0.892% |
| 19-yr FY2007–25 | 2,768.4 | 0.767% | 0.784% |

**JUDGED OWNER EARNINGS: $4,525M**, the 8-year FY2018–25 mean. **The judgment, disclosed as a
judgment:** the 5-year default window FY2021–25 lies entirely inside the wave whose step Stage
0 measured at **2.74x**; the 15- and 19-year windows contain a company a third the present
size; **FY2018–25 is the shortest window that contains a genuine revenue decline (FY2019,
−12.6%) and the pre-wave base.** It is the same construction the KLAC run used, for the same
reason. **The full $2,768M–$7,708M band is carried, not discarded.**
**One filed cross-check on the judgment, and it supports it:** in the nine months to
2026-07-26 — a period of record revenue — **operating cash flow less capital expenditure was
$3,580M against $3,655M a year earlier, down 2.1%.** The current year is not running above the
judged level despite revenue 11.4% higher.

**1. THE YIELD**
- **owner earnings $4,525M ÷ market cap $360,857M = 1.254%** · **sovereign 5.24%**
- band: **0.767% to 2.136%** — *and 2.136% is the best single year AMAT has ever filed, taken
  at the (c) = D&A ceiling this run ruled INVALID.*
- on the market cap net of **$7,957M of net cash** ($10.03/share): **1.282%**, band 0.784% to
  2.184%.

**2. WHAT THE PRICE ALREADY ASSUMES** *(perpetual-growth form, as everywhere in this queue)*
- **to match the bare sovereign: +3.99%/yr perpetual** (3.48% at the 3-yr window; 4.47% at the
  19-yr; 3.10% at the most generous construction available).
- **to clear the [E4-28] floor: +8.75%/yr PERPETUAL** — **8.50% on the screen's own
  construction, which this run reproduces to two decimal places** (5,512 ÷ 368,001 = 1.498%;
  10 − 1.498 = 8.50%; the row says 8.5). Range **8.03%** (best year) to **9.23%** (19-yr).
- **What the business has actually done — and here AMAT differs from KLA in the direction that
  hurts AMAT.** Owner-earnings CAGR, every window published per **[E4-38]**:

  | window | owner earnings | revenue |
  |---|---|---|
  | 7-yr FY2018 → FY2025 | **+8.15%** | +7.85% |
  | 9-yr FY2016 → FY2025 | **+10.72%** | +11.3% |
  | 14-yr FY2011 → FY2025 | **+6.54%** | +7.35% |
  | 18-yr FY2007 → FY2025 | **+5.12%** | **+6.13%** |

  **The KLAC run recorded that KLA's filed record over every window from eight to fifteen
  years EXCEEDED the rate its floor required, and had to answer that. AMAT's does not.** Over
  the two windows that contain a full cycle — fourteen and eighteen years — **AMAT has
  compounded owner earnings at 6.54% and 5.12% against the 8.75% its price requires
  perpetually.** Only the two shortest windows, both contaminated by the wave and by the
  FY2024 China pre-buy, exceed it. **The floor case here would need AMAT to grow faster
  forever than it has grown over either of its own completed cycles.**
- **Why it fails on three further independent bounds:**
  1. **[E4-38] — terminal-date selection.** Every favourable window ends at the top of the
     largest capital-spending wave in the industry's history. The corpus names this exact
     distortion — *"a calculated selection of either initial or terminal dates"* — and its
     remedy is to publish them all, which is done above. **The 2.74x step from the pre-wave
     mean is the size of the terminal-date effect, and the backlog is already telling the
     other story: Semiconductor Systems' order book is down 44% in three years while its
     revenue rose.**
  2. **[E4-44]/[E2-63] — decomposition, and the margin lever is largely spent.** The 18-year
     5.12% came almost entirely from revenue (+6.13%/yr); the margin lever added roughly a
     point a year and **operating margin is already 29.9% against a 4.7% trough and a 30.2%
     peak.** Reaching a 40% operating margin — which no full-line materials-engineering
     supplier has ever held — adds ~34% in total and then contributes zero forever. **That
     leaves revenue to carry 8.75% perpetually, from a $28bn supplier that is already a large
     fraction of total industry wafer-fab-equipment spending.** Perpetual 8.75% doubles the
     company every 8.3 years: ~$57bn of revenue by 2034, ~$113bn by 2042. *"the value of an
     asset, whatever its character, cannot over the long term grow faster than its earnings
     do."*
  3. **[E4-35] — the base rate, and the burden of proof it imposes.** *"fewer than 10 of the
     200 most profitable companies in 2000 will attain 15% annual growth in earnings-per-share
     over the next 20 years."* A floor case here needs **~8.75% perpetual, forever**, from a
     cyclical capital-goods supplier whose own eighteen-year record is 5.12%. That is a lesser
     claim than 15% for 20 years but the same class of claim, and the burden sits on the buyer.
- **And the measurement I cannot make, recorded rather than glossed [E4-55]: with no unit or
  installed-base series filed, none of that growth can be decomposed into price and volume.**

**3. WHAT YOU ARE PAID**
- **−3.99 points over the sovereign** at the judged level; **−4.47 to −3.10** across the whole
  band. **There is no construction in this file — no window, neither capex end, including the
  best single year ever filed with all net cash credited — in which AMAT pays as much as a
  30-year Treasury.** *(For the record beside its peers: KLA on 2026-09-07 paid −4.17 points.
  AMAT pays −3.99. It is the closest of the three and it is on the same side of the line.)*

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- **sovereign used 5.24% — the bare rate, no per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate (a
  business you cannot be certain about fails Q1) and in the discount to value demanded at the
  end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]**, on 793,597,443 shares, with net cash of
$7,957M ($10.03/share) credited as a separate line per the ACLS precedent:

| | conservative (19-yr) | **judged (8-yr)** | optimistic (3-yr) | most generous construction available |
|---|---|---|---|---|
| **zero growth, at the 5.24% sovereign** | $66.57 | $108.80 | $152.65 | $185.36 |
| **plus net cash $10.03** | **~$77** | **~$119** | **~$163** | **~$195** |
| **at the [E4-28] 10% floor, plus net cash** | **~$45** | **~$67** | **~$90** | ~$107 |

- **conservative ~$77 · judged ~$119 · optimistic ~$163 · CURRENT PRICE $454.71**
- **The price is 2.80x the TOP of the entire zero-growth-at-the-sovereign band and 5.9x its
  bottom; it is 5.05x the top of the floor band and 10.1x its bottom. Against the single most
  generous construction this file can build — best year ever filed, at the (c) = D&A ceiling
  ruled invalid, with every dollar of net cash credited — the price is still 2.33x.**
- *For scale against the precedent: KLA's price was 3.9x the top of its zero-growth band.
  **AMAT is meaningfully cheaper than KLA and meaningfully above its own value range.** Both
  statements are true and neither cancels the other.*

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- **FLOOR VERDICT FIRST. Honest pre-tax expectancy = owner-earnings yield + sustainable
  growth.** The growth judgment is disclosed: **6.5% perpetual-equivalent**, which is **above**
  AMAT's own 18-year owner-earnings CAGR (5.12%) and above its 18-year revenue CAGR (6.13%),
  and is therefore already generous.

  | construction | yield | + growth | **expectancy** |
  |---|---|---|---|
  | 19-yr window | 0.767% | 6.5% | **7.27%** |
  | **judged 8-yr** | **1.254%** | **6.5%** | **7.75%** |
  | 5-yr window | 1.534% | 6.5% | **8.03%** |
  | 3-yr window | 1.759% | 6.5% | **8.26%** |
  | best year ever filed | 1.969% | 6.5% | **8.47%** |
  | *best year + a generous 8% growth* | 1.969% | 8.0% | *9.97%* |
  | *best year, ex-net-cash cap, + 8% growth* | 2.013% | 8.0% | ***10.01%*** |

  **Every construction built on evidence sits BELOW the ~10% floor. The floor is reached at
  exactly one point in the whole table, and only by stacking three separate generosities at
  once: the best single year AMAT has ever filed as the level, 8% perpetual growth — above
  anything it has achieved over either completed cycle — and crediting the entire cash pile
  against the price.** **[E4-18] is the governing rule on that construction:** *"If a verdict
  only holds after narrowing assumptions, it is UNKNOWABLE … Gathering more evidence is
  legitimate; torturing the evidence you have is not."* **It is not accepted, and it is
  printed so that the reader can see how close the file came and on what terms.**
  *"that's the figure we quit on … that's true whether short rates are 6 percent or whether
  short rates are 1 percent"* **[E4-28]**.
- **→ THE NAME IS NOT RANKED. It is QUIT ON.** Per the template, the ranking lines below the
  floor are not filled in: there is no ranking position, and no comparison against the
  opportunity set is owed for a candidate that does not reach the floor.
- points over sovereign, recorded for the register: **−3.99** (band −4.47 to −3.10).

**WHICH BAR** *(one only)*
- [x] **SCREAMER TEST [E4-01, E4-25]** — take the conservative end and ask whether the price
      already clears it. **No margin is added on top; "startlingly low" is what you observe,
      not what you subtract.** Conservative case **~$77/share**; price **$454.71**.
      **OUTCOME THREE: the price is above the whole range. NO.**
      *(Bar 1 is not used and no end margin is applied — using both on the same number is
      forbidden, and Bar 2 is the honest bar when the answer is not close.)*
- **WINDAGE COUNT: ONE.** Conservatism is spent once, at the **[E4-41]** normalization of the
  level from the 5-year default to the 8-year window. Everything else is realistic or runs the
  *other* way: no risk premium in the rate **[E3-42]**; no end margin **[E4-48]**; **net cash
  credited in full**, which raises the value; and the operating-segment-capex construction that
  would have raised owner earnings by ~$1.7bn was considered at Q4 and **refused**. **The
  windage does no work: the verdict is identical at every point in a 2.78x band.**

- **VERDICT: [x] IN is NOT reached and UNKNOWABLE is NOT used — the name FAILS at Q5, on
  price, at the [E4-28] floor. Ranking position: NONE — quit on, not ranked.**
  *This is a verdict about the price on 2026-09-04, not about the business. Q1–Q4 all returned
  IN and Q4 returned GREAT.*

## Q6 — NOT OPENED. No entry; no position exists.

Q6 governs a holding. There is none and none is created. What follows is the **pre-committed
re-look, written in advance per [E1-02]** — *"I believe in establishing yardsticks prior to
the act"* — so that a future run cannot rationalise its way back in.

**THE PRICE RE-LOOK.** **~$119/share judged, zero growth at a 5.24% sovereign with net cash
credited; the [E4-28] floor clears near ~$67/share (~$90 generous) — an 80–85% decline.**
**So the file is likelier to re-open on earnings than on price**, and the earnings condition is
stated as a number: at $454.71 the floor needs **~$35.3bn of owner earnings** against $4.5bn
judged — a **7.8x** gap. *(At the bare sovereign it needs ~$18.5bn, a 4.1x gap.)*

**THESIS-CONFIRMING METRIC (both halves, two consecutive fiscal years, because either alone is
gameable):** **Semiconductor Systems segment gross margin holding above 54.0% in a year in
which that segment's revenue FALLS.** That is the [E2-44](1) pricing test — the one test this
run could not perform because no such year exists inside the disclosure window — run at the
segment level, mix-free. **It is the single observation that would most change this file.**

**BULL BREAKERS — pre-registered so they cannot be rationalised away later:**
- **Semiconductor Systems segment gross margin below 52.0%** in any year, or a fall in that
  margin in a year when its revenue falls. The FY2019 answer was a 1.3-point consolidated
  fall; a repeat at segment level converts Q2's NARROW to NONE.
- **Semiconductor Systems backlog below $6.0bn**, or total backlog below $13.0bn — the series
  has run $19.0bn → $15.0bn in three years and it is the honest forward number AMAT files.
- **Any activation of, or extension to, the suspended BIS denial order**, any missed audit
  milestone, or any new export-controls charge. **This is the one item that is not a valuation
  matter — it is the named way the business dies.**
- **Resolution of the open DOJ and SEC export-controls matters, or of the separate DOJ
  federal-award-applications matter, on terms including any admission, any named individual,
  or any unsuspended sanction.**
- **[E2-49] a fourth segment recast in four years**, or the withdrawal of any of three
  disclosures: **segment cost of products sold** (which is what makes segment gross margin
  computable and is what let this run do what the KLAC run could not), the segment backlog
  table, or revenue by customer location. A yardstick disposed of after deterioration is
  itself the finding — and one such disposal has already been recorded in FY2026.
- **AGS gross margin below 32.0%**, or AGS revenue declining year on year for the first time
  in the filed record.
- **RD&E below 11.0% of revenue** while revenue grows — under-investment, not leverage.
- **Any acquisition above ~$2bn**, which would be the first in the period read and would open
  the [E3-40] loss-of-focus vector that $54M of acquisitions in three years has kept shut.
- **A third customer above 10%, or either of the top two above 25%.**
- **The share count rising for two consecutive years** — it has already stopped falling
  (793.6M at 2026-07-26 against 792.9M at 2025-12-05).

**BEAR BREAKERS — the facts that would make me wrong in the other direction:**
- **AMAT filing a unit, installed-base or systems-shipped series for the first time**, which
  would close the [E4-55] blind spot that is one of the five caps on Q2's class.
- **A filed ASP series rather than a directional sentence**, or any price-range disclosure of
  the kind ACLS files.
- **Any of Tokyo Electron, ASM International, SEMES, Wonik IPS, SCREEN Holdings or Hitachi
  becoming an SEC periodic filer**, which would close the six unpriced cells at the centre of
  the competitor row.
- **AGS gross margin rising toward the Semiconductor Systems level**, which would convert the
  annuity from the low-margin half into the franchise-inside-the-franchise the brief posited.
- **Non-GAAP Economic Profit — AMAT's own company-selected pay metric — breaking above
  $4,866M**, its FY2022 level, which it has not done in three years.

**THE MONITORING QUESTION [E3-30], stated now so the answer is not invented later:** *is the
44% fall in Semiconductor Systems backlog, against rising revenue, an aberrational
order-timing effect — shorter lead times as supply chains normalised — or has the business
slipped in a way that permanently reduces intrinsic value?* **On the evidence today it reads as
the former, because revenue and segment gross margin both rose through it.** **Two more years
of backlog falling while revenue rises reverses that**, and [E4-17] is explicit that such
beliefs *"change quite gradually"* — while [E2-40] is equally explicit that once a view **has**
crystallized, delay is the graver error.

**Catalysts:** **Q4 FY2026 results and the FY2026 10-K, mid-November and mid-December 2026** —
the first full year on the recast segment basis, guided to **$10.25bn ±$500M of Q4 revenue**,
and the first annual filing to show whether the receivables build converted to cash; the
**FY2027 DEF 14A, late January 2027** (AMAT files 2024-01-24, 2025-01-22, 2026-01-28); and the
**BIS audit milestones**, the first of which falls inside the three-year suspension window that
began 2026-02-11.

**Position size: ZERO.** No position is taken. Had one been contemplated it would have been
**sized DOWN** in any case, because the **[E5-08](2) capital-allocation flag is live** and
**[E4-13]** binds it to position size and to nothing else.

- **VERDICT: NOT OPENED — no holding exists.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN → Q2 IN → Q3 IN → Q4 IN → Q5 FAIL
      on price. Q6 not opened because no position exists.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q2's class is
      **NARROW**, not PROVISIONAL: the six unpriced competitors are **non-registrants** (four
      with no SEC ticker line, one an unsponsored ADR with no periodic filings, one
      deregistered by Form 15F-12B on 2012-04-27), and under the ACLS adjudication an
      *additional* competitor can only narrow a moat, never widen one — so the gap caps the
      class rather than suspending it, and it is carried as a Q6 work-order.
- [x] Every UNRESEARCHED verdict names its artifact. **One item is UNRESEARCHED-with-no-
      document and it is recorded as UNKNOWABLE-from-the-filing-rung instead:** the outcome of
      the open DOJ and SEC export-controls matters and the separate DOJ federal-award-
      applications matter. No filing in existence resolves them; they are a Q6 monitoring item,
      not a verdict, and they are not load-bearing on the Q5 answer.
- [x] Every absence claim names its sweep and is worded "no instance found", per the
      **absence-claim rule**: unit / installed-base series (6 AMAT vintages + LRCX FY2026) ·
      ASP or price-range series (6 vintages) · market-share figure (6 AMAT vintages + LRCX ×2 +
      the 7 peer filings read for the KLAC row) · EBITDA (3 vintages, zero occurrences) ·
      competitor names in AMAT's own 10-K (6 vintages) · margin by geography (all vintages) ·
      capitalized-software caption (FY2025 cash-flow statement) · the identity of the public
      equity holding (FY2025 10-K + Q3 FY2026 10-Q) · a named individual, admission or
      restatement in the export-controls matter (3 10-K vintages + the 10-Q) · SEC registrant
      status of six named competitors (`company_tickers.json` + submissions histories).
- [x] Step 0: the filing was read; **accession `0001628280-25-056742`** plus the Q3 FY2026 10-Q
      `0001628280-26-058235` and the 2026 DEF 14A `0001193125-26-027307`; three cash-flow lines
      cross-checked to the filed statement; Note 15 reconciled to the filed revenue and
      operating income.
- [x] Owner earnings on a multi-year mean; **ten constructions across six windows published
      [E4-38]**; the capex band disclosed as a judgment, with the **D&A end ruled INVALID for
      this filer under [E5-20]** and the reason given in twelve years of filed ratios.
- [x] Competitor row filled: **8 registrants with filed same-formula figures**, six named
      non-registrants recorded with the rung and the obstacle, and the row's cash-in-denominator
      distortion corrected at Q4 on an ex-cash basis for the three largest.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury
      daily par yield curve), dated 2026-09-04, struck fresh this run.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen (Bar 2, the screamer test); **windage count ONE**, stated and located.
- [x] Prices dated; the aggregator quote flagged as a live quote only.
- [x] Run committed to git after every question under the write-early protocol.
- [x] **Operator rule 9 discharged, and it changed a number.** The brief expected Q1–Q4 IN and
      a Q5 fail, which is what happened — the outcome most at risk of confirmation bias. The
      disconfirming hunt was therefore run in **both** directions, and the direction that
      mattered was the one that hurt my own bear case: **the "7.6% incremental return" I had
      published at Q2 was an artifact of $8.3bn of cash sitting inside the denominator, and the
      correct figure is 95.3%.** It is corrected in a marked block at the head of Q4, with Q2
      left standing, and the correction is recorded as cutting *against* the file's own
      argument and *against* the KLAC precedent this run was measured on.
- [x] **The screen row was reproduced before it was rebuilt**, per the brief: `oe_top` 7,419
      exactly (3-yr D&A end), `oe_bottom` 5,512 exactly (5-yr capex end including the FY2023
      finance-lease additions), yield 1.498%, growth required 8.50%. Both the width and the
      step were then rebuilt over this run's own windows: **width 2.78x against the row's
      1.35x; step 2.74x against the row's 2.0x.**

## REGISTER
- **Verdict: [x] OUT ON PRICE at Q5** — about the price, not the business. Not UNRESEARCHED (no
  named document would change it) and not UNKNOWABLE (the evidence is in).
- **One line:** *The cheapest of the three equipment names on this screen, and still 2.8x the
  top of its own zero-growth value range — the first of them whose own full-cycle growth record
  falls short of the growth its price requires.*
- **If UNRESEARCHED — the work order:** n/a to the verdict.
- **If UNKNOWABLE:** n/a to the verdict. **Three things are genuinely unknowable from the
  filing rung and are recorded as findings rather than as verdicts:** the **physical unit and
  installed-base series** (no count in six vintages; the segment backlog table is the nearest
  substitute and is not the same thing); the **outcome of the open DOJ and SEC matters**; and
  the **identity of the $1.3bn public equity holding** whose mark runs through reported income.

---
# THE TWO REQUIRED OUTPUTS (queue contract)

## 1. THE PRICE
**Current price $454.71** (2026-09-04 close, aggregator, flagged as a live quote only) on
**793,597,443 shares** hand-read off the Q3 FY2026 10-Q cover = **market cap $360,857M**.

**Value, zero growth against the 5.24% US Treasury 30-year, with net cash of $7,957M
($10.03/share) credited, as a round-number range [E4-01]:**

> ### conservative ~$77 · **judged ~$119** · optimistic ~$163 per share
> ### at the [E4-28] 10% floor: ~$45 to ~$90, **judged ~$67**

**The price is 2.80x the top of the entire zero-growth band, 5.05x the top of the floor band,
and 2.33x the most generous single construction this file can build.**
Owner-earnings yield **1.254%** (band 0.767%–2.136%) against a **5.24%** sovereign; **−3.99
points over the bond.** Growth required to clear the floor: **+8.75%/yr perpetual**, against a
filed eighteen-year owner-earnings CAGR of **5.12%**.

## 2. PASS / FAIL

# ❌ FAIL — at Q5, ON PRICE, at the [E4-28] floor.
### Q1 IN · Q2 IN (NARROW, narrower than KLAC's) · Q3 IN (overlay, two flags, one open candor question) · Q4 IN (GREAT) · **Q5 FAIL** · Q6 not opened.

**All four business gates returned IN.** The file closes on price alone: at 1.254% against a
5.24% bond, AMAT pays roughly a quarter of what a Treasury pays, on every window and both capex
ends, including the best single year it has ever filed with every dollar of net cash credited.
It is **quit on under [E4-28], not ranked** — there is no ranking position. **It is however the
closest of the three equipment names this queue has run** (−3.99 points against KLA's −4.17,
and 2.80x its value band against KLA's 3.9x), and the one construction that reaches the floor —
best year ever filed, 8% perpetual growth, ex-net-cash capitalisation — is printed above so that
the reader can see exactly how much stacking it takes and refuse it for the stated reason
**[E4-18]**.
