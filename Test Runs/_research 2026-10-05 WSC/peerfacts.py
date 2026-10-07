import json,sys
def annual(f,tags,instant=False):
    g=f['facts'].get('us-gaap',{})
    out={}
    for t in tags:
        if t not in g: continue
        for unit,vals in g[t]['units'].items():
            if unit!='USD': continue
            for v in vals:
                if v.get('form') not in ('10-K','10-K/A'): continue
                fr=v.get('frame','')
                if instant:
                    if fr.startswith('CY') and fr.endswith('Q4I'): y=int(fr[2:6]); out.setdefault(y,v['val']/1e6)
                else:
                    if fr.startswith('CY') and len(fr)==6: y=int(fr[2:]); out.setdefault(y,v['val']/1e6)
    return out
rows={'Rev':(['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet'],0),
'OpInc':(['OperatingIncomeLoss'],0),'PreTax':(['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],0),
'Int':(['InterestExpense','InterestExpenseNonoperating','InterestExpenseDebt'],0),
'OCF':(['NetCashProvidedByUsedInOperatingActivities'],0),'SBC':(['ShareBasedCompensation'],0),
'RentCapex':(['PaymentsToAcquireEquipmentOnLease','PaymentsToAcquireRentalEquipment','PaymentsForProceedsFromProductiveAssets'],0),
'RentProc':(['ProceedsFromSaleOfEquipmentOnLease','ProceedsFromSaleOfProductiveAssets','ProceedsFromSaleOfRentalEquipment'],0),
'PPE':(['PaymentsToAcquirePropertyPlantAndEquipment'],0),
'Assets':(['Assets'],1),'GW':(['Goodwill'],1),'Intang':(['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'],1),
'Equity':(['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],1),
'Debt':(['LongTermDebt','LongTermDebtNoncurrent','DebtInstrumentCarryingAmount','LineOfCredit'],1)}
f=json.load(open(sys.argv[1]))
data={k:annual(f,v[0],v[1]) for k,v in rows.items()}
ys=range(2012,2026)
print('year '+' '.join(f'{k:>8}' for k in rows))
for y in ys:
    print(y,' '.join(f"{data[k].get(y,float('nan')):8.0f}" for k in rows))
