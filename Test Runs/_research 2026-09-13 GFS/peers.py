"""Fetch the latest annual report (10-K / 20-F) of GF customers and competitors, stripped to text, into peers/,
then print every paragraph naming GlobalFoundries or a foundry supplier list. Transcription only."""
import sys, os, json, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import get as G
CIKS = {"AMD": 2488, "CRUS": 772406, "NXPI": 1413447, "QCOM": 804328, "SWKS": 4127, "QRVO": 1604778, "HIMX": 1342338,
        "AVGO": 1730168, "ON": 1097864, "LSCC": 855658, "POET": 1437424, "MXL": 1288469, "AMBA": 1280263, "MRVL": 1835632,
        "TSEM": 928876, "INTC": 50863, "NVTS": 1821769, "RMBS": 917273}
which = sys.argv[1:] or list(CIKS)
for tk in which:
    c = CIKS[tk]
    sub = json.loads(G.get(f"https://data.sec.gov/submissions/CIK{c:010d}.json"))
    r = sub["filings"]["recent"]
    idx = [i for i, fm in enumerate(r["form"]) if fm in ("10-K", "20-F")][:1]
    for i in idx:
        acc, doc = r["accessionNumber"][i], r["primaryDocument"][i]
        name = f"{tk}_{r['form'][i]}_{r['reportDate'][i]}_{acc}.txt"
        p = os.path.join(HERE, "peers", name)
        if not os.path.exists(p):
            raw = G.get(f"https://www.sec.gov/Archives/edgar/data/{c}/{acc.replace('-', '')}/{doc}")
            open(p, "w", encoding="utf-8").write(G.strip_html(raw.decode("utf-8", "replace")))
        t = open(p, encoding="utf-8").read()
        print("=====", tk, r["form"][i], r["filingDate"][i], acc)
        seen = set()
        for m in re.finditer(r"(?i)global\s?foundries|\bGF\b(?= )", t):
            s = t.rfind("\n", 0, m.start()); e = t.find("\n", m.end())
            para = t[s + 1:e].strip()
            if para[:80] in seen: continue
            seen.add(para[:80])
            print("  -", para[:1400])
