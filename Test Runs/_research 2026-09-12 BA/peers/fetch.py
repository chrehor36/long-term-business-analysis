# -*- coding: utf-8 -*-
import sys, os, re, html, json, urllib.request, time
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
OUT = "Test Runs/_research 2026-09-12 BA/peers"

def latest(cik, forms=("10-K","20-F")):
    txt = sources._get(f"https://data.sec.gov/submissions/CIK{cik}.json", sources.SEC_UA,
                       f"sub_{cik}.json", max_age_h=12)
    d=json.loads(txt); r=d["filings"]["recent"]
    hits=[]
    for i in range(len(r["form"])):
        if r["form"][i] in forms:
            hits.append((r["filingDate"][i], r["reportDate"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["form"][i]))
    return hits

def grab(cik, acc, doc, name):
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{doc}"
    p = os.path.join(OUT, name + ".txt")
    if os.path.exists(p) and os.path.getsize(p) > 50000:
        print("cached", name); return
    raw = urllib.request.urlopen(urllib.request.Request(url, headers=sources.SEC_UA), timeout=120).read().decode("utf-8","replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", t)
    t = re.sub(r"(?i)</(td|th)>", " | ", t)
    t = re.sub(r"(?i)<br[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\u00a0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    open(p,"w",encoding="utf-8").write(t)
    print(name, len(t), "chars <-", url)

if __name__ == "__main__":
    if sys.argv[1] == "list":
        CIKS = {"LMT":"0000936468","NOC":"0001133421","RTX":"0000101829","GD":"0000040533",
                "TXT":"0000217346","TDG":"0001260221","HEI":"0000046619",
                "SPR":"0001364885","ERJ":"0001355444"}
        for tk,cik in CIKS.items():
            print("="*30, tk)
            for h in latest(cik)[:3]: print("  ", h)
