# Dispatcher's tight check: a quoted fragment followed within 40 characters by **[ID]** (or [ID, ID]) must be in that row.
import csv,re,sys
rows={}
with open('principle_ledger_v5.csv',encoding='utf-8') as f:
    r=csv.reader(f);next(r)
    for x in r: rows[x[0]]=' '.join(x)
norm=lambda s:re.sub(r'[^a-z0-9 ]','',re.sub(r'\s+',' ',s.replace('\u2019',"'")).lower()).strip()
txt=open(sys.argv[1],encoding='utf-8').read()
n=0;slip=0
for m in re.finditer(r'["\u201c]([^"\u201d]{4,}?)["\u201d][^"\u201c\n]{0,40}?\*\*\[([^\]]+)\]\*\*',txt):
    q,ids=m.group(1),re.findall(r'[MLR]\d{4}-\d{3}',m.group(2))
    if not ids: continue
    n+=1
    parts=[p for p in (norm(x) for x in re.split(r'\[\.\.\.\]|\.\.\.|\u2026',q)) if len(p)>=4]
    ok=all(any(p in norm(rows.get(i,'')) for i in ids) for p in parts)
    if not ok: slip+=1;print('SLIP?',ids,'|',q[:150].replace('\n',' '))
print('id-adjacent quotes',n,'unmatched',slip)
