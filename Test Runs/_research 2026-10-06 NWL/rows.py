import csv,sys
ids=open(sys.argv[1]).read().split()
rows={r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
out=open(sys.argv[2],'w',encoding='utf-8')
for i in ids:
    r=rows.get(i)
    out.write('===== '+i+' '+('MISSING' if not r else r['year']+' '+r['speaker'])+'\n')
    if r: out.write(r['quote_verbatim']+'\n')
