import json
d=json.load(open('companyfacts.json'))['facts']['us-gaap']
tags=['NetCashProvidedByUsedInOperatingActivities','ShareBasedCompensation','AllocatedShareBasedCompensationExpense','PaymentsToAcquirePropertyPlantAndEquipment','DepreciationDepletionAndAmortization','DepreciationAndAmortization','AmortizationOfIntangibleAssets','NetIncomeLossAttributableToNoncontrollingInterest','MinorityInterestDecreaseFromDistributionsToNoncontrollingInterestHolders','PaymentsToMinorityShareholders','PaymentsToAcquireBusinessesNetOfCashAcquired','Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','OperatingIncomeLoss','ProfitLoss','NetIncomeLoss','StockholdersEquity','ImpairmentOfLongLivedAssetsHeldForUse','RepaymentsOfLongTermCapitalLeaseObligations','FinanceLeasePrincipalPayments']
out={}
for t in tags:
    if t not in d: print('MISSING',t); continue
    s={}
    for u,v in d[t]['units'].items():
        for f in v:
            if f.get('fp')=='FY' and f['form'] in('10-K','10-K/A') and 'start' in f:
                y=int(f['end'][:4]); days=(int(f['end'][:4])-int(f['start'][:4]))
                if f['end'][5:]=='12-31' and f['start'][5:]=='01-01' and days==0:
                    s[y]=f['val']/1e6  # last filed vintage wins (sorted by filed)
    out[t]=s
    print(t, {k:round(v,1) for k,v in sorted(s.items())})
json.dump(out,open('xbrl_series.json','w'),indent=1)
