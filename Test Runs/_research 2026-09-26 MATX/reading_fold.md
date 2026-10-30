
## UPDATE 2026-09-26 - MATX: Q2 OUT. Matson carries freight to Hawaii and Alaska behind the Jones Act, at rates the Surface Transportation Board supervises, and across the Pacific at rates the market sets; it earned 3.7-11.7% on its ocean assets in 2012-2019 and has earned more since 2020 because of China.

**Matson, Inc. (MATX), wave 7 name 45, register entry 177.** Run file `Test Runs/2026-09-26 Run - MATX Matson.md`.
CIK 0000003453. Price $224.66 (NYSE close 2026-09-25, aggregator, flagged) x 29,903,458 shares (10-Q cover for
2026-06-30, `0001104659-26-090003`) = cap $6,718.1M; sovereign 5.49% (US Treasury, 30 Yr, 09/25/2026). **Q1 IN, Q2 OUT
on the business.** MATX appears once earlier in this file, as a screen row (*"Matson - ocean shipping, cyclical"*); this
is its first run.

### The finding
- **Two businesses share one fleet, and each fails a different [E3-03] criterion.** The Hawaii and Alaska trades (51% of
  2025 Ocean revenue) are closed to foreign-built ships by the Jones Act, and their rates are *"subject to the
  jurisdiction of the Surface Transportation Board"*, presumed reasonable within +7.5% / -10% a year adjusted by PPI:
  **criterion (3) fails in the registrant's words, and the shelter is a statute, [E2-59]'s legal administration of
  costs and entry.** The framework's own reading, *"Regulation caps a franchise [...] and floors a commodity business;
  neither creates the class"*, decides it; the OTTR run read a regulated utility the same way. The China service fails
  **criterion (2)**: *"competitive with limited barriers to entry"*, named international carriers and air freight, new
  carriers entering in 2020-2021.
- **The demonstration clause is in the filer's fourteen-year segment series.** Ocean margin 5.4-12.5% and 3.7-11.7%
  pretax on Ocean assets in 2012-2019, while Matson was the largest carrier in a closed trade and Horizon had left it;
  company return on total capital fell from 17-32% on a fleet carried at 1980s cost to 7-10% once four new Jones Act
  ships were on the books (2015-2019: capital +$888M, operating income -$67M). **The step up since 2020 is China**, by
  the MD&A's own attribution every year from 2020 to 2025.
- **Customers do treat Pasha as a substitute**: Hawaii autos 81,500 (2013) to 39,400 (2023) after *"certain customer
  losses"*; volume gained whenever a competitor's ship is in dry-dock (2020, 2021, 2025); *"stable market share"* as the
  outlook for three years running. Hawaii containers have sat between 137,200 and 160,200 every year 2012-2025.
- **The one Jones Act liner carrier with a filed record in the same trades, Horizon Lines, earned 0.4-3.0% in its better
  years and lost money in others** before Matson (Alaska) and Pasha (Hawaii) bought it in 2015, and pled guilty in 2011
  to antitrust violations in its Puerto Rico Jones Act trade. The statute did not make the trade a franchise for the
  second carrier.

### Beneath the close
- **Owner earnings, every window 3 to 14 years: $206.9M to $496.9M on the capex end (3.1-7.4% on the cap)**; the D&A end
  ($314-646M) is INVALID in this business [E5-20] (1982 ships depreciate on 1982 dollars; a new ship costs about $335M).
  2016-2019 negative on the capex end; 2021-2022 carry 58% of the fourteen-year total; about $100M a year without them.
  At the ~10% floor with no growth about $70-170 a share, at the sovereign $125-300, against $224.66 (computation only).
- **[E4-29] fires in the release, the proxy letter and the annual cash incentive (paid on EBITDA)**, not in the 10-K,
  the CGNX pattern again. Performance shares paid 250% of target on a three-year ROIC of 17.9% against a 6.7% target set
  in January 2023; the MD&A credits the years to China rates [E2-73]. Buybacks of about 13.9M shares at $75-126 in
  2021-2025, shares down 31% since 2020.
- **Signature, not a verdict**: #14 THE PATRON (a statute under federal-court challenge since February 2025 shelters
  half the Ocean revenue and a fleet paid for at US prices), with [E2-58]'s cycle as a feature in China.

### What the reading list should carry forward
- **Statutory shelters are now read one way across three runs** (OTTR's utility, USPH's Medicare price, and here the
  Jones Act): the shelter is the regime's, criterion (3) is checked in the registrant's own rate language, and the
  demonstration clause is read on the years the shelter was the only thing working. A future Jones Act name (Kirby, a
  tanker operator) should expect the same test, not the same answer.
- **When a filer does not split profit by trade, the MD&A's year-by-year attribution is the evidence.** Matson says
  which trade moved operating income every year; fourteen years of those sentences carried the attribution here.
- **Next dates**: the Q3 2026 10-Q (early November 2026), whether the Q3 outlook of *"approximately 45 percent higher"*
  Ocean operating income arrives, and the first Aloha Class delivery (Q1 2027).

### Priors refuted or confirmed
- Confirmed: the Jones Act trades, Pasha and TOTE, SSAT on the equity method, Alaska from Horizon in 2015 ($495.4M of
  total consideration including $428.9M of Horizon's debt), the 2021-2022 surge, tariffs, LNG-capable renewal, the CCF,
  buybacks.
- Refuted or corrected: Guam and Micronesia are not Jones Act trades (US-flag, *"but not U.S. built"*); the second China
  service is MAX, not CLX+; "fallen back" overstated (2024-2025 operating income 3-4 times the 2012-2019 level);
  *de minimis* appears in neither the 10-K nor the 10-Q.
- `cap_flag` and `deal_note` empty: confirmed on the filings. `best_year_note` (two years carry the window): confirmed,
  58%. `level_note_oe` (early half straddles zero, -$93.2M): confirmed as 2017 but incomplete, because the screen cannot
  see 2018-2021 (below).

### Tooling defects (reported, not patched)
- **`floor_screen.CAPX_TAGS` and `run.py`'s capex set miss `PaymentsForConstructionInProcess` and
  `PaymentsToAcquireOtherProductiveAssets`**, so Matson's 2018-2021 capex does not resolve.
- **`run.py` then labels a non-contiguous window as contiguous** ("5-yr, 5 yrs of data" = 2017 plus 2022-2025), printing
  $350-507M against a true 2021-2025 of $497-646M.
- **`run.py`'s "GROWTH THE PRICE ASSUMES" printed -4.2%** where the price must assume positive growth; PPG's run saw
  -9.2% the same way.
- **The screen's `oe_top` sits at the D&A end** with no flag for capital-intensive filers where that end is invalid.
