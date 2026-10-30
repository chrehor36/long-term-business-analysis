import json,sys
d=json.load(open('cache/facts.json'))
want=sys.argv[1:]
for ns in d['facts']:
    for tag,v in d['facts'][ns].items():
        if any(w.lower()==tag.lower() or (w.endswith('*') and w[:-1].lower() in tag.lower()) for w in want):
            for unit,arr in v['units'].items():
                rows={}
                for f in arr:
                    if f.get('fp')=='FY' and f['form']=='10-K' and ('frame' in f or True):
                        st=f.get('start','')
                        en=f['end']
                        if st and (int(en[:4])-int(st[:4])>1 or en[5:7]!='12'): continue
                        if st and not (st[5:7]=='01'): continue
                        rows.setdefault(en,f['val'])
                print(ns,tag,unit,' '.join(f"{k[:4]}:{v/1e6:.1f}" for k,v in sorted(rows.items())))
