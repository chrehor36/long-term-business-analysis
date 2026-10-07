import sys,os,json,urllib.request,time
sys.path.insert(0,"tools")
import sources as S
D="Test Runs/_research 2026-09-21 USNA/peers"
os.makedirs(D,exist_ok=True)
hdr={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
PEERS=["HLF","NUS","MED","NHTC","MTEX","LFVN","BODI"]
for t in PEERS:
    try:
        cik,name=S.cik_for(t)
    except Exception as e:
        print(t,"NO CIK",e); continue
    p=os.path.join(D,f"{t}_companyfacts.json")
    if not os.path.exists(p):
        try:
            r=urllib.request.urlopen(urllib.request.Request(
                f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json",headers=hdr),timeout=120)
            open(p,"wb").write(r.read())
        except Exception as e:
            print(t,"FAIL",e); continue
        time.sleep(0.3)
    print(t,cik,name,os.path.getsize(p))
