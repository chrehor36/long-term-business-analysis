# Company Run - Alpha Metallurgical Resources, Inc. (NYSE: AMR) - 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch. Every judgment cites a v5 ledger id in bold;
every filing fact carries its accession. Working folder: `Test Runs/_research 2026-10-05 AMR/` (filings as text, the
`tools/run.py` print, `arithmetic.py` for every computed number below, `ledger_grep.py`, `ledger_show.py`, `cite_check.py`).

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is closed to this run under the blind rule of
the brief, so whether the operator holds AMR is unknown to the analyst.

**BLIND RULE AND CONTAMINATION, declared.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`,
`Screens/WATCHLIST RUN QUEUE.md`, the prepped reading list, any other `Test Runs/` file about AMR (a listing of `Test Runs/`
filtered for "AMR|alpha" returned only `2026-08-30 Run - AXR (AMREP) v4.1.md` and `2026-09-06 Run - GOOGL Alphabet.md`,
neither about this company, neither opened), other companies' 2026-10-05 run or research files, and the not-adopted
small-cap case. Seen without opening: the five latest commit subjects (EFOR, AHCO, ABG, WSC runs and a run.py change), the
git-status list of untracked 2026-10-05 run files (ADNT, MBC, WEN), three 2026-10-05 holding-review file names (BRK.B, CCB,
HRB) returned by a grep that counted how earlier files spell the computation heading, and the memory index lines in the
session context (wave 7 state, "57 gate-clearers, nothing buyable"). None names AMR or bears on its facts. The session was
interrupted once by the coordinator's resume message; the working folder and this file were checked on disk and the run
continued from the filings already fetched.

---
## STEP 0 - THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $175.05 (2026-10-05, `tools/run.py`; aggregator, live quote only, flagged per operator rule 5).
- **Shares:** one class, common stock 12,679,045 outstanding at 2026-07-31 (10-Q cover, filed 2026-08-07, accession
  0001704715-26-000031; `python Screens/cover_shares.py AMR`). The balance sheet of the same 10-Q shows 12,685,495
  outstanding and 22,496,891 issued at 2026-06-30, the difference being 9,811,396 treasury shares.
- **Market cap:** $175.05 x 12.679M = **$2,219M**.
- **Sovereign for the earnings currency (USD; "All of our sales are conducted in U.S. dollars", 10-K FY2025):** 5.63%,
  US Treasury daily par yield curve, 30-year, 2026-10-02 (`tools/run.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-27, 0001704715-26-000010): Item 1, Item 5, Item 7 in full,
  the balance sheet, cash-flow statement and Notes 7, 14, 17 in part. 10-Q Q2 2026 (filed 2026-08-07, 0001704715-26-000031):
  balance sheet, cash flow, MD&A results. Earlier 10-Ks for the span: FY2024 (0001704715-25-000010), FY2023
  (0001704715-24-000028), FY2022 (0001704715-23-000010), FY2021 (0001704715-22-000012), FY2020 (0001704715-21-000026), FY2019
  (0001704715-20-000010), FY2018 (0001704715-19-000013); the 2018 merger S-4 (0001628280-18-011255) for the 2015-2017
  predecessor and Contura segment figures. Proxy DEF 14A 2026 (0001140361-26-012338) skimmed only (the file closed before
  Q5); the 8-K of 2026-08-07 (0001704715-26-000030) cover only, the exhibit not read.
- **One figure cross-checked against the filed statement:** net cash from operating activities 2025, $144,926 thousand on
  the filed cash-flow statement (10-K FY2025, 0001704715-26-000010) equals the $144.9M `tools/run.py` transcribes from XBRL.
  A disagreement found and recorded: XBRL gives 2020 capex as $119.6M; the filed FY2020 and FY2022 cash-flow statements give
  $153,990 thousand. The filed figure is used.
- **`tools/run.py AMR` arithmetic lines only** (its window rules and labels are v4 and are not used): OCF 2023-2025 851.2 /
  579.9 / 144.9; capex 245.4 / 198.8 / 127.2; D&A 136.9 / 167.3 / 174.5; SBC (expense tag) 20.9 / 12.9 / 13.6; the
  ten-year balance-sheet table (read under Q4 below). The tool does not see "Capital contributions to equity affiliates"
  (the DTA export terminal), $30.8M / $32.5M / $38.1M in 2023-2025 on the filed cash-flow statement, which is a real
  recurring cost of moving the coal and is deducted below. The brief expected a mine-development alternate; none was
  printed, and the 10-K FY2025 puts mine development inside the single capex line ("approximately $137.0 million in
  sustaining maintenance capital, approximately $9.5 million in planned projects to invest in mine development" of the
  2026 guidance of $148M to $168M).

**Owner cash by year** (filed cash-flow statements; OCF less stock pay as filed on the cash-flow line, less all capex, less
contributions to DTA; USD millions; `arithmetic.py`):

| year | OCF | stock pay | capex | DTA | owner cash | source |
|---|---|---|---|---|---|---|
| 2017 | 314.3 | 20.4 | 83.1 | 5.7 | 205.1 | 10-K FY2019 (Contura before the ANR merger) |
| 2018 | 158.4 | 13.4 | 81.9 | 5.3 | 57.9 | 10-K FY2019 (merger 2018-11-09) |
| 2019 | 131.9 | 12.4 | 192.4 | 10.1 | -83.0 | 10-K FY2020 |
| 2020 | 129.2 | 4.9 | 154.0 | 3.4 | -33.1 | 10-K FY2022 |
| 2021 | 174.9 | 5.3 | 83.3 | 6.7 | 79.7 | 10-K FY2022 |
| 2022 | 1,484.0 | 7.5 | 164.3 | 19.6 | 1,292.7 | 10-K FY2022 |
| 2023 | 851.2 | 19.0 | 245.4 | 30.8 | 556.0 | 10-K FY2025 |
| 2024 | 579.9 | 12.3 | 198.8 | 32.5 | 336.2 | 10-K FY2025 |
| 2025 | 144.9 | 13.6 | 127.2 | 38.1 | -34.0 | 10-K FY2025 |
| H1 2026 | 68.9 | 8.0 | 85.8 | 23.3 | -48.2 | 10-Q Q2 2026 |

Five-year mean 2021-2025: **$446.1M**, of which 2022 alone is $1,292.7M. Seven-year mean 2019-2025: $302.1M. The five years
without the spike (2019, 2020, 2021, 2024, 2025): $53.2M. OCF in 2019-2021 is after $49M to $63M a year of cash interest on
debt since repaid and includes $64M to $72M a year of tax refunds; 2023 carries a $130M working-capital build and 2024 a
$210M release (receivables and inventory lines), which roughly offset.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the question is what the mines will produce, not what the quotation does, and the market "doesn’t
tell us anything. It just tells us prices." **[M2006-077]**. No macro enters as a forecast **[M2000-094]**; but for a
price-taker the price of its product is not macro, it is the business, and the speakers measure a mine by its cost: "If we
owned a copper mining company in its entirety, we would measure it, probably, more by cost of production than we would by
whether copper was selling for $2.00 a pound or a dollar a pound." **[M2006-004]**. Margin of safety: "if you have to
actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**. The analyst's habit: contrary
evidence "write it down in the first 30 minutes" **[M1997-127]**.

**Contrary evidence, written down as found** **[M1997-127]**: (1) the predecessor's CAPP operations earned a margin of
-$0.74 a ton in 2015 and $0.06 a ton in January to July 2016, the bankruptcy years (S-4, 0001628280-18-011255); (2) the
company lost $316.3M in 2019 and $446.9M in 2020 and retained earnings stood at -$361M at end-2020 (10-K FY2020); (3)
Warrior Met Coal's margin per ton exceeded AMR's in every year 2019-2025, by about 75% on the seven-year mean (Q2 row); (4)
AMR idled Elk Run (November 2024) and Long Branch (2025) and cut Jerry Fork and Black Eagle when prices fell (10-K FY2025),
which is what the marginal producer does; (5) owner cash was negative in 2019, 2020, 2025 and the first half of 2026; (6) a
storm damaged the DTA stacker reclaimer in June 2026 (10-Q Q2 2026). Found for the business: no debt to speak of ($11.4M at
2026-06-30), $338.5M of cash and short-term investments, 294.5M tons of reserves, 20% of US met coal output in 2024, its own
export terminal share, and an injury rate 38% better than the industry's (10-K FY2025).

## THE STANDING RULE
A cash purchase of a listed share, unlevered, sized so that a total loss is survivable, carries no call on the buyer: "One
investment rule at Berkshire has not and will not change: Never risk permanent loss of capital." **[L2023-005]**. The
target's own liabilities are Q9's, not the buyer's ruin. No breach.

---
## Q1 - CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**; "a reasonable probability of being able to asses where the business will be in 10
  years" **[M2000-037]**. The product can stay opaque if "I understand the economic dynamics of the industry. Is there —
  are there competitive moats? Is there ease of entry?" **[M2011-014]**.
- **The economics, from the filings.** AMR mines met coal in Virginia and West Virginia (14 underground and 5 surface
  mines, 8 preparation plants, 65% of the DTA export terminal), sold 15.3M tons in 2025, 73% of coal revenues abroad, Asia
  the largest export market (10-K FY2025, 0001704715-26-000010). Export prices are "market-indexed pricing that changes with
  the market monthly"; domestic contracts are fixed for a year. Its profit per ton is the seaborne index for its grade less a
  cost that moves slowly. The dynamics are the oldest in mining and change slowly; of a large oil company the speakers say
  "it’s fairly easy to get your mind around the economic characteristics that will exist in the business" **[M2004-081]**,
  and of a mine they would measure "cost of production" **[M2006-004]**.
- **The key variables and whether they are foreseeable** **[M1998-044]**. (1) Volume: 294.5M tons of proven and probable
  reserves at end-2025 against 15.3M tons sold, about 19 years, mine lives 1 to 24 years by complex (10-K FY2025):
  foreseeable. (2) Cost per ton: $70 to $112 a ton over 2019-2025 (Q2 row), moving with labor, royalties and geology:
  foreseeable within a band. (3) The price: $80.90 to $225.45 a ton realized over 2020-2022 alone (10-K FY2021,
  0001704715-22-000012; 10-K FY2022, 0001704715-23-000010): not foreseeable year to year, but bounded by the cost curve,
  which is test (2) of Q2. (4) Ten-year demand for coking coal as steelmaking shifts toward electric furnaces. The speakers
  call coal's decline "for sure, is secular" **[M2016-021]** and "Of course, we know coal’s going to be — you know, but that
  doesn’t mean we’re going to be phased out over time" **[M2021-041]**; for met coal the change is slow, and "slow change
  can be much harder to perceive, and can lull you to sleep easier" **[M2014-038]**.
- **Would the insiders write it down?** **[M2000-105]**. They do, for reserve reporting: Peabody's 10-K FY2025
  (0001064728-26-000006) states seaborne met price assumptions of "$200 to $221 per tonne" for 2026-2030 and Ramaco's 10-K
  FY2025 (0001104659-26-020479) states reserve prices of $131 to $184 a ton by complex. That is a written long-run price
  band, unlike the forecast the tech insiders refused.
- **Routing.** This is not a fast-changing industry closing at Q1 (the routing fixed under What understanding means). What
  the analyst cannot foresee is the price path, which for a price-taker is the castle question (Q2: whose cost sets the
  price) and the value question (Q7: how sure is the cash). The doubt rule **[M2002-092]** was applied to the economics, not
  to the price: the dynamics (index price, cost per ton, volume, reserves) can be read from the filings of AMR and four rivals.
- **VERDICT: IN**, with the price path carried forward as the open variable **[M2011-014]**, **[M2006-004]**,
  **[M2004-081]**. (The alternative reading, TOO HARD (NATURE) on the price, is recorded under What in the framework was
  wrong or unclear.)

## Q2 - WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now." **[M1995-038]**

- **Is it a commodity?** The rows define the commodity by the customer's indifference: "the product is available from many
  suppliers [...] most insureds don't care from whom they buy." **[L2004-003]**. AMR's own words: "The coal industry is highly
  competitive, both in the U.S. and internationally"; export met coal "competes directly with international sources of
  production" from Australia and Canada "on many of the same factors"; export pricing is index-linked monthly; demand and
  price "depend to a large extent on the demand and price for steel" (10-K FY2025). Quality grades (Low-Vol, High-Vol A and
  B) set the discount to the index, not a premium for the seller's name. The price is set by others, as at the gas station:
  "whatever he charged for gas was my price" **[M2012-109]**; "he determined our profit, because we looked at his price every
  day" **[M2023-079]**. It is a commodity.
- **Pricing power and the agony before a rise.** None to test: the company reports price as an index outcome. Realization
  per ton: 2020 $80.90, 2021 $115.18, 2022 $225.45, 2023 $179.40, 2024 $142.66, 2025 $117.08, H1 2026 $121.57 (10-Ks FY2021 to
  FY2025; 10-Q Q2 2026).
- **The one exception: the low-cost producer.** "when a company is selling a product with commodity-like economic
  characteristics, being the low-cost producer is all-important" **[L2000-017]**; "commodity businesses have risk unless
  you’re the low-cost producer, because the low-cost producer can put you out of business" **[M1997-010]**; the cost is
  measured against the competitor **[M2001-013]**; "It’s like comparing a copper producer whose costs are $2.50 a pound with a
  copper producer whose costs are $1 a pound. Those are two different kinds of businesses. One is going to go broke at a
  buck-fifty a pound." **[M2009-059]**.

**The competitor row** (margin per short ton = realized price less cash cost of sales, before depreciation, overhead and idle
mines; each from the company's own 10-K; Warrior reports per metric ton FOB Port of Mobile including freight and is
converted at 1.10231; AMR and Ramaco report FOB mine or net of freight; Arch and Peabody report segment cash margins):

| year | AMR (Met / CAPP-Met) | Warrior HCC | Ramaco METC | Arch Met | Peabody Seaborne Met |
|---|---|---|---|---|---|
| 2015 | -0.74 (predecessor CAPP) | not read | not read | 8.26 | not read |
| 2016 | 0.06 (Jan-Jul pred.) / 30.84 (Jul-Dec Contura) | not read | not read | 1.75 (Jan-Sep pred.) | not read |
| 2017 | 43.11 (Contura CAPP) | 81.7 | not read | 29.41 | not read |
| 2018 | 43.13 (Contura CAPP-Met) | 82.0 | 25 | not read | 40.09 |
| 2019 | 25.85 | 64.9 | 35 | 39.26 | 17.32 |
| 2020 | 10.71 | 18.9 | 14 | 13.04 | not read |
| 2021 | 37.47 | 76.2 | 39 | not read | 32.28 |
| 2022 | 117.22 | 178.3 | 99 | 130.30 | 117.86 |
| 2023 | 67.73 | 98.9 | 59 | 77.03 | not read |
| 2024 | 30.64 | 62.8 | 35 | merged into Core | 22.20 |
| 2025 | 14.85 | 31.3 | 22 | (Core, not read) | 6.57 |
| mean 2019-25 | **43.5** | **75.9** | **43.3** | | |

Sources: AMR, S-4 0001628280-18-011255 (2015-2017), 10-K FY2018 0001704715-19-000013, FY2019 0001704715-20-000010, FY2021
0001704715-22-000012, FY2022 0001704715-23-000010, FY2023 0001704715-24-000028, FY2024 0001704715-25-000010, FY2025
0001704715-26-000010. Warrior, 10-K FY2019 0001691303-20-000014, FY2022 0001691303-23-000010, FY2025 0001193125-26-048914 (net
selling price less cash cost of sales per metric ton, e.g. 2025 $146.20 less $111.66). Ramaco, 10-K FY2019
0001558370-20-001079, FY2020 0001558370-21-001215, FY2022 0001558370-23-003736, FY2023 0001558370-24-003256, FY2025
0001104659-26-020479 (revenue less cash cost per ton FOB mine, whole dollars as filed). Arch, 10-K FY2017
0001628280-18-002109, FY2020 0001558370-21-000957, FY2023 0001558370-24-001229 (Met segment cash margin per ton sold; cash cost
$89.08 in 2023 and $93.61 in 2022 against AMR's $111.67 and $108.22). Peabody, 10-K FY2019 0001064728-20-000007, FY2022
0001064728-23-000013, FY2025 0001064728-26-000006 (Adjusted EBITDA margin per ton, Seaborne Metallurgical). Core Natural
Resources' 10-K FY2025 (0001710366-26-000007) was fetched and not read. The definitions differ at the edges (AMR's
non-GAAP cost excludes $29.0M of idled and closed mine costs in 2025, about $1.90 a ton); the order of the rows does not turn
on them.

- **What the row shows, over the whole span, not one year.** AMR is a middle-of-the-curve producer. Warrior earned more per
  ton than AMR in every year read, about 75% more on the 2019-2025 mean; Arch's Met segment ran $15 to $23 a ton cheaper in
  cash cost in 2022-2023; Ramaco earned the same as AMR; Peabody's seaborne mines earned less in four of the five years read since 2019 (2022 about equal).
  AMR is not the low-cost producer. Its own filing says "cost-competitive", not lowest (10-K FY2025, Item 1).
- **The trough test, which the low-cost producer passes and the others do not.** In the last full trough the predecessor's
  CAPP operations earned -$0.74 a ton (2015) and $0.06 a ton (January to July 2016), and Alpha Natural Resources went through
  bankruptcy (S-4; 10-K FY2025, "Our History"). In 2020 AMR's met margin was $10.71 a ton before overhead and idle mines, and
  the company lost $446.9M; in 2025 it was $14.85 and owner cash was -$34.0M. The high-cost producer's end is written: "In an
  unregulated commodity business, a company must lower its costs to competitive levels or face extinction." **[L1994-035]**;
  "sooner or later, the nature of a capitalist society is that the guy with the lower cost comes in and kills you."
  **[M2001-013]**.
- **The attacker with money** **[M2011-015]**. A new US met mine is hard to permit and slow to build (AMR's Kingston Wildcat mine began development in 2024 for first coal in 2026), so entry is not easy. But the price is not set by US entrants; it is set by Australian,
  Canadian and other seaborne supply (10-K FY2025, Competition). The barrier protects the incumbent's tons, not its price.
  Fewness does not cure a commodity: "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**.
- **Unit volume, widening or narrowing.** Tons sold: 15.5M (2020), 16.8M (2021), 16.4M (2022), 17.1M (2023), 17.1M (2024),
  15.3M (2025), guided 15.1M to 16.5M for 2026. Flat. The workforce is 97% union-free and wages were cut in Q2 2025 (10-K
  FY2025): the cost work is real, but it is the "foot-to-the-floor" of a company holding no low-cost title, not the widening
  of one it holds **[L2004-007]**.
- **Ask the competitors.** The speakers name coal for this test: asking ten coal executives which rival they would own for
  ten years gives "a better fix on the economics of the coal industry than any one of those individuals has" **[M2017-091]**;
  also **[M2014-057]**. Not done (no access); the filed margins above are the nearest public answer.
- **What could destroy it.** A long fall in seaborne prices toward the curve's middle (2015-2016, 2019-2020 and 2025 show what
  that does to AMR); the steel transition; collateral demands (DOL black lung rule, $80M to $100M), the New York Climate
  Change Superfund Act ("our liquidity would be materially, adversely affected" if upheld), the silica rule (10-K FY2025).
- **The other routes through a commodity field.** L2004-007 begins "Another way", so the low-cost position is not the only
  route the rows allow **[L2004-007]**. Searched for one here: the DTA terminal and blending let AMR serve many grades and five
  continents, which is a service and logistics edge; nothing in the filings shows it earning a margin above Ramaco's, which
  has no terminal. No other route found.
- **VERDICT: OUT.** A commodity seller whose price is set by others **[M2012-109]**, **[L2004-003]**, that is not the low-cost
  producer on its own competitors' filed numbers over the whole span **[L2000-017]**, **[M1997-010]**, **[M2009-059]**, and
  whose predecessor met the end the rows predict for the high-cost producer in the last trough **[L1994-035]**. The castle is
  shown open on the evidence, so the box is OUT, not TOO HARD **[M2006-013]**; price does not reopen it: "What you can’t do is
  turn any investment into a good deal by paying little" **[M2019-015]**; marginal businesses bought cheap "are the wrong
  foundation on which to build a large and enduring enterprise" **[L2014-009]**. The policy in one line: "We’re going to be
  investors in businesses, not commodities, by and large." **[M2007-131]**.

**The file closes here. Q3 to Q12 are NOT REACHED; nothing below is a clearance.**

---
## Q3 - HOW MUCH CAPITAL MUST GO IN. NOT REACHED.
Facts only, for the record: capex $127.2M in 2025 against D&A of $174.5M; 2026 guidance $148M to $168M with about $137M
"sustaining maintenance capital"; plus about $21M a year for DTA upgrades over five years (10-K FY2025). Capex ran $153M to
$245M in 2019, 2020, 2023 and 2024 while new mines were developed.

## Q4 - DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED. The balance sheets, read as the brief and the template ask
(filed balance sheets; `tools/run.py` table checked against the 10-Ks; USD millions):

| year-end | equity | cash | receivables | inventory | goodwill | debt | retained earnings |
|---|---|---|---|---|---|---|---|
| 2017 | 93 | 142 | 127 | 70 | 0 | 362 (partial tag) | 104 |
| 2018 | 1,071 | 234 | 293 | 122 | 96 | 588 | 403 |
| 2019 | 696 | 213 | 245 | 163 | 0 | 593 | 87 |
| 2020 | 200 | 139 | 146 | 108 | - | 583 | -361 |
| 2021 | 547 | 81 | 489 | 129 | 0 | 449 | -72 |
| 2022 | 1,430 | 302 | 407 | 201 | 11 | 11 | 1,275 |
| 2023 | 1,574 | 268 | 510 | 231 | 11 | 10 | 1,970 |
| 2024 | 1,649 | 482 | 362 | 169 | 11 | 6 | 2,156 |
| 2025 | 1,545 | 366 | 279 | 193 | 11 | 13 | 2,095 |
| 2026-06 | 1,499 | 308 (+31 short-term) | 231 | 262 | - | 11 | 2,071 |

What the figures say: equity was made by the 2018 all-stock merger (2017 $93M to 2018 $1,071M), then two loss years took it
to $200M and retained earnings to -$361M (goodwill of $124.4M written off in 2019, asset impairments of $83.5M in 2019 and
$256.5M in 2020; 10-K FY2020). The 2022 price spike repaid $450.6M of debt in one year and rebuilt equity; since then about
$1.17B has gone to buybacks (treasury stock $1,377.7M at 2026-06-30). Receivables move with the index (from $146M to $489M in
one year, 2020 to 2021), which is the price-taker's balance sheet. What they do not say: the long-tail obligations, carried at
$204.2M for asset retirement, $188.6M for workers' compensation and black lung and $76.1M for pensions at 2026-06-30, are
undiscounted at $497.8M (ARO), $284.2M (black lung), $70.7M (workers' compensation) and $982.8M (pension, paid from a trust
with $370.1M of assets against a net obligation of $87.3M) at end-2025 (10-K FY2025, Contractual Obligations). Restricted cash
of $128.2M and restricted investments of $34.5M are collateral, not free cash. Inventory rose $69M in the first half of 2026.
Adjusted EBITDA is the filer's headline measure and the annual bonus formula's (proxy, "AIB EBITDA" of $139.98M for 2025);
noted, not judged.

## Q5 - WHO RUNS IT. NOT REACHED.
## Q6 - WHAT WILL THEY DO WITH THE MONEY. NOT REACHED.
Facts for the record: buybacks under the $1.5B program (no price limit stated; 10-K FY2025 Note 7 and 10-Q Q2 2026):
3,544,413 shares for $516.8M in 2022 (average $145.82), 2,930,858 for $523.1M in 2023 ($178.48), 155,264 for $58.8M in 2024
($378.60), 247,914 for $40.0M in 2025 ($161.31), 156,648 for $31.0M in H1 2026 ($197.86); 7,035,097 shares for $1,169.7M in
all, average $166.27 (`arithmetic.py`). Debt of $588M at end-2018 repaid by end-2022. Dividends $113.0M in 2023 (including a
special), then ended. Set against the computation below only as arithmetic: the overall average sits under the
whole-cycle central figure; the 2024 purchases sat above it.

## COMPUTATION - NOT A CLEARANCE (the owner's reporting request; the file closed OUT at Q2)
*(The heading uses a hyphen in place of the protocol's dash, under the standing no-em-dash rule; the meaning is the
protocol's.)* No entry language attaches to anything in this section.

**(a) Value range, by the Q7 CONVENTION.** Five-year mean owner cash 2021-2025, $446.1M. The growth "shown" cannot be
measured: the base year is $79.7M and the end year -$34.0M, so the shown-growth end is undefined and the convention collapses
to its no-growth case: $446.1M / 5.63% = $7,924M, plus net cash of $327.1M (cash $307.6M and short-term investments $30.9M
less debt $11.4M, 10-Q Q2 2026), over 12.679M shares = **$651 a share**. This figure is driven by one year (2022, $1,292.7M)
and is not a central case.

**Whole-cycle variant** (asked because the window holds the 2022 spike): seven-year mean 2019-2025, covering the 2019-2020
trough, the spike and the 2025 trough: $302.1M, no growth at the sovereign, **$449 a share**. The five non-spike years
(2019-2021, 2024-2025): $53.2M, **$100 a share**. Whole-cycle range $100 to $449 (4.5 to 1), and $100 to $651 (6.5 to 1)
counting the convention's figure: wider than the convention's three to one, so had Q7 been reached it would have closed TOO
HARD on width alone **[L2000-025]**.

**(b) Fair price** (the price at or below which the central case clears the ~10% pre-tax floor CONVENTION of Q7,
**[M2003-149]**, **[L2002-020]**). Central case: the seven-year whole-cycle mean, $302.1M after tax. Tax treatment: owner
cash is after cash taxes; pre-tax adds back the mean net cash tax of 2019-2025, $3.9M a year (payments of $139.7M in 2022 and
$79.2M in 2023 against refunds of $64M to $72M a year in 2019-2021), giving $305.9M pre-tax. $305.9M / 10% = $3,059M, plus
$327.1M net cash, / 12.679M = **$267 a share**.

**(c) Cheap price.** CONVENTION of this run (ours, confessed): the price at which even the five non-spike years' mean
($53.2M, after tax, refunds left in as a conservative choice since they were carrybacks that will not recur) earns 10% on the
price after counting net cash, so that no forecast of a second spike is needed: $53.2M / 10% = $532M, plus $327.1M, / 12.679M
= **$68 a share**. Net cash alone is $25.80 a share.

**Against the price of $175.05:** below the fair price of $267, well above the cheap price of $68, inside a whole-cycle range
of $100 to $449. None of it is a buy signal: the file is OUT at Q2, and "it ought to just kind of scream at you" **[M1996-084]**;
this needs a pencil and a choice of years.

## Q7 to Q10, Q12 - NOT REACHED.
For the record only (Q9 facts): debt $11.4M; ABL facility $225M with $41.3M of letters of credit; surety bonds $170.0M;
minimum-liquidity covenant $75M; possible black lung collateral of $80M to $100M; Climate Superfund Act exposure unquantified
(10-K FY2025). Q12 not asked.

---
## THE BOX
**OUT at Q2.** A met coal miner selling into an index-priced seaborne market, a commodity on its own filing's words, that is
not the low-cost producer: Warrior earned about 75% more per ton on the 2019-2025 mean and more in every year read, Arch's
Met segment ran $15 to $23 a ton cheaper in cash cost (2022-2023), and the predecessor's CAPP mines earned nothing in the 2015-2016 trough that ended in
bankruptcy. Computation only, not a clearance: $175.05 against a whole-cycle range of $100 to $449, fair about $267, cheap
about $68.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. Not written question by question with a commit after each: the brief forbids
      commits, and the file was written whole after the reading, once the session resumed.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row's text
      (`Test Runs/_research 2026-10-05 AMR/cite_check.py`, result recorded below); no v4 id. Every filing fact carries its
      accession.
- [x] The order was kept; Q2 failed and closed the run; nothing after it is a clearance, and the computation is headed so.
- [x] Owner cash after every real cost (stock pay, all capex, DTA contributions), never a net-income proxy; the sovereign
      from the Treasury curve; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found, in the foundations paragraph.
- [x] Not a point-in-time run; no anchor bar applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; one XBRL figure (2020 capex) was overruled by the filed statement.
- [x] `python tools/check_framework.py` run before handing back (result recorded below). No commit made, per the brief.

**Checks run 2026-10-05:** see the final lines of this file.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Q1 for a price-taker.** The framework's Q1 asks for the ten-year "earning power", and a miner's earning power is its
   price, which no one can foresee; read strictly, every commodity producer closes TOO HARD (NATURE) at Q1, and Q2's
   commodity paragraph (the low-cost exception) would never be reached. The rows point the other way (**[M2006-004]**, measure
   a mine by its cost of production; **[M2004-081]**, oil economics are "fairly easy"), and the routing note only fixes
   fast-changing industries. This run read Q1 as the economic dynamics and carried the price path to Q2 and Q7. A sentence
   saying so in Q1 (or saying the reverse) would stop two analysts closing the same miner at different questions.
2. **Q2 has no rule for "middle of the curve".** The rows rule out "the high-cost producer" and admit "the low-cost
   producer"; AMR is neither, with one rival far better, one equal and one worse. This run read the exception strictly (the
   rows say "all-important" and "unless you’re the low-cost producer") and closed OUT. A reader who takes "high-cost" literally
   could call it TOO HARD instead. The text should say which.
3. **The Q7 range convention breaks when the five-year window starts low and ends negative.** "Growth shown" is undefined
   here, so the range collapses to one no-growth figure dominated by one year. The convention says nothing about a cyclical
   window; the whole-cycle variant was the owner's request, not a rule. A rule for cyclical businesses (window choice, or a
   margin-times-volume normalization) is missing.
4. **Cash taxes for the pre-tax floor.** The floor is pre-tax and owner cash is after tax; for a company with carryback
   refunds the add-back can be negative. This run used the mean net cash tax over the window and said so; the framework does
   not say how.
5. **The protocol's heading carries an em dash**; the operator's standing rule forbids them. This run wrote a hyphen and
   said why.
6. **Equity affiliates that are operating infrastructure.** The DTA terminal is booked as an equity investment, so its
   capital calls fall outside "capex" and outside `tools/run.py`. Q4's equity-method CONVENTION covers income, not
   contributions; this run deducted the contributions as a real cost. The framework is silent.

## WHAT I COULD NOT GET
The proxy's summary compensation table did not survive the text conversion and was not transcribed (Q5 not reached). Peer
rows missing: Warrior, Ramaco and Peabody before 2017 or 2018; Arch 2018 and 2021; Peabody 2020 and 2023; Core Natural
Resources' met segment for 2025 (fetched, not read). Global cost-curve position against Australian producers comes only
through Peabody's seaborne segment; BHP's and others' filings were not read. Predecessor ANR results are segment margins from
the S-4, not full statements. No management or competitor was interviewed.

---
**Checks run 2026-10-05, after the last edit:** `python tools/check_framework.py` PASS (output saved to
`Test Runs/_research 2026-10-05 AMR/check_framework_output.txt`); `python "Test Runs/_research 2026-10-05 AMR/cite_check.py"`:
37 ids cited, no E-ids, every id in `principle_ledger_v5.csv`, every quoted fragment beside an id found in that row, 0
problems. Not committed, per the brief.
