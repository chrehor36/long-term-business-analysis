import json, os, re, sys, time, urllib.request, html
sys.stdout.reconfigure(encoding="utf-8")
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
OUT=os.path.dirname(os.path.abspath(__file__))
def get(url,tries=4):
    last=None
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=180).read()
        except Exception as e:
            last=e; time.sleep(2.0*(i+1))
    raise last
CIK=1506293
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
docs=[("10K_FY2025","0001506293-26-000021","pins-20251231.htm"),
      ("10K_FY2024","0001506293-25-000022","pins-20241231.htm"),
      ("10K_FY2023","0001506293-24-000018","pins-20231231.htm"),
      ("10K_FY2022","0001506293-23-000023","pins-20221231.htm"),
      ("10K_FY2021","0001506293-22-000016","pins-20211231.htm"),
      ("10K_FY2020","0001506293-21-000025","pins-20201231.htm"),
      ("10Q_2026Q2","0001506293-26-000104","pins-20260630.htm"),
      ("10Q_2026Q1","0001506293-26-000068","pins-20260331.htm"),
      ("DEF14A_2026","0001506293-26-000058","pins-20260407.htm"),
      ("DEF14A_2025","0001506293-25-000084","pins-20250408.htm"),
      ]
for name,acc,doc in docs:
    p=os.path.join(OUT,name+".txt")
    if os.path.exists(p) and os.path.getsize(p)>10000:
        print("have",name,os.path.getsize(p)); continue
    a=acc.replace("-","")
    url=f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{doc}"
    try:
        t=strip(get(url))
        open(p,"w",encoding="utf-8").write(t)
        print("ok",name,len(t))
    except Exception as e:
        print("FAIL",name,e)
    time.sleep(0.3)
# companyfacts
p=os.path.join(OUT,"companyfacts.json")
if not os.path.exists(p):
    d=get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK:010d}.json")
    open(p,"wb").write(d); print("ok companyfacts",len(d))
else: print("have companyfacts")
