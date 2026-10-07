"""Fetch EDGAR documents for the WFC run with a descriptive UA and backoff on 429.
Usage: python fetch.py URL OUTFILE"""
import sys, time, urllib.request, urllib.error

UA = {"User-Agent": "Long-Term Business Analysis run (Chris Hrehor) chrehor36@gmail.com",
      "Accept-Encoding": "identity"}


def get(url, out):
    for i in range(8):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
            open(out, "wb").write(data)
            print("ok", len(data), out)
            return
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                w = 10 * (i + 1)
                print("HTTP", e.code, "sleep", w)
                time.sleep(w)
                continue
            raise
    sys.exit("gave up " + url)


if __name__ == "__main__":
    get(sys.argv[1], sys.argv[2])
    time.sleep(1)
