import csv,re,sys
rows=list(csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig')))
n=int(sys.argv[1]); 
for p in sys.argv[2:]:
    hits=[r for r in rows if re.search(p,r['quote_verbatim'],re.I)]
    print('##',p,len(hits))
    for r in hits[:n]:
        print(r['id'],'|',r['quote_verbatim'][:300].replace('\n',' '))
