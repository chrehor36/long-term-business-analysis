# Company Run - United Airlines Holdings, Inc. (UAL) - 2026-09-02
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS - every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order - not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation - it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 - THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** - the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.27** % · date **2026-09-01** · source **US Treasury daily par yield curve, 30-year
  constant maturity, from the issuing authority** (`home.treasury.gov/.../daily-treasury-rates.csv/2026/all`;
  copy saved at `Test Runs/_research 2026-09-02 UAL/` and `tools/_cache/UAL_TREASURY_2026.csv`).
  2026-09-01 is the latest published business day as of this run.
- FX: none. UAL earns in USD and quotes in USD. No ADR ratio.
- **TOOL DEFECT LOGGED.** `tools/sources.py` still names **FRED DGS30** as the USD source.
  `CLAUDE.md` was corrected on 2026-09-02 to make the **US Treasury daily par yield curve** the
  source and FRED the *fallback*. `tools/run.py` calls `sources.sovereign()` and therefore
  violates operator rule 5 as written. In this run the FRED call **timed out** and the
  Treasury curve was fetched directly, which is UP the evidence ladder. Detail in the
  DEFECTS section at the foot of this file.

**Price** - aggregator, live quote only, flagged: **$108.606**, 2026-09-02 (Stooq via
`tools/sources.py:price`). Shares outstanding **324,583,772**, cover page of the 10-Q for the
quarter ended 2026-06-30, dated **2026-07-09** (dei:EntityCommonStockSharesOutstanding).
**Market capitalisation $35,252M.**

**The filing was read** - not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes (Notes 10, 11, 12, 13,
  15 and the significant-accounting-policies note)
- document · date · accession no.: **UAL Form 10-K for fiscal year ended 2025-12-31, filed
  2026-02-12, accession 0000100517-26-000023**, primary document `ual-20251231.htm`. Also
  read: DEF 14A filed **2026-04-07**, accession 0001104659-26-040467, for the pay-versus-
  performance and incentive-metric work at Q3.
- figure cross-checked against the filed statement: **unrestricted cash, cash equivalents and
  short-term investments.** The MD&A liquidity paragraph states "$12.2 billion in unrestricted
  cash, cash equivalents and short-term investments" at 2025-12-31. The filed balance sheet
  carries cash and cash equivalents **$5,942M** plus short-term investments **$6,298M** =
  **$12,240M**. Agrees. Second cross-check: the cash-flow statement's capital expenditures
  line, **$(5,874)M** for 2025, matches the XBRL `PaymentsToAcquireProductiveAssets` fact used
  in the owner-earnings arithmetic below.

---
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** United buys aircraft, hires crews,
buys fuel, and rents space at airports. It then manufactures a perishable product - a seat on
a particular aeroplane at a particular time - and has to sell it before the door closes or it
is worth nothing forever. It produced **330,284 million available seat miles** in 2025 and
sold **271,619 million** of them (a **82.2%** load factor), at **16.18 cents** of passenger
revenue per available seat mile against **16.46 cents** of total cost per available seat mile.
The gap between those two numbers *is* the business. It was **1.42 cents** of operating margin
per ASM in 2025 (17.88c TRASM less 16.46c CASM), which is **8.0%** of revenue. Everything else
- cargo, the credit-card program, the regional feed - either fills the aeroplane or monetises
the people who already flew on it.

Three sources of revenue, filed: passenger, cargo, and other (which is mostly the sale of
MileagePlus miles to JPMorgan Chase and other partners). The cost side is dominated by three
items the company does not control - **fuel** (4,663 million gallons at $2.44 in 2025), **labour**
(113,200 employees at 2025-12-31, all major workgroups unionised), and **airport and
government charges**.

**The scarce input this business controls.** Not aircraft - Boeing and Airbus will sell an
aeroplane to anybody with the money, and the filing shows United paying for 634 of them. The
genuinely scarce, controlled inputs are **takeoff and landing slots, gates, and route
authorities at capacity-constrained hubs** - Newark, O'Hare, San Francisco, Dulles, LAX,
Denver, Houston and Guam. The filing itself treats these as the collateral of last resort:
the $3.0 billion revolving credit facility "is secured by certain route authorities and airport
slots and gates." The second scarce asset is the **MileagePlus member base and the Chase
co-brand contract**, which is examined separately at Q2.

**Will the fundamentals look broadly the same in ten years?** Yes, and that is not a
compliment. The mechanism - sell perishable seat-miles at a spread over cost, in a business
where capacity is added in indivisible 200-seat lumps with a 25-year life and a 5-to-9-year
order lead time - has been the same for fifty years and the filing gives no reason to think it
changes. **[E3-31]** asks for "relatively simple and stable in character," and this qualifies
on both counts. The corpus's hostility to airlines is a statement about the *returns* the
mechanism produces, not about whether the mechanism is legible; that belongs at Q2 and Q4, and
it is not permitted to pre-empt them here **[E4-26]**.

**VERDICT: [x] IN**

*One caution recorded against my own verdict, per **[E4-51]**: the fuel price and the demand
cycle are both exogenous and neither is forecastable, so "I understand the mechanism" is not
"I can estimate the earnings five years out" **[E5-34]**. That distinction is carried forward
and it is settled at Q4 and Q5, not here.*

## Q2 - IS IT A FRANCHISE? **[E3-03]**

**I pre-registered my expectation before opening the filings, per operator rule 9: I expected
Q2 OUT, and I recorded that the risk was reaching it lazily on the corpus's general disdain
for airlines rather than on United's filed record. Everything below is filed. Where a finding
runs AGAINST my expectation it is stated first and at full strength [E4-26].**

### THE STRONGEST CASE FOR THE NAME, STATED FIRST AND AT FULL STRENGTH **[E4-51]**

United's own 8-K of **2020-06-15, accession 0001104659-20-073190**, published the only
standalone MileagePlus figures that exist. Exhibit 99.1, slide 26:

| MileagePlus Holdings, US$m | 2017 | 2018 | 2019 |
|---|---|---|---|
| Total cash flow from mile sales | 3,624 | 5,072 | **5,330** |
| Revenue, net of redemptions | 1,874 | 2,002 | 1,938 |
| Operating expense excl. D&A | 150 | 122 | **110** |
| **EBITDA** | 1,724 | 1,880 | **1,828** |
| Net income | 371 | 1,625 | **1,578** |
| Frequent flyer deferred revenue | 5,569 | 5,843 | 6,161 |

That is a business with **$110 million of operating cost against $1,938 million of net
revenue**, 71% of its cash from third parties (Chase and 110-plus partners), a 20-year
operating agreement carrying a **guaranteed minimum 20% EBITDA margin** on the United leg,
and — from the same exhibit, slide 27 — *"During the 2008-2009 recession, United revenue
declined 19% while MPH revenue only declined 2%."* The registrant asserted in the 8-K body
that *"Multiplying MPH 2019 EBITDA by a factor of 12 equates to a MileagePlus valuation of
approximately $21.9 billion"* — against a UAL market capitalisation today of $35.3bn. On its
face this is the HOG two-business case: a franchise bolted to a non-franchise.

**It does not survive the test, and here is why - from the same documents.**

1. **Criterion (2) fails for the loyalty program on the airline's own words.** The FY2025
   10-K risk factors, accession 0000100517-26-000023: *"Our MileagePlus loyalty program
   benefits from the attractiveness and competitiveness of United Airlines as a material
   purchaser of award miles and the majority recipient for mileage redemption. If we are not
   able to maintain a competitive and attractive airline business, our ability to acquire,
   engage and retain customers in the MileagePlus loyalty program may be adversely
   affected."* The 2020 exhibit puts a number on the dependency: of 2019 redemption volume,
   **travel was 97% and within travel United was 80%.** A mile is a claim on a United seat.
   Its value is the seat's value. This is not HDFS, which lent to third parties at market
   rates against its own credit; it is a coupon book for the parent's own product.
2. **The $1,828M of EBITDA is a transfer price United set with itself, for the purpose of
   the financing.** Slide 11 of the same exhibit gives the mechanism: a partner buys 15,000
   miles at **$0.02/mile**; on redemption *"MPH buys seat from United for $0.01 per mile."*
   The 50% margin is the difference between two prices United chose. UAL's FY2025 10-K states
   flatly: **"The Company manages its operations as one segment"**, and the CODM assesses
   performance on **consolidated net income**. There is no filed segment split, then or now,
   that is not an artefact of a securitisation structure. The HOG method requires two
   businesses that transact with the outside world; here only one does.
3. **The disclosure has been withdrawn and cannot be refreshed.** The FY2025 10-K MD&A:
   MileagePlus Holdings *"redeemed in full … all $1.52 billion aggregate principal amount"* of
   the MileagePlus notes on **2025-07-07**, and with the July-2024 prepayment of the $1.80bn
   term loan, *"all indebtedness secured by the MileagePlus assets have been fully repaid."*
   The reporting obligation that produced the standalone numbers is gone. **The best market
   test available is seven years stale and pre-dates the pandemic.**
3b. **THE BRIEF'S PREMISE IS FACTUALLY WRONG AND THAT MATTERS TO THE VERDICT.** The
   instruction said United *"published audited standalone figures"* for MileagePlus. **No
   audited standalone MileagePlus financial statements exist on EDGAR.** What exists is
   Exhibit 99.1 to accession 0001104659-20-073190, a **lender presentation**, whose tables are
   labelled *"Historical amounts, as reported"* and carry **no audit report**; the Rule 144A
   offering memorandum was never filed; and **neither MileagePlus Holdings LLC nor Mileage
   Plus Intellectual Property Assets Ltd is an EDGAR registrant.** The string "MPH EBITDA"
   appears in exactly one document on all of EDGAR. Two further facts destroy the carve-out
   as an analytical object: the **2020-06-23 restatement** (accession 0001104659-20-075889,
   Ex. 99.2) moved the 2019 operating cash flow from $2,330M to **$1,715M** after $615M of
   income taxes paid to UAL; and **MPH's standalone frequent-flyer deferred revenue of
   $6,161M EXCEEDS UAL's consolidated $5,276M at the same date**, with no reconciliation
   published anywhere. A carve-out whose deferred revenue is larger than the parent's
   consolidated deferred revenue is not a business; it is a collateral package.
4. **Close substitutes are four deep and named.** Delta/SkyMiles with American Express,
   American/AAdvantage with Citi and Barclays, Southwest/Rapid Rewards with Chase, plus
   Chase's own transferable Ultimate Rewards currency, which converts into United *and*
   several competing programs. Under **[E3-03]** criterion (2) the customer must think there
   is **no close substitute**. There are at least four, they are marketed against each other,
   and the co-brand contracts are re-tendered - the 2020 exhibit records the Chase agreement
   as *"recently extended into 2029"*, i.e. it has a term and an expiry.
5. **[E5-28] scopes the pricing-power claim:** *"If you name some business that has incredible
   pricing power, you're talking about a business that's a monopoly or a near monopoly."*
   MileagePlus is roughly the third-largest US loyalty currency. It is not a near-monopoly and
   the competitor row does not support one.

**THE PEER COMPARISON, WHICH CUTS FOR UNITED ON CREDIT AND AGAINST IT ON DISCLOSURE.**
Delta discloses its co-brand economics in dollars every year: **remuneration from American
Express of $6.8bn (2023), $7.4bn (2024), $8.2bn (2025)**, with a stated expectation of $10bn.
**United has never disclosed a Chase dollar amount in any filing.** What it discloses is
partner revenue inside Other operating revenue, **$2.0bn in 2019 rising to $3.2bn in 2025**.
American ran the identical AAdvantage collateral financing in 2021 (accession
0000006201-21-000022, Ex. 99.1: 2019 cash from sales $5,912M, Adjusted EBITDA $2,911M, the
same 20% transfer-price margin) and **still owes $6,842M against it at 2025-12-31, including a
new $1.0bn term loan taken in 2025**, while United's is repaid in full. On the loyalty
collateral United is unambiguously the stronger credit; on loyalty disclosure it is the
weakest of the three, and **[E2-26]** asks what I would want to know if the positions were
reversed. I would want the Chase number. Delta gives it. United does not.

**So the two-business test was run, as instructed, and it returns one business. MileagePlus is
priced inside the consolidated figures below, not beside them.**

### CRITERION BY CRITERION **[E3-03]**

- **Needed or desired [x] - passes.** 181 million passengers in 2025. Air travel between
  distant points has no substitute at all for most journeys.
- **No close substitute [ ] - FAILS, and the registrant says so.** FY2025 10-K, Item 1A:
  *"Given the **highly competitive nature of the airline industry, the Company historically
  has had limited ability to, and may not be able to in the future, increase its fares and
  fees sufficiently to offset the full impact of increases in fuel prices** … In addition,
  **decreases in fuel prices for an extended period of time may result in increased industry
  capacity, increased competitive actions for market share and lower fares**."* The
  forward-looking-statements list names *"the highly competitive nature of the global airline
  industry and **susceptibility of the industry to price discounting and changes in
  capacity**."* That second sentence is **[E2-58]** written by the issuer: *"persistent
  over-capacity without administered prices (or costs) equals poor profitability"*, and
  prosperity breeding the next glut — *"nothing fails like success."*
- **Not price-regulated [x] - passes.** Fares are not regulated. Note **[E2-59]**: the pre-1978
  regime *did* administer airline prices and floored the industry's profits; *"That day is
  gone"* is exactly how that row says it ends. The absence of price regulation is not a moat.

**Two of three. [E3-03] is conjunctive. Criterion (2) is the one that fails.**

### THE **[E4-55]** UNITS SERIES - NINE YEARS, NOMINAL AND CPI-DEFLATED

The instrument the DG run built, applied where it belongs. Sources: the Operating Statistics
table of the UAL 10-Ks for FY2019 (0000100517-20-000010), FY2021 (0000100517-22-000009),
FY2023 (0000100517-24-000027) and FY2025 (0000100517-26-000023); overlapping years agree
across filings with no restatement. Deflator: **BLS CUUR0000SA0 annual averages (M13)**, from
the issuing authority's flat file, cross-checked against FRED CPIAUCNS to within rounding.
Full working: `Test Runs/_research 2026-09-02 UAL/units_series.md`.

| Year | ASMs (m) | Load factor % | PRASM nominal (c) | **PRASM real, 2025c** | TRASM nominal (c) | **TRASM real, 2025c** |
|---|---|---|---|---|---|---|
| 2017 | 262,386 | 82.4 | 13.13 | **17.25** | 14.40 | **18.91** |
| 2018 | 275,262 | 83.6 | 13.70 | **17.56** | 15.00 | **19.23** |
| 2019 | 284,999 | 84.0 | 13.90 | **17.50** | 15.18 | **19.12** |
| 2020 | 122,804 | 60.2 | 9.61 | 11.95 | 12.50 | 15.55 |
| 2021 | 178,684 | 72.2 | 11.30 | 13.43 | 13.79 | 16.38 |
| 2022 | 247,858 | 83.4 | 16.15 | **17.77** | 18.14 | **19.96** |
| 2023 | 291,333 | 83.9 | 16.84 | **17.79** | 18.44 | **19.48** |
| 2024 | 311,185 | 83.1 | 16.66 | **17.10** | 18.34 | **18.82** |
| 2025 | 330,284 | 82.2 | 16.18 | **16.18** | 17.88 | **17.88** |

**THE TEST REPLICATES, AND IT IS THE DECISIVE FINDING OF THIS RUN.**
- **Nominal PRASM 2017 to 2025: +23.2%. Real PRASM: −6.2%.** (17.25c to 16.18c.)
- **Nominal TRASM: +24.2%. Real TRASM: −5.5%.**
- Against the 2019 base: **nominal PRASM +16.4%, real PRASM −7.6%.**
- **Three consecutive real declines** in the three clean post-recovery years: PRASM real
  +0.1%, −3.9%, −5.4% for 2023, 2024, 2025; TRASM real −2.4%, −3.4%, −5.0%.
- Physical volume moved the other way: **ASMs +25.9% and RPMs +25.6%** over the same nine
  years. **Load factor fell from 84.0% in 2019 to 82.2% in 2025** - the aeroplanes are bigger
  and emptier.

**THE SAME TEST ON THE PEERS, AND IT IS THE STRONGEST FACT AGAINST THIS RUN'S CONCLUSION.**
Real PRASM, 2019 to 2025, in 2025 cents, same CPI-U deflator, all filing-sourced:

| | 2019 | 2025 | change |
|---|---:|---:|---:|
| **UAL** | 17.50 | 16.18 | **−7.6%** |
| DAL | 19.33 | 17.37 | −10.1% |
| AAL | 18.56 | 16.58 | −10.7% |
| LUV | 16.64 | 14.18 | −14.8% |

*(Alaska does not disclose consolidated PRASM before 2024. Delta's as-filed TRASM includes
refinery sales and is not on UAL's basis; PRASM is comparable.)*

**United's real price erosion is the SMALLEST of the four carriers that disclose the series.**
It is the best operator in the industry on the honest metric as well as on margin. That fact
is recorded here at full strength because **[E4-26]** requires the disconfirming evidence for
my own hypothesis to be hunted hardest. It does not change the verdict, and the reason is
**[E2-58]**: in a persistent-over-capacity business without administered prices, relative
position is the ratio of supply-tight to supply-ample years, and *"the one exception is a cost
advantage that is both wide and sustainable."* United does not have one; it has a
**less-bad-than-the-others** position on a metric that is negative for everybody.

**And the cost side settles where the gains went - [E3-62]'s second step.** Over the same nine
years, United's **real CASM fell 3.7%** while its **real PRASM fell 6.2%.** It took cost out
and gave more than all of it away. That is the question the corpus says nobody asks of a capex
case — *"how much is going to stay home and how much is just going to flow through to the
customer"* — answered from the filings, and the answer is the textile-loom answer: **nothing
stuck to the ribs as owners.**

This is **[E4-55]** precisely inverted from Precision Steel and therefore just as diagnostic:
there, pounds fell while price rises held dollars level; here, seat-miles rose 26% while the
price per seat-mile fell 6% in real terms and dollars rose anyway. *"Dollar revenue flattered
by pricing is how a shrinking franchise hides"* — United's dollar revenue is flattered by
**volume**, and the physical series says the price is losing to inflation. Same lesson, other
sign.

### **[E2-44]** - THE TWO-CHARACTERISTIC TEST, BOTH HALVES, BOTH FAIL

**Half one: can it raise prices "even when product demand is flat and capacity is not fully
utilized"?** Capacity is demonstrably not fully utilised — load factor 82.2%, i.e. **17.8% of
the seats United flew in 2025 went out empty**. Its answer, from the FY2025 MD&A regional
table, year on year:

| 2025 vs 2024 | Domestic | Atlantic | Pacific | Latin | **Total** |
|---|---|---|---|---|---|
| ASMs | +6.3% | +6.6% | +4.3% | +7.0% | **+6.1%** |
| **Average fare per passenger** | **−1.9%** | **−0.8%** | **−3.5%** | **−2.1%** | **−1.1%** |
| Yield | −1.8% | −0.8% | −1.8% | −3.2% | **−1.9%** |
| PRASM | −4.1% | −1.6% | +3.0% | −5.2% | **−2.9%** |
| Load factor (points) | −1.9 | −0.7 | +3.7 | −1.7 | **−0.9** |

**Average fare per passenger fell in every one of the four geographic regions**, in a year of
+6.1% capacity and 4.6% CPI-U-deflated cost inflation. Half one fails on the filed table.

**Half two: can it "grow dollar volume with only minor additional investment of capital"?**
Capital expenditure, filed cash-flow statements, FY2017 through FY2025: 3,998 + 4,177 + 4,528
+ 1,727 + 2,107 + 4,819 + 7,171 + 5,615 + 5,874 = **$40,016 million**. Firm purchase
commitments still outstanding at 2025-12-31, Note 12: **$57.0 billion**. Half two fails by a
factor that has no close comparison anywhere in this project's queue.

**And [E4-37], the inverse metric — "you can almost measure the strength of a business over
time by the agony they go through in determining whether a price increase can be sustained."**
United does not need to be inferred into the agony class. Its 10-K states it as a risk factor
in the first person: it *"historically has had limited ability to … increase its fares and
fees sufficiently to offset the full impact of increases in fuel prices."* That is the prayer
session, filed.

### THE ARITHMETIC OF **[E2-27]** - WHAT NINE YEARS OF CAPITAL BOUGHT

Operating income as filed, deflated by CPI-U to 2025 dollars:

| | 2017 | 2018 | 2019 | mean 2017-19 | **2025** |
|---|---|---|---|---|---|
| Operating income, nominal ($m) | 3,498 | 3,292 | 4,301 | 3,697 | **4,713** |
| **Operating income, real 2025$m** | 4,594 | 4,221 | 5,417 | **4,744** | **4,713** |
| ASMs (m) | 262,386 | 275,262 | 284,999 | 274,216 | **330,284** |

**Real operating income in 2025 is $4,713M against a 2017-2019 real mean of $4,744M - down
0.7%. Capacity over the same span is up 20.4%. The capital consumed to get there was $40.0
billion.** Against the single best pre-COVID year, 2019, real operating income is **down
13.0%**. And 2025's $4,713M itself **includes a $427 million gain on aircraft sale-leaseback
transactions** (Note 13); ex that credit, operating income is $4,286M and the nine-year real
comparison is **−9.7%**.

Three endpoints are published rather than one, because **[E4-38]** names the disease -
*"growth-rate presentations can be significantly distorted by a calculated selection of either
initial or terminal dates"* — and prescribes publishing every window. Every window says the
same thing.

This is **[E2-27]** verbatim: *"Viewed individually, each company's capital investment decision
appeared cost-effective and rational; viewed collectively, the decisions neutralized each
other and were irrational … After each round of investment, all the players had more money in
the game and returns remained anemic."*

### **[E3-33] / [E5-28]** - UNTAPPED PRICING POWER

**No.** The test asks whether a manager could raise the return enormously simply by raising
prices, and has not. United tried the opposite in 2025 and its fares fell in all four regions
while it added 6.1% of capacity. The claim would require near-monopoly **[E5-28]**; the
competitor row below shows a five-way oligopoly with two peers of equal or larger scale.
**The class does not apply.**

### **[E4-36]** - WHICH OF THE FOUR CAUSES OF EXTREME SUCCESS IS THIS?

The 2021-2024 earnings recovery is **wave-riding [E3-51]** and nothing else: a demand snap-back
against a supply chain that could not deliver aircraft, plus a fuel price that fell from $3.01
to $2.44 per gallon between 2023 and 2025 (10-K operating statistics). *"When a surfer gets up
and catches the wave … he can go a long, long time. But if he gets off the wave, he becomes
mired in shallows."* **A surfing run is not a moat; the advantage lives in the wave.** The
2025 numbers are the wave already flattening: fuel down another 8%, capacity up 6.1%,
operating income down 7.5%.

### **[E2-53]** - THE DOMINANCE CLASS, TESTED AND REFUTED

*"Once dominant, the newspaper itself, not the marketplace, determines just how good or how
bad the paper will be. Good or bad, it will prosper."* United is, on its own first line of
MD&A, **"the largest airline measured by available seat miles in the world."** It is dominant
on the only scale metric there is, and in 2025 that dominance delivered: capacity +6.1%,
revenue +3.5%, **operating income −7.5%**, fares down in every region. The marketplace, not
the airline, determined how good the year was. **[E2-53] is refuted on this name by its own
strongest form.**

### **[E4-04] / [E5-23]** - MUST THE MOAT BE CONTINUOUSLY REBUILT?

Yes, and it is the excluded class, not the defended one. The test the framework sets is:
*does the spending defend the same advantage, or buy its replacement?* A 25-year-old
aeroplane is a depleting asset and the $57.0bn of firm commitments **buys its replacement** -
it is Mitsui's Rhodes Ridge, not Coca-Cola's advertising. The average age of the 1,066-aircraft
mainline fleet is **15.3 years** (Item 2, Properties). A lapse in this spending does not narrow
the structure; it destroys it, because the fleet ages out.

### THE COMPETITOR ROW - required **[E3-28]**

**Peers named: 5 of the industry's 5 remaining scale US competitors.** Delta, American,
Southwest, Alaska and JetBlue. Spirit is excluded and the exclusion is itself the finding:
it filed for Chapter 11 twice inside 2024-2025 and is no longer a comparable going concern.
**Buffett says eight; the US industry no longer has eight**, which is the consolidation fact
the brief asked to be tested. All six filers have 31 December year ends, so the window is
identical with no alignment adjustment. Full working, tag by tag, with every extraction
decision stated in advance: `Test Runs/_research 2026-09-02 UAL/competitor_row.md`.

**OPERATING MARGIN, `OperatingIncomeLoss` ÷ total operating revenue, both as filed, same
window, all six** (%):

| FY | **UAL** | DAL | AAL | LUV | ALK | JBLU |
|---|---:|---:|---:|---:|---:|---:|
| 2017 | **9.6** | 14.5 | 9.9 | 16.1 | 15.3 | 13.9 |
| 2018 | **7.8** | 11.8 | 6.0 | 14.6 | 7.8 | 3.5 |
| 2019 | **9.9** | 14.1 | 6.7 | 13.2 | 12.1 | 9.9 |
| 2020 | **(41.4)** | (72.9) | (60.1) | (42.2) | (49.8) | (58.0) |
| 2021 | **(4.1)** | 6.3 | (3.5) | 10.9 | 11.1 | (1.3) |
| 2022 | **5.2** | 7.2 | 3.3 | 4.3 | 0.7 | (3.3) |
| 2023 | **7.8** | 9.5 | 5.7 | 0.9 | 3.8 | (2.4) |
| 2024 | **8.9** | 9.7 | 4.8 | 1.2 | 4.9 | (7.4) |
| **2025** | **8.0** | **9.2** | **2.7** | **1.5** | **2.1** | **(4.1)** |

**THE ATTACKER METRIC — RETURN ON UNLEVERAGED NET TANGIBLE OPERATING ASSETS** *(operating
income ÷ (total assets − goodwill − intangibles − cash and short-term investments −
non-interest-bearing current liabilities), identically defined for all six; the NIBCL term is
built as a residual from `LiabilitiesCurrent` less current debt, finance-lease and
operating-lease maturities, and was reconciled line by line against all six filed FY2025
balance sheets)*:

| | **UAL** | DAL | AAL | LUV | ALK | JBLU |
|---|---:|---:|---:|---:|---:|---:|
| **FY2019** | **15.7** | 22.4 | 8.5 | 23.1 | 15.8 | 9.8 |
| **FY2025** | **13.1** | 16.1 | 4.9 | 3.0 | 3.4 | **(3.5)** |

**RETURN ON TOTAL INVESTED CAPITAL INCLUDING WHAT WAS PAID FOR IT** *(operating income ÷
(total debt including all leases + equity); the metric that decided ITW and CSL and inverted
HD)*:

| | **UAL** | DAL | AAL* | LUV | ALK | JBLU |
|---|---:|---:|---:|---:|---:|---:|
| **FY2019** | **13.4** | 20.3 | 9.2 | 21.4 | 14.1 | 10.1 |
| **FY2025** | **10.2** | 14.2 | 4.5 | 3.1 | 2.8 | **(3.2)** |

*\*AAL's denominator is debt minus a stockholders' deficit and is not comparable. On a
debt-only basis FY2025 reads AAL 4.1%, UAL 15.2%, DAL 28.7%.*

**THIS IS THE SINGLE MOST DAMAGING TABLE IN THE RUN, AND IT IS NOT ABOUT UNITED.** **Every one
of the six earned a lower return on unleveraged net tangible operating assets in 2025 than in
2019**, and four of the six roughly quartered it. Six years, the largest fleet-renewal
programme in the industry's history, an industry that consolidated from eight scale
competitors to five, and the whole panel's return on operating assets fell. **[E2-45]'s
attacker's test** asks *"how I would like, assuming I had ample capital and skilled personnel,
to compete with it."* The answer the table gives is that you would not need to attack: the
incumbents are competing the returns away themselves, which is **[E2-27]** and **[E2-58]** in
one row.

*(A note on the subject figure. This run computed UAL's FY2025 attacker metric independently
at **14.8%** using a hand-built liability stack that also removes the **non-current**
frequent-flyer deferred revenue of $4,056M. The panel figure of **13.1%** uses a residual
NIBCL that captures only current liabilities, so it is the more conservative and the more
comparable. Both are shown; the $4.1bn difference is exactly that one line, and neither
version changes the ranking or the direction.)*

**BALANCE SHEET, 2025-12-31** (US$m; debt is the face-of-balance-sheet combined debt-and-
finance-lease lines plus both operating-lease lines, identically defined for all six):

| | **UAL** | DAL | AAL | LUV | ALK | JBLU |
|---|---:|---:|---:|---:|---:|---:|
| Total debt incl. all leases | **31,036** | 20,274 | 35,970 | 5,981 | 6,893 | 9,416 |
| Cash + short-term investments | **12,240** | 4,310 | 5,836 | 3,231 | 2,123 | 2,159 |
| **Net debt** | **18,796** | 15,964 | 30,134 | 2,750 | 4,770 | 7,257 |
| Stockholders' equity | **15,282** | 20,853 | **(3,727)** | 7,981 | 4,118 | 2,120 |
| Debt / (debt + equity) % | **67.0** | 49.3 | *deficit* | 42.8 | 62.6 | 81.6 |

**WHAT THE ROW SHOWS, AND IT CUTS BOTH WAYS.**

*For United:* it is **second of six on operating margin in 2025 (8.0%)**, it improved its
rank from fourth-of-six in 2019 to second, it holds **the largest liquidity buffer in the
panel by more than double the next carrier**, and three of the five peers earned a margin of
2.7% or less in 2025 while one lost money. **United is a good operator in this industry.**

*Against United:* **every single one of the six earned a lower operating margin in 2025 than
it did in 2017**, without exception - UAL 9.6→8.0, DAL 14.5→9.2, AAL 9.9→2.7, LUV 16.1→1.5,
ALK 15.3→2.1, JBLU 13.9→(4.1). Nine years, the largest fleet renewal in the industry's
history, a consolidated market, and the whole industry's margin is lower. **That is [E3-28]'s
purpose discharged: a moat is a claim about relative position, and relative position here is
"least badly injured," which is not a moat.** It is **[E2-58]** — *"long-term profitability
… set by the ratio of supply-tight to supply-ample years"* — read across six filers at once.

**And [E3-61]'s limit on the row is recorded rather than ignored:** *"In some businesses, the
participants behave like a demented Kellogg … I think you'd have to know the people
involved."* The row shows position; it cannot show conduct. If the four surviving network and
low-cost carriers permanently restrained capacity, the economics could change - that is the
one path by which this verdict could be wrong, and it is priced into Q6's monitoring line
below. What the filings show is the opposite: **UAL added 6.1% of capacity in 2025** and its
own risk factors warn that cheap fuel *"may result in increased industry capacity."*

- **Untapped pricing power** - could a manager raise the return simply by raising prices, and
  has not? **[E3-33]** **No.** See above; the 2025 regional table is a live experiment and it
  went the other way.
- **Class: [x] NONE** · **Direction: NARROWING.** **[E4-32]** asks for direction, and the
  direction here is negative on the honest series: real PRASM down three straight years, load
  factor down 1.8 points from 2019, real operating income flat to down across every window.
- **VERDICT: [x] OUT**

**Why OUT and not UNRESEARCHED or UNKNOWABLE.** The separating question **[E4-19]** is *"can I
name the document that would resolve this?"* There is no missing document. The 10-K states
the pricing failure in the first person; the nine-year physical series is filed and
CPI-deflated; the capital consumed is filed; the standalone MileagePlus case was pulled and
tested and returns one business. **The evidence is here and the business fails criterion (2)
of [E3-03].** That is the definition of OUT.

**⛔ THE FILE CLOSES HERE. Q3, Q4 and Q5 are recorded below as COMPUTATION ONLY, under the
heading operator rule 3 requires, because the queue's output contract demands a price. They
carry no entry language and no clearance.**
## Q3 - ARE THEY HONEST, AND ARE THEY RATIONAL?

> **COMPUTATION — NOT A CLEARANCE.** The file closed at Q2. Operator rule 2 forbids treating
> anything below as a pass. This section is recorded because the work was done and because a
> Q3 finding on a name the framework has rejected is still evidence about the framework.
> **[E4-19]'s "out" box is permanent; nothing here reopens it.**

### STEP 1 - THE WEIGHT CASE. Declared before anything else is read.

- [x] **Daily execution [E3-38, E2-70]** - an airline is the paradigm case. Roughly 5,000
      daily departures across six continents, weather, crews, maintenance, air traffic
      control, with a product that is destroyed at the moment of departure if unsold. The
      1977 root **[E2-70]** - an undifferentiated product magnifies the manager - applies
      exactly: the seat is a commodity and only execution separates the carriers.
- [ ] **Control [E1-16]** - no. A minority public holding, exitable daily.
- [x] **Leverage [E3-29]** - $31,036M of debt and lease obligations against $15,282M of
      equity and $76,448M of assets, with **a substantial portion of the assets already
      pledged** (10-K MD&A). Equity is 20.0% of assets. A 10% write-down of operating
      property and equipment ($46,121M) removes **30% of the equity**. *"Small asset errors
      destroy equity"* is satisfied on the arithmetic.

**Two of three ticked. Q3 is therefore a BINARY GATE, not an overlay, and no price
compensates [E1-16, E3-29, E5-35].** This is stated because a run that does not declare its
weight case has not done Q3 - and because it means that even a cheap price could not have
rescued this name had Q2 passed.

### HONESTY - binary, filings-based, dated to when each matter became PUBLIC **[E5-16]**

**No integrity disqualifier found.** Stated in the form the framework requires: *"A Q3 pass
is the absence of found disqualifiers, not a finding that the managers are honest"*
**[E5-17]**.
- No restatement in the nine years read. ICFR reported effective at 2025-12-31; auditor
  Ernst & Young LLP; no disagreement with accountants (Item 9: "None").
- **DOJ Antitrust Division Civil Investigative Demand, public 2015-06-30**, on "statements
  and decisions about airline capacity", with consolidated Sherman Act class actions in the
  District of Columbia alleging collusion on capacity. Still pending; no adverse finding.
  Recorded as a source to read, not a checklist item, per the framework's own instruction
  that litigation is not the primary checklist. **[E5-22]** applies in both directions:
  penalty size is not seriousness. The matter is eleven years old and unresolved.

### STEP 2 - THE FLAGS. Each a prompt to read, never a verdict **[E4-22, E5-15, E5-36]**

- [ ] **weak accounting** - not found. Straight-line depreciation on disclosed lives;
      maintenance expensed as incurred except power-by-the-hour engine contracts, which is
      the conservative treatment; no capitalised maintenance games found.
- [ ] **unintelligible footnotes** - not found. Notes 10 to 13 are plain and the purchase
      commitment table is given in one line of billions by year.
- [x] **trumpeted projections [E4-22, E5-30]** — mild but present. The 10-K guides "less than
      $8.0 billion of adjusted capital expenditures" for 2026 and declines to reconcile it to
      GAAP; the proxy is built on Adjusted EPS, Adjusted Pre-Tax Margin and Free Cash Flow
      targets. **[E3-48]'s action** was taken: 2025 guidance was broadly met on capex and
      beaten on adjusted EPS. Not a ratchet yet, but a guidance culture is *"a ratchet"* and
      *"once you start it, it's all over"* **[E5-30]**.
- [ ] **serial share issuance [E5-15]** - **the opposite, and it is to their credit.** Shares
      outstanding fell from 327,899,771 to 323,470,682 over 2025; 8.1 million shares
      repurchased at an average of **$78.75** for $640M. No equity issued.
- [x] **EBITDA / adjusted-earnings promotion [E4-29] - FIRES, and precisely where it
      matters.** The FY2025 10-K contains **zero instances of the string "EBITDA"**, which is
      genuinely clean financial reporting and is recorded as such. But the DEF 14A of
      2026-04-07 discloses that for 2025 the short-term incentive financial metric
      *"measured our **Adjusted EBITDAR Margin** (rather than our Adjusted EBITDA Margin) …
      Adjusted EBITDAR adjusts Adjusted EBITDA by **aircraft rent expense** … to normalize
      for different aircraft financing decisions made by airlines."*
      **In the most capital-intensive filer in this queue, the pay metric now deletes
      depreciation AND aircraft rent - that is the entire cost of the fleet.** **[E5-41]**
      names the mechanism: depreciation is *"reverse float"*, the expense where *"you spend
      the money first … and record the expense later"* — the worst kind, already paid — and
      EBITDA deletes exactly that. EBITDAR deletes it twice, once for owned aircraft and
      once for leased. The stated rationale is peer comparability, which is [E4-29]'s own
      described benefit *"in the interests of Wall Street."*
- [x] **[E2-49] metric-switching — FIRES, with both readings recorded.** *"Yardsticks seldom
      are discarded while yielding favorable readings."* The switch from Adjusted EBITDA
      Margin to Adjusted EBITDAR Margin was made **for 2025, the year operating income fell
      7.5%.** Against the flag: it was announced ahead with a stated reason, which is
      [E2-49]'s candor case, not its failure case. For the flag: the reason given makes the
      company's own leasing decisions invisible in the metric, and the switch is directional.
      **Recorded as a live prompt, not a finding of venality [E5-38].**
- [ ] **filed-figure tells [E4-30]** - cash taxes as a share of reported pretax income are
      *rising*, not falling: $7M/$3,387M (2023) → $88M/$4,168M (2024) → $62M/$4,306M (2025).
      All are trivial because of **$10.6 billion of federal NOL carryforwards** disclosed in
      the risk factors, which is the innocent explanation and it is filed. Reported growth is
      not unnaturally smooth; it is violently unsmooth. Neither tell fires.
- [ ] **[E2-57] the "except for" flag** — not found. The special-charges note quantifies each
      item and the company does not run an "except for" narrative in the 10-K.
- [ ] **[E3-53] restructuring charges** - the $561M AFA ratification accrual and the $814M
      of 2023 labour ratification bonuses are real costs of running the business and are
      carried in the owner-earnings mean **[E5-33]**, not annualised away.

### STEP 3 - THE PRIMARY TEST **[E2-01]**, and its scope carve-out **[E2-47, E2-43]**

Net income ÷ average stockholders' equity, filed, nine years:

| 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| 24.5% | 22.6% | 27.9% | **(80.8)%** | **(35.7)%** | 12.4% | 32.3% | 28.6% | 24.0% |

**Nine-year arithmetic mean: 6.2%.** The last three years read 32.3%, 28.6%, 24.0% and look
excellent; the nine-year series is what [E2-01] asks for, and it is 6.2%.

**[E2-47] carves out "unusual debt-equity ratios," and this is one.** Equity is 20.0% of
assets, so the ROE is a leveraged number and **[E2-43]**'s denominator - *unleveraged net
tangible assets, "the best guide to the economic attractiveness of the operation"* — is the
one that governs. Built from the FY2025 balance sheet:

| | US$m |
|---|---:|
| Total assets | 76,448 |
| less goodwill | (4,527) |
| less intangible assets, net | (2,655) |
| less cash and short-term investments | (12,240) |
| less accounts payable, accrued salaries, advance ticket sales and frequent-flyer deferred revenue (current and non-current), and other current | (25,132) |
| **= unleveraged net tangible operating assets** | **31,894** |
| Operating income 2025 | 4,713 |
| **Return, pre-tax** | **14.8%** |
| Operating income ex the $427M sale-leaseback gain | 4,286 |
| **Return, pre-tax, ex one-off** | **13.4%** |

**Return on total invested capital including what was paid for it** (the metric that decided
ITW and CSL and inverted HD): operating income $4,713M ÷ (total debt and leases $31,036M +
equity $15,282M = $46,318M) = **10.2% pre-tax, 7.9% after the 22.1% effective tax rate.**
The goodwill wedge is reported rather than hidden: $4,527M of Continental-merger goodwill sits
in that denominator and is excluded from the unleveraged figure above, per [E2-43].

**Both numbers are peak-cycle.** The same denominator in 2020 carried an operating loss of
$6,359M.

### THE HALF-OWNER TEST **[E2-26]** - and it substantially passes

Does the reporting tell me what I would want to know if the positions were reversed? Largely
yes, and it is worth saying so on a name being rejected:
- The **$57.0 billion purchase-commitment table is given by year**, five years plus a
  thereafter column. Most filers give a total.
- The **firm-order aircraft table gives contractual deliveries AND management's expected
  deliveries separately**, so the reader can see the Boeing and Airbus slippage.
- The **sale-leaseback gain of $427M is quantified separately** inside the special-charges
  note rather than buried - this is the [E2-26] standard met exactly.
- The **AFA ratification vote failure of 2025-07-29 is disclosed**, together with the fact
  that the $561M charge was recorded for an agreement the membership then rejected. Reporting
  a charge for a deal that did not happen is a candor act, not a concealment.
- The **non-cash "Investing and Financing Activities Not Affecting Cash" lines are on the face
  of the cash-flow statement** - $1,901M of operating-lease ROU assets acquired in 2025 -
  which is exactly the disclosure the brief predicted would have to be dug for.
- **Against:** management's own preferred capital-spend measure is non-GAAP and is
  deliberately not reconciled ("we are not able to predict non-cash capital expenditures
  without unreasonable efforts").

### THE INSTITUTIONAL IMPERATIVE - score all four **[E2-30]**

- [ ] **(1) resists any change in current direction** - not found. Order books were reworked
      around Boeing delays and CPAs were renegotiated in 2025.
- [x] **(2) projects or acquisitions materialise to soak up available funds** - **fires
      hard.** $57.0 billion of firm commitments against a $35.3 billion market
      capitalisation. Every dollar of the next decade's cash flow is spoken for.
- [ ] **(3) staff studies to justify the leader's craving** - no evidence in the filings.
- [x] **(4) peer behaviour mindlessly imitated** - **fires.** Every US network and low-cost
      carrier placed record orders into the same delivery window. This is **[E2-27]** with
      the [E2-30] mechanism named: *"Institutional dynamics, not venality or stupidity."*

### CAPITAL ALLOCATION - the buyback conditions **[E5-08, E4-31, E5-24, E5-25]**

- **(1) ample funds for operations and liquidity? NO, on [E5-25]'s standard.** Berkshire
  published its own conditions as numbers in advance — a $20bn liquidity floor, *"financial
  strength that is unquestionable takes precedence over all else."* United's liquidity floor
  is **$2.0 billion and it is imposed by its lenders' covenants**, not chosen. And the
  sequence is the test: **$637M of stock repurchased during 2025; $2,000,000,000 of new
  senior notes issued on 2026-02-02 and 2026-02-06**, weeks after the year end, at 5.375% and
  4.875%. **[E2-52]** is written for dividends but the class is the same: *"Beware of
  'dividends' that can be paid out only if someone promises to replace the capital
  distributed."* The capital distributed in 2025 was replaced with borrowed money in
  February 2026.
- **(2) repurchases at a material discount to conservatively calculated intrinsic value?
  NO.** The average repurchase price was **$78.75**. The conservative constructions computed
  at Q5 below put the zero-growth value at roughly **$25 to $115 per share** against the
  sovereign and **$13 to $60** against the [E4-28] floor. $78.75 sits inside the first range
  and above the second. **[E5-24]**: *"what is smart at one price is dumb at another."*
- **→ CAPITAL ALLOCATION FLAG, raised, with the humility clause [E4-13] attached in full:**
  this rests on our own intrinsic-value range, *"it is natural for CEOs to be optimistic about
  their own businesses. They also know a whole lot more about them than I do,"* and
  *"infractions, even serious ones, are innocent; many CEOs never stop believing their stock
  is cheap"* **[E5-08]**. **The flag binds position size, never the discount rate.** Since the
  file is closed there is no position to bind, and the flag is recorded for the register.

### PAY VERSUS PERFORMANCE **[E2-49]** - are the incentive metrics the reported metrics?

**No. Not one of them is.** From the DEF 14A of 2026-04-07 (accession 0001104659-26-040467)
and the `ecd` pay-versus-performance XBRL facts filed with it:

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|
| PEO compensation actually paid ($) | 11,099,444 | 9,915,781 | 23,055,816 | **96,724,681** | **45,643,992** |
| PEO summary-comp total ($) | 9,845,064 | 9,796,602 | 18,573,299 | 33,924,988 | 32,282,253 |
| Company-selected measure: **Adjusted EPS** | (13.94) | 2.52 | **10.05** | **10.61** | **10.62** |
| UAL TSR, $100 invested 2020-12-31 | 101.23 | 87.17 | 95.40 | 224.51 | **258.54** |
| Peer-group TSR, same basis | 98.25 | 63.99 | 82.72 | 82.68 | **87.62** |

Four observations, each filed:
1. **The company-selected measure is flat.** Adjusted EPS 10.05 → 10.61 → 10.62 across
   2023-2025, **+5.7% in two years**, while compensation actually paid to the CEO moved
   $23.1M → $96.7M → $45.6M. The pay outcome is a share-price outcome, not an earnings
   outcome.
2. **The 2025 short-term incentive paid a formulaic 135% of target** in a year when GAAP
   operating income fell 7.5% and fares fell in all four geographic regions.
3. **Every performance metric in the plan is non-GAAP**: Adjusted EBITDAR Margin (33% of
   STI), Absolute Adjusted EPS (40% of PBRSUs), Relative Adjusted Pre-Tax Margin (40% of
   PBRSUs), Free Cash Flow. The measure the CODM actually uses to run the company, per the
   segment note, is **GAAP net income** - and it appears in no incentive plan.
4. **In fairness, and it is a large fairness:** UAL's TSR of $258.54 against an airline peer
   group at $87.62 is a 3x relative outcome over five years. The pay is large because the
   stock tripled relative to the industry. **[E3-59]** asks how well they ran the business
   *"against the hand they were dealt"*, and against this hand they ran it well.

### THE GUARDRAIL - checked before the verdict **[E2-37, E2-38, E3-39]**

- [x] **Confirmed: nothing in this Q3 is being used to promote the name.** United's management
      is, on the filed record, the best operator in a bad industry - best-in-panel margin
      rank improvement, smallest real price erosion, largest liquidity buffer, net share
      count reduction, no EBITDA in the financial statements. **None of that repairs Q2.**
      *"A textile company that allocates capital brilliantly within its industry is a
      remarkable textile company — but not a remarkable business"* **[E2-37]**. *"Good jockeys
      will do well on good horses, but not on broken-down nags"* **[E2-38]**.
- [x] **Key-person dependence is recorded at Q2 as a moat defect [E4-23]**, not here as a
      strength: the corpus's own test is whether you can name the CEO. You have to be able to
      name United's, because the operating gap versus American and JetBlue is the whole
      difference between 8.0% and 2.7% and (4.1)% margins in the same year on the same
      routes with the same aircraft. *"If a business requires a superstar to produce great
      results, the business itself cannot be deemed great."*
- [x] **Is the franchise already intact and the damage excisable [E2-35, E2-36]?** Not
      applicable. There is no localised excisable cancer here; there is no franchise to
      operate on.

**VERDICT: NOT REACHED - the file closed at Q2.** Had it been reached, the honest form would
have been **IN** in the narrow sense the framework defines (no disqualifier found), carrying
one live **capital-allocation flag** and two live prompts ([E4-29] EBITDAR in the pay metric,
[E2-49] the switch). **IN never promotes.**

## Q4 - WILL IT SURVIVE?

> **COMPUTATION — NOT A CLEARANCE.** The file closed at Q2.

### OWNER EARNINGS - THE ONE NUMBER **[E2-23]**

Base = mean of (operating cash flow − share-based compensation), the project's stated
convention, because OCF nets the working-capital increment from one audited line, which is
[E2-23] constraint 3. Nine years, filed:

| FY | OCF | SBC | **OCF − SBC** | D&A | capex | non-cash PP&E via leases/debt |
|---|---:|---:|---:|---:|---:|---:|
| 2017 | 3,474 | 73 | **3,401** | 2,149 | 3,998 | n/d |
| 2018 | 6,164 | 101 | **6,063** | 2,165 | 4,177 | n/d |
| 2019 | 6,909 | 100 | **6,809** | 2,288 | 4,528 | n/d |
| 2020 | (4,133) | 108 | **(4,241)** | 2,488 | 1,727 | n/d |
| 2021 | 2,067 | 238 | **1,829** | 2,485 | 2,107 | n/d |
| 2022 | 6,066 | 89 | **5,977** | 2,456 | 4,819 | n/d |
| 2023 | 6,911 | 80 | **6,831** | 2,671 | 7,171 | 819 + 761 op-lease ROU |
| 2024 | 9,445 | 142 | **9,303** | 2,928 | 5,615 | 409 + 625 op-lease ROU |
| 2025 | 8,431 | 148 | **8,283** | 2,939 | 5,874 | (25) + **1,901** op-lease ROU |

**Stock compensation subtracted in full [E5-06].** It is small here ($148M, 0.25% of revenue);
**[E3-70]**'s market-value standard would raise it, and the reported charge is treated as the
floor of the subtraction, not the measure. The difference is immaterial at this scale and is
stated rather than assumed away.

### MAINTENANCE CAPEX - (c) IS A DISCLOSED JUDGMENT, AND THE D&A END IS INVALID **[E5-20]**

**This is the finding the brief predicted and it is confirmed three independent ways.**

1. **The corpus rules it out by name.** *"in the case of all railroads, merely spending their
   depreciation expense will not keep them in the same place … the true maintenance capex …
   is higher than 60 percent"* **[E5-20]**, and **airlines are named the same way at
   [E3-44]**. The [E3-44]/[E2-41] D&A default explicitly does not reach this class.
2. **The ratio says so.** Capex ÷ D&A is **2.00x in 2025**, 1.92x in 2024, 2.68x in 2023, and
   1.90x on the five-year mean. A business spending twice its depreciation for nine years is
   not one where depreciation approximates renewal.
3. **Management says so, in its own non-GAAP measure.** The FY2025 10-K MD&A: *"For 2026, the
   Company expects **less than $8.0 billion of adjusted capital expenditures** … calculated as
   capital expenditures … **plus property and equipment acquired through the issuance or
   modification of debt, finance leases and other financial liabilities and operating leases
   converted to finance leases**."* Management publishes a capital-spend measure that
   **explicitly adds back the lease-financed equipment** - the exact leakage the brief warned
   about - and guides it to **2.7x the depreciation charge.** This is the VZ precedent
   repeating: the D&A end is not conservative-versus-optimistic, it is **wrong**.

**The leakage, quantified.** The face of the cash-flow statement, "Investing and Financing
Activities Not Affecting Cash": **$1,901M of right-of-use assets acquired through operating
leases in 2025** (2024: $625M; 2023: $761M), plus PP&E acquired through debt and finance
leases of $(25)M, $409M and $819M. And Note 13: **$427 million of gains on aircraft
sale-leaseback transactions in 2025**. Fleet capacity is being acquired through channels that
never touch investing cash flow, and disposal gains are being booked in operating income
while the aircraft stays on the ramp under a lease. **Total capex is therefore the GENEROUS
end of the valid range, not the conservative one.**

**Fleet replacement, from the filing, as the independent check.** Item 2 Properties: **1,066
mainline aircraft, average age 15.3 years**, plus 424 regional aircraft under CPAs. Note 12:
**634 firm aircraft commitments** inside a $57.0 billion purchase-commitment total. Even
attributing only 80% of that total to aircraft gives roughly **$72 million per airframe**. A
1,066-aircraft fleet on a 27-year economic life needs **39 replacements a year**, which at
$72M is **$2.8 billion a year for mainline airframes alone** - before spare engines, cabin
retrofits, ground equipment, facilities and IT, all of which are also depreciating. **Total
depreciation and amortisation is $2,939M and it must cover all of it.** The airframe
replacement run-rate on its own consumes essentially the entire depreciation charge. That is
[E4-47] operating: *"under high inflation, replacement capex in current dollars outruns
depreciation charged in old dollars."*

**(c), as a disclosed guess:** somewhere between **60% of adjusted capital expenditure**
([E5-20]'s own stated floor, ≈$3,970M) and **all of it** (≈$6,620M on the three-year mean of
management's adjusted measure). Total GAAP capex is used as the working (c) below because it
sits inside that band and is the only figure taken directly from an audited statement.

### MORE THAN ONE WINDOW - THE SPREAD IS PART OF THE RANGE **[E4-25]**

| window | mean (OCF − SBC) | (c) = total capex | **OE** | yield on $35,252M |
|---|---:|---:|---:|---:|
| 3-yr, 2023-25 | 8,139 | 6,220 | **1,919** | **5.44%** |
| 5-yr, 2021-25 | 6,445 | 5,117 | **1,327** | **3.76%** |
| 7-yr, 2019-25 | 4,970 | 4,549 | **421** | **1.19%** |
| 9-yr, 2017-25 | 4,917 | 4,446 | **471** | **1.34%** |
| **7 clean yrs, ex 2020-21** | **6,667** | **5,169** | **1,498** | **4.25%** |
| 3-yr, at management's adjusted capex | 8,139 | 6,621 | **1,518** | **4.31%** |
| clean-7, at [E5-20]'s 60% floor | 6,667 | 3,101 | **3,566** | **10.12%** |
| *3-yr, at D&A -* ***INVALID [E5-20]*** | 8,139 | 2,846 | *5,293* | *15.01%* |

- **Short-window mean (3-yr): $1,919M. Long-window mean (9-yr): $471M.**
- **Spread, conservative end: the 9-year window is 75.5% BELOW the 3-year window.** The run.py
  threshold for "the spread is part of the range, not a tiebreak" is 15%. This is five times
  that.
- **Combined range (window spread × capex band): $421M to $5,293M - a 12.6x width.** Excluding
  the [E5-20]-invalid D&A construction entirely: **$421M to $3,566M, still 8.5x.**
- **Is that range too wide to reach a conclusion? YES, and [E4-25] says that IS the
  conclusion:** *"Usually, the range must be so wide that no useful conclusion can be
  reached."* Q4 would independently return **UNKNOWABLE on the owner-earnings width** even if
  Q2 had passed. **The file does not need Q2 to close it.**
- **[E5-11] - the wide spread is itself a Q4 finding about earnings reliability.** Name the
  distorted years: **fiscal 2020 and fiscal 2021**, in which operating cash flow was
  −$4,133M and +$2,067M against a 2019 base of +$6,909M.
- **[E3-55], scoped honestly against my own conclusion:** *"If we have a business about which
  we're extremely confident as to the business result, we would prefer that it have high
  volatility."* Volatility with a certain endgame is not a defect. **The endgame here is not
  certain** - that is the difference between See's losing money eight months a year and an
  airline losing $6.4 billion of operating income in one.

**OWNER EARNINGS BY YEAR, at the valid (total-capex) end.** Four of the nine years are
negative:

| 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **(597)** | 1,886 | 2,281 | **(5,968)** | **(278)** | 1,158 | **(340)** | 3,688 | 2,409 |

### THE BOOM-WINDOW TEST **[E4-41]** - `level_shift` and `best_year_dependence`, run

Run from `Screens/floor_screen.py` on the owner-earnings series above.

| series | `level_shift` | `best_year_dependence` |
|---|---|---|
| 9-yr, capex end | −7.58, **uninterpretable** (see defect note) | 0.854 - **ONE YEAR CARRIES THE WINDOW** |
| **7 clean years, capex end** | **1.62 — "STEP UP, normalize down [E4-41]"** | 0.244 — **ONE YEAR CARRIES THE WINDOW** |
| 7 clean years, D&A end | 1.60 — **"STEP UP, normalize down"** | 0.089 — no single-year dependence |

**Interpretation, which the tool is forbidden to supply (operator rule 8).** The clean-window
`level_shift` of 1.62 says the last three years sit 62% above the earlier four - the boom
window is real and the instrument detects it. `best_year_dependence` of 0.244 says removing
the single best year (**2024, $3,688M**) drops the mean 24%. **[E4-41]** requires the
favourable exogenous break to be named and removed before the mean is trusted, and it is
nameable: **the average price per gallon of fuel fell from $3.01 in 2023 to $2.44 in 2025.**
At 4,663 million gallons consumed in 2025, that fall is worth **$2,658 million a year** -
**56% of 2025 operating income** - and it is a commodity price, not an achievement.
**Normalising down for it is not optional.** A fuel price back at 2023 levels, with United's
own filed statement that it *"historically has had limited ability to … increase its fares and
fees sufficiently to offset the full impact of increases in fuel prices"*, takes 2025
operating income from $4,713M to roughly **$2,055M** and takes owner earnings at the valid
capex end **negative.**

### GREAT, GOOD, OR GRUESOME? **[E4-20]**

- [ ] great [ ] good [x] **GRUESOME**

The corpus names this business in the sentence that defines the class: *"The worst sort of
business is one that **grows rapidly, requires significant capital to engender the growth, and
then earns little or no money. Think airlines.** … Investors have poured money into a
bottomless pit, attracted by growth when they should have been repelled by it."* **[E4-20]**

**The framework does not permit that quotation to be the finding, so here is the arithmetic
instead, and [E4-43]'s warning against over-reading is applied first.** [E4-43] says the
*good* class passes and cites *"nothing shabby about earning $82 million pre-tax on $400
million of net tangible assets"* — 20.5%. **[E5-40]** puts ~12% on retained capital at
"quite satisfactory." United earns **14.8% pre-tax on unleveraged net tangible operating
assets (13.4% ex the sale-leaseback gain)**, which sits between those two marks. **On that
metric alone United is arguably "good," not gruesome, and that is recorded as the case
against this verdict.**

It fails anyway, for the reason [E4-20] actually gives, which is a **savings-account** test
about what the owner takes out:
- The account's interest rate, measured as the corpus measures it - owner earnings against
  the price paid - is **1.19% to 5.44%** across every valid window. The bond is 5.27%.
- The account *"requires you to keep adding money at those disappointing returns"*:
  **$57.0 billion of noncancelable firm commitments**, contracted, against a $35.3 billion
  market capitalisation.
- Nine years of it produced **$40.0 billion of capital expenditure and real operating income
  0.7% BELOW the 2017-2019 real mean.**
- **[E4-43]'s own escape clause is the test, and it fails it:** cash-consuming growth is only
  gruesome *"unless the cash they consume gets to earn a reasonable return."* $40.0 billion
  consumed; real operating income flat. It did not.

### STAYING POWER - SCORE ALL THREE **[E5-11]**

**(1) A large and reliable stream of earnings — LARGE, NOT RELIABLE. FAILS on "reliable."**
$59.1 billion of revenue and $4.7 billion of operating income is large by any measure. But
**operating income was −$6,359M in 2020 and −$1,022M in 2021**, and owner earnings at the
valid capex end were negative in **four of the last nine years**. [E5-29] is respected - risk
means impairment, not price movement - and the impairment was real: equity fell from $11,531M
to $5,029M between 2019 and 2021.

**(2) Massive liquid assets - PASSES, and it is the best in the industry.** $5,942M of cash
and equivalents plus $6,298M of short-term investments = **$12,240M**, cross-checked against
the MD&A's "$12.2 billion". That is **more than double Delta's $4,310M and more than double
American's $5,836M**, on a larger revenue base than either. **[E5-39] is applied strictly: the
$3.0 billion revolving credit facility is NOT counted**, because *"we will never be dependent
on the kindness of strangers … no bank lines counted."* It passes without it.
*Qualification, recorded: "a substantial portion of the Company's assets, principally aircraft
and certain related assets, certain route authorities and airport slots and gates, was
pledged" (MD&A). The liquid assets are unencumbered; most of the rest is not.*

**(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS - FAILS, and by the widest margin in this
queue. This is the one [E5-11] says "usually leads companies to experience unexpected
problems."**

| near-term call | US$m | source |
|---|---:|---|
| Debt, finance lease and other financial liabilities due within 12 months | **5,100** | MD&A, 2025-12-31 |
| Firm purchase commitments due in 2026 | **12,600** | Note 12 |
| Unresolved AFA flight-attendant contract, amendable since **August 2021**, TA rejected by the membership **2025-07-29**; $561M already accrued for a payment not made | **≥561** | Notes 12 and 13 |
| **Total contracted near-term calls** | **≈18,300** | |
| against: cash and short-term investments | 12,240 | |
| against: 2025 operating cash flow | 8,431 | |

It closes only by refinancing - and it was closed exactly that way on **2026-02-02 and
2026-02-06**, when UAL issued **$1.0 billion of 5.375% notes due 2031 and $1.0 billion of
4.875% notes due 2029**. **That is the kindness of strangers, exercised, six weeks after the
balance-sheet date, on a company that had just spent $637 million buying its own stock.**

**Four names in this project have now failed a strength on [E5-39] - LOW, ITW, SHW, HD. UAL
is the fifth, and it is the first to fail strength (3) rather than strength (2).**

**[E2-54]'s coverage test — "all interest, both payable and accrued, comfortably met out of
current cash flow net of ample capital expenditures."**
- On GAAP capex, clean-7 means: (6,667 + ~1,500 interest paid) − 5,169 = **$2,998M** against
  ~$1,600M of interest expense = **1.87x. Thin, but covered.**
- On management's own adjusted capital expenditure trajectory (guided <$8.0bn for 2026):
  (8,283 + 1,330) − 7,500 = **$2,113M** against $1,373M = **1.54x**, and at the $8.0bn
  guidance ceiling it is **1.18x**. **"Ample capital expenditures" is management's own
  number, and on it the test is not comfortably met.** *"Zip up your wallet."*

**[E3-52] - read the terms, not just the quantity, and this cuts BOTH ways.**
*Against:* the $31.0bn is **covenanted, secured, dated** debt - a $2.0bn minimum-liquidity
covenant and a 1.6:1 appraised-collateral-to-debt test, semi-annual, with cross-default and
cross-acceleration. That is the opposite of float.
*For:* United also carries **$8,131M of advance ticket sales and $7,777M of frequent-flyer
deferred revenue = $15.9 billion of customer-prepaid, non-interest-bearing, covenant-free
liabilities.** That genuinely is *"the benefit of debt … with none of its drawbacks"* and it
is why the unleveraged net tangible operating asset base is only $31.9bn on $76.4bn of assets.
**It is the single best structural feature of this business and it is recorded as such.**

**Leverage, named and quantified [E4-16, E3-29]** - *there is no ratio ceiling in this
framework and the corpus supplies none:* $31,036M of debt and lease obligations, $18,796M net
of liquidity, against $15,282M of equity and $4,713M of operating income. Net debt is **4.0x**
2025 operating income and **1.23x** equity. In 2020 the same structure met a 64.5% revenue
decline.

### **[E3-24]** - NAME THE SPECIFIC WAY THIS BUSINESS DIES, QUANTIFIED, WITH A LIKELIHOOD

**The mechanism.** A demand shock or a fuel spike arrives while $57.0 billion of
noncancelable aircraft commitments is running and $5.1 billion of debt is maturing annually.
The commitments cannot be cancelled without *"material liabilities to our counterparties"*
(Item 1A). Capacity therefore keeps arriving into a falling market - which is [E2-27]
exactly - fares fall further, and the equity absorbs the difference.

**Quantified from filed figures, three ways:**
1. **Fuel.** 4,663 million gallons at $2.44 = $11,378M in 2025. A return to the 2023 price of
   $3.01 costs **$2,658M**, or **56% of 2025 operating income**, with the company's own filed
   statement that it cannot reliably pass it on.
2. **Demand.** A 10% fall in revenue passenger miles at the 2025 yield of 19.67c removes
   27,162 million RPMs × $0.1967 = **$5,343M of passenger revenue**. Against $4,713M of
   operating income and a short-run cost base that is largely fixed, that alone is more than
   the whole of it.
3. **The 2020 stress test is filed, not modelled.** Revenue $43,259M → $15,355M (**−64.5%**);
   operating income +$4,301M → **−$6,359M**; **operating cash flow +$6,909M → −$4,133M**;
   equity $11,531M → $5,960M. The equity was preserved by CARES Act support, by the
   **MileagePlus $6.8bn secured financing** (which is the only reason standalone MileagePlus
   figures exist at all), and by capital-markets debt. **The MileagePlus collateral has now
   been released - the notes were redeemed 2025-07-07 and the term loan prepaid July 2024 -
   so the single largest unencumbered asset used to survive 2020 has been re-pledged into
   the general capital structure and spent.** The fire extinguisher used last time has been
   discharged.

**Likelihood: [x] a real possibility.** Not "a low-level possibility," and the reason is
**[E4-40]**: *"all of us in the industry made a fundamental underwriting mistake by focusing
on experience, rather than exposure."* The exposure is filed and it is enormous; the
experience of 2022-2025 has been benign; a benign loss history late in a good cycle is *"not
only useless, but actually dangerous"* as a guide. The event has occurred once in the last
six years.

**VERDICT: NOT REACHED - the file closed at Q2. Had it been reached it would have returned
UNKNOWABLE on [E4-25] (the range is too wide to conclude) with strength (3) of [E5-11]
failing outright. Neither is a pass.**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN. Q2 returned OUT. What follows is the price
the queue's output contract requires, and nothing else.**

---
## Q5 - WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

# COMPUTATION - NOT A CLEARANCE

**Operator rule 3.** The file closed at Q2 (OUT). Every figure below is arithmetic produced
after a failed gate. **It carries no entry language, no ranking position, and no clearance.**
It exists because the WATCHLIST RUN QUEUE requires every run to end with a price.

**Inputs.** Sovereign **5.27%** (US Treasury 30-year par yield, 2026-09-01, issuing
authority). Price **$108.606** (2026-09-02, aggregator, live quote only, flagged). Shares
**324,583,772** (10-Q cover, 2026-07-09). **Market capitalisation $35,252M.**
**No risk premium is added to the rate [E3-42]** - certainty is priced at the understanding
gate and in the end discount, never in the discount rate.

**1. THE YIELD**
- owner earnings **$421M .. $3,566M** (valid constructions only; the D&A end is excluded as
  INVALID **[E5-20]**) ÷ market cap **$35,252M** = **1.19% .. 10.12%** · sovereign **5.27%**
- **judged central figure: $1,498M** - the seven clean years excluding 2020-2021, at total
  capex - = **4.25%**, **1.02 points BELOW the bond.**
- *For completeness the invalid D&A construction would read $5,293M and 15.01%. It is shown
  only so the reader can see what the default would have produced and why [E5-20] voids it.*

**2. WHAT THE PRICE ALREADY ASSUMES**
- Perpetual growth needed to justify the quote **at the sovereign discount rate**, judged
  figure: **1.02%.** At the 5-year window: **1.51%.** At the 7-year window: **4.08%.**
- Perpetual growth needed to reach the **[E4-28] 10% floor**: **5.75%** at the judged figure,
  **4.56%** at the most generous valid window, **8.81%** at the 7-year window.
- **What the business has actually done:** real operating income **−0.7%** against the
  2017-2019 real mean; **−13.0%** against 2019 alone. Real PRASM **−6.2%** over nine years.
  Real TRASM **−5.5%**. Nominal revenue CAGR 2017-2025 is 5.7%, and all of it and more is
  volume and inflation.
- **[E4-35]'s base rate applies to the floor case:** sustained double-digit growth is a
  fewer-than-1-in-20 event among the 200 most profitable companies. This name needs 5.75%
  perpetual real-plus-inflation growth merely to reach the quit-on line, against a nine-year
  record of zero.

**3. WHAT YOU ARE PAID**
- At the judged owner earnings and zero growth: **4.25% against a 5.27% sovereign =
  −1.02 points over the sovereign.**
- Range across valid constructions: **−4.08 points to +4.85 points.**

**THE FLOOR, BEFORE ANY RANKING [E4-28, E3-13].** *"That's the figure we quit on."*
**Honest pre-tax expectancy at this price: 4.25%** (judged), **5.44%** at the most generous
valid construction. **Both are below roughly 10%. The name is not ranked. It is quit on**,
whatever the sovereign is and whatever the rest of the opportunity set looks like. **[E4-28]**
is explicit that this holds *"whether short rates are 6 percent or whether short rates are 1
percent."*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** - 324.58M shares:

| construction | zero-growth value at the 5.27% sovereign | at the [E4-28] 10% floor |
|---|---|---|
| 7-yr window (2019-25), $421M | ~**$25**/sh | ~**$13**/sh |
| 5-yr window, $1,327M | ~**$78**/sh | ~**$41**/sh |
| **clean-7 judged, $1,498M** | ~**$88**/sh | ~**$46**/sh |
| 3-yr window, $1,919M | ~**$112**/sh | ~**$59**/sh |
| clean-7 at [E5-20]'s 60% floor, $3,566M | ~**$209**/sh | ~**$110**/sh |

- **conservative ~$25 · judged ~$85-90 · optimistic ~$210 · current price $108.61**
- *The width of that range is not a presentation failure; it is the finding. **[E4-25]**:
  "Usually, the range must be so wide that no useful conclusion can be reached."*
- **[E2-63] - what bounds the upside is stated, not just the yield:** the $209 figure requires
  simultaneously that maintenance capex is only 60% of the spend, that the COVID years are
  permanently excluded from the record, and that the 2023-2025 fuel tailwind persists. Two of
  those three are assumptions the filing contradicts.

**WHICH BAR** - **[x] Bar 2, the screamer test [E4-01]**, and it returns the middle outcome.
No margin is added on top; "startlingly low" is observed, not subtracted. **The price of
$108.61 sits INSIDE the range** ($25 to $209), which is the outcome the framework calls
*"no useful conclusion — move on."* Not a buy, not a short, no view.
**Windage count: ONE.** Conservatism is spent once, at the (c) judgment, where total capex is
used because [E5-20] invalidates the D&A alternative. It is **not** re-spent in the discount
rate (no risk premium, [E3-42]), **not** in the growth rate, and **not** in a second end
margin.

**VERDICT: NOT APPLICABLE. The gate did not open. Ranking position: none - the name is quit
on at the [E4-28] floor, not ranked against the opportunity set.**

## Q6 - WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Not reached. There is no position, so [E1-02]'s pre-commitment and [E2-28]'s sell rule have
nothing to bind.** What is recorded instead is **the one thing that would reopen this file**,
written now so that it is pre-committed rather than retrofitted **[E1-02]**:

**THE REOPENING CONDITION.** Q2 turned on **[E3-03]** criterion (2) and on the CPI-deflated
unit-revenue series. It would be reopened by, and only by, **five consecutive years in which
US industry available seat miles grow more slowly than US real GDP while United's real PRASM
rises**. That is the filed, observable signature of **[E2-58]**'s ratio of supply-tight to
supply-ample years permanently changing, and it is the one path - flagged at the competitor
row under **[E3-61]** - by which this verdict is wrong. Five years, because **[E4-17]** says
*"those beliefs change quite gradually"* and **[E2-42]** makes five years the default window.
**Nothing shorter counts, and a single good year counts for nothing.**

**The monitoring metric, if anyone tracks it:** real PRASM in constant dollars, published
annually here, beside industry ASM growth. **[E4-32]**: direction outranks existence.

**And the corpus's own conduct on this exact security is on the record:** the 2020 airline
exit was *"complete, weeks, no half measures"* once the view crystallised **[E2-40]**. Q6
carries both halves - slow to conclude, fast once concluded.

**VERDICT: NOT REACHED.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, **Q2 OUT - file closed**.
      Q3, Q4, Q5 written as COMPUTATION under operator rule 3, each headed as such, none
      claiming a verdict.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the
      only IN and it rests on the filed operating statistics and the filed fleet table.
- [x] No UNRESEARCHED verdict was issued. The separating question **[E4-19]** was asked aloud
      at Q2 and the answer was that no missing document exists - the pricing failure is in the
      registrant's own risk factors and the physical series is filed for nine years.
- [x] No UNKNOWABLE verdict was issued at Q2. **Q4 would independently have returned
      UNKNOWABLE on [E4-25]** (a 12.6x owner-earnings range) and that is stated in its
      section.
- [x] Step 0: the filing was read - MD&A, cash-flow statement including the non-cash
      supplemental lines, and Notes 10 to 13 - with accession **0000100517-26-000023**, and a
      figure was cross-checked: MD&A "$12.2 billion" against balance-sheet $5,942M + $6,298M
      = **$12,240M**. Second cross-check: capex $(5,874)M on the face of the cash-flow
      statement against the XBRL fact used in the arithmetic.
- [x] Owner earnings on a multi-year mean; **six windows stated**; capex band disclosed as a
      judgment with the D&A end marked INVALID and the reason cited to the filing.
- [x] Competitor row filled - 5 of the 5 remaining scale US competitors, same metric, same
      window, filing-sourced. Not marked PROVISIONAL.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury),
      dated 2026-09-01.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen (Bar 2, the screamer test); **windage count stated: ONE.**
- [x] Prices dated; aggregator used for the live quote only and flagged.
- [x] Run committed to git after every question.
- [x] **Operator rule 9 honoured:** the expectation (Q2 OUT) was pre-registered in writing at
      the head of Q2 before the filings were opened, the disconfirming evidence was hunted and
      is stated first and at full strength in three separate places (the MileagePlus case, the
      peer real-PRASM row, the [E4-43] good-class reading of the 14.8% return), and the run
      says plainly where United is the best operator in its industry.

## REGISTER
- Verdict: **[x] OUT (about the business)**
- One line: **UAL fails [E3-03] criterion (2) - no close substitute - in its own risk
  factors; the nine-year CPI-deflated unit-revenue series shows real PRASM down 6.2% while
  seat-miles rose 25.9% and $40.0 billion of capital was spent to leave real operating income
  0.7% below its 2017-2019 mean.**
- **PASS/FAIL: FAIL. The file closed at Q2 (OUT).**
- **Price: $108.606, 2026-09-02.** Zero-growth value against the sovereign, valid
  constructions: **~$25 to ~$210 per share, judged ~$85-90.** At the [E4-28] floor:
  **~$13 to ~$110, judged ~$46.**
- MileagePlus was tested separately as instructed, on the HOG two-business method, using
  United's own 2020 filed standalone figures ($1,828M of 2019 EBITDA, a registrant-asserted
  $21.9bn valuation). **The test returns one business, not two**: the miles are a claim on a
  United seat (97% of redemptions are travel, 80% of those on United), the margin is an
  intercompany transfer price set for a securitisation, the filer reports **one segment**, and
  the disclosure obligation ended when the notes were redeemed on 2025-07-07.

---
## DEFECTS FOUND - in the tools and in the brief

**1. `tools/sources.py` contradicts `CLAUDE.md` on the USD sovereign, and it is not
cosmetic.** `SOVEREIGN_SOURCES["USD"]` is still `("FRED DGS30", "https://fred.stlouisfed.org/…")`.
`CLAUDE.md` was corrected on 2026-09-02 to make the **US Treasury daily par yield curve** the
source and **FRED the fallback**, on the ground that operator rule 5 requires the issuing
authority and FRED is a Federal Reserve Bank of St. Louis redistribution of a Treasury series.
`tools/daily_fetch.py` was already fixed; `sources.py` was not, and `tools/run.py` calls
`sources.sovereign()`. **Every run driven by `tools/run.py` therefore takes its sovereign from
the wrong rung of the evidence ladder.** In this run the FRED call timed out, which forced the
Treasury fetch and is how the defect surfaced. **Fix: move the Treasury curve into
`SOVEREIGN_SOURCES["USD"]` with FRED as an explicit fallback, mirroring `daily_fetch.py`.**

**2. `Screens/floor_screen.py` defines `level_shift()` and `best_year_dependence()` AFTER the
`if __name__ == "__main__": main()` block.** They are importable but they are never called by
the screen's own CLI path. The two instruments the brief asked for exist and are dead code in
the screen that owns them. They work when imported directly, which is how this run used them.
**Fix: move both above `main()` and wire them into the screen's output, or state in the file
that they are library-only.**

**3. `level_shift()` returns an uninterpretable value when the earlier-window mean is near
zero.** On UAL's nine-year owner-earnings series it returned **−7.58** and the verdict string
"STEP DOWN", because the 2017-2021 mean is −$543M. A ratio of two means straddling zero has no
meaning and the function's guard only tests `earlier == 0` exactly. **Fix: return `None` (or a
distinct verdict) when the earlier mean is negative or when `abs(earlier)` is small relative to
the series dispersion.** This run worked around it by re-running on the COVID-excluded window
and saying so.

**4. `tools/run.py` uses `WeightedAverageNumberOfDilutedSharesOutstanding` for the share
count.** For UAL the diluted figure carries warrant and convertible dilution and differs
materially from the 10-Q cover-page `dei:EntityCommonStockSharesOutstanding` used here
(324,583,772). Not wrong, but the two are different questions and the run file does not say
which one produced the market cap. **Fix: print both and label them.**

**5. In the brief - the `RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability` tag is not
where the leakage is for this filer.** The instruction to check it was right in spirit and
wrong in target. UAL's finance-lease activity is small ($474M of total finance lease
liabilities at 2025-12-31). **The material non-cash fleet acquisition is in OPERATING leases:
$1,901M of ROU assets acquired in 2025**, disclosed on the face of the cash-flow statement
under "Investing and Financing Activities Not Affecting Cash", plus $427M of sale-leaseback
gains in Note 13. A run that checked only the finance-lease tag would have found $(25)M and
concluded there was no leakage. **The general rule the brief was reaching for is: read the
supplemental non-cash schedule at the foot of the cash-flow statement, not a specific tag.**

**5b. In the brief - the claim that United "published audited standalone figures" for
MileagePlus is FACTUALLY WRONG, and it is the load-bearing premise of the whole two-business
instruction.** It did not. It published a **lender presentation exhibit** with no audit report
(accession 0001104659-20-073190, Ex. 99.1), restated it eight days later
(0001104659-20-075889, Ex. 99.2), and never filed the 144A memorandum. Neither MileagePlus
entity is an EDGAR registrant. A run that took the brief at its word would have cited
"audited" figures that do not exist, which is a PRIME RULE 1 exposure. **The instruction
should read: "United published selected MileagePlus financial data in a Reg FD lender
presentation."** The finding survives - the data is filed and signed by the registrant, one
rung down the ladder - but the label must be corrected. **The technical detail that decided
the analysis is one the brief could not have anticipated: MPH's standalone deferred revenue
($6,161M) exceeds UAL's consolidated ($5,276M) at 2019-12-31, unreconciled.**

**6. In the brief - SAVE (Spirit) no longer files as a comparable going concern**, and the
brief's own hedge ("if it still files") turned out to be the finding rather than a caveat. The
US industry no longer has the eight competitors **[E3-28]** asks for. That is a fact about
consolidation and it was recorded in the competitor row rather than treated as missing data.

**7. Restatement variance, disclosed rather than silently resolved.** `sources.annual()`
returns UAL FY2017 operating income of **$3,498M** and revenue of $37,736M; the peer file,
built from the latest-filed comparative (ASC 606 full retrospective restatement), carries
**$3,618M** and $37,784M. The Q2 real-operating-income table uses the former. Recomputed on
the latter, the 2017-2019 real mean is $4,770M against 2025's $4,713M - **−1.2% instead of
−0.7%.** The conclusion does not move; the variance is recorded because **[E4-38]** requires
the window and the basis to be visible.

