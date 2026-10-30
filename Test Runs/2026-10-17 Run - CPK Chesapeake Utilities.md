# Company Run — Chesapeake Utilities Corporation (NYSE: CPK) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (fccb3177): `PORTFOLIO.md` read for this one ticker; the operator does not hold CPK (no line names CPK or Chesapeake).*

**Dispatched run.** Done by a dispatched analyst under the canonical brief (`Screens/_daily/_dispatch_brief.md`), with the
one departure the brief states: the lines of evidence and the competitor slot are derived by the analyst from the 10-K's
Items 1, 1A and 7, not written by the dispatcher. Research folder: `Test Runs/_research 2026-10-17 CPK/` (notes, the
fetch and arithmetic scripts, `calc.py` and its output `calc_output.txt`, the ledger rows read, `run_py_output.txt`; the
raw filings sit in its gitignored `cache/`).

**Contamination, declared.** Before any work the session context showed: commit subjects about another company's run
(CPYYY, Centrica plc, closed OUT at Q2 on 2026-10-17); file names of two other research folders in the git status (AYI
2026-09-26, ARCB 2026-09-27); the memory index lines (generic queue state, nothing on this name). One command printed a
count of the files in `Test Runs/` (a number only, no names). Nothing about Chesapeake Utilities or CPK under any name was
seen. None of it is used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $132.18 (close 2026-10-16, printed by `tools/run.py`; aggregator, live quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock par $0.4867; 24,106,455 shares outstanding as
  of August 3, 2026 (10-Q for the quarter ended 2026-06-30, filed 2026-08-06, accession `0001628280-26-054477`;
  `python Screens/cover_shares.py CPK` prints the same count). Preferred stock authorized, none issued (10-K balance
  sheet). Check against issued less treasury: the 10-K equity statement carries treasury stock only as the Rabbi Trust
  deferred-compensation shares, equal and opposite to the deferred-compensation obligation ($12.6M each, 2025), so the
  cover count is the count. After the 10-Q: the 8-K of 2026-10-01 (`0001193125-26-409820`) and its prospectus supplement
  (424B5, `0001193125-26-409381`) open an at-the-market program of up to $225,000,000 including forward sales; no sale
  under it is filed, so no shares are added. The ATM is noted at Q6 and Q9.
- **Market cap:** $3,186.4M (132.18 x 24.106455M).
- **Sovereign for the earnings currency (USD):** 5.43%, US Treasury daily par yield curve, 30-year, 10/16/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-25, `0001628280-26-011753` (Items 1, 1A, 2, 5, 7, 8 and
  notes 4, 7, 12, 17); 10-K FY2024 `0001628280-25-008213`, FY2023 `0001628280-24-005944`, FY2022 `0001628280-23-004607`
  (statements for 2020 to 2022, segment operating income); 10-Q for 2026-06-30 `0001628280-26-054477`; proxy (DEF 14A)
  filed 2026-03-25 `0001628280-26-020945`; 8-Ks of 2026-07-13 (`0001628280-26-047964`, Florida Energy Pathway announced),
  2026-08-06 (`0001628280-26-054425`, results), 2026-09-01 (`0001193125-26-377589`, the 49% sale to NextEra's subsidiary
  and the LLC agreement), 2026-09-29 (`0001628280-26-063759`, officer designations), 2026-10-01 (`0001193125-26-409820`,
  the ATM).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities, 2025, $233.7M on
  the filed Consolidated Statements of Cash Flows (10-K FY2025) equals the tagged figure `tools/run.py` prints (233.7);
  2022, $158,882 thousand on the FY2022 filed statement equals the tagged 158.9.
- `python tools/run.py CPK` arithmetic lines only (`run_py_output.txt`): OCF 203.5 / 239.4 / 233.7 for 2023 to 2025; SBC
  7.6 / 8.4 / 8.5; capex 188.6 / 355.3 / 448.6; D&A 65.5 / 65.7 / 91.7; owner cash on all capex 7.3 / -124.3 / -223.4,
  mean -113.5; on D&A 130.4 / 165.3 / 133.5. Checked against the filed statements: all match. **Two things the tool does
  not see, read in the filing:** the cash-flow statement carries a second depreciation line, "Depreciation and accretion
  included in operations expenses" (11.9 / 15.8 / 15.9 for 2023 to 2025; 10.2 and 11.0 for 2021 and 2022), so the true
  depreciation is larger than the D&A line; and 2024's D&A is understated by $15.5M of FCG's reserve surplus amortization
  mechanism ("RSAM"), a regulator-approved credit to depreciation that was "completely utilized by December 31, 2024"
  (10-K FY2025, glossary and MD&A note 2). The tool's "debt on the face" column d3 is `CapitalizationLongtermDebtAndEquity`,
  which includes equity; it is not debt and is not used. SBC resolved: the only other stock-pay line (0.3 in 2023) is
  immaterial; the SBC column is complete. The five-year window used below, 2021 to 2025, is built in `calc.py` from the
  filed statements.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the margin of safety: a regulated utility's value is close to arithmetic, so the
question is whether the price leaves "this huge margin of safety" without pencil and paper **[M1996-084]**. The share is
read as a business whose cash comes from what its pipes and wires earn under its regulators, not from what the next buyer
pays **[M1997-109]**; the market's price for it carries no instruction **[M2006-077]**; no forecast of gas prices, rates or
policy enters as macro **[M2000-094]**, though the regulators' decisions enter as facts of the business. Who is paid to tell
you: the company's own proxy pays its officers half their long-term award on capital spending as a share of capitalization
(Q6), and the company has just opened an equity program sold through six banks (8-K 2026-10-01); both are read as
incentives to grow the base, not as evidence of value. **Contrary evidence, written down as found** **[M1997-127]**:
(1) all-capex owner cash is negative in three of five years and its five-year mean is negative; the business has been
funded by $623M of stock sold for cash (2020, 2023, 2024, 2025), dividend-reinvestment issuance besides, and rising debt; (2) Florida City Gas, bought for $922.8M in cash in
November 2023, earned net income of $5.2M on $1,133.7M of assets in 2025 (10-K FY2025, Item 1 table); (3) the officers'
long-term pay rewards capital spending relative to peers, and the 2023 to 2025 award paid the maximum on it, with ROE
measured "excluding Florida City Gas" (proxy); (4) return on capital employed fell from 6.3% (2021) to 6.0% (2025) while
capital doubled (`calc_output.txt`).

## THE STANDING RULE
The buyer's own conduct: a part-interest bought with the buyer's own money, unlevered, puts nothing the buyer has and needs
at risk for what he does not need **[M2012-081]**. No collateral, no short maturities on the buyer's side **[L2014-024]**. The
rule is met if the purchase is so financed; the target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, "a reasonable probability of being able to asses where the business will be in 10
  years" **[M2000-037]**.
- **The parts, by five-year operating income** (segment operating income, 2021 to 2025, from the 10-Ks FY2022 and FY2025):
  Regulated Energy 106.2 / 115.3 / 126.2 / 196.2 / 222.0, total $765.9M, 84% of the two segments' $907.4M; Unregulated
  Energy 24.4 / 27.4 / 24.4 / 31.7 / 33.6, total $141.5M, 16%. Regulated Energy decides (more than half), so Q1 is asked of
  it by the parts paragraph (Q1, A holding company; Q2, A business of parts).
- **The key variables, and how predictable they are** **[M1998-044]**. Regulated Energy earns "on the delivery of natural
  gas or electricity to customers", with gas and power costs passed through "under PSC-approved fuel cost recovery
  mechanisms" (10-K Item 1). Its earning power is therefore (i) the rate base, (ii) the return each commission allows on it
  and the lag in getting it, and (iii) customer and volume growth in its territories. The 10-K states each: rate bases of
  $453.7M (FPU gas) and $487.3M (FCG); allowed after-tax ROE 9.60% Delaware, 10.25% FPU gas, 9.50% FCG, 10.20% FPU
  electric, 6.88% allowed rate of return in Maryland; capital structures in rates with 45% to 53% equity; infrastructure
  riders (GUARD, SAFE, Delaware and Maryland surcharges, the electric Storm Protection Plan) that recover replacement capital
  between rate cases. The transmission arm (Eastern Shore under FERC; Peninsula Pipeline not cost-of-service regulated but
  95% of its revenue from the affiliated Florida distributors, recovered through their fuel clauses) earns on firm contracts
  of stated term (2026 to 2048). These are variables a filing reports and a commission decides in public; the industry's own
  insiders write them down: the company states a five-year capital plan through 2028 and projected-test-year rate cases
  **[M2000-105]**, test 5 passed.
- **Do the past statements tell me the future ones?** **[M2008-033]** Largely yes for the regulated part: revenue follows
  rate base and allowed return, and the statements show both. Two items blur it and are carried, not hidden: the FCG
  acquisition (2023) changes the base inside the window; and the RSAM credit flattered 2024.
- **The forecast is about regulators and customers, not technology.** No fast-moving technology governs a gas main. The
  ten-year question that is hard is policy (decarbonisation rules, "Federal, state and local legislative initiatives ...
  may change the demand for natural gas", Item 1A) and the regulatory compact; Q2 owns whether that castle stands.
- **Doubt test** **[M2002-092]**: the regulated part is a franchise utility whose two sides (rate base and allowed
  return) can be read from its filings; I have no doubt it is inside the perimeter. The unregulated part (propane,
  Aspire's Ohio gathering and supply, Marlin's mobile CNG, Eight Flags CHP, RNG projects) does not decide; it is carried
  to Q7 as an ordinary business.
- **VERDICT: IN.** The deciding part's economics, rate base times allowed return less lag, are knowable from the filings
  and written down by the insiders **[M2012-065]**, **[M1998-044]**, **[M2000-105]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The lines of evidence, chosen by the analyst from the 10-K FY2025** (Item 1, business and segments; Item 1A, risks;
Item 7, MD&A; the brief's one departure): (1) the franchise and the absence of a direct rival for homes and businesses
(Item 1, Competition; Item 1A, franchise agreements); (2) rates set by the commissions and FERC, and what the recent rate
cases asked and got (Item 1, Regulatory Overview; Note 17); (3) bypass and fuel switching by large customers (Item 1,
Competition); (4) the transmission arm's rivals and its affiliate dependence (Item 1, transmission tables); (5) policy
against gas and the climate risks (Item 1A); (6) customer and volume growth and the major projects table (Item 7); (7)
FCG's earnings since purchase (Item 1 table; Item 7). Chosen there because those three items are where the filer itself
describes how it earns, what it fears and what moved.

**The parts table** (segment operating income, 2021 to 2025, 10-Ks FY2022 `0001628280-23-004607` and FY2025
`0001628280-26-011753`; Q2, A business of parts, CONVENTION adopted 2026-10-06):

| part | five-year operating income | share | castle | decides |
|---|---|---|---|---|
| Regulated Energy (gas distribution DE, MD, FL incl. FCG; Eastern Shore and Peninsula transmission; FPU electric) | $765.9M | 84% | franchise utility at regulated returns (below) | **yes** (more than half) |
| Unregulated Energy (propane; Aspire Ohio supply and gathering; Marlin mobile CNG/LNG/RNG; Eight Flags CHP; RNG projects) | $141.5M | 16% | propane sold "primarily on the basis of price and service" against "national and local independent companies" (Item 1): a price-taking field | no; carried to Q7 at no growth |

**The castle tests, on Regulated Energy, each with its filing fact.**
- *The attacker with money* **[M2011-015]**. "our natural gas distribution operations do not compete directly with other
  distributors of natural gas for residential and commercial customers in our service areas"; the same for electric
  (Item 1). The distribution operations "hold franchises in each of the incorporated municipalities" (Item 1A). A
  hundred-million-dollar attacker cannot lay a second main where the franchise and the commission forbid it. The breach
  the filer names is at the edge: "Large customers could bypass our natural gas distribution systems and connect directly
  to intrastate or interstate transmission pipelines", met by negotiated rates (Item 1).
- *Pricing power and the agony before a rise* **[M2005-020]**. The business does not set its price; the commission does,
  in public, after a case. The recent cases show the agony as a procedure: Delaware asked $12.1M at an 11.5% ROE and
  settled at $6.1M; Maryland asked $6.9M at 11.5% and got $3.5M in two phases at an allowed 6.88% rate of return; FPU
  electric asked $12.6M at 11.3% and settled at $8.6M; FCG (2022 case) got $14.1M incremental at 9.50% and the Florida OPC
  appealed it to the state Supreme Court, which ruled against the OPC "on all contested matters" in June 2026 (10-K Item 1
  and Note 17; 10-Q `0001628280-26-054477`, Note on rates). FCG's new case asks $46.9M at 11.25%; $16.2M interim rates are
  in effect, subject to refund. Every increase was granted, each below what was asked. That is a regulated return, not
  pricing power: "The whole idea behind the utility industry is not to allow extraordinary profits." **[M2000-131]**.
- *The low-cost position and the customer's choice*. "Natural gas historically has maintained a price advantage in the
  residential, commercial and industrial markets" against electricity, oil and propane (Item 1). The customer does not
  pick the distributor; he picks the fuel, and gas has been the cheaper one on the filer's own statement.
- *Transmission*. Eastern Shore "competes with other interstate and intrastate pipeline companies" (Item 1); 44% of its
  revenue and 52% of its firm capacity are the affiliated Delmarva distributor. Peninsula Pipeline sells 95% of its revenue
  and 99% of its capacity to the affiliated Florida distributors and is "not regulated with regard to cost of service"
  (Item 1). Its earnings ride on the affiliates' fuel clauses, which their commission approves. The rows warn of the
  pipeline "vulnerable to competitive price pressures because of alternate ways of getting gas to market through other
  pipelines" against the one that "will remain the low-cost producer" **[M2003-075]**; no filing read shows which of the two
  Peninsula is outside its affiliate contracts.
- *Widening or narrowing* **[M1999-108]**. For the moat: average customers grew in both distribution systems (the
  projects table credits "Natural gas growth (excluding service expansions)" with $7.4M of margin in 2025, Item 7), firm
  transportation commitments of about 250,000 Dts/d from "multiple investment-grade shippers" back the $1.2B Florida
  Energy Pathway, and NextEra's subsidiary bought 49% of it (10-Q; 8-K 2026-09-01). Against: FCG, bought for $922.8M,
  earned net income of $5.2M on $1,133.7M of assets in 2025 once the RSAM credit had run out (Item 1 table), and needs the
  pending rate case to earn its allowed return.
- *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**. The filer names it: legislation
  "to implement renewable portfolio standards or to further subsidize the cost of solar, wind and other renewable power
  sources may change the demand for natural gas"; climate rules that "could reduce demand for our energy delivery
  services"; the regulators: "there can be no assurance that our regulated operations will be able to obtain such
  approvals or maintain currently authorized rates of return" (Item 1A). The rows' warning is direct: in some states "it is
  difficult to project both earnings and asset values in what was once regarded as among the most stable industries in
  America" **[L2023-011]**. The filings read show no such development in Delaware, Maryland or Florida: every case since
  2022 closed with an increase and the one appeal failed. The re-founding test **[L2006-008]** runs the other way here:
  gas pipe is still being newly built in the territory, with outside capital (NextEra) and shippers' firm commitments.

**The competitor row.** The 10-K names no rival by name: its rivals are "other natural gas suppliers and alternative fuel
providers", "other interstate and intrastate pipeline companies" and, for propane, "national and local independent
companies" (Item 1). **CONVENTION of this run:** three SEC filers chosen from the company's own performance peer group in
its proxy (DEF 14A `0001628280-26-020945`: Atmos, Black Hills, New Jersey Resources, NiSource, Northwest Natural, NorthWestern,
ONE Gas, RGC Resources, Spire, Unitil); rationale: a franchise has no rival in its territory, so the comparison is of the
field's returns, and the filer's own chosen peers are the least invented set; ONE Gas (pure gas distribution), Northwest
Natural (gas distribution of similar size) and Unitil (small gas and electric distributor) are the nearest in kind. Same
metrics, from each filer's own 10-K data (`peers.py`, `peers_output.txt`; latest 10-Ks: ONE Gas `0001587732-26-000009`,
Northwest Natural Holding `0001733998-26-000012`, Unitil `0001193125-26-042983`; XBRL transcription, flagged), 2021 to 2025:

| filer | ROE on average equity, 2021 / 22 / 23 / 24 / 25 | 5-yr avg | operating cash less capex, 5-yr sum | capex / OCF | equity 2025 over 2020 |
|---|---|---|---|---|---|
| CPK | 11.3 / 11.2 / 8.4 / 9.0 / 9.4 | 9.9% | -$321.8M | 1.33 | 2.29x |
| ONE Gas | 9.0 / 9.0 / 8.6 / 7.6 / 8.1 | 8.5% | -$1,259.8M (Winter Storm Uri swings in 2021 to 2022) | 1.66 | 1.54x |
| Northwest Natural | 8.6 / 8.2 / 7.6 / 5.9 / 7.9 | 7.7% | -$763.8M | 1.72 | 1.66x |
| Unitil | 8.6 / 9.0 / 9.4 / 9.4 / 8.9 | 9.1% | -$163.4M | 1.29 | 1.57x |

**The field's returns over the last full cycle, judged in words.** The whole field earns returns on book equity close to
what the commissions allow, high single digits, and every member spends more than its operating cash on plant, year
after year, and raises new equity to do it. CPK earned above its peers until it bought FCG (11%+ in 2021 and 2022) and has
earned at the field's level since (8.4% to 9.4%). These are ordinary returns, protected by a durable castle. The framework
sends exactly this case away from OUT: "A return set by a regulator is the exception, carried to Q3 as a second best"
(Q2, What it rules OUT), on the rows "there’s no way we get rich on our utility investments. But there’s no way we get
poor, either." **[M2009-104]** and the 2009 letter's willingness to own such businesses on "decent returns on the incremental
sums they invest" **[L2009-012]**. The allowed return is close to certain only "if you behave yourself" **[M2010-037]**.

**Is the castle open on the evidence, or is its future beyond judgment?** Neither, on the filings read. The franchise
stands, no rival can enter, the commissions have granted every case at returns near 9.5% to 10.25% on equity, and the
largest regulatory doubt in the window (the OPC appeal of FCG's order) was decided for the company. The threat that could
end it, policy against gas, is named by the filer but not shown in its states. A castle "tenuous in any way" would go to
TOO HARD **[M2000-019]**; this one is not shown tenuous, and the regulated-return exception carries its ordinary returns to
Q3. The non-deciding unregulated part, a price-taking propane and services business, is carried to Q7 at no growth.

- **VERDICT: IN** (Regulated Energy decides; the castle is a franchise at regulated returns, carried to Q3 as a second
  best) **[M2009-104]**, **[L2009-012]**, **[M2000-131]**. The policy and regulatory threat is written down here and
  carried, not judged away **[M1997-127]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
All figures from `calc.py` on the filed statements (`calc_output.txt`); "NOPAT" below is operating income plus other
income, after the year's effective tax rate, before interest: the "operating earnings after depreciation" by which the
rows say a utility's return is measured **[M2014-086]**.
- **Return on the capital actually needed** **[M2010-090]**. Capital employed (equity plus debt less cash) was $1,559.0M at
  2021 year-end and $3,216.4M at 2025 year-end. NOPAT $98.4M (2021) and $193.0M (2025). Return on capital employed: 6.3%
  (2021), 6.0% (2025). On tangible capital (goodwill and intangibles of $520.7M taken out, as the rows ask when judging the
  business **[M2011-060]**) 2025 is about 7.2%. On book equity: 11.3% and 11.2% (2021, 2022), 8.4%, 9.0%, 9.4% (2023 to
  2025), five-year average 9.9%.
- **What the added capital earned.** From 2021 to 2025 NOPAT rose $94.6M on $1,657.4M of added capital employed: **5.7%
  after tax**, with what was paid for FCG counted, as the rows require when judging the allocation, "because we paid for
  it" **[M2011-060]**; 7.9% with the goodwill added in the window taken out. Set beside the long government rate of 5.43%,
  the added capital, purchase price included, has earned about the bond rate. The regulated rate base itself earns the
  allowed return, roughly 6.8% after tax on capital at the filed allowed equity returns and debt costs (Q7 builds this
  figure and confesses it).
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**. The filing does not split maintenance from
  growth spending; the maintenance guess used is total depreciation (the D&A line plus the depreciation charged inside
  operations expenses, with 2024's RSAM credit added back): $72.9M (2021) rising to $107.6M (2025), the proxy the rows allow
  **[M1998-127]**. Capital spending ran far above it: $186.9M, $128.3M, $188.6M, $355.3M, $448.6M (2021 to 2025), plus
  $922.8M for FCG in 2023; growth spending above the maintenance guess averaged $174.6M a year. The plan is larger:
  $450M to $500M for 2026 in the 10-K, raised to $550M to $600M in the 10-Q, $1.5B to $1.8B for the five years to 2028, and
  CPK's 51% of the $1.2B Florida Energy Pathway for service in 2030. Capital spending was 1.33 times operating cash over the
  window; the gap was filled with $623M of stock sold for cash and with debt.
- **The growth arithmetic.** This is the capital-heavy kind of business the rows admit as "the second-best choice, still a
  good choice" **[M2018-055]**, on condition that the added sums earn "a reasonable return" **[M2012-057]**. The rows add
  that inflation sharpens the cost: "To earn more, their owners must invest more." **[L2011-019]**. Here the incremental
  return, with the acquisition counted, is 5.7%, close to the bond rate and well under the 10% floor Q7 applies; without
  the acquisition premium it is 7.9%, decent for a regulated rate base. The growth is "a very satisfactory rate" **[M1998-081]**
  only on the second reading.
- **WEIGHS AGAINST.** The rate base earns a second-best regulated return, but the capital added over the window,
  including the $922.8M paid for FCG, has earned about the long government rate (5.7% against 5.43%), and the business
  must keep adding capital faster than it generates cash to grow at all **[M2012-057]**, **[L2011-019]**, **[M2011-060]**.
  (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten year-ends, before the income account** **[M2025-032]** (USD millions; first-filed XBRL as
printed by `tools/run.py` with the debt lines from the same tags, read against the filed FY2025 and FY2022 balance
sheets; accessions in `run_py_output.txt`):

| year-end | total assets | equity | goodwill + intangibles | retained earnings | debt (LT + current + short-term) | cash | receivables |
|---|---|---|---|---|---|---|---|
| 2016 | 1,229 | 446 | 17 | 192 | 359 | 4 | 63 |
| 2017 | 1,417 | 486 | 27 | 229 | 458 | 6 | 77 |
| 2018 | 1,694 | 518 | 32 | 262 | 622 | 6 | 85 |
| 2019 | 1,783 | 562 | 41 | 301 | 733 | 7 | 50 |
| 2020 | 1,932 | 697 | 47 | 343 | 698 | 3 | 57 |
| 2021 | 2,115 | 774 | 58 | 393 | 789 | 5 | 58 |
| 2022 | 2,215 | 833 | 64 | 446 | 802 | 6 | 63 |
| 2023 | 3,305 | 1,246 | 525 | 489 | 1,385 | 5 | 72 |
| 2024 | 3,577 | 1,390 | 523 | 550 | 1,484 | 8 | 77 |
| 2025 | 3,995 | 1,598 | 521 | 627 | 1,620 | 2 | 102 |

What the figures say: assets more than tripled; equity rose $1,152M, of which retained earnings supplied $435M and new
stock about $717M; goodwill jumped from $46M to $508M in 2023 with FCG, so a third of today's equity is purchase premium
and tangible equity is about $1,078M; debt rose from $359M to $1,620M (and $1,688M at 2026-06-30, 10-Q), roughly in step
with equity, the equity share of capitalization including short-term debt held near 50% against a stated target of 50% to
60% (10-Q). Cash never exceeds $8M: the business runs on its revolver ($238.1M drawn at 2026-06-30). Receivables and
accrued revenue against sales: 14.5% (2024) to 16.3% (2025), a rise in a year when revenue grew 18%; no
build of prepaid or deferred accounts out of line **[M1995-064]** (prepaids $19.7M against $17.3M; regulatory assets $104.0M
against $101.3M). What they do not say: how much of the spending maintains and how much grows (no split filed), and what
FCG earns on what was paid for it beyond the one Item 1 line (net income $5.2M, 2025).

**The real costs.**
- *Depreciation* is real and split across two lines: "Depreciation and amortization" ($91.7M, 2025) and "Depreciation and
  accretion included in operations expenses" ($15.9M); both are charged here **[L2015-004]**. 2024's D&A was lowered by
  $15.5M of FCG's RSAM, a regulator-approved reserve credit used up at 2024 year-end: a real but non-repeating flattering
  of 2024 earnings; it is added back to the maintenance guess.
- *Stock pay* $8.5M (2025) is deducted from owner cash in every year **[L2021-003]**.
- *Restructuring and "one-time" items:* FCG transaction and transition costs of $10.4M, $4.0M, $1.2M (2023 to 2025) are
  real costs of the deal and stay in.
- *EBITDA in the filer's mouth:* none found. The filer features two non-GAAP figures: "Adjusted Gross Margin", which is
  computed before depreciation and before part of operations expense and is the measure of its segment discussion, and
  "Adjusted Net Income" and "Adjusted EPS", which add back the FCG transition costs (2025: $0.04 a share). Both are
  reconciled to GAAP in the 10-K.
- *The recast earnings for Q7* (all-equity, after the company's tax, before interest; `calc_output.txt`): owner cash after
  maintenance only 87.1 / 90.2 / 141.6 / 187.5 / 170.8 (2021 to 2025), five-year average $135.4M; after all capital
  spending -26.9 / 41.9 / 30.4 / -70.8 / -170.2, average -$39.1M; equity basis (after interest) maintenance-only average
  $102.9M. Never a net-income proxy (operator rule 5).

**The habits, recorded as a weighing and carried to Q5** (section A of the gaps case): the company issues EPS guidance
("The Company continues to affirm our 2028 EPS guidance range, which implies an annual EPS growth rate of approximately 8%",
proxy) and capital guidance ("$1.5 billion to $1.8 billion" through 2028, 10-K), sets its officers' cash bonus on "a band
centered around an EPS target of $5.92 per share" aligned with "the respective low end and high end of externally reported
guidance figures" (proxy), and features Adjusted EPS beside GAAP (10-K Item 7, proxy). Each is a "negative" short of a
"total exclusionary factor" **[M1994-018]**; the adjusted figure, small and reconciled, is still the kind the rows name as
making them "nervous" **[L2016-006]**.

- **VERDICT on the accounts: WEIGHS AGAINST, no STOP.** The accounts are not confusing: the two depreciation lines, the
  RSAM credit and the adjustments are each disclosed and reconciled, and no tell of suspicion was found in the statements
  **[M1995-064]**, **[M1995-063]**. They weigh against because the earning power the statements show is reached only after
  heavy capital spending they do not split, 2024 was flattered by a non-repeating regulatory credit, and the guidance and
  adjusted-EPS habits are present **[M1994-018]**, **[L2016-006]**. The recast earnings above feed Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a stock bought in the market the yardsticks and the reading tests carry the weight **[M1994-008]**.
- **The people.** Jeffry M. Householder, President and CEO since January 2019, Chair since May 2023; owns 73,237 shares
  (about $9.7M at the price) against 2025 total pay of $4,531,322; directors and officers as a group 1.36% (proxy). CFO
  Beth Cooper retired June 30, 2026 after 36 years; Jeffrey Sylvester, COO since 2022, CFO from July 1, 2026; Michael
  Galtman, Chief Accounting Officer 2019 to April 2026, principal accounting officer from September 2026 (8-Ks
  `0001628280-26-020829`, `0001628280-26-063759`). An orderly internal succession.
- **The first yardstick, the business against the hand dealt** **[M1994-008]**. The operations record is good: every rate
  case since 2022 closed with an increase, the FCG order survived the Supreme Court appeal, segment operating income rose
  from $131.1M (2021) to $255.9M (2025), and a $1.2B pipeline was signed up with firm shippers and a 49% partner. The
  capital record is the weak half (Q3, Q6): the largest decision of the window, FCG, earned $5.2M net in 2025.
- **The proxy** **[M1994-009]**. How they treat themselves: base pay near the peer median (FW Cook); half the long-term
  award paid on capital spending as a share of capitalization against peers, which paid the 200% maximum for 2023 to 2025;
  ROE for the same award "excluding Florida City Gas" (11.31%); a discretionary cash bonus in February 2024 for the FCG
  acquisition ($150,000 to the CEO). All of it is disclosed in plain words; the design is weighed at Q6, Part B.
- **The habits carried from Q4.** EPS guidance to 2028, capital guidance, a cash bonus keyed to the guidance band, Adjusted
  EPS beside GAAP. Read with the rest of the record: the rows are suspicious of managers who "consistently reach their
  declared targets" **[L2002-041]** and name "the scourge of earnings "guidance"" **[L2019-006]**. What the record shows: the
  adjustment is one disclosed item (FCG transition costs, $0.04 a share in 2025) and runs down as the integration ends; the
  a search of the 10-K text for "material weakness" and "restat" found neither reported; the 2025 bonus applied an EPS multiplier of 122%, the result landing inside the
  band. The proxy describes 2025 as "in line with our expectations, after adjusting for the Florida City Gas depreciation
  study outcome", which narrates a regulator's adverse ruling away rather than naming it as a miss; and it celebrates
  capital spending "exceeding the high end of the 2025 capital guidance range by $20 million" as an achievement.
- **How they talk about mistakes** **[L2024-003]**: no statement found, in the 10-K or the proxy, that FCG has earned less
  than was paid for it; the filings describe it through rate cases and integration costs. The reports are otherwise clear
  and tell an owner what he would want to know (rate bases, allowed returns, each rate case asked and granted, the RSAM
  mechanism, the second depreciation line) **[M1998-036]**; no figure that matters was found hidden or "touched on [...] in
  a dishonest manner" **[M2007-082]**.
- **VERDICT on integrity: IN.** The doubt rule **[M2013-088]** was applied to the habits and found no tell of dishonesty in
  the accounts or the reports: the habits are public, small and reconciled, which the rows treat as a weighing against,
  not a finding of character **[M2004-067]**. **Ability: WEIGHS FOR on running the business, AGAINST on the allocation of
  capital**, which Q6 judges **[M1994-008]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- *The retention test* **[R1995-009]**, **[M1998-110]**. Over 2021 to 2025 the company earned $519.4M and paid $221.5M in
  dividends, retaining $297.9M, and on top of it sold $623M of stock for cash and roughly doubled its debt; all of it went
  into plant and FCG. Market leg: the 10-K's own performance graph shows $100 invested at the end of 2020 worth $127 at the
  end of 2025 with dividends reinvested, against $183 for its industry index and $196 for the S&P 500 (10-K Item 5).
  Intrinsic leg: the return on the capital added was 5.7% after tax (Q3). Forward: "Can you keep using all of the capital
  you generate, effectively, for a very long time?" **[M2010-097]**: the company can use far more than it generates (capex
  1.33 times operating cash); the question is the return, which is the regulated return at best and about the bond rate
  on the window's record.
- *Buybacks.* None (640 shares bought in October 2025 for the Rabbi Trust only; "we have no publicly announced plans or
  programs to repurchase our shares", 10-K Item 5). The test of a buyback with no stated price does not arise. The bottom
  of the Q7 range, for the record: $33.47 a share on the all-equity basis ($78.58 equity-only), written back from Q7;
  with no shares bought, there is no price paid to set against it.
- *Issuance and deals* **[R1995-010]**, **[M1995-001]**. FCG was paid in cash ($922.8M), financed by a 4.4M-share offering
  ($366.4M net) and new debt; under the framework's definition it is an acquisition, not a merger, so the one STOP of Part A
  (an all-stock deal in undervalued stock, **[L2009-019]**) does not apply. Value given against value got: $922.8M paid for
  a business that earned $5.2M of net income in 2025 and asks its regulator for a $46.9M increase to earn its allowed
  return; on the record so far the cash given exceeds the value received, which the rows count as dilution whatever the
  currency **[M1995-001]**. Serial issuance: stock sold every year through the dividend plan, ATM programs in 2024 and
  2025, and a new $225M ATM with forward sales opened on 2026-10-01 (8-K). The rows name the habit "one of the surest
  indicators of a promotion-minded management" **[L2014-015]**; here it is the ordinary funding of a utility's rate base
  at prices well above book, which keeps the equity share near the regulator's capital structure. Carried as the
  framework carries it: a candidate second STOP, unresolved, weighed and not applied.
- **Part A WEIGHS AGAINST**: retained and raised capital has earned about the bond rate, the market leg trails the
  industry index, and the largest deal has not yet earned what was paid **[M1998-110]**, **[M1995-001]**.

**Part B, the pay, the board and the owners.**
- *Pay tied to what the person controls* **[L1994-019]**. Half the long-term award is "Total capital expenditures as a
  percentage of total capitalization as compared to companies in the performance peer group"; the other half is average ROE
  against peers, with an 8% floor for any payout above target, and the 2023 to 2025 ROE was measured "excluding Florida City
  Gas"; TSR is a 20% modifier (proxy). The capital component pays for spending, not for what the spending earns; the rows
  charge managers for the capital they use and call a record without that charge "a phony batting average" **[M1995-010]**.
  Leaving the acquisition out of the ROE measure pays on the return of the part that worked. The cash bonus centres on the
  EPS guidance band. A discretionary bonus was paid for completing FCG.
- *The board.* Eight directors, all independent except the CEO, who is also Chair since 2023; the compensation committee
  works with FW Cook against a peer median (proxy). "The people who have their hands on the switch are the beneficiaries of
  the system" **[M1998-066]**.
- *Owners as partners.* Dividends for 65 consecutive years and raised for 22, from $1.92 to $2.74 over five years (proxy);
  reports clear (Q5). Equity-plan and ATM issuance dilute existing owners at the market price, above the Q7 range, which
  is to their benefit only if the money then earns more than it costs.
- **Part B WEIGHS AGAINST**: the long-term award rewards capital spending relative to peers and measures return without
  the largest deal, the reverse of tying pay to the return on capital the person controls **[L1994-019]**, **[M1995-010]**.

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
asking first "are you going to have to put more cash into after you buy it?" **[M2014-068]**. Arithmetic in `calc.py`,
output in `calc_output.txt`; the construction is Q7's range convention with the PG re-test's four specifics and (a) to (f).

**Inputs.**
- *Rate:* 5.43%, the 30-year Treasury par yield, 10/16/2026. *Floor:* about 10%, applied to owner cash after the company's
  own tax, no conversion (Q7, Whose tax); no carryforward or credit expiring inside ten years was found, so no shelter is
  priced (effective tax rates 24.4% to 27.3%, 2021 to 2025).
- *Basis* (Q7, On what the floor is earned): all-equity central, owner cash before interest (after-tax interest paid added
  back at each year's effective rate) against market value plus net debt. Net debt at 2026-06-30 (10-Q): long-term debt
  $1,317.9M + current portion $131.7M + short-term borrowing $238.1M - cash $0.4M = **$1,687.3M**; finance-lease principal
  is not stated apart from long-term debt and its repayments are inside "Repayment of long-term debt and finance lease
  obligation", so it is in; operating leases ($7.9M liability at 2025 year-end) left out, said so. Subsequent events the
  10-Q states: the revolver enlarged to $650M (capacity, no draw stated); the Florida Energy Pathway announced; nothing
  adds to net debt. EV at the price: $3,186.4M + $1,687.3M = **$4,873.7M**. The equity-only figure is shown beside.
- *Cash input* (Q4 recast), all-equity, 2021 to 2025: after maintenance only 87.1 / 90.2 / 141.6 / 187.5 / 170.8, average
  **$135.4M**; after all capital spending -26.9 / 41.9 / 30.4 / -70.8 / -170.2, average -$39.1M.

**The specifics, applied.**
- *(e) Growth spending.* The filing allows the maintenance guess (depreciation on both lines, the proxy of **[M1998-127]**,
  the owner's "best guess" **[M2000-144]**), so the central case is owner cash after maintenance only, with the growth
  spending charged against the growth it buys; the all-spending case is beside.
- *(c) Acquisitions and the serial acquirer.* Net purchases over the window were $972.6M (FCG $925.0M in 2023, plus
  propane and other purchases of $36.4M and $11.8M in 2021 and 2022), against half of owner cash before purchases of
  $338.6M: the serial-acquirer convention applies, so the central figure is the **organic pair** (purchases left out,
  organic growth only) and the default pair (purchases deducted, total growth credited) is beside: maintenance-only owner
  cash less purchases averages -$59.1M, so the default pair has no positive value. FCG was paid in cash: an acquisition,
  not a merger. No signed, unclosed acquisition is pending; the Florida Energy Pathway is a construction project whose
  spending sits in the growth case below, and the 49% sale to NextEra's subsidiary states no proceeds (8-K 2026-09-01).
- *Organic growth as the filer reports it.* The filer reports no organic growth rate of earnings or cash; it reports
  margin items ("Natural gas growth (excluding service expansions)", $7.4M in 2025). **CONVENTION of this run:** the growth
  end is built from the growth spending itself: the window's average growth spending above the maintenance guess,
  **$174.6M a year**, each year's tranche earning a return R after tax from the following year onward, for ten years,
  after which spending and growth stop (zero nominal growth, purchases and growth spending stopping together). R is taken
  as **6.82%**, the higher of the shown incremental return (5.71%, Q3) and the allowed return on capital built from the
  filing (half equity at 9.75%, the middle of the 9.50% to 10.25% allowed returns in Delaware and Florida; half debt at
  5.25%, the band of the recent senior notes, after 26% tax). Rationale: (e) charges growth spending against the growth it
  buys, the filer gives no organic rate to carry, and the allowed return is the most the regulators let the spending earn,
  so the case leans to the business.
- *(b) Decline.* The all-spending series changes sign (first half 2021 to 2022 averages $7.5M, second half 2024 to 2025
  -$120.5M): the all-spending range is the no-growth case alone, -$720.6M of value, below zero per share, said so.
- *(a) Cycles.* No first or last window year is described by the filer as a peak, trough or aberration. Two facts are
  shown beside rather than used: the window holds only two full years of FCG (a post-purchase base of 2024 to 2025 is
  shown), and 2024 carried the RSAM credit (already added back to the maintenance guess).
- *(d) Working capital* is counted inside operating cash in every year.
- *(f) The cap.* The growth case lifts owner cash from $135.4M to about $254.5M by year ten, 6.5% a year, against sales
  growth of 13.0% a year 2021 to 2025 and below the discount rate after year ten (no growth). No cut is needed.

**The range (all-equity, central; per share after net debt; 24.106455M shares).**

| case | value of the business | per share | at 10% (fair-price ends) |
|---|---|---|---|
| no growth, maintenance-only, five-year base $135.4M | $2,494.1M | **$33.47** | -$13.81 |
| growth spending $174.6M/yr at R 6.82%, five-year base | $2,831.5M | **$47.46** | -$27.97 |
| beside: growth at the shown R 5.71% | $2,561.8M | $36.28 | -$32.91 |
| beside: post-FCG base (2024 to 2025 average $179.2M), no growth / with growth | $3,299.5M / $3,636.8M | $66.88 / $80.87 | $4.33 / -$9.83 |
| beside: 2025 NOPAT $193.0M, no growth / with 2026-guidance growth spending of $465M a year at 6.82% | $3,554.4M / $4,453.0M | $77.45 / $114.73 | $10.07 / -$27.65 |
| beside: literal window, all spending (series changes sign; no-growth case alone) | -$720.6M | below zero | n/a |
| beside: default pair, purchases deducted | negative base | below zero | n/a |

**Value range: $33.47 to $47.46 a share against $132.18.** Width 1.42 to 1. The growth case is the top at the sovereign
rate because the allowed return (6.82%) exceeds 5.43%; at the 10% floor the order inverts and growth spending destroys
value, "growth can destroy value" **[L2000-023]**, the finding (e) names.

**The floor, tested first.** The expected return at $132.18 (the rate at which each case's value equals the EV of
$4,873.7M): 2.78% on the no-growth case, 3.70% on the growth case, and 5.17% on the most generous case built (2025 NOPAT
carried flat with growth spending at the 2026 guidance level, all earning the allowed return). The simplest cross-check
agrees: 2025 NOPAT over EV is 3.96%, net income over market value 4.40%. **No case earns the floor at the price**; none
earns even the long government rate. "there’s just a point at which we drop out of the game" **[M2003-149]**. The price
also sits above the top of the range, which closes OUT however wide the range (the PG re-test's fourth specific).

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at 10% and the two averaged, after
the company's own tax, all-equity basis less net debt: **-$20.89 a share; no positive fair price exists on the all-equity
basis** (the business at 10% is worth less than its net debt on both ends: $1,354.3M and $1,013.0M against $1,687.3M).
The run is already on the organic pair, so the fallback the convention names for a non-positive central fair price gives
the same figure. **Equity-only beside:** owner cash after interest, maintenance-only, five-year average $102.9M; range at
the sovereign $78.58 to $100.37 (growth end: half of each year's growth spending funded by equity earning 9.75%, a
CONVENTION of this run on the same rationale as R); at 10%, $42.67 and $42.11; **equity-only fair price $42.39**. The
equity-only figure is the larger because the lenders' claim at about 5% is charged at its coupon, not at the 10% floor;
by the basis convention it never decides alone **[L2017-004]**. No cheap price is reported.

**What the result rests on, and the strongest thing against it.** The maintenance guess (total depreciation) is the
largest judgment; were maintenance half of it, five-year owner cash would rise by about $43M and the no-growth value at
the sovereign by about $800M, $33 a share: still below $70. The allowed return could rise in the pending FCG case; every
case built here already credits the allowed return to all growth spending. The rows say what to do with such a gap:
"If you need to use a computer or a calculator to make the calculation, you shouldn’t buy it." **[M2009-005]**.

- **VERDICT: OUT.** No case in the range earns the floor of about 10% at $132.18, the price sits far above the top of the
  range ($47.46), and the most generous case built earns 5.17% **[M2003-149]**, **[L2000-023]**, **[M2009-005]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT; operator rule 2). Facts already found are under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED (Q7 closed the file OUT; operator rule 2). Facts already found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED (Q7 closed the file OUT; operator rule 2). Facts already found are under AFTER THE STOP.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (Q7 closed the file OUT; operator rule 2). Facts already found are under AFTER THE STOP.

---
## THE BOX
**OUT at Q7.** Q1 IN, Q2 IN (Regulated Energy decides at 84%; a franchise at regulated returns, the framework's exception),
Q3 WEIGHS AGAINST, Q4 WEIGHS AGAINST, Q5 integrity IN, Q6 WEIGHS AGAINST on both parts; Q7 closes it: **value range
$33.47 to $47.46 a share (all-equity, maintenance-only, organic pair) against $132.18**; no case earns the floor of about
10% at the price (most generous case built: 5.17%), and the price sits far above the top of the range. Fair price
(reporting figure): -$20.89 all-equity, no positive fair price; equity-only $42.39.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged, operator rule 2.)* **[M1997-127]**
- **Q8, the bond.** 2025 NOPAT over EV at the price is 3.96%, net income over market value 4.40%, five-year
  maintenance-only owner cash after interest over market value 3.23%; the 30-year Treasury yields 5.43% (`calc_output.txt`).
- **Q9, the target's debt and exposures.** Debt $1,687.7M gross at 2026-06-30 (long-term $1,317.9M, current $131.7M,
  short-term $238.1M) against equity $1,673.4M; equity share of capitalization including short-term debt 50%, target 50% to
  60% (10-Q). Revolver enlarged in August 2026 to $650M ($250M 364-day tranche, $400M to 2031); $207.1M available at
  2026-06-30 before the amendment. Covenant: funded indebtedness no greater than 65% at each fiscal year-end, in compliance
  (10-K). Cash on hand $0.4M. Planned spending of $550M to $600M in 2026 and CPK's share of the $1.2B Florida Energy Pathway
  to 2030, funded by debt, the new $225M ATM with forward sales, and the dividend plan. A guaranty of about $109M of its
  capital contributions to the Florida Energy Pathway joint venture (8-K 2026-09-01). Contingent liability to Gulfstream
  for capacity released to third parties (10-K Item 1). Hurricane exposure in Florida, partly recovered through storm
  mechanisms (Item 1A). The acquisition criteria's "little or no debt" **[R1997-001]** is a whole-business criterion; not
  applied.
- **Q10.** Not reached; no sizing or action is implied.
- **Q12.** Natural gas, electricity and propane delivery to homes and businesses; no named business of the rows found.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template copy and the notes file were made before the first EDGAR
      call); written question by question; committed after each (Step 0 and Q1, Q2, Q3, Q4, Q5, Q6, Q7 with the Q6
      write-back, then this close), pathspec commits of the run file and research folder only.
- [x] Dispatched: the brief allowed per-question commits; the lock is the dispatching session's; the fold is the
      dispatcher's. No git lock was met. This run binds nothing until it is in the register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; the accidental sights (two
      other research-folder names and another company's commit subjects in the session context, a file count of `Test
      Runs/`, the memory index) are declared under contamination and not used. No search across `Test Runs/` was run.
- [x] Every v5 id resolves: `check_run.py` (in the research folder) finds every M/L/R id in `principle_ledger_v5.csv`, no
      E-id, and every quoted fragment beside an id inside that row (0 problems). Every filing fact carries its accession.
- [x] The order was kept; Q7 was the first STOP that failed; nothing after it is a clearance; Q8 to Q12 are NOT REACHED.
- [x] Owner cash after every real cost (both depreciation lines, stock pay, the RSAM credit reversed), never a
      net-income proxy; the sovereign from the US Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations line; Q2 threats; Q3 incremental return; Q6 FCG and pay).
- [x] Not a point-in-time run; rows of any date are admissible.
- [x] Only the arithmetic lines of `tools/run.py` were used; its "debt on the face" column was found to include equity
      and was not used; its missing second depreciation line was found in the filing and added.
- [x] Conventions of this run, confessed: the competitor set (from the proxy's peer group); the growth end of Q7 (growth
      spending at the higher of shown and allowed return, R 6.82%); the equity-only growth funding split (half equity at
      9.75%).
- [x] `python tools/check_framework.py` PASS before the closing commit (run 2026-10-17, all checks OK).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The serial-acquirer convention caught a single deal.** Q7 (c) tests "net purchases over the window" against half
of owner cash before purchases; one cash acquisition (FCG, $922.8M) trips it, so the central figure became the organic
pair although the company is not a serial buyer. Its prescription, "organic growth, as the filer reports it", then had
nothing to read: the filer reports no organic growth rate of earnings or cash. The run built the growth end from the
growth spending at a stated return and confessed it; the text should say what to do when the filer reports no organic
rate, and whether one large purchase is "serial". (2) **(e) does not say how to build the growth end** when growth is
bought by spending that the filing does not split: "growth spending charged against the growth it buys" needs a return
on that spending, which the text never names. (3) **The fair price can be negative** on the all-equity basis (both
ends at 10% are worth less than the net debt); Part VII defines the figure but not what to report when it is below zero,
and the fallback to the organic pair does not help when the run is already on it. Reported as a negative figure with
"no positive fair price". (4) **The regulated-return exception at Q2 meets the 10% floor at Q7.** Q2 carries a regulated
utility to Q3 "as a second best", but on the all-equity basis a rate base allowed about 7% after tax can never earn the
10% floor unless bought well below its rate base; every regulated utility at a market price near or above book will
close OUT at Q7. That may be the speakers' own result ("there’s no way we get rich on our utility investments" **[M2009-104]**), but the text does
not say so, and a reader of Q2 might expect the exception to lead somewhere. (5) **The tool**: `tools/run.py` reads only
the D&A line, missing the "Depreciation and accretion included in operations expenses" line ($15.9M in 2025), and its
ten-year debt column d3 is `CapitalizationLongtermDebtAndEquity`, which includes equity; both would mislead a run that
trusted the printout.
