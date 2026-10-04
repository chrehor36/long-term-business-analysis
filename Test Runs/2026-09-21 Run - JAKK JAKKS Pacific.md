# Company Run - JAKKS PACIFIC, INC. (JAKK) - 2026-09-21
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Wave 7, name 22 of 218. Unattended overnight cycle; nobody answered a question.
Research folder: `Test Runs/_research 2026-09-21 JAKK/`.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS - every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order - not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation - it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
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
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics, in my own words, without management's language.**

JAKKS is not a toy manufacturer and it is not an IP owner. It is a **middleman between other
people's characters and two retailers' shelves.** The cycle, from the FY2025 10-K:

1. **Rent a character.** JAKKS signs licences with Disney, Nickelodeon, Pixar, Marvel,
   NBCUniversal, Microsoft, Sega, Sony, Netflix, WarnerMedia, Nintendo, BBC, Hasbro and others.
   *"Generally, our license agreements for products and concepts call for royalties ranging from
   1% to 22% of net sales, and some may require minimum royalty guarantees and up-front or
   advanced royalty payments against those guarantees."*
2. **Design a toy around it**, nine to eighteen months from concept to shipment (three to nine
   when pushed). Some of the design is bought too: third-party inventors take *"1% to 5% of the
   wholesale sales price"* on concepts JAKKS accepts.
3. **Have somebody else build it.** *"We contract the manufacture of most of our products to
   unaffiliated manufacturers located in The People's Republic of China."* One of them, Hong Kong
   Meisheng, took **$75.3 million in 2025 and $98.4 million in 2024** - 13.2% and 14.2% of net
   sales. JAKKS owns the **molds and tooling**, which is almost the whole of its capital spending,
   and owns no factory.
4. **Sell it to two customers.** *"Our two largest customers are Target and Walmart, which
   accounted for 26.6% and 26.1%, respectively, of our net sales in 2025."* **52.7% of revenue to
   two buyers**; in 2024 Target, Walmart and Amazon were 29.6%, 26.2% and 10.6% - **66.4% to
   three.** Many customers *"take title to the goods in China."*
5. **Keep the spread.** FY2025, as the filed income statement lays it out as a percentage of net
   sales: cost of goods 49.7%, **royalty expense 16.2%**, amortization of tools and molds 1.7% -
   cost of sales 67.6%, gross profit 32.4%; then direct selling 6.4% and G&A 23.4%; **income from
   operations 2.5%.**

That last line is the whole business in one number, and it is worth stating plainly: **the
licensors take 16.2 cents of every sales dollar and the shareholder is left with 2.5 cents of
operating income.** The rented input costs six and a half times what the operation earns.

Two segments, and they are simply two shelves: **Toys/Consumer Products $461.9M** and **Costumes
(Disguise) $108.7M** in FY2025 (Note 3). Seasonality is extreme and disclosed - *"In 2025, 57.9%
of our net sales were made in the second and third quarters"* - with Costumes shipping into
Halloween.

**The scarce input this business controls.** *This is the question, and the honest answer is the
finding.* There are exactly two scarce inputs in the chain above, and **JAKKS owns neither**:

- **The characters.** Owned by Disney, Nintendo, Universal, Netflix, Hasbro and the rest, rented
  under agreements that expire and are re-bid. JAKKS' own risk factors say the rivals bid for the
  same ones: *"Our competitors have obtained and are likely to continue to obtain licenses that
  overlap our licenses with respect to products, geographic areas and retail channels."*
- **The shelf.** Owned by Walmart and Target. JAKKS' own risk factors: *"We cannot assure you that
  we will be able to obtain adequate shelf space in retail stores to support our existing
  products."*

What JAKKS does control is real but not scarce: a portfolio of owned brands (Disguise, Perfectly
Cute, Fly Wheels, Moose Mountain, Maui, ReDo Skateboard Co., Sky Ball, Xtreme Power Dozer), a mold
and tooling base, a sourcing network in China, and an in-house design and sales organisation. Every
one of those can be bought by a competitor at a price, and the 10-K says so: *"the toy industry has
no significant barriers to entry."* **Recorded here as an observation, not a verdict; it is Q2's
question and Q2 answers it.**

**Will the fundamentals look broadly the same in ten years?** **Yes, and that is what makes Q1
IN.** Children will still want toys; mass retailers will still sell them; entertainment companies
will still licence characters to people who make plastic; somebody will still tool a mold in Asia.
[E3-31] asks whether the business is *"relatively simple and stable in character"* and whether I
can *"realistically define what I don't know"*. This business is simple - it is a spread between a
licence and a shelf - and I can define what I do not know: **which characters will be hot in 2031,
and whether JAKKS will hold their licences.** That is not an understanding problem. It is a
durability problem, and the framework has a question for it.

**[E4-46] checked, because it is the trap at this gate.** *"If we can't make a decision in five
minutes, we can't make it in five months."* Nothing here needs five months. The 10-K's own income
statement gives the unit economics in seven lines. No fetch would repair an understanding deficit,
because there is no understanding deficit.

**[E5-13] checked the other way.** *"About a dozen truly good decisions - that would be about one
every five years."* Most names should end at Q1 and this one does not, which is not a compliment
to JAKKS; it is a statement that the toy-marketing business is legible.

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE

*No caveat attaches to this IN. The filings read are named at Step 0; the unit economics above are
taken from the filed income statement and Item 1 of the FY2025 10-K (accession 0001185185-26-000723),
not from tagged data.*

## Q2 - IS IT A FRANCHISE? **[E3-03]**

- **Needed or desired [x]** · **no close substitute [ ]** · **not price-regulated [x]**

**Criterion 1 passes.** Children want toys and costumes; Target and Walmart want a supplier who is
not one of the two dominant ones. JAKKS' own 10-K makes that second point for itself: *"the ongoing
consolidation of toy companies provides us with increased growth opportunities due to retailers'
desire to not be entirely dependent upon a few dominant toy companies."*

**Criterion 3 passes on its face** - no toy price is administered. But [E2-59]'s point is that
regulation *caps* a franchise and *floors* a commodity business; the absence of a cap says nothing
about whether there is a franchise to cap. Note what the 10-K does say about the regulation it has:
CPSA/CPSIA safety testing at the manufacturers' facilities. That is a cost of entry, not a barrier,
and the registrant says so below.

---

### Criterion 2 fails, and it fails on the registrant's own filed words

**The single sentence that decides this file**, from the FY2025 10-K's risk factors (accession
0001185185-26-000723, Item 1A, "There are risks associated with our license agreements"):

> *"**Sales of products under trademarks or trade or brand names licensed from others account for
> substantially all of our net sales.** Product licenses allow us to capitalize on characters,
> designs, concepts and inventions owned by others…"*

**Substantially all of net sales come from somebody else's property.** Everything that follows is
the consequence, and the registrant states each consequence itself:

> *"Intense competition exists for desirable licenses in our industry. **We cannot assure you that
> we will be able to secure or renew significant licenses on terms acceptable to us.**"* - Item 1A

> *"**Our competitors have obtained and are likely to continue to obtain licenses that overlap our
> licenses** with respect to products, geographic areas and retail channels."* - Item 1A

> *"In addition, the **toy industry has no significant barriers to entry.** Competition is based
> primarily upon the ability to design and develop new toys, procure licenses for popular characters
> and trademarks, and successfully market products. **Many of our competitors offer similar products
> or alternatives to our products.**"* - Item 1A

> *"In many of our product lines **we compete directly against one or both of two of the toy
> industry's most dominant companies, Mattel and Hasbro.** In addition, we compete in our Halloween
> costume lines with Rubies II. We also compete with numerous smaller domestic and foreign toy
> manufacturers, importers and marketers in each of our product categories."* - Item 1, Competition

> *"…certain of our competitors have greater financial resources, larger sales and marketing and
> product development departments, stronger name recognition, **wholly-owned brands and properties
> with high consumer awareness and appeal**, longer operating histories and benefit from greater
> economies of scale. These factors, among others, **may enable our competitors to market their
> products at lower prices** or on terms more advantageous to customers than those we could offer."*
> - Item 1, Competition

A product that a buyer can replace with *"similar products or alternatives"* from rivals with
*"wholly-owned brands"*, in an industry with *"no significant barriers to entry"*, where the rivals
bid for and win *"licenses that overlap our licenses"*, **has close substitutes**. That is
[E3-03] criterion 2 failing on filed evidence, which is the **OUT** branch of the four verdicts -
the evidence is here and the business fails - not a perimeter close.

**And the control runs the wrong way on both sides at once.** The licensor sets the royalty
(*"1% to 22% of net sales"*), sets the minimum guarantee, approves the product (*"the licensors have
the right to review and approve our use of their licensed products, designs or materials before we
may make any sales"*), approves the contract manufacturer, limits the distribution channels, and
audits the royalty afterwards. The retailer sets the shelf. JAKKS sits between two parties that each
hold a veto.

---

### **[E4-04]** - the second, independent leg, applied as the 2026-09-20 ruling requires

*The ruling: [E4-04] is applied as a **competence limit**, never as a fourth franchise criterion; a
name whose durability cannot be judged from filings closes **UNKNOWABLE**, not OUT. **The test that
IS on the business** is whether the filings show an advantage that must be **rebuilt from zero**
each generation, as against a lead **maintained** through the generations.*

**This is judgeable from these filings, and they answer it.** JAKKS is not a rapid-change industry
and not a depleting asset; nothing here is *"far beyond our perimeter"* **[E4-58]**. So [E4-04] is
not used to close the file and is not needed to - criterion 2 already did - but it is scored, and
it scores the same way:

- **The basis is replaced, not defended.** The scope paragraph's own contrast: *Coca-Cola's
  advertising defends the same trademark; Mitsui's Rhodes Ridge buys a replacement deposit.* Every
  dollar JAKKS spends on royalty advances and minimum guarantees buys **the next term of somebody
  else's trademark**. When a licence lapses, nothing narrows - the product line ends, and the 10-K
  even names the wind-down clause: *"limitations of the time period in which we have to sell
  existing inventory upon expiration of the license."* That is the excluded class.
- **[E3-51], the surfing run, and management names the wave itself.** The FY2025 MD&A explains the
  year's 19.0% fall in the larger segment as: *"The Dolls, Role Play and Dress Up Division decreased
  22.6% year over year, **mainly due to limited theatrical releases** and lower sales within the
  Disney Princess and Style Collection businesses"*, and *"Within the Action Play & Collectibles
  Division, down 15.6%, **Sonic the Hedgehog 3 and the Sonic/DC collaboration added incremental year
  over year sales, while lower Nintendo sales offset those gains.**"* The Q2 2026 earnings release
  repeats it from the other side: the doll business was up *"**despite a lack of new entertainment
  properties in that division**."* The 10-K's risk factors state the dependence as a fact: *"The
  success of many of our character-related and theme-related products depends upon the popularity of
  characters in books, movies, television programs, video games… **any sudden disruption in that
  third party's release calendar can have negative repercussions for our business.**"* **The
  advantage lives in the wave, and Disney and Nintendo own the ocean.**
- **[E4-36], which of the four causes of extreme success is this?** Wave-riding, and only that.
  There is no extreme max/min of a controlled variable, no nonlinear combination, no extreme
  performance across many factors. Wave-riding is the one of the four that is explicitly not
  ownable.
- **[E2-53], the dominance class - the strongest reading of franchise - fails outright.** The
  newspaper test is *"Once dominant, the newspaper itself, not the marketplace, determines just how
  good or how bad the paper will be. Good or bad, it will prosper."* JAKKS is the registrant that
  writes *"we compete directly against one or both of two of the toy industry's most dominant
  companies"*. The marketplace determines JAKKS, not the reverse.
- **[E4-23], key-person dependence, recorded at Q2 as the framework requires.** Not a defect here:
  the moat question does not turn on Stephen Berman personally. Recorded so that the absence of the
  finding is on the record, not assumed.

---

### THE COMPETITOR ROW - required **[E3-28]**. A moat is a claim about *relative* position.

**The metric is royalty expense as a percentage of net sales**, and it is chosen because it is the
moat made arithmetic for this industry: it is exactly the fraction of the top line that is **rent
paid for somebody else's property**. It is a filed, tagged, audited line in all four registrants'
own 10-Ks (`us-gaap:RoyaltyExpense`), over the **same three fiscal years**, and it is immune to the
impairments and restructurings that distort the operating line.

| Company | royalty expense ÷ net sales, FY2023-25 aggregate | operating margin, same window | net sales FY2022 → FY2025 | source |
|---|---|---|---|---|
| **JAKKS Pacific (JAKK)** | **16.05%** ($316.8M on $1,973.3M) | **+5.73%** | $796.2M → $570.7M, **-28.3%** | FY2023/24/25 10-Ks, acc. 0001185185-26-000723 and prior |
| Funko (FNKO) | **16.60%** ($507.1M on $3,054.1M) | **-4.47%** | $1,322.7M → $908.2M, **-31.3%** | FNKO FY2023/24/25 10-Ks |
| Hasbro (HAS) | **7.81%** ($1,081.4M on $13,840.1M) | **-6.05%** *(see note)* | $5,856.7M → $4,701.3M, **-19.7%** | HAS FY2023/24/25 10-Ks |
| Mattel (MAT) | **4.69%** ($758.5M on $16,168.4M) | **+11.15%** | $5,434.7M → $5,347.6M, **-1.6%** | MAT FY2023/24/25 10-Ks |

*Hasbro's operating line carries **$1,191.2M of goodwill impairment in FY2023 and $1,021.9M in
FY2025** (`us-gaap:GoodwillImpairmentLoss`). Added back, its three-year operating margin is **+9.94%**.
Both figures are shown because **[E5-33]** keeps such charges in the owner's mean - *"to tell owners
year after year, 'Don't count this' … is misleading"* - and because the row's conclusion is the same
either way.*

**Read the row.** It splits cleanly into two businesses that happen to sell the same object:

- **The two that own their characters** - Mattel (Barbie, Hot Wheels, Fisher-Price) and Hasbro
  (Transformers, Monopoly, Play-Doh) - pay **4.7% and 7.8%** of sales in royalty.
- **The two that rent them** - JAKKS and Funko - pay **16.1% and 16.6%**, between **2.1x and 3.4x**
  as much.
- **And the renters cannot cover it.** JAKKS' operating margin over the window is 5.73% and fell to
  **2.49%** in FY2025; Funko's is negative in two of three years. Mattel, paying a third of the
  rent, earns **11.15%**.

**Peers named: 4 of the industry's real competitors, and I took 3 outside the subject.** Buffett
says eight. The named competitors I could **not** put in the row, and why:

- **Rubies II** - the registrant's named costume competitor - **private**, no filings.
- **MGA Entertainment, Basic Fun, Moose Toys, LEGO** - **private.**
- **Spin Master** - Canadian, TSX-listed, **no SEC filing**; the SEDAR+ rung of the evidence ladder
  was not attempted this cycle.
- **Bandai Namco, Tomy** - Japan; a JPY-reporting comparison would need a different rung again.

**Does that make the moat class PROVISIONAL and the gate UNRESEARCHED?** **No, and the reason is
directional, not convenient.** The framework's PROVISIONAL rule exists so an unsupported *moat
claim* cannot stand on a half-built row. **No moat is being claimed here.** Every missing name is a
**further competitor** in a market whose own participant writes *"the toy industry has no
significant barriers to entry"* and *"numerous smaller domestic and foreign toy manufacturers,
importers and marketers in each of our product categories"*. Adding rivals to a row cannot convert
a NONE into a franchise. I can name the documents that would complete the row - Spin Master's SEDAR+
annual filing, Bandai Namco's TDnet - and getting them would change the count and not the finding.
**Class: NONE, not PROVISIONAL.**

**And state the row's limit [E3-61].** *"In some businesses, the participants behave like a demented
Kellogg… I think you'd have to know the people involved."* The row shows position; it cannot show
conduct. What it does show is that **all four** toy companies' revenues fell over the same three
years (-1.6% to -31.3%), so the industry's conduct toward itself is not the variable that separates
them. The variable that separates them is who owns the character.

---

### The other Q2 tests, each answered from filed figures

**[E3-46] - the second question about the business is a number:** *"the best businesses, by
definition, are going to be businesses that earn very high returns on capital employed over time."*
Pre-tax income ÷ average stockholders' equity, from the filed statements:

| FY | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| pre-tax return on average equity | 49.5% | 26.8% | 18.5% | **6.0%** |
| operating margin | 7.66% | 8.31% | 5.74% | **2.49%** |

**Three consecutive years of decline, and the 2022 figure is arithmetic on an equity base that had
been nearly wiped out** ($2.9M at 2019-12-31, $11.7M at 2020-12-31). The denominator recovering is
what produced the fall, which means the high early readings were not a return on capital employed;
they were a return on capital that was not there.

**[E4-32] - direction outranks existence.** The moat metric is going the wrong way: royalty expense
rose from 15.45% of sales (FY2024) to 16.19% (FY2025) **while sales fell 17.4%**, and the FY2025
MD&A names why - *"higher royalty expense due to **higher royalty guarantee shortfalls**"*. **JAKKS
paid royalty on sales it did not make.** A moat whose rent rises as its volume falls is not
widening.

**[E2-44] - the two-characteristic test. Both answered NO.**
1. *Can it raise prices even when demand is flat and capacity is not fully utilised?* **No, and the
   filing shows the opposite.** FY2025 Costumes: *"The decrease was primarily driven by **US
   customers lowering their order levels based on tariffs.**"* A cost shock arrived and the buyer
   simply ordered less. In the Q2 2026 release the pricing decision is openly described as somebody
   else's: *"Many retailers in the US are **recalibrating their pricing** and where they have done
   so, we see consumers responding positively."*
2. *Can it grow dollar volume with only minor additional investment of capital?* **No.** Net sales
   ran $796.2M → $711.6M → $691.0M → $570.7M, **-28.3% in three years**, while capex ran $10.4M,
   $8.9M, $11.2M, $9.6M and royalty **advances and guarantees** kept accruing. The 10-K states the
   capital mechanic explicitly: *"as we add licenses, the need to fund additional capital
   expenditures, royalty advances and guaranteed minimum royalty payments may strain our cash
   resources. Often, licensors require cash advance payments upon signing agreements… **which
   requires us to pay out cash several quarters prior to our ability to ship, invoice and ultimately
   collect revenue.**"* **Growth here is bought forward in cash, from the licensor, before a unit
   ships.**

**[E4-37] - the inverse metric, agony pricing.** *"It's not a great business when you have to have a
prayer session before you raise your prices a penny."* JAKKS does not get to hold the prayer
session: the retailer recalibrates the price, the customer cuts the order, and the royalty percentage
goes up anyway.

**[E3-33] and [E5-28] - untapped pricing power? No.** Claiming that class is claiming *"a monopoly
or a near monopoly"* **[E5-28]**. JAKKS is a sub-scale third player against two dominant firms with
52.7% of its revenue going to two retail buyers. The competitor row does not support it and nothing
in the filings does.

**[E4-55] - where units exist, monitor units.** JAKKS does not disclose unit volumes. The nearest
physical series the filings give is the licensor-side obligation, and it is the reverse of a
franchise metric: **future aggregate minimum royalty guarantees of $189.8 million at 2025-12-31,
of which $57.4 million is due within twelve months** - against FY2025 net sales of $570.7M and
FY2025 owner earnings of **-$12.0M**. The same disclosure at 2021-12-31 was $71.9M total / $31.0M
current. **The fixed rent obligation has grown 2.6x in four years while revenue fell.**

**[E2-45] - the attacker's test.** *"How I would like, assuming I had ample capital and skilled
personnel, to compete with it."* I would like it very much, and the 10-K tells me exactly how: bid
against JAKKS for the next Disney or Nintendo term. There is no factory to replicate, no
distribution network I cannot hire, no patent of consequence, no switching cost at either end, and
the registrant says *"the toy industry has no significant barriers to entry."* The only thing I
would have to beat is a royalty rate, and Mattel and Hasbro have *"greater financial resources"* to
beat it with. **A moat I could cross with a chequebook is not a moat.**

- **Untapped pricing power [E3-33]:** none found; see above.
- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: narrowing** - royalty ratio up,
  operating margin down three years running, pre-tax return on equity down from 49.5% to 6.0%,
  minimum guarantees up 2.6x in four years.

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**The ledger id that closes the file: [E3-03], criterion 2** - quoted here from the ledger row
itself rather than from the framework's rendering of it, because the row carries a second sentence
the rendering drops and that sentence is the arithmetic test:

> *"An economic franchise arises from a product or service that: (1) is needed or desired; (2) is
> thought by its customers to have **no close substitute** and; (3) is not subject to price
> regulation. **The existence of all three conditions will be demonstrated by a company's ability
> to regularly price its product or service aggressively and thereby to earn high rates of return
> on capital.** Moreover, franchises can tolerate mis-management."* - **[E3-03]**, 1991 letter

**JAKKS fails the demonstration as well as the definition.** It cannot price aggressively - the
retailer recalibrates the price and the customer cuts the order - and it does not earn high rates
of return on capital: operating margin 2.49% and pre-tax return on average equity 6.0% in FY2025,
both falling for three consecutive years.

**And the definition itself.** JAKKS' customers - Target and Walmart - can and do buy
substitutes from Mattel, Hasbro, Rubies II and *"numerous smaller domestic and foreign"* rivals, in
an industry the registrant itself describes as having *"no significant barriers to entry"*, on
licences the registrant itself says its competitors *"have obtained and are likely to continue to
obtain"* overlapping. **[E4-04]** scores the same way independently: the advantage must be **bought
again** every licence term rather than defended, which is the class the durability criterion
excludes, and the FY2025 MD&A attributes its own year to *"limited theatrical releases"* - **[E3-51]**'s
surfer, not the wave.

**Asked aloud, as the framework requires on every non-IN verdict: "Can I name the document that
would resolve this?"** The question does not arise. **This is OUT, not UNRESEARCHED and not
UNKNOWABLE** - the evidence is in hand, it is the registrant's own, and it says the business fails
criterion 2. No further document changes it; a further document would have to contradict the 10-K.

⛔ **THE HARD SEQUENCE CLOSES THE FILE HERE. Q3, Q4, Q5 and Q6 are not answered, and no valuation
is reported.** *(Operator rule 2: no Q5 output may be reported unless Q1-Q4 each show IN.)*

## NOTES BENEATH THE CLOSE - NOT VERDICTS, NOT A CLEARANCE

*The file closed at Q2. Everything below was read because the dispatch brief ordered it read
before any scoring, and because the CGNX prohibition forbids deciding in advance which gate is
boring. **None of it is scored, none of it is a verdict, and none of it could reopen the file** -
a Q3 finding can never promote a name **[E2-37, E2-38, E3-39]**, and Q4 and Q5 are shut by operator
rule 2. It is recorded so the next reader inherits the reading rather than repeating it.*

### WHAT WOULD HAVE BEEN Q3 - recorded, not scored

**The weight case, which is the part a run must declare before anything else counts.** Daily
execution: **yes** - this is an undifferentiated product whose licences must be re-won and whose
hits must be re-picked every season; [E3-43]'s *"a business, unlike a franchise, can be killed by
poor management"* is the live branch. Control: no. Leverage: no - the revolver was undrawn at
2025-12-31 and interest expense was $0.5M. **One of three ticked, so had Q3 been reached it would
have been a BINARY GATE and no price would compensate.** Recorded, not applied.

**The 8-K earnings release was read, as the brief required, before any flag was scored.** Filed
2026-07-24, accession **0001185185-26-003108**, and note the filing quirk: **JAKKS furnishes its
earnings release as Exhibit 10.1, not EX-99.1** - a run that searched for EX-99.1 would have found
nothing and concluded there was no release. *(Recorded as a retrieval hazard for the queue.)*

- **[E4-29], the fifth flag, fires.** Two of the release's seven headline bullets are
  *"**Adjusted EBITDA** (a non-GAAP measure) of $5.4 million"* and *"**Trailing-twelve-month
  Adjusted EBITDA of $37.8 million**, up from $34.6 million as of Q1 2026."* The company's own
  definition adds back *"depreciation, amortization and … reorganization expenses and **restricted
  stock compensation expense**"* - so the promoted metric deletes both the reverse float
  **[E5-41]** and the stock pay **[E5-06]** calls *"even more cavalier"* to exclude. Against
  $10.9M of FY2025 share-based compensation on $570.7M of sales, that add-back is not small.
  *Mitigating, and recorded in the same breath: the release **leads** with GAAP - net sales, gross
  margin, gross profit, operating loss and GAAP net income all precede the adjusted figures, and
  the GAAP operating loss of $0.1 million is stated plainly.*
- **And the pay follows the metric, which is where [E4-29] meets [E2-49].** The DEF 14A filed
  2026-04-22 (accession 0001185185-26-001465): *"Historically, factors given considerable weight in
  establishing bonus performance criteria are Net Sales, Adjusted EPS … and **Adjusted EBITDA
  applied on a basis consistent with past periods, as adjusted in the sole discretion of the
  Compensation Committee** to take account of extraordinary or special items. However, **since at
  least 2019, bonus performance has been based exclusively upon Adjusted EBITDA.**"* A single
  discretionary non-GAAP metric, sole-discretion adjustable, is the entire cash-bonus bullseye -
  the opposite of [E2-49]'s *"pre-set, long-lived and small bullseyes."*
- **[E3-50], stock-price targeting, fires from the same page.** *"In 2025 an additional performance
  bonus was established **based solely upon the market performance of our common stock.**"*
- **[E4-22] third flag - trumpeted projections: NOT found.** No earnings guidance, no growth
  target, no multi-year EPS goal appears in the release or the 10-K. The release's forward language
  is qualitative (*"setting us up well for the quarters ahead"*). **[E5-30]**'s ratchet has not
  been started.
- **[E5-15], serial share issuance: NOT the promotional case, but real dilution.** The share count
  ran **9,723,534 (Nov 2022) → 11,445,012 (Jul 2026), +17.7% in under four years**, of which
  571,295 was the preferred redemption and the remainder equity compensation. No shares were sold
  to the market: the $75M ATM has **never been drawn**, the 2022 $150M shelf **expired unused in
  2025**. So [E5-15]'s *"surest indicator of a promotion-minded management"* does not fire; the
  dilution is a cost, not a tell.
- **[E2-52], dividends funded by issuance: does NOT fire.** Dividends began in 2025 ($11.2M) and no
  capital was raised to replace them. But the timing is on the record: the payout began in the year
  owner earnings turned negative.
- **A disclosure correction, judged by direction [E2-69].** The 2026 proxy discloses that the
  Company *"identified an error in the previously reported Compensation Actually Paid amounts for
  fiscal 2024 and fiscal 2023"*, states the cause (fiscal-year-end rather than vesting-date stock
  price), quantifies it at each line ($605,024 up for FY2024, $1,409,944 down for FY2023 for the
  PEO), revises the table, and says it did not affect the financial statements. **That is a
  deviation toward candor, not the weak-accounting flag** - it is the [E2-26] half-owner test
  passed, one-time item quantified separately at every line.
- **[E2-01], the primary test, as a series:** pre-tax return on average equity 49.5% / 26.8% /
  18.5% / 6.0% across FY2022-25. It is at Q2 above because it is a fact about the business first.

### WHAT WOULD HAVE BEEN Q4 - the [E4-25] rebuild already stands at Step 0

The owner-earnings rebuild the screen's `spread_caveat` ordered is complete and sits under FLAG 4
at Step 0, headed **COMPUTATION - NOT A CLEARANCE**. The three facts a later reader needs, none of
them scored:

1. **Seventeen filed years, mean owner earnings $13.11M (capex end) / $6.98M (D&A end); eight of
   the seventeen negative; FY2025 itself -$12.0M.** The screen's $19-22M band is the highest and
   narrowest construction obtainable and rests on FY2022+FY2023.
2. **[E5-11] strength (3), the one that usually kills, is where this name's arithmetic is
   interesting** and it is a *licence* obligation, not debt: **minimum royalty guarantees of $189.8
   million at 2025-12-31, $57.4 million due within twelve months**, up from $71.9M / $31.0M at
   2021-12-31. Against $52.2M of cash at 2025-12-31 and FY2025 operating cash of $8.5M. These are
   fixed, and the 10-K says they are: *"Contractual minimal royalty payments are almost always
   fixed and determined upon signing, so these sorts of shocks could have a negative impact on our
   business … for multiple years."* Balance-sheet debt, by contrast, is essentially gone.
3. **[E4-41], normalize down for luck.** The newest periodic figures carry **$11.1 million of IEEPA
   tariff refunds** in non-operating income, which the earnings release itself names as the driver
   of the quarter's swing to profit. Any trailing-twelve-month figure built through Q2 2026 without
   removing it is overstated.

**Great, good or gruesome is not scored** and would have needed Q1-Q3 IN to be scored at all.

---

## **[E4-51]** - THE STRONGEST SINGLE FACT AGAINST MY OWN VERDICT

*"I'm not entitled to have an opinion unless I can state the arguments against my position better
than the people who are in opposition."*

**The fact: JAKKS' gross margin ROSE while its revenue fell 28%.** Gross margin ran **26.5%
(FY2022) → 31.4% (FY2023) → 30.8% (FY2024) → 32.4% (FY2025)** on the filed statements, a
five-point improvement through a collapse in volume. That is, on its face, exactly what a franchise
looks like under stress and exactly what I said was absent: **the business held price while losing
units.** The supporting case is real too - the company describes its portfolio as *"evergreen
brands"*, Disguise is a wholly-owned costume brand rather than a rented one, the balance sheet was
rebuilt from **$2.9 million of equity at 2019-12-31 to $249.1 million at 2025-12-31** with the
$125.8M Recap term loan, the $69.2M BSP term loan and the Series A preferred all retired, and
**Q2 2026 net sales were up 17%** with Action Play & Collectibles up over 40%. A reader could
fairly say I have written up a turnaround as a decline.

**Why it does not move the verdict, in three steps.**

1. **The filing says the gross margin did not come from price.** The FY2025 MD&A attributes it
   line by line: Toys/Consumer Products' cost-of-sales percentage fell *"due to **lower inventory
   obsolescence costs**"* - and adds, in the same sentence, *"**Although royalty rates were higher
   year-over-year**."* Costumes' gross margin went the **other** way (cost of sales 73.1% → 74.8%),
   *"attributable higher royalty expense due to **higher royalty guarantee shortfalls**"*. Writing
   off less stale inventory is not pricing power; it is a smaller order book.
2. **Where the rent actually lands, the margin collapsed.** Operating margin over the identical
   window: **7.66% → 8.31% → 5.74% → 2.49%.** Pre-tax return on average equity: **49.5% → 26.8% →
   18.5% → 6.0%.** A gross margin that rises while the operating margin falls by two-thirds is the
   signature of a company carrying the same fixed licence and overhead burden on a smaller base -
   which is precisely what the $189.8M of minimum guarantees, up 2.6x in four years against falling
   sales, describe.
3. **Gross margin is the wrong instrument for the question anyway.** [E3-03] criterion 2 asks
   whether the **customer** thinks there is no close substitute. Target and Walmart do not consult
   JAKKS' gross margin; they consult Mattel's catalogue, Hasbro's catalogue, Rubies II's catalogue
   and *"numerous smaller domestic and foreign"* catalogues, in an industry the registrant itself
   says has *"no significant barriers to entry"*. **No margin series can answer a question about
   substitutes at the buyer.**

**And the balance-sheet half of the counter-argument is conceded outright.** The deleveraging is
genuine and creditable. It is also, exactly, **[E2-38]**: *"Good jockeys will do well on good
horses, but not on broken-down nags."* A management that repaired a capital structure has not
acquired a moat, and under the guardrail a strong Q3 *cannot promote a name, repair Q2, or
substitute for Q4* - which is why this run did not score Q3 at all.

*Operator rule 9 applies to me: the disconfirming evidence above was hunted for my own verdict, and
the run states that the verdict survived it rather than that no such evidence exists.*

---

## Q3 · Q4 · Q5 · Q6 - NOT ANSWERED

**Operator rule 2: no Q5 output may be reported unless Q1-Q4 each show IN.** Q2 is OUT. No
valuation, no yield, no floor comparison and no ranking appears anywhere in this file. The
arithmetic under Step 0 FLAG 4 is headed **COMPUTATION - NOT A CLEARANCE** and carries no entry
language.

- Q3 **NOT ANSWERED** *(material recorded above, not scored)*
- Q4 **NOT ANSWERED** *(rebuild recorded at Step 0, not scored)*
- Q5 **NOT ANSWERED**
- Q6 **NOT ANSWERED**

---

## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 OUT, stop.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests on
      the filed income statement and Item 1 of the FY2025 10-K.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives - **none used.**
- [x] Every UNKNOWABLE verdict states what specifically cannot be known - **none used.**
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked. FY2025 10-K
      acc. 0001185185-26-000723; royalty expense 16.19% computed against the MD&A's stated 16.2%,
      plus three cash-flow lines tied to the dollar.
- [x] Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.
      **Seven windows computed and published [E4-38], under a COMPUTATION - NOT A CLEARANCE
      heading, because Q4 did not open.** No net-income proxy was used anywhere - PRIME RULE 3.
- [x] Competitor row filled - four registrants, one metric, one window, each from its own 10-K.
      Class NONE with the reason the missing private peers cannot change it, stated in the open.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated: USD 5.34%,
      2026-09-18, US Treasury daily par yield curve. Struck this session, not inherited.
- [x] Value stated as a round-number range, not a point estimate - **n/a, no value stated.**
- [x] One bar chosen, not both; windage count stated - **n/a, no bar used, no windage spent.**
- [x] Prices dated; aggregator used for live quotes only and flagged. $24.085 at 2026-09-21
      13:44:46 UTC, Yahoo, flagged as an aggregator, raw metadata saved, seven prior closes shown.
- [x] Run committed to git, with a pathspec, after each question.

## REGISTER
- Verdict: [ ] IN  [x] **OUT (about the business)**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
- **One line:** JAKKS rents substantially all of its revenue from other people's characters at
  16.05% of net sales - triple Mattel's 4.69% and double Hasbro's 7.81% over the same three years -
  sells it to two retailers who are 52.7% of the top line, and keeps 2.49% operating margin;
  **[E3-03]** criterion 2 fails on the registrant's own words.
- **If UNRESEARCHED - THE WORK ORDER:** n/a.
- **If UNKNOWABLE:** n/a.

### THE REVERSAL CONDITION, IN WORDS - the QLYS ruling
**No band is armed in `tools/alerts.json` and no `PORTFOLIO.md` row is added.** This name failed at
Q2, on the **business**, and a price alert on a business finding is a category error. The condition
that would reopen the file, stated so a future reader does not have to guess:

> **JAKKS becomes re-runnable only if the royalty ratio falls decisively and durably** - if
> wholly-owned brands (Disguise and the proprietary lines) grow to carry the majority of net sales
> and royalty expense falls toward the IP-owners' 5-8% of sales rather than the renters' 16-17% -
> **or if the minimum-guarantee obligation ($189.8M at 2025-12-31, $57.4M current) shrinks against
> a rising sales base.** A good quarter does not do it; a change of customer concentration does not
> do it; a share price does not do it. **The test is who owns the property that produces the
> revenue**, and today the registrant says it is not JAKKS.

---

*Run executed 2026-09-21 as an unattended overnight cycle. Wave 7, name 22 of 218. All primary
documents are in `Test Runs/_research 2026-09-21 JAKK/`.*
