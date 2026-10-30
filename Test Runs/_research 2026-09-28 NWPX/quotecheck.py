import re, glob, csv, html
run=open('../2026-09-28 Run - NWPX NWPX Infrastructure.md',encoding='utf-8').read()
qs=re.findall(r'\*"([^"*]{6,})"\*', run)
srcs=[]
for f in glob.glob('cache/*.txt')+glob.glob('*.txt')+['../_TEMPLATE - Company Run.md','../2026-09-19 Run - OTTR Otter Tail.md','../2026-09-28 Run - POWL Powell Industries.md','../../Framework/THE FRAMEWORK v4.md','../../Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv']:
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
