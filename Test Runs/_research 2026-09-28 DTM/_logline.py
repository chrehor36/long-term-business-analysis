import sys
ts=sys.argv[1]
line=("- "+ts+" | DTM (DT Midstream, Inc., cover 10-Q 0001842022-26-000009) | Q1 IN / Q2 OUT (on the business: "
"[E3-03] criterion (3) fails for the FERC-tariffed third of the profit in the filer's words, rates \"established by independent, third-party regulators\", "
"Guardian maximum tariff cut about 13% from 2025-04-01 and a further 5% from 2026-04-01; criterion (2) not shown for the unregulated gathering two-thirds, "
"which competes on \"price and service offerings\" against rival gatherers and producer-owned systems; gathering revenue per Mcf $0.523 to $0.491 2021-2025 on flat volume, "
"$1,416M of gathering capex for revenue +4% and operating income -13%, return on segment assets 6.3% to 4.2%; 12th of 14 SEC filers at 7.8% against a median of 11.8%; "
"take-or-pay terms, 20-year G3 agreements and Northeast permitting difficulty recorded as the strongest evidence against; PAGP, HESM and OTTR followed or distinguished in writing; "
"the open ABT, ABBV and CAT questions written both ways, none moves the file) | $122.28 (2026-09-25 NYSE close, aggregator, flagged) x 102,015,296 sh (one class, cover_shares.py agreed) "
"= cap $12,474.4M; sovereign 5.49% (UST 30Y par 09/25/2026, struck fresh) | FAIL (Q2) | 86070d9f 1ed75576 cc83dd7d 4905c95d b4f15697 | "
"WAVE 7 name 91 of 218, register entry 233 (dispatcher verified from the files: heading unique at line 502, 233 entries to the write-early heading, DTM first and once; "
"done file 91 lines ending DTM; no alert and no PORTFOLIO row; reading-list fold ends \"Next in the order file: OPXS.\"; check_framework PASS re-run by the dispatcher). "
"DTM in no tier roster. No live deal: DTM the buyer in every deal filing. Separated from DTE mid-2021: 2019 to H1 2021 carve-out, four full standalone years, current perimeter only in 2025. "
"Beneath the close, computation only: owner earnings $264-702M every window and TTM (2.12-5.63% of cap), five-year 2.57-4.70%. "
"#27 THE LICENCE and #20 THE WAVE named as signatures without a verdict, dated note only. Screen errors: acq_note refuted (a $1,198M payment in 2024 and a $10M adjustment received in 2025, not a $1,208M inflow); "
"cap_m at the 2026-08-28 close; oe_top 570 only with acquired-intangible amortization as (c) (filed three-year D&A end $628M); years_filed 7 counts carve-out years; the 2022 $552M Millennium stake unseen; "
"level_shift misses two perimeter changes; spread, yield_bottom, vs_sovereign and growth_required on the stale cap and 5.35%. "
"REPORTED, NOT PATCHED: tools/run.py subtracts acquired-intangible amortization, defaults to a three-year window, points_over() rests on an unprinted growth, growth struck against the bond not the floor, "
"five-year figure about $5M a year off the filed construction (untraced), no spin-off or year-end acquisition warning. "
"Agent's own errors (a Haynesville purchase value, gathering depreciation, a peer count, a JV base change, two quotes made verbatim) corrected before commit. "
"Left on disk uncommitted: the ignored cache/. 127 remain. Next: OPXS.\n")
open('Screens/_daily/OVERNIGHT LOG.md','a',encoding='utf-8').write(line)
