import sys, os, re, json
sys.path.insert(0, os.path.abspath('tools'))
import sources
sys.path.insert(0, os.path.abspath(os.path.join('Test Runs', '_research 2026-09-19 GFF')))
from fetch import strip

OUT = os.path.abspath(os.path.join('Test Runs', '_research 2026-09-19 GFF'))
CIK = '50725'

DOCS = [
    ('ex991_Q3FY2026', '0001628280-26-052927', 'gffq32026exhibit991.htm'),
    ('ex991_Q2FY2026', '0001628280-26-031705', 'gffq22026exhibit991.htm'),
    ('recast_FY2025',  '0001628280-26-054906', 'gff-20260807_d2.htm'),
    ('recast_cover',   '0001628280-26-054906', 'gff-20260807.htm'),
    ('launch_pr',      '0001628280-26-055203', 'griffonlaunchpressrelease.htm'),
    ('k8_feb18',       '0001628280-26-009094', 'gff-20260218.htm'),
]

for name, acc, doc in DOCS:
    path = os.path.join(OUT, name + '.txt')
    if os.path.exists(path) and os.path.getsize(path) > 2000:
        print('have', name); continue
    a = acc.replace('-', '')
    url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/%s' % (CIK, a, doc)
    try:
        raw = sources._get(url, headers=sources.SEC_UA, cache_name='gff2_' + name)
        txt = strip(raw.decode('utf-8', 'replace') if isinstance(raw, bytes) else raw)
        open(path, 'w', encoding='utf-8').write(txt)
        print('wrote', name, len(txt))
    except Exception as e:
        print('FAIL', name, e)

# list all 8-K filings 2026 with their items, to find the Feb 5 JV announcement
d = sources._get('https://data.sec.gov/submissions/CIK0000050725.json', cache_name='gff_sub')
j = json.loads(d)
r = j['filings']['recent']
print('--- 8-Ks in 2026 ---')
for form, date, acc, items in zip(r['form'], r['filingDate'], r['accessionNumber'], r['items']):
    if form == '8-K' and date >= '2025-10-01':
        print(date, acc, items)
