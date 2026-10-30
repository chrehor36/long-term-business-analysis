import json,re
def tab(f):
    rows={}
    cur=None
    for line in open(f):
        p=line.split()
        if len(p)>=2 and p[1] in('AMEREN','Evergy,','WEC','Xcel'): cur=p[0]; rows[cur]={}
        elif p and p[0].isdigit() and len(p)==13 and cur:
            rows[cur][int(p[0])]=[float(v) for v in p[1:]]
    return rows
R=tab('peers_facts.txt')
cols='NI OCF CAPEX DA REV EQ DIV ISS INT TAX SBC PPE'.split()
ix={c:i for i,c in enumerate(cols)}
# WEC fills (flagged): capex = PaymentsToAcquireOtherPropertyPlantAndEquipment; equity incl NCI
wcap={2018:2115.7,2019:2260.8,2020:2238.8,2021:2252.8,2022:2314.9,2023:2492.9,2024:2781.1,2025:4398.1}
weq={2019:10254.6,2020:10662.5,2021:11113.3,2022:11616.6,2023:12071.5,2024:12801.9,2025:14052.8}
for y,v in wcap.items(): R['WEC'][y][ix['CAPEX']]=v
for y,v in weq.items(): R['WEC'][y][ix['EQ']]=v
print('ticker  span  ROE(NI/avg eq) by year ... | mean ROE | sum(OCF-SBC-capex) | capex/DA | NI/netPPE mean | equity issued')
for t,d in R.items():
    roes=[];
    for y in range(2017,2026):
        if y in d and y-1 in d:
            e0,e1=d[y-1][ix['EQ']],d[y][ix['EQ']]
            if e0==e0 and e1==e1: roes.append((y,d[y][ix['NI']]/((e0+e1)/2)))
    yrs=[y for y in range(2016,2026) if y in d]
    fcf=sum(d[y][ix['OCF']]-(d[y][ix['SBC']] if d[y][ix['SBC']]==d[y][ix['SBC']] else 0)-d[y][ix['CAPEX']] for y in yrs if d[y][ix['CAPEX']]==d[y][ix['CAPEX']])
    cd=sum(d[y][ix['CAPEX']] for y in yrs if d[y][ix['CAPEX']]==d[y][ix['CAPEX']])/sum(d[y][ix['DA']] for y in yrs if d[y][ix['CAPEX']]==d[y][ix['CAPEX']])
    rop=[d[y][ix['NI']]/d[y][ix['PPE']] for y in yrs if d[y][ix['PPE']]==d[y][ix['PPE']]]
    iss=sum(d[y][ix['ISS']] for y in yrs if d[y][ix['ISS']]==d[y][ix['ISS']])
    div=sum(d[y][ix['DIV']] for y in yrs)
    print(t, f"{yrs[0]}-{yrs[-1]}", ' '.join(f"{y%100}:{r*100:.1f}" for y,r in roes), f"| mean {sum(r for _,r in roes)/len(roes)*100:.1f}% | FCF {fcf:,.0f} | capex/DA {cd:.2f} | NI/PPE {sum(rop)/len(rop)*100:.2f}% | issued {iss:,.0f} | dividends {div:,.0f}")
