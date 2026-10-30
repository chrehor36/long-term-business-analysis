import json,sys
d=json.load(open('facts_1786431.json'))['facts']['us-gaap']
tags=sys.argv[1:]
for t in tags:
    if t not in d: print(t,'MISSING'); continue
    u=list(d[t]['units'].values())[0]
    out={}
    for x in u:
        if x.get('form')=='10-K' and x.get('fp')=='FY':
            s,e=x.get('start'),x['end']
            if s is None or (int(e[:4])-int(s[:4])==1 or e[5:7]=='12' and s[5:7]=='01'):
                if s and (e[:4]!=s[:4] and not (s[5:]=='12-31' or s[5:]=='01-01')): pass
                key=e
                if s and s[:4]!=e[:4] and s[5:7]!='12': continue
                out.setdefault(key,x['val'])
    print(t.ljust(55),' '.join(f"{k[:4]}:{v/1e6:,.0f}" for k,v in sorted(out.items())))
