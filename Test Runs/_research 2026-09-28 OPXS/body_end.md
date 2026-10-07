## Q3 to Q6 — NOT SCORED. The file closed at Q2, OUT on the business.

⛔ Q3, Q4, Q5 and Q6 are not scored; no verdict below. What was read is recorded so a later reader does not have to
refetch it. Nothing here promotes or rescues the file **[E2-37, E2-38, E3-39]**.

---
## THE SCREEN ROW, ANSWERED

| Field | Screen | Finding |
|---|---|---|
| `deal_note` | "1 8-K Item 1.01 [...] most likely a credit facility or offering" | **CONFIRMED in kind** (Step 0): a Texas Capital Bank master equipment finance agreement of 2026-07-14, $246,783 interim funding toward a $2.1M coating system; no merger, tender or going-private form |
| `wc_note` | "ONE LINE MADE THE CASH: AccountsPayableAndAccruedLiabilities moved 139% of 2023 OCF" | **REFUTED** (Step 0): FY2023 operating cash was **−$296K**; the payables line (+$411K) is 139% of an absolute value; the year was decided by a $2,941K inventory build. The flag carries no sign |
| `cap_m` | 70 | reproduces at about $10.06 a share on the same count; at the 2026-09-25 close $72.5M |
| `oe_bottom_m`, `oe_top_m` | 1, 2 | reproduce in size as the five-year window ($1.48-1.57M on the filed construction); `yield_bottom` 1.98% implies $1.39M, near the five-year conservative end under the tool rule that counts the $800K intangible tag in FY2025 (below), $1.34M at 1.91%; not exact |
| `yield_bottom`, `vs_sovereign` | 1.98%, −3.37% | struck on the stale cap and an older 5.35%; today the five-year window is 2.04-2.16% against 5.49% |
| `growth_required` | 8.02% | reproduces as ~10% less 1.98%; a derivative of the two fields above |
| `level_shift` 2.2 "STEP UP - normalize down [E4-41]"; `best_year_dep` 0.36, `best_year_dep_oe` 0.481 "ONE YEAR CARRIES THE WINDOW" | | **CONFIRMED**: FY2025 alone is $6.05-6.19M of owner earnings against a five-year mean of $1.48-1.57M; it is 82% of the five-year sum at the capex end, and the trailing twelve months to 2026-06-28 are $0.58-1.29M |
| `level_shift_oe` "EARLY HALF STRADDLES ZERO" | | **CONFIRMED**: owner earnings were negative in eight of the sixteen filed years (FY2010, 2013, 2015, 2016, 2017, 2019, 2021, 2023) at the capex end |
| `years_filed` | 16 | reproduces as FY2010-FY2025; **the operating-cash tag is absent for FY2013-FY2015**, read here from the three 10-Ks (0001571049-13-001285, 0001571049-14-007394, 0001571049-15-009981) |
| `spread_caveat` | "4-construction width only [...] rebuild it" | answered: every trailing window 1-16 years, every rolling five-year window and the TTM, both (c) ends, below |

---
## COMPUTATION — NOT A CLEARANCE

*Operator rule 3. Arithmetic beneath a closed file. It carries no entry language, no value range and no ranking.*

**Construction** (`oe.py`, output `oe_out.txt`): operating cash as filed, less stock compensation in full **[E5-06]** (the cash-flow
add-back, *"Stock Compensation Expense"*, which resolves in every year FY2010-FY2025 and includes the restricted board shares and the
market-based officer awards; the 10-Q says the December 2025 performance shares, *"The fair value of these awards totaled $679 thousand as of
the grant date"*, are amortized through the same line), less (c) at two ends: **depreciation excluding acquired-intangible amortization**
(the AOC backlog intangible in FY2015, $342K, and the Speedtracker intangible in FY2024-FY2025 are left out) and **total purchases of property
and equipment**. No net-income proxy (operator rule 5). Dollars in thousands.

| FY | Operating cash | SBC | Depreciation | Capex | OE, capex end | OE, depreciation end |
|---|---|---|---|---|---|---|
| 2010 | (876) | 97 | 66 | 116 | (1,089) | (1,039) |
| 2011 | 1,114 | 87 | 66 | 31 | 996 | 961 |
| 2012 | 848 | 152 | 165 | 96 | 600 | 531 |
| 2013 | (1,538) | 128 | 69 | 121 | (1,787) | (1,735) |
| 2014 | 1,671 | 105 | 80 | 40 | 1,526 | 1,486 |
| 2015 (AOC bought) | (1,218) | 140 | 334 | 2,100 | (3,458) | (1,692) |
| 2016 | (539) | 192 | 345 | 34 | (765) | (1,076) |
| 2017 | 16 | 220 | 337 | 149 | (353) | (541) |
| 2018 | 1,039 | 153 | 327 | 167 | 719 | 559 |
| 2019 | 160 | 113 | 340 | 143 | (96) | (293) |
| 2020 | 3,911 | 197 | 248 | 152 | 3,562 | 3,466 |
| 2021 | 481 | 228 | 263 | 274 | (21) | (10) |
| 2022 | 2,042 | 162 | 307 | 257 | 1,623 | 1,573 |
| 2023 | (296) | 247 | 345 | 376 | (919) | (888) |
| 2024 | 1,781 | 425 | 387 | 681 | 675 | 969 |
| 2025 | 6,931 | 383 | 359 | 494 | 6,054 | 6,189 |

**Every trailing window ending FY2025, against the cap of $72.5M:** one year **$6,054-6,189K (8.35-8.53%)**; two $3,364-3,579K
(4.64-4.94%); three $1,937-2,090K (2.67-2.88%); four $1,858-1,961K (2.56-2.70%); **five (the corpus default [E2-42]) $1,482-1,567K,
2.04-2.16%**; seven $1,554-1,572K (2.14-2.17%); ten $995-1,048K (1.37-1.44%); **sixteen $454-529K (0.63-0.73%)**, $583K at the capex end with
the AOC fixed assets taken out of FY2015. **Rolling five-year windows** (capex end to depreciation end): to FY2014 $49K/$41K; to FY2015
−$425K/−$90K; to FY2016 −$777K/−$497K; to FY2017 −$967K/−$712K; to FY2018 −$466K/−$253K; to FY2019 −$791K/−$609K; to FY2020 $613K/$423K;
to FY2021 $762K/$636K; to FY2022 $1,157K/$1,059K; to FY2023 $830K/$770K; to FY2024 $984K/$1,022K; to FY2025 $1,482K/$1,567K. **Five of the
twelve rolling five-year windows are negative at both ends, and a sixth (to FY2014) is near zero.** **TTM to 2026-06-28** (FY2025 less nine months FY2025 plus nine months
FY2026): operating cash $2,552K, SBC $874K, capex $1,097K, depreciation about $384K (the nine-month FY2025 amortization estimated at
three-quarters of the year's $156K, flagged): **$581K to $1,294K, 0.80-1.78%**.

- **Only one year, FY2025, clears the bond, and it does not clear the ~10% the corpus quits on [E4-28].** Every multi-year window sits
  between 0.6% and 4.9%, below the 5.49% bond; **the bottom sits below zero on five of twelve rolling five-year windows and near zero on a sixth**. The range
  is wide enough that no useful conclusion could be reached from it **[E4-25]**.
- **(c) is a disclosed guess [E2-09]; here the two ends are close** (depreciation $66-387K, capex $31-681K outside FY2015), because the
  plants are leased and the work is labour-driven (*"As our processes are primarily labor driven"*). The width lives in the operating cash
  itself, which swings with inventory: FY2023 −$2,941K, FY2024 −$2,710K, FY2025 +$541K, nine months FY2026 −$2,126K. **[E2-23]'s
  working-capital increment is required here**: inventory ran at 35-47% of revenue in FY2022-FY2025 ($14.3M against $41.3M in FY2025) and a growing book
  consumes it.
- **[E4-41], normalise down**: FY2025's operating cash carried a working-capital release (inventory +$541K, payables +$725K) at the top of the
  procurement cycle; the TTM figure is a fifth of it.
- **Capital spent outside (c), recorded**: the Speedtracker product line, bought in January 2024 with *"$1 million cash on hand"* plus $30K of
  transaction costs ($1,050K of *"Purchases of Intangible Assets"* in FY2024 investing cash), impaired in full ($804K) on 2025-09-28; the AOC purchase from L-3 in November 2014 for $1,013.1K cash against assets the filer
  valued at $3,123.4K (a bargain purchase). **The FY2015 statement cannot be reconciled to the cash consideration from the filing as read**:
  the investing line shows $2,100K of property purchases while the cash consideration was $1,013.1K and the acquired fixed assets were valued
  at $2,064.7K; FY2015 is carried as filed and flagged, and every window that includes it (eleven years and longer) carries the flag.
- **Net-settlement withholding** ($19-245K a year, *"Cash Paid for Taxes Withheld On Net Settled Restricted Stock Unit Share Issue"*) sits in
  financing; it is the cash form of part of the SBC already subtracted, and is not subtracted twice.

---
## BENEATH THE CLOSE — Q3 MATERIAL, RECORDED WITHOUT A VERDICT

- **Weight case, not declared as a verdict:** daily execution is the live determinant (fixed-price bids, overhead absorption and contract
  execution decide each year **[E3-43]**'s *"a business"* clause); no leverage; no control.
- **[E4-29] fires, in the releases and the 10-K.** The 10-K MD&A and every furnished release carry *"Adjusted EBITDA"* (FY2025 $8,030K
  against net income $5,147K, the impairment added back); the Q3 FY2026 release (8-K filed 2026-08-11, accession 0001493152-26-037114,
  EX-99.1) lists it among its highlights and **guides it**: *"the Company continues to expect full-year fiscal 2026 Adjusted EBITDA to range
  between $7.5 million and $8.5 million"*, with revenue guidance *"of between $43 million and $45 million"*. That is also **[E4-22]**'s third
  flag and **[E5-30]**'s ratchet. The 10-Q adds a *"Non-recurring General and Administrative Expenses"* line ($291K) to its Adjusted EBITDA
  for the CEO overlap.
- **What pay vests on [E4-27]:** DEF 14A filed 2026-01-20 (accession 0001493152-26-002846). The CEO's bonus is *"based upon a one-year
  operating plan adopted by the Company’s Board"*, target 30% of a $300,000 salary, metrics not named; the performance shares granted
  2025-12-17 (50,000 to the CEO, 17,500 to the CFO) *"vest in five equal increments if [...] the average VWAP per share of common stock
  equals or exceeds $17.54, $21.05, $25.26, $30.31, and $36.37"*. **Pay on the stock price is [E3-50]'s eighth-flag prompt** (*"the highest
  stock price possible"*); no return-on-capital measure in pay.
- **Insider ownership and related parties:** directors and officers 27.7% as a group at 2026-01-12 (Dayton Judd 12.4%, Danny Schoening
  11.5%); Topline Capital Partners 10.0%; *"There are no transactions disclosable under Item 404 of Regulation S-K."*
- **Capital allocation, recorded:** the 2022 issuer tender, 1,603,773 shares *"at $ 2.65 , or $ 4.25 million"* (19% of the shares then
  outstanding), plus $371K of open-market purchases the same year; dividends paid in FY2017 ($261K) and FY2018 ($784K); a new $10,000,000
  repurchase authorisation on 2026-02-09 (about 14% of today's cap), unused through 2026-06-28; the Speedtracker purchase written off within
  about 20 months; the AOC purchase of 2014 at about a third of the
  filer's own fair value. **[E5-15], a prompt from the history:** common shares 314,867 at FY2015 year end, after the reverse split of
  2015-10-06 (tagged; ratio not traced), and 8,266,601 at FY2016 year end, through the preferred conversions and the 2016 offering ($4,247K of
  proceeds, tagged); not traced further.
- **[E2-01]:** return on equity FY2025 about 21% ($5,147K on $24,291K); FY2021-FY2025 net income $14,592K on average equity of about $17.2M,
  about 17% a year, with no debt; FY2012-FY2017 near zero or negative.

## BENEATH THE CLOSE — Q4 MATERIAL, RECORDED WITHOUT A VERDICT

- **Staying power [E5-11]:** cash $6.2M and no revolver draw at 2026-06-28; the $3M Texas Capital revolver runs to 2027-05-22 (covenants: fixed
  charge coverage at least 1.25:1, total leverage 3:1, and *"capital expenditures (limited to $1 million per year)"*); the new equipment line
  carries the same two ratios; capital commitments of $2.8M at 2026-06-28 (*"a DLC coater, a prototype metal machining center, a high vacuum
  coating system and a 4D PhaseCam LWIR Interferometer"*) against the loan agreement's $1M capex limit; leases $1.85M at FY2025.
- **Concentration:** *"approximately 70% of our gross business revenue from five major customers"*; *"approximately 83% of our material
  requirements are single-sourced across 104 suppliers"*; *"Approximately 99% of our contracts contain termination clauses for
  convenience"*; a pending termination for convenience on the M10 Booker (*"approximately $1.3 million"* of backlog).
- **Great, good or gruesome [E4-20]:** not scored. The capital needed is small but the stream is not reliable (eight negative years of
  sixteen).
- **Survival shapes, as signatures WITHOUT a verdict (Q4 was never opened):** **#20 THE WAVE** (the FY2023-FY2025 record is the ground-vehicle
  replenishment and its supply-tight years; the 10-Q records the orders slowing and a new entrant), with **#14 THE PATRON** as a feature (the
  buyer that funds the programme sets the terms: appropriations, continuing resolutions, termination for convenience, TINA certified cost)
  and **#11 THE PASS-THROUGH** as a feature (fixed prices absorbed the 2021-2025 cost inflation; the buyer keeps a second source so that the
  next bid passes productivity back). No new shape.

---
## TOOLING, REPORTED NOT PATCHED (operator rule 8; a tool may never add a number)

- **`tools/run.py OPXS`** (output `runpy_out.txt`) defaults to a **three-year** window and prints the corpus's five-year window as "THE
  OTHER WINDOW"; prints its table in **whole millions**, so for a $72M filer SBC and D&A show as 0 and 1 and no row can be checked by eye; and
  **builds FY2025 "D&A" as $1,159K against a filed $515K**, because its component rule adds the `AmortizationOfIntangibleAssets` tag, which
  this filer used for **$800K in FY2025**, to `Depreciation` ($359K). The filed amortization was $156K (D&A $515K less depreciation $359K); the $800K is the Speedtracker write-off
  (tagged separately as `AssetImpairmentCharges` $804K). Its conservative end takes max(D&A, capex) per year, so the impairment enters (c) and
  its three-year yield reads **2.36%** where the filed construction reads 2.67%. **A one-time impairment counted as maintenance capital; the
  third form of the acquired-amortization defect already on record.**
- Its *"3. POINTS OVER THE SOVEREIGN -0.51 .. -0.08"* rests on the unprinted growth assumption in `points_over()`, and its *"2. GROWTH THE
  PRICE ASSUMES 7.2% (at a 5.49% rate)"* is struck against the bond, not the ~10% floor [E4-28]; reported, not used.
- **`working_capital_flag()` (the screen's `wc_note`) carries no sign**: on a year of negative operating cash it divides by the absolute
  value and reports a line as having *"MADE THE CASH"* when the cash was below zero and a different line (inventory) decided it.
- The operating-cash tag is absent for FY2013-FY2015 in companyfacts, so any tool series for this filer silently skips three years.

---
## Q6 — THE REVERSAL CONDITION, IN WORDS (no band, no alert; FOLD step 4, the QLYS ruling)

The file failed on the business, so a price alert would be a category error. **The file reopens only on a filed change in what the
business is**: a 10-K whose Item 1 no longer says the buyers keep *"at least two"* suppliers for the products that carry the profit, together
with a multi-year record of the filer raising prices on its own schedule (not at re-bid) while unit volume holds, and operating margins that
stay well above the bond through a year of falling orders. None of these is a price.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 OUT; Q3-Q6 not scored and labelled so.
- [x] No question marked IN carries an "unverified" or "provisional" caveat.
- [x] No UNRESEARCHED verdict. [x] No UNKNOWABLE verdict; the [E4-04] perimeter close was considered and refused in writing.
- [x] Step 0: the 10-K FY2025 (0001493152-25-028071) and the 10-Q to 2026-06-28 (0001493152-26-037119) read, with the FY2024, FY2023, FY2015,
  FY2014, FY2013 and FY2011 10-Ks for the series; operating cash, D&A, SBC, capex and the working-capital lines cross-checked against the filed
  statements.
- [x] Owner earnings on every trailing window 1-16 years, every rolling five-year window and the TTM at both (c) ends, beneath the close,
  headed COMPUTATION — NOT A CLEARANCE; **no net-income proxy**; SBC resolves in every year FY2010-FY2025; the depreciation end excludes
  acquired-intangible amortization.
- [x] Competitor row filled: eight SEC filers on one metric and one window, the subject reconciled to its statements; the named rivals that
  cannot be rowed (private or London-listed) named with their obstacle; the verdict does not rest on the row.
- [x] Strongest evidence against the leading reading written first (operator rule 9).
- [x] Precedents read and applied or distinguished in writing: HII, BUKS, ERIC. The ABT, ABBV and CAT questions written both ways and not
  decided.
- [x] Sovereign for USD from the US Treasury, dated 09/25/2026, struck fresh.
- [x] Value not stated (Q5 not opened). No bar chosen (Q5 not opened).
- [x] Price dated 2026-09-25, aggregator, flagged; shares from the latest periodic cover.
- [x] Every ledger id in this file checked present in `principle_ledger.csv` before writing; ledger rows quoted as stored.
- [x] Run committed to git at the claim, after Step 0/Q1, after Q2, and at the close.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- One line: **OPXS, 2026-09-28, FAIL AT Q2 (OUT on the business).** Price $10.42 (Nasdaq close 2026-09-25, aggregator, flagged) x
  6,959,873 shares (10-Q to 2026-06-28 cover, 0001493152-26-037119) = $72.5M, against 5.49% (US Treasury 30-year par, 09/25/2026). A
  build-to-print maker of military periscopes, sights and laser filters whose buyers, in its own 10-K, *"have two fairly strong suppliers.
  It is in their best interest to keep at least two"*, whose 10-Q records *"new competition"* and possible *"pricing concessions"*
  ([E3-03] criterion (2) fails), and whose fixed prices could not follow cost while its returns followed volume (operating margin −11% to
  +17%, five loss years in fourteen; [E3-43] not demonstrated). Beneath the close, owner earnings $454K-$6,189K (0.63-8.53%) across every
  trailing window, five-year $1.48-1.57M (2.04-2.16%). No band, no PORTFOLIO row.
