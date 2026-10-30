# Company Run — Palantir Technologies Inc. (PLTR) — 2026-09-11
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

*RUN LOG: file created 2026-09-11 under the write-early protocol before any fetch; the
session was killed at the 22:10 ET limit with only the header on disk; resumed 2026-09-12
09:55 ET and the research rebuilt. Sections are appended as each closes; commits after each
gate. Research: `Test Runs/_research 2026-09-11 PLTR/`.*

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
## STEP 0 — THE RATE, THE COVER, AND THE FILING

### The sovereign, for the currency the business EARNS in **[E4-15, E3-32]**
- rate **5.35 %** · date **2026-09-11** · source **US Treasury daily par yield curve, 30-yr
  (issuing authority; struck fresh this session via `tools/sources.py` with the cache
  cleared; not the FRED fallback).** The brief carried 5.37% for 2026-09-10; the 2026-09-11
  print is 5.35% and that is the one used — read, not inherited.
- FX: none. Palantir reports in USD; *"Our contracts with customers and vendors are
  primarily denominated in U.S. dollars"* (FY2025 10-K, MD&A). 74% of FY2025 revenue and
  80% of H1 2026 revenue is from US customers. No ADR ratio.

### STAGE 0 — THE COVER COUNT, BY HAND. THREE CLASSES, AND THE THIRD IS THE ONE THAT MATTERS.

`python Screens/cover_shares.py PLTR`:

    10-Q filed 2026-08-04, period 2026-06-30, accession 0001321655-26-000041
    Class A Common Stock                              2,300,713,329
    Class B Common Stock                                101,340,151
    Class F Common Stock                                  1,005,000
    --- arithmetic sum, NOT a share count ---         2,403,058,480
    MULTIPLE CLASSES. Whether these are economically equivalent is a JUDGMENT
    from the charter, not arithmetic. READ THE FILING.

**The judgment the tool refuses to make, made here from the filing's own description of
the charter (FY2025 10-K, Note 9, Stockholders' Equity):**

> *"The Company's Class A, Class B, and Class F common stock (collectively, the 'common
> stock') **all have the same rights, except with respect to voting and conversion
> rights.** Class A and Class B common stock have voting rights of 1 and 10 votes per share,
> respectively. The Class F common stock has the voting rights generally described herein
> and **each share of Class F common stock is convertible at any time, at the option of the
> holder thereof, into one share of Class B common stock.** All shares of Class F common
> stock are held in a voting trust established by Stephen Cohen, Alexander Karp, and Peter
> Thiel (the 'Founders'). The Class F common stock generally gives the Founders the ability
> to control up to 49.999999 % of the total voting power of the Company's capital stock, so
> long as the Founders and certain of their affiliates collectively meet a minimum ownership
> threshold, which was 100.0 million of the Company's equity securities as of December 31,
> 2025."*

> *"Holders of the common stock are entitled to dividends when, as, and if declared by the
> Company's Board of Directors."* — same note, no class distinction.

**DECISION, three parts:**
1. **All three classes are economically equivalent and summing them is correct.** Same
   rights except voting and conversion; one undivided "Common stock" line on the balance
   sheet ($2,403k par at 2026-06-30); one basic and one diluted EPS struck across all
   classes ($0.44 / $0.41 for Q2 2026, on 2,399,820k basic weighted shares, which is the
   three-class total). Class B converts 1:1 into Class A; Class F converts 1:1 into Class B.
   **The difference is votes, not money.** This is the CRWD/SHOP finding again, with a
   third class added.
2. **Class F is 1,005,000 shares — 0.04% of the count — and carries up to 49.999999% of
   the vote.** Unlike Shopify's Founder Share it is not economically empty: it converts
   into Class B and shares in dividends. Its 1,005,000 shares are therefore counted at
   face, and the arithmetic is unaffected either way.
3. **The governance finding is recorded at Q3, not here.** A class engineered so that
   *"future issuances of our Class A common stock will dilute the voting power of our Class
   A common stockholders but may not result in further dilution of the voting power of our
   Founders"* (FY2025 10-K, Item 1A) is a live Q3 item under **[E2-26]** and the queue test
   of **[E3-66]**. It is not a share-count adjustment.

**COUNT USED: 2,403,058,480** (10-Q cover, as of the filing's own as-of date, all three
classes). The 10-K cover at 2026-02-10 was 2,291,470,751 + 99,199,960 + 1,005,000 =
2,391,675,711; the six-month increase of 11.4M shares (+0.48%) is net issuance, no split.

**AND THE COUNT THAT IS NOT ON THE COVER.** At 2025-12-31 (FY2025 10-K, Note 10):
**152.2 million options outstanding at a weighted $9.98 exercise price** (aggregate intrinsic
value $25.5 billion), **41.6 million unvested RSUs**, and 11.3 million SARs. Treasury-method
net of the options at $167.23 is 143.1M shares; with the RSUs, **the claims already granted
add ~185M shares (7.7%) to the cover count.** Cap is shown both ways below; the verdict does
not depend on which.

- **price $167.23 · 2026-09-11 close · aggregator, FLAGGED, live quote only** (operator rule 5)
- **MARKET CAP = $167.23 × 2,403,058,480 = $401,863M** (cover count) · **$432,754M** with the
  granted-but-unissued claims above.
- The screen row's `cap_m 436282` implies $181.55/share on the same 2,403M count, i.e. a
  price from an earlier date; on the cover count the screen did sum the three classes, and
  on the charter reading above that happened to be right. The brief's warning that the cap
  "may itself be wrong for exactly this reason" is **refuted for this filer**: the classes
  are equivalent, so the sum is the count.

### The filing was read — not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary: FY2025 Form 10-K, FYE 2025-12-31, filed 2026-02-17, accession
  `0001321655-26-000011`** (document `pltr-20251231.htm`).
- **Newest periodic: Q2 2026 Form 10-Q, period 2026-06-30, filed 2026-08-04, accession
  `0001321655-26-000041`.** Also read: Q1 2026 10-Q `0001321655-26-000028`; Q2 2025 10-Q
  `0001321655-25-000106`.
- **Vintages read for the SBC, customer-count and segment series:** FY2024 10-K
  `0001321655-25-000022`; FY2023 `0001321655-24-000022`; FY2022 `0001321655-23-000011`;
  FY2021 `0001193125-22-050913`; FY2020 `0001193125-21-060650`; S-1/A of 2020-09-21
  `0001193125-20-250103`.
- **Proxies:** DEF 14A filed 2026-04-24 `0001321655-26-000019`; DEF 14A 2025-04-25
  `0001321655-25-000057`.
- **Earnings releases (8-K EX-99.1), as the queue's standing rule for Q3 requires:** Q2 2026
  `0001321655-26-000039` (2026-08-03); Q1 2026 `0001321655-26-000026`; Q4 2025
  `0001321655-26-000004`; Q3 2025 `0001321655-25-000130`; Q4 2024 `0001321655-25-000007`;
  Q4 2023 `0001321655-24-000010`; Q4 2022 `0001321655-23-000005`.
- **Figures cross-checked against the filed statement (operator rule 4):**
  1. XBRL `NetCashProvidedByUsedInOperatingActivities` FY2025 = $2,134,473k. The filed
     Consolidated Statements of Cash Flows reads **"Net cash provided by operating activities
     2,134,473"** — agrees to the dollar.
  2. **SBC, because the brief said it decided CRWD:** XBRL `ShareBasedCompensation` FY2025
     = $684,033k; the filed cash-flow adjustments block reads **"Stock-based compensation
     684,033"** — agrees to the dollar. Cross-checked in every vintage: the FY2022 10-K reads
     564,798 / 778,215 / 1,270,702 for 2022/2021/2020 and the tagged values are identical;
     the FY2020 10-K reads "Net cash used in operating activities (296,608) (165,215)
     (39,012)" for 2020/2019/2018 — identical.
  3. **Capex:** filed "Purchases of property and equipment (33,882)" against XBRL
     `PaymentsToAcquirePropertyPlantAndEquipment` $33,882k — agrees.
  4. **Segment revenue reconciles to the total:** Government $2,402,287k + Commercial
     $2,073,159k = $4,475,446k = filed total revenue.

---
## THE SCREEN ROW — REPRODUCED, AND THE `n/a`s ARE CORRECT **[E4-25]**

**The published row** (`Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`, line 242):

    PLTR, cap_m 436,282 · oe_bottom_m 247 · oe_top_m 696 · spread 1.817 ·
    yield_bottom 0.0006 · vs_sovereign -0.0531 · growth_required 0.0994 ·
    level_shift n/a "EARLY HALF STRADDLES ZERO" · level_shift_oe n/a "SIGN CHANGE" ·
    best_year_dep 0.458 "ONE YEAR CARRIES THE WINDOW" · (8 years filed) ·
    acq_note "NET CASH INFLOW on the acquisition line ($67M)" · newest_filing 2025-12-31

**Both ends reproduce to the dollar.** `oe_bottom 247` is the **5-year (2021–25) mean at the
D&A end** of (c) = $247.0M; `oe_top 696` is the **3-year (2023–25) mean at the capex end** =
$695.8M. Two windows, two capex ends, and the "spread" is the two mixed — the same
construction defect the CRWD and SHOP runs recorded. The four-construction width is 182%; the
true width over every window is below.

**The `n/a`s are right, for the SHOP reason: the eight-year series is not one company.** Every
figure from a filed cash-flow statement, $M:

| year | OCF | SBC | **SBC ÷ OCF** | capex | D&A | **OE @ (c)=capex** | OE @ (c)=D&A |
|---|---|---|---|---|---|---|---|
| 2018 | (39.0) | 248.5 | n/m (OCF < 0) | 13.0 | 13.9 | **(300.5)** | (301.4) |
| 2019 | (165.2) | 242.0 | n/m | 13.1 | 12.3 | **(420.3)** | (419.5) |
| **2020** | (296.6) | **1,270.7** | n/m | 12.2 | 13.9 | **(1,579.5)** | (1,581.2) |
| 2021 | 333.9 | 778.2 | **233.1%** | 12.6 | 14.9 | **(456.9)** | (459.2) |
| 2022 | 223.7 | 564.8 | **252.5%** | 40.0 | 22.5 | **(381.1)** | (363.6) |
| 2023 | 712.2 | 475.9 | **66.8%** | 15.1 | 33.4 | **221.2** | 202.9 |
| 2024 | 1,153.9 | 691.6 | **59.9%** | 12.6 | 31.6 | **449.7** | 430.7 |
| **2025** | **2,134.5** | **684.0** | **32.0%** | 33.9 | 26.1 | **1,416.6** | 1,424.4 |
| **TTM to 2026-06-30** | **3,400.3** | **835.5** | **24.6%** | 42.1 | 27.9 | **2,522.7** | 2,536.9 |

*(H1 2026: OCF $2,115.3M, SBC $466.8M — 22.1%; H1 2025: $849.5M, $315.3M — 37.1%. The 2020
SBC of $1,270.7M is the direct-listing year: RSUs with a liquidity-event condition recognised
at once. `acq_note` reproduces: the $66.7M is the FY2022 "Business combinations, net of cash
acquired" line, a net **inflow** because a step-acquisition consolidated more cash than was
paid.)*

**Every window, both (c) ends [E4-38]:**

| window ending 2025 | (c) = capex | (c) = D&A |
|---|---|---|
| 1y (2025) | $1,416.6M | $1,424.4M |
| 2y (2024–25) | $933.1M | $927.6M |
| **3y (2023–25)** | **$695.8M** ← screen top | $686.0M |
| 4y (2022–25) | $426.6M | $423.6M |
| **5y (2021–25)** | $249.9M | **$247.0M** ← screen bottom |
| 6y (2020–25) | **$(55.0)M** | $(57.7)M |
| 7y (2019–25) | $(107.2)M | $(109.4)M |
| 8y (2018–25) | $(131.4)M | $(133.4)M |

**The range crosses zero at the six-year window, so no percentage width is definable
(the PINS class), and the honest statement is in dollars and a word: from MINUS $133M to PLUS
$1,417M on the filed years, and $2,523M on the trailing twelve months — a series whose sign
depends on the window.** `best_year_dep 0.458` understates it: drop 2025 from the five-year
window and the mean falls from $249.9M to **$(41.8)M** — the sign changes, as it did at SHOP.

**[E4-41] — WHICH YEARS DESCRIBE THE BUSINESS THAT EXISTS NOW?** Three facts date the
break: the first GAAP operating profit (2023, $120.0M); the first year SBC fell below
operating cash flow (2023, 66.8%); and the launch of AIP in 2023, to which the filings
attribute the US commercial acceleration. **The business that exists now is 2023-onward,
three and a half years. The earlier five are a different company — loss-making, paying its
staff more in stock than it collected in cash — and are shown, not used.** The multi-year
mean the corpus asks for **[E2-42]** is therefore taken over 2023–25 ($696M) and 2024–25
($933M), with the single year ($1,417M) and the TTM ($2,523M) as the top of the display.
**Every one of those four is used at Q5; the verdict does not depend on which.**

`growth_required 0.0994` reproduces (0.10 − 247/436,282). It is the perpetual Gordon rate at
a 10% discount, and it is a meaningless number for a business growing 56%: the fading-rate
form is computed at the COMPUTATION section below.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### Unit economics, in my own words, without management's language

A government agency or a company has data scattered across dozens of systems that were
never designed to talk to each other. Palantir sends its own engineers in, connects those
systems, and builds a model of the organisation — its people, assets, orders, suppliers,
targets — that the customer's staff then use to make decisions and, since 2023, that
language models can be pointed at. The customer pays a subscription for the software, either
hosted by Palantir on a hyperscaler's cloud or installed on the customer's own machines,
with the running and maintenance bundled in, and pays for services on top when it needs them.
Contracts run one to five years and revenue is recognised ratably. **$4,475M of revenue in
FY2025 from 954 customers — $4.7M per customer on average, and $93.9M each for the top
twenty, who between them are 42% of revenue.**

Two things about the money are unusual:
- **It is very cheap to serve once installed.** Cost of revenue is 18% of revenue; capex is
  **$33.9M on $4,475M of revenue — 0.76%** — because the computing runs on Amazon's,
  Microsoft's and Google's capital, bought as "third-party cloud hosting services" inside
  cost of revenue. Net property and equipment is **$61.4M**. Contribution margin, the
  company's own segment measure (revenue less cost of revenue and sales and marketing, ex
  SBC), is **66%** in both segments.
- **The customer base is two customers deep in one place.** *"Customer I represented 27%
  and 25% of total accounts receivable as of June 30, 2026 and December 31, 2025"* (Q2 2026
  10-Q); no customer is over 10% of revenue in any period. The filing does not name
  Customer I. Government is 54% of revenue; the US is 74% (FY2025) and 80% (H1 2026).

### THE FILED SEGMENT SPLIT, EVERY VINTAGE — the brief asked for it across vintages

| year | Government $M | growth | Commercial $M | growth | Gov share | Gov contribution | Comm contribution | US % | customers | employees |
|---|---|---|---|---|---|---|---|---|---|---|
| 2020 | — | — | — | — | — | — | — | 52% | **139** | 2,439 |
| 2021 | — | — | — | — | — | — | — | 57% | **237** | 2,920 |
| 2022 | 1,071.8 | — | 834.1 | — | 56% | — | — | 61% | **367** | 3,838 |
| 2023 | 1,222.2 | +14% | 1,002.8 | +20% | 55% | 59% | 52% | 62% | **497** | 3,735 |
| 2024 | 1,569.6 | +28% | 1,295.9 | +29% | 55% | 60% | 60% | 66% | **711** | 3,936 |
| **2025** | **2,402.3** | **+53%** | **2,073.2** | **+60%** | **54%** | **66%** | **66%** | **74%** | **954** | 4,429 |
| H1 2026 | 1,848.4 | +78% | 1,719.6 | +103% | 52% | — | — | **80%** | **1,049** (TTM) | 4,401 |

*(Segment tables begin in the FY2023 10-K; FY2022 government/commercial from the FY2024
10-K's three-year table. Q2 2026 alone: US commercial $764M +149%, US government $809M
+90%, from the 8-K EX-99.1.)* **Revenue per employee went from $448k (2020) to $1,011k
(2025); headcount rose 82% while revenue rose 310%.**

### [E4-55] — WHERE UNITS EXIST, MONITOR UNITS. THEY EXIST, AND THIS IS THE FIRST RUN IN SEVEN TO FIND THEM.

Six consecutive runs found no unit series. **Palantir files one, every year and every
quarter, with a stated definition that has not changed since the S-1:** *"We define a customer
as an organization from which we have recognized revenue during the trailing twelve-month
period."* 139 → 237 → 367 → 497 → 711 → 954 → 1,049 (June 2026 TTM). **Growth 71%, 55%,
35%, 43%, 34%, and 24% year-on-year at June 2026 (849 → 1,049).** The count has decelerated
in each of the last three prints while revenue growth accelerated from 17% to 93% — which
means **revenue per customer is doing the work**: $4.7M per customer in 2025 against $4.0M in
2024, and the top-twenty average rose 45% in a year. That is the honest reading of the
physical series and it is carried to Q2: the growth is expansion inside accounts more than
new logos.

**[E2-49] metric-withdrawal test — the prior that fired at SHOP and MRVL and failed at QLYS,
CRM and CORT: it FAILS here.** Recorded sweep of six 10-K vintages and the Q2 2026 10-Q: the
customer count is present in every one, same definition, same placement. **Net dollar
retention:** recorded sweep of the FY2023, FY2024 and FY2025 10-Ks — **zero instances of the
phrase in any of the three**, and zero in the seven 8-K EX-99.1 releases read. It has never
been a filed metric, so nothing was withdrawn; the number lives in the investor
presentation, which is off this framework's evidence ladder. **Remaining deal value** is
filed with a government/commercial split ($4.4bn / $6.8bn at 2025-12-31, +90% / +117%) and
**RPO** is filed ($4.1bn at 2025-12-31, $4.9bn at 2026-06-30, 43% inside twelve months).

### The scarce input this business controls

Not the software as such — Snowflake, Databricks and the hyperscalers sell data platforms.
Not the models — Palantir's own filings say AIP runs other people's language models. **The
scarce thing is the built ontology inside each customer: the integration of that customer's
particular systems, done by Palantir engineers on site, on which the customer's daily
operations then run.** Ripping it out is not a software migration; it is rebuilding the
organisation's operating picture. In government there is a second scarce input: **cleared
engineers and accredited deployments** — *"certain personnel may be required to receive
various security clearances"* — and a statute, which is treated at Q2 because it is a moat
question.

### Will the fundamentals look broadly the same in ten years?

**The revenue mechanism will:** subscriptions for an integrated data layer, sold to large
organisations, with services on top. **The product underneath has been rebuilt three times
in a decade** — Gotham, then Foundry, then AIP — and the filings attribute the acceleration
since 2023 to AIP and to *"demand for AI sovereignty"*. That is **[E3-31]**'s *"subject to
constant change"* clause in exact form, and it is adjudicated at Q2 under **[E4-04]** and
**[E3-51]** (does the spending defend the same advantage, or buy its replacement; is the run a
surfing run). **Q1 asks whether I can understand how the money is made, and I can,
completely**: two segments filed with contribution, one geography split, one unit series,
one deal-value series, a cash-flow statement whose every line reconciles, and no debt.

- **VERDICT: [x] IN**
  *Carried forward to Q2, not waived here: (a) the constant-change clause; (b) growth is
  inside accounts more than new logos; (c) 54% of revenue is from a customer class that
  writes its own contract terms; (d) the filing attributes its government growth to a
  statute.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The brief asked for the two halves tested separately, and they come out differently. Both
are set out at full strength before either is judged [E4-51].**

### THE GOVERNMENT HALF — 54% of revenue, and the filing says a statute built it

- **Needed or desired [x].** Government revenue +14% → +28% → +53% → +78% (H1 2026); US
  government +90% in Q2 2026; government remaining deal value $4.4bn (+90%) with a further
  $12.3bn of IDIQ ceiling *"where the funding of such contracts has not yet been determined
  or guaranteed"*. Demand is not the question.
- **No close substitute — [x] on the peer row, [ ] on the customer's own procurement rules.**
  The government-services comparators (below) earn **12.0%, 18.0% and 21.9% gross margins
  and 7.2%, 12.3% and 9.2% operating margins on flat or falling revenue**; Palantir's
  government segment earns a **66% contribution margin on +53% growth**. Nothing in the row
  looks like it. But the filing itself explains why, and the explanation is a law, not a
  product: *"We sell commercial items and services and do not contract for non-commercial
  developmental services. The U.S. government is required to procure commercial items and
  services to the maximum extent practicable in accordance with FASA … **The enforcement of
  FASA has resulted in a significant increase in our business with the U.S. federal
  government. Any change in or repeal of FASA, or a contrary interpretation of FASA by a
  court of competent jurisdiction, would adversely affect our competitive position for U.S.
  federal government contracts.**"* (FY2025 10-K, Item 1A). And the substitute the filing
  names is the customer building it: *"U.S. government agencies, including our customers,
  often award large developmental item and service contracts to build custom software
  rather than firm fixed-price contracts for commercial products."*
- **Not price-regulated [ ] — NARROWED, not failed, and [E2-59] is the reading.** *"Changes
  in procurement policy favoring more non-commercial purchases, different pricing, or
  evaluation criteria or **government contract negotiation offers based upon the customer's
  view of what our pricing should be** may affect the predictability of our margins"*;
  *"Many of our government and commercial contracts are subject to termination for
  convenience provisions. Additionally, **the U.S. federal government is prohibited from
  exercising contract options more than one year in advance.**"* This is not utility-style
  rate regulation; it is a monopsonist with statutory rights to walk away and to reopen
  price. **[E2-59]** is exactly this shape: administered conditions can *floor* a business
  — here the commercial-item preference floors Palantir against cost-plus contractors — but
  *"the moat belongs to the regime, and 'That day is gone' is how it ends."* The government
  half's moat is real, wide against the contractors, and **owned in part by Congress**.

### THE COMMERCIAL HALF — 46% of revenue, growing 103%, and the wave question

- **Needed or desired [x].** Commercial +60% (FY2025), +103% (H1 2026); US commercial +149%
  in Q2 2026; commercial RDV $6.8bn, +117%.
- **No close substitute — [x], NARROWLY, on the filed evidence, with the limit stated.** The
  data-platform comparators: Snowflake grew 29% and **lost $1,332M with SBC at 131% of
  operating cash flow**; C3.ai's revenue **fell 35.7%** and it lost $470M; ServiceNow, the
  nearest profitable platform, earns 13.7%. Palantir earned **31.6% GAAP operating margin
  in FY2025 and 47% in Q2 2026** — the highest of every company in the row, including the
  three hyperscalers' parents on a consolidated basis (Microsoft 46.8% is the one that is
  close). **[E3-46]**'s number — *"very high returns on capital employed over time"* — is
  answered: net property and equipment is $61M, capex 0.76% of revenue, and the returns are
  effectively unbounded on operating capital. The substitute question is answered by
  conduct: **customers are expanding inside accounts** (top-twenty average revenue +45%;
  revenue per customer $4.0M → $4.7M) faster than they are being added (customer count
  +24%). A customer with a close substitute does not triple its spend with the incumbent.
- **Not price-regulated [x].**

**[E2-44] — both halves.** *Half one, price:* **no filed price series exists** — no ASP, no
seat count, no per-customer price — so the test cannot be run on a price and this run does
not pretend it can. The only filed proxies are the contribution margins: commercial
**52% → 60% → 66%** while commercial revenue doubled, and government 59% → 60% → 66%. A
business being pushed on price does not widen its contribution margin 14 points in two
years; a business riding demand can. **Inconclusive on price, favourable on margin.** *Half
two, capital:* **passes as fully as any name in the queue** — $33.9M of capex on $4,475M of
revenue, and dollar volume +56% on that. **But the capital is not absent; it is somebody
else's.** The Q2 2026 10-Q: *"In March 2026, the Company amended one of its third-party cloud
services agreements. Under the amended agreement, the Company has committed to spend at
least **$5.6 billion**, with annual minimum commitments of **$268 million to $979 million**,
over ten contract years through February 29, 2036."* Palantir's (c) is low because the
hyperscalers' (c) is enormous, and the 10-K names the dependence: *"AWS, Microsoft Azure,
and other third parties have no obligation to renew their agreements with us on commercially
reasonable terms, or at all."* **For (c) this means the D&A default [E3-44] is valid — the
renewal spend is in cost of revenue, not in capex — and for the moat it means the platform
sits on a supplier that also sells a substitute.**

**[E4-04] / [E3-51] / [E4-36] — must the moat be continuously rebuilt, and which cause is
this?** The product has been re-platformed three times (Gotham, Foundry, AIP) and the
filings attribute the post-2023 acceleration to AIP and to *"demand for AI sovereignty"*.
That is a wave, and **[E3-51]** says the advantage in a surfing run *"lives in the wave, not
the surfer."* Against that: R&D excluding SBC is **$421M — 9.4% of revenue — a third of
CrowdStrike's rate**, and what the spend defends is the *same* installed ontology across
each re-platforming; a lapse in spending would narrow the structure, not destroy it (the
[E5-23] defence case, not the Rhodes Ridge replacement case). **[E4-36]**: the record comes
from **extreme performance on one variable — on-site integration by the vendor's own
engineers — combined with wave-riding since 2023**. Only the first is ownable. **The class
is NARROW because the part that is ownable is real and the part that is growing is the
wave.**

**Direction [E4-32]: widening on every filed series** — customers +34%/+24%, contribution
margin +6 points in both segments, RDV +105%, RPO +20% in six months, US share of revenue
62% → 80%.

**Key-person dependence, recorded here as a moat defect [E4-23], not at Q3 as a
strength:** the 10-K carries *"changes in our management, including any departures of one
of our Founders"* as a risk factor; the CEO's letters are the company's public voice; the
Class F structure at Q3 is built around three named men. Recorded.

**Untapped pricing power [E3-33] / [E5-28]?** Claiming that class is claiming near-monopoly.
Not claimed; no price series exists to support it, and the government half's prices are
negotiated against *"the customer's view of what our pricing should be."*

### THE COMPETITOR ROW — required **[E3-28]**

*Full working, every accession number, every verbatim quote and every recorded sweep:*
`Test Runs/_research 2026-09-11 PLTR/COMPETITOR_ROW.md`. **Peers taken: six with filed data
(three data-platform, three government-services), plus Microsoft, Amazon and Alphabet
name-swept and carried from their own completed runs. Databricks is a named limit.**

| latest FY, $M | **PLTR** FY25 | SNOW FY26 | AI FY26 | NOW FY25 | LDOS FY25 | BAH FY26 | SAIC FY26 | MSFT FY26 | GOOGL FY25 |
|---|---|---|---|---|---|---|---|---|---|
| revenue | **4,475** | 4,684 | 250 | 13,278 | 17,174 | 11,217 | 7,262 | 331,839 | — |
| revenue growth | **+56%** | +29% | **−36%** | +21% | +3% | −6% | −3% | — | — |
| gross margin | **82%** | 67% | 31% | 78% | 18% | 22%¹ | 12% | 68% | — |
| **GAAP operating margin** | **31.6%** | (30.6)% | (199)% | 13.7% | 12.3% | 9.2% | 7.2% | **46.8%** | 32.0% |
| GAAP net income | **1,625** | (1,332) | (470) | 1,748 | 1,462 | 851 | 358 | 133,749 | — |
| **SBC ÷ OCF** | **32.0%** | **131%** | n/m (OCF < 0) | 35.9% | 5.4% | 6.6% | 10.5% | 6.8% | 15.1% |
| capex ÷ revenue | **0.76%** | 2.2% | 0.8% | 6.5% | 0.7% | 0.8% | 0.4% | 34.9% | 22.7% |
| owner earnings (OCF−SBC−capex) | **1,417** | (479) | (456) | 2,621 | 1,530 | 882 | 513 | — | — |
| net cash (debt) | **+9,409**² | +2,505 | +575 | +8,564 | (3,540) | (3,212) | (2,305) | — | — |
| diluted shares, 3-yr change | **+24.3%**³ | +5.9% | +27.9% | +2.9% | −5.8% | −7.8% | −16.7% | — | — |
| filed customer count | **954** | 13,328 | none | ~8,700 | n/a | n/a | n/a | — | — |
| filed net retention | **none** | 125% | none | 98% renewal | n/a | n/a | n/a | — | — |
| US-government revenue | **54% gov, all** | not filed | not filed | 11% channel | 87% | 98% | 98% | — | — |
| **names Palantir in its 10-K?** | — | **NO** | **NO** | **NO** | **NO** | **NO** | **NO** | **NO** | **NO** |

¹ BAH files no gross-profit line; revenue less cost of revenue less billable expenses, computed and labelled. ² At 2026-06-30, cash $2,030M + marketable securities $7,379M, zero debt. ³ Palantir diluted weighted shares 2,063.8M (FY2022) → 2,565.2M (FY2025). MSFT/GOOGL figures from their own runs (`2026-09-06 Run - MSFT`, `2026-09-06 Run - GOOGL`) and the CRWD row; Amazon carries no comparable line.

**THE THREE LIMITS, NAMED [E3-28]:**
- **Databricks — private, no SEC filings.** No rung of the evidence ladder reaches it. Named
  once across the six peer 10-Ks, by C3.ai, as a data source, not a competitor. **The
  commercial moat class is held NARROW rather than anything stronger partly for this
  reason**: the most-cited private substitute cannot be measured.
- **The hyperscalers file no comparable line.** Recorded sweep of the FY2026 Microsoft, FY2025
  Amazon and FY2025 Alphabet 10-Ks: **no instance found** of a dollar figure for a data/AI
  platform product comparable to Foundry/AIP — Azure is a growth rate, AWS and Google Cloud
  are whole segments. The substitute that matters most for the commercial half cannot be
  sized from filings.
- **No filer in either set names Palantir, and Palantir names no one.** Its competition
  section reads: *"We are fundamentally competing with the internal software development
  efforts of our potential customers."* The CRWD run treated being named by every peer as
  attacker's-test evidence in the subject's favour; here the row is silent both ways, and
  silence is not evidence. **[E3-61]'s limit applies in full**: the row shows position, not
  conduct, and it cannot show whether the hyperscalers will price AIP's substitute at zero.

**What the row does say, and it is the strongest fact in the file for the moat:** on the
data-platform side **Palantir is the only one of four filers with a GAAP operating profit**,
and it is growing fastest; on the government side it earns a contribution margin **three
times the contractors' gross margin** on growth ten times theirs. That is not what a
commodity supplier's numbers look like. It is also exactly what a wave-rider's numbers look
like in the third year of the wave, and the row cannot tell the two apart.

### THE VERDICT — IN, NARROW, AND THE TWO HALVES ARE RECORDED SEPARATELY

- **Government: NARROW, regime-dependent.** Real switching costs (accredited deployments,
  cleared engineers, an ontology inside the agency), but the price and the term are the
  customer's to set, and the filing attributes the growth to FASA.
- **Commercial: NARROW, on a three-year record inside a wave**, with the private and
  hyperscaler substitutes unmeasurable from filings.
- Class: **[x] NARROW** · Direction: **widening, every filed series**.
- **VERDICT: [x] IN — NARROW.**

**Why not WIDE, why not OUT, and why not UNKNOWABLE — stated so the verdict is
falsifiable.** *Not WIDE*: criterion (3) is narrowed on 54% of revenue by the customer's
statutory rights; no price series exists; the largest substitutes are unmeasurable. *Not
OUT*: unlike CrowdStrike, there is **no filed evidence of discounting to retain customers,
no metric withdrawn, and the unit series is filed and rising**; the evidence that exists
points one way. *Not UNKNOWABLE*: the question of whether the commercial growth outlasts
the wave is a Q5 growth assumption, and **[E4-25]** says it belongs in the range, not in a
refusal to price. **What would flip it to OUT**: a filed statement of discounting or
*"customer commitment packages"* in the CRWD form; the customer count falling in a filed
year; or a FASA change. **What would flip it to WIDE**: a filed net retention number above
120% for eight quarters alongside a filed list-price increase held — documents I can name,
and which do not exist today.

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**The 8-K EX-99.1 releases were read before this gate was scored, as the queue's standing
rule requires — seven of them, Q4 2022 through Q2 2026.**

### STEP 1 — THE WEIGHT CASE, DECLARED
- [ ] **Daily execution [E3-38]** — not ticked. The product is installed software with a
  multi-year subscription; it is not *"only promises"* [E2-70]. A bad quarter of execution
  loses a renewal, not the company.
- [ ] **Control [E1-16]** — not ticked for the analyst; a marketable security with an exit.
- [ ] **Leverage [E3-29]** — not ticked. Zero debt; $9.4bn of cash and Treasuries; a $500M
  revolver undrawn to 2027-03-31.

**Case declared: OVERLAY.** Manager quality alone does not stop the run. **But the control
structure inverts the question the framework asks — not "how much damage can this manager
do before I can react" but "can the register react at all" — and that is recorded below
under candor and [E3-66], where it belongs.**

### HONESTY — binary, permanent, filings-based [E5-16]
- **Securities class action** (*Cupat v. Palantir*, D. Colo., filed 2022-09-15/10-25/11-04):
  dismissed without prejudice 2024-03-31; second amended complaint; **dismissed with
  prejudice and judgment for defendants 2025-04-04**; notice of appeal to the Tenth Circuit
  2025-05-02. The 10-K: *"the Company was not aware of any currently pending legal matters
  or claims … that were expected to have a material adverse impact."*
- **No DOJ, SEC or regulatory inquiry disclosed** in the FY2025 10-K or the Q2 2026 10-Q
  (recorded sweep for "investigation", "subpoena", "Department of Justice", "inquiry": the
  hits are generic risk-factor language only). *(For scale: the ServiceNow 10-K in the peer
  row discloses a DOJ investigation; Palantir's does not.)*
- **ICFR:** unqualified auditor opinion; no material weakness.
- **The 2021–22 "Strategic Commercial Contracts", dated to when they became public (the
  2021 10-Qs).** Palantir signed *"Investment Agreements"* to buy shares in SPACs and
  private companies which, in the same transactions, signed commercial contracts with
  Palantir — *"the total value of Strategic Commercial Contracts … $492.7 million"* at
  2022-12-31, one investee bankrupt in 2022, $166.6M of revenue recognised from them by
  then. **Revenue from customers the vendor had just funded** is the closest thing to a
  weak-accounting item in the file. It was disclosed at every step, no restatement
  followed, no new agreements since 2022, and the total value has run off to **$326M**
  (Q2 2026 10-Q) — under 4% of one year's revenue now. **Read, dated, not a disqualifier;
  carried as the one cockroach [E4-22] the kitchen has shown.**

### STEP 2 — THE FLAGS [E4-22, E5-15, E4-29]. Prompts to read, never verdicts.
- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRES AT FULL STRENGTH, IN THE 10-K
  AS WELL AS THE RELEASES.** Every EX-99.1 headlines *"Adjusted income from operations"*,
  *"Adjusted EBITDA"*, *"Adjusted free cash flow"* and a *"Rule of 40"* whose second term is
  the adjusted margin. The 10-K itself carries three non-GAAP measures — contribution
  margin, gross margin excluding SBC, adjusted income from operations — and the rationale is
  the exact sentence the corpus refuses: *"**We exclude stock-based compensation, which is a
  noncash expense**, from these non-GAAP financial measures because we believe that excluding
  this item provides meaningful supplemental information."* **[E5-06]**: *"To say
  'stock-based compensation' is not an expense is even more cavalier."* The gap between the
  two books in FY2025: GAAP operating income $1,414M; adjusted $2,254M; the difference is
  $684M of SBC plus $156M of employer payroll tax on it. In Q2 2026 the release's own
  "Rule of 40 score of 155%" is 93 points of revenue growth plus 62 points of adjusted
  margin, against a 47% GAAP margin.
- [x] **Trumpeted projections [E4-22 third flag] — FIRES, and [E3-48]'s record test is then
  run.** Guidance every quarter, raised every quarter; the Q2 2026 release is titled
  *"… Crushing Consensus Expectations."* **The record, guidance issued each February against
  the filed outturn:**

| year | revenue guidance at the start of the year | filed revenue | vs top of range |
|---|---|---|---|
| 2023 | $2,180–2,230M | $2,225.0M | inside, at the top |
| 2024 | $2,652–2,668M | $2,865.5M | **+7.4%** |
| 2025 | $3,741–3,757M | $4,475.4M | **+19.1%** |
| 2026 | $7,182–7,198M (Feb) → $8,150–8,158M (Aug) | — | raised 13% by mid-year |

  *"Nine cases out of ten"* of projections exist to justify a course **[E3-48]**; the
  remedy is the record, and **this record is three consecutive years of beating the initial
  guidance by a widening margin.** That is the candid direction — guidance set below what is
  then delivered — and it is recorded in management's favour. **[E5-30]** still applies: a
  guidance culture is a ratchet, and the test is what happens in the first year the number
  is missed.
- [x] **Serial share issuance [E5-15] — FIRES on the count, and is then read.** Diluted
  weighted shares: **979M (2020) → 1,924M (2021, the direct-listing conversion) → 2,064M →
  2,298M → 2,451M → 2,565M (2025) → 2,569M (Q2 2026).** From the first full listed year,
  **+33.5% in 4.5 years, 6.6% a year.** Options outstanding 152.2M at a $9.98 strike, $25.5bn
  in the money. The counterweight: **no equity has been sold to the market for cash since
  listing** — every share issued settled compensation. That is [E5-15]'s promotion tell
  *not* firing (no capital raised on a high price) while its dilution substance fires in
  full. Buybacks: $1.0bn authorised August 2023; **$64.2M (2024) and $75.0M (2025) spent,
  $139M total, 0.6M shares in 2025 — and the programme was terminated in January 2026.**
- [x] **Stock-price targeting [E3-50] — FIRES, and the proxy says so in its own words.** The
  pay-versus-performance section: *"**The financial performance measure used in 2025 to link
  CAP to performance is our stock price** … Guidance issued under the relevant rules states
  that we cannot use stock price as our company selected measure; therefore, we have not
  listed a company selected measure."* The tabular list of performance measures contains one
  entry: *"Stock price."* **The brief asked whether the CEO award vests on a filed number.
  It does not.** Mr Karp's August 2020 grant — **105.0M options at $11.38 and 21.45M RSUs,
  Class B** — *"vests in 40 equal quarterly installments beginning on August 20, 2021"*:
  service alone, through 2031, no operating metric. The 2025 SARs to the CFO and CRO vest on
  service and pay out only if the stock is above **$150** in a window in **2033**, capped at
  **$450**. In 2025 Mr Karp realised **$547.5M on RSU vesting** (SCT total $8.6M);
  Mr Cohen $697M on exercises and vests; and *"compensation actually paid"* to the CEO was
  **$11,094,359,597** — eleven billion dollars, all of it the mark-to-market of the 2020
  award. **[E2-01]** asks for *"a high earnings rate on equity capital employed … and not the
  achievement of consistent gains in earnings per share"*; Palantir's own scorecard contains
  neither, and contains nothing but the price.
- [ ] **Weak accounting** — the SPAC contracts above; otherwise the 10-K is GAAP-first with
  the non-GAAP reconciled at every line. **Noncash consideration** (revenue settled in
  customer equity) is a filed cash-flow line: $(37.2)M, $(52.5)M, $(46.6)M — under 1% of
  revenue, shown, not hidden.
- [ ] **Unintelligible footnotes** — no; the segment, deal-value and equity notes are
  unusually legible.
- [ ] **Filed-figure tells [E4-30]:** reported growth is **not** smooth (+47%, +41%, +24%,
  +17%, +29%, +56%, +93% quarterly); **cash taxes are 1.3% of pretax income** ($21.7M on
  $1,657M) — explained by **$8.3bn of indefinite federal NOLs** and $4.8bn of state NOLs, a
  disclosed asset, not a shifting ratio. Neither tell fires.
- [ ] **Metric-switching [E2-49]** — does not fire (Q1). **Dividends by issuance [E2-52]** —
  no dividend. **Except-for [E2-57]** — the *"otherworldly"* register runs the other way;
  no excuses were needed because nothing missed. **Restructuring [E3-53]** — none.

**[E4-52] — DO THE FLAGS CONVERGE? YES, AND THIS IS THE Q3 FINDING.** Four flags fire
toward one outcome: an adjusted book that deletes the largest expense; guidance and a
"Rule of 40" built on that book; a pay structure whose only measure is the stock price,
paying its CEO $11bn on paper in a year; and a share count rising 6.6% a year to settle
payroll. **They are not four prompts; they are one system, and the system's product is the
share price.** The corpus's name for the risk is **[E3-50]**: managers whose premise is that
*"their job at all times is to encourage the highest stock price possible"* — a premise the
corpus *"adamantly"* rejects — and its next step is named in the same passage,
*"unadmirable accounting stratagems."* None has been found. The flag binds **position
size**, as the framework says a capital-allocation flag must.

### STEP 3 — THE PRIMARY TEST [E2-01], multi-year, balance sheet first
Net income on year-end equity: **(41)% (2021, $(520)M on $2,291M), (14)% (2022), 6.0%
(2023, $210M on $3,476M), 9.2% (2024, $462M on $5,003M), 22.0% (2025, $1,625M on
$7,387M)**, and $1,942M in H1 2026 on $9,774M — **~40% annualised**. The denominator is 95%
cash and Treasuries: **on [E2-43]'s unleveraged net tangible operating assets the return is
undefined-high**, as it was for every pure-play in the CRWD row, and this run refuses to
print a spurious figure. On the third denominator **[E2-73]** — the operators judged on the
assets they were handed — the answer is the contribution margin: **66%, up from 56% in two
years.**

### THE HALF-OWNER TEST [E2-26] — split, and the split is the tell
**The 10-K passes it unusually well:** a customer count with a stable definition; the
top-twenty average revenue; RDV split by segment; contribution by segment; the SPAC
contracts' value and the bankruptcy; the $5.6bn cloud commitment with its annual minimums;
the Class F mechanics set out over five pages. **The releases fail it in the other
direction**: *"This quarter was otherworldly"*; *"Crushing Consensus Expectations"*; a
"Rule of 40" that is arithmetically 155%. **[E2-72] authorship:** Mr Karp writes his own
quarterly letters — the corpus's positive tell, recorded as such, with the register of those
letters recorded beside it.

### [E3-66] — WHERE DOES THE SHAREHOLDER STAND IN THE QUEUE? A THREE-CLASS FILER MUST SAY.
Permanently behind three named men, by construction. The Class F stock gives the Founders
*"the ability to control up to 49.999999% of the total voting power … so long as the
Founders and certain of their affiliates collectively meet a minimum ownership threshold,
which was 100.0 million of the Company's equity securities"* — **4.2% of the count**. The
10-K states the consequence three ways: *"future issuances … will dilute the economic
interests of our Founders but **will generally not result in further dilution of the voting
power** of such Founders"*; *"our Founders … will be able to achieve substantial liquidity
in their holdings, and substantially diminish their economic interest in us, **without
diminishing their voting power**"*; *"Upon the withdrawal or removal of any of our Founders
… the voting power of our outstanding capital stock will be further concentrated among the
remaining Founders, which may be as few as one."* Excluding Class F, the Founders held
**~22% of the voting power at 2026-02-10**. **[E2-26]**'s test — would I want to know this
if positions were reversed — is passed by the disclosure and failed by the fact. The
Shopify run recorded a 40–49.9% founder share immune to dilution; this is the same
structure with a lower ownership floor and a smaller economic stake behind it.

### THE INSTITUTIONAL IMPERATIVE — all four [E2-30]
- [ ] resists change in direction — no; the company re-platformed three times.
- [ ] projects/acquisitions to soak up funds — **no**: $9.4bn of cash sits in Treasuries;
  no acquisitions since 2022; $73M of private securities bought in 2025.
- [ ] staff studies for the leader's craving — nothing filed.
- [ ] peer behaviour imitated — the buyback was **terminated** while every peer in the
  queue was buying; the opposite of imitation.

### CAPITAL ALLOCATION — the buyback conditions [E5-08], and the refusal read correctly
- (1) ample funds: **yes**, beyond argument.
- (2) material discount to conservatively calculated IV: **no** — and management stopped.
  $139M was bought over 2024–25 at prices far below today's; the programme was terminated
  in January 2026 with the stock near $178. **[E5-24]**: *"what is smart at one price is dumb
  at another."* At a 0.35% owner-earnings yield a buyback would be dumb, and **[E2-51]**'s
  refusal-tell is inverted here: the refusal is the rational act. Recorded in
  management's favour, with **[E4-13]**'s humility clause the other way round — they know
  the business better, and they are not buying.
- **The one allocation error on the record is the 2021–22 SPAC programme**: $272M of
  unrealised and realised losses on marketable securities in FY2022 alone, on investments
  made to win contracts. Disclosed, ended, and small against today's cash.

### THE GUARDRAIL
- [x] Nothing here promotes the name. A strong operator cannot repair Q2 or substitute for
  Q4 **[E2-37, E2-38, E3-39]**.
- [x] Key-person dependence recorded at **Q2** as a moat defect **[E4-23]**.
- [x] The manager is not the plan; the franchise question was decided at Q2 on the filings.

- **VERDICT: [x] IN — no disqualifier found.** *Not a finding that the managers are honest
  **[E5-17]**. Four flags fire and converge **[E4-52]**; the convergence binds position size.
  The honesty binary shows a dismissed class action and one disclosed, ended episode of
  vendor-financed revenue. IN never promotes.*

---
## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**

**The windows, both (c) ends, are at the screen-row section above. The years that describe
the business that exists now [E4-41] are 2023 onward.**
- **Short-window mean** (2024–25): **$933.1M** at (c) = capex; $927.6M at (c) = D&A
- **Long-window mean** (2023–25): **$695.8M** at capex; $686.0M at D&A
- **Single year FY2025:** $1,416.6M · **TTM to 2026-06-30:** $2,522.7M
- **Spread, conservative end:** 3y/2y = 25% below; 5y (2021–25) = $250M, 73% below; 6y and
  longer are **negative**.
- **Combined range** (window spread × capex band): **$696M to $2,523M on the current
  business; minus $133M to plus $2,523M on the filed history.** The capex band itself is
  **$8M wide** — capex $33.9M against D&A $26.1M — because the capital is the
  hyperscalers'. **This is the corpus-default case for (c) [E3-44, E2-41]**: not
  capital-intensive, D&A a fair proxy, and the *renewal* spend (cloud hosting, $5.6bn
  committed over ten years) already inside operating cash flow as cost of revenue.
- **Is the range too wide to conclude [E4-25]?** It is 3.6x wide on the current business and
  crosses zero on the filed history. **It is not too wide for THIS question**, because the
  price fails against the top of it by the same order as against the bottom — the width is
  a Q5 fact and Q5 uses all four constructions.
- **The distorted years, named [E5-11]:** 2020 (direct-listing SBC of $1,270.7M); 2021–22
  (SBC above operating cash flow; SPAC-funded revenue). Not in the window used.
- **Interest income is inside OCF** — $229.2M (FY2025), $266.4M (TTM) — earned on the cash
  that Q5 credits separately. **Ex-interest: FY2025 $1,187.4M; TTM $2,256.3M.** Both are
  carried so the cash is not counted twice.
- **Working capital:** receivables rose $450.4M in FY2025 and $433.8M in H1 2026 (DSO ~82 →
  ~88 days); contract liabilities rose $238.7M and $256.5M. OCF nets both from one audited
  line [E2-23], constraint 3.
- **Stock compensation subtracted in full [E5-06] — and [E3-70] says the charge is the
  FLOOR.** Charged: $684.0M (FY2025), $835.5M (TTM). Granted in 2025 at grant-date fair
  value: 5.75M RSUs at $136.28 + 0.82M P-RSUs at $106.56 + 5.17M SARs at $22.43 ≈
  **$987M** — the *"like quantity and structure"* measure, ~$300M above the charge because
  the charge still amortises 2020 grants struck near $11. **The aggregate intrinsic value of
  options exercised in 2025 was $3.0bn and in 2024 $3.8bn** — value that left the register
  in those years for service rendered mostly before listing. Judged: **subtract $987M for
  FY2025, so OE at the market measure is ~$1,114M** (ex-interest ~$884M); the TTM equivalent
  is ~$2.2bn. **Disclosed judgment, and every construction is carried to Q5.**
- **Owner earnings by year:** see the screen-row table.

### Great, good, or gruesome? **[E4-20]**
- [x] **great** — *"an extraordinarily high interest rate that will rise as the years pass"*
  on capital that is almost nil: capex 0.76% of revenue, contribution margin 66% and rising,
  revenue +56% on $21M of incremental capex. **The savings account is the customers' and
  the hyperscalers'.** Evidence: FY2025 OCF $2,134M on $61M of net PP&E.

### Staying power — all three **[E5-11]**
- (1) large and reliable stream of earnings: **large — $2.1bn OCF, $3.4bn TTM.**
  *Reliable — qualified:* 54% government, *"many of our government and commercial contracts
  are subject to termination for convenience"*, options exercisable one year ahead, and
  RPO of $4.9bn covers **nine months of revenue** at the current run rate. Reliable on a
  one-year view; not contractually reliable beyond it.
- (2) massive liquid assets: **$9,409M of cash and US Treasuries, no debt.** Yes.
- (3) **no significant near-term cash requirements: YES, with one commitment named.** Zero
  debt; operating leases $211M noncurrent; the **$5.6bn cloud commitment, $268M–$979M a year
  through February 2036** — the largest year is 29% of TTM operating cash flow, and the
  commitment is the cost of serving the customers who produce that cash. The $500M revolver
  is undrawn and is not counted **[E5-39]**.
- **Leverage, named and quantified [E4-16, E3-29]: none.** Total liabilities $1,794M against
  $11,679M of assets; the liabilities are deferred revenue, customer deposits and leases —
  customer-prepaid, covenant-free **[E3-52]**.

### Name the specific way THIS business dies **[E2-27, E3-24]** — exposure, not experience **[E4-40]**
- **Mechanism 1 — the regime changes.** The filing says the government business was built
  by a statute's enforcement and would be *"adversely affect[ed]"* by its repeal or by a
  court reading it differently; that agencies *"often award large developmental item and
  service contracts to build custom software rather than firm fixed-price contracts for
  commercial products"*; that the current administration *"has launched efforts to evaluate
  and reduce overall government spending."* **Quantified:** government revenue $2,402M
  (FY2025), $1,848M in H1 2026; Customer I is 27% of receivables. A halving of US government
  revenue over three years removes roughly **$1.5–2bn of revenue and, at a 66% contribution
  margin, ~$1.0–1.3bn of contribution** — against $9.4bn of cash and no debt. **The business
  survives it; the price does not. Likelihood: a real possibility over a decade, not likely
  in any given year.**
- **Mechanism 2 — the wave ends.** The hyperscalers, on whose capital Palantir runs, sell
  their own AI tooling; Databricks is private and unmeasurable; the commercial acceleration
  is three years old and attributed by the filer to AIP and *"AI sovereignty."* If US
  commercial growth goes from 149% to zero, the business is a ~$6bn-revenue, ~$2.5bn-OE
  software company with $9bn of cash. **It does not die; the $402bn valuation does.** At
  the bare sovereign that business is worth roughly $57bn — **$24 a share against $167.**
  **Likelihood: a real possibility; the timing unknowable.**
- **What cannot kill it:** leverage (none), liquidity (none needed), a single customer (none
  above 10% of revenue).
- **Likelihood, in the corpus vocabulary:** [ ] likely [x] a real possibility [ ] a
  low-level possibility.
- **VERDICT: [x] IN.**

---
⛔ **Q1 IN · Q2 IN (NARROW) · Q3 IN · Q4 IN. Q5 opens legitimately. The arithmetic below is
therefore a clearance-eligible valuation, not a computation under a closed gate; the
COMPUTATION heading the brief asked for is used anyway for the growth-required block,
because that block is an engine and casts no vote [E3-34].**

---
## COMPUTATION — NOT A CLEARANCE: THE GROWTH THE BUYER NEEDS, AND FOR HOW LONG
*The brief asked for this before Q5 under this heading. Q1–Q4 are IN, so Q5 below is a
legitimate valuation; this block is the engine only and casts no vote [E3-34].*

**Inputs:** price $167.23 (2026-09-11, aggregator, flagged) × 2,403,058,480 = **$401,863M**;
cash and Treasuries $9,409M at face, no debt → **enterprise value $392,454M**; sovereign
5.35% bare; the floor 10% **[E4-28]**; a ten-year growth phase then 3% in perpetuity.

**1. The growth required for TEN years to justify today's EV at the 10% floor:**

| starting owner earnings | required growth, ten years, then 3% |
|---|---|
| $247M — the screen's 5-year mean | **72.7% a year** |
| $696M — 3-year mean, the corpus default window | **55.2% a year** |
| $1,187M — FY2025 ex-interest | **46.8% a year** |
| $1,417M — FY2025 | **44.1% a year** |
| $2,256M — TTM ex-interest | **37.1% a year** |
| $2,523M — TTM, cash not credited, against the full cap | **35.8% a year** |

**2. The expectancy at $167.23 for a given growth rate, ten, fifteen and twenty years:**

| owner-earnings growth | 10 years, from $1,187M | 10 years, from $2,523M | 15 years, from $2,523M | 20 years, from $2,523M |
|---|---|---|---|---|
| 10% a year | 3.6% | 4.2% | 4.6% | 5.1% |
| **15% — [E4-35]'s fewer-than-1-in-20 event** | 3.9% | 4.9% | 5.9% | 7.0% |
| 20% | 4.4% | 5.7% | 7.6% | 9.6% |
| 25% | 5.0% | 6.8% | 9.8% | 12.7% |
| **30%** | 5.8% | **8.2%** | **12.4%** | 16.1% |
| 40% | 8.0% | **11.7%** | 18.4% | 23.6% |

**The sentence the operator asked every run to end with: at $167.23 the buyer needs owner
earnings to compound at roughly 40% a year for ten years, or 30% a year for fifteen years,
from the best twelve months the company has ever filed, to earn the ~10% the corpus quits
on — and 15% for twenty years, the rate [E4-35] says fewer than one in twenty of the best
businesses on earth achieve, returns 7.0%.**

**3. The same assumption as a business rather than a rate [E4-44, E2-63].** A 10% return on
$392bn requires **$39.2bn of steady-state owner earnings**. At FY2025's 31.7% OE margin that
is **$124bn of revenue — 27.7x FY2025, 15.2x the FY2026 guidance**; at the TTM 41.0% margin,
**$96bn — 11.7x the FY2026 guidance**; at a 50% margin no software company of size has
sustained, **$78bn — 9.6x**. The 2026 guidance itself, $8.15bn, is the fastest year in the
company's history at +82%; the price needs that to be repeated, on a compounding base, for
most of a decade.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### 1. THE YIELD, at every construction, beside the bond

| construction | owner earnings | yield on $401,863M | vs 5.35% sovereign |
|---|---|---|---|
| 5-year mean, D&A end (the screen's bottom) | $247M | **0.06%** | −5.29 pts |
| 3-year mean, capex end | $696M | 0.17% | −5.18 pts |
| FY2025, market-measure SBC [E3-70], ex-interest | $884M | 0.22% | −5.13 pts |
| FY2025 ex-interest — **the bottom boundary of the current business [E5-34]** | **$1,187M** | **0.30%** | **−5.05 pts** |
| FY2025 | $1,417M | 0.35% | −5.00 pts |
| TTM ex-interest | $2,256M | 0.56% | −4.79 pts |
| **TTM to 2026-06-30 — the most generous figure in the file** | **$2,523M** | **0.63%** | **−4.72 pts** |

*(On the $432,754M cap that counts the 152M in-the-money options and 42M RSUs, every yield
is 7% lower again: 0.58% at the top.)* **There is no construction of Palantir's owner
earnings — on any window, either (c) end, with or without interest income, at the charged or
the market measure of SBC — that reaches one per cent, let alone the 5.35% bond.** The
screen's 0.06% was on the right cap and the wrong window; the right window is ten times
better and still fails by 4.7 points.

### 2. WHAT THE PRICE ALREADY ASSUMES
- year-1 growth needed to justify the quote: **36–47% a year for ten years** (table above),
  or **9.4% perpetual** on the TTM figure.
- what the business has actually done: revenue **+29% (2024), +56% (2025), +93% (Q2 2026)**;
  owner earnings from $221M to $2,523M TTM in three and a half years. **The business is
  currently growing faster than the price requires. The price requires it to keep doing so
  for a decade, compounding, in a wave whose durability no filing can evidence, and
  [E4-35]'s base rate says that among the 200 most profitable companies fewer than one in
  twenty sustain even 15% for twenty years.**

### 3. WHAT YOU ARE PAID
- **−4.72 to −5.29 points against the sovereign at today's price; an honest pre-tax expectancy
  of roughly 4–8% on any growth assumption inside [E4-35]'s base rate, and 11.7% only at 40%
  a year for a decade.**

**WHERE CERTAINTY IS PRICED — not in the rate [E3-42].** Sovereign used **5.35%, bare, no
per-name premium.** Certainty was handled at Q1 (the business is understood) and would be
handled once at the end margin; no margin is computed because the price exceeds the whole
range.

### THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]
*Owner earnings capitalised at the bare sovereign, no risk premium, plus $9,409M of cash and
Treasuries at face:*

| | conservative ($1,187M) | middle ($1,417M) | generous ($2,523M TTM) |
|---|---|---|---|
| **at the sovereign, 5.35%** | $31.6bn · **$13/sh** | $35.9bn · **$15/sh** | $56.6bn · **$24/sh** |
| **at the [E4-28] 10% floor** | $21.3bn · **$9/sh** | $23.6bn · **$10/sh** | $34.6bn · **$14/sh** |
| **current price** | | | **$167.23** |

**In round numbers: roughly $13 to $24 a share against the bare bond on zero growth; $9 to
$14 at the floor. The price is 7 to 13 times that.** *(Zero-growth capitalisations of a
business growing 56–93% are stated for the record, not as the case; the growth-adjusted
expectancy table above is the case, and it reaches the same verdict.)*

### THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21]
- **Honest pre-tax expectancy at this price: ~4% to ~8%** on every growth assumption inside
  the corpus's base rate; the floor is cleared only at 40% a year for ten years or 30% for
  fifteen. **Against ~10%: BELOW THE FLOOR. The name is not ranked — it is QUIT ON**, and the
  ranking lines are not filled in.
- points over sovereign: **−4.72 to −5.29** — *recorded, not a ranking input.*

### [E2-63] — WHAT BOUNDS THE UPSIDE
Three things. **The statute**: 54% of revenue is sold under a procurement preference the
filer says built the business. **The supplier**: the platform runs on AWS and Azure under a
$5.6bn commitment, and both sell substitutes. **The arithmetic of size**: $78–124bn of
revenue is what the price needs at steady state, against $8.15bn guided for 2026 — the
value *"cannot over the long term grow faster than its earnings do"* **[E4-44]**, and the
earnings would have to grow ten to fifteen-fold after the fastest year in the company's
history.

### WHICH BAR? [E4-01]'s screamer test, third outcome
- [ ] Normal method [E4-11] — not used; no margin is computed on a value the price already
  exceeds 7x at the generous end.
- [x] **Screamer test [E4-01]** — **the price is above the whole range.** It does not
  scream **[E3-25]**.
- **WINDAGE COUNT: ONE** — at [E5-34]'s bottom boundary. Everywhere else the inputs are
  realistic or generous: the bare sovereign; all cash at face; the TTM — the best twelve
  months ever filed — carried as the top; the charged SBC used as the floor measure and the
  market measure shown beside it; the growth table run out to twenty years. **Conservatism
  is not stacked [E4-48].**

- **VERDICT: NOT IN — QUIT ON at the [E4-28] floor** · **ranking position: NOT RANKED.**
  *Not UNRESEARCHED — every document is read. Not UNKNOWABLE — a 0.3–0.6% yield against a
  5.35% bond is a fact about today. Not OUT — OUT is permanent and about the business, and
  the business cleared Q1–Q4. This is the SHOP outcome: a name that fails only at Q5 fails
  on the price, and a price alert is the right instrument.*

**PASS/FAIL: FAIL, ON PRICE. Q1 IN · Q2 IN (NARROW) · Q3 IN · Q4 IN · Q5 NOT IN (quit on)
· Q6 filled as a watch. The twenty-sixth gate-clearer in the queue, and the dearest: at
0.30–0.63% it is below Shopify's 0.35–1.00%.**

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

*No position exists and none is opened; filled as a WATCH specification **[E1-02]**.*

**Pre-committed before any entry [E1-02]:**
- **Thesis-confirming metric (that the moat outlasts the wave):** the filed customer count
  growing above 20% a year **while** revenue per customer also grows, for three more filed
  years; commercial contribution margin held at or above 60%; the FASA commercial-item
  preference intact.
- **Thesis-breaking metric and threshold (the business, not the price):** (a) US commercial
  revenue growth below 20% in a filed year; (b) the customer count falling in a filed year;
  (c) a filed statement of discounting or retention packages in the CRWD form; (d) any
  change to FASA or a filed statement that a major agency has moved to developmental
  contracting; (e) SBC/OCF back above 50%; (f) any amendment of the Founder Voting Agreement
  in the direction the 10-K warns of — *"increasing the ability of one or more of our
  Founders to exercise control."* Any of (a)–(d) closes the file at Q2 and voids the bands.
- **Next catalyst date:** Q3 2026 8-K EX-99.1 (early November 2026); FY2026 10-K (February
  2027); the 2027 DEF 14A for any new CEO award and its vesting metric.

**The sell rule [E2-28]** — not applicable; no holding. For the record: the market already
judges the business more valuable than the facts indicate, which is trigger 1 by a factor
of seven.

**The real trigger is a moat downgrade and it is slow [E4-17, E3-30].** The monitoring
question is whether a deceleration, when it comes, is the wave receding or the ontology
being displaced — the customer count and the contribution margin, read together, are the
two series that separate them.

**Position size — a judgment, stated:** none at this price. If the price ever entered the
band, the [E4-52] convergence at Q3 (adjusted book, price-linked pay, founder control) sizes
the position **down**, per the framework.

### THE WATCH SPECIFICATION — this name failed on PRICE, so a price band is the right instrument
- **Floor band, $24 a share**: the zero-growth value at the bare sovereign on the TTM owner
  earnings ($2,523M ÷ 5.35% + $9.4bn cash). At $24 the zero-growth yield is 5.2% and a buyer
  underwriting 15% growth for a decade earns ~14.7%.
- **Re-read band, $40 a share**: where a buyer underwriting **15% owner-earnings growth for
  ten years** from the TTM figure reaches the 10% floor (10.2%). **Re-read, do not buy on
  the ping**: re-test the customer count, the commercial contribution margin, SBC/OCF and the
  FASA risk factor first.
- Both bands are voided by any of the business falsifiers (a)–(d) above.

- **VERDICT: [x] IN as a watch specification; no position.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped
- [x] No question marked IN carries an "unverified" or "provisional" caveat — Q2 is IN
      NARROW with its limits (Databricks, hyperscaler lines) stated as limits of the class,
      not as caveats on the verdict
- [x] Every UNRESEARCHED verdict names the artifact — none returned
- [x] Every UNKNOWABLE verdict states what cannot be known — none returned
- [x] Step 0: the filing was read, with accession numbers; four figures cross-checked
- [x] Owner earnings on multi-year means; windows stated; capex band disclosed as a
      judgment ($8M wide; D&A default valid [E3-44])
- [x] Competitor row filled: six peers with filings, three limits named
- [x] Sovereign for the earnings currency, from the issuing authority, dated 2026-09-11
- [x] Value stated as a round-number range
- [x] One bar chosen (screamer, third outcome); windage count one
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] Run committed to git after each gate

## REGISTER
- Verdict: [ ] IN [ ] OUT [ ] UNRESEARCHED [ ] UNKNOWABLE — **Q1–Q4 IN; Q5 NOT IN, QUIT ON
  AT THE FLOOR, ON PRICE.**
- One line: **A genuinely great business on the capital test, with a narrow moat whose
  government half is owned partly by a statute and whose commercial half is three years old
  and riding a wave, priced at 0.3–0.6% against a 5.35% bond; the buyer at $167.23 needs
  ~40% a year for a decade to reach the floor. Watch at $40, floor at $24.**
- **The strongest single fact against this conclusion:** the FY2026 revenue guidance of
  $8.15bn is **+82%**, US commercial is growing **149%**, and owner earnings went from $221M
  to $2.5bn in three and a half years — the business is at present growing faster than the
  40% the price requires, and if it did so for ten years the buyer would be right. The
  answer is [E4-35]'s base rate and the arithmetic of size ($78–124bn of revenue), not a
  claim that the growth stops next year.
- **Refuted priors, from the brief:** (1) *"whether a unit series exists — six runs found
  none"* — Palantir files one every quarter, never withdrawn; (2) *"[E2-49] withdrawal"* —
  does not fire; (3) *"the cap in the row may itself be wrong"* on the share classes — the
  three classes are economically equivalent by the charter and the sum is the count; (4) the
  SBC prior — 32.0% in FY2025 and 24.6% TTM, **below CRWD (68.0%), PINS (68.6%), QLYS
  (24.9% is a near match) and near CRM (23.4%)** — SBC did not decide this file; (5) *"the
  CEO's award structure"* — it vests on service, valued by stock price; the vesting metric
  is not a filed number; (6) *"Government IN NARROW and Commercial contestable"* —
  the halves came out the other way round on the peer row: government looks *wider*
  against its comparators and is the half the filer attributes to a statute; commercial is
  narrow on its own evidence.
- **Defects in the brief or tooling:** (a) the screen's `growth_required` is a perpetual
  Gordon rate and is meaningless for a filer growing 56% — the fading-rate form should be
  the published figure for any name with a `level_shift n/a`; (b) the row's `spread` again
  mixes two windows with two capex ends (the eighth consecutive run to record this); (c) the
  brief's sovereign (5.37%, 2026-09-10) was a day stale by the time the run struck it
  (5.35%, 2026-09-11) — immaterial, but the brief should not carry a number the run is told
  to re-strike; (d) `cover_shares.py` correctly refused to sum, and the screen's cap had
  summed anyway and happened to be right — the tool and the screen disagree by design and
  the screen's behaviour on multi-class filers is unlabelled; (e) the brief said Palantir
  "guides on Rule of 40" — true, but the more serious [E4-29] finding is that the 10-K
  itself carries the *"noncash expense"* rationale for excluding SBC, which the brief's
  framing (releases vs 10-K) would have led a run to score as release-only.
