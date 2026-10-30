## Q3 to Q6 — NOT SCORED. The file closed at Q2, OUT on the business.

⛔ Q3, Q4, Q5 and Q6 are not scored; no verdict below. What was read is recorded so a later reader does not have to
refetch it. Nothing here promotes or rescues the file **[E2-37, E2-38, E3-39]**.

---
## THE SCREEN ROW, ANSWERED

| Field | Screen | Finding |
|---|---|---|
| `acq_note` | "NET CASH INFLOW on the acquisition line ($1,208M, 9% of cap)" | **REFUTED** (Step 0): 2024 a $1,198M payment for the ONEOK pipes, 2025 a $10M adjustment received; $1,208M is the difference of the two tagged values |
| `cap_m` | 13,214 | reproduces at the 2026-08-28 close ($129.53 x 102,015,296 = $13,214M); at the 2026-09-25 close $12,474.4M |
| `oe_bottom_m` | 270 | reproduces as the **three-year capex end** (2023-2025: $6M, $390M, $415M) |
| `oe_top_m` | 570 | reproduces only as the three-year end that subtracts **total D&A including acquired-intangible amortization** ($57-60M a year of the 2019 purchase's customer intangibles); on the filed construction the three-year D&A end is **$628M** |
| `spread` | 1.109 | the width between the two ends of ONE window (570 / 270 − 1); the filing's every-window range is $264M to $702M |
| `yield_bottom`, `vs_sovereign` | 2.05%, −3.30% | struck on the stale cap and an older 5.35% sovereign; today the three-year bottom is 2.17% against 5.49% |
| `growth_required` | 7.95% | reproduces as ~10% less 2.05%; a derivative of the two fields above |
| `years_filed` | 7 | reproduces as seven tagged operating-cash years (2019-2025), but **2019, 2020 and the first half of 2021 are DTE carve-out** and 2019 carries almost none of the Haynesville business; standalone full years are four, current-perimeter years one. **The brief's hypothesis that the series pools pre-separation and acquired businesses is CONFIRMED** |
| `level_shift` / `level_shift_oe`, `best_year_dep` | 1.42 / 1.04 "no step", 0.048 | not relied on; the operating-cash series 390 → 867 contains two perimeter changes (the December 2019 purchase and the 2025 pipes) that a step test on the total does not separate |
| (not in the row) | — | the screen's acquisition flag reads only the business-combination tag and so **misses the $552M Millennium purchase of 2022-10-07** (an equity-method interest) |
| `spread_caveat` | "4-construction width only [...] rebuild it" | answered: seven windows and the TTM rebuilt at both (c) ends below |

---
## COMPUTATION — NOT A CLEARANCE

*Operator rule 3. Arithmetic beneath a closed file. It carries no entry language, no value range and no ranking.*

**Construction** (`oe.py`, output `oe_out.txt`): operating cash as filed, less stock compensation in full **[E5-06]**
(the cash-flow add-back; 1.0-3.0% of operating cash every year, so the [E3-70] grant-value question is immaterial here),
less (c) at two ends: **depreciation and amortization less the acquired-intangible amortization** (tagged
`AmortizationOfIntangibleAssets`, $24-60M) and **total plant and equipment expenditures** (which include growth). No
net-income proxy (operator rule 5).

| Year | Operating cash | SBC | D&A ex acquired amortization | Capex | OE, D&A end | OE, capex end |
|---|---|---|---|---|---|---|
| 2019 (carve-out) | 390 | 6 | 69 | 211 | 315 | 173 |
| 2020 (carve-out) | 597 | 6 | 97 | 518 | 494 | 73 |
| 2021 (half carve-out) | 572 | 12 | 108 | 140 | 452 | 420 |
| 2022 | 725 | 17 | 113 | 338 | 595 | 370 |
| 2023 | 798 | 20 | 125 | 772 | 653 | 6 |
| 2024 | 763 | 23 | 152 | 350 | 588 | 390 |
| 2025 (first year of the current perimeter) | 867 | 26 | 198 | 426 | 643 | 415 |

Every window ending 2025, against the cap of $12,474.4M: one year $415-643M (3.33-5.15%); two $402-616M; three
$270-628M (2.17-5.03%); four $295-620M; **five (the corpus default [E2-42]) $320-586M, 2.57-4.70%**; six $279-571M;
seven $264-534M (2.12-4.28%); **TTM to 2026-06-30 $454-702M, 3.64-5.63%** (TTM amortization taken at the 2025 annual
$60M, flagged). **Every window and the TTM: $264M to $702M, 2.12% to 5.63%, against the 5.49% bond.** The best end of
every annual window is below the bond; only the TTM D&A end touches it. None is near the ~10% figure the corpus quits
on **[E4-28]**.

- **(c) is a disclosed guess [E2-09], and the D&A end is suspect here [E5-20].** A pipeline is in the capital-intensive
  class the framework names with utilities; the filer is starting a *"multi-year modernization program for the acquired
  pipelines"* and PHMSA rules *"require the installation of new or modified safety controls and the implementation of new
  capital projects or accelerated maintenance programs"*. Management's own *"Maintenance capital investment"* in the
  furnished DCF reconciliations is **$34M, $22M, $29M, $30M, $62M (2021-2025)**, one-fifth to one-quarter of depreciation;
  it is a management definition (*"capital expenditures used to maintain or preserve assets or fulfill contractual
  obligations that do not generate incremental earnings"*), not a filed measure of what renewal requires, and this run does
  not use it.
- **Customer prepayments sit in operating cash** (contract liabilities +$97M in 2023, +$23M, +$26M), about $29M a year
  across the five-year window; **[E4-41]** would take them out of a judged level.
- **The JV recapitalisations are NOT in these figures**: NEXUS and Millennium borrowed and paid DTM *"the 371 million NEXUS
  financing distribution"* (2023) and *"the 416 million Millennium financing distribution"* (2024) through investing cash.
  They are borrowed money returned, not earnings, and they moved leverage into the joint ventures (DTM's share of JV
  interest expense: $11M in 2022, $56M in 2025).
- **The perimeter caveat binds the yield.** The cap buys the 2025 perimeter; the 2019-2024 years exclude the ONEOK pipes,
  so the long windows understate the current perimeter's cash and the one-year and TTM figures are the only
  like-for-like ones. Even on those, 3.33-5.63%.

---
## BENEATH THE CLOSE — Q3 MATERIAL, RECORDED WITHOUT A VERDICT

- **Weight case, not declared as a verdict:** leverage is the live determinant (long-term debt $3,324M; the Q4 notes below).
- **[E4-29] fires, in the releases and in pay.** Every furnished release headlines Adjusted EBITDA (*"Full year 2025
  Adjusted EBITDA of $1.138 billion, a 17% increase from 2024"*) and guides it two years out (*"Our Adjusted EBITDA
  guidance for 2026 is $1.155 to $1.225 billion [...] Our 2027 Adjusted EBITDA early outlook range is $1.225 to $1.295
  billion"*), which is also **[E4-22]**'s third flag and **[E5-30]**'s ratchet. The DEF 14A (0001140361-26-011280): the 2025
  annual incentive is **60% Adjusted EBITDA** (threshold $1,095M, target $1,125M, maximum $1,155M, result $1,138M, payout
  143.30%); performance shares (70% of the long-term grant) pay on relative TSR and a *"Leverage ratio [...] calculated as
  total Company net debt [...] excluding debt held by unconsolidated investees [...] divided by adjusted EBITDA"*. The
  incentive **[E4-27]**: a purchase at *"approximately 10.5x 2025 EBITDA"* raises the 60% metric the day it closes; the
  leverage metric excludes the JV debt the recapitalisations created. **No return-on-capital measure in pay.**
- **Metric adjusted after the event [E2-49], a prompt:** *"The Board exercised its authority to adjust the Company's leverage
  ratio for 2024 to exclude debt incurred as a result of the Interstate Pipelines acquisition"*, for the 2022-2024 grants.
- **Candor on the other side [E2-26]:** the DCF reconciliation removes both JV financing distributions as non-routine rather
  than counting them as distributable cash; Operating Earnings equalled reported earnings in 2025 with no adjustments.
- **Cash-tax tell [E4-30], a prompt:** cash taxes paid $24M, $22M, $12M, $5M on pre-tax income of $482M, $500M, $504M,
  $598M (5.0%, 4.4%, 2.4%, 0.8%, 2022-2025) while deferred income taxes rose to $1,270M. The FY2024 10-K records the
  Midwest purchase as *"a taxable deemed asset acquisition"*; the cause of the deferral was not traced further. Read, not
  scored.
- **Share count [E5-15]:** 96,732,466 distributed at separation, 102,015,296 at 2026-06-30 (+5.5%), mostly the
  4,168,750-share offering that funded the 2024 purchase. No buyback.
- **[E2-01] / [E2-43]:** return on total DTM equity (net income $441M on $4,736M) about 9.3% in 2025; the goodwill ($781M)
  and intangibles ($1,862M) are the wedge.

## BENEATH THE CLOSE — Q4 MATERIAL, RECORDED WITHOUT A VERDICT

- **Staying power [E5-11]:** the stream is contracted and large; liquid assets are small (cash $54M); near-term cash
  requirements are light: *"We have no debt maturing until 2029"* (the 2029 notes, $1,100M), revolver to December 2029.
- **Coverage [E2-54]:** 2025 operating cash plus cash interest less capex, $867M + $152M − $426M = $593M, against cash
  interest of $152M, **3.9 times**, before the JV-level debt.
- **Great, good or gruesome [E4-20]:** the gathering half carries the gruesome signature (capital added, $1,416M in five
  years, return on segment assets down from 6.3% to 4.2%); the pipeline half is the good class at a regulated return
  **[E4-43]**. Not scored.
- **Survival shape, as a signature WITHOUT a verdict (Q4 was never opened):** **#27 THE LICENCE** for the FERC third (a
  regulator, not the owner, decides the return on the capital it permits: Guardian's 13% and 5% cuts), and **#20 THE WAVE**
  for the gathering half (one customer, $555-596M a year since 2021, drilling a depleting basin).

---
## Q6 — THE REVERSAL CONDITION, IN WORDS (no band, no alert; FOLD step 4, the QLYS ruling)

The file failed on the business, so a price alert would be a category error. **The file reopens only on a filed change in
what the business is**: (1) the gathering segment showing, for five years in its own segment note, a rising price per Mcf
and a return on its assets well above the bond without capital growth outrunning depreciation; and (2) the FERC-tariffed
share of profit falling to where it no longer decides the whole, or the filings showing negotiated rates earning above
the recourse-rate cap across the interstate book. Neither is a price.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 OUT; Q3-Q6 not scored and labelled so.
- [x] No question marked IN carries an "unverified" or "provisional" caveat.
- [x] No UNRESEARCHED verdict. [x] No UNKNOWABLE verdict; the [E4-04] perimeter close was considered and refused in writing.
- [x] Step 0: the 10-K (0001842022-26-000003) and 10-Q (0001842022-26-000009) read; operating cash, D&A, SBC, capex and the
  acquisition line cross-checked against the filed statements.
- [x] Owner earnings on seven windows and the TTM at both (c) ends, beneath the close, headed COMPUTATION — NOT A
  CLEARANCE; **no net-income proxy**; SBC resolves in every year 2019-2025; the depreciation end excludes acquired-intangible
  amortization.
- [x] Competitor row filled: 13 SEC filers on one metric and one window, the subject reconciled to its 10-K; the unrowed
  named with their obstacle; class NONE, not PROVISIONAL.
- [x] Strongest evidence against the leading reading written first (operator rule 9).
- [x] Precedents read and applied or distinguished in writing: HESM, PAGP, OTTR. The ABT, ABBV and CAT questions written
  both ways and not decided.
- [x] Sovereign for USD from the US Treasury, dated 09/25/2026, struck fresh.
- [x] Value not stated (Q5 not opened). No bar chosen (Q5 not opened).
- [x] Price dated 2026-09-25, aggregator, flagged; shares from the latest periodic cover.
- [x] Every ledger id in this file checked present in `principle_ledger.csv` before writing.
- [x] Run committed to git after Step 0/Q1, after Q2, and at the close.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- One line: **DTM, 2026-09-28, FAIL AT Q2 (OUT on the business).** Price $122.28 (NYSE close 2026-09-25, aggregator,
  flagged) x 102,015,296 shares (10-Q to 2026-06-30 cover, 0001842022-26-000009) = $12,474.4M, against 5.49% (US Treasury
  30-year par, 09/25/2026). At least about a third of the profit is earned under FERC-set or FERC-tariffed rates
  ([E3-03] criterion (3) fails there; Guardian's maximum rate cut about 13% in 2025 and 5% in 2026), and the unregulated
  gathering two-thirds faces named substitutes at a falling unit price and a return on its own assets of 4.2%
  (criterion (2) not shown); DTM is 12th of 14 on return on deployed capital. Beneath the close, owner earnings $264-702M
  (2.12-5.63%) on every window. No band, no PORTFOLIO row.
