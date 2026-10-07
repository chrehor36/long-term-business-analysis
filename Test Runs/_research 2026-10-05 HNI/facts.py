import json,sys
from collections import defaultdict
t=sys.argv[1]
d=json.load(open(f'peers/{t}_facts.json'))['facts']
g=d.get('us-gaap',{})
tags=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','OperatingIncomeLoss','NetIncomeLoss','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','DepreciationDepletionAndAmortization','DepreciationAmortizationAndAccretionNet','ShareBasedCompensation','AllocatedShareBasedCompensationExpense','StockholdersEquity','Goodwill','LongTermDebtNoncurrent','LongTermDebt','PaymentsForRepurchaseOfCommonStock','PaymentsOfDividends','PaymentsOfDividendsCommonStock','RestructuringCharges','IncomeTaxesPaidNet','InterestPaidNet','Assets','CashAndCashEquivalentsAtCarryingValue','InventoryNet','AccountsReceivableNetCurrent']
out=defaultdict(dict)
for tag in tags:
    if tag not in g: continue
    for unit,vals in g[tag]['units'].items():
        for v in vals:
            if v.get('form') not in ('10-K','10-K405','10-KT'): continue
            fp=v.get('fp'); 
            if 'start' in v:
                from datetime import date
                s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
                if not (340<(e-s).days<380): continue
            key=v['end']
            # keep first filed
            prev=out[key].get(tag)
            if prev is None or v['filed']<prev[1]:
                out[key][tag]=(v['val'],v['filed'])
ends=sorted(k for k in out if k>='2012-01-01')
short={'Revenues':'Rev','RevenueFromContractWithCustomerExcludingAssessedTax':'Rev2','SalesRevenueNet':'Rev3','OperatingIncomeLoss':'OpInc','NetIncomeLoss':'NI','NetCashProvidedByUsedInOperatingActivities':'OCF','PaymentsToAcquirePropertyPlantAndEquipment':'Capex','PaymentsToAcquireProductiveAssets':'Capex2','DepreciationDepletionAndAmortization':'DA','DepreciationAmortizationAndAccretionNet':'DA2','ShareBasedCompensation':'SBC','AllocatedShareBasedCompensationExpense':'SBC2','StockholdersEquity':'Eq','Goodwill':'GW','LongTermDebtNoncurrent':'LTD','LongTermDebt':'LTD2','PaymentsForRepurchaseOfCommonStock':'Buyb','PaymentsOfDividends':'Div','PaymentsOfDividendsCommonStock':'Div2','RestructuringCharges':'Restr','IncomeTaxesPaidNet':'TaxPd','InterestPaidNet':'IntPd','Assets':'Assets','CashAndCashEquivalentsAtCarryingValue':'Cash','InventoryNet':'Inv','AccountsReceivableNetCurrent':'AR'}
for e in ends:
    row=out[e]
    print(e,' '.join(f"{short[k]}={row[k][0]/1e6:.1f}" for k in tags if k in row))
