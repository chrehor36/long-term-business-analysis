import sys, urllib.request, gzip, time, os
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
def get(url, out):
    for i in range(4):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)
            d = r.read()
            if r.headers.get("Content-Encoding") == "gzip": d = gzip.decompress(d)
            open(out, "wb").write(d); return len(d)
        except Exception as e:
            print("retry", e); time.sleep(2)
    raise SystemExit("failed " + url)
if __name__ == "__main__":
    print(get(sys.argv[1], sys.argv[2]))
