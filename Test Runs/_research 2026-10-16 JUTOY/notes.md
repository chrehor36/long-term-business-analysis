# JUTOY research notes (2026-10-16)

Run file copied from template before any fetch.

## Tools
- tools/run.py JUTOY: refused (not an SEC filer).
- Screens/cover_shares.py JUTOY: refused (NOT AN SEC REGISTRANT).
Figures taken by hand from HKEX filings.

## Step 0 sources (fetched 2026-10-16)
- Sovereign, RMB: PRC Ministry of Finance China Treasury Yield Curve (财政部-中国国债收益率曲线), published by ChinaBond on MOF's behalf at yield.chinabond.com.cn/cbweb-czb-web (key-term table queryGjqxInfo, workTime 2026-10-16): 30Yr 2.06%, 10Yr 1.65%. Chart series same day: 30.0 -> 2.06, 10.0 -> 1.648.
- FX: CFETS central parity (published for the PBOC), chinamoney.com.cn ccpr.json, 2026-10-16 9:15: HKD/CNY 0.85658; USD/CNY 6.7220.
- Price (aggregator, Yahoo chart API, flagged): 3303.HK last 2026-10-16 HK$0.38 (vol 384,000); 2026-10-15 HK$0.365. JUTOY ADR last trade 2026-10-14 US$12.54 (100 ADRs).
- ADR ratio: 1 ADS = 250 ordinary shares (Form F-6EF, 2009-04-23, accession 0001019155-09-000474; and F-6EF 2008, accession 0001144204-08-069883).
- Shares: Monthly Return FF301 for month ended 30 Sep 2026 (submitted 2026-10-06, HKEX file 2026100600381): 2,488,835,287 issued, 0 treasury. Rights-issue results announcement 2026-03-19 (2026031901220): 2,133,287,389 before + 355,547,898 rights shares = 2,488,835,287. Matches.
- Options outstanding (MR Sep 2026): 33,545,509 at HK$1.93; 132,404,790 at HK$0.47 (both out of the money at HK$0.38).

## Checks at close (2026-10-16)
- check_ids.py: 68 id citations, 49 distinct, 0 missing, 32 fragments beside ids found in their rows, no E-ids: PASS.
- tools/check_framework.py: PASS (TEST RUNS: phantom in 0 files).
- Correction to a first misreading of the rights-issue table: Cheung Hing (18.61 percent) is the chairman's company; Tang Hui holds 0.43 percent. The run file states the corrected reading.
