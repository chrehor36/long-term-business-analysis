import json, os, re, sys, time, urllib.request, html
sys.stdout.reconfigure(encoding="utf-8")
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
OUT=os.path.dirname(os.path.abspath(__file__))
def get(url,tries=5):
    last=None
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=240).read()
        except Exception as e:
            last=e; time.sleep(2.0*(i+1))
    raise last
def strip(b):
    t=b.decode("utf-8","ignore")
    t=re.sub(r"(?is)<(script|style).*?</\1>"," ",t)
    t=re.sub(r"(?i)<br\s*/?>","\n",t)
    t=re.sub(r"(?i)</(p|div|tr|h[1-6]|li)>","\n",t)
    t=re.sub(r"(?i)</t[dh]>"," | ",t)
    t=re.sub(r"(?s)<[^>]+>"," ",t)
    t=html.unescape(t)
    t=re.sub(r"[ \t\xa0]+"," ",t)
    t=re.sub(r"\n\s*\n+","\n",t)
    return t
DOCS=[
 ("META",1326801,"META_10K_FY2025","0001628280-26-003942","meta-20251231.htm"),
 ("META",1326801,"META_10K_FY2024","0001326801-25-000017","meta-20241231.htm"),
 ("GOOGL",1652044,"GOOGL_10K_FY2025","0001652044-26-000018","goog-20251231.htm"),
 ("GOOGL",1652044,"GOOGL_10K_FY2024","0001652044-25-000014","goog-20241231.htm"),
 ("SNAP",1564408,"SNAP_10K_FY2025","0001564408-26-000013","snap-20251231.htm"),
 ("SNAP",1564408,"SNAP_10K_FY2024","0001564408-25-000019","snap-20241231.htm"),
 ("SNAP",1564408,"SNAP_10K_FY2023","0001564408-24-000019","snap-20231231.htm"),
 ("SNAP",1564408,"SNAP_10K_FY2022","0001564408-23-000013","snap-20221231.htm"),
 ("SNAP",1564408,"SNAP_10K_FY2021","0001564590-22-003868","snap-10k_20211231.htm"),
 ("SNAP",1564408,"SNAP_10K_FY2020","0001564590-21-004377","snap-10k_20201231.htm"),
 ("RDDT",1713445,"RDDT_10K_FY2025","0001713445-26-000022","rddt-20251231.htm"),
 ("RDDT",1713445,"RDDT_10K_FY2024","0001713445-25-000018","rddt-20241231.htm"),
 ("TTD",1671933,"TTD_10K_FY2025","0001671933-26-000014","ttd-20251231.htm"),
]
for tk,cik,name,acc,doc in DOCS:
    p=os.path.join(OUT,name+".txt")
    if os.path.exists(p) and os.path.getsize(p)>50000:
        print("have",name,os.path.getsize(p)); continue
    a=acc.replace("-","")
    url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{doc}"
    try:
        t=strip(get(url)); open(p,"w",encoding="utf-8").write(t); print("ok",name,len(t))
    except Exception as e:
        print("FAIL",name,e)
    time.sleep(0.4)
for tk,cik in [("META",1326801),("SNAP",1564408),("RDDT",1713445),("TTD",1671933),("GOOGL",1652044)]:
    p=os.path.join(OUT,f"cf_{tk}.json")
    if os.path.exists(p): print("have cf",tk); continue
    try:
        open(p,"wb").write(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json")); print("ok cf",tk)
    except Exception as e: print("FAIL cf",tk,e)
    time.sleep(0.4)
