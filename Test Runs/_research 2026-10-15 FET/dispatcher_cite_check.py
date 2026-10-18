"""Dispatcher's citation check (overnight 2026-10-15): every quoted fragment ending within 40 characters before an id is in that row."""
import csv,re,sys,os,unicodedata
sys.stdout.reconfigure(encoding="utf-8")
root=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')
rows={r[0]:r[2] for r in csv.reader(open(os.path.join(root,'principle_ledger_v5.csv'),encoding='utf-8'))}
n=lambda t:re.sub(r'\s+',' ',unicodedata.normalize('NFC',t)).replace('\u2019',"'").replace('\u201c','"').replace('\u201d','"')
run=n(open(os.path.join(root,'Test Runs','2026-10-15 Run - FET Forum Energy Technologies.md'),encoding='utf-8').read())
bad=chk=0
for m in re.finditer(r'\[([MLR]\d{4}-\d{3})\]',run):
    i=m.group(1)
    if i not in rows: print('MISSING',i); bad+=1; continue
    pre=run[max(0,m.start()-40):m.start()]
    if '"' not in pre: continue
    end=run.rfind('"',0,m.start()); start=run.rfind('"',0,end)
    if start<0: continue
    frag=run[start+1:end]; chk+=1
    for p in re.split(r'\[\.\.\.\]|\.\.\.',frag):
        p=p.strip(' .,;:')
        if p and p.lower() not in n(rows[i]).lower(): print('SLIP',i,'|',p[:140]); bad+=1
print('checked',chk,'slips',bad)
