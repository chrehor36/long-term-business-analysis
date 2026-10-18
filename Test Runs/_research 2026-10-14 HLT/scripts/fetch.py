import sys, os, time, json, re, urllib.request, gzip
UA = "Chris Hrehor chrehor36@gmail.com"
def get(url, out=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip, deflate"})
    for i in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
                break
        except Exception as e:
            print("retry", e, file=sys.stderr); time.sleep(2)
    else:
        raise SystemExit("fail " + url)
    if out:
        open(out, "wb").write(data)
    time.sleep(0.15)
    return data
if __name__ == "__main__":
    get(sys.argv[1], sys.argv[2])
    print("ok", sys.argv[2], os.path.getsize(sys.argv[2]))
