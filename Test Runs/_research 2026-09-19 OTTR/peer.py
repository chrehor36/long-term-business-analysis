import sys, os, re, json, html
sys.path.insert(0, 'tools')
import sources

D = 'Test Runs/_research 2026-09-19 OTTR/peers'
os.makedirs(D, exist_ok=True)


def strip(raw):
    if isinstance(raw, bytes):
        raw = raw.decode('utf-8', 'ignore')
    raw = re.sub(r'(?is)<script.*?</script>', ' ', raw)
    raw = re.sub(r'(?is)<style.*?</style>', ' ', raw)
    raw = re.sub(r'(?is)<(br|/p|/div|/tr|/h[1-6])\s*/?>', '\n', raw)
    raw = re.sub(r'(?is)</t[dh]>', ' | ', raw)
    raw = re.sub(r'(?s)<[^>]+>', '', raw)
    raw = html.unescape(raw)
    raw = re.sub(r'[ \t\xa0]+', ' ', raw)
    raw = re.sub(r'\n\s*\n+', '\n', raw)
    return raw


def tenks(cik, n=2):
    cik10 = cik.zfill(10)
    j = json.loads(sources._get('https://data.sec.gov/submissions/CIK%s.json' % cik10, headers=sources.SEC_UA))
    r = j['filings']['recent']
    out = []
    for i in range(len(r['form'])):
        if r['form'][i] == '10-K':
            out.append((r['filingDate'][i], r['accessionNumber'][i], r['primaryDocument'][i]))
        if len(out) >= n:
            break
    return j['name'], out


def grab(tick, cik, n=2):
    name, ks = tenks(cik, n)
    print(tick, name)
    for fd, acc, doc in ks:
        a = acc.replace('-', '')
        url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/%s' % (int(cik), a, doc)
        try:
            raw = sources._get(url, headers=sources.SEC_UA)
        except Exception as e:
            print('  fail', acc, e)
            continue
        out = '%s/%s_tenk_%s.txt' % (D, tick, fd)
        open(out, 'w', encoding='utf-8').write(strip(raw))
        print('  ', fd, acc, os.path.getsize(out))


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        t, c = arg.split(':')
        n = 2
        if ',' in c:
            c, n = c.split(',')
            n = int(n)
        grab(t, c, n)
