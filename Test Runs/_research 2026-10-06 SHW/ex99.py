"""Fetch the EX-99.1 of an 8-K by accession (CIK given), convert to text, print guidance lines.
Usage: python ex99.py CIK ACCESSION [ACCESSION ...]"""
import sys, json, re, subprocess, os
from fetch import get

cik = sys.argv[1]
for acc in sys.argv[2:]:
    a = acc.replace("-", "")
    idx = get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/index.json", f"idx_{a}.json")
    names = [i["name"] for i in json.load(open(idx))["directory"]["item"]]
    cand = [n for n in names if n.endswith(".htm") and ("release" in n.lower() or "ex99" in n.lower() or "ex-99" in n.lower())]
    if not cand:
        print(acc, "no ex99 found", names); continue
    p = get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{cand[0]}", f"{a}_{cand[0]}")
    here = os.path.dirname(os.path.abspath(__file__))
    subprocess.run([sys.executable, os.path.join(here, "h2t.py"), p], check=True, stdout=subprocess.DEVNULL)
    t = open(re.sub(r"\.html?$", ".txt", p), encoding="utf-8").read()
    print("=====", acc, cand[0])
    for line in t.splitlines():
        if re.search(r"guidance|expect.*(per share|sales)|full year 20\d\d", line, re.I) and len(line) < 900:
            print("  ", line.strip()[:600])
