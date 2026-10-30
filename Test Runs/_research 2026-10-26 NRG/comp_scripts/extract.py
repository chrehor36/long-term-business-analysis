import json,sys
from datetime import date
p=sys.argv[1]; mode=sys.argv[2] if len(sys.argv)>2 else 'all'
d=json.load(open(p,encoding='utf-8'))
F={}
for tax,cs in d['facts'].items(): F.update(cs)
FLOW=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractWithCustomerIncludingAssessedTax','OperatingIncomeLoss',
'DepreciationDepletionAndAmortization','DepreciationAmortizationAndAccretionNet','DepreciationAndAmortization','Depreciation','CostOfGoodsAndServicesSoldDepreciationAndAmortization','AmortizationOfIntangibleAssets','AmortizationOfNuclearFuelLease','DepreciationNonproduction','DepreciationDepletionAndAmortizationExcludingNuclearFuel',
'NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations',
'PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','PaymentsForCapitalImprovements','PaymentsForProceedsFromNuclearFuel','PaymentsToAcquireNuclearFuel','PaymentsForNuclearFuel','ProceedsFromNuclearFuel',
'PaymentsToAcquireBusinessesNetOfCashAcquired','PaymentsToAcquireBusinessesGross','PaymentsToAcquireBusinessTwoNetOfCashAcquired',
'ShareBasedCompensation','AllocatedShareBasedCompensationExpense','PaymentsForRepurchaseOfCommonStock','GrossProfit']
INST=['Assets','Goodwill','IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet','IndefiniteLivedIntangibleAssetsExcludingGoodwill',
'LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities','LongTermDebt','LongTermDebtAndCapitalLeaseObligations','LongTermDebtAndCapitalLeaseObligationsCurrent','LongTermDebtNoncurrent','LongTermDebtCurrent','DebtCurrent','LongTermLineOfCredit','LineOfCredit','DebtInstrumentCarryingAmount',
'CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents',
'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','StockholdersEquity','MembersEquity']
def days(f):
  if 'start' not in f: return None
  a=date.fromisoformat(f['start']);b=date.fromisoformat(f['end']);return (b-a).days
def pick(c,inst):
  if c not in F: return {}
  out={}
  for u,fs in F[c]['units'].items():
    if u!='USD': continue
    for f in fs:
      if not f['form'].startswith('10-K'): continue
      if inst:
        if 'start' in f: continue
      else:
        dd=days(f)
        if dd is None or dd<340 or dd>380: continue
      y=f['end'][:4]; 
      if f['end'][5:7] in('01','02') : y=str(int(y)-1)
      key=(y,f['end'],f.get('start',''))
      # keep latest filed
      if key not in out or f['filed']>out[key]['filed']: out[key]=f
  return out
yrs=[str(y) for y in range(2014,2027)]
for c in FLOW+INST:
  o=pick(c, c in INST)
  if not o: continue
  row={}
  for (y,e,s),f in o.items():
    row.setdefault(y,[]).append((e,s,f['val'],f['accn'],f['filed']))
  print(c)
  for y in sorted(row):
    for e,s,v,a,fd in row[y]:
      print(f'   {y} {s}->{e} {v/1e6:12.1f} {a} {fd}')
