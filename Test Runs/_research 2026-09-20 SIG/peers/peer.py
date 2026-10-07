import urllib.request, json, os, sys
from datetime import date
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
D=os.path.dirname(os.path.abspath(__file__))
def facts(cik,tk):
    p=os.path.join(D,f"{tk}_companyfacts.json")
    if not os.path.exists(p):
        b=urllib.request.urlopen(urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json",headers=UA),timeout=180).read()
        open(p,'wb').write(b)
    return json.load(open(p))
def ann(g,tags,pit=False):
    out={}
    for t in tags:
        if t not in g: continue
        for unit,rows in g[t]["units"].items():
            for r in rows:
                if r.get("form") not in ("10-K","10-K/A"): continue
                if pit:
                    if "start" in r: continue
                else:
                    if "start" not in r: continue
                    s=date.fromisoformat(r["start"]); e=date.fromisoformat(r["end"])
                    if not (330<(e-s).days<400): continue
                k=r["end"]
                if k not in out or r["filed"]>out[k][1]:
                    out[k]=(r["val"]/1e6,r["filed"])
    return out
peers={"SIG":"0000832988","BRLT":"0001866757","MOV":"0000072573","FOSL":"0000883569","TPR":"0001116132","CPRI":"0001530721"}
T={"REV":["RevenueFromContractWithCustomerExcludingAssessedTax","Revenues","SalesRevenueNet"],
   "COGS":["CostOfGoodsAndServicesSold","CostOfRevenue","CostOfGoodsSold"],
   "OPINC":["OperatingIncomeLoss"],
   "NI":["NetIncomeLoss"],
   "EQ":["StockholdersEquity"],
   "ASSETS":["Assets"],
   "GW":["Goodwill"],
   "INTANG":["IntangibleAssetsNetExcludingGoodwill","FiniteLivedIntangibleAssetsNet"],
   "OCF":["NetCashProvidedByUsedInOperatingActivities"],
   "CAPEX":["PaymentsToAcquirePropertyPlantAndEquipment"],
   "DA":["DepreciationDepletionAndAmortization","DepreciationAndAmortization"],
   "SBC":["ShareBasedCompensation"]}
for tk,cik in peers.items():
    d=facts(cik,tk); g=d["facts"]["us-gaap"]
    res={k:ann(g,v,pit=k in("EQ","ASSETS","GW","INTANG")) for k,v in T.items()}
    ends=sorted(set(res["REV"])|set(res["OPINC"]))[-4:]
    print("=== "+tk+" "+d["entityName"])
    for e in ends:
        rev=res["REV"].get(e,(None,))[0]; cogs=res["COGS"].get(e,(None,))[0]
        op=res["OPINC"].get(e,(None,))[0]; ni=res["NI"].get(e,(None,))[0]
        eq=res["EQ"].get(e,(None,))[0]; a=res["ASSETS"].get(e,(None,))[0]
        gw=res["GW"].get(e,(0,))[0] or 0; it=res["INTANG"].get(e,(0,))[0] or 0
        gm = (1-cogs/rev)*100 if rev and cogs else None
        om = op/rev*100 if rev and op is not None else None
        roe = ni/eq*100 if ni is not None and eq else None
        print(f"  {e}  rev {rev if rev else 0:8.1f}  GM% {gm if gm else 0:6.1f}  OM% {om if om is not None else 0:6.1f}  NI {ni if ni is not None else 0:8.1f}  EQ {eq if eq else 0:8.1f}  ROE% {roe if roe is not None else 0:6.1f}  GW+INT {gw+it:7.1f}  OCF {res['OCF'].get(e,(0,))[0]:7.1f} CAPEX {res['CAPEX'].get(e,(0,))[0]:6.1f} DA {res['DA'].get(e,(0,))[0]:6.1f} SBC {res['SBC'].get(e,(0,))[0]:6.1f}")
