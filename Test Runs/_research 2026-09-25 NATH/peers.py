import sys,json;sys.path.insert(0,'tools')
import sources as S
for t in ['SFD','HRL','CAG','KHC','TSN','BRBR']:
    cik,name=S.cik_for(t)
    if not cik: print(t,'no cik');continue
    f=S.sec_facts(cik)
    rev,_,_=S.annual(f,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet'],vintage='newest')
    op,_,_=S.annual(f,['OperatingIncomeLoss'],vintage='newest')
    ys=sorted(set(rev)&set(op))[-6:]
    print(t,name,cik,' '.join(f"{y[:4]}:{op[y]/rev[y]*100:.1f}%({rev[y]:.0f})" for y in ys))
