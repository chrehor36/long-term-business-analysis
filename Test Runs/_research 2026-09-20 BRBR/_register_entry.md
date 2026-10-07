- **BRBR (BellRing Brands, Inc.), 2026-09-20 - FAIL at Q2 (OUT, ON THE BUSINESS).**
  Q1 IN. **WAVE 7, name 9. Register entry 141** (re-derived by counting the register itself with
  a line-start regex inside the slice from this file's `## COMPLETED FROM THE QUEUE` heading to
  `## THE WRITE-EARLY PROTOCOL`: **140 entries stood above this one**. The line-start anchor
  matters: a plain `str.index` on the heading text lands inside the MCFT entry above, which
  quotes both headings in its own prose, and returns 16). **Price US$8.98**, close of 2026-09-18,
  aggregator (Yahoo Finance chart endpoint), flagged, raw response on disk at
  `_research 2026-09-20 BRBR/quote_BRBR_raw.json`. **Shares 116,278,194**, from the **cover of
  the 10-Q for the quarter ended 2026-06-30, accession `0001772016-26-000022`, filed 2026-08-04**,
  as of 2026-07-28. **One class only** (Section 12(b) registers Common Stock, $0.01 par, alone;
  Section 12(g) states *"None"*; the Old BellRing dual-class structure was eliminated at the
  Spin-off). No splits, ever. **Cap re-struck by hand: US$1,044M**, against the screen row's
  $1,243M, which is the same number a few weeks stale. **Sovereign 5.34%, 09/18/2026, US Treasury
  daily par yield curve, 30-year, from the issuing authority, struck fresh in this run with
  `tools/sources.py`.**
  **FOUR STEP-0 FLAGS RESOLVED BEFORE Q1 OPENED, THREE OF THEM AGAINST THE SCREEN.**
  (i) `cap_flag` "cap $1,243M against a filed float of $9,368M (7.54x) as of 2025-03-31":
  **NEITHER NUMBER IS WRONG AND THE GAP IS AN 88% PRICE COLLAPSE.** The FY2025 10-K cover says
  the float *"as of March 31, 2025 , the last business day of the registrant's most recently
  completed second fiscal quarter, was $ 9,367,938,437 "*; BRBR closed at **$74.46 that day** and
  **$8.98 on 2026-09-18**. This is the **CALM/EMBC branch** of the flag, not the MCFT 1000x
  branch: the cap is right and the comparison was seventeen months out of date. The register now
  carries a third reading of this flag, the stale-float one.
  (ii) `wc_note` "AccountsPayableAndAccruedLiabilities moved 49% of 2022 OCF": **the arithmetic
  is exact (10.3 / 21.0 = 49.05%) and the sign is right, but the flag named the THIRD-largest
  line and its premise is inverted.** Inventories moved **(83.9)**, 399.5% of FY2022 operating
  cash, and receivables **(70.7)**, 336.7%, and **both consumed cash**. FY2022 OCF of $21.0M is
  depressed by a $154.6M working-capital build, not flattered by a payables stretch. **Third run
  in a row (EMBC, MCFT, BRBR) in which this flag names a line that is not the largest mover.**
  (iii) `spread_caveat` "4-construction width only": **eight fiscal years of operating cash exist,
  FY2018 through FY2025**, from seven consecutive 10-Ks under one CIK, the FY2020 10-K reaching
  back to FY2018 on its third comparative column. Window rebuilt over all eight.
  (iv) **THE PERIMETER, which the screen did not flag and whose empty `name_change_note` and
  `deal_note` are both false claims.** Old BellRing (now BellRing Intermediate Holdings, Inc.)
  IPO'd 39.4m Class A shares on **2019-10-21**; the Spin-off completed **2022-03-10**, Post
  contributing its Class B share, all its BellRing LLC units and *"$ 550.4 of cash"* for
  *"$ 840.0 in aggregate principal amount of BellRing's 7.00% Senior Notes"* plus equity, and
  distributing *"78.1 million, or 80.1 %, of its shares"*. **The filer today is the SUCCESSOR
  ISSUER under Rule 12g-3(a)**, which is why CIK 0001772016 and file number 001-39093 carry
  across and why EDGAR `formerNames` is empty: **the screen's name-change detector cannot see a
  Rule 12g-3(a) substitution.** The operating perimeter is continuous (same brands, same LLC),
  but before 2022-03-10 Post owned **71.5%** of the economics: FY2022 *"Net earnings including
  redeemable noncontrolling interest $ 116.0"* against *"Net earnings available to common
  stockholders"* of **$82.3**. **The consolidated cash series is a series; the bottom line is
  not**, so the run cut every per-share and net-earnings reading at 2022-03-10 and carried the
  OCF series whole.
  **Q1 IN.** A brand and nothing else. *"We primarily engage third-party contract manufacturers
  … for an agreed-upon tolling charge for each item produced."* Capex guided at **$10 million on
  $2.3 billion of sales** because the plants belong to somebody else; the one owned plant makes
  bars in Voerde, Germany. Shakes are **80.5%** of nine-month net sales. Simple and stable in
  character **[E3-31]**.
  **Q2 OUT, on [E3-03] criterion (2), from the subject's own filed numbers.** In the nine months
  to 2026-06-30 Premier Protein RTD shake net sales *"increased 0.5%, driven by 5.2% increase in
  volume and 4.7% decrease in price/mix"* — **the flagship gave back price into the worst input
  year in its record while its volume rose** — and consolidated gross margin fell from **34.9% to
  28.5%, 647 basis points**, on +2.28% sales. The 10-K says what it is in: *"highly competitive
  and highly sensitive to both pricing and promotion"*, competing on *"shelf space, price,
  promotional activities"*, against *"private label and store brand products"*. **74.0% of FY2025
  net sales went to Walmart, Costco and Amazon**; the majority of milk-based protein comes from
  *"one supplier"*, **46.3%** of shake supply from one contract manufacturer with **28.0%** from
  a single facility, and the 11-ounce bottle from *"only one supplier"*. **Administered cost on
  one side and administered price on the other, and no door on either [E2-58, E2-59].** The
  dominance test **[E2-53]** is disproved in one line: the self-described *"clear leader in
  ready-to-drink shakes"* lost **680bp** of gross margin in a quarter in which its own
  consumption grew **6.0%**. **[E4-36]/[E3-51]: wave-riding, and the filings prove it rather
  than assert it, because the wave has not stopped and the economics collapsed anyway.**
  **THE SMPL PRIOR (entry 135) IS CONFIRMED ON ITS ARITHMETIC AND NARROWED ON ITS INFERENCE.**
  647bp on +2.28%, exactly as SMPL recorded it from outside. But a **seven-name competitor row**,
  matched at the calendar quarter ended 2026-06-30 and computed from each filer's own statements,
  finds two filers SMPL did not have, and both refute *"category fact"*: **Post Holdings**, whose
  fiscal calendar is identical and whose nine months to 2026-06-30 are the same window, took
  gross margin **UP 17bp** (29.6% against 29.4%), and **Abbott's Nutritional Products segment**,
  which sells Ensure into the same aisle, lost only **130bp** (46.5% against 47.8%). **Both own
  their plants.** The two that own none, BRBR and SMPL, lost 647bp and 470bp. The row, worst
  first: **BRBR -680bp · SMPL -390bp · CELH -340bp · MED -270bp · ABT Nutrition -130bp · POST
  -100bp · HLF -30bp.** **The pass-through failure is a fact about who owns the conversion step,
  not about the category** — and inside BellRing it is narrower still: **Dymatize took +20.7%
  price/mix in the June quarter and grew 26.7%** while Premier Protein RTD cut price, so it
  tracks **channel concentration**. That is the correction the SMPL fold is owed, and it
  strengthens rather than weakens SMPL's own Q2 OUT.
  **Q3, Q4, Q5 and Q6 NOT OPENED**, with the material gathered before the close recorded under
  **BENEATH THE CLOSE [E4-29]** and marked SEEN AND NOT SCORED. Recorded there and scored
  nowhere: the FY2026 guidance track from four of the company's own 8-K EX-99.1 releases,
  **Adjusted EBITDA midpoint $440M (2025-11-18) → $432.5M → $325M → $285M (2026-08-04), a 35%
  cut in nine months**, beside a *"long-term financial algorithm"* of *"18% to 20%"* published
  on the first of those dates; **Adjusted EBITDA is 75% of the annual bonus** (DEF 14A
  2025-12-16) and the guidance is given *"only on a non-GAAP basis"* with no reconciliation;
  roughly **$645 million of buybacks at average prices of $52.62, $34.01 and $27.41** against
  today's $8.98, with **$506.9M of authorisation left** and the revolver drawn from $250.0M to
  $300.0M in the same nine months in which operating cash was $65.0M; **Total Stockholders'
  Deficit of $(467.2)M**, which makes **[E2-01]**'s denominator negative; owner earnings on the
  framework convention spanning **$119M (8-year, D&A end) to $203M (3-year, capex end)**, which
  brackets the screen's $139M-$203M and pulls its floor down, headed **COMPUTATION - NOT A
  CLEARANCE**; and **$1,140.0M of debt** ($840.0M of 7.00% notes due March 2030 plus $300.0M
  revolver) against a **$1,044M** market capitalisation, with nothing due inside three years.
  **No price alert is armed and no PORTFOLIO row is created (the QLYS ruling).** The reversal
  condition is written in words in the run file: four consecutive quarters of **positive** Premier
  Protein RTD price/mix with gross margin back above roughly 33%, **and** the three-customer share
  materially below 74%, **and** filed evidence that the conversion step has moved inside the
  company. **Margin recovery on falling whey prices alone is not the trigger, because that is the
  cycle and not the position [E3-30].**
  Run file: `Test Runs/2026-09-20 Run - BRBR BellRing Brands.md`. Research:
  `Test Runs/_research 2026-09-20 BRBR/`.
