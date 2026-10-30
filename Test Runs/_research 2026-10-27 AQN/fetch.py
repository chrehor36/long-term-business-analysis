import sys, os, time, urllib.request, gzip
UA = "Chris Hrehor chrehor36@gmail.com"
def get(url, out):
    if os.path.exists(out) and os.path.getsize(out) > 0:
        return out
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    with open(out, "wb") as f:
        f.write(data)
    time.sleep(0.3)
    return out
if __name__ == "__main__":
    print(get(sys.argv[1], sys.argv[2]))
