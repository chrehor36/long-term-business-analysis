import json,sys
def annual(cf, tag, unit='USD'):
    f=cf['facts'].get('us-gaap',{}).get(tag)
    if not f: return {}
    out={}
    for u,v in f['units'].items():
        if u!=unit: continue
        for x in v:
            if x.get('form') not in ('10-K','10-K/A'): continue
            if 'frame' in x and not x['frame'].endswith(('I',)) and len(x['frame'])==6:  # CYxxxx duration
                out[x['frame'][2:]]=x['val']
            elif x.get('fp')=='FY' and 'start' not in x:  # instants
                fy=x['end'][:4]
                if x['end'][5:7]=='12': out.setdefault(fy,x['val'])
    return out
def inst(cf,tag,unit='USD'):
    f=cf['facts'].get('us-gaap',{}).get(tag)
    if not f: return {}
    out={}
    for u,v in f['units'].items():
        if u!=unit: continue
        for x in v:
            if x.get('form') in ('10-K','10-K/A') and 'start' not in x and x['end'][5:]=='12-31':
                out.setdefault(x['end'][:4],x['val'])
    return out
if __name__=='__main__':
    cf=json.load(open(sys.argv[1]))
    tags=sys.argv[2:]
    yrs=[str(y) for y in range(2012,2026)]
    for t in tags:
        kind,tag=t.split(':',1)
        d=annual(cf,tag) if kind=='d' else inst(cf,tag)
        print(f"{tag[:45]:45s}", ' '.join(f"{y[2:]}:{d[y]/1e6:8.1f}" if y in d else f"{y[2:]}:{'-':>8s}" for y in yrs))
