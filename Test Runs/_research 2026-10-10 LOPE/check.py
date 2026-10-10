import csv,re,sys
R={}
for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8')):
    R[r.get('\ufeffid') or r['id']]=r['quote_verbatim']
t=open('Test Runs/2026-10-10 Run - LOPE Grand Canyon Education.md',encoding='utf-8').read()
bad=0
if re.search(r'\[E\d-\d+\]',t): print('E-id found'); bad=1
ids=set(re.findall(r'\[([MLR]\d{4}-\d{3})\]',t))
for i in sorted(ids):
    if i not in R: print('MISSING',i); bad=1
# quoted fragments within 250 chars before an id
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t):
    i=m.group(1); seg=t[max(0,m.start()-260):m.start()]
    # take the last quote in the segment that closes right before the id
    qs=re.findall(r'"([^"]{6,})"',seg)
    if not qs: continue
    q=qs[-1]
    # only fragments ending within 40 chars of the id
    if len(seg)-seg.rfind('"')>40: continue
    for part in re.split(r'\s*\[\.\.\.\]\s*',q):
        pn=" ".join(part.split()); rn=" ".join(R.get(i,"").split())
        if pn and pn not in rn and pn[0].swapcase()+pn[1:] not in rn:
            print('NOT IN ROW',i,'|',part[:90]); bad=1
print('ids',len(ids),'bad',bad)
