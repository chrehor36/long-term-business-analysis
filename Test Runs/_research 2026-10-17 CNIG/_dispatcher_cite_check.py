# Dispatcher's check (overnight 2026-10-17): every quoted fragment immediately before a ledger id is in that row.
import csv,re,sys,unicodedata
sys.stdout.reconfigure(encoding='utf-8')
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    for a,b in (('\u2019',"'"),('\u2018',"'"),('\u201c','"'),('\u201d','"'),('\u2014','-'),('\u2013','-')): s=s.replace(a,b)
    return re.sub(r'\s+',' ',s).strip().lower()
rows={}
with open('principle_ledger_v5.csv',encoding='utf-8') as f:
    r=csv.reader(f);next(r)
    for x in r: rows[x[0]]=norm(' '.join(x))
t=open(sys.argv[1],encoding='utf-8').read()
ids=set(re.findall(r'\[([MLR]\d{4}-\d{3})\]',t))
print('ids',len(ids),'missing',[i for i in ids if i not in rows],'E-ids',re.findall(r'\[E\d-\d+\]',t))
n=0;slips=[]
pat=re.compile(r'["\u201c]([^"\u201d]{6,}?)["\u201d][\s,.;:)]*(?:\(\w[^)]{0,40}\)\s*)?\*\*((?:\[[MLR]\d{4}-\d{3}\][,;\s]*)+)\*\*')
for m in pat.finditer(t):
    q=m.group(1); pids=re.findall(r'[MLR]\d{4}-\d{3}',m.group(2))
    parts=[p for p in re.split(r'\[\.\.\.\]|\.\.\.|\u2026',q) if len(p.strip(' .,;:'))>3]
    n+=1
    if not any(all(norm(p).strip(' .,;:') in rows.get(i,'') for p in parts) for i in pids): slips.append((pids,q))
print('adjacent fragments',n,'unmatched',len(slips))
for s in slips: print(' ',s)
