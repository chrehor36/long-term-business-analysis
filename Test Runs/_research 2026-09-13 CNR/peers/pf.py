import sys, os, re, json, time, urllib.request
BRK = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(BRK, "tools"))
import sources
P = os.path.join(BRK, "Test Runs", "_research 2026-09-13 CNR", "peers")
CACHE = os.path.join(P, "cache")
sys.path.insert(0, os.path.dirname(P))
os.chdir(BRK)
from flat import flatten

def get(url):
    req = urllib.request.Request(url, headers=sources.SEC_UA)
    err = None
    for k in range(4):
        try:
            r = urllib.request.urlopen(req, timeout=120).read().decode("utf-8", "replace")
            time.sleep(0.4); return r
        except Exception as e:
            err = e; time.sleep(3)
    raise err

def listing(tk):
    cik, name = sources.cik_for(tk)
    c10 = str(cik).zfill(10)
    cp = os.path.join(CACHE, f"sub_{tk}.json")
    if os.path.exists(cp): j = json.load(open(cp))
    else:
        j = json.loads(get(f"https://data.sec.gov/submissions/CIK{c10}.json")); json.dump(j, open(cp, "w"))
    r = j["filings"]["recent"]
    out = []
    for i, f in enumerate(r["form"]):
        if f in ("10-K", "10-K/A", "10-Q") and r["reportDate"][i] >= "2021-01-01":
            out.append((f, r["filingDate"][i], r["reportDate"][i], r["accessionNumber"][i], r["primaryDocument"][i]))
    return cik, name, out

def fetch(tk, cik, acc, doc):
    name = f"{tk}_{acc}"
    fp = os.path.join(P, "cache", name + ".flat.txt")
    if os.path.exists(fp): return fp
    raw = get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}")
    open(os.path.join(CACHE, name + ".htm"), "w", encoding="utf-8").write(raw)
    open(fp, "w", encoding="utf-8").write(flatten(raw))
    return fp

if __name__ == "__main__":
    for tk in sys.argv[1:]:
        cik, name, out = listing(tk)
        print(tk, cik, name)
        for o in out: print("  ", *o)
