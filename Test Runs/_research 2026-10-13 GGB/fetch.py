import sys, os, time, urllib.request, gzip
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
def get(url, out):
    out = os.path.join("cache", out)
    if os.path.exists(out):
        return out
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    open(out, "wb").write(data)
    time.sleep(0.3)
    return out
if __name__ == "__main__":
    print(get(sys.argv[1], sys.argv[2]))
