import sys, urllib.request, time, os, gzip
UA = "Chris Hrehor chrehor36@gmail.com"
def get(url):
    for i in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
            with urllib.request.urlopen(req, timeout=60) as r:
                b = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    b = gzip.decompress(b)
                return b
        except Exception as e:
            print("retry", e, file=sys.stderr); time.sleep(2)
    raise SystemExit("failed " + url)
if __name__ == "__main__":
    url, out = sys.argv[1], sys.argv[2]
    b = get(url)
    open(out, "wb").write(b)
    print(out, len(b))
