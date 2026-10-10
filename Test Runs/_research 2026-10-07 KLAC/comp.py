import json
from series import annual, TAGS, ITAGS
def get(t,U):
    d=json.load(open(f'cache/cf_{t}.json'))
    S={k:annual(d,v,U) for k,v in TAGS.items()}
    I={k:annual(d,v,U,instant=True) for k,v in ITAGS.items()}
    return S,I
def v(D,k,e): x=D[k].get(e); return x[0]/1e6 if x else 0.0
for t,U in [('KLAC','USD'),('AMAT','USD'),('LRCX','USD'),('ONTO','USD'),('NVMI','USD'),('ASML','EUR')]:
    S,I=get(t,U)
    ends=sorted(e for e in S['rev'] if e>='2009-06-01')
    if t=='ONTO': ends=[e for e in ends if e not in ('2017-12-30','2018-12-29')]  # Nanometrics/Rudolph duplicates: keep merged-entity years
    print(f'== {t} ({U}m)  year: rev | pretax+int margin | R&D% | pretax ROTC')
    rows=[]
    for e in ends:
        rev=v(S,'rev',e); ebit=v(S,'pti',e)+v(S,'intexp',e)
        tc=v(I,'equity',e)+v(I,'debt',e)+v(I,'debtc',e)-v(I,'cash',e)-v(I,'mktsec_c',e)-v(I,'mktsec_nc',e)-v(I,'gw',e)-v(I,'intang',e)
        rd=v(S,'rd',e)
        rows.append((e,rev,ebit/rev if rev else 0, rd/rev if rev else 0, ebit/tc if tc>0 else None))
        print(f'  {e} {rev:8.0f} {ebit/rev*100:6.1f}% {rd/rev*100:5.1f}% ', f'{ebit/tc*100:6.0f}%' if tc>0 else '   n/a (tangible capital <=0)')
    m=[r[2] for r in rows]; print(f'  span avg margin {sum(m)/len(m)*100:.1f}%  min {min(m)*100:.1f}% ({rows[m.index(min(m))][0]})  rev CAGR {((rows[-1][1]/rows[0][1])**(1/(len(rows)-1))-1)*100:.1f}%')
