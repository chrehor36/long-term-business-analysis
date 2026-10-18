import json,sys
names={"0001443646":"BAH","0000016058":"CACI","0001357615":"KBR"}
tags={"rev":["RevenueFromContractWithCustomerExcludingAssessedTax","Revenues","SalesRevenueServicesNet"],
"oi":["OperatingIncomeLoss"],
"amort":["AmortizationOfIntangibleAssets"],
"da":["DepreciationDepletionAndAmortization","DepreciationAndAmortization","DepreciationAmortizationAndAccretionNet","DepreciationAmortizationAndOther"],
"ocf":["NetCashProvidedByUsedInOperatingActivities","NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
"capex":["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"],
"sbc":["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"],
"acq":["PaymentsToAcquireBusinessesNetOfCashAcquired"],
"gw":["Goodwill"],"intg":["IntangibleAssetsNetExcludingGoodwill","FiniteLivedIntangibleAssetsNet"],
"assets":["Assets"],"eq":["StockholdersEquity","StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],
"cash":["CashAndCashEquivalentsAtCarryingValue"],
"debt":["LongTermDebt","LongTermDebtNoncurrent","DebtInstrumentCarryingAmount"],
"ltdnc":["LongTermDebtNoncurrent"],"ltdc":["LongTermDebtCurrent"],
}
def series(facts,taglist,annual=True,instant=False):
    out={}
    for t in taglist:
        f=facts["facts"].get("us-gaap",{}).get(t)
        if not f: continue
        for u,vals in f["units"].items():
            if u!="USD": continue
            for v in vals:
                if v.get("form") not in ("10-K","10-K/A"): continue
                if not instant:
                    if "start" not in v: continue
                    from datetime import date
                    s=date.fromisoformat(v["start"]); e=date.fromisoformat(v["end"])
                    if not 340<=(e-s).days<=380: continue
                key=v["end"][:7]
                if key not in out: out[key]=v["val"]
    return out,"merged" 
for cik,n in names.items():
    d=json.load(open(f"cache/facts_{cik}.json"))
    print("=====",n,d["entityName"])
    res={}
    for k,tl in tags.items():
        inst=k in ("gw","intg","assets","eq","cash","debt","ltdnc","ltdc")
        s,t=series(d,tl,instant=inst); res[k]=(s,t)
    ends=sorted(res["rev"][0].keys())[-11:]
    print("tags:",{k:v[1] for k,v in res.items()})
    hdr=["end"]+list(tags.keys())
    print(" ".join(f"{h:>8}" for h in hdr))
    for e in ends:
        row=[e]
        for k in tags:
            v=res[k][0].get(e)
            row.append("" if v is None else f"{v/1e6:.0f}")
        print(" ".join(f"{x:>8}" for x in row))
