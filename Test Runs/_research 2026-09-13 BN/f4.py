import urllib.request, os
from f2 import totext
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=180).read()
for acc,fn,out in [("0001837429-26-000008","bnt-20251231.htm","BWS_20F_2025.txt"),("0001837429-26-000018","bnt-20260630.htm","BWS_6K_Q2_2026.txt")]:
    if os.path.exists(out): continue
    b=get(f"https://www.sec.gov/Archives/edgar/data/1837429/{acc.replace('-','')}/{fn}")
    open(out,"w",encoding="utf-8").write(totext(b)); print(out,len(b))
