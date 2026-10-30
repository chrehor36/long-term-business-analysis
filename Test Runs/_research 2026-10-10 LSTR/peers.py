import json, os, sys, time, urllib.request
from datetime import date
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
C=os.path.join(os.path.dirname(os.path.abspath(__file__)),"cache")
P={"LSTR":853816,"CHRW":1043277,"JBHT":728535,"WERN":793074,"KNX":1492691,"KNXold":929452,"RXO":1929561,"SNDR":1692063,"HUBG":940942}
def facts(cik):
    p=os.path.join(C,f"facts_{cik:010d}.json")
    if not os.path.exists(p):
        b=urllib.request.urlopen(urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json",headers=UA),timeout=120).read()
        open(p,"wb").write(b); time.sleep(0.3)
    return json.load(open(p))
def annual(g,tag,dur=True):
    out={}
    if tag not in g: return out
    for u,arr in g[tag]["units"].items():
        for x in arr:
            if x.get("form") not in ("10-K","10-K/A"): continue
            e=date.fromisoformat(x["end"])
            if dur:
                if "start" not in x: continue
                if (e-date.fromisoformat(x["start"])).days<350: continue
            y=e.year if e.month>1 else e.year-1
            # first-filed vintage
            if y not in out or x["filed"]<out[y][2]:
                out[y]=(x["val"],x["accn"],x["filed"])
    return out
def first(g,tags,dur=True):
    res={}
    for t in tags:
        for y,v in annual(g,t,dur).items():
            res.setdefault(y,v+(t,))
    return res
rows={}
SEL=sys.argv[1:] or list(P)
for k,cik in [(k,P[k]) for k in SEL]:
    try: j=facts(cik)
    except Exception as e: print(k,"ERR",e); continue
    g=j["facts"].get("us-gaap",{})
    rev=first(g,["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet","SalesRevenueServicesNet"])
    oi=first(g,["OperatingIncomeLoss"])
    ni=first(g,["NetIncomeLoss","ProfitLoss"])
    eq=first(g,["StockholdersEquity","StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],False)
    at=first(g,["Assets"],False)
    gw=first(g,["Goodwill"],False)
    ltd=first(g,["LongTermDebtNoncurrent","LongTermDebt","LongTermDebtAndCapitalLeaseObligations","LongTermLineOfCredit"],False)
    cash=first(g,["CashAndCashEquivalentsAtCarryingValue"],False)
    ocf=first(g,["NetCashProvidedByUsedInOperatingActivities"])
    capex=first(g,["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"])
    print(f"== {k} (CIK {cik}) {j.get('entityName')}")
    print("year  revenue  opinc  opmargin  netinc  equity  goodwill  ltdebt  cash  OCF  capex  ROE  OI/(eq+ltd-cash)")
    for y in range(2005,2026):
        r=rev.get(y,(None,))[0]; o=oi.get(y,(None,))[0]; n=ni.get(y,(None,))[0]; e=eq.get(y,(None,))[0]
        gg=gw.get(y,(None,))[0]; d=ltd.get(y,(None,))[0]; c=cash.get(y,(None,))[0]; of=ocf.get(y,(None,))[0]; cx=capex.get(y,(None,))[0]
        if r is None and o is None: continue
        f=lambda v: f"{v/1e6:8.1f}" if v is not None else "      na"
        om=f"{o/r*100:6.1f}%" if (o is not None and r) else "    na"
        roe=f"{n/e*100:6.1f}%" if (n is not None and e) else "    na"
        cap=(e or 0)+(d or 0)-(c or 0)
        roc=f"{o/cap*100:6.1f}%" if (o is not None and e) and cap>0 else "    na"
        print(y,f(r),f(o),om,f(n),f(e),f(gg),f(d),f(c),f(of),f(cx),roe,roc)
