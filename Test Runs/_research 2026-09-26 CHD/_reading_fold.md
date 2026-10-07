
## UPDATE 2026-09-26 - CHD: Q1-Q4 IN (Q2 NARROW), Q5 QUIT ON. Church & Dwight sells value laundry and baking soda and has bought most of its premium brands; over the last decade it raised price 20% while its units rose 23% on almost no tangible capital, which clears the franchise demonstration narrowly. But its own 10-K says it meets cost increases "primarily by implementing cost reduction programs and, to a lesser extent, by passing along cost increases to customers", 89% of its operating capital is the price of brands, and at $96.38 the owner-earnings yield is 3.8-4.1% against a 5.49% bond.

**Church & Dwight Co., Inc. (CHD), wave 7 name 59, register entry 201.** Run file `Test Runs/2026-09-26 Run - CHD Church & Dwight.md`.
Price $96.38 (2026-09-25, Yahoo, flagged) x 237,203,907 common shares (10-Q cover `0001193125-26-327567`) = $22,861.7M; sovereign
5.49% (US Treasury 30Y par, 09/25/2026). **PASS/FAIL: PASS Q1-Q4 (Q2 NARROW), FAIL at Q5 (quit on at the ~10% floor).**

### What the run found
- **Two regimes in one company, from the filer's own component tables**: 2010-2017 price/mix −7.7% while volume rose 40.9%, bought with
  trade promotion *"due to competitive pricing activity"* and against P&G's discounted Simply Tide; 2018-2025 price/mix +22.7% with volume
  +14.0%. Ten years (2016-2025): price +20.0%, units +23.4%, P&G's shape with more units. 2022 lost 5.1 points of volume for 6.5 of price;
  2023 and 2024 grew units while holding it.
- **The value tier is not a franchise, in the filer's words**: 34% of consumer revenue; laundry *"subject to significant price
  competition"* and for fifteen years *"value products, priced at a discount from products identified by the Company as market leaders"*.
- **Returns**: pre-tax 59.8-121.0% on net tangible operating assets every year 2009-2025 (top of the household row with Colgate), because
  tangible capital stayed at about $0.7bn while sales went from $2.5bn to $6.2bn; but goodwill and intangibles rose to 89% of operating
  capital, and on that capital the return fell from 17.8-20.2% (2009-2016) to 14.8-17.5% (2017-2025), below P&G, Colgate and
  Kimberly-Clark.
- **The bought record**: six of seven power brands bought since 2001; VitaFusion ($652.3M in 2012, sold for $160.3M in 2025 after a
  $357.1M impairment) and Flawless ($475M in 2019, impaired $411.0M in 2022, exited 2025) failed; TheraBreath, Hero and Zicam carry the
  growth. The premium tier depends on acquisition judgment: recorded at Q2 as a moat defect.
- **Owner earnings, every window 3-21 years, both ends**: $538.1-1,014.2M (2.35-4.44%); five-year $858.8-947.3M (3.76-4.14%); with the
  $4.3bn of purchases 2016-2025 counted, $349.4M a year over ten years. Coverage 12.6x. GOOD class. Named death #19 THE SHELF (Walmart 23%,
  top four 44%, private label named in stain fighters, pregnancy tests and oral analgesics), feature #24 THE BOUGHT AVERAGE.
- **Q3**: no disqualifier; the growth-target flag with [E3-48] performed (fiscal 2025 missed every line of the January 2025 outlook and was
  reported against the lowered one); Adjusted EPS excludes the failed purchases; pay on adjusted figures and, from 2026, on net-sales growth
  rates; a capital-allocation flag on the 2025 buybacks at $83.59-95.71.
- **Q5**: expectancy 7.8-9.1% with the filed 4.0-4.7% growth; value about $60-81 against $96.38. Bands $60.34 and $80.67 armed, each a
  prompt for a full re-run.

### Refuted or corrected priors
- **The brief's "portfolio of bought brands" prior was half right**: the margin and the premium tier were bought, but the units kept growing
  after purchase and the company-level price-and-volume record clears the demonstration narrowly; neither the FUL pattern (price following
  cost) nor the Clorox pattern (units that never came back) is in CHD's filings.
- **The CL run's note** (*"CHD's 59-116% is real but on a much smaller and more acquisition-shaped base"*) **is confirmed** in figures:
  goodwill and intangibles are 89% of operating capital, the highest in the row after Coty.

### Brief errors and tooling (reported, not patched)
- **Brief errors**: cap 5.1% stale; `vs_sovereign` on the stale 5.35%; the screen's $779M bottom puts purchased-intangible amortisation and
  the non-cash lease cost into (c) (the top $899M reproduces as the 3y capex end); `acq_note` misses the 2026 Touchland earnout and Miss
  Mouth's purchase and the acquisition-related stock; `years_filed` 18 against 23; the brief placed the CL run's note in the CL register
  entry, where it is not.
- **Tooling**: the CL run's `peer_metrics.py` does not read `SalesRevenueGoodsNet` (CHD's revenue tag to 2017); the screen's D&A end
  reads a cash-flow caption that at CHD includes lease cost; `run.py` not run.

**Next in the order file: KVUE.**
