import sys, urllib.request, gzip, os, time
UA = "Chris Hrehor chrehor36@gmail.com"
def get(url, out):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
            open(out, "wb").write(data); print("ok", out, len(data)); return
        except Exception as e:
            print("retry", e); time.sleep(3)
    print("FAIL", url)
if __name__ == "__main__":
    get(sys.argv[1], sys.argv[2])
