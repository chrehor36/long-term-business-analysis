# Company Run — Superior Energy Services, Inc. (no exchange; operator's sheet ticker SPNX; SEC CIK 0000886835) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-16), after the run was committed: **not held** (`PORTFOLIO.md` carries no line for SPNX or SPN).

**Dispatch:** an unattended overnight cycle under `Screens/_daily/_dispatch_brief.md` as the brief of 2026-10-16 departs
from it (lines of evidence and competitors derived by the analyst from the filing). Working folder
`Test Runs/_research 2026-10-16 SPNX/`; the arithmetic scripts and their output are there (`scripts/`, `run_py_output.txt`,
`q7_output.txt`); raw filings are in its ignored `cache/`.

**Contamination, declared and not used.** (1) A directory listing of `Test Runs/` filtered for "SPNX|superior|SPN", run to
check for a former run of this name, returned one file name, `2026-09-21 Run - SGC Superior Group of Companies.md`: a
different company (a uniform maker), not opened. No file about Superior Energy Services under SPN or SPNX was listed.
(2) The session's opening git status and recent commit subjects named other companies' research folders (AYI, ARCB) and
a STAK fold with its box; not opened, not used. (3) The session's memory index carries one-line summaries of queue state
(counts of gate-clearers, a paused wave); nothing about this name; not used.

**Lines of evidence chosen from the filing** (the brief asks the analyst to derive them from Item 1, Item 1A, Item 7 and
the 2024 10-Qs): (a) dependence on customer drilling and completion spending, read through the rig counts the filer
itself tables (Item 7, Industry Trends); (b) the Rentals segment's economics over a full cycle, since Rentals is the
higher-margin part and the filer's MD&A calls it the part with "strong cash flow generating capacity"; (c) how contracts
are won (Item 1A: "Contracts are traditionally awarded on the basis of competitive bids or direct negotiations with
customers"; Item 1: price named first among "the principal competitive factors"); (d) the capital the rental fleet needs
to stand still (Item 7: fleet maintenance capex "similar to our 2023 capital expenditures"); (e) Argentina (Blue Chip Swap
losses, peso devaluation); (f) the decommissioning liability on the filer's own oil and gas property; (g) the 2020
Chapter 11 and the fresh-start accounts; (h) concentrated ownership, special dividends and the going-private transaction;
(i) the 2024 quarters, the first softening year after 2021-2023.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** **$80.00** a share, the cash price the company itself paid on 2025-01-29 to holders of fewer than 750
  pre-split shares (8-K 2025-01-30, accession 0001193125-25-016623; Disclosure Statement, Schedule 13E-3/A 2025-01-06,
  accession 0001193125-25-001653). **No market quote exists**: "Our Class A Common Stock is not currently traded on any
  exchange or quoted on any over-the-counter market. There is no expectation that a trading market will develop following
  the Stock Splits." (Disclosure Statement, 0001193125-25-001653). Yahoo returns "No data found, symbol may be delisted";
  the OTC Markets page for SPNX was unavailable (aggregators, tried for a quote only, flagged). **CONVENTION of this run:**
  the price is the company's own last stated cash price per share, $80.00 of 2025-01-29, twenty and a half months stale;
  rationale: it is the only price on the primary record, it was paid in cash, and the 750-for-1 forward split left every
  continuing holder's share count unchanged, so it is on today's share basis.
- **Shares by class:** one class, Class A common (Class B reclassified into Class A on 2023-12-18, 10-K FY2023, accession
  0000950170-24-028222). 20,216,192 issued and outstanding at 2024-12-13 (8-K 2024-12-16, accession 0001193125-24-279761;
  the 10-Q to 2024-09-30, accession 0000950170-24-118930, shows 20,216 thousand issued and outstanding and no treasury
  line). After the cash-out the company estimated "approximately 20,127,229" (an estimated 88,963 shares cashed out at the
  1-for-750 ratio, Disclosure Statement, 0001193125-25-001653); the 1-for-750 ratio was the one chosen (8-K 2025-01-30).
  **Count used: 20,127,229**, the company's own estimate; no filing states the final count. `python Screens/cover_shares.py
  SPNX` returned "NOT AN SEC REGISTRANT in the live ticker file"; `tools/run.py` read the dei cover count 20.216M at
  2024-10-29, which agrees with the 10-Q. Not counted: the CEO's 808,247 performance stock units (up to 150%) and 32,960
  restricted shares granted in August 2024 (8-K 2024-08-19, accession 0001193125-24-202588).
- **Market cap at the price:** 20.127M x $80.00 = **$1,610M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-15 (`tools/sources.py` through `tools/run.py`).
- **Filings read** (operator rule 4): 10-K FY2023 (filed 2024-03-08, accession 0000950170-24-028222), Items 1, 1A, 7, 8
  (segment note, cash-flow statement, tax note); 10-Qs to 2024-03-31 (0000950170-24-051196), 2024-06-30
  (0000950170-24-096720) and 2024-09-30 (0000950170-24-118930); 10-K FY2022 (0000950170-23-008104) and FY2021
  (0000950170-22-004202) for the successor years; the predecessor 10-Ks FY2020 (0000886835-21-000003), FY2019
  (0000886835-20-000004), FY2018 (0000886835-19-000003), FY2016 (0000886835-17-000006) and FY2014
  (0000886835-15-000007) for the full cycle by segment; Schedule 13E-3 (2024-12-17, 0001193125-24-279926) with the
  Houlihan Lokey opinion and board materials (exhibits (c)(i) to (c)(iii)); the amended Disclosure Statement (13E-3/A
  2025-01-06, 0001193125-25-001653); 8-Ks of 2024-08-19, 2024-10-15, 2024-10-30 (with the Q3 2024 release, exhibit 99.1,
  0000950170-24-119112), 2024-12-16, 2024-12-20, 2024-12-31, 2025-01-30; the final 13E-3/A (0001193125-25-016650).
  **No proxy exists after the 2019 DEF 14A** (the successor is not Section 12 registered; its 10-K carries the
  compensation disclosure). Later public documents the company itself issued: its website's news page (a banner
  announcing a definitive agreement to acquire Welltec International; the release body did not load) and its April 2026
  newsletter "Momentum" (superiorenergy.com PDF), which announces the closed acquisition of Abaco Drilling Technologies.
  The Quail Tools purchase is on the seller's filed record: Nabors Industries 10-Q to 2025-09-30, accession
  0001104659-25-104844 ("Consideration comprised of cash of $ 375.0 million and a seller note of $ 250.0 million" and, on
  2025-10-09, "prepayment in full of the $ 250.0 million seller note"); Nabors 8-K 2025-08-22, 0001104659-25-081917.
  **Cross-check:** 2023 net cash from operating activities $202,390K on the filed cash-flow statement (10-K FY2023) equals
  the XBRL value `tools/run.py` printed (202.4); capex $74,496K filed equals the printed 74.5.
- `tools/run.py SPNX` refused the ticker (not in the SEC ticker map after the Form 15). It was run through a wrapper that
  supplies the CIK by hand and a placeholder price (`scripts/run_wrap.py`; same arithmetic, the price and CIK only
  supplied); output in `run_py_output.txt`. Arithmetic lines only were used (Part VII). Its five-year window skipped 2021
  (the year is split into a predecessor month and a successor eleven months) and printed a 2019 D&A of 1.4, a tag error
  (filed 2019 DD&A is $196,459K, 10-K FY2020); the owner-cash table below is rebuilt from the filed statements.

**Owner cash after every real cost, from the filed cash-flow statements (USD millions):** operating cash flow less stock
pay less all capital spending. The company states that "Approximately 91% of total 2024 capital expenditures are targeted
for the replacement of existing assets" (Q3 2024 release, 0000950170-24-119112) and that fleet maintenance capex for WSI
"is expected to be similar to our 2023 capital expenditures" (10-K FY2023), so all-spending and maintenance-only are
treated as the same case (Q7 specific (e)).

| year | OCF | stock pay | capex | owner cash, as filed (equity-only) | net interest, after 21% | all-equity (before interest) |
|---|---|---|---|---|---|---|
| 2019 | 146.4 | 19.8 | 140.5 | -13.9 | +77.7 (expense 98.3) | 63.8 |
| 2020 | 2.2 | 2.6 | 47.7 | -48.1 | +73.0 (expense 92.4) | 24.9 |
| 2021 (pred. Jan + succ. Feb-Dec) | 64.3 | 3.6 | 37.2 | 23.4 | n/f, taken as 0 | 23.4 |
| 2022 | 175.4 | 4.8 | 65.8 | 104.8 | -9.3 (income 11.7) | 95.6 |
| 2023 | 202.4 | 4.1 | 74.5 | 123.8 | -20.4 (income 25.8) | 103.4 |
| **mean 2019-2023** | | | | **38.0** | | **62.2** |
| TTM to 2024-09-30 | 272.2 | 3.5 | 74.7 | 194.0 | | |

The TTM figure carries a working-capital release of $67.4M in the nine months of 2024 (receivables fell from $276.9M to
$200.1M, 10-Q 0000950170-24-118930). **CONVENTION of this run:** net interest is put on an after-tax basis at the 21%
statutory rate to move between the two bases; rationale: the template asks for owner cash before interest and after the
company's tax, and the company's own effective rates in the window (a 36.4% benefit in 2022, 25.5% expense in 2023) are
distorted by a worthless-stock deduction and valuation allowances. 2019 and 2020 owner cash is the predecessor's, before
its bonds were cancelled in Chapter 11.

## THE FOUNDATIONS (not a gate)
The foundation that bears most is that a share is a business and the market only quotes: here there is no market at all,
and the one price is a cash-out set by a board on which the two institutions holding about 65.7% appoint three of six
directors (Disclosure Statement, 0001193125-25-001653). The analyst's habits bear second: the Disclosure Statement prints
management's projections to 2028 and a banker's EBITDA-multiple ranges of $67 to $85 a share; these are not used, since
"we’ve never looked at a projection in connection with either a security we’ve bought or a business we’ve bought"
**[M1995-050]**. No macro forecast enters: the oil price is not forecast here, "We don’t think we can predict commodity
prices." **[M2016-025]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) Rentals earned $225.0M of
segment operating income on $553.7M of identifiable assets in 2023 (10-K FY2023 segment note), a high return in that
year; (2) the company has no borrowings at 2024-09-30 and $380.6M of cash including restricted cash; (3) in 2025-2026 it
bought Quail Tools, a rival drill-pipe renter, which consolidates its own field; (4) TTM owner cash to 2024-09-30 was
$194.0M, about 12% of the cash-out market value, though inflated by a working-capital release.

## THE STANDING RULE
The buyer's conduct, not the target's: a minority holding in an unlisted company with no trading market, a
stockholders agreement restricting transfers (10-K FY2023 Item 1A) and no reporting since 2025-01-30, could not be sold
to raise cash on demand; the rule is breached only if the purchase is financed so that "the other fellow can call your
tune" **[M2006-079]**. Bought with the buyer's own money and sized so that a total loss is borne, it is not a ruin risk to
the buyer. Noted, not weighed: an owner of these shares can be forced to take a price set by the controlling holders, as
the holders of fewer than 750 shares were.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The business, from the filing.** Rentals rents premium drill pipe, landing strings and tubulars (Workstrings
  International), bottom-hole-assembly tools (Stabil Drill) and offshore accommodation units (HB Rentals), "primarily
  priced on a per day, per man hour or similar basis" for terms "generally less than twelve months" (10-K FY2023, revenue
  policy). Well Services sells well control (Wild Well Control), snubbing, completion tools, and cementing, wireline and
  coil tubing in Latin America and Kuwait, and "includes the operations of our offshore oil and gas property" (segment
  note). No customer above 10% of revenue in 2021 to 2023.
- **The key variables** **[M1998-044]**: customers' drilling and completion spending, which the filer tracks by rig
  count ("Rig count is an indicator of the level of spending by oil and gas companies", Item 7), and the day rate and
  utilization of the rental fleet; then the fleet's replacement cost. These are readable from the figures: Rentals'
  revenue moved with the cycle from $852M (2014) to $294M (2016) to $452M (2023) (segment notes, FY2014 to FY2023
  10-Ks). The product needs no chemistry or technology forecast to be understood; what matters is "the economic dynamics
  of the industry. Is there — are there competitive moats? Is there ease of entry?" **[M2011-014]**.
- **Routing.** A dependence on a commodity price "is never by itself a STOP at Q1 or Q2" (the framework's commodity
  paragraph): "So if you can’t make a decision on something like PetroChina off the figures, forget about going further"
  **[M2008-069]**. The figures here are full and audited for eleven years, segment by segment, so the decision can be
  made off them. The industry is not one of fast technological change in the sense of Q1's routing (the rented product,
  drill pipe and downhole tools, is the same product across the whole span read); the energy-transition risk the filer
  lists (Item 1A, climate change) is a slow change to demand, weighed at Q2's test 11, not a reason the economics cannot
  be pictured.
- **Can I picture where it will be in ten years?** **[M2000-037]**, **[M2012-065]**: the earning power will swing with
  customer spending as it did from 2014 to 2023; the competitive position is what Q2 must read. The forecast asked is the
  shape of the economics across a cycle, which the filed record shows, not the oil price. Doubt about the perimeter is
  present only on the post-2024 deals, whose figures are not filed; they enter at Q7.
- **VERDICT: IN.** A rental and services business whose economics can be read off eleven years of segment figures
  **[M2008-069]**, **[M2011-014]**; the commodity dependence goes to Q2 and Q7 by the framework's placement.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.

**The parts table** (business of parts, section B; five-year segment operating profit 2019-2023, USD millions, from the
segment notes of the FY2020 and FY2023 10-Ks; 2019-2020 are the predecessor's segments, mapped to today's two as the
FY2021 10-K redrew them: Drilling Products and Services to Rentals; Onshore Completion and Workover, Production Services
and Technical Solutions to Well Services):

| part | 2019 | 2020 | 2021 | 2022 | 2023 | five-year sum | against the company's sum | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| Rentals (Drilling Products and Services before 2021) | 113.0 | 70.0 | -13.1 | 183.6 | 225.0 | 578.5 | more than the whole 136.5 | read below | **yes** (more than half) |
| Well Services (three predecessor segments) | 3.5 | -109.4 | -59.9 | 84.5 | 74.8 | -6.5 | negative | not read | no |
| Corporate and other | -98.0 | -132.7 | -82.1 | -64.8 | -58.0 | -435.6 | | | |
| company income from operations | 18.4 | -172.0 | -155.1 | 203.4 | 241.8 | 136.5 | | | |

2021 is the predecessor month plus the successor eleven months; the successor's Rentals carried $152.3M of fresh-start
depreciation. The 2019-2020 segment measure excludes allocated corporate expenses (FY2020 10-K). Rentals decides; Well
Services, which does not decide, would be carried to Q7 as an ordinary business at no growth were Q7 reached.

**The deciding part across the full cycle** (Rentals, called Drilling Products and Services until 2020; segment notes of
the 10-Ks FY2014, FY2016, FY2018, FY2020, FY2023 and the 10-Q to 2024-09-30; USD millions):

| year | revenue | segment op. income | identifiable assets | margin |
|---|---|---|---|---|
| 2014 | 852.5 | 275.2 | 1,212.9 | 32% |
| 2015 | 547.5 | 20.7 | 1,154.4 | 4% |
| 2016 | 293.5 | -116.2 (-143.0 on the FY2016 basis) | 824.3 | loss |
| 2017 | 293.7 | -18.7 | 663.0 | loss |
| 2018 | 383.7 | 69.9 | 587.3 | 18% |
| 2019 | 411.6 | 113.0 | 659.6 | 27% |
| 2020 | 281.4 | 70.0 | 557.5 | 25% |
| 2021 | 287.0 | -13.1 | n/f | loss (fresh-start D&A) |
| 2022 | 402.9 | 183.6 | 432.4 | 46% |
| 2023 | 452.2 | 225.0 | 553.7 | 50% |
| 9M 2024 (9M 2023) | 305.8 (334.4) | 139.1 (167.4) | 458.2 | 45% |

Ten-year sum of segment operating income 2014-2023: **$809M** on average identifiable assets of about $738M (the nine
years with a figure): about **11% a year pre-tax, before any share of the unallocated corporate costs** of $58M to $133M a
year (2016-2023), and on asset values written down by impairment (2015, 2016) and reset by fresh-start accounting in 2021.
Losses in three of the ten years. Revenue fell 66% from 2014 to 2016.

**The competitor row.** The 10-K's Competition paragraph names no rival ("competitors comprised of both small or
regionally focused companies in our Rentals segment, and large or international companies in our Well services
segment"). **CONVENTION of this run:** the rivals are SEC filers that rent the same product, chosen because the deciding
part is a rental fleet: RPC, Inc.'s Support Services segment ("Support Services such as the rental of drill pipe", RPC
10-K FY2015, 0001571049-16-012371); Parker Drilling's rental tools segment, which is Quail Tools, the business Superior
bought in 2025 (Parker 10-Ks FY2016 0000076321-17-000007 and FY2019 0000076321-20-000014; Parker stopped filing in 2020);
and Oil States International, one of the selected companies the company's own Disclosure Statement lists (with Expro,
Helix, Oceaneering, Ranger, RPC and Weatherford). Weatherford is shown beside for the field. Same metric where the filing
gives it: segment operating income over the same ten years. Rivals that do not file: the "small or regionally focused
companies" the 10-K describes are unnamed.

| rival | metric, 2014-2023 | figure | source |
|---|---|---|---|
| RPC Support Services (drill-pipe and tool rental) | segment operating profit, ten-year sum, on average identifiable assets of about $86M | **$49M**, about 6% a year pre-tax; losses in 5 of 10 years (2015, 2016, 2017, 2020, 2021) | RPC 10-Ks FY2015, FY2017 (0001144204-18-011709), FY2020 (0001104659-21-029211), FY2023 (0001558370-24-001993) |
| RPC, whole company | operating income, ten-year sum | $567M on average assets of about $1.15B, about 5% a year | XBRL company facts, RPC 10-Ks |
| Parker rental tools (Quail Tools and international) | segment gross margin before D&A | $137.1M (2014) to $14.3M (2016) on revenue down from $347.8M to $134.2M; operating gross margin $32.8M on $255.7M of revenue in 2018; Parker in Chapter 11 from 2018-12-12, emerged 2019 | Parker 10-Ks FY2016, FY2019 |
| Oil States International | operating income, ten-year sum | **-$585M**; losses in 2016-2021 | XBRL company facts, OIS 10-Ks |
| Weatherford (beside) | operating income, ten-year sum | about -$9.9B; losses 2015-2020 | XBRL company facts, WFRD 10-Ks |
| Superior, whole company | operating income, ten-year sum | about -$2.9B (as tagged); Chapter 11 from 2020-12-07 | XBRL company facts; 10-K FY2023 Item 1 |

**The castle tests, each with its filing fact.**
- **Is it a commodity business?** The filer's own words: "the principal competitive factors are price, performance,
  product and service quality, safety, response time and breadth of products and services" (Item 1), and "Contracts are
  traditionally awarded on the basis of competitive bids or direct negotiations with customers" in a market that "includes
  numerous small companies capable of competing effectively in our markets on a local basis, as well as several large
  companies that possess substantially greater financial resources than we do" (Item 1A). A rental of drill pipe by the
  day, won on bid, carries the rows' mark of the commodity: "most insureds don't care from whom they buy. [...]
  Consequently, price competition in insurance is usually fierce." **[L2004-003]**; the opposite of See's, where "it
  wouldn’t be a question of people buying candy for the low bid" **[M2017-009]**.
- **The low-cost producer?** The one named way through a commodity field: "commodity businesses have risk unless you’re
  the low-cost producer, because the low-cost producer can put you out of business." **[M1997-010]**; "when a company is
  selling a product with commodity-like economic characteristics, being the low-cost producer is all-important."
  **[L2000-017]**. No filing read states Superior's cost per unit of fleet against a rival's, and no rival's filing does;
  the rows ask it be measured "more by cost of production" **[M2006-004]**, and for copper "The figures are available."
  **[M2009-059]**; here they are not. What the filings do show is the outcome a low-cost position would prevent: in the
  2015-2017 downturn the deciding part lost money for two years, as RPC's rental segment did. The filer cites WSI's "depth
  of inventory resulting from consistent investments through the cycles" (Item 7): a size advantage claimed, not a cost
  figure shown.
- **Pricing power and the agony before a rise** **[M2005-020]**: the filer claims "being an early mover on effective
  pricing strategies to address cost inflation" in 2023 (Item 7), and Rentals' gross margin rose to 66.9% (2023) from
  65.8% (2022). But "you learn a lot about the durability of the economics of a business by observing the behavior of —
  the price behavior" **[M2005-020]** across the cycle, and across it Rentals' revenue fell 66% in two years (2014 to 2016)
  and its operating margin went from 32% to a loss: the price did not hold when rigs left. In 2024 a modest fall in the
  U.S. land rig count took nine-month Rentals operating income down 17% (10-Q to 2024-09-30), the company citing "reduced
  activity in U.S. land" (Q3 2024 release, 0000950170-24-119112).
- **The money test** **[M2011-015]**: could a well-funded rival rebuild a string inventory like WSI's? The filings show
  rivals holding fleets of the same kind through the same cycle (RPC, Parker's Quail Tools), and Superior itself bought
  Quail's fleet in 2025 for $625M (Nabors 10-Q, 0001104659-25-104844): the asset is for sale, the opposite of "if I had a
  hundred million dollars and I wanted to go in and take on See’s Candy, could I do it? And I came to the conclusion, no"
  **[M2011-015]**.
- **The rival who sets the price** **[M2012-109]**: no filing read names a price leader; Superior's own filing says
  contracts go by bid.
- **Widening or narrowing** **[M1999-108]**: the 2022-2023 margins are the best in the eleven years read; the 2024
  quarters turned down. A change for the better is credited only on a full cycle in which the price held (Q2, Change, the
  CONVENTION of 2026-10-06), and the only full cycle on file, 2014 to 2023, is the one above, in which it did not hold. The
  railroads that "were a terrible business for decades and decades and decades and then they got good" **[M2017-026]** are
  a reason to watch, not to credit.
- **What could destroy or reduce it** **[M2000-014]**: the filer lists the slow change, climate rules that "could
  decrease demand for oil and gas and consequently adversely affect the business of our customers" (Item 1), and
  customers that cut funds for drilling "due to increased dividend payments and share repurchase programs" (Item 1A).
  Neither is needed for the verdict.

**The field's returns over the last full cycle, judged in words** (section C; "ordinary" carries no figure): the deciding
part earned about 11% a year pre-tax on its written-down assets before overhead, with three loss years; the closest filed
rival in the same rental product earned about 6% with five loss years; the larger rivals lost money in total over the
decade; two of the companies compared, Superior and Parker, went through Chapter 11 inside it. That is a field in which
"you can have only two competitors and they’re still terrible businesses, they beat each other’s brains out"
**[M2013-052]**: a standing castle at best, protecting ordinary returns, not "an enduring "moat" that protects excellent
returns on invested capital" **[L2007-004]**. The framework sends such a field to OUT, not TOO HARD: its returns are known
from the filings, so the tenuous-moat reason ("We don’t know how to valuate that" **[M2000-019]**) does not apply.
Superior's rentals did about twice as well as RPC's on this record; the better of two ordinary renters is not a castle.

- **VERDICT: OUT.** The deciding part sells a product won on bid **[L2004-003]**, **[M2017-009]** in a field whose filed
  returns across 2014-2023 were ordinary for its best part and negative for the field **[M2013-052]**, **[L2007-004]**,
  with no filed evidence of a low-cost position **[M1997-010]** and a price that did not hold through the downturn
  **[M2005-020]**. The improvement of 2022-2023 is not credited without a full cycle **[M2017-026]**. The file closes here.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (closed at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0 (the template asks for them where the file closes before Q4); what
they show is under AFTER THE STOP.

## Q5 — WHO RUNS IT. STOP on integrity.
NOT REACHED. Integrity facts found are under AFTER THE STOP and flagged in the box line.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The owner's two reporting figures follow, under the protocol's heading.

### COMPUTATION, NOT A CLEARANCE
Built by Q7's range convention (`scripts/q7.py`, output `q7_output.txt`; USD millions unless per share).
- **Cash input:** owner cash after every real cost, five-year mean 2019-2023 (the Step 0 table): **$62.2M all-equity**
  (before net interest, after a 21% rate on it), **$38.0M equity-only** (after interest as paid, most of it the
  predecessor's bond interest in 2019-2020). All capital spending deducted; the filing allows the maintenance guess and it
  is the same figure (91% of 2024 capex "targeted for the replacement of existing assets"), so specific (e) changes nothing.
  Working capital is inside operating cash flow (d). No acquisition inside the window (c).
- **(a) Cycle.** The window's first year, 2019, is ordinary by the filer's description; 2020 (Chapter 11, pandemic) is
  aberrational but not an end year; the last year, 2023, is the best year in the successor's record. A base over the full
  cycle 2014-2023 cannot be computed on the same scope: the 2014 company had $4,557M of revenue from businesses since sold
  or shut (pressure pumping, completion services, Pumpco). **CONVENTION of this run:** the literal window is the central
  base and the TTM to 2024-09-30 is shown beside; rationale: no cycle base of the present business exists in the filings.
  TTM all-equity owner cash beside: about $174M, inflated by a $67.4M working-capital release.
- **Growth and the cap (f).** Shown growth of all-equity owner cash 2019 to 2023: **12.8% a year**. Carried ten years it
  needs year-ten owner cash of $208M, 22.6% of 2023 sales, against the best share earned in the window, 11.2% (2023):
  the cap applies, and the growth carried is the business's own sales growth over the same window, 2019 $1,425.4M to 2023
  $919.4M, **-10.4% a year** (the fall is mostly the shedding of businesses; the successor's own sales grew 15.0% a year
  from 2021 to 2023, shown beside, not used). By (b) the decline is the bottom of the range and no growth the top.
- **Net debt.** At the latest filed date, 2024-09-30: no borrowings ("no outstanding borrowings under our credit
  facility", Q3 2024 release); cash and equivalents $325.9M (restricted cash $54.7M left out, since it secures letters of
  credit and obligations; shown here); the cash-out of about $8.0M added (Disclosure Statement). Then the deal closed after
  the window (c): **Quail Tools, closed 2025-08-20, $375.0M cash plus a $250.0M seller note prepaid on 2025-10-09** (Nabors
  10-Q, 0001104659-25-104844), its financing of $625.0M added to net debt and the business **credited at nothing**, since
  no earnings of it are filed (Nabors files its revenue only: $193.5M in the nine months to 2024-09-30). Abaco Drilling
  Technologies, closed by early 2026 by the company's own newsletter: price not found, **not counted, a gap**. The
  decommissioning liability of $170.8M (10-Q) is an obligation outside the convention's net debt; shown, not added.
  Net debt used: **+$307.1M** (with Quail); -$317.9M beside (without).
- **The signed, unclosed deal, beside:** Welltec International, definitive agreement announced by the company in
  September 2026, close expected in the first half of 2027; price reported at about $1.2B including about $100M of assumed
  debt (aggregator, JPT, flagged; the company's release did not load). Not in the central figure; valued as if closed it
  would add about $1.2B to net debt with Welltec's own filed record credited, and Welltec files nothing with the SEC: on
  the convention's terms it would lower every per-share figure below by about $60.
- **The range** (discounted at 5.43%, ten years, then zero nominal growth):

| case | enterprise value | per share, with Quail financing (central) | per share, without Quail (beside) |
|---|---|---|---|
| bottom: decline at -10.4% for ten years | $509M | **$10.03** | $41.08 |
| top: no growth | $1,146M | **$41.68** | $72.73 |
| equity-only (after interest, no net debt) | $311M to $700M | $15.45 to $34.78 | same |

- **The floor, tested first:** at $80.00 the shares plus net debt are $1,917M (with Quail; $1,292M without). The top
  case's $62.2M is a 3.3% return on that (4.8% without Quail); **no case in the range earns about ten percent at the
  price** **[M2003-149]**. The width test is not reached (the range's ends are about four to one, which would be TOO HARD
  on its own). Beside, outside the range: the uncut 12.8% growth case values at $1,521M at ten percent, $60.29 a share with
  Quail ($91.34 without), so even the case the cap removes clears $80 only if the $625M Quail purchase is left out of net
  debt; the TTM figure of about $174M would be 9.1% on $1,917M.
- **Value range (central, all-equity, with Quail): $10.03 to $41.68 a share** against **$80.00**.
- **Fair price (reporting figure, never a verdict; Part VII): $8.11 a share**, each end case valued at ten percent
  ($319M and $622M), averaged, less net debt with Quail, after the company's own tax; **equity-only beside: $14.28**.
  Without the Quail financing (beside): $39.16. A price above the top of the range closes OUT by the floor convention;
  the file is already OUT at Q2.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q2** (the deciding part, Rentals, is a bid-won rental in a field whose filed 2014-2023 returns were ordinary for
its best part and negative for the field; no low-cost position on the record); **integrity facts recorded, not judged**.
COMPUTATION, NOT A CLEARANCE: value range $10.03 to $41.68 a share (all-equity, Quail financing in net debt) against the
company's own last cash price of $80.00 (2025-01-29, no market exists); fair price $8.11 (equity-only $14.28).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged **[M1997-127]**.

**Q3 (capital).** Rentals' 2023 segment capex $59.0M against segment D&A $49.4M (10-K FY2023 segment note); the
company's 2024 capex guidance $100M to $110M, 91% replacement, 68% in Rentals (Q3 2024 release). Fleet maintenance for
WSI "expected to be similar to our 2023 capital expenditures" (10-K FY2023, Item 7). Rentals' identifiable assets fell
from $1,212.9M (2014) to $432.4M (2022) through impairment, sales and fresh-start revaluation, so its recent returns are
on written-down capital. After the window the company spent $625M on Quail Tools and an undisclosed sum on Abaco, and has
signed for Welltec: a capital programme larger than the whole 2019-2023 owner cash.

**Q4 (the accounts; the balance sheets over eight to ten years, read in Step 0)** **[M2025-032]**. From `tools/run.py`'s
table and the filed statements: equity $1,132M (2017) to $291M (2018) to $50M (2019) to **-$339M (2020)**, retained deficit
to -$3,023M, long-term debt about $1,280M to $1,287M from 2017 to 2019, then the Chapter 11 and fresh start: equity $903M
at 2021-02-02, no borrowings since. Goodwill $808M (2017), $137M to $139M (2018-2020), nil after fresh start. Cash rose to
$391.7M (2023) after a $250.0M special dividend paid in December 2022, then fell to $325.9M (2024-09-30) after a second
$250.4M distribution in 2024. Receivables $276.9M on 2023 revenue of $919.4M, about 110 days, falling to $200.1M at
2024-09-30. A note receivable of $72.7M and deferred tax assets of $59.6M (2024-09-30). The decommissioning liability on
the company's own offshore oil and gas property, $170.8M in total, with the filer's warning that "the risk exists we may
underestimate the cost of plugging wells and abandoning production facilities" (Item 1A). Real costs recurring under
one-time names: restructuring and transaction expenses in every year read (2020 $47.1M, 2021 $24.2M, 2022 $6.4M, 2023
$3.3M, 9M 2024 $5.9M). Argentina: Blue Chip Swap losses of $19.9M (2023) and $5.1M (9M 2024) to move dollars out, foreign
exchange losses of $14.8M in Argentina (2023). A material weakness in internal control over tax-provider calculations
identified for FY2022, remediated by 2023-12-31, and a $7.6M correction of a FY2022 tax error recorded in 2023 (10-K
FY2023, Item 1A and Item 7). The Q3 2024 release features "Adjusted EBITDA", segment "Adjusted EBITDA Margin" and full-year
"2024 Guidance" of $235M to $265M Adjusted EBITDA (exhibit 99.1, 0000950170-24-119112); the 10-K and 10-Q themselves do
not use the term. Under Q4's text these would be weighed against and carried to Q5 **[L2016-006]**, **[L2019-006]**,
**[M1998-086]**; not weighed here.

**Q5 (the people; integrity facts).** Chief executive Brian Moore stepped down 2024-08-19; David J. Lesar (formerly
chairman and chief executive of Halliburton) became chairman and chief executive with a $1.0M salary, a 150% target bonus
and 808,247 performance stock units that vest on per-share hurdles and settle on a change in control, and a gross-up for
the golden-parachute excise tax (8-K 2024-08-19). The chief financial officer resigned effective 2024-12-31 "to pursue
other opportunities" with a lump sum of two times salary plus target bonus (8-K 2024-10-15). The going-private
transaction was approved by written consent of holders of 13,277,161 of 20,216,192 shares, with "no appraisal or
dissenters’ rights" for the others; the board did not assign a "going concern value"; the fairness opinion covered only
the cashed-out holders, "did not address fairness with respect to the Continuing Stockholders"; Houlihan Lokey disclosed
past work for both controlling institutions, "including, with respect to Monarch, having provided valuation advisory
services with respect to Monarch’s investment in the Company" (Disclosure Statement, 0001193125-25-001653). The stated
reason was cost: about $1.6M a year of public-company costs. The material weakness and tax correction above. Any later run
that reaches Q5 must answer these **[M2013-088]**.

**Q6 (the money and the owners).** Special dividends of $12.45 (December 2022) and $12.38 (March 2024) a share, about
$250M each; a share repurchase of $1.0M in 2024; then, after deregistration, acquisitions of Quail Tools ($625M), Abaco
and Welltec (pending). The 2023 10-K's strategy statement: "potential merger or acquisition opportunities" and "actions to
facilitate additional return of capital to shareholders". Owners have had no public reporting since 2025-01-30.

**Q9 (debt and exposures).** No borrowings at 2024-09-30; an asset-based facility whose borrowing base fell from $140.0M
(2023-12-31) to $89.9M (2024-09-30) with $39.5M of letters of credit. After the window: the $250M seller note was
prepaid within two months, financed by means not on the public record; Latham & Watkins advised "the financing sources
on the committed financing" for Welltec (aggregator, flagged). Liability insurance limits of $200M per occurrence, with
well control costs not covered (Item 1). The offshore decommissioning liability and the Argentine currency exposure above.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; committed after Step 0 and Q1, after Q2, and at the close. **Not kept in
      full:** the filings for Q1 and Q2 were all fetched and read before the Q1 section was written, so the file was not
      written question by question as each closed; the commits are per question.
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatcher's; the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened; the one file name seen by a filtered directory
      listing (a different company), the commit subjects and the memory line are declared under contamination.
- [x] Every v5 id resolves (`scripts/check_ids.py`, PASS); every filing fact has its accession; aggregator facts (the
      Welltec price, the Latham line, the failed quote pages) are flagged.
- [x] The order was kept; Q2 closed the run; everything after it is NOT REACHED or under COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; the sovereign from
      the US Treasury; no market quote exists, and the price used is the company's own cash-out price, confessed.
- [x] Contrary evidence written down (Foundations); facts for later questions under AFTER THE STOP; integrity flag in the
      box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used; its 2021 gap and 2019 D&A tag error were corrected from the
      filed statements.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A name with no price.** The framework and the template assume a quoted price; this company has no market and has
not reported since 2025-01-30. Nothing says what price a run uses, or whether a run of an unlisted, non-reporting company
is a purchase run at all; the run used the company's own cash-out price as a CONVENTION. (2) **Deals after the last
filing of a non-reporting company.** Q7 specific (c) credits a closed deal "at nothing where no earnings are filed" and
adds its financing to net debt. For a company that stopped filing and then spent $625M on a rival, the rule turns the
company's own capital decision into a pure debit, and the central fair price ($8.11) moves by about $31 a share on that
one line; the text does not say whether the seller's filed revenue counts as a "filed record". (3) **The parts mapping
across a reorganization.** The business-of-parts threshold uses "five-year operating profit" by part, but the predecessor
reported four segments and the successor two, with corporate costs allocated differently; the run mapped them by the
FY2021 10-K's redrawing and said so. Where the company's total five-year operating profit is small, a part can be four
times the whole, and "more than half" is then trivially met. (4) **The cap (f) on a shrinking company.** The cap swaps
in "the business's own sales growth over the same window", which here is -10.4% a year, mostly from businesses sold; the
rule turns a scope change into a decline case. The organic alternative (15.0% a year from 2021 to 2023) is shown, not
used. (5) **No rivals named.** The 10-K names none; the rivals were chosen as a CONVENTION, two of them from the company's
own Disclosure Statement's list; the template's instruction to take "the rivals the 10-K itself names" has no fallback
in the framework text.
