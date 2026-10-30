# Company Run — Shopify Inc. (SHOP) — 2026-09-07
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
## STEP 0 — THE RATE, THE FILER STATUS, THE COVER, AND THE FILING

### The sovereign, for the currency the business EARNS in **[E4-15, E3-32]**

- rate **5.24 %** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-yr
  (issuing authority, struck this session via `tools/sources.py`; not the FRED fallback)**

**The brief asked whether a Canadian filer takes a Canadian sovereign. It does not, and the
filing settles it in one sentence.** Shopify Inc. is incorporated in Canada (10-K cover:
*"Canada"*, head office **151 O'Connor Street, Ottawa, Ontario**, with a second principal
office at 85 10th Avenue, New York). But:

> *"We prepare and report our consolidated financial statements in accordance with
> accounting principles generally accepted in the United States of America ("U.S. GAAP").
> **Our reporting currency is U.S. dollars**, and we express all amounts in this Annual
> Report on Form 10-K in U.S. dollars, except where otherwise indicated."* — FY2025 10-K,
> "General Matters"

**Every dollar in this file is a US dollar. Operator rule 5 asks for the sovereign of the
earnings currency, and that is USD.** The Bank of Canada 30-year is not the right rate for
a company that reports, prices, invoices and settles in USD. *(Recorded, not waved away:
Shopify does earn in local currencies abroad and discloses currency-conversion fees as a
revenue line inside merchant solutions. The reporting currency is nonetheless USD and the
FX exposure is a Q4 item, not a Step 0 one.)*

### THE FILER STATUS — and it changed, which matters for the vintage sweep

**The brief asked. The answer is: BOTH, and the switch is dated.** Shopify filed as a
**foreign private issuer under the MJDS regime (Form 40-F) for FY2016 through FY2023**, and
a **Form 20-F for FY2015**. It became a **US domestic filer** and filed its **first Form
10-K for FY2024 on 2025-02-11**. Full list, from `data.sec.gov/submissions/CIK0001594805`:

| FY | form | filed | accession |
|---|---|---|---|
| 2015 | 20-F | 2016-02-17 | `0001594805-16-000019` |
| 2016 | 40-F | 2017-02-15 | `0001594805-17-000007` |
| 2017 | 40-F | 2018-02-15 | `0001594805-18-000009` |
| 2018 | 40-F | 2019-02-12 | `0001594805-19-000010` |
| 2019 | 40-F | 2020-02-12 | `0001594805-20-000010` |
| 2020 | 40-F | 2021-02-17 | `0001594805-21-000008` |
| 2021 | 40-F | 2022-02-16 | `0001594805-22-000011` |
| 2022 | 40-F | 2023-02-16 | `0001594805-23-000011` |
| 2023 | 40-F | 2024-02-13 | `0001594805-24-000007` |
| **2024** | **10-K** | **2025-02-11** | `0001594805-25-000012` |
| **2025** | **10-K** | **2026-02-11** | **`0001594805-26-000007`** |

**Why this is a finding and not trivia.** Under the 40-F regime the MD&A is filed as
**Exhibit 13**, a separate document, and the operating-metric tables live there rather than
in the primary document. A vintage sweep that reads only `shop-YYYYMMDD.htm` finds nothing
before FY2024 and would wrongly conclude the metrics were never filed. The vintage MD&As
read here are `exhibit13mdaq42023.htm`, `exhibit13mda2021.htm` and `exhibit13mda2019.htm`.
**The 40-F years are also the reason [E3-66] gets a real answer at Q4** — Shopify's
shareholders sit in a Canadian queue, not a US one, and the run states where.

### STAGE 0 — THE COVER COUNT, BY HAND. **AND THE SCREEN'S CAP IS WRONG BY 3.40x — THE LARGEST CAP DEFECT THIS PROJECT HAS FOUND.**

**1. The count, re-read from the cover this session.** `python Screens/cover_shares.py SHOP`:

    10-Q filed 2026-08-05, period 2026-06-30, accession 0001594805-26-000047
    Class A Subordinate Voting                     1,208,570,347
    Class B Multiple Voting                           78,073,584
    Class B Multiple Voting                                    1
    --- arithmetic sum, NOT a share count ---      1,286,643,932
    MULTIPLE CLASSES. Whether these are economically equivalent is a JUDGMENT
    from the charter, not arithmetic. READ THE FILING.

**2. The judgment the tool refuses to make, made here from the charter description in the
filing — and there are THREE classes, not two.** The third row above is not a rounding
artifact. It is **one single share**, and it is the Founder Share.

> *"The **Founder Share** provides a variable number of votes that represents, when combined
> with the votes attached to certain other voting shares of Shopify beneficially owned or
> controlled by Tobias Lütke, his immediate family and affiliates, **at least 40% of the
> aggregate voting power** attached to all of Shopify's outstanding voting shares, provided
> that such variable number of votes does not cause the aggregate voting power … **to exceed
> 49.9%** … **There are no economic rights associated with the Founder Share**, and in
> certain circumstances, Tobias Lütke could have voting power that is substantially greater
> than his economic interests and the percentage of shares that he holds."* — FY2025 10-K,
> Item 1A

> *"However, because of the variable voting power of the Founder Share, which effectively
> sets and preserves Tobias Lütke's voting power, **future issuances of Class A subordinate
> voting shares will not generally result in dilution of the voting power of Tobias
> Lütke**."*

**DECISION, three parts:**
- **The Founder Share carries NO economic rights and is excluded from value** — but including
  it changes the count by one share out of 1.29 billion, so the arithmetic is identical
  either way. It is excluded on principle, not for materiality.
- **Class A subordinate voting and Class B restricted voting ARE economically equivalent and
  summing them is correct.** They share the same "Common stock" line on the balance sheet
  ($10,376M at 2025-12-31, undivided), the same single EPS figure is struck across both
  ($0.95 basic FY2025 on 1,298,955,860 weighted shares — there is no two-class EPS split in
  the filing), and Class B converts 1:1 into Class A. **The difference is votes, not money.**
- **The governance finding is recorded at Q3, not here.** A single share engineered to hold
  40%-to-49.9% of the vote in perpetuity, *immune by construction to dilution from every
  future issuance*, is a live Q3 item under **[E2-26]** and **[E3-66]**. It is not a
  share-count adjustment.

**COUNT USED: 1,286,643,932** (10-Q cover, as of the filing's own as-of date; the Founder
Share's single unit included in the arithmetic and worth nothing).

**3. THE PRICE IS RE-STRUCK, AND THE SCREEN'S CAP IS OFF BY A FACTOR OF 3.40.**

- **price $145.09 · 2026-09-04 close · aggregator, FLAGGED, live quote only** (operator rule 5).
- **MARKET CAP = $145.09 × 1,286,643,932 = $186,679M.**
- **The published row says `cap_m 54964`.** That is **$54,964M against a true $186,679M** —
  **the screen understates Shopify's market capitalisation by $131.7 billion.**

**I reproduced the defect exactly, and it is the LEVI/PINS mechanism in its sixth and worst
instance.** `Screens/floor_screen.shares_outstanding()` tries `dei:EntityCommonStock
SharesOutstanding` first, then `us-gaap:CommonStockSharesOutstanding`, then
`us-gaap:CommonStockSharesIssued`. On Shopify:

| tag | rows in `companyfacts` | newest value |
|---|---|---|
| `dei:EntityCommonStockSharesOutstanding` | **0** | — |
| `us-gaap:CommonStockSharesOutstanding` | 2 | **39,310,446 at 2014-12-31** (20-F, `0001594805-16-000019`) |
| `us-gaap:CommonStockSharesIssued` | 2 | 39,310,446 at 2014-12-31 |

**39,310,446 is Shopify's share count at 31 December 2014 — five months BEFORE its May 2015
IPO and seven and a half years before its 10-for-1 split of June 2022.** Applying the split
(correctly, per the split-invariance rule) gives **393,104,460**, and:

    393,104,460 x $139.82 (the 2026-09-01 close) = $54,963,867,000  =  cap_m 54,964

**That reproduces the published figure to the dollar.** The count is **11.7 years stale**,
**pre-IPO**, and the market cap it produces is **29.4% of the true one**. *(The 550-day
staleness guard inside `shares_outstanding()` should have returned `None` and left the row
unpriced; it did not, and the row was published with a confident four-significant-figure
cap. Recorded as a tooling defect, not patched in this run — operator rule 8.)*

**Independent confirmation from the filing itself, so this does not rest on my arithmetic:**
the FY2025 10-K cover reports **`dei:EntityPublicFloat` = $140,315,345,495 as of
2025-06-30.** A company with a **$140.3 billion public float** cannot have a $55.0 billion
market capitalisation. **The screen's cap is smaller than Shopify's disclosed free float by
$85 billion.**

**Every downstream figure in the published row is therefore wrong in the same direction:**

| | published | corrected |
|---|---|---|
| cap | $54,964M | **$186,679M** |
| `yield_bottom` | 0.85% | **0.25%** |
| `vs_sovereign` | −4.39 pts | **−4.99 pts** |
| `growth_required` | 9.15% | **9.75%** |

**The row was already the worst yield in its neighbourhood. It is three times worse than
printed.**

**4. And the count is moving, for the first time in the company's history.** From the filed
Statements of Changes in Shareholders' Equity:

| | total shares | event |
|---|---|---|
| 2024-12-31 | 1,294,580,140 | |
| 2025-12-31 | 1,303,904,301 | +9.3M, all issuance; **no repurchases, ever** |
| 2026-03-31 | 1,300,779,030 | **first buyback in company history: 4,214,019 shares, $521M** |
| **2026-06-30** | **1,289,206,588** | **12,645,957 more shares, $1,445M** |

**$1,911M of cash spent on repurchases in the first half of 2026, against $0 in every prior
year of the company's existence.** Treated in full at Q3 under **[E5-08]**.

### The filing was read — not tagged data **[E3-27, E4-14]**

- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary: FY2025 Form 10-K, FYE 2025-12-31, filed 2026-02-11, accession
  `0001594805-26-000007`** (document `shop-20251231.htm`).
- **Newest: Q2 2026 Form 10-Q, period 2026-06-30, filed 2026-08-05, accession
  `0001594805-26-000047`** — and it carries two facts the 10-K cannot: the first buyback and
  a cash-flow presentation change. Also read: Q2 2025 10-Q `0001594805-25-000073`, for the
  comparability check on that change.
- Vintages read for the disclosure-history and metric tests: FY2024 10-K
  `0001594805-25-000012`; FY2023 40-F `0001594805-24-000007` (MD&A at
  `exhibit13mdaq42023.htm`); FY2021 40-F `0001594805-22-000011` (`exhibit13mda2021.htm`);
  FY2019 40-F `0001594805-20-000010` (`exhibit13mda2019.htm`); plus the FY2017/2018/2020/2022
  statements for the revenue-split series.
- **Figures cross-checked against the filed statement (operator rule 4):**
  1. XBRL returns FY2025 operating cash flow of $2,033M. The filed Consolidated Statements
     of Cash Flows reads **"Net cash provided by operating activities 2,033"** — agrees.
  2. **SBC, because the brief said it might decide the run:** XBRL
     `AllocatedShareBasedCompensationExpense` FY2025 = $449M; the filed cash-flow
     adjustments block reads **"Stock-based compensation 449"** — agrees.
  3. **Capex:** the filed investing section reads **"Purchases of property and equipment
     (26)"** against XBRL `PaymentsToAcquirePropertyPlantAndEquipment` $26M — agrees.
  4. **Gross profit by revenue line**, which is the AMAT test the brief demanded: the filed
     income statement's dimensioned rows give subscription revenue 2,752 / cost 520 and
     merchant revenue 8,804 / cost 5,481; **2,232 + 3,323 = 5,555 = the filed consolidated
     gross profit** — the split reconciles to the total exactly.

---
## THE SCREEN ROW — REPRODUCED, AND THE THREE `n/a`s ARE THE FINDING **[E4-25]**

**The published row** (`Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`, line 219):

    SHOP, cap_m 54,964 · oe_bottom_m 465 · oe_top_m 1,005 · spread 1.163 ·
    yield_bottom 0.0085 · vs_sovereign -0.0439 · growth_required 0.0915 ·
    level_shift n/a "EARLY HALF STRADDLES ZERO" ·
    level_shift_oe n/a "EARLY HALF STRADDLES ZERO - runs from -$735.0M" ·
    level_shift_full n/a (13 years filed) ·
    best_year_dep 0.566 "TWO YEARS JOINTLY CARRY THE WINDOW" ·
    best_year_dep_oe 1.271 · newest_filing 2025-12-31

**Every arithmetic figure except the cap reproduces.** `oe_bottom 465` is the **5-year mean
at the D&A end of (c)**; `oe_top 1,005` is the **3-year mean at the total-capex end**;
`spread 1.163` is (1005−465)/465. The `-$735.0M` in the `level_shift_oe` verdict string is
**FY2022 owner earnings**, and it is exactly right.

**THE THREE `n/a`s ARE ALL TRUE, AND THEY ARE TRUE FOR ONE REASON.** Here is the full
thirteen-year series they choked on, every figure from a filed cash-flow statement:

| year | OCF $M | SBC $M | capex $M | D&A $M | **OE @(c)=capex** | OE @(c)=D&A |
|---|---|---|---|---|---|---|
| 2013 | 1.4 | 1.8 | 3.5 | 1.8 | **(3.9)** | (2.2) |
| 2014 | (0.8) | 4.4 | 20.6 | 4.7 | **(25.8)** | (9.9) |
| 2015 | 15.8 | 8.2 | 16.5 | 7.2 | **(8.9)** | 0.4 |
| 2016 | 14.0 | 23.1 | 23.8 | 14.0 | **(32.9)** | (23.1) |
| 2017 | 7.9 | 49.2 | 20.0 | 23.4 | **(61.3)** | (64.7) |
| 2018 | 9.3 | 95.7 | 27.9 | 27.1 | **(114.3)** | (113.5) |
| 2019 | 70.6 | 158.5 | 56.8 | 35.7 | **(144.7)** | (123.6) |
| 2020 | 425.0 | 246.9 | 41.7 | 70.1 | **136.4** | 108.0 |
| 2021 | 535.7 | 330.8 | 50.8 | 66.3 | **154.1** | 138.6 |
| **2022** | **(136.0)** | 549.0 | 50.0 | 93.0 | **(735.0)** | (778.0) |
| 2023 | 944.0 | 615.0 | 39.0 | 70.0 | **290.0** | 259.0 |
| 2024 | 1,616.0 | 430.0 | 19.0 | 36.0 | **1,167.0** | 1,150.0 |
| **2025** | **2,033.0** | **449.0** | **26.0** | **31.0** | **1,558.0** | **1,553.0** |

**Seven consecutive negative years, then a positive pair, then the worst year in the file,
then the best three.** No ratio of an early mean to a late mean is definable on that, and
the tool was right to refuse three times. **[E4-25]** is the governing line: *"Usually, the
range must be so wide that no useful conclusion can be reached."* The refusal is the
diagnosis, and the diagnosis is that **the thirteen-year series is not one company.**

**`best_year_dep_oe 1.271` — THE HIGHEST IN THE 361-NAME QUEUE, AND I CONFIRM IT AND THEN
SHOW IT UNDERSTATES THE PROBLEM.** Dropping the best **two** owner-earnings years (2025 and
2024) from the nine-year window moves the mean by **127%**. Reproduced: the 9-year
(2017–2025) OE mean at the capex end is **$250.0M**; drop 2025 and 2024 and the remaining
seven average **$(66.5)M** — the mean does not merely move 127%, **it changes sign.**
A percentage is not really definable across a sign change, which is the same defect class
the DAL and TTSH rows carry, and the honest statement is the one the framework asks for:
**$250M becomes minus $67M. Two years out of nine carry the entire positive result.**

### THE BRIEF'S THREE MANDATORY CORRECTIONS — ALL THREE RUN

**CORRECTION 1 — the spread caveat. The published 116% is FOUR constructions out of
TWENTY-SIX, and the true width is 498%.** Every window, both (c) ends **[E4-38]**:

| window | (c) = capex | (c) = D&A |
|---|---|---|
| 1y (2025) | $1,558.0M | $1,553.0M |
| 2y (2024–25) | $1,362.5M | $1,351.5M |
| **3y (2023–25)** | **$1,005.0M** ← the published `oe_top` | $987.3M |
| 4y (2022–25) | $570.0M | $546.0M |
| **5y (2021–25)** | $486.8M | **$464.5M** ← the published `oe_bottom` |
| 6y (2020–25) | $428.4M | $405.1M |
| 7y (2019–25) | $346.5M | $329.5M |
| 8y (2018–25) | $288.9M | $274.1M |
| 9y (2017–25) | $250.0M | $236.4M |
| 10y (2016–25) | $221.7M | $210.4M |
| 11y (2015–25) | $200.8M | $191.3M |
| 12y (2014–25) | $181.9M | $174.5M |
| **13y (2013–25)** | **$167.6M** | $160.9M |

**Published range $465M–$1,005M, width 116%. True range $160.9M–$1,558.0M, width 868% —
or, restricting to the multi-year windows the corpus's five-year default admits,
$160.9M–$1,005.0M, width 525%.** This is the **thirteenth consecutive run** to find the
true width larger than the four-construction figure, and here it is larger by a factor of
between four and seven depending on where you stop. *(The range does **not** cross zero on
any full-window construction, unlike PINS — 2024 and 2025 are large enough to hold every
window positive. So a percentage IS definable here. It is just five to eight times the
published one.)*

**CORRECTION 2 — the cap.** Done above. **The queue's price was two trading days stale
(2026-09-01 $139.82 against 2026-09-04 $145.09, 3.8% low) and its share count was 11.7
YEARS stale and pre-IPO.** The staleness in the price is the smaller error by a factor of
eighty.

**CORRECTION 3(a) — separately-tagged capitalized software: NOT PRESENT. The HAS/CRWD
defect does not exist on this filer, and the recorded sweep says why.** Five vintages swept
for "capitaliz*": FY2025 (8 hits), FY2024 (8), FY2023 MD&A (1), FY2021 MD&A (2), FY2019
MD&A (8). The policy exists — *"The Company **may** capitalize certain development costs
incurred in connection with its internal use software"* — but **the investing section of
every filed cash-flow statement carries exactly ONE capital line, "Purchases of property and
equipment", and there is no `PaymentsToDevelopSoftware` tag in `companyfacts` at all**
(checked: absent). Total net property and equipment at 2025-12-31 is **$53M** and net
intangibles **$30M**, against $11,556M of revenue. **Capex is 0.22% of revenue.** There is
no hidden capital line because there is almost no capital.

**CORRECTION 3(b) — the raw D&A series, printed as required, and it HAS a discontinuity:**

| year | 2019 | 2020 | 2021 | **2022** | **2023** | **2024** | **2025** |
|---|---|---|---|---|---|---|---|
| **D&A $M** | 35.7 | 70.1 | 66.3 | **93.0** | **70.0** | **36.0** | **31.0** |
| of which depreciation | 16.8 | 38.2 | 41.8 | 36.0 | 28.0 | 22.0 | 18.0 |
| of which intangible amortization | 18.9 | 31.9 | 24.5 | **54.0** | 38.0 | 14.0 | 13.0 |

**A 3.0x step down from 2022 to 2025, and it is real and explained.** Two causes, both in
the filing: the **acquired-intangible amortization from the 2022 Deliverr acquisition ran
off** ($54M → $13M), and the **physical assets left with the logistics divestiture of May
2023** (depreciation $36M → $18M). **This is a perimeter event showing up in the D&A series,
which is exactly what the brief predicted, and it matters at Q4 because it makes the D&A end
of (c) fall by two thirds across the window — the two ends of the capex band are converging
on each other for a reason that has nothing to do with maintenance requirements.**

**A FOURTH DEFECT THE BRIEF DID NOT ASK FOR, AND IT IS THE ONE THAT WILL MATTER MOST AT
Q4.** The Q2 2026 10-Q carries this footnote to the cash-flow statement:

> *"**(1) Starting in April 2026, the cash flows associated with merchant cash advances are
> presented within investing cash flows on a basis consistent with loans**, given the similar
> nature of the underlying lending activities."*

**Shopify moved a recurring cash OUTFLOW out of operating cash flow and into investing, and
the comparative periods were NOT restated.** I checked: the Q2 2025 10-Q as originally filed
reports six-month 2025 operating cash flow of **$795M** and the Q2 2026 10-Q reports the
same **$795M** for the comparative — the prior-year number is unchanged, so the change is
**prospective only**. In FY2025 the line moved out was **"Merchant cash advances and related
receivables, net (141)"**, sitting *inside* operating cash flow. **Every future operating
cash flow figure is therefore larger than it would have been on the old basis, by whatever
the MCA book grows, and no restated history is provided to measure it against.** Recorded
here; treated at Q3 under the auditor's-eye test **[E4-34]** and at Q4 in the owner-earnings
construction.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**The brief said Q1 is not trivial here and must be done properly. It is right, and the
reason is that Shopify is two businesses in one income statement with gross margins forty
points apart, and the consolidated numbers hide which one is growing.**

### Unit economics, in my own words, without management's language

A person who wants to sell things on the internet needs a shop: a page that shows the
products, a basket, a checkout that takes a card, a way to print a shipping label, and a
back office that tracks what is left in the stockroom. Building that from scratch is weeks
of work and a permanent maintenance job. **Shopify rents it, for a monthly fee that scales
with the plan, and then takes a further slice of every sale that passes through it.** Those
are the two revenue lines and they are different businesses:

- **Subscription solutions — the rent.** A monthly fee for the storefront software, plus the
  point-of-sale upgrade, plus themes, apps and domain names. **$2,752M in FY2025.** This is a
  software subscription and it behaves like one.
- **Merchant solutions — the slice.** Overwhelmingly **Shopify Payments**, the card-processing
  business, plus currency conversion, plus shipping labels, plus **Shopify Capital**, which
  lends merchants money against their own future sales. **$8,804M in FY2025.** This is a take
  rate on volume, and much of it is payments.

**The physical quantity the whole thing rides on is GMV — the dollar value of goods sold
through Shopify's checkout. In FY2025 that was $378,441M**, and Shopify's revenue was
**3.05% of it**.

### THE FILED GROSS-PROFIT SPLIT — THE AMAT TEST, RUN, AND IT KILLS THE SIMPLE READING

**The brief said: get the filed split of revenue AND gross profit for each line across
vintages, because a product-line gross-profit split often kills a claim the consolidated
numbers supported. Shopify files it. Here is every year from FY2017, from the dimensioned
rows of the filed income statements.** *(Reconciles exactly: FY2025 $2,232M + $3,323M =
$5,555M = filed consolidated gross profit.)*

| | **SUBSCRIPTION** | | | **MERCHANT** | | | **merchant share of** | |
|---|---|---|---|---|---|---|---|---|
| year | rev $M | GP $M | **GM** | rev $M | GP $M | **GM** | **revenue** | **gross profit** |
| 2017 | 310.0 | 248.8 | **80.2%** | 363.3 | 131.5 | **36.2%** | 54.0% | 34.6% |
| 2018 | 465.0 | 364.0 | 78.3% | 608.2 | 232.3 | 38.2% | 56.7% | 39.0% |
| 2019 | 642.2 | 514.1 | 80.1% | 935.9 | 351.6 | 37.6% | 59.3% | 40.6% |
| 2020 | 908.8 | 715.2 | 78.7% | 2,020.7 | 826.3 | 40.9% | 69.0% | 53.6% |
| 2021 | 1,342.3 | 1,078.0 | 80.3% | 3,269.5 | 1,403.2 | **42.9%** | 70.9% | 56.6% |
| 2022 | 1,487.8 | 1,156.9 | 77.8% | 4,112.1 | 1,597.2 | 38.8% | 73.4% | 58.0% |
| 2023 | 1,837 | 1,483 | 80.7% | 5,223 | 2,032 | 38.9% | 74.0% | 57.8% |
| 2024 | 2,350 | 1,916 | **81.5%** | 6,530 | 2,556 | 39.1% | 73.5% | 57.2% |
| **2025** | **2,752** | **2,232** | **81.1%** | **8,804** | **3,323** | **37.7%** | **76.2%** | **59.8%** |
| **H1 2026** | **1,552** | **1,241** | **80.0%** | **5,201** | **2,013** | **38.7%** | **77.0%** | **61.9%** |

**Four things follow, and they are the whole of Q1's contribution to this run.**

1. **The high-margin business is the small one and it is getting smaller as a share.** The
   80%-gross-margin software subscription is **23.8% of revenue and 40.2% of gross profit**,
   down from 46.0% of revenue and 65.4% of gross profit in 2017. **Every point of mix shift
   for nine consecutive years has gone the same way.**
2. **The merchant-solutions gross margin has gone precisely nowhere in nine years.** 36.2% in
   2017, **37.7% in 2025** — and the 2025 figure is the **lowest since 2019**, below the 42.9%
   peak of 2021 by 5.2 points. Volume up 24x; margin flat.
3. **The subscription gross margin, by contrast, is a metronome:** between 77.8% and 81.5%
   for nine straight years, never once outside a 3.7-point band. **That half really is a
   software business.**
4. **The blended gross margin is falling and it is pure mix, not price.** 50.4% (2024) →
   **48.1%** (2025), with *both* component margins inside their normal ranges. **Anyone
   reading the consolidated 48.1% as margin compression is reading a mix shift. Anyone
   reading Shopify as an 80%-gross-margin software company is reading the 24% of it that is.**

### THE TAKE RATE, BUILT TWO WAYS — AND THE SECOND WAY IS THE HONEST ONE

**Take rate = merchant-solutions revenue ÷ GMV. Net take rate = merchant-solutions GROSS
PROFIT ÷ GMV**, which is what the shareholder actually keeps. GMV from the filed KPI tables
(FY2019 40-F ex.13, FY2021 40-F ex.13, FY2023 40-F ex.13, FY2024 and FY2025 10-K Item 7).

| year | GMV $M | GMV growth | **gross take rate** | **NET take rate** | net, change yoy |
|---|---|---|---|---|---|
| 2018 | 41,103 | — | 1.480% | 0.565% | — |
| 2019 | 61,138 | +48.7% | 1.531% | 0.575% | +1.0 bp |
| 2020 | 119,577 | **+95.6%** | 1.690% | 0.691% | **+11.6 bp** |
| 2021 | 175,362 | +46.7% | 1.865% | 0.800% | **+10.9 bp** |
| 2022 | 197,167 | +12.4% | 2.086% | 0.810% | +1.0 bp |
| 2023 | 235,910 | +19.7% | 2.214% | 0.861% | +5.1 bp |
| 2024 | 292,275 | +23.9% | 2.234% | 0.874% | **+1.3 bp** |
| **2025** | **378,441** | **+29.5%** | **2.326%** | **0.878%** | **+0.4 bp** |

**The gross take rate is still rising and the net take rate has stopped.** It added **23.5
basis points in the three years 2018–2021** and **6.8 basis points in the four years since**
— and **0.4 of a basis point in the most recent year, on 29.5% GMV growth.** The dollars are
growing beautifully; the rate at which Shopify converts a dollar of merchant sales into a
dollar of its own gross profit has been flat since 2023. **That is a Q2 fact and it is
adjudicated there, but it belongs in Q1 because it is how the money is actually made:
Shopify is now paid for volume, not for price.**

### WHAT DROVE THE TAKE RATE UP, AND WHY THAT LEVER IS RUNNING OUT

**One thing did nearly all of it: getting merchants to use Shopify's own card processor
instead of somebody else's.** From the FY2025 10-K:

> *"For the year ended December 31, 2025, the **Shopify Payments penetration rate was
> 65.6%**, resulting in GMV of **$248.1 billion** that was facilitated using Shopify
> Payments. This compares to a penetration rate of **61.9%**, resulting in GMV of $181.0
> billion … in the same period in 2024."*

**And the same filing publishes the number that says the lever is nearly exhausted —
adoption where the product is already available FELL in every single region in 2025:**

> *"As of December 31, 2025 Shopify Payments adoption among our merchants **where Shopify
> Payments is available** was as follows: **North America, 88%, APAC, 89% and EMEA, 83%**
> (December 31, 2024 — **North America, 91%, APAC, 90% and EMEA, 86%**)."*

**North America down 3 points, EMEA down 3 points, APAC down 1 point.** The headline
penetration rate rose only because Shopify launched Payments in more countries. **In the
markets where merchants have had the choice for years, a growing minority are choosing
somebody else's processor.** Recorded here as a fact about the mechanism; its meaning is a
Q2 question.

### THE THIRD BUSINESS NOBODY PUTS IN THE DESCRIPTION: SHOPIFY IS A LENDER

**This is the part of Q1 that the phrase "merchant solutions" conceals, and it decides the
owner-earnings construction at Q4.** From the filed balance sheet and cash-flow statement:

| | 2023 | 2024 | **2025** | **H1 2026** |
|---|---|---|---|---|
| **Loans and merchant cash advances, net** ($M, period end) | — | 1,224 | **1,784** | **2,184** |
| purchases and originations of loans ($M) | (1,861) | (3,006) | **(4,014)** | (2,933) |
| repayments and sales of loans ($M) | 1,338 | 2,542 | **3,435** | 2,460 |
| **net cash INTO the loan book** | **(523)** | **(464)** | **(579)** | **(473)** |
| **transaction and loan losses** (P&L) | 152 | 227 | **417** | 273 |
| *as % of revenue* | 2.2% | 2.6% | **3.6%** | 4.0% |

**Shopify originated $4,014M of loans in FY2025 — 35% of its revenue — and the loan book
grew $560M.** The cost of that business is a real expense line that **rose 84% in one year**,
to **$417M, or 3.6% of revenue**, and the 10-K attributes $124M of the increase to Shopify
Payments losses and **$61M to lending**. In the first half of 2026 it is running at **4.0% of
revenue**. **A payments-and-lending business is a credit business, and credit businesses are
read on exposure, not on experience [E4-40]:** *"focusing on experience, rather than
exposure."* This book has never been through a recession at this size.

### The scarce input this business controls

**Not the software.** Every competitor has a checkout. **Not the payments rails** — those
belong to the acquirers and the card networks. **Not the data centres** — Shopify has $53M of
net property and equipment against $11.6bn of revenue and rents its computing.

**The scarce thing is the merchant's live storefront, with its theme, its apps, its product
catalogue, its order history, its customer list and its checkout URL, all of which the
merchant built and none of which moves.** Migrating a working shop that is taking orders is
not a software project; it is a business interruption. **That is a real switching cost, it is
the single strongest asset in this file, and it belongs to the SUBSCRIPTION half — the 24% of
revenue and 40% of gross profit.** The 76% that is merchant solutions rides on it but is not
it: a merchant can stay on Shopify's storefront and move the card processing to a rival
tomorrow, and the filing above shows that in three regions a growing number are doing exactly
that.

### Will the fundamentals look broadly the same in ten years?

**The mechanism will.** Somebody will rent shopkeepers a shopfront and take a slice of the
till; that arrangement predates the internet by centuries and I expect it to outlive me.
**The split between rent and slice is the thing I cannot be sure about, and I record it here
rather than waving it through**, because **[E3-31]** requires the business to be *"relatively
simple and stable in character"* and this one has changed shape twice in five years — into
logistics in 2022 and out of it in 2023, and into lending throughout.

**But Q1 asks whether I can understand how the money is made, and I can, completely.** Two
revenue lines, both filed with their own cost of revenue; one physical volume metric (GMV)
published every quarter for eight years; one price metric (take rate) computable from the two
of them; one balance sheet with no debt; and a cash-flow statement whose every line I have
traced. **The complexity here is real but it is disclosed, and disclosed complexity is not
opacity.**

- **VERDICT: [x] IN**
  *Carried forward to Q2, not waived here: (a) the merchant-solutions gross margin has been
  flat at 36–43% for nine years and is at an eight-year low ex-2018; (b) the net take rate
  added 0.4 bp in the last year; (c) Shopify Payments adoption FELL in all three disclosed
  regions; (d) the switching cost lives in the 24% of revenue that is subscription, not the
  76% that is take rate. Those four facts are the Q2 case and they are decided there.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

- **Needed or desired [x]** — unambiguously. GMV through the platform grew from $41.1bn to
  $378.4bn in seven years and **accelerated in each of the last three** (+12.4% → +19.7% →
  +23.9% → +29.5%). Merchants are not being pushed; they are arriving.
- **No close substitute [ ] / [x] — SPLIT, AND THE SPLIT IS THE ANSWER.** The storefront has
  no close substitute for an installed merchant. **The payments business, which is 76% of the
  revenue, demonstrably does — and the filing names the substitutes' owners as Shopify's own
  suppliers.**
- **Not price-regulated [x]** — no regulation of Shopify's own prices. *(Card interchange is
  capped in the EU, UK and Australia, which constrains a cost and a revenue component inside
  merchant solutions. Recorded as a Q4 input risk, not an [E3-03](3) failure.)*

### **THE FACT THAT DECIDES THIS GATE, AND IT IS ONE RISK FACTOR IN SHOPIFY'S OWN 10-K**

> *"**We currently rely on two suppliers to provide the technology we offer through Shopify
> Payments.** At present, we have payment service provider agreements with **Stripe, Inc.**
> ("Stripe") and **PayPal, Inc.** ("PayPal") and their respective affiliates (together, our
> "Payment Service Providers"). Upon completion of the existing term, **the Stripe agreement
> automatically renews every 12 months, unless either party terminates the agreement
> earlier.** The PayPal agreement, following its initial term, **automatically renews every
> 12 months, unless either party terminates the agreement earlier.** … if our Payment Service
> Providers were to terminate their relationships with us before an alternative payment
> service provider was fully integrated, we could **incur substantial delays and expense**,
> and the quality and reliability of such alternative payment service provider **may not be
> comparable**."* — FY2025 10-K, Item 1A

**Read that against the Q1 arithmetic. Merchant solutions is $8,804M of revenue — 76.2% —
and $3,323M of gross profit — 59.8%, rising to 61.9% in the first half of 2026. The largest
part of it is Shopify Payments. And Shopify does not own Shopify Payments' technology: it
resells Stripe's and PayPal's, on contracts that roll over annually and that either side can
end.**

**That is a reseller margin, not a franchise.** The corpus's test is whether the *customer*
thinks there is no close substitute **[E3-03](2)**. Here the substitute is not merely close;
**it is the same product sold direct by the company that built it.** A Shopify merchant who
switches from Shopify Payments to Stripe changes processors without changing anything else
about the shop, and is often moving to the identical underlying rails.

**And the filing publishes the evidence that merchants are doing it:**

> *"As of December 31, 2025 Shopify Payments adoption among our merchants **where Shopify
> Payments is available** was as follows: North America, **88%**, APAC, **89%** and EMEA,
> **83%** (December 31, 2024 — North America, **91%**, APAC, **90%** and EMEA, **86%**)."*

**Down in all three regions in a single year, while the headline penetration rate rose from
61.9% to 65.6% on geographic expansion.** The headline says the moat is widening. The
component series says that in every market where merchants have had a real choice for years,
the share choosing Shopify's own processor **fell**.

### **[E2-44] — BOTH HALVES, RUN ON THE FILED SERIES, AND THEY SPLIT ALONG THE SAME SEAM**

*Can it raise prices "even when product demand is flat and capacity is not fully utilized",
and grow dollar volume "with only minor additional investment of capital"?*

**HALF ONE — PRICE. The subscription half passes and the merchant half fails, and both are
provable from the filings.**

*The subscription half:* Shopify raised subscription plan prices in **the second quarter of
2023** and the increase stuck — the FY2024 10-K attributes MRR growth in 2023 and 2024
directly to it. **That is a real price rise on a live customer base and it is the strongest
single piece of franchise evidence in the file.** But it is also the **only** one, and the
[E4-37] inverse metric reads the sequel:

| MRR at 31 Dec ($M) | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | **2025** |
|---|---|---|---|---|---|---|---|---|
| **filed** | 40.9 | 53.9 | 82.6 | 102.0 | 109 | 144 | 178 | **205** |
| **growth** | — | +31.8% | +53.3% | +23.5% | +6.9% | +32.1% | +23.6% | **+15.2%** |

**MRR growth has halved in two years, and the FY2025 10-K names the cause in its own
words:** *"In the year ended December 31, 2025, the MRR growth rate for the period was lower
than the same period in 2024 **driven by the impact of extending the length of paid
trials**."* **The subscription business's growth decelerated because the company lengthened
its discounts.** *"it's not a great business when you have to have a prayer session before you
raise your prices a penny"* **[E4-37]** — three years after the last increase, the lever
being pulled is a longer giveaway.

*The merchant half:* the **net take rate** — merchant gross profit ÷ GMV — added **0.4 basis
points in FY2025 on 29.5% GMV growth**, and 6.8 basis points in four years against 23.5 in
the three before that. **The merchant-solutions gross margin is 37.7%, against 36.2% in 2017
— 1.5 points of movement in nine years, and the current figure is the lowest since 2019.**
Demand is emphatically *not* flat, and the price still will not move. **That is [E2-44](1)
failing on the three quarters of the business.**

**HALF TWO — CAPITAL. Passes for the platform, and FAILS for the lender, which is the part
nobody counts.** Capex was **$26M on $11,556M of revenue — 0.22%**, and net property and
equipment is **$53M**. On the software, Shopify can double dollar volume without buying
anything. **But the lending business consumed $579M of net cash in FY2025 and $473M in the
first half of 2026 purely to grow its book**, and that is not "minor additional investment of
capital" — it is $1.05bn in eighteen months, forty times the capex. **It is invisible in the
capex line because it sits in investing, under "purchases and originations of loans".**

### **[E4-55] — WHERE UNITS EXIST, MONITOR UNITS. THEY EXISTED, SHOPIFY PUBLISHED THEM, AND THEN IT STOPPED.**

*"Precision Steel's pounds fell 69M → 46M while price rises held dollar revenue level … **Dollar
revenue flattered by pricing is how a shrinking franchise hides; the physical series is the
honest one.**"* — **[E4-55]**

**Shopify has two physical series. It publishes one and it withdrew the other.**

**Published, every year, never withdrawn: GMV.** $41.1bn → $378.4bn, growth accelerating.
**This is the strongest fact in the bull case and I am not discounting it.**

**Withdrawn: the number of merchants.** Recorded sweep of every MD&A vintage:

| filing | merchant count disclosed? | the sentence |
|---|---|---|
| FY2019 40-F, ex.13 | **YES** | *"The number of merchants on our platform has grown from approximately **820,000** as at December 31, 2018 to approximately **1,069,000** as at December 31, 2019."* |
| FY2020 40-F, ex.13 | **YES** | *"…from approximately 1,069,000 as at December 31, 2019 to approximately **1,749,000** as at December 31, 2020."* |
| FY2021 40-F, ex.13 | **NO** | — |
| FY2022 40-F, ex.13 | **NO** | — |
| FY2023 40-F, ex.13 | **NO** | — |
| FY2023 Annual Information Form | **NO** | — |
| FY2024 10-K | **NO** | — |
| **FY2025 10-K** | **NO** | — |
| **Q2 2026 10-Q** | **NO** | — |

**The merchant count was published for the two years it grew 30% and 64%, and has not
appeared in an SEC filing since the FY2020 40-F.** *(The count of merchants using Shopify
Payments where it is available is still given as a percentage; the absolute merchant count is
not.)*

**And this is not a metric the company stopped calculating. It is an input to a metric it
still publishes**, in its own words, unchanged from FY2019 through FY2024:

> *"**We calculate MRR at the end of each period by multiplying the number of merchants** who
> have subscription plans with us at the period end date **by the average monthly subscription
> plan fee**…"*

**Shopify counts its merchants every quarter, uses the number to compute a headline KPI, and
does not publish it.** Under **[E2-26]** — *"tell you the business facts that we would want to
know if our positions were reversed"* — the number of paying customers of a subscription
business is the first fact any owner would want. **It is the honest physical series and it is
the one that was withdrawn.**

### **[E2-49] — METRIC-SWITCHING. THE OPERATOR'S PRIOR HAD FAILED FOUR CONSECUTIVE TIMES. IT FIRES HERE, TWICE MORE.**

*"Yardsticks seldom are discarded while yielding favorable readings. But when results
deteriorate, most managers favor **disposition of the yardstick rather than disposition of the
manager**"* — demand *"pre-set, long-lived and small bullseyes"* — **[E2-49]**

**SECOND WITHDRAWAL — THE ATTACH RATE. INTRODUCED IN ONE ANNUAL FILING AND GONE FROM THE
NEXT.** Recorded sweep of every vintage for "attach rate": **0 mentions FY2019, 0 FY2020, 0
FY2021, 0 FY2022, NINE mentions FY2023, then 0 FY2024, 0 FY2025, 0 in the Q2 2026 10-Q.**

FY2023 40-F, Exhibit 13, verbatim:

> *"Key performance indicators … that we use to evaluate our business … **include MRR, Gross
> Merchandise Volume ("GMV") and Attach Rate.** … **Attach Rate is defined as total revenue
> divided by GMV** and is a key performance indicator of our business and our ability to
> generate greater value for our merchants."*
>
> | Years ended December 31, | 2023 | 2022 |
> |---|---|---|
> | Monthly Recurring Revenue | $149 | $110 |
> | Gross Merchandise Volume | $235,910 | $197,167 |
> | Revenue | $7,060 | $5,600 |
> | **Attach Rate** | **2.99%** | **2.84%** |

FY2024 10-K, Item 7, verbatim, one year later:

> *"Our key performance indicators … **are MRR and GMV.**"*

**The Attach Rate is not in the sentence and not in the table.** No explanation is given
anywhere in the FY2024 or FY2025 10-K; the recorded sweep returns zero mentions of the term
in either document. **And the reason it is worth withdrawing is computable from the two
series the company still publishes:**

| attach rate = total revenue ÷ GMV | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| **value** | 2.840% | **2.993%** | 3.038% | **3.054%** |
| **change** | — | **+15.3 bp** | +4.5 bp | **+1.6 bp** |

**It was introduced in the year it added 15 basis points and dropped in the year it added
4.5.** In the most recent year it added 1.6.

**AND A THIRD ITEM — MRR WAS RESTATED DOWNWARDS WHILE ITS DEFINITION TEXT STAYED WORD-FOR-WORD
IDENTICAL.** The FY2023 40-F reports MRR of **$149M (2023) and $110M (2022)**. The FY2024
10-K reports **$144M (2023) and $109M (2022)** — the same two years, **restated down 3.4% and
0.9%** — while GMV for those years is reproduced to the dollar ($235,910M and $197,167M,
unchanged). **The MRR definition paragraph is verbatim identical in both filings.** Then in
the FY2025 10-K the definition itself is rewritten, from *"multiplying the number of merchants
… by the average monthly subscription plan fee"* to *"**the aggregate value of all subscription
plans**"* — a formulation from which the merchant count has been removed.

**THE HONEST COUNTERWEIGHT, STATED BEFORE THE CONCLUSION [E5-38, E4-26].** *"the flag reads
the accounting, the binary [E5-16] judges the person on conduct, and the two tests stay
distinct."* **There is an innocent explanation available for two of these three and I will
give it its full weight: Shopify changed reporting regimes between the FY2023 and FY2024
filings**, from a Canadian-form MD&A filed as Exhibit 13 to a 40-F, to a US Item 7 MD&A inside
a 10-K. Different form, different drafters, different disclosure requirements. **That
explanation covers the Attach Rate and it plausibly covers the MRR restatement** (a
recalculation done during the conversion).

**It does not cover the merchant count.** That was dropped after the **FY2020** 40-F —
**three years and three filings before the form changed**, from the same document type, in the
same format, prepared under the same rules. **[E2-49]**'s operational form is *"a switch that
follows deterioration fires; one announced ahead with reasons is the candor case."* No reason
was announced, ahead or since. **The flag fires, and it fires as a prompt to read, which is
what the rest of this gate has done.**

### **[E3-03](2) AGAIN, ON THE BALANCE SHEET: THERE IS NO CONTRACT**

> *"Our merchants **typically enter into monthly subscription agreements.** … We do not
> consider this deferred revenue balance to be a good indicator of future revenue."*
> — FY2025 10-K, Item 7

**Deferred revenue is $398M against $11,556M of revenue — 3.4%** — and $300M of it is
current. **There is no minimum commitment, no term, and nothing to break.** *(For the
project's own scale: the CRWD run measured CrowdStrike at 99% of revenue; the PINS run
measured Pinterest at 1.1%. Shopify at 3.4% is much closer to Pinterest.)*

**But — and this is where Shopify is genuinely different from Pinterest — the lock-in here is
not contractual and never was.** It is that the merchant's shop is *running on the thing*.
An advertiser leaves Pinterest by changing a number in a dashboard; a merchant leaves Shopify
by rebuilding a storefront, re-installing apps, migrating a product catalogue and an order
history, and risking a checkout outage on a live business. **That is a real moat, it does not
appear anywhere in the deferred-revenue line, and it is the reason this gate does not close
the way Pinterest's did.**

### THE COMPETITOR ROW — required **[E3-28]**

*Full working, every accession number, every recorded sweep and every stated limit:*
`Test Runs/_research 2026-09-07 SHOP/COMPETITOR_ROW.md`.

**Peers taken: EIGHT with filed data, across both legs of the business. THREE hard limits are
named rather than papered over.**

| FY2025 unless stated | **SHOP** | BIGC | WIX | AMZN | ADBE | PYPL | XYZ *(Block)* | ETSY | *SQSP* |
|---|---|---|---|---|---|---|---|---|---|
| revenue $M | **11,556** | 342 | 1,993 | 716,924 | 23,769 | 33,172 | 24,194 | 2,884 | *1,012 (FY23)* |
| revenue growth | **+30.1%** | +2.8% | +13.2% | +12.4% | +10.5% | +4.3% | +0.3%¹ | +2.7% | *+16.8%* |
| **gross margin** | **48.1%** | **78.7%** | 68.1% | n/a² | 89% | 46.6%³ | 42.8% | 71.6% | *79.5%* |
| **GAAP operating margin** | **12.7%** | **(4.7)%** | **0.09%** | 11.2% | **36.6%** | 18.3% | 7.1% | 9.2% | *8.3%* |
| **SBC ÷ operating cash flow** | **22.1%** | **92.5%** | 40.7% | **14.0%** | 19.4% | 15.6% | 47.1% | 35.3% | *46.6%* |
| **capex ÷ revenue** | **0.22%** | 2.51% | 0.50% | **18.39%** | 0.75% | 2.57% | 0.64% | 1.90% | *1.68%* |
| **owner earnings (OCF−SBC−capex)** | **$1,558M** | **$(6.7)M** | $336M | **$(11,772)M** | $7,910M | $4,562M | $1,209M | $394M | *$106M* |
| net cash (debt) | **+$5,472M**⁴ | $(14)M | +$535M | +$54,633M | +$385M | +$4,765M | $(18)M | $(579)M | *$(311)M* |
| **names Shopify in its own filing?** | — | **NO** | **YES** | **NO** | **NO** | **NO** | **NO** | **NO** | *YES (FY23)* |

¹ Block's +0.3% is a bitcoin pass-through artifact; ex-bitcoin revenue rose 14.0%.
² Amazon files no gross-profit line and its cost of sales excludes fulfilment — not comparable, stated and not carried.
³ PayPal files no gross-profit line; this is net revenue less transaction expense less transaction and credit losses, **DERIVED and labelled**.
⁴ Shopify at 2026-06-30: cash $1,656M + marketable securities $3,291M + long-term investments $525M, **zero debt**.

**THE THREE HARD LIMITS, NAMED [E3-28]:**
- **Stripe — NOT an SEC registrant, private, no filings.** And it is not merely a peer:
  **it is Shopify's supplier.** There is no rung of the evidence ladder that reaches it.
- **Adyen — NOT an SEC registrant** (Euronext Amsterdam). Ladder rung 4 (exchange filings /
  issuer IR) exists and was not pulled in this run. **Named as a limit.** The take-rate
  question does not rest on it: two disclosing comparators (PayPal, Block) answer it below,
  and a third (Etsy) contradicts them, which is a better test than a fourth agreeing.
- **Squarespace — DEREGISTERED.** Form 25-NSE `0000876661-24-001010` (2024-10-17) and Form
  15-12G `0001140361-24-044947` (2024-11-01), holders of record: **one**, following the
  Permira take-private. **Last filed year is FY2023** and every Squarespace figure above is
  italicised and two years stale.

### **THE LOAD-BEARING COMPARATOR FACT: THE TWO INCUMBENTS THAT DISCLOSE A TAKE RATE HAVE NOT HELD IT, AND THEY NAME THE SAME MECHANISM SHOPIFY'S OWN MD&A DESCRIBES**

**PayPal — revenue ÷ total payment volume, five years, filed:**

| FY | transaction revenue $M | TPV $bn (as filed) | **transaction take rate** |
|---|---|---|---|
| 2020 | 19,918 | 936 | **2.128%** |
| 2021 | 23,402 | 1,250 | 1.872% |
| 2022 | 25,206 | 1,360 | 1.853% |
| 2023 | 26,857 | 1,530 | 1.755% |
| 2024 | 28,842 | 1,680 | 1.717% |
| **2025** | **29,798** | **1,790** | **1.665%** |

**Down 46.3 basis points in five years — 21.8% of the 2020 rate — with no year of increase.**

**Block / Square — transaction-based revenue ÷ gross payment volume, filed:**

| FY | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| **blended take rate** | **2.934%** | 2.858% | 2.801% | 2.773% | **2.746%** | **line retired** |
| Square-segment take rate | — | — | 2.807% | 2.775% | **2.746%** | **not computable** |

**Down every single year for four years — and then, in the FY2025 10-K, Block retired the
"transaction-based revenue" line entirely and replaced it with categories from which no take
rate can be derived.** *(That is a second, independent instance of [E2-49] in this row, on a
different company, in the same quarter.)*

**AND THE MECHANISM IS THE ONE SHOPIFY DISCLOSES ABOUT ITSELF.** PayPal's FY2025 10-K:
*"Transaction revenues growth was lower than the growth in TPV in 2025 due primarily to
changes in **product mix, merchant mix**…"* — larger merchants negotiate the rate down.
Shopify's FY2025 10-K, Item 1: *"While most merchants subscribe to our Basic and Grow plans,
**the majority of our gross merchandise volume has been generated from merchants subscribing
to our Shopify Plus plan and enterprise offerings**."* **Shopify's volume is concentrating in
exactly the customer class that compressed PayPal's and Block's rates.**

**THE COUNTEREXAMPLE, RECORDED AT FULL STRENGTH [E4-26]. Etsy's take rate ROSE**, from 22.3%
to **24.2%**, +190bp, published as a filed metric. **But read the mechanism: Etsy's GMS
*fell 5.3%* while revenue rose 2.7%.** The rate rose because the denominator shrank and Etsy
raised seller fees against a captive base. **Etsy is a marketplace — it owns the demand.
Shopify is a platform — the merchant owns the demand and brings it.** A marketplace can rake
harder; a platform whose merchant can move the checkout in an afternoon cannot. **The
counterexample is real and it is a different business model, and both halves belong in the
row.**

### **THE ROW'S OTHER FOUR READINGS, AND TWO OF THEM ARE STRONGLY IN SHOPIFY'S FAVOUR**

1. **THE SAME TWO-LINE SPLIT EXISTS AT WIX, AND IT CONFIRMS THE Q1 FINDING INDEPENDENTLY.**
   Wix files Creative Subscriptions at an **83.2% gross margin** and Business Solutions —
   its payments leg — at **31.6%**. **Two unrelated companies, same architecture, same
   forty-point gap.** The difference is the mix: Business Solutions is **29.3% of Wix's
   revenue; merchant solutions is 76.2% of Shopify's.** Shopify has taken the
   thin-margin half much further than its closest structural peer.
2. **SHOPIFY IS THE BEST OPERATOR ON THE STOREFRONT LEG BY A DISTANCE, AND THIS IS THE
   STRONGEST FACT IN ITS FAVOUR ANYWHERE IN THIS RUN.** On GAAP operating margin: Shopify
   **12.7%**, Wix **0.09%**, BigCommerce **(4.7)%**, Squarespace 8.3% in its last filed year.
   On owner earnings: Shopify **$1,558M**, Wix $336M, **BigCommerce NEGATIVE $6.7M**. On
   SBC/OCF: Shopify **22.1%**, Wix 40.7%, **BigCommerce 92.5%**. **Every pure-play storefront
   competitor is either barely profitable or unprofitable on GAAP, and Shopify earns more
   owner earnings than the other three combined, several times over.**
3. **SBC IS NOT THE DECIDING NUMBER HERE, AND THE BRIEF'S PRIOR IS REFUTED.** The brief
   expected SBC to close the file as it did at CRWD (68.0%) or clear it as at QLYS (24.9%).
   **Shopify is at 22.1% — lower than QLYS, and second-lowest of the nine names in this row,
   behind only Amazon at 14.0%.** Its own series: 58.1% (2020), 61.8% (2021), n/m (2022,
   negative OCF), 65.1% (2023), **26.6% (2024), 22.1% (2025), 22.8% (H1 2026)**. Cross-checked
   to the dollar against the filed cash-flow statements. **SBC fell in absolute dollars from
   $615M to $430M to $449M while revenue rose 64%.** This is a genuinely good number and it
   is not the reason this file is difficult.
4. **NOBODY NAMES SHOPIFY, AND THE ONE THAT DOES CALLS IT A POINT PRODUCT.** Recorded
   case-sensitive sweeps of full filed documents: BigCommerce 0 hits (419,080 chars), Amazon
   0 (312,331), Adobe 0 (371,127), PayPal 0 (535,722), Block **0 hits in five consecutive
   10-Ks** (2021–2025), Etsy 0 (443,244). **Wix is the only current filer that names
   Shopify**, and it does so dismissively: *"offerings that provide e-commerce software
   enabling a merchant to sell goods online such as **Shopify and BigCommerce**"* — listed as
   a **"point product"** overlapping *"parts of our solution."* **Shopify names nobody
   either**: its own FY2025 Item 1 "Competition" section lists competitive factors and
   generic categories and **contains not one company name**. *(It used to. The FY2023 Annual
   Information Form named Amazon, Salesforce, eBay, Walmart, Google, Microsoft, Oracle, TikTok
   and Meta. That named list did not survive the move from 40-F to 10-K. Recorded, with the
   innocent form-change explanation given its weight.)*

**AND THE SCALE FACT NOBODY SHOULD BE ALLOWED TO SKIP.** Amazon's **"Third-party seller
services"** line alone — commissions and related fulfilment fees, the closest filed analogue
to Shopify's merchant solutions — was **$172,162M in FY2025, growing 10.3%.** **That single
line is 14.9x Shopify's entire company**, and it is funded by AWS.

### **[E3-46] / [E2-43] — RETURNS ON CAPITAL, ON THE RIGHT DENOMINATOR**

*"the best businesses, by definition, are going to be businesses that earn very high returns
on capital employed over time"* **[E3-46]**, on *"unleveraged net tangible assets"* **[E2-43]**.

Total assets $15,189M **less** goodwill $491M and intangibles $30M, **less** cash $1,545M,
marketable securities $4,233M, long-term investments $975M, equity and other investments
$4,582M, equity-method investment $602M and deferred tax assets $33M = **$2,698M** of tangible
operating assets; **less** accounts payable and accrued liabilities $1,075M, deferred revenue
$398M, lease liabilities $188M and deferred tax liabilities $55M = **$982M of unleveraged net
tangible operating assets**, against **$1,468M of operating income**.

**149.5% pre-tax. And the composition is the finding: $1,784M of the $2,698M — 66% — is the
LOAN BOOK.** Strip the lender out and the platform runs on **negative $802M** of net tangible
operating capital: its customers and suppliers fund it. **The software business is close to
capital-free, and the lending business is where all the capital is going.**

### **[E3-33] / [E5-28] — UNTAPPED PRICING POWER? THE CLASS IS CLAIMED AND REFUSED.**

**[E3-33]** describes businesses where *"any manager could raise the return enormously just by
raising prices, and yet they haven't done it."* Shopify has a superficial claim: it takes
3.05% of $378bn of commerce and Etsy takes 24.2% of its own. **[E5-28] scopes the class and
disqualifies it:** *"If you name some business that has incredible pricing power, you're
talking about a business that's **a monopoly or a near monopoly**"* — **and claiming the class
is claiming near-monopoly, which the competitor row must then support.** It does not.
Shopify's GMV is **$378bn against Amazon's third-party seller volume alone**, and the price of
the thing it actually charges for — payment processing — is set by Stripe, Adyen, PayPal and
the card networks, **two of whom Shopify buys from under twelve-month contracts.** Etsy can
rake 24% because a seller who leaves Etsy loses the buyers; a merchant who leaves Shopify
Payments keeps every one of them. **The class is refused.**

### **[E4-04] AND [E4-36] — MUST THE MOAT BE REBUILT, AND WHICH CAUSE IS THIS?**

*Does a lapse in spending destroy the structure, or merely narrow it — and does the spending
defend the same advantage, or buy its replacement?* **R&D was $1,536M, 13.3% of revenue, down
from 24.5% in FY2023** — a large fall, and the storefront would keep running for years without
it. **A lapse narrows rather than destroys, which is the moat side of [E4-04].** But the
company has twice spent to buy a *replacement* rather than defend the same advantage: it
bought Deliverr for $2.1bn in 2022 to enter logistics and **wrote it off at $1,340M and sold
it in 2023**. That is [E4-04]'s excluded shape, executed once, at scale, within the window.

**[E4-36]'s four causes: this is mostly wave-riding [E3-51]**, and the wave is the migration
of retail to online. *"when a surfer gets up and catches the wave and just stays there, he can
go a long, long time."* **But not entirely** — the merchant storefront switching cost is an
ownable asset that does not live in the wave, and it is why this gate does not close.

### **VERDICT — Q2 IS THE CLOSEST CALL IN THIS FILE AND IT GOES IN, NARROWLY. HERE IS BOTH SIDES AT FULL STRENGTH FIRST [E4-51].**

*"I'm not entitled to have an opinion unless I can **state the arguments against my position
better than the people who are in opposition**."* **[E4-51]**

**THE CASE FOR OUT, put as well as I can put it.** Three quarters of Shopify's revenue and
three fifths of its gross profit is a **reseller margin on Stripe's and PayPal's technology,
under contracts that auto-renew every twelve months and that either party may terminate.**
That half's gross margin has moved 1.5 points in nine years and is at an eight-year low. Its
net take rate added **0.4 basis points** last year on 29.5% volume growth. Adoption of the
product among Shopify's own merchants **fell in all three disclosed regions**. The two
comparators that publish a take rate on the same mechanic have **lost it in every year for
four and five years respectively**, and both name **merchant mix** as the cause — the mix
Shopify's own filing says it is moving into. The subscription half's growth has **halved in
two years** and the company's stated reason is **longer discounts**. And across the same
period Shopify **withdrew the merchant count (after FY2020), withdrew the Attach Rate (after
FY2023) and restated MRR downward while leaving its definition text word-for-word
unchanged** — three disclosure reductions, all on the metrics that measure the moat.

**THE CASE FOR IN, and why it carries.**

1. **The switching cost is real, it is not contractual, and it is demonstrated by a price
   increase that stuck.** Shopify raised subscription prices in Q2 2023 and the FY2024 10-K
   attributes two years of MRR growth to it. A business with no moat cannot do that.
2. **The subscription gross margin has sat between 77.8% and 81.5% for nine consecutive
   years** through a pandemic, a bust, a 20% workforce cut and a divestiture. That is what a
   protected price looks like.
3. **The competitor row is not close on the storefront leg.** Every pure-play rival is at or
   below breakeven on GAAP operating margin — **Wix 0.09%, BigCommerce (4.7)%** — while
   Shopify earns 12.7% and **$1,558M of owner earnings against Wix's $336M and BigCommerce's
   negative $6.7M.** Squarespace was taken private. **This industry has one profitable
   independent participant and it is the subject.**
4. **The merchant-solutions attach is not an independent commodity business — it is the
   monetization of the franchise.** Shopify Payments is the default inside the merchant's own
   admin panel, and 65.6% of GMV runs through it. The take rate rose **57% in seven years**
   because the franchise pulled it up.
5. **149.5% pre-tax on unleveraged net tangible operating assets, capex at 0.22% of revenue,
   and SBC at 22.1% of operating cash flow** — second-lowest in a nine-name row.

- **Untapped pricing power [E3-33] / [E5-28]?** **No — refused on [E5-28]'s own scope.**
- **Class: [x] NARROW.** **Scoped explicitly: the franchise covers the storefront platform —
  23.8% of revenue and 40.2% of gross profit. The 76.2% that is merchant solutions is not a
  franchise on [E3-03](2) and is carried as a monetization of the franchise, not as one.**
- **Direction [E4-32]: FLAT TO NEGATIVE, and this is the reservation carried to Q6.**
  *"the moat widened every year is the primary criterion of a great business."* Here the
  franchise half has shrunk as a share of gross profit in **nine consecutive years** (65.4% →
  40.2%), the net take rate added 0.4bp, and Payments adoption fell in every disclosed region.
- **VERDICT: [x] IN — NARROW.** *No caveat of "unverified" or "provisional" attaches: the
  moat class is not PROVISIONAL, because the finding rests on Shopify's own filed
  gross-profit split, its own take-rate series, its own Payments-adoption disclosure and its
  own supplier risk factor, none of which needs a peer filing. The two non-registrant limits
  are named above and neither is load-bearing.*

**WHAT WOULD FLIP THIS TO OUT, named in advance so the verdict is falsifiable [E1-02]:**
**(a)** merchant-solutions **gross margin below 36%** in a filed fiscal year — the level at
which the take-rate half is earning less than it did in 2017; **or (b)** Shopify Payments
adoption where available **below 85% in North America**, which would be a fourth consecutive
annual decline; **or (c)** the **net take rate falling** in any filed year; **or (d)** a
subscription gross margin **below 77%**, breaking a nine-year band. Any one is a filed number
in a document I can name.

---
### **Q2 ADDENDUM — THREE MORE COMPARATORS ARRIVED AFTER THE ROW ABOVE WAS WRITTEN. THE VERDICT DOES NOT MOVE; TWO OF THE FINDINGS DO.**

*Appended rather than folded into the table above, so the reading order stays honest. Full
working in the same research file.*

**1. ADYEN — obtained after all, from the ISSUING COMPANY (ladder rung 4), and it makes THREE
processors, not two.** Adyen is not an SEC registrant (its only EDGAR presence is CIK 1788707,
an ADR depositary shell with nine F-6EF filings and nothing else). The figures below come from
Adyen's own audited ESEF/iXBRL annual report and its half-yearly workbooks, **which state on
their face that they are unaudited. Rung flagged; EUR not converted.**

| Adyen, net revenue ÷ processed volume | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| **take rate, basis points** | **22.54** | — | — | — | **15.52** | 16.96 |

**Down 31.1% over four years — the same direction as PayPal and Block.** The FY2025 rebound is
**not** pricing power and must not be read as one: **point-of-sale went from 18.1% to 22.3% of
volume while DIGITAL volume FELL 5.0%.** It is mix. **Adyen's own economics are otherwise the
best in the row — 46.9% operating margin and SBC at 4.1% of operating cash flow — which makes
the take-rate decline harder to dismiss, not easier: the most profitable operator in payments
could not hold its rate either.**

**2. GLOBAL PAYMENTS — AND IT IS THE MOST IMPORTANT SINGLE SENTENCE IN THE ENTIRE COMPETITOR
ROW.** GPN (FY2025, revenue $7,705.9M, operating margin 22.8%) is the **only current SEC filer
that names Shopify in a competitive context on the PAYMENTS leg**, and of the class it puts
Shopify in:

> *"In the United States, we compete with… **Fiserv, Inc., Chase Paymentech, Elavon, … Toast,
> Inc., Stripe, Inc., Shopify Inc. and Block Inc.**"*

**Global Payments classifies Shopify as a MERCHANT ACQUIRER — one of ten — not as software.**
**This corrects a reading in the row above.** I wrote there that only Wix names Shopify and
does so dismissively as a *"point product"*. **Both of the current filers that name Shopify
name it as something OTHER than a commerce platform: Wix as a point product, and Global
Payments as a payment processor alongside Fiserv, Elavon, Stripe and Block.** Neither treats it
as a category-defining franchise, and the payments industry's own filed view of Shopify is that
**it is a competitor in the commodity half of its business, not in the franchise half.**

**AND IT MAKES THE ZEROES READABLE, WHICH IS WHAT A CONTROL CASE IS FOR.** The row above
recorded 0 hits for Shopify at BigCommerce, Adobe, Amazon, Etsy, PayPal and Block (five
consecutive 10-Ks). **PayPal, Block, Amazon and Adyen name ZERO competitors by name at all —
that is house style, not a verdict, and I would have over-read those zeroes.** Global Payments
names ten. **The one filer in the row that does name names, names Shopify.**

**3. THE MARGIN CONVERGENCE, WITH THE THIRD AND FOURTH DATA POINTS IN.** Shopify **48.1%** ·
Block's Square segment **46.6%** · PayPal's derived transaction margin **46.6%**. Against the
non-payments comparators: BigCommerce **78.7%**, Adobe **89%**, Wix's Creative Subscriptions
leg **83.2%** — and **Wix's payments leg at 31.6%**. **Shopify's blended gross margin has
converged on the payment processors', not on the software companies', and it got there by
mix.**

**NET EFFECT ON THE Q2 VERDICT: NONE. It remains IN — NARROW.** The addendum strengthens the
bear half of a verdict that was already narrow, and it does not touch the four facts the IN
rests on (the 2023 price increase that stuck, the nine-year 77.8–81.5% subscription gross
margin, the profitability gap over every pure-play storefront rival, and 149.5% on unleveraged
net tangible operating assets). **The falsifiers named above are unchanged.**

**AND ONE HARD LIMIT IS NOW PERMANENT AND STATED AS SUCH: STRIPE.** EDGAR company search
returns *"No matching companies"*; there is no ticker-map entry and no filed number of any
kind. **Shopify's largest payments supplier — the company whose technology carries the
majority of Shopify's gross profit — cannot be measured from any document on the evidence
ladder.** That is recorded as a permanent limit on this row, not as a task.

---

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

### **STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**

*How much damage can this manager do before I can react?*

- [ ] **Daily execution [E3-38, E2-70]** — **NOT TICKED, but the exception is named and sized.**
  The 1977 root is *"their only products are promises"* — an undifferentiated product that
  magnifies the manager. Shopify's core product is the opposite: installed software running a
  live shop, differentiated by the merchant's own configuration, with a switching cost. **But
  one part of Shopify IS a promises business: Shopify Capital.** It originated **$4,014M** in
  FY2025 and carries a **$2,184M** book at 2026-06-30. That is underwriting, and underwriting
  is a have-to-be-smart-every-day job. **It is sized rather than ticked: $2,184M against
  $12,684M of shareholders' equity is 17.2%. A total loss of the book would be severe and
  survivable.** Recorded as the one live daily-execution exposure, monitored at Q6.
- [ ] **Control [E1-16]** — **NOT TICKED.** A minority position in a NASDAQ- and TSX-listed
  company, exitable in a day.
- [ ] **Leverage [E3-29]** — **NOT TICKED.** **Zero debt.** The $913M of convertible senior
  notes matured and were repaid in cash in Q4 2025 (financing outflow of $1,043M). At
  2026-06-30 the balance sheet carries $1,656M of cash, $3,291M of marketable securities and
  $525M of long-term investments against **no borrowings of any kind.**

**CASE DECLARED: Q3 IS A QUALITATIVE OVERLAY, not a binary gate.** No price is ruled out as a
remedy. **And per the guardrail, nothing in this section can promote the name** — a strong
Q3 cannot repair Q2's narrow class or substitute for Q4 **[E2-37, E2-38, E3-39]**.

### **HONESTY — binary, permanent, filings-based [E5-16]**

**Recorded sweep of the FY2025 10-K and the Q2 2026 10-Q for litigation, regulatory and
conduct matters. Nothing found.** The Commitments and Contingencies note reads, verbatim:

> *"**The Company currently has no material pending litigation or claims.** The Company is not
> aware of any litigation matters or loss contingencies that would be expected to have a
> material adverse effect on the business…"*

The one substantive matter in the file resolved **in Shopify's favour and is disclosed with
its full history**: an Express Mobile patent verdict in Delaware, a $55M liability recorded in
2022, the verdict vacated on post-trial motion in 2024 and the liability reversed through
G&A, and the appeal dismissed in 2025. **Disclosed at every stage including the reversal**,
which is the [E2-26] standard being met on a matter the company could have quietly dropped.

**Written as [E5-17] requires: this is the ABSENCE OF FOUND DISQUALIFIERS, not a finding that
the managers are honest.** *"Sincerity and empathy can easily be faked"*, and *"the filed
statement itself is not bedrock"* **[E5-32]**.

### **STEP 2 — THE FLAGS. Each is a prompt to READ, never a verdict [E4-22, E5-15, E5-36].**

- [ ] **weak accounting** — no comp games (SBC fully expensed), no pension assumptions (no
  defined-benefit plan), PwC unqualified. **BUT ONE ITEM FIRES AS A PROMPT and it is the
  cash-flow reclassification found at Step 0:** *"Starting in April 2026, the cash flows
  associated with merchant cash advances are presented **within investing cash flows**…"* —
  **applied prospectively, comparatives NOT restated.** Verified: the Q2 2025 10-Q as
  originally filed and the Q2 2026 10-Q both report six-month 2025 operating cash flow of
  $795M, so the prior year was left on the old basis. **In FY2025 the line moved out was
  $(141)M inside operating cash flow.** The effect is to raise reported operating cash flow
  by whatever the merchant-cash-advance book grows, with no restated history to measure it
  against. **This is [E4-34]'s fourth auditor question in its cash-flow form** — an action
  whose effect is to move a cash flow from one statement caption to another — and it is
  handled at Q4 by building owner earnings on a basis that is indifferent to it.
- [ ] **unintelligible footnotes** — **NO. The reverse.** The logistics disposal is
  disclosed with every component: goodwill $(1,438)M, intangibles $(337)M, net assets and
  transaction costs $(93)M, non-cash consideration received $528M, impairment $(1,340)M.
  **That is a management quantifying its own worst decision line by line**, which is the
  [E2-26] half-owner test passed on the least convenient fact in the file.
- [x] **TRUMPETED EARNINGS PROJECTIONS / GROWTH TARGETS — FIRES. [E4-22, E5-30, E3-48]**
  Shopify issues **quarterly guidance on five separate metrics.** Q4 2025 earnings release,
  verbatim: *"For the first quarter of 2026, we expect: • Revenue to grow at a **low-thirties
  percentage rate**…; • Gross profit dollars to grow at a **high-twenties percentage rate**…;
  • Operating expenses as a percentage of revenue to be **37% to 38%**; • **Stock-based
  compensation to be $140 million**; and • **Free cash flow margin to be in the low-to-mid
  teens**."* **[E5-30]:** *"once you start it, it's all over. You can't quit… And forecasting
  earnings, I can't imagine anything more destructive."*
  **[E3-48]'s action — pull the guidance and set it against the outturn.** Q1 2026 guided
  "low-thirties" revenue growth; **actual +34.3%** (Q1 2026 revenue $3,170M against $2,360M,
  derived from the filed six-month and three-month columns). SBC guided $140M; **actual
  $132M.** **The guidance was met or beaten on both testable items.** *"about nine cases out
  of ten"* of projections exist to justify a decided course **[E3-48]** — that base rate is
  not what this record shows, and the flag is recorded as a **cultural ratchet**, not as
  evidence of manipulation.
- [ ] **serial share issuance [E5-15] — DOES NOT FIRE, and the record is good.** Weighted
  diluted shares: 1,295.5M (2023) → 1,301.5M (2024) → 1,305.0M (2025) — **0.7% a year** — and
  the count has **fallen** to 1,289.2M at 2026-06-30. No secondary offering since the 2020
  equity raise. **This is the opposite of the [E5-15] pattern.**
- [ ] **EBITDA / adjusted-earnings promotion [E4-29] — DOES NOT FIRE, AND THE RECORDED SWEEP
  IS EMPHATIC. "EBITDA" appears ZERO times in the FY2025 10-K, ZERO times in the Q4 2025
  earnings release and ZERO times in the Q2 2026 earnings release.** For a company of this
  profile that is genuinely unusual and it is to management's credit.
  **BUT THE SAME SPECIES OF DELETION IS PRESENT UNDER A DIFFERENT NAME, AND IT IS THE
  HEADLINE MEASURE.** *"Free cash flow"* appears **21 times** in the Q4 2025 release and
  **17 times** in the Q2 2026 release; it is guided quarterly; and Shopify defines it as
  **operating cash flow less capital expenditures**. **It therefore deducts $26M of capex and
  none of the $449M of share-based compensation.** FY2025: Shopify's free cash flow is
  **$2,007M**; owner earnings on this framework's construction are **$1,558M**. **The
  company's headline cash measure overstates what an owner can take out by 28.8%**, and the
  gap is entirely one expense. **[E5-06]:** *"To say 'stock-based compensation' is not an
  expense is even more cavalier."* Recorded as the [E4-29] mechanism in a different costume;
  it is not EBITDA and I will not call it EBITDA.
- [ ] **filed-figure tells [E4-30] — NEITHER FIRES.**
  *Unnaturally smooth reported growth:* **no.** Net income reads +$2,915M (2021), **−$3,460M
  (2022)**, +$132M (2023), +$2,019M (2024), +$1,231M (2025). Nobody engineering smoothness
  files a $3.5 billion loss.
  *Cash taxes falling as a share of reported pretax income:* **no — RISING.** Cash paid for
  income taxes, net (filed supplemental line): **$50M (2023) · $116M (2024) · $194M (2025)**,
  against operating income of $(1,418)M · $1,075M · $1,468M — **10.8% → 13.2% of operating
  income**, and 5.2% → 12.9% of pretax income. The tell looks for the opposite direction.
- [x] **METRIC-SWITCHING [E2-49] — FIRES, THREE TIMES. Fully worked at Q2 and not repeated
  here:** the **merchant count** withdrawn after FY2020 (three filings before the form
  change, so the form change does not explain it); the **Attach Rate** introduced in the
  FY2023 40-F and gone from the FY2024 10-K; **MRR restated down 3.4% for FY2023 and 0.9% for
  FY2022 while its definition paragraph stayed word-for-word identical**, and then the
  definition itself rewritten in FY2025 to remove the merchant count from the formula.
- [ ] **dividends funded by issuance [E2-52]** — N/A. *"The Company has not paid and does not
  anticipate paying any cash dividends in the foreseeable future."*
- [ ] **stock-price targeting [E3-50]** — no instance found in the recorded sweep of the
  FY2025 10-K, the 10-K/A or the two earnings releases.
- [ ] **the restructuring charge [E3-53, E5-33]** — **present, and handled the RIGHT way.**
  May 2023: headcount cut by **approximately 23%**, **$148M** of severance, itemised across
  S&M ($28M), R&D ($102M) and G&A ($18M); and the **$1,340M logistics impairment run through
  OPERATING EXPENSES**, not below the line. **[E5-33]** says these are real costs and belong
  in the owner-earnings mean; **Shopify put them there itself.** They are inside the FY2023
  figures used at Q4 and are not added back anywhere in this run.

**[E4-52] — DO THE FLAGS CONVERGE?** Two fire: guidance culture, and metric withdrawal. **They
point in the same direction** — a management that manages the reported narrative — and the
lollapalooza test asks whether they are one reinforcing system. **My read: they are adjacent,
not confluent.** The metric withdrawals removed *historic* series; the guidance concerns
*future* quarters and has been met. There is no third element (no accounting aggression, no
issuance, no EBITDA, rising cash taxes, a $3.5bn loss filed without flinching). **I record the
two flags as two flags and decline to escalate.**

### **STEP 3 — THE PRIMARY TEST [E2-01]. And the two denominators disagree, which IS the finding.**

*"The primary test of managerial economic performance is the achievement of a high earnings
rate on equity capital employed (without undue leverage, accounting gimmickry, etc.) and not
the achievement of consistent gains in earnings per share."*

| $M | 2020 | 2021 | 2022 | 2023 | 2024 | **2025** |
|---|---|---|---|---|---|---|
| **operating income** | 90 | 269 | **(822)** | **(1,418)** | 1,075 | **1,468** |
| net income | 320 | 2,915 | **(3,460)** | 132 | 2,019 | 1,231 |
| shareholders' equity, year end | 6,401 | 11,133 | 8,239 | 9,066 | 11,558 | **13,473** |
| **operating income ÷ average equity** | 1.6% | 3.1% | n/m | n/m | 10.4% | **11.7%** |

**Net income is not the measure here and the table shows why: it swings by $6.4bn between
2021 and 2022 on mark-to-market of shares in other companies.** On **operating** income
against average book equity the answer is **11.7% pre-tax** — just under **[E5-40]**'s ~12%
*"quite satisfactory"* mark, and only two years old as a positive number.

**Now the [E2-43] denominator, which the corpus prescribes for acquisitive filers —
unleveraged net tangible operating assets, with the goodwill wedge reported separately:**
**$982M**, against $1,468M of operating income = **149.5% pre-tax.** *(Full derivation at Q2.)*

**THE DISAGREEMENT IS THE MANAGEMENT FINDING, AND IT IS THE LARGEST ONE IN THIS FILE.** The
operating business earns **149.5%** on the capital it actually uses. It earns **11.7%** on the
book equity management has assembled. **The gap is $11.5bn of assets that are not in the
business:**

| at 2025-12-31 | $M | % of equity |
|---|---|---|
| cash and equivalents | 1,545 | |
| marketable securities | 4,233 | |
| long-term investments | 975 | |
| **equity and other investments** (Affirm $1,511M, Global-E $868M, Klaviyo $599M, other) | **4,582** | |
| **equity-method investment** (Flexport) | **602** | |
| **total** | **11,937** | **88.6%** |

**Eighty-nine per cent of Shopify's book equity is not deployed in Shopify.** $5,184M of it
is cash and bonds; **$5,184M of it is shares in four other companies.** This is not a
liquidity buffer — [E5-11]'s strength (2) is satisfied several times over by the first
$5.2bn. **It is a portfolio, run by a software company, and it is the [E3-40] loss-of-focus
vector in balance-sheet form:** *"the management of a great company gets sidetracked and
neglects its wonderful base business while purchasing other businesses that are so-so or
worse… **Loss of focus is what most worries Charlie and me.**"*

### **THE HALF-OWNER TEST [E2-26] — SPLIT, AND BOTH HALVES ARE STRONG**

**PASSES on the financial statements.** The revenue and cost split by product line is filed
every year and reconciles exactly. The logistics disaster is quantified component by
component. The 23% workforce cut is itemised by expense line. Cash taxes, SBC and capex are
each on the face of the cash-flow statement. **Nothing material is buried in an adjusted
figure**, and there is no EBITDA anywhere.

**FAILS on the operating metrics.** *"tell you the business facts that we would want to know
if our positions were reversed."* **If our positions were reversed, the first fact I would
want about a subscription business is how many customers it has.** Shopify computes that
number every quarter — its own MRR definition was *"multiplying **the number of merchants**
who have subscription plans with us at the period end date by the average monthly subscription
plan fee"* — and has not published it since the FY2020 40-F. **It then removed the merchant
count from the definition itself in FY2025.**

**And [E2-72] — authorship.** *"owners are entitled to hear directly from the CEO… A
once-a-year report of stewardship should not be turned over to a staff specialist or public
relations consultant."* **Recorded sweep: there is no CEO stewardship letter in any Shopify
SEC filing.** The FY2025 10-K contains no letter to shareholders; the earnings releases carry
one or two quoted sentences from the CEO or President. The written record of stewardship in
this file is the MD&A. That is normal practice and it is not a disqualifier — **it is,
however, exactly the absence [E2-72] names**, and combined with the metric withdrawals it is
why the candor read here is "good on the numbers, thin on the narrative."

### **THE INSTITUTIONAL IMPERATIVE — SCORE ALL FOUR [E2-30]**
*Not a fraud test: "institutional dynamics, not venality or stupidity."*

- [ ] **resists any change in current direction** — **NO, and emphatically not.** This
  management changed direction twice in eighteen months: into logistics (July 2022) and out
  of it (May 2023), cutting 23% of the workforce on the way. Whatever else that is, it is not
  institutional inertia.
- [x] **projects/acquisitions materialise to soak up available funds — FIRES, AND IT IS THE
  CENTRAL Q3 FACT.** See below.
- [ ] **staff studies produced to justify the leader's craving** — not observable from
  filings. **Not scored** rather than scored zero.
- [x] **peer behaviour mindlessly imitated — FIRES, TWICE.** Amazon built fulfilment centres;
  Shopify bought a fulfilment company at the top of the cycle and exited eleven months later.
  And in February 2026 Shopify announced its first buyback in eleven years — at a moment when
  the practice is universal among large-cap software and when the share price was near an
  all-time high.

### **THE CENTRAL Q3 FACT: DELIVERR. $1,754M OF CASH IN, $528M OF PRIVATE PAPER OUT, ELEVEN MONTHS.**

**From the filed cash-flow statements and notes, with nothing added:**

| | |
|---|---|
| **cash paid for acquisitions, FY2022** ("Acquisition of businesses, net of cash acquired") | **$1,754M** |
| goodwill, 2021-12-31 → 2022-12-31 | $357M → **$1,836M** |
| Deliverr acquired | **2022-07-08** |
| logistics businesses sold to Flexport | **Q2 2023 — eleven months later** |
| carrying amount disposed (goodwill + intangibles + net assets) | **$1,868M** |
| consideration received | **13% of Flexport, non-cash, valued at $528M**, estimated by Shopify *"using unobservable inputs"* |
| **impairment charged to operating expenses** | **$(1,340)M** |
| Flexport equity-method losses since, cumulative | **$(279)M** (58 + 138 + 40 + 43) |
| **Flexport carrying value at 2026-06-30** | **$559M** |

**And the context that makes it a capital-allocation finding rather than a bad-luck finding:**
the purchase was made in **July 2022**, and Shopify's FY2022 operating cash flow was
**minus $136M** and its owner earnings **minus $735M — the worst year in its thirteen-year
filed history.** The company spent $1.75bn of cash buying a business at the moment it was
itself consuming cash. **[E2-30](2)** in one transaction: *"corporate projects or acquisitions
will materialize to soak up available funds."*

**[E4-39] — the rare-positive tell, and Shopify half-earns it.** *"a candid acquisition
post-mortem is almost never witnessed."* **There is no post-mortem** — no filing revisits the
Deliverr case against its announcement rationale. **But the accounting for it is
unflinching**: the loss ran through operating expenses, not below the line; it was not
excluded from any measure the company reports; and every component is itemised. **That is the
[E2-57] "except-for" flag NOT firing on the one occasion it easily could have.**

### **CAPITAL ALLOCATION — THE BUYBACK, AND THE TWO CONDITIONS [E5-08]**

**The facts, from the filed statements of changes in shareholders' equity and the Q4 2025
earnings release:**

> *"Shopify's Board of Directors has authorized a share repurchase program of **up to $2
> billion**. Shopify expects the program to be executed using **pre-arranged algorithmic
> trading instructions, with no set quarterly or annual minimums.**"* — 2026-02-11

| | shares repurchased | cash paid |
|---|---|---|
| every year 2015–2025 | **0** | **$0** |
| Q1 2026 | 4,214,019 | $521M *(equity charge)* |
| Q2 2026 | 12,645,957 | $1,445M *(equity charge)* |
| **H1 2026 total** | **16,859,976** | **$1,911M cash** |

**Average of roughly $113 per share on the cash paid.** Essentially the entire $2bn
authorization was executed in two quarters, by algorithm, with no price condition disclosed.

**CONDITION (1) — ample funds for operations and liquidity. MET, comfortably.** $5,472M of
cash, securities and long-term investments at 2026-06-30, zero debt, and owner earnings
running above $1.5bn a year. **[E5-25]** asks whether the company published its liquidity
floor as a number in advance; **it did not**, but the margin here is so wide the question does
not bite.

**CONDITION (2) — repurchases at a MATERIAL DISCOUNT to conservatively calculated intrinsic
value. FAILS ON MY OWN ARITHMETIC, AND THE FLAG IS RAISED WITH THE HUMILITY CLAUSE.** The
value range computed at Q5 is **roughly $16 to $31 a share** against the bare sovereign, on
every construction of a thirteen-year owner-earnings series. **Shopify repurchased at about
$113.** **[E4-13]:** *"it is natural for CEOs to be optimistic about their own businesses.
They also know a whole lot more about them than I do"*, and *"many CEOs never stop believing
their stock is cheap."* **This rests on my range, not on theirs. It binds position size and
nothing else — never the discount rate.**

**CONDITION (3), from [E4-31] — "Shareholders should have been supplied all the information
they need for estimating that value." THIS IS WHERE THE TWO HALVES OF Q3 MEET.** A buyback
executed against a register that has not been told the number of merchants since 2020, and
whose Attach Rate was withdrawn in 2024, is a buyback made against an under-informed
register. **The earliest full statement of the buyback rule fails on its third condition
before the second one is even reached.**

**AND THE TIMING IS THE [E5-24] FIRST LAW RUN BACKWARDS.** *"what is smart at one price is
dumb at another."* In **October 2022 Shopify's shares traded at $23.63** — a market
capitalisation near **$30bn** — with **$5,053M of cash and marketable securities** against
$913M of convertible notes on the balance sheet at that year end. **Nothing was repurchased.**
In 2026, at roughly **$113**, **$1,911M was.**

**THE DEFENCE, STATED PROPERLY BECAUSE IT IS A GOOD ONE [E4-26, E4-13].** Condition (1) is
first for a reason, and in 2022 it was **not** met: FY2022 operating cash flow was **negative
$136M** and owner earnings **negative $735M**. **On the corpus's own ordering, refusing to
repurchase in 2022 was correct**, and **[E2-51]**'s *"manager who consistently turns his back
on repurchases"* does not attach to a manager whose business was consuming cash.
**The rejoinder, which I record because it is also true: the reason operating cash flow was
negative in 2022 is that the same management had just spent $1,754M on Deliverr.** The
liquidity that would have licensed a repurchase at $23.63 was spent, three months earlier, on
the acquisition that was written off eleven months later. **Both statements are in the filings
and both belong in the record.**

### **EXECUTIVE COMPENSATION [E2-01, E2-73] — from the 10-K/A, accession `0001594805-26-000011`**

*(Shopify files no DEF 14A; Part III is filed by amendment. Recorded, because a run looking
for a proxy on EDGAR will not find one.)*

| NEO | 2023 | 2024 | **2025** |
|---|---|---|---|
| **Tobias Lütke, CEO** — salary $1 | $20,000,008 | **$150,000,084** | **$35,000,027** |
| Jeff Hoffmeister, CFO | $1,000,000 | $19,700,135 | $10,500,081 |
| Jessica Hertz, COO | $8,850,114 | $13,400,133 | $12,000,170 |
| Harley Finkelstein, President | $7,506,826 | $12,802,509 | $7,518,313 |
| **Kasra Nejatian, former COO & VP Product** | **$76,000,243** | $1,000,239 | $15,750,222 |

**A $1 salary for the CEO with everything in equity is the alignment structure the corpus
approves of** — Lütke is paid only if the shares rise. **But the amounts are not small
against the business:** the six named officers took **$82.3M in 2025** against **$1,468M of
operating income**, and the whole SBC charge is **$449M — 28.8% of owner earnings.** And
**$76.0M in a single year to a VP of Product in 2023 — the year the company cut 23% of its
workforce and wrote off $1,340M** — is a fact I record without interpretation, because the
grant's timing and vesting terms are not disclosed in enough detail to interpret it.

### **[E3-66] — WHERE DO THE SHAREHOLDERS STAND IN THE QUEUE? A NON-US RUN MUST SAY.**

*"there are many other countries where any good going to public shareholders has a very low
priority and almost every other constituency stands higher in line."* **[E3-66]**

**Shopify is a Canadian corporation under the CBCA, listed on NASDAQ and the TSX, and files as
a US domestic registrant.** Canada is not one of the jurisdictions [E3-66] warns about, and
Shopify has voluntarily accepted the heavier US regime. **But the share structure is the
finding, and the filing states it plainly:**

- Class A subordinate voting: **93.99% of the shares, 59.90% of the votes.**
- Class B restricted voting (10 votes each): **6.01% of the shares, 38.32% of the votes.**
- **The Founder Share: one share, no economic rights, 1.78% of the votes — variable, and set
  so that Lütke's total never falls below 40% and never exceeds 49.9%.**
- **Lütke's aggregate: 40.02% of the votes on roughly 6.1% of the economics** (1,548,000
  Class A + 77,750,132 Class B), as at 2026-04-21.
- And the mechanism that makes it permanent: *"**because of the variable voting power of the
  Founder Share… future issuances of Class A subordinate voting shares will not generally
  result in dilution of the voting power of Tobias Lütke.**"*
- The company's articles also **remove CBCA default class-vote rights** for certain amendments.

**This is not a disqualifier and it is not concealed — it is disclosed at length and was
approved by shareholders in a plan of arrangement on 2022-06-07. It is a structural fact a
buyer must accept:** the outside shareholder owns 94% of the economics and can never, under
any circumstance including unlimited future issuance, out-vote the founder. **[E3-66]** says
this class of factor is *"under-weighed precisely because it resists quantification"* — so it
is stated here rather than scored.

### **THE GUARDRAIL — checked before the verdict**

- [x] **Confirmed: nothing in this Q3 is being used to promote the name.** The one genuinely
  excellent Q3 finding — 149.5% pre-tax on unleveraged net tangible operating assets — is a
  fact about the *business*, and **[E2-37]** governs: *"a good managerial record… is far more
  a function of what business boat you get into than it is of how effectively you row."*
- [x] **Does this business REQUIRE a great manager?** No. The storefront runs without daily
  brilliance; the moat defect that would follow **[E4-23]** does not attach. Lütke's departure
  would be a shock to the shares and not to the switching cost.
- [x] **Is a great manager the reason to act?** **No, and this is the important negative.**
  There is no excisable-cancer case here **[E2-35, E2-36]** and no Pygmalion is being
  proposed. The name will be decided on price at Q5, not on the manager.

- **VERDICT: [x] IN**
  *IN = no disqualifier found. NOT a finding that the managers are honest — "sincerity and
  empathy can easily be faked" **[E5-17]**. IN never promotes.*
  **Two flags fired and are carried forward in writing: a quarterly guidance culture on five
  metrics [E4-22, E5-30], and three withdrawals or restatements of the operating metrics that
  measure the moat [E2-49]. One capital-allocation flag is live: the FY2026 repurchase fails
  [E5-08]'s second condition on this run's own value range, and its third condition [E4-31] on
  the register's information. Per the framework the flag BINDS POSITION SIZE and nothing
  else — never the discount rate [E4-13].**

---
## Q4 — WILL IT SURVIVE?

### **FIRST, THE QUESTION THE BRIEF PUT AT THE CENTRE: WHICH YEARS DESCRIBE THE BUSINESS THAT EXISTS NOW?**

**The screen refused three times and the refusals were right. Here is the answer, stated and
justified [E4-41], and it is not the answer the "pre-2020 versus post-2020" framing expects.**

**There are not two Shopifys in this series. There are FOUR, and the break that matters is
not 2020 — it is May 2023.**

| regime | years | what it was | OE @(c)=capex |
|---|---|---|---|
| **1. pre-monetization** | 2013–2019 | a subscription business too small to cover its stock compensation | **negative in all seven years**, $(3.9)M to $(144.7)M |
| **2. the pandemic** | 2020–2021 | GMV +95.6% then +46.7%; first positive owner earnings | +$136.4M, +$154.1M |
| **3. THE LOGISTICS COMPANY** | 2022 – H1 2023 | bought Deliverr for $1,754M cash (2022-07-08); owned warehouses, robots and freight | **$(735.0)M in 2022** — the worst year in the file |
| **4. what exists now** | **H2 2023 – present** | logistics sold to Flexport (Q2 2023); **23% of the workforce cut (May 2023)**; software plus payments plus lending | **+$290M, +$1,167M, +$1,558M** |

**Three filed events, all in the same six months, define the boundary:**
1. **The logistics businesses were SOLD in Q2 2023** — goodwill $(1,438)M, intangibles
   $(337)M, net assets $(93)M off the balance sheet. **This is a PERIMETER EVENT and the HON
   precedent binds: a multi-year owner-earnings mean that includes a divested business,
   divided by a market cap that excludes it, is two companies on either side of a division
   sign.** Every year through H1 2023 contains logistics; no year after does.
2. **Headcount was cut by approximately 23% in May 2023**, at a cost of $148M. The cost base
   of regime 4 is not the cost base of regime 3.
3. **The D&A series confirms it independently and physically:** $93M (2022) → $70M (2023) →
   **$36M (2024) → $31M (2025)**. The assets that generated two thirds of the depreciation
   left with the divestiture. **A 3.0x step in a depreciation series is a different set of
   assets, not a different accounting estimate.**

**THE DECISION, AND ITS COST, STATED PLAINLY: the business that exists now is 2.5 years old,
and THE CORPUS'S FIVE-YEAR DEFAULT WINDOW [E2-42, E1-03] CANNOT BE RUN ON IT.** *"we recommend
not less than a five-year test as a rough yardstick of economic performance."* **A five-year
mean on Shopify (2021–2025) averages a pandemic year, a logistics acquisition, a $1.34bn
write-off, a 23% redundancy programme and two years of the current business. That is not a
range; it is four companies.** I am not going to compute it and call it an estimate of
earning power.

**So both are reported, and the framework's own rule governs which one ranks: [E4-38] says
publish EVERY window, and [E5-34] says price against "the bottom boundary" of the estimate.**
The full thirteen-window table is at Step 0 above and is not repeated. **The judgment recorded
here is that windows reaching back past 2023-06-30 measure a company that no longer exists,
and windows inside it are shorter than the corpus's default. Both facts are carried into Q5
rather than resolved by preference.**

### **OWNER EARNINGS — THE ONE NUMBER, AND (c) IS THE BIGGEST JUDGMENT IN THIS FILE [E2-23]**

> *"(c) the average annual amount of capitalized expenditures for plant and equipment, etc.
> that the business requires to fully maintain its long-term competitive position and its unit
> volume. **(If the business requires additional working capital to maintain its competitive
> position and unit volume, the increment also should be included in (c).)**"* … *"**(c) must
> be a guess.**"*

**THE PLANT-AND-EQUIPMENT HALF OF (c) IS TRIVIAL HERE AND I SAY SO IMMEDIATELY.** Which case
is this under **[E3-44] / [E2-41] / [E5-20]**? **The corpus default holds and neither
exception applies.** Shopify is the opposite of the railroad: net property and equipment is
**$53M** against $11,556M of revenue; capex was **$26M (0.22% of revenue)** against D&A of
$31M; there is no separately-tagged capitalized software line in any filed cash-flow statement
(recorded sweep at Step 0); and there is no inflation-conditioned replacement problem
**[E4-47]** because there is almost nothing to replace. **The capex band — $26M to $31M — is
$5M wide on a $2,033M operating cash flow. It is 0.25% and it cannot change any answer in this
file.** *(This is the exact inverse of the CRWD finding, where the published spread was a
window spread wearing a capex band's clothes.)*

**THE WORKING-CAPITAL HALF OF (c) IS NOT TRIVIAL. IT IS $579 MILLION, AND IT DOES NOT APPEAR
IN OPERATING CASH FLOW.** Shopify's lending business funds its book through the **investing**
section:

| $M | 2023 | 2024 | **2025** | **H1 2026** |
|---|---|---|---|---|
| purchases and originations of loans | (1,861) | (3,006) | **(4,014)** | (2,933) |
| repayments and sales of loans | 1,338 | 2,542 | **3,435** | 2,460 |
| **net cash into the book** | **(523)** | **(464)** | **(579)** | **(473)** |
| loans and MCA, net, period end | — | 1,224 | **1,784** | **2,184** |

**Operating cash flow does not net this, because the corpus's own convention for our
construction — OCF less SBC less (c) — relies on OCF netting the working-capital change from
one audited line, and here the largest working-capital item in the business is filed in
investing.** *(And from April 2026 the merchant-cash-advance portion moved there too — the
reclassification found at Step 0 — which makes future operating cash flow larger still.)*

**THE GUESS, DISCLOSED AS [E2-23] REQUIRES IT TO BE.** Is the loan book's growth *required to
maintain* the competitive position and unit volume, or is it growth capital?

- **The maintenance argument is weak on its own terms.** To hold the book at $2,184M requires
  originations equal to repayments — **zero net cash.** On a strict reading, none of the $579M
  is maintenance.
- **The competitive-position argument is real.** Merchant capital is now a named competitive
  category in Shopify's own filing (*"alternative lenders"*, *"financial services"*), the book
  has grown in every year it has existed, and a Shopify that stopped extending credit would
  hand that merchant relationship to a competitor.
- **And [E2-60]'s third dimension binds:** restricted earnings are those whose payout costs
  the business *"its ability to maintain its unit volume of sales, its long-term competitive
  position, **its financial strength**."* **$579M a year is not distributable while the book
  is growing.**

**MY GUESS, AND IT IS A GUESS: the loan-book increment is REQUIRED, and both constructions are
reported rather than one chosen.** This is the honest form of *"I would rather be vaguely
right than precisely wrong"* **[E2-09]**.

| $M | 2023 | 2024 | **2025** | H1 2025 | **H1 2026** |
|---|---|---|---|---|---|
| operating cash flow | 944 | 1,616 | **2,033** | 795 | **1,139** |
| less share-based compensation **[E5-06]** | (615) | (430) | **(449)** | (227) | **(260)** |
| less capex | (39) | (19) | **(26)** | (10) | **(9)** |
| **= OWNER EARNINGS, conventional** | **290** | **1,167** | **1,558** | **558** | **870** |
| less net cash into the lending book | (523) | (464) | **(579)** | (345) | **(473)** |
| **= OWNER EARNINGS, full-capital** | **(233)** | **703** | **979** | **213** | **397** |

**TTM to 2026-06-30: conventional $1,870M · full-capital $1,163M.** *(TTM operating cash flow
$2,377M = FY2025 $2,033M + H1 2026 $1,139M − H1 2025 $795M. **Flagged: the H1 2026 leg sits
partly on the new merchant-cash-advance basis and the comparatives were not restated, so the
conventional TTM figure is overstated by an undisclosed amount. The full-capital construction
is immune to this**, because it deducts the whole lending increment wherever the filer chooses
to present it — which is why it is built.)*

**[E3-04] — THE LOOK-THROUGH ADJUSTMENT, APPLIED.** Shopify holds a 13% equity-method interest
in **Flexport**, whose losses are charged to net income and then **added back in operating
cash flow** ("Net loss on equity method investment 40"). **Owner earnings built from OCF
therefore do not bear it, and under [E3-04] they should.** Deduct **$40M (FY2025)**, $138M
(FY2024), $58M (FY2023), $43M (H1 2026). **FY2025 owner earnings become $1,518M conventional
and $939M full-capital.** *(The marketable minority stakes — Affirm, Global-E, Klaviyo — are
held at fair value and are credited to VALUE at Q5, not to earnings, so no look-through is
taken on them and nothing is double-counted.)*

**Stock compensation subtracted in full [E5-06]: yes, $449M, cross-checked to the dollar
against the filed cash-flow statement. And [E3-70]'s market-value test:** Shopify's awards are
RSUs and options; the reported charge is close to the market measure for the RSUs, and the
option grants (the CEO's entire $35.0M for 2025) are carried at grant-date fair value.
**$449M is treated as the floor of the subtraction, not a ceiling**, and no adjustment upward
is made because no quantifiable basis for one exists in the filing.

### **IS THE RANGE TOO WIDE TO REACH A CONCLUSION? [E4-25] — NO, AND HERE IS WHY THAT ANSWER IS AVAILABLE**

**The full published range is enormous: $160.9M (thirteen-year mean, D&A end) to $1,870M (TTM,
conventional) — an 11.6x span.** Restricted to the business that exists now it is **$703M
(FY2024 full-capital) to $1,870M (TTM conventional) — 2.7x.**

**[E4-25]** says that where the range is too wide, *"that IS the conclusion."* **It is not too
wide here, for one reason and one reason only: every construction gives the same answer at Q5.**
Against a market capitalisation of **$186,679M**, the widest possible spread of owner earnings
produces a yield of **0.38% at the bottom and 1.00% at the top**, against a **5.24%** sovereign
and a **~10% floor [E4-28]**. **A range that spans a factor of five and never once approaches
the decision threshold does not need to be narrowed. Stating that is not resolving the range by
preference — it is observing that the range is on one side of the line.**

**And a wide spread is a Q4 finding in its own right [E5-11], scoped by [E3-55].** *"If we have
a business about which we're extremely confident as to the business result, we would prefer
that it have high volatility."* **This is NOT that case.** The uncertainty here is about the
**level**, not the bounce: Shopify's owner earnings were $(735)M three years ago and $1,558M
last year, and the difference is not seasonality — it is a different perimeter, a different
headcount and a different set of assets. **The distorting years are named: 2020–21 (pandemic
pull-forward), 2022 (the Deliverr acquisition year), 2023 (the disposal, the impairment and
the 23% redundancy).**

**[E4-41] — NORMALIZE THE MEAN DOWN FOR LUCK. Applied, and the honest answer is that the
favourable break has ALREADY reversed and a NEW one has replaced it.** The pandemic tailwind
of 2020–21 is long gone. But **FY2024 and FY2025 carry $308M and $331M of interest income** on
a $5.8bn securities portfolio at a 5%+ short rate — **21% and 23% of operating income
respectively, earned on cash, not on commerce.** That is a rate tailwind not of management's
making and it belongs in [E4-41]'s category. **It is not deducted from owner earnings — it is
real cash — but it is named, and at Q5 it is why the cash is credited to VALUE rather than
allowed to inflate the operating yield.**

### **GREAT, GOOD, OR GRUESOME? [E4-20]**

- [x] **GREAT — on the platform, and it is not close.** *"pays an extraordinarily high
  interest rate that will rise as the years pass."* **149.5% pre-tax on unleveraged net
  tangible operating assets. Capex at 0.22% of revenue. Operating margin from (20.1)% in 2023
  to 12.7% in 2025, and rising.** The software business needs almost no capital and the
  return on what it does need is extraordinary.
- [ ] **GOOD — the lending arm, and [E4-43] says the good class PASSES.** *"nothing shabby
  about earning $82 million pre-tax on $400 million of net tangible assets."* Shopify Capital
  consumes $500M+ a year to grow a $2.2bn book. That is capital-hungry growth, and on
  **[E4-43]** it is a satisfactory business, not a failing one — **it only ranks below great.**
- [ ] gruesome — **no.** *"grows rapidly, requires significant capital to engender the growth,
  and then earns little or no money"* does not describe a company earning $1.5bn of owner
  earnings on $982M of net tangible operating assets.

**VERDICT ON THE THREE: GREAT, with a good business attached that is consuming a third of the
cash flow. And [E4-43]'s warning applies to the composite — the good half ranks below the
great half, and the good half is the one that is growing.**

### **STAYING POWER — SCORE ALL THREE [E5-11]. THE BRIEF SAID DO NOT PAD THIS. IT IS SHORT.**

1. **A large and reliable stream of earnings — LARGE, YES; RELIABLE, ONLY RECENTLY.**
   $1,558M of owner earnings in FY2025 on $11,556M of revenue growing 30%. **But it has been
   positive for three years out of thirteen.** The stream is large and it is young.
2. **Massive liquid assets — YES, OVERWHELMINGLY.** At 2026-06-30: cash $1,656M + marketable
   securities $3,291M + long-term investments $525M = **$5,472M**, plus **$5,413M** of
   marketable and equity-method stakes in other companies. **Against zero debt.**
3. **NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — YES, AND THIS IS THE ONE THAT USUALLY KILLS,
   SO IT IS CHECKED ITEM BY ITEM.** The **$913M of convertible senior notes matured and were
   repaid in cash in Q4 2025** ($1,043M financing outflow) — **the balance sheet now carries no
   borrowings at all.** Remaining fixed commitments, all of them: unconditional purchase
   obligations **$251M over two years**; operating lease liabilities **$178M** ($10M current);
   no pension, no defined-benefit obligation, no earn-outs disclosed. **Cash paid for interest
   in FY2025: $1 million.** **[E2-54]**'s coverage test — *"all interest, both payable and
   accrued, comfortably met out of current cash flow net of ample capital expenditures"* — is
   met by a factor of roughly two thousand. **[E5-39]:** nothing here depends on the kindness
   of strangers.

**Leverage, named and quantified: ZERO.** No debt of any kind at 2026-06-30. **The only
leverage-adjacent exposure in the business is the $2,184M loan book, which is 17.2% of
shareholders' equity and 40% of liquid assets, and it is an asset, not a liability.**

### **NAME THE SPECIFIC WAY THIS BUSINESS DIES [E2-27, E3-24], MODEL EXPOSURE NOT EXPERIENCE [E4-40]**

**THE MECHANISM, quantified from filed figures.** Shopify does not die of insolvency — it has
no debt and $5.5bn of cash. **It dies by the take rate reverting**, because 59.8% of its gross
profit and rising is a spread on payment volume that it buys wholesale from Stripe and PayPal
under twelve-month cancellable agreements, and the two comparators that publish the same
spread have lost 22% and 6% of it in five and four years respectively.

**THE ARITHMETIC, on filed FY2025 numbers, no forecasts:**

| net take rate (merchant gross profit ÷ GMV) applied to FY2025 GMV of $378,441M | merchant gross profit | change | **FY2025 owner earnings** |
|---|---|---|---|
| **0.878% — as filed, FY2025** | **$3,323M** | — | **$1,558M** |
| 0.810% — the 2022 level | $3,065M | $(258)M | **$1,300M** |
| 0.691% — the 2020 level | $2,615M | $(708)M | **$850M** |
| **0.575% — the 2019 level** | **$2,176M** | **$(1,147)M** | **$411M** |

**A reversion of the net take rate to where it stood in 2019 — before the pandemic, before
Shopify Payments penetration went from 41% to 65.6% — removes $1,147M, which is 74% of FY2025
owner earnings, without a single merchant leaving and without GMV falling by a dollar.**

**LIKELIHOOD: [x] a real possibility.** Not "likely": the take rate has risen in every year of
the filed record and Shopify Payments penetration is still climbing on geographic expansion.
Not "a low-level possibility": PayPal has lost 46 basis points of its take rate in five
consecutive years and Block has lost 19 in four, **both naming merchant mix as the cause, and
Shopify's own filing says the majority of its GMV now comes from Plus and enterprise
merchants** — the largest and most price-sensitive class. And **adoption of Shopify Payments
among merchants where it is available FELL in all three disclosed regions in 2025.**

**THE SECOND MECHANISM, quantified, and it is smaller: the credit book.** $2,184M net at
2026-06-30; transaction and loan losses already **4.0% of revenue** in H1 2026 against 2.2% in
2023. **[E4-40]** is the governing rule — *"model exposure, not experience"*, because *"a
benign loss history late in a good cycle is not only useless, but actually dangerous."*
**Consider some mathematics [E3-24]: if 20% of the $2,184M book produced losses averaging 50%
of principal, the charge would be $218M — 14% of a year's owner earnings, absorbed once,
against $5.5bn of liquid assets.** **Likelihood: [x] a low-level possibility, and not fatal
even so.** The book is not funded with debt and it is 17% of equity. **This is a real
possibility of pain and a low-level possibility of damage.**

**THE THIRD MECHANISM, NAMED AND NOT QUANTIFIED, AND [E4-51] REQUIRES ME TO SAY IT IS THE
WORST ONE.** The entire moat is that a merchant's live storefront is expensive to move.
**That is only valuable while the storefront is where the buyer arrives.** If purchasing
migrates to an agent layer — a chatbot that takes the order and routes the payment — the shop
becomes a catalogue endpoint and the switching cost becomes the cost of changing an API key.
**I cannot quantify this from filed figures and I will not pretend to.** It is named here as
the mechanism with the greatest severity and the least measurability, and the honest verdict
on it is that it is **unknowable in the [E4-19] sense** — no document I can name resolves it.
**That does not make Q4 UNKNOWABLE**, because the question Q4 asks is whether the business
survives, and a debt-free company with $5.5bn of cash and $1.5bn of owner earnings survives
this transition even if it is diminished by it.

- **VERDICT: [x] IN**
  *Carried forward, in writing: (a) owner earnings on the business that exists now rest on
  2.5 years, and the corpus's five-year default cannot be run; (b) the honest range is $703M
  to $1,870M, and it is reported as a range rather than collapsed; (c) the (c) guess on the
  lending book is $579M a year and is disclosed as a guess; (d) the take-rate reversion
  mechanism removes 74% of owner earnings on filed arithmetic and is rated **a real
  possibility**.*

---
⛔ **Q1 IN · Q2 IN (NARROW) · Q3 IN · Q4 IN. Q5 opens.**

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**Q1 IN · Q2 IN (NARROW) · Q3 IN · Q4 IN. This gate is open legitimately and this is a
clearance-eligible valuation, not a computation under a closed gate.**

### THE INPUTS, ALL OF THEM, AND EVERY GENEROUS CHOICE FLAGGED AS GENEROUS

| | |
|---|---|
| **price** | **$145.09** · 2026-09-04 close · **aggregator, FLAGGED, live quote only** |
| **shares** | **1,286,643,932** — 10-Q cover, all three classes, Founder Share worth nothing |
| **market capitalisation** | **$186,679M** |
| less cash and equivalents (2026-06-30) | $(1,656)M |
| less marketable securities | $(3,291)M |
| less long-term investments | $(525)M |
| **less equity and other investments** (Affirm, Global-E, Klaviyo, other) | **$(4,854)M** |
| **less equity-method investment** (Flexport, 13%) | **$(559)M** |
| plus debt | **$0 — there is none** |
| **= ENTERPRISE VALUE** | **$175,794M** |
| **sovereign** | **5.24%** · US Treasury 30-yr · 2026-09-04 · **the bare rate, no per-name premium [E3-42]** |

**THREE GENEROUS CHOICES, NAMED SO THEY ARE NOT MISTAKEN FOR CONSERVATISM:**
1. **Every non-operating asset is credited AT FACE, $10,885M in total.** That includes
   **$4,854M of shares in other people's companies** and **$559M of Flexport**, a loss-making
   private business whose carrying value has fallen for three straight years and whose 13%
   stake was valued by Shopify *"using unobservable inputs."* **[E3-71]** says such items go
   *"never at face, never at zero"* — I have used face, which is the friendliest treatment
   available, and I have done so because the answer does not depend on it.
2. **Interest income is stripped out of owner earnings** ($331M in FY2025) **precisely so the
   cash can be credited separately without double-counting.** Without that discipline the
   yield would look better than it is: a fifth of Shopify's operating income in FY2024 and
   FY2025 was earned on a bond portfolio, not on commerce **[E4-41]**.
3. **The whole range is shown, not just its bottom.**

### **1. THE YIELD, AT EVERY CONSTRUCTION, BESIDE THE BOND**

| construction | owner earnings | **yield on market cap** | **vs sovereign** |
|---|---|---|---|
| **FY2025 full-capital, ex-interest — the bottom boundary [E5-34]** | **$648M** | **0.35%** | **−4.89 pts** |
| FY2025 full-capital (lending increment in (c)) | $979M | 0.52% | −4.72 pts |
| FY2025 conventional, ex-interest | $1,227M | 0.66% | −4.58 pts |
| FY2025 conventional (OCF − SBC − capex) | $1,558M | 0.83% | −4.41 pts |
| **TTM to 2026-06-30, conventional — the most generous figure in the file** | **$1,870M** | **1.00%** | **−4.24 pts** |

**THERE IS NO CONSTRUCTION OF SHOPIFY'S OWNER EARNINGS — on any of thirteen windows, at either
end of the capex band, with or without the lending increment, with or without interest income,
before or after the Flexport look-through — THAT REACHES ONE AND A HALF PER CENT, LET ALONE
THE 5.24% GOVERNMENT BOND.** The single best twelve months in the company's history yields
**1.00%**.

*(The published row's `yield_bottom 0.85%` and `vs_sovereign −4.39 pts` were struck on the
$54,964M cap built from a 2014 pre-IPO share count. **On the true $186,679M cap the same
construction gives 0.25% and −4.99 points.** The screen's row was three times too flattering
on the one name in the queue where it mattered least, because the name fails by a factor of
six either way.)*

### **2. WHAT THE PRICE ALREADY ASSUMES**

**As a fading-rate DCF, run as an ENGINE ONLY and casting no vote [E3-34]** — ten years of
growth, then 3% in perpetuity, discounted at the **[E4-28]** 10% floor:

| starting owner earnings | **growth required for ten years to justify $175,794M** |
|---|---|
| $648M (bottom boundary) | **43.7% a year** |
| $1,227M (conventional, ex-interest) | **34.3% a year** |
| $1,539M (TTM, ex-interest) | **31.0% a year** |
| $1,870M (TTM conventional, cash NOT credited, against the full $186,679M cap) | **29.1% a year** |

**[E4-35] IS THE BOUND AND IT IS NOT CLOSE:** *"I would wager you a very significant sum that
**fewer than 10 of the 200 most profitable companies** in 2000 will attain **15% annual growth
in earnings-per-share over the next 20 years**."* **The quote requires roughly TWICE that
rate, for a decade, from a business whose owner earnings have been positive for three years.**

**AND THE SAME ASSUMPTION STATED AS A BUSINESS RATHER THAN A RATE, WHICH IS THE HONEST WAY TO
SEE IT.** A 10% return on a $175,794M enterprise value requires steady-state owner earnings of
**$17,579M**. Working back through Shopify's own filed ratios:

| at an owner-earnings margin of | implied revenue | vs FY2025 | implied GMV at today's 3.054% attach rate | vs FY2025 |
|---|---|---|---|---|
| **13.5% (FY2025 actual)** | **$130,411M** | **11.3x** | **$4.27 trillion** | **11.3x** |
| 20% (a mature software margin) | $87,897M | 7.6x | $2.88 trillion | 7.6x |
| **25% (better than Adobe's owner-earnings margin)** | **$70,318M** | **6.1x** | **$2.30 trillion** | **6.1x** |

**On the friendliest of those assumptions, today's price requires Shopify to eventually
intermediate $2.3 trillion of retail commerce — roughly six times the $378 billion it
facilitated in FY2025, and a large fraction of all the e-commerce in the world — at a margin
it has never earned.** **[E4-44]:** *"the value of an asset, whatever its character, cannot
over the long term grow faster than its earnings do… The Tinker Bell approach — clap if you
believe — just won't cut it."*

**What the business has actually done, filed:** revenue **+30.1%** in FY2025; GMV **+29.5%**;
gross profit **+24.2%**; MRR **+15.2% and decelerating**; net take rate **+0.4 basis points**.
**The top line is genuinely growing at close to the rate required. The gross profit is not, and
the price needs the compounding to run for a decade and then some.**

### **3. WHAT YOU ARE PAID — and this is the number that closes the question**

**Between −4.24 and −4.89 points against the sovereign at today's price.**

**And the expectancy test done properly, because a low current yield on a fast-growing business
is not automatically a bad investment and I am not going to pretend it is [E4-51].** Here is
the honest pre-tax expectancy at $145.09, on ten years of growth then 3% forever:

| owner-earnings growth for ten years | expectancy from **$648M** | expectancy from **$1,227M** |
|---|---|---|
| 10% a year | 3.72% | 4.35% |
| 15% a year — the [E4-35] fewer-than-1-in-20 event | 4.10% | 5.02% |
| 20% a year | 4.63% | 5.93% |
| 25% a year | 5.35% | 7.11% |
| **30% a year, for TEN YEARS** | **6.28%** | **8.55%** |

**Read the bottom row. If Shopify's owner earnings compound at THIRTY PER CENT A YEAR FOR A
DECADE — a rate essentially no large company has ever sustained — the buyer at $145.09 earns
8.55% on the most generous starting figure and 6.28% on the conservative one. BOTH ARE BELOW
THE 10% FLOOR.** *"that's the figure we quit on… that's true whether short rates are 6 percent
or whether short rates are 1 percent"* **[E4-28]**.

**That is the whole answer to this file, and it is worth stating plainly: the argument against
Shopify at this price is not that the business is bad. Q1 through Q4 all cleared. It is that
the price has already borrowed a decade of extraordinary success and still does not clear the
floor.**

### **THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]**

*Owner earnings capitalised at the bare sovereign, no per-name risk premium **[E3-42]**, plus
the full $10,885M of cash and investments at face:*

| | conservative ($648M) | middle ($1,227M) | generous ($1,539M) |
|---|---|---|---|
| **at the sovereign, 5.24%** | $23.3bn · **$18.07/sh** | $34.3bn · **$26.66/sh** | $40.3bn · **$31.29/sh** |
| **at the [E4-28] 10% floor** | $17.4bn · **$13.50/sh** | $23.2bn · **$18.00/sh** | $26.3bn · **$20.42/sh** |
| **current price** | | | **$145.09** |

**In round numbers, as the corpus requires: roughly $18 to $31 a share against the bare bond;
roughly $13.50 to $20 a share against the 10% floor. The price is $145.09 — between 4.6 and
10.7 times the value this method can construct on zero growth.**

*(Stated for completeness rather than as a defence: these are zero-growth capitalisations, and
Shopify is emphatically not a zero-growth business. That is exactly why the growth-adjusted
expectancy table above exists, and it reaches the same verdict.)*

### **THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21]**

- **Honest pre-tax expectancy at this price: 3.7% to 8.6%**, the upper end requiring 30% annual
  owner-earnings growth for ten years. **Against the corpus's ~10%.**
- **BELOW THE FLOOR ON EVERY ASSUMPTION I CAN HONESTLY MAKE. The name is not ranked — it is
  QUIT ON**, and per the template the ranking lines below it are not filled in.
- points over sovereign: **−4.24 to −4.89** — *not filled as a ranking input; recorded only.*

### **[E2-63] — WHAT BOUNDS THE UPSIDE, SINCE A Q5 VERDICT MUST NAME IT**

*"most operating businesses are also capped unless more capital is continuously invested."*
Two things cap Shopify. **The first is the attach rate:** at 3.05% of GMV, the ceiling on
revenue is set by how much commerce runs through the checkout, and the net take rate has added
0.4 basis points in a year. **The second is the supplier:** the majority of the gross profit is
a spread bought from Stripe and PayPal on twelve-month renewals, and three independent
processors — PayPal, Block and Adyen — have each lost take rate over four to five years.
**Shopify's upside is bounded by GMV growth times a rate it does not set.**

### **WHICH BAR? [E4-01]'s SCREAMER TEST, AND IT RETURNS THE THIRD OUTCOME**

- [ ] Normal method [E4-11] — **not used. No margin of safety is computed, because [E4-11]'s
  margin applies to a value the price already exceeds by 4.6x at the most generous end.**
- [x] **Screamer test [E4-01]** — three outcomes; this is the **third**: **the price is above
  the whole range, not inside it.** *"it ought to just kind of scream at you"* **[E3-25]**. It
  does not.
- **WINDAGE COUNT: ONE.** Conservatism is spent once, at **[E5-34]**'s instruction to price
  against the bottom boundary of the estimate. **Everywhere else the inputs are realistic or
  deliberately generous**: the sovereign is bare with no risk premium **[E3-42]**; all
  $10,885M of cash and investments is credited at face including a private loss-making stake;
  the owner-earnings series is the filed figures unadjusted; and the full range is published
  rather than its low end alone. **Conservatism is not stacked [E4-48].**

- **VERDICT: NOT IN — QUIT ON at the [E4-28] floor.** · **ranking position: NOT RANKED.**

  *The label needs a word of explanation, because the template offers IN / UNRESEARCHED /
  UNKNOWABLE at Q5 and none of the three is "the price fails". It is not **UNRESEARCHED** —
  there is no document I have not got; the filings are read and the arithmetic is complete.
  It is not **UNKNOWABLE** — nothing about the future is indeterminate here; a 0.35%-to-1.00%
  yield against a 5.24% bond is a fact about today. And it is deliberately **not OUT**, because
  OUT is permanent and is a verdict about the BUSINESS, and this business cleared Q1 through
  Q4. **This is the mirror image of the QLYS ruling of 2026-09-07** — a name that fails at Q2
  fails on the business and a price alert on it would be a category error; **a name that fails
  only at Q5 fails on the price, and a price alert on it is exactly the right instrument.**
  The framework's own words for this outcome are the ones used: **the name is quit on, and it
  is not ranked.***

**PASS/FAIL: FAIL, ON PRICE. The business cleared all four business gates — the first name in
this queue to do so and then fail here rather than earlier — and the price is between 4.6 and
10.7 times any value this method can construct.**

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

*There is no position and none is opened, so this is filled as a WATCH specification rather
than as an exit plan. **[E1-02]** requires yardsticks set in advance, and a name that clears
four business gates and fails only on price is the class most worth watching.*

**PRE-COMMITTED, BEFORE ANY ENTRY [E1-02]:**

- **Thesis-confirming metric:** **the net take rate — merchant-solutions gross profit ÷ GMV.**
  It is computable every quarter from two filed numbers. It must **rise**. It added 0.4 basis
  points in FY2025 (0.874% → 0.878%).
- **THESIS-BREAKING METRIC AND ITS THRESHOLD:** **the net take rate FALLING in any filed
  fiscal year**, or **merchant-solutions gross margin below 36%** (it is 37.7%; 36.2% is where
  it stood in 2017). Either one says the payments spread has begun to go the way PayPal's,
  Block's and Adyen's went.
- **The second breaker:** **Shopify Payments adoption where available falling below 85% in
  North America** (88% at 2025-12-31, down from 91%). Three more points and the default has
  stopped being a default.
- **The third, and it is the one that would reopen everything:** **the merchant count
  republished.** Shopify computes it every quarter and has not published it since the FY2020
  40-F. Its return would be the single strongest candor signal available from this management,
  and it costs them one line.
- **THE PRICE AT WHICH THIS BECOMES A DIFFERENT QUESTION.** The [E4-28] floor is reached at
  roughly **$20 a share on the middle construction and $31 on the most generous one, with no
  growth credited at all** — and at roughly **$45 to $60** if one is willing to underwrite
  15% owner-earnings growth for a decade, which **[E4-35]** says is a fewer-than-one-in-twenty
  event among the best businesses on earth. **Shopify has traded below $60 as recently as
  2023 and below $25 in October 2022.** This is a name to keep a file on.
- **Next catalyst date:** **Q3 2026 results, expected early November 2026** — the first full
  quarter reported entirely on the new merchant-cash-advance cash-flow basis, and the first
  read on whether the $2bn repurchase authorization is extended.

**THE SELL RULE [E2-28] — not applicable; there is nothing to sell.** Recorded for
completeness: the three hold conditions (satisfactory return on equity capital, competent and
honest management, market not overvaluing) are **two-for-three today**, and the one that fails
is the third.

**THE MONITORING QUESTION [E4-17, E3-30]:** *is the erosion an aberrational cycle, or has the
business slipped in a way that permanently reduces intrinsic value?* **On Shopify the question
is asked of the take rate, not of the revenue.** Revenue and GMV are accelerating; the rate at
which they convert into gross profit has flattened. **[E4-17]** says beliefs about moats
*"change quite gradually"* — three more years of a flat net take rate would be a permanent
downgrade, and one year is not.

**Position size [E5-14, E3-45]: ZERO. No position is taken and none is recommended.** *(Had
the price cleared, the live capital-allocation flag from Q3 — the FY2026 repurchase failing
[E5-08]'s second and third conditions — would have bound the size DOWN, per the framework.
It does not arise.)*

- **VERDICT: [x] IN as a WATCH specification.** No position; falsifiers pre-registered above.

---
## SELF-AUDIT

- [x] **Questions answered in order; no verdict skipped.** Q1 IN → Q2 IN (NARROW) → Q3 IN →
      Q4 IN → Q5 NOT IN, quit on at the floor → Q6 filled as a watch specification.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** The Q2 moat
      class is NARROW, which is a substantive finding, not a hedge; it is explicitly **not**
      PROVISIONAL, and the reason is stated (the verdict rests on Shopify's own filed
      gross-profit split, take-rate series, Payments-adoption disclosure and supplier risk
      factor, none of which needs a peer filing).
- [x] **No UNRESEARCHED verdict was written**, so none needs an artifact named.
- [x] **No UNKNOWABLE verdict was written.** One sub-finding is recorded as unknowable in the
      [E4-19] sense and does not carry a gate: whether agentic commerce dissolves the
      storefront switching cost. It is named at Q4 with the reason no document resolves it.
- [x] **Step 0: the filing was read**, with the FY2025 10-K accession `0001594805-26-000007`,
      the Q2 2026 10-Q `0001594805-26-000047`, the Q2 2025 10-Q `0001594805-25-000073`, the
      FY2025 10-K/A `0001594805-26-000011`, the FY2024 10-K `0001594805-25-000012`, and the
      FY2016–FY2023 40-F vintages with their Exhibit 13 MD&As.
      **FOUR figures cross-checked to the dollar/million against the filed statements:**
      operating cash flow $2,033M, share-based compensation $449M, capex $26M, and the
      product-line gross-profit split ($2,232M + $3,323M = $5,555M = filed consolidated gross
      profit).
- [x] **Owner earnings on a multi-year mean; window stated; capex band disclosed as a
      judgment.** **Thirteen windows published at both (c) ends [E4-38].** The capex band is
      disclosed and shown to be $5M wide (0.25% of OCF). **The (c) judgment that matters — the
      $579M-a-year lending-book increment — is disclosed AS A GUESS [E2-23] and both
      constructions are reported.**
- [x] **Competitor row filled** — **eleven comparators attempted, eight with SEC-filed data,
      one (Adyen) from the issuing company with the rung and the unaudited status flagged, and
      three hard limits named: Stripe (private, permanent), Squarespace (deregistered
      2024-11-01, last filed FY2023), Adobe Commerce (never segmented).** The moat class is
      not PROVISIONAL; the reason is stated at Q2.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.** USD
      5.24%, US Treasury 30-yr, 2026-09-04. **The Canadian-incorporation question was asked
      and answered from the filing: the reporting currency is USD.**
- [x] **Value stated as a round-number range, not a point estimate** — roughly $18 to $31 a
      share against the bare bond, roughly $13.50 to $20 against the 10% floor.
- [x] **One bar chosen, not both.** Screamer test [E4-01], third outcome. **Windage count:
      ONE**, stated, with the three deliberately generous choices named so conservatism is not
      mistaken for stacking [E4-48].
- [x] **Prices dated; aggregator used for the live quote only and flagged.** $145.09,
      2026-09-04.
- [x] **The share count was read off the cover of the latest periodic filing by hand**, the
      three-class judgment was made from the charter description, and **the screen's cap was
      found wrong by 3.40x and corrected.**
- [x] **Run committed to git after every gate**, own files by name, never `git add -A`.
- [x] `python tools/check_framework.py` run before the final commit.

## REGISTER

- **Verdict: NOT IN — QUIT ON AT THE [E4-28] FLOOR, ON PRICE.** Not OUT: the business cleared
  Q1 through Q4 and OUT is a permanent verdict about a business.
- **One line:** *Shopify is a genuinely good business wearing a narrow franchise — an 81%-margin
  storefront subscription that is only 24% of revenue — bolted to a 37.7%-margin payments
  spread it buys wholesale from Stripe and PayPal on twelve-month cancellable contracts; it has
  no debt, $10.9bn of cash and investments, 149.5% pre-tax returns on the capital it actually
  uses, and at $145.09 it costs between 4.6 and 10.7 times any value this method can construct,
  returning under 9% even if its owner earnings compound at 30% a year for a decade.*
- **Q1 IN · Q2 IN (NARROW) · Q3 IN · Q4 IN · Q5 NOT IN — quit on, not ranked · Q6 IN as a
  watch specification.**
- **Price $145.09 (2026-09-04) · shares 1,286,643,932 (10-Q cover, accession
  `0001594805-26-000047`, three classes, Founder Share worth nothing) · market cap $186,679M ·
  sovereign 5.24% USD.**
- **Owner earnings $648M to $1,870M depending on construction · yield 0.35% to 1.00% ·
  −4.24 to −4.89 points against the sovereign.**
- **Value roughly $18–$31/share at the bond, $13.50–$20 at the floor. FAIL at Q5.**

### THE WATCH SPECIFICATION — this name failed on PRICE, so a price band is the right instrument

*(Per the QLYS ruling of 2026-09-07 read in reverse: a name that fails at Q2 fails on the
business and a price alert would be a category error; **this name failed only at Q5**.)*

- **Alert band: $31 and below** — the top of the zero-growth value range at the bare sovereign.
- **A second, softer band at $60** — the level at which a buyer underwriting 15% owner-earnings
  growth for a decade would reach the [E4-28] floor. **[E4-35]** says that growth rate is a
  fewer-than-one-in-twenty event among the 200 most profitable companies on earth, so this band
  is recorded as a *read-again* trigger, not a buy trigger.
- **The business falsifiers that would close the file permanently** (any one → Q2 becomes OUT
  and the price bands are withdrawn): net take rate falling in a filed year · merchant-solutions
  gross margin below 36% · Shopify Payments adoption below 85% in North America · subscription
  gross margin below 77%.

## RUN LOG

- 2026-09-07: file created from the template before any data was fetched. Write-early protocol.
- 2026-09-07: Step 0 written and committed. **Found the screen's market cap wrong by 3.40x** —
  $54,964M against a true $186,679M — reproduced to the dollar as
  `39,310,446 (2014-12-31, pre-IPO) x 10 (2022 split) x $139.82`. Sixth instance of the
  companyfacts dimensioned-share-count defect and the largest in dollars.
- 2026-09-07: Q1 written — **IN**. Filed subscription/merchant gross-profit split rebuilt across
  nine vintages; net take rate built two ways; the lending business surfaced.
- 2026-09-07: Q2 written — **IN, NARROW**. Competitor row built at
  `_research 2026-09-07 SHOP/COMPETITOR_ROW.md`.
- 2026-09-07: **Q2 addendum** appended when three further comparators arrived (Adyen from the
  issuing company, Global Payments, and the permanent Stripe limit). The verdict did not move;
  two findings did, and both are recorded rather than folded silently into the original table.
- 2026-09-07: Q3 written — **IN (qualitative overlay)**. Deliverr worked; buyback tested against
  [E5-08]'s three conditions; two flags fired.
- 2026-09-07: Q4 written — **IN**. The four-regime finding; the 2.5-year window; the lending
  increment disclosed as the (c) guess; the take-rate reversion quantified as the named death.
- 2026-09-07: Q5 written — **NOT IN, quit on at the floor**. Q6 filled as a watch spec.
  Self-audit and register written. **Run complete.**
