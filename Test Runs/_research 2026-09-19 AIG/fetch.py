import sys, os, re, html, json
sys.path.insert(0, os.path.abspath('tools'))
import sources
D = os.path.abspath('Test Runs/_research 2026-09-19 AIG')
CIK = '5272'

def strip(h):
    h = re.sub(r'(?is)<(script|style).*?</\1>', ' ', h)
    h = re.sub(r'(?is)<ix:header>.*?</ix:header>', ' ', h)
    h = re.sub(r'(?is)<br\s*/?>', '\n', h)
    h = re.sub(r'(?is)</(p|div|tr|h[1-6]|li)>', '\n', h)
    h = re.sub(r'(?is)</t[dh]>', ' | ', h)
    h = re.sub(r'(?s)<[^>]+>', '', h)
    h = html.unescape(h)
    h = re.sub(r'[ \t\xa0]+', ' ', h)
    h = re.sub(r'\n\s*\n\s*\n+', '\n\n', h)
    return h

def grab(acc, doc, out, cik=CIK):
    a = acc.replace('-', '')
    url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/%s' % (cik, a, doc)
    raw = sources._get(url, headers=sources.SEC_UA, cache_name='aig_'+out, max_age_h=999)
    if not isinstance(raw, str): raw = raw.decode('utf-8', 'replace')
    open(os.path.join(D, out), 'w', encoding='utf-8').write(strip(raw))
    print(out, len(raw))

def index(acc, cik=CIK):
    a = acc.replace('-', '')
    url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/' % (cik, a)
    raw = sources._get(url, headers=sources.SEC_UA, cache_name='aigidx_'+acc, max_age_h=999)
    if not isinstance(raw, str): raw = raw.decode('utf-8','replace')
    return sorted(set(re.findall(r'href="/Archives/edgar/data/\d+/\d+/([^"]+\.(?:htm|txt))"', raw)))

if __name__ == '__main__':
    what = sys.argv[1]
    if what == 'idx':
        for acc in sys.argv[2:]:
            print(acc, index(acc))
    elif what == 'grab':
        grab(sys.argv[2], sys.argv[3], sys.argv[4])
