import json,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
d=json.load(open("cache/facts.json"))["facts"]["us-gaap"]
tags=sys.argv[1:]
for t in tags:
    if t not in d: print(t,"MISSING"); continue
    u=d[t]["units"]; k=list(u)[0]
    vals={}
    for f in u[k]:
        if f.get("form")=="10-K" and f.get("fp")=="FY":
            s=f.get("start","");e=f["end"]
            if s and (int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7])<11: continue
            # keep first-filed per end date
            vals.setdefault(e,(f["val"],f["accn"]))
    print(t, {e[:4]:round(v/1e6) for e,(v,a) in sorted(vals.items()) if e[5:7]=='12'})
