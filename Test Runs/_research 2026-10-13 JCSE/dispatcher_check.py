# Dispatcher's citation check (overnight 2026-10-13): every quoted fragment, straight or curly quotes,
# followed by one or more v5 ids, must appear in one of those rows' quote text. Usage: python -I dispatcher_check.py
import csv,re,sys
sys.stdout.reconfigure(encoding='utf-8')
root='C:/Users/chreh/OneDrive/Documents/BRK/'
run=open(root+'Test Runs/2026-10-13 Run - JCSE JE Cleantech Holdings.md',encoding='utf-8').read()
rows={}
with open(root+'principle_ledger_v5.csv',encoding='utf-8-sig') as f:
    r=csv.DictReader(f)
    for row in r: rows[row['id']]=row['quote_verbatim']
def norm(x):
    x=x.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"').replace('\u2014','--')
    return re.sub(r'\s+',' ',x).strip().lower()
run2=run.replace('\u201c','"').replace('\u201d','"')
n=bad=0
for m in re.finditer(r'"([^"\n]{3,600})"[\s,;.:)]*((?:\*?\*?\[[MLR]\d{4}-\d{3}\]\*?\*?[,;\s]*)+)',run2):
    n+=1; frag=m.group(1); cited=re.findall(r'[MLR]\d{4}-\d{3}',m.group(2))
    parts=[p.strip(' .,;') for p in re.split(r'\[\.\.\.\]|\.\.\.|…',frag) if p.strip(' .,;')]
    if not any(all(norm(p) in norm(rows.get(c,'')) for p in parts) for c in cited):
        bad+=1; print('SLIP',cited,':',frag[:160])
ids=set(re.findall(r'[MLR]\d{4}-\d{3}',run)); miss=[i for i in ids if i not in rows]
print('fragments',n,'slips',bad,'distinct ids',len(ids),'missing',miss,'E-ids',re.findall(r'\[E\d-\d+\]',run))
