"""Fetch AMBQ filings from SEC EDGAR into cache/ and strip each to text (cache/ is gitignored)."""
import sys, re, html, os, time, urllib.request
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
CIK = "1500412"
OUT = sys.argv[1]
def strip(raw):
    t = re.sub(r'(?is)<(script|style).*?</\1>', ' ', raw)
    t = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>', '\n', t)
    t = re.sub(r'(?i)</td>', ' | ', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    t = re.sub(r'[ \t\xa0]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n', t)
    return t
for spec in sys.argv[2:]:
    name, acc, doc = spec.split(',')
    url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-','')}/{doc}"
    dst = os.path.join(OUT, name + '.htm')
    if not os.path.exists(dst):
        req = urllib.request.Request(url, headers=UA)
        data = urllib.request.urlopen(req, timeout=60).read()
        open(dst, 'wb').write(data)
        time.sleep(0.3)
    raw = open(dst, 'rb').read().decode('utf-8', 'replace')
    open(os.path.join(OUT, name + '.txt'), 'w', encoding='utf-8').write(strip(raw))
    print(name, url, os.path.getsize(dst))
