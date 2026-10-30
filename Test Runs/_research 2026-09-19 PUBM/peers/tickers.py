import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fetch_core import get
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
t = json.loads(get("https://www.sec.gov/files/company_tickers.json"))
names = {v["ticker"]: (v["cik_str"], v["title"]) for v in t.values()}
for tk in ["MGNI","TTD","APPS","CRTO","GOOGL","AMZN","APP","U","TBLA","TEAD","PERI","CMCSA","VRVE","MSFT","DSP","IAS","DV"]:
    print(tk, names.get(tk))
out = open(os.path.join(H,"private_check.txt"),"w",encoding="utf-8")
for q in ["index exchange","openx","equativ","sovrn","sharethrough","freewheel","xandr","verve","triplelift","kargo","media.net","yieldmo","smaato","inmobi","teads"]:
    hits = [f"{v['ticker']} {v['title']}" for v in t.values() if q in v["title"].lower()]
    s = f"{q}: {hits}"; print(s); out.write(s+"\n")
