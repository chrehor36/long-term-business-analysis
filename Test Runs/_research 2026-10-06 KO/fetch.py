"""Fetch EDGAR documents for the KO run. Descriptive User-Agent, spaced requests. Writes to cache/ (gitignored).
Usage: python fetch.py name=url [name=url ...]   or   python fetch.py url
"""
import sys, time, os, urllib.request, urllib.error

UA = "Long-Term Business Analysis research chrehor36@gmail.com"
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
os.makedirs(CACHE, exist_ok=True)


def get(url, name=None):
    name = name or url.rstrip("/").split("/")[-1]
    path = os.path.join(CACHE, name)
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return path
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            break
        except urllib.error.HTTPError as e:
            if e.code != 429 or attempt == 4:
                raise
            time.sleep(15 * (attempt + 1))  # EDGAR asked us to slow down
    with open(path, "wb") as f:
        f.write(data)
    time.sleep(1.0)
    return path


if __name__ == "__main__":
    for a in sys.argv[1:]:
        if "=" in a and not a.startswith("http"):
            n, u = a.split("=", 1)
            print(get(u, n))
        else:
            print(get(a))
