import sys, os, re, html, json
ROOT = r'C:\Users\chreh\OneDrive\Documents\BRK'
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import sources
D = os.path.join(ROOT, 'Test Runs', '_research 2026-09-19 DIS', 'peers')
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

def subs(tk):
    cik, name = sources.cik_for(tk)
    txt = sources._get('https://data.sec.gov/submissions/CIK%s.json' % cik,
                       sources.SEC_UA, 'subs_%s.json' % tk, max_age_h=168)
    return cik, json.loads(txt), name

def filings(tk, forms=('10-K',), n=5):
    cik, d, name = subs(tk)
    r = d['filings']['recent']
    out = []
    for i in range(len(r['accessionNumber'])):
        if r['form'][i] in forms:
            out.append(dict(acc=r['accessionNumber'][i], form=r['form'][i],
                            date=r['filingDate'][i], rep=r['reportDate'][i],
                            doc=r['primaryDocument'][i], desc=r['primaryDocDescription'][i]))
        if len(out) >= n:
            break
    return cik, out, name

def grab(cik, acc, doc, out, maxage=999):
    a = acc.replace('-', '')
    url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/%s' % (int(cik), a, doc)
    raw = sources._get(url, headers=sources.SEC_UA, cache_name='pf_' + out, max_age_h=maxage)
    p = os.path.join(D, out)
    open(p, 'w', encoding='utf-8').write(strip(raw))
    print(out, len(raw), '->', os.path.getsize(p))
    return p

if __name__ == '__main__':
    for tk in sys.argv[1:]:
        cik, fl, name = filings(tk)
        print('==', tk, 'CIK', cik, name)
        for f in fl:
            print('  ', f['form'], f['date'], 'rep', f['rep'], f['acc'], f['doc'])
