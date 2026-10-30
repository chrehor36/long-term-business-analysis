import sys, os, re, json
sys.path.insert(0, os.path.abspath('tools'))
import sources

OUT = os.path.abspath(os.path.join('Test Runs', '_research 2026-09-19 GFF'))
CIK = '50725'

def strip(html):
    h = html
    h = re.sub(r'(?is)<script.*?</script>', ' ', h)
    h = re.sub(r'(?is)<style.*?</style>', ' ', h)
    h = re.sub(r'(?is)<br\s*/?>', '\n', h)
    h = re.sub(r'(?is)</(p|div|tr|h1|h2|h3|h4|li|table)>', '\n', h)
    h = re.sub(r'(?is)</t[dh]>', ' | ', h)
    h = re.sub(r'(?s)<[^>]+>', ' ', h)
    h = h.replace('&nbsp;', ' ').replace('&#160;', ' ').replace('&amp;', '&')
    h = h.replace('&#8217;', "'").replace('&#8220;', '"').replace('&#8221;', '"')
    h = h.replace('&#8212;', '--').replace('&#8211;', '-').replace('&#151;', '--')
    h = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))) if int(m.group(1)) < 65536 else ' ', h)
    h = re.sub(r'[ \t\xa0]+', ' ', h)
    h = re.sub(r'\n\s*\n\s*\n+', '\n\n', h)
    return h

DOCS = [
    ('tenk_FY2025', '0001628280-25-053242', 'gff-20250930.htm'),
    ('tenk_FY2024', '0000050725-24-000152', 'gff-20240930.htm'),
    ('tenk_FY2023', '0000050725-23-000055', 'gff-20230930.htm'),
    ('tenk_FY2022', '0000050725-22-000090', 'gff-20220930.htm'),
    ('tenk_FY2021', '0000050725-21-000068', 'gff-20210930.htm'),
    ('tenq_Q3FY2026', '0001628280-26-053536', 'gff-20260630.htm'),
    ('def14a_2026', '0000930413-26-000074', 'c114494_def14a-ixbrl.htm'),
    ('def14a_2025', '0000930413-25-000212', 'c110954_def14a-ixbrl.htm'),
]

for name, acc, doc in DOCS:
    path = os.path.join(OUT, name + '.txt')
    if os.path.exists(path) and os.path.getsize(path) > 10000:
        print('have', name); continue
    a = acc.replace('-', '')
    url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/%s' % (CIK, a, doc)
    try:
        raw = sources._get(url, headers=sources.SEC_UA, cache_name='gff_' + name)
        txt = strip(raw.decode('utf-8', 'replace') if isinstance(raw, bytes) else raw)
        open(path, 'w', encoding='utf-8').write(txt)
        print('wrote', name, len(txt))
    except Exception as e:
        print('FAIL', name, e)

# companyfacts
cf = os.path.join(OUT, 'companyfacts.json')
if not os.path.exists(cf):
    d = sources._get('https://data.sec.gov/api/xbrl/companyfacts/CIK0000050725.json', cache_name='gff_cf')
    open(cf, 'wb').write(d if isinstance(d, bytes) else d.encode())
    print('wrote companyfacts')
