import sys, urllib.request, gzip, os, time
UA = "Chris Hrehor chrehor36@gmail.com"
def get(url, out):
    if os.path.exists(out) and os.path.getsize(out) > 0:
        return out
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    for i in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
            open(out, "wb").write(data)
            time.sleep(0.2)
            return out
        except Exception as e:
            print("retry", i, e, file=sys.stderr); time.sleep(2)
    raise SystemExit("failed " + url)
if __name__ == "__main__":
    print(get(sys.argv[1], sys.argv[2]))
