# Company Run — HNI Corporation (NYSE: HNI) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The run was dispatched under a blind rule that forbids
opening `PORTFOLIO.md`, any holding review, the queue, the resume-state file and the prepped reading list, so whether the
operator holds this name is unknown to the analyst. **Contamination declared:** the session's recent commit subjects name
the boxes of other runs of the day (CTS, MOV, DBD, RES, all closed at Q2); none is this company. Project files read: `CLAUDE.md` and the operator protocol (loaded with the
session), the framework, the template, the v5 ledger and the tools; nothing about this company. The template was copied to this file
before any fetch.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $47.65 (2026-10-05; `tools/run.py` live quote; **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: common stock 72,181,800 (10-Q for the quarter ended 2026-07-04,
  filed 2026-08-04, accession `0000048287-26-000125`; `python Screens/cover_shares.py HNI`). One class only. The count is
  up from roughly 46 million before 2025-12-10 because HNI issued shares to Steelcase holders when it acquired Steelcase
  by merger on that date (10-K FY2025, accession `0000048287-26-000084`, Item 1: "acquired by merger Steelcase Inc. [...]
  for total consideration of cash and HNI common stock valued at $1.9 billion").
- **Market cap:** about $3,439M (72.18M x $47.65).
- **Sovereign for the earnings currency (USD):** 5.63%, US Treasury daily par yield curve, 30-year, 2026-10-02
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4), text copies in `Test Runs/_research 2026-10-05 HNI/`:
  - 10-K FY2025 (year ended 2026-01-03), filed 2026-03-03, accession `0000048287-26-000084`: Item 1, Item 1A, Item 7 in
    full, balance sheet, Note 4 (Steelcase and Kimball International).
  - 10-Q for the quarter ended 2026-07-04, filed 2026-08-04, accession `0000048287-26-000125`: MD&A and segments.
  - 10-Ks FY2016 to FY2024 (accessions `0000048287-17-000067`, `-18-000059`, `-19-000045`, `-20-000045`,
    `-21-000038`, `-22-000071`, `-23-000053`, `-24-000080`, `-25-000084`): segment tables and segment discussion only.
  - Proxy DEF 14A filed 2026-03-25, accession `0001140361-26-011104`: fetched, not read, because the file closed at Q2
    before Q5 and Q6 (see the self-audit).
  - 8-Ks: 2025-08-04 deal announcement and its press release exhibit 99.1 (`0000950103-25-009762`); 2025-12-10 closing
    (`0000950103-25-015967`); 2026-01-08 restructuring and impairment (`0001140361-26-000697`); 2026-06-10 term-loan
    refinancing (`0000950103-26-008782`); 2026-07-30 second-quarter release cover (`0000048287-26-000122`, exhibit not
    read); 2026-08-20 buyback authorisation (`0001140361-26-033891`).
  - Competitors, their own filings: Steelcase 10-K FY2025 (`0001050825-25-000069`); MillerKnoll 10-K FY2026
    (`0000066382-26-000092`); Kimball International 10-K FY2022, its last before HNI bought it (`0000055772-22-000102`);
    plus each company's XBRL company facts (first-filed 10-K values) for the ten-year rows.
- **One figure cross-checked against the filed statement:** total assets at 2026-01-03, $4,885.0M on the filed balance
  sheet of the FY2025 10-K, equal to the `tools/run.py` table's 4,885; long-term debt $1,276.9M on the filed sheet, equal
  to the table's 1,277; operating cash flow $276.3M in the MD&A, equal to the table's 276.
- `python tools/run.py HNI` arithmetic lines only (saved to `Test Runs/_research 2026-10-05 HNI/run_py.txt`); its labels,
  windows and "OE lo / OE hi" columns are not used. Its stock-pay column printed 16, 17 and 25 for 2023 to 2025, which
  match the filed cash-flow line (XBRL `ShareBasedCompensation` 16.5, 17.4, 24.7), so that known defect did not bite here;
  its share count (72.2M) is the post-merger cover count and is current.

### The balance sheets, ten year-ends, read before the income account (template, Q4 line; read here because the file closes before Q4) **[M2025-032]**
From the `tools/run.py` table (first-filed XBRL), with the FY2024 and FY2025 columns checked against the filed balance
sheet of `0000048287-26-000084` (USD millions):

| year-end | assets | equity | cash | receivables | inventory | goodwill | LT debt | retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2016-12-31 | 1,330 | 501 | 36 | 229 | 118 | 291 | 180 | 462 |
| 2017-12-30 | 1,392 | 514 | 23 | 259 | 156 | 280 | 240 | 467 |
| 2018-12-29 | 1,402 | 563 | 77 | 255 | 157 | 271 | 249 | 505 |
| 2019-12-28 | 1,453 | 584 | 52 | 275 | 163 | 271 | 174 | 530 |
| 2021-01-02 | 1,418 | 590 | 116 | 208 | 138 | 292 | 175 | 518 |
| 2022-01-01 | 1,498 | 590 | 52 | 240 | 182 | 297 | 175 | 515 |
| 2022-12-31 | 1,414 | 616 | 17 | 218 | 180 | 306 | 189 | 534 |
| 2023-12-30 | 1,929 | 761 | 29 | 247 | 197 | 441 | 428 | 524 |
| 2024-12-28 | 1,875 | 840 | 20 | 248 | 194 | 442 | 294 | 600 |
| 2026-01-03 | 4,885 | 1,836 | 209 | 571 | 475 | 958 | 1,277 | 590 |

What the figures say. (1) **Retained earnings did not grow in a decade**: $462M at the end of 2016, $590M at the start of
2026, while the company reported net income every year; the earnings went out as dividends and buybacks, and the
equity that did grow came from shares issued for two acquisitions (Kimball International, 2023; Steelcase, 2025), not
from earnings kept. (2) **Goodwill and intangibles now nearly equal the equity**: "Goodwill and Other Intangible Assets,
net" $1,702.6M against equity of $1,835.6M at 2026-01-03, so tangible equity is about $133M; in 2016 goodwill alone was
$291M against equity of $501M. The intangibles are what the buyer paid for, and Steelcase's were recorded on "a
benchmarking analysis of publicly disclosed purchase price allocations of comparable companies" (Note 4), so they are
not yet a measured figure. (3) **Debt stayed between about $175M and $250M for seven year-ends, then reached $428M (2023) and $1,277M** (and $1,357M at
2026-07-04, 10-Q), all senior secured term loans and revolver drawn for the Steelcase cash leg. (4) **Working capital is
lean and did not bloat**: receivables were about 10% of sales in 2016 ($229M on $2,204M) and in 2024 ($248M on
$2,526M); inventory rose from about 5% to about 8% of sales; nothing in these lines builds out of proportion to sales.
(5) **Cash was never a reserve**: $17M to $116M across the decade. What the figures cannot say: whether the combined
business will earn on $1.9B of purchase price what the two earned apart, since only 24 days of Steelcase sit in the
FY2025 statements.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what the combined HON, Allsteel, Kimball, Steelcase and Hearth & Home will produce
in cash, not what the next buyer will pay, "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**. The market serves and does not instruct: the price of $47.65 says nothing about value **[M2006-077]**. No
macro view enters: the office-occupancy and housing cycles are read only as properties of the business, never as a
forecast to trade on, since "macro conclusions are — just never enter into the discussion" **[M2000-094]**. Who is paid to
tell you: management's case for the merger is built on "pro forma Adjusted EBITDA of approximately $745 million" that is
"inclusive of annual run-rate synergies" (deal release, exhibit 99.1 of `0000950103-25-009762`), the buyer's and seller's
own projection; the habits ask instead for "what’s wrong in things" **[M2025-013]** and for the other side's case stated
better than its holder states it **[M2016-055]**.

**Contrary evidence, written down as found** **[M1997-127]**:
- Found against: the filer's own words, "The workplace furnishings industry is characterized by intense competition,
  with a significant number of competitors offering similar products" and "The Corporation faces significant price
  competition from its competitors and may encounter competition from new market entrants" (10-K FY2025, Item 1).
- Found against: "Price competition impacts the Corporation’s ability to implement price increases or, in some cases,
  maintain prices, which could lower profit margins" and price competition "from new market entrants who may manufacture
  and source products from lower cost countries" (10-K FY2025, Item 1A).
- Found against: legacy HNI office-furniture sales of $1,778M in 2015 (FY2017 10-K) against roughly $1,300M in 2024 once
  Kimball International's roughly $589M is taken out (FY2023 and FY2024 10-Ks; computed; divestitures of Lamex, Poppin
  and smaller units account for part of the fall, not all of it).
- Found against: the workplace segment earned (0.4)%, (0.0)% and 0.2% of sales in 2020, 2021 and 2022 (FY2021 and FY2022
  10-Ks).
- Found against: "adoption of hybrid working models has resulted in a significant decrease in worker attendance at their
  office locations. Despite office re-entry in many markets, office occupancy levels remain below historic levels."
  (10-K FY2025, Item 1A).
- Found against: the deal was sold on EBITDA with synergies added back, and the stated leverage "Includes EBITDA
  add-backs, which encompass two-year look-forward run-rate synergies" (deal release).
- Found FOR: the hearth segment earned 14.0% to 18.9% of sales in every year 2016 to 2025 and Hearth & Home is "North
  America’s largest manufacturer and marketer of prefabricated fireplaces, hearth stoves, and related products" (10-K
  FY2025, Item 1).
- Found FOR: legacy HNI turned its tangible capital fast (sales about 4 to 5 times tangible capital employed in 2024,
  computed from the filed balance sheet), so a thin margin still produced a high pre-tax return on that capital; "a one
  percent pre-tax margin only works in terms of return on capital if you turn your equity extraordinarily fast"
  **[M2017-096]**.
- Found FOR: the workplace segment's 2024 and 2025 margins (9.0% and 8.5%) were its best of the decade, credited by the
  filer to Kimball International synergies and a Mexico plant (10-Ks FY2024 and FY2025, segment discussion).

## THE STANDING RULE
Owning HNI shares bought for cash, unlevered, at a size the owner can see halved, does not put the buyer at risk of
ruin; the target's own $1.36B of secured debt is the target's exposure and belongs to Q9, not here. "We are never going
to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**; "Never risk permanent loss of
capital." **[L2023-005]**. No purchase is proposed, so no financing or sizing is at issue.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, "a reasonable probability of being able to asses where the business will
  be in 10 years" **[M2000-037]**.
- **The key variables, and whether they are foreseeable** **[M1998-044]**. Office furniture: service-sector employment,
  office occupancy and vacancy, corporate profits and moves (the filer's own list, Item 1A); the price-cost spread on
  steel, aluminium, wood, foam and freight; dealer coverage. Hearth: new single-family construction and remodel activity
  (Item 1 and segment discussion). None is technology; the product changes slowly; the selling system (independent and
  owned dealers, architects and designers for contract work, distributors for small business) is described the same way
  in the 2016 and 2025 filings. The dynamics can be read even where the year's demand cannot: "What is important is that
  I understand the economic dynamics of the industry. Is there — are there competitive moats? Is there ease of entry?"
  **[M2011-014]**.
- **How far off could I be** **[M2011-084]**. Ten years of filings from four office-furniture makers bound the earning
  power: consolidated operating margins of HNI 3.1% to 8.2% (2016 to 2025), Steelcase 0.7% to 6.9% (FY2016 to FY2025),
  MillerKnoll -1.5% to 9.4% (FY2017 to FY2026), Kimball International -2.1% to 8.5% (FY2015 to FY2022); hearth 14% to
  19%. The level of office demand ten years out cannot be foreseen to a point, but the range of what the industry earns
  on whatever demand comes is written in ten years of statements; asked whether "the financial statements will tell me
  the information that’s useful to me in making a judgment about what the future financial statements are going to look
  like" **[M2008-033]**, the answer here is yes.
- **Would the insiders write it down?** **[M2000-105]**. They do: HNI's board committed $1.9B and $1.36B of secured debt
  to a long view of this industry, and the competitors' 10-Ks describe their markets in near-identical words. This is not
  a field whose insiders would call the ten-year forecast too hard.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. The
  doubt found is the level of office demand after hybrid work, a variable inside an understood business, not doubt about
  how the business makes or loses money. Recorded; not decisive.
- **Routing.** Not a business whose ten-year economics are out of reach because its industry changes fast; not a
  financial institution; not a holding company (two operating segments, the hearth segment about 11% of first-half 2026
  sales: $310.8M of $2,819.9M, 10-Q `0000048287-26-000125`).
- **VERDICT: IN.** The economics of a dealer-sold maker of office furniture and fireplaces can be foreseen within a range
  the decade's filings draw **[M2012-065]**, **[M2011-014]**; what that foresight shows is Q2's question.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. A moat is what "protects
excellent returns on invested capital" **[L2007-004]**. The whole is bought at one price; office furniture is about 89%
of first-half 2026 sales ($2,509.2M of $2,819.9M, 10-Q `0000048287-26-000125`) and, on 2025 segment figures with
Steelcase's last full year added, roughly three quarters of segment operating income (computed). The castle that decides
is the office-furniture castle; the hearth castle is read below it.

**The competitor row** (same metric, operating income over net sales, each from its own filings; ten fiscal years where
the filings run that long):

| company | span | low | high | average | source |
|---|---|---|---|---|---|
| HNI, consolidated | 2016 to 2025 | 3.1% | 8.2% | 5.2% | XBRL first-filed 10-K values; 10-K FY2025 `0000048287-26-000084` |
| HNI, workplace segment (before corporate cost) | 2016 to 2025 | (0.4)% | 9.0% | 4.2% | segment tables, 10-Ks FY2017 to FY2025 (accessions in Step 0) |
| HNI, hearth segment (before corporate cost) | 2016 to 2025 | 14.0% | 18.9% | 17.2% | same |
| Steelcase | FY2016 to FY2025 | 0.7% | 6.9% | 4.3% | XBRL; 10-K FY2025 `0001050825-25-000069` |
| MillerKnoll | FY2017 to FY2026 | (1.5)% | 9.4% | 4.7% | XBRL; 10-K FY2026 `0000066382-26-000092` |
| Kimball International | FY2015 to FY2022 | (2.1)% | 8.5% | 4.5% | XBRL; 10-K FY2022 `0000055772-22-000102` |

Sales over the same spans (nominal): Steelcase $3,060M (FY2016) to $3,166M (FY2025), with acquisitions inside it, a real
decline; legacy HNI office furniture $1,778M (2015) to roughly $1,300M (2024, Kimball International removed, computed);
Kimball International $768M (FY2019) to $666M (FY2022). Four makers, four decade averages between 4% and 5%, every one
of them near or below zero in the same years (2020 to 2022, except MillerKnoll's FY2021). No office-furniture company in
the row shows a protected return; the one high, stable line is the hearth segment.

**The castle tests, each with its filing fact.**
1. **The attacker with money** **[M2011-015]**, **[M2012-106]**. The filer expects him: it "may encounter competition from
   new market entrants" (Item 1), including entrants "who may manufacture and source products from lower cost
   countries" (Item 1A); the same filing names "global importers" among its competitors (Item 1). The answer to whether
   someone with money could take it on is yes, and the filing says others are trying. "If the answer had been yes, we
   wouldn’t have done it." **[M2011-015]**.
2. **Pricing power, and the agony before a rise** **[M2005-020]**. "Price competition impacts the Corporation’s ability to
   implement price increases or, in some cases, maintain prices" (Item 1A); the 2025 workplace margin fell on
   "unfavorable price-cost" (segment discussion); the price realisation reported for 2021 to 2023 followed a cost
   inflation that every competitor passed on at the same time. The prayer session is in the filer's own sentence.
3. **Unit volume and share of mind** **[M1999-054]**. Legacy volume falls in the filer's own words, year after year:
   "lower volume across most customer segments in the legacy HNI workplace businesses" (2023), "lower demand across most
   customer channels" (2024), "lower net sales in the legacy HNI business" (first half 2026). Legacy office-furniture
   sales fell from $1,778M to roughly $1,300M in nine years, nominal. Hybrid work "has resulted in a significant decrease
   in worker attendance at their office locations" (Item 1A). The brand list is long (HON, Allsteel, Gunlocke, Kimball,
   Steelcase and more), but no filing read shows a customer asking for one by name at a higher price; the contract sale
   "generally attracts several manufacturers competing for the same projects" (Item 1).
4. **The low-cost position** **[L2004-007]**, **[M1997-010]**. The filer claims lean manufacturing and "value products
   designed to be among the best in their price range for product quality and performance" (Item 1), and the 2024 and
   2025 workplace margins were the decade's best. The test the rows set is the hard market: "Long term, a tough market
   helps the low-cost operator" **[L1997-021]**. In the tough market of 2020 to 2022 HNI's workplace segment earned
   (0.4)%, (0.0)% and 0.2%, while MillerKnoll earned 9.4% (FY2021, consolidated) and Kimball International 7.5% (FY2020).
   The low-cost operator does not earn nothing for three years while a rival earns nine percent. No evidence was found
   that HNI holds the "cherished title" **[L2004-007]**; the evidence found is that it does not.
5. **Would the customer still choose it over the low bid** **[M2017-009]**. The small-business channel is "driven on the
   basis of price, product quality, selection, and the speed and reliability of delivery"; the contract channel
   "generally attracts several manufacturers competing for the same projects" (Item 1). That is a customer who takes
   bids. A customer who would pass over the low bid for HNI's product is not found in any filing read.
6. **Ask the competitors** **[M1999-130]**. Steelcase: "The Americas office furniture industry is highly competitive, with
   a number of competitors offering similar categories of products" (10-K FY2025). MillerKnoll: "All aspects of the
   Company's business are highly competitive. The Company competes largely on design, product and service quality, speed
   of delivery and product pricing" (10-K FY2026). Kimball International: "There are numerous furniture manufacturers
   competing within the marketplace, with a significant number of competitors offering similar products" (10-K FY2022).
   Each names HNI among its rivals; none names a barrier.
7. **Widening or narrowing** **[M1999-108]**, **[M2000-075]**. Narrowing. The industry shrank in real terms and
   consolidated: HNI bought Kimball International (2023) and Steelcase (2025); MillerKnoll was formed by Herman Miller's
   purchase of Knoll (FY2022). Consolidation in a shrinking market answers a filling moat; it does not prove a wide one:
   "you can have only two competitors and they’re still terrible businesses, they beat each other’s brains out"
   **[M2013-052]**.
8. **What could destroy, modify or reduce it** **[M2000-014]**. Fewer people in fewer offices, importers from lower-cost
   countries, and the price competition the filer names (all Item 1A). Each is already visible in the record, not a
   remote threat.

**The commodity mark and its exception.** The rows' marks of a commodity business are present in the filer's and the
competitors' own words: similar products from many suppliers, a customer who buys on price, improvements every rival
copies (lean plants and Mexico moves are in all four companies' filings), and few large rivals that "beat each other’s
brains out" **[M2013-052]**, **[M2004-053]**. The way through a commodity field the rows name is the low-cost operator
**[L2004-007]**, **[L2000-017]**, and test 4 found the evidence against HNI holding it. "We’re going to be investors in
businesses, not commodities, by and large." **[M2007-131]**.

**The hearth castle, read below it.** Hearth & Home shows castle signs the office business lacks: margins of 14.0% to
18.9% in every year 2016 to 2025, holding 16.8% through a 20.8% sales fall in 2023; North America's largest maker; brand
leaders by the filer's account (Heat & Glo, Heatilator, Majestic, Quadra-Fire); its own installing distribution
(Fireside Hearth & Home). The filer still writes that "In both the workplace furnishings and residential building
products industries, the Corporation faces price competition" (Item 1A), and the part is about 11% of sales. A good small
castle beside a larger open one does not close the open one; the whole is bought at one price and the larger part
decides. (The framework has no by-parts rule at Q2; see the last section.)

**The contrary case, stated as its holder would state it** **[M2016-055]**. HNI's case: scale after Steelcase (by its own
account the market leader), $120M of run-rate cost synergies, a Mexico plant, the best workplace margins of its decade in
2024 and 2025, and a fast-turning, lean balance sheet that earned high pre-tax returns on tangible capital. Weighed: the
2024 and 2025 margins rest on cost actions any rival can copy and sit in the same filings as "unfavorable price-cost" and
falling legacy volume; scale gave none of the four a protected margin in the decade's record, since the largest
(Steelcase) averaged 4.3%; and a high return on tangible capital in a business that pays out its earnings and grows by
buying rivals at goodwill is a fact about turnover, Q3's subject, not evidence of a barrier.

**Why a STOP, and which box.** The castle is shown open on the evidence, not merely unjudgeable: the filer says it cannot
always "maintain prices"; legacy volume fell for a decade; every competitor earns the same thin, cycle-exposed margin; and
the one test that would rescue a commodity business, the low-cost title, is failed by the record of 2020 to 2022. A
castle that a well-funded attacker could take is the case where "we wouldn’t have done it" **[M2011-015]**, and price does
not reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**; "If you
really think a business is declining, most of the time you should avoid it." **[M2012-062]**. It is not TOO HARD: the
deciding question (is there a barrier?) is answered by the filings, and the answer is no; the tenuous-moat route to TOO
HARD **[M2000-019]** is for a moat whose future cannot be judged, and this one's present can be read.

- **VERDICT: OUT** at Q2 **[M1995-038]**, **[L2007-004]**, **[M2011-015]**, **[L2004-007]**, **[L1997-021]**,
  **[M2013-052]**, **[M2019-015]**. The file closes here.

---
## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (closed at Q2).

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED as a question (the balance-sheet reading was done in Step 0).
One tell written down as found, not weighed: the deal was argued in "pro forma Adjusted EBITDA of approximately $745
million" that is "inclusive of annual run-rate synergies" (deal release), the kind of figure Q4 reads against.

## Q5 — WHO RUNS IT. NOT REACHED. The proxy was fetched and not read.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
Facts found on the way, recorded and not weighed: the Steelcase deal was paid with $864.5M of cash and 25.2M HNI shares
valued at $1,012.5M, plus $45.4M of replacement awards (Note 4), so it is not the wholly-stock deal of Q6's one STOP;
buybacks are stated as "focused on offsetting the dilutive impact of issuances of common stock pursuant to equity awards"
(10-K FY2025, MD&A) with no price named, and $200M was added to the authorisation on 2026-08-17 (8-K
`0001140361-26-033891`). The stated synergy target is "$120 million when fully mature" (deal release).

## Q7, Q8, Q9, Q10, Q12 — NOT REACHED.

---
## COMPUTATION — NOT A CLEARANCE
*Written after the file closed OUT at Q2, at the owner's request for reporting (not a rule change). It carries no entry
language and clears nothing (operator rule 3). Script and output: `Test Runs/_research 2026-10-05 HNI/compute.py`,
`compute_out.txt`.*

**Owner cash after every real cost** (operating cash flow, less all capital spending including capitalised software,
less stock pay; never a net-income proxy, operator rule 5; USD millions, first-filed 10-K values):

| HNI, calendar year | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| owner cash | 95.7 | (2.1) | 115.4 | 145.7 | 164.9 | 52.2 | 3.8 | 171.9 | 156.4 | 183.8 |

| Steelcase, fiscal year ended late February | FY2016 | FY2017 | FY2018 | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| owner cash | 72.0 | 89.8 | 120.0 | 32.1 | 270.7 | 2.6 | (179.2) | 8.5 | 235.6 | 76.9 |

- Five-year averages: HNI 2021 to 2025 $113.6M (2016 to 2020: $103.9M); Steelcase FY2021 to FY2025 $28.9M (FY2016 to
  FY2020: $116.9M). Combined $142.5M against $220.8M five years earlier.
- Less the added after-tax interest of the merger debt, a **disclosed guess of $38M**: first-half 2026 net interest of
  $44.4M (10-Q) annualised to about $89M, against about $38M of net interest the two paid apart (HNI $27.2M in 2024,
  10-K; Steelcase $25.7M gross in FY2025 less interest earned on its cash, XBRL), taxed at about 25%. **Base: $104.5M a
  year**, $1.45 a share on 72.18M shares; at $47.65 an owner-cash yield of 3.0%.
- Depreciation variant (operating cash less depreciation and amortisation less stock pay), shown beside it as the
  convention asks: about $42M a year combined after the same interest guess; lower because both companies' D&A exceeds
  their capital spending, much of it amortisation of acquired intangibles that the rows say is not always a real cost
  **[L2012-003]**. Maintenance judgment: the filer describes capital spending as "primarily applied to machinery,
  equipment, and tooling required to support continuing operations" (10-K FY2025, MD&A), so most of it is maintenance;
  2026 capital spending is guided to "$140 million to $150 million" (same MD&A) against the two companies' combined recent level of
  about $115M to $120M.
- **Growth shown** (aggregate owner cash, not per share, per the convention's specifics): the combined five-year average
  fell from $220.8M to $142.5M, about **-8.4% a year**.

**(a) VALUE RANGE** (Q7 CONVENTION: five-year average, carried ten years at the growth shown and never above it, then no
growth, at the 5.63% sovereign; ends are the no-growth and shown-growth cases):
**$13.37 to $25.71 a share against $47.65.** Ratio of the ends 1.9 to 1, inside the three-to-one width. The price is
above the top of the range, so had the file reached Q7 it would close OUT through the floor convention (the expected
return at the price is below the minimum). Because the shown growth is negative, the no-growth case is the top of the
range, not the bottom; the convention's two ends were written for positive growth.

**(b) FAIR PRICE: about $20.70.** Rule: the price at which the central case clears the floor. Central case = the
no-growth case ($104.5M a year, flat), which is kinder than the record because the record shows decline. The floor of
"at least 10% pre-tax returns" is applied after corporate tax, as the row itself translates it, "(which translate to
6�-7% after corporate tax)" **[L2002-020]** (the damaged character is the row's own): **7% after corporate tax** on owner
cash, which is already after the company's tax. $104.5M / 0.07 / 72.18M = $20.68. Read strictly (10% applied to owner
cash), the fair price is $14.48.

**(c) CHEAP PRICE: about $11.20.** Rule: the price at or below which even the bottom case, owner cash shrinking at the
shown -8.4% for ten years then flat, still clears the 7% after-tax floor; at that price no pencil is needed because the
pessimistic case alone clears it **[M2009-005]**. Shown-growth stream discounted at 7%: $11.17.

**Sensitivities, written down because they are the case for the price** (not the range): (i) with the full $120M of
run-rate synergies counted after tax (about $90M) and no growth, the value at the 5.63% sovereign is $47.86, almost
exactly the price, and at the 7% floor $38.49; the price therefore assumes the synergies arrive in full and nothing
shrinks, and "we never count on synergies" **[L2016-008]**. (ii) On the company's own unaudited pro forma 2025 net
income of $176.1M (10-K FY2025, Note 4), held flat: $43.33 at the sovereign, $34.85 at the 7% floor. Every case found
sits below $47.65 except the one that counts every synergy and discounts at the bond rate with no margin.

---
## THE BOX
**OUT at Q2** (the castle shown open on the evidence: similar products under price competition the filer names, legacy
volume down for a decade, four makers averaging 4% to 5% margins, and no low-cost title in the hard market of 2020 to
2022). COMPUTATION, not a clearance: value range $13.37 to $25.71 a share, fair price about $20.70, cheap price about
$11.20, against $47.65.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question (Step 0 and the balance sheets, then the
      foundations, the standing rule and Q1, then Q2, each appended before the next was drafted). [ ] Committed after
      each: **not done**, by the dispatch instruction ("Do not commit"); the write-early rule was kept, the commit half
      was not.
- [x] Every v5 id resolves (Python check against `principle_ledger_v5.csv`, below); every filing fact carries its
      accession or names its filing; computed figures are marked computed. No v4 id is cited.
- [x] The order was kept; Q1 IN, Q2 OUT closed the file; nothing after it is a clearance; the valuation is headed
      COMPUTATION — NOT A CLEARANCE.
- [x] Owner cash after every real cost (capital spending and stock pay deducted), never a net-income proxy; the net
      income figure appears only as a labelled sensitivity. Sovereign from the US Treasury, dated. The price is an
      aggregator quote, flagged.
- [x] Contrary evidence written down as it was found **[M1997-127]**, in both directions.
- [x] No row dated after the anchor: not a point-in-time run; the anchor is today.
- [x] Only the arithmetic lines of `tools/run.py` were used; its windows and OE labels were not.
- [x] `python tools/check_framework.py` run before finishing (result recorded in the session report; no commit made).
- Not done, owed if the name is ever reopened: the proxy (Q5, Q6 Part B) and the second-quarter release exhibit were not
  read; Steelcase's 10-Qs for its last partial fiscal year (March to December 2025) were not read, so its owner cash ends
  at FY2025; the acquired intangibles are preliminary.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q2 has no by-parts rule.** Q1 reads a holding company *by its parts* (CONVENTION), but nothing tells a Q2 run what
to do when one segment shows a castle (hearth: 14% to 19% margins every year for a decade, market leader) and the larger
one does not. I read the castle of the part that dominates sales and profit and recorded the hearth castle below it; a
run that valued the hearth part alone would reach a different, partial answer, and the text does not say which is meant.
(2) **The Q7 range convention assumes positive growth.** With aggregate owner cash shrinking (-8.4% a year between the two
five-year windows), the *no-growth* end becomes the top and the *shown-growth* end the bottom; the convention's words
(*never above it*, *capped by Q3*) still work, but the text does not say so, and a run could read *no growth* as the
floor case. (3) **A merger inside the five-year window.** The convention's five-year average presumes one business; for
a company that has just absorbed a rival larger than itself, there is no stated rule for building the combined base
(I summed both companies' own five-year averages and deducted a disclosed guess for the added interest). (4) **The
floor's tax basis.** The floor CONVENTION names about ten percent pre-tax without saying whether owner cash (already
after corporate tax) is set against 10% or against the row's own after-tax translation of 6½ to 7%; the fair price
moves from $14.48 to $20.68 on that reading alone. I used 7% after corporate tax, from **[L2002-020]**, and showed both.
(5) **The template's position note** tells the analyst to check `PORTFOLIO.md`, which this dispatch's blind rule forbids;
the two instructions conflict, and the blind rule was followed.
