import sys, urllib.request, gzip, os, time
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
def get(url, out):
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache", out)
    if os.path.exists(p) and os.path.getsize(p) > 0:
        return p
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    open(p, "wb").write(data)
    time.sleep(0.3)
    return p
if __name__ == "__main__":
    print(get(sys.argv[1], sys.argv[2]))
