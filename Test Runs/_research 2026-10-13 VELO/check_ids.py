import csv,re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
run=open('Test Runs/2026-10-13 Run - VELO Velo3D.md',encoding='utf-8').read()
R={r[0]:r[2] for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
def norm(s): return re.sub(r'\s+',' ',s.replace('�','')).strip().lower()
bad=0
e=re.findall(r'\[E\d-\d+\]',run); print('E-ids:',e); bad+=len(e)
ids=set(re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run))
for i in sorted(ids):
    if i not in R: print('MISSING',i); bad+=1
print('ids cited:',len(ids))
# quoted fragment immediately before an id (allowing punctuation and other ids in between)
for m in re.finditer(r'"([^"]{3,}?)"[\s.,;:)]*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[\s,]*)+)',run):
    frag=m.group(1); fid=re.findall(r'[MLR]\d{4}-\d{3}',m.group(2))
    parts=[p for p in re.split(r'\[\.\.\.\]',frag) if p.strip()]
    ok=any(all(norm(p.strip(' .,')) in norm(R.get(i,'')) for p in parts) for i in fid)
    print('OK ' if ok else 'BAD', fid, frag[:70]); bad+= (not ok)
print('RESULT', 'PASS' if bad==0 else f'FAIL {bad}')
