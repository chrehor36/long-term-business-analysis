from facts import load, annual
d = load("ACM")
tags = ["NetCashProvidedByUsedInOperatingActivities","NetCashProvidedByUsedInOperatingActivitiesContinuingOperations","ShareBasedCompensation","AllocatedShareBasedCompensationExpense",
 "PaymentsToAcquirePropertyPlantAndEquipment","DepreciationDepletionAndAmortization","DepreciationAndAmortization","FinanceLeasePrincipalPayments",
 "PaymentsToMinorityShareholders","PaymentsOfDistributionsToAffiliates","PaymentsToAcquireBusinessesNetOfCashAcquired","PaymentsForRepurchaseOfCommonStock","PaymentsOfDividendsCommonStock",
 "Revenues","OperatingIncomeLoss","IncomeTaxesPaidNet","InterestPaidNet","IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest","IncomeTaxExpenseBenefit","InterestExpense","WeightedAverageNumberOfDilutedSharesOutstanding",
 "ProceedsFromDivestitureOfBusinessesNetOfCashDivested","ProceedsFromSaleOfBusinessNet","ProceedsFromDivestitureOfBusinesses"]
for t in tags:
    a = annual(d, t) if "Shares" not in t else annual(d, t, unit="shares")
    if not a: print(t, "-"); continue
    print(t); [print("  ", k, round(v[0]/1e6,1), v[2]) for k, v in a.items() if k >= "2015"]
