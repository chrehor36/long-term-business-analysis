import json, os, sys
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
OUT=os.path.dirname(os.path.abspath(__file__))
FILES={"PINS":"companyfacts.json","META":"cf_META.json","GOOGL":"cf_GOOGL.json",
       "SNAP":"cf_SNAP.json","RDDT":"cf_RDDT.json","TTD":"cf_TTD.json"}
DUR=["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","OperatingIncomeLoss",
 "NetIncomeLoss","NetCashProvidedByUsedInOperatingActivities","ShareBasedCompensation",
 "PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets",
 "DepreciationDepletionAndAmortization","DepreciationAndAmortization","Depreciation",
 "AmortizationOfIntangibleAssets","DepreciationAmortizationAndAccretionNet",
 "AllocatedShareBasedCompensationExpense","PaymentsForRepurchaseOfCommonStock",
 "RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability","FinanceLeasePrincipalPayments"]
INST=["CashAndCashEquivalentsAtCarryingValue","MarketableSecuritiesCurrent","ShortTermInvestments",
 "MarketableSecuritiesNoncurrent","LongTermDebtNoncurrent","LongTermDebt","ConvertibleDebtNoncurrent",
 "ConvertibleNotesPayableNoncurrent","OperatingLeaseLiabilityNoncurrent","OperatingLeaseLiabilityCurrent",
 "FinanceLeaseLiabilityNoncurrent","FinanceLeaseLiabilityCurrent","PropertyPlantAndEquipmentNet",
 "StockholdersEquity","Assets","Liabilities","AvailableForSaleSecuritiesDebtSecuritiesCurrent",
 "AvailableForSaleSecuritiesDebtSecuritiesNoncurrent","DebtSecuritiesAvailableForSaleCurrent",
 "DebtSecuritiesAvailableForSaleNoncurrent","LongTermDebtCurrent","DebtCurrent","DebtLongtermAndShorttermCombinedAmount"]
for tk,fn in FILES.items():
    cf=json.load(open(os.path.join(OUT,fn)))
    us=cf["facts"].get("us-gaap",{})
    print(f"\n########## {tk} — {cf.get('entityName')} ##########")
    for t in DUR:
        d=us.get(t)
        if not d: continue
        out={}
        for unit,rows in d["units"].items():
            for r in rows:
                if r.get("form")!="10-K" or r.get("fp")!="FY": continue
                st,en=r.get("start"),r.get("end")
                if not st or not en: continue
                if not (330<=(date.fromisoformat(en)-date.fromisoformat(st)).days<=400): continue
                if en<"2022-01-01": continue
                if en not in out or r["accn"]>out[en][1]: out[en]=(r["val"],r["accn"])
        if out:
            print(f"  {t}: "+"  ".join(f"{k[:4]}={v[0]/1e6:,.1f}[{v[1][-6:]}]" for k,v in sorted(out.items())))
    print("  --- instants ---")
    for t in INST:
        d=us.get(t)
        if not d: continue
        out={}
        for unit,rows in d["units"].items():
            for r in rows:
                if r.get("form")!="10-K" or "start" in r: continue
                en=r["end"]
                if en<"2023-12-01": continue
                if en not in out or r["accn"]>out[en][1]: out[en]=(r["val"],r["accn"])
        if out:
            print(f"  {t}: "+"  ".join(f"{k}={v[0]/1e6:,.1f}" for k,v in sorted(out.items())))
