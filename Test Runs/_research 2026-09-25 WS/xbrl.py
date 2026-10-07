import sys; sys.path.insert(0,'tools')
import sources as S
cik=S.cik_for('WS')[0]; f=S.sec_facts(cik)
tags={'OCF':['NetCashProvidedByUsedInOperatingActivities'],
 'SBC':['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],
 'CAPEX':['PaymentsToAcquirePropertyPlantAndEquipment'],
 'DA':['DepreciationDepletionAndAmortization','DepreciationAndAmortization','Depreciation'],
 'REV':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'],
 'OPINC':['OperatingIncomeLoss'],'NI':['NetIncomeLoss','ProfitLoss'],
 'AP':['IncreaseDecreaseInAccountsPayable'],'INV':['IncreaseDecreaseInInventories'],'AR':['IncreaseDecreaseInAccountsReceivable'],
 'ACQ':['PaymentsToAcquireBusinessesNetOfCashAcquired'],'DIVJV':['ProceedsFromEquityMethodInvestmentDividendsOrDistributions','EquityMethodInvestmentDividendsOrDistributions']}
for k,t in tags.items():
    for vin in ('newest','earliest'):
        try: r=S.annual(f,t,vintage=vin)
        except Exception as e: r=str(e)
        print(k,vin,r)
