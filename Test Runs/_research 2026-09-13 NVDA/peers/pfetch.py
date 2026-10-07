"""Fetch a peer's newest 10-K / 10-Q primary document from EDGAR (SEC User-Agent, throttled). Usage: pfetch.py CIK TAG [forms]"""
import sys, os, re, html, json, time, urllib.request
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "tools"))
import sources
OUT = os.path.dirname(os.path.abspath(__file__))


def get(url):
    for i in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=sources.SEC_UA), timeout=120).read().decode("utf-8", "replace")
        except Exception as e:
            print("retry", i, e); time.sleep(2 + 2 * i)
    raise RuntimeError(url)


def to_text(raw):
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
    t = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", t)
    t = re.sub(r"(?i)</(td|th)>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\u00a0]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t)


cik, tag = sys.argv[1], sys.argv[2]
forms = sys.argv[3].split(",") if len(sys.argv) > 3 else ["10-Q", "10-K"]
sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"))
r = sub["filings"]["recent"]
done = set()
for i, f in enumerate(r["form"]):
    if f in forms and f not in done:
        done.add(f)
        acc, doc = r["accessionNumber"][i], r["primaryDocument"][i]
        url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-', '')}/{doc}"
        name = f"{tag}_{f.replace('-', '')}_{r['reportDate'][i]}"
        open(os.path.join(OUT, name + ".txt"), "w", encoding="utf-8").write(to_text(get(url)))
        print(name, f, r["filingDate"][i], r["reportDate"][i], acc, doc)
        time.sleep(0.5)
    if len(done) == len(forms):
        break
