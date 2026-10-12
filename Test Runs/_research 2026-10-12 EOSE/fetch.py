import sys, os, time, json, urllib.request, gzip, re, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
def get(url, name=None):
    name = name or re.sub(r'[^A-Za-z0-9._-]', '_', url.split('/')[-1] or 'idx')
    p = os.path.join(CACHE, name)
    if os.path.exists(p):
        return open(p, 'rb').read()
    req = urllib.request.Request(url, headers=UA)
    for i in range(4):
        try:
            r = urllib.request.urlopen(req, timeout=60); d = r.read()
            if r.headers.get('Content-Encoding') == 'gzip': d = gzip.decompress(d)
            open(p, 'wb').write(d); time.sleep(0.15); return d
        except Exception as e:
            print('retry', e, file=sys.stderr); time.sleep(2)
    raise SystemExit('fail ' + url)
def text(b):
    s = b.decode('utf-8', 'ignore')
    s = re.sub(r'(?is)<(script|style).*?</\1>', ' ', s)
    s = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>', '\n', s)
    s = re.sub(r'(?i)</td>', ' | ', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    s = re.sub(r'[ \t\xa0]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    return s
if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'subs':
        cik = sys.argv[2]
        d = json.loads(get(f'https://data.sec.gov/submissions/CIK{int(cik):010d}.json', f'subs_{cik}.json'))
        r = d['filings']['recent']
        for i in range(len(r['form'])):
            if len(sys.argv) > 3 and r['form'][i] not in sys.argv[3].split(','): continue
            print(r['filingDate'][i], r['form'][i], r['accessionNumber'][i], r['primaryDocument'][i], r.get('items',[''])[i] if 'items' in r else '')
    elif cmd == 'doc':
        cik, acc, doc, out = sys.argv[2:6]
        url = f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}'
        b = get(url, acc + '_' + doc)
        open(os.path.join(CACHE, out), 'w', encoding='utf-8').write(text(b))
        print('wrote', out, len(b))
    elif cmd == 'idx':
        cik, acc = sys.argv[2:4]
        url = f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/index.json'
        d = json.loads(get(url, acc + '_index.json'))
        for it in d['directory']['item']: print(it['name'], it.get('size'))
