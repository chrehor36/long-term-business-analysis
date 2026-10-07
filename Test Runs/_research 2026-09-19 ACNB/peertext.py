import sys, os, re, json, urllib.request, html as H
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
PEERS = {
    'ORRF': '826154', 'MPB': '879635', 'FRAF': '723646', 'CZNC': '810958',
    'NWFL': '1013272', 'SHBI': '1035092', 'FULT': '700564', 'PFIS': '1056943',
    'FKYS': '737875', 'CZFS': '739421',
}

def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA)).read()

def strip(raw):
    s = raw.decode('utf-8', 'ignore')
    s = re.sub(r'(?is)<(script|style).*?</\1>', ' ', s)
    s = re.sub(r'(?is)<br\s*/?>', '\n', s)
    s = re.sub(r'(?is)</(p|div|tr|h1|h2|h3|li|table)>', '\n', s)
    s = re.sub(r'(?is)</t[dh]>', ' | ', s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    s = H.unescape(s)
    s = re.sub(r'[ \t\xa0]+', ' ', s)
    return re.sub(r'\n\s*\n+', '\n', s)

for t, cik in PEERS.items():
    out = f'peer_{t}_tenk.txt'
    if os.path.exists(out):
        print('have', out); continue
    sub = json.loads(get(f'https://data.sec.gov/submissions/CIK{cik.zfill(10)}.json'))
    f = sub['filings']['recent']
    best = None
    for form, fd, acc, prim, rd in zip(f['form'], f['filingDate'], f['accessionNumber'],
                                        f['primaryDocument'], f['reportDate']):
        if form == '10-K':
            best = (acc, prim, rd); break
    if not best:
        print('NO 10-K', t); continue
    acc, prim, rd = best
    a = acc.replace('-', '')
    raw = get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{prim}')
    open(out, 'w', encoding='utf-8').write(strip(raw))
    print(t, 'acc', acc, 'period', rd, os.path.getsize(out))
