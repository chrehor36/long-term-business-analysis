# Company Run — Archrock, Inc. (NYSE: AROC) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is barred by this session's blind rule, so
the analyst does not know whether the operator holds AROC. The run is written as if he does not.

**CONTAMINATION DECLARED.** Read before the run: `CLAUDE.md`, the operator protocol, the v5 framework in full, the
template, the v5 ledger by id, and the memory index the harness loads (it says in general terms that no name is
buyable; it says nothing about AROC). The session's git status showed commit subjects naming other runs' boxes (ENSG
OUT at Q4, OSIS OUT at Q2, MBUU OUT at Q2) and an untracked BOOT run file name; none was opened and none concerns this
company. No file about Archrock in `Test Runs/`, `Screens/` or `PORTFOLIO.md` was opened. `tools/run.py` printed only
arithmetic and no verdict for this name. Working folder: `Test Runs/_research 2026-10-05 AROC/` (filings as text,
`run_py_output.txt`, `returns_calc.txt`, `per_hp_calc.txt`, `value_calc.txt`).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $29.97 (2026-10-05; the quote printed by `tools/run.py`, an aggregator, live quote only, flagged per
  operator rule 5).
- **Shares by class** from the latest filing's cover: 175,338,185 common, single class (10-Q for the period ended
  2026-06-30, filed 2026-08-05, accession `0001389050-26-000028`; `python Screens/cover_shares.py AROC`, cover as of
  2026-07-29). Preferred stock authorized, none issued (10-K balance sheet).
- **Market cap:** $5,254.9M (29.97 x 175.338M).
- **Sovereign for the earnings currency:** USD, 30-year par yield 5.63%, US Treasury daily par yield curve, 2026-10-02
  (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-26, accession `0001389050-26-000009` (Business,
  Risk Factors, MD&A, the statements, the tax note); 10-Q for 2026 Q2, accession `0001389050-26-000028`; proxy (DEF 14A)
  filed 2026-03-17, accession `0001104659-26-029581` (pay design and the summary compensation table only); 8-Ks of
  2026-06-25 (`0001104659-26-077839`, CFO appointed, the former CFO retiring) and 2026-09-28 (`0001389050-26-000034`,
  the chief accounting officer retiring). For the ten-year record: 10-Ks for FY2015 (`0001389050-16-000047`), FY2017
  (`0001389050-18-000006`), FY2018 (`0001389050-19-000021`), FY2020 (`0001389050-21-000011`), FY2022
  (`0001389050-23-000013`) and FY2024 (`0001389050-25-000009`).
- **One figure cross-checked against the filed statement:** net cash from operating activities FY2025 $622,107
  thousand in the filed cash flow statement (10-K `0001389050-26-000009`, page F-6) equals the `tools/run.py` OCF of
  622 and the XBRL fact. Capital expenditures $502,465 thousand equals the tool's 502.
- **`tools/run.py AROC`, arithmetic lines only, each checked against the filing:**
  - OCF and capex for 2023 to 2025 agree with the filed cash flow statements.
  - **Stock pay is wrong in the tool:** it prints SBC of 21, 33 and 32 for 2023 to 2025; the filed cash flow statement
    shows stock-based compensation expense of $12,998, $14,646 and $19,027 thousand. The filed figures are used.
  - The tool's "OE lo / OE hi" columns and its yields are not used; owner cash is rebuilt below from the filings.
  - The tool's balance-sheet table is the first-filed XBRL; blanks (2016, 2017 to 2019 debt) are filled from the filed
    statements below. Its "lt debt" column is non-current debt, which is all of the debt here (no current maturities).
- **Owner cash after every real cost, by year** (US$M; OCF and capex from the filed cash flow statements; stock pay
  as filed; growth and maintenance capex as the filer splits them in MD&A):

| Year | OCF | Stock pay | Capex (all) | of which maintenance (filer) | PP&E sale proceeds | D&A | OCF - stock pay - all capex | same, net of PP&E sales |
|---|---|---|---|---|---|---|---|---|
| 2016 | 274.1 | 9.0 | 117.6 | 33.6 | 41.9 | 209.0 | 147.5 | 189.4 |
| 2017 | 201.9 | 8.5 | 221.7 | 35.7 | 47.0 | 188.6 | -28.3 | 18.7 |
| 2018 | 225.9 | 7.4 | 319.1 | 49.7 | 33.9 | 174.9 | -100.6 | -66.7 |
| 2019 | 290.1 | 8.1 | 385.2 | 58.6 | 81.0 | 188.1 | -103.2 | -22.2 |
| 2020 | 335.3 | 10.6 | 140.3 | 32.0 | 18.9 | 193.1 | 184.4 | 203.3 |
| 2021 | 237.4 | 11.3 | 97.9 | 47.3 | 29.6 | 178.9 | 128.2 | 157.8 |
| 2022 | 203.4 | 11.9 | 239.9 | 84.2 | 20.7 | 164.3 | -48.4 | -27.7 |
| 2023 | 310.2 | 13.0 | 298.6 | 92.2 | 72.2 | 166.2 | -1.4 | 70.8 |
| 2024 | 429.6 | 14.6 | 359.0 | 87.8 | 67.6 | 193.2 | 56.0 | 123.5 |
| 2025 | 622.1 | 19.0 | 502.5 | 110.7 | 120.8 | 256.8 | 100.6 | 221.5 |

  Five-year average 2021 to 2025: **$47.0M** after all capital spending; **$109.2M** net of recurring compressor-sale
  proceeds (the 2025 sale of the Flowco business, $71.0M, is left out as not recurring). Not deducted above: cash paid
  for acquisitions, $214.0M (2019, Elite), $866.2M (2024, TOPS) and $294.6M (2025, NGCS), plus the stock issued in each.
  Ten-year sum 2016 to 2025: OCF less stock pay $3,016.6M against capital spending of $2,681.8M plus $1,374.8M of cash
  acquisitions. Cash taxes paid were $3.3M in 2025 against a provision of $100.8M ($97.8M deferred); the FY2025 tax
  note shows federal NOL carryforwards of $648.6M still sheltering income, so the owner cash above is flattered by a
  shelter that is being used up.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content owning this "if the market closed for five years"
(**[M1997-109]**), and here that means owning a fee-for-horsepower fleet whose price per horsepower is set by how many
compressors the industry has built. The market serves and does not instruct: "It just tells us prices." (**[M2006-077]**),
so the 2023 to 2026 rise in the share price is no evidence about the castle. No macro forecast enters: "macro
conclusions are — just never enter into the discussion" (**[M2000-094]**); the gas-demand story the filer tells (LNG,
data centres) is a macro forecast and is not used as a reason, while what counts is "the average profitability of the
business over time and how strong its competitive mode is" (**[M2015-016]**, the transcript's word). Margin of safety:
if it needs pencil and paper "it’s too close to think about" (**[M1996-084]**). The analyst's habits: hunt "what’s
wrong in things" (**[M2025-013]**) and read competitors "to possibly reject your original hypothesis" (**[M1998-144]**).

**Contrary evidence, written down as found** **[M1997-127]** (the habit is to "write it down in the first 30 minutes"):
1. The filer's own Business section, FY2025 10-K: "The natural gas compression services business is highly
   competitive with low barriers to entry." Risk factors add new entrants, competitors that "may expand or fabricate
   new compressors", customers that "may purchase and operate their own compression fleets", and customer
   consolidation used to pursue "pricing concessions".
2. Revenue per average operating horsepower per month was $17.98 in 2015 and $16.97 in 2022 (computed from the
   segment figures of each 10-K): seven years of no nominal price rise, a real decline.
3. Utilization fell to an 81% average in 2016 and 82% in 2021; contract operations revenue fell 17% in 2016 and 6% more
   in 2017.
4. The dividend was cut from $0.1875 to $0.095 a quarter in May 2016 (FY2017 10-K dividend table).
5. Dividends paid 2018 to 2025 ($753.0M) exceeded net income for the same years ($722.0M); the accumulated deficit
   was $2,241M at 2017 and $2,257M at 2025. Debt rose from $1,417M (2017) to $2,411M (2025); shares went from 69.7M
   diluted (2017) to 174.8M (2025) through the 2018 roll-up of Archrock Partners (1.40 shares per unit), the 2019 Elite
   deal (21.7M shares to a Hilcorp affiliate), a 2024 offering of 12.65M shares and stock paid for TOPS and NGCS.
6. The $100.6M of goodwill bought with Elite in 2019 was written off in full in 2020.
7. Cost of sales per horsepower is the same at Archrock, Kodiak and USA Compression in 2025 (Q2 below): no low-cost
   position.
8. Kodiak "began operations in 2011" (KGS FY2023 10-K, accession `0001767042-24-000011`) and by the end of 2023 ran
   3.26M horsepower against Archrock's 3.76M: a new entrant reached near-equal scale in twelve years.
9. Pay: 80% of the 2025 annual incentive for the chief executive is weighted on Adjusted EBITDA (proxy).
10. 2026 so far (10-Q Q2): spot utilization 94% against 96% a year earlier, operating horsepower down from 4,651
    thousand to 4,516 thousand, aftermarket revenue down 35% in the quarter.
11. FY2025 cost of sales carried a $35.0M sales-and-use-tax settlement benefit that flatters the record 73% margin.

Evidence for the business, written down beside it: three years of rising price per horsepower (to $23.59 in 2025),
utilization at 95 to 96% from 2023 to 2025, consolidation to three large public fleets, a fleet that stays about six
years at a site, about 300 customers with the top five at 35% of revenue, no customer over 10%.

## THE STANDING RULE
Owning a share bought with the buyer's own money and not borrowed does not put the buyer at risk of ruin; the rule
binds the buyer's financing and sizing: "We are never going to risk what we have and need for what we don’t have and
don’t need." (**[M2012-081]**); "borrowed money has no place in the investor's tool kit" (**[L2014-005]**). Nothing here
is reached, since the file closes at Q2.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" (**[M2012-065]**), "a reasonable probability of being able to asses where the business
  will be in 10 years" (**[M2000-037]**, the transcript's spelling). The product need not be understood in detail; what
  must be is the industry's economics: "I understand the economic dynamics of the industry. Is there — are there
  competitive moats? Is there ease of entry?" (**[M2011-014]**).
- **The key variables, and how predictable** (**[M1998-044]**: "trying to identify the key variables in that
  particular business, and evaluating how predictable they were first"): (1) horsepower demanded, which follows US
  gas production and the pressure decline of maturing wells (60% of the operating fleet in gathering and processing,
  40% in gas lift; FY2025 10-K); (2) price per horsepower, a fixed monthly fee per unit set at contracting, with an
  initial term of 12 to 36 months (up to 60 for the largest units) and month-to-month thereafter on 30 days' notice;
  (3) the capital per horsepower added. Variable (1) is a volume driven by a large, slow-moving industry; variable (2)
  is set by the industry's supply of compressors, which is the castle question of Q2; variable (3) is disclosed.
- **Do the past statements tell me the future ones?** (**[M2008-033]**: whether "the financial statements will tell me
  the information that’s useful to me in making a judgment about what the future financial statements are going to look
  like"). Yes: the filer reports available and operating horsepower, utilization, segment revenue and margin, and splits
  capex into growth and maintenance every year since at least 2013, so the economics per horsepower can be rebuilt for a
  full cycle (Q2's table).
- **Routing.** Reciprocating compressors driven by gas engines or electric motors are not a fast-changing technology;
  the move toward electric drive and emissions rules is a slow change to the fleet, not one that puts the ten-year
  economics out of sight. Not a bank, not a holding company.
- **VERDICT: IN.** The business is a fee per horsepower on a fleet whose demand, pricing and capital needs are all
  disclosed over a full cycle; what is unknown is whether rivals let the price hold, and that is Q2's question, which
  Q1 reaches by passing it (**[M2011-014]**, **[M2012-065]**).

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." (**[M1995-038]**), asked in the knowledge that "most moats aren’t worth a damn in, you know,
in capitalism" (**[M1995-038]**). A moat is what "protects excellent returns on invested capital" (**[L2007-004]**); so
the first thing to read is whether there are excellent returns to protect.

**What the castle has earned, through the cycle** (pre-tax income plus interest, over year-end debt plus equity; filed
figures; `returns_calc.txt`):

| Year | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| EBIT / (debt + equity) | -0.3% | 2.1% | 5.4% | 5.6% | 0.8% | 6.1% | 6.7% | 10.3% | 10.1% | 15.1% |

Ten-year sum of EBIT over the ten-year sum of capital: about 6.9%, before tax, against a 30-year Treasury of 5.63% today.
The one year above 15% is 2025, which includes $47.1M of asset-sale gains and the $35.0M tax settlement. A business
whose castle protected "excellent returns" would show them through 2016 to 2022 as well; it did not.

**The tests, each with its filing fact.**
1. **The castle questions.** Why do customers rent from Archrock rather than from another fleet? The filer's answer is
   safety, large-horsepower units, service, geographic density and history; its own Competition paragraph answers the
   permanence question: "highly competitive with low barriers to entry", competing "with respect to price, equipment
   availability, customer service" (FY2025 10-K, `0001389050-26-000009`). Price and availability are the terms of a
   commodity.
2. **Would it stand without the lord?** Not the issue here: the fleet runs under standard maintenance programmes; the
   weakness is not dependence on a manager but the absence of a barrier.
3. **The money test.** "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do
   it? [...] If the answer had been yes, we wouldn’t have done it." (**[M2011-015]**). Here the answer has been given on
   the record: Kodiak began in 2011 and, with private-equity money (EQT Partners from 2019), reached 3.26M horsepower by
   the end of 2023 against Archrock's 3.76M, and 4.46M in 2025 against Archrock's 4.79M (KGS 10-Ks
   `0001767042-24-000011`, `0001767042-26-000012`). The filer adds that customers can build their own fleets and
   competitors "may expand or fabricate new compressors"; Enerflex, a manufacturer, says its US rental fleet (483,000
   horsepower) benefits from "vertical integration" with its own fabrication (40-F exhibit 99.3, accession
   `0001193125-26-072743`). Munger's railroad and airline: "and you can create another airline. [...] That’s what we
   don’t like about it." (**[M2013-054]**). This is the airline side.
4. **Pricing power, and the agony before a rise.** "you can almost measure the strength of a business over time by the
   agony they go through in determining whether a price increase can be sustained" (**[M2005-020]**); "you learn a lot
   about the durability of the economics of a business by observing the behavior of — the price behavior"
   (**[M2005-020]**). The price behaviour, per average operating horsepower per month, from each 10-K's segment figures
   (`per_hp_calc.txt`):

| Year | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Revenue / hp / month ($) | 18.22 | 18.16 | 17.98 | 16.69 | 16.15 | 16.55 | 17.34 | 16.84 | 16.46 | 16.97 | 18.98 | 21.53 | 23.59 |
| Adj. gross margin / hp / month ($) | 10.02 | 10.28 | 10.63 | 10.33 | 9.20 | 9.83 | 10.66 | 10.89 | 10.25 | 9.99 | 11.79 | 14.44 | 17.23 |
| Average utilization (%) | | | 85 | 81 | 82 | 87 | 88 | 86 | 82 | 87 | 95 | 95 | 96 |

   From 2013 to 2022 the price per horsepower did not rise in dollars; prices rose only from 2023, when utilization
   reached 95%, and the filer attributes the gains to "higher rates" in a market where production grew to records.
   (A caveat honestly carried: the fleet's mix moved toward larger units, which rent for less per horsepower, so part of
   the flat decade is mix; margin per horsepower, which mix affects less, was also flat at about $10 from 2015 to 2022.)
   A price that rises only when the whole industry's fleet is full is the market's price, not the firm's.
5. **Unit volume and share of mind.** There is no share of mind: customers buy horsepower. Share of market is roughly
   even among three fleets (Archrock 4.79M, Kodiak 4.46M, USA Compression 3.89M horsepower at end 2025, each from its
   own 10-K).
6. **The low-cost position.** In a commodity the one named route is cost: "Another way to prosper in a commodity-type
   business is to be the low-cost operator." (**[L2004-007]**); "commodity businesses have risk unless you’re the
   low-cost producer, because the low-cost producer can put you out of business" (**[M1997-010]**). The test is relative
   cost: "if your costs are on parity or less — labor costs — than your other major competitors, that is much more
   important to you than the absolute level" (**[M2001-013]**), and the difference that matters is the copper producer
   "whose costs are $2.50 a pound with a copper producer whose costs are $1 a pound. Those are two different kinds of
   businesses." (**[M2009-059]**). The 2025 cost of sales per revenue-generating horsepower per month: Archrock $7.01
   (excluding the one-time tax benefit), Kodiak $7.23, USA Compression $7.03. Parity, not advantage. Over the whole span
   2016 to 2025 Archrock's contract-operations margin averaged 62.7% against USA Compression's 64.8% (competitor row
   below); Archrock led only from 2023, on price, not cost.
7. **The brand in the customer's mind.** None; no customer asks for Archrock by name. Preferred-vendor arrangements
   give some customers "preferential consideration" in exchange for "favorable pricing" (FY2025 10-K, Customers).
8. **Would the customer still choose it over the low bid?** The test of See's was that "it wouldn’t be a question of
   people buying candy for the low bid" (**[M2017-009]**). Here the filer says the renewal of its contracts "at rates
   sufficient to maintain current revenue" depends on competitors' activity, and that consolidated customers use
   "purchasing power to pursue economies of scale and pricing concessions". The commodity description fits: "most
   insureds don't care from whom they buy" (**[L2004-003]**).
9. **Ask the competitors.** No conversation was held; the competitors' own filings were read in its place. USA
   Compression: "The natural gas compression business is highly competitive" and customers "may choose to vertically
   integrate their operations by purchasing and operating their own compression fleets", helped by "attractive
   financing terms from financial institutions and equipment manufacturers" (10-K FY2025, `0001522727-26-000015`).
   Kodiak: competitors that may "adopt more aggressive pricing policies" (10-K FY2025). All three describe the same open
   field.
10. **Widening or narrowing?** The question is "how wide the moat is and whether it’s likely to widen further or shrink
    on you" (**[M1999-108]**). The 2023 to 2025 rise in price is the strongest evidence for widening; against it, the 2026
    10-Q already shows spot utilization down to 94% and operating horsepower down 3% from a year earlier while
    competitors keep adding new large units (Kodiak fleet up 1.2%, Enerflex US fleet up from 428,000 to 483,000
    horsepower in 2025).
11. **What could destroy, modify or reduce it?** Customers owning their own fleets; competitors and manufacturers
    building new units whenever rates are high; customer consolidation; a fall in associated-gas activity in the
    Permian and Eagle Ford, which carry about three-quarters of Archrock's operating horsepower (FY2025 10-K).

**The competitor row** (each from its own filings; `per_hp_calc.txt`, `returns_calc.txt`):

| Metric | Archrock | USA Compression (USAC) | Kodiak (KGS) | Enerflex (EFXT) |
|---|---|---|---|---|
| Fleet horsepower, end 2025 | 4.79M | 3.89M | 4.46M | 0.48M (US rental) |
| Revenue / hp / month 2025 | $23.59 | $21.38 (filed) | $22.88 | not disclosed on this basis |
| Cost of sales / hp / month 2025 | $7.01 (ex tax benefit) | $7.03 | $7.23 | not disclosed |
| Adj. gross margin %, 2025 | 73% (70% ex benefit) | 67.1% | 68.4% | 57.3% (global EI line, incl. BOOM) |
| Margin %, average 2016-2025 | 62.7% (contract ops) | 64.8% (total revenues) | IPO 2023; n/a | n/a |
| Revenue / hp / month, 2016 and 2020 | $16.69 and $16.84 | $16.58 and $16.71 | n/a | n/a |
| Operating return, sum 2016-2025 (2021-2025 for KGS); AROC as pre-tax income plus interest, peers as operating income | 6.4% of total assets | 3.6% of total assets (goodwill write-offs of $223.0M in 2017 and $619.4M in 2020) | 6.8% of total assets | n/a |
| Operating return, 2021-2025 | 9.4% of total assets | 8.4% of total assets | 6.8% of total assets | n/a |
| Accessions | `0001389050-26-000009` and earlier 10-Ks above | `0001522727-26-000015`, `-25-000010`, `-23-000006`, `-21-000010`, `0001558370-19-000738`, `0001558370-18-000600` | `0001767042-26-000012`, `0001767042-24-000011` | `0001193125-26-072743` |

The three US fleets move together: flat prices to 2022, the same rise from 2023, the same cost per horsepower, returns
on assets in single digits through the span. "you can have only two competitors and they’re still terrible businesses,
they beat each other’s brains out" (**[M2013-052]**); the question is "whether it would be a game where four or five
people were slugging it out without making as much money as they could if one company dominated" (**[M2018-088]**).
In this field every improvement one fleet makes, "the improvement you get one day, your competitor gets the next day"
(**[M2004-053]**): telematics, large units and electric drive are offered by all three.

**The case for the castle, stated as strongly as I can.** Compression is essential and must run; "being a low-cost
producer of something that’s essential to people, it’s going to be a very good business usually" (**[M2004-091]**), but
the condition is the low-cost position, which the cost row shows Archrock does not hold. Industries can change for the
better: "the railroads were a terrible business for decades and decades and decades and then they got good"
(**[M2017-026]**); "We were slow to recognize the change, but better late than never." (**[L2022-020]**). The
consolidation of 2024 and 2025 (Kodiak with CSI Compressco, Archrock with TOPS and NGCS) and three years of discipline
could be such a change. Against it stands the filer's own sentence, written in February 2026 after the consolidation,
that barriers to entry are low and that rivals and customers can build fleets; the railroads became good when a new
railroad could not be built (**[M2013-054]**), and a new compressor fleet can be.

**Why OUT and not TOO HARD.** A tenuous moat whose value cannot be judged goes to TOO HARD (**[M2000-019]**: "when we see
a moat that’s tenuous in any way — getting back to your question — it’s just too risky"); a castle shown open on the
evidence closes OUT (**[M2011-015]**). This is the second case: the evidence is a full cycle of filed per-horsepower
economics, the filer's and both competitors' own statements of low barriers, an entrant that reached equal scale, and
cost parity among the three. The insiders have written it down; it is not a forecast they would refuse to make. The
lists of what Q2 rules OUT name it: industries "that are just never going to have barriers to entry" (**[M2012-106]**),
the customer who buys on price and availability (**[L2004-003]**, **[M2017-009]**), and the commodity business without
the low-cost position (**[M1997-010]**, **[M2001-013]**). The current high price per horsepower does not reopen it:
"What you can’t do is turn any investment into a good deal by paying little" (**[M2019-015]**), and the rows' boxes are
"in, out, and too hard" (**[M2006-013]**).

**VERDICT: OUT.** The castle is open on the evidence: low barriers to entry by the filer's own statement, a new entrant
at equal scale within twelve years, cost per horsepower at parity with the two large rivals, prices that did not rise in
dollars from 2013 to 2022 and rose only when the whole industry's fleet was full, and pre-tax returns on capital of about
7% over 2016 to 2025 (**[M1995-038]**, **[L2007-004]**, **[M2011-015]**, **[M2012-106]**, **[M2005-020]**, **[L2004-007]**,
**[M2009-059]**). The file closes here.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed OUT). The facts gathered are in Step 0's table: over 2016 to 2025 the business spent on fleet
capital about 89% of its cash earnings after stock pay, plus $1.37B of cash acquisitions.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. **The balance sheets were read in Step 0, before the income account**, as the rows ask: "balance
sheets over an 8 or 10 year period before I even look at the income account" (**[M2025-032]**). Filed figures, US$M,
year end (FY2017, FY2018, FY2020, FY2022, FY2024 and FY2025 10-Ks; 2016 from the FY2018 selected data):

| Year end | Total assets | PP&E net | Goodwill | Intangibles | Cash | Receivables | Inventory | Long-term debt | Total equity | Accumulated deficit | Deferred tax liab. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 2,414.8 | 2,079.1 | 0 | 86.7 | 3.1 | 111.7 | 93.8 | 1,441.7 | 684.9 | n/r | n/r |
| 2017 | 2,408.0 | 2,076.9 | 0 | 68.9 | 10.5 | 113.4 | 90.7 | 1,417.1 | 735.6 | -2,241.2 | n/r |
| 2018 | 2,552.5 | 2,171.0 | 0 | 52.4 | 5.6 | 148 | 76.3 | 1,529.5 | 841.6 | -2,263.7 | n/r |
| 2019 | 3,110.0 | 2,559.4 | 100.6 | 77.5 | 3.7 | 144.9 | 74.5 | 1,842.5 | 1,086.0 | -2,244.9 | 1.3 |
| 2020 | 2,779.7 | 2,389.7 | 0 | 61.5 | 1.1 | 104.4 | 63.7 | 1,688.9 | 935.6 | -2,402.0 | 0.7 |
| 2021 | 2,590.0 | 2,226.5 | 0 | 47.9 | 1.6 | 105 | 72.9 | 1,530.8 | 891.4 | -2,463.1 | 1.1 |
| 2022 | 2,598.8 | 2,199.3 | 0 | 37.1 | 1.6 | n/r | 84.6 | 1,548.3 | 860.7 | -2,509.1 | 0.9 |
| 2023 | 2,656.0 | 2,302.0 | 0 | 30.2 | 1.3 | n/r | 81.8 | 1,584.9 | 871.0 | -2,499.9 | 4.9 |
| 2024 | 3,824.2 | 3,323.8 | 52.2 | 98.3 | 4.4 | 132.5 | 89.7 | 2,198.4 | 1,323.5 | -2,438.1 | 62.5 |
| 2025 | 4,349.3 | 3,658.1 | 125.2 | 143.9 | 1.6 | 142.3 | 109.7 | 2,410.9 | 1,491.5 | -2,257.4 | 198.3 |

(n/r: not read in the filed statements this session; 2018 and 2021 receivables are the tool's XBRL transcription.)

What the figures say: (a) equity grew only by issuing shares; the accumulated deficit, inherited from the Exterran
years, did not shrink from 2017 to 2025, because dividends ($753.0M paid 2018 to 2025) took more than the net income
($722.0M). (b) Debt never fell below $1.4B and rose to $2.4B with the 2024 and 2025 acquisitions; coverage measured as
"pre-tax earnings/interest, not EBITDA/interest" (**[L2012-002]**) was 0.5x in 2017, 0.2x in 2020, 1.4x in 2021 and 3.6x
in the peak year 2025. (c) Cash is kept near zero every year; liquidity is the $1.5B revolver secured on receivables,
inventory and compressors, maturing 2028. (d) Goodwill bought with Elite in 2019 was gone the next year; new goodwill
and intangibles of $269M came with TOPS and NGCS. (e) Receivables and inventory track revenue without a build-up.
(f) Deferred tax liabilities went from under $5M to $198M in two years: the NOL shelter is being consumed, so cash taxes
will rise toward the book provision. What they cannot say: whether the fleet's book value is what it would cost to
replace. What the management would like them to say: the filer leads with "adjusted gross margin", and the proxy pays on
Adjusted EBITDA, the figure the rows call "utter nonsense" (**[M1998-086]**); depreciation is "almost always true costs"
(**[L2015-004]**), and here the filer's maintenance capex ($110.7M in 2025) is well under depreciation ($242.3M of
depreciation within $256.8M of D&A), while the fleet retires and sells units every year. These are recorded as weight,
not as a verdict.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. (Facts noted only: chief executive D. Bradley Childers, director since April 2013, 2025 total pay
$9,037,610 per the proxy; a new CFO from mid-2026 and the chief accounting officer retiring in December 2026.)

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. (Facts noted only: buybacks since April 2023 total 4,632,263 shares at an average $20.91 (10-Q Q2 2026);
acquisitions paid partly in stock in 2019, 2024 and 2025; the dividend is $0.23 a quarter from July 2026.)

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a clearance. The owner asked for the range, the fair price and the cheap price; they follow under the
required heading.

**COMPUTATION — NOT A CLEARANCE** (the file closed OUT at Q2; nothing here is an entry price or a reason to buy).

- **Method, the v5 CONVENTION** (Part VI and Q7, "The range, not the point"): owner cash after every real cost, averaged
  over 2021 to 2025, deducting all capital spending; carried for ten years at the shown growth, capped by the growth
  arithmetic, then at zero nominal growth; discounted at the 30-year Treasury, 5.63% (**[L2000-021]**, **[M1996-025]**:
  "use the government bond rate"); the two ends are the no-growth and shown-growth cases (**[L2000-024]**: "working with
  a range of possibilities is the better approach").
- **CONVENTION of this run, confessed:** the central cash input is owner cash after all capital spending **net of the
  proceeds of compressor sales** ($109.2M a year), because the fleet sells culled units every year as part of its
  capital cycle; the gross figure ($47.0M) is shown beside it. Cash paid for acquisitions is not deducted, because the
  base years contain only part of the streams bought (TOPS from 30 September 2024, NGCS from 1 May 2025); if it were,
  the five-year average would be about -$123M a year and no range could be built.
- **Shown growth:** the central series runs from $157.8M (2021) to $221.5M (2025), 8.8% a year at the endpoints, with a
  negative year between; the endpoints are suspect ("a base year in which earnings were poor can produce a
  breathtaking, but meaningless, growth rate", **[L2005-003]**) and 8.8% exceeds the 5.63% discount rate, so it is capped
  at 5.6% ("when the compound rate becomes higher than the discount rate, you get into infinite numbers",
  **[M1997-095]**; **[M1999-067]**).
- **VALUE RANGE (central): $11.06 to $17.24 a share** against a price of $29.97. Width 1.56 to 1, so the range is not
  TOO HARD by the three-to-one rule. The price is 1.74 times the top.
- Beside it, on the same method: all capex gross $4.76 to $7.42; the depreciation variant (OCF less stock pay less D&A,
  **[M1998-127]**) $15.67 to $24.43; the filer's maintenance capex only $26.55 to $41.40. My maintenance judgment
  (**[M2000-144]**: "the shareholders are entitled to my best guess"): true maintenance is nearer depreciation than the
  filer's maintenance line, since the filer's figure covers overhauls only and the fleet retires 38,000 to 66,000
  horsepower a year and sells more (**[L2000-035]**: "Every year we spend amounts equal to our depreciation charge simply
  to stay in the same economic place"; **[L1999-024]**). The maintenance-only variant is the one case that brackets the
  price, and it is the one the filings least support. A normal cash tax charge (the 2021 to 2025 average deferred
  provision, $43.7M a year) would lower the central range to $6.63 to $10.34.
- **FAIR PRICE: $8.65 a share.** Rule: the price at which owner cash per share ($0.623, central) plus growth at the
  midpoint of the two ends (2.8%) returns 10% pre-tax, the floor CONVENTION ("we don’t want to buy equities where our
  real expectancy is below 10 percent", **[M2003-149]**; "a very high probability of at least 10% pre-tax returns",
  **[L2002-020]**). Because cash taxes are nearly nil under the NOL shelter, the central owner cash is treated as pre-tax;
  the after-tax equivalent of 10% at the filer's 2025 effective rate of 24% is 7.6%. The fair price falls below the
  bottom of the range because the floor (10%) is above the bond (5.63%).
- **CHEAP PRICE: $6.23 a share.** Rule: the price at which the no-growth owner cash alone yields 10% pre-tax, needing no
  growth at all; it sits 44% below the bottom of the range, the "big discount from that present value calculated using
  the risk-free interest rate" (**[M1997-126]**) that lets the case "scream at you" (**[M2009-005]**).
- At $29.97 the central owner cash yields 2.1%; the owner would need 7.9% growth forever, from a fleet whose price per
  horsepower did not rise for nine years, to reach the floor.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED. (Computation only: a 2.1% owner-cash yield against a 5.63% Treasury.)

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. (Facts recorded at Q4: $2.35B of debt at June 2026, no cash, revolver to 2028, pre-tax coverage below 1x
in 2017 and 2020.)

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED. The draft would have the buyer do nothing.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED; not asked by the operator.

---
## THE BOX
**OUT at Q2.** The castle is open on the evidence: the filer itself says barriers to entry are low, Kodiak reached equal
scale from a 2011 start, cost per horsepower is at parity with the two large rivals, the price per horsepower did not rise
in dollars from 2013 to 2022, and pre-tax returns on capital averaged about 7% over 2016 to 2025. For the owner, as
COMPUTATION only: value range $11.06 to $17.24, fair price $8.65, cheap price $6.23, against $29.97.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template was copied before the first EDGAR request).
- [ ] Written question by question; committed after each (write-early). **Not done:** the research was gathered first
      and the file written after it, and nothing was committed, because this session's instruction forbids commits.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every filing fact has its accession;
      numbers are from filings or labelled COMPUTATION or CONVENTION.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); stock pay as filed, not the tool's;
      the sovereign from the issuing authority; the aggregator quote flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (eleven items, before the verdict).
- [x] No row dated after the anchor is cited in a point-in-time run (not a point-in-time run; anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its stock-pay figures were found wrong and
      replaced.
- [x] `python tools/check_framework.py` PASS before the commit (run; there is no commit in this session).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) The Q7 range CONVENTION says the cash input "deducts all capital spending" but does not say whether cash
paid for acquisitions is capital spending, nor whether recurring sales of fleet assets offset it; for a roll-up of
rental fleets the answer moves the five-year average from about +$109M to about -$123M a year, so the run had to confess
its own choice. (2) The convention measures growth "on the aggregate owner cash", which fails when the series has
negative years (2022, and 2023 gross); the endpoint rate was used and capped, but the rule should say what to do when the
series changes sign. (3) The convention treats the floor as "about ten percent pre-tax", yet in a company sheltered by
NOLs the owner cash is neither pre-tax nor after a normal tax; the run treated it as pre-tax and showed the tax-normalized
case beside it. (4) Q2's routing between OUT and TOO HARD turns on whether a castle is "shown open" or "cannot be
judged"; a commodity industry that has just consolidated and raised prices sits on that line, and no row or convention
says how many years of a changed price behaviour (**[M2005-020]**) would count as a change for the better
(**[M2017-026]**, **[L2022-020]**) rather than a cycle. The run decided it on the filer's own present-tense statement
of low barriers, which is a choice and is recorded as one.
