# Company Run: North American Construction Group Ltd. (TSX and NYSE: NOA), 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from `Test Runs/_TEMPLATE - Company Run.md`
to this dated name before any fetch (commit 497b28f8).

**Dispatched blind run** under `Screens/_daily/_dispatch_brief.md` with the brief's two stated departures (the analyst
derives the lines of evidence; a 40-F filer's exhibits stand in for Items 1, 1A and 7).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-16), after the run was committed: **not held** (`PORTFOLIO.md` carries no line for NOA).

**Contamination, declared and not used.** (1) At the start of the session the harness showed the repository's recent
commit subjects, which describe a different company's run of today (KGS, closed OUT at Q2 on a contract-compression
field) and the git status, which names research folders of two other companies (AYI, ARCB). (2) To check whether my
own dated file already existed I listed `Test Runs/` filtered to today's date, which the blind rule forbids as a
listing; it showed twelve other run files of today (HMH, INVX, KGS, NESR, NGS, NOV, OIS, OMSE, PED, RCON, SEI, USAC)
and their research folders, by name only; none was opened and none concerns NOA. (3) The project map and the memory
index loaded with the session name no position in NOA that I saw. Nothing from any of these is used below.

**Lines of evidence chosen, and why** (the brief leaves them to the analyst). NOA is a fleet-owning contractor paid by
the hour or by the unit by a few large mine operators, so the lines that decide it are: (a) how its work is won and
priced (the AIF's Competitive Conditions, the MD&A's risk factors on competition, insourcing, unit-price and inflation
terms); (b) who the customers are and how concentrated (note 16(f)); (c) the parts, Canada against Australia, over
five years (note 18 of the FY2025 and FY2023 statements); (d) returns on the assets employed over a full oil-sands and
coal cycle, against SEC-filing earthworks contractors; (e) the capital the fleet consumes (sustaining against growth
capital, finance-lease additions outside cash capex, depreciation); (f) acquisitions and their deferred payments
(MacKellar 2023, IMC 2026); (g) debt, leases and guarantees; (h) buybacks, stock pay, the adjusted figures the filer
features; (i) litigation, claims and restatements.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** CAD 16.27, TSX close 2026-10-15, via `tools/run.py NOA --quote NOA.TO` (**aggregator, live quote only,
  flagged**, operator rule 5). The NYSE line printed USD 11.46 the same day; it is not used, because the earnings
  currency is the Canadian dollar and the tool refused to convert (its currency guard).
- **Shares:** `python Screens/cover_shares.py NOA` reads 28,821,481 common shares from the FY2025 40-F
  (0001368519-26-000005), as of 2025-12-31. That is the **issued** count: the balance sheet (exhibit 99.3) shows 871,244
  of them held as treasury shares by the RSU/PSU trust, so 27,950,237 net at 2025-12-31. Checked against the later
  filings: the June 2026 quarter 6-K (0001368519-26-000013, filed 2026-08-12) shows 27,710,462 issued less 881,390
  treasury = **26,829,072 net at 2026-06-30** (its statement of shares), and 27,710,462 issued with 796,568 treasury at
  2026-08-07 (its outstanding share data). The count used is **26,829,072**, the latest filed statement figure.
  The AIF says there are no non-voting shares outstanding.
- **Market cap:** 16.27 x 26.829M = **CAD 436.5M**.
- **Sovereign for the earnings currency:** **4.19%**, Government of Canada long-term benchmark bond yield, Bank of
  Canada Valet series BD.CDN.LONG.DQ.YLD, observation 2026-10-14 (fetched 2026-10-16; saved as
  `boc_long.json` in the research folder). The Bank of Canada is the issuing authority's agent for the Government of
  Canada's benchmark series; **the protocol's sovereign table lists USD, JPY and EUR only and does not list CAD**, and
  `tools/sources.py` has no CAD source configured (the tool said so), so the rate was taken by hand and is said so here.
- **Filings read** (operator rule 4): the FY2025 40-F, filed 2026-03-12, accession **0001368519-26-000005**: exhibit
  99.1 the year-end news release, **99.2 the Annual Information Form** (dated 2026-03-11), **99.3 the audited
  consolidated statements** (KPMG, unqualified, report dated 2026-03-11), **99.4 the MD&A**; the June 2026 quarter 6-K,
  **0001368519-26-000013** (filed 2026-08-12, statements and MD&A, and its release exhibit); the FY2023 40-F
  **0001368519-24-000005** (statements exhibit and MD&A, for 2022 and 2023); the FY2022 40-F **0001368519-23-000006**
  (statements, for 2021 and 2022); the FY2021 40-F **0001368519-22-000003** (MD&A, for 2020 and 2021 capital split); the
  6-Ks of 2026-06-10 and 2026-06-15 (0001171843-26-004038, -004152: the CAD 200M 7.00% notes), 2026-07-08
  (0001171843-26-004540: an ML Northern five-year fuel-services award, about CAD 135M of backlog), 2026-07-21
  (0001171843-26-004790: Nuna update), 2026-09-10 (0001171843-26-005983: Brad Rogers named CEO from 2026-12-01). The
  management information circular was **not read** (see what I could not get); the file closed before Q5.
- **One figure cross-checked against the filed statement:** cash provided by operating activities FY2025 =
  **CAD 264,089K** on the face of the cash-flow statement (exhibit 99.3, F-4), equal to the XBRL figure 264.1M
  (NetCashProvidedByUsedInOperatingActivities) and to the tool's column; purchase of PP&E 281,095K likewise equal to
  the tagged 281.1M.
- **`tools/run.py NOA` arithmetic lines only.** Without `--quote` it refused (CAD earnings against a USD quote). With
  `--quote NOA.TO` it printed the price, the three share counts (all 28.821M, 2025-12-31, issued), and an owner-cash
  window of **2013 to 2015 only**, flagging that window's last year as over 18 months old: the cash-flow tags it reads
  stop there. Its ten-year balance-sheet table (2016 to 2025) and its debt-on-the-face lines (2022 to 2025) were used and
  checked against the FY2025 and FY2023 statements (total assets 1,819.8M and 1,546.5M agree). **Owner cash was
  therefore built by hand from the filed statements** (`q7_computation.py` in the research folder): see AFTER THE STOP
  and the COMPUTATION. The tool printed no v4 rule I relied on.

### The balance sheets, 2016 to 2025, read before the income account **[M2025-032]** (Step 0, because the file closes before Q4)
The speakers' instruction is to read "balance sheets over an 8 or 10 year period before I even look at the income
account" **[M2025-032]**. From the tool's table, checked against the FY2025 and FY2023 statements (CAD millions):

| year-end | assets | equity | cash | receivables | inventory | goodwill | intangibles | retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2016 | 350 | 159 | 14 | 39 | 3 | - | 2 | -130 |
| 2018 | 690 | 150 | 20 | 68 | 13 | - | 3 | -114 |
| 2020 | 839 | 248 | 44 | 24 | 19 | - | - | -35 |
| 2022 | 980 | 306 | 69 | 40 | 50 | 1 | 7 | 71 |
| 2023 | 1,546 | 357 | 89 | 66 | 65 | 1 | 7 | 123 |
| 2024 | 1,694 | 389 | 78 | 70 | 74 | 1 | 10 | 156 |
| 2025 | 1,820 | 457 | 100 | 149 (plus 30 contract assets) | 76 | 1 | 12 | 176 |

What they say. **Assets grew 5.2 times in nine years and equity 2.9 times; the difference is debt.** Debt on the face
of the balance sheet (current plus long-term, leases included) was 421M at 2022, 693M at 2023, 804M at 2024, 910M at
2025 (note 14: 350M senior notes at 7.75%, 309M equipment financing and finance leases, 174M revolver, 55M convertible
debentures due 2026-03-31, 27M mortgage), and **1,180M of borrowings at 2026-06-30** after a further CAD 200M of 7.00%
notes and the IMC equipment debt (6-K 0001368519-26-000013, liquidity table; the filer's own net debt there,
contingent obligations included, is **1,087.4M**). PP&E is the business: 1,359M of 1,820M of assets at 2025, owned
heavy equipment and "major component parts in use" (note 8). **Goodwill is negligible (0.5M) because the MacKellar
purchase of 2023 went almost wholly into equipment**, so the balance sheet carries no acquisition premium to test; the
deals' price shows instead in the contingent obligations (63.5M at 2025, 74.7M at 2026-06-30 with IMC) and in debt
assumed (MacKellar's 203.9M of equipment financing, note 21 of the FY2023 statements). **Retained earnings moved from a
130M deficit (2016) to 176M (2025)**: the losses of the March-2011 to 2013 fiscal years and the 2014 to 2016 oil-sands
trough (XBRL operating losses of 11.9M, 14.8M, 16.0M in the fiscal years to March 2011, 2012, 2013, and near-zero
operating income 2014 to 2016) were earned back only from 2019. Receivables against sales fell from about 18% (2016)
to about 12% (2025), and the receivable is concentrated: four customers were 68% of 2025 revenue and one Australian
customer 20% of receivables (note 16(f)); 67M of receivables at 2025 are from affiliates and joint ventures, chiefly
MNALP (note 10(b)). Inventory rose from 3M to 76M against sales from 1.4% to 5.9%: it is repair parts and rebuild
components, and the 2025 change of policy moved tires out of inventory into PP&E (note 24, comparatives restated).
**A deferred tax liability of 141M (2025) is growing** (book tax 22.6M against cash tax 10.3M in 2025, note 12): the
fleet is depreciated faster for tax than for the books.

What they do not say and cannot say. They do not show the economics of the joint ventures through which 44% of 2025
revenue was sold (AIF: gross sales to affiliates and joint ventures 44% of consolidated revenue; note 10: revenue from
them 571.2M), nor NOA's guarantees of MNALP's equipment leases (57.7M at 2025, 10.3M at 2026-06-30). They cannot say
what a fleet of this age will cost to keep: depreciation (217.2M in 2025) is the filer's estimate, and the sustaining
capital the filer reports (213.2M in 2025) is its own classification.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would own this "if the market closed for five years"
**[M1997-109]**, which for NOA means owning a fleet of haul trucks hired by the hour to a few mine operators; the
quotation "just tells us prices" **[M2006-077]**. No macro view enters: oil and coal prices are not forecast here; of macro
conclusions the speakers say they "just never enter into the discussion" **[M2000-094]**. Margin of
safety is an attitude here and arithmetic at Q7: if the case needs pencil and paper "it’s too close to think about"
**[M1996-084]**. Who is paid to tell you: the filer's own releases lead with "combined revenue" (its share of joint
ventures added) and adjusted EBITDA (6-K 0001368519-26-000013, release exhibit), which are figures it chooses; they are
read beneath the GAAP statements, not instead of them. The analyst's habits: write contrary evidence down at once
**[M1997-127]**, look for "what you’re missing" **[M2025-013]**.

**Contrary evidence, written down as found [M1997-127]:**
- AIF, Competitive Conditions: "Much of our business is secured through the formal competitive bidding process ...
  Our customers continue to increase the number of competitors on their bid lists in efforts to achieve lower pricing."
- MD&A risk factors: customers may insource the work; long-term contracts let customers "unilaterally reduce or
  eliminate scope of work without cause" (note 2(c)); Australian contracts let the client buy out NOA's equipment at
  predetermined values.
- Note 6(c) and (e): in 2024, 8.0M of previously recognized revenue was given up "in exchange for securing a contract
  extension".
- Field returns: operating income on total assets averaged 5.9% from 2016 to 2025 (6.9% with equity-method earnings),
  against debt costing about 6.4% (6-K 0001368519-26-000013, cash cost of debt).
- Owner cash after all capital spending was negative in 2024 and 2025 (-76.0M and -60.5M, equity-only).
- Three chief executives in one year: Joe Lambert resigned 2026-01-20 "to pursue other opportunities" (AIF), Barry
  Palmer acted, and Brad Rogers was named from 2026-12-01 (6-K 0001171843-26-005983).
- Fargo joint venture: cumulative catch-up write-downs of 7.7M (2025 Q2) and 12.9M (2025 Q4) on lower forecast margins
  (note 10).

## THE STANDING RULE
The rule binds the buyer's conduct: "We are never going to risk what we have and need for what we don’t have and
don’t need." **[M2012-081]**. A purchase of NOA paid in cash and unlevered puts the buyer at no risk of ruin; bought
on margin it would, since "borrowed money has no place in the investor's tool kit" **[L2014-005]**, and the stock's own
2025 range on the TSX (31.67 high in January, 16.78 low in August, AIF) shows how far a levered holder could be pushed.
The target's own debt is Q9's question, not this one.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "can I understand it?" **[M1995-051]**, meaning a fix on "what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**.
- **What the business is, from the filings.** NOA owns about 1,155 heavy-equipment units (AIF, Fleet and Equipment)
  and hires them out, fully maintained or with operators, to surface mines: in Canada as a subcontractor to its 49%
  Indigenous joint venture MNALP on oil-sands sites under three- to five-year non-exclusive master service agreements
  (time-and-materials, rental or unit rates); in Queensland through MacKellar (bought 2023-10-01) on metallurgical and
  thermal coal mines under multi-year contracts with minimum hours; since 2026-04-07 in Western Australia through IMC
  (gold, iron ore, lithium). 85% of 2025 revenue was time-and-materials, 15% unit-price (note 6(a)).
- **The key variables, and whether they are foreseeable.** (1) Whether mine owners keep outsourcing overburden,
  reclamation and fleet hire rather than doing it themselves; (2) the rate the bid process lets NOA charge per hour or
  unit; (3) fleet utilization and the cost of keeping the fleet; (4) the life of its customers' mines (oil-sands mines
  operate for decades; the AIF says NOA has "participated in every significant oil sands mining project" for over 40
  years, and one Queensland stockpile client has used it for over 30 years). These are visible in ten years of
  statements; the past statements do tell what the future ones will look like in kind, a capital-heavy hire business
  paid on bid rates. The framework's paragraph on a commodity business says a dependence on a commodity price is never
  by itself a STOP at Q1. The speakers' own words: "We don’t think we can predict commodity prices." **[M2016-025]**;
  and the decision is made "off the figures" **[M2008-069]**, which here are available.
- **What I doubt.** The ten-year life of the Queensland **thermal** coal work and the pace of the Western Australian
  expansion; and the economics of the joint ventures, which the statements show only as condensed tables (note 10). These
  bear on the amount of work, not on whether its economics can be read: they are read at Q2 and Q7.
- **VERDICT: IN.** The economics are readable from the filings: a fleet hired out at bid rates to a few mine operators,
  whose earning power over ten years is set by utilization, rates and the cost of the fleet, all reported. Understanding
  the economics does not require foreseeing commodity prices **[M2016-025]**, **[M2008-069]**, and the forecast here
  is of a kind its insiders do write down (backlog of CAD 4.0B at the AIF's date, contracts to 2029 and 2030).

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing" **[M1995-038]**; a moat is
what "protects excellent returns on invested capital" **[L2007-004]**, and it is judged, not measured: "You have to
understand the businesses." **[M1999-108]**.

**The castle tests, each with its filing fact.**
- *What keeps it standing, the filer's own answer.* The AIF claims experience (70 years in western Canada, 55 years
  in Queensland), safety, "long-term customer relationships, equipment capacity and scale of operations", and "a
  significant number of trucks larger than 240 tons", which it says give "a distinct advantage over competitors with
  respect to both specialized skill base and equipment availability" (exhibit 99.2, Fleet and Equipment; Competitive
  Conditions). These are real: few contractors can field ultra-class trucks on short notice. The test is whether they
  protect returns, below.
- *The money test.* "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?"
  **[M2011-015]**. The fleet is bought from the same dealers anyone can buy from (Finning and Hastings Deering for
  Caterpillar, SMS for Komatsu, Wajax for Hitachi, AIF Major Suppliers), the labour is union labour under an industry
  agreement (IUOE Local 955), and the customer, the mine owner, is itself the best-funded attacker: the MD&A's first risk
  factor is **customer insourcing**, "Certain customers perform some of this work internally and may choose to expand on
  the use of internal resources" (exhibit 99.4, risk factors). An attacker with money exists in the customer's own
  fleet. "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**.
- *Pricing power and the agony before a rise.* Work is won by bid: "Much of our business is secured through the formal
  competitive bidding process. Our competitive environment and customer behavior is focused on lowering costs ... Our
  customers continue to increase the number of competitors on their bid lists in efforts to achieve lower pricing."
  (AIF, Competitive Conditions). Through the last inflation the filer relied on escalation clauses that "may lag the
  actual cost increases thereby reducing our margins in the short term", and not all contracts carry them (MD&A risk
  factor, Inflation). In 2024 it gave back 8.0M of revenue already recognized "in exchange for securing a contract
  extension" (note 6(c), 6(e)). Gross margin (reported gross profit over revenue, XBRL from the 40-Fs) ran 13.8%,
  13.2%, 16.0%, 18.0%, 12.6% from 2021 to 2025. A business with power over its price does not concede booked revenue to
  keep a customer; the speakers' measure is "the agony they go through in determining whether a price increase can be
  sustained" **[M2005-020]**, and here the price is set by the bid list.
- *The low bid.* The test is whether the customer would choose it over the cheaper offer; See's passed because "it
  wouldn’t be a question of people buying candy for the low bid" **[M2017-009]**. NOA's customers, by the filer's
  own description, are "focused on lowering costs" and widen bid lists to get lower prices; and its contracts let them
  "unilaterally reduce or eliminate scope of work without cause" (note 2(c)) or, in Australia, buy out its equipment
  at predetermined values (MD&A risk factor). This is the commodity mark the 2004 letter names: "most insureds don't
  care from whom they buy" and "Consequently, price competition in insurance is usually fierce." **[L2004-003]**.
- *The low-cost exception.* "Another way to prosper in a commodity-type business is to be the low-cost operator."
  **[L2004-007]**; the position is read "more by cost of production" **[M2006-004]** from the filer's and its rivals'
  figures. No filing read states NOA's cost per hour or per unit against a rival's, and its returns (below) sit inside
  the field's, not above it; a low-cost operator in a commodity field would show returns the others cannot reach. The
  filings do not show NOA to be the low-cost operator. Customer concentration cuts the same way: four customers were
  27%, 20%, 11% and 10% of 2025 revenue (note 16(f)), so the buyer, not the seller, holds the bargaining position.
- *Share of mind, the brand.* Not a consumer business; the nearest thing is reputation for safety, which the filer says
  is a condition of being asked to bid ("Certain clients will not engage contractors to perform work if their safety
  practices do not conform", MD&A risk factor, Health and Safety). A condition of entry, shared by every contractor on
  the bid list, is not a reason the customer pays more.
- *Ask the competitors.* Not possible from the public record within this run; no rival is named in the filings
  (searched: "compet" across exhibits 99.2, 99.3, 99.4). Recorded, not answered.
- *Widening or narrowing.* Against: customers adding bidders (AIF), the 2024 revenue concession, 2025 gross margin back
  to 12.6%. For: longer committed contracts (the AIF names five-year Queensland contracts to 2029 and 2030, MNALP's
  regional services contract extended to 2029, CAD 4.0B of backlog). Longer contracts lock in volume; they do not show
  rising price, and the filer itself says customers seek them for "safe and cost-conscious execution certainty".
- *What could destroy, modify or reduce it.* Insourcing by a large customer; the end of a mine plan or a short-notice cut
  in volumes (MD&A risk factor, Short-notice Reductions in Work); the decline of thermal coal in Queensland; a large
  fixed-price project gone wrong (Fargo: 7.7M and 12.9M catch-up write-downs in 2025, note 10). "one competitor is
  frequently enough to ruin a business" **[M2012-108]**, and here the customer can be that competitor.

**The competitor row.** The filings name no rival, so the rivals are chosen as a **CONVENTION of this run**: up to
three SEC-filing earthworks and contract-mining contractors, one per kind of work NOA does (contract mining, bid heavy
civil earthworks, site earthworks); rationale: the brief asks for SEC-filing rivals when the filer names none, and these
are the SEC filers whose work is closest to NOA's. Metric: **operating income over year-end total assets, each
filer's own tagged 10-K or 40-F figures, every year 2016 to 2025** (`field_returns.py`, research folder). Pre-tax and
before interest.

| filer | what it does that NOA does | 2016-2025 mean | range | latest annual accession |
|---|---|---|---|---|
| NOA | fleet hire and contract earthworks at mines | **5.9%** (6.9% with equity-method earnings added) | 1.1% (2016) to 9.0% (2024) | 0001368519-26-000005 |
| NACCO Industries (NC) | contract mining (its North American Mining unit) and coal mining; consolidated figures, segments not read | 5.1% | -13.0% (2023) to 12.3% (2022) | 0000789933-26-000070 |
| Granite Construction (GVA) | bid heavy civil construction and earthworks | 2.7% | -6.7% (2020) to 7.0% (2025) | 0000861459-26-000004 |
| Sterling Infrastructure (STRL) | earthworks and site development | 8.7% | -1.6% (2016) to 15.4% (2025), rising each year from 2022 | 0000874238-26-000024 |

Rivals not filing with the SEC: none is named in NOA's filings. The Canadian and Australian contract miners NOA meets
on bid lists are, as far as I know from outside the filings, private or listed outside the United States; they are not
named, not read and not used.

**The parts table** (section B of the gaps case: a part decides at more than half of five-year operating profit, or
else the largest). The filer reports segment gross profit (note 18; FY2023 statements note 17); CAD millions:

| part | 2022 | 2023 | 2024 | 2025 | five-year note | castle | decides |
|---|---|---|---|---|---|---|---|
| Heavy Equipment - Canada | 81.8 | 104.2 | 67.4 | 38.6 | 292.0M for 2022 to 2025, plus most of 2021's 90.4M consolidated gross profit (see below) | open: bid work, insourcing, ordinary returns | **yes, the largest** (about 719M of five-year consolidated gross profit; Australia 294.6M) |
| Heavy Equipment - Australia | 6.7 | 40.6 | 132.2 | 115.1 | owned from 2023-10-01; two full years | bid and contract hire with buy-out options; two years of record | no |
| Other (US mine management, rebuilds, equity-method JVs) | 15.6 | 12.0 | 9.9 | 6.6 | small | not judged | no |

The FY2022 statements (0001368519-23-000006) carry no segment note: in 2021 and 2022 as first filed the company
reported as one business, and the Australian operations of 2021 were the small DGI parts business bought that year for
11.4M. The five-year window is 2021 to 2025, and Canada needs only 2.6M of 2021's 90.4M consolidated gross profit to
pass Australia's 294.6M, so Canada is the largest part and decides; whether it also passes half of the five-year
total depends on the 2021 split, which the filings read do not report, and the rule does not need it. Segment gross profit
is the filer's own segment measure (before corporate costs), used here as the operating-profit measure, said so. Australia, the part
that does not decide, earned segment gross profit of 13.4% (2024) and 9.5% (2025) of its segment assets before
corporate costs and tax (note 18); it is carried, not judged, and its contracts carry the same bid and buy-out terms.

**The field's returns over the last full cycle.** The cycle read is 2016 to 2025: it runs from the oil-sands trough of
2015-2016 through the 2020 collapse in demand and the 2022-2024 recovery to the 2025 dip. Over it NOA earned
operating income of 5.9% of total assets on average (6.9% with its share of joint-venture earnings), its best year 9.0%
(2024, at record revenue); after tax at the 23% this run uses for Canada that is about 4.5% to 5.3%, against a cash
cost of debt of 6.4% (6-K 0001368519-26-000013). Before the cycle it lost money at the operating line in the three
fiscal years to March 2013. The rivals' own filings show the same field: Granite 2.7%, NACCO 5.1%, Sterling 8.7% with
its best years in the last three. These are ordinary returns. "if you have a business that’s earning 5 or 6 percent on
equity and you hold it for a long time, you are not going to do well in investing" **[M1998-006]**; and few rivals do
not cure it: "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**. Every
improvement in the fleet is matched: "the improvement you get one day, your competitor gets the next day"
**[M2004-053]**.

A change for the better? NOA's return rose from 1.1% (2016) to 9.0% (2024). The framework credits a change only on a
full cycle in which the price behaviour held; here the question does not arise, because even the best year of the
recovery is an ordinary return on the assets. Nothing is waiting on a downturn to answer.

**Why OUT and not TOO HARD.** The tenuous-moat row sends a castle to TOO HARD because "We don’t know how to valuate
that, and therefore we leave it alone." **[M2000-019]**; that reason does not apply where the returns are known from ten
years of the filer's and the rivals' own filings. The framework's list names this case as OUT (the standing castle
that protects only ordinary returns), with "ordinary" judged in words and given no figure. The row behind judging it in
words: "You have to understand the businesses." **[M1999-108]**. The castle stands (NOA has held oil-sands work for decades), and what it protects is a bid-priced
return near the cost of its debt. The commodity rows add the second ground: the customer chooses on price
**[L2004-003]**, **[M2017-009]**, and the filings do not show NOA as the low-cost operator that is the one way through
such a field **[L2004-007]**, **[M1997-010]**.

- **VERDICT: OUT.** The deciding part (Heavy Equipment - Canada, the largest over five years) is a standing castle that
  protects only ordinary returns: contract mining won by competitive bid from a few large operators who widen their bid
  lists for lower prices and can insource the work, earning about 6% pre-tax on its assets across 2016 to 2025, inside a
  field of SEC-filing rivals at 3% to 9% **[L2007-004]**, **[M2013-052]**, **[L2004-003]**, **[M2017-009]**,
  **[M2011-015]**. The file closes here; Q3 to Q12 are NOT REACHED.

## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED (closed at Q2). Facts found are under AFTER THE STOP.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED (closed at Q2). The balance sheets were read in Step 0; facts found are under AFTER THE STOP.

## Q5: WHO RUNS IT? STOP on integrity.
NOT REACHED (closed at Q2). Facts found bear on it and are recorded under AFTER THE STOP, not judged.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED (closed at Q2). Facts found, including the buyback prices against the COMPUTATION range, are under AFTER
THE STOP.

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED as a question (closed at Q2). The two reporting figures are computed under AFTER THE STOP, headed
COMPUTATION, NOT A CLEARANCE.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9: COULD IT RUIN US? WEIGHING.
NOT REACHED. Debt facts are under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (not asked; the operator chooses where it applies).

---
## THE BOX
**OUT at Q2**: a standing castle that protects only ordinary returns (Heavy Equipment - Canada decides; contract mining
won by competitive bid, operating income about 5.9% of total assets over 2016 to 2025 inside a field of 2.7% to 8.7%);
**integrity facts recorded, not judged**. COMPUTATION beneath the stop, not a clearance: value range CAD 33.33 a share
(all-equity, organic pair, the no-growth case alone) against CAD 16.27; fair price about CAD -9.58 all-equity (CAD
19.11 equity-only); the default pair beside, 33.33 to 141.61, fair 2.45.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found, each with its source, under the question each bears on* **[M1997-127]**. *No verdict is given on
them and the box is unchanged (operator rule 2).*

### Bearing on Q3 (capital in, earnings out)
- Capital additions (the filer's own measure: net capital expenditures plus finance-lease additions, MD&A
  "Reconciliation of capital additions"), CAD millions, split by the filer into sustaining and growth: 2021 102.2 and
  6.8; 2022 113.1 and nil; 2023 168.6 and 40.4; 2024 223.9 and 84.6; 2025 213.2 and 111.7 (MD&As in
  0001368519-22-000003, 0001368519-24-000005, 0001368519-26-000005). Depreciation over the same years: 108.0, 119.3,
  131.3, 185.0, 217.2. Sustaining capital averaged 164.2M against depreciation of 152.2M.
- Finance-lease additions sit outside cash capex (non-cash, note 22(a)): 51.3M in 2025, 14.2M in 2024, 28.2M in 2023
  (plus 30.5M assumed with MacKellar), 8.9M in 2022, 19.2M in 2021. In 2025 a further 34.0M of trucks came by asset swap
  (note 8), not counted as spending here because 15 units and their financing went the other way.
- Return on the assets employed: see Q2's field table. PP&E (net) rose from 256.5M (2016) to 1,265.3M owned plus 93.6M
  under finance lease (2025), while operating income rose from 3.9M to 109.2M.

### Bearing on Q4 (the accounts)
- Featured figures: the releases lead with "combined revenue" (reported revenue plus NOA's share of joint-venture
  revenue), adjusted EBITDA, adjusted EPS and the filer's own "free cash flow" (exhibit 99.1 of 0001368519-26-000005;
  6-K 0001368519-26-000013). In Q2 2026 the non-GAAP measures add IMC's "economic benefit" for 2026-01-01 to 2026-04-06,
  a period before NOA owned it, which US GAAP puts in the opening balance sheet instead (6-K 0001368519-26-000013, IMC
  note). Adjusted earnings for 2025 Q4 excluded a 4.3M Nuna write-down on a customer's insolvency, a 0.9M bad debt and
  realignment costs as "infrequent" (MD&A, 0001368519-26-000005). The filer publishes guidance: a 2026 outlook of
  combined revenue 1.5B to 1.7B, adjusted EBITDA 380M to 420M, free cash flow 110M to 130M (MD&A, Outlook), raised for
  combined revenue on 2026-08-12 (release headline, 0001368519-26-000013).
- Restatement: 2024 comparatives restated for a voluntary change of policy on heavy-equipment tires (note 24): tires now
  capitalized and depreciated rather than expensed through cost of sales; 2025 net income lower by 3.0M than without the
  change. A change of policy, not an error correction, on the note's own description.
- Revenue from unapproved contract modifications: 3.2M recognized in 2025 (note 6(e)); 8.0M of earlier revenue given up
  in 2024 for a contract extension.
- Contingent consideration on MacKellar: fair value cut by 26.9M in 2025 (a gain through earnings) on "a downward
  adjustment to forecasted performance" (note 16(a)), and by a further 16.4M in H1 2026 (6-K 0001368519-26-000013); in
  2024 it was raised by 53.2M (a charge). These swings pass through net income, not through operations.
- An equity swap on 833,725 of NOA's own shares (par 26.73 and 25.10), entered "for risk management purposes in relation
  to its stock-based compensation arrangements", lost 9.4M in 2025 (note 16(b)).
- Auditor: KPMG LLP, unqualified opinions on the statements and on internal control, 2026-03-11 (exhibit 99.3). Critical
  audit matter: cost estimates on unit-price contracts.
- Taxes: cash taxes 10.3M against a provision of 22.6M in 2025; deferred tax liability 141.3M and growing (note 12).
- The thermal-coal contract named in the year-end release is the Carmichael mine, under an "alliance-type arrangement"
  (exhibit 99.1 of 0001368519-26-000005).

### Bearing on Q5 (integrity facts, recorded, not judged)
- Chief executives: Joe Lambert resigned 2026-01-20 "to pursue other opportunities" (AIF); Barry Palmer, with the
  company since 1982, served from that date; Brad Rogers named President and CEO effective 2026-12-01 after a search
  (6-K 0001171843-26-005983). Martin Ferron, CEO to 2020, is chair.
- The make-the-numbers habit and the adjusted figures featured, listed under Q4 above (guidance published and raised;
  combined revenue and adjusted EBITDA featured; a pre-ownership "economic benefit" added to non-GAAP results). Carried
  here by the framework's rule as evidence on the people, not judged.
- Directors and officers as a group owned 9.9% of the voting shares at 2026-03-06 (AIF, Directors and Officers).
- Contingencies: "various disputes, legal and tax matters are pending", none expected to be material (note 23). No
  investigation by a regulator was found in the documents read.
- The management information circular (pay, its measures, related parties) was **not read**.

### Bearing on Q6 (the money and the owners)
- Buybacks: 2025, 1,781,550 shares at an average CAD 21.24 (the NCIB to 2025-11-03) and 253,058 at CAD 19.24 (the NCIB
  from 2025-11-20), 38.4M in all; after year-end a further 407,616 shares (AIF); 2022, 34.1M; 2021, 16.5M (cash-flow
  statements). Against the COMPUTATION below, those prices sit below the central range point of CAD 33.33, above the
  central fair price (negative), and above or at the equity-only fair price of CAD 19.11. A computation, not a Q6
  finding.
- Issuance: in February 2025 holders converted 72.7M of 5.50% debentures into 3,002,231 shares at CAD 24.23 (AIF). The
  company issued shares at 24.23 and bought shares back at 19.24 to 21.24 in the same year.
- Deals: MacKellar (2023-10-01), total price 383.6M with 203.9M of equipment debt assumed, 65.6M paid in cash and the
  rest in earn-out, deferred and contingent payments (note 21, FY2023 statements); 159.5M of net purchases and deferred
  deal payments 2021 to 2025, against 256.3M of owner cash before purchases (maintenance case). IMC (2026-04-07), about
  CAD 125M: 42.3M cash from the revolver, 12.2M seller takeback, 30.1M contingent earn-out, equipment financing assumed
  (6-K 0001368519-26-000013). Both paid in cash and debt, none in shares.
- Dividends: CAD 0.48 a share a year (AIF).
- Stock pay: RSUs and PSUs settled with shares bought in the market through a trust (note 21); expense 8.7M (2024) and
  a 0.4M benefit (2025, after an 8.2M DSU mark-down).

### Bearing on Q9 (the target's debt)
- Borrowings at 2026-06-30: revolver 145.0M, equipment financing 459.1M, mortgage 26.3M, senior unsecured notes 550.0M
  (350M at 7.75% due 2030, 200M at 7.00% due 2031); cash 167.7M; contingent obligations 74.7M; the filer's net debt
  1,087.4M (6-K 0001368519-26-000013). The 55M 5.00% debentures due 2026-03-31 are gone from the June balance sheet.
- Covenants: senior debt to bank EBITDA no more than 3.0, total debt to bank EBITDA no more than 4.0, interest cover
  above 3.0, in compliance at 2025-12-31 (note 14(d)). Guarantees of MNALP equipment leases 10.3M at 2026-06-30.
- Against owner cash: net debt is about 13 years of the all-equity maintenance owner cash (83.0M a year, below); cash
  interest paid was 67.2M in 2025.

### COMPUTATION, NOT A CLEARANCE (the owner's two reporting figures; Q7's construction; `q7_computation.py`)
**Owner cash**, CAD millions, from the filed statements: operating cash flow (which already charges cash interest and
cash tax, takes joint ventures at dividends received, and counts working capital), less stock pay, less capital (the
filer's sustaining split for the maintenance case; all capital additions for the all-spending case). Never a net-income
proxy (operator rule 5). 2023 operating cash is the figure re-presented in the FY2024 40-F (278.1M; 270.4M as first
filed, the difference being a 7.8M cash settlement of deferred share units, already charged as stock pay in earlier
years); 2024 is as restated for tires.

| | 2021 | 2022 | 2023 | 2024 | 2025 | average |
|---|---|---|---|---|---|---|
| operating cash flow | 165.2 | 169.2 | 278.1 | 241.2 | 264.1 | 223.6 |
| stock pay | 11.6 | 4.8 | 15.8 | 8.7 | -0.4 | 8.1 |
| sustaining capital | 102.2 | 113.1 | 168.6 | 223.9 | 213.2 | 164.2 |
| all capital additions | 109.0 | 113.1 | 209.0 | 308.5 | 325.0 | 212.9 |
| purchases of businesses and deferred deal payments | 11.4 | 2.2 | 62.1 | 43.6 | 40.2 | 31.9 |
| equity-only owner cash, maintenance | 51.4 | 51.3 | 93.7 | 8.6 | 51.3 | **51.3** |
| equity-only owner cash, all spending | 44.6 | 51.3 | 53.3 | -76.0 | -60.5 | 2.5 |
| equity-only, depreciation variant | 45.6 | 45.1 | 131.0 | 47.5 | 47.3 | 63.3 |
| after-tax cash interest added back (23%) | 13.1 | 18.6 | 25.8 | 49.7 | 51.7 | 31.8 |
| **all-equity owner cash, maintenance** | 64.5 | 69.9 | 119.5 | 58.3 | 103.0 | **83.0** |
| all-equity owner cash, all spending | 57.7 | 69.9 | 79.1 | -26.3 | -8.8 | 34.3 |

**How Q7's convention was applied.**
- *The basis.* All-equity central, owner cash before interest against market value plus net debt, since Berkshire
  says "we evaluate acquisitions on an all-equity basis" **[L2017-004]**; equity-only beside. Net debt is the filer's
  own at the latest filed date, 2026-06-30: 1,087.4M including 74.7M of contingent deal obligations (1,012.8M without
  them); no later event in the filings read changes it. Operating leases (11.2M at 2025) left out, said so.
  **CONVENTION of this run:** the interest added back is taxed at 23% (Canada's federal 15% stated in note 12 plus
  Alberta's 8%, the head office's province, a rate taken from outside the filing); rationale: the debt and its interest
  sit in Canada, and the note states only the federal part.
- *The window and (a) cycles.* 2021 to 2025. The filer describes neither end year as aberrational (2025 had record
  revenue; its Fargo write-downs are equity-method, outside operating cash), so the literal window is the base.
- *(b) Decline.* None: the maintenance series rises (all-equity 64.5 to 103.0) or is flat (equity-only 51.4 to 51.3).
- *(c) Acquisitions and the serial acquirer.* Net purchases over the window, 159.5M, exceed half of owner cash before
  purchases (128.1M of 256.3M, maintenance case), so **the central figure is the organic pair**: purchases left out,
  organic growth as the filer reports it. **The filer reports no organic growth of owner cash or earnings** (it gives
  some figures "excluding IMC" for one quarter only). **CONVENTION of this run:** organic growth is carried at nil, so
  the central range is **the no-growth case alone, said so**; rationale: the rule credits only organic growth the filer
  reports, and none is reported. The default pair (purchases deducted, total growth credited) is shown beside. IMC
  closed after the window: its financing is in the June net debt and its earnings are credited at nothing, since no
  annual record of it is filed.
- *(d) Working capital* is inside operating cash flow. *(e) Maintenance central:* the filer's own sustaining split is
  the maintenance guess, of which "the shareholders are entitled to my best guess" **[M2000-144]**; the growth case
  charges the growth capital (48.7M a year) against the growth it buys. *(f) The cap:* the default pair's shown rate
  (12.4% a year, all-equity maintenance owner cash before purchases, 2021 to 2025) carried ten years gives 266.6M in
  year ten, under the highest share of sales the business has earned (12.4%, 2023) once sales grow at their own 18.4% a
  year, so no cut; the rate exceeds 4.19% only inside the ten years. After year ten, zero growth, and purchases and
  growth capital stop.
- *The floor first.* The return implied at the price on the central basis is **5.45%** (all-equity, organic pair,
  no-growth); on the default pair's growth case 9.79%. **No case on the central basis earns about ten percent at the
  price**: "there’s just a point at which we drop out of the game" **[M2003-149]**. The equity-only no-growth case implies 11.74%; it never decides alone. Had the file
  reached Q7 it would have closed OUT on the floor; the default pair's width is 4.2 to 1.

**(a) THE VALUE RANGE** (CAD a share, against **CAD 16.27**):
- **Central, all-equity, organic pair: CAD 33.33**, the no-growth case alone (1,981.6M at 4.19%, less net debt of
  1,087.4M, over 26.829M shares).
- Beside: default pair, all-equity, **33.33 to 141.61**; equity-only, organic pair, **45.60**; equity-only, default
  pair, 21.27 to 45.60 (inverted: on the equity-only series, which did not grow, the purchases and growth capital are
  worth less than they cost); all-spending case, all-equity, **-10.01** (34.3M a year at 4.19% is below net debt).

**(b) THE FAIR PRICE** (each end case valued at ten percent, the two averaged; owner cash after the company's own tax,
no conversion):
- **Central, all-equity, organic pair: CAD -9.58.** At ten percent the business is worth 830.3M, less than its net debt
  of 1,087.4M; no positive share price earns the floor on this basis. With the December 2025 net debt (878.5M, before
  IMC and the June notes) it would still be -1.80.
- Beside: **equity-only, organic pair: CAD 19.11**; default pair, all-equity, 2.45 (ends -9.58 and 14.48); default pair,
  equity-only, 9.84 (ends 19.11 and 0.58).
- Which is which: the central figure is the all-equity organic pair (-9.58); the equity-only figure (19.11) is shown
  beside and never decides alone. Neither figure is a verdict or entry language (operator rule 3). Because the central
  fair price is not positive, any alert the fold sets would need its basis named.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 497b28f8); written question by question; committed after Step 0
      and Q1 (f4bbea15), after Q2 (442e15db), and at the close.
- [ ] If dispatched: the brief allowed the per-question commits (it did); the lock and the fold are the dispatching
      session's to tick (operator rule ten). A run not in the register binds nothing.
- [ ] The blind rule: **not fully kept.** I listed `Test Runs/` filtered to today's date to check for my own file, which
      the rule counts as a listing; twelve other run file names were seen and are declared under contamination, none
      opened, none about NOA. No other run file, holding review, `PORTFOLIO.md`, register or reading list was opened or
      searched.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in its row (checked by
      `check_run.py` in the research folder); every filing fact carries its accession; numbers carry a filing or a
      CONVENTION label.
- [x] The order was kept; Q2 closed the run; everything after it is a fact recorded or a COMPUTATION, not a clearance.
- [x] Owner cash from operating cash flow less stock pay less capital, never a net-income proxy; the sovereign from the
      Bank of Canada, named and dated (the protocol's table lacks CAD, said so); the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found, in the foundations; facts for later questions are under AFTER THE STOP,
      and the integrity flag is in the box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used; its owner-cash window (2013 to 2015) was not used.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **The serial-acquirer rule with no reported organic growth.** The rule makes the organic pair central
and credits "organic growth as the filer reports it"; NOA reports none, so the central range collapses to a single
no-growth point and the fair price to one case. I carried organic growth at nil as a confessed CONVENTION; the text does
not say whether a missing organic figure means nil, a proxy (revenue growth in years with no deal, say), or that the
default pair then becomes central. The choice moves the central fair price from -9.58 to 2.45. (2) **The parts rule's
measure.** "Five-year operating profit" for a filer whose segment measure is gross profit, and whose segment note did
not exist for the window's first year (2021): I used segment gross profit and showed that which part is largest does
not depend on the missing year, though whether Canada passes half does; the text could say which measure stands in when
no segment operating profit is reported. (3) **A negative fair price.** Where the business earns less on its assets than
its debt costs, the all-equity fair price can be below zero while the equity-only figure sits above the price (here
-9.58 against 19.11); the framework rightly makes the all-equity figure central, but does not say how a negative fair
price is reported or alerted. (4) **The protocol's sovereign table has no CAD row**, and `tools/sources.py` has no CAD
source; the Bank of Canada long benchmark was taken by hand. A CAD row naming the series would make the next Canadian
run the same as this one.
