# Company Run — Steel Dynamics, Inc. (NASDAQ: STLD) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled at the fold by the dispatching session (overnight 2026-10-13, after the run was committed): not held (`PORTFOLIO.md` carries no line for STLD or Steel Dynamics).

**Dispatched run.** Done by a dispatched analyst under the canonical brief `Screens/_daily/_dispatch_brief.md`, with the
one departure the brief states (the lines of evidence and the competitors derived by the analyst from the filing).
Research folder: `Test Runs/_research 2026-10-13 STLD/` (notes, scripts, the `tools/run.py` output and the comparison
output are tracked; the raw filings sit in its ignored `cache/`).

**Contamination, declared and not used.** (1) The session context supplied at start showed the repository's recent commit
subjects, among them a run of another company (CLF) whose Q2 subject line names a pre-tax margin comparison that includes
STLD among four steelmakers, and its fold line. I did not open that run file, its research folder, the register or any
other blind-listed file. The comparison in this run's Q2 was computed from the four companies' own XBRL filings by a script
in this run's folder (`scripts/compare.py`, output `comparison_output.txt`); nothing in it is taken from the other run.
I cannot unsee that another analyst has drawn a comparison on the same names, and I declare it here as a possible anchor.
(2) The same context listed file names of other companies' research folders (git status); file names only, not opened.
(3) The memory index line on the queue names no STLD fact. Nothing else seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $240.63 (2026-10-13, live quote through `tools/run.py`; **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: 143,328,088 common shares, one class, voting, $0.0025 par, as of
  2026-07-23 (Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-28, accession `0001104659-26-087414`;
  `python Screens/cover_shares.py STLD`). Check: the 10-Q balance sheet shows 268,694,947 issued less 125,084,889 treasury
  = 143,610,058 outstanding at 2026-06-30, consistent with the cover count after further purchases. After the cover date
  the company states it "has repurchased $261 million, or just under one percent, of its common stock so far during the
  third quarter of 2026" (8-K of 2026-09-18, Exhibit 99.1, accession `0001104659-26-108777`); no share issue, split or
  merger in any 8-K filed since 2025-06 (8-K list read from the EDGAR submissions index). The cover count is used; the
  later purchases would lower it by about one percent, and that is said, not adjusted.
- **Market cap:** $34,489M (143.328M × $240.63).
- **Sovereign for the earnings currency (USD):** 5.60%, US Treasury daily par yield curve, 30-year, 2026-10-09, the latest
  published (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): Form 10-K for FY2025, filed 2026-02-27, accession `0001104659-26-021395` (Items 1, 1A,
  3, 5, 7, 7A, 8 notes on business combinations, debt, inventories, PP&E, segments); Form 10-Q for Q2 2026, filed
  2026-07-28, accession `0001104659-26-087414` (statements, liquidity, repurchases); DEF 14A filed 2026-03-27, accession
  `0001104659-26-035826` (pay, peers, board); 8-Ks: `0001104659-25-114956` (notes offering, 2025-11-21),
  `0001104659-25-117578` (NPS closing, 2025-12-02, with Ex. 99.1), `0001104659-25-124210` (2026 notes redeemed),
  `0001104659-26-085277` (Q2 2026 results, Ex. 99.1), `0001104659-26-090129` (CEO succession, 2026-08-04),
  `0001104659-26-098390` (8-K/A, transition awards), `0001104659-26-096861` (dividend), `0001104659-26-108777` (Q3 2026
  guidance), and the guidance and results releases of 2025-06 to 2026-04 listed at Q4. Earlier 10-Ks for the segment
  history: FY2023 `0001558370-24-002152`, FY2021 `0001558370-22-002377`, FY2019 `0001558370-20-001641`.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $1,449,534
  thousand in the filed Consolidated Statement of Cash Flows (10-K FY2025) against 1,450 ($M) in `tools/run.py`'s tagged
  series; also depreciation and amortization $551,390 thousand (551) and purchases of property, plant and equipment
  $948,025 thousand (948). They agree.
- `python tools/run.py STLD`, arithmetic lines only (`_research 2026-10-13 STLD/run_py_output.txt`): owner cash after
  stock pay and all capital spending (OCF less SBC less capex) by year 2023 1,800, 2024 -90, 2025 433 ($M); the five-year
  window 2021-2025 averages 1,349 on all capex and 2,186 on depreciation; capex 2023-2025 1,658 / 1,868 / 948 against D&A
  438 / 479 / 551; SBC 62 / 67 / 69, tagged, complete; no securities, mine, software or intangible spending found beside
  capex. The tool's yield, "growth the price assumes" and points-over-sovereign lines are not used (Part VII, the tooling).

**Lines of evidence chosen, and why** (the brief's departure: derived from the 10-K's Items 1, 1A and 7). Item 1 calls the
company a producer whose "primary competitive influences on products we sell are price, quality, and value-added
services" and says "Some of our products are commodities"; Item 7 says steel results are "driven primarily from the metal
spread", and Item 1A puts imports, scrap prices, the cycle and new capacity first. So the lines are: (1) segment operating
income over two cycles (FY2018 to FY2025 from four 10-Ks), to find the deciding part; (2) the cost position against the
rivals, from their own filings, over 2016 to 2025, which is how a commodity business is judged at Q2; (3) capital spending
against depreciation and what the added capital earned, since the company built two large mills (Sinton, aluminum) inside
the window; (4) acquisitions (New Process Steel in two steps) and their goodwill; (5) debt, maturities and leases;
(6) buybacks and the prices paid; (7) stock pay and the incentive structure; (8) quarterly earnings guidance and the
adjusted figure in the releases (found in the 8-Ks); (9) litigation and environmental proceedings (Item 3); (10) the CEO
succession of 2026-08-04.

## THE FOUNDATIONS (not a gate)
The share is read as a business **[M1997-109]**: this is a steel, scrap, joist and aluminum business whose price the market
quotes; the quote "just tells us prices" **[M2006-077]**. No macro conclusion enters **[M2000-094]**: tariffs, imports, rates
and the steel price are not forecast here; what counts is "the average profitability of the business over time and how
strong its competitive mode is" **[M2015-016]**. Margin of safety is the attitude for Q7 **[M1996-084]**. The analyst's
habits apply with force, since a business that looks this good at the top of a cycle invites anchoring: "destroy our
previous ideas" **[M2016-054]**, and look for "what’s wrong in things" **[M2025-013]**. **Contrary evidence, written down
as found** **[M1997-127]**: (a) the speakers themselves once said of a carbon steel company "we can’t evaluate a carbon
steel company, we don’t buy it" **[M2000-038]**, weighed at Q1, never a verdict alone (Q2, A row about one company);
(b) the 10-K says new domestic capacity and more EAF mills could raise scrap prices and press steel prices; (c) the company
gives quarterly earnings guidance a few weeks before each quarter ends and has met or beaten it in each of the five
quarters checked (Q4); (d) the founder-CEO steps down as CEO on 2027-01-01 (8-K `0001104659-26-090129`); (e) FY2009 to
FY2015 earned about two percent pre-tax on sales (Q2).

## THE STANDING RULE
A cash purchase of a small part-interest, held without borrowed money, puts the buyer at no risk of ruin: "borrowed money
has no place in the investor's tool kit" **[L2014-005]**; "We are never going to risk what we have and need for what we
don’t have and don’t need" **[M2012-081]**. No conduct of the buyer here plants that seed; the target's own debt is Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as written:** "a reasonable fix on about what the earning power and competitive position will look like in
  five or 10 years" **[M2012-065]**; "trying to identify the key variables in that particular business, and evaluating
  how predictable they were first" **[M1998-044]**.
- **The key variables, from the filing.** (1) The metal spread, "the difference between average steel mill selling
  prices and the cost of ferrous scrap consumed in our steel mills" (10-K FY2025, Item 7), times (2) tons shipped, less
  (3) conversion cost, against (4) the capital in the mills. Metallic raw materials are "approximately 55% to 65% of our
  steel mill operations’ manufacturing costs" (Item 7). The spread itself is a commodity price relation and is not
  foreseeable; the rows do not ask it to be: "We don’t think we can predict commodity prices." **[M2016-025]**. What must
  be foreseeable is the cost position and the business's place in the field, measured "more by cost of production than we
  would by whether copper was selling for $2.00 a pound or a dollar a pound" **[M2006-004]**. That is readable from the
  company's and its rivals' filings (Q2), and the spread's swing enters Q7 as the cycle base and the width of the range
  (the framework's commodity-business paragraph, Q2).
- **The economics, not the chemistry.** EAF steelmaking from scrap, scrap processing, joist and deck fabrication, and a new
  recycled-aluminum rolling mill are processes whose economics are plain in the figures: what matters is "the economic
  dynamics of the industry. [...] Is there ease of entry?" **[M2011-014]** (ease of entry is Q2's). The figures do tell the future
  figures in kind **[M2008-033]**: tons, spreads, conversion cost, capital per ton; the same 10-K line items run back
  through every 10-K read (FY2019 to FY2025).
- **The parts.** By Q2's threshold the steel operations segment decides (about two thirds of five-year segment operating
  profit, Q2 parts table). It is understood by the tests above. The aluminum segment is a start-up that lost money in every
  year of the window and does not decide; its ten-year economics are less sure (first commercial shipments in the second
  half of 2025, 10-K Item 1), which is weighed at Q2 and Q7, not here: a part that does not matter does not keep the whole
  outside the circle (Q1, A holding company, with Q2's threshold).
- **Change.** EAF steelmaking is the established technology; the 10-K's own change items are decarbonization rules and
  customers' demands, and more EAF capacity. Slow change, read at Q2, not the fast change that routes to TOO HARD here
  **[M1998-008]**, **[M1999-063]**.
- **The row against.** "if we can’t evaluate a carbon steel company, we don’t buy it" **[M2000-038]**: a row about one
  company, evidence of the speakers' view at that date, never by itself a verdict on the industry **[M1994-086]** (the
  convention of 2026-10-07). It is weighed: it warns that the field is one where the forecast is hard. The doubt row
  **[M2002-092]** was tested against it: the doubt here is about the level of earnings (the spread), which Q7 handles as a
  range, not about whether the business can be understood from its figures **[M2008-069]**.
- **VERDICT: IN.** The deciding part's economics (cost position, tons, capital per ton) can be read from the filings and
  carried ten years in kind; the price level is not forecast and is carried to Q7 **[M2012-065]**, **[M2006-004]**,
  **[M2008-069]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (segment operating income, $M, from the 10-Ks: FY2019 `0001558370-20-001641` for 2018-2019, FY2021
`0001558370-22-002377` for 2020-2021, FY2023 `0001558370-24-002152` for 2022-2023, FY2025 `0001104659-26-021395` for
2024-2025; "Other" (corporate, profit sharing) and inter-segment left out):

| part | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | five-year 2021-2025 | share |
|---|---|---|---|---|---|---|---|---|---|---|
| Steel operations | 1,840 | 1,031 | 889 | 4,360 | 3,093 | 1,882 | 1,582 | 1,428 | 12,345 | 68% |
| Steel fabrication | 62 | 119 | 121 | 365 | 2,425 | 1,593 | 667 | 407 | 5,457 | 30% |
| Metals recycling | 76 | 16 | 33 | 182 | 116 | 89 | 77 | 97 | 561 | 3% |
| Aluminum | n/r | n/r | n/r | n/r | (2) | (24) | (72) | (173) | (271) | -1% |

Steel operations carries more than half of five-year operating profit and **decides** (CONVENTION, the business of parts,
Q2). Steel fabrication (joist and deck, "approximately one-third of the total domestic steel joist and deck market for
bookings", 10-K Item 1) does not decide; its 2022 and 2023 profits run twenty to forty times its 2018 level and are
treated at Q7 as aberrational, not as a castle's proof. Aluminum is a start-up that has lost money every year it was
reported and does not decide; its future cannot yet be judged (the flat-rolled mill "shipped 15,000 metric tons of
finished product during the second half of 2025", 10-K Item 7) and it is carried at Q7 only as the cash it has shown.
Recycling is small and feeds the mills.

**The kind of business.** The filer's own words: "Some of our products are commodities, subject to their own cyclical
fluctuations in supply and demand" and "The primary competitive influences on products we sell are price, quality, and
value-added services" (10-K Item 1, steel competition); results are "driven primarily from the metal spread" (Item 1A).
This is a commodity business by the rows' marks: the product is bought on price, of which "most insureds don't care from
whom they buy" **[L2004-003]** is the insurance form, and the market sets the price, "whatever he charged for gas was my
price" **[M2012-109]**. By the framework's commodity paragraph (Q2, 2026-10-12) a dependence on the steel price is never by
itself a STOP; the question is whether this is the low-cost producer, read from its own and its rivals' filings: "when a
company is selling a product with commodity-like economic characteristics, being the low-cost producer is
all-important" **[L2000-017]**; "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**; the
cost is measured against the competitor, "if your costs are on parity or less" **[M2001-013]**; "The figures are
available." **[M2009-059]**.

**The competitors.** The 10-K names no rival (a search of its whole text for the steel producers' names and for "peer"
found none; its return graph uses the S&P 500 Steel index). **CONVENTION of this run:** the rivals are taken from the
company's own proxy, which names "the steel sector competitors which consisted of Cleveland-Cliffs Inc., Commercial Metals
Company, Nucor Corporation, and Metallus Inc." as "the principal companies within our industry with which we compete for
business" (DEF 14A 2026, `0001104659-26-035826`); the first three are used (the brief's limit of three) and Metallus, a
special-bar producer, is left out; all four file with the SEC. Rationale: the company's own board names them as the
competitors it measures itself against, the nearest the filings come to the 10-K naming them. Caveats: CMC's fiscal year
ends in August and CMC is mainly a long-products producer; CLF became a steelmaker through its 2020 purchases (before that
it mined iron ore), so its steel record starts with FY2021.

**The competitor row** (pre-tax income over net sales, %, and pre-tax income plus interest over year-end tangible capital,
meaning equity plus debt less cash less goodwill, %, from each company's XBRL-tagged 10-K figures; script
`scripts/compare.py`, output `comparison_output.txt`; tagged-data transcription, flagged per operator rule 4). FY2025
10-Ks: NUE `0001193125-26-071575`, CLF `0000764065-26-000025`, CMC `0000022444-25-000138`; the earlier 10-Ks of each
filer are listed by accession in `notes.md`.

| pre-tax margin % | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2016-25 (sum over sum) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| STLD | 7.4 | 10.0 | 13.7 | 8.4 | 7.4 | 22.9 | 22.6 | 17.1 | 11.3 | 8.2 | 14.3 |
| NUE | 8.0 | 8.6 | 12.9 | 7.9 | 4.1 | 25.2 | 24.7 | 18.1 | 9.4 | 7.9 | 14.3 |
| CMC (August years) | 2.1 | 1.7 | 3.6 | 4.6 | 6.8 | 7.9 | 17.0 | 12.8 | 8.0 | 1.4 | 7.6 |
| CLF (steel from 2021) | n/a | n/a | n/a | n/a | n/a | 18.6 | 7.8 | 2.6 | (5.0) | (10.8) | 3.1 (2021-25) |

| pre-tax return on tangible capital % | 2016 | 2018 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | mean 2016-25 | mean 2016-20 |
|---|---|---|---|---|---|---|---|---|---|---|
| STLD | 17.5 | 34.6 | 14.2 | 55.3 | 56.4 | 32.8 | 18.4 | 13.1 | 28.7 | 22.2 |
| NUE | 18.2 | 32.5 | 8.9 | 65.1 | 62.1 | 37.7 | 16.3 | 12.8 | 29.2 | 19.6 |
| CMC | 7.6 | 10.6 | 18.3 | 20.9 | 40.6 | 27.1 | 16.1 | 3.9 | 16.4 | 11.1 |
| CLF | n/a | n/a | n/a | 42.9 | 18.8 | 8.5 | (5.9) | (13.4) | 10.2 (2021-25) | n/a |

Read in words: over ten years STLD's pre-tax margin equals Nucor's on the sum, below it in the boom years 2021 to 2023 and
at or above it in the other seven; above CMC in every year and above CLF in every steel year. STLD is a low-cost producer at
parity with the lowest-cost rival named, not alone in the title.

**The earlier cycle, written down as found** **[M1997-127]**: FY2009 to FY2015 STLD's pre-tax income summed $1,009M on
$51,252M of sales, about 2.0%, with losses in 2009 and 2015 (tagged 10-K figures; Nucor 3.4% on the same years). For seven
years the field's low-cost players earned ordinary or worse returns on their equity. The change for the better since 2016
coincides with the trade measures Item 1A names ("measures to curb unfair trade such as tariffs, duties or quotas") and
with a pandemic boom.

**The field's returns over the last full cycle (section C).** The last full cycle is taken trough to trough, 2016 (7.4%)
to 2020 (7.4%), with the boom of 2021 and 2022 and the decline to 2025 (8.2%) after it. Over 2016 to 2020 STLD earned a mean
22% pre-tax on tangible capital and Nucor 20%; over 2016 to 2025, about 29% each. Those are not ordinary returns. The
change for the better since 2009-2015 is credited because it has met falling volume and held: STLD's steel shipments fell
in 2020 (10,718,333 tons against 10,816,641 in 2019; FY2021 and FY2019 10-Ks) and in 2024 (12,660,487 against 12,821,753;
FY2025 and FY2023 10-Ks), and the pre-tax margin in those years was 7.4% and 11.3%, above every year of 2009-2015. That is
the evidence the rows ask for, the price behaviour through the bad year **[M2005-020]**, **[L1995-022]**, read under the
convention of section C; its re-look condition has been met, not left pending.

**The castle tests, each with its fact.**
1. *Key factors and permanence* **[M1995-038]**: the EAF process from scrap ("more than 80% of the metallic melt mix in EAF
   steelmaking, in contrast to integrated mill steelmaking, where the proportion of scrap has traditionally been
   approximately 25% to 35%", Item 1), the scrap business that sold 65% of its ferrous output to the company's own mills in
   2025, mills near scrap and customers, and a pay structure largely at risk (Item 1). Permanent against the blast-furnace
   mills, whose way of making steel is as "ingrained" as GEICO's rivals' agents were **[L1995-011]**; not permanent against a
   new EAF mill, which buys the same furnaces.
2. *Without the lord* **[L2007-006]**: the advantage is a process and a pay culture, not one man; the co-founder steps down
   as CEO on 2027-01-01 and the CFO since 2007 succeeds (8-K `0001104659-26-090129`). Weighed at Q5.
3. *The money test* **[M2011-015]**: **fails.** Money can build this: the company itself built the Sinton flat-roll mill and
   entered aluminum rolling; Item 1A warns that "the introduction of additional domestic steel capacity could increase this
   global overcapacity" and that "additional EAF mills may be constructed, or companies currently operating blast furnace
   mills may invest in EAF mills". "Normally, if you’ve got a profitable business, you know, a dozen people want to go into
   it." **[M2000-077]**. In a commodity business the rows answer the entrant not with a moat but with cost: the low-cost
   operator survives him **[L2004-007]**. Carried as the strongest evidence against.
4. *Pricing power* **[M2005-020]**: none of its own; in 2021 "average selling prices increasing 81%" while ferrous scrap
   prices "increased 73%" (FY2021 10-K), and in 2025 "Steel segment average selling prices decreased 1%" (FY2025 10-K). It
   passes cost through with the market, not ahead of it **[M2005-017]**.
5. *Unit volume*: "record steel shipments of 13.7 million tons" in 2025 and mill utilization "86% in 2025 compared to 81%
   2024" (Item 7).
6. *The low-cost position* **[M2018-043]**: shown above, at parity with Nucor over ten years, ahead of CMC and CLF.
7. *Brand*: none. "Approximately 70% of our steel and steel fabrication sales are considered value-added" (Item 1), but the
   coatings and grades are ones the rivals also make.
8. *The low bid* **[M2017-009]**: the customer buys on price, quality and service (Item 1); fails, as a commodity does.
9. *Ask the competitors*: no instance on the public record found by this run; not answered.
10. *Widening or narrowing* **[M1999-108]**: the gap against the integrated mills holds (CLF's losses in 2024 and 2025);
   against the EAF rivals it is parity, and the new capacity named in Item 1A narrows the field's spread.
11. *What could destroy or reduce it* **[M2000-014]**: trade protection relaxed (Item 1A: "Should current or new tariffs,
   duties or quotas expire or be relaxed, repealed or circumvented by importers of steel and steel products, or should trade
   agreements be renegotiated, downward pressure may be exerted on United States steel and steel products prices"), scrap
   inflation as EAF capacity grows (Item 1A), and imports of a product "that can be shipped in from abroad very easily"
   **[M2007-116]**. None forecast; each weighed.

**Verdict reasoning.** The commodity paragraph puts the decision on the cost position; the cost position is low, at parity
with the lowest-cost rival named and well ahead of the high-cost ones; and the field's low-cost players have earned more
than ordinary returns over the last full cycle, including two years of falling volume. That is the rows' exception:
"Another way to prosper in a commodity-type business is to be the low-cost operator." **[L2004-007]**; "being a low-cost
producer of something that’s essential to people, it’s going to be a very good business usually" **[M2004-091]**. Against
it, written down and not argued away: the money test fails **[M2011-015]**; the title is shared, so "a tough market helps
the low-cost operator" **[L1997-021]** helps Nucor as much; the advantage over a new EAF entrant is parity at best, and in
such a field "the improvement you get one day, your competitor gets the next day" **[M2004-053]**; and 2009-2015 shows what
the field earns when supply runs ahead. These bear on how sure and how large the cash is, which is Q7's work **[M1999-104]**;
they do not show the castle open on the evidence, since the returns through two falling-volume years held and the cost
ranking among the four has held for ten years, read from their filings. The castle is not one whose future cannot be judged
in the sense of "We don’t know how to valuate that" **[M2000-019]**: the cost position is measured, and the uncertainty is
in the spread, which Q7 carries as width.

- **VERDICT: IN**, on the deciding part, with the money test's failure and the shared title carried to Q7 as uncertainty in
  the cash **[L2004-007]**, **[M2001-013]**, **[M2009-059]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital needed** (the capital "actually needed in the business" **[M2010-090]**): pre-tax income plus
  interest over year-end tangible capital, Q2's table: 17.5% in 2016, 34.6% at the 2018 peak, 14.2% in 2020, 55-56% in
  2021-2022, 13.1% in 2025; mean 22% over 2016-2020 and 29% over 2016-2025. The boom years are read as "a cyclical peak in
  earnings" **[L1994-009]**, and "we would not want to buy things on the basis that these returns would be sustained"
  **[M1998-016]**. Over FY2009 to FY2015 the same business earned about 2% pre-tax on sales (Q2).
- **Reinvestment to stand still and to grow.** Capital spending 2016-2025 summed $8,641M against depreciation and
  amortization of $3,759M (tagged 10-K cash-flow figures, `scripts/q7.py`), plus about $1,250M for businesses (2016
  $123M, 2018 $434M, 2019 $97M, 2020 $60M, 2022 $134M plus $222M for 45% of New Process Steel, 2025
  $176M net of cash for the other 55%). The growth projects named in the filings are the Sinton flat-roll mill (the company's
  capital spending was $1,198M in 2020 and $1,006M in 2021, the latter "primarily within our steel operations segment" as
  Sinton's operations commenced, FY2021 10-K), four new value-added lines, a biocarbon
  plant, and the aluminum mill and slab centers: aluminum segment capital spending of $968M in 2023, $1,309M in 2024 and
  $593M in 2025 (10-K FY2025 segment note). Outside aluminum, segment capital spending ran $690M, $629M and $474M in
  2023-2025 against non-aluminum depreciation and amortization of $433M, $472M and $532M. The filing states no maintenance
  figure; the guess the owner is "entitled to" **[M2000-144]** is the depreciation charge, which the rows allow as "a proxy
  for required capital expenditures" **[M1998-127]**, and which the years before the Sinton build support (capital spending
  of $198M, $165M and $239M in 2016-2018 against depreciation of $296M to $317M). The rest is "optional outlays, aimed at
  business growth" **[L1999-024]**.
- **What the added capital earned.** Tangible capital rose from $4,049M (2016) to $11,921M (2025), +$7,872M; pre-tax
  income plus interest rose from $710M to $1,563M, +$853M, about 11% pre-tax on the added capital between two years the
  filer describes as weak (2016 and 2025, each about 7-8% pre-tax on sales). Leaving out the aluminum segment's 2025
  operating loss ($173M) and the $1,667M of construction in progress at 2025 year-end (10-K PP&E note), about 16%. The
  aluminum investment of roughly $2.9B (2022-2025 segment capital spending, the 2022 figure not separately read) has earned
  nothing yet; whether it will is not shown. "whether that’s good or bad depends on what we earn on that incremental $130
  million over time" **[M2001-019]**.
- **The growth arithmetic and its caps.** Earnings rose because capital rose: "We just put way more capital into the
  business as we went along" **[M2023-081]** is the shape of the 2016-2025 record outside the price boom. Growth carried at
  Q7 is capped by what the farm can produce **[M1999-067]**.
- **WEIGHS AGAINST.** A capital-heavy business, "the second-best choice" at most **[M2018-055]**, whose added capital has
  earned about 11% pre-tax between like years with $2.9B in aluminum still unproven; the rows ask only "decent returns on the
  incremental sums they invest" **[L2009-012]**, and the record shows decent, not high, returns on the increment, with the
  largest single increment not yet tested.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten year-ends 2016-2025** **[M2025-032]** (`tools/run.py` table, first-filed XBRL vintages,
  accessions in `run_py_output.txt`; the FY2025 and Q2 2026 statements read as filed):
  - *Equity against goodwill and intangibles*: equity $2,927M to $8,957M (and $9,420M at 2026-06-30); goodwill $393M to
    $477M, intangibles $284M to $331M. Purchased goodwill is small against equity; the business was built, not bought.
  - *Retained earnings* $2,210M to $15,689M while treasury stock reached $7,981M at cost (2025) and $8,288M (2026-06-30):
    most of what was kept went into mills and into buying back about 42% of the share count (diluted shares 245.3M in 2016,
    148.4M in 2025, tagged).
  - *Cash* $841M (2016) to $770M (2025) and $568M (2026-06-30); short-term investments ran to $721M in 2023 and nil at
    2025 year-end.
  - *Receivables against sales*: $704M on $7,607M (9.3%) in 2016, $1,683M on $18,177M (9.3%) in 2025; $2,435M at
    2026-06-30 on first-half sales of $11,296M, up as prices rose. No drift.
  - *Inventory against sales*: $1,275M on $7,607M (16.8%) in 2016, $3,739M on $18,177M (20.6%) in 2025; the 10-K ties the
    2025 rise to "a $624.8 million dollar increase in inventories, primarily within our aluminum operations segment as our
    recycled aluminum flat rolled products mill began commissioning" (Item 7), and $206M came with New Process Steel (Note 2).
    Explained, not suspicious **[M1995-064]**.
  - *Debt*: $2,357M (2016) to $4,211M (2025), $4,182M at 2026-06-30; all fixed-rate senior notes due 2027 to 2055, revolver
    of $1.2B undrawn (Note 3). Deferred income taxes $1,071M at 2026-06-30.
  - *What they don't say*: capitalized interest (cash interest paid $156.7M in 2025 against $70.0M of expense) sits in the
    plant and will come back as depreciation; noncontrolling interests are negative ($200M deficit at 2026-06-30), the
    partners' share of start-up losses; redeemable noncontrolling interests $143M are puts the company may have to buy.
- **The real costs.** Depreciation is charged ($515.0M in 2025, partly units-of-production "subject to minimum and maximum
  levels", Note 1); stock pay is expensed ($69.0M) and is charged in owner cash; profit sharing ("8% of consolidated pretax
  income", Item 7) is a cash cost inside operating income; no restructuring charges recur; impairments: none in 2023-2025
  ("There were no material indicators of impairment or impairment charges recorded during 2025, 2024, or 2023", Item 7), one
  of $16M in Q2 2026 on relocating a slab center (Ex. 99.1, `0001104659-26-085277`). Owner cash is taken "after interest,
  taxes, depreciation, amortization and all forms of compensation" **[L2021-003]** and recast at Q7.
- **EBITDA in the filer's own mouth.** The Q2 2026 release leads with "Adjusted EBITDA of $921 million and cash flow from
  operations of $428 million" (Ex. 99.1, `0001104659-26-085277`); the 10-K uses EBITDA only in the covenant definitions.
  "The one figure we regard as utter nonsense is the so-called EBITDA." **[M1998-086]**; an adjusted figure featured
  **[L2016-006]**.
- **Guidance, and the record against it.** The company issues per-share earnings guidance each quarter, about two weeks
  before the quarter ends, and has met or beaten it in every quarter checked:

  | quarter | guidance (8-K, Ex. 99.1) | reported (8-K, Ex. 99.1) |
  |---|---|---|
  | Q2 2025 | $2.00-$2.04 (`0001104659-25-060609`) | $2.01 (`0001104659-25-069499`) |
  | Q3 2025 | $2.60-$2.64 (`0001104659-25-090047`) | $2.74 (`0001104659-25-101080`) |
  | Q4 2025 | $1.65-$1.69 (`0001104659-25-121880`) | $1.82 (`0001104659-26-006889`) |
  | Q1 2026 | $2.73-$2.77 (`0001104659-26-030153`) | $2.78 (`0001104659-26-045938`) |
  | Q2 2026 | $3.51-$3.55 (`0001104659-26-075470`) | $3.69 (`0001104659-26-085277`) |
  | Q3 2026 | $5.34-$5.38 (`0001104659-26-108777`) | to be reported 2026-10-19 |

  "the scourge of earnings "guidance" and the desire of CEOs to "hit the number."" **[L2019-006]**; "we become downright
  incredulous if they consistently reach their declared targets" **[L2002-041]**. Read for what it is: a range of four cents
  set inside the quarter, not a year-ahead promise; the misses are all upward. Recorded as a weighing against and carried to
  Q5 (the make-the-numbers paragraph, Q4).
- **Tells in the accounts** **[M1995-064]**: none found. Prepaid and other current assets $315M at 2026-06-30 against
  $293M at 2025 year-end; inventory movements explained; no reserve releases seen; no restatement in the 10-Ks read;
  receivables steady against sales.
- **VERDICT on the accounts: IN** (no confusion, no suspicion the statements raise **[M1995-063]**); **WEIGHS AGAINST** on
  the habits (quarterly guidance met or beaten in five of five quarters, Adjusted EBITDA headlined), which are "a negative"
  and not "a total exclusionary factor" **[M1994-018]**, carried to Q5. The recast earnings feed Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The record against the hand dealt** **[M1994-008]**: the same field, the same imports and the same scrap market as
  Nucor, and over 2016-2025 the same pre-tax margin on the sum, ahead of CMC every year and of CLF every steel year (Q2). The
  chief executive co-founded the company in 1993 and "was responsible for the design, construction, and start-up operation
  of all of our steel mills" (10-K Item 1); most operating chiefs named in Item 1 joined between 1994 and
  2003. The record is the founders' own, made in the business, not bought: goodwill is $477M against $9.4B of equity.
- **Where ability is doubtful.** Sinton's ramp was slow: the 10-K's own risk factor says "Delays in achieving full
  operational capacity at our new facilities has adversely affected and may continue to adversely affect our prospects"
  (Item 1A), and 2025 is the year "the Sinton Flat Roll Division’s year-over-year operating performance improved" (Item 7).
  The aluminum venture is a move into a business the filing itself calls one "in which we have little experience, including
  the aluminum industry" (Item 1A), at about $2.9B: "Loss of focus is what most worries Charlie and me" **[L1996-033]**.
  Weighed, not closed on: the venture is next to the scrap business and the filing ties it to existing flat-roll customers
  (Item 1).
- **How they treat themselves against the owners (the proxy)** **[M1994-009]**: CEO total pay of $12.06M in 2025, $11.78M
  in 2024 and $11.82M in 2023 (Summary Compensation Table, DEF 14A `0001104659-26-035826`); the annual plan pays only above
  a 10% return on average equity (CD&A); "our CEO holds 323 times his base salary in our common stock" (CD&A); hedging is
  prohibited and pledging severely limited. They have, on the proxy's figures, "gotten rich with their shareholders"
  **[M2003-055]** more than off them. Pay design is weighed at Q6, Part B.
- **The reports** **[M1998-036]**: the 10-K names its own difficulties (the Sinton delays, the aluminum inexperience, the
  scrap squeeze from new EAF capacity) in plain words; that is the candour the row asks for.
- **The habits carried from Q4**: quarterly per-share guidance met or beaten five times in five, and Adjusted EBITDA
  headlined in the release. "we become downright incredulous if they consistently reach their declared targets"
  **[L2002-041]**; the row's concern is that the managers "will at some point be tempted to make up the numbers". Read with
  the rest of the record: the guidance is set within the quarter, about two weeks before it ends, on a business whose
  results are largely known by then; the statements show none of the tells (Q4); no restatement in the 10-Ks read;
  environmental fines "did not exceed $1 million in aggregate" (Item 3); the related-person transactions are three
  relatives employed at market pay under $475,000 each and rail sales to a director's employer on market terms (proxy);
  one late Form 4 by the CEO in 2025 (proxy). The habit is recorded against them; it does not, on this record, raise a
  doubt about honesty, which is the test **[M2013-088]**. It does say the management watches the street's number
  **[M2004-067]**.
- **Love of the business and after the money**: the founder holds 323 times his salary in stock after thirty-three years
  and stays as executive chairman; the successor named on 2026-08-04 (8-K `0001104659-26-090129`) is the CFO since 2007, an
  insider of twenty-eight years; the board named the next generation before it was needed **[L2011-001]**.
- **Who besides the CEO**: answered by the board itself in August 2026. The new CEO's ability as an operator is untested in
  that role; she has run finance, legal, strategy and "several operating joint ventures" (10-K Item 1).
- **VERDICT on integrity: IN** (no doubt raised by the record read **[M2013-088]**, **[M2015-047]**); **ability WEIGHS FOR**
  (a record at parity with the best rival over a decade, built not bought), with the guidance habit, the slow Sinton ramp and
  the aluminum diversification weighed against **[M1994-008]**, **[L1996-033]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- *The retention test* **[R1995-009]**, **[M1998-110]**: retained earnings rose from $2,210M (2016-12-31) to $15,689M
  (2025-12-31), $13,479M kept after dividends over nine years (10-K balance sheets). Market leg: the 10-K for FY2016 put the
  market value of shares held by non-affiliates at $4,764M as of 2016-06-30 (cover, `0001144204-17-011732`, tagged); the
  market value today is $34,489M after $7.7B of buybacks over 2016-2025 (tagged cash-flow figures). The market leg passes by
  a wide margin. Intrinsic leg, which the market leg alone can mislead **[R2009-002]**: owner cash after maintenance (Q7's
  series) averaged $723M a year over 2016-2020 and $2,193M over 2021-2025, an increase of about $1,470M a year on the
  $13.5B kept, about 11% after tax; but the later cycle holds the 2021-2022 price boom, so the leg is flattered. Forward
  **[M2010-097]**: the largest single use of the money kept, the aluminum mill, has earned nothing yet (Q3).
- *Buybacks* **[L1999-023]**, **[L2016-002]**: the programme names no price; purchases "take place as and when we
  determine in open market or private transactions made based upon the market price of our common stock, the nature of
  other investment opportunities or growth projects" (10-K Item 7). Average prices paid (tagged dollars over shares):
  2016 $34.20, 2017 $34.09, 2018 $39.97, 2019 $30.85, 2020 $24.21, 2021 $62.76, 2022 $78.30, 2023 $108.37, 2024 $128.95,
  2025 $134.46; Q2 2026 by month $209.47 (April), $237.06 (May), $269.60 (June) (10-Q Part II Item 2); Q3 2026 "$261
  million, or just under one percent" at prices not yet filed (8-K `0001104659-26-108777`). Against the bottom of the Q7
  range (written back with Q7): the bottom is $228.24 a share on the all-equity central basis. Every yearly average to
  2025 and April 2026 ($209.47) sit below it, and on those the purchases are read by what they did; May 2026 ($237.06)
  sits above the bottom and June 2026 ($269.60) above the top of the range ($254.89). A programme with no stated price
  whose latest purchases were paid above the range **weighs against** **[L2016-002]**; "what is smart at one price is
  dumb at another" **[L2011-003]**.
- *Issuance and deals*: no share issuance for any deal; the share count fell from 245.3M diluted (2016) to 143.3M (cover,
  2026). New Process Steel was bought for cash in two steps, $222M for 45% (2022, tagged) and $228.9M for the rest (2025,
  Note 2), a business that was "Steel Dynamics’ single largest flat roll steel customer" (8-K Ex. 99.1,
  `0001104659-25-117578`); its pro forma adds little to 2025 net income ($1,189.8M pro forma against the reported figure,
  Note 2), so value got against value given **[M1995-001]** cannot be shown from the filing; it is small (about 1.3% of the
  market value). The all-stock STOP **[L2009-019]** does not arise.
- *Dividends*: $291M paid in 2025, raised 9% that year (Item 7); small against owner cash; no ratio rule is stated.
- **Part A: UNDECIDED.** The retention record passes on the market leg and, flattered by the boom, on the intrinsic leg;
  the buybacks carry no price and their test is at Q7; the largest use of retained money is untested **[M2001-111]**,
  **[L2010-002]**.

**Part B: the pay, the board and the owners.**
- *Pay against capital* **[L1994-019]**: the corporate bonus pool is 5.5% of "Adjusted Net Income" above a 10% return on
  average equity (CD&A), a capital charge of the kind the row asks for. Against it: "Adjusted Net Income" is "before taxes
  and extraordinary items, including adjustments for occasional start-up expenses associated with significant capital
  expenditures or businesses, non-cash asset impairments" (CD&A), so the aluminum start-up losses do not reduce the pool;
  "you get what you reward for" **[M2016-083]**; and the 10% hurdle sits below what this business earned in most years, so
  the chief executive's annual award was the "maximum award of 350% of his annual base salary" for 2025 (CD&A), a year in
  which net income fell 23% (Item 7). Divisional awards start at a minimum return on assets "between 0% and 6%" (CD&A), a low
  bar **[M2004-097]**.
- *Long-term pay*: performance shares measured against "Cleveland-Cliffs Inc., Commercial Metals Company, Nucor
  Corporation, and Metallus Inc." (CD&A); relative measures, tied to what management controls **[M2003-019]**. Restricted
  stock units are granted to every full-time non-union US employee (10-K Item 1). One-time transition awards of $2,000,000
  of restricted stock units each to two executives moved to new roles (8-K/A `0001104659-26-098390`).
- *Ownership*: "our CEO holds 323 times his base salary in our common stock and our other NEOs hold, on average, 42 times"
  (CD&A); hedging prohibited. "gotten rich with their shareholders" **[M2003-055]**.
- *The board*: chair and chief executive combined in one person since 2021, with a lead independent director (proxy); from
  2027 the retiring CEO becomes executive chairman over his successor; "how hard it is to replace a mediocre CEO if that
  person is also Chairman" **[L2014-026]** bears only if the successor proves mediocre. The board named a successor ahead of
  time **[L2011-001]**.
- **Part B: UNDECIDED.** A capital charge and heavy ownership weigh for; a low hurdle, start-up losses kept out of the
  bonus measure, and an executive chairman over a new chief executive weigh against **[M1994-009]**, **[L1994-019]**.

## Q7 — WHAT IS IT WORTH? STOP.
The value is "the discounted value of the cash that can be taken out of a business during its remaining life"
**[R1996-018]**, at the long government rate **[L2000-021]**, **[M1996-025]**, held as a range **[L2000-024]**, under Q7's
range convention and its specifics (CONVENTION, the framework's, Part VI). Arithmetic in `scripts/q7.py`, output
`q7_output.txt`; inputs are the tagged 10-K cash-flow figures cross-checked for FY2025 at Step 0.

**Owner cash after every real cost, by year ($M)** (operating cash flow less stock pay less the stated spending; working
capital changes are inside operating cash flow and so counted, specific (d)):

| year | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| all capital spending charged | 623 | 538 | 1,133 | 896 | (267) | 1,140 | 3,492 | 1,800 | (90) | 433 |
| and acquisitions charged | 500 | 532 | 699 | 799 | (327) | 1,140 | 3,136 | 1,800 | (90) | 257 |
| maintenance only (depreciation as the guess, Q3) | 525 | 404 | 1,055 | 1,027 | 605 | 1,798 | 4,017 | 3,020 | 1,299 | 830 |

- **The window and the cycle base, specific (a).** The literal five-year window is 2021-2025. Its first year is a cyclical
  peak on the filer's own description ("average selling prices increasing 81%" and a metal spread that "increased 86% in
  2021 compared to 2020", FY2021 10-K), and 2022 is the record year. So the base is the average over the last full cycle
  and the growth is measured between the averages of successive cycles **[L2005-003]**. The cycles are read from the
  pre-tax margin (Q2): troughs in 2015-2016, 2020 and 2025 (8.2%, the year the 10-K says "Metal spread compression" lowered
  operating income), peaks in 2018 and 2021-2022. The last full cycle is 2021-2025 and the one before is 2016-2020; each
  runs from the year after one trough to the next trough and holds one peak. Here the cycle base and the literal window
  cover the same years; they differ in the growth.
- **Base, all-equity basis** (owner cash before interest: after-tax interest of $55M a year added back, the
  income-statement interest expense of 2021-2025 averaged and taxed at 21%, near the 20.5% and 21.8% effective rates of
  2025 and 2024; capitalized interest left inside capital spending, a conservative choice, said here): growth case (all
  spending and acquisitions charged) $1,304M; maintenance-only case $2,248M.
- **Acquisitions, specific (c).** Net purchases over the window $532M against owner cash before purchases of $6,775M: not
  a serial acquirer. Default pair: purchases deducted, total growth credited. No deal is signed and unclosed; New Process
  Steel closed inside the window (2025-12-01) and is in the figures from that date.
- **Growth shown, specific (a), and the cap, specific (f).** Between the cycle averages ($441M to $1,249M with acquisitions
  charged; $723M to $2,193M maintenance) owner cash grew 23.2% a year (24.8% maintenance; 18.3% before acquisitions).
  Carried ten years, 23.2% takes owner cash from $1,304M to about $10.5B a year, three times the best year the company has
  had ($3,136M in 2022 on this basis) and about 55% of the cycle's average sales of $19,036M, against the highest share of
  sales it has earned in the filings read, 15.7% (2022). That is the absurdity the cap is for: "what the farm produces is
  all you’re going to get from the farm" **[M1999-067]**; "you get into infinite numbers" **[M1997-095]**. The growth carried
  is cut to the business's own sales growth between the same cycles, 14.3% a year (itself mostly a price-level jump), and
  that is above the discount rate, so it is cut to the discount rate, 5.6% (specific (f): "never above the discount rate").
  Both the shown rate and the cut are written here; the uncut case is shown beside. A reading of (f) that grows sales at
  their own 14.3% before testing the share would not fire the cut (14.5% against 15.7%); it is set down under What was
  unclear. The general clause, "any result that traces to an absurdity is cut back", cuts it on either reading.
- **Growth spending, specific (e).** The filing gives no maintenance figure; the guess is depreciation (Q3). The central
  pair is the maintenance-only case at no growth and the growth case with all growth spending and purchases charged. The
  growth case comes out below the maintenance no-growth case: the growth bought, at a rate the farm can bear, is worth less
  than its cost, so the maintenance no-growth case is the top of the range and the growth case the bottom. "growth can
  destroy value if it requires cash inputs in the early years of a project or enterprise that exceed the discounted value of
  the cash that those assets will generate in later years" **[L2000-023]**. The inversion is the finding.
- **Net debt** (on what the floor is earned, the all-equity basis): long-term debt and current maturities $4,182.1M less
  cash $567.7M at 2026-06-30 (10-Q balance sheet) = $3,614.4M; no short-term investments held; the 10-Q states no
  subsequent event; operating leases ($171.7M at 2025 year-end, tagged) left out, said so; redeemable noncontrolling
  interests ($143.3M) left out, said so; the Q3 2026 buybacks of $261M (8-K, after the 10-Q) left out, which also leaves the
  share count unreduced, the two roughly offsetting. Tax: owner cash is after the company's own tax paid; no carryforward or
  credit running out inside ten years is stated in the notes read.

| case (whole business, $M; ten years, then no growth) | cash | growth | value at 5.6% | per share | value at 10% | per share |
|---|---|---|---|---|---|---|
| **bottom: growth case, all spending and purchases charged, growth cut** | 1,304 | 5.6% | 36,327 | **$228.24** | 19,160 | $108.46 |
| **top: no-growth case, maintenance only** | 2,248 | 0% | 40,147 | **$254.89** | 22,483 | $131.64 |
| beside: no growth, all spending and purchases charged | 1,304 | 0% | 23,287 | $137.25 | 13,041 | $65.77 |
| beside: growth case uncut (cycle to cycle) | 1,304 | 23.2% | 141,896 | $964.79 | 65,956 | $434.96 |
| beside: maintenance with growth at 5.6% (no growth spending charged; shown only) | 2,248 | 5.6% | 62,630 | $411.75 | 33,032 | $205.25 |
| beside, literal window: all spending and purchases, end-year decline carried | 1,304 | (31.1%) | 2,740 | $(6.10) | 2,288 | $(9.26) |
| beside, literal window: maintenance, end-year decline carried | 2,248 | (17.6%) | 10,697 | $49.41 | 7,601 | $27.81 |

Per share = (whole-business value less net debt of $3,614M) over 143.328M shares. Beside the window, the latest twelve
months to 2026-06-30 (FY2025 plus the first half of 2026 less the first half of 2025, 10-Q): operating cash $1,572M,
capital spending $616M, stock pay $70M, depreciation and amortization $617M; owner cash $886M on all spending and $885M on
maintenance, held down by a $760M first-half rise in receivables as prices rose.

- **Value range:** $228.24 to $254.89 a share against $240.63 (all-equity central basis; width 1.12 to one). Equity-only
  beside it: $242.68 to $273.20 (owner cash after interest against the market value of the shares).
- **The floor, tested first** (CONVENTION, about ten percent, applied to owner cash after the company's own tax
  **[M2003-149]**): at the price the whole business costs $38,103M (market value $34,489M plus net debt $3,614M). To earn ten
  percent with no growth it would need about $3.8B of owner cash a year; the central cases offer $1,304M and $2,248M, a
  yield of 3.4% and 5.9% on the price, the first below the long bond's 5.6%. Valued at ten percent the two ends are worth
  $19,160M and $22,483M, about half the price. No case the analyst could defend earns the floor; only the uncut 23% growth
  case, which the cap rules out, would. "there’s just a point at which we drop out of the game" **[M2003-149]**.
- **The screamer.** The price sits inside a narrow range: "If you need to use a computer or a calculator to make the
  calculation, you shouldn’t buy it." **[M2009-005]**.
- **Fair price (a reporting figure, never a verdict; Part VII):** **$120.05** a share on the all-equity central basis (each
  end case valued at ten percent, the two averaged, less net debt), after the company's own tax; equity-only beside it,
  **$140.49**. No cheap price is reported.
- **VERDICT: OUT.** No case in the range earns the floor at the price (the floor tested first), and the price sits inside
  a narrow range besides **[M2003-149]**, **[M2009-005]**, **[M2006-013]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT**, decided at **Q7**: no case in the value range earns the floor at the price; range **$228.24 to $254.89** a share
(all-equity central basis) against **$240.63**; fair price $120.05 (all-equity), $140.49 (equity-only). Q1 IN, Q2 IN (on the
deciding part, steel operations, low-cost producer at parity with Nucor), Q4 accounts IN, Q5 integrity IN; Q3 weighs
against, Q6 undecided on both parts. Integrity facts were judged at Q5, not left unjudged.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts already found that bear on the questions after Q7, each with its source **[M1997-127]**; written down, not weighed;
no verdict; the box unchanged, operator rule 2.)*
- **Q8 (the bond).** The 30-year Treasury par yield is 5.60% (2026-10-09, Treasury). The central cases' owner cash on the
  whole-business price of $38,103M is 3.4% (growth case cash, all spending charged) and 5.9% (maintenance only) (Q7).
- **Q9 (debt and exposures).** Debt $4,286.6M face at 2025 year-end, all senior notes plus $36.6M other: $350M due 2027,
  $650M 2028, $600M 2030, $500M 2031, $600M 2034, $750M 2035, $400M 2050, $400M 2055 (10-K Note 3); the 2025 and 2026 notes
  were refinanced in 2025 (8-Ks `0001104659-25-114956`, `0001104659-25-124210`). Revolver $1.2B undrawn, maturing July 2028.
  Covenants: interest coverage 13.33 to 1 against a 2.50 minimum and debt to capitalization 0.32 against 0.60 (Note 3; the
  coverage is on the facility's EBITDA definition). Pre-tax income over interest expense: 2025 about 22 times ($1,493M plus
  $70M over $70M); 2015, the last loss year, pre-tax loss of $242M against interest of $154M (tagged). Redeemable
  noncontrolling interests of $143.3M (puts). Item 1A: covenant breach "could cause a default under our senior unsecured
  credit facility, our senior notes, or our other debt"; aluminum customers are "a relatively concentrated group"; the
  company has been named a potentially responsible party at "a number of disposal sites"; environmental remediation
  accruals of $4.4M, $2.6M and $0.6M (Item 7). Operating leases $171.7M (tagged, 2025). The "little or no debt" criterion
  **[R1997-001]** is stated for whole businesses.
- **Q10.** Nothing found beyond Q7.
- **Q12.** Steelmaking, scrap recycling, joists and aluminum rolling are not among the businesses the rows name; no
  newspaper-test fact found beyond the environmental items above.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). The
      commits: template, Step 0 to Q1, Q2, Q3, Q4, Q5, Q6, Q7 with the Q6 write-back, close.
- [x] If dispatched to an analyst: the brief allowed the per-question commits; the lock is the dispatching session's and was
      not touched by this analyst; the fold is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule). Seen by accident
      and declared under contamination at the top: commit subjects of another company's run naming a margin comparison that
      includes STLD; file names of other research folders. Not used: the Q2 comparison was computed from the filers' XBRL by
      this run's own script.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check script
      `scripts/check_ids.py`, output `check_ids_output.txt`); every filing fact carries its document and accession; figures
      from tagged XBRL are flagged as transcription, with one FY2025 figure set cross-checked against the filed statement.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operating cash less stock pay less capital spending and
      purchases, or less depreciation as the stated maintenance guess); the sovereign from the Treasury; the price quote is an
      aggregator's, flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (foundations list; Q2's earlier cycle and the money test; Q4's
      guidance record; Q5's Sinton and aluminum); facts for later questions under AFTER THE STOP.
- [x] No row dated after the anchor is cited (not a point-in-time run; the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its yield, "growth the price assumes" and
      points-over-sovereign lines were not used.
- [x] `python tools/check_framework.py` PASS before the closing commit (output in `check_framework_output.txt`).
- Honest notes: (1) the rival figures are tagged XBRL, not read from the rivals' filed statements; CLF's and CMC's
  comparability caveats are stated at Q2. (2) The 2016 market value used in Q6's market leg is the non-affiliate float on
  the FY2016 cover, a lower bound. (3) The Q3 2026 buyback prices are not yet filed. (4) The maintenance figure is a guess
  (depreciation), as the filing states none. (5) The H1 2026 upswing (Q3 2026 guidance of $5.34 to $5.38 a share) is outside
  the fiscal-year window and enters only the twelve-month line beside it.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Specific (f), the cap, has two readings.** It fires "where the shown growth of owner cash, carried ten years, would
require owner cash above the highest share of sales the business has earned", without saying sales at what date. Against
today's or the cycle's sales the 23% cycle-to-cycle growth fires it at once (55% of sales against a best of 15.7%); against
sales themselves carried at their own cycle-to-cycle growth (14.3%, a price jump) it does not (14.5%). In a commodity
business the two growth rates are the same price boom, so the second reading can never fire. I used the first, and the
general clause ("any result that traces to an absurdity is cut back") agreed; the decision turned on it, since the uncut
case alone would earn the floor and send the file to the width test. A sentence naming the sales base would close it.
(2) **The cycle base when the window is the cycle.** Specific (a) moves the base to the last full cycle when an end year is
aberrational, but here the last full cycle is the literal window, so (a) changes only the growth, from a 31% decline (end
years) to a 23% rise (cycle averages). Neither is a growth rate a business carries for ten years; the text could say what
growth (a) carries when two successive cycles differ mainly by price level, which is the commodity case Q2's paragraph sends
here. (3) **The money test against the commodity paragraph.** Q2's test 3 fails for any commodity business with an entrant
in sight, and the commodity paragraph puts the decision on the cost position; the text does not say in so many words that
the low-cost exception answers the money test. I read it so and carried the failure to Q7. It also does not say whether a
shared title (cost parity with one rival) is "the low-cost producer"; I read parity as enough on **[M2001-013]**. (4) **The
competitors when the 10-K names none.** The brief allows a confessed choice; the proxy's named LTIP peer group was the
nearest filing source. A standing rule (the proxy's named competitors first) would make runs comparable. (5) **The
maintenance guess.** Specific (e) applies "where the filing allows the guess"; this filing states no maintenance figure, and
I took the depreciation proxy the rows allow **[M1998-127]**. Whether a proxy counts as the filing allowing the guess is not
said; the central range depends on it (without it the range would be the all-spending pair, $137.25 to $228.24, and the box
the same). (6) **The all-equity add-back** says "owner cash before interest" but not what to do with capitalized interest,
which here sits in capital spending ($87M in 2025); I left it in, the conservative side, and said so. (7) **Intra-quarter
guidance.** The make-the-numbers paragraph does not separate a year-ahead target from a range issued two weeks before a
quarter closes; I weighed it, as the paragraph says, and found it raised no doubt at Q5 on this record.
