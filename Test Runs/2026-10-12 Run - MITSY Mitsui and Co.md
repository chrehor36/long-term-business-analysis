# Company Run: Mitsui & Co., Ltd. (TSE Prime: 8031; US over-the-counter ADR: MITSY, see the ticker note) 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form:
`Test Runs/_TEMPLATE - Company Run.md`. Dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the three
departures the brief states (lines of evidence derived by the analyst; the primary document is the company's own annual
securities report, not an SEC filing; the SEC arithmetic tools do not serve the name). Every judgment cites a v5 ledger
id in bold; every filing fact carries its document and date in place of an accession number (departure 2).

**TICKER NOTE, found before any verdict.** The brief names the run "MTSUY". On the price service `tools/sources.py` reads,
MTSUY is **Mitsubishi Corporation**'s ADR (long name "Mitsubishi Corporation", $29.23 on 2026-10-12), not Mitsui's.
Mitsui's ADR is **MITSY**: Mitsui's own IR page (https://www.mitsui.com/jp/en/ir/information/basic/index.html, read
2026-10-12) gives "Ticker Symbol: MITSY", "1ADR = 20 common shares", depositary Citibank, N.A. Every other detail of the
brief (the name, the TSE code 8031, the 107th Annual Securities Report, the seven segments, the July 2024 split) is
Mitsui's, so this run is a run of **Mitsui & Co., Ltd.**; the file keeps the name the brief gave it so that the dispatcher
can find it. The dispatching session should correct the ticker at the fold.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-12, after the run was committed: [withheld from the public copy].
This file was committed as `Test Runs/2026-10-12 Run - MTSUY Mitsui and Co.md` and renamed at the fold because the
dispatcher's brief gave the wrong ticker; see `Test Runs/ADDENDUM 2026-10-12 - the MTSUY brief that ran Mitsui, the dispatcher's ticker error.md`.*

**CONTAMINATION, declared.** (1) My first command, meant to check that the run file's name was free, was a filtered
listing of `Test Runs/` for the ticker. It printed four file names: two runs dated 2026-07-15 (one titled "MITSY (Mitsui &
Co)", one titled "MTSUY (Mitsubishi Corp)"), a run dated 2026-08-28 titled "MITSY (Mitsui) v4.1". None was opened. (2) The governing framework itself names a "MITSY regression run" (Q1, A holding company; Q4,
Equity-method income) and quotes the trading-house row **[M2023-031]**; those are the governing text, read as such. (3) The
filed report names National Indemnity Company, "a wholly owned subsidiary of Berkshire Hathaway Inc.", as a major
shareholder (9.82% reported on March 10, 2025; Annual Securities Report, 4. Corporate Information, (6) Status of Major
Shareholders). It is a filing fact. Under the row-about-one-company convention (Q2) it decides nothing here and is not
used as evidence for any box; it is named because the analyst's incentive to agree with a famous buyer is exactly what
operator rule 9 asks to be declared.

**Lines of evidence (departure 1), chosen from the report's overview, risk factors and operating review.** The report
calls Mitsui a "global investment and trading company" in seven segments; its risk factors put first business-investment
risk (non-operated joint ventures, equity-method investees), then geopolitical risk (Russian LNG, the Middle East), country
risk, commodity prices ("iron ore, metallurgical coal, copper, crude oil, natural gas, and LNG"), foreign exchange, the
listed-stock portfolio, credit risk and guarantees. So the run reads: (1) the parts table, segment profit and assets
FY2016 to FY2026, to find the part that decides; (2) the deciding part's cost position, volumes and returns over the last
iron-ore cycle (the trough of FY2016 to FY2026); (3) the equity-method investees and how their earnings reach cash
(dividends received against share of profit); (4) the balance sheets FY2016 to FY2026, debt, leases and guarantees;
(5) investments, acquisitions (Rhodes Ridge) and the post-year-end Penske proposal; (6) buybacks and their prices;
(7) stock pay; (8) litigation, Russia, and the integrity record; (9) pricing through the last inflation, read here as
the commodity price pass-through, since a trading and resource house sets no list price. Competitors: the report names
none by name; it says "Other Japanese global investment and trading companies" (Risk Factors, Risk Due to Competition),
so the comparison set is three of them (see Q2).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** ¥4,775, Tokyo close 2026-10-09 (the last Tokyo session before this run; 2026-10-12 is a Japanese holiday),
  Yahoo Finance chart service via `tools/sources.py`, **aggregator, live quote only (operator rule 5)**. ADR MITSY $610.70
  close 2026-10-12, same service, aggregator. USD/JPY 158.68 (same service, aggregator) puts 20 Tokyo shares at $601.8,
  1.5% under the ADR on a later day: consistent with the ratio of 20.
- **ADS ratio:** 1 ADS = 20 shares. Verified twice: the report's own definition ("'ADS' means an American Depositary
  Share representing 20 shares", Certain References and Information, page 1 of the 107th report) and Mitsui's IR
  shareholder page ("1ADR = 20 common shares", depositary Citibank, N.A.), read 2026-10-12.
- **Shares:** issued 2,864,666,576 at March 31, 2026 and at June 12, 2026 (107th report, 4. Corporate Information,
  (1) 2) Number of Shares Issued), after 41,075,000 shares cancelled on March 30, 2026. Treasury stock 17,038,165
  (same report, 2. Acquisition of Treasury Stock, (4)); a further 13,378,432 shares sit in the employee stock ownership
  trust, counted as treasury in the consolidated accounts. Later filing: the release of August 4, 2026 ("Share Repurchase
  and Cancellation of Treasury Stock") gives shares outstanding excluding treasury stock of 2,848,191,964 at June 30, 2026
  (the trust's 13,281,132 shares not deducted); the release of October 1, 2026 gives 8,285,900 shares bought from August 5
  to September 30, 2026 for ¥42,114,317,838. **Count used: 2,839,906,064** (June 30 count less the shares bought since),
  the trust's shares left in (0.5%; the count with them out is 2,826,624,932, shown where it matters).
  `python Screens/cover_shares.py MTSUY` returned "NOT AN SEC REGISTRANT in the live ticker file": not usable (departure 3).
- **Market cap:** 2,839,906,064 × ¥4,775 = **¥13,560.6 bn** (about $85.5 bn at 158.68).
- **Sovereign for the earnings currency (yen):** **4.14%**, the 30-year JGB, Japan Ministry of Finance official JGB curve
  (jgbcme.csv), dated 2026-10-08, via `python tools/sources.py`.
- **Net debt (for the all-equity basis):** interest-bearing debt excluding leases ¥5,303.1 bn less cash and time deposits
  ¥886.4 bn = **¥4,416.7 bn at June 30, 2026** (Financial Results for the Three-Month Period Ended June 30, 2026, IR
  presentation of August 4, 2026, slide "Consolidated Statements of Income & Financial Position"; the same slide gives
  ¥4,139.0 bn at March 31, 2026). The buyback after June 30 (¥42.1 bn) is added: **¥4,458.8 bn**. Lease liabilities
  (¥584.9 bn at March 31, 2026, IFRS 16, note 6) are left out of net debt and their principal repayments are charged
  inside owner cash instead (said so; the framework leaves operating leases out). Listed and unlisted equity stakes
  (other investments ¥2,820.8 bn, of which listed FVTOCI ¥1,479.3 bn) are **not** netted as cash, because their
  dividends are inside owner cash; counting both would count them twice.
- **Filings read** (operator rule 4; departure 2, no accession numbers exist): the English **Annual Securities Report for
  the 107th fiscal year (year ended March 31, 2026)**, compiled from the Yukashoken Hokokusho filed with the Kanto Local
  Finance Bureau on June 12, 2026 (en_107yuho.pdf, posted August 12, 2026); the 106th (FY2025), 104th (FY2023), 102nd
  (FY2021), 100th (FY2019) and 98th (FY2017) reports from the same IR library, which together give eleven years of
  statements, FY2016 to FY2026; the Q1 FY March 2027 results presentation (August 4, 2026); the releases of March 23,
  July 22, August 4, September 1 and October 1, 2026. There is no proxy in the US sense; pay and board are read from the
  report's Corporate Governance section.
- **One figure cross-checked against the filed statement:** total interest-bearing debt at March 31, 2026 in the IR
  presentation, ¥5,707.7 bn, equals the filed balance sheet's short-term debt ¥166,249 mn + current portion of long-term
  debt ¥509,475 mn + long-term debt ¥5,032,042 mn = ¥5,707,766 mn. Cash from operations FY2026 ¥952,912 mn agrees between
  the cash-flow statement, the selected data and the MD&A (¥952.9 bn).
- **Arithmetic** (`tools/run.py MTSUY` returned "not an SEC filer ... UNRESEARCHED, not UNKNOWABLE": not usable; done in
  `Test Runs/_research 2026-10-12 MTSUY/scripts/owner_cash.py` from the filed cash-flow statements, each year's investing
  lines summed and checked against the filed investing total, every year agreeing to the million). Owner cash after every
  real cost (Mn JPY → ¥ bn): cash from operations (which takes in dividends received, not the share of investees' profit,
  and the working-capital change) less net purchases of PP&E and investment property, less businesses bought net of
  businesses sold (equity-method investees, other investments, subsidiaries), less net loans made, less lease principal
  repaid, less transactions with non-controlling holders. Stock pay is inside operating cash (expensed; see Q4).

  | FY (Mar) | CFO | net PP&E | net businesses | lease | owner cash, all spending (equity-only) | same, all-equity (+ interest paid × 68.5%) | maintenance-only owner cash, all-equity | profit attributable |
  |---|---|---|---|---|---|---|---|---|
  | 2017 | 404.2 | 152.0 | 154.6 | 0 | 12.6 | 57.3 | 208.4 | 306.1 |
  | 2018 | 553.6 | 143.8 | 138.5 | 0 | 250.9 | 298.8 | 362.8 | 418.5 |
  | 2019 | 410.7 | 262.5 | 413.0 | 0 | -303.4 | -246.7 | 282.8 | 414.2 |
  | 2020 | 526.4 | 269.6 | -79.8 | 60.9 | 268.7 | 334.9 | 320.2 | 391.5 |
  | 2021 | 772.7 | 259.5 | 47.1 | 58.4 | 403.7 | 444.7 | 509.6 | 335.5 |
  | 2022 | 806.9 | 161.2 | 70.8 | 55.6 | 471.2 | 505.0 | 437.3 | 914.7 |
  | 2023 | 1,047.5 | 141.6 | 69.6 | 65.5 | 714.8 | 781.0 | 776.7 | 1,130.6 |
  | 2024 | 864.4 | 215.2 | 239.3 | 74.0 | 349.4 | 457.3 | 653.9 | 1,063.7 |
  | 2025 | 1,017.5 | 225.4 | -23.0 | 90.1 | 733.6 | 870.0 | 792.4 | 900.3 |
  | 2026 | 952.9 | 986.0 | 50.9 | 109.2 | -215.7 | -92.4 | 703.3 | 834.0 |
  | **5-yr avg FY2022-26** | 937.9 | | | | **410.7** | **504.2** | **672.7** | 968.7 |
  | 10-yr avg FY2017-26 | 735.7 | | | | 268.6 | 341.0 | 504.7 | 670.9 |

  Maintenance spending is taken as depreciation and amortization less right-of-use depreciation (FY2026: ¥333.2 bn less
  ¥91.9 bn = ¥241.3 bn), because lease cost is already charged as principal repaid; the filer's own three-year plan puts
  "Investments to strengthen existing businesses" at ¥680 bn for FY2027-29, ¥227 bn a year (Q1 FY2027 presentation,
  "Capital Allocation Forecast and Results"), which agrees. FY2026's PP&E line holds the Rhodes Ridge iron-ore interest
  (Mineral & Metal Resources capital additions ¥813.0 bn, segment note). FY2016 (a loss year, profit −¥83.4 bn) is in the
  research script and in the cycle reading at Q2 and Q7.

*(Note written during this run, 2026-10-12, at Q7: the ten-year averages in the Step 0 table and in Q3 first read ¥264.0 bn and ¥336.4 bn; they were computed before a FY2016/FY2017 line was corrected in `owner_cash.py` (an acquisition of ¥45,851 mn belonged to FY2016, as the check against the filed investing total showed). Corrected to ¥268.6 bn and ¥341.0 bn; the five-year figures were not affected.)*

## THE FOUNDATIONS (not a gate)
Three foundations bear on this name. A share is a business **[M1997-109]**: the question is what the iron ore, gas,
machinery and food businesses will produce, and not what the next holder pays. No macro forecast enters
**[M2000-094]**: commodity prices are not forecast here; they enter only as a property of the business, its place on the
cost curve. And the analyst's habits: write contrary evidence down at once **[M1997-127]**, and ask "What do I not know
that I need to know?" **[M1999-129]**. The famous holder named in the filing is the clearest case of "who is paid to tell
you" turned on the analyst himself: the pull is to agree; it is declared above and given no weight.
**Contrary evidence, written down as found** **[M1997-127]**: (1) owner cash after all spending was negative in three of
the last ten years (FY2019, FY2026, and near zero FY2017), so the business spends nearly what it makes; (2) FY2016 was the
company's first loss, −¥83.4 bn, with the Mineral & Metal Resources segment losing ¥162.5 bn, so the deciding part has a
recent large loss; (3) the company publishes profit forecasts and features an adjusted cash figure, "Core Operating Cash
Flow"; (4) Russian LNG exposure of ¥279.8 bn gross (Risk Factors (2)); (5) guarantees with a maximum potential of
¥1,147.8 bn (note 25).

## THE STANDING RULE
Buying a part-interest in a listed share, unlevered, does not by itself put the buyer at risk of ruin; the rule binds the
buyer's financing and sizing **[M2012-081]**, **[L2014-005]**. The target's own debt is weighed at Q9.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test applied.** Understanding means "a reasonable fix on about what the earning power and competitive position will
look like in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand the economic dynamics of the
industry" **[M2011-014]**. A holding company is understood by its parts, and only the part that decides matters (Q1, A
holding company; Q2, A business of parts, CONVENTION): more than half of five-year operating profit, or else the largest.

**The parts table (profit attributable to owners, ¥ bn, the segment note of each report; FY2022-25 as reported in the
104th and 106th reports, FY2026 in the 107th).**

| Segment | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | 5-yr sum | share of segment total |
|---|---|---|---|---|---|---|---|
| Mineral & Metal Resources (MMR) | 497.6 | 438.8 | 335.1 | 285.4 | 253.6 | 1,810.5 | **36.9%** |
| Energy | 114.0 | 309.4 | 281.7 | 173.5 | 164.2 | 1,042.8 | 21.2% |
| Machinery & Infrastructure | 120.8 | 171.9 | 248.7 | 232.9 | 225.9 | 1,000.2 | 20.4% |
| Chemicals | 68.9 | 70.9 | 39.2 | 75.9 | 67.5 | 322.4 | 6.6% |
| Innovation & Corporate Development | 57.6 | 66.7 | 53.8 | 87.3 | 59.0 | 324.4 | 6.6% |
| Lifestyle | 61.5 | 54.8 | 94.1 | 53.7 | 52.0 | 316.1 | 6.4% |
| Iron & Steel Products | 26.9 | 22.5 | 11.2 | 13.2 | 18.9 | 92.7 | 1.9% |

No part carries more than half. The largest, **Mineral & Metal Resources, decides.** (The report gives segment profit
after tax, not operating profit; profit attributable is the segment measure it gives, and it is used, said so.)

**What MMR is, from the filings.** Equity share of production in FY2026: iron ore 63.8 Mt, metallurgical coal 5.1 Mt,
copper 91 kt (Q1 FY2027 presentation, "Equity Share of Production"). Iron ore comes from Robe River (33.0%, operator Rio
Tinto, 20.8 Mt), Mt Newman / Yandi / Mt Goldsworthy / Jimblebar (7.0%, operator BHP, 20.6 Mt) and a 6.71% holding in Vale
(22.5 Mt equity share); Rhodes Ridge, an undeveloped Pilbara deposit, was bought in FY2026 (¥723.8 bn, MD&A cash flows).
Mitsui is a **non-operator**: "the business operations, including decision-making for development and production, are
subject to the operator's policy" (Risk Factors (1)). Profit sensitivity: ¥3.0 bn per US$1/t of iron ore (Risk Factors (5)).

**The key variables and whether they are foreseeable** **[M1998-044]**. (1) The operators' cost position: foreseeable.
BHP's own filing calls its Western Australia Iron Ore "the world’s lowest cost major iron ore producer, now for the
seventh year, with a greater than US$10 per tonne cost advantage over its nearest Pilbara competitor" (BHP Group 20-F for
FY2026, filed 2026-08-18, accession 0001193125-26-354647): WAIO cash cost US$19.66/t on revenue of US$23.7 bn and
Underlying EBITDA of US$14.7 bn. At the last trough the same business ran at US$15.06/t with EBITDA of US$5.5 bn on
revenue of US$10.3 bn (BHP 20-F for FY2017, accession 0001193125-17-297000, "WAIO unit costs" table, FY2016 column).
(2) Volume: foreseeable in the range the presentation gives (63 to 65 Mt a year through FY2029), with decades of
Pilbara deposits behind it and Rhodes Ridge to come. (3) The iron-ore price: **not foreseeable, and the company itself
will not write it down**: "Iron ore and metallurgical coal price assumptions are not disclosed." (Q1 FY2027
presentation, footnote 7). "If something’s important but unknowable, forget it." **[M2006-076]**; and the insiders' test,
"They would say, “That’s too hard.”" **[M2000-105]**.

**Routing.** This is not a fast-changing industry (no technology turns the ore body over in ten years), so the Q1 TOO
HARD route for rapid change does not apply **[L1993-023]**. What the rows give for a commodity producer is the
cost-position reading: "It’s like comparing a copper producer whose costs are $2.50 a pound with a copper producer whose
costs are $1 a pound. Those are two different kinds of businesses. One is going to go broke at a buck-fifty a pound. And
the other one’s going to still be doing fine." **[M2009-059]**. The ten-year fix asked for is on earning power and
competitive position **[M2012-065]**: the competitive position is foreseeable (bottom of the cost curve, the Pilbara's
reserves and its distance to China); the earning power is foreseeable only as a cycle range bounded below by the trough
record (BHP's WAIO still earned EBITDA of more than half its revenue in FY2016), not as a point. The price is the
unknowable variable; it is carried to Q7 as the width of the range and the cycle base, not treated as understood.
The speakers keep a model of "how far off we can be" **[M2011-084]**; here, on the deciding part, by the swing from FY2016 (MMR −¥162.5 bn, after
impairments in copper and other non-iron assets) to FY2022 (+¥497.6 bn).

**The doubt rule.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**.
I have no doubt about what MMR is (a minority, non-operating owner of low-cost bulk iron ore with smaller coal and copper
positions) or about its place on the cost curve; I have a stated ignorance of the price, which the speakers' copper
example shows is not the same thing. The trading-house row **[M2023-031]** ("businesses that we could understand as a
group, although it didn’t mean we had deep understanding on any") is a row about named companies and decides nothing
here (Q2, A row about one company, CONVENTION); it stays OPEN against the by-parts reading. The quick decision is made
"off the figures" **[M2008-069]**, which is how this run read it.

**Contrary evidence, written down** **[M1997-127]**: the company does not disclose the price it plans on; Mitsui is a
non-operator in the deciding part and depends on two operators; the FY2016 segment loss shows MMR also holds high-cost
assets (the copper losses), so "low-cost" is true of the iron ore and not of every MMR asset.

**VERDICT: IN**, on the deciding part's foreseeable cost position and volume, with the price carried as ignorance to Q7.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**. The file closes on the deciding part, MMR (Q2, A business of parts).

**What kind of business the deciding part is.** Iron ore is a commodity sold at an index price; no customer asks for
Mitsui's tonnes by name, and the product would fail the low-bid test **[L2004-003]**, **[M2017-009]**. The rows give the
route through such a field: "Another way to prosper in a commodity-type business is to be the low-cost operator."
**[L2004-007]**; "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**; "Being the
low-cost producer, for example, is a terribly important moat." **[M2018-043]**; and it is strongest in something people
must buy **[M2004-091]**. So the castle tests are run on the cost position.

**The castle tests, each with its filing fact.**
- *The attacker with money* **[M2011-015]**: a new Pilbara-scale system needs a deposit, a railway and a port, and the
  incumbents own them. Mitsui's own answer to growth was to buy into an existing deposit (Rhodes Ridge, ¥723.8 bn), which
  says the asset, not the money, is the scarce thing. The attack that matters is supply from elsewhere and falling
  Chinese demand; the report's own MMR risks are "Impact to demand for resources following Chinese economic slowdown" and
  "Impact of technological innovation and government policies on the supply, demand and commodity prices" (107th report,
  Operating Environment, (a)).
- *Pricing power and the agony before a rise* **[M2005-020]**: none. Mitsui is a price taker; ¥3.0 bn of profit moves
  with each dollar a tonne (Risk Factors (5)). The price-setter rows (**[M2012-109]**, **[M2023-079]**) describe a seller
  with no cost edge matching a rival; the low-cost seller is the one whose margin survives the rival's price.
- *Unit volume*: equity iron ore 63.8 Mt in FY2026, guided at 63 to 65 Mt through FY2029: flat until Rhodes Ridge.
- *The low-cost position* **[L1996-015]**, **[M2018-043]**: BHP's WAIO is "the world’s lowest cost major iron ore
  producer" with "a greater than US$10 per tonne cost advantage over its nearest Pilbara competitor" (BHP 20-F FY2026).
  **Contrary, written down at once** **[M1997-127]**: the nearest Pilbara competitor is the Rio Tinto system in which
  Mitsui's larger stake sits (Robe River, 33%), so most of Mitsui's Pilbara tonnes come from the second-cheapest system,
  not the cheapest. Both sit far below the price that clears the market; the trough record below is the test of it.
- *Would the customer choose it over the low bid* **[M2017-009]**: the low-cost producer is the low bid.
- *Widening or narrowing* **[M1999-108]**: BHP reports its lead held "for the seventh year"; Mitsui's volumes are flat.
  The reports name the change that could narrow it: "Progressive expansion of green steel in the steel industry through
  technological innovation" (107th report, Operating Environment, (e) Iron & Steel Products). That is slow change
  **[M2014-038]**: recorded, not resolved.
- *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**: a lasting fall in Chinese steel
  output and new seaborne supply would lower the price for everyone; neither would move the Pilbara off the bottom of
  the cost curve. What it would do to the level of returns is the open question, carried to Q7 as the cycle base.

**The competitor row.** The report names no rival by name; it names "Other Japanese global investment and trading
companies" (Risk Factors, Risk Due to Competition). The comparison set is three of them, at company level, return on
equity from each company's own report:
- **Sumitomo Corporation** (not an SEC filer; Integrated Report FY2025, "Summary of Key Financial Indicators", years
  ended March): 2016 3.2%, 2017 7.4%, 2018 12.5%, 2019 12.0%, 2020 6.4%, 2021 a loss (profit −¥153.1 bn, ROE not
  printed), 2022 16.2%, 2023 16.2%, 2024 9.4%, 2025 12.4%; the nine printed years average 10.6%.
- **ITOCHU** (not an SEC filer; Integrated Report 2026, "Trends of ROE / PBR / PER", the years it prints): 14.3%, 17.9%,
  13.4%, 15.8%, 12.7%, 15.6%, 14.6% for its fiscal years 2010, 2012, 2014, 2017, 2020, 2023, 2025.
- **Mitsubishi Corporation** (not an SEC filer): its IR site refused the automated fetch (HTTP 403); not read; recorded
  under what could not be got.
- **Mitsui** (selected financial data, 102nd and 107th reports): 2016 about −2.4% (the loss year, computed), 2017 8.61%,
  2018 10.86%, 2019 10.06%, 2020 9.69%, 2021 8.00%, 2022 17.98%, 2023 18.89%, 2024 15.29%, 2025 11.93%, 2026 10.22%;
  12.2% average for FY2017-26, 10.9% for FY2016-25.

Over the same decade Mitsui sits in the middle of its field at company level, below ITOCHU, near Sumitomo, with equity
ratios of 32% to 45% (selected data). The field of the deciding part is iron ore, and its leader's filing is used for
it (BHP, an SEC filer, 20-F accessions above).

**The parts table, with the castle of each part.**

| Part | share of 5-yr profit | castle | decides |
|---|---|---|---|
| Mineral & Metal Resources | 36.9% | low-cost Pilbara iron ore (non-operated), Vale stake, coal and copper | **yes (largest)** |
| Energy | 21.2% | LNG and oil and gas interests, price takers; Russian exposure ¥279.8 bn gross | no |
| Machinery & Infrastructure | 20.4% | power, Penske Automotive (20.3%) and truck leasing, ships, mobility | no |
| Chemicals, Lifestyle, Innovation & Corporate Development, Iron & Steel | 21.5% together | trading, healthcare (IHH), food, finance (JA Mitsui Leasing) | no |

Parts that do not decide and whose castles were not shown standing are carried to Q7 at no growth, as the convention
directs; Q7's bottom case values the whole on its owner cash at no growth.

**The field's returns over the last full cycle** (iron ore's trough was FY2016; the run reads FY2016 to FY2026). MMR,
profit attributable against segment total assets (segment notes of the 98th, 100th, 102nd, 104th, 106th and 107th
reports): FY2016 −10.2%, FY2017 7.8%, FY2018 11.4%, FY2019 7.5%, FY2020 9.5%, FY2021 7.0%, FY2022 15.6%, FY2023 14.3%,
FY2024 10.9%, FY2025 9.6%, FY2026 5.9% (Rhodes Ridge in the assets, not yet producing). Over the eleven years, ¥2,574.0 bn
of profit on average segment assets of ¥2,631.9 bn: **8.9% a year after tax on total assets, the loss year included**.
The field's leader kept EBITDA above half its revenue at the trough (BHP WAIO FY2016: US$5.5 bn on US$10.3 bn) and at 62%
in FY2026. Judged in words, as the convention asks: **excellent returns, held through a full price cycle, protected by
cost position**, which is what the rows say a moat is for, "an enduring "moat" that protects excellent returns on
invested capital" **[L2007-004]**. The deciding part's castle does not protect only ordinary returns.

**What the castle does not protect, written down** **[M1997-127]**: the level of the return, which moves with a price no
one in the business will forecast; Mitsui's share sits mostly in the higher-cost of the two Pilbara systems; MMR also
holds assets that lost money at the trough. And the company as a whole earns a return on equity in the middle of an
ordinary field: the parts that do not decide pull the whole toward the field's average. That is a finding for Q3 and
Q7, not a Q2 close, because the file closes on the deciding part.

**VERDICT: IN**, on the deciding part's low-cost castle and its full-cycle returns **[L2004-007]**, **[L2007-004]**.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital the business needs** **[M2010-090]**: company ROE 8% to 19% over FY2017-26, average 12.2%
  (Q2), on equity ratios of 32% to 45%; profit attributable against total assets about 2.7% (FY2017) to 7.5% (FY2023)
  and 4.4% in FY2026. The deciding part earns more (8.9% after tax on its assets over the cycle, Q2). Read with the
  cyclical-peak caution **[L1994-009]**: FY2022-24 were commodity-price years.
- **What goes back in to stand still and to grow** **[L1999-024]**, **[M2000-144]**: over FY2017-26 cash from operations
  averaged ¥735.7 bn, and net PP&E, businesses bought net of sold, loans, lease principal and minority transactions took
  so much of it that owner cash after all spending averaged ¥268.6 bn, about 40% of the average profit of ¥670.9 bn, and
  was negative in FY2019 and FY2026. Maintenance alone (depreciation less right-of-use depreciation, ¥241.3 bn in FY2026;
  the filer's plan: ¥227 bn a year "to strengthen existing businesses") leaves ¥504.7 bn a year over the decade, ¥672.7 bn
  over FY2022-26. The cash the owner receives "will regularly fall considerably short" of reported earnings where
  reinvestment eats it **[L2023-009]**. Equity-method profit reaches cash at about four-fifths: FY2026 share of profit
  ¥447.4 bn against dividends from equity-method investees ¥370.3 bn (MD&A, Non-current Assets).
- **What the added capital earned** **[M2001-019]**, **[M2023-081]**: equity attributable rose from ¥3,732 bn (FY2017)
  to ¥8,768 bn (FY2026), ¥5.0 tn more; average profit rose from ¥373 bn (FY2017-21) to ¥969 bn (FY2022-26). That is a
  decent return on the added sums **[L2009-012]**, but part of it is the price cycle and part is foreign exchange
  (the equity-method line alone gained ¥429.9 bn from currency in FY2026, MD&A). "We just put way more capital into the
  business" **[M2023-081]** is a fair description of the decade: total assets nearly doubled.
- **The serial-acquirer test** (Q7 specific (c)): businesses bought net of businesses sold averaged ¥81.5 bn a year over
  FY2022-26 against owner cash before purchases (equity-only) of ¥492.2 bn; with Rhodes Ridge (booked as PP&E, ¥723.8 bn)
  spread over the window as if it were a business bought, ¥226.3 bn, still under half. Not a serial acquirer by the
  convention; the default pair applies at Q7.
- **WEIGHS AGAINST**: a capital-heavy second-best business **[M2018-055]**, **[M1998-081]**, earning decent but not high
  returns on what it keeps adding, with little cash left after the spending; not the business that "gives you more and
  more money every year without putting up anything" **[M1998-081]**. (The "little or no debt" criterion is Q9's.)

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, eleven of them** **[M2025-032]** (¥ bn, March year ends; filed statements of the 98th, 100th,
102nd, 104th, 106th and 107th reports; FY2018-21 total assets from the selected data):

| FY | total assets | cash | inventories | equity-method inv. | other inv. | PP&E | intangibles | debt (ST+LT) | equity (parent) | retained | equity ratio |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 10,911 | 1,491 | 534 | 2,515 | 1,180 | 1,938 | 157 | 4,711 | 3,380 | 2,314 | 31% |
| 2017 | 11,501 | 1,504 | 590 | 2,742 | 1,337 | 1,823 | 169 | 4,802 | 3,732 | 2,550 | 32% |
| 2018 | 11,307 | 1,131 | 551 | 2,503 | 1,825 | 1,730 | 173 | 4,227 | 3,975 | 2,903 | 35% |
| 2019 | 11,946 | 956 | 608 | 2,976 | 1,948 | 1,945 | 174 | 4,625 | 4,263 | 3,079 | 36% |
| 2020 | 11,806 | 1,059 | 554 | 2,881 | 1,484 | 2,121 | 195 | 4,927 | 3,818 | 3,362 | 32% |
| 2021 | 12,516 | 1,063 | 615 | 3,044 | 1,956 | 2,175 | 189 | 4,747 | 4,570 | 3,548 | 37% |
| 2022 | 14,923 | 1,128 | 950 | 3,387 | 2,347 | 2,191 | 253 | 4,877 | 5,605 | 4,166 | 38% |
| 2023 | 15,381 | 1,390 | 941 | 3,930 | 2,134 | 2,301 | 277 | 5,041 | 6,368 | 4,841 | 41% |
| 2024 | 16,900 | 898 | 966 | 4,870 | 2,320 | 2,401 | 458 | 4,776 | 7,542 | 5,552 | 45% |
| 2025 | 16,812 | 977 | 960 | 4,973 | 2,191 | 2,470 | 505 | 4,841 | 7,547 | 5,801 | 45% |
| 2026 | 20,822 | 983 | 1,086 | 5,561 | 2,821 | 3,722 | 578 | 5,708 | 8,768 | 6,140 | 42% |

(Debt from FY2020 includes IFRS 16 lease liabilities, ¥584.9 bn at FY2026; excluding them, interest-bearing debt was
¥5,122.9 bn at March 31, 2026.)

**What moved and why.** Equity grew 2.6 times while debt grew 1.2 times, so the equity ratio rose from 31% to 42%: the
decade was financed mainly by retained profit, not borrowing. The growth is in **investments** (equity-method stakes
¥2.5 tn to ¥5.6 tn; other investments ¥1.2 tn to ¥2.8 tn, which move with the fair value of listed and LNG stakes through
other comprehensive income), and in FY2026 in **PP&E** (+¥1.25 tn, chiefly Rhodes Ridge). Intangibles and goodwill rose
from ¥157 bn to ¥578 bn (acquisitions such as AIM Services in FY2024): still small against equity. Inventories doubled
with revenue; current receivables were 19.1% of revenue in FY2020 and 16.8% in FY2026: nothing out of line with sales
**[M1995-064]**. Cash has been held near ¥1 tn. Retained earnings rose by ¥3.8 tn over the decade after ¥1.8 tn of
dividends and ¥1.4 tn of buybacks (cash-flow statements). The one item that jumped in FY2026 is current **other
financial assets, +¥1,030.7 bn**, which the MD&A ties to "Increase in margin deposits" and derivative assets, with
current other financial liabilities up from ¥653.9 bn to ¥1,806.7 bn: a commodity-derivatives and margin position that
grew in the year the Strait of Hormuz closed to transit (Operating Environment). It is explained, not hidden; it is a
Q9 matter (sudden demands for cash). What the figures cannot say **[M2025-032]**: the value and earning power of ¥5.6 tn
of equity-method stakes and ¥2.8 tn of other investments, whose own accounts were not read, and the guarantees off the
balance sheet (maximum ¥1,147.8 bn, note 25).

**The real costs.** Depreciation is charged and is real **[L2015-004]**: here ¥333.2 bn including right-of-use assets,
and owner cash charges lease principal and maintenance spending separately (Step 0); for a miner depreciation may be
short of what keeps it in place **[M2016-092]**, which is why owner cash deducts actual spending. Stock pay is expensed
and small (share-based compensation of US$88 mn in FY2026, statement of changes in equity). **Impairments recur**: ¥89.0
bn (FY2016), ¥110.8 bn (FY2020), ¥52.9 bn (FY2021), ¥67.0 bn (FY2024), ¥35.8 bn (FY2025), net of reversals (cash-flow
statements), plus equity-method impairments such as Mainstream Renewable Power (¥15.5 bn, FY2026). They are a cost of
the business, not a one-time item **[L2016-007]**, and owner cash, being cash, is untouched by them; the cash spent on
what was later impaired is inside the spending lines. EBITDA does not appear in the filer's mouth.

**The habits, recorded and carried to Q5.** (1) **Guidance**: the report publishes next year's profit (¥920 bn) and
"Core Operating Cash Flow" (¥1,050 bn) by segment, and the three-year plan sets profit, cash and ROE targets ("record-high
targets of COCF of 1.2 trillion yen, profit [...] of 1.1 trillion yen, and ROE of 12%", 107th report, Medium-term Management Plan 2029). The rows on guidance: **[L2019-006]**,
**[L2000-039]**.
(2) **An adjusted figure featured**: "Core Operating Cash Flow" leads the report's review and drives the directors'
bonus formula; it is cash from operations before working capital and after lease principal, that is, before every
investment the business makes (segment note 4; Remuneration ii)). It is defined, reconciled to the statement and never
called earnings, which is the honest end of the practice **[L2016-006]**, but it is the figure that leaves out the
capital spending that eats most of the cash (Q3). These are a weighing against **[M1994-018]**, not suspicion: no tell
in the accounts themselves (no building of prepaid or deferred accounts, no reserve movements found, inventories in line).

**Equity-method income** is counted as dividends received (the convention): owner cash starts from cash from
operations, which takes in ¥550.6 bn of dividends received in FY2026 against a share of profit of ¥447.4 bn plus
dividend income of ¥178.7 bn.

**VERDICT on the accounts: WEIGHS AGAINST** (guidance, a featured adjusted cash figure, recurring impairments), not a
STOP: the accounts do not confuse and raise no suspicion **[M1995-063]**, **[M1995-065]**. The recast owner cash in
Step 0 feeds Q7.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stock the speakers read rather than meet **[M2007-081]**; the two yardsticks are how the business is
run against the hand dealt and how the owners are treated **[M1994-008]**, **[M1994-009]**.

- **The record against the hand dealt.** The hand was a commodity cycle: from the first loss in the company's history
  (FY2016, −¥83.4 bn, with MMR −¥162.5 bn) to profit of ¥834-1,131 bn in FY2022-26, and an equity ratio raised from 31%
  to 42% while ¥3.2 tn went back to owners over the decade in dividends and buybacks. Against the field (Q2), Mitsui's
  decade of ROE is in the middle: better than Sumitomo's, below ITOCHU's printed years. The deciding part is run by
  others (BHP and Rio Tinto operate it); Mitsui's own ability shows in what it buys and sells, which the impairments of
  FY2016, FY2020-21 and FY2024 show to be uneven.
- **The reports.** The securities report explains each impairment and each large movement by name (Mainstream Renewable
  Power, JA Mitsui Leasing's loss on a factoring counterparty's Chapter 11 filing, note 28; the margin deposits; Rhodes
  Ridge), states its Russian exposure in yen (¥279.8 bn gross) and its guarantees in full (note 25). It tells the owner
  what the owner would want to know **[M1998-036]**; the strategy pages carry the plan vocabulary of a large company
  ("value creation framework", "nonlinear combinatory value"), which is a mark against **[M1998-038]**, not an integrity
  finding.
- **The habits carried from Q4**, read with the integrity record **[M2004-067]**: earnings guidance and three-year
  targets **[L2019-006]**, and a featured adjusted cash figure that also sets the bonus. Whether the targets are made
  with suspicious regularity **[L2002-041]** was not tested beyond one fact: the Q1 FY2027 presentation reports both
  measures "progressed well ahead of business plan". No sign in the accounts that numbers were made to fit (Q4).
- **Integrity record.** In the documents read (the six securities reports, the Q1 presentation, the 2026 releases): no
  investigation, sanction, restatement or fraud is disclosed; litigation is described as ordinary course with
  provisions recorded (note 25, II). The report says it complies with sanctions on Russia while staying in its Russian
  LNG business (Risk Factors (2)). **Written down, not verified** **[M1997-127]**: the analyst recalls, from outside the
  documents read, a data-falsification case at Mitsui in the early 2000s concerning diesel particulate filters sold in
  Tokyo; it is not in any document this run read and is not used. The doubt rule **[M2013-088]** is applied to what the
  record shows, and nothing in it raises a doubt about the present management's honesty.
- **Love of the business and the cheque.** The executives are employees paid a bonus formula (Q6); no founder sells.
  Nothing read bears on love of the business either way.
- **Ability** weighs neither way strongly: the deciding part's returns are the operators' and the ore body's; the
  company's own allocation record is mixed (Q3, Q6).

*Found while reading for Q7 and added here the same day* **[M1997-127]**: the 104th report says "the business targets set at
the start of each fiscal year were achieved" over the three years to FY2023, and that FY2023 profit and Core Operating
Cash Flow reached "record levels and significantly exceeding the targets". Targets met every year is the pattern that
makes the speakers "downright incredulous" **[L2002-041]**. Read with the record: the years were a commodity-price boom
the company does not control, the beat came from price and was large, not a penny over the line, and the accounts show
no tell (Q4). It weighs against; it does not raise a doubt about honesty.

**VERDICT on integrity: IN** (no doubt raised by the record read; the habits weigh against at Q4 and Q6).
**Ability: WEIGHS neither FOR nor AGAINST**, recorded as UNDECIDED **[M1994-008]**.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- **The retention test** **[R1995-009]**, **[M1998-033]**. FY2018-26: profit attributable ¥6,403 bn, dividends paid
  ¥1,684 bn, so about ¥4.7 tn kept before buybacks (cash-flow statements). Market value: about ¥2.9 tn at March 2017
  (FY2017 profit ¥306,136 mn / EPS ¥171.20 = 1,788 mn weighted shares, at the price implied by the reported PER of 9.42,
  ¥1,613; computed, labelled) against about ¥17.0 tn at March 2026 (EPS ¥291.12 × PER 20.47 = ¥5,959 on 2,847.6 mn
  shares) and ¥13.6 tn today. Each yen kept has been matched by well over a yen of market value; part of that is a
  re-rating from 0.8 times book (book per share ¥2,115.80 against ¥1,613 in 2017) to about twice book. Against intrinsic
  value, the bottom of the Q7 range on the equity (¥11.8 tn, all-equity basis) also exceeds the equity of 2017 plus what
  was kept. **Weighs FOR.** The forward question, "Can you keep using all of the capital you generate, effectively, for a
  very long time?" **[M2010-097]**, is answered by the plan: ¥970 bn of growth investment decided and ¥2.4 tn of
  "Management Allocation" to be split between investment and returns (Q1 FY2027 presentation).
- **Buybacks.** Every programme names an amount and a share count and no price: August 4, 2026, "Up to 60 million shares
  [...] Up to 200 billion yen"; November 5, 2025, "Up to 80 million shares [...] Up to 200 billion yen". The rows find a
  repurchase's worth "entirely purchase-price dependent" **[L2016-002]** and want the stock "below its intrinsic value,
  conservatively-calculated" **[L1999-023]**; "what is smart at one price is dumb at another" **[L2011-003]**. So by the
  convention the prices paid are read against the bottom of the Q7 range. Prices paid (treasury-stock tables; split-adjusted
  to today's shares): FY2023 programmes ¥1,582 and ¥1,875 a share (¥100.0 bn for 31,608,000 and ¥170.0 bn for 45,337,900
  pre-split shares); FY2025 ¥3,275 (¥400.0 bn for 122,138,700 shares, the count as the 106th report prints it after the
  July 2024 split); FY2026 ¥4,869 (¥200.0 bn for 41,075,000 shares, November 2025 to March 2026); FY2027 to September 30,
  ¥5,083 (¥42.1 bn for 8,285,900 shares). **Bottom of the Q7 range: ¥2,723 a share on the cycle base (¥4,152 on the literal window), all-equity basis; written
  back from Q7.** The FY2023 purchases (¥1,582, ¥1,875) sit below both; FY2025 (¥3,275) sits above the cycle bottom and
  below the literal one; FY2026 (¥4,869) and FY2027 (¥5,083) sit above both. **Weighs AGAINST** for the programme now running.
- **Issuance and deals** **[L2014-012]**, **[L2009-019]**: no shares issued for deals (the count has fallen every year);
  Rhodes Ridge paid in cash (¥723.8 bn); the July 22, 2026 proposal with Penske Corporation to buy PAG's free float
  (US$210 a share, US$3.8 bn for both buyers) is non-binding, to be paid with "new equity as well as [...] debt financing
  from one or more third parties", that is the buyers' cash and borrowing, not Mitsui stock. **The all-stock STOP does
  not apply.** The Penske price was not tested against PAG's value (outside this run's scope; recorded under Q9 facts).
- **Dividends** **[M2004-089]**, **[L2012-015]**: a progressive policy with a floor of ¥140 a share and total returns set
  at "the 50% level" of Core Operating Cash Flow over the plan. Clear and consistent, but a ratio, which the rows call
  "nuts" as a way to set a payout **[M2000-051]**; and the ratio is set on the adjusted figure that is before investment.
  Weighs slightly against.

**Part B, the pay, the board and the owners.**
- **Pay** (107th report, Corporate Governance (4)): directors' basic pay, a cash bonus of 0.12% of profit and of Core
  Operating Cash Flow (half each) times a position coefficient (capped at ¥1.5 bn in total), performance-linked restricted
  stock on three-year ROE and ESG measures, and tenure-linked restricted stock. Eight internal directors received
  ¥2,491 mn in FY2026 against profit of ¥834.0 bn. The bonus rises with profit and cash flow whatever capital was added to
  earn them; the rows ask for a charge on incremental capital **[L1994-019]** and warn against "a royalty on money that you
  left with me" **[M1997-043]**; the ROE leg of the stock award partly answers that. Pay is tied to whole-company results,
  which for the top officers is what they control **[M2003-019]**. The Remuneration Committee, chaired by an external
  director, sets levels "based on trends at other companies", the comparative-data habit the rows distrust **[L2005-015]**.
  Weighs slightly AGAINST; the sums are small against the business.
- **The board**: twelve directors, six external; the chair and the president are separate offices (bonus coefficients
  list both), so the chair-and-CEO concern **[L2014-026]** does not arise. Clawback provisions exist.
- **The owners**: the report gives the owner what an owner needs (Q5), and treats holders alike; guidance (Q4) is the
  departure from the speakers' own practice **[M2016-002]**.

**WEIGHS**: Part A **UNDECIDED** (retention for; the current buyback above the bottom of the value range, and a ratio dividend,
against; no STOP; completed at Q7). Part B **slightly AGAINST** (no capital charge in the bonus; peer-set levels).

## Q7: WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**, **[M1996-025]**, as a range
**[L2000-024]**; the floor (CONVENTION) about ten percent on owner cash after the company's own tax **[M2003-149]**,
**[L2002-020]**, **[M1994-004]**. Arithmetic: `Test Runs/_research 2026-10-12 MTSUY/scripts/valuation.py` (literal
window) and `valuation_cycle.py` (cycle base), from `owner_cash.py` (Step 0).

**Inputs.** Owner cash after the company's tax, from cash from operations (dividends received in place of the share of
investees' profit; working capital counted, specific (d)), all-equity basis (interest paid added back after tax at the
31.5% statutory rate) against market value plus net debt; equity-only beside. Market value ¥13,560.6 bn; net debt
¥4,458.8 bn (June 30, 2026 plus the buyback since; leases out, their principal charged in owner cash); enterprise value
**¥18,019.4 bn**. Sovereign 4.14% (30-year JGB, MOF, 2026-10-08). Shares 2,839.9 mn.

**The specifics, applied.**
- *(a) Cycles.* The window FY2022-26 opens on a commodity peak: profit of ¥914.7 bn in FY2022 and ¥1,130.6 bn in FY2023,
  which the filer calls "record levels" (104th report, Achievements of Quantitative Targets) **[L2005-003]**,
  **[L2003-004]**. The base is therefore the cycle, FY2017-26 (the year after the FY2016 trough to the latest year)
  **[M2011-101]**; the literal window is shown beside. Only one cycle lies in the filings read, so growth is measured
  between the cycle's halves, FY2017-21 against FY2022-26 (specific (b)'s fallback), which gives 14.8% a year on
  maintenance-only owner cash (12.6% a year inside the literal window, FY2022 to FY2026).
- *(f) The cap.* Carried ten years, 14.8% would need owner cash of 14.4% of FY2026 revenue; the highest share in the
  filings read is 5.4% (FY2023, FY2025). Cut to the business's own sales growth: 6.6% a year, FY2019-26 (revenue is not
  comparable before FY2019, when IFRS 15 changed its basis); 4.45% a year inside the literal window **[M1999-067]**,
  **[M1997-095]**.
- *(e) Growth spending.* The filing allows the maintenance guess (depreciation less right-of-use depreciation; the
  filer's own plan line "Investments to strengthen existing businesses", ¥227 bn a year) **[M2000-144]**, **[L1999-024]**,
  so the central case is maintenance-only owner cash, with growth spending charged against the growth it buys. Because
  the growth is capped, only the share of growth spending that buys the capped growth is charged (CONVENTION of this run:
  growth spending × capped rate ÷ shown rate; rationale: specific (e) forbids charging all spending and also capping the
  growth it bought, and gives no rule for the part; proportion is the least invented split). All-spending cases beside.
- *(c) Acquisitions.* Businesses bought net of sold are inside the spending; not a serial acquirer (Q3). Rhodes Ridge
  (FY2026) is inside the spending; it produces nothing yet and is credited only through the capped growth. The Penske
  proposal is non-binding and unsigned at the price date: left out, said so.
- *(d) Working capital* is inside cash from operations. *Tax*: the company's own; FY2026's effective rate was 20.5%
  against a statutory 31.0% (note 23), the gap being dividend and equity-method tax effects and resource taxes, not a
  carryforward that runs out, so no shelter is priced separately.

**COMPUTATION of the cases** (¥ per Tokyo share; all-equity basis, equity-only in brackets):

| Case | base ¥ bn/yr | growth 10 yrs | at the 30-yr JGB 4.14% | at 10% (floor test) | clears the floor at ¥4,775? |
|---|---|---|---|---|---|
| **Cycle base FY2017-26, no growth, maintenance only (bottom)** | 504.7 | 0 | **2,723** [3,677] | 207 [1,522] | no (implied return 2.8%) |
| **Cycle base, capped growth, its growth spending charged (top)** | 432.1 | 6.6% | **4,796** [5,299] | 824 [1,993] | no (implied return 4.15%) |
| beside: cycle base, all spending, capped growth | 341.0 | 6.6% | 3,453 [3,956] | 319 [1,488] | no |
| beside: literal window FY2022-26, no growth, maintenance only | 672.7 | 0 | 4,152 [4,927] | 799 [2,040] | no (3.7%) |
| beside: literal window, capped growth, charged | 613.2 | 4.45% | 5,999 [6,415] | 1,359 [2,483] | no (4.9%) |
| beside: literal window, all spending, capped growth | 504.2 | 4.45% | 4,653 [5,069] | 838 [1,962] | no |
| beside: literal window, shown growth 12.6%, no growth spending charged (breaks (e) and (f)) | 672.7 | 12.6% | 14,672 | 4,126 | no |
| beside: halves growth 14.8%, no growth spending charged (breaks (e) and (f)) | 672.7 | 14.8% | 17,869 | 5,100 | yes, by 5% |

**The floor, tested first.** No case the specifics allow earns the floor at the price: at ¥4,775 the expected return
on the whole business runs from 2.8% (cycle bottom) to 4.9% (literal-window top), against about ten percent. The only
arithmetic that clears it credits fifteen percent a year for ten years on the window's peak base while charging nothing
for the spending that would buy that growth, which breaks two specifics at once. On owner cash after interest (equity
only, beside, never deciding alone) the literal-window top case is worth ¥2,483 a share at ten percent, about half the price. "So,
there’s just a point at which we drop out of the game." **[M2003-149]**. The rows that rest the floor on cheap money
moving it "a little" **[M2016-078]** do not close a gap of this size, and the yen's long rate at 4.14% is not cheap money.

**Value range (the reporting figure, Q7's range convention in full):** **¥2,723 to ¥4,796 a share** on the cycle base
(all-equity; width 1.76 to one), against the price of ¥4,775; the literal window beside, ¥4,152 to ¥5,999 (width 1.44).
Per ADS (20 shares, ¥158.68 to the dollar): $343 to $604 on the cycle base ($523 to $756 literal), against the Tokyo price's
ADS equivalent of $602 and the ADR's $610.70. The range is narrower than three to one, so it is not TOO HARD on width; the
price sits inside it, near the top; and no case clears the floor.

**Fair price (a reporting figure, never a verdict; Part VII):** the two ends valued at ten percent and averaged:
**¥516 a share** on the all-equity basis, cycle base (ADS $65); **equity-only ¥1,758** (ADS $222). Literal window beside:
¥1,079 all-equity (ADS $136), ¥2,261 equity-only (ADS $285). Tax: the company's own, no conversion. The all-equity figure
sits far below the equity-only one because net debt of ¥4.46 tn is charged in full while the after-tax interest it costs
(about ¥94 bn a year over FY2022-26) is under three percent of it: the lenders take the first ¥4.46 tn of a business
worth ¥5 to 7 tn at ten percent. No cheap price is reported.

**How sure, how soon.** The price of ore and gas sets most of the cash and no one in the business will forecast it (Q1);
the margin asked grows as certainty falls **[M1997-080]**; and a wide margin is not available here at all, since the
price sits inside the range. "If you need to use a computer or a calculator to make the calculation, you shouldn’t buy
it." **[M2009-005]**.

**VERDICT: OUT.** No case earns the floor at the price (the floor tested first), and the price sits inside a range
narrower than three to one: not a screamer **[M2003-149]**, **[M2009-005]**, **[M1996-084]**.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file).

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7**: no case the range convention allows earns the floor of about ten percent at ¥4,775 (expected return 2.8%
to 4.9% on the whole business), and the price sits inside a range narrower than three to one. **Value range ¥2,723 to
¥4,796 a share** (cycle base FY2017-26, all-equity; literal window FY2022-26 beside, ¥4,152 to ¥5,999) **against ¥4,775**
(Tokyo close 2026-10-09). Q1 IN (by parts, Mineral & Metal Resources decides), Q2 IN (low-cost Pilbara iron ore,
full-cycle returns excellent), Q3 against, Q4 against (weighing), Q5 integrity IN, Q6 undecided / slightly against.
Ticker note: the run is of Mitsui & Co. (8031, ADR MITSY); "MTSUY" is Mitsubishi Corporation's ADR.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Q7 closed the file; written down, not weighed; the box unchanged **[M1997-127]**.)*
- **Q8 (the bond).** The 30-year JGB yields 4.14% (MOF, 2026-10-08); the expected return on the business at the price,
  on the cases of Q7, is 2.8% to 4.9% (`valuation_cycle.py`, `valuation.py`).
- **Q9 (debt and exposures).** Interest-bearing debt excluding leases ¥5,303.1 bn and net ¥4,416.7 bn at June 30, 2026
  (net debt-to-equity 0.49, Q1 FY2027 presentation); lease liabilities ¥584.9 bn (note 6). Long-term funds of "around 10
  years" with maturities spread (Risk Factors (9)); current portion of long-term debt ¥509.5 bn and short-term debt
  ¥166.2 bn at March 31, 2026, against cash of ¥982.7 bn. **Margin deposits and derivative positions**: current other
  financial assets rose ¥1,030.7 bn in FY2026, which the MD&A ties to "Increase in margin deposits" and derivative assets;
  current other financial liabilities rose from ¥653.9 bn to ¥1,806.7 bn. That is collateral posted against commodity
  derivatives, the "sudden demands for large sums" the standing rule names **[L2014-024]**, **[M2012-032]**, on Mitsui's
  own balance sheet. **Guarantees**: maximum potential ¥1,147.8 bn, of which ¥249.8 bn within a year (note 25).
  **Russia**: gross exposure ¥279.8 bn (Risk Factors (2); note 27 on the Russian LNG business). **Equity-method and FVTOCI
  stakes** ¥8.4 tn whose own accounts were not read. **Penske proposal**: Mitsui's share of US$3.8 bn, financed by equity
  and third-party debt, not yet agreed. Credit risk on ¥2,344.5 bn of current receivables (Risk Factors (8)). A financial
  arm sits inside (JA Mitsui Leasing, equity-method; a factoring counterparty's Chapter 11 filing caused a FY2026 loss,
  note 28), and the "little or no debt" criterion **[R1997-001]** would be read against all of the above.
- **Q10.** Nothing found.
- **Q12.** Coal (metallurgical and thermal) and oil and gas are among the businesses; Russian LNG continues under the
  sanctions regime; none is a business the rows name for the STOP.
- No integrity fact bears on Q5 beyond what Q5 recorded (Q5 was reached and answered).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template copy was the second command of the run, before the first
      download); written question by question; committed after each (Step 0, Q1, Q2, Q3, Q4, Q5, Q6, Q7, close).
      Exceptions, confessed: the Q7 arithmetic was run (as computation) before Q3 to Q6 were written, and Q6's retention
      paragraph quotes the bottom of the Q7 range (¥11.8 tn) in the text committed with Q6; the buyback line itself was
      left as a placeholder and written back with Q7, as the brief asks. A Q5 note found while reading for Q7 was added to
      Q5 the same day and marked so; the Step 0 ten-year averages were corrected with a dated note.
- [x] Dispatched run: the brief allowed the per-question commits; the lock is the dispatching session's; the fold is
      the dispatcher's. The run binds nothing until it is in the register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened. **Not fully kept on listing**: my first command
      was a filtered listing of `Test Runs/` for the ticker, which printed four file names about this company (declared
      at the top under contamination; none opened, none used).
- [x] Every v5 id checked against `principle_ledger_v5.csv` and every quoted fragment beside an id checked against its
      row by `Test Runs/_research 2026-10-12 MTSUY/scripts/check_citations.py`; every filing fact names its document and
      date (no accession numbers exist for a Japanese securities report; the BHP 20-F accessions are given).
- [x] The order was kept; Q7 was the first STOP to fail and closed the run; Q8 onward are facts, not clearances.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; the sovereign from
      the Japan Ministry of Finance; aggregator quotes flagged (price, ADR, FX).
- [x] Contrary evidence written down as found (foundations, Q1, Q2, Q4, Q5); facts for later questions under AFTER THE
      STOP; no integrity flag needed in the box line, since Q5 was answered.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` and `cover_shares.py` returned nothing usable (not an SEC filer); no line of theirs was used.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the reply).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The parts test asks for "operating profit" and a Japanese trading house reports segment profit after tax.** I used
profit attributable to owners by segment, the only segment profit the report gives, and said so; the convention should
say what to use when a filer reports no segment operating profit. (2) **Specific (e) and the cap collide.** Specific (e)
says never to charge all growth spending while capping the growth it bought, and (f) cuts the growth to sales growth;
neither says how much spending to charge for the capped growth. I charged it in proportion (capped rate over shown rate)
and confessed it as a CONVENTION of this run; the framework should choose. (3) **Specific (a) with one cycle.** The
window opens on a peak, so the base is "the last full cycle", but the filings read hold one trough (FY2016) and no second
trough or second peak, so "growth between successive cycles" cannot be measured; I used the cycle's halves (specific
(b)'s fallback). (4) **Equity-method income as dividends**: for a company whose dividends received include FVTOCI
dividends and whose share of profit includes currency translation, the convention is workable through cash from
operations, but it leaves ¥8.4 tn of stakes valued only through what they pay out; the convention could say so. (5)
**The all-equity fair price is very sensitive to net debt** when the floor is far above the cost of debt: here
¥516 against ¥1,758 equity-only; the reporting convention might note when the two diverge by more than threefold. (6)
**Q5's ability verdict** offers FOR or AGAINST only; the record here pointed neither way and I wrote UNDECIDED. (7) **The
brief's ticker**: "MTSUY" is Mitsubishi Corporation's ADR; the canonical brief has no step that checks the ticker
against the company before dispatch.
