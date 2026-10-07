"""Fetch HON filings from SEC EDGAR into cache/ and strip each to text. Arithmetic-free; transcription only.
Usage: python -I fetch.py ACCESSION DOCUMENT OUTNAME [CIK]
"""
import html, os, re, sys, time, urllib.request

UA = "LTBA research chrehor36@gmail.com"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")


def fetch(acc, doc, out, cik="773840"):
    os.makedirs(CACHE, exist_ok=True)
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{doc}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    raw = urllib.request.urlopen(req, timeout=60).read()
    p = os.path.join(CACHE, out + ".htm")
    open(p, "wb").write(raw)
    t = raw.decode("utf-8", errors="replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", "", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    open(os.path.join(CACHE, out + ".txt"), "w").write(t)
    time.sleep(0.3)
    print(out, len(raw), url)


if __name__ == "__main__":
    a = sys.argv[1:]
    fetch(*a)
