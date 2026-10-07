import json, sys, re
sys.path.insert(0,'.')
from fetch10k import get, totext
# usage: tk cik acc fy pattern
tk,cik,acc,fy,pat=sys.argv[1:6]
a=acc.replace('-','')
items=json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/index.json"))['directory']['item']
for it in items:
    print(it['name'],it.get('size'))
for it in items:
    if re.search(pat,it['name'],re.I):
        u=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{it['name']}"
        t=totext(get(u))
        fn=f"raw/{tk}_10K_FY{fy}_EX13.txt"
        open(fn,'w',encoding='utf-8').write(f"SOURCE: 10-K exhibit {it['name']} accession {acc} url {u}\n"+t)
        print('wrote',fn,len(t)); break
