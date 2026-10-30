# Company Run: Commercial Metals Company (NYSE: CMC), 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch** (commit
`5b26f82a`, "CMC run: template copied before any fetch").

**Dispatched blind run** under the canonical brief `Screens/_daily/_dispatch_brief.md`, with the one departure the brief
states: the lines of evidence were derived by the analyst from the 10-K's Items 1, 1A and 7, not supplied by the dispatcher.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled at the fold by the dispatching session (overnight 2026-10-13, after the run was committed): not held (`PORTFOLIO.md` carries no line for CMC or Commercial Metals).

**Contamination, declared.** (1) To check that this run file did not already exist, the analyst listed `Test Runs/` with a
filter on the date 2026-10-13; the listing showed the file names of the other runs of this date, among them
`2026-10-13 Run - STLD Steel Dynamics.md` and `2026-10-13 Run - CLF Cleveland-Cliffs.md`. No such file was opened.
(2) The session context supplied by the harness carried the five most recent commit subjects of the repository, all about an
STLD run of today (its box, its Q2 reading and its range and fair price). Steel Dynamics is one of the three rivals this run
reads from its own filings at Q2. Nothing from those subjects is used: the STLD figures below come from STLD's own 10-K and
XBRL facts, and the Q2 judgment on CMC rests on CMC's, Nucor's and Gerdau's own words. (3) The memory index loaded with the
session names counts of gate-clearers and queue state; it names no company relevant here and is not used.

**Lines of evidence, chosen from the FY2025 10-K (accession 0000022444-25-000138), and why.** Item 1 says the business is a
vertically integrated chain (scrap yards, electric-arc mills, rebar fabrication) whose products are "generally sold in
response to a competitive bid solicitation" and that "global steelmaking capacity greatly exceeds demand", and it credits
Section 232 tariffs with "a favorable backdrop". Item 1A names lower-cost competitors, new U.S. electric-arc capacity, the
need for "regular, substantial capital investments", acquisitions and goodwill, and debt covenants. Item 3 and Note 17 carry
a $110.0 million antitrust jury verdict, trebled. Item 7 reports results as metal margin per ton and tons shipped by
segment, announces two cash acquisitions ($675.0 million and about $1.84 billion), a fourth micro mill ($550 to $600 million
net), and buybacks. So the lines read are: (a) the segments and their profits over the cycle; (b) the cost position against
the rivals (the commodity question of Q2); (c) new capacity and imports (the attacker with money); (d) the tariff dependence;
(e) the antitrust litigation; (f) the acquisitions and their goodwill; (g) debt, leases and the litigation liability;
(h) buybacks and their prices; (i) stock pay and the pay metrics; (j) the receivables securitization that moved operating
cash in FY2017 to FY2019.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $64.77 (2026-10-13, live quote through `tools/run.py`; aggregator, flagged per operator rule 5).
- **Shares by class:** one class, common stock $0.01 par: **110,624,335** shares outstanding on the cover of the 10-Q for
  the quarter ended 2026-05-31 (filed 2026-06-29, accession 0000022444-26-000041), as of 2026-06-25
  (`python Screens/cover_shares.py CMC`). Check: the same 10-Q's balance sheet shows 129,060,664 issued less 18,365,208 in
  treasury = 110,695,456 at 2026-05-31; the cover count is 71,121 lower, consistent with June buybacks. No 8-K or prospectus
  after the 10-Q changes the count (8-Ks of 2026-08-05 and 2026-10-13 read: a buyback authorization and a dividend).
- **Market cap:** 64.77 x 110.624 = **$7,165M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, 30-year par yield, US Treasury daily par yield curve, dated
  2026-10-09 (`python tools/sources.py`; the latest Treasury print before the run date).
- **Filings read** (operator rule 4): 10-K FY2025 (fiscal year ended 2025-08-31, filed 2025-10-16, accession
  0000022444-25-000138), Items 1, 1A, 3, 5, 7 and Notes 17 and 19; 10-K FY2023 (0000022444-23-000126), FY2021
  (0000022444-21-000126) and FY2017 (0000022444-17-000027) for segment history and balance sheets; 10-Q for the quarter ended
  2026-05-31 (0000022444-26-000041), statements and Notes 2 and 14; proxy DEF 14A filed 2025-11-25 (0001193125-25-294507);
  8-Ks of 2025-11-26 (notes), 2025-12-01 (CP&P closed), 2025-12-15 (Foley closed), 2025-12-17 (credit agreement),
  2026-02-19 (8-K/A, Foley's audited FY2024 statements and pro forma, 0001193125-26-059507), 2026-06-25 (Q3 FY2026 earnings,
  0000022444-26-000038), 2026-08-05 (Investor Day and buyback, 0001193125-26-333797), 2026-10-13 (dividend,
  0000022444-26-000048). **No FY2026 10-K was on EDGAR on 2026-10-13** (EDGAR submissions list checked that day); the FY2025
  10-K is the latest annual filing.
- **One figure cross-checked against the filed statement:** net cash flows from operating activities FY2025, **$715,070
  thousand** in the filed consolidated statement of cash flows of the FY2025 10-K, against 715.1 in the XBRL line
  `tools/run.py` printed. Match.
- `python tools/run.py CMC` arithmetic lines only (saved in the research folder, `run_py_output.txt`): owner cash after
  stock pay and all capital spending, FY2023 677, FY2024 530, FY2025 275 ($M); with finance-lease principal deducted, 654,
  496, 235; the five-year window it prints (FY2021 to FY2025) averages 337 on the capital-spending basis and 505 on the
  depreciation basis. D&A FY2025 286; capital spending FY2025 403; stock pay FY2025 37. **Not used as printed:** the tool's
  three-year window and its yield lines; the window and the cycle are set at Q7 below. **Two corrections the tool does not
  make:** (i) FY2017 to FY2019 operating cash is understated by the receivables securitization, whose collections the
  filings put in investing (XBRL `IncreaseDecreaseInAccountsReceivableFromSecuritization`, 616.0, 670.5 and 367.5 in FY2017,
  FY2018 and FY2019); (ii) the $362.3 million FY2025 litigation charge is accrued, not paid, so FY2025 operating cash does not
  carry it (it is carried in net debt at Q7).

**The balance sheets, eight to ten years, read here because the file closes before Q4** (the template's instruction;
`tools/run.py`'s XBRL table checked against the filed statements of the FY2025 and FY2017 10-Ks and the 2026-05-31 10-Q;
$M, fiscal year-ends August 31).

| year-end | total assets | equity | cash | receivables | inventory | goodwill | intangibles | debt on the face | retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 3,131 | 1,367 | 518 | 689 | 540 | 66 | n/a | 758 + 313 current | 1,373 |
| 2017 | 2,975 | 1,401 | 253 | 707 | 614 | 65 | n/a | 806 + 19 current | 1,364 |
| 2018 | 3,328 | 1,493 | 633 | 749 | 589 | 64 | 14 | 1,139 | 1,446 |
| 2019 | 3,759 | 1,624 | 194 | 1,016 | 692 | 64 | 13 | 1,227 | 1,585 |
| 2020 | 4,082 | 1,889 | 545 | 881 | 625 | 64 | 13 | 1,084 | 1,808 |
| 2021 | 4,639 | 2,295 | 501 | 1,106 | 935 | 66 | 10 | 1,043 | 2,163 |
| 2022 | 6,237 | 3,286 | 679 | 1,359 | 1,170 | 249 | 257 | 1,502 | 3,312 |
| 2023 | 6,639 | 4,121 | 596 | 1,240 | 1,036 | 386 | 259 | 1,155 | 4,097 |
| 2024 | 6,818 | 4,300 | 860 | 1,159 | 972 | 386 | 235 | 1,190 | 4,504 |
| 2025 | 7,172 | 4,193 | 1,043 | 1,202 | 934 | 387 | 211 | 1,354 | 4,507 |
| 2026-05-31 (10-Q) | 9,796 | 4,532 | 560 | 1,391 | 1,173 | 2,137 | 464 | 3,400 | 4,888 |

What moved and why, "what the figures are saying and what they don’t say and what they can’t say" **[M2025-032]**:
(1) **Retained earnings did not move from 2015 to 2017** (1,374, 1,373, 1,364): the trough years kept nothing. They then
tripled, 1,446 to 4,507, almost all of it in FY2021 to FY2023 (net earnings 413, 1,217 and 860), the cycle's peak.
(2) **Equity against goodwill and intangibles.** Until 2021 goodwill and intangibles were under 5% of equity; the Tensar
purchase (FY2022, $552M paid) lifted them to 506; the two precast purchases of December 2025 lifted them to **2,600 against
equity of 4,532 at 2026-05-31**, so 57% of book equity is now purchased goodwill and intangibles. (3) **Debt** stayed
between about 1.0 and 1.5 billion for nine years and **rose to 3,400 at 2026-05-31**, financed by the 2025-11-26 notes
(5.75% due 2033 and 6.00% due 2035) for Foley; cash fell from 1,043 to 560 for CP&P. (4) **A liability the debt line does
not show:** the accrued antitrust loss, 362.3 at 2025-08-31 and 373.5 at 2026-05-31, a current liability awaiting the appeal.
(5) **Receivables and inventory against sales** held steady: receivables 15.4% of FY2025 sales against 17.4% in FY2019 and
16.4% in FY2021; inventory 12.0% of FY2025 sales against 11.9% in FY2019; nothing building out of line **[M1995-064]**.
(6) **Treasury stock** rose from 296 (2022-08-31) to 750 (2026-05-31): buybacks, read under AFTER THE STOP. What the figures
cannot say: the cost per ton of CMC's mills against its rivals' (no filing read states it), and what the precast businesses
earn on their price over a cycle (one partial year owned).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what CMC's mills, fabrication shops and precast plants will produce, not where the
quote goes **[M1997-109]**. No macro forecast enters **[M2000-094]**: the filing itself leans on one, Section 232 tariffs
restored and raised to 50% in 2025, which the 10-K calls "a favorable backdrop to the domestic long steel market"; this run
neither forecasts the tariff nor credits it, and records the dependence as a fact about the castle at Q2. Who is paid to
tell you **[M2020-037]**: the Investor Day release of 2026-08-05 (0001193125-26-333797) states "FY29 mid-cycle financial
targets" (core EBITDA of $1,650 to $1,800 million, a free cash flow defined as core EBITDA less capital expenditures);
projections are not consulted **[M1995-050]** and none enters this run. Margin of safety: if the decision needs pencil and
paper, "it’s too close to think about" **[M1996-084]**. **Contrary evidence, written down as found** **[M1997-127]**:
(1) the nine months to 2026-05-31 earned $443.3M net, against a $67.1M loss a year earlier (10-Q, 0000022444-26-000041),
with North America metal margin up $111 a ton year on year (earnings release, 0000022444-26-000038); (2) Gerdau's 20-F
says freight limits competition from non-regional producers, "Rebar deliveries are generally concentrated within a
350-mile radius of the mini mills", a local advantage for a mill sited near demand; (3) the precast purchases add a
business whose economics differ from steel's, and Tensar's geogrids are a proprietary product; (4) CMC claims in its 10-K to
be "the largest manufacturer and fabricator of rebar" in the U.S.

## THE STANDING RULE
A part-interest bought for cash with no borrowing puts the buyer at no risk of ruin; the rule binds the buyer's conduct,
"borrowed money has no place in the investor's tool kit" **[L2014-005]**, and "We are never going to risk what we have and
need for what we don" (the row's own apostrophe is a damaged character) **[M2012-081]**. Nothing in this name changes that;
the target's own debt and the litigation liability are Q9's subject.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test** **[M1995-051]**: understanding means "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**, which needs the "economic dynamics of the industry", not the
  chemistry **[M2011-014]**.
- **The key variables and whether they are foreseeable** **[M1998-044]**. From the 10-K (0000022444-25-000138, Item 7, Key
  Performance Indicators): for the two steel segments, "average selling price per ton and tons shipped", and "metal margin",
  "the difference between the average selling price per ton [...] and the cost of ferrous scrap per ton". So the economics
  are a spread (rebar and merchant bar over scrap) times tons, less conversion cost (power, gas, labour, electrodes), less the
  capital that keeps the mills competitive. Rebar goes into concrete in infrastructure, non-residential and residential
  building; that it will still be needed in ten years needs no forecast. The level of the spread is a commodity price and is
  not forecast here; by the framework's commodity paragraph a dependence on a commodity price is never by itself a STOP at
  Q1 **[M2016-025]**, and Q1 asks only whether the business can be understood from its figures **[M2008-069]**.
- **Do the past statements tell me the future ones** **[M2008-033]**? For the steel side, yes: ten years of segment results,
  tons and margins per ton are filed; the cycle is visible in them (net earnings $46M in FY2017, $1,217M in FY2022). For the
  precast side, one partial year is owned; Foley's audited FY2024 statements are filed (8-K/A, 0001193125-26-059507).
- **Routing.** Not a business of fast technological change: the 10-K's products are rebar, merchant bar, wire rod,
  fabricated rebar, fence posts, geogrids and precast concrete; the newest process, the micro mill, is a continuous
  melt-cast-roll line that both CMC and Nucor run. Not a bank. **The parts** (Q1's holding-company paragraph as extended
  2026-10-06): North America Steel Group carries more than half of five-year segment profit (table at Q2), so it is the part
  that matters, and it is understood by the tests above.
- **Doubt test** **[M2002-092]**: the doubts in this name are about the castle and the price, which are Q2's and Q7's, not
  about whether its economics can be read.
- **VERDICT: IN.** The economics of a scrap-fed electric-arc rebar chain are readable from the filings, "important and
  knowable" **[M2006-076]**, and insiders would write the ten-year shape down (rebar into concrete, priced as a spread over
  scrap), unlike the forecast **[M2000-105]** names.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question is asked from the attacker's side: "all moats are subject to attack in a capitalistic system" and "why is that
castle still standing?" **[M1995-038]**.

**The parts table** (Q2's business-of-parts paragraph). Segment profit is the filer's own segment measure, adjusted EBITDA
(ASC 280; the 10-Ks give no segment operating profit after depreciation), FY2021 to FY2025, $M. Sources: FY2025 10-K Note 19
(0000022444-25-000138) for FY2023 to FY2025 on the three-segment basis; FY2023 10-K (0000022444-23-000126) for FY2022 and
FY2021 10-K (0000022444-21-000126) for FY2021, when the businesses later called Emerging Businesses sat inside North America.

| part | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | five-year sum | share | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| North America Steel Group (with EBG in FY2021 and FY2022) | 746.6 | 1,553.9 | 1,331.6 | 944.4 | 742.5 | 5,319.0 | about 84% (about 80% if the EBG businesses earned in FY2021 and FY2022 what they earned after) | read below | **yes, more than half** |
| Emerging Businesses Group (now Construction Solutions Group) | in NA | in NA | 139.0 | 129.5 | 137.7 | 406.2 (three years) | about 6% | Tensar geogrids proprietary; precast added Dec. 2025 | no |
| Europe Steel Group | 148.3 | 346.1 | 48.5 | 22.5 | 69.3 | 634.7 | about 10% | one Polish mill, energy grants $78.7M in FY2025 | no |

The file closes on North America Steel Group. The precast purchases (about $2.5 billion, December 2025) do not change the
deciding part: the earnings release of 2026-06-25 (0000022444-26-000038) gives the precast businesses $52.9M of a $353.6M
quarter's core EBITDA, and the company's own expected annual contribution, $245 million (a forecast, named and not used),
would still leave the steel group more than half.

**The castle tests, each with its filing fact (North America Steel Group).**
1. **What keeps it standing, and how permanent** **[M1995-038]**. CMC's own account (10-K, Item 1, Competitive Advantage):
   a vertically integrated chain, recycling yards supplying "low-cost raw materials" to mills whose fabrication shops supply
   "a significant and consistent source of demand", and mills sited "in some of the highest demand locations for rebar".
   Each of these is held by its largest rival as well: Nucor's 10-K for 2025 (0001193125-26-071575) describes Nucor Rebar
   Fabrication with "nearly 70 fabrication facilities" (CMC: 53) and three rebar micro mills, and Gerdau names CMC among its
   "principal competitors" in North America with Nucor and Steel Dynamics (20-F for 2025, 0001104659-26-027678). The key
   factors are real, and none is CMC's alone.
2. **The money test** **[M2011-015]**, **[M2012-106]**. Asked of CMC's castle, the answer is in the rivals' filings: Nucor
   "announced that it would build a new rebar micro mill [...] in Lexington, North Carolina", "This is Nucor's third rebar
   micro mill", "$440 million investment to have an annual capacity of approximately 430,000 tons", completed in 2025, and
   micro mills "enables us to serve these markets with a logistics cost advantage relative to competitors operating from
   further away" (Nucor 10-K 2025). CMC's own fourth micro mill costs "$550.0 million and $600.0 million, net" (CMC 10-K,
   Item 7), and its 10-K says "Certain of our competitors have announced and are moving ahead with plans to develop new
   steelmaking capacity" with "a number of ongoing EAF projects in the U.S." (Item 1A). A regional rebar position can be
   bought, for about half a billion dollars, and is being bought by the larger rival. The row's own conclusion is the
   negative one: had the answer been yes, "we wouldn" have done it (the apostrophe is damaged in the row) **[M2011-015]**;
   "you can create another airline. WARREN BUFFETT: Very easily, and you have people that like to do it" **[M2013-054]**.
3. **Pricing power, and the agony before a rise** **[M2005-020]**. In FY2025 "The reduction in average selling prices per
   ton for steel and downstream products outpaced the 4% year-over-year decrease in the cost of ferrous scrap utilized per
   ton", steel prices down 5% and downstream down 9% (10-K, Item 7), North America adjusted EBITDA down 21%. The recovery in
   FY2026 (steel prices up $130 a ton against scrap up $19, earnings release 2026-06-25) followed the 50% Section 232 tariff,
   which the 10-K treats as the cause: "the elimination of Section 232 tariff exemptions is expected to provide a favorable
   backdrop". The price is the market's and the tariff's, not the company's; no price set by CMC and held against the market
   appears in the filings read.
4. **The low-cost position** **[M2018-043]** (the commodity exception, **[L2004-007]**, **[M1997-010]**). The rows measure it
   "more by cost of production" **[M2006-004]**, and "The figures are available" **[M2009-059]**. Here they are not: no filing
   read (CMC's 10-Ks and 10-Q, Nucor's and Steel Dynamics' 10-Ks, Gerdau's 20-F) states a cost of production per ton for
   rebar; each states selling price and scrap cost, the spread, not the conversion cost. What the filings do show:
   (a) CMC's own risk factor, "several of our competitors are significantly larger than us [...] These companies may have a
   lower cost structure [...] they may be able to offer lower prices" (10-K, Item 1A); (b) CMC's own risk factor, "We must
   make regular, substantial capital investments in our steel mills to maintain the mills, lower production costs and remain
   competitive"; (c) the whole-company comparison below, in which CMC's return on capital trailed both Nucor and Steel Dynamics
   in eight of ten years. CMC claims "a low cost, high-quality production process" (Item 1); no filing read shows it lower
   than its rivals'.
5. **Would the customer choose it over the low bid** **[M2017-009]**, **[L2004-003]**. Fabricated rebar "is generally sold in
   response to a competitive bid solicitation" (CMC 10-K, Item 1); Nucor sells "on a construction contract bid basis" (Nucor
   10-K); Gerdau: "Rebar, merchant bars and structural shapes are commodity steel products for which pricing is the primary
   competitive factor" (Gerdau 20-F). The product is bought on the bid.
6. **Who sets the price** **[M2012-109]**, **[M2023-079]**. CMC's 10-K: "Excessive imports of steel into the U.S. have
   exerted, and may continue to exert, downward pressure on U.S. steel prices", and "If the Section 232 or other import
   tariffs [...] are relaxed, repealed [...] a resurgence of substantial imports of foreign steel could occur. This would put
   downward pressure on U.S. steel prices." The marginal ton from abroad, admitted or kept out by the government, sets the
   price.
7. **Ask the competitors** **[M1999-130]**. Gerdau, a rival, lists CMC first among its principal North American competitors
   and calls the product a commodity priced on price (above). Nucor's micro-mill text names the advantage it is taking into
   regional markets, "a logistics cost advantage relative to competitors operating from further away", which is the same
   advantage CMC claims for its own sites.
8. **Widening or narrowing** **[M1999-108]**. Narrowing on the filings: new electric-arc capacity "expected to come online at
   various times over the next one to three years" (CMC 10-K, Item 1A), Nucor's third rebar micro mill in production
   ramp-up, CMC itself adding a fourth. And CMC's own defence of its western market was found unlawful by a jury: Pacific
   Steel Group alleged that CMC entered "an exclusivity agreement for certain steel mill equipment" in violation of antitrust
   law; on 2024-11-05 "a jury returned a verdict in favor of PSG in the amount of $110.0 million", trebled; the post-trial
   motion was denied on 2025-09-29; CMC appealed on 2025-10-24 (10-K Item 3; 10-Q Note 14). A castle whose wall included a
   restraint on a would-be entrant's equipment is not shown to stand on its own.
9. **What could destroy, modify or reduce it** **[M2000-014]**: a relaxed tariff and a resurgence of imports, and new
   domestic capacity, both named by the filer itself (above).

**The competitor row, same metric from each filer's own filings** (XBRL company facts, read against the 10-Ks; EBIT =
pre-tax income plus interest expense; margin = EBIT over sales; return on capital = EBIT over the prior year-end's equity
plus debt less cash; CMC fiscal years end August 31, the others December 31; the rivals' identity: the 10-K names none, so
the three are the run's CONVENTION, below).

| year | CMC margin | CMC return on capital | Nucor margin | Nucor return on capital | Steel Dynamics margin | Steel Dynamics return on capital | Gerdau margin (BRL, IFRS) |
|---|---|---|---|---|---|---|---|
| 2016 | 3.9% | 10.1% | 9.1% | 15.1% | 9.3% | 15.6% | -1.5% |
| 2017 | 2.9% | 8.0% | 9.6% | 19.3% | 11.4% | 24.1% | 4.6% |
| 2018 | 4.4% | 14.7% | 13.5% | 30.9% | 14.8% | 37.1% | 8.1% |
| 2019 | 5.8% | 22.8% | 8.6% | 15.4% | 9.6% | 19.1% | 7.9% |
| 2020 | 7.9% | 26.6% | 5.0% | 11.8% | 8.3% | 15.5% | 11.3% |
| 2021 | 8.7% | 20.0% | 25.7% | 121.0% | 23.2% | 70.2% | 27.7% |
| 2022 | 17.6% | 47.2% | 25.2% | 91.8% | 23.0% | 62.6% | 21.1% |
| 2023 | 13.2% | 24.5% | 18.8% | 48.1% | 17.5% | 36.8% | 15.6% |
| 2024 | 8.6% | 13.2% | 10.2% | 22.7% | 11.6% | 20.8% | 10.4% |
| 2025 | 1.4% (6.0% before the $362.3M litigation charge) | 2.0% (8.8% before it) | 8.4% | 16.9% | 8.6% | 13.7% | 6.6% |
| ten-year mean | 7.4% (7.9% before the charge) | 18.9% (19.6%) | 13.4% | 39.3% | 13.7% | 31.6% | 11.2% |

Accessions of the rivals' latest annual filings read: Nucor 10-K for 2025, 0001193125-26-071575; Steel Dynamics 10-K for
2025, 0001104659-26-021395; Gerdau 20-F for 2025, 0001104659-26-027678. Caveats, written as found: CMC's sales include scrap
resale and fabrication, which carry thin margins on large sales, so the margin column flatters the rivals; the return column
is less affected and shows the same order. Nucor and Steel Dynamics sell mostly flat-rolled sheet, whose 2021 and 2022 boom
exceeded the long-products market's; the comparison is of companies, not of rebar mills. Gerdau's return column is not
shown because its tagged debt series is incomplete. CMC led both U.S. rivals in 2019 and 2020 (the years after its 2018
purchase of Gerdau's U.S. rebar mills, $700.9M), and trailed both in the other eight.

**The field's returns over the last full cycle** (section C). Over 2016 to 2025, trough to recovery to peak to the FY2025
low, the field earned high returns at the 2021 to 2023 peak and ordinary to thin ones in the troughs (CMC 2.9% to 4.4%
margins in 2016 to 2018; Gerdau negative in 2016). The question this run decides is not whether the field's average is
ordinary but whether CMC's position within it is protected; the rows answer that high returns draw the attack, "competitors
will repeatedly assault any business "castle" that is earning high returns" **[L2007-004]**, and the filings show the
assault under way (new capacity, a rival's micro mills in CMC's markets).

**Why not TOO HARD.** The framework's commodity paragraph sends a file to TOO HARD (NATURE) where the cost position decides
and no filing states it. The cost position is not stated, but this file does not turn on it: even granting CMC's claim of low
cost at its newest mills, the source of that cost is equipment and siting that a rival buys for $440 million and places in
the same regional markets, so the advantage is one that "must be continuously rebuilt" **[L2007-005]**, and CMC's own risk
factor says as much. A commodity sold on the bid, priced by imports and tariffs, whose cost position any well-funded rival can
match with a filed capital budget, is a castle shown open on the evidence, not one whose future cannot be judged **[M2000-019]**.
"anything you do, your competitors can copy" **[M1996-017]**; "the improvement you get one day, your competitor gets the
next day" **[M2004-053]**; "you do not want to have something whose competitive position is going to erode over time"
**[M2007-117]**.

**CONVENTION of this run (the rivals):** the FY2025 10-K names no competitor; the run takes Nucor and Steel Dynamics (the two
largest U.S. electric-arc producers filing with the SEC) and Gerdau (a 20-F filer and the former owner of CMC's acquired
rebar mills), because Gerdau's own 20-F names exactly these three, CMC, Nucor and Steel Dynamics, as the principal North
American competitors. Rationale: the rival list is then a rival's, not the analyst's.

- **VERDICT: OUT.** North America Steel Group, the deciding part, sells a commodity on the bid at a price set by imports and
  tariffs; its key factors are held equally by a larger rival; the money test is answered yes in that rival's filed capital
  budget; and no filing shows CMC to be the low-cost producer, while its own filing concedes rivals may be. A castle shown open
  on the evidence closes OUT **[M2011-015]**, and price does not reopen it: "What you can’t do is turn any investment into a
  good deal by paying little" **[M2019-015]**.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- NOT REACHED: the file closed at Q2. Facts found are under AFTER THE STOP.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- NOT REACHED as a verdict. The balance sheets were read in Step 0, as the template asks when the file closes before Q4.
  Facts found are under AFTER THE STOP.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- NOT REACHED. Integrity facts were found and are recorded, not judged, under AFTER THE STOP; the box line carries the flag.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- NOT REACHED. Facts found (buybacks and their prices against the bottom of the computed range, the precast purchases,
  the pay metrics) are under AFTER THE STOP.

## Q7: WHAT IS IT WORTH? STOP.
- NOT REACHED as a verdict. The two reporting figures the brief asks for are computed below.

**COMPUTATION, NOT A CLEARANCE.** (Operator rule 3: arithmetic made after a closing STOP; no entry language; no verdict.)
Built by Q7's range convention in full: owner cash after every real cost, aggregate not per share; all capital spending
deducted; ten years at the growth shown, capped, then zero nominal growth; discounted at the sovereign, 5.60%; the floor of
about ten percent tested before the width; the all-equity basis central, the equity-only figure beside. $M unless per share.
The script is `scripts/q7.py` and `scripts/q7_range.py` in the research folder.

*Owner cash by year* (operating cash as filed, plus the securitization collections the filings put in investing in FY2017 to
FY2019; less stock pay; less capital spending; plus government assistance received for plant (FY2023 $5.0M, FY2025
$50.0M); less finance-lease principal; the all-equity figure adds back cash interest at (1 - 23.6%), the FY2024 effective
rate, a CONVENTION of this run, rationale: one stated rate for every year, the last full year before the litigation charge
distorted the rate). Sources: XBRL company facts read against the filed cash-flow statements of the FY2025, FY2023, FY2021
and FY2019 10-Ks (accessions in Step 0; FY2019 10-K 0000022444-19-000042).

| FY | operating cash, adjusted | capital spending | D&A | owner cash after interest | owner cash before interest (all-equity) | net purchases of businesses | sales | all-equity owner cash / sales |
|---|---|---|---|---|---|---|---|---|
| 2017 | 92.7 | 213.1 | 125.1 | -150.7 | -100.5 | -107.3 | 3,844 | -2.6% |
| 2018 | 236.6 | 174.7 | 131.7 | 38.0 | 68.6 | -68.5 | 4,644 | 1.5% |
| 2019 | 404.5 | 138.8 | 158.7 | 240.6 | 290.4 | 699.0 | 5,829 | 5.0% |
| 2020 | 791.2 | 187.6 | 165.8 | 558.9 | 604.5 | 18.1 | 5,477 | 11.0% |
| 2021 | 228.5 | 184.2 | 167.6 | -15.4 | 29.1 | 1.9 | 6,730 | 0.4% |
| 2022 | 700.3 | 450.0 | 175.0 | 185.5 | 221.6 | 552.4 | 8,914 | 2.5% |
| 2023 | 1,344.1 | 606.7 | 218.8 | 659.1 | 708.3 | 234.7 | 8,800 | 8.0% |
| 2024 | 899.7 | 324.3 | 280.4 | 495.8 | 533.6 | 0 | 7,926 | 6.7% |
| 2025 | 715.1 | 402.8 | 285.9 | 284.6 | 323.6 | 0 | 7,799 | 4.2% |

FY2016 (owner cash 454.4 all-equity, 12.6% of sales) is left out of the base: its operating cash includes the businesses
sold in FY2016 and FY2017, which the restated sales exclude. The FY2022 sale of plant and land ($315.1M proceeds) is not
owner cash and is left out. Net purchases are purchases of businesses less proceeds from businesses and equity investments
sold (FY2017 $163.4M, FY2018 $75.5M).

*The specifics, as applied.*
(a) **Cycle.** The literal window is FY2021 to FY2025. Its first year is aberrational on the filer's own description: FY2021
operating cash fell to $228.5M on "a $651.2 million year-over-year net increase in cash used by operating assets and
liabilities", a result "of rising volumes and values of inventory and average selling prices" (FY2021 10-K); the release came
in FY2023 ("a decreased scrap price environment", FY2023 10-K). The base is therefore the last full cycle, FY2017 (the lowest
earnings of the ten years read, $46.3M) to FY2025 (the low after the FY2022 peak, North America "metal margin compression"):
nine years, **all-equity owner cash before purchases $297.7M a year; net purchases $147.8M a year; after purchases
$149.9M**. The literal window beside: $363.3M before purchases, $157.8M of purchases.
(b) **Growth.** The series changes sign (FY2017, and FY2021 on the equity basis), so growth is measured between the halves of
the cycle, FY2017 to FY2020 against FY2022 to FY2025: owner cash before purchases $215.7M to $446.8M, **15.7% a year**. In
the literal window the halves change sign as well, so the literal window is shown at no growth alone, said so.
(c) **Acquisitions.** Net purchases over the cycle ($1,330M) are just under half of owner cash before purchases ($2,679M), so
CMC is not a serial acquirer by the convention over the window, and the default pair applies: purchases deducted, total
growth credited. CMC reports no organic growth rate, so the organic pair beside is the no-growth case. **Deals closed after
the window:** CP&P ($675M, closed 2025-12-01) and Foley ($1.84B, closed 2025-12-15), both paid in cash, so both
acquisitions, not mergers. Foley is valued on its own filed record (audited FY2024, 8-K/A 0001193125-26-059507): operating
cash $146.7M, plus cash interest $26.6M, less capital spending $9.1M and stock pay $2.9M, $161.3M before tax, **$123.2M after
tax at 23.6%** (Foley was a pass-through LLC and paid no entity tax), carried at no growth (one year filed). CP&P has no filed
earnings and is credited at nothing. The financing of both is inside net debt at 2026-05-31.
(d) **Working capital** is inside operating cash in every year, so its builds and releases are charged.
(e) **Growth spending.** The filings read state no maintenance figure and do not split the micro-mill spending by year (the
FY2025 10-K gives only the fourth mill's total, "$550.0 million and $600.0 million, net", and FY2026 capital spending of
about $600 million "driven by" it), so the central case charges all spending; the depreciation variant is beside. CMC's own
risk factor ("regular, substantial capital investments in our steel mills to maintain the mills, lower production costs and
remain competitive") argues that much of the spending above depreciation is the price of standing still.
(f) **The cap.** 15.7% carried ten years gives owner cash of about $1,280M, 16.4% of FY2025 sales, above the highest share
the business earned in the years read (12.6% in FY2016, 11.0% in FY2020); so the rate is cut to the business's own sales
growth between the same halves, 11.1%, and that is above the discount rate, so **the rate carried is 5.6%**. Both the shown
rate and the cut are written down here.

*Net debt, latest filed date (10-Q, 2026-05-31, Note 8):* total debt at face $3,428.9M (including finance leases $192.0M)
less cash and restricted cash $563.2M = **$2,865.7M**. **CONVENTION of this run:** the accrued antitrust loss ($373.5M, a
current liability awaiting the appeal) is added to net debt after the tax deduction its payment would bring, at 23.6%,
$285.3M, for **$3,151.0M**; the figures without it are shown beside. Rationale: it is a stated cash obligation of the
company, not yet in any year's operating cash. Operating leases are left out.

| case (all-equity, central) | value of the business at 5.60% | per share, less net debt and litigation | per share, less net debt only |
|---|---|---|---|
| no growth, before purchases (bottom) | $7,517M | **$39.46** | $42.04 |
| shown growth, cut to 5.6% for ten years, purchases deducted, then no growth on owner cash before purchases (top) | $9,016M | **$53.01** | $55.59 |

**VALUE RANGE: $39.46 to $53.01 a share against $64.77** (all-equity, central). The top is 1.34 times the bottom.
**The floor is tested first:** the market value of the business at the price is $7,165M plus $3,151M = $10,316M; the top
case returns 5.0% a year at that price, below the floor of about ten percent **[M2003-149]**; no case in the range earns the
floor at the price, and a price above the top closes OUT by the floor convention, whatever the width. As a computation, Q7
would close OUT. Beside: the literal window FY2021 to FY2025 at no growth alone, $50.05 a share; the depreciation variant
(capital spending equal to D&A), $56.91 to $80.23 at 5.60%, whose top alone would exceed the price; the equity-only basis
(cycle owner cash plus Foley less today's interest run-rate, $185M a year from the Q3 FY2026 10-Q including capitalized
interest, after tax), $42.57 to $54.50.

**FAIR PRICE (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent instead of 5.60%, the two
averaged. **All-equity, central: $10.51 a share** (the two ends at ten percent: $9.57 and $11.45, after net debt and the
litigation; $13.09 without the litigation). **Equity-only, beside: $23.27 a share** (ends $22.71 and $23.82). Tax: the
company's own tax throughout, no conversion. The all-equity figure is far below the equity-only one because $2.9 billion of
net debt at an average coupon near 5% costs the owner less a year than ten percent of its principal; the all-equity basis
charges the debt at its principal, as the speakers "evaluate acquisitions on an all-equity basis" **[L2017-004]**. No cheap
price is reported.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
- NOT REACHED.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
- NOT REACHED. Facts found are under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
- NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
- NOT REACHED. No business the rows name (casinos, tobacco, loading schemes) is among CMC's; the antitrust facts are
  recorded under Q5 below.

---
## THE BOX
**OUT at Q2** (the castle shown open on the evidence: North America Steel Group, the deciding part, sells a commodity on the
bid, priced by imports and tariffs, with a cost position a larger rival is buying in its markets for $440 million a mill and no
filing showing CMC the low-cost producer). **Integrity facts recorded, not judged** (an antitrust jury verdict against CMC,
$110.0 million trebled, plus fees and interest, on appeal; the compensation committee's neutralizing of that charge in the
annual bonus). COMPUTATION, NOT A CLEARANCE: value range $39.46 to $53.01 a share against $64.77, no case earning the floor at
the price; fair price $10.51 all-equity, $23.27 equity-only.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts found before and after the stop that bear on later questions, written down, not weighed **[M1997-127]**; no verdict;
the box unchanged (operator rule 2).

**Q3 (capital).** Capital spending exceeded depreciation in every fiscal year FY2017 to FY2025 except FY2019 (138.8 against
158.7), and averaged $298.0M a year against D&A of $189.9M over the nine years; FY2026 spending is "approximately $600
million" (FY2025 10-K). FY2022 brought $315.1M of proceeds from plant and land sold; the FY2025 10-K exhibit list includes a
purchase and sale agreement of 2021-09-29 with TAMCO and CMC Steel Fabricators as sellers. Return on capital by the run's measure averaged 18.9% over 2016 to 2025: 8.0% and 14.7% in FY2017 and
FY2018, 47.2% at the FY2022 peak, 2.0% in FY2025 (8.8% before the litigation charge). The Foley price, $1.84B, against Foley's
FY2024 owner cash of $161.3M before tax is 8.8% before tax and 6.7% after CMC's tax, on one year of the seller's record.

**Q4 (the accounts and the habits).** The filer's segment measure and featured figures are EBITDA: "Adjusted EBITDA is used by
management to compare and evaluate" segments (10-K, Item 7), and in Q4 FY2025 "the Company modified its method of calculating
adjusted EBITDA to exclude the impact of unrealized gains and losses on undesignated commodity derivatives", recasting prior
periods. The earnings release of 2026-06-25 leads with "adjusted earnings" and "Core EBITDA", gives a quarterly outlook ("core
EBITDA is expected to increase sequentially"), and states a "Net leverage adjusted for acquisitions" that includes "$245
million of expected annualized EBITDA contribution from the precast business". The Investor Day release of 2026-08-05 sets
"FY29 mid-cycle financial targets" and defines "Free Cash Flow" as "consolidated core EBITDA less capital expenditures"
(before interest, tax, stock pay and working capital), and core EBITDA as excluding "non-cash stock-based compensation" and
"litigation expense". These are the habits the framework records at Q4 as a weighing against and carries to Q5: "The one
figure we regard as utter nonsense is the so-called EBITDA" **[M1998-086]**; a management that highlights "adjusted per-share
earnings" makes the speakers "nervous" **[L2016-006]**; "the scourge of earnings "guidance"" **[L2019-006]**. No tell in the
accounts themselves was found: receivables and inventory held their ratio to sales (Step 0).

**Q5 (integrity facts, recorded, not judged).** (1) Pacific Steel Group sued on 2020-10-30 alleging that CMC "violated the
federal and California state antitrust laws and California common law by entering into an exclusivity agreement for certain
steel mill equipment manufactured by one of our equipment suppliers"; on 2024-11-05 "a jury returned a verdict in favor of PSG
in the amount of $110.0 million", trebled by the court; the motion for a new trial was denied on 2025-09-29; CMC filed its
notice of appeal on 2025-10-24; CMC says "We are confident we conducted our business appropriately" (10-K Item 3; 10-Q Note
14). (2) A second PSG suit alleges CMC units bid "below their costs for rebar furnish-and-install projects in California to
hamper PSG's ability to win jobs"; summary judgment was denied on 2025-09-29; no trial date; no liability recorded.
(3) The proxy (0001193125-25-294507): "the Compensation Committee approved an adjustment to neutralize the impact related to
the judgment in the previously disclosed Pacific Steel Group litigation", because "the inclusion of the charge would not be
reflective of the Company's strong financial performance in fiscal year 2025". (4) The chief executive since 2023-09-01,
Peter Matt, came from Constellium and Credit Suisse; the conduct alleged in the first suit predates the suit (filed 2020).
Any later run that reaches Q5 must answer these: "If you’ve got doubts, forget it." **[M2013-088]**; the speakers look at
"things that they do in public in relation to their investors and the promises they make" **[M2004-067]**.

**Q6 (the money and the owners).** Buybacks: FY2023 $101.4M (2,309,452 shares, about $43.91), FY2024 $182.9M, FY2025 $198.8M
(Q4 FY2025 at $46.54, $52.14 and $55.00 by month), nine months of FY2026 $76.4M (1,195,709 shares, about $63.90). The program
names no price; the 2026-08-05 increase of $600M "reflects our confidence in the strength of our business", with timing "based
on its evaluation of market conditions, capital allocation alternatives and other factors" (0001193125-26-333797). Every
average price found sits above the bottom of the computed range, $39.46; by Q6's tested reading a program with no stated price
then weighs against **[L2016-002]**, and the stated motive is the one the speakers name, to "show confidence"
**[L1999-028]**. The precast purchases (about $2.5B in cash, December 2025) lifted goodwill and intangibles to 57% of equity;
they were paid in cash, so Q6's all-stock STOP does not apply. Pay: the performance units pay on "Cumulative Adjusted EBITDA
(Comp)" and relative total stockholder return, whose weight rises "from 25% of the PSU mix to 50%" (proxy); the bonus
adjustment in Q5 (3) is to be read against "heads I win, tails you lose" **[L1994-020]**. Retained earnings rose from $1,364M
(FY2017) to $4,888M (2026-05-31) while the diluted share count fell from about 117 million to 112 million; whether each
dollar kept became more than a dollar of value was not tested.

**Q9 (debt and exposures).** Total debt $3,428.9M at 2026-05-31 against $1,364.1M nine months earlier; $2,000M of it the
5.75% notes due 2033 and 6.00% notes due 2035; covenants "including interest coverage and debt to capitalization ratios", in
compliance at 2026-05-31 (10-Q Note 8). Interest expense ran $40.2M in the quarter to 2026-05-31 against $10.9M a year
earlier. The antitrust liability, $373.5M, is payable if the appeal fails: "the cash payments incurred in connection with this
litigation could have a significant impact on our liquidity" (10-Q, Item 2). Against the debt, the cycle's all-equity owner
cash ran about $298M a year plus Foley's $123M; "you can’t talk about debt levels without relating it to the ability to pay
debt" **[M1995-104]**. For a whole business offered, the criterion is "little or no debt" **[R1997-001]**; this is a
part-interest, where the criterion is not stated.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 5b26f82a); written question by question; committed after each
      (write-early).
- [ ] If dispatched: the brief allowed the per-question commits (it did); the lock and the fold are the dispatching
      session's (operator rule ten); this run is not in the register until folded, and until then binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One listing of `Test Runs/` filtered on
      the date showed other runs' file names, and the harness's commit subjects showed an STLD run's results; both are
      declared under contamination at the top and not used.
- [x] Every v5 id resolves (`scripts/check_run.py` in the research folder: every M, L and R id found in
      `principle_ledger_v5.csv`, every quoted fragment beside an id found in that row, no E-id); every filing fact carries its
      document and accession; numbers are from filings or labelled CONVENTION.
- [x] The order was kept; Q2's STOP closed the run; everything after it is a fact recorded or a COMPUTATION, not a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the US Treasury,
      dated 2026-10-09; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (THE FOUNDATIONS, four items; Q2's caveats on the competitor row); the facts
      for later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor is cited (not a point-in-time run; today's date is the anchor).
- [x] Only the arithmetic lines of `tools/run.py` were used; its yield lines and window were not.
- [x] `python tools/check_framework.py` PASS before the final commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. **(1) The commodity paragraph's routing and the money test pull apart.** Q2's commodity paragraph says that
where the cost position decides and no filing states it, the file is TOO HARD (NATURE); no filing read states a rebar cost
per ton, for CMC or any rival. But the castle tests also include the money test, and here it is answered by a rival's filed
capital budget. This run held that the money test, the bid, and the price set by imports show the castle open whatever the
unstated cost figure, and closed OUT; another analyst could read the same facts as TOO HARD (NATURE). The paragraph does not
say whether its cost routing governs when another castle test already shows the castle open; a sentence saying which governs
would settle it. **(2) The cap in specific (f) does not say which sales the year-ten owner cash is compared with.** Against
sales grown at the business's own sales growth, CMC's 15.7% never trips the test (sales compound too); against today's sales
it does. The run compared with FY2025 sales and said so. **(3) The serial-acquirer threshold sits on a knife edge** for a
company whose largest purchases fall just after the window: CMC's net purchases over the cycle were 49.7% of owner cash
before purchases, under the half that would make the organic pair central, while the $2.5 billion of precast purchases closed
two months after the window. The convention values the late deals on their own record, which the run did. **(4) The two
bases of the fair price can differ by more than two to one** for a newly indebted company ($10.51 all-equity against $23.27
equity-only here), and the framework names the all-equity figure central without saying how a reader of the alert should
treat a gap that size.
