import sys, urllib.request, json, gzip, os
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
def get(url, out=None):
    r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)
    b = r.read()
    if r.headers.get("Content-Encoding") == "gzip": b = gzip.decompress(b)
    if out:
        open(out, "wb").write(b)
    return b
if __name__ == "__main__":
    url, out = sys.argv[1], sys.argv[2]
    get(url, out); print(out, os.path.getsize(out))
