import json, os, re, sys, time, urllib.request, urllib.error

UA = {'User-Agent': 'BRK research chrehor36@gmail.com', 'Accept-Encoding': 'gzip, deflate'}
BASE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(BASE, 'cache')
os.makedirs(CACHE, exist_ok=True)


def get(url, binary=False):
    key = re.sub(r'[^A-Za-z0-9._-]', '_', url)[-180:]
    path = os.path.join(CACHE, key)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            data = f.read()
        return data if binary else data.decode('utf-8', 'replace')
    req = urllib.request.Request(url, headers=UA)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read()
                if r.headers.get('Content-Encoding') == 'gzip':
                    import gzip
                    raw = gzip.decompress(raw)
            break
        except Exception as e:
            if attempt == 3:
                raise
            time.sleep(2 + attempt * 2)
    with open(path, 'wb') as f:
        f.write(raw)
    time.sleep(0.15)
    return raw if binary else raw.decode('utf-8', 'replace')


def submissions(cik):
    cik10 = str(cik).zfill(10)
    return json.loads(get(f'https://data.sec.gov/submissions/CIK{cik10}.json'))


def recent_filings(cik, forms=('10-K', '10-Q', '20-F'), n=40):
    s = submissions(cik)
    r = s['filings']['recent']
    out = []
    for i in range(len(r['form'])):
        if r['form'][i] in forms:
            out.append({
                'form': r['form'][i],
                'accession': r['accessionNumber'][i],
                'filingDate': r['filingDate'][i],
                'reportDate': r['reportDate'][i],
                'primaryDoc': r['primaryDocument'][i],
                'url': f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{r['accessionNumber'][i].replace('-','')}/{r['primaryDocument'][i]}",
            })
        if len(out) >= n:
            break
    return {'name': s.get('name'), 'filings': out}


def companyfacts(cik):
    cik10 = str(cik).zfill(10)
    return json.loads(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik10}.json'))


def strip_html(html):
    h = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', html)
    h = re.sub(r'(?i)<br[^>]*>', '\n', h)
    h = re.sub(r'(?i)</(p|div|tr|h[1-6]|li)>', '\n', h)
    h = re.sub(r'(?i)</t[dh]>', ' | ', h)
    h = re.sub(r'(?s)<[^>]+>', ' ', h)
    import html as _h
    h = _h.unescape(h)
    h = h.replace('\xa0', ' ').replace('’', "'").replace('“', '"').replace('”', '"')
    h = re.sub(r'[ \t]+', ' ', h)
    h = re.sub(r'\n\s*\n+', '\n', h)
    return h


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'filings':
        d = recent_filings(sys.argv[2], forms=tuple(sys.argv[3].split(',')) if len(sys.argv) > 3 else ('10-K', '10-Q', '20-F'))
        print(d['name'])
        for f in d['filings'][:20]:
            print(f"{f['form']:6} report={f['reportDate']} filed={f['filingDate']} acc={f['accession']}")
            print(f"       {f['url']}")
    elif cmd == 'text':
        out = strip_html(get(sys.argv[2]))
        dest = sys.argv[3]
        with open(dest, 'w', encoding='utf-8') as fh:
            fh.write(out)
        print(f'{dest}: {len(out)} chars, {out.count(chr(10))} lines')
