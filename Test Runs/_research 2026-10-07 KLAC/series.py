import json, sys, datetime as dt
def load(t): return json.load(open(f'cache/cf_{t}.json'))
def annual(d, tags, unit='USD', instant=False):
    out={}
    for tag in tags:
        f=d['facts'].get('us-gaap',{}).get(tag)
        if not f or unit not in f['units']: continue
        for v in f['units'][unit]:
            if v.get('form') not in ('10-K','20-F','10-K/A','20-F/A'): continue
            e=v['end']
            if instant:
                if 'start' in v: continue
            else:
                if 'start' not in v: continue
                days=(dt.date.fromisoformat(e)-dt.date.fromisoformat(v['start'])).days
                if not 350<=days<=380: continue
            # keep latest filed
            k=e
            if k not in out or v['filed']>out[k][1] or (v['filed']==out[k][1]):
                if k in out and out[k][2]!=tag and v['filed']==out[k][1]: continue
                out[k]=(v['val'],v['filed'],tag)
    return out
TAGS={
 'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet'],
 'gp':['GrossProfit'],
 'oi':['OperatingIncomeLoss'],
 'ni':['NetIncomeLoss'],
 'rd':['ResearchAndDevelopmentExpense','ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost'],
 'ocf':['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],
 'capex':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'],
 'sbc':['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],
 'da':['DepreciationDepletionAndAmortization','DepreciationAmortizationAndAccretionNet','DepreciationAndAmortization'],
 'acq':['PaymentsToAcquireBusinessesNetOfCashAcquired'],
 'buyb':['PaymentsForRepurchaseOfCommonStock'],
 'div':['PaymentsOfDividendsCommonStock','PaymentsOfDividends'],
 'tax':['IncomeTaxExpenseBenefit'],
 'pti':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],
 'intexp':['InterestExpense','InterestExpenseNonoperating','InterestExpenseDebt'],
}
ITAGS={'equity':['StockholdersEquity'],'assets':['Assets'],'gw':['Goodwill'],'intang':['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'],
 'cash':['CashAndCashEquivalentsAtCarryingValue'],'mktsec_c':['MarketableSecuritiesCurrent','AvailableForSaleSecuritiesDebtSecuritiesCurrent','ShortTermInvestments'],
 'mktsec_nc':['MarketableSecuritiesNoncurrent','AvailableForSaleSecuritiesDebtSecuritiesNoncurrent','LongTermInvestments'],
 'debt':['LongTermDebt','LongTermDebtNoncurrent'],'debtc':['LongTermDebtCurrent','DebtCurrent'],'liab':['Liabilities'],'inv':['InventoryNet'],'ar':['AccountsReceivableNetCurrent']}
if __name__=='__main__':
    t=sys.argv[1]; d=load(t); U=sys.argv[2] if len(sys.argv)>2 else 'USD'
    S={k:annual(d,v,U) for k,v in TAGS.items()}
    I={k:annual(d,v,U,instant=True) for k,v in ITAGS.items()}
    ends=sorted(set(S['rev'])|set(S['oi']))
    keys=list(TAGS)+list(ITAGS)
    print(t,'(USD millions)'); print('end'.ljust(11)+''.join(k.rjust(9) for k in keys))
    for e in ends:
        row=e.ljust(11)
        for k in keys:
            src=S[k] if k in S else I[k]
            v=src.get(e)
            row+=(f'{v[0]/1e6:9.0f}' if v else '        -')
        print(row)
