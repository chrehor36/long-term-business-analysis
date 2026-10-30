# Company Run — Sunbelt Rentals Holdings, Inc. (NYSE: SUNB; operator's list: ASHTY, the former Ashtead Group plc ADR) — 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. The dispatching session fills it at the fold. *Filled by the dispatching session at the fold, 2026-10-12, after the run was committed: not held (`PORTFOLIO.md` does not name Sunbelt, Ashtead, SUNB or ASHTY).*

**Dispatched blind run.** Analyst dispatched under the canonical brief `Screens/_daily/_dispatch_brief.md`, with the one stated departure (the lines of evidence are derived by the analyst from the 10-K, listed below). Working folder `Test Runs/_research 2026-10-12 SUNB/`.

**CONTAMINATION, declared:** before any fetch I listed `Test Runs/` filtered for "SUNB|ASHT|sunbelt|ashtead" to confirm the run file name was free; the filter returned nothing. The repository's recent commit subjects shown to me at session start name another company's run and fold (ADRZY); nothing about this company. The session's memory index lines (not opened beyond the index) state counts of gate-clearers and a queue position, and name no company relevant here. Nothing of the blind-listed files was opened, listed or searched. Nothing seen is used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $75.17 (NYSE close 2026-10-09, the last close before this run; Yahoo Finance chart API through `tools/sources.py` `price()`, **an aggregator, flagged, used for the live quote only** under operator rule 5). The fifty-two-week range the same feed prints is $61.03 to $86.68 (aggregator; context only; the NYSE line begins 2026-03-02).
- **Shares by class:** one class, common stock $0.01 par, **409,764,897** shares outstanding on the cover of the 10-Q for the quarter ended 2026-07-31 (filed 2026-09-09, accession `0001628280-26-061146`; `python Screens/cover_shares.py SUNB`). Checked against the 10-Q balance sheet: 414,502,814 issued less 4,635,333 treasury = 409,867,481 at 2026-07-31; the cover count is later and lower by about 0.1 million, consistent with the weekly buybacks the company reports. No 8-K or prospectus after the 10-Q changes the count (the 8-Ks of 2026-09-02 and 2026-09-09 read; no issuance). Charter: 2,500,000,000 common and 25,000,000 preferred authorised, no preferred issued (10-Q Note 12). Equity awards outstanding 2,978,581 (10-Q Note 13), about 0.7% of the count, not added.
- **Market cap:** 409.765M x $75.17 = **$30,802M**.
- **Sovereign for the earnings currency:** the business reports and earns mainly in USD (15% of FY2026 revenue from GBP and CAD subsidiaries, 10-K Item 7, Currency Translation Exposure). **USD 30-year 5.60%, US Treasury daily par yield curve, 10/09/2026** (`python tools/sources.py`, issuing authority). No GBP figure enters the valuation: Ashtead reported in USD from FY2022, and its own ten-year history restates FY2013 to FY2021 in USD (AR2022, page 168); the GBP ten-year history (AR2021, page 168) is read for context only.
- **Filings read** (operator rule 4):
  - 10-K for FY ended 2026-04-30, filed 2026-06-23, accession `0001628280-26-044888` (Items 1, 1A, 7, 7A, 8, 9A read).
  - 10-Q for the quarter ended 2026-07-31, filed 2026-09-09, accession `0001628280-26-061146` (statements, Notes 12, 13, 15, Item 2 repurchases).
  - 10-Q for the quarter ended 2026-01-31, filed 2026-03-12, accession `0001628280-26-017215` (fetched; consulted for the restated half-year).
  - DEF 14A filed 2026-07-21, accession `0001193125-26-310387` (read at Q5 and Q6).
  - Form 10 amendment (10-12B/A) filed 2026-02-13, accession `0001193125-26-050612`: Ashtead Group plc US-GAAP statements FY2023 to FY2025 (balance sheets 2023 to 2025, cash flows FY2023 to FY2025).
  - 8-Ks: 2026-03-02 (`0001193125-26-085376`, completion of the Scheme, auditor change, material weakness), 2026-06-23 (`0001628280-26-044797`), 2026-06-30 (`0001193125-26-290643`), 2026-07-08 (`0001193125-26-297740`), 2026-07-13 (`0001193125-26-302070`), 2026-07-15 (`0001193125-26-303702`, $450M 4.950% notes due 2030 and $750M 5.650% notes due 2036), 2026-09-02 (`0001193125-26-380411`), 2026-09-09 (`0001628280-26-061014`).
  - Ashtead Group plc Annual Report and Accounts 2021, 2022, 2023 and 2025 (IFRS; primary documents from the company's investor-relations site, ir.sunbeltrentals.com, "Annual reports and proxy statements"; no accession, the documents are UK filings). The ten-year histories (AR2025 page 166 printed, FY2016 to FY2025 in USD; AR2022 page 168 printed, FY2013 to FY2022 in USD) give the long series.
- **Which years come from which document, and the bridge.** FY2023 to FY2026: US GAAP (Form 10 and 10-K), USD. FY2013 to FY2022: IFRS, USD as Ashtead restated them in its own ten-year histories. IFRS 16 applies from FY2020 (no restatement of earlier years); from FY2020 to FY2022 the IFRS operating cash excludes lease principal paid, which sits in financing, so the IFRS "free cash flow" of those years is higher than a US-GAAP figure would be by about the lease principal. The two GAAPs overlap in FY2023 to FY2025 (the AR2025 history against the Form 10): IFRS free cash flow FY2025 $1,789.9M against US-GAAP free cash flow $1,675M (10-K Item 7, the company's own definition), FY2024 $216.5M against $126M; the gap is about $90M to $115M a year, which is the bridge I apply to the IFRS 16 years (FY2020 to FY2022) where a US-GAAP figure does not exist, and say so wherever it is used. The years before FY2020 are pre-IFRS 16, with lease cost inside operating costs as under US GAAP, and are taken as filed.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2026, **$3,784M** in the 10-K's Consolidated Statements of Cash Flows, equals the XBRL fact `NetCashProvidedByUsedInOperatingActivities` 3,784,000,000 for 2025-05-01 to 2026-04-30 in the same accession (SEC companyfacts, fetched 2026-10-12).
- **`python tools/run.py SUNB`** printed one line: "SUNB: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." The tool finds no tagged history (SUNB's EDGAR history begins in 2025 and the predecessor's years are not tagged under this CIK). Every figure in this run is therefore taken by hand from the filed statements named above; the owner-cash table is built at Q4 and Q7.
- **The lines of evidence, derived from the 10-K** (the brief's one departure from the canonical brief):
  1. Item 1, Overview and Market share: second largest North American rental business, estimated 11% share; largest in the UK, estimated 10%; the three largest hold about 31% of the North American market; over 40% of the US market is rental companies with five or fewer locations.
  2. Item 1, Competitive Strengths: "While the individual components of our General Tool fleet are similar to that of our peers" (the filer's own words on the product), with scale, clusters, purchasing power, service and brand claimed as the advantages.
  3. Item 1, Segments: General Tool 58%, Specialty 33%, UK 9% of FY2026 revenue; Item 7 segment table for profit.
  4. Item 1, Competition: named rivals United Rentals, Herc Rentals and EquipmentShare (North America); Speedy Hire, HSS ProService and Vp (UK).
  5. Item 1A: competition "depressing prices"; cyclicality; residual-value risk; "Our substantial debt"; the material weakness of FY2026 and its remediation.
  6. Item 7: Fleet Rotation and Depreciation ("our cash flows are countercyclical"); results by segment; dollar utilization; free cash flow and its definition; adjusted operating profit and adjusted EBITDA reconciliations; the UK goodwill not "substantially in excess" of carrying value.
  7. Item 7, Liquidity: $7,583M debt, $3,302M undrawn on the ABL; $1,413M of buybacks in FY2026.

### The balance sheets, read before the income account (Q4's rule, read here because the file closes before Q4)

"balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**. $M at 30 April. FY2017 to FY2022: IFRS, USD as Ashtead restated them (AR2022 and AR2025 ten-year histories; net debt excluding IFRS 16 lease liabilities from the AR2022 financial review, Chart 05, FY2018 to FY2022). FY2023 to FY2026: US GAAP (Form 10 balance sheets; 10-K; 10-Q for 2026-07-31). Net debt is borrowings less cash, leases left out.

| April | shareholders' equity | net debt (ex leases) | goodwill + other intangibles | receivables | revenue (year) | fleet at original cost |
|---|---|---|---|---|---|---|
| 2017 | 2,549 | n/a | n/a | n/a | 4,125 | 7,564 |
| 2018 | 3,481 | 3,736 | n/a | n/a | 4,959 | 9,047 |
| 2019 | 3,651 | 4,882 | n/a | n/a | 5,870 | 10,797 |
| 2020 | 3,749 | 5,368 | n/a | n/a | 6,399 | 11,868 |
| 2021 | 4,525 | 4,180 | n/a | n/a | 6,639 | 11,855 |
| 2022 | 5,034 | 5,179 | n/a | n/a | 7,962 | 13,539 |
| 2023 | 6,010 | 6,565 | 3,485 | 1,385 | 9,667 | 15,826 |
| 2024 | 7,060 | 7,974 | 3,806 | 1,528 | 10,859 | 17,745 |
| 2025 | 7,799 | 7,479 | 3,781 | 1,481 | 10,791 | 18,538 |
| 2026 | 7,409 | 7,554 | 3,814 | 1,669 | 11,154 | 19,231 |
| Jul 2026 | 7,447 | 8,524 | 4,161 | 1,929 | (quarter 3,115) | n/a |

(n/a: not in the documents read; the IFRS balance sheets of FY2017 to FY2022 were not extracted line by line, and the ten-year histories carry equity, fleet cost and revenue only. The FY2023 to FY2026 equity is US GAAP; IFRS shareholders' funds at April 2023 were $6,008M against $6,010M under US GAAP, so the two series join without a visible break.)

What the figures say. (1) The business is its fleet and its debt: fleet cost rose 2.5 times in nine years, net debt rose 2.3 times from April 2018 to July 2026, and equity 2.9 times from April 2017; net debt has run between 0.9 and 1.4 times equity (highest at April 2020), and 1.4 times EBITDA (FY2021) and 1.5 times (FY2022) by the filer's own measure, about 1.7 times at April 2026 and 1.9 times at July 2026 by my arithmetic on US-GAAP EBITDA. (2) Goodwill and intangibles ($3.8B, $4.2B after the July acquisitions) are half of equity: tangible equity is about $3.6B against $8.5B of net debt and $2.9B of operating leases. (3) Receivables kept pace with revenue until FY2026 (14% to 15% of revenue), then rose 13% in a year of 3% revenue growth, and 16% more in the following quarter (seasonal in part; the provision charge rose from $28M to $64M). (4) Retained earnings fell $1,457M in FY2026 because $2,319M of treasury shares was cancelled at the Redomiciliation; buybacks were $342M (FY2025) and $1,413M (FY2026), paid from the harvest years' free cash flow after dividends and acquisitions ($984M and $1,401M) with the balance borrowed. (5) Deferred tax liabilities ($2.4B) grow with the fleet: tax is deferred, not avoided. (6) The fleet's net book value has been flat at about $11.2B to $11.5B since April 2024 while its original cost rose and its average age went from 49 to 53 months (10-K Item 1): the FY2026 cash came partly from not replacing.

What they do not say and cannot say: the rental rates inside the revenue, the used-equipment values at which the fleet could be sold in a downturn, and how much of the fleet's book value is above what the market would pay for it; these are the questions of Q2 and Q9.

## THE FOUNDATIONS (not a gate)
Three foundations bear on this name. **A share is a business:** the test is whether I would be content to own it "if the market closed for five years" **[M1997-109]**; the business is a capital-heavy, cyclical renter of machines whose owners are paid by the cash the fleet throws off after the fleet is replaced, so the question is the business's cash through a cycle, not the quotation that began on 2026-03-02. **No macro enters:** the 10-K leans on forecasts of rental-industry growth (S&P Global, 4% a year 2026 to 2028) and on the "mega project" pipeline (Dodge, $1.5 trillion 2026 to 2028); those are other people's projections and are not used here; what counts is "the average profitability of the business over time and how strong its competitive mode is" (the transcript's word) **[M2015-016]**. **The market serves, it does not instruct:** the price is read as a price, "It just tells us prices." **[M2006-077]**, and the margin of safety is an arithmetic only at Q7 **[M1996-084]**. The analyst's habit applied: look for "what’s wrong" and "what you’re missing" **[M2025-013]**.

**Contrary evidence, written down as found** **[M1997-127]**:
- The filer's own words on its largest part: "While the individual components of our General Tool fleet are similar to that of our peers" (10-K Item 1). The product is not differentiated; any advantage must be scale, cost or service.
- One of the three "largest national competitors" the 10-K names, EquipmentShare, is a business founded within the last cycle (checked at Q2). If a newcomer with money became a top-three national rival inside ten years, the money test fails on the record.
- FY2026: revenue +3%, operating income -13% ($2,499M to $2,181M), General Tool segment profit -8%, General Tool dollar utilization 51% (FY2024) to 48% to 47% (10-K Item 7).
- A material weakness was found in FY2026 (a $550M note classified non-current when it was current; the Form 10 half-year restated) and declared remediated at 2026-04-30 (10-K Item 1A and Item 9A). A second correction is in the stock-pay note ("We have revised the weighted-average fair value of awards outstanding as of April 30, 2025 from $44.41 to $60.97 to correct the amount previously" reported, 10-K Note on stock-based compensation).
- The company gives earnings guidance and features adjusted operating profit and adjusted EBITDA (the 10-Q press release headline, read only as a headline on the IR site: "raises full-year fiscal 2027 guidance"; the 10-K's own risk factor names "our failure to meet our stated guidance").
- Free cash flow (the company's definition, before acquisitions) was $126M in FY2024 against net income of $1,572M; the cash the owner keeps swings with the fleet cycle by more than tenfold.

## THE STANDING RULE
The rule binds the buyer's conduct. A purchase of SUNB shares paid in cash, with no borrowed money and no position that can call for cash, risks only what is paid; borrowed money to own the stock is ruled out **[L2014-005]**, and "You never get in a position, obviously, where the other fellow can call your tune." **[M2006-079]**. The target's own $8.6B of debt is the target's exposure and is weighed at Q9, not here. **Not engaged** on a cash purchase of a size whose loss would not touch what the buyer has and needs **[M2012-081]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**; the chemistry may stay opaque if "I understand the economic dynamics of the industry" **[M2011-014]**.

**What the business is (10-K Item 1).** It buys standard machines (aerial work platforms 39% of General Tool fleet cost, forklifts 25%, earth moving 17%; power and HVAC 43% of Specialty fleet cost), rents them for days to months to about 800,000 US customers (none above 1% of revenue, top ten below 10%), maintains them, and sells them used after roughly the life the depreciation policy assumes (salvage 10% to 15% of cost for most types, Item 7, Critical Accounting Policies). 93% of FY2026 revenue was rental. The parts (Q2's paragraph on a business of parts, applied here to Q1 as the framework extends it): General Tool decides (more than half of segment profit in every year shown, see Q2), Specialty is the second part; both are the same economic activity on different machines.

**The key variables** **[M1998-044]**: (1) the original cost of the fleet on rent, which grows by capital spending and bolt-on purchases; (2) dollar utilization, the rental revenue a dollar of fleet earns, which carries both rate and time on rent (General Tool 51%, 48%, 47% in FY2024 to FY2026; Specialty 74%, 73%, 75%); (3) the cost of new machines and the price of used ones (the life-cycle inflation the 10-K names in depreciation); (4) the construction and industrial cycle, which the company says moves its demand "in line with GDP growth" and down in a downturn (Item 1A). The first three are read from thirteen years of filed history; the fourth is a cycle, not a technology, and its effect on this business is on the record (FY2021, the pandemic year: revenue about flat, $6,398.9M to $6,638.6M in the USD restatement and £5,053.6M to £5,031.1M as reported in GBP, while capital spending was cut from $1,877.8M to $947.4M; AR2022 and AR2021 ten-year histories).

**Do the past statements tell me the future ones?** **[M2008-033]** Largely yes for the shape of the business: the same machines rented to the same kind of customer, with the same ratio of rental to fleet, show in every year from FY2013 to FY2026. The products change slowly (electrification of small equipment, telematics); I find nothing in Item 1 or 1A that makes the ten-year economics a technology forecast. The 10-K's own technology risk ("We may fail to respond adequately to changes in technology and customer demands") is about software and ordering, not about whether customers will rent machines.

**Would the insiders write it down?** **[M2000-105]** Yes in outline: the company and its two listed rivals publish multi-year plans (Sunbelt 4.0 to 2029, its 300 to 400 greenfield stores) and the industry's rental-penetration figures. I do not use their forecasts (foundations), but the question is whether the forecast is of a kind insiders would write; it is.

**How far off could I be?** **[M2011-084]** Narrow on what the business does in ten years (rents the same classes of machine, more of them, at a penetration that has risen for decades); wide on what it earns in any one year, because the cycle moves utilization, used-equipment prices and the capital spending that decides the owner's cash. That width belongs to Q2 (does the castle protect returns through the cycle) and Q7 (the range); it does not put the economics outside the perimeter. "If something’s important but unknowable, forget it." **[M2006-076]**: the cycle's timing is unknowable but not decisive for a holder; its depth is read from the record.

**Doubt.** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]** I have no doubt that I can say where this business will be in ten years in kind; I have real doubt about the size of its castle, which is the next question, not this one. The UK part (9% of revenue, under 2% of segment profit) does not decide and is not needed to understand the whole.

- **VERDICT: IN.** The business renting standard machines is understood in its economics; its ten-year shape is foreseeable and is not a technology forecast **[M2012-065]**, **[M2011-014]**. Filing fact: 10-K FY2026 Item 1 (fleet composition, customers, segments) and Item 7 (dollar utilization, OEC), accession `0001628280-26-044888`; AR2022 and AR2025 ten-year histories.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years from now." **[M1995-038]**. A moat is what "protects excellent returns on invested capital" **[L2007-004]**.

### The parts table (section B of Q2: "lumping them together [...] impedes analysis" **[L2008-005]**)

Adjusted segment operating profit, 10-K FY2026 Item 7 segment table (`0001628280-26-044888`); the segments were first reported this way for FY2024, so three years are shown, not five.

| Part | FY2024 | FY2025 | FY2026 | share of the three years | castle (below) | decides? |
|---|---|---|---|---|---|---|
| North America, General Tool | $2,394M | $2,093M | $1,932M | 65% (70%, 63%, 61%) | shared scale and density in an undifferentiated product | **yes, more than half** |
| North America, Specialty | $964M | $1,138M | $1,176M | 33% | narrower fields, more technical, low rental penetration (segment RoI excluding goodwill 30% in FY2025) | no |
| United Kingdom | $53M | $73M | $59M | 2% | "more mature, competitive and fragmented" (10-K Item 1); segment RoI 7% (FY2025) | no |

For the two earlier years of a five-year window (FY2022, FY2023) the filer reported US, Canada and UK, not these parts; General Tool would need under about 30% of profit in those two years for its five-year share to fall below half, which its 70% share in FY2024 makes implausible. **General Tool decides.** Specialty, the better part, does not decide; the UK, an ordinary part, would be carried to Q7 at no growth.

### The castle tests, on General Tool

1. **What keeps it standing, and how permanent?** **[M1995-038]** The filer names geographic scale and clusters, breadth of fleet, purchasing power, service and brand (10-K Item 1, Competitive Strengths). The product is not among them: "While the individual components of our General Tool fleet are similar to that of our peers". The key factor is scale and density against the small independents (over 40% of the US market is firms with five or fewer locations, 10-K Item 1). It is permanent against them; it is shared with United Rentals, which is larger (about 15% North American share against Sunbelt's 11%; URI 10-K FY2025, `0001067701-26-000007`).
2. **Would it stand without the lord?** Yes. The business is decentralized (10-K Item 1, "Motivated local management teams"); nothing in the filings makes the returns depend on one person.
3. **The money test.** **[M2011-015]** Failed in volume, on the record. EquipmentShare, which reports "rapid growth since our inception in 2015" (EQPT 10-K FY2025, accession `0001628280-26-019656`), built a fleet with an original cost of $8.8 billion and revenue of $4,379M by 2025, and Sunbelt's own 10-K names it among its three largest national competitors. It did so at thin returns: operating income $297M (6.8% of revenue) against $285M of interest, pre-tax income $54M, about 8% pre-tax on its capital in 2024 and 2025. The row that fits is the airline exchange: "and you can create another airline." / "Very easily, and you have people that like to do it." **[M2013-054]**. The entrant has not taken the incumbents' returns so far; it shows that money can build a national rival in ten years and is content to own it at poor returns, the condition the speakers dislike, and "one competitor is frequently enough to ruin a business." **[M2012-108]**.
4. **Pricing power, the agony before a rise.** **[M2005-020]** Through the last deep downturn the field's price broke: United Rentals' 2009 equipment rentals fell 26.7%, reflecting "an 11.8 percent decrease in rental rates and a 12.4 percent decrease in the volume of OEC on rent", and rates fell another 2.1% in 2010 (URI 10-K FY2010, `0001193125-11-020326`); Ashtead's revenue fell 22% from FY2009 to FY2010 and its pre-tax profit before exceptionals went from £87.4M to £5.0M (AR2012 ten-year history). In the one volume-falling year since, FY2021, Sunbelt's US dollar utilization went from 51% to 50% and its US rental-only revenue fell 2% (AR2021 financial review), while United Rentals' 2020 "Fleet productivity decreased 6.9 percent" (rates, time and mix together; URI 10-K FY2020, `0001067701-21-000008`). Today the filer's own risk factor says competitive pressures have in the past adversely affected its results by "depressing prices that we can charge" (10-K Item 1A), and General Tool dollar utilization has fallen from 51% to 48% to 47% over FY2024 to FY2026 while the filer reports US industry rental revenue growth of 8% and 4% in calendar 2024 and 2025 (10-K Item 1, citing S&P Global).
5. **Unit volume.** Rising for decades: stores 485 (FY2012) to 1,611 (FY2026); book cost of the rental fleet $2.9B (FY2013) to $18.5B (FY2025); North American rental penetration "around 55% to 60%" and rising (10-K Item 1). Volume is the best evidence for the business; most of it was bought with capital, which is Q3's question.
6. **The low-cost position.** **[L2004-007]**, **[M1997-010]** Sunbelt is one of two scale operators whose costs sit far below the independents and below the funded entrant (EBIT margin FY2026 19.6%, 22.4% on the filer's adjusted operating profit; EquipmentShare 6.8%; Herc 15.4% in 2024 and 9.5% in 2025, the H&E deal year). It is not the low-cost producer of the field: United Rentals earned a 24.7% operating margin in 2025 and 23% to 28% in every year 2018 to 2025. The exception the rows grant is to "the low-cost operator" **[L2004-007]**; here two operators share the low end, and "you can have only two competitors and they’re still terrible businesses, they beat each other’s brains out." **[M2013-052]**. The record says these two have not done that since 2011; it also says the field did in 2009.
7. **The brand.** Claimed (10-K Item 1, "Well-established brand"); no filing fact shows customers asking for Sunbelt by name or paying more for it.
8. **Would the customer still choose it over the low bid?** **[M2017-009]** The field's answer, in the funded entrant's own risk factor: "We believe that price is an important competitive factor in the construction equipment rental industry. The availability of information on the internet has enabled consumers to more easily compare the rates and services offered by different rental companies." (EQPT 10-K FY2025, Item 1A). For General Tool's contractors the evidence is that the low bid matters; for Specialty and the mega projects, service and breadth matter more (10-K Item 1), but Specialty does not decide.
9. **Ask the competitors.** **[M2025-043]** Their filings say where they think the field competes: on price (EquipmentShare), and against the small independents (United Rentals: "Our competitors primarily include small, independent businesses with one or two rental locations"; Herc: "very few national competitors"). None says the national players are safe from each other.
10. **Widening or narrowing?** **[L2005-010]**, **[M1999-108]** Over thirteen years, widening against the independents (share and stores up, returns up). Over the last two years, narrowing in the deciding part: General Tool adjusted segment profit -19% ($2,394M to $1,932M) on equipment-rental revenue +3% ($5,826M to $6,013M), staff costs +8% in FY2026, dollar utilization down four points; the filer attributes it to costs, fleet repositioning and a weaker local commercial construction market (10-K Item 7). Two years cannot separate a cycle from a notch.
11. **What could destroy, modify or reduce it, five to fifteen years out?** **[M2000-014]** A construction-led downturn with surplus fleet in the hands of two scale players and a funded entrant, which is what broke the price in 2009; and the entrant itself, whose fleet ($8.8B original cost) is already about half the size of Sunbelt's ($19.2B).

### The competitor row (same measures, from the rivals' own filings; `q2_field_returns.txt` in the research folder)

Return = operating income (or pre-tax income plus interest where operating income is not tagged) on debt plus equity less cash at year end, pre-tax, goodwill included. CONVENTION of this run: the filer's own RoI is defined differently and the rivals publish none; one plain measure lets the four be compared from their filings.

| Company (filing) | metric | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| United Rentals (10-K XBRL, CIK 1067701) | EBIT margin | 24.2% | 23.0% | 21.1% | 23.4% | 27.8% | 26.7% | 26.5% | 24.7% |
| | pre-tax return on capital | 12.8% | 14.1% | 12.8% | 14.6% | 17.6% | 19.8% | 18.8% | 17.4% |
| Herc (10-K XBRL and FY2025 10-K text, CIK 1364479) | EBIT margin | 10.4% | 11.9% | 10.5% | 18.2% | 20.3% | 20.4% | 15.4% | 9.5% |
| | pre-tax return on capital | 7.7% | 8.9% | 7.9% | 13.2% | 14.0% | 13.8% | 10.2% | 4.2% |
| EquipmentShare (10-K XBRL, CIK 1693736) | EBIT margin | | | | | | 9.8% | 5.8% | 6.8% |
| | pre-tax return on capital | | | | | | | 8.1% | 8.5% |
| Sunbelt/Ashtead (filer's RoI; the column year is the fiscal year ending in April of that year) | RoI, pre-tax | 17.6% | 17.8% | 15.2% | 14.9% | 18.2% | 19.2% | 16.3% | 14.5% |

Sunbelt on the rivals' basis, US GAAP, FY2026: 14.4% (16.5% on adjusted operating profit). United Rentals 2010 to 2017: EBIT margin 8.8% in 2010, then 14% to 26%; return on capital 6.8% (2012, the RSC merger year) to 16.0%. The named UK rivals, Speedy Hire, HSS ProService and Vp, do not file with the SEC and are not compared (flagged as the brief asks).

### The field's returns over the last full cycle (section C)

The filer's record runs through two downturns. **The last deep, construction-led cycle** (Ashtead FY2003 to FY2011, trough to trough): RoI 4.9%, 6.9%, 11.0%, 14.7%, 12.9%, 14.0%, 9.7%, 4.6%, 7.0%, an average near 9.5% pre-tax and 4.6% at the trough (AR2012 ten-year history); United Rentals' rental rates fell 11.8% and 2.1% in 2009 and 2010, and it reported a net loss of $26M and an 8.8% operating margin in 2010. In words: over that full cycle the field earned ordinary returns at best, and its price did not hold. **Since FY2011** the filer's RoI has run 14.5% to 19.4% and United Rentals' return on capital 12% to 20%: the field changed for the better, with the consolidation and the rising rental share of equipment use the filings describe. **The one volume-falling year since** (FY2021 for Sunbelt, calendar 2020 for the field) was a short pandemic shock: Sunbelt's price held (US dollar utilization 51% to 50%, RoI 15.2% to 14.9%), United Rentals' fleet productivity fell 6.9%, Herc's return was 7.9%. It was not a construction downturn of the kind that broke the price in 2009, and the field's own price evidence in it is mixed.

The framework credits a change for the better "only on the evidence of a full cycle in which the price behaviour held" (Q2, Change, and what it does to a castle; the CONVENTION of 2026-10-06 as amended 2026-10-10), built on **[M2005-020]** and **[L1995-022]**; the speakers record that such changes happen, "the railroads were a terrible business for decades and decades and decades and then they got good." **[M2017-026]**, and give no span. Here the only full construction cycle on record shows ordinary returns and a broken price; the improvement has met one short shock in which the filer's price held and the field's evidence is mixed. I do not credit it on that evidence.

### Why the verdict is TOO HARD, and which cause

- **Not OUT.** A castle shown open on the evidence closes OUT; the evidence does not show it open. The scale position against the independents has widened for thirteen years; the entrant has taken volume but not the incumbents' returns; the two-year fall in General Tool's profit may be the cycle the filer describes. And an OUT for ordinary returns needs those returns on the current evidence, which the change for the better contests.
- **Not IN.** The castle's work is to protect returns through the downturn. In the deciding part the product is undifferentiated by the filer's own words, price is the competitive factor by a rival's own words, a funded entrant crossed the moat in volume within ten years, the number two is not the low-cost producer, and the last deep downturn took the rate down 11.8% in a year. "when we see a moat that’s tenuous in any way [...] it’s just too risky. We don’t know how to valuate that, and therefore we leave it alone." **[M2000-019]**; "If we can think of very much that can go wrong with them, we just forget it." **[M2000-016]**.
- **Cause: NATURE.** The deciding question is how rental rates and returns behave in the next construction-led downturn with two scale incumbents and a funded entrant holding fleet. It is a forecast the industry's insiders do not write down (none of the four filers gives one; each lists price competition as a risk), and no filing now available answers it: "We couldn't solve this problem, moreover, even if we were to spend years intensely studying those industries." **[L1993-023]**. Only the downturn answers it, which is why the framework sends an uncredited change for the better to TOO HARD (NATURE) and not to a research pass.
- **Dated re-look condition (the convention's words):** the first fiscal year in which the business's volume or its field's volume falls, read from the filings, after which the question is put again. Read here as: the first fiscal year after FY2026 in which Sunbelt's North American equipment-rental revenue at constant currency, or United Rentals' or the industry's North American rental revenue, falls; the question is then put again on that year's rate and return evidence. FY2021 met the literal trigger before this run; it is weighed above and found inconclusive (see "What in the framework was wrong or unclear").

- **VERDICT: TOO HARD (NATURE).** General Tool, the deciding part, holds a shared scale position in an undifferentiated, price-led field whose returns were ordinary through the last full construction cycle; the better returns since FY2011 are not yet credited on a full cycle in which the field's price held **[M2005-020]**, **[L1995-022]**; a moat this tenuous cannot be valued **[M2000-019]**; the deciding question is answered only by the next downturn **[L1993-023]**, **[M2006-013]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED.** The file closed at Q2 (TOO HARD, NATURE). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** The balance sheets were read in Step 0's last subsection, as the template asks when the file closes before Q4; facts on the accounts are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.** Integrity facts found are recorded under AFTER THE STOP, not judged; the box line carries the flag.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** Facts under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED as a question.** The figures below are the operator's two reporting figures (Part VII, The owner's price), computed after the STOP.

### COMPUTATION, NOT A CLEARANCE

Script and output: `q7_computation.py` and `q7_computation_output.txt` in the research folder. All $M unless a per-share figure. Discount rate 5.60% (UST 30-year, 10/09/2026); fair price at 10%.

**The window and its sources.** FY2022 (IFRS, AR2022) to FY2026 (US GAAP, 10-K). FY2022 is bridged to US GAAP by deducting the IFRS 16 lease principal ($107.6M, financing in IFRS) from free cash flow, by taking the lease interest ($80.7M) out of the interest added back, and, for the maintenance series, by deducting the lease interest from IFRS operating profit and the right-of-use depreciation ($154.1M) from IFRS depreciation (AR2022, cash flow statement, Note 6, Note 14).

**Owner cash, all spending deducted (the PG specific), literal window:**

| | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | average |
|---|---|---|---|---|---|---|
| free cash flow as filed (company definition; FY2022 Ashtead's) | 1,125 | 441 | 126 | 1,675 | 2,055 | |
| less lease principal (FY2022), stock pay (cash-flow add-back), finance-lease principal, intangibles and other investing | 970 | 328 | -22 | 1,651 | 1,951 | 976 |
| less acquisitions and contingent consideration, net of disposals | -308 | -755 | -898 | 1,504 | 1,761 | 261 |
| all-equity (plus debt interest paid after the company's tax) | -168 | -572 | -604 | 1,816 | 2,032 | 501 |

The series changes sign, so by specific (b) the growth is measured between the halves of the window, which is also meaningless here (negative first half), and this series gives the no-growth case alone: $501M a year all-equity, worth $8,943M at 5.60%, **$0.17 a share** after net debt. Beside it, before acquisitions (the organic pair; the filer reports no organic growth rate for the whole): $1,215M a year, **$31.31 a share** at no growth.

**The central case, maintenance only (specific e).** The filing allows the maintenance guess two ways: the depreciation charge, which **[M1998-127]** calls "not inappropriate in most companies to use as a proxy for required capital expenditures", and the filer's own statement: "Our current rental fleet has an original equipment cost of c. $19bn with a seven- to eight-year replacement cycle. Thus, on average, we replace $2.4bn per year (using eight years)" (AR2025, climate-related disclosures, printed page 71); less used-equipment proceeds of $0.42B to $0.83B a year (FY2022 to FY2026 cash flows), that is $1.6B to $2.0B of net rental replacement, against a rental depreciation charge of $1,851M in FY2026. I take depreciation as the maintenance proxy, since depreciation charges "are almost always true costs" **[L2015-004]**, and say that it is low: the fleet is depreciated at historical cost while the 10-K names life-cycle inflation in its fleet costs, so a shortfall exists that I do not quantify. Maintenance-only owner cash = (operating income + amortization of acquired intangibles) x (1 - the company's own tax rate that year); stock pay and the FY2026 restructuring costs ($134M, which the filer calls non-recurring) stay in as real costs.

| | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | average |
|---|---|---|---|---|---|---|
| maintenance-only owner cash, all-equity (M) | 1,482 | 1,912 | 1,976 | 1,960 | 1,688 | **1,804** |
| growth spending G = net capital spending above depreciation + acquisitions + working-capital increase | 1,877 | 2,662 | 2,688 | 170 | -218 | **1,436** |
| equity-only (M less debt interest after tax) | 1,342 | 1,730 | 1,682 | 1,648 | 1,417 | 1,564 |

Growth shown in M: 3.31% a year, FY2022 to FY2026 end to end (2.43% between the halves); revenue grew 8.79% a year over the same span, most of it bought (G averaged $1,436M a year, $7.2B over five years, against an increase in M of $206M). By specific (e) the growth spending is charged against the growth it buys; the growth bought here is worth less than its cost, so **the no-growth maintenance-only case is the top of the range and the growth case the bottom**, the inversion the convention names: "growth can destroy value" **[L2000-023]**. (f) The cap: 3.31% is below the discount rate and implies no share of sales above anything the filings show; no cut. (a) The cycle base: no end year of the window is called aberrational by the filer; the FY2026 harvest of cash (capital spending cut, fleet age 49 to 53 months) is the countercyclical pattern the filer describes as normal, and it is inside the all-spending series, not the maintenance series; the literal window stands. (c) Deals: the $667M of acquisitions paid in the quarter to 2026-07-31 and the $56M closed after it are in today's net debt and credited at nothing (no filed earnings). The UK part (2% of segment profit) is inside M at no extra growth; separating it moves nothing material.

**Net debt (all-equity basis).** Debt at 2026-07-31 $8,556M (10-Q balance sheet: $550M current plus $8,006M long-term) + finance-lease liabilities $171M (latest stated, 2026-04-30, 10-K XBRL; not restated in the 10-Q) - cash $32M + acquisitions closed after the quarter $56M + the dividend declared 2026-09-09 ($0.30 x 409.76M = $123M) = **$8,874M**. Operating leases ($2,867M at 2026-07-31) are left out, as the convention says, and said so. The $550M notes repaid on 2026-08-12 were refinanced inside the July issues and do not change net debt.

**(a) THE VALUE RANGE (a reporting figure; COMPUTATION):**
- **All-equity, central: $49.42 to $56.94 a share** (whole-business value $29,124M to $32,207M less $8,874M), against **$75.17**. Bottom = the growth case (M grown at 3.31% for ten years with growth spending of $1,436M a year charged, then flat with the spending stopped); top = the maintenance-only no-growth case.
- Equity-only beside: $57.48 to $68.14 a share (owner cash after interest; it is higher because the after-tax cost of the debt, about 4%, is below the 5.60% rate; it does not decide).
- The literal all-spending window beside: $0.17 a share (acquisitions deducted, no-growth alone by specific b); $31.31 (before acquisitions).
- Width: top over bottom 1.15, far inside three to one.

**The floor, tested first:** at $75.17 (whole-business value at the price $39,676M) the expected return is 4.55% on the no-growth case, 4.46% on the growth case, and 5.89% even if the shown growth is credited with no growth spending charged at all. **No case earns about ten percent** **[M2003-149]**; had Q7 been reached it would have closed OUT on price, and the price is above the top of every central range.

**(b) THE FAIR PRICE (a reporting figure, never a verdict; Part VII; COMPUTATION):** each end case valued at ten percent, the two averaged, after the company's own tax:
- **All-equity, central: $15.33 a share** (no-growth end $22.36, growth end $8.30, each after $8,874M of net debt).
- **Equity-only beside: $30.39 a share** (no-growth end $38.16, growth end $22.62).

The tax treatment: the company's own book tax rate each year (25.0% to 26.4%); cash taxes have run lower (FY2026 $332M paid against a $476M provision) because of accelerated tax depreciation on a growing fleet, a deferral that lasts while the fleet grows; no carryforward or credit runs out inside ten years that I found, so no shelter is priced separately.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** (Nothing found in the filings that touches the named businesses.)

---
## THE BOX
**TOO HARD (NATURE), decided at Q2**: General Tool, the deciding part, holds a shared scale position in an undifferentiated, price-led field whose returns were ordinary through the last full construction cycle; the better returns since FY2011 are not credited until a full cycle in which the field's price holds. **Re-look condition:** the first fiscal year in which the business's volume or its field's volume falls, read from the filings (here: the first fiscal year after FY2026 in which Sunbelt's North American equipment-rental revenue at constant currency, or United Rentals' or the industry's North American rental revenue, falls), after which Q2 is put again. **Integrity facts recorded, not judged** (see AFTER THE STOP, Q5 and Q6). For the operator, COMPUTATION, NOT A CLEARANCE: value range $49.42 to $56.94 a share (all-equity; equity-only $57.48 to $68.14) against $75.17; fair price $15.33 (equity-only $30.39); no case earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; the box unchanged (operator rule 2).

**Q3 (capital).**
- Capital spending on the fleet: rental additions $3,624M (FY2024), $1,946M (FY2025), $2,023M (FY2026); total additions $4,311M, $2,402M (AR2025 Table 02; 10-K Item 1). The filer's split (replacement = original cost of equipment sold): FY2022 $829.7M replacement, $935.7M growth (cash); FY2023 $1,380.8M and $1,638.8M; FY2024 $2,121.0M and $1,638.2M; FY2025 $1,323.1M and $622.8M (additions) (AR2022, AR2023, AR2024, AR2025 financial reviews).
- Five years of growth spending ($7.2B by this run's construction, including $3.5B of acquisitions) raised maintenance-only owner cash from $1,482M to $1,688M (q7 computation); revenue +40% over the same four years.
- Free cash flow (company definition) $126M in FY2024 against $2,055M in FY2026: "our cash flows are countercyclical" (10-K Item 7).
- The filer's RoI (pre-tax, goodwill included) 14.5% in FY2025, down from 19.2% in FY2023; segment RoI excluding goodwill FY2025: General Tool 20%, Specialty 30%, UK 7% (AR2025 glossary).

**Q4 (the accounts).**
- The company features "adjusted operating profit" and "adjusted EBITDA" (10-K Item 7, Non-GAAP Financial Measures) and calls EBITDA useful because it helps investors understand "ongoing cash earnings, from which capital investments are made and debt is serviced"; the adjusted figures exclude stock pay and restructuring.
- A material weakness was found after the half-year to 2025-10-31 (the $550M 1.500% notes due August 2026 classified non-current), the Form 10 half-year restated, and the weakness declared remediated at 2026-04-30; the company is not yet required to report on internal control under Section 404 (10-K Item 1A and Item 9A; 8-K of 2026-03-02).
- The stock-pay note corrects a prior figure: the weighted-average fair value of awards outstanding at 2025-04-30 "revised [...] from $44.41 to $60.97" (10-K stock-based compensation note).
- Stock pay swings with the share price because many awards were liability-classified: $92M (FY2024), -$9M (FY2025), $80M (FY2026) in the cash-flow add-back; $61M of awards reclassified from liability to equity in FY2026 (10-K statement of equity).
- Receivables rose 13% in FY2026 ($1,481M to $1,669M) against revenue +3%; the receivable provision charge rose from $28M to $64M (10-K cash flow statement); at 2026-07-31 receivables were $1,929M.
- Deferred tax liabilities $2,001M (FY2023) to $2,394M (FY2026) and $2,463M (2026-07-31); cash taxes paid $332M against a $476M provision in FY2026.
- UK goodwill: the fair value of the UK reporting unit "was not substantially in excess of its carrying value" (10-K Item 7, Critical Accounting Policies).

**Q5 (integrity facts, recorded, not judged).**
- Guidance: the company issues full-year guidance (IR site headline of the Q1 FY2027 release, "raises full-year fiscal 2027 guidance", read only as a headline) and its 10-K lists a failure to meet its own stated guidance among the risks to its share price. The rows on guidance and on making the numbers, **[L2019-006]** and **[L2002-041]**, bear on this at Q5 if a later run reaches it.
- The adjusted figures featured (Q4 above) **[L2016-006]**.
- At the US listing, outstanding performance share units, including those granted in fiscal 2026, had their performance conditions removed and "deemed to have been met at 85.5% of maximum" (DEF 14A, Compensation Discussion and Analysis), in a year in which net income fell 15%.
- The CEO's total reported pay rose from $12.1M (FY2025) to $14.6M (FY2026), including non-equity incentive pay of $2.2M against $1.4M, while operating income fell 13% (DEF 14A, 2026 Summary Compensation Table).
- The material weakness and the stock-pay correction (Q4 above).
- On the other side: the CEO has been with the business since 1996 and has run it since 2019; other executive officers average about 20 years with the group (10-K Item 1).

**Q6 (the money and the owners).**
- Buybacks: $1,413M in FY2026 (the program launched December 2024, completed in FY2026), an average of roughly $69 a share by the change in shares outstanding (430.7M to 410.3M; an estimate that ignores issuance); $1.5B new program from 2026-03-02, $315M spent by 2026-07-31, at $76.08 (May 2026) and $79.84 (June 2026) a share (10-Q Item 2). No price limit is stated. Against this run's computed range bottom ($49.42, all-equity), every price paid that I found is above it (the Q6 test of Part A, recorded here because Q7 is a computation).
- Dividends: $1.10 a share paid in FY2026; $0.75 declared in the quarter to 2026-07-31 and $0.30 a quarter from September 2026 (10-Q).
- Acquisitions: $1,277M (FY2022), $1,061M, $846M, $134M, $206M, then $667M in the quarter to 2026-07-31 and $56M after it (cash flow statements; 10-Q Note 15); all in cash, none in stock found. The Redomiciliation exchanged shares one for one; no stock-paid deal found.
- Pay: PSUs on relative TSR, compound adjusted EPS growth and adjusted RoI (DEF 14A); see Q5 for the waiver at listing.

**Q9 (debt and exposures).**
- Debt $8,556M at 2026-07-31, 81% fixed at 2026-04-30; senior notes maturing from 2027 to 2036; the ABL ($4,750M committed to November 2029) had $3,302M available at 2026-04-30; the company "was in compliance with all debt covenants that were in effect" (10-K Item 7). Net debt to EBITDA about 1.7x at 2026-04-30 (7,554 / 4,497), near 1.9x after the July acquisitions.
- Operating leases $2,867M (2026-07-31) on top.
- The 10-K's own risk factor: "Our substantial debt could adversely affect our financial health."
- Insurance: significant deductibles and self-insured retentions; no company-wide first-party environmental cover (10-K Item 1A).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). Commits: Step 0 (7ef6ab21), Q1 (9a6d9bfe), Q2 (c63522ec), then the computation and close.
- [x] If dispatched to an analyst: the brief allowed the per-question commits; the lock is the dispatching session's (not checked by me, as the brief does not ask me to); the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. One filtered listing of `Test Runs/` for the company's names was made before any fetch, to confirm the run file name was free; it returned nothing (declared under contamination at the top).
- [x] Every v5 id resolves (`check_cites.py`, run before each commit); every filing fact has its accession or, for the Ashtead annual reports, its document and page; no number without a row or a filing, and the run's own constructions are labelled.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; everything after it is NOT REACHED or headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operating income after depreciation, stock pay and restructuring, after tax; and free cash flow less stock pay, leases and acquisitions); the sovereign from the US Treasury; the price from an aggregator, flagged.
- [x] Contrary evidence was written down as it was found (foundations list, Q2 tests); the facts found for later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used (it printed only that it found no tagged history).
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The re-look condition of Q2's change-for-the-better convention was already met before this run.** The convention credits a change for the better "only on the evidence of a full cycle in which the price behaviour held" and fixes the re-look as "the first fiscal year in which the business's volume or its field's volume falls". For SUNB that year exists in the past: FY2021 (pandemic), US rental revenue -2%, the filer's dollar utilization held (51% to 50%) while United Rentals' fleet productivity fell 6.9%. The text does not say whether a past volume-falling year inside the improved era counts as the full cycle, or whether "full cycle" must be a downturn of the kind that broke the price before (here the construction-led 2009 to 2011). I weighed FY2021 as inconclusive (a one-year shock, the field's evidence mixed) and kept the box at TOO HARD (NATURE); another analyst could read FY2020 to FY2024 as a full peak-to-peak cycle in which the filer's price held, credit the change, and pass Q2, after which the file would close OUT at Q7 on price (no case earns the floor at $75.17). The box differs; the operator's figures do not. A sentence saying whether the re-look event must be a downturn in the field's volume of a stated depth, or simply any fall, would settle it. (2) **"The field's returns" has no measure.** The filer's RoI, United Rentals' and Herc's figures are defined differently; I built one plain measure (operating income on debt plus equity less cash) and labelled it a CONVENTION of this run. (3) **Specific (e)'s maintenance guess** does not say which of two filer-given guesses to use when they differ (depreciation, and "replacement = original cost of equipment sold", which the filer itself uses and which understates replacement when the fleet is aging); I used depreciation, which the row names, and said it is low under inflation. (4) **Specific (b) and (e) together**: the all-spending series changes sign (the investment years FY2023 and FY2024), so (b) reduces it to a no-growth case alone ($0.17 a share), while (e) makes the maintenance case central; the text could say that (b) applies to the beside-figure only when (e) applies. (5) **The template's Q5 wording** asks for integrity applied on doubt alone; a file closed at Q2 records integrity facts without judging them, and the facts here (performance conditions waived at listing, pay up as profit fell, guidance) are of the kind a later run must answer first.
