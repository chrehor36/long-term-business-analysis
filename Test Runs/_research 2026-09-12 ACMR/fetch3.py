import urllib.request, os, time
UA={"User-Agent":"BRK framework run chrehor36@gmail.com","Accept-Encoding":"identity"}
OUT="Test Runs/_research 2026-09-12 ACMR"; CIK="1680062"
def get(u):
    for i in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=120).read()
        except Exception: time.sleep(3)
    return b""
jobs=[("0001140361-22-007348","brhc10034322_10k.htm","10K_FY2021.htm"),
("0001140361-21-006683","brhc10020658_10k.htm","10K_FY2020.htm"),
("0001140361-20-006743","form10k.htm","10K_FY2019.htm"),
("0001654954-19-002737","acm_10k.htm","10K_FY2018.htm"),
("0001654954-18-002950","acmr_10k.htm","10K_FY2017.htm")]
for a,n,o in jobs:
    b=get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a.replace('-','')}/{n}")
    open(os.path.join(OUT,o),"wb").write(b); print(o,len(b)); time.sleep(0.4)
