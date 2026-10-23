# The run's own check: no E-ids; every M/L/R id in the v5 ledger; every quoted fragment beside an id is in that row.
import csv,re,sys,unicodedata
RUN='Test Runs/2026-10-23 Run - ES Eversource Energy.md'
rows={}
for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig')):
    rows[r['id']]=r['quote_verbatim']
txt=open(RUN,encoding='utf-8').read()
problems=0
eids=re.findall(r'\[E\d+-\d+\]',txt)
if eids: print('E-ids found:',eids); problems+=len(eids)
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',txt)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id',i); problems+=1
# quoted fragment immediately before an id: "..." **[ID]** (allow up to 3 ids chained by commas)
pat=re.compile(r'"([^"\n]{6,}?)"\s*(?:\([^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
def norm(s):
    return re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip()
n=0
flat=re.sub(r'\n\s*',' ',txt)
for m in pat.finditer(flat):
    frag,i=m.group(1),m.group(2); n+=1
    q=rows.get(i,'')
    parts=[p.strip() for p in frag.split('[...]')]
    ok=all(p in q for p in parts if p)
    okn=all(norm(p) in norm(q) for p in parts if p)
    if not ok:
        print(('NORMALISED-ONLY ' if okn else 'NOT IN ROW ')+i+': '+frag[:120]); problems+= 0 if okn else 1
print(f'ids cited: {len(set(ids))} distinct; fragments checked: {n}; problems: {problems}')
sys.exit(1 if problems else 0)
