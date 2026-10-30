
## UPDATE 2026-09-13 - AMZN: Q2 OUT, the cloud leg has cut its price in every filed year and carries the weight
`Test Runs/2026-09-13 Run - AMZN Amazon.md`. **Q1 IN, Q2 OUT, file closed; Q3 recorded (no disqualifier, gate case, capital-allocation flag on the 2022 repurchase,
soft [E2-49] fire); Q4 recorded (would read UNKNOWABLE on the level of owner earnings; THE ROUND TRIP proposed); Q5 headed COMPUTATION - NOT A CLEARANCE; Q6 recorded
with nothing armed.** Price **US$256.78** x **10,786,313,572 shares** = cap **US$2,769.7bn**; sovereign **USD 30-year 5.35%** (US Treasury, 09/11/2026, re-struck
unchanged at the resume). **The second of wave 5's eight "capex unresolved [E5-20]" names, resumed from disk after the first session died building the competitor
row.** **Register count at the fold, read from the register: 95 runs** (65 closed at Q2, 26 at Q5, 2 at Q4, 2 at Q1; AMZN adds one Q2 OUT).

### THE SKIP REASON, TESTED - NOT A CAPEX GAP IN THE FILING; A TAG DEFECT IN THE SCREEN, FIXED THE NEXT DAY
- **Reproduced, not inferred:** `Screens/floor_screen.py` at `a8bc84f` (2026-09-01 22:15, the commit that wrote the wave 5 table) returns `CAPEX_UNRESOLVED` for Amazon.
  Its `annual()` stopped at the first tag with any data; Amazon's `PaymentsToAcquirePropertyPlantAndEquipment` ends at FY2016 and its capex has lived under
  `PaymentsToAcquireProductiveAssets` since. The union fix `dff6ab6` landed at 2026-09-02 12:23 and the row was never re-triaged. The current screen prices Amazon and
  its capex end reproduces to the dollar (gross capex plus finance-lease additions: 5-yr -13,770, 3-yr 961).
- **So ABNB and AMZN were wrongly labelled for two different reasons**: ABNB had a real presentation gap and did not fit the exception; AMZN had no gap at all.
  **The six names left in the row should be put through the current `owner_earnings()` first** (a dated note is beside the wave 5 table).
- **The [E5-20] question, asked separately on the filing, answers yes for Amazon's plant**: the FY2025 10-K shortened a subset of server lives from six years to five
  *"due to the increased pace of technology development, particularly in the area of artificial intelligence and machine learning"*, a year after lengthening them.
  The D&A end is INVALID; (c) is judged upward from a renewal-at-scale CONVENTION (~1.21x P&E depreciation in 2025).

### THE BRIEF'S QUESTIONS, ANSWERED FROM THE FILED RECORD
- **What was unresolved:** nothing in the filing; the screen (above). `oe.py` was audited line by line against every filed cash-flow statement: all inputs matched but
  one unused build-to-suit figure (2021: 5,846 carried, 5,616 filed). "Cash basis" and "formation" are now defined in the run file.
- **Finance leases:** capital spending by another route; they enter (c). $58.3bn of property came in under capital/finance leases 2016-2021, nearly all equipment,
  with the principal repaid in financing.
- **SBC:** resolves in every year and is complete (the equity-statement line sits within 1.6% of the add-back; no stock-settled 401(k) or pension); 20.9% of OCF 2016-25.
- **Owner earnings, every window and both ends:** 5-yr 2021-25 **-$10.8bn to -$14.8bn on every capex construction; +$27.6bn at 1.3x depreciation**; TTM -$28.8bn to
  -$60.7bn against +$77.4bn; the window without 2021-22 does not rescue the capex ends (-$2.0bn to +$7.4bn). **The band changes the sign.**
- **Working-capital flag by eye:** fires 2017 (payables +38.7% of OCF), 2021 (-39.2%), 2022 (-46.8%). "Other assets" in OCF carries content and satellite-launch
  deposits, so no ex-working-capital figure was built.
- **The marks:** removed inside OCF (-$79.8bn non-operating, +$41.4bn deferred tax, TTM). Cash taxes 3.8% of pre-tax income TTM, explained by 100% bonus depreciation
  and the non-cash gains.
- **Three legs, from the text:** the framework's only segment rule is [E2-56] at Q3 (no instance found of a Q2 combining rule); the queue's practice (GHC, HAS, SONY)
  decides by where the profit and the capital are. AWS: 58% of operating income, 76% of H1 2026 net plant additions.

### WHY OUT AND NOT UNKNOWABLE
- **For IN, stated at full strength:** the largest cloud installed base at a 36.8% margin with $496bn of contracted revenue; the default Western shelf with paid units
  accelerating to +17%; $76bn of advertising growing faster than Google's; regulators alleging monopoly.
- **Against, and decisive:** AWS's own MD&A says sales were *"partially offset by pricing changes"* in every filed year 2013 to H1 2026; three filed rivals sell the same
  service, grow faster or earn more, and hold larger backlogs; Microsoft books $24.1bn a year from OpenAI, AWS's largest new committer; Oracle files that its multicloud
  services work with AWS; the server basis is replaced on five-year lives shortened for AI [E4-04]. The stores compete on *"selection, price, and convenience"*. The
  advertising leg files no price, volume or margin and does not carry the weight. **The documents that decide criterion 2 for the legs that carry the weight exist and
  were read.**

### REFUTED OR NARROWED PRIORS (the brief's four)
- **"The negative capex-only means say something about earning power": half right.** They do not show the business cannot earn (at a renewal-at-scale (c) the five-year
  mean is +$27.6bn); they do show owners have been paid nothing for five years on any construction that counts the plant bought. The split is the (c) judgment, and the
  filing does not separate maintenance from growth.
- **"Rising seller fees are [E2-44] evidence": refuted on the record.** No seller, fulfillment, referral or Prime fee change appears in any Amazon filing on disk; third-party
  seller services track paid units with the seller unit mix flat at 60-62%.
- **"AWS's lead in Table A is a moat": the premise was wrong.** AWS leads no Table A measure (second on margin, last of four on growth, fourth on backlog), and its
  own pricing sentence is the inverse of [E2-44](1).
- **"The laboratory stakes are separable from the operating business": refuted.** At least $200bn of the $252bn six-month backlog increase is from OpenAI and Anthropic,
  whose equity Amazon bought for $60bn in the same half-year and marks up at rounds its own cash joins; that is the proposed shape below.

### NEW FOR THE OPERATOR
- **A proposed survival shape, THE ROUND TRIP** (it would be the eighteenth): the business funds its largest customers, books their commitments as backlog, marks their
  equity up at rounds its own cash joins, and borrows to build the capacity they have committed to buy. Nearest are #1 CONTRACTED NOT TO STOP (Oracle supplies OpenAI but
  does not own it) and #8 THE EQUITY IS THE REVENUE (at Rigetti the subject's own shareholders pay). Amazon is also recorded as a later instance of #11 THE PASS-THROUGH
  (thirteen years of AWS price cuts). **Added to the index as proposed; no register changed.**
- **The three-leg competitor row is on disk** (`Test Runs/_research 2026-09-13 AMZN/peers/`: cloud, retail and marketplace, advertising, naming and multi-cloud sweeps, 9
  companies with accessions), for any later META, WMT, EBAY, SHOP, MELI or PDD run.

### TOOLING, SOURCE AND BRIEF DEFECTS FOUND
- **The wave 5 "capex unresolved" row was written by a screen with the single-tag defect** and not re-triaged after `dff6ab6`; at least one of its eight names (AMZN)
  was never unresolved.
- **The current screen's D&A end reads the broad cash-flow D&A line**, which for Amazon includes capitalised content and operating-lease amortisation ($65.8bn against
  $41.9bn of P&E depreciation in 2025), so its "_da" end is not the [E3-44] default for this filer.
- **The killed session's Table A pricing sweep searched only the peers**, and missed the subject's own decisive sentence.
- **Brief errors:** Walmart's 10-K and 10-Q were said not to be fetched and were already on disk from the WMT run; "AWS's lead in Table A"; "sellers pay rising fees".
- **Mine:** the committed Q2 section carries em dashes in my own prose, against the standing rule; left as committed history and not repeated from Q3 on.
