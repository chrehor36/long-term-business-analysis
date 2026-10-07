"""Fetch peer annual filings (10-K / 20-F / 40-F) to text dumps for the BE run."""
import json, os, re, sys, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import edgar

BASE = os.path.dirname(os.path.abspath(__file__))
ANNUAL = ('10-K', '20-F', '40-F', '10-K/A', '20-F/A', '40-F/A')

TICKERS = ['CAT', 'GEV', 'CMI', 'FCEL', 'PLUG', 'BLDP', 'GNRC']

def cik_map():
    d = json.loads(edgar.get('https://www.sec.gov/files/company_tickers.json'))
    return {v['ticker'].upper(): (v['cik_str'], v['title']) for v in d.values()}

def annuals(cik):
    s = edgar.submissions(cik)
    r = s['filings']['recent']
    out = []
    for i in range(len(r['form'])):
        if r['form'][i] in ANNUAL:
            out.append({'form': r['form'][i], 'accession': r['accessionNumber'][i],
                        'filingDate': r['filingDate'][i], 'reportDate': r['reportDate'][i],
                        'primaryDoc': r['primaryDocument'][i]})
    return s.get('name'), out

def url(cik, f):
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{f['accession'].replace('-','')}/{f['primaryDoc']}"

def index_docs(cik, f):
    acc = f['accession'].replace('-', '')
    d = json.loads(edgar.get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc}/index.json"))
    return [it['name'] for it in d['directory']['item']]

if __name__ == '__main__':
    cm = cik_map()
    for t in TICKERS:
        if t not in cm:
            print(f'{t}: NOT IN TICKER MAP'); continue
        cik, title = cm[t]
        try:
            name, fl = annuals(cik)
        except Exception as e:
            print(f'{t}: submissions FAILED {e}'); continue
        if not fl:
            print(f'{t} ({title} cik={cik}): no annual forms in recent'); continue
        fl.sort(key=lambda x: x['filingDate'], reverse=True)
        f = fl[0]
        print(f"{t} cik={cik} {name} :: {f['form']} report={f['reportDate']} filed={f['filingDate']} acc={f['accession']} doc={f['primaryDoc']}")
        dest = os.path.join(BASE, f"{t}_{f['form'].replace('/','')}_{f['reportDate']}.txt")
        if os.path.exists(dest):
            print('  exists'); continue
        u = url(cik, f)
        try:
            txt = edgar.strip_html(edgar.get(u))
        except Exception as e:
            print(f'  FETCH FAILED {u}: {e}'); continue
        with open(dest, 'w', encoding='utf-8') as fh:
            fh.write(f"SOURCE: {t} {f['form']} report={f['reportDate']} filed={f['filingDate']} acc={f['accession']}\nURL: {u}\n\n")
            fh.write(txt)
        print(f'  wrote {os.path.basename(dest)} {len(txt)} chars')
        # also list all docs in the filing, for exhibit-borne 40-F content
        try:
            docs = index_docs(cik, f)
            with open(os.path.join(BASE, f'{t}_docs.txt'), 'w', encoding='utf-8') as fh:
                fh.write('\n'.join(docs))
        except Exception as e:
            print(f'  index failed: {e}')
