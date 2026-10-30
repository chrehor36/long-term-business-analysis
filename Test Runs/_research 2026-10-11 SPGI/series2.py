import json,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
d=json.load(open(sys.argv[1]))["facts"]["us-gaap"]
for t in sys.argv[2:]:
    if t not in d: print(t,"MISSING"); continue
    u=d[t]["units"]; k=list(u)[0]; vals={}
    for f in u[k]:
        if f.get("form")=="10-K" and f.get("fp")=="FY" and f.get("start"):
            s=f["start"];e=f["end"]
            if (int(e[:4])-int(s[:4]))*12+int(e[5:7])-int(s[5:7])<11: continue
            vals.setdefault(e,(f["val"],f["accn"]))
    print(t, {e[:7]:round(v/1e6) for e,(v,a) in sorted(vals.items()) if e>='2014'})
