"""Fetch EDGAR filings for KBR into cache/ (raw, gitignored) and strip to text."""
import sys, json, re, os, time, urllib.request, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
def get(url, binary=False):
    fn = os.path.join(CACHE, re.sub(r"[^A-Za-z0-9._-]", "_", url[-150:]))
    if os.path.exists(fn):
        data = open(fn, "rb").read()
    else:
        for i in range(5):
            try:
                req = urllib.request.Request(url, headers=UA)
                data = urllib.request.urlopen(req, timeout=60).read()
                break
            except Exception as e:
                print("retry", e, file=sys.stderr); time.sleep(2 + i * 3)
        else:
            raise SystemExit("failed " + url)
        open(fn, "wb").write(data); time.sleep(0.2)
    return data if binary else data.decode("utf-8", "replace")
def strip(h):
    h = re.sub(r"(?is)<(script|style).*?</\1>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", h)
    h = re.sub(r"(?i)</td>", " | ", h)
    h = re.sub(r"<[^>]+>", " ", h)
    h = html.unescape(h)
    h = re.sub(r"[ \t\xa0]+", " ", h)
    h = re.sub(r"\n\s*\n+", "\n", h)
    return h
if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "list":
        cik = sys.argv[2]; forms = sys.argv[3].split(",") if len(sys.argv) > 3 else None
        j = json.loads(get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"))
        r = j["filings"]["recent"]
        for i in range(len(r["form"])):
            if forms and r["form"][i] not in forms: continue
            print(r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r.get("items", [""]*99999)[i])
    elif cmd == "doc":
        cik, acc, doc, out = sys.argv[2:6]
        url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
        t = strip(get(url))
        open(os.path.join(CACHE, out), "w", encoding="utf-8").write(t)
        print(out, len(t))
    elif cmd == "index":
        cik, acc = sys.argv[2:4]
        url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/index.json"
        j = json.loads(get(url))
        for it in j["directory"]["item"]: print(it["name"], it.get("size"))
