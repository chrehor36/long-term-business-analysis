import sys,io,json
sys.path.insert(0,'C:/Users/chreh/OneDrive/Documents/BRK/tools')
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
import sources as S
TAGS={'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'],
      'opinc':['OperatingIncomeLoss'],'ni':['NetIncomeLoss','ProfitLoss'],
      'ocf':['NetCashProvidedByUsedInOperatingActivities'],
      'capex':['PaymentsToAcquirePropertyPlantAndEquipment'],
      'da':['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortizationAndAccretionNet'],
      'sbc':['ShareBasedCompensation'],'assets':['Assets'],'eq':['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest']}
for t in sys.argv[1:]:
    c=S.cik_for(t); cik=c[0] if isinstance(c,tuple) else c; f=S.sec_facts(cik)
    print('==',t,cik,f.get('entityName'))
    for k,tags in TAGS.items():
        try:
            a,used,u=S.annual(f,tags,vintage='newest')
        except Exception as e:
            a=None;used=str(e)
        print(k, {y[:4]:round(v,1) for y,v in sorted(a.items())} if a else None, used)
