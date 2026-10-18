"""Fetch EDGAR filings for the NJR run; store raw in cache/ (gitignored). Text stripped beside it."""
import sys, os, json, time, re, requests
from bs4 import BeautifulSoup
H = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cache")
def get(url, fn=None):
    p = os.path.join(BASE, fn or re.sub(r'[^A-Za-z0-9._-]', '_', url.split('/')[-1]))
    if os.path.exists(p):
        return open(p, 'rb').read()
    for i in range(5):
        r = requests.get(url, headers=H, timeout=60)
        if r.status_code == 200:
            open(p, 'wb').write(r.content); time.sleep(0.2); return r.content
        time.sleep(2)
    raise SystemExit(f"fail {url} {r.status_code}")
def totext(raw, out):
    s = BeautifulSoup(raw, 'lxml')
    for t in s(['script','style']): t.decompose()
    txt = s.get_text('\n')
    txt = re.sub(r'\n\s*\n+', '\n', txt)
    open(os.path.join(BASE, out), 'w', encoding='utf-8').write(txt)
    return txt
if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'subs':
        cik = sys.argv[2].zfill(10)
        d = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik}.json", f"subs_{cik}.json"))
        f = d['filings']['recent']
        forms = sys.argv[3].split(',') if len(sys.argv) > 3 else None
        for i in range(len(f['form'])):
            if forms is None or f['form'][i] in forms:
                print(f['form'][i], f['filingDate'][i], f['accessionNumber'][i], f['primaryDocument'][i], f['reportDate'][i], (f.get('items') or ['']*9999)[i])
    elif cmd == 'doc':
        cik, acc, doc, out = sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
        url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
        raw = get(url, out + '.htm')
        t = totext(raw, out + '.txt'); print(len(t))
    elif cmd == 'facts':
        cik = sys.argv[2].zfill(10)
        get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json", f"facts_{cik}.json"); print('ok')
