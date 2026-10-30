import sys
sys.path.insert(0,'../../tools')
import sources as S
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueServicesNet']
OI=['OperatingIncomeLoss']
GP=['GrossProfit']
for t in ['MHH','CTSH','KFRC','ASGN','RHI','KELYA','BGSF','JOB','RGP','III','CTG','PRFT','EPAM','CCRN']:
    try:
        cik=S.cik_for(t)[0]; f=S.sec_facts(cik)
    except Exception as e:
        print(t,'FAIL',e); continue
    r,_,_=S.annual(f,REV,vintage='newest'); o,_,_=S.annual(f,OI,vintage='newest'); g,_,_=S.annual(f,GP,vintage='newest')
    print('==',t,cik)
    for e in sorted(r)[-8:]:
        oi=o.get(e); gp=g.get(e)
        print('  ',e,'rev',round(r[e],1),'GM%',round(100*gp/r[e],1) if gp else None,'OI',round(oi,1) if oi is not None else None,'OM%',round(100*oi/r[e],1) if oi is not None else None)
