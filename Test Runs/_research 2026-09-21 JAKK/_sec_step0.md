## STEP 0 - THE RATE, THE FILING, THE CAP, AND THE FOUR SCREEN FLAGS

**Sovereign, for the currency the business EARNS in** - the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34 %** · date **2026-09-18** · source **US Treasury daily par yield curve, 30-year
  par yield, from the issuing authority** (`tools/sources.py::sovereign('USD')`, fetched
  2026-09-21). 2026-09-21 is a Monday and the newest published print is the prior Friday's;
  that is the date named. **FRED DGS30 was not used and is the fallback, not the source.**
  *Struck this session. No rate was inherited from the dispatch brief, which deliberately gave none.*
- FX: none. JAKKS reports in USD. 27.0% of FY2025 net sales were generated outside the United
  States ($154.1 million) but the reporting and earnings currency is USD, so USD is the sovereign.

**PRICE - aggregator, live quote only, and flagged as such [operator rule 5].**
- **$24.085**, Yahoo Finance chart API, regularMarketTime **2026-09-21 13:44:46 UTC** (09:44 ET,
  market open). Raw metadata saved to `Test Runs/_research 2026-09-21 JAKK/price_raw_aggregator.json`.
- The prior closes, so an outlier print is visible: **23.79 (09-10) · 24.17 (09-11) ·
  24.33 (09-14) · 24.31 (09-15) · 24.24 (09-16) · 24.33 (09-17) · 24.13 (09-18)**. The live
  print sits inside a seven-session range of 23.79-24.33. **No outlier.**

**SHARES - off the cover of the newest periodic filing, verbatim.**
> *"The number of shares outstanding of the issuer's common stock is **11,445,012** as of
> **July 31, 2026**."* - Form 10-Q for the quarter ended June 30, 2026, cover page.

- Document: 10-Q, period **2026-06-30**, **filed 2026-07-31**, accession **0001185185-26-003186**.
- **Second class: none.** The FY2025 10-K cover says it in terms - *"The number of shares
  outstanding of the registrant's Common Stock, $.001 par value (**being the only class of its
  common stock**), is 11,444,411 as of March 2, 2026"* (accession 0001185185-26-000723). The
  Series A Senior Preferred issued in the 2019 Recapitalization was **redeemed in full on
  2024-03-11** for $20.0 million cash plus 571,295 common shares valued at $15.0 million
  (Note 13). Nothing preferred is outstanding.
- **Split after the measurement date: none.** `split_factor_after('JAKK','2026-06-30') = 1.0`.
  *(There is a 1-for-10 reverse split dated 2020-07-10 in the full history. It is older than
  every anchor used here and does not enter the cap; it does enter any per-share series read
  from a pre-2020 filing, and is flagged for that reason.)*

**THE CAP, STRUCK BY HAND, AGAINST THE SCREEN'S.**
`cap = close(anchor) x shares(measurement) x splits AFTER measurement`; `close`, never `adjclose`.

    24.085 x 11,445,012 x 1.0 = $275.65 million

- **Screen's figure: 291.** It does **not** reproduce at today's price, and **the gap is a stale
  price, not a count error.** Struck at the same share count and the close of **2026-08-28
  ($25.42)**, the formula gives **$290.93 million**, which is the screen's 291. The screen row
  was generated 2026-09-02. **Same 11,445,012 count, different day.**
  The stock has fallen 5.3% since. **Every yield in the screen row is therefore 5.3% too low**,
  which is the conservative direction, and the hand-struck cap of **$275.65M** governs everything
  below.

**THE FILING WAS READ** - not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **FY2025 Form 10-K**, period ended 2025-12-31, **filed 2026-03-02**, accession
  **0001185185-26-000723** (`10K_FY2025.htm` in the research folder). Also read in full:
  **FY2021 Form 10-K**, filed 2022-03-16, accession **0001185185-22-000288** (for screen flag 1);
  **Q2 FY2026 Form 10-Q**, filed 2026-07-31, accession **0001185185-26-003186**; and the
  **8-K of 2026-07-24**, accession **0001185185-26-003108**, with its earnings release exhibit.
- **Figure cross-checked against the filed statement:** the FY2025 MD&A states royalty expense at
  **16.2% of net sales**; the filed consolidated statement of operations tags royalty expense at
  **$92.4 million** against net sales of **$570.7 million**, which is **16.19%**. Agrees. Three
  further lines were tied from the filed FY2025 cash-flow statement to the XBRL series used below:
  operating cash **$8,492k**, purchases of property and equipment **$9,563k**, share-based
  compensation **$10,913k**. All three agree to the dollar.

---

### THE FOUR LIVE SCREEN FLAGS - each resolved here, before Q1 opens

Screen row, `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv` line 47. **Machine output, not a
finding; carried unlabelled** [operator rule 8: tools fetch and compute and are forbidden to conclude].

#### FLAG 1 - `wc_note`: "ONE LINE MADE THE CASH: AccountsPayable moved 336% of 2021 OCF."
**The ratio reproduces to the decimal. The sentence around it is wrong three ways, and the fourth
break is a structural defect in the tool.**

Reproduced from the **filed** FY2021 consolidated statement of cash flows (10-K accession
0001185185-22-000288, in thousands):

| FY2021 line, as filed | $k | x FY2021 OCF |
|---|---|---|
| **Inventory** | **(45,312)** | **7.71x** |
| **Accounts receivable** | **(43,743)** | **7.44x** |
| Accounts payable and payable to Meisheng | **25,017** | 4.26x |
| *- of which trade AP, as tagged* | *19,751* | ***3.36x*** |
| Accrued expenses | 7,767 | 1.32x |
| Prepaid expenses and other assets | 7,330 | 1.25x |
| Reserve for sales returns and allowances | 4,177 | 0.71x |
| **Net cash used in operating activities** | **(5,879)** | |

**19,751 / 5,879 = 3.3595 = 336%.** The number is exactly right.

1. **"ONE LINE MADE THE CASH" is impossible here: there was no cash. FY2021 operating activities
   USED $5.879 million.** The denominator is negative and near zero, so the 336% is a fact about a
   vanishing denominator, not about a large numerator. The AP move is **3.2% of FY2021 net sales**
   ($19.8M on $621.1M) - unremarkable for a toy company's Q4 payables. The same year's *total
   adjustments* line is **+$9 thousand**: the whole reconciliation from a net loss of $5,888k to
   operating cash of $(5,879)k nets to nine thousand dollars. Every large line offset another.
2. **AP was the THIRD-largest working-capital line, not the largest.** Inventory (7.71x) and
   accounts receivable (7.44x) are both more than double it. Had the flag named the largest it
   would have printed **771%**. *(The last two cycles found the flag naming the second-largest;
   this cycle it named the third.)*
3. **Direction: not inverted this time.** Accounts payable genuinely was a **source** of cash
   (+$25.0M as filed). But the **net working-capital swing for FY2021 was a $45.8 million USE of
   cash**, so a reader told "one line made the cash" takes away the opposite of what the year did.
4. **A fourth break, in the tool's own numbers: the flag understates its own line by 27%.**
   `WC_TAGS` in `Screens/floor_screen.py` reads `IncreaseDecreaseInAccountsPayable` only. JAKKS
   splits the filed line across **two** tags - `IncreaseDecreaseInAccountsPayable` 19,751 **plus**
   `IncreaseDecreaseInAccountsPayableRelatedParties` 5,266 (the Meisheng half) = the filed 25,017.
   The true filed ratio is **425%**, not 336%.

**THE STRUCTURAL DEFECT, and it is the generalisable one.** `WC_TAGS` is a four-item list:
`IncreaseDecreaseInAccountsPayableAndAccruedLiabilities`, `IncreaseDecreaseInAccountsPayable`,
`IncreaseDecreaseInContractWithCustomerLiability`, `IncreaseDecreaseInDeferredRevenue`. **It
contains no receivables tag and no inventory tag.** The flag's docstring says it fires when a
single working-capital line moves by more than 30% of a year's operating cash and *"names the year
and the line"* - but it can only ever name a *payable*. At JAKKS the two largest working-capital
lines in the flagged year are structurally invisible to it. This is the class of defect the
resume-state note calls *"a guard that reads the aggregate cannot see a defect that lives in the
components"*, one level down: **a guard that reads four tags cannot see a line that is tagged with
a fifth.** *Reported to the operator, not fixed here: operator rule 6 and PRIME RULE 5.*

**THE CAUSE IN THE BUSINESS, from the FY2021 10-K's own liquidity note** - and it names the two
lines the flag could not see:
> *"The decrease in cash flows provided by operating activities was primarily due to **higher
> working capital usage driven by an increase in accounts receivable due to higher Q4 sales and a
> higher inventory balance resulting from an increase in freight-in-transit**, partially offset by
> a lower net loss and higher non-cash charges related to valuation adjustments for our convertible
> senior notes and preferred stock derivative liability."* - FY2021 10-K, Item 7, Liquidity and
> Capital Resources

So the registrant's own explanation of FY2021 is receivables and in-transit freight - the 2021
supply-chain year, with goods on the water at year end and a heavy Q4 ship. **Accounts payable is
not mentioned.** The seasonal-payables hypothesis the brief offered is refuted for this year:
payables rose, but they rose less than half as much as the working capital they were funding.

**Verdict on flag 1: ratio REPRODUCED (336%, and 425% on the full filed line); the finding it
carries is BROKEN.**

#### FLAG 2 - `best_year_dep_oe` 0.892 with `best_year_dep` 0.44, "TWO YEARS JOINTLY CARRY THE WINDOW"
**Both reproduce to three decimals, and the two years are FY2022 and FY2023.**

Nine-year owner-earnings series (operating cash - SBC - capex, $m, XBRL newest vintage; FY2021 and
FY2023-25 tied by hand to the filed cash-flow statements):

| FY | 2017 | 2018 | 2019 | 2020 | 2021 | **2022** | **2023** | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| OE (capex end) | -6.6 | -14.8 | 9.5 | 33.0 | -16.2 | **70.6** | **49.5** | 18.2 | -12.0 |

- mean of nine = **$14.57M**; drop the best one (FY2022) = **d1 0.4808**; drop the best two
  (FY2022 + FY2023) = **d2 0.8916** = the screen's 0.892. The pair test fires (d2 > 0.25 and
  d2 >= 1.8 x d1).
- The same on the nine-year **operating-cash** series (11.4, -0.6, 21.8, 43.6, -5.9, 86.1, 66.4,
  38.9, 8.5): mean $30.03M, **d1 0.2334, d2 0.4399** = the screen's 0.44.

**Plainly: FY2022 and FY2023 carry the band, and without them there is no band.** The five-year
window the screen priced (FY2021-25) contains both. Remove them and the three years that remain -
FY2021, FY2024, FY2025 - average **-$3.34M** at the capex end and **-$3.84M** at the D&A end.
**The owner-earnings mean goes negative.**

**Verdict on flag 2: REPRODUCED exactly, and it is the most important number in the row.**

#### FLAG 3 - both `level_note` and `level_note_oe` are REFUSALS. A refusal is a work order.
The CSV strings are truncated: *"EARLY HALF STRADDLES ZERO - the pre-window years run from
$-16.2M to $..."*. **Completed here, and then extended to the whole filed history, because
`years_filed` says 17 and the band was built on 5.**

- The truncated string completes as **"$-16.2M to $70.6M"** (the OE series' 2017-2022 half) and,
  on the OCF series, **"$-5.9M to $86.1M"**. Both halves straddle zero, which is why the ratio
  refused, and **the refusal was correct**.
- **The seventeen filed years, which is what the work order is actually for** (FY2009-FY2025,
  owner earnings = operating cash - SBC - capex, $m):

| FY | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 |
|---|---|---|---|---|---|---|---|---|---|
| OE | 78.1 | 51.5 | 30.2 | 10.0 | **-33.6** | **-91.1** | 46.4 | 0.3 | -6.6 |

| FY | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| OE | -14.8 | 9.5 | 33.0 | -16.2 | 70.6 | 49.5 | 18.2 | -12.0 |

**Eight of seventeen filed years are negative.** FY2013 and FY2014 together consumed **$124.7
million** of owner earnings - roughly 45% of today's entire market capitalisation - and FY2009
carried a net loss of $385.5M. This is not a series with a level to shift; it is a series that
crosses zero repeatedly across seventeen years. **The refusal was the right answer, and the
pre-window years are worse than the window, not better.**

#### FLAG 4 - `spread_caveat`: "4-construction width only ... rebuild it [E4-25]"
The published band **$19M to $22M**, spread 0.187, reproduces exactly: the four constructions are
3y/capex **18.55**, 3y/D&A **18.83**, 5y/capex **22.02**, 5y/D&A **21.74**; low 18.55, high 22.02,
(22.02-18.55)/18.55 = **0.1869**. `yield_bottom` 18.55/291 = **0.0637**. Every published number in
the row reproduces.

**COMPUTATION - NOT A CLEARANCE.** *(Operator rule 3. Q1-Q4 have not been answered. No entry
language attaches to anything below, and this is a rebuild of a screen artifact, not a valuation.)*

| window | n | capex end | D&A end |
|---|---|---|---|
| 3 years (FY2023-25) | 3 | 18.55 | 18.83 |
| **5 years (FY2021-25) - what the screen priced** | 5 | **22.02** | **21.74** |
| 9 years (FY2017-25) | 9 | 14.57 | 11.95 |
| 10 years (FY2016-25) | 10 | 13.15 | 9.97 |
| **17 years - the full filed history** | **17** | **13.11** | **6.98** |
| full history excluding FY2022 and FY2023 | 15 | **6.86** | **-0.10** |
| the 5-year window excluding FY2022 and FY2023 | 3 | **-3.34** | **-3.84** |

**The screen's band is the narrowest and the highest construction available.** Widened to the full
filed history the range is roughly **$7M to $13M**, not $19M to $22M - the screen's floor is
**2.7x** the seventeen-year D&A-end mean and **1.4x** the seventeen-year capex-end mean. [E4-25]'s
own words: *"working with a range of possibilities is the better approach"*, and *"usually, the
range must be so wide that no useful conclusion can be reached."* The rebuilt range runs from
**-$3.8M to +$22.0M** across constructions and windows. **The spread of 0.187 was a width of four
constructions sharing two boom years, not a range of outcomes.**

*(Which end of the capex band is legitimate is a Q4 judgment and is not made here. Noted only:
JAKKS' capital spending is almost entirely **molds and tooling** - the FY2021 10-K says investing
"consisted primarily of cash paid for the purchase of molds and tooling used in the manufacture of
our products" - and its D&A is dominated by amortization of tools and molds, which the FY2025
income statement carries at 1.7% of net sales inside cost of sales. The two ends run within
$0.3-6M of each other in most years, so the capex band is not what moves this name.)*

---

### THE EMPTY SCREEN FIELDS - empty is not cleared, and the screen did not look

`cap_flag`, `deal_note`, `name_change_note`, `acq_note`, `da_note`, `flags_disagree` and
`window_disagree` are all blank on this row. Read by hand from the 10-K's equity, related-party,
debt and subsequent-event notes, the 10-Q, and the 8-K list:

1. **A capital-structure event the blank `deal_note` missed: the Series A Senior Preferred was
   redeemed on 2024-03-11** for **$20.0 million cash plus 571,295 common shares valued at $15.0
   million** at $26.26, settling a $29.9 million derivative liability and $6.0 million of accrued
   dividends (Note 13, FY2025 10-K). That is **5.0% of today's share count issued** inside the
   priced window, and $20M of cash out. The FY2024 owner-earnings figure in every construction
   above sits in the year that paid for it.
2. **A financing perimeter change: the JPMorgan ABL facility was replaced by a new BMO revolving
   credit agreement on 2025-06-24**, with financial covenants (minimum Consolidated Interest
   Coverage Ratio of 3.00:1.00 and a maximum Total Net Leverage Ratio), guaranteed by US, Canadian
   and Hong Kong subsidiaries (10-Q note, June 30 2026).
3. **The long-standing Meisheng relationship changed status and the screen has no field for it.**
   Hong Kong Meisheng Cultural Company Limited **ceased to be a related party** after the 2025
   annual meeting, having fallen below 10% and lost its board designee (Note 10). It remains a
   major contract manufacturer: payments of **$75.3 million (2025) and $98.4 million (2024)** -
   **13.2% and 14.2% of net sales.** A supplier of that size ceasing to be a "related party" means
   *less* disclosure going forward on a relationship that did not shrink.
4. **A dividend was initiated in 2025; there was no dividend in 2024.** Four quarterly dividends of
   $0.25 were paid in 2025 ($11.2 million total); the same $0.25 has been declared each quarter
   through the 8-K of 2026-07-22. **Cash dividends began in the year owner earnings went negative.**
   Against [E2-52]'s test: no shares were sold to fund it - the ATM has never been drawn and the
   2022 shelf **expired unused in 2025** - so this is not the Peter-and-Paul case; but it is a
   payout begun as the earnings stream turned.
5. **A new S-3 was filed 2025-10-29** (accession 0001185185-25-001567), after the 2022 shelf
   expired. Nothing has been sold under it.
6. **Tariffs, and a non-recurring credit inside the newest periodic figures.** The Q2 FY2026 10-Q
   records **$11.1 million refunded by the federal government related to import tariffs** (IEEPA),
   sitting in non-operating income, and the earnings release attributes the quarter's swing from a
   $2.3M loss to $5.9M of net income to exactly that: *"driven by refunded tariff expenditures
   reflected in Non-Operating Income."* **[E4-41]** - a favourable exogenous break is named and
   removed before any mean is trusted.

**Nothing found is a merger, a name change or a segment redefinition.** The six items are
capital-structure, financing, supplier-status, payout and tax-refund events. **The screen looked at
none of them**, and items 1, 4 and 6 all touch figures the screen priced.

---
