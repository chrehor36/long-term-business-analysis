import sys, os, re, html, json, urllib.request, time
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "tools"))
import sources
OUT = os.path.join(ROOT, "Test Runs", "_research 2026-09-13 BAM", "peers")
os.makedirs(OUT, exist_ok=True)

def totext(raw):
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
    t = re.sub(r"(?i)</(p|div|tr|li|h\d|table|br)>", "\n", t)
    t = re.sub(r"(?i)</t[dh]>", " | ", t)
    t = re.sub(r"(?i)<br[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t

def get(url):
    req = urllib.request.Request(url, headers=sources.SEC_UA)
    r = urllib.request.urlopen(req, timeout=180).read()
    time.sleep(0.4)
    return r

tick = json.loads(get("https://www.sec.gov/files/company_tickers.json"))
m = {v["ticker"]: v["cik_str"] for v in tick.values()}
peers = ["BX", "KKR", "APO", "CG", "ARES", "OWL", "TPG", "BLK", "TROW"]
meta = {}
for p in peers:
    cik = m.get(p)
    sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"))
    r = sub["filings"]["recent"]
    hits = [(r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["reportDate"][i])
            for i in range(len(r["form"])) if r["form"][i] == "10-K"]
    hits.sort(reverse=True)
    print(p, cik, sub["name"], hits[:3])
    fd, acc, doc, rd = hits[0]
    meta[p] = dict(cik=cik, name=sub["name"], filingDate=fd, acc=acc, doc=doc, reportDate=rd)
    fn = os.path.join(OUT, f"{p}_10K_FY2025.txt")
    if not os.path.exists(fn):
        raw = get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}").decode("utf-8", "replace")
        t = totext(raw)
        open(fn, "w", encoding="utf-8").write(t)
        print("  saved", len(t))
json.dump(meta, open(os.path.join(OUT, "meta.json"), "w"), indent=1)
