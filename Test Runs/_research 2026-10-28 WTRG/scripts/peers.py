import json, sys
sys.path.insert(0, "scripts")
from fetch import get
peers = {"AWK":"0001410636","AWR":"0001056903","CWT":"0001035201","WTRG":"0000078128"}
def ann(facts, tag, fy):
    try: units = facts["facts"]["us-gaap"][tag]["units"]["USD"]
    except KeyError: return None, None
    best=None
    for u in units:
        if u.get("form")=="10-K" and u.get("fp")=="FY" and u["end"].startswith(str(fy)) and u["end"][5:7]=="12":
            if "start" in u and not u["start"].startswith(str(fy)): continue
            if best is None or u["filed"]>best["filed"]: best=u
    return (best["val"], best["accn"]) if best else (None,None)
for t,c in peers.items():
    d=json.loads(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json"))
    print(t)
    for fy in range(2020,2026):
        ni,a1=ann(d,"NetIncomeLoss",fy)
        if ni is None: ni,a1=ann(d,"NetIncomeLossAvailableToCommonStockholdersBasic",fy)
        eq,a2=ann(d,"StockholdersEquity",fy)
        cx,a3=ann(d,"PaymentsToAcquirePropertyPlantAndEquipment",fy)
        if cx is None: cx,a3=ann(d,"PaymentsToAcquireProductiveAssets",fy)
        dep,a4=ann(d,"DepreciationDepletionAndAmortization",fy)
        if dep is None: dep,a4=ann(d,"DepreciationAndAmortization",fy)
        if dep is None: dep,a4=ann(d,"Depreciation",fy)
        rev,a5=ann(d,"Revenues",fy)
        if rev is None: rev,a5=ann(d,"RevenueFromContractWithCustomerIncludingAssessedTax",fy)
        f=lambda x: "-" if x is None else f"{x/1e6:,.1f}"
        print(fy, "NI",f(ni),"EQ",f(eq),"CAPEX",f(cx),"DEP",f(dep),"REV",f(rev), a1)
