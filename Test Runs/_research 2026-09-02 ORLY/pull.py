#!/usr/bin/env python3
"""ORLY research pull. Fetch only; no judgments. Operator rule 8."""
import json, os, sys, urllib.request, time

OUT = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}

def get(url, headers=UA, name=None, binary=False):
    if name:
        p = os.path.join(OUT, name)
        if os.path.exists(p) and os.path.getsize(p) > 0:
            mode = "rb" if binary else "r"
            kw = {} if binary else {"encoding": "utf-8"}
            with open(p, mode, **kw) as f:
                return f.read()
    req = urllib.request.Request(url, headers=headers)
    for attempt in range(4):
        try:
            data = urllib.request.urlopen(req, timeout=60).read()
            break
        except Exception as e:
            if attempt == 3:
                raise
            time.sleep(2 + attempt * 2)
    if not binary:
        data = data.decode("utf-8", "replace")
    if name:
        p = os.path.join(OUT, name)
        mode = "wb" if binary else "w"
        kw = {} if binary else {"encoding": "utf-8"}
        with open(p, mode, **kw) as f:
            f.write(data)
    return data

if __name__ == "__main__":
    what = sys.argv[1]
    if what == "sub":
        cik = sys.argv[2]
        d = get(f"https://data.sec.gov/submissions/CIK{cik}.json", name=f"sub_{cik}.json")
        j = json.loads(d)
        print(j["name"], j["cik"], j.get("tickers"))
        r = j["filings"]["recent"]
        for i in range(len(r["form"])):
            if r["form"][i] in ("10-K", "10-Q", "8-K", "DEF 14A"):
                print(r["form"][i], r["filingDate"][i], r["accessionNumber"][i],
                      r["primaryDocument"][i], r.get("reportDate", [""] * 999)[i])
    elif what == "facts":
        cik = sys.argv[2]
        get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json", name=f"facts_{cik}.json")
        print("ok")
    elif what == "doc":
        url, name = sys.argv[2], sys.argv[3]
        d = get(url, name=name)
        print(len(d))
