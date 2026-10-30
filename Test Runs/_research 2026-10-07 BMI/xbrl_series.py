import json,sys
d=json.load(open(sys.argv[1]))['facts']['us-gaap']
tags=sys.argv[2].split(',')
out={}
for t in tags:
    if t not in d: print('MISSING',t); continue
    for u,vals in d[t]['units'].items():
        for v in vals:
            if v.get('fp')=='FY' and v['form'].startswith('10-K') and ('frame' in v and len(v['frame'])==6 or ('start' not in v)):
                yr=v['end'][:4]
                key=(t,yr)
                if key not in out: out[key]=(v['val'],v['accn'],v['end'])
yrs=sorted({k[1] for k in out})
print('year',*[t[:22] for t in tags],sep=' | ')
for y in yrs:
    print(y,*[(round(out[(t,y)][0]/1e6,1) if (t,y) in out and abs(out[(t,y)][0])>1000 else (out[(t,y)][0] if (t,y) in out else '-')) for t in tags],sep=' | ')
