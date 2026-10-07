import sys, os, re, html, json, urllib.request, time
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "tools"))
import sources
OUT = os.path.dirname(os.path.abspath(__file__))

CIKS = {"BAM": 1937926, "BX": 1393818, "KKR": 1404912, "APO": 1858681, "CG": 1527166,
        "ARES": 1176948, "OWL": 1823945, "TPG": 1880661}


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


def subs(tk):
    fn = os.path.join(OUT, f"{tk}_submissions.json")
    if not os.path.exists(fn):
        open(fn, "wb").write(get(f"https://data.sec.gov/submissions/CIK{CIKS[tk]:010d}.json"))
    return json.load(open(fn))


def annual(tk, forms=("10-K", "10-K/A", "20-F", "40-F")):
    r = subs(tk)["filings"]["recent"]
    return [(r["form"][i], r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["reportDate"][i])
            for i in range(len(r["form"])) if r["form"][i] in forms]


def index(tk, acc):
    a = acc.replace("-", "")
    d = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{CIKS[tk]}/{a}/index.json"))
    return [(i["name"], i.get("size")) for i in d["directory"]["item"]]


def grab(tk, acc, doc, name):
    fn = os.path.join(OUT, name + ".txt")
    if os.path.exists(fn):
        print("exists", name); return
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{CIKS[tk]}/{a}/{doc}"
    t = totext(get(url).decode("utf-8", "replace"))
    open(fn, "w", encoding="utf-8").write(t)
    print(name, len(t), "->", url)


if __name__ == "__main__":
    m = sys.argv[1]
    if m == "annual":
        for tk in sys.argv[2:]:
            for x in annual(tk):
                print(tk, *x)
    elif m == "index":
        for x in index(sys.argv[2], sys.argv[3]):
            print(x)
    elif m == "grab":
        grab(*sys.argv[2:6])
    elif m == "forms":
        tk = sys.argv[2]; fm = sys.argv[3]; since = sys.argv[4] if len(sys.argv) > 4 else "0"
        for x in annual(tk, (fm,)):
            if x[1] >= since:
                print(tk, *x)
