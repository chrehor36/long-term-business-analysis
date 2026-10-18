import json, urllib.request, os, sys
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
CIKS={'CLF':764065,'NUE':73309,'STLD':1022671,'X':1163302}
TAGS=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','OperatingIncomeLoss','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','DepreciationDepletionAndAmortization','DepreciationAndAmortization','StockholdersEquity','LongTermDebtNoncurrent','LongTermDebt','Assets','NetIncomeLoss','IncomeTaxExpenseBenefit','InterestExpense','InterestExpenseNonoperating','CashAndCashEquivalentsAtCarryingValue','ShareBasedCompensation','AllocatedShareBasedCompensationExpense','PaymentsToAcquireBusinessesNetOfCashAcquired','PaymentsForRepurchaseOfCommonStock','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments','GrossProfit','CostOfGoodsAndServicesSold','InterestPaidNet','IncomeTaxesPaidNet','IncomeTaxesPaid','NetIncomeLossAttributableToNoncontrollingInterest','PaymentsToMinorityShareholders','PaymentsOfDividendsMinorityInterest','DistributionMadeToLimitedLiabilityCompanyLLCMemberCashDistributionsPaid']
out={}
for t,c in CIKS.items():
    fn=f'cache/facts_{t}.json'
    if not os.path.exists(fn):
        url=f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json'
        open(fn,'wb').write(urllib.request.urlopen(urllib.request.Request(url,headers=UA)).read())
    d=json.load(open(fn))
    g=d['facts'].get('us-gaap',{})
    res={}
    for tag in TAGS:
        if tag not in g: continue
        for u,vals in g[tag]['units'].items():
            for v in vals:
                if v.get('fp')!='FY' or not v.get('form','').startswith('10-K'): continue
                end=v['end']
                if 'start' in v:
                    # annual only
                    from datetime import date
                    s=date.fromisoformat(v['start']); e=date.fromisoformat(end)
                    if (e-s).days<350 or (e-s).days>380: continue
                fy=end[:4]
                key=(tag,fy)
                # keep latest filed
                if key not in res or v['filed']>res[key][1]:
                    res[key]=(v['val'],v['filed'],v['accn'])
    out[t]=res
import pickle; pickle.dump(out,open('cache/peers.pkl','wb'))
for t,res in out.items():
    print('=====',t)
    tags=sorted(set(k[0] for k in res))
    for tag in tags:
        row=[]
        for fy in range(2014,2026):
            v=res.get((tag,str(fy)))
            row.append(f"{v[0]/1e6:9.0f}" if v else '        -')
        print(f"{tag[:48]:48s}"+''.join(row))
