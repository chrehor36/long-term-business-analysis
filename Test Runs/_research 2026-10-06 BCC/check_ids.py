import csv,re,sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT='../../'
R={r['id']:r['quote_verbatim'] for r in csv.DictReader(open(ROOT+'principle_ledger_v5.csv',encoding='utf-8-sig'))}
s=open(ROOT+'Test Runs/2026-10-06 Run - BCC Boise Cascade.md',encoding='utf-8').read()
bad=0
e=re.findall(r'\[E\d+-\d+\]',s); print('E-ids:',e); bad+=len(e)
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',s)
miss=sorted({i for i in ids if i not in R}); print('ids cited:',len(set(ids)),'missing:',miss); bad+=len(miss)
Q=r'"([^"]+)"'
pre=re.compile(r'((?:'+Q+r'[,.;]?\s*(?:,\s*|and\s+)?)+)(?:\([^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
post=re.compile(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*:\s*'+Q)
checked=[]
def chk(frag,i):
    global bad
    frag=re.sub(r'\s+',' ',frag); checked.append((i,frag))
    row=re.sub(r'\s+',' ',R.get(i,''))
    for part in [p.strip(' .,;') for p in frag.split('[...]')]:
        if part and part not in row:
            print('NOT IN ROW',i,'|',part); bad+=1
for m in pre.finditer(s):
    i=m.group(m.lastindex)
    for f in re.findall(Q,m.group(1)): chk(f,i)
for m in post.finditer(s): chk(m.group(2),m.group(1))
for c in checked: print('  ok?',c[0],'|',c[1][:80])
print('fragments checked:',len(checked),'problems:',bad)
