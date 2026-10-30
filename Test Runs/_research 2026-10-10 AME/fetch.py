"""Fetch helper for the AME run: SEC EDGAR only, raw files to cache/ (gitignored).
Usage: python fetch.py subs CIK | facts CIK | url URL OUTNAME | text URL OUTNAME
"""
import sys, os, json, time, re, html, urllib.request

UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
os.makedirs(CACHE, exist_ok=True)


def get(url):
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:  # retry
            err = e
            time.sleep(1.5 * (i + 1))
    raise err


def to_text(raw):
    s = raw.decode("utf-8", "replace")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "subs":
        cik = sys.argv[2].zfill(10)
        out = os.path.join(CACHE, f"subs_{cik}.json")
        open(out, "wb").write(get(f"https://data.sec.gov/submissions/CIK{cik}.json"))
        print(out)
    elif cmd == "facts":
        cik = sys.argv[2].zfill(10)
        out = os.path.join(CACHE, f"facts_{cik}.json")
        open(out, "wb").write(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"))
        print(out)
    elif cmd == "url":
        out = os.path.join(CACHE, sys.argv[3])
        open(out, "wb").write(get(sys.argv[2]))
        print(out)
    elif cmd == "text":
        out = os.path.join(CACHE, sys.argv[3])
        open(out, "w", encoding="utf-8").write(to_text(get(sys.argv[2])))
        print(out, os.path.getsize(out))
