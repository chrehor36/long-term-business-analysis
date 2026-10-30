import json
f=json.load(open("companyfacts.json"))["facts"]["us-gaap"]
tags=["NetCashProvidedByUsedInOperatingActivities","ShareBasedCompensation","AllocatedShareBasedCompensationExpense","DepreciationDepletionAndAmortization","DepreciationAmortizationAndAccretionNet","PaymentsToAcquirePropertyPlantAndEquipment","PaymentsForSoftware","PaymentsToDevelopSoftware","PaymentsToAcquireBusinessesNetOfCashAcquired","IncreaseDecreaseInAccountsPayableAndAccruedLiabilities","AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisiteServicePeriodRecognitionValue"]
for t in tags:
    if t not in f: print(t,"--absent"); continue
    rows={}
    for u in f[t]["units"].values():
        for x in u:
            if x.get("fp")=="FY" and x["form"].startswith("10-K") and "start" in x:
                from datetime import date
                d=(date.fromisoformat(x["end"])-date.fromisoformat(x["start"])).days
                if 340<d<380:
                    rows.setdefault(x["end"][:4],[]).append((x["filed"],x["val"],x["accn"]))
    print(t)
    for y in sorted(rows):
        v=sorted(set(rows[y]))
        print("  ",y,"earliest",v[0][1],"newest",v[-1][1], "(filed",v[-1][0],")" if True else "")
