import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import get as G
G.HERE = os.path.join(HERE, "k2")
for fd, acc in [("2018-11-02","0001564590-18-026359"),("2018-11-05","0001564590-18-026604"),("2020-10-22","0001564590-20-047153"),("2020-10-26","0001564590-20-047490"),("2020-10-29","0001564590-20-048490"),("2021-11-26","0001564590-21-058378"),("2022-01-27","0001564590-22-002561")]:
    base = f"https://www.sec.gov/Archives/edgar/data/1033767/{acc.replace('-','')}/"
    d = json.loads(G.get(base + "index.json"))
    for it in d["directory"]["item"]:
        n = it["name"]
        if n.lower().endswith((".htm",".txt")) and "index" not in n and not n.startswith(acc):
            G.save_txt(f"{fd}_{acc[-6:]}__{os.path.splitext(n)[0]}.txt", G.get(base + n))
