# Company Run: Patrick Industries, Inc. (NASDAQ: PATK), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface copied
from `Test Runs/_TEMPLATE - Company Run.md` before any fetch. Every judgment cites a v5 ledger id in bold; every filing
fact carries its accession. Working folder: `Test Runs/_research 2026-10-06 PATK/` (fetch helper `fetch.py`, XBRL series
`series.py`, arithmetic `compute.py` with its output `compute_output.txt`, the filings as text, competitor files in
`peers/`). Em dashes are not used in this file; the protocol's computation label is written "COMPUTATION - NOT A
CLEARANCE" with a hyphen for that reason.

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is barred by the blind rule of this dispatch,
so this run does not know whether the operator holds PATK. Incentive line: the analyst holds no view and no position; the
framework's speakers own Forest River, one of Patrick's two largest customers (LCI's FY2025 10-K calls Forest River "a
Berkshire Hathaway company"), which bears on nothing below and is declared only so that it is on the record.

**CONTAMINATION, declared:** the `Test Runs/` listing showed the file name `2026-10-05 Run - LCII LCI Industries.md`
and research folders for other names dated 2026-10-05 and 2026-10-06 (ASO, BCC, BTU, GPOR, HRMY, NSIT, PTEN, ADT and
others); none was opened. The session's opening context showed recent commit subjects naming the BTU and PTEN runs (both
"OUT at Q2") and a `cover_shares.py` fix; their verdicts were seen as subject lines only. Nothing else about Patrick or
LCI from any run, review, queue or reading-list file was read.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $66.59 (close 2026-10-05; Yahoo chart API, an aggregator, flagged per operator rule 5; `tools/run.py`
  printed the same figure from its aggregator). Reference prices from the filings: $93.18 close on 2026-06-29, the last
  day before the merger announcement (S-4, accession `0001628280-26-063259`, "Comparative Per Share Market Price").
  Aggregator closes for context: $113.86 (2026-04-06), $123.79 (Dec 2025 month-end, split-adjusted).
- **Shares by class:** one class, common stock, no par: **32,118,264** as of 2026-07-31 (10-Q cover, filed 2026-08-06,
  accession `0000076605-26-000075`; `python Screens/cover_shares.py PATK`). Diluted weighted average Q2 2026 was 33,973
  thousand (convertible-note warrants and awards). Splits: three-for-two in May 2015, December 2017 and December 2024.
- **Market cap:** about $2,139M. Total debt principal $1,429.3M and cash $29.2M at 2026-06-28 (10-Q Note 8), so net debt
  about $1,400M and enterprise value about $3,539M.
- **Sovereign for the earnings currency (USD):** 5.66%, 30-year par yield, US Treasury daily par yield curve, 10/05/2026
  (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-19, `0000076605-26-000013`); 10-Q Q2 2026 (filed
  2026-08-06, `0000076605-26-000075`); DEF 14A 2026 (filed 2026-03-30, `0000076605-26-000034`); merger 8-K 2026-06-30
  (`0000076605-26-000059`); HSR 8-Ks (`0000076605-26-000080`, `0000076605-26-000084`); Form S-4 joint proxy/prospectus
  (filed 2026-09-23, `0001628280-26-063259`); Q4 2025 earnings release exhibit (`0000076605-26-000007`); 10-Ks for FY2007
  (`0000914760-08-000059`), FY2008 (`0000914760-09-000078`), FY2009 (`0000914760-10-000037`), FY2010
  (`0001140361-11-019493`), FY2012 (`0001140361-13-014593`), FY2015 (`0001437749-16-027616`), FY2018
  (`0000076605-19-000040`), FY2020 (`0000076605-21-000059`), FY2022 (`0000076605-23-000050`), FY2023
  (`0000076605-24-000078`), FY2024 (`0000076605-25-000062`). Competitors and customer: LCI Industries 10-K FY2025
  (`0000763744-26-000011`) and XBRL company facts; Thor Industries 10-K FY2026 (`0000730263-26-000027`).
- **One figure cross-checked against the filed statement:** FY2025 net cash provided by operating activities $329,414
  thousand in the 10-K cash-flow statement equals the XBRL value `tools/run.py` used (329.4); stock pay $19,066 thousand,
  D&A $170,212 thousand and acquisitions $121,740 thousand also match.
- **`tools/run.py PATK` arithmetic lines only** (Part VII; its v4 material ignored): owner cash (OCF less stock pay less
  capital spending) 2023 $330.3M, 2024 $234.4M, 2025 $227.4M; D&A basis $244.7M, $143.5M, $140.1M; five-year window
  capex basis $253.3M, D&A basis $182.4M. Stock pay resolved and complete for each year (tags printed by the tool,
  checked to the 10-K). One alternate: a $0.5M finance-lease principal payment in 2025 (immaterial).

### The balance sheets first, ten year-ends and the crisis before them ("balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**)
USD millions, first-filed XBRL checked to the statements for 2025 and June 2026:

| year-end | equity | goodwill + intangibles | tangible equity | debt | cash | receivables | inventory | sales |
|---|---|---|---|---|---|---|---|---|
| 2016 | 185 | 275 | -90 | 273 | 6 | 38 | 120 | 1,222 |
| 2017 | 371 | 471 | -100 | 354 | 3 | 78 | 175 | 1,636 |
| 2018 | 409 | 665 | -256 | 631 | 7 | 82 | 273 | 2,263 |
| 2019 | 497 | 676 | -179 | 675 | 139 | 88 | 254 | 2,337 |
| 2020 | 559 | 852 | -293 | 818 | 45 | 133 | 313 | 2,487 |
| 2021 | 768 | 1,191 | -423 | 1,286 | 123 | 172 | 614 | 4,078 |
| 2022 | 955 | 1,349 | -394 | 1,284 | 23 | 173 | 668 | 4,882 |
| 2023 | 1,045 | 1,288 | -243 | 1,026 | 11 | 164 | 510 | 3,468 |
| 2024 | 1,128 | 1,600 | -472 | 1,318 | 34 | 178 | 552 | 3,716 |
| 2025 | 1,184 | 1,583 | -399 | 1,289 | 26 | 185 | 595 | 3,951 |
| Jun 2026 | 1,131 | 1,539 | -408 | 1,429 | 29 | 277 | 653 | (H1 2,039) |

What the figures say. (1) Tangible equity is negative in every year: the whole of shareholders' equity, and more, is
purchased goodwill and intangibles; the operating assets are carried by debt and payables. (2) Debt rose 4.7 times in nine
years while sales rose 3.2 times; the rise came with the acquisitions ($2.41B of acquisition cash 2016 to 2025, XBRL
`PaymentsToAcquireBusinessesNetOfCashAcquired`). (3) Inventory rose faster than sales (9.8% of sales in 2016, 15.1% in
2025), and receivables from about 11 to about 17 days of sales; the 2021 inventory build (313 to 614) depressed 2021
cash and its release in 2023 (668 to 510) lifted 2023 cash: "If either year was aberrational, any calculation of growth will be distorted" **[L2005-003]**. (4) In
H1 2026 the revolver rose from $75M to $205M while $106.1M was spent on buybacks and $31.2M on dividends; operating cash
was $68.9M against $189.5M a year earlier (inventory up $56.5M). (5) Cash is never held in size; liquidity is the bank
revolver ($875M, due 2029).

What the earlier balance sheets say, and the figures cannot show in the table: in 2007 Patrick bought Adorn Holdings with
debt; at 31 Dec 2007 it "was in violation of the leverage covenant" and ran under a waiver (FY2007 10-K); in 2008 it wrote
off $27.4M of goodwill and $29.4M of intangibles, lost $71.5M on sales of $325.2M, and amended its credit agreement by
issuing lenders warrants for 474,049 shares at $1 (FY2009 10-K); at the end of 2009 it was exploring "asset sales,
divestitures and other types of capital raising alternatives" to cut leverage and had not yet refinanced a facility
expiring 3 January 2011; shareholders' equity was $18.1M at the end of 2010 (XBRL). The share price (aggregator,
split-adjusted) went from $2.32 (Dec 2007) to $0.12 (Dec 2008), a fall of about 95%.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**. The quotation has fallen from $113.86 in April to $66.59; it "just tells us prices" **[M2006-077]** and
says nothing yet about the business. Who is paid to tell me: the merger case in the S-4 is made by advisers paid on
completion and by a board whose pay is set on EBITDA, so it is read knowing there is an "enormous amount of fees possible from one action, and no fees applicable from another action" **[M2020-037]**. The analyst's
habits govern the run: look for "what you’re missing" **[M2025-013]** and "write it down in the first 30 minutes" **[M1997-127]**.

**Contrary evidence, written down as found** (in the order found):
1. FY2025 10-K, Item 1: "The barriers to entry for each industry are generally low", and "competition exists primarily
   on price, product features and innovation, timely and reliable delivery, quality and customer service." The same
   sentences stand in the FY2023 10-K.
2. FY2025 10-K, Item 1: Forest River and Thor together 28% of net sales (29% in 2024 and 2023); "Our customers do not
   maintain long-term supply contracts". FY2012 10-K: two RV customers 54% of sales; five customers 64%; one large MH
   customer had begun "producing in-house one of the product lines" Patrick had supplied.
3. FY2007 to FY2009 10-Ks: covenant breach, $56.7M of acquisition goodwill and intangibles written off within about a
   year of the purchase, lender warrants at $1, a 95% fall in the share price, sales down 43% from 2007 to 2009, gross
   margin 8.4% in 2008. FY2009 10-K: bankrupt competitors may return "offering below market pricing".
4. Q4 2025 release (`0000076605-26-000007`): adjusted EBITDA, adjusted net income and adjusted EPS featured; the
   adjustments remove a $24.4M settlement of "a motor-vehicle accident that resulted in two fatalities" (10-K) and add
   back stock pay.
5. DEF 14A 2026: the long-term award is earned on "three-year cumulative Company EBITDA"; the annual bonus on net income
   adjusted for acquisitions and "non-recurring charges" ($155.6M adjusted against $135.1M reported); the chief executive
   has also been Chairman since May 2024.
6. 10-Q Q2 2026, Part II Item 2: 981,867 shares bought between 30 March and 28 June 2026 at average prices of $102.39,
   $92.73 and $89.69, while the S-4 shows merger talks running from February, ending 3 May and resuming 7 June; on
   30 June the board agreed to issue about 30.2M shares (S-4 pro forma) for LCI at an exchange ratio whose implied value
   was $115.92 per LCI share against LCI's $100.12 close.
7. S-4 background: the Patrick board on 4 April 2026 discussed "the risk of vertical integration (i.e. 'self-supply')
   initiatives by certain significant customers"; in April 2026 a customer of both companies ("Party B") "expressed
   reservations regarding the potential combination"; the parties discussed "opportunities for customers to share in
   potential synergy savings".
8. LCI's FY2025 10-K: "While barriers to entry are generally low in the industries we serve", and its "competitive edge
   lies in product quality and reliability, product innovation, price, and customer service". Thor's FY2026 10-K: "we are
   not dependent on any one supplier"; components are "purchased from numerous suppliers"; no long-term commitments.
9. 8-K 2026-09-10: Patrick withdrew and refiled its HSR notification, starting a new waiting period.

Evidence for the business, written down with the same care: Patrick's operating margin held 7.5% in 2023 when RV
shipments fell 37% and LCI's fell to 3.3%; RV content per wholesale unit rose from $1,536 (2014) to $5,190 (2025) while
shipments ended near where they began; 4,500 active customers; the filer's claim that national competition "would
require" "a substantial capital commitment".

## THE STANDING RULE
Owning a share of PATK, unlevered and sized so that a 50% fall changes nothing, does not put the buyer at risk of ruin;
the rule binds the buyer's own borrowing, which "has no place in the investor's tool kit" **[L2014-005]**, and "We are
never going to risk what we have and need" **[M2012-081]**.
No leverage is contemplated. The target's own debt is a Q9 matter (not reached).

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding means "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, found by identifying "the key variables in that particular business, and
  evaluating how predictable they were first" **[M1998-044]**; the product may stay opaque if "I understand the economic
  dynamics of the industry" **[M2011-014]**.
- **What the business is** (10-K FY2025): about 191 plants and 50 warehouses making and distributing interior and
  exterior components (laminated panels, countertops, cabinet doors, wiring, fiberglass caps, marine towers and
  electrical systems, side-by-side roofs and doors) and distributing building products, sold to OEMs: RV 45% of 2025
  sales, MH 17%, marine 15%, industrial 13%, powersports 10%. Manufacturing 74%, distribution 26%.
- **The key variables and whether they are foreseeable.** (a) Unit volumes of the OEMs it supplies: RV wholesale
  shipments went 390,500 (2006) to 165,700 (2009) to 600,200 (2021) to 313,200 (2023) to 342,200 (2025) (Patrick
  10-Ks FY2015, FY2022, FY2023, FY2025); marine powerboat wholesale 192,300 (2023) to 140,100 (2025). The level in any
  year is not foreseeable; the range of the cycle is on the record for forty years. (b) Content per unit, which mixes
  price, share and acquisitions. (c) What the OEMs, three of which hold about 86% of RV retail share, choose to buy
  outside or make inside. (d) The capital put in through acquisitions. None of these is a technology forecast; the
  products are panels, wire, fiberglass and aluminum.
- **Do the past statements tell the future ones?** The row asks whether "the financial statements will tell me the information" **[M2008-033]**: yes in form. Seventeen years of filings show the same
  economics in every cycle: sales track OEM units, margins thin, cash swings with working capital.
- **Routing.** Not a fast-changing industry; not a bank; the pending merger makes the company a combination of two
  businesses of the same kind (LCI makes RV chassis, slide-outs, windows, furniture and aftermarket parts), each read by
  its parts and each understood the same way.
- **VERDICT: IN.** The economic dynamics can be foreseen in shape (a thin-margin component supplier to a concentrated
  group of OEMs in cyclical, discretionary markets): "I understand the economic dynamics of the industry" **[M2011-014]**. What that foreseen shape shows about
  the castle is Q2's question.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" and what keeps it standing "five, 10, 20 years from now" **[M1995-038]**; "competitors will repeatedly assault any business
"castle" that is earning high returns" **[L2007-004]**.

- **The attacker with money**: "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I
  do it?" **[M2011-015]**, asked of Patrick. The filer answers it: "The barriers to entry for each industry are
  generally low" (10-K FY2025, Item 1); its largest rival says the same of itself ("barriers to entry are generally low in
  the industries we serve", LCI 10-K FY2025). The best-funded attackers are the customers: Thor (FY2026 10-K) and Forest
  River can make in-house, and the Patrick board itself named "the risk of vertical integration (i.e. 'self-supply')
  initiatives by certain significant customers" (S-4). The filer's one counter-claim, that a national competitor would
  need "a substantial capital commitment", describes the cost of copying Patrick's footprint, not a reason the OEM must
  buy from it. These are industries "that are just never going to have barriers to entry" **[M2012-106]**, and "one
  competitor is frequently enough to ruin a business" **[M2012-108]**.
- **Pricing power**, measured "by the agony they go through in determining whether a price increase can be sustained"
  **[M2005-020]**: the 10-K risk factors name "our inability to maintain or
  increase prices"; LCI's FY2025 content rise was "driven primarily by sales price increases related to tariffs", that
  is, a cost passed through, not a price raised on strength. The merger talks turned on "opportunities for customers to
  share in potential synergy savings" (S-4): the improvement goes to the customer, the commodity mark in "the improvement
  you get one day, your competitor gets the next day" **[M2004-053]**. Operating margin over the whole span: 2010 2.3%,
  2012 6.2%, 2015 7.6%, 2018 7.9%, 2019 6.6%, 2022 10.2% (the boom), 2023 7.5%, 2025 7.0% (XBRL; 2010-2012 sales from
  the FY2012 10-K). Gross margin rose (11.9% in 2007, 15.0% in 2012, 23.1% in 2025) while operating margin has not risen
  above about 7% outside the boom; the gross gain went to selling, warehouse and acquisition costs.
- **Unit volume and share of mind**: the OEM, not the camper, chooses Patrick's panels; there is no brand in the
  consumer's mind to test.
- **The low-cost position**: "Another way to prosper in a commodity-type business is to be the low-cost operator"
  **[L2004-007]**; "being the low-cost producer is all-important" **[L2000-017]**. No filing
  gives Patrick's unit costs against LCI's, the regional suppliers' or the OEMs' in-house cost, and no customer or rival
  filing calls Patrick the low-cost producer. What the record shows is resilience, not low cost: 2023 margin 7.5% against
  LCI's 3.3%; but in 2008 Patrick's gross margin was 8.4% and it lost money before impairments, and in 2009 its operating
  margin was 0.6% against LCI's roughly 2.4% before LCI's $45M goodwill write-off (XBRL). The exception is not shown.
- **Would the customer still choose it over the low bid?** The See's test was whether it was "a question of people buying
  candy for the low bid" **[M2017-009]**. The filer says competition "exists primarily
  on price" first among its listed grounds; the customer says it is "not dependent on any one supplier", buys from
  "numerous suppliers", and has "identified a second-source supplier base for certain component parts" (Thor FY2026
  10-K); "Our customers do not maintain long-term supply contracts" (Patrick 10-K). The 2009 10-K feared rivals "offering
  below market pricing". This is the buyer who does not "care from whom they buy" **[L2004-003]**.
- **Ask the competitors**: LCI, the nearest, answers in its own 10-K that barriers are "generally low"; the competitor
  row is below.
- **Widening or narrowing**: content per RV unit rose ($1,536 in 2014, $2,965 in 2018, $3,235 in 2020, $5,257 in 2022,
  $4,800 in 2023, $5,190 in 2025; Patrick 10-Ks), but the metric is sales divided by units and includes acquired
  businesses and price; marine content per wholesale powerboat fell from $5,032 (2022, as restated) to about $3,900
  (2024, derived from the stated 11% rise in 2025) before $4,327 (2025). Customer concentration fell from 54% (2012) to 28% (2025) mainly because Patrick bought
  its way into other markets, not because the RV customers' power fell. The moat is not shown widening; the company is
  shown growing.
- **What could "destroy, or modify, or reduce the economic strengths"** **[M2000-014]**: the customer's own decision to self-supply or re-source,
  named by the board; a cycle like 2008-2009 with the present debt.
- **The competitor row** (same metric, competitors' own filings, the whole span):

| metric | Patrick (PATK) | LCI Industries (LCII) | source |
|---|---|---|---|
| operating margin 2010 / 2015 / 2019 / 2022 / 2023 / 2025 | 2.3% / 7.6% / 6.6% / 10.2% / 7.5% / 7.0% | 7.9% / 8.3% / 8.4% / 10.6% / 3.3% / 6.8% | XBRL company facts, CIK 76605 and 763744 |
| owner cash (OCF less stock pay less capex) as % of sales, mean 2016-2025 | 6.0% | 5.5% | `compute.py` |
| owner cash, sum 2016-2025 | $1,830M | $1,787M | same |
| acquisitions, sum 2016-2025 | $2,412M | $1,385M | same |
| RV content per unit, 2025 | $5,190 per wholesale RV | $5,670 per towable, $3,993 per motorhome | PATK release `0000076605-26-000007`; LCII 10-K `0000763744-26-000011` |
| two largest RV customers | Forest River + Thor 28% of sales | Thor 15% of sales | 10-Ks FY2025 |
| own words on barriers | "generally low" | "generally low" | 10-Ks FY2025 |
| Dometic (Swedish, not an SEC filer) | not read | | flagged: no filing obtained |

  The two leading suppliers earn the same thin margin over the cycle, each says its industry has low barriers, and each
  sells to the same three OEMs. Neither filing shows a supplier whose returns the customers cannot reach.

- **VERDICT: OUT.** The castle is shown open on the evidence: the filer's own statement that the barriers to entry "are
  generally low" and that competition is first "on price", matched word for word by its largest rival and by one of its two largest
  customers' statement (Thor) that it depends on no one supplier. The single fact that closes it is the filer's own: barriers
  "generally low" (10-K FY2025, `0000076605-26-000013`). A castle anyone can reach is the case the rows send OUT: "If the
  answer had been yes, we wouldn’t have done it." **[M2011-015]**; "anything you do, your competitors
  can copy" **[M1996-017]**; "In an unregulated commodity business, a company must lower its costs to competitive levels
  or face extinction" **[L1994-035]**, and the low-cost exception is not shown: "commodity businesses have risk unless you’re the low-cost producer"
  **[M1997-010]**. Price does not reopen it: "What you can’t do is turn any investment into a good deal by paying little"
  **[M2019-015]**. Not TOO HARD: the deciding facts are on the record and run one way. The TOO HARD box is for a moat
  "that’s tenuous in any way" **[M2000-019]**; this is a castle the filer says has no wall.

## Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED (Q2 closed the file).
## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED as a verdict; the ten balance sheets were read in Step 0 as the template requires.
## Q5: WHO RUNS IT. NOT REACHED (operator rule 2: no Q5 output when an earlier question is not IN).
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7: WHAT IS IT WORTH. NOT REACHED as a verdict; the owner's computations are below, labelled.
## Q8, Q9, Q10, Q12: NOT REACHED.

---
## THE BOX
**OUT at Q2.** The filer, its largest rival and one of its two largest customers (Thor) each say on the record that the barriers are low and
that the customer can buy elsewhere or make it; the low-cost exception is not shown. Not a TOO HARD: the deciding
question is answered, not unanswerable, so no research pass is opened. For the owner's report, the computations below sit
beside the price: price $66.59; value range at the long bond (COMPUTATION) $139 to $211 a share (whole-cycle bottom $131,
D&A-basis bottom $100); fair price on the ten-percent floor about $77 (enterprise basis, central case); cheap price about
$58. None of these is a clearance.

---
## COMPUTATION - NOT A CLEARANCE (at the owner's request; the file closed at Q2, and nothing here is entry language)
Arithmetic in `Test Runs/_research 2026-10-06 PATK/compute.py`, output in `compute_output.txt`. Construction per the Q7
CONVENTION of the framework (Part VI): owner cash after every real cost, five-year average 2021-2025, carried at the
growth shown and capped by Q3, ten years then zero nominal growth, discounted at the long bond, 5.66%.

**Owner cash** (OCF less stock pay less all capital spending, USD M): 2021 164.4; 2022 310.0; 2023 330.3; 2024 234.3;
2025 227.4. **Five-year average $253.3M** (about $7.89 a share). Variants: D&A basis $182.4M (deducts amortization of
acquired customer relationships, which the rows say "arise through purchase-accounting rules" **[L2012-003]**, so this is
the harsh variant); depreciation-only $262.7M; capital spending averaged $72.5M against depreciation of $63.0M, so the
capex basis already sits a little above a maintenance estimate. Acquisitions averaged $263.3M a year in the same window,
and owner cash after acquisitions averaged about minus $10M a year. 2025 operating cash includes a $42.0M rise in
deferred taxes (bonus depreciation; 10-K MD&A), which flatters that year.

**Growth shown:** aggregate owner cash 2021 to 2025, 8.45% a year; the base year 2021 is depressed by the inventory build, and "a base year in which earnings were poor can produce a
breathtaking, but meaningless, growth rate" **[L2005-003]**; and the growth was bought: sales fell from $4,078M to $3,951M over the window despite $1.32B of
acquisitions. CONVENTION of this run (from Q3's "how much capital must go in", confessed): the shown-growth case deducts
the window's average acquisition spending in each of the ten growth years, because the growth cannot be had without it.

**VALUE RANGE (equity, from levered owner cash, at 5.66%):**
- No-growth, five-year capex basis: $4,475M, **$139 a share** (bottom of the convention's range).
- Shown growth, capped (acquisitions deducted): $6,768M, **$211 a share** (top). Uncapped, shown only to show the cap's
  effect: $272. Width 1.5 to 1, inside the convention's three-to-one.
- **Whole-cycle variant** (the window holds the 2021-2022 RV boom): owner cash at the 2016-2025 mean margin (6.02% of
  sales, one full RV cycle) on 2025 sales = $237.7M; no-growth value **$131 a share**. Stress variant at the 2009-2025 mean
  margin (4.86%, which includes the 2009 trough) = $191.9M; **$106 a share**. D&A-basis no-growth: **$100 a share**.
- What the range means: at the long bond with no risk premium, every case sits well above $66.59. The range is
  arithmetic on a castle Q2 found open; the rows say a tenuous moat cannot be valued at all, "We don’t know how to valuate
  that" **[M2000-019]**.

**FAIR PRICE** (the price at or below which the central case clears the ten-percent pre-tax floor, the framework's Q7
CONVENTION, from "at least 10% pre-tax returns" **[L2002-020]** and "a point at which we drop out of the game" **[M2003-149]**). Central case: the whole-cycle owner cash, $237.7M, with no growth and
no acquisitions. Tax treatment: owner cash is after cash taxes; it is grossed up at the FY2025 effective rate, 23.7%, to
$311.5M pre-tax. Basis: the floor is applied to **equity plus net debt** (pre-tax owner cash plus FY2025 net interest
$74.5M, against market cap plus $1,400M net debt), because a return on equity alone can be made "almost any number you
want if we just used enough leverage" **[M2001-054]**.
- **Fair price, enterprise basis: about $77 a share** (central). Equity-only basis, shown beside it: about $97.
- At $66.59 the central case yields about 10.9% pre-tax on enterprise value: above the floor by less than one point, a
  case that would need a pencil, where the rows ask that "It should scream at you" **[M2009-005]**.
- Other cases, enterprise basis: five-year capex basis $83; stress $58; D&A basis $54.
- Pro forma for the LCI merger (if it closes; "we never count on synergies" **[L2016-008]**): central owner cash $464.6M for
  62.4M basic shares ($7.44 a share against $7.40 standalone), pro forma net debt about $2,081M; fair price about $82
  (enterprise), $98 (equity-only).

**CHEAP PRICE** (below which no pencil is needed). CONVENTION of this run, confessed: the lower of (a) the price at which
the stress case (the 2009-2025 mean margin, which carries a 2009-type trough) still clears the ten-percent floor on
enterprise value, and (b) one half of the whole-cycle no-growth value at the long bond. Rationale: the rows ask that "It should scream at you" **[M2009-005]**, illustrate with a price about a third of value ("worth 97 billion or 103 billion if I was
buying it at 35 billion") **[M2008-068]**, and say "the more volatile the business is" the "larger the margin of safety" **[M1997-080]**; Patrick's own record
holds a 95% price fall. (a) = $57.9; (b) = $65.4. **Cheap price about $58 a share.** Price $66.59 sits between cheap and
fair. Neither number reopens Q2.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. Not committed: the dispatch forbids
      commits; the operator commits.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every filing fact has its accession;
      every number carries a filing, a computation file or a CONVENTION label.
- [x] The order was kept; Q2 closed the run; Q3 to Q12 are NOT REACHED; no Q5 output is reported (operator rule 2).
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); sovereign from the US Treasury;
      aggregator prices flagged.
- [x] Contrary evidence written down as it was found, nine items, and the evidence for the business beside it.
- [x] No row dated after the anchor: not a point-in-time run; n/a.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` run before handing back (result reported to the dispatcher).
- Honest gaps: Dometic not read (not an SEC filer); RV content per unit not found in the FY2010 to FY2013 filings;
  organic growth cannot be separated from acquired growth beyond the first-year figures the MD&A gives; Party B is not
  named in the S-4; no unit-cost comparison exists in any filing read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q7's range and Q7's floor point opposite ways for a levered, cyclical company, and the framework does not say
which basis either uses.** Discounting levered owner cash at the long bond puts the bottom of the range at about twice the
price (a "screamer" on its face), while the ten-percent floor applied to equity plus net debt clears by under a point (a
pencil case). The framework does not say whether owner cash is before or after interest, nor whether the floor is on
equity or on enterprise value; the run showed both and chose enterprise for the floor. (2) **The Q7 CONVENTION's "growth
shown" does not say what to do when the growth was bought.** For a serial acquirer the window's growth came with $1.3B of
acquisitions; the run deducted the acquisition spend in the growth case (a CONVENTION of this run, from Q3). Without that,
the top of the range is $272 instead of $211. (3) **Q6's one STOP depends on Q7, which comes after it.** The rows' "it's impossible for that buyer to make a sensible deal in an all-stock deal" **[L2009-019]** cannot be tested at Q6 without the Q7 value; for a company with a pending
all-stock merger the order hides the most important Q6 question until Q7, and a Q2 close hides it altogether. (4) **No
rule says which company a buyer is buying when an all-stock merger is pending.** The run valued Patrick standalone and pro
forma side by side. (5) **The low-cost exception at Q2 cannot be tested from filings** for a supplier to an oligopsony;
no filing gives unit costs, so the exception was recorded as "not shown" rather than "absent". (6) The template's POSITION
NOTE asks the analyst to check `PORTFOLIO.md`, which a blind dispatch forbids; the note was left unchecked and said so.
(7) Operator rule 3's label contains an em dash, which the dispatch forbids; a hyphen was used.
