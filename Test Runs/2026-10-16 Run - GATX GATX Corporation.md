# Company Run — GATX Corporation (NYSE: GATX) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.  *Filled at the fold by the dispatching session, 2026-10-16, after the run was committed: `PORTFOLIO.md` read for this ticker only; not held.*

**Run record.** Dispatched blind run, resumed. The template was copied and committed by a first analyst earlier on 2026-10-16
(commit `0c41b965`, "GATX run: template copied before any fetch"); that session ended at a session limit before any question
closed. This analyst resumed from the first unfinished section, read the research folder first, and refetched nothing that
was already cached. The research folder is `Test Runs/_research 2026-10-16 GATX/` (notes, the first analyst's scripts
`fetch.py`, `xbrl.py`, `row.py`, `cfs.sh`, this analyst's `bal.py`, `returns.py`, `q7.py`, `splice.py`, `check_ids.py`, the
section drafts, and `run_py_output.txt`; the filings are in `cache/`, which is gitignored).

**Contamination declared (seen by accident, not used).** The session context showed: the repository's recent commit subjects
(a WAB run and its fold by the overnight cycle, and this run's own template commit); `git status` file names of other
research folders (`_research 2026-09-26 AYI`, `_research 2026-09-27 ARCB`) and of daily digest files; and a memory index
whose lines speak of the queue in general terms (a wave paused, holding reviews owed, a count of gate-clearers, "nothing
buyable"). None of it names GATX or says whether anyone holds or wants it, and none of it was used. No blind-listed file was
opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $164.85 (quote of 2026-10-16 printed by `tools/run.py`; an aggregator, flagged per operator rule 5, live quote only).
- **Shares by class** from the latest filing's cover: one class, common, 35,300,000 (10-Q for the quarter to 2026-06-30, filed
  2026-07-31, accession `0000040211-26-000079`; `python Screens/cover_shares.py GATX`). Checked against the same 10-Q's balance
  sheet: issued 69,494,376 less treasury 34,189,318 = 35,305,058 outstanding, the count used below. No 8-K or prospectus was
  filed after that 10-Q (the submissions file lists only Forms 4, 2026-08-05 to 2026-09-11).
- **Market cap:** 35.305M x $164.85 = **$5,820M**.
- **Sovereign for the earnings currency:** USD, **5.43%**, the 30-year par yield on the US Treasury daily par yield curve,
  2026-10-15 (issuing authority; printed by `tools/run.py`).
- **Filings read** (operator rule 4): 10-K for 2025 (filed 2026-02-19, `0000040211-26-000018`): Items 1, 1A, 3, 7 and 8, and
  the notes on debt, GABX, segments and litigation; 10-Q for 2026 Q2 (`0000040211-26-000079`); the proxy, DEF 14A filed
  2026-03-13 (`0001104659-26-027377`, cached, not reached: the file closed before Q5); 8-K of 2026-01-05
  (`0001193125-26-001584`, the GABX closing); 8-K/A of 2026-03-03 (`0000040211-26-000024`, the Wells Fargo Rail carve-out
  statements and the pro forma combined statements); 8-K of 2026-07-01 (`0001193125-26-292657`, the first call option); 8-K of
  2026-07-30 (`0000040211-26-000073`, the second-quarter release). For the cycle, the 10-Ks for 2013 (`0000040211-14-000010`),
  2015 (`0000040211-16-000064`), 2017 (`0000040211-18-000023`), 2019 (`0000040211-20-000017`), 2020 (`0000040211-21-000018`),
  2021 (`0000040211-22-000023`), 2022 (`0000040211-23-000023`), 2023 (`0000040211-24-000023`) and 2024 (`0000040211-25-000024`),
  read for the cash-flow statements, the segment tables, the Lease Price Index and utilization.
- **One figure cross-checked against the filed statement:** net cash from operating activities for 2025, $648.1M on the filed
  cash-flow statement of the 2025 10-K, equals the tagged figure (648.1). Also GATX shareholders' equity at 2025-12-31,
  $2,750.5M filed against 2,750 printed, and debt $12,533.9M filed against 12,534 printed.
- `tools/run.py GATX`, arithmetic lines only (output kept as `run_py_output.txt`). Its three-year window ends at 2023 because
  capital spending for 2024 and 2025 is filed under a line ("Portfolio investments and capital additions") that the element
  it reads does not carry; its capex column leaves out portfolio proceeds, which for a lessor are the other half of fleet
  turnover; and its depreciation column leaves out the gains on disposal that the cash-flow statement deducts from operating
  cash. Its printed owner earnings (capex basis -846.1, depreciation basis 123.6, three-year means) are therefore not used;
  owner cash is recast from the filed statements in the COMPUTATION under Q7, every line named. Stock pay resolved from the
  filed statements: 17.4, 12.7, 18.3, 23.0 and 25.0 for 2021 to 2025 ($M; 2025 read from the filing, where the tag stops).
- **Lines of evidence, derived from the 10-K 2025 (the brief's one stated departure from the canonical brief).** From Item 1
  (business and segments), Item 1A (risks) and Item 7 (MD&A) I chose: (1) the segments and their profit over the cycle, with
  the deciding part found by the parts table; (2) North American lease rates on renewal (the LPI), utilization and renewal
  success through the 2016 to 2021 downturn and the 2022 to 2025 inflation; (3) residual values, read as the net gains on
  asset dispositions and remarketing income; (4) the GABX joint venture, its filed record and GATX's guarantee of its loan;
  (5) debt, its cost, maturities and covenants, and the reliance on capital markets named in Item 1A; (6) the competitors the
  10-K names and their own filings; (7) buybacks and their prices; (8) stock pay; (9) litigation and environmental exposure
  (Note 24, East Palestine, asbestos); (10) purchase commitments under the supply agreements.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own GATX "if the market closed for five years"
**[M1997-109]**, and for a lessor the answer turns on the fleet's cash and on its lenders, not on the quote. The market serves
and does not instruct **[M2006-077]**: the $164.85 is read against where the filings lead, nothing more. No macro forecast
enters **[M2000-094]**: the rail cycle is read from GATX's own renewal-rate record, not forecast. The margin of safety is an
attitude here and an arithmetic only at Q7 **[M1996-084]**. Who is paid to tell you: GATX publishes a full-year earnings
estimate per share and raised it in July 2026; the framework weighs that at Q4 and judges it at Q5. **Contrary evidence,
written down as found** **[M1997-127]**: (1) the 10-K's own risk factor: "our competitors are larger than we are and have
greater financial resources, higher credit ratings, and a lower cost of capital, while some of our competitors manufacture
railcars for their own leasing businesses" (10-K 2025, Item 1A); (2) the renewal-rate change on GATX's own North American
Lease Price Index was negative in each of six years, 2016 to 2021; (3) the Wells Fargo fleet bought on 2026-01-01 adds $0.6M to
GATX's 2025 pro forma net income attributable to GATX, $333.3M to $333.9M (8-K/A `0000040211-26-000024`, Exhibit 99.2);
(4) GATX guarantees all $2.96B of the GABX term loan while owning 33.5% of GABX; (5) consolidated debt of $12,333M against GATX
shareholders' equity of $2,784M at 2026-06-30 (10-Q 2026 Q2).

## THE STANDING RULE
The buyer's conduct: a part-interest in GATX bought for cash, with no borrowed money and sized so that a fall of half or more
could be sat through, puts the buyer at no risk of ruin. The rule forbids borrowing to own it **[M2004-065]** and any risk to
"what we have and need for what we don’t have and don’t need" **[M2012-081]**. GATX's own leverage is the target's, weighed at
Q9, not the buyer's. Nothing in this run is a recommendation to buy, and no size is proposed.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test** is "a reasonable fix on about what the earning power and competitive position will look like in five or 10
  years" **[M2012-065]**, **[M2000-037]**, applied to the filings.
- **What GATX is (10-K 2025, Item 1):** an owner and lessor of long-lived transport assets. About 156,000 wholly owned
  railcars (107,625 in North America, 36,484 in Europe, 12,165 in India) with "estimated economic useful lives of 27 to 45
  years" in North America and an average age of about 17 years; about 800 North American customers shipping "more than 580
  different commodities"; full-service leases of one to ten years (average remaining term about 43 months in North America);
  627 locomotives; aircraft spare engines through the 50% Rolls-Royce joint ventures (456 engines) and 46 owned engines; tank
  containers (Trifleet). From 2026-01-01 it manages and consolidates GABX, about 101,000 former Wells Fargo railcars, of which it
  owns 33.5% after the first call option (10-Q 2026 Q2, note on GABX).
- **The key variables, and how predictable they are** **[M1998-044]**: the lease rate on renewal (the filer's Lease Price
  Index, LPI), the share of the fleet on lease (utilization), the renewal success rate, gains on remarketing used cars,
  maintenance cost, and the cost of debt. The filer reports each of them every year. LPI renewal-rate change: +6.9% (2011),
  +25.6%, +34.5%, +38.8%, +32.2% (2015); then -20.3%, -28.2%, -9.8%, -3.9%, -23.5%, -8.5% (2016 to 2021); then +23.4% (2022,
  restated +24.4%), +33.5%, +26.7%, +21.9% (2025), and +16.8% in 2026 Q2. Non-boxcar utilization 98.2% to 99.5% at every
  year-end read. The past statements tell me what kind of future statements to expect **[M2008-033]**: the fleet changes
  slowly (17 years' average age against lives of 27 to 45), the customers are shippers of industrial commodities, and the
  swings are in price, not in whether the business exists. The insiders do write a forecast down: the filer publishes a
  one-year earnings estimate and signs multi-year supply agreements (15,000 Trinity cars through 2028) **[M2000-105]**.
- **The lender-funded lessor, read against the framework's text on banks (Q1) and leverage (Q9), as the brief asks.** GATX is
  not a bank, but it is a balance sheet of long-lived assets funded mostly with borrowed money, so I read the bank door. What I
  took from it: (a) the door asks that both sides of the balance sheet be readable **[M2002-022]**. The asset side is railcars,
  engines and containers, listed by type, age, utilization and lease term, with no derivatives book "on top of it"
  **[M2005-068]**; the danger the rows place "always on the asset side" **[M2011-022]** appears here as lease rates and
  residual values, and both are reported. (b) The funding side is not deposits but capital-markets debt; the row names the
  risk of money raised "on a wholesale basis, and that money can run pretty fast" **[M2012-012]**. GATX's debt is unsecured
  term debt, weighted-average remaining term 8.2 years at 4.78% (10-K 2025, Item 7), maturing $653M in 2026, $855M in 2027,
  $825M in 2028, $907M in 2029 and $3,660M in 2030 (of which $2,959M is the GABX term loan GATX guarantees): it cannot be
  called on demand, but it must be refinanced as it falls due. (c) The finance-company row is the one that bites: "I don’t
  understand that — whether I can continually fund it [...] So, even though I could understand every individual transaction
  they did, I don’t regard the whole enterprise, or the operation of it, necessarily as being within my circle of
  competence." **[M2002-094]**. GATX's record answers it in part: it has borrowed on its own unsecured credit in every year of
  the cash-flow statements read, 2011 to 2025, including 2020, and the refinancing need is stated by year. What remains is the
  price of that funding against rivals' (a Q2 matter) and the amount of it (a Q9 matter), not an unreadable balance sheet.
  (d) A high return on equity in a business that deals in something close to a commodity is read for how much of it is
  gearing **[M2007-013]**; that reading is done at Q2.
- **The doubt test** **[M2002-092]**: my doubt is about whether the business is a good one, not about whether I can see it.
- **VERDICT: IN.** The ten-year economics of GATX, lease rates that cycle around a slowly changing fleet of long-lived cars
  funded by laddered term debt, can be bounded from its own fifteen-year record **[M2012-065]**, **[M2008-033]**, and the
  variables that matter are knowable **[M2006-076]**. Filing facts: 10-K 2025 Item 1 (fleet, lives, customers, lease terms),
  Item 7 (LPI, debt term and rate, maturities), 10-Q 2026 Q2 (GABX). The funding doubt **[M2002-094]** is carried to Q2 and Q9.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (business of parts, Q2's CONVENTION; segment profit as the filer defines it, after allocated interest and
before corporate SG&A and tax; 10-K 2022 `0000040211-23-000023` for 2021 and 2022, 10-K 2025 `0000040211-26-000018` for 2023 to
2025; $M):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five years | Share | Decides |
|---|---|---|---|---|---|---|---|---|
| Rail North America | 285.4 | 321.3 | 307.3 | 356.0 | 351.8 | 1,621.8 | 59.6% | yes (more than half) |
| Rail International | 105.0 | 85.9 | 113.4 | 119.8 | 125.9 | 550.0 | 20.2% | no |
| Engine Leasing (RRPF affiliates, GEL) | 60.8 | 14.7 | 106.4 | 117.3 | 181.5 | 480.7 | 17.7% | no |
| Other (Trifleet) | -1.3 | -3.9 | 29.2 | 12.9 | 29.5 | 66.4 | 2.4% | no |
| Total | 450.0 | 418.0 | 556.3 | 606.0 | 688.7 | 2,718.9 | | |

Rail North America carries more than half of five-year segment profit and decides; from 2026 it also holds GABX. The file
closes on its castle. The other parts are not judged here (Engine Leasing's joint ventures with Rolls-Royce earn more on their
capital than the rail parts on the filer's figures, and are recorded under AFTER THE STOP).

**The castle tests, on Rail North America, each with its filing fact.**
- **What keeps it standing, and how permanent** **[M1995-038]**. The filer names its own competitive factors: "availability of
  railcars, maintenance capabilities, lease rate, lease structures, customer relationships, and engineering expertise" (10-K
  2025, Item 1). The standing parts are real: a fleet of about 107,600 cars across tank and freight types, six major
  maintenance facilities and about 36,000 service events a year, full-service leases, 127 years of operation, and an average
  of 102,000 to 106,000 non-boxcar cars on lease in every year 2015 to 2019. None of them depends on a superstar; the castle
  passes the lord test.
- **The money test** **[M2011-015]**, **[M2000-077]**. A well-funded entrant can buy a fleet, and does: Wells Fargo, a bank,
  assembled about 101,000 operating-lease railcars and sold them for about $4.2B; Brookfield, an infrastructure investor,
  put up 70% of the equity to buy them (10-K 2025, Item 1); First Citizens holds about 128,400 railcars and locomotives in its
  Rail segment (FCNCA 10-K 2025, `0000798941-26-000015`); Trinity and Greenbrier build cars and lease them. The 10-K's own
  risk factor: "decreasing interest rates may invite new competition". New capital enters this field whenever the return on
  a railcar looks good, which is the failing answer: "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**.
- **Pricing power and the agony before a price rise** **[M2005-020]**. The price behaviour over a full cycle is the filer's
  own LPI: renewal rates fell against expiring rates in each of the six years 2016 to 2021 (-20.3%, -28.2%, -9.8%, -3.9%,
  -23.5%, -8.5%), and the filer gave the reason in 2017: "Challenging conditions continued in the North America railcar
  leasing market in 2017 due to the oversupply of existing railcars and continued delivery of new cars into the market." (10-K
  2017, `0000040211-18-000023`). Utilization stayed at 98% to 99% because price gave way, and the renewal success rate fell to
  66.7% (2016) and 70.8% (2020). The lease rate is set by the industry's car supply against shippers' demand, not by GATX:
  the business whose price the field sets, "whatever he charged for gas was my price." **[M2012-109]**. The rise since 2022
  is the same mechanism in reverse (car deliveries fell; renewal rates rose 22% to 34%), not a power GATX holds.
- **The low-cost position** **[L2004-007]**, **[M1997-010]**. In a lessor the largest cost after the car itself is the money.
  The filer concedes rivals with "higher credit ratings, and a lower cost of capital" and rivals that "manufacture railcars for
  their own leasing businesses" (10-K 2025, Item 1A); it buys its cars from those same manufacturers under supply agreements.
  The rows name exactly this disadvantage in leasing: "The banks have an advantage over us because their cost of funds is so
  low now. [...] So, pure money-type leasing is not an attractive business for us when we’ve got other people with a lower
  cost of funds." **[M2016-029]** (a row about leasing new automobiles, weighed, not deciding alone). GATX's edge is service,
  the maintenance network; its funding is not the cheapest in the field.
- **Brand, and the low bid** **[L2004-003]**, **[M2017-009]**. "Patents, trademarks, and licenses are not material to our
  businesses taken as a whole" (10-K 2025, Item 1). Lease rate is one of the competitive factors the filer lists, and the
  renewal record shows customers leaving when rates are lower elsewhere (renewal success 66.7% in 2016, 70.8% in 2020).
  Service is a route out of the commodity class the rows name, where "the people care enormously about service and the
  assurance of safety" **[M2001-014]**; GATX's full-service lease of hazardous-materials tank cars is that route, and the price
  record above shows it did not hold the price through the downturn.
- **Widening or narrowing** **[M1999-108]**. On the filer's own returns (below), the present upswing (2023 to 2025, return on
  capital 6.4% to 6.9%) has not reached the last one (2013 to 2016, 8.2% to 9.0%); no widening is shown.
- **What could destroy, modify or reduce it** **[M2000-014]**. The filer names faster railroads: "If PSR results in
  substantial increases in train velocity or decreases in dwell time for rail assets, the resulting excess supply of railcars
  and/or locomotives may adversely impact the demand for our rail assets." (10-K 2025, Item 1A); and oversupply from new-car
  deliveries, as in 2016 to 2021.

**The competitor row** (the rivals the 10-K names for Rail North America: Union Tank Car Company, CIT Rail, Trinity Industries
Leasing Company, American Industrial Transport; and in locomotives CIT Rail and LTEX Rail). Two file with the SEC: Trinity
Industries (its Railcar Leasing and Services Group) and First Citizens BancShares (CIT Rail is its Rail segment). Flagged as not
filing their own statements with the SEC: Union Tank Car Company, American Industrial Transport, LTEX Rail; the European rivals
of Rail International (VTG, Streem, Wascosa, Touax) do not file either. Same metric for all three: pre-tax operating profit
before interest, on the capital of the leasing business. The metric is the filer's own figures recombined; the definitions
differ by filer and are stated.

| Lessor | Metric | Years | Result | Source |
|---|---|---|---|---|
| GATX, consolidated | (net income + income taxes + interest expense) / average (debt + GATX equity) | 2013 to 2025 | 5.2% to 9.0%, mean 6.9%; trough 5.2% to 5.4% (2020 to 2022); its own interest cost averaged 3.9% | 10-Ks listed in Step 0; `returns.py` |
| Trinity, Railcar Leasing and Services Group | segment operating profit (before interest) / segment total assets at year-end | 2019, 2020, 2024, 2025 | 5.7%, 5.2%, 5.7%, 6.7% (2025 excludes the one-off $194.2M gain on the Triumph divestiture) | TRN 10-K 2020 `0000099780-21-000012`; 10-K 2025 `0000099780-26-000014` |
| First Citizens, Rail segment (CIT Rail) | (income before taxes + net interest expense) / operating lease equipment at year-end | 2023, 2024, 2025 | 3.3%, 3.8%, 3.7% | FCNCA 10-K 2025 `0000798941-26-000015`, Table 16 |

Two warnings on the comparison, written down as found **[M1997-127]**: Trinity carries its fleet at its own manufacturing cost
(its 2020 Leasing Group table eliminates $820.3M of deferred profit), which flatters its return on assets; First Citizens'
fleet was marked to fair value when it bought CIT in 2022, so its figure is the closest of the three to a return on what a
fleet costs today. GATX's figure includes the Rolls-Royce engine affiliates, which earn more than the rail parts, and before
2019 left out its leased-in railcars, which were then off the balance sheet; both flatter GATX's rail return. Before 2019 the
GATX figure also carries American Steamship, sold in 2020.

**The field's returns over the last full cycle, judged in words.** The filer's cycle is plain in its own index: renewal
rates rising 2011 to 2015, falling 2016 to 2021, rising 2022 to 2026. Over that full cycle GATX earned a pre-tax return on
all its capital of about 5% to 9%, against an interest cost on its own debt of about 4%; after tax at a quarter, that is
roughly 4% to 7% on the capital, which is about what a long government bond paid in the same span. Its return on equity of 7%
to 13% (2018 to 2025) is made by debt of 2.5 to 3.5 times equity: a high reported return is to be read for "a cyclical peak in
earnings, a monopolistic position, or leverage" **[L1994-009]**, and of leverage the rows say "we could make it almost any
number you want if we just used enough leverage" **[M2001-054]**; in a business dealing in something close to a commodity,
"part of that is because the banks are geared up more" **[M2007-013]**. The rivals that file earn the same or less: Trinity's
leasing group about 5% to 7% before interest on a fleet at manufacturing cost, First Citizens' rail fleet under 4% on a fleet at
recent fair value. These are ordinary returns, and the castle that stands protects them, not "excellent returns on invested
capital" **[L2007-004]**; "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**, and here
there are many. The moat is judged, not measured **[M1999-108]**, and the judgment from the filings is that it is a durable
fleet in a priced-by-the-field market, earning a spread over its borrowing cost. A return set by a regulator is the
framework's one exception and does not apply: lease rates here are set by the market.

**A change for the better** **[M2017-026]**: the 2022 to 2026 upswing (renewal rates up, return on capital from 5.2% to 6.9%) is
credited only on a full cycle **[L1995-022]**, and on the cycle already completed the returns were ordinary at the peak as at
the trough; nothing in the present upswing exceeds the last one.

**Not TOO HARD:** the tenuous-moat row sends a castle to the "too hard" box because "We don’t know how to valuate that"
**[M2000-019]**; here the returns are known from the filings, so the box is OUT, as Q2's list says of the standing castle that
protects only ordinary returns.

- **VERDICT: OUT.** Rail North America, the deciding part, is a standing castle that protects only ordinary returns: lease
  rates set by the field's car supply (six straight years of falling renewal rates, 2016 to 2021), rivals with cheaper money and
  their own factories, new capital entering by the billion (Wells Fargo's fleet, Brookfield's 70%), and a full-cycle pre-tax
  return on capital of about 7% against a 4% cost of debt, matched or undercut by the filing rivals **[L2007-004]**,
  **[M2012-109]**, **[M2011-015]**, **[M2001-054]**. The file closes here. Q3 to Q12 are NOT REACHED; the arithmetic below is
  COMPUTATION, NOT A CLEARANCE.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read for Q2 and the COMPUTATION; what they show is under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. One fact bearing on it is under AFTER THE STOP (the published earnings estimate); it is recorded, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. The buyback prices against the computed range are under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The value range and the fair price, at the owner's request, are in the COMPUTATION below.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. The debt facts are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (not asked by the operator).

## COMPUTATION, NOT A CLEARANCE (Q7's arithmetic after the Q2 STOP, at the owner's request; operator rule 3)
Nothing in this section is a verdict or entry language. The file is closed at Q2.

**Owner cash, recast from the filed statements** (`q7.py`, output in `q7_output.txt`; $M). For a lessor the cash-flow statement
splits fleet turnover in two: "Portfolio investments and capital additions" (cars, engines and containers bought, including
businesses and affiliates) and "Portfolio proceeds" plus "Proceeds from sales of other assets" (cars and other assets sold),
while operating cash has the gains on those sales taken out. Three cases:
- **Maintenance case (central, spec (e))**: operating cash less stock pay, less depreciation, plus net gains on disposal, less
  deferred income taxes. CONVENTION of this run: the maintenance outlay is depreciation net of the gain realised when used cars
  are sold; rationale: a fleet held level must buy back each year its depreciation plus the book value of the cars it sells,
  and the sale proceeds return that book value with the gain, so the net cost is depreciation less the gain. Depreciation is
  taken as the proxy the rows allow in most companies **[M1998-127]**; the rows also warn that in heavy-capital businesses it
  can fall short of what keeps the business in place **[L2015-004]**, **[M2016-092]**, and the filing allows no better guess,
  so the case flatters rather than understates. CONVENTION of this run: deferred taxes are charged as if paid, because they
  are deferred only while the fleet grows, and the case assumes it does not; the rows decline to treat deferred taxes as
  "a hidden form of equity" **[M2015-030]**.
- **All-spending case (beside)**: operating cash less stock pay, less all fleet spending and purchases of previously leased-in
  assets, plus portfolio and other sale proceeds (sale-leaseback proceeds left out as a financing).
- **Before interest (the all-equity basis)**: each case plus interest expense after tax. CONVENTION of this run: the tax on
  the add-back is 37% to 2017 and 24% from 2018 (the federal rate of each period plus state; the filed effective rates for 2023
  to 2025 were 22.6% to 23.9%); and the 2017 deferred tax line (-260.5, the tax-law remeasurement) is replaced by the mean of
  2016 and 2018 (45.5) so the charge is a normal year's.

| Year | Maint., after interest | Maint., before interest | All-spending, after interest | All-spending, before interest | Fleet spending beyond maintenance |
|---|---|---|---|---|---|
| 2021 | 176.6 | 331.6 | -477.5 | -322.5 | 688.3 |
| 2022 | 234.4 | 397.0 | -435.8 | -273.2 | 706.5 |
| 2023 | 202.6 | 402.8 | -869.9 | -669.7 | 1,110.8 |
| 2024 | 249.7 | 508.9 | -870.2 | -611.0 | 1,165.7 |
| 2025 | 257.6 | 555.1 | -396.8 | -99.3 | 707.6 |
| Mean 2021-2025 | 224.2 | 439.1 | -610.0 | -395.1 | |
| Mean 2014-2023 (cycle, beside) | 186.6 | 318.1 | | -144.5 | |

**The window and the cycle (spec (a)).** The filer does not call 2021 or 2025 a trough or a peak in words; its own index puts
2021 at the end of six years of falling renewal rates and 2025 in the fourth year of rising ones. The literal five-year window
2021 to 2025 is used as the central base, the more generous of the two; the cycle base, 2014 to 2023 (peak to peak of the
filer's LPI renewal-rate change, 38.8% and 33.5%; CONVENTION of this run, since the window spans one rising half only), is
shown beside. Before 2018 the figures include businesses since sold (American Steamship, Portfolio Management's marine
assets).

**Growth, the cap and the growth spending (specs (e) and (f)).** The shown growth of maintenance owner cash before interest,
2021 to 2025, is 13.75% a year; carried ten years it would take owner cash to about 51% of revenue against a highest share in
the filings read of 32.1% (2024), so the growth carried is the business's own revenue growth over the same window, **8.47%**
(the shown rate and the cut both written down, spec (f)). The growth is not free: GATX spent $3,690.6M beyond maintenance in
2022 to 2025 and maintenance owner cash before interest rose $223.5M, a return of **6.06%** after tax on the growth spending
(CONVENTION of this run: the return on growth spending is the rise in owner cash over the window divided by the spending
beyond maintenance in its last four years; rationale: spec (e) charges growth spending against the growth it buys and gives
no measure of the price of that growth; this one is the filer's own record, and it flatters, since part of the rise is the
lease-rate upswing on cars already owned). The growth case charges that spending each year, ten years, then no growth and no
spending.

**Acquisitions and GABX (spec (c)).** Fleet purchases from DB Cargo (2025, 5,882 cars) and the 2020 business purchase ($203.2M)
are inside the fleet spending above (deducted, total growth credited); net purchases of businesses over the window are small
against owner cash, so the serial-acquirer convention does not apply. GABX closed on 2026-01-01, after the window and before
the price date, and is a cash deal by GATX and Brookfield: valued on its own filed record, its financing in today's net debt.
Its record (10-Q 2026 Q2, note on GABX): six months to June 2026, income before taxes $6.1M, interest $80.5M, management fees
paid to GATX $24.9M (eliminated in consolidation). Annualised and taxed at 24%, **$169.5M** a year before interest for 100% of
GABX (CONVENTION of this run: the six-month record annualised; it is the higher of the two filed records, the 2025 pro forma
giving $128.2M). Because 100% of GABX's cash is counted, Brookfield's 66.5% is a claim ahead of GATX's shareholders: the
non-controlling interest at book, **$805.5M**, is added to net debt (CONVENTION of this run; rationale: the all-equity basis
counts market value plus net debt, and a consolidated joint venture's minority owner is paid before GATX's owners on the
cash counted). The 8-K/A's pro forma combined statements show GABX adding $0.6M to GATX's 2025 net income.

**Net debt** at the latest filed date, 2026-06-30 (10-Q): debt $12,333.3M less cash $747.1M and restricted cash $0.1M =
**$11,586.1M**; operating lease obligations ($143.8M) left out, as the convention says. No later filing states a subsequent
event that changes it. Enterprise value at the price: $5,820M + $11,586.1M + $805.5M = **$18,212M**.

**The range, all-equity basis (central), discounted at the sovereign 5.43%, ten years then zero growth:**

| Case | Owner cash before interest, incl. GABX | Whole business | Per share, less net debt and minority |
|---|---|---|---|
| No growth, window base | 608.6 | 11,208 | **-$33.54** |
| Growth 8.47%, spending charged at 6.06%, window base | 608.6 rising | 12,825 | **$12.28** |
| No growth, cycle base (beside) | 487.6 | 8,979 | -$96.65 |
| Growth, cycle base (beside) | 487.6 rising | 10,275 | -$59.94 |
| All-spending, window base, no growth (beside) | -225.6 | negative | -$468.69 |

**VALUE RANGE (reporting figure): -$33.54 to $12.28 a share, all-equity basis, against $164.85.** The literal window and the
cycle base are both shown above. The floor is tested first: at the price, the no-growth case returns 3.34% on enterprise value
(608.6 on 18,212) and the growth case 4.38% (the rate that equates it to enterprise value); on the cycle base, 2.68% and 3.79%.
**No case earns the floor of about ten percent; the close under Q7 would be OUT** **[M2003-149]**, whatever the width, and a
price above the top of the range closes OUT by the same convention. The width test does not arise; with a negative bottom the
ratio has no meaning.

**FAIR PRICE (reporting figure, Part VII; after the company's own tax, no conversion): -$212.97 a share on the all-equity
basis (central)**: each end case valued at ten percent instead of the sovereign (no growth -$178.61, growth -$247.32; growth
lowers value at ten percent because the growth spending earns 6.06%), averaged. Read plainly: at the floor of ten percent,
the window's owner cash before interest is worth less than the net debt and the minority's claim, so there is no positive
price at which the midpoint earns the floor. On the cycle base the figure is -$240.41.

**Equity-only basis, beside, never deciding alone:** owner cash after interest, window mean 224.2 plus GATX's after-interest
share of GABX (33.5% of its net income and the fees borne by Brookfield's 66.5%, after tax) 26.3 = 250.5, a 4.30% yield on the
market value of $5,820M. No growth: $130.66 a share at 5.43%, $70.95 at ten percent. Growth: $223.05 at 5.43%, $100.74 at ten
percent, where the equity pays only 11.4% of the growth spending because 88.6% of the net fleet investment of 2022 to 2025 was
matched by new net debt (net debt excluding GABX rose from $5,562M to $8,832M), which makes the equity's return on its share
of the spending 19.3%. **Fair price, equity-only: $85.85 a share.** This is the per-share magnification of a debt-financed
business that the all-equity basis exists to refuse **[L2017-004]**; and the window's after-interest mean understates today's
interest (expense $204.0M in 2021, $391.5M in 2025), so it flatters as well.

**The literal three-year window of `tools/run.py`** (2021 to 2023, capex basis -846.1, depreciation basis 123.6) is not used:
its capex column omits portfolio proceeds and its depreciation column omits the gains, as said in Step 0.

---
## THE BOX
**OUT at Q2** (Rail North America, the deciding part: a standing castle that protects only ordinary returns). COMPUTATION
beside the price: all-equity range -$33.54 to $12.28 a share against $164.85; no case earns the floor (3.3% to 4.4% on
enterprise value); fair price -$212.97 all-equity ($85.85 equity-only).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.

**Bearing on Q3 (capital).** GATX must keep buying cars: purchase commitments of $1,643.7M for 2026 to 2030, mainly railcars,
including the Trinity agreement for 15,000 cars through 2028, of which 8,133 were ordered and 5,720 delivered by 2025-12-31
(10-K 2025). Fleet spending beyond maintenance was $3,690.6M in 2022 to 2025 against a $223.5M rise in maintenance owner cash
before interest (6.06% after tax). Pre-tax return on all capital 5.2% to 9.0% in 2013 to 2025 (`returns.py`). The 2026 year to
date investment volume was $4.7B including GABX (Q2 release). Residual values, read as net gains on asset dispositions ($M): 80.7
(2013), 79.3, 99.7, 52.9, 52.5, 79.3, 56.2, 39.5 (2020), 99.4, 121.2, 130.9, 137.8, 140.0 (2025); in 2025, $118.9M of the $136.9M
segment total was gains on dispositions of owned assets (10-K 2025, segment note). The gains of 2025 equal half of income before
taxes and affiliates' earnings ($140.0M against $279.1M); they fell to $39.5M in the trough year 2020.

**Bearing on Q4 (the accounts; the balance sheets 2016 to 2025, `run_py_output.txt` checked against the filed statements).**
Total assets rose from $7,105M to $18,000M; GATX equity from $1,347M to $2,750M, of which retained earnings $1,828M to $3,451M;
long-term debt from $4,286M to $12,506M (2025 includes the $2,959M GABX loan, with $4,241.9M of restricted cash held for the
purchase); goodwill small throughout ($78M to $144M; $123.4M at 2026-06-30); receivables small against a lease book. The
deferred income tax liability was $1,195.7M at 2025-12-31. Equity-method affiliates (the Rolls-Royce joint ventures) earned
$117.3M after tax in 2025 and paid $50.0M in dividends; operating cash counts the dividends, as the framework's equity-method
convention asks. The 10-K carries a "Non-GAAP Financial Measures" section; the second-quarter release leads with GAAP net income
per share. No figure was found that confused; the accounts read plainly.

**Bearing on Q5 (people; recorded, not judged).** GATX publishes a full-year earnings estimate per diluted share and raised it
on 2026-07-30 to $9.90 to $10.30 (8-K `0000040211-26-000073`); the rows on guidance and on hitting the number (**[L2019-006]**
among the Q5 tests) would read it there. The proxy was cached and not read. Integrity facts: none found beyond this habit; the
box line does not carry the integrity flag, since no fact bearing on honesty was found.

**Bearing on Q6 (money and owners).** Buybacks name no price: $65.0M for 416,699 shares in 2025 (about $156 a share) and $21.9M
for 167,452 in 2024 (about $131); treasury stock rose by 272,981 shares and $51.4M in the first half of 2026 (about $188, which
may include shares withheld for tax; not separated). All sit above the bottom of the all-equity range computed above
(-$33.54), and above its top. A new $300M programme was approved on 2026-02-18 with no price stated (10-K 2025, Item 5). Diluted
shares fell from 47.6M (2012) to 35.9M (2025). Dividends paid every quarter since 1919 (Q2 release). The GABX structure gives
GATX annual call options toward 100%; the first was exercised on 2026-06-30 for $66.2M, taking it to 33.5%.

**Bearing on Q9 (debt and exposures).** Consolidated debt $12,333.3M at 2026-06-30 against GATX shareholders' equity of
$2,784.4M; the filer's "recourse leverage" (debt and lease obligations net of cash, over total equity including the minority)
was 3.3 at 2025-12-31. Maturities: $653M (2026), $855M, $825M, $907M, $3,660M (2030) and $5,605M thereafter; weighted remaining
term 8.2 years at 4.78%. GATX guarantees the whole GABX term loan ($2,959M at 2025-12-31, $2,860.2M at 2026-06-30) while owning
33.5%; the GABX loan carries an asset-coverage covenant (a ratio not to exceed 0.85 to 1.0). Some derivative contracts "could
require us to make immediate payment on net liability positions in the event that we default on certain outstanding debt
obligations" (10-Q 2026 Q2). The filer relies "largely on the capital markets and banks to fund our operations" and names
ratings as the gate to that funding (10-K 2025, Item 1A); this is what the rows ask of a borrower that must refinance
**[L2010-020]**, **[L2014-023]**. Pre-tax earnings including affiliates before interest covered interest about 2.1 times in
2025 ((436.1 + 391.5) / 391.5). Exposures: the owner of a leased hazardous-materials car may be liable for a spill "without regard
to the owner’s fault" (10-K 2025, Note 24); Norfolk Southern's third-party claims against GATX over the East Palestine derailment
were dismissed in 2024 and the other East Palestine litigation against GATX is resolved; subsidiaries face asbestos claims; the
litigation accrual was $4.6M.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the first analyst, commit `0c41b965`); written question by question;
      committed after each by pathspec: Q1 `12093a2c`, Q2 `f2f35b2c`, and the close.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is held by the dispatching session (not checked
      here; this analyst wrote no lock); the fold into the register is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what the session context showed by
      accident is declared under contamination at the top and was not used.
- [x] Every v5 id resolves (`check_ids.py`: no E-ids, every M/L/R id in `principle_ledger_v5.csv`, every quoted fragment beside
      an id found in that row); every filing fact carries its document and accession; numbers not from a filing are labelled
      CONVENTION of this run.
- [x] The order was kept; Q2's STOP closed the run; everything after it is NOT REACHED or COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay, depreciation, deferred taxes charged), never a net-income proxy; the
      sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (THE FOUNDATIONS, and the warnings under the competitor row); facts for later
      questions under AFTER THE STOP; no integrity flag, since none was found.
- [x] No point-in-time anchor; every row cited is from the v5 ledger, none dated after today.
- [x] Only the arithmetic lines of `tools/run.py` were used, and those not used are named with the reason.
- [x] `python tools/check_framework.py` PASS before the final commit.
- Honest limits: the competitor comparison uses three different definitions of capital (stated in the table); Trinity's
  2015 to 2018 leasing assets were not extracted, so its cycle coverage is four years, not thirteen; First Citizens' rail
  figures exist only from 2022 under that owner; GABX's record is six months; the proxy was not read (the file closed before
  Q5); the price is one aggregator quote.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Maintenance capital for a lessor.** Q7's specific (e) puts the maintenance case at the centre "where the filing allows
the guess", but a lessor's fleet turnover runs through two investing lines (purchases and portfolio proceeds) and the gains on
sale are taken out of operating cash; nothing says how proceeds and gains sit against maintenance. `tools/run.py` omits both,
and its two bases come out at -846.1 and 123.6 for the same years. I used depreciation net of the gain on sale, as a CONVENTION
of this run. (2) **The price of growth.** Spec (e) charges growth spending "against the growth it buys" and spec (f) caps the
rate, but neither says how to measure what a dollar of growth spending buys; I used the filer's own record over the window,
which flatters in an upswing. (3) **A consolidated joint venture with a minority owner.** The all-equity basis is "market value
plus net debt"; a consolidated 33.5%-owned joint venture puts 100% of its debt and cash in the statements and a minority claim
ahead of the shareholders, which the text does not mention; I added the minority interest at book to the claims. (4) **Deferred
taxes in a growing lessor.** The text does not say whether owner cash should charge deferred taxes that are deferred only while
the fleet grows; I charged them in the no-growth case, on **[M2015-030]**. (5) **The lender-funded lessor at Q1.** The bank
door and the finance-company row **[M2002-094]** sit in Q1, but the framework routes only banks and derivatives books; a
lessor with a readable asset side and wholesale term funding is not named, and I had to choose between Q1 TOO HARD on the
funding doubt and carrying it to Q2 and Q9 (I carried it). (6) **"Ordinary" returns.** Q2's convention judges them in words
with no benchmark; I set GATX's pre-tax return on capital against its own cost of debt and the long bond, which is my reading,
not the text's.
