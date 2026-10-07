import json, datetime
j=json.load(open('companyfacts.json'))['facts']
def ser(tags, inst=False, ns='us-gaap', forms=('10-K','10-K/A')):
    out={}
    if isinstance(tags,str): tags=[tags]
    for tag in tags:
      if tag not in j.get(ns,{}): continue
      for u,fs in j[ns][tag]['units'].items():
        if u not in ('USD','shares','USD/shares'): continue
        for f in fs:
            if f.get('form') not in forms: continue
            e=f['end']
            if not inst:
                if 'start' not in f: continue
                d=(datetime.date.fromisoformat(e)-datetime.date.fromisoformat(f['start'])).days
                if d<350 or d>380: continue
            if e[5:7] not in ('10',): continue
            y=int(e[:4])
            if y not in out or f['filed']>out[y][1]: out[y]=(f['val'],f['filed'])
    return {y:v[0] for y,v in out.items()}
T=[('Rev',['RevenueFromContractWithCustomerIncludingAssessedTax','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','Revenues']),('GP','GrossProfit'),('OpInc','OperatingIncomeLoss'),('NI','NetIncomeLoss'),('NIminor','NetIncomeLossAttributableToNoncontrollingInterest'),
('OCF',['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations']),('Capex','PaymentsToAcquirePropertyPlantAndEquipment'),('IntangBuy','PaymentsToAcquireIntangibleAssets'),('IntangSale','ProceedsFromSaleOfIntangibleAssets'),('DA','DepreciationAndAmortization'),('DDA','DepreciationDepletionAndAmortization'),('Dep','Depreciation'),('Amort','AmortizationOfIntangibleAssets'),('SBC','ShareBasedCompensation'),('SBCalloc','AllocatedShareBasedCompensationExpense'),
('dInv','IncreaseDecreaseInInventories'),('dAR','IncreaseDecreaseInAccountsReceivable'),('dAPAL','IncreaseDecreaseInAccountsPayableAndAccruedLiabilities'),('dOth','IncreaseDecreaseInOtherOperatingAssets'),('dTaxP',['IncreaseDecreaseInAccruedIncomeTaxesPayable','IncreaseDecreaseInAccruedTaxesPayable']),('DefTax','DeferredIncomeTaxExpenseBenefit'),
('Divs',['PaymentsOfDividendsCommonStock','PaymentsOfDividends']),('DivMin','PaymentsOfDividendsMinorityInterest'),('ToMin','PaymentsToMinorityShareholders'),('Buyback',['PaymentsForRepurchaseOfCommonStock','PaymentsForRepurchaseOfEquity']),('OptProc','ProceedsFromStockOptionsExercised'),('TaxPaid',['IncomeTaxesPaidNet','IncomeTaxesPaid']),('TaxExp','IncomeTaxExpenseBenefit'),('PreTax','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'),('Adv','AdvertisingExpense'),('Acq','PaymentsToAcquireBusinessesNetOfCashAcquired'),('Mkt','SellingAndMarketingExpense'),('COGS',['CostOfGoodsAndServicesSold','CostOfRevenue','CostOfGoodsSold']),('SharesB','WeightedAverageNumberOfSharesOutstandingBasic'),('SharesD','WeightedAverageNumberOfDilutedSharesOutstanding')]
B=[('Cash',['CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents']),('STI','ShortTermInvestments'),('AR','AccountsReceivableNetCurrent'),('Inv','InventoryNet'),('AP','AccountsPayableCurrent'),('Intang','IntangibleAssetsNetExcludingGoodwill'),('GW','Goodwill'),('PPE','PropertyPlantAndEquipmentNet'),('Assets','Assets'),('Equity','StockholdersEquity'),('EqTot','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'),('Minority','MinorityInterest'),('LTD','LongTermDebtNoncurrent'),('LTDc','LongTermDebtCurrent'),('STB',['LoansPayableToBankCurrent','ShortTermBankLoansAndNotesPayable','LoansPayableToBank']),('SharesOut','CommonStockSharesOutstanding')]
rows={}
for n,t in T: rows[n]=ser(t)
for n,t in B: rows[n]=ser(t,inst=True)
ys=sorted({y for v in rows.values() for y in v if y>=2005})
print('year     '+' '.join('%8d'%y for y in ys))
for n in rows:
    sc=1e6
    print('%-9s'%n+' '.join(('%8.1f'%(rows[n][y]/sc)) if y in rows[n] else '       -' for y in ys))
json.dump({n:{str(y):v for y,v in d.items()} for n,d in rows.items()},open('xb_rows.json','w'))
