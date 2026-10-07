import re, glob, csv, html
run=open('../2026-09-28 Run - PFGC Performance Food Group.md',encoding='utf-8').read()
qs=re.findall(r'\*"([^"*]{6,})"\*', run)
srcs=[]
for f in glob.glob('cache/*.txt')+glob.glob('*.txt')+['../_research 2026-09-26 SYY/peers/USFD_10K_2025-12-27.txt','../_research 2026-09-26 SYY/tenk_FY2026.txt','../2026-09-26 Run - SYY Sysco.md','../_TEMPLATE - Company Run.md','../../Framework/THE FRAMEWORK v4.md','../../Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv']:
    srcs.append(open(f,encoding='utf-8',errors='ignore').read())
srcs.append(open('../../principle_ledger.csv',encoding='utf-8-sig',errors='ignore').read())
def norm(s): 
    s=s.replace('’',"'").replace('“','"').replace('”','"').replace('​','').replace('\xa0',' ')
    return re.sub(r'\s+',' ',s).strip().lower()
S=[norm(x) for x in srcs]
bad=[]
for q in set(qs):
    parts=[p.strip() for p in re.split(r'\.\.\.|…|\[\.\.\.\]',q) if len(p.strip())>4]
    ok=all(any(norm(p) in s for s in S) for p in parts)
    if not ok: bad.append(q)
print(len(set(qs)),'quotes;', len(bad),'unmatched')
for b in bad: print(' -', b[:200])
