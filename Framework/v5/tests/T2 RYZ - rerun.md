# Company Run — Ryerson Holding Corporation (NYSE: RYZ) — 2026-10-06
**TEST RECORD, not a run of record.** Written under `Framework/v5/tests/T2 PROTOCOL - the four re-runs of 2026-10-06.md`
and `Framework/v5/tests/RULES UNDER TEST 2026-10-06 - sections D and H.md`; it binds nothing, enters no register and
changes no verdict of record. **Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules:
`Framework/OPERATOR-PROTOCOL.md`. The run form is the one fifteen test runs used
(`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`; not opened, under the T2 blind rule). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**
Copied 2026-10-06 before the first fetch. Working folder `Framework/v5/tests/_work_T2_RYZ/` (gitignored by `.gitignore`
line 117, `Framework/v5/tests/_work_*/`, so the commits below carry the run file alone; see the self-audit).

**POSITION NOTE, declared before any verdict:** not checked. The T2 protocol's blind rule forbids opening `PORTFOLIO.md`,
so whether the operator holds this name is unknown to this run and was not sought.

**CONTAMINATION, declared:** (1) the subject line of commit b4c7bb86, seen in `git log` while locating the protocol file,
names the four re-run tickers (ENSG, RYZ, EFOR, PBH) and says the re-runs test sections A, D and H; (2) the session's
opening `git status` listed `Framework/v5/tests/T2 ENSG - rerun.md` and research-folder names under `Test Runs/` (ARCB,
AYI, BDC, CHD); (3) `tools/run.py` printed v4 material (a yield, a "growth the price assumes", a sovereign-spread line)
beside its arithmetic. None of it was opened or used; only the arithmetic lines of `run.py` were read (Part VII). Nothing
of any earlier RYZ or RYI run, holding review or register entry was seen.

**THE EVENT THE BRIEF DID NOT NAME.** On 2026-02-13 Ryerson completed an all-stock merger with Olympic Steel, Inc.
(1.7105 Ryerson shares per Olympic share, about 19.5 million shares issued; 8-K of 2026-02-13, accession
0001193125-26-051335). Olympic ceased trading that day and filed a Form 15 on 2026-02-23 (accession 0001193125-26-063593);
the ticker changed from RYI to RYZ on 2026-02-24. The brief lists Olympic Steel (ZEUS) as a rival to be read from its own
filings; it is now a subsidiary of the subject, and its last own filings are the FY2024 10-K (accession
0001437749-25-004742) and the 10-Q for 2025-09-30 (accession 0001437749-25-032420). They are used here as the record of
the business Ryerson bought, and under rule under test, section D(c), the merged companies are valued on their combined
averages. Russel Metals is a Toronto-listed filer, not an SEC filer, and is named only as the filer names it.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $27.14 (2026-10-06, aggregator live quote via `tools/run.py`, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: 51,898,653 shares of common stock, one class, as of 2026-07-24
  (10-Q for the quarter ended 2026-06-30, filed 2026-07-29, accession 0001193125-26-323769; `python Screens/cover_shares.py
  RYZ` returns the same count; 100,000,000 authorized; no second class on the cover). The balance sheet shows 60.233M
  issued at 2026-06-30 (XBRL), the difference being treasury shares (treasury stock $237.0M at 2025-12-31, 10-K). The
  count stood at 32,211,943 on 2026-01-12 (special-meeting record date, 8-K 0001193125-26-048687) before the 19.5M merger
  shares. No 8-K or prospectus after the 10-Q changes it.
- **Market cap:** $1,409M (51.899M x $27.14).
- **Sovereign for the earnings currency (USD):** 5.66%, the US Treasury 30-year par yield, 2026-10-05, from the Treasury
  daily par yield curve (`python tools/sources.py`).
- **Filings read** (operator rule 4): the 10-K for FY2025 (filed 2026-02-23, accession 0001193125-26-062397) and the
  10-Ks for FY2014 to FY2024 (accessions 0001193125-15-094069, 0001564590-16-014318, 0001564590-17-004120,
  0001564590-18-004385, 0001564590-19-006287, 0001564590-20-008692, 0001564590-21-008111, 0001564590-22-006263,
  0000950170-23-003768, 0000950170-24-018005, 0000950170-25-024199); the 10-Q for 2026-06-30 (0001193125-26-323769); the
  proxy of 2026-03-18 (DEF 14A, 0001193125-26-114120) and of 2025-03-05 (0000950170-25-033598); the 8-Ks of 2025-10-28
  (merger agreement, 0001193125-25-257064), 2026-02-05 (preliminary Q4 results and proxy supplement, 0001193125-26-040024),
  2026-02-12 (special meeting, 0001193125-26-048687), 2026-02-13 (closing, 0001193125-26-051335), 2026-04-30 (annual
  meeting, 0001193125-26-208963) and 2025-04-17 (annual meeting, 0000950170-25-056771). Rivals: Reliance, Inc. 10-K FY2025
  (0001104659-26-020651), Worthington Steel, Inc. 10-K FY2026 (May year-end, 0001968487-26-000026), Olympic Steel 10-K
  FY2024 and 10-Q 2025-09-30 as above. Annual series for all four are transcribed from each year's 10-K as filed (SEC
  companyfacts, first-filed vintage; the accessions of the Reliance series are 0001558370-17-000994 through
  0001558370-25-001806 and the FY2025 10-K; of the Olympic series 0001437749-17-003663 through 0001437749-25-004742).
  **One figure cross-checked against the filed statement:** FY2025 net cash provided by operating activities, $87.0M, read
  on the consolidated statement of cash flows in the 10-K (same accession) against the XBRL figure the tool printed, 87.0;
  capital expenditures $(51.5)M likewise. The cover count 51,898,653 was read on the 10-Q cover itself.
- `python tools/run.py RYZ` arithmetic lines only (USD millions, as filed): OCF 365.1 / 204.9 / 87.0 for FY2023 / FY2024 /
  FY2025; SBC 13.8 / 11.6 / 8.7; D&A 62.5 / 77.6 / 79.7; capex 121.9 / 99.6 / 51.5; finance-lease principal 7.1 / 6.4 /
  6.0 (the tool's "other capital payment" alternate). The tool's three-year mean of OCF less SBC less capex is 116.6 and
  its five-year mean 141.4; its ten-year balance-sheet table is read below. Its v4 lines (a yield, a growth the price
  assumes, a spread over the sovereign) were not read (Part VII). The tool could not open the FY2025 10-K (HTTP 503) and
  read it from the earlier filings' XBRL; the figures above were checked against the FY2025 10-K directly.

**The balance sheets first, twelve year-ends FY2014 to FY2025, read before the income account** **[M2025-032]**, because
the file closes before Q4 (the brief and the template ask for them in Step 0 in that case). USD millions, from the 10-Ks
listed above (the tool's table runs 2016 to 2025; 2014 and 2015 are from the FY2014 and FY2015 10-Ks); total debt is the
filer's own "Total debt" line in each 10-K; the LIFO reserve is the inventory note.

| year-end | assets | equity | cash | receivables | inventory (LIFO reserve) | goodwill | PP&E | total debt | pension and OPEB liability | retained earnings | treasury stock |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2014 | 1,977 | (129) | 60 | 401 | 739 (25) | 103 | 426 | 1,259 | 385 | n/a | 7 |
| 2015 | 1,556 | (142) | 63 | 306 | 556 (122) | 103 | 400 | 1,035 | 328 | n/a | 7 |
| 2016 | 1,559 | (51) | 81 | 326 | 563 (115) | 103 | 388 | 964 | 299 | (112) | 7 |
| 2017 | 1,712 | (10) | 77 | 376 | 617 (71) | 115 | 423 | 1,046 | 244 | (95) | 7 |
| 2018 | 2,086 | 73 | 23 | 521 | 806 (18) | 120 | 489 | 1,153 | 258 | 14 | 7 |
| 2019 | 2,022 | 173 | 11 | 425 | 743 ((51)) | 120 | 440 | 982 | 218 | 100 | 7 |
| 2020 | 1,802 | 139 | 61 | 379 | 605 (63) | 120 | 422 | 740 | 232 | 34 | 7 |
| 2021 | 2,366 | 537 | 51 | 631 | 832 (303) | 124 | 388 | 639 | 163 | 322 | 8 |
| 2022 | 2,334 | 885 | 39 | 514 | 799 (245) | 129 | 458 | 367 | 118 | 692 | 61 |
| 2023 | 2,570 | 906 | 54 | 468 | 783 (148) | 158 | 590 | 437 | 107 | 813 | 179 |
| 2024 | 2,440 | 815 | 28 | 426 | 685 (95) | 162 | 637 | 467 | 91 | 780 | 234 |
| 2025 | 2,405 | 753 | 27 | 461 | 648 (151) | 162 | 610 | 463 | 70 | 699 | 237 |
| 2026-06-30 | n/a | n/a | 42 | n/a | n/a | 164 | n/a | 955 | n/a | n/a | n/a |

What the figures say. (1) The company came to market in August 2014 with negative equity of $129M and $1,259M of debt,
the residue of a private-equity owner: Platinum Equity held about 66% after the IPO of 11 million shares at $11.00, and
the IPO proceeds went to redeem 11.25% notes and to pay Platinum $15.0M (FY2014 10-K, 0001193125-15-094069). Equity turned
positive only in 2018 and was built almost entirely by the retained earnings of 2021 and 2022, the two years the filer
itself calls cyclical highs (FY2023 10-K, 0000950170-24-018005: "Commodity prices were at cyclical highs in 2021 and
2022"). (2) Debt fell from $1,259M to $367M by 2022, paid down from the working-capital release and the profits of the
price spike; the 11% notes of 2022 were replaced by 8.5% notes of 2028 in 2020, and those were retired in 2022, leaving an
asset-based revolving credit facility as the whole of the borrowing. It then rose again: $463M at 2025-12-31 and $955M at
2026-06-30 after $270.0M was borrowed to retire Olympic's debt and working capital was funded (10-Q 0001193125-26-323769).
(3) Inventory and receivables are the business: $1.1B of the $2.4B of assets, and the LIFO reserve of $151M means
inventory at current cost is about $800M. They swing with metal prices (receivables $379M in 2020, $631M in 2021), which
is why operating cash flow runs against the cycle: $278M in the 2020 trough, $35M in the 2021 boom. (4) Goodwill rose
from $103M to $162M over eleven bolt-on acquisitions, and PP&E from $426M to $637M in a three-year spend of $327M
(2022 to 2024) the filer calls "a historically high three-year investment cycle" (FY2025 10-K). (5) The pension
liability fell from $385M to $70M by contributions of $55M (2014) and $42M (2015) and by annuitisation in 2020; $33.1M of
pension and $30.7M of retiree-medical remain unfunded at 2025-12-31 (FY2025 10-K). (6) Treasury stock of $237M records
buybacks of 2021 to 2024, 2.9M shares of them from Platinum; retained earnings fell in 2024 and 2025 as losses and
dividends ran ahead of earnings. What they cannot say: the earning power of the merged company, whose first balance
sheet (2026-06-30) carries preliminary purchase accounting that the filer says "may be material" in its adjustments.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the market's silence about value: the quotation of $27.14 "doesn't tell us anything.
It just tells us prices" **[M2006-077]**, and it has moved from $22.87 on 2025-10-27 (the proxy supplement, 8-K
0001193125-26-040024) through an all-stock merger without telling the owner what the merged business earns. The share is
read as a business: a service center that must be worth owning "if the market closed for five years" **[M1997-109]**,
through at least one more metals cycle. No macro enters: the metals price, the tariff and the PMI readings the filer
reports are answered by asking "what's likely to be the average profitability of the business over time and how strong
its competitive mode is" **[M2015-016]**. Who is paid to tell: the merger's fairness opinions, the proxy supplement
records, priced the target on EV/EBITDA comparables and "customary" premiums, which the rows call "an absolutely asinine
way to evaluate the attractiveness of an acquisition" **[L2014-013]**; nothing from them is used. The analyst's habit:
hunt for "what's wrong in things" **[M2025-013]** and write it down at once **[M1997-127]**. **Contrary evidence, written
down as found** **[M1997-127]**: the filer's own volumes gained share in 2025 (Ryerson down 0.4% against the industry's
1.5% decline, FY2025 10-K); Reliance, the leader, has stayed "profitable every year since our initial public offering in
1994" (Reliance 10-K FY2025, 0001104659-26-020651), so a service center can be a very good business; the margin of safety
has to be read against that leader's economics, not against Ryerson's own history.

## THE STANDING RULE
The target is a cyclical, inventory-heavy, now re-levered distributor whose equity was negative for four of the last
twelve year-ends; it is the kind of holding whose price can halve inside a cycle, so it can be held only with money the
buyer does not need and never on margin **[L2014-005]**, because borrowed money "can prevent you from playing out your
hand" **[M2004-065]**; the rule binds the buyer's financing and sizing whatever the questions below conclude
**[M2012-081]**, **[L2023-005]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The business.** Ryerson buys carbon, stainless and aluminum from mills in large quantities, holds about $800M of it
  at current cost in 103 North American service centers, processes nearly 80% of what it sells (cutting, sawing, laser,
  forming), and delivers it in small lots to about 40,000 customers, none above 6% of sales and the top ten about 15%
  (FY2025 10-K, 0001193125-26-062397). One operating segment, metals service centers (same filing, Note 13). With
  Olympic Steel it adds carbon and coated flat products, pipe and tube and some metal-intensive end products (8-K
  0001193125-26-051335). The product needs no chemistry; what matters is "the economic dynamics of the industry"
  **[M2011-014]**.
- **The key variables, and whether they are predictable** **[M1998-044]**. Twelve years of the filer's own tables
  (10-Ks FY2014 to FY2025, accessions in Step 0) give them: tons sold (2,025 thousand in 2014, 2,381 at the 2019 peak,
  1,947 in 2025), average selling price per ton ($1,790; $1,503 in the 2016 trough; $3,117 at the 2022 peak; $2,348 in
  2025), gross profit per ton (about $293 to $348 from 2014 to 2020, $646 in 2022, $402 in 2025), operating expense per
  ton ($230 in 2016, $418 in 2025, the filer's own figure), and interest ($100M paid in 2014, $41M in 2025). The metal
  price is unforecastable in any year, but the filer says what it does to the business: "Changes in average selling
  prices are primarily driven by commodity metals prices, which impact Ryerson's selling prices over the subsequent three
  to six-month period" (FY2025 10-K), so the price passes through with a lag and the ten-year question is the spread per
  ton and the volume, not the price. Those two have been stable to falling for a decade: volume flat to down, the spread
  rising with the processing mix while the cost per ton rose faster. That is "a reasonable fix on about what the earning
  power and competitive position will look like in five or 10 years" **[M2012-065]**: a thin-margin intermediary whose
  earnings swing with the cycle around a low average.
- **Change.** The industry is slow: the filer's description of what a service center does in 2025 would have served in
  2014, and the fragmentation it describes ("the largest companies accounting for only a small percentage of total market
  share") is what Reliance's 10-K describes too (17% share for the leader). No fast-moving technology bears on the
  forecast; the AI risk factor in the 10-K is boilerplate about tools, not about the product. "Most of our decisions
  relate to things where we expect the future not to change much" **[M2000-034]**, and this is such a thing. The
  routing to TOO HARD for rapid change does not apply **[L2007-005]**, **[M1999-063]**.
- **Would the insiders write it down?** **[M2000-105]**. Reliance's 10-K writes its ten-year view in so many words
  (consistent profitability since 1994, share gains in a fragmented market); the merger proxy supplement records both
  advisers' five-year projections for both companies (8-K 0001193125-26-040024). The insiders write the forecast down;
  what they write is a cyclical, low-return business, which is a finding for Q2, not a bar to understanding.
- **How far off could I be?** The test used is **[M2008-033]**: do the past statements tell me the future ones? For any single year, no: the 2021 to 2022 spike doubled the spread per ton and the
  2025 trough halved it back. Over a cycle, yes: the averages of two cycles (Step 0 and Q7) sit close together. The error
  is in the year, not in the decade.
- **Do I doubt it is inside?** **[M2002-092]**. The one doubt is the merged company's integration, which no filing can yet
  show; but a merger of two service centers is the same business at larger scale, and the filer's and the target's own
  twelve-year records are both on file. The doubt is about execution, which Q5 and Q6 carry, not about what the business
  is. A holding company's parts rule does not arise: one segment **[M2006-013]**.
- **VERDICT: IN.** The business is understood in the rows' sense: its economics ten years out can be foreseen as the
  average of a cycle of a commodity intermediary **[M2012-065]**, **[M2000-037]**, from "the figures" of its own and its
  rivals' filings **[M2008-069]**; nothing is unknowable that is important **[M2006-076]**. Filing facts: the twelve-year
  tons and price-per-ton tables and the one-segment note (FY2025 10-K, 0001193125-26-062397; FY2019 10-K,
  0001564590-20-008692; FY2016 10-K, 0001564590-17-004120).

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
- **The castle question** **[M1995-038]**: why is Ryerson still standing after 184 years, and what keeps it standing?
  The filer's answer, in its own words, is scale and reach: "one of the largest value-add processors and distributors of
  industrial metals in North America measured in terms of sales", "among the largest purchasers of metals in North
  America", 103 facilities, 75,000 products, 40,000 customers (FY2025 10-K, 0001193125-26-062397). Munger's translation
  is "advantages of scale" **[M1995-039]**. The tests below ask whether that scale protects a return.
- **The attacker with money** **[M2011-015]**, **[M2000-077]**. The filer: "Our industry is highly fragmented with the
  largest companies accounting for only a small percentage of total market share. The majority of metals services
  companies have limited product lines and inventories and their customers are usually located within their local
  geographic area"; "There are a few large competitors, but most of the market is served by small local and regional
  competitors" (FY2025 10-K). Entry is by a warehouse, a saw and a credit line, and thousands have entered; the field
  consolidates by purchase, not by attrition, and the filer's own growth strategy is "industry consolidation through
  targeted M&A" (same filing), which is to say the share is bought at five to nine times EBITDA (the fifteen precedent
  transactions in the proxy supplement, 8-K 0001193125-26-040024). An attacker with money has no need to build; it buys
  the next one, as Ryerson did eleven times since 2014 and as Reliance did. "there are some industries that are just
  never going to have barriers to entry" **[M2012-106]**.
- **Pricing power and the agony before a rise** **[M2005-020]**. The filer sets no price of its own: "Average selling
  prices generally fluctuate with changes in replacement costs of the various metals we purchase"; "When metals prices
  decline, customer demands for lower prices and our competitors' responses to those demands could result in lower sale
  prices"; "When metals prices increase, competitive conditions will influence how much of the price increase we may pass
  on to our customers" (FY2025 10-K). The fourth quarter of 2025 is the agony itself: "material input costs rose faster
  than anticipated and the increases in costs of goods sold compressed gross margins as resale prices remained flat",
  gross margin 17.2% to 15.3% in one quarter (8-K 0001193125-26-040024). The competitor sets the price **[M2023-079]**,
  **[M2012-109]**; and "most insureds don't care from whom they buy" **[L2004-003]** reads across to a buyer of
  cut-to-length plate. The one price the filer does hold is on processing: "maintaining pricing discipline related to our
  processing services" (FY2025 10-K), a claim Reliance makes in the same words (Reliance 10-K FY2025,
  0001104659-26-020651), so it is the field's claim, not a moat of one.
- **Unit volume and share of mind** **[M1999-054]**. Tons sold: 2,025 thousand (2014), 2,381 (2019, with Central Steel
  & Wire bought in 2018), 1,947 (2025): down 4% over eleven years and down 18% from the acquired peak, while the North
  American industry's volume moved little. Share of mind for a service center is a buyer's habit and a salesman's call;
  nobody asks for Ryerson by name, and the filer records that its customers "may choose to diversify their supply chains
  to reduce reliance on a single supplier" after any merger (FY2025 10-K). The one positive fact: 2025 volume held better
  than the industry's (down 0.4% against 1.5%), which the filer calls share gained; Reliance's grew 6.2% the same year
  (Reliance 10-K FY2025). Volume is not failing; it is not growing either.
- **The low-cost position** **[M1997-010]**, **[L2000-017]**, **[L2004-007]**. This is the test a commodity
  intermediary must pass, and Ryerson fails it against the leader. Gross margin on sales (gross profit over sales, both
  filers' own lines): Ryerson 17.1% in 2025 and 16% to 21% every year since 2014; Reliance 28.7% on the same LIFO basis in
  2025, 29.5% FIFO (Reliance 10-K FY2025). Operating expense per ton, the filer's own figure, rose from $230 (2016) to
  $418 (2025) while tons fell; Reliance reports same-store expense per ton falling 1.0% in 2025 on volume up 5.3%. The cost
  that matters is the one measured against the rival, "if your costs are on parity or less [...] than your other major
  competitors" **[M2001-013]**, and Ryerson's is higher; the rows' sentence for that case is that "the guy with the lower
  cost comes in and kills you" **[M2001-013]**; "In an unregulated commodity business, a
  company must lower its costs to competitive levels or face extinction" **[L1994-035]**. Ryerson has not faced extinction
  because the field is fragmented enough that the leader does not need its customers; that is survival, not a castle.
- **The brand in the customer's mind** **[M2008-075]**: none claimed; the filer's trademark is a slogan ("say yes, figure
  it out", FY2025 10-K), not a promise the customer pays for. **Would the customer choose it over the low bid**
  **[M2017-009]**: "Competition is based principally on price, service, quality, production capabilities, inventory
  availability, and timely delivery" (FY2025 10-K), price first in the filer's own list.
- **Ask the competitors** **[M1999-130]**. Reliance's 10-K answers it without being asked: it attributes its share gains
  to "scale, processing capabilities, customer service levels, product and geographic diversity" and names its 17% share
  of U.S. industry tons; Olympic's last 10-K (0001437749-25-004742) reported a 1.5% operating margin on carbon flat
  products and 4.0% on specialty metals in 2024. Neither names Ryerson as the one it fears. Worthington Steel's 10-K
  (0001968487-26-000026) describes a different business (toll processing and electrical steel for automotive) and is a
  rival in flat-rolled only.
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Narrowing on the cost side (expense per ton up 82% in nine
  years against a flat volume), widening on the processing side (gross profit per ton up from about $300 to about $400
  outside the spike years, with $437M of capital spent in five years to do it, FY2025 10-K). The two together left the
  operating profit per ton in 2025 ($(16)) below 2016's ($70) and the 2020 trough's ($32); the moat that must be
  "continuously rebuilt" by capital spending **[L2007-005]** is the picture the figures give.
- **What could destroy it** **[M2000-014]**: nothing sudden; the mills selling direct (the filer names metal producers as
  competitors "to a lesser extent"), the next downturn arriving with $955M of debt (Q9, below), and the leader's cost
  advantage compounding.

- **The competitor row**, the same metric from each filer's own 10-Ks, over the last full cycle and the one before:
  pre-tax income (after interest) as a share of average total assets, and operating income (before interest) likewise,
  from the annual figures each company filed (Reliance accessions 0001558370-17-000994 to 0001558370-25-001806 and
  0001104659-26-020651; Olympic 0001437749-17-003663 to 0001437749-25-004742; Ryerson as in Step 0; Worthington Steel
  0000950170-24-090031, 0000950170-25-099742, 0001968487-26-000026).

| company | pre-tax on average assets, FY2020 to FY2025 | pre-tax on average assets, FY2016 to FY2019 | operating income on assets, FY2020 to FY2025 | pre-tax margin on sales, FY2020 to FY2025 | gross margin, latest year | years with a net loss, 2014 to 2025 |
|---|---|---|---|---|---|---|
| Reliance, Inc. (RS) | 14.7% | 8.9% | about 15% | 10.4% | 28.7% (LIFO), 29.5% (FIFO) | none since 1994 (its own statement) |
| Ryerson (RYZ) | 6.7% | 3.7% | 10.2% | 3.2% | 17.1% | five (2014, 2015, 2020, 2024, 2025) |
| Olympic Steel (ZEUS), FY2020 to FY2024 | 8.2% | 2.7% | n/a | n/a (operating margin 1.5% carbon flat, 4.0% specialty, 2024) | n/a | four (2014, 2015, 2016, 2020) |
| Worthington Steel (WS), FY2022 to FY2026 (May) | about 7.7% | n/a (spun off 2023) | n/a | 4.3% | 11.7% | none in its five filed years |
| Russel Metals | not an SEC filer; not used | | | | | |

- **The parts table**: not applicable; one operating segment, metals service centers (FY2025 10-K, Note 13). Olympic's
  segments (carbon flat, specialty metals flat, tubular and pipe) are now inside that one segment.
- **The field's returns over the last full cycle, judged in words** (section C). The cycle is 2020 trough to 2025
  trough on the filer's own description ("cyclical highs in 2021 and 2022", FY2023 10-K; "subdued downstream demand"
  and an operating loss in 2025, FY2025 10-K). Over it the leader earned a return any owner would call excellent on
  tangible capital, and the second and third earned, before interest, a return in the range of the long bond plus a few
  points, and after interest about half that; in the prior cycle Ryerson earned 3.7% pre-tax on assets and lost money
  after tax in two of four years. Those are ordinary returns on a durable position, and the rows say what to make of a
  business "earning 5 or 6 percent on equity" held long: "Time is the enemy of the poor business" **[M1998-006]**. The
  field is not one where every durable player earns ordinary returns, since Reliance does not; it is one where the
  low-cost operator earns well and the rest earn the commodity return, which is exactly the rows' description of a
  commodity field with one exception **[L2004-007]**, **[L2000-017]**, and Ryerson is not the exception. "you can have
  only two competitors and they're still terrible businesses" **[M2013-052]**; here there are thousands.
- **The change for the better claimed** is the merger: "$120 million in annual synergies by the beginning of 2028"
  (FY2025 10-K). Under section C a change for the better is credited only on the evidence of a full cycle in which the
  price behaviour held; none has run, and the rows "never count on synergies" **[L2016-008]**. Not credited.
- **The three boxes.** This is not a castle whose future cannot be judged: the field is slow, the returns of two cycles
  are on file from three filers, and the leader's own filings show what the castle in this field looks like and who holds
  it. So the box is not TOO HARD **[M2000-019]**; the castle is shown on the evidence to protect ordinary returns and to
  belong to a higher-cost operator in a field where the customer buys on price. The rows' word for that is extinction
  over time **[L1994-035]**, and the purchase they refuse is "a fair business at a wonderful price" **[M2003-040]**.
- **VERDICT: OUT.** A commodity intermediary that is not the low-cost operator **[M1997-010]**, **[L1994-035]**, whose
  price its rivals and the mills set **[M2023-079]**, whose customers buy "for the low bid" **[M2017-009]**, and whose
  castle, durable as it is, protects only ordinary returns over the last full cycle on its own and its rivals' filings
  (section C, **[L2007-004]**: the moat is what "protects excellent returns on invested capital", and these are not).
  The file closes here. **Integrity facts recorded, not judged** (AFTER THE STOP, Q5).

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **NOT REACHED.** The file closed at Q2. The facts already found that bear here are under AFTER THE STOP, Q3; nothing
  below this line is a clearance (operator rules 2 and 3).

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, eight to ten years of them, before the income account** **[M2025-032]** (`tools/run.py`
  prints the ten-year table; read the filed statements behind it). Say what moved and why: equity against goodwill and
  intangibles, cash, receivables and inventory against sales, debt, retained earnings; "what the figures are saying and
  what they don’t say and what they can’t say" **[M2025-032]**. *(line added 2026-10-05: the rule was in Q4 of the
  framework from adoption, and no run had been asked to do it.)*
- The real costs (depreciation, stock pay, restructurings, the recurring "one-time"); EBITDA in the filer's own
  mouth; what the accounts say of management's character. The make-the-numbers habit, guidance and a featured
  adjusted figure weigh against here and are carried to Q5 (section A of the gaps case, 2026-10-06).
- **NOT REACHED.** The file closed at Q2. The balance sheets were read in Step 0 as the template asks; the facts found
  on the accounts are under AFTER THE STOP, Q4, not weighed. The recast cash feeds the Q7 COMPUTATION only.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- The two yardsticks; the tells of dishonesty (the proxy, the letters, how they talk about mistakes); love of the
  business; what ability shows in. Integrity applied on doubt alone.
- The habits carried from Q4 (targets made or beaten, guidance, the adjusted figure featured), read with the integrity
  record; doubt closes **[M2013-088]**.
- **NOT REACHED.** The file closed at Q2. Integrity facts are recorded under AFTER THE STOP, Q5, not judged; the box
  line carries the flag (Part VII, section G of the gaps case).

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- Part A: the retention test (a dollar kept worth more than a dollar, over time); buybacks (only below value; a buyback
  with no stated price weighs against unless the prices paid sit at or below the bottom of the Q7 range); issuance and
  deals (value given against value got; an all-stock deal at an undervalued price is the one STOP here).
- Part B: pay tied to what the person controls; the board; the owners as partners.
- **NOT REACHED.** The file closed at Q2. The facts on the money and the owners, including the all-stock merger that
  Part A's one STOP describes and the buyback prices against the Q7 COMPUTATION's range, are under AFTER THE STOP, Q6.

## Q7 — WHAT IS IT WORTH? STOP.
### COMPUTATION, NOT A CLEARANCE
*The file closed at Q2. Everything in this section is arithmetic the T2 protocol requires so that the rules under test
can be seen to bear; it carries no entry language and changes no box (operator rules 2 and 3). Script:
`Framework/v5/tests/_work_T2_RYZ/compute.py`; USD millions; the rate is the 30-year Treasury par yield, 5.66%.*

- **The cash counted.** Owner cash after every real cost is the filer's operating cash flow (after the working-capital
  draw) less stock pay, less capital spending, less finance-lease principal, less cash paid for businesses net of cash
  acquired, each from the cash-flow statement of the year's 10-K: "they get credit for whatever net cash is left every
  year" **[M1998-080]**, and "are you going to have to put more cash into after you buy it?" **[M2014-068]**. Rule under
  test, section D(d): the increase in working capital is capital spending for the range; it is already inside the
  operating cash flow used, and no single year's draw is tied by the filer to one contract or event (the 2021 draw is
  tied to the metal price, "supply constraints in 2021", FY2021 10-K), so no aberrational-year variant at an earlier
  working-capital intensity is shown; the 2021 year is instead handled by rule under test, section D(a) as a peak year.
  Rule under test, section D(e): the filing offers no maintenance figure (Q3 facts), so the maintenance guess is not
  allowed and the central case charges all spending, with the depreciation variant beside it (Part VI's four specifics);
  no growth bought by that spending is capped in return, so nothing is charged twice.
- **Rule under test, section D(c), acquisitions and the merger.** The default pair is applied: cash paid for businesses
  is deducted and the total growth shown is credited. The merger with Olympic closed on 2026-02-13, after the five-year
  window and before the price; the text speaks of "a merger inside the window", and it is applied here as the nearer
  case, since the shares priced today are the merged company's: the two companies' own averages are combined over the
  same years, and the deal's financing is deducted through the share count (the 19.5M shares issued are in the 51.9M)
  and through net debt (the $270.0M borrowed to retire Olympic's debt is in the $913M). Olympic's figures are its own
  10-Ks FY2016 to FY2024 (accessions in Q2) and, for FY2025, the twelve months to 2025-09-30 from its 10-Q
  (0001437749-25-032420), the last period it filed; the $80.0M it paid for a business in the fourth quarter of 2024 is
  kept in 2024 and not repeated. The second pair (acquisitions not deducted, organic growth only) is shown beside, and
  on it no growth is credited: the only organic measure the filer reports is tons, and tons fell from an average of
  2,138 thousand over FY2016 to FY2019 to 1,993 thousand over FY2020 to FY2025 (Q1), so "never left out with the total
  growth credited" is honoured by crediting none.
- **Rule under test, section D(a), the cycle.** The literal window FY2021 to FY2025 opens on a year the filer itself
  calls a cyclical high ("Commodity prices were at cyclical highs in 2021 and 2022", FY2023 10-K), so its first year is
  aberrational in the rows' sense **[L2005-003]**, **[L2003-004]**, and the base is the average over the last full
  cycle, trough to trough, FY2020 to FY2025 (the 2020 trough on volume and price, the 2025 trough on price and operating
  profit, Q1's series), with the literal window shown beside it. The growth is measured between the averages of
  successive cycles **[M2011-101]**, **[M2011-102]**, **[M2021-039]**: the prior cycle FY2016 to FY2019 averaged
  combined owner cash of $(43.3)M (acquisitions deducted) and the last cycle $102.9M.
- **Rule under test, section D(b), decline and sign.** Between the cycle averages the series changes sign (negative to
  positive), so the compound rate is meaningless; inside the literal window the first half averages $129.4M and the
  second half $12.3M, a decline of nine-tenths over two and a half years that the rows would carry as negative
  **[M2006-058]**, **[M2006-059]** but whose compound rate is meaningless too. Under D(b) the range is therefore the
  no-growth case alone, said so: each basis below is a single figure, and the "range" is the spread across the stated
  variants, not a growth range.
- **Rule under test, section D(f), the cap.** No shown growth exists to carry, so the cap does not bind; for the width
  only, carrying the central unlevered figure at the discount rate for ten years would give $59.38 a share, a figure no
  evidence supports **[M1997-095]**, **[M1999-067]**, **[M1997-096]**. A price above the top of the range would close
  OUT by the floor convention; here the price sits below the central figure and the close comes through the floor
  itself.
- **Rule under test, section H, the basis.** The central figure is built on the all-equity basis: owner cash before
  interest and after the company's tax (cash interest paid added back at 75%, the 21% federal rate plus state being
  taken as 25%, a CONVENTION of this run; the FY2025 10-K calls its 22.6% effective rate "more in line with the U.S.
  statutory tax rates"), against market value $1,409M plus net debt $913M at 2026-06-30 (total debt $955.2M less cash
  $41.9M, the filer's own net-debt line; operating leases of $349M left out and said so). The whole-business value less
  net debt gives the per-share figure; the fair price is computed on the same basis; the equity-only figure (owner cash
  after interest against market value) is shown beside it and never decides alone. Rationale as the text gives it:
  "even a high-priced deal will usually boost per-share earnings if it is debt-financed" **[L2017-004]**, and the net
  debt doubled with the merger while the historical interest charge did not. The floor is about ten percent pre-tax on
  owner cash after the company's own tax, no conversion, "we don't want to buy equities where our real expectancy is
  below 10 percent" **[M2003-149]**, **[L2002-020]**, **[M1994-004]**; no carryforward runs out inside ten years that the
  filing prices (cash taxes paid were $5.7M on a pre-tax loss in 2025 and $176.9M in 2022; FY2025 10-K and FY2022 10-K).

| basis (all no-growth, D(b)) | owner cash, average | whole-business value at 5.66% | less net debt $913M, per share | expected return at $27.14 (all-equity) | fair price, all-equity | equity-only value per share | expected return at $27.14 (equity-only) | fair price, equity-only |
|---|---|---|---|---|---|---|---|---|
| **CENTRAL: combined companies, last full cycle FY2020 to FY2025, acquisitions deducted (D(a), D(c), H)** | 144.4 unlevered; 102.9 after interest | 2,551 | **$31.56** | **6.2%** | **$10.23** | $35.02 | 7.3% | $19.82 |
| beside: combined, literal window FY2021 to FY2025, acquisitions deducted (D(a) requires it shown) | 109.3; 69.9 | 1,931 | $19.62 | 4.7% | $3.47 | $23.78 | 5.0% | $13.46 |
| beside: combined, last cycle, acquisitions not deducted, organic growth only, which is none (D(c), second pair) | 233.5; 192.0 | 4,126 | $61.90 | 10.1% | $27.40 | $65.36 | 13.6% | $36.99 |
| beside: combined, last cycle, depreciation in place of capital spending and lease principal, acquisitions deducted (Part VI variant) | 161.4; 119.9 | 2,852 | $37.37 | 7.0% | $13.52 | $40.83 | 8.5% | $23.11 |
| beside: Ryerson alone, last cycle, acquisitions deducted (Olympic's cash left out while its shares and debt stay in) | 141.5; 108.6 | 2,499 | $30.56 | 6.1% | $9.66 | $36.96 | 7.7% | $20.92 |

- **Value range:** on the central basis the no-growth case alone, $31.56 a share against $27.14 (equity-only $35.02);
  across the variants $19.62 to $61.90 a share, a spread the variants make and not a growth range, its top the one
  basis that leaves $395M of purchased businesses out of the cost of the cash they produced. **Closes (as a
  computation):** OUT. The price sits inside the variants' spread and just below the central figure, and the expected
  return at the price on the central basis is 6.2% pre-tax after the company's tax, below the floor at which the name
  is quit on, "there's just a point at which we drop out of the game" **[M2003-149]**; the central figure is not "so
  obvious that you don't have to carry it out to tenths of a percent" **[M2009-005]**, and the pencil was needed
  **[M1996-084]**. The width across variants is under three to one, so the computation does not fall to TOO HARD
  **[L2000-025]**.
- **Fair price (a reporting figure, never a verdict; Part VII):** **$10.23 a share** on the all-equity basis (central
  case: $144.4M of owner cash before interest and after the company's tax, at ten percent, $1,444M, less net debt
  $913M, over 51.899M shares); **$19.82** on the equity alone ($102.9M after interest at ten percent over the shares).
  Tax treatment: owner cash after the company's own income tax, the interest add-back at a 25% rate (CONVENTION, above),
  no conversion for the holder's tax. The two differ because the merger doubled the net debt against which the floor is
  earned; the all-equity figure is the central one (rule under test, section H). No cheap price is reported.
- **VERDICT (computation only; the box was filled at Q2): OUT.** "we don't want to buy equities where our real
  expectancy is below 10 percent" **[M2003-149]**; the price is "startlingly low in relation to value" **[L2000-025]**
  on no basis shown.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
- **COMPUTATION, NOT A CLEARANCE.** The bond pays 5.66% with certainty; the central expected return at the price is
  6.2% pre-tax after the company's tax on a cyclical, levered stream (Q7), and 7.3% on the equity alone. "we are going
  to want to get a significantly higher return [...] than we are from a government bond" **[M2007-095]**; a margin of
  half a point to a point and a half over the bond is not that, and on the bond test alone the name is "taken out of
  the filter" **[M1997-089]**. The ranking against the best thing already held is not made: the blind rule keeps the
  holder's list closed to this run.
- **VERDICT (computation only): OUT.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
- **NOT REACHED.** The facts are under AFTER THE STOP, Q9. For the record of the rules under test: section H leaves the
  target's debt to be weighed on its own here; the criterion "Businesses earning good returns on equity while employing
  little or no debt" **[R1997-001]** is stated for whole businesses, and the facts recorded ($955M
  of floating-rate secured debt against a cycle-average of about $144M of unlevered owner cash) are what a run that
  reached this question would weigh.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
- **NOT REACHED.** The draft would have the buyer do nothing: "You wait for the fat pitch" **[M2003-070]**, and a
  pitch that is "just catching the lower outside corner" is one at which "If we swing, we will be locked into low
  returns" **[L1997-006]**. No position is taken here.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
- **NOT REACHED.** Not a named business; nothing found in the filings that the newspaper test would catch, and the
  Superfund matter (Q9 facts) is a legacy site named by the EPA among more than 100 parties, not a way the money is made.

---
## THE BOX
**OUT at Q2** (the castle: a commodity intermediary that is not the low-cost operator, whose price its rivals set and
whose durable position protects only ordinary returns over the last full cycle, section C). The Q7 COMPUTATION, NOT A
CLEARANCE, on the rules under test: central no-growth value $31.56 a share on the all-equity basis ($35.02 equity-only)
against $27.14, variants $19.62 to $61.90; fair price $10.23 all-equity, $19.82 equity-only; expected return at the
price 6.2% all-equity, 7.3% equity-only, below the floor. **Integrity facts recorded, not judged** (AFTER THE STOP, Q5).
Test record only; binds nothing.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Only when a STOP closed the file.)* Facts already found that bear on a later question, under the question each bears
on, each with its source **[M1997-127]**; written down, not weighed; no verdict; the box unchanged (operator rule 2).

**Q3, the capital.** (a) Tangible capital employed is inventory and receivables plus plant: about $1.1B of working
capital and $610M of PP&E against $4.6B of sales at 2025-12-31 (FY2025 10-K, 0001193125-26-062397); the business turns
its capital about two and a half times a year and earns a thin spread on it. (b) Operating income before interest on
average assets averaged 10.2% over FY2020 to FY2025 and 8.0% over FY2016 to FY2019, on the filer's own figures; after
interest, 6.7% and 3.7%. (c) Reinvestment to stand still: capital spending ran below depreciation every year 2014 to 2021
($21.6M to $59.3M against $42.5M to $58.4M of D&A, the 10-Ks' cash-flow statements) and above it in 2022 to 2024 ($105.1M,
$121.9M, $99.6M against $59.0M, $62.5M, $77.6M), then $51.5M against $79.7M in 2025; the filer gives no maintenance figure
and calls 2022 to 2024 "a historically high three-year investment cycle" (FY2025 10-K). The owner is entitled to the
manager's "best guess" of the maintenance need **[M2000-144]** and none is offered. (d) Cash paid for businesses, net:
$20.1M (2014), $8.8M, $1.1M, $50.3M, $169.7M (Central Steel & Wire, 2018), nil, nil, $14.5M, $57.0M, $137.8M (four
companies, 2023), $44.1M (Production Metals, 2024), nil (2025); the 10-Ks of each year. Tons sold were 2,025 thousand
before the first of them and 1,947 thousand after the last, so eleven acquisitions bought no net volume: "we're not
earning a higher rate of return on capital than we were when we started. We just put way more capital into the
business" **[M2023-081]** describes the figures. (e) Working capital is the cash trap of the rows: in the 2021 up-year
operating cash flow was $35.0M on $294.3M of net income, the profit "sitting in the yard" **[M2008-036]** as inventory
and receivables; in the 2020 down-year $277.9M came out on a $65.8M loss. The 10-K says so itself: "Working capital
needs tend to be counter-cyclical".

**Q4, the accounts.** (a) The balance sheets are read in Step 0. (b) Inventory is LIFO in the U.S. with a reserve of
$151M at 2025-12-31 (FY2025 10-K); the reserve swung from $(51)M in 2019 to $303M in 2021, so reported gross profit was
lowered by $56M of LIFO expense in 2025 and raised by $53M of LIFO income in 2024 (same filing). The inventory is not
"out of line" with sales **[M1995-064]** on a FIFO view (about $800M against $4.6B); the swings are price. (c) EBITDA in
the filer's own mouth: the 8-Ks feature "Adjusted EBITDA, excluding LIFO expense (income)" as "one of the primary metrics
management uses for planning and forecasting", and the pay plans are "based upon the achievement of pre-established
EBITDA, Adjusted EBITDA, and Adjusted EBITDA, excluding LIFO expense (income), targets" (8-K 0001193125-26-040024). The
rows' count of purchases "where people are talking about EBITDA, is going to be about zero" **[M2002-026]**, and the
adjusted figure regularly featured is the tell "makes us nervous" names **[L2016-006]**. (d) Guidance: the company
guides each quarter on revenue, margin, LIFO, net income and Adjusted EBITDA ex-LIFO, and in the fourth quarter of 2025
it missed its own guidance on all of them (net loss $37.9M against a guided loss of $7M to $9M; Adjusted EBITDA ex-LIFO
$20.4M against $33M to $37M; LIFO $22.5M against $10M to $14M; same 8-K). the rows call it "an offense that has been encouraged by the scourge of earnings" guidance "and the desire of CEOs
to" hit the number **[L2019-006]**; recorded here as the WEIGHING against **[M1994-018]** and carried to Q5. (e) The real costs: stock pay
$8.7M to $13.8M a year (2023 to 2025), restructuring and "reorganization expenses" adjusted out of Adjusted EBITDA every
year, $7.8M of merger advisory fees in Q4 2025, pension settlement charges of $64.6M in 2020 (FY2020 10-K,
0001564590-21-008111). (f) Net income has been negative in five of twelve years and operating cash flow positive in
eleven of twelve; the two tell different stories because of working capital, and the owner-cash recast in Q7 is after
the working-capital draw, as the rows' "whatever net cash is left every year" requires **[M1998-080]**. (g) Clear speech:
the MD&A explains the LIFO swings and the price lag in plain terms; the tons and price-per-ton tables have been given
every year since the IPO. (h) The merger's purchase accounting is preliminary and the filer says its adjustments "may be
material" (10-Q 0001193125-26-323769); $72.6M of intangibles were moved to PP&E and goodwill between the first and second
quarter allocations (same filing).

**Q5, the people (integrity facts recorded, not judged).** (a) Edward Lehner, CEO since June 2015, CFO from 2012; James
Claussen, CFO since 2021; the senior team averages "more than 30 years of experience" in metals (FY2025 10-K). (b) The
2026 proxy (DEF 14A 0001193125-26-114120) reports Mr. Lehner's 2025 total compensation at $17,857,908, of which stock
awards of $16,127,600 include a "special one-time, off-cycle grant of 600,000 RSUs" that cliff-vests after five years and
was made "for retention purposes and to align his total compensation with that of our Peer Group"; his 2024 total was
$4,963,050 and 2023 $6,476,248. (c) The say-on-pay vote fell from 93.7% for in April 2025 (26,806,616 for, 1,810,444
against; 8-K 0000950170-25-056771) to 64.4% for in April 2026 (29,296,410 for, 16,223,624 against; 8-K
0001193125-26-208963). (d) The 2023 PSUs paid 50% (the Adjusted EBITDA half at 100%, the free-cash-flow half at 0%) and
the 2024 PSUs are "currently projected to achieve a 0% payout", which the proxy attributes to "unexpected sluggish industry
demand" and "unprecedented years of declining metals prices" rather than to management (same proxy). (e) The merger
brought Olympic's executive chairman, Michael Siegal, in as Ryerson's Chair at $500,000 a year "in lieu of any other
board compensation", his son Zachary Siegal as Senior Vice President at a $525,000 base salary, and Olympic's CEO
Richard Marabito as President and COO at $975,000 base with a sign-on RSU award of up to $3,880,000, a car allowance,
tax-preparation fees and country-club dues; Mr. Siegal holds 50% of the partnership that leases a Cleveland warehouse to
Olympic (8-K 0001193125-26-051335; proxy as above). (f) The 2026 proxy's Platinum Equity reporting persons are disclosed
"based on information contained in a Schedule 13G/A filed with the SEC on February 12, 2024" (3,924,478 shares, 12.2% at
2025-12-31 and about 7.6% of the post-merger count); Platinum held 66% at the IPO, sold 1.6M shares to the company in
2022 and 2.9M in 2023 (FY2022 and FY2023 10-Ks), and one of its partners remains on the board. (g) The guidance habit and
the featured adjusted figure, carried from Q4. (h) How they talk about mistakes: the Q4 2025 miss is attributed to input
costs that "rose faster than anticipated" and "normal pricing reset timing" (8-K 0001193125-26-040024); the word mistake
does not appear. These are "things that they do in public in relation to their investors and the promises they make"
**[M2004-067]**; they are written down, not judged, and a later run that reaches Q5 must answer them **[M2013-088]**.

**Q6, the money and the owners.** (a) **The all-stock merger.** Ryerson paid for Olympic Steel wholly in its own shares
(1.7105 per Olympic share, about 19.5M shares, $527.3M at the closing price) and borrowed $270.0M to retire Olympic's
debt; the consideration was $837.3M (10-Q 0001193125-26-323769). On the day the agreement was signed Ryerson's shares
were $22.87 (8-K 0001193125-26-040024). The Q7 COMPUTATION below puts the central no-growth value of the merged company
at $31.56 a share on the all-equity basis, so the acquirer's shares were issued below that figure. Part A's one STOP
reads: "If shares of a prospective acquirer are selling below their intrinsic value, it's impossible for that buyer to
make a sensible deal in an all-stock deal" **[L2009-019]**. The fact is recorded; the deal is not weighed, and the
comparison the STOP needs is of the acquirer's own value before the merger, which this run did not compute. (b)
**Buybacks.** $1.8M at $22.39 (2021), $50.0M at $29.39 (2022), $113.9M at $35.00 (2023), $51.0M at $20.18 (2024), none in
2025; $38.4M of authorization remains and no price above which buying stops is stated (10-Ks FY2021 to FY2025). The
2023 purchases at $35.00 sit above the central no-growth value computed below ($31.56) and above every variant but
one; 2.9M of the 2023 shares were bought from Platinum. The rows read such a programme by the prices paid against
"intrinsic value, conservatively-calculated" **[L1999-023]** and find the announcement's silence on price
"puzzling" **[L2016-002]**. (c) **Dividends.** First paid in 2021 ($0.08 a quarter), raised every quarter to $0.1875
($0.75 a year; 8-K 0001193125-26-051335), which on 51.9M shares is about $39M a year against combined owner cash
averaging $103M over the last cycle (Q7). (d) **The retention test** over the cycle: equity rose from $139M (2020) to
$753M (2025) while $237M of stock was bought and $100M of dividends paid, almost all of it from the 2021 to 2022 price
spike; the per-share market value since then is not computed here (the blind rule and the no-other-price rule). (e)
**Pay tied to what the person controls** **[M2003-019]**: the PSUs vest on cumulative Adjusted EBITDA excluding LIFO and
a "Managerial Controllable Free Cash Flow" that adds back LIFO and working-capital changes; both move with the metal
price the proxy itself says management does not control. The incentive plan's share reserve was raised by 1,500,000
shares and extended to 2036 at the 2026 meeting (8-K 0001193125-26-208963). (f) **The board.** Eleven directors after the
merger, four of them from Olympic; the Chair is the seller's executive chairman, paid $500,000; a Platinum partner
(Jacob Kotzubei) drew 8.4M withheld votes of 45.6M cast in 2026 (same 8-K). (g) **Owners as partners**: quarterly
guidance, a featured non-GAAP figure, and a special grant explained by peer-group "market practices" are the facts; the
2026 say-on-pay result is the owners' own reading of them.

**Q9, the debt and exposures.** (a) Total debt $955.2M at 2026-06-30 ($962.0M drawn on the asset-based revolver plus
$2.6M foreign debt less issuance costs), net debt $913M, against $463.1M and $436M at 2025-12-31; the revolver's
commitments were raised from $1.3B to $1.8B and its maturity set at five years from 2026-02-13 (8-K 0001193125-26-051335;
10-Q 0001193125-26-323769). The whole of the borrowing is a floating-rate secured facility (4.9% at 2026-06-30) whose
availability is a borrowing base of receivables and inventory, which is to say it shrinks in the downturn when the
inventory and receivables it is secured on shrink. (b) The filer's own leverage ratio was 3.1x at 2025-12-31 "continuing
to approach Ryerson's target range of 0.5-2x" (8-K 0001193125-26-040024); after the merger it is higher, and the filer's
own history is of a company that carried $1.26B of 9% to 11.25% notes into 2014 and spent six years paying them down.
(c) Interest paid: $100.3M in 2014, $29.9M at the 2023 low, $41.2M in 2025; pre-tax income covered interest 1.9 times
on the FY2016 to FY2025 average of the filer's own figures, the rows' "pre-tax earnings/interest, not EBITDA/interest"
**[L2012-002]**. (d) Pension and retiree medical unfunded by $33.1M and $30.7M, minimum contribution about $11.4M in
2026 (FY2025 10-K). (e) Portland Harbor Superfund: JT Ryerson is one of more than 100 potentially responsible parties
for a remedy with "an estimated present value cost of $1.05 billion"; allocation "not anticipated until 2027";
management "cannot predict the ultimate outcome of this matter or estimate a range of potential loss" (FY2025 10-K,
Note 12). (f) Operating leases of $349M at 2025-12-31 are outside net debt and said so (rule under test, section H).
(g) Metals and currency derivatives are small and one to twelve months out (10-Q). These are the facts for "the capital
structure when somebody sticks a ton of debt into some business" **[M1997-009]** and for the maturities that "must
actually be met by payment" **[L2010-020]**; not weighed.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      Partly: the first session wrote nothing to the file before a timed limit stopped it, and the writing was done
      question by question in the second session (commits 15975dee Step 0, 44f2b39f Q1, 87dbae1b Q2, 8becc175 AFTER
      THE STOP, 27d83f77 Q7, and this one). The commits carry the run file alone: the protocol's pathspec names the
      working folder, which `.gitignore` line 117 ignores, and git refuses the pathspec ("did not match any file(s)
      known to git"); the folder's scripts (`fetch.py`, `series.py`, `compute.py`, `check.py`) and the fetched filings
      stay on disk, uncommitted.
- [x] If dispatched to an analyst: the brief allowed the per-question commits; the lock is the dispatcher's (not
      written by this run, as the protocol says); this is a test record and enters no register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule); the things
      seen by accident (two commit subjects, file names in the opening git status, `run.py`'s v4 lines) are declared
      under CONTAMINATION at the head of the file and not used.
- [x] Every v5 id resolves (87 distinct ids, checked by `check.py` against `principle_ledger_v5.csv`, and 21 quoted
      fragments checked against their rows); every filing fact has its accession; no number without a row or a filing
      except the two CONVENTIONS confessed in Q7 (the 25% tax rate on the interest add-back; Olympic's FY2025 taken as
      the twelve months to 2025-09-30).
- [x] The order was kept; Q2 closed the run; everything after it is headed NOT REACHED or COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority (US Treasury par yield curve); the price is an aggregator quote and is flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (the foundations paragraph: the 2025 share
      gain, Reliance's unbroken profitability); the facts for later questions are under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] No row dated after the anchor is cited: not a point-in-time run; the anchor is today.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS before every commit.
- [x] No em dash in the analyst's own prose (checked by `check.py`; the template's headings and the rows' own dashes
      inside quotation marks are not the analyst's).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Seven things. (1) **The brief's error.** It names Olympic Steel (ZEUS) as a rival to be read from its own filings and
describes the subject without naming the merger; Olympic has been a subsidiary of the subject since 2026-02-13 and filed
a Form 15 on 2026-02-23, and the canonical brief requires "any recent rename, merger or spin named". The run treats
Olympic's filings as the record of the business bought. (2) **Rule under test, section D(c), "A merger inside the
window."** The merger closed after the five-year window and before the price. The text does not say what to do with a
merger in that position; the run applied the combined-averages rule because the shares priced today are the merged
company's, and shows the Ryerson-alone basis beside it. The text should say "inside the window or between its end and
the price". (3) **Rule under test, section D(a), which series defines the cycle.** Owner cash in a working-capital
business runs against the cycle (the 2020 trough produced the most cash and the 2021 peak the least), so a trough
defined on owner cash would be a peak on volume and price. The run defined the cycle on the filer's own words about
prices and on operating profit per ton, and says so; the text should name the series. (4) **Rule under test, section
H, "as the filing states them".** Net debt is stated at two dates, $436M at 2025-12-31 and $913M at 2026-06-30; the
merger makes the choice worth $9 a share. The run took the later date because the share count is the later count; the
text should say the net debt is taken at the same date as the share count. (5) **Rule under test, section D(b), the
range when growth is meaningless.** "the range is the no-growth case alone" makes the central figure a point, and the
three-to-one width test then has nothing to measure; the run reported the spread across the stated variants and said
it is not a growth range. The text could say which variants bound the range in that case. (6) **The T2 protocol's
commit pathspec** names a folder that `.gitignore` ignores, so the command it gives cannot run as written; the run
committed the run file alone. (7) **The template's position note** asks the analyst to check `PORTFOLIO.md`, which the
blind rule forbids; the note was filled "not checked". A smaller point: section A's make-the-numbers habit is to be
"recorded at Q4" and "carried to Q5", but a file closed at Q2 has no Q4; the run put the habit under AFTER THE STOP,
Q4 and Q5, and the box line carries the flag, which seems to be what section G intends.
