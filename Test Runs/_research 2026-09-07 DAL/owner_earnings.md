# DAL OWNER EARNINGS — SIX WINDOWS, TWO CAPEX ENDS, TWO TAX BASES
### Working paper for the run of 2026-09-07. **No verdict is drawn in this file.**

Market capitalisation used throughout: **$52,722M** = 657,623,030 shares (10-Q cover, quarter
ended 2026-06-30, accession 0000027904-26-000031) × $80.17 (Stooq, 2026-09-04, aggregator,
live quote only, flagged).

## 1. THE INPUTS, ALL FILED (US$m)

Source: `sources.sec_facts(0000027904)`, cross-checked against the FY2025 10-K cash-flow
statement (accession 0000027904-26-000013) for 2023-2025 and against the FY2019, FY2021 and
FY2023 10-K comparatives for earlier years.

| FY | OCF | equity comp expense | D&A | capex (`PaymentsToAcquireProductiveAssets`) | deferred income taxes in OCF |
|---|---:|---:|---:|---:|---:|
| 2015 | 7,927 | 76 | 1,835 | 2,945 | 2,581 |
| 2016 | 7,205 | 154 | 1,902 | 3,391 | 2,223 |
| 2017 | 5,148 | 169 | 2,235 | 3,891 | 2,071 |
| 2018 | 7,014 | 159 | 2,329 | 5,168 | 1,364 |
| 2019 | 8,425 | 161 | 2,581 | 4,936 | 1,473 |
| 2020 | (3,793) | 119 | 2,312 | 1,899 | (3,110) |
| 2021 | 3,264 | 149 | 1,998 | 3,247 | 115 |
| 2022 | 6,363 | 150 | 2,107 | 6,366 | 591 |
| 2023 | 6,464 | 180 | 2,341 | 5,323 | 980 |
| 2024 | 8,025 | 236 | 2,513 | 5,140 | 1,155 |
| 2025 | 8,342 | 313 | 2,443 | 4,499 | 1,109 |

**Cross-check of the 2025 capex line:** the cash-flow statement's two property-and-equipment
lines are flight equipment $(3,521)M and ground property and equipment $(978)M, summing to
$(4,499)M, which equals the XBRL fact and the MD&A's "$4.5 billion".

**Equity compensation** is from Note 11 for 2023-2025 ($180 / $236 / $313M) and from
`AllocatedShareBasedCompensationExpense` + `ShareBasedCompensation` for earlier years. Delta's
cash-flow statement carries **no share-based-compensation add-back line**; the Note 11 measure
is *"including awards payable in common stock or cash"*, and the equity-settled portion appears
in the stockholders'-equity statement as $115M (2023), $31M (2024) and $120M (2025) of
additional paid-in capital. Subtracting the full expense may therefore double-count the
cash-settled portion; the full expense is subtracted anyway as the standing convention, and the
alternative treatment raises every figure below by roughly $150M.

## 2. THE CONSTRUCTIONS

`base = mean(OCF − equity comp)` · `base_tax = mean(OCF − equity comp − max(deferred tax, 0))`

| window | base | base, cash-tax normalised | D&A | capex | **OE @ capex** | yield | **OE @ capex, tax-norm** | yield | *OE @ D&A (INVALID [E5-20])* |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3-yr 2023-25 | 7,367 | 6,286 | 2,432 | 4,987 | **2,380** | 4.51% | **1,299** | 2.46% | *4,935 / 9.36%* |
| 5-yr 2021-25 | 6,286 | 5,496 | 2,280 | 4,915 | **1,371** | 2.60% | **581** | 1.10% | *4,006 / 7.60%* |
| 7-yr 2019-25 | 5,112 | 4,337 | 2,328 | 4,487 | **625** | 1.18% | **(150)** | (0.28)% | *2,784 / 5.28%* |
| 9-yr 2017-25 | 5,291 | 4,306 | 2,318 | 4,497 | **794** | 1.51% | **(190)** | (0.36)% | *2,973 / 5.64%* |
| 11-yr 2015-25 | 5,683 | 4,441 | 2,236 | 4,255 | **1,428** | 2.71% | **186** | 0.35% | *3,447 / 6.54%* |
| 9 clean ex 2020-21 | 7,035 | 5,530 | 2,254 | 4,629 | **2,406** | 4.56% | **901** | 1.71% | *4,781 / 9.07%* |
| clean-9 at [E5-20] 60% floor | 7,035 | 5,530 | — | 2,777 | **4,258** | 8.08% | **2,753** | 5.22% | — |

**Owner earnings by year at the capex end:**
4,906 / 3,660 / 1,088 / 1,687 / 3,328 / **(5,811)** / **(132)** / **(153)** / 961 / 2,649 /
3,530 for 2015 through 2025. Three of eleven are negative.

## 3. RECONCILIATION TO THE PUBLISHED SCREEN ROW

The published row was `oe_bottom_m 1137 | oe_top_m 4935 | spread 3.341`. Both reproduce
exactly from `Screens/floor_screen.owner_earnings()`, which returns
`{"5y_da": 4005.6, "5y_capex": 1136.8, "3y_da": 4935.0, "3y_capex": 2369.7}`.

The $234M gap between the screen's `5y_capex` ($1,136.8M) and the hand figure above ($1,371M)
is **exactly** the finance-lease additions that `capital_acquired()` adds to cash capex:
$1,049M (2021) + $91M (2022) + $31M (2023) + 0 (2024) + 0 (2025), a five-year mean of $234.2M.

**`capital_acquired()` output, by year:** 2015 2,945 · 2016 3,391 · 2017 3,891 · 2018 5,261
(lease 93) · 2019 5,586 (lease 650) · 2020 2,280 (lease 381) · 2021 4,296 (**lease 1,049**) ·
2022 6,457 (lease 91) · 2023 5,354 (lease 31) · 2024 5,140 (**lease 0**) · 2025 4,499
(**lease 0**).

**The two zeros are wrong.** Delta's FY2025 non-cash schedule reports flight and ground
equipment acquired or modified under finance leases of **$184M (2025)** and $(17)M (2024).
Delta moved the line out of `us-gaap:RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability`
into `dal:RightOfUseAssetObtainedInExchangeForFinanceLeaseLiabilityReversal` in FY2024, and the
SEC `companyfacts` endpoint does not expose Delta's `dal:` namespace at all. See the run file's
DEFECTS section, item 2.

## 4. THE SECOND AXIS — THE CASH-TAX SHIELD

Current versus deferred tax provision, Note 10 (`R83.htm` of the FY2025 filing):

| | 2023 | 2024 | 2025 |
|---|---:|---:|---:|
| Current tax provision (federal + state + international) | **(19)** | **(46)** | **(71)** |
| Deferred tax provision | (980) | (1,155) | (1,109) |
| Total income tax provision | (999) | (1,201) | (1,180) |
| Income before income taxes | 5,608 | 4,658 | 6,185 |
| **Current tax ÷ pre-tax income** | **0.34%** | **0.99%** | **1.15%** |

FY2025 10-K MD&A: *"During 2025, we utilized substantially all of our remaining pre-2018 net
operating loss carryforwards and, due to the limitations on post-2017 net operating losses,
began making cash federal income tax payments. We expect income tax cash payments to increase
in 2026 based on our projected financial results. As of December 31, 2025, we had approximately
$2.4 billion of U.S. federal pre-tax net operating loss carryforwards which we are expecting to
utilize during 2026."*

The "cash-tax normalised" column subtracts the deferred-tax add-back from operating cash flow —
i.e. it asks what owner earnings would have been had the **book** provision been paid in cash.
**Neither end is right**: the as-filed end assumes a shield the registrant says is exhausted,
and the fully-normalised end ignores the recurring deferral that $5.5bn a year of new aircraft
generates. Both are carried, and the width between them is part of the range.

## 5. THE INSTRUMENTS (`Screens/floor_screen.py`, imported directly)

| series | `level_shift` | `best_year_dependence` |
|---|---|---|
| 11-yr, capex end | 2.22 — "STEP UP, normalize down [E4-41]" | 0.444 — two years jointly carry the window |
| 9-yr 2017-25, capex end | **2,040.0 — uninterpretable, see DEFECTS item 1** | 0.948 |
| 9 clean years, capex end | 0.98 — "no step" | 0.130 |
| 9 clean years, D&A end | 1.05 — "no step" | 0.032 — no single-year dependence |

## 6. WHAT IS NOT IN THIS FILE

- Any verdict. The (c) judgment, the great/good/gruesome call and the value range are in the
  run file, which is where a judgment belongs (operator rule 8).
- A split of the FY2025 "Other, net" investing line of $589M between sale-leaseback proceeds
  and two equity-stake disposals. **Delta does not disclose it**; it is named as a hole rather
  than estimated.
- A dollar figure for the 61 widebody aircraft ordered on 2026-01-12 and 2026-01-27. Delta
  discloses the aircraft counts and not the price.
