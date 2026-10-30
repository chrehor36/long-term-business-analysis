# Company Run — Dycom Industries, Inc. (NYSE: DY) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The dispatch for this run is blind: `PORTFOLIO.md`, the holding
reviews, the session-state file, the register and the reading list were not opened, and no attempt was made to learn whether
anyone holds or wants this name. The template's instruction to check `PORTFOLIO.md` was therefore not followed (see the last
section).

**CONTAMINATION, declared.** (1) The session opened with a git snapshot whose recent commit subjects name five v5 runs of
2026-10-05 on contractors (IESC, FIX, MYRG, PRIM, MTZ), each "OUT at Q2", with one-line reasons. Those files were not opened;
the subjects were seen. Three of the five (MYRG, PRIM, MTZ) are among the competitors this run compares, so the
competitor data below was fetched fresh from the competitors' own filings and computed here, not taken from those runs.
(2) The analyst came to the name knowing in general terms that Dycom is a telecom contractor with a concentrated customer
list and a 2018 to 2019 margin collapse; that knowledge is the reason those years were read in the filings, and every fact
used below is taken from the filings, not from memory. (3) `tools/run.py` prints v4 material; only its arithmetic lines
were read (Part VII).

**Write-early note.** The file was copied from the template before any fetch and filled question by question. It was not
committed: the dispatch for this run forbids commits and pushes, so the commit-after-each step of the self-audit is left to
the operator.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $277.90 (2026-10-05, `tools/run.py`, Yahoo chart feed; **aggregator, live quote only, flagged** under
  operator rule 5). The same feed's last daily close in the saved history is $277.55
  (`Test Runs/_research 2026-10-05 DY/price_2y.txt`). The same feed shows the stock near $433 on 2026-08-17 and $303 on
  2026-09-08; no 8-K filed after 2026-08-27 explains the fall, and the run does not look for one outside the filings.
- **Shares by class** from the latest filing's cover: 30,160,957 common shares, par $0.33 1/3, one class, as of
  2026-08-24 (10-Q for the quarter ended 2026-08-01, filed 2026-08-27, accession `0000067215-26-000043`;
  `python Screens/cover_shares.py DY`). The count includes the 1,011,069 shares issued for Power Solutions (December 2025)
  and the 95,550 shares issued for National Technology Integrators (July 2026).
- **Market cap:** $8,382M at $277.90.
- **Sovereign for the earnings currency:** USD 5.63%, US Treasury daily par yield curve, 30-year, dated 10/02/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K for fiscal 2026 (53 weeks to 2026-01-31), filed 2026-03-09, accession `0000067215-26-000008`: Item 1, Item 1A,
    Item 7 in full, the balance sheet, cash-flow statement and Notes 6, 11, 14, 19, 20.
  - 10-Q for the quarter ended 2026-08-01, filed 2026-08-27, accession `0000067215-26-000043`.
  - Proxy (DEF 14A) filed 2026-04-16, accession `0000067215-26-000017` (pay design, summary compensation table,
    ownership table; read for the record only, since Q5 and Q6 were not reached).
  - 8-Ks: 2025-11-19 (`0000067215-25-000075`, the Power Solutions purchase agreement and financing commitment, with the
    press release exhibit), 2025-12-23 (`0001193125-25-330970`, the closing), 2026-08-26 (`0000067215-26-000039`, second
    quarter release, exhibit 99.1), 2026-08-04 (`0000067215-26-000032`) and 2026-08-25 (`0000067215-26-000036`) (board
    changes).
  - History: 10-K fiscal 2019 (`0000067215-19-000008`), 10-K fiscal 2020 (`0000067215-20-000012`), 10-K fiscal 2021
    (`0000067215-21-000010`), 10-KT for the six months to 2018-01-27 (`0000067215-18-000011`), 10-K fiscal 2003
    (`0000950144-03-011246`, selected financial data fiscal 1999 to 2003).
  - Competitors' latest 10-Ks: MasTec `0000015615-26-000020`, Quanta `0001050915-26-000006`, MYR Group
    `0000700923-26-000007`, Primoris `0001104659-26-018677`; and each company's XBRL company facts (transcription only).
- **One figure cross-checked against the filed statement:** total assets at 2026-01-31, $5,979,182 thousand on the filed
  consolidated balance sheet (10-K `0000067215-26-000008`), against $5,979M in the `tools/run.py` ten-year table. Net cash
  from operations fiscal 2026, $642.5M in the filed MD&A, against $643M in the tool. Both agree.
- `python tools/run.py DY`, arithmetic lines only, checked against the filing: the tool's "OE lo / OE hi" are
  (OCF less SBC less capex) and (OCF less SBC less maintenance capex) on a three-year window; the run does not use them and
  builds its own owner-cash lines below from the filed figures. Stock pay is not zero (fiscal 2026 $34.5M, fiscal 2025
  $40.3M, filed MD&A). Share count is current (no split since the cover date). OCF here contains no securities purchases.

### The balance sheets, read before the income account (**[M2025-032]**)
Ten year-ends from the filed statements (the `tools/run.py` table, first-filed XBRL vintage; spot-checked against the
fiscal 2026 and fiscal 2019 10-Ks), $M:

| year-end | equity | goodwill + intangibles | receivables incl. unbilled | contract assets | long-term debt | cash | revenue of the year |
|---|---|---|---|---|---|---|---|
| 2018-01 | 725 | 493 | 319 (+311 reclassified 2018-01-28) | 370 then 58 | 734 | 84 | 2,978 (twelve months, 10-K FY2019) |
| 2019-01 | 804 | 487 | 625 | 216 | 868 | 128 | 3,128 |
| 2020-01 | 869 | 466 | 817 | n.r. | 844 | 55 | 3,340 |
| 2021-01 | 811 | 391 | 858 | n.r. | 502 | 12 | 3,199 |
| 2022-01 | 759 | 374 | 896 | n.r. | 823 | 311 | 3,131 |
| 2023-01 | 869 | 360 | 1,067 | n.r. | 807 | 224 | 3,809 |
| 2024-01 | 1,055 | 421 | 1,243 | n.r. | 791 | 101 | 4,176 |
| 2025-01 | 1,239 | 550 | 1,374 | 63 | 933 | 93 | 4,702 |
| 2026-01 | 1,859 | 2,369 | 1,697 | 162 | 2,810 | 709 | 5,546 |
| 2026-08-01 (10-Q) | 2,064 | 2,534 | 2,278 | 221 | 2,791 (+28 current) | 340 | 3,971 (six months) |

(n.r. = not read for that year; the twelve-month revenue for the period to 2018-01-27 is the 10-K FY2019 comparative.
Receivables at 2018-01-27 are before the ASU 2014-09 reclassification of $311.7M of unbilled amounts from contract assets
to receivables, 10-K FY2019 Note 6.)

**What the figures say.** (a) **Receivables grow faster than revenue and sit near a third of a year's sales.** Receivables
including unbilled were 20% of the year's revenue at 2019-01, 24% at 2020-01, 27% at 2021-01, 29% at 2022-01 and 31% at
2026-01; the company's own DSO was 95 days (2018-01), 103 (2019-01, "primarily as a result of an increase in balances on large customer programs", 10-K FY2019), 130 (2020-01), 136 (2021-01), 114 (2025-01), 101 (2026-01), and 101
at 2026-08-01, with the 2021 rise put down to "the amount of work performed under a large customer program" (10-K FY2021,
`0000067215-21-000010`). In the six months to 2026-08-01 receivables rose $520.8M against net income of $206.9M, and
operations produced $79.1M of cash (10-Q). (b) **The fiscal 2026 cash figure is helped by a new payables programme.** A
supplier finance programme began in the fourth quarter of fiscal 2026; confirmed obligations were $226.4M at 2026-01-31 and
$367.4M at 2026-08-01, and fiscal 2026 operating cash included a $223.2M rise in accounts payable (10-K MD&A; 10-Q Note 22).
(c) **Equity grew mainly by retained earnings and, in the last year, by stock issued for an acquisition.** Retained earnings
rose from $710M (2018-01) to $1,467M (2026-01); equity rose a further $351.0M from the Power Solutions shares. (d) **The
last year changed the balance sheet's character.** Goodwill and intangibles went from $550M to $2,369M and long-term debt
from $933M to $2,810M with the $1,995.9M Power Solutions purchase (10-K MD&A, Acquisitions); at 2026-01-31 goodwill and
intangibles exceed equity. (e) **Inventory is small** ($79M to $128M over the decade): the work is labour and equipment, and
customers supply most materials (10-K Item 1). (f) What the figures cannot say: the customers' future capital budgets,
which decide volume, and whether the receivables owed by four concentrated buyers are as good as they look.

---
## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the market serving and not instructing: the price fell by about a third between
mid-August and early October 2026 with no filed explanation, and "It just tells us prices" **[M2006-077]**; the run asks only
where the facts and reasoning lead. A share is a business: would the analyst be content to own this contractor "if the
market closed for five years" **[M1997-109]**, through a customer capital-spending downturn of the kind shown in fiscal 2002
and fiscal 2019 to 2022? The analyst's habits govern the method: "What do I not know that I need to know?" **[M1999-129]**;
competitors' own filings read to "possibly reject your original hypothesis" **[M1998-144]**; and the other side stated as
well as its holder would state it **[M2016-055]**.

**Contrary evidence, written down as found** **[M1997-127]**, both ways:
- *For the business:* fiscal 2026 pre-tax margin 6.6% against MasTec 3.6%, Quanta 4.9%, MYR 4.4%, Primoris 5.1% (calendar
  2025); 92.2% of fiscal 2026 revenue under multi-year master service agreements and other long-term contracts; record total
  backlog $12,242.4M at 2026-08-01 (8-K exhibit 99.1, `0000067215-26-000039`); the 10-K's claim that it can "address larger
  customer opportunities due to our significant financial resources that some of our comparatively more capital-constrained
  competitors may be unable to take on" (Item 1); Building Systems at a 24.5% adjusted EBITDA margin in the second quarter.
- *Against the business:* the 10-K's own words, "Relatively few barriers to entry exist in the markets in which we operate"
  (Item 1 and Item 1A); master service agreements "awarded primarily through a competitive bidding process"; "In most cases, a
  customer may terminate an agreement for convenience"; "if competitors underbid us to procure business, we could be required
  to lower the prices we charge" (Item 1A); customers' in-house crews as competitors (Item 1A); pre-tax margin from 8.2%
  (fiscal 2017) to 1.7% (fiscal 2022) with costs "under absorption of costs incurred on large customer programs" (10-K
  FY2019); payments made to customers to obtain long-term agreements, carried as long-term contract assets (10-K FY2019 Note
  7: up $24.9M in fiscal 2019 "primarily due to a long-term customer agreement"); receivables rising $520.8M in six months;
  a supplier finance programme supporting the fiscal 2026 cash figure; the Building Systems margin explained in part by
  "favorable changes in cost estimates on projects" (8-K exhibit 99.1).

## THE STANDING RULE
No ruin to the buyer arises from the business as such; it would arise only from the buyer's conduct, borrowing to own it
**[L2014-005]** or a size that a 50 percent fall would force out **[M2020-022]**. The name brings a price that has moved by a
third in seven weeks, so the size question would be live if the run reached Q10. It does not. **[M2012-081]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**.
- **The key variables** **[M1998-044]**: (1) the telecom and utility customers' capital and maintenance budgets, which set
  volume; (2) the price per unit of work, set at bid under master service agreements; (3) labour productivity and the cost of
  ramping new customer programmes; (4) since December 2025, data-centre electrical work in one region for general
  contractors serving hyperscalers.
- **Do the past statements tell the future ones** **[M2008-033]**? Yes, as to the kind of economics. The record across
  three technology generations (copper and coax, fibre, wireless) shows one shape: pre-tax margin 13.5% (fiscal 2000) and
  12.7% (fiscal 2001), a loss and an $86.9M goodwill write-off in fiscal 2002, 4.9% (fiscal 2003) (10-K FY2003 selected data);
  1.1% (fiscal 2010); 8.2% (fiscal 2017); 1.7% to 2.8% (fiscal 2019 to 2022); 6.6% (fiscal 2026). The contractor's role, its
  dependence on a few buyers' budgets and its pricing at bid are stated in the same words in the 2019 and 2026 10-Ks. What
  cannot be foreseen is the level of the customers' spending; what can be foreseen is that the company earns a contractor's
  margin on whatever is spent, in a band set by the buyers. That is a fix on earning power and competitive position in the
  sense of **[M2012-065]**, low as the fix is.
- **Is the important thing knowable** **[M2006-076]**? The thing that decides Q2, whether the company has any protection
  against bid pricing and buyer power, is answered in the company's own filings. The level of customer budgets is important
  and unknowable, and it is not needed to close the file.
- **Would the insiders write it down** **[M2000-105]**? The company's own goodwill test writes down seven-year cash flows
  at an 11.5% discount rate for its reporting units (10-K, Critical Accounting Policies); the industry describes its own
  structure in plain words (Q2 below). This is not a field whose insiders call the economics "too hard".
- **Routing.** Not fast-moving technology for the contractor: it has done the same kind of work since 1969 while what it
  builds changed. The data-centre part (about 20% of revenue in the first half of fiscal 2027) is newer and its ten-year
  demand is not foreseeable, but its contract economics (fixed-price and cost-to-cost work for general contractors, 10-Q
  revenue note) are of a kind the analyst can read. No doubt that the communications part, about 80% of revenue, is inside
  the perimeter **[M2002-092]**.
- **VERDICT: IN.** The economics can be foreseen in kind: a bid-priced labour contractor to a few large buyers, whose
  margins swing with the buyers' programmes **[M2012-065]**, **[M1998-044]**. Filing fact: 10-K fiscal 2026 Item 1 and Item 7
  (`0000067215-26-000008`), the same language in 10-K fiscal 2019 (`0000067215-19-000008`).

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**. Each test with its filing fact:

1. **The attacker with money** **[M2011-015]**, **[M2012-106]**. The company answers it itself: "Relatively few barriers
   to entry exist in the markets in which we operate. As a result, any organization that has adequate financial resources,
   access to technical expertise, and the necessary equipment may become a competitor and the degree to which an existing
   competitor participates in the markets that we operate may increase rapidly." (10-K FY2026 Item 1, Competition). The
   rows: "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**; and of such fields, "there are some
   industries that are just never going to have barriers to entry. And in those industries, you better be running very
   fast" **[M2012-106]**.
2. **The customer and the low bid** **[M2017-009]**, **[L2004-003]**. "Historically, multi-year master service agreements
   have been awarded primarily through a competitive bidding process; however, occasionally we are able to negotiate
   extensions" (Item 1); "if competitors underbid us to procure business, we could be required to lower the prices we charge
   in order to retain contracts when they come up for competitive bidding at the end of their terms" (Item 1A). The
   customer buys on the bid, the failing answer to "it wouldn’t be a question of people buying candy for the low bid"
   **[M2017-009]**; the customer does not "care from whom they buy" in the sense of **[L2004-003]**: exclusivity has
   exceptions for large work orders, other providers and the customer's own employees (Item 1).
3. **Pricing power and the agony before a rise** **[M2005-020]**. No price rise is described in any filing read. The
   evidence runs the other way: fuel cost increases weighed on Communications margins in the second quarter of fiscal 2027
   (8-K exhibit 99.1: margin down 134 bps "reflecting higher investments to scale operations, impacts on segment operating
   leverage from wireless projects deferred into next year, and cost pressure in the segment from higher fuel prices"); the
   risk factors say it "may not be able to pass along increased fuel costs" and may be unable "to pass increased labor and
   training costs to our customers" (Item 1A). And the company has paid customers to win agreements: "Long-term contract
   assets represent payments made to customers pursuant to long-term agreements and are recognized as a reduction of contract
   revenues" (10-K FY2019 Note 7, `0000067215-19-000008`; still disclosed in 10-K FY2021, $17.6M at 2021-01-30).
4. **Who sets the price.** The buyer does. Top three customers took 50.2% of fiscal 2026 revenue (AT&T 25.4%, Verizon
   including Frontier 14.0%, Lumen 10.8%; Comcast 7.4%) (10-K Item 7), and the buyers are consolidating: AT&T bought Lumen's
   mass-markets fibre business on 2026-02-02 and Verizon bought Frontier on 2026-01-20 (same). "Generally, our customers are
   not contractually committed to procure specific volumes of services" (Item 1). A business whose price is set across the
   table is the business the rows name: "whatever he charged for gas was my price" **[M2012-109]**; "he determined our
   profit" **[M2023-079]**.
5. **The low-cost position** **[L2004-007]**, **[M1997-010]**. The one exception the rows allow in a commodity-type field
   is the low-cost operator. The evidence does not show Dycom holding it. Across calendar 2015 to 2025 its pre-tax margin
   averaged 4.9% against 3.3% to 4.4% for the four competitors, which favours it on average; but it fell furthest in the
   down years (1.7% to 2.8% in fiscal 2019 to 2022, when Quanta earned 4.1% to 5.1% and Primoris 3.8% to 4.3%), the opposite
   of the low-cost operator for whom "a tough market helps the low-cost operator" **[L1997-021]**. A higher average with deeper troughs is the mark of a business
   that rides its customers' programmes, not of one that sets the industry's cost.
6. **Widening or narrowing** **[M2000-014]**. The last decade's record: margin 8.2% (fiscal 2017) to 1.7% (fiscal 2022) to
   6.6% (fiscal 2026). The fiscal 2019 10-K explains the fall in its own words: labour costs up 2.6 points of revenue
   "primarily resulting from under absorption of costs incurred on large customer programs", other direct costs up "resulting
   from the impact of costs associated with the initiation of customer programs", contract assets up $149.8M, and a $17.2M
   charge when Windstream, a customer owing $45.0M, filed for Chapter 11. When the customers launched their largest
   programmes, the contractor's returns fell. The recovery since fiscal 2023 coincides with the fibre-to-the-home build and,
   in fiscal 2027, with data-centre work; the rows read a high return with care before crediting it: "a cyclical peak in
   earnings, a monopolistic position, or leverage" **[L1994-009]**. Pre-tax return on average equity ran 39% to 41% (fiscal
   2016 to 2017), 7% to 12% (fiscal 2019 to 2022) and 22% to 30% (fiscal 2023 to 2026), the widest swing of the five.
7. **Ask the competitors** **[M1998-145]**. Their own filings describe the same field in the same words (the competitor row
   below).
8. **What could destroy it** **[M2000-014]**: a customer moving work in-house ("We can offer no assurance that our existing
   or prospective customers will continue to outsource the specialty contracting services we provide", Item 1A), a merged
   customer choosing a rival (Item 1A), the end of a build cycle, a customer's financial failure (Windstream). Each is a
   decision of the buyer, not of the company.

**The competitor row** (same metric from each company's own filings; pre-tax income over revenue, %, calendar years; Dycom's
fiscal years mapped to the calendar year in which most of their months fall, fiscal years to July shown at the fiscal year;
XBRL company facts, first-filed vintage, transcription):

| | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | mean 2015-25 | pre-tax ROE mean |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Dycom (FY Jul 2015, Jul 2016, Jul 2017, then FY Jan 2019 onward) | 6.7 | 7.7 | 8.2 | 2.8 | 2.4 | 1.9 | 1.7 | 4.7 | 7.0 | 6.5 | 6.6 | 4.9 | 22.2 |
| MasTec | -1.6 | 4.4 | 5.6 | 5.3 | 7.1 | 6.7 | 5.4 | 0.4 | -0.7 | 2.0 | 3.6 | 3.5 | 15.3 |
| Quanta | 3.0 | 4.0 | 3.7 | 4.1 | 4.7 | 5.1 | 4.8 | 4.1 | 4.6 | 5.1 | 4.9 | 4.4 | 13.1 |
| MYR Group | 4.2 | 3.4 | 1.8 | 2.8 | 2.4 | 3.6 | 4.7 | 3.8 | 3.4 | 1.4 | 4.4 | 3.3 | 16.7 |
| Primoris | 3.2 | 2.4 | 4.4 | 3.9 | 3.8 | 4.2 | 4.3 | 3.6 | 3.1 | 4.0 | 5.1 | 3.8 | 17.7 |

(Dycom's six-month transition period to 2018-01-27 is not in the annual series; its 2018 column is fiscal 2019, to
2019-01-26. Pre-tax ROE is pre-tax income over average stockholders' equity, the same years. Workings:
`Test Runs/_research 2026-10-05 DY/comp.py`.)

The competitors in their own words, latest 10-Ks: MasTec, "they award most of their work through a bid process, and price
is often a principal factor in determining which service provider is selected" and "There are relatively few barriers to
entry into certain of the markets in which we operate" (`0000015615-26-000020`); Quanta, "there are relatively few barriers to
entry into some of the industries in which we operate" and "price is often an important factor in the award of such
agreements" (`0001050915-26-000006`); MYR Group, "We enter into contracts principally through a competitive bid process" and
"Many of our contracts, including our MSAs, are open to competitive bidding at the expiration of their terms"
(`0000700923-26-000007`); Primoris, "We may lose business to competitors through the competitive bidding processes"
(`0001104659-26-018677`). Five companies, one description: bid-priced work in a field with few barriers. The rows on such a
field: "you can have only two competitors and they’re still terrible businesses, they beat each other’s brains out"
**[M2013-052]**; "one competitor is frequently enough to ruin a business" **[M2012-108]**; "anything you do, your competitors
can copy" **[M1996-017]**.

**The other side, stated as its holder would state it** **[M2016-055]**. Dycom is the largest specialist in telecom outside
plant, with a national footprint, decades-long relationships with every large carrier, and a balance sheet smaller rivals
lack; master service agreements are renewed more often than lost; its margins in good years beat every peer; and the
Power Solutions purchase adds a data-centre electrical business earning margins well above the communications work. The
answer from the filings: the relationships are real but are priced at bid and terminable for convenience; scale has not
protected the margin in the buyers' heavy-spending years; and the Building Systems margins are seven months old under
Dycom, earned in one region at the top of a data-centre build, partly from what the release calls "favorable changes in cost estimates" (8-K exhibit 99.1). A margin
earned at the top of a build is the case the rows tell the reader to suspect first: "a cyclical peak in earnings"
**[L1994-009]**. The newest part's castle cannot be judged from seven months; it is about a fifth
of revenue; and it cannot make the larger part's castle stand.

- **VERDICT: OUT.** The castle is shown open on the evidence, in the company's own words and its competitors': few barriers,
  bid pricing, terminable agreements, concentrated and consolidating buyers who set the price, no low-cost position, and a
  margin that collapsed when the buyers' programmes were largest **[M2011-015]**, **[M2012-106]**, **[M2017-009]**,
  **[M2012-109]**, **[M2023-079]**. "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. Price does not
  reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**; the box is "out"
  among "in, out, and too hard" **[M2006-013]**.

---
## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED** (Q2 closed OUT). Facts recorded for the reader, weighed by nothing: capital expenditure ran $157M to $251M
a year in fiscal 2022 to 2026 against depreciation (excluding amortization) of $129M to $201M (XBRL `Depreciation`,
first-filed); receivables absorb about 30 cents of every added dollar of revenue (balance-sheet table above); purchased
goodwill and intangibles rose to $2,534M at 2026-08-01.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** Recorded because they bear on the computation below, not as a verdict: the headline of the second-quarter
release is "Adjusted Net Income" and "Adjusted EBITDA" (8-K exhibit 99.1); the 10-K's Non-GAAP Adjusted EBITDA adds back
stock-based compensation ($34.5M) and removes gains on asset sales; the fiscal 2026 operating cash includes a payables rise
of $223.2M alongside a new supplier finance programme. The balance-sheet reading required here is done above, in STEP 0.

## Q5 — WHO RUNS IT. STOP on integrity.
**NOT REACHED.** Proxy read for the record (`0000067215-26-000017`): chief executive Daniel Peyovich, total fiscal 2026 pay
$8,011,338; annual incentive gated at operating earnings of 2.5% of contract revenues and scaled by a cash-flow ratio;
performance units vest between 2.5% and 5.0% operating earnings margin. No capital charge appears in the measures read.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** Facts recorded: 100,000 shares bought in the quarter to 2026-05-02 at an average $359.63 (10-Q Note 17),
above the top of every computed range below; 1,011,069 shares issued for Power Solutions valued at $351.0M and 95,550 for
National Technology Integrators valued at $45.0M; a new $150.0M buyback authorization on 2026-08-26 naming no price.

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED.** The owner asked for the value range, the fair-price band and the cheap price; they follow at the end under
COMPUTATION, and none of them is a clearance.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Recorded: net debt $2,480M at 2026-08-01 (long-term debt $2,791.3M plus current $28.4M less cash $340.1M,
10-Q); covenants at a 4.50 net leverage maximum and 2.50 interest cover minimum, defined on EBITDA (10-K Item 7);
performance and surety bonds $1,215.8M outstanding (10-Q Note 21).

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT ASKED.** Building telecom and electrical networks is none of the businesses named.

---
## THE BOX
**OUT at Q2.** The castle is shown open in the company's own filing and in its four competitors': relatively few barriers to
entry, agreements won and renewed at competitive bid and terminable for convenience, three customers taking half the
revenue and consolidating, no low-cost position, and a margin that fell from 8.2% to 1.7% when the customers' programmes
were largest. Not a TOO HARD: the deciding question was answered, and against. For the record only, the computation below
puts the value at about $95 to $148 a share against $277.90.

---
## COMPUTATION — NOT A CLEARANCE
Operator rule 3: arithmetic after a closing STOP, carrying no entry language. Built by the Q7 CONVENTION of the framework
(Part VI) so that the numbers are comparable with other runs; the inputs are filed figures. Workings:
`Test Runs/_research 2026-10-05 DY/value.py` and `value_out.txt`.

**Owner cash after every real cost, $M** (net income, which is after interest, tax and stock pay **[L2021-003]**; plus
depreciation and amortization; less all capital expenditure; plus the book value of assets sold, that is proceeds less the
gain already in net income). Beside it the depreciation variant (net income plus amortization of purchased intangibles, less
gains), and the cash variant (operating cash less stock pay less capital expenditure plus proceeds):

| | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | five-year mean |
|---|---|---|---|---|---|---|
| all capital spending deducted (the convention's input) | 45.5 | 86.0 | 170.4 | 184.1 | 316.9 | **160.6** |
| depreciation variant | 61.9 | 140.7 | 210.4 | 228.3 | 323.3 | 192.9 |
| cash variant | 147.2 | -36.7 | 50.2 | 97.4 | 400.8 | 131.8 |
| cash variant less year-end supplier finance ($226.4M) | 147.2 | -36.7 | 50.2 | 97.4 | 174.4 | 86.5 |

Inputs from the 10-Ks (net income, D&A, capex, proceeds, gain on sale, OCF, stock pay), first-filed XBRL cross-read against
the fiscal 2026 MD&A for fiscal 2025 and 2026. Maintenance: the company does not split capex; its fiscal 2027 guide is
$210M to $220M net of disposals "to support growth opportunities and the replacement of certain fleet assets" (10-K Item 7),
so no maintenance figure is stated and all capex is deducted.

**Growth input.** The aggregate owner cash grew from $45.5M to $316.9M across fiscal 2022 to 2026, about 62% a year, from a
trough base year, "a breathtaking, but meaningless, growth rate" **[L2005-003]**. It is capped at the discount rate, 5.63%
(the cap is this run's reading of the convention; see the last section).

**Value range** (ten years at the growth shown, capped, then zero nominal growth, discounted at 5.63%; 30,160,957 shares):

| case | input $M | no growth | capped growth |
|---|---|---|---|
| **convention input (all capex), five-year mean** | 160.6 | **$94.6** | **$147.8** |
| depreciation variant | 192.9 | $113.6 | $177.6 |
| cash variant | 131.8 | $77.6 | $121.3 |
| cash variant less supplier finance | 86.5 | $50.9 | $79.6 |
| fiscal 2026 alone, all capex (peak check) | 316.9 | $186.6 | $291.7 |
| trailing twelve months to 2026-08-01, all capex (peak check, includes Power Solutions and its debt) | 463.4 | $272.9 | $426.6 |
| trailing twelve months, cash variant less supplier finance ($367.4M) | 79.7 | $47.0 | $73.4 |

The convention's range is **$95 to $148** a share (top over bottom 1.56, under three to one), against **$277.90**: the price
sits 88% above the top. At the price the convention input yields 1.92% after tax and 2.51% pre-tax; the expected pre-tax
return is about 2.5% with no growth and about 4.0% with the capped growth, both below the floor of about ten percent
pre-tax (CONVENTION, **[M2003-149]**, **[L2002-020]**, **[M1994-004]**). Only the trailing peak-earnings line with
Power Solutions in it reaches the price, and only at its no-growth end; the same twelve months produced about $80M of cash
once the supplier finance balance is taken out, which is "the 12 percent on capital but there’s never any cash"
**[M2003-122]**. The spread between the earnings and cash lines is itself the finding: the profit sits in receivables,
"there’s your profit sitting in the yard" **[M2008-036]**.

**Fair-price band** (prices inside the range at which the expected pre-tax return, solved as the rate that equates the
price to the pre-tax owner cash at an effective tax rate of 23.6%, is at or above about ten percent): **about $95 to $103 a
share**, and only on the capped-growth case; on the no-growth case no price inside the range clears ten percent, which
needs about **$70** or less.

**Cheap price** (below which the case needs no pencil, **[M1996-084]**, **[M2009-005]**): **about $35 a share**, the price
at which the no-growth case alone returns about twenty percent pre-tax, twice the floor; it is about 37% of the bottom of
the range, near the proportion in "I didn’t need to know whether it was worth 97 billion or 103 billion if I was buying it
at 35 billion" **[M2008-068]**. The fair-price band and the cheap price are reporting conventions made for the owner's
request, not rules of the framework, and they are confessed as such.

None of this reopens Q2: "You can turn any investment into a bad deal by paying too much. What you can’t do is turn any
investment into a good deal by paying little" **[M2019-015]**.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. [ ] Committed after each: not done; the
      dispatch forbids commits (write-early note above).
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, with every quoted fragment beside an id
      matched inside that row); every filing fact has its accession; no number without a row, a filing, or a stated
      convention.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; nothing after it is a clearance; the arithmetic
      after it is headed COMPUTATION — NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy: net income is the starting line but depreciation is
      replaced by all capital spending and gains are taken out (operator rule 5); the sovereign from the US Treasury; the
      price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (Foundations), both ways.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its owner-earnings lines were not used.
- [x] `python tools/check_framework.py` PASS before handing back (result recorded in the dispatch reply).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Six things. (1) **The Q7 convention's five-year average does not fit a company that has just doubled its capital.** Power
Solutions was owned for five of fiscal 2026's fifty-three weeks, so the five-year base carries almost none of its earnings,
while the share count, the debt and the interest going forward carry all of it; no rule says whether to keep the base, add
the acquired earnings, or use the trailing year. The run kept the convention's base and showed the trailing year beside it
as a peak check. (2) **"The growth shown, capped by Q3" has no number.** The shown growth here (62% a year off a trough base)
is the meaningless kind **[L2005-003]**; the run capped it at the discount rate, reading "no rate that runs past the discount
rate" literally. Another analyst could cap it at revenue growth (about 7.6% a year over ten years, acquisitions included)
and get a higher top; the close does not change, since the run closed at Q2. (3) **The convention does not say whether
working capital belongs in owner cash.** For a contractor whose receivables are near a third of a year's revenue and whose
latest cash figure leans on a supplier finance programme, that is the whole question; the run showed the earnings and cash
lines side by side rather than choose. (4) **The template's position note tells the analyst to check `PORTFOLIO.md`, which a
blind dispatch forbids.** The run followed the dispatch and recorded the note as not checked; the template could say "or
record that the run is blind". (5) **The fair-price band and the cheap price are not defined in the framework.** The run
defined them for the owner's request (ten percent pre-tax for the band; twice the floor on the no-growth case for the
cheap price) and labelled them reporting conventions. (6) **The by-parts reading is stated for Q1 only.** At Q2 a smaller
part (Building Systems) whose castle cannot be judged from seven months sat beside a larger part shown open; no sentence
says which governs. The run closed OUT on the larger part, since the smaller cannot hold up the larger's castle, but the
framework could say so.
