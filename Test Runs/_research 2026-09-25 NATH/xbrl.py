import sys;sys.path.insert(0,'tools')
import sources as S
f=S.sec_facts('0000069733')
T={'OCF':['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],
'CAPEX':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'],
'SBC':['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],
'DA':['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortizationAndAccretionNet'],
'NI':['NetIncomeLoss'],'REV':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet'],
'DIV':['PaymentsOfDividendsCommonStock','PaymentsOfDividends'],'BUY':['PaymentsForRepurchaseOfCommonStock'],
'OPINC':['OperatingIncomeLoss'],'TAXPAID':['IncomeTaxesPaidNet','IncomeTaxesPaid'],'PRETAX':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments']}
out={}
for k,tags in T.items():
    d,used,u=S.annual(f,tags,vintage='newest')
    out[k]=d; print(k,used)
ys=sorted(set().union(*[set(v) for v in out.values()]))
print('FY_end',*T.keys(),sep='\t')
for y in ys:
    print(y,*[('%.3f'%out[k][y]) if y in out[k] else '-' for k in T],sep='\t')
