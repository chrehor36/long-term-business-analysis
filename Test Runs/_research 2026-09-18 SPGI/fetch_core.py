import sys, os, re, html, json, time, urllib.request
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "tools"))
import sources
HERE = os.path.dirname(os.path.abspath(__file__))
CIK = 64040

def get(url):
    for k in range(4):
        try:
            req = urllib.request.Request(url, headers=sources.SEC_UA)
            return urllib.request.urlopen(req, timeout=180).read().decode("utf-8", "replace")
        except Exception as e:
            last = e; time.sleep(2 + 3 * k)
    raise last

def strip(raw):
    t = re.sub(r"(?is)<(script|style|ix:header).*?</\1>", " ", raw)
    t = re.sub(r"(?i)</(td|th)>", " | ", t)
    t = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", t)
    t = re.sub(r"(?i)<br[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\u00a0\u200b]+", " ", t)
    t = re.sub(r"( \| )+( ?\| ?)*", " | ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t

def grab(acc, doc, name, cik=CIK):
    path = os.path.join(HERE, name + ".txt")
    if os.path.exists(path) and os.path.getsize(path) > 1000:
        print("have", name); return
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{doc}"
    raw = get(url); t = strip(raw)
    open(path, "w", encoding="utf-8").write(t)
    print(name, len(t), "chars", url); time.sleep(0.4)

def exhibits(acc, cik=CIK):
    a = acc.replace("-", "")
    idx = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/index.json"))
    return [i["name"] for i in idx["directory"]["item"]]

if __name__ == "__main__":
    which = sys.argv[1]
    sub = json.load(open(os.path.join(HERE, "submissions.json"), encoding="utf-8"))["filings"]["recent"]
    rows = list(zip(sub["form"], sub["filingDate"], sub["reportDate"], sub["accessionNumber"], sub["primaryDocument"], sub["items"]))
    if which == "core":
        for f, fd, rd, acc, doc, it in rows:
            if f == "10-K" and rd >= "2016-12-31":
                grab(acc, doc, f"10-K_FY{rd[:4]}")
            if f == "10-Q" and fd >= "2025-01-01":
                grab(acc, doc, f"10Q_{rd}")
            if f == "DEF 14A" and fd >= "2024-01-01":
                grab(acc, doc, f"DEF14A_{fd[:4]}")
    if which == "8k":
        for f, fd, rd, acc, doc, it in rows:
            if f.startswith("8-K") and fd >= "2021-01-01" and any(x in it for x in ("2.02","8.01","7.01","2.01","1.01","2.05")):
                names = exhibits(acc)
                grab(acc, doc, f"8K_{fd}_{acc[-6:]}_main")
                for n in names:
                    if re.search(r"ex-?99|ex99|exhibit99|dex99", n, re.I) and n.lower().endswith((".htm",".html")):
                        grab(acc, n, f"EX99_{fd}_{acc[-6:]}_{re.sub(r'[^A-Za-z0-9]','',n)[:30]}")
    if which == "s4":
        grab("0001104659-26-082258", "tm2618680-1_s4.htm", "S4_2026-07-09")
