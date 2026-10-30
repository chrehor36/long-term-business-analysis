# Company Run — CENTRICA PLC (LSE: CNA; OTC ADS: CPYYY, four ordinaries per ADS) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold, 2026-10-17, after the run was committed: `PORTFOLIO.md` read for this ticker only; the operator does not hold this name.

*Run status: copied from the template 2026-10-17 before any fetch; written question by question; closed OUT at Q2. Dispatched blind run under `Screens/_daily/_dispatch_brief.md` with three stated departures (lines of evidence derived from the annual report; competitors taken from the report; the company's own annual report as the primary document).*

---
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
price. Each is weighed where it bears; on the last, "What you can’t do is turn any investment into a good deal by paying little"
**[M2019-015]**.

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

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question **[M1995-038]**: "why is that castle still standing? And what’s going to keep it standing or cause it not to be
standing five, 10, 20 years from now." The moat is what "protects excellent returns on invested capital" **[L2007-004]**.

### The parts table (section B of the gaps case, the framework's business of parts)
| Part | Five-year adjusted operating profit 2021-2025 | Share | Castle, in one line | Decides? |
|---|---|---|---|---|
| Infrastructure | £4,726m | 50.4% of group | a set of price-taking producers whose assets end within five years, beside new contracted and regulated assets | **Yes** (more than half; the largest) |
| Optimisation | £2,872m | 30.6% | an energy trading and optimisation book; earnings move with volatility, "A wide range of outcomes is possible" (H1 2026 p.3) | No |
| Retail | £1,930m | 20.6% | a price-capped supplier and a services business; see AFTER THE STOP | No |

**Inside the deciding part** (the filer's sub-lines, £m, adjusted operating profit; 2021 to 2023 from AR2021 p.19, AR2022 p.16,
AR2023 p.19; 2024 and 2025 from AR2025 pp.28 to 29; the restated segment totals above exceed these sums by other power assets
moved in from the old Business Solutions and Bord Gáis lines):

| Sub-part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year | share of £4,726m | where it is in ten years (filer's own words or dates) |
|---|---|---|---|---|---|---|---|---|
| Spirit Energy (incl. Norway, sold 2022) | 624 | 730 | 235 | 434 | 166 | 2,189 | 46.3% | "the end of our North Sea gas production"; Morecambe to "around the end of the decade" |
| Nuclear (20% of the existing fleet) | (38) | 724 | 536 | 353 | 180 | 1,755 | 37.1% | four of five stations closed by March 2030; Sizewell B on a CfD from 2035 |
| Rough / Centrica Storage | 77 | 339 | 312 | 2 | (45) | 685 | 14.5% | storage paused; production consent expires April 2027, no extension sought |
| Grain LNG, meters, other power | 13 | 23 | 38 | 10 | 13 | 97 | 2.1% | contracted, regulated or merchant gas-fired; see below |

About 98% of the deciding part's five-year profit came from three assets that the filer itself dates to their end inside five
years (Sizewell B's continuing share is a small part of Nuclear: £153m of the £578m carrying value rests on its 2035 to 2055 cash
flows, note 7(c)).

### The castle tests, each with its filing fact
1. **What keeps it standing, and how permanent** **[M1995-038]**. Nothing keeps the record castle standing: the profit came from
   gas fields being sold or depleted, a storage field whose storage business is paused and whose consent expires in April 2027,
   and four nuclear stations that close by March 2030. The "key factors" are reserves and station lives, and their permanence is
   given by the filer as a date.
2. **Would it stand without the lord?** Not the issue here: the assets end whoever runs them.
3. **The money test** **[M2011-015]**. A well-funded entrant could not build these assets, but it does not need to: the products
   (power and gas into the British market) are sold at the market price set by imports and other generators, and the filer's
   achieved prices follow the market (below).
4. **Pricing power and the agony before a rise** **[M2005-020]**. None. Nuclear achieved price £90/MWh in 2025 against £132 in
   2024; Spirit's achieved gas price 107p/therm against 132p (AR2025 p.27); nuclear 2026 and 2027 hedges at £76 and £73/MWh (p.29).
   The price is the market's: "whatever he charged for gas was my price" **[M2012-109]**. At the top of the cycle the state took
   the excess: the Electricity Generator Levy applies "a 45% tax rate to revenues generated over £75/MWh" to March 2028 (note
   7(c)), £511m charged to the end of 2025 (CFO report p.19), and UK gas production is taxed at 78% (AR2025, "Our view on taxation", p.23, and note 9). The
   price behaviour that the speakers read for durability **[M2005-020]** is that of a price taker whose good years are taxed away.
5. **Unit volume** **[M1999-054]**. Falling: nuclear output 6.6TWh (2024: 7.5TWh) on outages at Hartlepool; Spirit's total
   production 10.5mmboe (2024: 13.3mmboe), retained production 3.3mmboe; Rough's reservoir volume 8bcf (2024: 41bcf) (AR2025 p.27).
6. **The low-cost position** **[M2018-043]**, **[L2004-007]**. The cost position against other producers was not read from rivals'
   filings (see the competitor row). The filer's own unit costs rise as the fields deplete: Spirit's "Lifting and other cash
   production costs" £28.4/boe (2024: £25.3/boe), unit DDA £18.5/boe (p.27). The run does not rest its verdict on a cost
   comparison it did not make; it rests on tests 1, 4, 10 and the field's returns below, none of which turns on the cost rank.
7. **The brand** and 8. **the low bid**: a generator and a gas producer sell into a wholesale market where "most insureds don't
   care from whom they buy" has its exact analogue **[L2004-003]**: the buyer of a megawatt-hour or a therm does not know whose it is.
9. **Ask the competitors**: no competitor of the deciding part is named in the report (see the competitor row).
10. **Widening or narrowing** **[M1999-108]**, **[M2000-075]**. Narrowing by design: the 2025 report records disposals of
    Spirit's Southern North Sea and Dutch assets (proceeds about £180m, AR2025 p.28), the pause at Rough, and £508m of
    impairments "largely across our late-life gas field assets and investment in Nuclear" (CFO report p.18).
11. **What could destroy it** **[M2000-014]**. The destruction is not a risk but a schedule. And the record assets' value moved
    with every change in the forward curve: the nuclear investment was impaired by £372m (2019) and £481m (2020), written back
    by £747m (2021) and £195m (2022), impaired by £549m (2023), £48m (2024) and £251m (2025) (exceptional-items notes of each
    report).

### The competitor row
The 2025 report names no competitor of the deciding part; EDF is named as the operator of the nuclear fleet and owner of the other
80% (a partner, not a rival), and Ithaca Energy and Serica Energy only as buyers of Spirit's assets. Elsewhere the reports name
retail rivals: AR2024's Retail review (pdf page 35) compares complaints with "Ovo, Octopus and EDF", and AR2022 names
Octopus Energy as taker of Bulb's customers. **None of these files with the SEC** (flagged), and their own reports were not read in
this run. So no same-metric competitor row from rivals' filings is written; this is declared as a gap. For the nuclear part the
field is one fleet: Centrica's 20% is a fifth of the fleet's own economics, so its record is the field's record pro rata.

### The field's returns over the last full cycle (section C), judged in words
The deciding part's predecessors (Exploration & Production and Central Power Generation to 2017, Upstream 2018 to 2024,
Infrastructure 2025) earned adjusted operating profit of £210m (2016), £236m (2017), £567m (2018), £178m (2019), £90m (2020),
£676m (2021), £1,816m (2022), £1,121m (2023), £799m (2024) and £314m (2025): about £6.0bn over ten years, of which £2.9bn in the two
crisis years 2022 and 2023, and that before the impairments of the same assets, which netted to about £2.9bn from 2019 to 2025
(E&P £476m and £644m in 2019 and 2020; power assets £381m and £525m; the Norway disposal group £244m in 2021; gas storage £362m in
2022 and £75m in 2024; the nuclear swings above; gas fields £244m in 2025), and before the windfall levies of 2023 to 2025. The
2016 to 2018 impairments were not tallied. Over the full cycle, from the pre-crisis trough through the 2022 peak to 2025, the
assets of the deciding part returned, after the write-downs of the very assets that earned the profit, an amount the filer's own
statements show to be ordinary at best for a capital base of several billion pounds (the group's average capital employed was
£6.3bn to £6.9bn in 2017 to 2019, AR2018 and AR2019 ROACE tables), with the excess of the one good cycle taxed by levies. Judged in
words, as the framework requires **[M1999-108]**: a field that "protects only ordinary returns" over the cycle (Q2's OUT list,
the CONVENTION of section C), and in this case one whose producing assets are ending.

### The new parts, read as owned and weighed
Grain LNG (contracted, management's "expected unlevered, post-tax nominal IRR of ~9%", AR2025 p.28), Sizewell C (a regulated
return on equity during construction, H1 2026 p.4), the meter business and the Severn and Irish gas plants are the parts the
company is buying to replace the record (the policy "pivoting the Group towards more stable and predictable earnings", H1 2026
p.2). They produced 2.1% of the deciding part's five-year profit, so they do not decide. Their castles, as filed: a contracted
return that management itself puts near 9% unlevered is an ordinary return, and a regulator's return is carried by the framework to Q3
as a second best (Q2, What it rules OUT), where the rows say of such returns "there’s no way we get rich on our utility
investments" **[M2009-104]**, **[L2009-012]**; neither is a castle that protects excellent returns **[L2007-004]**. A
change for the better is credited only on a full cycle **[M2017-026]**, **[L1995-022]**, and these assets have no cycle in the
filings.

**Against OUT, written down** **[M1997-127]**: (1) nuclear generation is low in running cost and Sizewell B has a CfD to 2055;
(2) Grain LNG is Europe's largest LNG import terminal, contracted for decades, and Sizewell C's return is set by a regulator; (3)
Retail and Optimisation together earned half the group's five-year profit and are not read here as the deciding part; (4) if the
2025 reorganisation had been drawn differently (Rough with Optimisation, say), the shares would move, although the deciding
part's largest sub-parts would not; (5) the commodity paragraph makes the low-cost test the main Q2 question for a commodity
business, and that test was not run against rivals (test 6). None of these shows a castle that protects excellent returns over
ten to twenty years for the assets that carry the deciding part's record.

**VERDICT: OUT.** The deciding part's castle is not standing ten years out on the filer's own dates, has no pricing power, and
over the full cycle its field earned ordinary returns at best once the write-downs of the same assets are counted: a declining
business, "If you really think a business is declining, most of the time you should avoid it." **[M2012-062]**; "What you can’t
do is turn any investment into a good deal by paying little" **[M2019-015]**; the money test's own close, "If the answer had
been yes, we wouldn’t have done it." **[M2011-015]**; the box is "out" of the three **[M2006-013]**, and a low price does not
change it: "marginal businesses purchased at cheap prices may be attractive as short-term investments, they are the wrong
foundation on which to build a large and enduring enterprise" **[L2014-009]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (closed at Q2, operator rule 2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The ten balance sheets were read in Step 0 above **[M2025-032]**; facts found are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts were found and are recorded, not judged, under AFTER THE STOP.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. The buyback prices are recorded under AFTER THE STOP beside the bottom of the computed range; no Q6 line is written
back, because Q7 was not reached as a clearance.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The owner's two reporting figures (Part VII, The owner's price) are computed below under the
protocol's heading.

### COMPUTATION, NOT A CLEARANCE
*Made after the Q2 stop, for the owner's reporting figures only (operator rule 3; Part VII). Nothing here is a verdict or entry
language, and nothing here reopens Q2.* Script and output: `Test Runs/_research 2026-10-17 CPYYY/q7_compute.py` and
`q7_output.txt`.

**Owner cash, £m** (statutory Group Cash Flow Statements of AR2022, AR2023 and AR2025; lease cash from the leases notes; growth
spending from the AR2025 CFO report's net-investment table, p.20). All-equity basis: net cash from operating activities (after
the company's own tax, pension deficit payments, working capital and margin cash), operating interest added back, plus dividends
from joint ventures and associates (the nuclear associate), less purchases of property, plant and intangibles net of sales, less
businesses and joint ventures bought net of businesses sold (continuing), less lease cash, less distributions to the Spirit
Energy minority. Interest received and paid, securities and other investments are left out (they belong to net cash).

| | 2021 | 2022 | 2023 | 2024 | 2025 | average |
|---|---|---|---|---|---|---|
| Owner cash, all spending | 1,184 | 695 | 2,547 | 908 | (312) | 1,004 |
| Growth spending named by the filer (MAP; Sizewell C, Grain LNG, MAP) | 0 | 0 | 0 | 104 | 866 | |
| **Owner cash, maintenance only (central, specific (e))** | 1,184 | 695 | 2,547 | 1,012 | 554 | **1,198** |
| Depreciation variant (D&A in place of capital spending), maintenance only | 800 | 386 | 2,364 | 955 | 668 | 1,035 |
| Equity-only (after net interest), maintenance only | 953 | 539 | 2,508 | 1,030 | 584 | 1,123 |

**The specifics, applied.** Growth on the aggregate owner cash, not per share (the PG specifics). (a) Cycles: neither end year is
described by the filer as aberrational, so the literal window is the base; the cyclical peak sits inside it (2022 and 2023, the
gas-price crisis), which specific (a) does not address (see What was wrong or unclear); a beside figure without the two crisis
years is shown below as a CONVENTION of this run. (b) Decline: the central series falls from £1,184m to £554m, a shown growth of
**-17.3% a year** between the end years, carried as the bottom; the no-growth case is the top. In the all-spending series the sign
changes, so its growth (-31.8%) is measured between the first and second halves. (c) Acquisitions: deducted in the all-spending
series and the purchases stop after year ten; net purchases over the window (£444m net) are far below half of owner cash, so
the serial-acquirer rule does not apply; the filer reports no organic growth of owner cash, so no organic pair is shown. The
Severn CCGT, closed in May 2026 after the window, is inside the 30 June 2026 net cash (£367m paid) and credited at nothing, no
earnings of its own being filed in the documents read. The signed sale of Spirit's last Southern North Sea assets to Serica
(headline £57m, completion expected in the second half of 2026) is left out as immaterial. (d) Working capital is counted (it is
inside operating cash flow). (e) The maintenance-only case is central, the growth spending named by the CFO's report being the
filer's own split; the all-spending case is beside. (f) The cap: the shown growth is negative, so no cut arises. Discount rate
5.864% (Step 0); ten years at the shown growth, then zero nominal growth.

**(a) VALUE RANGE (central: all-equity, maintenance only), net cash of £709m at 30 June 2026 added, 4,619.49m shares:**
**137.6p to 457.7p a share** (whole business £5,649m to £20,437m), that is **$7.29 to $24.26 an ADS** at $1.3253 (BoE, 15 October
2026), against **150.50p** ($8.04 an ADS). Width 3.62 to one. Equity-only beside: 172.0p to 414.5p ($9.12 to $21.97 an ADS).
Beside, all spending: 77.3p to 404.7p; depreciation variant: 286.3p to 397.3p.

**(b) FAIR PRICE** (Part VII: each end case valued at ten percent, the two averaged; owner cash after the company's own tax, no
conversion): **189.6p a share, $10.05 an ADS, on the all-equity basis (central)**; **179.6p, $9.52 an ADS, equity-only** (beside).
Beside, all spending: 150.0p ($7.95); depreciation variant: 210.9p ($11.18).

**How Q7 would have closed, had it been reached** (for the record only): the floor test first: at 150.50p the top case returns
about 19% a year and the bottom case less than nothing, so some case earns the floor and the floor test alone does not close it;
the width is 3.62 to one, above the three-to-one line, so Q7 would have closed TOO HARD on width (the range convention).

**Beside, written down against the figures** **[M1997-127]**:
- *A CONVENTION of this run (rationale: the crisis peak sits inside the window, where specific (a) does not reach):* the central
  series without 2022 and 2023 averages £917m; carried the same way it gives 108.9p to 353.7p and a fair price of 148.6p,
  about the price.
- The construction carries the base at the shown rate for ten years. The filer's own dates end about 98% of the deciding part's
  five-year profit inside five years (Q2), and the decommissioning cash of Spirit and Rough (provisions £961m and £321m at the
  2025 year end, pre-tax, with a £536m deferred tax asset against the gas provisions) falls due as production ends; neither is in
  the five-year average. The range convention has no specific for a dated end of the earning assets, so the computation is likely
  high at its top.
- Not in net debt by the framework's definition, shown beside: decommissioning provisions of £1,270m (30 June 2026, pre-tax) and
  the IAS 19 pension deficit of £252m (30 June 2026, H1 2026, pension and decommissioning paragraphs); net of the deferred tax asset they are about £1.0bn, or about
  21p a share. The minority's 31% of Spirit Energy (non-controlling interests £411m at book, AR2025 balance sheet) is a claim on
  part of the cash counted.
- Part of the £0.7bn net cash is working liquidity for the trading and supply book (Step 0), not free cash.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (not asked; none of the businesses named in Q12 is among Centrica's).

---
## THE BOX
**OUT at Q2** (the castle of the deciding part, Infrastructure: its record assets end inside five years on the filer's own dates,
it has no pricing power, and its field earned ordinary returns at best over the cycle once the write-downs of the same assets are
counted). Q7 not reached; COMPUTATION, NOT A CLEARANCE: value range 137.6p to 457.7p a share (all-equity, maintenance only)
against 150.50p; fair price 189.6p all-equity, 179.6p equity-only. **Integrity facts recorded, not judged** (Part VII).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.

**Q2, the parts that do not decide (carried, not judged).**
- *Retail* (20.6% of five-year profit): adjusted operating margin 2.6% in 2025 (2024: 2.7%); UK Home Energy Supply adjusted
  operating profit £163m (2024: £269m), with warmer weather an £80m headwind, offset in part by regulatory reconciliations including £42m
  from the Energy Price Guarantee and £41m of lower Feed-in-Tariff costs; Home Services £114m at a 6.8% margin; bad debt £418m (2024: £369m) against "industry-wide challenges", with domestic
  debt owed to suppliers of £4.5bn (citing Ofgem); 7.96m home energy customers, the year's gain coming from 91,000 customers taken
  on from two failed suppliers, "a small decrease in underlying customers" and "increased levels of customer switching"; 32% of
  UK customers on fixed tariffs, "typically at a discount to the standard variable tariff" (AR2025 pp.25 to 26). Named rivals:
  Ovo, Octopus and EDF (AR2024's Retail review), none an SEC filer.
- *Optimisation* (30.6%): adjusted operating profit £1,481m (2022), £831m (2023), £339m (2024), £155m (2025); 2025 hit by
  "geopolitical uncertainty and EU storage targets"; management's medium-term range for Centrica Energy EBITDA £300m to £400m,
  and "A wide range of outcomes is possible for Centrica Energy in 2027" (H1 2026 p.3); the LNG book "fully hedged to 2028 and
  over 80% hedged to the end of the decade" (AR2025 p.26).
- *Infrastructure's new parts*: Grain LNG ("expected unlevered, post-tax nominal IRR of ~9% and an equity IRR of ~14%+",
  AR2025 p.28); Sizewell C ("a 10.8% real allowed return on equity through the full construction period, in turn supporting a
  12%+ IRR", H1 2026 p.4); the meter business (2.3m meters, run-rate EBITDA c.£60m, capital investment £271m in 2025 and £133m in
  H1 2026); rateable assets' EBITDA about £175m expected in 2026 (H1 2026 p.3).

**Q3, capital.** Capital expenditure (company definition) £1,227m in 2025 against depreciation and amortisation of £428m; 2026
capital investment "around £1.1bn" (H1 2026 p.3); free cash flow (company definition) £(167)m in 2025 and £(570)m in H1 2026.
The group's own post-tax return on average capital employed was 14% (2017), 13% (2018) and 9% (2019) before impairments (AR2018
and AR2019 performance measures); the measure is not published in the later reports read.

**Q4, the accounts.** The headline figures are adjusted EBITDA and adjusted operating profit, "before exceptional items and
certain re-measurements"; the re-measurements of energy derivatives were £(3,548)m in 2022 and £3,760m (with exceptional items)
in 2023, and the statutory result swung from a £782m loss (2022) to a £3,929m profit (2023). Long-term targets in adjusted EBITDA
(£2.0bn) and EPS (doubling by 2030), and segment guidance each half-year (H1 2026 pp.2 to 3): the habit Q4 records as a weighing
against and carries to Q5 (Q4, The make-the-numbers habit). In the company's favour: transformation costs "are included within
business performance rather than exceptional items" (H1 2026 p.5). Impairments or write-backs of the nuclear investment in every
year 2019 to 2025 (Q2, test 11). The Electricity Generator Levy is charged in cost of sales, not as tax (CFO report p.19).

**Q5, integrity facts (recorded, not judged).** In early 2023 the supplier British Gas used to install prepayment meters under
warrant "had, in some instances, not been showing our customers empathy and respect"; the company says it investigated and
reported publicly, found the issues "were not systemic", and Ofgem imposed a moratorium on such installations from February 2023
to January 2024 (AR2023 Chair's statement p.4 and principal risks). The Chair's statement also says that under the price cap
unpaid bills are "added to the bills of all other customers". A later run that reaches Q5 must answer these (Part VII).

**Q6, the money.** Buybacks: £615m at an average 120.1p (2023), £504m at 130.8p (2024), £827m at 159.0p (2025), completing a £2bn
programme in January 2026 (notes S4); against the computed bottom of 137.6p (central, all-equity) the 2025 purchases were above
it and the 2023 purchases below it (recorded only; Q7 was not reached, so no Q6 line is written). Dividend 5.5p for 2025 (2024:
4.5p), interim 2026 2.0p. Deals paid in cash: Grain LNG (about £200m equity for 50%, November 2025), Sizewell C (£1.3bn capped
commitment), Severn CCGT (£367m net, May 2026); disposals: Direct Energy (2021), Spirit Energy's Norwegian assets (2022), Cygnus
and the Southern North Sea assets (2025 to 2026).

**Q9, debt and exposures.** Margin cash: "a £1.2bn outflow of collateral and margin cash" in 2022 and "the £1.9bn margin cash
position seen at the end of August 2022" (AR2022 pp.20 and 36); derivative liabilities £10,151m against equity of £1,017m at the
2022 year end; committed facilities £5.0bn (£3.1bn undrawn) at the 2025 year end, £1.5bn of them maturing in 2028, with cash of
£4.3bn (viability statement, AR2025); borrowings £2,856m; decommissioning provisions £1.27bn and pension deficit £252m at June
2026; adjusted net cash £709m at June 2026 (from £1,487m at the 2025 year end).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit cbee8479); written question by question; committed after each
      (Q1 b4a190af, Q2 2dd1f81e, then this close).
- [x] Dispatched run: the brief allowed per-question pathspec commits of the run file and research folder only, and states the lock
      is held by the dispatching session; this run did not touch the lock. The fold into the register is the dispatcher's (operator
      rule ten); a run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Contamination, declared and not
      used:** the session context showed commit subjects for another company's run and fold (BIPC, 2026-10-17), file names of two
      other companies' research folders (AYI, ARCB) in the git status, and the repository map and a memory index line with counts
      of gate-clearers and the state of other queues; none concerns Centrica, and none was used. **One breach, declared:** before copying the template,
      the run listed `Test Runs/` through a filter for "CPYYY", "centrica" or "CNA" to check that the dated file did not already
      exist; under the blind rule that filter is a search across `Test Runs/`. It returned no match, so nothing was seen; later
      checks named the exact new research path only.
- [x] Every v5 id resolves (`check_run.py`: every M/L/R id in `principle_ledger_v5.csv`, every quoted fragment beside an id inside
      that row, no E-ids); every filing fact carries its document, date and page in place of an accession (no SEC filings exist).
- [x] The order was kept; Q1 IN, Q2 OUT closed the run; Q3 to Q12 NOT REACHED; the Q7 figures are headed COMPUTATION, NOT A
      CLEARANCE and carry no entry language.
- [x] Owner cash from the statutory cash-flow statements after every real cost (tax, pension deficit, leases, all capital
      spending, the minority), never a net-income proxy (operator rule 5); sovereign from the Bank of England, dated; aggregator
      quotes flagged.
- [x] Contrary evidence written down as found (foundations; Q1; Q2; beside the computation); facts for later questions under AFTER
      THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor rule arises.
- [x] `tools/run.py` printed no arithmetic for this name; nothing it printed was used.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Five things. (1) **The parts rule one level down.** The deciding part, Infrastructure, is itself a set of sub-parts with different
economics (merchant gas production, a nuclear share, a storage field, a contracted LNG terminal, a regulated nuclear project,
meters). Q2's business-of-parts paragraph says how to pick the deciding segment but not whether to apply the same threshold inside
it; this run judged the deciding part on its record, showed the sub-parts, and noted that 98% of its profit came from three
sub-parts with dated ends. (2) **A dated end of the earning assets.** Q1's routing, Q2's tests and Q7's range all assume a business
that goes on; none speaks of assets the filer itself dates to closure (station lives, production consents, depletion). The run
read it at Q2 as a castle not standing ten years out; Q7's construction (five-year average carried at the shown rate) has no
specific for it and so overstates a run-off business. (3) **A peak inside the window.** Specific (a) changes the base only when the
first or last year is aberrational; here the gas-price crisis (2022 and 2023) sits in the middle of the window and dominates the
average. The run used the literal window, as the text says, and showed a beside figure without those years as its own
CONVENTION. (4) **"A change for the better" against a change of assets.** Section C's sentence (credit only on a full cycle, until
then TOO HARD (NATURE)) is written for a business whose own economics improve; it is unclear whether it governs a company that
claims to change its earnings by buying different assets, while the business-of-parts paragraph says to read such a company on
the parts it owns. The run read the parts owned, found the new parts too small to decide, and did not use section C's box. (5)
**The commodity paragraph and the low-cost test.** For a commodity business the paragraph makes the low-cost test the Q2 question
and sends an unread cost position to TOO HARD (WORK); it does not say whether a castle can close OUT on other tests (no pricing
power, depletion, ordinary cycle returns) while the cost rank is unread. This run closed OUT on those tests and stated that it did
not rest on a cost comparison; a reader who takes the paragraph as exclusive would close the same file TOO HARD (WORK) at Q2.
Also noted: the GBP sovereign is not in the protocol's table (the run used the Bank of England's 30-year spot point, the DMO
refusing the fetch), and the template's competitor row presumes SEC-filing rivals, which a UK energy company does not have.

