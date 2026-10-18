## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** 150.50p a share, London close 2026-10-16 (Yahoo Finance chart API, aggregator, flagged per operator rule 5); the ADS
  CPYYY closed at $8.04 the same day (same aggregator, flagged). Check: four ordinaries at 150.50p at $1.3253 = $7.98 an ADS.
- **Shares by class** (one class, ordinary shares of 6 14/81p): **4,619,492,850 shares with voting rights** at 30 September 2026
  (5,064,902,964 issued less 445,410,114 in treasury), RNS "Total Voting Rights", Centrica plc, 1 October 2026 (read through the
  Investegate copy of the RNS). No SEC accession exists: `python Screens/cover_shares.py CPYYY` returns "CPYYY NOT AN SEC
  REGISTRANT in the live ticker file". The count includes the shares held by the employee trusts (90.4m at 31 December 2025,
  AR2025 note 26), which the EPS count leaves out (H1 2026 weighted average 4,536m); the voting count, the larger figure, is used.
  The ADS facility (SEC CIK 0001787383, F-6 of 2026-06-17, four ordinaries per ADS) is a depositary facility and files no accounts.
- **Market cap:** 4,619.49m x 150.50p = **£6,952m** (about $9,214m at $1.3253).
- **Sovereign for the earnings currency (GBP):** **5.864%**, the Bank of England's UK nominal spot (zero-coupon) gilt yield at 30
  years for 2026-10-15, the latest day published at the fetch (BoE yield-curve file "GLC Nominal daily data current month",
  sheet "4. spot curve"). Why this series: the protocol's USD line is the 30-year point of the issuer's curve, the brief names
  the DMO or the Bank of England, and the DMO's gilt reference-price export refused the fetch with a captcha page; the Bank of
  England fits its curve to gilt prices. Beside it, the Bank's 20-year nominal par yield (series IUDLNPY) was 5.7225% on
  2026-10-14; the run uses the 30-year spot figure, and the difference does not touch the box. Extracts in
  `Test Runs/_research 2026-10-17 CPYYY/sources_step0.md`.
- **Exchange rate:** $1.3253 per £, Bank of England spot series XUDLUSS, 2026-10-15 (latest published at the fetch).
- **Filings read** (operator rule 4; no 10-K, 20-F or proxy exists, so the company's own reports are the primary documents,
  downloaded from centrica.com, the date of each in place of an accession): Annual Report and Accounts **2025** (authorised for
  issue 18 February 2026), **2024** (19 February 2025), **2023** (14 February 2024), **2022** (15 February 2023), **2021**
  (23 February 2022), **2020** (24 February 2021), **2019** (12 February 2020), **2018** (20 February 2019; its Five Year
  Summary carries 2014 to 2018, which gives the FY2016 and FY2017 balance-sheet lines); the **Interim Results for the six months
  to 30 June 2026** (published 23 July 2026); the RNS above. The 2025 Preliminary Results announcement was downloaded and not
  needed. The directors' remuneration report was not read (the file closed before Q5 and Q6).
  **One figure cross-checked against the filed statement:** 2025 adjusted operating profit £814m, as printed in the Five Year
  Summary (AR2025 p.246), equals the total of segmental note 4(c) (p.151: Retail 424, Optimisation 155, Infrastructure 314,
  colleague profit share (34), MAP adjustment (45)) and the Group CFO's table (p.18); net assets £3,496m in the Five Year
  Summary equals the Group Balance Sheet (p.137).
- `python tools/run.py CPYYY` returned: "CPYYY: not an SEC filer. Use the evidence ladder: company IR site (English), exchange
  filings (TDnet / RNS / SEDAR+). This is UNRESEARCHED, not UNKNOWABLE." No arithmetic lines were printed; every figure below is
  read from the reports and summed by hand or by `Test Runs/_research 2026-10-17 CPYYY/q7_compute.py`.

### The lines of evidence chosen (the brief's first departure)
Derived from the 2025 report's business model (pp.14 to 17), the segment reviews (pp.24 to 31), the principal risks (pp.32 to
41) and the CFO's report and segment note, and chosen because the report itself shows they matter:
1. **The parts and their profit over the cycle** (Five Year Summaries of AR2018, AR2022 and AR2025; segment tables): the 2025
   resegmentation into Retail, Optimisation and Infrastructure decides which part decides.
2. **What the deciding part is made of, and how long each asset lasts** (AR2025 pp.27 to 29 and the nuclear impairment note
   7(c); H1 2026 pp.3 to 6): station closure dates, Spirit Energy's disposals, Rough's paused storage and expiring consent,
   Grain LNG's contracts, Sizewell C's regulated return, the meter business.
3. **Prices and the state's take** (price cap, Electricity Generator Levy, Energy Profits Levy): the levies are in the report
   (p.19, note 9) and cut the top of the cycle.
4. **Impairments and write-backs of the deciding part's assets over the decade** (exceptional items, notes 7): the filer's own
   record of what those assets were worth as prices moved.
5. **The balance sheets, ten years** (below), with the derivative books, margin cash, decommissioning and pension.
6. **Capital returned and its price** (buybacks 2023 to January 2026, note S4) and **acquisitions** (Grain LNG, Sizewell C,
   Severn CCGT): recorded, not judged, since the file closes before Q6.
Litigation and investigations, stock pay and the remuneration report were not read: they bear on Q4 to Q6, which the file does
not reach.

### The balance sheets first, ten years (read here because the file closes before Q4) **[M2025-032]**
Group, £m, 31 December. FY2016 and FY2017 from the AR2018 Five Year Summary and AR2018 comparatives; FY2018 to FY2025 from each
report's Group Balance Sheet (FY2022 from the AR2023 comparatives; FY2018 to FY2020 as first published, before later
restatements).

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Goodwill | n/r | 2,650 | 2,736 | 2,578 | 929 | 401 | 409 | 405 | 478 | 504 |
| Goodwill and intangibles (summary line) | 4,383 | 4,326 | 4,456 | 4,033 | 1,940 | 1,161 | 1,116 | 745 | 796 | 822 |
| Cash and cash equivalents | n/r | 2,864 | 1,268 | 1,342 | 1,820 | 5,060 | 4,842 | 6,443 | 6,338 | 4,307 |
| Trade and other receivables (current) | n/r | 4,669 | 5,543 | 4,839 | 2,801 | 5,881 | 8,450 | 5,409 | 5,204 | 4,675 |
| Inventories | n/r | 409 | 459 | 431 | 324 | 644 | 1,269 | 1,079 | 904 | 339 |
| Derivative assets (current + non-current) | n/r | 1,390 | 1,678 | 1,813 | 1,590 | 7,550 | 7,427 | 3,272 | 1,576 | 876 |
| Derivative liabilities (current + non-current) | n/r | 1,020 | 1,566 | 2,145 | 928 | 6,009 | 10,151 | 3,006 | 1,387 | 1,036 |
| Borrowings (current + non-current) | n/r | 6,298 | 4,754 | 5,343 | 5,376 | 4,643 | 4,017 | 4,103 | 3,512 | 2,856 |
| Provisions, non-current (mostly decommissioning) | n/r | 2,684 | 2,540 | 2,175 | 2,438 | 1,454 | 1,446 | 1,469 | 1,493 | 1,271 |
| Retirement benefit obligations | n/r | 886 | 302 | 219 | 601 | 231 | 110 | 181 | 150 | 307 |
| Retained earnings | n/r | 1,184 | 725 | (869) | (836) | 377 | (466) | 3,274 | 3,979 | 2,977 |
| Shareholders' equity | n/r | 2,703 | 3,145 | 1,212 | 957 | 2,365 | 1,017 | 3,877 | 4,422 | 3,085 |
| Net assets incl. minorities | 2,844 | 3,432 | 3,948 | 1,795 | 1,382 | 2,750 | 1,280 | 4,233 | 4,812 | 3,496 |
| Net debt (-) / net cash (+), company's definition | (3,473) | (2,596) | (2,946) | (3,507) | (2,998) | 680 | 1,199 | 2,744 | 2,858 | 1,487 |

(n/r: not in the documents read. 2018 to 2020 net debt as restated in the AR2022 Five Year Summary. Adjusted net cash at 30 June
2026 was £709m, H1 2026 p.2.)

What moved and why, in the filer's words where it gives them:
- **The equity was nearly lost and then refilled by one crisis.** Retained earnings went from £1,184m (2017) to £(869)m (2019) and
  £(836)m (2020) after impairments of exploration and production and nuclear assets (AR2019 and AR2020: E&P impairments of £476m
  and £644m, and £372m and £481m against the nuclear investment), and to £(466)m in 2022 on £(3,548)m of exceptional items and
  re-measurements of energy derivatives; the 2023 swing to £3,274m was largely the unwind of those re-measurements (£3,760m of
  exceptional items and re-measurements in 2023, AR2023 p.19). Shareholders' equity of £957m (2020) and £1,017m (2022) sat beside
  derivative liabilities of £928m and **£10,151m**.
- **Goodwill fell from £2,736m to £401m** as North America (Direct Energy, sold at the start of 2021) left the group; what remains
  (£504m) is mostly in Retail.
- **Debt was paid down from £6.3bn to £2.9bn and the group moved to net cash**, the turn coming in 2021 with the Direct Energy
  sale (discontinued investing inflow £2,588m, AR2022 cash-flow statement) and then the 2022 to 2023 windfall.
- **Receivables and inventories move with commodity prices**, not with customers: receivables £2,801m (2020), £8,450m (2022),
  £4,675m (2025); inventory £1,269m (2022) to £339m (2025), the last drop largely Rough's gas taken out of store (CFO report p.20).
- **Decommissioning and pension obligations shrank but did not go**: non-current provisions £2.7bn to £1.3bn (Spirit Energy £961m,
  Rough £321m at 31 December 2025, CFO report p.21); the pension deficit £886m (2017) to £307m (2025), with deficit payments of
  about £150m in 2026 and £140m in 2027 agreed (CFO report p.21).
- **What the balance sheet does not say and cannot say** **[M2025-032]**: the cash of £4.3bn is in part working liquidity for a
  trading and supply book (the 2022 derivative liabilities were ten times the equity; margin cash posted net £61m at the 2025
  year end, CFO report p.20), so the net cash is not all free; and the value of the nuclear and gas assets on it is rewritten
  every year with the price curve (nuclear investment £903m in 2023, £794m in 2024, £578m in 2025, with an impairment or a
  write-back in every year from 2019).

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what Centrica's businesses will produce, not what the quotation will do,
and the quotation's moves (169.55p at the end of 2025, AR2025 note 26; 150.50p now) tell nothing **[M2006-077]**. Margin of safety
**[M1996-084]** and no macro forecast **[M2000-094]** bear hardest: much of this group's recent profit came from a gas-price
crisis, and nothing in the run may rest on a view of where gas or power prices go. Who is paid to tell you **[M2020-037]**: the
company's own targets (adjusted EBITDA of £2.0bn and a doubling of EPS by 2030, H1 2026 p.2) are a projection by the seller and
are not used **[M1995-050]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the parts bought since 2024 have contracted or regulated
returns (Grain LNG "100% contracted until 2029, over 70% contracted until 2039 and over 50% contracted to 2045", AR2025 p.28;
Sizewell C "a 10.8% real allowed return on equity through the full construction period", H1 2026 p.4), the opposite of a
merchant business; (2) Retail's customer numbers, complaints and NPS all improved in 2025 (AR2025 p.25); (3) the group is in net
cash and has bought back £2bn of shares; (4) the Q7 computation made after the stop puts the mechanical range well above the
price. Each is weighed where it bears, and the last cannot reopen a castle question **[M2019-015]**.

## THE STANDING RULE
The purchase would be made for cash, with no borrowing, no option written and no position that can be called; nothing in owning
a minority of this share puts the buyer at risk of ruin **[M2012-081]**, **[L2023-005]**, **[M2004-065]**, **[L2014-005]**. The
target's own collateral and derivative exposures are the target's and belong to Q9 **[L2014-024]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test** **[M1995-051]**, **[M2012-065]**: a reasonable fix on the earning power and competitive position five or ten years
out. Centrica reports parts with different economics, so Q1 is answered on the parts that matter, a part mattering when it carries
more than half of five-year operating profit or else is the largest (Q1's holding-company paragraph with Q2's threshold, a
CONVENTION of the framework).

**Which part matters** (AR2025 Five Year Summary, p.246, adjusted operating profit restated to the 2025 segments, £m):

| | 2021 | 2022 | 2023 | 2024 | 2025 | five-year | share of group £9,374m |
|---|---|---|---|---|---|---|---|
| Retail | 206 | 34 | 808 | 458 | 424 | 1,930 | 20.6% |
| Optimisation (Centrica Energy, trading) | 66 | 1,481 | 831 | 339 | 155 | 2,872 | 30.6% |
| Infrastructure | 676 | 1,816 | 1,121 | 799 | 314 | 4,726 | **50.4%** |
| Profit share and MAP adjustment | 0 | (23) | (8) | (44) | (79) | (154) | |
| Group adjusted operating profit | 948 | 3,308 | 2,752 | 1,552 | 814 | 9,374 | |

Infrastructure carries 50.4% of the group's five-year adjusted operating profit (49.6% of the three segments' sum) and is the
largest part on either count: **it decides.** Its 2021 and 2022 figures include Spirit Energy's Norwegian assets, sold in 2022
(£556m and £485m, AR2022 p.16); without them Infrastructure is still the largest part (£3,685m against Optimisation's £2,872m).

**What the deciding part is, and where each piece will be in ten years** (AR2025 pp.27 to 29, note 7(c); H1 2026 pp.3 to 6):
- **Nuclear**, 20% of the UK's operating fleet, operated by EDF. The four AGR stations close between March 2028 and March 2030 on
  "lifetime closure dates announced by the operator" (note 7(c)); Heysham 1 and Hartlepool were extended in July 2026 to March
  2030 (H1 2026 p.4). Sizewell B runs to 2055 with a CfD of "£70.50/MWh from April 2035 to March 2055, based on 2025 prices and
  indexed to CPI inflation" (H1 2026 p.4); without that extension the carrying value "based on cash flows from 2035 to 2055 would
  be reduced by £153 million" (note 7(c)), out of £578m.
- **Spirit Energy** (69%): "The announced sales of the majority of Spirit Energy's assets signals the end of our North Sea gas
  production" (H1 2026 p.4); the Morecambe Hub is "expected to continue production through to around the end of the decade"
  (AR2025 p.28), with retained reserves of 9mmboe and a decommissioning provision of £961m.
- **Rough** (Centrica Energy Storage+): storage operations paused in 2025 "owing to uneconomic seasonal gas price spreads", a
  government decision on a commercial model awaited, and "Our current production consent with the North Sea Transition Authority
  ("NSTA") expires in April 2027, and we do not currently intend to seek an extension" (H1 2026 p.4).
- **Grain LNG** (50%, bought November 2025 with ECP for an equity investment of about £200m, enterprise value £1.5bn): contracted
  as quoted above, adjusted EBITDA "around £100m per annum (Centrica share)" expected (AR2025 pp.28 to 29).
- **Sizewell C** (15%, £0.4bn of a capped £1.3bn invested): a regulated asset base through construction (H1 2026 p.4).
- **Customer Assets** (the meter asset provider: 2.3m meters at June 2026, run-rate EBITDA "c.£60m per annum", H1 2026 p.3), Irish
  power (Whitegate CCGT, peakers under construction), and the Severn CCGT (bought May 2026, net consideration £367m).

**The key variables and how predictable they are** **[M1998-044]**: station lives (announced by the operator, extended a year or
two at a time); the end of Spirit's and Rough's production (dated by the filer); the contract and regulated terms of Grain,
Sizewell B after 2035, Sizewell C and the meters (written down in the filings); and the market prices of power and gas, which the
speakers do not forecast **[M2016-025]** and which the framework says is "never by itself a STOP at Q1 or Q2" (Q2, A commodity
business), so they enter at Q7. Read by its parts, the deciding part's ten-year position can be pictured: the assets that earned
its record end inside five years on the filer's own dates, and what remains is contracted, regulated, or merchant gas-fired
generation. The decision can be made off the figures **[M2008-069]**, as the trading houses were read "as a group" **[M2023-031]**.

**Against IN, written down** **[M1997-127]**: (1) the statements of the record do not show the future statements **[M2008-033]**,
since the assets that produced 2021 to 2025 are ending and the replacements have no record (Grain's first period was an adjusted
operating loss of £15m, AR2025 p.28); (2) the part's composition ten years out depends on capital not yet spent (capital
investment "around £1.1bn" in 2026, H1 2026 p.3), which the framework reads at Q6 as a use of the money, not at Q1 (Q2, A business
of parts: "read on the parts it owns"); (3) Rough's future waits on a government decision; (4) Optimisation, a trading book whose
management writes "A wide range of outcomes is possible for Centrica Energy in 2027" (H1 2026 p.3), is the second part (30.6%)
and does not decide, so by the convention it does not keep the whole outside the circle **[M2002-092]**; it is carried to Q4 and
Q9, and the bank-style exclusion of an unreadable derivatives book (Q1, The door the rows leave open for a bank) is not reached
because the deciding part is not the trading book. What is left in doubt is not where the owned deciding part will be (its record
assets' end is dated and its remaining assets' terms are filed) but what its castle and value are, which are Q2's and Q7's
questions.

**VERDICT: IN.** The deciding part can be understood from its filings, part by part, inside the perimeter **[M2012-065]**,
**[M2023-031]**; the trading book and the unbought assets are carried, not decisive.
