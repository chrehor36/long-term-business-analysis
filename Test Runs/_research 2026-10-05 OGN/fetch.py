import sys, urllib.request, gzip, time, os
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip, deflate"}
def get(url, out):
    if os.path.exists(out) and os.path.getsize(out) > 0:
        return
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    open(out, "wb").write(data)
    time.sleep(0.15)
if __name__ == "__main__":
    for i in range(1, len(sys.argv), 2):
        get(sys.argv[i], sys.argv[i+1]); print("ok", sys.argv[i+1])
