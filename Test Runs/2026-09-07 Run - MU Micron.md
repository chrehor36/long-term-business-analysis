# Company Run — Micron Technology, Inc. (MU) — 2026-09-07
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Research artifacts: `Test Runs/_research 2026-09-07 MU/`

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

---
# STAGE 0 — MU WAS RETURNED UNPRICED. WHAT ACTUALLY HAPPENED.

The queue's tail triage (`Screens/WATCHLIST RUN QUEUE.md`, line 86) lists MU as **UNPRICED on
perimeter/staleness grounds — "re-check before running."** Three things were to be established
before anything else. All three were, and one of them is the whole run.

### (a) The cover share count, by hand
Read off the cover of the most recent filed document, not from a screen:

| source | date | shares |
|---|---|---|
| **10-Q, Q3 FY2026 cover** (`mu-20260528.htm`, acc. 0000723125-26-000015) | 2026-06-17 | **1,129,393,151** |
| Balance sheet, same filing, as of 2026-05-28 | — | 1,275M issued / **1,129M outstanding**, 146M treasury |
| 10-K FY2025 cover (acc. 0000723125-25-000028) | 2025-09-26 | 1,122,466,035 |

The two independent counts in the same filing agree. **No share-class artifact, no Up-C
structure, no stale dei element.** The count is clean; the count was never the problem.

- **Market cap = 1,129,393,151 × $1,016.59 = $1,148,130M ≈ $1.148 trillion.**
  Price $1,016.59, close of **2026-09-04**, Yahoo chart endpoint — *aggregator, live quote only,
  flagged per operator rule 5.*

### (b) Did a perimeter guard fire, and why?
**No perimeter guard fired. The pricing tool crashed.** Re-run today,
`python tools/screen.py MU` returns cleanly: cap $1,143.7B, 3-year yield band −0.20%..+0.04%,
0 refused. The `2026-09-01 WATCHLIST TRIAGE.csv` row for MU is:

    MU,Semiconductors & Relat,1049376,-3147,-0.003,-0.0548,0.103,,False,False,False

— `oe_bottom` −$3,147M, `yield_bottom` −0.3%, `growth_required` 10.3%, and **`spread` empty**.
A band with no top is not a price, which is why the triage wrote UNPRICED. The proximate cause
is a genuine tool defect, reproduced today: `tools/screen.py` raises
`ZeroDivisionError` at `run.py:126` (`(r - tgr)` → 0) inside `points_over` on names where the
bisection walks the terminal growth rate into the sovereign. It fires on **INTC as well as MU**
— i.e. on the two names in this tier whose owner earnings are near or below zero. This is a
**defect note, not a finding about Micron**: a tool is forbidden to conclude (operator rule 8),
and it did not; it failed loudly and the file was held back. That was the correct outcome.

### (c) Do the owner-earnings history and the current cap describe the same company?
**No. They describe two different companies, and the gap is the largest in this queue.**

| | filed annual history (FY2025 10-K) | the last three filed quarters (10-Q, 9M to 2026-05-28) |
|---|---|---|
| Revenue | $37,378M (FY2025, full year) | **$78,959M in nine months**; **$41,456M in Q3 alone** |
| Gross margin | 40% (FY2025); **−9% (FY2023)** | **85% in Q3 FY2026**; 77% for the nine months |
| Net income | $8,539M (FY2025); **−$5,833M (FY2023)** | **$47,268M in nine months**; $28,243M in Q3 alone |
| Operating cash flow | $17,525M | **$45,702M in nine months** |
| Equity | $54,165M at 2025-08-28 | **$100,724M at 2026-05-28** |

The most recent **annual** filing is the FY2025 10-K, period ended **2025-08-28**, filed
2025-10-03 — **twelve months stale**. FY2026 ends 2026-09-03; that 10-K does not exist yet.
So the staleness flag was real and it was material: every owner-earnings window this framework
builds ends in a year in which Micron earned $8.5bn, and the market is pricing a company that
earned $47.3bn in nine months.

**But note carefully which way that cuts.** The Q3 FY2026 income statement shows revenue up
4.5x year-on-year while **cost of goods sold barely moved** ($6,400M vs $5,793M). Nothing about
the plant changed. The entire move is price. Micron's own MD&A quantifies it:

> "Sales of DRAM products increased 343%, primarily due to a **low-260% range increase in
> average selling prices** and a low-20% range increase in bit shipments."
> — Q3 FY2026 10-Q, nine-month comparison

**The staleness is not a reason the history understates the business. It is the [E2-58] cycle
happening in real time, at its tightest point on record.** Stage 0's job was to find out
whether the history and the cap describe the same company. They do not — and the reason they
do not is the finding this run is about.

**Stage 0 verdict: proceed.** Count clean, no guard, staleness real and characterised.

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- rate **5.24%** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-year,
  from the issuing authority** (`python tools/sources.py`, per CLAUDE.md "issuing authority
  first"; FRED is the fallback and was not used).
- Earnings currency: **USD.** The 10-K states it directly — *"The functional currency for all of
  our operations is the U.S. dollar. The substantial majority of our sales are transacted in the
  U.S. dollar."* No FX step, no ADR ratio.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **Primary document: 10-K FY2025, period ended 2025-08-28, filed 2025-10-03, accession
  0000723125-25-000028** (`mu-20250828.htm`).
- **Also read: 10-Q Q3 FY2026, period ended 2026-05-28, filed 2026-06-25, accession
  0000723125-26-000015.** Required, not optional: the annual filing is twelve months stale and
  Stage 0(c) shows the interim period is a different company.
- **Also read for the cycle:** 10-K FY2022 (acc. 0000723125-22-000048), 10-K FY2019
  (acc. 0000723125-19-000094), 10-K FY2016 (acc. 0000723125-16-000269) — needed because the
  cash-flow **detail lines** below the standard capex tag are not in XBRL for the older years.
- **Figures cross-checked against the filed statements:**
  1. FY2025 operating cash flow **$17,525M** — XBRL `NetCashProvidedByUsedInOperatingActivities`
     against the filed Consolidated Statements of Cash Flows. Agrees.
  2. **Balance sheet recomputed A−L per [E5-32]** (audited does not mean true): total assets
     $134,112M − total liabilities $33,388M = **$100,724M**, equals filed total equity. Agrees.

### THE INTC FINDING, RE-RUN ON MICRON — and it reverses
The INTC run of 2026-09-07 found that the standard capex tag can miss a fifth of a fab
company's spending because PP&E additions appear in **financing**. That check was run here line
by line on nine years of filed cash-flow statements. **Micron has the same line, and it is
small — but Micron has a much larger line running the OTHER way, which no screen catches.**

| FY | investing: "Expenditures for PP&E" | financing: "Payments on equipment purchase contracts" | investing: **"Proceeds from government incentives"** |
|---|---|---|---|
| 2016 | 5,817 | — | — |
| 2017 | 4,734 | **519** | 21 |
| 2018 | 8,879 | 206 | 355 |
| 2019 | 9,780 | 75 | 748 |
| 2020 | 8,223 | 63 | 262 |
| 2021 | 10,030 | 295 | 495 |
| 2022 | 12,067 | 141 | 115 |
| 2023 | 7,676 | 138 | 710 |
| 2024 | 8,386 | 149 | 315 |
| 2025 | 15,857 | — | **2,005** |
| **10y total** | **91,449** | **1,586** | **5,026** |

- **Capex hidden in financing: $1,586M over ten years, 1.7% of the investing line.** Real, added
  to (c) below, and **an order of magnitude smaller than at Intel.** The finding generalised as a
  *class of check*, not as a magnitude — which is the correct way for a queue-wide ruling to
  travel.
- **Two further off-line-item forms, both read from the filings and both disclosed:**
  - *"Non-cash equipment acquisitions on contracts payable"* — $321M (FY2025), $118M, $165M,
    $157M, $289M, $171M. Equipment received and not yet paid; it lands in a later year's line.
  - FY2014–FY2016 financing carries *"Proceeds from equipment sale-leaseback transactions"* of
    $14M / $291M / $765M — an equipment **inflow** in financing. Same class of leak, opposite
    sign, and it flatters the mid-2010s.
- **The larger item runs the other way: $5,026M of government incentives sits inside INVESTING
  as a positive**, offsetting capex, and it is **not** in the `PaymentsToAcquirePropertyPlantAndEquipment`
  tag. In FY2025 alone it is **$2,005M = 12.6% of gross capex.** This is the TXN CHIPS-Act check,
  and the accounting policy note tells you it hits (c) twice:

  > "Incentives related to the acquisition or construction of property, plant, and equipment are
  > recognized as a **reduction in the carrying amounts of the related assets and as a reduction
  > of subsequent depreciation expense** over the useful lives of the assets."
  > — FY2025 10-K, Note 1

  So government money reduces cash capex now **and** suppresses reported D&A later. Both ends of
  the owner-earnings band are affected, in opposite directions. It is carried below as a
  **disclosed third construction**, never silently netted.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics, in my own words, without management's language.** Micron builds enormous
factories that etch identical bits of memory onto silicon wafers, and sells those bits by the
gigabyte at whatever price the world's supply and demand set that quarter. Revenue is bits
shipped times price per bit. Cost is the fab: depreciation, the wafer, the power, and the
people. Every eighteen months or so a new process node arrives that puts more bits on the same
wafer, so cost per bit falls — and because all three surviving producers get the same node from
the same equipment vendors at roughly the same time, price per bit falls with it. Micron makes
money in the years when the industry cannot make enough bits, and loses money in the years when
it can. **Nothing about the product is Micron's.** A DDR5 part is built to a JEDEC specification
so that a customer can put Samsung's, SK hynix's or Micron's part in the same socket. That is
the definition of the product, written by a standards body, on purpose.

**The scarce input this business controls.** Honestly stated: **none that is durable.** What is
scarce is *installed leading-edge wafer capacity at this instant*, and Micron owns roughly a
fifth of it. But capacity is not controlled — it is bought, from ASML and Applied Materials and
Lam and Tokyo Electron, by anyone with the money, and Micron's own risk factor says so. The
nearest thing to a controlled scarce input is the **capital and the decade of process learning
required to be a fourth entrant**, which is why there are three and not thirty. That is a real
barrier to *entry*. It is not a barrier to *competition* among the three, and the difference
between those two is the whole of this run.

**Will the fundamentals look broadly the same in ten years?** The *economics* will: bits get
cheaper, fabs get more expensive, and the cycle turns. The *level* will not, and neither will
the product. Micron has been through this at least six times since 1996.

**VERDICT: [x] IN.** The business is genuinely simple — simpler than most names in this queue.
It is a price-taker with a cost curve. I understand exactly how it makes money and exactly how
it loses it. Q1 is not where a commodity fails; Q1 asks whether I can see the machinery, and I
can.

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

- **Needed or desired** [x] — yes, and overwhelmingly so right now.
- **No close substitute** [ ] — **FAILS, and it fails by construction.** A DDR5 module is built to a
  JEDEC standard so that Samsung's, SK hynix's and Micron's parts are interchangeable in the same
  socket. The substitute is not close; it is *identical by specification*, which is the point of
  the specification. Micron's own 10-K concedes the consequence in the plainest possible terms:

  > "In some prior periods, **average selling prices for our products have been below our
  > manufacturing costs** and we may experience such circumstances in the future."
  > — FY2025 10-K and Q3 FY2026 10-Q, Risk Factors

  A product with no close substitute does not sell below its cost of manufacture. This one has,
  and the company says it will again.
- **Not price-regulated** [x] — true, and in this class that is a liability rather than an asset.
  **[E2-59]** is explicit: administered pricing *floors* a commodity business and *caps* a
  franchise; **neither creates the class.**

### The commodity doctrine, [E2-58], applied — and Micron's filing writes the equation itself
The corpus's equation is *"persistent over-capacity without administered prices (or costs) equals
poor profitability"*, with long-term profitability set by *"the ratio of supply-tight to
supply-ample years"*, and prosperity breeding the next glut — *"nothing fails like success."*
**Micron files that sentence as a risk factor, in its own words, in the middle of the best quarter
in its history:**

> "**We intend to advance our process technology to increase bit output per wafer, improve yields,
> and increase wafer supply. In addition, our competitors may increase capital expenditures
> resulting in future increases in worldwide supply. We, and some of our competitors, have plans
> to construct new fabrication facilities and/or ramp production at existing fabrication
> facilities. Increases in worldwide supply of semiconductor memory and storage, if not
> accompanied by commensurate increases in demand, could lead to declines in average selling
> prices.**" — FY2025 10-K and Q3 FY2026 10-Q, Risk Factors

That is **[E2-27]** verbatim in a company's own filing: *"Viewed individually, each company's
capital investment decision appeared cost-effective and rational; viewed collectively, the
decisions neutralized each other and were irrational."* And Micron is currently executing its half
of it: four new fabs (two in Boise, two in Clay, New York), a Singapore HBM advanced-packaging
plant plus **an additional Singapore wafer fab broken ground in January 2026**, Hiroshima EUV
modernisation, Taiwan expansion, and a **$1.8bn cash acquisition of Powerchip's Tongluo fab
completed March 2026**.

### **[E2-44]**, BOTH HALVES, RUN AGAINST THE LAST DOWN-CYCLE. THIS IS THE DECIDING TEST.
The ACLS precedent asks the one question a no-moat supplier cannot pass: **did filed price and
margin hold through a revenue collapse?** ACLS's filed system-price range *rose* ($2.4-10.0M to
$2.6-12.0M) and gross margin *rose* (43.7% to 44.9%) while revenue fell 26%. That is what a Q2 IN
looks like on this test.

**Micron's answer, from the FY2023 10-K (accession 0000723125-23-000054), is the opposite on every
line:**

| FY2023 vs FY2022 | filed |
|---|---|
| DRAM revenue | **−51%**, on *"a high-40s percent range decline in average selling prices"* and bit shipments down only *"high-single-digit percent"* |
| NAND revenue | **−46%**, on *"a low-50s percent range decline in average selling prices"* — **with bit shipments UP "high-single-digit percent"** |
| Consolidated gross margin | **45% to negative 9%** |
| Inventory written down to NRV | **$1,831M**, *"as a result of declines in average selling prices for both DRAM and NAND"* |
| Fab underutilisation period costs | **$382M** (*"a portion of our facilities were underutilized for 2023"*) |
| Goodwill | **$101M impairment**, all of the Storage unit's |

**[E2-44] characteristic (1)** asks whether it can raise price *"even when product demand is flat
and capacity is not fully utilized."* Micron's DRAM volume fell by high single digits — near flat —
and price fell by nearly half. In NAND, **volume actually grew and price still fell by more than
half.** The answer is not "narrowly, no." The answer is that price is set entirely outside the
company. **[E4-37]**'s inverse metric — the agony of a price increase — does not even apply here:
there is no price decision to agonise over.

**[E2-44] characteristic (2)** asks whether dollar volume grows *"with only minor additional
investment of capital."* Over FY2016-FY2025 Micron spent **$93,035M** of total capital expenditure
and charged **$59,892M** of depreciation to move revenue from $12,399M to $37,378M. The capital is
the business.

### **[E4-55]** — where units exist, monitor units. The physical series is the honest one.
Micron publishes bit shipments and ASP as directional percentages. **Recorded sweep** of the
FY2016, FY2019, FY2022, FY2023 and FY2025 10-Ks and the Q3 FY2026 10-Q for an absolute bit count:
**no instance found**, so the percentage series *is* the physical record. Splitting the current
boom into its two components is decisive:

| period, filed | DRAM ASP | DRAM bits | NAND ASP | NAND bits |
|---|---|---|---|---|
| FY2023 (the trough) | **−high-40s%** | −high-single-digit% | **−low-50s%** | +high-single-digit% |
| FY2024 | +low-teens% | +mid-40s% | +low-30s% | +low-30s% |
| FY2025 | +low-40s% | +mid-teens% | (declines in some segments) | +high-teens% |
| **9M FY2026 vs 9M FY2025** | **+low-260% range** | **+low-20% range** | **+mid-310%** | +low-double-digit% |
| 9M FY2026, company's own summary | **~+140%** (approx., stated) | ~+30% | ~+130% | +low-20% |

**The plant produced roughly a fifth to a third more bits, and the price went up by a multiple.**
Q3 FY2026 cost of goods sold was **$6,400M against $5,793M a year earlier** — a 10% rise — while
revenue went from $9,301M to **$41,456M**. Nothing about Micron changed. The world's willingness to
pay changed. **[E4-36]**'s fourth cause of extreme success is wave-riding, and **[E3-51]** names
it: *"when a surfer gets up and catches the wave… he can go a long, long time. But if he gets off
the wave, he becomes mired in shallows."* **A surfing run is not a moat; the advantage lives in the
wave, not the surfer.**

### **[E4-04]** — must the moat be continuously rebuilt?
Yes, and Micron's filing says so in the same shape the INTC run found at Intel. Micron's gross
margin is stated to depend on *"continuing decreases in per gigabit manufacturing costs, which is
primarily achieved through improvements in our manufacturing processes and product designs"*, with
the named failure mode *"insufficient volume to run new technology nodes to achieve cost
optimization."* The framework's own scoping test — *does the spending defend the same advantage, or
buy its replacement?* — answers itself: **1α → 1β → 1γ (first EUV node, FY2025) → HBM3E 8-high →
12-high → HBM4.** Each node's advantage expires when the next arrives, at all three producers, from
the same equipment vendors. This is the excluded class. Unlike Intel, Micron has been *winning* its
recent node races — which changes the standing, not the class. **A better position on the wave is
not a different kind of moat.**

### THE COMPETITOR ROW — required **[E3-28]**. Same metric, same window, filing-sourced.
**Metric: consolidated gross margin from the filed income statement, at the FY2023-24 industry
trough and at the latest filed year.** Gross margin is the right metric here because the question
is whether price holds when volume leaves, and gross margin is where that shows.

| Company | GM, **trough year** | GM, latest filed FY | latest revenue | source |
|---|---|---|---|---|
| **MICRON (MU)** | **−9.1%** (FY2023) | 39.8% (FY2025) · **85% Q3 FY2026** | $37,378M FY25 | 10-K acc. 0000723125-23-000054 / -25-000028; 10-Q -26-000015 |
| Sandisk (SNDK) — NAND | **7.1%** (FY2023) | 71.5% (FY2026) | $20,248M | 10-K, CIK 2023554 |
| Western Digital (WDC) — HDD | 15.3% (FY2023) | 48.9% (FY2026) | $12,919M | 10-K, CIK 106040 |
| Seagate (STX) — HDD | 18.3% (FY2023) | 45.6% (FY2026) | $12,195M | 10-K, CIK 1137789 |
| Silicon Motion (SIMO) — fabless NAND controllers | **42.3%** (FY2023) | 48.3% (FY2025) | $886M | 20-F, CIK 1329394 |
| Intel (INTC) | 40.0% (FY2023) | 34.8% (FY2025) | — | INTC run, 2026-09-07 |
| Texas Instruments (TXN) | 68.8% (FY2023) | 57.0% (FY2025) | — | TXN run, 2026-09-06 |
| NVIDIA (NVDA) | 56.9% (FY2023) | 71.1% (FY2026) | $215,938M | 10-K, CIK 1045810 |
| **Samsung Electronics** — the #1 DRAM producer | **UNKNOWABLE at the filing rung** | | | CIK 879316: last filing 2015; only SC 13D/G, SUPPL, ARS; **no 10-K or 20-F ever**; companyfacts **404**; reports under the Rule 12g3-2(b) exemption |
| **SK hynix** — the #2 DRAM producer, HBM leader | **UNKNOWABLE at the filing rung** | | | CIK 2120882: US-listed July 2026 via F-1; **no 20-F yet due**; 19 furnished 6-Ks are event disclosures only; companyfacts carries **5 fee-table facts and zero financial statements** |

- **Peers named: 8 of the industry's ~10 real competitors** (three memory/storage direct, one HDD
  second, one fabless controller peer, three broad semiconductor comparators from completed runs on
  identical formulas). Two are missing.
- **The two missing are not a defect in this verdict, and the reason is the queue's standing
  adjudication:** the missing names are **additional competitors**, and adding a competitor cannot
  widen a moat. The row is sufficient to **refuse** an IN; it would not be sufficient to grant one.
  (One fact IS available at the SEC rung: SK hynix furnished a 6-K on 2026-08-19 approving a
  **₩40.0 trillion (~$29bn) treasury-share buyback**, and reported total equity of **₩120.7
  trillion at 2025-12-31** — evidence of a competitor as flush as Micron is, which is a prompt about
  the next capex round, not a comfort.)
- **What the row says, and it is the finding.** In the trough, **Micron had the worst gross margin
  of every company in the row, and it was the only negative one.** Not narrower — negative. And a
  **fabless controller designer with no fabs, no scale and one-fortieth of Micron's revenue held
  42.3%** through the same collapse. Then in the recovery all four memory and storage names moved
  together — MU 85%, SNDK 71.5%, WDC 48.9%, STX 45.6% — **from four different products, four
  different fiscal calendars and four different balance sheets.** Margins that collapse together and
  recover together are not evidence of four separate moats. They are one wave, measured four times.
- **[E3-61]'s limit stated:** the row shows position, not conduct. Whether the three producers hold
  discipline through the next build is *"you'd have to know the people involved"* — and the corpus
  says even Munger had no model for predicting it.

### Untapped pricing power **[E3-33]**, scoped by **[E5-28]**
Claiming this class means claiming *"a monopoly or a near monopoly."* Micron is one of three in
DRAM and one of five-plus in NAND, and the row above shows it as the **weakest** of the memory
names on trough margin. There is no untapped pricing power to find: Micron takes every dollar the
market offers each quarter, and the last three quarters prove it takes every dollar on the way up
as completely as it surrendered every dollar on the way down. **Not this class.**

### THE BEST FORM OF THE OPPOSING CASE — **[E4-51]** requires it stated better than its holders would
**The bull case is not "AI demand is strong." It is a structural claim, it is filed, and it is the
strongest case any commodity producer in this queue has offered.** From the Q3 FY2026 10-Q:

> "We recently executed certain strategic customer agreements… These agreements are structured as
> **take-or-pay agreements, with binding commitments for specific volumes over the multi-year
> contract terms** and include contractually enforceable volumes. **Pricing for most agreements is
> either fixed, or is subject to minimum and maximum pricing.** The largest agreements generally
> have a ceiling price for existing products that approximates the market price in the second
> calendar quarter of 2026, and **a floor price through the term of the agreement.**"

> "We expect gross margins from our strategic customer agreements with price bands, **even at floor
> pricing levels, to yield gross margins well above our peak quarterly margins in any past
> cycle.** Accordingly, we believe these agreements accelerate the transformation of our business
> model and will **significantly enhance the durability and predictability of our financial
> performance.**"

Stated at full strength: *if* multi-year take-or-pay contracts with contractual floors above any
previous peak margin come to cover a growing share of output, then the thing that made memory a
commodity — that price is renegotiated against spot every quarter — has been contractually removed
for that share, and the ratio of supply-tight to supply-ample years stops governing. **That is a
real argument and it deserves a real answer.** Four filed facts give it one:

1. **The corpus has already ruled on exactly this structure, and the ruling is [E2-59].** A
   contractual price floor is **administered pricing**. Administered pricing let pre-1970s insurers
   *"legally price their way to profitability even in the face of substantial over-capacity"* — and
   **the moat belongs to the regime, not to the company**, with *"That day is gone"* as how it ends.
   A take-or-pay contract with a floor is a regime with a term and a counterparty. Micron did not
   acquire a franchise; it sold forward part of a shortage.
2. **The filing sizes it, and it is 0.44% of the market capitalisation.** *"As of May 28, 2026, the
   transaction price allocated to our remaining performance obligations was **approximately $5
   billion**, of which $422 million has been recognized as contract liabilities. As of August 28,
   2025, our remaining performance obligations were **not material**."* **$5bn against a single
   quarter's revenue of $41.5bn and a $1,148bn market cap** — about six weeks of current sales. The
   structural claim, measured at the filing rung on the last filed date, is a rounding error on the
   price.
3. **The ceiling is filed too, and it binds the upside.** *"The largest agreements generally have a
   **ceiling price** for existing products that approximates **the market price in the second
   calendar quarter of 2026**"* — i.e. capped at approximately the 85%-gross-margin quarter. Per
   **[E2-63]**, a verdict must name what bounds the upside: **Micron's own contracts do.** The same
   instrument that floors the downside caps the top at today's spot.
4. **The rest of the same filing contradicts the durability claim.** The FY2025 10-K, ten months
   older: *"Due to volatile industry conditions, our customers are **generally reluctant to enter
   into long-term, fixed-price purchase contracts.** We typically enter into long-term agreements…
   **with acknowledgment that pricing, quantity, and other terms will be periodically negotiated to
   reflect market conditions**"*, and in the revenue note, *"**Substantially all contracts with our
   customers are short-term in duration at fixed, negotiated prices.**"* Both sentences still stand
   in the current 10-Q's business description.

**And the framework's own evidentiary rule closes it.** The durability claim is a **forward-looking
management expectation**, one quarter old, in an unaudited interim filing, about contracts signed
*"in the third and fourth quarters of"* fiscal 2026 — some *"subsequent to May 28, 2026"* and
therefore not in any financial statement at all. **"A gate marked IN carrying 'unverified' or
'provisional' is a protocol violation."** Ask the separating test aloud: *can I name the document
that would resolve this?* **The document would be a 10-K covering a memory down-cycle in which
contracted HBM was a material share of revenue. No such document exists, and none can until the
cycle turns.** That makes the HBM structural claim **UNKNOWABLE**, not UNRESEARCHED — and an
UNKNOWABLE cannot rescue an OUT already carried by filed evidence about the whole business.

*(The prior I was most likely wrong about, tested and reported honestly per **[E4-26]**: I expected
the HBM argument to be rhetoric and it is not — it is a filed, quantified, contractual change in
how a share of this revenue is priced, and it is the best case in the queue. It failed on **size**
and on the corpus's **[E2-59]** ruling, not on being unserious. If a future down-cycle 10-K shows
contracted volumes holding a floor margin above prior peaks, this class of argument must be
re-adjudicated on evidence rather than dismissed. That document is the work order this file leaves
behind, and it cannot be executed today.)*

### Class and direction
- **Class: [ ] WIDE  [ ] NARROW  [x] NONE  [ ] PROVISIONAL**
- **Direction:** widening *right now* on standing (Micron won the 1γ EUV node and HBM3E 12-high) —
  and that is a **surfing position, not a moat direction under [E4-32]**. The wave is [E4-36]'s
  fourth cause, and the corpus says it is the one cause that is not ownable.
- **Key-person dependence [E4-23]:** none material found. Recorded as absent, not as a strength.

### **VERDICT: [x] OUT** — permanent, and the file closes here.
Six independent grounds, each filing-sourced, any two of which would be sufficient:
1. **[E3-03](2)** — the product is defined by a standards body so that competitors' parts are
   substitutes. Micron's own filing: ASPs *"have been below our manufacturing costs."*
2. **[E2-58]** — the commodity equation, with the next glut's mechanism written by Micron as a risk
   factor while it builds six fabs.
3. **[E2-44]**, both halves, failed on the filed record: FY2023 DRAM price −high-40s% on near-flat
   volume; NAND price −low-50s% with volume **up**.
4. **The competitor row:** Micron had the worst — and the only negative — trough gross margin in a
   row of eight, and a fabless controller company with no fabs held 42.3% through the same collapse.
   All four memory/storage names then recovered together, which is one wave measured four times.
5. **[E4-04]** — the moat's basis must be replaced every node, at rising cost, by the company's own
   account of what drives its gross margin.
6. **[E2-59]** — the take-or-pay floors are administered pricing; the moat belongs to the regime, is
   filed at $5bn of remaining performance obligations, and carries a ceiling at today's spot.

**Q1 IN → Q2 OUT.** ⛔ **Q3, Q4, Q5 and Q6 do not open.** Per operator rule 2 and the framework's
hard sequence, OUT at Q2 closes the file permanently. What follows is the price the queue's output
contract requires, under the heading operator rule 3 mandates.

---
# COMPUTATION — NOT A CLEARANCE
*(Operator rule 3. The file closed at Q2. The queue's output contract requires a price either
way; this heading is how the hard sequence is preserved. **No entry language appears below and
none is implied.**)*

## The owner-earnings series, built by hand from the filed cash-flow statements
OE = operating cash flow − stock compensation − (c). **(c) at the capex end = investing
"Expenditures for property, plant, and equipment" PLUS the financing-line "Payments on equipment
purchase contracts"** (the INTC check, run above). SBC subtracted in full **[E5-06]**; the reported
charge is the floor of the subtraction, not the measure **[E3-70]** — recorded, **not stacked**.

| FY | revenue | net income | OCF | SBC | D&A | capex (inv+fin) | gov incentives | **OE @capex** | OE @D&A | OE @net capex |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 12,399 | −276 | 3,168 | 191 | 2,980 | 5,817 | — | **−2,840** | −3 | −2,840 |
| 2017 | 20,322 | 5,089 | 8,153 | 215 | 3,861 | 5,253 | 21 | **2,685** | 4,077 | 2,706 |
| 2018 | 30,391 | 14,135 | 17,400 | 198 | 4,759 | 9,085 | 355 | **8,117** | 12,443 | 8,472 |
| 2019 | 23,406 | 6,313 | 13,189 | 243 | 5,424 | 9,855 | 748 | **3,091** | 7,522 | 3,839 |
| 2020 | 21,435 | 2,687 | 8,306 | 328 | 5,650 | 8,286 | 262 | **−308** | 2,328 | −46 |
| 2021 | 27,705 | 5,861 | 12,468 | 378 | 6,214 | 10,325 | 495 | **1,765** | 5,876 | 2,260 |
| 2022 | 30,758 | 8,687 | 15,181 | 514 | 7,116 | 12,208 | 115 | **2,459** | 7,551 | 2,574 |
| 2023 | 15,540 | **−5,833** | 1,559 | 596 | 7,756 | 7,814 | 710 | **−6,851** | −6,793 | −6,141 |
| 2024 | 25,111 | 778 | 8,507 | 833 | 7,780 | 8,535 | 315 | **−861** | −106 | −546 |
| 2025 | 37,378 | 8,539 | 17,525 | 972 | 8,352 | 15,857 | 2,005 | **696** | 8,201 | 2,701 |
| **10y total** | | **45,980** | **105,456** | **4,468** | **59,892** | **93,035** | **5,026** | **7,953** | | **12,979** |

**The single most important line in this file.** Across a full ten-year cycle containing two booms
and two busts, Micron generated **$105.5bn of operating cash flow and consumed $93.0bn of capital
expenditure**, leaving **$7,953M of owner earnings in total — $795M a year.** Reported net income
over the same decade was **$45,980M**. The $38bn difference is capital expenditure in excess of
depreciation, and it is **[E2-27]**'s mechanism and the textile-loom lesson **[E3-62]**: the gains
went to the buyers of memory, not to the owners of Micron. *"Nothing was going to stick to our ribs
as owners."*

## Every window, published, never selected **[E4-38, E4-25]**

| window | (c) = total capex | (c) = D&A **[INVALID end, [E5-20]]** | (c) = capex net of government money |
|---|---|---|---|
| FY2023-25 (3y, the screen's window) | **−2,339** | 434 | −1,329 |
| **FY2021-25 (5y, the corpus default [E2-42])** | **−558** | 2,946 | 170 |
| FY2020-24 (5y) | −759 | 1,771 | −380 |
| FY2019-23 (5y, ending in the trough) | 31 | 3,297 | 497 |
| FY2018-22 (5y) | 3,025 | **7,144** | 3,420 |
| FY2017-21 (5y, the best) | **3,070** | 6,449 | 3,446 |
| FY2016-20 (5y) | 2,149 | 5,273 | 2,426 |
| **FY2016-25 (10y, full cycle)** | **795** | 4,110 | 1,298 |

- **Combined range across all windows and both capex ends: −$2,339M to +$7,144M — a $9,483M width
  on a mean that never exceeds $7.2bn.**
- **The D&A end is INVALID here, not merely optimistic [E5-20].** Memory fabs are the most
  capital-intensive assets in this queue; ten-year capex was **1.55x** ten-year depreciation, and
  government incentives further suppress reported D&A by reducing the carrying amount of the assets
  (Note 1). The D&A column is displayed as a display of the guess, never as an equally legitimate
  answer.
- **[E4-41] normalise DOWN, and the leave-two-out check:** full 10-year capex-end mean $795M;
  **best** leave-two-out (drop FY2016 and FY2023) **$2,206M**; worst (drop FY2018 and FY2019)
  −$407M. Even the most favourable pair-drop leaves $2.2bn.
- **[E5-11]/[E3-55] on the width:** this is not See's-style noise around a certain mechanism. The
  spread comes from the *level* being genuinely indeterminate — the same plant produced −$6,851M in
  FY2023 and +$696M in FY2025 on the same assets. **The width is the business, not a measurement
  artifact.**

## The current cycle, from the unaudited 10-Q — shown separately, never blended **[E4-25]**
| | 9M FY2026 | annualised |
|---|---|---|
| Operating cash flow | 45,702 | 60,936 |
| less SBC | 954 | 1,272 |
| less capex | 19,602 | 26,136 |
| **OE, capex end** | **25,146** | **33,528** |
| OE net of $2,989M government incentives | 28,135 | 37,513 |
| **Q3 FY2026 alone** (OCF 25,388 − SBC 355 − capex 7,826) | **17,207** | **68,828** |

## THE PRICE

**Market cap $1,148,130M** = 1,129,393,151 shares × **$1,016.59** (close 2026-09-04; aggregator,
live quote only, flagged). **Sovereign 5.24%**, US Treasury 30-year par yield, 2026-09-04, issuing
authority. **Bare rate, no per-name premium [E3-42].**

| construction | OE $M | yield | value @5.24% | value @10% floor | perpetual growth the price needs @5.24% |
|---|---|---|---|---|---|
| 10y full cycle, capex end | 795 | 0.07% | **$13** | $7 | 5.17% |
| 10y full cycle, net of government money | 1,298 | 0.11% | **$22** | $11 | 5.13% |
| leave-two-out best, 10y capex end | 2,206 | 0.19% | **$37** | $20 | 5.05% |
| best 5y window (FY2017-21), capex end | 3,070 | 0.27% | **$52** | $27 | 4.97% |
| 10y, (c)=D&A *[INVALID end]* | 4,110 | 0.36% | **$69** | $36 | 4.88% |
| best window (FY2018-22), (c)=D&A *[INVALID end]* | 7,144 | 0.62% | **$121** | $63 | 4.62% |
| 9M FY2026 annualised, capex end | 33,528 | 2.92% | **$567** | $297 | 2.32% |
| 9M FY2026 annualised, net of government money | 37,513 | 3.27% | **$634** | $332 | 1.97% |
| **Q3 FY2026 alone annualised — most generous constructible** | **68,828** | **5.99%** | **$1,163** | **$609** | **−0.75%** |

### **THE PRICE, AS A ROUND-NUMBER RANGE [E4-01]**
- **Conservative — the full-cycle record, which is the [E2-58]-consistent basis: ~$15 to ~$50 per share.**
- **Judged mid — the best five-year window plus the (invalid) D&A end as an upper bracket, i.e. the
  most that the *pre-AI* record can support: ~$50 to ~$120 per share.**
- **Generous — the current nine months annualised into perpetuity, which requires the present
  shortage to be permanent: ~$570 to ~$630 per share.**
- **Most generous constructible — the single best quarter in the history of the memory industry,
  annualised and capitalised forever: ~$1,160 per share.**
- **CURRENT PRICE: $1,016.59.**

### What the price already assumes
- **To yield the 5.24% sovereign at this price, Micron must earn $60,162M of owner earnings every
  year. Its ten-year mean is $795M — the price requires 75.7x the full-cycle figure.**
- **To clear the [E4-28] ~10% floor, it must earn $114,813M a year, forever — 144x the ten-year
  mean, and 1.67x the annualised rate of the best quarter it has ever had.**
- Put the other way: taking the current nine-month run-rate as the base, **the price needs that
  peak run-rate to grow 2.32% a year forever just to match the government bond**, and **7.08% a
  year forever to reach the floor** — compounding from the top of the sharpest shortage on record,
  against **[E4-35]**'s base rate that fewer than 10 of the 200 most profitable companies sustain
  15% for twenty years, and **[E4-44]**'s bound that value *"cannot over the long term grow faster
  than its earnings do."*
- **[E2-63] — state the ceiling.** Micron's own take-or-pay contracts cap the largest agreements at
  *"the market price in the second calendar quarter of 2026."* The company has contractually sold
  its own upside on that volume at approximately today's spot.

**Windage count: 0.** No end margin was applied, because Q5 never opened; the numbers above are the
realistic-input arithmetic of Bar 1 with the margin unspent **[E4-11, E4-48]**. Nothing here was
narrowed to reach a conclusion; the conclusion was reached at Q2 on filed evidence before any of it
was computed.

---
# RECORDED, NOT ADJUDICATED
*The operator's earned tests. Q3-Q6 do not open, so none of these is a verdict. They are on the
record because the reading was done and because several bear on the Q2 finding.*

- **The dividend, decomposed honestly.** Initiated FY2021, held at $0.115/quarter through FY2025
  ($0.46/yr, $522M), raised to **$0.15 in Q3 FY2026**. **[E2-52] fires on FY2023:** Micron paid
  **$504M of dividends and repurchased $425M of stock in the year it lost $5,833M**, funded by
  **$6,716M of new debt issuance**. *"Beware of 'dividends' that can be paid out only if someone
  promises to replace the capital distributed."* **[E2-60]**'s third dimension is the same event
  seen from the balance sheet: the payout was made while financial strength was being consumed, so
  (c) was understated in that year. On the current numbers the dividend is trivially covered
  ($436M declared against $47,268M of nine-month net income) — **a 0.9% payout, which is itself the
  candid signal about how much of this the board treats as durable.**
- **Buybacks [E5-08], all three conditions.** $7.19bn cumulative through FY2025 under a $10bn
  authorisation; **$2.66bn in the peak year, nothing in FY2025, $650M in 9M FY2026.** Condition (1)
  ample funds: yes, overwhelmingly. Condition (2) material discount to conservatively calculated
  IV: **not on any construction above except the one that capitalises a single quarter** — so the
  FY2026 repurchases are a capital-allocation prompt, stated with **[E4-13]**'s humility clause.
  Condition (3) **[E4-31]**, an adequately informed register: the FY2025 10-K notes repurchases are
  *"subject to… restrictions applicable under our CHIPS Act direct funding agreements"* — the
  constraint is disclosed, which is the candid form.
- **[E5-11] + [E5-39], the three strengths, read through a down-cycle.** (1) *Large and reliable
  stream of earnings*: large, **not reliable** — FY2023 net income −$5,833M. (2) *Massive liquid
  assets*: **yes, and transformed** — cash and short-term investments **$26,022M at 2026-05-28**
  against total debt of **$5,722M**, i.e. **net cash of ~$20bn**, after repaying **$9,380M of debt
  in nine months.** (3) *No significant near-term cash requirements* — **this is the one that
  binds and it is the reason the class is what it is**: the 10-Q guides capital expenditure
  upward across four new fabs, and *"expansion projects are multi-year projects that require
  significant lead time and commitment of capital well in advance of achieving any returns."* The
  balance sheet is at its strongest point ever **at exactly the moment the company has committed to
  its largest-ever capital programme** — which is [E2-27]'s setup, not its refutation.
- **[E2-54] coverage.** Interest paid net of capitalised amounts was $418M (FY2025) against
  $17,525M of OCF; nine-month FY2026 interest expense is $106M. Comfortably met. Debt is unsecured
  and, other than finance leases, unranked. **[E3-52]:** the $1,020M of *noncurrent unearned
  government incentives* and the $422M of customer deposits are covenant-light, long-dated
  liabilities of the favourable kind — small.
- **ASC 842.** Finance leases are primarily equipment and **gas supply agreements deemed to contain
  embedded leases**. Financing cash outflow for finance leases $323M / $155M / $109M (FY2025/24/23),
  plus **$1.16bn of executed-but-not-commenced obligations over a weighted-average 15 years** —
  disclosed, off the maturity table, and a genuine near-term-cash item under [E5-11](3).
- **Software capex.** No capitalised-software line found in the FY2025 cash-flow statement or
  footnotes — recorded sweep, **no instance found**. R&D is expensed: **$3,798M (FY2025), 10.2% of
  revenue**; $3,737M in nine months of FY2026. The AVGO/QCOM ruling therefore does not bite here in
  reverse — Micron's D&A is almost entirely plant depreciation, which is why the [E5-20] exception,
  not the [E3-44] default, governs (c).
- **Contingent-liability persistence.** Netlist patent litigation is continuous from **June 2022 to
  March 2026** across four complaints, now reaching **HBM products specifically**; venue transferred
  to D. Del. on 2026-03-06. **No accrual, no range of reasonably possible loss, is disclosed.**
  Persistent and unquantified — recorded as a prompt.
- **The absolute-size acquisition gate.** `acquisition_flag()` scales to market cap and **would not
  fire**: the **$1.8bn Powerchip Tongluo fab purchase (completed March 2026)** is 0.16% of a
  $1,148bn cap. The perimeter was found by reading the filing, per operator rule 4 — and the
  acquisition matters for a reason the flag could never see: **it is capacity being added into the
  shortage**, which is the [E2-27] mechanism, not a diversification question.
- **Pay versus performance.** The 10-K's own performance graph baselines **$100 invested on
  2020-08-31** in MU, the S&P 500 and the Philadelphia Semiconductor Index (SOX), dividends
  reinvested — a five-year window that ends before the current move. Not adjudicated; the proxy
  (DEF 14A) carries the Item 402(v) pay-versus-performance table and is the document that would
  resolve the compensation-metric question. It was not pulled, because Q3 does not open. **Named
  as the artifact, per the UNRESEARCHED discipline, though no verdict rests on it.**
- **[E4-52] lollapalooza.** Flags found are individually mild and do **not** converge: the FY2023
  debt-funded dividend, the buyback at a price no construction supports, and an unquantified
  persistent litigation matter. Three prompts, three different directions. **No confluence found**,
  and it is recorded that way rather than assembled into one.
- **[E4-30] cash-tax tell.** Income taxes paid net: $583M (FY2025) / $338M (FY2024) / $532M (FY2023)
  / $493M (FY2022). Nine-month FY2026 tax provision **$8,178M** on $55,433M pretax = **14.8%**,
  consistent with the company's own guidance of *"mid to high-teens percentage range, starting in
  2026."* **Cash taxes are RISING with pretax income, not falling as a share of it.** The tell does
  not fire.

---
# THE ANSWER

**PRICE: ~$15 to ~$120 per share on the full-cycle filed record; ~$570 to ~$1,160 per share only if
the tightest supply quarter in the history of the memory industry is treated as permanent. Current
price $1,016.59 (2026-09-04).**

**PASS/FAIL: FAIL. The file closed at Q2 — OUT, permanent.** Q1 returned IN. Q3, Q4, Q5 and Q6 did
not open.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN → **Q2 OUT** → stop.
- [x] No question marked IN carries an "unverified" or "provisional" caveat. Q1's IN rests on the
      filed unit economics; the one provisional-looking item in the file — the HBM durability
      claim — is explicitly held **UNKNOWABLE** and is not used to support any IN.
- [x] Every UNKNOWABLE states what specifically cannot be known: **(i)** whether contracted HBM
      floors hold through a down-cycle — the resolving document is a 10-K covering a memory
      down-cycle in which contracted HBM is a material share of revenue, and **it cannot exist
      until the cycle turns**; **(ii)** Samsung's and SK hynix's same-metric figures at the filing
      rung — obstacles named (12g3-2(b) exemption; no 20-F yet due).
- [x] Step 0: MD&A, cash-flow statement **including detail and supplemental lines**, and footnotes
      read across five filings; accession numbers recorded; **two** figures cross-checked to the
      filed statements (FY2025 OCF $17,525M; equity recomputed A−L = $100,724M, per [E5-32]).
- [x] Owner earnings on a multi-year mean; **eight windows published, none selected [E4-38]**;
      capex band disclosed as a judgment with the D&A end marked **INVALID [E5-20]**; the
      government-money construction shown as a third column, never netted silently.
- [x] Competitor row filled — **8 named of ~10**; the two non-registrants recorded **UNKNOWABLE at
      the filing rung** with obstacles named, and the adjudication stated that an additional
      competitor cannot widen a moat.
- [x] Sovereign is for the earnings currency (USD, stated in the 10-K), from the issuing authority
      (US Treasury), dated 2026-09-04.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar; **windage count 0** — no end margin applied because Q5 never opened.
- [x] Prices dated; aggregator used for the live quote only and flagged.
- [x] Run committed to git.
- [x] **Operator rule 9 check.** The prior stated at the outset was Q2 OUT on [E2-58]. That is the
      outcome, which is exactly when [E4-26] bites hardest. The disconfirming case was therefore
      pulled to its strongest filed form (the take-or-pay quotations, quoted in full including the
      *"well above our peak quarterly margins in any past cycle"* sentence), sized from the filing
      rather than characterised, and **defeated on the corpus's own [E2-59] ruling and on $5bn of
      remaining performance obligations — not on assertion.** The reader can check both against the
      Q3 FY2026 10-Q in under two minutes.

## REGISTER
- **Verdict: [x] OUT (about the business), at Q2.**
- **One line:** Micron is the textbook [E2-58] commodity — its own 10-K says average selling prices
  *"have been below our manufacturing costs"*, its FY2023 record shows DRAM price falling
  high-40s% on near-flat volume and NAND price falling low-50s% while volume **rose**, it posted
  the worst and only negative trough gross margin in an eight-name competitor row, and ten years of
  filed cash flow produced **$795M a year of owner earnings against a $1,148bn market cap**; the
  HBM take-or-pay structure is the best case any commodity producer in this queue has offered and
  it is **[E2-59] administered pricing sized at $5bn of remaining performance obligations, with a
  ceiling at today's spot.**
- **What specifically cannot be known:** whether contracted HBM floor pricing survives a
  down-cycle. **No document that would resolve it exists yet**, which makes it UNKNOWABLE rather
  than UNRESEARCHED — and it does not reopen a Q2 that fails on six other filed grounds.
