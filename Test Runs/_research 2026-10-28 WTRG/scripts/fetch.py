import sys, json, urllib.request, os, time, gzip
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
def get(url, out=None):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    if out:
        open(out, "wb").write(data)
    time.sleep(0.2)
    return data
if __name__ == "__main__":
    url, out = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None
    d = get(url, out)
    if not out: sys.stdout.write(d.decode("utf-8", "replace"))
