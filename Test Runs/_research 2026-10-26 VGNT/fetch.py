import sys, urllib.request, os, time, gzip
UA = "Chris Hrehor chrehor36@gmail.com"
def get(url, out):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    with open(out, "wb") as f:
        f.write(data)
    print(out, len(data))
    time.sleep(0.3)
if __name__ == "__main__":
    args = sys.argv[1:]
    for i in range(0, len(args), 2):
        get(args[i], args[i+1])
