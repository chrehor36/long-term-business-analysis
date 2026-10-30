import json, collections, sys
d=json.load(open("Test Runs/_research 2026-09-20 SIG/companyfacts.json"))
g=d["facts"]["us-gaap"]
def annual(tag):
    out={}
    if tag not in g: return out
    for unit,rows in g[tag]["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K","10-K/A"): continue
            if "start" not in r: continue
            from datetime import date
            s=date.fromisoformat(r["start"]); e=date.fromisoformat(r["end"])
            days=(e-s).days
            if not (330<days<400): continue
            key=r["end"]
            # prefer the most recently filed value
            prev=out.get(key)
            if prev is None or r["filed"]>prev[1]:
                out[key]=(r["val"]/1e6, r["filed"], r["accn"])
    return out
def pit(tag):
    out={}
    if tag not in g: return out
    for unit,rows in g[tag]["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K","10-K/A"): continue
            if "start" in r: continue
            key=r["end"]
            prev=out.get(key)
            if prev is None or r["filed"]>prev[1]:
                out[key]=(r["val"]/1e6, r["filed"], r["accn"])
    return out
tags={
 "OCF":["NetCashProvidedByUsedInOperatingActivities","NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
 "CAPEX":["PaymentsToAcquirePropertyPlantAndEquipment"],
 "DA":["DepreciationDepletionAndAmortization","DepreciationAndAmortization","DepreciationAmortizationAndAccretionNet"],
 "DEPonly":["Depreciation"],
 "SBC":["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"],
 "REV":["RevenueFromContractWithCustomerExcludingAssessedTax","Revenues","SalesRevenueNet"],
 "NI":["NetIncomeLoss"],
 "PRETAX":["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest","IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"],
 "CASHTAX":["IncomeTaxesPaidNet","IncomeTaxesPaid"],
 "EQUITY":["StockholdersEquity"],
 "ASSETS":["Assets"],
 "LIAB":["Liabilities"],
 "GOODWILL":["Goodwill"],
 "INTANG":["FiniteLivedIntangibleAssetsNet","IntangibleAssetsNetExcludingGoodwill"],
}
res={}
for k,tl in tags.items():
    m={}
    for t in tl:
        f = pit(t) if k in ("EQUITY","ASSETS","LIAB","GOODWILL","INTANG") else annual(t)
        for kk,vv in f.items():
            if kk not in m: m[kk]=vv
    res[k]=m
ends=sorted(set().union(*[set(v) for v in res.values()]))
cols=list(tags)
print("end      | "+" | ".join(f"{c:>9}" for c in cols))
for e in ends:
    row=[]
    for c in cols:
        v=res[c].get(e)
        row.append(f"{v[0]:9.1f}" if v else "        -")
    print(e+" | "+" | ".join(row))
