import json, os, sys
from datetime import date
from fetch import get
CIKS={'V':'0001403161','AXP':'0000004962','DFS':'0001393612','PYPL':'0001633917','FI':'0000798354','GPN':'0001123360','WU':'0001365135'}
for k,c in CIKS.items():
    p=f'cache/facts_{k}.json'
    if not os.path.exists(p):
        try: open(p,'wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json'))
        except SystemExit as e: print('FAIL',k,e); continue
    f=json.load(open(p))['facts'].get('us-gaap',{})
    print('########',k)
    for t in ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','RevenuesNetOfInterestExpense','OperatingIncomeLoss','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','NetCashProvidedByUsedInOperatingActivities','ShareBasedCompensation','PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToDevelopSoftware','DepreciationDepletionAndAmortization','DepreciationAndAmortization','StockholdersEquity','Goodwill','IntangibleAssetsNetExcludingGoodwill','LongTermDebt','LongTermDebtNoncurrent','CashAndCashEquivalentsAtCarryingValue','PaymentsForRepurchaseOfCommonStock','LitigationSettlementExpense','LossContingencyLossInPeriod']:
        if t not in f: continue
        rows={}
        for u,arr in f[t]['units'].items():
            for x in arr:
                if x.get('form') not in ('10-K','10-K/A') or x.get('fp')!='FY': continue
                if 'start' in x:
                    d=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days
                    if 350<=d<=380: rows[x['end']]=x['val']
                else: rows[x['end']]=x['val']
        if rows: print(t,' '.join(f"{k2[:7]}:{v/1e6:.0f}" for k2,v in sorted(rows.items()) if k2>='2012'))
