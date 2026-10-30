import json,sys
d=json.load(open("cache/facts.json"))["facts"]["us-gaap"]
tags=sys.argv[1:]
for t in tags:
    if t not in d: print(t,"MISSING"); continue
    u=list(d[t]["units"].values())[0]
    out={}
    for f in u:
        if f.get("fp")=="FY" and f.get("form","").startswith("10-K"):
            s=f.get("start","");e=f["end"]
            if s and (int(e[:4])-int(s[:4])>1 or e[5:7]!="12"): continue
            if s and not (s[5:7]=="01" and s[8:10]=="01"): continue
            out.setdefault(e,(f["val"],f["accn"]))
    print(t, " ".join(f"{k[:4]}:{v[0]/1e6:.0f}" for k,v in sorted(out.items()) if k[5:7]=="12"))
