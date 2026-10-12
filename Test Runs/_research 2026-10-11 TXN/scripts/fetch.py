import sys, os, json, time, urllib.request, gzip
UA = "Chris Hrehor chrehor36@gmail.com"
def get(url, out=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    for i in range(4):
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
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "wb").write(data)
    time.sleep(0.2)
    return data
if __name__ == "__main__":
    get(sys.argv[1], sys.argv[2])
