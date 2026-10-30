import sys, json
sys.path.insert(0,'tools')
import sources as S
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','RevenueFromContractWithCustomerIncludingAssessedTax']
GP=['GrossProfit']
COS=['CostOfRevenue','CostOfGoodsAndServicesSold','CostOfGoodsSold']
OI=['OperatingIncomeLoss']
out={}
for t in ['CRUS','ADI','QCOM','SWKS','STM','SYNA','TXN','QRVO']:
    try:
        cik=S.cik_for(t)[0]; f=S.sec_facts(cik)
    except Exception as e:
        print(t,'FAIL',e); continue
    r,_,_=S.annual(f,REV,vintage='newest'); g,_,_=S.annual(f,GP,vintage='newest'); c,_,_=S.annual(f,COS,vintage='newest'); o,_,_=S.annual(f,OI,vintage='newest')
    print('==',t,cik)
    for e in sorted(r)[-11:]:
        gp=g.get(e) if g.get(e) is not None else (r[e]-c[e] if c.get(e) is not None else None)
        oi=o.get(e)
        print(e, round(r[e],1), 'GM', round(100*gp/r[e],1) if gp else None, 'OM', round(100*oi/r[e],1) if oi is not None else None)
