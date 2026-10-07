import re,glob,csv,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
run=open('Test Runs/2026-09-28 Run - MSA MSA Safety.md',encoding='utf-8').read()
ids=set(re.findall(r'E\d-\d\d',run))
led={r[0] for r in csv.reader(open('principle_ledger.csv',encoding='utf-8'))}
print('ids',len(ids),'missing',sorted(i for i in ids if i not in led))
def norm(t):
    t=t.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('�',"'").replace('—','-').replace('–','-')
    t=re.sub(r'[\s|]+',' ',t)
    return t.lower()
corp=''
for f in glob.glob('Test Runs/_research 2026-09-28 MSA/cache/*.txt')+glob.glob('Test Runs/_research 2026-09-28 MSA/peers/*.txt')+glob.glob('Test Runs/_research 2026-09-28 MSA/*.txt')+['principle_ledger.csv','Framework/THE FRAMEWORK v4.md','Test Runs/_research 2026-09-28 MSA/treasury_2026.csv','Test Runs/_research 2026-09-28 MSA/cover_shares_out.txt']:
    corp+=norm(open(f,encoding='utf-8',errors='ignore').read())+' '
qs=re.findall(r'\*"([^"]{8,}?)"\*',run)
bad=0
for q in qs:
    parts=[p.strip(' .,;') for p in re.split(r'\.\.\.|…|\[\.\.\.\]',q) if len(p.strip(' .,;'))>6]
    miss=[p for p in parts if norm(p) not in corp]
    if miss:
        bad+=1; print('NOT FOUND:',q[:160],'| part:',miss[0][:80])
print('quotes',len(qs),'unmatched',bad)
