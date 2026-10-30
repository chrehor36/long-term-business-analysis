"""Fetch an EDGAR filing's documents for PAM (CIK 1469395) and write a text copy of each.
Usage: python -I fetch.py ACCESSION [prefix]
Downloads go to cache/edgar/<accession>/ ; text copies beside them (.txt)."""
import sys, os, json, re, time, html, urllib.request

UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://www.sec.gov/Archives/edgar/data/1469395"


def get(url):
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(req, timeout=60).read()
        except Exception as e:
            time.sleep(2 + 2 * i)
    raise RuntimeError(url)


def to_text(b):
    s = b.decode("utf-8", "ignore")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", s)
    s = re.sub(r"(?i)</td>|</th>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s


def main(acc):
    a = acc.replace("-", "")
    out = os.path.join(HERE, "cache", "edgar", acc)
    os.makedirs(out, exist_ok=True)
    idx = json.loads(get(f"{BASE}/{a}/index.json"))
    for it in idx["directory"]["item"]:
        n = it["name"]
        if not re.search(r"\.(htm|html|txt|pdf)$", n, re.I) or n.endswith("-index.htm") or n.endswith("-index-headers.html"):
            continue
        p = os.path.join(out, n)
        if not os.path.exists(p):
            b = get(f"{BASE}/{a}/{n}")
            open(p, "wb").write(b)
            time.sleep(0.25)
        if re.search(r"\.html?$", n, re.I):
            t = to_text(open(p, "rb").read())
            open(p + ".txt", "w", encoding="utf-8").write(t)
        print(n, os.path.getsize(p))


if __name__ == "__main__":
    for acc in sys.argv[1:]:
        print("==", acc)
        main(acc)
