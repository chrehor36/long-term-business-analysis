import urllib.request, os
from f2 import totext
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=300).read()
for acc,fn,out in [("0001001085-25-000007","bn-20241231_d2.htm","40F_2024_d2.txt"),("0001001085-24-000007","bn-20231231_d2.htm","40F_2023_d2.txt"),("0001001085-23-000007","bam-20221231_d2.htm","40F_2022_d2.txt")]:
    if os.path.exists(out): continue
    b=get(f"https://www.sec.gov/Archives/edgar/data/1001085/{acc.replace('-','')}/{fn}")
    open(out,"w",encoding="utf-8").write(totext(b)); print(out,len(b))
