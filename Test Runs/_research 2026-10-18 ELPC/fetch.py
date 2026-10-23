import sys, urllib.request, gzip, os
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
if __name__ == "__main__":
    get(sys.argv[1], sys.argv[2])
