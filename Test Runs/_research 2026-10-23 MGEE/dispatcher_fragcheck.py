import csv,re,sys
L={}
with open('principle_ledger_v5.csv',encoding='utf8') as f:
    r=csv.reader(f); h=next(r); qi=[i for i,c in enumerate(h) if 'quote' in c.lower() or 'text' in c.lower()][0]
    for row in r: L[row[0]]=row[qi]
def norm(s): return re.sub(r'\s+',' ',s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"')).strip().lower()
t=open(sys.argv[1],encoding='utf8').read()
n=bad=0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t):
    i=m.group(1)
    if i not in L: print('MISSING',i); bad+=1; continue
    pre=t[max(0,m.start()-400):m.start()]
    q=re.search(r'["”]\*?\s*(\([^)]{0,40}\))?\s*(\*\*\[[MLR]\d{4}-\d{3}\]\*\*[ ,;and]*)*$',pre)
    if not q: continue
    qs=pre[:q.start()]; o=max(qs.rfind('"'),qs.rfind('“'))
    if o<0: continue
    frag=qs[o+1:]
    if len(frag)<4 or len(frag)>600: continue
    n+=1
    parts=[p for p in re.split(r'\[\.\.\.\]|\.\.\.',frag) if p.strip()]
    if not all(norm(p) in norm(L[i]) for p in parts): print('SLIP',i,'|',frag[:120]); bad+=1
print('ids',len(re.findall(r'\[[MLR]\d{4}-\d{3}\]',t)),'fragments',n,'problems',bad, 'E-ids',len(re.findall(r'\[E\d+-\d+\]',t)))
