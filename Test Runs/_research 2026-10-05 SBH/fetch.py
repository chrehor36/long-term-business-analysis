import sys, json, os, time, re, html
import urllib.request
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()
def text_of(raw):
    s = raw.decode("utf-8", errors="replace")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "sub":
        cik = sys.argv[2]; out = sys.argv[3]
        raw = get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json")
        open(out, "wb").write(raw)
    elif mode == "doc":
        url = sys.argv[2]; out = sys.argv[3]
        raw = get(url)
        open(out, "w", encoding="utf-8").write(text_of(raw))
    elif mode == "raw":
        url = sys.argv[2]; out = sys.argv[3]
        open(out, "wb").write(get(url))
