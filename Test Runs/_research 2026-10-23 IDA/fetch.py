import sys, os, json, time, urllib.request, gzip, re, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
def get(url):
    fn = os.path.join(CACHE, re.sub(r'[^A-Za-z0-9._-]', '_', url)[-180:])
    if os.path.exists(fn):
        return open(fn, 'rb').read()
    req = urllib.request.Request(url, headers=UA)
    for i in range(5):
        try:
            r = urllib.request.urlopen(req, timeout=60); d = r.read()
            if r.headers.get('Content-Encoding') == 'gzip': d = gzip.decompress(d)
            open(fn, 'wb').write(d); time.sleep(0.3); return d
        except Exception as e:
            print("retry", e, file=sys.stderr); time.sleep(3)
    raise SystemExit("failed " + url)
def text(url):
    d = get(url).decode('utf-8', 'replace')
    d = re.sub(r'(?is)<(script|style).*?</\1>', ' ', d)
    d = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>', '\n', d)
    d = re.sub(r'(?i)</t[dh]>', ' | ', d)
    d = re.sub(r'<[^>]+>', ' ', d)
    d = html.unescape(d).replace('\xa0', ' ')
    d = re.sub(r'[ \t]+', ' ', d); d = re.sub(r'\n\s*\n+', '\n', d)
    return d
if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'subs':
        j = json.loads(get("https://data.sec.gov/submissions/CIK0001057877.json"))
        r = j['filings']['recent']
        for i in range(len(r['form'])):
            if r['form'][i] in sys.argv[2].split(','):
                print(r['filingDate'][i], r['form'][i], r['accessionNumber'][i], r['primaryDocument'][i], r.get('items',[''])[i] if 'items' in r else '')
    elif cmd == 'doc':
        acc, doc, out = sys.argv[2], sys.argv[3], sys.argv[4]
        url = "https://www.sec.gov/Archives/edgar/data/1057877/%s/%s" % (acc.replace('-', ''), doc)
        t = text(url); open(os.path.join(CACHE, out), 'w', encoding='utf-8').write(t); print(len(t))
    elif cmd == 'index':
        acc = sys.argv[2]
        url = "https://www.sec.gov/Archives/edgar/data/1057877/%s/index.json" % acc.replace('-', '')
        j = json.loads(get(url))
        for it in j['directory']['item']: print(it['name'], it.get('size'))
