import json
d=json.load(open('companyfacts.json'))['facts']['us-gaap']
def annual(tag):
    if tag not in d: return {}
    out={}
    for u,arr in d[tag]['units'].items():
        for x in arr:
            if x.get('form') in ('10-K','10-KT') and x.get('fp')=='FY' and 'start' in x:
                from datetime import date
                s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                if 340<(e-s).days<380:
                    out[x['end']]=x['val']  # later filings overwrite -> latest vintage
    return out
tags=['NetCashProvidedByUsedInOperatingActivities','ShareBasedCompensation','AmortizationOfIntangibleAssets','Depreciation','DepreciationDepletionAndAmortization','DepreciationAmortizationAndAccretionNet','PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireEquipmentOnLease','FinanceLeasePrincipalPayments','InterestPaidNet','InterestPaid','Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','OperatingIncomeLoss','PaymentsToAcquireBusinessesNetOfCashAcquired','IncreaseDecreaseInContractWithCustomerLiability','IncreaseDecreaseInCustomerAdvances','MinorityInterest','NetIncomeLossAttributableToNoncontrollingInterest']
for t in tags:
    a=annual(t)
    if a: print(t, {k[:7]:round(v/1e6,1) for k,v in sorted(a.items())})
