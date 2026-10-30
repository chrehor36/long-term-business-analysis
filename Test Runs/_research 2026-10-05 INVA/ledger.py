import csv,re,sys
rows=list(csv.DictReader(open(r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv',encoding='utf-8-sig')))
def show(r,n=400): print(r['id'],r['year'],'|',r['quote_verbatim'][:n].replace('\n',' '),'\n')
if sys.argv[1]=='kw':
    for kw in sys.argv[2:]:
        hits=[r for r in rows if re.search(kw,r['quote_verbatim'],re.I)]
        print('==',kw,len(hits))
        for r in hits[:40]: show(r,300)
else:
    ids=set(sys.argv[2:])
    for r in rows:
        if r['id'] in ids: show(r,3000)
