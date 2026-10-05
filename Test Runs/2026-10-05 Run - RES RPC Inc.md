# Company Run: RPC, Inc. (NYSE: RES), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template before any fetch.**

**POSITION NOTE, declared before any verdict:** not known to the analyst. The run was dispatched blind: `PORTFOLIO.md`,
any holding review, the resume-state file, the run queue, the reading list and any other run file on this company were
not opened. **Contamination declared:** the session's commit subjects name the boxes of other 2026-10-05 runs (HUBB,
ATKR, ETN and others, none an oilfield-services name); the working folder listing showed other run files by name only.
Nothing about RES was seen. The analyst's own incentive is named under operator rule 9: none known, beyond the builder's
wish to see the framework work.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $6.17 (2026-10-05; aggregator live quote via `tools/run.py`, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: 221,657,012 common, par $0.10, one class (10-Q for the period
  ended 2026-06-30, filed 2026-07-30, accession `0001104659-26-088774`; `python Screens/cover_shares.py RES`). The
  charter authorizes 1,000,000 preferred, none issued (same 10-Q, balance sheet).
- **Market cap:** about $1,368M ($6.17 x 221.657M).
- **Sovereign for the earnings currency (USD):** 5.63%, 30-year par yield, US Treasury daily par yield curve, dated
  2026-10-02 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-27, accession `0001104659-26-021480` (Items 1, 1A, 2, 5, 7, 7A; notes 2, 9, 18, 19, 21).
  - 10-Q Q2 2026, filed 2026-07-30, accession `0001104659-26-088774` (MD&A, balance sheet, cash flow, repurchase note).
  - DEF 14A for the 2026 meeting, filed 2026-03-18, accession `0001104659-26-030766` (pay, ownership, related parties).
  - 8-Ks: Pintail closing, 2025-04-07, `0001558370-25-004495`; credit agreement amended, 2026-07-07,
    `0001104659-26-081292`; CEO retirement notice, 2026-06-23, `0001654954-26-006153`; officer salary increases,
    2026-09-08, `0001104659-26-105928`; director Nix not standing, 2026-01-28, `0001104659-26-007185`; Q2 results,
    2026-07-30, `0001104659-26-088439`.
  - Older 10-Ks for the cycles: FY2016 `0001571049-17-001715`, FY2019 `0001104659-20-027017`, FY2020
    `0001104659-21-029211` (plus FY2011, FY2014, FY2022 fetched to the working folder for the series).
- **One figure cross-checked against the filed statement:** 2025 net cash from operations, $201,331K in the FY2025
  10-K's MD&A table, equals the XBRL/`run.py` figure of $201M; stockholders' equity at 2025-12-31, $1,099,171K on the
  filed balance sheet (10-Q comparative column), equals the `run.py` table's $1,099M.
- **A tagging error found:** XBRL `Revenues` for FY2015 reads 41,919 (thousands), which is a pronouncement-effect line,
  not revenue; the filed revenue is $1,263.8M (`SalesRevenueNet`, FY2015 10-K). The corrected figure is used throughout.
- `python tools/run.py RES`, arithmetic lines only (Part VII). Owner cash (OCF less stock pay less all capex), from the
  filed cash-flow lines, $M:

| year | revenue | operating income | OCF | stock pay | capex | D&A | OCF less SBC less capex | OCF less SBC less D&A |
|---|---|---|---|---|---|---|---|---|
| 2012 | 1,945.0 | 442 | 559.9 | 8 | 329 | 215 | 223 | 337 |
| 2013 | 1,861.5 | 277 | 365.6 | 8 | 202 | 213 | 156 | 145 |
| 2014 | 2,337.4 | 401 | 322.8 | 9 | 372 | 231 | -58 | 83 |
| 2015 | 1,263.8 | -156 | 473.8 | 10 | 167 | 271 | 297 | 193 |
| 2016 | 729.0 | -239 | 101.7 | 10 | 34 | 217 | 58 | -125 |
| 2017 | 1,595.2 | 226 | 133.7 | 11 | 118 | 164 | 5 | -41 |
| 2018 | 1,721.0 | 210 | 389.0 | 9 | 243 | 163 | 137 | 217 |
| 2019 | 1,222.4 | -114 | 209.1 | 9 | 251 | 170 | -51 | 30 |
| 2020 | 598.3 | -310 | 78.0 | 9 | 65 | 96 | 4 | -27 |
| 2021 | 864.9 | 16 | 47.7 | 7 | 68 | 73 | -27 | -32 |
| 2022 | 1,601.8 | 288 | 201.3 | 6 | 140 | 83 | 55 | 112 |
| 2023 | 1,617.5 | 245 | 394.8 | 8 | 181 | 108 | 206 | 279 |
| 2024 | 1,415.0 | 98 | 349.4 | 9 | 220 | 133 | 120 | 207 |
| 2025 | 1,626.6 | 45 | 201.3 | 12 | 148 | 161 | 41 | 28 |

  Five-year average (2021-2025): owner cash $79M on the capex basis, $119M on the depreciation basis. Ten-year average
  (2016-2025): $55M and $65M. Stock pay is deducted (complete in the cash-flow statement). Series from the companies'
  10-K XBRL (accessions in the working folder, `xbrl_table.txt`), transcription only; the 2025 figures were read in
  the filed statements.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is **no macro forecast enters**: the whole industry's year is set by the oil price,
and the run must not decide on a view of it. "macro conclusions are — just never enter into the discussion" **[M2000-094]**;
what counts is "the average profitability of the business over time and how strong its competitive mode is" **[M2015-016]**.
So the run asks what the business earns across the cycles on the record, never what crude will do. Second, **a share is a
business** **[M1997-109]**: the test is whether one would own this if the market closed, which turns the question to the
castle. Third, **the analyst's habits**: look for "what’s wrong in things" **[M2025-013]** and test the hypothesis "to
possibly reject your original hypothesis" **[M1998-144]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. (Item 1, FY2025 10-K) "cost efficiency savings have been disproportionately realized by the E&Ps rather than oilfield
   service companies"; the filer believes "there is a general oversupply of OFS capacity, particularly in pressure pumping,
   which has created a high level of price competition". Against any castle.
2. (Item 1) The filer's own list of "principal competitive factors" starts with "price"; Permian operations "have faced
   increased competition from assets shifting into the region from gassy basins".
3. (FY2016 10-K, `0001571049-17-001715`) customers "have thus far been very reluctant to accept increases in pricing for
   their services in order to compensate us for our increased costs". Against pricing power.
4. (Series above) Through 2016-2025, net income averaged about 5.0% a year on average equity, with no debt; 2014 equity
   $1,078M, 2025 equity $1,099M, while about $455M went out in dividends and buybacks 2015-2025. Against the return.
5. (Item 1) RPC "has not invested in electric fleets"; only 6 of its 10 frac fleets are Tier 4 (3 dual-fuel, 3 diesel),
   while the filer reports "Trend toward client preference for lower emissions equipment". Against a low-cost claim.
6. (Item 1, segment table) Pressure pumping revenue fell from $771.5M (2023) to $587.1M (2024) to $485.0M (2025).
   Against share.
7. (10-Q Q2 2026) Oil averaged 49.1% higher than a year earlier, yet quarterly operating income was $14.8M against
   $15.5M; management still calls the market "over-supplied". The upcycle in the commodity did not reach the servicer.
8. (DEF 14A 2026) The controlling family's LOR, Inc. obtained registration rights, and a shelf registers 127,235,202
   shares for resale, "a majority of the Company securities held by the Selling Stockholders"; the family's other
   company, Marine Products, agreed on 2026-02-05 to merge into MasterCraft. The insiders are positioned to sell.
9. (8-K 2026-06-23) The CEO gave notice of retirement; no successor named.
10. *For* the business, written down as fairly: zero bank debt through every bust on record (2015-16, 2019-20); dividends
   held or resumed; Downhole Tools (Thru Tubing Solutions, 24.2% of 2025 revenue) is described by the filer as
   "differentiated" with proprietary products; M2011-102 says lumpy earnings do not matter "as long as it’s a good
   business" **[M2011-102]**.

The index fork **[M2008-055]** is the operator's, not the company's, and is not answered here.

## THE STANDING RULE
A cash purchase of a listed stock, unlevered and sized at the buyer's choice, puts no one at risk of ruin; the rule binds
the buyer's financing and sizing, "Never risk permanent loss of capital." **[L2023-005]**, and nothing in this run
proposes borrowing or a position the buyer could be forced to sell **[L2014-024]**. Clear.

---
## Q1: CAN I UNDERSTAND IT? STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years" **[M2012-065]**; the chemistry or engineering need not be understood if "I understand the economic
dynamics of the industry" **[M2011-014]**.

**Key variables** **[M1998-044]**: (1) US onshore completion activity, which follows the oil and gas prices; (2) the price
per job, which follows the supply of fleets and crews against that activity; (3) RPC's cost and share against the other
pumpers. The first is a macro variable and is not forecast **[M2000-094]**. The second and third are economic dynamics of
an industry, and the filings give them plainly: high fixed cost, oversupplied capacity, price as the first competitive
factor, efficiency gains captured by the customer (contrary evidence 1, 2), across three full cycles on the record
(2012-2025).

**Is the ten-year picture knowable?** Not the year-by-year earnings, which ride the oil price. But the rows ask for the
average over time and the strength of the position **[M2015-016]**, and for cyclical businesses the order of the good and
bad years does not matter: "I don’t know the order in which they’re going to appear" **[M2011-101]**. The competitive
position in ten years is foreseeable in its character: a servicer in an industry the filer itself calls oversupplied,
with the customer consolidating (Item 1, "a more concentrated pool of larger, more powerful E&P companies"). That is a
fix on the economics, and an unflattering one.

**The other reading, stated and rejected.** One could close here TOO HARD (NATURE) because the earnings depend on the oil
price, which insiders "would not want to put down on paper" **[M2000-105]**. That reading is rejected because the
decision does not turn on the oil price: the castle question below is answered from the record across a boom
(2012-2014, 2022-2023), two busts (2015-2016, 2019-2021) and the 2026 oil spike (contrary evidence 7), and the answer
holds in each. This is not fast-moving technology **[M1998-008]**; the efficiency gains are a known, documented force.
Doubt check **[M2002-092]**: I do not doubt that I understand how this industry's money is made and kept; I doubt that
there is much of it, which is Q2's question, not Q1's.

- **VERDICT: IN.** The economic dynamics are understood from the filings **[M2011-014]**, **[M2012-065]**; the oil price
  is not needed for the decision **[M2015-016]**, **[M2000-094]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing" **[M1995-038]**; a moat
"protects excellent returns on invested capital" **[L2007-004]**.

**What the business sells.** Technical Services (94.4% of 2025 revenue): pressure pumping 29.8%, downhole tools 24.2%,
wireline 19.4% (Pintail, bought 2025-04-01), coiled tubing 9.3%, cementing 6.4%, plus snubbing, nitrogen, well control.
Support Services (5.6%): rental tools, pipe inspection and storage, a well control school (10-K FY2025 Item 1). One
private E&P customer was about 15% of 2025 revenue and 13% of 2024.

**The castle tests, each with its filing fact.**
1. **Is it a commodity?** The rows define one by the customer's indifference and the rival who sets the price: "whatever
   he charged for gas was my price" **[M2012-109]**; "he determined our profit, because we looked at his price every day"
   **[M2023-079]**. The filer: price is the first named competitive factor; capacity is oversupplied; "pricing
   competition to keep assets utilized is common" (Item 1, Competition). The efficiency gains go to the customer, which
   is the textile parade: "the other guy was doing the same thing" **[M2004-054]**; "the improvement you get one day, your
   competitor gets the next day" **[M2004-053]**. The filer's own words on pump hours, "assets being “burned” faster and
   requiring quicker capital investment cycles" (Item 1), are the self-neutralizing machinery of that row. On the
   evidence, pressure pumping, wireline, coiled tubing and cementing (about 65% of 2025 revenue together) sell a
   commodity-like service.
2. **The one exception: is RPC the low-cost operator?** "commodity businesses have risk unless you’re the low-cost
   producer" **[M1997-010]**; "being the low-cost producer is all-important" **[L2000-017]**; the cost is measured against
   the competitor **[M2001-013]**. Evidence against RPC holding that title: (a) through-cycle operating margin 2016-2025
   of 3.6% against Liberty's 7.1% and Halliburton's 4.4% (competitor row below); (b) RPC owns no electric fleets, the
   lower fuel-cost technology the filer says customers prefer, and only 6 of 10 fleets are Tier 4 (contrary evidence 5);
   (c) its pressure pumping revenue fell 37% from 2023 to 2025 while Liberty, the largest pure-play pumper in the
   row, saw total revenue fall 16%; a low-cost operator welcomes the hard market **[L2004-007]**, and RPC's share shrank in it. No filing fact found
   that shows RPC's cost per pump-hour below its rivals'. The exception is not shown; the evidence runs the other way.
3. **Pricing power and the agony before a rise** **[M2005-020]**. In 2017, after the worst bust on record, customers were
   "very reluctant to accept increases in pricing for their services in order to compensate us for our increased costs"
   (FY2016 10-K). In Q2 2026, with oil up 49.1%, operating income fell year on year and pricing "slight improvements"
   only (10-Q). That is the prayer session, stated by the filer.
4. **Would the customer still choose it over the low bid?** **[M2017-009]**. The filer describes its spot customers as
   "typically highly price-sensitive", and its large customers as consolidating buyers with "scale" who seek partners with
   "newer technology options" (Item 1). Neither group is buying anything but the low bid or the newest fleet.
5. **The money test** **[M2011-015]**. A well-funded entrant can buy frac fleets, wireline units and coiled tubing units
   from the same "limited number of manufacturers" RPC buys from (Item 1A); Permian rivals moved fleets in from gas basins
   in 2025. "there are some industries that are just never going to have barriers to entry" **[M2012-106]**. Answer: yes,
   the castle can be taken with money, and is being entered now.
6. **Unit volume and share of mind.** No brand: no instance of a customer asking for RPC by name was found in the
   filings; the one differentiated claim is Thru Tubing Solutions' proprietary tools, whose patents the filer calls
   "important, but are not indispensable" (Item 1, Intellectual Property).
7. **Widening or narrowing** **[M2000-075]**. Narrowing on the filer's own account: E&P consolidation "has resulted in the
   loss of some customers" (MD&A Overview, FY2025); pressure pumping revenue down two years running; the lower-emission
   trend runs ahead of RPC's fleet.
8. **What could destroy it** **[M2000-014]**: the continuing efficiency gains that the filer says keep adding pump-hour
   capacity, a concentrated customer base, and a 15% customer. These are present now, not in a forecast.
9. **Is the return protected?** The castle protects "excellent returns on invested capital" **[L2007-004]**. RPC's
   record: about 8.1% a year on average equity 2012-2025 including the 2012-2014 boom, 5.0% for 2016-2025, losses in 4 of
   14 years, and 2014 equity of $1,078M against 2025 equity of $1,099M. The boom years read as "a cyclical peak in earnings"
   **[L1994-009]**, not a protected return.

**The part that could be different.** Downhole Tools (TTS), 24.2% of 2025 revenue, is the filer's "differentiated
service line" with proprietary motors and the "UnPlug" product. Its margins are not reported separately (the segment
note reports only Technical and Support Services, both read as a whole by the CODM), so no castle can be shown there
from the filings. A part that may have a moat cannot rescue a whole whose larger part is shown open: the business bought
is the whole.

**The competitor row** (same metrics, each company's own 10-K XBRL; the latest accession named; 2016-2025, a span from
one trough through two peaks to now):

| company | 2016-2025 revenue, $M | operating margin, cumulative | (OCF less capex) / revenue | net income / average equity, per year | years with operating loss | latest 10-K accession |
|---|---|---|---|---|---|---|
| RPC (RES) | 12,992 | 3.6% | 4.9% | 5.0% | 3 of 10 | 0001104659-26-021480 |
| ProPetro (PUMP) | 12,463 | 1.4% | 0.4% | 1.1% | 5 of 10 | 0001680247-26-000028 |
| Liberty Energy (LBRT) | 26,665 | 7.1% | 1.9% | 10.6% (distorted: 2017 pre-IPO equity tag reads zero) | 3 of 10 | 0001694028-26-000006 |
| Patterson-UTI (PTEN) | 28,550 | -12.2% (impairments; drilling plus pumping) | 6.3% | -10.8% | 8 of 10 | 0000889900-26-000013 |
| Halliburton (HAL) | 201,093 | 4.4% | 5.1% | 0.9% | 3 of 10 | 0000045012-26-000015 |

Reading the row: the whole field earns low single-digit margins through the cycle; the field's best pure pumper
(Liberty) earns about twice RPC's operating margin; RPC's better cash conversion than Liberty comes from spending less on
its fleet (cumulative capex $1,468M against D&A $1,368M over the decade), not from a higher return. RPC's distinction is
its balance sheet, not its castle. "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**;
here there are dozens, which the filer names. Ask the competitors **[M1999-130]**: not done (no interviews; the scuttlebutt
is the filings only).

**Why the box is OUT and not TOO HARD.** TOO HARD is for the tenuous moat of which the rows say "We don’t know how to valuate that" **[M2000-019]**.
This one is valued easily enough, and judged: it is a commodity service with no low-cost title, no pricing power, a falling share in its largest line and
returns below the long bond across a decade, each a filing fact. "If the answer had been yes, we wouldn’t have done it."
**[M2011-015]**; the high-cost or mid-cost producer in a commodity field is on the list of what Q2 rules OUT **[L1994-035]**,
**[M1997-010]**, and so is the business whose price a rival sets, "whatever he charged for gas was my price" **[M2012-109]**,
**[M2023-079]**. Price does not
reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

- **VERDICT: OUT.** The castle is shown open on the evidence **[M2011-015]**, **[M1997-010]**, **[M2012-109]**,
  **[M2004-054]**; the cyclical-business door the rows leave open, "as long as it’s a good business" **[M2011-102]**, is
  closed by the same evidence. The run closes here.

---
**The run is closed at Q2. Everything below is COMPUTATION, NOT A CLEARANCE (operator rule 3), written at the owner's
request for the record. It carries no entry language.**

## Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED.
COMPUTATION, NOT A CLEARANCE, recorded because it was read: capex 2016-2025 totalled $1,468M against D&A of $1,368M;
the filer says pump hours of 20 to 22 a day leave assets "burned" faster and require "quicker capital investment cycles"
(Item 1). Maintenance at or above depreciation; the 2026 capex guide is $150M to $180M against 2025 D&A of $161M. No
weighing is drawn because Q3 is not reached.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED.
COMPUTATION, NOT A CLEARANCE: the balance sheets 2016 to 2025, read before the income account (from `run.py`'s table of
the filed year-end statements; 2025 checked against the filing), $M:

| year-end | equity | cash | receivables | receivables / revenue | inventory | goodwill | intangibles | debt | gross PP&E | net PP&E |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 807 | 132 | 169 | 23% | 108 | 32 | 0 | 0 | 2,093 | 498 |
| 2017 | 912 | 91 | 378 | 24% | 115 | 32 | 0 | 0 | 2,103 | 444 |
| 2018 | 950 | 116 | 324 | 19% | 130 | 32 | 0 | 0 | 2,152 | 518 |
| 2019 | 830 | 50 | 243 | 20% | 101 | 32 | 0 | 0 | 1,914 | 517 |
| 2020 | 632 | 84 | 162 | 27% | 83 | 32 | 0 | 0 | 1,055 | 264 |
| 2021 | 642 | 82 | 259 | 30% | 79 | 32 | 0 | 0 | 1,018 | 254 |
| 2022 | 858 | 126 | 417 | 26% | 97 | 32 | 1 | 0 | 1,108 | 333 |
| 2023 | 1,023 | 223 | 325 | 20% | 111 | 51 | 13 | 0 | 1,246 | 435 |
| 2024 | 1,078 | 326 | 277 | 20% | 108 | 51 | 14 | 0 | 1,374 | 514 |
| 2025 | 1,099 | 210 | 328 | 20% | 119 | 83 | 97 | 50 (seller note) | 1,452 | 532 |
| 2026-06-30 | 1,109 | 179 | 379 | about 21% of annualized Q2 | 126 | 81 | 94 | 30 | n/a | 519 |

What the figures say: equity fell from $1,078M (2014) to $632M (2020), about 41% of book lost in two busts, and has
only climbed back to where it stood in 2014; the 2020 impairment and other charges were $217.5M and 2019's $82.3M (FY2020
10-K MD&A). Gross PP&E halved in 2020 on impairment and disposals. Receivables and inventory track revenue, no build-up
found. Goodwill and intangibles appear only with Pintail (2025: $83M and $97M). Debt was zero until the Pintail seller
note. What they do not say: the margin of the differentiated Downhole Tools line, which is buried in the segment. One
further reading: inventory transferred to PP&E ($16.2M in 2025, $17.0M in 2024) is capital bought through operating cash,
already inside OCF less capex, so no second deduction is made. Management features EBITDA and "Adjusted EBITDA"; the
annual bonus metric is EBITDA less cash capex (DEF 14A). Q4 is not reached and no verdict is drawn on these.

## Q5, Q6: NOT REACHED.
COMPUTATION, NOT A CLEARANCE, facts only: CEO Ben M. Palmer's 2025 pay $3,192,075 (salary $618,000, stock $1,388,265,
bonus $1,155,660 at 187% of target, the target being EBITDA less cash capex of $35.0M, set "considering OCF achieved by
the company in the last ten years"; no bonus for 2024); salary raised to $750,000 effective 2026-05-16 while he is
retiring. Executive officers of RPC are also employees of Marine Products, and all RPC directors are Marine Products
directors (10-K note 18); Marine Products paid RPC $1.1M in 2025 for administrative services. Control group 56.6% of the
shares (Rollins family voting trusts and LOR, Inc.); NYSE controlled-company exemption elected. Buyback program with no
stated price; no open-market repurchases in 2025 or the first half of 2026 (10-Q). Pintail paid $170M cash, $25M in
shares (4,545,454 shares at about $5.50) and a $50M note; half the note and all the shares contingent on the seller's
employment. Dividends $0.04 a quarter.

## Q7: WHAT IS IT WORTH. NOT REACHED.
**COMPUTATION, NOT A CLEARANCE**, reported at the owner's request, on the CONVENTION construction of Q7 (five-year average
owner cash after every real cost; growth shown, capped; ten years then zero nominal growth; the sovereign 5.63%):
- **Owner cash input:** $79.1M (2021-2025 average, OCF less stock pay less all capex). Depreciation variant $118.9M.
  Ten-year window (2016-2025) $54.8M, depreciation variant $64.8M.
- **Growth shown:** the five-year base year (2021) is negative, so a five-year rate is meaningless ("a base year in which
  earnings were poor can produce a breathtaking, but meaningless, growth rate" **[L2005-003]**). Measured instead from the
  2012-2014 average ($107M) to the 2023-2025 average ($122M): about 1.2% a year nominal, part of which was bought with
  the Pintail acquisition.
- **How the cycle was treated:** the five-year window holds one bust year (2021) and two strong years (2023-2024) with
  the 2022 recovery; it is closer to mid-cycle than either the boom or the trough, but it excludes the 2015-2016 and
  2019-2020 losses. The ten-year window, which holds two full busts, is shown beside it as the cycle's honest test.
- **Value range:** $6.34 (no growth) to $6.97 (1.2% for ten years) a share, capex basis, five-year window, against $6.17.
  Depreciation variant $9.53 to $10.48. Ten-year window $4.39 to $4.83 (depreciation variant $5.19 to $5.71). Net cash
  (cash $179M less notes $30M at 2026-06-30) is not added, since its interest is already in OCF and the filer says it is
  held for the downturns.
- **Pre-tax and after-tax:** OCF is after cash tax. To set it against the floor of about ten percent pre-tax (CONVENTION;
  "at least 10% pre-tax returns" **[L2002-020]**), I add back the average income tax provision of the same window
  ($37.2M for 2021-2025, $8.1M for 2016-2025) rather than gross up by a rate, because the effective rate swung from 18.9%
  (2024) to 43.3% (2025). Pre-tax owner cash: $116.3M (five-year), $62.9M (ten-year). Expected pre-tax return at $6.17:
  8.5% (five-year, no growth) to 9.7% (with 1.2% growth); 4.6% to 5.8% on the ten-year window.
- **FAIR-PRICE BAND:** empty inside the range. The floor of about ten percent pre-tax is reached at $5.25 (no growth) to
  $5.96 (1.2% growth) on the five-year window, below the bottom of the range ($6.34), and at $2.84 to $3.22 on the ten-year
  window.
- **CHEAP PRICE:** about $2.80. Rule used (mine, confessed): the price at which the ten-year window, busts included,
  clears the floor ($2.84 to $3.22) and the five-year window returns about double it ($2.62 to $2.79). Below about $2.80 the
  arithmetic would need no pencil **[M1996-084]**; the price is $6.17.
- The convention range is about 1.1 to 1, so Q7, had it been reached, would have closed OUT: the price sits just below the
  bottom of a narrow range, and it does not "scream at you" **[M2009-005]**, and the expected return is below the floor **[M2003-149]**.
  This is arithmetic on a business Q2 has already put OUT.

## Q8, Q9, Q10, Q12: NOT REACHED.
COMPUTATION, NOT A CLEARANCE, facts only for Q9: no bank borrowings; $100M revolver extended to 2031-06-30 (covenants:
leverage 2.50x, debt service 2.00x, or tangible net worth $400M); Pintail seller note $30M outstanding, maturing
2028-04-01; operating and finance lease commitments about $27.4M; self-insurance with an actuarial range of $19.1M to
$26.7M; one customer at 15% of revenue.

---
## THE BOX
**OUT, at Q2.** A commodity oilfield service with no shown low-cost position, no pricing power in the filer's own words,
a shrinking share in its largest line and about 5% a year on equity across 2016-2025; the debt-free balance sheet is a
survival trait, not a castle. COMPUTATION only, not a clearance: value range $6.34 to $6.97 (capex basis, five-year
window) against $6.17; fair-price band empty inside the range (floor reached at $5.25 to $5.96); cheap about $2.80.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. **Not committed**: the dispatcher
      instructed no commits; the file stands uncommitted for the operator.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, and every quoted fragment beside an id
      is in that row); every filing fact has its accession; no number without a row, a filing or a CONVENTION label.
- [x] The order was kept; Q2 failed and closed the run; Q3 to Q12 are NOT REACHED and their contents are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay and all capex deducted; depreciation variant shown), never a
      net-income proxy (operator rule 5); the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]**, including the evidence for the business.
- [x] No row dated after the anchor: this is a live run dated 2026-10-05, not a point-in-time test.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 text was not read as rules (Part VII).
- [x] `python tools/check_framework.py` PASS before handing back (see the working folder).
- Defects confessed: the competitor row is XBRL transcription, not read line by line in each competitor's filed
  statement; Liberty's equity-based figure is distorted by a pre-IPO tag; Patterson-UTI mixes drilling with pumping;
  Halliburton is integrated and global. No interviews with customers, competitors or employees were made; the
  scuttlebutt is the filings. Downhole Tools' own margin could not be found in any filing read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) The dispatch named a Part VI convention for "a boom inside the window"; no such convention exists in
`Framework/THE FRAMEWORK v5.md` (a text search for "boom", "windfall" and "cycle" found none). The Q7 CONVENTION fixes a
five-year window and says nothing about a cyclical business whose five years are a recovery from a trough; I used the
rows on peak earnings and base years (**[L1994-009]**, **[L2005-003]**) and showed the ten-year window beside it. A
cyclical business needs a stated rule, or two analysts will pick windows that differ by half. (2) The growth convention
fails when the base year's owner cash is negative; I measured growth between three-year averages a decade apart and
said so. (3) Q1's routing for a business whose year-to-year earnings ride a macro variable is not written: test 5 (would
the insiders write it down?) seems to send it to TOO HARD (NATURE), while M2015-016 and M2011-101 say the average and the
moat are what count. I took the second reading and recorded the first; the framework should say which governs a
commodity-cycle business. (4) The owner's "cheap price" has no rule in the framework; I defined it (the floor cleared on
the window with the busts in it, and about double the floor on the five-year window) and confessed it as mine.
