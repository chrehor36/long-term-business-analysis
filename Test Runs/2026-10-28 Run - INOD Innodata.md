# Company Run — Innodata Inc. (Nasdaq: INOD) — 2026-10-28
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run. Departure from the canonical brief, as the brief states it: the repository moved on 2026-10-25 to
`C:\Projects\BRK`. Research folder: `Test Runs/_research 2026-10-28 INOD/` (notes, framework notes, the verbatim ledger rows
cited, the arithmetic script and its output, the tool output).*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-28: the operator does not hold this name (`PORTFOLIO.md` has no Innodata row).*

**Contamination, declared:** a listing of `Screens/` at the start printed file names, among them the blind-listed
`RESUME STATE ...`, `WATCHLIST RUN QUEUE.md` and `2026-08-31 PREPPED READING LIST (operator lists).md`; names only, none
opened. `git status` and `git log -3` printed paths of other analysts' research folders (ARCB 2026-09-27, AQN 2026-10-27)
and commit subjects naming WEC, OGS, SWX, SR and AQN; none about this company. A web search for the short-seller report
returned, among its links, an aggregator page whose entity tag named a person associated with a large technology company;
the filings never name the largest customer, and that tag is not used. After the second commit, `git log -2` printed the
concurrent analyst's commit subject ("CTAS run: template copied ..."). Nothing seen was used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $44.74 (close 2026-10-27; `tools/run.py` live quote, an **aggregator, flagged** per operator rule 5).
- **Shares by class:** one class, common, **34,382,651** at 2026-07-31 (cover of the 10-Q for the quarter to 2026-06-30,
  filed 2026-08-06, accession `0001104659-26-092021`; `python Screens/cover_shares.py INOD` agrees). Check: the same 10-Q's
  balance sheet shows 37,560 thousand issued less 3,184 thousand in treasury = 34,376 thousand at 2026-06-30, consistent.
  **After the 10-Q:** on 2026-08-06 the company filed an automatic shelf (S-3ASR, `0001104659-26-092086`), a prospectus
  supplement (424B5, `0001104659-26-092131`) and an 8-K (`0001104659-26-092133`) for an **at-the-market equity
  distribution agreement of up to $300,000,000** through five agents at up to 2.0% commission. No filing after the 10-Q
  states how many shares, if any, were sold; the third-quarter 10-Q is not yet filed. The count used is the cover count,
  and the unknown ATM sales are a stated gap. An S-8 was filed 2026-10-27 (`0001104659-26-119196`) for plan shares.
- **Market cap:** $1,538.3M (34.383M x $44.74).
- **Sovereign for the earnings currency (USD):** 5.30%, 30-year par yield, 2026-10-27, US Treasury daily par yield curve
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-26, `0001104659-26-020655`); 10-Q Q2 2026
  (`0001104659-26-092021`) and Q1 2026 (`0001104659-26-057270`); proxy DEF 14A filed 2026-04-24 (`0001104659-26-048201`);
  the 10-Ks for FY2016 to FY2024 (`0001144204-17-014715`, `0001144204-18-016374`, `0001144204-19-015946`,
  `0001104659-20-034167`, `0001104659-21-035749`, `0001410578-22-000489`, `0001410578-23-000153`, `0001410578-24-000124`,
  `0001410578-25-000194`); 8-Ks of 2023 to 2026 (credit agreement `0001104659-23-042168`, its amendments
  `0001104659-24-087285` and `0001104659-26-033893`; investigations closed `0001104659-25-060634`; board change
  `0001104659-25-108168`; officer agreements and changes `0001104659-26-025739`, `0001104659-26-075184`,
  `0001104659-26-092010`, `0001104659-26-112351`, `0001104659-26-107790`; bonus award `0001104659-23-129734`).
  **One figure cross-checked against the filed statement:** net cash from operations FY2025 $46,752 thousand (FY2025 10-K
  cash flow statement) against `tools/run.py`'s 46.8: agrees. The FY2024 figure is $35,015 thousand as filed in the FY2024
  10-K and $34,864 thousand as re-presented in the FY2025 10-K (provision for credit losses and receivables lines moved; the
  year-end cash for 2024 also moved from $46,883 to $46,897 thousand); the later presentation is used and the difference,
  $0.15M, is written down.
- `python tools/run.py INOD` arithmetic lines only (output in the research folder): three-year (OCF − SBC − capex) mean
  $14.6M, five-year $6.4M; capex and D&A by year as below. Checked against the statements: capex is the single "Capital
  expenditures" line, which the 10-K says includes capitalized developed software (FY2025 10-K, Liquidity); no
  acquisitions since 2016 ($4.23M in FY2016, Agility); the tool's "lt debt" for 2016 to 2022 is the "Long-term
  obligations" line, which is mostly an accrued pension liability and vendor-financed software licences, not borrowing
  (FY2020 10-K note; 10-Q Q2 2026 note: pension $9.534M, Microsoft licences $1.665M). The revolver has not been drawn.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the first: a share is a business, and the test is whether one would be content to
own it "if the market closed for five years" **[M1997-109]**. A business whose largest customer can leave on 30 to 90 days'
notice and whose revenue doubled in two years on that customer's programs is hard to hold through a closed market on its
figures alone. The quotation gives no information here: "It just tells us prices." **[M2006-077]** (the price, $44.74, is a market value near six times FY2025 revenue) The analyst's habit of looking "for what’s wrong in
things" **[M2025-013]** governed the reading. **Contrary evidence, written down as found** **[M1997-127]**: (1) one
customer was 58% of FY2025 revenue and 63% of receivables at 2025 year-end; (2) a customer that was under 10% of revenue
in FY2023 was 48% in FY2024; (3) a "large social media company" cut $8.5M of FY2023 revenue after a management change
(FY2023 10-K); (4) the 10-K says "There are relatively few barriers preventing companies from entering the markets in
which we operate"; (5) a short-seller report (Feb 2024), a securities class action (filed Feb 2024, dismissed with
prejudice 2026-06-10) and SEC and DOJ subpoenas (closed June 2025 without action); (6) a $300M at-the-market equity
programme registered in August 2026 while the company held $240M of cash; (7) the chief financial officer's chair was
filled on an interim basis from at least December 2023 to July 2026.

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase with no borrowed money and sized so that a total loss cannot touch what
the buyer has and needs, "We are never going to risk what we have and need for what we don’t have and don’t need"
**[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing in this business
changes that line; no purchase is in prospect after Q1 in any case.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**What the business is (FY2025 10-K, `0001104659-26-020655`).** Three reporting segments, unchanged in name since FY2018:
Digital Data Solutions (DDS: "AI training and post-training data, model evaluation, alignment, and safety, AI model
deployment and integration"), Synodex (medical records into structured data for insurers) and Agility (media intelligence
and public-relations software). Before FY2018 the segments were DDS, IADS and MIS (FY2016 10-K); docGenix was moved into
DDS in 2018. No rename, merger or acquisition since the two Agility purchases of 2016 (8-Ks `0001144204-16-113140` and
`0001144204-16-127188`; $4.23M cash paid). 10,107 employees at 2025 year-end; delivery centres in the Philippines, India, Sri Lanka, Israel
and Germany.

**Revenue by segment over the span ($M; segment notes of each 10-K):**

| FY | DDS | Synodex (IADS before 2018) | Agility (MIS before 2018) | Total | Pre-tax income |
|---|---|---|---|---|---|
| 2016 | 50.6 | 4.3 | 8.1 | 63.1 | (4.8) |
| 2017 | 47.8 | 3.7 | 9.4 | 60.9 | (5.1) |
| 2018 | 43.5 | 4.1 | 9.8 | 57.4 | 1.8 |
| 2019 | 41.2 | 3.9 | 10.7 | 55.9 | (1.1) |
| 2020 | 42.0 | 4.8 | 11.4 | 58.2 | 1.0 |
| 2021 | 52.6 | 4.2 | 13.0 | 69.8 | (1.0) |
| 2022 | 56.5 | 7.1 | 15.4 | 79.0 | (10.5) |
| 2023 | 61.6 | 7.5 | 17.7 | 86.8 | 0.1 |
| 2024 | 141.1 | 7.9 | 21.5 | 170.5 | 24.5 |
| 2025 | 220.8 | 7.3 | 23.5 | 251.7 | 41.4 |
| H1 2026 | | | | 182.2 | 34.9 (10-Q) |

**Customer concentration and terms, from the filings.** Two clients 31% (FY2016), 31% (FY2017), 30% (FY2018), 26% (FY2019);
one client 14% (FY2020), 11% (FY2021), 11% (FY2022, a different customer), 10% (FY2023, a different customer again); one
customer **48%** (FY2024) and **58%** (FY2025); in Q2 2026 one customer **37%** and another **34%** (six months: 46% and
26%), with **66% of receivables due from two customers** at 2026-06-30 (10-Q note 13). "Our customer agreements are
generally terminable by our customer upon 30 to 90 days’ notice", and the agreements "generally do not obligate customers
to purchase services in future periods" (FY2025 10-K, Item 1). The company names no customer; it says its base includes
"five of the companies commonly referred to as the “Magnificent Seven,”" and several AI research labs.

**The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years" and "some notion of how the industry will develop and where the company will
stand within the industry" **[M2012-065]**; "a reasonable probability of being able to asses where the business will be in
10 years" **[M2000-037]**. The key variables, "evaluating how predictable they were first" **[M1998-044]**:
1. *How much human-made training and evaluation data the few frontier model builders will buy in 2036.* Not foreseeable:
   the filer itself says the AI industry is "characterized by rapid technological change, evolving industry standards,
   changing customer preferences, new product and service introductions and the emergence of new vendors", and that
   "products, services or technologies developed by others will not render our services, platforms and solutions
   non-competitive or obsolete" cannot be guaranteed (FY2025 10-K, Item 1A).
2. *Innodata's share of that spending, customer by customer.* Not foreseeable: the largest customer changed identity three
   times between FY2021 and FY2024 by the filings' own wording ("Another customer"), the FY2024 largest customer went from
   under 10% to 48% in one year, a second customer went to 34% in one quarter of 2026, and every contract can be ended on
   30 to 90 days' notice.
3. *The price per unit of work against rivals and in-house teams.* Not foreseeable: "relatively few barriers preventing
   companies from entering", "We also compete with in-house personnel at current and prospective customers", and "our large
   customers may exercise pressure for discounts outside of agreed terms" (FY2025 10-K, Item 1A). The 10-K names nine AI-data
   rivals, seven of them private and several founded within the last decade (Item 1, Competition).

**Whether the past statements tell the future ones:** they do not. Ten years of the filings describe two
different businesses: a loss-making data-conversion and content shop on $56M to $79M of revenue (FY2016 to FY2022, pre-tax
income negative in six of seven years), then an AI-data contractor whose revenue tripled in two years on one customer's
programs. Nothing in FY2016 to FY2023 would have let a reader write FY2025 down, and nothing in FY2025 lets one write
FY2035.

**Would the insiders write it down?** "They would say, “That’s too hard.”" **[M2000-105]**. The filer writes no ten-year
forecast; it writes that its infrastructure "is designed to evolve as AI architectures, training techniques, and evaluation
methodologies change" and that "AI adoption will continue to unfold over many years" (Item 1). The industry growth it
quotes is third-party market sizing, and growth in the field is not the company's economics: "Just because Charlie and I can
clearly see dramatic growth ahead for an industry does not mean we can judge what its profit margins and returns on capital
will be as a host of competitors battle for supremacy." **[L2009-005]**. Nor can the winner be named: "there’s industries we
know that may have a wonderful future, but we don’t have the faintest idea who the winners will be" **[M2012-067]**.

**Routing.** The technology here is not a label on a consumer business, the case of "I think Apple is much more of a consumer products business" **[M2017-019]**: the customers are the model
builders themselves, and what they will buy depends on how models are trained, which is the thing changing fastest. "if
something comes in where there’s a technological component that’s of significance, or where we think the future technology
could hurt the business as it presently exists [...] it won’t make it through the filter." **[M1998-008]**; "We view
change as more of a threat into the investment process than an opportunity." **[M1999-063]**. The draft's routing sends a business "whose ten-year economics
cannot be foreseen because its industry changes fast" to TOO HARD here, at Q1. And "if you have doubts about something
being into your circle of competence, it isn’t." **[M2002-092]**.

**The parts.** DDS carried more than all of the five-year pre-tax income (FY2021 to FY2025, after eliminations: DDS
$70.3M, Synodex −$1.4M, Agility −$14.3M; total $54.6M), so DDS decides (Q1's holding-company paragraph read through Q2's
business-of-parts CONVENTION). Agility (a subscription software business, $23.5M revenue, pre-tax loss in FY2025) and
Synodex do not matter to the answer.

**Which cause.** NATURE, not WORK. The deciding question (the 2036 demand for, share of and price of human AI-training
and evaluation work at a few customers) is not in any filing not yet read; the insiders "would not want to put down on
paper their predictions" **[M2000-105]**, and "in other cases the nature of the industry would be the
roadblock. For example, a business that must deal with fast-moving technology is not going to lend itself to reliable
evaluations of its long-term economics." **[L1993-023]**; "Our problem -- which we can't solve by studying up" **[L1999-018]**.
"If something is not very predictable, forget it." **[M1998-044]**; "If something’s important but unknowable, forget it."
**[M2006-076]**.

**VERDICT: TOO HARD (NATURE)**, "a lot of things end up in the “too hard” pile, and it doesn’t bother us" **[M2006-013]**;
not a judgment of quality or price: "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction
of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**. No research pass is opened (NATURE).

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED (facts under AFTER THE STOP).
## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED (facts under AFTER THE STOP).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED (balance sheets read; facts under AFTER THE STOP).
## Q5 — WHO RUNS IT? NOT REACHED (integrity facts recorded under AFTER THE STOP, not judged).
## Q6 — WHAT WILL THEY DO WITH THE MONEY? NOT REACHED (facts under AFTER THE STOP).

## Q7 — WHAT IS IT WORTH? NOT REACHED. COMPUTATION, NOT A CLEARANCE (operator rule 3; the reporting convention of Part VII)
Built by Q7's range convention as written; the file is closed and nothing here is a verdict or entry language.
- **Owner cash after every real cost** (cash from operations − stock pay − capital spending − payments on vendor-financed
  software licences; all-equity basis: net interest income removed after tax at the 21% US statutory rate), $M, from the
  cash flow statements (FY2022 10-K `0001410578-23-000153` for 2021-22; FY2023 10-K `0001410578-24-000124`; FY2025 10-K
  `0001104659-26-020655` for 2024-25): FY2021 −1.66, FY2022 −11.66, FY2023 −4.00, FY2024 22.65, FY2025 22.86.
  **Five-year average $5.64M** (equity-only, after interest: $5.88M). As a share of sales: −2.4%, −14.8%, −4.6%, 13.3%, 9.1%.
  Inputs: OCF 5.151, −1.216, 5.903, 34.864, 46.752; stock pay 1.750, 3.283, 4.027, 3.998, 11.144; capex 4.368, 6.526,
  5.564, 7.741, 11.104; long-term obligation payments 0.691, 0.639, 0.452, 0.362, 0.420; net interest income 0, 0, −0.179,
  0.149, 1.552 (FY2021-22 not separated in the segment tables; cash interest paid $0.03M and $0.02M, taken as nil).
- **Growth.** The series changes sign; by specific (b) the growth is measured between the halves (FY2021-22 average −$6.66M,
  FY2024-25 average +$22.75M), which is meaningless between a negative and a positive figure, so **the range is the
  no-growth case alone, said so**. No cycle base under (a): no window year is called aberrational in the filer's own
  description; the change is structural, which is Q1's finding, not a cycle. No acquisitions in the window (c). Working
  capital is inside the operating cash figure (d). The filing gives no maintenance split (e); the depreciation variant is
  shown beside. The cap (f) does not bite on a no-growth case. Growth spending charged: none in year one or year ten (no
  growth case). Zero nominal growth after year ten; discounted at 5.30%.
- **Net debt at the latest filed date (10-Q, 2026-06-30, `0001104659-26-092021`):** cash $240.278M + held-to-maturity
  Treasuries $10.093M − vendor-financed licences $1.665M = **net cash $248.706M**; no borrowings (revolver undrawn);
  operating leases ($3.8M) left out; accrued pension ($9.534M) left out as not a borrowing, said so. The cash includes a
  **$66.962M customer advance**, with $61.8M of the related project costs incurred but unpaid in accounts payable; the
  filing says "The cash is not required to be segregated" and that management weighs both "when assessing the Company’s
  liquidity requirements". Shown beside, not central. ATM sales after 2026-06-30: unknown, not added.
- **VALUE RANGE (all-equity, central): $10.33 a share**, a single point (the no-growth case, $106.3M for the business at
  5.30% plus $248.7M net cash, over 34.383M shares), against **$44.74**. Beside: the depreciation variant $11.55; the
  central figure with the customer advance taken out of cash $8.38; the literal window is the window used.
- **Floor tested first:** at the price the enterprise value is $1,289.6M; the five-year average owner cash is 0.44% of it,
  FY2025's alone 1.77%. To earn 10% at the price the FY2025 owner cash would have to grow about 24.7% a year for ten years
  (45.6% from the five-year average). No case of the range earns the floor at the price: were Q7 reached, it would close
  OUT whatever the width, "there’s just a point at which we drop out of the game" **[M2003-149]**.
- **FAIR PRICE (reporting figure, Part VII; after the company's own tax, no conversion): $8.87 a share, all-equity
  (central)**; **equity-only $1.71** beside (owner cash after interest at 10% with no cash credited, by the stated
  definition; value on that basis $3.23). No cheap price is reported.

## Q8 — NOT REACHED. ## Q9 — NOT REACHED. ## Q10 — NOT REACHED. ## Q12 — NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**: the ten-year economics of an AI-training-data contractor whose largest customers
can leave on 30 to 90 days' notice cannot be foreseen, by the filer's own description of its industry: "They would say,
“That’s too hard.”" **[M2000-105]**; "a business that must deal with fast-moving technology is not going to lend itself to
reliable evaluations of its long-term economics" **[L1993-023]**. COMPUTATION, NOT A CLEARANCE: value $10.33 a share (single point, no-growth) and fair price $8.87
(all-equity; equity-only $1.71) against $44.74. **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged; operator rule 2; each with its source **[M1997-127]**.)*

**Q2, the castle.**
- The filer: "There are relatively few barriers preventing companies from entering the markets in which we operate. As a
  result, new market entrants also pose a threat to our business. We also compete with in-house personnel" (FY2025 10-K,
  Item 1A). Pricing: "we generally face pricing pressures from our customers [...] our large customers may exercise pressure
  for discounts outside of agreed terms" (same).
- Rivals named (FY2025 10-K, Item 1): Appen (listed in Australia, not an SEC filer), CloudFactory, Surge AI, Invisible
  Technologies, Turing, Mercor, Scale AI (private, not SEC filers), "Define.a" (as printed; not identified), TELUS Digital
  (a foreign issuer, not used); broader: Accenture, Cognizant, EXLService, Genpact, Infosys, PwC, QuantumBlack, Tata
  Consultancy Services. TaskUs and Concentrix are not named in the FY2025 10-K and were not used.
- **The competitor row** (operating income ÷ revenue, the rivals' 10-K XBRL, first-filed values; accessions in
  `Test Runs/_research 2026-10-28 INOD/` companyfacts caches): Genpact 13.3%, 12.0%, 11.6%, 12.2%, 11.8%, 12.7%, 11.5%,
  14.1%, 14.7%, 14.8% (FY2016 to FY2025; FY2025 `0001398659-26-000004`); EXLService 9.4%, 9.5%, 5.6%, 7.7%, 11.5%, 13.9%,
  13.6%, 14.6%, 14.3%, 15.0% (FY2025 `0001297989-26-000008`); Cognizant 17.0%, 16.8%, 17.4%, 14.6%, 12.7%, 15.3%, 15.3%,
  13.9%, 14.7%, 16.1% (FY2025 `0001058290-26-000008`). **Innodata** pre-tax ÷ revenue: −7.6%, −8.3%, 3.2%, −1.9%, 1.8%,
  −1.4%, −13.3%, 0.2%, 14.4%, 16.5%; ten-year sum $46.5M on $953M of revenue, 4.9%. Over the whole span the three rivals held
  12% to 15% in nearly every year; Innodata matched them only in the last two years, on one customer's programs.
- Gross margin as the AI work grew: 40% FY2025, 39% FY2024 (FY2025 10-K MD&A); DDS 39% and 37%; Q2 2026 46% (10-Q).
  FY2023 DDS gross margin 35% (21.5 ÷ 61.6, FY2024 10-K segment note).
- A change for the better is credited only on a full cycle (Q2's CONVENTION); the AI-data business has had no downturn
  in its two years.

**Q3, capital.** Capex $4.4M to $11.1M a year FY2021-25, rising with revenue; FY2025 capex $11.1M against D&A $6.9M;
next-twelve-month capex guided at about $13.1M (10-Q Q2 2026). Receivables rose from $14.3M (2023) to $46.5M (2025): the
growth consumed working capital (receivables increase $18.4M in FY2025 against OCF $46.8M). Net tangible operating assets
are small (property $8.4M, intangibles mostly capitalized software $14.2M at 2026-06-30).

**Q4, the balance sheets, FY2016 to FY2025 first ($ thousands, `tools/run.py` transcription checked against the filed
statements at FY2020, FY2022, FY2025, 2026-06-30).** Equity 33,784 (2016) falling to 18,773 (2022) as losses reduced it,
then 107,145 (2025) and 159,534 (2026-06-30). Retained earnings 12,400 (2016) to −9,683 (2023), then 51,158 (2025): the whole
accumulated profit of the company's history before 2024 was gone by 2022. Goodwill flat at about 2,000 to 2,800; intangibles
grew 8,191 to 13,983 (capitalized software replacing acquired Agility intangibles). Cash 10,869 to 18,902 (2016 to 2022),
then 82,230 (2025) and 240,278 (2026-06-30, inflated by a $67.0M customer advance and $61.8M unpaid project costs).
Receivables tracked sales (12.1% of revenue in 2022, otherwise 15.8% to 18.5% in every year 2016 to 2025; 18.5% in 2025). No borrowing in any year.
What the figures do not say: who the 58% customer is, what its contract runs to, and what part of 2026's cash is the owners'.
Real costs: stock pay rose from $0.7M (2017) to $11.1M (2025, 4.4% of revenue); the company features "Adjusted EBITDA" and
"Adjusted Gross Profit" in its 10-K and 10-Q MD&A (adding back stock pay and depreciation); FY2025 Adjusted EBITDA $57.9M
against pre-tax income $41.4M. Earnings guidance is given: an 8-K of 2026-06-17 (`0001104659-26-075184`) "reaffirming its
full-year 2026 revenue growth guidance". Disclosure controls were found ineffective in the past (FY2025 10-K risk factor
"In the past we have determined that our disclosure controls and procedures were not effective"). Tax: FY2024 had a $5.6M
deferred tax benefit (release); FY2025 effective rate 22%; H1 2026 16.0%.

**Q5, the people (integrity facts recorded, not judged).**
- Short-seller report: Wolfpack Research, 2024-02-15, alleging the AI capabilities were overstated; the stock fell about 30%
  that day (secondary sources only, **aggregators flagged**: blockleviton.com/cases/inod; markets.financialcontent.com
  investor alert of 2024-02-21; tipranks.com item; the report itself not read).
- Securities class action *D’Agostino v. Innodata Inc., et al.* (D.N.J., filed February 2024) alleging false statements
  about AI technology; **dismissed with prejudice 2026-06-10** (10-Q Q2 2026, note 10). Whether an appeal was filed: not
  stated in any filing read.
- SEC and DOJ subpoenas (2024), both closed without action in June 2025 (8-K `0001104659-25-060634`).
- Philippines labour judgment of 2008, about $5.3M plus interest, enjoined in the US since 2018 (10-Q note 10); other
  reasonably possible losses about $0.65M beyond accruals.
- Chief financial officer: an interim CFO (Marissa Espineli) from at least December 2023 (8-K `0001104659-23-129734`) to
  July 2026, when Jayant Chauhan was appointed (8-K `0001104659-26-075184`). Chairman Nick Toor resigned from the board
  2025-11-06 "not the result of any disagreement" (8-K `0001104659-25-108168`).
- CEO succession: Jack Abuhoff (9.4% holder per the proxy) became Executive Chairman 2026-09-30; Rahul
  Singhal became CEO (8-Ks `0001104659-26-092010`, `0001104659-26-112351`).
- Pay (proxy `0001104659-26-048201`): Abuhoff total $12,053,670 in 2025 (salary $544,688, bonus $1,301,137, stock
  $10,199,986) against $6,700,750 in 2024 per the pay-versus-performance table; PRSUs 50% on revenue growth and Adjusted
  EBITDA, 50% relative TSR; severance for the President of 200% of salary plus bonus, 300% on change of control with
  accelerated vesting (8-K `0001104659-26-025739`). No related-party transactions reported (proxy). Directors and officers
  own 11.8% as a group.

**Q6, the money and the owners.** No buybacks since 2016 ($0.13M that year). Shares outstanding about 25.5M (2016) to 34.4M
(2026-07-31), +35%, from option exercises and stock pay; a $300M ATM programme registered 2026-08-06 while cash and
Treasuries stood at $250M; the S-3 of 2024 ($50M) was registered and not, by the filings read, used. No dividends. No
all-stock deal. Q6's buyback test is moot (no buyback); the bottom of the computed range is $10.33.

**Q9, debt and exposures.** No borrowings; $50M secured revolver (Wells Fargo, SOFR + 2.25%, maturity 2029-04-04, fixed
charge cover covenant 1.10x), undrawn. The exposure is the customer: 63% of receivables from one customer at 2025 year-end,
66% from two at 2026-06-30 (10-Q note 13).

## SELF-AUDIT
- [ ] Copied to the dated file before any fetch and committed then (with the framework notes); **not kept in full**: the
      sections were written in one pass once Q1 had closed and the facts after it were gathered, then committed, not
      question by question. Since Q1 closed the file, there was one question to close; the lapse is declared.
- [x] Dispatched: the brief allowed per-question commits; the lock is the dispatcher's. Folding into the register is the
      dispatcher's (operator rule ten); this run binds nothing until folded.
- [x] No other run file, holding review, `PORTFOLIO.md` or blind-listed file was opened or searched; what was seen by
      accident (file names in a `Screens/` listing, other analysts' paths and commit subjects in git output, one aggregator
      entity tag) is declared under contamination above and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`; quoted fragments beside ids are the rows' own (check script in
      the research folder, `scripts/check_ids.py`); every filing fact carries its accession. The rival accessions are given
      for FY2025 only in the text; the earlier years' accessions are in the cached companyfacts files, not written out.
- [x] The order was kept; Q1 closed the file; nothing after it is a clearance; the Q7 arithmetic is headed COMPUTATION,
      NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay, all capex, vendor-financed licences), never a net-income proxy; the
      sovereign from the US Treasury; the price and the short-seller sources flagged as aggregators.
- [x] Contrary evidence was written down as found (foundations); facts for later questions are under AFTER THE STOP, the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor bar applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; its capex, intangibles and "lt debt" lines were checked against
      the statements (the "lt debt" is pension and vendor financing, not borrowing).
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the research notes).
- Honest weaknesses: the ATM sales since 2026-08-06 are unknown; the class-action appeal status is unknown; the
  short-seller report itself was not read; FY2021-22 net interest was taken as nil from cash interest paid; the Q2 2026
  customer advance makes the latest cash figure partly not the owners'.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) Specific (b) sends a sign-changing series to "the no-growth case alone", which for a business that has
just changed its nature turns the five-year window into an average of two different companies: here the range is a
single point built on three loss years of the old business and two profit years of the new one, and the convention has no
rule for a structural (not cyclical) break, since (a) covers only a cyclical or "aberrational" end year "on the filer's own
description". I applied (b) literally and wrote the change down at Q1, where it belongs. (2) The equity-only basis, as
Part VII and Q7 define it ("owner cash after interest against the market value"), credits no cash for a business with
large net cash and no debt, so its figure ($1.71) sits far below the all-equity figure for a reason that has nothing to do
with leverage; the text does not say whether net cash should be added on the equity-only basis, and I did not add it.
(3) The net-debt definition ("borrowings and finance leases less cash and securities, as the filing states them") has no
rule for cash that came in as a customer advance and is owed out to vendors ($67.0M advance, $61.8M unpaid costs at
2026-06-30); I kept the literal figure central and showed the adjusted one beside. A smaller point: the brief names the
"floor's pre-tax" as before the holder's tax, which matches Q7's Whose tax; no conflict was found.
