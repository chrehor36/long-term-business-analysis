import sys, urllib.request, os, gzip, json, time
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip, deflate"}
def get(url, out=None):
    out = out or os.path.join("cache", url.split("/")[-1] or "index.html")
    if os.path.exists(out): return out
    req = urllib.request.Request(url, headers=UA)
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip": data = gzip.decompress(data)
            break
        except Exception as e:
            print("retry", e); time.sleep(2)
    open(out, "wb").write(data); time.sleep(0.15); return out
if __name__ == "__main__":
    for u in sys.argv[1:]:
        a = u.split("=>"); print(get(a[0], a[1] if len(a)>1 else None))
