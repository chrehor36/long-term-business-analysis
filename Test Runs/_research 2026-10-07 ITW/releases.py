# Fetch the EX-99.1 earnings releases named on the command line and print each headline block (guidance trail).
import fetch, json, re, sys
for acc in sys.argv[1:]:
    a = acc.replace("-", "")
    j = json.loads(fetch.get(f"https://www.sec.gov/Archives/edgar/data/49826/{a}/index.json", f"idx_{a}.json"))
    ex = [x["name"] for x in j["directory"]["item"] if re.search(r"ex.?99", x["name"], re.I) and x["name"].endswith(".htm")]
    if not ex: print(acc, "no ex99"); continue
    t = re.sub(r"\s+", " ", open(fetch.doc(49826, acc, ex[0], f"ex99_{a}"), encoding="utf-8").read())
    i = t.find("Exhibit 99.1")
    print("==", acc, t[i:i + 900].encode("ascii", "replace").decode()); print()
