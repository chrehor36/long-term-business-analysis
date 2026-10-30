"""Fetch one EDGAR document for the MMM run.
Usage: python -I fetch.py URL OUTFILE
Descriptive User-Agent with contact; one request per call; sleeps 0.5 s to stay under the SEC rate limit."""
import sys, time, urllib.request

UA = {"User-Agent": "Long-term business analysis run chrehor36@gmail.com"}
url, out = sys.argv[1], sys.argv[2]
req = urllib.request.Request(url, headers=UA)
data = urllib.request.urlopen(req, timeout=60).read()
open(out, "wb").write(data)
time.sleep(0.5)
print(len(data), out)
