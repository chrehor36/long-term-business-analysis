"""Step 2c: Clorox incorporates MD&A and Item 8 by reference to Exhibit 99.1 of each 10-K. Fetch those exhibits."""
import json, os, re
from p_common import get, strip, jload, jsave, HERE

m = jload("manifest.json")
for name, v in list(m["CLX"].items()):
    if v["form"] != "10-K" or "EX99" in name:
        continue
    a = v["acc"].replace("-", "")
    ix = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/21076/{a}/index.json"))
    names = [i["name"] for i in ix["directory"]["item"]]
    ex = [n for n in names if re.search(r"ex-?99|exhibit99|ex991", n, re.I) and n.lower().endswith((".htm", ".html"))]
    print(name, v["acc"], ex)
    for n in ex:
        out = name.replace(".txt", f"_EX99_{re.sub(r'[^A-Za-z0-9]', '', n.rsplit('.',1)[0])[:25]}.txt")
        p = os.path.join(HERE, out)
        url = f"https://www.sec.gov/Archives/edgar/data/21076/{a}/{n}"
        if not os.path.exists(p):
            open(p, "w", encoding="utf-8").write(strip(get(url)))
        m["CLX"][out] = dict(form="10-K Exhibit 99.1", filed=v["filed"], period=v["period"], acc=v["acc"], url=url, size=os.path.getsize(p))
        print("  ", out, os.path.getsize(p))
jsave(m, "manifest.json")
