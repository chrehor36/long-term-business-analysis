# Company Run: SkyWest, Inc. (NASDAQ: SKYW), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is closed to this session by the blind rule of
the dispatch; whether the operator holds SKYW is unknown to this analyst.

**CONTAMINATION, declared.** Seen before or during the run, none of it opened: the commit subjects in the session header
(CENT, OGN, PENN, YELP v5 runs and a session-state commit); untracked file names in `git status` (CALY, PRKS, TDS runs of
2026-10-05, AYI and ARCB research folders); the memory index line "57 gate-clearers, nothing buyable"; the file name
`Test Runs/2026-07-15 Run - SWKS (Skyworks Solutions).md` (a different company) returned by a name search. No SkyWest file
existed in `Test Runs/` before this one. `tools/run.py` printed v4-era headings (owner-earnings yield, points over the
sovereign); no id, rule or verdict was printed and none was used.

**Analyst's incentive (operator rule 9).** None held. The pull is the other way: a run that closes early is cheap.
The counter-case was therefore written out in full at Q2 before the verdict.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $96.06 (2026-10-05; `tools/run.py` live quote, **aggregator, flagged** per operator rule 5).
- **Shares:** 38,828,325 common, no par, one class (10-Q for the period ended 2026-06-30, filed 2026-07-24, accession
  `0001104659-26-086641`, cover; `python Screens/cover_shares.py SKYW`). Issued count 85.38M includes treasury stock;
  not used.
- **Market cap:** 38.828M x $96.06 = **$3,730M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, 30-year par yield, US Treasury daily par yield curve,
  2026-10-05 (`python tools/sources.py`).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-17, accession `0001104659-26-016358`: Items 1, 1A, 2, 5, 7, 7A and 8 (statements, notes
    on deferred revenue, the auditor's critical audit matter).
  - 10-Q for the quarter ended 2026-06-30, filed 2026-07-24, accession `0001104659-26-086641` (balance sheet, fleet
    outlook, deferred revenue note).
  - 8-K of 2026-07-23, accession `0001104659-26-086251`, and its Ex. 99.1 (Q2 2026 results; $250M buyback increase).
  - DEF 14A for the 2026 meeting, filed 2026-03-25, accession `0001104659-26-034497` (board, pay; read only far enough
    to record two facts, since Q5 and Q6 were not reached).
  - Older 10-Ks for the span: FY2014 `0001047469-15-000907` (2014 loss, ExpressJet), FY2015 `0001558370-16-003629`,
    FY2016 `0001558370-17-001066` (the $465.6M impairment; the Delta "competitive base rate costs" clause), FY2018
    `0001558370-19-000847` (ExpressJet sale; 2016-2018 cash flows), FY2020 `0001558370-21-001367` (CARES Act grants,
    loans and warrants; 2018-2020 cash flows), FY2022 `0001558370-23-001442` (2021 grants and impairment; 2020-2022 cash
    flows).
  - Competitors, their own filings: Mesa Air Group 10-K FY2024 (`0000950170-25-070705`); Republic Airways Holdings
    (old registrant) 10-K FY2015 (`0001159154-16-000178`); Republic Airways Holdings (the former Mesa registrant after the
    2025 combination) 10-K FY2025 (`0001628280-26-019614`).
- **One figure cross-checked against the filed statement:** total assets at 2025-12-31, $7,386M in the XBRL table,
  = $7,386,249 thousand on the filed balance sheet (10-K FY2025). Operating cash flow 2025, $940.4M, = $940,364 thousand
  on the filed cash-flow statement. Both agree.
- **`tools/run.py` arithmetic lines, checked line by line, and one line REJECTED.** The tool's capex series is the XBRL
  tag `PaymentsToAcquirePropertyPlantAndEquipment`, which SkyWest uses only for "Buildings and ground equipment" ($32.0M
  in 2025). The aircraft line, "Aircraft and rotable spare parts" ($546.0M in 2025), and "Deposits on aircraft" ($75.3M)
  are missing from it. The tool's "OE capex" mean of $741.1M and its 19.87% "yield" are therefore wrong by roughly the
  whole aircraft budget and are not used anywhere below. Its OCF, SBC and D&A lines match the filed statements; its
  balance-sheet table matches the filings at the years checked. Owner cash below is rebuilt from the filed cash-flow
  statements (`Test Runs/_research 2026-10-05 SKYW/owner_cash.py`).

**Who pays for the aircraft (read before any arithmetic).** The 10-K FY2025, Item 1: under the capacity purchase
agreements "our major airline partners compensate us for our costs of owning the aircraft on a monthly basis. The
aircraft compensation structure varies by agreement but is intended to cover either our aircraft principal and interest
debt service costs or our aircraft depreciation and interest expense while the aircraft is under contract." That money
arrives as revenue and so sits inside operating cash flow; SkyWest buys the aircraft with its own cash and secured debt
($2.2B of its $2.4B debt finances aircraft and spare engines). Some aircraft are supplied by the partners: 51 E175s and
20 CRJ900s are "aircraft we lease from our major airline partners for a de minimis monthly cost" (Item 2). So the capital
the owner supplies is the purchase of SkyWest-owned aircraft; the partner's reimbursement is earnings, received over a
contract shorter than the aircraft's life, and the residual is SkyWest's.

### Owner cash, from the filed cash-flow statements (USD millions; COMPUTATION — NOT A CLEARANCE)
OCF less stock pay less all capital spending (aircraft and rotables, buildings, aircraft deposits net of deposits
returned, less proceeds of disposals). "Normalized" removes two things that are not earnings of the business: the CARES
Act payroll grants inside OCF ($345.5M in 2020, $422.7M in 2021; FY2020 and FY2022 10-Ks) and the swing in deferred and
unbilled revenue (cash taken ahead of, or behind, revenue under the capacity purchase agreements; +$242.5M in 2023 alone).

| Year | OCF | Stock pay | Net capex | D&A | Owner cash, raw | Owner cash, normalized (capex basis) | Normalized, D&A basis |
|---|---|---|---|---|---|---|---|
| 2016 | 506.7 | 7.6 | 1,061.0 | 285.0 | -561.9 | -561.9 | 214.1 |
| 2017 | 684.1 | 10.6 | 646.8 | 292.8 | 26.7 | 26.7 | 380.8 |
| 2018 | 802.5 | 13.1 | 1,089.2 | 334.6 | -299.7 | -299.7 | 454.8 |
| 2019 | 721.0 | 10.3 | 642.4 | 368.1 | 68.4 | 68.4 | 342.7 |
| 2020 | 633.6 | 6.8 | 416.8 | 475.0 | 209.9 | -246.3 | -304.4 |
| 2021 | 831.8 | 8.7 | 641.3 | 440.2 | 181.8 | -225.6 | -24.5 |
| 2022 | 480.4 | 9.2 | 527.2 | 394.6 | -56.0 | -85.3 | 47.3 |
| 2023 | 736.3 | 17.1 | 288.8 | 383.1 | 430.4 | 187.9 | 93.6 |
| 2024 | 692.5 | 19.9 | 323.1 | 383.9 | 349.5 | 397.4 | 336.6 |
| 2025 | 940.4 | 18.7 | 637.8 | 364.5 | 283.9 | 346.1 | 619.4 |
| **5-yr mean 2021-25** | | | 483.7 | 393.2 | 237.9 | **124.1** | 214.5 |
| **10-yr mean 2016-25** | | | 627.4 | 372.2 | 63.3 | **-39.2** | 216.0 |

Over ten years the business produced $7,030M of operating cash and spent $6,274M of net capital; after the $768M of
government grants are taken out, the owners' residual was negative. The 2019 ExpressJet sale proceeds ($53.2M) are left
out as non-recurring; the 2016 residual-value-guarantee settlement ($90.0M) is left in, as a disposal of aircraft.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own it "if the market closed for five years"
**[M1997-109]**, which for SkyWest means owning a contract operator whose four customers set its schedule, its aircraft
type and, at each renewal, its rates. The market is "there to serve you and not to instruct you" **[M2006-077]**: the stock's rise from an
indexed 40.96 at end-2022 to 249.09 at end-2025 (10-K FY2025, Item 5 performance graph, base 100 at end-2020) is a price
history, not evidence about the castle. No macro forecast enters, "we just don’t get into the macro factors" **[M2000-094]**; the pilot shortage is treated below as
a property of the business (who controls the key input), not as a forecast. The analyst's habit used most: "What do I
not know that I need to know?" **[M1999-129]**, and the search for "what’s wrong in things" **[M2025-013]**.

**Contrary evidence, written down as found**, "write it down in the first 30 minutes" **[M1997-127]**:
1. (Step 0) The tool's owner-cash figure was overstated by the whole aircraft budget; the business looks far richer
   through it than through its filed cash-flow statement.
2. (Step 0) Over 2016-2025, normalized owner cash on the capex basis averaged -$39.2M a year.
3. (Item 1A) "Our major airline partners are not prohibited from doing so under our code-share agreements" (flying
   their own regional jets or giving the flying to another regional).
4. (Item 1A) "Certain of our competitor regional airlines may agree to flying contract terms at lower rates or
   unfavorable contract terms, which could affect the terms offered to us."
5. (Item 1A) Partners have shifted the contracts toward "a lower percentage of contractual fixed monthly payments and a
   higher percentage of contractual variable payments."
6. (FY2016 10-K) The Delta agreements then allowed termination "if SkyWest Airlines fails to maintain competitive base
   rate costs", with multi-year rate resets on the CRJ fleet.
7. (FY2014, FY2016, FY2022 10-Ks) Fleet decisions taken by partners produced impairments of $74.8M (2014), $465.6M
   (2016), $84.6M (2021) and $51.4M (2022, assets held for sale), plus $21.9M special items in 2019.
8. (FY2020 and FY2022 10-Ks) The 2020 and 2021 results depended on $768.2M of government payroll grants; 2020 was a
   pre-tax loss even with them.
9. (DEF 14A 2026) In May 2023 the company gave employees, named executives included, "new opportunities to earn
   compensation that approximated the amount of compensation that was capped by the PSP Agreements", i.e. a make-whole
   for the pay limits that were a condition of the taxpayer support. Recorded for Q5 and Q6, which were not reached.
10. (Item 7, 10-K FY2025) D&A fell in 2025 partly "as a result of extending the estimated useful lives on our
    CRJ700/CRJ550 fleet by an average of three years" in Q4 2024; an estimate change that lowers the charge.
11. (Item 8, 10-K FY2025) The auditor's critical audit matter is the deferred revenue calculation, which rests on
    "forecasted block hours over the remaining contract term."

Evidence for the business, written down as found, so that the other side is stated: SkyWest survived when Republic
filed for Chapter 11 (2016) and Mesa reported substantial doubt as a going concern (FY2024); it was awarded new E175
flying by American (11 aircraft, 8-K of 2026-07-23), Delta (16) and United (8); it extended 40 United and 13 Delta E175
contracts in January 2026 (10-K FY2025, Item 1); and its 2024-2025 operating margins (14.0%, 15.2%) exceed the combined
Republic's (about 9-10%).

## THE STANDING RULE
A purchase of SkyWest common stock with cash, unlevered and sized within the buyer's means, cannot ruin the buyer: "borrowed money has no place in the investor's tool kit"
**[L2014-005]**, nothing that risks "what we have and need" **[M2012-081]**. The target's own debt is Q9's
matter and was not reached.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years" **[M2012-065]**, and it concerns the economics, not the product: "What is important is that I
understand the economic dynamics of the industry. Is there" ... "are there competitive moats? Is there ease of entry?"
**[M2011-014]**. The first step is to identify "the key variables in that particular business, and evaluating how
predictable they were" **[M1998-044]**.

**The key variables, from the filing.**
1. *The contract rates at renewal.* About 84% of 2025 flying revenue came from capacity purchase agreements (10-K FY2025,
   Item 7); the partner "controls scheduling, ticketing, pricing and seat inventories", and pays fixed rates per
   departure, block hour and aircraft. Individual aircraft come off contract between 2026 and 2034.
2. *Utilization, which the partner schedules and the pilot supply limits.* Block hours fell in 2022 and 2023 because
   captains left for the majors; they rose 14.7% in 2025 when captains were available (Item 1).
3. *Labor cost against the rates.* Salaries, wages and benefits were 45.3% of operating costs in 2025; 93.0% of
   code-share operating costs are "reimbursable at pre-determined rates", so a wage rise not matched at the next rate
   negotiation is SkyWest's loss (Item 1A).
4. *The aircraft and its residual.* SkyWest buys the E175s (firm commitments for 69, $2.28B), the partner reimburses
   ownership cost "while the aircraft is under contract", and the residual after the contract is SkyWest's (Items 1, 7).
5. *Scope clauses*, which cap how many regional aircraft, and of what size, each partner may use (Item 1).

**Are they foreseeable?** The economic dynamics are legible from the filings: a supplier of contract capacity to four
buyers, three of which own regional carriers of their own, with entry open to anyone who can certify an airline and
finance aircraft. That is enough to answer the M2011-014 questions, and the answers are the substance of Q2. What cannot
be written down ten years out is the level of the rates and the pilot market, but that is a judgment about who holds the
power in the negotiation, which Q2 owns; the industry is not one of "fast-moving technology" **[L1993-023]**, and the
routing rule sends a business to Q1 TOO HARD only when change in the industry puts the ten-year economics out of reach.
The doubt rule was weighed, "if you have doubts about something being into your circle of competence, it isn’t"
**[M2002-092]**: the doubt here is not whether I understand how the business makes money but
whether its terms will hold, which is the castle question. The filings let me see the industry well enough to judge the
castle, so the file passes to Q2.

**VERDICT: IN** **[M2012-065]**, **[M2011-014]**, **[M1998-044]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now. What are the key factors? And how permanent are they?" **[M1995-038]**

**Who the customer is.** SkyWest's customer is not the passenger. As of 2025-12-31, 353 of its 487 aircraft in scheduled
service flew for United or Delta (Item 1A); 46.2% of aircraft flew for United at 2026-06-30 (10-Q). The passenger buys a
United, Delta, American or Alaska ticket on a United Express, Delta Connection, American Eagle or Alaska aircraft.

**The castle tests, each with its filing fact.**

1. *The attacker with money.* "and you can create another airline" ... "Very easily, and you have people that like to do
   it" **[M2013-054]**. The filing's own competitor list: CommuteAir, Endeavor (owned by Delta), Envoy, PSA and Piedmont
   (owned by American), Horizon (owned by Alaska), GoJet, Republic (10-K FY2025, Item 1). Three of SkyWest's four customers
   own a rival, and "regional carriers owned by major airlines may have access to greater resources than we do through
   their parent companies." The attacker does not need to build a castle; the customer already owns one.
2. *Pricing power, and the agony before a rise.* "you can almost measure the strength of a business over time by the
   agony they go through in determining whether a price increase can be sustained" **[M2005-020]**. SkyWest does not set
   a price; the rates are negotiated with the buyer. The filed terms have moved against it: the FY2016 10-K's Delta
   agreement allowed termination "if SkyWest Airlines fails to maintain competitive base rate costs" and carried
   "multi-year rate reset provisions"; the FY2025 10-K says compensation has shifted to "a lower percentage of contractual
   fixed monthly payments and a higher percentage of contractual variable payments", moving utilization risk from the
   partner to SkyWest; and in 2014 United shortened the ExpressJet ERJ agreement from 2020 to 2017, triggering an
   impairment (FY2014 10-K).
3. *The rival sets the price.* "whatever he charged for gas was my price" **[M2012-109]**; "he determined our profit,
   because we looked at his price every day" **[M2023-079]**. The filing's sentence: "Certain of our competitor regional
   airlines may agree to flying contract terms at lower rates or unfavorable contract terms, which could affect the terms
   offered to us" (Item 1A).
4. *Would the customer still choose it over the low bid?* The filer states how the customer chooses: majors "award
   code-share flying agreements to regional airlines based primarily upon" the ability to fly contracted schedules, labor
   availability, "low operating cost", financial resources, infrastructure and operating performance (Item 1). That is a
   buyer of a commodity-like service choosing on cost and reliability; the rows' failing answer is "most insureds don't
   care from whom they buy" ... "Think airline seats." **[L2004-003]**, against See's, where "it wouldn’t be a question of
   people buying candy for the low bid" **[M2017-009]**.
5. *The brand in the customer's mind.* SkyWest has none with the passenger; the brand is the major's. The rows' warning
   about intermediaries runs the other way here: "the brand is our protection against the intermediaries making all the
   money" **[M2019-041]**, and when the intermediary is trusted "as much as" the product, "the value of having the brand
   moves over to the retailer from the product itself" **[M2001-090]**. In this business the major owns the brand, the
   passenger and the network; SkyWest is the supplier behind it.
6. *The low-cost position, the one exception.* "Another way to prosper in a commodity-type business is to be the
   low-cost operator." **[L2004-007]**; "being the low-cost producer is all-important" **[L2000-017]**. This is the
   counter-case's strongest ground and it was tested. The filer does not claim the lowest cost; it claims parity:
   "Currently, we believe our labor costs are competitive relative to other regional airlines. However, we cannot provide
   assurance that our labor costs going forward will remain competitive" (Item 1A). Parity is the airline row's minimum,
   "if your costs are on parity or less" ... "than your other major competitors" **[M2001-013]**, not an advantage. The
   competitor row below does not show SkyWest earning more than its independent rivals across the span; it shows it
   earning less than old Republic in 2012-2015, less than Mesa in four of the six years 2016-2021, and more than the
   combined Republic only in 2024-2025 (in 2023, 3.5% against 9.5%). And the key input is priced by the customers themselves: pilots
   "may seek employment at major airlines" which "generally offer higher salaries" (Item 1A), so the buyer of SkyWest's
   service is also the bidder for its scarcest cost.
7. *Unit volume.* Aircraft in scheduled service or under contract: 492 at end-2024, 487 at end-2025 (Item 7). Block hours
   rose 14.7% in 2025 from a pilot-constrained 2023-2024. The 50-seat fleet, the old core, is being retired or
   reconfigured at the partners' direction (17 CRJ200s removed in 2025; a 41-seat CRJ450 conversion announced, 10-Q).
8. *Widening or narrowing.* The record of impairments taken when partners changed fleet plans (contrary evidence item 7)
   and the shift of contract risk onto SkyWest (test 2) are the notch, not the widening. Against it, the January 2026
   extensions and the new E175 awards show SkyWest winning the flying that remains.
9. *What could, five to fifteen years out, act on the castle in the row's words*, "that will destroy, or modify, or reduce the economic strengths that we perceive currently exist in a business" **[M2000-014]**: a partner choosing to fly its own
   regional jets or move flying to its owned carrier (permitted, Item 1A); scope limits; a pilot shortage of the 2022-2023
   kind; a partner bankruptcy, in which the agreement "may not be assumed" (Item 1A); a further fleet change that strands
   owned aircraft. All but the partner bankruptcy happened to SkyWest or to a rival inside the span read.

**The competitor row** (operating income / operating revenue, each company's own filings; COMPUTATION, transcription from
the XBRL companyfacts of each filer, checked against the 10-K text where noted; revenue includes different amounts of
pass-through cost in different contracts and years, so the margins are indicative, not like-for-like):

| Year | SkyWest | Old Republic (RJET, old registrant) | Mesa | Republic (combined, post-2016 entity) |
|---|---|---|---|---|
| 2011 | 1.1% | (loss year, net -$151.8M) | n/a | |
| 2012 | 4.7% | 12.2% | n/a | |
| 2013 | 4.6% | 14.2% | n/a | |
| 2014 | 0.8% (3.1% ex $74.8M special items) | 13.5% | n/a | |
| 2015 | 7.6% | 6.3%; Chapter 11 filed 2016-02-25, "As a result of the pilot shortage, the Company has been forced to ground operating aircraft" (10-K FY2015) | n/a | |
| 2016 | -5.6% (9.6% ex $465.6M impairment) | | 9.7% (FY Sept) | |
| 2017 | 12.4% | | 15.6% | |
| 2018 | 14.7% | | 10.7% | |
| 2019 | 17.2% | | 16.7% | |
| 2020 | 5.1% (-11.1% ex $345.5M grant) | | 14.7% | |
| 2021 | 10.2% (-2.3% ex $422.7M grant and $84.6M impairment) | | 12.5% | |
| 2022 | 6.0% | | -34.8% (impairments $171.8M) | |
| 2023 | 3.5% | | going-concern doubt; American wound down and terminated Mesa's CPA on 2023-04-03 (10-K FY2024) | 9.5% |
| 2024 | 14.0% | | merged into Republic 2025 | 9.3% |
| 2025 | 15.2% | | | 10.0% (operating income $168M, 10-K FY2025 of the combined registrant) |

Envoy and Endeavor: their owners (American, Delta) do not report their profits in a segment I could find; not obtained.
What the row says over the whole span: no regional carrier, SkyWest included, shows returns protected from the customer.
SkyWest's margins were below old Republic's in all four years 2012-2015 and below Mesa's in four of the six years 2016-2021; its best years (2017-2019,
2024-2025) followed industry failures or shortages, the "cyclical peak in earnings" **[L1994-009]**, which the rows tell the reader to rule out before crediting a high return. "you can have only two competitors and they’re still terrible
businesses, they beat each other’s brains out" **[M2013-052]**; the same row calls airlines "a labor-intensive,
capital-intensive, largely commodity-type business".

**The counter-case, stated as strongly as I can**, since "you want to be able to state their case better than they can" **[M2016-055]**. SkyWest is the largest independent regional, has
flown since 1972, and its partners keep renewing and adding aircraft; the capacity purchase agreements put fuel, fare
and load-factor risk on the major and pay SkyWest's aircraft ownership cost; the aircraft are financed with fixed-rate
debt and the rates "reflect the interest rates effective at the closing" (Item 7A); rivals failed (Republic 2016, Mesa
2023-2025) while SkyWest consolidated share; a major that needs 50-to-76-seat flying under scope has few suppliers left;
and SkyWest's 2025 operating margin is about half again the combined Republic's. If SkyWest is the low-cost,
best-run operator in a commodity field, L2004-007 says it can prosper.

**Why the counter-case does not carry the castle.** Every element of it is a description of a good supplier, not of a
castle. The customer can fly in-house or move flying to its own carrier and "are not prohibited from doing so" (Item
1A); the filer says the rates it is offered are affected by what rivals accept; the customer has reshaped the terms in
its own favor (fixed to variable pay; termination for uncompetitive cost; rate resets; shortened terms); and the record
over fifteen years is one of near-zero or negative years whenever the customer or the pilot market moved (2011, 2014,
2016, 2020, 2021 without the grant, 2023), with the good years following rivals' failure. The low-cost claim is a claim
of parity in the filer's own words. The speakers' own airline cases point the same way: the carrier whose costs could be
undercut, "you do not want to have something whose competitive position is going to erode over time" **[M2007-117]**;
"In an unregulated commodity business, a company must lower its costs to competitive levels or face extinction."
**[L1994-035]**; and "growth has been a curse in the airline business because more and more capital has been put into the
business at inadequate returns" **[M2001-019]**. An attacker cannot take the majors' brands from SkyWest because SkyWest
does not own them; and it need not build a rival from nothing, because the customers already own the alternative. The
rows' See's question, "could I do it?" ... "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**,
is answered yes by the customers' own subsidiaries.

**OUT or TOO HARD?** The routing: a castle shown on the evidence to be filling in, or never built, closes OUT; a castle
whose future cannot be judged closes TOO HARD. The facts above are single facts in the filer's own words (permitted
in-sourcing; rates affected by rivals' bids; terms shifted against SkyWest; repeated partner-driven impairments), not a
forecast that insiders would refuse to write down. The evidence shows the castle open, so the box is OUT, not TOO HARD
(NATURE), and not TOO HARD (WORK): no single further fact found in a filing would supply SkyWest a moat its customers do
not grant it; the deciding facts were "things that are important and knowable" **[M2006-076]**, and they are known.

**VERDICT: OUT** **[M2011-015]**, **[M2013-054]**, **[M2012-109]**, **[L2004-003]**, **[M2006-013]**. The file closes
here; Q3 to Q12 are NOT REACHED. Price does not reopen it: "What you can’t do is turn any investment into a good deal by
paying little" **[M2019-015]**.

---
## Q4 balance-sheet reading, done in Step 0 because the file closed before Q4 (COMPUTATION — NOT A CLEARANCE)
"balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**. USD millions,
year-end, from the 10-Ks listed (XBRL table of `tools/run.py`, checked against the filed statements at 2024 and 2025):

| Year-end | Assets | PP&E net | Equity | Retained earnings | Debt (current + long-term) | Cash + securities | Deferred tax liability (gross) | Deferred revenue |
|---|---|---|---|---|---|---|---|---|
| 2016 | 5,137 | 3,822 | 1,351 | 1,104 | 2,546 | n/r | 1,022 | none |
| 2017 | 5,458 | 4,183 | 1,754 | 1,517 | 2,687 | 686 | 667 | none |
| 2018 | 6,313 | 5,006 | 1,964 | 1,777 | 3,160 | 689 | 956 | none |
| 2019 | 6,657 | 5,395 | 2,175 | 2,079 | 2,993 | 520 | 1,033 | none |
| 2020 | 6,888 | 5,362 | 2,140 | 2,052 | 3,204 | 826 | 1,019 | 111 |
| 2021 | 7,126 | 5,499 | 2,268 | 2,164 | 3,109 | 860 | 997 | 104 |
| 2022 | 7,415 | 5,549 | 2,348 | 2,237 | 3,380 | 1,047 | 1,130 | 145 |
| 2023 | 7,026 | 5,483 | 2,114 | 2,271 | 3,006 | 835 | 1,129 | 375 |
| 2024 | 7,140 | 5,587 | 2,409 | 2,594 | 2,672 | 802 | 1,153 | 338 |
| 2025 | 7,386 | 5,843 | 2,746 | 3,023 | 2,392 | 707 | 1,253 | 292 |

(n/r = not read for that year. Cash + securities 2017-2024 = cash from the run.py table plus the XBRL
available-for-sale securities line; 2025 from the filed balance sheet. 2026-06-30: assets $7,412M, debt $2,296M, equity
$2,761M, cash and securities $601M, 10-Q and Ex. 99.1.)

What the balance sheets say. (1) The business is its aircraft: PP&E is 79% of assets in 2025, financed roughly half by
secured debt; the debt peaked at $3,380M in 2022 and has been paid down by $988M since, from operating cash while capex
was deferred by the pilot shortage. (2) Retained earnings rose $1,919M over nine years; treasury stock at cost stood at $1,075M at
end-2025, and much of the rest is tied up in aircraft that must be replaced: the cash residual table at Step 0
is the better guide. (3) The deferred tax liability grew to $1,253M; cash taxes paid were $1.2M to $18.6M a year in
2021-2025 against provisions up to $137M, because aircraft are depreciated fast for tax. The rows do not let that be
read as free capital: "I don’t think I would look at that as a hidden form of equity" **[M2015-030]**. (4) Deferred
revenue appeared in 2020 and peaked at $375M in 2023: fixed payments received while the company could not fly the
schedules, now being earned off ($264.6M net still to recognize at end-2025, Item 1A). It flattered 2023 operating cash
by $242.5M. (5) Receivables are small ($160M against $4,058M revenue) and inventories are spare parts: nothing builds
against sales. (6) Intangibles went from $8M to nil with the ExpressJet sale. Nothing on these balance sheets is
confusing or suspect; what they show is a capital-heavy supplier whose equity grew slowly and whose free cash went back
into aircraft and buybacks.

## Q3: NOT REACHED (computation noted)
For the record, not a clearance: pre-tax income excluding grants, impairments and the ExpressJet gain averaged $193.5M a
year over 2016-2025 (sum $1,934.7M), about 4.4% on roughly $4.4B of capital employed (equity plus debt less cash and
securities). The committed E175s replace CRJs one for one where the filing says so (11 CRJ700s for American, 16 CRJs for
Delta, 10-Q): about $33M of new aircraft (the $2.28B commitment over 69 aircraft, spare engines included) to keep each
existing position, the shape of "spend more than its depreciation charge to simply maintain its present level of
business" **[L2023-009]**.

## Q4: NOT REACHED (the balance-sheet reading above was done as Step 0)
## Q5: NOT REACHED (contrary evidence item 9 recorded for a future reader)
## Q6: NOT REACHED (buyback prices recorded under the computation below)
## Q7: NOT REACHED
## Q8: NOT REACHED
## Q9: NOT REACHED
## Q10: NOT REACHED
## Q12 (optional): NOT ASKED

---
## COMPUTATION — NOT A CLEARANCE: value range, fair price, cheap price (reported at the owner's request)
Built on the framework's Q7 CONVENTION (five-year average of owner cash after every real cost; the growth shown, capped
by Q3's arithmetic; ten years then zero nominal growth; discounted at the sovereign, 5.66%), the inputs from the Step 0
table, and the arithmetic in `Test Runs/_research 2026-10-05 SKYW/value.py`. The rows behind the construction: "What is
the risk-free interest rate (which we consider to be the yield on long-term U.S. bonds)?" **[L2000-021]**; "use the
government bond rate" **[M1996-025]**; "depreciation is an economic cost every bit as real as wages, materials, or taxes"
**[R1996-023]**, "almost always true costs" **[L2015-004]**; and "it will pay you to be suspicious as to why the beginning
and terminal years have been selected" **[L2005-003]**. None of it is a clearance: the file closed OUT at Q2.

**The maintenance judgment**, since "the shareholders are entitled to my best guess" **[M2000-144]** of the
"expenditures that a company must make to maintain its competitive position" **[L1999-024]**. The filing allows one: the committed E175 deliveries are
stated as replacements for named CRJs (27 of them, 10-Q), the fleet in service was flat (492 to 487 in 2025), and the
CRJ700/CRJ550 and CRJ200 fleets average 20.3 and 22.8 years of age (Item 2). Aircraft capex is therefore mostly the cost of staying in
place, and depreciation understates it (the CRJ700 lives were lengthened in Q4 2024). The capex basis is the central
figure; the D&A basis is shown beside it as the generous bound. Firm aircraft and spare-engine commitments are $278M to
$336M a year for 2026-2030 (Item 7), before rotables, buildings and the 19 Delta-owned CRJ900s to be returned.

**Growth shown.** Owner cash itself has negative years and cannot carry a growth rate. Revenue is used (CONVENTION of
this run, rationale: the only aggregate series without sign changes over the window): 10.59% a year 2021-2025, a recovery
from the COVID and pilot-shortage base years that L2005-003 warns about, capped at 5.60% so that it does not run past the
discount rate; 3.17% a year over 2016-2025.

| Case | Owner cash ($M/yr) | No growth ($/share) | Shown growth ($/share) | Width |
|---|---|---|---|---|
| **Convention: five-year 2021-25, capex basis** | 124.1 | **56.47** | **88.01** (5.60%, capped) | 1.56 : 1 |
| Five-year, D&A basis (shown beside) | 214.5 | 97.60 | 152.12 | 1.56 : 1 |
| **Whole cycle 2016-25, capex basis** | -39.2 | no positive value | no positive value | undefined |
| Whole cycle 2016-25, D&A basis | 216.0 | 98.29 | 126.37 (3.17%) | 1.29 : 1 |
| Best recent three years 2023-25, capex basis (sensitivity only, not the convention) | 310.5 | 141.29 | 220.20 | 1.56 : 1 |

The five-year window holds abnormal years (2021: COVID and $422.7M of grants, removed; 2022-2023: the captain shortage),
so the whole-cycle variant is the one the owner asked for. Across the windows and bases the value runs from nothing to
about $220 a share, far wider than three to one: had Q7 been reached, that width alone would have argued TOO HARD under
the convention: "the range must be so wide that no useful conclusion can be reached" **[L2000-025]**. On the convention's own case the price, $96.06, sits **above the top** of the range
($56.47 to $88.01); the expected return at the price is below the floor, which the convention closes OUT:
"there’s just a point at which we drop out of the game" **[M2003-149]**.

**FAIR PRICE: $42.23.** The price at which the central case returns about 10% pre-tax: five-year capex-basis owner cash
grossed up for the cash taxes actually paid (+$11.4M a year, to $135.5M pre-tax), carried at half the capped shown growth
(2.80%) for ten years, then zero, discounted at 10%. *Tax treatment:* owner cash is after cash taxes; cash taxes are small
because accelerated tax depreciation defers them (deferred tax expense averaged $57.0M a year in 2021-2025 and is not
deducted), so adding back the cash taxes approximates a pre-tax figure while still omitting a real deferred liability, "not free equity
to us" **[M2015-030]**; the fair price is generous on that account. D&A-basis variant: $70.41.

**CHEAP PRICE: $23.26.** Rule (CONVENTION of this run): the price at which the convention's no-growth pre-tax owner cash
yields 15%, half again the floor, so that no pencil is needed: otherwise "it’s too close to think about" **[M1996-084]**; "It should scream at
you." **[M2009-005]**. D&A-basis variant:
$38.78. The price is about four times the cheap price and more than twice the fair price.

**Buyback prices, for Q6 if ever reached.** Q4 2025: 268,262 shares at an average $100.43 (10-K FY2025, Item 5). Q2 2026:
833,000 shares at $89.55 (Ex. 99.1). Both above the top of the convention range. The program names no price ("at
prevailing market prices", 8-K of 2026-07-23). In 2023, 10.6M shares were bought for $291.9M, about $27.57 a share
(statement of stockholders' equity, 10-K FY2025), near the cheap price above.

---
## THE BOX
**OUT at Q2.** The castle is shown open on the filer's own facts: four customers who set schedules, aircraft and
(through competing bids and renewals) rates, who own rival regional carriers and are "not prohibited" from using them,
and who have shifted contract risk onto SkyWest; a fifteen-year record of near-zero or loss years whenever the customer
or the pilot market moved, and partner-driven impairments of more than $690M. Computation only: convention range $56.47
to $88.01 a share (whole-cycle capex basis: no positive value), fair price $42.23, cheap price $23.26, against $96.06.
No research file is opened (not a TOO HARD).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. Written in one pass after the reading, not question by question with
      commits: the dispatch forbade commits, so write-early by commit was not possible; the file was created first.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, below); every filing fact carries its
      accession or names its filing; every number has a filing or a CONVENTION label.
- [x] The order was kept; Q2 closed the run; everything after it is labelled COMPUTATION or NOT REACHED.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy (operator rule 5);
      the tool's wrong capex line found and rejected; the sovereign from the US Treasury; the price flagged as an
      aggregator quote.
- [x] Contrary evidence written down as it was found, "write it down in the first 30 minutes" **[M1997-127]** (eleven
      items, before the verdict).
- [x] Not a point-in-time run; no row after an anchor in question.
- [x] Only the arithmetic lines of `tools/run.py` were used, and one of them was rejected.
- [x] `python tools/check_framework.py` run before handing back (result recorded in the reply); no commit made, per the
      dispatch.
- [ ] Not done: Envoy and Endeavor economics (no segment disclosure found); a like-for-like cost per block hour across
      regionals (not disclosed on a common basis); a reading of the capacity purchase agreements themselves (filed as
      exhibits with confidential terms redacted; not opened).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **The Q7 growth input assumes owner cash has a growth rate.** For a capital-heavy business whose owner
cash after all capex swings from -$562M to +$430M, "the growth the business has actually shown" on aggregate owner cash
is undefined; this run used revenue growth and confessed it as its own CONVENTION. The framework should say what to use
when owner cash changes sign. (2) **The window rule and the whole-cycle variant can disagree by more than the range
itself.** The convention's five-year range is 1.56 to 1, comfortably narrow, while the same arithmetic across windows and
bases spans nothing to $220; the three-to-one width test is applied within one case, and nothing says whether the spread
between cases counts. (3) **`tools/run.py`'s capex tag is unsafe for any filer that reports its main capital spending on a
separate line.** Here it omitted the aircraft entirely and overstated owner cash about sevenfold; Part VII tells a run to
use the tool's arithmetic lines, and this one was arithmetic and wrong. Every run should check the tool's capex against
the filed investing section. (4) **Q2's routing between OUT and TOO HARD for a supplier to a few powerful customers is not
stated.** The castle tests are written for a business that sells to many customers; for a contract supplier the customer
is also the competitor (three of SkyWest's four customers own rival carriers). I read the customer's freedom to in-source
and the filer's admission that rivals' bids set its terms as the castle shown open (OUT), not as a future that cannot be
judged (TOO HARD); a second analyst could route it TOO HARD (NATURE) on the ground that renewal rates in 2030 are
unknowable. A sentence on customer-owned competition would settle it.
