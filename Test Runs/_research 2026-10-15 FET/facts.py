import json, sys, os
here=os.path.dirname(os.path.abspath(__file__))
d=json.load(open(os.path.join(here,'cache',sys.argv[1])))
ns=d['facts']
def annual(tag, taxo='us-gaap', unit='USD'):
    try: u=ns[taxo][tag]['units'][unit]
    except KeyError: return {}
    out={}
    for x in u:
        if x.get('fp')=='FY' and x.get('form','').startswith(('10-K','20-F')) and 'frame' in x or (x.get('form','').startswith(('10-K','20-F')) and x.get('fp')=='FY'):
            s=x.get('start'); e=x['end']
            if s and (int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7]) not in (11,12): continue
            out.setdefault(e[:4], (x['val'], x['accn'], x['filed']))
            # keep earliest filed
            if x['filed'] < out[e[:4]][2]: out[e[:4]]=(x['val'],x['accn'],x['filed'])
    return out
tags=sys.argv[2].split(',')
taxo=sys.argv[3] if len(sys.argv)>3 else 'us-gaap'
res={t:annual(t,taxo) for t in tags}
years=sorted(set(y for r in res.values() for y in r))
print('year,'+','.join(tags))
for y in years:
    print(y+','+','.join(('%.1f'%(res[t][y][0]/1e6)) if y in res[t] else '-' for t in tags))
