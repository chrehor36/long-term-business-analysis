import sys,os,re,html,json,time,urllib.request
sys.path.insert(0,r'C:\Users\chreh\OneDrive\Documents\BRK\tools')
import sources
HERE=os.path.dirname(os.path.abspath(__file__))
PEERS={"MCO":"0001059556","MSCI":"0001408198","FDS":"0001013237","MORN":"0001289419",
       "VRSK":"0001442145","ICE":"0001571949","NDAQ":"0001120193","CME":"0001156375",
       "TRU":"0001552033","EFX":"0000033185"}
def get(url,binary=False):
    for k in range(4):
        try:
            req=urllib.request.Request(url,headers=sources.SEC_UA)
            d=urllib.request.urlopen(req,timeout=180).read()
            return d if binary else d.decode("utf-8","replace")
        except Exception as e:
            last=e; time.sleep(2+3*k)
    raise last
def strip(raw):
    t=re.sub(r"(?is)<(script|style|ix:header).*?</\1>"," ",raw)
    t=re.sub(r"(?i)</(td|th)>"," | ",t); t=re.sub(r"(?i)</(p|div|tr|li|h\d|table)>","\n",t)
    t=re.sub(r"(?i)<br[^>]*>","\n",t); t=re.sub(r"<[^>]+>"," ",t); t=html.unescape(t)
    t=re.sub(r"[ \t\u00a0\u200b]+"," ",t); t=re.sub(r"( \| )+( ?\| ?)*"," | ",t)
    return re.sub(r"\n\s*\n+","\n",t)
for tk,cik in PEERS.items():
    cf=os.path.join(HERE,f"{tk}_companyfacts.json")
    if not os.path.exists(cf):
        open(cf,"wb").write(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json",True)); time.sleep(0.4)
    sb=os.path.join(HERE,f"{tk}_sub.json")
    if not os.path.exists(sb):
        open(sb,"wb").write(get(f"https://data.sec.gov/submissions/CIK{cik}.json",True)); time.sleep(0.4)
    sub=json.load(open(sb,encoding="utf-8"))["filings"]["recent"]
    rows=list(zip(sub["form"],sub["filingDate"],sub["reportDate"],sub["accessionNumber"],sub["primaryDocument"]))
    got=0
    for f,fd,rd,acc,doc in rows:
        if f in ("10-K","20-F") and got<2:
            p=os.path.join(HERE,f"peer_{tk}_{f.replace('-','')}_{rd}.txt")
            if not os.path.exists(p):
                url=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
                open(p,"w",encoding="utf-8").write(strip(get(url)))
                print(tk,f,rd,acc,url); time.sleep(0.4)
            else: print("have",tk,rd)
            got+=1
