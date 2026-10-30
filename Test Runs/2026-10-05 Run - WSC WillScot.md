# Company Run: WillScot Holdings Corporation (NASDAQ: WSC), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface
`Test Runs/_TEMPLATE - Company Run.md`, copied to this dated file before any fetch. Every judgment cites a v5 ledger id
in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run and later
questions are marked NOT REACHED. Working folder: `Test Runs/_research 2026-10-05 WSC/` (filings as text, the tool
output, and the scripts `compute.py` and `roic.py` that make every number below from the filed figures).

Quotation marks: double quotes beside a bold id are the ledger row's own words; ‘single quotes’ are the filer's
words from the filing named.

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is closed to this run by the blind rule of
the brief, so whether the operator holds WSC is unknown to the analyst.

**CONTAMINATION, declared.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`,
`Screens/WATCHLIST RUN QUEUE.md`, the prepped reading list, any other run or research file about WSC, any other
company's 2026-10-05 run or research-pass file, and the unadopted gaps case. Seen without opening, in the session's
starting context: the git status listing (untracked run files named for ABG, CAG and GIII dated 2026-10-05, research
folders for AYI, BDC and ARCB, names only); five commit subjects (a small-cap triage screen; a session-state note that
‘unmapped small caps’ were run and a ‘gaps case’ waits; an HOS Hornbeck Offshore run closed OUT at Q2 on the reasoning
that offshore vessels are priced off rig rates and no peer earned the Treasury rate on assets over a cycle; a CSW
Industrials run closed OUT at Q7; a `tools/run.py` change printing finance-lease principal as an alternate); and the
memory index lines (wave 7 paused, holding reviews owed, ‘57 gate-clearers, nothing buyable’). Nothing about WSC was
in any of it. The HOS subject is the one that could steer this run, since it names a whole-span return test against
peers; this run uses a whole-span peer comparison because the brief and Q2's test 9 ask for one, and it reaches a
different box on it (below).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $17.07 (2026-10-05, from `tools/run.py`; an aggregator quote, live quote only, flagged under operator
  rule 5).
- **Shares** from the latest filing's cover: 181,190,958 common shares, one class, par $0.0001 (10-Q for the period
  ended 2026-06-30, filed 2026-08-06, accession `0001647088-26-000056`; `python Screens/cover_shares.py WSC`, cover as
  of 2026-07-30). No second class; the Class B shares of 2017 to 2020 were exchanged in the 2020 merger (10-K FY2020,
  `0001647088-21-000015`).
- **Market cap:** 181.19M x $17.07 = **$3,093M.** Debt at 2026-06-30 $3,495M face (10-Q, `0001647088-26-000056`;
  cash $18M), so enterprise value about $6.57B.
- **Sovereign for the earnings currency (USD):** **5.63%**, US Treasury daily par yield curve, 30-year, 2026-10-02
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-19, `0001647088-26-000011`; 10-Q Q2 2026, filed
  2026-08-06, `0001647088-26-000056`; DEF 14A filed 2026-04-22, `0001647088-26-000021`; 10-Ks FY2018 to FY2024
  (`0001628280-19-002990`, `0001647088-20-000010`, `0001647088-21-000015`, `0001647088-22-000009`,
  `0001647088-23-000014`, `0001647088-24-000030`, `0001647088-25-000009`); 8-Ks: Q2 2026 release
  `0001647088-26-000054`, Q4 2025 release `0001647088-26-000009`, the Item 2.05 Network Optimization 8-K of 2025-12-22
  `0001753926-25-001926`, CEO succession `0001647088-25-000050`, McGrath termination `0001647088-24-000149`, and the
  officer changes `0001647088-24-000153`, `0001647088-25-000002`, `0001647088-25-000016`, `0001753926-25-001166`,
  `0001647088-25-000069`, `0001647088-26-000003`, `0001647088-26-000034`.
- **One figure cross-checked against the filed statement:** net cash from operating activities FY2025 = $761,985
  thousand on the filed cash-flow statement (10-K FY2025, `0001647088-26-000011`, page 55); `tools/run.py` (XBRL) prints
  762.0. Agrees.
- **`tools/run.py` arithmetic lines, checked against the filing, and one material error found.** The tool's ‘capex’
  column is `PaymentsToAcquirePropertyPlantAndEquipment` only ($22.2M, $18.4M, $24.3M for 2023 to 2025). It omits
  **purchase of rental equipment and refurbishments** ($227.0M, $280.9M, $317.7M) and the **proceeds from sale of
  rental equipment** ($51.3M, $64.0M, $65.9M), both on the same filed statement. Its owner-earnings lines (mean 574.7 to
  637.0, ‘yield’ 18.6% to 20.6%) therefore overstate owner cash by about $250M a year and are **not used**. The
  rental fleet is the capital that matters here. Only its price, share, sovereign and balance-sheet lines are used.
  The tool prints v4 material; none of it is read (Part VII).

### Owner cash after every real cost, from the filed cash-flow statements (USD millions). COMPUTATION - NOT A CLEARANCE
Sources: 10-K FY2022 (`0001647088-23-000014`) for 2021 and 2022; 10-K FY2025 (`0001647088-26-000011`) for 2023 to 2025.
2021 and 2022 include the discontinued Tank and Pump and UK Storage units (sold 2022 and January 2023), as filed.

| | 2021 | 2022 | 2023 | 2024 | 2025 | mean |
|---|---|---|---|---|---|---|
| Operating cash flow | 539.9 | 744.7 | 761.2 | 561.6 | 762.0 | |
| less stock pay | 26.2 | 29.6 | 34.5 | 36.0 | 38.4 | |
| less purchase of rental equipment and refurbishments | 278.5 | 443.1 | 227.0 | 280.9 | 317.7 | |
| plus proceeds from sale of rental equipment | 55.2 | 70.7 | 51.3 | 64.0 | 65.9 | |
| less purchase of PP&E, plus PP&E sale proceeds | 30.1 | 43.2 | 9.0 | 16.6 | 21.4 | |
| less finance-lease principal | 17.4 | 42.2 | 16.6 | 19.4 | 27.3 | |
| **A. Owner cash, all capital spending deducted (as filed)** | **242.9** | **257.2** | **525.5** | **272.8** | **423.0** | **344.3** |
| A2. A with the 2024 McGrath fee and deal costs ($225.7M, 10-K FY2024 MD&A) added back | 242.9 | 257.2 | 525.5 | 498.5 | 423.0 | 389.4 |
| Acquisitions, net of cash acquired | 147.2 | 220.6 | 561.6 | 121.2 | 144.7 | |
| B. A less acquisitions (fleet and lines bought, counted as capital) | 95.7 | 36.6 | -36.2 | 151.6 | 278.3 | 105.2 |
| D. Depreciation variant: OCF less stock pay, total D&A and finance-lease principal | 178.1 | 329.3 | 371.5 | 121.3 | 266.2 | 253.3 |

Owner cash is after interest paid ($103.8M to $216.6M a year) and after cash taxes ($9.9M to $45.6M), so it is cash
to the equity. Net rental capex (purchases less sale proceeds) averaged **$248.0M** against rental depreciation
averaging **$275.5M** (2021 $218.8M, segment table, `0001647088-23-000014`; 2022 to 2025 $256.7M, $265.7M, $302.1M,
$334.0M before the restructuring charge). The organic fleet was not being replaced at its depreciation; acquisitions of
$1,195M over the five years added fleet and new lines. Then in Q4 2025 the company wrote off fleet with a net book
value of $311M (about 51,000 units, 30,000 storage and 21,000 modular) as ‘long idle, non-standard, or higher repair
cost units’, after $41M of incremental depreciation earlier in 2025 on units identified for disposal (8-K Item 2.05,
`0001753926-25-001926`). The filing gives no split of maintenance and growth capital (‘We manage our maintenance capex
and growth capex to align with the economic conditions’, 10-K FY2025, Item 1): no instance found of a maintenance
figure in the 10-Ks FY2018 to FY2025 by a search for ‘maintenance capex’ and ‘maintenance capital’. Which of A, B or D
is the true cost of standing still is a Q3 judgment, and Q3 is not reached.

### The balance sheets, ten year-ends, before the income account **[M2025-032]**
Read because the file closes before Q4. Source: `tools/run.py` table (first-filed XBRL vintages, accessions printed
there) checked against the filed balance sheets of the 10-Ks named above; tangible equity is mine (equity less goodwill
less intangibles).

| year-end | assets | equity | goodwill | intangibles | tangible equity | debt (face) | receivables | revenue | rental equip., net |
|---|---|---|---|---|---|---|---|---|---|
| 2019 | 2,898 | 644 | 235 | 127 | 282 | 1,633 | 248 | 1,064 | n/r |
| 2020 | 5,572 | 2,141 | 1,171 | 496 | 474 | 2,470 | 331 | 1,273 | 2,932 |
| 2021 | 5,774 | 1,997 | 1,179 | 461 | 357 | 2,712 | 400 | n/r | 2,778 |
| 2022 | 5,828 | 1,565 | 1,011 | 419 | 135 | 3,076 | 410 | 2,143 | 3,077 |
| 2023 | 6,138 | 1,261 | 1,177 | 420 | -336 | 3,557 | 451 | 2,365 | 3,381 |
| 2024 | 6,035 | 1,019 | 1,201 | 251 | -433 | 3,708 | 430 | 2,396 | 3,378 |
| 2025 | 5,816 | 856 | 1,258 | 224 | -626 | 3,588 | 395 | 2,281 | 3,093 |

(The run.py table also carries 2020's three interim quarter-ends; the public WillScot record starts with the SPAC
combination of November 2017, and its FY2015 to FY2017 figures are the predecessor's, with operating losses of $20.8M,
$3.2M and $58.3M, 10-K FY2019, `0001647088-20-000010`.)

**What the figures say.** (1) The 2020 Mobile Mini merger doubled the balance sheet with stock: 106,426,721 shares
issued at $12.53, a $1,353M purchase price, of which goodwill and intangibles took about $1.3B (10-K FY2020,
`0001647088-21-000015`, Note 2). (2) From 2021 the equity raised was handed back and more: about $2.31B of buybacks
(62.7M shares at an average of about $37; by year $28.4, $38.1, $43.7, $37.9, $24.8, $20.7 in H1 2026) took the
cover count from 229.05M (Feb 2021) to 181.19M, while debt rose $1.1B. Equity fell from $2,141M to $856M and tangible
equity went from +$474M to -$626M; retained earnings are a deficit of $800M. (3) Receivables ran at 17% to 23% of
revenue; the 2025 10-K records a $63.5M increase in receivable write-offs taken against revenue, ‘primarily driven by
aged receivables that we deemed uncollectible’, a provision for credit losses of $58.3M, $55.4M and $49.7M in 2025,
2024 and 2023 (cash-flow statement), and the auditor named the $61.8M allowance a critical audit matter. Revenue
booked in earlier years has been coming back out. (4) Cash is near nil ($9M to $25M); liquidity is the ABL ($1.5B
available, 10-Q Q2 2026). (5) Rental equipment, net, barely moved from 2020 to 2025 despite about $1.5B of gross fleet
purchases and $1.2B of acquisitions, and the 2025 write-off says the book carried fleet that was not worth its
carrying value.

**What they do not say and cannot say.** They do not separate maintenance from growth capital; they cannot say what
the fleet would fetch, and the 2025 write-off shows the carrying value was optimistic by at least $311M; the acquired
fleets (ModSpace 2018, Mobile Mini 2020) were stepped up to fair value, so any return on tangible assets for WSC is
depressed relative to a rival carrying its fleet at old historic cost. That last point matters at Q2.

### Units, utilization and rates (the key variables)
Company figures; the basis changes with discontinued operations and segment restatements, so each row is taken from
the earliest 10-K that states it on the continuing basis.

| year | modular avg units on rent | modular utilization | modular monthly rate | storage avg units on rent | storage utilization | storage monthly rate | source |
|---|---|---|---|---|---|---|---|
| 2018 | 70,257 | 71.6% | $552 | n/r | n/r | n/r | 10-K FY2018 `0001628280-19-002990` (ModSpace from Aug 2018) |
| 2019 | 91,682 | 72.0% | $614 | 16,878 | 65.8% | $120 | 10-K FY2019 `0001647088-20-000010` (legacy WillScot) |
| 2020 | 95,206 | 69.5% | $671 | 72,238 | 74.2% | $142 | 10-K FY2022 `0001647088-23-000014` (Mobile Mini from Jul 2020) |
| 2021 | 101,304 | 69.2% | $772 | 135,775 | 80.1% | $154 | 10-K FY2022 |
| 2022 | 104,808 | 68.5% | $905 | 169,565 | 86.8% | $192 | 10-K FY2023 `0001647088-24-000030` |
| 2023 | 98,650 | 64.4% | $1,099 | 156,558 | 73.4% | $235 | 10-K FY2024 `0001647088-25-000009` |
| 2024 | 94,780 | 61.9% | $1,185 | 126,455 | 60.0% | $266 | 10-K FY2025 |
| 2025 | 89,548 | 59.9% | $1,243 | 106,784 | 51.5% | $286 | 10-K FY2025 |
| Q2 2026 | 89,835 | 69.2% | $1,272 | 100,270 | 57.3% | $287 | 10-Q `0001647088-26-000056` (utilization after the fleet removal) |

From 2022 to 2025 modular units on rent fell 14.6% while the modular rate rose 37%; storage units on rent fell 37%
while the storage rate rose 49% (the 2023 storage rise was 19.3% excluding acquired climate-controlled units, 10-K
FY2023). Value-added products (VAPS) revenue was $397.5M in 2025 against $397.6M in 2024, flat (10-K FY2025 MD&A).
The Q2 2026 utilization jump is the denominator: 53,000 units were removed from the fleet count.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether the buyer would be content to own WSC "if the market closed for five years"
**[M1997-109]**, and the answer turns entirely on whether the castle and the debt hold through a construction cycle,
since the price has halved from the buyback prices the company itself paid. The market serves and does not instruct:
the fall from about $44 to $17 "just tells us prices" **[M2006-077]** and is not evidence either way. Who is paid to
tell you: the company's headline figures are Adjusted EBITDA, Adjusted Free Cash Flow and an ROIC that excludes goodwill
and intangibles and adds back real-estate-exit depreciation (Q2 2026 release, `0001647088-26-000054`), and 70% of the
executives' cash bonus is set on Adjusted EBITDA (DEF 14A, `0001647088-26-000021`); the analyst reads the cash-flow
statement instead. Margin of safety: "if you have to actually do it on" a pencil it is "too close to think about"
**[M1996-084]**, which bears on the computation at the end. The analyst's habit: "What do I not know that I need to
know?" **[M1999-129]**.

**Contrary evidence, written down as found** **[M1997-127]**: (i) `tools/run.py` omitted fleet capex and so showed an
owner-cash yield near 20%; the true all-in figure is about 11% on A and 3% on B. (ii) Rental depreciation exceeded net
rental capex in four of five years while units on rent fell, and $311M of fleet was then written off. (iii) Receivable
write-offs taken against revenue rose $63.5M in 2025. (iv) Units on rent fell for three straight years while rates
rose 37% to 49%, the pattern **[M2001-087]** describes, but the same years saw US non-residential starts fall, which the
company names as the cause. (v) The nearest rival held modular utilization at 77% to 80% from 2019 to 2024 while WSC's
fell from 72% to 62% (Q2 below). (vi) The company bought $2.31B of its own stock at about $37 a share with no stated
price limit, and the stock is $17. (vii) The CEO, the chair, the CFO (2025), the chief accounting officer (departed
August 2025, successor from January 2026), the chief legal officer and the CIO all changed between October 2024 and February 2026 (the 8-Ks listed in
Step 0). (viii) For the business: pricing held through a volume decline, leasing revenue turned up in Q2 2026 (+1.5%),
modular activations grew three quarters running, and the FTC's resistance to the McGrath merger implies a market
concentrated enough to worry an antitrust agency (8-K `0001647088-24-000149`).

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin if bought without borrowed money and sized within what the buyer
can lose: "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target's own leverage (3.7x
net debt to Adjusted EBITDA, all of it secured) is a Q9 matter, not the buyer's conduct, and Q9 is not reached.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding means "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**. The business: about 304,000 units at the end of 2025 (128,000
  modular, 176,000 storage) rented from about 260 branches to over 85,000 customers in 15 end markets, ‘no single
  customer accounted for more than 2% of revenues’, average modular lease about three years (10-K FY2025, Item 1).
  The product does not change: ‘Steel containers have a long useful life with no technical obsolescence’ (same).
- **Key variables, and how predictable** **[M1998-044]**: units on rent (cyclical, tied by the company to
  non-residential construction starts), the monthly rate (has risen every year 2018 to 2026 in the filings read),
  fleet capital to stand still (not disclosed, see Step 0), and the cost and availability of secured credit. The
  first is a cycle, not a forecast nobody can make; the economics of renting a steel box or a site office in ten years
  look much like today's. Technology does not touch it; this is a customer-behaviour forecast **[M2017-019]**, and the
  economic dynamics are the question, "Is there ease of entry?" **[M2011-014]**, which belongs to Q2.
- **Doubt test** **[M2002-092]**: no doubt that the business is inside the perimeter; the doubt is about its castle,
  which is Q2's.
- **VERDICT: IN.** A simple rental business whose product and customers will be recognisable in ten years
  **[M2000-037]**; the hard question is competitive, and the routing sends it to Q2.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now" **[M1995-038]**.

**The castle tests, each with its filing fact.**
1. **Key factors and permanence** **[M1995-038]**. The company's own answer is scale: ‘the broadest fleet portfolio,
   the most differentiated turnkey VAPS, and the most consistent service capabilities across the largest branch
   network’ (10-K FY2025, Item 1). Its own risk factor says the field is ‘highly competitive and highly fragmented’ and
   that ‘some of our competitors may have greater market share, less debt, greater pricing flexibility’; Item 1 adds
   ‘new competitors emerging on a regular basis’ (10-K FY2025, `0001647088-26-000011`). Named rivals: McGrath
   RentCorp, United Rentals, ATCO Structures & Logistics, Satellite Shelters ‘and numerous other regional and local
   companies’ (10-K FY2023, `0001647088-24-000030`).
2. **Would it stand without the lord?** The business is a fleet and a branch network; no superstar. Passes on its face.
3. **The money test** **[M2011-015]**: the attacker with money came. United Rentals bought General Finance (Pac-Van,
   ‘a leading provider of mobile storage equipment and modular office space’) in May 2021, and ‘Prior to the General
   Finance acquisition, we did not rent material amounts of such equipment’ (URI 10-K FY2021, `0001067701-22-000008`);
   mobile storage and modular office space were 3% of URI's rental revenue in each of 2023 to 2025 (URI 10-K FY2025,
   `0001067701-26-000007`), on the order of $0.4B against WSC’s $1.75B of leasing revenue (10-K FY2025). A storage container is a
   used ISO box bought and remanufactured (10-K FY2025, Item 1): "anything you do, your competitors can copy"
   **[M1996-017]**. URI's cost of funds and scale are the edge the rows name in leasing: "pure money-type leasing is not
   an attractive business for us when we’ve got other people with a lower cost of funds" **[M2016-029]**.
4. **Pricing power and the agony** **[M2005-020]**. For the castle: modular rate $614 (2019) to $1,243 (2025) to $1,272
   (Q2 2026); storage $142 (2020) to $286; leasing revenue rose while units fell. Against: rates rose while units on
   rent fell three years running and utilization fell to 59.9% and 51.5%; the test that matters is "maintain or
   increase market share" **[M2000-031]**, and the failure form is "pushed their pricing too far to the point that they
   lost market share" **[M2001-087]**. The company attributes the decline to the construction cycle and higher rates;
   the filings read do not let the analyst separate the two.
5. **Unit volume** **[M1999-054]**: down 14.6% (modular) and 37% (storage) from 2022 to 2025 (Step 0 table). Volume
   decline is not by itself a fail **[M2015-066]**; it is the evidence to be explained.
6. **The low-cost position** **[M2018-043]**: not shown. On the same metric over the whole span (below), the largest
   operator earns less on its tangible assets than its smaller listed rival and far less than United Rentals.
7. **Brand.** The Mobile Mini trade name was retired and impaired $132.5M in 2024 (10-K FY2024, MD&A,
   `0001647088-25-000009`); customers rent space, not a name. No instance found in the filings read of a customer
   asking for WillScot by name.
8. **Would the customer choose it over the low bid?** **[M2017-009]**: the company's own risk factor, ‘some of our
   competitors seek to obtain market share by reducing prices’ (10-K FY2025, risk factors), describes a market where
   the low bid exists; the 2026 recovery is credited to ‘large project activity’ and ‘strong win rates’ (Q2 2026
   release), i.e., won bids.
9. **Ask the competitors** (the row below, from their own filings).
10. **Widening or narrowing** **[L2005-010]**: in December 2025 the board approved exiting about 725 acres of leased
    real estate, 115 branch and drop-lot locations, about 25% of leased acreage, and abandoning about 51,000 units
    (8-K `0001753926-25-001926`). The company says market coverage is kept. Whether this is a moat being widened or
    "A moat that must be continuously rebuilt" **[L2007-005]** is not decided by the filings.
11. **What could destroy or reduce it, five to fifteen years out** **[M2000-014]**: a second competitor with lower
    funding costs (URI) pricing for share; a long non-residential construction trough with 3.7x secured leverage.

**The competitor row** (same metric from each company's own filings: operating income over tangible assets, i.e.
total assets less goodwill and intangibles, at year-end; first-filed XBRL from each 10-K; `roic.py` in the working
folder; for return on tangible assets as the measure, see **[M2011-060]**).

| company | span | operating income / tangible assets, by year | span mean | operating margin range |
|---|---|---|---|---|
| WillScot (WSC, CIK 1647088) | 2019-2025 | 4.6, 4.7, 8.7, 11.6, 14.8, 5.8, 4.2 | **7.8%** (9.9% with the 2024 deal fee, 2024 impairment and 2025 fleet write-off added back) | 8.0% to 28.5% |
| McGrath RentCorp (MGRC, CIK 752714) | 2016-2025 | 7.3, 8.5, 9.9, 11.1, 11.3, 9.3, 10.8, 10.4, 12.9, 12.3 | **10.4%** (11.2% for 2019-2025) | 18.7% to 26.8% |
| United Rentals (URI, CIK 1067701) | 2016-2025 | 17.7, 15.0, 16.3, 16.7, 14.9, 16.1, 18.3, 20.2, 19.7, 17.8 | **17.3%** (17.7% for 2019-2025) | 21.1% to 27.8% |
| Mobile Mini (pre-merger, CIK 911109) | 2012-2019 | 7.9, 5.9, 7.5, 3.1, 9.2, 8.4, 2.9, 11.4 | **7.0%** | 6.0% to 25.1% |
| Target Hospitality (TH, CIK 1712189) | 2019-2025 | 10.9, 1.1, 9.7, 26.6, 41.0, 17.2, -7.7 | 14.1%, swinging with one government contract | -10.8% to 42.7% |

Modular utilization, the rival's own figures: McGrath's Mobile Modular segment, cost-based average utilization 79.2%
(2019), 77.2% (2020), 76.2% (2021), 79.1% (2022), 79.7% (2023), 77.5% (2024), 73.0% (2025), with its monthly rental
rate as a share of equipment cost rising from 2.41% (2019) to 2.83% (2025), and its segment operating income on
average equipment cost rising from 5.9% (2016) to 10.6% (2020) to 12.7% (2025) (MGRC 10-Ks FY2016
`0001564590-17-002846`, FY2018 `0001564590-19-004446`, FY2020 `0001564590-21-007546`, FY2022
`0000950170-23-003738`, FY2023 `0000950170-24-017876`, FY2025 `0001193125-26-071463`). WSC's unit-based modular
utilization over the same years: 72.0%, 69.5%, 69.2%, 68.5%, 64.4%, 61.9%, 59.9%.

**What the row shows and does not show.** Over the whole span the largest operator earned about 7.8% before interest
and tax on tangible assets (9.9% with three discrete charges added back), below its smaller direct rival (10.4% to
11.2%) and about half of URI (17.3% to 17.7%), and the predecessor Mobile Mini earned 7.0% across 2012 to 2019. The
rival held its utilization while WSC's fell and WSC raised price faster. If those figures meant what they appear to
mean, the scale castle the company claims would be shown not to be there, and "one competitor is frequently enough to
ruin a business" **[M2012-108]**. But three confounds stand between the figures and that conclusion, each knowable and
none resolved by the filings read: (a) WSC's tangible assets carry fleets stepped up to fair value in the 2018 and 2020
acquisitions, while McGrath's carry old historic cost, which by itself depresses WSC's ratio; (b) utilization is
unit-based at WSC and cost-based at McGrath, and McGrath's Mobile Modular leans on classroom rentals that do not follow
non-residential construction; (c) URI's 17% is a whole equipment-rental company, of which storage and modular are 3%.
The castle is neither shown standing (no cost edge, no brand, an attacker with money inside the walls, volume down while
price rose) nor shown filling in on a like-for-like basis.

- **VERDICT: TOO HARD (WORK).** The castle's future cannot be judged on the evidence read: "when we see a moat that’s
  tenuous in any way [...] it’s just too risky. We don’t know how to valuate that" **[M2000-019]**; a castle whose
  future cannot be judged closes in the "too hard" pile **[M2006-013]**. The cause is WORK, not NATURE: the deciding
  question (is the 2022 to 2025 volume loss share lost to rivals, or the construction cycle on a castle that holds?)
  is knowable and important **[M2006-076]** from primary documents: the quarterly unit and utilization series of WSC
  and McGrath, a return on a common fleet-cost basis, and URI's equipment-type revenue. Industry insiders write down
  forecasts of utilization and rate; this is not the forecast "They would say, “That’s too hard.”" describes
  **[M2000-105]**. The research pass, steps 1 and 2, is written at the end of this file and is not run.

---
## Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED.
## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED. (The balance sheets were read in Step 0.)
## Q5: WHO RUNS IT. NOT REACHED.
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7: WHAT IS IT WORTH. NOT REACHED.
## Q8: BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9: COULD IT RUIN US. NOT REACHED.
## Q10: THE FAT PITCH. NOT REACHED.
## Q12 (optional): NOT ASKED (the run closed at Q2).

Facts already gathered that the later questions will meet if the research pass reopens the file, recorded here
without weight or verdict: Adjusted EBITDA is the headline and sets 70% of the bonus; ‘Adjusted Free Cash Flow’ and an
ROIC excluding goodwill are featured (Q2 2026 release); restructuring charges in 2024 and 2025 and a $180M termination
fee in 2024; receivable write-offs and a credit-loss allowance named a critical audit matter (Q4). A 2021 award earned
on stock-price thresholds from $42.50 to $60.00 (‘stock price attainment of the $45.00 per share threshold’, ratified
2023), a new CEO from 2026-01-01, an executive chair since 2025-09-04 with a $175,000 housing allowance, the 2026 PSUs
measured on relative TSR, and directors and officers owning 3% (DEF 14A) (Q5 and Q6 Part B). $2.31B of buybacks at
about $37 a share under a $1B authorization with no price named, dividends from 2025 at $0.07 a quarter, and the
2020 all-stock merger at $12.53 a share (Q6 Part A). $3,495M of secured debt, maturities from August 2028, an ABL with
$1.5B available, 90% of the debt fixed after swaps (Q9).

---
## COMPUTATION - NOT A CLEARANCE: value range, fair price and cheap price, at the owner's request
The file closed TOO HARD at Q2. What follows is arithmetic made at the owner's request; it carries no entry language and
clears nothing (operator rule 3). Construction per the Q7 CONVENTION (Part VI): five-year mean of owner cash
2021-2025, carried for ten years at the growth shown and capped, then zero nominal growth, discounted at the 30-year
Treasury of 5.63% **[L2000-021]**; the two ends are no growth and the capped shown growth **[L2000-024]**.

- **Growth shown** on aggregate owner cash A: endpoint 14.9% a year (2021 to 2025), log-linear 12.4%. Both exceed the
  discount rate; the growth came with falling units and with $1.2B of acquisitions that A does not charge, and the base
  year includes discontinued units, so the endpoint growth is the kind **[L2005-003]** warns of. **CONVENTION of this
  run:** with Q3 not reached, the shown growth is capped at the sovereign rate (5.63%), so that no case grows faster
  than it is discounted **[M1997-095]**; rationale: the Q7 convention requires a Q3 cap and none was set.
- **(a) VALUE RANGE** (per share, 181.19M shares):
  - **On A (all capital spending deducted, as filed), the convention's range: $33.75 (no growth) to $52.75 (growth
    capped at 5.63%).** Width 1.6 to 1.
  - Whole-cycle variant (the window holds an abnormal year, 2024's $225.7M deal fee and costs, and spans the 2022-2023
    construction peak and the 2025 trough): on A2, **$38.18 to $59.67.**
  - The capital-measure variants, shown because Q3 never chose between them: depreciation variant D, $24.83 to
    $38.81; B (acquisitions counted as capital), **$10.31 to $16.12.** Across the variants the range runs $10.31 to
    $59.67, about 5.8 to 1, wider than the three-to-one line at which the convention would close Q7 TOO HARD
    **[L2000-025]**. The choice of capital measure decides the answer, which is the Q3 question.
- **(b) FAIR PRICE**, the price at or below which the central case clears the floor of about 10% pre-tax
  (CONVENTION, Q7; **[M2003-149]**). Central case: A at half the capped growth (2.8% a year for ten years, then zero).
  **Fair price $23.02** (no-growth case on A: $19.00; on A2 central: $26.04; on D central: $16.94). Tax treatment:
  owner cash is after WillScot's own interest and cash taxes; the floor is read as pre-tax to the buyer, i.e. before
  the buyer's own tax on the return, and no gross-up for corporate tax is applied.
- **(c) CHEAP PRICE**, below which no pencil is needed **[M1996-084]**. Rule of this run (CONVENTION): the price at
  which the no-growth case clears the 10% floor on every capital-measure variant shown, i.e. on the most conservative,
  B. **Cheap price $5.81.** (On D alone it would be $13.98.)
- **Against the price of $17.07:** below the fair price on A ($23.02) and A2, above it on D's central case ($16.94),
  three times the cheap price. The expected return at $17.07 is 11.1% (no growth) to 13.2% (central) on A, 8.2% to 9.9%
  on D, and 3.4% to 4.3% on B. Whether the price clears the floor depends on which capital measure is true: a pencil
  case **[M2009-005]**, not a screamer, even before the castle is judged.

---
## THE BOX
**TOO HARD (WORK) at Q2.** The castle's future cannot be judged on the evidence read: the leader shows no cost edge,
no brand, an attacker with money in its market, and three years of volume loss under rising prices, but the
like-for-like comparison with McGrath that would show the castle filling in or standing is not yet made. The research
pass opens (steps 1 and 2 below; not run). Computation only: a range of $33.75 to $52.75 on all-in owner cash
(5.8 to 1 across capital measures, $10.31 to $59.67), fair $23.02, cheap $5.81, against $17.07.

---
## RESEARCH PASS, for the TOO HARD (WORK) at Q2 (Part VII). Steps 1 and 2 only; not run.
*(CONVENTION in its form, section VI of the framework. In the framework the pass is a separate dated file; the brief
for this run confines writing to this file and the working folder, so the two steps are written here.)*

### Step 1: What do I not know that I need to know? **[M1999-129]**
Each marked knowable or not **[M2006-076]**.
- **K1. Share or cycle.** Did WSC lose modular and storage volume to rivals from 2022 to 2025, beyond what the
  non-residential construction cycle explains? *Knowable* from the companies' own quarterly filings.
- **K2. Scale economics on a common basis.** Does the largest operator earn more, before interest and tax, on the
  historic cost of its fleet than its smaller rival does on the same basis? *Knowable*: WSC discloses gross rental
  equipment cost (Note 7), McGrath discloses average rental equipment at cost and segment operating income.
- **K3. Storage pricing through a downturn.** Has portable-storage pricing ever held through a volume downturn without
  the volume failing to return, i.e. is storage a commodity box priced by the low bid? *Knowable* from Mobile Mini's
  10-Ks 2012 to 2019 (its 2015-2016 energy downturn) and WSC's 2026 quarters.
- **K4. The attacker.** Is United Rentals' storage and modular business growing while WSC's leasing revenue falls?
  *Knowable* from URI's equipment-type revenue table (percent of rental revenue) and its rental revenue.
- **K5. Industry market shares by product and region.** *Not knowable* from primary documents: no instance found in
  the filings read of a share figure, and trade-association data are not public filings. Recorded and set aside (form
  (c)); the close is decided on K1 to K4.

### Step 2: the evidence, where it is, its span and source fixed now, and the single fact that would close OUT **[M1998-144]**
- **K1.** Evidence: WSC average modular and storage units on rent and utilization by quarter; McGrath Mobile Modular
  average rental equipment on rent and utilization by quarter, with its stated education share. Span: Q1 2019 to the
  latest 10-Q (Q2 2026, and Q3 2026 if filed when the pass runs). Source: WSC and MGRC 10-Ks FY2019 to FY2025 and their
  10-Qs. **OUT fact:** McGrath's Mobile Modular average rental equipment on rent, deflated by its own stated new-unit
  cost change or measured in its stated units where given, rose from 2022 to 2025 while WSC's modular average units on
  rent fell.
- **K2.** Evidence: operating income (as reported, and with the 2024 and 2025 discrete charges shown separately)
  divided by average gross rental equipment at cost, for WSC; Mobile Modular segment operating income divided by its
  average rental equipment at cost, for McGrath. Span: 2019 to 2025, every year, mean over the whole span (never one
  year; after-depreciation earnings set against a stock of fleet cost, never against gross capex). Source: WSC 10-K
  Note 7 (rental equipment) and income statements FY2019 to FY2025; MGRC 10-K segment tables FY2019 to FY2025.
  **OUT fact:** WSC's 2019-2025 mean is below McGrath Mobile Modular's 2019-2025 mean on that basis.
- **K3.** Evidence: Mobile Mini storage units on rent, utilization and yield 2012 to 2019; WSC storage units, rate
  and utilization by quarter Q1 2024 to the latest 10-Q. Source: Mobile Mini 10-Ks FY2012 to FY2019 (CIK 911109); WSC
  10-Qs. **OUT fact:** WSC storage average units on rent in the latest quarter are below the same quarter a year
  earlier while the storage rate is above it, for the fourth consecutive year.
- **K4.** Evidence: URI rental revenue and the mobile storage and modular share of it, FY2021 to FY2025; WSC leasing
  revenue over the same years. Source: URI 10-Ks FY2021 to FY2025 (equipment-type table); WSC 10-Ks. **OUT fact:**
  URI's mobile storage and modular rental revenue in FY2025 exceeds its FY2022 figure while WSC's leasing revenue in
  FY2025 is below its FY2022 figure.

**How step 4 closes.** IN at Q2 only if no OUT fact is found and K2 shows WSC at or above McGrath on the common basis
(scale shown as an advantage); the run then resumes at Q3 with the facts listed under Q12 above waiting for Q4 to Q6.
OUT if any single OUT fact is found. TOO HARD (NATURE) if no OUT fact is found but K2 leaves WSC below McGrath or the
answers otherwise leave the castle's future unjudgeable; the pass does not close TOO HARD (WORK) a second time
**[M2008-086]**, and a pass that ends unsure ends TOO HARD (NATURE) **[M2002-092]**. If the operator holds WSC, a second
session runs steps 3 and 4 blind from these two steps and the two closes are compared before either is acted on.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. **Not committed after each:** the brief
      for this run forbids commits, so the write-early commits were not made (declared, not a pass).
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, see below); every filing fact has its
      accession; numbers are from filings or from the scripts in the working folder, or are labelled CONVENTION.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance, and the value figures are headed
      COMPUTATION - NOT A CLEARANCE.
- [x] Owner cash after every real cost, from the cash-flow statement, never a net-income proxy (operator rule 5); the
      tool's omission of fleet capex was found and corrected, not used; the sovereign is from the US Treasury; the price
      is an aggregator quote, flagged.
- [x] Contrary evidence was written down as found **[M1997-127]** (foundations list, eight items).
- [x] Not a point-in-time run; no anchor rule applies. No v4 id is cited.
- [x] Only the arithmetic lines of `tools/run.py` were used, and its capex line was rejected.
- [x] `python tools/check_framework.py` PASS after writing (2026-10-05: test runs, phantom ids in 0 files; v5 ledger
      4279/4279 verbatim; v5 scope OK). A separate script (`check_ids.py`, working folder) confirmed: no E-ids; every
      M, L and R id cited (42 distinct, 49 citations) is in `principle_ledger_v5.csv`; every double-quoted fragment
      beside an id is in that id's row.
- Weak points the operator should know: the competitor return row is on year-end tangible assets from first-filed
  XBRL, not on averages, and WSC's 2020 and 2021 figures are as first reported (including units later discontinued);
  the confounds named under Q2 are the reason the box is TOO HARD rather than OUT, and a reader who weighs them less
  would close OUT.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Q2 has no rule for comparing returns across purchase-accounting bases.** The whole-span peer comparison the brief
   asks for is biased whenever one company's fleet was stepped up to fair value in acquisitions and the other's sits at
   historic cost; Q2's test 9 and the competitor row say "same metric", which is not the same economics. This run
   named the confound and sent it to the research pass (K2) rather than resolve it by choice.
2. **TOO HARD (WORK) against OUT is a judgment the text leaves open when the evidence leans one way but carries named
   confounds.** "A castle shown open on the evidence closes OUT" does not say how strong "shown" must be. I closed TOO
   HARD because each confound is knowable; another analyst could close OUT on the same row.
3. **Q7's range convention is silent on which capital measure feeds it when acquisitions buy the fleet.** "Deducts all
   capital spending" could mean A (investing capex) or B (capex plus acquisitions); the gap here is 3.3 to 1 in the
   input and moves the range from $33.75 to $10.31 at the bottom. The convention points to Q3 for the maintenance
   judgment, and when Q3 is not reached the computation cannot choose. I showed all variants and capped growth at the
   sovereign as this run's own CONVENTION.
4. **`tools/run.py` is unsafe for rental companies.** Its capex column reads only `PaymentsToAcquirePropertyPlantAndEquipment`
   and misses `PaymentsToAcquireEquipmentOnLease` (the fleet), overstating owner cash by about $250M a year here and
   printing a yield of about 20% where the true all-in figure is about 11% (A) or 3% (B). The tooling test ("same
   number sooner") fails silently for any lessor; the fleet-purchase tag should be read as capital.
5. **Operator rule 3 spells its heading with an em dash; the brief forbids em dashes.** Written "COMPUTATION - NOT A
   CLEARANCE", as many September runs did.
6. **The framework's research pass is a separate file; the brief confines this run to one file.** Steps 1 and 2 are
   written here; the operator may move them.
