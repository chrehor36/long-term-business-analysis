import re,glob,csv
norm=lambda s: re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('\xa0',' ')).strip()
corpus=[]
for f in glob.glob('filings/*.txt')+glob.glob('peers/COTY_10K_*.txt'):
    corpus.append(norm(open(f,encoding='utf-8',errors='ignore').read()))
corpus.append(norm(open('../../Screens/WATCHLIST RUN QUEUE.md',encoding='utf-8').read()))
for r in csv.DictReader(open('../../principle_ledger.csv',encoding='utf-8-sig')): corpus.append(norm(r['quote_verbatim']+' '+r['evolution_notes']))
big='\n'.join(corpus); bigs=re.sub(r' ?([|,.;:()]) ?',r'\1',big)
t=open('../2026-09-27 Run - IPAR Interparfums.md',encoding='utf-8').read()
ids=set(re.findall(r'\[?(E\d-\d+)',t)); led={r['id'] for r in csv.DictReader(open('../../principle_ledger.csv',encoding='utf-8-sig'))}
print('ids',len(ids),'missing',sorted(ids-led))
qs=re.findall(r'\*"(.+?)"\*',t)
miss=0
for q in qs:
    for part in re.split(r' ?\.\.\. ?|\[\.\.\.\]',q):
        p=norm(part).strip(' .')
        if len(p)<12: continue
        ps=re.sub(r' ?([|,.;:()]) ?',r'\1',p)
        if p not in big and ps not in bigs:
            miss+=1; print('NOT FOUND:',p[:160])
print('quotes',len(qs),'misses',miss)
