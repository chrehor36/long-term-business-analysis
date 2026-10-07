"""Fetch JNJ filings from SEC EDGAR into cache/ and strip each to text. Run from the research folder.
Usage: python -I fetch.py <accession-no-dashes>/<doc> <outname> [...]
       python -I fetch.py --index <accession-no-dashes>
"""
import sys, os, re, time, html, json, urllib.request

UA = "LTBA research chrehor36@gmail.com"
BASE = "https://www.sec.gov/Archives/edgar/data/200406/"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
os.makedirs(CACHE, exist_ok=True)


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    time.sleep(0.25)
    return data


def strip(raw):
    t = raw.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t


args = sys.argv[1:]
if args and args[0] == "--index":
    for acc in args[1:]:
        d = json.loads(get(BASE + acc + "/index.json"))
        print(acc, [x["name"] for x in d["directory"]["item"]])
else:
    for i in range(0, len(args), 2):
        path, out = args[i], args[i + 1]
        raw = get(BASE + path)
        open(os.path.join(CACHE, out + ".htm"), "wb").write(raw)
        open(os.path.join(CACHE, out + ".txt"), "w").write(strip(raw))
        print(out, len(raw))
