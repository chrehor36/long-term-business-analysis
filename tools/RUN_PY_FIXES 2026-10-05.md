# RUN.PY FIXES, 2026-10-05

Nine defects in `tools/run.py`, each found by a run of 2026-10-05 and corrected by hand from the filing in
that run. The fixes are transcription and arithmetic only (the tooling test in `Framework/OPERATOR-PROTOCOL.md`):
each new line is a filed figure, printed with the element it came from, or a sum or difference of filed
figures under a stated definition. Where two readings exist, both print and neither is chosen. Built
in a dev copy, tested on the eleven names below, then swapped into `tools/run.py` in one step.

**What changed in method.** The SEC companyfacts file carries standard elements only, and does not say which
section of a statement a line sits in. Three of the defects lived there: filer-specific elements
(MBUU's directors' stock pay, MTRN's mine development) and section placement (securities bought inside
operating cash flow). `tools/run.py` now also reads the calculation linkbase and instance of the last
three annual reports from EDGAR, cached in `tools/_cache/`, and lists the lines that sum to operating
cash flow, to investing cash flow and to liabilities. Each fiscal year is taken whole from the newest
filing that covers it. Filers that embed the linkbase in the schema (GENC) are read from the `.xsd`.

## Before and after

All figures are in USD millions unless marked. "Before" is the old `tools/run.py`. "After" is the new one.
"Filed" is the figure the run file of 2026-10-05 took from the filing.

| # | Defect | Test name | Before | After | Filed (run file) |
|---|---|---|---|---|---|
| 1 | Stale share count after a split | IESC | 19.9M shares (cover, 2026-07-27), cap 6.74B | cover and balance-sheet counts both listed with dates; split factor 2 after the cover date printed; 39.849M on the quote's basis, cap 13.48B (the filed-count cap 6.74B printed beside it) | 39,848,712 shares, cap $13,476M |
| 1 | Stale share count | SONY (`--quote 6758.T`) | 1,250.7M, a FY3/21 weighted average, pre-split; cap ¥4,656bn | every count listed with its date; the newest, IFRS 6,149.8M at 2025-03-31, used and labelled STALE (553 days); cap ¥22,896bn | 5,872.5M at 2026-06-30 (6-K, not in XBRL); cap ¥21,863bn |
| 2 | Treasury rate for a non-USD earner | SONY | USD 5.63%, US Treasury | JPY 4.15%, Japan MOF JGB 30-year, 2026-10-02; earnings currency taken from the XBRL unit | JPY 4.148%, MOF, 2026-10-02 |
| 3 | Securities purchases inside OCF | IESC FY2025 | OCF 286, no other line | OCF filed 286.1; `us-gaap:IncreaseDecreaseInTradingSecurities` effect −62.1; OCF excluding it 348.2 | "Marketable securities (62,099)" inside operating activities |
| 3 | Securities purchases inside OCF | GENC FY2025 | OCF 3, no other line | OCF filed 3.1; `us-gaap:IncreaseDecreaseInMarketableSecuritiesRestricted` effect −18.5; OCF excluding it 21.5 | "Marketable securities (18,460,000)" inside operating activities |
| 4 | Stock pay printed as 0 | EME 2025 | SBC 0 (all three years) | 20.6 via `AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue` (2024 20.0, 2023 13.7); tag printed per year | $20,595K (2024 $19,978K, 2023 $13,739K) |
| 4 | Stock pay printed as 0 | SXI FY2026 | SBC 0 (all three years) | 8.8 via the same fallback (FY2025 8.7, FY2024 9.8) | $8,821K (FY2025 $8,691K, FY2024 $9,811K) |
| 4 | Directors' stock pay missing | MBUU FY2026 | SBC 6 (employees only) | SBC 5.6, plus `mbuu:ShareBasedCompensationDirectors` 1.0 listed as an other stock-pay line; alternate owner cash (capex basis) 36.2 | 5,603 + 1,041 ($K); owner cash $36,202K |
| 4 | No stock pay at all | GENC | SBC 0 | "n/f" each year, with "not found in XBRL; read the cash-flow statement" | no equity plans FY2022-25 (Note 11) |
| 5 | Equity element missing | V (`--shares 1876`) | no equity column | equity 2017-2025 via `StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest`, e.g. 32,760 (2017), 37,909 (2025); element printed | 32,760 and 37,909 (assets less liabilities, the review's arithmetic) |
| 6 | "OE lo" / "OE hi" labels | HUBB 2024 | OE lo 748, OE hi 780 | OE capex 780, OE D&A 748; which basis is lower printed by year (capex in 2023, D&A in 2024-25) | 780.2 (owner cash, all capex), 748.5 (D&A variant) |
| 6 | "OE lo" / "OE hi" labels | MBUU FY2025 | OE lo 12, OE hi 23 | OE capex 22.7, OE D&A 12.0 | 21.6 all-capex after directors' pay ($21,582K) |
| 7 | Debt shows non-current only | OSIS FY2024 | lt debt 129 | debt on the face: `LineOfCredit` 384, `LongTermDebtCurrent` 8, `LongTermDebtNoncurrent` 129, sum 522 (FY2025: 178 + 8 + 464 = 650) | bank line $384M (FY2025 $178M) missing from the tool |
| 7 | Debt shows non-current only | EXTR FY2026 | lt debt 144 | `LongTermDebtCurrent` 19 + `LongTermDebtNoncurrent` 144 = 164 | 144 non-current; 165.0 gross in total |
| 8 | Mine development omitted | MTRN FY2025 | window stopped at FY2024; no mine line | FY2025 in the window (capex element `PaymentsToAcquireOtherPropertyPlantAndEquipment` 53.3); `mtrn:PaymentsForMineDevelopment` 26.3 (2024 12.2, 2023 9.3); capex alt 79.6 | PP&E 53.3; mine development 26.3 (12.2, 9.3) |
| 8 | Intangible payments omitted | OSIS FY2026 | capex 31 only | `PaymentsToAcquireOtherProductiveAssets` 18.0 (FY2025 17.7, FY2024 17.3); capex alt 48.5; alternate owner cash (capex basis) 200.9 | 18.0 (17.7, 17.3); owner cash 200.9 |
| 9 | Insurer message | (code read) | points to `Framework/SECTOR METHOD v5 - insurers and float companies.md` | unchanged; confirmed | the file exists |

## Also fixed, found while testing
- `--write` (v5 template) divided shares and cap, already in millions, by a million again and wrote "0.000M".
  It now writes the counts, the split note, the owner-earnings and alternates tables and the balance sheets.
- `--write --framework v4` crashed when the growth or points line was refused. It now leaves those blanks.
- The balance-sheet columns now take each year from the first element in the list that has it, not
  from the first element with any data. IESC's cash was blank for 2019-2022 and is now filled.
- When the window's last year is more than 18 months old, or OCF is tagged later than the window ends, the tool says so.
- `--currency` now defaults to the XBRL earnings unit. A typed currency that differs is used and the
  disagreement is printed. A currency with no issuing-authority source prints that, and no rate.

## What `tools/screen.py` sees
`tools/screen.py` imports `owner_earnings` from `tools/run.py`, so it now gets the stock-pay fallback and the
added capex element. Its `oe_lo` and `oe_hi` are unchanged in definition. EME, SXI and MTRN re-rank
(EME 2.98..3.14% before, 2.93..3.09% after; SXI 1.42..1.70% before, 1.16..1.44% after). `tools/screen.py`
itself was not edited.

## Not fixed
- **`tools/screen.py`'s own share count.** It still uses the weighted average and no split factor (IESC 6.8B).
  That is separate code, not shared with `tools/run.py`, so it was left alone.
- **SONY's current share count is not in XBRL.** The 2026-06-30 count is in a 6-K. The tool prints the
  newest filed count as STALE. `--shares` remains the route.
- **IFRS cash-flow elements are not read**, so SONY's owner earnings still stop at FY3/21 (US GAAP).
  The tool now says the window is over 18 months old. This was not one of the nine defects.
- **MTRN stock pay.** The largest-element rule (the CGNX fix of 2026-09-07) picks
  `AllocatedShareBasedCompensationExpense`, 11.2 for 2025, against the cash-flow line's 10.9. The rule
  was left as it is, so MTRN's alternate owner cash is 12.5 against the run's 12.7.
- **V has no single share count in companyfacts** (a multi-class cover). It still needs `--shares`, as before.
- The linkbase read needs EDGAR. If a filing cannot be read, the tool names it and says which checks
  were not made. It never prints an empty list as if it were a finding.

## Added later on 2026-10-05: finance-lease principal and paid-in-kind interest (the KLXE run)
FinanceLeasePrincipalPayments now joins the capex alternate, and PaidInKindInterest (a non-cash add-back inside operating cash flow) comes off the OCF alternate; both from companyfacts, printed beside the as-filed columns, neither chosen. KLXE 2025: lease principal 19.9 plus PIK interest 16.6, together 36.5 against the run's hand figure of about 36.

## Added later on 2026-10-05: rental-fleet purchases (the WSC run)
The capex alternate now also catches rental-fleet purchases in the investing section (for example us-gaap:PaymentsToAcquireEquipmentOnLease). WSC 2023 to 2025: 227.0, 280.9, 317.7, matching the run. tools/screen.py still ranks on the as-filed capex, so a rental company's screen yield is overstated until its run reads the alternate.

## Added later on 2026-10-05: dividends to minority partners (the ADNT run)
PaymentsOfDividendsMinorityInterest joins the alternate deductions: cash paid to minority partners in consolidated subsidiaries never reaches the parent's owners. Printed beside the as-filed columns, not chosen.
