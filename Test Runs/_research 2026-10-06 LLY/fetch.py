"""Polite EDGAR fetcher for the LLY run (2026-10-06). Saves raw files under cache/ (gitignored).
usage: python -I fetch.py URL OUTNAME
"""
import sys, time, urllib.request, gzip, os

UA = "LongTermBusinessAnalysis research chrehor36@gmail.com"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
os.makedirs(CACHE, exist_ok=True)


def get(url, out, tries=6):
    for i in range(tries):
        time.sleep(0.6 + i * 3)
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    raw = gzip.decompress(raw)
            with open(os.path.join(CACHE, out), "wb") as f:
                f.write(raw)
            print("OK", out, len(raw))
            return
        except Exception as e:  # noqa
            print("retry", i, e)
    print("FAILED", url)


if __name__ == "__main__":
    get(sys.argv[1], sys.argv[2])
