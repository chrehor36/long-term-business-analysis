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
10-Ks, the 424B4 and the Q2 2026 10-Q for "payment volume", "total payment volume", "TPV"
and "dollar volume": no dollar figure found in any vintage; the only instance with a number
is the prospectus's vertical mix (*"In 2020, 57% of our total dollar volume processed was in
utilities, 23% in financial institutions and 16% in insurance"*), and the phrase
"payment volumes" otherwise appears only in risk-factor prose. The bill amount is visible
only through its shadow — the network
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

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- **Needed or desired [x]** — unambiguously. Transactions **146.2M → 724.0M** in six years,
  consumers using the platform in December **16M → 53M**, billers **1,300 → 2,500** over the
  years the count was published. Utilities, insurers and governments are not being pushed;
  they are arriving.
- **No close substitute [ ] — FAILS, on the filed price series and on the company's own
  words.** Built below.
- **Not price-regulated [x]** — Paymentus's own fee is not regulated. *(Recorded, not waved
  away: the 68 cents of each revenue dollar that Paymentus passes through is administered by
  the card networks and, for debit, by the Durbin amendment; and convenience fees charged to
  payers of government and utility bills are constrained by state rules in several verticals.
  Neither regulates Paymentus's price; both bound the leg it does not control. A criterion
  (3) pass with the cost leg administered by someone else.)*

### **[E4-55] — WHERE UNITS EXIST, MONITOR UNITS. PAYMENTUS FILES THEM EVERY QUARTER, AND THE PRICE IT GETS PER UNIT HAS FALLEN 19% WHILE UNITS ROSE FIVEFOLD.**

*"Precision Steel's pounds fell 69M → 46M while price rises held dollar revenue level …
Dollar revenue flattered by pricing is how a shrinking franchise hides; the physical series
is the honest one."* — **[E4-55]**. Here the shape is the mirror image: **units are
honest and rising; dollar revenue is flattered by pass-through; and the price Paymentus
obtains for its own service per unit is falling.** Every figure from a filed KPI table or a
filed reconciliation (FY2021 10-K for 2019–2021; each subsequent 10-K; the Q2 2026 10-Q for
the half-years):

| year | **transactions (M)** | growth | revenue / tx | network fees / tx | **contribution profit / tx** | change | gross margin |
|---|---|---|---|---|---|---|---|
| 2019 | 146.2 | — | $1.613 | $0.951 | **$0.661** | — | 31.6% |
| 2020 | 195.0 | +33.4% | $1.548 | $0.930 | $0.618 | −6.5% | 30.7% |
| 2021 | 280.5 | **+43.8%** | $1.410 | $0.845 | $0.565 | −8.6% | 30.7% |
| 2022 | 366.8 | +30.8% | $1.355 | $0.806 | $0.549 | −2.8% | 30.1% |
| 2023 | 458.2 | +24.9% | $1.341 | $0.815 | $0.526 | −4.2% | 29.7% |
| 2024 | 597.0 | +30.3% | $1.460 | $0.938 | $0.523 | −0.6% | 27.3% |
| **2025** | **724.0** | **+21.3%** | **$1.653** | **$1.119** | **$0.534** | +2.1% | **24.8%** |
| H1 2025 | 349.0 | — | $1.591 | $1.072 | $0.519 | — | 24.8% |
| **H1 2026** | **416.8** | **+19.4%** | $1.725 | $1.179 | **$0.547** | +5.4% | 25.1% |

*(Quarterly transaction growth from the releases: 2025 Q1 +28.0%, Q2 +25.2%, Q3 +17.4%, Q4
+16.1%; 2026 Q1 +17.4%, Q2 +21.4%.)*

**Three readings, and they are the whole of the gate.**

1. **Units up 4.95x; the price Paymentus receives for its own service per unit down 19.2%**
   ($0.661 → $0.534), falling in five of six years. **Revenue per transaction rose 2.5%
   over the same span only because the pass-through rose 17.7%** — bigger bills carry more
   interchange. FY2025's 37.3% revenue growth on 21.3% unit growth is sixteen points of
   somebody else's money.
2. **The company said the same sentence four years running.** FY2021 10-K: *"contribution
   profit increased at a slower rate than transactions due to continued onboarding of larger
   clients."* FY2022: *"due to a continued mix shift to larger, high volume clients."*
   FY2023 and FY2024: *"For 2022 and 2023 [2023 and 2024], contribution profit increased at
   a slower rate than transactions processed due to a continued mix shift to larger, high
   volume clients."* **Four consecutive annual reports in which the filer explains that its
   unit price fell because its customers got bigger.** That is the PayPal/Block/Adyen
   mechanism from the SHOP run's payments leg, named by the subject about itself.
3. **The 2025–H1 2026 uptick (+2.1%, +5.4%) is real and is recorded at full strength
   [E4-26].** It coincides with the FY2023 MD&A's *"pricing improvements from customers
   related to our inflation management"* annualising, and with the enterprise mix
   stabilising. It recovers **one-fifth** of the six-year decline. It is the counter-fact,
   and it is not enough to make the series say the opposite of what it says.

### **[E2-44] — BOTH HALVES, RUN ON THE FILED SERIES**

*Can it raise prices "even when product demand is flat and capacity is not fully utilized",
and grow dollar volume "with only minor additional investment of capital"?*

**HALF TWO — CAPITAL — PASSES OUTRIGHT AND IS THE BEST FACT IN THE FILE.** Capital spending
(PP&E plus capitalised software) was **$37.1M on $1,196.5M of revenue — 3.1% — or 9.6% of
contribution profit**; net property and equipment is **$0.9M**; cash is $320.9M at year-end
and **$377.7M at 2026-06-30** with no debt of any kind. Transactions grew 4.95x on $150M of
cumulative capital spending. Paymentus can double its unit volume without buying anything
but engineers' time.

**HALF ONE — PRICE — FAILS, AND THE FILER SAYS SO IN ITS OWN VOICE.** Demand is not flat, so
the strict test cannot be run; what can be run is whether the company raises its price when
it wants to. The one price action in seven filings is the 2023 *"pricing improvements from
customers related to our inflation management"* — a recovery of interchange inflation, not
a rise in the company's own fee — and the filing describes how it went:

> *"We may be unable to fully adjust our pricing to address these pressures, and **our
> adjustments typically lag behind** the impact of inflation on clients, rising bill amounts
> and increased interchange fees."* — FY2025 10-K, Item 7

> *"**We also compete on pricing**, particularly in certain lower-margin industries where
> lower cost pricing can outweigh higher product quality and an enhanced customer
> experience."* — FY2025 10-K, Item 1, "Competition" (the sentence appears in every 10-K
> from FY2022)

**[E4-37]'s inverse metric** — *"you can almost measure the strength of a business over time
by the agony they go through in determining whether a price increase can be sustained"* —
returns a company that needed inflation as the occasion, lagged it, and could not fully
recover it. *"it's not a great business when you have to have a prayer session before you
raise your prices a penny."*

### THE COMPETITOR ROW — required **[E3-28]**

*Working: `Test Runs/_research 2026-09-11 PAY/competitor_row_raw.md` and `peers.py`; each
figure carries its accession; FY2025 unless stated; JKHY and BILL are June year-ends and
their FY2025 figures are the comparatives carried in the FY2026 10-Ks named.*

**Who the competitors are, from a filer, not from me.** Paymentus names nobody: its
competition section speaks of *"legacy solution providers and systems internally developed
by financial institutions."* **ACI Worldwide's FY2025 10-K names the industry in one
sentence:** *"The primary competitors for our bill payments solution include **Alacriti, FIS,
Fiserv, InvoiceCloud, Kubra, One Inc., Paymentus, PayNearMe, Repay**, as well as smaller
vertical-specific providers."* Nine names. **Public and in the row: Fiserv, FIS, ACI
Worldwide, Repay, Paymentus. Private and unreachable on any rung: Alacriti, Kubra (Hearst),
One Inc., PayNearMe. InvoiceCloud is EngageSmart, taken private by Vista in January 2024;
its last 10-K is FY2022 and is carried below, italicised and three years stale.** Jack Henry,
Flywire and Bill.com were the brief's names and are kept as adjacent comparators (bank bill
pay; education/healthcare payments; SMB AP/AR). **Peers named: 8 of the industry's roughly
12, four of them private and named as a hard limit.**

| FY2025, filing-sourced | **PAY** | Fiserv | FIS | ACIW | RPAY | JKHY | FLYW | BILL | *ESMT FY2022* |
|---|---|---|---|---|---|---|---|---|---|
| Revenue $M | **1,196.5** | 21,193 | 10,677 | 1,759.8 | 309.3 | 2,375.3 | 623.0 | 1,462.6 | *303.9* |
| Revenue growth | **+37.3%** | +3.6% | +5.4% | +10.4% | (1.2)% | +7.2% | +26.6% | +13.4% | *+40.5%* |
| Gross margin *(presentation differs, see note)* | **24.8%** | n/a | 36.9% | 49.0% | 75.0% | 42.7% | n/a | 81.4% | *76.4%* |
| **GAAP operating margin** | **6.3%** *(19.6% on contribution profit)* | **27.5%** | 16.3% | 18.7% | (82.4)% ¹ | 23.9% | 1.8% | (5.5)% | *5.4%* |
| **SBC ÷ operating cash flow** | **11.5%** | 5.9% | 6.9% | 21.9% | 20.1% | 4.4% | 71.7% | 69.2% | *27.1%* |
| Capital spending (PP&E + software) ÷ revenue | 3.1% | 8.3% | 9.3% | 0.7% | 13.5% | 9.5% | 0.2% | 2.6% | *2.1%* |
| **Owner earnings (OCF − SBC − capex − software) $M** | **106.4** | 3,942 | 1,438 | 239.3 | 31.0 | 387.3 | 27.0 | 70.0 | *31.6* |
| Net cash (debt) $M | **+320.9** | (n/a, levered) | (9,754) | (621) | (164) | n/a | +330.3 | (676) | *+311.8* |
| Goodwill $M | 131.8 | 37,703 | 17,762 | 1,231 | 475 | 805 | 407 | 2,397 | *426* |
| **Names Paymentus in its own 10-K?** | — | **NO** | **NO** | **YES** | **YES** | NO | NO | NO | *NO* |

*Notes. FIS operating cash flow is the continuing-operations line. Gross margins are not
comparable across the row and are shown only to say so: Paymentus presents interchange gross
(Q1); Fiserv reports no cost-of-revenue line; BILL and Flywire net most network cost out of
revenue. The comparable rows are operating margin, SBC/OCF and owner earnings. ¹ Repay's
FY2025 operating loss of $254.7M on $309.3M of revenue is an impairment year (accession
`0001193125-26-098518`); its cash figures are the comparable ones.*

**THE LOAD-BEARING COMPARATOR FACTS.**

- **On the one net measure that is comparable — GAAP operating margin — Paymentus at 6.3%
  is sixth of eight**, ahead only of Flywire and BILL, which are SBC-funded growth companies
  with 70% SBC/OCF. **On its own net top line it is 19.6%, which is the ACI Worldwide number
  (18.7%) and below Jack Henry (23.9%) and Fiserv (27.5%)** — the "legacy solution
  providers" its competition section says are slow and expensive earn more per dollar of net
  revenue than the challenger does, after twenty years of the challenger's existence.
- **The two filers that name Paymentus each name it in a list.** ACI Worldwide: eighth of
  nine. Repay (FY2025 10-K, `0001193125-26-098518`): *"In our Consumer Payments segment, our
  primary competitors include ACI Worldwide, Payliace, Paymentus, PayNearMe, PayScout and
  TabaPay"* — third of six, and **Repay took a $254.7M goodwill impairment on that very
  segment in 2025**, citing *"the decrease to comparable publicly traded companies'
  multiples."* The PINS run's reverse attacker's test: at CrowdStrike every pure-play peer
  named the subject and the subject named nobody. Here the subject names nobody, two of
  eight peers name it, both inside lists of private companies, and the two largest, Fiserv
  and FIS, do not consider Paymentus worth a sentence. **The industry's filed view of
  Paymentus is: one of nine, and the segment it competes in was just written down by a
  peer.**
- **The closest pure comparator, InvoiceCloud, was growing faster than Paymentus (40.5% vs
  25.7% in 2022) when last seen.** EngageSmart's FY2022 10-K, the last it filed, shows the
  same shape — sub-10% operating margin, net cash, capital-light — and it was worth taking
  private. That is the [E2-45] attacker's test answered by history: an attacker with
  capital and personnel built the same thing in the same verticals and grew faster.
- **[E3-46] — "the best businesses … earn very high returns on capital employed over time."
  Stated both ways, because the two denominators disagree.** On [E2-43]'s unleveraged net
  tangible operating capital Paymentus earns **roughly 82% pre-tax** — total assets $667.9M
  less cash $320.9M, restricted cash $3.6M, goodwill $131.8M and intangibles $12.0M leaves
  $199.6M, less $107.5M of non-interest-bearing operating liabilities leaves **$92.1M**,
  against $75.5M of operating income. Including the $143.8M of goodwill and intangibles it
  is 32%. **That is a genuinely high number, and it is high for the PINS reason: the
  denominator is almost nothing.** On the metric that says whether anything is being
  *protected* — operating margin on net revenue in an industry where the incumbents earn
  24–28% — Paymentus earns 19.6% and its gross margin has fallen every year for six years.
  A business earning 82% on $92M of capital and 6% on its revenue is not being shielded
  from competition; it is being competed with, on a very small asset base.

**[E3-61] — the row's limit.** Identical structures produce opposite outcomes and the row
cannot show conduct. What it shows is position: a challenger with the fastest unit growth in
the row, the lowest per-unit price trend, a net margin at the industry's middle, and no
filer naming it as the one to beat.

### THE OTHER Q2 TESTS

- **[E4-04] — must the moat be continuously rebuilt, and does success depend on a great
  manager?** The platform is rebuilt continuously by construction: capitalised software runs
  $37M a year on a life the filing gives as *"three to five years before being significantly
  replaced or modified."* That spending defends the same advantage (the integrations),
  not a replacement, so it is not the excluded class on its own. **The manager clause fires
  and is recorded HERE as a moat defect, not at Q3 as a strength [E4-23]:** *"Our founder,
  chairman, president and chief executive officer, Dushyant Sharma, is critical to overall
  management, product development, partnerships, culture and strategic direction"* (Item 1A).
  The company's own charter converts his Class B nine months after his death. *"The
  partnership's moat will go when the surgeon goes."*
- **[E4-36] — which cause of extreme success?** **Wave-riding [E3-51].** The prospectus
  states the wave: bank-based bill pay fell to *"22% in 2020"* of online consumer bill
  payment as payers moved to biller-direct electronic channels. Paymentus caught that wave
  in 2004 and has stayed on it; the record is *"when a surfer gets up and catches the wave
  and just stays there, he can go a long, long time."* A surfing run is not a moat; the
  advantage lives in the wave, and there are nine surfers on it by ACI's count.
- **[E2-53] — the dominance class?** No. A dominant provider does not write *"we also
  compete on pricing"* into Item 1 four years running.
- **[E2-45] — the attacker's test.** With ample capital and skilled personnel: build a
  modern single-code-base bill-pay platform, price the low-margin verticals below Paymentus,
  and sign the resellers. InvoiceCloud did the first two from 2009; the resellers are the
  open question and the strongest fact against this verdict (below).
- **[E3-33] / [E5-28] — untapped pricing power?** Claiming it is claiming near-monopoly;
  the filer says it competes on price and lags its own cost inflation. **Refused.**
- **[E4-32] — direction.** Units: widening (+21%, +19%). Price per unit: −19% in six
  years, +5% in the latest half. Gross margin: down 6.8 points in six years, up 0.3 in the
  latest half. **The moat's direction on the series that measures the moat is narrowing,
  with the most recent half flat.**

### **[E2-49] — METRIC-SWITCHING. THE OPERATOR'S PRIOR (WRONG FOUR TIMES, RIGHT ONCE) IS RIGHT A SECOND TIME, AND THE INSTRUMENT THE BRIEF HOPED FOR DOES NOT EXIST.**

**Net revenue retention: never filed.** Recorded sweep of the 424B4, all five 10-Ks and the
Q2 2026 10-Q for "net revenue retention", "dollar-based", "retention rate" and "churn": **no
instance found in any vintage.** The brief's instrument for withdrawal-testing is absent
from the record, which is itself a [E2-26] fact: a company with three-to-five-year contracts
that does not tell owners how many renew.

**The biller count: published for five vintages, withdrawn in the sixth.**

| filing | biller count | the sentence |
|---|---|---|
| 424B4 (May 2021) | **1,300** | *"a network of more than 1,300 billers as of December 31, 2020"* |
| FY2021 10-K | **1,700** | *"more than 1,700 billers"* |
| FY2022 10-K | **1,900** | *"more than 1,900 billers"* |
| FY2023 10-K | **2,200** | *"more than 2,200 billers"* |
| FY2024 10-K | **2,500** | *"more than 2,500 billers"* |
| **FY2025 10-K** | **NONE** | the only quantity is *"tens of thousands of billers"* reached through IPN partners |
| Q2 2026 10-Q | NONE | — |

**The count grew 31%, 12%, 16%, 14% and then disappeared.** It was not deteriorating; it was
growing at half the rate of transactions, which is the arithmetic of the enterprise mix
shift the margin story already tells (the average biller is getting bigger and paying less
per transaction). No reason is given for the withdrawal; the FY2025 10-K replaced a specific
number with a vaguer, larger one. **Fires as a prompt; read, it is consistent with the price
series rather than contradicting it.** The vertical mix (*"57% of our total dollar volume …
in utilities"*) appeared once, in the prospectus, and never again.

**The metrics that stayed:** transactions processed, contribution profit, adjusted gross
profit, adjusted EBITDA and free cash flow have been the KPI set in every 10-K since the
first, with one change to the adjusted-EBITDA definition (FY2023, adding foreign-exchange
and capitalised-software amortisation exclusions, disclosed). The consumers-in-December
count (16M → 53M) has never been withdrawn. **Two withdrawn, five kept, one never given.**

**Concentration:** *"No customer accounted for more than 10% of revenue"* in every vintage;
*"One reseller accounted for more than 10% of accounts receivable"* in FY2024 and FY2025 —
the reseller channel, not any biller, is the concentration. The largest-biller rebid risk
the brief raised is real but unquantifiable from the filings: no top-ten share is given.

### THE STRONGEST FACTS AGAINST THIS VERDICT, STATED BETTER THAN THE BULL WOULD **[E4-51]**

1. **JPMorgan Chase, U.S. Bank and PayPal chose to resell Paymentus rather than build.** The
   FY2025 10-K names all three as strategic partners who *"refer new billers to our platform,
   and in many cases, we jointly sell"*; JPM Chase signed *"minimum revenue commitments … for
   each of the calendar years through 2026"* and took warrants on 1.19M shares to do it. When
   the largest bank in the country puts its bill-pay customers on your platform and commits
   to minimums, that is a statement about substitutes.
2. **Contracts are three to five years and *"the majority of customers may not terminate
   their contract early without penalty"*** (Note 3), with no customer over 10% of revenue.
   The installed base does not leave between renewals, and units have compounded at 30% for
   six years.
3. **Contribution profit per transaction has risen for four consecutive half-years** — the
   decline may have ended in 2024 at $0.52.
4. **Operating margin on net revenue went from 7.5% (2023) to 19.6% (2025)** — the operating
   leverage is real and the company has only just crossed $1bn of gross revenue.

**Why they do not carry the gate.** (1) is evidence that the platform is *good*, and it is
also evidence that the reseller, not Paymentus, holds the customer relationship — the
company paid JPM in warrants and revenue-share for the privilege, and the reseller is the
one party over 10% of receivables. (2) says the customer is locked for a term; [E3-03](2)
asks what the customer *thinks* at the next RFP, and the answer is in the price series and
in *"we also compete on pricing."* (3) is one-fifth of a six-year decline and its cause is
the pass-through of cost inflation, not a rise in the fee. (4) is operating leverage on a
falling gross margin — the scale economics of a cost structure, which the corpus explicitly
distinguishes from a franchise: *"a business, unlike a franchise, can be killed by poor
management"* **[E3-43]**, and this one's filing says its founder is critical.

- Class: [ ] WIDE [ ] NARROW [x] **NONE** on criterion (2) *(a switching cost on the
  installed base, priced away at the RFP; the PROVISIONAL label is not taken — four peers
  are private and unreachable on any rung, the five that file were pulled, and the verdict
  rests on the subject's own filed price series, not on a peer figure)* · Direction: **narrowing
  on price for six years, flat in the latest half; widening on units**
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**OUT on [E3-03] criterion (2): the customer has a close substitute, the filer says it
competes on price, and the price the filer receives per unit of its own service fell 19% in
six years while units rose fivefold.** Not UNRESEARCHED: the document that would resolve
this is the filed unit-and-price series, and it is in hand for seven years. Not UNKNOWABLE:
the future of the *industry* is indeterminate, but the question is whether the customer has
a substitute today, and the filer's own competition section answers it. **This is a
business, and by the filed numbers a good one [E4-43] — capital-light, net cash, 82% on
tangible capital, 30% unit growth — and the framework says good ranks below great at Q5,
not that good fails Q2. What fails here is the specific claim of no close substitute, which
is the claim a franchise makes and which this filer does not make about itself.**

*Q3 and Q4 do not open. The findings gathered for them are recorded below for the register
under the operator protocol's heading, because the brief asked for them and because the
register is for the next reader, not for this verdict.*

---
⛔ **The file closed at Q2. Q3, Q4, Q5 and Q6 do not open.** What follows is recorded for
the register because the brief asked for it and the next reader will want it; none of it is
a verdict and none of it promotes the name (operator protocol rules 2 and 3).

---
## RECORDED FOR THE REGISTER — Q3 MATERIAL, GATHERED AND NOT ADJUDICATED

**The weight case that would have applied.** Daily execution [E3-38] would be ticked:
payment processing is a have-to-be-smart-every-day business (uptime, PCI, fraud, settlement
through third parties). No leverage [E3-29], no control [E1-16]. Q3 would have been a binary
gate. Recorded so the next reader does not treat it as an overlay.

**The two share classes, and who holds the votes.** Decided at Step 0: economically
identical, summed. The governance fact: Class B carries ten votes, AKKR holds **58.2%** of
the voting power on 33.8% of the economics and the founder **31.3%** on 18.1%; together
**89.5% of the votes on 52% of the shares** (DEF 14A 2026, as of 2026-04-09). The company
is a *"controlled company"* under NYSE rules and says so; AKKR nominates five directors
while it holds 10% and *"will be able to determine the outcome of all matters requiring
stockholder approval"* (Item 1A). The 10-K adds: *"we are subject to pressure from certain
institutional investors to sunset our dual-class structure."* **The sponsor is leaving:**
roughly 27M Class B shares converted to Class A in H2 2025 as AKKR sold, an AKKR-nominated
director resigned in July 2026 and was replaced by another AKKR managing director the same
day (8-K 2026-07-23). Two related-party employments are disclosed: the CEO's spouse is a
vice president ($0.3M a year) and a director's son is a vice president ($0.5M cash plus
$0.4M of RSUs a year, $1.1M of RSUs in 2023) — Note 15.

**[E4-29] — scored against the 8-K EX-99.1, as the brief and the CGNX rule require. It fires
at full strength, and the mechanism is a non-GAAP over a non-GAAP.** The 10-K carries
adjusted EBITDA as a KPI on page 51. The releases headline it: Q2 2026, *"Adjusted EBITDA up
54.0% year-over-year, with a record adjusted EBITDA margin 41.3%"*; Q1 2026 *"record 38.7%"*;
Q3 2025 *"record 36.5%"*. **The definition:** *"Adjusted EBITDA margin is defined as
adjusted EBITDA as a percentage of contribution profit"* — the numerator excludes SBC, D&A
and capitalised-software amortisation, and the denominator excludes the 68 cents of network
fees. **On GAAP revenue the same quarter's adjusted EBITDA margin is 13.5%; the GAAP net
margin is 7.1%.** The company also *"does not reconcile its forward-looking guidance for
non-GAAP measures"* and guides only on revenue, contribution profit and adjusted EBITDA.
**And the pay plan runs on it:** the 2025 and 2026 bonus programs weight revenue,
contribution profit, adjusted EBITDA and *"Adjusted EBITDA less capitalized software"*
equally — three of four non-GAAP (8-Ks 2025-03-19 and 2026-03-13; DEF 14A 2026). The
depreciation the corpus calls *"reverse float"* [E5-41] is $41M a year here, 99% of it
software the company spent cash to build; the headline metric deletes it.

**[E4-22] third flag and [E3-48] — the guidance record, eight releases.** FY2025 was guided
in March 2025 at revenue **$1,040–1,060M**, contribution profit **$358–366M**, adjusted
EBITDA **$112–116M**; raised in May, August and November; delivered **$1,196.5M / $386.3M /
$137.4M** — 13–15%, 6–8% and 18–23% above the initial guide. FY2024's November guide of
$829–834M was beaten by 4.5% with seven weeks left in the year. FY2026 was guided in
February at $1,390–1,410M and has been raised twice since. **Eight consecutive releases,
each beating and raising.** The corpus's reading is that a company that always makes the
numbers is managing the numbers [E4-22], and that the habit is a ratchet [E5-30]; the base
rate for projections is *"about nine cases out of ten"* [E3-48]. Not adjudicated.

**[E4-52] — the flags converge.** Non-GAAP headline + non-GAAP pay metrics + guide-and-beat
+ a compensation consultant (Compensia) recommending a **one-time RSU grant of 1,100,000
shares, grant-date fair value $34,232,000 (July 2025)**, to a founder who owns 18% of the
company, *"to address the fact that he had not previously been awarded any RSUs"*, followed
by **480,000 more RSUs in April 2026** and a **discretionary bonus of 20% on top of the
formula payout** *"in recognition of … revenue exceeding $1 billion"*. *"During 2025, we
did not grant any performance-based equity awards or stock options."* No pay ratio is
disclosed (EGC exemption through FY2025). Several flags pointing one way are one system
[E4-52]; recorded as such, not scored.

**Serial issuance [E5-15] — does not fire on the company.** No equity issued since the IPO
beyond option exercises; RSU vesting is net-settled with $10.7M of taxes withheld in 2025;
no buyback ever. The 4% annual evergreen addition to the equity plan is the standing dilution
mechanism (25.5M shares available at 2025-12-31). Dividends [E2-52]: none.

**[E4-30] — the filed-figure tells.** Reported growth is not unnaturally smooth (revenue
+27%, +26%, +24%, +42%, +37%). Cash taxes as a share of pretax income: 24.0% (2021), n/m
(2022), 5.6% (2023), 26.7% (2024), **17.5% (2025)** — the 2025 fall is explained in the
filing by the 2025 restoration of immediate deduction for domestic R&D. Not a tell, read.

**[E4-34] — the auditor's-eye items.** The reserve for credit adjustments, recorded as a
reduction of revenue, rose from **$1.0M to $8.9M** in 2025 (Note 3) with no explanation
beyond the policy — an 8.9x rise on 37% revenue growth, in the conservative direction. The
critical audit matter is payment-transaction revenue recognition. Auditor PwC, unchanged.

**Institutional imperative [E2-30]:** (2) — the $378M of cash has not been soaked up; no
acquisition since 2022. Not scored.

---
## RECORDED FOR THE REGISTER — Q4 MATERIAL, GATHERED AND NOT ADJUDICATED

**SBC ÷ operating cash flow, cross-checked to the dollar (Step 0), placed in the calibrated
row:** FY2025 **11.5%** (18,627 ÷ 162,127); on the total expense including the capitalised
portion 12.8%; FY2024 17.3%; three-year 13.2%; H1 2026 15.3%. **The row now runs CRWD 68.0%
(closed the file) · PINS 68.6% · QLYS 24.9% (cleared) · CRM 23.4% · SHOP 22.1% · PAY 11.5%
— the lowest SBC burden of any name calibrated so far**, and the only one under 20%. In the
competitor row only Fiserv (5.9%), FIS (6.9%) and Jack Henry (4.4%) are lower. SBC at
$18.6M is a full subtraction [E5-06]; the reported charge is the floor of the measure
[E3-70] and the run notes that 1,340 employees receive $14k of stock each on average.

**Customer funds in transit — the prior refuted at Q1.** Off balance sheet, held by PayPal's
Braintree and the sponsor banks as custodians ($215.7M at 2025-12-31); operating cash flow
is not flattered by float. What moves OCF is receivables (the $60.8M swing), which is where
the reseller concentration lives.

**Staying power [E5-11], had it been scored:** (1) a reliable stream — contribution profit
has grown every year 2019–2025 through a pandemic and an inflation cycle; (2) liquid assets
— **$377.7M cash at 2026-06-30, zero debt, no bank lines counted or mentioned** [E5-39];
(3) near-term cash requirements — none: leases $8.3M, contract liabilities $6.6M, no
holdbacks outstanding. Leverage [E4-16]: none. Coverage [E2-54]: no interest to cover.

**Great, good or gruesome [E4-20]:** by the filed figures, **good** — 82% pre-tax on
tangible operating capital, 30% unit growth financed from operations, net cash rising every
year. Not gruesome; not great, for the Q2 reason.

**The way it would die, named for the register:** the enterprise mix shift continues and the
reseller channel grows — contribution profit per transaction resumes its 2019–2024 decline
at ~5% a year while units grow ~20%, so net revenue grows ~14% and the operating leverage
that took the CP-margin from 7.5% to 19.6% stalls; or a reseller with revenue minimums
(JPMorgan Chase's commitments run *"through 2026"*) renegotiates at renewal. Quantified: a
return of CP/transaction to the 2024 low of $0.523 on 2025 units removes $8M of
contribution profit; a further 10% mix decline removes $39M, roughly half of operating
income. A real possibility, not a likelihood, on the filed series. Not adjudicated.

---
## COMPUTATION — NOT A CLEARANCE
*Headed as the protocol requires. Q1–Q4 have not all closed IN; this carries no entry
language and casts no vote. It exists so the register shows where the price sat.*

- Market cap **$4,569M** ($36.28 × 125,939,647; 2026-09-10; aggregator, flagged).
- Sovereign **5.37%** (US Treasury 30-yr, 2026-09-10).

| owner-earnings construction | OE $M | yield on cap | points vs bond | value at the bare bond (OE ÷ 5.37%) | per share |
|---|---|---|---|---|---|
| 7-year mean, capex end | 21.4 | 0.47% | −4.90 | $400M | ~$3 |
| 5-year mean (published `oe_bottom`) | 25.2 | 0.55% | −4.82 | $470M | ~$4 |
| **3-year mean (the years this run believes)** | **49.2** | **1.08%** | **−4.29** | **$916M** | **~$7** |
| 2-year mean | 61.2 | 1.34% | −4.03 | $1,140M | ~$9 |
| 1-year (2025, part working capital) | 106.4 | 2.33% | −3.04 | $1,981M | ~$16 |

- **Zero-growth value at the bare sovereign: roughly $4 to $16 a share** across the
  multi-year-to-one-year constructions, **against a price of $36.28**; at the ~10% floor
  [E4-28], **roughly $2 to $8**. The price is 2.3x the top of the range and 9x the bottom.
- **What the price assumes:** at the three-year mean, `tools/run.py`'s year-1 growth figure
  is **~27%** at a 5.37% rate; the business's net top line has grown 20–30% and its units
  21%. The expectancy test, run the SHOP way: from the **one-year** figure of $106M, **25%
  owner-earnings growth for ten years** and a sale at the bond yield returns roughly 15% a
  year to the buyer at $36.28; from the **three-year** mean at the same 25%, roughly 6%;
  from a $110M run-rate at 20% for ten years, roughly 10.7% — the floor, exactly, on a
  decade of growth the corpus rates at fewer than one in twenty among the best businesses
  [E4-35]. **The only path over the floor runs through the single best year and a decade of
  20%+; every multi-year construction is quit on.** Bar 2 outcome: price above the whole
  range → no. Windage count: zero — no margin was applied because nothing was cleared.

---
## Q3 — Q6: NOT OPENED
- **Q3 VERDICT: not opened** (Q2 OUT). · **Q4 VERDICT: not opened.** · **Q5 VERDICT: not
  opened** — see COMPUTATION above. · **Q6 VERDICT: not opened.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped — Q1 IN, Q2 OUT, file closed
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — Q1's
      four carried-forward items are facts, decided at Q2
- [x] Every UNRESEARCHED verdict names the artifact — none issued
- [x] Every UNKNOWABLE verdict states what cannot be known — none issued
- [x] Step 0: the filing was read, with accession numbers; four figures cross-checked
- [x] Owner earnings on a multi-year mean; windows stated (3y believed, 5y carried, all
      seven shown); capex band disclosed as a judgment (D&A vs capex-plus-software, $4M apart)
- [x] Competitor row filled: 8 named, 4 private named as a hard limit, two peers name the
      subject; moat class NONE, not PROVISIONAL, on the subject's own filed series
- [x] Sovereign is for the earnings currency (USD), from the issuing authority, dated
- [x] Value stated as a round-number range, and only under the COMPUTATION heading
- [x] One bar chosen (Bar 2, in computation only); windage count stated (zero)
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] Run committed to git after Step 0/Q1 and after Q2; this section committed with the fold
- [x] Absence claims carry their sweeps: payment volume in dollars (7 filings); net revenue
      retention (7 filings); biller count (7 filings); "Paymentus" in eight peer 10-Ks
- [x] Run files keep em dashes (ruled 2026-09-01)

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- One line: **Paymentus is a good, capital-light, net-cash bill-payment platform whose
  reported revenue is two-thirds card-network pass-through, whose own price per transaction
  fell 19% in six years while units rose fivefold, and whose filing says it competes on
  price — a business, not a franchise; and at $36.28 the price is 2.3x to 9x the zero-growth
  value at the bond in any case.**
- **Reversal condition, in words (no price alert — the failure is on the business, the QLYS
  ruling):** the file reopens if contribution profit per transaction rises for three
  consecutive fiscal years on a rising or flat gross margin, or if a filing shows a fee
  increase taken and held without an interchange-inflation pretext. The Q2 2026 half is the
  first data point (+5.4% on a flat margin); one half is not a series.
- **Priors refuted:** (1) customer funds do NOT sit on the balance sheet or in OCF — the
  DFS/Dell mechanism does not exist here; (2) net revenue retention is not filed in any
  vintage, so the instrument the brief named cannot be run; (3) the IPO year is not the
  break — the owner-earnings sign change is 2021–2022 and its cause is capitalised software
  ramping against a flat OCF, and the 2025 step is one-third receivables swing; (4) the
  screen's cap was the pre-IPO count, not merely stale; (5) SBC/OCF is the lowest in the
  calibrated row, not a file-closer. **Priors confirmed:** gross revenue recognition; the
  reseller-spread mechanism (via contribution profit per transaction rather than a take rate
  on volume, which is not filed); [E2-49] fires (biller count withdrawn); [E4-29] fires in
  the releases and the pay plan; the share classes are economically equivalent.
- **Strongest single fact against the conclusion:** JPMorgan Chase, U.S. Bank and PayPal
  resell the platform rather than build one, and JPM signed revenue minimums through 2026
  and took warrants to do it — the largest bank in the country judged Paymentus the
  substitute-less choice for its own bill-pay customers. Recorded at full strength; answered
  in Q2.
- **Defects in the brief:** the "fraction of a billed dollar" cannot be computed because
  payment volume in dollars is not filed — the answerable question is the fraction of a
  *revenue* dollar (32.3 cents kept, 24.8 after serving cost); the brief's NRR instrument
  does not exist for this filer; the brief's "IPO'd in 2021 … averaging a cash-consuming
  company" framing is the PINS shape only loosely — Paymentus was cash-generating before
  the IPO and the negative years are an investment ramp, not pre-monetisation.
- **Defects in the tooling:** (1) `regen_queue`/`floor_screen` priced PAY on the pre-IPO
  2020-12-31 `CommonStockSharesOutstanding` (seventh instance; cap understated 20.4%; the
  550-day staleness guard did not fire because the FY2021 10-K re-tagged that same 2020
  value in 2022, resetting the clock on a five-year-old number); (2) `tools/run.py` used the
  larger SBC tag (`AllocatedShareBasedCompensationExpense`, which includes SBC capitalised
  into software) and so double-counts ~$2M against the capital line it also subtracts;
  (3) `tools/run.py`'s share basis fell to the diluted weighted average (129.1M) rather than
  refusing — a 2.5% cap error that happened to be smaller than the queue's; (4) `S.cik_for`
  returns `(None, None)` for Fiserv's current ticker FI (the SEC map still says FISV) and
  for delisted EngageSmart — a peer-row builder needs a CIK override path.
