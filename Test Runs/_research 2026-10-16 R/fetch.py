import sys, urllib.request, os, time, gzip
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
def get(url, out):
    if os.path.exists(out): return out
    req = urllib.request.Request(url, headers=UA)
    for i in range(4):
        try:
            r = urllib.request.urlopen(req, timeout=60); data = r.read()
            if r.headers.get("Content-Encoding") == "gzip": data = gzip.decompress(data)
            open(out, "wb").write(data); time.sleep(0.3); return out
        except Exception as e:
            print("retry", e, file=sys.stderr); time.sleep(2)
    raise SystemExit("failed " + url)
if __name__ == "__main__":
    print(get(sys.argv[1], sys.argv[2]))
