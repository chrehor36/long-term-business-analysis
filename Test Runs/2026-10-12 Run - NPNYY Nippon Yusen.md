# Company Run: Nippon Yusen Kabushiki Kaisha, NYK Line (TSE: 9101; US OTC ADR: NPNYY), 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker; not held.*

**CONTAMINATION, declared before any fetch:** (1) a directory search for this run's own paths listed the file name
`Test Runs/2026-07-15 Run - NPNYY (Nippon Yusen KK).md`; it was not opened and nothing of it is known or used beyond its
existence. (2) The session header showed recent commit subjects about another company's v5 re-run (SSUMY, Sumitomo
Corporation, closed TOO HARD (WORK) at Q2); not used. (3) The project memory index carries general queue lines (counts of
gate-clearers, a paused wave); nothing about this name, not used.

**Departures from the canonical brief, as the dispatch states them:** the lines of evidence are derived by the analyst from
the company's own annual report; the primary document is the company's own annual securities report and integrated report,
since the company files no annual report with the SEC.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** ¥7,358 per Tokyo share, close of 2026-10-09 (Friday; 2026-10-12 is a Japanese holiday and the Tokyo market
  was closed), Yahoo Finance chart API, **aggregator, flagged** (operator rule 5). The ADR NPNYY closed $9.33 the same day
  (aggregator). ADS ratio from the company's own ADR page (`www.nyk.com/english/ir/stock/adr/`, read 2026-10-12):
  **5 ADRs : 1 ordinary share**, so one ADS is 0.2 share; depositary Bank of New York Mellon, CUSIP 654633304, OTC.
  Check: ¥7,358 × 0.2 ÷ ¥158.06 per $ (Yahoo USD/JPY close 2026-10-08, aggregator) = $9.31 against $9.33 quoted. The ratio holds.
- **Share changes checked from the company's own documents:** a 1-for-10 reverse split on October 1, 2017 and a 3-for-1 split
  on October 1, 2022 (IR Data Book 2026, note 3 to the indicators table); cancellations of treasury shares of 25,321,600 on
  2026-03-25 and 3,458,300 on 2026-05-29 (TSE notice "Notice Regarding Results and Completion of Stock Acquisition, and
  Retirement of Own Stock", May 7, 2026). No merger paid in NYK shares and no spin-off found in the documents read. Nippon
  Cargo Airlines left the group by a share exchange with ANA Holdings effective August 1, 2025 (NYK issued no shares; it
  received ANA shares); Movianto International B.V. was bought for cash in the year to March 2026.
- **Shares:** issued 405,321,700 less treasury 1,766,082 = **403,555,618** outstanding at June 30, 2026 ("Consolidated
  Financial Results for Three Months Ended June 30, 2026", TSE, August 5, 2026, item 4(4)); at March 31, 2026 the figures were
  408,780,000 issued less 3,288,388 treasury ("Consolidated Financial Results for the Year Ended March 31, 2026", TSE, May 11,
  2026). The IR news list (read 2026-10-12) shows no buyback, issue or cancellation announced after August 5, 2026, and the
  company's stock page gives 405,321,700 issued, agreeing.
- **Market cap:** 403,555,618 × ¥7,358 = **¥2,969.4bn** ($18.79bn at ¥158.06).
- **Sovereign for the earnings currency (yen):** **4.085%**, the 30-year JGB, 2026-10-09, Japan Ministry of Finance
  `jgbcme.csv` (issuing authority; `tools/sources.py` returned 4.136% for 2026-10-08 from the same file).
- **Filings read** (operator rule 4; the company has no SEC periodic filings, so its own documents are primary; title and date
  stand in place of an accession number):
  - "Financial Results 2026, Year Ended March 31, 2026" (audited English consolidated statements, NYK IR library), and the
    same series for the years to March 2018, 2019, 2021, 2022, 2023 and 2025 (balance sheets and the antitrust notes).
  - "Consolidated Financial Results for the Year Ended March 31, 2026" (TSE tanshin, May 11, 2026), and the first-quarter
    tanshin of August 5, 2026 (balance sheet and interest-bearing debt at June 30, 2026).
  - "IR Data Book 2026" (May 11, 2026): eleven years of statements, segments and cash flows, years to March 2016-2026.
  - "NYK FACT BOOK 2018" (Fact Book II): cash flows for the years to March 2008-2018.
  - "NYK Report 2025" (integrated report, November 2025): business and segment description, liner strategy, risks.
  - "IR Fact book 2025" (October 2025): competitor fleet table, the ONE 2030 plan, the medium-term plan.
  - Briefing materials of May 26 2020, May 9 2022, May 8 2024 and May 11 2026, each carrying Ocean Network Express's own
    annual results pages (ONE's "Financial Results" decks, reproduced inside NYK's briefings).
  - TSE notices: revision of forecasts (July 30, 2026); revision of the dividend forecast (August 5, 2026); the scheduled
    tender offer for NS United Kaiun (July 31, 2026); the DGMO third-party allotment (July 30, 2026); buyback completion and
    retirement (May 7, 2026).
  - Not read: the Japanese-language annual securities report (yuho) on EDINET, the corporate governance report and the notice
    of the June 2026 general meeting (the file closed before Q5 and Q6; listed under what could not be got).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities, year to March 2026,
  ¥473,358m in the IR Data Book 2026, page 6 = ¥473,358m in the audited consolidated statement of cash flows, Financial
  Results 2026, page 6. Total assets ¥5,201,670m also agree.
- `python tools/run.py NPNYY`: "not an SEC filer ... UNRESEARCHED, not UNKNOWABLE"; `python Screens/cover_shares.py NPNYY`:
  "NOT AN SEC REGISTRANT". Both expected; every figure below is from the company's documents. The arithmetic is in
  `Test Runs/_research 2026-10-12 NPNYY/compute.py`, with its output in `compute_out.txt` beside it.
- **Owner cash after every real cost** (¥bn, years to March 31): operating cash flow, which already carries tax paid,
  interest paid, the change in working capital and the dividends received from equity-method affiliates; less purchases of
  vessels, property, plant, equipment and intangibles; less repayment of lease liabilities; less cash paid for subsidiaries
  net of subsidiaries sold. Vessel-sale proceeds and the depreciation variant are shown beside, not used.

  | YE Mar | OCF | capex | lease | net acq. | **owner cash** | with vessel-sale proceeds | D&A variant |
  |---|---|---|---|---|---|---|---|
  | 2016 | 142.9 | 115.9 | 0.0 | -9.4 | **36.4** | 110.5 | 48.9 |
  | 2017 | 27.9 | 156.2 | 0.0 | 2.3 | **-130.6** | -100.0 | -66.3 |
  | 2018 | 89.1 | 199.2 | 0.0 | 8.3 | **-118.5** | -47.5 | -7.1 |
  | 2019 | 45.3 | 169.6 | 2.4 | -7.7 | **-119.0** | -33.7 | -39.1 |
  | 2020 | 116.9 | 138.8 | 19.3 | 0.0 | **-41.2** | 29.7 | -6.4 |
  | 2021 | 159.3 | 102.1 | 19.9 | -2.1 | **39.4** | 115.4 | 42.7 |
  | 2022 | 507.8 | 192.7 | 20.4 | -36.0 | **330.6** | 366.0 | 421.7 |
  | 2023 | 824.9 | 198.4 | 24.2 | 12.9 | **589.4** | 618.4 | 666.1 |
  | 2024 | 401.4 | 336.3 | 27.0 | -4.0 | **42.1** | 121.9 | 236.8 |
  | 2025 | 510.8 | 206.5 | 26.0 | -85.8 | **364.1** | 452.5 | 416.0 |
  | 2026 | 473.4 | 304.5 | 29.4 | 263.1 | **-123.6** | -41.3 | 5.7 |

  Five-year literal average (YE Mar 2022-2026): ¥240.5bn. For YE Mar 2008-2015 (Fact Book 2018), owner cash on the same
  definition was negative in every year, from -¥301.9bn to -¥55.2bn; the nineteen years YE Mar 2008-2026 sum to
  **-¥637.9bn** (+¥1,619.5bn if every vessel-sale proceed is credited). Stock pay is immaterial (a share-delivery trust;
  provision for stock payment ¥0.3bn at March 2026).

### The balance sheets, ten years, before the income account [M2025-032]
*(Read here because the file closes before Q4.)* ¥bn at March 31 (IR Data Book 2026 items 9 to 12; cash from its cash-flow
page; the other lines from the filed balance sheets of the Financial Results series; n.r. = not read):

| Mar 31 | total assets | shareholders' equity | interest-bearing debt | cash eq. | investment securities | goodwill | retained earnings |
|---|---|---|---|---|---|---|---|
| 2017 | 2,044 | 522 | 945 | 137 | 410 | 18.6 | 202 |
| 2018 | 2,072 | 552 | 983 | 103 | 423 | 22.0 | 345 |
| 2019 | 2,002 | 487 | 1,046 | 78 | 479 | 16.4 | 294 |
| 2020 | 1,933 | 463 | 1,050 | 77 | 449 | 11.1 | 312 |
| 2021 | 2,125 | 625 | 951 | 104 | 579 | 10.2 | 445 |
| 2022 | 3,080 | 1,714 | 808 | 227 | 1,146 | 8.7 | 1,396 |
| 2023 | 3,777 | 2,479 | 694 | 196 | 1,688 | 13.7 | 2,019 |
| 2024 | 4,255 | 2,650 | 914 | 145 | 1,813 | 27.7 | n.r. |
| 2025 | 4,320 | 2,919 | 738 | 150 | 1,993 | 22.9 | 2,298 |
| 2026 | 5,202 | 3,072 | 1,201 | 211 | 1,975 | 250.6 | 2,118 |
| Jun 30 2026 | 5,397 | 3,115 | 1,362 | 226 (deposits) | 2,023 | 246.1 | n.r. |

What the figures say: until March 2021 this was a thin, levered balance sheet (equity ratio 24% to 29%, debt-equity 1.5 to
2.3 times), and the year to March 2017 took a ¥265.7bn net loss with ¥168.1bn of impairments, a third of equity. What came
after is the container windfall of 2020-2023, held mostly in the equity-method affiliate: investment securities rose by
¥1.5 trillion (chiefly the ONE stake) and retained earnings by ¥1.7 trillion in three years. What they do not say: the equity
gain was not made by the consolidated fleet. Receivables rose from 11.5% of revenue (March 2020) to 16.4% (March 2026, with
Movianto consolidated); inventories, mainly fuel, from ¥32.5bn to ¥72.6bn. Since March 2023 debt has nearly doubled
(¥694bn to ¥1,362bn at June 30, 2026, leases of ¥248bn included) while the company paid for buybacks (¥200bn, ¥125bn and
¥144bn in the three years to March 2026), a ¥390bn dividend in the year to March 2023, the cash purchase of Movianto (¥263bn,
goodwill up ¥228bn) and a capex step-up to ¥305bn. Operating leases (chartered-in ships) are not in the debt figures; a
residual value guarantee of ¥29.7bn on leased vessels sits in the contingencies note.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this if the market closed for years **[M1997-109]**,
which for a shipping group means owning the freight cycle itself, not the next quote. The market serves and does not
instruct **[M2006-077]**: the quote has risen several-fold with the container windfall and says nothing of value by itself.
No macro forecast enters **[M2000-094]**, and that cuts hard here, because the company's own explanations of its results are
almost all macro (the Red Sea, tariffs, the Strait of Hormuz, the yen, bunker prices); what counts instead is "the average
profitability of the business over time" **[M2015-016]**. The analyst's habit applied: I am looking "for what’s wrong in
things" **[M2025-013]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) for Q1, the company's own one-year forecast moved by a
third in eleven weeks (recurring profit ¥185bn on May 11, 2026, ¥250bn on July 30, 2026), so the key variable is not
foreseeable even one year out by the insiders; (2) for Q2, ONE's full-cycle return on its founding capital was very high
(profits of $40.3bn over FY2018-FY2025), which runs against any reading that the field earns only ordinary returns and has to
be explained, not ignored; (3) for Q3, owner cash was negative in every year from March 2008 to March 2020 but one, and over
nineteen years is negative in sum; (4) the company's own note records "its conspiracy to fix prices of shipping with major
automobile shipping companies" (an integrity fact for Q5).

## THE STANDING RULE
The buyer's rule: a part-interest bought with the buyer's own money, and sized so that a fall of half or more is borne without
a forced sale, puts nothing the buyer has and needs at risk **[M2012-081]**; borrowed money to hold a stock this volatile is
what the rows name as the way to be prevented from "playing out your hand" **[M2004-065]**. Nothing in this business changes
that; the target's own debt is Q9's and is recorded under AFTER THE STOP.

---
### The lines of evidence, and where they were derived
Derived from the NYK Report 2025 (business and segment description, the liner and logistics growth strategy, "Past changes in
business environment"), the segment note and "Overview by Business Segment" of the May 11, 2026 tanshin (the equivalent of
Item 7), the risk and outlook statements in the tanshin, the briefing materials and the forecast revisions (the equivalent of
Item 1A; the yuho's own business-risk section was not read), and the contingencies notes of the Financial Results series.
Lines chosen: (1) the parts and their share of five-year segment profit; (2) ONE's own results, liftings, freight and margins
over FY2018-FY2025, and what NYK can and cannot see of ONE (equity method; dividends received); (3) pricing through the
2020-2022 spike and the collapse after, and the forecast record; (4) fleet spending against depreciation over nineteen years
and its financing; (5) acquisitions (Movianto, NS United Kaiun, DGMO) and goodwill; (6) debt and leases; (7) buybacks and
their prices; (8) the car-carrier price-fixing investigations and class actions; (9) the one SEC-filing liner rival's record.

## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The parts that matter** (Q1's holding-company paragraph, with Q2's threshold). Segment profit as the filer reports it
  (recurring profit, the only segment profit measure in its filings), years to March 2022-2026, of a consolidated
  ¥3,076.3bn: **Liner Trade ¥1,916.9bn, 62.3%**; Automotive, Dry Bulk and Energy (one "Bulk Shipping" segment until the year
  to March 2024) ¥859.4bn, 27.9%; Air Cargo ¥164.6bn, 5.4% (passed to ANA by share exchange, August 2025); Logistics
  ¥170.4bn, 5.5%; Others ¥13.4bn; eliminations -¥48.5bn (IR Data Book 2026, page 4). The part that matters is Liner Trade,
  and Liner Trade is in substance Ocean Network Express (ONE), the 38% equity-method affiliate formed in 2018 from the
  container businesses of NYK, MOL and K Line. Counted by cash received instead (the framework's equity-method convention),
  the result is the same: interest and dividends received were ¥1,331.6bn over the same five years, against ¥42.0bn in the
  year to March 2021, the difference being ONE's dividends.
- **What the business is.** ONE carries containers on scheduled services. It is sixth of the world's carriers by fleet,
  2,005,871 TEU and 6.4% of capacity at April 30, 2025, against MSC 6,502,429 TEU (20.7%), Maersk 14.3%, CMA CGM 12.4%,
  COSCO 10.5% and Hapag-Lloyd 7.6% (IR Fact book 2025, page 16); its fleet was 2,231,703 TEU at March 31, 2026 with 67 ships
  on order (ONE results deck in the NYK briefing of May 11, 2026).
- **The key variables and whether they are foreseeable** **[M1998-044]**: liftings (12.1m TEU in FY2021, 12.9m in FY2025;
  steady) and the freight rate against the cost of the fleet (wildly unsteady: ONE's revenue went from $10.9bn in FY2018 to
  $30.1bn in FY2021 and back to $16.6bn in FY2025 on nearly the same liftings). The freight rate is set by the supply of ships
  against demand: ONE's own FY2025 analysis gives "Freight Decreased due to softer supply-demand balance" and names newbuild
  deliveries that "increased market supply". It is not foreseeable: NYK's forecast of recurring profit for the year to March
  2027 went from ¥185bn (May 11, 2026) to ¥250bn (July 30, 2026), explained by "container freight market conditions [that]
  have continued to outperform our initial assumptions" (TSE notice, July 30, 2026).
- **The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**. The freight rate of 2036 cannot be fixed; but the definition asks for the
  economics, and the economic dynamics of this industry can be stated from the filings with confidence. What matters is "are
  there competitive moats? Is there ease of entry?" **[M2011-014]**, and the documents answer: entry is open to anyone with
  money to order ships, and the largest carrier became the largest by ordering them; the product is a commodity; ONE is a
  mid-sized price-taker that NYK's own report says "has been working to close the fleet scale gap with its major competitors"
  (NYK Report 2025, Liner & Logistics). That is a fix on the competitive position and on the kind of earning power (the
  commodity's cycle average), and Q2 then tests it. The industry is not one of rapid technological change (the box ship is
  seventy years old), so the routing rule for change **[M1998-008]** does not send it to TOO HARD here.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. My doubt is
  about the year's price, not about the economics: I hold no doubt that this is a commodity business whose returns are set
  by its field. A narrower reading is open and is carried to WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR: that the
  unforeseeable key variable alone ("If something is not very predictable, forget it." **[M1998-044]**) closes the file here
  TOO HARD (NATURE).
- **The other parts** (not deciding): car carriers, dry bulk and tankers are ship-operating businesses of the same commodity
  kind; LNG carriers and FPSOs earn on "medium- to long-term contracts that generate stable earnings" (tanshin, May 11, 2026);
  logistics is forwarding and contract logistics. All are understood in the same sense; none decides.
- **VERDICT: IN**, narrowly, on the economics of the deciding part (Liner Trade through ONE): a commodity carrier whose
  competitive position and kind of earning power can be stated, though its ten-year freight rate cannot; Q2 decides whether
  that matters **[M2012-065]**, **[M2011-014]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (Q2's business of parts; segment recurring profit, the filer's segment measure, years to March 2022-2026,
IR Data Book 2026, page 4; a part decides at more than half of five-year profit):

| part | five-year segment profit | share | castle, in one line | decides |
|---|---|---|---|---|
| Liner Trade (ONE, 38%, equity method; terminals) | ¥1,916.9bn | 62.3% | commodity carrier, price set by the field (below) | **yes** |
| Automotive (car carriers, auto logistics) | ¥317.2bn (3 years only) | inside 27.9% | ship operator in a field whose leaders, NYK included, were found fixing prices | no |
| Dry Bulk | ¥45.7bn (3 years only) | inside 27.9% | commodity tramp shipping | no |
| Energy (tankers, LNG carriers, FPSO) | ¥147.0bn (3 years only) | inside 27.9% | part spot (VLCC, VLGC), part long-term contracts (LNG) | no |
| Air Cargo (NCA, gone August 2025) | ¥164.6bn | 5.4% | sold | no |
| Logistics (Yusen Logistics, Movianto) | ¥170.4bn | 5.5% | forwarding and contract logistics | no |
| Others, eliminations | -¥35.1bn | -1.1% | | no |

The file closes on the deciding part, Liner Trade, which is ONE.

**The castle tests, each with its filing fact:**
- **The castle questions: what keeps it standing, and how permanent?** **[M1995-038]**, and why would a shipper use ONE rather
  than the carrier it already uses **[M1998-147]**? No document read names a reason other than price, schedule and network.
  NYK's own account of the field is "Excessive competition among containership operators", answered by "Establishment of ONE
  to integrate container shipping businesses of three Japanese operators" and "Scaling up" (NYK Report 2025, Liner &
  Logistics, "Past changes in business environment"). Merging three carriers that were losing money to reach the scale of
  the leaders is a defence against the field, not a castle within it.
- **The attacker with money** **[M2011-015]**: the answer is yes, and the filings show it being done. MSC is first with
  6.5m TEU, more than three times ONE's 2.0m (IR Fact book 2025, page 16). ONE's own plan is the same act: "Invest over US$25
  billion in the Container Shipping Business" to reach "Fleet scale of 3 million TEU by FY2030" (IR Fact book 2025, ONE 2030).
  Supply follows money: "the continued delivery of newbuild vessels increased market supply" (ONE FY2025 results). An
  industry where capacity is bought by whoever has the money is one of those "that are just never going to have barriers to
  entry" **[M2012-106]**; Munger's line on airlines fits the ship: "you can create another airline" **[M2013-054]**.
- **Pricing power and the agony before a rise** **[M2005-020]**: none. ONE's revenue went from $10.9bn (FY2018) to $30.1bn
  (FY2021) and back to $16.6bn (FY2025) on liftings of 12.0m to 12.9m TEU a year (FY2020-FY2025); its FY2025 profit analysis lists "Freight:
  Decreased due to softer supply-demand balance". The price is the field's, not ONE's: "whatever he charged for gas was my
  price" **[M2012-109]**; "he determined our profit, because we looked at his price every day" **[M2023-079]**.
- **Would the customer still choose it over the low bid?** **[M2017-009]**: the product is a slot on a ship; a shipper with
  two carriers on the same lane takes the cheaper one, as "most insureds don't care from whom they buy" **[L2004-003]**. No
  filing read claims a premium price. "Buy commodities, sell brands" **[L2011-008]**: ONE sells the commodity.
- **The low-cost position, the one exception for a commodity** **[L2004-007]**, **[L2000-017]**, **[M1997-010]**: no document
  read claims that ONE is the low-cost carrier, and NYK's own report concedes the opposite on scale ("close the fleet scale
  gap with its major competitors"). The competitor row below shows ONE neither clearly cheaper nor clearly dearer than the one
  SEC-filing rival: better in the 2023 trough, worse in 2025. The exception asks for the low-cost operator; on the evidence
  ONE is an average one, and "Average is going be terrible [...] And if you are average, you’re going to have a very poor
  business" **[M2000-072]**.
- **Unit volume and share of mind:** liftings are steady (12.1m TEU FY2021, 12.9m FY2025); share of capacity 6.4%. Volume
  holds; the price does not, which is the commodity's mark.
- **Ask the competitors** **[M1999-130]**: not possible from the public record beyond the rivals' own accounts; the row below
  stands for it.
- **Widening or narrowing** **[M1999-108]**: the scale gap to the leaders is the company's own admission; ONE 2030 is a plan to
  narrow it by spending $25bn, the same spending every rival can make. Every improvement goes to the customer: "the
  improvement you get one day, your competitor gets the next day" **[M2004-053]**.
- **What could destroy, modify or reduce it** **[M2000-014]**: newbuild deliveries, the reopening of the Suez route (ONE calls the
  prospect of resuming the Red Sea and Suez Canal passage "even more uncertain"; a reopening releases the capacity now
  absorbed by the detour round the Cape), and tariffs (NYK Report 2025: "If retaliatory tariffs are implemented, there
  is a strong possibility that the market will take a new downturn"). Each is a change in the field's price that ONE takes.

**The competitor row** (same metric: operating profit, or EBIT, over revenue, US$m; ONE from its own results pages in NYK's
briefings of May 2020, May 2022, May 2024 and May 2026, fiscal years April to March; ZIM Integrated Shipping Services from
its 20-F filings with the SEC, calendar years: 2025, 2024 and 2023 from accession 0001178913-26-000784 filed 2026-03-09, 2022
from 0001178913-25-000793, 2021 from 0001178913-24-000920, 2020 from 0001178913-23-000936, 2019 from 0001410578-22-000304,
2018 from 0001104659-21-039375):

| year | ONE revenue | ONE EBIT (margin) | ONE profit | ZIM revenue | ZIM operating income (margin) | ZIM equity, year end |
|---|---|---|---|---|---|---|
| 2018 | 10,880 | n.r. | -586 | 3,248 | -23 (-0.7%) | -224 |
| 2019 | 11,865 | n.r. | 105 | 3,300 | 153 (4.6%) | -252 |
| 2020 | 14,397 | 3,832 (26.6%) | 3,484 | 3,992 | 722 (18.1%) | 274 |
| 2021 | 30,098 | 17,196 (57.1%) | 16,756 | 10,729 | 5,816 (54.2%) | 4,600 |
| 2022 | 29,282 | 15,005 (51.2%) | 14,997 | 12,562 | 6,136 (48.8%) | 5,896 |
| 2023 | 14,536 | 392 (2.7%) | 974 | 5,162 | -2,511 (-48.6%) | 2,458 |
| 2024 | 19,233 | 3,804 (19.8%) | 4,244 | 8,427 | 2,527 (30.0%) | 4,043 |
| 2025 | 16,620 | 310 (1.9%) | 338 | 6,904 | 1,016 (14.7%) | 4,026 |

Named rivals that do not file with the SEC, flagged and not read: MSC (private), A.P. Moller-Maersk, CMA CGM (private),
COSCO Shipping, Hapag-Lloyd, Evergreen, HMM, Yang Ming, Wan Hai and PIL (the IR Fact book 2025 fleet table names them). The
two co-owners of ONE, MOL and K Line, report the same ONE.

**The field's returns over the last full cycle, judged in words.** Before the pandemic the field earned nothing: NYK's own
liner segment made -¥0.3bn, -¥12.7bn and ¥10.9bn in the three years to March 2018 on revenue of ¥586bn to ¥706bn; ONE lost
$586m in its first year; ZIM had negative equity at the end of 2017, 2018 and 2019. Then a supply shock that NYK itself names
("recurring profit entered a sharp upward trend from 2020 onward due to the effects of turmoil in global logistics and higher
freight rates", NYK Report 2025) gave every carrier margins of 50% or more for two years, the rival that had been insolvent
on its balance sheet included. After it, the field fell straight back: ONE's EBIT margin 2.7% in FY2023 and 1.9% in FY2025,
ZIM an operating loss in 2023. Over the whole span the cumulative return is high, and that is the contrary evidence written
down in the foundations; but it was the field's price in a shock, earned equally by the strong and the weak, and a return
from "a cyclical peak in earnings" is what the rows tell the reader to rule out before crediting a business with its return
**[L1994-009]**. Nothing in it came from a castle: the industry factors overwhelmed any one carrier's strategy **[M2000-069]**.

**A change for the better?** The rows record industries that got good, "the railroads were a terrible business for decades
and decades and decades and then they got good" **[M2017-026]**, and container shipping consolidated between 2016 and 2018
(the ONE merger among others). Under Q2's change-for-the-better convention it is credited only on a full cycle in which the
price behaviour held. It did not hold: one fiscal year after the peak, ONE's EBIT margin was 2.7%, and in FY2025 it was 1.9%
with newbuilds still arriving. So no credit is given, and since the first downturn after the consolidation has already
answered the question, the file is not left TOO HARD (NATURE) on it.

**Why the box is OUT and not TOO HARD.** A castle whose future cannot be judged goes to TOO HARD; a castle shown open on the
evidence goes to OUT **[M2011-015]**, **[M2006-013]**. Here the evidence shows the ground on which a castle would have to
stand: a commodity sold to customers who take the low bid **[L2004-003]**, a price set by the field **[M2012-109]**,
capacity open to anyone with money **[M2012-106]**, and no claim or sign of the low-cost position that is the commodity's one
exception **[M1997-010]**, **[L2004-007]**. The rows' policy for that ground is plain: "We’re going to be investors in
businesses, not commodities, by and large." **[M2007-131]**. Price does not reopen it **[M2019-015]**.

The non-deciding parts are not weighed for the box. For the record: Automotive is the part with the highest five-year profit
after Liner Trade, and it is the part in which NYK's own note records the price-fixing conspiracy (AFTER THE STOP, Q5);
LNG carriers on long-term charters are the nearest thing to a protected return in the group, and they are not the deciding
part.

- **VERDICT: OUT**, on the deciding part: Liner Trade (ONE) is a commodity carrier whose price is set by the field, with no
  evidence of the low-cost position, and the full cycle shows the field's returns falling back to nothing after the shock
  **[M2012-109]**, **[L2004-003]**, **[M1997-010]**, **[M2012-106]**, **[L1994-009]**. The file closes here.

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (the file closed at Q2; facts found are under AFTER THE STOP).

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (balance sheets read in Step 0; facts found are under AFTER THE STOP).

## Q5 — WHO RUNS IT. NOT REACHED (integrity facts found are under AFTER THE STOP).

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED (facts found are under AFTER THE STOP).

## Q7 — WHAT IS IT WORTH. NOT REACHED as a question; the operator's two reporting figures are computed under AFTER THE STOP,
headed COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES. NOT REACHED.

## Q9 — COULD IT RUIN US. NOT REACHED (debt facts are under AFTER THE STOP).

## Q10 — IS IT THE FAT PITCH. NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE. NOT REACHED; none of the businesses the rows name.

---
## THE BOX
**OUT at Q2**: the deciding part, Liner Trade (Ocean Network Express, 62.3% of five-year segment profit), is a commodity
carrier whose price is set by the field, with no evidence of the low-cost position; the full cycle shows the field's returns
falling back to nothing after the 2020-2022 shock. Integrity facts recorded, not judged (the car-carrier price-fixing
investigations and class actions in the company's own contingencies note; see AFTER THE STOP, Q5). For the operator's
reporting figures (COMPUTATION, NOT A CLEARANCE): value range a single no-growth case of ¥2,291 a share (all-equity basis,
cycle base), fair price below zero on the all-equity basis (-¥705) and ¥1,803 on the equity-only basis, against ¥7,358.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box is unchanged (operator rule 2) **[M1997-127]**.*

**Q3 (capital in, earnings out).** Purchases of vessels and other fixed assets were ¥501bn, ¥418bn, ¥238bn, ¥279bn, ¥309bn and
¥307bn in the years to March 2008-2013 against depreciation of ¥92bn to ¥101bn; ¥102bn to ¥336bn a year in the years to March
2021-2026 against depreciation of ¥99bn to ¥175bn (Fact Book 2018; IR Data Book 2026). Owner cash on gross capex was negative
in every year to March 2008-2015 and 2017-2020, and sums to -¥637.9bn over the nineteen years to March 2026; with every
vessel-sale proceed credited it sums to +¥1,619.5bn, ¥85bn a year, most of it from the years to March 2022-2025. Fleet count
782 vessels (March 2016) to 684 (March 2026); deadweight 62.1m to 54.9m tonnes; capex nonetheless rose (LNG carriers, FPSOs,
car carriers for new fuels). ROIC as the company computes it: 3.6%, -15.1%, 3.1%, -0.2%, 3.7% in the years to March 2016-2020;
47.1%, 35.7% in 2022-2023; 6.4% in the year to March 2026 (IR Data Book 2026, item 35, a company measure that includes
equity-method earnings). ONE plans to invest over $25bn in container shipping by FY2030 with debt to equity "around 6:4" (IR
Fact book 2025, ONE 2030).

**Q4 (the numbers).** The IR Data Book features EBITDA and EV/EBITDA as rows 13 and 14 of the company's own indicators table.
Equity-method income was ¥742.6bn and ¥811.9bn in the years to March 2022 and 2023 and ¥85.0bn in the year to March 2026
(ONE ¥19.0bn of it); dividends and interest received were ¥288.1bn, ¥457.2bn and ¥225.5bn in the same years. ONE has its own
published results (in NYK's briefings) but its full statements were not read. Recorded once-off items: impairments of
¥168.1bn and an antitrust loss of ¥19.5bn in the year to March 2017; a provision for loss on contracts of ¥44.8bn the same
year and ¥35.5bn in the year to March 2019. The year to March 2026 carries a loss on share exchange of ¥7.1bn (Nippon Cargo
Airlines to ANA). The tax line is low (tonnage tax and the foreign dividend exclusion; normal statutory rate 28.8%), and
total income taxes were ¥61.1bn on a profit before tax of ¥276.8bn in the year to March 2026. The company's one-year forecast
of recurring profit moved from ¥185bn (May 11, 2026) to ¥250bn (July 30, 2026).

**Q5 (who runs it): integrity facts, recorded and not judged** **[M2013-088]**. The company's own note: "The Group has been
subject to class civil lawsuits in several regions for damages and suspension of shipments, etc. without specific amount of
damage, for its conspiracy to fix prices of shipping with major automobile shipping companies concerning marine
transportation of assembled automobiles, etc." (Financial Results 2026, note 13(3); the note of 2021 adds that the Company
"has been under investigation by some authorities overseas, on account of suspected violations of the antitrust laws
concerning the shipping of cargo including automobiles handled in or after September 2012"). Cash paid for antitrust matters:
¥2.3bn, ¥24.8bn, ¥2.9bn, ¥0.9bn, ¥3.0bn and ¥19.0bn in the years to March 2014 to 2019, and ¥1.0bn in the year to
March 2021; losses booked
¥13.1bn (year to March 2014), ¥19.5bn (2017), ¥3.1bn (2018) (Fact Book 2018; IR Data Book 2026). The class actions remain
open with "no significant change from the previous fiscal year". Not read: the corporate governance report, the notice of
the 2026 meeting (pay, board), and any regulator's own decision.

**Q6 (the money and the owners).** Buybacks: ¥200.0bn, ¥125.0bn and ¥144.1bn in the years to March 2024, 2025 and 2026 (cash
flow statements). The programme of May 8, 2025 (up to 48,000,000 shares or ¥150bn, open market, May 9, 2025 to April 30,
2026) bought 28,779,900 shares for ¥149,999,675,747, an average of ¥5,212 a share; it named a sum and a share count, no price
(TSE notice, May 7, 2026). The bottom of the COMPUTATION range below is ¥2,291 a share on the all-equity basis (¥4,358 on the
equity-only basis), both under the prices paid. Dividends: ¥390.0bn paid in the year to March 2023; payout ratios of 24% to
46%; dividend forecast for the year to March 2027 raised from ¥200 to ¥240 a share on August 5, 2026. Deals: Movianto
International (European healthcare logistics) bought for cash, ¥263.1bn net cash paid, goodwill ¥250.6bn at March 2026 against
¥22.9bn a year earlier; a cash tender offer for NS United Kaiun at ¥10,600 a share, signed July 31, 2026, expected to start
late November or late December 2026 after competition approvals, for the shares not held by NYK or Nippon Steel (about
11.3m shares, roughly ¥120bn), with NYK ending at 83.33%; a $221m subscription for 87.4% of Diamond Gas MidOcean (LNG),
expected August to September 2026. No deal paid in NYK shares found.

**Q7 (worth): the operator's two reporting figures, COMPUTATION, NOT A CLEARANCE.** Built by Q7's range convention as
written, with the steps that decide shown:
- *Cash input:* owner cash after every real cost (Step 0 table), all capital spending deducted (PG specific 2), the company's
  own tax with no conversion (Whose tax; no carryforward shelter found), working capital inside operating cash flow (d),
  equity-method income counted as the dividends received (inside operating cash flow).
- *(a) Cycle base:* the first two years of the literal window (years to March 2022 and 2023) are aberrational on the filer's
  own description ("turmoil in global logistics and higher freight rates", NYK Report 2025). The last full cycle, trough to
  trough, runs from the year to March 2017 (net loss ¥265.7bn, the deepest trough) to the year to March 2024 (ONE EBIT margin
  2.7%): eight years, owner cash average **¥74.0bn** (¥86.4bn on the all-equity basis, interest paid added back after the
  28.8% statutory rate). The literal window (years to March 2022-2026) averages ¥240.5bn (¥252.0bn all-equity) and is shown
  beside.
- *(b) Growth:* the series changes sign, and the previous cycle (years to March 2010-2016) averaged -¥128.8bn, so growth
  between cycles, and between halves of the window, is meaningless. **The range is the no-growth case alone, said so.**
- *(c) Acquisitions:* deducted (net of businesses sold): over the cycle they were a net inflow of ¥3.3bn a year, over the
  literal window an outflow of ¥30.0bn a year; purchases stop after year ten. Not a serial acquirer (net purchases ¥150.1bn
  over the window, under half of owner cash before purchases). The NS United Kaiun deal is signed and not closed: left out of
  the central figure; valued beside only as its cash cost (about ¥120bn added to net debt, about ¥297 a share), its own filed
  record not read, so its earnings are credited at nothing.
- *(e) Maintenance:* the filings state no maintenance figure; the depreciation variant is shown in Step 0 beside.
  *(f) Cap:* not engaged (no growth carried).
- *Rate:* 30-year JGB 4.085% (2026-10-09). *Net debt:* interest-bearing debt ¥1,361.7bn (leases ¥248.3bn included) less cash
  and deposits ¥226.0bn = **¥1,135.7bn** at June 30, 2026 (first-quarter tanshin, August 5, 2026); operating leases left out;
  investment securities (¥2,022.8bn, chiefly the ONE stake, whose dividends are already in owner cash) not subtracted.
  Shares 403,555,618.
- **Floor tested first:** at ¥7,358 the central case earns 2.1% on the all-equity basis (owner cash ¥86.4bn against market
  value plus net debt of ¥4,105bn) and 2.5% on the equity-only basis; even the literal window, beside, earns 6.1% and 8.1%.
  No case earns the floor of about ten percent at the price, so the COMPUTATION closes OUT by the floor **[M2003-149]**,
  whatever the width.
- **(1) VALUE RANGE (COMPUTATION):** one case, no growth, central (all-equity basis, cycle base): **¥2,291 a share** (equity-only
  basis ¥4,358). Beside: literal window ¥13,691 (equity-only ¥15,811). Against the price of ¥7,358.
- **(2) FAIR PRICE (COMPUTATION; each end valued at ten percent and the two averaged, here one end):** central, all-equity basis:
  **below zero, -¥705 a share** (owner cash of ¥86.4bn a year capitalised at ten percent is worth less than the net debt of
  ¥1,135.7bn); equity-only basis: **¥1,803 a share**. Beside, on the literal window: ¥3,716 (all-equity), ¥6,247 (equity-only).
  The all-equity figure is the central one; the equity-only figure is beside it and never decides alone.
- **In dollars per ADS** (0.2 share per ADS; ¥158.06 per $, Yahoo close 2026-10-08, aggregator): price $9.31 computed ($9.33
  quoted); value range $2.90 (equity-only $5.51); fair price below zero (-$0.89) on the all-equity basis, $2.28 equity-only;
  literal window beside, fair $4.70 all-equity and $7.90 equity-only.

**Q9 (could it ruin us).** Interest-bearing debt ¥1,361.7bn at June 30, 2026: loans ¥948.4bn, bonds ¥165.0bn, leases ¥248.3bn;
up ¥160.2bn in the quarter and from ¥694.1bn at March 2023. Cash and deposits ¥226.0bn. Interest coverage as the company
computes it 22.7 times (year to March 2026). Residual value guarantees on leased vessels ¥29.7bn (to October 2032). Chartered
ships under operating leases are outside the debt figures. A pending cash tender of about ¥120bn (NS United) and a $221m
subscription (DGMO).

**Q12.** None of the businesses the rows name.

## RESEARCH PASS
Not opened: the box is OUT, not TOO HARD (WORK).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 43b696d4, before the first download); written question by question;
      committed after each (Step 0 and Q1; Q2; the box and AFTER THE STOP; this audit).
- [x] Dispatched run: the brief allowed per-question pathspec commits of my two paths only; the lock is the dispatching
      session's; the fold is the dispatcher's (operator rule ten). No lock problem met; every commit went through first time.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Declared under contamination at
      the head of the file: one file name of an earlier NPNYY run seen in a directory search for my own paths (not opened),
      commit subjects about another company in the session header, and the memory index lines (nothing on this name).
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in that row (checked by
      `Test Runs/_research 2026-10-12 NPNYY/check_ids.py`). Every filing fact carries its document and date in place of an
      accession (no SEC filings exist), and the ZIM figures carry their SEC accessions. No number without a filing or a row;
      the conventions used are the framework's own, named where used, and two choices of this run are confessed below.
- [x] The order was kept; Q2's STOP closed the file; nothing after it is a clearance, and the Q7 figures are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, from operating cash flow less all capital spending, lease repayments and net
      acquisitions; never a net-income proxy (operator rule 5). The sovereign is from the Ministry of Finance file. The price,
      the ADR quote and the exchange rate are aggregator quotes, flagged.
- [x] Contrary evidence written down as found (four items under THE FOUNDATIONS); the facts for later questions are under
      AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] `tools/run.py` and `cover_shares.py` printed only that the name is not an SEC filer; nothing of theirs was used.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the research notes).

**Choices of this run, confessed.** (1) CONVENTION of this run: segment "operating profit" for Q2's business-of-parts
threshold is read as the filer's segment recurring profit, the only segment profit measure NYK reports; rationale: the
deciding affiliate's earnings sit below operating profit under the equity method, and a reading by operating profit would
weigh a 38% stake at zero. The same part decides on cash received (dividends), so the box does not depend on it. (2)
CONVENTION of this run: the last full cycle for Q7's cycle base is taken trough to trough as the years to March 2017-2024,
the troughs fixed on the filer's own descriptions (the ¥265.7bn net loss of the year to March 2017; ONE's FY2023 EBIT margin
of 2.7%); rationale: the series has no clean peak inside the data read, and the trough years are the ones the filer itself
describes as such. The figures are reporting figures only; the box was decided at Q2.

**What I could not get.** The Japanese annual securities report (yuho) on EDINET, with its own business-risk section; the
corporate governance report; the notice and results of the June 2026 general meeting (pay, board); ONE's full financial
statements (only its results pages in NYK's briefings); the rivals that do not file with the SEC (MSC, Maersk, CMA CGM,
COSCO, Hapag-Lloyd, Evergreen, HMM, Yang Ming); EBIT for ONE's FY2018 and FY2019 (only revenue and profit were in the deck
read); the regulators' own decisions in the car-carrier cases.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. First, Q1 and Q2 overlap for a commodity business: Q1's test 2 says of an unpredictable key variable "If
something is not very predictable, forget it." **[M1998-044]**, which would close a shipping company at Q1 TOO HARD
(NATURE) on the freight rate alone, while Q2's commodity section gives the same company a finding, OUT, unless it is the
low-cost operator. The routing paragraph sends only fast technological change to Q1 TOO HARD and is silent on a commodity
whose price cannot be forecast; I read the definition of understanding as the economics ("Is there ease of entry?"
**[M2011-014]**), passed Q1 narrowly, and let Q2 decide, because an OUT on the evidence says more than "too hard". Another
analyst could close the same file at Q1, and the text should say which. Second, Q2's business-of-parts threshold is written in
"operating profit", but a Japanese holding whose deciding part is an equity-method affiliate reports that part's profit only
below operating profit (recurring profit); read literally, the threshold would let a part with near-zero operating profit
but 62% of the group's earnings be outvoted. I confessed a reading for this run; the text should name the measure (segment
profit as the filer reports it, or cash received). Third, Q7's cycle-base specific (a) assumes a peak or trough can be
identified inside the data, but gives no rule when the series of a cyclical business runs negative for a decade and then
spikes; the choice of the cycle moved the central fair price from below zero to ¥3,716 (literal window), so the specific
needs a rule for picking the cycle, or should say the run states its choice and shows the other beside it, which is what I
did.
