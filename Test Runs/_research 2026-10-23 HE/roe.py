import json,sys
def series(f,tags,dur=True):
    d=json.load(open(f))['facts']['us-gaap']; out={}; acc={}
    for t in tags:
        if t not in d: continue
        for x in d[t]['units'].get('USD',[]):
            if x.get('form')!='10-K' or x['end'][5:]!='12-31': continue
            if dur and x.get('start','')[5:]!='01-01': continue
            y=x['end'][:4]
            # keep latest-filed value per year (first filed? use earliest accn for first-filed)
            if y not in out or x['accn']<acc[y]:
                out[y]=x['val']; acc[y]=x['accn']
        if out: pass
    return out,acc
names={'0000354707':'HEI','0001004980':'PCG','0000827052':'EIX','0000104918':'AVA'}
for c,n in names.items():
    f='cache/hei_companyfacts.json' if n=='HEI' else f'cache/cf_{c}.companyfacts.json'
    ni,a1=series(f,['NetIncomeLossAvailableToCommonStockholdersBasic','NetIncomeLoss'])
    eq,a2=series(f,['StockholdersEquity'],dur=False)
    row=[]
    for y in range(2016,2026):
        y=str(y); py=str(int(y)-1)
        if y in ni and y in eq and py in eq:
            row.append(f"{y}:{100*ni[y]/((eq[y]+eq[py])/2):.1f}")
        else: row.append(f"{y}:na")
    tot_ni=sum(ni.get(str(y),0) for y in range(2016,2026)); avg_eq=sum(eq.get(str(y),0) for y in range(2016,2026))/10
    print(n, ' '.join(row), f"| 10y sum NI {tot_ni/1e6:.0f}M avg eq {avg_eq/1e6:.0f}M ratio {100*tot_ni/10/avg_eq:.1f}%")
    print('   accns NI', sorted(set(a1.values()))[-3:], 'EQ', sorted(set(a2.values()))[-2:])
