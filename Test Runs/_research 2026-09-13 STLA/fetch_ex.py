"""Fetch every EX-99 exhibit (htm) of the listed accessions into 6k/ and print the first headline lines."""
import json, sys, os, re, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get, save, strip, CIK

accs = sys.argv[1:]
for acc in accs:
    base = f"https://www.sec.gov/Archives/edgar/data/{int(CIK)}/{acc.replace('-', '')}/"
    d = json.loads(get(base + "index.json"))
    for it in d["directory"]["item"]:
        n = it["name"]
        if not n.endswith(".htm") or "index" in n:
            continue
        if not re.search(r"99|ex|exhibit|press|notice|agenda|bio", n, re.I) or n.startswith("a6k") or n.startswith("a6-kcover"):
            continue
        raw = get(base + n)
        txt = strip(raw)
        out = f"6k/{acc}_{n.replace('.htm', '')}.txt"
        save(out, ("SOURCE " + base + n + " accession " + acc + "\n" + txt).encode("utf-8"))
        lines = [l.strip() for l in txt.splitlines() if len(l.strip()) > 25]
        print("==", acc, n, "|", " / ".join(lines[2:5])[:400])
        time.sleep(0.2)
