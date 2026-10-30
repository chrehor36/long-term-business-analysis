# Fetch helper for the ITW run: SEC EDGAR only, with the brief's User-Agent. Saves under cache/ (gitignored).
import sys, os, json, time, re, urllib.request, gzip, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip, deflate"}
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
def get(url, name=None):
    name = name or re.sub(r"[^A-Za-z0-9._-]", "_", url.split("/")[-1])
    p = os.path.join(CACHE, name)
    if os.path.exists(p):
        return open(p, "rb").read()
    req = urllib.request.Request(url, headers=UA)
    for i in range(4):
        try:
            r = urllib.request.urlopen(req, timeout=60); b = r.read()
            if r.headers.get("Content-Encoding") == "gzip": b = gzip.decompress(b)
            open(p, "wb").write(b); time.sleep(0.15); return b
        except Exception as e:
            print("retry", url, e, file=sys.stderr); time.sleep(2)
    raise SystemExit("failed " + url)
def text(b):
    s = b.decode("utf-8", "ignore")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>", "\n", s)
    s = re.sub(r"(?i)</td>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s); s = re.sub(r"\n\s*\n+", "\n", s)
    return s
def subs(cik):
    return json.loads(get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json", f"sub_{cik}.json"))
def filings(cik, forms):
    j = subs(cik); out = []
    def add(rec):
        for f, a, d, p, rd in zip(rec["form"], rec["accessionNumber"], rec["filingDate"], rec["primaryDocument"], rec["reportDate"]):
            if f in forms: out.append((d, f, a, p, rd))
    add(j["filings"]["recent"])
    for extra in j["filings"].get("files", []):
        add(json.loads(get("https://data.sec.gov/submissions/" + extra["name"], f"sub_{cik}_{extra['name']}")))
    return sorted(out)
def doc(cik, acc, prim, name):
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{prim}"
    b = get(url, name)
    t = text(b); tp = os.path.join(CACHE, name + ".txt"); open(tp, "w", encoding="utf-8").write(t); return tp
if __name__ == "__main__":
    cik = sys.argv[1]; forms = sys.argv[2].split(",")
    for r in filings(cik, forms): print(*r)
