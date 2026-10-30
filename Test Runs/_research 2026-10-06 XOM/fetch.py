"""Fetch EDGAR documents into cache/ (gitignored) and write a stripped .txt beside each.
Usage: fetch.py CIK ACCESSION PRIMARYDOC OUTNAME   (or: fetch.py index CIK ACCESSION to list the filing's files)
Batch: fetch.py batch  (fetches the list in BATCH below)"""
import sys, os, re, time, html, urllib.request, urllib.error, json
UA = {"User-Agent": "Chris Hrehor research chrehor36@gmail.com"}
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache')
os.makedirs(D, exist_ok=True)


def get(url):
    for k in range(8):
        time.sleep(0.5 + 5 * k)
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
    raise RuntimeError('429 persisted: ' + url)


def strip(b):
    t = b.decode('utf-8', 'replace')
    t = re.sub(r'(?is)<(script|style).*?</\1>', ' ', t)
    t = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>', '\n', t)
    t = re.sub(r'(?i)</td>', ' | ', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t).replace('\xa0', ' ')
    t = re.sub(r'[ \t]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n', t)
    return t


def fetch(cik, acc, doc, out):
    b = get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-", "")}/{doc}')
    open(os.path.join(D, out + '.htm'), 'wb').write(b)
    open(os.path.join(D, out + '.txt'), 'w', encoding='utf-8').write(strip(b))
    print(out, len(b))


def index(cik, acc):
    j = json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-", "")}/index.json'))
    for it in j['directory']['item']:
        print(it['name'], it.get('size'))


BATCH = [
    (34088, '0000034088-26-000045', 'xom-20251231.htm', '10k2025'),
    (34088, '0000034088-26-000093', 'xom-20260630.htm', '10q2026q2'),
    (34088, '0001193125-26-147614', 'd16317ddef14a.htm', 'def14a2026'),
    (2115436, '0002115436-26-000006', 'xom-20260731.htm', '8k20260731'),
    (2115436, '0001193125-26-291990', 'd71068d8k12b.htm', '8k12b'),
]

if __name__ == '__main__':
    if sys.argv[1] == 'index':
        index(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'batch':
        for row in BATCH:
            fetch(*row)
    else:
        fetch(*sys.argv[1:5])
