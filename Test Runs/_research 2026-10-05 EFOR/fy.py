import json,sys
d=json.load(open(sys.argv[1]))['facts']['us-gaap']
tags=sys.argv[2].split(',')
for t in tags:
    if t not in d: print(t,'MISSING');continue
    u=list(d[t]['units'].values())[0]
    best={}
    for x in u:
        if x.get('fp')=='FY' and x.get('form','').startswith('10-K') and 'frame' in x:
            fr=x['frame']
            if len(fr)==6 or fr.endswith('I'): best[fr]=x['val']
    print(t, {k:round(v/1e6,1) if abs(v)>1e4 else v for k,v in sorted(best.items())})
