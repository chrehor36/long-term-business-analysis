"""Fetch EDGAR documents into cache/ and strip to text.
Usage: python -I fetch.py <cik> <accession> <docname> [outname]
Raw files and text dumps go to cache/ (gitignored)."""
import sys, os, re, time, urllib.request, html
UA = "Long-term business analysis research chrehor36@gmail.com"
here = os.path.dirname(os.path.abspath(__file__))
cache = os.path.join(here, "cache")
os.makedirs(cache, exist_ok=True)


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def strip(b):
    t = b.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t


if __name__ == "__main__":
    cik, acc, doc = sys.argv[1], sys.argv[2], sys.argv[3]
    out = sys.argv[4] if len(sys.argv) > 4 else doc
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-', '')}/{doc}"
    b = get(url)
    time.sleep(0.3)
    open(os.path.join(cache, out), "wb").write(b)
    if doc.endswith((".htm", ".html", ".txt")):
        open(os.path.join(cache, out + ".dump.txt"), "w").write(strip(b))
    print(url, len(b))
