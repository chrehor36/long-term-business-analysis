"""Fetch EDGAR documents into cache/ (gitignored). Usage: python fetch.py URL OUTNAME [URL OUTNAME ...]
Descriptive User-Agent with contact; sleeps between requests to stay under the SEC rate limit."""
import sys, time, os, urllib.request

UA = "LongTermBusinessAnalysis research chrehor36@gmail.com"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
os.makedirs(CACHE, exist_ok=True)

args = sys.argv[1:]
for url, name in zip(args[::2], args[1::2]):
    out = os.path.join(CACHE, name)
    if os.path.exists(out) and os.path.getsize(out) > 0:
        print("cached", name); continue
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    open(out, "wb").write(data)
    print(name, len(data))
    time.sleep(0.5)
