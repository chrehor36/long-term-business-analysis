import json,os,re,html,urllib.request,time
hdr={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
D="Test Runs/_research 2026-09-21 USNA/peers"
def get(url):
    for i in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(url,headers=hdr),timeout=120).read()
        except Exception as e: print("retry",e); time.sleep(3)
    return None
def strip(b):
    t=b.decode("utf-8","ignore")
    t=re.sub(r"(?is)<(script|style).*?</\1>"," ",t)
    t=re.sub(r"(?i)<br[^>]*>","\n",t)
    t=re.sub(r"(?i)</(p|div|tr|h[1-6]|li)>","\n",t)
    t=re.sub(r"(?i)</t[dh]>"," | ",t)
    t=re.sub(r"<[^>]+>"," ",t); t=html.unescape(t)
    t=re.sub(r"[ \t\xa0]+"," ",t); t=re.sub(r"\n\s*\n+","\n",t)
    return t
for tic,cik in [("HLF","1180262"),("NUS","1021561"),("MED","910329"),("NHTC","912061")]:
    b=get(f"https://data.sec.gov/submissions/CIK{cik.zfill(10)}.json")
    j=json.loads(b); r=j["filings"]["recent"]
    rows=[x for x in zip(r["form"],r["filingDate"],r["reportDate"],r["accessionNumber"],r["primaryDocument"]) if x[0]=="10-K"]
    rows.sort(key=lambda x:x[1],reverse=True)
    if not rows: print(tic,"none"); continue
    f,fd,rd,acc,doc=rows[0]
    print(tic,fd,rd,acc,doc)
    out=os.path.join(D,f"{tic}_10K_{rd}.txt")
    if os.path.exists(out): continue
    bb=get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}")
    if bb: open(out,"w",encoding="utf-8").write(strip(bb)); time.sleep(0.4)
