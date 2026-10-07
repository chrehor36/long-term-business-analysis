import json
d=json.load(open('companyfacts.json'))['facts']['us-gaap']
def ann(tag):
    if tag not in d: return {}
    out={}
    for u,v in d[tag]['units'].items():
        for x in v:
            if x.get('form')=='10-K' and x.get('fp')=='FY' and x.get('frame','').startswith('CY') and len(x['frame'])==6:
                out[int(x['frame'][2:])]=x['val']
    return out
tags=['NetCashProvidedByUsedInOperatingActivities','ShareBasedCompensation','PaymentsToAcquirePropertyPlantAndEquipment','DepreciationDepletionAndAmortization','DepreciationAndAmortization','AmortizationOfIntangibleAssets','ProceedsFromSaleOfPropertyPlantAndEquipment','PaymentsToAcquireBusinessesNetOfCashAcquired','InterestPaidNet','IncomeTaxesPaidNet','NetIncomeLoss','StockholdersEquity','LongTermDebt','PaymentsForRepurchaseOfCommonStock','MinorityInterest','FinanceLeasePrincipalPayments']
for t in tags:
    a=ann(t); print(t, {k:round(v/1e6,1) for k,v in sorted(a.items())})
