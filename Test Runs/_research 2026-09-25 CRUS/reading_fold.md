
## UPDATE 2026-09-25 - CRUS: Q2 OUT. A very good supplier and not a franchise: the one customer that buys 91% caps the price by contract and dual-sources, and the customers free to choose have left.

**Cirrus Logic, Inc. (CRUS), wave 7 name 32, register entry 164.** Run file `Test Runs/2026-09-25 Run - CRUS Cirrus
Logic.md`. Price $118.80 (close 2026-09-24, aggregator, flagged) x 50,117,561 shares (10-Q cover for 2026-06-27,
`0000772406-26-000037`) = cap $5,954M; sovereign 5.47% (US Treasury, 30 Yr, 09/24/2026). **Q1 IN, Q2 OUT on the
business.**

### The finding
- **[E3-03] criterion (2) fails on the customer's filed conduct, dated.** Apple is *"approximately 91 percent"* of
  FY2026 sales. The risk factors: customers *"can stop incorporating our products ... with limited notice to us and
  suffer little or no penalty"*, buy without minimums, *"regularly evaluate alternative sources of supply ... dual-source"*
  (**first filed in the FY2024 10-K**), and Cirrus has *"made commitments not to exceed certain pricing with some key
  customers"* (**first filed in the FY2023 10-K**). The shareholder letters report the price-downs as a scheduled
  item (*"previously anticipated pricing reductions"*, Q1 FY2027). [E3-03]'s demonstration clause, *"ability to
  regularly price its product or service aggressively"*, runs the other way.
- **The open-market series is the honest one, as units are for [E4-55].** Non-Apple revenue, from filed sales and the
  filed Apple percentages: about $398M in FY2016 (Samsung alone 15%) to about $180M in FY2026, down about 52% from
  FY2022 even after the $277M Lion Semiconductor purchase (impaired $85.8M a year later). Customers who are free to
  choose have chosen others.
- **[E2-53]**: one customer, not the business, sets how good Cirrus will be. **[E4-04] was refused as the ground**:
  the 2026-09-20 ruling's maintained-lead clause fits a twenty-year relationship. The failure is who holds the
  terms, not whether the relationship lasts. The perimeter close (UNKNOWABLE) was refused because the name does not
  pass [E3-03].
- **Strongest evidence against, weighed at [E3-47] and recorded**: gross margin 47.5% to 52.8% over ten years, a
  ten-year-high operating margin (23.0%), Apple's own 10-K saying new products *"often utilize custom components
  available from only one source"*, and a far better record with that customer than Skyworks (operating margin 27.8%
  to 12.2% since FY2022) or Qorvo (26.4% to 11.2%). All of it is compatible with the customer continuing to choose
  Cirrus; none of it shows the customer cannot choose otherwise.

### For the next single-customer component supplier
**Date the risk-factor language across every 10-K, not just the latest.** The two sentences that decided this file
(the price cap, the dual-sourcing) are not in the FY2022 10-K and are in FY2023's and FY2024's respectively; a run
reading one 10-K sees boilerplate, a run reading five sees a customer tightening terms. And **compute the
non-dominant-customer revenue in dollars**: a rising concentration percentage hides whether the rest of the business
is shrinking or the big customer is growing. Here it was both.

### Priors, refuted or confirmed
- **All the brief's priors confirmed**: fabless, fiscal year to late March, Apple the majority (named, 91%), GF and TSMC
  (with ASE, Amkor, STATS ChipPAC, SFA Semicon and SPIL), the $277M acquisition (Lion, FY2022), buybacks shrinking the
  count (63.4M basic weighted FY2018 to 50.1M on the cover).
- **Not in the brief**: the Wolfson layer of the perimeter ($444M, FY2015; its MEMS line discontinued FY2020), the
  pricing-cap and dual-source dating, and **the STEP UP flag's cause**: $180.3M of the FY2022 GlobalFoundries wafer
  prepayment flowing back through operating cash in FY2024-FY2026, a timing item, beside real operating growth ($343M to
  $460M operating income) that persisted.

### Beneath the close, for the next reader
- [E4-29] does not fire; non-GAAP EPS adds back SBC ($0.38 of $1.95 in Q4 FY2026); one guidance outturn inside its range;
  buybacks $1,738M over twelve years against $723M of SBC, the latest at $140.53 against $118.80 now. DEF 14A not read.
- Owner earnings FY2015-FY2026, SBC every year, (c) from total capex to D&A, prepayment stripped: 3y $310-333M, 5y
  $262-289M, 10y $226-253M, FY2026 alone $463-501M; $1.17bn cash and securities, no debt. Five-year yield 4.4-4.9%
  against 5.47%; about $3.5-3.7bn at the ~10% floor with no growth including cash, against $5.95bn. Arithmetic only.

### Tooling, REPORTED NOT PATCHED
- **`tools/run.py` omits "Investments in technology" from capex** ($0.7-29.3M a year at Cirrus, $29.3M in FY2018), so
  its capex end runs slightly high on any filer that capitalises purchased IP on a separate investing line.
- **`tools/run.py` headlines the three-year window** (6.21-6.65% here) with a $180.3M working-capital unwind inside it.
  It prints the divergence warning correctly; it cannot know a prepayment is a prepayment. A reader must.
- **`tools/sources.cik_for()` returns a (CIK, name) tuple**; passing it to `sec_facts()` builds a malformed URL with a
  clear error. Not a defect in existing callers; a trap for new scripts.
- `tools/run.py` did **not** repeat the CLX defect here: the FY2026 10-K is filed and was read.

**No alert, no PORTFOLIO.md row** (failed on the business). Reversal conditions in words at Q6, headed by a 10-K
withdrawing the pricing commitments and dual-sourcing language while gross margin holds, or three years of non-Apple
revenue growth to above about $400M without an acquisition.
