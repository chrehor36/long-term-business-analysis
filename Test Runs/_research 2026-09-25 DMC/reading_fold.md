
## UPDATE 2026-09-25 - DMC: Q2 OUT. Fresh Del Monte, renamed Del Monte Corporation, grows and ships bananas and pineapples at a 3% operating margin, and in March 2026 bought Del Monte Foods' US canned business out of bankruptcy.

**Del Monte Corporation (DMC), formerly Fresh Del Monte Produce Inc. (FDP), wave 7 name 38, register entry 170.** Run
file `Test Runs/2026-09-25 Run - DMC Del Monte Corp.md`. CIK 0001047340 (renamed on EDGAR 2026-06-04). Price $30.51
(close 2026-09-24, aggregator, flagged) x 47,146,218 shares (10-Q cover for 2026-06-26, `0001047340-26-000042`) = cap
$1,438.4M; sovereign 5.47% (US Treasury, 30 Yr, 09/24/2026). **Q1 IN, Q2 OUT on the business.** No earlier note on
this name was found in this file.

### The first thing the run found: the screen's Item 1.01 was DMC buying, not DMC being bought
- The 8-K of 2026-03-25 (`0001193125-26-124060`) carries **Amendment No. 1 to an Asset Purchase Agreement** (the EX-2.1)
  and the Item 2.01 completion: on 2026-03-19 DMC bought Del Monte Foods' US *"canned vegetable, tomato, and refrigerated
  fruit business assets"*, seven plants and *"global ownership of the Del Monte® brand"* for *"$285 million plus
  assumption of certain liabilities"*, won at *"a competitive bankruptcy auction process under Section 363"* (APA 8-K of
  2026-02-12). Total consideration $310.2M; net assets fair-valued at $341.9M. **No bid for DMC exists in the filing
  list; the quote is a price, not a spread.**
- The perimeter changed: prepared foods is **19% of Q2 2026 sales**, long-term debt went from $173.0M to $414.6M, and no
  statements of the acquired business have been filed. Seven years earlier the same management bought Mann Packing for
  $357.2M; it was sold on 2025-12-15 for $19.0M plus inventory.

### The finding
- **The registrant says it is a commodity business in plain words.** Bananas: *"few barriers to entry"*, supply that
  *"can be increased relatively quickly"*, prices that *"fluctuate significantly"*. The whole industry competes on
  price among other things, and sales depend on *"the availability of seasonal and alternative produce"*. Prepared
  foods: *"Consumer choices are driven by price and/or quality"* against the retailers' own label. Even the defended
  category, premium pineapple, *"has also led to increased competition"*, as the FY2016 10-K warned of the Del Monte
  Gold variety the company introduced in 1996.
- **Eighteen filed years agree**: operating margin mean 3.1%, best 6.1%; return on average equity mean 4.6%, best 12.9%;
  sales +22% nominal in seventeen years with a bought-and-sold acquisition inside. Dole plc earns within about a point
  of DMC in the same years (2021-25 operating margin -0.1% to 3.3%) and says of the class: *"Excess supply often causes
  severe price competition in our businesses."*
- **The banana leg is narrowing**: gross margin 10.0% (2023), 5.9%, 4.8%, and 2.3% in Q2 2026. The pineapple and
  fresh-cut leg rose to 11.4% gross in 2025, the strongest counter-evidence, answered in the run as a variety lead
  that must be re-won inside a segment that still earns 11% before SG&A.
- **Beneath the close**: the long-term PSUs vest on EBITDA and the releases lead with Adjusted EBITDA ($300.2M against
  $137.4M of operating income in 2025); owner earnings across 3, 5, 10 and 18 years at both (c) ends run $65.9M to
  $135.2M (4.6% to 9.4% on the cap), and at the ~10% floor the filed record is worth roughly $14 to $29 a share before
  the new perimeter and its debt (computation only). Named death as a signature: #11 THE PASS-THROUGH, with the
  filer's own TR4 disclosure (Ecuador, September 2025) as exposure [E4-40].

### Priors refuted or confirmed
- Registrant by CIK: confirmed; the screen label "DEL MONTE CORP" is the current legal name of Fresh Del Monte.
- The deal: **refuted as a sale of DMC, confirmed as a purchase by DMC** (perimeter change, WS shape at smaller scale).
- `wc_note` (payables 61% of 2021 OCF): arithmetic right, inference wrong. 2021's total working capital was a **$31.8M
  use**; the payables line offset a $105.1M inventory build.
- `level_shift_oe` STEP UP 3.89x: found. Capex fell from $122-150M a year (2017-2020) to $48-64M (2022-2025), below
  D&A, and the 2021-22 inventory builds reversed in 2023. Normalise down.
- Four constructions over five years: rebuilt over four windows; the screen's $66-135M reproduces exactly.

### Tooling defects (reported, not patched)
- `deal_note()` named the amendment, not the APA 8-K of 2026-02-12 filed seven days before the latest 10-K: the
  `deal_filings()` blind spot recorded at WS the same morning. It also cannot say which side of the deal the registrant
  is on, which is the first question the note tells the reader to answer.
- `working_capital_flag()` fired against a total working-capital use; its text *"ONE LINE MADE THE CASH"* is wrong in
  that case. Second instance after CAH.
- `run.py` prices on the intraday quote rather than the prior close; immaterial here.
