# Check: no E-ids; every M/L/R id in the v5 ledger; every quoted fragment beside an id is in that row.
import csv,re,sys,unicodedata
rows={r[0]:r[2] for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
txt=open('Test Runs/2026-10-13 Run - MSM MSC Industrial Direct.md',encoding='utf-8').read()
bad=0
if re.search(r'\[E\d-\d+\]|\bE\d-\d\d\b',txt): print('E-id found'); bad+=1
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',txt)
for i in set(ids):
    if i not in rows: print('MISSING',i); bad+=1
def norm(s): return re.sub(r'\s+',' ',s).strip()
# fragments: "..." immediately followed (within 3 chars) by one or more ids
for m in re.finditer(r'"([^"]{3,})"((?:[ ,]*\*\*\[[MLR]\d{4}-\d{3}\]\*\*)+)',txt):
    frag=m.group(1); fids=re.findall(r'[MLR]\d{4}-\d{3}',m.group(2))
    parts=[p.strip() for p in frag.split('[...]') if p.strip()]
    ok=any(all(norm(p) in norm(rows.get(f,'')) for p in parts) for f in fids)
    if not ok: print('FRAGMENT NOT IN ROW',fids,repr(frag[:80])); bad+=1
print('ids:',len(set(ids)),'bad:',bad)
