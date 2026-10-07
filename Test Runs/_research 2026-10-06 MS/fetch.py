"""Fetch MS filings from SEC EDGAR into cache/, with backoff on 429. Usage: python fetch.py URL NAME [URL NAME ...]"""
import sys, time, os, urllib.request, urllib.error, re, html

UA = "LTBA research chrehor36@gmail.com"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
os.makedirs(CACHE, exist_ok=True)


def get(url, name):
    path = os.path.join(CACHE, name)
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return path
    for i in range(8):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
            open(path, "wb").write(data)
            time.sleep(1)
            return path
        except urllib.error.HTTPError as e:
            print(name, e.code, "retry", file=sys.stderr)
            time.sleep(15 * (i + 1))
    raise SystemExit(f"failed {url}")


def to_text(path):
    raw = open(path, "rb").read().decode("utf-8", "replace")
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</(p|div|tr|li|h\d)>", "\n", raw)
    raw = re.sub(r"(?i)</t[dh]>", " | ", raw)
    raw = re.sub(r"<[^>]+>", " ", raw)
    raw = html.unescape(raw).replace("\xa0", " ")
    raw = re.sub(r"[ \t]+", " ", raw)
    raw = re.sub(r"\n\s*\n+", "\n", raw)
    out = path.rsplit(".", 1)[0] + ".txt"
    open(out, "w").write(raw)
    return out


if __name__ == "__main__":
    a = sys.argv[1:]
    for url, name in zip(a[0::2], a[1::2]):
        p = get(url, name)
        if name.endswith((".htm", ".html")):
            print(to_text(p))
        else:
            print(p)
