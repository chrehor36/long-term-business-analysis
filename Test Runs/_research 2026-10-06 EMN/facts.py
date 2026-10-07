import json,requests,sys,os
H={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
cik=sys.argv[1]; tag=sys.argv[2]
fn=f'facts_{cik}.json'
if not os.path.exists(fn):
    open(fn,'w').write(requests.get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json',headers=H).text)
j=json.load(open(fn))
def annual(tag):
    for ns in ('us-gaap','dei'):
        if tag in j['facts'].get(ns,{}):
            u=j['facts'][ns][tag]['units']
            for unit,vals in u.items():
                d={}
                for v in vals:
                    if v.get('form') in ('10-K','10-K/A') and v.get('fp')=='FY':
                        if 'start' in v:
                            from datetime import date
                            s=date.fromisoformat(v['start']);e=date.fromisoformat(v['end'])
                            if (e-s).days<350: continue
                        y=v['end'][:4]
                        # keep first-filed value
                        if y not in d or v['filed']<d[y][1]: d[y]=(v['val'],v['filed'],v['accn'])
                return unit,d
    return None,{}
for t in tag.split(','):
    unit,d=annual(t)
    print(t,unit,' '.join(f"{y}:{d[y][0]/1e6:.0f}" if isinstance(d[y][0],(int,float)) and abs(d[y][0])>1e5 else f"{y}:{d[y][0]}" for y in sorted(d)))
