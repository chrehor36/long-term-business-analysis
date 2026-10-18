# Company Run — Gerdau S.A. (NYSE: GGB; B3: GGBR4 / GGBR3) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to its dated name before any fetch** (commit
6da6ac07).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-13), after the run was committed: not held (`PORTFOLIO.md` carries no line for GGB, GGBR4, GOAU or Gerdau).

**Dispatch:** a dispatched purchase run under `Screens/_daily/_dispatch_brief.md`, with the brief's one stated departure
(the lines of evidence derived by the analyst from the 20-F's Items 4, 3.D and 5; see Step 0). Working folder
`Test Runs/_research 2026-10-13 GGB/` (scripts `fetch.py`, `strip.py`, `owner_cash.py`, `balance_sheets.py`, `q7.py`,
outputs `owner_cash.json`, `q7_out.txt`; raw filings in its ignored `cache/`).

**Contamination, declared and not used.** (1) The session opened with the repository's recent commit subjects in view; they
report a v5 run of another steel company (ANIOY, Acerinox) closed OUT at Q2. Not used: nothing in it was read, and this
run's Q2 is decided on Gerdau's and its named rivals' own filings. (2) Before any fetch I ran a directory listing of
`Test Runs/` filtered for "GGB" or "Gerdau" to make sure the dated file name was free; it printed nothing. That listing is
itself inside the blind rule's letter, and it is declared here. (3) The project memory index loaded with the session names
queue counts and other tickers; no line about this company was seen. Nothing else of the blind-listed files was opened.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** GGB ADS **US$ 5.18** (close 2026-10-13); GGBR4 preferred **R$ 25.98**, GGBR3 common **R$ 22.12** (B3 closes
  2026-10-13). Source: Yahoo Finance chart feed through `tools/sources.py` (**aggregator, flagged**, live quotes only per
  operator rule 5). The ADS and the preferred agree at one preferred share per ADS: R$ 25.98 / 5.0096 = US$ 5.19.
- **ADS ratio, from the filings:** the 20-F cover registers "Preferred Shares, no par value per share, each represented by
  American Depositary Shares"; Item 7 states "On December 31, 2025 there were 434,146,847 ADSs outstanding, representing
  33.8% of Gerdau Preferred Shares", and 434,146,847 / 1,283,097,330 issued preferred = 33.8%, so **one ADS = one preferred
  share** (20-F FY2025, filed 2026-03-13, acc 0001104659-26-027678; deposit agreement with JPMorgan Chase, 2019, Exhibit list).
- **Exchange rate:** **R$ 5.0096 per US$**, Banco Central do Brasil PTAX selling rate, 2026-10-13 (BCB Olinda PTAX service;
  issuing authority). Used for every conversion below.
- **Shares by class.** Cover of the 20-F FY2025 (acc 0001104659-26-027678): issued **717,782,619 common** and
  **1,283,097,330 preferred** at 2025-12-31. `python Screens/cover_shares.py GGB` printed 717,782,619 "single class /
  undimensioned", which is the common class only; the tool missed the preferred class and was overridden from the cover.
  Outstanding at 2025-12-31 less treasury: 717,363,819 common and 1,257,780,072 preferred (20-F FY2025, Item 7). **Latest filed
  count:** shares in circulation at **2026-06-30: 717,010,819 common and 1,246,169,820 preferred = 1,963,180,639**
  (interim statements, 6-K of 2026-08-04, acc 0001104659-26-090481, note 17: issued 717,138,819 / 1,268,017,330 less
  treasury 128,000 / 21,847,510). The 6-K of 2026-08-04 (acc 0001104659-26-090500, Exhibit 99.2) cancels 163,100 common and
  6,975,000 preferred treasury shares, which does not change the count in circulation. Buybacks after 2026-06-30 under the
  programme of 2026-02-23 are not in any filing read; the June count is used. The charter note: only the common votes; the
  preferred carry "specific rights" under the bylaws (20-F FY2025, Item 7); both classes are counted as one economic claim per
  share below, and the ADS price (a preferred share) is the price each figure is set against.
- **Rename, merger, spin-off or split in 2026:** none found in the 6-Ks of 2026 read (fifteen filings, 2026-02-23 to
  2026-09-01: 4Q25 results and management report, dividends, three treasury cancellations, the new buyback programme, 1Q26
  and 2Q26 results and interim statements, two purchases of 23.03% stakes in Dona Francisca Energética S.A. closed
  2026-07-20 and 2026-08-06, and a US$ 1.125 billion undrawn five-year credit facility signed 2026-08-31, acc
  0001104659-26-103986). The bonus shares of 2023 (1 for 20) and 2024 (1 for 5) are in the 20-F's share reconciliation.
- **Market cap:** 717.011M × R$ 22.12 + 1,246.170M × R$ 25.98 = **R$ 48,236M = US$ 9,629M**.
- **Sovereign for the earnings currency (BRL):** **12.57%**, the buy rate of **Tesouro Prefixado com Juros Semestrais
  (NTN-F) maturing 2037-01-01**, base date **2026-10-09** (latest in the file), from the Tesouro Nacional's
  `PrecoTaxaTesouroDireto.csv` on Tesouro Transparente (issuing authority). Why this series: the protocol's table has no
  BRL row; the NTN-F 2037 is the longest-dated nominal fixed-rate federal bond the Treasury sells; the long inflation-linked
  bonds (Tesouro IPCA+ to 2060, 6.47% real the same day) are real rates, and Q7 discounts at a nominal rate with zero
  nominal growth after year ten. **CONVENTION of this run:** the longest nominal federal bond stands for the long
  government rate in BRL; rationale: no 30-year nominal BRL bond exists and the framework's construction is nominal.
- **Filings read** (operator rule 4): 20-F FY2025 (filed 2026-03-13, acc 0001104659-26-027678), Items 3.D, 4, 5, 6, 7, 10,
  16 and the financial statements with notes 1 to 32; 20-F FY2023 (2024-03-28, acc 0001104659-24-040516), FY2021
  (2022-03-31, acc 0001104659-22-041058), FY2019 (2020-03-31, acc 0001104659-20-041231), FY2017 (2018-04-03, acc
  0001104659-18-022121), FY2015 (2016-03-31, acc 0001104659-16-108976) for the statements, segments and balance sheets of
  2013 to 2023; the 6-Ks of 2026 listed above, of which the 2Q26 interim statements (acc 0001104659-26-090481) and 2Q26
  results (acc 0001104659-26-090494) and the 4Q25 results (acc 0001104659-26-018601) were read in full. There is no proxy
  for a 20-F filer; Item 6 (directors, pay) stands in for it.
- **One figure cross-checked against the filed statement:** 2025 net sales **R$ 69,858,532 thousand** in the 20-F's
  consolidated statement of income equals the 4Q25 results release's statement (6-K acc 0001104659-26-018601, "NET SALES
  ... 69,858,532") and the XBRL tag (R$ 69,859M). Second check: net debt at 2026-06-30 computed here from the interim
  balance sheet, R$ 8,117.6M, equals the company's own "Net debt 8,118" in the 2Q26 release.
- **`python tools/run.py GGB`:** printed "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." It does not handle this
  IFRS 20-F filer. All arithmetic below is worked from the filed statements in `owner_cash.py`, `balance_sheets.py`, `q7.py`.
- **Owner cash after every real cost, R$ millions** (from the filed cash flow statements; full method in Q4's place under
  AFTER THE STOP). Operating cash with the purchases and sales of short-term investments taken out (the filer reports them
  inside operating cash), stock pay charged (the "long-term incentive plans" add-back reversed), less purchases of PP&E and
  intangibles and lease principal; interest and tax as paid:

  | year | op. cash adj. | capex+intang. | D&A | owner cash, all spending (equity basis) | same, before interest after tax (all-equity) | sales |
  |---|---|---|---|---|---|---|
  | 2017 | 1,525 | 911 | 2,093 | 614 | 1,442 | 36,918 |
  | 2018 | 1,841 | 1,262 | 1,892 | 579 | 1,313 | 46,159 |
  | 2019 | 4,754 | 1,847 | 2,074 | 2,745 | 3,321 | 39,644 |
  | 2020 | 5,644 | 1,805 | 2,499 | 3,592 | 4,239 | 43,815 |
  | 2021 | 11,867 | 3,192 | 2,659 | 8,398 | 9,012 | 78,345 |
  | 2022 | 11,199 | 4,481 | 2,867 | 6,408 | 6,843 | 82,412 |
  | 2023 | 10,295 | 5,336 | 3,047 | 4,571 | 4,819 | 68,916 |
  | 2024 | 9,133 | 5,946 | 3,126 | 2,727 | 3,171 | 67,027 |
  | 2025 | 7,585 | 6,853 | 3,684 | 245 | 1,099 | 69,859 |

  Five-year average 2021 to 2025: R$ 4,470M (equity basis), R$ 4,989M (all-equity). Stock pay resolved: R$ 149M in 2025,
  R$ 152M in 2024, R$ 158M in 2023 (cash flow statement add-back), charged above.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is that a share is a business: "Would I be happy buying this stock if the market
closed for five years?" **[M1997-109]**. The price of the ADS rose from the R$ 16 to R$ 19 a share the company paid in its
own buybacks of 2025 and 2026 to R$ 25.98 today; that rise is no instruction about value, "It just tells us prices"
**[M2006-077]**. No macro forecast enters: the import wave into Brazil and the U.S. tariff are read below only as facts
about the business's cash, "macro conclusions are — just never enter into the discussion" **[M2000-094]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) Gerdau's North America segment earned an operating margin
at or above Nucor's steel mills segment and Steel Dynamics' steel operations in 2022, 2024 and 2025 (Q2's competitor row),
which is evidence for a castle; (2) the literal five-year window, with the maintenance case and no growth, values the
equity-only claim above the price (Q7 computation beside the central figure); (3) the company has bought in 3.0% of its
shares in 2025 and lowered its capital spending plan for 2026 to R$ 4.7 billion from R$ 6.1 billion; (4) against the
business: the filer itself calls its North American products "commodity steel products for which pricing is the primary
competitive factor" and says of Brazil that it "cannot compete with heavily subsidized imports" (20-F FY2025, Item 4).

## THE STANDING RULE
Does owning this put the buyer at risk of ruin? Not on the buyer's conduct as posed: a part-interest bought outright, with no
borrowed money, "borrowed money has no place in the investor's tool kit" **[L2014-005]**, and no position sized so that a
fall in a Brazilian steel company could end the buyer; "We are never going to risk what we have and need for what we don’t
have and don’t need" **[M2012-081]**. The rule is met by the buyer, whatever the questions conclude.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**. The business is plain: three operating
  segments (20-F FY2025, note 27): **Brazil** (long, flat and special steel and the company's own iron ore, R$ 29.7bn of
  2025 sales), **North America** (scrap-fed mini mills in the U.S. and Canada making rebar, merchant bars, structural
  shapes and special bar quality steel, R$ 35.8bn), **South America** (mini mills in Argentina, Peru, Uruguay, R$ 5.6bn).
  Around 70% of the steel is made from scrap (20-F Item 4). The product chemistry needs no understanding; "What is
  important is that I understand the economic dynamics of the industry. Is there — are there competitive moats? Is there
  ease of entry?" **[M2011-014]**.
- **The key variables and whether they are foreseeable** **[M1998-044]**: (i) the spread of the steel price over scrap and
  pig iron in each region; (ii) shipments; (iii) import penetration in Brazil (21% in 2025 by the Brazil Steel Institute,
  as the 20-F reports) and the U.S. trade regime (Section 232, raised to 50% in 2025); (iv) the real against the dollar,
  since more than half of sales are in North America. None of the four is a forecast this run can make, and none is a
  technology that changes the product. A dependence on a commodity price "is never by itself a STOP at Q1 or Q2": "We
  don’t think we can predict commodity prices." **[M2016-025]**, and the business is read "off the figures" **[M2008-069]**.
  Q1 asks whether the economics can be read from the figures; they can: ten years of statements, segment results for
  2015 to 2025, shipments and capacity by segment, the company's own split of capital spending into maintenance and
  competitiveness.
- **Routing.** Not a fast-changing industry (the mini mill and the blast furnace are decades old in its own plants); not a
  bank; a group of operating segments read by its parts, the deciding part as Q2 defines it.
- **Doubt test.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. The
  doubt here is not whether the business can be understood but whether its castle stands, which is Q2's question.
- **VERDICT: IN.** The economics of a regional scrap-based steel maker can be read from its filings and its rivals'; the
  policy and price variables are key and unforecastable, and they are carried to Q2 (the low-cost position) and Q7 (the
  cycle base), where the framework places them.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now. What are the key factors? And how permanent are they?" **[M1995-038]**. The moat is what "protects excellent
returns on invested capital" **[L2007-004]**.

**Lines of evidence chosen (the brief's departure).** From Item 4 (business overview, segments, competition, raw materials,
trade protection), Item 3.D (risk factors: imports into Brazil, Section 232, anti-corruption and antitrust exposure, debt)
and Item 5 (segment results, capital spending by segment and by purpose, liquidity), this run follows seven lines:
(1) segments and their margins over the cycle, 2015 to 2025; (2) competition and the named rivals; (3) trade protection on
both sides (imports into Brazil, U.S. tariffs); (4) capital spending, maintenance against competitiveness, and where it
goes; (5) debt, liquidity and leases; (6) buybacks and their prices, and stock pay; (7) litigation and investigations
(the CADE cartel case, Operation Zelotes, tax claims). Lines 1 to 3 decide Q2; the rest are recorded under AFTER THE STOP.

**The parts table** (business of parts **[L2008-005]**; a part decides at more than half of five-year operating profit,
else the largest). Segment operating profit = gross profit less selling, general and administrative expense plus other
operating income, before equity income and impairments, R$ millions; 2021 and 2022 from the four-segment note of the 20-F
FY2023 (acc 0001104659-24-040516, note 27), 2023 to 2025 from the three-segment note of the 20-F FY2025 (acc
0001104659-26-027678, note 27); worked in `parts.py`. **CONVENTION of this run:** the old Special Steel segment's 2021 and
2022 profit is split between Brazil and North America in the proportions the 2023 recast implies (56.5% / 43.6%, the change
in each segment's 2023 profit between the two notes); rationale: the filer recast only 2023 to 2025; without the split North
America is still the largest part (26,766 against Brazil's 22,930).

| part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year total | share | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| North America | 4,824 + SS 606 | 7,761 + SS 953 | 5,758 | 3,724 | 4,710 | 28,335 | 48.6% | see below | **yes, the largest** |
| Brazil | 11,617 + SS 786 | 5,100 + SS 1,236 | 2,524 | 2,814 | 867 | 24,942 | 42.8% | open on the evidence (below) | no |
| South America | 1,394 | 1,501 | 1,001 | 663 | 443 | 5,002 | 8.6% | not judged | no |

No part carries more than half; **North America decides.** It is a near thing: Brazil carried most of the profit in 2021
and North America most of it from 2022.

**The deciding part is a commodity business, in the filer's own words.** "Rebar, merchant bars and structural shapes are
commodity steel products for which pricing is the primary competitive factor. Due to the high cost of freight relative to
the value of steel products, competition from non-regional producers is somewhat limited. Proximity of product inventories
to customers, combined with competitive freight costs and low-cost manufacturing processes, are key to maintaining margins"
(20-F FY2025, Item 4, Competition). "The Company’s principal competitors include Commercial Metals Company (CMC), Nucor
Corporation, and Steel Dynamics Inc." (same). All three file with the SEC. In a commodity field "being the low-cost producer
is all-important" **[L2000-017]**; "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**; the
low-cost operator is "Another way to prosper in a commodity-type business" **[L2004-007]**. The test is relative, "if your
costs are on parity or less — labor costs — than your other major competitors, that is much more important to you than the
absolute level" **[M2001-013]**, read from the operators' filings, "we would measure it, probably, more by cost of
production" **[M2006-004]**; "The figures are available." **[M2009-059]**. The Brazilian rivals the 20-F names
(ArcelorMittal, Simec, Sinobrás, Aço Verde do Brasil, CSN, Usiminas) belong to the part that does not decide and were not
read; of them ArcelorMittal and CSN file with the SEC and the others do not.

**The competitor row.** No filing read states unit costs for Gerdau North America or its rivals; the same metric available
from all is the segment operating margin, which for a commodity sold at a common regional price is the nearest filed
evidence of relative cost. Gerdau North America: segment operating profit / segment net sales (as above; 2015 to 2022 old
basis, 2023 on the new basis, which adds North American special steel). Nucor: steel mills segment earnings before income
taxes / steel mills total sales including intercompany (10-K FY2019 acc 0001564590-20-007794, FY2022 acc
0001564590-23-002793, FY2025 acc 0001193125-26-071575, segment notes). Steel Dynamics: steel operations segment operating
income / segment net sales (10-K FY2019 acc 0001558370-20-001641, FY2022 acc 0001558370-23-002303, FY2025 acc
0001104659-26-021395, segment notes). CMC: consolidated pre-tax income plus interest expense / net sales, fiscal years to
August, from its tagged 10-K data (XBRL company facts; **transcription, not the filed segment table**; CMC's North America
segment was not read, and the consolidated figure carries its Polish mills).

| year | Gerdau NA | Nucor steel mills | Steel Dynamics steel ops | CMC consolidated (FY Aug) |
|---|---|---|---|---|
| 2015 | 4.1% | n.r. | n.r. | 3.2% |
| 2016 | 1.1% | n.r. | n.r. | 3.9% |
| 2017 | 0.4% | 12.3% | 15.3% | 2.9% |
| 2018 | 5.9% | 17.4% | 19.9% | 4.4% |
| 2019 | 6.2% | 10.4% | 12.5% | 5.8% |
| 2020 | 5.0% | 4.8% | 11.9% | 7.9% |
| 2021 | 17.3% | 32.0% | 31.1% | 8.7% |
| 2022 | 25.0% | 24.0% | 20.5% | 17.6% |
| 2023 | 17.4% | 14.9% | 14.4% | 13.2% |
| 2024 | 11.7% | 9.7% | 12.6% | 8.6% |
| 2025 | 13.2% | 9.5% | 10.6% | 1.4% (pre-tax only) |
| average 2017-2021 | 7.0% | 15.4% | 18.1% | 5.9% |
| average 2022-2025 | 16.8% | 14.5% | 14.5% | 10.2% |
| average 2017-2025 | 11.3% | 15.0% | 16.5% | 7.8% |

The comparison is imperfect and the imperfections are stated: Gerdau's segment includes downstream fabrication and excludes
corporate cost; Nucor's steel mills segment excludes its downstream products and its profit sharing; Steel Dynamics' steel
operations are mostly flat-rolled sheet (64% to 77% of segment sales), not long products. "n.r." = not read. The two
largest named rivals' segments were read over nine years; CMC's segment was not.

**What the row shows, over the whole span.** (a) From 2015 to 2021 Gerdau North America was not the low-cost operator: its
margin trailed Nucor's mills and Steel Dynamics' steel operations in every year read except 2020 against Nucor, by 7 to 15
points in 2017 and 2018, and in 2015 to 2017 the filer wrote down North American assets by R$ 1,882M, R$ 2,779M and
R$ 1,070M (segment notes, 20-F FY2017 acc 0001104659-18-022121), while in 2017 to 2019 both rivals' segments stayed
profitable. The rows say what happens to the high-cost operator in a commodity field, "sooner or later, the nature of a
capitalist society is that the guy with the lower cost comes in and kills you." **[M2001-013]**. (b) From 2022 to 2025 the
position changed: Gerdau North America's margin was at parity with both rivals in 2022 to 2024 and above them in 2025,
through the one year in which its shipments fell (2024: 4,569 kt against 4,735 kt in 2023; 2025: 4,999 kt; 20-F FY2025
Item 4). Parity is what the rows ask of a commodity producer **[M2001-013]**. The filer attributes 2025 to "declining
imports following the reinforcement of tariffs", "a strong customer preference for domestic steel" and data-centre and
renewable demand (20-F FY2025 Item 4), and the 4Q25 release records a shift of the mix away from rebar and semi-finished
products (6-K acc 0001104659-26-018601).

**The other castle tests, for the deciding part.** *Pricing power:* none the filer claims; price is "the primary competitive
factor", and a business whose price the field sets is the one the rows warn of, "whatever he charged for gas was my price"
**[M2012-109]**, **[M2023-079]**. *The money test:* a well-funded entrant can build a mini mill, and the field keeps doing
so (the filer's own Midlothian expansion of 150 kt, startup 2H26, 4Q25 release); "If the answer had been yes, we wouldn’t
have done it." **[M2011-015]**. *What keeps it standing:* regional freight (rebar within about 350 miles of the mill,
merchant bar within 500, Item 4) and, since 2018, the U.S. tariff wall, which the filer says "will influence greater
capacity utilization and further improve the competitiveness of the Company’s operations in the U.S." (20-F FY2025,
Item 3.D). *What could destroy, modify or reduce it* **[M2000-014]**: the tariff is a government's to change, and the rows'
own narrated error with a return set by government is plain, "I did not anticipate or even consider the adverse
developments in regulatory returns" **[L2023-011]** (a row about one industry, weighed, not a verdict). *Fewness of rivals
cures nothing*: "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**. *Widening or
narrowing* **[M1999-108]**: narrowing to 2021, widening since 2022 on the row above.

**The field's returns over the last full cycle.** Not ordinary for the two leaders: Nucor's steel mills earned 19% pre-tax on
segment assets in 2019 ($1,791M on $9,283M), 7% in 2020 ($720M on $9,708M) and 51% in 2022 ($7,199M on $14,157M); Steel
Dynamics' steel operations 20% in 2019 ($1,031M on $5,171M) (same 10-Ks). The rule that a standing castle protecting only
ordinary returns closes OUT does not apply to this field. Gerdau North America earned 13.3% pre-tax on its segment assets in
2025 (R$ 4,710M on R$ 35,468M, which include most of the group's goodwill and R$ 2.9bn of joint ventures), 9.4% in 2024 and
19.1% in 2023 (20-F FY2025 note 27).

**The part that does not decide: Brazil, open on the evidence.** Operating margin 8.1% (2023), 9.3% (2024), 2.9% (2025)
(note 27). The filer: "Although the Company is a modern and highly efficient producer, it cannot compete with heavily
subsidized imports" (Item 4); imports a record "for the third straight year" (Item 3.D); a R$ 1,964.5M impairment of the
Brazil segment in December 2025, the whole of its goodwill and R$ 1,591M of fixed assets (note 29); "Gerdau may consider
restructuring its operations in Brazil" (Item 3.D). "we do not want to buy into a business that has a very high labor
content and that has a product that can be shipped in from abroad very easily" **[M2007-116]**. Under the parts convention a
part that does not decide and is open is carried to Q7 as an ordinary business at no growth; the Q7 computation below is at
no growth throughout.

**The judgment.** The deciding part sells a commodity at a price the field sets; it was not the low-cost operator over
2015 to 2021 on its own and its rivals' filings; it has been at or above parity since 2022. That is a change for the
better, and the framework credits such a change only on the evidence of a full cycle in which the price behaviour held (Q2,
Change, the CONVENTION of 2026-10-06 as amended 2026-10-10), from the rows "you learn a lot about the durability of the
economics of a business by observing the behavior of — the price behavior" **[M2005-020]** and "view last year's figures as
reflecting a cyclical problem, not a secular one" **[L1995-022]**. The change happens, "the railroads were a terrible
business for decades and decades and decades and then they got good." **[M2017-026]**, but the span of 2022 to 2025 is the
top and the first easing of one cycle under a rising tariff wall, with one year of a 3.5% fall in shipments; it is not a
full cycle. Whether parity holds through a U.S. downturn and under whatever trade regime follows is a forecast no filing
states and no further reading of 2025 documents can answer; "We couldn't solve this problem, moreover, even if we were to
spend years intensely studying those industries." **[L1993-023]**. A castle whose future cannot be judged is "too hard"
**[M2000-019]**, **[M2006-013]**. It is not OUT on this evidence: the most recent four years, read against the same rivals,
are evidence for the castle, and the high-cost years are before the change.

- **VERDICT: TOO HARD (NATURE)** at Q2, on the change for the better in the deciding part (North America). **Dated re-look
  condition:** the first fiscal year after FY2025 in which Gerdau's North America segment shipments fall below the prior
  year's (4,999 kt in 2025), or in which the U.S. field's shipments fall as Nucor's steel mills segment and Steel Dynamics'
  steel operations report them; the question is then put again with that year's segment margins against the same two
  rivals' segments. The 2024 dip (shipments down 3.5%) is recorded above, with the margin at parity in that year; this run
  reads one mild year as not the full cycle the convention asks for (see WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR).

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (the file closed at Q2).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED as a verdict; the balance sheets are read below under AFTER THE STOP, as the template asks when the file closes before Q4.
## Q5 — WHO RUNS IT. NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7 — WHAT IS IT WORTH. NOT REACHED as a STOP; the reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.
## Q8 — BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 — COULD IT RUIN US. NOT REACHED.
## Q10 — THE FAT PITCH. NOT REACHED.
## Q12 (optional) — PROUD OF HOW THE MONEY IS MADE. NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q2**: the deciding part (North America, 48.6% of five-year segment profit) sells
commodity steel at a price the field sets; it was not the low-cost operator against Nucor's mills and Steel Dynamics'
steel operations from 2015 to 2021 and has been at or above parity since 2022; that change for the better has not been
tested by a full cycle, and only a downturn can test it. **Re-look:** the first fiscal year after FY2025 in which Gerdau's
North America shipments, or the U.S. field's as Nucor and Steel Dynamics report them, fall; the question is then put again
on that year's segment margins. **Integrity facts recorded, not judged** (the CADE long-steel cartel fine; Operation Zelotes;
see AFTER THE STOP, Q5). COMPUTATION, NOT A CLEARANCE, beneath the stop: value range **R$ 10.17 to R$ 14.68 a share**
(all-equity; US$ 2.03 to 2.93 per ADS) against **R$ 25.98 (US$ 5.18)**; no case earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts already found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; no
verdict; the box unchanged, operator rule 2.)*

**Bearing on Q3 (capital in, earnings out).**
- Capital spending (PP&E and intangibles) 2021 to 2025: R$ 25.8bn against depreciation and amortization of R$ 15.4bn
  (cash flow statements, 20-F FY2023 and FY2025). The filer splits 2025's R$ 6.1bn into 41% maintenance and 59%
  "Competitiveness" (4Q25 release, acc 0001104659-26-018601) and estimates maintenance at "nearly R$3.0 billion/year over
  the next five years" (20-F FY2025 Item 4); "Maintenance projects are associated with the concept of reinvestment of
  depreciation" (same).
- Where it went: 77% of 2025 capital spending (R$ 4,734M) and 73% of 2024's (R$ 4,501M) to the Brazil segment, the part the
  filer says "cannot compete with heavily subsidized imports" and impaired by R$ 1,964.5M in December 2025; North America
  received R$ 1,227M and R$ 1,454M (20-F FY2025 Item 5). The Miguel Burnier mining platform (5.5 Mt/yr of iron ore) was at
  91% physical progress at 4Q25 (4Q25 release).
- What the spending has bought so far, on the filed record: consolidated shipments 11,323 kt (2023), 10,984 kt (2024),
  11,360 kt (2025) (20-F FY2025 Item 4); owner cash after all spending fell from R$ 8,398M (2021) to R$ 245M (2025) (Step 0).
- Pre-tax return on capital employed, consolidated, 2025: operating income before the impairment R$ 5,704M (R$ 3,739M +
  R$ 1,965M) against equity of R$ 53,585M plus net debt of R$ 7,807M, 9.3% (20-F FY2025 statements).

**Bearing on Q4 (the numbers). The balance sheets first, ten year-ends** (R$ millions; filed consolidated balance sheets in
the 20-Fs FY2017, FY2019, FY2021, FY2023, FY2025; debt = short-term debt + debentures + long-term debt; leases and FIDC
receivable-fund obligations shown apart; `balance_sheets.py`):

| year-end | cash + short-term inv. | debt | net debt | FIDC | equity (parent) | goodwill | equity less goodwill | inventory / sales | receivables / sales | PP&E | retained earnings |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 6,088 | 20,583 | 14,495 | 1,007 | 24,028 | 9,470 | 14,558 | 16.8% | 9.5% | 19,352 | 3,763 |
| 2017 | 3,377 | 16,510 | 13,133 | 1,135 | 23,645 | 7,891 | 15,754 | 18.2% | 7.6% | 16,444 | 3,315 |
| 2018 | 3,350 | 14,907 | 11,557 | 938 | 25,731 | 9,112 | 16,618 | 19.9% | 6.9% | 15,546 | 4,806 |
| 2019 | 6,295 | 16,050 | 9,755 | 1,018 | 26,956 | 9,469 | 17,486 | 19.3% | 6.7% | 15,902 | 5,645 |
| 2020 | 7,658 | 17,515 | 9,857 | 987 | 30,860 | 12,104 | 18,757 | 20.9% | 8.5% | 17,253 | 7,292 |
| 2021 | 6,787 | 14,040 | 7,253 | 46 | 42,604 | 12,428 | 30,177 | 21.5% | 6.9% | 18,742 | 17,838 |
| 2022 | 5,435 | 12,608 | 7,172 | 0 | 46,116 | 11,634 | 34,482 | 21.6% | 6.1% | 20,423 | 22,173 |
| 2023 | 5,344 | 10,893 | 5,550 | 0 | 49,059 | 10,825 | 38,234 | 22.1% | 7.1% | 22,880 | 25,915 |
| 2024 | 8,277 | 13,636 | 5,360 | 0 | 57,949 | 13,853 | 44,096 | 24.6% | 7.7% | 29,591 | 24,238 |
| 2025 | 6,375 | 14,182 | 7,807 | 0 | 53,585 | 11,996 | 41,590 | 21.1% | 6.9% | 30,641 | 23,054 |

What the figures say **[M2025-032]**: net debt was cut from R$ 14.5bn (2016) to R$ 5.4bn (2024) with the asset sales of
2016 to 2018 (Spain, Chile, the Beaumont wire-rod mill, two hydro plants, R$ 4.0bn of proceeds in 2018 alone) and the boom
cash of 2021 and 2022, and has turned up again to R$ 7.8bn (2025) and R$ 8.1bn (2026-06-30) as capital spending, buybacks
and dividends ran above owner cash. Equity more than doubled, most of it the retained earnings of 2021 to 2023 and currency
translation in "other reserves"; the share capital rose from R$ 19.2bn to R$ 24.3bn by capitalized reserves (the bonus
shares). Goodwill moves with the real against the dollar (most of it is North American). Inventory has run at 21% to 25% of
sales since 2020 against 17% to 18% in 2016 and 2017. PP&E nearly doubled from 2017 to 2025 (R$ 16.4bn to R$ 30.6bn) with
heavy spending and translation. What they do not say: how much of the 2024 and 2025 operating cash came from the use of
tax credits recognized in 2020, 2021 and 2023 (non-cash "tax credits recovery" of R$ 1,359M, R$ 1,182M and R$ 1,098M in the
income account, and a R$ 1,882M fall in "other receivables" in the 2024 cash flow).
- The real costs and the recurring "one-time": impairments in 2015 (R$ 4,996M), 2016 (R$ 2,918M), 2017 (R$ 1,115M), 2020
  (R$ 412M), 2024 (R$ 200M) and 2025 (R$ 1,965M); gains booked outside operations in 2021 (Eletrobras compulsory loan
  recovery R$ 1,391M) and the tax credit recoveries above. Stock pay R$ 149M to R$ 158M a year 2023 to 2025, added back in
  operating cash and charged in Step 0's owner cash.
- EBITDA in the filer's own mouth: the chief operating decision maker evaluates the segments "using Adjusted EBITDA"
  (20-F FY2025 note 27); the quarterly releases feature Adjusted EBITDA and "Net debt/Adjusted EBITDA 0.69x" (2Q26 release,
  acc 0001104659-26-090494). By the framework's section A this is recorded as a weighing against at Q4 and carried to Q5:
  "The one figure we regard as utter nonsense is the so-called EBITDA" **[M1998-086]**; **[L2016-006]**.
- Earnings guidance: none found in the releases read; the company publishes its capital spending plan and its maintenance
  estimate.

**Bearing on Q5 (integrity facts recorded, not judged).**
- **The CADE cartel case.** "A lawsuit was filed based on a request by two civil construction unions in the state of São
  Paulo alleging that Gerdau and other long steel producers in Brazil share customers, thus violating the antitrust
  legislation. After investigations [...] the final opinion was that a cartel existed", with a fine on 2005-09-23 equal to 7%
  of the prior year's gross revenue (R$ 245,070 thousand, updated to R$ 417,820 thousand at 2013-08-01); the effects are
  suspended on a bank guarantee; the company's two suits against the investigation were dismissed and the appeals rejected
  (20-F FY2025, legal proceedings).
- **Operation Zelotes.** The Federal Police investigated whether taxpayers "attempted to influence the decisions of the
  Administrative Board of Tax Appeals (CARF) through illegal means"; on 2016-02-25 it "came to Gerdau’s premises to execute
  court ordered searches and seizures" and interviewed individuals "including its former Chief Executive Officer and another
  former Board member"; outside counsel reporting to a special board committee investigated "certain matters relating to
  CARF proceedings and ultimately political donations by Company entities"; the investigation concluded and was reported to
  the Board and the SEC, whose staff closed its inquiry (20-F FY2019, acc 0001104659-20-041231, Item 3.D; also 20-F FY2017).
  The 20-F FY2025 no longer mentions it (text search).
- Control: Metalúrgica Gerdau S.A. is the controlling shareholder and "Indac – Ind. e Com. S.A. (holding of Gerdau’s family)
  is the ultimate controlling shareholder"; only the common shares vote (20-F FY2025 note 23, Item 7). The ADS holder owns a
  non-voting preferred share.
- Any later run that reaches Q5 must answer these facts **[M2013-088]**.

**Bearing on Q6 (the money and the owners).**
- Buybacks: 2025 programme completed, 63,000,000 preferred at an average R$ 16.27 and 1,500,000 common at R$ 15.65 (20-F
  FY2025 note 23); 2026 programme (approved 2026-02-23, up to 55,000,000 preferred and 1,441,120 common): by 2026-06-30,
  16,013,200 preferred for R$ 304,891 thousand (R$ 19.04 average) and 353,000 common for R$ 6,382 thousand (R$ 18.08)
  (interim note 17, acc 0001104659-26-090481). The programmes are stated by share count; no price above which buying stops
  was found in the filings read **[L2016-002]**. Against the computed range below: the prices paid (R$ 15.65 to R$ 19.04)
  sit above its bottom (R$ 10.17 all-equity, R$ 12.11 equity-only). This line is written back here as Q6's buyback test
  asks; it is not weighed, the file having closed at Q2.
- Payout: "R$2.4 billion in shareholder remuneration, including dividends and share buybacks, or a payout of 182%" in 2025
  (4Q25 release); dividends paid R$ 1,286M (2025), R$ 1,656M (2024), R$ 2,683M (2023) (cash flow statements).
- Deals: purchases of businesses and joint-venture capital R$ 790.6M (2025), R$ 647.6M (2024), R$ 477.2M (2023); disposals
  of Diaco and Gerdau Metaldom (announced January 2024; proceeds in 2024's R$ 1,560M); no share-paid deal found.

**Bearing on Q8 and Q9.**
- The bond: the NTN-F 2037 yields 12.57%; owner cash at the price yields 6.2% to 8.5% on every case of the cycle-based range
  (below) **[M1997-089]**, **[M2007-095]**.
- Debt at 2026-06-30: gross R$ 13,558M (short-term R$ 588M, debentures R$ 4,406M, long-term R$ 8,564M), cash and short-term
  investments R$ 5,440M, net R$ 8,118M; leases R$ 1,612M apart; a US$ 1.125bn undrawn facility to August 2031 (6-K acc
  0001104659-26-103986). Net debt is 7.8 times 2025's all-equity owner cash (R$ 1,099M) and 2.4 times the cycle average
  after all spending (R$ 3,586M). Provisions for tax, civil and labour claims R$ 2,383M (interim balance sheet). "Even a short
  absence of credit can bring a company to its knees." **[L2010-020]**.

### COMPUTATION, NOT A CLEARANCE (Q7's construction, for the owner's two reporting figures; operator rule 3)
*(Computed under Part VII, The owner's price, after the stop at Q2; no entry language; nothing here is a verdict.)*
- **Basis.** Owner cash after every real cost, after the company's own tax as paid, from Step 0's table (`owner_cash.py`).
  All-equity (central): owner cash plus interest paid less interest received, both after a 34% shield (**CONVENTION of
  this run**: the Brazilian statutory income tax and social contribution rate stands for the shield; rationale: the
  borrowing is mostly Brazilian and the filer reports no split) against market value plus net debt. Equity-only beside.
- **Net debt:** R$ 8,117.6M at 2026-06-30 (borrowings and debentures less cash and short-term investments; equals the
  company's own figure), plus the R$ 451.3M dividend the interim filing states as a subsequent event (paid 2026-09-11) =
  **R$ 8,568.9M**. Leases (R$ 1,612M) left out and their whole cost kept inside owner cash (**CONVENTION of this run**:
  under IFRS 16 every lease is on the balance sheet; the framework leaves operating leases out of net debt, and charging the
  lease payments in owner cash charges them once). The two Dona Francisca stake purchases closed after June are not in
  that filing's subsequent events and are left out (each "implies an enterprise value of R$150 million", 6-Ks of 2026-04-16
  and 2026-06-15).
- **(a) The cycle base.** The literal window is 2021 to 2025; its first year is aberrational on the filer's own
  description, U.S. steel prices that "rose to record breaking levels" and raw materials at "record levels throughout 2021"
  (20-F FY2021 Item 4) **[L2005-003]**, and owner cash that year was the highest of the eleven read. The base is therefore
  the last full cycle of owner cash, trough to trough: **2017 to 2025** (troughs 2017 and 2018, peak 2021, the 2025 low the
  filer calls a year of a "challenging and volatile global steel environment" with the Brazil impairment). **CONVENTION of
  this run:** 2025 is taken as the closing trough; rationale: the series fell for four straight years to its lowest since
  2018 and the first half of 2026 is higher (2Q26 operating income R$ 2,332M against R$ 1,485M a year earlier), so 2025 is the
  latest low on the record; whether it is the cycle's low no filing can say.
- **Growth.** Across the cycle the maintenance series changes sign (2017 negative) and the halves test is driven by the
  peak; no earlier cycle was computed. By (b) the range is the no-growth case alone, said so. **(e) Growth spending:** the
  filing allows the maintenance guess, so the central case is owner cash after maintenance only, taking depreciation and
  amortization (right-of-use depreciation included, standing for the lease cost as well) as the maintenance figure, the
  filer's own concept ("reinvestment of depreciation"); the filer's forward estimate of R$ 3.0bn a year sits below 2025's
  R$ 3.68bn and would move the nine-year average by under R$ 0.1bn. The growth that the competitiveness spending has bought
  is, on the filed record, none (shipments flat, owner cash falling, the Brazil impairment), so by (e) the inversion holds:
  **the maintenance no-growth case is the top of the range and the all-spending case the bottom.**
- **(c) Purchases of businesses:** gross purchases and joint-venture capital deducted (cycle average R$ 332M a year);
  disposal proceeds not counted as owner cash (**CONVENTION of this run**: the sale of earning assets is not a recurring cash
  stream, and the earnings leave with them; the net-of-disposals reading would add a falling business's sale proceeds to
  its earning power). Net purchases are below half of owner cash: not a serial acquirer. **(d)** working capital is inside
  operating cash. **(f)** no growth is carried, so the cap is not engaged. No signed, unclosed deal at the price date.
- **Cycle averages 2017 to 2025, R$ millions:** all-equity R$ 3,586 (all spending) to R$ 4,700 (maintenance); equity-only
  R$ 2,988 to R$ 4,102.
- **The floor tested first** (about ten percent, after the company's tax): at the price, enterprise value R$ 56,805M
  (R$ 48,236M + R$ 8,569M); the cases yield **6.3% to 8.3%** (all-equity) and 6.2% to 8.5% (equity-only) at no growth.
  **No case earns the floor at the price** **[M2003-149]**. Had Q7 been reached it would have closed OUT on this test,
  whatever the width (1.44 to 1).
- **VALUE RANGE (reporting figure (a)), at the BRL sovereign 12.57%, no growth:**
  - **All-equity (central): R$ 10.17 to R$ 14.68 a share = US$ 2.03 to US$ 2.93 per share and per ADS** (whole business
    R$ 28,528M to R$ 37,391M, less net debt R$ 8,569M, over 1,963.18M shares; PTAX 5.0096).
  - Equity-only: R$ 12.11 to R$ 16.62 a share = US$ 2.42 to US$ 3.32.
  - Against the price of **R$ 25.98 (US$ 5.18) per preferred share and ADS** (the common at R$ 22.12).
- **The literal window, shown beside (not the central figure):** 2021 to 2025 averages, all-equity R$ 4,614M (all spending)
  and R$ 7,084M (maintenance). No growth: R$ 14.33 and **R$ 24.34** a share (all-equity), R$ 16.59 and **R$ 26.60**
  (equity-only); the maintenance cases yield 12.5% and 13.6% at the price and would clear the floor. Carrying the shown
  decline (maintenance, -20.5% a year 2021 to 2025, all-equity) gives R$ 4.92; the all-spending decline is meaningless
  (2025 near zero). This is the window the cycle rule (a) exists to replace: its first year is the record year.
- **FAIR PRICE (reporting figure (b)), Part VII:** each end case valued at ten percent, the two averaged, after the
  company's own tax. **All-equity (central): R$ 16.74 a share = US$ 3.34 per ADS** (ends R$ 13.90 and R$ 19.57).
  Equity-only beside: **R$ 18.06 = US$ 3.60** (ends R$ 15.22 and R$ 20.89). No cheap price is reported.
- **Note on the rate.** The BRL long government rate (12.57%) is above the floor (10%), so the fair price (at 10%) sits above
  the top of the value range (at 12.57%); see WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 6da6ac07); written question by question; committed after Step 0 to
      Q1 (e4d66d6c), after Q2 (d3fd88f7), and after this close.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (not checked
      by the analyst); the fold and the position note are the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. **One breach of the letter, declared:** a
      directory listing of `Test Runs/` filtered for this name, run before the first fetch, which printed nothing. Commit
      subjects about another steel company's run were in view at the start; declared under contamination, not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check script
      `check_ids.py` in the research folder, PASS); no E-ids; every filing fact carries its accession; numbers carry a filing
      or a CONVENTION label.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; everything after it is under AFTER THE STOP or
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (securities taken out of operating cash, stock pay charged, all capital spending,
      lease principal), never a net-income proxy; the sovereign from the issuing authority (Tesouro Nacional, named and
      dated); the exchange rate from the Banco Central do Brasil; aggregator quotes flagged.
- [x] Contrary evidence written down as found (foundations, and the competitor row's 2022 to 2025 years carried into the
      judgment); facts for later questions under AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] `tools/run.py` printed only "UNRESEARCHED" for this IFRS filer; nothing from it was used. `cover_shares.py` gave the
      common class only and was overridden from the cover.
- [x] `python tools/check_framework.py` PASS before the final commit (see the commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The change-for-the-better re-look had already fired.** Q2's convention credits a change only "on the evidence of a full
cycle" and sets the re-look at "the first fiscal year in which the business's volume or its field's volume falls". Here
that year (2024, North America shipments down 3.5%) had already passed before the run, and the margin held at parity in
it. The text does not say whether the first fall after the change is itself the test, or only the trigger to look again
for a full cycle. This run read it as the trigger, judged one mild year under a rising tariff wall not to be a full cycle,
and set the re-look at the next fall; a reader who takes the fall as the test would close Q2 IN on the same table.
(2) **The floor sits below the long government rate.** In BRL the long nominal rate (12.57%) is above the floor of about ten
percent, which the speakers stated "in a world of 7 percent long-term bond rates" **[M1994-004]** and said would move with a
lasting change in rates **[M2003-151]**. The text applies "about ten percent" without saying what happens when the
sovereign is higher; the result is that the fair price (at 10%) exceeds the top of the value range (at the sovereign),
which reads oddly to the operator. This run applied the text as written and reports the bond comparison (Q8) beside it.
(3) **No 30-year nominal sovereign in the earnings currency.** The protocol's table has no BRL row; the longest nominal
federal bond (NTN-F 2037) was used and confessed as a CONVENTION of this run.
(4) **The parts threshold across a segment recast.** The filer changed its segments in 2025 and recast only 2023 onward,
so the five-year parts share needed an allocation of the old Special Steel segment; the threshold paragraph does not say how
to treat a recast that does not cover the window. A CONVENTION of this run split it by the 2023 recast; the deciding part
did not change either way.
(5) **Leases under IFRS 16.** The basis paragraph says "finance leases" in net debt and "operating leases left out"; an IFRS
filer has no such split. This run kept all lease cost inside owner cash and all lease liabilities out of net debt, and said
so.
(6) **Disposal proceeds under specific (c).** "net of businesses sold" would credit a net seller (2017 to 2025 net
disposals R$ 3.5bn) with its sale proceeds as if recurring; this run deducted gross purchases and left disposals out, as a
confessed CONVENTION.
(7) **Tooling.** `tools/run.py` returns UNRESEARCHED for an IFRS 20-F filer, and `Screens/cover_shares.py` reports one class
for a two-class Brazilian filer; both were worked around from the filings.
