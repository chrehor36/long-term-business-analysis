## Q3 to Q6: NOT SCORED. The file closed at Q2, OUT on the business.

⛔ Q3, Q4, Q5 and Q6 are not scored; no verdict below. What was read is recorded so a later reader does not have to
refetch it. Nothing here promotes or rescues the file **[E2-37, E2-38, E3-39]**.

---
## THE SCREEN ROW, ANSWERED

| Field | Screen | Finding |
|---|---|---|
| `deal_note` | blank | **CONFIRMED** (Step 0): four 8-Ks since the 10-K, a board appointment, two results releases and a vote; no merger, tender or going-private form |
| `cap_m` | 13,062 | **STALE**: implies about $199 a share on today's count; at the 2026-09-25 close, $159.75 x 65,640,926 = **$10,486M** |
| `oe_bottom_m` | 258 | **REPRODUCES** as the five-year window at the capex end, **$257.8M** (below) |
| `oe_top_m` | 461 | **REPRODUCES** as `tools/run.py`'s three-year window at the D&A end with acquired-intangible amortization left inside (c), $461M; on depreciation excluding that amortization the three-year top is $464.4M and the five-year $407.7M |
| `spread` | 0.786 | reproduces as 461 / 258 − 1, a width across two windows (a three-year top over a five-year bottom); the spread inside the five-year window is 58% |
| `yield_bottom`, `vs_sovereign` | 1.97%, −3.38% | struck on the stale cap and an older 5.35%; today the five-year bottom is **2.46%** against **5.49%** |
| `growth_required` | 8.03% | reproduces as ~10% less 1.97%; a derivative of the two fields above |
| `level_shift` 1.84, `level_shift_oe` 1.86, `level_shift_full` 2.66, "STEP UP - normalize down [E4-41]" | | **CONFIRMED as a step up, REFUTED as a windfall**: the rolling five-year mean rose from $54M (to FY2013) to $258M (to FY2025) at the capex end, and the filings attribute it to store weeks and AUV (units roughly doubled; AUV $4.8M in FY2016 to $8.7M in FY2025), which is growth, not luck. The one favourable break **[E4-41]** names is inside the window: FY2024 had a 53rd week (*"lapping the benefit of the additional week which added $114.7 million in revenue in 2024"*) |
| `best_year_dep` 0.073, "no single-year dependence (9-yr OCF series)" | | **CONFIRMED in effect, REFUTED on the series length**: no single year carries any window (the largest, FY2024, is 27% of the five-year capex-end sum), but the filed operating-cash series is **seventeen** years, FY2009-FY2025; FY2009-FY2014 sit under `NetCashProvidedByUsedInOperatingActivitiesContinuingOperations`, which the screen's series did not reach |
| `years_filed` | 17 | reproduces as FY2009-FY2025 |
| `spread_caveat` | "4-construction width only [...] rebuild it" | answered: every trailing window 1-17 years, every rolling five-year window and the TTM, both (c) ends, below |
| `newest_filing`, `newest_periodic` | 2025-12-30, 2026-06-30 | reproduce |

---
## COMPUTATION — NOT A CLEARANCE

*Operator rule 3. Arithmetic beneath a closed file. It carries no entry language, no value range and no ranking.*

**Construction** (`oe.py`, output `oe_out.txt`): operating cash as filed (FY2015-FY2025 `NetCashProvidedByUsedInOperatingActivities`,
FY2009-FY2014 `NetCashProvidedByUsedInOperatingActivitiesContinuingOperations`, the latest filing's figure; FY2023-FY2025 checked against
the FY2025 10-K statement), less stock compensation in full **[E5-06]** (the cash-flow add-back *"Share-based compensation expense"*,
resolving in every year FY2009-FY2025, $7.5M to $47.8M, 6.1% to 12.8% of operating cash; the plans are service- and performance-based
restricted stock units and all run through that line), less (c) at two ends: **depreciation excluding the amortization of acquired
intangibles** (reacquired franchise rights, $6.5M in FY2025; untagged for FY2009-FY2010 and taken as zero there, flagged) and **total
capital expenditures**. No net-income proxy (operator rule 5). $M.

| FY | Operating cash | SBC | Depreciation | Capex | Franchise acquisitions (outside (c)) | OE, capex end | OE, depreciation end |
|---|---|---|---|---|---|---|---|
| 2009 | 115.1 | 7.5 | 41.8 | 45.5 | 0 | 62.1 | 65.8 |
| 2010 | 120.1 | 7.7 | 41.3 | 45.1 | 0 | 67.3 | 71.1 |
| 2011 | 136.4 | 10.5 | 41.6 | 79.7 | 0 | 46.2 | 84.3 |
| 2012 | 148.0 | 13.2 | 45.6 | 87.0 | 4.3 | 47.8 | 89.2 |
| 2013 | 173.8 | 14.7 | 50.0 | 111.5 | 0 | 47.6 | 109.1 |
| 2014 | 191.7 | 14.9 | 57.5 | 125.4 | 0 | 51.4 | 119.3 |
| 2015 | 227.9 | 22.8 | 68.3 | 173.5 | 0 | 31.6 | 136.8 |
| 2016 | 257.1 | 26.1 | 81.8 | 164.7 | 0 | 66.3 | 149.2 |
| 2017 | 286.4 | 26.9 | 92.6 | 161.6 | 16.5 | 97.9 | 166.9 |
| 2018 | 352.9 | 34.0 | 100.5 | 156.0 | 2.2 | 162.9 | 218.4 |
| 2019 | 374.3 | 35.5 | 114.8 | 214.3 | 1.5 | 124.5 | 224.0 |
| 2020 | 230.4 | 29.4 | 117.3 | 154.4 | 10.6 | 46.6 | 83.7 |
| 2021 | 468.8 | 38.1 | 126.0 | 200.7 | 0 | 230.0 | 304.7 |
| 2022 | 511.7 | 36.7 | 134.4 | 246.1 | 33.1 | 228.9 | 340.6 |
| 2023 | 565.0 | 34.2 | 150.2 | 347.0 | 39.2 | 183.7 | 380.6 |
| 2024 | 753.6 | 47.1 | 176.0 | 354.3 | 0 | 352.2 | 530.6 |
| 2025 | 730.1 | 47.8 | 200.2 | 388.0 | 107.5 | 294.3 | 482.1 |

**Every trailing window ending FY2025, against the cap of $10,486M:** one year **$294.3-482.1M (2.81-4.60%)**; two $323.3-506.4M
(3.08-4.83%); three $276.8-464.4M (2.64-4.43%); four $264.8-433.5M (2.53-4.13%); **five (the corpus default [E2-42]) $257.8-407.7M,
2.46-3.89%**; six $222.6-353.7M (2.12-3.37%); seven $208.6-335.2M (1.99-3.20%); eight $202.9-320.6M (1.93-3.06%); nine $191.2-303.5M
(1.82-2.89%); ten $178.7-288.1M (1.70-2.75%); eleven to sixteen from $165.4-274.3M (1.58-2.62%) down to $130.0-218.2M (1.24-2.08%);
**seventeen $126.0-209.2M (1.20-2.00%)**. **Rolling five-year windows** (capex end / depreciation end): to FY2013 $54.2M/$83.9M, FY2014
$52.1M/$94.6M, FY2015 $45.0M/$107.8M, FY2016 $49.0M/$120.7M, FY2017 $59.0M/$136.3M, FY2018 $82.0M/$158.1M, FY2019 $96.6M/$179.1M, FY2020
$99.6M/$168.4M, FY2021 $132.4M/$199.5M, FY2022 $158.6M/$234.3M, FY2023 $162.7M/$266.7M, FY2024 $208.3M/$328.0M, FY2025 $257.8M/$407.7M.
**TTM to 2026-06-30** (FY2025 less the 26 weeks to 2025-07-01 plus the 26 weeks to 2026-06-30, from the 10-Q's cash-flow statement):
operating cash $803.3M, SBC $51.4M, capex $396.9M, D&A $222.3M, depreciation about $215.8M (the half-year intangible amortization is not
tagged in the 10-Q; FY2025's $6.5M used, flagged): **$355.0-536.1M, 3.39-5.11%**.

- **Every window sits below the 5.49% bond at both ends, and no window reaches the ~10% the corpus quits on [E4-28].** Owner earnings
  were positive in every one of the seventeen years at both ends; the bottom never approaches zero.
- **(c) is a disclosed guess [E2-09] [E3-44], and here the filing says where it sits.** Capex ran 1.1x to 2.5x depreciation because the
  company is building restaurants. The FY2025 10-K splits it (table cells as extracted): *"New company restaurants | $ | 180,783"*,
  refurbishment or expansion $135,817K, relocation $43,626K, the Support Center $27,770K (its $22.8M purchase, one-time); FY2024 $198,367K,
  $122,905K, $25,633K, $7,436K. The spend on existing restaurants (refurbishment, expansion and relocation) was **$179.4M in FY2025 and
  $148.5M in FY2024, against depreciation of $200.2M and $176.0M**: [E3-44]'s default holds for this filer, and maintenance sits near the
  depreciation end, some of the "expansion" being seats added to full restaurants, which is growth.
- **Capital spent outside (c), recorded:** franchise restaurants bought back from franchisees, $179.8M over FY2021-2025 ($107.5M in FY2025,
  $71.8M more in the 26 weeks to 2026-06-30). With them counted as capital the owner spent, the five-year capex-end figure is $221.9M (2.12%).
- **Working capital is a source, not a use** ([E2-23]'s increment is not required here): customers prepay $448.7M of gift cards and the
  company runs negative working capital, as its MD&A says.

---
## BENEATH THE CLOSE: Q3 MATERIAL, RECORDED WITHOUT A VERDICT

- **Weight case, not declared as a verdict:** daily execution is the live determinant **[E3-38]** (a value operator kept at the front by
  its managers, [E3-43]'s *"a business, unlike a franchise, can be killed by poor management"*); no leverage; no control.
- **What pay vests on [E4-27]** (DEF 14A filed 2026-04-10, accession 0001104659-26-041771): the 2025 cash bonus, *"50% of the target incentive bonus was based on whether the Company achieves an annual EPS growth target of 10% (the “ EPS Performance Goal ”) and the remaining 50% was based on a profit sharing pool (the “ Profit Sharing Pool ”) comprised of 1.75% of the Company’s pre-tax profits"* (spacing inside the quoted labels as extracted); the 2025 performance units the same, with EPS growth targets of *"10%"*, *"21%"* and
  *"33%"* over one, two and three years against FY2024. **EPS growth is the metric [E2-01] defines itself against** (*"and not the
  achievement of consistent gains in earnings per share"*), and buybacks move it; recorded as a prompt, not scored. No return-on-capital
  measure in pay. Restaurant managing partners are paid a share of their restaurant's pre-tax income, which is a return on a fixed box.
- **[E4-29]:** "EBITDA" does not appear in the FY2025 10-K, the 10-Q or the Q2 2026 release; the release's non-GAAP measure is restaurant
  margin, reconciled to income from operations with the filer's own caveat that it *"is not indicative of overall company performance"*.
  The proxy uses an EBITDA multiple once, to price the purchase of franchise restaurants in which the CEO held 2% (below). Prompt, not
  fired.
- **Related party:** on 2025-12-31 the company bought five Southern California franchise restaurants, two of which the CEO owned 2% of;
  *"Mr. Morgan received $518,400 in total for his ownership interest"*, and the proxy states he *"was not involved in the overall
  negotiation"*. The franchise agreements carry *"pre-determined formulas"* for such purchases. Recorded.
- **Capital allocation, recorded:** buybacks of $150.0M in FY2025 for 869,007 shares (about $172.6 average), $70.8M for 415,133 shares
  in the 26 weeks to 2026-06-30 (about $170.5), against $913.3M for 22.8M shares at $40.01 average from 2008 to 2025; dividends $180.3M in
  FY2025, $0.75 a quarter declared for 2026; $50.0M drawn on the revolver at 2026-06-30 in the same half-year as $70.8M of buybacks and
  $98.7M of dividends. [E5-08]'s second condition would need an intrinsic value this file does not compute; not scored.
- **[E2-01]:** net income attributable $405.6M in FY2025 on average equity of about $1,410M, about 29%, with no funded debt at year end.

## BENEATH THE CLOSE: Q4 MATERIAL, RECORDED WITHOUT A VERDICT

- **Staying power [E5-11]:** no borrowings at FY2025 and $50.0M at 2026-06-30 against a $450.0M unsecured revolver to 2030-04-24; cash
  $134.7M at FY2025; operating-lease right-of-use assets $879.5M (556 of 714 company restaurants on leased land; *"158 of the 714 company
  restaurants have been developed on land which we own"*); gift-card deferred revenue $448.7M, a customer-funded, covenant-free liability.
- **Concentration:** beef is *"Approximately half of our food and beverage costs"*, bought *"primarily from four beef suppliers"* that
  *"represent a significant portion of the total beef marketplace"*; 101 company restaurants in Texas and 50 in Florida.
- **Great, good or gruesome [E4-20]:** not scored. Each new box costs about $8.3M and the return on operating assets has held 23-43%, the
  shape of [E4-43]'s good class; recorded, not a verdict.
- **Survival shape, as a signature WITHOUT a verdict (Q4 was never opened):** **#11 THE PASS-THROUGH** (the company survives and grows,
  and the gain of its execution is passed to the guest as a real check that falls, while beef, sold by four packers, sets the cost; the
  owner's margin has not moved in seventeen years). No new shape.

---
## TOOLING, REPORTED NOT PATCHED (operator rule 8; a tool may never add a number)

- **`tools/run.py TXRH`** (output `runpy_out.txt`) builds "D&A" from `DepreciationDepletionAndAmortization`, which **includes the
  amortization of reacquired franchise rights** ($6.5M in FY2025, $2.2M in FY2024, $3.0M in FY2023), so its depreciation end counts an
  acquisition's amortization as maintenance capital; its three-year top of $461M reads $464.4M on depreciation alone. **The fourth form of
  the acquired-amortization defect already on record.** It defaults to a **three-year** window and prints the corpus's five-year window as
  "THE OTHER WINDOW"; its *"3. POINTS OVER THE SOVEREIGN -0.22 .. +1.61"* rests on the unprinted growth assumption in `points_over()`, and
  its *"2. GROWTH THE PRICE ASSUMES 4.7% (at a 5.49% rate)"* is struck against the bond, not the ~10% floor [E4-28]; reported, not used.
- **The screen's operating-cash series stops at FY2015** for this filer (its own note says *"9-yr OCF series"*), though FY2009-FY2014 are
  tagged under `NetCashProvidedByUsedInOperatingActivitiesContinuingOperations` (`tools/run.py` does read both tags). Any screen field
  built on the shorter series cannot see the pre-2015 level.
- The screen's `spread` divides a three-year top by a five-year bottom, so it is a cross-window width and not the capex band of either
  window; its own `spread_caveat` half-says this.

---
## Q6: THE REVERSAL CONDITION, IN WORDS (no band, no alert; FOLD step 4, the QLYS ruling)

The file failed on the business, so a price alert would be a category error. **The file reopens only on a filed change in what the
business is**: a multi-year record, in the MD&A's own traffic and check split, of the per person check rising faster than the category's
prices while guest traffic holds, with the operating margin rising out of the 7.6-9.6% band it has held since 2009, that is, [E3-43]'s
pricing half demonstrated; or a row in which the owner's return on operating assets stands clear of Darden's and Brinker's through a
cycle, which is [E2-58]'s "wide". None of these is a price.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 OUT; Q3-Q6 not scored and labelled so.
- [x] No question marked IN carries an "unverified" or "provisional" caveat.
- [x] No UNRESEARCHED verdict. [x] No UNKNOWABLE verdict; the [E4-04] perimeter close was considered and refused in writing.
- [x] Step 0: the 10-K FY2025 (0001104659-26-021292) and the 10-Q to 2026-06-30 (0001104659-26-092408) read, with the Q2 2026 release
  (0001104659-26-091980), the 8-K of 2026-03-05 and the DEF 14A of 2026-04-10; operating cash, D&A, SBC and capex cross-checked against the
  filed statements.
- [x] Owner earnings on every trailing window 1-17 years, every rolling five-year window and the TTM at both (c) ends, beneath the close,
  headed COMPUTATION — NOT A CLEARANCE; **no net-income proxy**; SBC resolves in every year FY2009-FY2025; the depreciation end excludes
  acquired-intangible amortization.
- [x] Competitor row filled: ten SEC filers on one formula and each filer's own last five fiscal years, the subject reconciled to its
  10-K; the segments and private chains that cannot be rowed named with their obstacle.
- [x] Strongest evidence against the leading reading written first (operator rule 9).
- [x] Precedents read and applied or distinguished in writing: DRI, EAT, BLMN followed; CMG and SBUX distinguished; MCD not applicable.
  The ABT, ABBV and CAT questions written both ways and not decided.
- [x] Sovereign for USD from the US Treasury, dated 09/25/2026, struck fresh.
- [x] Value not stated (Q5 not opened). No bar chosen (Q5 not opened).
- [x] Price dated 2026-09-25, aggregator, flagged; shares from the latest periodic cover.
- [x] Every ledger id in this file checked present in `principle_ledger.csv` before writing; ledger rows quoted as stored.
- [x] Run committed to git at the claim, after Step 0/Q1, after Q2, and at the close.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- One line: **TXRH, 2026-09-28, FAIL AT Q2 (OUT on the business).** Price $159.75 (Nasdaq close 2026-09-25, aggregator, flagged) x
  65,640,926 shares (10-Q to 2026-06-30 cover, 0001104659-26-092408) = $10,486M, against 5.49% (US Treasury 30-year par, 09/25/2026). The
  best guest-traffic record in casual dining (positive in every year the filer disclosed it, 2014-2025) was bought with a per person check
  that rose less than the food-away-from-home CPI (FY2014-19 +10.4% against +17.0%; FY2022-25 +20.0% against +24.4%), the operating margin
  held at 7.6-9.6% for seventeen years, and the filer bounds its pricing *"primarily due to competitive reasons"*: [E3-43]'s pricing half
  runs the wrong way and [E3-03] criterion (2) fails in the category's filed flows; [E2-58]'s exception is not wide in a ten-filer row
  (five-year OI/NTOA 35.5% against Darden 39.7%, Brinker 47.4%). Beneath the close, owner earnings $126.0-536.1M (1.20-5.11%) across every
  window and the TTM, five-year $257.8-407.7M (2.46-3.89%). No band, no PORTFOLIO row.
