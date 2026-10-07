import sys
sys.path.insert(0,'../../tools')
import sources as S
f=S.sec_facts('0001437226')
tags={'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueServicesNet','SalesRevenueNet'],
'gp':['GrossProfit'],'oi':['OperatingIncomeLoss'],'ni':['NetIncomeLoss'],'eq':['StockholdersEquity'],'gw':['Goodwill'],
'ia':['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'],'cash':['CashAndCashEquivalentsAtCarryingValue'],'ta':['Assets'],
'ar':['AccountsReceivableNetCurrent'],'sh':['WeightedAverageNumberOfSharesOutstandingBasic'],'tax':['IncomeTaxesPaidNet','IncomeTaxesPaid'],'pti':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments']}
res={}
for k,t in tags.items():
    try:
        r,_,_=S.annual(f,t,vintage='newest'); res[k]=r
    except Exception as e: res[k]={}; print(k,'ERR',e)
ends=sorted(set(e for r in res.values() for e in r if e>='2013'))
print('end',*res.keys(),sep='\t')
for e in ends:
    print(e,*[(round(res[k][e],2) if e in res[k] else '') for k in res],sep='\t')
