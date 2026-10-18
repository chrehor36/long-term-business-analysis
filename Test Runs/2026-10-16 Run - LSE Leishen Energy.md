# Company Run — Leishen Energy Holding Co., Ltd. (Nasdaq: LSE) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-16), after the run was committed: **not held** (`PORTFOLIO.md` carries no line for LSE or Leishen).

**Dispatched run.** Written by a dispatched analyst under the dispatcher's brief of 2026-10-16 (its one stated departure
from `Screens/_daily/_dispatch_brief.md`: the lines of evidence are derived by the analyst from the 20-F's Items 4, 3.D and
5; see Step 0). Research folder: `Test Runs/_research 2026-10-16 LSE/` (notes, the arithmetic script `scripts/compute.py`
and its output `compute_out.txt`, the citation check `scripts/check_ids.py`; raw filings in its gitignored `cache/`).

**Contamination, declared.** Seen by accident and not used: the subjects of the five most recent commits in the session's
opening git status (a fold of another company's v5 re-run and its overnight log line); the names of other companies'
research folders in that status listing; and the project memory index loaded with the session, which carries queue counts
and names of other runs but nothing about this company. No other run file, holding review, `PORTFOLIO.md`, register, reading
list or session-state file was opened, listed or searched. A listing of `Test Runs/` filtered for "LSE" or "leishen" was run
before the template was copied, to check that no file of this name existed; it returned nothing.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $4.53 (close 2026-10-15, Yahoo chart feed through `tools/sources.py`; **aggregator, live quote only, flagged**
  per operator rule 5). The IPO price was $4.00 (424B4 of 2024-12-20, accession 0001493152-24-050874).
- **Shares by class:** 17,025,000 ordinary shares in total, being **4,315,000 Class A** (one vote each, the listed class)
  and **12,710,000 Class B** (twenty-five votes each), as of the AGM record date of 2026-01-14 (6-K of 2026-01-29,
  accession 0001493152-26-004168) and on the balance sheet at 2026-03-31 (interim 6-K of 2026-09-14, accession
  0001493152-26-042590, Exhibit 99.1). `python Screens/cover_shares.py LSE` prints 17,025,000 "Class A Ordinary" from the
  20-F cover (accession 0001493152-26-004368); that cover predates the redesignation, and the tool's class label is wrong
  for today: the dual-class structure was adopted on 2025-11-27 and the 6,355,000 shares each of Polar Energy Company
  Limited and WISE-POWER Energy Services Co., Ltd. became Class B (20-F/A, accession 0001493152-26-019563, Note 21). Issued
  equals outstanding; no treasury shares. The F-3 of 2026-06-08 (accession 0001493152-26-027767, a $150,000,000 shelf,
  effective 2026-06-18) has sold nothing as of the interim 6-K. Both classes are counted: 17.025M.
- **Market cap:** $77.1M (17.025M x $4.53). Free float of the listed class is about 4.3M shares, about $19.5M.
- **Sovereign for the earnings currency:** the business earns in RMB (all operating subsidiaries in the PRC; functional
  currency RMB; the filings present in USD by translation). The protocol's table covers USD, JPY and EUR only; the RMB rate
  is taken from the issuing authority, the **PRC Ministry of Finance, "财政部-中国国债收益率曲线" (the MOF China government
  bond yield curve), 30-year: 2.06% on 2026-10-16** (the page is published under 主办单位：中华人民共和国财政部, the PRC
  Ministry of Finance; fetched 2026-10-16, copy in `cache/czb.txt.cache`). The USD 30-year par yield, 5.43% on 2026-10-15
  (US Treasury, `tools/run.py`), is shown beside wherever it matters, because the figures are reported in USD.
- **Filings read** (operator rule 4): the 20-F for FY2025 (filed 2026-01-30, accession 0001493152-26-004368) and its
  20-F/A (filed 2026-04-29, accession 0001493152-26-019563, which adds management's internal-control report and replaces
  Note 20, segments); the 20-F for FY2024 (filed 2025-02-14, accession 0001493152-25-006894); the 424B4 prospectus
  (2024-12-20, accession 0001493152-24-050874); the draft registration statement of 2023-08-24 (DRS, accession
  0001493152-23-030098) for FY2021 and FY2022; the interim 6-K for the six months to 2026-03-31 (filed 2026-09-14,
  accession 0001493152-26-042590, Exhibits 99.1 and 99.2); the F-3 (2026-06-08, accession 0001493152-26-027767); the 6-Ks of
  2025-01-08 (0001493152-25-001422, over-allotment), 2025-09-30 (0001493152-25-016253, the H1 FY2025 interim), 2025-11-20
  (0001493152-25-024447, the EGM proxy), 2025-12-03 (0001493152-25-025863, EGM results), 2026-01-22 (0001493152-26-003202,
  AGM notice and proxy), 2026-01-26 (0001493152-26-003498, Nasdaq annual-meeting deficiency notice), 2026-01-29
  (0001493152-26-004168, AGM results) and 2026-02-17 (0001493152-26-006870, FY2025 results release). There is no proxy
  statement on Schedule 14A; a foreign private issuer files none, and the AGM proxy of 2026-01-22 is the nearest.
- **One figure cross-checked against the filed statement:** net cash used in operating activities FY2025, $(3,522,067),
  on the consolidated statement of cash flows (20-F, page F-6) equals the XBRL value `tools/run.py` prints (-3.5).
  Total revenue FY2025, $48,335,553, also agrees between the statement of operations and the segment note.
- **Years the filings give.** Full fiscal years FY2021 to FY2025 (five income accounts and cash-flow statements: FY2021
  and FY2022 from the DRS, FY2022 to FY2025 from the 424B4 and the two 20-Fs), equity at 2020-09-30, balance sheets at
  every September 30 from 2021 to 2025, and the interim at 2026-03-31. That is six balance-sheet dates, not the eight to
  ten Q4 asks for **[M2025-032]**; no earlier year is filed anywhere, and none is invented.
- `python tools/run.py LSE`, arithmetic lines only (its 3-year window and its v4 material ignored, Part VII): OCF $4.4M,
  $15.1M, $(3.5)M for FY2023 to FY2025; capex $0.7M, $0.7M, $0.2M; D&A $0.4M, $0.5M, $0.5M; stock pay not found in XBRL,
  and none found in the filings (the 20-F and the interim carry no share-based compensation, no option plan and no equity
  incentive plan; a text search for "share-based", "stock-based" and "share based" found none). The tool labels the FY2025
  payment of $0.25M as dividends to minority partners; the filed cash-flow statement calls it "Payment for purchasing
  minority interests", and the statement governs. The full five-year arithmetic is in `compute_out.txt`.

**Owner cash after every real cost, by year** (USD M; operating cash flow as filed, less purchases of property and
equipment, of intangibles and of minority interests; no stock pay exists to deduct):

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | five-year average |
|---|---|---|---|---|---|---|
| Operating cash flow | 12.59 | (4.39) | 4.39 | 15.07 | (3.52) | 4.83 |
| Capital spending (PP&E, intangibles, minority buyout) | 1.01 | 2.85 | 0.98 | 0.72 | 0.46 | 1.20 |
| **Owner cash, all spending** | **11.58** | **(7.24)** | **3.41** | **14.35** | **(3.98)** | **3.62** |
| Owner cash, depreciation in place of capital spending | 12.42 | (4.68) | 3.97 | 14.55 | (4.26) | 4.40 |

The series swings with working capital (receivables built by $15.4M in FY2023 and released by $9.2M in FY2024). For the
six months to 2026-03-31 operating cash flow was $0.73M; for the twelve months to that date it was $(0.81)M.

**Lines of evidence, chosen from the 20-F's Items 4, 3.D and 5, and why.** (1) How the business wins its sales and from
whom (Item 4, Sales and Marketing and Our Customers; Item 3.D, customer concentration): the castle question turns on whether
the customer buys on the bid. (2) What happened to prices and margins when demand fell (Item 5, revenue and gross-profit
discussion by segment): the price behaviour in a downturn is the evidence the castle tests ask for. (3) The market position
the company claims and its source (Item 4, and the Frost & Sullivan section of the 424B4 that Item 4's claims rest on).
(4) The cyclicality and the dependence on oil and gas capital budgets (Item 3.D). (5) The conversion of profit into cash:
receivables, credit-loss provisions, loans made to third parties (Item 5 and the notes). (6) The flows between the company
and its controlling family (Item 7 related-party transactions and the equity notes), which bear on Q5 and Q6. These were
chosen because the first three decide Q2, the fourth and fifth decide whether the figures can be carried into Q7, and the
sixth is what an owner most needs to know about a controlled company.

**THE BALANCE SHEETS, read before the income account** **[M2025-032]** (USD thousands; DRS 0001493152-23-030098 for
2021-2022, 20-F 0001493152-25-006894 for 2023-2024, 20-F 0001493152-26-004368 for 2025, 6-K 0001493152-26-042590 for
2026-03-31):

| Sept 30 (Mar 31 for 2026) | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026-03 |
|---|---|---|---|---|---|---|---|
| Cash (incl. restricted) | n/f | 8,324 | 6,256 | 4,568 | 7,301 | 10,161 | 10,317 |
| Short-term investments | n/f | 7,359 | 2,273 | 7,235 | 17,851 | 18,680 | 16,898 |
| Trade receivables, net (current + non-current) | n/f | 14,360 | 16,647 | 30,743 | 21,826 | 19,634 | 21,351 |
| Advances to suppliers | n/f | 4,763 | 7,967 | 5,638 | 5,897 | 4,532 | 4,110 |
| Inventories | n/f | 1,594 | 3,236 | 7,877 | 5,397 | 3,653 | 2,760 |
| Loans receivable (third and related parties) | n/f | 0 | 0 | 0 | 1,549 | 4,741 | 5,293 |
| Total assets | n/f | 43,874 | 46,488 | 65,457 | 69,634 | 69,333 | 70,259 |
| Bank loans | n/f | 0 | 1,117 | 1,140 | 1,178 | 3,068 | 2,890 |
| Due to related parties | n/f | 7,115 | 6,375 | 13,388 | 9,239 | 5,756 | 5,938 |
| Taxes payable | n/f | 683 | 965 | 2,756 | 3,419 | 3,782 | 4,629 |
| Additional paid-in capital | 11,765 | 11,765 | 11,765 | 1,618 | 1,618 | 6,544 | 6,527 |
| Retained earnings | 8,690 | 13,228 | 18,772 | 29,368 | 37,339 | 38,208 | 35,785 |
| Total equity | 20,259 | 26,030 | 29,644 | 31,759 | 40,456 | 45,458 | 44,576 |
| Revenue in the year (H1 for 2026) | n/f | 31,257 | 46,717 | 73,084 | 69,073 | 48,336 | 20,978 |

n/f: not filed (only the 2020 equity accounts appear, in the DRS statement of changes in equity).

What moved and why. **Equity** grew from $20.3M to $45.5M on retained earnings, but in March 2023 the controlling family
withdrew $10.1M of share capital from the two operating companies, which cut paid-in capital from $11.8M to $1.6M and was
credited to "due to related parties" (20-F FY2024, Note on equity and Note on related parties); that payable is being paid
out ($1.3M to Li Hongqi and $2.9M to Li Hongliang in FY2024; $4.25M still owed to Li Hongqi and $1.50M to Li Hongliang at
2025-09-30, 20-F FY2025 related-party note). The IPO in December 2024 raised $5.4M net, which restored paid-in capital to
$6.5M. **There is no goodwill**, and intangibles are $0.1M. **Receivables** are large against sales: gross trade receivables
were $23.4M at 2025-09-30 against revenue of $48.3M, $4.3M of them reclassified as non-current, "to be collected beyond one
year due to the payment terms negotiated between the Company and its customers" (20-F FY2025, Note 4); the credit-loss
allowance rose from $1.2M to $3.8M over FY2023 to FY2025, and the provision charged to income was $0.8M, $1.5M, $3.0M and
$2.1M (FY2023, FY2024, FY2025, H1 FY2026). **Cash and securities** of $27.2M at 2026-03-31 include common stocks listed in
Hong Kong (a fair-value loss of $1.06M in H1 FY2026, interim MD&A), held in a company whose bank debt is $2.9M. **Loans
receivable** appeared in FY2024 and reached $5.3M: ten loans to six third parties at 3.5% to 8%, among them a customer
named Polar Petroleum Equipment (Shandong) and a credit line of RMB 25M to Beijing Chenghui Shengsi Technology, of which
RMB 21.33M was drawn from October 2024 to June 2025 and RMB 21.19M repaid in September 2025, the last month of the fiscal
year (20-F FY2025, Note 12). **Taxes payable** rose every year, from $0.7M to $4.6M, while income tax paid was $0.06M to
$0.31M a year against provisions of $1.3M to $2.0M in FY2021 and FY2022. **Debt** is small: $2.9M of one-year bank loans.

What the figures do not say and cannot say **[M2025-032]**: whether the receivables from the state-owned oil customers will
be paid on the new longer terms; who the six borrowers are beyond their names, and whether the customer "Polar Petroleum
Equipment" has any tie to "Polar Energy Company Limited", the CEO's holding vehicle (the filing calls the borrower a
customer and a third party, and says nothing more); and what part of "taxes payable" is income tax rather than
value-added tax.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**. For this name it bears directly: the listed class is a $19.5M float of a Cayman holding company whose
operations, cash and auditors' access sit in the PRC, and whose US listing the 20-F's own risk factors say could be ended
under the Holding Foreign Companies Accountable Act (Item 3.D). The market serves and does not instruct **[M2006-077]**:
the price has moved from the $4.00 IPO to $4.53 while revenue fell by 30% in FY2025 and by 25.6% more in H1 FY2026, and
the quotation says nothing either way. No macro forecast enters **[M2000-094]**: the filings blame FY2025 on "the economic
downturn" and "China-US trade tensions" (6-K of 2026-02-17); those are not used as reasons for or against. Margin of safety
is an attitude here, "if you have to actually do it on — with pencil and paper, it’s too close to think about"
**[M1996-084]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) the FY2025 results release compares FY2025
revenue of $48.3M with "USD $63.5 million" for FY2024 (6-K 0001493152-26-006870), which is FY2024's third-party revenue
only; the filed FY2024 total is $69.1M, so the release shows a 24% fall where the 20-F shows 30%; (2) the 20-F's Item 5 and
risk factors carry sentences that describe some other business, "We have derived most of our revenues to date from providing
integrated automation services to petroleum companies" and personnel skills "valuable to all companies engaged in the
integrated automation services industry" (20-F FY2025, Item 5.A and Item 3.D), which is not a description of this company's
four segments; (3) Item 4 says "we are the largest natural gas compressor rental service provider in Southwestern China",
while the Frost & Sullivan section of the prospectus it rests on says the company "ranked second, accounted for 4.3%" and
was first only "among the private oilfield service providers" (424B4, Industry); (4) the original 20-F omitted management's
report on internal control, added by the 20-F/A, which reports two material weaknesses; (5) the company lends its cash to
third parties and buys Hong Kong-listed stocks with it; (6) Nasdaq notified the company on 2026-01-16 that it had not held
an annual meeting within twelve months of its fiscal year-end (6-K 0001493152-26-003498).

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase of this name in cash, unlevered and sized so that a total loss or a
delisting changes nothing the buyer needs, risks nothing the buyer has and needs **[M2012-081]**, **[L2023-005]**; bought
with borrowed money, the thin float and the delisting risk would put the buyer "in a position where you have to sell"
**[M2020-007]**. No ruin to the buyer on the cash terms; the rule is met by how the purchase would be financed and sized.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
like in five or 10 years" and "where the company will stand within the industry" **[M2012-065]**; the product may be opaque
if "I understand the economic dynamics of the industry. Is there — are there competitive moats? Is there ease of entry?"
**[M2011-014]**.

**The business, from the filings.** Four reportable segments (20-F/A Note 20, accession 0001493152-26-019563), whose only
reported profit measure is gross profit: (i) clean-energy equipment, customised wellhead and gathering equipment for oil
and gas fields (reciprocating compressor units, wellhead safety control systems, heating units, skid-mounted systems,
composite pipe), sold to "leading oil and gas enterprises in China" by bidding and framework orders (20-F Item 4); (ii) oil
and gas engineering technical services, the rental, operation and maintenance of gas compressors and spare-parts warehouses
at customer sites; (iii) new energy production and operation, chiefly LNG and CNG trading with one small liquefaction plant
and one CNG station, at gross margins of 1.6% to 9.6%; (iv) digitalization and integration, resold IT hardware and
integration for oilfields. Customers are concentrated: the three largest took 42.6% and 45.3% of revenue in FY2025 and
FY2024 (20-F Item 3.D).

**The key variables and whether they are foreseeable** **[M1998-044]**: (1) the capital and maintenance budgets of the PRC
state oil companies, which the 20-F says follow "the level of activity in the global oil and gas industry" (Item 4,
Seasonality); (2) the price at which those buyers award tenders, which the filings show falling 10% to 40% for standard
products in FY2025; (3) whether the receivables are paid. None of these is a fast-moving technology: the equipment is
mature (compressors, valves, pipe), and the company's own R&D was $0.25M in FY2025 (Item 5). The economic dynamics are
readable from the filings: a small private supplier (1.0% of the PRC natural-gas compressor market, fourteenth, in the
prospectus's industry section) to a few state-owned buyers who set terms. Is it important and knowable **[M2006-076]**? The
deciding question, whether this supplier has any protection from its buyers and rivals, is answered in the filings
themselves (Q2). Would the insiders write the forecast down **[M2000-105]**? Yes: an industry report was commissioned and
printed in the prospectus, forecasting the segments to 2028; projections are not used here, but the industry is not one
its insiders call too hard.

**Abroad: governance and tax** **[M2000-141]**. The structure is direct ownership through Hong Kong holding companies, not
a variable-interest entity: the subsidiary table shows each operating company held 100% (20-F Item 5, overview), and the
20-F describes the parent as "a Cayman Islands holding company with operations mainly conducted by its subsidiaries based
in mainland China" (Item 3); no contractual-control arrangement over an operating company was found;
the tax is the PRC 25% enterprise income tax with the 15% High and New Technology Enterprise rate for the two main
subsidiaries, renewed in October and December 2025 for three years (interim MD&A); the restricted net assets of the PRC
subsidiaries exceed 25% of the consolidated net assets, so cash leaves the PRC only as the PRC allows (20-F/A Note 22).
These can be read; the rows ask a lower price for them, "We wanted to get paid more for going into China, and we did,
because we don’t know the game as well there" **[M2006-021]**, not a pass.

**The parts.** By Q2's business-of-parts threshold the clean-energy equipment segment decides (59.3% of five-year gross
profit; Q2 below). It is understood by the tests above. The services segment (32.4%) is the rental and upkeep of the same
equipment for the same buyers, and is understood on the same variables.

**Do I doubt it is inside?** **[M2002-092]** Not as to the economics: the business is a supplier of ordinary industrial
equipment on tender. The doubts that exist (the receivables, the loans, the family's dealings) are doubts about the figures
and the people, which Q4 and Q5 own, not about whether its ten-year economics can be pictured.

**VERDICT: IN.** The economics of a small tender-bid equipment and service supplier to the PRC state oil companies can be
foreseen from its filings **[M2012-065]**, **[M2011-014]**; no fast-changing technology puts them out of reach
**[M1998-008]**; governance and tax abroad are readable and ask a lower price, not a pass **[M2006-021]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now" **[M1995-038]**.

**The parts table** (business of parts, Q2's CONVENTION; "lumping them together, as is done in standard financial
statements, impedes analysis" **[L2008-005]**). **CONVENTION of this run:** the measure of a part's "operating profit" is
segment gross profit, because the filer reports no segment operating profit: its chief operating decision maker "uses gross
profit as the primary measure of segment profit or loss" and allocates no selling, administrative, credit-loss or research
cost to the segments (20-F/A Note 20, accession 0001493152-26-019563); rationale: it is the only segment profit filed, and
the corporate costs it leaves out (21% of FY2025 revenue) fall on all parts alike. Five years, FY2021 to FY2025 (DRS
0001493152-23-030098; 20-F 0001493152-25-006894; 20-F/A 0001493152-26-019563):

| Part | Five-year gross profit, USD M | Share | By year FY2021-FY2025 | Castle | Decides |
|---|---|---|---|---|---|
| Clean-energy equipment | 38.81 | 59.3% | 5.85, 6.23, 11.87, 10.32, 4.53 | open (below) | **yes, more than half** |
| Oil and gas engineering technical services | 21.20 | 32.4% | 2.82, 4.97, 5.84, 4.50, 3.07 | open (below) | no |
| New energy production and operation (LNG/CNG trading) | 3.32 | 5.1% | 0.20, 1.71, 0.46, 0.65, 0.30 | open: gross margin 1.6% to 9.6%, "fierce competition in the domestic gas trade market" (20-F FY2025 Item 5) | no |
| Digitalization and integration equipment | 2.18 | 3.3% | 0.16, 0.63, 0.21, 0.56, 0.62 | resold hardware; no castle claimed | no |

**The castle tests, on the deciding part (clean-energy equipment), each with its filing fact.**

1. *Would the customer still choose it over the low bid?* The rows' test is whether "it wouldn’t be a question of people
   buying candy for the low bid" **[M2017-009]**. The filing says the opposite of this business: its sales are won "when it
   comes to bidding for projects", where the company "may receive more favorable bidding results" on its record (20-F
   Item 4, Sales and Marketing). The buyers are a few state-owned oil companies; the three largest customers took 42.6% and
   45.3% of revenue (Item 3.D). The failing form in the rows is the customer who does not care from whom he buys: "most
   insureds don't care from whom they buy" **[L2004-003]**.
2. *Pricing power, and the agony before a price rise.* "you can almost measure the strength of a business over time by the
   agony they go through in determining whether a price increase can be sustained" **[M2005-020]**. Here the price moved the
   other way as soon as demand fell: "With the decline of the domestic market demand, cost control of major clients, domestic
   market competition is becoming more intense, which led to a 10% to 40% lower selling price for some of the common
   products" (20-F FY2025 Item 5.A). The segment's gross margin, 30.0%, 33.3%, 30.0% and 30.5% in FY2021 to FY2024, fell to
   20.5% in FY2025; its revenue fell 34.7%. In H1 FY2026 total revenue fell another 25.6% (interim MD&A,
   0001493152-26-042590). The customers also set the payment terms: $4.3M of receivables were moved to non-current because
   of "the payment terms negotiated between the Company and its customers" (20-F FY2025, Note 4).
3. *The price a competitor sets.* "whatever he charged for gas was my price" **[M2012-109]**: the FY2025 price cuts are
   attributed by the company to "domestic market competition"; in the services part the same: revenue fell 37.1% because of
   "the lower service price result from the market competition. Our existing customers adopted a low-cost operating model and
   tightly controlled budgets, which reduce the service price" (20-F FY2025 Item 5.A), and in FY2024 "we had to resort to
   lower margins in order to secure business" (20-F FY2024 Item 5.A, accession 0001493152-25-006894).
4. *Unit volume and share of mind; the low-cost position.* The company's share of the PRC natural-gas compressor market was
   1.0% in 2023, ranked fourteenth; 0.1% of reciprocating compressors; 1.7% of wellhead safety control panels; its one strong
   niche is ultra-high-pressure compressors, 24.2% and second (424B4, Frost & Sullivan section, accession
   0001493152-24-050874; the company paid for the report). No filing shows it to be the low-cost producer, and with 1% of its
   market it cannot be the scale producer; "commodity businesses have risk unless you’re the low-cost producer"
   **[M1997-010]**.
5. *The attacker with money.* "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do
   it?" **[M2011-015]**. The field already has at least thirteen larger compressor sellers (the prospectus ranking puts the
   company fourteenth); the whole company's equity is $44.6M; the barriers the prospectus lists are capital, technology, cost
   control and customer relationships with "CNPC, SINOPEC and CNOOC" (424B4, Entry Barriers), which every incumbent supplier
   also has.
6. *The brand in the customer's mind.* The company holds 6 registered trademarks (20-F Item 4, Intellectual Property); its
   customer awards are "Top Ten Excellent Supplier" and "Top Ten Key Supplier" for one oilfield project in 2020 and 2021
   (Item 4, Our Customers): a supplier's standing with a purchasing department, not a name asked for.
7. *Ask the competitors* **[M1999-130]**. Not done: no competitor is named in the 20-F and no scuttlebutt is on the public
   record; the one SEC-filing rival found is compared below.
8. *Widening or narrowing* **[M1999-108]**. Narrowing on the filings: segment revenue FY2023 $39.6M, FY2024 $33.8M, FY2025
   $22.1M; the company's response is to seek overseas customers (Pakistan, Indonesia, the Middle East) and new segments
   (hydrogen; subsidiaries formed in Saudi Arabia and the United States in 2025 with no operations), which is a search for a
   castle, not the defence of one.
9. *What could destroy it* **[M2000-014]**. The loss of one or two of the three largest customers (Item 3.D) or a further
   cut in their budgets; the filings show both happening in part already (the FY2025 new-energy decline "was mainly due to the
   expiration of sales agreement with a major client", Item 5.A).

The services part, which does not decide, fails the same tests on the same evidence (prices cut by "market competition";
"we had to resort to lower margins in order to secure business"), and its gross profit fell from $5.84M in FY2023 to
$3.07M in FY2025. Its high gross margin (70.9% to 89.5%) is before the corporate costs that the segment measure leaves out.

**The competitor row.** The 20-F names no competitor (Item 4, Competition, names none; the prospectus's ranking tables are
images and their names are not in the filed text). A sweep of EDGAR full-text search for 20-F and 10-K filers from 2024 to
2026 using "oilfield", "CNPC", "Sinopec", "PetroChina", "wellhead" and "natural gas compressor" found one PRC private
oilfield equipment and service supplier that files with the SEC: **Recon Technology, Ltd. (Nasdaq RCON, CIK 0001442620)**.
**CONVENTION of this run:** Recon is the rival compared, chosen because it is the only SEC-filing PRC supplier of oilfield
equipment and services to the same state-owned customers that the sweep found; rationale: the filing names none, and a
foreign rival would not show the PRC buyers' terms. No named rival that does not file with the SEC can be listed, because
the filing names none. Same metrics, from Recon's own 20-Fs (years to June 30; accessions 0001104659-21-139057,
0001410578-22-002904, 0001410578-23-002152, 0001410578-24-001721, 0001104659-25-099502, 0001104659-26-112415):

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| LSE gross margin | 28.9% | 29.0% | 25.1% | 23.2% | 17.6% | 24.9% (H1) |
| LSE operating margin | 20.0% | 17.6% | 16.3% | 10.9% | (3.4)% | (3.3)% (H1) |
| RCON gross margin | 15.1% | 23.2% | 28.1% | 30.3% | 23.0% | 33.2% |
| RCON operating margin | (128.5)% | (98.3)% | (103.3)% | (104.0)% | (86.5)% | (37.5)% |
| RCON operating cash flow, CNY M | (34.1) | (26.2) | (51.7) | (43.7) | (33.8) | (58.8) |

Recon lost money from operations and consumed operating cash in every year shown (and in FY2019 and FY2020 as well, its
20-Fs 0001144204-19-046766 and 0001104659-20-113968). Its losses are in large part its own overheads, so the row is evidence
about the field's terms, not proof that LSE must lose money: two private suppliers to the same buyers show gross margins in
the same 15% to 33% band, and the one with the longer public record has not earned an operating profit in any year of it.

**The field's returns over the last full cycle, judged in words.** LSE's own record is one rise and one fall: operating
income after a 25% tax on average equity of about 20%, 22%, 29% and 16% in FY2021 to FY2024 and a loss in FY2025 and H1
FY2026; owner cash, all spending, averaged 11% of average equity over FY2021 to FY2025 (`compute_out.txt`). The good
years were the pre-listing years, and equity in them stood $10.1M lower after the family's capital withdrawal of March
2023. The rival's record over the same span is a loss in every year. A durable castle protecting "excellent returns on
invested capital" **[L2007-004]** is not what these figures show; what they show is returns that held while the buyers'
budgets grew and fell away when the buyers cut prices.

**Why OUT and not TOO HARD.** The tenuous moat that cannot be valued goes to TOO HARD, "We don’t know how to valuate that"
**[M2000-019]**; this castle is not tenuous but shown open in the filer's own words. The deciding part sells on the bid to
a handful of state-owned buyers **[M2017-009]**, cut its prices 10% to 40% the first year demand fell **[M2005-020]**, says
the cut was set by competition **[M2012-109]**, holds 1% of its market and no low-cost position **[M1997-010]**, and shows
the gain going to the customer, "the improvement you get one day, your competitor gets the next day" **[M2004-053]**.
A lower price does not reopen it: "What you can’t do is turn any investment into a good deal by paying little"
**[M2019-015]**, and "If you really think a business is declining, most of the time you should avoid it." **[M2012-062]**.

**VERDICT: OUT.** The deciding part's castle is open on the evidence of the filings (Q2, What it rules OUT: the customer
who buys on the low bid **[L2004-003]**, **[M2017-009]**; the business whose price a competitor sets **[M2012-109]**); the
services part fails on the same evidence. The file closes here in the "out" box **[M2006-013]**; Q3 to Q12 are NOT
REACHED as clearances.

## Q3 to Q10, Q12: NOT REACHED (the file closed at Q2). The facts already found are below, not weighed.

---
## THE BOX
**OUT at Q2** (the deciding part, clean-energy equipment, sells on the bid to a few PRC state oil buyers and cut its prices
10% to 40% in FY2025 under competition; 1.0% of its market; the one SEC-filing rival loses money every year).
**Integrity facts recorded, not judged.** COMPUTATION, NOT A CLEARANCE: value range $11.86 to $14.08 a share at the RMB
30-year 2.06% (no-growth case alone, on the one cycle filed) against $4.53; fair price $3.81 all-equity ($2.36 equity-only);
on the central cases the expected return at the price is 6.9% to 8.4%, below the floor.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found **[M1997-127]**; no verdict; the box is unchanged (operator rule 2). A later run that reaches Q5 must
answer the integrity facts **[M2013-088]**.*

**Bearing on Q3 (capital).** Capital spending averaged $1.15M a year against depreciation of $0.38M over FY2021 to FY2025;
the business is light in fixed assets ($3.5M of property and equipment) and heavy in working capital: gross trade
receivables were $23.4M against FY2025 revenue of $48.3M, and receivables rose $15.4M in FY2023 alone. Owner cash, all
spending, averaged 11% of average equity over the five years (`compute_out.txt`). The cash the company holds ($27.2M with
short-term investments, 2026-03-31) is used to buy Hong Kong-listed common stocks and to lend to third parties, not in
the business.

**Bearing on Q4 (the accounts).** (1) The founders' share-capital withdrawal of March 2023 ($10.1M, "approximately 9.3
million" in the FY2025 note for the same withdrawal) was credited to "due to related parties", and its repayment runs
through the **operating** section of the cash-flow statement as the change in "Due to related parties": $(2.04)M, $(4.41)M,
$(3.34)M in FY2023 to FY2025 (20-F FY2025, statement of cash flows), including the $4.2M paid to Li Hongqi and Li Hongliang
in FY2024; a return of capital to owners is thereby inside operating cash flow. (2) Taxes payable rose from $0.7M to $4.6M
while income tax paid was $0.06M to $0.31M a year. (3) Receivables of $4.3M were reclassified as non-current, and the
credit-loss provision rose to $3.0M in FY2025 and $2.1M in H1 FY2026. (4) A credit line to a third party (Beijing Chenghui
Shengsi Technology) was drawn RMB 21.33M from October 2024 to June 2025 and repaid RMB 21.19M in September 2025, the last
month of the fiscal year (20-F FY2025 Note 12). (5) Management reports two material weaknesses, "the lack of sufficient
knowledge of U.S. GAAP and pertinent SEC reporting requirements" and "the lack of well-established procedures to ensure
timely review and detection of errors" (20-F/A Item 15); the original 20-F omitted that report and the full segment note.
(6) The tells the rows name: receivables and advance accounts against sales **[M1995-064]**; a visible lapse in the
reporting, where "There is seldom just one cockroach in the kitchen" **[L2002-039]**. No EBITDA or adjusted figure is
featured in the filings read; no earnings guidance in figures was found; the CEO's release says "we believe our efforts will
deliver improved performance in the coming year" (6-K 0001493152-26-006870). No stock pay exists.

**Bearing on Q5 (who runs it; integrity facts recorded, not judged).** (1) The FY2025 results release is headed "Highlighting
Strong Operating Cash Flow and Low Financial Leverage" (6-K 0001493152-26-006870); FY2025 operating cash flow was
$(3,522,067), negative (20-F FY2025, statement of cash flows). (2) The same release states FY2024 revenue as "USD $63.5
million", the third-party revenue only; the filed FY2024 total is $69.1M (20-F FY2025, statement of operations). (3) The
20-F says the company is "the largest natural gas compressor rental service provider in Southwestern China" (Item 4), where
the industry report in the prospectus ranks it second with 4.3%, first only among private providers (424B4). (4) Item 5
and Item 3.D describe "integrated automation services to petroleum companies" and "the integrated automation services
industry", which is not this company's business; the text reads as drawn from another filer's document (the rows' test:
"if it’s clearly the product of some investor relations department or outside consultant or something of the sort, you
know, that tells you something about the individual" **[M2007-083]**; and "a standardized bunch of popular jargon"
**[M1998-038]**). (5) Nasdaq's notice of 2026-01-16 for failing to hold an annual meeting within twelve months of the
fiscal year-end (6-K 0001493152-26-003498); the AGM was then held on 2026-01-29. (6) The 20-F/A lists a compensation
committee "chaired by Mr. Qiusheng" Huang, who resigned on 2025-12-31 (20-F/A Item 6). (7) The founder family: Li Hongqi,
chairman; his brother Li Hongliang, chief executive; his brother Li Hongguang held 10% before the listing; "Li Hongqi
beneficially owns 92 % of the Company in total" before the IPO (20-F FY2024, equity note). A bank loan of RMB 2M was
guaranteed by the chief executive (interim MD&A). (8) The company lent RMB 6M at 3.5% to a customer named "Polar Petroleum
Equipment (Shandong) Co., Ltd", described as a customer and a third party (20-F FY2025 Note 12); the chief executive's
holding vehicle is "Polar Energy Company Limited"; the filings read state no tie between them, and none is asserted here.
(9) Directors' and officers' cash pay for FY2025 was about $133,000 in total (20-F/A Item 6.B); no options or share awards.
The rows that bear: the tells "when the reports are essentially a little dishonest, or biased" **[M1995-111]**; "they don’t
take credit for things that they didn’t do" **[M1998-167]**; "If you’ve got doubts, forget it." **[M2013-088]**.

**Bearing on Q6 (the money and the owners).** (1) In March 2023, before the listing, the family withdrew $10.1M of share
capital from the operating companies (20-F FY2024 equity note); the IPO of December 2024 raised $5.4M net from outside
owners (20-F FY2025 Item 5); $5.76M was still owed to Li Hongqi and Li Hongliang at 2025-09-30. (2) On 2025-11-27, eleven
months after the listing, the shareholders adopted a dual-class structure that gives the family's 12,710,000 Class B
shares twenty-five votes each against one for the 4,315,000 listed Class A shares (6-K 0001493152-25-025863; 20-F/A Note
21), so that the family holds about 98.7% of the votes on 74.7% of the shares. (3) An F-3 shelf for $150,000,000, about
twice the market value, was declared effective on 2026-06-18; nothing sold under it as of the interim 6-K. The rows: "the
lord is going to try to take it all for himself" **[M1995-038]**; the agency cost where "the guy favors himself at the
expense of the shareholders" **[M1995-109]**; the factor "to channel the rewards from the business to the shareholders
rather than to itself" **[L1993-020]**; serial issuance as a candidate STOP **[L2014-015]** (no issuance has occurred
beyond the IPO). (4) No buyback; dividends of $70,142 paid in H1 FY2026 (interim MD&A, recipient not stated). (5) The
minority interests in Sichuan Leishen Hongzhuo and Sichuan Huayou Huitong were bought in September and November 2025.

**Bearing on Q9 (debt and exposures).** Bank loans $2.9M, all due within a year (ICBC, 2.35%); cash and securities $27.2M
(2026-03-31); operating lease obligations $0.8M. The exposures are the receivables from three customers who take over 40%
of revenue, the loans to six third parties ($5.3M), the Hong Kong equity portfolio, the PRC restrictions on moving cash
out (restricted net assets above 25% of consolidated net assets, 20-F/A Note 22) and the delisting risk the 20-F names.
On "little or no debt" **[R1997-001]** the company passes; the cash held in the PRC is "not worth as much as cash held at
home" in the rows' sense **[L2016-009]**.

**Bearing on Q12.** None of the named businesses applies.

## COMPUTATION, NOT A CLEARANCE (Q7's construction, for the owner's two reporting figures)
*The file closed at Q2. Nothing here is a clearance, and no entry language is used (operator rule 3).*

- **Cash input** (Q7's CONVENTION; Q4's recast as far as it was done): the five-year average of owner cash after every
  real cost, FY2021 to FY2025, **A: all spending $3.624M** (operating cash flow less purchases of property, equipment,
  intangibles and minority interests); **B: maintenance only $4.400M** (depreciation in place of capital spending: the
  filing states no maintenance figure, and "the depreciation charge is not inappropriate in most companies to use as a
  proxy for required capital expenditures" **[M1998-127]**; specific (e), with the maintenance guess the owner is owed
  **[M2000-144]**, **[L1999-024]**). All-equity basis: plus after-tax interest of $0.036M, so **A $3.660M, B $4.436M**.
  Working capital is counted, being inside operating cash flow (specific (d)); there are no acquisitions (specific (c));
  the minority buyouts are deducted.
- **Tax** (Q7, Whose tax): the company's own tax as paid inside operating cash flow; the main subsidiaries' 15% rate was
  renewed for three years in late 2025. Cash tax paid ($0.14M a year) ran far below the provision ($0.73M a year), so the
  input is generous; charging the provision instead lowers A to $3.07M (all-equity). Section E's statutory-rate
  recomputation was not made; it would lower the input further, which cannot change the close below.
- **Growth and the window** (specifics (a) and (b)): FY2025 is aberrational on the filer's own description, "a transition
  period" amid "the economic downturn" (6-K 0001493152-26-006870), and the five filed years hold a single cycle (revenue
  $31.3M, $46.7M, $73.1M peak, $69.1M, $48.3M, then H1 FY2026 down 25.6%); the base is that cycle's average, which is the
  window's, and growth between successive cycles cannot be measured with one cycle filed. The owner-cash series also changes
  sign (FY2022, FY2025). **The range is therefore the no-growth case alone, said so,** carried at zero nominal growth. The
  literal window is shown beside: owner cash between the halves rose from $2.17M to $5.19M (33.7% a year), which carried
  ten years traces to an absurdity, "if you trace out the mathematics of it, you bump into absurdities, then you better
  change expectations somewhat" **[M1999-067]**, and is cut by specific (f) to the sales growth between the halves, 14.6%
  a year; see the note under What was unclear on how the cap reads.
- **Net debt** at 2026-03-31 (interim 6-K 0001493152-26-042590): bank loans $2.890M less cash $10.317M (with restricted)
  and short-term investments $16.898M = **net cash $24.32M**; operating leases left out; loans receivable ($5.3M) left out
  as not cash or securities. Market value $77.12M; enterprise value **$52.80M**.
- **The floor, tested first** (Q7, 2026-10-10): expected return at the price on the central cases, no growth, owner cash
  over enterprise value: **A 6.93%, B 8.40%**, both below about ten percent **[M2003-149]**. Beside: with the founders'
  capital-withdrawal payments added back to operating cash flow (FY2024 $4.2M and FY2025 $0.44M; FY2023's part cannot be
  separated), 8.69% and 10.16%; with those added back and the yearly rise in taxes payable taken out, 7.20% and 8.67%;
  the literal-window growth case at 14.6% for ten years returns 16.4% at the price. On the central cases, **no case earns
  the floor: COMPUTATION, Q7 would close OUT**, whatever the width.
- **VALUE RANGE** (no growth, discounted at the RMB 30-year 2.06%, less net debt, per share): **$11.86 to $14.08** against
  $4.53 (at the USD 30-year 5.43%: $5.39 to $6.23). The width is 1.2 to one. The range at the sovereign lies far above the
  price because the RMB rate is 2.06%; the floor, not the range, is what the price fails.
- **FAIR PRICE** (Part VII: each end case valued at ten percent, the two averaged, after the company's own tax):
  **$3.81 a share on the all-equity basis** (central figure: A and B at 10%, $36.6M and $44.4M, averaged $40.5M, plus net
  cash $24.3M, over 17.025M shares); **$2.36 a share equity-only** (owner cash after interest at 10%, averaged, over the
  shares, no cash added). Beside, on the literal window (A no-growth and A at 14.6% averaged at 10%): $5.48 all-equity,
  $4.01 equity-only. The price, $4.53, is above the central fair price on both bases.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit b2f7e2c9); written question by question; committed after Step 0
      and Q1 (ee669005), Q2 (735aef2b), and the close.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's; the run binds
      only when folded into the register (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under Contamination and was not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row
      (`scripts/check_ids.py`, run at the close); every filing fact carries its accession; no E-ids.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance, and the Q7 figures are headed COMPUTATION, NOT
      A CLEARANCE.
- [x] Owner cash after every real cost from the cash-flow statements, never a net-income proxy (operator rule 5); the
      sovereign from the issuing authority (PRC Ministry of Finance for RMB; US Treasury for the USD figure beside); the
      price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations); the facts for later questions are under AFTER THE STOP, with
      the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; its share-class label and its "dividends to minority" label
      were corrected against the filings.
- [x] `python tools/check_framework.py` PASS before the closing commit (recorded in the closing commit message).
- Honest limits: six balance-sheet dates, not eight to ten; segment profit is gross profit only; the FY2023 part of the
  founders' repayments could not be separated; section E's statutory-rate tax recomputation was not made; the competitor
  comparison has one SEC-filing rival; the prospectus's ranking tables are images whose rival names were not read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The earnings currency when the reporting currency differs.** The protocol asks for the sovereign "for the earnings
currency"; this filer earns in RMB and reports in USD, and the brief's wording ("the one the filings report and the
business earns in") assumes the two agree. The run took RMB (where the cash is earned) and showed USD beside; at 2.06%
against 5.43% the range per share more than doubles, so the choice moves the range though not the floor or the fair price.
A one-line rule is wanted. (2) **Specific (a) with one cycle on file.** The text says the base is the last full cycle and
growth is measured "between the averages of successive cycles", but says nothing for a recently listed filer whose filings
hold one cycle; the run read it as (b)'s last clause, the no-growth case alone, and said so. (3) **The cap in (f)** compares
year-ten owner cash with "the highest share of sales the business has earned", without saying at what sales: grown at the
sales growth (here $189M, so the 33.7% growth passes the test by a hair) or at today's sales ($48M, so it fails by far).
The run cut the literal window to sales growth on the second reading and confesses it. (4) **The business-of-parts
threshold** speaks of operating profit, which most small foreign filers do not report by segment; the run used gross
profit as a CONVENTION. (5) **Q2's competitor row** asks for the rivals the filing names; a filing that names none and
prints its ranking tables as images leaves the analyst to choose, and the brief's instruction to confess the choice was
needed and used. (6) **Owner cash and distributions inside operating cash flow.** Q4 and Q7 give no instruction for a
return of capital to the controlling owners that the filer books inside operating activities; the run left it in the
central cases and showed the add-back beside, since adding it back moves one case across the floor. (7) `Screens/cover_shares.py`
reports the whole share count as one class when the cover predates a later redesignation; the tool cannot see a 6-K.
