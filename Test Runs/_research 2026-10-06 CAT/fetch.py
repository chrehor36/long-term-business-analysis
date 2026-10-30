"""Fetch CAT filings from SEC EDGAR (descriptive User-Agent, under the rate limit).
Usage: python fetch.py OUTDIR url=name [url=name ...]"""
import sys, time, urllib.request, os

UA = "LongTermBusinessAnalysis research chrehor36@gmail.com"
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for arg in sys.argv[2:]:
    url, name = arg.rsplit("=", 1)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    with open(os.path.join(out, name), "wb") as f:
        f.write(data)
    print(name, len(data))
    time.sleep(0.4)
