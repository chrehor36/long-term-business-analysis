# Company Run — ADVANCED MICRO DEVICES, INC. (AMD) — 2026-09-07
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

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the FY2025 10-K: *"Substantially all
of our sales transactions are denominated in U.S. dollars."* So USD, and only USD.
- rate **5.24%** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-year,
  home.treasury.gov (the issuing authority)**, struck fresh via `tools/sources.py` on
  2026-09-07. FRED DGS30 not used — it is the fallback, not the source.
- FX: none. No ADR.

### STAGE 0 BY HAND — the share count, the cap, the dividend, the buyback record

- **Share count, hand-read off the cover: 1,632,475,042** shares of common stock outstanding
  as of **2026-07-29**, from the cover of the Q2 FY2026 10-Q (accession
  **`0000002488-26-000123`**, 26 weeks ended 2026-06-27, filed 2026-08-05), matched to the
  `dei:EntityCommonStockSharesOutstanding` tag for the same accession. **SINGLE CLASS.** The
  FY2025 10-K cover gives 1,630,410,843 as of 2026-01-30; its balance sheet gives 1,695M
  issued / 1,630M outstanding with 65M in treasury. **No split in any window used.**
- **Price: $477.57**, close of **2026-09-04** (Yahoo via `tools/sources.py` — **AGGREGATOR,
  FLAGGED**, used for the live quote only, per operator rule 5).
- **MARKET CAP = $779,621M.** 1,632,475,042 × $477.57.
- **DIVIDEND — VERIFIED ABSENT, not assumed.** There is **no dividend line of any kind** in
  the FY2025 Consolidated Statements of Cash Flows financing section. That section reads, in
  full: debt/CP issuance $2,441M; debt/CP repayment $(950)M; employee-plan stock sales $285M;
  **repurchases of common stock $(1,316)M**; repurchases for tax withholding $(607)M;
  contingent-consideration settlement $(284)M; other nil. AMD paid no common dividend in any
  year inside any window used here.
- **THE BUYBACK RECORD AGAINST VALUE [E5-08]:** repurchases of **$985M (FY2023), $862M
  (FY2024), $1,316M (FY2025)** — $3,163M over three years — plus $427M/$728M/$607M of
  tax-withholding repurchases. Set against stock-based compensation of $1,384M/$1,407M/
  $1,638M over the same three years: **the buyback has not shrunk the register; it has
  partially offset dilution.** Shares outstanding went 1,617M → 1,622M → 1,630M → 1,632M
  (Q2 FY2026): **UP in every year in which the company spent $3.2bn buying its own stock.**
  Carried below, since Q3 does not open.

### The filing was read — not tagged data **[E3-27, E4-14]**

- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **PRIMARY: FY2025 Form 10-K, accession `0000002488-26-000018`, fiscal year ended
  2025-12-27, filed 2026-02-04** (`amd-20251227.htm`).
- **STUB: Q2 FY2026 Form 10-Q, accession `0000002488-26-000123`, 26 weeks ended 2026-06-27,
  filed 2026-08-05**, read in full for the TTM. *(The stub here is a filed 10-Q, not a
  furnished earnings release — the AVGO defect does not repeat.)*
- **Vintages read and diffed:** FY2021 10-K `0000002488-22-000016` · FY2022 10-K
  `0000002488-23-000047` · FY2024 10-K `0000002488-25-000012` · FY2025 10-K · Q2 FY2026
  10-Q. Five filed documents; six fiscal years of segment data reconstructed on a
  consistent basis.
- **FIGURE CROSS-CHECKED AGAINST THE FILED STATEMENT — and the check found the tagged data
  wrong.** XBRL `AmortizationOfIntangibleAssets` returns **2,800 / 2,400 / 2,300** for
  FY2023/24/25. Those are the **rounded MD&A narrative figures.** The filed Consolidated
  Statements of Cash Flows line *"Amortization of acquisition-related intangibles"* reads
  **2,811 / 2,393 / 2,254**. The filed statement governs.
- **SECOND CROSS-CHECK, AND IT IS THE ONE THAT MOVES THE ANSWER.** XBRL
  `NetCashProvidedByUsedInOperatingActivities` returns **$7,709M** for FY2025. The filed
  statement shows what that is: *"Net cash provided by operating activities of continuing
  operations **6,493**; Net cash provided by operating activities of discontinued operations
  **1,216**; Net cash provided by operating activities **7,709**."* **The screen — and every
  yield built on that tag — is carrying $1,216M of cash from a business AMD no longer owns.**
  Every construction below uses **$6,493M**.

---
## THE SCREEN ROW — REPRODUCED, THEN REBUILT OVER MY OWN WINDOWS

**The committed row** (`Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`):

    AMD,ADVANCED MICRO DEVICES INC,766725,1944,2293,0.179,0.0025,-0.0502,0.0975,2.84,
    STEP UP - normalize down [E4-41],0.285,,2025-12-27

**BOTH ENDS REPRODUCE TO THE DOLLAR, AND BOTH ARE WRONG IN THE SAME DIRECTION.**

- `oe_bottom` **1,944** = the **3-year FY2023-25 mean at the CAPEX end**, on the
  *consolidated* OCF: (1,667 + 3,041 + **7,709**)/3 − (1,384+1,407+1,638)/3 −
  (546+636+974)/3 = 4,139.0 − 1,476.3 − 718.7 = **1,944.0**. ✓
- `oe_top` **2,293** = the **5-year FY2021-25 mean at the DEPRECIATION-only end**, same
  consolidated OCF: 3,900.6 − 1,177.8 − 430.2 = **2,292.6**. ✓
- **So the two "ends" are two different WINDOWS crossed with two different CAPEX ENDS.** The
  four-construction defect in its purest form — **a fifth confirmation in four days after
  AAPL, GOOGL, AVGO and TXN.** The reported `spread` of 0.179 is neither a capex band nor a
  window spread; it is one of each, crossed, and it therefore measures nothing.
- **AND A DEFECT THE OTHER FOUR DID NOT HAVE: both of the screen's ends include $1,216M of
  discontinued-operations cash in their FY2025 term.** Corrected to continuing operations,
  the same two constructions are **1,539** and **2,049**. The screen overstates its own
  conservative end by **26.3%**.
- **The cap is light too**: $766,725M against the hand-read $779,621M — a $12,896M gap,
  consistent with pricing the 1,630,410,843 FY2025-cover count at a stale ~$470.26.
  Immaterial at this yield; recorded because it runs the same direction as the other two.

### THE REBUILD — continuing operations, eight windows, three capex ends ($M)

D&A is split per the AVGO ruling into the **physical/operating** line and the
**acquisition-related** line, and only the physical half is a candidate for (c).

| window | capex end | non-acq D&A end | depreciation-only end | yield (capex / dep) |
|---|---|---|---|---|
| 3-yr FY2023-25 | 1,539 | 1,570 | 1,785 | 0.20% / 0.23% |
| 4-yr FY2022-25 *(post-Xilinx, one perimeter)* | 1,662 | 1,642 | 1,850 | 0.21% / 0.24% |
| **5-yr FY2021-25** *(corpus default [E2-42])* | **1,898** | 1,860 | 2,049 | 0.24% / 0.26% |
| 8-yr FY2018-25 | 1,226 | 1,198 | 1,348 | 0.16% / 0.17% |
| 10-yr FY2016-25 | 953 | 922 | 1,055 | 0.12% / 0.14% |
| 5-yr FY2017-21 *(pre-Xilinx anchor)* | **592** | 558 | 644 | 0.08% / 0.08% |
| **TTM to 2026-06-27** | **5,841** | 6,705 | **6,953** | **0.75% / 0.89%** |
| FY2025 alone | 3,881 | 4,105 | 4,334 | 0.50% / 0.56% |

**TRUE WIDTH: $592M to $6,953M — 1,075% — against the screen's 17.9%. The screen understated
the width of this business's owner earnings by roughly sixty times, and understated it in
the flattering direction at the bottom.**

**AND THE WIDTH IS DECISION-IRRELEVANT, WHICH IS WHY THE FILE STAYS OPEN TO A VERDICT
[E4-25].** Every construction, on every window, at every capex end — including the trailing
twelve months and including the single best fiscal year in the company's history — yields
between **0.08% and 0.89% against a 5.24% sovereign.** The range straddles nothing. Per the
AVGO/QCOM adjudication rule: *a range that is wide but entirely on one side of the yardstick
is a finished answer, not an indeterminate one.*

**The screen's `level_shift 2.84 — STEP UP, normalize down [E4-41]` is correct, and it
understates the problem. The step is not a business cycle. It is an acquisition.**

---
## THE PERIMETER — XILINX SITS INSIDE EVERY WINDOW, AND IT WAS PAID FOR IN STOCK

**From the FY2022 10-K, Note 5 — Business Combinations:**
- Closed **2022-02-14**. **Total purchase consideration $48,793M** ($46,427M net of $2,366M
  of cash acquired).
- **Paid in stock: 429 million AMD shares** at the 2022-02-11 close of **$113.18**, plus
  $275M of replacement equity awards.
- Allocated: **acquisition-related intangibles $27,308M**; **goodwill $22,784M**; deferred
  tax liabilities $4,346M. Net tangible assets acquired were *negative*.
- Intangible detail: developed technology **$12,295M / 16 yr**; customer relationships
  **$12,290M / 14 yr**; backlog $793M / 1 yr; corporate trade name $65M / 1 yr; product
  trademarks $895M / 12 yr; IPR&D $970M indefinite-lived.
- Xilinx contributed FY2022 (from 14 Feb) **revenue $4,612M and operating income $2,247M** —
  a **48.7% operating margin** — *before* the $4.2bn of amortisation, SBC and deal costs
  recorded in All Other.
- **THE FILED PRO FORMA IS THE CROSS-CHECK AND IT IS BRUTAL.** AMD's own supplemental
  unaudited pro forma, as if Xilinx and Pensando had been owned from the start of FY2021:
  **FY2021 combined revenue $20,150M and combined net income $8 MILLION**, against AMD
  standalone's actual FY2021 net income of **$3,162M**. FY2022 pro forma: $24,117M revenue,
  $2,311M net income.

**WHY `acquisition_flag()` SHOWS NOTHING.** The `acq_note` cell in AMD's screen row is
**empty**. It is empty because the flag reads the *investing* cash-flow line "Acquisitions,
net of cash acquired," and **a $48.8bn all-stock deal never touches it** — FY2022's line
reads $(1,548)M, which is Pensando. **The largest perimeter break in this file is invisible
to every cash-flow-based test.** An absolute-size gate has to read the equity statement or
the business-combination note; the cash-flow statement will never show it.

**BUILDING OWNER EARNINGS PRO FORMA — WHAT I DID, AND THE PRECISE REASON I DID NOT NEED
XILINX'S STANDALONE 10-Ks.** The deal sits inside FY2022, so the corpus-default five-year
window FY2021-25 contains **exactly one pre-deal year**. Rather than guess, I ran the window
both ways:
- **post-Xilinx only, FY2022-25** (four full years, one perimeter throughout): **$1,662M**
  at the capex end.
- **corpus-default 5-yr FY2021-25** (one pre-deal year): **$1,898M**.
- The gap is **$236M — 14% — and it points AGAINST the bull case**: including the pre-deal
  year *raises* owner earnings, because standalone AMD produced $2,841M of owner earnings in
  FY2021 against $2,034M in FY2022 with Xilinx inside it. **A pro-forma build cannot rescue
  this file; it would lower the number.** Xilinx's standalone 10-Ks (CIK 743988, on EDGAR)
  would refine the FY2021 term by roughly $1bn of operating cash flow against a ~$780bn cap.
  **Recorded as a known, bounded, quantified imprecision — not as an unresearched gap:** its
  entire plausible range moves the yield by under 15 basis points, on a yield that is 4.35
  points short of the sovereign.

### AMORTISATION OF ACQUIRED INTANGIBLES — WHAT DOES IT RENEW? [E3-44] read for DIRECTION, not defaulted

1. **The physical half is small — but this is NOT the AVGO shape, and the brief's expectation
   is wrong at this filer. I record it as wrong.** AMD is **fabless; it owns no wafer fab.**
   Filed depreciation: 296 / 439 / 441 / 454 / **521** (FY2021-25). Filed capex: 301 / 450 /
   546 / 636 / **974**. **capex ÷ depreciation: 1.02 → 1.03 → 1.24 → 1.40 → 1.87, and ~2.1×
   in H1 FY2026** ($1,197M of capex in 26 weeks against $427M of total operating D&A).
   **The D&A end was the large end through FY2024; it INVERTED in FY2025 and the inversion is
   widening.** Capex at nearly twice depreciation and accelerating is a **growth build, not a
   maintenance bill** — which makes the **depreciation end the GENEROUS end and the capex end
   the CONSERVATIVE end.** That is the ordinary direction, and the **opposite of AVGO's
   inversion.** Stated explicitly so no later reader inverts it.
2. **The intangible half renews nothing that R&D above the OCF line does not already renew.**
   FY2025 amortisation of acquired intangibles is **$2,254M** — the unwinding of a price
   settled in 2022 in shares. What keeps Xilinx's developed technology current is **R&D,
   expensed above the OCF line at $8,091M, 23.4% of revenue, the highest ratio in the
   competitor row.** Deducting the amortisation as well would charge the renewal twice.
   **[E2-60]'s counter-test — is R&D intensity falling? — does NOT fire**, which is the
   opposite of AVGO's software segment: AMD's R&D ran $5,005M → $5,872M → $6,456M →
   **$8,091M**, holding 21.2% / 25.9% / 25.0% / 23.4% of revenue.
3. **BUT THE STOCK WAS THE COST, AND NO CASH-FLOW STATEMENT WILL EVER SHOW IT.** 429 million
   shares — **26.3% of today's 1,632M count** — left the building for Xilinx. **[E5-44]:**
   *"The intrinsic value of the shares you give in an acquisition must not be greater than
   the intrinsic value of the business you receive."* Measured today, those 429M shares are
   worth **$204.9bn at $477.57**, against an Embedded segment producing **$1,243M** of
   operating income. Measured at the time, $48.5bn against $2,247M annualised. **Carried with
   the humility clause and with [E5-24] — what is smart at one price is dumb at another; this
   is a hindsight measurement and it is labelled as one.**

### (c) JUDGED — a disclosed judgment, per [E2-23] *"(c) must be a guess"*

**(c) = total capital expenditure**, and **the capex end is the conservative end**, because
(i) the physical ratio is 1.87× and rising, so depreciation demonstrably understates what
this business is spending to hold position, and (ii) the technology renewal is already borne
inside operating cash flow as R&D. This is the [E3-44]/[E2-41] default **read in the
direction the filing points**, not defaulted to. **[E5-20]'s railroad exception is not
invoked** — AMD has no fabs — and its logic nevertheless runs the same way: the D&A end
overstates owner earnings here.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** AMD designs logic chips and pays
someone else to make them. It licenses the x86 instruction set (and since 2022 owns Xilinx's
FPGA architectures), employs about $8bn a year of engineers to lay out circuits, hands the
layout to TSMC, buys HBM memory and advanced packaging capacity, and sells the finished part
to four kinds of buyer: hyperscale cloud operators and their ODMs (Data Center), PC makers
and game-console makers (Client and Gaming), and industrial, aerospace and communications
equipment makers (Embedded). It owns no fab. Gross margin is the gap between what a designed
part sells for and what TSMC, the memory vendors and the packaging houses charge to build it
— **49.5% in FY2025** — and operating margin is what survives $8,091M of R&D, $2,254M of
purchase amortisation and $1,638M of stock compensation: **10.7%.**

**The scarce input the business controls — and this is the finding of Q1. It does not control
it.** The scarce inputs in leading-edge logic are (a) TSMC's most advanced process nodes and
(b) HBM and advanced-packaging capacity. **AMD rents both**, in competition with Nvidia,
Apple and every other fabless designer, on terms AMD does not set and does not disclose.
What AMD *does* own is an **x86 architectural licence** — a real legal scarcity, held by
exactly two companies at scale — and Xilinx's FPGA tooling and installed base. **The x86
licence is the only true scarce input this company owns, and it sits in the segment that
produced 20.7% of segment operating income in the most recent filed half.**

**Will the fundamentals look broadly the same in ten years?** The unit economics — design,
outsource, sell — will. **The competitive position will not, and the filing says so**: the
10-K names Arm-based PC processors against Client, customers building their own accelerators
against Data Center, and *"the ASIC market, which has been ongoing since the inception of
FPGAs"* against Embedded. AMD's own six-year record is the evidence: return on average
equity of **47.4% (FY2021), 4.2%, 1.5%, 2.9%, 7.2% (FY2025)**.

**I can understand it.** Design-for-hire on rented capacity is not a complex business model;
it is a simple one with a hard competitive question, and Q1 asks about comprehension, not
outcome. **[E4-46]** is satisfied — nothing in this business needs five months.

- **VERDICT: [x] IN**

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

**THE HONEST STRUCTURE IS THREE BUSINESSES [E5-37]**, and per **[E2-56]** — *"their marvelous
core businesses camouflage repeated failures … elsewhere"* — the consolidated series is
refused and each leg is judged on the filed segment note. This is the QCOM segment-separation
method, applied to three segments instead of two.

### THE PROFIT-MIX TEST DECIDES WHICH TAIL WAGS — AND IT IS OPERATING INCOME, NOT REVENUE

| FY | DC rev | DC OI | m | C&G rev | C&G OI | m | Emb rev | Emb OI | m | segment OI | **share of segment OI: DC / C&G / Emb** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2022 | 6,043 | 1,848 | 30.6% | 13,006 | 2,143 | 16.5% | 4,552 | 2,252 | **49.5%** | 6,243 | 29.6% / 34.3% / **36.1%** |
| 2023 | 6,496 | 1,267 | 19.5% | 10,863 | 925 | 8.5% | 5,321 | **2,628** | **49.4%** | 4,820 | 26.3% / 19.2% / **54.5%** |
| 2024 | 12,579 | 3,482 | 27.7% | 9,649 | 1,187 | 12.3% | 3,557 | 1,421 | 39.9% | 6,090 | **57.2%** / 19.5% / 23.3% |
| 2025 | 16,635 | 3,603 | 21.7% | 14,550 | 2,855 | 19.6% | 3,454 | 1,243 | 36.0% | 7,701 | **46.8%** / 37.1% / 16.1% |
| **H1-26** | 12,493 | **3,702** | 29.6% | 7,446 | 1,157 | 15.5% | 1,850 | 724 | 39.1% | 5,583 | **66.3%** / 20.7% / **13.0%** |

*Sources: FY2022 10-K `0000002488-23-000047` (FY2020-22); FY2024 10-K `0000002488-25-000012`
(FY2022-24, four-segment basis); FY2025 10-K `0000002488-26-000018` (FY2024-25, three-segment
basis after Client and Gaming were combined in Q1 FY2025 with prior periods retrospectively
adjusted); Q2 FY2026 10-Q `0000002488-26-000123` (H1 FY2026). FY2022-23 C&G is Client plus
Gaming added to match the current basis; FY2023 segment revenue is derived from the filed
cost-and-expense and operating-income rows and reconciles to filed total revenue of $22,680M.
Segment OI excludes the All Other category, which is $(4,979)M / $(4,419)M / $(4,190)M /
$(4,007)M / $(2,117)M and consists principally of acquisition-intangible amortisation and
stock-based compensation.*

**THE ANSWER TO THE QUESTION THE BRIEF SAID WOULD DECIDE THIS FILE: the Data Center tail wags
the dog, and it did not use to. Data Center is 66.3% of segment operating income in the most
recent filed half, up from 26.3% two years earlier. Embedded — the FPGA annuity, the genuine
franchise candidate — has gone from 54.5% of segment operating income to 13.0%.** The brief's
alternative (b) is the live one; (a) is half-true and is recorded below at full strength.

**One further reading of the same table, which is a Q2 fact and not a Q4 one:** segment
operating income of $7,701M in FY2025 became **$3,694M** of consolidated operating income.
**52% of everything the three businesses earned was consumed by the All Other line** —
$2,254M of purchase amortisation and $1,638M of stock compensation. A franchise is a claim
about what reaches the owner.

### EMBEDDED (Xilinx): the franchise candidate FAILS the ACLS supplier test on its own numbers

The ACLS run (2026-09-05) established the transplantable test: **did filed price and margin
hold through a revenue collapse?** ACLS passed it — revenue −26%, the filed system price
range raised from *"$2.4 million to $10.0 million"* to *"$2.6 million to $12.0 million"* and
held across three vintages, gross margin 43.7% → **44.9%** through the trough. AMD is fabless
and files no price range, so the price half cannot be run here. **The margin half can be, and
Embedded fails it:**

> **Revenue $5,321M (FY2023) → $3,454M (FY2025): −35.1%.
> Operating income $2,628M → $1,243M: −52.7%.
> Operating margin 49.4% → 36.0%: −13.4 points.**

**That is the exact opposite of what ACLS did.** A business with no close substitute and long
design-in cycles does not surrender thirteen points of operating margin while its volume
falls a third. The half-recovery in H1 FY2026 — operating income +20% year on year, margin
back to 39.1% — is real and is recorded, but it leaves Embedded operating income **still 53%
below its FY2023 peak, three years on.**

**[E4-55] — WHAT PHYSICAL SERIES IS FILED FOR EMBEDDED? NONE. THE ABSENCE IS THE FINDING.**
AMD files no unit series, no design-win count, no backlog figure and no attach rate for the
FPGA business, in any vintage. The **only** physical series anywhere in the filing is a
*percentage-change* series for Client processors. The Precision Steel test — pounds fell 69M
→ 46M while price rises held dollar revenue level — **cannot be run on the one segment where
it would matter most, because AMD publishes no pounds.**

### CLIENT AND GAMING (x86): [E2-44] passes BOTH halves for two years — then breaks in the stub

**[E2-44] half 1 — can it raise price with demand flat? THIS IS THE STRONGEST FACT IN THE
FILE FOR THE NAME, and AMD files it twice, in consecutive years, in its own MD&A:**

> **FY2024 10-K:** Client revenue rose *"primarily due to a **34% increase in unit shipments
> and a 13% increase in average selling price** driven by strong demand for AMD mobile and
> desktop Ryzen processors."*
>
> **FY2025 10-K:** *"primarily driven by a **31% increase in unit shipments of processors and
> a 15% increase in average selling price of processors**, reflecting strong demand for AMD
> desktop and mobile Ryzen processors."*

**Units +34% then +31%; price +13% then +15%. AMD took share while RAISING price in two
consecutive filed years.** Winning share *by* pricing is not a franchise; winning it while
*holding* price is. AMD did better than hold. **The brief's prior (a) is confirmed on the
FY2024-25 record, against my own expectation, and I record it as confirmed [E4-26].**

**[E2-44] half 2 — dollar volume growth on only minor additional capital?** Partly. Capex
went $636M → $974M → an annualised ~$2.4bn in H1 FY2026 while revenue grew 34% then 44%.
Capital intensity is rising, not falling.

**AND THEN THE STUB BREAKS HALF 1.** H1 FY2026: Client and Gaming revenue **+13%** ($6,562M →
$7,446M) with segment operating income **−8.4%** ($1,263M → $1,157M). **Margin 19.1% →
15.5%.** Growing revenue with falling profit is precisely the shape [E2-44] exists to detect,
and it is the most recent filed evidence in the file.

**NO x86 MARKET SHARE FIGURE IS FILED BY AMD IN ANY VINTAGE.** The competition section names
Intel as *"our primary competitor in the supply of CPUs and APUs"* and states that Nvidia
*"is the discrete GPU market share leader"* — AMD files its **competitors'** leadership, never
its own share. **The share trajectory the brief asked for cannot be established from AMD's
filings.** It can only be read from the other side, and Intel's filings tell it: revenue
**$63,054M (FY2022) → $52,853M (FY2025), −16.2%**, with operating income $2,334M → $93M →
**$(11,678)M** → **$(2,214)M**. **AMD gained share against a competitor that has lost money at
the operating line in two of the last three years.** Under **[E3-51]** that is a wave, not a
moat: *"when a surfer gets up and catches the wave … he can go a long, long time. But if he
gets off the wave, he becomes mired in shallows."*

### DATA CENTER: 66% of the profit, and it fails [E3-03](2) and (3) in AMD's own words

**[E3-03](2) — no close substitute. FAILS, twice, from the 10-K's own competition section:**

> *"In the Data Center segment, we compete primarily against Intel Corporation (Intel) and
> Nvidia Corporation (Nvidia) with our CPU, GPU DPU and AI NIC server products. In addition,
> we compete against Altera with our FPGA and adaptive SoC server products. A variety of
> smaller fabless silicon companies offer proprietary accelerator solutions and Arm®-based
> CPUs targeting data center use cases. **In addition, some of our customers are internally
> developing their own data center microprocessor products and accelerator products which
> could impact the available market for our products.**"*

The last sentence is the QCT shape, filed. **The first sentence is worse for the moat claim
than the last: AMD is not the thing with no close substitute — AMD IS the close substitute,
to Nvidia.** The competitor row makes the gap arithmetic.

**[E3-03](3) — not subject to price regulation. FAILS, and I did not expect this one.** From
the FY2025 10-K MD&A:

> *"During the second quarter of fiscal year 2025, the Company recorded approximately **$800
> million of inventory and related charges** on AMD Instinct MI308 Data Center GPU products
> due to new U.S. export restrictions on certain semiconductors to China… **U.S. government
> officials have expressed an expectation that the U.S. government will receive 15% of the
> revenue generated from licensed MI308 sales to China**; however, to date, the U.S.
> government has not published a regulation establishing such requirement."*

**A 15% revenue share expected by the state, and an $800M write-off (of which $360M was later
reversed on licences granted) imposed by administrative action inside one fiscal year, is
price and quantity administration of the segment's largest growth market.** **[E2-59]**
governs: regulation *caps* a franchise and *floors* a commodity business, and *"neither
creates the class."* Criterion 3 is not met for this segment's China business, and the
mechanism is the state, which no amount of engineering answers.

**THE CUSTOMER-CONCENTRATION TEST — AND IT DOES NOT REPRODUCE THE QCOM KILL. RECORDED AGAINST
MY OWN PRIOR, PER [E4-26].** The brief expected the QCT shape — a handful of hyperscalers all
building their own silicon. Across four filed vintages:

| filing | filed concentration |
|---|---|
| FY2021 10-K | *"Two customers, A and B, accounted for **14% and 11%**, respectively, of our consolidated net revenue"* |
| FY2022 10-K | **Customer A — GAMING segment — 16%** of consolidated revenue |
| FY2023 (per FY2024 10-K) | **Customer A — GAMING segment — 18%** of consolidated revenue |
| FY2024 10-K | one customer = **24% of consolidated accounts receivable**; no revenue customer ≥10% |
| **FY2025 10-K** | ***"No customer accounted for at least 10% of the Company's consolidated net revenue in fiscal years 2025 and 2024."*** One customer = **11%** of accounts receivable |

**AMD files NO 10%-of-revenue customer in FY2024 or FY2025, and the last one it did file was a
game-console maker, not a hyperscaler.** QCOM's Q2 was closed on the finding that *"the
concentration and the substitution are one fact"* — Apple, Samsung and Xiaomi were each 10%+
of revenue **and** each named as building the substitute. **At AMD the substitution is filed
and the concentration is not.** This is the single strongest filed fact against the verdict
below and it is recorded as such rather than argued away.

**The economics of the segment, filed.** Data Center revenue grew **+32%** in FY2025 while its
operating income grew **+3.5%** ($3,482M → $3,603M) and its margin fell **27.7% → 21.7%**.
Adding back the full $440M net MI308 charge still leaves margin at 24.3% and an incremental
margin of **13.8% against a 27.7% base** — the accelerator growth is dilutive to the segment
that already existed. H1 FY2026 recovers to **29.6%** on +81% revenue, against a prior-year
half that carried the $800M charge. **The margin series is 27.7% → 21.7% → 29.6%. It is not a
monotonic decline and I do not present it as one.**

### THE COMPETITOR ROW — required **[E3-28]**. Same metric, same window, filing-sourced.

**Metric: GAAP operating margin, most recent full fiscal year, each company's own 10-K.**

| Company | operating margin | revenue $M | R&D % rev | goodwill + intangibles % of assets | period | source |
|---|---|---|---|---|---|---|
| **AMD** | **10.7%** | **34,639** | **23.4%** | **54.4%** | FY2025 | 10-K `0000002488-26-000018` |
| **NVIDIA** | **60.4%** | **215,938** | 8.6% | 11.7% | FY to 2026-01-25 | 10-K, XBRL |
| **Broadcom** | 39.9% *(semiconductor segment **57.6%**)* | 63,887 | 17.2% | 76.0% | FY2025 | 10-K `0001730168-25-000121` |
| **Texas Instruments** | 34.1% | 17,682 | 11.8% | 12.5% | FY2025 | 10-K `0000097476-26-000059` |
| **Qualcomm** | 27.9% *(QCT **30.4%**, QTL 72.4%)* | 44,284 | 20.4% | 24.9% | FY2025 | 10-K `0000804328-25-000085` |
| **Marvell** | 16.1% | 8,195 | 25.3% | 57.5% | FY to 2026-01-31 | 10-K, XBRL |
| **Intel** | **−4.2%** | 52,853 | 26.1% | — | FY2025 | 10-K, XBRL |

**Peers named: 6 of the 6 real competitors AMD's own 10-K names across its three segments**
(Intel, Nvidia, Broadcom, Marvell, Texas Instruments, Qualcomm). Altera is also named and is
now privately held by Silver Lake and files nothing — **UNKNOWABLE, not UNRESEARCHED: no such
document is published anywhere**; Lattice at ~$500M of revenue is not a peer for a $780bn
market capitalisation. **The row is complete and is NOT PROVISIONAL.** QCOM, AVGO and TXN
figures are carried from the completed runs of 2026-09-02 and 2026-09-06 on the same metric
and window; INTC and NVDA and MRVL from their own filings.

**AMD is LAST among the profitable names in the row, at 10.7%, with the second-highest
goodwill-and-intangibles share of assets and the highest R&D intensity. The company it is
beating — Intel — has negative operating income. The company whose market it is entering —
Nvidia — earns 5.6× AMD's operating margin on 6.2× the revenue.** *(**[E3-61]** limits what
the row can show: it shows position, not conduct. It cannot tell me whether Nvidia will price
rationally, and the corpus says even Munger had no model for predicting that.)*

### THE REMAINING Q2 TESTS

- **[E4-04] — must the moat be continuously rebuilt? YES, and this is the excluded class.**
  AMD spends **23.4% of revenue on R&D**, the highest in the row, and what that R&D buys is a
  **replacement** for the last node, not a defence of the same asset. The framework's test:
  *does a lapse in spending destroy the structure, or merely narrow it — and does the spending
  defend the same advantage, or buy its replacement?* In leading-edge logic a two-year lapse
  is terminal, and the spending buys the replacement. **This is Mitsui's Rhodes Ridge, not
  Coca-Cola's trademark.**
- **[E4-36] — which of the four causes of extreme success is this?** Wave-riding. AMD's record
  from FY2017 is the clearest surfing run in this queue: it caught two waves it did not create
  — Intel's 10nm process failure and TSMC's process lead — and it rents the second of them.
  **Wave-riding is the one of the four that is not ownable.**
- **[E3-33] / [E5-28] — untapped pricing power? NO.** AMD raised Client ASPs 13% then 15% in
  consecutive years: **the power was tapped, not untapped.** And [E5-28] scopes the claim —
  *"a business that has incredible pricing power … is a monopoly or a near monopoly."* AMD is
  #2 in x86 CPUs, #2 in data-centre accelerators, #2 in discrete GPUs by its own filing, and
  contested in FPGAs. **The only market where AMD's own 10-K claims leadership is semi-custom
  game consoles** — inside the segment with the lowest margin in the company.
- **[E4-37] — the agony-pricing inverse metric.** Not answerable from the filing in either
  direction. No pricing-decision narrative is disclosed. Recorded as unavailable, not as a
  pass.
- **[E4-32] — direction.** Consolidated gross margin 44.9% → 46.1% → 49.4% → 49.5% and
  operating margin 5.4% → 1.8% → 7.4% → 10.7% are **improving, and I record that honestly.**
  But [E4-32] asks whether the *moat* widened, not whether profit rose — *"that does not
  necessarily mean that the profit is more this year than last year"*, and its converse binds
  equally. The segment evidence runs the other way: Embedded's margin is down 13.4 points,
  Client and Gaming's is down 3.6 points in the stub, and all the growth is concentrated in
  the segment where AMD is the challenger.
- **[E2-53] — the dominance class?** No. *"Once dominant, the newspaper itself, not the
  marketplace, determines just how good or how bad the paper will be. Good or bad, it will
  prosper."* AMD's economics are set by TSMC's roadmap, Nvidia's pricing, Intel's recovery or
  failure, and US export administration. **Position does not carry this business; execution
  does, every single year.**
- **[E3-46] — the second question about the business is a number.** Return on average equity:
  **47.4% (FY2021) · 4.2% · 1.5% · 2.9% · 7.2% (FY2025).** On the [E2-43] unleveraged
  net-tangible-asset denominator, with the goodwill wedge reported separately rather than
  hidden: **49.6% · 17.8% · 9.4% · 13.4% · 24.7%.** The goodwill-and-intangibles wedge is
  **$41,831M against $62,999M of book equity.** Neither series is the record of a business
  that *"earn[s] very high returns on capital employed over time."*
- **[E4-23] — key-person dependence, recorded HERE as a moat defect, not at Q3 as a
  compliment.** AMD's recovery from 2014 is inseparable from one CEO's tenure. *"If a business
  requires a superstar to produce great results, the business itself cannot be deemed great …
  The partnership's moat will go when the surgeon goes."*

### Q2 VERDICT

- Needed or desired **[x]** · no close substitute **[ ]** · not price-regulated **[ ]**
- **Class: [ ] WIDE [ ] NARROW [x] NONE (composite)** · **Direction: the profit mix is
  migrating OUT of the one segment with franchise economics and INTO the one where AMD is the
  challenger** — Embedded from 54.5% to 13.0% of segment operating income in two years.

**VERDICT: [x] OUT**

**In one sentence:** *AMD contains a franchise and is not one — the Embedded FPGA annuity
earns 36-49% operating margins on long design-in cycles, but its operating income has fallen
52.7% from its FY2023 peak while surrendering 13.4 points of margin through a 35% revenue
decline (the ACLS test, failed, on the one segment where it could be run), and it is now
13.0% of segment operating income; the 66.3% that is Data Center fails [E3-03](2) in the
10-K's own words — Nvidia is the leader AMD is attacking, at 60.4% operating margin against
AMD's 10.7%, and "some of our customers are internally developing their own … accelerator
products" — and fails [E3-03](3) on a filed $800M export-control charge and a 15% government
revenue share the filing says officials expect; and the whole enterprise rents its scarce
input from TSMC and must rebuild its advantage every node at 23.4% of revenue, which is
[E4-04]'s excluded class and [E3-51]'s surfing run.*

### THE STRONGEST FILED FACTS AGAINST THIS VERDICT — [E4-51], stated as its holders would state them

1. **The [E2-44] both-halves pass is real, and AMD filed it twice.** Units +34%/+31% with ASP
   +13%/+15% in consecutive years is a franchise signature, and I expected not to find it.
2. **There is no 10%-of-revenue customer in FY2024 or FY2025.** The QCOM kill does not
   reproduce. The concentration half of the QCT shape is filed **absent**.
3. **The consolidated direction is up on every headline metric** — gross margin, operating
   margin, revenue, and Data Center margin recovering to 29.6% in H1 FY2026.
4. **Embedded's H1 FY2026 is +20% on operating income and +2.5 points of margin.** If
   FY2023-25 was an inventory correction rather than an erosion, the ACLS finding reverses.
5. **Intel is dying and AMD is the only x86 alternative.** A duopoly reduced to one healthy
   participant is a stronger position than the row's margin column suggests.

**Why the verdict survives them.** (1) is one segment at 20.7% of profit whose operating
income is *falling* in the most recent filed half. (2) removes one leg of the QCT argument but
not the other — the substitution is filed regardless of the concentration, and the [E3-03](2)
failure here is against **Nvidia**, not against the customers. (3) is the wave, and [E4-32]
asks about the moat, not the profit. (4) is a possibility, and after three years Embedded
remains 53% below peak; the ACLS test is scored on what happened, not on what may. (5) is the
strongest of the five and it is the reason this file is not closed at Q1 — but a duopoly in
which the survivor earns a 10.7% operating margin while a third party (Nvidia) earns 60.4% in
the adjacent and larger market is a position, not a franchise, and **[E2-58]**'s equation
applies: *persistent over-capacity without administered prices equals poor profitability*, and
the leading-edge logic industry is adding capacity at record rates.

---
⛔ **Q3, Q4, Q5 AND Q6 DO NOT OPEN.** Q2 returned **OUT**. Operator rule 2: the hard sequence
is a block, and OUT is permanent — *"the evidence is here and the business fails."* What
follows is reported under **operator rule 3** because this queue's output contract requires a
price either way, and it carries **no entry language**.

---

# COMPUTATION — NOT A CLEARANCE

*(operator rule 3. Q1-Q4 did not all show IN. Nothing below is a valuation verdict, a
ranking, or a recommendation. It exists because the queue's contract says the operator gets a
number either way, and because the number is the same on every construction.)*

**Owner earnings, judged.** (c) = total capital expenditure (the conservative end, direction
established above). On the corpus-default five-year window FY2021-25: **$1,898M**. On the
post-Xilinx-only window FY2022-25: **$1,662M**. On the trailing twelve months to 2026-06-27:
**$5,841M**. **Judged for pricing: $5,841M**, the TTM — the single most generous multi-period
construction available, chosen deliberately so that the arithmetic below cannot be accused of
a stale window.

**1. THE YIELD**
- owner earnings **$5,841M** ÷ market cap **$779,621M** = **0.75%** · sovereign **5.24%**
- the full band across all eight windows and all three capex ends: **0.08% to 0.89%**

**2. WHAT THE PRICE ALREADY ASSUMES**
- To pay the 5.24% sovereign from **$5,841M** of owner earnings, the price would have to be
  **$111,470M — $68.28 a share.** The quote is $477.57.
- Perpetual growth in owner earnings required merely to **match** the 5.24% bond at this
  price: **4.49% a year, forever, with no terminal decline** (4.49% growth + 0.75% starting
  yield = 5.24%). To clear the **[E4-28] ~10% floor** the required perpetual growth is
  **9.25% a year, forever.**
- **[E4-35] is the governing base rate:** *"fewer than 10 of the 200 most profitable
  companies … will attain 15% annual growth in earnings-per-share over the next 20 years."*
  The required rate here is not 15% — but it is required **in perpetuity**, which is the
  harder claim, and **[E4-44]** bounds it: *"the value of an asset … cannot over the long
  term grow faster than its earnings do."*
- What the business has actually done: owner earnings of **$592M** on the pre-Xilinx
  five-year window and **$1,898M** on the corpus-default five-year window. **Revenue** has
  compounded **28.8% a year** FY2020-25 ($9,763M → $34,639M). **Consolidated operating
  income** has compounded **22.0%** over the same five years ($1,369M → $3,694M). **But
  measured from FY2021 instead of FY2020 — the [E4-38] test, publish every window rather than
  select the base year — consolidated operating income went $3,648M (FY2021) → $3,694M
  (FY2025): +1.3% in four years, on revenue that more than doubled.** Both windows are
  published because the corpus requires it; the second is the one that pays owners.

**3. WHAT YOU ARE PAID**
- **−4.49 percentage points against the sovereign** at the most generous construction.
- **−5.16 points** at the corpus-default five-year window.
- **There is no construction in this file that pays the bond.**

**THE FLOOR [E4-28].** Honest pre-tax expectancy at $477.57: **0.75% plus growth.** For the
floor of *"the figure we quit on"* to be met, this business must compound owner earnings at
roughly **9.2% a year forever** from a $5,841M base — and that is the arithmetic of the floor,
not a forecast. **Below the floor, the name is not ranked. It is quit on**, whatever the
sovereign is. It is also 4.49 points below the bond, so the two tests agree here and do not
have to be adjudicated.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — zero-growth capitalisations of the judged
owner-earnings band at the 5.24% sovereign, per share:

| construction | owner earnings | value/share at 5.24% |
|---|---|---|
| pre-Xilinx 5-yr anchor | $592M | **~$7** |
| corpus-default 5-yr FY2021-25 | $1,898M | **~$22** |
| FY2025 alone | $3,881M | **~$45** |
| **TTM to 2026-06-27 (most generous)** | **$5,841M** | **~$68** |
| TTM, depreciation end, absolute ceiling | $6,953M | **~$81** |

- **conservative ~$7-22 · judged ~$68 · optimistic ~$81 · CURRENT PRICE $477.57**
- **Even at the ceiling of the most generous construction, the price is 5.9× the value.**

**WHICH BAR:** **[x] Screamer test [E4-01]** — outcome three, *price above the whole range*.
No margin is added on top; none is needed, and adding one would be the second spend of
conservatism.
**Windage count: 1.** Conservatism was spent once, at the (c) judgment, and it was spent
**AGAINST** this conclusion: I judged (c) at total capex and then priced off the **TTM**, the
most generous multi-period construction in the file, which *raises* owner earnings by $3,943M
over the corpus-default window and *helps* the name. It still fails by 4.49 points.

---

# OBSERVATIONS BEYOND THE CLOSURE — NO VERDICT ATTACHES

*These tests belong to Q3 and Q4. **Q3 and Q4 did not open and no verdict is recorded for
them.** The work was commissioned in the run brief and is filed here as evidence for a future
re-open, exactly as the price above is. **Nothing in this section is a gate result, and none
of it may be read as promoting or condemning the name beyond the Q2 finding.*** [E2-37]'s
guardrail runs in both directions: a Q3 finding cannot repair Q2, and it cannot deepen a Q2
that has already closed.

**Cash taxes as a share of reported pretax income [E4-30] — the tell fires, and the filing
explains it.** Cash income taxes paid (supplemental cash-flow disclosure): **$523M (FY2023) ·
$1,386M (FY2024) · $884M (FY2025)** against reported pretax income of **$508M · $2,022M ·
$4,166M** — **103% → 68.5% → 21.2%.** The direction is the [E4-30] pattern. The mechanism is
disclosed and is not concealment: the reported tax **provision** is a *benefit* in FY2023
($(346)M) and FY2025 ($(103)M) on positive pretax income, driven by deferred taxes on the
Xilinx intangibles and the FY2022 GILTI accounting-method change (which the FY2022 10-K
quantifies: $857M of deferred tax liabilities recorded, $296M added to FY2022 net income,
$0.19 of EPS). **A prompt to read, read, and the reading found a disclosed cause — not a
verdict [E5-36, E5-38].**

**EBITDA and adjusted-earnings promotion [E4-29] — the 10-K is clean and the PROXY is not.**
Term counts: *"EBITDA"* **0** in the FY2025 10-K and **0** in the 2026 proxy; *"non-GAAP"*
**0** in the 10-K and **28** in the proxy (`0001193125-26-129057`, filed 2026-03-27).
**AMD's company-selected measure in its Pay Versus Performance table is Non-GAAP Net Income:
$6,831M against GAAP net income of $4,335M — a 57.6% uplift**, and the difference is
substantially the acquired-intangible amortisation and stock compensation that the All Other
segment carries. The charge that consumes 52% of segment operating income is the charge the
pay metric removes.

**Pay versus performance — and AMD's own filed table says it has underperformed its peers.**
From the same proxy, FY2025: CEO Summary Compensation Table total **$55,161,779**;
**Compensation Actually Paid to CEO $146,727,337** (2.7×); average non-CEO NEO SCT
$15,633,139, CAP $44,925,524. FY2024 CAP to CEO was **$(18,654,655)** — negative — on an SCT
of $30,996,392, so the measure is genuinely mark-to-market in both directions. **Value of an
initial fixed $100 investment: AMD $234 against the peer group's $547.** That is AMD's own
disclosure that its shareholders received less than half the peer-group return over the
measurement period. EIP payout for FY2025: **121% of target.**

**[E4-52] — the lollapalooza test. Do the flags converge?** Four observations point one way:
(i) a pay metric that deletes the amortisation and SBC consuming 52% of segment profit;
(ii) $3,163M of buybacks over three years during which the share count **rose** every year;
(iii) a $48.8bn all-stock acquisition invisible to every cash-flow test; (iv) segment
operating income of $7,701M reported alongside consolidated operating income of $3,694M.
**They are not independent — they are one system, and its name is purchase accounting.**
Recorded as a convergence, not as a conduct finding: **[E5-38]** — a fired flag is not a
venality finding, and **[E2-30]** governs — *"institutional dynamics, not venality or
stupidity."*

**[E5-11] staying power — scored, without a Q4 verdict.**
1. *A large and reliable stream of earnings* — **large, not reliable.** Consolidated operating
   income across the last five filed years: $3,648M · $1,264M · $401M · $1,900M · $3,694M.
   The 2023 trough is 11% of the 2021 peak.
2. *Massive liquid assets* — **$5,539M of cash and equivalents plus $5,013M of short-term
   investments = $10,552M**, against total debt of **$3,222M** ($874M current + $2,348M
   long-term) and interest paid of **$91M**. Net cash of $7,330M. **[E2-54]**'s coverage test
   passes with enormous room: interest of $91M against $6,493M of continuing-operations
   operating cash flow net of $974M of capex.
3. ***No significant near-term cash requirements* — THIS IS THE ONE THAT IS NOT CLEAN.** The
   FY2025 10-K discloses **$12,166M of total unconditional commitments, of which $8,498M fall
   in fiscal 2026** — wafer and substrate purchases plus *"multi-year cloud service provider
   (CSP), software, and technology license agreements."* **$8,498M due inside twelve months
   against $10,552M of cash and short-term investments.** Plus **$1.3bn of leases that have
   commenced or not yet commenced** ($940M commenced, $1.3bn not yet). The wafer half is
   ordinary for a fabless filer and converts to inventory and then revenue; the CSP half does
   not — AMD is prepaying for cloud capacity it says *"may be reduced, terminated or sold to
   others by the CSPs."* **[E5-39]:** *"cash is a lot like oxygen"* — this is the strength
   that would be tested first, and it is the one the corpus says is most often skipped.

**[E2-60] — restricted earnings and the third dimension of maintenance.** Does not fire in the
payout form: **AMD pays no dividend**, so no earnings are being distributed at the cost of
financial strength. It fires weakly in the **buyback** form — $3,163M returned over three
years while $2,441M of new debt was issued in FY2025 — but AMD's net cash position of $7,330M
means the capital structure did not deteriorate. **Recorded as not firing.**

**ASC 842 — leases.** Operating lease expense **$196M (FY2025)**, $147M, $127M, plus variable
lease expense of $100M/$83M/$46M; cash paid for operating leases $176M/$155M/$147M. Balance
sheet: long-term operating lease liabilities **$625M**; ROU assets sit inside other non-current
assets. **Weighted-average remaining term 6.95 years (from 7.28); weighted-average discount
rate 4.74% (from 4.63%).** Leases expire *"at various dates through 2038."* Finance and
short-term leases are stated to be immaterial. **No off-balance-sheet lease problem; the only
lease item of size is the $1.3bn of not-yet-commenced leases, which is a Strength-3 item and is
carried above, not here.**

**Software-capex line — the answer is that there is no line, and the absence is the finding.**
The FY2025 10-K discloses **no internal-use-software or software-development capitalisation
policy** and no such line in investing activities. The $229M gap between the cash-flow
"Depreciation and amortization" line ($750M) and separately-tagged Depreciation ($521M) is
amortisation of purchased technology licences and other non-acquired intangibles, not
capitalised internal development. **AMD's software spending — and the 10-K devotes a full
paragraph of the R&D section to it (*"design automation tools for hardware, embedded software,
AI stack, and optimized software tools and libraries"*) — runs through R&D expense, above the
OCF line.** This *strengthens* the (c) ruling above: there is no capitalised-software channel
through which renewal spending could be hiding below the line.

**Contingent-liability persistence.** FY2025 10-K, Note 12: ***"As of December 27, 2025, there
were no material legal proceedings."*** No recurring accrual, no reserve-development pattern,
nothing to track across vintages. Warranty is the only accrued contingency of substance and is
immaterial to the file. **Nothing persists; the test returns empty.**

**[E5-15] serial share issuance.** Shares outstanding 1,617M → 1,622M → 1,630M → 1,632M is a
slow drift, not serial issuance. **But the 429 million shares issued for Xilinx in a single
morning — 26.3% of the current count — is the only issuance that matters in this file**, and
it is carried at the perimeter section under **[E5-44]**, not here.

**[E2-49] metric-switching.** One switch is on the record and it is **announced with a stated
reason and prior periods retrospectively adjusted**: *"Beginning in the first quarter of fiscal
year 2025, we combined the Client and Gaming segments into one reportable segment to align
with how we manage our business. All prior period segment data were retrospectively adjusted."*
The combination merged a **rising** margin (Client) with a **falling** one (Gaming) and
therefore reduces visibility — but it was disclosed ahead, restated backwards, and both
sub-lines are still given in the FY2025 revenue table. **[E2-49] asks whether the yardstick was
disposed of *after* deterioration; here it was not, and the candour case applies.** Recorded as
NOT firing, against my expectation.

---
## SELF-AUDIT

- [x] Questions answered in order; no verdict skipped; **stopped at the first non-IN verdict**
- [x] No question marked IN carries an "unverified" or "provisional" caveat — Q1 is the only
      IN, and it rests on the read filing
- [x] The OUT verdict is about the **business**, is evidenced from the filing, and names the
      criteria it fails ([E3-03](2) and (3), [E4-04])
- [x] Step 0: the filing was read, with accession numbers; **two figures cross-checked against
      the filed statement, and both cross-checks found the tagged data wrong** (rounded
      amortisation; discontinued-operations cash in OCF)
- [x] Owner earnings on multi-year means; **eight windows shown, not one defended**; capex band
      disclosed as a judgment **with its direction named (capex end = conservative; the
      opposite of AVGO's inversion)**
- [x] Competitor row filled with 6 named peers on one metric and one window; the one
      unobtainable peer (Altera) recorded **UNKNOWABLE**, not UNRESEARCHED; **moat is NOT
      marked provisional**
- [x] Sovereign is for the earnings currency, from the issuing authority, dated
- [x] Value stated as a round-number range, not a point estimate
- [x] One bar chosen; **windage count stated (1), and its direction stated (against the
      conclusion)**
- [x] Price dated; aggregator used for the live quote only and flagged
- [x] **The perimeter break is named, quantified, and its invisibility to `acquisition_flag()`
      explained** — a $48.8bn all-stock deal inside every window
- [x] **[E4-26] discharged: the two filed facts that most damage this conclusion — the
      [E2-44] both-halves pass and the absent 10% customer — are recorded at full strength,
      before the rebuttal, not after it**
- [x] **[E2-45] noted: this run is INTC's attacker of record in the parallel run, and the
      attack developed here (Intel's own filed operating losses of $(11,678)M and $(2,214)M)
      is evidence FOR AMD's position and is recorded that way**
- [x] **The Q3/Q4 material commissioned in the brief is filed BELOW the closure line, labelled
      as carrying no verdict, and the hard sequence is preserved: no Q3, Q4, Q5 or Q6 verdict
      appears anywhere in this file** (operator rule 2)
- [x] Run committed to git

## KNOWN DEFECTS IN THIS RUN — stated, not buried

1. **Xilinx's standalone 10-Ks (CIK 743988) were not pulled.** The pro-forma question was
   answered by running the window both ways and showing the direction, which is sufficient at
   a 0.75% yield but is **not** the full pro-forma build the brief contemplated. Quantified:
   the FY2021 term moves by roughly $1bn of operating cash flow, worth under 15bp of yield.
   **If this file is ever re-opened at a materially lower price, this is the first work order.**
2. **The FY2023 segment revenue figures are DERIVED**, not read off a revenue row — the FY2024
   10-K's three-year segment table gives FY2023 cost-and-expense and operating-income rows,
   from which revenue is the sum. They reconcile exactly to the filed $22,680M total, but they
   are one arithmetic step from the filing rather than zero.
3. **The x86 share trajectory could not be established from AMD's filings and I did not pull
   third-party share data**, because the evidence ladder's rungs above "aggregator" were
   exhausted: AMD files no share figure in any vintage. The substitute used — Intel's own
   filed revenue and operating-income decline — answers the *direction* but not the *level*.
4. **[E4-37]'s agony-pricing metric is unavailable in either direction** and is recorded as
   unavailable rather than scored.
5. **The competitor row's NVDA, MRVL and INTC lines come from XBRL rather than from a read
   filing.** Operator rule 4 binds the *subject*, not the row, and the AVGO and QCOM runs
   sourced theirs the same way — but the row is screening-grade, not filing-grade, for those
   three names, and the AMD, AVGO, TXN and QCOM lines are filing-grade.
6. **Data Center's H1 FY2026 margin recovery to 29.6% is one half-year.** If it holds for two
   more, the [E3-03](2) finding stands but the economics argument beneath it weakens
   materially. That is the strongest single re-open trigger in the file.

## REGISTER

- **Verdict: [x] OUT (about the business)** — closed at **Q2**.
- **One line:** *AMD's franchise-shaped segment is 13% of its profit and its operating income
  has halved in three years; the 66% that is Data Center is a challenger to a 60.4%-margin
  incumbent, on wafers it rents, with its customers' own accelerators named as a substitute in
  its own 10-K and a 15% government revenue share expected on its largest growth market.*
- **PRICE: $477.57** (2026-09-04, aggregator, flagged). **Value range ~$7 to ~$81 per share;
  judged ~$68.**
- **FAIL. The file closed at Q2 (OUT). Q1 IN. Q3, Q4, Q5 and Q6 did not open.**
