import json, datetime
j=json.load(open('companyfacts.json'))['facts']
def ser(tag, inst=False, ns='us-gaap', forms=('10-K',)):
    out={}
    if tag not in j.get(ns,{}): return out
    for u,fs in j[ns][tag]['units'].items():
        for f in fs:
            if f.get('form') not in forms: continue
            e=f['end']
            if not inst:
                if 'start' not in f: continue
                d=(datetime.date.fromisoformat(e)-datetime.date.fromisoformat(f['start'])).days
                if d<350 or d>380: continue
            if not e.endswith('12-31'): continue
            y=int(e[:4])
            if y not in out or f['filed']>out[y][1]: out[y]=(f['val'],f['filed'])
    return {y:v[0] for y,v in out.items()}
T=[('Rev','RevenueFromContractWithCustomerExcludingAssessedTax'),('RevSvc','SalesRevenueServicesNet'),('RevNet','SalesRevenueNet'),('Reimb','ReimbursementRevenue'),
('OpInc','OperatingIncomeLoss'),('NI','NetIncomeLoss'),('OCF','NetCashProvidedByUsedInOperatingActivities'),('OCFc','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'),
('Capex','PaymentsToAcquirePropertyPlantAndEquipment'),('Dep','Depreciation'),('Amort','AmortizationOfIntangibleAssets'),('SBC','ShareBasedCompensation'),
('dCWCL','IncreaseDecreaseInContractWithCustomerLiability'),('dDefRev','IncreaseDecreaseInDeferredRevenue'),('dRec','IncreaseDecreaseInReceivables'),('dAP','IncreaseDecreaseInAccountsPayable'),('dAccr','IncreaseDecreaseInAccruedLiabilities'),('dPrep','IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets'),('dOther','IncreaseDecreaseInOtherOperatingCapitalNet'),
('Buyback','PaymentsForRepurchaseOfCommonStock'),('TaxPaid','IncomeTaxesPaidNet'),('TaxExp','IncomeTaxExpenseBenefit'),('PreTax','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'),('IntangBuy','PaymentsToAcquireIntangibleAssets'),('OtherInv','PaymentsForProceedsFromOtherInvestingActivities'),('SharesB','WeightedAverageNumberOfSharesOutstandingBasic'),('SharesD','WeightedAverageNumberOfDilutedSharesOutstanding'),('SGA','SellingGeneralAndAdministrativeExpense'),('DirCost','DirectOperatingCosts'),('CostSvc','CostOfServicesExcludingDepreciationDepletionAndAmortization'),('GWimp','GoodwillImpairmentLoss')]
B=[('Cash','CashAndCashEquivalentsAtCarryingValue'),('AR','AccountsReceivableGrossCurrent'),('Recv','ReceivablesNetCurrent'),('Unbilled','UnbilledReceivablesCurrent'),('CWCL','ContractWithCustomerLiabilityCurrent'),('DefRevC','DeferredRevenueCurrent'),('Equity','StockholdersEquity'),('GW','Goodwill'),('Intang','IntangibleAssetsNetExcludingGoodwill'),('PPE','PropertyPlantAndEquipmentNet'),('Liab','Liabilities'),('LiabC','LiabilitiesCurrent'),('Debt','LongTermDebtNoncurrent'),('DebtC','LongTermDebtCurrent'),('LOC','LineOfCredit'),('STB','ShortTermBorrowings'),('RPO','RevenueRemainingPerformanceObligation'),('Lease','OperatingLeaseLiability'),('ROU','OperatingLeaseRightOfUseAsset')]
rows={}
for n,t in T: rows[n]=ser(t)
for n,t in B: rows[n]=ser(t,inst=True)
ys=sorted({y for v in rows.values() for y in v})
print('year '+' '.join('%9d'%y for y in ys))
for n in rows:
    print('%-9s'%n+' '.join('%9.1f'%(rows[n][y]/1e6) if y in rows[n] and n not in('SharesB','SharesD') else ('%9.3f'%(rows[n][y]/1e6) if y in rows[n] else '        -') for y in ys))
json.dump({n:{str(y):v for y,v in d.items()} for n,d in rows.items()},open('xb_rows.json','w'))
