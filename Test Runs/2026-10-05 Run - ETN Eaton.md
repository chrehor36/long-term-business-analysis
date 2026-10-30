# Company Run — Eaton Corporation plc (NYSE: ETN) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run from the
template `Test Runs/_TEMPLATE - Company Run.md`, copied to this dated file before any fetch. Every judgment cites a v5
ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run and later
questions are marked NOT REACHED. Working folder: `Test Runs/_research 2026-10-05 ETN/` (raw filings, the fetch and
text scripts, the peer table script `peers.py`, and the ledger rows read, `rows.txt`).

**POSITION NOTE, declared before any verdict:** not checked. Under the blind rule of this run's brief, `PORTFOLIO.md`,
the holding reviews, the session-state file, the queue register and the prepped reading list were not opened, and no
attempt was made to learn whether the operator holds or wants this name.

**CONTAMINATION, declared.** (1) The session's git status listed untracked run files dated 2026-10-05 for ATKR, HUBB and
NVT; none was opened, and the HUBB and NVT figures below were fetched fresh from EDGAR. (2) The same listing showed a file
named `ETN_sub.json` inside another run's research folder (AYI peers); it was not opened. (3) Recent commit subjects named
OUT-at-Q2 boxes for five contractors and distributors (WCC, LMB, DY, MTZ, PRIM); none concerns Eaton, and I record them
so a reader can judge whether they leaned on my Q2. (4) The memory index loaded into the session carries a sentence about
a count of gate-clearers with "nothing buyable"; it names no company. Nothing else about this name was seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $437.83 (2026-10-05, live quote via `tools/run.py`; aggregator, flagged per operator rule 5, used for the
  quote only). For scale: the 10-K gives $318.51 as the close on the last trading day of 2025 (Note 14), so the price has
  risen about 37% in nine months.
- **Shares:** one class of ordinary shares. The 10-Q for the quarter ended 2026-06-30 (filed 2026-07-31, accession
  `0001551182-26-000030`) states on its cover: "There were 388.4 million ordinary shares outstanding as of June 30, 2026."
  `python Screens/cover_shares.py ETN` printed 1,551,182,000,000, which is the CIK scaled by a million: a tool defect,
  recorded, and the cover figure read by hand was used instead.
- **Market cap:** $437.83 × 388.4M = **$170.05B**.
- **Sovereign for the earnings currency (USD):** **5.63%**, the 30-year par yield, US Treasury daily par yield curve,
  dated 2026-10-02 (as fetched by `tools/run.py` from the issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-26, accession `0001551182-26-000007` (Item 1, Item
  1A, MD&A, the four statements, Notes 2, 3, 6, 9, 11, 12, 14, 16, 18); 10-Q for Q2 2026, `0001551182-26-000030`
  (statements, Notes 2, 3, 15, MD&A, liquidity); proxy DEF 14A filed 2026-03-13, `0001193125-26-105117` (CD&A, summary
  compensation table, board leadership); 8-Ks of 2026-02-06 (`0001140361-26-004227`, the $8B Boyd bridge facility),
  2026-06-11 (`0000950142-26-001733`, the Mobility Reverse Morris Trust with Dana), 2026-07-31 (`0001551182-26-000027`,
  results) and 2026-10-05 (`0001140361-26-038523`, a new principal accounting officer). History: 10-Ks for FY2013
  (`0001551182-14-000011`), FY2016 (`0001551182-17-000014`), FY2019 (`0001551182-20-000050`), FY2022
  (`0001551182-23-000004`), and Eaton Corporation (Ohio) FY2009 (`0000950123-10-018180`).
- **One figure cross-checked against the filed statement:** operating cash flow 2025, $4,472M in the XBRL facts and
  $4,472M on the filed Consolidated Statement of Cash Flows (10-K FY2025, page 30). Agrees.
- **`tools/run.py ETN`, arithmetic lines only** (Part VII; the tool's v4 wording, ids and floor were ignored). Its SBC
  column read zero for every year: a defect, because Eaton has no separate stock-pay line in its cash-flow statement.
  Stock pay was taken from Note 14 instead (pre-tax expense of RSUs and RSAs, PSUs and options): **2021 $101M, 2022 $97M**
  (10-K FY2022, Note on equity-based compensation), **2023 $97M, 2024 $108M, 2025 $126M** (10-K FY2025, Note 14).

**Owner cash after every real cost** (operating cash flow, which already adds stock pay back, less stock pay, less all
capital spending; USD millions; OCF and capex from the filed cash-flow statements):

| year | OCF | stock pay | capex | owner cash | D&A | of which amortization of acquired intangibles | depreciation | depreciation variant |
|---|---|---|---|---|---|---|---|---|
| 2021 | 2,163 | 101 | 575 | **1,487** | 922 | 431 | 491 | 1,571 |
| 2022 | 2,533 | 97 | 598 | **1,838** | 954 | 483 | 471 | 1,965 |
| 2023 | 3,624 | 97 | 757 | **2,770** | 926 | 450 | 476 | 3,051 |
| 2024 | 4,327 | 108 | 808 | **3,411** | 921 | 425 | 496 | 3,723 |
| 2025 | 4,472 | 126 | 919 | **3,427** | 1,006 | 486 | 520 | 3,826 |
| five-year mean | | | | **2,587** | | | | 2,827 |

Amortization for 2023 to 2025 is the 10-K FY2025 MD&A figure; for 2021 and 2022 the XBRL `AmortizationOfIntangibleAssets`
fact. Owner cash per share on the 2025 figure: $3,427M / 388.4M = $8.82; on the five-year mean, $6.66. Against the price,
the five-year mean is a 1.52% yield; the 2025 figure 2.0%; the sovereign is 5.63%.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the one on macro: "macro conclusions are — just never enter into the
discussion" **[M2000-094]**. Eaton's own 10-K opens on "megatrends of the electrification, digitalization, and the
reindustrialization" and on "momentum in the data center and utility end markets"; that is a forecast, and it is kept out
of every question below. The second is that the market serves and does not instruct **[M2006-077]**: the price has risen
by about a third since the year's last close while the 2026 first-half net income fell 13%, so the price is not evidence
about the business. Third, who is paid to tell you **[M2020-037]**: the filing's own framing is "adjusted earnings", which
Q4 reads. **Contrary evidence, written down as found** **[M1997-127]**: (a) commodity inflation cut Electrical Americas'
margin by 380 basis points in 2025 and 470 in Q2 2026 (both filings), so the price did not keep up with cost; (b) the
10-K's risk factor says "potential price increases, could negatively impact our market share or relationships with
distributors or customers"; (c) debt more than doubled in March 2026 to buy Boyd Thermal for $9.55B; (d) 22% of the
electrical segments' 2025 sales went to six customers; (e) the Electrical Americas margin was about 20% as late as 2020
and 2021 and about 30% in 2024 and 2025, so the present level is recent.

## THE STANDING RULE
Bought for cash, unlevered, at a size the buyer can hold through a fall of half, ownership of a share of Eaton puts the
buyer at no risk of ruin; the rule binds the buyer's financing and sizing, and borrowing to buy is ruled out
**[L2014-005]**, **[M2012-081]**. Nothing about the target changes this line; the target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years" **[M2012-065]**; the product may stay opaque if "the economic dynamics of the industry" are
understood **[M2011-014]**. Eaton is a holding of parts and is read by its parts (CONVENTION, section VI).

**The parts, from the filings** (2025 segment operating profit, 10-K FY2025 Note 18; Q2 2026 segments, 10-Q Note 15):
- **Electrical Americas** (2025 sales $13,276M, profit $3,972M, 29.9%) and **Electrical Global** ($6,815M, $1,323M,
  19.4%): breakers, panelboards, switchgear, UPS, power distribution assemblies and systems, sold through distributors and
  direct, specified into buildings, data centers, utilities and factories. Together 73% of 2025 sales and 79% of 2025
  segment profit. The 10-K names the "Principal methods of competition" as "performance of products and systems,
  technology, customer service and support, and price."
- **Aerospace** ($4,249M, $1,013M, 23.9%): fuel, hydraulic and pneumatic systems on aircraft platforms; 20% of segment
  sales to three airframers.
- **Mobility** (Vehicle $2,505M at 16.7%, eMobility $604M at a loss): to be separated into a Reverse Morris Trust with
  Dana; Eaton receives "approximately $1.1 billion in cash distribution" and its holders "at least 50.1%" of the combined
  company (8-K 2026-06-11). It leaves the parts that matter.
- **Boyd Thermal**, bought 2026-03-12 for $9.55B net of cash: liquid cooling and thermal components for data centers and
  aerospace; $524M of sales and $121M of segment profit from closing to 2026-06-30 (10-Q Note 2). Annualized, about 6% of
  sales.

**Key variables** **[M1998-044]**: for the electrical core, (1) share and price in an industry of a few large makers whose
products carry listings and codes and fit an installed base; (2) the margin through a cycle. Both have a fifteen-year
record in the filings (Q2). The product technology of low- and medium-voltage distribution changes slowly; the record
read back to 2008 shows the same four or five makers. The demand level (data-center and utility spending) is a forecast
and is not a variable I am allowed to use **[M2000-094]**; what I must judge is whether Eaton stands where it stands in the
industry, which the record lets me do.

**Doubts written down.** Boyd's liquid cooling and the solid-state transformer work bought with Resilient Power are
newer technologies whose ten-year economics depend on chip and data-center design; "if you have doubts about something
being into your circle of competence, it isn’t" **[M2002-092]**. I read them as parts that do not decide the whole's
earnings (about 6% of sales and a similar share of segment profit), so the by-parts convention does not put the whole
outside; they decide capital allocation, which Q6 weighs. This reading is mine and is confessed in the last section.

**VERDICT: IN.** The electrical core and Aerospace are businesses whose economics and position can be foreseen in the
sense of **[M2000-037]**; the industry is slow-changing, so the routing to TOO HARD for fast change **[M1998-008]** does
not apply to the parts that matter.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing" **[M1995-038]**.

**The record through the cycle** (segment operating margin; the electrical segments were "Electrical Americas" and
"Electrical Rest of World" in 2009, "Electrical Products" and "Electrical Systems and Services" from 2011 to 2019,
"Electrical Americas" and "Electrical Global" from 2020; so the lines are not one series):

| | 2008 | 2009 | 2011 | 2012 | 2013 | 2015 | 2016 | 2017 | 2018 | 2019 |
|---|---|---|---|---|---|---|---|---|---|---|
| Electrical Americas (2008-09) / Products (2011-19) | 15.7% | 15.2% | 14.7% | 16.7% | 16.1% | 16.6% | 17.8% | 17.8% | 18.4% | 19.4% |
| Rest of World (2008-09) / Systems and Services (2011-19) | 8.0% | 4.3% | 10.1% | 11.3% | 14.4% | 13.1% | 12.6% | 13.6% | 14.9% | 16.3% |

| | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | H1 2026 |
|---|---|---|---|---|---|---|---|
| Electrical Americas | 20.2% | 20.6% | 22.5% | 26.5% | 30.2% | 29.9% | 26.6% |
| Electrical Global | 15.9% | 18.7% | 19.4% | 19.3% | 18.4% | 19.4% | 19.6% |

Sources: FY2009 Ohio 10-K MD&A (`0000950123-10-018180`); FY2013 10-K (2011 to 2013, "before acquisition integration
charges"); FY2016 10-K (2014 to 2016); FY2019 10-K (2017 to 2019); FY2022 10-K (2020 to 2022); FY2025 10-K (2023 to
2025); Q2 2026 10-Q (H1 2026). In 2009 Electrical Americas sales fell 15% and its margin moved from 15.7% to 15.2%;
company net income fell from $1,058M to $383M and operating cash flow held at $1,408M against $1,441M, and the dividend
was held at $2.00 a share (FY2009 10-K). In 2020 (sales down 16% company-wide, 17,858 against 21,390) the Americas
electrical margin was 20.2%.

**The castle tests, each with its filing fact.**
1. *The attacker with money* **[M2011-015]**. No instance found in the filings read of a new entrant reaching scale in
   North American low-voltage distribution between 2008 and 2026; the competitors named in the peers' filings and releases
   read are the same few (Schneider, Siemens, ABB, Hubbell in its niches, and Eaton); that ABB took over GE's industrial
   electrical business in 2018 is my own knowledge, not read in a filing this session. The
   barriers I can see from the filings are listings and codes, an installed base whose replacement and extension parts
   are brand-specific, the distributor channel, and the engineer's specification. These are my reading of how the
   products are sold; the 10-K does not describe its channel in that detail, so the test is answered by the record of
   who competes, not by a statement.
2. *Pricing power and the agony before a rise* **[M2005-020]**. The test the row gives is "the agony they go through in
   determining whether a price increase can be sustained." The filing speaks of that agony in its risk factors: "our
   responses to mitigate the impact of these conditions, such as potential price increases, could negatively impact our
   market share or relationships with distributors or customers" (10-K FY2025, Item 1A). And the margin record shows cost
   moving faster than price twice in eighteen months: 380 basis points of "higher commodity and wage inflation" in
   Electrical Americas in 2025, 470 basis points of "higher commodity inflation" in Q2 2026. The row on raw materials
   reads this as a lag rather than a breach: strong businesses "manage to pass through increases in raw material costs
   [...] But you get these temporary situations where, sometimes, the costs are increasing faster" **[M2005-017]**; and
   Schneider reports the same thing (below). **Weighs against, not decisive.**
3. *Unit volume and share of mind* **[M1997-099]**: not measurable from the filings; Eaton reports backlog and orders,
   not units. Electrical Americas backlog $13,246M at end-2025 against $10,141M a year earlier, book-to-bill 1.2 (10-K);
   $15,175M at 2026-06-30, orders up 41% organic trailing twelve months (10-Q). This is demand in a boom, not share.
4. *The low-cost position* **[L2007-004]**, **[M2018-043]**. Not shown: no filing gives cost against a competitor. Eaton
   is not argued to be the low-cost maker; the castle, if there is one, is the oligopoly and the installed base.
5. *Would the customer still choose it over the low bid?* **[M2017-009]**, **[M2001-014]**. Switchgear and breakers sit
   in the safety path of a building or data center; the parachute row is the nearest analogy, "I don’t think if you were
   buying a parachute you’d want to take the — necessarily take the low bid" **[M2001-014]**. Against it, the filing lists
   price among the principal methods of competition, and six customers bought 22% of electrical sales in 2025 (10-K Item 1),
   which is buying power.
6. *Ask the competitors* **[M1999-130]**. Their own figures follow in the competitor row: the three global rivals report
   electrical-distribution margins of about 19% to 22%; Eaton's Americas segment earns about 30% and its Global segment
   about 19%. Schneider, in its own FY2025 release, writes that "A decline in gross margin was driven by negative mix and
   raw material inflation" in Energy Management (non-SEC; Schneider Electric "2025 Full Year Financial results", se.com,
   flagged); the cost squeeze is the industry's, not Eaton's alone.
7. *Widening or narrowing* **[M1999-108]**, **[M2000-075]**. Over 2011 to 2025 the margins in both electrical lines rose
   in nearly every year, through 2015-2016's industrial and oil slump (Systems and Services 13.1%, 12.6%) and through 2020.
   The record reads as a moat that held and widened; how much of the rise since 2022 is the data-center boom cannot be
   separated from the filings.
8. *What could destroy or reduce it, five to fifteen years out* **[M2000-014]**: (a) a technology shift in power
   distribution (solid-state transformers, DC distribution in data centers), which Eaton is buying into rather than
   inventing (Resilient, 2025); (b) customer concentration, if hyperscale buyers design their own power trains; (c)
   Asian makers entering listed products. No filing read shows any of these happening; they are risks named, not evidence.

**The competitor row** (same metric from each company's own filings; EBIT is operating income where reported, otherwise
pre-tax income plus interest; tangible assets are total assets less goodwill, intangibles and cash; XBRL company facts,
first-filed values, `peers.py`):

| company (source) | metric | 2009 | 2015 | 2019 | 2020 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| Eaton, consolidated (10-K XBRL) | EBIT margin | n/a | 11.4% | 13.2% | 10.6% | 17.1% | 18.9% | 18.8% |
| Eaton, consolidated | EBIT / tangible assets | n/a | 21.1% | 19.7% | 13.2% | 22.3% | 25.4% | 26.1% |
| Hubbell, HUBB (10-K XBRL, CIK 48898) | operating margin | 12.5% | 14.0% | 13.0% | 12.7% | 19.3% | 19.4% | 20.7% |
| Hubbell | EBIT / tangible assets | 20.8% | 30.3% | 28.0% | 25.5% | 36.5% | 39.4% | 36.7% |
| nVent, NVT (10-K XBRL) | operating margin | n/a | 15.7% (2016) | 15.1% | 1.9% | 18.0% | 17.5% | 15.8% |
| Vertiv, VRT (10-K XBRL) | operating margin | n/a | n/a | 4.7% | 4.9% | 12.7% | 17.1% | 17.9% |
| GE Vernova, GEV (10-K XBRL) | operating margin | n/a | n/a | n/a | n/a | -2.8% | 1.3% | 3.6% |
| ABB (20-F XBRL to FY2023; deregistered 2024) | operating margin | 13.0% | 8.6% | 6.9% | 6.1% | 15.1% | n/a | n/a |
| Schneider Electric, Energy Management (FY2025 release, non-SEC, flagged) | adjusted EBITA margin | | | | | | | 21.8% |
| Siemens, Smart Infrastructure (FY2025 earnings release, non-SEC, flagged) | profit margin | | | | | | 17.3% | 19.6% |

Segment comparisons, which fit better than the consolidated lines: Eaton Electrical Americas 29.9% and Global 19.4%
(2025, before amortization of acquired intangibles); Schneider Energy Management 21.8% (adjusted EBITA, before purchase
amortization); Siemens Smart Infrastructure 19.6% (fiscal 2025, which the release says includes "a €0.3 billion gain"
from exiting wiring accessories). Return on the segment's own identifiable assets (10-Q Note 15, which excludes goodwill):
Electrical Americas earned $3,972M in 2025 on identifiable assets of $6,283M at year-end, about 63% pre-tax. Eaton's
consolidated return on tangible assets is good but below Hubbell's in every year shown; the castle is in the electrical
segments, and in the Americas above all.

**Verdict.** The castle is shown standing on the evidence: a few makers for decades, a margin that held through 2009 and
2020 and widened from 2011 to 2025, and segment returns on tangible capital far above any cost of money. The evidence
against (cost passed through late in 2025-2026, price among the means of competition, buyer concentration, the level of
the last three years being boom-driven) reduces the confidence in the level of earning power, which is Q7's question,
and does not show the castle filling in, which is what would close it OUT **[M2011-015]**; nor is its future beyond
judging **[M2000-019]**. **VERDICT: IN**, with the price-cost lag carried forward as the strongest contrary fact.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, **[M2011-060]**: the electrical segments earn far above their
  tangible capital (Electrical Americas about 63% pre-tax on identifiable assets in 2025, above); the whole company earned
  EBIT of $5,173M in 2025 on tangible assets of $19,806M (26%), before netting the $8.2B of payables, accrued pay and
  other current liabilities that fund part of them (10-K balance sheet). Read with the row's warning about "a cyclical
  peak in earnings" **[L1994-009]**: the 2023-2025 returns are boom-year returns; the 2015-2019 returns of about 20% on the
  same measure are the quieter years' figure.
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**. Depreciation (D&A less amortization) ran
  $471M to $520M a year over 2021-2025; capital spending ran $575M to $919M, and the 10-Q guides "approximately $1.15
  billion in capital expenditures in 2026" "to expand production capacity". My maintenance guess, stated as a guess per
  **[M2000-144]**: about depreciation, $500M to $550M a year, with the rest growth capacity. Capex is about 3.3% of sales.
  Working capital rose with sales: inventory went from 12.8% of sales (2017) to 17.2% (2025).
- **What the added capital earned.** Between 2015 and 2025 consolidated EBIT rose from $2,377M to $5,173M (+$2.8B) while
  tangible assets rose from $11,270M to $19,806M (+$8.5B), an increment of about 33% pre-tax on the tangible capital
  added; goodwill and intangibles stayed near $19.5B to $20.8B over the span because Lighting (2020) and Hydraulics (2021)
  were sold while Tripp Lite and Cobham Mission Systems (2021) and Fibrebond (2025) were bought. From March 2026 the
  calculus changes: Boyd Thermal added $9.55B of capital for an annualized segment profit of roughly $400M (from $121M in
  the 3.6 months after closing), about 4% pre-tax before interest and before amortization, a bet on its growth.
- **WEIGHS FOR**: a business of the second kind in **[M1998-081]** at worst ("It takes more money, but the rate at which
  you invest — reinvest — the money to get that growth is a very satisfactory rate"), on the tangible capital; the
  purchased capital (goodwill of $20,229M at 2026-06-30) earns much less and is weighed at Q6.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first** **[M2025-032]** (USD millions; FY-end XBRL first-filed values as printed by `tools/run.py`,
checked against the filed balance sheets for 2024 and 2025; 2026-06-30 from the 10-Q):

| year-end | assets | equity | goodwill | intangibles | cash + ST inv. | receivables | inventory | total debt | retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2017 | 32,623 | 17,253 | 13,568 | 5,265 | 1,095 | 3,943 | 2,620 | 7,751 | 8,669 |
| 2018 | 31,092 | 16,107 | 13,328 | 4,846 | 440 | 3,858 | 2,785 | 7,521 | 8,161 |
| 2019 | 32,805 | 16,082 | 13,456 | 4,638 | 591 | 3,437 | 2,805 | 8,322 | 8,170 |
| 2020 | 31,824 | 14,930 | 12,903 | 4,175 | 1,102 | 2,904 | 2,109 | 8,058 | 6,794 |
| 2021 | 34,027 | 16,413 | 14,751 | 5,855 | 568 | 3,297 | 2,969 | 8,579 | 7,594 |
| 2022 | 35,014 | 17,038 | 14,796 | 5,485 | 555 | 4,076 | 3,430 | 8,655 | 8,468 |
| 2023 | 38,432 | 19,036 | 14,977 | 5,091 | 2,609 | 4,475 | 3,739 | 9,269 | 10,305 |
| 2024 | 38,381 | 18,488 | 14,713 | 4,658 | 2,080 | 4,619 | 4,227 | 9,152 | 10,096 |
| 2025 | 41,251 | 19,425 | 15,769 | 5,054 | 803 | 5,387 | 4,721 | 9,895 | 10,702 |
| 2026-06-30 | n/a | 20,254 | 20,229 | n/a | 695 | n/a | n/a | 20,611 | n/a |

Total debt is long-term debt including current portion plus short-term borrowings (XBRL `LongTermDebt` plus
`ShortTermBorrowings`; 2025 from the balance sheet: 1 + 1,136 + 8,758; 2026-06-30: 2,091 + 11 + 18,509).

**What the figures say.** (1) Equity was flat for eight years (17.3B to 19.4B) while net income doubled (2,145 in 2018 to
4,087 in 2025): nearly every dollar earned went out as dividends ($12.65B over 2016-2025) and buybacks ($10.25B over the
same years), XBRL cash-flow facts; retained earnings fell in 2020 and barely rose overall. (2) Goodwill and intangibles
were nearly constant at about $19-21B until 2025 and then jumped by $4.5B in six months of 2026, to goodwill alone of
$20.2B, more than total equity. (3) Receivables kept pace with sales (19.3% of sales in 2017, 19.6% in 2025). Inventory
outran sales (12.8% to 17.2%). (4) Prepaid expenses and other current assets rose from $874M to $1,444M in 2025; Note 3
explains it: "Unbilled receivables were $759 million and $330 million at December 31, 2025 and 2024", from "higher revenue
recognized over time" and the Fibrebond acquisition. An explained build, recorded, not a tell by itself **[M1995-064]**.
(5) Debt was steady at $7.5B to $9.9B for nine years, then doubled to $20.6B in March 2026. **What they cannot say:** how
much of the 2023-2025 margin is the boom; the books show the margin, not its durability.

**The real costs.**
- *Depreciation* is a real cost **[R1996-023]**; capex exceeded it in every year shown, so owner cash deducts all capex,
  with the depreciation variant shown (STEP 0).
- *Amortization of acquired intangibles* ($486M in 2025, about $1B a year at the Q2 2026 rate of $255M a quarter):
  "Some truly deplete over time while others never lose value" **[L2012-003]**. The intangibles are mostly customer
  relationships and technology from Cooper, Tripp Lite, Cobham, Fibrebond, Boyd; some technology depletes. Owner cash
  above is unaffected (amortization is non-cash and not in it).
- *Stock pay* is deducted **[L2015-003]**: $126M in 2025, small (3% of OCF).
- *Restructuring*: charges in every year from 2012 to 2025 except 2018 and 2019 (XBRL `RestructuringCharges`: 50, 36, 54,
  129, 211, 116, 0, 0, 214, 292, 33, 57, 202, 335), a 2020 programme of $382M and a 2024 programme now estimated at $475M.
  A recurring cost; "to tell owners year after year, "Don't count this," when management is simply making business
  adjustments that are necessary, is misleading" **[L2016-007]**. Owner cash includes the cash paid, so the recast is
  unaffected; the framing is weighed below.
- *Acquisition and divestiture charges* of $183M in 2025 included "Employee transaction and retention award compensation
  expense related to the acquisition of Fibrebond of $82 million"; that is pay, and it is excluded from adjusted earnings.

**EBITDA and adjusted earnings in the filer's own mouth.** The 10-K's MD&A sets out "Adjusted earnings" and "Adjusted
earnings per ordinary share" ($12.07 against GAAP $10.45 in 2025), adding back amortization, restructuring and acquisition
charges, the last of which includes the Fibrebond retention pay. No EBITDA figure was found in the 10-K or the 10-Q read.
Adjusted EPS is also the bonus metric (proxy). This is "a management that regularly attempts to wave away very real costs
by highlighting "adjusted per-share earnings"" **[L2016-006]**, at least in part: the restructuring and retention pay are
real; part of the amortization is not.

**The make-the-numbers habit and the two-tell line (CONVENTION).** The proxy shows 2025 adjusted EPS of $12.07 against
a target of $12.00: one year, and the committee then cut the payout from a formulaic 96% to 70% by removing "gains on the
Fibrebond acquisition that were not included in our profit plan" and "real-estate related transactions and the deferral of
certain cash payments". I did not assemble several years of guidance against results, so the habit is not established
**[L2002-041]**; the adjusted-earnings framing is one tell. One tell is a weighing, not suspicion **[M1994-018]**. The
committee's cut, which removed one-off gains from its own executives' bonus, reads the other way.

**Tax and contingencies.** Unrecognized tax benefits $1,300M plus $218M interest (10-K MD&A); two Brazilian goodwill-tax
cases and US transfer-pricing litigation (Note 12) of a size the company calls not material; the 2026 effective tax rate
rose to 24.9% for the half from 17.6%, partly "withholding tax expense related to funding the acquisition of Boyd Thermal".
A new principal accounting officer from 2026-10-05 (8-K), the second controller change since 2024 (10-K executive list).

**VERDICT on confusion: IN** (the accounts can be read and the recast made); **WEIGHS AGAINST** on the adjusted-earnings
framing and the recurring restructuring **[L2016-006]**, **[L2016-007]**. The recast earnings fed to Q7 are owner cash
after all capex and stock pay (STEP 0).

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**. The record against the hand dealt: under the previous chief executive (2016 to
  May 2025) the portfolio was turned toward electrical and aerospace (Lighting sold 2020, Hydraulics 2021, Mobility now
  leaving), and electrical margins rose from the high teens to near 30%. The hand was a good one: the industry's demand
  rose for all makers, and Hubbell's margin rose further over 2021-2025 (12.7% to 20.7%) than Eaton's
  consolidated margin (15.5% to 18.8%). The new chief executive, Paulo Ruiz, took office on 2025-06-01 (proxy and 10-K),
  after running Hydraulics, Energy Solutions and the Industrial sector; his record as chief
  executive is sixteen months and includes the Boyd purchase and the Mobility separation.
- **How they treat themselves against the owners** **[M1994-009]**. CEO total pay in the summary compensation table:
  $7,923,677 for 2025, $5,031,963 for 2024 (as a sector president). Modest for the size. The board separated the chairman
  and chief executive roles at the succession, with a non-executive chairman from 2025-06-01 (proxy). Director stock
  ownership guidelines exist (proxy), not examined further.
- **Tells of dishonesty** (the list in the framework's Q5). None found in the documents read: no restatement found, no
  reserve releases found, a clawback policy for restatements and misconduct, and a pay committee that cut its executives'
  bonus for one-off gains. The adjusted-earnings framing is common practice and is weighed at Q4, not read as dishonesty.
  Integrity is applied on doubt alone **[M2013-088]**; I have no doubt from the record read, while knowing that a
  marketable-stock reader reads rather than meets **[M2007-081]**.
- **Love of the business** **[M2000-098]**: not judgeable from documents beyond the career record (Ruiz has been inside
  Eaton since 2019, the Electrical sector president since 2022).
- **VERDICT on integrity: IN**; **ability WEIGHS FOR** on the company record, **UNDECIDED** for the new chief executive.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- *Retention test* **[R1995-009]**, **[M1998-110]**. Eaton retained little: dividends plus buybacks of $22.9B against net
  income of $23.4B over 2016 and 2018-2025 alone (2017 not extracted), and the rest went into deals net of disposals. The market leg was not tested: the
  filings read give the end-2025 close ($318.51, Note 14) but no earlier year-end close was found in them, and I did not
  take one from memory. With so little retained, the test has little to bite on either way. The forward question, "Can you
  keep using all of the capital you generate" well **[M2010-097]**, turns on the deals.
- *Buybacks* **[L1999-023]**, **[L2016-002]**. 7.8M shares for $2.5B in 2024 (about $320 each) and 5.7M for $1.9B in 2025
  (about $327), under a $9.0B authority with no stated price (10-K MD&A). By the CONVENTION, a programme with no stated
  price weighs against unless the prices paid sit at or below the bottom of the Q7 range; the bottom of the range below is
  $118, so the purchases at $320 to $327 **weigh against**. Buybacks were suspended for 2026 because of Boyd.
- *Deals* **[L2014-012]**, **[L2017-004]**. All the recent deals were paid in cash or debt, so the all-stock STOP
  **[L2009-019]** does not arise. Value given against value got: Boyd at $9.55B for roughly $400M of annualized segment
  profit (above) prices the bought business at about 24 times pre-tax, pre-interest segment profit, debt-financed, at a
  time when the sovereign is 5.63%. Judged "on an all-equity basis" **[L2017-004]**, the deal earns about 4% pre-tax at
  its present profit and needs growth to earn its cost; the 10-Q's own reason for the goodwill is "the anticipated
  synergies", and "we never count on synergies" **[L2016-008]**. Fibrebond ($1.43B) and Ultra PCS ($1.53B) are smaller.
  **Part A WEIGHS AGAINST**: the core throws off far more than it needs, and the surplus has gone, in the last year, into
  buybacks at prices above the Q7 range and into a large debt-financed purchase whose present earnings are below the bond.
**Part B, the pay, the board, the owners.**
- *Pay tied to what the person controls* **[M2003-019]**, **[L1996-018]**. Short-term plan on adjusted EPS (which adds
  back amortization and restructuring) and adjusted operating cash flow; long-term plan half PSUs vesting on relative TSR,
  half options and RSUs (proxy CD&A). Relative TSR and options pay on the stock price, which the row calls a "lottery
  ticket" when it is "totally out of the control of the person whose behavior we would like to affect" **[L1996-018]**;
  no charge for capital employed appears in the metrics. Against that, the committee cut the 2025 award for one-offs.
- *The board* **[M2007-120]**, **[L2014-026]**: the chairman is now non-executive. **Part B WEIGHS AGAINST, mildly**: the
  plan rewards adjusted earnings and the share price, not returns on capital.

## Q7 — WHAT IS IT WORTH? STOP.
**The construction (CONVENTION, Part VI).** Owner cash after every real cost, five-year mean **$2,587M** (2021-2025,
STEP 0), carried at the growth shown, capped by Q3, for ten years, then zero nominal growth, discounted at the sovereign
5.63% **[L2000-021]**, **[M1996-025]**; the ends are the no-growth and shown-growth cases **[L2000-024]**. Growth shown on
aggregate owner cash, 2021 to 2025: ($3,427M / $1,487M) to the quarter power = **23.2% a year**.

**The Q3 cap.** 23.2% a year for ten years carries owner cash from the $2,587M base to about $21B, about five times
Eaton's 2025 net income of $4.1B, while sales grew 8.7% a year over the same years (19,628 to 27,448). The gap is margin
expansion plus a low base year (2021 owner cash of $1,487M was depressed by working capital: operating cash flow fell that
year from $2,944M to $2,163M while net income rose); "a base year in which earnings were poor can produce a breathtaking,
but meaningless, growth rate" **[L2005-003]**, and carried ten years it traces to "absurdities" **[M1999-067]**. I
therefore cap the shown-growth case at the sales growth shown, **8.7%**, and show the uncapped case beside it.

**COMPUTATION** (USD; per share on 388.4M shares; `Test Runs/_research 2026-10-05 ETN/` arithmetic in this session):

| case | growth yrs 1-10 | value at 5.63% | per share | value at 10% | per share |
|---|---|---|---|---|---|
| no growth | 0% | $45.9B | **$118** | $25.9B | $67 |
| shown growth, Q3-capped | 8.7% | $92.3B | **$238** | $47.5B | $122 |
| shown growth, uncapped | 23.2% | $280.4B | $722 | $131.2B | $338 |
| depreciation variant, no growth (mean $2,827M) | 0% | $50.2B | $129 | n/a | n/a |

**Value range: $118 to $238 a share** (Q3-capped), **against $437.83.** Width 2.0 to 1, inside the three-to-one line. The
uncapped range, $118 to $722 (6.1 to 1), is shown for the reader.

**Expected return at the price** (the discount rate at which each case equals $437.83): no growth **1.5%**; capped growth
**3.2%**; uncapped 23.2% growth **8.3%**. Ten-year growth needed to reach a 10% return at the price: **26.9% a year**.

**The floor and the conversion between pre-tax and after-tax.** The floor (CONVENTION) is about ten percent pre-tax
**[M2003-149]**, **[L2002-020]**, **[M1994-004]**. Owner cash is measured after Eaton's corporate income tax. The 2002 row
states the floor as "at least 10% pre-tax returns" and in its parenthesis translates it to an after-corporate-tax figure;
that corporate tax is the holder's own (Berkshire, a corporation, is taxed on what its equities return), so the 10% is the
return to the holder before the holder's tax. I therefore discount Eaton's after-tax owner cash at 10% and read the result
as the buyer's pre-tax return; no grossing-up for Eaton's own tax is done. Had the 10% been read as a pre-corporate-tax
yield on Eaton's own earnings, the after-tax equivalent at Eaton's 2025 effective rate of 17.1% would be 8.3%; at 8.3% the
capped case is worth $152 and the uncapped $436, so the verdict does not change.

**Reported at the owner's request (CONVENTION of reporting, not a rule; COMPUTATION, NOT A CLEARANCE beyond what Q7
itself decides):**
- **Value range:** $118 to $238 a share (Q3-capped); $118 to $722 uncapped.
- **Fair-price band** (prices inside the range at which the expected return is at or above about 10% pre-tax): in the
  capped case, **$118 to $122**, that is, only the very bottom of the range; at the bottom end the no-growth case yields
  only 5.63% (it is valued at the sovereign), so the band exists only if the capped growth is credited. In the uncapped
  case the band would run from $118 to $338.
- **Cheap price** (below which no pencil is needed, because the floor is met with no growth at all): **about $67**, the
  no-growth owner cash capitalized at 10%.
- **The price, $437.83,** is above the top of the capped range and above the uncapped case's 10% value ($338); its
  expected return in the most generous case written (8.3%) is below the floor.

**Closes.** The price sits above the top of the narrower range, and by the PG specific, "a price above the top of the
range closes OUT through the floor convention above". Even uncapped, no case in the range reaches the floor at this
price, so the close does not depend on my cap. This is not a screamer; it would need far more than a pencil **[M2009-005]**,
**[M1996-084]**; "there’s just a point at which we drop out of the game" **[M2003-149]**. The boom-year margin and the
Boyd debt are weighed inside "the degree of certainty" **[M1999-104]** and would only lower the range.

**VERDICT: OUT.** The file closes here.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
**NOT REACHED** (Q7 closed OUT). COMPUTATION — NOT A CLEARANCE: the 30-year Treasury at 5.63% exceeds the expected return
at the price in the no-growth (1.5%) and capped (3.2%) cases; "one opportunity cost of buying the stock is to compare it
with a bond" **[M1997-089]**.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED as a clearance.** Recorded for the file because the facts were read: debt rose from $9.9B (2025) to $20.6B
(2026-06-30), of which $2,088M is commercial paper "used primarily to manage fluctuations in working capital and to
partially fund acquisitions" (10-Q). Net interest ran $201M in Q2 2026 against $71M a year earlier. Ratings A-/A3 stable
(10-K, before the Boyd financing). Against 2025 owner cash of $3.4B, net debt is about six years of owner cash; relating
debt to the ability to pay it **[M1995-104]**, the electrical earnings held through 2009 and 2020, so ruin is not in view,
but the "little or no debt" description **[R1997-001]** no longer fits, and maturities from 2028 must be met or refinanced
**[L2010-020]**. Would weigh AGAINST.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.** Inaction is the default **[M2003-070]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** No named business of the rows (casinos, tobacco, loading schemes) is among Eaton's; nothing in the
documents read would trouble the newspaper test **[M2008-011]**.

---
## THE BOX
**OUT at Q7.** The castle (Q2) is IN on the evidence and the capital needs (Q3) weigh for, but the price, $437.83 against a
value range of **$118 to $238** a share (Q3-capped; $118 to $722 uncapped), gives an expected return of 1.5% to 3.2%
(8.3% at an uncapped 23% ten-year growth), below the ~10% pre-tax floor and below the 5.63% Treasury in the main cases.
Fair-price band $118 to $122 (capped case); cheap price about $67. COMPUTATION figures are as labelled above.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. **Not written question by question with a commit after each**: the brief
      forbade commits, so the file was drafted after the reading and written once; the write-early rule was therefore not
      kept, and this is declared.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every filing fact has its accession;
      non-SEC figures (Schneider, Siemens) are flagged; the retention test's market leg is marked not tested.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 are NOT REACHED and their figures are
      labelled COMPUTATION or recorded without a verdict.
- [x] Owner cash after every real cost (all capex, stock pay), never a net-income proxy; the sovereign from the Treasury;
      the quote flagged as an aggregator's.
- [x] Contrary evidence written down as found (Foundations line, and carried into Q2, Q4, Q6).
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` used; its zero stock-pay column and `cover_shares.py`'s CIK-scaled count
      were found to be defects and replaced from the filings.
- [x] `python tools/check_framework.py` run on 2026-10-05 after the file was written: PASS. A separate script confirmed no
      E-ids, every M/L/R id present in `principle_ledger_v5.csv`, and the quoted fragments beside ids inside their rows
      (one mismatch, a phrase from another row beside M1999-104, found and corrected). Nothing committed (brief).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **Q7's two closes collide.** The convention sends a range wider than three to one to TOO HARD and a
price above the top to OUT, but says nothing of a wide range whose every case is below the floor at the price. The
uncapped range here is 6.1 to 1, and the floor fails at every point in it; I closed OUT because the floor result does not
depend on the width, and because the Q3 cap gives a 2 to 1 range anyway. The convention should say that the floor test is
run first across the whole range, and the width rule applies only where some case clears the floor. (2) **The Q3 cap is
not operational.** "No rate that runs past the discount rate or traces to an absurdity" does not say what to cap to; I
capped owner-cash growth at sales growth shown over the same years, a choice of mine that moves the top of the range from
$722 to $238. A rule for the cap (sales growth shown, or growth in owner cash measured from a base-year average rather
than a single year) would make two analysts agree. (3) **"Pre-tax" in the floor needs one sentence.** The 2002 row's own
parenthesis converts the 10% to an after-corporate-tax figure, and nothing in the framework says whether that corporate tax
is the target's or the holder's; I read it as the holder's and discounted after-tax owner cash at 10%, and showed the
other reading. (4) **The by-parts convention has no threshold for "matters".** Boyd Thermal is about 6% of sales but
$9.55B of capital; I judged it below the line for Q1 and weighed it at Q6. The convention should say whether a part is
measured by earnings or by capital. A smaller note: the template's write-early, commit-after-each rule cannot be kept in a
run whose brief forbids commits; the template could name the alternative (a timestamped draft per question).
