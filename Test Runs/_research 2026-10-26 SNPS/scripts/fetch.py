"""Fetch a URL from SEC EDGAR with the required User-Agent into the cache folder."""
import sys, os, time, urllib.request, gzip
UA = "Chris Hrehor chrehor36@gmail.com"
CACHE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cache")
def fetch(url, name=None):
    name = name or url.rstrip("/").split("/")[-1]
    path = os.path.join(CACHE, name)
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return path
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
            with open(path, "wb") as f:
                f.write(data)
            time.sleep(0.15)
            return path
        except Exception as e:
            print("retry", i, e, file=sys.stderr); time.sleep(2)
    raise SystemExit("failed " + url)
if __name__ == "__main__":
    print(fetch(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))
