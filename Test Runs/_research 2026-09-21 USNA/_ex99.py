import json,os,re,html,urllib.request,time
hdr={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
D="Test Runs/_research 2026-09-21 USNA"
def get(u):
    for i in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=hdr),timeout=120).read()
        except Exception as e: print("retry",e); time.sleep(3)
def strip(b):
    t=b.decode("utf-8","ignore")
    t=re.sub(r"(?is)<(script|style).*?</\1>"," ",t)
    t=re.sub(r"(?i)<br[^>]*>","\n",t); t=re.sub(r"(?i)</(p|div|tr|h[1-6]|li)>","\n",t)
    t=re.sub(r"(?i)</t[dh]>"," | ",t); t=re.sub(r"<[^>]+>"," ",t); t=html.unescape(t)
    t=re.sub(r"[ \t\xa0]+"," ",t); t=re.sub(r"\n\s*\n+","\n",t); return t
for acc,label in [("0000896264-26-000050","2026Q2"),("0000896264-26-000030","2026Q1"),
                  ("0000896264-26-000014","2025Q4")]:
    a=acc.replace("-","")
    idx=get(f"https://www.sec.gov/Archives/edgar/data/896264/{a}/index.json")
    if not idx: continue
    items=json.loads(idx)["directory"]["item"]
    for it in items:
        n=it["name"]
        if re.search(r"(?i)(ex.?99|exhibit99)", n) and n.endswith((".htm",".txt")):
            b=get(f"https://www.sec.gov/Archives/edgar/data/896264/{a}/{n}")
            if b:
                out=os.path.join(D,f"EX991_{label}.txt")
                open(out,"w",encoding="utf-8").write(strip(b))
                print(label,n,os.path.getsize(out))
            time.sleep(0.3)
