import sys, os, json, re, time
sys.path.insert(0, os.path.abspath('tools'))
import sources
from sources import SEC_UA, _get

OUT = os.path.abspath('Test Runs/_research 2026-09-19 TFC')
CIK = '0000092230'

def save(name, txt):
    p = os.path.join(OUT, name)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(txt)
    print('wrote', name, len(txt))

sub = _get(f'https://data.sec.gov/submissions/CIK{CIK}.json', SEC_UA, f'sub_{CIK}.json', max_age_h=6)
save('submissions.json', sub)
j = json.loads(sub)
r = j['filings']['recent']
rows = list(zip(r['form'], r['filingDate'], r['reportDate'], r['accessionNumber'], r['primaryDocument']))
for f in ('10-K','10-Q','DEF 14A','8-K'):
    sel = [x for x in rows if x[0]==f][:16]
    print('---', f)
    for x in sel: print(x)
print('name:', j.get('name'), 'formerNames:', j.get('formerNames'))
