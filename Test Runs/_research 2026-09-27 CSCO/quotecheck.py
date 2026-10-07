import re,glob,csv,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
run=open(r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-27 Run - CSCO Cisco Systems.md',encoding='utf-8').read()
ids=set(re.findall(r'E\d-\d{2}',run))
led={r['id']:r for r in csv.DictReader(open(r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger.csv',encoding='utf-8-sig'))}
print('ids cited',len(ids),'missing',sorted(i for i in ids if i not in led))
def norm(s):
    s=s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"').replace('\ufffd',"'").replace('\xa0',' ')
    s=re.sub(r'[\*\|]',' ',s); s=re.sub(r'\s+',' ',s); return s.strip().lower()
corpus=''
for f in glob.glob('flat/*.txt')+glob.glob('filings/*.txt')+glob.glob('peers/*.txt')+glob.glob('8k/*.txt'):
    corpus+=' '+norm(open(f,encoding='utf-8',errors='ignore').read())
for f in ['../../principle_ledger.csv','../../Framework/THE FRAMEWORK v4.md','../../Screens/SURVIVAL SHAPES - index.md','../../Test Runs/_TEMPLATE - Company Run.md']+glob.glob('../../Framework/v4/RULING CASE 2026-09-20*'):
    corpus+=' '+norm(open(f,encoding='utf-8',errors='ignore').read())
qs=re.findall(r'\*"(.+?)"\*',run)
miss=[]
for q in qs:
    parts=[p for p in re.split(r'\s*(?:\.\.\.|\[\.\.\.\]|…)\s*',q) if len(p.strip())>3]
    ok=all(norm(p) in corpus for p in parts)
    if not ok: miss.append(q)
print('quotes',len(qs),'not found',len(miss))
for m in miss: print('  X',m[:220])
