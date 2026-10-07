import csv,sys
rows={}
with open(r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv',encoding='utf-8-sig') as f:
    for row in csv.DictReader(f): rows[row['id']]=row
for i in sys.argv[1:]:
    print(i,'|',rows[i]['quote_verbatim'][:900]); print()
