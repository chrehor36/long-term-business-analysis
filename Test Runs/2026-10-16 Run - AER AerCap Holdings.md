# Company Run — AerCap Holdings N.V. (NYSE: AER) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-16), after the run was committed: **not held** (`PORTFOLIO.md` carries no line for AER or AerCap).

**Dispatch.** Dispatched blind analyst run under `Screens/_daily/_dispatch_brief.md`, with the brief's one stated
departure: the lines of evidence were not handed over in a list; the analyst derived them from the 20-F's Item 4
(business), Item 3.D (risk factors) and Item 5 (operating and financial review), which are the 20-F's counterparts of a
10-K's Items 1, 1A and 7. Those three items of the FY2025 20-F were read for this run, with the financial statements and
notes the questions below needed.

**Contamination declared.** (1) Before reading the blind rule's full reach I ran one filtered listing of `Test Runs/`
for "AER" or "AerCap" file names; it returned nothing. No file was opened. (2) The session's starting git status and
commit subjects showed other companies' research folders and an overnight fold of another ticker; nothing about this
company. (3) The project memory index carries a line about the queue's count of gate-clearers; nothing about this name.
None of it was used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $147.33 (2026-10-16; live quote printed by `tools/run.py`, an aggregator, flagged per operator rule 5).
- **Shares by class:** one class, ordinary shares. `python Screens/cover_shares.py AER` returns 166,876,547 from the
  20-F cover as of 2025-12-31 (accession `0001628280-26-007513`), which checks: 179,043,739 issued less 12,167,192
  treasury = 166,876,547 (20-F Item 4, History and development). That count is stale: the latest interim report, 6-K
  accession `0001628280-26-050456` (filed 2026-07-29, to 2026-06-30), states 170,043,739 issued less 12,859,674
  treasury = **157,184,065 outstanding** (including 2,754,000 unvested restricted shares), after 10.3 million shares
  repurchased in the first half at an average $140.10 and 9.0 million cancelled. The 6-Ks filed after it (2026-09-16,
  2026-09-23, 2026-10-07) were not read for share counts; by the brief they are senior-note issues. **Count used:
  157,184,065.**
- **Market cap:** 157.184M × $147.33 = **$23,158M**.
- **Net debt at the latest filed date (2026-06-30, same 6-K):** debt $42,773.5M less cash and cash equivalents
  $1,686.4M = **$41,087.1M** (restricted cash $113.1M not deducted; the $2.25bn of junior subordinated notes counted in
  full although the company gives them a 50% equity credit; lessee deposits $1.2bn and the accrued maintenance liability
  $3.5bn are operating liabilities and are left out, said so; no operating leases of size). No subsequent event stated in
  that filing adds debt; the July 2026 order for 15 Boeing 787s is a purchase commitment. **Enterprise value at the price:
  $64,245M.**
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-15
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 20-F for FY2025 (filed 2026-02-12, accession `0001628280-26-007513`): Item 3
  (risk factors), Item 4, Item 5, the financial statements (balance sheets, income statement, cash flows) and the
  segment, debt and Ukraine notes as cited; 20-F for FY2023 (`0001378789-24-000010`), FY2021 (`0001378789-22-000006`),
  FY2018 (`0001378789-19-000009`) for the cash flows, balance sheets and income statements of 2016 to 2023; FY2020 20-F
  (`0001378789-21-000007`) fetched, used only through the FY2021 20-F's comparatives; interim 6-K to 2026-06-30
  (`0001628280-26-050456`, the interim report and the earnings release exhibit); the compensation report filed by 6-K
  (`0000950157-26-000221`, exhibits 99.1 to 99.3). **One figure cross-checked:** net cash from operating activities
  FY2025 $5,393,124 thousand on the filed cash-flow statement (F-7) equals the XBRL figure $5,393M that `tools/run.py`
  reads; total assets FY2025 $71,671,790 thousand on the filed balance sheet equals the tool's $71,672M.
- **`python tools/run.py AER`, arithmetic lines only:** it prints owner earnings for 2011 to 2013 only, because the
  capital-spending elements it reads stop being tagged after 2013 (it says so); its owner-earnings lines are not used.
  Its ten balance sheets 2016 to 2025 are used (read against the filed statements; Q4 material below, read here in Step 0
  because the file may close before Q4). Owner cash is built by hand from the filed cash-flow statements: see the
  COMPUTATION section. Its v4 material was not read as a rule (Part VII, the tooling).

**The balance sheets, eight to ten years, before the income account** **[M2025-032]** (read in Step 0; `tools/run.py`
table checked against the filed 2025, 2023 and 2021 balance sheets; USD millions):

| year-end | total assets | equity | debt | cash | assets / equity |
|---|---|---|---|---|---|
| 2016 | 41,620 | 8,524 | 27,717 | 2,035 | 4.9 |
| 2018 | 43,209 | 8,828 | 29,508 | 1,204 | 4.9 |
| 2019 | 43,749 | 9,315 | 29,486 | 1,121 | 4.7 |
| 2020 | 42,048 | 8,864 | 28,742 | 1,249 | 4.7 |
| 2021 | 74,570 | 16,571 | 50,205 | 1,729 | 4.5 |
| 2022 | 69,727 | 16,118 | 46,533 | 1,597 | 4.3 |
| 2023 | 71,275 | 16,589 | 46,484 | 1,627 | 4.3 |
| 2024 | 71,442 | 17,185 | 45,295 | 1,209 | 4.2 |
| 2025 | 71,672 | 18,323 | 43,565 | 1,379 | 3.9 |
| 2026-06 | 71,184 | 18,410 | 42,774 | 1,686 | 3.9 |

What they say: total assets were flat at about $42bn to $44bn from 2016 to 2020, nearly doubled in 2021 with GECAS
(closed 1 November 2021: 111.5 million new shares, about $23bn of cash and $1bn of notes, financed with $24bn of new debt,
FY2021 20-F), fell in 2022 with the Russia write-off, and have been flat at $70bn to $72bn since. Debt is three-fifths of
assets throughout. Equity rose from $16.1bn (2022) to $18.4bn (2026-06) while about $8.5bn was spent on buybacks
2023 to H1 2026, so retained earnings, not new capital, carried it. Goodwill: none; other intangibles $118M. The lease
assets themselves (flight equipment held for operating leases, finance leases, held for sale, prepayments, maintenance
rights) were $69.1bn (2021), $64.0bn (2022), $64.9bn (2023), $65.8bn (2024), $66.7bn (2025): the earning base has
grown about 1.4% a year since the Russia loss, and the maintenance-rights asset bought with GECAS is being used up
($4.4bn in 2021 to $1.7bn in 2025). What they cannot say: the market value of the fleet against its book (the company
reports gains on sale of 20% to 27% over book in 2025 and 2026, a strong sale market by its own description) and the
condition of about 300 airline lessees.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what roughly $66.7bn of aircraft, engines and helicopters,
leased to about 300 airlines and financed with about $43bn of debt, will earn its owners, not what the quote does. The
market's recent behaviour (a 50% rise in 2025, the company's own compensation report) instructs nothing **[M2006-077]**.
The analyst's habits govern the reading: look for "what’s wrong" and "what you’re missing" **[M2025-013]**, and
write contrary evidence down as found **[M1997-127]**. **Contrary evidence, written down as found** **[M1997-127]**:
(1) the 20-F names no rival and calls the field "highly competitive", with competition "based on [...] lease rates"
(Item 4, Competition); (2) Russia: "we were only able to recover a small minority of the assets and in 2022 wrote-off
the rest" (Item 3.D), a $2.67bn charge on the 2022 income statement; (3) the 2023 to 2025 returns that the company
features (ROE 21% in 2025) contain $2.95bn of Russia recoveries and a sale market the company itself ties to "ongoing
aircraft supply constraints" (Q2 2026 release); (4) two rivals' own 10-Ks say some competitors have a lower cost of
capital, and one says barriers to entry "are relatively low" (Q2 below); (5) adjusted EPS is featured, guided, and is the
main pay metric (compensation report).

## THE STANDING RULE
Owning a part-interest bought with the buyer's own money, unlevered and sized so that a 50% fall is borne, puts the
buyer at no risk of ruin; borrowed money to own it is ruled out, "borrowed money has no place in the investor's tool kit"
**[L2014-005]**, **[M2004-065]**. The target's own leverage is a different matter and is weighed at Q9, not here
**[M2012-081]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The business, from Item 4.** AerCap buys aircraft (and engines and helicopters) mostly new from Airbus, Boeing and
Embraer, leases them on operating leases of up to about 16 years to about 300 airlines in every region, sells them in
mid-life, and funds the fleet with about $43.8bn of debt (Item 5). At 2025-12-31 it owned 1,501 aircraft, managed 148,
had 283 on order (purchase obligations $15.5bn, 2026 to 2031), owned 470 engines and 323 helicopters; utilization 99%;
top five lessees 18.5% of lease revenue; 45% of lease revenue from emerging-market airlines (Item 3.D). The filer reports
one segment, "leasing, financing, sales and management of commercial flight equipment" (notes), so Q1's
holding-company paragraph and Q2's parts table do not apply; engines (9% of net book value) and helicopters (6%) sit
inside the one segment.

**The key variables and how predictable they are** **[M1998-044]**: (1) demand for leased aircraft: air traffic and the
OEMs' ability to deliver (the 2025 RPK growth of 5.3% and "supply constraints" are the filer's own Item 5 words);
(2) the lease rate the market sets against the funding cost: fixed rents "initially determined in part by reference to
the prevailing interest rate for a debt instrument with a term similar to the lease term" (Item 5), against an average
cost of debt of 4.1% (2025); (3) the residual value at sale, shown by gains on sale ($819M on $3.9bn of proceeds in 2025)
and by the impairment test (the 339 passenger aircraft of 15 years or more, $3.0bn, carried with undiscounted cash flows
141% above book, Item 5); (4) lessee credit, which the company itself calls the risk that "airlines with high financial
leverage are more likely [...] to seek operating leases" (Item 3.D); (5) access to funding: BBB+ from all three agencies,
$11.0bn undrawn, 1.8 times the next twelve months' maturities and commitments (Item 5).

**Ten years out** **[M2012-065]**, **[M2000-037]**: I can picture the business in 2036 doing what it does now, leasing
mid-life and new narrowbodies and widebodies to airlines on spreads over its funding cost, as it did through 2009, 2020
and 2022 (the filings read cover 2010 to 2026). The forecast is about airlines' demand for capacity and their use of
leases, not about a technology turning over the product: the product is a long-lived airframe whose types change on a
decade scale and are visible in the order book **[M2017-019]**. What I cannot foresee is the price of money and of
aircraft in a given year; those are the cycle, and they belong to Q2 and Q7, not to whether the economics can be seen
**[M2011-014]**. Would the insiders write it down **[M2000-105]**? They do: the depreciation policy is a written
25-year life and 15% residual for passenger aircraft (Item 5, critical estimates), and the lease book runs to 2035 and
beyond (Item 4, scheduled expirations). The statements do tell me something about the future statements **[M2008-033]**:
the fleet, the lease expiries, the order book and the debt maturities are all scheduled in the filing.

**The financial-institution rows** (Q1 owns them; how far the text reaches a lessor). A lessor is not a bank: it takes no
deposits and runs no derivatives book of size (interest-rate swaps hedge the floating 25% of its debt, Item 3.D). But it
is a lender in substance, owning aircraft on borrowed money, so the rows on institutions reach it as far as their own
words do. (a) **The asset side can be read** **[M2002-022]**, **[M2011-022]**: the filing gives the fleet by type, age
and net book value, lessees by region, the largest five, lease expiries by year, the off-lease aircraft (44 at year-end,
27 being remarketed, about 2% of book), and the impairment headroom. This is not a book whose condition "no one probably
knows" **[M2005-068]**. (b) **The funding side is wholesale** **[M2012-012]**: bonds, bank lines, export credit and
securitizations, with no "natural customer base" **[M2012-012]**; its money is not "so cheap" **[M2011-022]**. But it is term money:
maturities are scheduled ($6.2bn in 2026, $7.3bn in 2027), not deposits that "can run pretty fast". The rows' door for
a bank, "very cheap money on the deposit side" **[M2002-022]**, is therefore half open: the asset side is readable, the
cheap-money half does not exist. (c) **Can it continually fund itself** **[M2002-094]**? On the record, yes, through
two shocks: in 2020 it issued $10.9bn and repaid $11.6bn of debt (FY2021 20-F, cash flows), and in 2022 it absorbed the
Russia write-off without breaching (it repaid $4.2bn net that year). (d) **A no-growth test** **[L2004-009]**: from
2016 to 2020 the asset base was flat at $42bn to $44bn and the business earned 11.7% to 12.6% on equity in 2016 to 2019
(XBRL first-filed figures, field table at Q2); so the earning power is not an artefact of growth.

**The doubt rule** **[M2002-092]**, **[M1997-024]**. The one place I doubt my reading is the residual and credit
tail: Russia showed that aircraft in one country (an insurance claim covering 113 owned aircraft and 23 spare engines,
FY2023 20-F; a $2.67bn charge in 2022 against lease assets of about $64bn, some 4%) can be lost to a government in weeks,
and how far off I can be
**[M2011-084]** on lessee credit across 45% emerging markets is wide. That doubt is about the size of the downside, not
about whether the economics can be seen; it is weighed at Q9 (debt and exposures) and enters Q7 as the width of the
range. It does not make the business unforeseeable: the doubt is how bad a bad year can be, not what this
business will be in ten years.

- **VERDICT: IN.** The economics of an aircraft lessor ten years out (rent on long-lived, mobile assets to airlines,
  funded by scheduled term debt) can be foreseen from the filings **[M2012-065]**, **[M2008-033]**; the asset side can be
  read, which is the condition the rows set for a financial business **[M2002-022]**, **[M2005-068]**; funding is
  wholesale, not cheap and not run-prone, and is carried to Q9 **[M2012-012]**. Q1 decides only that the questions can be
  asked; whether the castle stands is Q2's.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question starts from the attacker **[M1995-038]**: "all moats are subject to attack in a capitalistic system".

**The castle tests, each with its filing fact.**
- **The attacker with money** **[M2011-015]**, **[M2012-106]**. Money has just come in, at scale: Air Lease, the
  second US-listed lessor, was taken private on 2026-04-08 by a holding company "jointly owned, directly or indirectly,
  by Sumitomo Corporation [...] SMBC Aviation Capital Limited [...] Apollo [...] and Brookfield" (Air Lease 8-K,
  accession `0001193125-26-147571`). Aircastle's 10-K (FY to 2026-02-28, accession `0001628280-26-026216`) says the
  industry is "characterized by ongoing merger and acquisition activity and new entrants, as barriers to entry are
  relatively low", and that mid-life aircraft are contested by fund-backed "new entrants". AerCap's own risk factor:
  "competitors have increased in relative size to AerCap due to consolidation" (Item 3.D). Given ten billion dollars, a
  well-funded owner can buy aircraft from the same two manufacturers and lease them to the same airlines; the record says
  owners keep doing it. **Fails.**
- **Would the customer still choose it over the low bid** **[M2017-009]**, **[L2004-003]**. The 20-F: "Competition for
  a leasing transaction is based on a number of factors, including delivery dates, lease rates, term of lease, other
  lease provisions, aircraft condition and the availability in the marketplace of the types of aircraft that can meet
  customer requirements" (Item 4). Air Lease's 10-K (FY2025, `0001628280-26-007707`) lists the same factors in the same
  order. The airline asks for an A320neo or a 787 at a rate and a date; nothing in the filings shows it asking for AerCap
  by name. The product is the manufacturer's aircraft plus money. **Fails.**
- **Pricing power, and the agony before a rise** **[M2005-020]**. Fixed rents are set "in part by reference to the
  prevailing interest rate for a debt instrument with a term similar to the lease term and with a similar credit quality
  as the lessee" (Item 5): the rent follows the price of money and the lessee's credit, not the lessor. In 2025 basic
  lease rents fell $94M "primarily due to lease extensions at lower rates, lower PBH rent, as well as redeliveries and
  lease terminations" (Item 5). Rents have risen since 2023 with aircraft scarcity, which is the cycle's doing (below).
- **Unit volume** **[M1999-054]** is not the measure where the customer buys capacity: AerCap's owned fleet went from
  962 aircraft (2018) to 1,501 (2025) only by buying GECAS, and in 2025 it shrank from 1,543 to 1,501 as it sold 113 and
  bought 71 (Item 4).
- **The low-cost position** **[L2000-017]**, **[M1997-010]**, **[M2001-013]**, read from the filings **[M2009-059]**,
  **[M2006-004]**. Its cost of money is 4.1% (2025, Item 5) at BBB+. Two rivals' own 10-Ks say some competitors have
  "access to lower capital costs" (Air Lease) or "a lower cost of capital" (Aircastle); the new owners of Air Lease
  include a bank's lessor, and the speakers' own row on leasing says why that matters: "pure money-type leasing is not
  an attractive business for us when we’ve got other people with a lower cost of funds. I mean, they’ve got the edge."
  **[M2016-029]** (a row about the speakers' own position and about car leasing; weighed, not a verdict on this field,
  by Q2's convention on a row about one company). AerCap claims purchasing discounts from scale (Item 4); if they exist
  they do not show in the return below, which is Air Lease's to a tenth of a point over twelve years. **No low-cost
  position on the record.**
- **Ask the competitors** **[M1999-130]**: not possible from the record, beyond the competitors' filings calling the field
  low-barrier and capital-cost-driven (above).
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Returns since 2023 are higher (pre-financing return on
  assets, excluding the Russia items, 4.5% in 2022, 5.4% in 2023, 5.7% in 2024, 6.4% in 2025), and the company says why:
  "ongoing aircraft supply constraints" (CEO, Q2 2026 release, `0001628280-26-050456`) and "supply constraints continue
  to keep load factors at record highs" (Item 5). That is the manufacturers' shortfall lifting every owner of aircraft,
  not a moat AerCap built. A change for the better is credited only on a full cycle in which the price behaviour held
  **[M2005-020]**, **[L1995-022]**; the full cycle on the record (2014 to 2025) is below, and it is ordinary.
- **What could destroy, modify or reduce it** **[M2000-014]**: governments (Russia, 2022: a $2.67bn charge; about
  $2.95bn recovered from insurers by settlement and court judgment 2023 to 2025, Item 5 and FY2023 20-F); pandemics (2020:
  $1.09bn of impairment and a net loss of $295M, FY2021 20-F); manufacturers' failures and emissions rules on older
  aircraft (Item 3.D; Item 4, Regulation). Each was survived on the record; none is a moat.

**The competitor row.** The 20-F names no rival: "Our competitors are primarily other major aircraft leasing
companies" (Item 3.D). The rivals below are therefore a **CONVENTION of this run**: the three aircraft or engine lessors
that file annual statements with the SEC; rationale: they are the only lessors whose own filed statements can be read
for the same metric. Rivals that Aircastle's 10-K names and that do not file with the SEC (flagged): SMBC Aviation
Capital, Avolon, Dubai Aerospace Enterprise, Aviation Capital Group, BOC Aviation, Carlyle Aviation Partners,
Castlelake. Metric: pre-tax income plus interest expense over average total assets (a return on all capital before
financing), and net income over average equity; first-filed figures from each filer's own annual XBRL, worked in
`Test Runs/_research 2026-10-16 AER/field_returns.txt`. One figure cross-checked: Air Lease FY2025 income before taxes
$1,369,693 thousand on its filed 10-K equals the series.

| filer (accession of latest annual) | span | pre-tax, pre-interest return on average assets, mean | net income on average equity, mean | assets / equity |
|---|---|---|---|---|
| AerCap (20-F, `0001628280-26-007513`) | 2014-2025 | 5.3% | 11.0% | 3.9 to 5.6 |
| Air Lease (10-K, `0001628280-26-007707`) | 2014-2025 | 5.2% | 9.6% (2015-2025) | 3.8 to 4.3 |
| Aircastle (10-K, `0001628280-26-026216`) | FY2015-FY2026 (February years) | 4.3% | 2.8% | 3.4 to 4.5 |
| Willis Lease Finance (10-K, `0001018164-26-000036`) | 2014-2025 | 5.5% | 11.2% | 5.5 to 6.8 |

AerCap year by year, pre-financing return on average assets: 6.4% 2014, 5.6% 2015, 5.4% 2016, 5.6% 2017, 5.5% 2018,
6.1% 2019, 2.2% 2020, 4.1% 2021, 0.8% 2022, 7.2% 2023, 6.0% 2024, 8.5% 2025 (2023 and 2025 include $1.29bn and $1.49bn
of Russia recoveries).

**The parts table:** none; the filer reports one segment (FY2025 20-F, notes).

**The field's returns over the last full cycle, judged in words.** The span 2014 to 2025 holds an upswing (2014 to 2019),
a trough (2020), the loss of a country's fleet (2022) and the recoveries after it (2023 to 2025). Across it the four
lessors earned about 4% to 5.5% a year before financing on what they own, against a cost of debt AerCap puts at 4.0% to
4.1% (2024, 2025; Item 5) and against today's 30-year Treasury at 5.43%. AerCap's 11% on equity is that thin spread
multiplied by four to five times leverage: "part of that is because the banks are geared up more" **[M2007-013]**, a
business "dealing in what is basically a commodity — money". The largest firm in the field earns before financing what
the smaller ones earn; its size has bought it the steadiest funding, not a higher return. This is the standing castle
that protects only ordinary returns: the moat is what "protects excellent returns on invested capital"
**[L2007-004]**, and the returns protected here are those of a leveraged lender **[M2013-052]**, **[M2000-072]**. The
return is not set by a regulator, so the regulated exception does not apply.

**The other side, stated as well as I can** **[M2016-055]**: AerCap is the largest lessor by far, with 283 new aircraft
on order in a market short of them, 99% utilization, investment-grade funding that held through 2020 and 2022,
remarketing reach to 300 airlines, and gains on sale of 20% to 27% over book in 2025 and 2026 that suggest its book
values are conservative. All true; none of it shows in a return on assets above the field's over a full cycle, and gains
over book mean the return on what the fleet is actually worth is lower than the book figure, not higher.

- **VERDICT: OUT.** The castle is shown open on the evidence **[M2011-015]**: the customer buys on lease rate and
  delivery **[L2004-003]**, **[M2017-009]**; well-funded attackers, some with a lower cost of capital, keep entering and
  consolidating, by the rivals' own filings **[M2012-106]**, **[M2016-029]**; no low-cost position shows in the figures
  **[M1997-010]**, **[M2009-059]**; and the field, AerCap included, earns ordinary returns before financing over a full
  cycle, lifted to 10% to 12% on equity by gearing **[M2007-013]**, **[L2007-004]**. Not TOO HARD: the returns are known
  from the filings, so the tenuous-moat row's reason, "We don’t know how to valuate that" **[M2000-019]**, does not
  apply. The file closes here. **Q3 to Q12 NOT REACHED.**

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING. NOT REACHED (facts under AFTER THE STOP).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED (balance sheets read in Step 0; facts under AFTER THE STOP).
## Q5 — WHO RUNS IT? NOT REACHED (facts under AFTER THE STOP).
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED (facts under AFTER THE STOP).

## Q7 — WHAT IS IT WORTH? NOT REACHED as a question. COMPUTATION, NOT A CLEARANCE (below), for the reporting figures.

### COMPUTATION, NOT A CLEARANCE
*Everything in this section is arithmetic under Q7's conventions, done after the file closed at Q2, for the operator's
reporting figures (Part VII, The owner's price). It carries no entry language and clears nothing (operator rule 3).
Worked in `Test Runs/_research 2026-10-16 AER/q7_computation.py`, output `q7_output.txt`.*

**Owner cash, built by hand from the filed cash-flow statements** (FY2025, FY2023 and FY2021 20-Fs; USD millions). The
tool could not do it: the purchase lines are untagged for it after 2013 (Step 0). The pieces:
- Net cash from operating activities, less share-based compensation (a real cost **[L2021-003]**), less the deferred tax
  the statement adds back, so that the company's own tax is charged as booked (**CONVENTION of this run**: the deferral
  comes from tax depreciation on a fleet that must be replaced, and a no-growth fleet's deferral stops growing; "I don’t
  think I would look at that as a hidden form of equity" **[M2015-030]**); the cash-tax variant is not carried.
- Plus maintenance payments received less returned (financing lines in the filer's statement; they are rent paid for the
  wear on the aircraft and the filer releases the unspent balance to income) (**CONVENTION of this run**); security
  deposits received and returned are left out, being returnable.
- Russia insurance recoveries ($1.25bn 2023, $0.17bn 2024, $1.49bn 2025, in investing) left out: aberrational
  **[L2005-003]**, and the 2022 loss they repay was not a cash outflow inside the window.
- **Maintenance spending, the guess the filing allows** **[M2000-144]**, **[L1999-024]**: depreciation and amortization
  as the proxy **[M1998-127]**, less the gains on sale (book value recovered above book), plus the other consumption of
  lease assets that the operating cash flow adds back or collects (maintenance-rights write-offs, impairments, and the
  principal collected on finance leases) (**CONVENTION of this run**, the components named; rationale: each is lease
  capital used up and not inside depreciation). Checked against a second guess, net spending less the growth in the
  lease-asset base (2023 to 2025): within 9%.
- All spending: purchases of flight equipment plus prepayments, less sale proceeds.
- **Acquisitions (specific (c)).** GECAS (closed 2021-11-01) was paid with about $23bn of cash and $1bn of notes plus
  111.5 million shares (FY2021 20-F): the cash part is the larger by the filing's own terms, so it is an acquisition,
  capital spending. Net purchases over the window ($22.5bn) exceed half of owner cash before purchases, so **the serial
  acquirer rule makes the organic pair central**: purchases left out, organic growth credited. The filer reports no
  organic growth; no business was bought after 2021, so growth measured between 2022 and 2025 is organic. The debt that
  paid for GECAS is in today's net debt. The default pair (GECAS deducted) is beside.

| year | maintenance-only owner cash (central) | all-spending owner cash, GECAS left out | GECAS deducted | after-tax interest paid (all-equity add-back, 15%) | lease revenue |
|---|---|---|---|---|---|
| 2021 | 1,804 | 2,852 | -19,641 | 944 | 4,412 |
| 2022 | 2,335 | 3,378 | 3,378 | 1,330 | 6,531 |
| 2023 | 2,687 | 1,389 | 1,389 | 1,403 | 6,860 |
| 2024 | 3,059 | 1,806 | 1,806 | 1,535 | 7,004 |
| 2025 | 3,038 | 2,245 | 2,245 | 1,624 | 7,369 |

**The base (specific (a)), a CONVENTION of this run:** the four full years of the combined company, 2022 to 2025, because
2021 holds two months of GECAS and is aberrational as a base on the filing's own description of the deal; the literal
2021 to 2025 window is shown beside. Maintenance-only base **$2,780M** (equity basis, after interest); all-spending base
$2,204M. All-equity: add interest paid net of capitalized, after tax at 15% (**CONVENTION of this run**: the Pillar Two
minimum rate the filer says applies from 2024, Item 5), average $1,473M: maintenance-only **$4,253M**, all-spending $3,678M.

**Growth and the cap (specifics (b), (e), (f)).** The maintenance-only series shows 9.2% a year 2022 to 2025. Carried ten
years it would need owner cash of 61% of lease revenue against a highest filed share of 43.7% (2024), so it is cut to the
business's own lease-revenue growth over the same years, **4.1%** **[M1999-067]**, **[M1997-095]**. By (e) the central
case is maintenance-only, and the growth case charges the growth spending actually made against the growth it buys:
**no-growth end = maintenance-only base at 0%; growth end = all-spending base at 4.1%** **[L2000-023]**, **[M2014-068]**.
Ten years, then zero nominal growth, at the 30-year Treasury, 5.43%.

**The floor, tested first** **[M2003-149]**. Expected return at the price (the discount rate at which each end equals the
price; all-equity against market value plus net debt, $64,245M): **6.62% (no-growth end) and 7.75% (growth end)**. No
case earns the floor of about ten percent on the central basis. Under Q7 the file would close **OUT here as well**,
whatever the width. (Equity-only, beside and never deciding alone **[L2017-004]**: 12.00% and 12.36%; that the
equity-only figure clears and the all-equity one does not is the leverage at work, the flattery the all-equity basis
exists to refuse.)

**(a) THE VALUE RANGE** (Q7's range convention in full; per share, 157,184,065 shares; whole-business value less net debt
$41,087M): **$236.88 to $336.73**, width 1.42 to 1, against **$147.33**. The price sits below the bottom of the range
discounted at the government rate, and still no case earns ten percent on what is paid for the business: the range is
built at 5.43% and the business earns about 6.6% after its own tax and before financing on its price (market value plus
net debt), so the risk-free discount values them far
above what a ten percent owner would pay **[L2000-025]**, **[M2009-005]**.

**(b) THE FAIR PRICE** (Part VII: each end valued with its own cash at ten percent, the two averaged; after the company's
own booked tax; no conversion): **all-equity basis (central): $28.83 a share** (ends $9.17 and $48.49); **equity-only
basis, beside: $181.30 a share** (ends $176.85 and $185.76). The two differ by six times because $41bn of debt stands
ahead of the shares and the unlevered return is below ten percent; the all-equity figure is the one the convention makes
central.

**Shown beside** (none of them changes the closes above):

| variant | range at 5.43% (all-equity, per share) | fair price all-equity / equity-only | return at the price, all-equity |
|---|---|---|---|
| maintenance-only at 4.1% with growth spending not charged | $236.88 to $430.29 | $53.07 / $205.54 | 6.62% / 8.86% |
| literal window 2021-2025, maintenance-only, 0% and 4.1% | $201.60 to $381.33 | $30.81 / $191.11 | 6.15% / 8.28% |
| all-spending series at its own growth between halves of 2022-2025 (-7.8%), the (b) decline | -$28.55 (end alone) | -$121.04 / $84.14 (end alone) | 2.85% |
| asset-base maintenance check, 2023-2025 | $231.39 to $422.68 | $49.61 / $198.56 | 6.55% / 8.77% |
| default pair: GECAS deducted, literal window | five-year average -$2,165M: no positive value | not computable | n/a |

The all-spending series' own growth is meaningless over this window (it runs -12.7% a year 2022 to 2025 by end years,
-7.8% by halves, and +27% 2023 to 2025), because deliveries and prepayments bunch; it is shown, not carried. Working
capital (specific (d)) is inside the operating cash flow as filed; no single-contract draw was found.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED (facts under AFTER THE STOP).
## Q10 — IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional) — NOT REACHED.

---
## THE BOX
**OUT at Q2** (the standing castle that protects only ordinary returns: the customer buys on lease rate and delivery,
attackers with money and a lower cost of capital keep entering, no low-cost position on the record, and the field earns
about 4% to 5.5% before financing over 2014 to 2025, lifted to about 11% on equity by four to five times leverage);
**integrity facts recorded, not judged**. COMPUTATION, NOT A CLEARANCE: value range $236.88 to $336.73 a share at the
government rate against $147.33; no case earns the floor on the all-equity basis (6.62% and 7.75% at the price); fair
price $28.83 all-equity (central), $181.30 equity-only beside.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(written down as found **[M1997-127]**; no verdict; the box unchanged.)*
- **Q3 (capital).** The business needs about $5bn to $6bn a year of aircraft purchases and prepayments to stay where it
  is and grow a little (2023 to 2025 cash flows); purchase obligations $15.5bn 2026 to 2031 plus a July 2026 order for
  15 Boeing 787s (Q2 2026 release). The lease-asset base grew about 1.4% a year 2022 to 2025 while lease revenue grew
  4.1%: most of the growth was rate, not assets.
- **Q4 (the accounts).** The company features adjusted net income and adjusted EPS ($15.37 for 2025 against GAAP
  $21.30, compensation report; $5.14 adjusted against $4.59 GAAP for Q2 2026, release) and gives full-year adjusted EPS
  guidance, raised in July 2026 to "approximately $16.80, not including any additional gains on sale" (release,
  `0001628280-26-050456`). Adjusted figures exclude Russia recoveries and purchase-accounting items, so in 2025 the
  adjusted figure is below GAAP. Net income is swung by the Russia items: -$726M (2022), $3.1bn (2023), $3.8bn (2025).
  Operating cash flow excludes gains on sale and maintenance reserves by classification (Item 5). No confusion found in
  the statements read; the accounts were not judged.
- **Q5 (integrity-bearing, carried by the convention):** the guidance and the featured adjusted figure above; pay keyed
  to adjusted EPS ("The Committee focuses on clear quantitative performance metrics, particularly adjusted EPS",
  compensation report, `0000950157-26-000221`, ex. 99.3), with a 2026 target table from $13 to $20 of adjusted EPS
  setting payout factors of 0.5x to 2.0x; the CEO's long-term award is 52% adjusted EPS, 20% share-price target, 28%
  time-based; shareholders asked about "the quantum of our CEO’s total compensation opportunity" (same report; quoted
  as the filing's words, not a ledger row). A 2024 ransomware incident is disclosed (Item 3.D). The 20-F calls the
  company's ethics record "excellent". Not judged.
- **Q6 (money and owners).** Buybacks: 16.8M shares at an average $87.80 (2024), 22.1M at $109.92 (2025), 10.3M at
  $140.10 (H1 2026); $2.6bn in 2023 (Item 5; interim report). Against the COMPUTATION above, those prices sit below the
  bottom of the range at the government rate ($236.88) and above the all-equity fair price at the floor ($28.83), and
  below the equity-only fair price ($181.30); the Q6 test was not run. No programme states a price limit in the text
  read. GECAS was paid mainly in cash with 111.5M new shares (GE then held about 46%), so it is not an all-stock deal;
  the Q6 STOP was not tested. Dividends began in 2024 ($0.40 a quarter in 2026).
- **Q9 (debt and exposures).** Debt $43.8bn principal, 61% of total assets, interest paid $1.9bn (2025); 25% floating
  ($10.9bn); maturities $6.2bn (2026), $7.3bn (2027), $9.3bn (2028); $11.0bn undrawn, 1.8 times twelve months' needs;
  covenants include loan-to-value, interest-coverage and leverage ratios (Item 3.D, Item 5). Funding is wholesale. 45% of
  lease revenue from emerging-market airlines; aircraft repossession depends on foreign courts (Item 3.D). Russia: 2022
  charge $2.67bn; the war-risk cover "may be invalidated" by hostilities between major powers (Item 3.D). This is the
  "little or no debt" criterion's opposite **[R1997-001]**; not applied, as Q9 was not reached.
- **Q12.** Nothing found in the businesses the rows name.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after Step 0, Q1 and Q2, and once
      more for the COMPUTATION and the close together (write-early; those two went in one commit). The run tools and filings were fetched after the copy.
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's; the fold is the
      dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened. One filtered listing of `Test Runs/` file names for
      this ticker was run at the start and returned nothing; declared under Contamination above. Nothing else seen.
- [x] Every v5 id resolves (check script in the research folder, `check_ids.py`); every filing fact has its accession or
      its 20-F item; numbers carry a row, a filing, or a CONVENTION label.
- [x] The order was kept; Q2 closed the file OUT; everything after it is facts or COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, built from the cash-flow statements, never a net-income proxy (operator rule 5);
      the sovereign from the Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations; Q2's other side); facts for later questions under AFTER THE
      STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used (its share count superseded by the interim report, its
      owner-earnings lines unusable after 2013 and not used).
- [x] `python tools/check_framework.py` PASS before the final commit (recorded in the commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The financial-institution rows reach a lessor only by analogy.** Q1's bank door asks for a readable asset side
and "very cheap money on the deposit side" **[M2002-022]**; a lessor has the first and no deposits at all. I read the door as half open
and passed Q1 on the asset side, carrying the wholesale funding to Q9. The text does not say whether a lender without
deposits needs the cheap-money half; a sentence would settle it. (2) **Q7 has no rule for a lessor's maintenance
spending.** Depreciation as the proxy **[M1998-127]** misses the other consumption of lease capital (maintenance-rights
write-offs, finance-lease principal, impairments) and ignores gains on sale; I named the components as a CONVENTION and
checked them against an asset-base guess. (3) **Specific (e) and specific (b) collide** when the all-spending series
falls because deliveries bunch: (e) puts growth spending against growth, (b) carries a shown decline as the bottom. I
kept (e) central and showed (b) beside; the text does not say which governs. (4) **The serial-acquirer rule fires on one
transformational deal** (GECAS) because its test is mechanical; the organic pair it then requires needs "organic growth
as the filer reports it", which this filer does not report. I measured growth on the years after the deal and said so.
(5) **The government-rate range and the ten-percent floor point opposite ways for a leveraged, low-return asset base**:
the price is below the bottom of the range and no case earns the floor. The floor-first rule decides it, but the range's
figures invite a misreading; a sentence in Part VII saying that a range below the price is no sign of cheapness when the
floor fails would help the operator. (6) The template's Step 0 asks for "the latest 10-Q"; for a 20-F filer it is the
interim 6-K, and the cover tool's count is the 20-F's, superseded by the interim; I used the interim.
