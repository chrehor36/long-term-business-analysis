import sys,urllib.request,time
sys.path.insert(0,"..")
from fetch import text, UA
cik,acc,doc,out=sys.argv[1:5]
url=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
for i in range(4):
    try:
        b=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=90).read();break
    except Exception as e: print(e); time.sleep(3)
open(out,"w",encoding="utf-8").write(text(b)); print(out,len(b))
