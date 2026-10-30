import json,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
d=json.load(open('companyfacts.json'))['facts']['us-gaap']
flow=['NetCashProvidedByUsedInOperatingActivities','ShareBasedCompensation','PaymentsToAcquirePropertyPlantAndEquipment','Depreciation','AmortizationOfIntangibleAssets','Revenues','OperatingIncomeLoss','NetIncomeLoss','IncomeTaxesPaidNet','InterestPaidNet','PaymentsForRepurchaseOfCommonStock','PaymentsOfDividends','PaymentsToAcquireBusinessesNetOfCashAcquired','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments','MinorityInterest','NetIncomeLossAttributableToNoncontrollingInterest','DefinedContributionPlanCostRecognized','DefinedBenefitPlanContributionsByEmployer']
inst=['StockholdersEquity','LongTermDebt','LongTermDebtNoncurrent','CashAndCashEquivalentsAtCarryingValue','Goodwill','IntangibleAssetsNetExcludingGoodwill','ContractWithCustomerLiability','ContractWithCustomerLiabilityCurrent','ContractWithCustomerAssetNet','Assets','LongTermDebtCurrent','DebtCurrent']
out={}
def first_last(t,isflow):
    s={}
    for u,v in d[t]['units'].items():
        for f in sorted(v,key=lambda f:f['filed']):
            if f['form'] not in('10-K','10-K/A'): continue
            if isflow:
                if 'start' not in f: continue
                if not(f['start'][5:]=='01-01' and f['end'][5:]=='12-31' and f['start'][:4]==f['end'][:4]): continue
            else:
                if f['end'][5:]!='12-31': continue
            y=int(f['end'][:4]); s.setdefault(y,[f['val']/1e6,None]); s[y][1]=f['val']/1e6
    return s
for t in flow+inst:
    if t not in d: print('MISSING',t); continue
    s=first_last(t,t in flow); out[t]=s
    print(t, {k:(round(v[0]),round(v[1])) if v[0]!=v[1] else round(v[0]) for k,v in sorted(s.items())})
json.dump(out,open('xbrl_series.json','w'),indent=0)
