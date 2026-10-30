# Company Run — Shoe Station Group, Inc. (Nasdaq: SHOE; formerly Shoe Carnival, Inc., SCVL) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is barred to this run by its blind rule, so
whether the operator holds SHOE is unknown to the analyst. The analyst holds no view formed before this run.

**CONTAMINATION DECLARED.** (1) A directory listing taken to confirm the output path showed that a file named
`Test Runs/2026-09-01 Run - SHOE Shoe Station Group.md` exists; it was not opened, and its verdict is unknown to me.
(2) The same listing showed the names of other 2026-10-05 run files, among them a footwear retailer (BOOT Boot Barn);
none was opened. (3) The session's starting context showed five commit subjects (GENC, AROC, MTRN, MBUU and a session
note), none about SHOE or a footwear retailer. Nothing else outside the filings and the framework was read.

**CIK** 0000895447. Name changed from Shoe Carnival, Inc. to Shoe Station Group, Inc. effective 2026-06-12, ticker SCVL to
SHOE (8-K filed 2026-06-11, accession 0001193125-26-266625, Item 5.03; 10-Q for the quarter to 2026-08-01, accession
0001193125-26-387855, MD&A overview). Working folder: `Test Runs/_research 2026-10-05 SHOE/`.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $12.76 (close 2026-10-05, Yahoo Finance chart endpoint; AGGREGATOR, live quote only, flagged per operator
  rule 5). `tools/run.py` printed $12.77 from its own aggregator the same day. For reference from the filing, not a
  price: the company bought 390,492 shares for $7.0 million in the first half of fiscal 2026, about $17.93 a share, and
  1,600 shares at $16.65 in the period 2026-05-31 to 2026-07-04 (10-Q, accession 0001193125-26-387855, Part II Item 2).
- **Shares by class** from the latest filing's cover: one class, 27,183,815 common shares (10-Q filed 2026-09-10 for the
  quarter to 2026-08-01, accession 0001193125-26-387855; `python Screens/cover_shares.py SHOE`). The proxy gave 27,538,278
  at 2026-03-31 (DEF 14A, accession 0001193125-26-191497); the fall is the buyback above. Treasury shares 13,865,375 of
  41,049,190 issued (10-Q balance sheet).
- **Market cap:** 27,183,815 × $12.76 = **$346.9M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, 30-year par yield, US Treasury daily par yield curve, dated
  10/02/2026 (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for fiscal 2025 (year to 2026-01-31), filed 2026-03-26, accession
  0001193125-26-126279 (Items 1, 1A, 7, 8: balance sheet, income statement, equity, cash flows, Notes 3, 11, 14); 10-Q
  for the quarter to 2026-08-01, filed 2026-09-10, accession 0001193125-26-387855 (statements, MD&A, Part II); DEF 14A
  filed 2026-04-29, accession 0001193125-26-191497 (directors, principal shareholders, related-person transactions);
  8-Ks of 2025-09-25 (0001193125-25-217451, CFO), 2025-12-09 (0001193125-25-312955), 2025-12-12 (0001193125-25-316812,
  buyback and dividend), 2026-02-25 (0001193125-26-068399, CEO departure), 2026-03-09 (0001193125-26-098464, interim CEO
  pay and the fiscal 2026 bonus metric), 2026-06-11 (0001193125-26-266625, rename). History: 10-Ks for fiscal 2007
  (0001206774-08-000811), 2010 (0001206774-11-000882), 2012 (0001174947-13-000180), 2015 (0001174947-16-002383), 2018
  (0001564590-19-010585), 2020 (0001564590-21-015810), 2022 (0000950170-23-009730), 2024 (0000950170-25-043195), for the
  five-year tables, the vendor shares and the Shoe Station acquisition note.
- **One figure cross-checked against the filed statement:** net cash from operations, fiscal 2025, **$71,300 thousand**
  in the filed Consolidated Statement of Cash Flows (accession 0001193125-26-126279) against 71 ($M) in `tools/run.py`.
  Also merchandise inventories at 2026-01-31, $439,638 thousand filed against 440 in the tool's balance-sheet table. Both
  agree.
- **`python tools/run.py SHOE`, arithmetic lines only** (its v4 text, ids and floor ignored, per Part VII). Each line
  checked against the filing:
  - Share count 27.2M: agrees with the 10-Q cover (27,183,815).
  - Stock pay: the cash-flow line "Stock-based compensation" ($7,312K fiscal 2025; $7,697K 2024; $4,887K 2023). Note 14
    says it "includes share-settled awards [...] in the form of restricted stock units, performance stock units, and
    restricted and other stock awards", and the 10-K says shares were issued "to our non-employee directors upon the
    issuance of service-based restricted stock awards"; directors' stock pay is therefore inside the line. Complete.
  - Current debt: none. "Fiscal 2025 marked the 21st consecutive fiscal year we ended with no debt"; $99.0M undrawn on a
    $100M credit agreement collateralized by inventory, expiring 2027-03-23 (10-Q MD&A).
  - Lease obligations: operating lease liabilities $371.4M at 2026-01-31 ($58.1M current, $313.4M long-term) and $354.6M
    at 2026-08-01 ($50.9M, $303.7M); rent-related payments $98.1M in fiscal 2025 (10-K MD&A, Leases). The rent is inside
    operating cash flow, so owner cash below already bears it; the liability is read at the balance sheets.
  - Owner cash by the tool's formula (operating cash − stock pay − capital spending), $M, recomputed from the filed cash
    flows (XBRL facts, accessions in the research folder): **FY2021 111.0; FY2022 −32.3; FY2023 61.6; FY2024 61.7; FY2025
    19.3; five-year average 44.3.** Depreciation variant (operating cash − stock pay − D&A): 123.6, 21.8, 89.1, 63.8,
    29.7; average 65.6. Earlier years, capital-spending basis: FY2016 38.2; FY2017 15.6; FY2018 56.5; FY2019 41.9; FY2020
    47.1 (pre-pandemic five-year average 39.9).
  - Capital spending against depreciation, FY2016 to FY2025: $322.7M against $238.5M (135%); the excess is the
    rebanners and remodels ($37.1M of fiscal 2025 capital spending "supporting the rebanner initiative", 10-K Item 1).
  - Acquisitions, paid in cash and not in capital spending: Shoe Station, 2021-12-03, "total consideration of $ 70.3
    million" (10-K fiscal 2022, accession 0000950170-23-009730, Note 3); Rogan's, fiscal 2024, $44.8M net of cash (10-K
    fiscal 2025, MD&A). Owner cash for FY2021 to FY2025 after these: $21.2M a year on average.
  - Latest half: net income $631K for the 26 weeks to 2026-08-01 against $28,568K a year earlier; operating cash $34.1M
    (inventory release of $13.0M); capital spending $15.0M (10-Q cash-flow statement).

### The balance sheets, read before the income account (Q4's rule, read here because the file closes before Q4)
"balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**. Fiscal year-ends
FY2016 to FY2025 from `tools/run.py`'s ten-year table (first-filed XBRL), the FY2025 column checked against the filed
balance sheet, plus 2026-08-01 from the 10-Q. $M.

| year-end | assets | equity | cash | inventory | goodwill + intangibles | inventory / that year's sales |
|---|---|---|---|---|---|---|
| FY2016 (2017-01-28) | 458 | 319 | 63 | 280 | 0 | 28.0% |
| FY2017 | 416 | 307 | 48 | 260 | 0 | 25.5% |
| FY2018 | 418 | 304 | 67 | 258 | 0 | 25.0% |
| FY2019 | 628 | 297 | 62 | 259 | 0 | 25.0% |
| FY2020 | 643 | 310 | 107 | 233 | 0 | 23.9% |
| FY2021 | 812 | 453 | 117 | 285 | 44 | 21.4% |
| FY2022 | 990 | 526 | 51 | 390 | 45 | 30.9% |
| FY2023 | 1,042 | 583 | 99 | 346 | 45 | 29.4% |
| FY2024 | 1,124 | 649 | 109 | 386 | 59 | 32.1% |
| FY2025 (2026-01-31) | 1,202 | 690 | 117 | 440 | 59 | 38.7% |
| 2026-08-01 (10-Q) | 1,168 | 677 | 118 | 427 | 59 | n/a (half year) |

What moved and why. **Equity** was flat at about $300M from FY2016 to FY2020 (earnings went out in buybacks: $42.6M,
$29.8M, $46.0M, $37.8M in FY2016 to FY2019), then more than doubled to $690M on the pandemic earnings of FY2021 and FY2022
(net income $154.9M and $110.1M) and the smaller buybacks after them. **Goodwill and intangibles** appear only with the
Shoe Station (2021) and Rogan's (2024) purchases and are 9% of equity: the equity is mostly inventory, cash and store
fixtures. **Assets** jumped in FY2019 by the lease right-of-use asset (accounting, ASC 842), not by business. **Debt:**
none in any year; the debt-like item is $354.6M of operating lease liabilities at 2026-08-01, about half of equity.
**Inventory against sales** is the line that moved: from 21% to 25% of sales before and during the pandemic to 38.7% at
2026-01-31, while sales fell. The rows tell me to "look twice" where "inventories look out of line, you know, with sales"
**[M1995-064]**. The filer explains it in advance and in the open: "opportunistic buys for seasonal and in-demand
merchandise", with a stated plan to cut inventory by $50 to $65M and "increase promotional activity to work through excess
inventory" (10-K MD&A, accession 0001193125-26-126279); the 10-Q then shows the promotion and a 630 basis-point fall in
merchandise margin. I read it as a merchandising error disclosed and paid for, not a hidden one; it is evidence for Q2
(the margin is set by promotion), and it is not a Q4 confusion. **Retained earnings** $313M to $809M; **receivables**
trivial ($6M), as in a cash retailer. What the figures cannot say: what a store is worth when its lease ends, and how much
of the merchandise margin the vendors will leave to a reseller in ten years.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I "Would I be happy buying this stock if the market closed for five
years?" **[M1997-109]**, which here turns on whether a family shoe reseller keeps its customers and its margin for five
years. The market has fallen from the company's own buyback price of about $17.93 to $12.76; "It just tells us prices."
**[M2006-077]**, and nothing in the fall is read as information. No macro enters: tariffs and "pressure on lower-income
consumers" (10-K MD&A) are read only as properties of the business, never as forecasts; macro conclusions "just never
enter into the discussion" **[M2000-094]**. The margin of safety is an attitude here: a case that needs a pencil is "too
close to think about" **[M1996-084]**. The analyst's habits: "I’m looking for what’s wrong in things" **[M2025-013]**.
**Contrary evidence, written down as found**, by the rule to "write it down in the first 30 minutes" **[M1997-127]**,
against the OUT this run reaches:
(a) profitable "in every fiscal year except 1995" since 1993 and debt-free for 21 years (10-K Item 1 and MD&A), including
FY2008, when comparable sales fell 4.6% and operating income was still $8.4M;
(b) in FY2023 to FY2025 its operating margin (8.0%, 7.6%, 5.9%) was above Famous Footwear's (7.7%, 5.6%, 3.2%), Designer
Brands' (2.4%, 1.2%, 1.7%) and Foot Locker's (1.7%, 1.3% for FY2023 and FY2024), all from their own filings (competitor
row, Q2);
(c) the Shoe Station banner grew sales from $99.9M (fiscal 2022) to $236.7M (fiscal 2025) before transfers were counted
separately, and grew low single digits on a comparable basis in fiscal 2025 (10-K MD&A);
(d) the founding chairman's family owns 31.5% and the proxy reports no related-person transaction over $120,000 in
fiscal 2025 (DEF 14A);
(e) at $12.76 the price sits below every value this run computes from the five-year owner cash (see the computation at
the end), which is the kind of finding that tempts a buyer to stop at Q2's door.
Each is weighed in Q2 below; none answers why the castle stands.

## THE STANDING RULE
The buyer's conduct: any purchase would be made from cash, unlevered, at a size whose total loss could not touch what the
buyer has and needs; "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**;
"Never risk permanent loss of capital." **[L2023-005]**. Nothing in owning a small, debt-free retailer's stock breaks the
rule. Satisfied by conduct; no business question is answered here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, which needs the key variables and "evaluating how predictable they were
  first" **[M1998-044]**.
- **What the business is, from the filing.** It buys branded shoes (Nike about 24% of net sales, Skechers 13%, Crocs 9%,
  together 46% in fiscal 2025, "no long-term contracts in place with any of our vendors") and sells them in 422 leased
  stores in 35 states and Puerto Rico (257 Shoe Carnival, 165 Shoe Station at 2026-08-01) and online (about 10% of
  merchandise sales). "All stores are leased" (10-K Item 1, accession 0001193125-26-126279; 10-Q MD&A).
- **The key variables:** comparable sales (traffic and units times price), merchandise margin (set by promotion and by
  vendor cost and allocation), occupancy, and the vendors' choice of where to sell. Each is reported every year, and their
  history is long (comparable sales are given back to fiscal 2003 in the five-year tables).
- **Foreseeable?** The product is plain and the economics are those of a reseller of other companies' brands. I do not
  need to know which shoe will be in fashion to see what the business earns over a cycle: "What is important is that I
  understand the economic dynamics of the industry." **[M2011-014]**. The industry is not one of fast technology, so the
  routing to TOO HARD at Q1 does not apply; the insiders would write down the economics of a shoe store chain, whatever
  they would say of its fashion calls.
- **The doubt, stated.** The rows warn that "it’s easy to sort of think you understand retail, and then subsequently find
  out you don’t" **[M2014-052]**, and "if you have doubts about something being into your circle of competence, it isn’t."
  **[M2002-092]**. My doubt is not about what drives the economics; it is about whether the company can defend them, which
  is Q2's question, not Q1's. If the run had needed a forecast of which banner wins, I would send it to TOO HARD; it does
  not, because the castle question below is answered on the record.
- **VERDICT: IN.** A branded-goods reseller in leased stores, whose margin is set by its vendors and its rivals. What
  counts is to "understand the economic dynamics of the industry." **[M2011-014]**, and on those I have "a reasonable fix"
  **[M2012-065]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing?" **[M1995-038]**. The tests, each with its filing fact (10-K fiscal 2025 accession
0001193125-26-126279 unless another is named).

1. **What keeps the customer, and how permanent is it?** The filer's own list: "the principal competitive factors in our
   industry are merchandise selection, price, fashion, quality, location, shopping environment and service" (Item 1). The
   merchandise is other companies' brands, sold also by the vendors themselves, by department stores, sporting goods
   stores, off-price stores and online. The filer's own description of the competitive answer is price and breadth: "We
   compete with most department stores and traditional shoe stores by offering competitive prices". Nothing on the list
   is owned. A retailer must "stay smart, day after day. Your competitor is always copying and then topping whatever you
   do." **[L1995-008]**.
2. **Would it stand without the lord?** "In retailing, to coast is to fail." **[L1995-008]**; "For a retailer, hiring that
   nephew would be an express ticket to bankruptcy." **[L1995-009]**. The record of the last eighteen months is the test
   applied: a single-banner Shoe Station strategy announced in March 2025, 101 stores rebannered in fiscal 2025 at an
   operating-income cost of about $24.1M, then "significant variability in in-store sales performance across rebannered
   locations", the pace slowed (10-K Item 1); the chief executive departed 2026-02-24 (8-K, 0001193125-26-068399); the
   strategy reversed: "we are no longer pursuing a single-banner Shoe Station strategy" and "No additional rebanners are
   expected" (10-Q MD&A, 0001193125-26-387855). The results depend on the calls of the people in charge, and the calls
   have been wrong at the scale of the fleet.
3. **The money test.** In the filer's own words: "The retail footwear industry is highly competitive with few barriers to
   entry." and "Many of our competitors are significantly larger and have substantially greater resources than we do."
   (Item 1A). The rows answer the attacker test plainly: "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**;
   "there are some industries that are just never going to have barriers to entry" **[M2012-106]**.
4. **Pricing power, and the agony before a rise.** The filer: "If our competitors become more promotional than we are, or
   if we match our competitors’ promotional intensity, and lower margins are not offset [...], our results [...] may be
   adversely affected" (Item 1A). In fiscal 2025 it held price, "maintained pricing discipline", and the result was "an
   approximate 13% decrease in units sold, partially offset by pricing increases" (MD&A). In the second quarter of fiscal
   2026 the market set the price back: merchandise margin down 630 basis points on "an increasingly promotional footwear
   marketplace" (10-Q). That is the rival setting the price: "whatever he charged for gas was my price" **[M2012-109]**;
   "he determined our profit, because we looked at his price every day" **[M2023-079]**; and the strength of a business
   is measured "by the agony they go through in determining whether a price increase can be sustained" **[M2005-020]**.
   The positive test, "charge more for a product and maintain or increase market share" **[M2000-031]**, failed in
   fiscal 2025 in the plainest form: price up, units down about 13%, comparable sales down 5.6%, and share lost to the
   nearest peer (test 9). The rows name what that shows: they "lost market share without getting — without having — the
   moat that they thought they had" **[M2001-087]**.
5. **Unit volume and share of mind.** Comparable sales, from the filed five-year tables (10-Ks fiscal 2007, 2010, 2015,
   2020, 2025, accessions above): FY2003 −3.0%, FY2004 −0.8%, FY2005 +6.9%, FY2006 +1.5%, **FY2007 −5.2%, FY2008 −4.6%**,
   FY2009 +3.5%, FY2010 +8.2%, FY2011 +0.7%, FY2012 +4.5%, FY2013 0.0%, FY2014 +1.8%, FY2015 +3.0%, FY2016 +0.5%, FY2017
   +0.3%, FY2018 +4.3%, FY2019 +1.9%, FY2020 −5.3%, FY2021 +35.3%, **FY2022 −11.1%, FY2023 −8.8%, FY2024 −3.9%, FY2025
   −5.6%, first half FY2026 −4.7%** (second quarter −7.1%; Shoe Station banner −8.5%). Average sales per store fell from
   $3.47M (FY2021) to $2.64M (FY2025), and sales per square foot from $321 to $253 (10-K five-year table). Units fell about 13% in fiscal 2025 and 4% in the second quarter of fiscal 2026.
6. **The low-cost position.** Not shown. Over the pre-pandemic span FY2009 to FY2019, its operating margin averaged 4.75%
   against Famous Footwear's 5.58% (segment), Designer Brands' 6.15% and Foot Locker's 8.58% (competitor row below). A
   reseller of identical branded goods is in a commodity-like position for the goods themselves, and there "commodity
   businesses have risk unless you’re the low-cost producer" **[M1997-010]**; "being the low-cost producer is
   all-important" **[L2000-017]**. Gross margins are not comparable across these filers (Shoe Carnival puts buying,
   distribution and occupancy in cost of sales; Famous Footwear's gross margin ran 42% to 48% over FY2008 to FY2025); the operating line is the
   test, and on it the company is not the low-cost operator.
7. **The brand in the customer's mind.** The brands the customer asks for are Nike's, Skechers', Crocs'. The rows name
   which side the brand protects: "the brand is our protection against the intermediaries making all the money"
   **[M2019-041]**, said by a brand owner of the retailer; and "there will be a battle, always, between brands and
   retailers" **[M2001-090]**. The filer reports its vendors' side of the battle: "Certain key suppliers’ business models are
   changing and such changes include, but are not limited to, increased direct-to-consumer initiatives, changes in planned
   product allocations and reductions in the number of retailers with which they are choosing to do business" (Item 1A).
   The vendor's power is in the numbers: Nike was 31% of net sales in FY2015 (10-K, 0001174947-16-002383), 32% in FY2018
   (0001564590-19-010585), 33% in FY2020, 28% in FY2021, **14% in FY2022** (10-K, 0000950170-23-009730), 24% in FY2025.
   The retailer's own banner is being renamed: the company took the smaller banner's name, then found the format did not
   travel to its own stores. The retail name is not what the customer asks for.
8. **Would the customer still choose it over the low bid?** Shoe Carnival's customers are "moderate to low-income
   families" served with "a value-oriented selection, with entry-level price points" (Item 1); the fiscal 2025 decline is
   put on "pressure on lower-income consumers" (MD&A). That customer buys on the low bid, the opposite of See's, where "it
   wouldn’t be a question of people buying candy for the low bid" **[M2017-009]**. The same goods, "a product that has a
   whole bunch of competitors" **[M2023-074]**.
9. **Ask the competitors.** On the record: the nearest peer, Famous Footwear (Caleres), had comparable sales of −1.8%,
   −6.3%, −1.3%, −2.3% in its fiscal 2022 to 2025 against Shoe Carnival's −11.1%, −8.8%, −3.9%, −5.6% (Caleres 10-Ks,
   accessions 0000014707-23-000018 and 0000014707-26-000053). Four years running, the company lost ground to the
   competitor most like it.
10. **Widening or narrowing?** Narrowing on every measure the filings give: comparable sales negative four years and into
    the fifth; sales per store and per square foot down a fifth from FY2021; the store target of "at least 500 stores by
    2028" (10-K fiscal 2022) against 422 stores now and 12 to 20 closures planned (10-Q); the FY2022 10-K's statement that
    those results "set the new benchmark for us going forward" against an operating margin of 11.6% then and 0.3% in the
    first half of fiscal 2026. "whether it’s likely to widen further or shrink on you" **[M1999-108]**: it has shrunk.
11. **What could destroy, modify or reduce it.** The vendors selling direct and choosing fewer retailers (Item 1A, test
    7); a promotional rival; tariffs on imported footwear (the 10-Q's tariff section). Each acts on a margin the company
    does not set. The pandemic years are the warning, not the base: a margin of 15.6% gained in one year and lost in four,
    and "usually if something can gain competitive advantage very quickly, you have to worry about them losing it quickly,
    too" **[M2002-050]**; "companies now riding high but vulnerable to competitive attacks" **[L1996-031]**.

**The competitor row** (operating income ÷ net sales, from each company's own filings; fiscal years ending about January
of the next calendar year; Famous Footwear is a segment of Caleres and its operating earnings exclude Caleres's corporate
costs, so it flatters that row).

| fiscal year | SHOE / SCVL | Famous Footwear (CAL segment) | Designer Brands (DBI) | Foot Locker (FL) |
|---|---|---|---|---|
| 2008 | 1.3% | 2.0% | n/r | n/r |
| 2009 | 3.7% | 3.3% | −2.5% | 1.6% |
| 2010 | 5.7% | 6.1% | 6.6% | 5.2% |
| 2011 | 5.5% | 4.3% | 7.5% | 7.8% |
| 2012 | 5.7% | 6.2% | 10.5% | 9.9% |
| 2013 | 4.9% | 7.0% | 10.2% | 10.2% |
| 2014 | 4.5% | 6.6% | 9.7% | 11.3% |
| 2015 | 4.7% | 6.9% | 8.2% | 11.3% |
| 2016 | 3.8% | 5.3% | 7.4% | 12.9% |
| 2017 | 3.7% | 5.6% | 4.5% | 7.3% |
| 2018 | 4.8% | 5.3% | 1.9% | 8.8% |
| 2019 | 5.2% | 4.8% | 3.6% | 8.1% |
| 2020 | 2.2% | −1.9% | −26.2% | 4.1% |
| 2021 | 15.6% | 15.8% | 6.4% | 9.7% |
| 2022 | 11.6% | 11.5% | 5.7% | 6.6% |
| 2023 | 8.0% | 7.7% | 2.4% | 1.7% |
| 2024 | 7.6% | 5.6% | 1.2% | 1.3% |
| 2025 | 5.9% | 3.2% | 1.7% | (deregistered; Form 15 filed 2025-09-18, 0001140361-25-035399) |
| **avg FY2009-2019** | **4.75%** | **5.58%** | **6.15%** | **8.58%** |
| **avg FY2009-2025** | **6.06%** | **6.08%** | **3.46%** | **7.36% (to FY2024)** |

Sources: SHOE from its 10-K five-year tables and XBRL facts (accessions above); Famous Footwear from Caleres 10-Ks
0000014707-09-000060, 0000014707-11-000026, 0000014707-14-000020, 0000014707-17-000010, 0001437749-20-006641,
0000014707-23-000018, 0000014707-26-000053; Designer Brands (CIK 1319947) and Foot Locker (CIK 850209) from their XBRL
company facts, operating income and revenue tags as filed in each 10-K (accessions in
`Test Runs/_research 2026-10-05 SHOE/peers/`). Academy Sports (ASO, CIK 1817358) is a general sporting-goods retailer with
filings only from FY2018: 2.7%, 3.7%, 7.4%, 13.4%, 13.2%, 11.0%, 9.1%, 8.5% for FY2018 to FY2025; it sells far more than
shoes and is shown for scale, not as a like-for-like peer. Across the whole span the company earned what its nearest peer
earned, below the athletic specialists before the pandemic, and with its comparable sales falling faster than that peer's
in the last four years. No company in the row shows a protected margin; the margins of Designer Brands and Foot Locker
fell from their 2012 to 2016 peaks to below 2% by FY2024, and the filer names its vendors' "increased direct-to-consumer
initiatives" as a risk (I do not claim from these filings that the one caused the other). That is a castle-less field, and
this company is not its strongest member. *Caveat on the DBI row:* its FY2009 figure is as carried in the XBRL facts of a
later 10-K, after the 2011 merger with Retail Ventures, and was not read in the original filing.

**The weighing of the contrary evidence written at the foundations.** (a) Survival without debt shows financial prudence,
not a castle; a business can stay solvent and still earn its rivals' price. (b) The FY2023 to FY2025 lead over peers is
three years against four years of losing comparable sales to the nearest of them, and it ended in a 0.3% first-half
margin. (c) Shoe Station's growth was partly bought (the 2021 purchase, $70.3M) and partly transferred from Shoe Carnival
stores; on a comparable basis it fell 8.5% in the latest quarter. (d) Family ownership is a Q5 and Q6 matter, not a
castle. (e) The price does not reopen a castle shown open: "What you can’t do is turn any investment into a good deal by
paying little" **[M2019-015]**; "If you really think a business is declining, most of the time you should avoid it."
**[M2012-062]**; "marginal businesses purchased at cheap prices may be attractive as short-term investments, they are the
wrong foundation" **[L2014-009]**.

**OUT or TOO HARD?** A castle whose future cannot be judged goes to TOO HARD, because "We don’t know how to valuate that"
**[M2000-019]**. This one's future is judged on the record, not unknown: the filer itself writes that the industry has few
barriers to entry, that competitors are larger, that the vendors are reducing the retailers they sell through, and that
promotion sets the margin; the comparable sales, the units, the share against the nearest peer and the reversed strategy
all run one way. The attacker test is answered yes, and of a yes the row says "If the answer had been yes, we wouldn’t
have done it." **[M2011-015]**; the industry is among those "that are just never going to have barriers to entry"
**[M2012-106]**; and the company is not "the low-cost producer" **[M1997-010]**. Of the rows' three boxes, "in, out, and
too hard" **[M2006-013]**, the framework's Q2 routing sends a castle shown open on the evidence to OUT, not TOO HARD.

- **VERDICT: OUT.** The castle is open. In the filer's words the industry has "few barriers to entry" (10-K Item 1A);
  of an attacker who can get in, the row: "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. The
  price is the rivals': "whatever he charged for gas was my price" **[M2012-109]**. The brand is the vendor's: "the brand
  is our protection against the intermediaries making all the money" **[M2019-041]**. It is not the low-cost operator:
  "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**. And it is losing ground: "In
  retailing, to coast is to fail." **[L1995-008]**.

---
## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (the file closed at Q2).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED as a verdict. The balance sheets were read in Step 0 above, as the template asks when the file closes before Q4; no confusion or suspicion was found there.
## Q5 — WHO RUNS IT. NOT REACHED. Facts gathered and not judged: chairman J. Wayne Weaver, 91, chairman since 1988; the Weavers own 31.5% (DEF 14A); interim chief executive Clifton Sifford, 72, a former chief executive, appointed 2026-02-24 with a one-time grant of 112,220 restricted stock units (8-K 0001193125-26-098464); chief financial officer W. Kerry Jackson, recalled from retirement in 2025 (8-K 0001193125-25-217451); fiscal 2026 bonus on "operating income before nonrecurring items" (8-K 0001193125-26-098464); departing chief executive's payments and costs $5.3M (10-Q).
## Q6 — WHAT WILL THEY DO WITH THE MONEY. NOT REACHED. Facts gathered: quarterly dividend raised to $0.17 (10-Q); $50M repurchase authority with no stated price (8-K 0001193125-25-316812); $7.0M spent at about $17.93 a share in the first half of fiscal 2026 (10-Q).
## Q7 — WHAT IS IT WORTH. NOT REACHED (computation at the owner's request below, not a verdict).
## Q8 — BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 — COULD IT RUIN US. NOT REACHED. Fact gathered: no debt; operating lease liabilities $354.6M; credit agreement of $100M expiring 2027-03-23, to be renewed in the second half of fiscal 2026 (10-Q).
## Q10 — THE FAT PITCH. NOT REACHED.
## Q12 — WOULD WE BE PROUD. NOT ASKED (optional; the file closed at Q2).

---
## COMPUTATION — NOT A CLEARANCE
*(Q2 closed the file OUT. The figures below are arithmetic at the owner's request, carry no entry language, and do not
reopen Q2: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**. Script: `Test Runs/_research 2026-10-05 SHOE/valuation.py`.)*

**(a) The value range by the Q7 convention** (Part VI): five-year average owner cash after every real cost, FY2021 to
FY2025, capital-spending basis, **$44.3M**; carried ten years at the growth shown, then zero nominal growth, discounted at
the 5.63% sovereign.
- *Growth shown.* The convention measures it on aggregate owner cash, but that series has a negative year (FY2022,
  −$32.3M), so no compound rate can be taken from it. **CONVENTION (this run's):** the growth shown is taken from net sales
  over the same years, $1,330.4M (FY2021) to $1,135.3M (FY2025), **−3.89% a year**. Rationale: it is the nearest measure
  of the same five years that has a rate, and it is negative, which the business's comparable sales confirm.
- No-growth end: $786.1M, **$28.92 a share**. Shown-growth end (−3.89% for ten years, then flat): $578.9M, **$21.30 a
  share**. Ratio of ends 1.36, inside three to one. Depreciation variant: $31.57 to $42.86.
- Cash: $118.0M of cash and equivalents at 2026-08-01 ($4.34 a share); the $13.6M of marketable securities fund the
  deferred-compensation liability and are left out. Counting only cash above a $60M working floor (see (b)), $2.13 a share.
- **Value range: $21.30 to $28.92 a share for the business, $23.43 to $31.05 with surplus cash, against $12.76.**
- *What the range does not say.* Its base year FY2021 is the pandemic windfall (owner cash $111.0M, operating margin
  15.6%), and its owner cash leaves out the $115.5M spent on the two acquisitions that bought sales while comparable sales
  fell; with them deducted the five-year average is $21.2M. The latest half earned $631K of net income. The convention
  range therefore sits far above what the business now earns, and a price below it is not a finding about value: Q2 has
  already said why.

**(b) The fair price** (the price at or below which the expected return on the central case clears the floor of about ten
percent pre-tax, the Part VI CONVENTION from "we don’t want to buy equities where our real expectancy is below 10 percent"
**[M2003-149]** and "at least 10% pre-tax returns" **[L2002-020]**).
- **Central case (my judgment, labelled as such):** pre-tax owner cash of **$35M a year, falling 3% a year.** Basis: the
  pre-pandemic operating margin averaged 4.75% (FY2009 to FY2019) and 4.3% (FY2003 to FY2019); applied at about 3.3% to
  sales of about $1.08B (fiscal 2025 less the current decline) it gives about $35M, with capital spending taken equal to
  depreciation (fiscal 2026 guidance $17 to $20M against depreciation of about $34M, so the near term is lighter) and the
  recurring rebanner, impairment and severance charges ($24.1M in fiscal 2025, $13.6M in the first quarter of fiscal 2026)
  treated as a business that keeps paying such costs. The 3% decline is below the 7.4% average fall in comparable sales
  of FY2022 to FY2025 and near the −4.7% of the latest half, softened by store closures that lift the average store.
- **CONVENTIONS (this run's):** expected pre-tax return = central owner cash ÷ (market value − surplus cash) + the growth
  rate (here −3%); surplus cash = cash and equivalents above $60M, the bottom of the filer's own year-end range of $62M to
  $132M over five years (10-K Item 1), taken as the cash a seasonal retailer keeps.
- At the floor: enterprise value $35M ÷ (10% + 3%) = $269.2M; plus $58.0M surplus cash = $327.2M; **fair price $12.04 a
  share.** At $12.76 the central case returns about **9.1% pre-tax**, just below the floor.
- After-tax equivalent: 10% pre-tax is **about 7.4% after tax at the filer's fiscal 2025 effective rate of 25.7%** (10-K
  MD&A, Income Taxes). The 10-Q expects about 37% for fiscal 2026, inflated by non-deductible severance; not used.

**(c) The cheap price** (below which the case needs no pencil). **My rule (CONVENTION of this run):** the price at which
the floor still clears on the stress case, so that the decision would not depend on the central case being right: "if you have to actually do it on — with pencil
and paper, it’s too close to think about" **[M1996-084]**; "It should scream at you." **[M2009-005]**. Stress case: pre-tax owner cash $25M (about this fiscal year's underlying run rate: the
first half earned about $15M of operating income before $13.6M of charges and the second quarter's operating income fell
from $25.2M to $7.6M), falling 5% a year. Enterprise value $25M ÷ 15% = $166.7M; plus $58.0M; **cheap price $8.26 a share.**

**Against the price:** $12.76 sits above the fair price ($12.04) and well above the cheap price ($8.26), and far below the
convention range ($21.30 to $28.92), whose base the pandemic year inflates. None of this is a clearance; the file closed
at Q2.

---
## THE BOX
**OUT, at Q2.** The castle is shown open on the evidence: "highly competitive with few barriers to entry" in the filer's
own words; margins set by promotional rivals and by vendors who own the brands and are cutting their retailers (Nike
33% of sales in FY2020, 14% in FY2022); not the low-cost operator over FY2009 to FY2019 (4.75% operating margin against
5.58%, 6.15% and 8.58% for the three peers); comparable sales negative four years and into the fifth, units down about
13% in fiscal 2025, ground lost to Famous Footwear each of those years; the rebanner strategy reversed and the chief
executive gone. Not reached Q7; computation only: convention range $21.30 to $28.92 a share against $12.76; fair price
$12.04; cheap price $8.26.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template was copied first; the run.py, cover and EDGAR fetches came
      after). **Not written question by question, and not committed after each:** the task forbids commits, and the file
      was written in one pass after the reading, with the contrary evidence logged in the foundations as it was found in
      the reading. Declared, not hidden.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, see below); every filing fact carries its
      accession; numbers without a row or filing are labelled CONVENTION or judgment.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance; the valuation is headed COMPUTATION — NOT A
      CLEARANCE.
- [x] Owner cash is operating cash less stock pay less capital spending, never a net-income proxy (operator rule 5); the
      sovereign is the Treasury's; the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down, to "write it down in the first 30 minutes" **[M1997-127]** (five items, weighed
      in Q2).
- [x] No row dated after the anchor: not a point-in-time run; the anchor is today.
- [x] Only the arithmetic lines of `tools/run.py` were used; every line checked against the filing.
- [x] `python tools/check_framework.py` PASS before the file was left (see the result line at the end).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The Q7 range convention misleads on a declining business with a windfall in its window.** Its five-year average
takes FY2021, the pandemic year (owner cash $111.0M against $19.3M in FY2025), and it counts capital spending but not
acquisitions, though $115.5M of acquisitions bought the sales that offset falling comparable sales. The result is a range
($21.30 to $28.92) whose bottom is two thirds above the price while the business earned $631K in its latest half. Had Q2
passed, the convention would have read this as a possible screamer. The convention needs a sentence on a base window
that straddles a one-off year, and on whether cash spent on acquisitions to hold sales is capital spending.
(2) **"Growth shown" is undefined when owner cash has a negative year**, as here (FY2022). I used the net-sales rate over
the same years and confessed it; two analysts could choose differently.
(3) **The owner's fair-price request is not a framework rule**, and the framework does not say whether the ten percent is
measured on market value or on market value less surplus cash, nor how a declining case enters (as negative growth, or
as a lower base). I chose enterprise value and negative growth, both confessed; the fair price moves by about a dollar on
either choice.
(4) **Q1 and retail.** Q1's list of what it rules out gives retail as its narrated example, "it’s easy to sort of think you
understand retail, and then subsequently find out you don’t" **[M2014-052]**, but the routing sends to TOO HARD at Q1 only for fast change. Whether a retailer should be held at Q1 on
that row, or passed to Q2 as here, is not said. I passed it to Q2 because the doubt was about the castle, not the
economics.
(5) **The competitor row asks for "the same metric".** The nearest peer reports its shoe chain only as a segment whose
operating earnings exclude corporate costs, so the row compares unlike figures; the framework does not say whether a
segment figure may stand in.

*Check results (2026-10-05):* `python tools/check_framework.py` **PASS** (test runs: phantom ids in 0 files; v5 ledger
4279/4279 verbatim; v5 scope 0 outside). Run-file script check (`Test Runs/_research 2026-10-05 SHOE/check_ids.py` and a
stricter adjacency pass): 57 id citations, 42 distinct, all M/L/R ids present in `principle_ledger_v5.csv`, no E-ids,
and every id directly follows a quoted fragment found in that row.
