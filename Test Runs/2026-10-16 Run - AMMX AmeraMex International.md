# Company Run: AmeraMex International, Inc., d/b/a Hamre Equipment (OTC Pink: AMMX), 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**
*(Copied from the template at 19:48 EDT before any fetch; commit 2e3f1f76.)*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching
session at the fold, after the run was committed (089cdce7): `PORTFOLIO.md` read for this ticker only; not held.*

**Dispatched run.** Brief of 2026-10-16 (overnight cycle), departing from `Screens/_daily/_dispatch_brief.md` in the three
ways it states (lines of evidence derived by the analyst; competitors from the 10-K's own list; a company that no longer
files). Lock held by the dispatching session (`Screens/_daily/_overnight.lock`, PID 13436, written 19:46:02).
Research folder: `Test Runs/_research 2026-10-16 AMMX/` (`figures.md` holds every figure and its source;
`owner_cash.py` and `peers.py` the arithmetic; raw documents in the ignored `cache/`).

**Contamination declared.** Before the template was copied I ran a directory listing of `Test Runs/` filtered for
"AMMX", "amera" or "hamre"; it returned nothing. The listing itself is a search of `Test Runs/` that the blind rule forbids;
it is declared here. Nothing else of any blind-listed file was seen. The git status at session start lists research
folders of other names (AYI, ARCB) by file name only; not opened, not used.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $0.099 (close 2026-10-15, OTC Pink, Yahoo chart API, **aggregator, flagged** per operator rule 5; 300 shares
  traded that day; closes over the prior month ran $0.081 to $0.109 on daily volumes of 0 to 44,000 shares). A thin quote.
- **Shares by class:** one class, common. The last SEC cover: **14,829,155** as of 2022-11-18 (10-Q to 2022-09-30,
  accession 0001099910-22-000243). The company stopped filing (Form 15, 2023-04-05, 0001099910-23-000058). Its later
  self-published statements give four different counts (`figures.md`, "the same year printed differently"); the latest,
  the second-quarter 2026 release (Newsfile 310172, 2026-08-18, unaudited), gives **21,112,988** at 2026-06-30, both as
  weighted shares and in the equity statement, with common stock at par $21,112 and paid-in capital unchanged at
  $21,671,534, so six million new shares carry no recorded consideration. **21,112,988 is used**; the 14.8 million SEC count
  is shown beside where it matters. `python Screens/cover_shares.py AMMX` failed: "NOT AN SEC REGISTRANT in the live
  ticker file". Issued less treasury: no treasury stock since 2019 (10-K FY2020, 0001099910-21-000051).
- **Market cap:** 21,112,988 x $0.099 = **$2.09M** (on the SEC count, $1.47M).
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-15
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2021 (2022-03-31, 0001099910-22-000055), 10-K FY2020 (0001099910-21-000051),
  10-K FY2019 (2020-06-05, 0001099910-20-000042), Form 10-12G/A with FY2017 and FY2018 audited statements (2019-07-02,
  0001099910-19-000046), the three 2022 10-Qs (0001099910-22-000107, -000157, -000243), the proxy DEF 14A (2021-10-15,
  0001099910-21-000121), the 8-Ks of 2020 and 2021, the NT 10-Q (0001099910-22-000236) and the Form 15. After the SEC
  record ends, **the company's own published statements, all labelled "UNAUDITED"**: year-end 2022 release (2023-03-31),
  year-end 2024 release (2025-04-25, Newsfile 249749), year-end 2025 release (2026-03-10, Newsfile 287859), second-quarter
  2026 release (2026-08-18, Newsfile 310172). The OTC Markets disclosure list shows annual reports for FY2022 to FY2025 and
  quarterlies to 2026-06-30 (tier code PL), but every document download returned the site's "scheduled maintenance" page
  between 19:50 and 20:05 EDT; those documents were **not read**, and the press releases stand in for them.
  The company website (ammx.net) returned 403 Forbidden.
- **One figure cross-checked against the filed statement:** FY2020 revenue $12,279,120 in the FY2020 10-K's income
  statement equals the 2020 column of the FY2021 10-K (0001099910-22-000055). The cross-check of the cash-flow statement
  failed: FY2019 operating cash is $(2,491,724) in the FY2019 10-K and $(1,525,908) in the FY2020 10-K's comparative
  column, with no restatement note found; the difference, $965,816, is twice the $482,908 loss on extinguishment of debt,
  which the FY2019 10-K added back with the wrong sign. Recorded here; weighed at Q4.
- `python tools/run.py AMMX` failed: "AMMX: not an SEC filer." **The arithmetic was done by hand** from the statements
  (`owner_cash.py`, `figures.md`). Owner cash after every real cost, by year (operating cash less property and rental-fleet
  spending, less equipment financed under capital leases, less finance-lease principal, less stock paid for services):
  2017 $0.24M; 2018 $(2.27)M; 2019 $(3.13)M; 2020 $(1.26)M; 2021 $4.33M; 2022 $(0.12)M; 2023 $(3.79)M; 2024 $(2.88)M;
  2025 $4.04M. Five-year average 2021-2025: **$0.32M**; nine-year average 2017-2025: **$(0.54)M**. 2017 to 2021 are
  audited; 2022 to 2025 are the company's unaudited releases. Depreciation 2017-2025 ran $0.80M to $1.41M a year; stock
  paid for services $25,660 (2020), $46,400 (2021), $71,000 (2022); no option plan.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the test is whether I would own this if the market closed for five years, and here
the market has nearly closed already, with days of no trades and a company that left the SEC's reporting system, so the
business is all there is to own. The market serves and does not instruct **[M2006-077]**: the fall of the quote from $0.41
(the June 2021 cover figure, 10-K FY2021) to $0.099 tells me a price, nothing more. No macro enters **[M2000-094]**:
port container-handler demand and California emission rules are read as properties of this business, not forecasts.
**Who is paid to tell you** **[M2020-037]** bears hardest: every company release names as its investor-relations contact
McCloud Communications, LLC, whose managing member is Marty Tullio, the company's own Secretary and a director since 2012
(DEF 14A 2021: "Since 1999, Ms. Tullio has owned McCloud Communications, LLC"); the company paid a broker-dealer, M Vest
LLC, in stock for services (10-K FY2021), and 200,000 shares for "marketing services" in 2022 (10-Q, 0001099910-22-000243).
The material reaching an outside reader after 2022 is written by people paid by the company. **Contrary evidence, written
down as found** **[M1997-127]**: (1) the speakers call a dealership, run well, "a very good business. It’s a local
business." **[M2015-011]**, which is the case for a well-run local dealer; (2) the audited years 2017 and 2018 show
operating margins of 17.4% and 19.9%, high for a dealer; (3) the company survived 2020 and 2023 losses and remains
in business with orders announced as recently as 2026-10-13 (Newsfile 318710, headline only).

## THE STANDING RULE
The buyer pays cash for a stock whose whole market value is about $2 million; no borrowing, no collateral, no option given,
so nothing about the purchase can call the buyer's tune **[M2012-081]**, **[L2023-005]**. The illiquidity of the quote is
a fact about selling, not about ruin. The rule does not bind here.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The lines of evidence chosen, from the 10-K's Item 1 and Item 7 (Item 1A is omitted as a smaller reporting company):**
(1) what it sells and to whom: new and used heavy equipment as "authorized dealers for manufacturers such as Taylor Machine
Works, Terex Heavy Equipment, Barko Hydraulics, Genie, and Menzi Muck", with "the majority of our revenue ... from the
sales of new and refurbished container handlers to portside logistics companies"; (2) the rental fleet and its
conversion to sales (Item 7: "six rental contracts were converted to sales"); (3) inventory and its financing (floor
plans and a $6.5M line at 10%; Item 1, Market: "Commercial success is frequently dependent upon capital availability");
(4) customer concentration (one customer 10% or more of sales in 2021, three in 2020; note 2); (5) related-party
dealings (the leased yard owned by the President's trust, the President's note, the director's brokerage); (6) the
competition paragraph; (7) going-concern language: the FY2020 10-K (0001099910-21-000051), note 2, "Going Concern
Considerations": working capital of about $(854,426) "due to classification of business line of credit as current
liability because of technical default"; a text search of the FY2019 and FY2021 10-Ks, the Form 10 and the 2022 10-Qs
found no such heading; (8) after 2022, the company's unaudited releases.

**The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will
look like in five or 10 years" **[M2012-065]**, and the product can be plain or opaque so long as I "understand the
economic dynamics of the industry" **[M2011-014]**. The economics here are a local dealer's: buy machines from makers and
from trade-ins and closing terminals, refurbish, sell or rent them, earn a margin on each machine, carry the inventory on
borrowed money, and sell parts, service and hauling. The key variables **[M1998-044]** are the margin per machine, the
utilisation of the rental fleet, the cost of the inventory financing, the maker authorisations, and a handful of port
and forestry customers. None is a technology forecast: the makers bear the product change (the 2026 releases add
California zero-emission grant revenue, "Cal-Start CORE Grant Revenues" of $940,830 in the second quarter of 2026,
Newsfile 310172, which is the dealer passing through a subsidy on a maker's machine). Would the industry's insiders write
the ten-year forecast down **[M2000-105]**? For a small Northern California dealer, yes, in kind: it will earn a thin and
lumpy margin on machines it does not make, set by makers, rival dealers and auctions, financed at the lenders' rates.
That is a forecast of mediocrity, but it is a forecast, and what the economics will be is knowable **[M2006-076]**.

**What troubled the test.** The statements do not reliably tell me the future statements **[M2008-033]**, but that is
because of how they are kept, not because the economics are unforeseeable; it belongs to Q4. Do I doubt it is inside
the circle **[M2002-092]**? Not the economics of a dealer; the doubt I have is about the numbers and the people, which
later questions own.

**VERDICT: IN.** The ten-year economics of a small equipment dealer and renter are foreseeable in kind **[M2012-065]**,
**[M2011-014]**; whether they are good is Q2's question **[M1997-148]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The filer's own answer, first.** Item 1, Competition (10-K FY2021, 0001099910-22-000055; the same words in the Form 10,
0001099910-19-000046): "There are a large number of companies and individuals engaged in the provision of construction
equipment; accordingly, there is a high degree of competition in our industry. Many of the companies and individuals with
whom we compete have substantially greater technical, personnel, and financial resources than us. In view of our limited
financial resources, we will continue to be at a significant competitive disadvantage compared to our competitors."
Contrary evidence is hunted against that sentence below; none overturns it.

**The castle tests, each with its filing fact.**
1. *The attacker with money* **[M2011-015]**. The whole of what an attacker must assemble is a yard, a maker's dealer
   authorisation, a parts stock and a credit line. Equity at the end of 2025 was $3.0M or $3.7M depending on which company
   release is read (`figures.md`); "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could
   I do it?" has an easy answer here, and the authorisations are the makers' to give: the 10-K names "authorized dealers
   for manufacturers such as Taylor Machine Works, Terex Heavy Equipment, Barko Hydraulics, Genie, and Menzi Muck", and
   no filing found states an exclusive territory (a text search of the four annual filings for "exclusive" found none
   bearing on a dealer agreement). "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**.
2. *Pricing power, the agony before a rise* **[M2005-020]**. The gross margin on equipment sales, by year from the filed
   and published statements: 2017 18.3%, 2018 18.9%, 2019 9.3%, 2020 1.0%, 2021 15.2%, 2022 22.5%, 2023 8.7%, 2024 8.7%,
   2025 4.8%, and in the second quarter of 2026 **negative 19.9%** (equipment sales $3,814,230 against their cost
   $4,572,903, Newsfile 310172), which the CEO calls "margin pressure associated with several large, lower-margin fleet
   transactions". A business that sells machines below cost to move them has no price of its own; the price is the
   market's for each machine, and "whatever he charged for gas was my price." **[M2012-109]**.
3. *The brand in the customer's mind* **[M2008-075]**. "a brand is a promise"; the refurbished export machines are "sold
   AS IS with NO warranty agreement" (10-K FY2021, Item 1, Strategy), and the notes say "Generally, the Company sells its
   equipment with no warranty." The name the customer asks for is Taylor or Terex, not Hamre.
4. *Would the customer still choose it over the low bid* **[M2017-009]**. Customers are found by referral, billboard, a
   yard "highly visible from the freeway", and "Monitoring government websites, bidding on jobs" (Item 1); one customer was
   10% or more of 2021 sales and three of 2020's, and "The loss of one of these customers would significantly impact the
   Company" (note 2, 10-K FY2021). Government bids are the low bid by construction; a used machine bought for a price is
   "a product that has a whole bunch of competitors" **[M2023-074]**.
5. *The low-cost position* **[M1997-010]**, **[L2004-007]**. In a field where the machine is the commodity, the cost that
   differs between dealers is the cost of carrying the inventory, and here it is high: the main line at "a rate of 10%,
   per annum" (note 6, FY2021), the floor plan at "30 day LIBOR plus 6.75%" after 180 days, the 2022 senior facility at
   "8.25% plus the SOFR" (note 15); interest paid was $1,202,977 in 2024 and $1,354,386 in 2025 against operating profit of
   $437,844 and $926,517 (Newsfile 287859). The speakers' own reason for staying out of dealer finance is that "we can’t
   come up with money as cheap as the banks can" **[M2015-011]**; a dealer whose inventory is financed at these rates is
   the high-cost carrier, and "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**.
6. *Unit volume, share of mind, widening or narrowing* **[M1999-108]**. Revenue 2017 to 2025: $8.7M, $9.8M, $12.7M,
   $12.3M, $24.7M, $19.2M, $13.4M, $14.7M, $14.0M; the rental fleet was built, sold down to $0.8M net (10-Q 2022-09-30),
   rebuilt to $6.1M (end 2024) and, in the two 2025 balance sheets the company has published, either sold down to $0.74M
   or kept at $6.62M. No series shows a position widening; the record is a trader's, lumpy and reversing.
7. *Ask the competitors* **[M2017-091]**. Not possible from the public record; the makers named in the 10-K do not
   report on their dealers.
8. *What could destroy it* **[M2000-014]**. The loss of a maker's authorisation, of a port customer, or of the credit
   lines (the FY2020 10-K's "technical default" on the business line). "one competitor is frequently enough to ruin a
   business" **[M2012-108]**.

**The competitor row.** The 10-K's own list of rivals is of makers: "Caterpillar, Komatsu Ltd., and AB Volvo", and
"Hitachi Construction Machinery Co. Ltd., Liebherr, Deere & Company, Doosan Bobcat, XCMG Group, SANY Group, and Zoomlion"
(Item 1, citing a Grand View Research report). **Two file with the SEC: Caterpillar and Deere. Flagged as not filing
with the SEC: Komatsu, Volvo, Hitachi Construction Machinery, Liebherr, Doosan Bobcat, XCMG, SANY, Zoomlion.** The named
rivals are makers, not dealers or renters. **CONVENTION of this run:** two SEC-filing equipment dealers are added as
substitutes, Titan Machinery (a dealer of CNH machines) and Alta Equipment Group (a dealer and renter of material-handling
and construction machines); rationale: the 10-K names no dealer, and a maker's margin says nothing about a dealer's. The
metric is operating margin from each filer's own 10-K (SEC companyfacts, `peers.py`), over the whole span available:

| Name | Kind | Operating margin over the span | Other | Latest 10-K accession |
|---|---|---|---|---|
| Caterpillar | maker (named) | 3.0% (2016) to 20.2% (2024), 2015-2025 | pre-tax 0.4% to 20.6% | 0000018230-26-000008 |
| Deere | maker (named) | 9.7% (2016) to 21.2% (2023), 2015-2024 | return on equity 19.4% to 46.7% | 0001104659-25-122321 |
| Titan Machinery | dealer (substitute) | -1.7% (FY2015) to 6.3% (FY2022), FY2015-FY2025 | return on equity -11.2% to 19.0% | 0001628280-26-022376 |
| Alta Equipment Group | dealer, renter (substitute) | -0.9% (2020) to 2.9% (2023), 2019-2025 | net loss in five of the seven years | 0001193125-26-076932 |
| AmeraMex | dealer, renter | -6.4% (2023) to 19.9% (2018), 2017-2025 | owner cash summed 2017-2025 $(4.84)M | `figures.md` |

**The parts table.** The filer reports two lines, equipment sales and rentals, with gross profit but no operating profit
by line. On gross profit, the nearest figure the filings allow, 2021 to 2025: equipment sales $10.11M (58%), rentals
$7.30M (42%); the rental cost line appears not to carry all the fleet's depreciation (2025: rental revenue $3,117,384,
rental cost $114,589). **Equipment sales decide** (the largest part; no part carries more than half of operating profit,
which is not reported). The rental part's castle is no better: the same fleet is converted to sales when a buyer appears
("six rental contracts were converted to sales", 10-K FY2021).

**The field's returns over the last full cycle, judged in words.** The excess returns in this field are the makers':
Caterpillar's and Deere's margins are two to ten times the dealers'. The dealers that file, Titan and Alta, earned ordinary
returns or losses across 2015 to 2025. AmeraMex's accounting returns were high in its good years (pre-tax operating profit
on year-end equity plus net debt: 21.5% in 2017, 25.1% in 2018, 39.9% in 2021) and nil or negative in others (9.3% in
2019, negative in 2020 and 2023), and across nine years the earnings never came out as cash: owner cash summed to
$(4.84)M, and on the all-equity basis to $0.56M, on a business carrying $8M to $14M of capital. A castle protects
"excellent returns on invested capital" **[L2007-004]**; here neither the castle nor the returns show.

**Contrary evidence weighed.** (1) **[M2015-011]**: "running dealerships well is a very good business. It’s a local
business." By the run's convention on a row about one company (Q2, "A row about one company"), this row about Berkshire's
own auto dealers is evidence of the speakers' view of that business, not a verdict on this one, and the same row says
"There are not any huge advantages of scale" and that dealer finance is the banks' advantage. (2) The 2022 equipment
margin of 22.5% and the 2017 and 2018 margins near 19% show the business can earn a good margin in a good year; the
2020, 2025 and 2026 margins show it cannot hold one, which is the "cyclical problem, not a secular one" question
**[L1995-022]** answered the other way: no filing shows the competitive position maintained through the bad years.

**VERDICT: OUT.** The castle is shown open on the evidence: a commodity seller **[L2004-003]** that is not the low-cost
operator **[M1997-010]**, **[L2004-007]**, whose price is the market's **[M2012-109]**, **[M2005-020]**, which an attacker
with modest money could copy **[M2011-015]**, in a field "never going to have barriers to entry" **[M2012-106]**, and whose
own 10-K says it "will continue to be at a significant competitive disadvantage". The file closes here, in the box the
speakers call "out" **[M2006-013]**.
A low price does not reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

## Q3 to Q6: NOT REACHED
Q2 closed the file OUT (operator rule 2). Facts already found for these questions are under AFTER THE STOP, not weighed.

## Q7: WHAT IS IT WORTH? NOT REACHED as a clearance.
**COMPUTATION NOT A CLEARANCE** *(operator rule 3; the protocol's heading, written without the dash; computed only
for the two reporting figures the brief asks for; nothing below is a verdict or entry language).*

Q7's range convention applied in full, on the figures in `figures.md` (`value.py`):
- **The cash input.** Owner cash after every real cost, as above (Step 0). The central figure is on the all-equity basis
  (owner cash before interest: interest paid added back at (1 - 28.15%), the FY2021 tax note's 21.00% federal plus 7.15%
  state), with the equity-only figure beside it. The company's own tax is used; no carryforward is priced separately (the
  FY2021 note's federal loss carryforward of about $2.2M begins to expire in 2036, outside ten years, and the later releases
  give no tax note).
- **(a) Cycles.** The window's first year, 2021, is aberrational on the filer's own description ("record-breaking sales",
  10-K FY2021, Item 7; "pent-up demand for equipment following the COVID pandemic", year-end 2022 release), and its last
  year, 2025, rests on a cash-flow statement whose investing lines are printed as positive "Payments" ($642,919 and
  $4,484,392) and whose year-end balance sheet the company itself replaced five months later (rental fleet $739,805 in
  Newsfile 287859, $6,619,681 for the same date in Newsfile 310172). The base is therefore the last full cycle, trough
  to trough, 2020 to 2023 inclusive (operating losses in 2020 and 2023): all-equity **$304,764** a year, equity-only
  **$(210,134)**. The literal window 2021-2025 is shown beside: all-equity $965,829, equity-only $316,831.
- **(b) Decline.** No earlier full cycle is filed to measure growth between cycles, so on the base the range is the
  no-growth case alone, said so. On the literal window the series changes sign; its halves (2021-22 against 2024-25)
  show a decline of 16.9% a year all-equity and 34.9% equity-only, carried as the bottom of the literal range.
- **(c) Acquisitions.** None in the window. **(d) Working capital** is inside owner cash (operating cash carries the
  inventory swings of $5.2M one way in 2024 and $4.9M the other in 2025). **(e) Growth spending:** the filings allow no
  maintenance guess (the rental fleet is built and sold as a trading position, not maintained), so all spending is
  charged; said so. **(f) The cap:** no growth is carried, so no cap binds.
- **Rate:** 5.43%, US Treasury 30-year, 2026-10-15. Ten years, then no growth.
- **Net debt** at the latest company-published date, 2026-06-30 (Newsfile 310172): lines of credit $1,549,303 + notes
  payable $1,315,741 current and $10,656,060 long-term, less cash $1,094,729 = **$12,426,375**. The finance-lease
  liabilities of $3,293,617 in the year-end 2025 release do not appear in the June 2026 balance sheet; left out, said so.
  The related-party operating lease is left out. Shares 21,112,988.

| Case | Annual cash | Value a share at 5.43% | Fair price a share (10%) | Return at the price |
|---|---|---|---|---|
| Central: cycle base 2020-23, all-equity, no growth | $304,764 | **$(0.32)** | **$(0.44)** | 2.1% on $14.5M (shares $2.09M + net debt) |
| Beside: cycle base, equity-only | $(210,134) | $(0.18) | $(0.10) | negative |
| Literal window 2021-25, all-equity, no growth (top) | $965,829 | $0.25 | $(0.13) | 6.7% |
| Literal window, all-equity, decline 16.9% a year (bottom) | | $(0.36) | $(0.43) | |
| Literal window, equity-only, no growth | $316,831 | $0.28 | $0.15 | 15.2% on $2.09M |
| Literal window, equity-only, decline 34.9% a year | | $0.03 | $0.02 | |

- **The floor, tested first.** At $0.099 no all-equity case earns the floor of about ten percent (the best, the literal
  window's no-growth case, 6.7%); the computation would close **OUT** at Q7 had the file reached it **[M2003-149]**. The
  equity-only literal case clears it (15.2%) only because the lenders, owed $12.4M against equity of $3.3M, take the first
  dollar; the equity-only figure never decides alone (Q7, On what the floor is earned).
- **The width.** The central range is a single case. The literal range runs from negative to positive, so no ratio of
  ends exists; said so.
- **Reporting figures (a reporting convention, not a rule):** **(a) VALUE RANGE: $(0.32) a share** (central, a single
  no-growth case on the 2020-23 cycle base, all-equity; the literal window beside runs $(0.36) to $0.25); **(b) FAIR
  PRICE: $(0.44) a share all-equity** (equity-only $(0.10)), against the price of $0.099. With the $1,549,303 of lines of
  credit treated as inventory finance and left out of net debt, the central fair price is $(0.37). On the last SEC share
  count (14,829,155) the central value is $(0.46) and the fair price $(0.63). No case of the central basis is positive.

## Q8 to Q12: NOT REACHED

---
## THE BOX
**OUT at Q2** (the castle shown open on the evidence: a commodity dealer, not the low-cost operator, price set by the
market, by its own 10-K "at a significant competitive disadvantage"). COMPUTATION beneath the stop: value $(0.32) a share,
fair price $(0.44) (all-equity; equity-only $(0.10)), against $0.099. **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down as found **[M1997-127]**; no verdict; the box is unchanged, operator rule 2.)*

**Bearing on Q3 (capital).** Owner cash summed 2017-2025: $(4,840,505); all-equity $558,446. Accounting operating profit
summed over the same years about $9.8M; the difference went into inventory (from $3.26M at the end of 2017 to $7.48M or
$11.04M at the end of 2025, by the two company releases) and a rental fleet bought and sold in turns. Book equity rose
from $1.35M (end 2017) to $3.0M or $3.7M (end 2025) with no dividend paid.

**Bearing on Q4 (the accounts).** Each item from the company's own documents:
1. The same year printed differently, with no restatement note found in the documents read: FY2019 operating cash
   $(2,491,724) then $(1,525,908); FY2022 year-end accumulated deficit $(17,464,626) (release of 2023-03-31) then
   $(16,912,288) (equity statement in the release of 2025-04-25); FY2024 net loss $(1,158,221), equity $2,241,493
   (2025-04-25) then $(856,734), $2,542,980 (2026-03-10); the 2025-12-31 balance sheet with total assets $18,197,479,
   inventory $11,040,250, rental fleet $739,805, equity $3,668,143 (2026-03-10) then $17,363,629, $7,481,302, $6,619,681,
   $3,005,677 (2026-08-18). The FY2023 net loss was reported by search results as $(764,741) in the first FY2023 release
   and is $(1,374,361) in the next; the first release was not read.
2. Balance sheets that do not balance: 2026-06-30 total assets $21,478,765 against liabilities and equity $21,485,048;
   2025-12-31 (as reprinted) $17,363,629 against $17,363,912 (Newsfile 310172).
3. The year-end 2022 release's revenue lines ($18,203,837 and $1,081,672) sum to $19,285,509, not the $19,222,509 total
   printed. The 2026 second-quarter release prints a six-month "Gross Margin: 85%" (its own table: $1,560,763 on
   $10,226,990, 15.3%). The 2025 release text gives net income "$1.0 million" and gross-profit growth "37 percent"; its
   table gives $1,125,163 and 57%.
4. FY2025 "Other Income (Expense)" of $1,865,036, larger than the year's pre-tax income of $1,587,695, with no
   explanation in the release; the reprinted 2025 deficit implies net income of $462,414 instead of $1,125,163.
5. The 2026 interim statements show a "Related Party Receivable" of $162,000 current and $534,336 non-current, not
   explained, and a financing inflow labelled "Payment on Note Payable - Related Party" of $656,750, equal to the new
   "Customer Deposits" of $656,750.
6. In the SEC filings: the FY2019 sign error above; the FY2021 notes say "no shares issued for compensation" while the
   equity statement shows 80,000 shares for services; the FY2020 balance sheet's share line reads 14,808,737 against
   14,549,155 in its equity statement; the date of the merger into the Nevada company is 1990 in the notes and the Form 10
   and 2006 in the 10-K's Item 1; management called disclosure controls and internal control "effective" in each 10-K.
7. The NT 10-Q for the third quarter of 2022 gave as its reason adapting "the new ASC842 standard for lease accounting
   ... into its existing Accounting Software so the financials flow correctly."
8. After the Form 15 (2023-04-05) no statement found is audited; every later statement read is labelled "UNAUDITED".

**Bearing on Q5 (the people; integrity facts, recorded, not judged).**
1. Every company release read names as investor-relations contact McCloud Communications, LLC, "Marty Tullio, Managing
   Member"; Ms Tullio is the company's Secretary and a director (DEF 14A 2021: "Since 1999, Ms. Tullio has owned McCloud
   Communications, LLC"). Item 13 of the FY2021 10-K lists only the yard lease and the President's note as related-party
   transactions; no payment to McCloud is disclosed there.
2. A director's brokerage bought machines from the company when two customers lost financing, the company then buying
   them back; "The brokerage made $42,681 on the transactions", and a further note "brokered through the same Director’s
   company" stood at $744,424 at the end of 2020 (note 8, 10-K FY2021).
3. The yard is leased from a trust whose trustee is the President, $12,000 a month, renewing annually; the President lent
   the company money at 10% on demand, repaid in 2021, and "From time to time ... provides a personal guarantee" on loans.
4. Director independence is stated three ways: the proxy names Maloney and Morris independent; the FY2021 10-K's audit
   committee paragraph says "Both J. Jeffery Morris and Michael Maloney are independent directors"; the same 10-K's Item 13
   says "None of our directors (see Item 10 above) are independent as defined under the Nasdaq Marketplace Rules." Brian
   Hamre, a director, is the President's nephew (Form 10/A). Maloney's holding is 130,000 shares in the proxy and 260,000
   in the 10-K.
5. Financing from Geneva Roth Remark Holdings in 2020 and 2021: convertible notes, then Series A preferred "convertible
   into Common Stock at a price per share equal to 70% of the lowest closing bid price" over ten trading days, dividends
   10%, 22% on default (8-K, 0001099910-21-000003); all repaid in 2021 before conversion (note 10, FY2021).
6. The company left SEC reporting by Form 15 in April 2023, after which its statements are unaudited, restated between
   releases without explanation, and published through the director's investor-relations firm.
7. Pay: President $150,000, CFO $120,000 a year, no bonus or options (10-K FY2021, Item 11); directors $500 each for 2020.

**Bearing on Q6 (money and owners).** No dividend ever (Item 5). Shares: 753,415,879 before a 1:50 reverse split on
2020-12-21; 559,163 post-split shares retired "at a cost of $7,813" (10-K FY2020); 80,000 and 200,000 shares paid for
services in 2021 and 2022; 21,112,988 shares at 2026-06-30 against 15,112,988 six months earlier, with par value up $6,000
and paid-in capital unchanged.

**Bearing on Q9 (debt).** Net debt $12.4M at 2026-06-30 against equity of $3.26M; long-term notes $10.66M; interest paid
exceeded operating profit in 2024 and 2025; the FY2020 10-K records a "technical default" on the business line of
credit; all inventory, equipment and rental fleet are pledged (notes 3 to 5, FY2021). The "little or no debt" criterion
**[R1997-001]** would weigh hard against.

**Bearing on Q12.** Nothing found.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 2e3f1f76); written question by question; committed after each.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock was held by the dispatching session; the
      fold is the dispatcher's.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched: **not met in full.** One filtered
      listing of `Test Runs/` for this company's names, before the template was copied, returned nothing; declared under
      contamination above. No other blind-listed file was opened, listed or searched.
- [x] Every v5 id resolves (`check_ids.py` in the research folder: 48 citations, 36 distinct ids, no E-id, none missing;
      its one flag, at **[M2011-015]**, is a false match across a filing quotation, and both fragments beside that id were
      checked by hand and are in the row); every SEC fact has its accession; facts after 2022
      carry the release date and Newsfile number in place of an accession (brief, "A company that no longer files").
- [x] The order was kept; Q2's STOP closed the file; everything after it is headed COMPUTATION or recorded as facts.
- [x] Owner cash after every real cost, never a net-income proxy; the sovereign from the US Treasury; the price flagged as
      an aggregator quote. `tools/run.py` and `Screens/cover_shares.py` both failed for a non-SEC filer; the arithmetic is
      by hand and shown.
- [x] Contrary evidence written down as found (Foundations; Q2, Contrary evidence weighed); facts for later questions under
      AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] `tools/run.py` produced no output to use; no rule or id from it entered.
- [x] `python tools/check_framework.py` PASS (run 2026-10-16 before the final commit).

**What I could not get.** The OTC Markets annual and quarterly reports for FY2022 to 2026 (download endpoint in maintenance
for the whole session); the company's website (403); the first FY2023 release; any audited statement after FY2021. The
press releases used in their place are the company's own publications, but they are not the OTC filings, and the OTC
filings may differ from them (the FY2025 annual report was amended on 2026-03-17, a week after the release used here).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) The framework has no rule for a company whose own published statements contradict each other for the
same date: Q7's specifics assume one set of figures per year, and here the company printed two balance sheets for
2025-12-31 five months apart, so "the latest filed date" for net debt and the cash input for 2025 each depend on which
document is treated as the filing. I used the later release for net debt (latest), the earlier one for the 2025 cash-flow
year (the only 2025 cash-flow statement published) and named 2025 aberrational under specific (a); another analyst could
choose otherwise. (2) Q2's business-of-parts paragraph asks for each part's share of five-year operating profit; a filer
that reports only gross profit by line, as here, leaves the threshold unappliable, and I used gross profit, said so.
(3) The brief's competitor rule (rivals the 10-K names) met a 10-K that names only makers; the framework's field test
("the filer's and the rivals' filings") does not say whether the field is the maker's or the dealer's, and the answer
decides the comparison; the dealer substitutes are a CONVENTION of this run.
