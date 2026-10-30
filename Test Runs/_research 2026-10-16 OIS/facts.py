import sys,json,urllib.request,os,time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def facts(cik):
    p=f'cache/facts_{cik}.json'
    if not os.path.exists(p):
        b=urllib.request.urlopen(urllib.request.Request(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json',headers=UA),timeout=120).read()
        open(p,'wb').write(b)
    return json.load(open(p,encoding='utf-8'))
def annual(d,tag,unit='USD',ns='us-gaap'):
    try: arr=d['facts'][ns][tag]['units'][unit]
    except KeyError: return {}
    out={}
    for x in arr:
        if x.get('form') not in ('10-K','20-F','10-K/A','40-F'): continue
        if 'start' in x:
            from datetime import date
            s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
            if not (350<(e-s).days<380): continue
        fy=x['end'][:4]
        # keep the first-filed value for each period end
        if fy not in out or x['filed']<out[fy][1]:
            out[fy]=(x['val'],x['filed'],x['accn'])
    return out
if __name__=='__main__':
    cik=sys.argv[1]; d=facts(cik)
    for tag in sys.argv[2:]:
        a=annual(d,tag)
        print(tag, {k:round(v[0]/1e6,1) for k,v in sorted(a.items())})
