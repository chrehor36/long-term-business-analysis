import urllib.request, json, sys, gzip
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
r = urllib.request.urlopen(urllib.request.Request("https://www.sec.gov/files/company_tickers.json", headers=UA), timeout=60)
b = r.read()
if r.headers.get("Content-Encoding") == "gzip":
    b = gzip.decompress(b)
d = json.loads(b)
want = set(sys.argv[1:])
for v in d.values():
    if v["ticker"] in want or any(w.lower() in v["title"].lower() for w in want if len(w) > 5):
        print(v["ticker"], v["cik_str"], v["title"])
