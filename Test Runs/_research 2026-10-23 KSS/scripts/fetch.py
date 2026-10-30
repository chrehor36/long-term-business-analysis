import sys, urllib.request, gzip, os, time
UA = "Chris Hrehor chrehor36@gmail.com"
def get(url, out):
    if os.path.exists(out) and os.path.getsize(out) > 0:
        return
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
            open(out, "wb").write(data); time.sleep(0.2); return
        except Exception as e:
            print("retry", url, e); time.sleep(2)
    raise SystemExit("failed " + url)
if __name__ == "__main__":
    for a in range(1, len(sys.argv), 2):
        get(sys.argv[a], sys.argv[a+1])
