# Company Run — FreightCar America, Inc. (Nasdaq: RAIL) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

Dispatched blind run, written by an unattended analyst under `Screens/_daily/_dispatch_brief.md` as relayed in the
dispatcher's brief of 2026-10-16. Working folder: `Test Runs/_research 2026-10-16 RAIL/` (notes, scripts, the run.py
output, the field table; raw filings under its gitignored `cache/`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.  *Filled at the fold by the dispatching session, 2026-10-16, after the run was committed: `PORTFOLIO.md` read for this ticker only (RAIL, FreightCar); not held.*

**Contamination, declared and not used.** Before any reading for this run, the session context carried: the subjects of the
five most recent commits (all about another company's run and fold, LZRFY); the working-tree status, which lists untracked
files in other companies' research folders by name (AYI, ARCB) and coursework paths; and a one-line memory index that
describes the state of the queue in general terms (counts of runs and gate-clearers, no ticker of this company). The
`.gitignore` was read for its research-folder patterns only. None of it names this company, and none of it was used. No
other `Test Runs/` file, holding review, `PORTFOLIO.md`, register, reading list or resume-state file was opened, listed or
searched; the only directory listing of `Test Runs/` made was a filename match for "RAIL" or "freight", before the copy,
to check that no file of this name existed (it returned nothing).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $5.92 (close 2026-10-16; Yahoo Finance chart endpoint, read by `tools/run.py` and re-read directly; an
  aggregator, flagged per operator rule 5, live quote only). The weekly closes on the same feed ran $9.17 (2026-04-13),
  $10.20 (week of 2026-06-22), $7.94 (2026-08-03), $6.25 (2026-10-05).
- **Shares by class** from the latest filing's cover: 32,791,280 common shares, a single class, as of 2026-07-31 (10-Q for
  the quarter ended 2026-06-30, filed 2026-08-03, accession `0001193125-26-330623`; `python Screens/cover_shares.py RAIL`).
  Check: the 10-Q balance sheet states 32,775,760 shares issued and outstanding at 2026-06-30 (issued equals outstanding;
  no treasury shares shown); the 8-K of 2026-07-02 (`0001193125-26-294701`) states that the 2026-06-26 net exercise by
  OC III LFE II, LP issued 13,619,377 shares, leaving 32,775,760 outstanding at 2026-06-30. The 8-Ks filed after the 10-Q
  (2026-08-05, `0001213900-26-085699`, a rights agreement; 2026-10-15, `0001213900-26-109859`, the Stockholder Agreement
  and the rights agreement's termination) issue no shares. Still outstanding at 2026-06-30 (10-Q, Warrants note): three
  replacement penny warrants of 4,132 shares each (exercise price $0.01) and the 2023 Warrant for 1,636,313 shares at
  $3.57; at $5.92 the treasury-stock count of the 2023 Warrant is about 0.65 million shares (arithmetic, stated).
- **Market cap:** 32.791M x $5.92 = **$194.1M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-15 (issuing authority; fetched by `tools/sources.py` through `tools/run.py`).
- **Filings read** (operator rule 4): the FY2025 10-K (filed 2026-03-09, `0001193125-26-098668`), Items 1, 1C, 7 and 8
  (a smaller reporting company; the filing carries no Item 1A risk factors, and none was found by a search for "Risk
  Factors" and "Item 1A"); the 10-Q for 2026-06-30 (`0001193125-26-330623`); the proxy (DEF 14A filed 2026-03-19,
  `0001213900-26-031465`); the 8-Ks of 2026-07-02, 2026-08-05 and 2026-10-15; for the last cycle the 10-Ks for FY2024
  (`0000950170-25-037977`), FY2023 (`0000950170-24-032849`), FY2022 (`0000950170-23-010051`) and FY2021
  (`0000950170-22-004254`), and the XBRL company facts for FY2009 to FY2025 (each year's figure carries the accession of
  the 10-K that first filed it; see `field_out.txt` in the working folder).
  **One figure cross-checked against the filed statement:** FY2025 revenues $500,991 thousand on the filed Consolidated
  Statement of Operations (`0001193125-26-098668`) against $501.0M in the XBRL facts and in `tools/run.py`; cash, cash
  equivalents and restricted cash $64,295 thousand on the filed balance sheet against 64,295 in the run.py table. Both agree.
- `python tools/run.py RAIL`, arithmetic lines only (its v4 material ignored, Part VII): operating cash less stock pay less
  capital spending (USD millions) FY2023 -9.2, FY2024 36.8, FY2025 27.8; five-year window FY2021 to FY2025 mean -0.7 on
  the capex basis, 0.5 on the depreciation basis; capital spending FY2023 12.7, FY2024 5.0, FY2025 3.4 against
  depreciation and amortization 4.6, 5.8, 6.2; stock pay 1.2, 3.1, 3.6, resolved from the ShareBasedCompensation tag each
  year. Alternates it prints and does not choose: finance-lease principal 1.0, 2.1, 1.1 (FY2023 to FY2025). The full
  owner-cash recast is under Q4 in AFTER THE STOP and in the COMPUTATION under Q7.

**The balance sheets, read in Step 0 because the file closes before Q4** **[M2025-032]** ("I like to look at balance
sheets over an 8 or 10 year period before I even look at the income account"). From the run.py ten-year table
(first-filed XBRL) checked against the filed balance sheets of FY2023 and FY2025 and the 10-Q of 2026-06-30, USD millions:

| year-end | total assets | cash | inventory | debt on the face | warrant liability | mezzanine preferred | stockholders' equity | retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2016 | 339.3 | 92.8 | 97.9 | 0 | none | none | 256.9 | 187.5 |
| 2017 | 295.9 | 87.8 | 45.3 | 0 | none | none | 231.7 | 161.4 |
| 2018 | 289.7 | 45.1 | 64.6 | 0 | none | none | 193.6 | 120.8 |
| 2019 | 245.2 | 66.3 | 25.1 | 10.2 | none | none | 117.2 | 45.8 |
| 2020 | 182.7 | 54.0 | 38.8 | 55.3 | not read | none | 30.5 | -38.6 |
| 2021 | 200.7 | 26.2 | 56.0 | 79.5 | not read | none | -1.7 | -80.1 |
| 2022 | 199.7 | 37.9 | 64.3 | 92.2 | 31.0 | none | -28.6 | -118.9 |
| 2023 | 259.5 | 40.6 | 125.0 | 29.4 | 36.8 | 83.5 | -46.2 | -142.8 |
| 2024 | 224.2 | 44.5 | 75.3 | 108.4 | 136.3 | none | -150.3 | -220.6 |
| 2025 | 290.0 | 64.3 | 68.3 | 107.2 | 168.5 | none | -107.4 | -182.5 |
| 2026-06-30 | 276.1 | 63.0 | 57.8 | 100.7 | 14.0 | none | 36.2 | -171.0 |

What the figures say: retained earnings fell from +$187.5M at the end of 2016 to -$220.6M at the end of 2024, about
$408M of cumulative deficit in eight years; equity went negative in 2021 and stayed negative until the warrant holder's
June 2026 net exercise derecognized the exercised warrants (paid-in capital rose from $72.6M to $204.5M and the
warrant liability fell from $168.5M to $14.0M; 10-Q). Goodwill of $21.5M (2016 to 2018)
is gone by 2019. Cash fell from $92.8M (2016) to a low of $26.2M (2021) and is $63.0M at mid-2026. Debt appeared in 2019
and has been between $79M and $108M since 2021, except at the end of 2023, when a term loan had been exchanged for $85.4M of
Series C preferred (mezzanine, liquidation value $95.0M, FY2023 10-K), itself redeemed in 2024 with a $115.0M Blue Torch term
loan at Term SOFR (3% floor) plus 6% (FY2025 10-K, Liquidity). Inventory moves with the delivery schedule (125.0 at the end
of 2023 against 75.3 a year later). The deferred tax asset of $53.0M at the end of 2025 is new, the release of a
valuation allowance in 2025 (FY2025 10-K, Income Taxes). What they cannot say: whether the two profitable years after the
move to Mexico are the business or the top of a cycle; the income account and the rivals answer that, at Q2.

## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own this if "the market closed for five years" **[M1997-109]**; the
question then is what a railcar builder that sells mostly to lessors will earn across a cycle, not where the quotation goes.
No macro forecast enters: the railcar cycle is read only from the filed record of deliveries and margins, and the
steel and aluminum prices only as the filer passes them through. The analyst's habits bear most: the evidence against is
sought first and written down as found, "write it down in the first 30 minutes" **[M1997-127]**, and scuttlebutt is
used "to possibly reject your original hypothesis" **[M1998-144]**; here the rivals' filings are that test.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the FY2025 10-K names price first among the bases of
competition ("In addition to price, competition is based on delivery timing, product performance and technological
innovation, reputation for product quality and customer service"); (2) 78% of 2025 sales went to financial institutions,
and the top five customers took about 75% of revenue (FY2025 10-K, Item 1); (3) cumulative operating losses of about
$160M over FY2016 to FY2025 (XBRL, field table); (4) the 10-Q for 2026-06-30 shows second-quarter manufacturing gross margin
of 3.2% against 13.4% a year earlier, and an operating loss for the half year; (5) the warrant holder group owns about 48.8%
and the board adopted, then terminated under a stockholder agreement, a rights plan in 2026 (8-Ks of 2026-08-05 and
2026-10-15). Evidence for, also written down: (6) operating income of $37.3M (2024) and $33.9M (2025) after six years of
operating losses (FY2017 to FY2022) and a small profit in FY2023; (7) backlog rose from 1,926 cars ($137M) at the end of 2025 to 3,972 cars ($344M) at
2026-06-30 (10-Q).

## THE STANDING RULE
The buyer's own conduct: a part-interest bought for cash, without borrowed money, in a size the buyer can hold through a
fall of half or more, risks nothing the buyer has and needs; "never going to risk what we have and need for what we
don’t have and don’t need" **[M2012-081]**, and "borrowed money has no place in the investor's tool kit" **[L2014-005]**.
The rule does not bar the name; the target's own debt (a 9.7% term loan maturing 2028, covenants on liquidity and
leverage) is Q9's, not the standing rule's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The lines of evidence chosen, and why** (derived from the FY2025 10-K, Items 1 and 7; the filing has no Item 1A):
Item 1 says what is sold (freight cars of many types, rebuilds and conversions, parts), from where (one leased plant in
Castaños, Coahuila, Mexico; 1,916 of 1,986 employees in Mexico), to whom (financial institutions 78%, shippers 16%; top
five customers about 75% of 2025 revenue) and on what terms (competition on price, delivery, performance, quality and
service; a sole supplier of roll-formed center sills used in 66% of new cars). Item 7 says what drives the figures
(deliveries, product mix, raw material prices passed through, the backlog, interest on a term loan, a warrant liability
marked to the stock price). So the evidence this name needs is: (a) the delivery and margin record over a full railcar
cycle, the filer's own; (b) the same record for the rivals, from their filings (Q2); (c) the cost position against those
rivals, since the product is bought by lessors largely on price (Q2); (d) the balance sheet and the warrant and preferred
history (Step 0, Q4, Q6); (e) the tariff and trade exposure of a Mexican plant selling into the United States, which the
10-K names in Item 7 (Q2, test 11; Q9).

**The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will
look like in five or 10 years" **[M2012-065]**. The product is a steel or aluminum box on trucks, built to AAR standards,
whose designs change slowly (the BethGon coal car since the late 1970s, aluminum since 1986; Item 1); the chemistry of
it does not matter, "What is important is that I understand the economic dynamics of the industry." **[M2011-014]**. The key
variables, found by "trying to identify the key variables in that particular business" **[M1998-044]**, are three
and each is readable: the North American delivery cycle (cyclical, its timing not
foreseeable, its existence and amplitude on the filed record of every builder: Trinity's rail products revenue fell 41.6% in
2025, RAIL's deliveries ran from 751 cars in 2020 to 4,362 in 2024); the cost position against the two large builders, which
also build in Mexico; and the price the lessors will pay. The steel and aluminum prices are not forecast, "We don’t
think we can predict commodity prices." **[M2016-025]**, and need not be, since the 10-K says aluminum and steel prices are generally not fixed when an
order is accepted and some customer contracts provide for variable pricing on raw-material costs (Item 1, Backlog note). The financial statements do tell
"the information that’s useful to me" **[M2008-033]** about the future ones once read across a whole cycle: this is a
business whose average can be read from its figures, "if you can’t make a decision on something like PetroChina off the
figures, forget about going further" **[M2008-069]**. The industry insiders would write a ten-year range down; nothing here
is the fast-moving technology the insiders "would not want to put down on paper" **[M2000-105]**. Test 6 (can I name the
winner?) belongs to Q2 and is answered there from the rivals' filings.

**What I could misjudge.** Whether the 2024 and 2025 results describe the new Mexican business or the top of a cycle; a
question of the castle and of the cycle, which Q2 owns, and not of whether the economics can be understood.

- **VERDICT: IN.** The economics of a cyclical railcar assembler selling largely to lessors can be foreseen as a range from
  its own and its rivals' filed record **[M2012-065]**, **[M2011-014]**, **[M2008-069]**; the commodity inputs are not a STOP
  at Q1 (Q2's commodity-business paragraph, **[M2016-025]**). Filing fact: FY2025 10-K (`0001193125-26-098668`), Item 1
  and Item 7.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question is put from the attacker's side: "why is that castle still standing?" **[M1995-038]**, where a moat is what
"protects excellent returns on invested capital" **[L2007-004]**.

**The rivals.** The FY2025 10-K names no competitor (Item 1, Competition, speaks of "established competitors in the railcar
industry in North America"; there is no Item 1A); the FY2023 and FY2024 10-Ks name none either (searched for Trinity,
Greenbrier, National Steel Car). The FY2022 10-K (`0000950170-23-010051`) names three: "Trinity Industries, Inc., The
Greenbrier Companies, Inc. and National Steel Car Limited". **CONVENTION of this run:** the rivals are the three the filer
last named, since the latest 10-K names none and the brief asks for the 10-K's own names first; rationale: the filer's own
latest list is better evidence of whom it competes with than a list I would choose. National Steel Car is private and files
nothing with the SEC (flagged). Trinity (CIK 99780) and Greenbrier (CIK 923120) are read from their own 10-Ks.

**The parts table** (the filer's segments; FY2021 to FY2023 reported Manufacturing and "Corporate and Other", FY2024 on
Manufacturing and Aftermarket; segment operating income, USD millions, from the FY2021, FY2023, FY2024 and FY2025 10-Ks):

| part | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | five-year sum | share of segment profit | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| Manufacturing (new cars, conversions, rebodies) | -0.8 | 14.8 | 31.6 | 59.6 | 62.2 | 167.4 | about 90% (Aftermarket is reported for three years only) | judged below | **yes, more than half** |
| Aftermarket (parts, services) | inside Corporate and Other | inside Corporate and Other | 3.9 | 7.2 | 7.2 | 18.3 (three years) | about 10% | not judged | no |

The file closes on Manufacturing, since "lumping them together, as is done in standard financial statements, impedes
analysis" **[L2008-005]**; the Aftermarket part, which does not decide, would be carried as ordinary at no growth at Q7.

**The castle tests, each with its filing fact.**
1. *What keeps it standing*: "What are the key factors? And how permanent are they?" **[M1995-038]**. Item 1 offers long customer relationships, engineering, new
   designs ("nearly 50 new or redesigned products" in seven years), patents (the automatic door hopper) and "competitive
   pricing". None is a reason the lessor must buy from this builder; the 10-K says many customers do not buy every year
   and "The size and frequency of railcar orders often results in a small number of customers representing a significant
   portion of our sales in a given year" (top three customers 26%, 20% and 13% of 2025 revenue against 13%, 9% and 9% in 2024).
2. *Would it stand without the lord.* Not the question here; there is no castle for a lord to hold.
3. *The money test*: "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?"
   **[M2011-015]**. The filer answered it for its own industry: it built its present capacity in 2019 and 2020 through a joint
   venture with Fasemex in Castaños, began production in the third quarter of 2020, bought the partner's half "in exchange for
   $0.2 million in cash and 2,257,234 shares of the Company's common stock", and moved all production there by March 2021
   (FY2021 10-K, `0000950170-22-004254`, Item 7). Its property, plant and equipment is $28.4M at 2026-06-30, the plant itself
   leased (10-Q). Capacity in this field is created cheaply and quickly; "If the answer had been yes, we wouldn’t have done
   it." **[M2011-015]**. And "one competitor is frequently enough to ruin a business" **[M2012-108]**: the two large rivals
   also build in Mexico.
4. *Pricing power.* No price rise is described in the five RAIL 10-Ks read; margin moves are put down to "product mix" (2025
   up, the second quarter of 2026 down) and to deliveries, and some contracts pass raw-material costs through. Nothing
   shows a business able to raise its price without the agony by which "you can almost measure the strength of a business
   over time" **[M2005-020]**.
5. *Unit volume and share of mind.* Deliveries: 751 cars (2020), 1,731 (2021), 4,362 (2024), 4,125 (2025) (FY2021 and FY2025
   10-Ks); Greenbrier delivered 20,400 in fiscal 2025 (its 10-K, `0001193125-25-253612`). Volume follows orders won on a bid,
   not a name the buyer asks for.
6. *The low-cost position*, the route through a commodity field: "when a company is selling a product with commodity-like
   economic characteristics, being the low-cost producer is all-important" **[L2000-017]**. It is measured against the rival
   **[M2001-013]**, by "cost of production" **[M2006-004]**, and "The figures are available." **[M2009-059]**: see the
   competitor row. RAIL's gross margin was below Greenbrier's manufacturing gross margin in six of the ten years FY2016 to
   FY2025, level within a point in three, and ahead in one (2023); on the manufacturing segments alone it was 10.8% against
   12.1% in 2024 and 13.5% against 14.5% in 2025. No filing read shows a cost advantage; parity at best in the latest years.
7. *The brand.* BethGon and AutoFlood are design names known to coal shippers; the buyers are 78% financial institutions
   (FY2025 10-K, Item 1), lessors who place cars with shippers. No instance found in the filings read of a customer asking
   for the car by name or paying more for it.
8. *Would the customer choose it over the low bid.* The question asked of See's was whether it "wouldn’t be a question of
   people buying candy for the low bid" **[M2017-009]**. The 10-K lists price first: "In addition to price, competition is
   based on delivery timing, product performance and technological innovation, reputation for product quality and customer
   service." The lessor stands where the insurance buyer does: "most insureds don't care from whom they buy" **[L2004-003]**.
9. *Ask the competitors.* No interview; their filings stand in. Trinity's 10-K for 2025 puts its rail-products margin fall down
   to "lower deliveries, reduced overhead absorption due to lower production volumes", the same mechanism as RAIL's.
10. *Widening or narrowing*: "whether it’s likely to widen further or shrink on you" **[M1999-108]**. The move to Mexico
   (2020 to 2021) took RAIL from a high-cost US builder to rough parity; nothing in the filings shows it widening past the
   rivals, and the first half of 2026 shows a consolidated gross margin of 9.6% (15.0% in the first half of 2025) and a
   manufacturing gross margin of 3.2% in the second quarter (13.4% a year earlier) (10-Q, `0001193125-26-330623`).
11. *What could "destroy, or modify, or reduce the economic strengths"* **[M2000-014]**: the 10-K's own list in Item 7 and its
   forward-looking statements (tariffs and trade barriers including those on Mexico, the cycle, a few customers, the sole
   center-sill supplier). One plant, in one country, across one border from its customers.

**The competitor row** (the same metric from each filer's own filings; each figure from the 10-K that first filed it; the
working file is `field_out.txt`; the segment figures from the 10-Ks named below the tables).

*(i) The field's returns over the last full cycle: consolidated operating income on total assets less cash, pre-tax.*

| fiscal year | RAIL | Trinity (TRN) | Greenbrier (GBX, year to August) |
|---|---|---|---|
| 2016 | 6.4% | 8.7% | 25.3% |
| 2017 | -15.3% | 6.3% | 14.6% |
| 2018 | -13.1% | 4.0% | 13.1% |
| 2019 | -42.2% | 4.9% | 6.9% |
| 2020 | -62.6% | -1.5% | 7.2% |
| 2021 | -13.0% | 3.2% | 1.5% |
| 2022 | -9.3% | 3.9% | 3.6% |
| 2023 | 4.8% | 4.7% | 4.8% |
| 2024 | 20.8% | 5.7% | 8.3% |
| 2025 | 15.0% | 7.9% | 8.9% |
| mean FY2016 to FY2025 | **-10.9%** | **4.8%** | **9.4%** |

Accessions: RAIL `0001193125-17-069639` (FY2016) through `0001193125-26-098668` (FY2025); TRN `0000099780-17-000014` through
`0000099780-26-000014`; GBX `0001193125-16-746547` through `0001193125-25-253612`; each year's accession is in `field_out.txt`.
Caveats, stated: Trinity's and Greenbrier's figures include their leasing arms (Trinity's 2016 and 2017, as first filed, also the
businesses spun off as Arcosa in 2018, and its 2025 a $194.2M divestiture gain); RAIL's 2025 assets include a $53.0M deferred
tax asset first recognized that year (without it, 2025 is about 19.6%). The cycle: the filer called 2020 "the cyclical industry
downturn" (FY2021 10-K); RAIL's deliveries peaked in 2015 and 2024 within the decade, so FY2016 to FY2025 runs from the year
after one peak to the year after the next.

*(ii) The cost position: manufacturing margins.*

| fiscal year | RAIL gross margin (consolidated; the Manufacturing segment alone where reported) | Greenbrier Manufacturing gross margin | Trinity Rail Products operating margin (its own metric; no segment gross margin is filed) |
|---|---|---|---|
| 2016 | 7.7% | 22.2% | 14.9% |
| 2017 | 0.8% | 20.4% | 10.4% |
| 2018 | -1.1% | 15.5% | 7.3% |
| 2019 | -6.2% | 12.1% | 9.6% |
| 2020 | -12.5% | 12.1% | 2.3% |
| 2021 | 5.6% | 9.3% | 0.4% |
| 2022 | 7.1% | 7.1% | 2.8% |
| 2023 | 11.7% | 8.2% | 4.8% |
| 2024 | 12.0% (Manufacturing 10.8%) | 12.1% | 7.8% |
| 2025 | 14.6% (Manufacturing 13.5%) | 14.5% | 5.2% |
| mean | **4.0%** | **13.4%** | **6.6%** |

Sources: RAIL GrossProfit over Revenues (XBRL) and the FY2024 and FY2025 10-K MD&A for the segments; Greenbrier 10-Ks FY2018
(`0001193125-18-309099`), FY2020 (`0001564590-20-048326`), FY2022 (`0000950170-22-020502`), FY2023 (`0000950170-23-055208`) and
FY2025 (`0001193125-25-253612`), each year's Manufacturing "Margin (%)" as first stated (FY2024 as recast in the FY2025 10-K
after maintenance services were folded into Manufacturing); Trinity 10-Ks FY2017 (`0000099780-18-000027`), FY2019
(`0000099780-20-000025`), FY2021 (`0000099780-22-000013`), FY2023 (`0000099780-24-000017`) and FY2025 (`0000099780-26-000014`),
the Rail Group or Rail Products Group "Operating profit margin" as first stated. RAIL's segment operating margins before its
corporate cost were 11.0% (2024) and 13.1% (2025), above Trinity's 7.8% and 5.2% in the same years; RAIL's corporate cost was
5.3% and 7.1% of revenue in those years (FY2025 10-K MD&A), leaving consolidated operating margins of 6.7% and 6.8%.

**The field's returns, judged in words** (section C; "ordinary" carries no figure). Over FY2016 to FY2025 the two durable
builders earned on their operating assets, before tax, about 5% (Trinity) and about 9% (Greenbrier) a year on average with
their leasing arms included; their rail manufacturing margins averaged about 7% (Trinity, operating) and 13% (Greenbrier,
gross) and fell to the low single digits in the 2020 to 2022 trough. That is an ordinary return for the largest players in a
field of a few, near what a long Treasury paid over those years once tax is taken out: "you can have only two competitors and
they’re still terrible businesses" **[M2013-052]**. The filer itself lost money at the operating line in six of the ten years
and averaged a negative return.

**A change for the better** (section C; "the railroads were a terrible business for decades and decades and decades and then they
got good" **[M2017-026]**). The move to Castaños is a real change: from operating losses in FY2017 to FY2022 to operating income
of $37.3M and $33.9M in FY2024 and FY2025. The convention credits such a change only on a full cycle in which the price
behaviour held, and until then sends the file to TOO HARD (NATURE). I do not send it there, for two reasons from the filings.
First, credited in full, the change shows RAIL level with Greenbrier's manufacturing margins in the same years, not ahead of
them on cost, so even credited it produces no low-cost castle, only a place in a field whose durable players earn ordinary
returns, which section C closes OUT, not TOO HARD. Second, the field's volume has already fallen (Trinity's rail-products
revenue down 41.6% in 2025; Greenbrier's deliveries down 8.5% in fiscal 2025), and RAIL's manufacturing gross margin was 3.2%
in the second quarter of 2026 against 13.4% a year earlier (10-Q), on the filer's word an "unfavorable product mix": the price
behaviour of a bid business in a falling field.

**Contrary evidence for the business, weighed.** Backlog of 3,972 cars and $344M at 2026-06-30 against 1,926 cars and $137M at
the end of 2025 (10-Q); segment operating margins above Trinity's in 2024 and 2025; a capital-light, leased plant. None is a
reason the castle stands: a backlog is orders won on bids, and capacity that is cheap to stand up is the same fact that lets
others stand it up.

- **VERDICT: OUT.** A commodity-type field whose durable players earned ordinary returns over the last full cycle (Trinity about
  5%, Greenbrier about 9% pre-tax on operating assets, FY2016 to FY2025), in which this filer averaged a loss and reached at best
  cost parity in its two best years: the standing castle that protects only ordinary returns closes OUT (section C, the moat
  being what "protects excellent returns on invested capital" **[L2007-004]**; **[M2013-052]**). The money test fails on the
  filer's own record of building its capacity cheaply **[M2011-015]**; the customer buys on price **[M2017-009]**,
  **[L2004-003]**; and the one route through a commodity field, the low-cost position **[L2000-017]**, is not shown by the
  margins against Greenbrier, "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**. The castle
  is shown open on the evidence, not unjudgeable, so the box is OUT of the three, "in, out, and too hard" **[M2006-013]**.
  Filing facts: FY2025 10-K `0001193125-26-098668` (Item 1, Competition and Customers; Item 7); 10-Q `0001193125-26-330623`;
  FY2021 10-K `0000950170-22-004254`; FY2022 10-K `0000950170-23-010051`; the rivals' 10-Ks above.

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (closed at Q2).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (closed at Q2); the balance sheets were read in Step 0.
## Q5 — WHO RUNS IT. NOT REACHED (closed at Q2).
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED (closed at Q2).
## Q7 — WHAT IS IT WORTH. NOT REACHED as a question (closed at Q2); the COMPUTATION, NOT A CLEARANCE, for the reporting figures is below.
## Q8 — IS IT BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 — COULD IT RUIN US. NOT REACHED.
## Q10 — IS IT THE FAT PITCH. NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE. NOT REACHED.

---
## COMPUTATION, NOT A CLEARANCE: Q7's range and the fair price, for the owner's two reporting figures
*(The file closed OUT at Q2. Nothing below is a clearance, a verdict or entry language (operator rule 3). Arithmetic in
`valuation.py`, output in `valuation_out.txt`, in the working folder.)*

**The cash input.** Owner cash after every real cost, from the filed cash-flow statements (XBRL first-filed, checked
against the FY2021 to FY2025 10-Ks): operating cash flow, less stock pay, less all capital spending, less finance-lease
principal (FY2022 to FY2025, 0.7, 1.0, 2.1, 1.1), less cash paid for acquisitions (Carly Railcar Components, $6.3M net of
cash, December 2025). This is the equity-only series (after interest). The all-equity series adds back the cash interest
paid (FY2021 to FY2025: 6.5, 8.8, 4.9, 4.6, 13.8) at its cost after the 21% statutory rate. USD millions:

| fiscal year | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| owner cash, equity-only | 38.1 | -37.0 | -25.8 | -69.7 | -60.7 | 0.9 | -10.1 | 34.7 | 20.4 |
| owner cash, all-equity | 38.2 | -36.9 | -25.6 | -69.4 | -55.6 | 7.8 | -6.2 | 38.3 | 31.3 |

**The specifics, in Q7's order.**
- *The window and the cycle, specific (a).* The literal five-year window is FY2021 to FY2025. Its first year is aberrational
  on the filer's own description: the year after "the cyclical industry downturn", with the Shoals plant closed in February
  2021, production moved to Castaños by March 2021, $6.5M of restructuring, and a $24.7M rise in VAT receivable "due to
  production increases and delays in receiving VAT refunds" (FY2021 10-K, `0000950170-22-004254`, Item 7). The base is
  therefore the average over the last full cycle of owner cash, whose peaks are FY2017 (38.1) and FY2024 (34.7): FY2018 to
  FY2024, all-equity **-21.09** a year (equity-only -23.97). FY2017 to FY2023, beside: -21.11. The literal window, beside:
  all-equity **3.12** (equity-only -2.98). A cyclical base is the speakers' own way of reading a lumpy business, "what
  difference does it make to us if the earnings average, say, 300 million a year, if it comes in in a very lumpy fashion?"
  **[M2011-102]**, and of the window's end years, "If either year was aberrational, any calculation of growth will be distorted." **[L2005-003]**.
- *Decline and sign changes, specific (b).* Inside the window the series changes sign (first two years averaging -29.9
  equity-only, last two +27.6); the growth between the halves is meaningless, and between cycles both averages are negative
  (FY2013 to FY2017 -13.7, FY2018 to FY2024 -24.0). **The range is therefore the no-growth case alone, said so**; it has one
  point, not two ends.
- *Acquisitions, specific (c).* The one deal in the window (CRC, $6.3M) is deducted as capital spending; no growth is credited
  in any case, so the organic pair is the same figure. A second aftermarket acquisition closed after 2026-06-30 (earnings
  release of 2026-08-03, exhibit 99.1 to `0001193125-26-330605`); its price was not found in the documents read; credited at
  nothing. Not a serial acquirer (one deal of $6.3M in the window; the half test cannot be read because owner cash before
  purchases is negative over the window, stated).
- *Working capital, specific (d).* Counted, inside operating cash flow. The FY2021 VAT draw is tied by the filer to one event;
  the literal window with it removed is shown beside: all-equity **8.06**.
- *Maintenance, specific (e).* The filing describes the capital spending as "enhancement of machinery and equipment on current
  production lines" (FY2025 10-K, Capital Expenditures) and guides $7.0M to $10.0M for 2026; over the window it ran at 6.2 a year
  against depreciation of 5.0. No growth spending can be separated, so all spending is the maintenance case; the
  depreciation variant (run.py: window mean 0.5 against -0.7 on the capex basis) moves nothing material.
- *The cap, specific (f).* No growth is carried, so no cap applies.
- *Tax* (Q7, Whose tax). The window's owner cash is after the company's own cash tax (mostly Mexican; paid FY2023 to FY2025:
  2.1, 5.9, 7.6). Restated at the 21% statutory rate on each year's pre-tax income before the warrant marks, only FY2024 changes,
  by about $0.3M; the mean moves by less than $0.1M. The shelter (federal loss carryforwards, recorded as a net deferred tax
  asset of $52.1M at 2026-06-30, 10-Q) is valued per case as the present value at 5.43% of 21% of the case's owner cash a year
  until the asset is used: central case nil (no taxable income in it), literal window $11.9M, VAT-adjusted window $25.0M.
- *Net debt* at the latest filed date: debt $100.725M (current 2.875, long-term 97.850) less cash $62.978M = **$37.75M**
  (10-Q 2026-06-30). Operating leases ($44.2M of lease liability, chiefly the Castaños plant) are left out, as Q7 says. No
  floor-plan finance. Shares 32.804M (cover count plus the three penny warrants; the $3.57 warrant left out, about 0.65M shares
  on the treasury method at $5.92, stated). Market value $194.2M; with net debt $231.9M.
- *The floor tested first* (2026-10-10). At the price, all-equity owner cash of about $22M to $23M a year would be needed to
  earn ten percent on the market value plus net debt less the shelter. The central case is -21.1, the literal window 3.1, the
  VAT-adjusted window 8.1. **No case earns the floor at the price** **[M2003-149]** ("there’s just a point at which we drop out
  of the game"), so Q7, had it been reached, would close OUT whatever the width.

**The results** (no-growth case, zero nominal growth for ever, discounted at the 5.43% long Treasury rate; fair price with the
same cash discounted at ten percent; per share):

| case | value a share, all-equity | fair price, all-equity | value a share, equity-only | fair price, equity-only | expected return at $5.92, all-equity |
|---|---|---|---|---|---|
| **CENTRAL: cycle base FY2018 to FY2024** | **-$12.99** | **-$7.58** | -$13.46 | -$7.31 | -9.1% |
| beside: cycle FY2017 to FY2023 | -$13.00 | -$7.59 | -$13.18 | -$7.16 | -9.1% |
| beside: literal window FY2021 to FY2025 | $0.96 | $0.16 | -$1.67 | -$0.91 | 1.4% |
| beside: literal window, FY2021 VAT draw removed | $4.14 | $2.07 | $1.33 | $0.83 | 3.9% |

Two checks that are not cases, flagged as chosen start years ("growth-rate presentations can be significantly distorted by a
calculated selection of either initial or terminal dates" **[L2003-004]**): the years after the move only, FY2022 to FY2025,
all-equity owner cash 17.8 a year, an expected return of 9.1% at the price and a no-growth value of $9.93 a share; the two best
years only, FY2024 and FY2025, 34.8 a year and 18.3%. The second is the whole case for the business: it holds if, and only if,
2024 and 2025 are the normal year of the new business, which the first half of 2026 (operating loss of $4.9M, 10-Q) and the
field's record do not show.

**The two reporting figures** (a reporting convention, not a rule; neither is a verdict):
- **(a) VALUE RANGE:** a single no-growth point, **-$12.99 a share** (all-equity, cycle base FY2018 to FY2024, after the company's
  own tax), against **$5.92**; the literal window beside at $0.96 (equity-only -$1.67). The range has no width because the shown
  growth is meaningless (specific (b)).
- **(b) FAIR PRICE:** **-$7.58 a share** on the all-equity basis (the central figure), **-$7.31** equity-only beside; on the literal
  window, $0.16 all-equity and -$0.91 equity-only. No price earns the floor on the central case.

---
## THE BOX
**OUT at Q2 (Q1 IN): a standing castle that protects only ordinary returns** (Trinity about 5% and Greenbrier about 9% pre-tax on
operating assets over FY2016 to FY2025; this filer a loss on average and at best at cost parity with Greenbrier's manufacturing
margins in its two best years); **integrity facts recorded, not judged**. COMPUTATION, NOT A CLEARANCE: value -$12.99 a share
(no-growth single point, all-equity, cycle base) against $5.92, literal window $0.96 beside; no case earns the floor; fair price
-$7.58 all-equity (-$7.31 equity-only). No research pass (the box is OUT, not TOO HARD).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down as found, "write it down in the first 30 minutes" **[M1997-127]**; no verdict on any of them; the box is unchanged.)*
- **Q3 (capital).** Property, plant and equipment $28.4M at 2026-06-30; the plant is leased (the lease reclassified from finance to
  operating in 2025: right-of-use finance asset $45.1M at the end of 2024, operating $40.3M at the end of 2025; FY2025 10-K).
  Capital spending ran near depreciation over the window; inventory swings with deliveries ($125.0M at the end of 2023, $57.8M at
  2026-06-30); a VAT receivable of $6.7M (10-Q) that drew $24.7M of cash in 2021.
- **Q4 (the accounts).** Warrant fair-value losses of $99.5M (2024) and $32.2M (2025), non-cash and non-operating, from warrants
  issued in financings; FY2025 net income of $38.1M includes a $49.0M tax benefit from the release of a valuation allowance;
  FY2025 other income includes a $3.3M Employee Retention Credit and a $2.1M bargain-purchase gain; FY2023 a $14.9M loss on
  extinguishment of debt. The earnings release of 2026-08-03 features Adjusted EBITDA ($1.2M for the quarter) and gives
  full-year guidance (deliveries 3,500 to 3,900, revenue $410M to $460M, Adjusted EBITDA $36M to $44M), and states "our share of
  industry new-railcar orders reaching approximately 45%" for the quarter. To be weighed at Q4 and carried to Q5 if a later run
  reaches them.
- **Q5 (integrity, recorded and not judged).** (1) Related-party payments: the company paid $24,543,000 in 2025 to the family of
  director Jesús Gil (Fasemex, the plant's lessors, a supplier, a trucker, a warehouse) "related to steel fabrication services,
  rent and security deposit payments for the Manufacturing Facility, material and safety supplies, trucking services, royalty
  payments, and rent of an external warehouse" (proxy, `0001213900-26-031465`, Certain Relationships). (2) On 2026-08-05, after
  the lender's affiliate exercised its warrants, the board adopted a rights agreement; on 2026-10-14 it terminated it under a
  Stockholder Agreement with the OC III holders (about 48.8%), agreeing to adopt no future rights plan with a threshold below 20%,
  with board review of transfers to a would-be holder of more than 20% (8-Ks `0001213900-26-085699`, `0001213900-26-109859`).
  (3) Guidance and a featured Adjusted EBITDA (Q4 above); Adjusted EBITDA also weighs 31.67% of the CEO's and CFO's annual bonus
  (proxy). (4) Corporate professional services expenses rose $5.5M in 2025 (FY2025 10-K MD&A); the cause is not stated in what I
  read. CEO total pay $2.03M (2025) and $2.30M (2024) (proxy, Summary Compensation Table). Any later run that reaches Q5 must
  answer these first (Part VII).
- **Q6 (the money and the owners).** Warrants issued in 2020, 2021 and 2022 to the lender's affiliate for 23%, 5% and 5% of the
  fully diluted common at $0.01, and in 2023 for 1,636,313 shares at $3.57 (10-Q, Warrants); the June 2026 net exercise issued
  13,619,377 shares for no cash, about 41.5% of the shares now outstanding. Series C preferred of $85.4M issued in 2023 in exchange
  for a term loan and redeemed in 2024 from a $115.0M term loan, with $27.9M of dividends paid that year (FY2025 10-K). No dividend
  on the common, no buyback. Q6's buyback test is moot (no buyback).
- **Q9 (debt and exposures).** Term loan $100.7M at 9.7% (2026-06-30), maturing 2028-12-31, with liquidity and quarterly leverage
  covenants; a $35M asset-based revolver with a springing maturity of 2028-10-02 (10-Q); the top five customers about 75% of 2025
  revenue; a sole supplier of roll-formed center sills (66% of new cars in 2025); one plant in Mexico; tariffs named by the filer.
- **Q12.** Nothing found that bears on it.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early): template
      copy `a4c7ee23`; Step 0 to Q1 `c8498e80`; Q2 `57f5f099`; the close in the commit after this one.
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session (the brief says so; I did not touch it); the fold into the register is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule); what was seen by
      accident is declared at the top under Contamination and was not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in its row (`check_ids.py` in the
      working folder, PASS); every filing fact carries its accession; numbers of mine are arithmetic on filed figures, in the
      working scripts.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; everything after it is headed COMPUTATION, NOT A
      CLEARANCE or AFTER THE STOP.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing authority (US
      Treasury par curve); the price an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (the foundations line, and the contrary evidence for the
      business weighed at Q2); facts for later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor is cited in a point-in-time run: not a point-in-time run (anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS before the closing commit.
- One slip to declare: the first write of the run file replaced the template whole with the sections then closed, so the
  template's later headings (Q2 onward, the box, the audit) were re-added by hand as each part closed; nothing in them was
  changed from the template's wording except to fill them.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Section C carries two exits for one fact pattern.** A filer that has improved, on a change not yet tested by a full cycle,
inside a field whose durable players earn ordinary returns, can be sent to TOO HARD (NATURE) by the change-for-the-better
sentence or to OUT by the ordinary-returns item; the text does not say which governs. I read the ordinary-returns item as
deciding where the improvement, credited in full, reaches only parity with the field (the improvement then cannot make a
castle), and said why in Q2; a case may want to write that down. (2) **Specific (a) has no rule for a business that changed its
form inside the cycle.** RAIL's last full cycle of owner cash (FY2018 to FY2024) is mostly the US-plant business it closed in
2020 and 2021; the convention values that business, and the change-for-the-better rule that might speak to it sits at Q2, not Q7.
I kept the convention's base central and showed the post-move years as a flagged check. (3) **The shelter convention says
carryforwards "that run out inside ten years".** Post-2017 federal losses never expire; "run out" can mean expire or be used up.
I valued the shelter by use (until the recorded asset is exhausted), stated. (4) **The all-equity basis names no tax rate for
the interest added back.** I used the 21% statutory rate, stated; a company that pays no US tax because of its losses gains no
cash from the deduction, so the choice slightly flatters the all-equity case. (5) **The brief's rival rule meets a 10-K with no
Item 1A and no named rivals.** A smaller reporting company may omit risk factors; I took the rivals the filer last named (FY2022
10-K) as a CONVENTION of the run before choosing my own, and said so.
