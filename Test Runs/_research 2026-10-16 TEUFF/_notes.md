# TEUFF research notes

2026-10-16: template copied before any fetch (commit e5c0725f).

## Fetches (2026-10-16)
- SEC submissions JSON, CIK 0001504795: last filings 2018-04-20 (6-K 0001615774-18-002774, 8-A12B/A 0001615774-18-002777,
  Form 15-12B 0001615774-18-002778). No company filing after 2018-04-20. Delisting notice 25-NSE 0000876661-15-000631 (2015-12-15).
- Documents read (raw HTML in cache/, gitignored): 20-F FY2016 0001615774-17-001018 (2017-03-13); 20-F/A 0001615774-17-001086
  (2017-03-16, filed solely to add the auditor's name and signature to the audit report); 20-F FY2015 0001615774-16-005107;
  20-F FY2014 0000919574-15-003118; 20-F FY2013 0000919574-14-002363; 20-F FY2012 0000919574-13-002244; 20-F FY2011
  0001193125-12-119758; 6-Ks of 2017-04-19, 05-31, 06-15, 06-23, 07-14, 07-17, 12-27, 2018-03-09, 2018-04-20.
- tools/run.py TEUFF: "not an SEC filer" (ticker not in the live ticker file). Screens/cover_shares.py TEUFF: "NOT AN SEC
  REGISTRANT in the live ticker file". Figures taken by hand from the filed documents (operator rule 4).
- tools/sources.py: USD 30-year 5.43%, US Treasury daily par yield curve, 10/15/2026.
- Price, aggregator (Yahoo chart API via tools/sources.py `_chart`), FLAGGED: TEUFF, OTC Markets OTCPK, close 2026-10-15
  $0.00001 (volume 0); last day with any volume 2026-03-13, 423 shares at $0.00001; 52-week high $0.0001; regularMarketPrice
  field prints 0.0. Split 1:50 effective 2017-01-31 (matches the 20-F).
- Company website www.box-ships.com: no response 2026-10-16; Wayback capture 2023-03-20 shows an empty "Index of /" (cgi-bin
  only); earlier captures (2018-2020) returned empty bodies to the fetch. No later primary document found.
- OTC Markets profile API: response not JSON (blocked); not used.

## Literal five-year window, owner cash = CFO less all capital spending (USD)
| FY | CFO | capex (vessels, improvements, other fixed) | owner cash |
|---|---|---|---|
| 2012 | 32,531,933 | 62,420,555 | -29,888,622 |
| 2013 | 38,197,504 | 0 | 38,197,504 |
| 2014 | 19,822,381 | 0 | 19,822,381 |
| 2015 | 13,213,612 | 0 | 13,213,612 |
| 2016 | -9,299,923 | 134,140 | -9,434,063 |
Sources: FY2013 20-F cash flow statement (FY2012, FY2013); FY2016 20-F cash flow statement (FY2014 to FY2016).
