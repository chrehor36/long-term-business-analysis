import csv, sys
rows={r['id']:r for r in csv.DictReader(open(r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv',encoding='utf-8-sig'))}
out=open('ids_out.txt','w',encoding='utf-8')
for i in sys.argv[1:]:
    r=rows.get(i)
    out.write(i+' :: '+(r['quote_verbatim'] if r else 'MISSING')+'\n\n')
