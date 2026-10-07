import json, sys
d=json.load(open("companyfacts.json"))
def show(tag, taxo="us-gaap", annual_only=False):
    node=d["facts"].get(taxo,{}).get(tag)
    if not node:
        print("== %s : ABSENT"%tag); return
    print("== %s (%s)"%(tag, node.get("label")))
    for unit, arr in node["units"].items():
        seen={}
        for f in arr:
            key=(f.get("start"), f.get("end"))
            # keep latest filed vintage AND report all vintages count
            seen.setdefault(key, []).append(f)
        for key in sorted(seen, key=lambda k:(k[1] or "", k[0] or "")):
            vs=seen[key]
            vals=sorted({(v["val"], v["form"], v["fy"], v["fp"], v["filed"], v.get("frame","")) for v in vs}, key=lambda x:x[4])
            start,end=key
            if annual_only and start and (int(end[:4])*12+int(end[5:7]) - (int(start[:4])*12+int(start[5:7]))) < 11: continue
            for v in vals:
                print("   {} -> {}  {}  {:>18}  {} {} {} filed {} {}".format(start,end,unit,format(v[0],","),v[1],v[2],v[3],v[4],v[5]))
for t in sys.argv[1:]:
    ann = t.endswith("!")
    show(t.rstrip("!"), annual_only=ann)
