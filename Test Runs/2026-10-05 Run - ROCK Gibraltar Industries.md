# Company Run: Gibraltar Industries, Inc. (NASDAQ: ROCK), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Filled top to
bottom from `Test Runs/_TEMPLATE - Company Run.md` (copied to this dated name before any fetch); every judgment cites a v5
ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run and later
questions are marked NOT REACHED. Working folder: `Test Runs/_research 2026-10-05 ROCK/` (filings as text, `calc.py`,
`peer_margins.py`, `series.py`, `ids.py`, `fetch.py`). Em dashes in the template's headings are replaced by colons in
this file (owner's standing rule).

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is barred to this run by its blind rule, so
whether the operator holds ROCK is unknown to the analyst.

**BLIND RULE AND CONTAMINATION, declared.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`, the
register, the prepped reading list, any other run or research file about ROCK, other companies' 2026-10-05 run files, the
unadopted small-cap gaps case. Seen without opening: (a) the git status and recent commit subjects in the session header,
which name three other v5 runs of record (LKQ, SCSC, KSS), each "OUT at Q2" with a value range, a "fair about" and a
"cheap about" price, and the untracked file names of three other 2026-10-05 runs (ANDE, LCII, SLVM); (b) a glob for
`*ROCK*` in `Test Runs/` that matched only the file names of a BLK run and an AROC run (not opened; neither is about this
company); (c) the memory index line "57 gate-clearers, nothing buyable". None of these says anything about Gibraltar.
The commit subjects show a pattern (OUT at Q2 on price competition); I name it here so that it cannot steer the Q2 verdict
silently, and the Q2 verdict below departs from it on the evidence.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $40.32 (close 2026-10-05; Yahoo chart via `tools/sources.py`; **aggregator, live quote only, flagged** per
  operator rule 5). Context, same source: $59.15 on 2025-11-14, $47.14 on 2025-11-17 (the first close after the OmniMax
  agreement), 2026 low $33.82 (2026-05-19).
- **Shares by class** from the latest filing's cover: 29,683,889 common, $0.01 par, one class (10-Q for the period ended
  2026-06-30, filed 2026-08-05, accession `0000912562-26-000147`, cover count as of 2026-08-03; `python
  Screens/cover_shares.py ROCK`). The balance-sheet line "34,698 shares issued and outstanding" is the issued count;
  5,015 thousand are in treasury, so about 29,683 thousand are outstanding, which agrees with the cover. `tools/run.py`
  prints 34.482M as "balance-sheet count"; it is the issued figure and was not used.
- **Market cap:** 29.683889M x $40.32 = **$1,196.9M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, US Treasury daily par yield curve, 30-year, 2026-10-02
  (`tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-26, `0000912562-26-000025`: Items 1, 1A, 5, 7, 7A, 8 (statements; notes 5, 6, 7, 8, 9,
    16, 17, 18).
  - 10-Q Q2 2026, filed 2026-08-05, `0000912562-26-000147`: statements, notes 5 to 14, MD&A, Part II.
  - DEF 14A, filed 2026-04-06, `0000912562-26-000083`: CD&A, Summary Compensation Table, pay-versus-performance note,
    ownership tables.
  - 8-Ks: 2025-11-17 `0001140361-25-042426` (OmniMax agreement and Ex. 99.1 press release); 2026-02-02
    `0001140361-26-003087` (closing, credit agreement); 2026-04-17 8-K/A `0001140361-26-015303` (Ex. 99.1 OmniMax audited
    statements FY2025 and FY2024; Ex. 99.2 pro forma); 2026-04-03 `0000912562-26-000080` (special bonuses); 2026-02-23
    `0000912562-26-000018` and 2026-07-16 `0000912562-26-000141` (Renewables sales); 2026-08-05 `0000912562-26-000145`
    Ex. 99.1 (Q2 2026 earnings release); 2026-01-22 `0000912562-26-000016` (HSR).
  - History: 10-Ks FY2016 `0000912562-17-000008`, FY2018 `0000912562-19-000009`, FY2021 `0000912562-22-000009`, FY2022
    `0000912562-23-000009`, FY2023 `0000912562-24-000012` (segment tables, largest-customer lines, solar trade passages).
  - Competitor filings: Euramax Holdings (OmniMax's predecessor) 10-K FY2014, filed 2015-03-26, `0001026743-15-000011`;
    SSD, NX and ARRY XBRL company facts (accessions in the Q2 competitor row).
- **One figure cross-checked against the filed statement:** net cash from operating activities of continuing operations,
  FY2025, **$137,107 thousand**, read on the face of the consolidated statement of cash flows (10-K FY2025,
  `0000912562-26-000025`). `tools/run.py` prints OCF 2025 as 167.0; the filed statement shows that 167,001 is the total
  including $29,894 thousand from discontinued operations. The tool's OCF line therefore carries the sold Renewables
  business in every year; flagged, and the tool's owner-earnings lines were not used for value.
- **`tools/run.py ROCK` arithmetic lines** (transcription, read against the filings; output saved as
  `run_py_output.txt`): consolidated OCF less SBC less capex 2023 to 2025: 195.7, 146.8, 112.2; five-year version 105.2
  (capex basis), 103.1 (D&A basis); SBC 8.9, 10.0, 8.3; capex 13.9, 17.4, 46.4; D&A 18.7, 19.1, 29.8. These are the
  old company with Renewables, without OmniMax and without its debt; they describe a business that is no longer owned.
  SBC is resolved and complete (the only stock-pay line; 10-K note 9).

### The balance sheets, ten year-ends, read before the income account [M2025-032]
Read "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**, from
`run_py_output.txt` (first-filed XBRL) checked against the filed statements named above. USD millions.

| year-end | equity | goodwill + intangibles | tangible equity | cash | debt | receivables | inventory | retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2017 | 532 | 427 | 105 | 222 | 210 | 145 | 86 | 275 |
| 2018 | 597 | 420 | 177 | 297 | 2 | 140 | 99 | 339 |
| 2019 | 674 | 423 | 251 | 191 | 0 | 148 | 78 | 406 |
| 2020 | 744 | 670 | 74 | 32 | 86 | 198 | 98 | 470 |
| 2021 | 825 | 653 | 172 | 13 | 24 | 236 | 176 | 546 |
| 2022 | 822 | 650 | 172 | 18 | 89 | 217 | 170 | 628 |
| 2023 | 915 | 639 | 276 | 99 | 0 | 225 | 121 | 739 |
| 2024 | 1,048 | 375 (continuing; Renewables reclassified) | 673 | 269 | 0 | 115 | 93 | 876 |
| 2025 | 950 | 559 | 391 | 116 | 0 | 120 | 117 | 831 |
| 2026-06-30 | 891 | **1,700** | **minus 809** | 15 | **1,246** | 260 | 268 | 772 |

What moved and why, from the filings:
- **Equity against goodwill.** For nine years tangible equity stayed between about $74M and $673M; at 2026-06-30 it is
  **negative $809M**: goodwill $939.1M plus customer relationships $620.1M plus other intangibles $140.7M against equity
  of $890.8M (10-Q, `0000912562-26-000147`). OmniMax alone added goodwill of $526.7M (not tax-deductible) and intangibles
  of $640.0M (10-Q note 5). Accumulated goodwill impairments of $133.2M sit behind the goodwill line (10-K note 6), and
  Renewables carried a further $243.4M of impairment and remeasurement before it was sold (10-Q note 13).
- **Debt.** Senior subordinated notes of $210M were retired in 2018; the company carried little or no debt from 2018 to
  2025 ("no outstanding debt as of December 31, 2025 and 2024", 10-K note 8). On 2026-02-02 it borrowed $1.3B of secured
  term loans to buy OmniMax; at 2026-06-30 debt is $1,246.0M gross (TLA $625.0M, TLB $600.0M, revolver $21.0M) against
  cash of $15.1M (10-Q note 7).
- **Cash.** Cash swung from $13M (2021) to $269M (2024) to $15M (2026-06-30). The 2024 pile came from operations and the
  locker sale; it was spent on four 2025 acquisitions ($210.7M) and the OmniMax deal.
- **Working capital against sales.** Inventory doubled in 2021 ($98M to $176M) in the supply squeeze and was released in
  2023 ($41.4M inflow, 10-K FY2025 cash-flow statement), which flatters 2023 operating cash. Receivables and inventory at
  2026-06-30 ($260M, $268M) carry OmniMax and the season.
- **Retained earnings.** Up from $211.7M (end 2016) to $875.9M (end 2024), down to $772.2M at 2026-06-30 after the
  Renewables losses ($141.9M net in 2025, $74.6M net in the first half of 2026).
- **What the figures do not and cannot say** **[M2025-032]**: the OmniMax allocation is provisional and built on Level 3
  inputs (10-Q note 5); "tax credits" of $79.5M sat in accrued expenses at 2025 year-end (credits bought to reduce
  cash taxes, 10-K note 7), so cash taxes in 2025 to 2026 are not the book provision; operating lease liabilities rose to
  $151.2M non-current (10-Q balance sheet) and are outside the debt figure above.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own it "if the market closed for five years"
**[M1997-109]**, which turns the question to the business, not the quotation. The market serves and does not instruct
**[M2006-077]**: the 20% fall on the day the OmniMax deal was announced and the 2026 low are prices, not information about
the castle. Who is paid to tell you: the deal was presented by the company and its two banks (Perella Weinberg, BofA
Securities, 8-K 2025-11-17) at "an effective adjusted EBITDA multiple of 8.4x" that counts synergies and tax benefits; the
analyst reads the seller's audited statements instead. The analyst's habits: look for what is wrong **[M2025-013]**, ask
"What do I not know that I need to know?" **[M1999-129]**, and treat scuttlebutt as a way "to possibly reject your
original hypothesis" **[M1998-144]**.

**Contrary evidence, written down as found** **[M1997-127]** (in the order it was found):
1. 10-K FY2025 Item 1: "The Company's sales process regularly includes a competitive bid process through a customer
   product line review"; the building accessories market is "fragmented and driven mainly by contractor preferences".
2. 10-K FY2025 Item 1A: competition "is based primarily on product functionality, quality, price"; some competitors "may
   have more established brand names"; the company "may not be successful in passing along pricing increases".
3. OmniMax was bought for $1.343B in cash (10-Q note 5) from a private-equity seller (SVP, owner since 2020); its audited
   2025 operating income was $38.5M on sales of $517.6M (8-K/A Ex. 99.1), against "adjusted net sales of $565 million and
   adjusted EBITDA of $110 million" in the deal release.
4. OmniMax under SVP bought Millennium Metals ($69.7M, 2024), Hancock ($107.7M, 2025) and Nu-Ray ($72.9M, 2025) and paid
   SVP $88.5M as return of capital in 2024 to 2025 (8-K/A Ex. 99.1 cash-flow statement): a business assembled for sale.
5. Euramax (OmniMax's predecessor) 10-K FY2014: "Generally, our customers are price sensitive"; its principal
   competitive factors include "the potential proliferation of low-cost competition"; it named Gibraltar as a residential
   competitor; it lost money from continuing operations in each of 2010 to 2014.
6. Sales to the largest customer, a home improvement retailer, by the filer's own percentages: about $195M in 2022 (14%
   of $1,390.0M) to about $136M in 2025 (12% of $1,135.5M), a fall of roughly 30% (the rounding of the percentages puts
   it between about 24% and 35%).
7. Residential segment margin fell from 19.0% (2024) to 16.6% (2025) to 11.4% (first half 2026, 10-Q), the filer citing
   "price/cost alignment" and "early stage production inefficiencies".
8. Renewables: TerraSmart bought for $223.9M (2020, 10-K FY2021); the segment sold in 2026 for about $80M after $243.4M of
   impairment and remeasurement and a $25.0M warranty settlement (10-Q note 13).
9. Market value: $41.65 a share at 2016 year-end, $40.32 now, with $560.5M of earnings retained in between.
10. In April 2026, after the formula bonus paid 25% of target, the committee paid special bonuses topping officers up to
    100% of target for "the Company's multiple acquisitions" and Renewables divestiture work (8-K `0000912562-26-000080`).

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin if it is bought with the buyer's own money and sized so that a total loss
is survivable: "borrowed money has no place in the investor" **[L2014-005]**, and the rule is to be "never going to risk
what we have and need" **[M2012-081]**. The target's own leverage is a Q9 matter, not the buyer's conduct. Nothing in this
run asks for margin or a size that a total loss of this position could make ruinous.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "what the earning power and competitive position will look like in five or 10 years"
  **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**; the first step is the key variables and
  whether they are predictable **[M1998-044]**.
- **The parts that matter** (holding company read by its parts, the framework's CONVENTION at Q1). After OmniMax,
  Residential is 83% of sales (Q2 2026 release, `0000912562-26-000145`): roof trim, flashing, drip edge, soffit, gutters
  and downspouts, metal roofing, roof and foundation vents, mailboxes and cluster box units (10-K Item 1). Agtech
  (greenhouse and canopy design-build, about 12% to 13% of 2026 sales) and Infrastructure (bridge bearings, expansion joints,
  about 5%) are smaller (10-Q note 12).
- **Key variables:** residential repair and remodel volume and housing starts (mailboxes "driven mainly by new
  construction starts", 10-K MD&A); the spread between steel and aluminum coil cost and selling price; the outcome of
  retailer product line reviews; integration of OmniMax. None of these depends on fast-moving technology. The products
  (gutters, flashing, vents, mailboxes) are the same kind of product the filings describe in 2016 and in 2025, and the
  economic dynamics, "Is there ease of entry?" **[M2011-014]**, can be read from the filings.
- **Doubt test** **[M2002-092]**. I understand what moves the Residential economics. The doubt is not whether the products
  will exist in ten years but whether this company will keep its margin among competitors, which is Q2's question. Agtech
  (controlled-environment agriculture, a 2021 to 2023 run of cannabis-customer distress, margins of minus 0.6% to 10.0%,
  10-K FY2023 and 10-Q) is harder to foresee, but at about 12% to 13% of sales it does not decide the whole.
- **VERDICT: IN.** The ten-year economics of a roofing-accessory and rainware maker are a matter of volumes, metal spreads
  and competitive position, all things that are "important and knowable" **[M2006-076]**; no fast technology bars the
  forecast. Passed to Q2.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question is "why is that castle still standing?" and what keeps it standing **[M1995-038]**, starting from the
premise that competitors "will repeatedly assault any business" earning high returns **[L2007-004]**.

**The castle tests, each with its filing fact**
1. **Key factors and how permanent** **[M1995-038]**. The filer names its strengths as breadth, quality, "speed and
   industry-leading service" and well-recognized brands, and says no individual piece of intellectual property is material
   (10-K Item 1). Service and breadth are real but are not shown in the filings to be permanent.
2. **The money test: could a well-funded attacker take it?** **[M2011-015]**. The filer calls the market "fragmented"
   (10-K Item 1); capital needs are small (Residential capex $6.9M to $16.5M a year on $780M to $824M of sales, 2023 to
   2025, 10-K note 16); entrants exist in numbers, since the company itself bought three small metal-roofing makers for
   $108.6M in 2025 and OmniMax bought three more in 2024 to 2025. Euramax named "the potential proliferation of low-cost
   competition" as a principal competitive factor (10-K FY2014, `0001026743-15-000011`). On the filings, money can buy a
   roll-forming line and a regional customer list; whether it can buy the national retail programs is not shown.
3. **Pricing power and the agony before a rise** **[M2005-020]**. The filings narrate the prayer session in most years:
   2021 "multiple price increases" to restore "alignment" after inflation (10-K FY2021); 2023 "price declines related to
   commodity cost reductions" (10-K FY2023); 2026 "price increases to align with rising commodity costs" and "unfavorable
   alignment of price/material cost" (10-Q MD&A). Price follows the metal. Against that, the margin recovered after each
   squeeze, which is what "over time the businesses with strong competitive positions manage to pass through increases in
   raw material costs" **[M2005-017]** describes.
4. **Unit volume.** Residential "ongoing operations" sales fell $13.3M in 2023 and $13.3M in 2025 (10-K FY2023, 10-K
   FY2025 tables); growth came from acquisitions ($60.8M in 2023, $65.3M in 2025, OmniMax in 2026). Organic growth in H1
   2026 was 1%, "the result of price increases" (10-Q MD&A).
5. **The low-cost position.** No filing claims or shows that Gibraltar is the low-cost producer. Euramax claimed to be "an
   integrated low-cost supplier of metal products" to home centers (10-K FY2014) and still earned thin margins.
6. **The brand against the retailer** **[M2001-090]**. About 70% of 2025 revenue went through "retailers, wholesalers and
   distributors" and 40% of OmniMax's through retailers (10-K Item 1). The retailer runs the "product line review"; where
   the retailer sets the terms, "the value of having the brand moves over to the retailer from the product itself"
   **[M2001-090]**.
7. **Would the customer still choose it over the low bid?** **[M2017-009]**. The filer: "The Company's sales process
   regularly includes a competitive bid process through a customer product line review or specific project opportunity,
   and its reputation for quality and on-time delivery make the Company a preferred provider for many customers" (10-K
   Item 1). The first half of that sentence is the low bid; the second is a claim of service, which the rows accept as a
   way out of the commodity class when it holds, as with "the low-cost producer providing very good service"
   **[M2000-146]**.
8. **Ask the competitors** **[M1999-130]**. The nearest competitor on the public record is OmniMax itself, now owned.
   Euramax 10-K FY2014: "Generally, our customers are price sensitive"; large customers "may also become more resistant to
   price changes"; 2011 to 2014 net sales $827M to $934M with operating income (gross profit less selling and general less
   D&A) of about 2% to 3% of sales, and a loss from continuing operations in every year 2010 to 2014. OmniMax audited 2024 and 2025
   (8-K/A `0001140361-26-015303`): operating income $31.7M and $38.5M on $482.2M and $517.6M (6.6%, 7.4%), with "other
   operating charges" of $18.1M and $16.2M in each year.
9. **Widening or narrowing** **[M1999-108]**. Residential (Products) segment operating margin, as filed: 2016 15.1%, 2017
   16.5%, 2018 15.1%, 2019 13.7%, 2020 18.1%, 2021 16.7%, 2022 16.5%, 2023 17.6%, 2024 19.0%, 2025 16.6%, H1 2026 11.4%
   (10-Ks FY2016, FY2018, FY2021, FY2023, FY2025; 10-Q). Over 2016 to 2025 the band is stable, which is the strongest fact
   for the castle. Against it: sales to the largest customer fell about 30% from 2022 to 2025 (contrary evidence 6), and
   the first-half 2026 margin is the lowest since 2019.
10. **What could destroy, modify or reduce it** **[M2000-014]**: losing a national retail program at a line review;
    steel and aluminum tariffs the company "may not be able to pass" on (10-K Item 1A); a housing downturn (no year of the
    2008 to 2011 downturn is in the segment series read here).

**The competitor row** (operating income over sales, as filed; ROCK Residential is a segment figure before unallocated
corporate costs of 2.4% to 4.1% of consolidated sales)

| year | ROCK Residential segment | ROCK consolidated | SSD (Simpson) | NX (Quanex) | OmniMax / Euramax |
|---|---|---|---|---|---|
| 2016 | 15.1% | 7.2% | 16.4% | 3.9% | n/a |
| 2017 | 16.5% | 9.4% | 14.2% | 3.9% | n/a |
| 2018 | 15.1% | 9.4% | 16.0% | 4.0% | n/a |
| 2019 | 13.7% | 9.0% | 15.9% | minus 3.0% | n/a |
| 2020 | 18.1% | 10.4% | 19.9% | 6.5% | n/a |
| 2021 | 16.7% | 7.2% | 23.4% | 7.6% | n/a |
| 2022 | 16.5% | 9.4% | 21.7% | 9.1% | n/a |
| 2023 | 17.6% | 11.5% | 21.5% | 9.8% | n/a |
| 2024 | 19.0% | 13.6% | 19.3% | 4.3% | 6.6% (OmniMax) |
| 2025 | 16.6% | 10.8% | 19.6% | minus 10.6% (impairment) | 7.4% (OmniMax) |

Sources: ROCK 10-Ks as listed in Step 0 (consolidated 2023 to 2025 on the continuing basis of the FY2025 10-K, earlier
years as filed with Renewables); SSD company facts, 10-K FY2025 `0001628280-26-012920` and earlier vintages; NX company
facts, 10-K FY2025 `0001423221-25-000100` and earlier (fiscal years ending October); OmniMax 8-K/A `0001140361-26-015303`;
Euramax 2011 to 2014 about 2% to 3% (`0001026743-15-000011`). Over the whole span ROCK's Residential segment sits below
SSD's consolidated margin in every year but 2017 even before corporate costs are charged to it, and above NX in every year.
Renewables history, for the record: ROCK's Renewables segment margin 12.6% (2020), 4.7% (2021), 6.7% (2022), 9.1% (2023),
then losses and a $243.4M write-down; ARRY (`0001820721-26-000008`) ran 12.9%, 10.9%, minus 2.9%, minus 1.1%, 13.6%,
minus 24.8%, minus 2.3% (2019 to 2025): the solar racking castle was open for both, and Gibraltar's own filings narrate the
AD/CVD circumvention case and the UFLPA import stoppages as the cause of project delays (10-K FY2022, 10-K FY2023). No
listed rival was found for Agtech or Infrastructure (sweep: SEC ticker list for greenhouse, canopy and bridge-bearing
makers; none).

**Weighing the castle.** The facts pull two ways, and the rows give no formula for the width of a moat **[M1999-108]**.
For a standing castle: a decade of 13.7% to 19.0% segment margins on small capital, recovered after every metal squeeze
**[M2005-017]**. For an open one: the filer's own account of a bid at the retailer's line review **[M2017-009]**, a fragmented
market with cheap entry **[M2012-106]**, a competitor that says its customers are price sensitive, a 30% fall in sales to the
largest customer since 2022, and a castle that has just been doubled by buying that competitor, whose own record is GAAP
margins of 2% to 7%. What the filings do not show is the reason the 15% to 19% margins have held: low cost, service, the
retail programs, or the niche lines (vents, USPS-approved mailboxes). That is the factor whose permanence decides the
castle **[M1995-038]**, and on the evidence in hand it cannot be named. A moat that cannot be named is a moat that is
"tenuous in any way", and the rows' answer is that it is "just too risky" to value **[M2000-019]**; the framework routes a
castle whose future cannot be judged to TOO HARD, not OUT. It is not shown to be filling in over the whole span (the margin
band held through 2025), so OUT on the low-bid ground **[L2004-003]** would go beyond the evidence;
"Consequently, price competition in insurance is usually fierce" **[L2004-003]** describes an industry where margins do
not hold, and Gibraltar's Residential margins have held so far.

**The cause.** WORK, not NATURE. The deciding question, whether the combined Residential business holds its margin and its
retail programs against the low bid, is important and knowable **[M2006-076]**: the insiders of a roofing-accessory business
would write down a ten-year forecast (test 5, **[M2000-105]**), there is no fast technology, and the evidence lies in filed
documents not yet read (the largest-customer and segment series back to 2008 through the housing downturn, Euramax's
segment data 2010 to 2014, OmniMax's statements). This is the reader's cause, the work not yet done **[M1994-026]**, not "the nature of the industry would be the roadblock" **[L1993-023]**.

- **VERDICT: TOO HARD (WORK)** **[M2006-013]**. The castle's future cannot be judged from the evidence read; the run closes
  here and the research pass below is opened (steps 1 and 2 only, not run).

---
## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING. NOT REACHED.
Facts recorded for the research pass, not a weighing. Residential segment profit against segment assets: 2024 $148.8M on
$497.3M (29.9%), 2025 $137.2M on $639.4M (21.5%), both including goodwill (10-K note 16); the capital the business needs is
small **[M2010-090]**, while the capital paid is now large: Residential segment assets were $2,249.0M at 2026-06-30 (10-Q
note 12). The incremental purchase: $1,343.4M for OmniMax, whose 2025 operating income before acquisition amortization was
about $71.8M (GAAP $38.5M plus about $33.3M of amortization; depreciation $9.3M, 8-K/A), about 5.3% pre-tax on the price,
about 7.5% with the company's full $29.4M synergy target. "Has it earned high returns on capital?" **[M1995-051]** has two
answers here: yes on the capital the old business needed, no on the capital just added.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED.
Facts recorded for the research pass, not a verdict. (1) The Q2 2026 release headlines "Adjusted EPS $1.11" against GAAP
$0.92 and guides "Adjusted EBITDA" of $310M to $326M, defined to exclude stock compensation, with no reconciliation for the
guidance (Ex. 99.1, `0000912562-26-000145`). (2) Exit activity and restructuring costs appear in every period read (2025 and
2026 in 10-Q note 9; "80/20" restructuring in the FY2016, FY2018 and FY2021 10-Ks) and are excluded from the adjusted
figures as "special charges". (3) OmniMax's "other operating charges" were $18.1M and $16.2M in consecutive years. (4) The
deal release priced OmniMax on adjusted EBITDA. (5) The company gives annual EPS guidance and "reiterated" it in August
2026. Under Q4 these are candidate tells (adjusted earnings featured; recurring charges excluded; EBITDA talk); whether
there is a make-the-numbers habit was not tested (PSUs paid zero for 2025, MICP paid 25%, proxy `0000912562-26-000083`, so
the targets are not always met).

## Q5: WHO RUNS IT? NOT REACHED.
Facts recorded: William Bosway, CEO since January 2019, Chairman since January 2022 (proxy); owns 166,027 shares (about
$6.7M at $40.32) against total pay of $4.73M (2025), $5.23M (2024), $5.53M (2023) (Summary Compensation Table); directors
and officers as a group own 0.9%. TerraSmart and the other 2020 acquisitions ($313.7M of acquisition cash, XBRL company
facts) and the 2026 Renewables exit both fall in his tenure.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
Facts recorded for the research pass: retained earnings rose $560.5M from 2016 year-end to 2026-06-30 while market value
went from about $1,315.3M (31,580,694 cover shares at 2017-02-17 x $41.65, aggregator) to $1,196.9M; $226.4M was spent on
share repurchases and tax-withholding buybacks over 2017 to H1 2026 (XBRL company facts). The 2025 buyback, 914,679 shares
for $60.0M (about $65.60 a share, 10-K MD&A), names no price above which it stops ("at prices the Company deems
appropriate", 10-K Item 5) and sits above the top of the computed range below. OmniMax: all cash, debt-financed, bought
from a financial owner after a two-year add-on spree. Pay: 75% of the annual bonus on "Adjusted Net Sales for MICP" and
"Adjusted EPS for MICP"; PSUs on one-year ROIC that excludes the year's acquisitions and, for 2025, the discontinued
Renewables (proxy); special top-up bonuses for acquisition work after a 25% formula payout (8-K 2026-04-03).

## Q7: WHAT IS IT WORTH? NOT REACHED. **COMPUTATION: NOT A CLEARANCE.**
*Reported at the owner's request. No entry language; the file closed at Q2.* Arithmetic in `calc.py`.

**What is valued.** The business now owned is not the business of the five-year window: Renewables is sold, OmniMax was
added, and $1,231M of net debt replaced a debt-free balance sheet. CONVENTION of this run: value the operating business
before interest (legacy continuing operations plus OmniMax) and subtract net debt at 2026-06-30 ($1,246.0M gross less
$15.1M cash = $1,230.9M; leases and the small net liabilities of the sold Renewables excluded). Rationale: a five-year
average of owner cash to the old debt-free equity would count cash that now goes to the lenders.

**Owner cash, after every real cost, before interest (pre-tax, USD millions).**
- Legacy continuing operations, 2021 to 2025: operating income (segments less unallocated corporate, 10-Ks FY2021, FY2023,
  FY2025) 76.8, 104.9, 120.6, 139.7, 122.8; average 113.0; plus amortization of purchased customer relationships and trade
  names (2023 6.2, 2024 6.3, 2025 15.3; 2021 and 2022 not filed on the continuing basis, taken at 6.0 as a CONVENTION of
  this run), since such amortization arises "through purchase-accounting rules" **[L2012-003]**: average EBITA 120.9. All
  capital spending deducted: depreciation less capex averaged minus 12.6 over 2023 to 2025 (2025 includes two facilities
  bought), giving **108.3**; depreciation variant **120.9**. Stock pay is inside operating income (8.3 to 10.0 a year).
- OmniMax, 2024 and 2025 (8-K/A audited; five years are not on file): EBITA 52.9 and 71.8, average 62.4; all-capex
  **60.8**; depreciation variant **62.4**. Its recurring "other operating charges" are kept as costs. No synergy is
  counted: "we never count on synergies" **[L2016-008]**.
- Combined: **169.1** (all capex) to **183.3** (depreciation variant). Less interest of about $80M (Q2 2026 interest
  $20.965M x 4, less about $4M of non-cash issuance-cost amortization; CONVENTION of this run): **$89.1M to $103.3M
  pre-tax to the equity**, **$67.7M to $78.5M after tax** at 24% (CONVENTION: the 2023 to 2025 continuing effective rates
  were 26.1%, 21.0%, 22.9%), **$2.28 to $2.65 a share**.

**Growth shown, and its cap.** The literal growth of legacy operating income over the window is 12.4% a year (76.8 to
122.8), but 2021 was a depressed base year and much of the rise was bought: "a base year in which earnings were poor can
produce a breathtaking, but meaningless, growth rate" **[L2005-003]**. Capped by Q3 (acquired growth is paid for with
capital the owner-cash figure does not deduct), the shown growth is taken as 2022 to 2025 excluding the 2025 acquisitions'
own $14.5M of operating income (10-K note 5): 104.9 to 108.3, **1.1% a year**.

**Value range, at the 5.63% sovereign, ten years at the shown growth then zero nominal growth, after tax at 24%, less net
debt, per share:**

| case | all capex | depreciation variant |
|---|---|---|
| no growth | **$35.44** | $41.89 |
| shown growth, capped (1.1%) | **$42.44** | $49.47 |
| whole-cycle variant, no growth (Residential profit scaled to its 2016 to 2025 average margin, 16.5% against 17.3%) | **$31.42** | $37.84 |
| shown growth uncapped (12.4%), shown only to reject it | $163.57 | $180.77 |

**VALUE RANGE (convention): $35.44 to $42.44 a share**, depreciation variant $41.89 to $49.47; **whole-cycle variant
$31.42 to $37.84** (the 2021 to 2025 window holds a supply-squeeze year and a strong housing market, and no year of a housing
downturn). Widest span top to bottom 49.47 / 31.42 = 1.6 to 1, inside the three-to-one width. **Price $40.32 sits inside
the range.**

**FAIR PRICE:** the price at or below which the central case clears the ~10% pre-tax floor **[M2003-149]**, the
convention's floor. Central case: the midpoint of the two bases, $176.2M before interest, $96.2M (**$3.24 a share**) before
corporate income tax and after interest, growing 1.1%. Tax treatment: the return is measured before company-level income
tax, after interest (interest is deductible), as in "at least 10% pre-tax returns" **[L2002-020]**. Fair price = 3.24 / (10% minus 1.1%) =
**about $36.41**; with no growth, **about $32.41**. At $40.32 the central case's expected pre-tax return is about 9.1%.

**CHEAP PRICE:** **about $18.03.** Rule (CONVENTION of this run): the price at which the worst case in the range
(whole-cycle, all capex, no growth: $80.3M or $2.70 a share pre-tax to the equity) earns 15% pre-tax, which is the same as
saying the worst case could lose a third of its cash to the equity and still clear the 10% floor. Rationale: with net debt
about equal to the market value of the equity, a one-tenth fall in operating cash takes about a fifth of the equity's cash,
so a price that needs no "pencil and paper" **[M1996-084]** must carry a cushion against the leverage that the floor alone does not.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
For the record only: the central case's 9.1% pre-tax at $40.32 against the 5.63% Treasury.

## Q9: COULD IT RUIN US? NOT REACHED.
Facts recorded: debt $1,246.0M, secured, at SOFR plus 1.375% to 2.25% (variable), TLA amortizing to a $561.3M maturity in
2031, TLB due 2033; covenants of maximum net leverage 5.25x stepping to 4.25x and minimum interest coverage 3.0x, both on
the company's adjusted definitions (10-Q note 7). Coverage as the rows measure it, pre-tax earnings over interest: pro forma
2025 about 1.6x ($51.8M pre-tax plus $80.3M interest, over $80.3M, 8-K/A Ex. 99.2); H1 2026 about 1.6x (10-Q). The
acquisition criteria ask for "little or no debt" **[R1997-001]**; this balance sheet no longer has it.

## Q10: IS IT THE FAT PITCH? NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
Not reached. No named business: roofing accessories, rainware, mailboxes, greenhouses, bridge components.

---
## THE BOX
**TOO HARD (WORK), decided at Q2.** The castle's future cannot be judged from the evidence read: a decade of stable
15% to 19% Residential segment margins stands against the filer's own account of retailer line-review bidding, a fragmented
market with cheap entry, a competitor (now owned) that calls its customers price sensitive, and a 30% fall in sales to the
largest customer since 2022; the reason the margins hold is not named in any filing, and it is knowable by further reading.
For the record (COMPUTATION, NOT A CLEARANCE): value range $35.44 to $42.44 (depreciation variant $41.89 to $49.47;
whole-cycle $31.42 to $37.84) against $40.32; fair about $36.41 (no growth $32.41); cheap about $18.03.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the copy was the first action after reading the framework); written in
      order. **Not committed after each question: the owner's instruction for this run forbids commits.**
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`; no v4 id used); every filing fact has its
      document and accession in Step 0 or at the fact; numbers carry a filing or a CONVENTION label.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; Q3 to Q10 are recorded facts, not clearances;
      the valuation is headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): built from operating income less all
      capex, with stock pay inside, and the depreciation variant beside it; the sovereign from the Treasury; aggregator
      quotes flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (ten items under the foundations).
- [x] No row dated after the anchor is cited (the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used, and its OCF line was found to include discontinued operations
      and was not used for value.
- [x] `python tools/check_framework.py` PASS (run after writing; result in the session report).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **The Q7 convention assumes the business of the five-year window is the business being bought.** Here a $1.343B
   debt-financed acquisition closed four months after the window ended and a fifth of the old sales was sold. The convention
   gives no rule for valuing a company whose capital structure and parts changed after the window; I valued the operating
   business before interest and subtracted net debt, and confessed it. A rule is needed (enterprise basis whenever net debt
   changes by more than some share of market value inside or after the window).
2. **"Growth shown" has no rule for bought growth.** The literal shown growth (12.4%) came mostly from acquisitions and a
   depressed base year; carried at face it gives $164 to $181 a share. The cap "by the growth arithmetic of Q3" does not say
   that growth bought with acquisition capital, which the owner-cash figure never deducts, must come out. I removed it and
   moved the base year, on the base-year row cited at Q7. The convention should say so.
3. **Q2's OUT and TOO HARD line is thin when margins are stable but the reason is unnamed.** The routing says "a castle shown
   open on the evidence closes OUT; a castle whose future cannot be judged closes TOO HARD", and the rules-out list includes
   "the customer who buys on the low bid". The filer here says its sales process includes the low bid, and its margins held
   for ten years anyway. Which governs, the customer's buying process or the record of margins, is not stated; I let the
   margin record keep it out of OUT and the unnamed reason send it to TOO HARD. Two analysts could split here.
4. **The template's position note requires `PORTFOLIO.md`, which the blind rule forbids.** I recorded the position as
   unknown. The template should say what a blind run writes.
5. **Operator rule 3's required heading for early valuation math is printed with an em dash between its two halves**,
   which the owner's standing rule forbids; I wrote it as COMPUTATION: NOT A CLEARANCE.
6. **The cheap price has no rule in the framework** (the owner asked for one and "no pencil" is not a number); the rule used
   here is confessed above as a CONVENTION of this run.

---
## RESEARCH PASS (Part VII), STEPS 1 AND 2 ONLY. Not run.
Form: the framework's research pass with the four refinements of 2026-10-05 (single-fact OUT answers; span and source fixed
here before any reading; an unanswerable question recorded and set aside; a blind second session only for a held name,
which is unknown here). Margin comparisons run over the whole span; no capital test sets after-depreciation earnings
against gross capex (capex is set against depreciation, earnings before depreciation are never set against gross capex).

### Step 1: "What do I not know that I need to know?" **[M1999-129]**
| # | question | knowable? |
|---|---|---|
| A | Why did sales to the largest customer fall about 30% from 2022 to 2025: lost programs or line reviews, price concessions, or the retailer's own volume and the company's mix? | Knowable in part (filer MD&A, 10-Q and earnings-release narration); the retailer's own category data is not public. |
| B | Does the Residential margin hold through a housing downturn and a metal-price collapse, i.e., over a whole cycle? | Knowable (segment tables 2008 to 2015 in the 10-Ks FY2010 to FY2015). |
| C | What did the OmniMax business (Euramax's North American residential roof-drainage line) earn over a cycle, before SVP's add-ons? | Knowable for 2008 to 2014 (Euramax 10-Ks); 2015 to 2023 likely not on the public record. |
| D | Where does the Residential profit come from: the bid-driven accessory lines or the niche lines (vents, USPS-approved cluster boxes)? | Probably unknowable from primary documents (no product-line disclosure); to be recorded as such if the search fails. |
| E | Do the retailers award these programs on price? What do the rivals' own filings say? | Knowable in part (Euramax 10-Ks 2010 to 2014; any listed rival in roof drainage or roofing accessories). |

### Step 2: evidence, span, source, and the single fact that closes OUT **[M1998-144]**
- **A.** Span: FY2019 to Q2 2026. Source: ROCK 10-K Item 1 largest-customer line each year, MD&A Residential paragraphs,
  10-Q MD&A, earnings releases (8-K Ex. 99.1) for Q1 2023 to Q2 2026. **OUT if:** any of these documents attributes a
  decline in Residential sales or margin to a lost line review, a lost or reduced retail program, or a price concession to
  a retail customer.
- **B.** Span: FY2008 to FY2025. Source: ROCK 10-Ks FY2010, FY2012, FY2015 (segment notes, three years each) and those
  already read. **OUT if:** in any year of the span the Residential (Products) segment's operating margin before impairment
  charges falls below 10% and the filer attributes the fall to pricing, competition or price/cost alignment rather than to
  volume alone. (10% is a CONVENTION of this pass: about the best year of the no-castle rival NX in 2016 to 2025.)
- **C.** Span: FY2008 to FY2014 and FY2024 to FY2025. Source: Euramax Holdings 10-Ks (CIK 1026743) segment notes for the
  North American residential segment; OmniMax 8-K/A `0001140361-26-015303`. **OUT if:** Euramax's North American segment
  operating margin before impairments is below 5% in three or more of the years 2010 to 2014.
- **D.** Span: FY2016 to Q2 2026. Source: ROCK 10-Ks, 10-Qs, proxy, earnings releases. **OUT if:** the filer states that
  the mail-and-package or ventilation lines account for the larger share of Residential operating income (which would mean
  the bid-driven accessories, now the bulk after OmniMax, carry the lower margin). If no document breaks it out, record D as
  unanswerable (refinement c) and close on A, B, C, E.
- **E.** Span: FY2010 to FY2025. Source: Euramax 10-Ks FY2010 to FY2014 (Item 1 competition, Item 1A customers); an SEC
  full-text search for filers naming "roof drainage", "rainware" or "drip edge" with "line review". **OUT if:** a rival's
  filing states that home-improvement retailers award these product categories on price at line review.

**How step 4 closes.** Any one OUT fact closes the file **OUT** at Q2 ("a castle shown open on the evidence"). If none is
found and B shows the margin held through 2008 to 2011 and C shows the OmniMax line earned more than its cost of capital
over a cycle, Q2 is re-answered **IN** and the run continues from Q3, where the debt-financed purchase price will be met
again (Q3, Q6, Q9). If the reading ends unsure, the close is **TOO HARD (NATURE)**, never a second TOO HARD (WORK) on the
same question **[M2008-086]**.
