import sys, os, re, html, json
sys.path.insert(0, os.path.abspath('tools'))
import sources
D = os.path.abspath('Test Runs/_research 2026-09-19 DIS/peers')
os.makedirs(D, exist_ok=True)

def strip(h):
    h = re.sub(r'(?is)<(script|style).*?</\1>', ' ', h)
    h = re.sub(r'(?is)<br\s*/?>', '\n', h)
    h = re.sub(r'(?is)</(p|div|tr|h[1-6]|li)>', '\n', h)
    h = re.sub(r'(?is)</t[dh]>', ' | ', h)
    h = re.sub(r'(?s)<[^>]+>', '', h)
    h = html.unescape(h)
    h = re.sub(r'[ \t\xa0]+', ' ', h)
    h = re.sub(r'\n\s*\n\s*\n+', '\n\n', h)
    return h

def subs(cik):
    c = str(cik).zfill(10)
    t = sources._get('https://data.sec.gov/submissions/CIK%s.json' % c,
                     headers=sources.SEC_UA, cache_name='subs_%s' % c, max_age_h=999)
    return json.loads(t)

def listfilings(cik, forms=('10-K',), n=8):
    d = subs(cik)
    r = d['filings']['recent']
    out = []
    for i in range(len(r['accessionNumber'])):
        if r['form'][i] in forms:
            out.append((r['form'][i], r['filingDate'][i], r['reportDate'][i],
                        r['accessionNumber'][i], r['primaryDocument'][i]))
            if len(out) >= n:
                break
    return d.get('name'), out

def grab(cik, acc, doc, out):
    a = acc.replace('-', '')
    url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/%s' % (int(cik), a, doc)
    raw = sources._get(url, headers=sources.SEC_UA, cache_name='pf_' + out, max_age_h=999)
    p = os.path.join(D, out)
    open(p, 'w', encoding='utf-8').write(strip(raw))
    print('WROTE', out, len(raw))
    return p

if __name__ == '__main__':
    for t in ['NFLX', 'CMCSA', 'WBD', 'PARA', 'PSKY', 'AAPL', 'AMZN']:
        try:
            cik = sources.cik_for(t)
            nm, fl = listfilings(cik)
            print('===', t, cik, nm)
            for f in fl:
                print('   ', f)
        except Exception as e:
            print('===', t, 'ERR', e)
