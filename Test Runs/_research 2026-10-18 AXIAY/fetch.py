import sys, urllib.request, gzip, os
UA = "Chris Hrehor chrehor36@gmail.com"
def get(url, out=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    if out:
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        open(out, "wb").write(data)
    return data
if __name__ == "__main__":
    d = get(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    if len(sys.argv) <= 2:
        sys.stdout.write(d.decode("utf-8", "replace"))
