"""Step 2: fetch annual filings FY2021+ and the newest interim after the newest annual; companyfacts for 10-K filers."""
import json, os, sys
from p_common import get, strip, jload, jsave, HERE

idx = jload("index.json")
ONLY = sys.argv[1:] or list(idx)


def allrows(t):
    sub = jload(f"{t}_submissions.json")
    cols = ["form", "filingDate", "reportDate", "accessionNumber", "primaryDocument", "primaryDocDescription"]
    rows = []
    def add(r):
        for i in range(len(r["form"])):
            rows.append({c: r[c][i] for c in cols})
    add(sub["filings"]["recent"])
    for fl in sub["filings"].get("files", []):
        if fl["filingTo"] >= "2021-01-01":
            fn = f"{t}_sub_{fl['name']}"
            p = os.path.join(HERE, fn)
            if not os.path.exists(p):
                jsave(json.loads(get("https://data.sec.gov/submissions/" + fl["name"])), fn)
            add(jload(fn))
    return rows


manifest = jload("manifest.json") if os.path.exists(os.path.join(HERE, "manifest.json")) else {}
for t in ONLY:
    cik = idx[t]["cik"]
    rows = allrows(t)
    ann_forms = ("10-K", "10-K/A", "20-F", "20-F/A")
    ann = [r for r in rows if r["form"] in ann_forms and r["reportDate"] >= "2021-01-01"]
    newest = max(r["filingDate"] for r in ann if r["form"] in ("10-K", "20-F"))
    interim = [r for r in rows if r["form"] == "10-Q" and r["filingDate"] > newest]
    interim = sorted(interim, key=lambda r: r["filingDate"])[-1:] if interim else []
    six = []
    if t in ("UL", "HLN"):
        six = [r for r in rows if r["form"] == "6-K" and r["filingDate"] > newest]
    todo = []
    for r in ann:
        tag = r["form"].replace("-", "").replace("/", "")
        todo.append((r, f"{t}_{tag}_FY{r['reportDate'][:4]}_{r['reportDate']}.txt"))
    for r in interim:
        todo.append((r, f"{t}_10Q_{r['reportDate']}.txt"))
    manifest.setdefault(t, {})
    for r, name in todo:
        p = os.path.join(HERE, name)
        a = r["accessionNumber"].replace("-", "")
        url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{r['primaryDocument']}"
        if not (os.path.exists(p) and os.path.getsize(p) > 5000):
            txt = strip(get(url))
            open(p, "w", encoding="utf-8").write(txt)
        manifest[t][name] = dict(form=r["form"], filed=r["filingDate"], period=r["reportDate"],
                                 acc=r["accessionNumber"], url=url, size=os.path.getsize(p))
        print(t, name, r["accessionNumber"], os.path.getsize(p))
    if six:
        jsave(six, f"{t}_6K_list_after_newest_annual.json")
        print(t, "6-K after newest annual:", len(six))
        for r in six:
            print("   ", r["filingDate"], r["accessionNumber"], r["primaryDocument"], r["primaryDocDescription"])
    if t not in ("UL", "HLN"):
        fn = f"{t}_companyfacts.json"
        if not os.path.exists(os.path.join(HERE, fn)):
            jsave(json.loads(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json")), fn)
    jsave(manifest, "manifest.json")
