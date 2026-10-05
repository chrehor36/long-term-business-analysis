# Company Run — IES Holdings, Inc. (NASDAQ: IESC) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not known to this analyst. The run was done blind at the operator's
instruction: `PORTFOLIO.md`, the holding reviews, the session-state files, the run queue, the prepped reading list and any
other run file about IESC were not opened. Whether anyone holds or wants this name is unknown to this run.

**CONTAMINATION, declared.** (1) The session context showed the repository's recent commit messages, which name today's v5
runs of PWR Quanta (TOO HARD (WORK) at Q2), LINC and UTI, and a session-state commit titled "the electrical-trades run
list (16 names, top down)"; a directory listing showed untracked run files for EME and FIX dated today. None of those
files was opened; the competitor figures below were fetched fresh from SEC XBRL. The PWR verdict was known before this
run's Q2 was written, and is named here so the reader can weigh it. (2) The user's memory index (loaded into the session)
says the v4 queue held “57 gate-clearers, nothing buyable”; it names no ticker. (3) Nothing seen named IESC.

Working folder: `Test Runs/_research 2026-10-05 IESC/` (filings as text, `owner_cash.py`, `rows.py`, peer facts).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $338.19 (2026-10-05, Yahoo chart via `tools/sources.py`; aggregator, live quote only, flagged per operator
  rule 5). The quote is on the post-split basis (see shares).
- **Shares by class** from the latest filing's cover: 19,924,356 common, as of 2026-07-27 (10-Q for the quarter to
  2026-06-30, filed 2026-07-31, accession `0001048268-26-000130`; `python Screens/cover_shares.py IESC`). One class. **A
  two-for-one split was distributed after the close of 2026-08-21** (8-K filed 2026-07-31, accession
  `0001048268-26-000131`, Item 8.01; 10-Q Note 15; Yahoo split event dated 2026-08-24). Shares on today's basis:
  19,924,356 × 2 = **39,848,712**.
- **Market cap:** $338.19 × 39.849M = **$13,476M**. *`tools/run.py` printed $6.74B because it multiplied the post-split
  quote by the pre-split cover count; see the closing section.*
- **Sovereign for the earnings currency (USD):** **5.63%**, US Treasury daily par yield curve, 30-year, dated 10/02/2026
  (`tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY to 2025-09-30, filed 2025-11-21, accession `0001048268-25-000174`
  (Items 1, 1A, 5, 7, 7A, the cash-flow statement, Notes 13, 15, 16); 10-Q for the quarter to 2026-06-30, accession
  `0001048268-26-000130` (balance sheet, income statements, cash-flow statement, Notes 2, 3, 6, 7, 13, 15, MD&A);
  DEF 14A filed 2026-01-07, accession `0001048268-26-000018` (related-person transactions, compensation); 8-K of
  2026-08-11 (DBM Global transaction), accession `0001493152-26-036976`; 8-K of 2026-07-31, accession
  `0001048268-26-000131`; Schedule 13D/A of Tontine filed 2026-01-09, accession `0001104659-26-002521`; for history the
  10-Ks for FY2022 (`0001048268-22-000099`), FY2020 (`0001048268-20-000033`), FY2016 (`0001193125-16-789187`) and FY2012
  (`0001193125-12-503507`), segment tables and cash-flow statements only. The FY2026 10-K (year ended 2026-09-30) is not
  yet filed.
- **One figure cross-checked against the filed statement:** FY2025 net cash from operations, $286M in `tools/run.py`
  against **$286,096K** on the filed Consolidated Statement of Cash Flows (accession `0001048268-25-000174`). Agrees.
  Also FY2025 equity, $884M (tool) against $883,955K (10-Q comparative column). Agrees.
- `python tools/run.py IESC`, arithmetic lines only. Its owner-earnings lines (OCF − SBC − capex: FY2023 $120–132M,
  FY2024 $184–192M, FY2025 $206–226M) are **not used**, for two reasons found in the filing: the company classifies its
  purchases of trading securities **inside operating cash flow** (FY2025 line “Marketable securities (62,099)”, FY2024
  (33,214); 9M FY2026 (153,889)), and the tool takes no account of distributions to noncontrolling interests or
  finance-lease principal. The recast is at Q4 below and in `owner_cash.py`. SBC is resolved: non-cash compensation
  $12.9M FY2025, $5.5M FY2024, $4.4M FY2023 (filed cash-flow statement).

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the share as a business: the question is whether this business, owned with the
market closed, would give back its cash, "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**; and the quotation, up about nineteen-fold in five years on the filer's own graph (Item 5, $100 to
$1,931.28 from 2020-09-30 to 2025-09-30), "doesn’t tell us anything. It just tells us prices." **[M2006-077]**. No macro
view enters: what matters is "the average profitability of the business over time and how strong its competitive mode
is" **[M2015-016]**, **[M2000-094]**; the data-centre building cycle is read only as evidence of that average, never as
a forecast. **Contrary evidence, written down as found** **[M1997-127]**: (a) the run began expecting a commodity
contractor; the first contrary fact was the Communications segment's description of customers who “significantly rely
upon our past performance record, technical expertise and specialized knowledge” and use IES “as a preferred provider”
(10-K FY2025, Item 1), written down at once and tested at Q2; (b) the second was Infrastructure Solutions' 34.4% gross
margin in FY2025 on custom-engineered products, also tested at Q2; (c) the third was that operating tangible capital is
small and customer-financed (Q3 computation), which cuts for the business, not against it; (d) against my own view, the
controlling holder has run the company to a high return on its capital since he became chief executive in 2020, and a
reader who credits the man over the field would weigh that heavily. Each is carried to the question it belongs to.

## THE STANDING RULE
No borrowed money, no position that a fall can call: "borrowed money has no place in the investor's tool kit"
**[L2014-005]**; "We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]**. The shares fell about 40% in FY2022 on the filer's own five-year graph (index $221.90 to $134.14) and
about 19% from 2026-08-06 to 2026-08-28 on the Yahoo series (aggregator); a buyer who could not hold through that
should not hold it. The rule binds the buyer and is not engaged by the business.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand the economic dynamics of the
  industry" and can answer "Is there ease of entry?" **[M2011-014]**.
- **What the business is** (10-K FY2025, Item 1; segment revenue FY2025 / 9M FY2026 from the 10-Q, accession
  `0001048268-26-000130`): an electrical and technology contractor and fabricator in four segments. Communications
  (cabling and network infrastructure inside data centres; 33.8% of FY2025 revenue, 38.0% of 9M FY2026); Residential
  (electrical, plumbing and HVAC for homebuilders and multi-family developers, mostly Texas and Florida; 38.7% / 29.0%;
  one Residential customer was 12.0% of consolidated revenue in FY2024 and FY2023); Infrastructure Solutions (generator
  enclosures, bus duct and power distribution equipment for data centres and industry, motor and generator repair, and
  since January 2026 steel fabrication through Gulf Island; 14.8% / 18.0%); Commercial & Industrial (electrical and
  mechanical construction, including data centres; 12.7% / 15.0%). The filer: 87.1% of FY2025 revenue on fixed or unit
  price, 12.9% time and materials; “We enter into contracts principally on the basis of competitive bids” (Item 7,
  Critical Accounting Policies).
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) bid margins against labour and material
  costs; (2) construction volume in the end markets: data-centre building (three of four segments name it as the key
  end market, 10-Q MD&A), and single- and multi-family starts; (3) the supply of skilled labour (10,283 employees,
  “the pace of growth in this business may also be slowed by the availability of labor”). The **level** of (2) ten years
  out is a forecast nobody writes down, and the filer says its markets are “highly cyclical” for Communications,
  Residential and C&I alike (Item 1, Seasonality). The **character** of (1) and (3) is readable: a bid contractor with a
  thirteen-year margin record that can be read against four filed competitors.
- **Routing.** No fast-changing technology is in the product: the trades are electricians, plumbers and fabricators, so the
  Q1 TOO HARD route for rapid change does not apply. What the rows ask at Q1 is the average over time and the strength of
  the moat **[M2015-016]**; the past statements do tell me what the future ones will look like over a cycle **[M2008-033]**,
  because the company has published a full cycle: operating losses in FY2009 to FY2012, margins of 1.5% to 5.6% from
  FY2014 to FY2022, and 6.7% to 12.6% since (XBRL from the 10-Ks, accessions in the Q2 row). The holding company is
  understood by its parts: each of the four is a contractor or job-shop fabricator whose economics are the same kind. I
  have no doubt that these businesses are inside the perimeter **[M2002-092]**; the importance of the unknowable cycle
  level is taken up at Q2, where it decides nothing if the castle is open **[M2006-076]**.
- **VERDICT: IN.** The economic dynamics of electrical contracting can be understood and the competitive position can be
  given a reasonable fix from the filed record **[M2012-065]**, **[M2011-014]**; the cycle's level is unknown, and the
  question it bears on is the castle's, which comes next.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**. The answer is wanted for the parts that earn the money: in 9M FY2026 the
segment operating income was Communications $202.2M, Infrastructure Solutions $130.9M, C&I $85.4M, Residential $31.6M,
before corporate $(61.6)M (10-Q Note 6).

**The castle tests, each with its filing fact.**
- **The filer's own account of entry.** Residential: “There are few barriers to entry for electrical contracting services
  in the residential markets.” C&I: “The electrical and mechanical contracting services industry is generally highly
  competitive ... Traditionally, competitors in certain parts of this market have faced few barriers to entry.”
  Communications: “We compete on quality of service and/or price.” (10-K FY2025, Item 1, Competition, accession
  `0001048268-25-000174`.) The rows: "there are some industries that are just never going to have barriers to entry"
  **[M2012-106]**; "Is there ease of entry?" **[M2011-014]**. The filer answers yes for two segments in its own words.
- **The low bid.** Revenue is won “principally on the basis of competitive bids”, 87.1% fixed or unit price (Item 7).
  The castle test asks whether the customer would choose it over the low bid **[M2017-009]**; a business whose customers
  do not "care from whom they buy" sells a commodity **[L2004-003]**. The filer's own description of how it wins work is
  the bid.
- **Pricing power, and the agony before a price rise** **[M2005-020]**. FY2022 is the test: when labour and material costs
  rose, fixed-price work absorbed them. Segment operating margin FY2021 to FY2022 (10-K FY2022 Note, accession
  `0001048268-22-000099`): Communications 9.7% to 3.9%; Infrastructure Solutions 11.5% to 2.1%; C&I 0.2% to −4.0%;
  Residential 5.9% to 5.2%. FY2025: single-family homebuilders “requested price concessions from their suppliers”
  (10-K FY2025 MD&A, Residential); 9M FY2026: “lower demand and reduced housing starts have limited our ability to recover
  higher material costs through increased pricing” (10-Q MD&A). The customer sets the price when volume is weak, as with
  the station next door: "whatever he charged for gas was my price" **[M2012-109]**.
- **The record through a cycle.** Operating margin on the filed XBRL: FY2009 −0.9%, FY2010 −6.3%, FY2011 −7.3%, FY2012
  −0.1%, FY2014 1.5%, FY2015 3.2%, FY2016 3.6%, FY2017 2.5%, FY2018 3.0%, FY2019 3.9%, FY2020 4.2%, FY2021 5.6%, FY2022
  2.6%, FY2023 6.7%, FY2024 10.4%, FY2025 11.4%, 9M FY2026 12.6% (FY2013 is mis-scaled in XBRL and not used). The company
  was reorganised in bankruptcy in 2006 (its 2006 Equity Incentive Plan was “authorized pursuant to the Company’s plan of
  reorganization”, 10-K FY2012, accession `0001193125-12-503507`). Communications, the segment with the best case,
  earned 6.2% in FY2016, 6.5% in FY2018, 7.7% in FY2019, 3.9% in FY2022, 14.6% in FY2025, 17.2% in 9M FY2026. A return
  that is unprecedented is not assumed to last: "we would not want to buy things on the basis that these returns would
  be sustained" **[M1998-016]**; and a base year in which earnings were poor "can produce a breathtaking, but meaningless,
  growth rate" **[L2005-003]**.
- **The low-cost position.** In a commodity field the one escape is to be the low-cost operator **[L2004-007]**,
  **[M1997-010]**. Through FY2010 to FY2022 IES's average operating margin (1.4%) was the lowest in the row below: under EME
  (3.9%) and FIX (4.3%) over the same years, and under LMB (1.9%) and MYRG (3.4%) over their shorter records. No filing fact shows a cost advantage; the filer claims advantages of “financial capabilities”, bonding capacity
  and relationships (Item 1), which the peers also have.
- **Unit volume and share of mind; the brand.** Not applicable in the rows' sense: the customer is a hyperscaler, a
  homebuilder or a general contractor buying a project, not a consumer asking by name. The best fact for the castle is
  Communications' “preferred provider” status with “long-term, repeat customers” (Item 1). It did not carry price in
  FY2022 (3.9% margin with the same customer base), so on the evidence the preference is for a reliable bidder, not a
  willingness to pay over the low bid **[M2017-009]**. Contrast the case the rows give of a supplier whose customers
  "would be totally crazy to hire some other supplier" **[M2016-009]**: no filing fact puts IES there.
- **The attacker with money** **[M2011-015]**. The assets are trained crews, a bonding line and relationships; Communications
  carried total segment assets of $535M at 2026-06-30 (10-Q Note 6) against $202M of nine-month operating income. A
  well-funded attacker buys or hires the same things, and the row's peers are doing it now (EME and FIX revenue up 53% and
  120% from FY2022 to FY2025 on their own XBRL). Labour scarcity is the present barrier and it binds every bidder
  equally; the filer names it as its own constraint, not as a moat (10-Q MD&A).
- **Ask the competitors** **[M1999-130]**: no interviews were made; the competitors' own filings are the row below.
- **Widening or narrowing** **[M1999-108]**. Margins are widening now at every competitor at once. "the improvement you
  get one day, your competitor gets the next day" **[M2004-053]**: the tide, not this castle, is the shown cause.
- **What could destroy it** **[M2000-014]**: the end of the data-centre building wave, which the backlog does not hedge
  (backlog $4,525M at 2026-06-30 against $2,374M at 2025-09-30, of which $1,723M is “agreements without an enforceable
  obligation”, 10-Q MD&A; customers “may” cancel “on short notice”, 10-K Item 1A); and the reversal of the customer float
  in billings in excess of costs, up $180.8M in nine months (10-Q).

**The competitor row**, operating income ÷ revenue, from each company's own 10-K XBRL (`peers/*_facts.json`; latest
accession that carries the year):

| | FY2010–FY2022 average | lowest year | FY2023–FY2025 average | FY2025 | accession of FY2025 figure |
|---|---|---|---|---|---|
| IESC IES Holdings (Sept FY) | 1.4% (12 yrs) | −7.3% (FY2011) | 9.5% | 11.4% | `0001048268-25-000174` |
| EME EMCOR | 3.9% (13 yrs) | −0.6% (2010) | 8.8% | 10.1% | `0000105634-26-000025` |
| FIX Comfort Systems | 4.3% (13 yrs) | −4.0% (2011) | 11.0% | 14.4% | `0001104659-26-017530` |
| MYRG MYR Group | 3.4% (2016–22) | 2.1% (2017) | 3.2% | 4.6% | `0000700923-26-000007` |
| LMB Limbach | 1.9% (2017–22) | 0.2% (2018) | 6.9% | 7.6% | `0001628280-26-013285` |

Every bidder in the building trades moved from low single digits to high single or low double digits in the same three
years (MYRG, a transmission contractor, did not). IES's rise is larger than most because it started lower; the row shows
no year before FY2023 in which IES out-earned the field.

- **The STOP.** "most moats aren’t worth a damn" **[M1995-038]**; the rows send a castle shown open on the evidence to
  OUT: "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. The evidence here is not ignorance of the
  future (which would be TOO HARD, **[M2000-019]**) but the filer's own statement of easy entry and bid pricing, the
  FY2022 collapse in the very segments that earn most today, and a competitor row in which the margin rise is shared.
  Price does not reopen it: the rows' boxes are "in, out, and too hard" **[M2006-013]**.
- **VERDICT: OUT.** The castle is shown open on the evidence: by the filer's own words entry is easy and work is won
  on competitive bids **[M2012-106]**, **[L2004-003]**; the business could not pass cost on when costs rose in FY2022
  **[M2005-020]**; and its present margins are the industry's tide, shared by its competitors **[M2004-053]**, after a
  decade at commodity margins **[M1998-016]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED.** The file closed OUT at Q2. Arithmetic is in the computation block below.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** The balance-sheet reading and the recast are in the computation block below, because the reply was asked for
them; neither is a clearance.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.** Facts found are recorded in the computation block, unjudged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.**

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED.** Arithmetic below, headed COMPUTATION.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.**

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.** What the draft would have the buyer do is the default, nothing **[M1996-006]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** No named business is in the filings.

---
## COMPUTATION — NOT A CLEARANCE
*Everything in this block was computed after the file closed OUT at Q2. It carries no entry language and clears nothing
(operator rule 3). It is written because the owner asked for these figures.*

**C1. The balance sheets, ten year-ends, read first** (`tools/run.py` table, first-filed XBRL, $M; the FY2019 to FY2022
cash figures, blank in the tool, are from the filed cash-flow statements; June 2026 from the 10-Q). "what the figures are
saying and what they don’t say and what they can’t say" **[M2025-032]**:

| year-end | assets | equity | cash | trade receivables | inventory | goodwill | intangibles | LT debt | retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2016-09 | 394 | 223 | 33 | 124 | 13 | 40 | 32 | 29 | 33 |
| 2019-09 | 445 | 246 | 19 | 186 | 22 | 51 | 27 | 0 | 66 |
| 2022-09 | 935 | 361 | 25 | 371 | 96 | 92 | 72 | 82 | 203 |
| 2025-09 | 1,596 | 884 | 127 | 552 | 112 | 108 | 42 | 0 | 801 |
| 2026-06 | 2,276 | 1,229 | 77 | 723 (+139 retainage) | 134 | 130 | 54 | 0 | 1,154 |

What moved and why. (1) FY2016 equity is lifted by a $97.1M tax benefit from releasing a valuation allowance on old
losses (XBRL income-tax line, FY2016 10-K); equity built by operations is smaller than the 2016 figure suggests.
(2) Retained earnings rose from $33M to $801M in nine years and to $1,154M at June 2026, with no dividend and small
buybacks: the business has kept almost everything. (3) Goodwill and intangibles were 45% of equity in FY2022 and 15% in
June 2026; acquisitions were modest against retention until Gulf Island ($152.0M, January 2026) and the pending DBM Global
purchase ($650M base price, 8-K `0001493152-26-036976`). (4) Trade receivables ran 16% to 18% of revenue throughout (2016
17.8%, 2019 17.3%, 2022 17.1%, FY2025 16.4%, June 2026 18.1% of trailing revenue of $3,986M): no build-up against sales.
(5) The growth is customer-financed: billings in excess of costs rose from $177M to $358M and accounts payable from $457M to
$584M in nine months (10-Q). This float reverses when the wave ends. (6) Debt was used and repaid around acquisitions
($82M at FY2022; drawn and repaid in Q2 FY2026 for Gulf Island). (7) A new asset class appears: marketable equity
securities of $310.6M at June 2026 (from $35.0M at FY2024) and a 12.5% interest in Jett Texas Company LLC, an investment
company that financed the purchase of CB&I's storage business ($44.9M paid; carried at $63.9M). The holdings are not
named in the filings read. (8) What the figures cannot say: the margin on the $4.5B backlog, and whether the $1.7B of
unenforceable agreements will become work.

**C2. The real costs and the recast.** Net income is not the measure **[L2010-017]**: FY2025 includes $7.5M of unrealised
securities gains and $14.8M of non-cash equity-method income from Jett; 9M FY2026 includes $80.4M of gains on marketable
securities (10-Q). Stock pay is a cost **[L2015-003]**. Depreciation is a true cost **[L2015-004]**; capital spending now
runs above it (FY2023 $17.7M against D&A $29.4M; FY2024 $45.2M against $37.1M; FY2025 $67.3M against $46.9M; 9M FY2026
$123.0M against $45.7M; guidance for FY2026 $110M to $130M, 10-K MD&A). The filing gives no maintenance split (searched
“maintenance” in Item 7 of the 10-K and the 10-Q MD&A; the capex discussion is of capacity). Percentage-of-completion
covers about 64% of revenue (10-K Item 7), the kind of accounting the rows name as open to games **[M2013-086]**; no tell
was found in the balances read (receivables flat to sales, contract assets $120M against contract liabilities $358M).

**Owner cash after every real cost** = operating cash + trading-securities purchases booked in operating cash − stock
pay − distributions to noncontrolling interests − all capital spending − finance-lease principal ($M; filed cash-flow
statements, `owner_cash.py`):

| FY | owner cash, all capex | D&A variant |
|---|---|---|
| 2021 | 26.0 | 11.5 |
| 2022 | −25.6 | −21.8 |
| 2023 | 117.0 | 105.3 |
| 2024 | 196.5 | 204.6 |
| 2025 | 255.0 | 275.3 |
| **five-year average** | **113.8** | **115.0** |
| trailing twelve months to 2026-06 | 395.6 (includes the $180.8M rise in billings in excess) | |

**C3. Capital (Q3's arithmetic).** Operating tangible equity at FY2025 (equity $884.0M less goodwill $107.8M,
intangibles $41.6M, cash $127.2M, securities $104.6M, Jett $59.7M) is about $443M with no debt, against operating income
of $383.5M: the capital needed is small because customers finance the work. At FY2019 the same figure was about $150M
against $41.9M; at FY2022 about $254M (with $82M of debt) against $56.0M. The return on the capital the business needs is
high in the boom and was moderate before it **[M2010-090]**; "a cyclical peak in earnings" is the first explanation the
rows say to rule out **[L1994-009]**, and it has not been ruled out.

**C4. Value (Q7's arithmetic, the CONVENTION construction).** Five-year average owner cash $113.8M; the growth shown
(from $26.0M in FY2021 to $255.0M) is from a poor base year **[L2005-003]** and is capped at the discount rate; ten years,
then zero nominal growth; discounted at the 5.63% sovereign **[L2000-021]**, **[M1996-025]**:
- **Value range: $51 to $79 a share** ($2.02B no-growth; $3.16B growth capped at 5.63%) **against $338.19.** Top to bottom
  1.6 to 1, inside the three-to-one width. The price is 4.3 times the top of the range.
- Owner-cash yield at the price: 0.84% on the five-year average, 2.94% on the trailing twelve months, against the 5.63%
  bond. To justify $338.19 at the sovereign, the five-year average would have to grow 24.4% a year for ten years (8.2% from
  the trailing figure, which carries a working-capital inflow).
- With the trailing figure in place of the average: $176 to $276, still below the price; a range built from both ends
  would run $51 to $276, wider than three to one **[L2000-025]**.
- **FAIR-PRICE BAND (owner's request), COMPUTATION:** at the floor of about ten percent (CONVENTION, **[M2003-149]**), the
  prices that return ten percent are **$29 (no growth) to $42 (growth capped at the sovereign)**. Both lie below the
  bottom of the value range at the bond rate, so **no price inside the $51 to $79 range reaches the floor**; the band is
  $29 to $42.
- **CHEAP PRICE (owner's request), COMPUTATION:** **about $28 a share or below**, where the five-year owner cash alone,
  with no growth, returns the ten-percent floor and the shown growth is free; at that price the case would not need a
  pencil **[M1996-084]**, **[M2009-005]**. It does not reopen Q2: a castle shown open is not cured by price.
- **Q8's bond test, arithmetic only:** the 0.84% owner-cash yield is below the 5.63% bond **[M1997-089]**.

**C5. Facts for Q5, Q6 and Q9, recorded and not judged.**
- *Control.* Tontine (Jeffrey L. Gendell) owned about 52% at 2026-07-27 (10-Q Note 2); 53.2% after selling 182,094 shares
  between 2025-12-03 and 2025-12-11 at weighted prices of $417.93 to $480.37 pre-split (13D/A `0001104659-26-002521`).
  Mr. Gendell was CEO from 2020-10-01 to 2025-06-30 and is Executive Chairman; his brother David is a director. Most
  Tontine shares are on a resale shelf. Related-person dealings disclosed: an office sublease from Tontine at about
  $8,625 to $8,810 a month, a board-observer letter, and the employment of the CEO's son, wife and daughter (FY2025 pay
  about $604K, $288K and $156K) (DEF 14A). The Jett investment is not disclosed as related-party.
- *Pay* (DEF 14A). Gendell total $3.35M FY2025; Simmes $6.20M, including a supplementary bonus of 1% of adjusted pretax
  income above 80% of target (cap $5M). Long-term units vest on “Cumulative Adjusted Pretax Income”; the FY2023–25 target
  was $336.0M and the outcome $852.0M (153.6% over), vesting at the 120% cap. No capital charge in either plan; compare
  **[L1994-019]**, **[M1995-010]**. “Value Creation PSUs” (50,000 to Gendell pre-split) were granted in November 2024 in
  consideration of “the related significant increase in stockholder value”.
- *Buybacks.* FY2025: 173,262 shares at $174.25 pre-split ($87.13 post-split); 9M FY2026: 4,112 shares at $418.31
  pre-split ($209.16). The programme names no price **[L2016-002]**. Both averages sit above the top of the C4 range
  ($79); under the framework's CONVENTION at Q6 they would weigh against. The FY2026 average ($418.31 pre-split) lies inside the
  range at which Tontine sold in December 2025; the 10-Q does not give the purchase dates.
- *Issuance.* DBM Global: $650M base price, of which $140M in 215,487 new shares at $649.69 pre-split ($324.85
  post-split), the rest in cash; not all-stock, so the one Part A STOP **[L2009-019]** is not engaged. The new shares are
  credited at about four times the C4 top, so on this run's arithmetic the stock leg favours IES's continuing owners
  **[M1995-001]**; what the $510M cash leg buys (DBM's own earnings) was not read.
- *Retention, market leg* **[R1995-009]**: retained earnings rose about $694M from FY2020 to FY2025 while market value rose
  from about $0.67B to about $7.9B (Yahoo split-adjusted closes $15.89 and $198.82, aggregator); passes in market value,
  the intrinsic leg not tested.
- *Debt and exposures.* No funded debt at 2026-06-30; $300M revolver ($287.8M available), covenants 3.0× leverage and
  3.0× interest cover; surety bonds with estimated cost to complete $400.9M; a change of control (Tontine selling) would
  trigger change-of-control provisions in the credit agreement and the surety agreements (10-Q Note 2). Little or no debt
  holds today **[R1997-001]**; the DBM cash leg will need the securities, the revolver or both.

---
## THE BOX
**OUT**, at **Q2**: the castle is shown open on the filer's own evidence (easy entry and competitive bids in its own
words, the FY2022 margin collapse in the segments that earn most today, and a competitor row in which the margin rise is
shared by every building-trades bidder) **[M2012-106]**, **[M2005-020]**, **[M2004-053]**. Not reached as a clearance, but
computed for the owner: value range $51 to $79 a share against $338.19; fair-price band $29 to $42; cheap below about $28.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template was copied before `tools/run.py` was run). **Not** written
      question by question with a commit after each: the research was done first and the file written in one pass; no
      commit was made, at the operator's instruction for this run.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, see below); every filing fact carries its
      document and accession; numbers without a filing are arithmetic on filed numbers, in `owner_cash.py`.
- [x] The order was kept; Q2 failed and closed the run; everything after it is NOT REACHED or headed COMPUTATION.
- [x] Owner cash after every real cost, never a net-income proxy; the sovereign from the US Treasury; the price flagged as
      an aggregator quote; the Yahoo split-adjusted historical closes flagged.
- [x] Contrary evidence written down as it was found (Foundations, four items).
- [x] No point-in-time anchor; rows of every year may be cited.
- [x] Only the arithmetic lines of `tools/run.py` were used, and two of them were found wrong and replaced (market cap,
      owner earnings); its v4 text was not read as rule.
- [x] `python tools/check_framework.py` run before handing back (result recorded in the reply; no commit made).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. **(1) The tooling gave two wrong numbers that look right.** `tools/run.py` printed a market cap of $6.74B
by multiplying a post-split quote by the pre-split cover count (the 2:1 split was distributed on 2026-08-21, after the
2026-07-27 cover date), and so printed an implied growth (6.8%) and yields (2.52% to 2.72%) that are off by a factor of
two; `tools/sources.py` already has `split_factor_after`, which run.py does not apply to the cover count. Its owner
earnings start from operating cash, which here includes $62M (FY2025) and $154M (9M FY2026) of purchases of trading
securities, and it ignores distributions to noncontrolling interests and finance-lease principal. The framework's rule
(read only the arithmetic lines) assumes the arithmetic is right; it needs a line saying the share count must be brought
to the price's split basis and the operating-cash line read for securities classified in it. **(2) Q1 for a cyclical
business at the top of a boom.** Q1 asks for a fix on “earning power” ten years out; here the level is unforeseeable (the
data-centre wave) while the competitive position is readable. The framework does not say whether an unknowable level with
a knowable position is Q1 TOO HARD or passes to Q2. I passed it on **[M2015-016]** (the average over time and the strength
of the moat are what is asked), and the decision fell at Q2; another analyst could close the same file TOO HARD (NATURE)
at Q1, and the routing paragraph should say which. **(3) Q2 for a company of several parts.** The by-parts reading is
written for Q1 only. Here the filer states easy entry for two segments (Residential, C&I) but not in so many words for the
two that earn most (Communications, Infrastructure Solutions), where the evidence is the FY2022 margin collapse and the
shared rise. I applied the parts reading to Q2 and judged each part on its own facts; the framework should say whether a
castle shown open in the parts that earn the money closes the whole. **(4) The Q7 convention across a regime change.** The
five-year average here spans a year of negative owner cash (FY2022) and a boom with a large customer-float inflow; built
from both ends the range exceeds three to one, built from the convention's average it does not. The convention does not
say whether working-capital swings in a contractor's operating cash are to be normalised; I followed it literally and
showed the trailing figure beside it.
