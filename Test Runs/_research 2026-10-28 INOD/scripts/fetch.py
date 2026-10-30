import sys, urllib.request, os, time, hashlib
UA = "Chris Hrehor chrehor36@gmail.com"
CACHE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cache")
def get(url, name=None):
    name = name or url.rstrip("/").split("/")[-1]
    p = os.path.join(CACHE, name)
    if os.path.exists(p) and os.path.getsize(p) > 0:
        return p
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            with open(p, "wb") as f: f.write(data)
            time.sleep(0.2)
            return p
        except Exception as e:
            print("retry", i, e, file=sys.stderr); time.sleep(2)
    raise SystemExit("failed " + url)
if __name__ == "__main__":
    for a in sys.argv[1:]:
        if "|" in a:
            u, n = a.split("|", 1)
        else:
            u, n = a, None
        print(get(u, n))
