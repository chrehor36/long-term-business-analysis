# Company Run — KLA CORPORATION (KLAC) — 2026-09-07
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
- **rate 5.24%** · **date 2026-09-04** · source: **US Treasury daily par yield curve,
  30-year, from the issuing authority** (`tools/sources.py`, struck fresh this run per the
  2026-09-02 correction; FRED is the fallback, not the source).
- Earnings currency: **USD**. KLA is a Delaware domestic filer reporting in USD. Its revenue
  is overwhelmingly non-US by *destination* (Taiwan/China/Korea), and that is an exposure
  question read at Q2 and Q4 — not an FX repricing question, because the tools are sold and
  the receivables carried in dollars. No ADR ratio: single class, direct Nasdaq listing.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Form 10-K, FY ended 2026-06-30, filed 2026-08-06, accession `0000319201-26-000027`**
  — the anchor document, and the most recent annual filing in existence at run date.
- Vintage 10-Ks read for the through-cycle series: FY2025, FY2024, FY2023, FY2020, FY2019
  (accessions recorded in `_research 2026-09-07 KLAC/`).
- **Figure cross-checked against the filed statement:** *Net cash provided by operating
  activities*, FY2026 Consolidated Statements of Cash Flows — see the Q4 cross-check block.

**Price and shares:**
- price **$185.60**, 2026-09-04 close (aggregator via `tools/run.py` — **live quote only,
  flagged** per operator rule 5)
- shares **1,306,546,783**, hand-read off the **FY2026 10-K cover**, *"Common Stock, $0.001
  par value per share"*, as of **2026-08-03**. **Single class.** run.py's 1,319.6M is the
  weighted-average diluted/basic blend — the standing tool defect — and is rejected again.
- **market cap $242,495M** (1,306,546,783 × $185.60). The screen's $229,430M was struck at
  an earlier quote; the construction is the same.

**THE 10:1 SPLIT — GUARD VERIFIED BY HAND, TWO INDEPENDENT FILED SERIES.** The brief warned
the split guard must be checked, not assumed. It is checked:
1. **Shares outstanding, filed balance sheet:** 134.4M (FY2024) → **132.0M (FY2025) →
   1,307.0M (FY2026)**. Shares *issued*: 280.6 → 281.2 → **2,816.6M**. Both series step by
   exactly **10.0x** in a year in which the company **bought stock back** — a buyback cannot
   multiply a share count, so the step is the split and nothing else.
2. **Dividends declared per share, independently tagged:** **$5.65 (FY2024) → $6.75 (FY2025)
   → $0.80 (FY2026)**. $0.80 × 10 = **$8.00**, which continues the increase series rather
   than breaking it. Two unrelated filed series agree on the same 10:1 factor.
**The cover count is post-split scale and is used as filed. No adjustment applied, and none
is needed** — this is the AAPL/WMT/CTAS guard run again and it passes clean.

---
# STAGE 0 — THE SCREEN ROW, REBUILT BY HAND, AND WHAT IT GOT WRONG

**Construction, as everywhere in this queue:** owner earnings = **OCF − SBC − capex**
(the conservative end) and **OCF − SBC − D&A** (the other end), $M, from `companyfacts`
XBRL taking the **originally filed** value at each fiscal-year end and flagging any later
restatement (the INTC defect: a superseded input silently inside a window).

| FY (Jun) | revenue | GM% | op inc | op m% | R&D% | OCF | SBC | D&A | of which intang. amort. | tangible D&A | capex | capex ÷ tang.D&A | **OE (capex end)** | OE (D&A end) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2009 | 1,520.2 | 43.1 | −131.2 | −8.6 | 24.4 | 195.7 | 105.5 | 135.8 | 0.0 | 135.8 | 22.2 | 0.2 | **67.9** | −45.7 |
| 2010 | 1,820.8 | 55.2 | 314.2 | 17.3 | 18.1 | 447.8 | 86.0 | 87.3 | 33.8 | 53.5 | 30.2 | 0.6 | **331.6** | 274.5 |
| 2011 | 3,175.2 | 60.3 | 1,160.3 | 36.5 | 12.2 | 823.2 | 81.4 | 86.0 | 32.9 | 53.1 | 51.2 | 1.0 | **690.6** | 655.7 |
| 2012 | 3,171.9 | 58.1 | 1,016.3 | 32.0 | 14.3 | 941.6 | 78.8 | 92.1 | 30.3 | 61.8 | 57.6 | 0.9 | **805.2** | 770.6 |
| 2013 | 2,842.8 | 56.5 | 729.7 | 25.7 | 17.2 | 913.2 | 70.1 | 87.5 | 20.8 | 66.7 | 74.6 | 1.1 | **768.5** | 755.6 |
| 2014 | 2,929.4 | 57.9 | 772.1 | 26.4 | 18.4 | 778.9 | 60.9 | 83.1 | 16.2 | 66.9 | 67.5 | 1.0 | **650.4** | 634.9 |
| 2015 | 2,814.0 | 56.8 | 661.3 | 23.5 | 18.9 | 605.9 | 55.3 | 80.5 | 15.8 | 64.7 | 45.8 | 0.7 | **504.8** | 470.1 |
| 2016 | 2,984.5 | 61.0 | 960.4 | 32.2 | 16.1 | 759.7 | 45.0 | 66.9 | 7.6 | 59.3 | 31.7 | 0.5 | **682.9** | 647.7 |
| 2017 | 3,480.0 | 63.0 | 1,276.3 | 36.7 | 15.1 | 1,079.7 | 50.9 | 57.8 | 3.0 | 54.8 | 38.6 | 0.7 | **990.1** | 970.9 |
| 2018 | 4,036.7 | 64.1 | 1,537.2 | 38.1 | 15.1 | 1,229.1 | 62.8 | 62.7 | 4.6 | 58.1 | 67.0 | 1.2 | **1,099.4** | 1,103.7 |
| 2019 | 4,568.9 | 59.1 | 1,389.4 | 30.4 | 15.6 | 1,152.6 | 94.2 | 233.2 | 87.4 | 145.8 | 130.5 | 0.9 | **927.9** | 825.2 |
| 2020 | 5,806.4 | 57.8 | 1,758.8 | 30.3 | 14.9 | 1,778.8 | 111.4 | 348.0 | 220.6 | 127.5 | 152.7 | 1.2 | **1,514.8** | 1,319.4 |
| 2021 | 6,918.7 | 59.9 | 2,488.5 | 36.0 | 13.4 | 2,185.0 | 111.8 | 333.3 | 206.3 | 127.1 | 231.6 | 1.8 | **1,841.6** | 1,739.9 |
| 2022 | 9,211.9 | 61.0 | 3,654.2 | 39.7 | 12.0 | 3,312.7 | 126.9 | 363.3 | 229.1 | 134.2 | 307.3 | 2.3 | **2,878.5** | 2,822.4 |
| 2023 | 10,496.1 | 59.8 | 3,994.7 | 38.1 | 12.4 | 3,669.8 | 171.4 | 415.1 | 260.6 | 154.5 | 341.6 | 2.2 | **3,156.8** | 3,083.3 |
| 2024 | 9,812.2 | 60.0 | 3,635.7 | 37.1 | 13.0 | 3,308.6 | 212.7 | 401.7 | 239.3 | 162.5 | 277.4 | 1.7 | **2,818.5** | 2,694.2 |
| 2025 | 12,156.2 | 60.9 | 5,014.2 | 41.2 | 11.2 | 4,081.9 | 265.0 | 394.1 | 220.4 | 173.7 | 335.3 | 1.9 | **3,481.6** | 3,422.8 |
| 2026 | 13,579.5 | 61.3 | 5,660.8 | 41.7 | 11.3 | 4,143.1 | 310.2 | 394.0 | 190.8 | 203.2 | 375.9 | 1.9 | **3,457.0** | 3,438.9 |

*Operating income is computed on the identical formula used for every peer in the Q2 row —
**revenue − cost of revenue − R&D − SG&A** — because KLA stopped tagging the
`OperatingIncomeLoss` subtotal after FY2014 (the same defect the ACLS run recorded against
this filer). Restatements found across vintages and rejected as immaterial: FY2018 capex
$66.9M vs $67.0M; FY2017/18 R&D and SG&A differ by $0.1–1.1M; FY2020 taxes paid $194.6M vs
$204.7M. None of them touches a window boundary.*

## THE SCREEN'S 5.2% SPREAD IS THE FOURTH SPREAD DEFECT AGAIN — SIXTH CONSECUTIVE RUN

The corrected queue row reads `oe_bottom 3,092 · oe_top 3,252 · spread 0.052`. **Both ends
reproduce to the dollar and the width between them is not a width.** `oe_bottom` is the
**5-year FY2022–26 mean at the D&A end**; `oe_top` is the **3-year FY2024–26 mean at the
capex end**. Two different windows, two different capex ends, one number called a spread —
the identical construction that misled on AAPL, GOOGL, AVGO, AMD and INTC.

**Rebuilt over six windows and both capex ends, per [E4-25]** — *"working with a range of
possibilities is the better approach"* — and per [E4-38]'s remedy, **publish every window**:

| window | capex end | yield | D&A end | yield | growth needed to reach the 10% floor |
|---|---|---|---|---|---|
| 3-yr FY2024–26 | **3,252.4** | 1.341% | 3,185.3 | 1.314% | 8.66% |
| 5-yr FY2022–26 *(the corpus default [E2-42])* | **3,158.5** | 1.302% | 3,092.3 | 1.275% | 8.70% |
| 8-yr FY2019–26 | **2,509.6** | 1.035% | 2,418.3 | 0.997% | 8.97% |
| 10-yr FY2017–26 | **2,216.6** | 0.914% | 2,142.1 | 0.883% | 9.09% |
| 15-yr FY2012–26 | **1,705.2** | 0.703% | 1,646.6 | 0.679% | 9.30% |
| 18-yr FY2009–26 | **1,481.6** | 0.611% | 1,421.3 | 0.586% | 9.39% |
| 5-yr leave-two-out | 2,951.2 | 1.217% | | | 8.78% |
| 10-yr leave-two-out | 1,903.4 | 0.785% | | | 9.22% |
| **best year ever filed (FY2025)** | **3,481.6** | **1.436%** | | | **8.56%** |

- **TRUE WIDTH: 1,421.3 to 3,252.4 = 2.29x, a 128.8% spread.** The screen said 5.2%. The
  brief's warning was correct and is now confirmed for the sixth consecutive name.
- **The width does NOT change the verdict, and that is the point worth stating.** Every
  construction in the table — including the best single year KLA has ever filed, and
  including the (c) = D&A ceiling — yields **under 1.5% against a 5.24% sovereign**. This is
  the rare case where [E4-25]'s *"too wide to reach a conclusion"* does not bite: the range
  is enormous and lies **entirely on one side of the answer**.

## [E4-41] — THE STEP-UP FLAG IS REAL, AND THE SCREEN UNDERSTATES IT BY MORE THAN HALF

The row says `level_shift 1.73 · STEP UP — normalize down`. By hand:
- **pre-wave five-year mean, FY2015–19: $819.3M**
- **wave five-year mean, FY2022–26: $3,158.5M**
- **step = 3.86x**, not 1.73x.

*"Favourable exogenous breaks in the window are named and removed before the mean is
trusted"* **[E4-41]**. They are named at Q4. Recorded here: the current level is not a
level, it is a peak on a wave whose height the screen measured at less than half its size.
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, without management's language.** A chip fab prints tens of
billions of features onto a wafer through several hundred sequential steps. A vanishing
fraction go wrong and the die is scrap. **Yield — the share of good die on a wafer — is the
entire economics of a fab**, and a fab now costs $20bn+. KLA does not make chips and does
not make the machines that make chips. **KLA sells the machines that let the fab see what
went wrong**: optical and electron-beam scanners that find a defect a few nanometres across
on a moving wafer, metrology tools that measure whether a printed feature is the width the
design called for, and the software that tells the engineer which of three hundred steps
broke. A yield point on a leading-edge line is worth more than the whole process-control
tool budget, which is why the tool is bought.

That mechanism produces a specific and unusual revenue shape, and the filing splits it:
- **Product $10,453.5M** and **Service $3,125.9M** (FY2026, MD&A "Revenues and Gross Margin"
  table). Product is the fab's capital decision. Service is the fab's *operating* decision —
  *"The amount of our service revenues is typically a function of the number of systems
  installed at our customers' sites and the utilization of those systems"* (Item 7).
- **Three reportable segments** (Note 17), and the franchise is one of them:

| segment, FY2026 | revenue | % of revenue | segment profit | % of segment profit | segment margin |
|---|---|---|---|---|---|
| **Semiconductor Process Control** | **$12,244.7M** | **90.2%** | **$5,482.8M** | **97.0%** | **44.8%** |
| Specialty Semiconductor Process | $584.1M | 4.3% | $64.6M | 1.1% | 11.1% |
| PCB and Component Inspection | $750.4M | 5.5% | $108.0M | 1.9% | 14.4% |

  **Everything in this file that matters is the first row.** The other two are 9.8% of
  revenue and 3.0% of profit, and one of them lost money in two of the last three years.
- By product category (Note 17): **Wafer Inspection $6,630.8M (49%)**, Patterning $2,706.8M
  (20%), Services $3,125.9M (23%). Inspection plus patterning metrology is 69% of the
  company.

**The scarce input this business controls.** Two things, and they are different in kind:
1. **The physics of seeing a sub-10-nanometre defect at production throughput** — deep-UV
   and e-beam optics, the illumination and detection chains, and the algorithms that
   separate a killer defect from noise. This is defended with **R&D of $1,532.1M, 11.3% of
   revenue** (FY2026), a line that has never fallen in the eighteen years read.
2. **The process of record.** A fab qualifies a specific tool into a specific step and the
   defect library accumulates against that tool. Swapping the inspector mid-node means
   re-qualifying, which is why the installed base is sticky and why service grows off it.

**Will the fundamentals look broadly the same in ten years?** The *mechanism*, yes: as long
as chips are patterned they must be inspected, and the smaller the feature the more
inspection is needed per wafer. The *level*, emphatically no — and the filing says so
itself, which is why this sentence is quoted at Q4 and again at Q5:

> *"Heavy investments in the capacity and infrastructure needed to support AI-driven
> semiconductor growth have elevated our customers' capital spending. While AI adoption is
> likely to continue and grow, **the sustainability of such elevated investments cannot be
> assured.**"* — FY2026 10-K, Item 1A

That is not a Q1 failure. A cyclical business is understandable *as* a cyclical business —
the ACLS precedent — and the cycle is visible in the filed record: revenue 1,520 → 3,175 →
2,814 → 13,579 ($M, FY2009–26), with an operating **loss** in FY2009. The business is
simple, the customers are twenty companies, and the accounts are legible. What must not
happen is for the cycle to be quietly treated as a level, and Stage 0 has already flagged
that the screen did exactly that.

- **VERDICT: [x] IN**

*Recorded against myself under operator rule 9: the Q1 pass rests on the business being
simple and legible, not on it being good. The INTC precedent is the warning — a
semiconductor business can be perfectly understandable and still fail Q2 on its own filed
risk factors. Q2 is decided on the row.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The brief's claim: the strongest structural position in semiconductor equipment — process
control, sold into every fab whatever else it buys, with a service annuity on the installed
base. The brief's own prior for how it could be wrong [E4-26]: that the position is held by
customer preference rather than by structure, and that the ACLS test would show it in the
last downturn's pricing. Both were run straight. The verdict is IN, NARROW — and it is the
strongest narrow this queue has recorded.**

### The three criteria [E3-03]

- **(1) Needed or desired — YES.** A leading-edge line cannot be yielded without inspection
  and metrology; the tool is bought to protect the fab's whole output, not to add capacity.
- **(2) No close substitute — PASSES, and it is evidenced from the ATTACKERS' filings, not
  from KLA's.** KLA's own 10-K supplies no share number (below). The competitors do supply
  the structure:
  > *"**Although the market for process control systems used in semiconductor manufacturing
  > is currently concentrated and characterized by relatively few participants,** the
  > semiconductor capital equipment industry is intensely competitive. **We compete mainly
  > with Onto Innovation Inc., and KLA Corp.**"* — **Nova Ltd**, 20-F FY2025, acc.
  > 0001178913-26-000504, Item 3.D
  and the switching mechanism, stated by the challenger in the same paragraph:
  > *"**A substantial investment is required by the customers to evaluate, test, select and
  > integrate capital equipment into a production line. As a result, once a manufacturer has
  > selected a particular vendor's capital equipment, we believe that the manufacturer
  > generally relies upon that equipment for the specific production line application and
  > frequently will attempt to consolidate its other capital equipment requirements with the
  > same vendor.**"* — Nova, same filing
  Lam Research files the identical mechanism in its own words (10-K FY2026, acc.
  0000707549-26-000037): once qualified, *"the manufacturer generally maintains that
  selection for that specific production application and technology node."*
- **(3) Not price-regulated — passes on price, and the ACLS inversion applies here too.**
  Nobody caps KLA's prices. What is regulated is **who it may sell to**, and the licence
  belongs to the US government. Item 1A, verbatim: *"**the U.S. export restrictions on
  semiconductors and semiconductor technology to China and Chinese customers may reduce the
  need for our products and make it easier for our China-based competitors to develop and
  sell their own products and take market share from us.**"* [E2-59] governs: a regime that
  moves the boundary is not the company's moat, in either direction.

### [E4-04] — must the moat be continuously rebuilt?

**No — this is the defence case, not the replacement case, and the distinction from INTC is
exact.** Intel's moat basis (the process node) must be *wholly replaced* every generation at
$20–25bn a year, which is why the INTC run put it in [E4-04]'s excluded class on 2026-09-07.
KLA's moat spend is **R&D of $1,532.1M, 11.3% of revenue**, defending platform families that
have been in the catalogue for decades (Surfscan, Archer, Teron, eDR) against slowly moving
device roadmaps. A lapse narrows the lead; it does not vaporise the structure, because the
installed base and the process-of-record qualification persist while it is repaired.
**Capex is 2.8% of revenue.** The capital intensity of this industry belongs to KLA's
customers, not to KLA. **No key-person dependence found [E4-23].**

### The primary moat metric, filing-sourced, and its trend — AND THE DISCONFIRMING HALF

The primary metric is **gross margin, because it is the only pricing instrument this filer
files.** Stated as a limit before it is used: **KLA files no ASP, no price list and no price
range** — the ACLS run had a filed system price range ($2.6M–$12.0M) that rose through a 26%
revenue collapse, and **that instrument does not exist here.** *Recorded sweep: no instance
found of an average selling price, price range or unit price in the FY2026, FY2025, FY2024,
FY2023, FY2020 or FY2019 10-Ks.* So the [E2-44] price test must run on margin alone, and
margin is mix-confounded — which is why it is run at the **segment** level, where the mix is
controlled.

**Semiconductor Process Control segment gross margin, from the segment note (Note 17,
"segment revenues less segment costs of revenues", the same definition in both vintages —
and the FY2024 figures agree TO THE DOLLAR across the FY2024 and FY2026 10-Ks: $5,629,302 on
$8,733,556):**

| FY (Jun) | SPC revenue $M | SPC gross profit $M | **SPC gross margin** | consolidated GM |
|---|---|---|---|---|
| 2022 | 7,924.8 | 5,167.7 | **65.21%** | 61.0% |
| 2023 | 9,324.2 | 5,957.6 | **63.89%** | 59.8% |
| **2024 — revenue −6.3%** | **8,733.6** | **5,629.3** | **64.46%** ↑ | 60.0% |
| 2025 | 10,947.4 | 7,024.6 | **64.17%** | 60.9% |
| 2026 | 12,244.7 | 7,791.2 | **63.63%** | 61.3% |

**[E2-44](1) — can it raise prices when demand is flat and capacity is not fully utilized?
The ACLS test PASSES, mix-free: in FY2024 the franchise segment's revenue fell 6.3% and its
gross margin ROSE 0.57 points.** That is the one test a no-moat supplier cannot pass, and it
is passed at the segment level where the Orbotech/PCB mix cannot flatter it.

**And now the disconfirming half, hunted deliberately [E4-26], because it is the strongest
fact in this file against my own conclusion.** From the FY2022 peak the same segment's gross
margin has fallen **65.21% → 63.63%, −1.58 points, across a period in which its revenue grew
54.5%.** In the largest capacity boom in the company's history, at record volume and
utilisation, the core franchise's gross margin drifted *down*. Meanwhile **consolidated**
gross margin *rose* 61.0% → 61.3% — because the loss-making PCB/Display line was exited. **The
headline margin improvement is a mix effect and the underlying franchise margin declined.**
This is the HAS/EFX lesson applied in the direction that hurts: read the profit mix, not the
headline. It does not overturn the FY2024 downturn pass, but it is the honest counterweight
to it and it belongs in Q6's monitoring set.

**The other counterweight, and it is the deepest one: FY2009.** Consolidated gross margin
**43.1%** and an **operating LOSS of $131.2M** — 13 to 21 points below every year since. That
is the filed record of what a genuine semiconductor capex collapse does to this business, and
it is why the class below is NARROW and why Q4 and Q5 normalize hard.

### THE SERVICE ANNUITY — the franchise inside the franchise, and its disclosure wall

**What the filing gives (Item 7, "Revenues and Gross Margin" table, five vintages):**

| FY | Product $M | **Service $M** | service % of revenue | service YoY |
|---|---|---|---|---|
| 2018 | 3,160.7 | 876.0 | 21.7% | — |
| 2019 | 3,392.2 | 1,176.7 | 25.8% | +34.3% |
| 2020 | 4,328.7 | 1,477.7 | 25.4% | +25.6% |
| 2021 | 5,240.3 | 1,678.4 | 24.3% | +13.6% |
| 2022 | 7,301.4 | 1,910.5 | 20.7% | +13.8% |
| 2023 | 8,379.0 | 2,117.0 | 20.2% | +10.8% |
| **2024 — product −11.0%** | **7,482.7** | **2,329.6** | **23.7%** | **+10.0%** |
| 2025 | 9,472.9 | 2,683.3 | 22.1% | +15.2% |
| 2026 | 10,453.5 | 3,125.9 | 23.0% | +16.5% |

- **The annuity test passes on the revenue line, decisively: in FY2024 product revenue fell
  11.0% and service rose 10.0%.** That is what an installed-base annuity is supposed to do
  and it did it. Service has never had a down year in the nine filed.
- **Two facts that cut the other way and are usually left out.** (a) Service's **share** of
  revenue is *lower* today (23.0%) than in FY2019 (25.8%) — the annuity is growing in
  dollars and shrinking in mix. (b) Over the full eight years service compounded at
  **17.2%** and product at **16.1%** — the annuity is barely outgrowing the cycle it is
  supposed to be independent of, because it is *driven by* the installed base the cycle
  builds.
- **THE HAS/EFX PROFIT-MIX TEST CANNOT BE RUN, AND THE ABSENCE IS THE FINDING.** The brief
  required service's share of **gross profit or operating income**, not revenue. *Recorded
  sweep across six 10-K vintages (FY2019, FY2020, FY2023, FY2024, FY2025, FY2026): **no
  instance found** of a "cost of service revenues" line, a "cost of product revenues" line,
  a product-versus-service gross profit split, a service gross margin, a service contract
  attach rate, or a service contract renewal rate.* KLA's income statement carries **one
  undifferentiated caption, "Costs of revenues,"** and there is no gross profit line at all.
  The segment note cannot substitute, because it says so itself: *"**Services are offered in
  multiple segments.**"* **The profitability of the annuity is not disclosable from KLA's
  filings.** Under the four-verdict test this is UNKNOWABLE from the filing rung, not
  UNRESEARCHED — no SEC document exists that resolves it — and it is recorded as a **moat
  defect**, because the single most-cited reason to own KLA is a number the company has
  chosen not to file.
- The one hard number under the annuity runs the wrong way: **deferred service revenue fell
  from $896.9M to $842.2M** in FY2026 (balance sheet, current $604.1M + non-current $238.1M),
  a **−$54.6M** move that ties exactly to the cash-flow line *"Deferred service revenue
  (54,617)"*. Service revenue rose 16.5% while the deferred balance behind it fell.

### [E4-55] — WHERE UNITS EXIST, MONITOR UNITS. HERE THEY DO NOT EXIST.

*Recorded sweep of the FY2026 10-K for: systems shipped, units shipped, tools shipped, number
of systems, number of tools, installed base as a count, units sold, wafers or transistors
inspected in absolute terms.* **No instance found.** The filing says *"growth in our installed
base of tools"* three times and never sizes it. The only counts in the document are 9,100
patents, 3,600 pending applications and ~17,000 employees.

**This is WORSE than ACLS, which at least filed an installed base of ~3,400 tools rising
through its bust.** [E4-55]'s whole point is that *"Dollar revenue flattered by pricing is
how a shrinking franchise hides; the physical series is the honest one."* **KLA can only be
read in dollars.** Revenue growth cannot be decomposed into price and volume from any filing.
Carried as a named blind spot, and it is one of the two reasons the class is NARROW.

### THE COMPETITOR ROW — required [E3-28]

**Identical formula for every filer**, because KLA stopped tagging the `OperatingIncomeLoss`
subtotal after FY2014: **OP = revenue − cost of revenue − R&D − SG&A** (sales-and-marketing
plus G&A where a peer splits them). ROUNTOA = OP ÷ (assets − goodwill − intangibles −
non-interest-bearing current liabilities) — *a CONVENTION of this row, [E2-43] in the closest
computable form, year-end denominators.* Latest full fiscal year each.

| | **KLA** | AMAT | LRCX | ASML | **ONTO** | CAMT | **NVMI** | ACLS |
|---|---|---|---|---|---|---|---|---|
| latest FY | FY2026 6/30/26 | FY2025 10/26/25 | FY2026 6/28/26 | FY2025 cal | FY2025 1/3/26 | FY2025 cal | FY2025 cal | FY2025 cal |
| form · accession | 10-K `0000319201-26-000027` | 10-K `0001628280-25-056742` | 10-K `0000707549-26-000037` | 20-F `0001628280-26-011378` | 10-K `0001193125-26-066937` | 20-F `0001178913-26-001561` | 20-F `0001178913-26-000504` | 10-K `0001104659-26-020461` |
| revenue | **$13,579.5M** | $28,368.0M | $23,232.7M | €32,667.3M | $1,005.3M | $496.1M | $880.6M | $839.0M |
| **gross margin** | **61.3%** | 48.7% | 50.5% | 52.8% | 49.7% | 50.5% | 57.4% | 44.9% |
| R&D % revenue | 11.3% | 12.6% | 10.2% | 14.4% | 13.1% | 9.7% | 16.3% | 13.0% |
| **operating margin** | **41.7%** | 29.9% | 35.3% | 34.6% | **19.0%** | 25.8% | 28.8% | 14.2% |
| **ROUNTOA** | **48.5%** | 34.5% | 52.0% | 49.4% | 15.7% | 12.0% | 12.6% | 10.2% |
| goodwill | $1,788.8M | $3,707.0M | $1,630.0M | €4,588.6M | $644.0M | $74.3M | $90.8M | none |

*ASML is left in **EUR, not converted** — a stated rung limitation; only its margins and
ratios are comparable, not its levels. KLA's ROE (87.5% on average equity) is **excluded as a
quality signal**: it is a buyback-and-debt artifact (equity was $1.4bn on $12.6bn of assets at
FY2022). ROUNTOA is the comparable column.*

**GROSS MARGIN THROUGH BOTH DOWNTURNS — the [E2-44] test run across the cohort:**

| FY | **KLA** | AMAT | LRCX | ASML | ONTO | CAMT | NVMI | ACLS |
|---|---|---|---|---|---|---|---|---|
| 2018 | 64.2 | 45.0 | 46.6 | 46.0 | 54.2 | 49.4 | 57.8 | 40.6 |
| **2019 ↓** | **59.1** | 43.7 | 45.1 | 44.7 | **44.1** | 48.3 | 54.2 | 42.0 |
| 2021 | 59.9 | 47.3 | 46.5 | 52.7 | 54.4 | 50.9 | 56.6 | 43.2 |
| 2022 | 61.0 | 46.5 | 45.7 | 50.5 | 53.6 | 49.8 | 55.5 | 43.7 |
| **2023 ↓** | **59.8** | 46.7 | 44.6 | 51.3 | 51.5 | 46.8 | 56.6 | 43.5 |
| **2024 ↓** | **60.0** | 47.5 | 47.3 | 51.3 | 52.2 | 48.9 | 57.6 | 44.7 |
| 2025 | 60.9 | 48.7 | 48.7 | 52.8 | 49.7 | 50.5 | 57.4 | 44.9 |
| 2026 | **61.3** | — | 50.5 | — | — | — | — | — |

**The row's finding, and unlike ACLS's it cuts FOR the subject:**
1. **KLA holds the highest gross margin in the set in every one of eleven fiscal years,
   in booms and in troughs, without a single exception.** The narrowest the gap to
   second place has ever been is **4.7 points** (FY2019, vs Nova). Against its *direct*
   inspection/metrology rivals — Onto and Camtek — **the gap has never been under 9.6
   points.** ACLS's row showed the lowest margin in its cohort; KLA's shows the highest in
   the same cohort, on the same formula.
2. **The FY2019 −5.1-point drawdown is the one apparent blemish and it is a MIX event, now
   resolved rather than left open:** FY2019 is the first year consolidating **Orbotech**
   (closed 2019-02-20), a lower-margin PCB/display business, and the segment table shows the
   drag directly — PCB & Component Inspection earned a **$(470.3)M segment loss in FY2024**
   and $(281.2)M in FY2025. The franchise segment did not fall; the acquired one did.
3. **[E2-45] — the attacker's test has already been run by an actual attacker, and filed.**
   Onto Innovation, the closest pure-play, with ample capital and skilled personnel:
   > *"**We have, from time to time, selectively reduced prices on our systems in order to
   > protect our market share, and competitive pressures may necessitate further price
   > reductions.**"* … *"Some of our competitors have greater financial, engineering,
   > manufacturing and marketing resources, broader product offerings and service
   > capabilities and **larger installed customer bases than we do.**"* … *"**Some of our
   > competitors have more extensive support and service infrastructures than we do, which
   > could place us at a disadvantage.**"* — Onto 10-K FY2025, acc. 0001193125-26-066937,
   > Item 1A, in a section whose competitor sentence begins *"We principally compete with
   > KLA…"*
   **Onto cut price to defend share and still earns 19.0% against KLA's 41.7%.** The
   attacker's test is not a thought experiment here; it is on file, with the result.
4. **[E4-32] direction — WIDENING in scope, and the evidence is the attacker's own language
   changing on a datable schedule.** Onto's FY2019 10-K: *"Our principal competitor for
   advanced packaging inspection **is Camtek Ltd.**"* Onto's FY2023 and FY2025 10-Ks: *"Our
   principal competitors for advanced packaging inspection are **KLA and Camtek Ltd.**"*
   **KLA was added to the advanced-packaging inspection contest between FY2019 and FY2023 by
   the incumbent it was attacking** — the same evidence class the INTC run used in the
   opposite direction. Advanced packaging is the fastest-growing part of the market.
5. **Peers taken: 8, against 5 competitors KLA names itself.** Filed same-formula figures
   obtained for **7 registrants**. **The row's limit, stated: two of KLA's five named
   competitors are non-registrants and were NOT priced — Hitachi High-Tech Corporation
   (inside Hitachi Ltd, TSE 6501; no 10-K/20-F) and Lasertec Corporation (TSE 6920).** These
   are real competitors in exactly the two niches where KLA's lead is least established —
   e-beam review/CD-SEM and EUV reticle inspection. Adjudicated under the ACLS rule: **an
   additional competitor can only narrow a moat, never widen one**, so their absence cannot
   manufacture a stronger class — it caps the class at NARROW and becomes a **Q6 monitoring
   work-order**, not an UNRESEARCHED close.
6. **[E3-61] limit:** the row shows position, not conduct. On conduct the filed record is
   the FY2024 segment-margin rise through a 6.3% revenue decline, and Onto's filed admission
   that *it* is the one cutting price.

### The claims NOT made, each refused with its reason

- **[E2-53] dominance class — REFUSED.** *"Once dominant … Good or bad, it will prosper."*
  KLA does not prosper good or bad: it posted an **operating loss in FY2009** and a 6.5%
  revenue decline in FY2024. **The marketplace, not the position, sets the level** — the
  identical finding the ACLS run recorded. KLA is the highest-margin participant in a
  violently cyclical industry, which is not the same thing as being insulated from it.
- **[E3-33]/[E5-28] untapped pricing power — NOT CLAIMED.** Claiming it claims near-monopoly.
  *Recorded sweep: **no instance found** of a process-control market-share figure in KLA's
  own 10-K or in any of the seven peer filings read.* The only quantified statements KLA
  makes about share are conditional and negative (*"any loss of competitive position could
  negatively impact our prices … and market share"*). **Any "KLA holds ~55% of process
  control" number entering this project must name a source that is not an SEC filing** — the
  resolving document is a paid Gartner/TechInsights/VLSI segment report, which sits **off
  this framework's evidence ladder**. And the segment gross margin drifting down 1.58 points
  through a record boom is affirmative evidence *against* unused pricing power.
- **[E4-36] which of the four causes?** Honestly: **an extreme max on one or two variables
  (defect-detection physics plus installed-base lock-in) riding a very large wave.** The
  structure is ownable and predates the wave — the eleven-year unbroken margin lead proves
  that. The *current level* is the wave, and Item 1A says so: *"the sustainability of such
  elevated investments cannot be assured."* Both are held: the class is judged on the
  structure; Q4 and Q5 are computed off the normalized level.

### Customer power — the [E3-03](3) inversion, quantified

- **One customer, TSMC, is ~19% of total revenue in FY2026 and FY2025** (Note 17), up from
  **13% in FY2024**. Concentration is rising, not falling.
- **China is 29.8% of revenue** (FY2026), having been **42.8% in FY2024**, 33.3% in FY2025,
  and 16% in FY2018. **KLA files the China percentage in every vintage read — it DIFFERS
  from ACLS, where the run found no China revenue percentage had ever been filed.** In
  dollars China is flat at ~$4.05bn for three years while total revenue grew 38%: *"Revenue
  in China was comparable to the prior fiscal year, as continued investments in legacy-node
  technologies by domestic semiconductor companies were largely offset by export control
  restrictions affecting certain advanced technology transactions."*
- Nova independently names the same threat: *"new competitors enter our market from time to
  time, including **the recent emergence of local competitors in China.**"*

- Class: [ ] WIDE  **[x] NARROW**  [ ] NONE  [ ] PROVISIONAL · **Direction: WIDENING in the
  peer margin gap and in product scope (advanced packaging); NARROWING at the China edge and
  — the fact I like least — in the franchise segment's own gross margin.**
- **VERDICT: [x] IN — NARROW, and the strongest narrow this queue has recorded.**
  *The strongest fact against this verdict, stated per [E4-51] so a bear would accept it as
  fairly put: **the Semiconductor Process Control segment's gross margin has fallen 1.58
  points from its FY2022 peak while its revenue grew 54.5%.** If the [E2-44] pricing test is
  the one test a no-moat supplier cannot pass, then a franchise that cannot hold its gross
  margin at record volume is showing the first millimetre of the same crack — and the second
  fact is that **there is no unit series and no service margin with which to check it.**
  Held IN on the FY2024 segment-margin rise through a revenue decline, on eleven unbroken
  years of the highest gross margin in the cohort, and on two rivals conceding installed
  base, service infrastructure and price conduct in their own filings.*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — THE WEIGHT CASE, DECLARED.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution [E3-38]** — NOT ticked. [E3-38]'s root class is the undifferentiated
  product whose *"only products are promises"* **[E2-70]**, which magnifies the manager.
  KLA's product is the most differentiated thing in its cohort by the one measure filed —
  eleven consecutive years of the highest gross margin in an eight-company row. Q2 found a
  franchise, and by **[E3-43]** a franchise tolerates some mis-management. The technology
  roadmap dependence is real and it is the moat-*defence* spend, priced at Q2, not here.
- [ ] **Control [E1-16]** — NOT ticked. Liquid public minority stake; exit is a trade.
- [ ] **Leverage [E3-29]** — NOT ticked, and the numbers are given rather than asserted:
  **$5,950.0M of principal, every dollar of it fixed-rate senior unsecured notes, ZERO due
  before 15 March 2029** (Note 7), against **$4,902.4M of cash and marketable securities**
  and **$3,457.0M of annual owner earnings**. Interest of $284.4M is covered **12.2x** by
  owner earnings on the current year and **5.2x** on the eighteen-year mean. Book equity is
  small ($6,349.8M) but that is a **buyback artifact, not a leverage exposure** — the ACLS
  and CTAS treatment.

**NONE TICKED → Q3 IS A QUALITATIVE OVERLAY.** Findings are recorded; manager quality alone
does not stop this run and cannot promote it.

**Honesty — binary, permanent, filings-based [E5-16], each matter dated to when it became
PUBLIC.** *"understanding about business mistakes; tolerance for personal misconduct is
zero."*
- **THE 2006 OPTIONS-BACKDATING MATTER — recorded in full, not softened, because [E5-16] is
  a binary and a run that buries this has failed the test.** It became public **2006-05-22
  via a Wall Street Journal article, not by company disclosure.** The company restated
  **$348M pre-tax across FY1995–FY2005**. **The Board's own findings were that the option
  pricing was "intentional" and involved "falsification of Company records."** CEO Kenneth
  Schroeder was **terminated**; founder Kenneth Levy "retired" as Chairman Emeritus with a
  funded office and assistant to age 70. The SEC settled with the company **2007-07-25 with
  no fraud charge and no penalty**; a $65M class settlement; DOJ closed **2008-07-31**.
  **How it is weighed, stated so it can be attacked:** [E5-16] refuses integrity failures
  permanently, but it refuses them *about the people who committed them*. **Every actor is
  gone.** Richard Wallace became CEO in **January 2006**, in the aftermath, and has now served
  twenty years without a repeat. The matter is **dated to 2006** and stays dated — *"each
  matter dated to when it became PUBLIC, so the test stays point-in-time honest."* A run
  written in 2007 would have closed this file at Q3; a run written in 2026 records that the
  institution once falsified records, that it was caught by a newspaper rather than by its
  own disclosure, and that the disclosure conduct since has been clean. **It is not carried
  as a live disqualifier and it is not erased. It is the reason the FY2026 disclosure record
  above was read hard rather than assumed.**
- **No self-dealing found** in the current record. Related-party transactions are disclosed
  at a $100,000 threshold with dollar amounts attached; the one large item is **$159.3M of
  sales to Rapidus Corporation** (~1.3% of FY2025 revenue), on whose board director Emiko
  Higashi sat — **disclosed in the right place, with the number, and Higashi did not stand
  for re-election at the 2025 AGM.** That is the correct handling, not a concealment.
- Say-on-pay **92.39% for** at the 2025 AGM (8-K acc. 0001193125-25-272448, Item 5.07); ~92.5%
  in 2024. No shareholder proposals. One director, Robert Calderoni, drew 8.5% against —
  forty times the next-highest; cause not established (**UNRESEARCHED**, and immaterial to
  the verdict).

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30].** *Each is a prompt to READ, never a
verdict. The list is open, not closed.*
- [ ] **weak accounting** — not found. SBC is expensed and disclosed ($310.2M FY2026). PwC
  audits; no pension games (no material DB plan).
- [ ] **unintelligible footnotes** — not found. Note 7 (debt) prints every tranche with its
  effective rate; Note 17 prints segment cost of revenues, R&D and SG&A line by line; the
  impairments are *"recognized as separate charges"* with the quarter and the reporting unit
  named. This is legible reporting.
- [x] **TRUMPETED EARNINGS PROJECTIONS — FIRES, AND IT IS THE REAL ONE.** KLA issues formal
  **quarterly guidance on revenue, GAAP and non-GAAP gross margin, and GAAP and non-GAAP
  diluted EPS** in every earnings release. **[E5-30] is the governing reading — the behaviour
  is a ratchet:** *"once you start it, it's all over. You can't quit… And forecasting
  earnings, I can't imagine anything more destructive."* **[E3-48] requires the record be
  pulled and set against outturn, and it was, for eight consecutive quarters:**

  | | revenue vs guidance midpoint | non-GAAP EPS vs midpoint |
  |---|---|---|
  | FY25 Q1–Q4 | +3.35% · +4.31% · +2.10% · +3.25% | +4.71% · +5.81% · +4.47% · **+9.96%** |
  | FY26 Q1–Q4 | +1.90% · +2.23% · +1.94% · +2.32% | +3.28% · +1.72% · +3.52% · +6.77% |
  | **mean** | **+2.68%** | **+5.03%** |

  **Sixteen for sixteen above the midpoint. Never missed, never merely hit.** That is not
  forecasting skill; on a ±5% revenue band and a ±8–10% EPS band it is **a midpoint set to be
  beaten.** And the one quarter the GAAP number could not be made — **FY25 Q2, GAAP EPS $6.16
  against a $7.45 midpoint, below even the floor of the band, on a $239.1M impairment worth
  $1.76/share** — the non-GAAP number beat by 5.81% anyway. That is the whole distance
  between the two framings in one quarter, and it is the exact incentive [E5-30] warns about.
- [ ] **serial share issuance [E5-15]** — the reverse. Shares outstanding **155,995k (FY2016)
  → 130,698k (FY2026), −16.2%**, pre-split, falling every year since FY2019. Employee-plan
  issuance of ~0.5–0.7M/yr is swamped by repurchase. **The buyback is real retirement, not a
  dilution offset.** *The one exception is worth naming: FY2019 is the only year in eleven in
  which the count ROSE (156,048k → 159,475k) despite $1,095.2M of buybacks — because stock
  was issued for **Orbotech**, KLA's largest-ever acquisition.*
- [ ] **EBITDA / adjusted-earnings promotion [E4-29]** — **DOES NOT FIRE.** *Recorded sweep of
  the FY2019, FY2023 and FY2026 10-Ks for the string "EBITDA": **zero occurrences in all
  three**.* The fifth flag, which fires on most of this queue, is clean here.
- [ ] **filed-figure tells [E4-30]** — **DOES NOT FIRE, AND THE EVIDENCE RUNS THE OTHER WAY.**
  Cash taxes paid against pretax income, nine years, cross-checked to the filed cash-flow
  statement for FY2024–26:

  | FY | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | **FY18–26** |
  |---|---|---|---|---|---|---|---|---|---|---|
  | cash tax % of pretax | 17.4 | 13.9 | 15.5 | 13.8 | 13.3 | 13.1 | **26.0** | 19.1 | 13.9 | **16.3%** |
  | book rate % | 44.9 | 9.4 | 7.7 | 12.0 | 4.8 | 10.6 | 13.4 | 12.5 | 13.8 | **12.9%** |

  **KLA has paid $908.3M MORE cash tax than it booked as expense over nine years**, cash
  exceeding book in eight of nine. [E4-30] hunts the opposite signature — high book earnings,
  falling cash tax. The tax authorities' own view is that these earnings are at least as real
  as reported. *(FY2026's 13.9% is down from 26.0%, but the **book** rate is 13.8% — the two
  have converged, so the FY2024–25 elevation was the 2017 transition-tax hangover finishing,
  not a new shelter.)*
- [ ] **metric-switching [E2-49]** — not found. The MD&A leads with the same revenue/gross
  margin table in FY2019, FY2023 and FY2026; the segment presentation changed in FY2025 to
  comply with **ASU 2023-07**, which is a standards change and was announced as one, not a
  yardstick disposed of after deterioration.
- [x] **A NON-GAAP EPS METRIC INSIDE THE PAY PLAN — fires, bounded.** The FY2023 one-off
  "Complementary EPS Awards" pay on **non-GAAP diluted EPS which explicitly excludes
  "goodwill and intangible impairment."** That is the classic construction: it rewards the
  numerator for excluding the cost of a bad acquisition and the denominator for retiring
  stock. Tranche 1 earned **131% on cumulative EPS of $49.11** against a $47.18 target, over a
  window in which KLA retired ~3%/yr of its shares. **Three mitigations, all verifiable:** it
  was *"special grants made only in fiscal year 2023"* and is not the recurring plan; the
  exclusion list is **closed and enumerated at six named items**, not an open "other items
  management deems non-recurring"; and the proxy's own *"What We Don't Do"* table commits to
  different metrics for short- and long-term plans.

**[E4-52] — do the flags CONVERGE?** No. The lollapalooza test asks whether several flags
point at one outcome as a reinforcing system. Here the two live flags (guidance culture, a
retired non-GAAP EPS award) point at *managing the quarter*, while the strongest counter-
evidence — cash tax exceeding book by $908M, no EBITDA anywhere, a falling share count, a
cash-based recurring long-term metric — points the other way. **Two prompts, not a system.**

**STEP 3 — THE PRIMARY TEST [E2-01], on the right denominator.**

**KLA's ROE is EXCLUDED as a quality signal and the reason is stated:** book equity fell to
$1,401.4M on $12,597.1M of assets at FY2022 because of buybacks and $6bn of debt; the
resulting 237% and 116% ROE readings are a **leverage-and-buyback artifact**, exactly the
*"unusual debt-equity ratios"* carve-out **[E2-47]** and the reason **[E2-43]** substitutes
**unleveraged net tangible operating assets**. On that denominator (assets − goodwill −
intangibles − non-interest-bearing current liabilities), pre-tax operating return:

| FY | 2013 | 2015 | 2017 | 2019 | 2021 | 2023 | 2024 | 2025 | **2026** |
|---|---|---|---|---|---|---|---|---|---|
| **op income ÷ unlevered NTOA** | 18.0% | 18.9% | 31.0% | 37.4% | 50.1% | 56.1% | 41.1% | 51.5% | **48.8%** |

**[E3-46]'s "second question about the business is a number" is answered emphatically: a
48.8% pre-tax return on tangible operating capital, and the series has never gone below 11.7%
since FY2010.** It is the highest in the competitor row on the same formula except Lam's
52.0%. *Scope it honestly: the denominator is depressed by the same buybacks — but it is
TANGIBLE assets less operating liabilities, which buybacks reduce only through the cash they
consume, and KLA still carries $4.9bn of cash and securities inside it.*

**The [E2-56]/[E5-40] retention test — the great-business signature, and its caveat.**
FY2019–26: capex $2,152.3M plus acquisitions $2,418.3M = **$4,570.6M of capital invested**,
against operating income rising **$1,389.4M → $5,660.8M, +$4,271.4M**. That is a **~93%
incremental pre-tax return**, against [E5-40]'s *"quite satisfactory"* ~12%. **Caveat stated
before it is used [E4-26]: that is not a clean attribution — most of the $4.27bn came from
the AI capex wave, not from the $4.57bn.** The honest reading is the weaker and still
remarkable one: **KLA retained almost nothing** — owner earnings of $20,076.7M over those
eight years against $19,978.6M returned in buybacks and dividends, **99.5%** — and grew
operating income four-fold anyway. Growth here does not consume capital.

**The half-owner test [E2-26].** Passes, with three affirmative instances rather than an
absence:
1. The impairments are *"recognized as separate charges"*, quantified by quarter, by
   reporting unit, and split between goodwill and intangibles — **not buried in an adjusted
   figure.** ($219.0M and $70.5M in FY2024; $239.1M in FY2025; $256.6M in FY2020.)
2. The annual bonus grid is printed with **the target ($3.930bn), the actual ($4.404bn) and
   the payout (144%)**, and the balanced scorecard carries a self-scored **"3 — primarily
   meets expectations" on gross margin**, reason given: *"slightly less than our internal
   plan."* **A management gaming its disclosure does not print a below-plan self-score.**
3. The proxy volunteers that the Summary Compensation Table **overstates** the shares granted:
   *"the 30-day average price was 8% higher than the price on the date of grant, which is the
   price used to determine the value of the award."* A disclosure that works against the
   company's own headline.
**Against those, the [E2-26] failure of the file:** the item a half-owner would most want —
**what the service annuity actually earns** — is the one thing not disclosed (Q2). And the
guidance culture is the standing exception: the *assumptions* behind guidance live in an IR
Letter to Shareholders that every release **expressly disclaims from incorporation by
reference**, i.e. off the filed record and outside Section 18.

**The institutional imperative — all four scored [E2-30].** *Not a fraud test.*
- [ ] **resists change in current direction** — not found. KLA **exited the Display business
  in FY2024–25** and wrote off $528.6M of goodwill and intangibles doing it, renaming the
  segment. That is the opposite of resistance.
- [ ] **projects/acquisitions to soak up funds** — not found. **Acquisition spend is $2,418M
  in eight years, of which $1,818M is one deal in FY2019 and ZERO in FY2025 and FY2026**,
  while $19.98bn went out to shareholders. The absolute-size acquisition gate is not
  approached: nothing since FY2023 exceeds $27.1M.
- [ ] **staff studies justifying the leader's craving** — no instance found.
- [x] **peer behaviour mindlessly imitated — FIRES, softly, on two counts.** Quarterly EPS
  guidance is the sector norm and KLA follows it. And the **10-for-1 split of June 2026**
  (announced 2026-05-07; effective 2026-06-11; authorised shares raised 500M → 5,000M) is a
  cosmetic act that creates no value and followed a wave of large-cap splits. Neither is
  venal; both are the imperative operating exactly as [E2-30] describes.

**[E4-39] — the acquisition post-mortem, the rare positive tell. NOT FOUND, and the
acquisition needed one.** *Recorded sweep of the FY2019, FY2020, FY2023, FY2024, FY2025 and
FY2026 10-Ks: no instance found of KLA revisiting the **Orbotech** acquisition against its
announcement case.* The deal closed 2019-02-20 for **$3,255.6M of consideration, of which
$1,845.7M was booked as goodwill**; it was the only event in eleven years to increase the
share count; and it has since produced **~$776.6M of goodwill and purchased-intangible
impairments — about 41% of the goodwill recorded — in three separate years (FY2020 $256.6M ·
FY2024 $289.5M · FY2025 $239.1M)**, the exit of an entire product line, and a segment that
lost **$(470.3)M and $(281.2)M** in FY2024 and FY2025. **The word "synergies" disappears from
the 10-K after FY2021 and never returns.** The impairments themselves are disclosed cleanly,
which is the [E2-26] pass above. **What is absent is the Washington-Post-style review** —
*"almost never witnessed"* **[E4-39]** — and its absence is recorded rather than excused: a
deal that impaired 41% of its own goodwill and whose synergy language was quietly dropped is
precisely the deal that earns a post-mortem, and did not get one.

**CAPITAL ALLOCATION — THE TWO BUYBACK CONDITIONS [E5-08], AND CONDITION 2 FAILS HARD.**

- **(1) Ample funds for operations and liquidity? YES.** $4,902.4M of cash and marketable
  securities, $4,143.1M of operating cash flow, no debt maturity before March 2029.
- **(2) Repurchases at a MATERIAL DISCOUNT to conservatively calculated intrinsic value?
  NO — and it is not close.** The record, against implied average prices paid (pre-split):

  | FY | 2017 | 2019 | 2021 | **2022** | 2024 | 2025 | **2026** |
  |---|---|---|---|---|---|---|---|
  | buyback $M | **25.0** | 1,095.2 | 938.6 | **3,967.8** | 1,735.7 | 2,149.9 | **2,289.8** |
  | implied avg price | **~$103** | ~$108 | ~$256 | **~$413** | ~$575 | ~$720 | **~$1,263** |

  **The pattern is monotonic and it is backwards: the smallest buyback in eleven years
  ($25.0M) came at the lowest price (~$103), and the largest ($3,967.8M) came near the cycle
  top at ~$413 — funded by $2,967.4M of fresh debt raised in the same fiscal year.** Spending
  then rises with price every year to FY2026's $2,289.8M at ~$1,263. **[E5-24]'s first law —
  *"what is smart at one price is dumb at another"* — is being run in reverse.** Against this
  run's own Q5 range (a conservative $21.64–$47.51 per post-split share at the sovereign,
  zero growth), FY2026's repurchases were made at roughly **2.7x to 5.8x** the top of that
  band. Contrast [E5-25], where compliance looked like **publishing both conditions as
  numbers in advance** — KLA publishes a **$10.9bn standing authorisation** and no price
  discipline at all.
- **→ CAPITAL ALLOCATION FLAG, RAISED**, and stated with the humility clause **[E4-13]**:
  this rests on *our* IV range, and *"it is natural for CEOs to be optimistic about their own
  businesses. They also know a whole lot more about them than I do."* **[E5-08]** adds that
  *"infractions, even serious ones, are innocent; many CEOs never stop believing their stock
  is cheap."* **The flag binds POSITION SIZE, never the discount rate.**
- **Two things on the other side, stated so the charge is fair.** KLA **delevers after it
  levers** — the FY2022 debt was repaid $620.0M / $1,087.3M / $750.0M in FY2022/23/25. And
  the **dividend** record is the disciplined half of the same policy: **eleven consecutive
  fiscal years of increases, $2.08 → $8.00 pre-split, +14.4%/yr compounded, no cut and no
  freeze**, at a **25.5% cash payout ratio** of operating cash flow. *(Streak length before
  FY2016 is UNRESEARCHED and deliberately not claimed: the FY2015 **$16.50 special dividend**
  makes FY2016 look like an 89% cut on a naive reading, and that is exactly the artifact a
  streak claim gets built to dodge.)*
- **[E2-52]/[E2-60] — are the distributions funded by capital replacement?** Tested, and
  **no, not currently.** FY2025 and FY2026 dividends plus buybacks ($3,054.5M and $3,347.6M)
  are **75%** and **81%** of operating cash flow, funded from cash with **zero net debt
  issued in FY2026**. The one year it was not true is FY2022, and that debt has been partly
  repaid. **[E2-60]'s "financial strength" limb holds:** debt is flat at ~$5.9bn since FY2022
  while owner earnings doubled.
- **[E2-51] — the refusal tell** does not apply: they buy, aggressively. The demerit is the
  price, not the abstention.

**THE GUARDRAIL — checked before the verdict is written.**
- [x] Confirmed: **nothing in this Q3 is used to promote the name.** The 48.8% return on
  tangible capital is a fact about the *business* recorded at Q2's request [E3-46], not a
  compliment to the manager — *"a good managerial record … is far more a function of what
  business boat you get into than it is of how effectively you row"* **[E2-37]**.
- [x] This business does **not require** a superstar; no key-person dependence was recorded at
  Q2 **[E4-23]**.
- [x] No great manager is the reason to act. There is no excisable-cancer case here
  **[E2-35, E2-36]**; there is nothing to excise.
- **[E3-40] loss of focus?** The vector to watch. Orbotech was exactly the shape [E3-40]
  warns of — *"neglects its wonderful base business while purchasing other businesses that
  are so-so or worse."* But the evidence says the base business was **not** neglected (R&D up
  115% since FY2019; SPC segment revenue up 55% in four years) and the so-so business has now
  been **written down and partly exited**. Recorded as a **Q6 monitoring item**, not a live
  finding.
- **THE MATERIAL NEGATIVE, recorded plainly.** **All sixteen directors and executive officers
  together hold 120,462 shares of 131,684,530 outstanding — 0.0915%.** The CEO of twenty
  years holds **34,503 shares, 0.026% of the company.** There is no founder, no family and no
  anchor owner; the largest holders are Vanguard (10.3%) and BlackRock (8.8%). On the
  evidence of the share register these are **very highly paid employees, not owners** — CEO
  compensation $25.1M in FY2025 against a stake of ~$35–41M accumulated over 37 years at the
  company. It is not misconduct and it is not a disqualifier. It is the honest answer to
  *"how well do they treat their owners"* **[E3-59]** in its ownership limb, and it sits
  beside the capital-allocation flag rather than offsetting it.
- **VERDICT: [x] IN — as an OVERLAY, with one capital-allocation flag live.**
  *IN is **the absence of found disqualifiers, not a finding that these managers are
  honest** — [E5-17]: "People are not that easy to read. Sincerity and empathy can easily be
  faked," and [E5-32]: audited does not mean true. **IN never promotes**, and nothing here is
  used to repair Q2 or substitute for Q4.*
  **The two live flags, carried forward: (1) a quarterly EPS guidance culture with a
  sixteen-for-sixteen record of beating its own midpoint [E3-48, E5-30]; (2) a buyback
  programme run monotonically backwards on price [E5-08](2), which BINDS POSITION SIZE and
  nothing else [E4-13].** Against them: no EBITDA anywhere in three vintages, cash tax
  $908.3M above book over nine years, a falling share count, impairments disclosed as
  separate charges by quarter and reporting unit, and a self-scored below-plan mark printed
  in the proxy.

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**THE FILING CROSS-CHECK, operator rule 4.** Owner earnings are built from `companyfacts`
and the drivers are checked against the filed statement. FY2026 10-K, Consolidated Statements
of Cash Flows: *Net cash provided by operating activities* **$4,143,079 thousand**; *Common
stock repurchases* **$(2,289,769)**; *Payment of dividends to stockholders* **$(1,057,832)**;
*Income taxes paid, net* **$781,409**. All four agree with the tagged series to the dollar.
Note 17's segment reconciliation reproduces the operating-income formula used throughout this
file to the dollar in all three presented years.

**MORE THAN ONE WINDOW — AND THE SPREAD IS THE RANGE [E4-25], EVERY WINDOW PUBLISHED [E4-38].**
The full table is at Stage 0 and is not repeated. In summary, $M, capex end:

| 3-yr | 5-yr | 5-yr LTO | 8-yr | 10-yr | 10-yr LTO | 15-yr | 18-yr |
|---|---|---|---|---|---|---|---|
| 3,252.4 | 3,158.5 | 2,951.2 | 2,509.6 | 2,216.6 | 1,903.4 | 1,705.2 | 1,481.6 |

- **Combined range (window spread × capex band): $1,421.3M to $3,252.4M — a 2.29x width,
  128.8%.** The screen said 5.2%.
- **Is the range too wide to reach a conclusion [E4-25]? NO — and this is the unusual case
  where a 2.29x width settles nothing and settles everything at once.** The width is enormous
  and **every point in it lies on the same side of the Q5 answer**: the best construction
  available (best year ever filed, at the (c) = D&A ceiling) yields **1.44%** against a 5.24%
  sovereign. A range that is wide but wholly one-sided is a conclusion, not a failure to
  reach one.
- **The distorted years, named in both directions [E5-11, E4-41]:**
  - **UP — FY2022–26, the AI/leading-edge capex wave.** Named by the registrant itself:
    *"Heavy investments in the capacity and infrastructure needed to support AI-driven
    semiconductor growth **have elevated our customers' capital spending**. While AI adoption
    is likely to continue and grow, **the sustainability of such elevated investments cannot
    be assured.**"* Backlog rose **$7.86bn → $12.57bn** in one year on the same driver — with
    KLA's own caveat that *"backlog on any particular date does not provide meaningful
    information about the timing of future revenue recognition."*
  - **UP — FY2024, China.** China was **42.8% of revenue** that year, ~$4.2bn, on legacy-node
    pre-buying ahead of export controls. **This contaminates the one downturn observation the
    file has**, and it is stated rather than hidden: FY2024's gross-margin rise through a 6.5%
    revenue decline happened in a year with an abnormal China mix. It is not a clean stress
    test. *(It arguably understates the result — China legacy-node tools are the cheaper end —
    but "arguably" is not evidence, so the observation is carried with the caveat attached.)*
  - **DOWN — FY2019/FY2020, Orbotech.** The gross-margin trough of 57.8% (FY2020) was **not
    cyclical**: management's own MD&A bridge attributes it to Orbotech (−2.6pp) and intangible
    amortization (−1.6pp), against volume of only −1.0pp. *This closes the one item the
    competitor row had left open.*
  - **DOWN and KEPT IN per [E5-33]:** the **$785.1M** of goodwill and intangible impairments
    (FY2020, FY2024, FY2025) and the restructuring charges are real costs borne by
    shareholders and are **not** added back anywhere in this file.
- **[E3-55] scope check.** Is the width distortion, or is it certain-endgame volatility that
  should be treated as noise? **It is distortion, not See's-in-August noise.** See's loses
  money eight months a year around a level that is known; KLA's *level* moved 3.86x and the
  filing says the new level's sustainability "cannot be assured." The width is uncertainty
  about the level, which is exactly what [E4-25] says belongs in the open.

**MAINTENANCE CAPEX — (c) AS A DISCLOSED JUDGMENT, AND THE D&A END IS INVALID FOR THIS FILER.**

The corpus default is D&A **[E3-44, E2-41]**. **It does not apply here, and the reason is
arithmetic rather than rhetorical:**

| FY2026 | $M |
|---|---|
| D&A as tagged | **394.0** |
| less amortization of purchased intangibles | **(190.8)** |
| **= tangible depreciation** | **203.2** |
| **capital expenditures** | **375.9** |
| **capex ÷ tangible depreciation** | **1.85x** |

**Nearly half of KLA's "D&A" is purchase-accounting amortization of Orbotech-era intangibles
— a charge that requires no cash to renew and is running off toward zero (intangibles net
$1,373.2M in FY2019 → $230.8M in FY2026).** Using it as the (c) proxy would credit the
business with maintenance spending it does not do. **So the D&A end of `run.py`'s band is
INVALID for this filer** — the same ruling the CTAS run made for a different reason — and
**(c) is judged at total capex, $375.9M, which is 1.85x true tangible depreciation and is
therefore already conservative.**

- **[E3-44] direction question, answered: KLA is asset-LIGHT.** Capex is **2.8% of revenue**;
  net PP&E is $1,380.5M against $13,579.5M of revenue. It is not the railroad class [E5-20],
  and there is no inflation-conditioned understatement [E4-47] worth arguing about at this
  capex intensity. **The band's two ends differ by under 2% ($3,457.0M vs $3,438.9M in
  FY2026), so the capex band does no work in this file and cannot change the verdict.**
- **THE QCOM RULING APPLIED — R&D above the OCF line may be the real maintenance spend, and
  here it is.** KLA's competitive position is renewed in the **R&D line, $1,532.1M, 11.3% of
  revenue**, which is expensed and therefore **already deducted inside operating cash flow**.
  Owner earnings as constructed are conservative on this axis, not aggressive. **But the
  direction of that spend is a finding and it belongs at Q6: R&D as a share of revenue has
  FALLEN from 15.6% (FY2019) to 11.3% (FY2026)** — the maintenance spend is a smaller share
  of the business than it was, which is either operating leverage or under-investment, and
  the filing does not say which.
- **[E2-23] constraint 3, the working-capital increment — INCLUDED BY CONSTRUCTION and it
  bites hard here.** Inventory rose **$1,262.5M (FY2019) → $3,648.5M (FY2026)**, a $2,386M
  build, every dollar of which flows through operating cash flow as a use of cash and is
  therefore already inside owner earnings. This is a working-capital-hungry business and the
  method charges it correctly.
- **Stock compensation subtracted in full [E5-06]: $310.2M in FY2026**, and in every year of
  the eighteen-year series. Noted per **[E3-70]**: the reported charge is the *floor* of the
  correct subtraction, not the measure; no market-value adjustment is attempted and the
  understatement, if any, makes owner earnings **lower**, not higher.
- **ASC 842 — checked, immaterial.** Operating-lease ROU assets $335.1M, non-current operating
  lease liabilities $211.4M. *No finance-lease ROU asset is tagged in any year* — **the
  COST/HD finance-lease addendum fix does not bite on this filer.**
- **Software capex — checked.** There is **no separate capitalized-software caption** in the
  cash-flow statement; the single line is *"Capital expenditures."* **The HAS defect does not
  bite**, and if any software is capitalised inside that caption it makes (c) larger and the
  answer more conservative.

### Great, good, or gruesome? **[E4-20]**

- **[x] GREAT** — *"pays an extraordinarily high interest rate that will rise as the years
  pass."*
- **The evidence, and it is the strongest of any name in this queue:**
  - **48.8% pre-tax return on unleveraged net tangible operating assets** (FY2026), a series
    that has run 37.4% → 58.8% → 48.8% since FY2019 and has not been below 11.7% since FY2010.
    Highest in the competitor row on the identical formula bar Lam's 52.0%.
  - **Growth consumes essentially no capital.** Over FY2019–26 KLA earned **$20,076.7M** of
    owner earnings and returned **$19,978.6M** of it — **99.5%** — while operating income went
    from $1,389.4M to $5,660.8M. **A business that quadruples its profit while distributing
    everything it earns is the great account in [E4-20]'s own terms**, not the good one.
  - Capex 2.8% of revenue; net PP&E 10.2% of revenue.
- *The one qualification, stated: the "rise as the years pass" limb is the cycle's, not the
  position's. The rate has risen — and it fell in FY2009, FY2013, FY2015 and FY2024.*

### Staying power — all three scored **[E5-11]**

- **(1) A large and reliable stream of earnings — YES, with the honest caveat.** Owner
  earnings have been **positive in all eighteen years read, including FY2009 (+$67.9M) when
  the company posted an operating LOSS of $131.2M**. Reliable in sign; violently variable in
  size. **[E5-29] governs: volatility is not risk** — the impairment question is coverage,
  and coverage is not in question.
- **(2) Massive liquid assets — YES.** Cash **$1,649.8M** plus marketable securities
  **$3,252.6M** = **$4,902.4M**, against $5,950.0M of principal debt. Net debt ~$1.05bn,
  covered 3.3x by a single year's owner earnings.
- **(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — PASSES CLEANLY, and this is the one that
  usually kills.** Note 7: **$5,950.0M of principal, 100% fixed-rate senior unsecured notes,
  ZERO current maturities.** The earliest maturity is **$800M on 15 March 2029 — two and a
  half years out** — then 2032, 2034, 2034, 2049, 2050, 2052, 2062. **[E3-52] applies in
  KLA's favour**: this is long-dated, covenant-light, fixed-rate paper, *"in compliance with
  all of our covenants"*, plus $1,775.1M of **customer-prepaid contract liabilities** — the
  benefit of debt without its drawbacks. **[E5-39]'s test — nothing depends on the kindness
  of strangers — is met: no commercial paper, no revolver draw, no ratings trigger except a
  change-of-control-plus-downgrade put.**
- **Leverage, named and quantified [E4-16, E3-29]** — *there is no ratio ceiling in this
  framework*: **$5,950.0M principal; interest $284.4M; [E2-54] coverage — interest, both paid
  and accrued, out of current cash flow NET of ample capital expenditure — is 12.2x on FY2026
  owner earnings, 8.8x on the 5-year mean, and 5.2x on the eighteen-year mean including
  FY2009.** It clears on every window, which is what [E2-54] asks.
- **[E2-55] — score the worst case, not the expected one.** At the FY2009 analogue (revenue
  −40%, gross margin 43%), the fixed cost base of R&D + SG&A ($2,663.6M) against gross profit
  of ~$3,500M still covers interest four times over with $4.9bn of securities untouched and
  no maturity for years. **Certain, not merely likely.**
- **[E3-66] jurisdiction** — US filer, Delaware; shareholders stand first in the queue. Not
  an issue.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40]**

**Model exposure, not experience [E4-40].** The benign recent record is *"not only useless,
but actually dangerous"* as a guide. Three mechanisms, quantified from filed figures, and the
honest finding is that **none of them kills the business — they impair the level, which is a
Q5 fact, not a Q4 one.**

1. **THE CAPACITY GLUT — the [E2-27] mechanism proper, and the likeliest.** Every fab builds
   for AI at once; *"viewed individually, each company's capital investment decision appeared
   cost-effective and rational; viewed collectively, the decisions neutralized each other."*
   The capacity arrives, device prices fall, capex stops. **Quantified:** the filed FY2009
   precedent is a **−40% revenue year with a 43.1% gross margin and an operating loss.**
   Applied to today: revenue to $8,150M at a 55% gross margin gives gross profit $4,483M
   against a fixed R&D+SG&A base of $2,663.6M → operating income ~$1,819M. **It takes roughly
   a 60% revenue collapse (to ~$5.4bn) at a 50% gross margin to zero the operating line.**
   Owner earnings in a −40% year land near **$1.3–1.6bn** — inside the 15- and 18-year window
   means already published. **Likelihood: [x] a real possibility** on a five-to-ten-year view.
   **Fatal: no.** The company earns money and pays no maturities in it.
2. **CHINA — the [E4-40] exposure question, and the registrant writes the mechanism itself.**
   *"the U.S. export restrictions … may reduce the need for our products and **make it easier
   for our China-based competitors to develop and sell their own products and take market
   share from us**."* Nova independently names *"the recent emergence of local competitors in
   China."* **Quantified:** China is **$4,048.4M, 29.8% of revenue**. A total loss removes
   ~$2,590M of gross profit at the SPC segment's 63.6% margin against FY2026 operating income
   of $5,660.8M — **a 46% cut, taking operating margin from 41.7% to roughly 24%** and owner
   earnings to roughly **$1.4–1.6bn**. **Likelihood of a total loss: a low-level possibility.
   Likelihood of material erosion at legacy nodes: [x] a real possibility** — the dollars have
   already been flat for three years while the rest of the company grew 38%.
3. **CUSTOMER CONCENTRATION.** One customer, TSMC, at **~19% of revenue and rising from 13%**.
   Loss or insourcing removes ~$2,580M of revenue and ~$1,640M of gross profit. **Likelihood:
   a low-level possibility** — a fab does not build its own inspection tools, and no filing in
   the peer set describes a customer doing so.
- **The bear case stated as its holders would state it [E4-51]:** *KLA is a supplier whose
  earnings quadrupled because twenty customers decided at the same time to spend more than
  they ever have, on a technology wave the company itself will not vouch for; it has no unit
  series with which to prove any of that growth was volume rather than a spending spike; its
  core segment's gross margin is lower today than at the start of the boom; nearly a third of
  its revenue sits in a country whose own suppliers its filing says US policy is helping; one
  customer is a fifth of it; and management is buying the stock hardest at the highest price
  it has ever been.* **Every clause of that is filed, and I accept it as fairly put.**
- **What it does not establish is a death.** Owner earnings were positive in the worst year in
  the filed record, there is no maturity to refinance, the liquid book covers the net debt
  three times over, and the annuity did not fall when the product line did.

- **VERDICT: [x] IN — GREAT, on the position; and the range is wide, one-sided, and
  survivable.**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

*Q1 IN · Q2 IN · Q3 IN · Q4 IN. The gate is open and this is a normal Q5 output, not a
computation. **KLA is the sixteenth name in this queue to clear all four business gates.***

### THE JUDGED LEVEL — [E4-41] applied, and the brief's own trap sprung in its favour

The brief's stated way of being wrong on Q5 was: *"if the honest normalized level is far
below the current one, the yield is worse, not better."* **That is what happened.** Every
lengthening of the window lowers the yield, without exception:

| window | OE $M | **yield** |
|---|---|---|
| best year ever filed (FY2025) | 3,481.6 | **1.436%** |
| 3-yr | 3,252.4 | 1.341% |
| 5-yr *(corpus default [E2-42])* | 3,158.5 | 1.302% |
| 5-yr leave-two-out | 2,951.2 | 1.217% |
| **8-yr — the shortest window containing a down year** | **2,509.6** | **1.035%** |
| 10-yr | 2,216.6 | 0.914% |
| 15-yr | 1,705.2 | 0.703% |
| 18-yr | 1,481.6 | **0.611%** |

**JUDGED OWNER EARNINGS: $2,600M**, sitting just above the 8-year mean. **The judgment,
disclosed as a judgment:** the 5-year default window FY2022–26 lies *entirely inside* the
wave the registrant itself declines to vouch for, so it measures the peak, not the business;
the 15- and 18-year windows contain a company less than a third the present size and
understate real structural growth in inspection intensity; **the 8-year window FY2019–26 is
the shortest that contains both a genuine down year (FY2024) and the pre-AI base.**
The full **$1,421M–$3,252M** band is carried, not discarded.

**1. THE YIELD**
- **owner earnings $2,600M ÷ market cap $242,495M = 1.07%** · **sovereign 5.24%**
- band: **0.61% to 1.44%** — *and 1.44% is the best single year KLA has ever filed.*

**2. WHAT THE PRICE ALREADY ASSUMES** *(perpetual-growth form, as everywhere in this queue)*
- **to match the bare sovereign: +4.17%/yr perpetual** (3.90% at the 3-yr window; 4.63% at
  the 18-yr).
- **to clear the [E4-28] floor: +8.93%/yr PERPETUAL** — **8.66% at the 3-yr window, which
  reproduces the screen row's 8.65% to within two basis points.**
- **What the business has actually done — and this is the loudest fact against my own
  conclusion, stated per [E4-51] before it is answered.** Owner-earnings CAGR, every window
  published per [E4-38]: **+15.4% over 8 years · +17.6% over 10 · +11.3% over 15 · +11.0%
  from FY2012.** Revenue: +16.4% over 8 years, +10.2% over 15. **KLA's filed record over
  every window from eight to fifteen years EXCEEDS the 8.93% the floor requires.** This is
  the CTAS shape — the second name in this queue whose own history beats the rate its price
  demands — and it deserves an answer rather than a dismissal.
- **Why it fails anyway, on three independent bounds:**
  1. **[E4-38] — terminal-date selection.** Every one of those windows *ends at the top of
     the largest capital-spending wave in the industry's history*, and the registrant's own
     Item 1A says its sustainability *"cannot be assured."* The corpus names this exact
     distortion — *"a calculated selection of either initial or terminal dates"* — and its
     remedy is to publish them all, which is done above. The 3.86x step from the pre-wave
     mean is the size of the terminal-date effect.
  2. **[E4-44]/[E2-63] — decomposition, and the lever is nearly spent.** The 15-year 11.3%
     came almost entirely from revenue (+10.2%/yr); the margin lever added ~0.9 points a year
     and is close to exhausted, because **operating margin is already 41.7% and gross margin
     61.3% — both the highest in the eight-company row, and the core segment's gross margin
     is DRIFTING DOWN.** Even reaching a 50% operating margin adds ~20% in total and then
     contributes zero forever. That leaves revenue to carry 8.93% perpetually — **and KLA at
     $13.6bn is already better than a tenth of total industry WFE spending.** Perpetual 8.93%
     doubles the company every 8.1 years: ~$27bn by 2034, ~$54bn by 2042, ~$109bn by 2050.
     **That requires either a WFE market approaching a trillion dollars or a share gain
     without limit, from the participant that already earns the highest margin in it.**
     *"the value of an asset, whatever its character, cannot over the long term grow faster
     than its earnings do"* — and the ceiling here is the end market, named.
  3. **[E4-35] — the base rate, and the burden of proof it imposes.** *"fewer than 10 of the
     200 most profitable companies in 2000 will attain 15% annual growth in earnings-per-share
     over the next 20 years."* A floor case here needs **~9% perpetual, forever**, from a
     cyclical capital-goods supplier. That is a lesser claim than 15% for 20 years but it is
     the same class of claim, and the burden sits on the buyer.
- **And the measurement I cannot make, recorded rather than glossed [E4-55]: with no unit
  series filed, none of that growth can be decomposed into price and volume.** The single
  most important input to a growth judgment is unavailable from the primary source.

**3. WHAT YOU ARE PAID**
- **−4.17 points over the sovereign** at the judged level; **−4.63 to −3.80** across the
  whole band. **There is no construction in this file, on any window or either capex end,
  including the best year ever filed, in which KLA pays as much as a 30-year Treasury.**

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- **sovereign used 5.24% — the bare rate, no per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

- **sovereign used 5.24% — the bare rate, no per-name premium added [E3-42].** Certainty is
  handled at Q1 (understanding) and once at the end (Bar 2's conservative construction),
  never in the rate.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]**, on 1,306,546,783 shares:

| | conservative (18-yr) | **judged (8-yr)** | optimistic (3-yr) |
|---|---|---|---|
| **zero growth, at the 5.24% sovereign** | **~$22** | **~$38** | **~$48** |
| **at the [E4-28] 10% floor** | ~$11 | **~$20** | ~$25 |

- **conservative ~$20 · judged ~$38 · optimistic ~$50 · CURRENT PRICE $185.60**
- **The price is 3.9x the TOP of the entire zero-growth-at-the-sovereign band and 8.6x its
  bottom; it is 7.5x the top of the floor band and 16x its bottom.**

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].** *(Corrected 2026-09-03, found by the
HHH run — this block still carried v4.0's "THERE IS NO HURDLE" heading, the SEVENTH
surviving home of the rule the framework rewrote on 2026-08-28. The floor section above at
[E4-28] already governs; this block is the ranking that applies only to what clears it.)*
- **FLOOR VERDICT FIRST. Honest pre-tax expectancy = owner-earnings yield + sustainable
  growth.** At a generous **6.5%** perpetual-equivalent growth judgment — above the long-run
  nominal growth of the end market, and above what the [E4-44] decomposition supports once
  the margin lever is spent — expectancy is:

  | construction | yield | + growth | **expectancy** |
  |---|---|---|---|
  | 18-yr window | 0.61% | 6.5% | **7.1%** |
  | judged 8-yr | 1.07% | 6.5% | **7.6%** |
  | 3-yr window | 1.34% | 6.5% | **7.8%** |
  | **best year ever filed, most generous construction available** | 1.44% | 6.5% | **7.9%** |
  | *best year ever + a generous 8% growth* | 1.44% | 8.0% | *9.4%* |

  **Every construction, including one built to flatter, sits BELOW the ~10% floor. Even
  granting the best year KLA has ever filed AND 8% perpetual growth, the expectancy does not
  reach it.** *"that's the figure we quit on … that's true whether short rates are 6 percent
  or whether short rates are 1 percent"* **[E4-28]**.
- **→ THE NAME IS NOT RANKED. It is QUIT ON.** Per the template, the ranking lines below the
  floor are not filled in: there is no ranking position, and no comparison against the
  opportunity set is owed for a candidate that does not reach the floor.
- points over sovereign, recorded anyway for the register: **−4.17** (band −4.63 to −3.80).

**WHICH BAR** *(one only)*
- [x] **SCREAMER TEST [E4-01, E4-25]** — take the conservative end and ask whether the price
      already clears it. **No margin is added on top; "startlingly low" is what you observe,
      not what you subtract.** Conservative case **~$22/share**; price **$185.60**.
      **OUTCOME THREE: the price is above the whole range. NO.**
      *(Bar 1 is not used and no end margin is applied — using both on the same number is
      forbidden, and Bar 2 is the honest bar when the answer is not close.)*
- **WINDAGE COUNT: ONE.** Conservatism is spent once, at the **[E4-41] normalization** of the
  level from the 5-year default to the 8-year window. Realistic inputs everywhere else; no
  risk premium in the rate [E3-42]; no end margin [E4-48]. **And the windage does no work:
  the verdict is identical at every point in a 2.29x band, including at the most generous
  construction available.** That is why this file is not a close call and why no
  degree-of-difficulty credit [E4-18] was needed to reach it.

- **VERDICT: [x] UNKNOWABLE is NOT used and [x] IN is NOT reached — the name FAILS at Q5, on
  price, at the [E4-28] floor. Ranking position: NONE — quit on, not ranked.**
  *This is a verdict about the price on 2026-09-04, not about the business. Q1–Q4 all
  returned IN and Q4 returned GREAT.*

## Q6 — NOT OPENED. No entry; no position exists.

Q6 governs a holding. There is none and none is created. What follows is the **pre-committed
re-look, written in advance per [E1-02]** — *"I believe in establishing yardsticks prior to
the act"* — so that a future run cannot rationalise its way back in.

**THE PRICE RE-LOOK.** **~$38/share judged, zero growth at a 5.24% sovereign, recomputed at
the rate of the day. The [E4-28] floor clears near ~$20/share (~$25 generous) — an 87–89%
decline.** **So the file is FAR likelier to re-open on earnings than on price**, and the
earnings condition is stated as a number: at $185.60 the floor needs **~$24.2bn of owner
earnings** against $2.6bn judged — a **9.3x** gap.

**THESIS-CONFIRMING METRIC (both halves, two consecutive fiscal years, because either alone
is gameable):** **Semiconductor Process Control segment gross margin back above 65.0%**
(its FY2022 level) **WHILE** segment revenue also grows. That is the [E2-44] pricing test and
the [E4-32] direction test in one line, run on the only instrument this filer files.

**BULL BREAKERS — pre-registered so they cannot be rationalised away later:**
- **SPC segment gross margin below 62.0%** in any year — a further point of the drift already
  recorded, and the single most informative number in the filing.
- **Service revenue declining year on year for the first time in the filed record**, or
  service falling below 21% of revenue — the annuity failing the test it passed in FY2024.
- **[E2-49] withdrawal of any of three disclosures**: the segment cost-of-revenues split
  (which is what makes the segment gross margin computable at all), the product/service
  revenue split, or the China revenue percentage. Any of the three would remove the
  instrument this file was decided on, and a yardstick disposed of after deterioration is
  itself the finding.
- **R&D below 10.5% of revenue** — the moat-defence spend has already fallen 15.6% → 11.3%;
  a further fall while revenue grows is under-investment, not leverage.
- **A second customer above 10%, or TSMC above 25%** — concentration compounding.
- **Any acquisition above ~$1bn**, given the Orbotech record: 41% of that goodwill impaired,
  the synergy language dropped, and no post-mortem ever filed.
- **Buybacks above ~$2.5bn/yr at these prices**, or any *debt-funded* buyback — the FY2022
  pattern repeating.

**BEAR BREAKERS — the facts that would make me wrong in the other direction:**
- **KLA filing a physical/unit series or an installed-base count for the first time**, which
  would close the [E4-55] blind spot that caps this file's Q2 at NARROW.
- **Any disclosure of service gross profit or cost of service** — it would make the
  franchise-inside-the-franchise measurable for the first time.
- **A Chinese process-control competitor named by KLA or by Nova with a quantified share**,
  which would move the China mechanism from exposure to experience.
- **Hitachi High-Tech or Lasertec becoming SEC registrants**, closing the two unpriced cells
  in the competitor row.

**THE MONITORING QUESTION [E3-30], stated now so the answer is not invented later:** *is the
core segment's 1.58-point gross-margin drift an aberrational cycle effect — mix toward China
legacy nodes and toward the newly-scaled advanced-packaging line — or has the business
slipped in a way that permanently reduces intrinsic value?* **On the evidence today it reads
as the former. Two more years of the same reading reverses that**, and [E4-17] is explicit
that such beliefs *"change quite gradually"* — while [E2-40] is equally explicit that once a
view **has** crystallized, delay is the graver error.

**Catalysts:** the **FY2026 DEF 14A**, due late September 2026 (KLA files 2023-09-21,
2024-09-24, 2025-09-23) — the first proxy on post-split figures and the first to score the
FY2026 pay outcome; **FY2027 Q1 earnings, late October 2026** (guided to $4.0bn ±$200M
revenue, the first quarter above a $16bn annual run-rate); and the **FY2027 10-K, August
2027** — the first full year that will say whether the AI capex level held.

**Position size: ZERO.** No position is taken. Had one been contemplated it would have been
**sized DOWN** in any case, because the **[E5-08](2) capital-allocation flag is live** and
[E4-13] binds it to position size and to nothing else.

- **VERDICT: NOT OPENED — no holding exists.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN → Q2 IN → Q3 IN → Q4 IN → Q5
      FAIL on price. Q6 not opened because no position exists.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q2's class is
      **NARROW**, not PROVISIONAL: the two unpriced competitors (Hitachi High-Tech, Lasertec)
      are **non-registrants**, and under the ACLS adjudication an *additional* competitor can
      only narrow a moat, never widen one — so the gap caps the class rather than suspending
      it, and it is carried as a Q6 work-order.
- [x] Every UNRESEARCHED verdict names its artifact. **Three items are marked UNRESEARCHED and
      none of them is load-bearing:** the guidance *assumptions* (IR "Letter to Shareholders"
      at ir.kla.com, expressly not incorporated by reference — off the filing rung); the
      pre-FY2016 dividend streak (10-K FY2014/FY2015 dividend notes); the cause of director
      Calderoni's 8.5% against-vote.
- [x] Every absence claim names its sweep, per the **absence-claim rule**, and is worded "no
      instance found": service gross profit (6 vintages) · physical/unit series (6 vintages) ·
      ASP or price range (6 vintages) · process-control market share (KLA + 7 peer filings) ·
      EBITDA (3 vintages) · Orbotech post-mortem (6 vintages).
- [x] Step 0: the filing was read; **accession `0000319201-26-000027`**; four cash-flow lines
      cross-checked to the filed statement; the segment gross-profit figure cross-checked
      **across two vintages to the dollar** ($5,629,302 on $8,733,556 in both the FY2024 and
      FY2026 10-Ks).
- [x] Owner earnings on a multi-year mean; **eight windows published [E4-38]**; the capex band
      disclosed as a judgment, with the **D&A end ruled INVALID for this filer** and the
      reason given in dollars.
- [x] Competitor row filled: **8 companies, 7 with filed same-formula figures**, two named
      non-registrants recorded with the rung and the obstacle.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury),
      dated 2026-09-04, struck fresh this run.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen (Bar 2, the screamer test); **windage count ONE**, stated and located.
- [x] Prices dated; the aggregator quote flagged as a live quote only.
- [x] Run committed to git after every question under the write-early protocol.
- [x] **Operator rule 9 discharged:** the disconfirming evidence was hunted hardest against my
      own expected conclusion. The brief expected Q1–Q4 IN and a Q5 fail; that is what
      happened, which is the outcome most at risk of confirmation bias, so the two facts that
      most threatened it — **KLA's own 8-to-15-year growth record exceeding the rate the floor
      demands**, and **the FY2024 segment-margin rise through a revenue decline** — were given
      their strongest form and answered rather than omitted.

## REGISTER
- **Verdict: [x] OUT ON PRICE at Q5** — about the price, not the business. Not UNRESEARCHED
  (no named document would change it) and not UNKNOWABLE (the evidence is in).
- **One line:** *The best business this queue has run, at a price that pays a third of what a
  Treasury bond pays.*
- **If UNRESEARCHED — the work order:** n/a to the verdict. The three non-load-bearing items
  are listed in the self-audit with their locations.
- **If UNKNOWABLE:** n/a to the verdict. **Two things are genuinely unknowable from the
  filing rung and are recorded as moat defects rather than as verdicts:** the **profitability
  of the service annuity** (no cost-of-service line exists in any vintage; Note 17 cannot be
  reworked because *"Services are offered in multiple segments"*) and **KLA's process-control
  market share** (no SEC filing in the industry states one; the resolving document is a paid
  Gartner/TechInsights/VLSI report, which is **off this framework's evidence ladder**).

---
# THE TWO REQUIRED OUTPUTS (queue contract)

## 1. THE PRICE
**Current price $185.60** (2026-09-04 close, aggregator, flagged as a live quote only) on
**1,306,546,783 shares** hand-read off the FY2026 10-K cover = **market cap $242,495M**.

**Value, zero growth against the 5.24% US Treasury 30-year, as a round-number range [E4-01]:**

> ### conservative ~$22 · **judged ~$38** · optimistic ~$50 per share
> ### at the [E4-28] 10% floor: ~$11 to ~$25, **judged ~$20**

**The price is 3.9x the top of the entire zero-growth band and 7.5x the top of the floor band.**
Owner-earnings yield **1.07%** (band 0.61%–1.44%) against a **5.24%** sovereign; **−4.17 points
over the bond**. Growth required to clear the floor: **+8.93%/yr perpetual**.

## 2. PASS / FAIL

# ❌ FAIL — at Q5, ON PRICE, at the [E4-28] floor.
### Q1 IN · Q2 IN (NARROW) · Q3 IN (overlay, one capital-allocation flag) · Q4 IN (GREAT) · **Q5 FAIL** · Q6 not opened.

**All four business gates returned IN — the sixteenth name in this queue to do so, and on the
[E2-43] and [E2-44] evidence the best business it has run.** The file closes on price alone:
at 1.07% against a 5.24% bond, KLA pays roughly one-fifth of what a Treasury pays, on every
window and both capex ends, including the best single year it has ever filed. It is **quit on
under [E4-28], not ranked** — there is no ranking position.
