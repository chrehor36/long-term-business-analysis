"""Fetch an SEC URL into the research cache (cache/ is git-ignored). Usage: python -I fetch.py URL OUTNAME"""
import sys, urllib.request, time, os, gzip
UA = "Chris Hrehor chrehor36@gmail.com"
url, out = sys.argv[1], sys.argv[2]
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
path = os.path.join(base, out)
if not os.path.exists(path):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
            break
        except Exception as e:
            print("retry", i, e, file=sys.stderr); time.sleep(2)
    else:
        sys.exit(1)
    open(path, "wb").write(data)
    time.sleep(0.2)
print(path, os.path.getsize(path))
