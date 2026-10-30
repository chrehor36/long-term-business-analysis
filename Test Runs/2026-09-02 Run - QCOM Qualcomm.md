# Company Run — QUALCOMM INCORPORATED (QCOM) — 2026-09-02
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**RESULT IN ONE LINE: the file closes at Q2. Qualcomm contains a franchise and is not one —
QTL is a genuine toll gate with a published expiry schedule (fiscal 2027–2031) and 12.6% of
revenue; the 87% that is QCT fails the no-close-substitute test in its own 10-K's words.**
The price is reported below under operator rule 3 as **COMPUTATION — NOT A CLEARANCE**:
**roughly $100 to $155 a share, judged ~$100, against a quote of $169.43.**

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
- **rate 5.27%** · **date 2026-09-01** (the latest published row) · source: **U.S.
  Department of the Treasury, Daily Treasury Par Yield Curve Rates, 30-year**, from the
  issuing authority at `home.treasury.gov`, fetched 2026-09-02.
- Neighbouring prints, so the choice is visible: 5.25% (08-31), 5.22% (08-28), 5.19%
  (08-27), **5.18% (08-26 — the rate the screen used)**.
- `tools/sources.py` returned `USD FAILED: The read operation timed out` on its FRED path.
  FRED is the **fallback** under `CLAUDE.md` as corrected 2026-09-02; the issuing authority
  was used, which is UP the evidence ladder.
- **Earnings currency: USD.** The filer reports in USD and pays its shareholders in USD.
  It is worth recording that **only 24% of FY2025 revenue was booked to US-headquartered
  customers** (Note 8: China 46%, US 24%, South Korea 21%, other foreign 9%) — but revenue
  is reported by *licensee headquarters*, the receipts are USD-denominated, and the USD
  sovereign is the right yardstick. The geographic exposure is adjudicated at Q4, not by
  switching the rate.
- FX / ADR ratio: **not applicable** — domestic filer, ordinary shares on Nasdaq.

**The filing was read** — not tagged data **[E3-27]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes (Notes 1, 2, 3, 5, 6,
  7, 8, 9, 10, 12, and the commitments-and-contingencies note)  [x] Item 1 Business,
  Item 1A Risk Factors, Item 3 Legal Proceedings
- **document · date · accession no.: Form 10-K for the fiscal year ended 2025-09-28 ·
  filed 2025-11-05 · accession `0000804328-25-000085` · primary document
  `qcom-20250928.htm`.**
- Also read: **Form 10-Q for the quarter ended 2026-06-28, filed 2026-07-29, accession
  `0000804328-26-000086`** — the most recent periodic filing in existence at this run date.
- **Figure cross-checked against the filed statement:** *Capital expenditures* in the
  Consolidated Statements of Cash Flows reads **$1,192M** (FY2025), **$1,041M** (FY2024),
  **$1,450M** (FY2023). SEC companyfacts `PaymentsToAcquireProductiveAssets` returns
  1,192 / 1,041 / 1,450. **They agree.** Second cross-check: filed *Net cash provided by
  operating activities* **$14,012M** (FY2025) against companyfacts 14,012. Agree. Third:
  the Note 8 segment table's QTL EBT of **$4,043M** was read off the filed note itself,
  not from tagged data.

---
# STAGE 0 — ARTIFACT CHECK

## Stage 0(a) — THE SHARE COUNT, BY HAND FROM THE COVER PAGE

*This check is here because the screen counts one share class and has been wrong twice.*

- **QCOM has ONE class of stock.** 10-K cover, Securities registered pursuant to Section
  12(b): *"Common stock, $0.0001 par value | QCOM | The Nasdaq Stock Market LLC"*.
  Securities registered pursuant to Section 12(g): *"None"*. **No dual-class artifact
  exists here.** This is a clean case and it is stated as one.
- **Cover-page counts, both read by hand:**
  - 10-K cover: *"The number of shares outstanding of the registrant's common stock was
    **1,071 million at November 3, 2025**."*
  - **10-Q cover (Q3 FY2026, the current one): *"The number of shares outstanding of the
    registrant's common stock was **1,050 million at July 27, 2026**."***
- **Live quote: $169.43, 2026-09-02** — *aggregator, flagged as such per operator rule 5;
  quotes are the one permitted aggregator use.*
- **MARKET CAP, BY HAND: 1,050M × $169.43 = $177,902M.**
- **The screen's $172,263M is 3.2% low** — it is a stale-share-count effect of the same
  family as the Nike error, though far smaller here. **The hand figure $177,902M is used
  throughout, and it moves every yield DOWN, i.e. against the name.** No verdict turns on
  the 3.2%.

## Stage 0(b) — THE SCREEN'S NINE-YEAR SERIES, RECOMPUTED FROM THE FILED CASH FLOWS

Construction: **operating cash flow − share-based compensation − capital expenditures**,
$M, from the filed consolidated statements of cash flows.

| FY (end) | OCF | SBC | capex | **filed OE** | **screen** | D&A |
|---|---|---|---|---|---|---|
| 2017 (09-24) | 4,693 | 914 | 690 | **3,089** | 3,089 | 1,461 |
| 2018 (09-30) | 3,895 | 883 | 784 | **2,228** | 2,228 | 1,561 |
| 2019 (09-29) | 7,286 | 1,037 | 887 | **5,362** | 5,362 | 1,401 |
| 2020 (09-27) | 5,814 | 1,212 | 1,407 | **3,195** | 3,195 | 1,393 |
| 2021 (09-26) | 10,536 | 1,663 | 1,888 | **6,985** | 6,985 | 1,582 |
| 2022 (09-25) | 9,096 | 2,031 | 2,262 | **4,803** | 4,803 | 1,762 |
| 2023 (09-24) | 11,299 | 2,484 | 1,450 | **7,365** | 7,365 | 1,809 |
| 2024 (09-29) | 12,202 | 2,648 | 1,041 | **8,513** | 8,513 | 1,706 |
| 2025 (09-28) | 14,012 | 2,783 | 1,192 | **10,037** | 10,037 | 1,602 |

**All nine years reconcile to the dollar. The screen is clean on this name.**
*(FY2017 and FY2018 OCF each carry a second tagged value — 5,001 and 3,908 — from a later
reclassification. The screen used the as-first-filed figures and so does this run; the
alternative moves FY2017 by +$308M and FY2018 by +$13M and moves no verdict.)*

**The screen's $7,415M bottom boundary is reproduced exactly.** It is the five-year
(FY2021–25) mean of **OCF − SBC − D&A**: 7,291 / 5,303 / 7,006 / 7,848 / 9,627 → **7,415.0**.
Its 4.30% yield is against the screen's $172,263M cap; **on the hand-built $177,902M cap the
same figure yields 4.17%.**

## Stage 0(c) — WHICH END OF THE CAPEX BAND IS THE CONSERVATIVE ONE

**capex/D&A = 0.813x** on nine-year means ($1,289.0M capex against $1,586.3M D&A). The
operator's 0.81x is confirmed from the filings.

**Therefore the D&A end is the LOW end here, and this is the reverse of the usual case.**
The framework's default is that D&A *is* the guess for (c) **[E3-44, E2-41]**, and its
exception class **[E5-20]** — railroads, airlines, "anything whose own filing says
depreciation understates renewal" — is the class where the D&A end is *too generous* and is
struck. **Qualcomm is not in that class**, and the direction is stated rather than assumed:
because Qualcomm spends **less** on plant than it charges to depreciation, using D&A as (c)
produces the **lower** owner-earnings figure. The [E3-44] default and the conservative end
happen to coincide, which is convenient and is recorded as coincidence, not as a finding.
The reason D&A exceeds capex is adjudicated at Q4: Qualcomm is fab-less, its D&A carries
**acquired-intangible amortization**, and its real reinvestment is R&D, which is already
expensed above the OCF line.

## Stage 0(d) — THE BOOM TEST, AND THE THREE TESTS RUN AGAINST IT

**The operator's flag is CONFIRMED, on both constructions.**

| | earlier six (FY17–22) | recent three (FY23–25) | level_shift |
|---|---|---|---|
| capex end | **4,277.0** | **8,638.3** | **2.02x** |
| D&A end | 4,070.0 | 8,160.3 | 2.00x |

The operator's 4,277 / 8,638 / 2.02 are reproduced to the dollar. **[E4-41] applies:
*"normalize the mean DOWN for luck"* — favourable exogenous breaks in the window are named
and removed before the mean is trusted.** What the break was is established at Q2 and Q4.

**TEST 1 — every window published [E4-38], because *"growth-rate presentations can be
significantly distorted by a calculated selection of either initial or terminal dates."***
Cap $177,902M, sovereign 5.27%.

| window | mean(OCF−SBC) | **OE, (c)=D&A** | **OE, (c)=capex** | yield (D&A) | yield (capex) | **g for the [E4-28] 10% floor** |
|---|---|---|---|---|---|---|
| 3-yr FY23–25 | 9,866.0 | **8,160.3** | **8,638.3** | 4.59% | 4.86% | 5.14–5.41% |
| **5-yr FY21–25 — the [E2-42] default** | 9,107.2 | **7,415.0** | **7,540.6** | **4.17%** | **4.24%** | **5.76–5.83%** |
| 7-yr FY19–25 | 8,055.3 | **6,447.4** | **6,608.6** | 3.62% | 3.71% | 6.29–6.38% |
| 9-yr FY17–25 — full cycle | 7,019.8 | **5,433.4** | **5,730.8** | 3.05% | 3.22% | 6.78–6.95% |

- **Eight constructions run from $5,433M to $8,638M — a width of 59.0%, not 16%.**
  The screen's 16% is the distance from one corner (5-yr D&A) to another (3-yr capex) and
  it understates the true spread by nearly four times. **The width belongs in the open
  [E4-25], and the AEO caution — that five windows can cluster tightly and disconfirm the
  flag — was tested here and does NOT hold. QCOM's windows do not cluster.**
- **Every one of the eight constructions yields BELOW the 5.27% sovereign.** The top of the
  entire range, 4.86%, is 41 basis points under the government bond.

**TEST 2 — best_year_dependence, leave-one-out on the maximum (FY2025 = $10,037M).**
Every window in the table above contains FY2025, which is exactly the Nike failure mode.
Recomputed with FY2025 removed:

| window (FY2025 excluded) | OE, (c)=D&A | OE, (c)=capex | change vs the window that includes it |
|---|---|---|---|
| 3-yr FY22–24 | 6,719.0 | 6,893.7 | **−17.7% / −20.2%** |
| **5-yr FY20–24** | **6,131.4** | 6,172.2 | **−17.3% / −18.1%** |
| 7-yr FY18–24 | 5,279.4 | 5,493.0 | −18.1% / −16.9% |
| 8-yr FY17–24 | 4,909.2 | 5,192.5 | — |

**The dependence is real: dropping the single best year takes the five-year default down
17.3%, from $7,415M to $6,131M, a yield of 3.45%.** It is not, however, Nike's pathology —
Nike's ten constructions clustered inside 17% *because* every window held the best year, and
the first window excluding it fell 43%. **Here the full window set is already 59% wide with
the best year in it, and removing it moves the whole set down by roughly a sixth rather than
collapsing it.** The width was never being hidden. Both findings are carried.

**TEST 3 — is the step a boom or a level change?** The step is 2.02x and it is
**concentrated in the last three years**, which are also the three years in which the
disclosed customer mix changed. This is the question Q2 has to answer, and the answer
determines whether the recent-three mean or the nine-year mean is the honest one. It is
answered there, from the filing, not here.

**NOTHING ABOVE IS A CLEARANCE.** All of Stage 0 is transcription and arithmetic; under
operator rule 3 no valuation language attaches to it until Q1–Q4 have each returned IN.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, without management's language. There are two businesses
and they have nothing to do with each other except the laboratory that feeds them both.**

**QTL is a toll gate.** Qualcomm invented enough of the mathematics of digital cellular that
its patents were written into the 3G, 4G and 5G standards. A standard is a rulebook everyone
must obey to interoperate, so a patent that is *essential* to the standard cannot be designed
around — it can only be licensed or infringed. Qualcomm therefore charges a percentage of the
**selling price of the finished handset**, not of the chip inside it, to essentially every
phone maker on earth, including the ones that buy no Qualcomm silicon at all. The cost of
collecting this is $1,539M against $5,582M of revenue. There is no factory, no inventory and
no working capital. **It is the closest thing to a pure economic rent in the S&P 500.**

**QCT is a fabless chip shop.** It designs the modem and the system-on-chip that go into
Android phones, cars and connected devices, has TSMC and Samsung build them, and sells them
to about a dozen device makers. It charges per part. It carries inventory, it competes on
performance per watt every product cycle, and its customers hold the whip.

**The scarce input this business controls.** For QTL it is precise and nameable: **the
standard-essential patent estate in cellular, plus the seat in the standards bodies where the
next generation's essentials are decided.** For QCT there is no scarce input Qualcomm
controls — it buys its wafers from two foundries, its CPU architecture is licensed from Arm
(litigated, below), and its EDA tools are the same ones its rivals use. **QCT's advantage is
a design lead, which is a lead, not a scarcity.**

**Will the fundamentals look broadly the same in ten years?** The *mechanism* — a royalty on
cellular devices and a chip sold into them — yes; it has been the mechanism for thirty years
and cellular standards will exist in 2036. **The parties and the rates will not be the same,
and the filing gives the dates: every material licence expires between fiscal 2027 and
fiscal 2031.** That is a Q2 matter and it is adjudicated there, because **[E3-42]** locates
certainty at the understanding gate and again in the end discount, not spread across every
question: *"You better just stick with businesses that you can understand, use the government
bond rate."*

**Recorded against myself under [E4-26] and operator rule 9.** There is a real case that this
gate should fail. **[E3-31]** asks for businesses *"relatively simple and stable in
character"* and warns *"If a business is complex or subject to constant change, we're not
smart enough to predict future cash flows."* A modem SoC is re-architected every eighteen
months and a patent estate must be re-created every generation; "subject to constant change"
is a fair description of both. **I am marking this IN on the narrow ground that I can write
the money-making mechanism in two paragraphs without using management's words, and I can.**
What I cannot predict is the *level*, and the framework's own structure puts that at Q4's
range and Q5's conservative end **[E5-34]**, not here. **The dissent is recorded rather than
resolved in the name's favour.**

- **VERDICT: [x] IN**

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that "(1) is needed or desired; (2) is thought by its
> customers to have **no close substitute** and; (3) is not subject to price regulation."
> — **[E3-03]**

**THE TWO BUSINESSES MUST BE TESTED SEPARATELY, BECAUSE THEY GIVE OPPOSITE ANSWERS.**

### The separation, from the filed segment notes ($M)

| FY | **QTL rev** | **QTL EBT** | QTL margin | **QCT rev** | **QCT EBT** | QCT margin |
|---|---|---|---|---|---|---|
| 2016 | **7,664** | **6,528** | **85%** | 15,409 | 1,812 | 12% |
| 2017 | 6,445 | 5,175 | 80% | 16,479 | 2,747 | 17% |
| 2018 | 5,163 | 3,525 | 68% | 17,282 | 2,966 | 17% |
| 2019 | 4,591 | 2,954 | 64% | 14,639 | 2,143 | 15% |
| 2020 | 5,028 | 3,442 | 68% | 16,493 | 2,763 | 17% |
| 2021 | 6,320 | 4,627 | 73% | 27,019 | 7,763 | 29% |
| 2022 | 6,358 | 4,628 | 73% | **37,677** | **12,837** | **34%** |
| 2023 | 5,306 | 3,628 | 68% | 30,382 | 7,924 | 26% |
| 2024 | 5,572 | 4,027 | 72% | 33,196 | 9,527 | 29% |
| **2025** | **5,582** | **4,043** | **72%** | **38,367** | **11,670** | **30%** |
| 9M 2026 | 4,252 | 3,105 | 73% | 28,193 | 7,959 | **28%** |
| *Q3 2026 alone* | *1,278* | *881* | *69%* | *8,504* | *2,192* | ***26%*** |

*Sources: FY2018 10-K (acc. 0001728949-18-000095) for FY2016–18; FY2020 10-K
(0001728949-20-000067) for FY2019–20; FY2022 10-K (0000804328-22-000021) for FY2021–22;
FY2025 10-K (0000804328-25-000085) Note 8 for FY2023–25; Q3 FY2026 10-Q
(0000804328-26-000086) for the stub. FY2018 QTL is shown as first filed ($5,163M); the
FY2020 10-K restates it to $5,042M for the revenue-recognition change. Both are published
here rather than the more convenient one **[E4-38]**.*

**THE FIRST THING THIS TABLE SAYS, AND IT REVERSES THE OBVIOUS READING OF THE BOOM.**
**The 2.02x owner-earnings step-up is entirely QCT, and QTL — the franchise — did not
participate in it.** QCT EBT went from $1.8–3.0bn (FY2016–20) to $11.7–12.8bn. QTL EBT went
from **$6,528M in FY2016 to $4,043M in FY2025 — down 38.1%.** The boom happened in the
business with no moat, and the business with the moat got smaller. That single fact
organises the whole of Q2.

**FY2025 shares of the whole: QTL is 12.6% of revenue and 25.4% of reportable-segment EBT.
QCT is 86.6% of revenue and 73.4% of segment EBT.**

---
### QTL against [E3-03] — a franchise, and I will say so plainly

- **(1) Needed or desired — PASSES, absolutely.** No cellular device is lawfully sold
  without a licence to the standard-essential portfolio. The 10-K's own claim is
  *"the mobile communications industry generally recognizes that **any company seeking to
  develop, manufacture and/or sell certain cellular products requires a license or other
  rights to use our patents**"* and *"Our patent portfolio is the most widely and extensively
  licensed in the industry."*
- **(2) No close substitute — PASSES, in the strongest form the criterion has.** A
  standard-essential patent is not merely hard to substitute; substituting it is *unlawful*.
  This is a better answer than Coca-Cola gives.
- **(3) Not subject to price regulation — FAILS, and the filing itself supplies the
  evidence.** Qualcomm's SEPs carry FRAND commitments, which are a *contractual undertaking
  to be price-constrained*, enforceable by courts and by competition authorities, and the
  10-K lists the remedies it is exposed to: *"**requiring us to reduce our royalty rates,
  reduce the base on which our royalties are calculated, grant patent licenses to chipset
  manufacturers** or other component suppliers, sell chipsets to unlicensed OEMs or modify or
  renegotiate some or all of our existing license agreements; and **determinations that some
  or all of our license agreements are invalid or unenforceable**."* **[E2-59]** is exact on
  what this means: administered pricing *floors* a commodity business and *caps* a franchise,
  and *"neither creates the class."* Here the regime caps. **Criterion 3 fails, and it is the
  only one of the three that does.**

### QTL against [E4-04] — and THIS is the operator's question, answered with a date

> "A moat that must be **continuously rebuilt** will eventually be no moat at all."
> — **[E4-04]**

The framework's own scoping test: **"does a lapse in spending destroy the structure, or
merely narrow it — and does the spending defend the same advantage, or buy its
replacement?"** *(Mitsui's Rhodes Ridge buys a replacement deposit; Coca-Cola's advertising
defends the same trademark.)*

**A patent estate buys its replacement. Not as a matter of judgment — as a matter of
statute.** Every patent expires twenty years from filing. The 3G essentials are gone. The
4G essentials are going. To collect a royalty in 2045 Qualcomm must have already invented
and patented the 6G essentials. **Qualcomm's $9,042M of FY2025 R&D — 20.4% of revenue — is
Rhodes Ridge, not the Coca-Cola trademark.** A trademark renews indefinitely for a filing
fee; a patent cannot be renewed at any price. **QTL is in [E4-04]'s excluded class by legal
construction, and it is the clearest instance of that class this project has run.**

**THE EXPIRY, PRECISELY, AS THE OPERATOR ASKED.** FY2025 10-K, Note 2, verbatim:

> "Our patent license agreements with key OEMs are generally long-term, **with terms expiring
> at varying dates between fiscal 2027 and 2031**. We generally seek to renew or renegotiate
> such license agreements prior to expiration."

**So the durability of this moat is a schedule, and the schedule is: every material licence
Qualcomm holds expires within the next two to six fiscal years — the first of them within
twelve to fifteen months of this run date.** The risk factor states what happens then:

> "**We might not be able to extend or modify such license agreements, or enter into new
> license agreements, without negatively affecting the material terms and conditions** of our
> license agreements with such licensees… certain of our license agreements contain binding
> renewal provisions which provide that if the parties are unable to agree… **either party
> may initiate binding arbitration**… **we may not be able to recognize some or any revenues
> related to that licensee's product sales until such new license agreement is finalized.**"

**AND THE RENEWAL RECORD IS ALREADY ON THE FILE, IN THE MOST RECENT CYCLE, AND IT IS BAD.**
- **A licensee expired and produced nothing:** *"Beginning in the second quarter of fiscal
  2025, **QTL revenues did not include royalties from Huawei, whose license agreement has
  expired.**"* Huawei is one of the largest handset makers on earth. The agreement reached
  its term and was not replaced.
- **Two renewals produced flat revenue:** *"we executed final agreements for new long-term
  licenses with **two key Chinese OEMs (for which the initial terms had expired)**"* — and
  QTL revenue in that year moved from $5,572M to $5,582M, **+0.2%**, in a year when QCT
  handset revenue rose 11.8% on the same industry's units.

**That is the answer to "if QTL is the franchise and it is time-limited, say so precisely."
It is a franchise. Its term is fiscal 2027 to fiscal 2031. Its most recent renewal cycle
lost one licensee outright and re-signed two others for no increase.**

### QTL's direction — [E4-32], and the disconfirming reading is given first [E4-26]

> the moat *widened every year* is *"the primary criterion of a great business"* — **[E4-32]**

**THE FACT THAT CUTS FOR QUALCOMM, AND IT IS REAL.** The collapse from 85% margins and
$6,528M of EBT happened in **FY2016–FY2019**, during the Apple withholding and the
four-regulator assault. **Since FY2020 QTL has been flat-to-firm, not shrinking**: EBT
$3,442 → $4,627 → $4,628 → $3,628 → $4,027 → **$4,043M**, margin 68 → 73 → 73 → 68 → 72 →
**72%**, and 9M FY2026 revenue is **up 1.9%** year on year. **QTL absorbed the loss of Huawei
and stayed flat.** I expected to find a business in decline and over the last five years I
did not find one. That is stated first because **[E4-51]** requires the case against my
position be put better than its holders would put it.

**WHY IT DOES NOT CARRY THE GATE.** *"That does not necessarily mean that the profit is more
this year than last year"* — but nine years of flat-at-a-lower-level is not a widening moat
either, and **[E4-32]**'s criterion is widening. QTL EBT is **38.1% below its FY2016 peak**
and has not recovered in six years. **The structural repricing was permanent and the filing
never claims it will reverse.**

### [E4-55] — where units exist, monitor units. **QUALCOMM STOPPED PUBLISHING THEM.**

> Precision Steel's pounds fell 69M → 46M while price rises held dollar revenue level — *"a
> serious reverse, not likely to disappear in some 'bounce back' effect."* **Dollar revenue
> flattered by pricing is how a shrinking franchise hides; the physical series is the honest
> one.** — **[E4-55]**

The FY2020 10-K, verbatim, is the whole of this point:

> "**Approximately 575 million, 650 million and 855 million MSM integrated circuits were sold
> during fiscal 2020, 2019 and 2018, respectively.** Through fiscal 2020, we provided the
> volume of MSM integrated circuit shipments to allow management and investors to, in part,
> evaluate, assess and benchmark our QCT segment's performance. **Beginning in fiscal 2021,
> we will no longer provide MSM integrated circuit shipments since such measure is becoming
> increasingly less meaningful**…"

**Units fell 855M → 650M → 575M — down 32.7% in two years — and the disclosure was then
withdrawn.** The count for FY2016–18 was 842M / 804M / 855M, so the withdrawal came
immediately after the only sustained decline in the series. **This is [E4-55] and
[E2-49] firing together** — *"Yardsticks seldom are discarded while yielding favorable
readings. But when results deteriorate, most managers favor **disposition of the yardstick
rather than disposition of the manager**."* It is recorded here at Q2, where the moat metric
lives, and again at Q3 as a disclosure flag. **There is no physical series in the FY2025
10-K for either segment.** QTL's unit driver is disclosed only as a year-on-year *delta*
("$299 million decrease in estimated sales of 3G/4G/5G-based multimode products"), never as
a level.

---
### QCT against [E3-03] — and it fails on the subject's own words

- **(1) Needed or desired — PASSES.** A phone needs a modem and an SoC.
- **(2) No close substitute — FAILS, twice over, and the 10-K is the evidence both times.**
  - **Eleven named merchant competitors**, verbatim: *"Examples (some of which are strategic
    partners of ours in other areas) include **Broadcom, HiSilicon, MediaTek, Mobileye,
    Nvidia, NXP Semiconductors, Qorvo, Samsung, Skyworks, Texas Instruments and UNISOC**."*
  - **And the customers are the substitute.** Verbatim: *"Certain of our largest mobile
    handset customers (**for example, Apple, Samsung and Xiaomi**) develop their own
    integrated circuit products, which they have in the past utilized, and/or currently
    utilize, in certain of their devices. **We expect such customers will in the future
    utilize their own integrated circuit products in some or all of their devices, rather
    than our products.**"* Those three names are **the same three that were each 10%+ of
    consolidated revenue in FY2025.** The concentration and the substitution are one fact.
  - **And it has already happened.** *"**Apple began utilizing its own modem** (rather than
    our products) in its recently released smartphones and we expect that Apple will
    increasingly use its own modem products… **which will have a significant negative impact
    on our QCT revenues, results of operations and cash flows.**"* By the Q3 FY2026 10-Q the
    tense has moved: *"Apple **utilizes** its own modem… in certain of its smartphones."*
- **(3) Not subject to price regulation — passes, and is worth nothing [E2-59].**

**QCT fails criterion (2) and the failure is written by the company.**

---
### THE COMPETITOR ROW — required **[E3-28]**

> "**I can't be an intelligent owner of a business unless I know what all the other
> businesses in that industry are doing.**" — **[E3-28]**

**Same metric (operating margin on the segment or the whole company, most recent full fiscal
year), same window, all primary-sourced.** QCOM is shown at the *segment* line because the
whole point of this question is that the consolidated figure blends two different animals.

| Company | operating / EBT margin | revenue, same period | ROE | purity | period | source |
|---|---|---|---|---|---|---|
| **QCOM — QTL** | **72.4%** *(85% FY16 → 64% FY19 → 72% FY25)* | $5,582M | n/a (no segment equity) | **pure licensing** | FY2025 | 10-K acc. 0000804328-25-000085, Note 8 |
| **QCOM — QCT** | **30.4%** *(12% FY16 → 34% FY22 → 30% FY25 → **26% Q3 FY26**)* | $38,367M | n/a | **pure chips** | FY2025 | same |
| *QCOM consolidated* | *27.9% operating* | *$44,284M* | *see Q3* | *blend* | FY2025 | same |
| **MediaTek** — the direct modem/SoC rival | **17.4%** *(FY2024 17.6% implied)* | NT$595,966M ≈ **US$19.2bn** | n/d in release | **near-pure** mobile/consumer SoC | FY2025, to 2025-12-31 | **MediaTek 4Q25 press release, 2026-02-04, company IR (English)** — evidence-ladder rung 3 |
| **Broadcom (AVGO)** | **39.9%** | $63,887M | n/d (tag absent) | MIXED (semis + infrastructure software) | FY to 2025-11-02 | SEC XBRL 10-K |
| **Texas Instruments (TXN)** | **34.1%** *(50.6% FY22 → 34.1%)* | $17,682M | **30.7%** | analog/embedded, own fabs | FY2025 | SEC XBRL 10-K |
| **NXP (NXPI)** | **24.8%** *(28.8% FY22 → 24.8%)* | $12,269M | 20.1% | auto/industrial | FY2025 | SEC XBRL 10-K |
| **Marvell (MRVL)** | **16.1%** *(negative FY21–25)* | $8,195M | 18.7% | data infrastructure | FY to 2026-01-31 | SEC XBRL 10-K |
| **Skyworks (SWKS)** | **12.2%** *(27.8% FY22 → 12.2%)* | $4,087M | 8.3% | RF, Apple-concentrated | FY to 2025-10-03 | SEC XBRL 10-K |
| **Qorvo (QRVO)** | **11.2%** *(26.4% FY22 → 2.4% → 11.2%)* | $3,679M | 10.1% | RF, Apple-concentrated | FY to 2026-03-28 | SEC XBRL 10-K |
| **InterDigital (IDCC)** — the pure-play licensing comparator | **55.3%** *(its best year ever; 15.4% FY20)* | **$834M** | **36.9%** | **pure licensing** | FY2025 | SEC XBRL 10-K |
| Samsung System LSI · HiSilicon · UNISOC | **NOT OBTAINABLE** — see below | — | — | captive / private / non-registrant | — | — |

**Peers: 11 named by the subject; same-metric filing-sourced figures obtained for 7 of
them, plus InterDigital added by me as the only pure licensing comparator on the shelf.**

**The four not obtained, and the verdict on each — this is the four-verdict test applied to
the row itself.** *Samsung System LSI* is a sub-line of Samsung's DS division and is not
separately reported; *HiSilicon* is a wholly-owned Huawei subsidiary that publishes nothing;
*UNISOC* is privately held in China; *Mobileye* competes only in ADAS. For the first three I
asked *"can I name the document that would resolve this?"* and **the answer is no — no such
document is published anywhere.** That is **UNKNOWABLE about those competitors**, not
UNRESEARCHED, and it does not hold the subject's moat class provisional, because **the
verdict below rests on the subject's own filed admissions, not on the row.**

**WHAT THE ROW ACTUALLY SHOWS, INCLUDING THE PART THAT CUTS FOR QUALCOMM.**

1. **QTL is the best licensing business in the row, by a distance, and it is not close.**
   72.4% against InterDigital's 55.3% — and 55.3% is IDCC's **best year in its recorded
   history** (it ran 15.4% and 16.7% as recently as FY2020–21). **QTL at its worst year in a
   decade, FY2019, still earned 64%, above IDCC's best.** If the question were only "is QTL
   a franchise," the row answers yes.
2. **QCT is the second-best chip business in the row and beats its direct rival by 13
   points.** 30.4% against MediaTek's 17.4%, NXP's 24.8%, Marvell's 16.1%, Skyworks' 12.2%
   and Qorvo's 11.2%; only Broadcom (39.9%, and a different business) is ahead. I expected
   QCT to be middling and it is not. **Stated plainly because [E4-26] requires it.**
3. **And the row's limit, stated [E3-61]:** *"In some businesses, the participants behave
   like a demented Kellogg. In other businesses, they don't… **I think you'd have to know the
   people involved.**"* The row shows position. It cannot show what Apple's silicon team
   does next, and Apple is not in the row at all — **the most important competitor Qualcomm
   has is its largest customer, and it publishes no comparable metric.**
4. **Skyworks and Qorvo are the row's warning label.** Both were 26–28% margin businesses in
   FY2022 and are 11–12% now, and the single cause is the same customer relationship
   Qualcomm has. **The row contains two worked examples of what happens to a supplier when
   Apple re-sources, and both of them are severe.**

---
### The remaining Q2 tests

- **[E3-33] / [E5-28] — untapped pricing power?** **No.** Claiming it would be claiming
  near-monopoly (*"you're talking about a business that's a monopoly or a near monopoly"*),
  and QTL's price is the one thing four competition authorities and a FRAND commitment
  exist to constrain. For QCT the filing says the opposite direction: *"the concentration of
  device share among a few companies, and **the corresponding purchasing power of these
  companies, may result in lower prices for our products**."*
- **[E4-37] — the inverse metric, agony over price increases.** QCT genuinely raised price
  in FY2025: *"$2.5 billion in higher revenues per chipset primarily driven by **higher
  average selling prices** and favorable mix."* **That is a yawn-priced increase and it
  passes.** QTL's is the agony case: its rate is fixed by contracts that took litigation in
  four jurisdictions to settle.
- **[E2-44] — the two-characteristic test.** *Raise prices when demand is flat and capacity
  under-utilised?* QCT did in FY2025 — **passes**. *Grow dollar volume with only minor
  additional capital?* Capex is **2.7% of revenue** — **passes, easily.** **Both halves of
  [E2-44] pass, and that is a genuine and unexpected positive.** It does not repair criterion
  (2), which is what the gate turns on.
- **[E2-45] — the attacker's test.** *"how I would like, assuming I had ample capital and
  skilled personnel, to compete with it."* **Against QTL I would not like it at all** — I
  cannot design around an essential patent, and my only routes are invalidation, an antitrust
  complaint, or waiting for expiry. **That is the strongest single fact in this file for the
  name.** **Against QCT I would like it very much, and the record shows the play works:**
  hire a modem team, buy TSMC capacity, and take the socket. Apple did it. Samsung does it.
  Xiaomi does it. The Chinese state funds UNISOC to do it. **The attacker's test splits the
  company exactly the way the segment table does.**
- **[E2-53] — the dominance class.** *"Once dominant, the newspaper itself, not the
  marketplace, determines just how good or how bad the paper will be."* **QTL is in this
  class while its contracts run. QCT plainly is not** — the marketplace, in the form of three
  customers who are 54% of revenue and are all building substitutes, determines how good QCT
  will be.
- **[E4-36] — which of the four causes of extreme success?** The recent record is
  **wave-riding [E3-51]**, and the table proves it: QCT EBT margin 12% → 17% → 17% → 15% →
  17% → **29% → 34%** across FY2020–22. The wave was the 5G premium-tier upgrade cycle plus
  the shortage-era pricing. *"when a surfer gets up and catches the wave… he can go a long,
  long time. But if he gets off the wave, he becomes mired in shallows."* **The wave is
  receding on the filed record: QCT margin 34% (FY22) → 26% (FY23) → 29% → 30% → 28% (9M
  FY26) → 26% (Q3 FY26), and Q3 FY2026 handset revenue is down 19.6% year on year.**

---
### THE VERDICT, AND THE REASONING STATED SO IT CAN BE ATTACKED

**I find that Qualcomm contains a franchise and is not one.**

**QTL is a franchise.** It passes [E3-03](1) and (2) in the strongest form either criterion
takes, it earns 72% before tax on a $5.6bn revenue line, and no attacker can touch it while
its patents are in force. **It fails [E3-03](3) on price regulation, and it fails [E4-04]'s
durability test not by judgment but by statute — a patent estate is a depleting asset whose
basis must be replaced on a legal clock, which is the excluded class the framework names.**
**Its term is published: fiscal 2027 to fiscal 2031.** Its last renewal cycle lost Huawei
outright and re-signed two Chinese OEMs for +0.2%.

**QCT is not a franchise, and its own 10-K is the document that says so** — eleven named
competitors, and the statement that its three largest customers, who are 54% of consolidated
revenue, build the substitute and will increasingly use it.

**And the composite is not a franchise, because the franchise is not the company.** QTL is
**12.6% of revenue and 25.4% of reportable-segment EBT**. **You cannot buy QTL; you buy
Qualcomm, and 87% of Qualcomm is a fabless chip business in the class [E2-58] describes.**
**[E2-56]** names the reading error to avoid — *"Their marvelous core businesses…
**camouflage** repeated failures in capital allocation elsewhere"* — and instructs that the
consolidated series be judged **segment-by-segment, never on the blended return.** Judged
that way, the blend is a small toll gate with an expiry schedule bolted to a large,
well-run, customer-concentrated semiconductor business whose largest customer has announced
its exit in the filing.

**The finding that most nearly rescues it, stated once more so it is not buried:** QCT's
30.4% EBT margin beats every merchant peer except Broadcom and beats MediaTek by thirteen
points, QTL is the best licensing business on the shelf, and both halves of [E2-44] pass.
**Qualcomm is a very good business. [E5-42] is the rule that keeps that from being the
answer** — *"whether it's a good investment for us depends on how much we pay"* — and
[E3-03] is not asking whether the business is good. It is asking whether the advantage is
durable and substitute-proof. **For 87% of the revenue the answer is written in the filing
and it is no.**

- Class: [ ] WIDE  [ ] NARROW  **[x] NONE (composite)** — *QTL alone: NARROW, with a
  published expiry* · **Direction: NARROWING** (QTL EBT −38% from peak and flat for six
  years; QCT margin 34% → 26% over four years and falling in the current quarter)
- **VERDICT: [x] OUT**

> **Q2 closes the file. Under the hard sequence (operator rule 2), no verdict below this
> point is reached and no Q5 clearance exists.** Everything that follows was performed
> because the operator asked for it specifically and is recorded as **NOT REACHED —
> COMPUTATION, NOT A CLEARANCE** (operator rule 3). None of it carries entry language and
> none of it can reopen Q2.

---
# BELOW THE CLOSING GATE — RECORDED, NOT REACHED
### **COMPUTATION — NOT A CLEARANCE** (operator rule 3)

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — **NOT REACHED**

**STEP 1 — THE WEIGHT CASE, declared even though the gate is not reached.**
- [x] **Daily execution [E3-38] — TICKED.** 86.6% of revenue is a fabless chip business that
  must win a design socket every eighteen months against eleven named rivals and three
  customers building substitutes. There is no franchise under QCT to coast on. *(QTL alone
  would not tick this box — a signed licence collects while you sleep. The blend does,
  because the blend is mostly QCT.)*
- [ ] Control [E1-16] — not ticked; minority public stake.
- [ ] **Leverage [E3-29] — not ticked.** Debt $14,811M against $12,478M of cash, restricted
  cash and marketable securities — **net debt $2,333M** — and interest expense of $664M
  against $12,663M of pretax income, **19x covered**.
- **One ticked → had the gate been reached, Q3 would be a BINARY GATE and no price would
  compensate.**

**STEP 2 — THE FLAGS.** *Each a prompt to READ, never a verdict **[E5-36]**.*

- [ ] **weak accounting — not fired**, with one thing recorded. SBC is expensed in full
  ($2,783M FY2025) and sits in the cash-flow reconciliation. The item to record is a
  *disclosed* change of form: *"we have **replaced our annual cash incentive awards for
  fiscal 2026 and 2027 with a two-year equity award** for our broader non-executive
  leadership team."* **That converts a cash expense into a stock expense and therefore
  flatters operating cash flow** — 9M FY2026 SBC is up 21.7% while OCF is down 16.1%. This
  run's construction subtracts SBC in full **[E5-06]**, so the figures here are immune; a
  cash-flow-only screen would not be. **Announced ahead with a reason, which is the candor
  case, not the flag [E2-49].**
- [ ] unintelligible footnotes — **not fired.** Note 8's segment table and Note 3's tax
  reconciliation are readable at first pass.
- [ ] trumpeted earnings projections — **not fired in the filing.** The "Looking Forward"
  section is qualitative and carries no EPS or revenue target.
- [x] **serial share issuance [E5-15] — DOES NOT FIRE, and fires hard in reverse.** Diluted
  shares 1,498M (FY2016) → **1,105M (FY2025)**, −26.2%. Proceeds from stock issuance were
  $404M in FY2025 against $8,791M of repurchases.
- [ ] **EBITDA / adjusted-earnings promotion [E4-29] — NOT FIRED, and the sweep is recorded.**
  Full-text search of the FY2025 10-K: **"EBITDA" 0 occurrences. "Non-GAAP" 0. "free cash
  flow" 0.** The fifth flag, which the corpus restates twelve-plus times, is entirely absent.
  **This is a real credit and it is stated as one [E4-26].**
- [ ] **[E2-57] the except-for flag — NOT FIRED.** *"except for"* appears **0 times.**
- [ ] **filed-figure tells [E4-30] — CHECKED AND CLEAN, and this cuts for the company.**
  Cash income taxes paid as a share of reported pretax income: **19.0% (FY16), 33.1% (FY17),
  n/m (FY18), 14.7%, 14.5%, 14.6%, 14.0%, 18.8%, 31.9% (FY24), 24.5% (FY25).** The tell is
  cash taxes *falling* as a share of pretax income. They are **rising** — 14.0% at the FY2022
  peak to 24.5% now. And *unnaturally smooth growth?* Diluted EPS ran **$3.81, $1.65,
  −$3.32, $3.59, $4.52, $7.87, $11.37, $6.42, $8.97, $5.01.** Nobody is smoothing this.
- [x] ### **SIXTH — METRIC-SWITCHING [E2-49]. THIS ONE FIRES, AND IT IS THE ONE FINDING IN Q3 THAT MATTERS.**

  > "Yardsticks seldom are discarded while yielding favorable readings. But when results
  > deteriorate, most managers favor **disposition of the yardstick rather than disposition
  > of the manager**" — demand *"pre-set, long-lived and small bullseyes."* — **[E2-49]**

  Qualcomm published MSM chipset unit shipments for years: **842M (FY2016), 804M (FY2017),
  855M (FY2018), 650M (FY2019), 575M (FY2020)**. Then, verbatim in the FY2020 10-K:
  *"**Beginning in fiscal 2021, we will no longer provide MSM integrated circuit shipments**
  since such measure is becoming increasingly less meaningful in understanding and
  evaluating the performance of our QCT segment."*

  **The yardstick was disposed of in the year immediately following a 32.7% two-year
  decline, and it had been provided in every prior year, including the years it rose.**
  The operational form of the test is exactly this: *"compare the headline metric across
  successive filings; a switch that **follows** deterioration fires."* It followed. **There
  is now no physical unit series in the filing for either segment**, and QTL's unit driver
  appears only as a year-on-year dollar delta, never as a level. Under **[E4-55]** that is
  also the moat-monitoring metric, which is why it is recorded at Q2 as well.

**STEP 3 — THE PRIMARY TEST [E2-01], and the denominator has to be argued.**

> "**The primary test of managerial economic performance is the achievement of a high
> earnings rate on equity capital employed** (without undue leverage, accounting gimmickry,
> etc.)" — **[E2-01]**

**Return on book equity is unusable here and the reason is a corporate action, not the
business.** In FY2018 Qualcomm bought back **$22,580M** of stock in a single year — a Dutch
auction executed after the Broadcom bid was blocked — taking shareholders' equity from
**$30,746M to $807M**. Every ROE from FY2019 onward is computed on a denominator manufactured
by that transaction. **[E2-47]** carves out exactly this case (*"unusual debt-equity ratios"*)
and **[E2-43]** directs the denominator to unleveraged net tangible assets for such filers.

**So the series is reported on capital employed — pretax EBT ÷ (shareholders' equity + total
debt) — which is immune to the buyback because the buyback moved the mix, not the total.**
Equity is recomputed as **Assets − Liabilities** from the filed balance sheets, which is the
**[E5-32]** cross-check (*"the floating plug"* — audited does not mean true); it reconciles to
the tagged `StockholdersEquity` in every year where both exist.

| FY | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| equity (A−L), $M | 31,768 | 30,758 | **807** | 4,909 | 6,077 | 9,950 | 18,013 | 21,581 | 26,274 | 21,206 |
| total debt, $M | 10,008 | 20,894 | 15,365 | 15,434 | 15,226 | 15,245 | 14,983 | 15,398 | 14,634 | 14,811 |
| **pretax return on capital employed** | **16.4%** | 5.8% | 3.2% | **36.8%** | 26.8% | **40.8%** | **45.5%** | 20.1% | 25.3% | **35.2%** |

- **ten-year mean 25.6% · five-year mean 33.4%, pretax.** By **[E3-46]**'s standard —
  *"the best businesses, by definition, are going to be businesses that earn very high
  returns on capital employed over time"* — **this is a high return, and it is not close.**
  It is far above the [E2-42] red-light level. **This is the strongest number in the file and
  it is recorded as such.**
- **Goodwill wedge, reported separately per [E2-43]:** goodwill is **$11,358M** of the
  $21,206M of FY2025 equity, so **net tangible equity is at most $9,848M** before other
  intangibles. On that denominator the returns are higher still, which is why the wedge is
  disclosed rather than hidden inside book equity.
- **[E2-73]:** *"what we pay for a business does not affect the amount of capital its manager
  has to work with."* Judged on the capital actually in the business, this management is
  running a high-return operation. **That finding is recorded and, per the guardrail below,
  is not permitted to promote anything.**

**The half-owner test [E2-26]: MIXED, and the failure is specific.**
*Passes* on: segment revenue and EBT with the significant expense categories; QCT revenue
split three ways; revenue by country; customer concentration in percentage terms; the tax
reconciliation and the valuation-allowance mechanics; the litigation descriptions, which are
unusually full. **Fails on the three things a buyer of *this* business most needs:**
1. **Which licensee is 21% of revenue** — the note letters (x)/(y)/(z) are never mapped to
   the three names given in Item 1.
2. **The expiry date of any individual licence** — only the range *"fiscal 2027 and 2031."*
3. **Any unit series at all**, withdrawn in FY2021 (above).

**The institutional imperative — score all four [E2-30].** *Not a fraud test.*
- [ ] resists change in current direction — **no; the opposite.** The diversification into
  automotive and IoT is a genuine change of direction and it is being executed (below).
- [x] **projects/acquisitions materialise to soak up available funds — LIVE.** Seven
  acquisitions for $668M in FY2025 (**$526M of it goodwill**, i.e. 79% of the price was not
  identifiable assets), plus **Alphawave at ~$2.4bn enterprise value** with **$2.3bn of cash
  restricted** for it, into a data-centre business the filing still calls a *"nonreportable
  segment."*
- [ ] staff studies to justify a craving — not observable from filings.
- [x] **peer behaviour mindlessly imitated — LIVE.** The Alphawave purchase is an entry into
  AI data-centre silicon at the top of an industry-wide capital cycle in which every named
  peer is doing the same thing. **[E2-27]**: *"Viewed individually, each company's capital
  investment decision appeared cost-effective and rational; viewed collectively, the
  decisions neutralized each other and were irrational."*

**Capital allocation — the two buyback conditions [E5-08], plus the third [E4-31]:**
- **(1) ample funds for operations and liquidity? YES, comfortably.** $12,478M of cash,
  restricted cash and marketable securities; a **$4.0bn undrawn revolver** to 2029-08-08; a
  **$4.5bn commercial-paper programme with nothing outstanding**; net debt of $2,333M;
  interest 19x covered; and *"We are not subject to any financial covenants under the notes."*
- **(2) repurchases at a material discount to conservatively calculated IV? NO, on our own
  range — and the humility clause is not a formality here.** FY2025: **56 million shares
  retired for $8,791M, an average of ~$157/share**; the Q4 monthly table shows **$157.75,
  $153.36 and $158.93**. At $157 the capitalisation was roughly **$171bn**, against a
  conservative (nine-year, D&A-end) owner-earnings figure of **$5,433M — a 3.2% yield,
  more than two points under the sovereign.** By our arithmetic these were not purchases at
  a material discount. **[E4-13] and [E5-08] both apply and they cut against us: the stock
  is $169.43 today, above every price paid, so management's timing has so far beaten our
  range, and *"many CEOs never stop believing their stock is cheap"* is the charitable and
  probably correct reading.** **→ CAPITAL ALLOCATION FLAG. It binds position size, never the
  discount rate.**
- **(3) [E4-31] — was the register supplied all the information it needs to estimate value?
  NO, and this is the sharpest Q3 finding after the yardstick.** *"Shareholders should have
  been supplied all the information they need for estimating that value."* **A licensing
  business is a portfolio of dated contracts. Qualcomm discloses the termination dates only
  as a five-year band and never names which licensee is which.** No shareholder can build the
  QTL runoff, and QTL is the only part of this company that is a franchise. **The buyback is
  being executed against a register that has been given a range where it needs a schedule.**
- **[E2-52] — dividends funded by issuance? Does not fire.** $3.8bn of dividends against
  $404M of issuance proceeds and $8,791M of repurchases; the payout is funded from
  operations several times over.
- **[E4-39] — the rare-positive tell, a candid acquisition post-mortem?** **No instance
  found**, and the sweep is named: the FY2025, FY2022, FY2020 and FY2018 10-Ks were
  full-text searched for any revisiting of a prior acquisition against its announcement case.
  There is none. *(The corpus says this is "almost never witnessed", so its absence is the
  base case, not a flag.)*

**THE GUARDRAIL [E2-37, E2-38, E3-39] — checked before writing the verdict.**
- [x] Confirmed: **nothing in this Q3 is being used to promote the name.** The 33.4%
  five-year pretax return on capital employed, the clean tax tells, the absent EBITDA
  promotion and the 26% share retirement are all real and none of them repairs Q2.
  *"a textile company that allocates capital brilliantly within its industry is a remarkable
  textile company — but not a remarkable business."* **[E3-39]**: *averaged out, betting on
  the quality of a business is better than betting on the quality of management.*
- [x] Key-person dependence: **not found.** Cristiano Amon's tenure is not the moat and the
  filing does not claim it is.
- **VERDICT: NOT REACHED.** *Had it been reached, the honest entry would be: **no integrity
  disqualifier found** — which under **[E5-17]** is the absence of found disqualifiers and
  not a finding that the managers are honest — with a **metric-switching flag [E2-49]** on
  the withdrawn unit disclosure and a **live capital-allocation flag** on buyback condition
  (2) and on the **[E4-31]** information condition.*

---
## Q4 — WILL IT SURVIVE? — **NOT REACHED. COMPUTATION — NOT A CLEARANCE.**

### Owner earnings — the one number **[E2-23]**, with (c) as a DISCLOSED JUDGMENT

**THE (c) JUDGMENT, AND IT IS THE REVERSE OF THE USUAL DIRECTION.**

The corpus default is D&A **[E3-44, E2-41]** — *"by and large, the depreciation charge is not
inappropriate in most companies to use as a proxy for required capital expenditures."* The
exception class **[E5-20]** is the capital-intensive filer whose own document says
depreciation understates renewal; there the D&A end is **INVALID**, not merely optimistic.

**Qualcomm is not in the exception class, and here D&A is also the CONSERVATIVE end.**
The grounds, all filed:
1. **capex/D&A = 0.813x** on nine-year means ($1,289M against $1,586M). Qualcomm spends
   **less** on plant than it charges to depreciation, so substituting D&A for capex *reduces*
   owner earnings. The [E3-44] default and the conservative choice coincide.
2. **It is fabless.** Capex is **2.7% of revenue**. There is no fab renewal cliff of the kind
   [E5-20] was written for; the wafers are TSMC's and Samsung's problem, and their capital
   cost arrives as cost of revenues, already inside OCF.
3. **A large part of D&A is acquired-intangible amortization, not plant renewal** — goodwill
   is $11,358M and the company bought seven businesses in FY2025 alone. That is why D&A
   exceeds capex, and it means the D&A end is if anything *over*-conservative as a plant
   proxy.
4. **The real reinvestment is R&D — $9,042M, 20.4% of revenue — and it is already expensed
   above the operating-cash-flow line.** This is the important point about this business's
   (c): the maintenance spending that keeps QTL's patent estate alive is *not capitalised at
   all*. It is fully charged, every year, inside OCF. **No adjustment is needed and none is
   made — but it is the reason [E2-60]'s third dimension is satisfied: the payout is not
   coming at the expense of the ability to maintain the competitive position, because the
   maintenance is being paid for in the income statement.**

**RULING: both ends of the band are valid. (c) is displayed at D&A and at capex, and the D&A
end is the conservative one. The judged figure is the D&A end, and the reason is [E5-34]:
*"we will buy the stock… if it sells at a reasonable price in relation to the bottom boundary
of our estimate."*** Windage count: **one** (the conservative end of the band), spent here.

### THE WINDOWS — every one published **[E4-38]**, spread carried as part of the range **[E4-25]**

Cap **$177,902M** (hand-built, Stage 0(a)); sovereign **5.27%**.

| window | mean(OCF−SBC) | **OE, (c)=D&A** *(conservative)* | OE, (c)=capex | **yield (D&A)** | yield (capex) | **g for the [E4-28] 10% floor** |
|---|---|---|---|---|---|---|
| 3-yr FY23–25 | 9,866.0 | **8,160.3** | 8,638.3 | **4.59%** | 4.86% | 5.41% / 5.14% |
| **5-yr FY21–25 — [E2-42] default** | 9,107.2 | **7,415.0** | 7,540.6 | **4.17%** | 4.24% | **5.83% / 5.76%** |
| 7-yr FY19–25 | 8,055.3 | **6,447.4** | 6,608.6 | **3.62%** | 3.71% | 6.38% / 6.29% |
| 9-yr FY17–25 — full cycle | 7,019.8 | **5,433.4** | 5,730.8 | **3.05%** | 3.22% | 6.95% / 6.78% |

- **Short-window mean (3-yr, judged (c)): $8,160M · Long-window mean (9-yr): $5,433M ·
  five-year default: $7,415M.**
- **Spread, conservative end: the 9-year is 33.4% below the 3-year.**
- **COMBINED RANGE (window spread × capex band): $5,433M to $8,638M — a width of 59.0%.**
  *The screen's 16% was one corner to another and understated this by nearly four times.*

**IS THE RANGE TOO WIDE TO REACH A CONCLUSION [E4-25]? No — and the reason is the useful
part.** *"If the combined range is too wide to reach a conclusion, that IS the conclusion."*
Here the width is large but **the answer does not move anywhere inside it: every one of the
eight constructions yields below the 5.27% sovereign, and the highest of them, 4.86%, is 41
basis points short.** A range that is wide but entirely on one side of the yardstick is a
finished answer, not an indeterminate one.

**A wide spread is itself a Q4 finding [E5-11] — name the distorted years, and there are
three.**
1. **FY2018** — owner earnings $2,228M on revenue of $22,611M, with a **$22,580M** buyback,
   the NXP transaction's collapse and the US Tax Act charge all in one year. A genuinely
   distorted year and it sits in the long windows.
2. **FY2019** — the Apple settlement year; QTL revenue was suppressed for the first six
   months and then restored.
3. **FY2025** — the terminal year, and the one the boom test turns on.

**[E3-55] scopes this honestly:** volatility with a certain endgame is not a defect. **This is
not that case.** The spread here is not See's losing money eight months a year; it measures
uncertainty about the *level*, and the level is exactly what is in dispute.

### **[E4-41] — NORMALIZE THE MEAN DOWN FOR LUCK. The break is named and removed.**

> the corpus's only pro-forma that ever disclosed earnings **too high** is Berkshire's own — a
> no-megacat year and a bond tailwind stripped out as *"about $500 million less than we
> actually reported."* — **[E4-41]**

**The break is named: the 5G premium-tier upgrade cycle, and it lands entirely in QCT.**
The segment table proves the attribution — QCT EBT margin ran 12 / 17 / 17 / 15 / 17% in
FY2016–20 and then **29 / 34 / 26 / 29 / 30%** in FY2021–25, while QTL's EBT *fell* over the
same span. **The 2.02x level shift is a QCT margin event, not a franchise event.**

**And it is already reversing on the filed record, which is what makes the normalisation
computable rather than a guess.** From the Q3 FY2026 10-Q:

| | 9M FY2025 | 9M FY2026 | change |
|---|---|---|---|
| Revenues | 33,013 | 32,798 | −0.7% |
| **Operating income** | **9,437** | **7,302** | **−22.6%** |
| QCT EBT margin | 30.7% | **28.2%** | −2.5 pts |
| **QCT handsets revenue** | **20,831** | **18,934** | **−9.1%** |
| Operating cash flow | 10,016 | 8,405 | −16.1% |
| **OWNER EARNINGS (OCF−SBC−capex)** | **7,111** | **4,248** | **−40.3%** |

*Q3 FY2026 alone: QCT handsets $5,086M against $6,328M, **−19.6%**; QCT EBT margin **26%**;
operating income $1,626M against $2,762M, **−41%**.*

**THE NORMALISED FIGURE, AND HOW IT IS BUILT.** Three independent constructions are run and
all three are published rather than the convenient one:

| construction | figure | yield on $177,902M | vs 5.27% |
|---|---|---|---|
| **(a) Nine-year full-cycle mean, (c)=D&A** — the [E4-41] instrument, since a full cycle contains its own booms and busts | **$5,433M** | **3.05%** | **−2.22 pts** |
| **(b) FY2026 run-rate: 9M owner earnings annualised (4,248 × 4/3)** — what the business is earning *now* | **$5,664M** | **3.18%** | **−2.09 pts** |
| **(c) Five-year default less the QCT margin excess** — FY2021–25 mean $7,415M, with QCT EBT re-struck at its FY2016–20 mean margin of 15.6% instead of the FY2021–25 mean of 29.6%, a reduction of $3,904M pretax on FY2025 alone | **~$4,700M** | **~2.6%** | **−2.6 pts** |

**All three land between roughly $4,700M and $5,700M. The normalised owner-earnings figure
this run adopts is $5,400M, and it is a DISCLOSED JUDGMENT, not a computation.** It sits at
the nine-year full-cycle mean, is corroborated within 5% by the independent current-year
run-rate, and is 27% below the screen's $7,415M bottom boundary.
**Yield on the normalised figure: 3.04% against a 5.27% sovereign — 223 basis points BELOW
the government bond.**

**best_year_dependence, reported alongside [E4-38]:** removing FY2025 takes the five-year
default from $7,415M to $6,131M, **−17.3%**. The dependence is real and it points the same
way as the normalisation, which is why both are reported rather than one.

**Stock compensation subtracted in full [E5-06]:** yes, at the reported charge — $2,783M in
FY2025, five-year mean $2,322M. **[E3-70] says the reported charge is the FLOOR of the correct
subtraction, not the measure** (*"an amount equal to what the company could have realized by
publicly selling options of like quantity and structure"*). **At 6.3% of revenue and rising
21.7% year on year, SBC here is material enough that this understatement matters** — but the
windage has been spent once already, at the conservative end of the capex band **[E4-11,
E4-48]**, so no further conservatism is applied and the point is recorded instead. **Windage
count: one.**

### Great, good, or gruesome? **[E4-20]**

- [x] **GREAT, on the business's own economics — and this is not the question that closes
  the file.** *"The great one pays an extraordinarily high interest rate that will rise as
  the years pass."* Pretax return on capital employed averaged **25.6% over ten years and
  33.4% over five**; capex is 2.7% of revenue; QTL earns 72% before tax on essentially no
  capital. **This business does not eat capital and it is not gruesome by any reading.**
- **[E4-43] is the reason this matters less than it looks:** the *good* class passes and the
  *great* class ranks above it — but Q4's classification is about survival and capital
  hunger, and **it cannot reopen Q2, which is about durability.** A great savings account
  whose interest rate is contractually scheduled to be renegotiated between fiscal 2027 and
  2031 is still a great savings account today. That is precisely the distinction Q2 drew.

### Staying power — score all three **[E5-11]**

- **(1) A large and reliable stream of earnings — LARGE, AND THE RELIABILITY IS THE ISSUE.**
  $12,663M of pretax income in FY2025 and $8,241M in nine months of FY2026. But the stream is
  **41% concentrated in two customers** (9M FY2026: 24% + 20%), **46% concentrated in China**,
  and the licensing half runs on contracts that expire fiscal 2027–2031.
- **(2) Massive liquid assets — YES.** $12,478M of cash, restricted cash and marketable
  securities. *(Of which $2,323M is restricted for Alphawave, so $10,155M is free.)*
- **(3) No significant near-term cash requirements — YES, and this is the one that usually
  kills, so it is scored carefully.** **$15.1bn of principal fixed-rate notes with maturities
  spread from 2027 to 2053**; nothing outstanding on the $4.5bn commercial-paper programme;
  nothing drawn on the $4.0bn revolver; **no financial covenants on the notes.** **[E5-39]**'s
  test — *"We will never be dependent on the kindness of strangers"* — is met without counting
  either facility. **[E2-54]**'s coverage test — all interest met out of current cash flow
  **net of ample capital expenditures** — is met at 19x. **This passes cleanly.**
- **Leverage, named and quantified [E4-16, E3-29]:** total debt $14,811M; cash and securities
  $12,478M; **net debt $2,333M**, or **0.18x** FY2025 pretax income. **There is no leverage
  problem here and there is no leverage ratio in this framework to apply anyway.**
- **[E3-52] — read the terms, not just the quantity.** All fixed-rate, unsecured, no
  covenants, maturities to 2053, with $3.6bn of notional swaps converting some fixed to
  floating. This is patient money on good terms.

**Staying power: 3 of 3. Qualcomm is not going to be killed by its balance sheet.**

### Diversification into automotive and IoT — real revenue or a story? **THE NUMBERS.**

*The operator asked this as a test, not an assumption **[E4-26]**.*

| $M | FY2021 | FY2022 | FY2024 | FY2025 | 9M FY2025 | **9M FY2026** |
|---|---|---|---|---|---|---|
| **Automotive** | 975 | 1,372 | 2,910 | **3,957** | 2,904 | **4,015 (+38.3%)** |
| **IoT** | 5,056 | 6,948 | 5,423 | **6,617** | 4,811 | **5,244 (+9.0%)** |
| Handsets | 16,830 | 25,027 | 24,863 | **27,793** | 20,831 | **18,934 (−9.1%)** |

**VERDICT ON THIS SUB-QUESTION: automotive is REAL and it is the best thing in the file.**
$975M to $3,957M in four years is **a 4.1x**, and it is still compounding at 38% in the
current nine months while handsets fall 9.1%. **IoT is real but flat-ish** — $6,948M in
FY2022, $5,423M in FY2024, $6,617M in FY2025, +9.0% now; it round-tripped a cycle rather
than growing through one.

**But scale it honestly, because that is what decides whether it rescues anything.**
**Automotive plus IoT is $10,574M, 27.6% of QCT revenue and 23.9% of consolidated revenue.**
Handsets are still **72.4% of QCT**. **Automotive would have to grow at 38% a year for four
more years just to replace handsets at their current level** — and the filing gives no
segment EBT for automotive, so **the margin is not disclosed and cannot be computed.**
*(Absence stated as an absence: Note 8 gives EBT for QCT as a whole and revenue only for the
three streams. No document published by Qualcomm splits QCT EBT by stream, so this is
**UNKNOWABLE**, not UNRESEARCHED.)* **A diversification whose profitability is not disclosed
cannot be credited with profits.**

### **NAME THE SPECIFIC WAY THIS BUSINESS DIES [E2-27, E3-24] — quantified, not asserted**

> "**Consider some mathematics:** … If 10% of all $48 billion of the bank's loans … produced
> losses averaging 30% of principal, the company would roughly break even." — **[E3-24]**

**[E4-40] governs the construction: model EXPOSURE, not experience.** *"all of us in the
industry made a fundamental underwriting mistake by focusing on experience, rather than
exposure."* Qualcomm's recent *experience* is a 2.02x earnings step-up. Its *exposure* is
below.

**MECHANISM 1 — THE CUSTOMER WHO IS ALSO THE COMPETITOR. Likelihood: LIKELY. The filing does
not say this might happen; it says it is happening.**

> "**Apple utilizes its own modem** (rather than our products) in certain of its smartphones
> and we expect that Apple will increasingly use its own modem products, rather than our
> products, in its future devices, **which will have a significant negative impact on our QCT
> revenues, results of operations and cash flows.**" — Q3 FY2026 10-Q

**The mathematics, from filed figures only.** The largest customer/licensee is **21% of
FY2025 consolidated revenue = $9,300M**, rising to **24%** in 9M FY2026. *(The filing does
not map the letters to the names, so the run does not either; the exposure is stated at the
concentration line, which is a filed number.)* QCT's FY2025 gross margin was
**(38,367 − 19,302) ÷ 38,367 = 49.7%**, and QCT operating expense was $7,395M, of which the
R&D component does not fall when a socket is lost.

- **If $6,000M of QCT chip revenue is withdrawn** at a 49.7% gross margin and no reduction in
  operating expense, **QCT EBT falls by $2,982M** — from $11,670M to $8,688M, and
  **consolidated pretax income falls 23.5%**, from $12,663M to $9,681M.
- **If $4,000M is withdrawn**, EBT falls $1,988M and consolidated pretax falls **15.7%**.
- **If the whole $9,300M relationship goes — chip and royalty together, which requires the
  licence to lapse as well as the socket** — the loss is larger than either figure and the
  exercise stops being arithmetic and becomes the combined case below.
- **The filing supplies a partial mitigant and it is stated:** *"Apple purchases our MDM (or
  thin modem) products… **which have lower revenue and margin contributions** than our
  combined modem and application processor products."* So the margin above is a ceiling on
  the damage from the Apple line specifically, and the true figure is somewhat lower.

**MECHANISM 2 — THE EXPIRY SCHEDULE. Likelihood: A REAL POSSIBILITY, and it is dated.**
Every material licence expires **fiscal 2027–2031**. QTL EBT is **$4,043M = 31.9% of
FY2025 consolidated pretax income** on 12.6% of revenue.
- **The last full repricing of this book, FY2016→FY2019, took QTL EBT from $6,528M to $2,954M
  — a 54.7% reduction.** That is not a hypothetical; it is Qualcomm's own history at the last
  time its licensing terms were forced open.
- **A 25% repricing at renewal costs $1,011M of pretax income — 8.0% of the FY2025 total.
  A repeat of the FY2016–19 experience, 55%, costs $2,224M — 17.6%.**
- **The base rate from the most recent renewal cycle is not reassuring:** Huawei's agreement
  expired and produced **zero**; two Chinese OEMs re-signed and QTL revenue moved **+0.2%**.

**MECHANISM 3 — CHINA. Likelihood: A REAL POSSIBILITY.** **46% of FY2025 revenue = $20,340M**
is booked to China-headquartered customers, in a jurisdiction whose government the filing
says *"has prioritized semiconductor self-sufficiency"*, and where one large customer has
already been removed by **US export-licence revocation** (Huawei, May 2024, *"we do not
expect to receive any further product revenues from Huawei"*).

**THE COMBINED CASE, WHICH IS THE ONE TO STATE [E4-51].** Mechanisms 1 and 2 are not
independent — they are the same fact, which is that Qualcomm's counterparties have grown
strong enough to take both the socket and the rate. **If $6,000M of chip revenue is lost and
the licence book reprices 25%, consolidated pretax income falls from $12,663M to $8,670M,
−31.5%.** Applying that reduction to the normalised owner-earnings figure of $5,400M gives
**about $3,700M, a yield of 2.08% on today's capitalisation, against a 5.27% sovereign.**

**And the honest counter, put as its holders would put it [E4-51]:** Qualcomm has been told
it was dying at every one of these junctures — the FTC case, the KFTC fine, the EC fines, the
Apple withholding, the Broadcom bid, the NXP collapse, the Arm suit — and it won or survived
every one of them, grew owner earnings 2.02x through the period, and is currently compounding
automotive at 38%. **The bear case is not that the business fails. It is that the *franchise*
half shrinks on a published schedule while the *chip* half's best customer builds the
substitute, and that the price today already assumes neither happens.** That is the case its
holders would accept as fairly stated, and it is the one this file rests on.

- Likelihood: **[x] likely** (mechanism 1, which the filing states as fact) ·
  **[x] a real possibility** (mechanisms 2 and 3)
- **VERDICT: NOT REACHED.** *Had it been reached: **staying power 3 of 3, great on the
  savings-account test, and the named death is specific, dated and quantified.** Q4 would
  most likely have returned IN — the business survives — which is exactly why Q2 and not Q4
  is where this file closes.*

---
## Q5 — **NOT REACHED. COMPUTATION — NOT A CLEARANCE** (operator rule 3)

⛔ **Q5 did not open. Q2 returned OUT.** Everything below is arithmetic produced to satisfy
the queue's output contract, which requires a price either way. **It carries no entry
language, it is not a clearance, and it cannot reopen Q2.**

**Inputs, all established above:** cap **$177,902M** (1,050M shares × $169.43, 2026-09-02;
quote from an aggregator and flagged) · sovereign **5.27%** (US Treasury 30-year,
2026-09-01, issuing authority) · owner-earnings range **$5,433M – $8,638M**, normalised
judgment **$5,400M**.

**1. THE YIELD**

| construction | owner earnings | ÷ cap | **yield** | sovereign | **points over/under** |
|---|---|---|---|---|---|
| 3-yr FY23–25, (c)=capex — *most generous* | $8,638M | $177,902M | **4.86%** | 5.27% | **−0.41** |
| 5-yr FY21–25, (c)=D&A — *the screen's boundary* | $7,415M | | **4.17%** | 5.27% | **−1.10** |
| 9-yr FY17–25, (c)=D&A — *full cycle, conservative* | $5,433M | | **3.05%** | 5.27% | **−2.22** |
| **NORMALISED [E4-41] — the judged figure** | **$5,400M** | | **3.04%** | 5.27% | **−2.23** |
| FY2026 run-rate (9M annualised) — *what it earns now* | $5,664M | | **3.18%** | 5.27% | **−2.09** |

**Every construction in the file, generous and conservative alike, yields less than the
government bond. The best of them falls 41 basis points short; the judged figure falls 223.**

**2. WHAT THE PRICE ALREADY ASSUMES**

| | perpetual g to justify the quote **at the sovereign** | perpetual g to reach the **[E4-28] 10% floor** |
|---|---|---|
| on $8,638M (most generous) | **0.41%** | **5.14%** |
| on $7,415M (screen's boundary) | **1.10%** | **5.83%** *(the screen's 5.70% on its own cap, reproduced)* |
| on $5,400M (normalised) | **2.24%** | **6.96%** |

**What the business has actually done — both windows published [E4-38], because
*"growth-rate presentations can be significantly distorted by a calculated selection of
either initial or terminal dates"*:**

| | **from FY2017** (a trough — the Apple-withholding year) | **from FY2016** (a normal year) |
|---|---|---|
| owner-earnings growth | **+15.87%/yr** | **+6.05%/yr** |
| share retirement | +3.81%/yr | +3.47%/yr |
| **owner earnings per share** | **+20.30%/yr** | **+9.69%/yr** |
| **and in the current year (9M FY2026)** | **−40.3%** | **−40.3%** |

**THE PER-SHARE DECOMPOSITION THE OPERATOR ASKED FOR.** Prices are month-end closes nearest
the fiscal year end, from an aggregator and flagged as such; everything else is filed.

| | FY2017 → FY2025 (8 yrs) | **FY2016 → FY2025 (9 yrs)** |
|---|---|---|
| **real owner-earnings growth** | +15.87%/yr | **+6.05%/yr** |
| **share retirement** | +3.81%/yr | **+3.47%/yr** |
| **multiple change** | **−3.80%/yr** *(25.0x → 18.3x)* | **+0.57%/yr** *(17.4x → 18.3x)* |
| **= total price return** | **+15.73%/yr** *($51.84 → $166.36)* | **+10.32%/yr** *($68.72 → $166.36)* |

**Read it on the FY2016 base, which is the fair one because FY2016 was a normal year and
FY2017 was a trough: of 10.3 points of annual return, 6.1 came from the business, 3.5 from
retiring a quarter of the shares, and 0.6 from the multiple. The market has not re-rated
this company in nine years.** That is a disconfirming fact for anyone arguing the market has
mispriced it, and it is stated first for that reason **[E4-26]**.

**And the comparison that decides the arithmetic:** the price requires **5.14% to 6.96%
perpetual growth** merely to reach the floor the corpus says it quits below. **The business
has compounded owner earnings at 6.05% a year across a nine-year window that contained the
entire 5G upgrade cycle, the shortage-era pricing and a 2.02x margin boom — and its current
nine months are down 40.3%.** **[E4-35]** is the governing base rate: *"I would wager you a
very significant sum that **fewer than 10 of the 200 most profitable companies** in 2000 will
attain 15% annual growth in earnings-per-share over the next 20 years."* Perpetual growth is
a stronger claim than twenty-year growth, and the burden of proof sits with the buyer.
**[E4-44]** bounds it from the other side: *"the value of an asset, whatever its character,
cannot over the long term grow faster than its earnings do."*

**3. WHAT YOU ARE PAID**
- **−2.23 points against the sovereign** on the judged figure; **−0.41 points** on the most
  generous construction in the file. **You are paid less than the government bond on every
  reading.**

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — capitalised at the sovereign, **zero
growth**, so that the growth assumption is visible as an addition rather than buried:

| construction | value | **per share (1,050M)** |
|---|---|---|
| 3-yr capex-end $8,638M ÷ 5.27% | $163,910M | **~$156** |
| 5-yr default $7,415M ÷ 5.27% | $140,702M | **~$134** |
| 9-yr cycle $5,433M ÷ 5.27% | $103,093M | **~$98** |
| **normalised $5,400M ÷ 5.27%** | **$102,467M** | **~$100** |
| *at the [E4-28] 10% floor instead of the bond, on the normalised figure* | *$54,000M* | *~$51* |

### **THE PRICE**
> **COMPUTATION — NOT A CLEARANCE.**
> **Conservative ~$100 per share · generous ~$156 per share · judged ~$100 per share ·
> CURRENT PRICE $169.43 (2026-09-02).**
> **Round-number band: roughly $100 to $155, against a quote of $169.**
> Whole-company: roughly **$102bn to $164bn** against a market capitalisation of
> **$178bn**.

**WHICH BAR — display only, since no bar was earned.**
- [x] **Screamer test [E4-01]** — *does the price already clear the **conservative** case?
  No margin is added on top.* Three outcomes: below the conservative case → act; inside the
  range → no useful conclusion; **above the whole range → no.** **The quote is $169.43 and
  the top of the entire zero-growth range is ~$156. The price is above the whole range.**
- [ ] Normal method [E4-11] — not run; a margin of safety is applied to a business that has
  passed Q2, and this one did not.
- **Windage count: ONE.** Conservatism was spent once, at the conservative end of the capex
  band **[E4-11, E4-48]**. It was deliberately *not* spent again on the [E3-70] SBC
  understatement, on the undisclosed automotive margin, or in the discount rate — **and no
  per-name risk premium is in the rate, which [E3-42] names as the error** (*"mathematical
  gibberish"*). The sovereign is used bare.

- **VERDICT: NOT REACHED. No ranking position exists** — a name that failed Q2 is not ranked
  against the opportunity set, because the ranking is among businesses that cleared the
  gates. **[E4-28]**: *"that's the figure we quit on."* On the judged figure the honest
  pre-tax expectancy at this price is **3.0% plus growth**, and it would need **6.96%
  perpetual growth** to reach 10%.

---
## Q6 — WHAT WOULD PROVE ME WRONG? — **NOT REACHED**

*No position exists, so there is nothing to sell. Recorded as the monitoring specification
that would apply if Q2 were ever re-opened by new facts — which is the honest use of this
question for a name that failed.*

**What would prove this run wrong, pre-committed [E1-02]:**
1. **A licence renewal disclosed at improved terms.** The first material expiries fall in
   **fiscal 2027**, i.e. within twelve to fifteen months. If QTL revenue *rises* through the
   FY2027–2031 renewal window while unit volumes are flat, the durability finding at Q2 was
   wrong and the file should be re-opened. **This is a dated, falsifiable test and it is the
   main one.**
2. **QCT holding EBT margin above 30% while handset revenue falls.** That would mean
   automotive and IoT carry a franchise margin, which the filing currently does not disclose.
3. **Reinstatement of a unit series.** If Qualcomm resumes publishing physical volumes,
   the **[E2-49]** flag clears and the **[E4-55]** moat metric becomes readable again.

**The thesis-breaking metric and its threshold:** **QTL EBT below $3,500M in any fiscal year**
(a 13% fall from FY2025) would confirm the repricing mechanism; **QTL EBT above $4,600M**
(above the FY2022 peak) would refute it.

**Next catalyst dates, from the filings:** the FY2026 10-K, expected early November 2026 —
the first annual report inside the fiscal-2027 expiry window; and the **Qualcomm v. Arm**
trial, scheduled **2026-03-09** in the District of Delaware, with **Arm's appeal of its own
loss pending in the Third Circuit** since 2025-10-01.

**The sell rule [E2-28] — not engaged; there is no holding.** **[E5-14]**'s do-not-trim rule
and the permanent class are not in play. **Position size: nil.**

- **VERDICT: NOT REACHED.**

---
## SELF-AUDIT

- [x] Questions answered in order; no verdict skipped. **Q1 IN → Q2 OUT → hard stop.**
      Q3–Q6 performed at the operator's explicit instruction and labelled **NOT REACHED** and
      **COMPUTATION — NOT A CLEARANCE** throughout (operator rule 3).
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the
      only IN and its dissent is recorded explicitly rather than hedged inside the verdict.
- [x] Every UNRESEARCHED verdict names the artifact — **there are none in this run.**
- [x] Every UNKNOWABLE states what specifically cannot be known — **three are recorded:**
      (a) Samsung System LSI, HiSilicon and UNISOC segment economics — no such document is
      published anywhere; (b) QCT EBT split by handsets/automotive/IoT — Qualcomm publishes
      revenue by stream and EBT only for QCT as a whole; (c) the mapping of customer/licensee
      (x)(y)(z) to Apple/Samsung/Xiaomi. **In each case I asked "can I name the document that
      would resolve this?" and the answer is no.**
- [x] Step 0: the filing was read with accession number; **three figures cross-checked**
      against the filed statements (capex $1,192M/$1,041M/$1,450M; OCF $14,012M; QTL EBT
      $4,043M read off Note 8 itself).
- [x] Owner earnings on a multi-year mean; **four windows published [E4-38]**; capex band
      disclosed as a judgment with its direction argued from the filing, not assumed.
- [x] **Competitor row filled** — 7 of the subject's 11 named peers, plus MediaTek from its
      own IR release and InterDigital added as the pure-licensing comparator. The four not
      obtained are recorded as UNKNOWABLE with the reason.
- [x] Sovereign is for the earnings currency, from the **issuing authority**, dated
      (2026-09-01), with the FRED fallback failure recorded.
- [x] Value stated as a **round-number range**, not a point estimate.
- [x] **One bar chosen** (screamer, display only); **windage count stated: one.**
- [x] **Prices dated; the aggregator flagged** — live quote $169.43 (2026-09-02) and the
      historical month-end closes used in the decomposition.
- [x] **Stage 0(a) share count done by hand from the cover page.** One class; 1,050M at
      2026-07-27; the screen's cap corrected up 3.2%, which moves every yield *down*.
- [x] Run committed to git — after Stage 0, after Q2, after Q4, and at completion.

**Errors and omissions in this run, recorded rather than absorbed [E4-26]:**
1. **The screen's "spread 16%" is wrong and this run says so.** The true width across the
   four windows and both capex ends is **59.0%**. The screen measured one corner to another.
2. **The screen's cap was 3.2% low.** Corrected by hand; it moves against the name.
3. **The screen's nine-year series is otherwise clean** — all nine years reconcile to the
   dollar. Unlike PLAB, there is nothing to correct in the series itself.
4. **I did not obtain the Apple agreement's term.** No document containing it exists on the
   public record: no Apple agreement is filed as a material contract, and "Apple" and
   "agreement" do not co-occur in the FY2025 10-K. **UNKNOWABLE, not UNRESEARCHED.**

## REGISTER

- Verdict: [ ] IN  **[x] OUT (about the business)**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
- **One line: Qualcomm contains a franchise and is not one — QTL earns 72% before tax on a
  patent estate whose licences expire between fiscal 2027 and 2031 and whose EBT is already
  38% below its FY2016 peak, but QTL is 12.6% of revenue, while the 87% that is QCT fails
  [E3-03](2) in the 10-K's own words because its three largest customers, 54% of revenue,
  build the substitute and one of them has already shipped it.**
- **THE PASS/FAIL LINE: FAIL. The file closed at Q2 (OUT).** Q1 returned IN; Q3, Q4, Q5 and
  Q6 were not reached and are recorded as computation only.
- **THE PRICE (COMPUTATION — NOT A CLEARANCE): roughly $100 to $155 a share, judged ~$100,
  against a quote of $169.43 on 2026-09-02.**
