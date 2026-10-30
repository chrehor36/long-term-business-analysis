import sys, os, json, time, urllib.request, gzip
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
def get(url, name=None):
    name = name or url.rstrip("/").split("/")[-1]
    p = os.path.join(OUT, name)
    if os.path.exists(p): return p
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip": data = gzip.decompress(data)
    open(p, "wb").write(data); time.sleep(0.3); return p
if __name__ == "__main__":
    for u in sys.argv[1:]:
        print(get(u))
