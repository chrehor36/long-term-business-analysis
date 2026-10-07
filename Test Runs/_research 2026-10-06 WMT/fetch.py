"""Fetch WMT filings from SEC EDGAR into cache/ (raw, gitignored) and write stripped text beside them.
Usage: python fetch.py <accession-no-dashes>/<file> <outname> [...pairs]
       python fetch.py --index <accession-no-dashes>
Descriptive User-Agent; sleeps between requests to stay under EDGAR's rate limit."""
import sys, os, time, re, html, json, urllib.request

UA = "LTBA research chrehor36@gmail.com"
BASE = "https://www.sec.gov/Archives/edgar/data/104169/"
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
os.makedirs(CACHE, exist_ok=True)


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    time.sleep(0.4)
    return data


def strip(raw):
    t = raw.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t


args = sys.argv[1:]
if args and args[0] == "--index":
    for acc in args[1:]:
        d = json.loads(get(BASE + acc + "/index.json"))
        print(acc, [i["name"] for i in d["directory"]["item"]])
    sys.exit()
for path, name in zip(args[0::2], args[1::2]):
    raw = get(path if path.startswith("http") else BASE + path)
    open(os.path.join(CACHE, name + ".htm"), "wb").write(raw)
    open(os.path.join(CACHE, name + "_dump.txt"), "w", encoding="utf-8").write(strip(raw))
    print(name, len(raw))
