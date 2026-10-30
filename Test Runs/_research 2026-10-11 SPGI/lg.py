"""Search principle_ledger_v5.csv. Usage: lg.py REGEX [maxchars]  or  lg.py --id ID [ID...]"""
import csv,re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
rows=list(csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig')))
if sys.argv[1]=='--id':
    want=set(sys.argv[2:])
    for r in rows:
        if r['id'] in want: print(r['id'],r['year'],r['source_file'],'|',r['quote_verbatim'],'\n')
else:
    pat=re.compile(sys.argv[1],re.I); n=int(sys.argv[2]) if len(sys.argv)>2 else 500
    for r in rows:
        if pat.search(r['quote_verbatim']): print(r['id'],'|',r['quote_verbatim'][:n].replace('\n',' '),'\n')
