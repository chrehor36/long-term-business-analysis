"""Fetch Salesforce filings from SEC EDGAR into cache/ and strip to text. Rate-limited.
Usage: python -I fetch.py ACCESSION:DOCNAME:LABEL ...   (DOCNAME '?' lists the filing's documents)
"""
import sys, time, re, html, urllib.request, json, os
UA = "LongTermBusinessAnalysis research chrehor36@gmail.com"
CIK = "1108524"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    time.sleep(0.4)
    with urllib.request.urlopen(req, timeout=120) as r:
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


def index(acc):
    a = acc.replace("-", "")
    j = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json"))
    return [it["name"] for it in j["directory"]["item"]]


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        acc, name, label = arg.split(":")
        a = acc.replace("-", "")
        if name == "?":
            for n in index(acc):
                print(acc, n)
            continue
        b = get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{name}")
        with open(os.path.join(OUT, label + ".txt"), "w") as f:
            f.write(strip(b))
        print("saved", label, len(b))
