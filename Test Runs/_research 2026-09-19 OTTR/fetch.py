import sys, os, re, json, html
sys.path.insert(0, 'tools')
import sources

D = 'Test Runs/_research 2026-09-19 OTTR'
CIK = '1466593'


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


def get_doc(acc, doc, out):
    a = acc.replace('-', '')
    url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/%s' % (CIK, a, doc)
    raw = sources._get(url, headers=sources.SEC_UA)
    open(os.path.join(D, out), 'w', encoding='utf-8').write(strip(raw))
    print('wrote', out, os.path.getsize(os.path.join(D, out)))


def index(acc):
    a = acc.replace('-', '')
    url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/' % (CIK, a)
    raw = sources._get(url, headers=sources.SEC_UA)
    if isinstance(raw, bytes):
        raw = raw.decode('utf-8', 'ignore')
    return re.findall(r'href="[^"]*?/([^/"]+\.(?:htm|txt))"', raw)


if __name__ == '__main__':
    what = sys.argv[1]
    if what == 'cf':
        raw = sources._get('https://data.sec.gov/api/xbrl/companyfacts/CIK000%s.json' % CIK, headers=sources.SEC_UA)
        open(os.path.join(D, 'companyfacts.json'), 'wb').write(raw if isinstance(raw, bytes) else raw.encode())
        print('cf ok')
    elif what == 'idx':
        print(index(sys.argv[2]))
    else:
        get_doc(sys.argv[2], sys.argv[3], sys.argv[4])
