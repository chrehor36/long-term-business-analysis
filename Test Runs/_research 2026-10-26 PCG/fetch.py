"""Fetch SEC JSON/HTML into cache. usage: fetch.py URL NAME"""
import sys, urllib.request, os, time
url, name = sys.argv[1], sys.argv[2]
p = os.path.join(r"C:/Projects/BRK/Test Runs/_research 2026-10-26 PCG/cache", name)
if not os.path.exists(p):
    req = urllib.request.Request(url, headers={"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"})
    data = urllib.request.urlopen(req, timeout=60).read()
    open(p, "wb").write(data); time.sleep(0.2)
print(p, os.path.getsize(p))
