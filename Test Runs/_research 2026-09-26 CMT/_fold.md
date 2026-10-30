
## UPDATE 2026-09-26 - CMT: Q2 OUT. Core Molding moulds truck, powersports and industrial parts to its customers' designs; its own 10-K has said for twenty years that those customers demand and receive price reductions through competitive selection, and its operating margin has summed to 5.3% of sales over twenty-two years. A supplier, not a franchise.

**Core Molding Technologies, Inc. (CMT), wave 7 name 49, register entry 191.** Run file `Test Runs/2026-09-26 Run - CMT Core Molding Technologies.md`.
CIK 0001026655, fiscal year to 31 December. Price $23.21 (NYSE American close 2026-09-25, aggregator, flagged)
x 8,849,034 shares (10-Q cover at 2026-08-03, `0001026655-26-000053`, issued including 285,735 unvested restricted) =
cap $205.4M ($198.8M on the balance-sheet count); sovereign 5.49% (US Treasury, 30 Yr, 09/25/2026). **Q1 IN, Q2 OUT on
the business.** One unattended session ran the whole file, from the claim to the fold.

### The finding
- **[E3-03] criterion (2) fails in the registrant's own words, the same every year FY2006-FY2025**: *"OEMs continue to
  demand and receive price reductions and measurable increases in quality through their use of competitive selection
  processes, rating programs, and various other arrangements"*; *"end products are similar and are not unique to a
  facility or customer base"*; *"Our products primarily compete on the basis of capability, product quality, cost, and
  delivery"*. Six rival moulders named (Molded Fiber Glass, CSP, Ashley, RMC, STS Group, 20/20).
- **The customers' terms and conduct say the same.** The founding customer (Navistar, now International Motors) kept Core
  as primary supplier *"as long as the Company remains competitive in cost, quality, and delivery"* (FY2006-FY2019);
  Volvo's existing programmes moved to programmes the company *"does not support"* (16% of 2023 sales, 4% of 2025).
- **[E2-44] fails twice**: fixed-price contracts that *"may not provide for recovery of all of the Company's cost
  increases"* (a 4.8-point price lag in 2021, recovered over four years), and capex 1.26 times depreciation over twenty
  years. **Returns**: operating margin -4.1% to 11.8%, 5.3% summed FY2004-FY2025; two SEC-filing suppliers to the same
  kind of customer earned 3.4% and 5.7% over 2010-2025.

### Beneath the close
- **Owner earnings, every window 3 to 20 years and both ends: $5.45M to $15.82M (2.65-7.70%).** The three-year window
  (FY2023-FY2025) is above the 5.49% sovereign at both ends; every window of eight years or more is below it. FY2023-FY2024
  carry 101.7% of the five-year capex-end total. **At or below zero in nine of twenty years on the capex end** (FY2018
  -$14.1M), and -$10.0M over the twelve months to 2026-06-30 as the Mexico expansion is paid for. SBC resolves from 2006;
  no NCI. At the ~10% floor with no growth about $6-18 a share, at the sovereign $11-33, against $23.21 (computation only).
- **Q3 prompts**: [E4-29] fires in the releases and investor decks (Adjusted EBITDA headlined; the 10-K is clean);
  three-to-five-year targets (revenue above $500M, operating margin 8-10%) against $273.8M and 5.2%, and annual revenue
  guidance missed on the downside three years running; the proxy was read and pay rests on EBIT, operating cash and ROCE,
  not EBITDA; five small disclosure slips in thirteen months of 8-Ks.
- **Signature, not a verdict**: #11 THE PASS-THROUGH in its re-tendered-programme form.

### What the reading list should carry forward
- **The OEM-supplier reading, for the next auto, truck or equipment component maker**: read Item 1A for the price-down
  sentence and the major-customers note across every 10-K on file. When the registrant says its customers *"demand and
  receive price reductions"* through competitive selection, and the major-customer list turns over, criterion (2) is
  read in its own words; a *"Sole Sourced"* claim in an investor deck is a claim about one programme, not a franchise.
- **Read the investor decks furnished under Item 7.01 before scoring Q3.** Here the 10-K is plain and GAAP-only, and the
  decks carry the Adjusted EBITDA headline, the *"Competitive Moat"* slide and the multi-year targets. The CGNX rule
  (read the EX-99.1 release) extends to the decks.
- **Press utilisation is this trade's physical series [E4-55]**: large compression presses 89% (2022) to 50% (2025), filed
  in Item 1 every year.
- **Next dates**: the 10-Q for the quarter to 2026-09-30 (early November 2026); the Volvo roof programme's start of
  production in Q1 2027.

### Priors refuted or confirmed
- `deal_note`: a credit facility, as it guessed (the Third Amendment with Huntington, 2026-07-02). `wc_note`: **refuted**;
  payables were 43% of 2021 operating cash, but receivables and inventories used $15.7M and working capital used $5.9M net.
  `level_note_oe`: the -$14.1M is FY2018, confirmed, the field cut off mid-figure. `best_year_dep_oe` 0.678: two years
  (FY2023-FY2024) carry the whole five-year window, confirmed. `spread_caveat`: rebuilt over twenty years. `years_filed` 16
  is the XBRL span; the 10-Ks run to FY1996.

### Tooling defects (reported, not patched)
- **`run.py` printed "GROWTH THE PRICE ASSUMES -13.6%"**: the sixth run running (MATX, PPG, LNN, SYY, MLI, CMT).
- **`run.py` printed "POINTS OVER THE SOVEREIGN +3.53 .. +5.33"** on yields of 6.23-7.95% against 5.49%: the third run with
  this line wrong (SYY, MLI, CMT).
- `run.py`'s per-year minimum and maximum mix the two (c) ends inside one window; the D&A end carries acquired-intangible
  amortisation (the open ruling); it stops at five years; the screen's level notes are truncated in the CSV;
  `cover_shares.py` returns an "issued" count that includes unvested restricted stock without flagging it.
