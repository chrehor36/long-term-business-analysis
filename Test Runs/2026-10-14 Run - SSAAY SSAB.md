# Company Run — SSAB AB (Nasdaq Stockholm: SSAB B / SSAB A; ADR OTC: SSAAY) — 2026-10-14
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession (here, for a non-SEC filer,
the document and its date); a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.
Copied to this dated name before any fetch (commit 55d88f2b).

Dispatched blind run. Research folder: `Test Runs/_research 2026-10-14 SSAAY/` (notes, fetch and arithmetic scripts;
the filings themselves sit in its ignored `cache/` subfolder).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-14), after the run was committed: not held (`PORTFOLIO.md` carries no line for SSAAY, SSAB A, SSAB B or SSAB).

**CONTAMINATION, declared.** Before any reading, the session context showed me: (1) the subjects of the five most recent
commits, which are the overnight run and fold of OUTKY (Outokumpu, a stainless steel producer, another company), including
the words "OUT at Q2 (Europe decides on a knife edge ... a high-cost producer whose price Asian imports set ...)"; (2) the
memory index lines that the v4.1 wave queue was paused with "57 gate-clearers, nothing buyable" and that holding reviews
are owed (no names); (3) research-folder names of other runs in the git status (AYI, ARCB), not opened; (4) the
`_overnight.lock` file name in `Screens/_daily/` when I listed it to see whether a lock was held. None of it concerns SSAB,
and none of it is used. The OUTKY subject is the one that could steer me, since it is a European steel producer closed at
Q2 by a parts reading: I note it so the reader can weigh whether my Q2 reading followed it. I reached my Q2 reading on SSAB's
own segment figures and on the US rivals' filings, and the deciding part here is SSAB Americas, not SSAB Europe.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** SSAB B **SEK 102.20**, SSAB A SEK 101.45 (Nasdaq Stockholm closes 2026-10-13; Yahoo Finance chart API,
  an aggregator, flagged under operator rule 5). ADR SSAAY USD 5.27 (last trade shown 2026-10-13, OTC, thin and possibly
  stale; aggregator, flagged). SEK/USD 0.1005 (Yahoo, 2026-10-14, flagged).
- **Shares by class:** 996,617,667 shares, of which 295,966,330 class A (one vote) and 700,651,337 class B (one tenth of a
  vote), same rights to assets and result; "SSAB holds no treasury shares" after the cancellation of the 33,217,659 shares
  bought in 2023-2024 (Annual Report 2025, Board of Directors' report and The share, pp. 54 and 184). The interim report
  for Q2 2026 (dated 2026-07-22) gives an average of 996.6 million shares outstanding in Q2 2026, so no change since the
  annual report. `python Screens/cover_shares.py SSAAY` returns "NOT AN SEC REGISTRANT"; `python tools/run.py SSAAY`
  returns "not an SEC filer ... UNRESEARCHED, not UNKNOWABLE"; both tools give nothing, as expected, and all arithmetic
  below is done from the annual reports.
- **ADR ratio:** EDGAR CIK 0001437040 holds two 2016 facilities. Citibank, F-6EF filed 2016-02-02, accession
  0001193805-16-002421: "each ADS representing the right to receive one-half (1/2) of one A share of SSAB AB".
  JPMorgan, F-6EF filed 2016-12-06, accession 0001193805-16-004351: "each American Depositary Share representing one-half
  of one ordinary share". **I rely on the Citibank facility** (the "A" in the ticker and its A-share wording; I could not
  confirm from EDGAR which facility trades as SSAAY, and both give the same ratio). **1 ADS = 0.5 share.** Check: A share
  SEK 101.45 x 0.1005 x 0.5 = USD 5.10 against the USD 5.27 quote.
- **Market cap:** 295.97m x SEK 101.45 + 700.65m x SEK 102.20 = **SEK 101,632m**.
- **Sovereign for the earnings currency (SEK):** **3.178%**, Sveriges Riksbank series SEGVB10YC, Swedish government bond
  10 years, observation dated 2026-10-12 (Riksbank SWEA API, the issuing authority's central bank publication). The ten-year
  is the longest maturity the Riksbank publishes in its government-bond series (its list holds 2, 5, 7 and 10 years); the
  Debt Office issues a few longer bonds but publishes no long yield series I could fetch, so the ten-year is used, said so.
- **Filings read** (operator rule 4; no accession numbers exist, so the document and date are recorded): SSAB Annual
  Report 2025 (ssab-annual-report-2025.pdf, ssab.com, posted 2026-03-17); Annual Reports 2024, 2023, 2021, 2020, 2018 and
  2016 (their prior-year columns supply 2022, 2019, 2017 and 2015); Interim report Q2 2026 (2026-07-22). The 2022 and 2019
  reports were not found at the URL patterns I tried; their figures come from the next year's comparatives.
- **One figure cross-checked against the filed statement:** operating result 2025 SEK 6,116m appears identically in the
  consolidated statement of cash flows (first line), the segment table of note B.1 (total) and the 10-year summary; cash
  flow from operating activities 2025 SEK 10,079m in the cash flow statement equals the figure in note A.3's reconciliation.
- **`tools/run.py` arithmetic lines:** none (not an SEC filer). Owner cash is computed by hand in
  `Test Runs/_research 2026-10-14 SSAAY/owner_cash.py` from the filed cash flow statements, every input listed in the script.

**Owner cash after every real cost, SEK m** (cash from operating activities, which is after interest paid and received, tax
paid and the change in working capital; less investments in intangible and tangible fixed assets net of sales of such
assets, which nets the emission allowances the filer buys and sells through these same lines; less acquisitions net of
divestments; less lease principal, taken as the total lease cash outflow less lease interest, from 2019 when IFRS 16 began.
"All-equity" adds back interest paid other than lease interest, less interest received, after tax at the Swedish statutory
20.6%, a CONVENTION of this run, rationale: the group is Swedish-domiciled and the filer states no blended rate for interest).

| Year | CFO | net capex | net acquisitions | lease principal | **equity-only** | **all-equity** | strategic capex (filer) | maintenance capex (filer) |
|---|---|---|---|---|---|---|---|---|
| 2016 | 3,297 | 1,281 | 46 | n.a. | 1,970 | 2,759 | 273 | 1,053 |
| 2017 | 6,650 | 1,552 | 10 | n.a. | 5,088 | 5,837 | 237 | 1,366 |
| 2018 | 6,750 | 2,309 | -65 | n.a. | 4,506 | 4,936 | 397 | 1,943 |
| 2019 | 5,341 | 2,924 | 1,022 | 690 | 705 | 965 | 1,035 | 1,875 |
| 2020 | 4,366 | 2,090 | 90 | 614 | 1,572 | 1,901 | 582 | 1,622 |
| 2021 | 14,873 | 2,147 | 130 | 615 | 11,981 | 12,176 | 835 | 2,053 |
| 2022 | 18,156 | 3,411 | 433 | 679 | 13,633 | 13,546 | 1,952 | 2,196 |
| 2023 | 21,473 | 5,303 | -9 | 661 | 15,518 | 15,009 | 1,889 | 2,585 |
| 2024 | 11,896 | 6,569 | 38 | 713 | 4,576 | 4,054 | 2,601 | 2,773 |
| 2025 | 10,079 | 10,812 | -5 | 776 | **-1,504** | **-1,538** | 7,215 | 2,907 |

Five-year average 2021-2025: equity-only 8,841, all-equity 8,649; after maintenance only (strategic added back): 11,739 and
11,548. Ten-year 2016-2025: equity-only 5,804, all-equity 5,964; maintenance only 7,506 and 7,666. Stock pay: none in
shares; the long-term incentive is cash-based and expensed ("SSAB had no share-based remuneration programs for payout in
2025", AR 2025 p. 48), so it is inside CFO already.

**The balance sheets, 2015 to 2025, read before the income account** **[M2025-032]** (consolidated statements of financial
position; SEK m; goodwill and other intangibles shown as filed; net debt here is borrowings less cash and current
interest-bearing receivables, leases left out):

| Dec 31 | Goodwill + intangibles | Inventories | Receivables | Cash | Borrowings | Lease liabilities | Total equity | Total assets |
|---|---|---|---|---|---|---|---|---|
| 2015 | 27,871 + other | 12,691 | 6,048 | 2,711 | 27,111 | n.a. | 44,441 | 85,158 |
| 2016 | 29,909 + other | 15,001 | 7,118 | 3,879 | 23,248 | n.a. | 52,940 | 90,913 |
| 2017 | 27,730 + 1,918 | 16,035 | 7,822 | 4,249 | 18,064 | n.a. | 53,294 | 87,476 |
| 2018 | 29,994 + 1,444 | 19,813 | 8,784 | 2,598 | 13,216 | n.a. | 59,514 | 92,487 |
| 2019 | 32,508 (all intangibles) | 20,391 | 6,945 | 3,591 | 12,609 | 2,629 | 60,417 | 93,978 |
| 2020 | 28,896 | 17,444 | 6,905 | 7,051 | 14,991 | 2,453 | 54,096 | 88,601 |
| 2021 | 31,455 | 25,599 | 10,870 | 13,796 | 9,922 | 2,590 | 73,508 | 112,019 |
| 2022 | 1,416 | 37,907 | 12,048 | 24,900 | 8,173 | 2,504 | 67,191 | 109,711 |
| 2023 | 1,496 | 32,485 | 10,673 | 28,916 | 7,710 | 2,912 | 67,948 | 107,839 |
| 2024 | 1,520 | 31,780 | 9,696 | 27,810 | 6,996 | 3,156 | 71,015 | 110,728 |
| 2025 | 2,009 | 28,301 | 9,388 | 22,766 | 8,420 | 2,923 | 67,821 | 106,129 |
| 2026-06-30 | 2,240 | 28,876 | 13,425 | 19,657 | 7,395 | 3,462 | 70,849 | 111,607 |

What moved and why, in the filings' own terms. (1) **Goodwill of about SEK 30bn, from the IPSCO acquisition (2007) and the
Rautaruukki combination (2014), sat on the books until 2021 and was written down by SEK 33,291m in 2022**, "primarily
related to the acquisitions of Ipsco and Rautaruukki" (AR 2023, note C.1), split SSAB Special Steels 18,139, SSAB Americas
12,401, SSAB Europe 2,209, Tibnor 542. It was written off in the group's record earnings year, so the write-down says
what the purchase prices were worth, not what the year earned. Equity before 2022 was therefore about half goodwill; the
tangible equity has stayed near SEK 66-70bn since. (2) **Debt fell from SEK 27bn (2015) to SEK 7-8bn (2022-2025), and cash
rose from SEK 2.7bn to a peak of SEK 28.9bn (2023)**; the turn came from the 2016 rights issue (SEK 4,907m, AR 2016,
statement of changes in equity) and the 2021-2023 earnings. The cash is now being spent on the Nordic transformation: it
fell to SEK 19.7bn by mid-2026 while net cash fell from SEK 18.2bn to SEK 8.6bn on the filer's definition. (3)
**Inventories rose from SEK 12.7bn (2015) to SEK 37.9bn (2022)**, against revenue that went from SEK 55bn to SEK 129bn;
inventory stayed near 29-30% of revenue in the peak year and in 2025 (28,301 against 96,220), so the stock moved with
prices and volumes, not ahead of them. Receivables are near 10% of revenue throughout. (4) **Retained earnings and
reserves**: equity attributable to owners went from SEK 44.4bn to SEK 67.8bn over ten years while SEK 33bn of goodwill was
written off and about SEK 27bn of dividends and buybacks paid since 2018 (dividends 1,030 + 1,545 + 5,406 + 8,960 + 4,983
+ 2,591, buybacks 1,292 + 1,215, from the cash flow statements); the shares grew from 549m to 1,030m in the 2016 rights issue
and fell to 996.6m after the 2023-2024 buyback. (5) **What the figures cannot say**: the balance sheet carries no line for
the SEK 47bn of committed transformation spending (capex plan, AR 2025 p. 94: "Potentially taxonomy-aligned capital
expenditure within the next five years 46,968", which "corresponds to investment decisions for Oxelösund of SEK 6.2 billion
... as well as investment decisions for Luleå of EUR 4.5 billion less already paid capital expenditure"); investment
commitments at year-end were SEK 3,350m (note C.1), and the EUR 2.7bn Luleå loan package was signed in 2025 and is
undrawn (note D.3). Contingent liabilities were SEK 18,796m at 2026-06-30, mostly parent guarantees of subsidiaries'
obligations "primarily related to ... the Luleå investment" (AR 2025, note E.4).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own SSAB "if the market closed for five years"
**[M1997-109]**, which makes the question the business's cash over a steel cycle and a five-year building programme, not
the quotation. The market serves and does not instruct **[M2006-077]**: a class B price that rose 59% in 2025 (AR 2025, The share) and
a further 47% in 2026 to date (SEK 69.66 to 102.20) tells me nothing about value. No macro forecast enters **[M2000-094]**: the EU trade measures of 1 July 2026, the US
tariffs and the CBAM are facts the filings report, and I do not forecast them; where the castle rests on them, Q2 says so as
a fact about what holds the castle up, not as a forecast. Who is paid to tell me **[M2020-037]**: the only prices I used are
an aggregator's quotes, flagged. The analyst's habits: the margin must "scream" **[M1996-084]**, and temperament over
intellect **[M2004-035]**. **Contrary evidence, written down as found** **[M1997-127]**: (a) SSAB Special Steels holds
"a market share of over 30% in wear steels" with brands (Hardox, Strenx, Armox, Toolox) and earned an operating margin of
19% even in 2025 (4,958 on 26,352), which is a real castle in a steel company; (b) SSAB Americas' operating margin was
above Nucor's steel mills segment in 2022, 2023 and 2024; (c) SSAB states its "North American steel mills have both modern
technology and a leading cost position" (AR 2025, CEO letter); (d) the price per share is far below the range at the
sovereign rate (Q7 computation below), which tempts a reader to look past Q2. Each is weighed where it belongs.

## THE STANDING RULE
A part-interest bought for cash in a listed share, unlevered and sized by the buyer, carries no road to the buyer's ruin:
no borrowing that can call, no collateral, no sudden demand for large sums **[M2012-081]**, **[L2014-024]**,
**[L2023-005]**. The rule is met by the buyer's conduct; nothing in the target changes it.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**What the filings say the business is.** "A steelmaker since 1878, SSAB operates facilities in Sweden, Finland, and the
United States" (AR 2025, Board of Directors' report, p. 51). Five reporting segments (note B.1): SSAB Special Steels
(quenched and tempered and advanced high-strength steels; Oxelösund and Mobile; "a market share of over 30% in wear
steels"), SSAB Europe (strip, plate and tube from Luleå, Borlänge, Raahe and Hämeenlinna), SSAB Americas (heavy plate from
the Mobile, Alabama and Montpelier, Iowa scrap-based mills), Tibnor (Nordic distribution) and Ruukki Construction.

**Lines of evidence, chosen from the report's equivalents of Item 1, Item 1A and Item 7** (departure from the canonical
brief, as instructed): from the business-segment pages (Item 1): segment revenue and operating result 2016-2025, shipments,
named competitors per segment, customers (distributors, heavy transport, energy, construction, automotive) and raw
materials (iron ore from LKAB at index-linked prices, coking coal on annual contracts, scrap on the spot market for the US
mills). From the risk section of the Board of Directors' report (Item 1A): "The steel markets are highly competitive",
energy and permitting risk for the transformation, raw-material price risk, import pressure. From the Board of
Directors' report and segment discussion (Item 7): price and cost bridges (2025: "Price and product mix -6,540", "Variable
costs 4,000"), the transformation projects (Oxelösund electric arc furnace, start Q2 2027; Luleå mini-mill, start "at the
end of 2029"), the capex plan, financing (EUR 2.7bn green loans, SEK 2.8bn green bonds 2025), acquisitions and goodwill
(IPSCO, Rautaruukki, the 2022 write-down; Blastech 2025; Ovako Metals Oy, approved April 2026), the 2023-2024 buyback and
its prices, remuneration (cash STI and LTI, no share plans), and legal matters ("from time to time involved in various
legal disputes with customers, suppliers, and employees"; no named investigation found in the 2025 report by a search for
investigation, litigation, cartel, competition authority, fine and penalty). Pricing through the last inflation is read
from the segment revenue and margins of 2021-2023.

**The parts, and which matter (Q1's holding-company paragraph, with Q2's threshold):** SSAB Americas carried 38.6% and
SSAB Special Steels 35.6% of the five segments' summed operating result over 2021-2025 (Q2 table), so no part carries more
than half and the largest, **SSAB Americas, decides**; it is the part that "matters" here. On the IFRS figures (which
put the 2022 goodwill write-down into the segments) Americas is also the largest, 39.9%.

**The test applied to SSAB Americas.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**.
The key variables **[M1998-044]** are few and reported every year: tonnes shipped (1.7-1.8 million tonnes a year since the
2021 reorganization), the plate price against scrap, the mills' cost against rivals', and the capacity the rivals add.
None is a fast-moving technology: the electric arc furnace and Steckel mill are decades old, and the filer calls its US
mills modern. The product's dependence on a commodity price is not by itself a STOP here: the speakers "don’t think we can
predict commodity prices" **[M2016-025]** and still decide "off the figures" **[M2008-069]**, and Q1 asks whether the
business can be understood from its figures, which ten years of segment reports allow. The economics can be pictured: a
US heavy-plate maker selling mostly to distributors and fabricators at prevailing prices. Whether that picture is a good
one is Q2's question, not Q1's. The non-deciding parts are also understandable in this sense; SSAB Europe's coming
change of process (blast furnace to electric arc furnace in Luleå and Raahe) is a change in its cost, read at Q2 and Q7,
and does not make SSAB Europe's industry one of rapid technological change in the sense of **[M1999-063]**.

**Do I doubt that it is inside?** **[M2002-092]** Not for Americas: the business is simple and its figures are reported
by segment for ten years. Abroad, the governance and tax are readable: Swedish company law, a Swedish annual report in
English, statutory tax rate stated.

**VERDICT: IN.** The deciding part, SSAB Americas, is a plate mill whose economics can be read off its figures
**[M2008-069]**, **[M2011-014]**, with its key variables known and reported **[M1998-044]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (Q2, A business of parts, CONVENTION of the framework: a part decides at more than half of five-year
operating profit, or else the largest decides). Operating result by segment, SEK m, as the filer reports it (the main
segment measure is "the adjusted operating result, which excludes the items affecting comparability", note B.1; 2021 from
AR 2021, 2022-2023 from AR 2023 adjusted, 2024-2025 from AR 2025, where adjusted equals reported):

| Segment | 2021 | 2022 | 2023 | 2024 | 2025 | Sum 2021-25 | Share | Castle (below) | Decides |
|---|---|---|---|---|---|---|---|---|---|
| SSAB Americas | 5,412 | 12,262 | 9,651 | 2,883 | 2,167 | 32,375 | **38.6%** | open | **yes (largest)** |
| SSAB Special Steels | 4,624 | 8,217 | 6,752 | 5,297 | 4,958 | 29,848 | 35.6% | stands on the evidence read (after the stop) | no |
| SSAB Europe | 8,095 | 8,535 | 1,183 | 714 | 78 | 18,605 | 22.2% | open (the filer's own words, after the stop) | no |
| Tibnor | 1,533 | 434 | -220 | 81 | 37 | 1,865 | 2.2% | distributor | no |
| Ruukki Construction | 599 | 524 | -6 | 50 | 52 | 1,219 | 1.5% | not read | no |
| Sum of segments | | | | | | 83,912 | 100% | | |

On the IFRS figures, which charge the 2022 goodwill write-down to the segments (SSAB Special Steels -10,202, SSAB Americas
-139 in 2022), SSAB Americas is still the largest part (19,968 of 50,042, 39.9%). **SSAB Americas decides.** The margin
between it and SSAB Special Steels is three points on the adjusted figures, and I say so in the box line.

**What SSAB Americas is.** Heavy plate from two scrap-fed electric arc furnace mills, Mobile (Alabama) and Montpelier (Iowa).
Revenue 2025 SEK 21,173m, shipments 1,835 thousand tonnes (AR 2025, segment pages). "SSAB Americas' main competitors are
American steelmakers like Nucor, Cleveland-Cliffs, Orion, Algoma Steel and imported products." The US mills "source scrap
metal on the spot market". In 2025 "prices weakened on the North American heavy plate market. Steel distributor customers
were cautious whereas activity in the Energy customer segment was good." The filer's claim: "Our North American steel
mills have both modern technology and a leading cost position" (CEO letter, AR 2025).

**SSAB Americas over the span read, from the filer's segment tables** (2016-2020 excluding items affecting comparability and
the surplus depreciation on the IPSCO purchase; 2020 as restated in AR 2021):

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Revenue, SEK m | 10,639 | 12,727 | 16,878 | 17,460 | 13,239 | 20,680 | 32,163 | 29,775 | 22,708 | 21,173 |
| Operating result, SEK m | 737 | 183 | 1,837 | 2,128 | -257 | 5,412 | 12,262 | 9,651 | 2,883 | 2,167 |
| Operating margin | 6.9% | 1.4% | 10.9% | 12.2% | -1.9% | 26.2% | 38.1% | 32.4% | 12.7% | 10.2% |

On the IFRS basis, with the surplus depreciation charged, 2017 was a loss of SEK 530m and 2018 SEK 1,065m (AR 2018). Aggregate
margin 2016-2020: 4,628 on 70,943, **6.5%**; 2021-2025: 32,375 on 126,499, **25.6%**.

**The competitor row, same metric, from the rivals' own filings** (the rivals the filer names for SSAB Americas; three that
file with the SEC):

| Year | SSAB Americas operating margin | Nucor, steel mills segment: earnings before income taxes and noncontrolling interests / net sales to external customers | Cleveland-Cliffs, consolidated operating income / revenues |
|---|---|---|---|
| 2017 | 1.4% | 1,953 / 12,930 = 15.1% | (an iron-ore miner until its 2020 steel acquisitions; not comparable) |
| 2018 | 10.9% | 3,500 / 16,245 = 21.5% | not comparable |
| 2019 | 12.2% | 1,791 / 13,934 = 12.8% | not comparable |
| 2020 | -1.9% | 720 / 12,109 = 5.9% | part-year after acquisitions; not used |
| 2021 | 26.2% | 9,735 / 24,145 = 40.3% | 4,012 / 20,444 = 19.6% |
| 2022 | 38.1% | 7,199 / 24,190 = 29.8% | 1,939 / 22,989 = 8.4% |
| 2023 | 32.4% | 3,712 / 20,093 = 18.5% | 659 / 21,996 = 3.0% |
| 2024 | 12.7% | 2,226 / 18,734 = 11.9% | -763 / 19,185 = -4.0% |
| 2025 | 10.2% | 2,383 / 20,003 = 11.9% | -1,579 / 18,610 = -8.5% |
| **Aggregate 2017-2025** | **19.4%** (36,266 on 186,803) | **20.5%** (33,219 on 162,383) | 2021-2025: **4.1%** (4,268 on 103,224) |

Sources: Nucor 10-K FY2019 (accession 0001564590-20-007794, note on segments: 2017-2019), 10-K FY2022
(0001564590-23-002793: 2020-2022), 10-K FY2025 (0001193125-26-071575, "Nucor's results by segment": 2023-2025); USD
thousands converted to millions where the older notes give thousands. Cleveland-Cliffs 10-K FY2022 (0000764065-23-000032)
and FY2025 (0000764065-26-000025), consolidated statements of operations; Cliffs reports its Steelmaking segment by
Adjusted EBITDA only (2021 5,280; 2022 3,089; 2024 715; 2025 -16, USD m), so its consolidated operating income is used.
**Flagged:** Orion (no SEC filings found) and imports are not read; Algoma Steel Group files on Form 40-F (accession
0001193125-26-102628 for FY2025), not a 10-K or 20-F, and was not read. Nucor's segment mixes sheet, bar, structural and
plate; its plate line had external sales of USD 2,523m, 2,020m and 2,492m in 2023-2025 and its "three plate mills" a
capacity of "approximately 3,600,000 tons per year" (10-K FY2025), but Nucor files no plate profit. **No filing read states
a cost per tonne for plate by producer.** The comparison is margin against margin over the whole span, which is the nearest
the filings allow to the cost of production **[M2006-004]**, **[M2009-059]**.

**The castle tests, applied to SSAB Americas, each with its filing fact.**

1. *What keeps it standing, and how permanent is it?* **[M1995-038]** The filer names two things: the cost position of its
   mills and import tariffs ("Increased import tariffs are driving regionalization", CEO letter, AR 2025). The margins
   before the 2018 US tariffs were 6.9% (2016) and 1.4% (2017); since then they have been 10-38% except in 2020. A
   castle whose wall is a tariff is held up by a rule the business does not control; this is a fact about the castle's
   source, not a forecast of the rule **[M2000-094]**, and the speakers record a regulated protection that broke and that
   they "did not anticipate or even consider" **[L2023-011]**.
2. *The money test: could a well-funded attacker take it?* **[M2011-015]** The test has been run in the market, and the
   answer is yes. Nucor "completed construction on our approximately $1.70 billion state-of-the-art plate mill in
   Brandenburg, Kentucky", which "rolled its first plate in December 2022" and shipped from 2023 (Nucor 10-K FY2022); Nucor's
   plate capacity is now about 3.6 million tons a year against SSAB Americas' 1.8 million tonnes shipped. After it, SSAB
   Americas' operating result fell from SEK 9,651m (2023) to SEK 2,883m (2024) and SEK 2,167m (2025), and its revenue from
   SEK 29.8bn to SEK 21.2bn while its tonnes were about flat (1,803, 1,713, 1,835). I cannot separate the new mill's effect
   from the fall in the plate price that the filer reports; the point the test makes is that capital can build this
   business: "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**; "one competitor is frequently enough
   to ruin a business" **[M2012-108]**.
3. *Pricing power and the agony before a rise* **[M2005-020]**: none shown. Plate is sold "at prevailing prices"
   (Nucor's description of its own plate sales, which are "spot market sales"), and SSAB's own bridge attributes its 2025
   fall to "a decrease in prices for SSAB Americas' and SSAB Europe's products". The price is the market's and the
   rivals', not SSAB's: "whatever he charged for gas was my price" **[M2012-109]**.
4. *Unit volume and share of mind* **[M1999-054]**: volume flat at 1.7-1.8 million tonnes from 2022 to 2025; no brand in
   the customer's mind is claimed for commodity plate. *The brand* **[M2015-038]**: none for this part (the Hardox and
   Strenx brands belong to SSAB Special Steels).
5. *Would the customer choose it over the low bid?* **[M2017-009]** The customers named are steel distributors and energy
   projects buying plate to a standard; the filer gives no evidence of a premium price over Nucor's or imports'; the
   failing answer is that the buyer does not "care from whom they buy" **[L2004-003]**.
6. *The low-cost position, which in a commodity is the one exception* **[L2004-007]**, **[L2000-017]**, **[M1997-010]**.
   Against the integrated rival, Cleveland-Cliffs, SSAB Americas is far ahead (25.6% against 4.1% over 2021-2025). Against
   Nucor, the field's large scrap-based producer and the one that added capacity, it is at parity on the aggregate
   (19.4% against 20.5% over 2017-2025), ahead in the plate boom (2022-2024), and **behind in both weak years read: 1.4%
   against 15.1% in 2017, a loss of 1.9% against a profit of 5.9% in 2020.** The low-cost producer is the one that is "going
   to still be doing fine" when the price falls, and the two "are two different kinds of businesses" **[M2009-059]**; in the
   two downturns read, SSAB Americas was not the one doing fine. The cost is measured against the competitor
   **[M2001-013]**, and that row allows parity as enough for an airline's labour cost; read on the evidence here, parity in
   good years and a worse result in bad years is not the "cherished title" the exception requires **[L2004-007]**: "the
   low-cost producer can put you out of business" **[M1997-010]**. A caveat on my side of the scale: SSAB Americas'
   depreciation is unusually low (SEK 263m on SEK 21.2bn of revenue in 2025, 1.2%, against Nucor steel mills' USD 810m on
   20,003m, 4.0%), so its operating margin already flatters its cost against a rival running newer mills **[M2015-049]**.
7. *Ask the competitors* **[M1999-130]**: not on the record I can read. *Would it stand without the lord?* **[L2007-006]**:
   yes; nothing here depends on a person.
8. *Widening or narrowing?* **[M1999-108]** Narrowing on the evidence: margin 32.4% to 12.7% to 10.2% from 2023 to 2025,
   with a new mill of twice SSAB Americas' annual tonnage now in the market. Q2 2026 shows a rebound in plate prices
   ("The North American plate market was relatively strong during the second quarter and prices increased"); one quarter's
   price is not a widening of the moat.
9. *What could destroy, modify or reduce it?* **[M2000-014]** New capacity (already built), imports if the tariff wall
   changes, and scrap cost, which "is the most significant element in the total cost of steel production" for an EAF mill
   (Nucor 10-K FY2025) and is bought by both SSAB Americas and its rivals on the same spot market.

**The field's returns over the last full cycle, judged in words** (Q2, section C of the gaps case). The field is not one of
ordinary returns: Nucor's steel mills earned a pre-tax 20.5% of sales across 2017-2025, and SSAB Americas itself 19.4%,
helped by very low depreciation on old mills. So this file does not close on the ordinary-returns item. It closes on the
commodity rule's own test: in a commodity, the castle is the low-cost position, and the evidence read shows SSAB Americas
at parity with the leader in good years and behind it in both troughs read, while the leader has spent USD 1.7bn to build
the same business beside it. A castle that capital has just crossed, held up by a tariff, defended by a cost position that
is not the field's lowest, is a castle "shown on the evidence to be filling in" (Q2, The routing with Q1) **[M2011-015]**,
**[M1997-010]**, **[L2007-004]**.

**The strongest case against this verdict, written down** **[M1997-127]**: (a) parity of cost is enough by the airline row
**[M2001-013]**, and SSAB Americas met parity over nine years and beat Nucor in 2022-2024; (b) the comparison is against a
mixed segment, since no filing states plate cost, and the framework's commodity paragraph sends a cost position that "no
filing states" to TOO HARD (NATURE), not OUT; (c) SSAB Americas still earned 10% in 2025 after the new mill opened. I weigh
(b) as the serious one and answer it this way: the commodity paragraph asks whether it "is the low-cost producer, read from
its own and its operators' filings", and the margins in the two downturns are read from those filings; and the money test
**[M2011-015]** stands on its own fact, the Brandenburg mill, which needs no cost figure. If the reader holds that a margin
proxy against a mixed segment cannot read a cost position, the box is TOO HARD (NATURE), not IN; nothing on the record
makes it IN. I record this under "What in the framework was wrong or unclear".

**VERDICT: OUT.** The deciding part, SSAB Americas, sells a commodity at the market's price **[M2012-109]**, is not the
low-cost producer on the filings read **[M1997-010]**, **[M2009-059]**, and has a castle that a well-funded rival has just
crossed **[M2011-015]**, **[M2012-108]**; a castle shown open closes OUT (Q2, Why it is a STOP). The run closes here; Q3 to
Q12 are NOT REACHED, and the figures computed below are COMPUTATION, NOT A CLEARANCE.

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (closed at Q2).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (the balance sheets were read in Step 0, as the template asks).
## Q5 — WHO RUNS IT. NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7 — WHAT IS IT WORTH. NOT REACHED (the computation below is beneath the stop).
## Q8 — IS IT BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 — COULD IT RUIN US. NOT REACHED.
## Q10 — IS IT THE FAT PITCH. NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE. NOT REACHED.

---
## THE BOX
**OUT at Q2**: the deciding part, SSAB Americas (38.6% of 2021-2025 segment operating result against SSAB Special
Steels' 35.6%, a three-point margin), is commodity heavy plate sold at the market's price, not the low-cost producer on the
filings read (behind Nucor's steel mills in both downturns read, 2017 and 2020), and its castle has been crossed by Nucor's
USD 1.7bn Brandenburg plate mill; **integrity facts recorded, not judged** (featured EBITDA and adjusted figures, quarterly
outlook guidance, pay tied to an EBITDA margin; see AFTER THE STOP, Q4 and Q5). Computation beneath the stop: central value
range SEK 211 to 288 per share at the sovereign against SEK 102.20, fair price SEK 62.8 all-equity, SEK 48.7 equity-only;
no case of the central range earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box is unchanged, operator rule 2 **[M1997-127]**.)*

**Q2, the parts that did not decide.**
- SSAB Special Steels: "a global leader in the production of Q&T steels and has a market share of over 30% in wear steels";
  brands Hardox, Strenx, Armox, Toolox; named competitors "ArcelorMittal, Dillinger, Voestalpine, Nucor, Nippon Steel, JFE
  and NLMK Clabeq" (AR 2025). Operating margin 2016-2025: 11.5%, 9.1%, 7.5%, 7.9%, 9.1%, 19.7%, 24.4%, 21.0%, 18.4%, 18.8%
  (segment tables, AR 2016-2025). Q2 2026: "investments to increase capacity within SSAB Special Steels" (a new quenching
  line in Oxelösund). Not compared with the named rivals' filings, because the part does not decide. Had it decided, its
  castle (a brand asked for by name, a share of over 30%, margins that held near 18-19% in 2024-2025 while the commodity
  parts fell) would have been read on that evidence; I give no verdict on it.
- SSAB Europe: operating margin 2023-2025 2.6%, 1.7%, 0.2%; the filer: "Our existing Nordic production system has cost
  disadvantages, included those involving logistics, compared to competitors with larger production sites" (AR 2025, CEO
  letter). It is the part the Luleå mini-mill (start "at the end of 2029") and the Oxelösund furnace (start Q2 2027) are
  meant to change. Named rivals "ArcelorMittal, Dillinger, Salzgitter, ThyssenKrupp, Tata Steel Europe and Voestalpine".
- Tibnor margins 0-1% in 2024-2025; Ovako Metals Oy acquired with a cash flow of SEK 65m in Q2 2026 (interim Q2 2026).

**Q3, capital.** Maintenance capital expenditure by the filer's own split was SEK 2,907m in 2025 against depreciation,
amortization and impairment of SEK 4,072m (which includes right-of-use depreciation); strategic capex rose from SEK 273m
(2016) to SEK 7,215m (2025), and "total maintenance and strategic capital expenditure for the full-year 2026 remains at
approximately SEK 13.5 billion" (interim Q2 2026). Committed transformation spending within five years SEK 46,968m (capex
plan, AR 2025 p. 94). The filer calls the blast-furnace route one "which we believe will have an unsustainable cost
position in the future" (CEO letter), which bears on whether the spending is maintenance in substance **[L1999-024]**,
**[M1997-016]**. Return on capital employed (the filer's measure, whose capital employed includes the cash): 2, 6, 7, 3, 2,
27, -1, 22, 13 and 12% for 2016-2025. SSAB Americas' fixed assets are small: intangible, tangible and right-of-use assets in
the USA were SEK 6,662m at end-2025 (note C.1), against SSAB Americas' SEK 2,167m operating result.

**Q4, the accounts.** EBITDA is the first profit line in the key figures, and the 2022 accounts featured an "adjusted
operating result" of SEK 29,283m against a reported loss of SEK 4,355m (the goodwill write-down excluded; 10-year summary).
The 2022 write-down of SEK 33,291m fell in the record year, not in a bad one. Emission allowances are bought and sold
through the investing lines (net purchases SEK 724m in 2025, SEK 1,207m in 2024; the amount sold in 2025 "was purchased back
with forward contracts", note C.1). No confusing item found in the balance sheets read.

**Q5, the people (integrity facts, recorded, not judged).** (1) Quarterly outlook guidance is given every quarter
("Outlook for the third quarter of 2026": shipments and realized prices by division, maintenance-cost and capex estimates;
interim Q2 2026), a habit the rows name **[L2019-006]**. (2) The CEO's short-term incentive is 70% weighted to "EBITDA
margin versus peers" (paid at the maximum for 2025, SEK 5,775,000); total CEO pay 2025 SEK 22,025 thousand (AR 2025,
remuneration report, tables 1 and 2(a)). (3) The adjusted operating result was featured for 2022 (above). (4) The CEO's
three-year long-term incentive, 90% on relative shareholder return, paid zero for 2023-2025. (5) Ethics Line 2025: 41
reports, 9 within scope, action in 3 "related to compliance with rules", 2 still under investigation (AR 2025,
sustainability report). (6) No named investigation, cartel matter or fine found in AR 2025 by the search listed under Q1;
"various legal disputes with customers, suppliers, and employees" (note E.4). Any later run that reaches Q5 must answer
(1) to (3) **[M2013-088]**.

**Q6, money and owners.** (1) Buyback: a programme "for a total maximum amount of SEK 2.5 billion", resolved October 2023
and completed March 2024, 33,217,659 shares for SEK 2,507m, an average of SEK 75.5 a share; no price limit stated (AR 2025,
Board of Directors' report). Against the computation below, that average sits below the bottom of the central range at the
sovereign (SEK 211) and above the fair price at ten percent (SEK 62.8); not weighed. (2) Issuance: the Rautaruukki
combination of 2014 issued 225,310,735 new shares (AR 2018, share-capital history), a deal paid in the buyer's shares,
which the speakers call a merger **[L2009-019]**; the 2016 rights issue raised SEK 4,907m and took the shares from about
549m to 1,030m. The goodwill of IPSCO and Rautaruukki, about SEK 30bn, was written off in 2022. (3) Dividend: "Dividend
policy is 40% of profit after tax" (AR 2025); SEK 2.00 a share paid in Q2 2026. (4) Acquisitions 2021-2025 net SEK 587m,
small.

**Q9, debt and exposures.** Net cash at 2026-06-30 SEK 12,262m on this run's basis (cash 19,657 less borrowings 7,395;
leases of SEK 3,462m left out because their cash is charged in owner cash), SEK 8,629m on the filer's. Undrawn facilities
SEK 8,237m, plus the Luleå package of EUR 2.7bn (four green loan facilities) and the EUR 700m revolving facility to 2029.
Contingent liabilities SEK 18,796m, mostly parent guarantees tied to the Luleå investment. Committed spending of SEK 47bn
over five years against that liquidity.

**COMPUTATION, NOT A CLEARANCE (Q7's construction, for the owner's two reporting figures; no entry language).**
Script: `Test Runs/_research 2026-10-14 SSAAY/q7.py`; inputs from the owner-cash table in Step 0.
- *Basis.* All-equity: owner cash before interest, after the company's tax, against market value plus net debt; net cash
  SEK 12,262m at 2026-06-30 (the latest filed balance sheet; no subsequent event stated in that filing beyond the Ovako
  payment already in it). Equity-only beside, with no net cash added.
- *(a) Cycle base.* The first window year, 2021, is aberrational on the filer's own description: "The full year 2021 was
  the best in SSAB's history, with record results posted by all divisions" (AR 2021). The rows warn that "If either
  year was aberrational, any calculation of growth will be distorted" **[L2005-003]**. The base is
  therefore the average over the last two full cycles of owner cash, 2016-2020 and 2021-2025 (troughs 2016 and 2020, peaks
  2017-2018 and 2022-2023): all-equity, maintenance case, **SEK 7,666m**; the literal window (2021-2025), SEK 11,548m, is
  shown beside.
- *(e) Maintenance case central.* The filer splits capex into maintenance and strategic every year, so the central case adds
  back strategic capex; the all-spending case (SEK 5,964m) is shown beside. Maintenance capex runs below the depreciation
  charge in every year read (2025: 2,907 against 4,072 including right-of-use depreciation), so a depreciation variant
  would be lower than the maintenance case.
- **CONVENTION of this run: the committed Nordic transformation is charged in full in every central case as the cost of
  staying in place.** SEK 46,968m (capex plan, AR 2025), spread evenly over 2026-2030 and discounted at the case's rate, with
  no growth credited for it. Rationale: the filer itself says the blast-furnace route would have "an unsustainable cost
  position", so the spending is "expenditures that a company must make to maintain its competitive position"
  **[L1999-024]**, and leaving a signed SEK 47bn out of a business priced at about SEK 100bn would make every figure below
  meaningless. The figures without it are shown beside.
- *(f) The cap.* Growth between the cycle averages of owner cash is about 25% a year (3,784 to 11,548), an absurdity; the
  growth carried is cut to the business's own sales growth between the same cycles (SEK 67,647m to 108,753m average
  revenue, 9.95% a year), and that is capped at the discount rate, **3.178%**, for ten years, then zero nominal growth
  **[M1999-067]**, **[M1997-095]**.
- *(b) Decline:* none shown. *(c) Acquisitions:* net SEK 587m over 2021-2025, deducted; no merger in the window; not a
  serial acquirer; Ovako Metals Oy, signed in 2025 and closed in Q2 2026, has no filed earnings and is credited at nothing.
  *(d) Working capital:* counted, since cash from operating activities includes it.
- *The floor tested first* **[M2003-149]**: at ten percent, the central bottom case is worth SEK 53.5 a share and the top
  case SEK 72.1, both below SEK 102.20. **No case of the central range earns the floor at the price.** The width test is
  therefore not needed (the range is 1.36 to 1).

| Case (per share, SEK) | at the sovereign 3.178% | at ten percent |
|---|---|---|
| **Central, all-equity, bottom (no growth)** | **211.4** | 53.5 |
| **Central, all-equity, top (3.178% ten years, then zero)** | **288.3** | 72.1 |
| Equity-only, bottom / top | 194.0 / 269.4 | 39.6 / 57.8 |
| Beside: all-equity without the transformation charge, bottom / top | 254.3 / 331.3 | 89.2 / 107.9 |
| Beside: all-spending case, bottom / top | 157.7 / 217.5 | 36.4 / 50.9 |
| Beside: literal window 2021-2025, bottom / top | 334.0 / 449.8 | 92.4 / 120.5 |

**The two reporting figures (a reporting convention; neither is a verdict or entry language):**
- **(a) VALUE RANGE: SEK 211 to SEK 288 per class B share** (all-equity, central), **USD 10.62 to 14.49 per ADS** (0.5 share
  at SEK/USD 0.1005), against **SEK 102.20 (USD 5.27 per ADS quoted)**.
- **(b) FAIR PRICE: SEK 62.8 per class B share, all-equity (the central figure); SEK 48.7 equity-only**; per ADS USD 3.16 and
  USD 2.45. Computed as Part VII states: each end case valued with its own cash stream at ten percent, the two averaged,
  after the company's own tax with no conversion. Without the transformation charge, the all-equity fair price would be
  SEK 98.5; on the literal window, SEK 106.5. The price is above the central fair price.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 55d88f2b); written question by question; committed after Step 0
      and Q1 (59025f92) and after Q2 (4f8565ec); this section in the closing commit.
- [x] Dispatched: the brief allowed per-question commits; a lock file was present in `Screens/_daily/` (not opened); the
      fold is the dispatching session's (operator rule ten).
- [x] No other run file, holding review, `PORTFOLIO.md`, resume-state file, queue file or reading list was opened, listed or
      searched. What I saw by accident is declared under CONTAMINATION at the top. I listed `Screens/_daily/` once with a
      filter for "lock", which showed only `_overnight.lock`.
- [x] Every v5 id checked against `principle_ledger_v5.csv`, and every quoted fragment beside an id checked against its row,
      by `Test Runs/_research 2026-10-14 SSAAY/check_citations.py`; no E-ids. Every filing fact carries its document and
      date (no accession numbers exist for SSAB; the SEC filings cited carry theirs).
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance, and every figure after it is headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash flow statements, never a net-income proxy (operator rule 5);
      the sovereign from the Riksbank, dated; aggregator quotes flagged.
- [x] Contrary evidence written down as found (foundations, and the strongest case against the Q2 verdict); facts for
      later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time test; no anchor-date issue.
- [x] `tools/run.py` and `Screens/cover_shares.py` returned nothing for a non-SEC filer; nothing they print was used.
- [x] `python tools/check_framework.py` run before the closing commit.
- Honest limits: the 2022 and 2019 annual reports were not fetched (their figures come from the next year's comparatives);
  Nucor's FY2016 segment data sits in an exhibit I did not fetch, so the competitor row starts in 2017; Algoma (Form 40-F)
  and Orion were not read; the lease principal is taken as total lease cash less lease interest, which may include
  short-term lease payments already inside operating cash and so overstate the deduction slightly; the ADR facility
  behind the ticker SSAAY could not be confirmed (both give 0.5 share).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **The commodity paragraph and a mixed-segment rival.** Q2's commodity paragraph asks whether the business
is "the low-cost producer, read from its own and its operators' filings", and sends a cost position that "no filing
states" to TOO HARD (NATURE). No filing states a cost per tonne of plate: SSAB reports by segment, and Nucor's steel mills
segment mixes sheet, bar, structural and plate. I read the cost position from margins over the whole span, troughs
included, and closed OUT on that and on the money test, which needs no cost figure. A second analyst could read the same
filings and close TOO HARD (NATURE). The text does not say whether a margin comparison against a rival's mixed segment
counts as read from the filings, or whether the money test can close a commodity part OUT without a cost figure. (2)
**The parts threshold on a knife edge.** The deciding part was chosen by three points of five-year operating profit, and the
five-year window is mostly boom years; over ten years (2016-2025) SSAB Special Steels' summed result (37,111) is slightly
larger than SSAB Americas' (37,003), so a ten-year reading would make the branded part decide and might change the box.
The framework fixes five years; it does not say what to do when the choice of part turns on the window. I followed the
text. (3) **Committed future spending in Q7.** Q7's specifics price a signed but unclosed acquisition beside the central
figure, but say nothing of a signed capital programme about half the market value that replaces the production base
rather than buying growth. Specific (e) charges "growth spending" against the growth it buys; Luleå buys mainly a
different cost position. I charged it in every central case as a CONVENTION of this run and showed the figures without
it; the text should say which it wants.

