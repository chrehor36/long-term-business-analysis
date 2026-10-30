import json
d=json.load(open('is_parsed.json')); x=json.load(open('xbrl_series.json'))
S={}
for fy in sorted(d,key=int):
    fy=int(fy); r=d[str(fy)]; sc=1e3 if fy>=2021 else 1e6
    for j in range(len(r['sales'])):
        y=fy-j
        oi=r['oi'][j] if 'oi' in r else r['gm'][j]-r['sga'][j]
        S[y]=dict(sales=r['sales'][j]/sc,gm=r['gm'][j]/sc,oi=oi/sc,tool=(r['tooling'][j]/sc if 'tooling' in r and j<len(r['tooling']) else None),src=fy)
eq={int(k):v/1e6 for k,v in x['StockholdersEquity'].items()}
gw={int(k):v/1e6 for k,v in x['Goodwill'].items()}
ia={int(k):v/1e6 for k,v in x.get('IntangibleAssetsNetExcludingGoodwill',{}).items()}
print('yr  sales  tooling  GM%   OI   OI%   OI/avgEq  OI/avgTangEq')
for y in sorted(S):
    if y<2004: continue
    s=S[y]; e0,e1=eq.get(y-1),eq.get(y)
    roe=rte=''
    if e0 and e1:
        ae=(e0+e1)/2; roe=f"{s['oi']/ae*100:5.1f}%"
        te=ae-(gw.get(y,0)+gw.get(y-1,0))/2-(ia.get(y,0)+ia.get(y-1,0))/2
        rte=f"{s['oi']/te*100:5.1f}%"
    t=f"{s['tool']:6.1f}" if s['tool'] else '   -  '
    print(f"{y} {s['sales']:6.1f} {t} {s['gm']/s['sales']*100:5.1f}% {s['oi']:6.2f} {s['oi']/s['sales']*100:5.1f}% {roe:>8} {rte:>8}")
json.dump(S,open('is_series.json','w'),indent=0)
