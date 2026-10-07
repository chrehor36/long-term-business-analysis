"""Fetch Bloom Energy primary documents to text. CIK 1664703."""
import json, os, re, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import edgar

BASE = os.path.dirname(os.path.abspath(__file__))
CIK = 1664703

def full_filings(forms):
    s = edgar.submissions(CIK)
    r = s['filings']['recent']
    out = []
    for i in range(len(r['form'])):
        if r['form'][i] in forms:
            out.append({'form': r['form'][i], 'accession': r['accessionNumber'][i],
                        'filingDate': r['filingDate'][i], 'reportDate': r['reportDate'][i],
                        'primaryDoc': r['primaryDocument'][i]})
    # older filings live in the paginated files
    for f in s['filings'].get('files', []):
        d = json.loads(edgar.get('https://data.sec.gov/submissions/' + f['name']))
        for i in range(len(d['form'])):
            if d['form'][i] in forms:
                out.append({'form': d['form'][i], 'accession': d['accessionNumber'][i],
                            'filingDate': d['filingDate'][i], 'reportDate': d['reportDate'][i],
                            'primaryDoc': d['primaryDocument'][i]})
    return out

def url(f):
    return f"https://www.sec.gov/Archives/edgar/data/{CIK}/{f['accession'].replace('-','')}/{f['primaryDoc']}"

def dump(f, name):
    dest = os.path.join(BASE, name)
    if os.path.exists(dest):
        print('exists', name); return
    for attempt in range(6):
        try:
            txt = edgar.strip_html(edgar.get(url(f)))
            break
        except Exception as e:
            print('retry', name, e); time.sleep(5 + 5*attempt)
    else:
        print('FAILED', name); return
    with open(dest, 'w', encoding='utf-8') as fh:
        fh.write(f"SOURCE: {f['form']} report={f['reportDate']} filed={f['filingDate']} acc={f['accession']}\nURL: {url(f)}\n\n")
        fh.write(txt)
    print('wrote', name, len(txt))

def index_docs(f):
    """List documents in a filing (for EX-99.1)."""
    acc = f['accession'].replace('-','')
    idx = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc}/index.json"
    for attempt in range(4):
        try:
            d = json.loads(edgar.get(idx)); break
        except Exception as e:
            print('idx retry', f['filingDate'], e); time.sleep(4+4*attempt)
    else:
        return []
    return [(f"/Archives/edgar/data/{CIK}/{acc}/{it['name']}", it['name']) for it in d['directory']['item']]

if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'list'
    fl = full_filings(('10-K', '10-Q', '10-K/A', '10-Q/A', '8-K', 'DEF 14A', 'S-1', 'S-1/A', '424B4'))
    if what == 'list':
        for f in fl:
            print(f"{f['form']:8} report={f['reportDate']} filed={f['filingDate']} acc={f['accession']} {f['primaryDoc']}")
    elif what == 'tenk':
        for f in fl:
            if f['form'] == '10-K':
                dump(f, f"BE_10K_FY{f['reportDate'][:4]}.txt")
    elif what == 'tenq':
        for f in fl:
            if f['form'] in ('10-Q', '10-Q/A') and f['reportDate'] >= '2025-06-30':
                tag = 'A' if f['form'].endswith('/A') else ''
                dump(f, f"BE_10Q{tag}_{f['reportDate']}.txt")
    elif what == 'proxy':
        for f in fl:
            if f['form'] == 'DEF 14A' and f['filingDate'] >= '2024-01-01':
                dump(f, f"BE_DEF14A_{f['filingDate']}.txt")
    elif what == 'eightk':
        # earnings-release 8-Ks: dump EX-99.1 for the last several
        for f in fl:
            if f['form'] == '8-K' and f['filingDate'] >= '2025-02-01':
                docs = index_docs(f)
                for full, nm in docs:
                    if re.search(r'ex[-_]?99', nm, re.I) and nm.endswith('.htm'):
                        dest = os.path.join(BASE, f"BE_8K_{f['filingDate']}_{nm}.txt")
                        if os.path.exists(dest): continue
                        try:
                            txt = edgar.strip_html(edgar.get('https://www.sec.gov' + full))
                        except Exception as e:
                            print('fail', nm, e); continue
                        with open(dest, 'w', encoding='utf-8') as fh:
                            fh.write(f"SOURCE: 8-K filed={f['filingDate']} acc={f['accession']} doc={nm}\n\n" + txt)
                        print('wrote', dest, len(txt))
    elif what == 'facts':
        d = edgar.companyfacts(CIK)
        with open(os.path.join(BASE, 'BE_companyfacts.json'), 'w') as fh:
            json.dump(d, fh)
        print('facts written')
    elif what == 's1':
        for f in fl:
            if f['form'] in ('424B4',):
                dump(f, f"BE_{f['form'].replace('/','')}_{f['filingDate']}.txt")
