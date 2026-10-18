"""Fetch helper for the TEX run: SEC EDGAR with the operator's User-Agent; caches to ./cache."""
import sys, os, json, re, time, hashlib, urllib.request, gzip, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
def get(url, binary=False):
    fn = os.path.join(CACHE, hashlib.md5(url.encode()).hexdigest())
    if os.path.exists(fn):
        data = open(fn, "rb").read()
    else:
        for i in range(5):
            try:
                req = urllib.request.Request(url, headers=UA)
                with urllib.request.urlopen(req, timeout=60) as r:
                    data = r.read()
                    if r.headers.get("Content-Encoding") == "gzip":
                        data = gzip.decompress(data)
                break
            except Exception as e:
                print("retry", e, file=sys.stderr); time.sleep(2)
        else:
            raise SystemExit("fail " + url)
        open(fn, "wb").write(data); time.sleep(0.15)
    return data if binary else data.decode("utf-8", "replace")
def text(url):
    h = get(url)
    h = re.sub(r"(?is)<(script|style).*?</\1>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", h)
    h = re.sub(r"(?i)</td>", " | ", h)
    h = re.sub(r"<[^>]+>", " ", h)
    h = html.unescape(h).replace("\xa0", " ")
    h = re.sub(r"[ \t]+", " ", h)
    h = re.sub(r"\n\s*\n+", "\n", h)
    return h
def subs(cik):
    return json.loads(get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"))
if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "list":
        s = subs(sys.argv[2]); r = s["filings"]["recent"]
        forms = sys.argv[3].split(",") if len(sys.argv) > 3 else None
        print(s["name"])
        for i in range(len(r["form"])):
            if forms is None or r["form"][i] in forms:
                print(r["filingDate"][i], r["form"][i], r["accessionNumber"][i], r["primaryDocument"][i], r.get("items", [""]*9999)[i])
    elif cmd == "text":
        out = text(sys.argv[2])
        if len(sys.argv) > 3:
            open(sys.argv[3], "w", encoding="utf-8").write(out); print(len(out))
        else:
            print(out)
    elif cmd == "index":
        cik, acc = sys.argv[2], sys.argv[3].replace("-", "")
        j = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc}/index.json"))
        for it in j["directory"]["item"]:
            print(it["name"], it.get("size"))
