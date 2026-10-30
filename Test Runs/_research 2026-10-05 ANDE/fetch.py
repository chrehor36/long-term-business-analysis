import sys, os, time, json, urllib.request, gzip
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
def get(url, out=None):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    if out:
        open(out, "wb").write(data)
    time.sleep(0.15)
    return data
if __name__ == "__main__":
    get(sys.argv[1], sys.argv[2])
