import json, sys
from collections import defaultdict
def annual(f, tags, unit='USD'):
    g=f['facts'].get('us-gaap',{})
    out={}
    for t in tags:
        if t not in g: continue
        for x in g[t]['units'].get(unit,[]):
            if x.get('form')!='10-K' or not x.get('fp')=='FY': continue
            st=x.get('start'); en=x['end']
            if st:
                from datetime import date
                d=(date.fromisoformat(en)-date.fromisoformat(st)).days
                if d<350 or d>380: continue
            y=int(en[:4])
            # keep latest-filed value for that year end
            k=(y)
            if k not in out or x['filed']>out[k][1]: out[k]=(x['val'],x['filed'],x['accn'])
        if out: pass
    return out
def merged(f,tags):
    res={}
    for t in tags:
        a=annual(f,[t])
        for y,v in a.items():
            if y not in res: res[y]=v
    return res
cfg={'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet'],
 'opinc':['OperatingIncomeLoss'],
 'ocf':['NetCashProvidedByUsedInOperatingActivities'],
 'rentcap':['PaymentsToAcquireEquipmentOnLease','PaymentsForPurchaseOfRentalEquipment','PaymentsToAcquireRentalEquipment'],
 'nonrentcap':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'],
 'proceeds':['ProceedsFromSaleOfPropertyPlantAndEquipment','ProceedsFromSaleOfProductiveAssets','ProceedsFromSaleOfEquipmentOnLease'],
 'acq':['PaymentsToAcquireBusinessesNetOfCashAcquired'],
 'equity':['StockholdersEquity'],
 'assets':['Assets'],
 'debt':['LongTermDebt','LongTermDebtNoncurrent','DebtAndCapitalLeaseObligations','LongTermDebtAndCapitalLeaseObligations'],
 'cash':['CashAndCashEquivalentsAtCarryingValue'],
 'goodwill':['Goodwill'],
 'sbc':['ShareBasedCompensation'],
 'netinc':['NetIncomeLoss'],
 'da':['DepreciationDepletionAndAmortization','DepreciationAndAmortization'],
}
if __name__=='__main__':
  f=json.load(open(sys.argv[1]))
  print(f['entityName'])
  rows=defaultdict(dict)
  for k,tags in cfg.items():
    for y,v in merged(f,tags).items(): rows[y][k]=v[0]
  for y in sorted(rows):
    r=rows[y]
    print(y, ' '.join(f"{k}={r[k]/1e6:.0f}" for k in cfg if k in r))
