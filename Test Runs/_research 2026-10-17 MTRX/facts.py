import json, sys
def annual(path, tags):
    d = json.load(open(path))
    name = d.get("entityName")
    g = d["facts"]["us-gaap"]
    out = {}
    for t in tags:
        if t not in g: continue
        for u, rows in g[t]["units"].items():
            for r in rows:
                if r.get("fp") == "FY" and r.get("form","").startswith("10-K") and "frame" in r and len(r["frame"]) == 6:
                    out.setdefault(r["frame"], {}).setdefault(t, r["val"])
    return name, out
if __name__ == "__main__":
    path = sys.argv[1]; tags = sys.argv[2].split(",")
    name, out = annual(path, tags)
    print(name)
    print("frame  " + "  ".join(t[:22] for t in tags))
    for f in sorted(out):
        print(f, "  ".join(("%12.1f" % (out[f][t]/1e6)) if t in out[f] else "           -" for t in tags))
