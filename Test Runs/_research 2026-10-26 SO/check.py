# Check: no E-ids; every M/L/R id in the v5 CSV; every quoted fragment beside an id is in that row.
import csv,re,sys,unicodedata
ROOT='C:/Projects/BRK/'
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open(ROOT+'principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open(ROOT+'Test Runs/2026-10-26 Run - SO Southern Company.md',encoding='utf-8').read()
bad=0
for e in re.findall(r'\[E\d+-\d+\]',t): print('E-id',e);bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING',i);bad+=1
def norm(s): return re.sub(r'\s+',' ',s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"')).strip()
# fragment pairs: a quoted string immediately followed (within 12 chars) by one or more ids
pairs=0
for m in re.finditer(r'"([^"]{6,})"\s*(?:\([^)]*\))?\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,\s]*)+)',t):
    frag=m.group(1); fid=re.findall(r'[MLR]\d{4}-\d{3}',m.group(2))
    parts=[p.strip(' .,;') for p in frag.split('[...]')]
    ok=any(all(norm(p) in norm(rows.get(i,'')) for p in parts if p) for i in fid)
    pairs+=1
    if not ok: print('NOT IN ROW',fid,'|',frag[:120]);bad+=1
print('ids',len(set(ids)),'pairs',pairs,'problems',bad)
