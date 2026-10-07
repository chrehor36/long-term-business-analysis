"""Step 2d: Clorox Exhibit 99.1 (MD&A + financial statements) is the <primary>_d2.htm document in each 10-K."""
import os
from p_common import get, strip, jload, jsave, HERE
m = jload("manifest.json")
for name, v in list(m["CLX"].items()):
    if v["form"] != "10-K":
        continue
    a = v["acc"].replace("-", "")
    doc = v["url"].rsplit("/", 1)[1].replace(".htm", "_d2.htm")
    url = f"https://www.sec.gov/Archives/edgar/data/21076/{a}/{doc}"
    out = name.replace(".txt", "_EX991_d2_MDA_and_financials.txt")
    p = os.path.join(HERE, out)
    if not os.path.exists(p):
        open(p, "w", encoding="utf-8").write(strip(get(url)))
    m["CLX"][out] = dict(form="10-K Exhibit 99.1", filed=v["filed"], period=v["period"], acc=v["acc"], url=url, size=os.path.getsize(p))
    print(out, os.path.getsize(p))
jsave(m, "manifest.json")
