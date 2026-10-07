import sys
sys.path.insert(0,'../../tools')
import sources as S
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueServicesNet']
OI=['OperatingIncomeLoss']
OCF=['NetCashProvidedByUsedInOperatingActivities']
for t in ['ICFI','BAH','CACI','SAIC','LDOS','TTEK','ACM','ACN','GD','MMS','PSN','KBR']:
    try:
        cik=S.cik_for(t)[0]; f=S.sec_facts(cik)
    except Exception as e:
        print(t,'FAIL',e); continue
    r,_,_=S.annual(f,REV,vintage='newest'); o,_,_=S.annual(f,OI,vintage='newest')
    print('==',t,cik)
    for e in sorted(r)[-12:]:
        oi=o.get(e)
        print('  ',e, 'rev',round(r[e],1), 'OI', round(oi,1) if oi is not None else None, 'OM%', round(100*oi/r[e],1) if oi is not None else None)
