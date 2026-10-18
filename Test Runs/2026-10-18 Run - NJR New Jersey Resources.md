# Company Run: New Jersey Resources Corporation (NYSE: NJR), 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind run
under the canonical brief `Screens/_daily/_dispatch_brief.md`, with its one stated departure (the lines of evidence derived by
the analyst from the 10-K's Items 1, 1A and 7, listed below). Every judgment cites a v5 ledger id in bold; every filing fact
carries its accession; a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.
Copied to this dated name before any fetch (commit `1ae70f37`, "NJR run: template copied before any fetch").

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (34b75b55): `PORTFOLIO.md` read for this one ticker; the operator does not hold NJR (no line names NJR, New Jersey Resources or New Jersey Natural Gas).*

**CONTAMINATION, declared and not used.** (1) The session context at dispatch showed the five latest commit subjects of the
repository, which include a fold of an MDU Resources Group run of 2026-10-18 and its box and figures (a gas utility; "Q2 IN on
the gas franchise at regulator-set ordinary returns", "OUT at Q7, on the floor"). I read the subjects because they were printed
to me; I did not open the MDU file, and nothing in this run is taken from it. Its similarity of subject (a gas distributor) is
the reason I declare it: a previous conclusion on a like business is the anchor the analyst's habits warn of. I built every figure below from NJR's own filings. (2) A directory listing of `Test Runs/` made to check that this
run's file name was free showed three run-file and research-folder names dated 2026-10-18 (HOKCY, MDU, XNGSY); names only, not
opened. (3) The memory index loaded with the session names a queue state and counts of gate-clearers; it does not name NJR and
was not used.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $52.19 (close 2026-10-16; Yahoo Finance chart API through `tools/sources.py`; **aggregator, flagged per operator
  rule 5**, used as a live quote only).
- **Shares by class** from the latest filing's cover: one class, common stock $2.50 par, **101,467,946** shares as of
  2026-07-31 (Form 10-Q for the quarter to 2026-06-30, filed 2026-08-04, accession `0000356309-26-000037`;
  `python Screens/cover_shares.py NJR`). Check against the balance sheet of the same 10-Q: 101,410,957 shares outstanding
  at 2026-06-30, 18,922 in treasury; the cover count is 57k higher a month later, consistent with the continuous issuance
  under the dividend reinvestment and waiver-discount plans (Q6). No 8-K or prospectus after the 10-Q changes the count (the
  8-K of 2026-08-20, accession `0001140361-26-033890`, is a debt placement at NJNG). No preferred stock outstanding.
- **Market cap:** $52.19 x 101.468M = **$5,296M**.
- **Net debt** (all-equity basis, Q7): long-term debt $3,200.1M + current maturities $282.9M + short-term debt $220.0M
  less cash $34.0M = **$3,669.0M** at 2026-06-30 (10-Q, `0000356309-26-000037`). Long-term debt includes the solar asset
  financing obligations of the failed sale-leasebacks ($471.5M at 2025-09-30, FY2025 10-K debt note), which are debt in
  substance and are kept in. Operating leases left out ($171.5M noncurrent plus $5.5M current at 2026-06-30), said so. The
  10-Q states no subsequent event; the 8-K of 2026-08-20 ($150M of NJNG senior notes, $100M closed 2026-08-20, $50M due
  2026-10-22, proceeds "for general corporate purposes, including, but not limited to, refinancing or retiring short-term
  debt and funding capital expenditures") raises gross debt and cash together and is treated as neutral to net debt.
  **Enterprise value at the price: $8,965M.**
- **Sovereign for the earnings currency:** USD, **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-16
  (`tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (period 2025-09-30, filed 2025-11-20, `0000356309-25-000093`): Items 1,
  1A, 3, 5, 7, 8 (statements, Notes 9, 10, 12, 15, 17); 10-Q for the quarter to 2026-06-30 (filed 2026-08-04,
  `0000356309-26-000037`); proxy DEF 14A (filed 2025-12-10, `0000356309-25-000096`); 8-K with the FY2026 third-quarter
  release, exhibit 99.1 (filed 2026-08-03, `0001140361-26-030982`); 8-K of 2026-08-20 (`0001140361-26-033890`); and, for the
  span, the 10-Ks for FY2017 (`0000356309-17-000185`), FY2018 (`0000356309-18-000139`), FY2019 (`0000356309-19-000133`),
  FY2020 (`0000356309-20-000098`), FY2021 (`0000356309-21-000095`), FY2022 (`0000356309-22-000098`) and FY2023
  (`0000356309-23-000083`), statements and segment notes.
- **One figure cross-checked against the filed statement:** cash flows from operating activities FY2025, $466,349K on the
  filed consolidated statement of cash flows (10-K FY2025) against $466.3M in the tagged series `tools/run.py` reads: agree.
  Second check: total assets 2025-09-30, $7,578,775K filed against $7,579M tagged: agree.
- `python tools/run.py NJR`, arithmetic lines only (output kept at `Test Runs/_research 2026-10-18 NJR/run_py_output.txt`).
  Its owner-earnings window stopped at FY2019 because the capital-spending element was not tagged under the names it reads
  after FY2019; its "d3" debt column is `CapitalizationLongtermDebtAndEquity`, which includes the common equity, so its debt
  sums are wrong and are not used. Every owner-cash line below is transcribed from the filed cash-flow statements instead
  (`Test Runs/_research 2026-10-18 NJR/scripts/q7.py`, output in `q7_output.txt`). Stock pay, as filed in the stock-based
  compensation note ("Compensation expense included in operation and maintenance expense"): FY2021 $7.1M, FY2022 $14.8M,
  FY2023 $14.7M, FY2024 $16.0M, FY2025 $17.8M. The cash-flow statement shows no separate add-back line for it, so I cannot
  see whether operating cash already bears it; I deduct it again (errs low by at most that sum, said so).

**The lines of evidence this name needs, derived from the 10-K (the brief's departure), with the item each came from:**
1. The parts and which decides: four segments (Natural Gas Distribution, Clean Energy Ventures, Energy Services, Storage and
   Transportation) plus Home Services and Other; segment earnings over five years (Item 1, Item 7, Note 15).
2. The regulatory compact at NJNG: the base rate case of 2024-11-21 ($157.0M increase, 9.6% return on equity, 54.0% equity
   ratio, 7.08% on rate base), the case filed 2026-06-01 ($157.6M, 10.10% asked), the IIP and SAVEGREEN riders, the CIP
   decoupling (Item 7, Note 4; 10-Q).
3. The policy threat to gas distribution in New Jersey: the Energy Master Plan, the executive orders of February 2023 and the
   proceeding "to plan for the future of natural gas utilities in New Jersey" (Item 1A).
4. Customer count and throughput over the span (Item 1, Item 7).
5. Capital spending against depreciation and operating cash; the external financing that fills the gap (debt, sale-leasebacks,
   share issuance) (Item 7 liquidity; statements of cash flows).
6. Clean Energy Ventures' dependence on investment tax credits and REC markets, and the OBBBA's effect on them (Item 1A;
   10-Q).
7. Energy Services' earnings volatility, the asset management agreements and their prepaid cash (Item 1, Item 7).
8. The non-GAAP figure (NFE, NFEPS), guidance and the pay plan built on it (Item 7; 8-K exhibit 99.1; proxy).
9. Manufactured gas plant remediation ($144.3M to $200.2M, recovered through the RAC) and other contingencies (Item 3).
10. The accounting change of FY2021 (investment tax credits at Clean Energy Ventures moved from flow-through to deferral,
    retrospective) (FY2021 10-K, Note 2).

## THE FOUNDATIONS (not a gate)
The foundation that bears on this name is the first, a share is a business: "Would I be happy buying this stock if the market
closed for five years?” Because then you’re buying a business" **[M1997-109]**. A regulated gas distributor is the kind of
business one can picture owning through a closed market; what the market would not supply in those five years is the outside
money this business takes in every year (Q3, Q6), so the question is less idle here than it looks. The market serves and does
not instruct: "It just tells us prices." **[M2006-077]**, so the stock's rise from $27.02 (2020-09-30) to $52.19 (aggregator
closes) is no evidence either way. No macro view enters; interest rates enter only through the sovereign at Q7. **Contrary
evidence, written down as found** **[M1997-127]**: (i) operating cash has not covered capital spending in any of the ten fiscal
years FY2016 to FY2025 except FY2018, and the dividend has been paid every year partly from new debt, sale-leaseback money and
new shares (Q3, Q6); (ii) the State of New Jersey has an open proceeding on the future of its gas utilities and executive
orders with heat-pump adoption targets (Item 1A); (iii) the company features a non-GAAP per-share earnings figure, gives
guidance on it, and pays its officers on it (Q4, Q5, Q6); (iv) the business pays its owners a dividend it borrows to pay.

## THE STANDING RULE
The buyer's conduct, not the target's: a part-interest bought with the buyer's own money, unlevered, sized so that a fall of
half or more leaves the buyer whole, carries no ruin to the buyer: "We are never going to risk what we have and need for what
we don’t have and don’t need." **[M2012-081]**. Nothing about NJR changes that; its own debt is weighed at Q9.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
like in five or 10 years" **[M2012-065]**. NJR is a holding company of four reported segments, so by Q1's holding-company
paragraph (CONVENTION, by parts) it is understood when each part that decides is understood; a part decides at more than half
of five-year operating profit, or else the largest. The parts, from the filer's own segment measure (net financial earnings,
NFE; Note 15 of the FY2025 and FY2023 10-Ks; the filer reports net income and NFE by segment, not operating income for every
year of the window, so NFE is used and said so):

| Part | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Five-year | Share of the four segments |
|---|---|---|---|---|---|---|---|
| NJNG, regulated gas distribution | 107.4 | 140.1 | 131.4 | 133.4 | 213.5 | 725.8 | 54.8% |
| Energy Services, wholesale gas marketing | 71.1 | 39.1 | 68.5 | 111.5 | 34.9 | 325.1 | 24.5% |
| Clean Energy Ventures, commercial solar | 16.8 | 39.4 | 44.5 | 33.7 | 61.2 | 195.5 | 14.7% |
| Storage and Transportation | 13.0 | 22.5 | 12.8 | 12.2 | 18.5 | 79.1 | 6.0% |

($ millions, NFE as filed: FY2021-FY2023 from the FY2023 10-K `0000356309-23-000083`, FY2024-FY2025 from the FY2025 10-K
`0000356309-25-000093`. On GAAP net income the NJNG share is higher still: FY2021 Storage and Transportation bore a $92.0M
impairment of the PennEast investment, which NFE excludes.)

**NJNG decides** (54.8%, more than half). Its economics are among the most foreseeable a buyer meets: a franchise to deliver gas
to 588,975 customers (2025-09-30) in six New Jersey counties, its margin "decoupled" from weather and usage by the Conservation
Incentive Program, its commodity cost passed through "without markup" under the BGSS clause, its earnings set by a rate base the
regulator values and a return the regulator allows (9.6% on equity, 54.0% equity ratio, 7.08% overall, order of 2024-11-21;
Item 7). The rows ask the analyst to start by "trying to identify the key variables in that particular business, and evaluating how
predictable they were first" **[M1998-044]**. Here they are the rate base (the capital spent and allowed), the allowed return, and the number of customers who
stay on gas. The first two are knowable from the filings and the regulator's orders; the third is the open one, and it belongs
to Q2 as "what could destroy" the castle, not to Q1 as a change too fast to forecast: customer counts rose every year of the
span read (547,626 in FY2019 to 588,975 in FY2025, Item 7 of the FY2021 and FY2025 10-Ks) and throughput to residential and
commercial customers was 63.9 Bcf, 64.7 Bcf and 68.6 Bcf in FY2023 to FY2025 (Item 1, weather 13.4%, 11.3% and 5.5% warmer than
normal). Do the past statements tell me the future ones **[M2008-033]**? For the utility, yes: its income is the allowed return
on a rate base that the cash-flow statement shows being built.

**The parts that do not decide.** Energy Services is a wholesale trading book whose earnings swing with price spreads between
places and times (FY2024 $111.5M, FY2025 $34.9M); its ten-year economics I cannot foresee, and the 10-K itself says changes "in
pricing dynamics and supply could have an adverse impact" (Item 1A). It is 24.5% of five-year NFE and does not decide, so by the
convention it does not keep the whole outside the circle; it is carried to Q7 as the least certain cash in the average and to Q9
as an exposure. Clean Energy Ventures depends on tax credits and state incentives "in order for the projects to be economically
viable" (Item 1A); the OBBBA of 2025 changed the credit framework (10-Q). Storage and Transportation is FERC-regulated storage
and pipeline, small. **"if you have doubts about something being into your circle of competence, it isn’t."** **[M2002-092]**:
I have that doubt about Energy Services, and I record it; the convention reads the whole by the deciding part, and
**[M2023-031]** ("understand as a group, although it didn’t mean we had deep understanding on any") stays open against the
convention, as the framework says.

**VERDICT: IN**, on NJNG, the deciding part **[M1995-051]**, **[M2012-065]**. The doubt about Energy Services is recorded and
carried.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now. What are the key factors? And how permanent are they?" **[M1995-038]**. The file closes on the deciding part, NJNG
(Q1's table; Q2's business-of-parts paragraph, CONVENTION).

**The castle tests, NJNG, each with its filing fact (10-K FY2025, `0000356309-25-000093`, unless stated).**
- *What it is.* A franchise to own the pipes: "Although its franchises are nonexclusive, NJNG is not currently subject to
  competition from other natural gas distribution utilities with regard to the transportation of natural gas in its service
  territory", and bypass by large customers is not a significant exposure "Due to significant distances between NJNG’s current
  large industrial customers and the nearest interstate natural gas pipelines" (Item 1, Competition). The rows name the kind:
  "it has a natural franchise because of surface capabilities" **[M1995-037]**.
- *The attacker with money* **[M2011-015]**. A rival would have to lay a second network of mains under 109 municipalities and win
  a franchise from the same regulator to sell the same molecule at a regulated price; I can see no attacker doing it, and the
  filing reports none. Customers already may buy the gas itself from third-party suppliers (13,121 residential and 7,846
  commercial transport customers at 2025-09-30), and NJNG earns its margin on delivery either way ("is not negatively affected
  by customers who use its transportation service and purchase natural gas from another supplier", Item 7).
- *Pricing power and the agony before a rise* **[M2005-020]**. The price is not NJNG's to set; it is asked of the BPU in a rate
  case and granted in part. The order of 2024-11-21 granted $157.0M at 9.6% on equity; the case filed 2026-06-01 asks $157.6M
  and 10.10% (10-Q, `0000356309-26-000037`). This is the prayer session written into law, and it is why the return is ordinary.
- *Unit volume and share of mind.* Customers 547,626 (FY2019) to 588,975 (FY2025), every year up (Item 7, FY2021 and FY2025
  10-Ks); residential throughput 43.4 Bcf, 44.5 Bcf, 47.8 Bcf in FY2023 to FY2025 in winters 13.4%, 11.3% and 5.5% warmer than
  normal. The new customers of FY2025 are expected to add about $9.4M of annual margin (Item 7).
- *Low-cost position; would the customer choose it over the low bid.* At the fuel level the competitor is oil, electricity and
  propane: "Competition does exist from suppliers of oil, electricity and propane" (Item 1). The filing does not state NJNG's
  delivered cost against electric heat; I record that as not found, not as an answer.
- *Ask the competitors.* No rival is named by the 10-K (below).
- *Widening or narrowing* **[M1999-108]**. In the numbers: widening slowly (customers, throughput, rate base). In the law:
  narrowing pressure. Item 1A: New Jersey's EMP defines 100% clean energy by 2050 as including "maximum electrification of the
  transportation and building sectors"; "In February 2023, the Governor of New Jersey issued two executive orders that
  established, or accelerated, previously established 2050 targets for clean-sourced electricity and electric heat pump
  adoption, with target dates of 2030 or 2035, as applicable. An additional executive order opened a proceeding to plan for the
  future of natural gas utilities in New Jersey." Against it, the filer: "While the EMP does not place a moratorium or end date
  on natural gas hook ups, further legislation or rulemaking that de-emphasizes the role of natural gas [...] could put upward
  pressure on natural gas prices and place customer growth targets at risk." No outcome of the proceeding is reported in the
  10-K or in the 10-Q to 2026-06-30.
- *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**. The regulator and the legislature, not a
  competitor. The rows carry both the bet and its failure: "the bet we are making is that regulatory authorities will treat us
  fairly in the future" **[M2014-087]**; "there’s no question that railroads, utilities, insurance companies, are all very much
  affected by the political process" **[M2012-074]**; and the confessed mistake, "In such jurisdictions, it is difficult to
  project both earnings and asset values [...] I did not anticipate or even consider the adverse developments in regulatory
  returns" **[L2023-011]**. The row on stranded utility assets says which way a commission tends to lean when the stranding
  comes from policy and not from folly: "If they’re stranded because of rank foolishness, you know, they will probably be less
  inclined — or the utility commissions — will be less inclined to let you figure that in your rate base as you go forward as
  opposed to things that are — where societal demands are just changing." **[M2017-094]** (said of generation assets; I apply
  it by analogy to gas mains, a reading of mine, not the speakers').

**The competitor row.** The 10-K names no competitor by name: for NJNG, "suppliers of oil, electricity and propane"; for Energy
Services, "wholesale marketing and trading companies, utilities, natural gas producers and financial institutions"; for Clean
Energy Ventures, "a large number of firms competing in all facets of the market". So the comparators are a **CONVENTION of this
run**: three SEC-filing gas distribution holding companies, Atmos Energy (CIK 731802), ONE Gas (CIK 1587732) and Northwest
Natural Holding (CIK 1733998); rationale: the field's returns are the test Q2 asks for, and these are listed, nearly pure gas
distributors with filings over the whole span. Metric: net income on average common equity, from the companies' own 10-K XBRL
facts (first-filed vintage; script `Test Runs/_research 2026-10-18 NJR/scripts/peer_metrics.py`), FY2021 to FY2025, and capital
spending against depreciation.

| Company | ROE FY2021-FY2025, each year | Five-year average | Capital spending / depreciation, FY2021-25 | Operating cash less capital spending, FY2021-25 |
|---|---|---|---|---|
| Atmos Energy (10-Ks `0000731802-21-000040` to `0000731802-25-000056`) | 9.1, 8.9, 8.7, 9.1, 9.3 | 9.0% | 4.5x | -$6,582M |
| ONE Gas (10-Ks `0001587732-22-000019` to `0001587732-26-000009`) | 9.0, 9.0, 8.6, 7.6, 8.1 | 8.5% | not computed (depreciation not tagged under the names read) | -$1,260M |
| Northwest Natural Holding (10-Ks `0001733998-22-000005` to `0001733998-26-000012`) | 8.6, 8.2, 7.6, 5.9, 7.9 | 7.7% | 2.8x | -$764M |
| NJR consolidated (filed statements) | 7.2, 15.9, 13.9, 13.8, 14.6 | 13.1% | 4.1x | -$954M |
| NJNG alone (estimate, below) | n/a, 8.4, 7.2, 6.7, 9.9 | about 8% | utility plant spending $1,750M against NJNG depreciation $529M (3.3x) | not reported |

*NJNG alone* is my estimate, labelled as such: NJNG segment net income (Note 15) against 54.0% (the allowed equity ratio) of
net utility plant at year end (balance sheet); a CONVENTION of this run, rationale: NJNG's own equity is not reported in the
NJR 10-K. (Atmos's and ONE Gas's operating cash in FY2021 was negative from the February 2021 winter storm's gas costs and
recovered later; the five-year sums carry both legs.) Over the longer span the field is the same: Atmos 9.9% average FY2017 to
FY2025, Northwest Natural 7.9% FY2018 to FY2025. **The field's returns over the last full cycle:** the durable players earn 8%
to 9% on equity, about what their regulators allow, and every one of them spends several times its depreciation and more than
its operating cash. NJR's consolidated 13.1% comes from the parts that are not the utility (Energy Services' trading margin and
Clean Energy Ventures' tax credits), not from a better castle at NJNG.

**The parts table** (section B):

| Part | Share of five-year NFE | Castle | Decides |
|---|---|---|---|
| NJNG | 54.8% | standing natural franchise; regulator-set ordinary return; political threat named | yes |
| Energy Services | 24.5% | none that I can see: a trader of spreads among "wholesale marketing and trading companies, utilities, natural gas producers and financial institutions"; earnings follow the spreads | no; carried to Q7 at no growth |
| Clean Energy Ventures | 14.7% | none of its own: return "based substantially on our eligibility for ITCs and the future market value of RECs" (Item 1A) | no; carried to Q7 at no growth |
| Storage and Transportation | 6.0% | FERC-regulated cost-of-service pipeline (Adelphia) and storage (Leaf River, half of Steckman Ridge) | no |

**Judgment.** The castle stands: no attacker with money can build a second gas network, and the evidence of the span (customers,
throughput, a full rate case granted in 2024) shows it standing. It protects ordinary returns only, about what the field earns,
which by Q2's list closes OUT, except that a return set by a regulator is the exception the list names, carried to Q3 as a
second best. The rows behind the exception: "there’s no way we get rich on our utility investments. But there’s no way we get
poor, either." **[M2009-104]**; "the industry offers owners the opportunity to deploy large sums at fair returns"
**[L2005-005]**; and the speakers' own word for the trade, "in utilities the trade has been the compact has been that you get a
modest return." **[M2024-011]**. Can its future ten to twenty years out be judged **[M2000-014]**? This is the closest call of the
run, and I write it down as such **[M1997-127]**. Against: the State has set targets for heat pumps and opened a proceeding on
the future of its gas utilities, and **[L2023-011]** is the speakers' own warning that a regulator's climate can make "earnings
and asset values" hard to project. For: no moratorium or end date on hook-ups is in force, customers rose every year through
FY2025, the regulator granted a full return in November 2024, and the row on stranded assets says policy-driven stranding is the
kind a commission tends to let into the rate base **[M2017-094]**. I judge the castle standing for the ten-year horizon on the
evidence of the filings, with the political threat named and carried; a reader who weighs the proceeding more heavily would send
the file to TOO HARD (NATURE) here, and I record that reading in the framework section below. Nothing later in this run depends
on which of the two readings is taken: Q7 closes the file on its own evidence.

**VERDICT: IN**, on NJNG's standing franchise, with its regulator-set ordinary return carried to Q3 as a second best
**[M2009-104]**, **[L2005-005]**; the political threat to gas distribution in New Jersey written down and carried
**[L2023-011]**, **[M2012-074]**.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
"does it look like it has good economics? Has it earned high returns on capital?" **[M1995-051]**, measured on "the capital
actually needed in the business" **[M2010-090]**.

**Return on the capital employed** (earnings after depreciation against capital employed; filed statements, FY2021 to FY2025).
Earnings: income before income taxes, plus interest expense, plus equity in earnings of affiliates, with the $92.0M PennEast
impairment of FY2021 added back and the $58.2M gain on the residential solar sale of FY2025 taken out. Capital employed: common
equity plus long-term debt, current maturities and short-term debt, less cash, at year end (FY2020 as restated in the FY2021
10-K).

| FY | Pre-tax, pre-interest earnings ($M) | Capital employed, year end ($M) | Return on average capital, pre-tax |
|---|---|---|---|
| 2020 | | 3,939.0 | |
| 2021 | 321.8 | 4,238.5 | 7.9% |
| 2022 | 436.9 | 4,800.6 | 9.7% |
| 2023 | 437.0 | 5,126.0 | 8.8% |
| 2024 | 505.0 | 5,559.7 | 9.5% |
| 2025 | 503.0 | 5,995.3 | 8.7% |

Average 8.9% pre-tax, about 6.7% after a 25% tax (the federal 21% plus the filer's state line; Q7). The figure flatters the
cash: "Other income, net" includes the allowance for equity funds used during construction ($10.0M in FY2025, $6.9M in FY2024),
a regulatory credit with no cash in it, and the "equivalent value of ITCs recognized on equipment financing" ($17.0M in FY2025),
which the cash-flow statement takes back out. **Incremental:** from FY2021 to FY2025 capital employed rose $1,757M and the
pre-tax earnings $181M, about 10% pre-tax and 7.7% after tax on the added money, near the 7.08% overall return the BPU allows on
NJNG's rate base (order of 2024-11-21). The added capital earns what a regulator allows, not more: "a fair return on the assets
employed" **[M2008-024]**.

**Reinvestment to stand still and to grow.** Every year of the ten read, capital spending ran far above depreciation: FY2021 to
FY2025, total capital spending (utility plant, solar equipment, storage and transportation, cost of removal) $3,041M against
depreciation and amortization $749M, 4.1 times; at NJNG alone, utility plant $1,750M against NJNG depreciation $529M, 3.3 times
(Q2's table). Operating cash ($2,087M over FY2021 to FY2025) did not cover the spending in any of those years; the gap and the
dividend ($741M) were met with $645M of new long-term debt and term loans net of repayments, $70M more short-term debt,
$572M of solar and meter sale-leaseback money and $197M of new shares (DRP and waiver-discount issuance) (cash-flow statements, FY2023 and
FY2025 10-Ks). The rows name exactly this condition: "you have to keep putting more and more money into a public utility. And
you’d better hope that the rate of return allowed is commensurate" **[M2005-052]**; "BNSF must annually spend more than its
depreciation charge to simply maintain its present level of business" **[L2023-009]**. Whether NJNG's spending is maintenance
or growth the filing does not split in a form I could read (the capital-expenditure table in Item 7 is an image); the
depreciation charge is the proxy the rows allow **[M1998-127]**, and Q7 uses it.

**The growth arithmetic and its cap.** The growth is real and it is bought: earnings rise because rate base rises, and rate base
rises because money is put in. The speakers' description of their own utility fits: "we’re not earning a higher rate of return on
capital than we were when we started. We just put way more capital into the business as we went along" **[M2023-081]**. The
difference is who supplies the money: Berkshire's utility retained all of it ("We have never had a penny of dividends"
**[M2019-059]**), while NJR pays out about half its earnings and raises the rest outside. The rows' grades: the best business
needs "very little" capital; the second-best "takes more money, but the rate at which you invest — reinvest — the money to get
that growth is a very satisfactory rate" **[M1998-081]**; the capital-heavy utility is "the second-best choice, still a good
choice" **[M2018-055]** on the condition of "decent returns on the incremental sums they invest" **[L2009-012]**. About 7% after
tax on the added money, against a 5.43% long bond, is a decent return for a regulated business and a poor one for an owner who
must also supply the capital; the parts outside the utility (Clean Energy Ventures' solar, $684M of spending over the window)
earn what tax credits and REC prices allow, and the 10-K calls those credits and prices the risk.

**WEIGHS AGAINST**: a capital-heavy business whose added capital earns a regulator's fair return and no more, whose operating
cash has not covered its spending in nine of ten years, and which can grow only with outside money **[M2005-052]**,
**[L2023-009]**, **[M1998-081]**; graded at best the second-best business of **[M2018-055]**, **[L2009-012]**. (The "little or no
debt" criterion is applied at Q9.)

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them, before the income account** **[M2025-032]**. Filed consolidated balance sheets at
September 30 ($ millions): FY2016 and FY2017 from the FY2017 10-K (`0000356309-17-000185`), FY2018 from the FY2018 10-K
(`0000356309-18-000139`), FY2019 from the FY2019 10-K (`0000356309-19-000133`), FY2020 as first filed (`0000356309-20-000098`)
with the restated figures beside, FY2021 (`0000356309-21-000095`), FY2022 and FY2023 (`0000356309-23-000083`), FY2024 and FY2025
(`0000356309-25-000093`).

| Sept 30 | Total assets | PP&E, net | Common equity | Debt (long-term + current + short-term) | Cash | Billed receivables | Regulatory assets (current + noncurrent) | Shares out (M) | Retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 3,718.6 | 2,407.7 | 1,166.6 | 1,238.2 | 37.5 | 142.7 | 495.6 | 86.09 | 825.6 |
| 2017 | 3,928.5 | 2,609.7 | 1,236.6 | 1,428.5 | 2.2 | 196.5 | 426.7 | 86.56 | 868.0 |
| 2018 | 4,143.7 | 2,651.0 | 1,419.0 | 1,456.1 | 1.5 | 205.5 | 386.9 | 88.29 | 1,007.1 |
| 2019 | 4,373.0 | 3,041.2 | 1,551.7 | 1,584.1 | 2.7 | 139.3 | 529.5 | 90.00 | 1,076.0 |
| 2020 first filed | 5,569.8 | 3,983.0 | 1,844.7 | 2,412.1 | 117.0 | 134.2 | 564.0 | 95.95 | 1,148.3 |
| 2020 restated | 5,316.5 | 3,722.8 | 1,643.9 | 2,412.1 | 117.0 | 134.2 | 564.0 | 95.95 | 947.5 |
| 2021 | 5,722.3 | 4,213.5 | 1,630.9 | 2,612.3 | 4.7 | 212.8 | 552.2 | 95.71 | 934.6 |
| 2022 | 6,261.4 | 4,649.9 | 1,817.2 | 2,984.5 | 1.1 | 222.3 | 540.8 | 96.25 | 1,067.5 |
| 2023 | 6,537.5 | 5,022.1 | 1,990.7 | 3,136.3 | 1.0 | 97.5 | 658.4 | 97.58 | 1,177.8 |
| 2024 | 6,981.6 | 5,403.2 | 2,200.4 | 3,360.3 | 1.0 | 105.5 | 682.3 | 99.46 | 1,298.8 |
| 2025 | 7,578.8 | 5,810.1 | 2,391.7 | 3,604.2 | 0.6 | 109.4 | 721.4 | 100.48 | 1,451.4 |

(2026-06-30, 10-Q: assets 8,024.5; equity 2,643.5; debt 3,703.0; cash 34.0; shares 101.41M. No goodwill in any year;
intangibles peaked at $41.1M in 2017 from $55.7M of wholesale energy contracts bought that year and were amortized to nil by
2024.)

**What moved, and why.** (1) Plant and debt. Net plant rose from $2.41B to $5.81B (2.4 times) and debt from $1.24B to $3.60B
(2.9 times) while equity rose 2.05 times; debt was 51% of debt plus equity in 2016 and 60% in 2025. The business is being built
with borrowed money faster than with owners' money. (2) Shares. 86.09M to 100.48M (+16.7%), from a $212.9M public offering in
FY2020 and continuous issuance under the DRP and the waiver-discount program. (3) Cash. Never more than $117M at a year end, and
under $5M in eight of ten; the company lives on its bank lines and commercial paper (Item 1A: "We have relied, and continue to
rely, upon short-term bank borrowings or commercial paper supported by our revolving credit facilities"). (4) Receivables and
gas in storage move with the gas price, not with sales effort: billed receivables $222M and storage $274M at the 2022 price
peak, $97.5M and $200M a year later. Nothing out of line. (5) Regulatory assets rose from $496M to $721M; they are costs the BPU
has allowed or is expected to allow NJNG to recover (MGP remediation $167.0M, CIP, BGSS, SAVEGREEN, pension), and the 10-K names
their disallowance as a risk. They are the one asset on this balance sheet whose value depends on a regulator's future decision.
(6) Retained earnings fell between the 2020 as filed and the 2020 restated column by $200.8M: in FY2021 the company changed its
accounting for investment tax credits at Clean Energy Ventures "from the flow through method to the deferral method", applied
retrospectively, which cut FY2019 net income from $169.5M to $123.9M and FY2020 from $193.9M to $163.0M (FY2021 10-K, Note 2
and the restatement table). The change moved the accounts toward the slower, more conservative recognition, the one the filing
says "is considered the preferred method per the authoritative guidance"; it is evidence for the accounts, not against them. What the figures say: a utility growing its plant on
borrowed money and new shares, paying out about half its earnings. What they cannot say: whether the regulatory assets and the
rate base will be recovered in a New Jersey that electrifies (Q2).

**The real costs.** Depreciation is real and here it is short of what is spent: "Depreciation charges are a more complicated
subject but are almost always true costs" **[L2015-004]**; capital spending ran 4.1 times depreciation (Q3). Stock pay is
expensed ($17.8M in FY2025) and deducted again in owner cash (Step 0). Restructuring charges: none found in the span read. The
FY2021 PennEast impairment ($92.0M, equity in earnings of affiliates) and the FY2025 $58.2M gain on the residential solar sale
are both real and both one-time; neither is in owner cash, which starts from operating cash. Cash income taxes are small
($9.9M in FY2025 against a $97.0M provision), because of deferred taxes on utility plant and solar credits; Q7 says how that is
treated. The asset management agreements of December 2020 paid Energy Services "approximately $260M in cash from fiscal 2022
through fiscal 2024" with "approximately $34M per year from fiscal 2025 through fiscal 2031" to come (Item 1): cash received
ahead of the revenue, which flatters operating cash in the FY2022 to FY2024 years of the window; recorded, and weighed at Q7.

**EBITDA and the adjusted figure in the filer's own mouth.** The company's headline earnings figure is net financial earnings
(NFE), "a non-GAAP financial measure" that removes unrealized derivative gains and losses and the timing of hedges on gas
inventory (Item 7). Over FY2023 to FY2025 NFE ($882.3M) and net income ($890.1M) are within 1% of each other and the adjustments
run both ways (-$38.1M, +$19.6M, -$12.1M before tax), so the figure does not wave away real costs; but it is the figure featured
in every release, guidance is given on it per share (FY2026 NFEPS "$3.52 to $3.62", "7 to 9 percent long-term NFEPS growth
target, starting from a fiscal 2025 base of $2.83 per share", 8-K exhibit 99.1, `0001140361-26-030982`), and officers are paid on
it (Q5, Q6). For one segment, Storage and Transportation, "Management uses Adjusted EBITDA and NFE, non-GAAP financial measures,
when evaluating the operating results of S&T" (Item 7). The rows: "The one figure we regard as utter nonsense is the so-called
EBITDA" **[M1998-086]**; "a management that regularly attempts to wave away very real costs by highlighting "adjusted per-share
earnings" makes us nervous" **[L2016-006]**; and the scourge of "earnings "guidance" and the desire of CEOs to "hit the
number."" **[L2019-006]**. These are the habits the make-the-numbers paragraph sends to Q5: "We regard it is a negative when we
find a management that’s preoccupied with accounting considerations. But, we find it so frequent that we can’t afford to use it
as a total exclusionary factor." **[M1994-018]**.

**Confusion or suspicion?** The accounts read cleanly: sale-leasebacks of solar assets are booked as financing obligations inside
long-term debt, not as sales; derivatives are marked to market and reconciled; the regulatory assets are listed by kind; the one
accounting change of the span went the conservative way. No prepaid or deferred account builds out of line, no reserve moves with
a stock sale, inventories follow the gas price **[M1995-064]**. Nothing confuses me and nothing raises suspicion **[M1995-063]**,
**[M1995-065]**.

**VERDICT on the accounts: WEIGHS AGAINST**, not a STOP: the accounts can be read and show a business whose spending runs far
past its depreciation and its operating cash **[L2015-004]**, **[M2025-032]**; the featured non-GAAP per-share figure, the
guidance on it and the segment EBITDA are recorded as a weighing against and carried to Q5 **[L2016-006]**, **[L2019-006]**,
**[M1994-018]**. The recast earnings fed to Q7: owner cash from the filed cash-flow statements, after stock pay and all capital
spending, with the depreciation proxy for maintenance beside.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
The people: Stephen D. Westhoven, President and CEO since October 2019, an officer since 2004; Roberto Bel, CFO since January
2022; Patrick Migliaccio, COO of NJNG (CFO before him); a separate, independent chair of the board since January 2020 (proxy,
`0000356309-25-000096`; 10-K Item 1). For a marketable stock the speakers read rather than meet **[M1994-009]**: "read the proxy
statements, see what they think of — see how they treat themselves versus how they treat the shareholders, look at what they
have accomplished, considering what the hand was that they were dealt".

**The habits carried from Q4, read with the integrity record.** The FY2025 results release (8-K exhibit 99.1, filed 2025-11-19,
`0001140361-25-042738`) says: "Achieved high end of fiscal 2025 net financial earnings per share (NFEPS) guidance range of $3.20
to $3.30 , which was increased in the second quarter of fiscal 2025" and "Fiscal 2025 marks the fifth consecutive year that NJR
has outperformed its initial annual NFEPS guidance". The FY2024 release (`0001140361-24-047766`) likewise reports the "higher end
of fiscal 2024 [...] guidance range". The FY2026 third-quarter release raised the lower end again. The rows on this habit are
plain: "we become downright incredulous if they consistently reach their declared targets. Managers that always promise to
"make the numbers" will at some point be tempted to make up the numbers." **[L2002-041]**; and the test is "things that they do
in public in relation to their investors and the promises they make" **[M2004-067]**; "If you’ve got doubts, forget it."
**[M2013-088]**.

Read with the rest of the record, does the habit leave doubt about honesty? What I find:
- *What the beats are made of.* FY2025's NFE rose on a base-rate increase at NJNG ($80.1M more earnings) and a $58.2M pre-tax
  gain on the sale of the residential solar portfolio, both disclosed and both in GAAP; Energy Services "Benefitted from natural
  gas volatility during the 2025 winter period, contributing to NFEPS guidance increase" (FY2025 release). These are a rate
  order, a sale and the weather, each named; I find no beat made of a reserve release, a change of estimate or a reclassification.
- *The adjusted figure is close to GAAP* (Q4: within 1% over FY2023 to FY2025, adjustments both ways), and for pay the board took
  the gain out: "For purposes of performance measurement in fiscal year 2025, the LDCC adjusted NFEPS to remove the one-time gain
  and the associated taxes and dilution to NFE from NJRCEV's sale of the 91 MW residential solar portfolio" (proxy). The
  long-term target is stated "starting from a fiscal 2025 base of $2.83 per share", which also leaves the gain out. A management
  inflating the figure would have kept the gain in both places.
- *The one accounting change of the span* moved credit recognition to the slower method, cutting FY2019 and FY2020 earnings by
  $76.5M on restatement (Q4).
- *The talk about mistakes.* The PennEast pipeline investment was written off by $92.0M in FY2021 "because of numerous
  regulatory and legal challenge" (FY2021 10-K); the loss was charged in GAAP and the 10-K says why in plain words. (Written down
  as found **[M1997-127]**: this is also evidence for Q2's contrary side, a gas pipeline into New Jersey stopped by regulatory and
  legal challenge.)
- *Governance.* Chair and CEO separate; directors and officers "prohibited from pledging the Company’s securities as collateral";
  share ownership guidelines (directors five times the cash retainer; "Each of the named executive officers were in compliance");
  a recoupment policy beyond the Dodd-Frank minimum (proxy).
- *No restatement for error, no investigation, no enforcement matter* found in Item 3 of the FY2025 10-K or the 10-Q (search of
  both for "investigation", "subpoena", "class action", "consent order": only the MGP environmental proceedings with the NJDEP).

The habit is real and advertised, and it weighs against **[L2002-041]**, **[L2019-006]**; but the record read with it shows the
beats made of disclosed, GAAP-visible events, the adjusted figure close to GAAP, and the board stripping a gain out of its own pay
measure. I do not find the doubt that closes the file **[M2013-088]**; I find a management that plays the guidance game in the
open, which Q6 Part B weighs as pay design.

**Treatment of owners against themselves** **[M1994-009]**. CEO total pay FY2025 $6.43M (summary compensation table), against
consolidated net income of $335.6M; target mix salary $1.01M, annual incentive $1.11M, long-term equity $3.50M. Not lavish for the
size; the design is the question, and it belongs to Q6 Part B.

**Love of the business; ability.** The CEO has spent over twenty years in the company (officer since 2004); I have no evidence on
love of the business beyond tenure, and I say so. Ability, "how well they run the business [...] the hand they were dealt"
**[M1994-008]**: the utility is run as the field runs it (a full rate case won in 2024 at 9.6%, customers added every year, the
second case filed on schedule), and the non-utility capital has a mixed record: PennEast lost, Clean Energy Ventures built on tax
credits, Energy Services' trading earnings swinging with winters. "The really great business is one that doesn’t require good
management." **[M1996-037]**: the utility is the part that does not need it.

**VERDICT on integrity: IN** (the make-the-numbers habit recorded and weighed, not found to raise the doubt that closes the file
**[M2013-088]**, **[L2002-041]**). **Ability WEIGHS FOR, narrowly**, on the running of the utility; the use of capital outside it
is weighed at Q6 **[M1994-008]**, **[M1996-037]**.


## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
**The retention test.** "We test the wisdom of retaining earnings by assessing whether retention, over time, delivers
shareholders at least $1 of market value for each $1 retained." **[R1995-009]**. Here the owners supplied two kinds of money:
earnings kept, and new money through share sales. FY2018 to FY2025 (eight fiscal years; filed statements, FY2019 and FY2020 net
income as restated): net income $1,803.2M less cash dividends $1,058.6M = **$744.6M retained**; new shares sold for **$560.7M**
(the FY2020 public offering $212.9M, waiver-discount issuance $221.5M, DRP $126.3M). Owners' money put in: **$1,305.3M**. Market
value: 86.56M shares at $42.15 on 2017-09-29 = $3,648.5M; 100.48M shares at $48.15 on 2025-09-30 = $4,838.1M (aggregator closes,
flagged): **+$1,189.6M**. Per share: retained about $7.90 per average share against a price gain of $6.00. On the market leg the
test fails narrowly over eight years: less than a dollar of market value for each dollar kept or raised. Against intrinsic value
the test fails more plainly: Q7's central range for the whole business is below the debt it carries (Q7). The forward question,
"Can you keep using all of the capital you generate, effectively, for a very long time?" **[M2010-097]**: the utility can use
all of it and more, at the regulator's return, which is why it must also raise money outside. The check the speakers set is
"if after three or four years, you’ve found that the dollars we’ve retained hasn’t created more of that in value, then the
presumption becomes very strong at that point that we should start paying out money" **[M1998-110]**; at NJR the opposite
presumption also fails, because the business could not pay out more without borrowing more.

**Dividends with one hand, issuance with the other.** NJR pays about half its earnings in cash dividends ($180.1M in FY2025) in
years when operating cash does not cover capital spending, and in the same years sells shares to its owners at a discount through
the waiver-discount program and the DRP ($34.8M in FY2025, $74.4M in FY2024). The owner receives a dollar and is offered the
chance to buy it back as new shares; the difference is borrowed. "dividend policy should always be clear, consistent and
rational" **[L2012-015]**: it is clear and consistent; whether it is rational for a business that needs outside money every year
is the question the rows put through the retention test, and the test fails above. Serial issuance: "we have never invested in
companies that are hell-bent on issuing shares" **[L2014-015]**. NJR's issuance is steady and small (no more than 2% of the shares
in any year but FY2020, when it was 6.6%), sold at prices near the market, and used to fund rate base, not deals; it is not the promotion the row
describes, but it is continuous, and the framework carries serial issuance as an unresolved candidate STOP. I weigh it against
and do not close the file on it.

**Buybacks.** The only repurchase in the span read is FY2021's $27.2M of treasury stock (FY2023 10-K cash-flow statement), with
no stated price limit found. The test: a buyback with no stated price weighs against "unless the prices actually paid sit at or
below the bottom of the Q7 range" (Q6, the framework's convention), the value being "entirely purchase-price dependent"
**[L2016-002]**. *Written back at Q7 (2026-10-18):* the bottom of the central Q7 range is -$18.22 a share (all-equity; equity-only bottom
$5.26). The FY2021 purchases were made at market prices of a stock that traded above $30 that year (aggregator closes: $34.81
on 2021-09-30), far above the bottom and above the top ($15.91) of the range, so the no-stated-price buyback **weighs against**;
it was small ($27.2M) and not repeated in FY2022 to FY2025.

**Issuance and deals.** The one large purchase of the span, Leaf River and Adelphia in FY2020 ($523.6M, "Acquisition of assets,
net of cash acquired", FY2020 10-K), was paid in cash, funded by the $212.9M offering and debt; no all-stock deal in undervalued
stock, so the one STOP of Part A **[L2009-019]** does not arise. What it has returned: Storage and Transportation's NFE was
$12.8M to $22.5M a year on about $1.0B of segment assets (Note 15), about 1% to 2% after tax on assets; the PennEast write-off
($92.0M) sits in the same segment. "Only if we receive less in value than we give." **[M1995-001]**: on those returns the segment
has not yet given back what was paid.

### Part B: pay, the board, the owners
**Pay tied to what the person controls** **[M2003-019]**. The long-term plan pays on three-year cumulative NFEPS and on total
shareholder return against a comparator group; the annual plan includes NFEPS and a leadership component (proxy,
`0000356309-25-000096`: "NFEPS is the most important financial measure used to link compensation actually paid to Company
performance"). Per-share earnings in a business that grows them by putting in borrowed and newly raised capital carry no charge
for that capital: "When capital invested in an operation is significant, we also both charge managers a high rate for
incremental capital they employ and credit them at an equally high rate for capital they release." **[L1994-019]**; "a batting
average that does not include a cost of capital is a phony batting average" **[M1995-010]**. Relative TSR rewards the stock's ride
against peers, not what the managers control. And the plan pays on the same figure the company guides on: "the scourge of
earnings "guidance" and the desire of CEOs to "hit the number."" (the row's words, **[L2019-006]**). In the board's favour: an
independent chair separate from the CEO since 2020; directors required to hold five times their cash retainer; pledging
prohibited; the solar gain taken out of the FY2025 pay measure (Q5).

**WEIGHS AGAINST, Part A**: the retention test fails over eight years on the market leg and plainly on the intrinsic leg; a
dividend paid from borrowed money while shares are sold to fund the business; no all-stock deal **[R1995-009]**, **[M1998-110]**,
**[L2014-015]**. **WEIGHS AGAINST, Part B**: pay on per-share earnings with no capital charge and on relative TSR, guided in public
**[L1994-019]**, **[M1995-010]**, **[L2019-006]**; the board's structure weighs for.

## Q7: WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is the
risk-free interest rate" **[L2000-021]**, held as a range **[L2000-024]**, at the long government rate, 5.43% (Step 0).

**Owner cash, from the filed cash-flow statements** ($ millions; script `Test Runs/_research 2026-10-18 NJR/scripts/q7.py`,
output `q7_output.txt` and `q7b_output.txt`). All spending = utility plant + solar equipment + storage and transportation and
other + cost of removal, with equity-investee flows and business sales netted (specific (c): the FY2025 $137.2M proceeds from
the residential solar sale netted against spending; no business bought inside the window; the FY2020 Leaf River and Adelphia
purchase, $523.6M in cash, lies before it and its earnings are inside the window's statements). Maintenance = depreciation and
amortization + cost of removal (the depreciation proxy **[M1998-127]**; the filing does not split NJNG's spending into
maintenance and growth in a form I could read, so the guess **[M2000-144]** is the depreciation charge plus the removal cost NJR
pays in cash beside it). Stock pay deducted. All-equity basis adds back interest paid at (1 - 25%) (CONVENTION of this run: the
federal 21% plus the filer's "State income taxes, net of federal benefit" line, about four points a year over the window).

| FY | Operating cash | Stock pay | All spending (net) | Owner cash, all spending, after interest | same, all-equity | Owner cash, maintenance only, after interest | same, all-equity |
|---|---|---|---|---|---|---|---|
| 2021 | 391.0 | 7.1 | 622.1 | -238.3 | -179.3 | 222.1 | 281.1 |
| 2022 | 323.5 | 14.8 | 590.6 | -282.0 | -218.7 | 140.1 | 203.4 |
| 2023 | 479.0 | 14.7 | 538.6 | -74.3 | 6.8 | 270.8 | 351.9 |
| 2024 | 427.4 | 16.0 | 569.1 | -157.7 | -67.5 | 196.4 | 286.6 |
| 2025 | 466.3 | 17.8 | 568.3 | -119.7 | -22.0 | 213.8 | 311.5 |
| **Five-year average** | | | | **-174.4** | **-96.1** | **208.6** | **286.9** |
| Literal ten-year window FY2016-25, beside | | | | -217.2 | -160.2 | 157.5 | 214.4 |

**Whose tax.** Operating cash carries the cash taxes actually paid, which were small ($9.9M in FY2025 against a $97.0M provision;
FY2021 to FY2025 the provision exceeded cash paid by $58.9M a year on average), sheltered by deferred taxes on utility plant and
by solar credits that the OBBBA is ending for new projects (10-Q). The framework asks owner cash at the statutory rate with the
shelter's present value added back where credits run out inside ten years. I did not build that schedule; the direction is
known: at the book tax provision the maintenance-case owner cash falls from $286.9M to $228.0M and the top of the range from
$15.91 to $5.22 a share. Every figure below uses the cash-tax figure, the more generous one, and the box does not change on the
stricter one.

**The specifics, in order.** (a) *Cycles.* No end year of the window is a cyclical peak or trough on the filer's own
description. Two things flatter the window and are recorded, not removed: the AMA prepayments ("approximately $260M in cash
from fiscal 2022 through fiscal 2024", ahead of the revenue), and the FY2025 sale proceeds netted under (c). Removing either
would lower every case. (b) *Decline.* The all-spending series is negative in every year of the window, so its growth rate is
meaningless; the maintenance series is positive and grew 2.60% a year end to end (all-equity, FY2021 $281.1M to FY2025
$311.5M), 7.28% between the halves of the window (shown beside). (c) *Acquisitions:* above; not a serial acquirer. (d) *Working
capital* is inside operating cash and counted. (e) *Growth spending.* The filing allows the maintenance guess, so the central
case is owner cash after maintenance only, and the growth spending ($383.0M a year on the five-year average, the difference
between the two series) is charged against the growth it buys in the growth case, for ten years, stopping when growth stops.
(f) *The cap.* The shown 2.60%, carried ten years, would take maintenance owner cash to $371.0M, 18.2% of FY2025 revenue and 21.0%
of revenue carried at the company's own sales growth, above the highest share earned in the window (17.9%, FY2023). So the growth
carried is the business's own sales growth FY2021 to FY2025, **-1.42% a year** ($2,156.6M to $2,036.4M); the shown 2.60% and the
cut are both written down, and the uncapped case is shown beside. (Revenue here includes gas costs passed through to customers,
so it moves with the gas price; I record the oddity in the framework section and apply the text as written.)

**The range, all-equity basis (central)**, enterprise value less net debt of $3,669.0M, per share on 101.468M shares:

| Case | Per share, at 5.43% | Expected return at $52.19 |
|---|---|---|
| Top: maintenance only, no growth (central, (e)) | **$15.91** | 3.20% |
| Bottom: growth case, growth capped at sales growth (-1.42%), growth spending charged ten years | **-$18.22** | 2.03% |
| Beside: growth case at the shown 2.60%, uncapped | -$0.61 | 2.94% |
| Beside: growth case at the halves rate 7.28% | $28.38 | 4.36% |
| Beside: literal ten-year window, maintenance, no growth | $2.76 | |
| Beside: all spending, no growth, forever | -$53.61 | negative |

The inversion (growth case below the no-growth case) is the finding the framework names: "growth can destroy value if it requires
cash inputs in the early years of a project or enterprise that exceed the discounted value of the cash that those assets will
generate in later years" **[L2000-023]**. Here it means that at a 5.43% rate the regulated return of about 7% after tax barely pays
for the money it takes, and at the 10% floor it does not.

Equity-only basis (beside, never decides alone): top $37.87, bottom $5.26 (capped), expected return at the price 3.94% and
2.10%. The equity-only figures are higher because NJR's after-tax interest ($97.7M on $3,669M of net debt, about 2.7%) costs less
than the 5.43% discount rate; the lenders are taking a smaller return than the long bond, which flatters the per-share figure in
exactly the way **[L2017-004]** warns of.

**The floor first** *(the framework's order since 2026-10-10)*. "we don’t want to buy equities where our real expectancy is below
10 percent" **[M2003-149]**. At $52.19 no case of the range earns it: the best case I can defend, the maintenance case with no
growth, yields 3.20% on the enterprise value; even the halves-rate growth case, which I do not hold as central, returns 4.36%; and
a ceiling that is not a case at all (maintenance owner cash grown 7.28% for ten years with no growth spending charged, the double
count the framework forbids) returns 5.69% (q7_output.txt). Every one of them is below the floor, and every one is below the long
bond itself. The price is also above the top of the range, which closes OUT by the same floor. **"Well, if government bond rates
were 2 percent, we’re not going to buy a business to earn 3 or 3 1/2 percent expectancy over the years."** **[M2007-095]**: here
the bond pays 5.43% and the business offers about 3%.

**Value range: -$18.22 to $15.91 a share (all-equity, central) against $52.19.** Width not tested: the floor closes the file first.

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued with its own cash at 10% and the two
averaged, after the company's own (cash) tax: **all-equity -$20.77 a share, not positive** (top at 10%: -$7.88; growth case at
10%: -$33.66); **equity-only $8.03 beside it** (top $20.56; growth case -$4.51). At 10% even the maintenance case's whole
enterprise value ($2,869M) is below the net debt ($3,669M). No cheap price is reported.

**VERDICT: OUT** at Q7, on the floor: no case in the range earns about ten percent at the price, and the price sits above the top
of the range **[M2003-149]**, **[L2000-023]**, **[M2007-095]**.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT). Facts found are under AFTER THE STOP.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT**, decided at **Q7** on the floor: value range **-$18.22 to $15.91 a share** (all-equity, central; equity-only $5.26 to
$37.87 beside) against **$52.19**; the best defensible case yields 3.20% on the enterprise value, below the 10% floor and below the
5.43% long bond. Q1 IN, Q2 IN (regulator-set ordinary return carried; political threat recorded; TOO HARD (NATURE) named as the
other reading), Q3 against, Q4 against (not a STOP), Q5 integrity IN and ability for, narrowly, Q6 against in both parts.
Reporting figures (Part VII, not verdicts): fair price **-$20.77 all-equity, not positive**; **$8.03 equity-only**.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.
- **Bears on Q8 (the bond).** The 30-year Treasury yields 5.43% (2026-10-16, US Treasury par yield curve); the business's best case
  at the price yields 3.20% on enterprise value and 3.94% on the equity alone (Q7).
- **Bears on Q9 (debt and exposures).** Debt $3,703.0M at 2026-06-30 (long-term $3,200.1M, current maturities $282.9M,
  short-term $220.0M; 10-Q `0000356309-26-000037`), 58% of debt plus equity; $150M more NJNG notes placed 2026-08-20 to 2026-10-22
  (8-K `0001140361-26-033890`). FY2025 pre-tax earnings before interest against interest, excluding the $58.2M sale gain:
  ($368.3M + $128.6M) / $128.6M = 3.9 times (10-K FY2025). Cash at year end under $5M in eight of the last ten years; the company
  relies on "short-term bank borrowings or commercial paper supported by our revolving credit facilities" ($575M NJR and $250M
  NJNG facilities expiring August 2029, 10-K glossary) and says so in Item 1A. Solar asset financing obligations $471.5M inside
  long-term debt (2025-09-30). Energy Services "could possibly be required to comply with various margin or other credit
  enhancement obligations" on a downgrade (Item 1A). NJNG is one utility in one state; MGP remediation estimated at $144.3M to
  $200.2M, recovered through a BPU rider (Item 3). Operating leases $177.0M outside the debt figure. Debt covenants on
  debt-to-capital ratios (Item 1A).
- **Bears on Q10.** Nothing beyond Q7.
- **Bears on Q12.** No business named in the rows (casinos, tobacco, loading schemes, gambling) is among NJR's; nothing found.
- **Integrity facts:** the make-the-numbers habit (initial NFEPS guidance outperformed five years running, by the company's own
  statement) was reached and judged at Q5, so the box carries no "recorded, not judged" flag.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `1ae70f37`); written question by question; committed after each
      (Q1 `9637fe47`, Q2 `394d403c`, Q3 `dbb96372`, Q4 `072b9caf`, Q5 `ecf8ac1d`, Q6 `0641515e`, Q7 with the Q6 write-back
      `cc4dbc50`, this close in the next commit). **Declared defect in the write-early record:** from the Q3 commit to the Q7
      commit, an append script of mine opened the run file for writing before reading it, so each of those four commits holds
      only the newest section(s) in the run file and the earlier sections were lost from it; each section was also committed,
      the same minute, as a draft in the research folder (`draft_q3.md` to `draft_q7.md`, in the same commits). The run file was
      rebuilt in the closing commit from the Q2 commit's file and those committed drafts, with no change of content; found by
      the id check, which counted 22 ids where there should have been more than 60.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock in `Screens/_daily/` was present at dispatch
      (held by the dispatching session, not touched by me); the fold into the register is the dispatcher's (operator rule ten). A
      run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched, except the one listing of `Test Runs/`
      file names declared under CONTAMINATION at the top, with the commit subjects and memory line seen at dispatch; none used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check script
      `Test Runs/_research 2026-10-18 NJR/scripts/check_run_ids.py`, output `check_run_ids_output.txt`); no E-id; every filing
      fact carries its accession; numbers not from a filing are labelled CONVENTION or are arithmetic on filed figures.
- [x] The order was kept; Q7, the first STOP that failed, closed the run; Q8 to Q12 are NOT REACHED and nothing after Q7 is a
      clearance.
- [x] Owner cash from the filed cash-flow statements after stock pay and all spending, maintenance by the depreciation proxy
      beside, never a net-income proxy (operator rule 5); the sovereign from the US Treasury; aggregator quotes (prices) flagged.
- [x] Contrary evidence written down as found (foundations; Q2's political threat and the closest-call note; Q5's PennEast
      entry); facts for later questions under AFTER THE STOP.
- [x] Not a point-in-time run; no row was rejected for date.
- [x] Only the arithmetic lines of `tools/run.py` were used, and two of those (the owner-earnings window and the "d3" debt
      column) were found wrong for this filer and replaced by the filed statements (Step 0).
- [x] `python tools/check_framework.py` PASS before the closing commit (output in the reply and in
      `Test Runs/_research 2026-10-18 NJR/check_framework_output.txt`).
- Honest gaps: (1) the statutory-tax schedule with the credit shelter's present value was not built (Q7 shows the direction and
  that the box does not move); (2) NJNG's maintenance and growth spending were not split from the filing (the capital table in
  Item 7 is an image), so maintenance is the depreciation proxy; (3) NJNG's own equity is an estimate (54% of net utility plant);
  (4) ONE Gas depreciation was not read; (5) the FY2021 repurchase prices were not read from Item 5 of that year, only bounded by
  the year's closes; (6) the stock-pay add-back could not be seen in the cash-flow statement, so it may be deducted twice
  (at most $17.8M a year); (7) the outcome of New Jersey's proceeding on the future of gas utilities is not in the filings read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Specific (f), the cap, on a pass-through utility.** The cap cuts growth to "the business's own sales growth", but NJR's
revenue is dominated by gas costs passed through without markup, so "sales" fell 1.4% a year over FY2021 to FY2025 because the
gas price fell from its 2022 peak, not because the business shrank (customers and rate base rose). Applied as written, the cap
turns a 2.60% shown growth into -1.42%. The box does not depend on it (every case is below the floor), but for a utility or any
pass-through business the text should say whether "sales" means revenue as filed or a margin the filer reports (here, utility
gross margin), and I applied revenue as filed. (2) **Specific (e) where growth spending is compulsory and regulated.** The
central case values maintenance-only cash at no growth, and the growth case charges the growth spending for ten years; for a
utility whose growth spending earns a regulated return a little above the long bond, the result swings on the discount rate (at
5.43% the halves-rate growth case is above the top; at 10% every growth case is below it), and the text does not say which
growth rate to carry when end-years and halves both are meaningful but differ (2.60% against 7.28%). I took end-years as "the
growth the business has actually shown" and showed halves beside. (3) **Q2's regulated-return exception and a political threat.**
The exception carries a regulator-set ordinary return to Q3, but the text does not say how to judge a castle whose threat is the
regulator's own State (an executive order opening a proceeding on the future of gas utilities). Whether that is "a castle whose
future cannot be judged" (TOO HARD (NATURE)) or a narrowing to be weighed is left to the analyst; I judged IN with the other
reading written down. A sentence on regulatory or legislative threats to a regulated castle would make two analysts agree.
(4) **Q4 and EBITDA.** The STOP paragraph quotes **[M2002-026]** on EBITDA talk ("about zero") inside "Why confusion is a STOP",
while the make-the-numbers paragraph sends an adjusted figure featured to Q5 as a weighing; a segment EBITDA used for 6% of
earnings fell between the two, and I weighed it. (5) **Whose tax, in a deferred-tax utility.** The statutory-rate rule was written
for carryforwards and credits that run out; a regulated utility's deferred taxes on accelerated depreciation do not run out while
it grows, and the text does not say whether they are a shelter to be priced separately or ordinary cash. I used cash taxes and
showed the book-tax direction. (6) **The template's "Shares by class" check against "issued shares less treasury shares"** could
not be done exactly: the balance sheet states outstanding shares directly and the par-value dollar total divided by $2.50 gives a
number (101.2M) below the outstanding count, a presentation I could not reconcile from the face of the statement; the cover count
was checked against the stated outstanding count instead.
