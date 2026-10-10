import json,sys
def load(t):
    return json.load(open(f'{t}_facts.json'))['facts']
def ann(d,tags,unit='USD'):
    out={}
    for tag in tags:
        try: u=d['us-gaap'][tag]['units'][unit]
        except KeyError: continue
        for x in u:
            if x.get('fp')=='FY' and x.get('form') in ('10-K','10-K/A') and x.get('start'):
                s,e=x['start'],x['end']
                m=(int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7])
                if m<11: continue
                y=int(e[:4]) if int(e[5:7])>6 else int(e[:4])-1  # fiscal year label by end; FY ending Jun -> prior? keep end year
                y=int(e[:4])
                if y not in out or x['filed']<out[y][1]: out[y]=(x['val'],x['filed'],tag)
    return out
t=sys.argv[1]; d=load(t)
R=ann(d,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet'])
G=ann(d,['GrossProfit'])
O=ann(d,['OperatingIncomeLoss'])
N=ann(d,['NetIncomeLoss','ProfitLoss'])
RD=ann(d,['ResearchAndDevelopmentExpense','ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost'])
print(t,'FYend  revenue  gross%  R&D%  opmargin%  netinc')
for y in sorted(R):
    r=R[y][0]
    f=lambda D: (f"{100*D[y][0]/r:6.1f}" if y in D else '   n/a')
    print(y, f"{r/1e6:9.0f}", f(G), f(RD), f(O), f"{N[y][0]/1e6:8.0f}" if y in N else 'n/a')
