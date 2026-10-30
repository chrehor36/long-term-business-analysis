import sys
sys.path.insert(0,'../../tools')
import sources as S
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueGoodsNet']
OI=['OperatingIncomeLoss']
GP=['GrossProfit']
OCF=['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations']
AP=['AccountsPayableCurrent']
INV=['InventoryNet']
AR=['AccountsReceivableNetCurrent']
for t in sys.argv[1:]:
    try:
        cik=S.cik_for(t)[0]; f=S.sec_facts(cik)
    except Exception as e:
        print(t,'FAIL',e); continue
    r,rt,_=S.annual(f,REV,vintage='newest'); o,_,_=S.annual(f,OI,vintage='newest'); g,_,_=S.annual(f,GP,vintage='newest'); c,_,_=S.annual(f,OCF,vintage='newest')
    print('==',t,cik,rt)
    for e in sorted(r)[-12:]:
        oi=o.get(e); gp=g.get(e)
        print('  ',e,'rev',round(r[e],0),'GM%',round(100*gp/r[e],2) if gp else None,'OI',round(oi,0) if oi is not None else None,'OM%',round(100*oi/r[e],2) if oi is not None else None,'OCF',round(c[e]) if c.get(e) is not None else None)
