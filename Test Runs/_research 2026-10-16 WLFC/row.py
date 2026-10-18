import csv,sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
rows={r[0]:r for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8'))}
hdr=rows.get('id')
for i in sys.argv[1:]:
    r=rows.get(i)
    if not r: print(i,'MISSING'); continue
    print(f"--- {i} ({r[3]}): {r[2][:1500]}")
