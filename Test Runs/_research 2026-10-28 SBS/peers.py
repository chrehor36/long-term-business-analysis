import json,urllib.request,time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
peers={'AWK':1410636,'WTRG':78128,'CWT':1035201}
def ann(f,tag):
    out={}
    for u,arr in f['facts']['us-gaap'].get(tag,{}).get('units',{}).items():
        for x in arr:
            if x.get('form')!='10-K': continue
            if 'start' in x:
                s,e=x['start'],x['end']
                if not(s[5:]=='01-01' and e[5:]=='12-31'): continue
            elif x['end'][5:]!='12-31': continue
            y=x['end'][:4]
            if y not in out or x['filed']>out[y][1]: out[y]=(x['val'],x['filed'],x['accn'])
    return out
res={}
for t,c in peers.items():
    f=json.load(urllib.request.urlopen(urllib.request.Request(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json',headers=UA)))
    ni=ann(f,'NetIncomeLoss'); eq=ann(f,'StockholdersEquity')
    rev=ann(f,'Revenues') or ann(f,'RevenueFromContractWithCustomerIncludingAssessedTax')
    oi=ann(f,'OperatingIncomeLoss')
    line=[]
    for y in range(2016,2026):
        y=str(y); py=str(int(y)-1)
        if y in ni and y in eq and py in eq:
            roe=ni[y][0]/((eq[y][0]+eq[py][0])/2)
            line.append(f"{y}:{roe*100:.1f}%")
    accn=sorted({v[2] for v in ni.values()})[-1]
    print(t,' '.join(line),'| latest NI accn',accn)
    time.sleep(0.3)
