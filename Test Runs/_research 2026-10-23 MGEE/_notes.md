# MGEE research notes (2026-10-23)
Working notes for the run. Started before any fetch.

## Sources fetched (raw in cache/, gitignored)
- 10-K FY2025 0001193125-26-067036; 10-K FY2022 0000950170-23-003632 (segments 2020-22)
- 10-Q Q2 2026 0001193125-26-333969; DEF 14A 0001161728-26-000005
- 8-Ks 0001193125-26-214717 (offering/forwards), -334011 (Q2 earnings), -360327 (dividend), -414025 (credit agreements)
- SEC companyfacts MGEE (CIK 1161728), WEC (783325), Alliant (352541). WPL (107832) has no standalone facts.
- Price $74.24 close 2026-10-22 (Yahoo, aggregator). UST 30y 5.29% 10/22/2026 (Treasury).
- tools/run.py MGEE failed: no overlapping OCF/D&A/capex (D&A tag is UtilitiesOperatingExpenseDepreciationAndAmortization).

## Segment net income 2021-2025 (USD M; 10-K FY2022 and FY2025 Footnote 22)
Electric 63.9, 65.2, 75.9, 74.5, 85.8 = 365.3 (61.8%)
Gas 15.5, 18.2, 14.1, 13.7, 16.3 = 77.8 (13.2%)
Nonregulated 21.4, 22.1, 22.4, 24.1, 24.8 = 114.8 (19.4%)
Transmission 6.9, 6.6, 7.7, 8.9, 9.5 = 39.6 (6.7%)
All other -1.9, -1.2, -2.4, -0.7, -0.4 = -6.6
Total NI 591.0

## ROE (NI / average common equity), XBRL
MGEE 2016-2025: 10.7,13.0,10.6,10.4,10.1,10.6,10.5,10.6,10.2,10.7 (avg 2015-25 10.71)
Alliant 2016-2025: 9.5,11.1,11.7,11.4,11.3,11.3,11.2,10.8,10.0,11.3 (avg 10.92)
WEC 2016-17, 2020-25: 10.6,13.0,11.5,11.9,12.4,11.2,12.3,11.6 (avg 11.59; 2020+ equity incl. NCI; 2018-19 missing)

## Year-end closes (Yahoo, aggregator): 2016 65.30, 2017 63.10, 2018 59.96, 2019 78.82, 2020 70.03, 2021 82.25, 2022 70.40, 2023 72.31, 2024 93.96, 2025 78.42

## Close checks (2026-10-23)
- check_ids.py on the run file: E-ids none; 64 distinct ids cited, none missing from principle_ledger_v5.csv; 21 quoted fragments beside an id checked, 0 failing.
- tools/check_framework.py: PASS.
