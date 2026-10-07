import json
f=json.load(open("Test Runs/_research 2026-09-13 RGTI/companyfacts.json"))
g=f["facts"]["us-gaap"]
SHELL="0001564590-22-006345"
def dur(tag, start, end):
    if tag not in g: return None
    best=None
    for u,rows in g[tag]["units"].items():
        for r in rows:
            if r.get("start")==start and r["end"]==end and r["accn"]!=SHELL:
                if best is None or r["filed"]>best["filed"]: best=r
    return best["val"] if best else None
def inst(tag, end):
    if tag not in g: return None
    best=None
    for u,rows in g[tag]["units"].items():
        for r in rows:
            if r["end"]==end and "start" not in r and r["accn"]!=SHELL:
                if best is None or r["filed"]>best["filed"]: best=r
    return best["val"] if best else None
P=[("FY21(11m)","2021-02-01","2021-12-31"),("FY22","2022-01-01","2022-12-31"),("FY23","2023-01-01","2023-12-31"),
   ("FY24","2024-01-01","2024-12-31"),("FY25","2025-01-01","2025-12-31"),("H1-25","2025-01-01","2025-06-30"),("H1-26","2026-01-01","2026-06-30")]
T=["RevenueFromContractWithCustomerIncludingAssessedTax","Revenues","CostOfRevenue","OperatingExpenses","OperatingIncomeLoss","NetIncomeLoss",
   "NetCashProvidedByUsedInOperatingActivities","ShareBasedCompensation","AllocatedShareBasedCompensationExpense","PaymentsToAcquirePropertyPlantAndEquipment",
   "DepreciationDepletionAndAmortization","Depreciation","FairValueAdjustmentOfWarrants","ProceedsFromIssuanceOfCommonStock","ProceedsFromWarrantExercises",
   "ProceedsFromStockOptionsExercised","NetCashProvidedByUsedInFinancingActivities","ProceedsFromNotesPayable"]
print("tag".ljust(55)+"".join(p[0].rjust(13) for p in P))
for t in T:
    print(t[:55].ljust(55)+"".join((f"{dur(t,s,e)/1e3:,.0f}" if dur(t,s,e) is not None else "-").rjust(13) for _,s,e in P))
for t in ["CashAndCashEquivalentsAtCarryingValue","AvailableForSaleSecuritiesDebtSecuritiesCurrent","DebtSecuritiesAvailableForSaleExcludingAccruedInterestCurrent","DebtSecuritiesAvailableForSaleExcludingAccruedInterestNoncurrent","AvailableForSaleSecuritiesDebtSecuritiesNoncurrent","StockholdersEquity","RevenueRemainingPerformanceObligation","OperatingLeaseLiability"]:
    print(t[:55].ljust(55)+"".join((f"{inst(t,e)/1e3:,.0f}" if inst(t,e) is not None else "-").rjust(13) for e in ["2021-12-31","2022-12-31","2023-12-31","2024-12-31","2025-12-31","2026-06-30"]))
