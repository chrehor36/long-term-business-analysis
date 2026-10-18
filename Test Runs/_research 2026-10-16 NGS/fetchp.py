import sys, os, time, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import totext
UA = "Chris Hrehor chrehor36@gmail.com"
for cik, acc, doc, out in [("1389050","0001389050-26-000009","aroc-20251231x10k.htm","AROC_k2025.htm"),("1522727","0001522727-26-000015","usac-20251231.htm","USAC_k2025.htm"),("1767042","0001767042-26-000012","kgs-20251231.htm","KGS_k2025.htm")]:
    p = os.path.join("cache","peers",out)
    if not os.path.exists(p):
        url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
        open(p,"wb").write(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":UA}),timeout=90).read()); time.sleep(0.5)
    print(totext(p))
