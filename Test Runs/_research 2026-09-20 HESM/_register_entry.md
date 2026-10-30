- **HESM (Hess Midstream LP), 2026-09-20 - FAIL at Q2 (OUT, ON THE BUSINESS).** Q1 IN.
  **WAVE 7, name 6. Register entry 138** (re-derived by counting the register itself with a
  line-start regex immediately before insertion: 137 entries stood above this one, and no earlier
  entry carried HESM). **Price US$40.16**, close of 2026-09-18, aggregator (Yahoo via
  `tools/sources.py`), flagged. **Shares 128,350,881 Class A shares**, from the **cover of the
  10-Q for the quarter ended 2026-06-30, accession `0001193125-26-338055`**, as of 2026-07-31.
  **TWO CLASSES, AND THEY ARE NOT SUMMED**: 77,827,485 Class B shares also stand, but Class B
  carries votes and no economic interest in the Company; the economics are the Class B *units*
  of Hess Midstream Operations LP, held by Chevron, and the market price buys the Class A share
  only. **Cap US$5,154.6M** (Class A only). **Sovereign 5.34%, 09/18/2026, US Treasury daily par
  yield curve, 30-year, struck fresh from the issuing authority with `sov_USD_treasury.csv`
  deleted first.**
  **Q2 OUT. [E3-03]'s three criteria are all MET on their face, and each one is held up by a
  single contract with the counterparty that owns the general partner.** Clause (3) passes and
  **PAGP's failure on it does not transfer** - it was tested, not inherited: *"Section 1(b) of
  the Natural Gas Act ('NGA') exempts natural gas gathering facilities from regulation by
  FERC"*, and *"the crude oil and NGL pipelines in our gathering system similarly are not
  subject to FERC jurisdiction under the Interstate Commerce Act."* Clause (2) passes in the
  registrant's own words, and note the order of its two reasons: *"As a result of our
  **contractual relationship with Chevron** under our commercial agreements **and** our direct
  connections to Chevron's production operations in the Williston Basin, we believe that we will
  not face significant competition."* Clause (1) passes with a number: *"For the year ended
  December 31, 2025, **97% of our revenues** were attributable to our fee-based commercial
  agreements with Chevron."*
  **The fee is an administered price the counterparty wrote, which is [E2-59] exactly.** Item 1:
  *"a fee recalculation mechanism … **in order to target a return on capital deployed**"*, and
  since 2023 *"the base rate for 2024 was set based on the average of the tariff rates from the
  years 2021 through 2023"*, escalated by a CPI index *"not … more than 3% in any calendar
  year"* and floored so that *"no fee will ever be reduced below the amount of the applicable fee
  payable by Chevron in the prior year."* Administered pricing floors a commodity business's
  profits but **the moat belongs to the regime** [E2-59], and here the regime is Chevron, which
  owns 37.7% of the Partnership, owns the general partner (8-K 2026-03-04: *"HIP GP is owned 100%
  by HINDL"*, HINDL being *"an indirect, wholly owned subsidiary of Chevron Corporation"*), and
  under Item 1A *"may compete with us and have no obligation to present business opportunities to
  us"* while the partnership agreement *"replaces our general partner's fiduciary duties to
  holders of the Company's shares with contractual standards."*
  **And the volume term is a depleting asset the registrant says it does not control** - Item 1A:
  *"our success depends, in part, on Chevron and other producers replacing declining
  production"*; volumes *"will naturally decline over time"*; *"**We have no control over** the
  level of drilling activity in our areas of operation."* That is [E4-04]'s excluded class
  (depleting assets) and [E3-51]'s surfing run: **the advantage lives in the wave, not the
  surfer.** The OUT is deliberately **not** the [E4-04] perimeter close - durability here *can*
  be judged from the filings, and they judge it.
  **PAGP'S CROSS-RUN NUMBER REPRODUCES, AND THE INFERENCE STILL FAILS.** PAGP's competitor table
  scored HESM first of eleven at 25.5%. Rebuilt independently here from HESM's own filings on the
  same metric (operating income / net PP&E + net intangibles + equity-method investments,
  FY2021-25 means): **25.56%**, first of twelve, **2.1x the peer median of 12.3%**. PAGP's other
  ten cells reproduced within 1.2 points. **But the return is the number the related-party
  contract was written to deliver**, which [E4-26] required be hunted rather than admired: the row
  this run added makes it plain - **Antero Midstream, the closest structural analogue in the list,
  a single-sponsor gathering-and-water business with dedicated acreage, earns 12.4% on the same
  metric over the same window.** The pipes are not twice as good. The contract is.
  **THE SHARPEST FINDING IS A SERIES NOBODY HAD RUN: four 10-K vintages of the three-year MVC
  table, side by side.** MVCs are 80% of Chevron's own nominations, set three years forward, and
  each 10-K prints three years. Gas gathering, third year of each vintage: **FY2021 up 11%
  (2024: 351), FY2023 up 8% (2026: 412), FY2024 flat (2027: 418), and FY2025 - the first
  development plan nominated by CHEVRON rather than Hess - DOWN 18% (2026: 419 / 2027: 422 /
  2028: 346).** Crude gathering 2028 down 21%, terminaling down 20%, processing down 17%, water
  down 6%. **No footnote explains it**, though the FY2024 10-K did footnote its own soft year for
  Tioga turnaround maintenance. Grossed back up, Chevron's 2028 plan nominates ~433 MMcf/d against
  ~528 for 2027. **And the actuals have already turned**: the Q2 2026 furnished release reports
  throughput *"decreased 15% for oil terminaling and 12% for water gathering … primarily due to
  lower production as a result of **lower new-well activity**"* [E4-55].
  **FOUR SCREEN CELLS REFUTED AT SOURCE.** (i) `deal_note` guessed the lone Item 1.01 was *"most
  likely a credit facility or offering"*; it is a **Unit Repurchase Agreement with Chevron's
  HINDL** (455,811 Class B units for ~$18M at $39.49) plus a **$42M accelerated share
  repurchase**, both funded *"with borrowings under its existing revolving credit facility."*
  **Second consecutive midstream name this note has misdirected.** The whole 8-K index since
  `newest_periodic` was read by hand: nothing material sits after 2026-06-30. (ii)
  `growth_required -0.0281` is **the PAGP look-through error again, at 1.61x instead of 4x**:
  consolidated owner earnings over a Class-A-only cap. Class A owns **62.25%** of the opco, and
  three filed statements agree (Item 1's *"62.3% controlling interest"*, the share counts, and the
  pre-tax income split). Corrected to one tier the yield is **7.85% to 8.76%**, not 12.81%. That
  arithmetic is headed **COMPUTATION - NOT A CLEARANCE** in the run file and Q5 never opened.
  (iii) The two level flags disagreed (`level_note` "no step" 1.56 vs `level_note_oe` "STEP UP -
  normalize down [E4-41]" 1.84); both describe a **contracted build-out ramp**, which is not an
  [E4-41] windfall, so the flag fires for the wrong reason - **but points the right way for a
  reason neither flag could see**: capex is guided at **$105M for 2026** against $247.5M actually
  spent in 2025, the expansion programme is complete, and the finished capacity is nominated 18%
  emptier in 2028. (iv) **The `PropertyPlantAndEquipmentNet` tag trap is NOT present** - HESM
  tags it continuously FY2018 to FY2025, so the PAA/PAGP defect is filer-specific, not
  industry-wide.
  **THE BRIEF'S OWN CLAIM THAT THE FILER SPLITS MAINTENANCE FROM EXPANSION CAPEX IS ALSO
  REFUTED.** Neither the FY2025 10-K nor either furnished release splits them; the 10-K gives one
  line, *"Total capital expenditures $247.5"*, and the words *"maintenance capital"* and
  *"expansion capital"* appear nowhere in the Q2 2026 release. Had Q4 opened, (c) would have been
  a **disclosed guess** [E2-23, E3-44] with no filer split to lean on.
  **BENEATH THE CLOSE, SEEN AND NOT SCORED** (the standing [E4-29] instruction from the CGNX run
  was performed before the gate closed, as PAGP did): **Adjusted EBITDA 21 times and Adjusted
  Free Cash Flow 16 times in the Q2 2026 EX-99.1, 27 times in the FY2025 one**, both leading the
  highlights, with Adjusted Free Cash Flow defined to deduct capital expenditure but not
  depreciation - [E5-41]'s reverse float in its purest form; **nine lines of numeric full-year
  guidance** issued 2025-12-09 and twice reaffirmed, plus an *"approximately $1 billion of
  Adjusted Free Cash Flow after Distributions through 2028"* target [E4-22]; **$1,015.7M returned
  to holders in 2025** ($400.0M repurchases, $350.2M distributions, $265.5M to the noncontrolling
  interest) against $983.8M of operating cash and $255.6M of capex, with long-term debt up
  $290.1M over the same year [E2-60]; and **cash and cash equivalents of $1.9 million** at
  2025-12-31 against $3,800.5M of total debt [E5-11, E5-39].
  **NO PRICE ALERT AND NO PORTFOLIO ROW** - the name failed on the BUSINESS, and a band would be
  the QLYS category error. **Reversal condition, in words:** HESM would have to stop being a
  contractual claim on one counterparty's depleting basin. Concretely, that means third-party
  revenue growing from ~4% of the total to a majority of it under contracts HESM negotiated at
  arm's length with parties that do not own its general partner, or the general partner passing
  to an owner with fiduciary duties to the Class A holders, **and** a development-plan vintage in
  which the third year stops falling. Price does not enter it.
  Filing read: **10-K FY2025, accession `0001193125-26-071592`, filed 2026-02-25**; newest
  periodic **10-Q 2026-06-30, `0001193125-26-338055`**; furnished releases
  `0001193125-26-329567` (Q2 2026) and `0001193125-26-032732` (FY2025); 8-K
  `0001193125-26-091542` (Items 1.01/7.01/8.01/9.01). Three figures cross-checked against the
  filed statements: operating cash 983.8, depreciation 214.1, long-term debt 3,739.5.
  `check_framework.py` **PASS**, 0 phantom cites across 1,058 test-run files; **ledger counted at
  311 rows**, not the stale KEY FILES pointer's 267.
