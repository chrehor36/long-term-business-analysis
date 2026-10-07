import json,sys
cik=sys.argv[1] if len(sys.argv)>1 else 'cf_DMC.json'
d=json.load(open(cik))
g=d['facts'].get('us-gaap',{})
tags={'Rev':['Revenues','SalesRevenueNet','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueGoodsNet'],
'GP':['GrossProfit'],'OpInc':['OperatingIncomeLoss'],'NI':['NetIncomeLoss'],
'OCF':['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],
'Capex':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'],
'DA':['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortizationAndAccretionNet'],
'SBC':['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],
'dAPAcc':['IncreaseDecreaseInAccountsPayableAndAccruedLiabilities'],
'dRec':['IncreaseDecreaseInAccountsReceivable','IncreaseDecreaseInReceivables'],
'dInv':['IncreaseDecreaseInInventories'],
'Eq':['StockholdersEquity'],'Div':['PaymentsOfDividendsCommonStock','PaymentsOfDividends'],
'Buyback':['PaymentsForRepurchaseOfCommonStock'],'Acq':['PaymentsToAcquireBusinessesNetOfCashAcquired'],
'Impair':['AssetImpairmentCharges'],'Debt':['LongTermDebtNoncurrent','LongTermDebt','LongTermDebtAndCapitalLeaseObligations']}
out={}
for k,ts in tags.items():
  for t in ts:
    if t not in g: continue
    for u,arr in g[t]['units'].items():
      if u!='USD':continue
      for f in arr:
        if f.get('form') not in ('10-K','20-F','10-K405','10-KT'): continue
        if 'start' in f:
          from datetime import date
          s=date.fromisoformat(f['start']);e=date.fromisoformat(f['end'])
          if not 350<(e-s).days<380: continue
        y=f['end'][:4] if f['end'][5:7]!='01' else str(int(f['end'][:4])-1)
        key=(k,y)
        # prefer latest filed
        if key not in out or f['filed']>out[key][1]:
          if key in out and out[key][2]!=t and ts.index(out[key][2])<ts.index(t) and out[key][1]>=f['filed']: continue
          out[key]=(f['val']/1e6,f['filed'],t)
years=sorted({y for (_,y) in out})
print('year '+' '.join(f'{k:>8}' for k in tags))
for y in years:
  print(y,' '.join(f"{out[(k,y)][0]:8.1f}" if (k,y) in out else '       -' for k in tags))
