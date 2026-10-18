import sys, os, json, time, urllib.request, gzip
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
def get(url, out=None):
    req = urllib.request.Request(url, headers=UA)
    for i in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
            break
        except Exception as e:
            print("retry", e); time.sleep(2)
    else:
        raise SystemExit("failed " + url)
    if out:
        open(out, "wb").write(data)
    time.sleep(0.2)
    return data
if __name__ == "__main__":
    get(sys.argv[1], sys.argv[2])
    print("ok", sys.argv[2])
