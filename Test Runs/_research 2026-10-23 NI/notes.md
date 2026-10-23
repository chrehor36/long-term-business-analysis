# NI run notes 2026-10-23
Started; template copied before any fetch.
- Fetched EDGAR filings into cache/ (gitignored) with fetch.py; XBRL via xb.py; peers via peers.py (ATO, OGS, CNP: a CONVENTION of the run, the 10-K names no rival).
- run.py's d3 "debt" column is total capitalization (CapitalizationLongtermDebtAndEquity); debt recomputed.
- Q1-Q4 written and committed together (IN, IN, weighing, weighing against).
- Q5 IN (argued both ways), Q6 weighs against, Q7 OUT: range $29.20-$32.83 equity-only vs $43.69; fair $12.17 equity-only, -$25.93 all-equity. check_framework PASS.
