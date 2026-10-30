import json
from datetime import date
d=json.load(open("facts.json")); g=d["facts"]["us-gaap"]
def annual(*tags):
    out={}
    for t in tags:
        if t not in g: continue
        for u,vals in g[t]["units"].items():
            for v in vals:
                if v.get("fp")=="FY" and v["form"].startswith("10-K") and "start" in v:
                    s=date.fromisoformat(v["start"]); e=date.fromisoformat(v["end"])
                    if 350<(e-s).days<380: out.setdefault(int(v["end"][:4]),v["val"]/1e6)
    return out
ocf=annual("NetCashProvidedByUsedInOperatingActivities")
sbc=annual("StockIssuedDuringPeriodValueShareBasedCompensation","ShareBasedCompensation")
cap=annual("PaymentsToAcquirePropertyPlantAndEquipment")
da=annual("DepreciationDepletionAndAmortization")
amort=annual("AmortizationOfIntangibleAssets")
acq=annual("PaymentsToAcquireBusinessesNetOfCashAcquired")
acq[2017]=803.8  # Fleet, net cash per FY2017 10-K text (XBRL tag 0)
div=annual("ProceedsFromDivestitureOfBusinesses")
bb=annual("PaymentsForRepurchaseOfCommonStock")
rev=annual("RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet")
oi=annual("OperatingIncomeLoss"); gp=annual("GrossProfit")
sh=annual("WeightedAverageNumberOfDilutedSharesOutstanding")
tax=annual("IncomeTaxExpenseBenefit"); intp=annual("InterestPaidNet","InterestPaid")
print("FY   rev    GM%   OI    OCF   SBC  capex  D&A  amort  OEcapex OE_DA  acq   divest  buyback  dilShares")
cum=0;cumoe=0
for y in range(2010,2027):
    oe=ocf[y]-sbc.get(y,0)-cap[y]; oed=ocf[y]-sbc.get(y,0)-da[y]
    a=acq.get(y,0) or 0; dv=div.get(y,0) or 0
    print(f"{y} {rev[y]:7.1f} {100*gp[y]/rev[y]:5.1f} {oi[y]:6.1f} {ocf[y]:6.1f} {sbc.get(y,0):5.1f} {cap[y]:5.1f} {da[y]:5.1f} {amort.get(y,0):5.1f} {oe:7.1f} {oed:6.1f} {a:6.1f} {dv:6.1f} {bb.get(y,0) or 0:7.1f} {sh[y]/1 if sh[y]<1000 else sh[y]/1e6:6.2f}")
