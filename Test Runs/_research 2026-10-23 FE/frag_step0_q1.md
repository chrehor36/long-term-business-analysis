## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $46.49 (close 2026-10-22, as printed by `tools/run.py`; an aggregator quote, live quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: **578,639,932** common, $0.10 par, as of June 30, 2026 (10-Q for the
  quarter ended 2026-06-30, filed 2026-07-28, accession `0001031296-26-000123`). `Screens/cover_shares.py FE` also printed
  13,628,447 shares: those are Jersey Central Power & Light's common, a co-registrant on the combined 10-Q, "all held by
  FirstEnergy Corp." (cover page); they are not added. Checked against the filed balance sheet of the same 10-Q: "578,639,932
  and 577,851,052 shares outstanding as of June 30, 2026, and December 31, 2025"; FE shows no treasury line (shares under the
  ICP 2020 "are issued from authorized but unissued common stock", FY2025 10-K Note 5). No 8-K or prospectus after the 10-Q
  changes the count (the EDGAR submissions list, fetched today, shows no filing after 2026-07-28).
- **Market cap:** 578.64M x $46.49 = **$26,901M**.
- **Sovereign for the earnings currency (USD):** **5.29%**, 30-year par yield, US Treasury daily par yield curve, 10/22/2026
  (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for FY2025 (filed 2026-02-18, `0001031296-26-000046`): Items 1, 1A, 7, the
  statements of Item 8, Notes 5 (stock-based pay), 13 (regulatory matters), 14 (contingencies) and 15 (segments); 10-Q for the
  quarter ended 2026-06-30 (filed 2026-07-28, `0001031296-26-000123`); proxy DEF 14A (filed 2026-04-01,
  `0001193125-26-138029`); 8-K of 2026-07-28 with its Ex. 99.1 news release (`0001031296-26-000122`); 8-K of 2026-02-12
  (`0001031296-26-000020`, a director not standing again); for the window and the history, the 10-Ks for FY2024
  (`0001031296-25-000006`), FY2023 (`0001031296-24-000008`), FY2021 (`0001031296-22-000013`), FY2020
  (`0001031296-21-000020`) and FY2019 (`0001031296-20-000008`). **Cross-checked against the filed statement:** net cash
  provided from operating activities 2025 = $3,700M in `tools/run.py` (XBRL) and $3,700M on the filed FY2025 cash-flow
  statement; total assets 2025-12-31 = $55,904M in both.
- `python tools/run.py FE`, arithmetic lines only (output in `Test Runs/_research 2026-10-23 FE/run_py_output.txt`): OCF
  1,387 / 2,891 / 3,700 (2023-2025); capital investments 3,356 / 4,030 / 4,705; three-year mean of OCF less capex -1,371,
  of OCF less D&A 1,091; the five-year window -791 and 1,145. Read against the filing: (a) stock pay is "n/f" in XBRL; the
  filing gives it (Note 5: total stock-based costs $85M / $86M / $83M for 2025 / 2024 / 2023, of which $39M / $43M / $44M
  expensed net of capitalization) and the equity statements give the stock actually issued under the plans, $50M / $98M /
  $89M / $74M / $60M for 2021-2025, which this run deducts; (b) `run.py`'s capex omits "Asset removal costs" ($226M / $213M /
  $274M / $305M / $376M for 2021-2025), a separate investing line, which this run counts as capital spending; (c) the
  depreciation `run.py` prints for 2023-2025 (1,461 / 1,581 / 1,664) is the segment note's "Depreciation", not the
  cash-flow statement's "Depreciation and amortization" (1,255 / 1,446 / 1,607); (d) finance-lease principal is $2M to $8M a
  year, immaterial. Owner cash is built at Q7 from the filed statements (`q7.py` in the research folder).
- **Lines of evidence chosen, from Items 1, 1A and 7, and why.** (1) *The regulated return and the regulatory climate*:
  Item 1 shows every price and return set by six state commissions and FERC (the allowed-ROE table), and Item 1A's second
  group of risks is state and federal rate regulation; this decides Q2 and Q3. (2) *HB 6 and what followed*: the first risk
  factor of Item 1A and a long section of Item 7 (the DPA, the SEC order, the PUCO audits, the securities class action, the
  indictment of two former officers); this decides Q5 and bears on Q9. (3) *The capital program and how it is paid for*:
  Item 7 (Energize365, $36 billion for 2026 to 2030, "expected to be funded with a combination of organic cash flows, the
  issuance of debt, including hybrid securities, and the issuance of common equity"); this bears on Q3, Q6 and Q7. (4) *The
  debt*, including "approximately $6.8 billion of external FE holding company debt" (Item 1) and the 2.50 times
  interest-coverage covenant (10-Q); Q9. (5) *The transmission part and its minority owner*: Item 1 records that Brookfield
  owns 49.9% of FET; Q2's parts, Q6 and Q7.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what six million customers' wires and the transmission grid will
pay their owners, not where the quotation goes. No macro forecast enters **[M2004-102]**: data-centre demand, PJM capacity
prices and interest rates appear in the filing and are read only as properties of this business. The market serves and
does not instruct **[M2006-077]**; the earnings releases feature "Core Earnings (non-GAAP)" and a growth target of "6% to
8%", and projections are not used **[M1995-050]**. Margin of safety **[M1996-084]**: if the case needs a pencil it is too
close. **Contrary evidence, written down as found** **[M1997-127]**: (i) the company itself, by its DPA, agreed to the
filing of a criminal information charging it with one count of conspiracy to commit honest services wire fraud and paid a
$230M penalty (FY2025 10-K, Item 7); (ii) in the five years 2021-2025 the business spent more on its assets than its
operations produced plus the long-term debt it raised, and sold 49.9% of its transmission holding company and $1B of common
stock to cover the gap (cash-flow statements, FY2023 and FY2025 10-Ks); (iii) earnings attributable to FE were $1,283M in
2021 and $1,020M in 2025 after $17.4B of capital investments over the five years (same); (iv) the PUCO cut the Ohio
companies' ROE to 9.63% and a $352M impairment for disallowances was recorded in 2025 (Item 7); (v) of the securities class
action, "FE believes that it is probable that it will incur a loss", the amount not estimable (10-Q,
`0001031296-26-000123`).

## THE STANDING RULE
A part-interest bought for cash with no borrowing, and sized so that its loss cannot touch what the buyer has and needs, does
not risk ruin; the buyer's conduct is the rule's subject **[L2014-024]**, and the target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**. FE is a regulated wires
  business: distribution in six states, high-voltage transmission in PJM, and 3,610 MW of regulated generation in West
  Virginia (FY2025 10-K, Item 1). Its earnings are a regulated return on a rate base ("a total rate base of approximately
  $21.3 billion" for the electric companies, plus $5.4 billion FirstEnergy-owned in Stand-Alone Transmission, Item 1).
  **The key variables** **[M1998-044]**: the size of the rate base, the allowed return and capital structure each
  commission grants, how fast and how fully costs are recovered, and customer demand. Each is on the public record (the
  allowed-ROE table of Item 1; the rate-case record of Item 7). They are not a technology forecast: the load forecast is
  about customers **[M2017-019]**, and the commissions' orders are filed.
- **Important and knowable** **[M2006-076]**; **would the insiders write it down** **[M2000-105]**? The regulators do write
  it down: each rate order states the return and the capital structure (the PUCO's order of 2025-11-19, "a return on equity
  of 9.63% and a hypothetical capital structure of 48.8% debt and 51.2% equity", Item 7). What is not knowable is the
  regulatory mood ten years out; that is a question about the castle and is carried to Q2.
- Routing: not a fast-changing industry; not a bank; FE is a holding company read by its parts, all three of which are
  regulated electric utilities of the same kind (Q2's parts table).
- **VERDICT: IN.** The economics can be pictured from the figures **[M2008-069]**, and the first question **[M1995-051]** is
  passed: a cost-of-service utility whose ten-year earning power is a rate base times an allowed return, both on file.
