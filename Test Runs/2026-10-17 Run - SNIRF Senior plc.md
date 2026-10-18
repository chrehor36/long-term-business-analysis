# Company Run — SENIOR PLC (LSE: SNR; OTC: SNIRF) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind run under
`Screens/_daily/_dispatch_brief.md` with the brief's two stated departures (no SEC filings; lines of evidence derived by the analyst).
Every judgment cites a v5 ledger id in bold; a filing fact carries its document and date in place of an accession (the issuer files no
10-K, 20-F or 40-F with the SEC).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold, 2026-10-17, after the run was committed: **not held** (`PORTFOLIO.md` read for this one ticker).

**THE FACT THAT FRAMES THIS RUN, found at Step 0 and written down at once** **[M1997-127]**: the shares cannot be bought. Senior was
acquired by Zeus UK Bidco Limited (funds advised by Tinicum and Blackstone) by a scheme of arrangement at 300p a share in total
(297.85p cash plus the 2.15p FY2025 final dividend): Rule 2.7 announcement 7 April 2026; scheme approved by shareholders 26 May 2026;
court sanction 6 October 2026; last day of dealings 7 October 2026; scheme effective 8 October 2026; admission to trading on the London
Stock Exchange cancelled, and the shares removed from the Official List, at 08:00 on 9 October 2026 (RNS of 6 and 8 October 2026, the
LSE cancellation notice and the FCA removal notice, all read through aggregator copies and search summaries, flagged). The brief could
not open the company's ‘Offer for the Company’ page and asked the analyst to check; this is what the check found. **CONVENTION of this
run:** the run is completed as the brief asks, as an analysis of the business against the last London close before cancellation (297.5p,
7 October 2026), because the framework names no rule for a name that has ceased to trade; rationale: the register asks for a run of
record and the business analysis stands on the filings whatever the quote; no purchase can follow from it while the company is private,
and the box line says so.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** 297.5p, the last London close (7 October 2026, the last day of dealings), Yahoo Finance chart data for SNR.L, an
  aggregator, flagged (operator rule 5). It sits at the scheme's cash consideration of 297.85p. SNIRF (OTC, USD): last quote 3.75 USD
  (stale, no volume, mid-September to 8 October 2026) and one print of 3.35 USD on 9 October 2026, same aggregator, flagged; not used.
  **There is no live price: the shares were cancelled from trading on 9 October 2026.**
- **Shares:** 419,418,082 ordinary shares of 10p issued at 31 December 2025, none issued in 2024 or 2025 (Annual Report and Accounts
  2025, share capital note and shareholder analysis); less 7,331,947 own shares held at 31 December 2025 (same report, Company note on
  own shares, which calls them treasury shares and describes the reserve as Employee Benefit Trust holdings) = **412,086,135
  outstanding**. One class. The offer's fully diluted value of about GBP 1,275m at 300p (Rule 2.7 announcement, 7 April 2026, aggregator
  summary) implies about 425m fully diluted shares. No later total-voting-rights announcement was read (none found; the shares no longer
  exist as listed securities). `python Screens/cover_shares.py` and `python tools/run.py` were not run: the issuer has no SEC financial
  filings, as the brief says.
- **Market cap:** 412.1m x 297.5p = **GBP 1,226m** (basic); about GBP 1,264m fully diluted.
- **Sovereign for the earnings currency (GBP):** **5.72%**, the Bank of England's series IUDLNPY, ‘Yield from British Government
  Securities, 20 year Nominal Par Yield’, 14 October 2026 (5.7225%; 5.758% on 7 October 2026, the last dealing day), from the Bank of
  England database (the issuing side of gilts, as the brief directs; the protocol's table names no GBP source). **CONVENTION of this
  run:** the 20-year par yield is used because it is the longest daily nominal par yield in that database; rationale: the protocol's
  other series are 30-year, the 10-year series (5.38% on 14 October 2026) is shorter still, and the gap between a 20- and a 30-year gilt
  is immaterial to a range this far from the price.
- **Filings read** (operator rule 4): Annual Report and Accounts 2025 (year to 31 December 2025, approved 27 February 2026); the 2024,
  2023, 2022, 2020, 2018, 2016 and 2015 annual reports (their five-year summaries and balance sheets with comparatives give every year
  2012 to 2025; the 2017, 2019 and 2021 reports themselves were not fetched, 404 at the company's URL pattern); Results for the
  half-year ended 30 June 2026; the offer announcements listed above (aggregator copies). Document list in
  `Test Runs/_research 2026-10-17 SNIRF/notes.md`.
- **One figure cross-checked against the filed statement:** 2025 net assets GBP 380.3m in the five-year summary (2025 report, page 188)
  equals Total assets 781.5 less Total liabilities 401.2 on the consolidated balance sheet (page 132). Agrees.
- **Arithmetic** (by hand from the statements; `q7.py` in the research folder): owner cash after every real cost, by year, is under Q7
  below (computed after the stop, so headed COMPUTATION, NOT A CLEARANCE). Gross capital expenditure against depreciation and
  amortisation excluding right-of-use assets, 2016 to 2025 (five-year summaries, GBP m): capex 52.8, 54.8, 56.3, 64.8, 26.8, 21.3,
  30.5, 35.9, 43.2 (group), 32.6 (continuing); D&A 54.0, 57.9, 56.9, 57.5, 51.4, 38.3, 39.5, 41.2, 39.6 (group), 23.3 (continuing).
  Stock pay (share-based payment charge, statements of changes in equity, GBP m): 2.2, 1.9, 3.4, 1.8, 3.0, 3.5, 4.3, 4.1, 4.5, 5.1
  (2016 to 2025). The Employee Benefit Trust bought 3,888,256 shares in 2025 (4,148,205 in 2024) to meet awards; no shares were issued.

**The lines of evidence chosen (the brief's second departure).** From the 2025 report's strategic report and divisional reviews (the
business and its two divisions), its principal risks (price-down pressure, programme risk, the land-vehicle cycle) and its financial
review (continuing against discontinued figures), the lines that decide this name are: (1) the two divisions' margins and returns over the
last full cycle, 2015 to 2025, which runs through the 737 MAX grounding and the pandemic, with the Aerostructures disposal handled by
using continuing figures where the report restates them (2024 and 2025) and the reported divisions before; (2) customers and pricing:
the filer's own principal risk on price-down pressure and what happened to price through the inflation of 2022 to 2025; (3) the
competitors' returns over the same span; (4) acquisitions and their goodwill (the 2014 and 2015 purchases, the 2020 impairment, Spencer
in 2022); (5) debt, leases and pensions; (6) buybacks (none made; the postponed GBP 40m programme) and stock pay through the trust;
(7) litigation (the US class actions charged 2018 to 2024); (8) the offer. Chosen because the first three decide Q2 and the rest feed
the later questions.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the first: a share is a business, "Would I be happy buying this stock if the market closed for
five years?" **[M1997-109]**, and the market closed on this one for good on 9 October 2026; what is left to judge is the business, which
is what the questions below do. The market "just tells us prices" **[M2006-077]**: the bid of 300p is a price a buyer paid, not a
finding about value, and the bidders and their advisers are the parties paid to tell in this case: "you do not get impartial advice from
Wall Street" **[M2020-037]**. The margin of safety, "if you have to actually do it on — with pencil and paper, it’s too close to think
about" **[M1996-084]**, is carried to Q7. **Contrary evidence, written down as found** **[M1997-127]**: (i) the shares no longer trade
(above); (ii) two private-equity groups competed (Advent International, three proposals in January and February 2026, per the aggregator
summary of the Rule 2.7 announcement, and the Tinicum and Blackstone vehicle that won at a 36.6% premium to the six-month average
price), which is evidence that informed buyers saw more value than the market did; (iii) the continuing business's margins in 2025 and
the first half of 2026 (Aerospace 11.4% and 13.1%, Flexonics 11.2% and 11.4%) are the best since 2015, which runs against the ordinary
record of the decade before; (iv) Precision Castparts, an aerospace parts maker, is the speakers' own example of a supplier where "people
don’t simply just take the low bid" **[M2016-006]**, so an aerospace components business cannot be presumed to lack a castle.

## THE STANDING RULE
Owning this would not put a buyer at risk of ruin on the buyer's own conduct if bought with cash and sized within the buyer's means;
"borrowed money has no place in the investor's tool kit" **[L2014-005]**, **[M2012-081]**. Moot in practice: there is nothing to buy.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The business, from the 2025 report.** Senior designs and makes fluid conveyance and thermal management components: ducting, bellows,
  flexible joints, hydraulic tubes and fittings, heat exchangers, expansion joints, hoses, exhaust-gas-recirculation (EGR) coolers and
  fuel lines. Two divisions after the Aerostructures sale (completed 31 December 2025): **Aerospace**, GBP 426.3m revenue in 2025
  (civil aerospace 32% of group revenue, defence 16%, adjacent markets such as semiconductor equipment 10%), and **Flexonics**, GBP
  313.4m (land vehicles 25% of group revenue: EGR coolers, EGR tubes and bellows, diesel fuel rails; power and energy 17%: expansion
  joints and bellows for petrochemical, oil and gas, nuclear and power plant). No customer took more than 10% of revenue in 2024 or 2025
  (2025 report, segment note).
- **The test.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand the economic dynamics of
  the industry" **[M2011-014]**. The key variables **[M1998-044]**: (1) aircraft build rates and Senior's content on each platform
  (Airbus backlog 8,754 aircraft at end 2025 against 793 delivered in 2025; Boeing 600 delivered in 2025, per the 2025 report's market
  review), plus defence volumes and the aftermarket; (2) North American and European heavy-truck builds and the powertrain mix (the
  land-vehicle products serve diesel engines); (3) industrial and energy capital spending for the expansion joints; (4) the price Senior
  can hold against its customers. Variables (1) and (3) are visible years ahead in backlogs and long platform lives; (2) is a slow change
  (the report prepares for electrification, battery cooling and hydrogen; the 2026 interim reports US truck demand pulled forward ahead of
  the 2027 regulatory change), not the fast-moving technology that closes a file here **[L1993-023]**; (4) is the castle question and
  belongs to Q2. Do the past statements tell me the future ones **[M2008-033]**? Mostly: the business has been the same two divisions
  for the whole span, and the disposal removes the part whose economics were worst.
- **Routing.** Not a bank or a holding company; the parts are two operating divisions, read by parts at Q2 (section B). Not an industry
  of fast change. Would the insiders write a ten-year forecast down **[M2000-105]**? Aircraft makers publish twenty-year fleet forecasts,
  and Senior's own goodwill test uses, in the filing's words, ‘the average growth rate forecast for the aerospace market as included in
  market outlooks from Boeing and Airbus’ (2025 report, goodwill note). *(Filing words are set in single quotes in this run; double
  quotes are kept for the ledger rows.)*
- **Contrary evidence written down** **[M1997-127]**: the land-vehicle line sells components for diesel engines; if heavy trucks move
  off diesel inside ten years, about a quarter of group revenue changes its economics. "if you have doubts about something being into your
  circle of competence, it isn’t" **[M2002-092]**: the doubt here is about the durability of a product line, which is Q2's test of what
  can "destroy, or modify, or reduce" the economic strengths **[M2000-014]**, not about whether the economics can be read.
- **VERDICT: IN.** The economics of a maker of engineered metal components sold to aircraft, engine, truck and plant builders can be read
  from its filings and its customers' published build forecasts **[M2012-065]**, **[M2011-014]**; the deciding uncertainty is the
  castle, carried to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now." **[M1995-038]**; a moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The parts table** (section B; adjusted operating profit by division, GBP m, from the segment notes of the 2022, 2023 and 2025 reports;
Aerospace 2021 to 2023 is the division as then reported, including Aerostructures; 2024 and 2025 are continuing operations as restated in
the 2025 report):

| part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year sum | share of company total (197.0) | share of the two divisions (292.4) |
|---|---|---|---|---|---|---|---|---|
| Aerospace | 7.9 | 20.3 | 27.0 | 36.9 | 48.5 | 140.6 | 71% | 48% |
| Flexonics (incl. China JV) | 13.1 | 25.8 | 38.5 | 36.4 | 38.0 | 151.8 | 77% | 52% |
| central costs | (14.9) | (17.6) | (19.7) | (20.3) | (22.9) | (95.4) | | |
| company (adjusted) | 6.1 | 28.5 | 45.8 | 53.0 | 63.6 | 197.0 | | |

Which part decides: measured against the company's five-year operating profit, both divisions exceed half, because central costs are
negative; measured against the two divisions' sum, Flexonics alone does (52%). On either reading Flexonics decides; on the first,
Aerospace decides with it. The file closes on both castles, Flexonics first. (The ambiguity is written up under WHAT IN THE FRAMEWORK WAS
WRONG OR UNCLEAR.)

**The castle tests, each with its filing fact.**
1. *What keeps it standing, and how permanent* **[M1995-038]**. For Senior: parts designed into long-lived aircraft and engine platforms
   and qualified with the customer, proprietary designs (the filer claims, in its principal-risk text, ‘higher competitive barriers based
   on the Group's broad range of IP and strong design expertise’), a spread of platforms (large commercial, regional, business jet,
   military), and an aftermarket. Against it, the same principal risk: ‘Customer pricing pressure is an ongoing challenge within our
   industries’, and of the aerospace customers, ‘large Aerospace OEMs, who leverage their buying power and market position to drive down
   supplier pricing’ (2025 report, principal risks, Price-down pressures).
2. *Would it stand without the lord?* No superstar is visible; the margin recovery is credited by the filer to price, volume and its own
   lean programme (the Senior Operating System). Neither for nor against.
3. *The money test* **[M2011-015]**. The filer's own words on Flexonics: ‘the Flexonics markets are more exposed to lower-cost global
   competition which drives price-down pressure’, and its answer is to move work to ‘cost competitive facilities, such as Mexico, the Czech
   Republic, South Africa, India and China’ (same section). That is the shape the rows warn against: "a product that can be shipped in
   from abroad very easily" **[M2007-116]**. For an attacker with money the barrier is customer qualification, not cost.
4. *Pricing power, the agony before a rise* **[M2005-020]**. Mixed. Through the inflation of 2022 to 2025 Flexonics' margin rose from 6.0%
   (2021) to 8.7%, 11.1%, 11.5% and 12.1% (2022 to 2025, incl. JV), and the filer credits ‘improved pricing’ for the Aerospace margin's
   rise to 11.4% in 2025 and 13.1% in the first half of 2026 (one 2025 award is a ‘Contract extension with improved pricing for
   proprietary thermal insulation components’): cost passed through, as "the businesses with strong competitive positions manage to pass
   through increases in raw material costs" **[M2005-017]**. Against it, the same report records ‘a resumption in price reduction and
   contractual price-down requests, particularly in certain Flexonics sectors’ in 2025: the customers ask for the price back as soon as
   supply chains settle.
5. *Unit volume and share of mind.* Not a consumer brand; volume follows the customers' build rates. Not applicable.
6. *The low-cost position* **[L2000-017]**, **[M1997-010]**. No filing shows Senior as its field's low-cost producer; shifting work to
   low-cost countries is the response of a business competing on cost, not the position of one that sets it.
7. *The brand.* Not applicable; sold business to business on specification.
8. *Would the customer choose it over the low bid?* **[M2017-009]**. The speakers' aerospace example is a supplier where "people don’t
   simply just take the low bid" **[M2016-006]**. Senior's filing describes the opposite pressure from its largest customers (test 1), and
   its margins have never approached those of the rivals below that sell into the same aircraft (competitor row).
9. *Ask the competitors.* Not possible from the public record within this run; the annual report names no competitor (below).
10. *Widening or narrowing* **[M1999-108]**. Over the decade, narrowed then recovered: Aerospace margin 13.4% (2015), 11.2%, 10.6%, 10.6%,
   9.1% (2019), 1.1% (2020), 1.8%, 3.7%, 4.4% (2023, incl. Aerostructures), then continuing 9.5% (2024), 11.4% (2025), 13.1% (H1 2026);
   Flexonics 14.5% (2015), 8.5%, 6.9%, 8.3%, 9.6%, 5.4% (2020), 6.0%, 8.7%, 11.1%, 11.5%, 12.1% (2025, incl. JV), 12.3% (H1 2026, incl.
   JV). The moat is not shown wider than in 2015; it is shown recovering since 2022.
11. *What could destroy, modify or reduce it* **[M2000-014]**. The land-vehicle line (a quarter of group revenue) sells EGR coolers, EGR
   tubes and bellows and diesel fuel rails; a move of heavy trucks off diesel would remove those products' purpose. The filer positions
   itself for battery cooling and hydrogen, but no filing shows those products earning anything yet. In aerospace, loss of content on a
   platform at re-sourcing is the standing risk.

**The competitor row.** The 2025 annual report names no competitor (a search of the 2016 to 2025 reports for the usual rivals found the
names only in directors' biographies and in the board-diversity review named after Sir John Parker). **CONVENTION of this run:** three
rivals that file with the SEC are chosen by product line: Parker-Hannifin (aerospace fluid conveyance and engine components), Eaton
(aerospace fuel and fluid conveyance) and Modine (heat-transfer products including commercial-vehicle coolers); rationale: the brief allows
chosen rivals where the report names none, and these three overlap Senior's two divisions. Named rivals that do not file: none (none are
named). Metric: company-level operating (or pre-tax) margin from each 10-K, since segment figures are not in the SEC's company facts; a
company-level figure is a coarse comparison and is flagged as such.

| fiscal year | Senior adjusted operating margin (group as reported; 2024-25 continuing) | Senior statutory operating margin | Parker-Hannifin operating margin (pre-tax), accession | Eaton pre-tax margin, accession | Modine operating margin, accession |
|---|---|---|---|---|---|
| 2015 | 12.7% | 8.5% | 14.5% (11.3%), 0000076334-15-000079 | n/a (revenue not tagged) | 3.5%, 0001140361-15-022274 |
| 2016 | 9.3% | 7.2% | 13.9% (9.8%), 0000076334-16-000196 | n/a | -0.6%, 0001140361-16-067258 |
| 2017 | 8.1% | 6.4% | 14.9% (11.0%), 0000076334-17-000095 | 16.5%, 0001551182-18-000074 | 2.6%, 0001140361-17-022417 |
| 2018 | 8.5% | 6.7% | 15.7% (11.9%), 0000076334-18-000087 | 11.2%, 0001551182-19-000045 | 4.4%, 0001140361-18-025479 |
| 2019 | 8.0% | 5.5% | 17.0% (13.5%), 0000076334-19-000096 | 12.1%, 0001551182-20-000050 | 5.0%, 0001140361-19-009735 |
| 2020 | 0.5% | -24.2% | 14.4% (11.0%), 0000076334-20-000099 | 9.8%, 0001551182-21-000022 | 1.9%, 0001140361-20-012690 |
| 2021 | 0.9% | 1.6% | 17.1% (15.7%), 0000076334-21-000187 | 14.8%, 0001551182-22-000004 | -5.4%, 0001140361-21-018956 |
| 2022 | 3.4% | 3.8% | 18.8% (10.2%), 0000076334-22-000034 | 14.0%, 0001551182-23-000004 | 5.8%, 0001140361-22-020696 |
| 2023 | 4.8% | 3.9% | 17.9% (14.1%), 0000076334-23-000042 | 16.5%, 0001551182-24-000006 | 6.5%, 0001140361-23-026536 |
| 2024 | 7.5% | 6.6% | 20.4% (18.0%), 0000076334-24-000044 | 18.4%, 0001551182-25-000006 | 10.0%, 0001140361-24-027133 |
| 2025 | 8.6% | 6.4% | 21.9% (20.7%), 0000076334-25-000035 | 18.0%, 0001551182-26-000007 | 11.0%, 0001558370-25-008058 |

(Fiscal years by the calendar year in which each year ends: Parker in June, Modine in March, Eaton and Senior in December. Senior's
margins from its five-year summaries, adjusted operating profit and operating profit over revenue. Rival figures from SEC company facts,
`Test Runs/_research 2026-10-17 SNIRF/rivals.py`; tag-dependent; Eaton's operating income is not tagged after 2019, so its pre-tax
margin is shown.)

**The field's returns over the last full cycle** (section C), judged in words. Senior's own return, adjusted operating profit before tax
over total equity plus net debt at the year end (five-year summaries; my arithmetic): 2014 21.6%, 2015 17.2%, 2016 12.3%, 2017 12.0%,
2018 12.7%, 2019 11.3%, 2020 0.6%, 2021 1.1%, 2022 4.5%, 2023 6.9%, 2025 12.8% (the filer's own continuing ROCE: 11.7% in 2024, 13.1%
in 2025). On statutory operating profit every year is lower (2019 7.8%, 2025 9.5%). The filer's stated aim is ‘a pre-tax return between
15% and 20%’; on this arithmetic it has not been met in any year since 2015. By division, before central costs, on segment net assets
(segment assets less segment liabilities, the segment notes; goodwill sits in segment assets from 2017): Flexonics 10.6%, 14.4%, 16.6%,
9.8%, 10.8%, 18.8%, 28.4%, 26.9%, 27.3% (2017 to 2025); Aerospace 14.0%, 13.7%, 13.2%, 1.4%, 2.2%, 4.4%, 5.8% (2017 to 2023, including
Aerostructures) and 16.5% in 2025 (continuing); central costs of GBP 14.7m to 22.9m a year are unallocated and would take several points
off each. Equity over twelve years went from GBP 411.6m (2014) to 380.3m (2025), while about GBP 164m was spent on acquisitions in 2014
and 2015 (cash flow, ‘Acquisitions less disposals’) and GBP 134.3m of goodwill was written off in 2020. **The judgment:** over the full
cycle 2015 to 2025, from a peak through the deepest aerospace trough in memory and back, the business as a whole earned ordinary returns,
below its own target in every year after 2015, much nearer to Modine's record than to Parker's or Eaton's in the same aircraft and the
same trucks: over that cycle the castle protected ordinary returns, where a moat is meant to protect "excellent returns on invested
capital" **[L2007-004]**; "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**. Flexonics alone
earned moderate returns for 2017 to 2022 and good ones from 2023, under a principal risk that names low-cost global competition.

**The change for the better.** The last three years show a better business: Flexonics' segment return near 27% before central costs
from 2023, Aerospace continuing margins of 11.4% and 13.1%, the group's best margin since 2015 (10.0% in the first half of 2026), and the
weakest part (Aerostructures) sold. The rows record that a business can change for the better, "the railroads were a terrible business
for decades and decades and decades and then they got good" **[M2017-026]**, and the framework credits such a change only on the
evidence of a full cycle in which the price behaviour held (Q2, Change, and what it does to a castle, citing **[M2005-020]** and
**[L1995-022]**). The price gains here were made in 2023 to 2026, in a rising aircraft market and, in 2025 and 2026, a US truck market
pulled forward ahead of the 2027 emissions change (2026 interim). No downturn has yet tested them, and the filer reports customers pressing
for price-downs as soon as supply settled. Only the next fall in volume can say whether the improvement is a castle or a cycle: "We
couldn't solve this problem, moreover, even if we were to spend years intensely studying those industries." **[L1993-023]**

**Contrary evidence weighed, not dismissed** **[M1997-127]**: the rise in price and margin through the inflation is real and filed; two
buyers competed for the whole company; a supplier of qualified aerospace parts can hold a castle **[M2016-006]**. Against these: the
cycle's returns are ordinary; the filer names buyer power and low-cost competition as principal risks; and a quarter of revenue serves the
diesel engine. None of the three supporting facts has been through a downturn.

- **VERDICT: TOO HARD (NATURE).** Over the last full cycle the castle protected ordinary returns **[L2007-004]**, and the improvement
  since 2023 is a change for the better that the framework credits only after a full cycle; until then the question is one that only a
  downturn can answer **[L1993-023]**, **[M2006-013]**. The deciding part is Flexonics, with Aerospace on the first reading; both stand in
  the same place. **Re-look condition (dated, from the filings):** the first fiscal year in which Flexonics' land-vehicle revenue or the
  group's civil aerospace revenue falls year on year (the likeliest candidates are 2027 and 2028, after the US truck pre-buy ahead of the
  2027 rule), read from the filings, after which the question is put again; and in any case only if the shares are again offered to the
  public.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING. NOT REACHED (facts under AFTER THE STOP)
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED (the balance-sheet reading is under AFTER THE STOP)
## Q5 — WHO RUNS IT? NOT REACHED (integrity facts recorded under AFTER THE STOP, not judged)
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED (facts under AFTER THE STOP)

## Q7 — WHAT IS IT WORTH? NOT REACHED as a question. COMPUTATION, NOT A CLEARANCE (operator rule 3; the owner's reporting figures, Part VII)
Nothing here is entry language; the file closed at Q2 and the shares no longer trade.

**Owner cash after every real cost, by year** (GBP m; net cash from operating activities, which is after interest paid, tax, restructuring,
lawsuit and deal costs and working capital; plus interest received and fixed-asset disposals; less purchases of property, plant and
equipment and intangibles, lease principal repaid, and the share-based payment charge; group as reported 2016 to 2024, continuing
operations 2025; five-year summaries and cash flow statements; `q7.py`). The all-equity column adds back bank interest net of interest
received at 25% tax (lease interest stays charged, since lease principal is charged and leases are left out of net debt). **CONVENTION
of this run:** one tax rate of 25% (the UK main rate from 2023) for the add-back in every year; rationale: the add-back is small (GBP 4m to
10m) and a year-by-year rate would not move any figure below by a penny a share.

| year | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| equity basis (after interest) | 45.5 | 55.9 | 41.6 | 42.4 | 11.9 | -5.9 | 15.0 | -3.8 | -1.6 | 20.0 |
| all-equity basis (before interest) | 53.0 | 63.1 | 48.3 | 48.0 | 17.6 | -1.8 | 19.9 | 3.7 | 8.0 | 28.9 |

**The range, by Q7's convention in full.**
- *(a) Cycle base.* The literal window 2021 to 2025 starts in the pandemic trough (2021 adjusted margin 0.9%, the filer's own account of
  that year) and straddles the Aerostructures disposal, so the base is the average over the last full cycle, 2016 to 2025, peak through
  trough and back: **GBP 28.9m all-equity** (22.1m equity basis). The literal window is shown beside: 11.7m all-equity (4.7m equity).
- *(b) Decline.* The series changes sign inside the window, so growth is measured between the halves: 2016 to 2020 average 46.0m against
  2021 to 2025 average 11.7m, a fall of about 24% a year (all-equity; 35% equity basis). Carried as the bottom of the range for ten years,
  then zero nominal growth; the no-growth case is the top.
- *(c) Acquisitions.* Deals over the cycle, net of businesses sold (cash flow lines ‘Acquisitions less disposals’ and ‘Acquisition
  costs/Disposal proceeds’): +1.3, +0.4, 0, +2.9, +0.4, +51.7, -25.3, -23.9, -10.7, -13.0 (2016 to 2025; the Aerostructures sale is
  excluded because its cash flows are already outside the 2025 figure), a net outflow of GBP 16.2m, 1.6m a year. Default pair:
  deducted, total growth credited: central base **GBP 27.3m**. Not a serial acquirer (net purchases in the window, 21.2m, are about a
  third of owner cash before purchases). No merger, no signed unclosed deal by the company; the takeover of the company itself is not a
  deal of the company's.
- *(d) Working capital.* Counted (inside net cash from operating activities; inventories rose from 14.5% of sales in 2014 to 24.2% in
  2024, then 19.6% in 2025 after the disposal).
- *(e) Maintenance.* Cash capital spending over the cycle (GBP 419.0m) was below depreciation and amortisation excluding right-of-use
  assets (459.6m), so a maintenance-only case would be lower, not higher; the all-spending case is central and the depreciation variant
  (capex replaced by depreciation: base 23.2m) is shown beside.
- *(f) The cap.* Not engaged; the shown growth is negative.
- **Discount rate:** 5.72% (Step 0). **Net debt:** GBP 89.4m at 30 June 2026, borrowings less cash, excluding IFRS 16 leases of 49.9m
  (2026 interim, net debt note), the latest filed balance-sheet date; leases left out and said so; no subsequent event stated in that
  filing changes it. Shares 412.1m.

| case (all-equity, central unless named) | base GBP m | top of range (no growth) | bottom (decline carried) | expected yield at 297.5p on EV of GBP 1,315m |
|---|---|---|---|---|
| **central: cycle base, acquisitions deducted** | 27.3 | **94p** (EV 477m) | **nil** (-1p; EV 85m, below net debt) | 2.1% |
| acquisitions left out | 28.9 | 101p | 0p | 2.2% |
| depreciation variant | 23.2 | 77p | nil (-4p) | 1.8% |
| literal window 2021 to 2025, acquisitions deducted | 7.5 | 10p | nil (-16p) | 0.6% |
| continuing operations, 2025 alone | 28.9 | 101p | 0p | 2.2% |
| equity basis, cycle base, acquisitions deducted | 20.5 | 87p | | 1.7% on market value |

- **The floor, tested first (2026-10-10):** the floor of about ten percent on GBP 1,315m needs about GBP 132m of owner cash a year; the
  best case shows 28.9m. **No case earns the floor at 297.5p**, so Q7, had it been reached, would close OUT whatever the width
  **[M2003-149]**. The width test is therefore not needed (the central range, nil to 94p, is in any case wider than three to one).
- **VALUE RANGE (reporting figure, COMPUTATION):** **nil to 94p a share** (all-equity, central), against a last price of 297.5p.
- **FAIR PRICE (reporting figure, COMPUTATION; Part VII):** **about 20p a share** on the all-equity basis (each end valued at ten percent,
  EV 289m and 70m before the acquisition deduction, 263m and 64m after it; averaged; less net debt 89.4m; 19.5p, after the company's own
  tax, no conversion); **equity-only figure beside: about 29p** (28.6p). On the offer's fully diluted share count the central figure is
  about 19p. London price 297.5p (7 October 2026 close, aggregator, flagged); SNIRF 3.75 USD (stale aggregator quote, flagged). The
  basis: the central figure is the all-equity one; the equity-only one is beside it and decides nothing.
- The buyback line for Q6 (written here because the file closed before Q6, and recorded at AFTER THE STOP, Q6): the bottom of the
  computed range is nil and the top 94p; the trust's purchases in 2024 and 2025 were made at about 169p and 190p a share.

## Q8 to Q12: NOT REACHED

---
## THE BOX
**TOO HARD (NATURE), decided at Q2** (over the last full cycle the castle protected ordinary returns, and the improvement since 2023 is a
change for the better not yet tested by a downturn). Integrity facts recorded, not judged. COMPUTATION, NOT A CLEARANCE: value range nil
to 94p against a last price of 297.5p; no case earns the floor at that price. **Re-look condition:** the first fiscal year in which
Flexonics' land-vehicle revenue or the group's civil aerospace revenue falls year on year, read from the filings; and only if the shares
are again offered to the public. **The shares cannot be bought: the company was taken private by scheme of arrangement (effective 8
October 2026; trading cancelled 9 October 2026).**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged; operator rule 2; **[M1997-127]**.)*

**Bearing on Q3 (capital).** Capital spending against depreciation, 2016 to 2025: GBP 419.0m of cash capex against 459.6m of D&A
excluding right-of-use assets; capex exceeded depreciation only in 2019, 2024 and 2025 (2025 continuing: 32.6m against 23.3m, a year with site relocation costs charged and an aerospace facility in Saltillo,
Mexico named in the report). Inventories rose faster than sales from 2019 to 2024 (Step 0 table below).
The 2014 and 2015 acquisitions (about GBP 164m, ‘Acquisitions less disposals’) preceded the GBP 134.3m goodwill impairment of 2020.
Spencer Aerospace was bought on 25 November 2022 (cash outflows on deals of 25.3m, 23.9m, 10.7m and 13.0m in 2022 to 2025, including
deferred and contingent consideration).

**Bearing on Q4 (the balance sheets, twelve years, before the income account, as Q4 asks).** From the consolidated balance sheets
(2015, 2016, 2018, 2020, 2022, 2024 and 2025 reports, each with its comparative; `bs_extract.txt`), GBP m:

| year end | goodwill | other intangibles | PP&E | inventories | trade and other receivables (current) | cash | bank loans and overdrafts | net assets | retained earnings | revenue |
|---|---|---|---|---|---|---|---|---|---|---|
| 2014 | 262.5 | 28.3 | 167.6 | 119.3 | 137.1 | 13.2 | 117.5 | 411.6 | 359.0 | 820.8 |
| 2015 | 284.5 | 72.1 | 206.6 | 126.9 | 140.6 | 14.4 | 207.2 | 430.9 | 384.7 | 849.5 |
| 2016 | 318.8 | 60.5 | 254.2 | 154.4 | 152.5 | 17.5 | 214.6 | 500.5 | 400.0 | 917.0 |
| 2017 | 302.4 | 41.6 | 256.1 | 154.5 | 154.3 | 12.6 | 167.2 | 531.6 | 438.8 | 1,023.4 |
| 2018 | 312.9 | 26.7 | 285.6 | 177.8 | 165.0 | 17.2 | 170.0 | 568.2 | 465.6 | 1,082.1 |
| 2019 | 297.1 | 12.9 | 369.3 (incl. right-of-use) | 169.3 | 133.6 | 15.8 | 161.7 | 559.6 | 472.5 | 1,110.7 |
| 2020 | 165.0 | 4.8 | 330.5 | 147.6 | 85.3 | 23.6 | 153.0 | 393.3 | 305.1 | 733.6 |
| 2021 | 150.2 | 4.2 | 294.6 | 145.2 | 98.0 | 51.1 | 131.0 | 425.1 | 343.2 | 658.7 |
| 2022 | 199.7 | 36.2 | 307.2 | 194.3 | 126.7 | 43.2 | 143.7 | 449.4 | 346.5 | 848.4 |
| 2023 | 193.3 | 33.1 | 284.7 | 207.5 | 141.7 | 47.6 | 179.6 | 457.1 | 368.0 | 963.5 |
| 2024 | 195.4 | 32.1 | 292.1 | 236.0 | 137.2 | 45.5 | 198.9 | 469.9 | 376.7 | 977.1 |
| 2025 (after the disposal) | 160.9 | 26.7 | 176.4 | 144.9 | 108.2 | 82.0 | 155.3 | 380.3 | 350.0 | 738.2 (continuing) |

What moved and why, on the filings: goodwill and intangibles rose with the 2014 and 2015 purchases and fell by the 2020 impairment;
Spencer added goodwill in 2022; in 2025, with the disposal and exchange movements, goodwill fell by GBP 34.5m and PP&E by about 116m. Retained earnings ended the
twelve years below where they began (359.0m to 350.0m) despite profits in every year but 2020, because of the 2020 loss (GBP 158.5m,
mostly the impairment), the 2025 loss on disposal and the dividends; net assets fell from 411.6m to 380.3m. Inventories against sales:
14.5% (2014), 15.2% (2019), 21.5% (2023), 24.2% (2024), 19.6% (2025): working capital became heavier through the recovery. Borrowings
peaked at about GBP 215m in 2016 and stood at 155.3m in 2025 against cash of 82.0m. The defined-benefit surplus fell from 43.5m to
23.3m in 2025 with a GBP 7.3m charge for ‘pensions benefit clarifications’. What the figures do not say: the continuing business's own
balance sheet before 2025, which is not filed. Adjusting items charged in most years (restructuring 2019 to 2025, site relocation 2023 to
2025, US class action lawsuits 2018, 2019 and 2024, pensions 2018 and 2025), the recurring "one-time"; the reported cash flows include
them and the owner cash above is after them. EBITDA appears in the filer's covenant leverage ratio (net debt to EBITDA), not as an earnings figure.

**Bearing on Q5 (integrity facts, recorded, not judged).** The 2025 report's headline KPIs lead with adjusted measures (adjusted operating
margin, adjusted profit before tax, adjusted EPS of 9.65p) and show basic EPS (6.60p, down 18%) beside them; adjustments were made in most
years from 2018 (above). US class action lawsuits were charged as adjusting items in 2018 (GBP 3.9m), 2019 (2.6m) and 2024 (1.1m); their
subject was not read in this run. Executive incentive measures: adjusted EPS, relative TSR and ROCE, one third each (2025 remuneration
report). The filer publishes medium-term margin and ROCE targets and reports progress against them in the 2025 report and the 2026
interim (‘already meeting target levels’). The board unanimously recommended the cash offer of 300p.

**Bearing on Q6 (the money and the owners).** No share buybacks in the span; the Employee Benefit Trust bought 3,888,256 shares in 2025
for GBP 7.4m (about 190p) and 4,148,205 in 2024 for 7.0m (about 169p) to meet awards (equity statement and directors' report); against
the COMPUTATION range above (nil to 94p) those prices sit above its top. A GBP 40m buyback from the Aerostructures proceeds was announced
and then postponed when the offer talks began (2025 report). Dividends were suspended for 2020 and 2021 and resumed in 2022 (2.30p for
2023, 2.40p for 2024, 3.00p for 2025). No deal was paid in shares. The Aerostructures business was sold to Sullivan Street Partners
(completed 31 December 2025; upfront net cash proceeds GBP 95.7m per the 2025 report, with an earn-out and a GBP 31.5m loss after tax from
discontinued operations in 2025).

**Bearing on Q9 (debt and exposures).** Net debt excluding leases GBP 89.4m at 30 June 2026 (73.3m at 31 December 2025); leases 49.9m;
leverage 0.9 times EBITDA and interest cover 9.4 times by the covenant definitions; committed facilities of GBP 264.7m, mostly five private
placement loans, weighted average maturity 2.4 years (2026 interim). Short maturities of size relative to the facilities, read against
**[L2014-024]**'s shape, would be the item to weigh.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit e675c091); written question by question; committed after Step 0 and Q1
      (a6377f40), after Q2 (08aa80f4), and at the close.
- [x] Dispatched: the brief allowed per-question pathspec commits of the two paths; the lock is the dispatching session's (operator rule
      ten); the run binds nothing until folded into the register.
- [x] Blind rule: no other run file, holding review, `PORTFOLIO.md` or listed Screens file was opened or searched. **Contamination
      declared:** (1) before the copy I ran a directory listing of `Test Runs/` filtered for "SNIRF" and "Senior", to check for a prior
      file under the run's own name; it returned nothing, but a filtered listing is a search of the folder, a breach of the letter of the
      rule, declared here; (2) the session context showed recent commit subjects (another company's run and fold of 2026-10-17) and the
      names of other companies' research folders in the git status; (3) the session's memory index carries one line on the queue and
      gate-clearer counts. None names this company or bears on it; none was used.
- [x] Every v5 id resolves (`check.py`: every M/L/R id in the CSV, no E-ids, every double-quoted fragment beside an id found in a row
      cited with it); every filing fact names its document and date (no accession exists for this issuer; rivals carry SEC accessions);
      every number has a filing or a CONVENTION.
- [x] The order was kept; Q2 closed the file; everything after it is NOT REACHED, COMPUTATION, or facts not weighed.
- [x] Owner cash after every real cost (stock pay and lease principal charged), never a net-income proxy; the sovereign from the Bank of
      England (GBP; series and date named; the 20-year choice confessed); aggregator quotes flagged (price, SNIRF quote, offer
      announcements read through aggregator copies).
- [x] Contrary evidence written down as found (foundations, Q1, Q2); facts for later questions under AFTER THE STOP; integrity flag in
      the box line.
- [x] Not a point-in-time run; no row dated after an anchor arises.
- [x] `tools/run.py` not used (no SEC filings); arithmetic by hand and in `q7.py` and `rivals.py`.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the commit).
- **Weaknesses I know of:** the offer timeline rests on aggregator copies of the RNS, not the RNS files themselves; the 2017, 2019 and 2021
  reports were not read directly (their figures come from comparatives and five-year summaries); the rival comparison is company-level,
  not segment-level; the parts table mixes perimeters (Aerostructures inside Aerospace until 2023); the cycle base for Q7 also mixes
  perimeters (group to 2024, continuing in 2025); the class actions' subject was not read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A name that has stopped trading.** The framework and the template assume a price at which the name can be bought; nothing says what
a run does when the company has been taken private between dispatch and run (here, eight days before). I completed the run on the last
close and confessed it as a CONVENTION; a rule (for example, close at Step 0 with a box such as "not available", or run the business
questions only) would save the work. (2) **The parts threshold when central costs are negative.** Section B makes a part decide at "more
than half of the company's five-year operating profit"; with unallocated central costs both divisions exceed half of the company total
(71% and 77%), so both decide, while against the divisions' sum only Flexonics does (52%). The text should name the denominator.
(3) **Ordinary returns over the cycle against a recent change for the better.** Q2's list sends a castle that protected only ordinary
returns over a full cycle to OUT, and section C sends a change for the better, until a full cycle passes, to TOO HARD (NATURE). When the
full cycle is ordinary and the last three years are better (partly through a disposal), both sentences apply; I read section C as the
more specific one and closed TOO HARD (NATURE); another analyst could close OUT on the same evidence, with the same practical result.
(4) **A disposal inside the Q7 window.** Specific (c) deducts acquisitions "net of businesses sold"; applied literally to a window that
contains the sale of a whole division, it credits the business with the proceeds of selling part of itself, and the window's owner cash
mixes the old and new perimeters. I excluded the discontinued sale and said so; the text has no rule for a discontinued operation.
(5) **The sovereign for GBP.** The protocol's table has no GBP row, and the Bank of England's daily database carries par yields to 20
years only; the brief's direction (DMO or Bank of England) was followed with the 20-year series, confessed. A GBP row in the table would
fix the series for every UK run. (6) **The re-look condition for a private company.** Section C's dated re-look reads the filings of
the first down year; a company taken private files only at Companies House, and no rule says whether that counts.
