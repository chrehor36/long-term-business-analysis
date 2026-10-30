# Company Run - Chevron Corporation (NYSE: CVX) - 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch. Every judgment cites a v5 ledger id in bold;
every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run and later questions are marked
NOT REACHED. Working folder: `Test Runs/_research 2026-10-06 CVX/` (the `tools/run.py`, `cover_shares.py` and `sources.py`
prints; `arithmetic.py` for every computed number below; `ledger_grep.py`, `ledger_show.py`, `htm2txt.py`; raw filings in
`cache/`, gitignored).

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md` is closed to
this run, so whether the operator holds CVX is unknown to the analyst.

**BLIND RULE AND CONTAMINATION, declared.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`,
`Screens/WATCHLIST RUN QUEUE.md`, the prepped reading list, `tools/alerts.json`, and any earlier run file or research
folder for CVX in `Test Runs/`, `Framework/v4/` or `Framework/v5/tests/`. Seen without opening: a listing of `Test Runs/`
filtered to files dated 2026-10-0x (no CVX file among them). Opened for FORM only: `Test Runs/2026-10-05 Run - AMR Alpha
Metallurgical.md`, another commodity producer's v5 run; its reasoning about met coal was seen, and this run's commodity
reading below was made from Chevron's and its rivals' filings, not from that file's numbers. Contamination from memory,
declared: the analyst's training holds that Berkshire bought Chevron stock in 2020 and later held it, and that Chevron
bought Hess. The first is a prior about the buyer, not about the business, and is set aside; the second is confirmed by
the filings below. Two ledger rows name the company: **[M2011-012]** ("You’re not going to have a big edge in trying to
pick Chevron against Exxon against Continental and Occidental") and **[M2015-017]** (Munger naming "Exxon and Chevron"
among companies with "long histories of trying to be way safer than average"). Both were found by a text search of the
ledger and are used only where marked.

---
## STEP 0 - THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $206.47 (2026-10-05, `tools/run.py`; aggregator, live quote only, flagged per operator rule 5).
- **Shares by class:** one class, common stock, par $.75, **1,975,771,274** outstanding on the cover of the 10-Q for the
  quarter ended 2026-06-30 (filed 2026-08-06, accession `0000093410-26-000167`; `python Screens/cover_shares.py CVX`). The
  balance sheet of the same filing shows 2,442.677M issued, the difference being treasury stock.
- **Market cap:** $206.47 x 1,975.771M = **$407,937M** (`arithmetic.py`).
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 10/05/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4), all from SEC EDGAR:
  - 10-K FY2025, filed 2026-02-24, `0000093410-26-000078`: Item 1 (business, reserves, production, competition), Item 1A
    in part, Item 7 (MD&A, business environment and outlook, results by segment, liquidity, capex), the cash-flow
    statement, Note 14 segment earnings, the stock-compensation note, and the supplementary oil and gas Tables III and IV.
  - 10-Q Q2 2026, filed 2026-08-06, `0000093410-26-000167`: cover, balance sheet, equity statement, debt and buyback
    paragraphs of the MD&A.
  - 8-K of 2026-07-31, `0000093410-26-000162`, EX-99.1 (second-quarter 2026 earnings release): read in full on page one
    and two.
  - 8-K of 2026-10-05, `0000093410-26-000188`, Item 5.02: officer changes effective 2027-01-01 (the CFO becomes President,
    Oil, Products & Gas; a new CFO is elected).
  - DEF 14A filed 2026-04-07, `0001193125-26-145617`: fetched; not read past the cover, the file closing before Q5.
  - Earlier 10-Ks for the span: FY2018 `0000093410-19-000008`, FY2019 `0000093410-20-000010`, FY2022
    `0000093410-23-000009` (segment earnings, production, cash-flow statements, return on capital employed, Table IV).
  - Competitors, their own 10-Ks: ExxonMobil FY2019 `0000034088-20-000016`, FY2022 `0000034088-23-000020`, FY2025
    `0000034088-26-000045`; ConocoPhillips FY2019 `0001193125-20-039954`, FY2022 `0001163165-23-000006`, FY2025
    `0001163165-26-000009`.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities 2025, **$33,939M**
  on the filed Consolidated Statement of Cash Flows (10-K FY2025, `0000093410-26-000078`), equals the 33,939 that
  `tools/run.py` transcribes from XBRL. Also equal for 2024 (31,492) and 2023 (35,609).
- **`tools/run.py CVX` arithmetic lines only** (its window rules, labels and yields are v4 and are not used): OCF
  2023-2025 35,609 / 31,492 / 33,939; capex 15,829 / 16,448 / 17,347; D&A 17,326 / 17,282 / 20,132; SBC "n/f" (not found
  in XBRL; read from the notes instead, below); the ten-year balance-sheet table (carried to Q4, not reached). Two costs
  the tool does not see are taken from the filed statements: stock pay (the share-based compensation note) and net loans
  to equity affiliates (an investing line, the means by which Chevron funded its share of Tengizchevroil's expansion).

**Owner cash by year** (filed cash-flow statements and notes; OCF less stock pay less all capex less net lending to equity
affiliates; USD millions; `arithmetic.py`). Under the framework's equity-method CONVENTION (Q4), affiliate income enters
only as the dividends received, which OCF already does through its "distributions more (less) than income" line.

| year | OCF | stock pay | capex | net affiliate loans | owner cash | source |
|---|---|---|---|---|---|---|
| 2016 | 12,690 | 642 | 18,109 | -2,034 | -8,095 | 10-K FY2018 |
| 2017 | 20,338 | 368 | 13,404 | -16 | 6,550 | 10-K FY2018, FY2019 |
| 2018 | 30,618 | 165 | 13,792 | +111 | 16,772 | 10-K FY2018, FY2019 |
| 2019 | 27,314 | 394 | 14,116 | -1,245 | 11,559 | 10-K FY2019 |
| 2020 | 10,577 | 190 | 8,922 | -1,419 | 46 | 10-K FY2022 |
| 2021 | 29,187 | 761 | 8,056 | +401 | 20,771 | 10-K FY2022 |
| 2022 | 49,602 | 1,073 | 11,974 | -24 | 36,531 | 10-K FY2022 |
| 2023 | 35,609 | 0 | 15,829 | -302 | 19,478 | 10-K FY2025 |
| 2024 | 31,492 | 600 | 16,448 | -233 | 14,211 | 10-K FY2025 |
| 2025 | 33,939 | 472 | 17,347 | +778 | 16,898 | 10-K FY2025 |

Stock pay is the expense for options plus stock appreciation rights, restricted stock, performance shares and restricted
stock units as each year's note states it (2023 was a net reversal of $15M, taken as zero); part of it is cash-settled and
already in OCF, so the deduction is conservative. Five-year mean 2021-2025: **$21,578M**; ten-year mean 2016-2025:
**$13,472M**; five-year mean 2016-2020: $5,366M. Brent averaged $69 in 2025 and $81 in 2024 (10-K FY2025, MD&A) and $104
in the second quarter of 2026 (EX-99.1). Asset-sale proceeds ($1.8B in 2025, $7.7B in 2024) are excluded as non-recurring.
The Hess acquisition of July 2025 was paid mainly in stock (equity statement, "Hess Corporation acquisition" $45,603M of
Chevron equity issued, 10-K FY2025) and is not in the table.

---
## THE FOUNDATIONS (not a gate)
A share is a business, and the quotation "doesn’t tell us anything. It just tells us prices." **[M2006-077]**. No macro
enters as a forecast **[M2000-094]**, and the speakers apply that to oil by name: "we are not two fellows who think we can
predict the price of soybeans or corn or oil or anything else" **[M2016-025]**; "if we were in an oil stock, it’s because
we think it offers a lot of value at this price, but it does not mean that we think the price of oil is going up."
**[M2007-129]**. For a price-taker the price of its product is not macro but the business itself, and the rows measure a
producer by what it controls: "we would measure it, probably, more by cost of production than we would by whether copper
was selling for $2.00 a pound or a dollar a pound" **[M2006-004]**. Margin of safety: "if you have to actually do it on —
with pencil and paper, it’s too close to think about" **[M1996-084]**.

**Contrary evidence, written down as found** **[M1997-127]**: (1) Chevron's lifting cost per barrel was the lowest of the
three US-filing majors read in every year 2020-2025 (Q2 row); (2) the company is a descendant of Standard Oil of
California (10-K FY2025, Item 1, footnote 1), and Munger names Rockefeller's Standard Oil as "practically the only one"
of the oil giants that "continued to do monstrously well" after getting big **[M2013-009]**; (3) a speaker says "a big
integrated oil company" is "fairly easy to get your mind around" **[M2004-081]**; (4) owner cash was positive in nine of
ten years, and cash dividends were paid through both troughs ($8,032M in 2016, 10-K FY2018; $9,651M in 2020, 10-K
FY2022); (5) proved reserves rose to 10.6 billion BOE at
end-2025 and second-quarter 2026 production was a record 4,070 MBOED (10-K FY2025; EX-99.1). Found against: (6) the
company's own statement that the most significant factor in upstream results "is the price of crude oil, which is
determined in global markets outside of the company’s control" (10-K FY2025, MD&A); (7) return on capital employed
averaged 7.1% over 2016-2025 and was negative in 2016 and 2020 (Q2); (8) $8.17B of 2019 upstream impairments, chiefly
Appalachia shale and Big Foot (10-K FY2019); (9) first-quarter 2026 earnings of $2,210M at $81 Brent against
second-quarter earnings of $12,072M at $104 Brent (EX-99.1).

## THE STANDING RULE
A cash purchase of a listed share, unlevered and sized so that a total loss is survivable, carries no call on the buyer:
"One investment rule at Berkshire has not and will not change: Never risk permanent loss of capital." **[L2023-005]**; "We
are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**. The target's own
debt and decommissioning obligations are Q9's, not the buyer's ruin. No breach.

---
## Q1 - CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**; "a reasonable probability of being able to asses where the business will
  be in 10 years" **[M2000-037]**. The product can stay opaque if "I understand the economic dynamics of the industry"
  **[M2011-014]**. The rows speak to this kind of company directly: "a big integrated oil company, it’s fairly easy to
  get your mind around the economic characteristics that will exist in the business" **[M2004-081]**; and to how an oil
  asset is valued, "it’s worth the discounted value of the oil that’s going to come out. And then you have to make an
  estimate as to volume and as to price." **[M2002-079]**.
- **The economics, from the filings.** Chevron produces oil and gas (3,723 MBOED in 2025 including affiliates; 43% of
  proved reserves in the United States, 15% in Australia, 11% in Kazakhstan) and refines and sells products and
  petrochemicals (10-K FY2025, `0000093410-26-000078`, Items 1 and 7). Upstream earned $12,822M and downstream $3,022M of
  2025 segment earnings, with "All Other" at -$3,545M. In its own words: "Earnings of the company depend mostly on the
  profitability of its upstream business segment. The most significant factor affecting the results of operations for
  the upstream segment is the price of crude oil, which is determined in global markets outside of the company’s
  control." and "In the company’s downstream business, crude oil is the largest cost component of refined products."
- **The key variables and whether they are foreseeable** **[M1998-044]**. (1) Volume: 10,591 million BOE of proved
  reserves at end-2025, about 7.8 years of 2025 production (`arithmetic.py`), replaced over time by drilling and by
  purchase (Noble 2020, PDC 2023 and Hess 2025 per the filings): foreseeable within a band, at a cost. (2) Unit cost:
  lifting cost of $9.23 to $13.15 a BOE over 2016-2025 (Table IV, consolidated): foreseeable within a band. (3) The price:
  Chevron's average US crude realization was $74.36, $73.47 and $62.25 a barrel in 2023-2025 (Table IV); Brent averaged
  $104 in the second quarter of 2026 (EX-99.1): not foreseeable, and the speakers say so of oil by name **[M2016-025]**,
  **[M2011-044]**, and of an oil producer's results, "how it works out is going to depend on the price of oil to a great
  extent" **[M2020-035]**. (4) The ten-year demand path: the company writes that "Significant uncertainty remains as to
  the pace and extent to which a lower carbon future progresses" (10-K FY2025, MD&A); slow change, "much harder to
  perceive" **[M2014-038]**.
- **Would the insiders write it down?** **[M2000-105]**. They write down the dynamics and a planning price, not a price
  forecast: production guidance for 2026 is given "assuming a Brent crude oil price of $60 per barrel" (10-K FY2025), and
  the company calls the price "outside of the company’s control". That is the position of every producer in the industry,
  stated in the competitors' filings too (Q2).
- **Routing.** Not a fast-changing industry closing at Q1 (the routing fixed under What understanding means). What cannot
  be foreseen is the price path, which for a price-taker is the castle question (Q2: who sets the price, and is Chevron the
  low-cost producer) and the value question (Q7: how sure the cash). The doubt rule **[M2002-092]** was applied to the
  economics, which can be read from Chevron's filings and its rivals' "off the figures" **[M2008-069]**, **[M2005-015]**.
- **VERDICT: IN**, with the oil price carried forward as the open variable **[M2004-081]**, **[M2011-014]**,
  **[M2002-079]**. (The alternative reading, TOO HARD (NATURE) on the price under **[M2020-035]**, is recorded under What
  in the framework was wrong or unclear.)

## Q2 - WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now." **[M1995-038]**. What a castle protects: "A truly great business must have an enduring "moat" that
protects excellent returns on invested capital." **[L2007-004]**; "a great business, which means that business is going
to earn a high return on capital employed for a very long period of time" **[M2007-023]**.

- **Is it a commodity?** The rows define the commodity by the customer's indifference: "the product is available from
  many suppliers [...] most insureds don't care from whom they buy." **[L2004-003]**. The filings, in three companies'
  own words: Chevron, the price of crude "is determined in global markets outside of the company’s control", and "Strong
  competition exists in all sectors of the petroleum and petrochemical industries" (10-K FY2025, `0000093410-26-000078`,
  Items 1 and 7); ExxonMobil, "The oil, gas, and petrochemical businesses are fundamentally commodity businesses" (10-K
  FY2025, `0000034088-26-000045`, Item 1A); ConocoPhillips, "We deliver our production into the worldwide commodity
  markets" (10-K FY2025, `0001163165-26-000009`, Item 1). That is the competitors answering the "ask the competitors"
  test **[M2017-091]** in their own filings: none claims a product the buyer asks for by name. The speakers name the
  case: the gas station where "whatever he charged for gas was my price" **[M2012-109]**; "he determined our profit,
  because we looked at his price every day" **[M2023-079]**; and of the oil business itself, "if oil sells at X, you
  know, you do very well. And if it sells at half of X, you know, your costs are the same" **[M2023-082]**. It is a
  commodity, upstream and downstream alike.
- **Pricing power and the agony before a rise.** None to test. Chevron's average crude realization in the United States
  was $74.36, $73.47 and $62.25 a barrel in 2023, 2024 and 2025 (Table IV, 10-K FY2025), moving with Brent ($81 in 2024,
  $69 in 2025). Downstream earnings ran from $47M (2020) to $8,155M (2022) (10-K FY2022, `0000093410-23-000009`), the
  refiner's margin set by the same market. The branded network (about 8,600 Chevron- and Texaco-branded stations in the
  United States, about 5,200 abroad, 10-K FY2025) sells gasoline, the product of the gas-station rows above.
- **The return the castle is supposed to protect** **[L2007-004]**. Return on average capital employed as Chevron files
  it: 2016 -0.1%, 2017 5.0%, 2018 8.2%, 2019 2.0%, 2020 -2.8%, 2021 9.4%, 2022 20.3%, 2023 11.9%, 2024 10.1%, 2025 6.6%
  (10-Ks FY2018, FY2019, FY2022, FY2025). Mean **7.1%**; below the 5.66% long government rate in four of ten years
  (`arithmetic.py`). The one year above 20% was the year of $99 Brent. There is no excellent return here for a moat to
  protect; the return follows the price.
- **The one exception: the low-cost producer.** "when a company is selling a product with commodity-like economic
  characteristics, being the low-cost producer is all-important" **[L2000-017]**; "commodity businesses have risk unless
  you’re the low-cost producer, because the low-cost producer can put you out of business" **[M1997-010]**; measured
  against the competitor, not in absolute terms **[M2001-013]**; "It’s like comparing a copper producer whose costs are
  $2.50 a pound with a copper producer whose costs are $1 a pound. Those are two different kinds of businesses."
  **[M2009-059]**.

**The competitor row** (each company's own 10-K; `arithmetic.py`). Metric A: upstream after-tax earnings per barrel of
oil-equivalent produced, which carries every real cost of the barrel (lifting, production taxes, depreciation and
depletion of what was spent to find or buy it, exploration, income tax): Chevron's "Total Upstream" segment earnings over
net production including affiliates; ExxonMobil's Upstream earnings (U.S. GAAP) over oil-equivalent production;
ConocoPhillips' segment net income total (net income less Corporate and Other) over total production. Metric B: average
production (lifting) cost per BOE of consolidated operations, from each company's supplementary oil and gas table.

| year | CVX A ($/BOE) | XOM A | COP A | CVX B ($/BOE) | XOM B | COP B |
|---|---|---|---|---|---|---|
| 2016 | -2.67 | not read | not read | 13.15 | not read | not read |
| 2017 | 8.19 | 9.18 | 2.55 | 11.41 | not read | not read |
| 2018 | 12.45 | 10.06 | 16.92 | 10.78 | not read | not read |
| 2019 | 2.31 | 10.01 | 14.53 | 10.62 | not read | not read |
| 2020 | -2.16 | -14.55 | -1.99 | 10.07 | 11.57 | 10.99 |
| 2021 | 13.98 | 11.64 | 14.49 | 9.90 | 12.15 | 9.99 |
| 2022 | 27.67 | 26.74 | 29.97 | 10.16 | 13.09 | 11.27 |
| 2023 | 15.31 | 15.62 | 17.69 | 10.23 | 12.05 | 11.87 |
| 2024 | 15.23 | 16.01 | 13.92 | 9.23 | 11.70 | 12.26 |
| 2025 | 9.44 | 12.35 | 10.53 | 9.71 | 11.29 | 12.01 |
| mean 2017-25 (A) / 2020-25 (B) | **11.38** | **10.79** | **13.18** | **9.88** | **11.97** | **11.40** |

Sources: Chevron 10-K FY2018 `0000093410-19-000008`, FY2019 `0000093410-20-000010`, FY2022 `0000093410-23-000009`, FY2025
`0000093410-26-000078` (segment earnings; selected operating data; Table IV). ExxonMobil 10-K FY2019
`0000034088-20-000016`, FY2022 `0000034088-23-000020`, FY2025 `0000034088-26-000045` (Upstream earnings by year;
oil-equivalent production; "Average production costs, per oil-equivalent barrel - total", consolidated subsidiaries).
ConocoPhillips 10-K FY2019 `0001193125-20-039954`, FY2022 `0001163165-23-000006`, FY2025 `0001163165-26-000009` (net income
by segment; total production; "Average Production Costs Per Barrel of Oil Equivalent", total consolidated operations).
The definitions differ at the edges: each company's upstream line carries its own impairments and gains (Chevron's 2019
holds $8.17B of US upstream impairments, mainly Appalachia shale and Big Foot, 10-K FY2019; ExxonMobil's 2020 holds
$19.3B of upstream impairments, 10-K FY2022); fiscal regimes differ by country; ConocoPhillips is almost wholly upstream.
The order of the means does not turn on any single year.

- **What the row shows, over the whole span.** On lifting cost (B) Chevron is the cheapest of the three in every year
  read, by $1.5 to $2.9 a barrel against ExxonMobil: contrary evidence, written down **[M1997-127]**. On the full cost of
  the barrel (A), which is the cost the rows mean when they say "the low-cost producer can put you out of business"
  **[M1997-010]**, Chevron is second of three: ConocoPhillips earned more per barrel in seven of the nine years 2017-2025
  and about $1.80 more on the mean; ExxonMobil was ahead in five of the nine and behind on the mean by $0.59
  (`arithmetic.py`). Chevron's filing claims no low-cost title; it describes itself as competing with "fully integrated,
  major global petroleum companies, as well as independent and national petroleum companies" (10-K FY2025, Item 1). The
  producers the filing names as setting world supply ("Production levels from the members of Organization of Petroleum
  Exporting Countries (OPEC), Russia and the United States are major factors in determining worldwide supply", 10-K
  FY2025) mostly file no 10-K; their costs were not read, and no claim is made about them beyond the filing's own
  sentence. Chevron is not shown to be the low-cost producer: it is mid-curve among its US-filing peers, and its price is
  set by others.
- **The attacker with money** **[M2011-015]**. The test runs the other way here: the industry is entered every year by
  anyone with acreage and capital (Chevron itself grew by buying Noble Energy in 2020, PDC Energy in 2023 and Hess in 2025,
  per the 10-Ks FY2022 and FY2025), and the speakers say of oil supply at half the price, "it also brings down the oil
  production of the United States very fast" **[M2023-082]**: supply that comes and goes with price is the mark of an
  industry with no barrier around the price. "there are some industries that are just never going to have barriers to
  entry. And in those industries, you better be running very fast" **[M2012-106]**.
- **Unit volume, widening or narrowing.** Production 2,594 MBOED (2016) to 3,723 (2025) and 4,070 in the second quarter
  of 2026 (10-Ks; EX-99.1), much of it bought with stock and cash. Volume rose; earnings per barrel did not (Metric A,
  $9.44 in 2025 against $8.19 in 2017). Volume is not share of mind here: no customer asks for Chevron's barrel by name.
- **What could destroy, modify or reduce it** **[M2000-014]**. The price of oil, which the company says it does not
  control; the pace of the energy transition, which it says is uncertain; host-government terms (21% of 2025 production
  in OPEC+ countries; Tengiz exports through the Caspian Pipeline Consortium, with "recent drone attacks"; Venezuela
  under sanctions authorizations; the Leviathan and Tamar fields in Israel), all from the 10-K FY2025 MD&A. These are the
  threats of a price-taker, not of a castle under siege.
- **The other routes through a commodity field.** **[L2004-007]** begins "Another way", so the low-cost position is not
  the only route the rows allow. Searched for one here: integration (refining its own crude) adds a second commodity
  margin, not a protected one (downstream earnings $47M to $8,155M over 2016-2025, 10-Ks); the brands sell gasoline at the
  price across the street **[M2012-109]**; long-life assets (Tengiz, Australian LNG "committed under binding long-term
  contracts" whose prices "are typically linked to crude oil prices", 10-K FY2025) lengthen the volume but leave the price
  with the market. No other route found.
- **The rows that name the company, read last.** "You’re not going to have a big edge in trying to pick Chevron against
  Exxon against Continental and Occidental" **[M2011-012]**, said to explain why studying the oil sector would give no
  edge: the speaker treats the large producers as interchangeable, which is the commodity reading. And of a large oil
  producer generally: "It is a — it is a investment that depends on the price of oil. [...] If you own oil, you should
  only own oil, if you expect these prices to go up significantly." **[M2020-035]**, from speakers who say they cannot
  forecast that price **[M2016-025]**.
- **VERDICT: OUT.** A commodity seller whose price is set by the world market **[M2012-109]**, **[M2023-079]**,
  **[L2004-003]**, that is not the low-cost producer on its own competitors' filed full-cycle numbers over the span
  **[L2000-017]**, **[M1997-010]**, **[M2009-059]**, and whose return on capital employed (mean 7.1%, 2016-2025) shows no
  excellent return for a moat to protect **[L2007-004]**, **[M2007-023]**. The castle is shown open on the evidence, so
  the box is OUT, not TOO HARD **[M2006-013]**: this is not a tenuous moat whose value cannot be judged **[M2000-019]**,
  but the absence of one, read from ten years of filed figures. Price does not reopen it: "What you can’t do is turn any
  investment into a good deal by paying little" **[M2019-015]**; marginal businesses bought cheap "are the wrong
  foundation on which to build a large and enduring enterprise" **[L2014-009]**; "We’re going to be investors in
  businesses, not commodities, by and large." **[M2007-131]**.

**The file closes here. Q3 to Q12 are NOT REACHED; nothing below is a clearance.**

---
## Q3 - HOW MUCH CAPITAL MUST GO IN. NOT REACHED.
Facts for the record only: capex $17,347M in 2025 against D&A of $20,132M; upstream capex $15,890M of it; 2026 organic
capex guided at $18 to $19 billion, upstream $17 billion (10-K FY2025, MD&A). Capex ran $8.1B to $18.1B a year over
2016-2025 (table in Step 0). Proved reserves equal about 7.8 years of 2025 production, so standing still requires the
spending; the filing gives no maintenance figure.

## Q4 - DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED.
Facts for the record only. The balance sheets as `tools/run.py` transcribes them (first-filed XBRL, USD millions; not
re-read against each filed statement, the file having closed at Q2): equity 145,556 (2016), 131,688 (2020), 152,318
(2024), 186,450 (2025, after the Hess stock issue) and 189,883 at 2026-06-30 (10-Q); retained earnings 173,046 (2016) to
205,365 (2025); debt on the face of the balance sheet 44,315 (2020), 20,836 (2023), 40,758 (2025); total debt and finance
leases $37.1 billion at 2026-06-30 (10-Q). Goodwill steady at about 4.4B to 4.7B. The earnings release features "adjusted
earnings" beside reported earnings and gives the reconciliation (EX-99.1, Attachment 4 named); the 10-K presents earnings
and the reconciliations of non-GAAP terms. Not judged.

## Q5 - WHO RUNS IT. NOT REACHED.
## Q6 - WHAT WILL THEY DO WITH THE MONEY. NOT REACHED.
Facts for the record only: a $75 billion repurchase program from 2023-04-01 with no fixed expiration and no stated
price limit ("The timing of the repurchases and the actual amount repurchased will depend on a variety of factors,
including the market price of the company’s shares", 10-Q Q2 2026); 281 million shares for $44.0 billion under it to
2026-06-30, about $156.58 a share on average, and 16.2 million for $3.0 billion in the second quarter of 2026, about
$185.19 (`arithmetic.py`). Net treasury purchases of $14,678M, $15,044M and $11,855M in 2023-2025 (cash-flow statement).
The Hess acquisition of 2025 was paid chiefly in Chevron stock ($45,603M of Chevron equity issued, equity statement, 10-K
FY2025). The quarterly dividend is $1.78 (EX-99.1).

## Q7 - WHAT IS IT WORTH. NOT REACHED.
**COMPUTATION — NOT A CLEARANCE** (operator rule 3; the convention's construction, shown because the brief asks for the
arithmetic of every run and because it is the reversal arithmetic should Q2 ever be read the other way). Five-year mean
owner cash 2021-2025 **$21,578M**; growth shown on aggregate owner cash 2021 to 2025, **-5.03%** a year; sovereign 5.66%.
No-growth case **$192.95** a share; shown-growth case (ten years at -5.03%, then flat) **$130.06**; width 1.48 to one.
Price **$206.47**, above the top of the range. On the floor (CONVENTION, about ten percent pre-tax; the gross-up uses the
mean of the filed effective tax rates of 2024 and 2025, 35.5% and 36.8%, a CONVENTION of this run because the framework
names no rate), the five-year mean gives a pre-tax yield of 8.28% at the price; no-growth owner cash clears ten percent
pre-tax at **$171.04** ("cheap"); with the growth shown negative there is no price above that at which the central case
clears it ("fair" not computed). On the ten-year mean ($13,472M, Brent from the 2016 and 2020 troughs to the 2022 spike)
the no-growth value is $120.47 and the ten-percent price $106.79. The window decides the answer, which is the price
dependence of Q2 restated in dollars.

## Q8 - IS IT BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 - COULD IT RUIN US. NOT REACHED.
Facts for the record only: total debt $37.1B against $8.5B of cash and securities at 2026-06-30 (10-Q); reverted
decommissioning obligations from previously divested Gulf of America assets, $297M spent in 2025 and "an additional
$200-300 million annually through 2033" (10-K FY2025); Hess Midstream LP general-partner liability named as a risk factor
(10-K FY2025, Item 1A).
## Q10 - IS IT THE FAT PITCH. NOT REACHED.
## Q12 (optional) - WOULD WE BE PROUD OF HOW THE MONEY IS MADE. NOT ASKED (the file closed at Q2).

---
## THE BOX
**OUT**, decided at **Q2**: a commodity price-taker, mid-curve among its US-filing peers on full-cycle earnings per
barrel (CVX $11.38, XOM $10.79, COP $13.18, mean 2017-2025) though lowest of the three on lifting cost, with return on
capital employed averaging 7.1% over 2016-2025 **[L2000-017]**, **[M1997-010]**, **[L2007-004]**. Q7 not reached;
computation only, not a clearance: $206.47 against a convention range of $130 to $193, "cheap" about $171. **Reversal
condition:** filed evidence, over a full cycle, that Chevron's full-cycle cost per barrel sits below its peers' (Metric A
ahead of both rivals across a span including a trough), or a ruling that Q2's low-cost exception is read on lifting
cost; either would send the file to Q3. Q11 belongs to the holding review, not to this run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after Q1 (`8f9bce1`) and after
      Q2 (`03c30cc`), and again at the close.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in that row's text
      (`Test Runs/_research 2026-10-06 CVX/cite_check.py`, result below); no v4 id. Every filing fact carries its
      document and accession.
- [x] The order was kept; Q2 failed and closed the run; nothing after it is a clearance, and the valuation is headed
      COMPUTATION — NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay, all capex, net lending to equity affiliates), never a net-income proxy;
      the sovereign from the Treasury curve; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found, in the foundations paragraph and at the competitor row.
- [x] Not a point-in-time run; no anchor bar applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; stock pay and affiliate loans were taken from the filings
      because the tool does not see them.
- [x] `python tools/check_framework.py` PASS before each commit (output in the research folder).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Q1 for a price-taker.** **[M2004-081]** says a big integrated oil company's economics are "fairly easy" to grasp;
   **[M2020-035]** says how it works out "is going to depend on the price of oil to a great extent", and the speakers say
   they cannot forecast that price **[M2016-025]**. Read strictly, test 1 of Q1 ("where will it be in ten years?") closes
   every producer TOO HARD (NATURE) at Q1; read as the economic dynamics, Q1 passes and Q2's commodity paragraph decides.
   This run took the second reading (as the routing note does for fast change) and records the first. The framework
   should say which.
2. **Which cost makes "the low-cost producer"?** The rows say "low-cost producer" without a measure. On lifting cost
   Chevron is the lowest of the three filers read in every year; on full-cycle earnings per barrel it is second. This run
   used the full cycle, because depreciation of what was spent to find or buy the barrel is a real cost (Q4) and the rival
   who can "sell it cheaper" **[M1997-010]** is the one with the lower full cost. A reader using lifting cost would pass
   Q2. Nor does the framework say against which field the position is measured (US filers only, or the whole cost curve,
   much of which files nothing). The text should say both.
3. **Q2 as a STOP sits against the speakers' own oil purchases.** The rows record oil stocks bought on price against value
   without a price forecast **[M2007-129]**, **[M2024-054]**, and PetroChina bought "very, very cheap in relation to
   earnings, in relation to reserves" **[M2004-082]**. Under v5's order a commodity producer that is not the low-cost
   producer closes at Q2 and can never reach the value question, so the purchase the rows narrate cannot be made by the
   framework. The tension is not carried in section VI; it should be, or Q2 should name the commodity producer bought at
   a screaming price as an exception routed to Q7.
4. **The Q7 convention in a cyclical window.** The five-year window 2021-2025 holds the 2022 price spike and shows
   negative growth, so the shown-growth end falls below the no-growth end, and the ten-year mean gives a value 38% lower.
   The convention names no rule for a cyclical business (window choice, or a margin-times-volume normalization), and no
   tax rate for the pre-tax floor; this run used the mean filed effective rate and said so.
5. **Capital lent to equity affiliates and growth bought with stock.** The equity-method CONVENTION counts affiliate
   income as dividends received but says nothing of capital lent to the affiliate (Chevron funded its share of the Tengiz
   expansion partly by loans); this run deducted net affiliate lending. And the convention measures growth on aggregate
   owner cash, which credits production bought with newly issued shares (Hess) as growth; the per-share caveat in the
   convention addresses buybacks only.
6. **Tool defects (reported, not fixed):** `tools/run.py` prints "SBC n/f" for CVX, so its owner-earnings lines deduct no
   stock pay, and it does not see net loans to equity affiliates; it still prints v4 windows and yields, which were not
   used.

**Checks run 2026-10-06, after the last edit:** `python tools/check_framework.py` PASS (output saved to
`Test Runs/_research 2026-10-06 CVX/check_framework_output.txt`); `python -I "Test Runs/_research 2026-10-06
CVX/cite_check.py"`: every id in `principle_ledger_v5.csv`, every quoted fragment beside an id found in that row, 0
problems.
