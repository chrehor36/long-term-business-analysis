import json,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
f=json.load(open('facts.json'))['facts']['us-gaap']
tags=sys.argv[1:] or ['Revenues','SalesRevenueNet','RevenueFromContractWithCustomerExcludingAssessedTax','CostOfGoodsAndServicesSold','CostOfGoodsSold','CostOfRevenue','GrossProfit','OperatingIncomeLoss','NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','ShareBasedCompensation','AllocatedShareBasedCompensationExpense','DepreciationDepletionAndAmortization','DepreciationAndAmortization','Depreciation','AmortizationOfIntangibleAssets','PaymentsToAcquireBusinessesNetOfCashAcquired','IncreaseDecreaseInAccountsPayableAndAccruedLiabilities','IncreaseDecreaseInOtherOperatingCapitalNet','ResearchAndDevelopmentExpense','PaymentsForRepurchaseOfCommonStock','PaymentsOfDividends','LongTermDebt','IncomeTaxesPaidNet','IncomeTaxesPaid']
for t in tags:
    if t not in f: continue
    u=f[t]['units']
    for unit,vals in u.items():
        best={}
        for v in vals:
            if v.get('form') not in ('10-K','10-K/A'): continue
            fp=v.get('fp'); 
            if 'start' in v:
                from datetime import date
                s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
                if (e-s).days<350: continue
            fy=v['end'][:4]
            key=fy
            # newest filed
            if key not in best or v['filed']>best[key]['filed']: best[key]=v
        if best:
            print(t,unit,' '.join(f"{k}:{best[k]['val']/1e6:.1f}" for k in sorted(best)))
