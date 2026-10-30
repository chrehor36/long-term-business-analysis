import json, collections
d=json.load(open("facts.json"))["facts"]["us-gaap"]
def series(tags, unit="USD", dur=True):
    out={}
    for t in tags:
        if t not in d: continue
        for u,vals in d[t]["units"].items():
            if u!=unit: continue
            for v in vals:
                if v.get("form") not in ("10-K","10-K/A"): continue
                fy_end=v["end"]
                if dur:
                    if "start" not in v: continue
                    from datetime import date
                    s=date.fromisoformat(v["start"]); e=date.fromisoformat(v["end"])
                    if not (350<=(e-s).days<=380): continue
                if not fy_end.endswith("09-30"): continue
                y=int(fy_end[:4])
                # keep first-filed value per year
                key=y
                if key not in out or v["filed"]<out[key][1]:
                    out[key]=(v["val"],v["filed"],t,v["accn"])
    return out
rows={
 "sales":["Revenues","SalesRevenueNet","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueGoodsNet"],
 "opinc":["OperatingIncomeLoss"],
 "netinc":["NetIncomeLoss"],
 "interest":["InterestExpense","InterestExpenseNonoperating","InterestExpenseDebt"],
 "ocf":["NetCashProvidedByUsedInOperatingActivities","NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
 "capex":["PaymentsToAcquirePropertyPlantAndEquipment"],
 "da":["DepreciationDepletionAndAmortization","DepreciationAndAmortization"],
 "sbc":["ShareBasedCompensation"],
 "buyback":["PaymentsForRepurchaseOfCommonStock"],
 "acq":["PaymentsToAcquireBusinessesNetOfCashAcquired"],
 "tax":["IncomeTaxExpenseBenefit"],
}
S={k:series(v) for k,v in rows.items()}
yrs=sorted(set().union(*[set(s) for s in S.values()]))
print("FY    "+"".join(f"{k:>10}" for k in rows))
for y in yrs:
    print(f"{y}  "+"".join(f"{(S[k][y][0]/1e6 if y in S[k] else float('nan')):10.1f}" for k in rows))
# shares
sh=series(["CommonStockSharesOutstanding"],unit="shares",dur=False)
wd=series(["WeightedAverageNumberOfDilutedSharesOutstanding"],unit="shares")
print("shares outstanding / diluted wtd")
for y in sorted(set(sh)|set(wd)):
    print(y, sh.get(y,(float('nan'),))[0]/1e6 if y in sh else '-', wd[y][0]/1e6 if y in wd else '-')
