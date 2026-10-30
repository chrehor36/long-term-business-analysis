import json,sys
from datetime import date
def ff(cf,tag,year,instant=False):
    f=cf['facts'].get('us-gaap',{}).get(tag)
    if not f: return None
    for u,v in f['units'].items():
        if u!='USD': continue
        c=[x for x in v if x.get('form')=='10-K' and x.get('fy')==year and x['end'][:4]==str(year) and x['end'][5:]=='12-31']
        if instant: c=[x for x in c if 'start' not in x]
        else: c=[x for x in c if 'start' in x and (date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days>350]
        if c: return c[0]['val']
    return None
if __name__=='__main__':
    cf=json.load(open(sys.argv[1])); y0,y1=int(sys.argv[2]),int(sys.argv[3])
    for t in sys.argv[4:]:
        k,tag=t.split(':',1)
        row=[]
        for y in range(y0,y1+1):
            v=ff(cf,tag,y,k=='i')
            row.append(f"{y%100}:{v/1e6:8.1f}" if v is not None else f"{y%100}:{'-':>8}")
        print(f"{tag[:42]:42s}",' '.join(row))
