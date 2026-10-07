import sys,json; sys.path.insert(0,'tools')
import sources as S
out=[]
for t in ['RS','RYI','ZEUS','WS','WOR','STLD','NUE','CMC']:
    try:
        cik=S.cik_for(t)[0]; f=S.sec_facts(cik)
    except Exception as e:
        print(t,'fail',e); continue
    g=f['facts'].get('us-gaap',{})
    def pick(tags):
        for tg in tags:
            if tg in g:
                us=g[tg]['units'].get('USD',[])
                rows=[u for u in us if u.get('form')=='10-K' and u.get('fp')=='FY' and 'start' in u]
                d={}
                for u in rows:
                    import datetime as D
                    s=D.date.fromisoformat(u['start']);e=D.date.fromisoformat(u['end'])
                    if 340<(e-s).days<380: d[u['end']]=(u['val']/1e6,u['accn'],u['filed'])
                if d: return tg,d
        return None,{}
    for lab,tags in [('REV',['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet']),('OPINC',['OperatingIncomeLoss']),('GP',['GrossProfit']),('SBC',['ShareBasedCompensation']),('OCF',['NetCashProvidedByUsedInOperatingActivities']),('CAPEX',['PaymentsToAcquirePropertyPlantAndEquipment'])]:
        tg,d=pick(tags)
        for k in sorted(d)[-6:]:
            print(t,lab,tg,k,round(d[k][0],1),d[k][1],d[k][2])
