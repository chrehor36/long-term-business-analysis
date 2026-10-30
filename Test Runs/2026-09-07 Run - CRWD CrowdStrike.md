# Company Run — CrowdStrike Holdings, Inc. (CRWD) — 2026-09-07
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

---
## STEP 0 — THE RATE, THE COVER, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- rate **5.24 %** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-yr
  (issuing authority; struck fresh this session, not the FRED fallback)**
- FX: none. CrowdStrike earns and reports in USD. (Revenue outside the US is billed largely
  in USD; no ADR ratio applies.)

**STAGE 0 — THE COVER COUNT, BY HAND. TWO SHARE CLASSES AND A 4-FOR-1 SPLIT.**

*Both halves of the operator's Stage 0 instruction fired, and the second one is material to
the price by a factor of four.*

1. **The two classes no longer exist.** The FY2026 10-K states: *"On December 11, 2024, all
   of our outstanding shares of Class B common stock automatically converted into an equal
   number of shares of Class A common stock pursuant to the provisions of the Amended and
   Restated Certificate of Incorporation."* The balance sheet confirms **0 shares of Class B
   issued and outstanding at both 2026-01-31 and 2025-01-31**. Economic equivalence is
   established from the filing's own charter description, not assumed: *"The rights of the
   holders of Class A and Class B common stock are identical, except with the respect to
   voting and conversion rights. As such, the undistributed earnings are allocated equally to
   each share of common stock without class distinction and the resulting basic and diluted
   net income (loss) per share attributable to CrowdStrike common stockholders are the same
   for shares of Class A and Class B common stock."* **Single class, economically identical,
   and the question is moot as of 2024-12-11.**
2. **A 4-FOR-1 SPLIT, EFFECTIVE 2026-07-01, VERIFIED BY HAND AGAINST THE FILING.** The
   Q2 FY2027 10-Q (accession `0001535527-26-000031`, filed 2026-08-27) says: *"On June 3,
   2026, the Company announced a **four-for-one split** of the Company's outstanding shares
   of Class A common stock in the form of a stock dividend… Each stockholder of record at
   the close of business on **June 25, 2026** … received, after the close of business on
   **July 1, 2026**, three additional shares for every share held."*
   - **10-K cover (2026-02-28, PRE-split): 253,614,090 shares.**
   - **10-Q cover (2026-08-20, POST-split): 1,023,934,842 shares.** ← **the count used.**
   - **Split guard, checked two independent ways, as the KLAC run requires:** the price feed
     carries a split event dated 2026-07-02 at 4.0/1.0; and 253,614,090 × 4 = 1,014,456,360
     against the filed 1,023,934,842 — a +0.93% difference over six months, which is ordinary
     net issuance, not a split artifact. **Both agree.**
   - Using the pre-split cover count against a post-split quote would have understated the
     market cap by 75%. This is the same class of error as the KLAC 10:1 guard.

- **price $213.10 · 2026-09-04 · aggregator, FLAGGED, live quote only** (operator rule 5)
- **shares 1,023,934,842** (10-Q cover, 2026-08-20, single class)
- **MARKET CAP = $213.10 × 1,023,934,842 = $218,201M**

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary: FY2026 10-K, FYE 2026-01-31, filed 2026-03-05, accession
  `0001535527-26-000010`.**
- Vintages also read in full for the disclosure-history tests: FY2025 `0001535527-25-000009`,
  FY2024 `0001535527-24-000007`, FY2023 `0001535527-23-000008`, FY2022 `0001535527-22-000006`,
  FY2021 `0001535527-21-000007`, FY2020 `0001535527-20-000006`.
- Fourteen 10-Qs read for the metric-withdrawal dating: Q1–Q3 of FY2023, FY2024, FY2025,
  FY2026 and Q1–Q2 FY2027 (`…-26-000031`, `…-26-000025`, `…-25-000033`, `…-25-000025`,
  `…-25-000019`, `…-24-000026`, `…-24-000020`, `…-24-000013`, `…-23-000026`, `…-23-000020`,
  `…-23-000014`, `…-22-000025`, `…-22-000018`, `…-22-000012`).
- **Figure cross-checked against the filed statement:** XBRL returns FY2026 operating cash
  flow of $1,612,349k. The filed Consolidated Statements of Cash Flows, page F-8 of the
  FY2026 10-K, shows **"Net cash provided by operating activities 1,612,349"** — agrees to
  the dollar. Second cross-check, because the SBC number decides this run: XBRL
  `ShareBasedCompensation` FY2026 = $1,096,679k; the filed cash-flow statement shows
  **"Stock-based compensation expense 1,096,679"** — agrees to the dollar.

---
## THE SCREEN ROW — REPRODUCED, AND IT IS THE SEVENTH CONSECUTIVE SPREAD DEFECT

**The published row** (`Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`, line 246):

    CRWD, cap_m 220,218 · oe_bottom_m 233 · oe_top_m 278 · spread 0.192 ·
    yield_bottom 0.0011 · vs_sovereign −0.0516 · growth_required 0.0989 ·
    level_shift 4.4 "STEP UP - normalize down [E4-41]" · best_year_dep 0.35 ·
    newest_filing 2026-01-31

**BOTH ENDS REPRODUCE TO THE DOLLAR AND THE WIDTH BETWEEN THEM IS NOT A WIDTH.**
Rebuilt by hand from the filed cash-flow statements:

- `oe_bottom 233` = the **5-year** (FY2022–26) mean of (OCF − SBC − PP&E capex) = **$233.1M**
- `oe_top 278` = the **3-year** (FY2024–26) mean of the *same construction* = **$277.7M**

**Two windows, ONE capex end.** The "19.2% spread" is a window spread wearing a capex band's
clothes. The framework requires the band to be the capex judgment **[E2-23], [E3-44], [E5-20]**
and the window spread to be carried *alongside* it **[E4-25]**; the row collapses them into
one number and reports neither.

**And the capex end it used was understated.** CrowdStrike's investing section has **two**
capital lines — *"Purchases of property and equipment"* **and** *"Capitalized internal-use
software and website development costs"*. The published row's arithmetic reproduces only when
the second line is excluded ($68.8M in FY2026 alone; $370.9M of true total capex against
$302.1M). This is exactly the case the operator flagged as the HAS fix: **capitalized software
sits on its own line and the tag list must catch it.** Re-running `floor_screen.owner_earnings`
on today's facts returns **188 / 219** rather than 233 / 278, because `capital_acquired()`
now resolves the software line — so the published row cannot be reproduced from current
tagged data at all, only from the omission.

**A third defect: `da_annual()` returns EMPTY for this filer.** No D&A element resolves,
so the screen never computed a D&A end at all. The corpus default for (c) **[E3-44, E2-41]**
was silently unavailable and the row never said so.

**REBUILT OVER SIX WINDOWS AND BOTH CAPEX ENDS, THE TRUE RANGE IS $114.3M – $308.4M — a
2.70x width (170%), against the published 19.2%.** (Table at Q4.)

**THE STEP, REBUILT — AND THE FLAG POINTS AT THE WRONG END OF THE SERIES.** `level_shift 4.40
"STEP UP — normalize down [E4-41]"` is computed on **operating cash flow**, which has indeed
stepped up 4.4x. **Owner earnings have not.** On my own construction, the four-year pre-step
mean (FY2019–22) at the capex end is **$30.4M** against the four-year recent mean (FY2023–26)
of **$198.3M** — a 6.5x step — but the series **peaked in FY2024 at $291.6M and has fallen in
each of the two years since, to $206.5M and then $144.8M, a 50% decline while revenue grew
57%.** The [E4-41] instruction to normalise down for a favourable window is right in
principle and inverted in application here: the recent years are the *weak* ones. Normalising
this series down means pricing off a level the company has already fallen below.

`best_year_dep 0.350` ("two years jointly carry the window") is likewise computed on OCF.
On the owner-earnings series the single best year ever filed is **FY2024 at $372.3M** (D&A
end) — a year now two years in the past.

**`growth_required 0.0989` reproduces exactly**: the screen solves `FLOOR − oe/cap` =
0.10 − 233/220,218 = **0.09894**. It is a *perpetual* Gordon growth rate at a 10% discount
rate, not a fading ten-year rate, and the run states both forms at Q5.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics, in my own words, without management's language.** CrowdStrike rents a
small program that a customer installs on every computer, server and cloud machine it owns.
The customer pays a fee per machine per year, and pays again for each extra capability
switched on for that same machine. The program watches what happens on the machine and sends
what it sees to CrowdStrike's own computers, which decide whether it is an attack. Customers
pay for the whole year up front, and often for two or three years up front; that is why cash
arrives long before revenue is booked, and why deferred revenue is **$4,753M** against
**$4,812M** of annual revenue. The company also sells emergency clean-up work by the hour
after a customer has been broken into; that is 5% of revenue and exists mostly to sell the
subscription. Gross margin is 75%. The cost of one more machine is the cost of storing and
processing its data, so an existing customer adding machines and capabilities is close to
pure margin, which is why the whole strategy is to sell more to people who already have it.

Two things about the money are unusual and both matter later:
- **Customers fund the business.** Total assets less goodwill, intangibles, cash and
  non-interest-bearing operating liabilities is **negative $1,073M**. Every operating asset,
  plus a further billion, is paid for by customers in advance. That liability is
  covenant-free and has no due date **[E3-52]**.
- **The employees take most of the cash.** Stock compensation was **$1,096.7M against
  $1,612.3M of operating cash flow — 68.0%.** That is not a footnote; it is the largest
  single claim on the cash the business produces, and it is settled by printing shares.

**The scarce input this business controls.** Not the software — competitors ship software.
The scarce thing is **the installed position**: one privileged agent already running inside
the customer's operating system on every machine, which the customer had to plan, test and
roll out, and would have to plan, test and roll out again to remove. Behind that sits the
aggregate telemetry from all of those agents, which is genuinely cumulative and which no
new entrant can synthesise. Neither the engineering talent nor the threat intelligence is
scarce to CrowdStrike specifically; the deployed footprint is.

**Will the fundamentals look broadly the same in ten years?** The revenue mechanism — pay
per machine per year, pay more per capability — is simple and I expect it to survive. The
*product* underneath it will not: research and development ran **$1,384.8M in FY2026, 28.8%
of revenue**, and that spending buys new modules, not the defence of an existing one. That is
the [E3-31] *"subject to constant change"* concern in its exact form. I record it here and
adjudicate it at Q2 under **[E4-04]**, which is where the framework puts the mechanism (does
the spending defend the same advantage, or buy its replacement?). **Q1 asks whether I can
understand how the money is made, and I can.**

- **VERDICT: [x] IN**
  *Recorded and carried forward: the [E3-31] constant-change clause is live and is decided
  at Q2, not waived here.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- Needed or desired **[x]** — yes, unambiguously. Endpoint security is not discretionary.
- No close substitute **[ ]** — **FAILS. See the price evidence below.**
- Not price-regulated **[x]** — no price regulation.

### THE FILED SERIES, ACROSS SEVEN VINTAGES

| as of Jan 31 | ARR ($M) | ARR growth | net new ARR | dollar-based net retention | subscription customers | customers with 4+ / 5+ / 6+ modules |
|---|---|---|---|---|---|---|
| 2018 | — | — | — | — | 1,242 | — |
| 2019 | — | — | — | — | 2,516 | — |
| 2020 | — | — | — | **124%** | 5,431 | — / ~33% / — |
| 2021 | — | — | — | **125%** | 9,896 | 63% / 47% / 24% |
| 2022 | 1,731.3 | 65% | 681.3 | **123.9%** | 16,325 | 69% / 57% / 34% |
| 2023 | 2,559.7 | 48% | 828.4 | **125.3%** | 23,019 | **WITHDRAWN** |
| 2024 | 3,435.2 | 34% | 875.5 | **119%** | **out of Key Metrics; 29,000 survives in Item 1** | withdrawn |
| 2025 | 4,241.8 | 23% | 806.7 | **112%** | **WITHDRAWN ENTIRELY** | withdrawn |
| 2026 | 5,252.8 | 24% | 1,010.9 | **115%** | withdrawn | withdrawn |
| **Jul 2026 (Q2 FY27)** | **5,841.4** | **25%** | 588.6 (6mo) | **NO NUMBER FILED** | withdrawn | withdrawn |

### **[E4-55] — WHERE UNITS EXIST, MONITOR UNITS. THEY DO NOT EXIST ANY MORE, AND THE DATING IS THE FINDING.**

*Precision Steel's pounds fell 69M → 46M while price rises held dollar revenue level — "a
serious reverse, not likely to disappear in some 'bounce back' effect." Dollar revenue
flattered by pricing is how a shrinking franchise hides; the physical series is the honest
one.* **[E4-55]**

**Three separate withdrawals, each dated to the filing:**

1. **SUBSCRIPTION CUSTOMERS — withdrawn in the 10-K filed 2023-03-09, with a stated reason.**
   The FY2023 10-K announced it in advance, which is the candid form **[E2-49]**: *"we
   believe that our subscription customer metric **no longer provides valuable insight into
   the performance of our business**. As a result, beginning in the first quarter of fiscal
   2024, we will no longer provide a number of subscription customers as a key metric."* The
   reason given is real — they moved down-market and through managed-service partners who are
   counted as one customer — but the effect is that **the only unit series the company ever
   filed is gone.** The count was still rising when it went (82% → 65% → **41%** growth), so
   this is not the classic deteriorating-yardstick case; it is the loss of the denominator.
   **The last unit datapoint of any kind in any filing is a prose sentence in Item 1 of the
   FY2024 10-K: *"As of January 31, 2024, we had 29,000 subscription customers worldwide."***
   Filed **2024-03-07**, four and a half months before the July 19 outage. Recorded sweep:
   the FY2025 and FY2026 10-Ks were searched for any customer count in any section — **no
   instance found.** The first annual report covering the outage is the first with no unit
   number anywhere in it. I record the sequence and do not assert causation.
2. **MODULE ADOPTION RATES — withdrawn in the SAME filing, 2023-03-09, with NO announcement
   and NO reason.** Last filed in the FY2022 10-K: *"As of January 31, 2022, **69%** of our
   customer base had adopted four or more modules, **57%** … five or more modules, and **34%**
   … six or more modules."* Recorded sweep: the FY2023, FY2024, FY2025 and FY2026 10-Ks were
   searched for any module-adoption percentage; **no instance found in any of the four.**
   The series was *rising* when it disappeared (63→69, 47→57, 24→34).
3. **THE QUARTERLY NET RETENTION NUMBER — replaced by an adjective in the 10-Q filed
   2023-08-31, and never restored.** This is the one that matters, and the sequence is exact:

| 10-Q, period ended | filed | what the filing says the net retention rate was |
|---|---|---|
| 2022-04-30 | 2022-06-03 | *"was **above 120%**"* |
| 2022-07-31 | 2022-08-31 | *"was **above 120%**"* |
| 2022-10-31 | 2022-11-30 | *"was **above 120%**"* |
| 2023-04-30 | 2023-06-01 | *"was **above 120%**"* |
| **2023-07-31** | **2023-08-31** | *"was **effectively at our benchmark**"* ← **THE SWITCH** |
| 2023-10-31 | 2023-11-29 | *"was **slightly below our benchmark**"* |
| 2024-04-30 | 2024-06-05 | *"was **consistent with our expectations**"* |
| 2024-07-31 (the outage quarter) | 2024-08-29 | *"was **consistent with our expectations**"* |
| 2024-10-31 | 2024-11-27 | *"was **115%**"* ← the one numeric reappearance |
| 2025-04-30 | 2025-06-04 | *"was **in line with our expectations**"* |
| 2025-07-31 | 2025-08-28 | *"**continued to be strong**"* |
| 2025-10-31 | 2025-12-03 | *"**increased … over the prior quarter**"* |
| 2026-04-30 | 2026-06-04 | *"**continued to be strong**"* |
| **2026-07-31** | **2026-08-27** | *"**improved sequentially**"* |

**THE PUBLISHED YARDSTICK — "above 120%" — WAS REPLACED BY AN UNPUBLISHED ONE — "our
benchmark" — IN THE FIRST QUARTER THE PUBLISHED ONE STOPPED BEING MET.** [E2-49] is written
for this: *"Yardsticks seldom are discarded while yielding favorable readings. But when
results deteriorate, most managers favor **disposition of the yardstick rather than
disposition of the manager**"* — and the demand is for *"**pre-set, long-lived and small
bullseyes**."* "Our benchmark" is nowhere defined in any filing. It is the opposite of a
pre-set bullseye: it is a bullseye drawn after the shot, and it was drawn **91 days** after
the last *"above 120%"* — a dating almost identical to the AAPL precedent's 86 days.

The annual number survives, but its **precision was cut in the same direction**: 123.9% and
125.3% (one decimal) in the FY2022 and FY2023 10-Ks; **119%, 112%, 115% (integers)** from the
FY2024 10-K onward — and the FY2024 10-K restates the prior year as "125%", rounding 125.3%
down. The decimal disappeared in the first vintage the number fell.

**Recorded sweep on the fourth metric the operator named: GROSS RETENTION.** CrowdStrike
claims in both the FY2025 and FY2026 10-Ks that *"we have maintained **high dollar-based
gross retention rates** following the incident."* **No gross retention rate number appears in
any of the seven 10-K vintages or any of the fourteen 10-Qs read.** The single strongest
piece of evidence for the switching-cost case is asserted and never filed. Under the
absence-claim rule: no instance found, in twenty-one filings searched.

### **[E2-44] — BOTH HALVES. THIS IS THE TEST THAT DECIDES Q2, AND IT DECIDES IT AGAINST.**

*Can it raise prices **"even when product demand is flat and capacity is not fully
utilized"**, and grow dollar volume **"with only minor additional investment of capital"**?*

**Half two passes and passes well.** Total capex including capitalized software is $370.9M
against $4,812M of revenue — 7.7%. Working capital is a **source**, not a use: deferred
revenue rose $1,023.9M in FY2026. Dollar volume grows on very little incremental capital.
This half is a genuine strength and it is why the business is not gruesome.

**Half one fails, and the company's own MD&A is the evidence.** The FY2026 10-K, Certain
Factors Affecting Our Performance:

> *"**Customer commitment packages** introduced following the July 19 Incident **have included
> discounting**, additional modules, professional services, flexible payment terms or
> subscription period extensions. Our customer commitment packages **have resulted, and are
> expected to continue to result, in increased contraction**, due to elongated subscription
> terms, and decreased upsell dollar values."*

**The framework's question is whether a franchise raises price and keeps the customer.
CrowdStrike kept the customer by cutting price, and says in its own filing that it expects
to keep doing so.** [E4-37] supplies the inverse metric — *"you can almost measure the
strength of a business over time by the agony they go through in determining whether a price
increase can be sustained"* — and here there was no agony because there was no attempt: the
tested response to the largest event in the company's history was a discount. That is a
[E3-03] criterion (2) failure. A customer who has no close substitute does not need to be
paid to stay.

### **THE JULY 19 INCIDENT, READ FROM THE FILINGS**

- **Date and mechanism, from the 10-K:** *"On July 19, 2024, the Company released a content
  configuration update for its Falcon sensor that resulted in system crashes for certain
  Windows systems."*
- **What it cost, from the rollforward in Note 10 (accrued and expensed, net of insurance
  receivable):** balance at 2024-01-31 **$0**; FY2025 expense **$60,062k**, payments
  $(38,917)k, balance **$21,145k**; FY2026 expense **$117,730k**, payments $(123,377)k,
  balance **$15,498k**. **Total $177.8M of expense over two years, $162.3M paid.** These sit
  in S&M, R&D and G&A — inside operating cash flow, so owner earnings already carries them.
- **Litigation, dated:** securities class action filed 2024-07-30 — **dismissed, final
  judgment entered 2026-01-28, no appeal taken, closed.** Airline-passenger class action
  filed 2024-08-05/19, consolidated — **dismissed 2025-06-18, on appeal to the Fifth
  Circuit.** Six derivative suits, all stayed. **Delta Air Lines** sued 2024-10-25 alleging
  *"computer trespass … intentional misrepresentation/fraud by omission, strict-liability
  product defect, gross negligence"*; motion to dismiss **granted in part and denied in
  part 2025-05-16; discovery ongoing.** No accrual is recorded for any of it: the company
  states it *"is not possible to estimate the amount of any loss or range of possible loss."*
- **What happened to retention and new customers in the four quarters after, from the
  filings and not from press:** net retention **119% → 112%** over the fiscal year containing
  the outage, then **112% → 115%** the year after. Net new ARR **$875.5M (FY2024) → $806.7M
  (FY2025) → $1,010.9M (FY2026)** — a dip of 8% in the outage year and then a record. ARR
  growth **34% → 23% → 24%**, and 25% at the latest quarter.

**WHAT THIS MEANS, STATED BOTH WAYS.** The operator's prior asked whether Q2 could be
genuinely WIDE because retention held through the outage. **It substantially did hold, and
that is the strongest evidence in this file.** A software vendor grounded airlines worldwide
and lost seven points of net retention, all of which it has since won back but three. Very
few businesses would survive that. It is real switching-cost evidence and I am not going to
minimise it.

**But it is switching-cost evidence, not franchise evidence, and the corpus separates the
two at exactly this point.** [E3-03](2) asks whether customers *think there is no close
substitute*. The filed answer is that they had to be paid — in discounts, free modules, free
professional services and extended terms — to keep thinking it, and that the paying is
ongoing. A franchise is a business that *"is thought by its customers to have no close
substitute"*; a business that must fund the belief is a business with high switching costs
and a credible substitute on the other side of them. [E4-32] settles the direction question:
*"the moat widened every year"* is *"the primary criterion of a great business"*. This moat
was **narrowed by a self-inflicted event, has been partly rebuilt at the company's own
expense, and is not yet back to where it was.** Direction over the measurable window is
negative, and the three series that would let an outsider check it were withdrawn.

### **[E4-04] — MUST THE MOAT BE CONTINUOUSLY REBUILT?**

The framework's test: *does a lapse in spending destroy the structure, or merely narrow it —
and does the spending defend the same advantage, or buy its replacement?* CrowdStrike spent
**$1,384.8M on R&D (28.8% of revenue)** and **$1,272.4M on acquisitions in FY2026 and the
five weeks after** (Pangea $212.1M, Onum $252.7M, Seraphic $327.4M closed 2026-02-03, SGNL.AI
$627.9M closed 2026-02-20 — the last two disclosed as subsequent events). The 10-K names the
purpose: to *"expand the functionality of our Falcon platform, add to our technology or
security expertise, or bolster our leadership position by **gaining access to new customers
or markets**."* **That is buying the replacement, not defending the trademark.** It is the
Mitsui/Rhodes Ridge shape, not the Coca-Cola shape. The one thing that would survive a
spending lapse is the installed agent — real, but narrowing, not widening, without the spend.

**Key-person dependence, recorded at Q2 as a moat defect [E4-23], not at Q3 as a strength:**
George Kurtz is co-founder, CEO and the public face of the company through the outage. The
10-K carries a named risk factor on his departure. Recorded.

### THE COMPETITOR ROW — required **[E3-28]**

*(filled below from the peer filings; a moat is a claim about relative position and cannot be
evidenced from one company's numbers)*

**Peers named: 4 of the 4 the industry actually has as filed comparables** (Buffett says
eight; endpoint/platform security has four SEC registrants that can be put in the same row,
and Microsoft only at the honest rung described below). Full working, with 21 accession
numbers, in `Test Runs/_research 2026-09-07 CRWD/COMPETITOR_ROW.md`.

| same metric, latest filed year | **CRWD** FY26 | PANW FY25 | S FY26 | FTNT FY25 | MSFT FY26 |
|---|---|---|---|---|---|
| Revenue | $4,812.0M | $9,221.5M | $1,001.3M | $6,799.6M | $331,839M |
| Gross margin | 74.7% | 73.4% | 74.1% | **80.5%** | 67.9% |
| Subscription gross margin | 77.7% | 72.5% | not filed | **86.8%** | 64.7% |
| **GAAP operating margin** | **(6.1)%** | 13.5% | (32.1)% | **30.7%** | **46.8%** |
| GAAP net income | **$(161.2)M** | $1,133.9M | $(450.7)M | $1,853.4M | $133,749M |
| **SBC ÷ operating cash flow** | **68.0%** | 34.9% | 388.4% | **10.8%** | **6.8%** |
| Net tangible operating assets | $(1,149.8)M | $(4,649.6)M | $(213.3)M | $(1,902.1)M | $373,852M |
| Net retention filed? | 115% | **none filed** | **withdrawn** (last 110%) | **none filed** | n/a |

**The attacker metric, with the caution the operator required.** Net tangible operating
assets is **negative for all four pure-plays** — customers fund the entire operating asset
base. That is a genuine structural strength shared across the group **[E3-52]**, and it makes
[E2-43]'s unleveraged-net-tangible-assets return **not meaningful** for any of them: dividing
CrowdStrike's loss by its negative denominator returns a spurious *positive* 25.5%, which
this run names and refuses rather than prints. **[E3-46]'s question — "the best businesses,
by definition, are going to be businesses that earn very high returns on capital employed
over time" — cannot be answered on this denominator, so it is answered on operating margin,
where CrowdStrike is last of five.**

**Microsoft, at its honest rung, and it is a blocked rung.** Recorded sweep of the FY2026
(`0001193125-26-323660`) and FY2025 (`0000950170-25-100235`) 10-Ks: **no filed security
revenue figure exists** — zero instances of a dollar figure attached to security, no security
line in the ten-line revenue disaggregation, one generic mention of Defender in a competition
sentence, zero of Sentinel. The widely-quoted "$20bn+ security business" is an earnings-call
number and is **off this framework's evidence ladder**. **The Microsoft-versus-Falcon question
is therefore UNRESEARCHED-becoming-UNKNOWABLE from filings**, and the Q2 verdict below does
not rest on it. Microsoft's own completed run established the switching-cost argument at its
Q2; nothing in Microsoft's filings lets me size the security business against CrowdStrike's.

**PANW's column is a full year stale**: the FY2026 10-K is not filed as of 2026-09-07
(submissions feed verified; only an 8-K, `0001327567-26-000019`, 2026-09-01). Named, not
patched.

**THE STRONGEST FACT FOR CROWDSTRIKE IN THE WHOLE ROW, AND IT IS THE [E2-45] ATTACKER'S TEST
RUN IN REVERSE.** *"how I would like, assuming I had ample capital and skilled personnel, to
compete with it."* **Every pure-play peer names CrowdStrike by legal entity name in its
competition section, under securities liability, and CrowdStrike names no one.** SentinelOne
lists *"CrowdStrike Holdings, Inc."* as the first name in its first competitor category; Palo
Alto lists it among independent security vendors; Fortinet names it twice. CrowdStrike's own
FY2026 10-K contains **zero named competitors** and asserts that no competitor has *"a true
platform offering equivalent to the Falcon platform."* This is the datable-language evidence
class and it runs in CrowdStrike's favour.

**THE STRONGEST FACT AGAINST, AND IT IS THE RATIO THE OPERATOR ASKED FOR.** CrowdStrike is
**the only filer in the row running a GAAP operating loss, and its stock compensation is 3.7×
that loss** ($1,096.7M of SBC against a $(293.3)M operating loss). On SBC ÷ OCF it is at
**68.0%** against Fortinet's **10.8%** and Microsoft's **6.8%** — and it is **the only
company in the row moving the wrong way**, rising in each of the three observable years:
**55.6% → 62.3% → 68.0%.** Fortinet earns a *higher* subscription gross margin (86.8% vs
77.7%) on a 30.7% operating margin. The ratio has no definitional slack in it.

**THE ROW'S LIMIT, STATED [E3-61].** *"In some businesses, the participants behave like a
demented Kellogg. In other businesses, they don't … I think you'd have to know the people
involved."* And two more limits specific to this row: **CrowdStrike's 115% net retention is
uncontested rather than winning** — PANW and FTNT file no retention metric at all, and
SentinelOne **withdrew** its number in FY2026 while keeping the heading (*"Our NRR remained
in expansionary territory"*, last filed 110%), so there is nothing filed to rank 115% against.
**Metric withdrawal is an industry habit, not a CrowdStrike habit**: Palo Alto withdrew
billings outright in its FY2024 10-K (*"Beginning in the first fiscal quarter of 2025,
billings will no longer be a key financial metric and will no longer be reported"* — last
value $10,208.1M, growth having decayed 37.0% → 23.1% → 11.0%). Only Fortinet withdrew
nothing. **This materially softens the [E2-49] reading at Q3: CrowdStrike did what its
industry does.** It does not soften [E2-44], which is a question about price and is answered
by CrowdStrike's own MD&A.

- **Untapped pricing power [E3-33] / [E5-28]?** **No.** Claiming that class is claiming
  near-monopoly, and the competitor row does not support it. The opposite is filed: the
  company discounted into its largest test.
- Class: **NARROW**, and **narrowing over the measured window**.
- **VERDICT: [x] OUT — on [E3-03] criterion (2), evidenced by the company's own MD&A.**

### **WHY THIS IS NOT "WIDE", STATED AT FULL STRENGTH FIRST [E4-51, E4-26]**

*"I'm not entitled to have an opinion unless I can state the arguments against my position
better than the people who are in opposition."* **[E4-51]** The operator pre-registered that
Q2 might be genuinely WIDE if net retention held through the outage. **It substantially did,
and here is that case put as well as I can put it:**

> On 19 July 2024 CrowdStrike shipped an update that crashed millions of Windows machines,
> grounded airlines, stopped hospitals and became the largest IT outage in history. **Twenty-
> five months later the company has more annual recurring revenue than ever, added a record
> $1,010.9M of net new ARR in the year after the incident, is growing ARR at 25%, and its
> net retention rate — 119% before, 112% at the trough, 115% now, and "improved sequentially"
> at the latest quarter — never once went below 100%.** No cohort of customers left. There is
> no better natural experiment on switching costs available anywhere in this queue: the
> product failed catastrophically and publicly, and the customers stayed. The securities
> class action was dismissed with final judgment and no appeal. Every pure-play competitor
> names CrowdStrike in its own competition section under securities liability; CrowdStrike
> names none of them. On the [E2-45] attacker's test — *"how I would like … to compete with
> it"* — the honest answer is that I would not want to, and the peer filings say the same.

**That case is real and I am not discounting it. Here is why it does not carry Q2 anyway.**

**[E3-03] criterion (2) is not "customers stay". It is that the product is *"thought by its
customers to have no close substitute."*** Those are different claims, and CrowdStrike's own
MD&A settles which one is true: the customers stayed **because they were paid to**, in
*"discounting, additional modules, professional services, flexible payment terms or
subscription period extensions"*, and the company says in the same sentence that these
packages *"have resulted, and are expected to continue to result, in increased contraction …
and decreased upsell dollar values."* A customer with no close substitute does not have to
be compensated, and the compensation does not have to be ongoing two years later. What the
outage proved is that **switching costs are high** — which is a fact about the difficulty of
leaving, not about the absence of an alternative. High switching costs and a credible
substitute are perfectly compatible, and the discount is the price of the gap between them.

**[E2-44](1) is the framework's price test and there is no filed evidence CrowdStrike passes
it.** *Can it raise prices "even when product demand is flat and capacity is not fully
utilized"?* CrowdStrike files no ASP, no price list, no unit count and no physical series of
any kind, so the test cannot be run on a price series — it can only be run on the one natural
experiment the company actually had, and in that experiment **it cut price.** [E4-37] supplies
the inverse metric: *"you can almost measure the strength of a business over time by the agony
they go through in determining whether a price increase can be sustained."* There was no
agony because there was no attempt.

**[E4-32] settles direction, which the framework says outranks existence.** *The moat widened
every year* is *"the primary criterion of a great business."* Over the only window that can be
measured, this moat **narrowed** — self-inflicted, then partly and not fully rebuilt at the
company's own expense — and **the three series that would let an outsider check the rebuild
were all withdrawn before it could be checked.**

**What would flip this verdict, named in advance so it is falsifiable:** a filed dollar-based
**gross** retention rate at or above 97% for four consecutive quarters, published as a number;
or the restoration of the quarterly net-retention number to a **pre-set, published** bullseye
in the sense [E2-49] demands; or a filed statement of a list-price increase taken and held. Any
one of those is a document I can name, so this verdict is reviewable — but it is **OUT, not
UNRESEARCHED**, because the documents that exist have been read and they answer the question.

**Q2 CLOSES THE FILE. Everything below this line is recorded because the operator's brief
asked for it and because a closed file still owes the register its findings. None of it is a
verdict, and per operator rule 2 none of it can promote the name.**

---

## THE CONTINGENT-ROYALTY FLAG — IT FIRES, AND IT IS NOT A ROYALTY. IT IS PAYROLL SETTLED IN STOCK.

The operator flagged 4+ year-ends of persistent contingent-consideration liability at ~$45M
and predicted the payments would sit in FINANCING where the owner-earnings numerator never
sees them. **The persistence is real and worse than four years. The location is worse than
financing.**

| as of Jan 31 | `BusinessCombinationContingentConsiderationLiability` | source accession |
|---|---|---|
| 2021 | $5.3M | `0001535527-21-000007` |
| 2022 | $18.5M | `0001535527-22-000006` |
| 2023 | $7.9M | `0001535527-23-000008` |
| 2024 | $3.6M | `0001535527-24-000007` |
| 2025 | $18.4M | `0001535527-25-000009` |
| **2026** | **$45.4M** | `0001535527-26-000010` |

**Six consecutive year-ends. It amortised almost to zero by FY2024 ($3.6M) and then went up
12.6x in two years.** But reading the note rather than the tag changes what it is. The FY2026
10-K, in the equity-award footnote:

> *"The above table **excludes founder holdbacks** related to business combinations where a
> variable number of shares will be issued upon vesting to settle a **fixed monetary amount of
> $45.4 million, contingent upon continued employment with the Company.** The share price will
> be determined based on the Company's average stock price … five days prior to each vesting
> date. During the fiscal year ended January 31, 2026, 19,560 shares were issued to settle
> founder holdbacks at a weighted average price of $470.56 per share."*

**Three findings, in ascending order of seriousness:**

1. **It is not an earnout on revenue and not a royalty.** It is a retention payment to the
   founders of acquired companies, conditioned on continued employment. Economically it is
   **compensation**, and it belongs beside the $1,096.7M of SBC, not beside goodwill.
2. **It is settled in shares, so it never touches ANY section of the cash flow statement —
   not financing, not investing, not operating.** The operator's prediction was that the
   payments would hide in financing. They hide better than that: there is no cash payment at
   all. The equity statement carries it as *"Issuance of common stock for founders holdbacks
   related to acquisitions"* — **$4,314k (FY2026), $3,555k (FY2025), $9,204k (FY2024)** — and
   the owner-earnings numerator, built from operating cash flow, cannot see it by construction.
3. **The filing says in terms that it is EXCLUDED from the equity-award table** — the table an
   outside reader would use to size total dilution. A fixed $45.4M obligation, settled in a
   variable number of shares, contingent on employment, sitting outside the disclosed award
   table. It is small against $1,096.7M of SBC, and I am not going to inflate it. **But the
   flag was right to fire, and the correct reading is that it makes owner earnings slightly
   too high, not too low.** The operator's hypothesis (b) — that handling the contingent
   liability correctly might lift owner earnings — is **refuted**: handling it correctly
   lowers them.

---

## TESTS RUN BELOW THE CLOSED GATE — RECORDED, NOT VERDICTS

### (c) — THE DIRECTION TEST **[E3-44, E2-41, E5-20]**, AND THE HAS FIX CATCHES THE TAG

**Which case is this?** The corpus default is that D&A is a fair proxy for (c) **[E3-44,
E2-41]**; the exception class is the business whose own filing shows depreciation understates
renewal **[E5-20]**. **CrowdStrike is in the exception class, and not for the railroad reason.
Capex has exceeded D&A in every single filed year:**

| FY | total capex | total D&A | capex ÷ D&A |
|---|---|---|---|
| 2022 | $133.0M | $68.8M | **1.93x** |
| 2023 | $264.1M | $93.8M | **2.82x** |
| 2024 | $226.0M | $145.3M | **1.56x** |
| 2025 | $313.8M | $214.0M | **1.47x** |
| 2026 | $370.9M | $281.5M | **1.32x** |

**So the D&A end of the band is the GENEROUS end here and (c) is judged at TOTAL CAPEX.**

**The HAS fix caught the tag, and it is worth $68.8M in FY2026 alone.** CrowdStrike's
investing section carries capital on **two** lines — *"Purchases of property and equipment"*
($302,108k) and *"Capitalized internal-use software and website development costs"*
($68,751k). The published screen row used only the first. Capitalized software is **inside**
property and equipment on the balance sheet (the PP&E note carries *"Capitalized internal-use
software and website development costs 265,987 / 183,117"* as a component), so its
amortisation is already inside the $250.2M D&A line — **omitting the cash line from (c) while
keeping its amortisation in D&A double-counts in the company's favour.** The cash line is the
right figure to use: gross software additions were $120.3M in FY2026, of which ~$51.5M was
capitalised SBC already subtracted in the SBC line, so taking the $68.8M cash figure avoids
double-counting.

### **THE ONE NUMBER, AND IT IS THE POINT OF THIS RUN [E5-06, E3-70]**

> *"To say 'stock-based compensation' is not an expense is even more cavalier."* — **[E5-06]**

**SBC ÷ operating cash flow, CrowdStrike, by fiscal year:**

| FY | operating cash flow | stock compensation | **SBC ÷ OCF** |
|---|---|---|---|
| 2020 | $99.9M | $79.9M | 80.0% |
| 2021 | $356.6M | $149.7M | 42.0% |
| 2022 | $574.8M | $310.0M | 53.9% |
| 2023 | $941.0M | $526.5M | 56.0% |
| 2024 | $1,166.2M | $648.7M | 55.6% |
| 2025 | $1,381.7M | $861.4M | 62.3% |
| **2026** | **$1,612.3M** | **$1,096.7M** | **68.0%** |
| H1 FY2027 | $1,121.2M | $674.6M | 60.2% |

**THE PINS YARDSTICK, MEASURED.** Pinterest's $880M against $1,284M was **68.5%**, and its
single best year in history still yielded 3.16% against the bond. **CrowdStrike is at 68.0% —
the same place, to within half a point — and it got there by rising in each of the last three
years while Pinterest's was a level.** The half-year improvement to 60.2% is real and is
recorded; one half-year is not a trend and the FY2026 full year is the filed figure.

**And [E3-70] says the reported charge is the FLOOR of the subtraction, not the measure:**
subtract *"an amount equal to what the company could have realized by publicly selling options
of like quantity and structure."* CrowdStrike's awards are overwhelmingly RSUs and PSUs, whose
grant-date fair value is the share price, so the charge is close to the market measure here —
but the $45.4M of founder holdbacks sits **outside** the disclosed award table, and $51.5M of
FY2026 SBC was capitalised into software rather than expensed. **$1,096.7M is a floor.**

**WHAT THE RATIO DOES TO THE BUSINESS, IN ONE COMPARISON.** Over four years:

| | FY2022 | FY2026 | CAGR |
|---|---|---|---|
| Revenue | $1,451.6M | $4,812.0M | **+34.9%/yr** |
| Operating cash flow | $574.8M | $1,612.3M | **+29.4%/yr** |
| **Owner earnings, (c) = capex** | **$131.8M** | **$144.8M** | **+2.4%/yr** |
| **Owner earnings, (c) = D&A** | **$196.0M** | **$234.2M** | **+4.6%/yr** |

**Revenue tripled, operating cash flow tripled, and owner earnings did not move.** Between
FY2024 and FY2026 owner earnings at the capex end **fell from $291.6M to $144.8M, −29.5% a
year, while revenue grew 57%.** Every incremental dollar of operating cash flow over the last
three years was claimed by stock compensation and capital spending: OCF rose $446.1M from
FY2024 to FY2026; SBC rose $448.0M.

**Buybacks against issuance.** The board authorised $1.0bn on **2025-06-03** and a further
$500M on **2026-04-06** ($1.5bn total). Actual repurchases: **zero in FY2026**, $50.6M in
Feb–Mar 2026 at $351.97 pre-split (= $87.99 post-split), and **$175.6M in H1 FY2027** at
~$91 post-split. Against $1,096.7M of a single year's SBC, **$226.2M of buyback offsets 20.6%
of one year's issuance.** It is dilution mop-up, not a return of capital. *(Fairly stated the
other way, and it is a point for management: they bought at ~$88–91 against a $213.10 quote
today. On the [E5-24] test — "what is smart at one price is dumb at another" — that is the
right direction, unlike the KLAC pattern. The scale is the criticism, not the timing.)*

### Q3 ITEMS — NO VERDICT IS WRITTEN, THE GATE IS CLOSED. **[E2-49, E3-48, E4-52, E4-22]**

**Weight case, declared as the template requires.** Daily execution **[x] TICKED** — this is
the [E2-70] *"their only products are promises"* shape in its purest modern form: a company
whose product is an agent with kernel-level privilege on every machine a customer owns, where
one bad content update on one Friday produced the largest IT outage in history. **Q3 is a
BINARY GATE for this business, not an overlay, and no price compensates [E1-16, E3-29,
E5-35].** Control and leverage are not ticked.

**[E2-49] METRIC-SWITCHING — FIRES, AND THE PROXY IS WORSE THAN THE 10-K.** Beyond the three
disclosure withdrawals dated at Q2, the compensation plan itself moves its own bullseyes:
- The **Net Retention Rate modifier band was lowered from 115%–120% to 110%–115%** for FY2026,
  *after* the metric fell out of the bottom of the old band in Q4 FY2025 (the 2025 proxy:
  *"119%, 118%, 115%, and 112% … falling within our target range, **other than with respect to
  the fourth quarter**"*). Under the new band, 112% is mid-range. The stated reason —
  *"As companies scale, net retention rates typically moderate from early-stage levels"* — is
  a reason, and it arrived in the year the miss did.
- The **non-GAAP operating income funding threshold was lowered from 85% to 80%** for FY2026.
- The **PSU revenue metric changed unit** from a growth percentage to an absolute dollar
  figure for FY2026, and the band narrowed from **20 points wide (FY2024)** to **4 points
  (FY2025)** to **1.31% of revenue (FY2026)**.

**THE TARGET-BELOW-ACTUAL TEST — THE FIFTH REPLICATION. HIT, CLEANLY, ON THE 70%-WEIGHTED
METRIC.**

| | $M |
|---|---|
| FY2024 **actual** net new ARR (FY2024 10-K) | 875.5 |
| FY2025 **target** net new ARR (2025 proxy) | **775.0** |
| target minus prior-year actual | **−100.5 (−11.5%)** |
| FY2025 **actual** net new ARR | 806.7 — **down 7.9% year over year** |
| CEO cash bonus paid | **106.0% of target, $1,325,064** |

The target carrying **70% of the entire cash bonus** was set 11.5% below what the company had
already delivered; the company then delivered less than the prior year; and the bonus paid
above target. *(Stated fairly: the FY2024 and FY2026 targets were both set ABOVE the prior
year's actual, and the non-GAAP EPS leg of the test is NOT clean because the non-GAAP
definition changed for FY2026 — on the recast base the FY2026 band sits above prior-year
actual. One clean hit in three years, on the heaviest-weighted metric.)*

**THE SHARPEST SINGLE FINDING IN THE PROXY — THE PSU BAND *IS* THE GUIDANCE RANGE, TO THE
CENT.**

| FY2026 PSU band (2026 proxy) | FY2026 guidance issued 2025-03-04 (8-K `0001535527-25-000005`) |
|---|---|
| Revenue **$4,743.5M – $4,805.5M** | Total revenue **$4,743.5 – $4,805.5 million** |
| Non-GAAP EPS **$3.33 – $3.45** | Non-GAAP diluted EPS **$3.33 – $3.45** |

**The 50%-of-target threshold is the bottom of management's own published guidance and the
200%-of-target maximum is the top of it.** Actual revenue came in at $4,812.1M — **0.14% above
the maximum** — and the PSUs paid **200% of target**. This is [E3-48] and [E3-50] converging:
management sets the guidance, management is paid on beating the guidance, and the whole
distance from half pay to double pay is **1.31% of revenue**. Under **[E4-52]** — *"extreme
consequences from **confluences** of psychological tendencies acting in favor of a particular
outcome"* — **the guidance flag, the metric-switching flag and the pay structure are not three
prompts; they are one reinforcing system**, and it is exactly the system [E5-30] warns is a
ratchet: *"once you start it, it's all over. You can't quit."*

**[E4-22] WEAK ACCOUNTING — one live item, dated.** The FY2026 10-K discloses that in **Q4
FY2026** the company *"identified an **immaterial error** related to the timing of recognition
of stock-based compensation expense in prior periods associated with certain awards granted in
the fiscal years ended January 31, 2022 and 2023. Specifically, stock-based compensation
expense was attributed based on such awards' vesting schedule, rather than on a straight-line
basis."* Prior balance sheets, income statements, equity and cash-flow statements were revised.
The correction is to **the very line this run turns on**, and it was found by the company, in
the fourth quarter, four years after the grants. *(Fairly stated: no cash-flow impact in any
period, no equity impact, revisions of $4.0M and $(17.1)M at the net-income line — genuinely
small — and the company found and published it.)*

**[E4-29] EBITDA — DOES NOT FIRE, AND THE ABSENCE IS CLEAN.** Recorded sweep: **zero
occurrences of "EBITDA" and zero of "non-GAAP" in the FY2024, FY2025 and FY2026 10-Ks.** The
non-GAAP apparatus is heavy in the earnings releases and the proxy, but the annual report
itself is GAAP throughout. That is a real point in management's favour and it is recorded as
one.

**PAY VERSUS PERFORMANCE, from the Item 402(v) table, 2026 proxy, as filed:**

| FY | PEO SCT total | **PEO Compensation Actually Paid** | CRWD TSR ($100) | **Peer TSR ($100)** | GAAP net income |
|---|---|---|---|---|---|
| 2026 | $247,579,143 | **$330,345,041** | 204.54 | **256.43** | **$(161,165)k** |
| 2025 | $35,195,300 | $148,504,806 | 184.46 | 204.12 | $(12,566)k |
| 2024 | $46,983,855 | $343,689,775 | 135.54 | 159.97 | $73,439k |
| 2023 | $36,532,681 | $(111,653,036) | 49.07 | 106.58 | $(182,285)k |
| 2022 | $147,695,746 | $34,920,193 | 83.71 | 126.43 | $(232,378)k |

**CrowdStrike underperformed its own chosen peer index (S&P 500 Information Technology) in
every one of the five years the table shows.** Over the window, PEO Compensation Actually Paid
totals **$745.8M** against **cumulative GAAP net income of $(515.0)M**. The five measures the
company names as most important are Non-GAAP Operating Income, Net New ARR, Net Retention
Rate, Revenue Growth Percent and Non-GAAP EPS — **no GAAP measure, and no return-on-capital or
per-share measure, appears among them.** [E2-01] asks for *"a high earnings rate on equity
capital employed … **and not the achievement of consistent gains in earnings per share**"*;
CrowdStrike's own scorecard contains neither.

**[E2-01] THE PRIMARY TEST — the multi-year series, run.** Return on equity capital employed
is **negative in five of the last six years** (net income $(92.6)M, $(232.4)M, $(182.3)M,
$73.4M, $(12.6)M, $(161.2)M against year-end equity rising to $4,472.6M). And [E2-43]'s
denominator does not rescue it: **unleveraged net tangible operating assets are NEGATIVE
$1,073M**, so the ratio is undefined rather than high, and this run refuses to print the
spurious positive that dividing a loss by a negative denominator produces.

**THE HONESTY BINARY [E5-16] — ONE OPEN MATTER, AND IT IS THE MOST SERIOUS ITEM IN THE FILE.**
FY2026 10-K, Note 10, verbatim:

> *"The Company has received requests for information from the **U.S. Department of Justice**
> and the **U.S. Securities and Exchange Commission** relating to the Company's **recognition
> of revenue and reporting of ARR for transactions with certain customers**, the July 19
> Incident and related matters. The Company is cooperating and providing information in
> response to these requests."*

**The two headline metrics of the entire franchise case — revenue recognition and ARR — are
the subject of a Department of Justice and SEC inquiry.** No accrual is recorded and the
company states it cannot estimate a range of loss. **This is a request for information, not a
charge, not a finding, and not an allegation against any person, and [E5-38] governs how it is
read: a fired flag is not a venality finding.** But [E5-22] governs the other half — *penalty
size is not seriousness, in either direction* — and the item is recorded, dated to the FY2025
10-K (2025-03-10) when it first became public, and carried forward. **Q3 would be
UNRESEARCHED-pending on this matter alone even if Q2 had passed**, because the document that
resolves it (a closing letter, or a charge) does not yet exist.

### Q4 ITEMS — RECORDED. **[E2-23, E5-11, E2-60, E2-54, E3-52]**

**OWNER EARNINGS, BY YEAR AND BY WINDOW. EVERY WINDOW PUBLISHED [E4-38].**
*(OE = OCF − SBC − (c). Figures $M, from the filed cash-flow statements, originally-filed
XBRL with the FY2026 revisions flagged.)*

| FY | OCF | SBC | OCF−SBC | total capex | total D&A | **OE @ (c)=capex** | OE @ (c)=D&A |
|---|---|---|---|---|---|---|---|
| 2019 | (23.0) | 20.5 | (43.5) | 42.6 | 15.4 | (86.1) | (58.9) |
| 2020 | 99.9 | 79.9 | 20.0 | 87.5 | 23.5 | (67.5) | (3.5) |
| 2021 | 356.6 | 149.7 | 206.9 | 63.7 | 40.2 | 143.2 | 166.7 |
| 2022 | 574.8 | 310.0 | 264.8 | 133.0 | 68.8 | 131.8 | 196.0 |
| 2023 | 941.0 | 526.5 | 414.5 | 264.1 | 93.8 | 150.4 | 320.7 |
| **2024** | 1,166.2 | 648.7 | 517.5 | 226.0 | 145.3 | **291.6** | **372.3** ← peak |
| 2025 | 1,381.7 | 861.4 | 520.3 | 313.8 | 214.0 | 206.5 | 306.4 |
| **2026** | 1,612.3 | 1,096.7 | **515.7** | 370.9 | 281.5 | **144.8** | 234.2 |

**"OCF − SBC" has been flat at $515–520M for three consecutive years** while revenue grew 57%.

| window | OE @ (c)=capex | OE @ (c)=D&A |
|---|---|---|
| 3-year FY2024–26 | $214.3M | $304.3M |
| 4-year FY2023–26 | $198.3M | $308.4M |
| **5-year FY2022–26 (corpus default [E2-42, E1-03])** | **$185.0M** | $285.9M |
| 6-year FY2021–26 | $178.1M | $266.1M |
| 7-year FY2020–26 | $143.0M | $227.5M |
| 8-year FY2019–26 (all filed) | $114.3M | $191.7M |

- **COMBINED RANGE (window spread × capex band): $114.3M to $308.4M — a 2.70x width (170%).**
  Against the published screen row's 19.2%.
- **Is the range too wide to reach a conclusion [E4-25]?** **No, and that is the unusual thing
  about this name.** The band is 2.7x wide and it does not matter: **every point in it, at
  every window and both capex ends, produces a yield between 0.05% and 0.14% against a 5.24%
  sovereign.** The width would have to be roughly **sixty-fold** to change the answer. This is
  Bar 2's third outcome — *price above the whole range* — reached without needing the range
  resolved.
- **Distorted year in the window [E5-11]?** Yes, and it is FY2024, the peak, now two years
  past. **[E4-41] normalise-down applies but points the opposite way to the screen's flag:**
  the screen's `level_shift 4.40 "STEP UP — normalize down"` is computed on operating cash
  flow. **Owner earnings peaked in FY2024 and have fallen 50% since.** Normalising this series
  down means pricing off a level the company has already fallen below.
- **Judged owner earnings: $185M** — the 5-year corpus-default window at (c) = total capex,
  because capex has exceeded D&A in every filed year and the D&A end is therefore the generous
  one. **Windage count: ONE.** Conservatism is spent at the capex end of (c) and nowhere else
  [E4-11, E4-48]. The deferred-revenue sensitivity below is presented as a *finding*, not as a
  second haircut.

**[E2-23] CONSTRAINT 3 — THE WORKING-CAPITAL INCREMENT, AND IT RUNS BACKWARDS HERE.** The
convention nets working capital through operating cash flow. For CrowdStrike that increment is
a **source**, not a use: deferred revenue rose **$1,023.9M** in FY2026 alone. Read as **[E3-52]**
reads it — *"liabilities **without covenants or due dates** attached to them … the benefit of
debt … but saddle us with none of its drawbacks"* — this is a genuine and unusual strength,
and it is why net tangible operating assets are negative $1,073M. **But it is the growth of
that liability, not its existence, that produces the reported cash flow**, and the sensitivity
is computable from the filed statement:

    FY2026 OCF                                              $1,612.3M
    less the increase in deferred revenue                   $(1,023.9)M
    = operating cash flow ex-prepayment-growth                 $588.4M
    less stock compensation                                 $(1,096.7)M
    = ($508.3)M
    less total capex                                          $(370.9)M
    = ($879.2)M

**Stop the growth and the business consumes $879M a year.** This is not a forecast and it is
not subtracted from the judged figure; it is the single most important structural fact about
where the reported cash comes from, and it is the named death mechanism below.

**GREAT, GOOD OR GRUESOME [E4-20] — IT DOES NOT FIT THE TAXONOMY, AND SAYING WHY IS THE
FINDING.** Not gruesome: it does not *"require you to keep adding money"* — capex is 7.7% of
revenue and working capital is a source. Not great: the rate is not high and, decisively, it is
**not rising** — owner earnings have fallen two years running. **The taxonomy is built on cash
added to a savings account, and CrowdStrike's deposits are not made in cash. They are made in
ownership.** The business does not consume capital; it consumes the shareholders' share of
itself, at $1,096.7M a year. Nearest class: **GOOD, and deteriorating** [E4-43].

**STAYING POWER — ALL THREE SCORED [E5-11].**
1. **A large and reliable stream of earnings — SPLIT.** Revenue is as reliable as revenue gets:
   $5,252.8M of ARR under contract, $4,753.4M of deferred revenue, $4.2bn of unbilled backlog,
   customers who did not leave after the worst outage in the industry's history. **Earnings are
   the opposite of reliable**: GAAP operating loss in every year of the company's existence,
   widening $(19.1)M → $(116.4)M → $(293.3)M, and owner earnings down 50% in two years. **The
   revenue passes and the earnings do not, and [E5-11] asks about earnings.**
2. **Massive liquid assets — PASSES, emphatically.** $5,230.1M of cash and equivalents against
   $750M of senior notes. 7.0x coverage of all debt in cash alone.
3. **No significant near-term cash requirements — THE ONE THAT USUALLY KILLS, AND IT IS THE
   ONE THAT BITES HERE.** Non-cancelable purchase obligations, from Note 10: **FY2027
   $600.2M · FY2028 $661.0M · FY2029 $627.6M** — **$1,888.9M over three years**, for data
   centre capacity and the like, contracted and not cancellable. Add **$955.3M of acquisitions
   that closed in the five weeks after the year end** (Seraphic $327.4M on 2026-02-03, SGNL.AI
   $627.9M on 2026-02-20), plus $464.8M spent on Pangea and Onum inside FY2026 — **$1,420.1M of
   cash acquisitions in thirteen months against $185M of judged owner earnings.** The cash pile
   covers it; the owner earnings do not come close. Buffett's *"cash is a lot like oxygen"*
   **[E5-39]** test is passed only by the balance sheet, never by the earnings.

**[E2-54] COVERAGE — trivially passed.** Interest paid $22.5M against $1,612.3M of operating
cash flow net of $370.9M of capex. 55x. **Leverage is not this business's risk and no ratio is
imposed** — the framework has none and the corpus supplies none for subject companies.

**ASC 842 — immaterial and recorded as such.** Operating lease liabilities $18.2M current +
$56.4M non-current = **$74.6M**, against $11,086.7M of assets. Right-of-use assets are on the
balance sheet, the FY2026 non-cash lease cost was $17.2M, and $40.9M of new ROU assets were
added. **No off-balance-sheet lease finding.** The real long-dated commitment is the $1,888.9M
of data-centre purchase obligations, which is not a lease and is disclosed in Note 10.

**[E2-60] RESTRICTED EARNINGS — DOES NOT FIRE, for the mechanical reason.** *"a company that
consistently distributes restricted earnings is destined for oblivion."* CrowdStrike pays **no
dividend** and has never paid one, so nothing is distributed and the [E2-52] issuance-funded-
dividend flag cannot fire either. The buyback is funded from a cash balance that grew $990.0M
in the year. **Recorded as not applicable, having been tested.**

**[E5-08] THE TWO BUYBACK CONDITIONS.** (1) **Ample funds — YES**, unambiguously: $5.2bn of
cash, $990.0M of net cash generated in FY2026. (2) **A material discount to conservatively
calculated intrinsic value — NO, and it is not close.** On this run's range the zero-growth
value at the sovereign is $2–$6 per share and repurchases were executed at $88–$91. **[E4-31]'s
third condition also fails**: *"Shareholders should have been supplied all the information they
need for estimating that value"* — and the three series that would let a shareholder estimate
it were withdrawn between 2023-03-09 and 2023-08-31. **CAPITAL-ALLOCATION FLAG RAISED**, stated
with the humility clause **[E4-13]**: this rests on our own range, and management knows this
business far better than we do; *"many CEOs never stop believing their stock is cheap"*
**[E5-08]**. **It binds position size only, never the discount rate.**

**THE ABSOLUTE-SIZE ACQUISITION GATE.** `acquisition_flag` returns **$1,364.4M of goodwill =
0.62% of market cap** — far below the 15% threshold, so the queue's read-the-note trigger does
not fire on the balance-sheet test. **It fires on the FLOW test instead, which the screen does
not compute:** $1,420.1M of cash paid for four businesses in thirteen months, against $185M of
owner earnings and $1,612.3M of operating cash flow. **Acquisitions consumed 88% of operating
cash flow in the trailing year.** Goodwill rose from $912.8M to $1,363.3M in FY2026 and will
rise again on SGNL.AI and Seraphic. **[E4-39]: recorded sweep for a post-mortem — no
acquisition post-mortem, no revisit of any deal against its announcement case, in any of the
seven 10-K vintages. No instance found.** [E3-40]'s *loss of focus* vector is the thing to
watch: four acquisitions in thirteen months, all bolt-ons to the platform rather than
adjacencies, which is the *better* reading of the two available.

**NAME THE SPECIFIC WAY THIS BUSINESS DIES [E2-27, E3-24, E4-40] — MODEL EXPOSURE, NOT
EXPERIENCE.** The corpus's named failure mode for this exercise is *"focusing on **experience,
rather than exposure**"* **[E4-40]**, so the mechanism below comes from what the filing shows
the business is exposed to, not from what has recently happened to it.

> **The mechanism: the prepayment engine reverses while the compensation ratchet does not.**
> CrowdStrike's reported operating cash flow is produced by the *growth* of customer
> prepayments, not by its earnings. In FY2026, $1,023.9M of the $1,612.3M of operating cash
> flow was the increase in deferred revenue. Stock compensation, meanwhile, is a ratchet: it
> rose 27.3% in FY2026 and cannot be cut without losing the engineers who build the modules
> that produce the ARR growth that produces the prepayments. **The two are coupled in one
> direction only.**
>
> **Quantified from the filed figures**, as set out above: with the deferred-revenue increment
> at zero and FY2026's actual SBC and capex, the business runs at **negative $879.2M a year**.
> A softer and more likely version: if operating cash flow merely stops growing (it grew 16.7%
> in FY2026) while SBC continues on its three-year trend (+27.3%), owner earnings at the capex
> end go **negative within one year** — $1,612.3M − $1,396.2M − $400M = **$(183.9)M**.
>
> **The trigger that produces it** is the one the competitor row cannot price: bundling. The
> only participant that can make endpoint security a feature rather than a product is
> Microsoft, and **Microsoft files no security revenue figure at all**, so the exposure is
> real and unmeasurable from filings. The second trigger is a second incident — and the
> exposure to that is structural and permanent, because the product is a privileged agent
> pushing content updates to every machine a customer owns. The customer-commitment packages
> show what the *first* one cost in price; a second would arrive with the discount already
> given and the DOJ and SEC already in the file.
>
> **Likelihood: a real possibility on a ten-year view; a low-level possibility within three.**
> ARR growth is 25% and stable, the cash balance is $5.2bn, and nothing forces the reversal
> soon. Ten years is the framework's horizon, not three.

---

## COMPUTATION — NOT A CLEARANCE

**Operator rule 3. The file closed at Q2. The arithmetic below is reported because the queue's
output contract requires a price either way, and it carries NO ENTRY LANGUAGE. Q5 was not
opened and no ranking position is assigned.**

- **sovereign 5.24%** (US Treasury 30-yr, 2026-09-04, issuing authority) — **the bare rate,
  no per-name premium added [E3-42]**
- **price $213.10** (2026-09-04, aggregator, flagged) · **shares 1,023,934,842** (10-Q cover,
  2026-08-20, post-split, single class) · **market cap $218,201M**
- **owner earnings $114.3M – $308.4M** across six windows and both capex ends; **judged
  $185M** (5-year corpus default, (c) = total capex)

**1. THE YIELD**

| construction | owner earnings | yield | vs the 5.24% sovereign |
|---|---|---|---|
| 8-year, (c)=capex | $114.3M | **0.052%** | **−5.19 pts** |
| **5-year, (c)=capex — JUDGED** | **$185.0M** | **0.085%** | **−5.16 pts** |
| 5-year, (c)=D&A | $285.9M | 0.131% | −5.11 pts |
| 4-year, (c)=D&A — the best window available | $308.4M | 0.141% | −5.10 pts |
| **the single best year ever filed (FY2024, (c)=D&A)** | **$372.3M** | **0.171%** | **−5.07 pts** |

**Below the bond on every construction, including the best year the company has ever filed at
the most generous capex end. The gap is roughly five full points wide in every cell.**

**2. WHAT THE PRICE ALREADY ASSUMES**
- **Perpetual growth needed to reach the [E4-28] 10% floor: 9.92% a year, forever** (the
  screen's own form, `FLOOR − oe/cap`; reproduces its published 9.89% at its inputs).
- **Year-1 growth needed, fading to 2.5% over ten years, discounted at 10%: 141.8%.**
- **What the business has actually done: owner earnings +2.4%/yr (capex end) and +4.6%/yr
  (D&A end) over four years, and −29.5%/yr over the last two.** Revenue did +34.9%/yr and
  operating cash flow +29.4%/yr over the same window and none of it reached the owner.
- **[E4-35]'s base rate:** *"fewer than 10 of the 200 most profitable companies in 2000 will
  attain 15% annual growth in earnings-per-share over the next 20 years."* The requirement here
  is 9.92% **in perpetuity** — a longer commitment than the wager Buffett offered — from a
  company whose owner earnings have gone backwards for two years.
- **[E4-44]'s second bound:** *"the value of an asset … cannot over the long term grow faster
  than its earnings do."* **[E2-63]'s ceiling:** the upside is bounded by a 74.7% gross margin
  that is already 3rd of 5 in the peer row and by an operating margin that is last of 5 and
  falling.

**3. WHAT YOU ARE PAID**
- **−5.16 points against the sovereign** at the judged figure; −5.07 points at the most
  flattering figure in the file.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]**

| | |
|---|---|
| conservative (8-yr, capex end, zero growth at the sovereign) | **~$2 / share** |
| judged (5-yr, capex end, zero growth at the sovereign) | **~$3.50 / share** |
| optimistic (best window, D&A end, zero growth at the sovereign) | **~$6 / share** |
| at the [E4-28] 10% floor instead of the sovereign | **~$1 to ~$3 / share** |
| **current price** | **$213.10** |

**The quote is ~61x the judged zero-growth value and ~37x the top of the entire zero-growth
band.** Bar 2 **[E4-01]**, outcome three: **price above the whole range.** No margin is
subtracted and none needs to be — *"startlingly low"* is what you observe, and this is its
opposite. **Windage count: ONE** (the capex end of (c)); no premium in the rate [E3-42], no
second haircut for the deferred-revenue sensitivity.

**THE [E4-28] FLOOR VERDICT, WHICH IS AS FAR AS THE FILE GETS:** honest pre-tax expectancy at
this price is **~0.1% plus growth**. Even granting the required 9.92% perpetual growth as a
free gift, expectancy is exactly 10.0% — i.e. the floor is only reached if the growth
assumption is *precisely right forever*. **Below the floor, this is quit on, not ranked
[E4-28] — "that's the figure we quit on"** — and it never had the chance to be ranked, because
Q2 closed the file.

---

## SELF-AUDIT
- [x] Questions answered in order; stopped at the first verdict that is not IN (Q2 OUT)
- [x] No question marked IN carries an "unverified" or "provisional" caveat
- [x] Q1 IN is clean; the [E3-31] constant-change concern is recorded and adjudicated at Q2,
      not waived
- [x] Q2 OUT names the corpus test it fails ([E3-03] criterion 2, [E2-44] half one) and quotes
      the company's own MD&A as the evidence
- [x] The counter-case is stated at full strength BEFORE the verdict, per [E4-51], and the
      operator's pre-registered "Q2 may be WIDE" hypothesis is engaged directly and answered
- [x] Every absence claim names its recorded sweep (gross retention: 21 filings; module
      adoption: 4 vintages; customer count: 2 vintages; EBITDA/non-GAAP: 3 vintages;
      acquisition post-mortem: 7 vintages; MSFT security revenue: 2 vintages)
- [x] Step 0: the filing was read, with accession number; **two** figures cross-checked to the
      dollar against the filed cash-flow statement (OCF and SBC)
- [x] Stage 0 done by hand: both share classes resolved (Class B converted 2024-12-11,
      economic equivalence read off the charter description), **4-for-1 split of 2026-07-01
      caught and verified two independent ways**, post-split cover count used
- [x] Owner earnings on a multi-year mean; **six windows published in full [E4-38]**; capex
      band disclosed as a judgment with the direction test shown
- [x] Competitor row filled — 4 peers, all four the industry has as filed comparables; the
      Microsoft rung is named as blocked rather than patched with press numbers
- [x] Sovereign is for the earnings currency, from the issuing authority, dated, struck fresh
- [x] Value stated as a round-number range, not a point estimate
- [x] One bar chosen (Bar 2, outcome three); **windage count stated: ONE**
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] Q5 was NOT opened; all valuation arithmetic is headed COMPUTATION — NOT A CLEARANCE and
      carries no entry language (operator rules 2 and 3)
- [x] Screen row reproduced to the dollar before being criticised
- [x] Run committed to git

## REGISTER
- **Verdict: OUT (about the business), at Q2.**
- **One line:** CrowdStrike's customers proved after the largest IT outage in history that
  they will not leave — but the company's own MD&A says it kept them by discounting and
  expects to keep discounting, which is a switching-cost finding and not a franchise; and the
  three series that would let an outsider check the rebuild were withdrawn between 2023-03-09
  and 2023-08-31, the quarterly net-retention number being replaced by *"effectively at our
  benchmark"* 91 days after it last cleared its own published 120% bar.
- **The price, under COMPUTATION — NOT A CLEARANCE: $213.10** against a zero-growth value of
  **~$2 to ~$6 per share**, judged **~$3.50**.
- **PASS / FAIL: FAIL. The file closed at Q2 (OUT) — the second question, not on price.** It
  would also have failed Q5 on price by roughly five points against the sovereign on every
  construction including the best year ever filed.
