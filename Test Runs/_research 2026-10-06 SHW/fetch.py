"""Fetch SEC EDGAR documents with a descriptive User-Agent; cache under cache/. Rate-limited.
Usage: python fetch.py name=url [name=url ...]   (or bare urls)"""
import sys, time, os, urllib.request
UA = "Long-term business analysis research chrehor36@gmail.com"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
os.makedirs(CACHE, exist_ok=True)


def get(url, name=None):
    name = name or url.rstrip("/").split("/")[-1]
    path = os.path.join(CACHE, name)
    if os.path.exists(path):
        return path
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    with open(path, "wb") as f:
        f.write(data)
    time.sleep(0.25)
    return path


if __name__ == "__main__":
    for a in sys.argv[1:]:
        if "=" in a and not a.startswith("http"):
            n, u = a.split("=", 1)
            print(get(u, n))
        else:
            print(get(a))
