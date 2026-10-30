# Company Run: Insight Enterprises, Inc. (NASDAQ: NSIT), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Every judgment
cites a v5 ledger id in bold; every filing fact carries its accession; the first STOP that failed closed the run and the
later questions are marked NOT REACHED. Copied from the template to this dated name before any fetch. Working folder:
`Test Runs/_research 2026-10-06 NSIT/` (fetch and arithmetic scripts, filing texts, tool output).

**POSITION NOTE, declared before any verdict:** not checked. The run was dispatched blind: `PORTFOLIO.md`, holding
reviews, the session-state file, the queue register and the reading list were not opened, so whether the operator holds
NSIT is unknown to this analyst.

**CONTAMINATION, declared.** No file about Insight was opened other than the filings. Seen without being sought: the
session-start git status listed untracked run files for POOL, ADT, GPOR and HRMY (2026-10-05 and 2026-10-06) and three
recent commit subjects with their verdicts (KTB TOO HARD (NATURE) at Q2; SBH OUT at Q2; AMN OUT at Q2); the memory
index carries a one-line queue summary ("57 gate-clearers, nothing buyable"). None names NSIT or a reseller peer. The
AMN, SBH and KTB subjects show that recent runs have closed at Q2; that is a base rate that could pull this analyst
toward the same close, and it is declared for that reason.

---
## STEP 0 - THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $159.39, close 2026-10-05, from the aggregator quote that `tools/run.py` prints (**aggregator, live quote
  only, flagged** under operator rule 5).
- **Shares:** one class, common stock $0.01 par, **29,348,850** on the cover of the 10-Q for the period ended
  2026-06-30, filed 2026-08-06, accession `0000932696-26-000070` (`python Screens/cover_shares.py NSIT`). The balance
  sheet at 2026-06-30 shows 29,515 thousand; the 10-Q reports 193,079 more shares bought after quarter end.
- **Market cap:** 29.349M x $159.39 = **$4,678M**. Net debt at 2026-06-30: long-term debt $1,475.1M less cash
  $363.5M = **$1,111.6M** (10-Q `0000932696-26-000070`), before $266.6M of inventory financing payables and the earnout
  liabilities. Enterprise value about $5,790M.
- **Sovereign, earnings currency USD:** **5.66%**, US Treasury daily par yield curve, 30-year, 10/05/2026 (issuing
  authority; fetched by `tools/sources.py` through `tools/run.py`). About 81% of 2025 net sales were in North America
  (10-K FY2025), so USD is the earnings currency.
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-12, `0000932696-26-000007`): Items 1, 1A, 5, 7, the
  statements and the acquisition notes; 10-Q Q2 2026 (filed 2026-08-06, `0000932696-26-000070`); DEF 14A (filed
  2026-04-02, `0000932696-26-000029`); 8-Ks of 2025-10-01 (`0000932696-25-000009`, Inspire11), 2025-11-14
  (`0000932696-25-000024`) and its 8-K/A of 2026-03-23 (`0000932696-26-000020`, new CEO, departures), 2025-12-17
  (`0000932696-25-000032`, buyback authorisation), 2025-12-19 (`0000932696-25-000035`, ABL to $2.0B), 2026-05-13
  (`0000932696-26-000057`, annual meeting votes), 2026-05-28 (`0000932696-26-000063`, ABL amendment), 2026-02-05 and
  2026-08-06 (earnings furnishings, cover pages only). History: 10-K FY2024 (`0001628280-25-005817`), FY2023
  (`0001628280-24-006391`), FY2022 (`0001628280-23-003850`), FY2019 (`0001564590-20-005741`), FY2016
  (`0001193125-17-048059`), FY2013 (`0001193125-14-062744`), FY2010 (`0000950123-11-017134`), FY2008 (filed late,
  2009-05-12, `0001362310-09-007124`, the aged-trade-credit restatement) and FY2006 (filed late, 2007-07-26,
  `0000950153-07-001566`, the option-dating restatement).
- **Cross-check against the filed statement:** operating cash flow 2025 is $303,827 thousand on the filed cash-flow
  statement (10-K FY2025) against $303.8M in the tool; goodwill $1,169,734 thousand against $1,170M; total assets
  $9,087,372 thousand against $9,087M. All agree.
- **`tools/run.py NSIT`, arithmetic lines only** (its v4 rule text, its three-year "owner earnings" window and its
  "growth the price assumes" line were not used; Part VII). Owner cash after every real cost, computed here from the
  filed cash-flow statements, USD millions; OE capex = OCF - SBC - capital spending, OE D&A = OCF - SBC - D&A:

| year | OCF | SBC | capex | D&A | OE capex | OE D&A | net income | acquisitions | buybacks |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 96.1 | 11.1 | 12.3 | 38.1 | 72.7 | 46.9 | 84.7 | 10.8 | 50.0 |
| 2017 | -307.1 | 12.8 | 19.2 | 42.6 | -339.1 | -362.5 | 90.7 | 186.9 | 0 |
| 2018 | 292.6 | 15.4 | 17.3 | 37.5 | 259.9 | 239.7 | 163.7 | 74.9 | 22.1 |
| 2019 | 127.9 | 16.0 | 69.1 | 46.2 | 42.8 | 65.7 | 159.4 | 664.3 | 27.9 |
| 2020 | 355.6 | 17.7 | 24.2 | 65.6 | 313.7 | 272.3 | 172.6 | 6.4 | 25.0 |
| 2021 | 163.7 | 18.2 | 52.1 | 55.4 | 93.4 | 90.1 | 219.3 | 0 | 50.0 |
| 2022 | 98.1 | 22.7 | 70.9 | 56.6 | 4.5 | 18.8 | 280.6 | 68.2 | 107.9 |
| 2023 | 619.5 | 29.0 | 39.3 | 62.5 | 551.2 | 528.0 | 281.3 | 481.5 | 217.1 |
| 2024 | 632.8 | 34.0 | 46.8 | 98.1 | 552.0 | 500.7 | 249.7 | 270.2 | 200.0 |
| 2025 | 303.8 | 33.7 | 24.5 | 106.3 | 245.6 | 163.8 | 157.3 | 285.3 | 151.1 |

  Five-year mean (2021-2025): OE capex **$289.3M**, OE D&A **$260.3M**. Ten-year mean (2016-2025): OE capex
  **$179.7M**, OE D&A **$156.3M**. Sources: XBRL first-filed vintage, accessions listed by `tools/run.py`
  (`Test Runs/_research 2026-10-06 NSIT/run_py_output.txt`); 2023-2025 read on the FY2025 statement. No securities
  purchases, no capitalised software line beside capex (tool's linkbase read). Stock pay is complete in the SBC line
  (the equity statement's "Stock-based compensation expense" equals it each year). **Operating cash swings with the
  working capital of a reseller**: operating cash over net income ran from -3.39 (2017) to 2.53 (2024); 2023 and 2024
  were releases (OCF 2.2 and 2.5 times net income) and 2017 an absorption of $307M. The filer says why: "We have an
  inverted cash cycle resulting from typically paying partners on shorter terms than we provide to our clients. This
  generally means in periods of growing hardware sales, we typically use cash from operations." (10-K FY2025, MD&A,
  `0000932696-26-000007`). The first half of 2026 shows it again: OCF $20.1M on net earnings $107.6M as receivables
  rose $2,394M (10-Q `0000932696-26-000070`). Acquisitions are capital: $2,048.5M over 2016-2025 against $1,796.7M of
  owner cash (capex basis) in the same ten years, plus $56M of earnout payments in financing (2023-2025) and the
  $222.0M warrant settlement of 2025.

**The balance sheets, read before the income account** **[M2025-032]** ("balance sheets over an 8 or 10 year period
before I even look at the income account"). Ten year-ends from `tools/run.py` (first-filed XBRL), with the FY2025
and Q2 2026 statements read directly; USD millions:

| year-end | equity | goodwill | intangibles | tangible equity | receivables | AP-trade (filed) | debt | retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2016 | 713 | 63 | 21 | 629 | 1,437 | | 41 | 460 |
| 2017 | 843 | 131 | 101 | 611 | 1,815 | | 313 | 550 |
| 2018 | 987 | 167 | 112 | 708 | 1,932 | | 197 | 705 |
| 2019 | 1,160 | 415 | 279 | 466 | 2,511 | | 859 | 841 |
| 2020 | 1,342 | 429 | 247 | 666 | 2,685 | | 439 | 993 |
| 2021 | 1,509 | 428 | 215 | 866 | 2,937 | | 362 | 1,168 |
| 2022 | 1,638 | 493 | 205 | 940 | 3,272 | | 638 | 1,369 |
| 2023 | 1,736 | 684 | 370 | 682 | 3,568 | | 941 | 1,448 |
| 2024 | 1,771 | 894 | 426 | 451 | 4,172 | 3,060 | 864 | 1,509 |
| 2025 | 1,649 | 1,170 | 426 | **53** | 5,517 | 4,264 | 1,361 | 1,520 |
| 2026-06-30 | 1,605 | 1,166 | 384 | **55** | 7,816 | 6,520 | 1,475 | 1,487 |

What the figures say. (1) **Tangible equity has gone from $629M to about $53M in nine years while book equity more than
doubled**: every dollar of book growth and more is goodwill and intangibles from acquisitions (PCM 2019 $664M; SADA
2023 about $400M plus up to $390M of earnout; Infocenter 2024 $265M; Inspire11 and Sekuro 2025 $285M). (2) **Debt rose
from $41M to $1,475M**, to fund those purchases, the 2025 maturity of the convertible notes ($333.1M) and the cash
settlement of the call-spread warrants ($222.0M), and buybacks ($851M over ten years). (3) **The business runs on its
suppliers' money**: receivables of $7.8B against trade payables of $6.5B at 2026-06-30, plus long-term receivables of
$699M matched by long-term payables of $620M (multi-year software contracts carried through). Receivables have run
from 26% of net sales (2016) to 67% (2025); the filer explains that agency transactions are booked net in sales but
gross in receivables and payables ("netted costs were $4.0 billion and $2.2 billion in the fourth quarter of 2025 and
2024", 10-K FY2025 MD&A), so the sales line no longer measures the balance sheet it carries. (4) **The convertible's
true cost bypassed the income statement**: additional paid-in capital fell from $342.9M to $164.6M in 2025, of which
$196.9M was "Settlement upon exercise of Warrants" charged to equity (statement of stockholders' equity, 10-K FY2025);
only $25.1M passed through earnings as a revaluation loss. (5) Of $358.0M of year-end 2025 cash, $306.6M sat in
foreign subsidiaries (10-K FY2025, Undistributed Foreign Earnings). (6) Retained earnings rose $1,060M over 2016-2025
against cumulative net income of $1,859M, the gap being buybacks retired through retained earnings. What they cannot
say: how much of the receivables and payables is principal business and how much agency pass-through in any year
before 2023; the filer gives the netted-cost figure only for recent fourth quarters.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what Insight's business will earn, not what the quotation will do; the price
rose from the $93.18 average the company itself paid in the first half of 2026 (10-Q) to $159.39, and the quotation
"just tells us prices." **[M2006-077]**. Margin of safety: a case that needs a spreadsheet to clear is
"it’s too close to think about" **[M1996-084]**. The analyst's habits: scuttlebutt and the reading are aimed "to
possibly reject your original hypothesis" **[M1998-144]**, and the anchor to resist is "always your previous
conclusion" **[M2016-054]**; here the anchor to resist is the base rate of recent Q2 closes (contamination note above).
**Contrary evidence, written down as found** (Darwin's rule, to "write it down in the first 30 minutes" **[M1997-127]**):
(a) gross profit grew from $339.7M (2004, FY2008 10-K selected data) to $1,761.4M (2025), and earnings from operations
from $63.8M to $334.9M; (b) services were 59% of gross profit in 2025 against 49% in 2022, and the filer expects margin
to keep rising with services; (c) the first half of 2026 shows gross profit up 16% and earnings from operations up 38%
year over year (10-Q); (d) the reseller has survived thirty-seven years, two restatements and the shift to cloud; (e)
return on tangible capital looks high (EBIT of $335M on tangible equity plus net debt of about $1.17B), because suppliers
finance the working capital; (f) ePlus and CDW, peers in the same trade, earn steady returns, so the trade itself is not
a loser for everyone. Each is weighed at Q2 below.

## THE STANDING RULE
Owning this unlevered, at a size the buyer can hold through a halving, carries no ruin to the buyer; the rule binds the
buyer's financing, "We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]**, and "borrowed money has no place in the investor's tool kit" **[L2014-005]**. No conflict for a cash
purchase. (The target's own debt is Q9's, not reached.)

---
## Q1 - CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The question:** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power
  and competitive position will look like in five or 10 years" **[M2012-065]**.
- **What the business is, from the 10-K FY2025 (`0000932696-26-000007`):** a reseller and integrator of other firms'
  hardware, software and cloud. 2025 net sales $8,247M: North America 81%, EMEA 16%, APAC 3%. Products 79% of net sales
  and 41% of gross profit; services (cloud fees booked net, Insight-delivered services, warranties, agency fees) 21% of
  net sales and 59% of gross profit. Purchases from over 6,000 partners; Microsoft 32% and TD Synnex 12% of purchases;
  Microsoft products 17% of net sales; the top five manufacturers 50% of net sales. No research and development group.
- **The key variables:** (1) the spread a reseller earns on hardware and software sold in competition; (2) the partner
  funding and cloud fees the vendors pay, which the filer says "can and do change significantly in the amounts made
  available and the requirements year over year" (Item 1A); (3) the volume of client IT spending and the hardware
  refresh; (4) services gross profit, much of it bought; (5) working capital, financed by suppliers.
- **The test applied.** The economic dynamics of the trade can be read without forecasting any technology, which is what
  the rows ask: "What is important is that I understand the economic dynamics of the industry." and "Is there ease of
  entry?" **[M2011-014]**. The dynamics are written in the
  filer's own risk factors in the same words every year since at least 2008: competition "based on price, product
  availability, speed of delivery, credit availability", suppliers who also sell direct, partner incentives set by the
  partner, and competitors with "lower operating cost structures" (10-K FY2008 `0001362310-09-007124` through FY2025
  `0000932696-26-000007`). That is a fix on the competitive position: an intermediary between vendors who set its
  incentives and clients who buy on price. What I cannot foresee is the level of any one vendor's incentive programme in
  2036; but the question the rows ask at Q1 is whether the economics and the position can be foreseen at all, and the
  position has been the same for seventeen years of filings, so the forecast that decides the case is about structure,
  not technology.
- **Routing considered, and why not TOO HARD here.** The IT industry changes fast, and the filer says so ("The IT
  industry is characterized by rapid technological change and the frequent introduction of new products and changing
  delivery channels and models", Item 1A). The rows send a business to TOO HARD at Q1 when change puts its ten-year
  economics out of reach: "a business that must deal with fast-moving technology is not going to lend itself to reliable
  evaluations of its long-term economics" **[L1993-023]**; "where we think the future technology could hurt the business
  as it presently exists" **[M1998-008]**. For a reseller the technology changes what is resold, not the reseller's
  economics: across PCs, client-server, on-premise licences and cloud, the filings show the same thin spread (earnings
  from operations 1.9% to 4.6% of net sales in every year 2004-2025 except 2008's impairment year). The forecast is
  "about customers" and suppliers rather than about technology, the distinction drawn in "as opposed to, say, IBM’s
  customers, it’s a different sort of analysis" **[M2017-019]**. The doubt that remains is whether this intermediary
  keeps its place, which is Q2's question, not a doubt about understanding: the rule "if you have doubts about something
  being into your circle of competence, it isn’t." **[M2002-092]** is applied to the understanding, and the understanding
  is not in doubt.
- **VERDICT: IN**, narrowly, on **[M2011-014]** and **[M2012-065]**, with the filer's own risk factors as the filing
  fact. Contrary reading recorded: a second analyst could close here TOO HARD (NATURE), reading the cloud vendors' direct
  sales as change "9 times out of 10, we’re going to pass on that" **[M1999-063]**; the framework's routing paragraph
  does not separate a vendor's channel policy from a technology forecast (see the last section).

## Q2 - WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" **[M1995-038]**, asked from the attacker's side, since "most moats
aren’t worth a damn" **[M1995-038]**.

**The tests, each with its filing fact.**
1. **The money test.** Could a well-funded attacker take it? "If the answer had been yes, we wouldn’t have done it."
   **[M2011-015]**. The attackers are already inside, by the filer's own list: "Systems integrators and digital
   consultants such as Accenture, Capgemini, Atos, HCL Technologies, Tata Consultancy Services and Infosys; and [...]
   Technology providers, value-added resellers and direct marketers such as CDW, Presidio, World Wide Technology, SHI
   and Computacenter", and "We sometimes compete directly with publisher and manufacturer partners [...] including
   Microsoft, Cisco Systems, Dell, HP Inc. and Adobe Systems" (10-K FY2025, Item 1). The trade has no barrier the filer
   names; the rows on such trades: "there are some industries that are just never going to have barriers to entry"
   **[M2012-106]**. Fails.
2. **Pricing power.** The filer: "Generally, pricing competition is very aggressive in the industry, and we expect
   pricing pressures to continue." (Item 1A, FY2025). The rows' measure is the agony before a rise, "a prayer session
   before you raise your prices a penny" **[M2005-020]**; Insight does not set its price at all. Product gross margin was
   9.4% (2020), 9.1%, 9.3%, 10.1%, 10.8%, 10.9% (2025) while product gross profit dollars fell from $836.5M (2022) to
   $714.7M (2025) (statements of operations, 10-K FY2022 `0001628280-23-003850` and FY2025). Fails.
3. **Who sets the price.** The supplier sets the services half of the profit: partner funding and cloud fees "can and do
   change significantly", "We regularly experience partner funding program changes that reduce the incentives many
   partners make available to us", and "recent changes in incentives for certain cloud-based solutions adversely
   impacted our results of operations in 2025" (Item 1A and MD&A, FY2025). The SADA purchase (Google Cloud, December 2023,
   about $400M cash) carried an earnout of up to $390M; the maximum still open fell to $240M at the end of 2024 and $120M
   at the end of 2025 with no SADA earnout paid (10-K FY2024 `0001628280-25-005817`, FY2025). The rows' case of a
   business whose price another sets: "whatever he charged for gas was my price" **[M2012-109]**; "he determined our
   profit, because we looked at his price every day" **[M2023-079]**. Here the competitor sets the product spread and
   the supplier sets the fee. Fails.
4. **Would the customer still choose it over the low bid?** The filer: "Competition in the industry is based on price,
   product availability, speed of delivery, credit availability, quality and breadth of product lines, and,
   increasingly, on the ability to provide services" (Item 1A, FY2025). The client buys the vendor's product, not
   Insight's: the rows' failing answer is the customer who does not care whom he buys from, "most insureds don't care
   from whom they buy" **[L2004-003]**, against the test "it wouldn’t be a question of people buying candy for the low
   bid" **[M2017-009]**. No filing fact shows a client paying Insight more than a rival for the same Dell laptop or
   Microsoft licence. Fails.
5. **The low-cost position, the one way through a commodity field.** "Another way to prosper in a commodity-type
   business is to be the low-cost operator." **[L2004-007]**; "when a company is selling a product with commodity-like
   economic characteristics, being the low-cost producer is all-important" **[L2000-017]**. **The single fact:** the
   filer has written in every 10-K from FY2008 to FY2025 that "some of our competitors have higher margins and/or lower
   operating cost structures, allowing them to price more aggressively" (found verbatim in the FY2008, FY2010, FY2013,
   FY2016, FY2019, FY2022 and FY2025 10-Ks; script and output in the working folder). The competitors' own filings
   confirm it over the whole span (competitor row below): Insight converted 21.4% of its gross profit into operating
   earnings over 2010-2025, against 35.2% at CDW, 30.2% at TD SYNNEX and 27.9% at ePlus, and it trailed all three in
   every single year. The rows: "commodity businesses have risk unless you’re the low-cost producer, because the
   low-cost producer can put you out of business" **[M1997-010]**; "In an unregulated commodity business, a company must
   lower its costs to competitive levels or face extinction." **[L1994-035]**; "the guy with the lower cost comes in and
   kills you" **[M2001-013]**. Fails, on the evidence.
6. **Brand and share of mind.** Insight sells others' brands; the filer says "brand names and individual products are
   important to our business" of the vendors' brands (Item 1, FY2025). No instance found in the filings read of a client
   asking for Insight by name. Fails as a moat; not a weakness by itself.
7. **Ask the competitors.** "which one would it be and why?" **[M1999-130]**. No competitor's statement about Insight is
   on the public record read (CDW's, TD SYNNEX's and ePlus's 10-Ks were read for figures, not for such statements).
   Recorded as no instance found; not used.
8. **Widening or narrowing.** "whether it’s likely to widen further or shrink on you" **[M1999-108]**; the position
   "grows either weaker or stronger" **[L2005-010]**. Earnings from operations were $419.8M (2023), $388.6M (2024),
   $334.9M (2025) while $1,037M was spent on acquisitions in those three years (statements of operations and cash flows,
   FY2025); gross profit was $1,669.5M, $1,766.0M, $1,761.4M, flat with the bought services added. The share of gross
   profit kept as operating earnings fell from 25.3% (2022) to 19.0% (2025). The first half of 2026 recovered (earnings
   from operations $202.6M against $146.6M, 10-Q). Over the long span the ratio drifted up from about 19% (2010-2016) to
   23% (2022-2025) and then back down; the gap to CDW did not close in any year. Narrowing over the last three years,
   flat over sixteen.
9. **What could hurt it**, in the row's words what could "destroy, or modify, or reduce the economic strengths"
   **[M2000-014]**: the filer names it, "cloud-based solutions and
   technologies developed by manufacturer and publisher partners are alternatively marketed directly to customers
   without utilizing solutions providers like us, which can reduce the volume of hardware, software or services we
   sell" (Item 1A, FY2025). Software net sales in North America fell 27% in 2025, "primarily due to a significant
   multiyear transaction in the first quarter of 2024 with no comparable transaction in 2025, changes in certain vendor
   relationships (shifting us from a principal to an agent role), as well as the continued migration of on-premise
   software to cloud solutions" (MD&A, FY2025). The supplier that is 32% of purchases is also a direct seller. One such
   attacker can be enough: "one competitor is frequently enough to ruin a business" **[M2012-108]**.

**The competitor row, same metric from the competitors' own filings.** The metric is operating income divided by gross
profit, because gross profit is untouched by the gross-to-net reclassifications that make every peer's sales line
incomparable over time (Insight's own sales fell 21% from 2022 to 2025 partly for that reason, MD&A FY2025). Gross margin
on sales is shown for completeness. Operating income is GAAP, after stock pay, amortization and restructuring, for all
four; CDW's figure carries heavy amortization from its 2007 buyout, which understates its advantage. Annual 10-K XBRL,
first-filed vintage (script `peers/comp.py`, output reproduced):

| year | NSIT GM / op% / op÷GP | CDW GM / op% / op÷GP | TD SYNNEX GM / op% / op÷GP | ePlus GM / op% / op÷GP |
|---|---|---|---|---|
| 2010 | 13.4 / 2.6 / 19.2 | 15.8 / 4.0 / 25.4 | 5.7 / 2.3 / 40.5 | - |
| 2013 | 13.6 / 2.4 / 17.3 | 16.3 / 4.7 / 28.9 | 6.0 / 2.2 / 36.8 | 20.8 / 6.0 / 28.7 |
| 2016 | 13.5 / 2.7 / 20.0 | 16.6 / 5.9 / 35.2 | 9.1 / 2.7 / 29.6 | 21.8 / 6.3 / 28.9 |
| 2019 | 14.7 / 3.1 / 21.1 | 16.9 / 6.3 / 37.3 | 12.2 / 3.4 / 28.1 | 24.1 / 5.8 / 24.1 |
| 2022 | 15.7 / 4.0 / 25.3 | 19.7 / 7.3 / 37.0 | 6.3 / 1.7 / 26.9 | 25.3 / 8.1 / 32.0 |
| 2023 | 18.2 / 4.6 / 25.1 | 21.8 / 7.9 / 36.1 | 6.9 / 1.9 / 27.2 | 25.0 / 8.0 / 32.1 |
| 2024 | 20.3 / 4.5 / 22.0 | 21.9 / 7.9 / 35.9 | 6.8 / 2.0 / 30.0 | 24.8 / 7.1 / 28.7 |
| 2025 | 21.4 / 4.1 / 19.0 | 21.7 / 7.4 / 34.0 | 7.0 / 2.3 / 32.4 | 27.5 / 6.8 / 24.8 |
| **sum 2010-2025, op ÷ GP** | **21.4%** | **35.2%** | **30.2%** | **27.9%** (2013-2025) |

Every year 2010-2025 is in `Test Runs/_research 2026-10-06 NSIT/peers/comp.py`'s output; Insight is lowest of the four
in each year. Sources: CDW 10-K FY2025 `0001402057-26-000011` (series from `0001402057-12-000006`); TD SYNNEX 10-K FY2025
`0001628280-26-003598` (series from `0001177394-12-000006`; a distributor, and its 2021 merger with Tech Data changes its
mix); ePlus 10-K FY ended March 2026 `0001140361-26-023171` (series from `0001022408-15-000017`; includes a small
financing arm). Before XBRL, Insight's own selected data (10-K FY2008): operating earnings over gross profit 18.8%
(2004), 18.2%, 19.0%, 17.3%, and 14.0% in 2008 before the $397.2M goodwill impairment. **SHI**: private, no filings;
not compared (flagged). **Softchoice**: filed in Canada, not with the SEC; not retrieved, not compared (flagged).

**The contrary evidence, weighed.** (a) Growth in gross profit and operating earnings is real but bought: $2,048.5M of
acquisitions over 2016-2025 against $1,796.7M of owner cash, and operating earnings rose $186.1M from 2016 to 2025, about
9.1% pre-tax on the acquisition money alone before any organic growth is credited (COMPUTATION). The rows on growth that
consumes capital: "whether that’s good or bad depends on what we earn on that incremental $130 million over time"
**[M2001-019]**. (b) The services shift raises gross margin but the share kept as operating earnings did not rise with
it after 2022. (c) The 2026 rebound is two quarters against a sixteen-year record. (d) Survival is not a castle: a
reseller can survive as a high-cost operator for decades, and the rows count that as a business, not a moat ("We’re
going to be investors in businesses, not commodities, by and large." **[M2007-131]**). (e) The high return on tangible
capital comes from suppliers' credit and acquired goodwill excluded from the base, which is the leverage the rows tell
the analyst to strip out, and is in any case Q3's question. (f) CDW's and ePlus's steady returns show the trade rewards
the low-cost operator; they are the evidence against Insight, not for it.

**Why OUT and not TOO HARD.** The castle's future is not unjudgeable; it is judged on the evidence. The framework's Q2
list of what it rules OUT names the high-cost producer in a commodity field and the business whose price a competitor
sets, on the rows quoted at tests 3 and 5 above; TOO HARD is for a moat whose value cannot be reckoned, "We don’t know
how to valuate that" **[M2000-019]**. Here the one single fact the OUT answer needs is on file
in the company's own words for seventeen years and in the competitors' statements for sixteen. The rows' three boxes,
"in, out, and too hard" **[M2006-013]**: this is out. Price does not reopen it: "What you can’t do is turn any investment
into a good deal by paying little" **[M2019-015]**.

- **VERDICT: OUT.** A commodity intermediary that is not the low-cost operator, whose product spread is set by
  competitors and whose fee income is set by its largest supplier, which is also a direct competitor.

## Q3 - HOW MUCH CAPITAL MUST GO IN. NOT REACHED.
## Q4 - DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED as a question (the balance sheets were read in Step 0).
## Q5 - WHO RUNS IT. NOT REACHED.
## Q6 - WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.

**Facts read for the questions not reached, recorded and not judged** (so a later reader need not fetch them again):
- **Accounting history.** FY2006 10-K, filed late with a restatement after an Options Subcommittee review of grants
  1995-2005: "during a portion of the period under review, the Company retrospectively selected dates for anniversary
  grants and promotion grants based on the lowest price in a particular period"; $30.9M of incremental compensation net
  of tax (`0000950153-07-001566`). FY2008 10-K, filed late with a second restatement: aged trade credits from "unclaimed
  credit memos, duplicate payments, payments for returned product or overpayments made to us by our clients" had been
  taken into income before the legal discharge of the liabilities, December 1996 to September 2008, cumulative charge
  $61.2M pre-tax; a material weakness; an SEC inquiry (`0001362310-09-007124`). The co-founder who was an executive
  through 2004, Timothy A. Crown, has been a director since 1994 and is the Board's "independent Chair" in the 2026 proxy.
- **Adjusted figures.** Adjusted earnings from operations ($504.0M in 2025) excludes, among others, restructuring
  ($37.1M 2025, $31.6M 2024), "transformation costs" ($13.1M, $18.4M, "not expected to recur in the longer term"),
  amortization of acquired intangibles ($76.8M) and earnout revaluations; GAAP earnings from operations were $334.9M.
  The same adjusted figure is "a basis for executive variable compensation" (10-Q) and the cash-incentive measure in the
  proxy (target $527.7M, actual $504.0M, 85.0% payout), with "non-GAAP Adjusted ROIC" (15.15% adjusted against 10.07%
  from GAAP EFO) driving the performance shares (DEF 14A `0000932696-26-000029`). The rows' reading of the habit, for
  the reader who reaches Q4: a management "that regularly attempts to wave away very real costs" by highlighting
  adjusted earnings "makes us nervous" **[L2016-006]**.
- **People and pay.** CEO Joyce Mullen (pay $10.5M in 2025) retired; Jack Azagury, from TowerBrook Capital Partners'
  advisers, became CEO on 2026-04-13 with $1.1M salary, $1.65M target bonus, $1.0M relocation bonus and $18.0M of equity
  (8-K/A `0000932696-26-000020`); the North America president and the general counsel left in March 2026. One-time
  "retention and continuity" awards were granted in December 2025 to four executives after a year in which GAAP earnings
  fell 37%. Directors and officers as a group hold 1.21%; at the 2026 meeting four directors received 11% to 14% of
  votes against (8-K `0000932696-26-000057`). In 2025 the company bought 600,000 shares privately from ValueAct Capital,
  "a former affiliate", for $76.1M (10-Q).
- **Capital returns.** Buybacks $151.1M (2025) and $150.0M in the first half of 2026 at an average $93.18, then $23.2M at
  $120.38 after the quarter; the authorisation names no price (8-K `0000932696-25-000032`). Shares outstanding fell from
  about 46M diluted (2009) to 29.3M. No dividend.
- **Debt.** ABL facility raised to $2.0B (December 2025), $868.2M drawn at year-end 2025; $500M senior notes due 2032;
  covenants include a minimum receivable and inventory requirement; inventory financing $266.6M; earnouts outstanding up
  to $120M (SADA, 2026), $66M (Inspire11), AUD 122.5M (Sekuro) (10-K FY2025, 10-Q).

## Q7 - WHAT IS IT WORTH? NOT REACHED. Owner's reporting below.

### COMPUTATION - NOT A CLEARANCE
*(The file closed OUT at Q2. Nothing below is a clearance, a ranking or entry language; it is the arithmetic the owner
asked to see, built by the Q7 convention as if the question had been reached.)*

Method, as the convention states it: owner cash after every real cost, "a figure calculated after interest, taxes,
depreciation, amortization and all forms of compensation" **[L2021-003]**, averaged over five years, carried at the
growth shown and then at no growth, discounted at the long government rate, "What is the risk-free interest rate (which
we consider to be the yield on long-term U.S. bonds)?" **[L2000-021]**, held as a range because "working with a range of
possibilities is the better approach" **[L2000-024]**. Rate 5.66%; shares 29.349M.

**(a) VALUE RANGE.**
- **Five-year window (2021-2025).** Base $260.3M (D&A basis) to $289.3M (capex basis). Growth shown: the aggregate owner
  cash series (93.4, 4.5, 551.2, 552.0, 245.6) has no readable rate, its ends set by working-capital swings, the case
  the rows warn of, "a base year in which earnings were poor can produce a breathtaking, but meaningless, growth rate"
  **[L2005-003]**; the steadier figure the cash comes from, earnings from operations, went from $332.1M (2021) to
  $334.9M (2025), **0.2% a year**, and that rate is used. Range: **$157 (D&A basis, no growth) to $177 (capex basis,
  0.2% for ten years, then none)**. The width is about 1.1 to 1. The price, $159.39, sits inside it.
- **Whole-cycle variant (2016-2025),** owed because the five-year window holds two abnormal years (2023 and 2024
  operating cash at 2.2 and 2.5 times net income, working-capital releases) and the decade holds the opposite swing
  (2017, -$307M). Base $156.3M (D&A) to $179.7M (capex). Range at no growth: **$94 to $108**. Growth: earnings from
  operations grew 9.4% a year 2016-2025, but every dollar of it came with acquisitions larger than the decade's owner
  cash ($2,048.5M against $1,796.7M), so no growth is credited without its price, the rows' warning that "growth can
  destroy value if it requires cash inputs in the early years" **[L2000-023]**. For information only, the same base
  grown free at 9.4% for ten years would give $228, a ceiling that assumes the acquisitions cost nothing.
- **Closes, had Q7 been reached:** OUT under the convention (narrow range, price inside it, not a screamer); the
  expected pre-tax return at the price is below the floor (next item).

**(b) FAIR PRICE** (the price at or below which the central case clears about 10% pre-tax, the speakers' own figure,
"a very high probability of at least 10% pre-tax returns" **[L2002-020]**, applied as the framework's CONVENTION).
- **Central case:** the midpoint of the five-year and whole-cycle owner cash on the capex basis, $234.5M after tax.
  CONVENTION of this run: neither window alone is the business's normal cash, because the five-year mean carries the
  two releases and the ten-year mean carries a business half its present size; the midpoint is the least-chosen figure
  between them.
- **Tax treatment:** owner cash is after tax; it is grossed up at 25% to a pre-tax figure (the effective rate was 25.5%
  in 2023 and 25.0% in 2024; 2025's 30.3% carried non-deductible warrant and earnout losses; CONVENTION, the filed
  effective rate of the two clean years). Pre-tax $312.7M.
- **Floor on equity:** owner cash is after interest, so the 10% is set against the market value of the equity, not
  equity plus net debt. Fair equity value $3,127M, **fair price about $107 a share**.
- **Cross-check on equity plus net debt:** five-year mean GAAP earnings from operations $377.8M (pre-tax, before
  interest, after stock pay and amortization) at 10% gives an enterprise value of $3,778M, less net debt $1,111.6M,
  $2,667M equity, **about $91 a share**. The two bases bracket a fair price of **$91 to $107**.
- At $159.39 the pre-tax yield is 8.25% on the five-year owner cash and 5.12% on the ten-year; earnings from operations
  are 6.53% of enterprise value. All below the floor, "a point at which we drop out of the game" **[M2003-149]**.

**(c) CHEAP PRICE** (below which no pencil is needed). Rule, CONVENTION of this run: the price at which even the bottom
of the whole-cycle range is at least twice the price, so that the margin needs no arithmetic, "It should scream at you."
**[M2009-005]**. Bottom of the whole-cycle range $94.12, so **cheap price about $47 a share**. (On the central case at a
20% pre-tax yield the figure would be $53; the lower is reported.)

**Against the price:** $159.39 is above the fair price ($91 to $107) by half or more, inside the five-year range
($157 to $177) and above the whole-cycle range ($94 to $108), and more than three times the cheap price.

## Q8 - IS IT BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 - COULD IT RUIN US. NOT REACHED (the debt facts are recorded above).
## Q10 - IS IT THE FAT PITCH. NOT REACHED.
## Q12 (optional) - WOULD WE BE PROUD OF HOW THE MONEY IS MADE. NOT ASKED. (No named business; an IT reseller.)

---
## THE BOX
**OUT, at Q2.** A commodity intermediary that is not the low-cost operator: the filer has said in every 10-K since
FY2008 that competitors have "lower operating cost structures", and over 2010-2025 it kept 21.4% of its gross profit as
operating earnings against 35.2% at CDW, 30.2% at TD SYNNEX and 27.9% at ePlus, lowest of the four in every year; its
fee income is set by Microsoft and the other vendors, which also sell direct. COMPUTATION, not a clearance: value range
$157 to $177 (five-year) and $94 to $108 (whole-cycle) against $159.39; fair price $91 to $107; cheap price about $47.
No research pass is owed (the close is OUT, not TOO HARD (WORK)).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. [ ] **Written question by question and committed after each: NO.** The
      file was copied first and then filled in one pass after the reading, and nothing was committed, by instruction.
      The write-early protocol was not kept; declared.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, below); every filing fact has its document
      and accession; every number carries a filing, the tool output, or a CONVENTION label.
- [x] The order was kept; Q2 closed the run; Q3 to Q10 are NOT REACHED; the valuation is headed COMPUTATION and carries
      no entry language.
- [x] Owner cash from the cash-flow statements after stock pay and all capital spending, with the D&A variant; no
      net-income proxy (net income shown only as a comparison column). Sovereign from the US Treasury. Aggregator quote
      flagged.
- [x] Contrary evidence written down as found (Foundations, and weighed at Q2).
- [x] Not a point-in-time run; no anchor date applies.
- [x] Only the arithmetic lines of `tools/run.py` used; its three-year window, its v4 wording and its "growth the price
      assumes" line set aside.
- [x] `python tools/check_framework.py` run before handing back (result reported in the reply; no commit made).
- [ ] Position note not completed: `PORTFOLIO.md` is behind the blind rule.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 routing has no place for a supplier's channel policy.** The routing sends "fast-moving technology" to Q1 TOO
HARD and customer forecasts through; a reseller's decisive unknown is neither, it is what Microsoft and Google will pay
their resellers and whether they sell direct. I treated it as a structural question for Q2; a second analyst could
close Q1 TOO HARD (NATURE) on the same facts, and the text does not decide between us. (2) **The Q7 convention's growth
input is unworkable for a business with an inverted cash cycle.** "The growth shown is measured on the aggregate owner
cash" fails when the five yearly figures run 93, 4, 551, 552, 246; I measured growth on earnings from operations
instead and say so. (3) **The convention is silent on bought growth.** It caps growth by Q3's arithmetic but does not say
whether growth that came with acquisitions larger than the owner cash counts as "growth shown". I credited none in the
whole-cycle variant and showed the free-growth ceiling separately. (4) **Margin comparisons need a stated metric when
the revenue line changes basis.** Gross-to-net reclassification makes sales-based margins incomparable across years and
across peers; the framework says compare "over the whole span" but not on what. I used operating income over gross
profit; the choice is mine. (5) **The template's position note points to `PORTFOLIO.md`, which the blind rule forbids**;
left open. (6) **The protocol's heading "COMPUTATION" with a dash conflicts with the owner's no-em-dash rule**; written
with a hyphen. (7) **Fair and cheap prices are not framework terms**; the tax gross-up, the central case and the
cheap-price rule are this run's conventions and are labelled so.
