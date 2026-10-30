# Company Run — Innodata Inc. (INOD) — 2026-09-11
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*Write-early protocol: this file was created before any filing was fetched. Started
2026-09-11, killed twice by session limits (17:10 and 22:10 ET), resumed 2026-09-12 with the
research folder intact. Sections are appended as each closes and committed after each gate.*

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
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.37 %** · date **2026-09-10** · source **US Treasury daily par yield curve, 30-year,
  home.treasury.gov (the issuing authority; not FRED)**, struck via `tools/sources.py` on
  2026-09-11. The brief's 5.37% is confirmed by my own strike, not inherited.
- FX: none on the revenue side. Innodata is a Delaware corporation, Nasdaq-listed, reporting
  in USD; the 10-K says *"most of the Company's revenue is denominated in U.S. dollars"* while
  *"the currencies of the Company's production facilities located in the Philippines, India,
  Sri Lanka, Canada and Israel"* set the cost base. USD is the earnings currency; the peso and
  rupee exposure is a cost-side item carried to Q1 and Q4.

**Shares — Stage 0, BY HAND off the cover of the LATEST periodic filing:**
> *"The number of outstanding shares of the registrant's common stock, $0.01 par value per
> share, as of July 31, 2026 was 34,382,651."*
> — **Q2 2026 10-Q cover**, period 2026-06-30, filed 2026-08-06, accession
> **0001104659-26-092021**, doc `inod-20260630x10q.htm`. `cover_shares.py` returns the same
> figure. No second share class; no preferred; no convertible. Diluted weighted count for Q2
> 2026 was 34,771,000 (1.2M options and 428,263 RSUs in the money).

**Price** (aggregator, flagged per operator rule 5 — live quotes only):
- **$53.65**, close of **2026-09-11**, Yahoo Finance via `tools/sources.py`, struck 2026-09-11.
- **Market capitalisation = 34,382,651 × $53.65 = $1,844.6M.** *(The brief's screen row
  carried `cap_m 1944` on a higher price; the count is the same. Not a share-count miss this
  time — the sixth in the queue does not fire here.)*

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **FY2025 10-K · period 2025-12-31 · filed 2026-02-26 · accession 0001104659-26-020655**
  (`inod-20251231x10k.htm`) — the document of record.
- Also read: **Q2 2026 10-Q** (above); **Q1 2026 10-Q** acc. 0001104659-26-057270; **FY2024
  10-K** acc. 0001410578-25-000194; **FY2023** acc. 0001410578-24-000124; **FY2022** acc.
  0001410578-23-000153; **FY2021** acc. 0001410578-22-000489; **FY2020** acc.
  0001104659-21-035749; **FY2019** acc. 0001104659-20-034167; **FY2018** acc.
  0001144204-19-015946; **FY2016** acc. 0001144204-17-014715; **FY2013** acc.
  0001144204-14-015700; the **8-K EX-99.1 earnings releases** for every quarter from Q4 2023
  to Q2 2026 (nine releases, the latest acc. 0001104659-26-092010 of 2026-08-06); the **8-K
  of 2026-08-06, Item 1.01** (acc. 0001104659-26-092133) with its EX-1.1; the **S-3ASR and
  424B5 of 2026-08-06**; 8-Ks of 2026-06-17, 2026-03-24, 2026-03-10, 2025-11-07,
  2024-08-08; **DEF 14A 2026** acc. 0001104659-26-048201.
- **Figure cross-checked against the filed statement:** XBRL
  `NetCashProvidedByUsedInOperatingActivities` FY2025 = **$46,752K**; the filed CONSOLIDATED
  STATEMENTS OF CASH FLOWS in `inod-20251231x10k.htm` reads *"Net cash provided by operating
  activities 46,752"* — agrees to the dollar. Stock-based compensation **$11,144K** and
  capital expenditures **$(11,104)K** likewise agree with the filed lines.
- **Balance-sheet integrity check [E5-32]:** at 2026-06-30, total assets $356,673K less total
  liabilities $197,139K = **$159,534K** = the stated stockholders' equity, exactly.

---
## THE PERIMETER — THE SAME REGISTRANT, TWO DIFFERENT BUSINESSES

No acquisition sits in the window: goodwill has been $2.0–2.1M since 2016, intangibles are
$14M and almost all of it capitalised software. The perimeter problem here is not a purchase;
it is that **the same 10,000-person company sold a different product to different customers
before 2024.** Filed revenue and the ten-percent customers, every vintage:

| FY | revenue $M | net income $M | customers ≥10% of revenue (filed) | named? |
|---|---|---|---|---|
| 2009 | 76.7 | 7.3 | — | — |
| 2010 | 61.5 | −0.7 | — | — |
| 2011 | 73.9 | 4.5 | — | — |
| 2012 | 86.6 | 7.5 | — | — |
| 2013 | 64.2 | −10.6 | — | — |
| 2014 | 59.1 | −1.0 | — | — |
| 2015 | 58.5 | −2.8 | — | — |
| 2016 | 63.1 | −5.5 | — | — |
| 2017 | 60.9 | −5.1 | two, together **30%** | **Wolters Kluwer, Reed Elsevier** |
| 2018 | 57.4 | −0.3 | WK **19%** ($10.6M) + RE **11%** ($6.4M) = 30% | yes |
| 2019 | 55.9 | −2.2 | **16%** ($8.9M) + **10%** ($5.7M) = 26% | no (last named FY2018) |
| 2020 | 58.2 | +0.6 | one, **14%** | no |
| 2021 | 69.8 | −1.7 | one, **11%** | no |
| 2022 | 79.0 | −11.9 | one, **11%** | no |
| 2023 | 86.8 | −0.9 | one, **10%** | no |
| **2024** | **170.5** | **28.7** | one DDS customer, **48%** | no — *"a Big Tech customer"* |
| **2025** | **251.7** | **32.2** | one DDS customer, **58%** | no |
| H1 2025 | 116.7 | 15.0 | **59%** | no |
| Q1 2026 | 90.1 | 14.9 | **56%** + second customer **17%** | no |
| **Q2 2026** | **92.1** | **14.4** | **37%** + **34%** = **71% in two** | no |
| H1 2026 | 182.2 | 29.3 | 46% + 26% = 72% | no |

*(FY2017–FY2025 10-Ks, Item 1 and the segment note; the quarters from the 10-Qs and the
8-K EX-99.1 of 2026-05-07 and 2026-08-06. Receivables: **63% or $29.2M from one customer**
at 2025-12-31; 61% from two at 2024-12-31.)*

**Fifteen years of a $56–87M publishing-services outsourcer that lost money in nine of them,
then two years of an AI-data vendor whose largest customer is half the company.** The
customer arrived in 2023 (*"In the one year that Innodata has been working with this
customer … approximately $110.5 million of annualized run rate revenue"*, 8-K EX-99.1
2024-08-08) and has never been named in any filing. The second customer, at 34% of Q2 2026,
was *"zero"* twelve months earlier (8-K EX-99.1 2026-05-07).

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Innodata hires people — 10,107
employees at 2025-12-31, plus contractors to *"12,200 professionals across more than 70
countries"* — mostly in the Philippines, India and Sri Lanka, and rents their hours to
companies training AI models. The hours go into writing and grading model outputs, building
training datasets, red-teaming, and evaluation. The customer signs a master services
agreement and then buys work by statement of work or purchase order; the 10-K's own words are
that these *"generally do not obligate customers to purchase services in future periods"* and
are *"terminable by our customer upon 30 to 90 days' notice."* Revenue is therefore heads ×
utilisation × a rate the customer negotiates; direct costs are 55–61% of revenue and are
*"relatively fixed in advance of any particular quarter."* Two small legacy lines ride along:
Synodex (medical-record abstraction for insurers) and Agility (a PR-monitoring subscription
product), together ~$31M of the $252M.

**The scarce input this business controls:** none that is scarce. It controls a trained,
security-cleared (ISO 27001) delivery workforce in low-cost geographies and the project
management to scale it quickly — from 4,325 heads to 10,107 in two years. That is real
operational competence; it is not a scarce input, because the 10-K says the barriers are
low (*"There are relatively few barriers preventing companies from entering the markets in
which we operate"*) and the customers can do it themselves (*"We also compete with in-house
personnel at current and prospective customers who may attempt to duplicate our offerings
using their own personnel"*). The one asset it does own is the off-the-shelf datasets where
*"we retain intellectual property and monetize the same asset across multiple customers"* —
new, and the reason the adjusted gross margin rose from 43% to 49%.

**[E4-55] — does a physical/unit series exist? YES, and this refutes the brief's prior.**
Every 10-K files year-end headcount. Revenue per year-end employee:

| FY | year-end employees (filed) | revenue $M | **revenue per head** |
|---|---|---|---|
| 2018 | ~3,147 (147 + "over 3,000") | 57.4 | ~$18K |
| 2019 | 3,640 | 55.9 | $15.3K |
| 2020 | 3,769 | 58.2 | $15.4K |
| 2021 | 4,931 | 69.8 | $14.1K |
| 2022 | 4,209 | 79.0 | $18.8K |
| 2023 | 4,325 | 86.8 | $20.1K |
| 2024 | 6,648 | 170.5 | $25.6K |
| 2025 | 10,107 | 251.7 | $24.9K |

The series says the 2024–25 step was **mostly volume** — heads 2.3× — with a **one-time ~25%
lift in rate per head in 2024 and none in 2025.** Precision Steel's test [E4-55] runs the
other way here: dollar revenue is not flattered by price; it is carried by hiring. That is the
honest description of the growth and it is carried to Q2 as evidence on who sets the rate.
*(Caveat: year-end heads against full-year revenue understates per-head revenue in a hiring
year; the direction survives the caveat.)*

**Will the fundamentals look broadly the same in ten years?** The company itself has not
looked the same for three: it was a publishing BPO for Wolters Kluwer and Reed Elsevier at
$56M of revenue in 2019, and an AI-training-data vendor at a $365M run-rate in 2026. The
mechanism — sell hours of trained people to whoever needs data made by hand — is simple and
I can describe every dollar of it from the filed statements. What it will be sold *for* in
2036 is the Q2 question, not the Q1 one.

- **VERDICT: [x] IN.** The mechanism is understood from the filings without management's
  language. It is a labour-arbitrage services business with a project-management layer and a
  small dataset-licensing line, and nothing in it requires five months of study [E4-46].

---
## COMPUTATION — NOT A CLEARANCE
*(operator rule 3: this arithmetic is produced before Q2–Q4 have closed. It carries no
entry language and it is not a Q5 output.)*

### THE SCREEN ROW — REPRODUCED, AND THE TWO ENDS ARE TWO WINDOWS AND TWO (c) DEFINITIONS

Screen row: `oe_bottom_m 6 | oe_top_m 17 | spread 1.658`. **Owner earnings by year, from the
filed cash-flow statements (all $M; XBRL cross-checked to the FY2025 filed statement):**

| FY | OCF | SBC | capex | D&A | **OE, capex end** | **OE, D&A end** |
|---|---|---|---|---|---|---|
| 2016 | −2.74 | 1.16 | 2.74 | 3.20 | **−6.6** | −7.1 |
| 2017 | 0.64 | 0.70 | 3.41 | 3.67 | **−3.5** | −3.7 |
| 2018 | 3.57 | 0.80 | 2.03 | 3.37 | **0.7** | −0.6 |
| 2019 | 4.28 | 0.84 | 1.67 | 2.70 | **1.8** | 0.7 |
| 2020 | 5.66 | 0.91 | 1.41 | 2.27 | **3.3** | 2.5 |
| 2021 | 5.15 | 1.75 | 4.37 | 2.87 | **−1.0** | 0.5 |
| 2022 | −1.22 | 3.28 | 6.53 | 3.89 | **−11.0** | −8.4 |
| 2023 | 5.90 | 4.03 | 5.56 | 4.72 | **−3.7** | −2.8 |
| **2024** | **34.86** | **4.00** | **7.74** | **5.80** | **23.1** | **25.1** |
| **2025** | **46.75** | **11.14** | **11.10** | **6.89** | **24.5** | **28.7** |
| H1 2025 | 14.99 | 5.60 | 4.06 | 3.16 | 5.3 | 6.2 |
| H1 2026, as filed | **164.44** | 13.10 | 5.31 | 4.48 | 146.0 | 146.9 |
| H1 2026, ex-prepayment (see below) | ~48.0 | 13.10 | 5.31 | 4.48 | **~29.6** | ~30.4 |

- screen `oe_bottom` **6** = the **5-year FY2021–25 mean at the capex end**: my figure
  **6.4**. Reproduces.
- screen `oe_top` **17** = the **3-year FY2023–25 mean at the D&A end**: my figure **17.0**.
  Reproduces.
- **So the published "spread" is two different windows AND two different (c) definitions
  — the INTC/MRVL shape, for the third time in this queue.** The same-window, same-(c)
  spreads are: 5-yr capex 6.4 vs 5-yr D&A 8.6 (a $2M capex band); 3-yr capex 14.6 vs 3-yr
  D&A 17.0. The width the row was reporting is almost entirely the window.

### THE BEST-YEAR DEPENDENCE — THE HIGHEST OF 361 NAMES, AND HERE IS WHY

| window | capex end $M | D&A end $M | yield on $1,844.6M (capex end) |
|---|---|---|---|
| 10-yr FY2016–25 | **2.8** | 3.5 | 0.15% |
| 5-yr FY2021–25 — corpus default [E2-42] | **6.4** | 8.6 | 0.35% |
| 3-yr FY2023–25 | **14.6** | 17.0 | 0.79% |
| **5-yr with the best two years dropped (FY2021–23)** | **−5.2** | −3.6 | negative |
| 2-yr FY2024–25 | **23.8** | 26.9 | 1.29% |
| FY2025 alone | 24.5 | 28.7 | 1.33% |
| **TTM to 2026-06-30, ex-prepayment** | **~48.8** | ~49.6 | **2.65%** |
| TTM to 2026-06-30, as filed | ~165 | ~166 | (not a real number — below) |

Dropping FY2024–25 takes the five-year mean from **+$6.4M to −$5.2M: the sign flips.** Every
positive multi-year figure in the screen is two years old, and the eight years before them
sum to **−$20M** at the capex end. **The brief's reading is confirmed: this is a company whose
entire owner-earnings record is two years old.**

**THE H1 2026 OCF IS NOT AN EARNINGS FIGURE, AND THE 10-Q SAYS SO.** Filed H1 2026 operating
cash flow is $164.4M on $29.3M of net income, because *"Accounts payable, accrued expenses and
other"* contributed **+$135.8M**. The 10-Q, Liquidity: *"As of June 30, 2026, cash and cash
equivalents were $240.3 million, including amounts received in advance in connection with
ongoing customer programs. At June 30, 2026, $67.0 million remained recorded within advances
from customers, while $61.8 million of related project costs that had been incurred but
remained unpaid was included in accounts payable and accrued expenses."* The EX-99.1 puts
the same thing in one number: *"net of these prepayments, cash was approximately $134
million"* against $250.4M reported — **a ~$116M customer prepayment for "pass-through costs"
sitting in operating cash flow.** Stripping it, H1 2026 OCF is ~$48M and TTM owner earnings
are **~$49M at the capex end**, which is the most generous honest figure in this file. The
prepayment itself is carried to Q4: a customer has pre-funded something larger than a
quarter's revenue, the 10-Q does not say what, and the cash *"is not required to be
segregated."*

### WHICH YEARS DESCRIBE THE BUSINESS THAT EXISTS NOW [E4-41] — DECIDED, AND JUSTIFIED

**The years FY2016–FY2023 describe a different business and are refused for the level; they
are kept for one purpose only — they show what this company earns when the large customer is
absent: roughly nothing, and negative in the years it was investing (FY2016–17, FY2021–23).**
The evidence that the level changed rather than spiked: revenue $86.8M → $170.5M → $251.7M →
a $365M annualised H1 2026; heads 4,325 → 10,107; a second ≥10% customer arriving in 2026;
GAAP gross margin 36% → 39% → 45%; and the 10-K's own perimeter statement that the
ten-percent customers were Wolters Kluwer and Reed Elsevier through 2018 and a *"Big Tech
customer"* from 2024. Any window reaching back past 2023 averages a publishing BPO with an
AI-data vendor — the PINS ruling of 2026-09-07, *"not a range — two companies."*

**The years that describe the business now are FY2024, FY2025 and H1 2026 — a 30-month
record — and [E4-41] then says normalise the mean DOWN for luck.** The favourable exogenous
break is filed in the company's own words: revenue growth was *"primarily due to higher volume
for AI data engineering services from existing customer programs"* — one customer's LLM
training budget. The mean is not stripped of it, because there is no filed basis for the
strip; it is **named**, and every figure below runs on the *unstripped* number so the
conclusion cannot be accused of it.

**THE REBUILT WIDTH, IN DOLLARS AND A WORD: from −$5M (the five years without the two
customer years) to +$49M (trailing twelve months, prepayment removed) — a $54M range on a
business whose best full year is $29M. The word is SIGN: the constructions disagree about
whether Innodata had ever earned anything for its owners before 2024, and the published
$6M–$17M width was a fifth of the real one.** Sixteenth consecutive run in which the
published width was understated.

### THE (c) JUDGMENT — a disclosed judgment, per [E2-23] "must be a guess"

FY2025 capex $11.1M against D&A $6.9M; the capex is *"principally for the purchase of
technology equipment including servers, network infrastructure and workstations, and
expenditures for capitalized developed software"* (MD&A), of which capitalised software
amortisation was $4.0M in 2025. This is a labour business, not a capital one — capex is 4.4%
of revenue — and the gap between capex and D&A is workstations and servers for 3,459 new
heads in one year, i.e. growth, not renewal. **The D&A default [E3-44, E2-41] is the right
class here, and the capex end is carried as the conservative bound.** The band is $2–4M
wide and does not move any verdict; the window does. **Separately-tagged capitalised
software: none in XBRL** (`PaymentsToDevelopSoftware` absent); it lives inside the single
"Capital expenditures" line and the intangibles note (*"Amortization expense relating to
capitalized developed software was approximately $4.0 million"*). It is inside capex and
therefore inside (c) at the capex end.

**Stock compensation subtracted in full [E5-06]: $11.1M in FY2025, 4.4% of revenue and
23.8% of OCF; $13.1M in H1 2026 alone, 7.2% of revenue.** SBC nearly tripled year on year
(4.0 → 11.1) and is on pace to double again. **[E3-70] recorded and not stacked:** the
market-value measure would be higher (the grants were made at $40–70 on a stock that was $7
two years earlier); the reported charge is the floor. Windage is not spent here.

### THE PRICE — the number the queue's output contract requires

- **Price $53.65** (2026-09-11, Yahoo, aggregator, flagged) · **cap $1,844.6M**
- **Owner-earnings yield: 0.15% to 2.65%** across every honest construction — 10-year mean
  to prepayment-stripped TTM. **Sovereign 5.37%.** The most generous figure that exists sits
  **2.7 points below a government bond**; the corpus-default five-year window sits **5.0
  points below**.
- For the yield to reach the bond on the trailing figure, owner earnings would have to be
  **$99M — twice the best twelve months ever filed and 3.4× the best full year.**

*Nothing in this block is a clearance. Q2, Q3 and Q4 follow.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

### THE BULL CASE, BUILT AT FULL STRENGTH FIRST [E4-26, E4-51]

The brief's prior is OUT on criterion (2). Before testing it, the case as its holders would
state it, every leg filed:

1. **The customers are the hardest customers in the world to win, and Innodata has won
   them.** *"Our customer base includes five of the companies commonly referred to as the
   'Magnificent Seven,' as well as several leading artificial intelligence research labs"*
   (FY2025 10-K). The largest went from zero to $110M of run-rate in one year (2024); the
   second from zero to 34% of revenue in twelve months (Q2 2026). Two of the most demanding
   buyers on earth each chose this 10,000-person New Jersey company over Scale AI and their
   own contractor pools.
2. **The growth arrives WITH margin — [E2-63] passes.** GAAP gross margin 36% (FY2023) →
   39.4% → 39.5% → **46% (Q2 2026)**; adjusted gross margin 43% → 49%, *"nine points above
   our publicly stated 40% target, driven by mix: off-the-shelf datasets, where we retain
   intellectual property and monetize the same asset across multiple customers."* Operating
   margin 14.3% → 15.8% → 19% (Q2 2026 pre-tax). A commodity vendor does not expand gross
   margin seven points through a 55% revenue ramp.
3. **The capital half of [E2-44] passes outright:** capex 4.4% of revenue, no debt, no
   acquisitions, and 10,000 heads added on retained earnings and option proceeds.
4. **Diversification is arriving, in the filing's numbers:** the largest customer fell from
   56% of revenue in Q1 2026 to 37% in Q2 while a second scaled to 34%; *"revenue from our
   other Big Tech customers, in the aggregate, grew 453% year-over-year"* (Q1 2026 release).
5. **There is a research bench and a product roadmap** — ICML papers, an evaluation
   platform in beta with a first $1M hyperscaler engagement, a Federal practice, ISO 27001
   in every delivery centre, and a customer pre-funding programmes to the tune of $116M.

That is a genuine case and it is stated before it is tested.

### [E3-03], CRITERION BY CRITERION

**(1) Needed or desired — yes.** Frontier-model training needs hand-made data and human
evaluation, and the budgets are real: the filing's customers spend *"hundreds of millions of
dollars"* on it.

**(3) Not price-regulated — yes.** No regulator sets the rate.

**(2) "Thought by its customers to have no close substitute" — and this is where the file
turns, on the company's own words, four times over:**

- **The substitutes are named by the company, and there are seventeen of them.** *"Major
  competitors … include providers of AI data engineering, training, and evaluation services
  such as Appen, CloudFactory, Surge AI, Invisible Technologies, Turing, Mercor, Define.a,
  TELUS Digital, and Scale AI … We also compete with broader technology and business process
  services providers, including Accenture, Cognizant Technology Solutions, EXLService
  Holdings, Inc., Genpact Limited, Infosys Limited, PwC, QuantumBlack, and Tata Consultancy
  Services."* Then the sentence that decides it: *"Customers may also choose to perform
  certain functions internally or pursue alternative technical approaches, which represents an
  ongoing source of competition."* And in the risk factors: *"There are relatively few
  barriers preventing companies from entering the markets in which we operate … We also
  compete with in-house personnel at current and prospective customers who may attempt to
  duplicate our offerings using their own personnel."*
- **The customer sets the price — [E4-37]'s agony metric, filed.** *"Due to the intense
  competition … we generally face pricing pressures from our customers … Our ability to
  maintain or increase pricing is restricted as customers generally expect to receive volume
  discounts or special pricing incentives as we do more business with them; moreover, our
  large customers may exercise pressure for discounts outside of agreed terms."* A supplier
  whose largest customers press for discounts *outside of agreed terms* is a rate-taker.
  **[E2-44] half (1) fails** — the filing says the opposite of *"raise prices even when
  demand is flat."*
- **The contract is at will.** *"These contractual arrangements are negotiated periodically
  and generally do not obligate customers to purchase services in future periods. Our
  customer agreements are generally terminable by our customer upon 30 to 90 days' notice …
  and may be terminable with shorter notice periods."* And the forward-looking-statements
  block calls the DDS segment's contracts *"primarily at-will."*
- **The unit series (Q1) says the growth was heads, not price.** Revenue per head rose once,
  in 2024, and was flat in 2025 at ~$25K; the volume did the rest. That is what a customer
  buying hours at a rate card looks like from the inside.

**The concentration series is the sharpest single fact and it runs the wrong way for a
franchise:** one unnamed customer 48% → 58% → 59% → 56% → 37%, with a second at 34%; **71% of
Q2 2026 revenue in two accounts that can leave on 90 days' notice.** The brief's prior — *"the
2024–25 revenue step is substantially one hyperscaler customer"* — is confirmed by the filing
(*"a Big Tech customer"*, *"one of its existing 'Magnificent Seven' Big Tech customers"*), and
the counterparty is never named in any vintage.

### [E4-04] — MUST THE MOAT BE CONTINUOUSLY REBUILT? IT WAS REPLACED OUTRIGHT, TWO YEARS AGO

*"Does a lapse in spending destroy the structure, or merely narrow it — and does the spending
defend the same advantage, or buy its replacement?"* Through FY2018 the ten-percent customers
were **Wolters Kluwer and Reed Elsevier** and the product was publishing-content services;
that business earned nothing for fifteen years (nine loss years of seventeen). The AI-data
business is a **different product sold to different customers**, built in 2023–24. The prior
moat, such as it was, was not defended — it was abandoned and replaced. **This is [E4-04]'s
excluded class in its plainest form, and the mechanism is [E3-51]'s surfing run:** the wave is
frontier-lab training budgets; Innodata is a fast, competent surfer; the advantage lives in
the wave. **[E4-36] — which cause of extreme success?** Wave-riding. Not ownable.

**Does success depend on a great manager [E4-23]? The filing says yes, and the manager is
leaving the seat on 2026-09-30.** *"We are, to a considerable degree, reliant on the
continuing leadership of our Chief Executive Officer and would be materially and adversely
affected should he unexpectedly cease to be employed by us."* Jack Abuhoff, founder, long-time
CEO and 9.4% holder (DEF 14A 2026), becomes Executive Chairman; Rahul Singhal (CRO since 2022)
becomes CEO (8-K 2026-08-06). **Recorded here as a moat defect per [E4-23]** — the surgeon
is in the plan by the company's own statement.

**[E3-33] untapped pricing power — not claimable.** [E5-28] says the class is *"a monopoly or
a near monopoly"*; a company that concedes discount pressure outside agreed terms is not one.

**[E3-46] — the second question is a number.** Operating margin 15.8% in the best year;
negative or nil in eleven of the seventeen filed. The two good years are good; *"very high
returns on capital employed over time"* is not the record.

**[E2-49] metric-switching — checked, does not fire.** Segments (DDS, Synodex, Agility) and
the headline metrics have been stable across vintages.

### THE COMPETITOR ROW — required **[E3-28]**

Same metric, latest full fiscal year of each, SEC XBRL companyfacts (TELUS Digital in IFRS
from its 20-F, acc. 0001628280-25-005299):

| Company | operating margin | gross margin | revenue $M | SBC % rev | capex % rev | goodwill+intangibles % assets | period |
|---|---|---|---|---|---|---|---|
| **INOD (subject)** | **15.8%** | **39.5%** | 251.7 | **4.4%** (7.2% H1 2026) | 4.4% | 9.5% | FY2025 |
| Cognizant (CTSH) | 16.1% | — | 21,108 | 0.9% | 1.4% | 41.2% | FY2025 |
| ExlService (EXLS) | 15.0% | 38.4% | 2,087.7 | 3.8% | 2.5% | 26.8% | FY2025 |
| Genpact (G) | 14.8% | 36.0% | 5,079.9 | 1.8% | 1.5% | 30.5%* | FY2025 |
| WNS | 13.3% | 35.4% | 1,314.9 | 2.9% | 4.1% | 34.4% | FY to 2025-03 |
| TaskUs (TASK) | 11.9% | — | 1,183.5 | 2.5% | 5.4% | 35.5% | FY2025 |
| **TELUS Digital (TIXT)** *(direct competitor, named in the 10-K)* | **2.0%** | — | 2,658 | 1.2% | 2.7% | 42.6%* | FY2024, IFRS |
| Concentrix (CNXC) | −9.3% (goodwill impairment year) | 35.0% | 9,825.8 | 1.0% | 2.4% | 34.1%* | FY to 2025-11 |

*\*goodwill only where intangibles are untagged.*

**Peers: 7 of the 17 the 10-K names, plus the brief's Concentrix. The limit, stated
[E3-28]:** Appen is ASX-listed and off the SEC shelf; **Scale AI, Surge AI, Mercor, Turing,
Invisible, CloudFactory, Define.a and Sama are private** — which means **eight of the nine
direct AI-data competitors cannot be put on the row at all.** The row therefore shows
Innodata against the BPO industry it came from, not against the AI-data industry it now
sells into. On that row the moat class would be PROVISIONAL. **The verdict below does not
rest on the row; it rests on Innodata's own filing, which concedes substitutability in
four separate places.**

**What the row shows anyway, including what cuts against my prior [E4-26]:**
1. Innodata's FY2025 margins are **the best on the row** — 15.8% operating and 39.5% gross
   against a BPO band of 12–16% and 35–38%. The refuted prior: I expected rate-card margins
   *below* the BPO peers. They are above, and rising into Q2 2026. The filing's explanation is
   mix (retained-IP datasets) plus operating leverage on fixed costs — both real, neither a
   moat.
2. **The one direct competitor on the row, TELUS Digital, earns 2.0% and lost money in
   FY2024** — the AI-data business is not a high-margin business for the one comparable
   filer, and it is 10× Innodata's size.
3. Innodata pays **2–5× its peers' SBC as a share of revenue**, and the ratio is rising
   (7.2% in H1 2026). The margin advantage is partly paid in shares.
4. **[E2-45]'s attacker test:** the attacker has ample capital and skilled personnel by
   definition — it is the customer. The 10-K says so.
5. **[E3-61]'s limit:** the row shows position, not conduct; it cannot show what the Mag 7
   data teams decide to insource in 2027.

### CLASS AND DIRECTION

- Needed or desired [x] · no close substitute [ ] **FAILS on the company's own filing —
  seventeen named competitors, in-sourcing named as competition, discount pressure "outside
  of agreed terms", at-will contracts, 71% of revenue in two accounts** · not price-regulated [x]
- Must the moat be continuously rebuilt? **It was replaced outright in 2023–24 [E4-04];
  the current one rides a wave [E3-51].** Does success depend on a great manager? **Yes, per
  the 10-K, and he leaves the CEO seat in three weeks [E4-23].**
- Primary moat metric, filing-sourced, and its trend: **share of revenue from the largest
  customer 48% → 58% → 37%, with the top two at 71%; revenue per head flat at ~$25K.** The
  first says the franchise is the customer's, the second says the growth is hiring.
- Class: [ ] WIDE  [ ] NARROW  **[x] NONE**  [ ] PROVISIONAL *(the row alone would be
  PROVISIONAL; the filing decides)*
- **Direction: the margins are widening and the customer base is broadening — both cut in
  the company's favour and are recorded — but neither converts an at-will hours contract
  with a rate-setting customer into a franchise.**
- **VERDICT: [x] OUT.** The prior was OUT held on concentration; the evidence is OUT held
  on **substitutability**, in the filing's own words. [E3-03] criterion (2) is not met. The
  business is well run and its two years are real; it is a good surfer on someone else's
  wave, and *"the advantage lives in the wave, not the surfer"* [E3-51]. This is the business
  failing, not the diligence: every document that would resolve it has been read.

---
⛔ **Q2 is OUT. Q3 and Q4 do not open as gates.** Per the queue's output contract and the
brief, the findings gathered for them are recorded below as **RECORD — NOT A GATE**, so the
file carries what was read; none of it can promote the name or reopen Q2.

---
## RECORD — NOT A GATE. What was read for Q3 and Q4 before Q2 closed the file.

### Q3 — what the filings and the furnished releases show

**Weight case, declared for the record:** daily execution — **ticked**. This is an hours
business on at-will contracts: *"a business, unlike a franchise, can be killed by poor
management"* [E3-43]. Control — no. Leverage — no (no debt; the $50M Wells Fargo revolver is
undrawn *"through the filing date"*). **Gate, not overlay — had Q2 cleared.**

**The flags [E4-22, E4-29, E5-15], each read, dated:**

| flag | 10-K (filed) | 8-K EX-99.1 (furnished) | reading |
|---|---|---|---|
| **EBITDA / adjusted promotion [E4-29]** | Adjusted EBITDA reconciled **by segment** in the MD&A; Adjusted Gross Margin defined and reconciled | **The second bullet of every release**: *"Adjusted EBITDA of $25.4 Million, Beats Consensus by 50%"*; *"Adjusted EBITDA grew 92% - operating leverage by definition."* Adds back SBC of $7.2M in the quarter — 28% of the adjusted figure. **And it is paid on:** the December 2025 PRSUs are weighted *"50% to a financial performance objective, year-over year revenue growth and Adjusted EBITDA"* (DEF 14A 2026). | **Fires at full strength, in the filed document as well as the furnished one.** Not the CGNX shape (clean 10-K, dirty release) — it is in both. |
| **Trumpeted projections [E4-22 third; E5-30]** | — | Guides full-year revenue growth every quarter and **raises it serially**: FY2024 guided ~20% (Feb 2024) → 40%+ (May) → 60%+ (Aug) → 88–92% (Nov); actual **+96%**. FY2025 40%+ → 45%+ → 45%+; actual **+48%**. FY2026 35%+ (Feb) → 40%+ (May) → **an 8-K on 2026-06-17 issued solely to "reaffirm" it** → reiterated (Aug). Q4 2023 revenue *"exceeded our guidance … by 6.5%"*; Q4 2024 *"well above the high end of our Q4 revenue guidance of $52–$55 million."* | **Fires — the [E5-30] ratchet in its raise-and-beat form.** Not the [E4-30] smoothness tell (results are lumpy: +96%, +48%, +55%). [E3-48]'s demand for the record is met: every guide since 2024 was beaten, and every one was raised at least once. |
| **Serial share issuance [E5-15]** | Cover count **25,877,454 (2018-03-09) → 34,382,651 (2026-07-31): +32.9% in ten years**, with **no offering** — all of it options and RSUs (option proceeds $6.7M FY2024, $3.3M FY2025, **$10.9M in H1 2026**; diluted count 3.2M above basic in FY2025). *"We did not have any sales of unregistered equity securities"* (FY2025 10-K). A $50M universal shelf filed 2024-08-08, unused. | **8-K 2026-08-06, Item 1.01: a $300,000,000 equity distribution agreement** with Goldman Sachs, Craig-Hallum, Wells Fargo, Maxim and Wedbush, *"at the market offerings"*, up to 2.0% commission, on an S-3ASR effective the same day. **$300M is 16% of the market cap, armed the same week a new CFO arrived with a mandate for "capital allocation and capital markets … M&A."** No sale is yet filed. | **Fires as a prompt.** The brief's prior — "has sold stock through an ATM" — is **refuted in tense**: through 2026-06-30 no ATM or offering shares were sold; the ten-year dilution is compensation. The ATM is armed, not used. Recorded; read again at the Q3 2026 10-Q. |
| **Weak accounting [E4-22 first]** | **Material weakness in ICFR at 2019-12-31** (FY2019 10-K); remediation through FY2020; **disclosure controls "not effective as of December 31, 2021"** (FY2021 10-K); effective since FY2022, and the 10-K still carries *"In the past we have determined that our disclosure controls and procedures were not effective."* Auditor: BDO India Services Private Limited since 2020-08-24. | — | **Fires as a prompt, dated 2020–2022.** Three of the last seven years with a controls finding; none since. |
| **Filed-figure tells [E4-30]** | Cash taxes paid **$2.4M (FY2024) on $24.5M pre-tax = 9.9%; $6.0M (FY2025) on $41.4M = 14.5%** — rising, not falling. FY2024 net income includes a **$6.0M valuation-allowance release** (Q3 2024). | — | Does not fire. |
| **Litigation as a source to read [E5-16, E5-22]** | *"In February 2024, David D'Agostino filed a putative class action … alleges … that the defendants made false and misleading statements regarding the Company's artificial intelligence ("AI") technology and services."* Motion to dismiss *"fully briefed and pending."* Plus a 2008 Philippine labour judgment of ~$5.6M plus 12%/6% interest, enjoined from US enforcement since 2018. | — | **An allegation, dated 2024-02, unresolved.** Read, not scored. Not a disqualifier. |
| **Except-for [E2-57]** | Q4 2023 release backs out *"the large social media company that went through a highly-publicized take-private in 2022 in conjunction with which it terminated our services"* ($8.5M of 2022 revenue) to restate growth as 23% instead of 10%. | | Fires once, mildly — and it is also the filed precedent for the named death at Q4. |

**[E4-52] — the flags converge:** Adjusted-EBITDA headlines + Adjusted EBITDA in the PRSU
formula + quarterly guidance raises + an 8-K to reaffirm guidance + a $300M ATM + a
capital-markets CFO. That is one system, and it is the one [E4-52] describes.

**The primary test [E2-01]:** ROE on year-end equity — FY2016 −16%, FY2017 −17%, FY2018 −1%,
FY2019 −8%, FY2020 +2%, FY2021 −6%, FY2022 −64%, FY2023 −4%, **FY2024 +45%, FY2025 +30%**
(on average equity, 64% and 38%). Two years of extraordinary returns on a $60–100M equity
base after eight years of destroying it. **[E2-01]'s own carve-out applies: FY2024 carries
a $6.0M tax-allowance release, and FY2025 is stated after $11.1M of SBC that non-GAAP adds
back.**

**Candor [E2-26]:** the 10-K is candid about concentration, at-will terms, pricing pressure,
in-house competition and the controls history — the half-owner would learn every material
negative from Item 1A. The releases are not: they lead on adjusted figures and consensus
beats. **The prepayment is the sharpest candor read:** the balance sheet shows the $67.0M
advance and the 10-Q explains it; the release's headline cash figure of $250.4M is stated
before the *"net of these prepayments … approximately $134 million"* qualifier. Disclosed,
twice — but the gross number leads.

**Capital allocation [E5-08, E2-30]:** no buybacks ever; no dividends ever. (2) *"projects
or acquisitions will materialize to soak up available funds"* — $134M of net cash, a $300M
ATM, and a CFO whose stated brief includes M&A: **the prompt fires before any use of funds
is filed.** Recorded, not scored. **The people, dated:** Abuhoff, founder, 9.4% holder, SCT
total **$12.05M for 2025** (up from $6.70M in 2024 and $0.96M in 2023 — the 2025 figure is
grant-date value of a 200,196-share RSU/PRSU award); cash bonus $1.30M. CEO → Executive
Chairman 2026-09-30; Singhal CEO (employment agreement 2026-03-09, 200% severance / 300% on
change of control with full acceleration); CFO Jayant Chauhan from Mphasis M&A, 2026-07-06,
replacing an interim CFO; Chairman Toor resigned 2025-11-06 and Abuhoff took the chair.
**Integrity: no disqualifier found. Nothing here promotes the name.**

### Q4 — what the filings show about survival

**Owner earnings — see the computation block.** Five-year default **$6.4M**; the honest
range **−$5M to +$49M**; the word is SIGN.

**Great, good, or gruesome [E4-20]?** In form, the 2024–25 business is the *great* account —
$25–29M of owner earnings on $107M of equity with 4% capex — **but the account is 30 months
old and 71% of its deposits come from two depositors who can withdraw on 90 days' notice.**
On the seventeen-year record it is the *gruesome* account: capital consumed for a decade at
no return. The framework's instruction is to say which; **the honest answer is that the
class cannot be assigned from a two-year record, and that is a Q4 finding in itself
[E5-11].**

**Staying power [E5-11] — all three, scored on the worst case [E2-55]:**
- **(1) a large and reliable stream of earnings — FAILS on "reliable."** The filing's own
  words: *"unanticipated variations in the number and timing of our projects … may cause us
  to significantly underutilize our production capacity and employees … and have resulted in
  losses."* Two customers, at will.
- **(2) massive liquid assets — passes, with the prepayment removed.** ~$134M of cash and
  Treasuries net of the customer advance, no debt, a $50M revolver undrawn (borrowing base
  $30.8M; fixed-charge covenant 1.10×). Cash is 7% of the market cap.
- **(3) no significant near-term cash requirements — passes narrowly, and the prepayment is
  the item to watch.** $61.8M of *"project costs that had been incurred but remained unpaid"*
  sit in payables against the $67.0M advance; the cash *"is not required to be segregated."*
  If the programme is cancelled the advance is a liability. The Philippine judgment (~$5.6M
  plus interest since 2008) is enjoined, not extinguished. No debt maturities.
- **Leverage, named and quantified [E4-16, E3-29]:** none financial. The leverage is
  **operational** — direct costs *"relatively fixed in advance"* against revenue that is
  *"primarily at-will."*
- **Jurisdiction [E3-66]:** delivery in the Philippines, India and Sri Lanka; the 10-K names
  *"tax authorities [that] have exercised … significant discretionary and arbitrary powers."*
  The shareholder sits in Delaware; the cost base does not.

**The named way this business dies [E2-27, E3-24, E4-51] — the bear case as its holders
would state it:**
- **The mechanism:** the largest customer — 58% of FY2025 revenue, 37% of Q2 2026 — moves the
  work in-house or to one of the nine named competitors at the next statement of work, on the
  30–90 days' notice the MSA allows, while 10,107 employees' costs stay *"relatively fixed in
  advance of any particular quarter."*
- **Quantified from filed figures:** FY2025 revenue from that customer ≈ 58% × $251.7M =
  **$146M**; at the 39.5% gross margin that is **~$58M of gross profit against $39.9M of
  total operating income.** Lose it over two quarters and the company is at a **GAAP
  operating loss of roughly $18M a year** before it can cut heads — and cutting heads in the
  Philippines carries the labour-court exposure the 2008 judgment shows. **The company has
  filed this exact shape twice:** two clients were **41% of revenue in 2012** (FY2013 10-K),
  fell to 26% in 2013, and revenue dropped **26% with a $10.6M net loss**; and the 2022
  social-media customer terminated on its take-private and took $8.5M with it. **And it is
  already visible in the latest quarter:** the largest customer *"contributed less revenue in
  Q2 than in Q1"* — the share fell from 56% to 37% partly because the dollars fell.
- **Likelihood: a real possibility** — not a low-level one. The 10-K's own risk factor is
  written in the past tense (*"has adversely affected"*, *"have resulted in losses"*), the
  contracts are at will, the customer is a Mag 7 company with its own contractor pool, and the
  filing says customers *"may attempt to duplicate our offerings using their own personnel."*
  **[E4-40] — exposure, not experience:** the twelve consecutive quarters of growth are the
  benign loss history; the exposure is the 71%.

**The ten-year share count, as the brief asked:** **25,877,454 (cover, 2018-03-09) →
34,382,651 (cover, 2026-07-31): +32.9%**, every share of it from options and RSUs, none from
an offering; diluted weighted **25.5M (FY2016) → 35.0M (FY2025), +37%.** The next tranche is
armed: $300M at the market, 16% of the cap, filed 2026-08-06, unsold.

**SBC / OCF, cross-checked to the dollar:** FY2025 **$11,144K / $46,752K = 23.8%**; FY2024
$3,998K / $34,864K = 11.5%; H1 2026 $13,104K / ~$48,000K ex-prepayment ≈ **27%** (8.0% on the
filed, prepayment-inflated OCF). Calibrated row: CRWD 68.0% closed the file · PINS 68.6% ·
**INOD 23.8%, rising** · QLYS 24.9% cleared · CRM 23.4% · SHOP 22.1%.

---
## COMPUTATION — NOT A CLEARANCE: THE VALUE BAND
*(operator rule 3. The queue's output contract requires a price and a band either way. Q2 is
OUT; this carries no entry language and no ranking.)*

**One book. Owner earnings against the bond [E4-01, E3-42] — the bare sovereign, 5.37%, no
per-name premium. Net cash of ~$134M (≈ $3.90 a share) is shown separately, not netted.**

| owner-earnings construction | $M | ÷ 5.37% = zero-growth value | per share (34.38M) | ÷ 10% floor [E4-28] | per share |
|---|---|---|---|---|---|
| 5-yr FY2021–25, capex end (corpus default window) | 6.4 | $119M | **~$3.50** | $64M | ~$1.90 |
| 3-yr FY2023–25, D&A end (the screen's `oe_top`) | 17.0 | $317M | ~$9 | $170M | ~$5 |
| 2-yr FY2024–25, capex end (the years that describe the business now) | 23.8 | $443M | **~$13** | $238M | ~$7 |
| FY2025 alone, D&A end | 28.7 | $535M | ~$16 | $287M | ~$8 |
| **TTM to 2026-06-30, prepayment removed, capex end (the most generous honest figure)** | **48.8** | **$909M** | **~$26** | **$488M** | **~$14** |
| 5-yr with FY2024–25 dropped | −5.2 | — | — | — | — |

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]: roughly $4 to $26 a share at the bare
sovereign with zero growth (add ~$4 of net cash: $8 to $30); roughly $2 to $14 at the ~10%
floor. Current price $53.65. The price is 1.8× to 7× the sovereign range on the most and
least generous constructions, and above the whole of it.**

**What the price already assumes [E4-35, E4-44] — the growth belief faced in writing:** a
buyer at $1,844.6M who receives the prepayment-stripped trailing $48.8M and needs the ~10%
floor [E4-28] over ten years, exiting at the sovereign's 18.6×, needs owner earnings of
~$257M in year ten — **18% compound growth for a decade from the best twelve months ever
filed; 27% a year from the two-year mean; 45% a year from the corpus-default five-year
window.** Against [E4-35]'s base rate — fewer than one in twenty of the best businesses
sustain 15% for twenty years — and against a business whose largest customer's dollars fell
last quarter. **The ceiling [E2-63]:** bounded by two customers' training budgets and by the
rate they set.

**No bar is applied and no margin is stated**, because Q2 is OUT and Bar 1/Bar 2 are Q5
apparatus. **Windage count: zero** — every figure above is the unstripped, most generous
construction of each window, and the conclusion does not need conservatism to hold.

---
## Q5, Q6 — NOT OPENED. Q2 is OUT.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped — Q1 IN, Q2 OUT, file closed; Q3/Q4
      material recorded below the gate and headed as such
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — Q1 rests on
      the FY2025 10-K and the Q2 2026 10-Q
- [x] Every UNRESEARCHED verdict names the artifact — none issued
- [x] Every UNKNOWABLE verdict states what cannot be known — none issued
- [x] Step 0: the filing was read, with accession number; FY2025 OCF, SBC and capex
      cross-checked to the filed cash-flow statement; A − L = equity at 2026-06-30
- [x] Owner earnings on a multi-year mean; windows stated (2/3/5/10-yr, TTM, and the
      five-year with the two customer years dropped); (c) disclosed as a judgment
- [x] Competitor row filled — 7 of 17 named plus CNXC; eight private direct competitors and
      ASX-listed Appen named as unobtainable; the verdict rests on the filing, not the row
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury),
      dated 2026-09-10
- [x] Value stated as a round-number range, headed COMPUTATION — NOT A CLEARANCE
- [x] One bar chosen — none applied, stated why; windage count stated (zero)
- [x] Prices dated; aggregator used for live quotes only and flagged
- [x] Run committed to git, by file name, after each gate
- **Operator rule 6 addendum:** the run was started 2026-09-11 and killed twice by session
  limits (17:10 and 22:10 ET); the header-only file and the research folder survived under
  the write-early protocol and the run was completed 2026-09-12 on the same price and
  sovereign strikes, both dated in Step 0.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- One line: **Innodata rents 10,000 trained people in the Philippines, India and Sri Lanka to
  AI-model builders under at-will contracts terminable on 30–90 days' notice; 71% of its
  latest quarter's revenue is two unnamed Mag 7 customers, its own 10-K names seventeen
  competitors and the customers' in-house teams as substitutes and concedes discount pressure
  "outside of agreed terms", and its entire positive owner-earnings record is two years old
  after fifteen years of a different business that earned nothing. Q2 OUT; price $53.65
  against a computed band of roughly $4–$26.**
- **The reversal condition, in words (the QLYS ruling — no price alert on a business
  failure):** Q2 reopens only on filed evidence that the customers regard Innodata as having
  no close substitute — concretely, (a) a filed multi-year agreement with minimum purchase
  commitments running *toward* Innodata, replacing the at-will MSA; (b) the top-two customer
  share below 40% with revenue still growing and revenue per head rising, not flat; and (c)
  a 10-K Competition section that no longer names the customers' own personnel as a
  competitor. Any one is a document; all three are needed.
- **The strongest fact against this verdict, stated because [E4-51] requires it:** the
  margins are widening through the ramp — GAAP gross margin 36% → 46% and adjusted 43% → 49%
  in ten quarters, on retained-IP datasets *"monetized … across multiple customers"* — and
  the second customer went from zero to 34% of revenue in a year while the largest was
  still growing in absolute dollars. If the datasets and evaluation platform become the
  product and the hours become the delivery mechanism, then what the customers are buying is
  no longer substitutable by their own contractor pools, and Q2 is NARROW rather than NONE.
  **The run's answer:** the same filing still says the contracts are at will and the
  customers set the rate; the datasets are ~nine points of gross margin on a $92M quarter,
  not yet a business; and the strongest counter-evidence is fewer than three quarters old.
  But it is the closest thing in the file to a case for the other side, and it is on record.
