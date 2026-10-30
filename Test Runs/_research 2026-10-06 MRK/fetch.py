"""Fetch MRK filings from SEC EDGAR into cache/ (gitignored). Rate-limited, descriptive UA.
Usage: python -I fetch.py subs [forms]     list filings
       python -I fetch.py doc ACC DOC NAME   download one document to cache/NAME and strip it to cache/NAME.txt
       python -I fetch.py index ACC          list a filing's files
"""
import json, sys, time, urllib.request, os, re, html
UA = {"User-Agent": "Long-term business analysis research chrehor36@gmail.com"}
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
os.makedirs(CACHE, exist_ok=True)
CIK = "310158"


def get(url):
    time.sleep(0.25)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def save(url, name):
    p = os.path.join(CACHE, name)
    if not os.path.exists(p):
        open(p, "wb").write(get(url))
    return p


def to_text(p):
    t = open(p, "rb").read().decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    out = p.rsplit(".", 1)[0] + ".txt"
    open(out, "w").write(t)
    return out


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "subs":
        p = save(f"https://data.sec.gov/submissions/CIK{int(CIK):010d}.json", "submissions.json")
        d = json.load(open(p))
        r = d["filings"]["recent"]
        forms = set(sys.argv[2].split(",")) if len(sys.argv) > 2 else None
        for i in range(len(r["form"])):
            if forms and r["form"][i] not in forms:
                continue
            print(r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i])
    elif cmd == "doc":
        acc, doc, name = sys.argv[2], sys.argv[3], sys.argv[4]
        url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-', '')}/{doc}"
        print(to_text(save(url, name)))
    elif cmd == "index":
        acc = sys.argv[2]
        url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-', '')}/index.json"
        d = json.loads(get(url))
        for it in d["directory"]["item"]:
            print(it["name"], it.get("size"))
