"""Fetch SEC EDGAR documents with a descriptive User-Agent, a polite pace and backoff on HTTP 429.
Usage:
  python fetch.py URL OUTFILE          fetch one URL to OUTFILE (raw, under cache/)
  python fetch.py --text IN.htm OUT.txt  strip an HTML filing to text
"""
import sys, time, urllib.request, urllib.error, re, html, gzip, os

UA = "Long-Term Business Analysis research (contact chrehor36@gmail.com)"


def get(url):
    for attempt in range(1, 10):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
        try:
            r = urllib.request.urlopen(req, timeout=60)
            raw = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                raw = gzip.decompress(raw)
            time.sleep(0.4)
            return raw
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                wait = 15 * attempt
                print(f"  {e.code}; sleeping {wait}s", file=sys.stderr, flush=True)
                time.sleep(wait)
                continue
            raise
    raise RuntimeError("gave up after repeated 429s: " + url)


def to_text(src, dst):
    s = open(src, encoding="utf-8", errors="replace").read()
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>|</th>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    open(dst, "w", encoding="utf-8").write(s)


if __name__ == "__main__":
    if sys.argv[1] == "--text":
        to_text(sys.argv[2], sys.argv[3])
    else:
        os.makedirs(os.path.dirname(sys.argv[2]) or ".", exist_ok=True)
        open(sys.argv[2], "wb").write(get(sys.argv[1]))
        print("ok", sys.argv[2])
