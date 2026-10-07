import sys, io, json, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from edgar import submissions, get, strip_html
cik = int(sys.argv[1]); since = sys.argv[2]; until = sys.argv[3]
s = submissions(cik); r = s['filings']['recent']
for i in range(len(r['form'])):
    if r['form'][i]=='8-K' and since <= r['filingDate'][i] <= until:
        acc = r['accessionNumber'][i]; nod = acc.replace('-','')
        idx = get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{nod}/{acc}-index.htm")
        docs = re.findall(r'href="(/Archives/edgar/data/[^"]+)"[^>]*>([^<]+)</a>\s*</td>\s*<td[^>]*>([^<]*)</td>', idx)
        print(r['filingDate'][i], acc, r['items'][i] if 'items' in r else '', [(d[1], d[2]) for d in docs][:6])
