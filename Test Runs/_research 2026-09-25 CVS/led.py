import csv,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8',errors='replace')
R={r[list(r.keys())[0]]:r for r in csv.DictReader(open(r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger.csv',encoding='utf-8'))}
for i in sys.argv[1:]:
    r=R.get(i)
    if not r: print(i,'MISSING'); continue
    print('##',i,' | '.join(f'{k}={v[:700]}' for k,v in r.items() if k!=list(r.keys())[0]))
