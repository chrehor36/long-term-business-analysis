import json,sys
from datetime import date
TAGS={"rev":["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax"],
 "opinc":["OperatingIncomeLoss"],
 "ocf":["NetCashProvidedByUsedInOperatingActivities","NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
 "capex":["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsForCapitalImprovements","PaymentsToAcquireProductiveAssets"],
 "sbc":["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"],
 "flp":["FinanceLeasePrincipalPayments","RepaymentsOfLongTermCapitalLeaseObligations"],
 "fop":["RepaymentsOfFinancingObligation","PaymentsOfFinancingObligations","RepaymentsOfDebtFinancingObligation"],
 "ni":["NetIncomeLoss"],
}
def series(f,keys):
    d=json.load(open(f)); g=d["facts"].get("us-gaap",{})
    out={}
    for k in keys:
        best={}
        for t in TAGS[k]:
            if t not in g: continue
            for unit,u in g[t]["units"].items():
                if unit!="USD": continue
                for x in u:
                    if x.get("form") not in ("10-K","10-K/A","20-F") or "start" not in x: continue
                    a=date.fromisoformat(x["start"]); b=date.fromisoformat(x["end"])
                    if not (340<=(b-a).days<=380): continue
                    fy=x["end"][:4]
                    # prefer first tag in list, latest filed (restated) within tag
                    if fy not in best: best[fy]=(t,x)
                    elif best[fy][0]==t and x["filed"]>best[fy][1]["filed"]: best[fy]=(t,x)
        out[k]={fy:round(v[1]["val"]/1e6,1) for fy,v in sorted(best.items())}
    return out
if __name__=="__main__":
    s=series(sys.argv[1],["rev","opinc","ocf","capex","sbc","flp","fop","ni"])
    for k,v in s.items(): print(k,v)
