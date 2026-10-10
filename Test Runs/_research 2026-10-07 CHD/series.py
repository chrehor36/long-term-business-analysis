from comp import facts, annual
f=facts('CHD')
T={'OCF':['NetCashProvidedByUsedInOperatingActivities'],'SBC':['ShareBasedCompensation'],
'CAPEX':['PaymentsToAcquirePropertyPlantAndEquipment'],'DA':['DepreciationDepletionAndAmortization','DepreciationAndAmortization'],
'ACQ':['PaymentsToAcquireBusinessesNetOfCashAcquired'],'DIVEST':['ProceedsFromDivestitureOfBusinesses','ProceedsFromSaleOfProductiveAssets'],
'BUYBACK':['PaymentsForRepurchaseOfCommonStock'],'DIV':['PaymentsOfDividendsCommonStock','PaymentsOfDividends'],
'INTEXP':['InterestExpense','InterestExpenseNonoperating'],'INTINC':['InvestmentIncomeInterest','InterestIncomeOther'],
'TAX':['IncomeTaxExpenseBenefit'],'PRETAX':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],
'NI':['NetIncomeLoss'],'OPTPROC':['ProceedsFromStockOptionsExercised'],'EARNOUT':['PaymentForContingentConsiderationLiabilityFinancingActivities']}
D={k:annual(f,v) for k,v in T.items()}
yrs=sorted(k for k in D['OCF'] if k>='2015-12')
print('year   '+' '.join(f'{k:>8}' for k in T))
for y in yrs:
    print(y,' '.join(f"{(D[k][y][0]/1e6 if y in D[k] else float('nan')):8.1f}" for k in T))
