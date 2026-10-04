# Company Run — DICK'S SPORTING GOODS, INC. (DKS) — 2026-09-02
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Standing instruction for this run: `Test Runs/ADDENDUM 2026-09-02 - DKS and PINS re-priced,
and a THIRD perimeter class the guards cannot see.md` — **build owner earnings pro forma,
or state precisely why not.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.27 %** · date **2026-09-01** · source **US Treasury daily par yield curve, 30-year
  constant maturity, fetched from home.treasury.gov (the issuing authority)**. The 20-year
  reads 5.27% the same day. FRED DGS30 was tried first and refused the connection —
  **and FRED is the fallback, not the source, so going to Treasury is up the evidence
  ladder, not around it** (CLAUDE.md, corrected 2026-09-02).
- FX: none. DKS reports in USD. Foot Locker's International segment earns in EUR/GBP/JPY/AUD
  but is consolidated and translated; **2.8 million square feet of 58.9 million, 4.8%.**

**Currency note.** The Foot Locker International business is ~16% of Foot Locker's owned
store count and earns abroad. It is not separately reported at the cash-flow line, so no
second sovereign is struck. Recorded, not hidden.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Form 10-K, fiscal year ended 2026-01-31, filed 2026-03-27, accession
  0001089063-26-000007, document `dks-20260131.htm`.**
- **Form 10-Q, 13 weeks ended 2026-05-02, filed 2026-06-04, accession
  0001089063-26-000027, document `dks-20260502.htm`.**
- **Form 8-K, 2026-08-25, accession 0001089063-26-000033** (Q2 fiscal 2026 results —
  the first quarter containing Foot Locker's back-to-school season).
- Foot Locker Inc. pre-acquisition 10-Ks (CIK 0000850209) for the attacker row.

**Figures cross-checked against the filed statement** (three, not one):
1. **Cash flow, fiscal 2025:** operating cash flow **$1,537,343k**; capital expenditures
   **$(1,137,176)k**; D&A **$488,630k**; stock-based compensation **$123,667k**. Read off
   the Consolidated Statements of Cash Flows, page 60 of the 10-K.
2. **The acquisition line, read directly** (brief test 7): the investing section reads
   **"Cash acquired from acquisition of Foot Locker, net of cash paid  257,095"** — a
   **positive $257.1 million inflow.** **CONFIRMED FROM THE STATEMENT: $2.5 billion of
   purchase consideration appears nowhere in the fiscal 2025 cash-flow statement.** The
   deal was paid in stock (9.6 million DKS shares) and in cash that was more than replaced
   by Foot Locker's own balance-sheet cash. `acquisition_flag()` fires on the sign, not
   the size, exactly as the addendum predicted.
3. **Stage 0 share classes, hand-read off the 10-Q cover, verbatim:**
   > *"As of May 29, 2026, DICK'S Sporting Goods, Inc. had 65,931,904 shares of common
   > stock, par value $0.01 per share, and 23,570,633 shares of Class B common stock, par
   > value $0.01 per share, outstanding."*

   **65,931,904 + 23,570,633 = 89,502,537. The operator's hand-read is confirmed exactly.**
   companyfacts carries no `dei:EntityCommonStockSharesOutstanding` for DKS at all; its
   `us-gaap:CommonStockSharesOutstanding` fallback is **93,768,978 at 2011-01-29**, fifteen
   years and seven months stale. Verified independently: that tag's entire history in
   companyfacts is `{2010-01: 89.77M, 2011-01: 93.77M}` and stops.

**Price.** $136.92, 2026-09-02, aggregator quote (flagged, operator rule 5 — aggregators for
live quotes only). **Market capitalisation $12,255M.**

**ASC 842 — brief test 4.** Finance-lease liability went **$0 (fiscal 2024) → $39.2M
(fiscal 2025)**, arriving with Foot Locker; payments on financing lease obligations were
**$1.142M** in the year. Against **$1,137.2M of cash capex** the finance-lease channel is
**3.4% of one year's capex and 0.1% of the cash outflow**. **Immaterial for the fifth run
running.** Stated, as instructed, rather than silently skipped.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.**

DICK'S buys athletic footwear, apparel and hard goods from brands it does not own — Nike
above all — puts them in large leased boxes near affluent suburban interchanges, and sells
them at a mark-up. On the DICK'S Business alone in fiscal 2025: **$14,108.9M of sales,
$5,126.3M of gross profit (36.33%), $1,568.4M of segment profit (11.12%)**. Roughly
36 cents of every sales dollar survives the cost of the goods and the rent; 25 cents goes
to payroll, marketing and corporate; 11 cents is left. That 11 cents is the whole business.

The company does not manufacture. It does not own most of its real estate — it leases
**substantially all** of its stores, on leases running to 2043, and it discloses that
**"approximately three-quarters of our DICK'S Sporting Goods stores will be up for lease
renewal at our option over the next five years."** It does not own the brands customers
come for. What it owns is **shelf space, allocation, and the customer's habit of driving
to it.**

The second business, bought 2025-09-08, is Foot Locker: **2,561 stores, 13.5 million
square feet**, mall-based sneaker retail across North America, Europe and Asia. Same
economics, worse: **24.43% gross margin against DICK'S 36.33%, and a segment LOSS of
$52.2 million** in the four-and-a-half months owned.

**The scarce input this business controls.**

Not the product. **Nike, Adidas, Hoka, On and Brooks own the product**, and the 10-K's own
risk factors say so. What DICK'S controls is two things and they are both physical:

1. **Trade-area position** — 888 DICK'S-Business boxes over 45.5 million square feet, with
   long leases at option, in catchments where a second 50,000-square-foot sporting goods
   box is not economic. This is a *local* scarcity, replicated 888 times, not a national one.
2. **The scale of the order book** — $17.2 billion of purchasing gives it first call on
   constrained allocations, and it is the reason vendors give it exclusive product.

Both are real. **Neither is owned outright**, and criterion 2 of [E3-03] will be tested at
Q2 against precisely this: the input is scarce, but the *supplier* controls it.

**Will the fundamentals look broadly the same in ten years?**

Yes, in kind. People will still buy running shoes, youth-sports equipment and golf clubs;
they will buy some of them in stores. The *format* is changing fast (House of Sport, Field
House, and on the other side direct-to-consumer brand sites), and the mix between the two
is genuinely uncertain — but the question [E3-31] asks is whether the business is
**"relatively simple and stable in character."** Buying goods wholesale and selling them
retail out of leased boxes is the oldest legible business on the shelf. There is no
technology I cannot follow, no reserve that must be estimated, no float.

**One clarification against [E4-46].** This is not a business that would take five months
to learn. Every number that matters is on two pages of the 10-K. The Foot Locker overlay
is an *arithmetic* complication (a five-month stub inside a twelve-month year), not a
comprehension one — and the company filed the pro forma table that resolves it.

- **VERDICT: [x] IN**

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that "(1) is needed or desired; (2) is thought by its
> customers to have **no close substitute** and; (3) is not subject to price regulation."

**I was asked to argue against the prior that this closes at Q2, and to hunt disconfirming
evidence hardest [E4-26]. I have. The disconfirming case is written out first and in full,
because it is real. It does not survive the second criterion.**

---
### THE CASE FOR THE FRANCHISE — built as strongly as the filings allow

1. **The DICK'S Business comps are positive on BOTH legs.** Fiscal 2025 +4.5% = +4.2% sales
   per transaction **and +0.3% transactions**. Fiscal 2024 +5.2% = +4.0% and **+1.2%**.
   Q2 fiscal 2026, reported 2026-08-25: **+4.9%, "growth in average ticket and
   transactions."** Under [E4-55] the physical series is the honest one, and DICK'S physical
   series is **positive**: comparable transactions compound **+11.7% over ten years**.
   Precision Steel went 69M pounds to 46M. This is not that.
2. **The deflated physical test does not replicate.** Real sales per square foot went
   **$270 → $310 (+15%)** over ten years in January-2026 dollars, and real sales per store
   **+19%**. The DG instrument — five straight real declines ending below the start — finds
   nothing here. **Reported as a negative result, as instructed.**
3. **Gross margin expanded 744 basis points**, 28.9% (fiscal 2018) to 36.33% (DICK'S
   Business, fiscal 2025), while sales grew 67%. That is not the signature of a business
   with no pricing power.
4. **Segment profit margin 11.12%** on the DICK'S Business — roughly double most of the
   competitor row.
5. **House of Sport is genuinely differentiated** and it is scaling: 19 → 35 → 41 stores in
   two years, Field House 27 → 42 → 52. The capex depressing the bottom boundary is
   substantially **growth** capex, not renewal.
6. **Vertical brands are $1.8 billion, 13% of DICK'S Business net sales, "at higher gross
   margins as compared to sales of similar products from national brands."** That is owned
   product, not resold product.
7. **On the attacker metric, standalone DICK'S is near the top of its own industry:**
   **35.6%** in fiscal 2024, against Shoe Carnival 17.7%, Designer Brands 6.0%, Foot Locker
   4.7%, Genesco 2.6%, Sportsman's Warehouse −4.1%, Big 5 −22.0%.
8. **The field has thinned.** The Sports Authority liquidated 2016. Modell's and Gander
   Mountain are gone. Hibbett was taken by JD Sports in 2024. Big 5 went private after two
   years of operating losses. **DICK'S is the last large-format national sporting-goods
   chain**, which is the [E2-53] dominance argument in its strongest form.

**That is a serious case, and points 1, 2 and 3 each refute a specific instrument this
project has used to close other files. I record that plainly.**

---
### CRITERION 1 — NEEDED OR DESIRED: **YES**
Athletic footwear, team-sports equipment, golf, apparel. Recurring, replacement-driven,
child-growth-driven. No argument against it.

### CRITERION 3 — NOT PRICE-REGULATED: **YES**
No rate regulation of any kind. [E2-59] does not apply in either direction.

### CRITERION 2 — NO CLOSE SUBSTITUTE: **NO. This is where the file closes.**

**(a) The company's own risk factor names its suppliers as its competitors.** Verbatim,
fiscal 2025 10-K:

> *"We operate in a highly fragmented, intensely competitive and rapidly evolving global
> marketplace. We operate a number of different store formats and compete with an expanding
> set of retailers and other potential competitors across multiple formats and channels —
> including large-format, specialty and traditional retailers; mass merchants; department
> stores; and online and direct to consumer sellers, **including vendors**."*

**(b) The scarce input is controlled by the supplier, and the dependence has grown every
year.** Nike as a share of merchandise purchases, transcribed from nine consecutive 10-Ks:

| fiscal year | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| **Nike, % of merchandise purchases** | 18% | 19% | 21% | 19% | 17% | 23% | 24% | 25% | **31%** |

And, in the same paragraph every year: *"We do not have long-term purchase contracts with
any of our vendors; all of our purchases from vendors are made on a short-term purchase
order basis."* **The one input that makes the store worth driving to is bought on short-term
purchase orders from a supplier that is 31% of the book and sells direct.**
Foot Locker's own last 10-K puts its Nike concentration at **59%, down from ~72% in 2015** —
because Nike cut it back, then partly returned. That is what supplier power looks like when
it is actually exercised, and DICK'S has just bought the company it was exercised on.

**(c) THE DECISIVE FACT, and it is one week old.** From the 8-K of **2026-08-25**
(accession 0001089063-26-000033), verbatim:

> *"As the quarter progressed, conditions across portions of the athletic footwear and
> apparel marketplace became increasingly promotional, and **we took action to remain
> competitively priced** to protect and grow our leadership position."*

**[E4-37] is the inverse metric — the strength of a business is measured by "the agony they
go through in determining whether a price increase can be sustained."** DICK'S did not
agonise over a price increase. It **matched a competitor's price cut and said so in the
headline of its own release.** A product its customers thought had no close substitute would
not require that. And the cost sits on the same page: **DICK'S Business segment margin fell
42bp in the quarter and 54bp in the half, on comps of +4.9% and +5.4%** — segment profit
**+1.3% on +6.0% more sales**. **Volume up, price surrendered.** That is what a close
substitute being available looks like in a filing.

**(d) The competitor row — required [E3-28], same metric, same window, filing-sourced.**
Return on unleveraged net tangible operating assets **[E2-43]** = operating income ÷ (net
PP&E + inventories + receivables − payables), with operating-lease right-of-use assets
excluded from every denominator identically. Full working, tag substitutions and accession
numbers: `Test Runs/_research 2026-09-02 DKS/03 - competitor row, attacker metric.md`.

**FISCAL 2024 — the last clean standalone year, same window for all:**

| company | FYE | operating income $M | denominator $M | **return** |
|---|---|---:|---:|---:|
| **Academy Sports (ASO)** | 2025-02-01 | 538.6 | 1,238.3 | **43.5% — 1st** |
| **DICK'S, standalone** | 2025-02-01 | 1,473.9 | 4,136.3 | **35.6% — 2nd** |
| Boot Barn (BOOT) | 2025-03-29 | 239.4 | 1,045.1 | 22.9% |
| Shoe Carnival (SCVL) | 2025-02-01 | 91.2 | 515.4 | 17.7% |
| Designer Brands (DBI) | 2025-02-01 | 34.9 | 586.8 | 6.0% |
| **Foot Locker (FL)** | 2025-02-01 | 103.0 | 2,213.0 | **4.7%** |
| Genesco (GCO) | 2025-02-01 | 13.9 | 534.0 | 2.6% |
| Sportsman's Warehouse (SPWH) | 2025-02-01 | (18.2) | 448.2 | −4.1% |
| Big 5 (BGFV) | 2024-12-29 | (55.6) | 252.6 | −22.0% |

**FISCAL 2025 — the current year:**

| company | FYE | operating income $M | denominator $M | **return** |
|---|---|---:|---:|---:|
| **Academy Sports (ASO)** | 2026-01-31 | 512.2 | 1,484.8 | **34.5% — 1st** |
| Boot Barn (BOOT) | 2026-03-28 | 299.1 | 1,231.9 | 24.3% |
| **DICK'S, consolidated** | 2026-01-31 | 1,095.9 | 6,909.5 | **15.9%** |
| Shoe Carnival / Shoe Station | 2026-01-31 | 66.8 | 552.4 | 12.1% |
| Designer Brands (DBI) | 2026-01-31 | 47.8 | 600.1 | 8.0% |
| Genesco (GCO) | 2026-01-31 | 17.3 | 554.6 | 3.1% |
| Sportsman's Warehouse (SPWH) | 2026-01-31 | (37.4) | 405.6 | −9.2% |
| *Hibbett — last filed before JD Sports* | *2024-02-03* | *137.0* | *448.6* | *30.5%* |
| **the attackers, carried from the NKE run** | | | | Deckers **166.3%** · Lululemon **61.5%** · On **52.4%** · **NIKE 26.0%** |

**Nine filers taken, of an industry with roughly ten remaining US public participants.**
Named as unavailable, with the obstacle: **Hibbett** (acquired by JD Sports July 2024 — last
10-K carried); **Big 5** (taken private 2025 — last 10-K carried); **JD Sports plc** and
**Amazon** (not SEC registrants for this segment); **On Holding** files under IFRS with no
`us-gaap` tags, so its 52.4% is carried from the NKE run rather than reproduced. The moat
class is **not** held PROVISIONAL for these four: none of them would raise DICK'S ranking,
and two of them (JD, Amazon) sharpen the substitute finding rather than soften it.

**Adjusted, so the row is not read unfairly against DICK'S.** The 15.9% is not like-for-like:
it carries a full Foot Locker balance sheet against five months of Foot Locker income plus
$382.1M of acquisition charges sitting inside operating income. Adding those charges back per
the proxy's own Appendix A gives non-GAAP operating income of **$1,516.2M and a return of
21.9%.** **Even on the flattering construction, DICK'S ranks below Academy Sports and below
NIKE** — the supplier that is 31% of its purchases.

**(e) Direction outranks existence [E4-32].** *"the moat widened every year"* is *"the
primary criterion of a great business."* DICK'S own series, eight years:

| fiscal year | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| return on unlev. net tangible operating assets | 17.5% | 14.1% | 36.2% | **84.6%** | 48.6% | 38.7% | 35.6% | **15.9%** |

**Peak in fiscal 2021, then four consecutive declines, then a halving.** Operating margin
peaked at **16.55%** in fiscal 2021 and is **11.12%** on the DICK'S Business today — **543
basis points off the peak**. Nike concentration up 13 points. **The moat is narrowing on
every measure computable from the filings.**

**(f) [E4-36] and [E3-51] — which of the four causes of extreme success is this?** The
fiscal 2020–21 numbers are a **wave**: a pandemic sporting-goods boom on top of The Sports
Authority's liquidation, plus stimulus, which the company itself names — *"a favorable sales
impact in fiscal 2021 following government stimulus payments"*. *"when a surfer gets up and
catches the wave and just stays there, he can go a long, long time. But if he gets off the
wave, he becomes mired in shallows"* **[E3-51]**. The 84.6% was the wave. The 15.9% is the
shallows. **A surfing run is not a moat; the advantage lived in the wave, not the surfer.**

**(g) [E4-04] — does the spending defend the same advantage, or buy its replacement?**
This is the test that settles the House of Sport argument, and it settles it against the
name. Core DICK'S stores: **677 → 644 → 630**. House of Sport: **19 → 35 → 41**. Field
House: **27 → 42 → 52**. Capex against D&A: **1.49x → 2.01x → 2.33x**, guided to **~$1.6
billion gross for fiscal 2026 against $488.6M of D&A — 3.3x**. DICK'S is not maintaining a
store base; **it is demolishing and rebuilding it.** Under the scope the corpus sets —
*Mitsui's Rhodes Ridge buys a replacement deposit; Coca-Cola's advertising defends the same
trademark* — **the 50,000-square-foot DICK'S box is Rhodes Ridge.** The capital is buying the
next moat, not defending the one it has.

**(h) [E2-53], the dominance class, tested and refuted by the filing itself.** *"Once
dominant, the newspaper itself, not the marketplace, determines just how good or how bad the
paper will be. Good or bad, it will prosper."* On **2026-08-25** DICK'S **held its DICK'S
Business comparable-sales guidance at +2.5% to +4.0% and simultaneously CUT its DICK'S
Business segment-profit guidance from $1.58–1.66bn to $1.54–1.60bn**, for a reason it stated
as external: the marketplace turned promotional. **The marketplace determined how good the
year would be, not the position.** The dominance class fails its own test in the current
quarter.

**(i) [E3-33] / [E5-28] — untapped pricing power?** No. The claim requires *"a monopoly or a
near monopoly"*, and the row above holds nine filers plus JD Sports plus Amazon plus every
brand selling direct. Management is not declining to raise prices out of restraint; it has
just cut them.

**(j) The acquired half, on the same instruments.** Foot Locker's own disclosed sales per
gross square foot — a named line of its Item 6, seventeen years, every year confirmed in two
overlapping filings with no restatement:

| FL fiscal year | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|---|---|---|---|---|---|
| nominal $/gross sq ft | 515 | 495 | 504 | 510 | 417 | 540 | 548 | 510 | **507** |
| **real, Jan-2026 dollars** | **690** | 650 | 651 | 643 | 518 | 625 | 596 | 538 | **519** |

**Nominal: −1.6% over eight years. Real: −24.7%.** **THE DG INSTRUMENT REPLICATES ON FOOT
LOCKER EXACTLY AS IT DID ON DOLLAR GENERAL — nothing visible nominally, a quarter of the
productivity gone in real terms.** Foot Locker's comps chained **+6.9% over nine years
against CPI +30.8%: −18.3% real.** Its stores went **3,363 → 2,410, −28.3%.** Its operating
income went **$1,000M (fiscal 2016) → $103M (fiscal 2024), −90%.** Its return on unleveraged
net tangible operating assets was **4.7%**, eighth of nine in its own industry.

**DICK'S paid $2.5 billion for that**, and in the eleven months since has reported: a
**−$52.2M segment loss** on the stub; pro forma comps **−3.3%** (International **−8.1%**);
Q2 fiscal 2026 pro forma comps **−3.6%**, *in the quarter that finally includes
back-to-school*; **104 owned stores closed in six months** (WSS alone 143 → 99); and a
segment-profit guidance revision from **+$100–150M to −$80M to −$40M**. **The perimeter
question the addendum posed is answered: Foot Locker SUBTRACTS owner earnings, so the
screen's 4.34% was biased UPWARD, not downward.**

---
### CLASS AND DIRECTION
- Needed or desired **[x]** · no close substitute **[ ] FAILS** · not price-regulated **[x]**
- Must the moat be continuously rebuilt? **Yes — and it is being rebuilt right now, in
  concrete, at 2.3x depreciation rising to 3.3x [E4-04].**
- Does success depend on a great manager? Not decisively; recorded at Q3 as an overlay.
- **Class: [x] NONE.** *(Not NARROW: a narrow moat still needs criterion 2 to hold in some
  degree, and the company cut price into a promotional market in the most recent quarter.)*
- **Direction: NARROWING** on every filed measure — returns, margin, supplier concentration,
  and the acquired half.

### THE LIMIT OF THE ROW, STATED [E3-61]
*"In some businesses, the participants behave like a demented Kellogg. In other businesses,
they don't … I think you'd have to know the people involved."* The row shows position, not
conduct. It cannot tell me whether the athletic-footwear marketplace stays promotional. What
it does show is that DICK'S is **not** the price-setter in it — which is the criterion-2
question, and is answerable from the row.

### WHAT WOULD REOPEN THIS FILE
Named, so it can be reopened honestly rather than by mood: **(1)** DICK'S Business segment
margin sustained above 12% through a promotional cycle **without price-matching**; **(2)**
Nike concentration falling below 20% while vertical brands pass 25% of sales; **(3)** Foot
Locker at a positive segment profit for four consecutive quarters. All three are observable
in the quarterly 8-K. **None is true today.**

- **VERDICT: [x] OUT** — criterion 2 of **[E3-03]** fails. Permanent, per the four-verdict
  table.

⛔ **The file closes here. Q3, Q4 and Q6 are not gates that were passed; what follows Q5 is
recorded because the tests were run and the operator asked for their results, and it carries
no verdict.**

---
## Q3 · Q4 · Q6 — NOT OPENED

**Operator rule 2: the hard sequence.** Q2 returned OUT, so Q3, Q4 and Q6 do not open and
carry no verdict. What follows under those headings is **the result of tests the operator
commissioned by name**, recorded because a test that was run gets reported. **None of it is
a gate, and none of it can reopen Q2** — and under the guardrail nothing in a Q3 finding
could promote this name in any case **[E2-37, E2-38, E3-39]**.

### TEST 6 — PAY VERSUS PERFORMANCE, AND WHETHER THE INCENTIVE METRIC IS THE REPORT METRIC **[E2-49]**
Source: DEF 14A filed 2026-05-01, accession 0001089063-26-000015.

**The metric.** The 2025 short-term incentive plan runs on **Adjusted Non-GAAP EBT**, which
the proxy states is *"further adjusted to account for the effect of changes in tax law or
foreign trade law (including certain impacts of tariffs), unbudgeted interest and fees
related to financing activities, and other nonrecurring legal and business development
costs, **operating results of acquired companies** and asset write-downs."*

**So the largest capital-allocation decision in the company's history is excised, by name,
from the measure that pays the people who made it.** The achieved figure, **$1,560.9M**, is
identical to Appendix A's *"Non-GAAP basis for DICK'S Business"* income before income taxes —
Foot Locker removed in full, plus the $390.0M of acquisition charges, plus the $13.4M
write-down.

**The bullseye itself is fair, and that is worth saying.** The goal levels are published (in
a graphic, not in text — I read them off `dks-20260501_g117.jpg`): threshold **$1,278M**,
target range **$1,437M–$1,597M**, maximum **$1,757M**, achieved **$1,560.9M**, payout
**100% of target**. The target band brackets the prior year's actual pre-tax income of
$1,519.0M. **This is not the ULTA pattern of a target set below the prior year's outturn.**
The objection is to the metric's construction, not to where the bullseye was placed.

**The Pay Versus Performance table, transcribed:**

| fiscal year | CAP to PEO | TSR on $100 | peer-group TSR | **net income $M** | **Adjusted Non-GAAP EBT $M** |
|---|---:|---:|---:|---:|---:|
| 2021 | 32,721,261 | 281 | 161 | 1,520 | 2,025 |
| 2022 | 12,575,614 | 320 | 155 | 1,043 | 1,447 |
| 2023 | 23,065,140 | 407 | 179 | 1,047 | 1,433 |
| 2024 | 36,086,981 | **640** | 211 | 1,165 | 1,550 |
| **2025** | **9,558,359** | **350** | 180 | **849** | **1,561** |

**In fiscal 2025 the reported result and the paid-on result move in opposite directions.**
Net income **−27.1%**; diluted EPS **−29.0%**; shareholder return **−45.3%** ($640 → $350).
**Adjusted Non-GAAP EBT: +0.7%, and the cash bonus paid at 100% of target.** That is the
[E2-49] mechanism operating exactly as described — *"Yardsticks seldom are discarded while
yielding favorable readings"* — and it is worth pairing with [E4-27], *"Never, ever, think
about something else when you should be thinking about the power of incentives."*

**The counterweight, stated because it is true:** compensation actually paid to the PEO fell
from $36.1M to $9.6M, because the equity is marked to the share price. **The equity leg is
aligned; the cash leg is not.**

**Two new metrics appeared in the 2025 long-term plan** — *"External Merchandise Margin"*
and *"eCommerce Comp Sales Growth"*, each introduced in the proxy's own words as *"a new
metric"*, the second explained as *"an area of greater company focus, given the current
competitive landscape."* Recorded as an [E2-49] prompt to read, not as a verdict.

### THE METRIC THAT WAS DROPPED — a second [E2-49] observation
DICK'S published **"Net sales per square foot"** as a named line of Item 6 for years:
**$186 (fiscal 2013) · $185 · $181 · $182 · $178 · $167 (fiscal 2018)** — six consecutive
declines. **The line is absent from the fiscal 2019 10-K**, whose Item 6 retains same-store
sales, store count and total square footage and drops only that row. The SEC's elimination
of Item 301 did not take effect until February 2021 and does not explain it.

### THE RESTRUCTURING SEQUENCE **[E3-53, E5-33, E2-57]**
fiscal 2014 golf restructuring · fiscal 2016 $46.4M inventory write-down + $32.9M store
impairment · fiscal 2017 $7.1M severance · fiscal 2022 Field & Stream exit $30.1M · fiscal
2023 business optimization $84.8M · fiscal 2025 Foot Locker acquisition charges $390.0M +
$13.4M technology-contract write-down · fiscal 2026 "Organizational Alignment" $45–55M plus
*"charges incurred to redesign the store operating model for the DICK'S Business."*
**Seven of the last twelve fiscal years carry an add-back.** Under [E5-33] these are real
costs and they stay in the owner-earnings mean below; they are not annualised away.

### FLAGS THAT DO **NOT** FIRE — recorded, because absence is evidence too
- **[E4-29] EBITDA:** the word does not appear in the fiscal 2025 10-K, the Q1 10-Q or the
  2026-08-25 earnings release. **Zero EBITDA promotion.** Clean.
- **[E5-15] serial issuance:** the opposite. Diluted shares **107.6M (fiscal 2017) → 85.1M
  (fiscal 2025)**, −20.9%, *including* the 9.6M shares issued for Foot Locker.
- **[E2-52] dividends funded by issuance:** no. Dividends $413.9M and buybacks $347.1M in
  fiscal 2025 against $1,537.3M of operating cash flow, with no net share issuance.
- **[E4-30] cash-tax tell:** cash taxes paid $243.2M / $399.5M / $255.8M against pre-tax
  income of $1,318.2M / $1,519.0M / $1,142.0M = **18.5% / 26.3% / 22.4%.** No falling trend.
- **Unintelligible footnotes:** no. The proxy's Appendix A quantifies every adjustment at
  every line for five years, which is the **[E2-26] half-owner test passing.**
- **Reported growth unnaturally smooth [E4-30]:** no. It is conspicuously lumpy.

### THE CAPITAL-ALLOCATION FLAG **[E5-08] condition 2** — stated with the humility clause
In the 26 weeks to 2026-08-01 the company **repurchased 0.7 million shares at an average
price of $196.38**, for $141.2M, with **$3.0 billion of authorisation remaining**. The share
price on 2026-09-02 is **$136.92** — **30% below the average paid, six months later** — and
the conservative end of the computation below is **$107 per share**. Under [E5-08] the
second condition is a **material discount to conservatively calculated intrinsic value**, and
[E5-24]'s first law is that *"what is smart at one price is dumb at another."*
**Condition 2 fails on our own range. FLAG RAISED.** Carried with **[E4-13]**: this rests on
our range, and *"it is natural for CEOs to be optimistic about their own businesses. They
also know a whole lot more about them than I do"*, and with [E5-08]'s own hedge that *"many
CEOs never stop believing their stock is cheap."* **The flag binds position size, never the
discount rate** — and here it binds nothing, because Q2 already closed the file.

**[E5-44], the stock-deal law, named and not resolved:** *"The intrinsic value of the shares
you give in an acquisition must not be greater than the intrinsic value of the business you
receive."* DICK'S gave **9.6 million shares** plus cash for a business that earned **$103M
of operating income on $7,988M of sales** in its last standalone year, down from **$1,000M
in fiscal 2016**. Whether the paper given exceeded the value received is a judgment this run
does not need to reach, because Q2 closed. **It is named so it is not missed.**

---
# COMPUTATION — NOT A CLEARANCE
**Operator rule 3.** Q2 returned OUT. Everything below is arithmetic. **It carries no entry
language, it is not a valuation opinion for action, and it does not reopen any question.**
It is produced because the queue's output contract requires a price from every run.

## THE PERIMETER PROBLEM, SOLVED — owner earnings ON A PRO FORMA BASIS
The addendum's instruction was **"build owner earnings pro forma, or state precisely why
not."** It is built.

**Method.** Owner earnings = **operating cash flow − stock-based compensation − (c)**, the
project's standing CONVENTION, with (c) shown at **both** ends of the corpus band: D&A, the
default **[E3-44, E2-41]**, and **total capex**, the conservative end. DICK'S and Foot Locker
have fiscal years ending within days of each other, so the two standalone records align
without adjustment. Foot Locker's figures are from **its own 10-Ks** (CIK 0000850209), capex
tagged `PaymentsToAcquireProductiveAssets`, and the CFO-less-capex row reproduces Foot
Locker's own disclosed "Free cash flow" line to the dollar. Full working:
`Test Runs/_research 2026-09-02 DKS/04 - Foot Locker standalone, from its own 10-Ks.md`.

**No landlord double-count.** Construction allowances from landlords sit **inside** operating
cash flow ($161.7M / $76.3M / $67.1M in fiscal 2025/24/23) and capex is taken **gross**, so
OCF − gross capex nets them once and correctly. The company's own "net capital expenditures"
is not used, which would have double-counted the allowance. **Recorded because it is the
kind of error this project has made before.**

### The two records, standalone, $M

| fiscal year | **DICK'S** OE (D&A end) | OE (capex end) | **Foot Locker** OE (D&A end) | OE (capex end) |
|---|---:|---:|---:|---:|
| 2021 | 1,241.5 | 1,255.8 | 440.0 | 428.0 |
| 2022 | 505.8 | 507.2 | **(66.0)** | **(143.0)** |
| 2023 | 1,076.1 | 882.6 | **(121.0)** | **(164.0)** |
| 2024 | 840.4 | 438.2 | 122.0 | 84.0 |
| 2025 | 925.0 | 276.4 | *acquired 2025-09-08 — inside DICK'S column* | |

**Foot Locker's own last three standalone years produce owner earnings of −$66M, −$121M and
+$122M at the D&A end and −$143M, −$164M and +$84M at the capex end. Two of the three are
negative on both constructions.**

### PRO FORMA COMBINED, $M

| fiscal year | OE (D&A end) | OE (capex end) |
|---|---:|---:|
| 2021 | 1,681.5 | 1,683.8 |
| 2022 | 439.8 | 364.2 |
| 2023 | 955.1 | 718.6 |
| 2024 | 962.4 | 522.2 |
| 2025 *(as reported; five months of Foot Locker inside, and the $390.0M of acquisition charges kept in per [E5-33])* | 925.0 | 276.4 |

| window | D&A end | **capex end** |
|---|---:|---:|
| **five-year, FY2021–FY2025** *(the corpus default [E2-42])* | **$992.6M** | **$713.0M** |
| four-year, FY2021–FY2024 *(both filers standalone)* | $1,009.7M | $822.2M |
| **three-year, FY2023–FY2025** | $947.5M | **$505.7M** |

**COMBINED RANGE: $506M to $1,010M. Spread at the conservative end across windows: 41%.
Full band width: 100%.** Under **[E4-25]** the window spread and the capex band together
*are* the range, and this one is wide because a distorted year sits in it — three of them,
in fact: fiscal 2021's stimulus wave, fiscal 2025's five-month perimeter change, and the
fiscal 2023–2025 capex step from $587M to $1,137M.

### WHAT THE PRO FORMA ANSWERS
The addendum said the direction of the screen's bias *"is not determinable from the screen."*
It is determinable from the filings, and here it is:

- **Foot Locker's four-year mean standalone owner earnings are +$93.8M (D&A end) and +$51.3M
  (capex end).** Against **$2.5 billion of consideration** that is **3.8% and 2.1%** — both
  **below the 5.27% government bond**, before a dollar of the $500–750M of acquisition
  charges.
- **Forward, it is negative.** Guidance of 2026-08-25 puts Foot Locker segment profit at
  **−$80M to −$40M** with **~$0.4bn of capex** in fiscal 2026.
- **Therefore the screen's 4.34% bottom boundary was biased UPWARD, not downward.** The
  pro forma bottom boundary is **4.13%**. The addendum's worry was correct in principle; the
  magnitude is small and the sign is the unfavourable one.

### THE (c) JUDGMENT — DISCLOSED, as [E2-23] requires
> *"(c) must be a guess — and one sometimes very difficult to make."*

**Capex against D&A: 0.96x · 1.00x · 1.49x · 2.01x · 2.33x, guided to ~3.3x in fiscal 2026.**
**Capex is emphatically the conservative end on this name, and the D&A end is the generous
one** — the reverse of the [E5-20] railroad case, and the operator's brief settles the
direction correctly.

**But the two ends are not equally legitimate here, and the reason comes from Q2.** [E2-23]
puts in (c) whatever *"the business requires to fully maintain its long-term competitive
position and its unit volume."* Q2(g) found that DICK'S is **converting** its estate — core
boxes 677 → 644 → 630 while House of Sport goes 19 → 35 → 41 — because the 50,000-square-foot
box is losing to the format. **If the conversion is required to hold position, it is in (c)
by the definition's own words, whatever the accounting calls it.** Against that: when the
estate was *not* being converted, in fiscal 2021 and 2022, **capex ran at 0.96x and 1.00x of
D&A** — direct filed evidence that steady-state maintenance for this business is about equal
to depreciation.

**Judgment, disclosed: (c) sits nearer the capex end than the D&A end, and the honest
central figure is roughly $700–800M.** Both ends are carried, per [E4-25]. **The band does
change the answer, which under the template is itself a finding.**

### 1. THE YIELD
| construction | owner earnings | ÷ $12,255M cap | vs the 5.27% sovereign |
|---|---:|---:|---:|
| **bottom boundary [E5-34]** — 3y, capex end | **$505.7M** | **4.13%** | **−1.14 pts** |
| 5y, capex end *(default window)* | $713.0M | 5.82% | +0.55 pts |
| 4y, capex end | $822.2M | 6.71% | +1.44 pts |
| 3y, D&A end | $947.5M | 7.73% | +2.46 pts |
| 5y, D&A end | $992.6M | 8.10% | +2.83 pts |
| 4y, D&A end | $1,009.7M | 8.24% | +2.97 pts |

**[E5-34] prices off the bottom boundary: 4.13%, which is 114 basis points BELOW the
government bond.** At the judged central figure of ~$760M the yield is **6.2%**, about
**95 basis points over** the bond.

### 2. WHAT THE PRICE ALREADY ASSUMES
- Perpetual growth required to reach the **[E4-28] 10% floor**: **5.87%** at the bottom
  boundary · **4.18%** at the five-year capex end · **1.76%** at the most generous end.
- Growth required merely to match the bond at the bottom boundary: **1.14%**.
- **What the business has actually done.** Consolidated pre-tax income **$1,994.4M (fiscal
  2021) → $1,142.0M (fiscal 2025), −42.7% in four years.** Pro forma combined net income
  **$1,143.0M → $755.5M, −33.9%** on flat revenue. Owner earnings at the capex end
  **$1,683.8M → $276.4M**. Fiscal 2026 guidance, revised 2026-08-25, puts non-GAAP diluted
  EPS at **$11.00–12.00 against $13.20 delivered in fiscal 2025 — down 12.9% at the
  midpoint.** **The realised four-year growth rate on every one of these measures is
  negative.** A 5.87% perpetual growth case must be argued against **[E4-35]**'s base rate
  (*fewer than 10 of the 200 most profitable companies* sustain 15% for twenty years) with a
  four-year record that is negative. **It cannot be made from this evidence.**

### 3. WHAT YOU ARE PAID
**−1.14 points over the sovereign at the bottom boundary; +0.55 points at the five-year
capex end; +2.83 points at the five-year D&A end.** Judged central: **+0.95 points.**

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-01]**, at 89,502,537 shares
| basis | value | per share |
|---|---:|---:|
| bottom boundary, capitalised at the sovereign | ~$9,600M | **~$105** |
| judged central ~$760M at the sovereign | ~$14,400M | **~$160** |
| most generous end at the sovereign | ~$19,200M | **~$215** |
| bottom boundary at the **[E4-28] 10% floor** | ~$5,100M | **~$55** |
| judged central at the 10% floor | ~$7,600M | **~$85** |
| most generous end at the 10% floor | ~$10,100M | **~$115** |

**Zero-growth range against the bond: roughly $105 to $215 a share, centre ~$160.**
**Against the [E4-28] floor: roughly $55 to $115 a share, centre ~$85.**

## ⛔ **PRICE: $136.92** (2026-09-02, aggregator quote, flagged). Market cap **$12,255M**.

The quote sits **inside** the sovereign-referenced range and **above the whole of** the
floor-referenced range. Under **Bar 2 [E4-01]**, price-inside-the-range is *"no useful
conclusion"* — the middle outcome, and the usual one. **No bar is applied and no margin is
struck, because Q1–Q4 did not all return IN and Q5 never opened.** Windage count: **one**
(the capex end of (c)); nothing else has been made conservative twice.

---
# PASS / FAIL

## ❌ **FAIL. The file closed at Q2 — OUT.**
**[E3-03] criterion 2 fails: the customer has a close substitute, and the company said so
itself on 2026-08-25 when it cut price to hold share.** Q1 returned IN. Q3, Q4, Q5 and Q6
were never opened and hold no verdict.

**Price reported under the queue's output contract: $136.92, market cap $12,255M, pro forma
owner earnings $506M–$1,010M, yield 4.13%–8.24% against a 5.27% sovereign, growth required
for the [E4-28] floor 5.87% at the bottom boundary.**

---
## SELF-AUDIT
- [x] Questions answered in order; stopped at the first non-IN verdict; nothing below Q2
      carries a verdict
- [x] No question marked IN carries an "unverified" or "provisional" caveat
- [x] No UNRESEARCHED verdict was issued — the moat class is **NONE**, not PROVISIONAL, and
      the four missing peers are named with their obstacles and shown not to change the row
- [x] Step 0: three primary documents read with accession numbers; **three** figures
      cross-checked against filed statements, not one
- [x] Owner earnings on a multi-year mean, **on a pro forma basis as instructed**; three
      windows shown; capex band disclosed as a judgment with the filed evidence for it
- [x] Competitor row filled — **nine filers**, same metric, same window, all from SEC XBRL
      with accession numbers
- [x] Sovereign is for the earnings currency, from the **issuing authority**, dated
- [x] Value stated as a round-number range, not a point estimate
- [x] **No bar applied** — Q5 did not open. Windage count stated: one
- [x] Price dated; aggregator flagged as a live quote only
- [x] Run committed to git after Q1 and after Q2, per the write-early protocol
- [x] Every brief-commissioned test run and reported, **including the two that came back
      negative** (the deflated physical series on DKS; the ASC 842 check)

## REGISTER
- **Verdict: OUT (about the business), at Q2.**
- **One line:** DICK'S is the best-run survivor of a shrinking format, it has just bought the
  worst-run one for $2.5 billion, and in the most recent quarter it told its owners it cut
  price to keep its customers — which is what a close substitute looks like in a filing.
- **Not UNRESEARCHED and not UNKNOWABLE.** The evidence is here and it is recent.
- **Reopen conditions, pre-committed [E1-02]:** DICK'S Business segment margin held above 12%
  through a promotional cycle without price-matching; Nike below 20% of purchases with
  vertical brands above 25% of sales; Foot Locker at a positive segment profit for four
  consecutive quarters. Observable in the quarterly 8-K.

---
## ADDENDUM TO THE RUN — TEN CONSECUTIVE Q2 OUTs: BIAS, OR COMPOSITION? **[E4-26, E3-41]**

The operator's brief asked this directly and it deserves a direct answer rather than a
reassurance. *"you must not fool yourself, and you're the easiest person to fool"* **[E3-41]**
applies to the analyst who keeps producing the same verdict.

**Three things are true at once, and only the third is about me.**

1. **It is partly a composition fact about the queue.** The tier-1 wave that produced these
   ten is dominated by **consumer-discretionary retailers and resellers**: AEO, KR, DG, NKE,
   ULTA, DKS. Retail is the sector where **[E3-03] criterion 2 is structurally hardest**,
   because the retailer sells other people's products and the customer can buy the identical
   SKU elsewhere. The names on this shelf that *do* clear criterion 2 — Costco, Home Depot,
   TJX — are on the **PRE-RUN, EXCLUDED** list at the top of this very queue. **A queue that
   excludes the winners and then reports a high failure rate is measuring its own
   composition.** That is the honest first answer.
2. **It is partly a fact about the market in 2026.** Six of the ten closed on the same
   mechanism — a franchise that was real in 2019–2021 and has been narrowing since, with the
   narrowing traceable to a specific named cause (Nike's direct channel here; Sephora-at-Kohl's
   at ULTA; Apple/Samsung/Xiaomi building the substitute at QCOM). That is not a screening
   artifact; it is the same wave receding across a sector.
3. **Where the bias would show, and what I did about it.** The failure mode would be reaching
   for the OUT before the disconfirming case was built. So this run **built the disconfirming
   case first, in eight numbered points, before touching criterion 2** — and **three of those
   points survive intact and are recorded as findings against the house view**: the DG
   deflated instrument **does not replicate** on DICK'S; the [E4-55] units series is
   **positive**, not negative; and standalone DICK'S ranks **2nd of nine** on the attacker
   metric, above NIKE. **If the bias were driving the verdict, those three would have been
   softened. They are not.** What defeated the franchise case was not a screen or a ratio —
   it was **one sentence the company itself published on 2026-08-25**, eight days before this
   run, saying it had cut price to hold its customers.

**The verdict I would have written if that sentence did not exist:** NARROW moat, direction
uncertain, **taken to Q3** — because points 1, 2 and 3 of the disconfirming case are real and
the standalone returns are genuinely good. **The sentence exists.** Recorded so the operator
can see exactly how close this ran, and exactly what it turned on.

## TOOL AND BRIEF DEFECTS FOUND — operator rule 6

1. **`tools/sources.py` was still hard-coded to FRED for USD, against CLAUDE.md.** At 12:00
   on 2026-09-02 it returned `USD FAILED: Remote end closed connection without response`
   with **no Treasury fallback at all**, while the comment three lines above the dictionary
   read *"taken from the authority that issues the debt -- never an aggregator."* The
   corrected chain existed only in `daily_fetch.py`. **This run went to
   home.treasury.gov directly and struck 5.27% at 2026-09-01.** *A concurrent session fixed
   `sources.py` during this run; re-tested at the end, it now returns
   `USD 5.27% 09/01/2026 US Treasury daily par yield curve` — which independently confirms
   the rate used above. The defect was live when this run started; recording it rather than
   quietly benefiting from someone else's repair.*
2. **The brief's sign on the acquisition line is the tool's, not the filing's.** The brief
   says `acquisition_flag()` fires "with a NEGATIVE acquisition line of $257M." On the face
   of the filed cash-flow statement the line reads **"Cash acquired from acquisition of Foot
   Locker, net of cash paid  257,095"** — a **positive inflow** in investing activities. Same
   fact, opposite sign convention, and operator rule 4 says the filing is what gets read.
   The substantive claim — that **$2.5bn of consideration appears nowhere in the cash-flow
   statement** — is **confirmed from the statement itself**.
3. **The brief's test 1 cannot be fully run on Foot Locker.** It asks for "sales per square
   foot, sales per store, and transactions" for both companies. **Foot Locker discloses no
   transaction count in any of the nine years** — only comps and sales per square foot. The
   square-foot leg runs (and replicates the DG finding); the transactions leg does not exist.
   Named as a gap rather than filled by estimate.
4. **No defect found in the brief's arithmetic.** The four screen figures (532 / 672 / 918 /
   947), the capex-to-D&A ratios (1.49x / 2.01x / 2.33x on $587M / $803M / $1,137M against
   $394M / $400M / $489M), the share count (89,502,537), the market cap ($12,255M), the
   purchase consideration, the stub contribution, the pro forma table and the comp
   decomposition **all reproduce exactly from the filings.**
