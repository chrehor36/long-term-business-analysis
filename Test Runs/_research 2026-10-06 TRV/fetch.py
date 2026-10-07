"""Fetch EDGAR documents for the TRV run into cache/ (gitignored).
The User-Agent declares a contact, per the SEC's fair-access notice; a pause keeps the rate low.
Usage: python -I fetch.py URL OUTFILE
"""
import os
import sys
import time
import urllib.request

UA = "LongTermBusinessAnalysis research run chrehor36@gmail.com"


def get(url, out):
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    if os.path.exists(out) and os.path.getsize(out) > 0:
        return out
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
    with urllib.request.urlopen(req, timeout=90) as r:
        data = r.read()
    with open(out, "wb") as fh:
        fh.write(data)
    time.sleep(0.4)
    return out


if __name__ == "__main__":
    print(get(sys.argv[1], sys.argv[2]))
