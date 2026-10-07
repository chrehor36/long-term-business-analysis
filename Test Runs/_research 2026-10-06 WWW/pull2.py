import sys
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources as S
cik=sys.argv[1]; f=S.sec_facts(cik)
for k,t in {"rev":["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","RevenueFromContractWithCustomerIncludingAssessedTax","SalesRevenueNet"],"gp":["GrossProfit"],"opinc":["OperatingIncomeLoss"],"ocf":["NetCashProvidedByUsedInOperatingActivities"],"capex":["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"],"sbc":["ShareBasedCompensation"]}.items():
    d,u,_=S.annual(f,t,vintage="newest"); print(k, {e[:7]:round(v,1) for e,v in sorted(d.items())})
