# Company Run - Group 1 Automotive, Inc. (GPI) - 2026-09-25
**CIK 0001031203. NYSE. December fiscal year end. WAVE 7, name 28 of 218 by the order file
(`Screens/_daily/_wave7_order.txt` line 28; `_wave7_done.txt` held 27 lines, the last PII, when this
run started). Name claimed at dispatch, commit `effc95b`. Every figure below was fetched and struck on
2026-09-25 unless its line says otherwise. The July 5-pack
(`Test Runs/2026-07-16 Run - Auto Dealers 5-pack (ABG LAD AN GPI PAG).md`) was used for nothing: it
priced GPI on a net-income proxy, which operator rule 5 forbids and the 2026-09-20 addendum condemns.**
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.47** % · date **09/24/2026** (the newest row the curve carried at the time of the
  run) · source (issuing authority) **US Treasury daily par yield curve, 30 Yr,
  `home.treasury.gov` daily-treasury-rates.csv for 2026**, struck fresh by this run and saved raw
  as `Test Runs/_research 2026-09-25 GPI/treasury_2026.csv`. **FRED DGS30 was not used.** The
  neighbouring rows read 5.40 (09/23) and 5.29 (09/22). Nothing was inherited from the brief or
  from the PII run, which happened to strike the same row.
- FX if the quote and the earnings differ in currency: **not required; the earnings currency is
  the dollar, established from the segment note, not assumed.** Note 20 of the FY2025 10-K gives two
  reportable segments. **Pre-tax income: U.S. $732.1M / $652.2M / $563.1M for 2023 / 2024 / 2025;
  U.K. $68.1M / $6.3M / $(113.2)M.** The U.K. is 26% of 2025 revenue ($5,944.6M of $22,571.4M) and
  **none of 2025's pre-tax income** (the U.S. earned 125% of the consolidated $449.9M). On the
  2023-25 sum the U.S. is 102% of pre-tax income ($1,947.4M of $1,908.6M; the U.K. summed to $(38.8)M). The
  sterling business is carried in Q4 as a risk to the dollar earnings, not as a second earnings currency. USD sovereign.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K FY2025, filed 2026-02-13, period 2025-12-31, accession `0001031203-26-000064`**
    (primary document `gpi-20251231.htm`): Item 1 (Business, Competition, franchise agreements),
    Item 1A, Item 7 including Liquidity and the non-GAAP cash-flow reconciliation, the four
    primary statements, and Notes 1, 3 (acquisitions, Inchcape), 4 (restructuring), 13
    (floorplan), 14 (debt), 20 (segments).
  - **10-Q for the quarter ended 2026-06-30, filed 2026-07-30, accession
    `0001031203-26-000123`** (cover, statements, MD&A).
  - **10-Ks FY2023 (`0001031203-24-000013`), FY2021 (`0001031203-22-000007`), FY2019
    (`0001031203-20-000006`), FY2016 (`0001031203-17-000007`)** for the long series.
  - **8-Ks read (the perimeter)**: 2026-07-30 (`0001031203-26-000121`, Items 1.01/2.02/7.01: the
    Hennessy purchase agreement, the Q2 2026 release EX-99.1 and the deal release EX-99.2);
    2026-08-11 (`0001031203-26-000126`, a director and the dividend); 2026-09-08
    (`0001193125-26-384390`, Items 2.02/8.01, with the **offering-memorandum excerpts EX-99.2**);
    2026-09-10 (`0001193125-26-386882`, the notes purchase agreement); 2026-09-22
    (`0001193125-26-397968`, the notes closing); 2026-09-22 (`0001031203-26-000137`, the Conifer
    stockholder agreement); 2026-09-24 (`0001193125-26-400088`, a real-estate credit agreement
    of Group 1 Realty with Bank of America). **DEF 14A filed 2026-04-02, accession
    `0001031203-26-000100`.**
- figure cross-checked against the filed statement (say which): **two, by re-derivation from
  the filed lines.**
  1. FY2025 **net cash provided by operating activities $694.5M** (Consolidated Statements of
     Cash Flows, F-8), rebuilt from its own lines: 325.2 + 121.1 + 30.6 + 24.8 + 199.6 + 29.0 +
     5.4 - 18.7 + 1.3 - 0.4 = **717.9 of earnings-side cash**, plus working capital (27.2) +
     (2.2) + (47.7) + 39.0 + (4.4) + 49.6 + (1.1) + (29.3) = **(23.3)** = **694.6**. It ties to
     $0.1M of rounding.
  2. **Total stockholders' equity $2,789.1M** at 2025-12-31, rebuilt from the equity statement's
     closing row: 0.2 + 388.5 + 4,421.9 + 31.6 - 2,053.2 = **2,789.0**. Ties to rounding.
- *If the filing could not be obtained → **UNRESEARCHED**.* **Not invoked; every rung used was
  SEC EDGAR primary documents.**

**THE PERIMETER, checked before anything else. A deal is live, and it is a purchase, not a sale
of the company.** On **2026-07-30** GPI signed a Purchase and Sale Agreement to buy *"substantially
all of the assets"* of **Hennessy Automobile Companies** (8-K Item 1.01, `0001031203-26-000121`):
*"the operation of ten automobile dealerships and one collision center located in the greater
Atlanta, Georgia market"*, for *"an aggregate purchase price of approximately $1.3 billion, plus an
additional amount for the remaining inventory assets"*, closing *"no later than the 160th day after
the date of the Purchase Agreement"* (extendable to the 190th), subject to manufacturer consents and
HSR. It is funded by **$1.25bn of senior notes closed 2026-09-22: $625.0M of 6.250% notes due 2032
and $625.0M of 6.625% notes due 2035** (`0001193125-26-397968`), the 2032 notes carrying a special
mandatory redemption if the deal is not done by 2027-01-06. **The offering-memorandum excerpts
(`0001193125-26-384390` EX-99.2) give Hennessy's revenue as $1,726.2M and "Adjusted EBITDA (as
defined by Hennessy's management)" as $124.0M for the twelve months to 2026-03-31**, with the
warning that the Hennessy figures were *"provided to us by Hennessy and has not been independently
verified or audited"*, and a **pro forma net leverage ratio of 4.2x**. **No sale of GPI is live:
the quote is an owner-earnings price, not a spread.** The Conifer stockholder agreement of
2026-09-21 (a board seat from 2026-11-01, a 19% standstill, voting with the board) is read at Q3.
The 2026-09-24 8-K is a mortgage facility for the real-estate subsidiary.

**THE PRICE AND THE CAP** *(struck by this run; the screen's cap was flagged, and the flag is
resolved)*
- **Share count, quoted verbatim from the cover of the 10-Q filed 2026-07-30, accession
  `0001031203-26-000123`:** *"As of July 24, 2026, the registrant had 11,922,225 shares of common
  stock outstanding."* (The 10-K cover: *"As of February 6, 2026, there were 11,925,199 shares of our
  common stock, par value $0.01 per share, outstanding."*)
- **One equity class.** The balance sheet: *"Preferred stock, $ 0.01 par value, 1,000,000 shares
  authorized; no ne issued or outstanding"* (the split "no ne" is the filing's own text artifact,
  kept); common 24,941,249 issued less 12,897,840 in treasury = 12,043,409 outstanding at
  2025-12-31, consistent with the cover counts after 2026 buybacks.
- **Price $247.79** (close 2026-09-24, **aggregator quote, flagged**: Yahoo Finance chart endpoint,
  `regularMarketTime` 2026-09-24 20:00 UTC; raw response saved as `price_raw.json`, with
  `price_hist_raw.json` and `price_2026_raw.json` for the dated closes below).
- **cap = close x shares**, split-invariant, `close` never `adjclose`: $247.79 x 11,922,225 =
  **$2,954 million.**
- **The screen flag, resolved.** The row read *"CAP BELOW FILED PUBLIC FLOAT - cap $3,193M against a
  filed float of $5,500M (1.72x) as of 2025-06-30."* Neither figure is wrong; **the price fell.** The
  10-K cover prices the float at the 2025-06-30 close, which the same aggregator gives as
  **$436.71**; $5.5bn / $436.71 implies ~12.6M non-affiliate shares, inside the 13,278,785 (2024-12-31) to 12,043,409 (2025-12-31) outstanding range the balance sheets give. Since then: $393.30
  (2025-12-31), $357.97 (2026-07-29), **$296.71 on 2026-07-30, the day the Q2 results and the
  Hennessy deal were announced, down 17% in a session**, $281.60 (2026-09-08), $247.79 now. **The
  quote is 43% below the float date and 31% below the eve of the Hennessy announcement.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words, no management language:** Group 1 owns about 250 car
  dealerships in the U.S. and the U.K. (the September 2026 releases: *"249 automotive dealerships,
  310 franchises, and 32 collision centers"*, 37 brands). Each dealership holds a manufacturer's
  franchise, buys that manufacturer's new cars at the manufacturer's price, borrows the purchase
  price from a floor-plan lender until the car is sold, and sells it at a few points of margin;
  it takes the trade-in and resells it, arranges the buyer's loan and sells service contracts for
  a commission, and then repairs the cars it and its neighbours sold, including warranty work the
  manufacturer pays for. **The revenue is mostly cars and the profit is mostly not.** FY2025 from
  the income statement (10-K `0001031203-26-000064`, F-5), gross profit by line: new vehicles
  $755.4M on $10,989.9M of sales (**6.9%**), used retail $347.2M on $7,195.0M (**4.8%**), used
  wholesale $(0.9)M, **parts and service $1,585.6M on $2,844.6M (55.7%)**, and finance and insurance
  commissions **$934.6M**, which are booked net and are all gross profit. **Parts and service is 13%
  of revenue and 44% of gross profit; F&I is 4% of revenue and 26% of gross profit; new cars are
  49% of revenue and 21% of gross profit.** Selling, general and administrative expense takes
  $2,545.5M, **70 cents of every gross-profit dollar**; depreciation $121.1M; floor-plan interest
  $101.5M and other interest $182.9M. Income from operations was $734.0M, **3.3 cents on the sales
  dollar** ($955.2M, 4.2 cents, before $192.8M of impairments and $28.4M of U.K. restructuring).
  Cash follows inventory: $2,741.3M of cars and parts at year end, financed by $1,915.8M of
  floor-plan notes, so the dealer's own capital in inventory is small and its cost is an
  interest line that moves with short rates.
- **The scarce input this business controls:** **the manufacturer's franchise, protected by state
  law.** Item 1: U.S. franchise agreements mostly *"continue indefinitely"*, and *"the U.S.
  jurisdictions in which we operate have automotive dealership franchise laws, which generally
  provide that it is unlawful for a manufacturer or distributor to terminate or not renew a
  franchise unless “good cause” exists. As a result, it generally is difficult, outside of
  bankruptcy, for a manufacturer or distributor to terminate, or not renew, a franchise under these
  laws, which were designed to protect dealers."* Warranty repair and recall work can only be done
  by a franchised dealer of that brand. **It is not an exclusive input**, and the registrant says
  so in the same Item (quoted at Q2): no cost advantage in buying cars, no exclusive territory. The
  U.K. has *"generally ... not"* such laws, and U.K. terms are *"two-year rolling"*.
- **Will the fundamentals look broadly the same in ten years?** **Yes, in the U.S.; less certainly
  in the U.K.** People will still buy cars on credit, trade them in, and have them serviced under
  warranty by a franchised dealer; the U.S. dealer franchise laws are the reason the direct-to-
  consumer and agency models have not reached U.S. new-car retailing. The moving parts are named in
  the filing and all of them are understandable: the **agency model** already adopted by some
  manufacturers in the U.K. (the dealer earns a fee and no longer owns the car), **direct-to-consumer
  EV makers**, **Chinese brands** (*"growing from approximately 8% in 2024 to approximately 13% in
  2025"* of U.K. new-car sales, Item 1A), and manufacturers cutting *"dealership financial
  assistance"* (Toyota named). None of these is a comprehension problem; they are Q2 and Q4
  questions.
- **VERDICT: [x] IN**
  *A franchised car retailer: thin-margin vehicle sales that feed a high-margin repair and
  finance-commission business. Every figure above is off the filed FY2025 statements and Item 1;
  nothing rests on "unverified", "general knowledge" or "provisional". The business can be stated in
  five sentences and has been the same business, on the same lines of the income statement, since
  the FY2016 10-K.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**
- Needed or desired **[x]** · no close substitute **[ ] FAILS** · not price-regulated **[x]**
  (retail vehicle, repair and F&I prices are not regulated; the protection the business does
  have is regulation of **entry**, not of price, and is taken below under [E2-59])

**Clause (2) fails on the registrant's own words.** Item 1, Competition, FY2025 10-K
(`0001031203-26-000064`):

> *"The automotive retail industry is highly competitive across all our service lines. Consumers
> have a number of choices when deciding where and how to (i) purchase and/or lease a new or used
> vehicle [...] We believe the principal competitive factors in the automotive retailing industry
> are location, service, **price**, selection, online capabilities, established customer
> relationships and reputation."*

> *"Our principal new vehicle dealer competitors also have franchise agreements with the various
> vehicle manufacturers and, as such, **generally have access to new vehicles on the same terms as
> we do. We do not have any cost advantage in purchasing new vehicles from vehicle manufacturers,
> and our current franchise agreements do not grant us the exclusive right to sell a
> manufacturer’s product within a given geographic area.**"*

Item 1A adds: *"Customers are using the internet to compare prices for new and used vehicles,
automotive repair and maintenance services, finance and insurance products"*, and that a
manufacturer *"may grant another dealer a franchise to start a new dealership near one of our
locations"*. For the high-margin line, Item 1: *"our dealerships compete with other franchised
dealers to perform warranty maintenance and repairs [...] A number of regional or national chains
offer selected parts and services at prices that may be lower than ours."* **The customer can buy
the identical car, made by the same manufacturer at the same wholesale price, from the next
franchised dealer of the same brand, and compare the two prices on a phone. That product has a
close substitute by construction. [E3-03] criterion (2) is not met.** The used-car, F&I and
customer-pay repair lines have more substitutes, not fewer (the filing names large used-car
chains, banks and independent shops).

- **Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04]** The
  business is not in the rapid-change class, so [E4-04]'s perimeter close (UNKNOWABLE) is **refused
  in writing**: the franchise question is answerable from these filings and the answer is
  negative. What applies instead is Buffett's own classification of this trade, **[E3-74]**:
  *"retailing is a good case of a business where you have to stay smart. [...] you are under
  attack all of the time."* And the 1991 distinction **[E3-43]**: *"“a business” earns exceptional
  profits only if it is the low-cost operator or if supply of its product or service is tight.
  **Tightness in supply usually does not last long.**"* The registrant disclaims the first route
  in terms (*"We do not have any cost advantage"*); the record below shows the second.
- **Primary moat metric, filing-sourced, and its trend: margins, twelve years, from GPI's own five
  10-Ks** (FY2016 `0001031203-17-000007` for 2014-16; FY2019 `0001031203-20-000006` for 2017-18,
  which still include Brazil, ~4% of revenue; FY2021 `0001031203-22-000007` for 2019-20 on the
  continuing basis; FY2023 `0001031203-24-000013` for 2021-22; FY2025 for 2023-25). Operating
  margin "ex" adds back the impairment, restructuring and other-operating-income lines printed on
  the face of the income statement.

  | | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|
  | revenue $M | 9,937.9 | 10,632.5 | 10,887.6 | 11,123.7 | 11,601.4 | 11,597.9 | 10,600.2 | 13,481.9 | 16,222.1 | 17,873.7 | 19,934.3 | 22,571.4 |
  | gross margin | 14.6% | 14.4% | 14.7% | 14.8% | 14.9% | 15.2% | 16.4% | 18.1% | **18.3%** | 16.9% | 16.3% | 16.0% |
  | **new-vehicle gross margin** | 5.4% | 5.1% | 5.2% | 5.2% | 5.0% | **4.7%** | 5.9% | 9.4% | **11.1%** | 8.7% | 7.2% | 6.9% |
  | operating margin, as filed | 3.04% | 2.62% | 3.12% | 3.07% | 2.94% | 3.09% | 4.68% | 6.56% | **6.73%** | 5.42% | 4.56% | 3.25% |
  | operating margin, ex | 3.46% | 3.44% | 3.43% | 3.25% | 3.32% | 3.28% | 4.93% | 6.57% | **6.74%** | 5.60% | 4.76% | 4.23% |
  | parts & service GM | 52.8% | 54.1% | 53.9% | 53.8% | 53.6% | 54.3% | 54.3% | 54.6% | 54.9% | 54.6% | 54.9% | 55.7% |

  **The shape is a wave, not a moat.** For six years (2014-19) the business earned **3.3-3.5
  cents** on the sales dollar before impairments, with new cars at about five points of gross
  margin. The 2020-22 vehicle shortage doubled the new-car margin to **11.1%** and the operating
  margin to **6.7%**; as supply returned the new-car margin fell in each of three steps (8.7%,
  7.2%, 6.9%) and the operating margin with it. The 10-K's own words for 2025 (U.S. MD&A): *"Gross
  profit per unit sold continues to moderate towards pre-COVID levels, facing pressure from
  affordability concerns of consumers due to rising costs of vehicles from OEMs and relatively high
  consumer interest rates."* The registrant itself names the base the margin is returning to; the Q2 2026 release (EX-99.1 to
  `0001031203-26-000121`): *"NV GP per retail unit (“PRU”) | $3,254 | (8.5)%"*, total gross profit
  **(8.0)%**, used retail units **(11.2)%**. That is [E3-43]'s *"supply ... tight"* case exactly,
  and [E2-58]'s *"ratio of supply-tight to supply-ample years"*. **The one steady line is parts and
  service, 53-56% for twelve years**, and it is the strongest thing for the business; it is taken
  on at the row and in the paragraph after it.

**THE COMPETITOR ROW — required [E3-28].** A moat is a claim about *relative* position.

| Company | gross margin 2021 / 22 / 23 / 24 / 25 (mean) | operating margin as filed 2021-25 (mean; mean ex-impairment) | parts & service GM mean | source |
|---|---|---|---|---|
| **GPI (subject)** | 18.1 / 18.3 / 16.9 / 16.3 / 16.0 (**17.1%**) | 6.56 / 6.73 / 5.42 / 4.56 / 3.25 (**5.30%**; 5.55%) | **54.9%** | 10-K FY2025 `0001031203-26-000064`, FY2023 `0001031203-24-000013` |
| AutoNation (AN) | 19.16 / 19.51 / 19.04 / 17.88 / 17.91 (18.70%) | 7.36 / 7.50 / 6.13 / 4.88 / 4.49 (6.07%; 6.20%) | 47.05% | 10-K FY2025 `0001628280-26-007800`, FY2023 `0000350698-24-000021` |
| Penske Automotive (PAG) | 17.38 / 17.40 / 16.65 / 16.37 / 16.40 (16.84%) | 5.31 / 5.35 / 4.56 / 4.30 / 4.03 (4.71%; 4.73%) | 58.96% (retail automotive only) | 10-K FY2025 `0001628280-26-012830`, FY2023 `0001019849-24-000033` |
| Lithia Motors (LAD) | 18.65 / 18.28 / 16.84 / 15.37 / 15.23 (16.88%) | 7.28 / 6.89 / 5.45 / 4.33 / 4.24 (5.64%; 5.64%) | 54.89% | 10-K FY2025 `0001023128-26-000015`, FY2023 `0001023128-24-000032` |
| Asbury (ABG) | 19.34 / 20.09 / 18.62 / 17.15 / 17.07 (18.45%) | 8.05 / 8.25 / 6.44 / 4.86 / 4.78 (6.48%; 6.96%) | 57.60% | 10-K FY2025 `0001144980-26-000051`, FY2023 `0001144980-24-000076` |
| Sonic (SAH) | 15.44 / 16.55 / 15.63 / 15.42 / 15.72 (15.75%) | 4.34 / 2.24 / 2.95 / 3.24 / 2.43 (3.04%; 3.84%) | 50.14% | 10-K FY2025 `0001628280-26-010570`, FY2023 `0001043509-24-000022` |

*The peer rows were fetched and computed by a sub-agent of this run from the filed income
statements (not XBRL), every gross profit re-added from revenue less cost of sales for all 25
peer-years; the working file with every year, every line and every accession is
`Test Runs/_research 2026-09-25 GPI/peers/COMPETITOR_ROW.md`. "Ex-impairment" for the peers adds back
only the impairment lines on the face of each income statement; GPI's figure on that same basis is
the 5.55% shown. Comparability limits, stated: PAG restated 2023-25 for Penske Motor Group (bought
from a related party in November 2025) and carries commercial-truck and Australian distribution
businesses; AN and LAD carry captive-finance income inside operating income; SAH carries its
loss-making EchoPark used-car segment; dealership-sale gains sit inside operating income at AN, LAD,
SAH and GPI, below it at PAG and ABG; ABG's 2021 is before its Larry H. Miller purchase.*

- **Peers named: 5 of the industry's 5 other U.S.-listed franchised dealer groups**, which are also
  the five companies GPI's own proxy uses for its relative-TSR comparator (DEF 14A 2026, footnote 3:
  *"Comparator group consists of Lithia Motors, AutoNation, Sonic Automotive, Penske Automotive Group
  and Asbury Automotive Group."*). The rest of the industry is thousands of private dealer groups
  (Hennessy, the seller GPI is buying, is one), which file nothing; they are **not** a missing
  class the row needs, because the four public peers that say it in words say they buy on the same
  terms as everyone: LAD *"We do not have any cost advantage in purchasing new vehicles from
  manufacturers."*; ABG *"We do not have any cost advantage over other retailers in purchasing new
  vehicles from manufacturers."*; SAH *"We do not have any cost advantage in purchasing new vehicles
  from manufacturers due to economies of scale or otherwise."*; AN and PAG, that competitors
  *"generally have access to new vehicles on the same terms"* / *"give them access to new vehicles
  on the same terms as us"*, and that their rights are *"non-exclusive"*. The row is not
  PROVISIONAL.
- **What the row shows.** GPI is **fourth of six on operating margin** (5.30% against a range of
  3.04% to 6.48%), **third of six on gross margin**, and **fourth on parts-and-service margin**
  (54.9% against 47.1% to 59.0%). **All six ran the same wave**: every one peaked in 2021-22 and every
  one sat 2.5 to 3.5 points lower in 2025. GPI's own fall was among the steepest (6.73% to 3.25% as
  filed; 6.74% to 4.23% ex-items; AN 7.50% to 4.49%, ABG 8.25% to 4.78%, LAD 7.28% to 4.24%). **No
  member of the class earns a margin the others cannot; the margins move together because the
  thing that moved them, manufacturer supply, is outside all six.** The row's limit, stated
  **[E3-61]**: it shows position, not conduct, and conduct in local markets is not in any filing.
- **The strongest thing against the verdict, recorded beside it.** (i) **Parts and service**: 44%
  of GPI's gross profit at 53-56% margins for twelve years, with warranty work reserved to
  franchised dealers of the brand, is a real and durable earnings stream. But the row shows every
  franchised group earns the same stream at the same margin (PAG 59%, ABG 58%, LAD 55%), so it is a
  property of **holding a franchise**, not of Group 1. (ii) **Returns on capital are high**
  **[E3-46, E2-43]**: pre-tax income plus non-floor-plan interest on unleveraged net tangible assets
  (equity less goodwill and franchise rights, plus non-floor-plan debt) was **20% in 2019, 42% in
  2021, 50% in 2022, 37% in 2023, 28% in 2024 and 19% in 2025 (25% before the impairments and
  restructuring)**. The mean is lifted by the two wave years, and 2019, the last year before the
  wave, is the honest base. (iii) **The state franchise laws** make a U.S. franchise hard to
  terminate and keep manufacturers from selling direct; that protection is real, but it belongs to
  **the regime, not the company**: it is [E2-59]'s administration *"legally through government
  intervention"*, it protects every franchised dealer equally, and the filing itself shows where it
  is absent: the U.K. has *"generally ... not"* such laws, and there the agency model has arrived and
  the U.K. segment went from $68.1M of pre-tax income (2023) to $(113.2)M (2025). **None of the three
  is a franchise in [E3-03]'s sense: the customer's substitute is the next dealer of the same brand.**
- **The attacker's test [E2-45].** *"how I would like, assuming I had ample capital and skilled
  personnel, to compete with it."* The answer is written in GPI's own cash-flow statements: with
  capital, one simply **buys dealerships**, which GPI itself did for **$4,813M over 2014-25** and is
  doing again for ~$1.3bn (Hennessy). Item 1A: *"As competition for acquisitions increases that may
  result in fewer acquisition opportunities available to us and/or higher acquisition prices, and
  some of our competitors may have greater financial resources than us."* A position anyone can buy
  at auction from a retiring family is priced at its economics; it is not a moat.
- **Untapped pricing power [E3-33] and the two-characteristic test [E2-44].** No. The registrant
  sells the manufacturer's product at a price the customer compares online; the 2021-22 margin was
  the manufacturers' shortage, and it is being competed away as supply returns (new-vehicle margin
  down three years running, Q2 2026 PRU (8.5)%). The same filing names the opposite pressures:
  manufacturers cutting dealer assistance (*"Certain of our OEM partners, including Toyota, have
  recently announced their intention to reduce these forms of dealership financial assistance"*),
  agency pricing in the U.K., Chinese brands that *"often compete aggressively on price"*. **Where
  units exist, monitor units [E4-55]**: Q2 2026 new units (4.4)% and used retail units (11.2)% with
  total gross profit (8.0)%.
- Class: [ ] WIDE [ ] NARROW **[x] NONE** [ ] PROVISIONAL · Direction: **narrowing from a supply-wave
  peak back toward the pre-2020 base**, [E4-32]'s direction test read against a moat that was never
  the company's.
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**
  **OUT, on the business.** [E3-03] clause (2) fails in the registrant's own words and in four of
  its five peers' words; the competitor row shows a mid-ranked member of a six-company class whose
  margins rise and fall together with manufacturer supply; the excess returns of 2021-23 are
  [E3-43]'s tight-supply case, which *"usually does not last long"*, and they are already mostly
  gone. **This is "a business", not a franchise.** Not UNKNOWABLE: nothing about the answer depends
  on the future being knowable; the filings answer it. **The file closes here. Everything below is
  recorded beneath the close and carries no verdict.**

---
# BELOW THE CLOSE: MATERIAL RECORDED WITHOUT VERDICTS

*Q2 closed the file OUT on the business. Operator rule 2 bars any Q5 output being reported as a
clearance, and the hard sequence bars verdicts on Q3 to Q6. The material below was gathered because
the brief's priors were hypotheses to be refuted, and a reader deciding whether Q2 was right is
entitled to the rest of the evidence. **No box below is ticked as a verdict.***

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? MATERIAL ONLY, NO VERDICT

**Weight case, as it would be declared.** **Daily execution: ticked**, from Q2's own finding: this is
[E3-43]'s *"a business"*, which *"unlike a franchise, can be killed by poor management"*, and
[E3-74]'s retailing, where *"you cannot coast"* **[E3-38]**. **Leverage: ticked.** Tangible equity at
2026-06-30 is **negative**: equity $2,952.2M less goodwill $2,172.6M and franchise rights $947.4M =
**$(167.8)M**, against $3,363.0M of non-floor-plan debt and $2,181.2M of floor-plan notes (10-Q
`0001031203-26-000123`), before the $1,250M of notes closed on 2026-09-22 **[E3-29]**. Control:
unticked. **Q3 would be a binary gate.**

**Honesty, dated.** No integrity matter found in the 10-K legal-proceedings note, which describes only
ordinary-course dealership litigation. No restatement; the 10-K's error-correction boxes are unchecked.
**[E5-17]'s cap applies: this is the absence of a found disqualifier, not a finding.**

**The flags [E4-22, E5-15, E4-29, E4-30].**
- **Adjusted earnings promoted [E4-29] and the except-for flag [E2-57]: FIRES, and it is the sharpest
  Q3 finding.** The 2026 proxy (DEF 14A `0001031203-26-000100`) leads its performance summary with:
  *"Diluted earnings per common share from continuing operations of $25.13, a decrease of 31.6%
  compared to 2024. Adjusted diluted earnings per common share from continuing operations* of $40.71,
  a 3.8% increase compared to 2024"*. GAAP net income from continuing operations was **$323.7M**;
  adjusted was **$524.5M**, a gap of **$200.8M (62% of GAAP)**, most of it the U.K. impairments and
  restructuring. Across 2021-25 the proxy's own PvP table gives adjusted net income of 633.7 / 728.7 /
  623.3 / 530.6 / 524.5 against GAAP net income of 552.1 / 751.5 / 601.6 / 498.1 / 325.2: **adjusted is
  11% higher over five years ($3,040.8M against $2,728.5M)**. To the company's credit, **2022's
  adjustment went the other way** (adjusted $22.8M *below* GAAP, removing gains), which is the candor
  direction [E2-69] asks a reader to weigh. The word EBITDA appears nowhere in the Q2 2026 release; it
  appears in the notes offering memorandum (pro forma adjusted EBITDA $1,038.8M, *"Net leverage ratio"*
  4.2x), which is addressed to lenders.
- **What pay vests on [E4-27].** The 2025 annual bonus was 80% on *"Adjusted Net Income From Continuing
  Operations"* (threshold $423M, target $528M, maximum $582M), and the result was: *"Actual/reported
  adjusted net income from continuing operations: $525 million; as further adjusted by the CHR
  Committee: $542 million."* The further adjustment was *"for a portion of the unbudgeted impact of the
  significant increases in the U.K. national insurance contribution and U.K. minimum wage in 2025."*
  **Reported adjusted net income came in below target; the committee's second adjustment lifted it
  above target, in a year GAAP net income fell 35%.** The 2025 performance shares vest 50% on
  cumulative two-year adjusted EPS ($72 threshold / $84 target / $95 maximum) and 50% on relative TSR
  against the five peers in the Q2 row. CEO Summary Compensation Table total **$11,120,439** (2025),
  compensation actually paid $9,959,830. The PvP five-year TSR: **$310.15 against the peer group's
  $202.84**, so the relative-TSR half has been earned on the record.
- **Trumpeted projections [E4-22] third flag: not found.** The Q2 2026 release gives no earnings
  guidance; the one forward target found is the *"$50 million annualized expense reduction
  initiative"*, reported as completed.
- **Serial issuance [E5-15]: no. The opposite.** Weighted-average basic shares were 23,380 thousand in 2014 (FY2016
  10-K); 11,922,225 were outstanding on 2026-07-24; **$2,188M of buybacks 2014-25**.
- **Cash-tax tell [E4-30]: clean.** Cash taxes paid as a share of pre-tax income: 27.9% (2017), 19.9%,
  21.2%, 16.6%, 20.4%, 20.5%, 23.0%, 22.2%, **24.0% (2025)**, the post-2017 step being the federal rate
  cut; no falling trend.
- **Metric switching [E2-49]: not found.** Adjusted net income was the bonus metric before and after
  the 2025 fall; the U.K. strategic goals (20%) were added for the Inchcape integration.

**The primary test [E2-01].** Net income on average equity: **14.8% (2019), 21.2%, 33.7%, 37.0%
(2022), 24.5%, 17.6%, 11.3% (2025)**, with tangible equity now negative, so the return is on a
denominator made mostly of purchased goodwill. On [E2-43]'s unleveraged net tangible assets the
pre-tax return is in Q2's paragraph: 20% (2019), 50% (2022), 19% (2025).

**Capital allocation [E5-08, E5-24, E4-13].** **2025: 1,343,229 shares bought at an average $413.05
($554.8M)**, more than the year's operating cash less capital spending ($694.5M − $270.0M = $424.5M),
while long-term debt rose from $2,737.9M to $3,440.5M. H1 2026: 205,190 shares at $353.08. **The quote
is now $247.79**, 40% below the 2025 average. Condition (1), ample funds, is not met in the sense
[E5-25] gives it: the buyback was borrowed. Condition (2) cannot be scored without an intrinsic-value
range, and the only one this run computes (below) is a computation, not a clearance; with the humility
clause **[E4-13]**, management knows the business better than I do. **The institutional imperative
[E2-30]**: item (2), *"acquisitions will materialize to soak up available funds"*, is the reading the
record invites and not one this run can prove: **$4,813M of acquisitions over 2014-25 against $5,683M
of operating cash**, Inchcape (2024, U.K., *"revenues and net loss attributable to Inchcape Retail for
the year ended December 31, 2025, of $ 2.4 billion and $ 18.7 million"*, then $192.8M of 2025
impairments, most in the U.K.), and Hennessy (~$1.3bn, announced the same day as a quarter in which
gross profit fell 8%). **The market's reading on 2026-07-30 was a 17% one-day fall.** The Conifer
agreement (2026-09-21) puts one of *"Group 1’s largest shareholders"* on the board with a 19% standstill
and a vote with management; recorded, not scored.

- **VERDICT: not written.** Q2 closed the file.

## Q4 — WILL IT SURVIVE? MATERIAL ONLY, NO VERDICT

### Owner earnings **[E2-23]**, rebuilt year by year from the filed cash-flow statements; no net-income proxy

Operating cash less stock compensation (the cash-flow add-back line, in full **[E5-06]**) less (c).
**The floor-plan prior, tested and confirmed as a real distortion of single years, and refuted as a
distortion of the long mean.** GPI says it in the MD&A: *"In accordance with U.S. GAAP, we report
floorplan financed with lenders affiliated with our vehicle manufacturers [...] within Cash Flows from
Operating Activities [...] We report floorplan financed with the Revolving Credit Facility [...] within
Cash Flows from Financing Activities"*, and it publishes an *"Adjusted net cash provided by operating
activities"* ($699.2M for 2025 against GAAP $694.5M; $683.0M against $586.3M for 2024). I did not use
the company's figure. I built my own floor-plan-neutral line from filed lines: GAAP operating cash plus
the net of the financing section's *"Borrowings on credit facility — floorplan line and other"* and
*"Repayments"*. **The swings are large: 2021 GAAP operating cash $1,259.6M included a $529.8M inventory
liquidation while $468.6M of credit-facility floor plan was repaid in financing; 2023's $190.2M
absorbed a $567.6M inventory rebuild while $425.8M was borrowed.** Summed over 2014-25 the floor-plan
net is **$(4.6)M**: over twelve years the two constructions agree to the dollar; over 2021-25 the
neutral line is $68M a year higher.

| $M | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | TTM 6/26 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| operating cash (GAAP) | 198.3 | 141.0 | 384.9 | 196.5 | 270.0 | 370.9 | 805.4 | 1,259.6 | 585.9 | 190.2 | 586.3 | 694.5 | 439.2 |
| floor-plan line, net (financing) | 29.3 | 52.7 | (78.8) | 61.2 | 84.2 | (118.6) | (375.9) | (468.6) | 469.6 | 425.8 | 102.1 | (187.7) | 219.7 |
| SBC | 16.0 | 18.9 | 21.1 | 18.9 | 18.7 | 18.8 | 32.3 | 28.3 | 27.0 | 20.1 | 25.2 | 29.0 | 32.0 |
| capex | 150.4 | 120.3 | 156.5 | 215.8 | 141.0 | 191.8 | 103.2 | 143.6 | 155.5 | 185.4 | 245.1 | 270.0 | 272.9 |
| D&A | 42.3 | 47.2 | 51.2 | 57.9 | 67.1 | 71.6 | 75.8 | 78.9 | 89.3 | 92.0 | 113.1 | 121.1 | 125.2 |
| **OE, GAAP, capex end** | 31.9 | 1.9 | 207.3 | (38.2) | 110.3 | 160.3 | 669.9 | 1,087.7 | 403.4 | (15.3) | 316.0 | 395.5 | 134.3 |
| **OE, floor-plan-neutral, capex end** | 61.2 | 54.7 | 128.5 | 23.0 | 194.5 | 41.7 | 294.0 | 619.1 | 873.0 | 410.5 | 418.1 | 207.8 | 354.0 |
| acquisitions paid | 336.6 | 212.3 | 57.3 | 109.1 | 135.3 | 143.2 | 1.3 | 1,099.6 | 528.7 | 366.1 | 1,276.8 | 546.8 | |

Sources: cash-flow statements of the FY2016, FY2019, FY2021, FY2023, FY2025 10-Ks and the Q2 2026
10-Q (accessions at Step 0 and Q2); TTM = FY2025 − H1 2025 + H1 2026.

- **Windows [E4-25, E4-38]**, capex end to D&A end: **12-year 2014-25: $278-375M** (both
  constructions); **5-year 2021-25: $437-538M GAAP, $506-607M neutral**; **2014-19, the six years before
  the wave: $79-185M GAAP, $84-190M neutral**; **TTM: $134-282M GAAP, $354-502M neutral**.
- **Combined range: roughly $80M to $610M, about 7.5 times its bottom. [E4-25]'s "no useful conclusion
  can be reached".** The distorted years are named: **2020-22, the supply wave** (normalized DOWN, not
  up, under **[E4-41]**; the 5-year window contains two of its three years) and **2021, 2024, 2025, the
  acquisition years**.
- **(c), a disclosed guess.** Capex exceeded D&A in every one of the twelve years (ratio 1.4 to 3.7).
  Part of capex is real estate (2025: $55.7M of $270.0M) and part is manufacturer-required facility
  "imaging" (MD&A: *"manufacturer imaging programs"*), which is maintenance in [E2-23]'s sense because
  the franchise requires it. **The D&A end [E3-44, E2-41] is displayed but I place (c) at the capex
  end**, the non-real-estate capex ($214.3M in 2025, 1.8x D&A) being the closest filed figure to it.
- **The acquisition prior [E4-41], tested and confirmed.** **$4,813M of acquisitions over 2014-25 and
  $3,818M over 2021-25**, against operating cash of $5,683M and $3,317M. Revenue doubled (9.9bn to
  22.6bn) mostly by purchase; the numerator of every recent window contains bought earnings whose
  price sits in debt, not in the cap. **Interest paid rose from $80.2M (2014) to $268.2M (2025)**,
  before the $1,250M of 6.25%/6.625% notes (about $80M a year more).

### Great, good, or gruesome? **[E4-20]**: stated, unticked
The owner-earnings series says **good at best, and only through the wave**: before 2020 the business
earned $80-190M a year on a ~$1.1bn equity base while spending about as much on acquisitions; the
capital added since has been bought at prices that produced $192.8M of impairments in its first full
year (U.K.).

### Staying power, all three scored **[E5-11]**: findings, not a verdict
- (1) large and reliable stream of earnings: **no**; 2014-19 owner earnings of $2M to $207M a year.
- (2) massive liquid assets: **no**; cash $164.5M at 2026-06-30 plus $157.5M in floor-plan offset
  accounts, against $2,181.2M of floor-plan notes that roll with the inventory.
- (3) no significant near-term cash requirements: **not met**. Floor plan is payable when each car is
  sold and is *"benchmarked to SOFR"*; current maturities of long-term debt $314.6M; the Hennessy price
  (~$1.3bn plus inventory) is due at closing by early 2027; the revolver matures 2030-05-30.
- **Leverage, named [E4-16] and the coverage test [E2-54]**: 2025 operating cash plus interest paid,
  less capex, covered interest paid **2.6x** ($694.5M + $268.2M − $270.0M over $268.2M). Covenants at
  2025-12-31: total adjusted leverage 3.14 against a maximum of 5.75; fixed-charge coverage 3.28
  against a minimum of 1.20. The company's own pro forma net leverage after Hennessy: **4.2x**.

### The way it dies, named from exposure **[E2-27, E3-24, E4-40]**
**Shape #6, THE BORROWED BALANCE SHEET, with #20 THE WAVE as a feature** (`Screens/SURVIVAL SHAPES -
index.md`; no new shape). The business runs on floor plan it must keep rolling and on acquisition
debt it has just enlarged, at the moment its margin is returning from a wave to the pre-2020 base.
Quantified from filed figures: at the 2014-19 operating margin of ~3.3% (ex-items) on TTM revenue of
$22,154.8M, income from operations would be ~$730M against TTM floor-plan interest $93.5M and other
interest $195.9M plus ~$80M on the new notes: **pre-tax ~$360M, still positive.** The company's own
4.2x pro forma leverage would pass 5.75x on a fall of roughly a quarter in adjusted EBITDA (the
covenant's definition differs from the marketing ratio, so this is an approximation, stated as one).
**Likelihood: a low-level possibility** that it threatens solvency; the real possibility is the owner's
return, not survival.

- **VERDICT: not written.** Q2 closed the file.

## COMPUTATION — NOT A CLEARANCE
*No entry language. No box. Operator rule 3.*
- Yields on the $2,954M cap: 12-year **9.4% to 12.7%**; 5-year **14.8% to 20.5%**; 2014-19 **2.7% to
  6.4%**; TTM **4.5% to 17.0%**; against the sovereign **5.47%** and the ~10% floor **[E4-28]**.
- Value at the floor, round numbers **[E4-01]**: **roughly $1bn to $6bn against $3.0bn**, the price
  inside the range, which under the screamer test is no useful conclusion. The 12-year capex-end mean
  needs about half a point a year of growth to reach the floor, but that mean was earned on the
  pre-acquisition share count and interest bill, and the range it sits in is [E4-25]'s. Windage count:
  **one** (the capex end of (c)).

## Q6 — WHAT WOULD PROVE ME WRONG? REVERSAL CONDITIONS, NO POSITION
No alert and no PORTFOLIO.md row: the name failed on the business (the QLYS ruling). What would reopen
Q2, in words, before any price is looked at **[E1-02]**:
1. **An operating margin above all five listed peers' for three consecutive years in a supply-ample
   market** (new-vehicle gross margin back near the 2014-19 5%), which would be the relative advantage
   the row did not show.
2. **A filed sentence that changes**: the registrant's *"We do not have any cost advantage in
   purchasing new vehicles"* withdrawn or reversed with evidence.
3. **The U.S. regime** is the risk the other way: the agency or direct model arriving in the U.S. would
   be [E3-30]'s permanent slip, not a cycle.

- **VERDICT: not written.** Q2 closed the file.

---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN, Q2 OUT. Q3, Q4 and Q6 carry material
  and the words "not written"; Q5's block is replaced by COMPUTATION — NOT A CLEARANCE, with no box,
  no ranking and no entry language (operator rule 3).
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's figures are off
  the filed FY2025 statements and Item 1.
- [x] Every UNRESEARCHED verdict names the artifact: **none issued.** The only limit met is named with
  its rung: the private dealer groups (Hennessy among them) file nothing; the row is not PROVISIONAL
  for the reason written at Q2.
- [x] Every UNKNOWABLE verdict states what cannot be known: **none issued.** [E4-04]'s perimeter close
  was considered and refused in writing at Q2.
- [x] **Step 0: the filing was read, with accession numbers; two figures cross-checked by
  re-derivation** (FY2025 operating cash $694.5M from its own lines; total equity $2,789.1M from the
  equity statement's closing row).
- [x] **Owner earnings on multi-year means, every window published, both (c) ends and the judged end
  disclosed, the floor-plan construction tested both ways**; SBC off the cash-flow line in full; **no
  net-income proxy anywhere** (the July 5-pack's proxy was not used; PRIME RULE 3 as amended 2026-09-20).
- [x] **Competitor row filled** with all five U.S.-listed franchised groups, ten 10-Ks, accessions
  recorded; built by a sub-agent of this run from the filed statements, working file in
  `peers/COMPETITOR_ROW.md`, figures read by me against its per-peer tables before use.
- [x] **Sovereign for the earnings currency (USD, from the segment note), from the issuing authority,
  dated**: 5.47%, US Treasury daily par yield curve, 30 Yr, 09/24/2026, raw file saved; FRED not used.
- [x] Value stated as a round-number range ($1bn to $6bn), inside the COMPUTATION only.
- [x] One bar: none chosen, because Q5 did not open; windage count stated (ONE).
- [x] **Prices dated; aggregator used for the live quote only and flagged** ($247.79, close 2026-09-24,
  Yahoo chart endpoint, raw responses saved).
- [x] **Every ledger id cited resolves** (checked by `tools/check_framework.py`, check 5) and the
  acceptance test PASSES before the fold commit.
- [x] Run committed to git with pathspecs: `effc95b` (claim), `38fd01d` (Step 0, Q1), `4e013c5` (Q2),
  then the below-the-close and fold commits.

**ERRORS AND ARTIFACTS, recorded rather than smoothed.**
1. **My own error, caught before commit:** the first Step 0 draft said the U.S. was "98%" of 2023-25
   pre-tax income; the sum is $1,947.4M of $1,908.6M, **102%**. Corrected.
2. **My own error, caught before commit:** a shell heredoc expanded the dollar signs in that corrected
   line and wrote "(,947.4M of ,908.6M ...)" into the run file; seen on the read-back and fixed by
   hand before the Q1 commit.
3. **My own error, caught before commit:** Q2 first quoted the MD&A as *"continues to modera[te]"*, a
   bracketed completion of a truncated grep. The filed sentence was then read in full and quoted
   whole (*"continues to moderate towards pre-COVID levels ..."*). PRIME RULE 1.
4. **Text artifacts kept as filed:** the balance sheet's *"no ne issued"*; the 10-K's *"a pproximately"*
   and *"based o n"* splits in the cover's float sentence.
5. **The price response carries a null close for 2026-09-22**; that day is not quoted.
6. **The screen's two dated figures (cap and float) were both right**: the flag was a price move, not
   a data error; recorded at Step 0.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- **One line: Q1 IN / Q2 OUT, on the business.** A franchised car retailer that says in its own 10-K it
  has no cost advantage in buying cars and no exclusive territory, ranked fourth of six listed peers on
  operating margin, whose 2021-22 returns were the manufacturers' supply shortage and are returning to
  the 3.3% pre-2020 base; at $247.79 (cap $2,954M) against a 5.47% sovereign the owner-earnings range
  runs from about $80M to $610M, too wide for a conclusion, recorded as arithmetic only.
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.
