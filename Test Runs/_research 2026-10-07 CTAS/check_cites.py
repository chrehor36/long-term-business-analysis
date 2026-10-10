# Citation check for the CTAS run: no E-ids; every M/L/R id in the v5 ledger; every quoted fragment that stands
# immediately before an id (up to two ids later in the same sentence) is found in that row (normalized quotes/dashes/space).
import csv,re,sys,unicodedata
f=sys.argv[1] if len(sys.argv)>1 else r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-07 Run - CTAS Cintas.md'
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open(r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv',encoding='utf-8-sig'))}
def norm(s):
    s=s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"').replace('\u2014','-').replace('\u2013','-')
    s=s.replace('\ufffd','')
    return re.sub(r'\s+',' ',s).strip().lower()
t=open(f,encoding='utf-8').read()
bad=0
if re.search(r'\[E\d',t): print('E-id present'); bad+=1
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING',i); bad+=1
flat=re.sub(r'\s+',' ',t)
n=0
for m in re.finditer(r'"([^"]{6,400}?)"((?:[^"*]{0,40}?)\*\*\[([MLR]\d{4}-\d{3})\]\*\*(?:, \*\*\[([MLR]\d{4}-\d{3})\]\*\*)?)',flat):
    frag=m.group(1); cands=[x for x in (m.group(3),m.group(4)) if x]
    pieces=[p.strip() for p in re.split(r'\[\.\.\.\]',frag) if p.strip()]
    ok=any(all(norm(p) in norm(rows.get(c,'')) for p in pieces) for c in cands)
    n+=1
    if not ok: print('FRAGMENT NOT IN ROW',cands,'::',frag[:120]); bad+=1
print('ids',len(set(ids)),'fragments checked',n,'problems',bad)
