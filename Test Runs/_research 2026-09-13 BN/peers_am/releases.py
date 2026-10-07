"""Find Q4 earnings-release 8-K (or 6-K for BAM) exhibits in a filing-date window and save them.
usage: releases.py TICKER FORM FROM TO
Saves <TICKER>_REL_<filingdate>_<exhibitname>.txt for EX-99 documents, prints margin hits."""
import sys, os, re, json
from fetch import CIKS, subs, get, totext, OUT

tk, form, d0, d1 = sys.argv[1:5]
r = subs(tk)["filings"]["recent"]
for i in range(len(r["form"])):
    if r["form"][i] != form or not (d0 <= r["filingDate"][i] <= d1):
        continue
    acc = r["accessionNumber"][i]
    a = acc.replace("-", "")
    idx = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{CIKS[tk]}/{a}/index.json"))
    names = [it["name"] for it in idx["directory"]["item"]]
    ex = [n for n in names if re.search(r"(ex|exhibit)[-_]?99", n, re.I) and n.lower().endswith((".htm", ".html"))]
    print(tk, form, r["filingDate"][i], acc, r.get("items", [""] * len(r["form"]))[i], ex)
    for n in ex:
        fn = os.path.join(OUT, f"{tk}_REL_{r['filingDate'][i]}_{re.sub(r'[^A-Za-z0-9]', '', n)[:30]}.txt")
        if not os.path.exists(fn):
            t = totext(get(f"https://www.sec.gov/Archives/edgar/data/{CIKS[tk]}/{a}/{n}").decode("utf-8", "replace"))
            open(fn, "w", encoding="utf-8").write(t)
        t = re.sub(r"\s+", " ", open(fn, encoding="utf-8").read())
        hits = [t[max(0, m.start() - 150):m.end() + 150] for m in re.finditer(r"FRE margin|fee[- ]related earnings margin|FRE Margin", t, re.I)]
        print("   ", os.path.basename(fn), len(t), "margin hits:", len(hits))
        for h in hits[:3]:
            print("      >", h.encode("ascii", "replace").decode())
