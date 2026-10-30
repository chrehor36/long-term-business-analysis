import sys, os, json, time, urllib.request, gzip
UA = "Chris Hrehor chrehor36@gmail.com"
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
def get(url, name=None):
    name = name or url.rstrip("/").split("/")[-1]
    p = os.path.join(CACHE, name)
    if os.path.exists(p):
        return open(p, "rb").read()
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    for i in range(5):
        try:
            r = urllib.request.urlopen(req, timeout=60)
            b = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                b = gzip.decompress(b)
            open(p, "wb").write(b)
            time.sleep(0.15)
            return b
        except Exception as e:
            print("retry", url, e, file=sys.stderr); time.sleep(2)
    raise SystemExit("failed " + url)
if __name__ == "__main__":
    for u in sys.argv[1:]:
        n = None
        if "=>" in u: u, n = u.split("=>")
        b = get(u, n); print(u, len(b))
