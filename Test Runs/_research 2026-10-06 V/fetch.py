"""Fetch Visa filings from SEC EDGAR into cache/ (gitignored) and strip them to text.
Usage: python fetch.py URL NAME [URL NAME ...]
A descriptive User-Agent with contact is sent; a pause keeps the rate far under EDGAR's limit."""
import os, re, sys, time, html, urllib.request

UA = "Long-term business analysis research chrehor36@gmail.com"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
os.makedirs(CACHE, exist_ok=True)


def fetch(url, name):
    path = os.path.join(CACHE, name)
    if not os.path.exists(path):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        with open(path, "wb") as f:
            f.write(data)
        time.sleep(0.4)
    return path


def to_text(path):
    raw = open(path, "rb").read().decode("utf-8", "replace")
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", raw)
    raw = re.sub(r"(?i)</td>|</th>", " | ", raw)
    raw = re.sub(r"<[^>]+>", " ", raw)
    raw = html.unescape(raw).replace("\xa0", " ")
    raw = re.sub(r"[ \t]+", " ", raw)
    raw = re.sub(r"\n\s*\n+", "\n", raw)
    out = os.path.splitext(path)[0] + ".txt"
    open(out, "w").write(raw)
    return out


if __name__ == "__main__":
    a = sys.argv[1:]
    for url, name in zip(a[::2], a[1::2]):
        p = fetch(url, name)
        if name.endswith((".htm", ".html")):
            print(to_text(p), os.path.getsize(p))
        else:
            print(p, os.path.getsize(p))
