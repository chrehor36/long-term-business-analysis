# KGHI research notes, 2026-10-17
Run file copied from the template at the start, before any fetch.
Raw downloads go in cache/ (gitignored) and stay untracked.

## Sources found (raw copies in cache/, untracked)
- SEC EDGAR CIK 0000856200: last filings 2008-02-28 (8-K and Form 15). Accessions are listed in the run file.
- Company statements to stockholders, retrieved from Internet Archive captures of www.kaisergroup.com/docs/
  (2008-03-31 through 2012-09-30; annuals 2007-2010 are scanned images). 2011-2014 annuals, the 2015 meeting
  document and the "Kaiser Announcement" were listed by the company but never captured (archive returned 404).
- www.kaisergroup.com now belongs to KAISER GmbH & Co. KG (Germany), unrelated.
- OTC Markets: financial-report endpoint totalRecords 0; quote endpoints under maintenance on 2026-10-17.
- Price: TradingView 0.0001, no trades (aggregator).
- Treasury 30-year par yield 5.43% on 10/16/2026 (tools/sources.py).
## Scripts
- h2t.py strips filings to text; bs.py extracts balance sheets by position; seg.py prints a text segment;
  check_ids.py is the run's id and quote check.
