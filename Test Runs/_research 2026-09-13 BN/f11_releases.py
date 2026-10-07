import urllib.request, os, json, re
from f2 import totext
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=240).read()
jobs=[("0001171843-26-003394","6K_20260514_Q1release.txt"),("0001171843-26-000765","6K_20260212_Q4release.txt"),("0001171843-25-007252","6K_20251113_Q3release.txt")]
for acc,out in jobs:
    if os.path.exists(out): print("have",out); continue
    base=f"https://www.sec.gov/Archives/edgar/data/1001085/{acc.replace('-','')}/"
    idx=get(base+"index.json"); j=json.loads(idx)
    names=[x["name"] for x in j["directory"]["item"]]
    ex=[n for n in names if re.search(r"ex.?99.?1|exh_991",n,re.I) and n.endswith(".htm")]
    print(acc,names,ex)
    if ex:
        b=get(base+ex[0]); open(out,"w",encoding="utf-8").write(totext(b)); print(out,len(b))
