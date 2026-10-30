# Company Run — Paymentus Holdings, Inc. (PAY) — 2026-09-11
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*Run history: created 06:57 ET under the write-early protocol; the session was killed at
11:50 ET with the file still a bare template and the research folder on disk; resumed 12:15
ET from the cached filings. No question was lost.*

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

---
## STEP 0 — THE RATE, THE COVER, AND THE FILING

### The sovereign, for the currency the business EARNS in **[E4-15, E3-32]**
- rate **5.37 %** · date **2026-09-10** · source **US Treasury daily par yield curve, 30-yr
  (issuing authority, struck this session via `python tools/sources.py`; not the FRED
  fallback; the daily fetch of 2026-09-10 shows the same figure and was read, not inherited)**
- FX: none. *"The reporting currency of the Company is the U.S. Dollar"* (FY2025 10-K, Note
  2), and revenue by geography is **$1,177.6M United States / $18.9M Other** of $1,196.5M —
  98.4% US. Canadian-dollar and Indian-rupee exposure is a cost-side item (engineering in
  Canada and India), recorded at Q4 if reached, not a Step 0 one.

### STAGE 0 — THE COVER COUNT, BY HAND, AND THE SCREEN'S CAP IS THE PRE-IPO COUNT AGAIN

**1. The count, read from the cover this session.** `python Screens/cover_shares.py PAY`:

    10-Q filed 2026-08-04, period 2026-06-30, accession 0001193125-26-330940
    Common Class A [Member]        63,114,220
    Common Class B [Member]        62,825,427
    --- arithmetic sum, NOT a share count ---   125,939,647
    MULTIPLE CLASSES. Whether these are economically equivalent is a JUDGMENT
    from the charter, not arithmetic. READ THE FILING.

**2. The judgment the tool refuses to make, made here from the charter description in the
filing.** FY2025 10-K, Note 9 (Stockholders' Equity), verbatim:

> *"The shares of Class A common stock and Class B common stock are **identical, except
> with respect to voting and conversion**. Each share of Class A common stock is entitled to
> one vote. Each share of Class B common stock is entitled to **ten votes**. … Holders of
> common stock are entitled to receive any dividends as may be declared from time to time by
> the board of directors."*

> *"Shares of Class B common stock may be converted to Class A common stock **at any time at
> the option of the stockholder**. Shares of Class B common stock automatically convert to
> Class A common stock upon the following: (i) sale or transfer … (ii) the death of the
> Class B common stockholder (or nine months after the date of death if the stockholder is
> one of the Company's founders); and (iii) on the first trading day on or after the date on
> which the outstanding shares of Class B common stock represent **less than 10%** of the
> then outstanding Class A and Class B common stock."*

And the EPS note (Note 13): *"The rights of the holders of Class A and Class B common stock
are identical, except with respect to voting and conversion. As the liquidation and dividend
rights are identical, the undistributed earnings are allocated on a proportionate basis to
each class of common stock and the resulting basic and diluted net income per share
attributable to common stockholders are, therefore, **the same for both Class A and Class B
common stock**."*

**DECISION: the two classes ARE economically equivalent and summing them is correct.** Same
$0.0001 par, identical dividend and liquidation rights on the filing's own words, 1:1
conversion at the holder's option, one EPS figure struck across both. **The difference is
votes, not money.** Class B is 49.9% of the shares and carries **90.9% of the votes**
(62.8M × 10 = 628M votes against 63.1M) — AKKR 58.2% and the founder 31.3% of the voting
power on 33.8% and 18.1% of the economics (DEF 14A 2026, ownership table as of 2026-04-09).
That is a governance finding for Q3, not a share-count adjustment. *(Same outcome as PINS's
Stage 0: both classes live, the sum is the right number, the vote gap is recorded at Q3.)*

**3. The price is re-struck, and the queue's cap reproduces to the dollar from a stale count.**
- **price $36.28 · 2026-09-10 close · aggregator, FLAGGED, live quote only** (operator rule 5).
- **shares 125,939,647** (10-Q cover, as-of the filing's own date; both classes, judged equivalent).
- **MARKET CAP = $36.28 × 125,939,647 = $4,569M.**
- **The brief's row says `cap_m 3635`. Reproduced exactly:** `$35.13 (2026-09-01 close) ×
  103,479,239 = $3,635M`. **103,479,239 is `us-gaap:CommonStockSharesOutstanding` at
  2020-12-31 — the PRE-IPO count, five months before the May 2021 listing, and the last
  undimensioned share fact this filer ever tagged** (every later cover is tagged by class and
  `companyfacts` drops dimensioned facts; the FY2021 10-K tags the 2021 year-end as **0**).
  The queue also priced the name nine days stale. **This is the LEVI / NKE / DKS / PINS /
  SHOP mechanism in its seventh instance; the published cap understates the true one by
  20.4%, and every yield in the row is overstated by the same fraction.** `tools/run.py`
  avoided the pre-IPO count only by falling to the diluted weighted average (129.1M), which
  is an EPS denominator and 2.5% above the cover. Recorded as a tooling defect, not patched
  here (operator rule 8).

**4. And the count moved for a reason worth recording.** The annual-meeting record dates give
a third cover pair: **2025-06 record date: 35,123,281 A / 90,001,141 B** (8-K 2025-06-06);
**2026-06 record date: 62,936,502 A / 62,852,835 B** (8-K 2026-06-08). **Roughly 27 million
Class B shares converted to Class A between June and December 2025 and the public float rose
from $354.0M (2024-12-31) to $1,353.8M (2025-06-30, 10-K cover).** No company registration
statement was filed; the sponsor sold. AKKR's 2026 proxy holding is 40.0M B + 2.5M A =
33.8% of the economics, down from roughly 56%. Treated at Q3.

### The filing was read — not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary: FY2025 Form 10-K, FYE 2025-12-31, filed 2026-02-24, accession
  `0001193125-26-064510`.** Large accelerated filer; ceased to be an emerging growth company
  at 2025-12-31 (Note 2).
- **Newest: Q2 2026 Form 10-Q, period 2026-06-30, filed 2026-08-04, accession
  `0001193125-26-330940`.** Also Q1 2026 `0001193125-26-204469` and Q3 2025
  `0001193125-25-262925`.
- Vintages read for the disclosure-history and metric tests: FY2024 10-K
  `0000950170-25-036566`; FY2023 `0000950170-24-025084`; FY2022 `0000950170-23-005995`;
  FY2021 `0000950170-22-002823` (carries the 2019 and 2020 statements); and the IPO
  prospectus, 424B4 filed 2021-05-26, `0001564590-21-030067`.
- Proxies: DEF 14A 2026 `0001193125-26-170573` (filed 2026-04-22); DEF 14A 2025
  `0001193125-25-091379`.
- **Eight 8-K EX-99.1 earnings releases read** for the guidance record and the non-GAAP
  headline test: Q3 2024 through Q2 2026 (`0000950170-24-125439`, `-25-036271`, `-25-063531`,
  `-25-102005`, `0001193125-25-262574`, `-26-063980`, `-26-203992`, `-26-330585`), plus the
  non-earnings 8-Ks of 2025-03-19, 2025-06-06, 2025-07-02, 2026-03-13, 2026-03-26,
  2026-04-08, 2026-06-08 and 2026-07-23.
- **Figures cross-checked against the filed statement (operator rule 4):**
  1. XBRL FY2025 operating cash flow **$162,127k**; the filed Consolidated Statements of Cash
     Flows reads *"Net cash provided by operating activities 162,127"* — agrees.
  2. **Capitalised software, because the brief said it decides (c):** XBRL
     `PaymentsToDevelopSoftware` **$36,737k**; the filed investing section reads
     *"Capitalized internal-use software development costs (36,737)"* beside *"Purchases of
     property and equipment (361)"* — agrees. **Capitalised software is 99% of the capital
     line. The HAS/CRWD defect is live on this filer and `tools/run.py` handles it (its
     `SOFTWARE_CAP` list resolves the tag and sums it).**
  3. **SBC, two figures, and the difference matters:** the cash-flow add-back reads
     *"Stock-based compensation 18,627"* (XBRL `ShareBasedCompensation` 18,627) while Note 11's
     total expense is **$20,821k** (`AllocatedShareBasedCompensationExpense`); the $2.2M gap
     is SBC capitalised into software. The run subtracts the cash-flow figure, because the
     capitalised part is already inside the $36.7M capital line — subtracting both would
     count it twice. `tools/run.py` used the larger tag (21) and so understates OE by ~$2M.
  4. **Contribution profit reconciles:** filed gross profit 296,342 + *"other cost of
     revenue"* 89,967 = **386,309** = the filed contribution-profit table — agrees.

---
## THE SCREEN ROW — REPRODUCED, AND THE THREE FLAGS ARE ONE FINDING **[E4-25]**

**The published row** (`Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`, line 221):

    PAY, cap_m 3,635 · oe_bottom_m 24 · oe_top_m 48 · spread 0.965 ·
    yield_bottom 0.0067 · vs_sovereign −0.047 · growth_required 0.0933 ·
    level_shift 4.25 "STEP UP - normalize down [E4-41]" ·
    best_year_dep 0.322 "ONE YEAR CARRIES THE WINDOW" (9-yr OCF series) ·
    level_shift_oe n/a "EARLY HALF STRADDLES ZERO - runs from -$17.9M" ·
    best_year_dep_oe 0.675 · flags_disagree FIRES · years_filed 7 · newest 2025-12-31

**Every arithmetic figure except the cap reproduces.** Here is the whole seven-year series,
every line from a filed cash-flow statement (FY2021 10-K for 2019–2021, then each year's
10-K). Capex is PP&E **plus capitalised software**; (c) at the capex end and the D&A end:

| year | OCF | SBC (CF) | PP&E | cap. software | **capex total** | D&A | **OE @(c)=capex** | OE @(c)=D&A |
|---|---|---|---|---|---|---|---|---|
| 2019 | 17.5 | 1.6 | 1.0 | 10.2 | 11.3 | 6.0 | **4.7** | 9.9 |
| 2020 | 35.6 | 2.0 | 0.5 | 14.4 | 14.8 | 8.1 | **18.8** | 25.6 |
| 2021 | 19.5 | 3.1 | 1.0 | 19.3 | 20.3 | 13.3 | **(3.9)** | 3.1 |
| **2022** | 19.9 | 6.7 | 1.3 | 29.8 | 31.0 | 24.1 | **(17.9)** | (10.9) |
| 2023 | 68.8 | 9.4 | 0.6 | 33.7 | 34.3 | 30.6 | **25.1** | 28.8 |
| 2024 | 63.6 | 11.0 | 0.5 | 36.1 | 36.6 | 36.5 | **16.1** | 16.2 |
| **2025** | **162.1** | 18.6 | 0.4 | 36.7 | 37.1 | 41.1 | **106.4** | 102.4 |

*($M. The −$17.9M in the `level_shift_oe` verdict string is FY2022 at the capex end, exactly.)*

**`oe_bottom 24` is the 5-year mean at the capex end (25.2 here; the screen's 24 uses the
larger SBC tag); `oe_top 48` is the 3-year mean (49.2). Both reproduce within the SBC-tag
difference noted at Step 0.**

### THE BRIEF'S QUESTION: WHICH YEARS DESCRIBE THE BUSINESS THAT EXISTS NOW **[E4-41]**

**The three flags point at one thing, but it is not the IPO year.** The IPO was May 2021.
The owner-earnings sign change is 2021–2022, and the filed statements say why: capitalised
software ramped from $14M to $30M a year while operating cash flow stalled at $19–20M for
two years — G&A doubled ($17.8M → $33.0M in 2021, the public-company cost base), SBC tripled,
and 2022 carried an operating loss (−$3.0M). **Those two years are the company paying to
become a public company on a $400–500M revenue base; they are not a cash-consuming business
in the PINS sense, and they are not the business that exists now.**

**The 2025 step is the second thing, and it is half real and half working capital.** The
cash-flow detail lines: *"Accounts and other receivables (43,618)"* in 2024 and **"17,141"**
in 2025 — a $60.8M swing between two adjacent years. Strip the receivables line from both
and 2024 OCF is $107.3M and 2025 is $145.0M. So the honest reading of 2024–2025 is a
business generating roughly **$110–145M of operating cash a year**, not the $64M / $162M the
filed pair shows. **The `STEP UP` flag is right that a level shift occurred (2023 onward)
and right that 2025 must be normalised down; it is wrong if read as "2025 is a fluke."** The
first half of 2026 confirms the level: OCF **$79.3M** with a receivables *drag* of $3.4M,
against $81.9M in H1 2025 that carried a $23.4M receivables *release*.

**DECISION, stated and justified:** the years that describe the business that exists now are
**2023–2025** — the post-transition, profitable, large-accelerated-filer company with the
present biller mix (large enterprise billers joined from 2022, per every MD&A since).
2019–2020 are the private company; 2021–2022 are the transition. **The five-year window is
still run and carried, because the corpus's default is five years [E2-42] and the spread is
part of the range [E4-25]; the three-year window is the one this run believes.**

### THE REBUILT WIDTH — every window, both (c) ends **[E4-38]**

| window | (c) = capex | (c) = D&A |
|---|---|---|
| 1y (2025) | $106.4M | $102.4M |
| 2y (2024–25) | $61.2M | $59.3M |
| **3y (2023–25)** | **$49.2M** ← the published `oe_top` | $49.1M |
| 4y (2022–25) | $32.4M | $34.1M |
| **5y (2021–25)** | **$25.2M** ← the published `oe_bottom` | $27.9M |
| 6y (2020–25) | $24.1M | $27.5M |
| 7y (2019–25) | $21.4M | $25.0M |

**Published range $24M–$48M, width 96.5%. Rebuilt range, all windows: $21.4M–$106.4M, width
397%. Restricted to multi-year windows, as the corpus's five-year default admits: $21.4M–
$61.2M, width 186%.** In dollars and a word: **the bottom is $21M, positive, and one-fifth
of the top.** The range does not cross zero on any window of three years or more; the two
negative years are inside every window of four or more and pull the long means down to a
level the current business has not reported since 2022. This is the **fifteenth consecutive
run** to find the published width understated. The capex band is almost nothing here — D&A
and capex differ by $4M a year at most — so the whole width is the window, which is the
[E4-41] question and not a (c) question.

**`best_year_dep_oe 0.675` confirmed and understated in the usual way:** drop 2025 from the
seven-year OE series and the mean falls from $21.4M to **$7.2M** — 66% by the tool's
arithmetic; in words, **one year out of seven carries three-quarters of the seven-year
mean.** Whether that year is the new level or a spike is the question the receivables
analysis above answers: mostly the new level, roughly a third spike.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**The brief said Q1 is the file: gross versus net. It is, and the filing answers it in one
sentence, then quantifies it in a table.**

### Unit economics, in my own words, without management's language

A utility, an insurer, a city or a mortgage servicer sends out bills. The customer wants to
pay by card, by bank transfer, by PayPal, by text, at a kiosk, or by talking to a speaker in
the kitchen. **Paymentus is the plumbing between the biller's accounting system and every one
of those payment methods.** The biller integrates once; Paymentus takes the payment, clears
it through the card network or the ACH system, and reconciles it back into the biller's
ledger. **Paymentus is paid a fee per transaction** — either by the biller, who absorbs it,
or by the payer as a "convenience fee," or by a bank whose online bill-pay runs on the same
platform. No licence fee, no implementation fee, no subscription of any size (other revenue
was **0.8%** of the total in 2025). **724 million transactions in 2025 at $1.65 of revenue
each.**

### GROSS, NOT NET — and the fraction of a revenue dollar Paymentus keeps

The prior is confirmed by the filing, verbatim (FY2025 10-K, Note 3):

> *"The Company recognizes fees charged to customers **primarily on a gross basis** as
> transaction revenue when the Company is the principal in respect of completing a payment
> transaction. … The Company therefore bears full margin risk when completing a payment
> transaction, and on that basis, controls those services prior to being transferred to the
> customer. **The interchange fees charged by the card issuing financial institutions and
> the fees charged by the payment networks are recognized as transaction expense within cost
> of revenue.**"*

So reported revenue includes the interchange, assessment and network fees that Paymentus
passes to Visa, Mastercard and the ACH operators. **The company's own "contribution profit"
is revenue net of exactly those fees**, and it files the reconciliation in every vintage:

| $M | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | **2025** |
|---|---|---|---|---|---|---|---|
| **Revenue (gross)** | 235.8 | 301.8 | 395.5 | 497.0 | 614.5 | 871.7 | **1,196.5** |
| interchange, assessment, network fees *(cost of revenue less "other cost of revenue")* | 139.1 | 181.3 | 237.0 | 295.7 | 373.5 | 559.7 | **810.2** |
| **Contribution profit** *(the net top line)* | 96.7 | 120.5 | 158.5 | 201.3 | 240.9 | 312.1 | **386.3** |
| *as % of revenue* | **41.0%** | 39.9% | 40.1% | 40.5% | 39.2% | 35.8% | **32.3%** |
| other cost of revenue *(support, hosting, amortisation)* | 22.2 | 27.9 | 37.1 | 51.6 | 58.6 | 73.9 | 90.0 |
| **Gross profit** | 74.4 | 92.6 | 121.4 | 149.7 | 182.3 | 238.2 | **296.3** |
| *gross margin* | 31.6% | 30.7% | 30.7% | 30.1% | 29.7% | 27.3% | **24.8%** |
| Operating income | 18.4 | 18.4 | 10.4 | (3.0) | 18.1 | 44.9 | **75.5** |
| *operating margin on revenue* | 7.8% | 6.1% | 2.6% | (0.6%) | 2.9% | 5.1% | **6.3%** |
| *operating margin on contribution profit* | 19.0% | 15.3% | 6.5% | (1.5%) | 7.5% | 14.4% | **19.6%** |

*(Sources: FY2021 10-K for 2019–2021, then each 10-K's contribution-profit table; GP and
operating income from the filed income statements.)*

**THE ANSWER TO THE BRIEF'S QUESTION.** Of each dollar of Paymentus **revenue** in 2025,
**67.7 cents went to the card networks and banks, 32.3 cents was Paymentus's own top line,
24.8 cents survived the cost of serving the transaction, and 6.3 cents was operating
income.** Six years earlier the network share was 59.0 cents and the kept share 41.0 —
**Paymentus keeps a smaller fraction of every revenue dollar each year, and the filing says
why: *"Gross margin decreased as a result of a customer mix shift toward high-volume
enterprise billers."*** Per transaction: revenue $1.653, network fees $1.119, contribution
$0.534, gross profit $0.409, operating income $0.104.

**What cannot be answered, and why:** the brief asked what fraction of a *billed* dollar is
kept. **Paymentus does not file payment volume in dollars.** Recorded sweep of all five
10-Ks, the 424B4 and the Q2 2026 10-Q for "payment volume", "total payment volume" and
"TPV": no instance found. The bill amount is visible only through its shadow — the network
fees, which the MD&A says rise with *"the average transaction amount"* (hot summers, cold
winters, twice-yearly property taxes). The unit series that exists is transactions, and the
price series that exists is contribution profit per transaction; both are built at Q2.

**"Contribution profit" is a non-GAAP construct and the AMAT rule applies.** The company
files the split; the run uses it, because it is the honest top line for a principal that
passes 68 cents through. But it is also the denominator of the company's headline "adjusted
EBITDA margin" (a non-GAAP over a non-GAAP) and one of four bonus metrics, three of which
are non-GAAP — **[E4-29] is live from page 51 of the 10-K and is scored at Q3 against the
8-K releases**, as the brief required.

### The customer-funds question — answered, and the prior is refuted

The brief expected customer funds in transit to sit on the balance sheet and inside operating
cash flow, the way DFS flattered Dell's. **They do not.** FY2025 10-K, Note 2, verbatim:

> *"The Company has established a relationship with its merchant processors to act as
> collection and paying agents … These merchant processors act as custodians of the cash
> received, and **the Company has no legal ownership rights to the funds** held in such
> custodial accounts and does not control the use of these funds. As the Company does not
> take ownership of the funds, **these custodial accounts are not included in the Company's
> consolidated balance sheets.** The balance of cash in the custodial accounts held by these
> merchant processors was **$215.7 million and $147.2 million** as of December 31, 2025 and
> 2024, respectively."*

**Paymentus never touches the money.** PayPal's Braintree and the sponsor banks hold it; the
company's balance sheet carries $320.9M of its own cash, $3.6M of restricted deposits, and
no settlement asset or liability. Operating cash flow is therefore not flattered by float.
**What does move operating cash flow is receivables from billers and one reseller** — the
$60.8M swing shown above — and *"One reseller accounted for more than 10% of accounts
receivable for both December 31, 2025 and 2024"* (Note 2; the sentence first appears in the
FY2024 vintage). That reseller is not named; the warrant note identifies JPMorgan Chase as
the counterparty with *"minimum revenue commitments … for each of the calendar years through
2026"*, and the run treats the two as probably the same party without asserting it.

### The scarce input this business controls

**Not the rails** — Visa, Mastercard, the ACH network and PayPal's Braintree own those, and
take 68 cents of the dollar. **Not the software as such** — the filing gives its own
capitalised software a useful life of *"three to five years before being significantly
replaced or modified."* **The scarce thing is the biller's integration: the connection from
Paymentus into the biller's core billing and accounting system, configured once, with the
biller's customers' saved payment methods, autopay enrolments and notification preferences
attached to it.** Contracts run *"typically between three to five years"* and *"the majority
of customers may not terminate their contract early without penalty"* (Note 3). A utility
that has 400,000 households on autopay through Paymentus does not move them casually. That
is a real switching cost and it is the whole of the bull case; whether it is a franchise is
Q2's question, and the price series there is the test.

### Will the fundamentals look broadly the same in ten years?

**The mechanism will.** Bills will be paid electronically through somebody's plumbing, and
the biller will pay per transaction; that has been the model since the first lockbox. **The
split of the dollar will not necessarily look the same**, because the 68-cent pass-through
is set by parties Paymentus does not control — the filing says so twice: *"we do not control
the payment channel used by consumers, which is the primary determinant of the amount of
interchange"*, and *"our adjustments typically lag behind the impact of inflation on
clients, rising bill amounts and increased interchange fees. We may be unable to fully
adjust our pricing."* That is recorded here as the way the economics move and adjudicated at
Q2 as a pricing-power question.

**Q1 asks whether I can understand how the money is made, and I can, completely.** One
revenue line, one unit (the transaction), one filed net-of-network top line reconciled to the
dollar, one physical series published every quarter since the IPO, no customer funds on the
books, no debt, and a cash-flow statement whose every line I have traced. **The complexity
here is that reported revenue is two-thirds somebody else's money, and the company files the
table that strips it out.**

- **VERDICT: [x] IN**
  *Carried forward to Q2, not waived here: (a) contribution profit per transaction fell from
  $0.661 to $0.534 over six years while units rose 5x; (b) gross margin fell 6.8 points, and
  the filing attributes it to mix toward large billers; (c) the company says in Item 1 that
  it "compete[s] on pricing"; (d) the money leg is a pass-through the company does not
  control. Those four facts are the Q2 case and are decided there.*

