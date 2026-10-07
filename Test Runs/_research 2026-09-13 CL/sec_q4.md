
## Q4 — WILL IT SURVIVE?

### THE PERIMETER, settled first, because it decides where the window can start
- **Venezuela.** The FY2016 10-K's own organic definition excludes *"the deconsolidation of the Company's Venezuelan
  operations"*, alongside foreign exchange, acquisitions and divestments. **No window in this section starts before 2016**, and
  the eleven-year 2015-2025 window is displayed but not used, and labelled as crossing the perimeter change.
- **Acquisitions inside the window, from the 10-Ks** (each a change of perimeter, none restated backwards): EltaMD and PCA
  SKIN 2018, *"aggregate cash consideration of approximately $730"*; Filorga September 2019, $1,711M of acquisition cash; hello
  2020, $351M; **three United States dry pet food plants from Red Collar Pet Foods in 2022, *"a purchase price, as adjusted, of
  $719"***; Prime100 (Care TopCo, Australia) 2025, $301M. Total acquisition cash 2016-2025: **$3,899M**. They are shown beside
  owner earnings and are **not** subtracted from it; they are capital allocation and were scored at Q3.
- **Equity-method stakes [E3-04]: immaterial and no look-through adjustment is made.** *"equity method investments included in
  Other assets in the Consolidated Balance Sheets were $ 82 and $ 81"* (2025, 2024), against $16,330M of assets.
- **The ESOP open item, closed on the filing.** Step 0 left it open because no share-based-compensation list reads the ESOP
  tags. The note answers it outright: ***"Annual expense related to the ESOP was $ 0 in 2025, 2024 and 2023."*** The 6,646,688
  ESOP shares are common shares already inside the share count and *"have all been released and allocated to participant
  accounts"*; the ESOP *"had no outstanding borrowings from the Company"*. **So nothing is missing from the compensation
  charge, and the draft's deduction of ESOP dividends ($15M in 2025) from owner earnings is over-conservative** — those
  dividends are paid on shares already counted. It is kept in the table as a display and is **not** used in the range.
- **Hyperinflationary remeasurement: inside net income and NOT separately quantified, and that is stated rather than
  estimated.** *"Remeasurement adjustments for these operations are included in Net income attributable to Colgate-Palmolive
  Company"* (Note 2). No amount is disclosed in any 10-K on disk. The exposure can only be bounded by region: Latin America and
  Africa/Eurasia are 29.2% of 2025 net sales, and the 10-K names *"Argentina, Nigeria and Türkiye"*. **An UNRESEARCHED tag is
  not warranted, because no document exists that gives the figure; it is recorded as a disclosure gap.**

### OWNER EARNINGS — THE ONE NUMBER [E2-23]
**Built by hand from the filed cash-flow statements, not from a net-income proxy and not from tagged data** (script `oe.py`,
output `oe_out.md`; sources 10-K FY2017 for 2015-2017, FY2020 for 2018-2020, FY2023 for 2021-2023, FY2025 for 2023-2025, and
the 10-Q for the quarter ended 2026-06-30 for the interim). **Verified in this session against the filings:** FY2025
depreciation and amortization $630M, stock-based compensation $155M, capital expenditures $564M; H1 2026 net cash provided by
operations $1,742M, D&A $311M, SBC $78M, capex $266M; H1 2025 $1,484M / $299M / $55M / $232M and the $293M Prime100 payment.
All match the script's inputs.

**(c), the disclosed judgment. It "must be a guess."**
- **[E5-20] asked on the filing, and answered: Colgate is NOT in the exception class.** The exception is the business *"whose
  own filing says depreciation understates renewal"* — railroads, airlines, utilities. Colgate's filing says the opposite
  shape: net property, plant and equipment is **$4,660M against $20,382M of sales**, capital expenditures have run **2.1% to
  3.9% of sales** across the decade, and the FY2025 10-K plans FY2026 at *"approximately 3.0% of Net sales"*. Over 2016-2025
  **capex was $5,420M against depreciation of $4,719M (1.15x) and D&A of $5,390M (1.01x)** — the [E2-41] and [E3-44] default
  case, *"capital expenditures that over time roughly approximate depreciation"*. **So the D&A end is VALID here, not invalid.**
- **And (c) is still set at TOTAL capital expenditures, not at depreciation, for two reasons from the filing.** (i) **[E4-47],
  the inflation condition:** 29.2% of sales sit in Latin America and Africa/Eurasia, where depreciation is charged in old
  dollars and replacement is bought in new ones — and the segment notes show it: **Latin America's own capex/D&A is 1.35x over
  2016-2025 ($1,198M against $890M)**. (ii) No split of maintenance from growth is filed, and the credit for treating Hill's
  plant building as growth (segment capex of $888M against D&A of $360M across 2021-2024) is **declined** rather than taken.
  **The band is narrow anyway**: the capex end and the D&A end differ by about 1% over ten years.
- **The working-capital increment [E2-23] constraint 3: NONE is required, and the carve-out is why.** Colgate's working capital
  is negative — *"(7.0)% in 2025"* of net sales — so growth **releases** cash rather than absorbing it. That is the benign
  case. **But a release is not a repeatable earning**, so every window below is also shown with the filed working-capital lines
  (receivables, inventories, accounts payable and other working capital) stripped out.
- **No restructuring is added back.** Q3's **[E5-33]** finding binds here: program charges have been excluded from the
  headline measure in thirteen of fourteen years, so their cash stays in owner earnings because operating cash flow carries it.

| year | OCF | SBC | D&A | depreciation | capex | OE (c)=capex | OE (c)=depreciation | OE (c)=D&A | capex/depr. | acquisitions |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 3,141 | 123 | 443 | 410 | 593 | **2,425** | 2,608 | 2,575 | 1.45 | 5 |
| 2017 | 3,054 | 127 | 475 | 440 | 553 | **2,374** | 2,487 | 2,452 | 1.26 | 0 |
| 2018 | 3,056 | 109 | 511 | 452 | 436 | **2,511** | 2,495 | 2,436 | 0.96 | 728 |
| 2019 | 3,133 | 100 | 519 | 457 | 335 | **2,698** | 2,576 | 2,514 | 0.73 | 1,711 |
| 2020 | 3,719 | 107 | 539 | 451 | 410 | **3,202** | 3,161 | 3,073 | 0.91 | 353 |
| 2021 | 3,325 | 135 | 556 | 467 | 567 | **2,623** | 2,723 | 2,634 | 1.21 | 0 |
| 2022 | 2,556 | 125 | 545 | 465 | 696 | **1,735** | 1,966 | 1,886 | 1.50 | 809 |
| 2023 | 3,745 | 122 | 567 | 495 | 705 | **2,918** | 3,128 | 3,056 | 1.42 | 0 |
| 2024 | 4,107 | 135 | 605 | 530 | 561 | **3,411** | 3,442 | 3,367 | 1.06 | 0 |
| 2025 | 4,198 | 155 | 630 | 552 | 564 | **3,479** | 3,491 | 3,413 | 1.02 | 293 |
| TTM to 2026-06-30 | 4,456 | 178 | 642 | n/a | 598 | **3,680** | | 3,636 | | 0 |

**Owner earnings is positive in every year of the window, and its worst year — 2022, the input-cost year — was still
$1,735M.** Share-based compensation has never exceeded 4.9% of operating cash flow and averages 3.6% across the decade, so
shape #2 in the survival-shapes index does not apply.

**THE WINDOWS, AND THE SPREAD IS PART OF THE RANGE [E2-42, E4-25].** The corpus's default is five years; more than one window
is run and the spread carried.

| window | OE (c)=capex | OE (c)=D&A | **less the working-capital release (the conservative read)** |
|---|---|---|---|
| **5-yr 2021-25 — the [E2-42] default** | **2,833** | 2,871 | **2,763** |
| 10-yr 2016-25 — the post-Venezuela perimeter | **2,738** | 2,741 | **2,680** |
| 5-yr 2020-24 | 2,778 | 2,803 | 2,695 |
| 5-yr 2021-25 excluding 2022 | 3,108 | 3,118 | 2,851 |
| 3-yr 2023-25 | 3,269 | 3,279 | **2,879** |
| TTM to 2026-06-30 *(one twelve months, not a mean)* | 3,680 | 3,636 | not computed |
| 11-yr 2015-25 *(crosses the Venezuela perimeter: shown, not used)* | 2,683 | 2,707 | — |

**THE RANGE CARRIED TO Q5: owner earnings of about $2.7bn to $3.3bn a year, centred on the five-year default of $2,833M,
with $3,680M as the trailing-twelve-months reading and $2,680M as the most conservative.** *"working with a range of
possibilities is the better approach"* **[E4-25]**. **The three-year and TTM readings are the ones to distrust, not the
ten-year one**: the three-year window carries a mean working-capital release of **+$390M a year** against **+$58M** across
the decade, which is most of the difference between $3,269M and $2,738M.

**THE WINDAGE COUNT, because conservatism is spent once.** It has been spent **twice** and both are named: (1) (c) is set at
total capital expenditures rather than at the depreciation the corpus's own default prescribes, on the [E4-47] argument above;
(2) the working-capital release is stripped in the conservative column. The ESOP-dividend deduction the draft carried would
have been a **third** and it has been removed as unjustified. **Unwinding both would put the five-year figure at $2,871M rather
than $2,763M — a 4% band.** The count is stated so Q5 cannot spend it again.

### GREAT, GOOD OR GRUESOME — [E4-20]
**GREAT, and the arithmetic says so rather than the adjective.** *"The great one pays an extraordinarily high interest rate
that will rise as the years pass."* Owner earnings per diluted share ran **$2.70 (2016) to $4.29 (2025)**, about **+5.3% a
year**, on net tangible operating assets that **fell** from $4,083M to $4,128M in nominal terms while sales rose 34%. Capital
expenditure has never exceeded 3.9% of sales. This is the opposite of *"the worst sort of business ... grows rapidly, requires
significant capital to engender the growth, and then earns little or no money."* **The qualification, recorded:** the rise in
the rate came from price and from the share count, not from units (Q2: worldwide volume +7.7 points in ten years), so the
"rise as the years pass" clause depends on pricing continuing to outrun costs. **[E4-43]'s caution is noted and not needed
here** — nothing in the record puts Colgate in the *good* class, let alone the gruesome one.

### STAYING POWER — all three scored [E5-11], including the third
1. **A large and reliable stream of earnings: YES.** Net cash provided by operations in every year 2016-2025: 3,141, 3,054,
   3,056, 3,133, 3,719, 3,325, **2,556**, 3,745, 4,107, 4,198. **Never negative, never below $2.5bn, and the trough year was
   the worst raw-material year of the decade.** Two thirds of sales are outside the United States and 45% in emerging markets,
   which is diversification of demand as well as exposure to currency.
2. **Massive liquid assets: NO, and this is scored honestly as a fail rather than argued around.** Cash was **$1,370M at
   2026-06-30** on $16,790M of assets, with current marketable securities not even a separate balance-sheet line. Colgate does
   not carry a fortress balance sheet; it carries a fortress cash flow. **[E2-61]'s sector scope does not rescue it** — that
   carve-out is for insurers and float businesses, and Colgate is neither. **[E5-39] is the standard that is not met:** the
   10-K describes an *"undrawn revolving credit facility supporting our commercial paper programs"*, which is exactly the
   *"kindness of strangers"* the corpus refuses to depend on. **Recorded as the single weakest item in Q4.**
3. **No significant near-term cash requirements: YES, and this is the one most often skipped.** The filed maturity schedule,
   excluding commercial paper: *"2026 | $ | 1,115 | 2027 | 523 | 2028 | 615 | 2029 | 591 | 2030 | 500 | Thereafter | 4,495 |
   Total | $ | 7,839"*. **The largest single year is $1,115M against $4,198M of operating cash flow**, and by 2026-06-30 debt
   payable within one year had already fallen to **$34M** from $1,117M. **Supplier finance is not a hidden maturity:** the
   obligations *"are included in Accounts Payable"* and *"were not material"*. **Pensions are not one either:** United States
   plans are underfunded $441M, international $179M, other retiree benefits $663M — about $1,283M in total, against $4.2bn of
   annual operating cash flow.
- **The coverage test [E2-54]** — *"all interest, both payable and accrued, to be comfortably met out of current cash flow net
  of ample capital expenditures"*: **interest paid $270M in 2025 against $4,198M less $564M of capex, or $3,634M — 13.5x.**
  **Comfortably met**, on the corpus's own construction with capex taken out first.
- **Read the terms, not just the quantity [E3-52].** Colgate's liabilities are the opposite of float: $7,839M of dated,
  covenanted debt, most of it *"Thereafter"*. But its **working capital is negative**, so its suppliers and its customers
  together fund a part of the business without covenants or due dates of the kind that force a sale. The negative working
  capital is a genuine, if small, float-like benefit, and it is named rather than counted twice.
- **Jurisdiction [E3-66].** The registrant is a Delaware corporation on the NYSE, so United States shareholders stand where the
  corpus says they stand best. **But the earning assets do not:** plants in over 80 countries, operations in over 200, with the
  10-K naming *"challenges to our ability to repatriate cash from Russia"* and $1,234M of the $1,288M of 2025 year-end cash
  sitting in foreign subsidiaries. **Where the cash is earned is not where the shareholder stands**, and that gap is recorded.
- **[E2-55] and [E5-29]:** scored on the worst case rather than the expected one, the 2022 trough is the test and it passed
  ($1,735M of owner earnings, 13x interest cover, no covenant event). Volatility in the earnings stream is not risk here;
  impairment of the earning power is, and that is the next section.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES — [E2-27, E3-24, E4-40, E4-51]
**It does not die of its balance sheet. It dies of who owns the shelf.** Stated in the form **[E4-51]** demands, as a bear case
its holders would accept as fairly put, and modelled on **exposure, not experience [E4-40]**.

**The mechanism, from the filing's own words.** Colgate owns the trademark and rents the route to the buyer. The counterparty
that owns that route *"exercise[s] greater bargaining strength than we do, including the exclusive access to valuable
first-party consumer data and analytics"*; it *"ha[s] demanded and may continue to demand higher trade discounts, allowances,
slotting fees, significant investment (including through display media, paid search and co-op programs) or changes to product
assortments, which have led to and could continue to lead to reduced sales or profitability in certain markets"*; it applies
*"AI-aided category pricing pressures and algorithms"*; and it stocks its own *"'private label' products ... which are
typically sold at lower prices than branded products"* on the same shelf. **Walmart alone is *"approximately 11%"* of net
sales**, and the same 11% is filed for 2025, 2024 and 2023. **Trade promotion is deducted from net sales before they are
reported**, so the transfer to the retailer never appears as a line an owner can watch.

**Quantified from filed figures, in the [E3-24] form.** North America is the case where the mechanism has already run, and it
is the only region where retail is concentrated:
- Net selling price: **-1.9% (2024), -0.2% (2025)** — two consecutive years of price given back.
- Volume: **-9.3 points cumulative over 2021-2025.**
- Segment operating margin: **32.4% in 2016** (before skin health was placed in the segment) against **21.5% in 2025** on the
  8-K recast basis that takes skin health back out (net sales $3,679M, operating profit $790M). **About eleven points of margin
  in nine years, or roughly one point a year, like for like.**
- **The model:** if that North American path ran across the whole company for a decade, the 2025 operating margin of **20.7%
  ex-impairment** would fall toward **10-11%**, and owner earnings would roughly **halve, from about $2,833M to about
  $1,450M** — a business still comfortably solvent, still covering its interest 6-7x, and worth less than half of what Q5 is
  about to compute.
- **The likelihood, in the corpus's vocabulary: a REAL POSSIBILITY for the developed-market third, a LOW-LEVEL POSSIBILITY for
  the whole company.** The reason is in the same filings: retail is concentrated in North America and parts of Europe and not
  elsewhere, and the regions where it is not concentrated did not lose margin over the decade — **Latin America 31.0% to
  29.6%, Europe 24.7% to 25.3%, Africa/Eurasia 19.4% to 21.8%, Asia Pacific 31.7% to 27.0%**, against North America's 32.4% to
  21.5%. **Two thirds of the profit sits where no single customer has 11% of anything.** That is what keeps this a
  low-level possibility for the company and a real one for a third of it.
- **[E2-27]'s collective-irrationality mechanism is the aggravator and is named:** every branded staple in the Q2 row raised
  price 2021-2023 and gave some back in 2025, and each one's advertising rose as a share of sales. *"Viewed individually, each
  company's capital investment decision appeared cost-effective and rational; viewed collectively, the decisions neutralized
  each other."* Advertising at 13.3% of sales that holds a share still 3.4 points below 2015's is that pattern in miniature.
- **Exposure, not experience [E4-40].** The benign reading — that Colgate has held 39-45% of global toothpaste for twelve years
  and earns 79-101% pre-tax on tangible operating capital — is the *experience*. The *exposure* is one customer at 11%,
  retailer consolidation the 10-K says *"may further increase our concentration risk"*, a private-label substitute on the same
  shelf, and algorithmic category pricing the filing names by name.

**SURVIVAL SHAPE.** Against `Screens/SURVIVAL SHAPES - index.md`: this is close to **#11 THE PASS-THROUGH** but is not it — the
gains are not competed away by rivals or absorbed by suppliers, they are **taken by one concentrated counterparty at the point
of sale**. It is the inverse of **#13 THE TENANT**: there, the product is rented and the rent is reset; here the **product is
owned outright and the distribution is rented**. **A new shape is therefore proposed, pending the operator, in the form the
other six proposals used: #19 THE SHELF — the brand is owned, but the route to the buyer is rented from a counterparty who
stocks a cheaper copy beside it, holds the buyer's data, and reprices the terms every year.**

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *IN on survival, without strain. **Owner earnings exist, are built by hand from the filed cash-flow statements, and are
  positive in every year of the perimeter window**, with a worst year of $1,735M in 2022 and a range carried to Q5 of about
  **$2.7bn to $3.3bn**, centred on the five-year default of **$2,833M**, with the windage spent twice and counted. **[E5-20] was
  asked on the filing and answered: Colgate is not in the exception class**, capex being 1.15x depreciation and 1.01x D&A over
  the decade; (c) is nevertheless set at total capex on **[E4-47]**'s inflation condition, evidenced by Latin America's own
  1.35x. **[E4-20]: GREAT** — owner earnings per share compounded 5.3% a year on tangible operating capital that did not grow.
  **Staying power scores 2 of 3 [E5-11]:** the earnings stream and the maturity profile pass comfortably (interest covered
  **13.5x** after capex, largest maturity year $1,115M against $4,198M of operating cash), and **strength 2 fails — $1,370M of
  cash is not "massive liquid assets", and the filing points at an undrawn revolver behind its commercial paper, which is
  [E5-39]'s kindness of strangers.** That is recorded as a real weakness and it is not what kills this business. **The named
  death is not insolvency but the slow transfer of the franchise's rent to the owner of the shelf**, modelled above at roughly
  a halving of owner earnings over a decade, **a real possibility for the developed-market third and a low-level possibility
  for the whole**, because two thirds of the profit is earned where no customer has 11% of anything. The file continues to Q5.*
