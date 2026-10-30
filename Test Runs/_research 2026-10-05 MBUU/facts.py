import json,sys
def annual(t,tags,fp='FY'):
    d=json.load(open(f'peers/{t}_facts.json'))['facts']
    out={}
    for tag in tags:
        for ns in ('us-gaap',):
            if tag in d.get(ns,{}):
                for unit,vals in d[ns][tag]['units'].items():
                    for v in vals:
                        if v.get('form','').startswith('10-K') and v.get('fp')=='FY':
                            # duration ~1y or instant
                            if 'start' in v:
                                from datetime import date
                                s=date.fromisoformat(v['start']);e=date.fromisoformat(v['end'])
                                if not 350<(e-s).days<380: continue
                            key=v['end']
                            # keep first-filed? keep latest filed (restated)
                            if key not in out or v['filed']>out[key][1]:
                                out[key]=(v['val'],v['filed'],tag)
        if out: pass
    return out
t=sys.argv[1]
rows={'Rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet'],
'OpInc':['OperatingIncomeLoss'],'NI':['NetIncomeLoss'],'OCF':['NetCashProvidedByUsedInOperatingActivities'],
'Capex':['PaymentsToAcquirePropertyPlantAndEquipment'],'Dep':['Depreciation','DepreciationDepletionAndAmortization','DepreciationAndAmortization'],
'SBC':['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],'Equity':['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],
'Assets':['Assets'],'GW':['Goodwill'],'Int':['IntangibleAssetsNetExcludingGoodwill'],'Cash':['CashAndCashEquivalentsAtCarryingValue'],
'Inv':['InventoryNet'],'Buyback':['PaymentsForRepurchaseOfCommonStock'],'GP':['GrossProfit'],'IntExp':['InterestExpense','InterestExpenseNonoperating','InterestExpenseDebt'],
'Tax':['IncomeTaxExpenseBenefit'],'PreTax':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments']}
want=sys.argv[2].split(',') if len(sys.argv)>2 else list(rows)
data={k:annual(t,rows[k]) for k in want}
ends=sorted(set(e for k in data for e in data[k]))
print(t, 'USD millions')
print('end'.ljust(11)+''.join(k.rjust(9) for k in want))
for e in ends:
    print(e.ljust(11)+''.join((f"{data[k][e][0]/1e6:9.1f}" if e in data[k] else ' '*9) for k in want))
