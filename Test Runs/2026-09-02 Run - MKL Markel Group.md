# Company Run — MARKEL GROUP INC. (MKL) — 2026-09-02
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**SECTOR METHOD UNDER TEST — AND THIS IS ITS FIRST ACTUAL APPLICATION.**
`Framework/SECTOR METHOD - owner earnings for insurers and float-bearing holding companies.md`
(written 2026-09-02) prescribes the read order **WTM → MKL → L → BRK-B**. `Test Runs/2026-09-02
Run - WTM White Mountains.md` exists **but is an unfilled template skeleton** — every field is
still `____`. **So MKL is the first filer the method has ever touched, not the second.**
The method therefore arrives here with **zero** prior contact with a non-Berkshire registrant.

**The run has two jobs and the second outranks the first:** (1) run MKL through the six
questions; (2) **report every place the method does not fit.** Method findings are logged
inline as **[METHOD FINDING n]** and collected in `## JOB 2` at the foot of this file.

**Operator rule 9 is live on this run.** The brief states: *"Markel was chosen as the closest
structural analogue to the two-component method in the entire queue"* and *"the method should
fit Markel almost too well, and that is the danger."* The brief is correct that this is the
danger and **wrong about the structure it expects to find** — see [METHOD FINDING 1] and
[BRIEF DEFECT 1] below. Thirteen consecutive watchlist names have closed at Q2; the brief
states plainly that clearing Q2 would be more valuable than another OUT. That statement is
itself an incentive **[E4-27]**, and it is recorded here so the reader can weigh it.

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
- rate **5.27%** · date **2026-09-01** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year**, via `python tools/sources.py`. FRED DGS30 not used; it is the
  labelled fallback only.
- FX: none. Markel Group is a US registrant reporting in USD. International division writes
  in 15 countries and the 2025 income statement carries **net foreign exchange losses of
  $256,234k** — material, and recorded at Q3/Q4, but the reporting and earnings currency is USD
  and the USD sovereign is the correct yardstick.

**STAGE 0(a) — SHARE CLASS BY HAND OFF THE COVER** *(sector method, Stage 0)*
- 10-Q cover, verbatim: *"Number of shares of the registrant's common stock outstanding at
  **July 22, 2026: 12,389,958**"*
- **ONE class only.** Cover exhibit table lists a single registered security: *"Common Stock,
  no par value | MKL | New York Stock Exchange"*. Note 8(a) of the 10-Q: *"The Company has
  50,000,000 shares of no par value common stock authorized."* **No A/B structure. The BRK-A/B
  artifact class does not apply to MKL.**
- **Price $1,827.44**, 2026-09-02, Yahoo Finance — **aggregator, live quote only, flagged**
  per operator rule 5.
- **Market capitalisation = 12,389,958 × $1,827.44 = $22,642M.**

**STAGE 0(b) — insurer, float-bearing holding company, or neither?**
**Float-bearing holding company, and the filer says so in its own first paragraph:** *"Markel
Group is a holding company that owns independently operated businesses across a range of
industries. The cornerstone business, Markel Insurance, provides specialized insurance
products… It generates and holds capital used to support growth and investment across Markel
Group."* (10-K FY2025, Item 1.) The sector method is the correct method. It is **not** a
BAM/BN-class perimeter problem.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **document · date · accession no.: Form 10-K for FY2025, filed 2026-02-26, accession
  0001096343-26-000020** (`mkl-20251231.htm`). Also read: 10-Q Q2 2026 (filed 2026-07-29,
  acc. 0001096343-26-000064); 10-K FY2024 (0001096343-25-000027); 10-K FY2023
  (0001096343-24-000025); 10-K FY2022 (0001096343-23-000033); 10-K FY2021
  (0001096343-22-000039); 10-K FY2020 (0001096343-21-000032).
- **figure cross-checked against the filed statement:** consolidated **adjusted operating
  income $2,303,778k for 2025** appears at three independent places in the FY2025 10-K and
  reconciles at each: (i) Item 7 "Key Financial Metrics" summary ($2,304M rounded); (ii) Item 7
  reconciliation from operating income $3,194,852k + amortization $185,007k − net investment
  gains $1,076,081k = $2,303,778k; (iii) note 2 segment table, as the sum of the four segments
  plus corporate: 1,379,067 + 343,183 + 326,572 + 174,636 + 80,320 = **2,303,778**. Verified by
  hand. Second cross-check: **shareholders' equity $18,598M** (Item 7 key metrics) against
  segment capital reconciliation total equity **$18,596M** — a **$2M difference which is
  noncontrolling interests presentation**, and the segment table's $18,596M is *total* equity
  while $18,598M is shareholders' equity; the reconciliation is disclosed, not a discrepancy.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.**
Markel does three things that make money and one that spends it.

1. **It sells promises to pay for unusual accidents.** Someone with a risk no ordinary
   insurer will price — a fine-art collection, an amateur sports league, a classic car, a
   directors-and-officers policy for a private company, a wind farm — pays a premium today.
   Markel promises to pay a claim that may not arrive for a decade. It earns money here in
   exactly one way: **the premium it collected must exceed the claims and the cost of
   collecting the premium.** That difference is underwriting profit and in 2025 it was
   **$455,671k on $8,401,323k of earned premium** — 5.4 cents on the premium dollar.
2. **It holds the money in between and invests it.** Because claims are paid years after
   premiums arrive, Markel permanently sits on other people's money. It calls this
   **insurance float** and puts it at **$18,827M at 2025 year end**. That money buys bonds
   and stocks. In 2025 those investments threw off **$970,427k of net investment income** and
   an additional **$1,076,081k of mark-to-market gains** that run through the income statement
   under ASU 2016-01. The float is the reason the investment portfolio is roughly **1.65x
   larger than the shareholders' equity that funds it** ($37,439M invested assets against
   $18,598M of shareholders' equity).
3. **It owns 20-odd unrelated private companies outright.** Bakery ovens, precast concrete,
   ornamental houseplants, leather handbags, dredges, manufactured-housing communities,
   concierge primary care, teacher-exchange sponsorship. In 2025 these produced
   **$844,391k of adjusted operating income** across the Industrial ($343,183k), Financial
   ($326,572k) and Consumer and Other ($174,636k) segments on **$6,048,125k of operating
   revenue**. This is the second component, and **it is not small** — 36.7% of the group's
   $2,303,778k of adjusted operating income.
4. **It spends money buying more of (3) and buying back its own shares.** Share count fell
   from **13,783k (2020) to 12,590k (2025)**, and to **12,389,958 by 2026-07-22** — a 10.1%
   reduction over five and a half years.

**The scarce input this business controls.**
**Underwriting authority over risks that have no filed rate.** In the admitted market a
regulator approves the rate and the form, so every carrier sells the same contract at an
approved price and competes on price alone. In the **excess and surplus (E&S)** market it does
not: the 10-K states *"E&S eligibility allows us to underwrite unique loss exposures with
**more flexible policy forms and premium rates**."* The scarce thing is not capital — capital
is abundant and Bermuda proves it — it is **the accumulated loss data and the underwriters who
can price a risk that has never been priced**, held inside **"over 100 individually managed
products, each with its own distinct competitive environment."** The filer names the same
input: *"This expertise is our principal means of competing."*

**A second scarce input, and it is the one that actually distinguishes Markel from a pure
insurer: permanent capital with no redemption right.** Markel Ventures buys private companies
and never sells them. The 10-K's pitch to sellers is explicit: *"Markel Group supports each
business by empowering leaders to make the best long-term decisions… **We believe this approach
is difficult to replicate** and makes Markel Group a distinctive home for businesses."* Against
a private-equity buyer with a seven-year fund life, permanence is a real and non-replicable
term of trade. Whether it is a *moat* is Q2's problem, not Q1's.

**Will the fundamentals look broadly the same in ten years?**
**Yes, and this is the strongest thing about the name.** Specialty insurance has existed in
recognisable form since Lloyd's; E&S has been a distinct US regulatory channel for over a
century; the products are general liability, professional liability, marine, property, surety.
Manufactured housing communities and bakery ovens will exist. The *composition* changes —
Global Reinsurance went into run-off in August 2025, D&O was withdrawn from two platforms in
2024–25, classic car converts to fronting on 2026-01-01 — but the **mechanism** (collect
premium, hold float, invest it, own operating businesses) is the same mechanism Markel has run
since 1930 and is running today. **[E3-31]**'s test is *"relatively simple and stable in
character"*, and the mechanism is; the *outcome* is volatile, which **[E3-55]** and **[E5-29]**
expressly separate from risk: *"we would prefer that it have high volatility than low
volatility"* where the business result is confident.

**Where the understanding runs out, stated honestly.** I can understand the mechanism. I
**cannot** independently verify the loss reserve, which is the single largest number on the
balance sheet and is an estimate made by the company about events that have not finished
happening. That is not a Q1 failure — **[E3-27]**'s *"there are no answers in the financial
statements"* concedes exactly this, and the corpus's own remedy is **[E2-67]**'s reserve
development table, which is executed at Q4, not here. But it is recorded now: **a material
part of this business's reported earnings is a judgment made by the people whose pay depends
on it**, and Q3 carries that weight.

- **VERDICT: [x] IN**

*Q1 IN. The mechanism is describable without management's language, the scarce input is
nameable, and the ten-year shape is stable. The reserve-estimate exposure is carried forward
to Q3 and Q4 rather than closing the file here.*

---
## STAGE 0(b) MATERIALITY — float ÷ investments, per the METHOD AMENDMENT of 2026-09-02

The sibling WTM run added a mandatory test: **compute float ÷ investments and state it before
weighting the cost of float.** WTM came in at 22.0% against Berkshire's 41.8% and the run
concluded that step 2 was *"a rounding item beside the portfolio, not the engine."*

| | float | investments | float ÷ inv | investments ÷ equity |
|---|---|---|---|---|
| Berkshire **[E5-46]**, 2018 | $66bn | $158bn | **41.8%** | 158 / 349 = **0.45x** |
| White Mountains, FY2025 | $1,831.1M | $8,323.9M | **22.0%** | — |
| **Markel, FY2025** | **$18,827M** | **$37,439M** | **50.3%** | 37,439 / 18,598 = **2.01x** |

**Markel's float ratio is the highest of the three and it exceeds Berkshire's.** Step 2 is
therefore **not** a minor term here — it is the engine, and this is the first name in the Mini
Berk track where the amendment's warning runs the *other* way.

**CONVENTION 4 gets its first validation, and it passes.** Markel is the first filer where a
**published** float figure and the **constructed** recipe both exist:
- filer-published: **$18,827M**
- CONVENTION 4 (loss reserves $30,857,453 + unearned premiums $7,253,079 − reinsurance
  recoverables $14,616,279 − receivables $3,964,598 − DAC $909,516) = **$18,620M**
- **difference −1.1%.** The recipe reproduces a published float to within about one percent.
  *(The residual is the two components Markel's own footnote adds and CONVENTION 4 omits:
  payables to insurance and reinsurance companies +$1,667,871 and life and annuity benefits,
  less prepaid reinsurance premiums −$3,073,999.)* **[METHOD FINDING 2]**

**[METHOD FINDING 3] — and it is the serious one. The amendment tests the wrong ratio.**
Stage 0(b) asks float ÷ investments. The number that actually decides whether **[E5-46]** is
safe to apply is **investments ÷ shareholders' equity**. Berkshire's was **0.45x** — its
investments were *smaller than its own equity*, so counting them at market and adding
capitalised operating earnings could not double-count. **Markel's is 2.01x.** Half of Markel's
portfolio is other people's money. Applying [E5-46] literally to Markel therefore makes a
claim Berkshire's own arithmetic never had to make: **that $18.8bn of policyholder liabilities
should be valued at zero.** The method document is silent on this and its silence is safe only
for filers whose investments are smaller than their equity. Worked below at Q5.

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

- **Needed or desired [x]** — insurance is compelled by statute, by lenders, by landlords and
  by counterparties. Not in question.
- **No close substitute [ ]** — **this is where the file closes. Worked below.**
- **Not price-regulated [x]** — and this one passes *cleanly*, which is rare. The 10-K:
  *"The E&S, or non-admitted, market focuses on hard-to-place risks… **E&S eligibility allows
  us to underwrite unique loss exposures with more flexible policy forms and premium rates.**
  … The admitted market is subject to more state regulation than the E&S market, particularly
  with regard to **rate and form filing requirements**."*

### FIRST, THE E&S COUNTER-ARGUMENT TO [E2-70], BUILT PROPERLY

The brief is right that this deserves a real construction rather than a dismissal. **[E2-70]**,
1977: *"Insurance companies offer standardized policies which can be copied by anyone. Their
only products are promises. **It is not difficult to be licensed, and rates are an open book.**
There are no important advantages from trademarks, patents, location, corporate longevity, raw
material sources, etc."*

**Four of those clauses are materially weaker in E&S than in the 1977 admitted market, and the
10-K supports each from the filer's own text:**

1. **"Rates are an open book" is substantially false in E&S.** Admitted carriers must file
   rates and forms with each state regulator, and those filings are public — a competitor can
   read your price. E&S carriers do not file. Markel's E&S paper is written on *"Evanston
   Insurance Company, an Illinois domiciled E&S carrier licensed to do business in all 50
   states."* The rate is negotiated per risk and is not public.
2. **"Standardized policies which can be copied by anyone" is materially weaker.** Markel
   writes *"over 100 individually managed products, each with its own distinct competitive
   environment"* on *"more flexible policy forms."* A manuscript form for a wind farm or a
   marine-war risk is not a standardized policy.
3. **The filer names non-price competition explicitly**: *"In the standard market, regulations
   dictate relatively uniform products and coverages among competitors resulting in
   **competition primarily on the basis of price.** Competition in the specialty insurance
   market tends to **focus less on price and more on other value-based considerations**, such
   as service, distribution, expertise, capacity, product innovation, coverage limits, and
   financial strength ratings."*
4. **The channel is structurally scarce.** E&S is reached through wholesale brokers holding
   limited binding authority; 71% of Markel's U.S. Wholesale and Specialty gross written
   premium goes through wholesale brokers.

**And the market is growing and Markel is large in it:** *"In 2024, the E&S market represented
**$129.8 billion, or 12%, of the $1.1 trillion U.S. property and casualty industry.** In 2024,
we were the **fifth largest E&S writer** in the U.S. as measured by direct premium writings."*
(A.M. Best, *Market Segment Report — U.S. Surplus Lines*, 2025-09-09, cited in the 10-K.)

**That is the strongest available counter to [E2-70] and it is a real one.** It is recorded
here at full strength before it is tested, per **[E4-51]**.

### THEN, THE FOUR THINGS THAT DEFEAT IT

**(1) The corpus's own commodity doctrine reads E&S the WRONG way round. [E2-59]** is explicit
that administered pricing *floors* a commodity business's profits — pre-1970s insurers *"could
legally price their way to profitability even in the face of substantial over-capacity"* — and
that **the moat then belongs to the regime, not the company.** E&S's defining feature is the
*absence* of that regime. Freedom of rate is not a moat; **it is the removal of a floor.** It
lets Markel raise price in a hard market and it lets all four larger E&S writers, every Lloyd's
syndicate and every new Bermudian cut price in a soft one. On the corpus's own reading, E&S is
**more** exposed to **[E2-58]**'s equation — *"persistent over-capacity without administered
prices (or costs) equals poor profitability"* — not less.

**And Markel's 10-K states [E2-58] almost verbatim, as its own description of its industry:**
*"Historically, the performance of the property and casualty insurance industry has tended to
fluctuate in **cyclical periods of price competition and excess underwriting capacity, followed
by periods of high premium rates and shortages of underwriting capacity**… **During periods of
excess underwriting capacity, as defined by availability of capital, competition can result in
lower pricing and less favorable policy terms and conditions for insurers.**"* The supply-tight
to supply-ample ratio, in the filer's words. The scarce input is **capital**, and capital is
the one input with no barrier to entry at all.

**(2) [E2-58]'s single exception is a cost advantage "both wide and sustainable." Markel does
not have one, and its own ratio is moving the wrong way.**

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| Expense ratio | 34.4% | 35.5% | **36.1%** |

**Three consecutive years of rising expense ratio**, +1.7 points. This is the metric where a
wide-and-sustainable cost advantage would appear, and it is deteriorating. *(Peer comparison at
the competitor row below.)*

**(3) THE DECISIVE NUMBER — the underwriting profit is entirely prior-year reserve releases.**
From the 10-K's own underwriting ratio table (FY2025, Item 7):

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| Current accident year loss ratio | 64.9% | 65.6% | 64.2% |
| Prior accident years loss ratio | (0.5)% | (5.6)% | (5.8)% |
| Loss ratio | 64.5% | 60.0% | 58.4% |
| Expense ratio | 34.4% | 35.5% | 36.1% |
| **Reported combined ratio** | **98.8%** | **95.5%** | **94.6%** |
| **CURRENT-ACCIDENT-YEAR COMBINED RATIO** | **99.3%** | **101.1%** | **100.3%** |

**On the business it actually wrote in each of the last three years, Markel's underwriting lost
money in two of them and barely broke even in the third.** Every dollar of the reported
underwriting profit — $92.8M, $367.0M, $455.7M — comes from releasing reserves established in
earlier accident years. **$484,000k was released in 2025 alone.**

This is **[E4-40]** exactly: *"all of us in the industry made a fundamental underwriting mistake
by **focusing on experience, rather than exposure**."* A benign loss history produced by
releasing old reserves is *"not only useless, but actually dangerous"* as evidence of a moat.
And it is **[E2-50]**: *"Where 'earnings' can be created by the stroke of a pen, the dishonest
will gather"* — not an accusation, a scoping rule, and it says the reserve table carries the
weight here.

**(4) [E4-37]'s inverse metric cannot be run, because the filer stopped publishing the number.**
The corpus: *"you can almost measure the strength of a business over time by **the agony they go
through in determining whether a price increase can be sustained**."* For an insurer that agony
is published as a **numeric rate change**, and Markel's peers publish it. Markel publishes an
adjective: *"In 2025, we achieved **modest rate increases** overall across our diversified
product portfolio."* No number, in the whole 10-K.

### [E4-55] — THE PHYSICAL SERIES. THE ABSENCE IS THE FINDING.

The brief asked for policies in force, premium per policy, retention rates, and Ventures unit
series. Word-count against the FY2025 10-K:

| series | occurrences |
|---|---|
| "policies in force" | **0** |
| "policy count" | **0** |
| "renewal retention" | **0** |
| "retention" | 6 — **and all six mean *reinsurance* net retention**, not policyholder retention |
| numeric rate change | **0** |
| Ventures unit series (any physical measure) | **0** — only "organic revenue growth", a non-GAAP dollar measure |

*"Net retention of underwriting gross premium volume was 79% in 2025 compared to 78% in 2024"*
is the share of premium Markel keeps rather than cedes. **It is not a customer metric.**
**No physical series exists in this filing at all.** Under [E4-55], dollar revenue flattered by
pricing is how a shrinking franchise hides, and the honest series is unavailable.

### DIRECTION — [E4-32] says direction outranks existence, and the direction is negative

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Markel Insurance combined ratio | **90%** | 92% | 99% | 95% | **95%** |
| Earned premiums ($M) | 6,736* | 7,804* | 8,012 | 8,131 | 8,401 |

*\*operating revenues, segment basis, recast.* **The combined ratio is 4.3 points worse than
2021.** Earned premium grew **1.5%** in 2024 and **3.3%** in 2025 — at or below inflation.

**And three product lines were exited or converted in eighteen months, each on loss
performance or economics:**
- **Global Reinsurance into run-off, August 2025.** $1.0bn of gross premium. The 10-K: it *"had
  a two point unfavorable impact on the Markel Insurance segment combined ratio in 2025 and a
  one point unfavorable impact in 2024 and 2023."*
- **Risk-managed D&O withdrawn** from the European platform in late 2024 and the U.S. platform
  in early 2025 *"following **heightened loss performance**."*
- **U.S. classic car** (the Hagerty book) converted from underwriting to fronting on 2026-01-01.

A franchise narrowing on three fronts at once is [E4-32] running backwards.

### THE COMPETITOR ROW — required [E3-28]

**Metric: GAAP combined ratio, five years, filing-sourced.** Every cell taken from the filing
text; accessions in `_research 2026-09-02 MKL/competitor-row.md`.

| Company | 2021 | 2022 | 2023 | 2024 | 2025 | **5-yr mean** | rank |
|---|---|---|---|---|---|---|---|
| Kinsale (KNSL) | 77.1 | 78.5 | 75.4 | 76.4 | 75.9 | **76.66** | 1 |
| Arch (ACGL) | 85.2 | 81.6 | 79.3 | 82.5 | 82.8 | **82.28** | 2 |
| RLI | 86.8 | 84.4 | 86.6 | 86.2 | 83.6 | **85.52** | 3 |
| W. R. Berkley (WRB) | 89.6 | 89.3 | 89.7 | 90.3 | 90.7 | **89.92** | 4 |
| Fairfax (FFH) † | 95.0 | 94.7 | 93.2 | 92.7 | 93.0 | **93.72** | 5 |
| **MARKEL (MKL)** | **90.0** | **92.0** | **98.8** | **95.5** | **94.6** | **94.18** | **6** |
| Axis (AXS) | 97.5 | 95.8 | 99.9 | 92.3 | 89.8 | **95.06** | 7 |
| White Mountains (WTM) | — | — | — | — | — | **NOT REPORTED** ‡ | — |
| Berkshire (BRK-B) | — | — | — | — | — | **NOT REPORTED** § | — |

† *Fairfax reports under IFRS, not US GAAP; the ratio is a declared non-GAAP supplementary
measure covering only P&C (Life and Run-off excluded), basis breaks at IFRS 17 in 2022, and the
40-F primary document contains no combined ratio at all — it is in Exhibit 99.3. Its
**discounted** IFRS 17 ratio is far lower (84.6/81.0/81.4/83.9) and not comparable.*
‡ *White Mountains publishes **no consolidated combined ratio**; only the Ark/WM Outrigger
segment has one (82.40 five-year mean, and 2021–22 are Ark alone). This is the WTM run's Stage
0(b) finding showing up again — WTM is not really an insurer at the group level.*
§ *Berkshire's FY2025 10-K contains **zero occurrences of "combined ratio."***

**MARKEL RANKS 6th OF 7, AND LAST AMONG THE FIVE CLEAN US GAAP COMPARABLES.** Kinsale, Arch,
RLI and W. R. Berkley — all four direct E&S/specialty competitors, all filing the same metric on
the same basis over the same window — beat Markel by **4.3 to 17.5 points.** Kinsale, which
writes the same E&S risks through the same wholesale channel, runs **17.5 points better.**

**And the gap widens, not narrows, on the honest basis.** Markel's five-year mean is held up by
prior-year releases; on the current accident year it is **100.3% (2025)**, which would place it
**dead last by more than four points against the worst peer's reported figure.**

**Three comparability flags recorded rather than smoothed:** KNSL's 2022 is restated between
filings (77.9 → 78.5) because the denominator changed to add fee income; ACGL's 2021 is the only
year consolidating Watford (sub-total 84.3 vs total 85.2); AXS's 2023 spike to 99.9 is 8.1 points
of adverse reinsurance development. Every year appearing in two filings cross-checks exactly.

**On the row's own limit [E3-61]:** the row shows position, not conduct — *"I think you'd have to
know the people involved."* But position is what [E3-03] criterion 2 asks about, and **the
position is sixth.**

**§ The Berkshire absence is a finding in its own right.** The largest property-casualty
underwriter in the world does not report the metric the rest of the industry competes on. That is
[E4-55]-adjacent evidence that the combined ratio is a *management* yardstick rather than a
franchise measurement — which weakens the whole row as moat evidence, and therefore cuts against
any name that would need to *win* on it. Markel does not win on it either way.

**One row is already decisive and it came back before anything else: Berkshire Hathaway's
FY2025 10-K contains ZERO occurrences of the phrase "combined ratio."** The industry's own
headline underwriting metric is **absent from the filing of the largest property-casualty
underwriter in the world.** That is an [E4-55]-adjacent observation about the metric itself:
the one filer in this peer set that the corpus treats as the standard **does not report the
number the rest of the industry competes on**, which is evidence that the combined ratio is a
*management* yardstick rather than a *franchise* measurement. It does not rescue Markel — it
weakens the whole row as moat evidence, and that cuts against any name that would have to win
on it.

**Peers named: 8 (WTM, RLI, KNSL, AXS, WRB, ACGL, FFH, BRK-B) of an industry that has well
more than eight** — the 10-K itself cites an E&S market of $129.8bn in which Markel is fifth,
against *"large, global specialty insurance carriers,"* *"other Lloyd's syndicates,"* and
*"differentiated local market competition"* in 15 countries. **The row cannot be closed to the
industry's real breadth**, and [E3-61] states the row's limit anyway: identical structures
produce opposite conduct, and *"I think you'd have to know the people involved."*

### THE ATTACKER METRIC — return on unleveraged net tangible operating assets **[E2-43, E2-45]**

**It adapts, and it adapts unusually well, because the filer publishes the denominator itself.**
The FY2025 10-K reports **"tangible capital"** by segment — *"total capital less goodwill and
intangible assets, net of deferred taxes"* — which is [E2-43]'s *"unleveraged net tangible
assets"* almost exactly. **Adjusted operating income ÷ tangible capital, Markel Ventures
(Industrial + Financial + Consumer and Other combined):**

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Adjusted operating income ($M) | 452 | 754 | 774 | 772 | **845** |
| Tangible capital ($M) | 2,463 | 2,820 | 3,044 | 3,036 | **3,251** |
| **Return on tangible capital** | 18.4% | 26.7% | 25.4% | 25.4% | **26.0%** |

**That is a genuinely good number and it is the best fact in this file.** 25–26% on tangible
operating capital for four consecutive years is [E3-46]'s *"very high returns on capital
employed over time."* **It is reported here at full strength because it cuts against the
verdict.**

**Where it does NOT adapt: the insurance segment.** There is no meaningful "unleveraged net
tangible operating assets" for an underwriter, because the assets are a securities portfolio
funded by policyholders and the *leverage is the product*. Markel itself does not attempt it —
it publishes **return on equity** for Markel Insurance (13% five-year average) and tangible
capital only for the three Ventures segments. **Stated per the brief's instruction: the
attacker metric does not adapt to the underwriting business, and the honest substitute is the
cost of float [E3-69], computed at Q5.**

**But the growth behind that 25% has stopped.** Industrial organic revenue growth:
**21% (2021) → 18% → 8% → 0% → 2% (2025).** Industrial adjusted operating income has *fallen*
three years running: **$378M (2023) → $365M → $343M.** The return is high; the reinvestment
runway inside it is not visible.

### [E3-33] UNTAPPED PRICING POWER

**No.** Claiming it would be claiming *"a monopoly or a near monopoly"* **[E5-28]**, and the
filer's own disclosure is that it is **fifth** in a market where price is set by available
capital. The 10-K's pricing language is the opposite of untapped power: *"When we believe the
prevailing market price **will not support our underwriting profit targets, the business is not
written.**"* That is a price-taker describing walking away, not a price-setter declining to
raise.

### [E4-04] / [E4-23] — DOES SUCCESS DEPEND ON A GREAT MANAGER? **YES, AND THE FILING SAYS SO.**

*"Our investment strategy, **which is led by the Markel Group Chief Executive Officer (CEO)**,
prioritizes long-term value creation by allocating a substantial portion of the Markel
Insurance investment portfolio to equity securities."* The CEO personally runs the equity book
that carries the segment's return on equity, and the group's whole model — allocate across
underwriting, public equities and private acquisitions — is a capital-allocation model, which
is a *person*.

**[E2-70]** says the same thing about the underwriting half: *"there is no question that the
nature of the insurance business **magnifies the effect which individual managers have on
company performance.**"*

**[E4-23] governs: *"if a business requires a superstar to produce great results, the business
itself cannot be deemed great… The partnership's moat will go when the surgeon goes."* Recorded
here at Q2 as a moat defect, per the template — not at Q3 as a strength.**

### CLASS AND VERDICT

- Class: [ ] WIDE  [ ] NARROW  [x] **NONE**, on criterion 2 · **Direction: NEGATIVE**
- **The decisive reasoning on [E3-03] criterion 2:** E&S risks are placed *"primarily through
  wholesale insurance brokers."* **The wholesale broker's function is substitution** — the
  broker exists to shop one risk to several carriers. A buyer who wants Markel's marine-war
  cover can take Arch's, Kinsale's, RLI's, W. R. Berkley's, or a Lloyd's syndicate's, and the
  intermediary is paid to present exactly those alternatives. Markel is **fifth**. Its own
  stated means of competing is *"expertise"* — which is [E4-23]'s surgeon, not [E2-53]'s
  position. There is no *"close substitute"* failure here; **substitution is the market's
  distribution mechanism.**

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**⛔ THE FILE CLOSES HERE. Q3, Q4 and Q5 do not open. Everything below the line is
`COMPUTATION — NOT A CLEARANCE` under operator rule 3, reported because the queue's output
contract requires a price, and carrying no entry language.**

---
# COMPUTATION — NOT A CLEARANCE

*Operator rule 3. Q2 returned OUT; no figure below is a valuation of a cleared name. These are
reported because (a) the queue requires a price either way and (b) **the brief's central
question is whether the sector method works, and that question cannot be answered without
running the method to the end.***

## THE SCREEN ADJUDICATION — reproducing $2,294M, then decomposing it

**The screen printed:** cap $22,268M · bottom boundary $2,294M · top $2,474M · spread 7.8% ·
`level_shift` 1.67 ("STEP UP — normalize down [E4-41]") · **yield 10.30%** · perpetual growth
required to clear the [E4-28] floor **MINUS 0.30%**.

**Reproduced from the filed consolidated statements of cash flows.** OCF, D&A and capex hand-read
from three 10-Ks (FY2025 acc. 0001096343-26-000020 for 2023–25; FY2022 acc. 0001096343-23-000033
for 2020–22; FY2020 acc. 0001096343-21-000032 for 2018–19):

| window | mean OCF | less D&A | less capex |
|---|---|---|---|
| 3-year 2023–25 | $2,714,023k | $2,377,353k | **$2,473,855k** |
| 5-year 2021–25 | $2,625,116k | $2,282,444k | $2,401,023k |
| 8-year 2018–25 | $2,128,768k | $1,814,079k | $1,947,301k |

**The 3-year mean OCF less 3-year mean capex is $2,473,855k — the screen's top boundary of
$2,474M, exactly.** The bottom reproduces to within $83M (share-based compensation, which
Markel does not break out on the cash-flow statement, plus rounding). **So the screen is mean
operating cash flow less a capex charge, with no insurance-specific correction of any kind.**

### THE DECOMPOSITION, IN ORDER — how much of the 10.30% survives each correction

**Correction 1 — float growth is borrowed money [E2-61].** Premiums arrive before losses are
paid, so writing more business *looks* like cash generation. The increment sits inside operating
activities on the face of the filed statement, in eight named lines. Summed:

| year | OCF | float increment in OCF | **% of OCF** | net investment income | % of OCF |
|---|---|---|---|---|---|
| 2018 | 892,857 | 263,275 | 29.5% | 435,258 | 48.7% |
| 2019 | 1,274,120 | 396,683 | 31.1% | 442,182 | 34.7% |
| 2020 | 1,737,587 | 1,096,167 | **63.1%** | 375,826 | 21.6% |
| 2021 | 2,274,067 | 917,360 | 40.3% | 367,417 | 16.2% |
| 2022 | 2,709,442 | 1,199,386 | 44.3% | 446,755 | 16.5% |
| 2023 | 2,786,807 | 1,655,108 | **59.4%** | 734,532 | 26.4% |
| 2024 | 2,594,006 | 1,017,541 | 39.2% | 920,496 | 35.5% |
| 2025 | 2,761,256 | 960,275 | 34.8% | 970,427 | 35.1% |

**Cross-check that this identification is right:** the eight lines sum to +$960,275k in 2025,
and the filer's own published float rose $17,519M → $18,827M, i.e. **+$1,308M**. The difference
is FX translation and the life-and-annuity component, which is not a separate cash-flow line.
Same direction, same order of magnitude. The lines *are* the float.

**Correction 2 — net investment income is forbidden in the second factor [E5-48].** *"We exclude
in the second factor the dividends and interest from the investments we hold because including
them would produce a **double-counting of value**."* NII is 16–49% of OCF in every year.

**THE ANSWER THE BRIEF ASKED FOR, stated in order:**

| | 3-year 2023–25 | 5-year 2021–25 | 8-year 2018–25 |
|---|---|---|---|
| (0) mean OCF — **the screen's construction** | $2,714,023k = **11.99%** | $2,625,116k = **11.59%** | $2,128,768k = **9.40%** |
| (1) less float increment **[E2-61]** | $1,503,048k = **6.64%** | $1,475,182k = **6.52%** | $1,190,543k = **5.26%** |
| (2) less net investment income **[E5-48]** | $627,897k = **2.77%** | $787,256k = **3.48%** | $603,932k = **2.67%** |
| (3a) less (c) = capex | $387,729k = **1.71%** | $563,163k = **2.49%** | $422,465k = **1.87%** |
| (3b) less (c) = D&A | $291,226k = **1.29%** | $444,585k = **1.96%** | $289,243k = **1.28%** |

*(yields on the hand-verified cap of $22,642M)*

**Of the printed 10.30%, between 1.28 and 2.49 points survive — roughly one-eighth to
one-quarter.** The float correction alone removes about 5.3 points; the investment-income
correction removes about another 3.6. **This is the HOG failure at larger scale**: the screen
printed HOG at 18.97% and the full run found the motorcycle company lost money.

**BUT — and this is the part that matters for the brief's question — the 1.28–2.49% figure is
ALSO wrong, and wrongly low.** It charges the entire $22.6bn market capitalisation against only
the non-investment earnings, while pretending the $37.4bn securities portfolio is not there.
**That is the mirror image of the screen's error.** Neither number is the answer. **The sector
method exists precisely because neither single-yield construction works on a float-bearing
company**, and this run is the demonstration.

**Note on (c) — the capex band inverts here.** Capex is **below** D&A in all eight years
(8-year capex $181,467k mean against D&A $314,689k mean; ratio **0.58**). So the **D&A end is
the CONSERVATIVE end** on this filer, not the generous one — the reverse of the [E5-20]
railroad case. And [E3-44]'s D&A default is close to meaningless for a company whose real
maintenance requirement is **reserve adequacy**, not plant.

## STEP 2 — COST OF FLOAT **[E3-69]**, and the correction that halves the story

> *"a comparison of underwriting loss to float developed… meaningless over short time periods…
> But when the ratio takes in a period of years, it gives a rough indication of the cost of
> funds… **A low cost of funds signifies a good business; a high cost translates into a poor
> business.**"*

**CONVENTION 2 requires the window to be stated: five years, 2021–2025.** That is the longest
window available, and it is short **because the filer only began publishing float in the FY2025
10-K** — see [METHOD FINDING 1].

| year | underwriting profit | float | cost of float |
|---|---|---|---|
| 2021 | $614,331k | $13,543M | (4.54)% |
| 2022 | $594,289k | $14,947M | (3.98)% |
| 2023 | $92,786k | $16,733M | (0.55)% |
| 2024 | $366,976k | $17,519M | (2.09)% |
| 2025 | $455,671k | $18,827M | (2.42)% |

**Five-year cost of float = MINUS 2.60%** — Markel is *paid* 2.60% a year to hold $16.3bn.
Against the 5.27% sovereign that is a **7.87-point funding advantage, worth about $1,285M a
year pre-tax**. On [E3-69]'s own words this is emphatically *"a good business."*

**The correction, and it must be made: strip the reserve releases.** On a current-accident-year
basis (combined ratios 99.3% / 101.1% / 100.3%), the 2023–25 underwriting result is a **loss of
$58.6M in total**, and the cost of float becomes **PLUS 0.11%**.

**Reported honestly: even at +0.11%, float costing eleven basis points against a 5.27% sovereign
is still a ~5.16-point funding advantage. The [E3-69] test PASSES on either construction.**
This is the strongest fact against my own Q2 verdict and it is stated at full strength.

## STEP 1 AND STEP 3 — AND THE PLACE THE METHOD BREAKS OPEN

**Step 3, component 2 [E5-48]** — pre-tax, after overhead, interest, D&A and minorities, with
investment income removed:

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| consolidated adjusted operating income | 1,585,388 | 2,086,815 | 2,303,778 |
| less ALL net investment income **[E5-48]** | (734,532) | (920,496) | (970,427) |
| less amortization of acquired intangibles | (180,614) | (181,472) | (185,007) |
| less interest expense | (185,077) | (204,300) | (205,910) |
| less noncontrolling interests | (105,030) | (100,384) | (45,395) |
| **= COMPONENT 2, pre-tax** | **380,135** | **680,163** | **897,039** |

**3-year mean component 2 = $652,446k.** *(2025 alone is $897,039k; memo, net FX has averaged
−$72,280k over the same three years and is not deducted above.)*

**Step 1, component 1 — and the method gives TWO answers 2.68x apart:**

| construction | arithmetic | component 1 | per share |
|---|---|---|---|
| **B — corpus-literal [E5-46]**, float treated as free permanent equity | invested assets $37,439,262 − NCI $504,433 | **$36,935M** | **$2,981** |
| **A — float and debt subtracted as the liabilities they are** | B − float $18,827M − debt $4,304M | **$13,804M** | **$1,114** |

**The spread is $23,131M against a $22,642M market capitalisation. The ambiguity is larger than
the company.** **[METHOD FINDING 4]**

**Which is corpus-faithful?** B is. [E5-46] says *"all of our investments … those funded both by
float and by retained earnings … can be viewed as an element of value,"* conditioned on
underwriting breaking even — and [E3-52] licenses it: float is *"the benefit of debt … with none
of its drawbacks."* Markel's underwriting has been profitable on a reported basis in all five
years, so **the license holds on the corpus's stated test.**

**And B produces an answer I do not believe, which is the finding.** B gives component 1 alone
at **$2,981/share against a $1,827.44 price** — the securities portfolio, before a cent of
operating earnings, is 163% of the market capitalisation. Add component 2 at any multiple and
the value is roughly **$3,300–$4,150/share, a 1.8x to 2.3x screamer.** Construction A gives
roughly **$1,530–$2,270/share** — *straddling the price.*

**[E4-25] governs: *"Usually, the range must be so wide that no useful conclusion can be
reached."* The range here spans from "roughly fairly priced" to "trading at 44 cents on the
dollar," and the width comes from an unresolved question in the METHOD, not from the business.
That width IS the conclusion.**

## THE PRICE — the one construction I am willing to defend

**The look-through pre-tax earnings yield.** It counts the *income* the portfolio actually
produces rather than its market value, so it cannot double-count, and it ignores mark-to-market
entirely:

| | 3-year mean basis | FY2025 basis |
|---|---|---|
| component 2 (pre-tax, ex-investment income) | $652,446k | $897,039k |
| **plus** net investment income | $875,152k | $970,427k |
| **= look-through pre-tax earnings** | **$1,527,598k** | **$1,867,466k** |
| ÷ market cap $22,642M | **6.75%** | **8.25%** |
| against the USD sovereign **5.27%** | **+1.48 pts** | **+2.98 pts** |

**THE PRICE, as a round-number range [E4-01]:**
- **at the sovereign (5.27%): roughly $2,340 to $2,860 per share**
- **at the [E4-28] floor (10%): roughly $1,230 to $1,510 per share**
- **current price: $1,827.44** — *inside* the range and **above** the floor-based value.

**Growth required to clear the [E4-28] 10% floor: 1.75% to 3.25% perpetual**, against realised
adjusted-operating-income growth of **16.5% a year (2018 $792,483k → 2025 $2,303,778k)**.
**Against the screen's claim of MINUS 0.30%, the honest requirement is 1.75%–3.25% — still a low
bar, and this is the first name in this queue whose corrected requirement stays plausible.**

**Stated plainly, because the brief asked for it plainly: a substantial part of the 10.30% does
NOT survive — but the name does not collapse the way HOG, DKS or UAL did.** The corrected
look-through yield of 6.75%–8.25% is **above the sovereign on every construction**, which no
other name in this queue has managed. **It is Q2 that closes this file, not the price.** Under
**[E5-35]** that is the correct order: *"You can turn any investment into a bad deal by paying
too much. What you can't do is turn any investment into a good deal by paying little."*

**Windage count: ONE** — the reserve-release correction at step 2. Applied once, disclosed.

---
## THE [E2-49] METRIC SWITCH — ESTABLISHED EXACTLY: FY2024, AND SELF-DECLARED

**[E2-49]:** *"Yardsticks seldom are discarded while yielding favorable readings. But when
results deteriorate, most managers favor **disposition of the yardstick rather than disposition
of the manager**"* — demand *"pre-set, long-lived and small bullseyes."*

**THE ANSWER: the headline changed in fiscal 2024, and Markel says so itself.** FY2024 10-K
(acc. 0001096343-25-000027), Item 1, page "10K - 2", verbatim:

> *"We measure financial success using both operating income and total shareholder return… **Prior
> to 2024, we used growth in book value per share, rather than operating income, to measure our
> performance. As our business diversified beyond underwriting operations, book value became less
> indicative of intrinsic value because a significant portion of our operations is not recorded at
> fair value. We believe total operating income across the Markel Group system is a better measure
> of our performance.**"*

**The full sequence, from eleven 10-Ks read (FY2015–FY2025):**

| FY | headline per-share metric | BVPS stated |
|---|---|---|
| 2015–2019 | **book value per share** + 5-yr CAGR in BVPS | $561.23 → $802.59 |
| 2020–2022 | BVPS still the **first row** of "Consolidated Performance Measures" | $885.72 / $1,034.56 / **$929.27** |
| 2023 | BVPS **demoted** — closing-stock-price rows moved above it | $1,095.95 |
| **2024** | **BVPS REMOVED from the table entirely**; "Operating income (loss)" in its place | **NOT DISCLOSED** |
| **2025** | **"Adjusted operating income"** + **"5-Year CAGR in intrinsic value per share"** | **NOT DISCLOSED** |

**"Book value per share" occurs ONCE in the whole FY2024 10-K — in the sentence announcing its
retirement — and ZERO times in the FY2025 10-K.** This is not a demotion; **the metric was
withdrawn from the filing.**

**AFTER WHAT? The trigger was 2022, and the concession is on the record.** FY2022 10-K
(acc. 0001096343-23-000033), verbatim: *"Over the past five years, the compound annual growth in
book value per common share was **6%**… our common share price increased at a compound annual rate
of 3%. **While these measures, considered independently of other factors, fall below our internal
targets**, we remain confident in the strong operating performance of our businesses."* BVPS **fell
10% in 2022** and the five-year CAGR collapsed to 6%, the worst reading in the 2013–2023 series.

**And here is the part that convicts it. The switch did not come out of the trough — it came the
year AFTER the trough, and the retired metric was BEATING its replacement.** FY2023 10-K, verbatim:

> *"**We measure financial success by our ability to grow the market price per common share of our
> stock, or total shareholder return**… Over the past five years, our common share price increased
> at a compound annual rate of **6%**. We also have considered the performance of book value per
> common share over the long-term, **although we believe that as our business has evolved, this
> measure has become less reflective of shareholder value**… Over the past five years, the compound
> annual growth in book value per common share was **11%**."*

**Markel declared book value "less reflective of shareholder value" in the same sentence in which
it reported that book value had compounded at 11% while the stock price replacing it had compounded
at 6%.** [E2-49] describes disposing of the yardstick when results deteriorate; this is disposal of
the yardstick that was **winning**, in favour of one that was losing — and then, in 2025, of a third
that Markel computes itself.

**In fairness, and it is real fairness: this was telegraphed for seven years.** FY2017 10-K,
verbatim: *"we recognize that **book value per share does not capture all of the economic value in
our business**, as a growing portion of our operations are not recorded at fair value… beginning in
2018, we will also measure our financial success through the growth in the market price of a share
of our stock."* The stated reason — that Markel Ventures is carried at cost less depreciation while
the insurance investments are at fair value — **is economically correct.** A run that ignored that
would be unfair to the filer. [E2-49]'s own carve-out is that a switch *"announced ahead with
reasons (as Berkshire's own 1982 switch was) is the candor case."* **Markel announced it seven
years ahead with reasons. That is the candor case, and it is granted.**

**What is NOT granted is where it landed.** The FY2025 replacement is not a GAAP output at all:

> *"First, we take an adjusted earnings metric and apply a consistent multiple… **with 12x as the
> midpoint**… Second, we add certain items from our balance sheet… **Our simplified intrinsic value
> per share growth calculation may differ from calculations that others may perform, and our stock
> price growth may vary significantly from our intrinsic value growth calculation.**"*

**Markel replaced an audited, externally checkable per-share measure with a per-share measure it
computes itself, by applying a multiple of its own choosing to an adjusted earnings figure of its
own definition.** The sensitivity is disclosed (14.5% at 8x, 15.2% at 12x, 15.7% at 16x), which is
to its credit. But this is the opposite of [E2-49]'s *"pre-set, long-lived and small bullseyes"* —
it is a management valuation printed as a performance metric. **The flag fires, on the destination
rather than the announcement.**

**A second, quieter switch in the same family:** Markel Insurance's **"5-Year average annual return
on equity"** — now a headline — **was published for the first time in 2024**, and the 10-K concedes
why: *"presented beginning in 2024 due to the **impracticality of calculating return on equity prior
to 2020** for the newly defined Markel Insurance segment."* A five-year average introduced in the
year its own history begins has no record to be judged against.

**And a third, in the FY2025 filing.** MD&A, Item 7, verbatim: *"In 2025, we made notable changes to
our financial reporting, including **the re-segmentation of our businesses, the expansion of both
consolidated and segment financial metrics**, and the addition of detail regarding our business
strategy, among others."*

**What changed, all at once:**

1. **The reportable segments were rebuilt.** Note 2: *"The Company has four reportable segments:
   Markel Insurance, Industrial, Financial, and Consumer and Other."* The **Markel Ventures
   segment was dissolved** into three; the **Investing segment was dissolved entirely** — *"the
   results from the Company's investing activities, previously reported in the Investing segment,
   are now attributed to the Company's segments or corporate operations based on the subsidiary
   that holds the investments."*
2. **The headline metric became "5-Year CAGR in intrinsic value per share"** — a **company-defined,
   non-GAAP, multiple-based construct**: *"we take an adjusted earnings metric and apply a
   consistent multiple… **with 12x as the midpoint**… Second, we add certain items from our
   balance sheet."* The filer publishes it at three multiples: **14.5% / 15.2% / 15.7%.**
3. **Operating revenues were recast to exclude net investment gains**, and *"prior periods have
   been recast."*
4. **Corporate expense allocation was discontinued mid-year**: *"beginning in the third quarter
   of 2025, the Company discontinued allocating corporate expenses that are not integral to
   operating its underlying businesses."*

**[BRIEF DEFECT 1 — and it is the load-bearing one.]** The brief states: *"Markel reports three
engines: Insurance, Investments, and Markel Ventures… That is [E5-46] and [E5-47] made explicit
in the filer's own segment structure — **the first component and the second component, published
separately.** Nowhere else in the queue is the corpus's method so nearly pre-computed by the
registrant."*

**As of the FY2025 10-K that is no longer true, and the change runs in exactly the direction
[E5-48] forbids.** Investment income is now reported **inside** the Markel Insurance segment's
"adjusted operating income," and the filer's own segment-performance definition says so: *"We
measure the operating performance of our Markel Insurance segment by its operating revenues and
adjusted operating income, **which are comprised of results attributed to its insurance
activities and earnings on the investments held in support of its insurance activities.**"*
**The two components the method needs kept apart have been merged by the registrant, in the most
recent filing, and prior periods were recast so the old separation cannot be recovered from the
current document.** The run had to un-merge them by hand — that is the $970,427k line removed at
step 3 above.

**Did the switch FOLLOW deterioration? On the segment that drives the group, yes.** Markel
Insurance's return on equity: **20% (2021) → (3)% (2022) → 16% (2023) → 18% (2024) → 14% (2025)**,
and the 5-year average annual ROE the filer now leads with **was published for the first time in
2024** — the 10-K concedes the reason: *"Markel Insurance's 5-year average annual return on
equity is presented beginning in 2024 due to the impracticality of calculating return on equity
prior to 2020 for the newly defined Markel Insurance segment."* **A five-year average introduced
in the year it began is a metric with no history to be judged against**, which is the opposite of
[E2-49]'s *"pre-set, long-lived and small bullseyes."*

**The candor side, stated fairly:** the changes are **disclosed, explained, and prior periods are
recast** — which is the [E2-67] standard of publishing your own restatement, and it is genuinely
better conduct than the HD/QCOM/ULTA switches this test has fired on before. **But the direction
is the tell**: every one of the four changes moves reporting *away* from an externally-checkable
GAAP figure and *toward* a company-defined construct with a company-chosen multiple. A filer that
adopts "intrinsic value per share, at 12x our own adjusted earnings" as its headline has, in
[E3-50]'s words, taken control of the yardstick. **The flag fires. It is a prompt to read, not a
verdict [E5-36], and Q2 had already closed the file.**

---
## MATERIAL GATHERED FOR Q3 AND Q4 — **NOT ADJUDICATED**

**⛔ Q2 returned OUT, so Q3 and Q4 never opened and NO VERDICT is rendered on either.** The brief
commissioned three specific Q3/Q4 tests, and the evidence was gathered before Q2 closed. It is
recorded here so the work is not lost and so the reader can check the Q2 verdict against it —
**not** scored. Rendering a Q3 verdict after a Q2 OUT would violate the hard sequence.

### [E2-67] — RESERVE DEVELOPMENT AS THE CANDOR TEST. **Markel passes it, and passes it well.**

The sector method makes this the candor read for a reserve-driven filer **[E2-50]**. The corpus's
positive pole is Berkshire publishing its own reserving errors *"so you can… judge whether we may
have some systemic bias."*

**Markel does all four things the standard asks, and the fourth is the rare one:**
1. **It names its own bias, in four separate places**, including Item 1 of the 10-K: *"through its
   long-standing practice of **establishing reserves that are more likely to be redundant than
   deficient**."* Note 11 repeats it and adds the asymmetry: *"management responds quickly to
   increase loss reserves following any indication of increased claims frequency or severity…
   however in instances where trends have been more favorable than previously anticipated,
   management will **wait to reduce loss reserves** until those trends are observed over additional
   periods."*
2. **It publishes a ten-year loss development triangle** (note 11(d), accident years 2016–2025),
   with the run-off Global Reinsurance division **broken out separately**.
3. **It states the streak and its length**: *"reserves have developed favorably for **each of the
   past 21 years**."*
4. **It then tells the reader not to trust it**: *"**we caution readers not to place undue reliance
   on this favorable trend.**"* That clause is the part most insurers omit, and it is the [E2-26]
   half-owner test satisfied.

**Development, all five years favorable:** 2021 **$479.8M** · 2022 **$167.4M** · 2023 **$38.6M**
(0.3% of opening reserves — effectively nil) · 2024 **$455.3M** · 2025 **$488.3M**.

**What the triangle shows that the headline does not — and it cuts toward the Q2 verdict:**
- **Accident year 2018 has developed cumulatively ADVERSE**: first booked $2,407.9M, marked down to
  $2,125.5M by year-end 2019, and **strengthened in every year since 2020** to $2,427.2M. A released
  redundancy clawed back in full and then some.
- **AY2022 was released too early and partly taken back**: 3,591.3 → 3,315.1 → 3,320.1 → 3,358.4.
- **Adverse development has run continuously somewhere in the book for four straight years**:
  2023 **−$326.8M** (U.S. general liability and professional liability — *"$331.9 million, or 11
  points on the U.S. Wholesale and Specialty combined ratio"*), 2024 **−$176.9M** (risk-managed
  D&O), 2025 **−$128.8M** (run-off D&O). **The 21-year streak is intact at the consolidated level
  and broken at the line level.**
- **The guided range has gone one-sided.** FY2022 guided *"adverse development of 2%, or $200
  million, to favorable development of 6%, or $800 million."* FY2025 guides *"favorable development
  of up to 5%, or $800 million"* — **adverse development is no longer contemplated in the range.**

**Direction of the error, stated as [E2-67] requires: REDUNDANT.** Reserves have been consistently
set above the actuarial point estimate and released later. **The filer names it. The test passes.**
*(And it is precisely this redundancy-and-release pattern that produces the reported underwriting
profit which Q2 found is absent on the current accident year. Both statements are true.)*

### [E2-62] — CONCENTRATION IS LICENSED BY LOSS-ABSORPTION
Equity securities **$13,004,312k at market against shareholders' equity of $18,597,756k — 69.9% of
book in stocks**, at a cost basis of $4,094,745k (unrealised gain **$8,909,567k**), marked through
net income under ASU 2016-01. **[E2-62]:** concentration *"makes sense only because our insurance
business is conducted from a position of exceptional financial strength. For almost all other
insurers, a comparable degree of concentration (or anything close to it) would be totally
inappropriate."* **The method document's own warning is against reading the eight smaller names as
small Berkshires. Recorded, not scored.** A 40% equity drawdown is ~$5.2bn, ~28% of book.

### [E5-11] STRENGTH (2), RE-EXPRESSED PER [E2-61] — recorded, not scored
Debt-to-capital **19%** (2025), down from 24% (2022); senior debt $4,304M against $37,439M of
invested assets; preferred stock **fully redeemed June 2025** ($600M). Read as reserve adequacy and
net worth rather than cash, per the substitution. **No score rendered.**

### GOODWILL AND THE VENTURES ACQUISITION RECORD **[E5-50]** — partial, not scored
**Exactly one impairment in six years: $80.0M in 2022, on the Nephila ILS fund-management unit**,
reducing that unit's goodwill to $221.8M — elevated catastrophe losses since the 2018 acquisition,
Hurricane Ian, ILS investor redemptions, rising cost of capital. Determined by a **quantitative** DCF
test. **No goodwill or indefinite-lived intangible impairment in 2019, 2020, 2021, 2023, 2024 or
2025**, each stated in the respective note 8. *(A recurring $16,800 "Impairment of goodwill" line in
the FY2022–FY2024 tax-rate reconciliations is the non-deductible portion of the same $80M charge,
not a second impairment — trap flagged and avoided.)*

**The base rate worth carrying: $4,365,093k of goodwill and intangibles has produced a single 1.8%
write-down in six years**, and Markel defaults to **qualitative** testing justified partly on the
ground that the purchase price represented fair value at acquisition — reasoning that is close to
circular. **The one time it ran a quantitative test on a stressed unit, it took a charge.**

**NOT OBTAINED, and named as work orders rather than glossed:**
- **Pay versus performance** — the DG/ULTA instrument (a target set BELOW the prior year's actual,
  paying ~182%) was **not run**. Artifact: DEF 14A filed **2026-04-02, acc. 0001096343-26-000033**,
  plus the 2025 and 2024 proxies. Q3 never opened, so this is not a gap in a verdict.
- **The full Markel Ventures acquisition record** — consideration paid per deal against what each
  earns. Artifact: the business-combination footnote across FY2005–FY2025 10-Ks.
- **[E3-54] retention test** ($1 of market value per $1 retained, five-year rolling) — the third
  element **[E5-50]** was therefore **not** rendered as an up-or-down judgment. **The brief required
  it at Q5 step 5; Q5 did not open, and inventing the judgment anyway would be the error operator
  rule 3 exists to prevent.**

---
# JOB 2 — WHERE THE SECTOR METHOD DOES NOT FIT

**[METHOD FINDING 1] — the method assumed a float series that this filer published for the first
time three months ago.** Occurrences of the word "float" in Markel's 10-Ks:

| FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| **0** | **0** | **0** | **0** | **0** | present, with a 5-year series |

The brief said *"Markel publishes float and combined ratio; build the series."* **Markel began
publishing float in the FY2025 10-K, filed 2026-02-26, and only back to 2021.** [E3-69] demands
*"a period of years"*; five is what exists, from a first-time disclosure, introduced in the same
filing as a re-segmentation. **This is the WTM finding replicating on a second filer, and it
generalises: float is a Berkshire disclosure convention, not an industry one.**

**[METHOD FINDING 2] — CONVENTION 4 validated, first time, to −1.1%.** Markel is the first filer
where both a published float and the constructed recipe exist. The recipe reproduced the
published figure to about one percent. **CONVENTION 4 should be retained.** Recommended
refinement, from this run: adding *payables to insurance and reinsurance companies* and
subtracting *prepaid reinsurance premiums* closes most of the residual.

**[METHOD FINDING 3] — Stage 0(b) tests the wrong ratio, and the amendment only guards one
side.** The amendment tells a run what to do when float ÷ investments is **low** (WTM 22.0% →
"step 2 is a minor term"). It says nothing about the **high** side. Markel is **50.3%, above
Berkshire's 41.8%.** The ratio that actually governs whether [E5-46] is safe is **investments ÷
shareholders' equity**: Berkshire **0.45x**, Markel **2.01x**. Berkshire's investments were
*smaller than its own equity*, so counting them at market could not double-count. Markel's are
twice its equity. **Recommendation: Stage 0(b) should compute investments ÷ equity as well, and
where it exceeds 1.0x the run must state which construction of component 1 it is using and why.**

**[METHOD FINDING 4] — the method does not say whether float is subtracted from component 1, and
on this filer the silence is worth $23.1bn.** Constructions A and B differ by **2.68x**, a spread
larger than the market capitalisation. On Berkshire the same ambiguity is nearly harmless. **The
method is under-specified in exactly the place it is most load-bearing, and it did not know it
because it was derived from the one filer where the question does not bite.**

**[METHOD FINDING 5] — steps 2 and 3 double-count underwriting profit as written.** Step 2 says
*"Negative cost is a credit; positive cost is a charge."* Step 3 says *"pre-tax earnings of
everything else,"* and [E5-48]'s 2015 amendment **includes underwriting income** in the second
factor. **If step 2 credits negative float cost as value AND step 3 capitalises the underwriting
profit, the same $455,671k is counted twice.** This run resolved it by treating **step 2 as the
license-test for step 1** (is the float free? — [E5-46]'s own condition) and putting underwriting
profit **only** in step 3. **That resolution should be written into the method document; it is
not there now.**

**[METHOD FINDING 6] — the method has no rule for the deferred tax on unrealised gains, and
[E3-71] supplies one it does not use.** Markel's equities are **$13,004,312k at market against
$4,094,745k of cost — $8,909,567k of unrealised gain**, carrying a deferred tax liability of
roughly **$1,871,000k at 21% (about $151/share)**. Step 1 says "investments at market" and stops.
**[E3-71]** explicitly values the deferred-tax item as *"an interest-free loan — never at face,
never at zero."* **Step 1 should carry that instruction; it does not.**

**[METHOD FINDING 7] — the method's (c) discussion is inapplicable and should say so.** The
framework's capex band is meaningless for a float-bearing company: Markel's capex/D&A is **0.58**,
so the [E3-44] D&A default is the *conservative* end, and neither end measures the thing that
actually has to be maintained, which is **reserve adequacy**. The method inherits Q4's capex
machinery without noting that it does not bite.

**[METHOD FINDING 8] — the multi-currency gap replicates.** Markel's International division
operates in **15 countries** and the FY2025 income statement carries **net foreign exchange losses
of $256,234k** — 9.4% of pre-tax income, swinging to **+$129,438k** in 2024. Per the amendment's
FINDING 8 this run **states the exposure, uses the reporting currency's sovereign (USD 5.27%), and
records that the choice is unresolved.** No blending rule invented.

**[METHOD FINDING 9 — NEW, and it is a warning about the method's own success condition.]** The
method's premise is that the registrant publishes the two components separately. **Markel did,
and then stopped.** The FY2025 re-segmentation merged investment income into the insurance
segment and recast prior periods. **A method that depends on a filer's voluntary segment
presentation is hostage to it.** Any future application must check whether the separation still
exists in the *current* filing rather than assuming the structure the brief describes.

---
## SELF-AUDIT
- [x] Questions answered in order; stopped at the first non-IN verdict (Q2 OUT)
- [x] No question marked IN carries an "unverified" or "provisional" caveat
- [x] Q5 was NOT opened. All valuation output is headed **COMPUTATION — NOT A CLEARANCE** and
      carries no entry language (operator rule 3)
- [x] Step 0: filings read with accession numbers; two figures cross-checked by hand
      (adjusted operating income $2,303,778k reconciled three ways; invested assets $37,439,262k
      rebuilt from the balance sheet as 32,835,960 + 3,964,705 + 638,597)
- [x] Share count hand-read off the 10-Q cover; single class confirmed
- [x] Competitor row attempted; peers incomplete and **stated as incomplete** rather than filled
- [x] Sovereign for the earnings currency, from the issuing authority, dated
- [x] Value stated as a round-number range
- [x] Windage count stated: ONE
- [x] Prices dated; aggregator used for the live quote only and flagged
- [ ] Run committed to git — *done at the commit following this write*

## REGISTER
- **Verdict: OUT (about the business), at Q2.**
- **One line:** Markel is a well-run float-bearing holding company whose float costs it less than
  nothing and whose private operating businesses earn 25–26% on tangible capital — and it is not
  a franchise, because its underwriting has lost money on the current accident year in two of the
  last three years, its expense ratio has risen three years running, it is fifth in a market
  reached through brokers whose function is substitution, and it publishes no numeric rate change
  and no physical unit series at all.
- **PRICE: $1,827.44** (2026-09-02). Value, reported under COMPUTATION — NOT A CLEARANCE:
  **~$2,340–$2,860/share at the sovereign; ~$1,230–$1,510/share at the [E4-28] floor.**
- **PASS/FAIL: FAIL — closed at Q2 (OUT).** Q1 returned IN.

