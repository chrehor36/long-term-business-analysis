import sys, urllib.request, gzip, os, time
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
def get(url, out):
    if os.path.exists(out) and os.path.getsize(out) > 0:
        return
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    with open(out, "wb") as f:
        f.write(data)
    time.sleep(0.2)
if __name__ == "__main__":
    get(sys.argv[1], sys.argv[2])
