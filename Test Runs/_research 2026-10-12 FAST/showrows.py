import csv, sys
sys.stdout.reconfigure(encoding="utf-8")
r={x['id']:x for x in csv.DictReader(open(r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv",encoding='utf-8-sig'))}
n=int(sys.argv[1]); 
for i in sys.argv[2:]:
    x=r.get(i)
    print(i, x['year'] if x else 'MISSING', '|', (x['quote_verbatim'][:n].replace('\n',' ') if x else ''),'\n')
