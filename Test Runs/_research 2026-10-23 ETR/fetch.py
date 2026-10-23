"""Fetch an EDGAR URL to cache/ with the project User-Agent. Usage: python fetch.py URL OUTNAME"""
import sys, urllib.request, gzip, os, time
UA = "Chris Hrehor chrehor36@gmail.com"
url, out = sys.argv[1], sys.argv[2]
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache", out)
req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
for i in range(4):
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                data = gzip.decompress(data)
        break
    except Exception as e:
        print("retry", e); time.sleep(2)
open(path, "wb").write(data)
print(path, len(data))
