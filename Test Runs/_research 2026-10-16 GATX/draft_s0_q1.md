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

