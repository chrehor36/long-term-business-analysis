"""Fetch an SEC EDGAR URL to the cache folder with a descriptive User-Agent and backoff on 429/503.
Usage: python fetch.py URL OUTNAME"""
import sys, time, urllib.request, urllib.error, os
UA = "Long-Term Business Analysis research chrehor36@gmail.com"
url, out = sys.argv[1], sys.argv[2]
dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache", out)
os.makedirs(os.path.dirname(dest), exist_ok=True)
delay = 2
for attempt in range(9):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        open(dest, "wb").write(data)
        print("ok", len(data), dest)
        time.sleep(0.3)
        sys.exit(0)
    except urllib.error.HTTPError as e:
        if e.code in (429, 503, 403):
            print("http", e.code, "retry in", delay, file=sys.stderr); time.sleep(delay); delay = min(delay * 2, 120)
        else:
            raise
    except Exception as e:
        print("err", e, "retry in", delay, file=sys.stderr); time.sleep(delay); delay = min(delay * 2, 120)
sys.exit(1)
