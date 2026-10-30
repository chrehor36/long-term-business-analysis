import sys, json, time, urllib.request, gzip, os
UA = "Chris Hrehor chrehor36@gmail.com"
def get(url, out=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    time.sleep(0.2)
    if out:
        open(out, "wb").write(data)
    return data
if __name__ == "__main__":
    url, out = sys.argv[1], sys.argv[2]
    get(url, out); print("ok", out, os.path.getsize(out))
