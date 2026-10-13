# Company Run — ITOCHU Corporation (TSE: 8001; US OTC ADR: ITOCY) — 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session (overnight cycle, 2026-10-12), after the run was committed: `PORTFOLIO.md` names no ITOCHU Corporation (8001, ITOCY); not held.*

**Dispatched run.** Brief: the canonical brief (`Screens/_daily/_dispatch_brief.md`) with three stated departures (lines of
evidence derived by the analyst from the company's own annual documents; competitors those the company's documents name; a
non-SEC registrant, so the primary documents are the company's own). Template copied 2026-10-12 before any fetch.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
*ITOCHU is not an SEC registrant. `python tools/run.py ITOCY` printed "not an SEC filer ... UNRESEARCHED, not UNKNOWABLE" and
`python Screens/cover_shares.py ITOCY` printed "NOT AN SEC REGISTRANT"; neither tool returned a figure. Every figure below
is by hand from the company's own documents (operator rule 5, primary filings), each named with its date in place of an
accession number. Working arithmetic: `Test Runs/_research 2026-10-12 ITOCY/scripts/q7.py`; extracted statement pages:
`Test Runs/_research 2026-10-12 ITOCY/extracts/`.*

- **Price:** ¥2,155 per Tokyo share (TSE 8001, close 2026-10-09, the last Tokyo session before this run; 2026-10-12 is a
  Japanese holiday). ITOCY ADS $13.62 (close 2026-10-12). USD/JPY 158.56 (2026-10-12). All three from Yahoo Finance's chart
  service: **AGGREGATOR, flagged** (operator rule 5, live quotes only).
- **ADS ratio: 1 ADS = 1 share**, from the depositaries' post-split amendments filed with the SEC: Citibank F-6 POS of
  2026-01-05 (accession 0001193805-26-000004: "representing the right to receive one (1) share of common stock"),
  JPMorgan F-6 POS of 2025-12-17 (0001193805-25-001740) and Deutsche Bank F-6 POS of 2026-01-09 (0001104659-26-002352),
  each "one (1) share". The Bank of New York Mellon amendment of 2025-12-08 (0001019155-25-000479) states the ratio only on
  the face of the receipt, not read. Before the split Citibank's ADS was two shares (424B3 of 2010-12-20,
  0001193805-10-003125). Which of the four unsponsored programmes trades as ITOCY is not stated in any filing read; all
  amended ratios read agree, and the quotes agree (¥2,155 / 158.56 = $13.59 against $13.62).
- **Shares:** issued 7,924,447,520; treasury 931,394,253 at 2026-06-30 (Q1 results, "Consolidated Financial Results for
  the Three-Month Period Ended June 30, 2026", 2026-08-06, p.1; the layout of that table swaps its two columns, and the
  reading that agrees with the stated quarter's average of 6,990,376,434 shares outstanding is the one used; the treasury
  stock line of the balance sheet, ¥725.6bn at June against ¥728.1bn at March, agrees that treasury shares fell slightly in
  the quarter); outstanding 6,993,053,267 at 2026-06-30, less 93,718,850 shares repurchased to 2026-09-30 under the
  resolution of 2026-08-03 (timely disclosure "Announcement Regarding the Status of Repurchase of Own Shares", 2026-10-01:
  the tender offer's 82,735,750 shares at ¥1,813, settled 2026-09-28, plus market purchases) = **6,899,334,417 shares**.
  Purchases continue to 2027-01-29 (up to 190,000,000 shares or ¥300bn in all). One class. The five-for-one split of
  2026-01-01: every per-share figure below is on the post-split basis.
- **Market cap:** ¥14,868bn (6,899.3M × ¥2,155); $93.8bn at 158.56.
- **Sovereign for the earnings currency (yen):** **4.136%**, the 30-year JGB, Japan Ministry of Finance `jgbcme.csv`,
  row 2026/10/8 (the latest row in the file as fetched 2026-10-12; issuing authority).
- **Filings read** (operator rule 4; documents and dates in place of accession numbers): Financial Information Report 2026
  (FY ended 2026-03-31; English translation including the auditor's report filed under the Financial Instruments and
  Exchange Act; posted 2026-06-12), and the same report for FY2022 to FY2025; the financial sections of the annual reports
  for FY2016 to FY2021; Integrated Report 2025 (posted 2025-09-05); consolidated results for FY2026 (2026-05-01) and its
  supplementary material; Q1 results (2026-08-06) and presentation (2026-08-07); Notice of Convocation of the 102nd
  Ordinary General Meeting (June 2026) and its web disclosure items; timely disclosures of 2026-02-19, 03-02, 03-25, 04-10
  (two), 04-15, 06-22, 08-03 (three), 08-28, 08-31, 09-02 and 10-01; the 2016 statements on the Glaucus report (2016-05-06,
  2016-07-27 twice, 2016-08-01). The fiscal year is named by its March year-end (FY2026 = April 2025 to March 2026; the
  company itself calls that year "FY2025" in its presentations).
- **One figure cross-checked:** net cash provided by operating activities FY2026, ¥1,131,837 million in the English
  Financial Information Report 2026 (p.38), equals 営業活動によるキャッシュ・フロー 1,131,837 (百万円) in the Japanese
  決算短信 of 2026-05-01 (`extracts/ja_crosscheck.txt`).
- **Owner cash** (recast at Q4, computed in Q7): operating cash flow (which carries dividends received, not equity
  earnings), less purchases of property, plant, equipment and intangibles, plus their sale proceeds, less repayments of
  lease liabilities (IFRS 16 puts the rent of the stores and offices there), less dividends to non-controlling interests.
  FY2022 to FY2026, ¥bn: 388.4, 482.5, 567.7, 518.7, 586.6; five-year average **508.8** (equity-only, before purchases of
  businesses). Net purchases of businesses averaged 222.4 a year. Net profit attributable averaged 840.6 in the same years.
- **Balance sheets, ten years** (read here because Q4 reads them first; ¥bn, March year-ends; each from that year's
  statement of financial position):

| FY | Total assets | Cash | Trade recv. | Inventories | Equity-method inv. | PP&E | Goodwill | Intangibles | Borrowings (ST+LT) | Lease liab. | Retained earnings | Treasury | Shareholders' equity |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2017 | 8,122 | 606 | 1,949 | 775 | 1,627 | 680 | 132 | 238 | 2,945 | none | 2,020 | 122 | 2,402 |
| 2018 | 8,664 | 432 | 2,183 | 870 | 1,845 | 813 | 129 | 233 | 2,779 | none | 2,325 | 150 | 2,669 |
| 2019 | 10,099 | 572 | 2,398 | 937 | 1,559 | 1,078 | 392 | 736 | 2,984 | none | 2,608 | 106 | 2,937 |
| 2020 | 10,920 | 611 | 2,114 | 952 | 1,640 | 2,137 | 404 | 759 | 2,877 | 1,179 | 2,948 | 167 | 2,996 |
| 2021 | 11,178 | 544 | 2,123 | 899 | 1,868 | 1,940 | 397 | 729 | 3,155 | 1,064 | 3,239 | 181 | 3,316 |
| 2022 | 12,154 | 612 | 2,459 | 1,077 | 2,289 | 1,936 | 369 | 713 | 2,906 | 1,011 | 3,812 | 241 | 4,199 |
| 2023 | 13,115 | 606 | 2,533 | 1,305 | 2,829 | 1,998 | 367 | 713 | 3,007 | 1,005 | 4,434 | 302 | 4,823 |
| 2024 | 14,490 | 600 | 2,831 | 1,382 | 3,159 | 2,111 | 384 | 744 | 3,358 | 1,039 | 5,032 | 402 | 5,427 |
| 2025 | 15,134 | 550 | 2,835 | 1,482 | 3,561 | 2,231 | 405 | 804 | 3,551 | 1,071 | 5,658 | 560 | 5,755 |
| 2026 | 16,733 | 594 | 3,033 | 1,545 | 4,105 | 2,417 | 428 | 801 | 3,673 | 1,085 | 6,270 | 728 | 6,590 |

  Revenues (¥bn): 4,838 (FY2017), 5,510, 11,600 (IFRS 15, and FamilyMart a subsidiary from September 2018), 10,983, 10,363,
  12,293, 13,946, 14,030, 14,724, 14,823 (FY2026). Two level shifts make the years before FY2020 unlike the years after:
  FamilyMart became a subsidiary in FY2019 (goodwill and intangibles trebled) and IFRS 16 put about ¥1.2tn of leases on the
  balance sheet in FY2020. The reading is in Q4.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is whether I would be content to own this trading house's cash for years
with the market closed, and the answer depends on the cash, which is why owner cash is recast in full below. The market
serves and does not instruct **[M2006-077]**: the stock has risen about threefold since March 2021 (¥718 post-split at the
FY2021 close to ¥2,155), and that rise is no reason to buy. No macro enters **[M2000-094]**: the yen, Chinese steel output
and Japanese rates are not forecast here; the iron-ore price enters only as a property of the deciding part (Q1, Q2). A
currency-related holding is "a bet on how government now, and in the future, will behave" **[M2011-025]**: for a dollar
holder of the ADS that bet is inside the purchase, and it is named, not forecast. Who is paid to tell me: the company's own
presentation features "Record High", "core profit" and achievement rates against its plan; the speakers warn that "you do
not get impartial advice" where fees ride on one answer **[M2020-037]**, and the company's directors are paid on
consolidated net profit (Q6). Margin of safety: "if you have to actually do it on — with pencil and paper, it’s too close to
think about" **[M1996-084]**.

**Contrary evidence, written down as found** **[M1997-127]**: (1) the deciding part's profit swung from a loss of ¥16.7bn
(FY2016) to ¥246.9bn (FY2023) on iron-ore and coal prices; (2) owner cash runs at about 60% of reported net profit (equity
earnings count only as the dividends that arrive; store leases are real rent); (3) in FY2015 two investments (a Colombian
coal company and Ting Hsin) were moved out of the equity method into fair value through other comprehensive income, so the
fall in the coal investment in FY2016 (a ¥46.5bn loss in the parent's own accounts) never reached consolidated net profit
(company statements of 2016-05-06 and 2016-07-27); (4) about ¥731bn is lent to and invested in the vehicle that holds 20% of
CITIC Limited, a Chinese financial conglomerate, against a look-through market value of ¥701bn at 2026-03-31; (5) the
company names its yearly profit plan, reports progress against it and pays its directors on consolidated net profit; (6)
incremental returns: retained earnings rose ¥2,458bn from FY2022 to FY2026 while net profit rose ¥80bn (Q3).

## THE STANDING RULE
Owning a marketable minority stake bought with cash puts no buyer at risk of ruin, provided it is not bought with borrowed
money, "borrowed money has no place in the investor's tool kit" **[L2014-005]**, and not sized so that a fall would force a
sale **[M2012-081]**. The ADS adds a currency exposure for a dollar holder; it cannot call on him. Nothing in this purchase
gives anyone the switch. Passes for the buyer; the target's own debt is Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]**.

**The routing: a holding company read by its parts** (Q1's holding-company paragraph and Q2's business of parts, both
CONVENTIONS of the framework; **[M2023-031]** stays OPEN against them). ITOCHU reports eight Division Companies plus
"Others, Adjustments & Eliminations". Net profit attributable to ITOCHU by segment, ¥bn. The company reports no segment
operating profit; this run uses segment net profit as the measure of each part's "operating profit", a **CONVENTION of this
run**, rationale: it is the only profit the filer reports by part.

| Part | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | Five years | Share |
|---|---|---|---|---|---|---|---|
| Metals & Minerals | 226.0 | 246.9 | 226.1 | 178.4 | 143.5 | 1,020.9 | 24.3% |
| Machinery | 80.0 | 107.1 | 131.6 | 136.5 | 155.6 | 610.8 | 14.5% |
| Others, Adj. & Elim. (incl. CITIC, C.P. Pokphand) | 82.0 | 108.1 | 89.4 | 109.9 | 197.6 | 587.0 | 14.0% |
| Energy & Chemicals | 90.7 | 114.3 | 91.7 | 78.6 | 69.3 | 444.6 | 10.6% |
| ICT & Financial Business | 104.3 | 64.6 | 67.8 | 83.2 | 93.0 | 412.9 | 9.8% |
| General Products & Realty | 105.4 | 94.8 | 66.1 | 69.7 | 60.8 | 396.8 | 9.4% |
| Food | 59.0 | 16.5 | 66.3 | 85.1 | 92.1 | 319.0 | 7.6% |
| The 8th (FamilyMart) | 44.1 | 23.0 | 35.8 | 65.1 | 45.0 | 213.0 | 5.1% |
| Textile | 25.1 | 25.5 | 27.0 | 73.8 | 43.3 | 194.7 | 4.6% |
| Total reported | 820.3 | 800.5 | 801.8 | 880.3 | 900.3 | 4,203.2 | |

*Sources: the segment discussion and segment note of each year's Financial Information Report. FY2022's Energy & Chemicals,
General Products & Realty and The 8th are derived from the FY2023 report's stated changes, FY2023's ICT from FY2024's, and
FY2024's General Products & Realty from the total; the FY2022 column sums to 816.6 against the reported 820.3 (a
restatement or rounding not resolved). Shares are of the reported total.*

No part carries more than half; **the largest part, Metals & Minerals, decides**. "Others" is not a reportable segment and
not a part with economics of its own (it nets corporate items and eliminations); its largest item, the CITIC stake, is
carried to Q9.

**The deciding part.** Metals & Minerals is chiefly ITOCHU Minerals & Energy of Australia: an 8% interest in BHP's Western
Australia iron-ore joint ventures (Mt Newman, Yandi, Mt Goldsworthy, Jimblebar), operated by BHP; 18.1% of CSN Mineração in
Brazil (equity method); coking-coal interests (Fitzroy 30%, Oaky Creek 20%, Maules Creek 15%); and steel trading through
Marubeni-Itochu Steel (Integrated Report 2025, the Metals & Minerals pages). "Owning interests in approximately 30 million
tons of iron ore" (FY2026 supplementary material, 2026-05-01). The company describes the Western Australian operation as "a
vertically integrated operating structure encompassing all key infrastructure, including rail and port facilities, centered
on one of the world's largest iron mines", with "low operating costs" at the newly acquired deposit (Financial Information
Report 2026), and CSN Mineração as able "to produce efficiently and cost-competitively" (Integrated Report 2025).

**Key variables, and how predictable they are** **[M1998-044]**: (1) volume and cost position: long-lived, operated by the
partner, expanding (the Ministers North deposit bought from BHP in FY2026; CSN pellet feed planned for 2028): foreseeable;
(2) the iron-ore and coking-coal price, which sets the year's earnings. The part earned, ¥bn, FY2015 to FY2026: 11.2, a loss
of 16.7, 45.2, 82.5, 79.2, 111.4, 104.1, 226.0, 246.9, 226.1, 178.4, 143.5. The company will not write down even next year's
iron-ore price: its plan prints "N.A." and says "The actual prices are not presented, as they are subject to negotiation
with individual customers and vary by ore type" (FY2026 results, 2026-05-01, p.8).

**Applied.** The economics of a low-cost commodity producer are understood in the speakers' own instances: the two copper
producers, "One is going to go broke at a buck-fifty a pound. And the other one’s going to still be doing fine."
**[M2009-059]**; and an oil producer bought "off the figures" **[M2008-069]**, from a report that is "easy to read.
Understandable." **[M2005-015]**. What can be foreseen of this part in ten years is its competitive position (the low end of
the cost curve, long reserves, the partner's rail and port) and its sign (profitable in every year of the decade but FY2016,
which carried an impairment and a loss on sale in coal). What cannot be foreseen is the price level, so the earnings ten
years out are a range, not a point: "we also have some model in our mind of how far off we can be. I mean there’s some
things we can be way off on" **[M2011-084]**. That range is Q7's work (its cycle specific (a) exists for this kind of case),
not a reason to refuse Q1. The statements do tell me what the future statements will look like, within that range
**[M2008-033]**: volume times the margin over a low cost. Abroad: the governance and tax are Japanese and are read in the
filings (statutory effective rate 31.0%; a board with outside directors and a Governance, Nomination and Remuneration
Committee) **[M2000-141]**.

**The doubt rule, faced.** "if you have doubts about something being into your circle of competence, it isn’t"
**[M2002-092]**. My doubt is about the price of iron ore in 2036, not about how the business makes money; I carry the first
into the range and the margin (Q7) and would send only the second to the box. The strongest case against this verdict is
test 5, whether the insiders would write the forecast down **[M2000-105]**: here the insider will not write down one year of
the price. I read that test as about the economics of the business, which the filings show, rather than the quotation of
its product; that reading is mine, stated as a judgment and not as a row. A run that read it the other way would close here
TOO HARD (NATURE).

**The rows about these companies, weighed and not deciding** (Q2's CONVENTION on a row about one company): the speakers said
of the five trading houses that they "owned a whole bunch of businesses that we could understand as a group, although it
didn’t mean we had deep understanding on any" **[M2023-031]**. Under the framework's by-parts reading this row does not
decide; it is consistent with the verdict and adds nothing to it.

**Not deciding, recorded:** the CITIC stake (in "Others") is a financial conglomerate whose condition "no one probably
knows" with precision **[M2005-068]**; of Chinese banks, "It’s no judgment that there’s anything bad" **[M2007-052]**. Under
the threshold it does not decide; it is weighed at Q9.

- **VERDICT: IN**, on the deciding part (Metals & Minerals, a low-cost iron-ore and coking-coal producer whose position is
  foreseeable and whose price level is carried to Q7 as range width) **[M2012-065]**, **[M2009-059]**, **[M2011-084]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now. What are the key factors? And how permanent are they?" **[M1995-038]**. Read on the deciding part, Metals &
Minerals (Q1's table; Q2's business of parts).

**The castle is cost, not price.** Iron ore and coking coal are commodities: the customer buys tonnes by grade and price, so
the tests of pricing power, share of mind, brand and the low bid (tests 4, 5, 7 and 8) all return the same answer, none, and
the castle has to be the commodity exception: "Another way to prosper in a commodity-type business is to be the low-cost
operator." **[L2004-007]**; "when a company is selling a product with commodity-like economic characteristics, being the
low-cost producer is all-important" **[L2000-017]**; "commodity businesses have risk unless you’re the low-cost producer"
**[M1997-010]**; "Being the low-cost producer, for example, is a terribly important moat." **[M2018-043]**.

**The evidence of the cost position, from the operator's own filing.** ITOCHU's 8% of Western Australia Iron Ore sits in
joint ventures operated by BHP, whose annual report on Form 20-F for the year to 2026-06-30 (filed 2026-08-18, accession
0001193125-26-354647) states: "WAIO maintained its position as the world’s lowest cost major iron ore producer, now for the
seventh year, with a greater than US$10 per tonne cost advantage over its nearest Pilbara competitor"; WAIO cost per tonne
US$19.66 (FY2026) and US$18.56 (FY2025), against revenue of US$23,726M on 254,377 kt of BHP-share sales, about US$93 a
tonne; underlying EBITDA US$14,667M, a margin of 62%. (BHP is ITOCHU's partner and the operator, named as such in
ITOCHU's documents, not a named rival; its filing is read as evidence of the asset ITOCHU part-owns.) ITOCHU's own words:
"vertically integrated ... including rail and port facilities, centered on one of the world's largest iron mines"
(Financial Information Report 2026); CSN Mineração "has built an integrated operations system with all of the important
infrastructure, including railways, ports, and ore-dressing facilities, enabling it to produce efficiently and
cost-competitively" (Integrated Report 2025).

**The castle tests, each with its filing fact.**
1. *Key factors and their permanence* **[M1995-038]**: geology (reserves in long-lived Pilbara hubs; the Ministers North
   deposit added in FY2026 "can utilize existing infrastructure") and owned rail and port. Permanent on a ten-year view.
2. *Without the lord*: ITOCHU is a passive 8% partner; the operator runs it. The castle does not depend on ITOCHU's managers
   at all.
3. *The attacker with money* **[M2011-015]**: a new entrant can add tonnes and lower the price for everyone, but cannot buy
   its way below the lowest cost of an existing integrated system; "there are some industries that are just never going to
   have barriers to entry" **[M2012-106]** is answered here by geology and infrastructure, not by a brand. What the attacker
   can do is take the margin, not the position.
4. *Pricing power, the prayer session* **[M2005-020]**: none; the price is set by the market, and the company will not even
   state its own assumption (Q1).
5. to 8. *Share of mind, brand, the low bid*: not applicable to a bulk commodity; failing answers in kind, which is why only
   the cost exception can carry the part.
9. *Ask the competitors*: not available to me; the operator's statement of its lead over "its nearest Pilbara competitor"
   is the nearest thing in the record read.
10. *Widening or narrowing* **[M1999-108]**: the iron-ore half is widening on the operator's account (lowest cost "for the
    seventh year"; BHP plans ">305 Mtpa (100 per cent basis) by Q4 FY2028"), and ITOCHU is adding ore (Ministers North;
    CSN Mineração raised to about 18% for about ¥120bn in November 2024). The coal half is not: FY2026 carried
    "Extraordinary losses on the group reorganization of Fitzroy (Australian coking coal project)", and the Q1 presentation
    (2026-08-07) speaks of "The turnaround of the two coking coal projects". Coal is the weaker, smaller sub-part.
11. *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**: the company's own list for this
    part names "Decline in commodity prices and steel product prices due to economic downturns or overproduction in demand
    countries" and "Drastic decrease in consumption of existing raw materials by widespread of clean energy" (Integrated
    Report 2025). The first reduces the margin of every producer and leaves the lowest-cost one standing last; the second is
    the twenty-year threat (steel made by direct reduction needs high-grade ore, and coking coal is a blast-furnace input),
    and the company's answer is CSN's high-grade ore for direct-reduced iron. On ten years the blast-furnace demand that
    Pilbara ore and coking coal serve is the business's present, not a forecast I make; on twenty it is a real modification
    of the castle, weighed here and carried to Q7 as a reason the growth case is capped.

**The competitor row.** ITOCHU's documents name no rival by name: they refer to "general trading companies" as a field
(Integrated Report 2025: "No. 1 in the non-resource sector"; "mired in a perpetual fourth-place position among general
trading companies" in 2010) and, for this part, name only partners and operators (BHP, CSN, Glencore, Whitehaven, AMCI,
Allegheny, Norsk Hydro, Ivanhoe). No named rival could be read; this is recorded, not filled from outside the documents.

**The parts table.**

| Part | Share of five-year net profit | Castle (read only for the deciding part) | Decides |
|---|---|---|---|
| Metals & Minerals | 24.3% | lowest-cost iron ore (operator's filing); coking coal weaker | **yes (largest)** |
| Machinery | 14.5% | not read to a verdict (dealerships, North American power, Hitachi Construction Machinery stake, aircraft and ships) | no |
| Others, Adj. & Elim. | 14.0% | not a part; CITIC stake weighed at Q9 | no |
| Energy & Chemicals | 10.6% | not read to a verdict (energy trading, chemicals) | no |
| ICT & Financial Business | 9.8% | not read to a verdict (ITOCHU Techno-Solutions, retail finance) | no |
| General Products & Realty | 9.4% | not read to a verdict (construction materials, pulp, tyres, real estate) | no |
| Food | 7.6% | not read to a verdict (NIPPON ACCESS, the largest food wholesaler in Japan by the company's account; Dole) | no |
| The 8th (FamilyMart) | 5.1% | not read to a verdict (convenience stores) | no |
| Textile | 4.6% | not read to a verdict (DESCENTE) | no |

A part that does not decide and is open is carried to Q7 as an ordinary business at no growth; here the parts are not
valued separately (owner cash is reported only for the whole), so this run carries the whole at the growth convention of
Q7 with the cap, and says so.

**The field's returns over the last full cycle, judged in words** (no figure, by the framework's CONVENTION). The deciding
part's net profit on its segment total assets, from the company's own segment figures: FY2017 5.3%, FY2018 9.7%, FY2019
9.4%, FY2020 13.9%, FY2021 11.4%, FY2022 17.6%, FY2023 19.4%, FY2024 16.1%, FY2025 11.8%, FY2026 8.0%, with a loss in
FY2016. That is after tax and on total assets, not on equity; across a cycle that ran from the FY2016 trough to the FY2023
peak and back, it averages near the middle of that list. The operator's margin on the same ore is the 62% above. These are
not ordinary returns, and the castle that protects them is the cost position, which on the operator's evidence has held
through the whole cycle. "A truly great business must have an enduring "moat" that protects excellent returns on invested
capital." **[L2007-004]**: this part's returns are good, and swing with the price, which is the commodity's nature and Q7's
problem. "you can have only two competitors and they’re still terrible businesses" **[M2013-052]** does not describe a
field whose lowest-cost member makes a 62% margin at the operator's level.

**What weighs against, kept.** The coal sub-part is in turnaround; the twenty-year demand for blast-furnace inputs is
threatened by the company's own account; and "you make a judgment as to the ability of your particular company and product
and management to ward off competitors" **[M2017-012]**: here the warding-off is done by the partner's cost, not by ITOCHU.

- **VERDICT: IN**, on the deciding part: a commodity producer whose castle is the lowest-cost position, evidenced in the
  operator's own filing and held through a full cycle **[L2004-007]**, **[L2000-017]**, **[M2018-043]**; the twenty-year
  threat from cleaner steelmaking and the weak coal sub-part are carried to Q7 and Q9.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
"does it look like it has good economics? Has it earned high returns on capital?" **[M1995-051]**; the grades are the best
business, the second best that reinvests at "a very satisfactory rate", and the worst, "forced to grow to stay in the game"
**[M1998-081]**.

**Return on the capital actually needed** (two measures, never one against the other; ¥bn; from the filed statements).
- *Earnings after depreciation against capital employed.* Capital employed = total equity + borrowings − cash and time
  deposits − goodwill − intangibles (leases left out, their rent being inside earnings): FY2022 about 5,976; FY2026 8,984.
  Earnings = net profit including non-controlling interests plus after-tax net interest on borrowings: FY2022 about 877
  (14.7%); FY2026 about 965 (10.7%). The company's own return on shareholders' equity: 21.8% (FY2022), 17.7%, 15.6%, 15.7%,
  14.6% (FY2026) (Summary, Financial Information Report 2026), with net debt to equity 0.54 falling to 0.46. "we could make
  it almost any number you want if we just used enough leverage" **[M2001-054]** warns against reading ROE alone; the gearing here is
  moderate and falling.
- *Cash earnings against capital spending.* Owner cash before purchases of businesses (all-equity, Q7's definition)
  averaged 523 a year over FY2022 to FY2026, against capital spending on property and intangibles of 213 a year (already
  deducted inside it; a maintenance guess of about 173 is made at Q7) and net purchases of businesses of 222 a year.

**Reinvestment to stand still and to grow.** The business keeps about two thirds of its earnings (dividends paid were
¥1,090bn over FY2022 to FY2026 against net profit attributable of ¥4,203bn; buybacks added ¥544bn). Most of what is kept
goes into stakes in other businesses: equity-method investments rose from ¥2,289bn to ¥4,105bn in the window (Q4), with
cash purchases of stakes and minority buy-outs of ¥1,112bn net. "Every year we spend amounts equal to our depreciation
charge simply to stay in the same economic place" **[L2000-035]**: here capital spending (285 in FY2026) runs above
depreciation excluding the right-of-use assets (about 220).

**The growth arithmetic.** The incremental figures disagree with each other, and both are written down:
- earnings after depreciation before interest rose about 88 (877 to 965) while capital employed rose about 3,008: about 3% on
  the added capital, on a base year (FY2022) that was the deciding part's peak and with yen weakness inflating the capital
  (translation adjustments in equity rose to ¥1,047bn);
- owner cash before purchases rose 198 (388 to 587) against purchases and growth spending of about 1,336 over the same years:
  about 15%, on a base year whose cash was depressed by a working-capital build of about ¥240bn (receivables, inventories,
  payables and other, FY2022 cash flow statement).
"we’re not earning a higher rate of return on capital than we were when we started. We just put way more capital into the
business" **[M2023-081]** is the test; the first measure says it of this window, the second does not. The rows accept the
capital-heavy business as "the second-best choice, still a good choice" **[M2018-055]** where it earns "decent returns on
the incremental sums" **[L2009-012]**; whether ITOCHU's incremental sums earn that is not settled by five years that began
at a commodity peak.

**The caps for Q7.** Owner cash at 4% of revenue (FY2026), the highest share in the filings read about 4.2% (FY2021). The
literal growth of owner cash over the window, 10.9% a year, carried ten years, would need about 7% of revenue on revenue
growing at its own window rate of 4.8%: past anything earned, so specific (f) cuts it (Q7).

- **WEIGHS UNDECIDED**: returns of about 11 to 15% after tax on tangible capital employed, a falling gearing, and
  incremental returns of 3% or 15% depending on whether earnings or cash are measured and on a base year at the deciding
  part's peak **[M1998-081]**, **[L2009-012]**, **[M2023-081]**. The "little or no debt" criterion is applied at Q9.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
"I like to look at balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**.

**The balance sheets first** (the ten-year table is in Step 0). What moved, and why:
- *Equity against goodwill and intangibles.* Shareholders' equity rose from ¥2,402bn (FY2017) to ¥6,590bn (FY2026). Goodwill
  and intangibles jumped from ¥363bn (FY2018) to ¥1,128bn in FY2019, when FamilyMart became a subsidiary, and have since moved little
  (¥1,228bn in FY2026; FamilyMart goodwill ¥214.6bn, a key audit matter). Of the equity rise, ¥1,047bn is translation
  adjustments (a weaker yen on foreign assets), not earned profit; retained earnings rose from ¥2,020bn to ¥6,270bn.
- *Where the kept money went.* Investments accounted for by the equity method rose from ¥1,627bn to ¥4,105bn and other
  investments to ¥1,398bn: the balance sheet of a holder of stakes. This is why the equity-method rule matters below.
- *Cash, receivables, inventory against sales.* Cash has stayed near ¥0.6tn for ten years. Trade receivables (¥3,033bn) and
  inventories (¥1,545bn) grew with revenue after FY2019 (revenue ¥11.6tn to ¥14.8tn; receivables ¥2.4tn to ¥3.0tn): no
  build out of line with sales was found. Advances to suppliers rose to ¥339bn (FY2026 from ¥275bn).
- *Debt.* Borrowings stayed between ¥2.8tn and ¥3.7tn while equity nearly trebled: net interest-bearing debt to equity
  fell from about 0.97 (FY2017) to 0.46 (FY2026). Leases of about ¥1.1tn arrived with IFRS 16 in FY2020; most are
  FamilyMart's stores.
- *Treasury stock* rose from ¥122bn to ¥728bn: the buybacks (Q6).
- *Other comprehensive income.* Comprehensive income attributable exceeded net profit over FY2016 to FY2026 taken together
  (¥7,153bn against ¥6,599bn), mostly from the yen; but in single years losses ran around net profit (FY2016 comprehensive
  income was a loss of ¥144.8bn against net profit of ¥240.4bn).
"what the figures are saying and what they don’t say and what they can’t say" **[M2025-032]**: they say a larger, less
geared holder of stakes; they cannot say what the stakes earn in cash beyond the dividends they send up.

**The real costs.**
- *Depreciation*: ¥458.7bn in FY2026, of which right-of-use depreciation was about ¥239bn ($1,495M at ¥159.88, leases
  note): the stores' rent in another form. The lease repayments (¥259.2bn) are deducted in owner cash; nothing of the rent
  is left out. Depreciation is a true cost **[L2015-004]**; capital spending ran above the non-lease depreciation.
- *Equity-method income*: ¥323.5bn of FY2026's profit before tax was equity in earnings; cash dividends received (all
  sources) were ¥265.6bn. Over FY2022 to FY2026 equity earnings were ¥1,601bn and dividends received ¥1,158bn. Under the
  framework's CONVENTION on equity-method income, owner cash counts the dividends, which operating cash flow already does.
- *Stock pay*: directors' stock remuneration ¥2.8bn in FY2026 (Notice of the 102nd meeting); expensed; immaterial to
  owner cash.
- *"Extraordinary gains and losses"*: present every year (FY2026: the ¥111.4bn gain on selling C.P. Pokphand; the Fitzroy
  reorganization losses; reversals and impairments). The GAAP figure is used throughout; "core profit", which excludes
  them, is not.
- *Tax*: ¥262.0bn on profit before tax of ¥1,199.5bn in FY2026 (about 22%, low because equity earnings arrive after the
  investees' tax); cash taxes paid ¥210.0bn. Owner cash is after cash taxes.

**What the accounts say of the management, the tells.**
- *Featured adjusted figure, plan and progress.* The presentations feature "core profit" beside the consolidated figure, a
  full-year plan, "High achievement rates: 31% for consolidated net profit and 28% for core profit against the full-year
  forecast", and "Record High" (Q1 presentation, 2026-08-07). "a management that regularly attempts to wave away very real
  costs by highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**; "the scourge of earnings "guidance"
  and the desire of CEOs to "hit the number."" **[L2019-006]**. Here the adjusted figure is shown beside GAAP, not in its
  place, and the statutory reports carry GAAP only. Recorded as a WEIGHING against **[M1994-018]**, and carried to Q5.
- *The FY2015 reclassifications.* A Colombian coal investment (Drummond) and Ting Hsin were moved from the equity method to
  fair value through other comprehensive income in FY2015, on the stated ground of lost significant influence (company
  statement of 2016-07-27); the coal investment's fall in FY2016 then went through other comprehensive income, and the
  parent booked a ¥46.5bn loss in its own accounts with "no impact on 'Net Profit attributable to ITOCHU'" (2016-05-06). The
  auditor, Deloitte Touche Tohmatsu, gave an unqualified opinion. "if we find numbers where it looks like people are taking
  the most optimistic interpretation of things that they can under GAAP and all of that, we get very worried"
  **[M1994-079]**. One disclosed, audited choice, ten years ago, whose effect is visible in the comprehensive income line:
  recorded as a WEIGHING against, carried to Q5.
- *No confusion found.* The statements are long but consistent from year to year, segment figures reconcile to the totals
  (one unresolved ¥3.7bn difference in FY2022 from derived figures, Q1), and the key audit matters (FamilyMart goodwill,
  the CITIC investment) are stated with their assumptions. "people don’t obfuscate with numbers, usually, without a
  purpose" **[M2003-029]**: no obfuscation found. The CITIC investment's recoverable amount rests on "the growth outlook of
  the Chinese economy and the impact of relevant regulations on the Chinese financial businesses" (auditor's report): an
  estimate that cannot be checked from here, weighed at Q9.

**The recast earnings for Q7.** Owner cash, not net profit: operating cash flow less capital spending (net of sale
proceeds), less lease repayments, less dividends to non-controlling interests; five-year average ¥508.8bn against average
net profit attributable of ¥840.6bn. The gap is the equity-method rule (about ¥89bn a year of earnings not received as
dividends), capital spending above non-lease depreciation, and working capital.

- **VERDICT on the accounts: IN (no confusion, no suspicion raised by the statements themselves); WEIGHS AGAINST**, for
  the featured core profit, the plan-and-progress reporting and the FY2015 reclassifications, all carried to Q5
  **[M1994-018]**, **[L2016-006]**, **[L2019-006]**, **[M1994-079]**.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
"you judge management by two yardsticks. One is how well they run the business [...] And then the second thing you want to
figure out is how well that they treat their owners." **[M1994-008]**. A marketable minority stake: the people are read from
the documents, not met.

**Who.** Masahiro Okafuji, President & Chief Executive Officer from April 2010 and Chairman & Chief Executive Officer since
April 2018, re-elected at the 102nd meeting (2026-06-19) with 94.05% approval; Keita Ishii, President & Chief Operating
Officer. Nine directors, four of them outside directors, with a Governance, Nomination and Remuneration Committee chaired by
an outside director (Notice of the 102nd meeting; results of voting, 2026-06-22). Mr. Okafuji holds 3,530,936 shares, of
which 2,230,261 are to be provided under the stock remuneration plan; his variable pay was 90.35% of the total.

**Yardstick one: the record against the hand dealt.** The company's own account of where it started: in 2010 ITOCHU "was
mired in a perpetual fourth-place position among general trading companies" (Integrated Report 2025). Net profit
attributable rose from ¥240bn (FY2016, the trough of the resource cycle) to ¥900bn (FY2026); shareholders' equity from
¥2.2tn to ¥6.6tn; and the profit shifted towards the parts that do not depend on resource prices (the company's "No. 1 in the
non-resource sector"). Net debt to equity fell from about 1.2 (FY2016: ¥2,556bn on ¥2,194bn) to 0.46. Read against the hand
dealt, a resource-heavy, under-rated fourth-placed house in 2010, the record is strong. Ability **WEIGHS FOR**.

**Yardstick two and the integrity record.**
- *How they talk about mistakes* **[L2024-003]**: the Integrated Report names them: "Lessons learned from past management
  decisions, such as the investment in TOA Oil Co., Ltd. and the expansion into real estate during Japan's economic bubble,
  have been repeatedly discussed and reviewed at management meetings", and "we have learned from our own experience that
  excessive reliance on a particular business can weaken overall management". Mistakes are named, not forbidden words.
- *The reports* **[M1998-036]**: the Financial Information Report states segment results with their causes, the key audit
  matters with their assumptions, and the losses (Fitzroy, impairments). The CEO's message is long and personal (it
  mentions his Nikkei "My History" column); whether it is the product of an investor relations department **[M2007-083]**
  cannot be told from outside.
- *Habits carried from Q4.* The plan, the progress against it, "core profit" beside the GAAP figure and "Record High":
  "we become downright incredulous if they consistently reach their declared targets" **[L2002-041]**. The plan was revised
  in both directions by segment in August 2026 (Machinery and Energy & Chemicals up on "extraordinary gains and other
  factors"); the record read does not show a habit of meeting the declared figure exactly, and the GAAP figure is the one
  reported. Weighed against, not a doubt about honesty.
- *The FY2015 reclassifications carried from Q4.* An accounting choice that kept a coal loss out of net profit, disclosed
  and audited, in a company whose directors are paid on net profit (Q6). It is the strongest integrity fact in the record,
  and it is ten years old, single, and visible in the comprehensive income line the company itself publishes.
- *The response to a short seller (2016).* The company's statements answered the Glaucus report point by point on the three
  accounting treatments, cited the auditor's unqualified opinion, and also attacked the seller's motive ("the purpose of
  Glaucus is to arbitrary provide their own opinions regarding deterioration in enterprise value of ITOCHU with a short interest"). The answer on the substance was given; the
  attack on motive is tone, not evidence.
- *Owners treated as partners*: the dividend is stated as progressive with a stated minimum (¥44 for the year to March
  2027); buybacks are announced with their method, and the 2026 tender offer was priced at a 15% discount to the lowest of
  four reference prices so that "the interests of shareholders who do not tender their shares" were respected (2026-08-03).
  No selective disclosure found; the company issues "Statement Regarding Media Reports" when the press runs ahead of it
  (2026-08-03, 2026-08-28).
- *Tells of dishonesty searched for* (too good to be true, reports that dance, the stock price in the lobby, serial
  issuance): no instance found in the documents read; no share issuance for acquisitions in the window.

"If you’ve got doubts, forget it." **[M2013-088]**. I have no doubt about honesty from the record read; I have reservations
about incentives (net-profit pay, the plan), which are Q6's. "trustworthiness is more important than the brains"
**[M2015-047]**: nothing in the record shows the brains used against the owners. Love of the business against the money
**[M2000-098]**: a chief executive in post for sixteen years who holds about 1.3 million shares bought or vested and is
owed 2.2 million more on retirement; the rows' test of love after the cheque belongs to whole-business sellers and is not
applied to a hired chief executive here.

**Chairman and chief executive in one person** **[L2014-026]**: Mr. Okafuji has held both since 2018. The row speaks of a
"mediocre CEO"; the record does not show one. Recorded for the successor question: the President & COO, Mr. Ishii, is the
evident second, but no successor is named in the documents read.

- **VERDICT on integrity: IN** (no doubt about honesty found in the record read) **[M2013-088]**, **[M2015-047]**; **ability
  WEIGHS FOR** **[M1994-008]**; the habits carried from Q4 weigh against and are passed to Q6, Part B.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
"the biggest judgment you have to make is how well capital will be deployed in the future" **[M2001-111]**.

**Part A: the money.**
- *The retention test* **[R1995-009]**, **[M1998-110]**. Over FY2022 to FY2026 (post-split per share): earnings 581.5,
  dividends 164.0, retained 417.5 a share. The share price went from ¥718 (FY2021 close, ¥3,590 before the split) to
  ¥1,974.5 (FY2026 close): ¥1,256.5 of market value for ¥417.5 retained, about three to one. The market leg passes. The
  intrinsic leg: owner cash before purchases rose from ¥388bn to ¥587bn while the share count fell, and book value per
  share rose from ¥571.5 to ¥942.8 (part of it translation); the cash leg is mixed by Q3's base-year problem. On the rows'
  test, "at least $1 of market value for each $1 retained", it passes.
- *Buybacks.* Programmes are fixed sums with no stated price ceiling: ¥300bn resolved 2026-08-03 ("at least ¥300.0 billion
  in FY2026", results of 2026-05-01; the company's FY2026 is the year to March 2027), ¥170bn spent in FY2026 and ¥154bn in FY2025 (cash flow statements). Prices paid in
  2026: ¥1,813 in the tender offer (82,735,750 shares, ¥150.0bn) and about ¥2,274 in the market in September (10,983,100
  shares for ¥24.97bn, by difference, disclosure of 2026-10-01). "corporate repurchase announcements almost never refer to a
  price above which repurchases will be eschewed" **[L2016-002]**; "Continuing shareholders are hurt unless shares are
  purchased below intrinsic value." **[L2011-003]**. Under the framework's CONVENTION, a buyback with no stated price weighs
  against unless the prices paid sit at or below the bottom of the Q7 range. **Written back from Q7 (2026-10-12): the bottom of the Q7 range
  is ¥1,466 a share (central, all-equity; ¥1,310 all-spending); the prices paid, ¥1,813 in the tender and about ¥2,274 in the
  market, sit above it. The buybacks weigh against** **[L2016-002]**, **[L2011-003]**.
  How management reasons about buying stock is "a pretty good test" **[M2017-056]**: the August 2026 tender was priced at a
  15% discount to the lowest of four reference prices, offered to cross-shareholding insurers, which shows attention to the
  price paid against the market, not against value.
- *Issuance and deals.* No share issuance in the window; every deal read was paid in cash (CSN Mineração, about ¥120bn,
  2024; DESCENTE, FY2025; Hitachi Construction Machinery to 33.4%, closed April 2026; ITOCHU-SHOKUHIN and Sun Frontier
  Fudousan tender offers, April 2026; DENTSU SOKEN, 38.22% at ¥2,880 a share, about ¥215bn, signed 2026-08-31 and not
  closed; Aviation Capital Group, a basic agreement of 2026-08-03, not definitive). The one STOP here, an all-stock deal by
  an undervalued acquirer **[L2009-019]**, is not triggered. Net purchases of businesses were ¥1,112bn over the window,
  below half of owner cash before purchases (¥1,272bn): not a serial acquirer by the framework's CONVENTION, but close to the
  line, and the pace in 2026 (HCM, ITOCHU-SHOKUHIN, Sun Frontier, DENTSU SOKEN, ACG) is rising. "what is smart at one price
  is dumb at another" **[L2011-003]**: the prices of these deals are not judged here.
- *Dividends.* Progressive, with a stated minimum (¥44 a share for the year to March 2027) and a total payout policy of
  "40% or higher" (2026-08-03). The rows about these companies say "each of the five is applying only about 1/3 of its
  earnings to dividends" **[L2023-008]**: weighed as a row about named companies, not deciding.
- **Part A WEIGHS UNDECIDED**: retention passes on the market leg **[R1995-009]**; the buybacks name no price and were
  paid above the bottom of the Q7 range **[L2016-002]**; acquisitions are paid in cash and are many.

**Part B: the pay, the board and the owners.**
- *Pay* (Notice of the 102nd meeting, business report): six internal directors received ¥5,637M in FY2026: monthly ¥602M,
  performance-linked bonuses ¥1,818M, share price-linked bonuses ¥395M, BIP trust stock ¥569M, restricted stock ¥2,252M.
  "We have net profit (consolidated) as the linked indicator for the performance-linked bonus and performance-linked stock
  remuneration". No charge for the capital used: "When capital invested in an operation is significant, we also both charge
  managers a high rate for incremental capital they employ" **[L1994-019]**; a pay plan tied to consolidated net profit
  rewards retention whatever it earns, and in a business that keeps two thirds of its earnings this is the incentive that
  matters. The share price-linked bonus is measured against TOPIX over two years: closer to what the rows call a "lottery
  ticket" arrangement whose value "is totally out of the control of the person whose behavior we would like to affect"
  **[L1996-018]**, though its relative measure removes the market's ride. Pay tied "to what is actually under the
  reasonable control of the person" **[M2003-019]**: net profit is under management's control in a way the iron-ore price
  is not; the plan does not separate them. Against the rows' praise that the five managements "have been far less aggressive
  about their own compensation than is typical in the United States" **[L2023-008]** (a row about named companies, weighed
  only).
- *The board*: nine directors, four outside; the chief executive also chairs (Q5). Directors' own purchased holdings: the
  chief executive's 1.3 million shares outside the plan; the outside directors' holdings not read.
- *The owners*: the same information for all (timely disclosures in English and Japanese; statements when the press runs
  ahead); a yearly profit plan is published and progress against it reported, the guidance the rows distrust (Q4, Q5).
- **Part B WEIGHS AGAINST**: pay on consolidated net profit with no capital charge **[L1994-019]**, **[M2003-019]**.

## Q7 — WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is the
risk-free interest rate" **[L2000-021]**. The moat and the management enter "as to the degree of certainty that we
attribute to the stream of income" **[M1999-104]**; the range is a range, "working with a range of possibilities is the
better approach" **[L2000-024]**. All arithmetic: `scripts/q7.py`, output in `extracts/q7_output.txt` (¥bn unless per
share).

**The cash input (Q4's owner cash), FY2022 to FY2026.**

| ¥bn | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | Average |
|---|---|---|---|---|---|---|
| Operating cash flow | 801.2 | 938.1 | 978.1 | 997.3 | 1,131.8 | |
| less property, plant, equipment and intangibles (net of sales) | 124.9 | 165.7 | 136.4 | 192.6 | 260.1 | |
| less lease repayments | 267.0 | 261.3 | 252.6 | 260.3 | 259.2 | |
| less dividends to non-controlling interests | 20.9 | 28.5 | 21.4 | 25.6 | 25.9 | |
| **Owner cash, equity-only, before purchases** | 388.4 | 482.5 | 567.7 | 518.7 | 586.6 | **508.8** |
| after-tax net interest on borrowings (interest paid less lease interest less interest received, × (1 − 31.0%)) | −2.0 | 6.4 | 13.4 | 25.9 | 27.7 | 14.3 |
| **Owner cash, all-equity, before purchases** | 386.4 | 488.9 | 581.1 | 544.6 | 614.3 | **523.1** |
| Net purchases of businesses (equity-method and other investments, subsidiaries, minority buy-outs; net of sales) | +136.3 | −217.2 | −471.3 | −360.6 | −199.1 | **−222.4** |
| Maintenance guess: D&A less lease repayments (proxy for right-of-use depreciation) | 137.2 | 148.7 | 167.8 | 189.7 | 199.5 | 168.6 |
| Growth spending above it (capital spending less the guess) | 19.9 | 45.4 | 34.8 | 37.8 | 85.5 | 44.7 |

Working capital is inside operating cash flow and is counted (specific (d)). Equity-method income is counted as the
dividends received, which is what operating cash flow carries (the framework's CONVENTION). The tax is the company's own
cash tax, no conversion (Whose tax). Interest paid is taken to include the lease interest the leases note states (¥13.0bn
to ¥20.8bn a year), which is therefore not added back: leases are left out of net debt and their whole cost stays in owner
cash, said so. The maintenance guess uses lease repayments as the proxy for right-of-use depreciation in every year (for
FY2026 the note gives ¥239.0bn against repayments of ¥259.2bn), a **CONVENTION of this run**, rationale: the
right-of-use depreciation table for the earlier years was not extracted, and the proxy errs towards a larger maintenance
need.

**The specifics applied.**
- *(a) Cycles.* The series that defines the cycle is owner cash as recast, and it is comparable only from FY2020 (FamilyMart
  consolidated from FY2019, IFRS 16 from FY2020); no full cycle of it exists in comparable form. FY2022, the first window
  year, carried a working-capital build of about ¥240bn on high commodity prices (receivables, inventories, payables and
  other, FY2022 cash flow statement), and the deciding part's profit peaked in FY2022 to FY2024. The literal window is used,
  and the growth measured between the window's halves is shown beside: literal 10.86% a year, halves 8.27%.
- *(b) Decline.* No decline in owner cash over the window; the bottom is the no-growth case.
- *(c) Acquisitions.* Net purchases of businesses, ¥1,112bn over the window, are deducted and the total growth credited
  (the default pair). The filer reports no organic growth, so no organic pair is shown. Not a serial acquirer: net purchases
  (¥1,112bn) are below half of owner cash before purchases (¥1,272bn equity-only; ¥1,308bn all-equity). No merger (no deal
  paid in shares) in the window. After year ten the purchases stop with the growth: the terminal is owner cash before
  purchases. *Signed, not closed:* DENTSU SOKEN, 74.71 million shares (38.22% of 195,492,458) at ¥2,880, about ¥215.2bn
  (notice of 2026-08-31), valued beside as if closed: the financing added to net debt, and the target's dividends to a
  38.22% holder credited at nothing because its own filings were not read (stated): **−¥31 a share** on every figure below.
  The Aviation Capital Group agreement of 2026-08-03 is a basic agreement, not a signed definitive deal, and is left out.
  *Closed after the window, before the price date:* Hitachi Construction Machinery's additional stake, ITOCHU-SHOKUHIN and
  Sun Frontier Fudousan (April 2026): their cash is inside the June 2026 net debt, and their earnings are credited at nothing
  (no filed earnings of theirs read), which understates value slightly.
- *(d) Working capital* counted, inside operating cash flow.
- *(e) Growth spending.* The filing allows a guess (the maintenance proxy above, after **[M1998-127]**'s "the depreciation
  charge is not inappropriate in most companies to use as a proxy for required capital expenditures"): the central case is
  maintenance-only in the no-growth case and in the terminal, with the growth spending (¥44.7bn a year) and the purchases
  charged in the ten growth years against the growth they buy; the all-spending case is shown beside.
- *(f) The cap.* The literal growth of 10.86% a year carried ten years would need owner cash of about 6.95% of revenue on
  revenue growing at its own window rate (4.79% a year, ¥12,293bn to ¥14,823bn); the highest share earned in the filings
  read is about 4.2% (FY2021: ¥438bn on ¥10,363bn). The growth is cut to the business's own sales growth, 4.79%, and that is
  above the discount rate, so it is carried at **4.136%**, never above the discount rate.
- *The four PG specifics:* growth on aggregate owner cash (above); all spending deducted (the beside case); zero nominal
  growth after year ten; a price above the top closes OUT.
- *Basis.* Central: all-equity (owner cash before interest, against market value plus net debt). **Net debt ¥3,610bn**:
  borrowings ¥4,161.2bn (short-term ¥849.3bn, long-term ¥3,311.9bn) less cash ¥673.4bn and time deposits ¥52.8bn at
  2026-06-30 (Q1 balance sheet, 2026-08-06), plus ¥175.0bn spent on buybacks to 2026-09-30 (disclosure of 2026-10-01,
  matched by the share count used). Leases (¥1,082.8bn) are left out of net debt and said so. Equity-only beside.
- *Rate:* 4.136%, the 30-year JGB (Step 0).

**The range** (per share on 6,899.3 million shares; price ¥2,155; per ADS at 1:1 and 158.56):

| Case | Whole business at 4.136% | Per share, all-equity (less net debt) | Per share, equity-only |
|---|---|---|---|
| No growth, maintenance-only (central bottom) | ¥13,727bn | **¥1,466** ($9.25) | ¥1,940 |
| Growth 4.136% ten years, purchases and growth spending deducted, then no growth (central top) | ¥16,734bn | **¥1,902** ($12.00) | ¥2,355 |
| All-spending beside: no growth | ¥12,647bn | ¥1,310 | ¥1,783 |
| All-spending beside: growth | ¥15,654bn | ¥1,746 | ¥2,198 |
| DENTSU SOKEN as if closed | | −¥31 on each | −¥31 on each |
| Purchases excluding minority buy-outs (sensitivity) | | ¥1,466 to ¥2,033 | |
| Literal growth 10.86% uncut (not used; (f) cuts it) | | growth case ¥3,821 | |

**The floor, tested first.** The expected return at ¥2,155, solved on each case (the rate at which the case's cash equals
market value plus net debt): central no-growth 3.07%, central growth 3.80%; all-spending 2.83% and 3.59%; equity-only
3.42% to 4.45%. Even the uncut literal-growth case, which the cap forbids, returns 6.05%. **No case in the range earns the
floor of about ten percent at the price** (the framework's CONVENTION, after **[M2003-149]**: "we don’t want to buy
equities where our real expectancy is below 10 percent"). The file closes OUT on the floor whatever the width; the width
is shown for the record: 1.22 to one, narrow.

**And the top.** The price, ¥2,155, is above the top of the central range (¥1,902): "a price above the top of the range
closes OUT", the same close. "If you need to use a computer or a calculator to make the calculation, you shouldn’t buy it"
**[M2009-005]**; here no calculation was needed to see the price above the value, and the calculation agrees.

**Fair price** (Part VII; a reporting figure, never a verdict): each end case valued at ten percent, the two averaged, less
net debt, per share, after the company's own tax:
- **Central (all-equity, maintenance-only (e)): ¥289 a share, $1.82 an ADS** (no-growth case ¥5,678bn and growth case
  ¥5,535bn at ten percent, averaged ¥5,606bn, less ¥3,610bn).
- **Equity-only beside: ¥789 a share, $4.97 an ADS.**
- All-spending beside: ¥238 all-equity, ¥737 equity-only. DENTSU SOKEN as if closed: −¥31 on each.
The equity-only figure exceeds the all-equity one because the net debt (¥3,610bn) costs only about ¥14bn a year after tax:
counted as debt in full, it outweighs its cheap interest at a ten percent floor. The central figure is the all-equity one, by
the framework's CONVENTION.

**The rows' own figure for these companies, weighed only.** "They were sitting as a group where they were earning, we’ll
say 14% on what we were going to pay to buy them" **[M2023-031]**: at today's price ITOCHU's reported net profit is 6.1% of
its market value and its owner cash before purchases 3.4%; whatever the speakers paid, the price today is not that price.

- **VERDICT: OUT**, on the floor: no case in the range earns about ten percent at ¥2,155 (3.1% to 3.8% central), and the price
  sits above the top of the range (¥1,466 to ¥1,902 a share, all-equity, at the 30-year JGB of 4.136%) **[M2003-149]**,
  **[M2009-005]**, **[L2013-012]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED** (Q7 closed the file OUT). Facts found are under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** A fact found is under AFTER THE STOP.

---
## THE BOX
**OUT, at Q7 (the floor).** Q1 IN and Q2 IN on the deciding part (Metals & Minerals: lowest-cost iron ore on the operator's
filing); Q4 accounts IN, weighing against; Q5 integrity IN. At ¥2,155 no case in the range earns about ten percent (central
3.1% to 3.8%), and the price is above the top of the range: **value range ¥1,466 to ¥1,902 a share (all-equity, central;
$9.25 to $12.00 an ADS) against ¥2,155 ($13.62 an ADS)**; equity-only beside ¥1,940 to ¥2,355. Not a TOO HARD, so no
research pass is opened.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.

**Bearing on Q8 (the alternatives).** The 30-year JGB yields 4.136% (MOF, 2026-10-08); the expected returns solved at Q7 on
the central cases are 3.07% and 3.80%, below the government bond's own yield.

**Bearing on Q9 (debt and exposures).**
- Borrowings ¥4,161.2bn and cash and time deposits ¥726.2bn at 2026-06-30; lease liabilities ¥1,082.8bn (mostly
  FamilyMart's stores); net interest-bearing debt to shareholders' equity 0.46 at 2026-03-31 (Summary, Financial
  Information Report 2026). The company's own interest coverage (its stated definition, an operating figure plus interest
  and dividends received over interest expense) fell from 23.6 times (FY2022) to 7.7 times (FY2026) as dollar rates rose.
- The CITIC exposure: a 50% stake in Chia Tai Bright Investment (with the Charoen Pokphand Group), which owns 20% of CITIC
  Limited; investment ¥82.1bn plus a shareholder loan of ¥649.3bn (US$4,061M) at 2026-03-31, together about ¥731bn, against
  ITOCHU's look-through share of CITIC's market value of ¥701.5bn (HK$11.82 a share). CTB recognised an impairment of
  RMB17,291M in the year to March 2019. The auditor names the CITIC investment a key audit matter, its recoverable amount
  resting on "the growth outlook of the Chinese economy and the impact of relevant regulations on the Chinese financial
  businesses" (auditor's report, Financial Information Report 2026). CITIC Limited's summarized balance sheet: total assets
  RMB13,021bn against equity RMB1,497bn (2025), a financial conglomerate.
- Guarantees: maximum potential future payments ¥171.5bn, of which ¥131.2bn of substantial risk (contingent liabilities
  note, 2026-03-31).
- Commodity exposure is measured by the company with value at risk (five-day, 99%), stated in the financial instruments note;
  not read further.
- The Integrated Report 2025 records "Received Moody's A rating for the first time in roughly 20 years" (no date read).
- The signed DENTSU SOKEN purchase (about ¥215bn) and the Aviation Capital Group basic agreement (an aircraft lessor, a
  business with its own debt) would add to the debt and to a leasing exposure; terms of the second not read.

**Bearing on Q12.** A sweep of the Financial Information Report 2026, the Integrated Report 2025 and the FY2026 supplementary
material for "tobacco", "cigarette", "casino" and "gambling" found no instance; coal mining (Q2) is the business most open to
the newspaper test, not a business the rows name.

*No integrity facts are recorded after the stop: Q5 was reached and answered IN.*

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 91ec1b11); written question by question; committed after each
      (write-early): Step 0 to Q1, Q2, Q3, Q4, Q5, Q6, Q7 with the Q6 buyback line, then this close.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (not checked
      by the analyst). The run binds only once folded into the register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Contamination, declared and not
      used:** (1) the session's opening context showed recent commit subjects about another company (VSXY) and a git status
      listing other companies' research-folder names (AYI, ARCB and others) and a project memory index whose lines mention
      "Japanese names" owed and a count of gate-clearers; (2) the framework's own text names "the MITSY regression run" and a
      Q1 paragraph on the five Japanese trading houses; (3) the company's own timely disclosure of 2026-03-02, listed on its
      investor-relations news page and read while looking for buyback disclosures, states that Berkshire Hathaway's National
      Indemnity Company holds over 10% of ITOCHU's voting rights; (4) ledger rows **[L2023-008]**, **[M2023-031]** and
      M2025-018 describe Berkshire's own purchase of the five trading houses. Items (3) and (4) bear on the analyst's
      incentive (operator rule 9): the speakers' own purchase is not evidence about the business today, and no verdict
      here rests on it; the two rows were weighed under the framework's CONVENTION on a row about one company and decided
      nothing. I did not try to learn whether the operator holds or wants the name.
- [x] Every v5 id resolves (checked by `scripts/check_cites.py`, below); every filing fact names its document and date (no
      accession numbers exist for a non-SEC filer; SEC accessions given for the F-6 amendments and BHP's 20-F); no number
      without a filing or a convention.
- [x] The order was kept; Q7 was the first STOP to fail and closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost (capital spending, lease repayments, minority dividends, net purchases of businesses
      in the growth years), never a net-income proxy; the sovereign from the Japan Ministry of Finance; quotes from an
      aggregator flagged.
- [x] Contrary evidence written down as found (Foundations; Q1's doubt; Q2's coal and twenty-year threat; Q3's
      incremental return; Q4's tells); facts for later questions under AFTER THE STOP.
- [x] No row dated after the anchor: not a point-in-time run; every row cited is dated 2025 or earlier.
- [x] `tools/run.py` and `Screens/cover_shares.py` returned nothing for this non-SEC name; no line of theirs was used.
- [x] `python tools/check_framework.py` PASS before the closing commit (2026-10-12); the run's own citation check
      (`scripts/check_cites.py`: no E-ids, 76 distinct ids all in the v5 ledger, every quoted fragment beside an id found in
      its row) PASS, and the fragments with nested quotation marks that the script cannot parse were checked by hand.
- Own shortfalls, stated: the maintenance guess uses lease repayments as the right-of-use depreciation proxy in four of
  five years (a confessed convention of this run); segment profits for three FY2022 parts and one FY2024 part are derived,
  and FY2022's column does not sum to the total by ¥3.7bn; the DENTSU SOKEN target's own filings were not read (its
  dividends credited at nothing); none of the non-deciding parts' castles was read to a verdict; named rivals: none named
  by the company, so none read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 for a commodity producer.** Q1's test 5 asks whether insiders would write the forecast down **[M2000-105]**, and test
2 says "If something is not very predictable, forget it." **[M1998-044]**; but Q2 names the low-cost commodity producer as the
exception and Q7's cycle specific (a) exists for cyclical cash. The text does not say whether an unforecastable product
price is a Q1 matter (TOO HARD, NATURE) or a Q7 matter (range width). This run read it as Q7's and said so at Q1; a run that
read it the other way would close at Q1. A ruling would make the two runs agree. (2) **The parts threshold for a filer that
reports no segment operating profit.** ITOCHU reports segment net profit only; this run used it and confessed the choice.
Whether an unallocated "Others" line holding a material associate (CITIC, about 10 to 14% of profit) counts as a part is not
said. (3) **Leases under IFRS 16.** "On what the floor is earned" puts "finance leases" in net debt and leaves "operating
leases" out; IFRS 16 makes no such split for a lessee. This run left all lease liabilities out of net debt and deducted the
lease repayments and interest from owner cash, which is the same economics; the text should say which. (4) **The no-growth
case and purchases.** Specific (c) stops purchases "After year ten, when growth stops"; it does not say whether the
no-growth end case (growth zero from year one) carries the purchases. This run carried none (a business that buys no growth
spends nothing to buy it, the convention's own rationale), which raises the bottom of the range. (5) **The cap's degenerate
case.** Where the business's own sales growth (4.79%) is above the 30-year JGB (4.136%), (f) leaves the growth exactly at
the discount rate, so the ten growth years add exactly ten years' cash: an artefact of a high long rate, worth a sentence.
(6) **"Cash paid for businesses" and minority buy-outs.** The text does not say whether buying out minorities in existing
subsidiaries (¥450bn of the window's purchases) is a purchase of a business; this run counted it and showed the figure
without it. (7) **"Proceeds from dividends"** mixes equity-method dividends with dividends on fair-valued holdings; the
equity-method convention counts the first and is silent on the second, which this run also counted.
