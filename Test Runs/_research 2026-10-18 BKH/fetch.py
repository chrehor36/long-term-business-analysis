import sys, urllib.request, gzip, os, time
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
def get(url, out):
    req = urllib.request.Request(url, headers=UA)
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
            open(out, "wb").write(data); return len(data)
        except Exception as e:
            print("retry", e); time.sleep(2)
    raise SystemExit("failed " + url)
if __name__ == "__main__":
    print(get(sys.argv[1], sys.argv[2]))
