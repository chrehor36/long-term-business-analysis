"""Fetch EDGAR documents with a descriptive User-Agent and backoff on 429. No arithmetic.
Usage: python edgar_fetch.py URL OUTFILE"""
import sys, time, urllib.request, urllib.error

UA = "Long-Term Business Analysis research (contact chrehor36@gmail.com)"


def fetch(url, out):
    delay = 2.0
    for attempt in range(12):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            open(out, "wb").write(data)
            print(f"OK {url} -> {out} ({len(data)} bytes)")
            time.sleep(0.5)
            return
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                print(f"HTTP {e.code}, sleeping {delay:.0f}s")
                time.sleep(delay)
                delay = min(delay * 2, 120)
                continue
            raise
        except Exception as e:
            print(f"error {e}, sleeping {delay:.0f}s")
            time.sleep(delay)
            delay = min(delay * 2, 120)
    raise SystemExit("gave up: " + url)


if __name__ == "__main__":
    fetch(sys.argv[1], sys.argv[2])
