import sys, os, re, html, json, urllib.request, time
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
OUT = "Test Runs/_research 2026-09-13 RGTI"

def totext(raw):
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
    t = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", t)
    t = re.sub(r"(?i)</t[dh]>", " | ", t)
    t = re.sub(r"(?i)<br[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\u00a0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t

def get(url):
    req = urllib.request.Request(url, headers=sources.SEC_UA)
    err = None
    for k in range(3):
        try:
            return urllib.request.urlopen(req, timeout=120).read().decode("utf-8", "replace")
        except Exception as e:
            err = e; time.sleep(2)
    raise err

def grab(cik, acc, doc, name):
    p = os.path.join(OUT, name + ".txt")
    if os.path.exists(p):
        print("have", name); return
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{doc}"
    raw = get(url)
    t = totext(raw)
    open(p, "w", encoding="utf-8").write(t)
    print(name, len(t), "chars ->", url)
    time.sleep(0.4)

def exhibits(cik, acc):
    a = acc.replace("-", "")
    idx = get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/index.json")
    items = json.loads(idx)["directory"]["item"]
    out = []
    for it in items:
        n = it["name"]
        if n.lower().endswith((".htm", ".html", ".txt")) and "index" not in n:
            print("  ", acc, n, it.get("size"))
            out.append(n)
    return out

MAIN = []
if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "main":
        for args in MAIN:
            try: grab(*args)
            except Exception as e: print("FAIL", args[-1], e)
    elif mode == "idx":
        cik = sys.argv[2]
        for acc in sys.argv[3:]:
            exhibits(cik, acc); time.sleep(0.3)
    elif mode == "one":
        grab(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
