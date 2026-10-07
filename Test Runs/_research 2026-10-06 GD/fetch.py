"""Fetch an EDGAR URL into cache/ with a descriptive User-Agent and backoff on 429/5xx.
Usage: python fetch.py URL OUTNAME"""
import sys, time, urllib.request, urllib.error, os
UA = {"User-Agent": "Long-term business analysis research chrehor36@gmail.com",
      "Accept-Encoding": "identity"}


def get(url, out):
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache", out)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return dest
    delay = 2
    for attempt in range(9):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            open(dest, "wb").write(data)
            time.sleep(0.5)
            return dest
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504):
                print(f"HTTP {e.code}, retry in {delay}s", file=sys.stderr)
                time.sleep(delay); delay = min(delay * 2, 120); continue
            raise
        except Exception as e:
            print(f"{e}, retry in {delay}s", file=sys.stderr)
            time.sleep(delay); delay = min(delay * 2, 120)
    raise SystemExit("gave up: " + url)


if __name__ == "__main__":
    print(get(sys.argv[1], sys.argv[2]))
