import json,os,re,html,urllib.request,time,sys
hdr={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
D="Test Runs/_research 2026-09-21 USNA"
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
s=json.load(open(os.path.join(D,"submissions.json")))
allf=[]
for blk in [s["filings"]["recent"]]+[json.load(open(os.path.join(D,"_extra.json")))] if False else [s["filings"]["recent"]]:
    allf+=list(zip(blk["form"],blk["filingDate"],blk["reportDate"],blk["accessionNumber"],blk["primaryDocument"]))
# older filings live in the paged files
for f in s["filings"].get("files",[]):
    b=get("https://data.sec.gov/submissions/"+f["name"])
    if b:
        j=json.loads(b)
        allf+=list(zip(j["form"],j["filingDate"],j["reportDate"],j["accessionNumber"],j["primaryDocument"]))
tenks=[r for r in allf if r[0]=="10-K"]
tenks.sort(key=lambda r:r[1],reverse=True)
for form,fd,rd,acc,doc in tenks[:10]:
    print(form,fd,rd,acc,doc)
    out=os.path.join(D,f"10K_{rd}.txt")
    if os.path.exists(out) or not doc: continue
    b=get(f"https://www.sec.gov/Archives/edgar/data/896264/{acc.replace('-','')}/{doc}")
    if b: open(out,"w",encoding="utf-8").write(strip(b)); time.sleep(0.3)
