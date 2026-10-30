import urllib.request, os
from f2 import totext
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=300).read()
for acc,fn,out in [("0001001085-26-000011","a2025-q4bnannualreport.htm","6KA_AR2025_annualreport.txt")]:
    if os.path.exists(out): continue
    b=get(f"https://www.sec.gov/Archives/edgar/data/1001085/{acc.replace('-','')}/{fn}")
    open(out,"w",encoding="utf-8").write(totext(b)); print(out,len(b))
