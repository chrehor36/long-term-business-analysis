"""Fetch helper for the ASML run (2026-10-26). Downloads go to cache/ (git-ignored).
Usage: python -I fetch.py URL OUTNAME   -> writes cache/OUTNAME, prints size.
       python -I fetch.py --text IN OUT -> strips HTML from cache/IN to cache/OUT (plain text).
"""
import sys, os, re, time, html, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
os.makedirs(CACHE, exist_ok=True)
UA = "Chris Hrehor chrehor36@gmail.com"


def get(url, out):
    p = os.path.join(CACHE, out)
    if os.path.exists(p) and os.path.getsize(p) > 0:
        print("cached", p, os.path.getsize(p)); return
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            break
        except Exception as e:
            print("retry", i, e); time.sleep(2 + 3 * i)
    else:
        raise SystemExit("failed " + url)
    with open(p, "wb") as f:
        f.write(data)
    print("wrote", p, len(data))
    time.sleep(0.3)


def to_text(inp, out):
    raw = open(os.path.join(CACHE, inp), "rb").read().decode("utf-8", "replace")
    raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    raw = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>", "\n", raw)
    raw = re.sub(r"(?i)</td>|</th>", " | ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    raw = html.unescape(raw).replace("\xa0", " ")
    raw = re.sub(r"[ \t]+", " ", raw)
    raw = re.sub(r"\n\s*\n+", "\n", raw)
    open(os.path.join(CACHE, out), "w", encoding="utf-8").write(raw)
    print("text", out, len(raw))


if __name__ == "__main__":
    if sys.argv[1] == "--text":
        to_text(sys.argv[2], sys.argv[3])
    else:
        get(sys.argv[1], sys.argv[2])
