import json, time, urllib.parse, urllib.request, collections, os
from fetch_core import HERE
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept":"application/json"}
def q(phrase, forms=None, cik=None, start=None, end=None):
    p={"q":'"%s"'%phrase}
    if forms: p["forms"]=forms
    if cik: p["ciks"]=cik
    if start: p["dateRange"]="custom"; p["startdt"]=start; p["enddt"]=end
    url="https://efts.sec.gov/LATEST/search-index?"+urllib.parse.urlencode(p)
    d=json.loads(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read())
    tot=d.get("hits",{}).get("total",{}).get("value")
    names=collections.Counter()
    for h in d.get("hits",{}).get("hits",[]):
        s=h["_source"]; names[(s.get("display_names") or ["?"])[0][:60]+" "+s.get("form","")]+=1
    time.sleep(0.4)
    return tot,url,names.most_common(8), [(h["_source"].get("display_names",["?"])[0][:50],h["_source"].get("form"),h["_source"].get("file_date"),h["_id"]) for h in d.get("hits",{}).get("hits",[])[:5]]
QS=[("Vantage Data Centers",None),("Vantage Data Centers","10-K"),("Stack Infrastructure",None),("Stack Infrastructure","10-K"),
    ("Aligned Data Centers",None),("Aligned Data Centers","10-K"),("NTT Global Data Centers",None),("NTT Global Data Centers","10-K"),
    ("Cologix",None),("Cologix","10-K"),("Flexential",None),("Flexential","10-K"),("DataBank",None),("DataBank","10-K"),
    ("colocation","ABS-15G"),("data center","ABS-EE"),("Vantage Data Centers Issuer",None),("DataBank Issuer",None),("Stack Infrastructure Issuer",None),
    ("cross-connects","10-K"),("interconnection revenue","10-K"),("colocation pricing","10-K"),("oversupply","10-K")]
out=[]
for ph,fm in QS:
    try: r=q(ph,fm,start="2021-01-01",end="2026-09-18")
    except Exception as e: r=(None,str(e),[],[])
    out.append({"phrase":ph,"forms":fm,"range":"2021-01-01..2026-09-18","total":r[0],"url":r[1],"top_entities":r[2],"sample":r[3]})
    print(ph,fm,r[0]); print("   ",r[2][:6])
json.dump(out,open(os.path.join(HERE,"FTS_queries.json"),"w"),indent=1)
