"""Competitor ROE from SEC companyfacts: earnings attributable to common / average common equity, FY 10-K values, latest filing per FY end."""
import json, os, sys
here=os.path.dirname(os.path.abspath(__file__))
names={"0000004904":"AEP","0000922224":"PPL","0001109357":"EXC","0001031296":"FE"}
def series(facts, tag):
    out={}
    u=facts["facts"]["us-gaap"].get(tag,{}).get("units",{}).get("USD",[])
    for x in u:
        if x.get("form")!="10-K": continue
        if tag.startswith("StockholdersEquity"):
            key=x["end"]
        else:
            if x.get("fp")!="FY" or not x.get("start"): continue
            from datetime import date
            s=date.fromisoformat(x["start"]); e=date.fromisoformat(x["end"])
            if (e-s).days<350: continue
            key=x["end"]
        # keep the latest-filed value for each period end
        if key not in out or x["filed"]>out[key][1]:
            out[key]=(x["val"],x["filed"],x["accn"])
    return out
for cik,n in names.items():
    f=json.load(open(os.path.join(here,"cache",f"facts_{cik}.json")))
    ni={}
    for t in ["NetIncomeLossAvailableToCommonStockholdersBasic","NetIncomeLoss"]:
        for k,v in series(f,t).items(): ni.setdefault(k,v+(t,))
    eq={}
    for t in ["StockholdersEquity","StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"]:
        for k,v in series(f,t).items(): eq.setdefault(k,v+(t,))
    print("==",n)
    for y in range(2020,2026):
        e=f"{y}-12-31"; p=f"{y-1}-12-31"
        if e in ni and e in eq and p in eq:
            avg=(eq[e][0]+eq[p][0])/2
            print(y, "NI %6.0f"%(ni[e][0]/1e6), "Eq %7.0f"%(eq[e][0]/1e6), "ROE %.1f%%"%(100*ni[e][0]/avg), ni[e][2], ni[e][3][:22], eq[e][3][:30])
