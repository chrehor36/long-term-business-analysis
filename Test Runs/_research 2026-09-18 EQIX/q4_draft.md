---
## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the
> queue asks every run for a price and because the (c) question is the one this name was queued
> on; it decides nothing and cannot reopen Q2 [E2-37, E3-39].

### THE SKIP REASON, TESTED ON THE FILING RATHER THAN INHERITED
The wave 5 label is *"capex unresolved [E5-20]: build (c) by hand from the filing"*. The five
checks the dated notes ask for, in order:

**(a) The current `owner_earnings()` prices the name.** On the companyfacts fetched today:
`{'5y_da': 885,930,800, '5y_capex': -559,919,800, '3y_da': 1,028,973,667, '3y_capex': -602,214,000}`.
So on the current screen the label is the AMZN/CL kind of **tooling artefact**: the
`CAPEX_UNRESOLVED` of the 2026-09-01 triage no longer fires. **But the priced numbers are wrong in
two places, below.**

**(b) Early-year facts: a hole of a different kind, a WRONG VALUE rather than a missing one.**
`PaymentsToAcquireProductiveAssets` carries FY2010-FY2025, but for FY2010-FY2013 the values
`annual()` returns are **$14.9M, $28.1M, $24.7M and $74.3M**, which are Equinix's **real estate
purchases** (`PaymentsToAcquireRealEstate` carries the same $24.7M and $74.3M). The same element
also holds **$1,098.6M (FY2012)** and **$696.8M / $572.4M (FY2013)**, the plant figures; `annual()`
keeps one value per year and kept the small one. The screen's owner earnings for FY2010-13
(**+$309M, +$488M, +$523M, +$427M**) are therefore overstated by roughly $1bn a year. They sit
outside every window priced here, but a ten-year-plus window on the screen would be wrong.

**(c) Overlapping capex elements carry DIFFERENT values, and the screen reads only one line of two.**
The face of the cash-flow statement carries two capital lines every year: *"Real estate
acquisitions | ( 994 ) | ( 337 ) | ( 384 )"* and *"Purchases of other property, plant and
equipment | ( 4,311 ) | ( 3,066 ) | ( 2,781 )"* (FY2025 10-K). `CAPX_TAGS` reaches the second
(`PaymentsToAcquireProductiveAssets` = $4,311M, exact) and **never the first**
(`PaymentsToAcquireRealEstate`, $994M in FY2025, $2,878M over FY2015-25). Separately,
`capital_acquired()` **adds** `RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability`
($236M FY2025, non-cash lease additions), which is a legitimate capital addition but a different
one from the cash principal repaid on the same leases (*"Repayments of finance lease liabilities |
( 155 )"*, in financing). **The screen's capex end therefore omits real estate and uses non-cash
lease additions; this run's hand build uses real estate plus the cash lease principal.** The
difference in FY2025 is $994M + $155M - $236M = **$913M** of capital spending the screen's
`5y_capex` end does not see. The hand build is below.

**(d) What the D&A is made of.** FY2025 *"Depreciation, amortization and accretion | 2,066"* (face)
is, from the FFO/AFFO reconciliation and the notes:

| component | FY2025 $M | source |
|---|---:|---|
| **real estate depreciation** (buildings, core systems: electrical and mechanical plant, leasehold improvements, finance-lease buildings) | **1,282** | *"Real estate depreciation | 1,282"* |
| non-real-estate depreciation (internal-use software, 3-5 year life; personal property) | 568 | *"Non-real estate depreciation expense | 568"* |
| amortisation of acquired intangibles (customer relationships) | 200 | *"Amortization expense | 200"* |
| accretion (asset retirement obligations) | about 16 | residual; *"Accretion expense adjustment | 16"* |

**`da_annual()`'s NVDA defect does not bite here**: it returns
`DepreciationAmortizationAndAccretionNet` = $2,066M, the face total, exactly. (The element
`DepreciationDepletionAndAmortization` carries $2,050M, the segment note's total without
accretion.) **90% of the D&A is plant and software; 10% is acquired intangibles**, so unlike SPGI
the band is about plant.

**(e) [E5-20] asked separately, on the filing: YES. Equinix is in the exception class, and the
company's own "recurring" figure points the other way.** Four filed facts:
1. **Capital intensity of a utility.** Gross plant $36,972M against revenue $9,217M (4.0x); capital
   spending (other plant plus real estate) **31.6-57.6% of revenue** every year FY2015-25.
2. **The filer shortened useful lives, twice.** FY2024 10-K: *"approximately $64 million of higher
   depreciation expense driven by IBX data center expansions and acceleration of depreciation
   expense for certain assets with shortened useful lives"* (Americas; $27M and $19M likewise in the
   other regions), and *"We evaluated the estimated useful lives of our property, plant and
   equipment, and made certain revisions to these estimates during the years ended December 31,
   2025 and 2024"* (FY2025 10-K). This is the AMZN trigger in this queue.
3. **The replacement costs more than the original [E4-47].** The year-end tables of projects under
   construction give total project capex per sellable cabinet of **$58.7k (FY2020), $61.3k, $62.2k,
   $80.0k, $101.8k and $126.2k (FY2025)**. Gross plant excluding land and construction in progress
   is **$80.0k per cabinet of capacity** on the books. Depreciation charged on $80k does not renew a
   cabinet that now costs $126k to build. [E4-47]: *"inflation destroys value, but it destroys it
   very unequally"*.
4. **The old plant cannot serve today's customer at the same unit volume.** *"Because many of our
   IBX data centers were built a number of years ago, the current demand for power may exceed the
   designed electrical capacity in these IBX data centers. As power, not space, is a limiting factor
   in many of our IBX data centers, our ability to fully utilize the space in those IBX data centers
   may be impacted"*, and the company is *"considering redevelopment of certain sites"* (FY2025 10-K
   Item 1A; the construction table includes *"MI1 redevelopment | Miami"*, 475 cabinets, $59M).
   Keeping an old building's unit volume is, in [E2-23]'s words, what *"the business requires to
   fully maintain its long-term competitive position and its unit volume"*; the company classifies
   such work as non-recurring.

**So v4's rule applies as written: the D&A end is INVALID, not merely optimistic, and (c) is
judged upward from total capex.** And the company's own measure runs the other way: *"recurring
capital expenditures"* have been **10.9-16.9% of D&A every year FY2016-25** ($284M against $2,066M
in FY2025), a level that would renew the plant roughly once a century. The sentence that justified
it (*"future capital expenditures remain minor relative to our initial investment throughout its
useful life"*) was withdrawn from the filings in October 2025 (Q3).

**Of the seven names now run from this row: ABNB had a real presentation gap, AMZN had no gap, NVDA
a tag gap plus a history gap, CL a tag gap only, SPGI a tag gap plus a (c) question about
acquisitions, TOST a tag gap plus a definition break, and EQIX has NO tag gap now but a
mis-assigned early-year value and a second capital line (real estate) the screen never reads; and
the [E5-20] exception class applies at EQIX, the second name after AMZN.**

### (c) — THE DISCLOSED JUDGMENT, BUILT THREE WAYS
*"(c) must be a guess"* [E2-23]. Three routes, FY2021-25, each from filed figures
(`c_triangulate.py`):

| route | (c) a year, FY2021-25 | how |
|---|---:|---|
| the company's "recurring capital expenditures" | **$228M** | AFFO reconciliations; **rejected as (c)**, for the four reasons above and because pay is funded on the metric it feeds (Q3) |
| depreciation only / total D&A (the corpus default, INVALID here as an END, kept as a yardstick) | $1,657M / $1,863M | face of the cash-flow statement |
| **total capex less growth** | **$1,150M to $1,998M** | $17,353M of capital spending, less the cost of **81,800 cabinets of capacity added** (310,500 to 392,300) at the filed project cost of $58.7k-$101.8k a cabinet (0-15% of the added capacity assumed acquired rather than built, because no filing counts it), less **$3,276M** of land and construction in progress bought ahead of use |
| **replacement cost** | **about $2,940M (FY2025)** | FY2025 depreciation excluding intangibles ($1,866M) scaled by the current project cost over the book cost per cabinet ($126.2k / $80.0k = 1.58) |

**Two independent routes (depreciation, and capex less growth) land within the same band, about
$1.2-2.0bn a year. The company's figure is one-seventh of the bottom of it.** The judgment: **(c)
central = total capex less growth, mid-point about $1.6bn a year over FY2021-25 (about $1.87bn at
FY2025's scale, i.e. depreciation excluding intangibles); (c) conservative = replacement cost,
about $2.9bn at FY2025.** Finance-lease principal ($149M a year mean) is added to (c) at both ends,
because it is the cash cost of buildings held on finance leases and sits in financing; stock pay
capitalised into construction ($60M, $77M, $69M FY2023-25) is subtracted too, because it is in
neither the expensed SBC nor cash capex (the TOST treatment).

### OWNER EARNINGS - THE ONE NUMBER **[E2-23]**
Construction (CONVENTION, v4 section VI): operating cash flow, less stock-based compensation, less
(c). Every figure from the filed cash-flow statements (10-Ks FY2017, FY2020, FY2022, FY2025; 10-Qs
Q2 2025 and Q2 2026), never a net-income proxy. SBC resolves for every year on the face and is
subtracted in full [E5-06]; **the screen's `sbc_annual()` max-rule picks $311.0M for FY2020 where
the face says $295.0M** (a P&L element against the cash-flow add-back, the ARM limit in the resume
note); the hand build uses the face.

| $M | FY2016 | FY2017 | FY2018 | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | TTM 2026-06 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| operating cash flow | 1,019 | 1,439 | 1,815 | 1,993 | 2,310 | 2,547 | 2,963 | 3,217 | 3,249 | 3,911 | 3,942 |
| SBC (face) | 156 | 176 | 181 | 237 | 295 | 364 | 404 | 407 | 462 | 498 | 531 |
| D&A (face) | 837 | 1,043 | 1,228 | 1,285 | 1,423 | 1,656 | 1,736 | 1,844 | 2,011 | 2,066 | 2,185 |
| other plant capex | 1,113 | 1,379 | 2,096 | 2,080 | 2,283 | 2,752 | 2,278 | 2,781 | 3,066 | 4,311 | 5,406 |
| real estate | 28 | 95 | 182 | 169 | 200 | 202 | 248 | 384 | 337 | 994 | 1,119 |
| finance-lease principal | 114 | 94 | 104 | 127 | 115 | 166 | 134 | 149 | 140 | 155 | about 155 |
| company "recurring" capex | 142 | 168 | 203 | 186 | 161 | 199 | 189 | 218 | 250 | 284 | 284 |
| **OE, company (c) [displayed, rejected]** | 608 | 1,002 | 1,328 | 1,444 | 1,739 | 1,819 | 2,236 | 2,443 | 2,397 | 2,974 | 2,972 |
| OE, (c) = total D&A [INVALID end] | 27 | 221 | 407 | 471 | 592 | 527 | 823 | 966 | 776 | 1,347 | 1,226 |
| OE, (c) = all capital spending incl. growth | -392 | -304 | -748 | -619 | -583 | -935 | -101 | -564 | -833 | -2,116 | -3,338 |

**MORE THAN ONE WINDOW [E4-25, E4-38], with the judged (c):**

| window | OCF - SBC - lease principal - capitalised SBC | **(c) central: capex less growth** | **(c) conservative: replacement cost** | (display) company (c) | (display) D&A end |
|---|---:|---:|---:|---:|---:|
| **five-year default [E2-42], FY2021-25** | 2,561 | **about $0.96bn** (range $0.56-1.41bn) | **about zero** (-$0.06bn) | $2.37bn | $0.89bn |
| three-year, FY2023-25 | 2,787 | about $1.1bn | about zero | $2.61bn | $1.03bn |
| ten-year, FY2016-25 | about 2,000 | about $0.7bn | slightly negative (about -$0.1bn) | $1.80bn | $0.62bn |
| **FY2025** | 3,189 | **about $1.32bn** | **about $0.25bn** | $2.97bn | $1.35bn |
| TTM to 2026-06-30 | 3,187 | about $1.2bn | about $0.05bn | $2.97bn | $1.23bn |

*(Ten-year and TTM central figures scale route 2 by the D&A of the window; the replacement-cost end
applies the 1.58 ratio to each window's depreciation. Arithmetic in `oe.py` and `c_triangulate.py`.)*

**The combined range on the default window runs from about zero to about $1.4bn, with a central
figure near $1.0bn. It touches zero in words: at replacement cost, the five-year business has
earned approximately nothing for its owners after keeping its plant current.** [E4-25]: *"Usually,
the range must be so wide that no useful conclusion can be reached."*

**Interest income is inside operating cash**: $193M in FY2025 ($137M, $94M before), earned on
cash and short-term investments averaging about $2-3bn; removed at Q5 with the cash.

**Stock compensation**: 12.7% of operating cash in FY2025, 13.4% over FY2021-25, 13.0% over
FY2016-25. Not the ARM/TOST shape; subtracted in full.

**Per share, the SPGI construction.** Owner earnings per diluted share with (c) at
depreciation excluding intangibles (the central level): about **$6.3 (FY2021, $567M on 90.4M
shares)** to **$13.5 (FY2025, $1,323M on 98.1M)**; at the displayed D&A end $5.83 to $13.73.
Diluted shares rose **67.7% FY2015-25** and **11.0% FY2020-25**, so per-share growth runs about a
tenth below total growth over the last five years.

### GREAT, GOOD, OR GRUESOME? **[E4-20, E4-43]**
- [ ] great
- [ ] good
- [x] **gruesome-leaning, on the incremental numbers**
FY2015-2024 Equinix invested **$31.7bn** (other plant $20,695M + real estate $1,884M + acquisitions
$9,142M). Income from operations rose from **$567M (FY2015) to $1,848M (FY2025): +$1,281M, 4.0%
pre-tax on the capital added**; operating income plus D&A rose **$2,822M, 8.9%**, before any
maintenance. New senior notes in 2026 carry **4.40%, 4.70%, 3.95% and 4.75%** coupons (8-Ks of
2026-03-05 and 2026-05-07). [E4-20]'s gruesome account *"both pays an inadequate interest rate and
requires you to keep adding money at those disappointing returns"*; [E4-43] passes the good class
at roughly 20% pre-tax on net tangible assets. A 4% incremental operating return on a programme
the company now guides at **$5-7bn a year** is on the gruesome side of that line, on this run's
(c). On the company's own AFFO view it looks good; that view is the one Q3 and (c) above decline.

### STAYING POWER - score all three **[E5-11]**
- **(1) A large and reliable stream of earnings: YES.** Recurring revenue above 90% of the total,
  contracts of 1-5 years renewing annually, operating cash $3.9bn, no customer above 3% of recurring
  revenue.
- **(2) Massive liquid assets: NO.** **$2,224M** of cash and short-term investments at 2026-06-30
  (*"Cash and cash equivalents | $ | 979"*, *"Short-term investments | 1,245"*) against about
  **$19.7bn** of senior notes and loans (and $3.0bn more issued 2026-08-06). The $4.0bn revolver is a
  bank line and [E5-39] does not count it (*"We will never be dependent on the kindness of
  strangers"*).
- **(3) No significant near-term cash requirements: NO.** 2026: **$4,912M** of purchase commitments
  (*"primarily for real estate purchases, IBX infrastructure equipment not yet delivered and labor
  not yet provided"*), **$1,317M** of debt maturities, and **about $2,039M** of expected dividends
  (release of 2026-07-29), against operating cash of about $3.9bn. 2027: $1,995M of commitments and
  $1,764M of maturities. The gap is financed by the bond and equity markets every year.
- **Score: 1 of 3.** **Leverage, named and quantified [E4-16, E3-29]:** about $19.7bn of notes and
  loans plus $2.3bn of finance leases and $1.4bn of operating leases, against Adjusted EBITDA of
  $4.5bn; maturities spread **$1.3-2.7bn a year** to 2030 and **$9.6bn thereafter**. **[E2-54]'s
  coverage test, run as written:** cash interest ($448M paid + $79M capitalised = $527M) against
  operating cash before interest ($4,359M) net of ample capital expenditure ((c) central $1.87bn +
  lease principal $0.16bn): **$2.34bn, 4.4x covered**; at replacement-cost (c), **$1.26bn, 2.4x**.
  The interest is comfortably met. **[E3-52] terms**: the debt is fixed-rate senior unsecured notes
  across seven currencies, not covenanted bank debt due next year.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**
**The mechanism: the capacity race, paid for twice.** Named in the company's own words in its
newest filing: *"if the market was to experience an event of excess data center capacity,
capacity originally developed to serve wholesale or hyperscale requirements could be redirected
toward the enterprise colocation markets in which we operate, increasing available supply and
intensifying competition and pricing pressure in our core business"*, and *"certain network, cloud
and content providers may seek to offer connectivity and interconnection through alternative models
that bypass colocation environments"* (10-Q for Q2 2026, `0001101239-26-000147`; both sentences
new in that filing). [E2-27]: *"viewed collectively, the decisions neutralized each other and were
irrational ... After each round of investment, all the players had more money in the game and
returns remained anemic."* The filing itself states the premise that forces the race: *"If we fail
to invest before or contemporaneously with our competitors, our results of operations could
suffer."*

**Quantified from filed figures.** The business earns its central owner earnings of about $1.3bn
(FY2025) on $9.2bn of revenue. **Each 1% of recurring revenue lost to price is about $87M**
($8,739M x 1%). A 5% price concession across recurring revenue (the Americas MRR per cabinet rose
only 11.6% in five years, so 5% is less than half a decade of increases) removes about **$437M, a
third of central owner earnings**. At the same time the **$4.9bn of 2026 purchase commitments**
cannot be cancelled, the dividend (**$2.0bn**, *"Dividend per Share Growth ... Approximates AFFO per
Share Growth"*) already exceeds central owner earnings, and the replacement-cost (c) says the plant
already absorbs most of what is left. **The business does not go broke: fixed-rate long-dated notes,
4.4x interest cover, an investment-grade issuer.** **It dies as an investment the way [E2-27]
describes: more money in the game each round and the return anemic**, with the owner's dividend
financed by new owners.

- Survival shapes (`Screens/SURVIVAL SHAPES - index.md`): **#6 THE BORROWED BALANCE SHEET** (the
  business runs on other people's money it must keep rolling: $11.1bn of equity raised FY2015-25
  and senior notes outstanding grown to $18.4bn at FY2025, funding plant, dividends and
  acquisitions), with **#11 THE PASS-THROUGH**
  (gains of the capacity race passed to customers) as the mechanism and **#1 CONTRACTED NOT TO STOP**
  ($8.4bn of purchase commitments) as a feature. **No new shape is proposed**: the distinctive thing
  here (renewal at current cost booked as growth, and a dividend set by a measure that excludes it)
  is a (c) finding, recorded above, not a new way to die.
- **Exposure, not experience [E4-40]:** the filed record (FY2015-25) is a decade of rising demand
  ending in an AI build-out; the company's new oversupply sentence is about exposure the record has
  not yet shown.
- **Likelihood: [ ] likely [x] a real possibility [ ] a low-level possibility** for a price-led
  compression of returns in colocation (the company added the risk sentence in its latest filing);
  **a low-level possibility** for insolvency.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on survival**  [ ] OUT  [ ] UNRESEARCHED
  [ ] UNKNOWABLE
  *It survives: 4.4x interest cover on central (c), long-dated fixed-rate debt, reliable recurring
  revenue. But staying power scores 1 of 3, the incremental return is about 4% pre-tax, and on the
  five-year default window the owner-earnings range runs from about zero (replacement-cost (c)) to
  about $1.4bn, central near $1.0bn: at the bottom, [E4-25]'s "no useful conclusion".*

