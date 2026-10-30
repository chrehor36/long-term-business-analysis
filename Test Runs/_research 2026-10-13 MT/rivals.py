import json
from datetime import date
def ann(f,ns,tags,forms=('10-K','20-F')):
    out={}
    for tag in tags:
        if tag not in f['facts'].get(ns,{}): continue
        for u,arr in f['facts'][ns][tag]['units'].items():
            for x in arr:
                if x.get('form') not in forms: continue
                if 'start' in x:
                    d=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days
                    if d<340 or d>380: continue
                y=int(x['end'][:4])
                if y not in out or x['filed']>out[y][1]: out[y]=(x['val'],x['filed'],x.get('accn'))
        if out: pass
    return out
def merged(f,ns,tags):
    out={}
    for t in tags:
        a=ann(f,ns,[t])
        for y,v in a.items():
            if y not in out: out[y]=v
    return out
spec={
 'NUE':('us-gaap',{'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet'],
   'oi':['OperatingIncomeLoss','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'],
   'eq':['StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','StockholdersEquity'],
   'debt':['LongTermDebtAndCapitalLeaseObligations','LongTermDebtNoncurrent','LongTermDebt'],'cash':['CashAndCashEquivalentsAtCarryingValue']}),
 'CLF':('us-gaap',{'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet'],
   'oi':['OperatingIncomeLoss'],
   'eq':['StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','StockholdersEquity'],
   'debt':['LongTermDebt','LongTermDebtNoncurrent'],'cash':['CashAndCashEquivalentsAtCarryingValue']}),
 'PKX':('ifrs-full',{'rev':['Revenue','RevenueFromContractsWithCustomers'],'oi':['ProfitLossFromOperatingActivities'],
   'eq':['Equity'],'debt':['Borrowings','NoncurrentPortionOfNoncurrentBorrowings'],'cash':['CashAndCashEquivalents']}),
}
for t,(ns,m) in spec.items():
    f=json.load(open(f'cache/{t}_facts.json'))
    d={k:merged(f,ns,v) for k,v in m.items()}
    print('==',t)
    for y in range(2015,2026):
        r=d['rev'].get(y); o=d['oi'].get(y)
        if r and o:
            print(y, 'rev',round(r[0]/1e6),'oi',round(o[0]/1e6),'margin %.1f%%'%(100*o[0]/r[0]),'eq',round(d['eq'][y][0]/1e6) if y in d['eq'] else '-', o[2])
        else: print(y,'missing', bool(r), bool(o))

print('== returns on equity plus net debt (pre-tax)')
for t,(ns,m) in spec.items():
    f=json.load(open(f'cache/{t}_facts.json'))
    d={k:merged(f,ns,v) for k,v in m.items()}
    rs=[]
    for y in range(2016,2026):
        try:
            cap=d['eq'][y][0]+d['debt'][y][0]-d['cash'][y][0]; r=d['oi'][y][0]/cap; rs.append(r)
            print(t,y,'%.1f%%'%(100*r), end='; ')
        except KeyError: pass
    print('\n',t,'avg %.1f%% over %d yrs'%(100*sum(rs)/len(rs),len(rs)))
