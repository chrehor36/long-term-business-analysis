import json,sys
def annual(facts, tags, fp_end_month=None):
    out={}
    g=facts["facts"].get("us-gaap",{})
    for tag in tags:
        if tag not in g: continue
        for unit,arr in g[tag]["units"].items():
            for x in arr:
                if x.get("form") not in ("10-K","10-K/A","10-KT"): continue
                if "frame" in x and x["frame"].startswith("CY") and len(x["frame"])==6:
                    y=int(x["frame"][2:])
                    out.setdefault(y,(x["val"],tag,x["accn"]))
                elif "start" not in x and "frame" in x and x["frame"].endswith("I") and len(x["frame"])==9:
                    pass
    return out
def inst(facts,tags):
    out={}
    g=facts["facts"].get("us-gaap",{})
    for tag in tags:
        if tag not in g: continue
        for unit,arr in g[tag]["units"].items():
            for x in arr:
                if x.get("form") not in ("10-K","10-K/A"): continue
                f=x.get("frame","")
                if f.startswith("CY") and f.endswith("Q4I"):
                    y=int(f[2:6]); out.setdefault(y,(x["val"],tag,x["accn"]))
    return out
if __name__=="__main__":
    f=json.load(open(sys.argv[1]))
    rows={
     "Sales":["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet","SalesRevenueGoodsNet"],
     "OpInc":["OperatingIncomeLoss"],
     "PretaxCont":["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest","IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"],
     "NetInc":["NetIncomeLoss"],
     "OCF":["NetCashProvidedByUsedInOperatingActivities"],
     "OCFcont":["NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
     "Capex":["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"],
     "DA":["DepreciationDepletionAndAmortization","DepreciationAmortizationAndAccretionNet","DepreciationAndAmortization"],
     "SBC":["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"],
     "Acq":["PaymentsToAcquireBusinessesNetOfCashAcquired"],
     "Buyback":["PaymentsForRepurchaseOfCommonStock"],
     "Impair":["GoodwillImpairmentLoss","GoodwillAndIntangibleAssetImpairment","ImpairmentOfIntangibleAssetsExcludingGoodwill"],
    }
    res={k:annual(f,v) for k,v in rows.items()}
    ys=sorted(set(y for d in res.values() for y in d))
    ys=[y for y in ys if y>=2012]
    print("year  "+"  ".join(f"{k:>10}" for k in rows))
    for y in ys:
        print(y, "  ".join(f"{(res[k][y][0]/1e6 if y in res[k] else float('nan')):10.1f}" for k in rows))
    bs={"Equity":["StockholdersEquity"],"Goodwill":["Goodwill"],"Intang":["IntangibleAssetsNetExcludingGoodwill","FiniteLivedIntangibleAssetsNet"],"Assets":["Assets"],"Cash":["CashAndCashEquivalentsAtCarryingValue"],"LTD":["LongTermDebtNoncurrent","LongTermDebt"]}
    r2={k:inst(f,v) for k,v in bs.items()}
    ys=sorted(set(y for d in r2.values() for y in d)); ys=[y for y in ys if y>=2012]
    print("year  "+"  ".join(f"{k:>10}" for k in bs))
    for y in ys:
        print(y, "  ".join(f"{(r2[k][y][0]/1e6 if y in r2[k] else float('nan')):10.1f}" for k in bs))
