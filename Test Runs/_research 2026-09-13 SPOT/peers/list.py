import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from edgar import recent_filings
for cik, forms in [(1744676, ('20-F',)), (908937, ('10-K',)), (2012807, ('10-K',)), (1319161, ('10-K',)), (320193,('10-K',)), (1652044,('10-K',)), (1018724,('10-K',))]:
    try:
        d = recent_filings(cik, forms=forms, n=8)
        print(cik, d['name'])
        for f in d['filings']:
            print(f"  {f['form']} report={f['reportDate']} filed={f['filingDate']} acc={f['accession']} {f['url']}")
    except Exception as e:
        print(cik, 'ERR', e)
