import json,os
from datetime import date
C=os.path.join(os.path.dirname(os.path.abspath(__file__)),"cache")
j=json.load(open(os.path.join(C,"facts_0000853816.json")))
allf={}
for ns in j["facts"]:
    allf.update(j["facts"][ns])
pt=[t for t in allf if "ransport" in t]
print("transport tags:",pt)
def annual(tag,dur=True):
    out={}
    if tag not in allf: return out
    for u,arr in allf[tag]["units"].items():
        for x in arr:
            if x.get("form") not in ("10-K","10-K/A"): continue
            e=date.fromisoformat(x["end"])
            if dur:
                if "start" not in x or (e-date.fromisoformat(x["start"])).days<350: continue
            y=e.year if e.month>1 else e.year-1
            if y not in out or x["filed"]<out[y][1]: out[y]=(x["val"],x["filed"])
    return {k:v[0] for k,v in out.items()}
T=[("intx","InterestAndDebtExpense",1),("intnet","InterestIncomeExpenseNonoperatingNet",1),("intexp","InterestExpense",1),("pretax","IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",1),("tax","IncomeTaxExpenseBenefit",1),("rev","Revenues",1),("PT",pt[0] if pt else "",1),("comm","SalesCommissionsAndFees",1),("ins","OperatingInsuranceAndClaimsCostsProduction",1),
("OI","OperatingIncomeLoss",1),("NI","NetIncomeLoss",1),("OCF","NetCashProvidedByUsedInOperatingActivities",1),("capex","PaymentsToAcquirePropertyPlantAndEquipment",1),
("DA","DepreciationAndAmortization",1),("SBC","ShareBasedCompensation",1),("bbk","PaymentsForRepurchaseOfCommonStock",1),("tsacq","TreasuryStockValueAcquiredCostMethod",1),
("divpaid","PaymentsOfDividends",1),("dps","CommonStockDividendsPerShareDeclared",1),("leasein","CapitalLeaseObligationsIncurred",1),("debtrepay","RepaymentsOfLongTermDebtAndCapitalSecurities",1),
("rec","ReceivablesNetCurrent",0),("ap","AccountsPayableCurrent",0),("resC","SelfInsuranceReserveCurrent",0),("resN","SelfInsuranceReserveNoncurrent",0),
("cash","CashAndCashEquivalentsAtCarryingValue",0),("sti","ShortTermInvestments",0),("lti","LongTermInvestments",0),("ltd","LongTermDebtAndCapitalLeaseObligations",0),("ltdc","LongTermDebtAndCapitalLeaseObligationsCurrent",0),
("flc","FinanceLeaseLiabilityCurrent",0),("fln","FinanceLeaseLiabilityNoncurrent",0),("eq","StockholdersEquity",0),("tss","TreasuryStockShares",0),("assets","Assets",0)]
D={k:annual(t,bool(d)) for k,t,d in T if t}
ys=range(2007,2026)
print("year "+" ".join(f"{k:>8}" for k,_,_ in T))
for y in ys:
    row=[]
    for k,_,_ in T:
        v=D.get(k,{}).get(y)
        row.append(f"{v:8.3f}" if (v is not None and abs(v)<1000) else (f"{v/1e6:8.1f}" if v is not None else "      na"))
    print(y," ".join(row))
