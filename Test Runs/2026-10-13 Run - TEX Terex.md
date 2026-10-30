# Company Run — Terex Corporation (NYSE: TEX) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**
*(Copied from `Test Runs/_TEMPLATE - Company Run.md` before any fetch; research folder `Test Runs/_research 2026-10-13 TEX/`.
A dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the brief's one stated departure: the lines of
evidence are derived by the analyst from the FY2025 10-K's Items 1, 1A and 7.)*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (TEX; also searched for Terex, no match); not held.*

**CONTAMINATION, declared:** (1) the session context shown at start carried the subjects of the five most recent commits
of the repository, which name another company's v5 run (a Hong Kong machinery maker, its box and its computed range); (2) a
directory listing of `Test Runs/` made to copy the template showed the file names of other runs dated 2026-10-12 (names
only), and a name filter for "TEX" showed the file names of runs on other companies whose tickers contain those letters
(names only, none about Terex; no prior Terex run file was listed); (3) the memory index loaded at start carried one-line
notes on the queue and on how many names had cleared. None of them was opened, and nothing of them is used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $51.49 (51.485, quote of 2026-10-13 through `tools/sources.py`; **aggregator, live quote only, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock $0.01 par, **114.3 million** outstanding as of
  2026-07-28 (10-Q for the quarter to 2026-06-30, filed 2026-07-30, accession `0000097216-26-000116`;
  `python Screens/cover_shares.py TEX`). Checked against the same 10-Q's balance sheet: issued 134.4 million less 20.8 million
  in treasury = 113.6 million at 2026-06-30, the 0.7 million gap falling in the four weeks to the cover date. The REV merger
  issued 47.9 million shares on 2026-02-02 (8-K of 2026-07-31, Exhibit 99.2, accession `0000097216-26-000124`, Note 2:
  "In connection with the Merger, there were an additional 47.9 million shares of Terex issued upon conversion"); they are
  inside the cover count, since 85.5 million issued at 2025-12-31 became 134.4 million at 2026-06-30. No 8-K after the 10-Q
  issues shares (filing list read through the 8-K of 2026-08-03, accession `0000097216-26-000130`).
- **Market cap:** 114.3 million x $51.485 = **$5,885M**.
- **Net debt at the latest filed date (2026-06-30, 10-Q `0000097216-26-000116`, Note I):** total debt $2,687M (5% notes 2029
  $597M, 6.25% notes 2032 $737M, term loan 2031 $1,214M, revolver $110M, secured borrowings $20M, finance leases $9M) less cash
  $407M = **$2,280M**. Operating leases left out, said so. The REV cash consideration ($548M including REV's bank debt repaid,
  against $81M of REV cash acquired) is inside these balances, the merger having closed on 2026-02-02.
- **Sovereign for the earnings currency (USD):** **5.60%**, US Treasury daily par yield curve, 30-year, 10/09/2026
  (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-13, accession `0000097216-26-000035` (Items 1, 1A, 7, 8);
  10-Q for the quarter to 2026-06-30, filed 2026-07-30, `0000097216-26-000116`; proxy (DEF 14A) filed 2026-04-29,
  `0000097216-26-000071`; 8-K of 2026-07-31 with REV's last quarter and the pro forma combination, `0000097216-26-000124`;
  the 10-Ks for FY2018 to FY2024 (`0000097216-19-000024`, `-20-000027`, `-21-000030`, `-22-000013`, `-23-000012`,
  `-24-000013`, `-25-000011`); REV Group's 10-Ks for FY2021 to FY2025 (`0001564590-21-060365`, `0000950170-22-026493`,
  `0000950170-23-069876`, `0000950170-24-135208`, `0001193125-25-313470`). **One figure cross-checked against the filed
  statement:** net cash provided by operating activities FY2025 **$440M**, read on the filed Consolidated Statement of Cash
  Flows (10-K `0000097216-26-000035`, page F-8), equal to the XBRL figure `tools/run.py` printed.
- `python tools/run.py TEX` arithmetic lines only (output kept at `Test Runs/_research 2026-10-13 TEX/run_py_output.txt`):
  operating cash $459M, $326M, $440M (FY2023 to FY2025); stock pay $44M, $30M, $32M; capex $127M, $137M, $118M; D&A $56M,
  $82M, $157M (FY2025 includes the amortization of ESG intangibles). Its "capex alt" column doubles capex by adding a
  company-tagged line (`tex:PaymentstoAcquireProductiveAssetsincludingdiscontinuedoperations`) that is the same payment
  under another tag; the filed cash-flow statement shows one capex line ($118M for FY2025), so the alternate is a double
  count and is not used. Five-year owner cash and the recast are built at Q4 from the filed statements.
- **The balance sheets, ten year-ends, read in Step 0 because the file closes before Q4** **[M2025-032]** (`tools/run.py`
  table of first-filed XBRL figures, checked against the filed balance sheets of the FY2018, FY2023 and FY2025 10-Ks and the
  10-Q at 2026-06-30; $M):

| year-end | assets | equity | goodwill + intangibles | cash | receivables | inventory | debt | retained earnings | sales |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 5,007 | 1,485 | 278 | 428 | 512 | 854 | 1,576 | 1,898 | 4,443 |
| 2017 | 3,462 | 1,222 | 288 | 626 | 580 | 970 | 985 | 1,996 | 4,363 |
| 2018 | 3,486 | 860 | 278 | 368 | 660 | 1,212 | 1,219 | 749 | 5,125 |
| 2019 | 3,196 | 932 | 280 | 535 | 402 | 848 | 1,176 | 771 | 4,353 |
| 2020 | 3,032 | 922 | 283 | 665 | 381 | 610 | 1,174 | 750 | 3,076 |
| 2021 | 2,864 | 1,110 | 293 | 267 | 508 | 814 | 674 | 937 | 3,887 |
| 2022 | 3,118 | 1,181 | 301 | 304 | 548 | 988 | 776 | 1,201 | 4,418 |
| 2023 | 3,616 | 1,672 | 311 | 371 | 548 | 1,186 | 623 | 1,675 | 5,152 |
| 2024 | 5,730 | 1,832 | 2,200 | 388 | 643 | 1,147 | 2,584 | 1,964 | 5,127 |
| 2025 | 6,139 | 2,095 | 2,118 | 772 | 712 | 1,109 | 2,584 | 2,139 | 5,421 |
| 2026-06-30 | 10,344 | 4,925 | 5,464 | 407 | 1,157 | 1,656 | 2,687 | 2,121 | (half-year 3,972) |

  What moved and why. (1) **Equity against goodwill and intangibles:** tangible equity was about $1.2B in 2016 and $1.36B
  in 2023; after ESG (goodwill $803M and intangibles $1,113M on a $2,010M price, 10-K FY2024 Note D) it fell to about
  -$370M at 2024-12-31, and after REV (goodwill $1,470M, intangibles $1,989M, 10-Q Note on the merger) it is about -$540M at
  2026-06-30: the equity now rests entirely on purchased goodwill and intangibles. (2) **Equity and retained earnings in
  2017 and 2018:** equity fell from $1,485M to $860M while the company bought back $925M (2017) and $428M (2018) of stock,
  funded in part by the sale of MHPS ($776M of divestiture proceeds in 2017, XBRL); retained earnings fell from $1,996M to
  $749M in 2018 because "On December 21 2018, the Company retired 50.0 million shares of its common stock held in treasury"
  (10-K FY2018, `0000097216-19-000024`), not because of losses. (3) **Debt:** cut from $1,576M (2016) to $623M (2023), then
  raised to $2,584M for ESG (6.25% notes and a $1,250M term loan, 2024-10-08) and to $2,687M with the REV cash leg; no
  maturity before May 2029. (4) **Inventory against sales:** 19% of sales in 2016 and 2019, 22% to 23% in 2022 and 2023
  (inventory rose $372M in two years ahead of a sales fall), 20.5% in 2025 after a release; receivables 9% to 13% of
  sales. The 2025 operating cash of $440M owed much to that release ("Working capital reductions remain a key priority",
  Item 7; inventories +$39M and payables +$118M in the 2025 cash flow). (5) **What the figures do not say:** the 2016 to
  2019 columns include businesses since sold (MHPS, cranes), and the 2026 column includes REV, so no two of these years
  describe the same company; "what the figures are saying and what they don’t say and what they can’t say" **[M2025-032]**.

## THE FOUNDATIONS (not a gate)
A share is a business, and the test is the closed market: "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**. For Terex the answer turns on what its businesses earn through a fall in their customers' spending, since the
company sells equipment to rental fleets, quarries, haulers, utilities, municipalities and RV buyers. The market serves and
does not instruct, "It just tells us prices." **[M2006-077]**: the $58.99 at which the company issued 47.9 million shares to
REV's holders on 2026-02-02 and the $51.49 quoted today are prices, not findings. Who is paid to tell you bears on the two
deals of 2024 and 2026 and on the company's yearly EBITDA and EPS outlook: "you do not get impartial advice from Wall
Street" **[M2020-037]**. The margin of safety is an attitude here **[M1996-084]**. **Contrary evidence, written down as found**
**[M1997-127]**: (1) debt rose from $623M at 2023-12-31 to $2,687M at 2026-06-30, through the ESG purchase (cash, borrowed) and
the REV merger (its cash leg from the revolver and cash); (2) the 10-K says the company competes "particularly" on price and
that "Low-cost competition from China and other developing markets could also result in decreased demand for our products"
(Item 1A), and the Aerials segment margin fell to 5.0% in 2025; (3) the segment measure changed in 2026 to "Adjusted segment
operating profit" (10-Q, Note B); (4) the portfolio has been remade repeatedly, "much of this change has been historically
accomplished through acquisitions and managing our portfolio of companies by divestiture of non-core businesses and
products" (Item 1), so the past statements are statements of a different set of businesses; (5) the first-filed FY2016
figures show an operating loss of $147.8M (XBRL OperatingIncomeLoss, FY2016 vintage).

## THE STANDING RULE
The buyer's own conduct: a purchase of these shares for cash, unborrowed, sized so that a fall of half or more could be sat
through, puts the buyer at no risk of ruin. "We are never going to risk what we have and need for what we don’t have and
don’t need." **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target's own debt
is Q9's question, not this one.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The lines of evidence, chosen from the FY2025 10-K (the brief's departure: derived here, not handed down).** From Item 1
(business and segments): four reportable segments from 2026-02-02, Environmental Solutions (refuse bodies, compactors,
utility digger derricks and insulated aerials), Materials Processing (mobile and static crushing and screening, washing,
conveyors, material handlers, concrete mixers and pavers), Specialty Vehicles (REV's fire apparatus, ambulances, terminal
trucks, sweepers and Class A and C motorhomes) and Aerials (Genie booms, scissors, telehandlers); the competitor table names
the rivals product by product. From Item 1A (risks): price competition and "Low-cost competition from China and other
developing markets"; the anti-dumping and countervailing duties on Chinese mobile access equipment in the US and the EU; the
debt raised for ESG and REV and the integration of REV. From Item 7 (MD&A): the 2025 results by segment (ES sales up 12.7% on
the filer's pro forma basis, MP down 11.6%, Aerials down 14.5% with a 5.0% margin), working-capital release as the main
source of 2025 cash, the 2026 EBITDA and EPS outlook, and the adjusted ROIC. The lines chosen: (1) each part's economics
and which part decides; (2) the castle of the deciding part against its named rivals over a full cycle; (3) the cyclicality
of the rental and dealer channels; (4) the two deals and the debt; (5) the habits of guidance and adjusted figures.

**The parts, and which one matters (Q1's holding-company paragraph, with Q2's threshold).** Five-year operating profit,
FY2021 to FY2025, from the segment notes (Terex 10-K FY2023 `0000097216-24-000013` for 2021 and 2022, 10-K FY2025
`0000097216-26-000035` for 2023 to 2025 as recast; REV Group's operating income from its 10-Ks FY2021 to FY2025, REV being
the whole of the new Specialty Vehicles segment):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year | share of the parts' total ($3,264M) |
|---|---|---|---|---|---|---|---|
| Materials Processing | 240.9 | 297.8 | 358.6 | 252 | 234 | 1,383 | 42% |
| Aerials | AWP 152.1 (with Utilities) | AWP 196.2 (with Utilities) | 321 | 271 | 103 | 695 to 1,043 | 21% to 32% |
| Environmental Solutions | inside AWP | inside AWP | 50 (Utilities only) | 82 (ESG from 2024-10-08) | 234 | 366 to 714 | 11% to 22% |
| Specialty Vehicles (REV, FY to October) | 83.8 | 36.8 | 88.6 | 79.6 | 182.2 | 471 | 14% |

The filings do not split AWP's 2021 and 2022 profit between Genie and Utilities, so Aerials and ES are shown as ranges; on
any split **Materials Processing is the largest part** and, at 42%, no part carries more than half. By the business-of-parts
CONVENTION (Q2, adopted 2026-10-06), MP decides, and it is the part that "matters" for Q1. *(The whole-company picture moves
toward ES and SV: ESG was owned for fifteen of the sixty months and REV only from 2026-02-02; in the half-year to 2026-06-30
the adjusted segment profits were ES $145M, MP $140M, SV $146M, Aerials $25M, 10-Q Note B. The threshold is applied to the
five-year record as the convention states it; see the section on what was unclear.)*

**The tests, applied to MP.**
- *Where it will be in ten years* **[M2000-037]**: a maker of tracked and static crushers, screens, washing plants and
  conveyors sold through "a global network of independent distributors, direct sales and rental companies" (Item 1) to
  quarries, contractors and recyclers. The product changes slowly (diesel to hybrid and battery drives, offered across "A
  majority of our product portfolios", Item 1, Research); nothing in the filings points to a technology that would make
  the machines obsolete inside ten years, so the change routing of Q1 **[M1998-008]** is not engaged.
- *The key variables and how predictable they are* **[M1998-044]**: unit demand from aggregates and recycling, which the
  10-K ties to infrastructure spending, interest rates ("high interest rates which remain a headwind for rent to own
  conversions", Item 7) and European demand; dealers' restocking; and price against steel and engine costs. They are
  cyclical but not opaque: MP's sales fell 22% from 2019 to 2020 and 25% from 2023 to 2025, and its margin stayed between
  9% and 16% in every year from 2016 to 2025 (segment notes; see Q2).
- *Do the past statements tell me the future ones?* **[M2008-033]** For MP, largely yes: the segment has kept its shape
  through the recasts (cranes moved in, tower and rough-terrain cranes sold in 2025), and its ten years of figures are a
  readable cycle. For the company as a whole, less so: the portfolio has been remade (MHPS sold 2017, cranes 2019 and
  2025, ESG bought 2024, REV merged 2026), which is weighed at Q6, not here.
- *Important and knowable?* **[M2006-076]**: the economics of a dealer-sold capital-goods maker are knowable; "I understand
  the economic dynamics of the industry" **[M2011-014]** is the standard, not the metallurgy.
- *Would insiders write it down?* **[M2000-105]**: a quarry-equipment maker's insiders would write down a ten-year view of
  aggregates demand and their own cost base; this is not a field where they would say "That’s too hard." **[M2000-105]**.
- *Can I name the winner?* **[M2012-067]**: not from the filings read so far; that is Q2's question, and it is where the
  doubt in this file sits.
- *How far off could I be?* **[M2011-084]**: by the cycle's full swing, about a quarter of sales and a few points of
  margin, which the range at Q7 must carry.
- *Do I doubt it is inside?* **[M2002-092]**: not as to the economics of the deciding part. The doubt concerns Aerials,
  whose ten-year margins hang on trade duties against Chinese makers (Item 1A), a part that does not decide and is carried
  forward.

**VERDICT: IN.** The deciding part, MP, is a dealer-sold maker of crushing and screening machinery whose economic
dynamics can be read from ten years of segment figures, which is "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]** as to the earning power; whether the competitive
position lasts is put to Q2. Filing facts: 10-K FY2025 Items 1, 1A, 7 and Note B (`0000097216-26-000035`); segment notes of
the FY2018 to FY2024 10-Ks; REV 10-Ks FY2021 to FY2025.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question is put to the deciding part, Materials Processing (Q1's parts table: 42% of five-year segment profit, the
largest part, none above half), as the business-of-parts CONVENTION directs: "lumping them together [...] impedes
analysis" **[L2008-005]**. The other parts are read after it, as non-deciding parts.

**MP over the whole span, from the filer's segment notes** (operating profit and margin; identifiable assets where filed):

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| MP net sales ($M) | 944.5 | 1,119.8 | 1,322.6 | 1,602.6 | 1,256.8 | 1,691.8 | 1,941.6 | 2,227.0 | 1,902 | 1,681 |
| MP operating profit ($M) | 86.6 | 125.1 | 176.0 | 227.9 | 143.4 | 240.9 | 297.8 | 358.6 | 252 | 234 |
| margin | 9.2% | 11.2% | 13.3% | 14.2% | 11.4% | 14.2% | 15.3% | 16.1% | 13.2% | 13.9% |
| identifiable assets ($M) | | | | | 1,596.3 | 1,648.0 | 1,800.1 | 2,091.4 | 1,885 | 1,964 |
| profit on identifiable assets, pre-tax | | | | | 9.0% | 14.6% | 16.5% | 17.1% | 13.4% | 11.9% |

Sources: 10-K FY2018 `0000097216-19-000024` (2016); 10-K FY2019 `0000097216-20-000027` (2017, 2018 as recast that year);
10-K FY2021 `0000097216-22-000013` (2019 to 2021, assets 2020 and 2021); 10-K FY2023 `0000097216-24-000013` (2022, 2023 and
assets); 10-K FY2025 `0000097216-26-000035` (2024, 2025 and assets). The series mixes recast vintages (cranes were moved
into MP and later sold), which is stated, not smoothed. The 2025 figure includes the gain on the sale of the tower and
rough-terrain cranes businesses, which the filer names as a cause of the 13.9% margin and removes as $41M of "Divestitures"
in its adjusted reconciliation (Item 7); without it MP earned about $193M, 11.5% of sales.

**The castle tests, each with its filing fact.**
- *The key factors and how permanent* **[M1995-038]**: the filing names brands (Powerscreen, Finlay, Cedarapids, Fuchs and
  others), a global dealer network, and manufacturing in Northern Ireland, India, Malaysia and the US (Item 1). It names no
  patent, no cost advantage and no market share. Its own account of how it competes: "We compete with other manufacturers
  based on many factors, particularly price, performance and product reliability" and "in some instances, customers may
  prefer the pricing, performance or reliability aspects of a competitor’s product despite our product pricing or
  performance" (Item 1, Competition).
- *Would it stand without the lord?* **[M1996-037]**: nothing in the filings ties MP's results to one person; the segment
  has had several presidents and kept its margins. This test passes.
- *The money test* **[M2011-015]**, **[M2000-077]**: the 10-K lists seven primary rivals in crushing and screening alone
  ("Astec Industries, Deere (Kleeman), Keestrack, Metso, Portafill, Rubble Master and Sandvik") and others in each of the
  adjacent lines; it says that "Some of our competitors are smaller companies which may have lower operating costs and
  greater operational flexibility" and that "Other competitors are large, well-established companies with capacity,
  financial and other resources that may be in excess of ours" (Item 1A). A field in which both smaller lower-cost makers
  and larger richer ones are named as primary rivals is not one where a well-funded attacker is shown to be helpless; the
  filing gives no reason why one could not take share.
- *Pricing power, and the agony before a rise* **[M2005-020]**, **[M2005-017]**: MP's margin rose from 14.2% (2021) to
  16.1% (2023) through the steel and logistics inflation of those years, which is evidence of costs passed through. It is
  not evidence peculiar to Terex: the rival that files with the SEC reported the same, Astec's Materials Solutions EBITDA
  rising in 2022 "from the impact of favorable volume, pricing and mix that generated $51.3 million higher gross profit
  partially offset by the impact of higher inflation" (Astec 10-K FY2022, `0000792987-23-000015`). The whole field priced
  through that inflation.
- *Unit volume and share of mind* **[M1999-054]**: the filer gives no unit or share figures; MP's sales fell 14.6% in 2024
  and 11.6% in 2025, the 2025 fall attributed to "macro uncertainty, high interest rates [...] and weak European demand" (Item 7). The
  backlog rose 22% to $391M at 2025-12-31 (Item 1).
- *The low-cost position* **[L2000-017]**, **[M2001-013]**: no filing read states MP's costs against Metso's, Sandvik's or
  Kleemann's; the only cost statement is the one above, that some rivals "may have lower operating costs". The test cannot
  be answered from the filings read.
- *Would the customer still choose it over the low bid?* **[M2017-009]**: the filing's own sentence is that customers may
  prefer a competitor's "pricing, performance or reliability" despite Terex's; no fact read shows customers paying more for
  a Terex machine.
- *Ask the competitors* **[M1999-130]**: Astec names Terex among its Materials Solutions rivals, with "McCloskey
  International (part of Metso Corporation)", Metso, Sandvik, the Wirtgen Group, Epiroc, Weir and others, and calls the
  segment "highly competitive and fragmented" facing "strong competition in product performance, product innovation, range
  of products offered, service and price" (Astec 10-K FY2025, `0000792987-26-000011`, Item 1).
- *Widening or narrowing* **[M1999-108]**, **[L2005-010]**: margin 16.1% (2023) to 13.2% (2024) to about 11.5% (2025 without
  the cranes gain) on falling volume; profit on identifiable assets 17.1% to 11.9%. Narrowing over the last two years; over
  the decade, wider than in 2016 (9.2%). A cyclical swing and a secular one cannot be told apart from these figures alone.
- *What could destroy it* **[M2000-014]**: the filer names Chinese low-cost competition and rivals' new products and
  electrification (Item 1A); none is quantified for MP.

**The competitor row** (same metric, from the rivals' own filings; the 10-K's named rivals that file with the SEC; up to three):

| Rival (Terex part compared) | Metric | Years and figures | Accession |
|---|---|---|---|
| Astec Industries, Materials Solutions (formerly Aggregate and Mining Group) vs Terex MP | segment profit as Astec defines it (to 2019), then Segment Operating Adjusted EBITDA (before D&A, so more generous than Terex's operating profit) | A&M 2018 $45.5M on $453.2M (10.0%), 2019 $22.8M on $405.0M (5.6%); Materials Solutions 2021 $39.1M on $352.1M (11.1%), 2022 $44.5M on $422.7M (10.5%), 2024 $37.2M on $467.7M (8.0%), 2025 $55.6M on $553.0M (10.1%). Terex MP: 13.3%, 14.2%, 14.2%, 15.3%, 13.2%, 13.9% in the same years, on operating profit | `0001140361-20-006100`, `0000792987-23-000015`, `0000792987-26-000011` |
| Oshkosh, Access segment (JLG) vs Terex Aerials (AWP until 2022, with Utilities) | segment operating income / sales | FY2019 12.3%, FY2020 7.9% (years to September); 2021 8.7%, 2022 7.9%, 2023 14.8% ($738.8M on $4,990.0M), 2024 15.6% ($805.4M on $5,164.7M), 2025 11.2% ($502.0M on $4,494.4M). Terex: 2019 7.2%, 2020 0.0%, 2021 7.0%, 2022 7.9%, 2023 13.6%, 2024 11.2%, 2025 5.0% | `0001564590-20-054491`, `0000950170-23-003473`, `0001193125-26-054061` |
| Federal Signal, Environmental Solutions Group vs Terex ES (refuse; Federal Signal's refuse line New Way was bought on 2025-11-25, so the products overlap only in part) | segment operating income / sales | 2023 14.5% ($209.2M on $1,437.9M), 2024 16.8% ($261.2M on $1,557.1M), 2025 17.7% ($324.6M on $1,837.5M). Terex ES: 2023 8.7% (Utilities only), 2024 10.0%, 2025 13.8% | `0001628280-26-011576` |
| Context, not one of the three: Oshkosh Vocational (Pierce fire apparatus, McNeilus refuse) vs REV / SV | segment operating income / sales | 2023 7.2%, 2024 12.0%, 2025 14.7%. REV operating margin FY2023 3.4%, FY2024 3.3%, FY2025 7.4% | `0001193125-26-054061`; REV 10-Ks |

**Named rivals that do not file with the SEC, flagged:** Metso, Sandvik, Keestrack, Rubble Master, Portafill (crushing and
screening); CDE Global, McLanahan, Superior, Weir (washing, conveyors); Liebherr, Sennebogen (handlers); Dingli, Haulotte,
JCB, Linamar (Skyjack), Manitou, MEC, Sinoboom, XCMG, Zoomlion (Aerials); Labrie, Altec and the other ES rivals. Deere files
but reports Kleemann inside its Wirtgen business, not separably; Caterpillar files and is not separable either.

**The parts table** (Q1's figures; the file closes on the deciding part):

| Part | share of five-year operating profit | castle, on the filings read | decides |
|---|---|---|---|
| Materials Processing | 42% | returns above the one SEC-filing rival over a full cycle; no cost, price or share evidence against Metso, Sandvik and Kleemann; the filer says it competes "particularly" on price | **yes** (largest part) |
| Aerials | 21% to 32% | below the leader (JLG) in six of the seven years compared and level in the seventh; rental-company customers; duties needed against Chinese makers (Item 1A); 5.0% margin in 2025 | no |
| Environmental Solutions | 11% to 22% | Heil and the other ESG brands bought in 2024; margins below Federal Signal's ESG in each of the three years; ES owned whole only from 2024-10-08 | no |
| Specialty Vehicles (REV) | 14% | REV's margins below Oshkosh Vocational's in each of the three years compared; RV line consumer-cyclical | no |

**The field's returns over the last full cycle, judged in words (section C).** MP earned double-digit operating margins in
every year from 2017 to 2025, held 11.4% in the 2020 trough, and earned 9% to 17% pre-tax on its identifiable assets
(which include its goodwill) from 2020 to 2025; the one rival readable from SEC filings, Astec, earned less on a measure
that flatters it. That is a better than ordinary return in this field, so the standing-castle-with-ordinary-returns OUT does
not apply **[L2007-004]**, **[M2013-052]**. But the returns of MP's three largest rivals, Metso, Sandvik and Kleemann, are not in
any filing read, and the filer itself names price as its first ground of competition and lower-cost rivals as a risk. The
evidence shows that MP has earned good returns; it does not show why, or why they will last against richer and cheaper
rivals for ten to twenty years.

**VERDICT: TOO HARD (WORK).** The castle of the deciding part cannot be judged from the filings read: "when we see a moat
that’s tenuous in any way [...] it’s just too risky. We don’t know how to valuate that, and therefore we leave it alone."
**[M2000-019]**; "too hard" is the box **[M2006-013]**. It is not shown open, so it is not OUT **[M2011-015]**. The cause is
WORK, not NATURE: the deciding question, whether MP holds a cost, price or share position against Metso, Sandvik and
Kleemann, is "important and knowable" **[M2006-076]** from those rivals' own published annual reports and segment
disclosures, which this run did not read (the brief limits the competitor row to rivals that file with the SEC); it is not a
forecast the industry's insiders would refuse to write down **[M2000-105]**. The research pass is written below, steps 1
and 2 only, and by Part VII it is closed unrun, because the COMPUTATION beneath the stop shows no case of the range earning
the floor at the price.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED** (Q2 closed the file TOO HARD (WORK)). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** The ten balance sheets were read in Step 0; the recast of owner cash and the habits found are under AFTER
THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.** Integrity facts found are recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** Facts found (the two deals, the buybacks, the pay plan) are under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED.** The arithmetic the owner asked for is under AFTER THE STOP, headed COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Debt facts are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** (No business named in Q12's list is among the segments: refuse and utility equipment, crushing and
screening machinery, fire apparatus, ambulances, terminal trucks, motorhomes, aerial platforms.)

---
## THE BOX
**TOO HARD (WORK)**, decided at **Q2**: the castle of the deciding part, Materials Processing (42% of five-year segment
profit), cannot be judged from the filings read; its returns beat the one SEC-filing rival's over a full cycle, but no
filing read shows a cost, price or share position against Metso, Sandvik and Kleemann, which do not file with the SEC or are
not separable, and the filer says it competes "particularly" on price. A research file is owed (Part VII), steps 1 and 2
written below; **closed unrun** under Part VII's 2026-10-12 rule, since the COMPUTATION beneath the stop shows no case of the
range earning the floor at the price (best case 6.26% against about 10%). COMPUTATION beneath the stop: value range
**$46.84 to $49.35 a share** (all-equity, organic pair, maintenance central) against **$51.49**; fair price **$17.66**
all-equity ($24.71 equity-only). **Integrity facts recorded, not judged** (guidance, adjusted figures featured, pay on
adjusted measures; see Q5 below).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box is unchanged (operator rule 2); each fact with its source* **[M1997-127]**.

**Bearing on Q3 (capital).**
- Capital spending ran well above depreciation from 2022: capex $109.6M, $127.2M, $137.0M, $118.0M (2022 to 2025) against
  depreciation of $42.4M, $51.7M, $58M, $69M (10-K FY2023 and FY2025, PP&E notes and cash-flow statements), while the
  legacy businesses' sales grew about 2.9% a year from 2021 to 2025 on the segment figures (Q7 computation below). The
  10-K calls the 2025 spending "to support business growth" (Item 7).
- What the two purchases earn on their price, on the filed figures: REV's operating income for FY2025 was $182.2M (REV
  10-K FY2025) against a provisional consideration of $3,384M (8-K `0000097216-26-000124`, Ex. 99.2, Note 2), 5.4% pre-tax
  on the price in REV's best year of the five (its five-year average operating income was $94M). ES, which holds ESG
  (bought for $2,010M) and Utilities, earned $234M in 2025 on identifiable assets of $2,755M (8.5% pre-tax).

**Bearing on Q4 (the accounts).**
- Owner cash after every real cost, as the computation recasts it (operating cash less stock pay less capital spending
  net of asset-sale proceeds; never a net-income proxy, operator rule 5): Terex $202.5M, $121.5M, $322.1M, $160.0M,
  $293.0M (2021 to 2025), average $219.8M; REV $125.8M, $58.1M, $79.3M, $13.1M, $177.7M (FY2021 to FY2025), average $90.8M.
  REV's FY2024 operating cash carried "higher income tax payments, including those associated with the sale of the Bus
  Manufacturing Businesses" (REV 10-K FY2025, MD&A); the amount tied to the sale is not stated, and the year is kept as filed.
- The filer features EBITDA in its own mouth: "We expect 2026 sales of between $7.5 billion and $8.1 billion, EBITDA
  between $930 million to $1 billion and earnings per share between $4.50 to $5.00" (10-K FY2025, Item 7); the 10-Q
  reconciles net income to "Adjusted EBITDA".
- The segment measure changed in 2026 to "Adjusted segment operating profit", recast for earlier periods (10-Q Note B);
  in the half-year to 2026-06-30 the adjusted segment total was $456M against GAAP operating profit of $105M, the gap
  being corporate costs ($147M), restructuring ($8M) and "Purchase Price Accounting" ($199M).
- The ROIC the company reports (11.7% at 2025-12-31) uses an "Effective tax rate as adjusted" of 13.5% against the reported
  24.3%, and an operating profit "as adjusted" that adds back restructuring, purchase-price accounting, deal and litigation
  costs and removes the $41M divestiture gain (10-K FY2025, Item 7, ROIC tables).
- Restructuring charges recur in every quarter of 2025 ($6M, $12M, $5M, $5M; same tables) and in 2026 ($8M in the half).
- Carryforwards: the foreign operating losses that are not reserved "do not expire" ($299M Germany, $159M Italy, $29M Spain;
  10-K FY2025, tax note), so no shelter runs out inside ten years and Q7's section E pricing of an expiring shelter does
  not arise.

**Bearing on Q5 (integrity facts recorded, not judged).**
- Guidance is given every year in the 10-K (EBITDA and EPS outlook above). The FY2024 10-K's 2025 outlook was net sales of
  $5.3 to $5.5 billion and EPS of $4.70 to $5.10 (printed in square brackets in the filing) (10-K FY2024, `0000097216-25-000011`, Item 7); 2025 net sales were $5,421M
  and GAAP diluted EPS $3.33 (10-K FY2025). Whether the outlook's EPS was an adjusted figure was not read.
- Annual incentive: 80% on financial targets, of which Operating Profit (which "excludes certain unusual and non-recurring
  items such as one-time gains and losses") against the plan, "$604 million for the Company, $264 million for MP, and $264
  million for ES", and net working capital (proxy 2026, `0000097216-26-000071`, CD&A).
- Long-term incentive: 65% performance-based on adjusted ROIC (target 11.7% for 2025, achieved 11.6%) and three-year
  relative TSR against a peer group, 35% time-based (proxy, CD&A). CEO total compensation $7.29M in 2025, $6.62M in 2024
  (Summary Compensation Table).
- Chief executive Simon Meester since 2024-01-01, formerly president of Genie and of the Aerials business; holds 328,370
  shares; non-executive chairman David A. Sachs holds 421,286 shares (proxy, beneficial ownership table).
- The habits named here are the kind Q4 weighs and Q5 judges **[M1994-018]**, **[L2002-041]**, **[L2016-006]**, **[L2019-006]**;
  any later run that reaches Q5 must answer them **[M2013-088]**.

**Bearing on Q6 (the money and the owners).**
- ESG: $2,010M in cash (10-K FY2024, Note D), financed with the 6.25% notes and the new term loan. REV: a merger by the
  2026-10-12 definition (a deal paid in both is classed by the larger part; $2,828M of the $3,384M was Terex stock, 47.9
  million shares at $58.99 on 2026-02-02, and $548M cash including REV's bank debt). Q6's STOP on an all-stock deal in
  undervalued stock **[L2009-019]** would have to be tested against Terex's own value when the shares were issued; the
  COMPUTATION for Terex alone (FY2021 to FY2025 averages, net debt and 64.9 million shares at 2025-12-31, same method as
  Q7 below) gives a central range of $58.49 to $63.59 a share (all-spending pair beside: $44.93 to $63.59), so the shares
  were issued inside that range, near its bottom. Not judged.
- Buybacks: $63M (2023, 1.3 million shares), $50M (2024, 0.9 million), $56M on the statement of equity (2025, 1.4 million;
  the MD&A gives "1,360,706 shares of common stock for $53 million", about $39 a share). The programmes name sums, not prices
  ("authorized the repurchase up to $150 million", December 2022 and July 2025; 10-K FY2025 Item 5) **[L2016-002]**.
- Dividends $43M to $46M a year 2023 to 2025 ($0.17 a quarter in 2025).
- The 10-K's stated policy is continued buying: "We continue to build and actively pursue our inorganic investment
  pipeline" (Item 1). Net purchases of businesses over FY2021 to FY2025, Terex and REV together, were $1,634M against owner
  cash before purchases of $1,848M, which makes the company a serial acquirer by Q7's 2026-10-12 convention.

**Bearing on Q9 (debt).**
- Net debt $2,280M at 2026-06-30 (Step 0). Pre-tax earnings over interest, the coverage the rows use **[L2012-002]**: 2025
  ($292M + $177M) / $177M = 2.6x; the half-year to 2026-06-30 ($13M + $97M) / $97M = 1.1x, after the REV purchase-price
  charges. Maturities: 5% notes May 2029 ($600M), revolver October 2029, term loan October 2031, 6.25% notes October 2032.
  The revolver's 3.00x first-lien net leverage covenant is tested only when more than 30% of the commitments are drawn (10-Q
  Note I). Credit guarantees to customers' lenders: maximum exposure $50M (10-Q).

**Bearing on Q7 and the owner's reporting figures. COMPUTATION, NOT A CLEARANCE.** *(No entry language; neither figure
is a verdict, operator rule 3. Script and output: `Test Runs/_research 2026-10-13 TEX/q7_computation.py`, `q7_output.txt`,
`q7_sensitivity.py`, `q7_sensitivity_output.txt`.)*
- **Basis.** All-equity (central): owner cash before interest and after the company's own cash taxes, against market value
  plus net debt; net debt $2,280M at 2026-06-30 with the REV cash leg inside it; operating leases left out. Equity-only beside:
  owner cash after today's interest ($45M net interest in the quarter to 2026-06-30, times four, after the 24.5% statutory
  rate the filer uses in its pro forma note). Interest added back at 24.5%. Rate 5.60% (Treasury 30-year, 10/09/2026). Ten
  years, then zero nominal growth.
- **The window and the merger.** FY2021 to FY2025 for Terex; REV, merged on 2026-02-02 (after the window, before the price
  date, paid mostly in shares), valued on its own filed five-year record (FY2021 to FY2025 to October), with its shares in
  the 114.3 million count and its cash leg in net debt, which is the combined companies' averages. Owner cash before
  interest: Terex $264.8M, REV $104.8M, **combined $369.5M** (all spending); after maintenance only, **$427.5M**.
- **(a) Cycles.** Neither end year is the series' peak or trough (owner cash peaked in 2023 at $322.1M and was lowest in
  2022 at $121.5M for Terex), and the filer describes neither 2021 nor 2025 as aberrational; the literal window is the base.
- **(b) Decline.** No negative growth shown; not engaged.
- **(c) Acquisitions.** Net purchases over the window ($1,634M: ESG $2,001M and three small deals, less the cranes sale
  $109M and REV's divestitures of $374.2M, chiefly the bus businesses) exceed half of owner cash before purchases ($924M), so by the serial-acquirer
  CONVENTION the central figure is the **organic pair**: purchases left out, organic growth. The filer reports no organic
  growth for the window, so it is built from the segment notes: legacy Terex (MP plus AWP) $3,870.6M in 2021 against MP
  $1,681M plus Aerials $2,060M plus Utilities held at its 2024 level of $594M (ES 2024 $822M less ESG's $228M since
  2024-10-08; no 2025 Utilities figure is filed) = $4,335M in 2025, **2.87% a year**; REV's reported sales, divestitures
  inside, $2,380.8M to $2,463.5M, **0.86% a year** (understating REV's organic rate); combined, weighted by owner cash,
  **2.30% a year**. The default pair is shown beside: owner cash after net purchases averages $42.7M, total sales growth
  8.67% a year, value **-$6.67 a share** at 5.6% (the ESG purchase inside the window swamps it).
- **(d) Working capital** is inside operating cash in every year (2025's release included).
- **(e) Maintenance central.** The filing allows the guess with depreciation as the proxy **[M1998-127]**, **[M2000-144]**:
  Terex depreciation $44.3M to $69M a year against capex of $59.7M to $137M; REV depreciation $22.2M to $25.2M against
  $24.7M to $51.1M. Central: the no-growth end on owner cash after maintenance only; the growth end on owner cash after all
  spending, so the growth spending is charged against the growth it buys and never also capped.
- **(f) The cap.** 2.30% is below the discount rate; carried ten years, owner cash after all spending would be about $464M,
  5.9% of 2025 pro forma combined sales of $7,885M (8-K `0000097216-26-000124`, Ex. 99.2), below the 7.5% the combination
  earned on the same measure in 2025; no cut.
- **(a) VALUE RANGE (central, all-equity): $46.84 to $49.35 a share** (EV $7,634M no growth, after maintenance only;
  EV $7,921M at 2.30%, after all spending), against **$51.49**. Width 1.05 to one. Beside: all-spending pair **$37.79 to
  $49.35**; the maintenance pair crediting growth without charging its spending, **$46.84 to $60.22**, shown and not used;
  default pair (acquisitions deducted) **-$6.67**; equity-only, at 5.6%: $45.56 (maintenance, no growth) to $43.82 (all
  spending, 2.30%). The literal window is the base used, so it is the figure shown.
- **Floor test first.** Expected return at the price, on the four cases: 4.53% (all spending, no growth), 5.44% (all
  spending, 2.30%), 5.24% (maintenance, no growth), 6.26% (maintenance, 2.30%); **no case earns the floor of about ten
  percent** **[M2003-149]**. A check outside the convention: on 2025 alone, the best year in the window, the best case
  returns 9.56% at the price, still below the floor. Had Q7 been reached, the price above the top of the range would close
  it OUT by the floor convention; the width is narrow, so the TOO HARD close **[L2000-025]** does not arise.
- **(b) FAIR PRICE (all-equity, central): $17.66 a share**: each central end valued at ten percent, $17.45 (maintenance, no
  growth; EV $4,275M) and $17.87 (all spending, 2.30%; EV $4,322M), averaged, less net debt. **Equity-only beside: $24.71**
  ($25.51 and $23.91). The equity-only figure is higher because the debt costs less after tax than the ten percent the
  equity is asked to earn, the flattery of per-share figures the all-equity basis is there to refuse **[L2017-004]**.

## RESEARCH PASS FOR THE TOO HARD (WORK) AT Q2: STEPS 1 AND 2 (written, not run; closed unrun under Part VII)
*Part VII's rule of 2026-10-12: a pass is run only where the COMPUTATION shows some case of the range earning the floor at
the price; none does (best case 6.26%), so the pass is written and closed unrun, and the name is re-looked under an alert
at the top of its computed range ($49.35) like any OUT. The dated register note is the dispatching session's to write.*

**Step 1. "What do I not know that I need to know?"** **[M1999-129]**, each marked knowable or not **[M2006-076]**:
1. *Does MP earn more than its two largest rivals over a full cycle?* Knowable: Metso and Sandvik publish segment results
   for their aggregates and crushing-and-screening businesses in their annual reports.
2. *Do MP's prices hold when its volume falls?* Knowable: Terex's MD&A for 2019 to 2020 and 2023 to 2025 states the causes
   of MP's margin changes (price, volume, cost).
3. *Is MP's share of mobile crushing and screening rising or falling?* Knowable only if a primary document states it;
   if none does, it is recorded unanswerable with the search made (form (c)) and the close is decided on 1 and 2.

**Step 2. For each knowable question: the evidence, where it is, the span, and the single fact that closes OUT** **[M1998-144]**:
1. Evidence: segment operating margin (operating profit after depreciation over sales) and operating profit over capital
   employed, for Terex MP and for Metso's aggregates segment and Sandvik's crushing-and-screening business. Source: Terex
   10-Ks FY2016 to FY2025 (segment notes); Metso and Sandvik annual reports FY2016 to FY2025 (segment notes). Span fixed:
   FY2016 to FY2025, the whole span, never one year. **OUT fact:** Metso's aggregates segment's average operating margin
   over FY2016 to FY2025 exceeds MP's average over the same years. (Margin against margin, and profit after depreciation
   against capital employed; never one set against the other.)
2. Evidence: the MD&A attribution of MP's margin change in each year in which MP's sales fell (2020, 2024, 2025). Source:
   Terex 10-Ks FY2020, FY2024, FY2025, Item 7, MP segment discussion. **OUT fact:** MP's MD&A names lower pricing (or
   price concessions, discounts) as a cause of a margin decline in any of those three years.
3. Evidence: a stated market share for MP in mobile crushing and screening in any two years of FY2016 to FY2025. Source:
   Terex 10-Ks and investor-day materials filed on 8-K; Metso and Sandvik annual reports. **OUT fact:** a primary document
   states MP's share lower at the end of the span than at its start.
**How step 4 would close:** IN only if MP's ten-year average margin is at or above both rivals' and no down year names
lower pricing, and then the run continues from Q2 (MP's castle IN; Aerials, ES and SV read as non-deciding parts, the open
ones carried to Q7 at no growth); OUT on any one OUT fact; TOO HARD (NATURE) if the pass ends unsure **[M2002-092]**, never
TOO HARD (WORK) a second time **[M2008-086]**.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early): Step 0
      and foundations, Q1, Q2, then the close, each a pathspec commit of the two paths.
- [x] If dispatched to an analyst: the brief allowed the per-question commits; the lock is the dispatching session's (not
      checked by the analyst); the run binds nothing until folded into the register (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. Two directory listings of `Test Runs/`
      (to copy the template and to check for an existing Terex file) showed other runs' file names; they are declared under
      CONTAMINATION at the top and not used. The session's start context showed commit subjects of another company's run;
      declared, not used.
- [x] Every v5 id resolves (`checkids.py` in the research folder: every M, L and R id in `principle_ledger_v5.csv`, no
      E-id, every quoted fragment beside an id found in that row); every filing fact carries its document or accession.
- [x] The order was kept; Q2 was the first STOP that failed and closed the run; nothing after it is a clearance, and the
      Q7 arithmetic is headed COMPUTATION, NOT A CLEARANCE. **Confessed:** the Q7 arithmetic was run in the research folder
      before Q2 was written (to fix the inputs while the filings were open), so the analyst knew while writing Q2 that no
      case earned the floor at the price. The knowledge bears on whether the box would change what the operator sees (it
      would not: price above every case either way), and it is the incentive operator rule 9 names; Q2 was decided on the
      castle evidence alone, and the computation does not enter its text.
- [x] Owner cash after every real cost (operating cash less stock pay less net capital spending), never a net-income proxy
      (operator rule 5); the sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found (foundations); facts for later questions are under AFTER THE
      STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor is cited (the run is dated today; not a point-in-time test).
- [x] Only the arithmetic lines of `tools/run.py` were used; its "capex alt" column was checked against the filed
      statement and found to double count, and is not used.
- [x] `python tools/check_framework.py` PASS before the closing commit (recorded in the commit of the close).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The parts threshold reads a record that no longer describes the company.** Q2's business-of-parts convention decides
on five-year operating profit, which here makes Materials Processing the deciding part (42%); but ESG was owned for fifteen
of the sixty months and REV for none, and on the half-year to 2026-06-30 ES, MP and SV each earned about a third of the
adjusted segment total. A company that has just bought or merged its way into a new mix is judged on a part that may no
longer be its largest. The text says nothing about acquisitions inside or after the window for this threshold (Q7 has rules
for both). I applied the five-year record as written and said so at Q1. (2) **The serial-acquirer convention undercounts a
large purchase made late in the window.** With purchases left out and only organic growth credited, ESG contributes fifteen
months of cash to a sixty-month average and none of its growth; the default pair, meanwhile, deducts the whole $2,001M and
goes negative. Neither pair values the business as it now stands; I showed a 2025-only check outside the convention to be
sure the close did not hang on it (it does not). (3) **"Organic growth, as the filer reports it" assumes the filer reports
it.** Terex reports a pro forma ES growth for one year and no organic figure for the window; I built one from segment
notes, holding Utilities at its 2024 level for want of a 2025 figure, and said so. (4) **Specific (e) does not say whether
growth capital spending stops after year ten**, as purchases do under (c); I charged it throughout in the growth case,
the more conservative reading. (5) **The "rivals that file with the SEC" limit, from the brief, decides the cause of the
box here:** MP's largest rivals publish full annual reports outside the SEC, so the question is knowable and the box is
WORK, while a stricter reading of "filing" might have made it NATURE. (6) **Template wording:** the Q2 template asks for
"the field's returns over the last full cycle" but Q2's text gives no rule for which rival returns count when the
best-placed rivals do not file in the filer's jurisdiction.
