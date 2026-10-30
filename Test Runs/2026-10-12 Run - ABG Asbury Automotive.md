# Company Run — Asbury Automotive Group, Inc. (NYSE: ABG) — 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

Dispatched blind run under `Screens/_daily/_dispatch_brief.md` (operator rule ten). Analyst's research folder:
`Test Runs/_research 2026-10-12 ABG/` (notes, fetch script, field-returns script and output, the Q7 script; raw filings
under the ignored `cache/`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**Contamination, declared:** a directory listing of `Test Runs/` made to check that this run's file name was free showed the
names of other run files and research folders dated 2026-10-12 (ADRZY, BOOM, BOUYF, CLIR, DPMAY, DSGR, EOSE, EQPT, EVI, FAST,
FSRDQ, GIC, HTOO, SUNB) and an addendum title; none concerns this company, none was opened, nothing in them was used. The
session's start-up context showed recent commit subjects about HTOO and GIC and the memory index lines (a count of
"gate-clearers" and that nothing is buyable); no line names ABG and none was used. No ABG file of any date was looked for
or seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $165.28 a share (2026-10-12 quote; aggregator, live quote only, flagged per operator rule 5; printed by
  `tools/run.py`). The 10-K's Item 5 gives $229.78 as the NYSE close of 2026-02-18, so the quote is about 28 percent lower
  than eight months ago.
- **Shares by class** from the latest filing's cover: one class, common stock $0.01 par, **17,951,917** shares (10-Q for the
  quarter ended 2026-06-30, filed 2026-07-31, accession `0001144980-26-000094`; `python Screens/cover_shares.py ABG`).
  Check: the 10-K balance sheet at 2025-12-31 shows 41,338,419 issued less 22,109,690 in treasury = 19,228,729; the 10-Q
  records 1,346,359 shares bought and retired in the first half of 2026 (19,228,729 less 1,346,359 = 17,882,370, the rest
  being award issuance net of net-share settlement), consistent with the cover; no 8-K since the 10-Q (accessions
  `0001144980-26-000096`, `-000098`, `-000100`, all officer changes) reports an issuance. One class; no charter note.
- **Market cap:** $165.28 x 17.952M = **$2,967M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, 30-year par yield, US Treasury daily par yield curve, 2026-10-09
  (`python tools/sources.py`; the issuing authority).
- **Filings read** (operator rule 4): the 10-K for FY2025 (filed 2026-02-20, accession `0001144980-26-000051`), Items 1,
  1A, 3, 5, 7, 8 and notes 3, 10, 14, 18, 20, 21; the 10-Q for Q2 2026 (accession `0001144980-26-000094`); the proxy
  (DEF 14A filed 2026-03-24, accession `0001144980-26-000070`); the 8-Ks since the 10-Q (above) and the Q2 earnings 8-K
  (`0001144980-26-000089`, cover only; the release exhibit was not opened); for the cycle, the 10-Ks for FY2024
  (`0001144980-25-000077`), FY2022 (`0001144980-23-000080`), FY2021 (`0001144980-22-000079`), FY2019
  (`0001144980-20-000059`), FY2016 (`0001144980-17-000063`) and FY2013 (`0001144980-14-000010`, selected data 2009 to 2013).
  **Lines of evidence chosen (the brief's slot):** Item 1 (the franchise system, competition, acquisitions and
  divestitures), Item 1A (manufacturer dependence, electrification and autonomy, debt, the FTC matter, impairments), Item 7
  (results by line, the floor-plan cash-flow classification and the filer's adjusted operating cash flow, capital spending,
  buybacks, impairments).
  **One figure cross-checked against the filed statement:** net cash from operating activities for FY2023, $313.0M in the
  cash-flow statement of the FY2025 10-K, equals the $313M `tools/run.py` transcribes from XBRL; total equity at 2025-12-31,
  $3,891.9M filed, equals the transcribed $3,892M.
- `python tools/run.py ABG`, arithmetic lines only (its v4 rule text, ids and floor ignored, Part VII): OCF as filed 2021
  $1,164M, 2022 $696M, 2023 $313M (2024 $671.2M and 2025 $775.2M from the filed statement); SBC 2021 to 2025 $16M, $21M,
  $24M, $27M, $28M; capital spending as tagged 2021 to 2023 $74M, $95M, $142M (the tool's window stops at 2023 because the
  capex tag changed; the later years were read from the filed statements). **The as-filed OCF is not owner cash for a
  dealer**, and the tool's three-year mean is not used: new-vehicle inventory runs through operating cash while most of the
  floor-plan debt that funds it is classified as financing (10-K FY2025, Item 7, "Classification of Cash Flows Associated
  with Floor Plan Notes Payable"), so 2021's $1,164M is inventory sold down in the chip shortage and 2023's $313M is
  inventory rebuilt. Owner cash is recast at Q4.

## THE FOUNDATIONS (not a gate)
The share is read as a business: would I be content to own this "if the market closed for five years" **[M1997-109]**; a
dealer group is a plain business whose cash can be pictured, so the test can be put. The quotation has fallen about 28
percent since February; that tells nothing, "It just tells us prices." **[M2006-077]**. No macro view enters: tariffs,
affordability and interest rates are read only as they show in the business's own units and margins **[M2000-094]**. The
margin-of-safety attitude is carried to Q7: if it needs pencil and paper "it’s too close to think about" **[M1996-084]**.
Who is paid to tell me: the filer's featured measures (adjusted operating cash flow, "transaction adjusted net leverage") are
read against the GAAP lines they reconcile to. **Contrary evidence, written down as found** **[M1997-127]**: (1) the
dealer's moat is lent, not owned: the manufacturer grants the franchise, sells new vehicles to every same-brand rival on the
same terms, can demand facility spending, and may terminate under the framework agreements (10-K Item 1, "Competition" and
"Dealer and Framework Agreements"); (2) volume is falling now: same-store new units down 6 percent and same-store used retail
units down 14 percent in Q2 2026 against Q2 2025, same-store new-vehicle gross profit down 24 percent (10-Q
`0001144980-26-000094`, MD&A); (3) the FTC administrative proceeding over the sale of add-on products at three stores, filed
2024-08-16 and still pending (10-K Item 3; 10-Q legal note); (4) franchise-rights impairments of $117.2M, $149.5M and
$141.0M in 2023, 2024 and 2025 (10-K, Item 7, Critical Accounting Policies), on a franchise-rights balance built by the
acquisitions of 2020 to 2025; (5) a long-time speaker on this very business: "I don’t think I can tell you what the auto
industry will look like five or ten years from now" **[M2023-100]**.

## THE STANDING RULE
A part-interest bought in the market for cash, sized so that it cannot touch what the buyer has and needs, carries no
leverage that can call and no collateral; the buyer's ruin is not in the purchase as framed **[M2012-081]**,
**[L2014-005]**. Nothing about the target changes that; the target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from the filing.** 171 franchised dealership locations (223 franchises, 36 brands) and 39
  collision centers in 15 states, plus TCA, an in-house seller of service contracts and other vehicle-protection products
  sold through its own stores (10-K FY2025 Item 1). Gross profit in 2025: new vehicles 20.2 percent, used retail 7.8,
  wholesale 0.6, parts and service 47.9, finance and insurance 23.4 (10-K Item 7, gross profit mix). Brand mix of new-vehicle
  revenue: 40 percent import, 32 luxury, 28 domestic; Toyota and Lexus 30 percent of new-vehicle revenue (Item 1A).
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, and the product can stay ordinary if "I understand the economic dynamics of the
  industry" **[M2011-014]**. The key variables, named first as the rows ask **[M1998-044]**: (1) new and used units and the
  gross profit per unit; (2) parts-and-service gross profit, which is 48 percent of the total; (3) F&I per vehicle; (4) the
  franchise system itself, which sets who may sell and service a brand where. Each is reported every year, and their range is
  on the record through a severe trough: in 2009 the company still earned $90.9M from operations on $3.23B of revenue,
  $80.6M after floor-plan interest (10-K FY2013, Item 6, `0001144980-14-000010`), and in 2020 it earned more than in 2019
  (pre-tax $338M against $244M, XBRL of the FY2020 10-K `0001144980-21-000075`). The rows' foreseeability test is passed for
  (1) to (3) within a range: a local dealer sells and services the brands it holds; the car parc it services is old and
  growing older ("a historically high 13.0 years", 10-Q Q2 2026 MD&A); warranty and recall work must by manufacturer policy be
  done at a franchised dealer (10-K Item 1, Parts and Service).
- **The doubt, stated.** Variable (4) is the one that could change the economics: manufacturers selling direct
  ("certain electric vehicle manufacturers have been permitted to circumvent the state automotive franchise laws of several
  states", 10-K Item 1, Competition), electrification and autonomy (Item 1A). Is this a forecast about technology or about
  customers **[M2017-019]**, **[M2023-030]**? For the dealer it is mostly about law and about the brands it holds: the state
  franchise laws make termination or non-renewal unlawful without "good cause" and restrict a same-brand rival from
  establishing a store within the area served (10-K Item 1), and they have held for decades. The speaker who said he could
  not see the auto industry five or ten years out said in the same answer "We like our dealership operation" **[M2023-100]**;
  that is a row about one company and is weighed, not decisive (Q2, A row about one company). Retail is the field the rows
  warn is easy to think one understands **[M2014-052]**; the warning is taken by reading the dealer's own reported variables
  over seventeen years rather than its strategy text.
- **Is it important and knowable** **[M2006-076]**? The franchise-law question is important and, on the filings, knowable as
  a present fact; its ten-year durability is carried to Q2 test 11 as the castle's threat, not a reason the economics cannot
  be pictured. The doubt row **[M2002-092]** is answered this way: I do not doubt that a franchised dealer's ten-year
  economics can be pictured within a range; I doubt their level and their protection, which are Q2's and Q7's questions.
- Routing: not a fast-changing industry on the filings (the same four lines of business in the 2009 and 2025 statements);
  not a bank (it arranges finance and does not lend: "We do not directly finance our customers' vehicle purchases or leases",
  10-K Item 1); TCA, an insurance-like part, is read at Q2 under the parts paragraph.
- **VERDICT: IN.** The economics of a franchised dealer can be pictured ten years out within a range from the filer's own
  reported variables over a full cycle **[M2012-065]**, **[M1995-051]**; the franchise-law and direct-sales doubt is real
  and is carried to Q2 as the castle's main threat, not settled here.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**

- **The parts table** (10-K FY2025 note 20, Segment Information; segment operating income as the CODM measures it, after
  floor-plan interest and before impairments):

  | part | 2023 | 2024 | 2025 | share of three-year total | castle | decides |
  |---|---|---|---|---|---|---|
  | Dealerships | $955.9M | $816.7M | $858.6M | 92 percent | the franchised store: sale, service, F&I commission | **yes** |
  | TCA | $69.0M | $72.8M | $79.8M | 8 percent | a captive seller of service contracts through the company's own stores | no |

  The filer reports two segments only since TCA was bought in December 2021, so five years of segment profit do not exist;
  the three filed years are used and the share is so lopsided that the five-year figure could not change which part decides
  (CONVENTION of this run, confessed: three years in place of five where the segments have existed only three full years;
  rationale: the threshold is more than half, and Dealerships holds more than nine-tenths). The file closes on Dealerships
  **[L2008-005]**. TCA, which does not decide, is carried to Q7 inside the consolidated cash.

- **The castle questions: what keeps it standing, and how permanent** **[M1995-038]**. The reason a customer buys a Toyota
  or a Lexus from this store and not from a stranger is that only a franchised dealer may sell it new, the manufacturer
  appoints few of them, and the state franchise laws "restrict competitors from relocating their stores or establishing new
  stores of a particular vehicle brand within a specified area that is served by our dealership of the same vehicle brand"
  (10-K Item 1, Competition). Warranty and recall work must be done at a franchised dealer, and the technician
  certifications are the manufacturer's (Item 1, Parts and Service). These are reasons that have held for decades. They are
  also reasons the dealer does not own: the manufacturer grants them and sets the terms, "Our new vehicle store competitors
  also have franchise agreements with the various vehicle manufacturers, and as such, generally obtain new vehicle inventory
  from vehicle manufacturers on the same terms as us" (Item 1, Competition).

- **Would it stand without the lord** **[M1995-040]**? Stores are run by local general managers under 17 local brand names
  (Item 1); no superstar is named or needed. Against it, the rows' warning on retail, "In retailing, to coast is to fail."
  **[L1995-008]**, and the speaker on this very trade: "running dealerships well is a very good business. It’s a local
  business." **[M2015-011]**, which puts the weight on the running.

- **The money test** **[M2011-015]**. A rival with a large sum cannot open a new Toyota point beside this store: the
  manufacturer appoints and the state law protects the area (Item 1). He can buy existing stores, which is what this company,
  its listed rivals and a Berkshire subsidiary have done for a decade; the price of the stores then carries the rent, and
  the castle protects the store, not the buyer's return on what he pays for it (carried to Q3 and Q6). In used vehicles the
  rival is open to all comers: "companies with a primarily internet-based business model, such as Carvana" (Item 1A).

- **Pricing power and the agony before a rise** **[M2005-020]**. None in new vehicles: the filer says new-vehicle margins
  were "above historical levels" in and after the pandemic because of supply disruption and are now "softening"; same-store
  new-vehicle gross profit per unit fell 11 percent in 2025 (from $3,734 to $3,342) and same-store new-vehicle gross profit
  fell 24 percent in Q2 2026 on "affordability constraints" (10-K Item 7; 10-Q MD&A). The price of a new car is set by the
  manufacturer's invoice and by the same-brand rival a few miles away, the shape the rows call a rival who sets the price
  **[M2012-109]**. Parts and service is the other way: 2025 parts-and-service gross profit rose 9 percent all-store and the
  margin on it is high (2025 revenue $2,506.8M, gross profit $1,472.5M, Item 7).

- **Would the customer still choose it over the low bid** **[M2017-009]**? For a new vehicle of a given brand, no: the
  customer can buy the same car from any same-brand dealer, and "most insureds don't care from whom they buy" **[L2004-003]**
  is the right description of that line. For warranty work the customer has no low bid to take; for customer-pay repair
  the independents compete, more so as cars age (the 10-Q ties the fall in collision work to the "increasing trend of aged
  vehicles").

- **The low-cost position** **[L2004-007]**. No evidence of one: SG&A was 64.7 percent of gross profit in 2025 and 67.2
  percent in Q2 2026 (Item 7; 10-Q), and the speaker who owns the same trade says "There are not any huge advantages of
  scale, at least that I’m aware of, in owning lots of dealerships." **[M2015-011]**, **[M2015-078]**.

- **The competitor row** (same metric for each filer, from its own 10-K XBRL facts, transcription checked for ABG against the
  filed statements; pre-tax income plus non-floor-plan interest, that is earnings after floor-plan interest and before other
  interest, divided by net tangible capital = equity plus non-floor-plan debt less cash less goodwill less franchise rights;
  floor-plan debt is left with the inventory it funds; script and table in `Test Runs/_research 2026-10-12 ABG/field_returns.txt`):

  | filer (latest 10-K accession) | pre-tax return on net tangible capital, 2011-2019 average (low, high) | on total capital incl. purchased intangibles, 2011-2019 | margin 2011-2019 | 2021-2025 average, tangible | 2025, tangible / total |
  |---|---|---|---|---|---|
  | ABG (`0001144980-26-000051`) | 23.9% (16.1, 31.3) | 20.6% | 4.00% | 40.3% | 27.9% / 11.4% |
  | AutoNation (`0001628280-26-007800`) | 30.4% (24.1, 42.5) | 17.0% | 3.69% | 45.0% | 29.3% / 17.6% |
  | Group 1 (`0001031203-26-000064`) | 26.0% (20.2, 34.1) | 12.1% | 2.52% | 35.6% | 19.1% / 9.8% |
  | Lithia (`0001023128-26-000015`) | 23.4% (18.2, 27.1) | 18.2% | 3.79% | 19.5% | 12.8% / 8.6% |

  Lithia's figures after 2021 include an auto-finance arm whose non-recourse funding sits in its debt, so its later
  tangible return is understated against the other three (flagged; not adjusted). Sonic and Penske, also in the filer's peer
  index (10-K Item 5), were not read (the brief's limit of three). Carvana, named in Item 1A, has a different model and was
  not read.

- **The field's returns over the last full cycle, judged in words** (Q2, What it rules OUT, the standing castle that protects
  only ordinary returns). Over 2011 to 2019, a stretch from the recovery through the 2016 volume peak and the flat years
  after, every one of the four filers earned, every year, pre-tax returns on the tangible capital the business needs that sit
  in the twenties and thirties, and ABG stayed profitable at the operating line through the 2009 trough (above). Those are
  not ordinary returns; they are what a franchise point protected by law and by the manufacturer's appointment earns when it
  is run well **[M2015-011]**. On the total capital an acquirer has paid, goodwill and franchise rights included, the same
  years show lower figures (12 to 21 percent pre-tax), which is the rent capitalised into the price of the stores; that bears
  on the buyer of stores (Q3, Q6, Q7), not on whether the castle stands. The moat is judged, not measured **[M1999-108]**.

- **Widening or narrowing** **[L2005-010]**, **[M1999-108]**. The 2021 to 2023 returns were a supply shock, not a widening,
  and the filer says so; the 2025 returns are back inside the 2011 to 2019 band for ABG and AutoNation and below it for Group
  1 and Lithia. No change for the better is credited: none is needed for the verdict, and the rule credits one only on a full
  cycle **[M2005-020]**, **[L1995-022]**. Same-store volume is falling in 2026 (Q2: new units down 6 percent, used retail
  down 14 percent); that is the downturn the next full cycle will be read on.

- **Ask the competitors** **[M1999-130]**. No public answer to the silver-bullet question was found. Revealed preference
  only: each of the three rivals read has spent heavily buying more franchised stores over 2011 to 2025 (acquisition lines in
  their cash-flow statements, XBRL `PaymentsToAcquireBusinessesNetOfCashAcquired`), which says the insiders want more of
  this castle, not less; it is weak evidence and weighed as such.

- **What could destroy, modify or reduce it, five to fifteen years out** **[M2000-014]**. Three things, from the filer's own
  risk factors: (1) manufacturers selling direct or under agency terms, which the laws now limit and which "certain electric
  vehicle manufacturers" already do in several states (Item 1; Item 1A); if franchise laws were "repealed, weakened, or
  superseded by our framework agreements", the dealer would be "more susceptible to termination, non-renewal, or
  renegotiation" (Item 1A); (2) electrification and autonomy reducing service work (Item 1A); (3) federal pressure on how
  dealers are paid for arranging finance and selling add-on products (Item 1A, the CFPB and FTC paragraph), which reaches the
  23 percent of gross profit that F&I supplies. The newspaper test of **[L2006-008]** put to this business: if direct online
  sale had come first, would franchised dealers exist? For new cars perhaps not; for service and for the used car taken in
  trade, yes. The castle would be smaller, not gone. None of the three is shown in the filings to be filling the moat now:
  franchise laws stand in all 15 of the company's states, and parts-and-service gross profit grew in 2025.

- **Why not TOO HARD.** The tenuous moat goes to TOO HARD because "We don’t know how to valuate that" **[M2000-019]**. Here
  the returns of four durable players over the last full cycle are known from their own filings, so the castle's present
  strength can be valued; the threats above are carried to Q7 as uncertainty in the cash, where "The moat and the management
  are part of the valuation process" **[M1999-104]**. A doubt this run does not hide: the castle is lent by the manufacturers
  and the states, and a lender can change its terms; the rows' warning on brands and intermediaries, "the brand is our
  protection against the intermediaries making all the money" **[M2019-041]**, is here read from the intermediary's side:
  the dealer is the intermediary, and the law is what has kept the brand owner from taking all the money.

- **VERDICT: IN.** The deciding part's castle stands on the evidence of the field's returns over 2011 to 2019 and the trough
  of 2009 **[M1995-038]**, **[M2015-011]**; the new-vehicle line has no pricing power and is commodity-like
  **[M2012-109]**, **[L2004-003]**, which is weighed, not decisive, since parts and service and F&I carry 71 percent of
  gross profit; the franchise-law, direct-sales and F&I-regulation threats are carried to Q7 and Q9.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital the business needs** **[M2010-090]**, **[M2011-060]**. On net tangible capital (goodwill and
  franchise rights out, floor-plan debt left with the inventory it funds), ABG earned 16 to 31 percent pre-tax every year
  2011 to 2019, 23.9 percent on average, and 27.9 percent in 2025 (Q2's competitor row; XBRL of its 10-Ks, checked for 2023
  and 2025 against the filed statements). Read with care before crediting **[L1994-009]**: the 2021 to 2023 figures (41 to
  62 percent) are a cyclical peak the filer itself calls above historical levels, and they are not credited.
- **What the added capital earned.** Goodwill is counted here "because we paid for it" **[M2011-060]**. From 2019 to 2025
  total capital (equity plus non-floor-plan debt less cash) rose from $1,581M to $7,424M, by $5,843M, and pre-tax earnings
  before other interest rose from $299M to $850M, by $551M: 9.4 percent pre-tax on the added capital, about 10.5 percent if
  2025's $141.0M of impairments are added back and its $80.2M divestiture gain taken out (XBRL of the FY2019 and FY2025
  10-Ks; `field_returns.txt`). In cash: net acquisitions over 2019 to 2025 (cash paid less the floor-plan borrowings that
  came with the inventory, less divestiture proceeds net of floor-plan repaid) were **$5,691M**, and annual owner cash before
  acquisitions on the all-equity basis rose from $239M (2019) to $559M (2025), by $320M (Q4 recast; `q7_output.txt`): about
  **5.6 percent after tax** on what was spent, the long government rate and no more. The equity raised for the LHM purchase
  ($666.9M for 3,795,000 shares, 10-K FY2021 `0001144980-22-000079`) is inside the capital figure. "we’re not earning a
  higher rate of return on capital than we were when we started. We just put way more capital into the business"
  **[M2023-081]** is the shape of 2019 to 2025 here: revenue up from $7.2B to $18.0B, the return on total capital down from
  18.9 to 11.4 percent pre-tax.
- **Reinvestment to stand still** **[L2000-035]**, **[M2000-144]**. Capital spending has run well above depreciation:
  2025 $205.3M (ex-real-estate $186.0M) against depreciation and amortization of $82.4M; 2024 $320.1M against $75.0M; the
  company expects about $250.0M in 2026 "to upgrade or replace our existing facilities, construct new facilities, expand our
  service capacity, and invest in technology" (10-K Item 7, Investing Activities). The filing gives no split between
  maintenance and growth, so the maintenance guess the rows ask for cannot be read from it. Part of the spending is not
  optional: "manufacturers may have the right, and may direct us, to implement costly capital improvements to dealerships as
  a condition to entering into, renewing, or extending franchise agreements" (10-Q `0001144980-26-000094`,
  commitments and contingencies note), the compulsory reinvestment the rows avoid **[M1997-016]**. Loaner vehicles are a further real cost
  carried in operating cash (loaner amortization $56.8M in 2025, cash-flow statement). Some spending is rent bought out
  (purchases of previously leased real estate $217.1M in 2021, $11.9M in 2024), which returns as rent saved.
- **Growth arithmetic** **[M1998-081]**, **[L2009-012]**. The stores need little capital to grow organically (inventory is
  floor-plan funded; the parts-and-service line grows on the existing bays); the company's growth has been bought. The rows'
  test of the capital-heavy second best is "decent returns on the incremental sums" **[L2009-012]**; the incremental sums
  here have so far earned about the bond rate in cash.
- **WEIGHS AGAINST.** The stores earn high returns on the tangible capital they need, which weighs for **[M2010-090]**; but
  the capital actually being added goes into acquisitions that have so far returned about 5.6 percent after tax in owner cash
  and into facility spending the manufacturers can compel, so the growth arithmetic weighs against **[M2023-081]**,
  **[M1997-016]**. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, eight years of them, before the income account** **[M2025-032]** (XBRL first-filed values
  printed by `tools/run.py`, accessions in its output; checked against the filed statements for 2021, 2022, 2024 and 2025:
  receivables $229.8M and $171.9M, inventory $959.2M, equity $3,891.9M all match; USD millions):

  | year-end | revenue | inventory (% of revenue) | receivables (%) | goodwill + franchise rights | equity | tangible equity | non-floor-plan debt |
  |---|---|---|---|---|---|---|---|
  | 2018 | 6,874 | 1,068 (15.5) | 130 (1.9) | 247 | 473 | 226 | 905 |
  | 2019 | 7,210 | 985 (13.7) | 136 (1.9) | 324 | 646 | 322 | 939 |
  | 2020 | 7,132 | 875 (12.3) | 156 (2.2) | 987 | 906 | -81 | 1,202 |
  | 2021 | 9,838 | 718 (7.3) | 230 (2.3) | 3,608 | 2,116 | -1,492 | 3,583 |
  | 2022 | 15,434 | 959 (6.2) | 172 (1.1) | 3,583 | 2,904 | -679 | 3,301 |
  | 2023 | 14,803 | 1,768 (11.9) | 226 (1.5) | 4,105 | 3,244 | -861 | 3,206 |
  | 2024 | 17,189 | 1,979 (11.5) | 286 (1.7) | 3,957 | 3,502 | -455 | 3,139 |
  | 2025 | 17,999 | 2,136 (11.9) | 295 (1.6) | 4,379 | 3,892 | -487 | 3,572 |

  What moved and why. Equity rose eightfold, from $473M to $3,892M, on retained earnings ($923M to $3,616M) and the $666.9M
  share sale of 2021, less buybacks; but purchased goodwill and franchise rights rose faster, from $247M to $4,379M, so
  tangible equity went from positive to about minus $0.5B: the balance sheet is now mostly the price paid for stores bought
  since 2020. Inventory fell to 6 to 7 percent of revenue in the shortage and has returned to about 12 percent, below the
  2018 level; receivables have stayed under 2.5 percent of revenue throughout. Nothing builds up against sales in the way the
  rows warn of **[M1995-064]**. Non-floor-plan debt went from $905M to $3,572M, most of it raised for the acquisitions (notes
  of 2020 and 2021, real-estate facilities of 2021 and 2025); floor-plan notes of $2,027M more sit against the inventory at
  2025 year-end. Cash is kept near zero ($40.4M), with $151.6M parked in floor-plan offset accounts and a revolver behind it
  (10-K Item 7, Liquidity). TCA carries $414.7M of investments against $828.2M of deferred revenue (current $243.6M plus
  long-term $584.6M): those securities back its contract obligations and are not counted as free cash anywhere in this run.
  What the figures can't say: whether the $4.4B of goodwill and franchise rights is worth its carrying value; the filer
  wrote franchise rights down by $117.2M, $149.5M and $141.0M in 2023, 2024 and 2025 for "the underperformance of certain
  stores" (10-K Item 7, Critical Accounting Policies).
- **The owner cash, recast** (operator rule 5: a cash figure, never net income; script `q7.py`, output `q7_output.txt`).
  For a dealer the as-filed operating cash is distorted by the floor-plan split (Step 0), so the base is the filer's own
  "Adjusted cash flow provided by operating activities", which puts the non-trade floor-plan borrowings and repayments back
  beside the inventory they fund and is reconciled to GAAP line by line in every 10-K (FY2025 `0001144980-26-000051`, FY2022
  `0001144980-23-000080`, FY2021 `0001144980-22-000079`). **CONVENTION of this run, confessed: floor-plan notes are treated
  as an operating liability of the inventory, their interest as an operating cost, and they are left out of net debt at Q7
  (shown beside); rationale: every manufacturer requires floor-plan finance and each note is repaid when its vehicle is sold
  (10-K Item 7), and the filer measures and reconciles its own operating cash this way.** Then less stock pay,
  less all capital spending (real estate and bought-out leases included), plus other interest after a 25 percent tax for
  the all-equity basis (**CONVENTION of this run: 25 percent**; rationale: the filer's effective rate was 24.8, 25.2 and 25.7
  percent in 2023 to 2025). USD millions:

  | year | adjusted CFO | stock pay | capital spending | other interest x 0.75 | owner cash, all-equity | owner cash after interest | acquisitions net of divestitures | after acquisitions |
  |---|---|---|---|---|---|---|---|---|
  | 2019 | 282.3 | 12.5 | 71.7 | 41.2 | 239.3 | 198.1 | 129.7 | 109.6 |
  | 2020 | 442.6 | 12.6 | 48.8 | 42.5 | 423.7 | 381.2 | 705.0 | -281.3 |
  | 2021 | 632.1 | 16.2 | 299.1 | 70.4 | 387.2 | 316.8 | 3,425.4 | -3,038.2 |
  | 2022 | 987.0 | 20.6 | 107.9 | 114.1 | 972.6 | 858.5 | -647.8 | 1,620.5 |
  | 2023 | 705.3 | 23.5 | 142.3 | 117.1 | 656.6 | 539.5 | 1,213.2 | -556.6 |
  | 2024 | 688.4 | 26.7 | 320.1 | 134.3 | 475.9 | 341.6 | -157.5 | 633.4 |
  | 2025 | 651.4 | 27.7 | 205.3 | 140.6 | 559.0 | 418.4 | 1,023.3 | -464.3 |

  Acquisitions net of divestitures = cash paid for acquisitions less the floor-plan borrowings that came with the acquired
  inventory, less divestiture proceeds net of the floor-plan repaid on the stores sold (cash-flow statements of the 10-Ks
  named). The filer's adjusted CFO changed definition in the FY2020 10-K (offset-account changes and the used-vehicle
  borrowing base were taken out); 2019 is on the later definition as the FY2021 10-K restates it ($282.3M, against $155.1M
  on the old one). Earlier years (2014 to 2018, old definition: $193.2M, $118.9M, $260.3M, $195.6M, $181.6M) are not used.
- **The real costs.** Depreciation is real **[R1996-023]** and here it understates what keeps the business in place:
  capital spending ran at two to four times depreciation in 2024 and 2025 (Q3), so the recast charges all spending
  **[L2015-004]**. Stock pay ($27.7M in 2025) is charged. Loaner-vehicle amortization ($56.8M) is a real cost and is already
  inside operating cash. The impairments are the write-down of prices paid for stores; in cash they are already charged,
  as the acquisition spending in the last two columns, and they recur three years running, so they are not "one-time".
- **EBITDA and adjusted figures in the filer's own mouth.** The annual cash bonus is 80 percent weighted on "Adjusted
  EBITDA" ($974.3M for 2025 against a target of $921.9M; DEF 14A `0001144980-26-000070`, CD&A), and the performance shares
  on one-year "adjusted EPS" ($27.43 against GAAP diluted $25.13). The rows call EBITDA "utter nonsense" as earnings
  **[M1998-086]** and ask whether "the tooth fairy pays for capital expenditures" **[L2000-036]**; a company that spends two
  to four times its depreciation pays its managers on a figure that leaves the spending out. The 10-K itself features
  adjusted operating cash flow and a "transaction adjusted net leverage ratio" (target 2.5x to 3.5x; 3.2x at 2025
  year-end, Item 1), both reconciled or defined; the reconciliation is clear and the reason given for it is a real one.
- **Targets.** The 10-Ks carry a stated revenue target: "$20 billion by 2025" (announced December 2020), raised in April
  2022 to "$32 billion by 2025" (10-K FY2022 Item 1), replaced in February 2024 by "$30 billion or more by 2030" (10-K FY2024
  Item 1), and absent from the FY2025 10-K; 2025 revenue was $18.0B. The rows find predicting growth rates "both deceptive
  and dangerous" **[L2000-037]**; here the target was missed by a wide margin and then dropped, not met by bending the
  accounts, so it is not the made-every-quarter habit **[L2002-041]**; what it shows is a management steering by size,
  carried to Q5 and Q6.
- **VERDICT on the accounts: WEIGHS AGAINST** (not a STOP). No confusion: the floor-plan split, the one thing a reader could
  misread, is explained and reconciled in the filer's own words; no suspicion from the accounts' tells: receivables and
  inventory run in line with sales, no reserve is seen moving, the impairments are disclosed with their cause
  **[M1995-064]**, **[M1995-063]**. Against: pay on EBITDA and adjusted EPS, a featured size target missed and withdrawn,
  and recurring write-downs of acquired franchise rights; "a negative" but not "a total exclusionary factor"
  **[M1994-018]**. The habits are carried to Q5. The recast owner cash above feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
The question: "do we really want to be in partnership with this person and count on them to behave in the future [...] as
they behaved in the past" **[M2015-005]**. A stock bought in the market is judged by reading, not meeting **[M2007-081]**.

- **Who.** David W. Hult was President and CEO from January 2018 (COO from November 2014) and became Executive Chairman
  after the 2026 annual meeting; Daniel E. Clara, who joined the company in 2002 and held store jobs from client advisor and
  F&I manager to general manager before running operations, became President and CEO on 2026-05-04 (8-K
  `0001144980-25-000155`; 8-K/A `0001144980-26-000083`; DEF 14A `0001144980-26-000070`). On 2026-01-29 the board had eleven members, ten
  independent (8-K `0001144980-26-000003`). The chief human resources officer left in August 2026, terminated without cause
  under a 2017 severance agreement, then retained as a consultant at $27,083.33 a month to year-end (8-Ks
  `0001144980-26-000096`, `-000100`); no reason is given.
- **First yardstick: the business run against the hand dealt** **[M1994-008]**. On the same metric as the rivals, ABG's
  stores earned 23.9 percent pre-tax on net tangible capital over 2011 to 2019, between Lithia and Group 1, and in 2025 its
  earnings margin after floor-plan interest (4.72 percent) was the highest of the four filers read (AutoNation 3.85, Lithia
  3.68, Group 1 2.80; Q2's table). The stores are run well, which the trade needs: "Buying a retailer without good
  management is like buying the Eiffel Tower without an elevator." **[L1995-006]**. Ability in operations weighs for.
- **Second yardstick: how they treat the owners** **[M1994-009]**. The capital half is Q6's: $5.7B of net acquisitions
  since 2019 returning about the bond rate in owner cash (Q3), buybacks at $196 to $231 a share in 2023 to 2025 with the
  stock now $165, and a revenue target pursued by acquisition. The proxy: CEO pay of $10.7M for 2025 (salary $1.3M, stock
  $7.0M, cash bonus $2.4M at 137 percent of target), the bonus 80 percent on adjusted EBITDA and the performance shares on
  one-year adjusted EPS (Q4); the CEO holds 55,420 shares, about $9.2M at the quote, and all fifteen directors and officers
  together 145,318 shares, under 1 percent (DEF 14A). The executive chairman's amended agreement vests all his unvested
  equity on any departure other than for cause (8-K `0001144980-25-000155`). These weigh against, as Part B of Q6 records;
  none is an integrity fact.
- **The habits carried from Q4**, read with the integrity record **[M2004-067]**: pay on EBITDA and adjusted EPS, and a
  revenue target raised from $20B to $32B for 2025, missed ($18.0B), replaced by "$30 billion or more by 2030" and then
  dropped. A missed target dropped in plain sight is the opposite of the made-every-quarter habit the rows distrust
  **[L2002-041]**; it shows a management steering by size, which is weighed at Q6, not a management bending figures.
- **The integrity record.** (1) An FTC administrative proceeding filed 2024-08-16 against the company, three of its Texas
  dealerships and one general manager, alleging violations of Section 5 of the FTC Act and of the Equal Credit Opportunity
  Act "in connection with the sale of add-on products (e.g., vehicle service contracts, maintenance plans, etc.)"; the
  company "vigorously disputed, and continues to vigorously dispute, the FTC’s allegations" and sued in federal court to
  enjoin the proceeding as unconstitutional; both remain pending, and no loss range is given (10-K Item 3; 10-Q legal note).
  (2) A 2016 FTC consent order over advertisements that "did not adequately disclose information about used vehicles with
  open safety recalls", with no payment and no admission (10-K Item 1A). (3) The filer's own risk factor: "there is a risk
  that our employees could engage in misconduct [...] It is not always possible to detect or deter employee misconduct"
  (Item 1A). Against these, the reports read as candid where a reader could be misled (the floor-plan reconciliation, the
  impairments with their cause, the dropped target), which is "telling us about the things that we would want to know
  about if we owned a hundred percent of the company" **[M1998-036]**; no figure that matters is touched on dishonestly
  **[M2007-082]**. How they talk about mistakes **[L2024-003]**: the write-downs are put to "the underperformance of
  certain stores", not to the prices paid; no instance found in the FY2025 10-K, the Q2 2026 10-Q or the proxy of the word "mistake" about an
  acquisition (a text search of the three documents).
- **Love of the business** **[M2000-098]**. The new chief executive spent 24 years in the company's stores and offices
  before running it (8-K `0001144980-25-000155`), the kind of track record the rows read **[M1998-168]**. The directors'
  holdings are small; whether they were bought or granted is not shown in the ownership table read.
- **The doubt question, answered.** "If you’ve got doubts, forget it." **[M2013-088]**. The FTC matter is an allegation,
  contested, about the sale of add-ons at three of about 170 stores, unresolved after two years; the rows warn that a
  practice "which, if put on the front page, you know, would make you very unhappy, you can get in a lot of trouble. It may
  take a while." **[M2016-033]**, and that a management is judged by whether it acts when it learns of a problem
  **[M2017-005]**; what the company did internally is not in the filings. I do not find in the filings read a fact that
  shows the people running the company to be dishonest, and I do not treat a pending, contested allegation against three
  stores as one; but the matter goes to the F&I line that carries 23 percent of gross profit, and its outcome must be read
  by any later run before Q5 is answered again. This is a judgment, stated as one.
- **VERDICT on integrity: IN** (no dishonesty shown in the filings; the FTC proceeding recorded as an open integrity fact,
  unproven) **[M2013-088]**, **[M1998-036]**. **Ability WEIGHS FOR in operations** **[M1994-008]**, **[L1995-006]**; the
  treatment of owners' capital weighs against and is judged at Q6 **[M1994-009]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **The retention test** **[R1995-009]**, **[M1998-110]**, read in market value and against intrinsic value
  **[R2009-002]**. From 2020-02-28 (NYSE close $88.64 x 19,278,564 shares = $1,708.9M; 10-K FY2019 Item 5 and cover,
  `0001144980-20-000059`) to today's quote ($2,967.1M), market value rose $1,258.2M. Over the same span the company earned
  $3,611.3M (net income 2020 to 2025 and the first half of 2026: $254.4M, $532.4M, $997.3M, $602.5M, $430.3M, $492.0M,
  $302.4M; the 10-Ks and the 10-Q), paid no dividend ("We have not paid any dividends since 2008", 10-K Item 5), spent
  $1,115.6M on buybacks and raised $666.9M of new equity. Retained: $2,495.7M. Market value added net of the new equity:
  $591.3M, about **$0.24 of market value per dollar retained** at today's quote. The market leg fails. On the intrinsic leg,
  this run's organic no-growth valuation at the sovereign (Q7, beside) rose from about $173 a share at 2019 (2019 owner cash
  $239.3M, net debt about $935M from the FY2019 balance sheet, 19.28M shares) to $332.50, against about $134 a share
  retained: a pass on that leg, but only on the reading Q7 itself does not let decide, and the 2019 base is the pre-boom low.
  The forward question **[M2010-097]**: the stated policy is to keep "acquiring revenue through strategic transactions"
  (10-K Item 1, Business Strategy), and the dollars so spent since 2019 have returned about the bond rate in owner cash (Q3).
  The retention test weighs against.
- **Buybacks** **[L1999-023]**, **[L2011-003]**. The programme names no price: "The share repurchase authorization does not
  require the Company to repurchase" and the extent "will depend on general market conditions" (10-Q, Share Repurchases;
  10-K Item 7). Prices actually paid under the programme (shares and dollars from the 10-Ks and the 10-Q): 2022 $181.6
  (1,635,030 shares, $297.0M); 2023 $196.1 (1,316,167, $258.1M); 2024 $220.4 (830,297, $183.0M); 2025 $230.8 (432,752,
  $99.9M); first half 2026 $206.2 (1,346,359, $277.6M). The authorization was raised to $500.0M in February 2026.
  **The line Q6 needs from Q7, written back with Q7:** every price paid, $181.6 to $230.8 a share, sits far above the
  bottom of the Q7 range ($7.39, the central case) and above the organic fair price ($102.33); it sits below only the
  organic no-growth value at the sovereign ($332.50), which is not "intrinsic value, conservatively-calculated"
  **[L1999-023]** on this run's evidence. The programme names no price **[L2016-002]**, so it weighs against.
- **Issuance and deals** **[L2014-012]**, **[M1995-001]**. One share issue in the decade read: 3,795,000 shares sold for
  cash at about $175.73 net ($666.9M) in 2021 to help pay for LHM (10-K FY2021). Every acquisition was paid in cash and
  debt; no all-stock deal, so the one STOP of Part A **[L2009-019]** does not arise; not a serial issuer **[L2014-015]**.
  The value given against the value got is Q3's finding: about 5.6 percent after tax in owner cash on $5.7B net, and three
  years of franchise-rights write-downs on the stores bought. A size target drove the buying (Q4, Targets): "So there are
  all these forces that push toward deals, and if you try to push toward deals, you’re going to get a lot of dumb deals."
  **[M2014-076]**. Divestitures are part of the policy too (24 franchises sold in 2025 for $566.5M with an $80.2M gain; a
  further $125.8M gain in the first half of 2026), which recycles capital into the next purchase or the buyback.
- **Part A: WEIGHS AGAINST.** Retained dollars have not shown a dollar of market value each, the buybacks name no price, and
  the acquisitions the policy commits to have earned about the bond rate **[R1995-009]**, **[L1999-023]**, **[M2014-076]**.

**Part B: the pay, the board and the owners** (DEF 14A `0001144980-26-000070`; 8-Ks named at Q5).
- Pay tied to what the person controls **[M2003-019]**: the targets are indexed to industry volume (the bonus and share
  matrices move with the U.S. seasonally adjusted annual sales rate as Wards reports it), which is a fair attempt to pay for
  what management controls. Against: the bonus is 80 percent on adjusted EBITDA, which leaves out the capital spending this
  business must make **[L2000-036]**; the performance shares measure one year of adjusted EPS, which buybacks and debt can
  raise without any gain in the business, and carry no charge for the capital the acquisitions used **[L1994-019]**,
  **[M1995-010]**; one strategic objective pays for "the integration of large acquisitions". Peer data from a pay consultant
  inform the levels **[L2005-015]**.
- The owners: the CEO in 2025 held 55,420 shares (about $9.2M at the quote) against $10.7M of pay that year; all directors
  and officers together 145,318 shares, under 1 percent; whether the directors bought with their savings is not shown
  **[L2019-008]**. The former CEO, now executive chairman, keeps full vesting of unvested equity on any exit not for cause.
  The board lowered the threshold for owners to call a special meeting from 50 to 25 percent in January 2026 (8-K
  `0001144980-26-000003`), a step toward the owners. Ten of eleven directors independent at that date.
- **Part B: WEIGHS AGAINST** (pay on EBITDA and one-year adjusted EPS with no capital charge, small owned stakes)
  **[M1994-009]**, **[L1994-019]**; the volume-indexed targets and the special-meeting change weigh for.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**, **[M1996-025]**: "the discounted value of
the cash that can be taken out of a business during its remaining life" **[R1996-018]**, crediting only "whatever net
cash is left every year" **[M1998-080]** after asking "are you going to have to put more cash into after you buy it?"
**[M2014-068]**. The arithmetic is in `Test Runs/_research 2026-10-12 ABG/q7.py`, its output in `q7_output.txt`.

- **The cash input.** Owner cash as Q4 recasts it, all-equity basis, after the company's own tax (Q7, Whose tax): the
  filer's adjusted operating cash flow less stock pay, less all capital spending, plus other interest after tax.
- **The window and the cycle (specific (a)).** The literal window is 2021 to 2025: owner cash $387.2M, $972.6M, $656.6M,
  $475.9M, $559.0M, average **$610.3M**. Its first year is aberrational on the filer's own description: new-vehicle margins
  "above historical levels" in and after the pandemic "as a result of inventory disruptions from supply chain issues" (10-K
  FY2025 Item 7, Overview), same-store new-vehicle gross profit per unit up 82 percent in 2021 (10-K FY2021 Item 7), and 2021
  also holds only two weeks of the LHM stores. So the base is the last full cycle of the owner-cash series, trough to
  trough: **2019** ($239.3M, the low before the shortage) **to 2024** ($475.9M, the low after the 2022 peak of $972.6M),
  average **$525.9M** (**[L2005-003]**: no picked base year). Caveat written down as found: 2026 is running lower again
  (first-half operating income $413.4M against $491.7M; 10-Q), so the cycle may not have ended at 2024; a later trough would
  lower the base. Growth between the averages of successive cycles cannot be measured: only one cycle is on the record read.
- **Acquisitions (specific (c)), the default pair: acquisitions deducted, total growth credited.** Net acquisitions over the
  cycle averaged $778.0M a year (window $971.3M), more than the owner cash itself, so owner cash after acquisitions averages
  **minus $252.1M** (window minus $361.0M) and changes sign year to year (+110, -281, -3,038, +1,621, -557, +633, -464);
  the compound rate is meaningless and so is the rate between halves (specific (b)), so **the default pair is the no-growth
  case alone, said so**: years one to ten at minus $252.1M, then purchases stop with growth and the business is valued at no
  growth on owner cash before purchases, $525.9M (2026-10-10 amendment). At 5.60 percent: **$7.39 a share**; valued at ten
  percent: minus $163.97 a share.
- **The organic pair, beside: acquisitions left out, only organic growth credited.** The filer reports organic growth line by
  line, same-store, never for the whole or for owner cash, and the lines ran both ways across the cycle (same-store
  new-vehicle gross profit +89 percent in 2021, then down 14, 22 and 8 percent in 2023, 2024 and 2025; same-store
  parts-and-service gross profit up 13, 11, 6 and 5 percent in 2021, 2022, 2024 and 2025; 10-Ks FY2021, FY2022, FY2024,
  FY2025, Item 7). No organic growth of owner cash is shown, so it is carried at none: **the organic pair is the no-growth
  case alone, said so**: $525.9M forever, **$332.50 a share** at 5.60 percent; **$102.33** valued at ten percent.
- **Working capital (d)** is inside the adjusted operating cash. **Growth spending (e):** the filing gives no maintenance
  split (Q3), so the central case charges all spending; the depreciation variant is shown beside. **The cap (f):** no
  growth is carried, so no cut arises. **Deals:** no signed and unclosed deal found (no Item 1.01 or 2.01 8-K since the
  10-Q; "There were no acquisitions during the six months ended June 30, 2026", 10-Q note 3); Herb Chambers closed on
  2025-07-21 inside the window and is in the series as an acquisition, not as a merger (see the last section). **Tax:**
  goodwill and franchise rights from acquisitions are deductible "ratably over a 15-year period" (10-Q note 3); the
  effective rate (24.8 to 25.7 percent) is not below statutory federal plus state, so no expiring shelter is priced.
- **On what the floor is earned** **[L2017-004]**. Net debt at the latest filed date, 2026-06-30: current debt $447.7M plus
  long-term debt $3,010.0M, less cash $30.4M and short-term investments $5.3M = **$3,422.0M** (10-Q balance sheet; the
  10-Q states no subsequent event). Left out and said so: floor-plan notes $1,839.5M (Q4's convention; shown beside),
  operating leases $233.3M, and TCA's investments $416.5M, which back its contract liabilities and are not free cash.
  Market value at the quote $2,967.1M; enterprise value **$6,389.1M**.
- **The floor, tested first** (2026-10-10). At no growth the price earns owner cash over enterprise value: **8.23 percent**
  on the cycle base, 9.55 percent on the literal window. To earn about ten percent at the price the business would need
  $638.9M of owner cash a year with no growth, or the cycle base grown about 2.85 percent a year for ten years, which no
  filing read shows. Every case, valued at ten percent, against the price:

  | case | at 5.60% (per share) | at 10% (per share) | price $165.28 |
  |---|---|---|---|
  | default pair, cycle base (central; no-growth alone) | $7.39 | -$163.97 | not earned |
  | organic pair, cycle base (no-growth alone) | $332.50 | $102.33 | not earned |
  | literal window, default pair | $10.55 | -$183.13 | not earned |
  | literal window, organic pair | $416.44 | $149.33 | not earned |
  | beside: depreciation in place of all spending, cycle base | $442.18 | $163.75 | not earned (by $1.53) |
  | beside: depreciation variant, literal window | $563.40 | $231.63 | earned, two departures from the construction away |
  | beside: floor-plan notes counted in net debt, organic cycle | $230.03 | -$0.14 | not earned |
  | beside: equity-only, owner cash after interest $439.3M against market value | $436.96 | $244.70 | earned; never decides alone |

  No case of the range, central or organic, earns the floor at the price. The one beside case that does stacks two
  departures (the boom window the cycle rule sets aside, and depreciation in place of spending that has run at two to four
  times depreciation); the equity-only case earns it because the lenders' $3.4B is left out, the flattery the all-equity
  basis exists to refuse **[L2017-004]**. "So, there’s just a point at which we drop out of the game." **[M2003-149]**.
- **Value range** (central, all-equity, at 5.60 percent): **$7.39 a share** (the default pair collapses to its no-growth
  case; both ends the same), against **$165.28**; organic pair beside **$332.50**; literal window beside $10.55 and
  $416.44. The width test is not reached: the floor closes first. Were it reached, the range from the central case to the
  organic case runs far past three to one **[L2000-025]**.
- **Fair price (a reporting figure, never a verdict; Part VII):** the central default pair valued at ten percent is not
  positive (minus $163.97 a share), so by the 2026-10-10 amendment the figure is set on the organic pair and **labelled
  so: $102.33 a share** (organic pair, cycle base; both end cases the no-growth case valued at ten percent, averaged, less
  net debt; after the company's own tax; all-equity basis). Equity-only figure beside: **$244.70**. Literal window beside:
  $149.33 (organic). No cheap price is reported.
- **VERDICT: OUT.** No case in the range earns the floor of about ten percent at $165.28: the central default pair is not
  positive at ten percent and the organic pair is worth $102.33 there **[M2003-149]**; and even a case that cleared it would
  have needed the pencil **[M2009-005]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT). Facts found are under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts found are under AFTER THE STOP.

---
## THE BOX
**OUT at Q7**: no case earns the floor of about ten percent at $165.28; value range (central, all-equity, at 5.60
percent) $7.39 a share, organic pair beside $332.50; fair price $102.33 on the organic pair, labelled (the central case is
not positive at ten percent), equity-only $244.70 beside. Q1 IN, Q2 IN (Dealerships decides), Q3 and Q4 weigh against,
Q5 integrity IN with the FTC proceeding recorded as an open, unproven integrity fact, Q6 weighs against.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; the box is unchanged (operator rule 2) **[M1997-127]**.
- **Q8 (the bond).** The 30-year Treasury yields 5.60 percent (2026-10-09); the price earns 8.23 percent in owner cash on
  enterprise value at no growth on the cycle base, 9.55 percent on the literal window (Q7).
- **Q9 (debt and exposures).** At 2026-06-30: total debt outstanding $3,476.8M (senior notes $405.0M due 2028, $800.0M due
  2029, $445.0M due 2030, $600.0M due 2032; real-estate facilities $520.5M, $410.3M and $147.5M; a Wells Fargo master loan
  $44.3M; mortgage notes $26.0M; revolver $70.0M; finance leases $8.3M), current maturities $447.7M; floor-plan notes
  $1,839.5M more (10-Q note 9 and balance sheet). Variable-rate debt including floor plan $2.62B at 2025 year-end (10-K
  Item 7A). Cross-defaults: "an event of default under either the Revolving Credit Facility or the Used Vehicle Floor Plan
  Facility could be, or result in, an event of default under the New Vehicle Floor Plan Facility, and vice versa" (10-K
  Item 7). The company targets a "transaction adjusted net leverage ratio" of 2.5x to 3.5x and stood at 3.2x at 2025
  year-end (Item 1). Pre-tax income plus other interest covered other interest 4.5 times in 2025 ($662.2M plus $187.5M,
  over $187.5M; 10-K income statement), the pre-tax measure the rows ask for, not EBITDA. Insurers require collateral for
  self-insurance deductibles, met with surety bonds, letters of credit and cash (Item 1). Toyota and Lexus are 30 percent
  of new-vehicle revenue (Item 1A). Not "little or no debt" **[R1997-001]**, a criterion stated for whole businesses.
- **Q12 (how the money is made).** The FTC's complaint, as the 10-K describes it, concerns the sale of add-on products
  (service contracts, maintenance plans) and the Equal Credit Opportunity Act at three Texas stores; unresolved (Q5).
  Integrity facts recorded at Q5 and judged there; none bears on a named business of Q12.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `263c852d`, before the first EDGAR request); written question by
      question; committed after each (Step 0 to Q1, Q2, Q3, Q4, Q5, Q6, Q7 with the Q6 buyback line, the close).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's and was not
      touched; the fold is the dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; the one directory listing of
      `Test Runs/` (to check this file's name was free) and the start-up context are declared under contamination above and
      nothing in them was used.
- [x] Every v5 id resolves (`check_quotes.py` against `principle_ledger_v5.csv`); every filing fact carries its accession
      or names the filing whose accession is in Step 0; the numbers carry their filing or their script.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 are NOT REACHED and their facts are
      under AFTER THE STOP.
- [x] Owner cash after every real cost from the filer's reconciled adjusted operating cash flow, never net income
      (operator rule 5); the sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (the foundations' five items, Q2's threats, Q5's integrity record).
- [x] No row dated after the anchor: not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used; its three-year owner-earnings mean was not used, for the reason
      given in Step 0.
- [x] `python tools/check_framework.py` PASS before the closing commit (recorded below the reply in the research notes).
- Departures, declared: three years of segment profit in place of five for the parts table (Q2, confessed); floor-plan
  notes treated as operating (Q4, confessed); a 25 percent tax rate on the interest add-back (Q4, confessed). The
  trough-to-trough cycle 2019 to 2024 was chosen by this run from the owner-cash series under specific (a), and 2026 may
  extend it.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The acquisitions specific degenerates for a serial acquirer.** Under (c) the default pair deducts acquisitions and
credits the total growth; when acquisitions exceed owner cash and the after-acquisition series changes sign, (b) sends the
pair to its no-growth case alone, which deducts ten years of purchases and credits none of the growth they buy. The result
here is $7.39 a share, a figure no reading of the business supports, and the 2026-10-10 fallback to the organic pair is
what carries the reporting figure. The text should say what to do when the default pair collapses for this reason, rather
than leaving the central figure to an artefact. (2) **"Merger" against "acquisition" is not defined.** The LHM purchase
(2021, $3.48B, about doubling revenue), Koons (2023) and Herb Chambers (2025) all fall inside the window; read as mergers,
each would be "valued on the combined companies' own averages" (Herb Chambers' own audited statements are filed in 8-K/A
`0001104659-25-071383`), which would raise the base materially and could change the floor test; read as acquisitions they
are capital spending. This run treated them as acquisitions because they were cash purchases under a stated policy of
buying stores, and says so; the framework should say which reading governs. (3) **"Organic growth, as the filer reports
it"** assumes a whole-company figure; this filer reports same-store growth only line by line, which moved in opposite
directions, so the organic pair fell to no-growth by default. (4) **Floor-plan debt** is borrowings on the balance sheet,
and Q7's net-debt definition ("borrowings and finance leases less cash and securities") would include it, but it funds
inventory under every manufacturer's terms and the filer's own adjusted cash puts it in operations; the run confessed a
convention and showed both, and the choice moves the organic fair price from $102.33 to about zero. (5) **The cycle rule**
asks for "the last full cycle" in a series that may still be falling; a trough chosen in 2024 may be superseded by 2026.
(6) **The brief's slot for competitors** said "the rivals the 10-K itself names": the 10-K names none in its Competition
section; it names Carvana in Item 1A and a five-company peer index in Item 5, which this run used. **The brief's error, as
asked:** the dispatching message lists "a cyclical first or last window year sets a cycle base" among "the amendments of
2026-10-10 in Q7"; the cycle specific was adopted on 2026-10-06 (section D of the gaps case), and the framework words it as
a first or last year that is "a cyclical peak or trough, or otherwise aberrational" on "the filer's own description",
not any cyclical year. The same list leaves out two amendments of 2026-10-10 that bear on a run: the absurdity cut to the
business's own sales growth (Q7 (f), section B) and the change-for-the-better rule that now sends an uncredited
improvement to TOO HARD (NATURE) (Q2, section G). None of the three changed this run: no growth was carried, so (f) did
not bite, and Q2 credited no change for the better.
