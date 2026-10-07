## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN → **Q2 OUT, the file closed**; Q3-Q6
  recorded beneath explicit RECORDED, NOT GOVERNING banners, as at EQIX and TOST.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the
  filed income statement, supplement and property note. The stale peers and unfiled private builders
  at Q2 are named and are not what closes the gate.
- [x] No UNRESEARCHED verdict was returned. One open document is named inside a recorded section (the
  officers' carry allocation for the June 2026 promote: Q3 2026 10-Q, 2027 proxy); it governs nothing.
- [x] No UNKNOWABLE verdict was returned.
- [x] Step 0: the filing was read with accession numbers; three figures on the face of the FY2025
  cash-flow statement cross-checked to companyfacts, and a fourth (stock compensation) found to be in
  no published element, which is the Q4 finding; one peer figure (CyrusOne FY2021) checked to its filed
  text.
- [x] Owner earnings on multi-year windows (five-year default, three-year, ten-year display, FY2025,
  TTM), hand-built from the filed cash-flow statements; (c) disclosed as a judgment with the company's
  figure displayed and rejected; the perimeter refusal stated because every window crosses a merger,
  a deconsolidation or a stake sale.
- [x] Competitor row rebuilt for DLR's products from filings (nine examined, four current filers),
  not imported from the EQIX run; the EQIX row's DLR figure corrected on the fairer denominator.
- [x] Sovereign for the reporting currency (USD), from the issuing authority, dated 09/17/2026,
  re-struck by this run; the 48.2% non-US revenue named.
- [x] Value stated as a round-number range under a COMPUTATION — NOT A CLEARANCE heading.
- [x] One bar (the screamer test); windage count one.
- [x] Price dated as a close, aggregator flagged, corroborated by a Form 4 inside the day's range.
- [x] Run committed to git after every gate, with a pathspec.
- [x] Every ledger id cited was looked up in `principle_ledger.csv` (`led.py`) before it was written.
- [x] No em dashes in anything this run wrote (the template's own headings and the required
  `COMPUTATION — NOT A CLEARANCE` heading carry them).
- [x] Never presented as proven to beat the market; nothing here claims it.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **Q3, corrected before the next gate (commit `64030e7`)**: the first committed wording said
   employees *"including the executives who negotiated the purchase"* are entitled to cash from the
   June 2026 promote. No document read says who negotiated, or that the named officers' carry vehicle
   covers those joint ventures; the sentence now states the officers' carry percentages and names the
   allocation as open.
2. **Q4, corrected before Q5 (commit `f77e9b3`)**: a parenthesis said the development table's cost
   definition *"widened in the Q4 2024 supplement"* to include acquisition and infrastructure cost. The
   Q4 2021 supplement's footnote already includes them; the note now says the layout changed and the
   later tables include joint-venture projects.
3. **Drafts corrected before commit, recorded because they were mine**: a Q2 draft said the backlog
   *"doubled"* ($817M to $1.4bn is +71%, and part of it was bought with the Blackstone stakes); a Q2
   draft asserted that other builders' development tables show similar yields (none was read; the
   sentence was removed); a Q3 draft said every stock deal was paid in shares quoted at $150-190,
   which no filing read supports for the 2017 and 2020 mergers (replaced with the 2026 deal prices
   derived from the 8-Ks); a Q4 draft gave
   SBC as 4.8% of operating cash over FY2021-25 (it is 4.4%).
4. **A placeholder preferred balance for FY2015 in `q3calc.py`** (`prefv`) was not from a filing; the
   FY2016 return-on-equity figure that used it is not reported anywhere in the run.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **The five kinds of capex gap it offered did not include what DLR has.** The brief asked which of
   *"tag change, tag overlap with different values, history hole, presentation change, or none"* the
   label was. It was none of them: the capex line sits under `PaymentsToDevelopRealEstateAssets` in
   **every** year FY2009-25, an element no `CAPX_TAGS` member reaches, so the triage's label was simply
   right; **and the current screen stops one step earlier, on `SBC_UNRESOLVED`**, because DLR's stock
   compensation is in no element companyfacts publishes. The brief pointed at the EQIX real-estate
   line; the real-estate line here IS the capex line.
2. **The perimeter list stopped at 2022.** The brief named Interxion (2020, confirmed: closing 8-K
   `0001193125-20-072868`) and Teraco (2022, confirmed: *"On August 1, 2022, we completed our acquisition
   of a majority interest in Teraco"*). It did not name DuPont Fabros (2017, stock), the 2019 and 2021
   deconsolidations, or **the largest perimeter change in the record, which sits after the last full
   year**: the June 2026 Blackstone buy-in ($3.5bn for 64% of two joint ventures, $5.2bn of assets
   capitalised, 12.3M shares), with the Teraco put (3.43M shares), Columbia Capital (a fund manager,
   2.34M shares plus an earn-out) and the Astra land ($482M) in the same quarter.
3. **The prior about the EQIX row was wrong in its number, and the brief's figure carried the error.**
   The brief quoted DLR's return on plant as *"6.9-7.4%"*. That row's denominator included about $5bn
   of construction in progress and land held; on operating real estate, ex-impairment, the figure is
   **8.7-8.9%** (FY2023-25). The brief was right that the row should not be imported, and the corrected
   figure still sits in the large-product cluster, so the conclusion survives the correction.
4. **The brief did not anticipate the promote.** Its Q3 prompts were the 8-K earnings releases and
   [E4-29]/[E4-22]; the sharpest Q3 fact is a $201M promote booked as revenue on the company's own
   purchase price, with a carried-interest plan for employees adopted ten months earlier. Recorded at
   Q3, not governing.
5. **The REIT routing note** pointed at a sector method that does not exist; the brief said so and was
   right. Recorded at Step 0.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`tools/sources.price()` returns an intraday `regularMarketPrice` stamped with today's date** while
  its docstring says *"Latest close."* Third name (TOST, EQIX, DLR).
- **`floor_screen.CAPX_TAGS` does not reach `PaymentsToDevelopRealEstateAssets`**, where DLR files its
  whole capex line every year FY2009-25 (and where other REITs may). Adding it would change a number,
  so it is a proposal for the operator, not a fix made here; with it, the EQIX proposal
  (`PaymentsToAcquireRealEstate`) would cover the two data-centre REITs' two capital lines.
- **SBC in a non-published element**: DLR's *"Amortization of share-based compensation"* is in no
  element companyfacts carries. `SBC_UNRESOLVED` is the right answer; no tag rule recovers it (the
  resume note's source-limit class).
- **`ACQ_TAGS` misses DLR's FY2021-24 acquisitions** (the screen series has FY2020 and FY2025 only)
  and reads $309.0M for FY2025 against $321.2M on the face.
- **A same-element denominator for REIT peers exists**: `RealEstateGrossAtCarryingValue` (Schedule
  III gross) resolves for DLR, EQIX, CyrusOne, QTS, CoreSite and DuPont Fabros, and equals DLR's
  operating real estate at cost excluding construction in progress. It gives a row without per-filer
  hand definitions (`rowcalc.py`).
- `Screens/cover_shares.py DLR` matched the 10-Q cover exactly.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**Read the price series of the product, through a cycle, before reading the latest spread.** DLR's
2026 renewal spreads (+48.7% cash on large leases) are the strongest fact for a franchise in the file;
the same filer's 2021-22 roll-downs (-11.9%, -3.3%), and a competitor's same-year sentence, turn them
into [E2-58]'s supply cycle. Every REIT and every capacity business files renewal or rate tables; the
series, not the quarter, is the moat evidence.

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** DLR FAILS AT Q2 (OUT, on [E3-03]'s demonstration clause and [E3-46]: rebuilt for DLR's
  own products, return on operating plant 8.2-8.9% (FY2023-25), the large-product cluster's return and
  drifting down from 9.3-10.6%; large-product cash renewals -11.9% (2021) to +48.7% (H1 2026), the
  supply cycle [E2-58]; per-share operating earnings +0.8% a year for ten years with shares +150%;
  [E2-44](2) fails on capex of 35-64% of revenue; [E4-04] engaged in the company's own words). Q1 IN;
  Q3 IN on the binary (recorded; [E4-29] in the pay, serial issuance, dividends matched by issuance,
  a $201M promote booked on the company's own purchase); Q4 IN on survival (recorded; a real tag gap
  behind `SBC_UNRESOLVED`; [E5-20] exception class applies on capital intensity; five-year owner
  earnings about zero to $0.55bn, central about $0.34bn; staying power 1 of 3); price $184.26 x
  370,036,176 = $68.2bn, headed COMPUTATION — NOT A CLEARANCE: 0.5-0.8% business yield against a
  5.29% sovereign; Q6 arms nothing.
- Work order: none. UNKNOWABLE: none.
