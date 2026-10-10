# Company Run: Cintas Corporation (NASDAQ: CTAS), 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch.**

Dispatched blind run under `Screens/_daily/_dispatch_brief.md` as filled by the dispatching session's message of 2026-10-07
(lock held by the dispatcher: `Screens/_daily/_overnight.lock` read "interactive v5 re-runs batch 4" at 09:53).
Working folder `Test Runs/_research 2026-10-07 CTAS/`. Raw filings and XBRL downloads are kept under `cache/` there
(gitignored); the provenance record is the accession numbers below.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**CONTAMINATION, declared:** (1) the session's opening git status listed other names' research folders (AYI, BDC, CHD,
ARCB and others) and the five most recent commit subjects, which give boxes and alert prices for CL, CMG, CSL and COKE;
(2) the `.gitignore` comments name earlier runs of other companies (DELL, SNPS, MGM, AGCO, ATR); (3) the auto-memory index
loaded with the session says that a number of names have cleared the gates and that "nothing [is] buyable", without naming
any; (4) the dispatching message says earlier Cintas run files exist. Nothing about Cintas from any of these was seen, and
none of it is used. No other run file, research pass, holding review, `PORTFOLIO.md` or register file was opened, listed or
searched.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $196.98 (quote of 2026-10-07 printed by `tools/run.py`; **aggregator, live quote only, flagged** per operator
  rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock, no par value, **400,169,561** shares
  (10-K for the fiscal year ended 2026-05-31, filed 2026-07-29, accession `0000723254-26-000028`, cover as of 2026-06-30;
  `python Screens/cover_shares.py CTAS`). Check against issued less treasury: the balance sheet of 2026-05-31 gives
  779,537 thousand issued and 379,390 thousand treasury, 400,147 thousand outstanding; agrees to within the June
  vesting. Filings after the 10-K: the press release of 2026-09-23 (8-K `0000723254-26-000044`, exhibit 99, furnished)
  gives 399,517 thousand outstanding at 2026-08-31 after buybacks of $544.7M in the quarter and to 2026-09-22. No
  prospectus or 8-K after the 10-K issues shares; the shares to be issued to UniFirst holders (0.7720 a UniFirst share) are
  not yet issued (8-K of 2026-10-06, `0000950103-26-015293`: closing not before 2026-12-11 under the FTC timing
  agreement). Count used: 400.17M (cover). **The 2024 split, checked:** the four-for-one split of September 2024 (8-K of
  2024-09-12, items 5.03 and 9.01, `0000723254-24-000040`) is inside every count above; the 10-K's per-share figures and
  the 2024 share counts are stated after it (402,948 thousand outstanding at 2025-05-31, against about 101 million before).
- **Market cap:** 400.17M x $196.98 = **$78.83B**.
- **Sovereign for the earnings currency (USD):** **5.64%**, the 30-year par yield of 2026-10-06, US Treasury daily par
  yield curve (`python tools/sources.py`). Revenue outside the U.S. is under 10% (10-K Item 7A), so USD is the earnings
  currency.
- **Filings read** (operator rule 4): 10-K FY2026 (period 2026-05-31, filed 2026-07-29, `0000723254-26-000028`); latest
  10-Q (period 2026-02-28, filed 2026-04-07, `0000723254-26-000012`); the proxy of 2026-09-15 (`0000723254-26-000040`);
  the 8-Ks of 2026-03-11 (merger agreement, `0000950103-26-003567`), 2026-03-31 (credit agreement,
  `0000723254-26-000010`), 2026-09-23 (Q1 FY2027 results, `0000723254-26-000044`) and 2026-10-06 (FTC timing,
  `0000950103-26-015293`); the S-4 for the UniFirst merger (filed 2026-04-27, `0001140361-26-016785`); the 10-Ks that
  cover the last two downturns (listed at Q2 and Q4). **One figure cross-checked against the filed statement:** net cash
  provided by operating activities FY2026, $2,276,280 thousand on the filed cash-flow statement (10-K p. 43), against
  2,276 in `tools/run.py`. Agrees.
- `python tools/run.py CTAS`, arithmetic lines only (saved as `run_py_output.txt`): operating cash 2,068 / 2,166 / 2,276
  (FY2024 to FY2026, $M), stock pay 117 / 128 / 128, capital spending 409 / 409 / 395, depreciation and amortization
  442 / 494 / 513. Its D&A line includes $194.2M (FY2026) of "Amortization of intangible assets and capitalized contract
  costs"; depreciation alone is $318.6M. It found no securities, intangible, software or other spending beside capex. It
  does not see the one Cintas-specific item: **rental garments are not capital spending here.** The filer carries
  "Uniforms and other rental items in service" as a current asset ($1,276.2M at 2026-05-31), amortized over 18 to 30
  months for uniforms and 8 to 60 months for other items (10-K, Critical Accounting Policies), and their purchase is
  inside operating cash (the line "Uniforms and other rental items in service", -$137.6M in FY2026, is purchases net of
  amortization). Sales commissions are likewise capitalized ("capitalized contract costs", $304.7M net) with their cash
  inside operating cash. Operating cash therefore already bears both; owner cash below is built from it.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own Cintas "if the market closed for five years"
**[M1997-109]**, and what decides that is "the prospects of the businesses" **[M1998-099]**, read below from the filings.
The market serves and does not instruct: the quote of $196.98 "just tells us prices" **[M2006-077]** and is set against
value only at Q7. Margin of safety is an attitude here and arithmetic only at Q7 **[M1997-126]**. The analyst's habit
that bears hardest: this is a business with a long record of rising margins and a reputation for quality, exactly the
kind of "cherished belief" against which contrary evidence must be written down as it is found **[M1997-127]**, looking
for "what’s wrong in things" **[M2025-013]**. **Contrary evidence, written down as found** **[M1997-127]**:
(1) the filer does not describe route density or a cost advantage in its 10-K; "Product, design, price, quality, service
and convenience to the customer are the competitive elements" and the markets are "local in nature and highly
fragmented" (10-K Item 1, Competition); (2) a pending acquisition of the third-largest rival, UniFirst, worth about
$5.5B, part paid in Cintas stock and under an FTC second request (8-Ks above); (3) the press release of 2026-09-23 gives
full-year guidance and features an "adjusted diluted EPS". Further items are added under the question where found.

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase of this stock would be bought with owned money, never on margin
("borrowed money has no place in the investor's tool kit" **[L2014-005]**), and sized so that a fall of half "or more"
is borne without a forced sale **[M2020-022]**; nothing in the name itself bears on the buyer's ruin **[M2012-081]**.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from the filing.** Cintas rents and launders work uniforms, mats, mops, shop towels and
  restroom items, and sells restroom supplies, first aid and safety products, workplace water, fire protection services
  and directly sold uniforms. "Over 95% of the Company's revenue is derived from fees for route servicing [...] performed by
  a Cintas employee-partner, at the customer's location of business" (10-K FY2026, Critical Accounting Policies,
  `0000723254-26-000028`). About 12,500 local delivery routes, 484 operational facilities and 12 distribution centers;
  more than one million business customers, none over 1% of revenue; over 90% of revenue in the U.S. (10-K Item 1).
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**. The key variables **[M1998-044]**: the number of customers
  and routes; revenue per customer stop (the filer's "penetration of additional products and services into existing
  customers"); price; and the cost of a stop (labor, fuel, garments, plant). Each is visible in the filings over twenty
  years (Q2 and Q4 below), and none turns on a technology. The filer's own history of the business runs from 1929 (shop
  towels collected and washed along the Ohio River) through 1968 (uniform programs) to today (10-K Item 1), and the
  rival filings of 2011 and 2025 describe the same industry in nearly the same words (UniFirst 10-K FY2011
  `0001284084-11-000040` and FY2025 `0001193125-25-256222`, Competition: quality of products, quality of service, price).
  The forecast is about customers and route costs, not about technology **[M2017-019]**, **[M2023-030]**. AI appears in the
  10-K only as a tool the company uses for "route optimization" and other functions (Item 1A).
- **Do the past statements tell me the future ones?** **[M2008-033]** Yes in the main: revenue is recurring route revenue
  billed monthly; the statements separate the rental segment from the others; and the one accounting peculiarity (rental
  garments carried as a current asset and amortized, Step 0) is stated plainly.
- **Important and knowable** **[M2006-076]**: the variables above are both. The one important item that is not yet knowable
  is the outcome of the UniFirst merger (FTC second request; closing not before 2026-12-11). It is knowable in its
  economics, since UniFirst is a filer in the same industry, and is taken at Q6 and Q7.
- **Would the insiders write it down?** **[M2000-105]** The industry's own participants do: the S-4 carries UniFirst's
  internal forecasts to fiscal 2030 and several advisers' cash-flow valuations of a uniform renter (S-4
  `0001140361-26-016785`, "Unaudited Prospective Financial Information Prepared by UniFirst"). They are noted only as
  evidence that insiders will write such a forecast down; their numbers are not used **[M1995-050]**.
- **Can I name the winner, not just the industry?** **[M2012-067]** The filings name it: of the four large North
  American renters, Cintas has grown and widened its margin while the others have not (Q2's competitor row).
- **The parts** (Q1's holding-company paragraph, extended 2026-10-06 to operating segments): Uniform Rental and Facility
  Services carries about four fifths of five-year operating profit (Q2's parts table) and decides; First Aid and Safety and
  All Other (fire protection, direct sale) are route and product businesses of the same kind and are understood by the
  same tests.
- **Do I only think I understand it?** **[M1997-024]** The risk named honestly: a route business looks simple, and the
  economics of route density are inferred from margins, not stated by the filer (contrary evidence (1), foundations).
  That is a Q2 question (is the advantage real and lasting), not a Q1 question (can its economics be foreseen).
- **VERDICT: IN.** The ten-year economics of a route-based uniform and facility-services renter can be foreseen in the
  sense of **[M2012-065]**: a century-old service whose key variables are customers, price and route cost, read from
  twenty years of filings, with no technological component that "won’t make it through the filter" **[M1998-008]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**Sources for this question.** Cintas 10-Ks FY2008 (`0000892251-08-000175`), FY2010 (`0001047469-10-006785`), FY2013
(`0000723254-13-000011`), FY2016 (`0000723254-16-000050`), FY2019 (`0000723254-19-000021`), FY2021
(`0000723254-21-000021`), FY2022 (`0000723254-22-000019`), FY2025 (`0000723254-25-000017`), FY2026
(`0000723254-26-000028`). Rivals' own filings: UniFirst 10-Ks FY2011 (`0001284084-11-000040`), FY2021
(`0001564590-21-052248`), FY2025 (`0001193125-25-256222`) and its XBRL company facts FY2010 to FY2025; Aramark's IPO
prospectus (424B4 of 2013-12-12, `0001193125-13-471927`) and 10-Ks FY2016 (`0001584509-16-000514`), FY2019
(`0001584509-19-000237`), FY2022 (`0001584509-22-000236`) and FY2023 (`0001584509-23-000237`) for its Uniform segment;
Vestis 10-K FY2025 (`0001628280-25-054597`) and company facts FY2022 to FY2025; G&K Services 10-Ks FY2010
(`0000950123-10-081070`) and FY2016 (`0000039648-16-000043`) and company facts FY2010 to FY2016. **Vestis's history,
checked:** Vestis is Aramark's former "Uniform and Career Apparel" segment, spun off to Aramark's holders on 2023-09-30
(Aramark's 10-K FY2023 describes the separation of Uniform "as an independent publicly traded company"; Vestis's first
10-K is for the year ended 2023-09-29, `0001967649-23-000025`); its own filings start there, and its earlier record is
Aramark's segment. Aramark itself filed no segment figures before its 2013 prospectus (it was privately held). **Non-filers
flagged:** Alsco (named by UniFirst as a principal competitor; private, no SEC filings) and Elis (the French renter that
made UniFirst an all-cash proposal of $230.00 a share in 2024, per the S-4's Background; listed in Paris, not an SEC
filer). Neither can be put in the competitor row.

**The competitor row: operating margin (operating income over revenue), each from its own filings.**

| Fiscal year (each filer's own) | Cintas, total | Cintas, Uniform Rental segment (pre-tax, before corporate) | UniFirst | Aramark Uniform segment, then Vestis | G&K Services |
|---|---|---|---|---|---|
| 2008 | not computed | 15.9% (FY2008 10-K, MD&A) | 10.6% | not filed (Aramark private) | 9.0% |
| 2009 | 10.8% | 13.4% (15.7% before restructuring, FY2010 10-K) | 13.2% | not filed | not computed (impairment year) |
| 2010 | 11.0% | 13.1% (336.5 / 2,569.4) | 12.7% | not filed | 7.1% |
| 2011 to 2013 | 11.6% / 13.2% / 13.1% | 14.9% (FY2013) | 10.9% / 12.0% / 13.7% | 8.8% / 8.7% / 8.3% | 7.9% / 4.9% / 8.6% |
| 2016 | 15.9% | 17.8% (672.9 / 3,777.8) | 13.7% | 12.5% | 12.5% (last year filed) |
| 2019 | 16.4% | 17.6% (976.7 / 5,552.4) | 12.8% | 7.4% | acquired by Cintas 2017 |
| 2020 | 16.4% | 17.8% (1,004.6 / 5,643.5) | 9.6% | 6.8% | |
| 2021 | 19.5% | 21.5% | 10.7% | 5.0% | |
| 2022 | 20.2% | 21.7% | 6.7% | 8.3% | |
| 2023 | 20.4% | 21.4% | 6.0% | 8.2% (Aramark FY2023) | |
| 2024 | 21.6% | 22.2% | 7.6% | 5.6% (Vestis) | |
| 2025 | 22.8% | 23.5% | 7.6% | 2.4% (Vestis) | |
| 2026 | 23.1% | 24.1% | FY2026 10-K not yet filed | not yet filed | |

Computed from: Cintas XBRL company facts (OperatingIncomeLoss over Revenues) and the segment notes cited; UniFirst XBRL
OperatingIncomeLoss over revenue and its FY2011 10-K's five-year table (FY2007 9.3%, FY2008 10.6%, FY2009 13.2%);
Aramark Uniform segment operating income over segment revenue (FY2011 117.3 / 1,340.1; FY2013 117.3 / 1,411.3; FY2016
195.3 / 1,563.7; FY2019 191.3 / 2,585.8; FY2020 171.5 / 2,517.1; FY2021 120.8 / 2,420.5; FY2022 218.1 / 2,639.4;
FY2023 227.3 / 2,770.7, all $M); Vestis OperatingIncomeLoss 158.0 / 2,805.8 (FY2024) and 64.4 / 2,734.8 (FY2025);
G&K Services company facts and its FY2010 10-K. The Cintas segment figure to FY2022 is income before income taxes by
segment, which excludes corporate interest; from FY2023 the segment note reports operating income. Comparable in kind,
not to the decimal.

**Capital behind the margins, latest filed year.** Cintas FY2026: operating income $2,606.5M on capital employed of
$7,279M (equity 5,140 + debt 2,428 - cash 289), 36% before tax; on net tangible capital (less goodwill 3,544, service
contracts 288 and noncompete and other intangibles 89) about 78% before tax. UniFirst FY2025: operating income $184.5M on
about $1,959M (equity 2,169, no debt, cash and short-term investments 210), 9% before tax. Vestis FY2025: $64.4M on about
$2,000M (equity 866, long-term debt 1,168, cash 30), about 3% before tax.

**The parts table** (five-year operating profit FY2022 to FY2026, segment notes of the FY2022, FY2025 and FY2026 10-Ks; $M):

| Part | Five-year operating profit | Share | Castle | Decides |
|---|---|---|---|---|
| Uniform Rental and Facility Services | 8,442 (1,353.5 + 1,478.8 + 1,659.5 + 1,873.4 + 2,077.0) | 81% | the route network, below | **yes** (more than half) |
| First Aid and Safety Services | 1,175 | 11% | sold on the same routes and by the same sales force; margin 25.4% FY2026 | no |
| All Other (Fire Protection, Uniform Direct Sale) | 823 | 8% | margin 15.3% FY2026; not judged separately | no |

The file closes on Uniform Rental.

**The castle tests, each with its filing fact.**
1. **What keeps it standing, and how permanent** **[M1995-038]**. The filer names its strategy, not a moat: "This frequent
   contact with our customers enables us to develop close personal relationships. The combination of our distribution
   system and these strong customer relationships provides a platform from which we launch additional products and
   services" (10-K FY2026, MD&A, Business Strategy). The filer does **not** describe route density or a cost advantage in
   its 10-K (no instance found of "density" in the FY2026 10-K or in the S-4, by text search; the 10-K lists "Product,
   design, price, quality, service and convenience" as the competitive elements). The rival does: Vestis says its "size
   and scale provide a competitive advantage in purchasing power, route density, operating efficiencies" against smaller
   competitors (Vestis 10-K FY2025, Business). The castle I read from the figures, not from the filer's words: the largest
   route network in a business where most of the cost is the stop (plant, truck, driver), so that each added product or
   customer on an existing route costs the largest network least. That reading is mine, inferred from the margins and the
   rival's text.
2. **Would it stand without the lord?** **[L2007-006]** No single superstar: the margin widened under two chief
   executives (Scott D. Farmer, July 2003 to May 2021; Todd M. Schneider since June 2021; proxy of 2026-09-15) and runs through 12,500 routes.
3. **The money test** **[M2011-015]**, **[M1997-103]**. The attacker with money existed and failed: Aramark, a food-service
   company with revenue of $13B to $19B over the span, ran the second-largest uniform renter at 5% to 12.6% margins, never
   near Cintas's, bought AmeriPride in 2017 to get bigger (Aramark 10-K FY2019: Uniform revenue up 30% to $2,585.8M) and
   saw the margin fall to 7.4%, then spun the business off; as Vestis it reports "lost business in excess of new business"
   and a 2.4% margin (Vestis 10-K FY2025, MD&A). Elis, the European leader, tried to enter by buying UniFirst in 2024,
   not by building (S-4, Background). "why are there no new entrants into the field?" **[M2000-077]**: none found
   entering by building in any filing read.
4. **Pricing power and the agony before a rise** **[M2005-020]**, **[M2005-017]**. Through the inflation of FY2022 to
   FY2025 the filer says "Management has been able to mitigate these inflationary pressures through pricing and various
   efficiency initiatives" (10-K FY2022 and FY2025, Inflation and Changing Prices). The segment's gross margin dipped from
   47.6% (FY2021) to 46.7% (FY2022) and then rose to 48.2%, 49.3% and 50.0% (FY2024 to FY2026). UniFirst's margin over the
   same inflation fell from 10.7% to 6.0% (FY2021 to FY2023). The strong position passed the costs through; the weaker
   one did not.
5. **Unit volume and share of mind** **[M1999-054]**. Organic revenue growth of 8.3% in FY2026, "a result of new business,
   the penetration of additional products and services into existing customers and price increases, partially offset by
   lost business" (10-K FY2026, MD&A); 8.9% in Q1 FY2027 (press release, 8-K `0000723254-26-000044`). Vestis's rental
   revenue fell with lost business; UniFirst's revenue was flat FY2024 to FY2025 ($2,427.4M to $2,432.4M).
6. **The low-cost position** **[M2018-043]**, **[L2004-007]**. The rows' test is cost "on parity or less" against "your
   other major competitors" **[M2001-013]**. The filings show a gross margin of 50.0% in Cintas's rental segment against
   UniFirst's cost of revenues of 63.4% of revenue, before depreciation and amortization of a further 5.8% (UniFirst 10-K
   FY2025, MD&A); the definitions differ, and the difference widens the gap rather than closing it. The filings cannot say
   how much of the gap is lower cost and how much higher price. **Contrary evidence, written down as found** **[M1997-127]**: the rows' low-cost
   operator passes its advantage on, "not to widen our profit margin but rather to enlarge the price advantage we offer
   customers" **[L1996-016]**, **[M2011-063]**; Cintas has widened its margin by about ten points in ten years. A margin
   that high is an umbrella for an attacker.
7. **The brand in the customer's mind** **[M2015-038]**. Weak as evidence: the customer is a business buying a service; no
   filing shows customers asking for Cintas by name.
8. **Would the customer still choose it over the low bid?** **[M2017-009]**. **Contrary evidence** **[M1997-127]**: the
   rivals call uniform rental "a price-sensitive service" (Vestis 10-K FY2025, Risk Factors) and name price among the "main
   sources of differentiation" (UniFirst 10-K FY2025); the filer itself lists price among its competitive elements and
   warns that "our customers and prospects may decide to perform certain services in-house" (10-K FY2026, Item 1A).
   Against it: Cintas grows faster than all three rivals while earning about three times their margin, which is not what
   a low-bid market does to its highest-margin seller **[M2000-031]**.
9. **Ask the competitors** **[M1999-130]**, **[M2022-021]**. UniFirst's board, controlled by the founding family, rejected
   Cintas at $255 (2022) and $275 (2024 and 2025) a share and asked for "very high $300s", then accepted $155.00 in cash
   plus 0.7720 Cintas shares in March 2026, partly so that its holders could "participate in the future growth of
   Cintas" (S-4, Background and Reasons). Vestis names Cintas and UniFirst as its "notable competitors of size".
10. **Widening or narrowing?** **[M1999-108]**, **[L2005-010]**. Widening, on the competitor row: in FY2009 to FY2010
    Cintas's rental segment and UniFirst earned about the same margin (about 13% each); by FY2025 Cintas earned 23.5%
    against UniFirst's 7.6% and Vestis's 2.4%.
11. **What could destroy, modify or reduce it, five to fifteen years out?** **[M2000-014]**. Customers doing the work
    in-house; a rival with money accepting a lower margin to buy share (the umbrella of test 6); labor (about 800 of
    48,100 employee-partners in unions; the filer names "union organizing activities" among its risks); and the FTC,
    whose second request on the UniFirst merger shows a regulator examining how concentrated the field is (8-K of
    2026-10-06). None is shown by the filings to be under way against Cintas; in-sourcing is named by every filer and has
    not stopped growth.

**The field's returns over the last full cycle** (section C). The durable players do not all earn ordinary returns:
UniFirst earns ordinary returns (about 9% before tax on its capital in FY2025, margins 6.0% to 13.7% across the span),
Aramark's segment and Vestis earned less, and Cintas earns about 36% before tax on all its capital and far more on its
tangible capital. The castle protects excellent returns for one player, not ordinary returns for the field, so the
"standing castle that protects only ordinary returns" does not apply. **The change for the better** (Cintas's rental margin
from about 13% to 16% in FY2008 to FY2013 to about 24% now) is credited only on a full cycle in which the price behaviour
held **[M2005-020]**, **[L1995-022]**: it held through the FY2019 peak, the COVID downturn of FY2020 to FY2021 (rental
segment margin 17.8% and 21.5%; gross margin 45.9% to 47.6% on "certain cost control measures", 10-K FY2021) and the
inflation of FY2022 to FY2025 (above). One full cycle and one inflation, both passed with the margin held and then raised.
Credited. The earlier downturn (FY2009 to FY2010) cost the rental segment about three points of margin (15.9% to 13.1%)
while revenue fell about 10% over two years (from $3,937.9M in FY2008 to $3,547.3M in FY2010, all segments); it did not
reach a loss.

- **VERDICT: IN.** The castle stands on the evidence: an attacker with money (Aramark) failed over the whole span
  **[M2011-015]**, the leader passed inflation through while its rivals' margins fell **[M2005-017]**, and the gap is
  widening **[M1999-108]**. Contrary evidence carried forward: the filer does not state the advantage it enjoys; price
  matters in the field; and the widening margin is the opposite of the low-cost operator's habit **[L1996-016]**, which
  leaves room under the umbrella. These are weighed at Q7 in how sure the cash is **[M1999-104]**, not here.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, read on tangible assets with goodwill set aside
  **[M2011-060]**. Capital employed (equity plus debt less cash, which equals the net operating assets) and operating
  income, $M, from the filed balance sheets and income statements (XBRL company facts, latest-filed vintage):

  | Fiscal year | Operating income | Capital employed | Pre-tax return on it | Goodwill and intangibles in it | Pre-tax return on the rest |
  |---|---|---|---|---|---|
  | 2016 | 781.7 | 2,998 (1,843 + 1,294 - 139) | 26% | 1,354 | 48% |
  | 2021 | 1,385.5 | 5,736 (3,688 + 2,542 - 494) | 24% | 3,633 | 66% |
  | 2026 | 2,606.5 | 7,279 (5,140 + 2,428 - 289) | 36% | 3,921 (goodwill 3,544, service contracts 288, noncompete and other 89) | about 78% |

  The incremental return, FY2016 to FY2026: operating income up $1,825M on capital employed up $4,281M, 43% before tax,
  with the G&K Services purchase ($2,102M cash in FY2017) inside the added capital. FY2021 to FY2026, with no large deal:
  up $1,221M on $1,543M, 79% before tax. The cautions the rows require **[L1994-009]**: not a cyclical peak (the return
  rose through the COVID downturn, Q2); not leverage (debt is about one times operating income, Q9); not a return made by
  shrinking equity **[M1998-017]** (the measure above counts debt and equity alike, so buybacks do not flatter it).
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**. Capital spending ran $395.1M in FY2026
  against depreciation of $318.6M (1.24 times), and 0.97 to 1.46 times depreciation over FY2022 to FY2026. The filing
  does not split maintenance from growth. My guess, owed to the owner as a guess **[M2000-144]**: maintenance is about the
  depreciation charge **[L2000-035]**, since depreciation grew in step with revenue and the filer describes the spending
  above it as "ongoing investments in technology, capacity and talent" (press release of 2026-09-23). Two further
  reinvestments sit inside operating cash, not capex: the rental garments in service (up $137.6M in FY2026) and the
  capitalized sales commissions (up $29.4M net). Acquisitions of route businesses ran $46M to $233M a year. The profit
  ends the year as cash **[M2008-036]**: operating cash exceeded net income in every year of the window (Q4).
- **The growth arithmetic** **[M2001-019]**, **[M1998-081]**. Revenue grew organically 8% to 12% a year in FY2022 to
  FY2026, while capital employed grew about 5% a year (FY2021 to FY2026) and operating income about 13%. Growth here adds
  value: each added dollar of capital has earned far more than its cost **[L2009-012]**. The cap: owner cash grew 11.1%
  a year over the window (Q7), above the 5.64% discount rate, so it may be carried only for the ten years and not after
  **[M1997-095]**; at 11% for ten years the cash about trebles, on a revenue base of $11.3B, which does not run into an
  absurdity against an economy-sized limit **[M1999-067]**, but it does assume the margin holds at 23% to 24%.
- **WEIGHS FOR.** A business that earns very high returns on the tangible capital it needs and has earned more on the
  capital it added, the second-best kind of business in **[M1998-081]** and close to the best: "high returns on capital"
  with modest "incremental investment to grow" **[L2009-012]**.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them, before the income account** **[M2025-032]** (`tools/run.py`'s ten-year table,
  first-filed XBRL vintage, checked against the FY2026 filed balance sheet; $M):

  | Year-end (May 31) | Assets | Equity | Cash | Receivables | Inventory | Goodwill | Intangibles | Long-term debt | Retained earnings |
  |---|---|---|---|---|---|---|---|---|---|
  | 2018 | 6,958 | 3,017 | 139 | 805 | 280 | 2,847 | 546 | 2,535 | 5,838 |
  | 2019 | 7,437 | 3,003 | 97 | 910 | 335 | 2,842 | 495 | 2,538 | 6,691 |
  | 2020 | 7,670 | 3,235 | 145 | 870 | 409 | 2,870 | 761 | 2,540 | 7,297 |
  | 2021 | 8,237 | 3,688 | 494 | 902 | 482 | 2,913 | 720 | 1,643 | 7,877 |
  | 2022 | 8,147 | 3,308 | 90 | 1,006 | 472 | 3,043 | 719 | 2,484 | 8,719 |
  | 2023 | 8,546 | 3,864 | 124 | 1,153 | 507 | 3,056 | 701 | 2,486 | 9,597 |
  | 2024 | 9,169 | 4,316 | 342 | 1,244 | 410 | 3,212 | 690 | 2,026 | 10,618 |
  | 2025 | 9,825 | 4,684 | 264 | 1,417 | 447 | 3,400 | 694 | 2,425 | 11,798 |
  | 2026 | 10,529 | 5,140 | 289 | 1,555 | 446 | 3,544 | 707 | 1,429 | 13,074 |

  Plus the FY2017 balance sheet (assets 6,844, goodwill 2,782, equity 2,303, debt 2,771 + 363 current) as the year G&K
  came in, and FY2016 (assets 4,099, goodwill 1,276, equity 1,843). **What moved and why.** Goodwill jumped once, by
  $1.5B in FY2017 (G&K Services), and since then has grown only by small route purchases ($3.54B now); "intangibles"
  in the table is the XBRL finite-lived figure and includes capitalized contract costs, which are commissions, not
  purchased assets. Equity has grown slowly ($3.0B to $5.1B in eight years) while retained earnings grew from $5.8B to
  $13.1B: the difference is treasury stock of $10.9B, bought back. Debt has been held flat at about $2.4B to $2.8B gross for
  nine years while operating income more than doubled. Receivables grew with revenue (13.2% of the year's revenue in FY2019, 13.8% in
  FY2026, against revenue of $6,892M and $11,265M), roughly steady. Inventory built in FY2022 to FY2023 (supply chain) and was worked down in FY2024. "What the
  figures are saying and what they don’t say" **[M2025-032]**: they say a business that funds its growth, its purchases,
  a rising dividend and large buybacks from its own cash with flat debt; they do not say what part of the margin is
  price and what part cost (Q2), and the rental garments in service ($1.28B, current assets) are an estimate of
  useful lives (18 to 60 months) that the filer names as a critical estimate.
- **The real costs.** Depreciation is charged and is roughly the stand-still spending (Q3) **[R1996-023]**. Stock pay is
  expensed ($128.1M in FY2026, about 6% of net income) and is deducted again below in owner cash **[L2015-003]**; options
  still outstanding are a further cost in shares (options exercised in FY2026: 2,054 thousand shares). No recurring
  "one-time" charges: the only charge set apart in FY2022 to FY2026 is the UniFirst transaction expense ($15.1M in
  FY2026, $14.4M in Q1 FY2027); the FY2025 gain on property ($19.3M) is disclosed and was not featured. Insurance
  reserves (workers' compensation, auto) are self-insured and actuarially estimated, a real and disclosed estimate.
  EBITDA appears in the filer's mouth only as a debt covenant and a rating ratio (10-K, Liquidity), never as earnings.
- **Owner cash after every real cost** (operating cash less stock pay, capital spending net of property sales, and
  acquisitions; operating cash already bears the garments and the commissions; operator rule 5, no net-income proxy;
  $M): FY2022 1,023.4; FY2023 1,105.1; FY2024 1,355.2; FY2025 1,419.8; FY2026 1,588.6; five-year average 1,298.4. Before
  interest (after the company's tax on it), the all-equity basis of Q7: 1,096.5; 1,192.3; 1,430.8; 1,496.2; 1,669.4;
  average 1,377.0. Net income over the same years was $1,235.8M to $2,000.0M; owner cash runs at about 80% of net income,
  the gap being acquisitions and stock pay (script `q7_value.py`, output `q7_value_output.txt`).
- **The tells.** None in the accounts: no prepaid or deferred accounts building out of line (prepaid and other current
  assets rose to $286.2M from $170.0M in FY2026; they include $96.0M of the current portion of capitalized commissions and
  the $5.2M bridge-loan fee; the rest is not itemized in the parts read, a small gap declared), inventories in line with sales after FY2023, no reserve releases found,
  stock pay expensed **[L2002-039]**. **The habits carried to Q5** (section A of the gaps case): full-year guidance given
  and raised each quarter (press release of 2026-09-23 raised its revenue and adjusted-EPS guidance) **[L2019-006]**;
  an adjusted EPS featured beside GAAP, though the adjustment is only the UniFirst transaction expense and is reconciled
  **[L2016-006]**; and the incentive plan pays on "adjusted diluted EPS" against a declared target (proxy, Q6). Recorded
  as a WEIGHING against **[M1994-018]**.
- **VERDICT on the accounts: IN; WEIGHS FOR** on clarity, with the guidance and adjusted-EPS habit weighing against and
  carried to Q5. The accounts confuse nothing material **[M1995-063]**: the one unusual treatment (garments as a current
  asset) is stated and its cash is inside operating cash. The recast earnings feed Q7.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**. How well they run the business against the hand dealt: the same industry, the
  same customers, and a margin that went from par with UniFirst (about 13% in FY2009 to FY2010) to three times
  UniFirst's and ten times Vestis's (Q2). How they treat the owners: a family-founded company whose executive chairman
  (Scott D. Farmer, chief executive July 2003 to May 2021) holds 14.0% of the shares
  (56.0M shares, proxy of 2026-09-15, Principal Shareholders), so management's gain-loss equation is largely the owners'.
- **The proxy** **[M1994-009]**. Chief executive Todd M. Schneider (with Cintas since 1989, CEO since June 2021): fiscal
  2026 cash incentive paid $2,766,430; long-term equity target $7,888,917, half on diluted EPS and half on sales growth;
  EPS goals threshold $4.48, target $4.72, maximum $5.05, achieved "between Target and Maximum" on adjusted diluted EPS
  of $4.94. Perquisites "minimal" (automobile allowance, executive medical). Say-on-pay approved by about 95% in 2025.
  The executive chairman's pay was redesigned in fiscal 2025 to a $750,000 salary and a restricted-stock retainer, no
  incentive plan. Related-person transactions: a 25% share in an airplane owned with a Farmer family entity since 2006,
  each party paying its own use (Cintas was reimbursed $4,592,003 in fiscal 2026), and $592,965 of Cintas services sold
  to a car dealer owned by a brother-in-law of Mr. Farmer and of director Robert E. Coletti. Both disclosed and
  committee-approved; neither is large against $11.3B of revenue.
- **The letters and reports** **[M1998-036]**, **[M2007-083]**. The 10-K is plain and complete on the items an owner needs
  (segments, buybacks with average prices by programme, debt, the garment accounting). The press release is the IR
  department's product, with guidance and an adjusted figure (Q4).
- **The habits carried from Q4, read with the integrity record.** Guidance given and raised, an adjusted EPS figure that
  differs from GAAP only by the deal costs, and incentive targets on adjusted EPS. Weighed against the rows: "we become
  downright incredulous if they consistently reach their declared targets" **[L2002-041]**, and predictions "corrode CEO
  behavior" **[L2000-039]**. Read with the rest of the record (accounts with no tells, every adjustment reconciled and
  small, owner-family control, plain 10-K), they do not raise a doubt about honesty **[M2013-088]**; they are a weight
  against, carried to Q6 Part B on what the pay rewards.
- **Integrity record searched.** The FY2026 10-K reports only ordinary-course legal proceedings (Item 3); no
  investigation, restatement or material weakness appears in the FY2022 to FY2026 10-Ks read; the S-4's account of the
  UniFirst talks shows Cintas withdrawing in 2025 rather than meeting a price and covenant it would not accept, and
  returning publicly at the same $275 (S-4, Background), conduct that is "realistic as to price" rather than a deal
  pursued at any price. Gaps declared: litigation older than the FY2008 10-K was not read.
- **Love of the business and ability.** A chief executive who joined the company in 1989 and an executive chairman who
  joined in 1981 and holds 14% **[M2000-098]**; ability shown in the record against the hand dealt **[M1994-008]**, and in
  the capital returns of Q3.
- **VERDICT on integrity: IN** (no doubt raised by the record **[M2013-088]**); **ability WEIGHS FOR** **[M1994-008]**.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test** **[R1995-009]**, **[M1998-110]**. Earnings kept over FY2021 to FY2025 (the rise in retained earnings, $7,297M at
  2020-05-31 to $11,798M at 2025-05-31) were about $4.5B; the market value of the stock held by non-affiliates went from $37.3B at 2020-11-30
  ($355.30 a share before the split, $88.83 after) to $74.4B at 2025-11-30 ($186.02) (10-K covers FY2021 and FY2026),
  while buybacks retired shares at the same time. The market leg passes by a wide margin. The intrinsic leg
  **[R2009-002]**: owner cash grew 11% a year (Q4), so value per dollar kept rose as well. Passes.
- **Buybacks** **[L1999-023]**, **[L2011-003]**. $952.1M in FY2026 (3,960 thousand shares at an average of $196.38 under the
  programmes, plus 829 thousand shares withheld for employees' taxes at $210.50), $934.8M in FY2025 (average $179.07),
  $48.4M after year-end to 2026-07-29 at $199.70, and $544.7M in Q1 FY2027 to 2026-09-22 (price not yet filed). Every
  programme is a fixed dollar authorization "for $1.0 billion" with no expiration and no stated price (10-K, MD&A)
  **[L2016-002]**. By the run's convention (Q6, the buyback with no stated price), the prices paid are set against the
  bottom of the Q7 range, $55.53 to $65.69 a share all-equity (Q7): every average price paid since FY2025 is about three
  times that bottom and above the top of the range ($141.17). **Weighs against.**
- **Issuance and deals** **[M1995-001]**, **[L2014-012]**. *G&K Services* (agreed August 2016, closed March 2017): $97.50
  a share in cash, $2,102M net cash paid in FY2017, 14.0 times trailing adjusted EBITDA (S-4's precedent table), financed
  with debt; afterwards the rental segment's margin rose from 17.8% (FY2016) to 21.7% (FY2022) with G&K inside it, and debt
  was not added to afterwards. Value got appears to have exceeded value given on the later record. *UniFirst* (agreed
  2026-03-10, pending): $155.00 cash plus 0.7720 Cintas shares a UniFirst share, about $5.5B in all, 14,261,683 new
  Cintas shares (3.4% of the combined), $2.85B bridge commitment, $350.0M termination fee payable by Cintas in certain
  cases (10-K and S-4). Value given against value got, on the filed records and with no synergies counted
  **[L2016-008]**: UniFirst's own owner cash before acquisitions averaged $66.2M a year over FY2021 to FY2025 and its
  operating income was $184.5M in FY2025, against cash of about $2.86B plus shares worth about $2.8B at today's price.
  On the standalone record Cintas gives more than it gets **[L1994-015]**; the case for the deal rests on running
  UniFirst's routes at Cintas's margins, which is a synergy. **The one STOP** **[L2009-019]**: not met; the deal is part
  cash, and the stock given is, on this run's Q7 range, above its value, not below. Weighs against.
- **Dividends and the order of uses** **[L2012-011]**: reinvestment and route purchases first, then dividends ($701.5M
  paid FY2026, raised each year), then buybacks; debt held flat. Clear and consistent **[L2012-015]**.
- **Part B, pay tied to what the person controls** **[M2003-019]**. The plan pays on adjusted diluted EPS and sales growth
  with no charge for the capital used **[L1994-019]**, so buybacks and debt-financed purchases raise the measured result;
  options carry no step-up for retained earnings **[L1994-021]**. Owner alignment is strong through the founding family's
  14%, and the executive chairman takes no incentive pay. The board: eight nominees, the executive chairman and his
  brother-in-law among them; the chief executive is not the chairman **[L2014-026]**. The proxy also asks holders to move
  the company's domicile from Washington to Delaware (Item 4) and carries a holder proposal on majority voting (Item 5);
  noted, not weighed.
- **Part A: WEIGHS AGAINST** (buybacks at prices above the whole Q7 range, and a large deal whose value rests on synergies)
  **[L2011-003]**, **[L2016-008]**. **Part B: UNDECIDED** (EPS-based pay without a capital charge **[L1994-019]**, against
  a family owner with 14% and a non-incentive chairman **[M1994-009]**).

## Q7: WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**, **[M1996-025]**, held as a range
**[L2000-024]**, **[L1999-027]**. Construction: the CONVENTION of Q7 and its specifics as written in the framework, nothing
added. Arithmetic in `q7_value.py`, output `q7_value_output.txt` (working folder). Rate 5.64% (Step 0); price $196.98;
400.17M shares.

- **The cash** (Q4's recast; five-year window FY2022 to FY2026, $M). All-equity basis (owner cash before interest, after
  the company's tax at its own effective rate, 17.5% to 20.4%): all spending including acquisitions 1,096.5 / 1,192.3 /
  1,430.8 / 1,496.2 / 1,669.4, average **1,377.0**; maintenance-only (operating cash less stock pay less depreciation as
  the maintenance guess of Q3, no acquisitions) average **1,606.4**; acquisitions left out but all capex charged, average
  1,536.0. Equity-only basis (after interest): 1,298.4 / 1,527.8 / 1,457.4.
- **The six specifics, applied.** (a) *Cycles*: neither end year is described by the filer as a peak, trough or
  aberration; FY2022 carried "the positive impact from the lifting of COVID-19 restrictions" (10-K FY2022) but is a
  recovery year inside a rising series, not a trough. Literal window used; it is the window shown **[L2005-003]**. (b)
  *Decline*: none; the series rises every year. The growth shown, on aggregate owner cash: **11.08%** a year FY2022 to
  FY2026 (all-equity, all spending); 11.42% on the first-half and second-half averages, which agrees. (c) *Acquisitions*:
  deducted, total growth credited (the default) **[M1998-080]**, **[M2014-068]**, **[M2023-081]**; the organic pair beside
  it uses owner cash before acquisitions and the filer's organic revenue growth, 12.2%, 8.0%, 8.0% and 8.3% in FY2023 to
  FY2026, compounding to about 9.1% a year (organic revenue growth stands in for organic cash growth; said so). The pending
  UniFirst merger is neither inside the window nor closed, which the specifics do not cover: CONVENTION of this run,
  rationale: the deal is signed and its financing is committed but it may yet be blocked, so it is shown beside the
  central range, never inside it (below). (d) *Working capital*: inside operating cash (garments, receivables,
  commissions), so charged. (e) *Growth spending*: the filing allows the maintenance guess (Q3), so the central range runs
  from the maintenance-only case at no growth to the all-spending case at the growth that spending bought **[M2000-144]**,
  **[L1999-024]**; the default pair is shown beside. (f) *The cap*: 11.08% is above the 5.64% rate, so it is carried for
  ten years only and then at zero nominal growth **[M1997-095]**; no absurdity results inside the ten years (Q3)
  **[M1999-067]**.
- **Net debt** (all-equity basis): senior notes at face $2,436.6M less cash $289.0M at 2026-05-31, plus the $48.4M of
  buybacks the 10-K states after year-end: **$2,196.0M**. Operating leases ($277.9M) left out, said so. "Investments"
  ($438.7M) are the cash surrender value of insurance policies (10-K, Note 1), not cash, and are left out. The UniFirst
  financing is not incurred and is not added (it enters only the combined line).

**Value range, central, all-equity basis: $65.69 to $141.17 a share against $196.98.** Width 2.15 to 1.

| Case (all-equity unless marked) | Range a share | Width | Expected return at $196.98 |
|---|---|---|---|
| **Central (e)**: maintenance-only, no growth / all spending at 11.08% for ten years | **$65.69 to $141.17** | 2.15x | 2.0% to 4.3% |
| Default (c): all spending, no growth / at 11.08% | $55.53 to $141.17 | 2.54x | 1.7% to 4.3% |
| Organic pair: before acquisitions, no growth / at 9.1% | $62.57 to $134.47 | 2.15x | 1.9% to 4.0% |
| Equity-only, central (e) | $67.69 to $144.25 | 2.13x | 1.9% to 4.3% |
| Beside only: combined with UniFirst on its filed record, no synergies **[L2016-008]**, cash paid $2.86B added to net debt, 14.26M shares added | $59.86 to $132.74 | 2.22x | not computed |

The literal window is the window used (no cycle base was needed), so the literal figures are the figures above. What the
price needs: at the 5.64% rate the price is reached only if owner cash grows about **15.2% a year for ten years** and then
holds; at the 10% floor it needs about 25.3% a year. Owner cash has grown 11.1%.

**How sure** **[M1999-104]**. The castle of Q2 is the reason the range is as narrow as it is; the contrary evidence of
Q2 (an unstated advantage, a price-sensitive field, a margin umbrella) argues for the lower half, not the upper.

**Closes** (the CONVENTION's two closes and the floor). The range is narrower than about three to one, so it is not TOO
HARD **[L2000-025]**. The price is above the top of every case. By the floor (about ten percent pre-tax, on owner cash
after the company's own tax, before the holder's tax **[M1994-004]**, **[L2002-020]**, **[M2003-149]**), the expected
return at the price is 2.0% to 4.3%, below the floor and below the 5.64% government bond itself: "there’s just a point at
which we drop out of the game" **[M2003-149]**. A price above the top of the range closes OUT however wide the range
(specific (f)).

**Fair price (a reporting figure, never a verdict; Part VII):** **$51.72** a share, all-equity basis (central), the price at
which the midpoint of the central range (the average of its two end streams) earns the floor of 10%, after the company's
own tax, net debt deducted; **$55.46** on the equity-only basis beside it. The default pair gives $48.86 (all-equity) and
$52.60 (equity-only); the combined-with-UniFirst line $45.14. No cheap price is reported.

- **VERDICT: OUT.** The price, $196.98, sits above the top of the range, $141.17, and the expected return at that price
  is below the floor and below the bond **[M2003-149]**; this is not a screamer but its opposite **[M2009-005]**.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (the file closed at Q7).

## Q9: COULD IT RUIN US? WEIGHING.
NOT REACHED.

## Q10: IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7** (price above the top of the value range): central range **$65.69 to $141.17** a share (all-equity; $67.69
to $144.25 equity-only) against **$196.98**; fair price $51.72 all-equity, $55.46 equity-only. Q1 IN, Q2 IN, Q3 weighs for,
Q4 IN, Q5 IN on integrity, Q6 weighs against (Part A) and undecided (Part B). No integrity facts were found that a later
question must answer (Q5 was reached and answered).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down under the question each bears on, not weighed; the box is unchanged; operator rule 2.)* **[M1997-127]**
- **Q8, the bond:** the 30-year Treasury yields 5.64% (2026-10-06); the expected return at the price in every case of Q7
  is 1.7% to 4.3%.
- **Q9, debt and exposures:** senior notes $2,436.6M at face: $1,000M at 3.70% due in fiscal 2027 (current at
  2026-05-31; issued 2017), $400M at 4.20% due 2028, $800M at 4.00% due 2032, $236.6M at 6.15% due 2037. No commercial
  paper or revolver drawings at 2026-05-31; revolver $2.0B to 2031-03-27, of which $1.25B is held under "certain funds"
  for the UniFirst deal; a $2.85B 364-day bridge commitment (one tranche since replaced by the revolver); the 10-K expects
  "approximately $2.8 billion in additional indebtedness" for the deal. Ratings A- (S&P) and A3 (Moody's), stable.
  Pre-tax income over net interest in FY2026: $2,505.3M over $101.2M, about 25 times. Covenant on debt to EBITDA;
  cross-default provisions. Termination fee of $350.0M payable by Cintas in certain cases. Operating leases $316.5M
  undiscounted. Self-insured workers' compensation, auto and general liability, with $125.8M of standby letters of
  credit and surety bonds. (10-K FY2026, MD&A Liquidity and Notes 6 and 7.)
- **Q10:** nothing beyond Q7.
- **Q12:** uniform, mat, restroom, first aid and fire services; no business of the kinds the rows name **[M2008-011]**.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. **Departure declared:** Step 0, Q1 and Q2
      were committed one at a time; Q3 to Q6 were written after the session limit reset and committed together in one
      commit (`fa5c4f55`); Q7 to the end in the next.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock was held by the dispatching session (read at
      start: "interactive v5 re-runs batch 4"). The fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under CONTAMINATION at the top and was not used.
- [x] Every v5 id resolves and every quoted fragment beside an id is in that row (`check_cites.py`, run on the finished
      file); no E-ids. Every filing fact carries its accession or names its document.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 are NOT REACHED, facts after the stop
      written down, not weighed.
- [x] Owner cash after every real cost from operating cash (stock pay, capex and acquisitions deducted), never a net-income
      proxy; sovereign from the U.S. Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations, Q2 tests 1, 6 and 8, Q4, Q6).
- [x] No row dated after the anchor: not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used; its D&A line was split into depreciation and amortization by
      hand, and its capex line was supplemented by the garments and commissions inside operating cash (Step 0).
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the commit message).
- Gaps: the Q1 FY2027 10-Q was not yet filed, so the price of the $544.7M of buybacks since June is unknown; Cintas
  litigation before FY2008 was not read; UniFirst's FY2026 10-K (year ended about 2026-08-29) was not yet filed; Alsco
  and Elis could not be put in the competitor row.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A signed, unclosed merger has no rule.** Q7's specific (c) covers a merger inside the window and a deal "closed
after the window and before the price date"; the brief says "a merger is valued on the combined companies' averages".
UniFirst is signed, approved by its holders and financed, but not closed and under an FTC second request. I kept it out
of the central range and showed the combined figure beside it, as a CONVENTION of this run; a rule is owed, since here the
combined line lowers the top of the range by about $8. (2) **"The literal window shown beside"** has nothing to show
when no cycle base is used; I said so. (3) **The maintenance-only no-growth case and the acquisitions default** (specifics
(c) and (e)) give two different bottoms ($65.69 and $55.53); the text makes (e) central "where the filing allows the
guess" and (c) "the default pair", without saying which bottom is the range's bottom for Q6's buyback test. I used (e) as
central and gave both. (4) **Q2's "low-cost operator" exception** assumes the filings can separate cost from price; for
a service business they cannot, and the rows' own picture of the low-cost operator (one that passes the saving on)
**[L1996-016]** fits a margin-widening leader badly. The framework gives no way to read a castle that shows as high margin
and high growth together. (5) **The fair price's "midpoint of the range"** is ambiguous between the midpoint value and
the midpoint stream; I used the average of the two end streams discounted at the floor, stated.

**Errors in the brief, as dispatched** (the dispatching message said to assume one): (a) it lists "capital spending on
rental garments and trucks against depreciation" as a line of evidence; at Cintas rental garments are not capital
spending at all but a current asset ("Uniforms and other rental items in service") amortized over 8 to 60 months, with
the purchases inside operating cash (Step 0). A run that added garments to capex would double-charge them. (b) It asks for
"route density and the route-based cost advantage as the filer describes it"; the filer does not describe either in its
10-K or the S-4 (no instance found by text search); only a rival (Vestis) uses the phrase. (c) It calls UniFirst "any
later large offer"; it is a signed merger agreement of 2026-03-10, approved by UniFirst's holders on 2026-06-12, with
Cintas shares in the consideration, which is what brings it under Q6's issuance test and Q7's merger specific.
(d) Minor, in the filing rather than the brief: the S-4's Background dates Elis's 2024 proposal "September 27, 2026",
evidently a typing error for 2024 (the same sentence ties it to the price of 2024-09-26); flagged, not smoothed.
