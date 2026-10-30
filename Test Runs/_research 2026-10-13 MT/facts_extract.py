import json,sys
f=json.load(open('cache/companyfacts.json'))['facts']['ifrs-full']
def ann(tag):
    if tag not in f: return {}
    out={}
    for unit,arr in f[tag]['units'].items():
        for x in arr:
            if x.get('form') not in ('20-F','20-F/A'): continue
            if 'start' in x:
                from datetime import date
                d=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days
                if d<340 or d>380: continue
            y=x['end'][:4]
            # keep latest filed
            if y not in out or x['filed']>out[y][1]:
                out[y]=(x['val'],x['filed'],unit)
    return out
if __name__=='__main__':
    for t in sys.argv[1:]:
        a=ann(t)
        print(t, {k:(round(v[0]/1e6),v[2]) for k,v in sorted(a.items())})
