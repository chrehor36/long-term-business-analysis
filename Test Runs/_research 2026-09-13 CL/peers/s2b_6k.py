"""Step 2b: fetch the half-year 6-K for UL and HLN (the interim after the newest 20-F)."""
import json, os
from p_common import get, strip, jload, jsave, HERE

m = jload("manifest.json")
items = [("UL", 217410, "0000217410-26-000057"), ("HLN", 1900304, "0001104659-26-088450"),
         ("HLN", 1900304, "0001654954-26-007001")]
for t, cik, acc in items:
    a = acc.replace("-", "")
    ix = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/index.json"))
    names = [i["name"] for i in ix["directory"]["item"]]
    print(t, acc, names)
    for n in names:
        if n.lower().endswith((".htm", ".html")) and "index" not in n.lower():
            name = f"{t}_20F-filer_6K_H1-2026_{acc[-6:]}_{n.rsplit('.',1)[0][:30]}.txt"
            p = os.path.join(HERE, name)
            url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{n}"
            if not os.path.exists(p):
                open(p, "w", encoding="utf-8").write(strip(get(url)))
            m[t][name] = dict(form="6-K", filed="2026-07-28" if t == "UL" else "2026-07-30", period="2026-06-30",
                              acc=acc, url=url, size=os.path.getsize(p))
            print("  ", name, os.path.getsize(p))
jsave(m, "manifest.json")
